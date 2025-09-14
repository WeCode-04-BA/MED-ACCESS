import pandas as pd

#import the disease and symptoms dataset
diseases = pd.read_csv("./data/raw/dataset.csv")

#strip spaces,lowercase,remove duplicates,drop empty symptoms columns
for col in diseases.columns:
    diseases[col] = diseases[col].astype(str).str.strip().str.lower().str.replace(r"[\s_]+","_",regex=True)
    diseases[col] = diseases[col].replace("nan",pd.NA)

diseases = diseases.drop_duplicates()   

#drop columns with 80% missing values
threshold = len(diseases) * 0.2
diseases = diseases.dropna(axis=1,thresh=threshold)


#export  the  disease and symptoms dataset
diseases.to_csv("./data/processed/cleaned_dataset.csv",index=False)
print("disease and symptoms dataset successfully exported")


#import the description,precaution, and severity datasets
description = pd.read_csv("./data/raw/symptom_Description.csv")
precaution = pd.read_csv("./data/raw/symptom_precaution.csv")
severity = pd.read_csv("./data/raw/Symptom-severity.csv")

#low-case description(disease and description column)
description["Disease"] = description["Disease"].str.lower()
description["Description"] = description["Description"].str.lower()

#export the description dataset
description.to_csv("./data/processed/cleaned_symptoms_description.csv",index=False)
print("disease and description dataset successfully exported")

#low case precaution dataset
for  col in  precaution.columns:
   precaution[col] =  precaution[col].str.lower()

#export the precaution dataset
precaution.to_csv("./data/processed/cleaned_symptom_precaution.csv",index = False)
print("disease and precautions dataset successfully exported")

# severity dataset is clean lets export it
severity.to_csv("./data/processed/cleaned_symptom_severity.csv",index=False)
print("symptom and weight dataset successfully exported")