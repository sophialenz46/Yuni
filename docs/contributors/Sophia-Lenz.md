# Sophia Lenz

## Meta-Goals

### Target grade

Meine angestrebte Note liegt zwischen 1,0 und 1,3.

### Personal goals

Im Rahmen dieses Moduls möchte ich meine Kenntnisse in der Programmiersprache Python aufbauen und erweitern. Außerdem möchte ich lernen, Designentscheidungen fundiert und zielgerichtet zu treffen. Ein weiteres Ziel ist es, den sicheren Umgang mit GitHub zu erlernen, um das Tool später im Berufsalltag selbstständig und selbstbewusst einsetzen zu können. Darüber hinaus möchte ich ein besseres Verständnis für die Backend-Entwicklung von Websites gewinnen und nachvollziehen können, wie die technischen Prozesse im Hintergrund funktionieren.

---

## Eidesstattliche Erklärung

**[Sophia Lenz, Matrikelnr.: 77204989208]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

KI-Systeme (z.B. LLM-basierte Werkzeuge) habe ich ausschließlich als Hilfsmittel gemäß der Vorgaben im Modul eingesetzt. Insbesondere habe ich zu keiner Zeit und in keiner Weise agentische Systeme ("Agentic AI") genutzt. Jegliche Nutzung habe ich vollständig und gemäß der geltenden Regeln und Vorgaben an HWR Berlin und Fachbereich 1 dokumentiert. 

Mir ist bewusst, dass folgendes als Täuschungsversuch gewertet wird und zu einer Beurteilung der Modulleistung mit "nicht ausreichend" führt:

- Die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe;
- Die nicht vollständige Offenlegung genutzter KI-Systeme;
- Jegliche Nutzung von Agentic AI.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.




---

## Vertical Feature Ownership

I owned the **Community feature (Forum + WhatsApp Groups)**.

My responsibilities included implementing the Community navigation, displaying and sharing WhatsApp groups, creating and answering forum questions, managing the related database tables (`beitrag`, `antwort`, `gruppe`), and providing the forum API.

**Step-by-step walkthrough:**

Is missing

| Activities | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Implement Community page and navigation between WhatsApp Groups and Forum |[248de89](https://github.com/sophialenz46/Yuni/commit/248de89e21aa75c22a98c2eb94f63812552732b9) | HTML & CSS Documentation |
| Implement WhatsApp group overview (`GET /community/gruppen`) |  | Flask Documentation |
| Implement WhatsApp group sharing (`GET`, `POST /community/gruppen/teilen`) |  | Flask Documentation |
| Implement validation of WhatsApp invitation links and prevent duplicates | | Flask Documentation |
| Implement Forum overview (`GET /community/forum`) with categories and newest posts first | | Flask Documentation |
| Implement reply counts and relative timestamps for forum posts |  | Python Documentation |
| Implement creating forum questions (`GET`, `POST /community/forum/frage`) | | Flask Documentation |
| Implement individual forum post pages (`GET /community/forum/<id>`) | | Flask Documentation |
| Implement forum replies (`POST /community/forum/<id>/antwort`) | | Flask Documentation |
| Create database tables `Beitrag`, `Antwort`, and `Kategorie` with relationships to users, degree programs, and modules | [1729b96](https://github.com/sophialenz46/Yuni/commit/1729b96ea1e7ce95b8846edcb5c8d1f8e82f120a) | SQLAlchemy Documentation |
| Implement Forum API (`GET /api/forum`) with JSON responses and authentication |  | Flask Documentation |

---

## Portfolio Ownership

I owned Portfolio **B** in our **4-person** team.

| Portfolio Task | Concrete Tasks at Yuni | Proof |
| :-- | :-- | :-- |
| **App Scope** | | |
| Synthesize discovery findings | Translate survey results into Demand Side, Supply Side, and the three core application features. | |
| Maintain the value proposition | Update the value proposition according to current project decisions, such as contact via email and hiding or deleting offers, and ensure consistency with the implemented application. | |
| Control project scope | Prioritize the main user journeys (searching for and offering tutoring). Postpone additional features, such as English-language support and tutoring requests, until the core functionality works. | |
| Maintain feedback response | Document and evaluate feedback from peer reviews and the lecturer, including feedback about the guest role. Record whether feedback was accepted or rejected and explain the decisions. | |
| **Data Integration** | | |
| Integrate the data model | Combine all database tables (`user`, `guide`, `favorit`, `angebot`, `studiengang`, `modul`, `beitrag`, `antwort`, `gruppe`) into one consistent Entity Relationship Diagram (ERD) with uniform naming conventions. |[77ec260](https://github.com/sophialenz46/Yuni/commit/77ec26044409d45ecc775cc0d72c55c74f65625c) |
| Coordinate data constraints | Ensure primary keys, foreign keys, uniqueness constraints, and deletion rules. This includes unique email addresses and usernames, preventing duplicate favorites and WhatsApp group links, and ensuring correct data deletion when an account is deleted. | |
| Review schema changes | Ensure database changes from different vertical features do not introduce duplicate concepts or inconsistent relationships. Shared tables such as `studiengang` and `modul` must be reused across features, and the `sprache` field belongs to the `user` table. | |
| Verify database readiness | Verify that database initialization works, the SQLite database contains functional example data, and the documented ERM matches the actual implementation. | |

---

