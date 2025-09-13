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