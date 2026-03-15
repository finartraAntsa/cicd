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
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def modelisation(files):
    try:
        file = pd.read_csv(files)
        print("Fichier importé avec succès")
    except FileNotFoundError:
        print("Aucun fichier trouvé")
        return None

    X = file[["heures_etude", "heures_sommeil", "presence_cours"]]
    Y = file[["score"]]

    # *************** Ici nous n'allons utiliser que la régression linéaire multiple ***************
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


# ----------------- Exemple avec RandomForest et GridSearchCV -----------------
# pipeline = Pipeline([
#     ('scaler', StandardScaler()),
#     ('rf', RandomForestRegressor(random_state=42))
# ])
#
# param_grid = {
#     'rf__n_estimators': [50, 100],
#     'rf__max_depth': [5, 10]
# }
#
# grid = GridSearchCV(pipeline, param_grid, cv=5, scoring='r2', n_jobs=-1)
# grid.fit(X, Y)
#
# print("Meilleur score R² :", grid.best_score_)
# print("Meilleurs paramètres :", grid.best_params_)
#
# # Le meilleur modèle entraîné
# best_model = grid.best_estimator_
#
# # On peut maintenant l'utiliser pour prédire
# y_pred = best_model.predict(X)