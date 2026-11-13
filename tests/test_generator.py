import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)
response = client.get("/")
assert response.status_code == 200
assert response.json() == {"message": "Hello"}
