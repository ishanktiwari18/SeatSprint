# SeatSprint

<p align="center">
  <h3 align="center">Modern Ticket Booking Platform</h3>
  <p align="center">
    Real-time ticket booking system for Movies and Concerts built with Django, React, Docker, MySQL and Redis.
  </p>
</p>

---

## Features

### Authentication

- User Registration
- User Login
- JWT Authentication
- Role Based Access (Customer / Organizer)
- Password Validation
- Protected Routes

### Backend

- Django REST Framework
- MySQL Database
- Dockerized Services
- Redis
- Celery Worker
- Celery Beat
- Swagger/OpenAPI Documentation
- UUID Primary Keys

### Frontend

- React 18
- React Router
- Axios
- Tailwind CSS
- Responsive UI
- Protected Pages

### Current Progress

- Authentication
- User Management
- JWT Login
- Docker Environment
- Swagger Documentation
- Database Integration
- Organizer Dashboard UI
- Browse Events UI
- My Bookings UI

---

# Tech Stack

## Frontend

- React 18
- React Router
- Axios
- Tailwind CSS
- Vite

## Backend

- Django
- Django REST Framework
- Simple JWT
- Celery

## Database

- MySQL 8

## Cache

- Redis

## DevOps

- Docker
- Docker Compose
- Nginx

---

# Project Structure

```
SeatSprint
│
├── backend/
│   ├── apps/
│   │   ├── accounts/
│   │   ├── bookings/
│   │   ├── events/
│   │   ├── venues/
│   │   ├── waitlist/
│   │   ├── notifications/
│   │   └── payments/
│   │
│   ├── config/
│   └── manage.py
│
├── frontend/
│   ├── src/
│   └── package.json
│
├── docker/
├── nginx/
├── docker-compose.yml
└── README.md
```

---

# Architecture

```
                React Frontend
                      │
                  Axios API
                      │
                Nginx Reverse Proxy
                      │
                Django REST API
          ┌───────────┼───────────┐
          │           │           │
        MySQL       Redis      Celery
```

---

# Screenshots

## Login

> Replace with your login screenshot.

```
docs/images/login.png
```

---

## Browse Events

> Replace with your browse page screenshot.

```
docs/images/browse.png
```

---

## My Bookings

> Replace with your bookings screenshot.

```
docs/images/bookings.png
```

---

## Organizer Dashboard

> Replace with your organizer screenshot.

```
docs/images/dashboard.png
```

---

## Database

> Replace with your MySQL Workbench screenshot.

```
docs/images/database.png
```

---

# Getting Started

## Clone Repository

```bash
git clone https://github.com/<your-username>/SeatSprint.git

cd SeatSprint
```

---

# Environment Variables

Create a `.env`

```env
DJANGO_ENV=development

DJANGO_SECRET_KEY=change-me

DB_NAME=seat_sprint_db

DB_USER=seat_sprint_user

DB_PASSWORD=devpassword

DB_ROOT_PASSWORD=rootdevpassword

DB_HOST=db

DB_PORT=3306

REDIS_URL=redis://redis:6379/0

ALLOWED_HOSTS=*

CORS_ORIGINS=http://localhost:3000

EMAIL_HOST=

EMAIL_PORT=

EMAIL_USE_TLS=1

EMAIL_HOST_USER=

EMAIL_HOST_PASSWORD=
```

---

# Running with Docker (Recommended)

## Build Containers

```bash
docker compose up --build
```

---

## Run Containers

```bash
docker compose up
```

---

## Stop Containers

```bash
docker compose down
```

---

## Rebuild

```bash
docker compose down

docker compose up --build
```

---

# Services

| Service | URL |
|---------|------|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| Swagger | http://localhost:8000/swagger/ |
| MySQL | localhost:3307 |
| Redis | localhost:6379 |

---

# Docker Commands

## Backend Shell

```bash
docker compose exec backend python manage.py shell
```

## Create Superuser

```bash
docker compose exec backend python manage.py createsuperuser
```

## Migrations

```bash
docker compose exec backend python manage.py makemigrations

docker compose exec backend python manage.py migrate
```

## View Logs

```bash
docker compose logs backend

docker compose logs frontend

docker compose logs db
```

---

# Manual Installation

## 1. Backend

```bash
cd backend

python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Run server

```bash
python manage.py runserver
```

---

## 2. Frontend

```bash
cd frontend

npm install
```

Run

```bash
npm run dev
```

---

## 3. Redis

Start Redis server.

---

## 4. MySQL

Create database

```sql
CREATE DATABASE seat_sprint_db;
```

Update `.env` accordingly.

---

## 5. Celery Worker

```bash
celery -A config worker -l info
```

---

## 6. Celery Beat

```bash
celery -A config beat -l info
```

---

# API Documentation

Swagger UI

```
http://localhost:8000/swagger/
```

---

# Database

Current database includes:

- Users
- Venues
- Sections
- Rows
- Seats
- Events
- Shows
- Price Categories
- Show Seats
- Bookings
- Waitlists
- Payments
- Notifications

---

# Current Development Status

| Module | Status |
|---------|--------|
| Docker Setup | ✅ |
| MySQL | ✅ |
| Redis | ✅ |
| JWT Authentication | ✅ |
| User Registration | ✅ |
| Login | ✅ |
| Swagger | ✅ |
| Organizer Dashboard UI | ✅ |
| Browse UI | ✅ |
| Booking UI | ✅ |
| Event CRUD | 🚧 |
| Venue CRUD | 🚧 |
| Live Seat Map | 🚧 |
| Booking Engine | 🚧 |
| Waitlist Logic | 🚧 |
| Payment Integration | ⏳ |

---

# Future Improvements

- Live Seat Selection
- Automatic Seat Hold Expiry
- Waitlist Promotion
- Payment Gateway
- QR Ticket Generation
- Email Notifications
- Search & Filters
- Analytics Dashboard
- Admin Panel
- CI/CD Pipeline
- Unit Testing
- Integration Testing

---

# License

This project is licensed under the MIT License.

---

# Author

**Ishank Tiwari**

GitHub: https://github.com/ishanktiwari18

LinkedIn: https://linkedin.com/in/<your-linkedin>

---

## Acknowledgements

Built using:

- Django
- Django REST Framework
- React
- Docker
- MySQL
- Redis
- Celery
- Tailwind CSS
- Vite