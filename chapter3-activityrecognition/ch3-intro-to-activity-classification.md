---
layout: default
title: Intro to Activity Classification
parent: Activity Recognition
grand_parent: Mobile Sensing &amp; Analytics
nav_order: 1
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


## Chapter 3: Activity Recognition using Inertial Sensors [[Slides](https://drive.google.com/file/d/0Bw0KEeNzOgzFZnhUN1p2dW1XOUk/view?usp=sharing&resourcekey=0-n1aXmftU7ipvCZAFdq0UpA)]

Let's turn to a concrete example to illustrate how activity recognition can work. Consider the case where we want to identify whether a person is sitting, standing, jogging, walking upstairs, walking downstairs or driving a car. Our hypothesis is that each of these activities involves a different “signature” that can help detect the current state of the user. For example as you saw earlier, walking and jogging should involve a series of steps with sharp peaks whereas the other activities in the list would not involve such steps. But walking may be expected to be slower than jogging, so we can distinguish between the two states.

### Detection v.s. Classification

Before proceeding further, I want to highlight a key difference between the approach that we take for the pedometer versus activity recognition. In the case of the pedometer, we had to count the number of steps, so we came up with a specialized algorithm to detect each step. This approach works for step counting, but if we had a large number of activities that we wanted to distinguish, then it would be much more time-consuming to design a specialized algorithm for each one. In other words, such a method simply would not scale.

With activity recognition, we take a more general approach where we assume that we don’t know the distinguishing characteristics of each class (walking, sitting, etc) ahead of time. We simply want to provide some sample datasets of each class (called training data), and some large set of possible characteristics of the data that might be important (called features), and then let an automated algorithm identify what features are most useful to distinguish between the classes.

Let us make this distinction more concrete with an example. Consider three classes that we want to distinguish: Walking (W), Sitting (S), and Other (O). The first step in designing a classifier is to obtain some labeled datasets for these three classes - in other words, we might get several volunteers to have a phone in their pocket and provide 30 seconds of raw accelerometer data when they were engaged in each of the activities (i.e. 30 seconds of walking, 30 seconds of sitting, and 30 seconds of a few other activities). The second step is to decide on a bag of features to provide to the classifier - these features may or may not be important for distinguishing between the classes, but they provide a comprehensive set of possibilities to try. These features could be averages or standard deviations over a window, features that extract periodic patterns in the data, features that extract peak acceleration changes, and so on. Note that we don’t know which of these features are important - we hope that some combination of them would be sufficient to distinguish the classes. Once we do all this, we use a classification algorithm, and provide the features + training data. The classifier tries to learn which features are most important to distinguish between the classes. Once we have such a classifier, we can apply it to new datasets and evaluate its performance.

Having provided a birds eye view of classification, let us turn to a step-by-step exploration of the data collection and processing pipeline. 

### Labeled data collection

The first step in designing any mobile health sensing algorithm is labeled data collection. In other words, you want to collect data from a set of users (preferably large) while performing certain everyday activities that you want to distinguish. By labels, we mean that the ground truth corresponding to the raw data must be available. For example, we might want an hour of the raw accelerometer data from a phone, as well as user-provided labels regarding their state (walking, running, etc). This data is referred to as a training dataset, and this is the data that we are going to use to develop our classification algorithm. 

While obtaining labeled data, make sure to collect sufficient data for each of the categories that you want to classify. For example, if you want to classify walking, ascending or descending stairs, sitting, and standing, then try to collect about 10 instances of each of these classes from each user, where each activity may be about 10-30 seconds long. You may also want to collect data while carrying the phone in different orientations, to make sure that your algorithms are less sensitive to orientation variations.

In this class, we will use the freely available Sensor Logger app supported for Android and iPhone  to create your own labeled datasets. (https://github.com/tszheichoi/awesome-sensor-logger)

For example, if you are collecting data about four activities - sitting, standing, walking and jogging. Once you select your activities, you can use the app to collect accelerometer data.

1. For each of the activities you choose to classify,  toggle “Accelerometer” on the “Logger” tab and click “Start Recording”. (You can turn off the “HTTP Data Push” during the data collection.) Click “Stop Recording” once finished.
2. Collect at least 5 minutes of data for each activity (more is better). Make sure that you have collected data for all activities for a roughly equal length of time. Each activity can be multiple recording sessions (Start -> Stop), but each session be only one activity. You should name your session in the “Recordings” tab. (Click the recording, then click “Rename” to assign “walking”, “sitting” and etc.)
3. Once you have collected all the data, you can either click “Select” on the “Recordings” tab or export each recording individually. When exporting, choose “Zipped CSV” which will contain all data in CSV format.

### Visualizing Common Activities 

For the purpose of this document, we consider six activities: walking, jogging, ascending stairs, descending stairs, sitting, and standing. We selected these activities because they are performed regularly by many people in their daily routines. The activities also involve motions that often occur for substantial time periods, thus making them easier to recognize. Furthermore, most of these activities involve repetitive motions and hopefully this should also make the activities easier to recognize.

To aid in recognition, it's crucial to understand the directional sensitivity of accelerometers:
- X-Axis: Captures horizontal movement of the user’s leg.
- Y-Axis: Reflects upward and downward motion.
- Z-Axis: Represents the forward movement of the leg.

It's worth noting that the Y-values typically have the most significant accelerations across activities. This prevalence is attributed to Earth’s gravitational pull, which leads to a consistent 9.8 m/s^2 acceleration in the direction of the Earth’s center. For all activities, barring sitting, this direction predominantly aligns with the Y-axis.

Figure 1 plots the accelerometer data for a typical user, for all three axes and for each of the six activities. 

It is clear that sitting and standing do not exhibit periodic behavior but do have distinctive patterns, based on the relative magnitudes of the x, y, and z, values, while the four other activities (Figure 1 a-d), which involve repetitive motions, do exhibit periodic behavior. 

The periodic patterns for walking, jogging, ascending stairs, and descending stairs can be described in terms of the time between peaks and by the relative magnitudes of the acceleration values. The plot for walking demonstrates a series of high peaks for the y-axis, spaced out at approximately ½ second intervals. The peaks for the z-axis acceleration data echo these peaks but with a lower magnitude. The distance between the peaks of the z-axis and y-axis data represent the time of one stride. The x-axis values (side to side) have an even lower magnitude but nonetheless mimic the peaks associated with the other axes. For jogging, similar trends are  seen for the z-axis and y-axis data, but the time between peaks is less (~¼ second), as one would expect. The range of y-axis acceleration values for jogging is greater than for  walking, although the shift is more noticeable in the negative direction. For descending stairs, one observes a series of small peaks for y axis acceleration that take place every ~½ second. Each small peak represents movement down a single stair. The z-axis values show a similar trend with negative acceleration, reflecting the regular movement down each stair. The x-axis data shows a series of semi-regular small peaks, with acceleration vacillating again between positive and negative values. For ascending stairs, there are a series of regular peaks for the z-axis data and y-axis data as well; these are spaced approximately ~¾ seconds apart, reflecting the longer time it takes to climb up stairs. 

As one would expect, sitting and standing do not exhibit any regular periodic behavior and all of the acceleration values are relatively constant. As mentioned earlier, the primary differences between these activities is the relative magnitudes of values for each axis, due to the different orientations of the device with respect to the Earth when the user is sitting and standing Thus it appears easy to differentiate between sitting and standing, even though neither involves much movement. 

<p float="left">
  <img src="images/walking.png" alt="drawing" width="500"/>
  <img src="images/jogging.png" alt="drawing" width="500"/>
  <img src="images/upstairs.png" alt="drawing" width="500"/>
  <img src="images/downstairs.png" alt="drawing" width="500"/>
  <img src="images/sitting.png" alt="drawing" width="500"/>
  <img src="images/standing.png" alt="drawing" width="500"/>
</p>

<!---
<p float="left">
  <img src="images/image2.png" alt="drawing" width="500"/>
  <img src="images/image4.png" alt="drawing" width="500"/>
  <img src="images/image5.png" alt="drawing" width="500"/>
</p>
--->
_Figure 1: Accelerometer data for common activities corresponding to one individual (data from [2])_

Having looked at the data for the activities that we want to distinguish, let's turn our attention back to designing the classifier that will automatically determine user state.

