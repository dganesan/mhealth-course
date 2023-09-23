---
layout: default
title: Activity Classification with a Decision Tree
parent: Activity Recognition
grand_parent: Mobile Sensing &amp; Analytics
nav_order: 4
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

