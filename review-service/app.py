from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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
