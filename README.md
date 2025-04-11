# Movie Review System

A microservices-based application built with FastAPI, Docker, and PostgreSQL, allowing users to register, log in, add movies, and post reviews.

## Architecture Overview

The system is composed of 3 main services:

| Service        | Description                             | Port |
|----------------|-----------------------------------------|------|
| User Service   | Handles user registration, login & JWT  | 8001 |
| Movie Service  | Manages movie catalog                   | 8002 |
| Review Service | Accepts and lists reviews per movie     | 8003 |

All services communicate over a shared Docker network and are orchestrated via Docker Compose.

## Technologies Used

- Python 3.9  
- FastAPI  
- PostgreSQL (for User Service)  
- Docker & Docker Compose  
- Uvicorn  
- Pytest  
- dotenv  

## Folder Structure

```
movie-review-system/
├── user-service/
│   ├── app.py
│   ├── models.py
│   ├── database.py
│   ├── tests/
│   │   └── test_user_app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── wait-for-db.sh
├── movie-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── review-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
└── .env
```
## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/movie-review-system.git
cd movie-review-system

2. Create a .env File

POSTGRES_DB=movie_review_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=secretsanta0123
SECRET_KEY=secretsanta
DATABASE_URL=postgresql://admin:secretsanta0123@movie-review-db:5432/movie_review_db
BASE_URL_USER=http://user-service:8000
BASE_URL_REVIEW=http://review-service:8000
BASE_URL=http://movie-service:8000

3. Start All Services

docker compose up --build -d

4. Verify Health

curl http://localhost:8001/health  # User Service
curl http://localhost:8002/health  # Movie Service
curl http://localhost:8003/health  # Review Service

API Endpoints

User Service (port 8001)
	•	POST /register – Register new user
	•	POST /login – Obtain JWT token
	•	GET /protected – Auth-protected route
	•	GET /health – Health check

Movie Service (port 8002)
	•	POST /movies – Add a movie
	•	GET /movies – List all movies
	•	GET /movies/{id} – Get movie by ID
	•	GET /health – Health check

Review Service (port 8003)
	•	POST /reviews – Add a review
	•	GET /reviews/{id} – Get reviews for a movie
	•	GET /health – Health check

Running Unit Tests

docker exec user-service pytest -v

Tests are located in:

user-service/tests/test_user_app.py

Includes tests for:
	•	Register
	•	Login
	•	Protected route access

Shut Down All Services

docker compose down

Notes
	•	Only the User Service uses PostgreSQL; others use in-memory storage for simplicity.
	•	All APIs are written with FastAPI and return standard JSON responses.
	•	This project is intended for educational/demo purposes.

License

This project is open-source and free to use.

You can now paste this into GitHub and it will look clean with proper formatting, collapsible code blocks, and readable tables. Let me know if you want to add contributor info or GitHub badges too.
