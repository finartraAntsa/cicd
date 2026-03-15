from fastapi import FastAPI, Query
from traitement import modelisation

app = FastAPI()


@app.get("/")
def dire_bonjour():
    """Endpoint racine qui renvoie un message de bienvenue."""
    return {"mot": "bonjour tous le monde"}


@app.get("/modelisation")
def modeliser(files: str = Query(..., description="Chemin vers le fichier CSV")):
    """
    Endpoint pour effectuer la modélisation.
    
    Args:
        files (str): Chemin vers le fichier CSV contenant les données.

    Returns:
        dict: Scores de validation croisée et score moyen.
    """
    resultat = modelisation(files)
    if resultat is None:
        return {"erreur": "Aucun fichier trouvé ou fichier invalide."}
    return resultat