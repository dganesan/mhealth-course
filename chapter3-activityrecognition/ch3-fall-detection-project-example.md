# Fall Detection Using Wearable Sensors
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

To distinguish between these movement types, we need rich sensor data that captures both linear and rotational motion. Modern smartphones provide us with two perfect tools for this: the accelerometer and gyroscope. The accelerometer measures linear acceleration across three axes, making it particularly sensitive to impacts and sudden movements. It's excellent at detecting the intensity of motion but can sometimes struggle to distinguish between similar movements with different rotational components. This is where the gyroscope becomes useful. By measuring rotational velocity, it helps us understand how the device (and by extension, the body) orients itself during different movements. The combination of these two sensors can potentially provide a  more complete picture of movement than either sensor alone. For instance, while both a fall and a controlled sit-down might show similar acceleration patterns, their rotational signatures often differ significantly. In summary, we use two sensors:

* **Accelerometer Data**: Provides linear acceleration measurements across three axes, capturing the intensity and direction of movement. This sensor is particularly sensitive to sudden changes in motion, making it ideal for detecting impact events.

* **Gyroscope Data**: Measures rotational velocity, offering insights into how the device (and by extension, the body) orients itself during different movements. This data is crucial for distinguishing between similar movements that have different rotational components.

![Example Sensor Signals](images/fall-signals-example.png)

*Figure 1: Example accelerometer (left) and gyroscope (right) signals during a fall event, showing characteristic impact patterns*

As we move through this project guide, we'll explore how to collect data from these sensors effectively, process it appropriately, and extract meaningful features that help our classification system distinguish between different types of movement. We'll see how the challenges of data collection differ for discrete events versus continuous activities, and learn strategies for handling both effectively. Most importantly, you'll develop practical skills in dealing with real-world data collection challenges – skills that extend far beyond this specific application to the broader field of machine learning and data science.

![Processing pipeline](images/fall-detection-pipeline.svg)

*Figure 2: Overall processing pipeline*

## Discrete Events vs Continuous Activities

One of the key challenges in human activity recognition is understanding the fundamental difference between discrete events and continuous activities:

* **Discrete Impact Events**: Falls, stumbles, and trips are singular events that occur at specific moments in time. These events have clear start and end points, with a distinct impact moment that we want to capture. For these events, we need to identify and isolate each occurrence specifically.
* **Continuous Activities**: Activities like walking, standing, or general movement are ongoing and don't have natural boundaries. These activities can be recorded in longer continuous segments and later divided into analysis windows, as there's no specific "event" to capture.

For discrete events like falls, we need to capture each instance separately and ensure we have enough examples for training. But what counts as "enough"? Through experimentation, we've found that about 50 samples per event type provides a good balance between effort and model performance. This brings us to our first major decision point: how to collect these 50 samples efficiently while ensuring data quality.

### Recording Strategies

![Data Collection Methods](images/data-collection-methods.svg)

*Figure 3: Comparison of batch and individual recording methods for fall data collection*

As shown in Figure 3, we have two main approaches to collecting our fall data. 

* **Batch recording** The batch recording method initially seems more efficient - start recording, perform all 50 falls with short breaks between them, then stop. It's quicker and involves less interaction with the recording device. However, this efficiency comes with hidden costs. When you later process this data, you'll need sophisticated algorithms to identify each fall, separate it from the "getting up" motion, and ensure you haven't accidentally included any unwanted segments. If something goes wrong - if the phone shifts in your pocket or if one fall wasn't performed correctly - you might not discover the problem until much later, potentially compromising a large portion of your dataset.
* **Individual recording** The alternative is individual recording - separate files for each fall. While this means more time spent starting and stopping recordings, it provides immediate quality control. You can verify each recording right after making it and redo it if necessary. The processing is also much simpler: trim a few seconds from the start and end of each recording, and you have your fall event cleanly isolated.

** Continuous activities** For continuous activities like walking, our approach is quite different. Here, we're not trying to capture individual events but rather collect enough examples of the activity to represent its natural variation. A single 2-3 minute recording of walking, for instance, will provide plenty of data once we split it into windows for analysis.

### Recommended Strategy for Students

Given these considerations, we recommend that students use the individual recording method for falls and impact-like events. Yes, it takes more time. Yes, you'll handle more files. But the benefits outweigh these inconveniences. The quality control alone makes it worthwhile - nothing is more frustrating than discovering problems in your data after you've completed all your recordings.

Moreover, this method provides valuable learning opportunities. Each recording becomes a mini-experiment where you can observe the sensor patterns immediately and develop an intuition for what constitutes a "good" recording. This understanding becomes invaluable when you move on to feature extraction and classification.

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

![Window Selection Strategies](images/window-selection-strategies.png)

*Figure 4: Windowing strategies for different activity types, showing how raw sensor data is processed into feature vectors*

* **High-Impact Events**: When dealing with falls and other high-impact events, these events pivot around a crucial moment - the impact - and the window needs to capture not just this moment but the motion leading up to and following it. So you can pick a 5-second window centered on the impact point (±2.5 seconds) to provide a good view of the event. 
* **Impact-Like Events**: Impact-like events such as controlled sitting or deliberate drops might have temporal patterns that are different from that of fall events. Someone carefully lowering themselves to the ground might take twice as long as someone falling, yet both actions need to be correctly classified. So, for each such event, you need to pick a window that is appropriate for its natural duration.
* **Regular Activities**: Walking, standing, and other regular activities require a fundamentally different approach. Without natural start and end points, we impose structure through systematic sampling. One solution is to sliding windows - 5-second segments that overlap by 50\%; you can also try non-overlapping windows. We usually prefer overlapping windows for two reasons. First, it ensures we don't miss important transitions that might occur at window boundaries. Second, it provides our classifier with multiple perspectives on the same movement, improving its ability to recognize patterns. The 5-second duration captures enough cycles of repetitive movements (like walking) to establish clear patterns while remaining short enough to detect activity changes promptly.

Despite these different windowing strategies, our goal is to feed consistent, comparable data to our classifier. Each window, regardless of its source or size, must generate the same set of features. For fixed-width windows from falls and sliding windows from regular activities, this is straightforward. This unified approach allows our classifier to learn the distinctive patterns of each activity type while handling the inherent differences in how these activities unfold over time. The key is maintaining this consistency without losing the unique temporal characteristics that help distinguish between different types of movement.

In the next section, we'll explore how to extract meaningful features from these windows, leveraging both accelerometer and gyroscope data to capture the full complexity of human movement.

## Feature Extraction from Multiple Sensors

With our data properly windowed, we now face the challenge of extracting meaningful features that capture the essence of different movements. While previous assignments focused solely on accelerometer data, our fall detection system leverages both accelerometer and gyroscope signals. This dual-sensor approach provides a richer understanding of movement patterns, as illustrated in Figure 5.

![Feature Extraction Pipeline](images/feature-extraction-pipeline.svg)

*Figure 5: Feature extraction pipeline showing parallel processing of accelerometer and gyroscope data*

## Feature Extraction from Multiple Sensors

When working with both accelerometer and gyroscope data, we extend our feature extraction approach to capture the unique characteristics of both sensors. Figure 5 illustrates how we process data from both sensors to create a comprehensive feature vector that captures both linear acceleration and rotational motion patterns. After segmenting our data into appropriate windows, we process accelerometer and gyroscope data streams using the same pipeline. Each sensor provides three-dimensional data (X, Y, Z axes), and we extract the same set of features from each dimension. This parallel approach ensures we capture both the linear and rotational aspects of each movement, providing our classifier with a richer understanding of the activity dynamics.

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

### Implementation Tips

When extending your existing accelerometer-based code to include gyroscope features:

1. **Naming Convention**: Use clear prefixes ('acc_' and 'gyr_') to distinguish features from different sensors. This makes your code more maintainable and helps when analyzing feature importance later.

2. **Signal Processing**: While the feature extraction functions are the same, remember that accelerometer and gyroscope signals have different units and typical value ranges. Consider normalizing each sensor's data separately before feature extraction.

3. **Feature Selection**: Not every feature needs to be calculated for both sensors. Some features might be more meaningful for one sensor than the other. As you develop your system, you can analyze feature importance to determine which combinations work best for your specific classification task.

4. **Processing Efficiency**: Since the same functions are applied to both sensor streams, consider structuring your code to avoid duplication. A general feature extraction function that can be applied to either sensor type can make your code more efficient and easier to maintain.

This comprehensive approach to feature extraction ensures your classification system can leverage both linear and rotational motion information, typically resulting in more robust activity recognition compared to single-sensor approaches.
### Parallel Processing: Two Perspectives on Movement

Think of accelerometer and gyroscope data as two complementary views of the same movement. The accelerometer tells us about linear motion - how quickly something speeds up, slows down, or changes direction. The gyroscope reveals rotational motion - how the body turns and tilts during movement. Together, they paint a complete picture that neither sensor could provide alone.

Consider a fall versus a controlled sit-down. Both might show similar patterns of downward acceleration, but their rotational signatures often differ dramatically. A fall typically involves uncontrolled rotation, while sitting down shows a more measured, deliberate rotational pattern. By processing both sensor streams in parallel, we capture these subtle but crucial differences.

### Time Domain Analysis: The Basic Building Blocks

The foundation of our feature extraction starts with statistical measures that capture the overall characteristics of movement. From each axis of both sensors, we compute measures like mean, standard deviation, maximum and minimum values, and root mean square (RMS). While these calculations are identical for both sensors, their interpretations differ in meaningful ways.

Take RMS as an example. For accelerometer data, a high RMS value indicates intense linear motion - the kind you might see during a fall. For gyroscope data, high RMS suggests significant rotational movement - perhaps someone spinning as they fall. When analyzing controlled movements like sitting down, you might see moderate accelerometer RMS values paired with low gyroscope RMS, indicating deliberate linear motion with minimal rotation.

### Peak Analysis: Finding Critical Moments

The relationship between acceleration peaks and rotational velocity becomes particularly fascinating during impact events. A fall typically shows sharp acceleration peaks coinciding with rapid changes in rotational velocity. The width and prominence of these peaks tell us about the nature of the impact - sharp, narrow peaks often indicate sudden stops, while broader peaks suggest more controlled movements.

Looking at both sensors reveals temporal relationships that neither could show alone. During a fall, we often see rotational velocity peaks slightly preceding acceleration peaks, as loss of balance (rotation) leads to the actual fall (acceleration). In controlled movements, these peaks might be more synchronized, indicating deliberate coordination of rotation and linear motion.

### Frequency Domain: Patterns in Time

Transforming our signals into the frequency domain reveals periodic patterns that might be invisible in the time domain. For continuous activities like walking, accelerometer frequency features capture the rhythmic pattern of steps, while gyroscope features might reveal the subtle rocking motion of the body. Even in discrete events like falls, frequency domain features can distinguish between smooth, controlled movements and the chaotic frequencies characteristic of uncontrolled motion.

### Creating a Unified Feature Vector

All these individual features come together in our final feature vector, where careful organization becomes crucial. Here's how we structure our data:

```python
features_df = pd.DataFrame({
    # Accelerometer features first, organized by axis
    'acc_mean_x': [...], 'acc_std_x': [...], 'acc_peak_x': [...],
    'acc_mean_y': [...], 'acc_std_y': [...], 'acc_peak_y': [...],
    'acc_mean_z': [...], 'acc_std_z': [...], 'acc_peak_z': [...],
    
    # Then gyroscope features, following the same pattern
    'gyr_mean_x': [...], 'gyr_std_x': [...], 'gyr_peak_x': [...],
    'gyr_mean_y': [...], 'gyr_std_y': [...], 'gyr_peak_y': [...],
    'gyr_mean_z': [...], 'gyr_std_z': [...], 'gyr_peak_z': [...]
})
```

This organization isn't just about keeping things tidy - it makes it easier to analyze feature importance and understand how different aspects of movement contribute to classification decisions.

### Practical Implementation Considerations

When implementing this dual-sensor approach, keep a few key principles in mind. First, normalize your sensor data separately before feature extraction, as accelerometers and gyroscopes operate on different scales. Second, maintain consistent naming conventions - the 'acc_' and 'gyr_' prefixes prevent confusion and make your code more maintainable. Finally, remember that not every feature needs to be calculated for both sensors - let your understanding of movement patterns guide which features you prioritize.

The effort invested in careful feature extraction pays dividends in classification performance. By thoughtfully combining features from both sensors, we create a robust foundation for distinguishing between different types of movement. The next challenge lies in using these features effectively in our classification system, a topic we'll explore in the following section.