# user-service/tests/test_user_app.py

import requests
import time
import os
import uuid

# Use service name inside Docker network

BASE_URL = os.getenv("BASE_URL", "http://localhost:8001")  # default for local testing


def test_register():
    unique_username = f"newuser_{uuid.uuid4().hex[:8]}"  # Generate a unique username
    res = requests.post(f"{BASE_URL}/register", json={"username": unique_username, "password": "newpassword"})
    assert res.status_code == 200
    assert res.json()["message"] == "User registered successfully"  

def test_login():
    # Ensure the user is present (you might want to adjust this if 'testuser' is always there)
    requests.post(f"{BASE_URL}/register", json={"username": "testuser", "password": "secretsanta"}) # Use the correct password
    time.sleep(0.2)  # short delay to ensure DB commit

    # Attempt login with the correct password
    res = requests.post(f"{BASE_URL}/login", json={"username": "testuser",
                                                   "password": "secretsanta"}) # Use the correct password
    print("Login:", res.status_code, res.text)
    assert res.status_code == 200
    assert "access_token" in res.json()

def test_protected_route():
    # Login to get JWT token with the correct password
    login_res = requests.post(f"{BASE_URL}/login", json={"username": "testuser",
                                                        "password": "secretsanta"}) # Use the correct password
    assert login_res.status_code == 200
    token = login_res.json().get("access_token")
    assert token is not None

    # Attempt to access a protected route (assuming you have one at /protected)
    headers = {"Authorization": f"Bearer {token}"}
    protected_res = requests.get(f"{BASE_URL}/protected-route", headers=headers)
    print("Protected:", protected_res.status_code, protected_res.text)
    assert protected_res.status_code == 200  # You might need to adjust the expected status code
    assert "Access granted" in protected_res.json()["message"]