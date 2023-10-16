---
layout: default
title: Evaluating Classifier Performance
parent: Activity Recognition
grand_parent: Mobile Sensing &amp; Analytics
nav_order: 9
usemathjax: true
description: "Chapter 3"
---
## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}
---

## Chapter 4: Evaluating Classifier Performance

So far, we have seen how to construct a decision tree classifier. But how do we ensure that our decision tree classifier (or any classifier) is up to the task? This chapter delves into the world of classifier evaluation.

### Understanding the Confusion Matrix

At the heart of evaluating classifiers is the confusion matrix. It offers a snapshot of how a classifier performed, providing insights into both correct predictions and different types of errors.

A confusion matrix for our three-class problem (Sitting, Standing, and Walking) can be visualized as:

| **Actual \ Predicted** | **Sitting (A)** | **Standing (B)** | **Walking (C)** |
|----------------------|--------------|---------------|--------------|
| **Sitting (A)**          | 25           | 5             | 2            |
| **Standing (B)**        | 3            | 28            | 1            |
| **Walking (C)**         | 1            | 0             | 30           |

The **rows** of this matrix represent the **actual** classes, while the **columns** represent the **predicted** classes.

### True Positives, True Negatives, False Positives, and False Negatives

To better interpret the matrix, we need to understand a few essential terms:

- **True Positive (TP)**: Refers to the cases where the classifier correctly predicts a positive outcome. For instance, in our example, there are **25** TPs for **Sitting (A)** where the classifier correctly predicted 'Sitting' when the actual activity was indeed 'Sitting'.

- **True Negative (TN)**: Refers to the cases where the classifier correctly predicts a negative outcome. Considering the 'Sitting' class, a TN would be a situation where an instance was correctly predicted as 'not Sitting'.

- **False Positive (FP)**: It's when the classifier incorrectly predicts a positive outcome. For instance, if the actual activity was 'Sitting', but the classifier predicted 'Walking', it has committed a false positive error for the 'Walking' class. 

- **False Negative (FN)**: It's when the classifier incorrectly predicts a negative outcome. If the actual activity was 'Walking' but the classifier predicted 'Sitting', it has made a false negative error for the 'Walking' class.

**Visual Example**:

Let's break down the 'Walking' activity in our matrix:
- **30** instances were correctly classified as **Walking (C)** – these are **True Positives**.
- **1** instance of **Standing (B)** was mistakenly classified as **Walking (C)** – a **False Positive** for the 'Walking' detection.
- **2** instances were actually **Sitting (A)** but were mistakenly classified as **Walking (C)** – these are also **False Positives** for the 'Walking' detection.
- Instances where the actual activities were either **Sitting (A)** or **Standing (B)** and were not classified as **Walking (C)** contribute to **True Negatives** for 'Walking'.

### Metrics Derived from the Confusion Matrix

**Accuracy**: Represents the overall correctness of the classifier.

\[ \text{Accuracy} = \frac{\text{Sum of correct classifications (diagonal values)}}{\text{Total number of classifications}} \]

Number of Correct Predictions (Diagonal elements): 25 + 28 + 30 = 83
Total Predictions: Sum of all elements in the matrix = 95

\[ \text{Accuracy} = \frac{83}{95} = 0.8737 \] or 87.37\%

While Accuracy is calculated across all classes, the bellow three metrics i.e. Precision, Recall, and F1 Score, are typically defined for each class, especially in multi-class classification problems.

**Precision**: Given that a specific class was predicted, how often was that prediction correct? 

\[ \text{Precision}_A = \frac{\text{tp}_A}{\text{tp}_A + \text{fp}_A} \]
Where tp (true positive) is the correct prediction count for that class, and fp (false positive) is the count of other classes incorrectly predicted as that class.

For Sitting (A), Precision would be:

\[ \text{Precision}_A = \frac{25}{25 + 3 + 1} \approx 0.86 \]

**Recall (Sensitivity)**: Of all the instances of a specific class in the dataset, how many were correctly predicted by the classifier?

\[ \text{Recall}_A = \frac{\text{tp}_A}{\text{tp}_A + \text{fn}_A} \]
Where fn (false negative) is the count of instances of that class incorrectly predicted as another class.

For Sitting (A), Recall would be:

\[ \text{Recall}_A = \frac{25}{25 + 5 + 2} \approx 0.78 \]

**F-measure (F1 Score)**: A balanced harmonic mean of Precision and Recall, helpful when you want to balance the two metrics and have a single performance number.

\[ \text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} \]

To get the F1 Score, we first need the precision and recall for each class. Let's compute it for the class 'Sitting (A)':

#### Precision for 'Sitting (A)':
\[ \text{Precision}_A = \frac{\text{TP}_A}{\text{TP}_A + \text{FP}_A} = \frac{25}{25 + 3 + 1} = \frac{25}{29} = 0.8621 \]

#### Recall for 'Sitting (A)':
\[ \text{Recall}_A = \frac{\text{TP}_A}{\text{TP}_A + \text{FN}_A} = \frac{25}{25 + 5 + 2} = \frac{25}{32} = 0.7813 \]

#### F1 Score for 'Sitting (A)':
\[ \text{F1 Score}_A = 2 \times \frac{0.8621 \times 0.7813}{0.8621 + 0.7813} = 0.8197 \]

Similarly, you can calculate the precision, recall, and F1 Score for classes 'Standing (B)' and 'Walking (C)'.

With these evaluation metrics in hand, you can rigorously assess your decision tree classifier and understand its strengths and potential areas of improvement.

### Caveat: Data Imbalance (Class Skewness)

Often, the dataset used to evaluate a classifier might not have an even distribution of classes. Imagine a scenario where you have 1000 instances of 'Walking' but only 50 instances of 'Sitting' and 50 instances of 'Standing'. This creates a data imbalance.

**Problems with Data Imbalance**:
- **Biased Classifier**: The classifier might tend to favor classes with a higher number of instances. It could achieve a high accuracy simply by predicting the majority class for all inputs, leaving the minority class poorly classified.
  
- **Misleading Accuracy**: With skewed data, a high accuracy might not indicate a well-performing classifier. For instance, a naive classifier that always predicts 'Walking' would achieve an accuracy of approximately 91\% in the skewed dataset above. Yet, it would be entirely failing to identify 'Sitting' and 'Standing' instances.

When faced with imbalanced datasets, it's essential to use metrics beyond just accuracy. Precision, recall, and F1 score give a clearer picture of classifier performance.

The implications of these errors can vary based on the application. In some contexts, a false positive might be more problematic than a false negative, and vice-versa.
