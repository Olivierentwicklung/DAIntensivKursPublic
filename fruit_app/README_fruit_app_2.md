# 🚀 Fruit App 2

Displays a list of fruits using **Django Templates** and a **list of dictionaries**.

## ⚙️ Features

- Displays a list of Fruits
- Displays information about each fruit
- Display a 404 page

## 🧪 Example Usage

- Get the app in Browser

  ```bash
   In Browser: http://127.0.0.1:8000/fruits/list/
  ```

---

## 🧠 What I Learned

- How to use a list of dictionaries
- How to use an if condition in a Django template
- How to use a `base.html` file with:
  - `{% load static %}`
  - `{% include "fruit_app/header.html" %}`
  - `{% block content %} {% endblock %}`
- How to extend a base template in another page
  - `{% extends 'fruit_app/base.html'%}`
  - `{% load static %}`

---

## 🛠️ Tech Details

**Key concepts:**

- Django views & urls
- Template rendering
- Reusable templates
- Navigation between templates
- Main 404 template
- Server-side rendering

**🎥 Demo:**

- Backend

  ![Demo](../z_screenshots/api-fruit-app-1.png)

- Frontend

  ![Demo](../z_screenshots/fruit_app_2_Olivier_Lowe.png)

---

## 🚀 Future Improvements

- Improve UI with CSS framework
- Add more complex API features (pagination, filtering)

---

➡️ [View Main README](/README.md#-fruit-app-2-django-templates)
