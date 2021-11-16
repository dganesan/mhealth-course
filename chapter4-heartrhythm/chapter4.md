---
layout: default
title: Heart Rhythm Sensing
nav_order: 4
parent: Mobile Sensing &amp; Analytics
has_children: true
usemathjax: true
description: "Health Rhythm Sensing"
---
## Sensing Heart Rhythm
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}
---

## Chapter 2: Measuring the activity of the human heart 

Cardiovascular disease — pathologies of the heart, blood vessels and the vascular system of the brain — claims more lives than anything else, accounting for nearly one-third of deaths worldwide. Those deaths are projected to increase until at least 2030. Thanks to advances in wearable health-tracking devices, people can monitor their heart rhythms much easier now. Wrist-worn smartwatches and fitness monitors or wearables have been widely adopted by consumers and are currently gaining increased attention by researchers for their potential contribution to digital measurement of heart rhythm, thereby providing early detection of irregularities as well as to provide a more holistic view of daily cardiovascular health.

#### Part 1:  How can we measure activity of the human heart [[slides 1-9](https://drive.google.com/file/d/0Bw0KEeNzOgzFLWpBMnV5cHNCYzA/view?usp=sharing&resourcekey=0-wID7JSxr1I4jmcmoAzvfgw)]

Interestingly, there are many different ways of monitoring the human heart, ranging from wristworn fitness bands that largely use optical heart rate monitors to conventional Electrocardiograms and Stethoscopes, to more recent development of contactless monitoring devices that use Ballistocardiography or Mechanocardiography.

<iframe width="320" height="240" src="https://www.youtube.com/embed/1rDx3fZXjXQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Part 2: Photoplethysmography (PPG) [[notes](ch4-ppg.html)] [[slides 10-25](https://drive.google.com/file/d/0Bw0KEeNzOgzFLWpBMnV5cHNCYzA/view?usp=sharing&resourcekey=0-wID7JSxr1I4jmcmoAzvfgw)]

The most common method for monitoring heart rhythm with a wearable device is by using an optical heart rate sensor that uses Photoplethysmography (PPG) i.e. collecting pulse rate or volumetric changes in blood flow that act as a surrogate for heart rate (HR).

<iframe width="320" height="240" src="https://www.youtube.com/embed/t00XbGrDQAk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Part 3: PPG Noise sources [[notes](ch4-ppg.html)] [[slides 26-35](https://drive.google.com/file/d/0Bw0KEeNzOgzFLWpBMnV5cHNCYzA/view?usp=sharing&resourcekey=0-wID7JSxr1I4jmcmoAzvfgw)]

PPG is challenging to analyze in real-world environments since the optical signal can be noisy (due to device movement, environment lighting), and also the signal quality can vary across individuals (due to skin tone, underlying health conditions that lead to lower than normal blood flow).

<iframe width="320" height="240" src="https://www.youtube.com/embed/OG6PixUimm4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Part 4: Estimating Heart rate and Breathing rate from PPG [[notes](ch4-ecg-ppg-analysis.html)] [[slides 36-40](https://drive.google.com/file/d/0Bw0KEeNzOgzFLWpBMnV5cHNCYzA/view?usp=sharing&resourcekey=0-wID7JSxr1I4jmcmoAzvfgw)]

We look at how one can extract heart rate and breathing rate from PPG using techniques very similar to those that you used for counting steps. After removing noise and baseline wander from a PPG signal, count the peaks to get a rough estimate of heart rate. Then look for the variation in the peak height to obtain information about breathing rate.

<iframe width="320" height="240" src="https://www.youtube.com/embed/yaiwkc_YeVQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Part 5: Estimating Oxygen Saturation from PPG [[slides 41-44](https://drive.google.com/file/d/0Bw0KEeNzOgzFLWpBMnV5cHNCYzA/view?usp=sharing&resourcekey=0-wID7JSxr1I4jmcmoAzvfgw)]

The PPG signal can also be used to measure blood oxygenation; this functionality is used in the Apple Watch 6 but is also the principle behind Pulse Oximeters. Oxygen saturation measurement has become particularly important during pandemic since it is one of the early signals that an individual may be infected. any people with COVID-19 have low levels of oxygen in their blood, even when they feel well. Low oxygen levels can also be an early warning sign that medical care is needed. 

<iframe width="320" height="240" src="https://www.youtube.com/embed/jGXN7MGAJn8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Part 6: Phonocardiography, Ballistocardiography and Mechanocardiography [[slides 41-44](https://drive.google.com/file/d/0Bw0KEeNzOgzFLWpBMnV5cHNCYzA/view?usp=sharing&resourcekey=0-wID7JSxr1I4jmcmoAzvfgw)]

To conclude this lesson, we provide a brief overview of other ways of measuring heart rhythm. While ECG uses electrodes and PPG uses optical sensors, there are other ways of measuring the human heart. Bedside sleep monitors can use radar signals to measure the ballistic signals of the heart and calculate heart rate; mattresses with sensitive pressure sensors can do the same.

<iframe width="320" height="240" src="https://www.youtube.com/embed/13II_ibiQig" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Notebook 1:  (Assignment)

