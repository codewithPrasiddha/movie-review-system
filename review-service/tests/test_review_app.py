import requests
import time


import os

BASE_URL_USER = os.getenv("BASE_URL_USER", "http://localhost:8001")
BASE_URL_REVIEW = os.getenv("BASE_URL_REVIEW", "http://localhost:8003")

def get_token():
    requests.post(f"{BASE_URL_USER}/register", json={"username": "john", "password": "pass123"})
    time.sleep(0.2)
    res = requests.post(f"{BASE_URL_USER}/login", json={"username": "john", "password": "pass123"})
    return res.json().get("access_token")

def test_add_review():
    token = get_token()  # should return valid JWT
    headers = {"Authorization": f"Bearer {token}"}
    
    review = {
    "user": "testuser",  #  string
    "movie_id": 1,
    "reviewer": "John Doe",
    "rating": 5,
    "comment": "Amazing movie!"
}



    res = requests.post(f"{BASE_URL_REVIEW}/reviews", json=review, headers=headers)
    print(res.status_code, res.text)
    assert res.status_code == 200

