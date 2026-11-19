import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}

def test_generate():
    response = client.post("/generate", json={"class_name": "MyWidget", "variable_name": "controller"})
    assert response.status_code == 200
    data = response.json()
    assert "generated_code" in data
    assert "class MyWidget" in data["generated_code"]
    assert "TextEditingController controller" in data["generated_code"]
