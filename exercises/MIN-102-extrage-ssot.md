# MIN-102: Extrage un SSOT din transcript

**Sesiune:** 2 · **Durată:** 25 minute · **Starea ta:** „Nu am încredere în ce iese."

## Povestea

Ai un transcript de ședință. Vrei un tabel în care fiecare afirmație are sursă, ca să poți construi minuta pe el fără să recitești tot.

## Pași

1. Deschide o conversație nouă în unealta ta. Lipește `agents/extractor.md`, apoi atașează `project/raw/sedinta-nimbus.txt`.
2. Cere: „Extrage SSOT-ul din transcript."
3. Salvează tabelul în `project/docs/ssot.md`.
4. Rulează:
   ```
   python3 tools/check_ssot.py project/docs/ssot.md project/raw/sedinta-nimbus.txt
   ```

   **Ce vezi?**
   - `TRECE` → treci la pasul 5.
   - `PICĂ` cu `G-01` (citatul nu apare) → modelul a parafrazat în loc să copieze. Cere-i: „Copiază citatul întocmai din transcript" și rulează iar.
   - `PICĂ` cu `G-02` sau `G-03` → ai o regulă care nu ține. Notează care, o folosești la `MIN-105`.
5. Compară cu ce ai găsit tu citind: lipsește vreo decizie, acțiune sau risc? Adaugă-l manual sau cere-i modelului să-l caute, tot cu citat.

   **Ce vezi?**
   - Nimic nu lipsește → verifică încă o dată linia `00:07:10` (o cifră a fost corectată) și `00:08:05` (cine pregătește PDF-ul).
   - Lipsește ceva → înseamnă că scriptul nu l-ar fi prins niciodată: scriptul verifică ce e în tabel, nu ce lipsește.

## Criterii de acceptare

- [ ] `ssot.md` există și `check_ssot.py` dă `TRECE`
- [ ] Zero rânduri cu citat parafrazat
- [ ] „Cred că vineri" apare cu `dedus` și marcaj de incertitudine
- [ ] Propunerea de a muta lansarea nu apare ca `decizie`
- [ ] Estimarea către client are responsabil `nenumit`
- [ ] Cifra bugetului este cea corectată (25.000), cu citat

## Constrângeri

Nu edita `project/raw/`. Nu cere modelului „să completeze ce lipsește".

## Pasul următor

`MIN-103`: primești un SSOT făcut de altcineva și afli ce e greșit în el.
