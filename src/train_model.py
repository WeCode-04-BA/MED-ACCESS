# Regular EDA and plotting libraries
import numpy as np
import pandas as pd

# Models from Scikit-Learn
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
#Model Evaluations
from sklearn.model_selection import train_test_split,cross_val_score

#import dataset
dataset = pd.read_csv("./data/processed/clean_dataset.csv")

# Use the labelEncode()  to encode the diseases column
le = LabelEncoder()
dataset["disease_encoded"] = le.fit_transform(dataset["diseases"])

# Separate dataset into X and y
X = dataset.drop({"diseases","disease_encoded"} ,axis=1)
y = dataset["disease_encoded"]

#Split the data into train and test
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2)

#Set random seed
np.random.seed(42)

#create a new classifier with best parameters
clf = GaussianNB(var_smoothing = 1e-09)

#fit the model
clf.fit(X_train,y_train)

#accuracy score
print(f"accuracy score: {clf.score(X_test,y_test)}")

#predicted values
print(f"predicted values: {clf.predict(X_test)}")

#decode predicted values
decode_preds = le.inverse_transform(clf.predict(X_test))
print(f"decode  predicted values:{decode_preds}")

# Export the model
from joblib import dump , load
# save model to file
dump(clf,filename = "./Models/best_model.joblib")
print("Successfully exported the model")