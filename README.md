# Documentație ca SSOT: un sistem de lucru cu AI care rămâne în sursă

Repo de lucru pentru mentoratul **Get AI Conversations Right** (Product Makers Romania). Nu e un tutorial. E un proiect mic, cu reguli, agenți, teste și un verificator care rulează, pe care îl clonezi, îl folosești în fiecare sesiune și îl iei cu tine.

Ideea: AI-ul scrie bine, dar inventează, interpretează și uită instrucțiuni. În loc să verifici tot de mână, **ancorezi** rezultatul într-o sursă unică de adevăr (SSOT), **scrii dinainte** ce vrei, **testezi** că regulile țin și **separi** cine generează de cine verifică.

**Pentru cine e:** oameni care folosesc deja AI la muncă și vor să aibă încredere în ce iese. Nu cere cod. Cere Python 3 pentru un singur script.

## Pornire

```
git clone https://github.com/eimarin-tech-writer/docs-as-ssot.git
cd docs-as-ssot
python3 tools/check_ssot.py project/docs/ssot.exemplu.md project/raw/sedinta-nimbus.txt
```

Dacă vezi `Verdict: TRECE`, ești gata. Apoi deschide `exercises/MIN-101-pornire.md`.

Fără Python? Poți face tot cu agenții, în orice unealtă, și sari peste script. Pierzi garanția deterministă a verificării de citate, deci rulează Verificatorul cu mai multă atenție. Vezi `docs/tools.md`.

## Ce e în repo

| Piesă | Unde | Ce te învață |
|---|---|---|
| Regula proiectului | `AGENTS.md` | ce nu are voie să uite niciun agent |
| Sursa de exercițiu | `project/raw/sedinta-nimbus.txt` | transcript fictiv, cu capcanele din ședințele reale |
| SSOT | `project/docs/ssot.*.md` | cum arată o afirmație ancorată |
| Specificație | `project/docs/spec.template.md` | cum scrii ce vrei, înainte de generare |
| Ghid de stil | `project/docs/style-guide.md` | stil ca reguli numerotate, verificabile |
| Agenți | `agents/` | instrucțiuni gata de lipit pentru Extractor, Generator, Verificator, Autor de spec, Corector de stil |
| QA | `qa/` | severitate, fișă de constatare, teste, raport |
| Verificator automat | `tools/check_ssot.py` | regula impusă, nu doar scrisă |
| Exerciții | `exercises/` | un tichet per pas, cu criterii de acceptare |

## Exercițiile

Fiecare exercițiu e un tichet: o poveste, pași cu verificare după fiecare, criterii de acceptare. Lucrul e gata când toate criteriile sunt îndeplinite.

| Tichet | Sesiune | Starea din care pleci | Ce produci |
|---|---|---|---|
| `MIN-101` | 1 | „Merge setup-ul?" | verificator rulat pe exemplu |
| `MIN-102` | 2 | „Nu am încredere în ce iese" | `ssot.md` din transcript |
| `MIN-103` | 2 | „Cum prind ce n-am văzut?" | fișe de constatare pe un SSOT plantat |
| `MIN-104` | acasă | „Cum arată documentul perfect?" | sursa ta + minuta de aur |
| `MIN-105` | 3 | „Face altceva decât am cerut" | `spec.md` + `tests.md` + raport |
| `MIN-106` | acasă | „O regulă a picat" | regulă rescrisă + a doua rulare |
| `MIN-107` | 4 | „Nu sună la fel de fiecare dată" | `style-guide.md` + corector |
| `MIN-108` | 4 | „Merge pe munca mea?" | sistemul rulat pe sursa ta reală |

## Cazul tău

Sesiunile se fac pe ședința demo, ca toți să vadă același lucru. Temele (`MIN-104`, `MIN-108`) le faci pe sursa ta. Ce se schimbă:

| Sursa ta | „Citat" înseamnă | „Loc" înseamnă | Regulă de pornit |
|---|---|---|---|
| transcript de ședință | replica | `hh:mm:ss` | responsabilul apare doar dacă e numit |
| capitol de curs sau carte | fraza | pagina | niciun articol sau definiție din afara textului |
| material de training | fraza sau obiectivul | modul sau slide | nu adăuga module necerute |
| documentație de produs (câmpuri, API) | definiția | câmp sau versiune | termenii vin doar din glosar |

Scriptul `check_ssot.py` citește transcripturi cu `[hh:mm:ss]`. Pentru alte surse adaptezi expresia `LINIE` din script sau folosești doar Verificatorul; `MIN-104` explică.

## Cum folosești mai multe unelte

Nu contează dacă lucrezi în Claude, ChatGPT, Gemini sau Copilot. „Agent" înseamnă o conversație separată, cu instrucțiunile din `agents/` lipite la început. Cine generează nu verifică, așa că folosești două conversații, fie în aceeași unealtă, fie în unelte diferite. Detalii în `docs/tools.md`.

## Ce NU face sistemul

- Nu garantează că un model respectă o regulă. O regulă scrisă e o cerință. De aceea există teste, trei rulări și verificator.
- Scriptul nu înțelege sensul. Prinde un citat inventat, nu prinde o discuție transformată în decizie.
- Nu repară surse proaste. Dacă sursa e un e-mail pe care nu îl fixezi nicăieri, SSOT-ul nu are din ce să se hrănească.

## Cum se citește mai departe

Începe cu `docs/how-this-works.md` (zece minute, o buclă, un glosar).

## Licență

MIT, vezi `LICENSE`. Copyright © 2026 Eliza Marin. Poți folosi, copia și adapta liber; păstrează nota de copyright.
