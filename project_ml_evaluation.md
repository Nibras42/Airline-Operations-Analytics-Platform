#### SER541: Machine Learning Evaluation  
#### Title: Aircraft Type and Capacity Allocation Patterns in U.S. Domestic Airline Routes  
#### Author: Anonymous  
#### Date: April 2026  

---

## Evaluation Metrics

### Metric 1  
**Name:** Mean Squared Error (MSE)  

**Choice Justification:**  
MSE measures the average squared difference between predicted and actual values. It is appropriate for regression problems where prediction accuracy is important.  

**Interpretation:**  
Lower MSE indicates better model performance.  

---

### Metric 2  
**Name:** R² Score  

**Choice Justification:**  
R² measures how well the model explains the variance in the target variable. It provides insight into how much of the variability in load factor is captured by the model.  

---

## Alternative Models

### Baseline Model  
**Construction:**  
Linear regression using only SEATS as input.  

**Evaluation:**  
MSE: 0.073267  
R²: 0.065651  
This model performs poorly, indicating that seat capacity alone is not sufficient to predict load factor.  

---

### Main Linear Model  
**Construction:**  
Linear regression using SEATS, DEPARTURES_PERFORMED, and AIRCRAFT_TYPE.  

**Evaluation:**  
MSE: 0.048559  
R²: 0.380746  
This model significantly improves performance, showing that multiple operational factors influence load factor.  

---

### Ridge Model  
**Construction:**  
Ridge regression with regularization applied to the main feature set.  

**Evaluation:**  
MSE: 0.073267  
R²: 0.065651  
This model performs similarly to the baseline, indicating that regularization negatively impacted performance in this case.  

---

### Lasso Model  
**Construction:**  
Lasso regression applied to the main feature set.  

**Evaluation:**  
MSE: 0.053997  
R²: 0.311393  
This model performs moderately well but removes some useful features, leading to reduced performance compared to the main linear model.  

---

### KNN Model  
**Construction:**  
K-Nearest Neighbors regression using k=5.  

**Evaluation:**  
MSE: 0.047077  
R²: 0.399643  
This model achieves the best performance, capturing non-linear relationships between features and load factor.  

---

## Best Model  

**Model:** KNN Regressor  
This model provides the lowest prediction error and highest explanatory power, making it the best-performing model for this problem.