# Docs as SSOT: working with AI so it stays in the source

A working repo for the mentoring track **Get AI Conversations Right** (Product Makers Romania). It is not a tutorial. It is a small project with rules, agents, tests and a verifier that actually runs. You clone it, use it in every session, and keep it.

The idea: AI writes well, but it invents, interprets and forgets instructions. Instead of checking everything by hand, you **anchor** the output in a single source of truth (SSOT), **write down in advance** what you want, **test** that your rules hold, and **separate** who generates from who verifies.

**Who it's for:** people who already use AI at work and want to be able to trust what comes out. No coding required. It needs Python 3 for a single script.

## Quickstart

```
git clone https://github.com/eimarin-tech-writer/docs-as-ssot.git
cd docs-as-ssot
python3 tools/check_ssot.py project/docs/ssot.example.md project/raw/nimbus-meeting.txt
```

If you see `Verdict: PASS`, you are ready. Then open `exercises/MIN-101-setup.md`.

No Python? You can do everything with the agents, in any tool, and skip the script. You lose the deterministic quote check, so run the Verifier with extra care. See `docs/tools.md`.

## What's inside

| Piece | Where | What it teaches |
|---|---|---|
| Project rule | `AGENTS.md` | what no agent may forget |
| Practice source | `project/raw/nimbus-meeting.txt` | a fictional transcript with the traps of real meetings |
| SSOT | `project/docs/ssot.*.md` | what an anchored claim looks like |
| Specification | `project/docs/spec.template.md` | how to write what you want before generating |
| Style guide | `project/docs/style-guide.md` | a fictional content guide (Nimbus): voice, tone by moment, patterns, terms, 17 numbered rules |
| Agents | `agents/` | paste-ready instructions: Extractor, Generator, Verifier, Spec author, Style checker |
| QA | `qa/` | severity, finding card, tests, report |
| Automatic verifier | `tools/check_ssot.py` | a rule that is enforced, not just written |
| Exercises | `exercises/` | one ticket per step, with acceptance criteria |

## The exercises

Each exercise is a ticket: a story, steps with a check after each one, and acceptance criteria. The work is done when every criterion is met.

| Ticket | Session | Where you start | What you produce |
|---|---|---|---|
| `MIN-101` | 1 | "Does my setup work?" | the verifier run on the example |
| `MIN-102` | 2 | "I don't trust what comes out" | an `ssot.md` from the transcript |
| `MIN-103` | 2 | "How do I catch what I didn't see?" | findings on a planted SSOT |
| `MIN-104` | at home | "What does the perfect document look like?" | your source + a golden output |
| `MIN-105` | 3 | "It does something other than what I asked" | `spec.md` + `tests.md` + report |
| `MIN-106` | at home | "A rule failed" | a rewritten rule + a second run |
| `MIN-107` | 4 | "It doesn't sound the same every time" | `style-guide.md` + a style checker |
| `MIN-108` | 4 | "Does it work on my work?" | the system run on your real source |
| `MIN-109` | 4 or at home | "It's polite, but it doesn't sound like us" | your voice as testable rules and a tone-by-moment table |

## Your own case

Sessions use the demo meeting so everyone sees the same thing. The homework tickets (`MIN-104`, `MIN-108`) use your own source. What changes:

| Your source | "Quote" means | "Location" means | A rule to start with |
|---|---|---|---|
| meeting transcript | the line | `hh:mm:ss` | the owner appears only if named |
| course chapter or book | the sentence | the page | no article or definition from outside the text |
| training material | the sentence or objective | module or slide | do not add modules nobody asked for |
| product documentation (fields, API) | the definition | field or version | terms come only from the glossary |

`check_ssot.py` reads transcripts with `[hh:mm:ss]`. For other sources you adapt the `LINE` expression in the script or use only the Verifier; `MIN-104` explains.

## Using several tools

It does not matter whether you work in Claude, ChatGPT, Gemini or Copilot. An "agent" is a separate conversation with the instructions from `agents/` pasted at the start. Whoever generates does not verify, so you use two conversations, in the same tool or in different ones. Details in `docs/tools.md`.

## What the system does NOT do

- It does not guarantee a model follows a rule. A written rule is a request. That is why there are tests, three runs and a verifier.
- The script does not understand meaning. It catches an invented quote; it does not catch a discussion turned into a decision.
- It does not fix bad sources. If your source is an email you never file anywhere, the SSOT has nothing to feed on.

## Read next

Start with `docs/how-this-works.md` (ten minutes, one loop, a glossary).

## License

MIT, see `LICENSE`. Copyright © 2026 Eliza Marin. You may use, copy and adapt it freely; keep the copyright notice.
