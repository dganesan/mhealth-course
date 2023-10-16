---
layout: default
title: Cardiac Risk Prediction
parent: Activity Recognition
grand_parent: Mobile Sensing &amp; Analytics
nav_order: 6
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

## Example: Cardiac Risk Prediction

Suppose our dataset contains the following attributes:

1. **Age**: <40, 40-55, >55
2. **Smoker**: Yes, No
3. **Exercise**: Regularly, Rarely

Our target variable is:
**Risk**: High, Low

### Cardiac Risk Prediction Dataset

| Age     | Smoker | Exercise   | Risk |
|---------|--------|------------|------|
| <40     | No     | Regularly  | Low  |
| <40     | No     | Rarely  | Low  |
| <40     | No     | Rarely     | Low  |
| <40     | Yes    | Regularly  | Low  |
| <40     | Yes    | Rarely     | High |
| 40-55   | No     | Regularly  | Low  |
| 40-55   | No     | Rarely     | High |
| 40-55   | Yes    | Regularly  | High |
| 40-55   | Yes    | Rarely     | High |
| >55     | No     | Regularly  | Low  |
| >55     | Yes    | Regularly  | High |
| >55     | Yes    | Rarely     | High |
| >55     | No     | Rarely     | High |

### Initial Entropy Calculation

From the table:
- $p_{\text{Low}} = \frac{6}{13}$
- $ p_{\text{High}} = \frac{7}{13} $

Thus, the entropy for this set $ S $ is:
$ \text{Entropy}(S) = -\frac{6}{13} \log_2(\frac{6}{13}) - \frac{7}{13} \log_2(\frac{7}{13}) \approx 1$

### Information Gain Calculation

#### For Age

1. **Age <40:**
    - Total: 5
    - High Risk: 1
    - Low Risk: 4
    - $ \text{Entropy} = -\frac{1}{5} \log_2(\frac{1}{5}) - \frac{4}{5} \log_2(\frac{4}{5}) $ $ \approx 0.72 $

2. **Age 40-55:** 
    - Total: 4
    - High Risk: 3
    - Low Risk: 1
    - $ \text{Entropy} = -\frac{3}{4} \log_2(\frac{3}{4}) - \frac{1}{4} \log_2(\frac{1}{4}) \approx 0.81$
    
3. **Age >55:** 
    - Total: 4
    - High Risk: 3
    - Low Risk: 1
    - $ \text{Entropy} \approx 0.81 \text{(same as above)}$

Let us compute the weighted entropies and then the information gain for the Age attribute in the next step.

$ \text{Weighted Entropy for Age}  = \frac{5}{13} \times 0.72 + \frac{4}{13} \times 0.81 + \frac{4}{13} \times 0.81 \approx 0.78$

$ \text{Information Gain for Age} = \text{Initial Entropy} - \text{Weighted Entropy for Age} \approx 1 - 0.78 \approx 0.22$

#### For Smoker

1. **Smoker = Yes:** 
    - Total: 6
    - High Risk: 5
    - Low Risk: 1
    - $ \text{Entropy} = -\frac{5}{6} \log_2(\frac{5}{6}) - \frac{1}{6} \log_2(\frac{1}{6}) \approx 0.65 $
    
2. **Smoker = No:** 
    - Total: 7
    - High Risk: 2
    - Low Risk: 5
    - $\text{Entropy} = -\frac{2}{7} \log_2(\frac{2}{7}) - \frac{5}{7} \log_2(\frac{5}{7}) \approx 0.86$

$ \text{Weighted Entropy for Smoker}  \approx \frac{6}{13} \times 0.65 + \frac{7}{13} \times 0.86 \approx 0.76 $

$ \text{Information Gain for Smoker} = \text{Initial Entropy} - \text{Weighted Entropy for Smoker} \approx 1 - 0.76 \approx 0.24  $

#### For Exercise

1. **Exercise = Regularly:** 
    - Total: 6
    - High Risk: 2
    - Low Risk: 4
    - $ \text{Entropy} = -\frac{4}{6} \log_2(\frac{4}{6}) - \frac{2}{6} \log_2(\frac{2}{6}) = 0.92 $
    
2. **Exercise = Rarely:** 
    - Total: 7
    - High Risk: 5
    - Low Risk: 2
    - $ \text{Entropy} = -\frac{2}{7} \log_2(\frac{2}{7}) - \frac{5}{7} \log_2(\frac{5}{7}) = 0.86 $

$ \text{Weighted Entropy for Exercise} = \frac{6}{13} \times 0.92 + \frac{7}{13} \times 0.86 \approx 0.89 $

$ \text{Information Gain for Exercise} = \text{Initial Entropy} - \text{Weighted Entropy for Exercise} \approx 1 - 0.89 \approx 0.11 $

Given the information gains:

1. Age: 0.22
2. Smoker: 0.24
3. Exercise: 0.11

The attribute **Smoker** has the highest information gain and will be the root node. 

For the second-level decision, let's take the subset of data for one of the age groups, say "Age < 40", and repeat the computation of information gain for "Smoker" and "Exercise". We'll select the attribute with the highest information gain to split the data further. 

### Dataset subset for "Smoker = Yes"

| Age     | Smoker | Exercise   | Risk |
|---------|--------|------------|------|
| <40     | Yes    | Regularly  | Low  |
| <40     | Yes    | Rarely     | High |
| 40-55   | Yes    | Regularly  | High |
| 40-55   | Yes    | Rarely     | High |
| >55     | Yes    | Regularly  | High |
| >55     | Yes    | Rarely     | High |

From the subset, the probabilities are:

- $ p_{\text{High}} = \frac{5}{6} = 0.83 $
- $ p_{\text{Low}} = \frac{1}{6} = 0.17 $

Thus, the entropy for this subset $ S $ is: $-\frac{5}{6} \log_2(\frac{5}{6}) - \frac{1}{6} \log_2(\frac{1}{6}) $ $ \approx 0.65 $

#### For Age:

1. **Age <40:**
    - Total: 2
    - High Risk: 1
    - Low Risk: 1
    - $ \text{Entropy} = -\frac{1}{2} \log_2(\frac{1}{2}) - \frac{1}{2} \log_2(\frac{1}{2}) = 1 $

2. **Age 40-55:** 
    - Total: 2
    - High Risk: 2
    - Low Risk: 0
    - $ \text{Entropy} = 0$
    
3. **Age >55:** 
    - Total: 2
    - High Risk: 2
    - Low Risk: 0
    - $ \text{Entropy} = 0 $

$ \text{Weighted Entropy for Age}  = \frac{2}{6} \times 1 + \frac{2}{6} \times 0 + \frac{2}{6} \times 0 \approx 0.33$

$ \text{Information Gain for Age} = \text{Initial Entropy} - \text{Weighted Entropy for Age} \approx 0.65 - 0.33 \approx 0.32$

### Weighted Entropy and Information Gain for Exercise

1. **Exercise = Regularly:** 
    - Total: 3
    - High Risk: 2
    - Low Risk: 1
    - $ \text{Entropy} = -\frac{2}{3} \log_2(\frac{2}{3}) - \frac{1}{3} \log_2(\frac{1}{3}) = 0.92 $
    
2. **Exercise = Rarely:** 
    - Total: 3
    - High Risk: 3
    - Low Risk: 0
    - $ \text{Entropy} = 0 $

$ \text{Weighted Entropy for Exercise} = \frac{3}{6} \times 0.92 + \frac{3}{6} \times 0 = 0.46 $
$ \text{Information Gain for Smoker} = 0.65 - 0.46 = 0.19 $

Given the information gains for the "Age > 55" group:

1. Age: 0.32
2. Exercise: 0.19

"Age" has the higher Information Gain for this group, so we will choose this as the next level node for Smoker=Yes.


### Dataset subset for "Smoker = No"

| Age     | Smoker | Exercise   | Risk |
|---------|--------|------------|------|
| <40     | No     | Regularly  | Low  |
| <40     | No     | Rarely  | Low  |
| <40     | No     | Rarely     | Low  |
| 40-55   | No     | Regularly  | Low  |
| 40-55   | No     | Rarely     | High |
| >55     | No     | Regularly  | Low  |
| >55     | No     | Rarely     | High |

From the subset, the probabilities are:

- $ p_{\text{High}} = \frac{2}{7} = 0.29 $
- $ p_{\text{Low}} = \frac{5}{7} = 0.71 $

Thus, the entropy for this subset $ S $ is: $-\frac{2}{7} \log_2(\frac{2}{7}) - \frac{5}{7} \log_2(\frac{5}{7}) $ $ \approx 0.86 $

#### For Age

1. **Age <40:**
    - Total: 3
    - High Risk: 0
    - Low Risk: 3
    - $ \text{Entropy} = 0 $

2. **Age 40-55:** 
    - Total: 2
    - High Risk: 1
    - Low Risk: 1
    - $\text{Entropy} = 1$
    
3. **Age >55:** 
    - Total: 2
    - High Risk: 1
    - Low Risk: 1
    - $\text{Entropy} = 1$

$ \text{Weighted Entropy for Age}  = \frac{3}{7} \times 0 + \frac{2}{7} \times 1 + \frac{2}{7} \times 1 \approx 0.57$

$ \text{Information Gain for Age} = \text{Initial Entropy} - \text{Weighted Entropy for Age} \approx 0.86 - 0.57 \approx 0.29$

### Weighted Entropy and Information Gain for Exercise

1. **Exercise = Regularly:** 
    - Total: 3
    - High Risk: 0
    - Low Risk: 3
    - $ \text{Entropy} = 0 $
    
2. **Exercise = Rarely:** 
    - Total: 4
    - High Risk: 2
    - Low Risk: 2
    - $ \text{Entropy} = 1 $

$ \text{Weighted Entropy for Exercise} = \frac{3}{7} \times 0 + \frac{3}{7} \times 1 = 0.43 $
$ \text{Information Gain for Smoker} = 0.86 - 0.43 = 0.43 $

Given the information gains for the "Smoker=No" group:

1. Age: 0.29
2. Exercise: 0.43

"Exercise" has the higher Information Gain for this group, so we will choose this as the next level node for Smoker=No.

Thus, the structure of our decision tree becomes:

1. Root node: Smoker
   - For Smoker=Yes: Split based on **Age**.
   - For Smoker-No: Split based on **Exercise**.

To determine the final classification under each branch, you would continue the process of calculating Information Gain until you reach leaves with maximum purity (i.e. all High or all Low) or until you run out of attributes to split on. 
