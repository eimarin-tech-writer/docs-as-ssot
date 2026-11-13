# Unelte: cum ții doi agenți în orice AI

„Agent" aici înseamnă o **conversație separată**, cu fișierele din `agents/` lipite la început și sursa atașată. Atât. Merge oriunde.

Numele exacte ale funcțiilor (proiecte, Gem-uri, GPT-uri, agenți) se schimbă des și diferă pe abonament. Tabelul de mai jos e un punct de pornire; verifică ce are contul tău.

| Unealtă | Generator | Verificator | Unde țin fișierele |
|---|---|---|---|
| Claude | un Project cu `agents/generator.md`, `spec.md`, `style-guide.md` în knowledge | alt Project sau conversație nouă, doar cu sursa, rezultatul și criteriile | în Project |
| ChatGPT | un Project sau un GPT propriu | o conversație nouă, în afara proiectului | în Project |
| Gemini | un Gem cu instrucțiunile | o conversație nouă, fără Gem | atașate la Gem |
| Copilot | un agent sau o conversație cu instrucțiunile lipite | o conversație nouă | atașate în conversație |

## Reguli valabile peste tot

1. **Două conversații, nu una.** Generatorul nu vede ce gândește Verificatorul și invers.
2. **Sursa o atașezi, nu o rezumi.** Dacă nu poți atașa, o lipești întreagă.
3. **Instrucțiunile sunt fișierele din `agents/`**, lipite așa cum sunt. Nu le rescrie din memorie.
4. **Dacă folosești mai multe unelte, alege roluri, nu comparații.** O unealtă generează, alta verifică, o singură trecere, criterii fixe, fișă la final. Dacă te prinzi că rulezi același prompt în patru locuri și compari, ai ieșit din sistem.
5. **Datele de la job rămân în contul de la job.** Înainte să pui un transcript într-un cont personal, verifică politica angajatorului.

## Fără Python

Scriptul `check_ssot.py` e un strat opțional. Fără el, adaugă în instrucțiunile Verificatorului pasul: „pentru fiecare rând, caută citatul pe linia citată și spune dacă apare întocmai". Un model poate face asta, dar nu determinist, deci rulează de două ori și compară.
