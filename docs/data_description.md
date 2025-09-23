### Data

The dataset we used in our project is  relevant to the problem of predicting `diseases` from patient `symptoms`.
It contains both the `features (symptoms)` and the `target variable (disease)` required for supervised machine learning.

Structure of the Dataset
* Target Column (diseases) – the label representing the medical condition.  
        - e.g. `panic disorder`, `flu`, `diabetes`, etc

* Feature Columns - Multiple symptom columns.     
                - e.g. `anxiety`, `depression`, `chest pain`, `dizziness`, `shortness of breath`, etc
  * each represented in binary format:   
                   1 = symptom present   
                   0 = symptom absent


Example Record
 * Disease: allergy
 * Symptoms: `anxiety and nervousness(0)`, `depression (1)`, `shortness of breath (1)`, `depressive or psychotic symptoms (1)`, `sharp chest pain (0)`, …

dataset shape:(15917,378)
