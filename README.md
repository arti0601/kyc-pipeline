 # 🚀 KYC Pipeline Service

A minimal backend system for handling merchant KYC onboarding, built using **Django** and **Django REST Framework**.

This project simulates a real-world KYC workflow with state transitions, reviewer queues, and access control.

---

## ✨ Features

* 🧾 Merchant KYC submission flow
* 🔁 Centralized state machine for status transitions
* 🧑‍💼 Reviewer queue with SLA tracking
* 🔐 Role-based access control (Merchant / Reviewer)
* ⚠️ Proper error handling for invalid actions

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** SQLite (default)
* **API Testing:** Postman

---

## ⚙️ Setup Instructions

```bash
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## 🔑 Authentication

This project uses simple header-based auth:

```
username: merchant1
username: reviewer1
```

---

## 📡 API Endpoints

### 🧑 Merchant

**Create KYC Submission**

```
POST /api/v1/create/
```

---

### 🔄 Update KYC Status

```
POST /api/v1/<id>/update/
```

**Example Body:**

```json
{
  "status": "submitted"
}
```

---

### 🧑‍💼 Reviewer

**View Review Queue**

```
GET /api/v1/queue/
```

---

## 🔁 State Machine

Allowed transitions:

```
draft → submitted → under_review → approved/rejected
                           ↓
                more_info_requested → submitted
```

Invalid transitions return:

```
400 Bad Request
```

---

## 🧪 Example Workflow

1. Merchant creates submission → `draft`
2. Merchant submits → `submitted`
3. Reviewer views queue
4. Reviewer approves/rejects

---

## 📌 Notes

* Only valid state transitions are allowed
* Merchants cannot access other merchants' data
* SLA (`at_risk`) is dynamically calculated (>24 hours)

---

## 🚀 Future Improvements

* JWT-based authentication
* File upload UI
* Email notifications
* Deployment with Docker

---

## 👨‍💻 Author

Built as part of **Playto Founding Engineering Intern Challenge**
