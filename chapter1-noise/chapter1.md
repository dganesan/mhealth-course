---
layout: default
title: Data Smoothing
nav_order: 1
parent: Mobile Sensing &amp; Analytics
has_children: true
usemathjax: true
description: "Smoothing and Filtering"
---
## Data Smoothing and Filtering
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}
---

## Chapter 1: Sensor data smoothing and filtering

Most sensor data is affected to some extent by **noise**, that is unexplained variations in the data that in many cases is uninterpretable, and in almost all cases is not of interest to us. Data analysis is often considerably simpler if this noise can be removed from the data. This chapter provides an overview of the sources of noise in typical sensor data and the methods by which noise can be removed.

<iframe width="320" height="240" src="https://www.youtube.com/embed/SV2ShtHPuKM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Part 1: Introduction to Smoothing and Filtering [[notes](ch1-intro.html)] [[slides](https://drive.google.com/file/d/1jo4hHP76vGtyNnOeWMaLCT0mmdynV-Nd/view?usp=drive_link)]
We start by explaining the difference between information and noise, and describe what causes noise in sensor data. We then show different examples of noisy signals and what are some common sources of noise in these signals.

<!---
<iframe width="320" height="240" src="https://www.youtube.com/embed/4TI_h2Ad6AM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="320" height="240" src="https://www.youtube.com/embed/Pq3ganioUzU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
--->

### Part 2: Time-series Smoothing and Filtering [[notes](ch1-timedomainfiltering.html)] [[slides](https://drive.google.com/file/d/1jo4hHP76vGtyNnOeWMaLCT0mmdynV-Nd/view?usp=drive_link)]
Noise removal techniques can be divided into two class. The first is time-domain approaches, where the information is contained in the amplitude of a signal. For example, you may be interested in the temperature of this room, the orientation of your phone, your location and driving trajectory, and so on. All of these contain information in the time domain.

<!---
<iframe width="320" height="240" src="https://www.youtube.com/embed/i9wRUw_X2XM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
--->

### Part 3: Frequency-domain  Filtering [[notes](ch1-freqdomainfiltering.html)] [[slides](https://drive.google.com/file/d/1jo4hHP76vGtyNnOeWMaLCT0mmdynV-Nd/view?usp=drive_link)]
The second is frequency-domain approaches, which removes noise that is periodic in nature. For example, accelerometer readings when you walk show periodic motion and your heart beats in a quasi-periodic manner. Many noise sources are similarly periodic and can be removed using frequency domain filtering methods.

<!---
<iframe width="320" height="240" src="https://www.youtube.com/embed/B7T7Yj4XdhI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
--->

### Notebook 1: Time Domain Noise Removal [[html](notebooks/Chapter1-TimeDomainNoiseRemoval.html)] [[ipynb](notebooks/Chapter1-TimeDomainNoiseRemoval.ipynb)]
This notebook shows a few examples of time-series signals and how different time-domain smoothing methods (moving average, exponentially weighted moving average, and median filtering) work on this data. 

### Notebook 2: Frequency Domain Noise Removal [[html](notebooks/Chapter1-FreqDomainNoiseRemoval.html)] [[ipynb](notebooks/Chapter1-FreqDomainNoiseRemoval.ipynb)]
This notebook shows a few examples of time-series signals and how different frequency-domain noise removal methods (low-pass, high-pass, and notch filter) work on this data. 

### Notebook 3: Fourier Decomposition [[html](Chapter1-Fourier-Denoising.html)] [[ipynb](Chapter1-Fourier-Denoising.ipynb)]
The Fourier transform is a tool that allows you to take a signal and see the power of each frequency in it. This example notebook shows how you can remove frequency-domain noise from a signal using a fourier transform.

<!---
<iframe width="320" height="240" src="https://www.youtube.com/embed/v1rEPYGzZ-c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
--->

### Notebook 4: Butterworth Filtering [[html](Chapter1-ButterworthFilter.html)] [[ipynb](Chapter1-ButterworthFilter.ipynb)]
Frequency-domain noise can be removed by a combination of frequency filters. A low-pass filter can remove high frequency components while letting through low frequency components. A high pass filter does the reverse and lets high frequency components through while removing low frequency components. A notch filter removes a specific frequency from the signal. In this notebook, we show how to use a filter called a 'butterworth filter' to remove noise. A Butterworth filter is a popular frequency domain 'lowpass' filter that can remove high frequency noise while only letting the low frequencies through. Since many signals we deal with such as steps, heartbeats and breathing are low frequency signals i.e. only a few repetitions per minute, this is a good approach.

<!---
<iframe width="320" height="240" src="https://www.youtube.com/embed/O68PSIXEU9Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
--->

<!---

#### Notebook 4: Sampling Rate and Nyquist [[html](Chapter1-SamplingRate.html)] [[ipynb](Chapter1-SamplingRate.ipynb)]
Signals in the real world are continuous but need to be sampled at a particular rate for a computer to process the signal. This example notebook shows the relationship between sampling rate and the ability to reconstruct a signal. 

#### Notebook 6: 3D Trajectory Estimation [[html](Chapter1-3D-Trajectory-Smoothing.html)] [[ipynb](Chapter1-3D-Trajectory-Smoothing.ipynb)]
This is a more advanced example that shows how to use an inertial sensor (accelerometer, gyroscope, magnetometer) to track the trajectory of a smartphone in 3D space. The mathematical aspects are more complicated here and you will not learnt it in this class although this can be interesting for potential course projects.

--->

