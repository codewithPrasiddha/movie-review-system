from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

class Movie(BaseModel):
    title: str
    genre: str
    director: str
    release_date: str

movies_db = {}

@app.post("/movies")
def add_movie(movie: Movie):
    movie_id = len(movies_db) + 1
    movies_db[movie_id] = movie
    return {"id": movie_id, "message": "Movie added successfully"}

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return movies_db.get(movie_id, {"message": "Movie not found"})

@app.get("/movies")  
def get_all_movies():
    return movies_db

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)