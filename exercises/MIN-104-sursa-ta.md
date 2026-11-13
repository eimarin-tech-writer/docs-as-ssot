# MIN-104: Sursa ta și minuta de aur

**Sesiune:** acasă, după sesiunea 2 · **Durată:** ~60 minute · **Starea ta:** „Cum arată documentul perfect?"

## Povestea

Până acum ai lucrat pe sursa mea. Acum aduci a ta. Și scrii, **de mână**, rezultatul corect. Acela e **minuta de aur**: răspunsul la „cum aș recunoaște documentul perfect?", și setul tău de test pentru restul mentoratului.

## Pași

1. Alege o sursă pe care o cunoști bine, scurtă (20–30 de minute de ședință, sau 3–5 pagini). Anonimizeaz-o dacă are date sensibile.
   - Datele de la job rămân în contul de la job. Verifică politica angajatorului înainte să le pui în orice altă unealtă.
2. Pune-o în `project/raw/`. Folderul e ignorat de Git: nu se urcă.
3. **Scrie de mână** rezultatul corect, fără AI: ce ai vrea să scoată sistemul. Ține-l într-un fișier `minuta-de-aur.md`.

   **Ce vezi?**
   - Poți face lista în câteva minute → sursa e bună.
   - Nu știi ce ar trebui să iasă → sursa e prea lungă sau prea vagă. Alege alt fragment.
4. Adaptează formatul la sursa ta, după tabelul din `README.md`, secțiunea „Cazul tău". Dacă sursa nu are `[hh:mm:ss]`, notează cum arăți „Loc" (pagină, modul, câmp).
5. Rulează agentul Extractor pe sursa ta. Dacă sursa nu are timestamps, scriptul nu o citește fără modificări: folosește doar Verificatorul sau adaptează expresia `LINIE` din `tools/check_ssot.py`.
6. Compară cu minuta de aur: ce lipsește? Ce e în plus? Ce e greșit?

## Criterii de acceptare

- [ ] Sursa ta, în `project/raw/`
- [ ] `minuta-de-aur.md`, scrisă înainte de a vedea rezultatul AI-ului
- [ ] Un SSOT scos de Extractor pe sursa ta
- [ ] O listă scurtă: câte rânduri sunt corecte, câte greșite, câte lipsesc
- [ ] Un tip de greșeală pe care o recunoști ca fiind a ta (inventat, atribuit greșit, omis, interpretat)

## Pasul următor

`MIN-105`: scrii ce vrei de la sursa asta, ca specificație, și o testezi.
