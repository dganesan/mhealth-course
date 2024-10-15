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

<!---
### Introduction

#### [[Introduction slides](https://drive.google.com/file/d/1j2wEaVO-UGrN5gIUIbTZGTM6q670wJwG/view?usp=drive_link)]

<iframe width="320" height="240" src="https://www.youtube.com/embed/BtvTFG5fEHE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Preliminaries: Python Basics [[html](CS328_Python_Basics.html)] [[ipynb](https://colab.research.google.com/drive/1hheScRsp3Dy-mkJ1xu-EMPPwyhMAbytN?usp=sharing#scrollTo=0uJ1tEU1CtpR)]
This notebook gives you an introduction to the main building blocks that will be useful for class including working with multidimensional arrays in [Numpy](https://numpy.org/) and visualizations using  using [Matplotlib](https://matplotlib.org/), a powerful visualization library. Open this notebook, learn about creating basic charts, and try to build some of your own. 
--->

Each of the following lessons has associated slides, videos, course notes, and Python notebooks that explain and illustrate the main concepts.

### [Chapter 1: Introduction to Smoothing and Filtering](chapter1-noise/chapter1.html)  ([Slides](https://drive.google.com/file/d/1jo4hHP76vGtyNnOeWMaLCT0mmdynV-Nd/view?usp=drive_link))
This chapter provides an introduction into the first steps in processing sensor data i.e. removing noise. The chapter describes sources of noise that present a challenge for analyzing sensor signals and describes methods to remove noise including time-domain noise removal and frequency-domain noise removal techniques. This chapter gives you the basic tools for removing noise and will help you with your first assignment which involves noise removal from accelerometer and ECG data.

### [Chapter 2: How to Design a Step Counter](chapter2-steps/chapter2.html)  ([Slides](https://drive.google.com/file/d/1Kd_HMOOB18xM1RMed2RNRpk6MaX0FaLf/view?usp=drive_link))
The second chapter provides an overview of how step counters (also referred to as pedometers) work. We look at what characteristics of steps are sufficiently distinctive to be measured accurately by a step counter. We also look at how placement of the phone or smartwatch can affect the signal, as well as other sources of error. We discuss methods to deal with these errors. This chapter will give you ideas on how to solve the assignment that asks you to design a step counter and check how it works for different sensor placements.

### [Chapter 3: Activity Recognition using Inertial Sensors](chapter3-activityrecognition/chapter3.html)  ([Slides](https://drive.google.com/file/d/11pNNJWFnmdlYtXsYdp9OkW0Fv1oyuzHO/view?usp=drive_link))
The fourth chapter describes how to design a classifer for activity recognition i.e. the task which involves identifying the physical activity a user is performing. Activity recognition is useful because it permits us to gain useful knowledge about the habits of millions of users passively—just by having them carry cell phones or wear smart watches. We describe how you can build a simple classifier to recognize if a person is sitting, standing, jogging, walking upstairs, walking downstairs or driving a car. We also look at how to collect a training dataset and measure the performance of a classifier.

### [Chapter 4: Photoplethysmography](chapter4-heartrhythm/chapter4.html)  ([Slides](https://drive.google.com/file/d/0Bw0KEeNzOgzFLWpBMnV5cHNCYzA/view?usp=sharing&resourcekey=0-wID7JSxr1I4jmcmoAzvfgw))
The third chapter describes how fitness bands/smartwatches like Fitbit and Apple Watch measure heart rate. We look at how optical heart rate monitoring sensors work, and how to extract important metrics like heart rate and breathing rate from the photoplethsmography signal. We also look at the challenges involved in estimating heart rhythm accurately at the population scale. This chapter is useful for your assignment on estimating heart rate from the PPG signal obtained when you place your finger on a smartphone camera.

### [Chapter 5: Voice-based Health Analytics](chapter5-voiceanalytics/chapter5.html) ([Slides](https://drive.google.com/file/d/0Bw0KEeNzOgzFRm13c3NqREdxTUU/view?usp=sharing&resourcekey=0-m5VIqT4c3JBhd4kykBkIPA))
Voice is an extremely useful and important part of health analytics. There are many interesting questions that can be answered with audio processing -- for example, do changes in vocal pattern indicate symptoms of an underly neurological disease? how much social interaction does a person engage in? what is the emotional content of the voice? and so on. These indicators can be leveraged for understanding depression, stress, mood, and many other factors that are relevant to personal health. In this lesson, we discuss useful voice-based features that can be used for voice-based health analytics.

### [Chapter 6: Sleep Sensing](chapter6-sleepsensing/chapter6.html) ([Slides](https://drive.google.com/file/d/1PC-8H7l06iG9JCHh6s1a29TE6jStaZMx/view?usp=sharing))
Sleep is increasingly recognized as important to public health, with sleep insufficiency linked to motor vehicle crashes, industrial disasters, and medical and other occupational errors. We discuss the importance of measuring sleep stages, and both traditional ways to measure sleep using polysomnography as well as how modern wearable devices can measure sleep and sleep stages.





