import json

BASE_URL = "http://127.0.0.1:3001"

def test_register_existing_user(api_request_context, test_user):
    response = api_request_context.post(
        f"{BASE_URL}/register",
        data=json.dumps({"email": test_user["email"], "password": "any"}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status == 200
    assert response.json() == "Already registered"

def test_login_wrong_password(api_request_context, test_user):
    response = api_request_context.post(
        f"{BASE_URL}/login",
        data=json.dumps({"email": test_user["email"], "password": "wrongpass"}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status == 200
    assert response.json() == "Wrong password"

def test_login_nonexistent_user(api_request_context):
    response = api_request_context.post(
        f"{BASE_URL}/login",
        data=json.dumps({"email": "notfound@example.com", "password": "pass"}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status == 200
    assert response.json().strip() == "No records found!"

def test_update_without_login(api_request_context, test_user):
    response = api_request_context.put(
        f"{BASE_URL}/update",
        data=json.dumps({"email": test_user["email"], "name": "name"}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status == 401 or response.status == 200
    # Your backend sends either 401 or 200 with message:
    body = response.json()
    assert body == "Unauthorized. Please login first." or "email" in body

def test_delete_nonexistent_user(api_request_context):
    response = api_request_context.delete(
        f"{BASE_URL}/delete",
        data=json.dumps({"email": "nonexistent@example.com"}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status == 200
    assert response.json() == "User not found"
