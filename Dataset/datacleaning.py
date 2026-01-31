import pandas as pd
import re
from Assets.masterskills import MASTER_SKILLS
from Assets.Assigningjobroles import assign_job_roles

df = pd.read_csv(r"Dataset\Raw Dataset\rolesdataset.csv")

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'\s+', ' ', text)
    return text

df["ALL"] = df["ALL"].apply(clean_text)

for skill in MASTER_SKILLS:
    df[skill] = df["ALL"].apply(lambda x: 1 if skill in x else 0)

df = df.drop(columns=["Target","ALL","index"])

role_labels = df.apply(assign_job_roles, axis=1)
print(role_labels.shape[1])
df = pd.concat([df, role_labels], axis=1)

# df.to_csv("Dataset\Processed Dataset\Final.csv",index=False)