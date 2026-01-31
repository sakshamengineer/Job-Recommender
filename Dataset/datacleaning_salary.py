import pandas as pd

data = pd.read_csv("Dataset\Raw Dataset\salary.csv")

data['YearsExperience'] = data['YearsExperience'].round().astype('int64')
roles = pd.get_dummies(data["JobRole"],dtype=int)
data = data.drop('JobRole',axis=1)

data = pd.concat([roles,data],axis=1)
data.rename(columns={'Salary(LPA)':"Salary"},inplace=True)

data = data[["software_engineer","data_science","machine_learning_engineer","data_engineer","devops","cloud_engineer","mobile_app_developer","network_engineer","cyber_security","business_analyst","YearsExperience","Salary"]]

data.to_csv("Dataset/Processed Dataset/Final_salary.csv",index=False)