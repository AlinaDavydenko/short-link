from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_short_url():
    data = {"original_url": "https://habr.com/ru/articles/1005390/"}
    response = client.post("/shorten", json=data)
    assert response.status_code == 200
    assert response.json()["original_url"] == data["original_url"]
    assert response.json()["clicks"] == 0


def test_redirect_url():
    data = {"original_url": "https://habr.com/ru/articles/1005390/"}
    post_response = client.post("/shorten", json=data)
    short_code = post_response.json()["short_code"]
    response = client.get(f"/{short_code}", follow_redirects=False)
    assert response.status_code == 307
