from fastapi.testclient import TestClient  # ceci va créer un client
from app import app  # c'est la variable

client = TestClient(app)  # c'est un constructeur


def test_api():
    # validation test number one
    reponse1 = client.get("/")
    assert reponse1.status_code == 200
    assert reponse1.json() == {"mot": "bonjour tous le monde"}  # validation json

    # validation test number 2
    reponse2 = client.get("/modelisation?files=file.csv")
    assert reponse2.status_code == 200