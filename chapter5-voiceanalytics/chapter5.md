---
layout: default
title: Vocal Biomarkers
nav_order: 5
parent: Mobile Sensing &amp; Analytics
has_children: true
usemathjax: true
description: "Vocal Biomarkers"
---
## Voice-based Health Analytics
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}
---

## Chapter 5: Voice-based Health Analytics

<iframe width="320" height="240" src="https://www.youtube.com/embed/oL5PbFeFMyY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="320" height="240" src="https://www.youtube.com/embed/IliokKSNuXQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Voice is an extremely useful and important part of health analytics, and an amazing amount of information can be gleaned from recorded audio from a simple microphone. As microphones become more powerful and more ubiquitous, the possibility that computing systems will be able to monitor vocal biomarkers and extract changes in health patterns has exciting possibilities for understanding ourselves and in anticipating problems. 

#### Part 1:  What are some of the useful features we can extract from voice? [[notes](ch5-audiofeatures.html)] [[slides](https://drive.google.com/file/d/0Bw0KEeNzOgzFRm13c3NqREdxTUU/view?usp=sharing&resourcekey=0-m5VIqT4c3JBhd4kykBkIPA)]

We will start with a discussion of useful speech features. In particular, we focus on MFCC features which are closest to human perception of voice including how we perceive frequency and volume. We also discuss other features that can be combined with MFCC to understand emotional content of speech. 

#### Part 2: What health states can be classified with audio biomarkers? [[notes](ch5-audioclassification.html)] [[slides](https://drive.google.com/file/d/0Bw0KEeNzOgzFRm13c3NqREdxTUU/view?usp=sharing&resourcekey=0-m5VIqT4c3JBhd4kykBkIPA)]

We then look at some interesting ways in which voice processing can be used for obtaining measures of health. There are many ways in which audio biomarkers may be used -- for example, should a person undergo further screening for depression or other mental health issues? are the changes in vocal patterns indicative of worsening neurological disease? what is the mood of an individual? is a person stressed? and so on. In this chapter, we will look at some interesting ways in which voice processing can be used for obtaining measures of health. 

###  Notebook 1: Determining Gender from Speech [[html](Chapter5-GenderClassification-Voice.html)] [[ipynb](Chapter5-GenderClassification-Voice.ipynb)]
This notebook tries to identify a voice as male or female, based upon acoustic properties of the voice and speech. The dataset consists of 3,168 recorded voice samples, collected from male and female speakers. The voice samples are pre-processed by analyzing frequency range of 0hz-280hz (human vocal range).
