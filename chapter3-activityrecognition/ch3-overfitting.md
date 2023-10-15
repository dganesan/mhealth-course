---
layout: default
title: Overcoming Overfitting
parent: Activity Recognition
grand_parent: Mobile Sensing &amp; Analytics
nav_order: 7
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

## A Closer Look with Cardiac Risk Assessment

Imagine our cardiac risk assessment dataset has some inconsistencies. Maybe a few healthy individuals have been mistakenly labeled as high risk due to errors in manual data entry. A deep decision tree might create specific branches to classify these individuals correctly based on the noisy data. However, when we introduce new data, these branches misclassify because they were based on incorrect data in the first place.

## Addressing Overfitting: Basic Approaches

### Train-Test Split

A foundational approach to handle overfitting is dividing the data into a training set and a test set. 

- **Train Model**: Use the training set to teach the model. 
- **Evaluate**: Test its performance on the unseen test set.
- **Tweak and Repeat**: Based on the test set performance, make changes to the model, train it again, and keep repeating this loop.

By evaluating the model on the test set, which it hasn't seen during training, we get a clearer picture of how the model performs on new, unseen data. The idea is to select the model version that gives the best performance on the test set.

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

## Conclusion

Overfitting remains one of the primary challenges in machine learning. Recognizing its signs and employing techniques like train-test splits and validation sets are crucial first steps in combating it. K-fold cross-validation, with its systematic approach to training and evaluating, offers a robust mechanism to understand a model's performance. While it can be computationally more intensive, the insights gained from multiple evaluations often outweigh the costs, leading to more trustworthy and generalizable models.

