# MIN-107: Style you can test

**Session:** 4 · **Time:** 55 minutes · **Where you start:** "It doesn't sound the same every time."

## The story

"Professional tone" cannot be tested. "No evaluative adjectives" can. You turn style preferences into numbered rules, then ask an agent to check them.

## Steps

### A. Read the guide (10 min)

1. Open `project/docs/style-guide.md`. Find one rule that can be checked with a search and one that needs judgment.

### B. Correct three texts (20 min)

2. Paste `agents/style-checker.md` into a new conversation, then the guide and the texts below, one at a time.
3. Ask: "Report the deviations, with the rule number."

   **T1**
   > Task: Nora will definitely fix the rounding bugs by Friday!

   **T2**
   > The team decided brilliantly to move the launch to 12/21 even though the bugs are still open, and unfortunately Sara can't do the estimate this week, TBD.

   **T3**
   > Nora notes the issue with the copied production data in the test environment and Sara sends the requirements list on Monday and Chris prepares the pdf.

   **What do you see?**
   - Every deviation has a rule number → the agent works to the guide.
   - A deviation with no number → an "observation without a rule". Decide: it becomes a rule (you add it) or it disappears.
4. Rewrite the three texts following the guide. Run the checker again on your versions.

### C. Your own guide (25 min)

5. Take three texts from your work that you corrected by hand in the last month.
6. From the corrections, extract **eight numbered rules** (R-01…R-08), each with "how to check".
7. Extract **five terms**, with the preferred version and the versions to avoid.
8. Write a text that breaks one of your rules and give it to the Checker, with your guide. Does it catch the deviation?

   **What do you see?**
   - Yes, with the rule number → the rule is well written.
   - No → the rule is vague. Rewrite it with a yes/no criterion.

## Acceptance criteria

- [ ] The three texts corrected, with rules cited
- [ ] At least one "observation without a rule" handled (new rule or dropped)
- [ ] Your guide: eight numbered rules, five terms
- [ ] A test text that breaks one of your rules and is caught by the Checker

## Next step

`MIN-108`: you put the three files (SSOT, spec, guide) on your real work.
