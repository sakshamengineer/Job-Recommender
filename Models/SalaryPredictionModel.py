import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

data = pd.read_csv(r"D:\Saksham\Projects\Resume Based Job Recommender\Dataset\Processed Dataset\Final_salary.csv")

X = data.iloc[:,:-1].values
Y = data.iloc[:,-1].values

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.8,random_state=42)

model = LinearRegression()
model.fit(X_train,Y_train)

joblib.dump(model,"Models/SalaryPredictionModel.pkl")