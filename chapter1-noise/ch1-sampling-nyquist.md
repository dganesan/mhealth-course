---
layout: default
title: Sampling and Nyquist
parent: Data Smoothing
grand_parent: Mobile Sensing &amp; Analytics
nav_order: 3
usemathjax: true
description: "Chapter 1"
---
## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}
---

<!-- Custom JavaScript files set in YAML front matter -->
<td>
<svg id="fourWaveAlias" class="svgWithText" width="485" height="300" style="padding: 5px; margin-left: 110px; margin-right: 145px;"></svg>
<script type="text/javascript" src="js/four_wave_alias.js"></script>
<div class="controls">
	<br/>
	<label for=waveAliasSlider>Sampling Period</label><br/>
	<input type=range min=1 max=4 value=4 id=waveAliasSlider step=1 oninput="updateAliasRate(value);"
	onMouseDown="startSetAliasRate();" onMouseUp="endSetAliasRate();">
</div>
</td>
