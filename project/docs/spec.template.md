# Specification: [name of the deliverable]

One page. If it doesn't fit, it's too much.

## 1. Intent

Who reads the result and what do they do with it?

> [to fill in]

## 2. Inputs

Which sources are allowed? Anything not listed here does not go in.

> [to fill in]

## 3. Output

Type of document, sections, length, format.

> [to fill in]

## 4. Rules

Each rule is checkable with a yes or no.

| No. | Rule | How to check |
|---|---|---|
| G-01 | | |
| G-02 | | |

## 5. What it does not do

What it refuses, and what it offers instead (reason + alternative).

> [to fill in]

## 6. Acceptance

When is it done?

> [to fill in]

---

## A completed example: meeting minutes

**1. Intent.** Meeting participants read the minutes to know what was decided and what they have to do.
**2. Inputs.** Only the verified `project/docs/ssot.md`. Nothing from the model's memory.
**3. Output.** Fixed sections: decisions, actions, open questions, risks. Every row carries an ID from the SSOT.
**5. What it does not do.** It does not deduce decisions. For anything not in the SSOT it answers "not in the source" and shows what does exist.
**6. Acceptance.** Zero critical, at most 2 high, over three runs.

| No. | Rule | How to check |
|---|---|---|
| G-01 | Every decision, action and question has an ID from the SSOT. | count the rows without an ID |
| G-02 | The owner appears only if named in the SSOT; otherwise "unnamed". | look for actions with a name that has no source |
| G-03 | A deadline appears only if said explicitly; "I think", "maybe" become "probably, to be confirmed". | look for dates and deadlines with no marker |
| G-04 | "Decided" only for rows of type `decision`. | check every "decided" against the type |
| G-05 | No figure or system name that is not in the SSOT. | look the numbers up in the SSOT |
| G-06 | What is not in the SSOT is stated as "not in the source", not filled in. | a test for the missing case |
