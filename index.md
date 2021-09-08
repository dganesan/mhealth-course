---
layout: default
title: Mobile Sensing &amp; Analytics
nav_order: 1
has_children: true
usemathjax: true
description: "CS328"
---
## Mobile Health Sensing and Analytics
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}
---

## CS328: Mobile Health Sensing and Analytics

Fitness gadgets such as ​Fitbit​, ​Apple Watch,​ ​Android Wear,​ and smartphone apps such as ​RunKeeper​ and M​oves​ calculate activity patterns, calories burned each day, track sleep patterns, and compute heart rate. We will learn how to build the computational elements for developing such applications by leveraging various sensors on smartphones, including the accelerometer, camera, microphone, and GPS. This is a hands-on course where students learn by doing! 

Each of these lessons has associated slides, videos, course notes, and Python notebooks that explain and illustrate the main concepts.

#### Preliminaries: Python Basics [[html](CS328_Python_Basics.html)] [[ipynb](https://colab.research.google.com/drive/1hheScRsp3Dy-mkJ1xu-EMPPwyhMAbytN?usp=sharing#scrollTo=0uJ1tEU1CtpR)]
This notebook gives you an introduction to the main building blocks that will be useful for class including working with multidimensional arrays in [Numpy](https://numpy.org/) and visualizations using  using [Matplotlib](https://matplotlib.org/), a powerful visualization library. Open this notebook, learn about creating basic charts, and try to build some of your own. 

#### [Lesson 1: Introduction to Smoothing and Filtering](chapter1-noise/chapter1.md)
This lesson provides an introduction into the first steps in processing sensor data i.e. removing noise. The lesson describes sources of noise that present a challenge for analyzing sensor signals and describes methods to remove noise including time-domain noise removal and frequency-domain noise removal techniques.

#### [Lesson 2: How to Design a Step Counter](chapter2-steps/chapter2.md)
The second lesson provides an overview of how step counters (also referred to as pedometers) work. We look at what characteristics of steps are sufficiently distinctive to be measured accurately by a step counter. We also look at how placement of the phone or smartwatch can affect the signal, as well as other sources of error. We discuss methods to deal with these errors. 

#### [Lesson 3: Activity Recognition using Inertial Sensors](chapter3-activityrecognition/chapter3.md)

#### [Lesson 4: Evaluating Classifier Performance](chapter4-evalclassifier/chapter4.md)



