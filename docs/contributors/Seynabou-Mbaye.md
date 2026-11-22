# Seynabou Mbaye

## Meta-Goals

### Target grade

Meine angestrebte Note liegt im Bereich von 1,0 bis 1,3.

### Personal goals

In diesem Modul möchte ich meine bisherigen Kenntnisse in Python weiterentwickeln und lernen, diese gezielt bei der Entwicklung von Webanwendungen anzuwenden. Zusätzlich möchte ich meine Fähigkeiten im Umgang mit Git und GitHub verbessern, um die Versionsverwaltung und die Zusammenarbeit an gemeinsamen Projekten sicherer zu beherrschen. Diese Erfahrungen sollen mir helfen, sowohl bei zukünftigen Studienprojekten als auch im späteren Berufsleben effektiv in Entwicklungsteams mitzuarbeiten.

---

## Eidesstattliche Erklärung

**[Seynabou Mbaye, Matrikelnr.: 77204233346]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

KI-Systeme (z.B. LLM-basierte Werkzeuge) habe ich ausschließlich als Hilfsmittel gemäß der Vorgaben im Modul eingesetzt. Insbesondere habe ich zu keiner Zeit und in keiner Weise agentische Systeme ("Agentic AI") genutzt. Jegliche Nutzung habe ich vollständig und gemäß der geltenden Regeln und Vorgaben an HWR Berlin und Fachbereich 1 dokumentiert. 

Mir ist bewusst, dass folgendes als Täuschungsversuch gewertet wird und zu einer Beurteilung der Modulleistung mit "nicht ausreichend" führt:

- Die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe;
- Die nicht vollständige Offenlegung genutzter KI-Systeme;
- Jegliche Nutzung von Agentic AI.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

## Vertical Feature Ownership

[First, briefly describe the vertical feature(s) that you owned.

Next, provide a **step-by-step walkthrough** of owned vertical feature(s) that examiner can follow in app. Ensure this matches actually implemented functionality.

**In addition**, supply ample proof of ownership, primarily through exemplary git commit traces. For every vertical feature you owned, maintain a table like this.]

| Activities | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| [Design Challenge research] | [Research traces](../product-discovery/01-design-challenge.md#raw-materia) | See left |
| [Refactor to use Flask Blueprints] | [d816e4](https://github.com/hwrberlin/fswd/commit/d816e4), [75a6c1](https://github.com/hwrberlin/fswd/commit/75a6c1) | [Flask Documentation](https://flask.palletsprojects.com/en/stable/blueprints/#the-concept-of-blueprints) |
|  |  |  |
|  |  |  |
|  |  |  |

---

## Portfolio Ownership

[Indicate your [Portfolio Ownership](https://hwrberlin.github.io/fswd/assessment.html#vertical-feature-and-portfolio-ownership). Usually, it will be sufficicent to just write something like: "I owned Portfolio **B** in our **4-person** team."

**In addition**, supply ample proof of ownership, primarily through work diary entries, git commit traces, and other useful artifacts. Maintain a table like this.]

| Portfolio Task | Proof |
| :-- | :-- |
| **Discovery Process** | |
| Plan discovery activities | [Discovery Plan](../product-discovery/material/02-up/.todo) |
| Maintain discovery evidence | *01.11.:* I reminded everybody to upload their discovery evidence |
| | *05.11.:* I checked all uploads for completeness |
**API** | |
| Integrate API behavior | [74a6b7](https://github.com/hwrberlin/fswd/commit/74a6b7) |
| | |
| | |

---

## AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :-- | :-- | :-- | :-- |
| 01 | Google Gemini ([Shared Conversation](https://share.gemini.google/zsTte9OSWPoG)) | Überarbeitung und Verbesserung der zuvor mit Proto.io erstellten Screens der Yuni-Plattform; Generierung von HTML-Code; Erstellung einer virtuellen interaktiven Web-App; Umsetzung und Anpassung von UI-Elementen und Funktionen. | HTML-Code und UI-Screens der Yuni-Web-App: Start Screen, Registrierung, Welcome Screen, Nachhilfe suchen, Nachhilfe anbieten, Community, Studien-Guides, Mein Profil, Favoriten, Logout und Einstellungen. | **Verwendete Prompts und Vorgehensweise:** 1. Überarbeitung der vorhandenen Screens: Anpassung der Beschriftung „Nachhilfe finden“ zu „Nachhilfe finden und suchen“, Vereinheitlichung der Header-Formatierung, Umstellung der Filteroptionen auf Dropdowns, Ergänzung von „(60 Minuten)“ beim Stundenpreis, Gestaltung eines Umschalters zwischen WhatsApp-Gruppen und Forum sowie Ergänzung eines „PDF herunterladen“-Links bei Studien-Guides. 2. Erstellung einer vollständigen interaktiven Web-App im Querformat für Yuni mit den Farben Korallenrot (#FA8785), Soft-Rosa (#FFBFC4), Weiß und Dunkelgrau. Ergänzung eines personalisierten Welcome Screens nach der Registrierung bzw. Anmeldung, eines Logout-Buttons und Einstellungen im Profil sowie einer Favoritenfunktion für Nachhilfeangebote und Forum-Beiträge über Herzsymbole. Dabei sollte das restliche Design unverändert bleiben. 3. Anpassung der Hochschulauswahl auf der Seite „Nachhilfe suchen“, sodass ausschließlich die HWR als Hochschule angegeben wird und das entsprechende Dropdown entfernt wird. 4. Wiederherstellung der vorherigen Version der Web-App mit ausschließlicher Änderung der Hochschulauswahl auf der Nachhilfe suchen-Seite. **Link zur Gemini-Konversation:** https://share.gemini.google/zsTte9OSWPoG |

