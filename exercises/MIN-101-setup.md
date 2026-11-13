# MIN-101: Setup

**Session:** 1 · **Time:** 10 minutes · **Where you start:** "Does my setup work?"

## The story

Before you build anything, you prove you have the environment and that you understand the basic rule: what an anchored row means.

## Steps

1. Clone the repo and open the folder.
2. Run:
   ```
   python3 tools/check_ssot.py project/docs/ssot.example.md project/raw/nimbus-meeting.txt
   ```

   **What do you see?**
   - `Verdict: PASS` → go on to step 3.
   - `command not found` or a Python error → install Python 3 and try again. If you can't, tell the mentor: you'll work without the script (see `docs/tools.md`).
3. Open `project/raw/nimbus-meeting.txt`. Read the first 12 lines.
4. Pick one row from `ssot.example.md` and find its quote in the transcript, at the stated location.

   **What do you see?**
   - The quote appears on that line, word for word → you've understood the rule.
   - You can't find it → check that you searched at `Location`, not in the whole text.
5. Read `AGENTS.md` (two minutes).

## Acceptance criteria

- [ ] The script ran and printed `PASS` (or you noted that you work without it)
- [ ] You found a quote from the SSOT in the transcript by hand
- [ ] You can say in one sentence why "I think Friday" is not the same as "Friday"

## Next step

`MIN-102`: you extract an SSOT from the transcript yourself.
