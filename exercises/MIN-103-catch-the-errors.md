# MIN-103: Catch the errors

**Session:** 2 · **Time:** 25 minutes · **Where you start:** "How do I catch what I didn't see?"

## The story

A colleague extracted an SSOT from the same meeting. You don't trust it. You look for errors in two ways and see what each one catches.

## Steps

1. Run the script on your colleague's table:
   ```
   python3 tools/check_ssot.py project/docs/ssot.to-review.md project/raw/nimbus-meeting.txt
   ```
   Note every flagged row and which rule caught it.

   **What do you see?**
   - A `FAIL` verdict with several findings → you have a first list.
   - `PASS` → check that you used the `to-review` file, not `example`.
2. Open a **new** conversation. Paste `agents/verifier.md`. Attach the transcript, the table `ssot.to-review.md` and `qa/severity.md`.
3. Ask: "Verify the table. Write a finding card for every problem and a verdict."
4. Compare the two lists: what did only the script catch? What did only the Verifier catch?

   **What do you see?**
   - The Verifier caught what the script missed (meaning, not presence) → the layers complement each other, exactly as they should.
   - The Verifier missed something the script caught → its instructions don't insist on quotes. Add the rule and run again.
   - The Verifier "found" problems with no evidence from the source → ask for the full card, with location and quote. A card without evidence is not taken into account.
5. Look for what is **missing** from the table: read the transcript and list what does not appear.

## Acceptance criteria

- [ ] The script's list: the flagged rows, with the rule
- [ ] At least three finding cards from the Verifier, in the format of `qa/finding-card.md`
- [ ] At least one error the script could not catch, and why
- [ ] At least two things that are missing from the table
- [ ] One row you found to be correct (no false positive)

## Next step

`MIN-104` at home: you pick your own source and write the correct result by hand.
