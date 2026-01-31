import joblib
import numpy as np
from Models.Assets.Role_columns import ROLE_COLUMNS

def predict_job_role(skills):
    model = joblib.load("Models/JobpredictModel.pkl")
    proba = model.predict_proba(skills)
    scores = np.array(proba)[0]
    scores = scores / scores.max()
    pretty_scores = list(zip(ROLE_COLUMNS, scores))
    pretty_scores.sort(key=lambda x: x[1], reverse=True)

    predicted_roles = []
    for role , score in pretty_scores:
        if score > 0.5:
            predicted_roles.append(role)

    return predicted_roles

def predict_salary(jobrole):
    model = joblib.load("Models/SalaryPredictionModel.pkl")
    salary = model.predict([jobrole])
    return salary