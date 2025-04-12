Movie Review System

A microservices-based application built with FastAPI, Docker, and PostgreSQL, allowing users to register, log in, add movies, and post reviews.

Architecture Overview

The system consists of three microservices:

Service	Description	Port
User Service	Handles registration, login & JWT auth	8001
Movie Service	Manages movie catalog	8002
Review Service	Accepts and displays movie reviews	8003

All services run in isolated containers via Docker Compose and communicate over a shared Docker network.

Technologies Used
	•	Python 3.9
	•	FastAPI
	•	PostgreSQL (for User Service)
	•	Docker & Docker Compose
	•	Uvicorn
	•	Pytest
	•	dotenv
	•	Prometheus (for monitoring)

Folder Structure

movie-review-system/
├── user-service/
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── wait-for-db.sh
│   └── tests/
│       └── test_user_app.py
├── movie-service/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests/
│       └── test_movie_app.py
├── review-service/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests/
│       └── test_review_app.py
├── docker-compose.yml
├── prometheus.yml
└── .env

Setup Instructions
	1.	Clone the Repository

git clone https://github.com/yourusername/movie-review-system.git
cd movie-review-system

	2.	Create a .env File

POSTGRES_DB=movie_review_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=secretsanta0123
SECRET_KEY=secretsanta
DATABASE_URL=postgresql://admin:secretsanta0123@movie-review-db:5432/movie_review_db
BASE_URL_USER=http://user-service:8000
BASE_URL_REVIEW=http://review-service:8000
BASE_URL=http://movie-service:8000

	3.	Start the Services

docker compose up --build -d

	4.	Check Service Health

curl http://localhost:8001/health   # User Service
curl http://localhost:8002/health   # Movie Service
curl http://localhost:8003/health   # Review Service

API Endpoints

User Service (port 8001)
	•	POST /register – Register new user
	•	POST /login – Obtain JWT token
	•	GET /protected – Protected route (requires token)
	•	GET /health – Health check

Movie Service (port 8002)
	•	POST /movies – Add a new movie
	•	GET /movies – List all movies
	•	GET /movies/{id} – Retrieve movie by ID
	•	GET /health – Health check

Review Service (port 8003)
	•	POST /reviews – Submit a movie review
	•	GET /reviews/{movie_id} – Get all reviews for a movie
	•	GET /health – Health check

Running Unit Tests

To run all tests across services:

pytest

To run tests only for the user service:

docker exec user-service pytest -v

Shut Down All Services

docker compose down

Notes
	•	Only the User Service uses PostgreSQL. Other services use in-memory dictionaries for simplicity.
	•	All APIs are built with FastAPI and return clean JSON responses.
	•	This project is meant for learning and demonstration purposes.
	•	Monitoring is enabled via Prometheus at http://localhost:9090.

License

This project is open-source and free to use for educational purposes.
