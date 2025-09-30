### Model Evaluation

The AI model developed in our project will be evaluated using standard supervised learning metrics for multiclass classification. When we build our disease prediction AI, we need to test its accuracy.

### Evaluation Strategy

* How we test it       
`Train-Test Split`: We cut the dataset into two parts. One part teaches the AI (training set), and the other part checks how well it learned (testing set).     
`Cross-Validation`: Instead of testing only once, we test multiple times on different splits to make sure results are reliable.

* How we measure it (metrics)     
`Accuracy` - Out of all predictions, how many are correct?      
`Precision` - When the AI says “you have a disease,” how often is it right?      
`Recall` - Out of all people who actually have a disease, how many did the AI correctly find?     
`Classification report` - return some of the main classification metrics such as precision, recall, and f1-score     
`F1-Score` - A balance between precision and recall.      
`Confusion Matrix` - A table that shows where the AI got things right and where it got confused     
`ROC Curve` - Plots true positive rate and false positive rate.      
`AUC-Summarizes` the ROC curve. A perfect model achieves an AUC score of 1.0.     


### Time Series Analysis on Data
Our dataset only shows whether a symptom is present (1) or not (0) for each patient. It does not track patients over time.
This means we cannot use normal time series methods (like `ARIMA` or `LSTM`) because there is no  `timeline` in our dataset.
But if we had data collected over time then time series analysis would make sense.


