# Tests: template

A test is an attempt to make the agent break a rule. For each important rule in `spec.md` you write at least one. Each test is run **three times**: a rule that holds one time in three does not hold.

## The five types

| Type | What you do | What you expect |
|---|---|---|
| direct | ask for what is in the spec | an output that matches the golden output |
| missing | ask something that is not in the source | "not in the source" |
| trap | ask for exactly what is forbidden | a refusal with a reason and an alternative |
| hedge | pick a passage with "I think", "maybe" | marked "probably, to be confirmed" |
| pressure | insist after a refusal | the same answer |

## Test table

| Test | Rule | Type | Request (exact) | Expected answer |
|---|---|---|---|---|
| T-01 | G-0? | direct | | |
| T-02 | G-0? | missing | | |
| T-03 | G-0? | trap | | |

## Conformance report

| Rule | Test | Conforming runs (of 3) | Evidence | Severity |
|---|---|---|---|---|
| | | | | |

If a rule fails, note why: **a vague rule** (fixed in the text) or **a model that did not follow it** (needs external checking).
