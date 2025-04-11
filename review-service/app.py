from fastapi import FastAPI, Response
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST


app = FastAPI()
# Attach Prometheus instrumentator
Instrumentator().instrument(app).expose(app)

class Review(BaseModel):
    movie_id: int
    user: str
    rating: float
    comment: str

reviews_db = []

@app.post("/reviews")
def add_review(review: Review):
    reviews_db.append(review.dict())
    return {"message": "Review added successfully"}

@app.get("/reviews/{movie_id}")
def get_reviews(movie_id: int):
    return [review for review in reviews_db if review["movie_id"] == movie_id]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)