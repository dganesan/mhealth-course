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

### Introduction

#### [[Introduction slides](https://goo.gl/ftTBJR)]

<iframe width="320" height="240" src="https://www.youtube.com/embed/BtvTFG5fEHE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Preliminaries: Python Basics [[html](CS328_Python_Basics.html)] [[ipynb](https://colab.research.google.com/drive/1hheScRsp3Dy-mkJ1xu-EMPPwyhMAbytN?usp=sharing#scrollTo=0uJ1tEU1CtpR)]
This notebook gives you an introduction to the main building blocks that will be useful for class including working with multidimensional arrays in [Numpy](https://numpy.org/) and visualizations using  using [Matplotlib](https://matplotlib.org/), a powerful visualization library. Open this notebook, learn about creating basic charts, and try to build some of your own. 

### Lessons

Each of the following lessons has associated slides, videos, course notes, and Python notebooks that explain and illustrate the main concepts.

#### [Lesson 1: Introduction to Smoothing and Filtering](chapter1-noise/chapter1.html)
This lesson provides an introduction into the first steps in processing sensor data i.e. removing noise. The lesson describes sources of noise that present a challenge for analyzing sensor signals and describes methods to remove noise including time-domain noise removal and frequency-domain noise removal techniques. This lesson gives you the basic tools for removing noise and will help you with your first assignment which involves noise removal from accelerometer and ECG data.

#### [Lesson 2: How to Design a Step Counter](chapter2-steps/chapter2.html)
The second lesson provides an overview of how step counters (also referred to as pedometers) work. We look at what characteristics of steps are sufficiently distinctive to be measured accurately by a step counter. We also look at how placement of the phone or smartwatch can affect the signal, as well as other sources of error. We discuss methods to deal with these errors. This lesson will give you ideas on how to solve the assignment that asks you to design a step counter and check how it works for different sensor placements.

#### [Lesson 3: Photoplethysmography](chapter4-heartrhythm/chapter4.html)
The third lesson describes how fitness bands/smartwatches like Fitbit and Apple Watch measure heart rate. We look at how optical heart rate monitoring sensors work, and how to extract important metrics like heart rate and breathing rate from the photoplethsmography signal. We also look at the challenges involved in estimating heart rhythm accurately at the population scale. This lesson is useful for your assignment on estimating heart rate from the PPG signal obtained when you place your finger on a smartphone camera.

#### [Lesson 4: Activity Recognition using Inertial Sensors](chapter3-activityrecognition/chapter3.html)

#### [Lesson 5: Evaluating Classifier Performance](chapter4-evalclassifier/chapter4.html)



