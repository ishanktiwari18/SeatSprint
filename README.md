# SeatSprint

<p align="center">
  <h3 align="center">Modern Ticket Booking Platform</h3>
  <p align="center">
    Real-time ticket booking system for Movies and Concerts built with Django, React, Docker, MySQL and Redis.
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/DRF-A30000?style=for-the-badge&logo=django&logoColor=white" alt="Django REST Framework" />
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React" />
  <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL" />
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis" />
  <img src="https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white" alt="Celery" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="Nginx" />
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" alt="JWT" />
  <img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black" alt="Swagger" />
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

<table>
<tr>
<td valign="top" width="25%">

**Frontend**
- React 18
- React Router
- Axios
- Tailwind CSS
- Vite

</td>
<td valign="top" width="25%">

**Backend**
- Django
- Django REST Framework
- Simple JWT
- Celery

</td>
<td valign="top" width="25%">

**Database / Cache**
- MySQL 8
- Redis

</td>
<td valign="top" width="25%">

**DevOps**
- Docker
- Docker Compose
- Nginx

</td>
</tr>
</table>

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

<img src="C:\Users\Ishank\OneDrive\Pictures\Screenshots\Screenshot 2026-07-03 094151.png" alt="Login page" width="800" />

---

## Browse Events

<img src="C:\Users\Ishank\OneDrive\Pictures\Screenshots\Screenshot 2026-07-03 094743.png" alt="Browse events page" width="800" />

---

## My Bookings

<img src="C:\Users\Ishank\OneDrive\Pictures\Screenshots\Screenshot 2026-07-03 094758.png" alt="My bookings page" width="800" />

---

## Organizer Dashboard

<img src="C:\Users\Ishank\OneDrive\Pictures\Screenshots\Screenshot 2026-07-03 094813.png" alt="Organizer dashboard" width="800" />

---

## Database

<img src="C:\Users\Ishank\OneDrive\Pictures\Screenshots\Screenshot 2026-07-03 094948.png" alt="MySQL Workbench users table" width="800" />

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

LinkedIn: https://linkedin.com/in/ishank-tiwari-it18

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