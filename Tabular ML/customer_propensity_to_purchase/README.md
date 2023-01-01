<h1 align='centre'>
Customer propensity to purchase detection
</h1>

<p>
This project is about detection whether a customer's going to buy a product or not 

Dataset: https://www.kaggle.com/datasets/benpowis/customer-propensity-to-purchase-data \
View the script in colab to see a rendered version

### Insights from dataset:
1. Dataset only has the information about current clicks and pages viewed and nothing from paste purchases.
2. Since it doesn't have any historical data of the customer we can't give a full on perfect prediction \
  eg: If a user buys a tooth brush today and there's a possibility that user might buy tooth paste along with it but with this dataset we can't predict that. We have to
  predict purely based on their clicks while buying tooth paste
3. The dataset is also visibly predictable. If you see the checked_delivery_detail, sign_in and sign_out pages have more correlation with whether the user ordered the product or not.

### Model:
Reason I picked tree based model is to see how well 3 tree model with each other in a dataset which is basically yes or no question and since the data is visually understandable we can have more insights from these models.
  1. Decision tree
  2. Random Forest tree (Bagging)
  3. XGBoost (Boosting) \
Above are the 3 models picked where 
- Decision consist of only one tree and prone to overfit
- Random Forest is a collection of decision tree and uses bagging technique and picks to pick the final prediction and like it name suggests it picks the subset of data randomly and uses to fit a tree
- XGboost is said to be the best out of above 2 model due to its way of building the tree model in series by correcting previous's error rather than in parallel without having any connection with other model like random forest.

From the output we can see that Random Forest actually give priority to more features than xgboost and decision tree which prioritized 'checked_delivery_detail' and 'saw_checkout' more than any other.
and since the output of all the models are same I would go with random forest in this scenario.

Remember:
  This data is easy to interept and the true potential of the 3 models will be understood in a much more complex data.
  Which is a point to try in the future.
