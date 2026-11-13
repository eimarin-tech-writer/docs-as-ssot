# MIN-108: Demo, the system on your work

**Session:** 4, second half · **Time:** 25 minutes · **Where you start:** "Does it work on my work?"

## The story

You have an SSOT, a spec and a guide. You run them end to end on your source and show what came out, including what didn't work.

## Steps

1. Take the source from `MIN-104`, with its golden output.
2. Run the chain:
   1. Extractor → `ssot.md`
   2. `check_ssot.py` (if the source has timestamps)
   3. Generator → output in `project/output/`
   4. Verifier on the output
   5. Style checker
3. Compare the result with the golden output.

   **What do you see?**
   - Zero critical, at most 2 high → the chain works on your case.
   - Criticals → say which ones, and which rule would have caught them. That is also a good result.
4. Prepare 3 minutes of presentation: what you tried, what the system caught, what it missed, what you do next week.

## Acceptance criteria

- [ ] The full chain run once
- [ ] The result compared with the golden output
- [ ] A conformance report
- [ ] Three minutes of presentation: what it caught, what it missed, what comes next
- [ ] One next step, a single one, that you take in your real work

## After the mentoring

Keep the repo. Put your sources in `project/raw/`, your rules in `spec.md` and `style-guide.md`, and run the system on every new deliverable.
