from fastapi import FastAPI
from traitement import modelisation

app = FastAPI()


@app.get("/")
def dire_bonjour():
    """Endpoint racine qui renvoie un message de bienvenue."""
    return {"mot": "bonjour tous le monde"}


@app.get("/modelisation")
def modeliser(files):
    resultat = modelisation(files)
    if resultat is None:
        return {"erreur": "Aucun fichier trouvé ou fichier invalide."}
    return resultat

