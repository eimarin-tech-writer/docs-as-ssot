#!/usr/bin/env python3
"""
check_ssot.py: a deterministic checker for an ssot.md against its transcript.

Usage:
    python3 tools/check_ssot.py project/docs/ssot.example.md project/raw/nimbus-meeting.txt

What it checks (presence and match only, not meaning):
  G-01  every row has a location [hh:mm:ss] that exists in the transcript and a
        quote that appears verbatim on that line
  G-02  the owner appears only if named on the cited line (or the speaker
        commits themselves, "I'll send..."); otherwise it must be "unnamed"
  G-03  a hedge ("I think", "roughly", "no promises") must not become
        "verified" without an uncertainty marker in the claim
  --    the speaker in the table is the speaker of the cited line

What it cannot check: whether the quote really supports the claim (discussion
vs decision), whether something is missing from the table, whether a figure was
corrected later. That is the job of the Verifier agent and of the human.

Language: the hedge and commitment lists below are English. For another
language, replace HEDGES, MARKERS and COMMITMENT.

Exit code: 0 = pass / pass with conditions, 1 = fail. Standard library only.
"""
import re
import sys
import unicodedata

TYPES = {"fact", "decision", "action", "open question", "risk"}
STATUSES = {"verified", "inferred", "unconfirmed"}
HEDGES = ["i think", "i guess", "maybe", "perhaps", "probably", "might",
          "roughly", "around", "no promises", "can t promise", "not sure",
          "hopefully", "i believe"]
MARKERS = ["approximately", "roughly", "around", "probably", "estimate",
           "no guarantee", "to be confirmed", "tbc", "tentative", "uncertain",
           "unconfirmed"]
COMMITMENT = re.compile(r"\bi (ll|will|can take|can send|can handle)\b")
LINE = re.compile(r"^\[(\d\d:\d\d:\d\d)\]\s*(?:([^:\[\]]{1,40}):\s*)?(.*)$")
NO_VALUE = {"", "-", "—", "–", "n/a", "unnamed"}


def norm(text):
    """Lowercase, no diacritics or punctuation, collapsed spaces."""
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def read_transcript(path):
    lines = {}
    with open(path, encoding="utf-8") as f:
        for raw in f:
            m = LINE.match(raw.strip())
            if m:
                loc, speaker, text = m.groups()
                lines[loc] = (speaker.strip() if speaker else None, text)
    return lines


def read_ssot(path):
    rows = []
    header = None
    with open(path, encoding="utf-8") as f:
        for raw in f:
            raw = raw.strip()
            if not raw.startswith("|"):
                continue
            cells = [c.strip() for c in raw.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            if header is None:
                names = [norm(c) for c in cells]
                if "id" in names and "quote" in names:
                    header = names
                continue
            rows.append(dict(zip(header, cells)))
    return rows


def clean_quote(q):
    return q.strip().strip('„”"«»“”').strip()


def check(rows, transcript):
    findings = []  # (id, severity, rule, message)
    seen = set()
    for r in rows:
        rid = r.get("id", "?")
        kind = norm(r.get("type", ""))
        status = norm(r.get("status", ""))
        claim = r.get("claim", "")
        speaker = r.get("speaker", "")
        owner = r.get("owner", "")
        quote = clean_quote(r.get("quote", ""))
        loc = r.get("location", "").strip()

        if rid in seen:
            findings.append((rid, "medium", "-", "duplicate ID"))
        seen.add(rid)
        if kind not in TYPES:
            findings.append((rid, "medium", "-", f"unknown type: '{r.get('type', '')}'"))
        if status not in STATUSES:
            findings.append((rid, "medium", "-", f"unknown status: '{r.get('status', '')}'"))

        # G-01: source
        if not quote or not loc:
            findings.append((rid, "critical", "G-01", "row without a quote or a location in the transcript"))
            continue
        if loc not in transcript:
            findings.append((rid, "critical", "G-01", f"location {loc} does not exist in the transcript"))
            continue
        line_speaker, line_text = transcript[loc]
        if norm(quote) not in norm(line_text):
            findings.append((rid, "critical", "G-01",
                             f"the quote does not appear on line {loc} (possibly invented)"))
            continue

        # speaker
        if norm(speaker) not in {norm(v) for v in NO_VALUE}:
            if line_speaker is None:
                findings.append((rid, "medium", "-",
                                 f"line {loc} has no speaker label: attribution cannot be verified"))
            elif norm(speaker) != norm(line_speaker):
                findings.append((rid, "critical", "attribution",
                                 f"wrong speaker: table says {speaker}, line {loc} is {line_speaker}"))

        # G-02: owner
        if norm(owner) not in {norm(v) for v in NO_VALUE}:
            name = norm(owner)
            named = name in norm(line_text)
            self_commit = (
                line_speaker is not None and norm(line_speaker) == name
                and COMMITMENT.search(norm(line_text)) is not None
            )
            if not (named or self_commit):
                findings.append((rid, "critical", "G-02",
                                 f"owner {owner} is not named on line {loc}"))

        # G-03: hedge turned into certainty
        n_quote = norm(quote)
        has_hedge = any(re.search(rf"\b{re.escape(h)}\b", n_quote) for h in HEDGES)
        has_marker = any(m in norm(claim) for m in MARKERS)
        if has_hedge and status == "verified" and not has_marker:
            findings.append((rid, "critical", "G-03",
                             "the quote contains a hedge, but the claim is 'verified' with no uncertainty marker"))
    return findings


def decide(findings):
    n = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for _, sev, _, _ in findings:
        n[sev] = n.get(sev, 0) + 1
    if n["critical"] > 0:
        return "FAIL", n
    if n["high"] > 2:
        return "FAIL", n
    if n["high"] >= 1:
        return "PASS WITH CONDITIONS", n
    return "PASS", n


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    ssot, transcript = argv[1], argv[2]
    rows = read_ssot(ssot)
    if not rows:
        print("No rows found in the SSOT table. Check the header (ID | Type | ... | Quote | Location | Status).")
        return 2
    findings = check(rows, read_transcript(transcript))
    for rid, sev, rule, msg in findings:
        print(f"[{sev.upper():8}] {rid:6} {rule:11} {msg}")
    verdict, n = decide(findings)
    print(f"\n{len(rows)} rows checked. critical={n['critical']} high={n['high']} "
          f"medium={n['medium']} low={n['low']}")
    print(f"Verdict: {verdict}")
    print("Remember: the script checks presence and match, not meaning. The Verifier and you do the rest.")
    return 1 if verdict == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
