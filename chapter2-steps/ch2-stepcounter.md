---
layout: default
title: Step Detection Algorithm
parent: Step Counting
grand_parent: Mobile Sensing &amp; Analytics
nav_order: 2
usemathjax: true
description: "Chapter 2"
---
## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}
---

## Step Detection Algorithm

There are many different ways that we can design a step detection algorithm. We outline one such method in this section. The key insight in our method is to convert the 3-axis signal into a one axis magnitude signal, and then extract steps from this signal.

<img src="images/image12.png" alt="drawing" width="600"/>

_Figure 5: Step Detection Algorithm_

**Step 1: Extract signal magnitude**: In the previously described algorithm, we selected the axis along which maximum acceleration occurred and focused on that one. Here, we are just going to take the magnitude of the entire acceleration vector i.e. 

<img src="images/image1.png" alt="drawing" width="100"/>

, where x, y, and z are the readings of the accelerometer along the three axes. 

<img src="images/image5.png" alt="drawing" width="600"/>

_Figure 6: Example showing sources of noise in magnitude signal_

**Step 2: Filter the signal to remove noise**: The second step is to remove noise, and extract the specific signal corresponding to walking. Before we perform this step, we need to know what are the sources of noise. There are several sources of noise that we need to filter out (shown in Figure 6):


* **Jumpy peaks**: Since the phone is often carried in a pocket/purse, it can jiggle a little with each step. Also, some users have a bounce in their step, so even though they are taking a single step, the phone can bounce multiple times within this step. 
* **Short peaks**: Small peaks can occur when a user is using a phone (e.g. making a call or using an app).
* **Slow peaks**: Slow peaks can occur when the phone is moved or due to movements of the leg while sitting (if the phone is in the pant pocket)

To remove these sources of noise, we are going to use frequency-domain noise removal. Notice that we need to remove high frequency variations like jumpy peaks and low frequency variations like slow peaks. A simple solution is to use a filter that keeps only frequencies relating to walking and removes the rest. For example, we know that typical walking pace may be under three steps a second (3 Hz) and over half step a second (0.5Hz), so perhaps we remove all frequencies above 5 Hz and below 0.5 Hz (just to give some margin for error). Note that this method would not be able to detect running or bicycling, which may have higher pace. 

Even after we remove low and high frequency peaks, we may be left with some short peaks. A simple way to deal with this is to look only for large peaks and ignore small peaks.


<p float="left">
<img src="images/image6.png" alt="drawing" width="500"/>
<img src="images/image10.png" alt="drawing" width="500"/>
</p>

_Figure 7: Zero crossings (left) and peaks (right) of the filtered magnitude signal_

**Step 3: Detecting Steps.** Once you have the smoothed data, let us consider how to detect the step. There are many approaches to do this. We could do what was suggested earlier, which is to look for large peaks and use that to detect steps. Another approach is to take the derivative (slope) of the smoothed acceleration signal. The derivative changes from negative to positive (or positive to negative) exactly when a step occurs, so you can just count the number of times the derivative changed from negative to positive to detect the number of steps that occurred.  Another possibility is to subtract the mean for each window and look at  zero crossings i.e. times when the signal crosses from the negative to positive in the upward direction (this can be tricky, however, since the signal baseline can change over time as shown below). 

We will focus on detecting peaks using Python and tuning parameters to make it work effectively.

## Implementing Step Counting in Python

Step counting, at its core, is about detecting repeating patterns or peaks in acceleration data that correspond to an individual's steps. In Python, the `scipy` library provides the `find_peaks` function that serves precisely this purpose, allowing us to detect peaks in our dataset easily.

### The `find_peaks` Function

The `find_peaks` function from the `scipy.signal` module is designed to identify the indices of relative maxima (peaks) in a 1D array. Its basic syntax is:

```python
from scipy.signal import find_peaks

peaks, properties = find_peaks(data_array, prominence=prom, width=wid)
```

In this function:

- `data_array` is the 1D array or dataset where we want to identify peaks.
- `prominence` is a parameter that defines how much a peak stands out relative to its surrounding data points, effectively describing the peak's height.
- `width` is a parameter that specifies the width of the peaks.

In our step counting context:

```python
peaks, _ = find_peaks(df['accel_mag'], prominence=prom, width=wid)
num_steps = len(peaks)
```

We're identifying peaks in the `accel_mag` column of our DataFrame, which represents the magnitude of the acceleration data. Counting the number of these peaks gives us an estimate of the number of steps. However, typically, you will under/over estimate the number of steps by quite a large margin unless you fine tune the parameters of the `find_peaks` function.

### Tuning Parameters: Prominence and Width

1. **Prominence**: This parameter helps in distinguishing the true peaks from noise. A higher prominence value would mean that only the peaks which stand out prominently from their neighbors would be detected. This can be particularly useful to ensure that the small fluctuations or noise in the data do not get identified as steps.

2. **Width**: The width parameter is crucial in the context of step detection because it directly relates to our intuition about the duration between consecutive steps. For instance, consider a typical walking pace: we expect a person to take around 1 to 2 steps every second, depending on their speed. If our data is sampled at 100 Hz (100 samples per second), a step, which takes half a second, would span roughly 50 samples. Thus, the `width` parameter can be tuned based on our expectations of step duration and the sampling rate of our data.

### Importance of Sampling Rate

The sampling rate, or the number of samples collected per unit of time, plays a pivotal role in peak detection. Given our earlier example, if we're walking at a pace of 1-2 steps per second:

- At a 50 Hz sampling rate, a step might span 25 to 50 samples.
- At a 100 Hz sampling rate, a step might span 50 to 100 samples.

As you can see, the width parameter's optimal value changes with the sampling rate. Thus, when tweaking the `width` parameter, it's essential to consider the sampling rate of the data to ensure accurate peak (step) detection.

### Summary

The `find_peaks` function, with its prominence and width parameters, offers a flexible tool for step detection in accelerometer data. By understanding and adjusting these parameters in the context of our data's sampling rate and the expected step duration, we can achieve reliable and accurate step counting in Python.
