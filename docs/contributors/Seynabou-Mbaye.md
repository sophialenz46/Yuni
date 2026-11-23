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

# Vertical Feature Ownership

I owned the Tutoring feature (offering, searching, managing, and contacting).

My responsibilities included implementing the creation of tutoring offers, the search with filters, and the contact via email. I also managed the related database table (angebot) and provided the tutoring API (/api/angebote) with its filter logic.

## Step-by-step walkthrough

| Activities | Proof, e.g., git commits | Sources used |
|---|---|---|
| Implement the form to create a tutoring offer (GET, POST) with validation and flash messages | | Flask Documentation |
| Implement tutoring search page showing only active offers | | Flask Documentation |
| Implement filter logic (e.g., degree program, module) as one shared function for search page and API | | Python Documentation |
| Implement offer detail view with contact via email | | Flask Documentation |
| Hide the contact button on a user's own offers | | Jinja2 Documentation |
| Implement empty states and confirmation feedback for the tutoring pages | | Jinja2 Documentation |
| Create database table angebot with relationships to user, studiengang, and modul | | SQLite Documentation |
| Implement tutoring API (GET /api/angebote) with the same filters as the search page, JSON responses, and authentication (401 for guests) | | Flask Documentation |

# Portfolio Ownership

I owned Portfolio A in our 4-person team.

| Portfolio Task | Concrete Tasks at Yuni | Proof |
|---|---|---|
| **Discovery Process** | | |
| Plan discovery activities | Document and justify the research questions, the target group (students at HWR), and the method (anonymous online survey with 40 participants). | |
| Maintain discovery evidence | Store the survey and its results as raw material in the evidence folder and keep evidence clearly separated from assumptions. | |
| Identify discovery gaps | Check which statements in the value proposition and happy paths are not supported by the survey and note open questions for further investigation. | |
| **API** | | |
| Define the API purpose | Justify for /api/angebote, /api/forum, /api/guides, and /api/profil who would use each endpoint in a machine-facing way. | |
| Integrate API behavior | Ensure a uniform JSON format, status codes (200, 401, 404), and error responses across all four endpoints. | |
| Verify API readiness | Document example calls for success and failure cases and test them in the submission version. | |


---

## AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :-- | :-- | :-- | :-- |
| 01 | Google Gemini ([Shared Conversation](https://share.gemini.google/zsTte9OSWPoG)) | Überarbeitung und Verbesserung der zuvor mit Proto.io erstellten Screens der Yuni-Plattform; Generierung von HTML-Code; Erstellung einer virtuellen interaktiven Web-App; Umsetzung und Anpassung von UI-Elementen und Funktionen. | HTML-Code und UI-Screens der Yuni-Web-App: Start Screen, Registrierung, Welcome Screen, Nachhilfe suchen, Nachhilfe anbieten, Community, Studien-Guides, Mein Profil, Favoriten, Logout und Einstellungen. | **Verwendete Prompts und Vorgehensweise:** 1. Überarbeitung der vorhandenen Screens: Anpassung der Beschriftung „Nachhilfe finden“ zu „Nachhilfe finden und suchen“, Vereinheitlichung der Header-Formatierung, Umstellung der Filteroptionen auf Dropdowns, Ergänzung von „(60 Minuten)“ beim Stundenpreis, Gestaltung eines Umschalters zwischen WhatsApp-Gruppen und Forum sowie Ergänzung eines „PDF herunterladen“-Links bei Studien-Guides. 2. Erstellung einer vollständigen interaktiven Web-App im Querformat für Yuni mit den Farben Korallenrot (#FA8785), Soft-Rosa (#FFBFC4), Weiß und Dunkelgrau. Ergänzung eines personalisierten Welcome Screens nach der Registrierung bzw. Anmeldung, eines Logout-Buttons und Einstellungen im Profil sowie einer Favoritenfunktion für Nachhilfeangebote und Forum-Beiträge über Herzsymbole. Dabei sollte das restliche Design unverändert bleiben. 3. Anpassung der Hochschulauswahl auf der Seite „Nachhilfe suchen“, sodass ausschließlich die HWR als Hochschule angegeben wird und das entsprechende Dropdown entfernt wird. 4. Wiederherstellung der vorherigen Version der Web-App mit ausschließlicher Änderung der Hochschulauswahl auf der Nachhilfe suchen-Seite. **Link zur Gemini-Konversation:** https://share.gemini.google/zsTte9OSWPoG |

