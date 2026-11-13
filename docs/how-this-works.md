# Cum funcționează: zece minute

## Bucla

Orice lucru cu AI din repo merge în aceeași buclă:

```
Research → Write → Test → Score → Fix
```

| Pas | Întrebarea | Unde în repo |
|---|---|---|
| Research | Ce spune sursa, de fapt? | `ssot.md` |
| Write | Ce vreau exact și ce nu are voie să facă? | `spec.md`, `style-guide.md` |
| Test | Ține regula când încerc s-o încalc? | `qa/tests.md` |
| Score | Cât de grav e ce a picat? | `qa/severity.md` |
| Fix | Ce rescriu și rulez iar? | regula, nu promptul |

Cheia e a doua linie: repari **regula**, nu repeți promptul mai insistent. Mai mult interogat nu înseamnă mai bun.

## De ce SSOT

Un model nu știe ce s-a spus într-o ședință. Are doar ce i-ai dat. Dacă nu îi dai o sursă și nu îl obligi să citeze din ea, completează golurile plauzibil. Asta se vede ca „halucinație", dar e un gol de sursă.

SSOT-ul e tabelul în care fiecare afirmație are:

- un **tip** (fapt, decizie, acțiune, întrebare deschisă, risc),
- un **citat** care apare întocmai în sursă,
- un **loc** unde îl găsești,
- un **status**: verificat (citatul susține exact afirmația), dedus (susține parțial), neconfirmat (nu apare).

**Regula de podea:** ce nu poate fi urmărit până la sursă nu se afirmă.

## Cine generează nu verifică

Un model care își verifică propriul rezultat repetă aceeași greșeală. De aceea:

- **Generatorul** scrie.
- **Verificatorul**, într-o conversație separată, primește sursa, rezultatul și criteriile, și scrie fișe de constatare.
- **Scriptul** verifică ce se poate verifica fără model: citatele sunt reale, vorbitorii se potrivesc.
- **Omul** decide.

Trei straturi, fiecare prinde altceva:

| Strat | Prinde | Nu prinde |
|---|---|---|
| script | citat inventat, vorbitor greșit, ezitare devenită certitudine | sensul |
| Verificator | discuție devenită decizie, cifră corectată mai târziu | ce nu i-ai spus să caute |
| om | ce contează în context | ce nu citește |

## Contractul unei specificații

Un spec bun are șase câmpuri și fiecare regulă se verifică cu da/nu:

1. Intenție: cine citește și ce face cu rezultatul
2. Intrări: ce surse sunt permise
3. Ieșire: ce structură are rezultatul
4. Reguli: G-01, G-02…
5. Ce nu face, și ce oferă în loc
6. Acceptare: când e gata

O regulă care nu se poate verifica cu da/nu e o dorință. O rescrii.

## Severitate

Gravitatea nu e cât de urât arată greșeala, ci ce se întâmplă cu cititorul care are încredere în text. **Eroarea tăcută e mai gravă decât cea vizibilă**: o decizie inventată trece neobservată, o eroare de format se vede.

## Glosar

| Termen | Înseamnă aici |
|---|---|
| SSOT | tabelul de afirmații ancorate în sursă |
| Sursă | fișierul brut din `project/raw/` |
| Agent | o conversație separată cu instrucțiuni proprii |
| Generator | agentul care scrie |
| Verificator | agentul care caută ce nu ține |
| Guardrail | regulă care se și verifică |
| Fișă de constatare | un rând de verdict: afirmație, sursă, dovadă, severitate, remediu |
| Minuta de aur | rezultatul corect, scris de mână de tine, pe o sursă pe care o știi |
