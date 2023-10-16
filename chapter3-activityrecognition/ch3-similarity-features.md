---
layout: default
title: Similarity-based features
parent: Activity Recognition
grand_parent: Mobile Sensing &amp; Analytics
nav_order: 5
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

## Similarity-based Features

Similarity metrics play an integral role in time-series analysis, especially when dealing with human-centric data such as movements and speech. This can be useful in mobile health (mHealth), where patterns can be extracted from various sources like inertial sensors, audio recordings, and video feeds to deduce information about a user's state or condition.

**Gait Similarity**: For instance, gait—the pattern of walking—can be very informative. Two individuals with a standard walking pattern might have high gait similarity. However, someone with a neurological disorder might exhibit a distinctly different gait pattern. By measuring similarity or dissimilarity in gait patterns, clinicians can discern deviations from the norm and make diagnostic or treatment decisions.

**Gesture Recognition**: In the realm of Internet of Things (IoT) and smart homes, gesture recognition is gaining prominence. Users might control devices through specific hand gestures. However, these gestures might not be perfectly synchronized across users or even for the same user over time. Some gestures might be faster, while others could be slower. Hence, time-aligned similarity metrics become important.

### Key Similarity Metrics

#### Euclidean Distance

- **Definition**: A straight-line distance between two points in Euclidean space.
- **Utility**: Useful for measuring the absolute difference between two time-series signals.
- **Examples**: Can help differentiate between two audio signals, like a shout versus a whisper, based on magnitude and pitch.
- **Confounders**: Highly sensitive to distortions and time shifts.

#### Dynamic Time Warping (DTW)

- **Definition**: An algorithm that finds an optimal alignment between two sequences. DTW can adjust for speed differences (like stretching or compressing) between two time series.
- **Utility**: Especially helpful when sequences have temporal shifts. More robust than Euclidean Distance to stretching and compression, for example, if one speaker speaks in a slow drawl whereas another speaker is faster; or if the same gesture is performed slowly by one person but rapidly by another.
- **Examples**: Recognizing hand gestures for IoT devices. Even if one gesture is performed more slowly than the other, DTW can still find an optimal match.
- **Confounders**: Computationally intensive, especially for long sequences.

#### Cosine Similarity (not covered in class; not needed for quiz)

- **Definition**: Measures the cosine of the angle between two non-zero vectors. Values range from -1 (completely dissimilar) to 1 (completely similar).
- **Utility**: Measures orientation rather than magnitude, often used in text analysis but can be applied to time-series data.
- **Examples**: Comparing orientation of movement trajectories captured by inertial sensors.

### Applications in mHealth

In mHealth scenarios, different sensors capture a plethora of data.

1. **Inertial Sensors**: Capturing movements and gestures. Similarity metrics can help in activity recognition or detecting abnormalities in movement patterns.
  
2. **Audio**: Speech patterns might vary due to fatigue or certain medical conditions. Similarity metrics can discern these nuances, aiding in early diagnosis or monitoring.

3. **Facial Features**: Facial expressions can be indicative of emotional states or reactions to stimuli. By measuring similarity in facial movements over time, one can trace the evolution of emotional states or even detect neurological anomalies.

