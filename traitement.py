# 0) Data engineering
# 1) Preprocessing
# 2) Standardisation
# 3) Echantillonnage (Cross-validation)
# 4) Apprentissage
# 5) Comparaison
# 6) Interprétation
# 7) Test de stabilité
# 8) Choix du modèle

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score


def modelisation(files):
    try:
        file = pd.read_csv(files)
        print("Fichier importé avec succès")
    except FileNotFoundError:
        print("Aucun fichier trouvé")
        return None

    X = file[["heures_etude", "heures_sommeil", "presence_cours"]]
    Y = file[["score"]]

    model = LinearRegression()

    # Validation croisée 5-fold
    scores = cross_val_score(model, X, Y, cv=5)

    # Entraînement final après sélection du modèle
    # Dans notre cas, ce n'est pas nécessaire
    model.fit(X, Y)

    # Valeur de retour sous forme de JSON
    return {
        "Scores par fold": scores.tolist(),
        "Score moyen": scores.mean()
    }
