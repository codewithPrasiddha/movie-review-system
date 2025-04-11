# user-service/tests/test_user_app.py

import requests
import time
import os
import uuid

# Correct BASE_URL: points to container hostname in CI, or localhost in dev
BASE_URL = os.getenv("BASE_URL", "http://user-service:8000")  # works inside Docker and locally


def test_register():
    unique_username = f"newuser_{uuid.uuid4().hex[:8]}"  # Generate a unique username
    res = requests.post(f"{BASE_URL}/register", json={"username": unique_username, "password": "newpassword"})
    assert res.status_code == 200
    assert res.json()["message"] == "User registered successfully"  


def test_login():
    # Register user (if not already present)
    requests.post(f"{BASE_URL}/register", json={"username": "testuser", "password": "secretsanta"})
    time.sleep(0.2)  # Short delay to ensure DB commit

    # Attempt login
    res = requests.post(f"{BASE_URL}/login", json={"username": "testuser", "password": "secretsanta"})
    print("Login:", res.status_code, res.text)
    assert res.status_code == 200
    assert "access_token" in res.json()


def test_protected_route():
    # Login and get JWT token
    login_res = requests.post(f"{BASE_URL}/login", json={"username": "testuser", "password": "secretsanta"})
    assert login_res.status_code == 200
    token = login_res.json().get("access_token")
    assert token is not None

    # Access protected route
    headers = {"Authorization": f"Bearer {token}"}
    protected_res = requests.get(f"{BASE_URL}/protected", headers=headers)
    print("Protected:", protected_res.status_code, protected_res.text)
    assert protected_res.status_code == 200
    assert "Access granted" in protected_res.json()["message"]