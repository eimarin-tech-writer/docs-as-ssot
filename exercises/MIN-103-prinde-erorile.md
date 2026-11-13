# MIN-103: Prinde erorile

**Sesiune:** 2 · **Durată:** 25 minute · **Starea ta:** „Cum prind ce n-am văzut?"

## Povestea

Un coleg a scos un SSOT din aceeași ședință. Nu ai încredere în el. Cauți erorile în două feluri și vezi ce prinde fiecare.

## Pași

1. Rulează scriptul pe tabelul colegului:
   ```
   python3 tools/check_ssot.py project/docs/ssot.de-verificat.md project/raw/sedinta-nimbus.txt
   ```
   Notează fiecare rând semnalat și ce regulă l-a prins.

   **Ce vezi?**
   - Verdict `PICĂ` cu mai multe constatări → ai o primă listă.
   - `TRECE` → verifică că ai folosit fișierul `de-verificat`, nu `exemplu`.
2. Deschide o conversație **nouă**. Lipește `agents/verificator.md`. Atașează transcriptul, tabelul `ssot.de-verificat.md` și `qa/severity.md`.
3. Cere: „Verifică tabelul. Scrie o fișă de constatare pentru fiecare problemă și un verdict."
4. Compară cele două liste: ce a prins doar scriptul? Ce a prins doar Verificatorul?

   **Ce vezi?**
   - Verificatorul a prins ce scriptul a ratat (sens, nu prezență) → straturile se completează, exact cum trebuie.
   - Verificatorul a ratat ceva ce scriptul a prins → instrucțiunile lui nu insistă pe citate. Adaugă-i regula și rulează iar.
   - Verificatorul a „găsit" probleme fără dovadă din sursă → cere fișa completă, cu loc și citat. O fișă fără dovadă nu se ia în seamă.
5. Caută ce **lipsește** din tabel: citește transcriptul și enumeră ce nu apare.

## Criterii de acceptare

- [ ] Lista scriptului: rândurile semnalate, cu regula
- [ ] Cel puțin trei fișe de constatare de la Verificator, în formatul din `qa/finding-card.md`
- [ ] Cel puțin o eroare pe care scriptul n-a putut s-o prindă și de ce
- [ ] Cel puțin două lucruri care lipsesc din tabel
- [ ] Un rând pe care l-ai găsit corect (fără fals pozitiv)

## Pasul următor

`MIN-104` acasă: îți alegi propria sursă și scrii rezultatul corect de mână.
