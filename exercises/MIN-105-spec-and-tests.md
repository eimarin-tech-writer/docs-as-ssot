# MIN-105: Spec, rules and tests

**Session:** 3 · **Time:** 60 minutes · **Where you start:** "It does something other than what I asked."

## The story

You have an SSOT you trust. Now you write exactly what you want from it, instead of repeating prompts, and you test whether the rules hold.

## Steps

### A. Cut the prompt (10 min)

1. Take a prompt you usually use and that has grown long.
2. Sort every sentence into one of five: **intent**, **input**, **rule**, **format**, **noise**.

   **What do you see?**
   - Half of it is noise ("be very careful", "make it perfect") → that cannot be tested. Remove it.
   - The rules cannot be checked with a yes or no → they are wishes. You rewrite them in step 4.

### B. Write the spec (15 min)

3. Open a new conversation. Paste `agents/spec-author.md`. Say in your own words what you want: the minutes of the Nimbus meeting, for whom, what they do with them.
4. Answer the questions, one at a time. For each rule, answer "how would I check this with a yes or no?".
5. Save the result in `project/docs/spec.md`.

   **What do you see?**
   - You can check every rule with a yes or no → a good spec.
   - A rule stays vague ("the minutes should be clear") → rewrite it as a checkable rule or drop it.

### C. Generate and test (35 min)

6. New conversation. Paste `agents/generator.md`, then `spec.md`, `style-guide.md` and `ssot.md`. Ask for the minutes.
7. Write in `qa/tests.md` (based on `qa/tests.template.md`) at least five tests, one of each type: direct, missing, trap, hedge, pressure.
8. Run **each test three times**, in new conversations. Fill in the conformance report.

   **What do you see?**
   - 3/3 conforming → the rule holds.
   - 2/3 or less → the rule does not hold. Mark the severity following `qa/severity.md`. It stays for `MIN-106`.
9. In a separate conversation, run the Verifier on the generated minutes, with `spec.md` and the SSOT.

## Acceptance criteria

- [ ] `spec.md` with the six fields filled in
- [ ] At least six G- rules, each with "how to check" as a yes or no
- [ ] `qa/tests.md` with at least five tests, one of each type
- [ ] A conformance report with three runs per test
- [ ] At least one rule that failed, with a severity
- [ ] One finding card from the Verifier on the minutes

## Constraints

Do not fix the prompt when a test fails. Note the rule that failed. You fix it in `MIN-106`.

## Next step

`MIN-106` at home: you rewrite the rule that failed and run again.
