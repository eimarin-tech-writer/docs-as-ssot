# MIN-104: Your source and the golden output

**Session:** at home, after session 2 · **Time:** ~60 minutes · **Where you start:** "What does the perfect document look like?"

## The story

Until now you worked on my source. Now you bring yours. And you write, **by hand**, the correct result. That is the **golden output**: the answer to "how would I recognize the perfect document?", and your test set for the rest of the mentoring.

## Steps

1. Pick a source you know well and that is short (20–30 minutes of a meeting, or 3–5 pages). Anonymize it if it has sensitive data.
   - Work data stays in the work account. Check your employer's policy before putting it in any other tool.
2. Put it in `project/raw/`. The folder is ignored by Git: it is never uploaded.
3. **Write by hand** the correct result, without AI: what you would want the system to produce. Keep it in a file `golden-output.md`.

   **What do you see?**
   - You can make the list in a few minutes → the source is a good one.
   - You don't know what should come out → the source is too long or too vague. Pick another fragment.
4. Adapt the format to your source, following the table in `README.md`, section "Your own case". If the source has no `[hh:mm:ss]`, note how you will express "Location" (page, module, field).
5. Run the Extractor agent on your source. If the source has no timestamps, the script will not read it without changes: use only the Verifier or adapt the `LINE` expression in `tools/check_ssot.py`.
6. Compare with the golden output: what is missing? What is extra? What is wrong?

## Acceptance criteria

- [ ] Your source, in `project/raw/`
- [ ] `golden-output.md`, written before you saw the AI's result
- [ ] An SSOT extracted by the Extractor from your source
- [ ] A short list: how many rows are correct, how many wrong, how many missing
- [ ] One type of mistake you recognize as yours (invented, wrongly attributed, omitted, interpreted)

## Next step

`MIN-105`: you write what you want from this source, as a specification, and test it.
