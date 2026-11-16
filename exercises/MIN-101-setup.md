# MIN-101: Setup

**Session:** 1 · **Time:** 10 minutes · **Where you start:** "Does my setup work?"

## The story

Before you build anything, you prove you have the environment and that you understand the basic rule: what an anchored row means.

## Steps

1. Clone the repo and open the folder. In a terminal:
   ```
   cd ~/Documents
   git clone https://github.com/eimarin-tech-writer/docs-as-ssot.git
   cd docs-as-ssot
   ```

   **Something missing?**
   - No git → on the repo page on GitHub, choose **Code > Download ZIP**, unzip it, and open the `docs-as-ssot-main` folder in a terminal.
   - On Windows → run the same commands in PowerShell. In step 2, if `python3` is not found, try `python` or `py` instead.
   - No AI model installed on your computer → you don't need one. This exercise uses no AI, and the later ones work in any AI chat in the browser (see `docs/tools.md`).
2. Run the checker from the repo root:
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
