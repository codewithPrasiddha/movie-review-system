Movie Review System

A microservices-based application built with FastAPI, Docker, and PostgreSQL, allowing users to register, log in, add movies, and post reviews.

Architecture Overview

The system is composed of 3 main services:

Service	Description	Port
User Service	Handles user registration, login & JWT	8001
Movie Service	Manages movie catalog	8002
Review Service	Accepts and lists reviews per movie	8003

All services communicate over a shared Docker network and are orchestrated via Docker Compose or Kubernetes.

Technologies Used
	•	Python 3.9
	•	FastAPI
	•	PostgreSQL (for User Service)
	•	Docker & Docker Compose
	•	Kubernetes
	•	Uvicorn
	•	Pytest
	•	dotenv

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
│   ├── wait-for-db.sh
│   ├── deployment.yaml
│   ├── service.yaml
│   └── user-service-hpa.yaml
├── movie-service/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── deployment.yaml
│   ├── service.yaml
│   └── movie-service-hpa.yaml
├── review-service/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── deployment.yaml
│   ├── service.yaml
│   └── review-service-hpa.yaml
├── prometheus.yml
├── docker-compose.yml
└── .env

Getting Started

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

3. Start All Services

Option A: Using Docker Compose

docker compose up --build -d

Option B: Using Kubernetes

kubectl apply -f user-service/deployment.yaml
kubectl apply -f user-service/service.yaml
kubectl apply -f movie-service/deployment.yaml
kubectl apply -f movie-service/service.yaml
kubectl apply -f review-service/deployment.yaml
kubectl apply -f review-service/service.yaml

(Optional) Apply Horizontal Pod Autoscalers (HPA)

kubectl apply -f user-service/user-service-hpa.yaml
kubectl apply -f movie-service/movie-service-hpa.yaml
kubectl apply -f review-service/review-service-hpa.yaml

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
	•	GET /metrics – Prometheus metrics

Movie Service (port 8002)
	•	POST /movies – Add a movie
	•	GET /movies – List all movies
	•	GET /movies/{id} – Get movie by ID
	•	GET /health – Health check
	•	GET /metrics – Prometheus metrics

Review Service (port 8003)
	•	POST /reviews – Add a review
	•	GET /reviews/{id} – Get reviews for a movie
	•	GET /health – Health check
	•	GET /metrics – Prometheus metrics

Running Unit Tests

Run tests inside the Docker container:

docker exec user-service pytest -v

Or run locally from the host machine (with virtualenv activated):

pytest

Tests are located in:
	•	user-service/tests/test_user_app.py
	•	movie-service/tests/test_movie_app.py
	•	review-service/tests/test_review_app.py

Includes tests for:
	•	Register
	•	Login
	•	Protected route access
	•	Add movie
	•	Get movie
	•	Add review
	•	Get review

Shut Down All Services

Docker Compose:

docker compose down

Kubernetes:

kubectl delete -f user-service/
kubectl delete -f movie-service/
kubectl delete -f review-service/

Notes
	•	Only the User Service uses PostgreSQL; the others use in-memory storage for simplicity.
	•	Prometheus is configured to monitor all services via the /metrics endpoint.
	•	All APIs are written using FastAPI and return JSON responses.
	•	This project is intended for educational and demonstration purposes.

License

This project is open-source and free to use.
