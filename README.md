# Movie Review System

A microservices-based project using **FastAPI**, **Docker**, **PostgreSQL**, and **Kubernetes**, allowing users to register, log in, add movies, and post reviews.

## ⚙️ Architecture Overview

```bash
User Service     --> Handles user login, register, JWT (port 8001)
Movie Service    --> Manages movie catalog (port 8002)
Review Service   --> Handles movie reviews (port 8003)
Database         --> PostgreSQL backend for user-service
Prometheus       --> Monitors all services on port 9090
```

## 🗂️ Folder Structure

```bash
movie-review-system/
├── user-service/
│   ├── app.py
│   ├── models.py
│   ├── database.py
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
```

## 📦 Technologies Used

```bash
- Python 3.9
- FastAPI
- PostgreSQL (for user-service)
- Docker & Docker Compose
- Pytest
- Uvicorn
- Prometheus (for monitoring)
- dotenv (.env management)
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/movie-review-system.git
cd movie-review-system
```

### 2. Create .env File

```bash
POSTGRES_DB=movie_review_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=secretsanta0123
SECRET_KEY=secretsanta
DATABASE_URL=postgresql://admin:secretsanta0123@movie-review-db:5432/movie_review_db
BASE_URL_USER=http://user-service:8000
BASE_URL_REVIEW=http://review-service:8000
BASE_URL=http://movie-service:8000
```

### 3. Start All Services

```bash
docker compose up --build -d
```

### 4. Check Health of All Services

```bash
curl http://localhost:8001/health   # user-service
curl http://localhost:8002/health   # movie-service
curl http://localhost:8003/health   # review-service
```

## 🔐 Authentication Flow

```bash
# Register
curl -X POST http://localhost:8001/register \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "secretsanta"}'

# Login to get JWT
curl -X POST http://localhost:8001/login \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "secretsanta"}'

# Access protected route
curl http://localhost:8001/protected \
  -H "Authorization: Bearer <JWT_TOKEN>"
```

## 🎬 Movie & Review API

```bash
# Add a Movie
curl -X POST http://localhost:8002/movies \
  -H "Content-Type: application/json" \
  -d '{"title": "Avengers", "genre": "Action", "director": "Marvel", "release_date": "2012"}'

# Get Movies
curl http://localhost:8002/movies

# Add Review
curl -X POST http://localhost:8003/reviews \
  -H "Content-Type: application/json" \
  -d '{"movie_id": 1, "user": "testuser", "rating": 5, "comment": "Great!"}'

# Get Reviews for Movie ID 1
curl http://localhost:8003/reviews/1
```

## ✅ Unit Tests

```bash
# Run tests for all services
pytest

# Run from inside container
docker exec user-service pytest -v
```

## 📊 Monitoring (Prometheus)

```bash
http://localhost:9090  # Prometheus UI
http://localhost:8001/metrics
http://localhost:8002/metrics
http://localhost:8003/metrics
```

## 🧹 Shutdown Services

```bash
docker compose down
```

## 🗃️ Kubernetes Commands

```bash
kubectl apply -f user-service/deployment.yaml
kubectl apply -f user-service/service.yaml
kubectl apply -f user-service/user-service-hpa.yaml

kubectl get pods
kubectl get svc
kubectl get hpa
```

## 📜 License

Open-source for learning and demonstration use.
