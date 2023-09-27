---
layout: default
title: Activity Recognition
nav_order: 3
parent: Mobile Sensing &amp; Analytics
has_children: true
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


## Chapter 3: Activity Recognition using Inertial Sensors [[Slides](https://drive.google.com/file/d/1qfVTzDZgv0Lk49Z2MUrz-yQPi1wBF5xX/view?usp=drive_link)]

Having discussed the design of a pedometer that uses an accelerometer, let us now turn to the problem of activity recognition,  a task which involves identifying the physical activity a user is performing. Activity recognition is useful because it permits us to gain useful knowledge about the habits of millions of users passively—just by having them carry cell phones in their pockets. Such techniques can have a wide range of applications, including automatic customization of the mobile device’s behavior based upon a user’s activity (e.g., sending calls directly to voicemail if a user is jogging) and generating a daily/weekly activity profile to determine if a user is performing a healthy amount of exercise.

#### Part 1: Activity classification vs Step counting [[notes](ch3-detection-vs-classification.html)]
We describe the difference between detection and classification, and provide an overview of a classification pipeline. We start with how to collect labeled data, and visualize the signal for a variety of common activities like walking, jogging, walking upstairs, walking downstairs, sitting and standing.

#### Part 2: Visualizing accelerometer signals for common activities  [[notes](ch3-visualizing-activities.html)]
We now visualize the accelerometer signal for a variety of common activities like walking, jogging, walking upstairs, walking downstairs, sitting and standing. This will help us get an intuitive feel for how the accelerometer signal differs for different activities.

#### Part 3: Time-domain features for classification [[notes](ch3-time-domain-features.html)]
One of the crucial steps in classifying sensor data is identifying distinguishing features in the data. Some of these features are time-domain statistics of the data such as average and standard deviations. We describe some commonly used features.

#### Part 4: Frequency-domain features for classification [[notes](ch3-freq-domain-features.html)]
Another important class of features is frequency domain features. We describe some basic frequency domain features.

#### Part 5: Decision tree classification [[notes](ch3-decision-tree.html)]
We start by explaining how to perform activity classification using a decision tree.

#### Part 5: Evaluating Classifier Performance [[notes](ch3-classifier-performance.html)]
We look at how to evaluate classifier performance.

