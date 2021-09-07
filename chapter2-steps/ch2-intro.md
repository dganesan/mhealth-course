---
layout: default
title: Introduction
parent: Chapter 2
nav_order: 1
usemathjax: true
description: "Chapter 2"
---

## Introduction

Pedometers or step counters are now popular as an everyday exercise progress monitor and motivator. The increasing popularity of these devices can be attributed to several reasons. First, many people are known to overestimate their level of activity, hence these devices can provide more reliable feedback to an individual about how much or little they move during the day. Second, they provide instant and constant feedback about activity levels, making it possible to “gamify” by providing credits for every step an individual takes. Third, they can encourage individuals to compete with themselves in getting fit and losing weight. 



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


_				Figure 1: Definition of each axis. _


## Overview

From the characteristics that can be used to analyze running or walking, we choose _acceleration _as the relevant parameter. The three components of motion for an individual (and their related axes) are forward (_roll_), vertical (_yaw_), and side (_pitch_), as shown in Figure 1. The 3-axis accelerometer senses acceleration along its three axes: _x_, _y_, and _z_. The pedometer will be in an unknown orientation, so the measurement accuracy should not depend critically on the relationship between the motion axes and the accelerometer’s measurement axes.



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")


_Figure 2: Walking stages and acceleration pattern_

Let’s think about the nature of walking. Figure 1 depicts a single step, defined as a unit cycle of walking behavior, showing the relationship between each stage of the walking cycle and the change in vertical and forward acceleration. Figure 2 shows a typical pattern of x-, y-, and z- measurements corresponding to vertical, forward, and side acceleration of a  running person. The figure should give you confidence that you’re on the right track - the large spikes corresponding to each step, and the periodic nature of walking/running, suggest that we should be able to detect these patterns.



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")


_Figure 3: Step counting in an ideal situation._

In an ideal situation, you would like to see a signal like shown in Figure 3. One of the axes of the phone is along the direction of gravity, and the steps can be clearly observed in the signal.

But Figure 3 is misleading - if you take a few traces with the phone oriented in different ways in your pocket, you will quickly realize that the shape of the x, y, z curves depends on the orientation of the phone! While the figure shows the y-axis acceleration to be the largest, this may not be the case if the x-axis is oriented downward. 



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")


_Figure 4: Accelerometer signal in a real-world situation_

A more realistic signal is shown in Figure 4, where some component of the user acceleration and gravity is present along all three axes. Since acceleration changes as a result of a step can result in changes along all the three axes, so we need to design an _orientation-independent_ algorithm to detect steps. 
