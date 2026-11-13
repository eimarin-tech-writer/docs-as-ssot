# MIN-106: Repară regula, nu promptul

**Sesiune:** acasă, după sesiunea 3 · **Durată:** 30 minute · **Starea ta:** „O regulă a picat."

## Povestea

Un test a picat. Reflexul e să adaugi „fii mai atent" în prompt. Aici faci altceva: afli de ce a picat și repari cauza.

## Pași

1. Ia regula care a picat cel mai grav la `MIN-105` (cea mai mare severitate).
2. Deschide rulările eșuate. Citește exact ce a făcut modelul diferit de ce voiai.
3. Decide cauza:

   | Cauză | Semn | Remediu |
   |---|---|---|
   | **regulă vagă** | oricine ar fi interpretat-o în două feluri | rescrie regula cu un criteriu da/nu |
   | **regulă ignorată** | e clară, dar modelul a încălcat-o | mută verificarea în afara modelului (script, Verificator) |
   | **sursă proastă** | modelul a completat un gol din SSOT | repară SSOT-ul, nu spec-ul |

   **Ce vezi?**
   - Regula era vagă → o rescrii și gata.
   - Era clară, dar a fost încălcată → o regulă scrisă nu e un guardrail. Adaugă un test automat sau o sarcină explicită Verificatorului.
4. Fă remedierea. Rulează **aceleași teste**, de trei ori.
5. Notează în raport: ce era înainte, ce e acum, rezultatele.

## Criterii de acceptare

- [ ] O regulă rescrisă sau o verificare mutată, cu cauza numită
- [ ] Aceleași teste rulate de trei ori după remediu
- [ ] Un before/after în raport
- [ ] O propoziție: ce ai învățat despre regula asta

## Pasul următor

`MIN-107`: faci ca rezultatul să sune la fel de fiecare dată.
