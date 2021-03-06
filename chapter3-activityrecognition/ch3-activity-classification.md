---
layout: default
title: Activity Classification with a Decision Tree
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

Having provided a birds eye view of classification, let us turn to a step-by-step exploration of the data collection and processing pipeline. My goal is not to teach you the mathematical underpinnings of classification (courses like Artificial Intelligence and Machine Learning cover this in more detail); rather, my objective is to convey how these techniques can be used in practice so that you get an appreciation of them. 


### Labeled data collection

The first step in designing any mobile health sensing algorithm is labeled data collection. In other words, you want to collect data from a set of users (preferably large) while performing certain everyday activities that you want to distinguish. By labels, we mean that the ground truth corresponding to the raw data must be available. For example, we might want an hour of the raw accelerometer data from a phone, as well as user-provided labels regarding their state (walking, running, etc). This data is referred to as a training dataset, and this is the data that we are going to use to develop our classification algorithm. 

While obtaining labeled data, make sure to collect sufficient data for each of the categories that you want to classify. For example, if you want to classify walking, ascending or descending stairs, sitting, and standing, then try to collect about 10 instances of each of these classes from each user, where each activity may be about 10-30 seconds long. You may also want to collect data while carrying the phone in different orientations, to make sure that your algorithms are less sensitive to orientation variations.

In many cases, you will have to go through an IRB (Institutional Review Board) since the study involves “experimenting” on human subjects and there is some risk of harm (e.g., the subject could trip while jogging or climbing stairs). But if you are just trying it out on yourself for the purpose of the course, then there is no need to go through an IRB. This is the approach we will take.


### Visualizing Common Activities 

For the purpose of this document, we consider six activities: walking, jogging, ascending stairs, descending stairs, sitting, and standing. We selected these activities because they are performed regularly by many people in their daily routines. The activities also involve motions that often occur for substantial time periods, thus making them easier to recognize. Furthermore, most of these activities involve repetitive motions and hopefully this should also make the activities easier to recognize. We will assume that the z-axis captures the forward movement of the leg and the y-axis captures the upward and downward motion. The x-axis captures horizontal movement of the user’s leg. Figure 1 demonstrates these axes relative to a user. 

Figure 1 plots the accelerometer data for a typical user, for all three axes and for each of the six activities. It is clear that sitting and standing (Figure 1 e,f) do not exhibit periodic behavior but do 

have distinctive patterns, based on the relative magnitudes of the x, y, and z, values, while the four other activities (Figure 1 a-d), which involve repetitive motions, do exhibit periodic behavior. Note that for most activities the y values have the largest accelerations. This is a consequence of Earth’s gravitational pull, which causes the accelerometer to measure a value of 9.8 m/s2 in the direction of the Earth’s center. For all activities except sitting this direction corresponds to the y axis.

The periodic patterns for walking, jogging, ascending stairs, and descending stairs (Figure 1a-d) can be described in terms of the time between peaks and by the relative magnitudes of the acceleration values. The plot for walking, shown in Figure 1a, demonstrates a series of high peaks for the y-axis, spaced out at approximately ½ second intervals. The peaks for the z-axis acceleration data echo these peaks but with a lower magnitude. The distance between the peaks of the z-axis and y-axis data represent the time of one stride. The x-axis values (side to side) have an even lower magnitude but nonetheless mimic the peaks associated with the other axes. For jogging, similar trends are  seen for the z-axis and y-axis data, but the time between peaks is less (~¼ second), as one would expect. As one might expect, the range of y-axis acceleration values for jogging is greater than for  walking, although the shift is more noticeable in the negative direction. For descending stairs, one observes a series of small peaks for y axis acceleration that take place every ~½ second. Each small peak represents movement down a single stair. The z-axis values show a similar trend with negative acceleration, reflecting the regular movement down each stair. The x-axis data shows a series of semi-regular small peaks, with acceleration vacillating again between positive and negative values. For ascending stairs, there are a series of regular peaks for the z-axis data and y-axis data as well; these are spaced approximately ~¾ seconds apart, reflecting the longer time it takes to climb up stairs. 

As one would expect, sitting and standing do not exhibit any regular periodic behavior and all of the acceleration values are relatively constant. As mentioned earlier, the primary differences between these activities is the relative magnitudes of values for each axis, due to the different orientations of the device with respect to the Earth when the user is sitting and standing Thus it appears easy to differentiate between sitting and standing, even though neither involves much movement. 

<p float="left">
  <img src="images/image2.png" alt="drawing" width="500"/>
  <img src="images/image4.png" alt="drawing" width="500"/>
  <img src="images/image5.png" alt="drawing" width="500"/>
</p>

_Figure 1: Accelerometer data for common activities corresponding to one individual (data from [2])_

Having looked at the data for the activities that we want to distinguish, let's turn our attention back to designing the classifier that will automatically determine user state.


### Feature Generation & Data Transformation 

One of the crucial steps in classifying sensor data is identifying distinguishing features in the data. Some of these features are aggregate statistics of the data such as average and standard deviations. Other features capture frequency of patterns in the data - for example, steps occur with a certain frequency, and the frequency changes whether you are walking vs running. If we can capture such frequency information, it can be a valuable feature for classification. There are numerous features that could be useful, and often the feature generation process is the most time-consuming part of writing a classification system.

We have pre-generated several informative features that you can apply to the raw accelerometer readings, and a list of some of these features are provided below. As shown in the table, its useful to divide features into two classes - time domain features and frequency domain features. In this chapter, I will focus on providing an intuitive  understanding of the different features and why they might be useful for distinguishing between the classes. For a more mathematical explanation, refer to [1] and [2].

**Time domain features:** The time-domain features are some statistical measures that you can extract from a window of samples (say 100 samples). Some of these are intuitive - for example, the mean is just an average of the acceleration over a window of samples. The median, as you know, is the number that you get if you sorted the acceleration values in the window and took the middle value. Standard deviation captures how much the acceleration varies from sample to sample, and so on. 

*Examples of time domain features: Mean, Median, Variance, Standard deviation, Min, Max, Range, Zero-crossings, Angle, Angular velocity.*

Figure 1 suggests why these features may be useful - for example, sitting and standing (e and f) have very low standard deviation since it's almost flat, whereas all other cases have high standard deviation. Therefore, the standard deviation feature can be useful to distinguish between these two cases and the rest. But how can we separate sitting from standing? The mean feature offers a solution - you can see that the mean for each axis is closer together in (e) than in (f), which suggests that this could be a useful feature. 

Some of the time-domain features are not so intuitive, but you are already familiar with at least one of these from the pedometer case study. Recall that in the pedometer case study, you had a dynamic threshold, and measured each time the signal crossed from above to below the threshold with a high slope. This is a crossing of the threshold (zero axis). So, counting the number of such crossings in a time window provides another useful feature.

**Frequency domain features:** This class of features represents information about periodic patterns and rhythmic behavior in the signal. Again, you saw such features in the pedometer case study, where you were asked to look for a periodic pattern in the walking signal. This is exactly the type of information that we are looking to extract, but by leveraging some more powerful methods. 

While the methods themselves are outside the scope of our review, the features are important to understand. The dominant frequency feature corresponds to the most significant rhythmic component in the data. For example, in the case of the walking traces, this would be the steps, with a period of roughly ½ second per step. The signal energy is another way of looking at the amount of variation in the accelerometer data - the larger its periodic components, the more the signal energy. There are other such frequency domain features, but these two are sufficient for our needs.

*Examples of frequency domain features: Dominant frequency, Signal Energy.*


The figure below shows an example for walking on a treadmill. You can see that there seem to be a few dominant frequencies, and some of them are harmonics of the frequency of the walking. But the dominant frequencies give you sufficient information about the periodicity of walking.

 <img src="images/image3.png" alt="drawing" width="500"/>

_Figure 2: Energy in different frequency bands for accelerometer data collected during walking_


### Decision tree classifier

Once we extract different features from the data, it's time to build our classifier. At a high level, the goal of a classifier is to identify which of the above features that you obtained from your raw data is most useful in distinguishing between the different activities that you want to classify. There are many different classifiers, and an exhaustive summary would take too much time. But let me try to introduce one such classifier to provide an intuition for how such a method would work.

**What is a decision tree?** One of the most commonly used classifiers is a decision tree. The idea is simple and best explained with an example. Suppose you had the following six features - means along each of the x, y, z axes, and standard deviations along each of these axes. Given these features, you want to distinguish between standing, sitting, walking, running, biking, and driving. The key question is which of these features is most useful to distinguish between these activities. 

**How does a decision tree work? **The idea behind a decision tree is to view this problem in a hierarchical manner. First, let us assume that we already constructed a decision tree (see figure above), and just try to understand how to use it, and what its telling us. In the above figure, the root node makes a decision on whether meanX &lt; 8.48 (this number is not important for now, focus on the concept). If true, then the decision is to take the right branch, and if false, take the left branch. Say we took the right branch - then we look at another decision, say checking if stddevX &lt; 11.36. Similarly, this decision tree proceeds by checking one feature after another until we finally get to the leaf node that tells us what our current state is. So, the process of using a decision tree to classify the current activity seems intuitive - its just a sequence of if-then-else statements with each statement checking the values of one or more parameters. But what does each of these branches really mean? What separates the left branch and the right branch?

<img src="images/image1.png" alt="drawing" width="500"/>
	
_Figure 3: Example of a decision tree_

**Decision tree with an example.** Let us look at an example of a decision tree and try to interpret its meaning. The root node separates {sitting, standing, driving} on the left branch from {biking, walking, running} on the right branch. Clearly, this node is identifying some feature that separates between more sedentary activities from the more active ones. This makes sense - if we had to think of an algorithm, we would perhaps do the same thing. Let's now look at the decision nodes at the next level down starting with the left branch. This node separates driving from other sedentary activities (sitting, standing) by looking at the standard deviation of the Z axis. This seems to make sense as well - driving will cause lots of vibrations due to the car and the road, whereas we are unlikely to see these vibrations when you are sitting on a chair or standing (unless there’s an earthquake!). The corresponding decision node on the right branch seems to be doing something similar - it uses standard deviation on the vertical axis to distinguish between biking, and other physical activities such as running and walking. The intuition is that biking on the road is likely to have small vibrations because of the road whereas running or walking has large variations due to acceleration changes for each step (as you observed in the pedometer case study). The remaining decision nodes in the left branch no longer use the standard deviation, and only use the mean to separate sitting and standing. This is easiest to understand from Figure 1 where we saw the raw accelerometer signal for sitting and standing. Both are flat, so there’s little to be gained from looking at standard deviation, but they have different averages, so this is the most useful feature for separating the classes. On the right branch, walking vs running uses the difference in standard deviations between these two - intuition would suggest that running has more vibrations than walking. In summary, a decision tree works by identifying which features best separate the categories, and builds it as a tree structure. 

Perhaps a simpler approach to understand how a decision tree works is to view it as a series of questions. Consider a game where your friend has chosen an activity class, and you need to guess it. You are allowed a sequence of questions, each of which could be about some characteristic about the classes. What is the minimal number of questions you might ask? In this example, the first question you might as is: Is the user in a sedentary or active state? If the answer is “active”, you might ask further questions to refine the state. The  decision tree can be viewed as learning the best sequence of questions given the data and its characteristics.

**How to build the decision tree?** We now understand how a decision tree works but how do we build the decision tree in the first place. There are several algorithms for this purpose, and we describe one of the more popular ones (C4.5). The idea is that at each node of the tree, choose the attribute of the data that most effectively splits its set of samples into subsets enriched in one class or the other. The splitting criterion is referred to as [information gain](http://en.wikipedia.org/wiki/Information_gain), which is a metric for describing how separation you have achieved between the right and left branches after the split compared to before the split. The algorithm now works as follows:

**Pseudocode.** In pseudocode, the general algorithm for building decision trees is:

1. For each attribute _a_, find the normalized information gain from splitting on _a_
2. Let _a_best_ be the attribute with the highest normalized information gain
3. Create a decision node that splits on _a_best_
4. Recurse on the sublists obtained by splitting on _a_best_, and add those nodes as children of node

A great overview of how decision trees work is in [3]. You can ignore the Gini index and the Classification error measures - we will focus on the Entropy measure. You can ignore parts of the chapter that are not discussed in class.

While the process of building the decision tree is useful to understand, you will not be asked to write the code for this algorithm. Thankfully, there are software packages that do this for you.


### References

1. [Preprocessing Techniques for Context Recognition from Accelerometer Data](http://web.ist.utl.pt/diogo.ferreira/papers/figo10preprocessing.pdf), Davide Figo,_ _Pedro C. Diniz,_ _Diogo R. Ferreira,_ _Jo˜ao M. P. Cardoso

2. [Feature Learning for Activity Recognition in Ubiquitous Computing](http://ijcai.org/papers11/Papers/IJCAI11-290.pdf),Thomas Plotz, Nils Y. Hammerla, and Patrick Olivier, IJCAI 2011

3. [Classification: Basic Concepts, Decision Trees, and Model Evaluation](http://www-users.cs.umn.edu/~kumar/dmbook/ch4.pdf), Pang-Ning Tan, Michigan State University,  Michael Steinbach, University of Minnesota, Vipin Kumar, University of Minnesota

