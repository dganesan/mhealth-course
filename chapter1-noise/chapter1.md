---
layout: default
title: Chapter 1
nav_order: 1
usemathjax: true
description: "Chapter 1"
---

# Chapter 1: Sensor data smoothing and filtering

Most sensor data is affected to some extent by **noise**, that is unexplained variations in the data that in many cases is uninterpretable, and in almost all cases is not of interest to us. Data analysis is often considerably simpler if this noise can be removed from the data. This process is referred to by various terms - data smoothing, filtering, cleaning, and so on. The underlying idea in all these methods is to remove the noise while retaining the important characteristics of the signal.

Noise removal techniques can be divided into two class. The first is time-domain approaches, which is the more intuitive way of approaching the problem. The second is frequency-domain approaches, which removes noise that is periodic in nature. Our goal is not to provide a detailed mathematical exposition of these techniques but to keep it practical. You can tackle most issues with noise in sensor data analysis by understanding the general idea underlying these techniques, and by knowing which denoising technique to apply and when. Before we launch into these three classes, however, we give you a brief introduction into the difference being time and frequency domain information in signals, and noise in sensor signals.


# Information and Noise in Signals

One very important part of any sensor data processing task is understanding how information is contained in the signals you are working with, and what types of noise can corrupt the signal and make it difficult to extract the information. 

There are two ways that are common for information to be represented in naturally occurring signals. We will call these: information represented in the time domain, and information represented in the frequency domain. Information represented in the time domain describes when something occurs and what the amplitude of the occurrence is. For example, you may be interested in the temperature of this room, the orientation of your phone, your location and driving trajectory, and so on. All of these contain information in the time domain.

In contrast, information represented in the frequency domain is more indirect. Many things in our universe show periodic motion. For example, accelerometer readings when you walk show periodic motion; a wine glass struck with a fingernail will vibrate, producing a ringing sound; your heart beats in a quasi-periodic manner; the pendulum of a grandfather clock swings back and forth, and so forth. By measuring the frequency, phase, and amplitude of this periodic motion, information can often be obtained about the system producing the motion. Suppose we sample the accelerometer on your phone. A single sample, in itself, contains no information about the periodic motion, and therefore no information about the walking activity. The information is contained in the frequency with which patterns corresponding to steps occur in the signal.

Noise is anything that corrupts the signal and makes it difficult to extract the information of interest. We deal with noisy signals all the time, often without our knowledge. For example, when we use a thermometer to check body temperature, it is common to take two or three readings to verify that the first one did not have noise. 

There are many different types of noise --- noise may appear are sudden spikes in the signal, as  random perturbations, as periodic variations, and so on. The underlying physical phenomena causing noise can range from quantum noise or electronic and mechanical noise in the sensor, to a variety of external factors that depend on sensor placement, external vibrations and electronic interference and so on.


# Noisy Sensor Signals

Now that you understand the difference between information and noise, let us turn to what causes noise in sensor data. We will start by showing you different examples of noisy signals and what are some common sources of noise in these signals.


### Noise in Accelerometer Data

Figure 1 shows the typical accelerations along the three axes (x, y, and z) while walking. You can see that there is clearly some periodic pattern in this data, but it also seems really noisy making it hard to analyze the data to extract useful information such as number of steps. The noise in the accelerometer signal can be categorized into two types.



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


_Figure 1: Typical pattern of x-, y-, and z accelerations while walking with smartphone in pocket._

**Intrinsic sensor noise**: Some of the sources of noise in an accelerometer is due to the electronic noise from the circuitry that is converting the motion into a voltage signal and the mechanical noise from the sensor itself. There are several sources of electronic noise, referred to as Johnson noise, shot noise, flicker noise, and several others.  The mechanical noise of the sensor comes from thermo-mechanical noise, which arises due to the fact that an accelerometer has tiny moving parts, and these are susceptible to mechanical noise due to molecular agitation. Normally, you don’t have to worry about the intrinsic sensor noise because the sensor manufacturer would have carefully calibrated the sensor and the hardware filters to deal with them. But sometimes they do manifest in the signal. 

**External vibration noise**: Another common source of noise is external vibration noise, which is noise from the movements external to the sensor and therefore affects the readings. For example, consider the case that you want to detect whether a phone is being carried by a person or not. An intuitive algorithm to determine this would be to check if the accelerometer reading is changing. If the accelerometer reading is continuously changing, that would imply that the phone is being carried, whereas if the reading is not changing, then it is stationary. 

If you implement this algorithm, you will find that it does not work as expected. The reason is that even though you think that the phone is stationary when placed on say, a table, there are continuous external vibrations induced by the earth’s movement, nearby vehicles, the HVAC system, people’s movement, and many others. These tiny movements manifest as small changes in the accelerometer reading which can be misinterpreted by your algorithm as a person carrying a phone.

As another example, take the case of the algorithm that detects how you are holding the phone and changes the screen orientation accordingly. This algorithm can use the accelerometer reading to measure tilt (more on this in a later lecture), but we do not want this measure to be influenced by the tremors of your hand. Even though you don’t realize it, there are continuous small tremors in our hand that will be picked up by an accelerometer. If you do not believe me, try holding a laser pointer in one hand and point it at a wall several meters away to see how steady your hand is. The vibrations of your hand make the accelerometer outputs appear “jittery”.  These jitters need to be smoothed before applying an algorithm to determine screen orientation.


### Noise in Electrocardiogram (ECG) Data

This problem is by no means isolated to accelerometer signals. For example, if you looked at signal from an ECG sensor, you would see a lot of noise sources such as those shown in Figure 2. 



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")


_Figure 2: Typical ECG signal with different interference sources_

The figure shows four sources of noise in the ECG signal. One visible problem is power line interference i.e. the 50Hz power line signal causes electromagnetic interference which is recorded by the ECG device. This issue is particularly problematic for low frequency signals like ECG. Many other sources of ECG noise are present as well including those caused by breathing, muscle contractions, body movement, and so on. 


### Noise in Image Data

Images are often noisy, and these sources of noise need to be filtered out before meaningful information can be extracted from the data. Here are two examples of noisy images, and how they look after they are cleaned. In the first example (boat), one could argue that the boat is at least visible in the noisy signal, but in the second example (eye), the noisy data makes it very hard to even identify the fact that it is an image of the eye. Thus, noise can severely impact the visual quality of the image to the point where it may be even hard for the human eye to identify the object(s) present in the image.



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")
         

<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")


<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")


_Figure 3: Noise in images. (left) salt-and-pepper noise, and (right) fixed pattern noise in camera_

The reasons for image noise are many as well --- often, noise is caused by the camera, especially in poor illumination conditions, high temperature or just electronic noise in the circuit. 


### Noise in Audio Signals 

Audio data recorded by a microphone can also be highly susceptible to noise. The noise could be due to ambient sound, for example, you are speaking in a party where many other people are simultaneously talking. Or it could be due to a loud noise nearby such as talking near a construction site. Of course, the hardware and circuit could add to the noise as well. Below is an example that shows how much noise can distort an audio signal.



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.png "image_tooltip")


_Figure 4: Noisy audio signal_

So, how do we deal with noise? Turns out that this is a vast topic, and there are many methods that have been fine tuned to handle noise for different types of sensors. We will not be able to talk about all these methods, but we will try to understand the classes of methods, and the tradeoffs in using these types of filtering techniques.


### Noise in GPS Data

Other sensor information like GPS location is also susceptible to noise. GPS readings can be noisy due to a variety of reasons including clock error, tropospheric delays, multipath effects due to buildings, weather conditions, and so on. If you have used Google Maps or any other mapping service, you may be tempted to believe that GPS is fairly accurate, but the raw data coming from the GPS receiver often has noise that is being smoothed before it is displayed on screen. For example, the figure below shows what you would get if you blindly connected the GPS locations coming from your receiver while you are driving down a street. The green line shows the actual trajectory that should have been observed if the GPS readings were error-free.



<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image7.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image7.png "image_tooltip")


_Figure 5: Noisy GPS readings while driving in red. Actual trajectory in green._


# Time-series Smoothing and Filtering

We start our discussion of smoothing methods with the simplest method, moving average smoothing and proceed to a variant of this method referred to as exponential weighted smoothing. The fact that they are simple doesn’t mean that they are not useful - in spite of their simplicity, these methods are surprisingly effective in practice, and therefore very widely used.


## Over-sampling and Averaging

Many sources of noise tend to be random in nature. Informally, this means that the noise has roughly equal amounts of positive and negative changes, and there is no pattern in the noise over time. Formally, the noise is said to be uncorrelated in time, has zero mean, and finite variance. 

In this case, noise can be reduced by over-sampling the sensor and averaging the values. For example, take the case where you are writing an algorithm to determine the rotation of the screen of the mobile phone. If there were no noise, you may sample at a low rate of say 10 Hz (or 10 times/second), but since you have noise due to small hand movements (if you are holding the phone), you may use a sampling rate of 100 Hz. You can then average every 10 samples readings and the average value is reported at a 10 Hz frequency and used in the application to determine whether the screen has rotated. In this way, the noise in the acceleration signal is reduced. You might ask how much the noise reduces by this method. Mathematically, if you have N samples of a random noise signal, and average these samples, your noise reduces by a factor of 1/√N.


## Moving Average Smoothing

Instead of averaging and reducing the number of samples, one can also perform a moving average. Lets try use an example to illustrate this approach. Figure 1 shows a noisy accelerometer signal, and let us try to apply a moving average smoothing to this signal. We are going to replace each sample by the average of the current sample, the sample before it, and the sample after it. 

More precisely, let us represent the input accelerometer signal as follows:

x =  x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, … x<sub>n</sub> where the index is the sample number.

The output of the moving average filter is:

  _s<sub>1</sub>_ = (x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub>)/3

 _s<sub>2</sub>_ = (x<sub>2</sub> + x<sub>3</sub> + x<sub>4</sub>)/3

 _s<sub>3</sub>_ = (x<sub>3</sub> + x<sub>4</sub> + x<sub>5</sub>)/3

  …

 _s<sub>n-2</sub>_ = (x<sub>n-2</sub> + x<sub>n-1</sub> + x<sub>n</sub>)/3

In the example above, we averaged three input values together, but we could have averaged more nearby points to smooth even more aggressively. As you increase the smoothing window, the signal will look cleaner and more visually pleasing, but beware of using too large a window since you will smooth out the important characteristics of the signal (for example, steps if you want to do step detection).


## Exponential smoothing

Moving average assumes random noise where the statistics of the noise does not change over time. But what happens if the noise itself is a time varying? In this case, exponential smoothing is an effective alternative that works well in practice. The key idea is a small twist on the moving average method described earlier. Whereas the moving average smoothing gives equal weight to the set of values that are averaged, the idea in exponential smoothing is to assign exponentially decreasing weights as the observation get older. In other words, recent observations are given relatively more weight than the older observations.



<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image8.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image8.png "image_tooltip")


where α is the smoothing factor, and 0 &lt; α &lt; 1. In other words, the smoothed output _s<sub>t </sub>_is a simple weighted average of the current observation _x<sub>t</sub>_ and the previous smoothed output _s<sub>t-1</sub>_. 

You might wonder why this is called exponential smoothing, but this will become evident if you expand the above equation by substituting the defining equation for simple exponential smoothing back into itself 



<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image9.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image9.png "image_tooltip")


In other words, as time passes the smoothed statistic s<sub>t</sub> becomes the weighted average of a greater and greater number of the past observations x<sub>t−n</sub>, and the weights assigned to previous observations are in general proportional to the terms of the geometric progression {1, (1 − α), (1 − α)<sup>2</sup>, (1 − α)<sup>3</sup>, ...}. A geometric progression is the discrete version of an exponential function, so this is where the name for this smoothing method originated.

The smoothing factor applied to α here is something of a misnomer, as larger values of α actually reduce the level of smoothing, and with α = 1 the output series is just the same as the original series (with lag of one time unit). Simple exponential smoothing is easily applied, and it produces a smoothed signal as soon as two observations are available.

The effect of exponential smoothing of an accelerometer signal obtained during walking is shown in Figure 3. You can now start to see the distinct steps much more cleanly, and you can even count them quite easily by eye. At this point, you might even be considering different possible algorithms that can automatically extract steps from the smoothed signal. Not bad for a simple smoothing algorithm!



<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image10.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image10.png "image_tooltip")


<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image11.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image11.png "image_tooltip")


_Figure 56: (left) accelerometer signal during walking without smoothing (right) after exponentially weighted smoothing with smoothing = 6 (i.e. _α = ⅙).

To see exponential averaging in practice, check out the demo in [2]. Try changing the smoothing parameter, and see its effect on the signal (the smoothing parameter is 1/α, so larger smoothing means smaller α). 


## Median Filtering

When the noise appears like sudden spikes in the data (also referred to as salt-and-pepper noise), then the moving average and exponential smoothing methods are not the best methods. An example is shown below, where the noise pattern comprises sharp spikes in the data. Exponential smoothing will remove noise, but has two issues. First, it averages some of the peaks in the data and they don’t quite have the same amplitude. Second, you will notice that the averaging causes a time lag in the peaks i.e. the peaks are shifted slightly to the right of the original peak. 



<p id="gdcalert12" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image12.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert13">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image12.png "image_tooltip")


_Figure 7: Exponential smoothing vs Median filtering. Median filtering is better for removing spikes in the signal (salt-and-pepper noise) compared to exponential smoothing._

One solution to this issue is to use median filtering. The median filter operates over sliding windows as with moving average and exponential smoothing, but computes the median over each window rather than the average. If the input accelerometer signal is: x =  x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, … x<sub>n</sub> , the output of the median filter is:

 _s<sub>1</sub>_ = median(x<sub>1</sub> , x<sub>2</sub> , x<sub>3</sub>)

 _s<sub>2</sub>_ = median(x<sub>2</sub> , x<sub>3</sub> , x<sub>4</sub>)

 _s<sub>3</sub>_ = median(x<sub>3</sub> , x<sub>4</sub> , x<sub>5</sub>)

  …

 _s<sub>n-2</sub>_ = median(x<sub>n-2</sub> , x<sub>n-1</sub> , x<sub>n</sub>)

Because they are so simple to implement and understand, time-domain smoothing is often the first methods tried when faced with a problem. These work exceedingly well in practice, so in many cases you can stop here. But knowing a little bit about other approaches can help you be considerably more effective for sensor signals, and will separate you from your peers. So, let us move on to discuss a very powerful technique for noise removal --- frequency-domain smoothing (or filtering).


# Frequency-domain Filtering

We have discussed how to remove time-domain noise, now let us turn to noise in the frequency domain. 


## How frequency domain filtering works

A long time ago, French scientist and mathematician Jean Baptiste Fourier (1768–1830) proved the mathematical fact that any periodic waveform can be expressed as the sum of an infinite set of sine waves. The frequencies of these sine waves must be integer multiples of some period. An example of this observation is shown in Figure 4. You take two periodic sine waves, add them up, and you get a complicated looking curve. The inverse is also true. You can take any time-series pattern and break it down into a weighted sum of sinusoidal waves.



<p id="gdcalert13" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image13.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert14">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image13.png "image_tooltip")


_Figure 11:  What happens if we add a number of sine waves together, with some weights for each wave? We end up with a complicated waveform that is the summation of the individual waves. _

What does all of this have to do with smoothing signals? A whole lot as it turns out. The main idea is that noise in these waveforms are often concentrated in some frequencies, and not in others. For example, take the case of the accelerometer walking data in Figure 1. The rate at which you walk is typically one or two steps a second; even if you run, the step rate is a few steps a second. So the frequency of interest is only a few Hz.  Similarly, in the case of ECG, the useful frequencies of the electrical signals in the heart are between 0.5 - 150 Hz. In both cases, the frequencies of interest are limited to a relatively small range.

Here’s the magic: _once you convert a signal to a weighted sum of sinusoidals, you can just remove all the sinusoidals whose periods are outside the range that you expect, and what you are left with is a much cleaner signal! _This core idea is that by converting data from the time-domain (which we normally look at) to the frequency domain (which is this new way of viewing data as sinusoidals), we can more easily distinguish the useful data from noise and remove the noise.


## Types of Frequency-domain Filters



<p id="gdcalert14" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image14.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert15">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image14.png "image_tooltip")


_Figure 11: Types of frequency-domain filters_

Figure 11 shows four types of frequency-domain filters that are commonly used in practice:



* **Low-pass filter**: A low-pass filter passes signals with frequency lower than a certain cutoff frequency and attenuates (i.e. reduces the effect of) signals that are higher than the cutoff frequency. An example where a low-pass filter is used is to remove baseline variations in an ECG signal
* **High-pass filter**: A high-pass filter passes signals with frequency higher than a cutoff frequency and attenuates signals that are lower than the cutoff. An example where a high-pass filter is used is to remove hand shaking and external vibrations from an ECG signal.
* **Bandpass filter**: A bandpass filter allows signals between certain frequencies to pass through but attenuates signals outside this band. An example of use of a bandpass filter is to look at frequencies corresponding to normal walking from an accelerometer signal.
* **Notch filter**: A notch filter attenuates the signal within a very small band but lets the other frequencies go through unaltered. An example of use of a notch filter is to remove powerline interference from an ECG signal.

In practice, one has to be careful about how to use the above filters. In many practical situations, removing frequencies abruptly causes unwanted artifacts in the signal. For example, some of you might have seen a ringing sound when you listen to percussion instruments in a concert. This topic is more involved and you can learn these in more advanced classes.


## ECG Noise Removal

A classic example of how these frequency domain filters are used for noise removal is in the case of ECG filtering, so let us discuss how this works. Figure 8 shows an example of the raw ECG data and the filtered ECG data that we would like to extract from it. There are three sources of noise in the ECG data shown in this picture:



<p id="gdcalert15" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image15.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert16">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image15.png "image_tooltip")


_Figure 8: (top) ECG signal with baseline wander, powerline interference, and other high-frequency noise, (bottom) filtered ECG signal. _

**Baseline Wander**: Baseline wander is a low-frequency component present in the ECG system which causes the signal to “wander” off from the actual ECG waveform. This is due to offset voltages in the electrodes, due to periodic breathing, and due to body movement. This noise can cause problems in the analysis of the ECG waveform. As you can see in Figure 8, baseline wander is a slowly oscillating waveform, with frequency much lower than the ECG signal that we are interested in. So, intuitively, it can be removed by using a high-pass filter with an appropriately chosen cutoff to remove the baseline wander while letting through the ECG waveform of interest.

**Powerline Noise**: The frequency of alternating current in the electrical mains is typically around 50-60Hz. Since this is in the frequency range of the ECG signal that we are interested in, it appears as a significant source of noise that can disrupt any measurement that we wish to make. This noise can be clearly seen in the ECG figure below. The blue curve is the measured ECG signal which has periodic variations of the power line on top of the actual ECG signal in red.  Power-line noise can be  removed from the ECG signal by implementing a notch filter at 50/60Hz.



<p id="gdcalert16" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image16.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert17">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image16.png "image_tooltip")


_Figure 9: (red) ECG signal without powerline noise, and (blue) ECG signal with powerline noise._

**High frequency Noise**: Various other electronic equipment in the vicinity of the ECG sensor including pacemakers, mobile phones, and other electronics can interfere with the ECG signal. These sources of noise are high frequency, and need to be removed by an appropriately selected low-pass filter.

If we put these methods together, we get a filtering pipeline that looks like the one below. The ECG signal of interest is between 0.5Hz to 150Hz, so we can remove baseline wander by having a high-pass filter with a cutoff of 0.5Hz, and we can remove high frequency noise by having a low-pass filter with a cutoff of 150Hz. This leaves us with powerline interference, which we can remove with a notch filter with a 50Hz cutoff.



<p id="gdcalert17" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image17.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert18">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image17.png "image_tooltip")


_Figure 10: ECG filtering pipeline comprising several frequency-domain filters to cutoff low frequency baseline wander, high frequency RF noise and narrow frequency powerline noise. _

Conclusion

I hope that this chapter gave you a glimpse of how to remove noise from raw sensor data and extract clean signals for further processing. While the filtering methods described are not comprehensive, you should be able to handle the vast majority of noise observed in sensor signals using these techniques. I would like to highlight two take-away messages from this section. The first is that effective noise removal is the foundation for any analytics that you wish to perform with sensor data. In practice, it is often important that you try to identify the source and type of noise in the signal, since that will allow you to remove the noise more effectively. The second take-away is that any method that you use for removing noise can come with some unwanted artifacts that you may have to deal with in later stages of analysis. So, make sure that you know the advantages and disadvantages of the filtering approaches that you are using before you start using them in your data processing.


# References

[1] [Smoothing data with low pass filters](http://justinvoss.com/2011/11/07/smoothing-data-with-low-pass-filters/)

[2] [Frame-rate independent low pass filter ](http://phrogz.net/js/framerate-independent-low-pass-filter.html)

[3] [Matlab Arduino Tutorial: Filtering noise from acceleration data](http://www.youtube.com/watch?v=TeKk3DjN_gs)

[4] [The Scientist and Engineer’s Guide to Signal Processing](http://www.analog.com/en/content/scientist_engineers_guide/fca.html)

[5] [A numerical tour of signal processing](https://www.ceremade.dauphine.fr/~peyre/numerical-tour/)

[6] <span style="text-decoration:underline;">Physical activity sensor data</span>

[7] [Acceleration/Vibration Noise Measurement](http://www.sensorsmag.com/sensors/acceleration-vibration/noise-measurement-8166)

[8] [Quadcopter: Accelerometer Data Filtering](http://philstech.blogspot.com/2012/04/quadcopter-accelerometer-data-filtering.html)

[9] [ECG Digital Filtering](http://joachimbehar.comuv.com/ECG_tuto_1.php)

[10] [Techniques for accurate ECG signal processing](http://www.eetimes.com/document.asp?doc_id=1278571)

[11] [Kionix - Accelerometer Errors](http://kionixfs.kionix.com/en/document/AN012%20Accelerometer%20Errors.pdf)
