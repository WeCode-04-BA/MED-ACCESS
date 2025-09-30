
import joblib
import pandas as pd

#Model Evaluations
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import confusion_matrix
from sklearn.metrics import  accuracy_score ,precision_score , recall_score , f1_score
from sklearn.preprocessing import LabelEncoder

#import dataset , encode the diseases column,Separate  dataset into X and y and split data into train and test
dataset = pd.read_csv("./data/processed/clean_dataset.csv")
le = LabelEncoder()
dataset["disease_encoded"] = le.fit_transform(dataset["diseases"])
X = dataset.drop({"diseases","disease_encoded"} ,axis=1)
y = dataset["disease_encoded"]
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2)

#load  the model
model = joblib.load("./Models/best_model.joblib")

# Make predictions
y_pred = model.predict(X_test)

# Loop control
keep_running = True

while keep_running:
    # Menu
    print("\n📊 Choose a metric to view:")
    print("1. Accuracy")
    print("2. Precision")
    print("3. Recall")
    print("4. F1-score")
    print("5. Confusion Matrix")
    print("6.  Exit and create report")
    choice = input("Enter your choice (1–6): ")
    print("\n" * 100)
   

    if choice == "1":
        accuracy = accuracy_score(y_test,y_pred)
        print(f"\n Accuracy: {accuracy:.4f}")
    elif choice == "2":
        precision = precision_score(y_test , y_pred , average="weighted")
        print(f"\n Precision: {precision:.4f}")
    elif choice == "3":
        recall = recall_score(y_test,y_pred , average="weighted")
        print(f"\n Recall: {recall:.4f}")
    elif choice == "4":
        f1 = f1_score(y_test,y_pred,average="weighted")
        print(f"\n F1-score: {f1:.4f}")
    elif choice == "5":
       cm = confusion_matrix(y_test,y_pred)
       print("\n Confusion Matrix:")
       print(cm)
    elif choice == "6":
        keep_running = False
        # Calculate metrics
        accuracy = accuracy_score(y_test,y_pred)
        precision = precision_score(y_test , y_pred , average="weighted")
        recall = recall_score(y_test,y_pred , average="weighted")
        f1 = f1_score(y_test,y_pred,average="weighted")
        cm = confusion_matrix(y_test,y_pred)
        #create report string
        report = (f"\n Accuracy: {accuracy:.4f} \n Precision: {precision:.4f} \n Recall: {recall:.4f} \n F1-score: {f1:.4f} \n Confusion Matrix:\n {cm}")
        print(report)
        with open("./reports/model_evaluation.txt", "w") as file:
           file.write(report)
        print("report saved!,Thanks for evaluating our model!")


