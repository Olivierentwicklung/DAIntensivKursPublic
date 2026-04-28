# 🧪 Market Management Application

## 🎯 Goal

Build a full-stack application:

- Backend: Django + Django REST Framework
- Frontend: Angular
- Testing: Postman + DRF API Browser

---

## 📋 Requirements

You will build an application to manage:

- Markets
- Sellers
- Products

---

## 🧱 Entities

### 🏬 Market

    - name
    - location
    - description
    - net_worth
    - image_url

### 👤 Seller

    - name
    - contact_info
    - markets
    - image_url

➡ A seller can work in multiple markets

### 📦 Product

    - name
    - description
    - price
    - image_url
    - market
    - seller

➡ A product belongs to one market and one seller

---

## 🔗 ER Diagram

Before coding:

👉 Create an **Entity Relationship Diagram**

Relationships:

- One Market → Many Products
- One Seller → Many Products
- Many Sellers ↔ Many Markets

---

## ⚙️ Backend (Django + DRF)

### Tasks

    - Create models
    - Run migrations
    - Register models in admin
    - Create serializers
    - Create API views
    - Configure URLs

### Required Files

    - models.py
    - api/serializers.py
    - api/views.py
    - api/urls.py

---

## 🌐 API Endpoints

### Markets

    - GET /api/markets/
    - POST /api/markets/
    - GET /api/markets/{id}/
    - PUT /api/markets/{id}/
    - DELETE /api/markets/{id}/

### Sellers

    - GET /api/sellers/
    - POST /api/sellers/
    - GET /api/sellers/{id}/
    - PUT /api/sellers/{id}/
    - DELETE /api/sellers/{id}/

### Products

    - GET /api/products/
    - POST /api/products/
    - GET /api/products/{id}/
    - PUT /api/products/{id}/
    - DELETE /api/products/{id}/

---

## 🧪 Testing

Use:

- Postman
- DRF API Browser

Test:

- Create Market
- Create Seller
- Assign Seller to Market
- Create Product
- Update Product
- Delete Product
- List Products

---

## 🖥️ Frontend (Angular)

Create:

- Market List / Detail / Create / Edit
- Seller List / Detail / Create / Edit
- Product List / Detail / Create / Edit

---

## 🔌 Angular Services

Create:

- market.service.ts
- seller.service.ts
- product.service.ts

Each must include:

- getAll()
- getById()
- create()
- update()
- delete()

---

## ⭐ Bonus (Optional)

- Search products
- Filter by market/seller
- Form validation
- Pagination
- Authentication
- UI styling

---

## 📝 Submission

- ER Diagram
- Backend project
- Frontend project
- Screenshots or demo

---

## 📊 Grading

- ER Diagram — 15%
- Django Models — 20%
- Serializers — 15%
- Views & URLs — 15%
- API Testing — 10%
- Angular Components — 15%
- Angular Services — 10%

---

## 🚀 Good luck!
