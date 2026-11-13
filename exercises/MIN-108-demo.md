# MIN-108: Demo, sistemul pe munca ta

**Sesiune:** 4, a doua parte · **Durată:** 25 minute · **Starea ta:** „Merge pe munca mea?"

## Povestea

Ai SSOT, spec și ghid. Le rulezi cap-coadă pe sursa ta și arăți ce a ieșit, inclusiv ce nu a mers.

## Pași

1. Ia sursa de la `MIN-104`, cu minuta de aur.
2. Rulează lanțul:
   1. Extractor → `ssot.md`
   2. `check_ssot.py` (dacă sursa are timestamps)
   3. Generator → rezultat în `project/output/`
   4. Verificator pe rezultat
   5. Corector de stil
3. Compară rezultatul cu minuta de aur.

   **Ce vezi?**
   - Zero critice, cel mult 2 ridicate → lanțul funcționează pe cazul tău.
   - Critice → spune care, și ce regulă le-ar fi prins. Acesta e tot un rezultat bun.
4. Pregătește 3 minute de prezentare: ce ai încercat, ce a prins sistemul, ce a ratat, ce faci săptămâna viitoare.

## Criterii de acceptare

- [ ] Lanțul complet rulat o dată
- [ ] Rezultatul comparat cu minuta de aur
- [ ] Un raport de conformitate
- [ ] Trei minute de prezentare: ce a prins, ce a ratat, ce urmează
- [ ] Un pas următor, unul singur, pe care îl faci în lucrul tău real

## După mentorat

Păstrează repo-ul. Pune sursele tale în `project/raw/`, regulile tale în `spec.md` și `style-guide.md`, și rulează sistemul la fiecare livrabil nou.
