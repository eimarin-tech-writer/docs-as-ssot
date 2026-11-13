# MIN-105: Spec, reguli și teste

**Sesiune:** 3 · **Durată:** 60 minute · **Starea ta:** „Face altceva decât am cerut."

## Povestea

Ai un SSOT în care ai încredere. Acum scrii exact ce vrei de la el, în loc să repeți prompturi, și testezi dacă regulile țin.

## Pași

### A. Taie promptul (10 min)

1. Ia un prompt pe care îl folosești de obicei și care a devenit lung.
2. Sortează fiecare propoziție într-una din cinci: **intenție**, **intrare**, **regulă**, **format**, **zgomot**.

   **Ce vezi?**
   - Jumătate e zgomot („fii foarte atent", „fă-l perfect") → asta nu se poate testa. Scoate-o.
   - Regulile nu se pot verifica cu da/nu → sunt dorințe. Le rescrii la pasul 3.

### B. Scrie spec-ul (15 min)

3. Deschide o conversație nouă. Lipește `agents/autor-spec.md`. Spune în cuvintele tale ce vrei: minuta ședinței Nimbus, pentru cine, ce face cu ea.
4. Răspunde la întrebări, una pe rând. Pentru fiecare regulă, răspunde la „cum aș verifica asta cu da sau nu?".
5. Salvează rezultatul în `project/docs/spec.md`.

   **Ce vezi?**
   - Poți verifica fiecare regulă cu da/nu → spec bun.
   - O regulă rămâne vagă („minuta să fie clară") → rescrie-o ca o regulă verificabilă sau scoate-o.

### C. Generează și testează (35 min)

6. Conversație nouă. Lipește `agents/generator.md`, apoi `spec.md`, `style-guide.md` și `ssot.md`. Cere minuta.
7. Scrie în `qa/tests.md` (pe baza `qa/tests.template.md`) cel puțin cinci teste, câte unul din fiecare tip: direct, lipsă, capcană, ezitare, presiune.
8. Rulează **fiecare test de trei ori**, în conversații noi. Completează raportul de conformitate.

   **Ce vezi?**
   - 3/3 conforme → regula ține.
   - 2/3 sau mai puțin → regula nu ține. Marchează severitatea după `qa/severity.md`. Rămâne pentru `MIN-106`.
9. Într-o conversație separată, rulează Verificatorul pe minuta generată, cu `spec.md` și SSOT-ul.

## Criterii de acceptare

- [ ] `spec.md` cu cele șase câmpuri completate
- [ ] Cel puțin șase reguli G-, fiecare cu „cum verifici" în da/nu
- [ ] `qa/tests.md` cu cel puțin cinci teste, câte unul din fiecare tip
- [ ] Raport de conformitate cu trei rulări pe test
- [ ] Cel puțin o regulă care a picat, cu severitate
- [ ] O fișă de la Verificator pe minută

## Constrângeri

Nu repara prompt-ul când un test pică. Notează regula care a picat. O repari la `MIN-106`.

## Pasul următor

`MIN-106` acasă: rescrii regula care a picat și rulezi din nou.
