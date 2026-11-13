# How this works: ten minutes

## The loop

All AI work in this repo follows the same loop:

```
Research → Write → Test → Score → Fix
```

| Step | The question | Where in the repo |
|---|---|---|
| Research | What does the source actually say? | `ssot.md` |
| Write | What exactly do I want, and what must it not do? | `spec.md`, `style-guide.md` |
| Test | Does the rule hold when I try to break it? | `qa/tests.md` |
| Score | How serious is what failed? | `qa/severity.md` |
| Fix | What do I rewrite and run again? | the rule, not the prompt |

The key is the last line: you fix the **rule**, you do not repeat the prompt more insistently. Asking more does not mean asking better.

## Why an SSOT

A model does not know what was said in a meeting. It only has what you gave it. If you give it no source and don't force it to quote from it, it fills the gaps plausibly. That looks like a "hallucination", but it is a gap in the source.

The SSOT is the table in which every claim has:

- a **type** (fact, decision, action, open question, risk),
- a **quote** that appears verbatim in the source,
- a **location** where you can find it,
- a **status**: verified (the quote supports exactly the claim), inferred (it supports it partly), unconfirmed (it does not appear).

**The floor rule:** what cannot be traced to the source is not stated.

## Whoever generates does not verify

A model that checks its own output repeats the same mistake. So:

- The **Generator** writes.
- The **Verifier**, in a separate conversation, receives the source, the output and the criteria, and writes finding cards.
- The **script** checks what can be checked without a model: quotes are real, speakers match.
- The **human** decides.

Three layers, each catching something different:

| Layer | Catches | Does not catch |
|---|---|---|
| script | invented quote, wrong speaker, a hedge turned into certainty | meaning |
| Verifier | a discussion turned into a decision, a figure corrected later | what you didn't tell it to look for |
| human | what matters in context | what they don't read |

## The contract of a specification

A good spec has six fields, and each rule is verifiable with a yes or no:

1. Intent: who reads it and what they do with the result
2. Inputs: which sources are allowed
3. Output: what structure the result has
4. Rules: G-01, G-02…
5. What it does not do, and what it offers instead
6. Acceptance: when it is done

A rule you cannot check with a yes or no is a wish. You rewrite it.

## Severity

Severity is not how ugly the mistake looks; it is what happens to the reader who trusts the text. **A silent error is worse than a visible one**: an invented decision goes unnoticed, a formatting error is seen.

## Glossary

| Term | Means here |
|---|---|
| SSOT | the table of claims anchored in the source |
| Source | the raw file in `project/raw/` |
| Agent | a separate conversation with its own instructions |
| Generator | the agent that writes |
| Verifier | the agent that looks for what doesn't hold |
| Guardrail | a rule that is also checked |
| Finding card | one verdict row: claim, source, evidence, severity, remedy |
| Golden output | the correct result, written by hand by you, on a source you know |
