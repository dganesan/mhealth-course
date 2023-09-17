---
layout: default
title: Step Counting
nav_order: 2
parent: Mobile Sensing &amp; Analytics
has_children: true
usemathjax: true
description: "Step Counter"
---
## Designing a Pedometer and Calorie Counter
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}
---

## Chapter 2: Designing a Pedometer and Calorie Counter

Pedometers or step counters are now popular as an everyday exercise progress monitor and motivator. The increasing popularity of these devices can be attributed to several reasons. First, many people are known to overestimate their level of activity, hence these devices can provide more reliable feedback to an individual about how much or little they move during the day. Second, they provide instant and constant feedback about activity levels, making it possible to “gamify” by providing credits for every step an individual takes. Third, they can encourage individuals to compete with themselves in getting fit and losing weight. 


#### Part 1: Introduction to Step Counting [[notes](ch2-intro.html)] [[slides](https://drive.google.com/file/d/1joGfgzsmzz55cQmhGwQvQImarvfrmdbF/view?usp=drive_link)]
We start by explaining what an accelerometer on a phone or fitness band measures when you walk, and why it is convenient to work with the magnitude signal.

<iframe width="320" height="240" src="https://www.youtube.com/embed/t40WyxXuwKk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Part 2: Sources of noise [[slides](https://drive.google.com/file/d/1joGfgzsmzz55cQmhGwQvQImarvfrmdbF/view?usp=drive_link)]
We describe some of the real-world challenges in accurately estimating the number of steps including common sources of noise such as the device moving around, differences across people in terms of their gait patterns, and others.

<iframe width="320" height="240" src="https://www.youtube.com/embed/UExjHCCgd1g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Part 3: Designing a Step Counter [[notes](ch2-stepcounter.html)] [[slides](https://drive.google.com/file/d/1joGfgzsmzz55cQmhGwQvQImarvfrmdbF/view?usp=drive_link)]
This part describes how you design a step counter and how you detect the number of steps 

<iframe width="320" height="240" src="https://www.youtube.com/embed/PYQMBEYPgoo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Part 4: Calorie Tracking [[notes](ch2-calories.html)] [[slides](https://drive.google.com/file/d/1joGfgzsmzz55cQmhGwQvQImarvfrmdbF/view?usp=drive_link)]
Step counters not only tell us the number of steps but also a (rough) estimate of the number of calories burned. We now look at how we can map from steps to calories.

<iframe width="320" height="240" src="https://www.youtube.com/embed/Y7vNEf2ksB8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<!---

#### Part 3: Distinguishing horizontal vs vertical movements [[slides](https://drive.google.com/file/d/1joGfgzsmzz55cQmhGwQvQImarvfrmdbF/view?usp=drive_link)]
We look at a more complex problem where we have to distinguish between horizontal braking and acceleration while driving in a vehicle versus vertical changes in acceleration due to walking. This can let us distinguish between acceleration due to steps versus due to moving in a vehicle

<iframe width="320" height="240" src="https://www.youtube.com/embed/eV0htD4r4ZI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Notebook 1: Design a step counter (Assignment)

--->