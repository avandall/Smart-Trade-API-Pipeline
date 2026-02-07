from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["message"] == "Smart Trade API"


def test_upload_sample():
    with open("data/input_sample.csv", "rb") as f:
        r = client.post("/api/upload", files={"file": ("input_sample.csv", f, "text/csv")})
    assert r.status_code == 200
    json = r.json()
    assert json["status"] == "ok"
    assert "rows" in json["result"]
