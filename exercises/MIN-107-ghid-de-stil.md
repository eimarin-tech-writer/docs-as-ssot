# MIN-107: Stil care se poate testa

**Sesiune:** 4 · **Durată:** 55 minute · **Starea ta:** „Nu sună la fel de fiecare dată."

## Povestea

„Ton profesionist" nu se poate testa. „Fără adjective evaluative" se poate. Transformi preferințele de stil în reguli numerotate, apoi ceri unui agent să le verifice.

## Pași

### A. Citește ghidul (10 min)

1. Deschide `project/docs/style-guide.md`. Găsește o regulă care se verifică cu o căutare și una care cere judecată.

### B. Corectează trei texte (20 min)

2. Lipește `agents/corector-stil.md` într-o conversație nouă, apoi ghidul și textele de mai jos, pe rând.
3. Cere: „Raportează abaterile, cu numărul regulii."

   **T1**
   > Task: Ioana va rezolva rotunjirile, sigur până vineri!

   **T2**
   > Echipa a decis excelent să mute lansarea pe 12/21, din păcate Sorina nu apucă estimarea, TBD.

   **T3**
   > Ioana notează problema cu datele de productie copiate in mediul de test si Sorina trimite lista de cerinte luni si Catalin pregateste pdf-ul.

   **Ce vezi?**
   - Fiecare abatere are un număr de regulă → agentul lucrează conform ghidului.
   - O abatere fără număr → o „observație fără regulă". Decide: devine regulă (o adaugi) sau dispare.
4. Rescrie cele trei texte după ghid. Rulează din nou Corectorul pe versiunile tale.

### C. Ghidul tău (25 min)

5. Ia trei texte din munca ta, pe care le-ai corectat de mână în ultima lună.
6. Scoate din corecturi **opt reguli numerotate** (R-01…R-08), fiecare cu „cum verifici".
7. Scoate **cinci termeni** cu varianta preferată și variantele de evitat.
8. Scrie un text care încalcă una dintre regulile tale și dă-l Corectorului, cu ghidul tău. Prinde abaterea?

   **Ce vezi?**
   - Da, cu numărul regulii → regula e bine scrisă.
   - Nu → regula e vagă. Rescrie-o cu un criteriu da/nu.

## Criterii de acceptare

- [ ] Cele trei texte corectate, cu reguli citate
- [ ] Cel puțin o „observație fără regulă" tratată (regulă nouă sau eliminată)
- [ ] Ghidul tău: opt reguli numerotate, cinci termeni
- [ ] Un text de test care încalcă o regulă a ta și e prins de Corector

## Pasul următor

`MIN-108`: pui cele trei fișiere (SSOT, spec, ghid) pe lucrul tău real.
