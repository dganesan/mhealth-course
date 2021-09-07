---
layout: default
title: Chapter 1
nav_order: 1
has_children: true
usemathjax: true
description: "Chapter 1"
---

Most sensor data is affected to some extent by **noise**, that is unexplained variations in the data that in many cases is uninterpretable, and in almost all cases is not of interest to us. Data analysis is often considerably simpler if this noise can be removed from the data. This chapter provides an overview of the sources of noise in typical sensor data and the methods by which noise can be removed.

#### [Part 1: Introduction to Smoothing and Filtering](ch1-intro.md) 
We start by explaining the difference between information and noise, and describe what causes noise in sensor data. We then show different examples of noisy signals and what are some common sources of noise in these signals.

<iframe width="320" height="240" src="https://www.youtube.com/embed/4TI_h2Ad6AM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="320" height="240" src="https://www.youtube.com/embed/Pq3ganioUzU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### [Part 2: Time-series Smoothing and Filtering](ch1-timedomainfiltering.md) 
Noise removal techniques can be divided into two class. The first is time-domain approaches, where the information is contained in the amplitude of a signal. For example, you may be interested in the temperature of this room, the orientation of your phone, your location and driving trajectory, and so on. All of these contain information in the time domain.

<iframe width="560" height="315" src="https://www.youtube.com/embed/i9wRUw_X2XM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### [Part 3: Frequency-domain  Filtering](ch1-freqdomainfiltering.md) 
The second is frequency-domain approaches, which removes noise that is periodic in nature. For example, accelerometer readings when you walk show periodic motion and your heart beats in a quasi-periodic manner. Many noise sources are similarly periodic and can be removed using frequency domain filtering methods.

<iframe width="560" height="315" src="https://www.youtube.com/embed/B7T7Yj4XdhI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Example 1: Accelerometer Data Smoothing (Assignment 1)

#### Example 2: ECG Data Filtering (Assignment 1)

#### Example 3: [Fourier Decomposition](Chapter1-Fourier-Denoising.html)
<iframe width="560" height="315" src="https://www.youtube.com/embed/v1rEPYGzZ-c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Example 3: [Butterworth Filtering](Chapter1-ButterworthFilter.html)
<iframe width="560" height="315" src="https://www.youtube.com/embed/O68PSIXEU9Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Example 4: [3D Trajectory Estimation](Chapter1-3D-Trajectory-Smoothing.html)
