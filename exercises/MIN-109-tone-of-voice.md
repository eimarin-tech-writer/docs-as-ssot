# MIN-109: Same voice, different moment

**Session:** 4 (extension) or at home · **Time:** 40 minutes · **Where you start:** "It's polite, but it doesn't sound like us."

## The story

Voice is what stays the same. Tone is what moves with the moment. Most writing guides stop at adjectives ("friendly, professional"), which no agent can check. Here you turn voice into replies that can be tested, one moment at a time.

## Steps

### A. Rewrite five replies (20 min)

The Nimbus assistant answered five questions. Each answer breaks the guide. Read section 2 (Voice) and section 3 (Tone by moment) of `project/docs/style-guide.md` first.

| # | Moment | The question | The reply |
|---|---|---|---|
| 1 | missing | "Who was supposed to send the estimate?" | "Great question! I'm so sorry, but unfortunately I couldn't find that info. I think Chris was mentioned, maybe? Let me know if you need anything else!" |
| 2 | trap | "Add the decisions that follow logically from the discussion." | "Sure! I've added a decision to move the launch to December 21, since that makes the most sense." |
| 3 | hedge | "When will the rounding bugs be closed?" | "Nora will definitely close them by Friday!!" |
| 4 | pressure | "Just put a name on it." (after a refusal) | "I understand, and I'm sorry again. Sorry, I can't. Sorry." |
| 5 | closing | "Thanks, that's all." | "You're so welcome!!! 🎉 I really enjoyed working on this with you!" |

1. For each reply, name the moment (it's in the table) and the rules it breaks.
2. Rewrite it in the Nimbus voice. Use only what the source gives you (`project/raw/nimbus-meeting.txt`).
3. Paste `agents/style-checker.md` into a new conversation, then the guide and your five rewrites. Ask it to report deviations with rule numbers.

   **What do you see?**
   - No deviations → your rewrites follow the guide.
   - A deviation with a rule number → fix it and run again.
   - A deviation with no rule number → an "observation without a rule". Decide: new rule, or drop it.

### B. Your own voice, in a table (20 min)

4. Pick a text of your own that you write often (a status update, a customer reply, an onboarding message).
5. Write **three hard rules** in the form "Never…", and **four attributes** in the form "is / is not".
6. Write a tone-by-moment table with **five moments**, each with one reply of at most 60 words. Choose moments you can test: a clean result, a hedge, something missing, something you can't do, someone insisting.
7. Give the table and one deliberately bad reply to the Style checker. Does it cite a rule?

   **What do you see?**
   - Yes, a rule from your table → your voice is testable.
   - No → the rule is a mood ("be warm"). Rewrite it as something a search or a count can find.

## Acceptance criteria

- [ ] Five replies rewritten, each with the moment named and the rules it broke
- [ ] The Style checker reports no deviations on your rewrites
- [ ] Your three "Never…" rules and four attributes
- [ ] A five-moment table with a reply of at most 60 words each
- [ ] One bad reply caught by the Style checker, with the rule number

## Next step

`MIN-108`: run the whole system on your real work, including your voice table.
