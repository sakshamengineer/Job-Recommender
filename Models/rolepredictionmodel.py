import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
import joblib
from Assets.Role_columns import ROLE_COLUMNS

df = pd.read_csv(r"D:\Saksham\Projects\Resume Based Job Recommender\Dataset\Processed Dataset\Final.csv")
FEATURE_COLUMNS = [col for col in df.columns if col not in ROLE_COLUMNS]

X = df[FEATURE_COLUMNS].values
Y = df[ROLE_COLUMNS].values


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = OneVsRestClassifier(
    LogisticRegression(max_iter=2000),
)

model.fit(X_train, y_train)

a = np.zeros(56,dtype=int)

# X_input = X_test[[0]]

proba = model.predict_proba([a])[0]

scores = np.array(proba)
scores = scores / scores.max()

pretty_scores = list(zip(ROLE_COLUMNS, scores))
pretty_scores.sort(key=lambda x: x[1], reverse=True)

for role, scores in pretty_scores:
    print(role , "-->", scores)

# joblib.dump(model,"Models/JobpredictModel.pkl")