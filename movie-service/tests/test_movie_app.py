import requests


BASE_URL = "http://localhost:8002"


def test_add_movie():
    movie = {
        "title": "Inception",
        "genre": "Sci-Fi",
        "director": "Christopher Nolan",
        "release_date": "2010-07-16"
    }
    response = requests.post(f"{BASE_URL}/movies", json=movie)
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_movie():
    response = requests.get(f"{BASE_URL}/movies/1")
    assert response.status_code == 200
