# Revision notes: bringing each chapter in line with lecture use

Chapters 1–3 were revised on 2026-09-23 so the pages follow the order in which the material is taught, show the idea rather than write it out, and stay legible when projected. Chapters 4–11 have not yet had this pass. This file records what the pass consists of, so it can be repeated one chapter at a time. The page-building rules themselves are in `CONVENTIONS.md`, which was updated in the same session.

## The pass, per chapter

**1. Order and titles follow the course notes.**
- Read the section and subsection headings of `../CourseNotes/chapters/chapterN.tex` and order the pages the way the notes (and the lecture) introduce the material. A page that uses an idea must come after the page that introduces it. In chapter 2, the placement page plotted magnitude before magnitude was introduced, so the magnitude page moved first.
- Where a page does not fit its chapter's argument, consider moving it rather than deleting it. The accelerometer vs gyroscope page moved from chapter 3 to chapter 2. Keep visually interesting pages.
- Index titles: short, about 30 characters or fewer, so the index boxes do not wrap. Chapter 1 titles are the reference. Avoid titles that imply something false about earlier pages; "Trying it on real data" implied the earlier pages were not real.
- Update the `<title>` of each page to match its index entry, and the footer to match the chapter name in the index (chapter names use "&").
- Do not edit the course notes. The site may diverge from the notes' headings and order.

**2. Remove text that the lecture says aloud.**
- Subtitles: remove, almost without exception. Keep one only if the instructor asks for it.
- Tag chip after the title: keep only live dial values, live results (`found 57 · true 45`), or context the viewer needs (`phone in hip pocket`). Remove sampling rates, durations, sample counts, start offsets, dataset names.
- A fact the viewer must not miss goes into the chart as a short annotation next to the thing it describes, not as a subtitle. Examples: the distance step of `ch2/find-peaks-criteria.html` marks "distance = 40 samples = 0.40 s × 100 Hz" on a kept peak; `ch2/step-count-distance.html` places "the sensor reports raw units, not m/s²" directly under the prominence box of the code line.
- Do not repeat the same name several times on one slide (title, figure label, plot title).

**3. Units.** Every numeric parameter needs a visible unit or scale: seconds vs samples for distance and width, m/s² vs raw sensor units for height and prominence, σ when a threshold is a multiple of the standard deviation. Label unitless axes honestly ("sensor units").

**4. Legibility at 1920×1080** (sizes are in `CONVENTIONS.md`).
- Legends at the top right, and only for panels with more than one series. Drop legend entries that a label strip already names. If a top-right legend would cover a trace, raise the top of the y-range to make headroom.
- No label may cross a line or trace: move it (e.g. the h1–h6 labels now sit below their stems) and give SVG labels a white halo (`paint-order: stroke; stroke: #fff; stroke-width: 6px`).
- Check for text overflowing boxes, tick labels colliding with axis titles, and y-axis titles running into tick labels in short panels (increase `ylx`).
- Hide a control on steps where it does nothing (`visibility: hidden`, so the bar does not jump).

**5. Consistency across pages.** Pages that show the same data should show the same numbers, or say why they differ.

## Workflow

1. Edit in this Drive folder.
2. Run `node tools/check-pages.mjs chN/*.html`. It walks every step forward and back, prints each step's title, tag and subtitle, and reports exceptions. Add `SHOTS=<dir>` to save a screenshot of every finished step, and look at them. A syntax check is not enough: an earlier bulk edit broke 11 pages at runtime.
3. After any edit shared across pages, run the harness on every page it touched.
4. Publish: copy into `../Github/mhealth-course` (branch `gh-pages`) with `rsync -a --exclude .git --exclude .DS_Store`. Never use `--delete`: the repository holds `.nojekyll` and `.gitignore`, which this folder does not. For a moved or removed page, `git rm` the old path. Then commit and push.

## Open items from chapters 1–3

- `ch3`: the feature tables disagree. `pipeline-stages.html` computes variance on the band-passed signal (no mean column); `windows-to-features.html` computes mean and variance on the raw magnitude. Same 12 s trace, different numbers.
- `ch3/bandpass-preprocessing.html`, last step: the 4 Hz vs 5 Hz comparison is almost invisible on walking. The notes justify 5 Hz for running, so a running trace would show it.
- `ch3/pipeline-stages.html`, stage 1: the y-range was raised to 30 for legend headroom, but the ticks stop at 20.
- `ch3/activity-traces.html`: walking-upstairs y flat-tops near 19.6 m/s² (probably the sensor's 2 g limit). Students may ask.
- `ch2/activity-signals.html`, swimming: the traces flatten at the top of the plot, which suggests the y-range is too small.
- `ch2/find-peaks-criteria.html`: height and prominence are bare numbers on a unitless "amplitude" axis. Decided to leave as is; the known-steps page explains the scaling.
- `ch2/step-count-distance.html`: the first step's heading still reads "Checking the count against 45 known steps"; only the index and tab title became "Verifying Counted Steps".

## Chapter 4: starting points

Headings in the notes: Time-domain features (mean for sitting vs standing; mean not enough for standing vs walking; variance; gyroscope adds information; when time-domain features run out), Frequency-domain features (dominant frequency; signal energy; tracking dominant frequency over time), Similarity-based features (how the alignment is computed), Learned features: embeddings.

Current pages, in index order: Sliding-Window Time Features, Spectrum and Dominant Frequency, Dynamic Time Warping. The harness shows:
- `time-domain-features.html`, step 2 subtitle "The window mean fails to separate standing from walking." (remove); tag `w = 2 s (100 samples) · step = 0.5 s` (keep the live window and step, consider dropping the sample count).
- `frequency-domain-features.html`: tags carry `(N = 250)`; Δf may be worth keeping because it is the frequency resolution being taught.
- `dtw-alignment.html`, step 2 subtitle "Each cell adds its local cost to the cheapest of its three neighbours." (remove or turn into an in-chart annotation); last step tag has `25 Hz`.
- No page covers the gyroscope subsection, signal energy, or embeddings. That is fine unless a visual would help the lecture.
- Index titles and `<title>`s differ (e.g. "Sliding-Window Time Features" vs `<title>Time-Domain Features`); align them.
