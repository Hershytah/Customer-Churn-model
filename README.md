# Customer-Churn-model

This project aims to analyze customer data to find out how churning depends on different factors.<br>
The project also builds a prediction model after evaluating accuracy , precision and recall scores.

## Problem Statement 

The goal of this project is to:

1. Analyze how churning depends on differrent variables.
2. Explore how Binning, One Hot Encoding and creating dummy variables work.
3. Gathering insights that compels a story out of data.
4. Handling Imbalanced data and exploring Smoteen.
5. Exploring different models like Decision tree classifier, Random forest, svm ,etc.
6. Evaluating models using measures like accuracy, recall and precision scores.
7. Saving the model using pickle.

## Data Description

Source : The dataset was obtained from UCI Machine Learning Repository.

Rows and columns : 3150 rows and columns

Data Description :

Call Failures: number of call failures.<br>
Complains: binary (0: No complaint, 1: complaint).<br>
Subscription Length: total months of subscription.<br>
Charge Amount: Ordinal attribute (0: lowest amount, 9: highest amount).<br>
Seconds of Use: total seconds of calls.<br>
Frequency of use: total number of calls.<br>
Frequency of SMS: total number of text messages.<br>
Distinct Called Numbers: total number of distinct phone calls.<br>
Age Group: ordinal attribute (1: younger age, 5: older age).<br>
Tariff Plan: binary (1: Pay as you go, 2: contractual).<br>
Status: binary (1: active, 2: non-active).<br>
Churn: binary (1: churn, 0: non-churn) - Class label.<br>
Customer Value: The calculated value of customer.

Target Variable : Churn

## Methodology :

1. Data cleaning and preprocessing:<br>
   a. Data Cleaning.<br>
   b. Binning.<br>
   c. One hot Encoding.<br>
   d. Creating dummy variables.<br>
2. Exploratory Data Analysis <br>
  a. Univariate Analysis.<br>
  b. Bivariate Analysis.<br>
3. Insights and Conclusions.
4. Experimenting with Different models while evaluating accuracy measures.
5. Saving the model using pickle.

## Technology Used :

1. Python
2. Pandas, Numpy
3. Matplotlib, seaborn
4. Scikit Learn
5. Smoteen
6. Jupyter notebook
7. Pickle

## Results and Insights:

1.The data consists of very low proportion of churning customers to study.<br>
  The churn ratio is 84:16, The data is highly imbalanced.

  <img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/230ebe04-7b92-491a-8dc2-ea603235dc14" />

2. Inactive customers and Customers with complaints are very likely to churn.<br>
  (1 - active , 2 - non-active).<br>
  
  <img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/e8f1ce3d-0c86-4049-b563-2f28d46ba5a0" />
  <img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/8556ff66-9bb1-4abe-84c8-30f5142ec087" />


3. Customers with the lowest charge amount are likely to churn as they have the highest ratio comparatively.
  
4. Pay as you go customers have a very high ratio of churning while the customers with contractual payments have a negligible ratio.<br>
  (1 - pay as you go, 2 - contractual).<br>

   <img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/2b3636c1-2055-48ff-9fe0-866e8987e791" />

5. Customers with subscription length of 25-36 and 37-48 are very likely to churn.
 
6. Customers in the age group 25-34 have the highest chances of churning.

7.Low usage customers → High chance of churn.<br>
High usage customers → Much lower chance of churn.<br>
This is a strong indicator that engagement (measured in seconds of use) is a good predictor of churn.<br>

  <img width="991" height="665" alt="image" src="https://github.com/user-attachments/assets/8982635a-634f-4cfc-80e3-b247be93da6a" />

8.Churning is higher when the frequency of SMS is low.

  <img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/4b763cdd-8dc6-424c-939c-e79e53896c1b" />

## Conclusion:

The analysis successfully presents the part that every variable plays in influencing the target variable and a final prediction model is saved after consistent evaluation of experimenting various available models.

## References:

https://archive.ics.uci.edu/dataset/563/iranian+churn+dataset
