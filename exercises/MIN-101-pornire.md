# MIN-101: Pornire

**Sesiune:** 1 · **Durată:** 10 minute · **Starea ta:** „Merge setup-ul?"

## Povestea

Înainte să construiești ceva, dovedești că ai mediul și că înțelegi regula de bază: ce înseamnă un rând ancorat în sursă.

## Pași

1. Clonează repo-ul și deschide folderul.
2. Rulează:
   ```
   python3 tools/check_ssot.py project/docs/ssot.exemplu.md project/raw/sedinta-nimbus.txt
   ```

   **Ce vezi?**
   - `Verdict: TRECE` → continuă la pasul 3.
   - `command not found` sau eroare Python → instalează Python 3 și încearcă din nou. Dacă nu poți, spune-i mentorului: lucrezi fără script (vezi `docs/tools.md`).
3. Deschide `project/raw/sedinta-nimbus.txt`. Citește primele 12 linii.
4. Alege un rând din `ssot.exemplu.md` și găsește-i citatul în transcript, la locul indicat.

   **Ce vezi?**
   - Citatul apare pe linia indicată, cuvânt cu cuvânt → ai înțeles regula.
   - Nu îl găsești → verifică dacă ai căutat la `Loc`, nu în tot textul.
5. Citește `AGENTS.md` (două minute).

## Criterii de acceptare

- [ ] Scriptul a rulat și a afișat `TRECE` (sau ai notat că lucrezi fără el)
- [ ] Ai găsit manual un citat din SSOT în transcript
- [ ] Poți spune într-o propoziție de ce „cred că vineri" nu e același lucru cu „vineri"

## Pasul următor

`MIN-102`: scoți tu singur un SSOT din transcript.
