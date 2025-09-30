import pandas as pd

#import the disease and symptoms dataset
dataset = pd.read_csv("./        data/raw/Disease and symptoms dataset.csv")

#drop duplicates
dataset = dataset.drop_duplicates()
 
#import the WHO dataset
who_dataset = pd.read_csv("./        data/raw/GHE_FULL_DD.csv")

# get South Africa data from WHO dataset

sa_data = who_dataset[who_dataset['DIM_COUNTRY_CODE'] == 'ZAF']

#lower case  and remove spaces to allow them to combine without any problem
sa_disease = sa_data["DIM_GHECAUSE_TITLE"].str.lower().str.strip()
dataset["Disease_clean"] = dataset["diseases"].str.lower().str.strip()

# find matching disease
matching_diseases = dataset[dataset["Disease_clean"].isin(sa_disease)]

# Adding new diseases to matching list
additions = ["human immunodeficiency virus infection (hiv)",
             "lung cancer","brain cancer","allergy","panic attack",
             "diabetes","heart attack","tooth disorder","skin cancer",
             "pregnancy","depression","drug abuse","food allergy","alcoholic liver disease",
             "flu","chickenpox"]

# disease names from matched list
matched_disease_names = matching_diseases["Disease_clean"].unique().tolist()

#combine addition and matched lists
final_diseases_name = list(set(matched_disease_names + additions))


# filter full dataset
final_filtered_dataset  = dataset[dataset["Disease_clean"].isin(final_diseases_name)]

#remove the disease_clean column
final_filtered_dataset.drop(columns=["Disease_clean"] , inplace = True)

# done cleaned
dataset = final_filtered_dataset
print(dataset.head())


#export the dataset
dataset.to_csv("./        data/processed/clean_dataset.csv",index=False)
print("Succefully exported")
