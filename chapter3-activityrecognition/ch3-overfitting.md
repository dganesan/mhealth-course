---
layout: default
title: Overcoming Overfitting
parent: Activity Recognition
grand_parent: Mobile Sensing &amp; Analytics
nav_order: 8
usemathjax: true
description: "Activity Recognition"
---
## Human Activity Recognition
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}
---

## Introduction to Overfitting

Overfitting is a prevalent phenomenon in machine learning where a model learns to fit the training data too closely, capturing even its noise and outliers. This means that while it performs exceptionally well on training data, its performance degrades on unseen data.

### Why Does Overfitting Occur?

In the context of decision trees, the depth or complexity of the tree plays a significant role in overfitting. A decision tree that is too deep will have leaves with very specific decisions, often based on individual or minimal data points. Such granularity can mean the tree is fitting to the noise in the data rather than the underlying patterns. While overfitting is particularly pronounced in decision trees due to their hierarchical nature, it's essential to note that overfitting can occur in any machine learning algorithm.

Noise in the data further exacerbates overfitting. In real-world datasets, it's not uncommon to find inconsistencies or errors—these are referred to as noise. When a model, like a deep decision tree, learns from such data, it might treat this noise as valid patterns, leading to overfitting.

### A Closer Look with Cardiac Risk Assessment

Imagine our cardiac risk assessment dataset has some inconsistencies. Maybe a few healthy individuals have been mistakenly labeled as high risk due to errors in manual data entry. A deep decision tree might create specific branches to classify these individuals correctly based on the noisy data. However, when we introduce new data, these branches misclassify because they were based on incorrect data in the first place.

## Addressing Overfitting: Basic Approaches

Cross validation is an evaluation method to identify how well the classifier will perform for data it has not already seen. One way is to not use the entire data set when training a learner. Some of the data is removed before training begins. Then when training is done, the data that was removed can be used to test the performance of the learned model on ``new'' data. This is the basic idea for a whole class of model evaluation methods called _cross validation_.

### Train-Test Split

A foundational approach to handle overfitting by cross-validation is dividing the data into a training set and a test set. This is also referred to as the **holdout method** and is the simplest kind of cross validation. The data set is separated into two sets, called the training set and the testing set. A common rule of thumb is to use 70\% of the dataset for training and 30\% for testing. Dividing the data into training and test subsets is usually done randomly, in order to guarantee that there is no systematic error in the process.

- **Train Model**: Use the training set to teach the model. 
- **Evaluate**: Test its performance on the unseen test set.
- **Tweak and Repeat**: Based on the test set performance, make changes to the model, train it again, and keep repeating this loop.

By evaluating the model on the test set, which it hasn't seen during training, we get a clearer picture of how the model performs on new, unseen data. The idea is to select the model version that gives the best performance on the test set. However, its evaluation may depend heavily on which data points end up in the training set and which end up in the test set, and thus the evaluation may be significantly different depending on how the division is made.

## The Role of Validation Sets

While the train-test methodology helps, there's still room for over-optimizing on the test set, especially when we make numerous tweaks based on test set performance. To avoid this, we introduce a third dataset called the validation set.

- Train the model on the training set.
- Tweak and tune the model based on performance on the validation set.
- Only once you've finalized the model, evaluate it on the test set to get an unbiased performance metric.

Having a separate validation set allows us to make adjustments without biasing our model to the test data.

## K-fold Cross-Validation: Beyond Simple Splits

While train-test and train-validation-test splits are fundamental to avoiding overfitting, they might not always be enough. This is where k-fold cross-validation comes into play.

### Understanding K-fold Cross-Validation

Instead of dividing the dataset into two or three static sets, k-fold cross-validation divides the dataset into \( k \) different subsets (or "folds"). The model is trained and evaluated \( k \) times, each time using a different fold as the test set and the remaining \( k-1 \) folds combined as the training set. This process is iterated until every fold has been used as the test set.

For example, in a 5-fold cross-validation:
1. In the first iteration, Fold 1 is the test set, and Folds 2-5 combined are the training set.
2. In the second iteration, Fold 2 becomes the test set, while Folds 1, 3, 4, and 5 are the training set.
... and so on until the fifth iteration.

### Advantages of K-fold Cross-Validation

1. **Better Utilization of Data**: Especially in scenarios where the dataset is limited in size, k-fold cross-validation ensures that every data point has been in the test set exactly once and in the training set \( k-1 \) times. This comprehensive utilization can lead to a more reliable estimate of model performance.
  
2. **Reduced Variability**: By averaging the results from the \( k \) folds, we can reduce the variance associated with a single random train-test split. This leads to a more stable and generalized model assessment.

3. **Mitigates Overfitting**: With multiple train-test splits, the model's ability to generalize is tested more rigorously, making it less likely that the model is overfitting to a specific subset of the data.

### Calculating Error in K-fold Cross-Validation

The final performance metric in k-fold cross-validation is typically the average of the errors across the \( k \) iterations. If \( E_i \) represents the error in the \( i^{th} \) fold, the overall error \( E \) is calculated as:

\[ E = \frac{1}{k} \sum_{i=1}^{k} E_i \]

By taking the average error across the folds, we ensure that the model's performance is not overly influenced by any single partition of the data.

Overfitting remains one of the primary challenges in machine learning. Recognizing its signs and employing techniques like train-test splits and validation sets are crucial first steps in combating it. K-fold cross-validation, with its systematic approach to training and evaluating, offers a robust mechanism to understand a model's performance. While it can be computationally more intensive, the insights gained from multiple evaluations often outweigh the costs, leading to more trustworthy and generalizable models.

### Implementing Train-Test Splitting  in Python

```python
from sklearn.model_selection import train_test_split

features = ['x_mean', 'y_mean', 'z_mean', 'x_std', 'y_std', 'z_std']  # and other feature columns if needed
X = resampled_data[features]
y = resampled_data['label']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

The `test_size` parameter defines the proportion of the dataset to include in the test split. A common split ratio is 80\% training and 20\% testing.

#### Optimizing Tree Depth to Prevent Overfitting

A simple way to prevent overfitting in decision trees is to control the depth of the tree. A tree that is too deep might overfit the training data, while a very shallow tree might underfit. 

To find the optimal depth, you can:
1. Train multiple trees with varying depths.
2. Evaluate each tree on the test set.
3. Choose the depth that gives the best performance on the test set.

Here's a simple example using scikit-learn:

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

best_depth = 1
best_accuracy = 0

# Check for depths from 1 to 10
for depth in range(1, 11):
    clf = DecisionTreeClassifier(max_depth=depth, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    if acc > best_accuracy:
        best_accuracy = acc
        best_depth = depth

print(f"Best depth is: {best_depth} with accuracy: {best_accuracy}")
```

#### Other Strategies:

1. **Pruning**: Instead of letting the tree grow to its maximum depth, you can prune it to remove nodes that add little power to the classification.
2. **Minimum Split Size**: Set the minimum number of samples required to split an internal node.
3. **Minimum Leaf Size**: Set the minimum number of samples required to be at a leaf node.
4. **Cross-Validation**: Instead of a single train/test split, use k-fold cross-validation to get an average performance metric, which will provide a more robust performance estimate.
5. **Feature Importance**: Some features might be noisy. Decision trees in scikit-learn provide a `feature_importances_` attribute, which can be used to understand which features are most informative and potentially remove or adjust features that add noise.

Remember, while it's important to ensure your model doesn't overfit the training data, it's equally crucial to ensure it doesn't underfit by being too simplistic. Balancing complexity and simplicity is key to building a robust decision tree classifier.

### Implementing k-fold Cross-Validation in Python

Here's how you can implement k-fold cross-validation using scikit-learn:

```python
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

# Define the classifier
clf = DecisionTreeClassifier(max_depth=3, random_state=42)  # Example depth

# Use cross_val_score for k-fold cross-validation
k = 5  # for a 5-fold cross-validation
scores = cross_val_score(clf, X, y, cv=k, scoring='accuracy')

average_score = scores.mean()
print(f"Average accuracy across {k} folds: {average_score:.2f}")
```

The advantage of k-fold cross-validation is that it uses the entire dataset for both training and validation, ensuring a more comprehensive evaluation. However, keep in mind that it requires training the model \(k\) times, which might be computationally expensive for larger datasets or complex models.

#### Combining Cross-Validation with Hyperparameter Tuning

When optimizing hyperparameters, such as the depth of a decision tree, it's beneficial to combine k-fold cross-validation. By doing this, you ensure that the selected hyperparameters are robust across different data subsets. Here's an example using `GridSearchCV` which will search for the best depth while performing k-fold cross-validation:

```python
from sklearn.model_selection import GridSearchCV

# Define the parameter grid
param_grid = {'max_depth': range(1, 11)}

# Create the grid search object with k-fold cross-validation
grid_search = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid, cv=k, scoring='accuracy')

# Fit the grid search object to the data
grid_search.fit(X, y)

# Get the best parameters and score
best_depth = grid_search.best_params_['max_depth']
best_score = grid_search.best_score_

print(f"Best depth found using {k}-fold cross-validation: {best_depth}")
print(f"Best average accuracy: {best_score:.2f}")
```
This combined approach will give a more robust estimation of the model's performance and the optimal hyperparameters, reducing the risk of overfitting on the training data.

### Notebook: Tuning Tree Depth of Decision Tree Classifier ([html](notebooks/Chapter3-Classification-DecisionTree-IrisDataset.html)) ([ipynb](Chapter3-Classification-DecisionTree-IrisDataset.ipynb))
This notebook describes how you can plot the cross-validation scores as you vary the tree depth of a Decision Tree Classifier, and prune the tree at an appropriate depth to avoid overfitting.
