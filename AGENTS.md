# AGENTS.md: regulile proiectului

Citește fișierul ăsta înaintea oricărei sarcini. Se aplică oricărui agent, în orice unealtă.

## Regula de aur

**Nicio afirmație fără sursă.** Orice decizie, acțiune, cifră sau nume din rezultat trimite la un loc din `project/raw/`, cu un citat care apare întocmai acolo. Ce nu poate fi urmărit nu se afirmă. Se scrie „nu apare în sursă".

## Unde stau lucrurile

| Folder | Conține | Cine scrie |
|---|---|---|
| `project/raw/` | sursele brute (transcript, document) | omul, niciodată un agent |
| `project/docs/` | `ssot.md`, `spec.md`, `style-guide.md` | omul, cu agenți |
| `project/output/` | livrabile (minute, materiale) | agentul Generator |
| `qa/` | severitate, fișe de constatare, teste, rapoarte | Verificatorul și omul |
| `agents/` | instrucțiunile fiecărui agent | omul |

## Reguli de lucru

1. **Cine generează nu verifică.** Generatorul și Verificatorul sunt conversații separate. Verificatorul primește sursa, rezultatul și criteriile, nu și raționamentul Generatorului.
2. **Intrările sunt cele atașate.** Nimic din memoria modelului, nimic din alte ședințe sau documente care nu sunt în `project/raw/`.
3. **Ezitarea rămâne ezitare.** „Cred că vineri" nu devine „termen: vineri". Se scrie „probabil vineri, de confirmat".
4. **Discuția nu e decizie.** „S-a decis" doar dacă cineva a hotărât explicit.
5. **Responsabilul apare doar dacă e numit.** Altfel: „nenumit".
6. **Omul decide.** Fișele de constatare informează decizia, nu o iau.

## Regula impusă (nu doar scrisă)

`tools/check_ssot.py` verifică orice `ssot.md`: citatul apare întocmai pe linia citată, vorbitorul și responsabilul se potrivesc, ezitarea nu devine certitudine. Rulează-l după fiecare extragere. Dacă pică, nu mergi mai departe.

Scriptul verifică prezența și potrivirea, nu sensul. Sensul îl verifică agentul Verificator, iar decizia finală e a omului.

## Severitate (rezumat; detalii în `qa/severity.md`)

| Nivel | Când | Decizie |
|---|---|---|
| critic | cititorul e indus în eroare fără să știe | pică |
| ridicat | se pierde o decizie sau o acțiune | cel mult 2, cu condiții |
| mediu | formulare, ton, structură | recomandare |
| scăzut | cosmetic | notă |
