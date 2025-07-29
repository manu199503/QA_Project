import pytest
import json
from playwright.sync_api import sync_playwright

BASE_URL = "http://127.0.0.1:3001"

@pytest.fixture(scope="session")
def api_request_context():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        yield request_context
        request_context.dispose()

@pytest.fixture(scope="function")
def test_user(api_request_context):
    email = "testuser@example.com"
    password = "testpass"
    api_request_context.delete(
        f"{BASE_URL}/delete",
        data=json.dumps({"email": email}),
        headers={"Content-Type": "application/json"},
    )
    api_request_context.post(
        f"{BASE_URL}/register",
        data=json.dumps({"email": email, "password": password}),
        headers={"Content-Type": "application/json"},
    )
    yield {"email": email, "password": password}
    api_request_context.delete(
        f"{BASE_URL}/delete",
        data=json.dumps({"email": email}),
        headers={"Content-Type": "application/json"},
    )
