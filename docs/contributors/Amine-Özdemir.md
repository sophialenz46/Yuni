# Amine Özdemir

## Meta-Goals

### Target grade

Meine angestrebte Note liegt zwischen 1,0 und 1,3.

### Personal goals

Im Rahmen dieses Moduls möchte ich meine bisherigen Kenntnisse in Python vertiefen und lernen, diese bei der Entwicklung von Webanwendungen praktisch anzuwenden. Darüber hinaus möchte ich ein besseres Verständnis für die Frontend- und Backend-Entwicklung sowie deren Zusammenspiel gewinnen. Ein weiteres Ziel ist es, meine Fähigkeiten im Umgang mit Git und GitHub auszubauen, um die Versionsverwaltung sicherer zu beherrschen und die Zusammenarbeit an gemeinsamen Projekten zu verbessern. Diese Kenntnisse möchte ich sowohl in zukünftigen Studienprojekten als auch im späteren Berufsleben nutzen, um effektiv in Entwicklungsteams mitarbeiten zu können.

---

## Eidesstattliche Erklärung

**[Amine Özdemir, Matrikelnr.: 77209818149]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

KI-Systeme (z.B. LLM-basierte Werkzeuge) habe ich ausschließlich als Hilfsmittel gemäß der Vorgaben im Modul eingesetzt. Insbesondere habe ich zu keiner Zeit und in keiner Weise agentische Systeme ("Agentic AI") genutzt. Jegliche Nutzung habe ich vollständig und gemäß der geltenden Regeln und Vorgaben an HWR Berlin und Fachbereich 1 dokumentiert. 

Mir ist bewusst, dass folgendes als Täuschungsversuch gewertet wird und zu einer Beurteilung der Modulleistung mit "nicht ausreichend" führt:

- Die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe;
- Die nicht vollständige Offenlegung genutzter KI-Systeme;
- Jegliche Nutzung von Agentic AI.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

## Vertical Feature Ownership

I owned the **Account feature (registration, login/logout with access control, settings, account deletion)** together with the **start page, welcome page, and master data (degree programs and modules)**.

My responsibilities included the `user` table, registration restricted to HWR student email addresses, login and logout with sessions, the shared access control (`@login_required`) used by all other features, the settings page (change name, change password), deleting an account including all related data across features, the tables `studiengang` and `modul` with example data, and the profile API.

### Step-by-step walkthrough

*Will be added once the feature is fully implemented.*

### Proof of ownership

| Activities | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Set up shared Flask app (`app.py`) and `requirements.txt` | [d18ee3f](https://github.com/sophialenz46/Yuni/commit/d18ee3f) | [Lecture notebook: Full-stack web development](https://hwrberlin.github.io/fswd/fswd-intro.html) |
| Implement start page (`GET /`) with header, navigation, registration/login box and feature cards | [bf04ae1](https://github.com/sophialenz46/Yuni/commit/bf04ae1) | [Lecture notebook: HTML + CSS](https://hwrberlin.github.io/fswd/html-css.html) |
| Create database tables `studiengang` and `modul` with example data | | [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.readthedocs.io/) |
| Create database table `user` with unique username and email | | [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.readthedocs.io/) |
| Implement registration (`GET`, `POST /registrieren`) restricted to `@stud.hwr-berlin.de` addresses | | [Flask Documentation](https://flask.palletsprojects.com/), [WTForms Documentation](https://wtforms.readthedocs.io/) |
| Implement password hashing and checking | | [Werkzeug Documentation](https://werkzeug.palletsprojects.com/) |
| Implement login (`GET`, `POST /anmelden`) and logout (`POST /abmelden`) with sessions | | [Flask Documentation](https://flask.palletsprojects.com/) |
| Implement access control (`@login_required`) with redirect for pages and 401 for API routes | | [Flask Documentation](https://flask.palletsprojects.com/) |
| Provide `current_user` for all templates | | [Flask Documentation](https://flask.palletsprojects.com/) |
| Implement welcome page (`GET /willkommen`) | | [Flask Documentation](https://flask.palletsprojects.com/) |
| Implement profile header component (used on the profile page) | | [Jinja Documentation](https://jinja.palletsprojects.com/) |
| Implement settings: change name (`GET`, `POST /einstellungen`) | | [Flask Documentation](https://flask.palletsprojects.com/) |
| Implement settings: change password (`POST /einstellungen/passwort`) | | [Werkzeug Documentation](https://werkzeug.palletsprojects.com/) |
| Implement account deletion (`POST /konto/loeschen`) including all related data | | [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.readthedocs.io/) |
| Implement Profile API (`GET /api/profil`) with JSON response and authentication | | [Flask Documentation](https://flask.palletsprojects.com/) |

---

## Portfolio Ownership

I owned Portfolio **D** in our **4-person** team.

| Portfolio Task | Concrete Tasks at Yuni | Proof |
| :-- | :-- | :-- |
| **Product Rules** | | |
| Identify shared product rules | Make important rules explicit: registration only with HWR student email, guests only see the start, login and registration pages, the university is fixed to HWR Berlin, only the creator may hide or delete an offer, only active offers are visible, no contact button on one's own offer, each favorite exists only once, deleting an account removes all of the person's data. | |
| Integrate domain behavior | Ensure that vertical features do not implement contradictory or duplicated rules: login checks only via `@login_required`, filter logic as one shared function for search page and API, favorite logic in one place only. | |
| Align HTML and API behavior | Ensure that human-facing pages and API endpoints enforce the same rules: `/api/angebote` returns the same (only active) offers as the search page with the same filters; guests receive 401 from the API instead of a redirect. | |
| **Documentation Quality** | | |
| Maintain documentation structure | Ensure that all required Markdown pages are present, linked, and published via GitHub Pages. | |
| Coordinate documentation quality | Check consistent terminology, readable Markdown, correct diagrams (ERM), and valid code references in the documentation. | |
| Review design decisions | Ensure that every team member has at least two design decisions in the mandatory format with evidence of how the options were evaluated (e.g., branches). | |
| Verify contribution documentation | Ensure that all four contribution pages cover all mandatory sections and that every claim is backed by proof such as git commits. | |
| **Repository Delivery** | | |
| Coordinate release identification | Ensure that the submission commit contains the latest integrated work of all four features, including documentation. | |
| Verify readme instructions | Test the README on Windows and macOS: clone, install, initialize the database, start the app, log in with a demo account, and complete the happy path within 10 minutes. | |

---