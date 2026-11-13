#!/usr/bin/env python3
"""
check_ssot.py: verificator determinist pentru un ssot.md față de transcript.

Folosire:
    python3 tools/check_ssot.py project/docs/ssot.exemplu.md project/raw/sedinta-nimbus.txt

Ce verifică (doar prezența și potrivirea, nu sensul):
  G-01  fiecare rând are un loc [hh:mm:ss] care există în transcript și un citat
        care apare întocmai pe linia aceea
  G-02  responsabilul apare doar dacă e numit în linia citată (sau vorbește la
        persoana I despre sine); altfel trebuie să fie „nenumit"
  G-03  o ezitare („cred că", „vreo", „nu garantez") nu devine „verificat" fără
        un marcaj de incertitudine în afirmație
  --    vorbitorul din tabel este vorbitorul liniei citate

Ce NU poate verifica: dacă citatul susține cu adevărat afirmația (discuție vs
decizie), dacă ceva lipsește din tabel, dacă o cifră a fost corectată mai târziu.
Asta rămâne în sarcina agentului Verificator și a omului.

Exit code: 0 = trece / trece cu condiții, 1 = pică. Doar biblioteca standard.
"""
import re
import sys
import unicodedata

TIPURI = {"fapt", "decizie", "actiune", "intrebare deschisa", "risc"}
STATUSURI = {"verificat", "dedus", "neconfirmat"}
HEDGE = ["cred", "poate", "probabil", "vreo", "nu garantez", "nu sunt sigur", "parca"]
MARKERE = ["aproximativ", "probabil", "estim", "fara garantie", "de confirmat",
           "aproape", "circa", "incert"]
PERSOANA_I = re.compile(r"\b(eu|trimit|iau|inchid|fac|rezolv|ma ocup)\b")
LINIE = re.compile(r"^\[(\d\d:\d\d:\d\d)\]\s*(?:([^:\[\]]{1,40}):\s*)?(.*)$")
FARA_VALOARE = {"", "-", "—", "–", "n/a", "nenumit"}


def norm(text):
    """Litere mici, fără diacritice și punctuație, spații comprimate."""
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def citeste_transcript(cale):
    linii = {}
    with open(cale, encoding="utf-8") as f:
        for brut in f:
            m = LINIE.match(brut.strip())
            if m:
                loc, vorbitor, text = m.groups()
                linii[loc] = (vorbitor.strip() if vorbitor else None, text)
    return linii


def citeste_ssot(cale):
    randuri = []
    antet = None
    with open(cale, encoding="utf-8") as f:
        for brut in f:
            brut = brut.strip()
            if not brut.startswith("|"):
                continue
            celule = [c.strip() for c in brut.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in celule if c):
                continue
            if antet is None:
                if "id" in [norm(c) for c in celule] and "citat" in [norm(c) for c in celule]:
                    antet = [norm(c) for c in celule]
                continue
            randuri.append(dict(zip(antet, celule)))
    return randuri


def curata_citat(c):
    return c.strip().strip('„”"«»“”').strip()


def verifica(randuri, transcript):
    constatari = []  # (id, severitate, regula, mesaj)
    vazute = set()
    for r in randuri:
        rid = r.get("id", "?")
        tip = norm(r.get("tip", ""))
        status = norm(r.get("status", ""))
        afirmatie = r.get("afirmatie", "")
        vorbitor = r.get("vorbitor", "")
        responsabil = r.get("responsabil", "")
        citat = curata_citat(r.get("citat", ""))
        loc = r.get("loc", "").strip()

        if rid in vazute:
            constatari.append((rid, "mediu", "-", "ID duplicat"))
        vazute.add(rid)
        if tip not in TIPURI:
            constatari.append((rid, "mediu", "-", f"tip necunoscut: „{r.get('tip', '')}”"))
        if status not in STATUSURI:
            constatari.append((rid, "mediu", "-", f"status necunoscut: „{r.get('status', '')}”"))

        # G-01: sursă
        if not citat or not loc:
            constatari.append((rid, "critic", "G-01", "rând fără citat sau fără loc în transcript"))
            continue
        if loc not in transcript:
            constatari.append((rid, "critic", "G-01", f"locul {loc} nu există în transcript"))
            continue
        vorb_linie, text_linie = transcript[loc]
        if norm(citat) not in norm(text_linie):
            constatari.append((rid, "critic", "G-01",
                               f"citatul nu apare pe linia {loc} (posibil inventat)"))
            continue

        # vorbitor
        if norm(vorbitor) not in {norm(v) for v in FARA_VALOARE}:
            if vorb_linie is None:
                constatari.append((rid, "mediu", "-",
                                   f"linia {loc} nu are etichetă de vorbitor: atribuirea nu se poate verifica"))
            elif norm(vorbitor) != norm(vorb_linie):
                constatari.append((rid, "critic", "atribuire",
                                   f"vorbitor greșit: tabelul spune {vorbitor}, linia {loc} e a lui {vorb_linie}"))

        # G-02: responsabil
        if norm(responsabil) not in {norm(v) for v in FARA_VALOARE}:
            nume = norm(responsabil)
            in_text = nume in norm(text_linie)
            vorbeste_despre_sine = (
                vorb_linie is not None and norm(vorb_linie) == nume
                and PERSOANA_I.search(norm(text_linie)) is not None
            )
            if not (in_text or vorbeste_despre_sine):
                constatari.append((rid, "critic", "G-02",
                                   f"responsabilul {responsabil} nu e numit în linia {loc}"))

        # G-03: ezitare devenită certitudine
        n_citat = norm(citat)
        are_ezitare = any(re.search(rf"\b{re.escape(h)}\b", n_citat) for h in HEDGE)
        are_marcaj = any(m in norm(afirmatie) for m in MARKERE)
        if are_ezitare and status == "verificat" and not are_marcaj:
            constatari.append((rid, "critic", "G-03",
                               "citatul conține o ezitare, dar afirmația e „verificat” fără marcaj de incertitudine"))
    return constatari


def decizie(constatari):
    n = {"critic": 0, "ridicat": 0, "mediu": 0, "scazut": 0}
    for _, sev, _, _ in constatari:
        n[sev] = n.get(sev, 0) + 1
    if n["critic"] > 0:
        return "PICĂ", n
    if n["ridicat"] > 2:
        return "PICĂ", n
    if n["ridicat"] >= 1:
        return "TRECE CU CONDIȚII", n
    return "TRECE", n


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    ssot, transcript = argv[1], argv[2]
    randuri = citeste_ssot(ssot)
    if not randuri:
        print("Nu am găsit niciun rând în tabelul SSOT. Verifică antetul (ID | Tip | ... | Citat | Loc | Status).")
        return 2
    constatari = verifica(randuri, citeste_transcript(transcript))
    for rid, sev, regula, mesaj in constatari:
        print(f"[{sev.upper():7}] {rid:6} {regula:9} {mesaj}")
    verdict, n = decizie(constatari)
    print(f"\n{len(randuri)} rânduri verificate. critic={n['critic']} ridicat={n['ridicat']} "
          f"mediu={n['mediu']} scăzut={n['scazut']}")
    print(f"Verdict: {verdict}")
    print("Reține: scriptul verifică prezența și potrivirea, nu sensul. Restul face Verificatorul și tu.")
    return 1 if verdict == "PICĂ" else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
