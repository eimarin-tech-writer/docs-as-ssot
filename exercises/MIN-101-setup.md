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
   - No AI model installed on your computer → you don't need one. The later exercises work in any AI chat in the browser (see `docs/tools.md`).
   - No terminal, or you can't install anything → skip steps 1 and 2 and use "No terminal?" below.
2. Run the checker from the repo root:
   ```
   python3 tools/check_ssot.py project/docs/ssot.example.md project/raw/nimbus-meeting.txt
   ```

   **What do you see?**
   - `Verdict: PASS` → go on to step 3.
   - `command not found` or a Python error → install Python 3 and try again. If you can't, use "No terminal?" below and tell the mentor you work without the script (see `docs/tools.md`).
3. Open `project/raw/nimbus-meeting.txt`. Read the first 12 lines.
4. Pick one row from `ssot.example.md` and find its quote in the transcript, at the stated location.

   **What do you see?**
   - The quote appears on that line, word for word → you've understood the rule.
   - You can't find it → check that you searched at `Location`, not in the whole text.
5. Read `AGENTS.md` (two minutes).

## No terminal? Use an AI chat in the browser

This replaces steps 1 and 2. Steps 3 to 5 stay the same; you read the files on GitHub.

1. Get these four files from GitHub. Open each one and choose **Download raw file**, or choose **Raw** and copy the text.
   - [`project/docs/ssot.example.md`](../project/docs/ssot.example.md)
   - [`project/raw/nimbus-meeting.txt`](../project/raw/nimbus-meeting.txt)
   - [`AGENTS.md`](../AGENTS.md)
   - [`tools/check_ssot.py`](../tools/check_ssot.py), so the model has the exact checks. They are listed at the top of the file.
2. Start a new conversation in Gemini, ChatGPT, Claude or Copilot. Attach the four files, or paste them whole, and send this prompt:
   ```
   I'm doing exercise MIN-101 from the docs-as-ssot repo and I can't run scripts on my computer.
   Attached: ssot.example.md, nimbus-meeting.txt, AGENTS.md and check_ssot.py.

   Apply the checks in check_ssot.py to every row of ssot.example.md, against nimbus-meeting.txt.
   If you can execute Python, run the script and show me its output.
   If you can't, apply each check by hand and tell me you did it by hand.

   For every row, report: the ID, the transcript line at its Location, whether the quote
   appears on that line (ignore case and punctuation, as the script does), and any finding
   with its rule (G-01, G-02, G-03, speaker, type, status).
   End with the number of rows checked and the verdict.

   Use only the attached files. If something is not in them, say "not in the source".
   ```

   **What do you see?**
   - 9 rows, no findings, `PASS` → go on to step 3.
   - A finding, or a different number of rows → the example is correct, so the mistake is the model's. Open the transcript at that `Location` and check the row yourself. Then send the prompt again in a new conversation and compare: without the script, the check is not deterministic (see "Without Python" in `docs/tools.md`).
3. After step 4, send the model the row you checked by hand and your one-sentence answer to "why is 'I think Friday' not the same as 'Friday'?". Ask it to point out anything that does not hold. The mentor still has the last word.

## Acceptance criteria

- [ ] The script ran and printed `PASS`, or the AI chat reported 9 rows with no findings (or you noted that you work without either)
- [ ] You found a quote from the SSOT in the transcript by hand
- [ ] You can say in one sentence why "I think Friday" is not the same as "Friday"

## Next step

`MIN-102`: you extract an SSOT from the transcript yourself.
