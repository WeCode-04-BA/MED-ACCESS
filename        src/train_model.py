# Regular EDA and plotting libraries
import numpy as np
import pandas as pd

# Models from Scikit-Learn
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier

#Model Evaluations
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score


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

# Creating a dictionary
models = {"Decision Tree" :DecisionTreeClassifier(),
          "Naïve Bayes" : GaussianNB(),
          "Logistic Regression": LogisticRegression(),
          "Random Forest": RandomForestClassifier(),
          "LinearSVC": LinearSVC(),
          "KNeighbors": KNeighborsClassifier()}  


# Train and evaluate
best_model = None
best_score = 0
model_scores = {}

for name, model in models.items():
    
     #Set random seed
    np.random.seed(42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    model_scores[name] = score
    print(f"{name} Accuracy: {score:.2f}")
    
    if score > best_score:
        best_score = score
        best_model = model


# Export the model
from joblib import dump 

# save model to file
dump(best_model,filename = "./Models/best_model.joblib")
print("Successfully exported the model")
print(f"\n Best model saved: {type(best_model).__name__} with accuracy {best_score:.2f}")



