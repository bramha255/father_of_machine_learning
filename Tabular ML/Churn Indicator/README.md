<h1>End-to-End Machine Learning Churn Model</h1>
For this End-to-End we mean from data collection till deployment of the model

# Objective
Mail objective of this project is to take the model and take it to the user using **Web App** so they can use to predict whether customer will churn or not



For this we have used a [bank churn dataset](https://www.kaggle.com/datasets/adammaus/predicting-churn-for-bank-customers)


Trying out different model with default parameter and choosing one out of it \
*Note: This is not the best way to choose a model but we are just simplifying the process in the future version must robost model will be considered and used* 

### Data Manipulation 
We have done basic checks like
- Checking for empty values
  - We found there is no empty values
- Checking whether dataset is balanced 
  - We found the data is unbalanced since we saw ~79% data is from Retained customer and only 21% is from Exited customer 
- Correlation of the data
  - We found the correlation of the data and found useful information(we will also get important features from the model after trained to see which feature affect the most)

### Model Training and evaluation
As seen in the code we have tried using 
1. Logistic Regression
2. Support Vector Machine
3. KNearest Classifier
4. Random Forest Classifier

But Random Forest Classifer gave better result(with default values) and decided to fine tune that using GridSearchCV

     GridSearchCV is a technique used to find the optimal hyper-parameter for a model. \
     To use this we need to know the model and what are the hyper-parameters we can finetune and provide a dict which consists of different value for a parameter it has to try \
     *Beware this takes lot of computation power since it tries to fit model with multiple parameter combination and get the best out of it*
     
Using that we came to find the no. of trees(estimators), max_depth and, etc.. \

We have evaluated the model using sklearn classification report which is a fantastic metric that outputs mainly
- Accuracy
- Precision
- Recall 
- f1 score
- weighted average
- macro average

Here we mainly focused on first 4 metrics 
1. Accuracy: We don't want to use this since the data is imbalanced i.e model can get higher accuracy by just predicting "Retained" \
2. Precision and Recall: We use this to get a better understanding of the model for each class.
3. f1 score: Its a combination of the precision and Recall so we can use that as a metric to measure the model's performance.

### Final Note:
The model is not the greatest but it is working and able to detect 46% of the customer who are leaving.

**Test data metrics** 

              precision    recall  f1-score   support

           0       0.88      0.96      0.92      1207
           1       0.75      0.46      0.57       293

    accuracy                           0.86      1500
    macro avg      0.81      0.71      0.74      1500
    weighted avg   0.85      0.86      0.85      1500
    
My thoughts:
- This model has been traied on a batch and bank data are generated non-stop so using additional data we can improve the models' performance.
- Trying Deep Learning can also improve model's performance but it was avoided(Purely my decision nothing more than that)
- Also the end product of this project is bringing the model to the user using **Web App** which we have done and you can check that out ** [here](Provide link here)**

