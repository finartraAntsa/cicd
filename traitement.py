# 0) Data engenging
# 1) Preprocessing
# 2) Standardisation
# 3) Echantillonage( Cross-validation )
# 4) Apprentissage
# 5) Comparaison
# 6) Interpretation
# 7) Test de stabilité
# 8) Choix du model

import pandas as pd
import sklearn


def modelisation(files):
    try:
        file = pd.read_csv(files)
        print("fichier importé avec succées")
    except FileNotFoundError:
        print("aucun fichier trouvé")

    X = file[["heures_etude", 
              "heures_sommeil", 
              "presence_cours"]]
    
    Y = file[["score"]]

    # ***************Ici nous n'allons utiliser que la regression lineaire multiple **************
    model = sklearn.linear_model.LinearRegression()

    # Validation croisée 5-fold
    scores = sklearn.model_selection.cross_val_score(model, 
                                                     X,
                                                     Y, 
                                                     cv=5)

    # Entrainement final apre selection du model
    # Qui sur notre cas n'est pa necassaire
    model.fit(X, Y)

    # ici le valuer de retour est un json donc
    return {"Scores par fold ": scores.tolist(),
            "Score moyen ": scores.mean()}
""""

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('rf', RandomForestRegressor(random_state=42))
])

param_grid = {
    'rf__n_estimators': [50, 100],
    'rf__max_depth': [5, 10]
}

grid = GridSearchCV(pipeline, param_grid, cv=5, scoring='r2', n_jobs=-1)
grid.fit(X, y)

print("Meilleur score R² :", grid.best_score_)
print("Meilleurs paramètres :", grid.best_params_)

# Le meilleur modèle entraîné
best_model = grid.best_estimator_

# On peut maintenant l'utiliser pour prédire
y_pred = best_model.predict(X)

"""
