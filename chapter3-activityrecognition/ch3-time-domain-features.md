---
layout: default
title: Time domain features
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

## Time Domain Features

Time-domain features represent statistical measures derived from a sequence of samples within a specific window, such as 100 samples. These features serve as essential building blocks for discerning patterns and categorizing different activities based on accelerometer data.

#### Key Features:
- *Mean*
- *Median*
- *Variance*
- *Standard deviation*
- *Min*
- *Max*
- *Range*
- *Zero-crossings*
- *Angle*
- *Angular velocity*

Let's delve deeper into some of these accelerometer-based time-domain features:

#### Mean

- **Definition**: The average of acceleration values over a window.
- **Utility**: Helps in differentiating activities based on their overall acceleration magnitude.
- **Examples**: Clearly distinguishes between standing (which typically has a near-zero mean) and more dynamic activities like walking or running which exhibit higher means.
- **Confounders**: Might blur the distinction between sitting and standing since both can portray similar mean values.

#### Median

- **Definition**: The middle value once acceleration values are arranged in order.
- **Utility**: Provides a more robust measure in the presence of outliers compared to the mean.
- **Examples**: Helps differentiate between regular walking and sudden jolts during walking which might be seen as outliers.

#### Variance & Standard Deviation

- **Definition**: Variance indicates the dispersion of numbers from the mean. The standard deviation is essentially the square root of variance.
- **Utility**: Enables differentiation of activities based on variability.
- **Examples**: Running, for instance, might exhibit a higher variance than walking. Additionally, walking upstairs can reflect a distinct variance pattern in contrast to flat surface walking.
- **Confounders**: There might be overlapping variance values for activities that are somewhat similar.

#### Min, Max, & Range

- **Definition**: Represents the minimum and maximum acceleration values within a window. The range is the differential between these values.
- **Utility**: Recognizes the extreme limits of motion.
- **Examples**: Activities like jumping can display a higher range than walking due to the drastic up-and-down motions involved.

#### Zero-Crossings

- **Definition**: Counts the instances when the signal transits through a zero value.
- **Utility**: Particularly beneficial for repetitive or cyclical motions.
- **Examples**: Activities such as walking or running may manifest periodic zero-crossings, attributed to the consistent foot-strike patterns.
- **Confounders**: Excessive noise within data can give rise to a higher count of zero-crossings.

#### Other Features

**Cross-Correlation** - Measures the similarity between two signals relative to the delay imposed on one of them. For instance, comparing acceleration in the X-axis with that in the Y-axis.

**Number of Peaks and Troughs** - Presents data on the repetitiveness and intensity of specific activities. Activities with a higher frequency like jogging will likely register more peaks within a specific window than walking.

**Slope of Zero Crossing** - Indicates the rate of value change during a zero crossing. This can be pivotal in distinguishing between slow-paced and rapid movements.

### Features from Gyroscopes and Magnetometers

Although the primary emphasis has been on accelerometers, other sensors like gyroscopes and magnetometers are equally valuable. Gyroscopes record rotational movements, while magnetometers detect magnetic field intensity.

##### Gyroscope

**Angle & Angular Velocity**: Provides insights into the rotation speed of an object. Activities involving turning or spinning will generally indicate higher values.

- **Definition**: Angle denotes orientation inferred from accelerometer and gyroscope data integration. Angular velocity measures the change rate of this angle.
- **Utility**: Offers insights into orientation and its variations.
- **Examples**: Different body postures like standing and sitting might reflect varying orientations. Movements such as turning or twisting can be effectively captured using angular velocity.

##### Magnetometer

- **Magnetic Field Strength**: Presents orientation data in relation to the Earth's magnetic field.
- **Utility**: Can assist in determining the direction an individual is moving or facing.

#### Combining Features

Leveraging a single feature may not always be sufficient in differentiating activities, especially when there's an overlap. However, amalgamating multiple features can create a multi-dimensional realm, making activity categorization more precise and definitive. For instance, using just the mean and variance might not clearly differentiate between ascending and descending stairs, but their combination could provide a sharper distinction.

## Implementing feature extraction in Python

Lets look at how you can implement time-domain feature extraction in Python. We will look at a couple of examples where accelerometer and temperature data are split into windows of appropriate size and features are extracted from that window of data. 

### The `resample` function

A python function that is particularly useful for converting raw data into a feature vector is the resample function. Lets take the case of accelerometer data with three orthogonal axes: X, Y, and Z. 

```python
import pandas as pd

# Assuming your data frame 'df' has a DateTime index and columns 'x', 'y', and 'z' for accelerometer readings.
resampled_data = pd.DataFrame()

for t, w in df.resample('100L'):
    frame = {}
    frame['time'] = t
    frame['x_mean'] = w['x'].mean()
    frame['y_mean'] = w['y'].mean()
    frame['z_mean'] = w['z'].mean()
    
    frame['x_std'] = w['x'].std()
    frame['y_std'] = w['y'].std()
    frame['z_std'] = w['z'].std()
    
    resampled_data = resampled_data.append(frame, ignore_index=True)
```

In this code:

- We resample the raw accelerometer data at 100 milliseconds intervals ('100L').
- For each window, we compute the mean and standard deviation for the X, Y, and Z accelerometer readings.
- We create a dictionary (frame) for each window, populate it with the computed features and the time stamp (t), and then append it to a new DataFrame (resampled_data).

After executing this code, resampled_data will hold the resampled accelerometer data with features calculated for each window. Using a dictionary like this streamlines the process of iterative feature engineering and DataFrame population. The `append` method of pandas DataFrame can easily ingest dictionaries, where each key becomes a column in the DataFrame, and the corresponding value becomes the row entry for that column.

## Notebook: Resampling temperature time-series ([html](notebooks/Chapter3-Resampling.html)) ([ipynb](notebooks/Chapter3-Resampling.ipynb))
This notebook shows an example using `resample` and applies it to a synthetic temperature data trace. The initial temperature signal is generated at 10Hz over 2 weeks. The notebook shows how this can be resampled into hourly and daily intervals and a few features extracted for each window.


