# 🚀 Public Django Projects

This repository contains several small applications built with **Python and Django** to practice backend development, API design, and frontend integration.

The goal of these projects is to explore different ways of building and consuming web applications using Django.

---

## 🧱 Tech Stack

- Python
- Django
- HTML / CSS
- JavaScript (Fetch API)

---

## 📦 Projects Overview

### 🔹 Tech Gadgets App

Displays a list of gadgets and their manufacturers using **Django Templates** and a **dummy-data JSON**.

**Key concepts:**

- Django views & urls
- Template rendering
- Server-side rendering

**🎥 Demo:**

![Demo](z_screenshots/Module_05_aufgabe_as_landingpage_1_Olivier_Lowe.png)

➡️ [View detailed README](tech_gadgets/README_tech_gadgets.md)

---

### 🔹 Fruit App 1 (API + External Frontend)

Provides a **JSON API** built with Django, consumed by an external frontend using JavaScript.

**Key concepts:**

- Building API endpoints
- JSON responses
- Frontend integration with Fetch API

**🎥 Demo:**

![Demo](z_screenshots/fruit_app_1_Olivier_Lowe.png)

➡️ [View detailed README](fruit_app/README_fruit_app_1.md)

---

### 🔹 Fruit App 2 (Django Templates)

Displays a list of fruits using **Django Templates** and a **list of dictionnaries**.

**Key concepts:**

- Django views & urls
- Template rendering
- Reusable templates
- Navigation between templates
- Main 404 template
- Server-side rendering

**🎥 Demo:**

![Demo](z_screenshots/fruit_app_2_Olivier_Lowe.png)

➡️ [View detailed README](fruit_app/README_fruit_app_2.md)

---

## ⚙️ Setup

```bash
git clone https://github.com/Olivierentwicklung/DAIntensivKursPublic.git


python -m venv .venv
.venv\Scripts\activate  # on Windows

pip install -r requirements.txt
python manage.py runserver
```

---

## 🧠 What I Learned

- How to structure Django projects with multiple apps
- Differences between server-rendered pages and API-based architecture
- How to connect a Django backend with a JavaScript frontend

---

## 🚀 Future Improvements

- Add authentication system
- Improve UI with CSS framework
- Add more complex API features (pagination, filtering)
