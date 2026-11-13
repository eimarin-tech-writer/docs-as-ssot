# AGENTS.md: project rules

Read this file before any task. It applies to every agent, in every tool.

## The golden rule

**No claim without a source.** Every decision, action, figure or name in the output points to a place in `project/raw/`, with a quote that appears there verbatim. What cannot be traced is not stated. You write "not in the source".

## Where things live

| Folder | Contains | Who writes |
|---|---|---|
| `project/raw/` | raw sources (transcript, document) | the human, never an agent |
| `project/docs/` | `ssot.md`, `spec.md`, `style-guide.md` | the human, with agents |
| `project/output/` | deliverables (minutes, materials) | the Generator agent |
| `qa/` | severity, finding cards, tests, reports | the Verifier and the human |
| `agents/` | the instructions for each agent | the human |

## Working rules

1. **Whoever generates does not verify.** The Generator and the Verifier are separate conversations. The Verifier receives the source, the output and the criteria, not the Generator's reasoning.
2. **Inputs are what is attached.** Nothing from the model's memory, nothing from other meetings or documents that are not in `project/raw/`.
3. **A hedge stays a hedge.** "I think Friday" does not become "deadline: Friday". Write "probably Friday, to be confirmed".
4. **A discussion is not a decision.** "Decided" only if someone explicitly decided.
5. **The owner appears only if named.** Otherwise: "unnamed".
6. **The human decides.** Finding cards inform the decision; they do not make it.

## The enforced rule (not just written)

`tools/check_ssot.py` checks any `ssot.md`: the quote appears verbatim on the cited line, the speaker and owner match, a hedge does not become certainty. Run it after every extraction. If it fails, do not go further.

The script checks presence and match, not meaning. The Verifier agent checks meaning, and the final decision is the human's.

## Severity (summary; details in `qa/severity.md`)

| Level | When | Decision |
|---|---|---|
| critical | the reader is misled without knowing it | fail |
| high | a decision or an action is lost | at most 2, with conditions |
| medium | wording, tone, structure | recommendation |
| low | cosmetic | note |
