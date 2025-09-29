import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Load the trained model
model = joblib.load("./Models/best_model.joblib")

#create random patient data using 1 and 0 
patientData1 = np.random.randint(0, 2, size=(10, 377))  

# Make predictions
predictions = model.predict(patientData1)

# Load the encoder used during training
dataset = pd.read_csv("./data/processed/clean_dataset.csv")
le = LabelEncoder()

# fit and Decode predictions back to disease names
le.fit(dataset["diseases"])
decoded_predictions = le.inverse_transform(predictions)


# Display results
for i, disease in enumerate(decoded_predictions):
    print(f"Sample {i+1}: Predicted disease → {disease}")
