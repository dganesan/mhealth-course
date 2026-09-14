# CS328 companion visualization conventions (settled with the instructor on chapter 1)

You are building step-through, animated HTML pages that accompany one chapter of the CS328
course notes (Mobile Health Sensing and Analytics, UMass Amherst). Read this whole file before
writing anything.

## Scope rule (most important)
- Cover ONLY what the chapter's course notes actually discuss. Do not introduce concepts,
  figures, or terminology that are not in the chapter text. The instructor rejected pages that
  went beyond the notes (e.g. a frequency response of the moving average when the notes never
  mention it). If the notes only show a time series, show only a time series.
- Match the chapter's own figures: same signals, parameters, data sets, axis units and wording.
  The chapter's figure-generation scripts (if present) are the source of truth for parameters.
- Pick 3 to 5 concepts per chapter where MOTION or INTERACTION teaches something a static
  figure cannot: a window sliding, a threshold moving, a tree splitting, a boundary changing as
  a parameter moves, data flowing through a pipeline stage by stage. Skip concepts that are
  just text, tables or code.

## Reference page
Copy the structure, CSS tokens, fonts, control bar, keyboard handling, hash deep-links, hover
tooltip and step machinery from the reference page:
`<VIZ>/ch1/smoothers-in-motion.html` (VIZ is given in your task). Read it fully first. Reuse its
CSS verbatim where possible. Key facts of the template:
- White ground, Helvetica Neue bold titles (#222), grey #666 secondary, Menlo for math/numbers,
  matplotlib-like axes: thin grey grid, mono tick labels, axis titles in 12 px sans.
- Colors: blue #2a78d6 (primary series / controls accent), green #1baf7a, violet #4a3aa7,
  orange-red #eb6834 (noise, errors, "bad"), grey #8f8f8f raw input, dashed #444 clean target.
  Categorical classes: blue, orange-red, green, violet in that order.
- Footer line "CS328 · <Chapter title>" left, "n / N" counter right (mono).
- Every page: `<title>` first, then `<style>`, no doctype/html/head/body tags (the wrapper adds
  them), no external dependencies at all, everything inline, seeded PRNG for reproducibility.

## Page anatomy (each step of a page)
1. `<h1>` title in a plain academic register: informative, not sensational. Examples:
   "Sampling rate and the Nyquist criterion", "Effect of window length on the peak count",
   "Splitting a node on one feature". Never "Why X can't Y", "The price of", "wagon wheel".
   A mono tag chip after the title shows live parameter values, e.g. `w = 9 · α = 0.2`.
2. ONE short, plain sentence under the title saying what the animation shows. It must read
   instantly: ≤ 15 words, one idea, no semicolons, no metaphors, no stacked clauses, no numbers
   unless essential, no "watch how the rhythm sits on every axis" style phrasing.
   GOOD: "How the angle of the phone affects the reading on each axis."
   GOOD: "Filtering the magnitude to keep only walking frequencies."
   BAD:  "Ten seconds from a phone in a pocket: the walking rhythm is on every axis, each offset
         by its share of gravity." (the instructor rejected this: it confuses more than it explains)
   It runs the full slide width (`.head p { max-width: none; color:#444; font-size: clamp(15px,1.6vw,18px) }`)
   and must never wrap to a second line (≈ 110 characters max).
   No other prose anywhere: no notes, no takeaways, no formula blocks below the chart.
   Essential formulas go inside the SVG as a short Menlo annotation.
   Axes must end where the data ends: never an x-axis to 10 s when the trace stops at 6 s.
   Prefer a drawing (e.g. a phone that rotates) to a sentence when the concept is physical.
3. The chart: a real SVG drawn to scale with axes, ticks, units, viewBox about 1200×600–700, filling
   the slide. Every panel with more than one series has a CONVENTIONAL LEGEND drawn at step
   entry (before any animation), on a white 90%-opacity rounded rect, colored swatches, ink text,
   listing every series that will appear in that step. Never rely on end-of-trace labels alone.
4. Footer.

## Controls (the "dials")
- Control bar under the slide with this CSS (copy it):
  .bar { display:flex; flex-wrap:wrap; gap:12px 24px; align-items:center; padding:14px 18px; border:1px solid var(--rule); border-radius:6px; background:#f6f7f9; font-size:14px; color:var(--ink); }
  .group { display:flex; align-items:center; gap:8px; }
  .group label { font-size:13px; font-weight:700; color:var(--ink); }
  .val { font-family:var(--mono); font-size:14px; font-weight:700; color:var(--ma); min-width:5ch; }
  button, select { font:inherit; font-size:14px; color:var(--ink); background:#fff; border:1px solid #9a9a9a; border-radius:5px; padding:7px 13px; cursor:pointer; }
  button.primary { background:var(--ma); color:#fff; border-color:var(--ma); min-width:88px; font-weight:700; }
  input[type=range] { accent-color:var(--ma); width:200px; height:30px; cursor:pointer; }
- Order: Prev / Play / Next / Restart / Reset dials, then the parameter dials, then Speed.
- Every slider has a bold blue mono `.val` readout beside it. Labels sentence-case, dark.
- Speed menu: very slow / slow / normal / fast / instant. Animations must be meaningful at
  "very slow" (about 4× slower than normal) for lecture use.
- DIALS PERSIST: a step may set a control only if the user has not touched it (per-control
  dirty flag set on input/change). Play, Restart and re-entering a step always compute from the
  live dial values. Never disable a control. "Reset dials" clears the flags, re-applies the
  step's presets and restarts the step. Moving a dial mid-step redraws immediately at the
  current progress (no forced replay).
- Keyboard: → finishes the current animation or advances, ← goes back, space plays/pauses,
  r restarts. Clicking the slide advances. URL hash `#n` opens step n.

## Wording
- "60 Hz powerline noise", never "hum". "ECG", never "real ECG". "notch (band-stop)" at first
  mention. Use function names from the notes (lfilter, filtfilt, find_peaks, rolling(...)).
- Numbers shown to students should be large and on one line; no wrapping, no index clutter.

## Data
- Prefer the chapter's real data sets under
  `~/Library/CloudStorage/GoogleDrive-deepak.ganesan@gmail.com/My Drive/Teaching/CS328-Master/CS328-Notebooks/data/`
  (inline a small slice as a JS array, rounded, ≤ ~80 KB per page). Otherwise a seeded synthetic
  signal that matches the chapter figure.
- A SciPy-verified Butterworth/FFT library exists at `<SHARED>/butter.js`
  (window.Butter = { butter(N, cutoffHz|[lo,hi], fs, 'lowpass'|'highpass'|'bandpass'|'bandstop') -> sos,
  sosfilt, sosfiltfilt, sosFreqz, rfftMag }). Inline its text if you need filtering.
- Python 3 with numpy/pandas/scipy is available for exporting data slices and for checking
  numbers against the chapter figures.

## Process for each page
1. Write the page to `<VIZ>/chN/<slug>.html` where slug is short kebab-case.
2. Verify JS syntax with node: extract each <script> body and `new Function(body)`.
3. Take ONE headless Chrome screenshot of an animated step early in its animation:
   wrap a copy with `<!doctype html><html><head><meta charset="utf-8"></head><body>…</body></html>`
   in a temp file and run
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --window-size=1280,1000 --virtual-time-budget=900 --screenshot=<out.png> "file://<tmp>#<step>"
   Look at it, make ONE fix pass, take one more screenshot only if the fix was structural.
   Do not loop.
4. Do NOT publish artifacts. Do not touch other chapters' folders.

## Deliverable back to the coordinator
A short report: for each page, the file name, a title (≤ 6 words, will be a one-line link),
the list of step titles, the dials, the data used, and any caveat. Keep it under 40 lines.
