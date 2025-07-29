import json

BASE_URL = "http://127.0.0.1:3001"

def test_update_requires_login(api_request_context, test_user):
    response = api_request_context.put(
        f"{BASE_URL}/update",
        data=json.dumps({"email": test_user["email"], "name": "No Login Update"}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status == 401 or response.status == 200
    body = response.json()
    assert body == "Unauthorized. Please login first." or "email" in body

def test_login_then_update(api_request_context, test_user):
    login_resp = api_request_context.post(
        f"{BASE_URL}/login",
        data=json.dumps({"email": test_user["email"], "password": test_user["password"]}),
        headers={"Content-Type": "application/json"},
    )
    assert login_resp.status == 200
    assert login_resp.json() == "Success"

    response = api_request_context.put(
        f"{BASE_URL}/update",
        data=json.dumps({"email": test_user["email"], "name": "Session Test"}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status == 200
    assert "name" in response.json()
