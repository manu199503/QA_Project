import json

BASE_URL = "http://127.0.0.1:3001"

def test_register_success(api_request_context):
    email = "positive@example.com"
    password = "positivepass"
    api_request_context.delete(
        f"{BASE_URL}/delete",
        data=json.dumps({"email": email}),
        headers={"Content-Type": "application/json"},
    )
    response = api_request_context.post(
        f"{BASE_URL}/register",
        data=json.dumps({"email": email, "password": password}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status == 200
    body = response.json()
    assert "email" in body

def test_login_success(api_request_context, test_user):
    response = api_request_context.post(
        f"{BASE_URL}/login",
        data=json.dumps({"email": test_user["email"], "password": test_user["password"]}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status == 200
    assert response.json() == "Success"

def test_update_success(api_request_context, test_user):
    login_resp = api_request_context.post(
        f"{BASE_URL}/login",
        data=json.dumps({"email": test_user["email"], "password": test_user["password"]}),
        headers={"Content-Type": "application/json"},
    )
    assert login_resp.status == 200
    assert login_resp.json() == "Success"

    new_name = "Updated Name"
    new_password = "newpass123"
    response = api_request_context.put(
        f"{BASE_URL}/update",
        data=json.dumps({"email": test_user["email"], "name": new_name, "password": new_password}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status == 200
    body = response.json()
    assert body.get("name") == new_name

def test_delete_success(api_request_context):
    email = "positive_delete@example.com"
    password = "deletepass"
    api_request_context.post(
        f"{BASE_URL}/register",
        data=json.dumps({"email": email, "password": password}),
        headers={"Content-Type": "application/json"},
    )
    response = api_request_context.delete(
        f"{BASE_URL}/delete",
        data=json.dumps({"email": email}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status == 200
    assert response.json() == "User deleted successfully"
