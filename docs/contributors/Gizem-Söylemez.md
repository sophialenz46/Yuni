# Gizem Söylemez

## Meta-Goals

### Target grade

Meine angestrebte Note liegt zwischen 1,0 und 1,3. 

### Personal goals

Meine persönlichen Lernziele im Rahmen dieses Moduls umfassen insbesondere die Vertiefung meiner bisherigen Python-Kenntnisse sowie den Ausbau meines Verständnisses für Backend-Prozesse bei der Entwicklung von Webanwendungen. 
Darüber hinaus möchte ich mein Verständnis für das Zusammenspiel zwischen Frontend und Backend erweitern. Ebenso möchte ich meine Kenntnisse im Umgang mit Git und GitHub vertiefen, um mehr Sicherheit bei der gemeinsamen Programmierarbeit in Teams zu gewinnen und mich besser auf die Zusammenarbeit in Entwicklungsteams im späteren Berufsleben vorzubereiten.

---

## Eidesstattliche Erklärung

**[Gizem Söylemez, Matrikelnr.: 77203702868]**

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

I owned the __Study Guides and Personal Area feature__(study guides, profile page, favorites, my offers)

My responsibilities included the tables __guide__ and __favorit__, the study guides page with guide view, PDF download and checklists, the heart component for saving offers, posts and groups as favorites, the profile page with the favorites lost and the "My offers" section (hide, show and delete own offers only) and the guides API. 

### Step-by-step walkthrough
will be added once the feature is fully implemented.

Next, provide a **step-by-step walkthrough** of owned vertical feature(s) that examiner can follow in app. Ensure this matches actually implemented functionality.

## Proof of ownership 

| Activities | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| [Design Challenge research] | [Research traces](../product-discovery/01-design-challenge.md#raw-materia) | See left |
| [Refactor to use Flask Blueprints] | [d816e4](https://github.com/hwrberlin/fswd/commit/d816e4), [75a6c1](https://github.com/hwrberlin/fswd/commit/75a6c1) | [Flask Documentation](https://flask.palletsprojects.com/en/stable/blueprints/#the-concept-of-blueprints) |
|  |  |  |
|  |  |  |
|  |  |  |

---

## Portfolio Ownership

I owned Portfolio **C** in our **4-person** team. 

**In addition**, supply ample proof of ownership, primarily through work diary entries, git commit traces, and other useful artifacts. Maintain a table like this.]

| Portfolio Task | Concrete Tasks at Yuni | Proof |
| :-- | :-- |:--
| **User Experience** |||
|Maintain the central user journey | Ensure that all vertical features form one coherent flow: start page, registration and login, welcome page, tutoring search, study guides and profile. ||
|Integrate navigation and page structure | Provide a shared base template (base.html) with navigation and footer, make all pages extend it and keep page headers consistent.|9e96476, 475e679, 6086b5e, 7d85b19|
|Integrate forms and feedback|Ensure consistent labels, success and error messages and empty states in all forms and lists.||
|Maintain UI terminology| Ensure one term per concept in app and documentation (e.g "Studien-Guides", informal "du", German page language).
||
**Design + Code**|||
|Enforce software-design boundaries|Ensure compliance with the mandatory structure: no JavaScript except Bootstraps's, only Flask, Jinja2 and SQLite.||
|Integrate cross-cutting code conventions|Agree on shared conventions: naming of route functions, consistent CSS units, static files via url_for, @login_required for access control, 404 for unknown IDs.||
|Monitor code integration|Keep main runnable while all members commit directly to main; detect and resolve any (merge-) conflicts.|_**18.11:**_ I proposed working rules for committing directly to main in our team meeting: 1. pull before starting work, 2. announce changes to shared files (app.py, db.py, requirements.txt, base.html, style.css) beforehand and confirm once pushed, 3. start the app and check that all pages load before every push, 4. always keep commit messages clear and understandable.|
| | |

---
