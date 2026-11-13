# Specificație: [numele livrabilului]

O pagină. Dacă nu încape, e prea mult.

## 1. Intenție

Cine citește rezultatul și ce face cu el?

> [de completat]

## 2. Intrări

Ce surse sunt permise? Tot ce nu e aici nu intră.

> [de completat]

## 3. Ieșire

Tip de document, secțiuni, lungime, format.

> [de completat]

## 4. Reguli

Fiecare regulă se verifică cu da sau nu.

| Nr. | Regulă | Cum verifici |
|---|---|---|
| G-01 | | |
| G-02 | | |

## 5. Ce nu face

Ce refuză, și ce oferă în loc (motiv + alternativă).

> [de completat]

## 6. Acceptare

Când e gata?

> [de completat]

---

## Exemplu completat: minuta de ședință

**1. Intenție.** Participanții la ședință citesc minuta ca să știe ce s-a decis și ce au de făcut.
**2. Intrări.** Doar `project/docs/ssot.md` verificat. Nimic din memoria modelului.
**3. Ieșire.** Secțiuni fixe: decizii, acțiuni, întrebări deschise, riscuri. Fiecare rând cu ID din SSOT.
**5. Ce nu face.** Nu deduce decizii. Pentru ce nu e în SSOT răspunde „nu apare în sursă" și arată ce există.
**6. Acceptare.** Zero critice, cel mult 2 ridicate, pe trei rulări.

| Nr. | Regulă | Cum verifici |
|---|---|---|
| G-01 | Fiecare decizie, acțiune și întrebare are ID din SSOT. | număr rândurile fără ID |
| G-02 | Responsabilul apare doar dacă e numit în SSOT; altfel „nenumit". | caută acțiuni cu nume fără sursă |
| G-03 | Un termen apare doar dacă e spus explicit; „cred că" devine „probabil, de confirmat". | caută date și termene fără marcaj |
| G-04 | „S-a decis" doar pentru rânduri de tip `decizie`. | verific fiecare „decis" pe tip |
| G-05 | Nicio cifră sau nume de sistem care nu e în SSOT. | caută numerele în SSOT |
| G-06 | Ce nu e în SSOT se spune „nu apare", nu se completează. | test de lipsă |
