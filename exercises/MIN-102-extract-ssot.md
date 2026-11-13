# MIN-102: Extract an SSOT from a transcript

**Session:** 2 · **Time:** 25 minutes · **Where you start:** "I don't trust what comes out."

## The story

You have a meeting transcript. You want a table in which every claim has a source, so you can build the minutes on it without rereading everything.

## Steps

1. Open a new conversation in your tool. Paste `agents/extractor.md`, then attach `project/raw/nimbus-meeting.txt`.
2. Ask: "Extract the SSOT from the transcript."
3. Save the table to `project/docs/ssot.md`.
4. Run:
   ```
   python3 tools/check_ssot.py project/docs/ssot.md project/raw/nimbus-meeting.txt
   ```

   **What do you see?**
   - `PASS` → go to step 5.
   - `FAIL` with `G-01` (the quote does not appear) → the model paraphrased instead of copying. Ask: "Copy the quote verbatim from the transcript" and run again.
   - `FAIL` with `G-02` or `G-03` → you have a rule that doesn't hold. Note which one; you'll use it in `MIN-105`.
5. Compare with what you found by reading: is any decision, action or risk missing? Add it by hand, or ask the model to look for it, again with a quote.

   **What do you see?**
   - Nothing is missing → check line `00:07:10` once more (a figure was corrected) and `00:08:05` (who prepares the PDF).
   - Something is missing → that means the script would never have caught it: the script checks what is in the table, not what is absent.

## Acceptance criteria

- [ ] `ssot.md` exists and `check_ssot.py` gives `PASS`
- [ ] Zero rows with a paraphrased quote
- [ ] "I think Friday" appears as `inferred` with an uncertainty marker
- [ ] The proposal to move the launch does not appear as a `decision`
- [ ] The estimate for the client has the owner `unnamed`
- [ ] The budget figure is the corrected one (25k), with a quote

## Constraints

Do not edit `project/raw/`. Do not ask the model to "fill in what is missing".

## Next step

`MIN-103`: you get an SSOT made by someone else and find out what is wrong in it.
