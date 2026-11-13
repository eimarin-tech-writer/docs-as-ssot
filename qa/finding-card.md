# The finding card

The same format in every session, so the verifier (agent or human) always reports the same way.

```
claim:      the text in question
source:     location + short quote, or "none"
evidence:   what I compared
severity:   critical | high | medium | low
remedy:     one concrete step
```

## A good example

```
claim:      M-04: "Nora closes the rounding bugs by Friday" (verified)
source:     00:03:12, "I think by Friday, but no promises"
evidence:   the quote contains a hedge ("I think") and a reservation ("no promises");
            the claim turned them into a firm deadline
severity:   critical
remedy:     status "inferred", claim: "Nora estimates Friday, with no guarantee"
```

## A bad example

```
claim:      M-04
source:     —
evidence:   doesn't sound right
severity:   medium
remedy:     check it
```

Without a source and without evidence, the card is not a finding. It is an opinion.
