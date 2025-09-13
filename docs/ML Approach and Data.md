# Machine Learning Approach

Our project uses a classification approach because the goal is to predict a disease category based on given symptoms. The solution is relevant since classification algorithms are designed for problems where the output is a discrete label 

We planned the workflow as follows:
 * Encode symptoms using one-hot encoding
 * Encode disease labels using label encoding or dummies
 * Train and compare different classification algorithms.
 * Select the best-performing model for deployment in the GUI.

The algorithms chosen:
 * Decision Tree Classifier – Simple and provides clear decisions rules
 * Naïve Bayes – Fast  and effective with categorical features
 * Logistic Regression (multiclass) – baseline model.
 * Random Forest – ensemble method that improves accuracy.

 # Data 
The MED-Access system needs good quality medical data to work well. This data should give a clear and correct picture of patient health. It includes information such as patient details and medical history, descriptions of symptoms, results from tests like blood work and basic health measurements (such as heart rate, blood pressure, and temperature), and medical images such as X-rays, CT scans, and MRIs.

Records of past cases with confirmed diagnoses are also important because they help train the AI to make better predictions. The system will use this data to learn, test, and improve its accuracy, and it will keep updating as new information is added. Since all these data types are directly connected to patient care and diagnosis, they are reliable and useful for solving the problem of too few doctors in hospitals and clinics
