### Solution Techniques

We built a model that predicts diseases from symptoms (0 = symptom present, 1 = absent). This is a multiclass classification problem since the AI must choose one disease from many. 

**Techniques Used**: The data was cleaned, duplicates removed, and diseases encoded into numerical form.
Classification algorithms were tested, including `Decision Tree`, `Random Forest`, `Logistic Regression`, `Naïve Bayes`, `LinearSVC`, and `KNeighborsClassifier`.

 **Improving Accuracy**: Accuracy was improved using `hyperparameter tuning GridSearchCV` and by comparing multiple models to select the best performer.
