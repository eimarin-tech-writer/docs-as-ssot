# MIN-106: Fix the rule, not the prompt

**Session:** at home, after session 3 · **Time:** 30 minutes · **Where you start:** "A rule failed."

## The story

A test failed. The reflex is to add "be more careful" to the prompt. Here you do something else: you find out why it failed and fix the cause.

## Steps

1. Take the rule that failed worst in `MIN-105` (the highest severity).
2. Open the failed runs. Read exactly what the model did differently from what you wanted.
3. Decide the cause:

   | Cause | Sign | Remedy |
   |---|---|---|
   | **vague rule** | anyone could have read it in two ways | rewrite the rule with a yes/no criterion |
   | **ignored rule** | it is clear, but the model broke it | move the check outside the model (script, Verifier) |
   | **bad source** | the model filled a gap in the SSOT | fix the SSOT, not the spec |

   **What do you see?**
   - The rule was vague → you rewrite it, and that's it.
   - It was clear but it was broken → a written rule is not a guardrail. Add an automatic test or an explicit task for the Verifier.
4. Apply the fix. Run **the same tests**, three times.
5. Write in the report: what it was before, what it is now, the results.

## Acceptance criteria

- [ ] One rule rewritten or one check moved, with the cause named
- [ ] The same tests run three times after the fix
- [ ] A before/after in the report
- [ ] One sentence: what you learned about this rule

## Next step

`MIN-107`: you make the result sound the same every time.
