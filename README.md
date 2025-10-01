# MED-ACCESS: Disease Prediction Using AI

### Project Information
* Course: `DIPLOMA INFORMATION TECHNOLOGY` 
* Module: `Business Analysis 3.2 Project`
* Institution: `Vaal University of Technology (VUT)`
* Group Name: `WECODE-04`
* Year: `2025`

### Overview
MED-Access is an AI healthcare system designed to help address the shortage of doctors in `South Africa`. The system predicts diseases based on patient symptoms using `machine learning` classification algorithms.
By quickly analyzing symptoms, the model provides potential diagnoses that:
* Support doctors with faster decision-making
* Reduce patient waiting times

### Methods
* **Dataset**: Symptoms (0/1 binary values) as features, Disease as the target column.
* **Preprocessing**: Cleaning, duplicate removal, encoding diseases into numbers 
* **Algorithms Tested**:
  * Decision Tree Classifier
  * Naïve Bayes
  * Logistic Regression
  * Random Forest Classifier
  * LinearSVC
  * KNeighborsClassifier
* **Evaluation Metrics**:
  * Accuracy
  * Precision, Recall, F1-score
  * Confusion Matrix
  *  ROC Curve & AUC
* **Improving Accuracy**:
   * GridSearchCV

### Results
* Naïve Bayes a gave the best accuracy with `0.97`.
* Evaluation showed improvements after data cleaning, encoding, and hyperparameter tuning (GridSearchCV).

### Repository Structure

***
project-root/      
|--- data/     `raw and processed datasets`             
|--- src/          `scripts for cleaning, training, evaluating, prediction`       
|--- model/       `saved trained models`    
|--- reports/       `results`          
|--- notebooks/     `EDA, preprocessing, and model testing`      
|--- docs/          `documentation (report parts)`          
|--- poster/        `poster drafts`        
|--- presentation/     `slides, graphs for presentation`             
|--- README.md  `project documentation`
***

### Future Work
* **NLP**: Allow patients to describe symptoms in text.
* **Speech Recognition & Synthesis**: Patients can talk to the system, and it can talk back like a real conversation.
* **Chatbot**: An interactive assistant that asks about symptoms step by step and gives possible health suggestions.
* **Deep Learning**: CNNs for X-rays, RNNs/LSTMs for time-series health data.

### Group Members
* `Washu Ravele` 
* `Otshidzwa Kwinda` 
* `Lehlogonolo Mohlala` 
* `Vukona Chauke`

  
