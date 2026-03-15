from fastapi import FastAPI
from pydantic import BaseModel
from traitement import modelisation

app = FastAPI()


@app.get("/")
def direBonjour():
    return {"mot": "bonjour tous le monde"}


@app.get("/modelisation")
def modeliser(files):
    resultat = modelisation(files)
    return resultat
