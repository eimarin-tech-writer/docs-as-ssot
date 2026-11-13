# Style guide: meeting minutes

Numbered rules, so that a person or an agent checking a text can cite them. An observation without a rule number is a preference: either it becomes a rule, or it is not reported.

## Who we write for

Meeting participants and colleagues who were not there. They read fast and look for what was decided and what they have to do.

## Voice

| The minutes are | The minutes are not |
|---|---|
| neutral: they report, they don't comment | evaluative ("a great idea") |
| precise: names, dates, exact amounts | vague ("soon", "a few") |
| careful: they say when something is uncertain | confident about unconfirmed things |

## Terminology

One concept, one term.

| Use | Don't use | Means |
|---|---|---|
| decision | resolution, conclusion | something explicitly settled |
| action | task, to-do, ticket | something to be done, with or without an owner |
| open question | pending, to discuss | something not yet decided |
| risk | issue, problem | something that could go wrong |
| owner | assignee, responsible | the person who does the action |
| unnamed | TBD, unknown | an owner who was not said |

## Structure of the minutes

The same sections, in the same order:

1. **Decisions**
2. **Actions**
3. **Open questions**
4. **Risks**
5. **To be confirmed** (rows that are `inferred` or `unconfirmed`)

Every row: one sentence, with the ID from the SSOT in parentheses. Actions look like this: `Owner: action. Deadline. (M-08)`.

## Rules

| No. | Rule | How to check |
|---|---|---|
| R-01 | Use only the terms in the "Use" column. | look for the forbidden terms |
| R-02 | At most 20 words in a sentence. | count |
| R-03 | One row = one decision or action. | count the action verbs |
| R-04 | An action starts with the owner's name or with "Unnamed:". | read the start of the row |
| R-05 | Every row has an ID from the SSOT. | look for rows without an ID |
| R-06 | No evaluative adjectives or adverbs: "great", "important", "unfortunately". | search |
| R-07 | Dates with the month in letters (December 14); times in 24h format (10:00). | look for "12/14", "AM", "PM" |
| R-08 | Uncertainty is marked: "probably", "to be confirmed". | look for deadlines with a hedged source and no marker |
| R-09 | Names and terms are written as in the source (PDF, not pdf). | compare with the source |
| R-10 | The minutes end with the date of the next meeting, if it was said. | read the last row |

## Right / wrong

| Wrong | Right | Rule |
|---|---|---|
| "Nora will fix the rounding bugs by Friday." | "Nora: close the rounding bugs. Probably Friday, to be confirmed. (M-04)" | R-04, R-08 |
| "Task: send estimate — TBD" | "Unnamed: send the estimate to the client. (M-06)" | R-01, R-04 |
| "The team decided to move the launch." | "Open question: moving the launch to December 21 is not decided. (M-03)" | R-01 |
