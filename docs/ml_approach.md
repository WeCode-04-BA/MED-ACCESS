# Machine Learning Approach

Our project uses a `classification` approach because the goal is to predict a `disease` category based on given `symptoms`. The solution is relevant since `classification` algorithms are designed for problems where the output is a discrete label 

We planned the workflow as follows:
 * Clean data, remove duplicates,
 * Encode the target disease column.
 * Use symptom indicators (0/1) as features.
 * Train and compare different classification algorithms.
 * Compare accuracy, precision, recall, F1-score, and confusion matrix for each model.
 * Choose the best-performing model for deployment.

The algorithms chosen:
 * Decision Tree Classifier – Simple and provides clear decisions rules
 * Naïve Bayes – Fast  and effective with categorical features
 * Logistic Regression (multiclass) – baseline model.
 * Random Forest Classifier – ensemble method that improves accuracy.
 * LinearSVC - Effective for high-dimensional data such as symptoms represented in 0/1   format.
 * KNeighborsClassifier - Non-parametric method that classifies based on similarity to  neighboring cases.

 
