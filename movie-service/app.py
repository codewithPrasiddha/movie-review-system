from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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