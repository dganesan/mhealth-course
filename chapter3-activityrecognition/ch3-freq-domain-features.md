---
layout: default
title: Freq domain features
parent: Activity Recognition
grand_parent: Mobile Sensing &amp; Analytics
nav_order: 3
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

**Frequency domain features:** This class of features represents information about periodic patterns and rhythmic behavior in the signal. Again, you saw such features in the pedometer case study, where you were asked to look for a periodic pattern in the walking signal. This is exactly the type of information that we are looking to extract, but by leveraging some more powerful methods. 

While the methods themselves are outside the scope of our review, the features are important to understand. The dominant frequency feature corresponds to the most significant rhythmic component in the data. For example, in the case of the walking traces, this would be the steps, with a period of roughly ½ second per step. The signal energy is another way of looking at the amount of variation in the accelerometer data - the larger its periodic components, the more the signal energy. There are other such frequency domain features, but these two are sufficient for our needs.

*Examples of frequency domain features: Dominant frequency, Signal Energy.*


The figure below shows an example for walking on a treadmill. You can see that there seem to be a few dominant frequencies, and some of them are harmonics of the frequency of the walking. But the dominant frequencies give you sufficient information about the periodicity of walking.

 <img src="images/image3.png" alt="drawing" width="500"/>

_Figure 2: Energy in different frequency bands for accelerometer data collected during walking_
