Movie Review System

This is a microservices-based Movie Review System built using FastAPI, PostgreSQL, Docker, and Docker Compose. The system allows users to register and log in, add movies, and post reviews for those movies.

Project Architecture

The system consists of the following microservices:
	1.	User Service – Handles user registration, login, and authentication using JWT.
	2.	Movie Service – Allows adding new movies and retrieving movie details.
	3.	Review Service – Enables posting and retrieving reviews for movies.

Each service runs in its own container and communicates over a Docker network. PostgreSQL is used as the backend database for the user service.

Technologies Used
	•	Python 3.9
	•	FastAPI
	•	PostgreSQL
	•	Docker & Docker Compose
	•	Uvicorn (ASGI Server)
	•	Pytest (for testing)
	•	dotenv (for managing environment variables)

Folder Structure

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

How to Run

1. Clone the Repository

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

3. Start the Project

docker compose up --build -d

4. Check Health Endpoints

curl http://localhost:8001/health  # User Service
curl http://localhost:8002/health  # Movie Service
curl http://localhost:8003/health  # Review Service

API Endpoints

User Service (localhost:8001)
	•	POST /register – Register a new user
	•	POST /login – Log in and get JWT token
	•	GET /protected – Protected route (JWT required)
	•	GET /health – Health check

Movie Service (localhost:8002)
	•	POST /movies – Add a new movie
	•	GET /movies – List all movies
	•	GET /movies/{movie_id} – Get movie by ID
	•	GET /health – Health check

Review Service (localhost:8003)
	•	POST /reviews – Submit a review
	•	GET /reviews/{movie_id} – Get reviews for a movie
	•	GET /health – Health check

Running Tests

To run the unit tests inside the user-service container:

docker exec user-service pytest -v

Tests included:
	•	test_register
	•	test_login
	•	test_protected_route

Shut Down

docker compose down

Notes
	•	Only the User Service persists data using PostgreSQL.
	•	The Movie and Review Services use in-memory data for simplicity.
	•	Intended for educational/demo purposes.
	•	For production, consider using persistent databases, secret managers, and Kubernetes.
