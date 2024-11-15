---
layout: default
title: Fall Detection - Project Example
parent: Activity Recognition
grand_parent: Mobile Sensing &amp; Analytics
nav_order: 10
usemathjax: true
description: "Activity Recognition"
---

# Fall Detection - Project Example
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Project Overview

In the assignments throughout this course, you've worked with carefully curated datasets where the hard work of data collection, cleaning, and labeling was already done for you. However, real-world machine learning projects rarely start with such polished data. This project guides you through the complete process of building a fall detection system from the ground up, introducing challenges you haven't encountered in previous assignments and showing you how to overcome them. This will be useful for you as you think through your project.

Our goal is to create a system that can reliably distinguish between different types of human movement, with particular attention to high impact events such as potentially dangerous falls. This isn't as straightforward as it might first appear – the system needs to recognize the difference between someone accidentally falling and someone intentionally sitting down quickly, while also being able to ignore routine movements like walking or standing. To accomplish this, we'll expand beyond the single-sensor approach used in your assignments to leverage both accelerometer and gyroscope data.

### Classification Categories

Our system focuses on three distinct movement categories, each representing different levels of impact and motion patterns:

* **Impact Events**: These are sudden, high-intensity movements characterized by rapid acceleration changes. This category includes hard falls, stumbles, and trips where the body experiences unexpected motion changes. These events typically show distinctive spike patterns in sensor data, making them particularly interesting for detection.

* **Impact-like Events**: These represent controlled movements that may appear similar to falls in sensor data but are intentional actions. Examples include sitting down on the floor, dropping into a chair, or reaching for something on the ground. These movements share some characteristics with actual falls but follow more controlled patterns.

* **Regular Activities**: This category encompasses typical daily movements like walking, standing, or light motion. These activities serve as our baseline and help the classifier understand the difference between normal movement patterns and potential fall events.

### Sensor Configuration

To distinguish between these movement types, we need rich sensor data that captures both linear and rotational motion, so lets use both the accelerometer and gyroscope. 

* **Accelerometer Data**: Provides linear acceleration measurements across three axes, capturing the intensity and direction of movement. This sensor is particularly sensitive to sudden changes in motion, making it ideal for detecting impact events.

* **Gyroscope Data**: Measures rotational velocity, offering insights into how the device (and by extension, the body) orients itself during different movements. This data is crucial for distinguishing between similar movements that have different rotational components.

![Example Sensor Signals](images/fall-signals-example.png)

*Figure 1: Example accelerometer (left) and gyroscope (right) signals during a fall event, showing characteristic impact patterns*

<img src="images/fall-detection-pipeline.png" alt="Fall Detection Pipeline" style="max-width: 100\%; cursor: pointer;" onclick="window.open(this.src, '_blank');">

![Fall Detection Pipeline](images/fall-detection-pipeline.svg)

*Figure 2: Overall processing pipeline*

## Labeled Data Collection

One of the key challenges you will face is deciding how to collect and label your data. For this, you will need to first understand the difference between discrete events and continuous activities:

### Discrete Events vs Continuous Activities

* **Discrete Impact Events**: Falls, stumbles, and trips are singular events that occur at specific moments in time. These events have clear start and end points, with a distinct impact moment that we want to capture. For these events, we need to identify and isolate each occurrence specifically.
* **Continuous Activities**: Activities like walking, standing, or general movement are ongoing and don't have natural boundaries. These activities can be recorded in longer continuous segments and later divided into analysis windows, as there's no specific "event" to capture.

For discrete events like falls, we need to capture each instance separately and ensure we have enough examples for training. But what counts as "enough"? Generally, about 50 samples per event type provides a good balance between effort and model performance. This brings us to our first major decision point: how to collect these 50 samples efficiently while ensuring data quality.

### Recording Strategies

![Data Collection Methods](images/data-collection-methods.svg)

*Figure 3: Comparison of batch and individual recording methods for fall data collection*

As shown in Figure 3, we have two main approaches to collecting our fall data. 

* **Batch recording** The batch recording method initially seems more efficient - start recording, perform all 50 falls with short breaks between them, then stop. It's quicker and involves less interaction with the recording device. However, this efficiency comes with hidden costs. When you later process this data, you'll need sophisticated algorithms to identify each fall, separate it from the "getting up" motion, and ensure you haven't accidentally included any unwanted segments. If something goes wrong - if the phone shifts in your pocket or if one fall wasn't performed correctly - you might not discover the problem until much later, potentially compromising a large portion of your dataset.
* **Individual recording** The alternative is individual recording - separate files for each fall. While this means more time spent starting and stopping recordings, it provides immediate quality control. You can verify each recording right after making it and redo it if necessary. The processing is also much simpler: trim a few seconds from the start and end of each recording, and you have your fall event cleanly isolated.

For continuous activities like walking, our approach is quite different.
**Continuous activities**  Here, we're not trying to capture individual events but rather collect enough examples of the activity to represent its natural variation. A single 5 minute recording of walking, for instance, will provide plenty of data once we split it into windows for analysis.

**Recommended Strategy for Students** Given these considerations, we recommend that students use the individual recording method for falls and impact-like events. Yes, it takes more time and you'll handle more files. But the  quality control makes it worthwhile - nothing is more frustrating than discovering problems in your data after you've completed all your recordings. Moreover, this method provides valuable learning opportunities. Each recording becomes a mini-experiment where you can observe the sensor patterns immediately and develop an intuition for what constitutes a "good" recording. This understanding becomes invaluable when you move on to feature extraction and classification.

### Practical Implementation

For falls and impact-like events, establish a consistent recording protocol:
1. Start your recording
2. Wait two seconds to establish a clean baseline
3. Perform the fall or movement
4. Stay still for two seconds to ensure a clean endpoint
5. Stop recording
6. Immediately verify the data quality
7. Label and save the file

For continuous activities, the process is simpler:
1. Start recording
2. Perform the activity naturally for say 5 minutes
3. Stop recording

Remember that safety comes first, especially when recording fall data. Use protective mats, ensure you have enough space, and consider having a spotter present. It's better to take extra time and stay safe than to rush and risk injury.

This structured approach to data collection sets the foundation for everything that follows. Clean, well-organized data makes the subsequent processing and classification tasks much more manageable. In the next section, we'll explore how to take this raw data and transform it into windows suitable for feature extraction.

## Window Selection Strategies

Once we've collected our raw sensor data, we face a new challenge: how do we divide this data into meaningful segments for analysis? The answer varies depending on what type of movement we're examining. Figure 4 illustrates how we can handle types of activities.

![Window Selection Strategies](images/window-selection-strategies.svg)

*Figure 4: Windowing strategies for different activity types, showing how raw sensor data is processed into feature vectors*

* **High-Impact Events**: When dealing with falls and other high-impact events, these events pivot around a crucial moment - the impact - and the window needs to capture not just this moment but the motion leading up to and following it. So you can pick a 5-second window centered on the impact point (±2.5 seconds) to provide a good view of the event. 
* **Impact-Like Events**: Impact-like events such as controlled sitting or deliberate drops might have temporal patterns that are different from that of fall events. Someone carefully lowering themselves to the ground might take twice as long as someone falling, yet both actions need to be correctly classified. So, for each such event, you need to pick a window that is appropriate for its natural duration.
* **Regular Activities**: Walking, standing, and other regular activities require a fundamentally different approach. Without natural start and end points, we impose structure through systematic sampling. One solution is to sliding windows - 5-second segments that overlap by 50\%; you can also try non-overlapping windows. We usually prefer overlapping windows for two reasons. First, it ensures we don't miss important transitions that might occur at window boundaries. Second, it provides our classifier with multiple perspectives on the same movement, improving its ability to recognize patterns. The 5-second duration captures enough cycles of repetitive movements (like walking) to establish clear patterns while remaining short enough to detect activity changes promptly.

In the next section, we'll explore how to extract meaningful features from these windows, leveraging both accelerometer and gyroscope data to capture the full complexity of human movement.

## Feature Extraction from Multiple Sensors

With our data properly windowed, we now face the challenge of extracting meaningful features that capture the essence of different movements. While previous assignments focused solely on accelerometer data, our fall detection system leverages both accelerometer and gyroscope signals. This dual-sensor approach provides a richer understanding of movement patterns, as illustrated in Figure 5.

![Feature Extraction Pipeline](images/feature-extraction-pipeline.svg)

*Figure 5: Feature extraction pipeline showing parallel processing of accelerometer and gyroscope data*

### Time Domain Features

For both sensors, we begin with basic statistical measures that capture the central tendency and variability of the signal. From each axis of both the accelerometer and gyroscope, we compute:
- Mean values that represent average motion intensity
- Standard deviation indicating motion variability
- Maximum and minimum values showing movement extremes
- Root Mean Square (RMS) capturing the signal's overall energy

### Peak Characteristics

Peak analysis becomes particularly interesting when comparing accelerometer and gyroscope data. In a fall event, we typically see:
- Sharp acceleration peaks indicating sudden impacts
- Corresponding rotational velocity peaks showing body orientation changes
- Peak width and prominence that help distinguish controlled versus uncontrolled movements

The relationship between these peaks often helps distinguish between similar activities – for instance, a fall versus a controlled sitting motion might show similar acceleration patterns but very different rotational velocity signatures.

### Frequency Domain Analysis

Transforming both sensor streams into the frequency domain reveals different aspects of the movement:
- Accelerometer frequency features capture repetitive linear motions
- Gyroscope frequency features identify rotational patterns
- Dominant frequencies often differ between sensors for the same activity

### Creating the Combined Feature Vector

The final step concatenates features from both sensors into a single feature vector. In your pandas DataFrame, each row represents one window of activity, with columns clearly labeled by both sensor type and feature:

```python
features_df = pd.DataFrame({
    # Accelerometer features
    'acc_mean_x': [...],
    'acc_std_x': [...],
    'acc_peak_height_x': [...],
    'acc_dom_freq_x': [...],
    # (repeat for y and z axes)
    
    # Gyroscope features
    'gyr_mean_x': [...],
    'gyr_std_x': [...],
    'gyr_peak_height_x': [...],
    'gyr_dom_freq_x': [...],
    # (repeat for y and z axes)
})
```

**Implementation Tips**  When extending your existing accelerometer-based code to include gyroscope features, follow these two tips:
* **Naming Convention**: Use clear prefixes ('acc_' and 'gyr_') to distinguish features from different sensors. This makes your code more maintainable and helps when analyzing feature importance later.
* **Feature Selection**: Not every feature needs to be calculated for both sensors. Some features might be more meaningful for one sensor than the other. As you develop your system, you can analyze feature importance to determine which combinations work best for your specific classification task.

