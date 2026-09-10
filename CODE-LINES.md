# Live code lines + fit-to-screen (instructor approved on ch1/smoothers-in-motion.html)

Reference implementation: `<VIZ>/ch1/smoothers-in-motion.html` (read it: search for `.code`, `id="code"`, `code:` and `$('code')`).

## 1. Live code line (only where the chapter notes have a matching code block)
- Under the subtitle add `<pre class="code" id="code" hidden></pre>`.
- CSS (copy verbatim):
  .code { margin: 8px 0 0; font-family: var(--mono); font-size: clamp(13px, 1.35vw, 16px); color: var(--ink); background: #f4f6f9; border: 1px solid var(--rule); border-radius: 5px; padding: 6px 12px; white-space: pre; overflow-x: auto; }
  .code[hidden] { display: none; }
  .code .p { color: var(--ma); font-weight: 700; }
- Each step may carry `code:` (string, or a function returning a string if it must read live dial values). Where the head is rendered add:
  `$('code').hidden = !code; $('code').innerHTML = code || '';` (resolve functions first). Re-render the head whenever a dial changes so the numbers update live.
- The code line is the ACTUAL call from the chapter's notes (read the chapter .tex: look for lstlisting / minted / verbatim blocks) with the values that the dials currently hold. Wrap every value a dial controls in `<b class="p">…</b>`. Keep it to one line (≤ ~100 chars); if the notes' call is longer, show only the call that matters for the step.
- Steps that do not correspond to a code call get no code line (leave it hidden). Do NOT invent code that is not in the notes; if a page has no matching code anywhere in the chapter, skip the code line for that page entirely and say so in the report.
- Remove any older pseudo-code annotation inside the SVG that now duplicates the code line.

## 2. Fit on one screen without scrolling (every page, code or not)
- `svg.chart { display:block; width:100%; height:auto; max-height: calc(100vh - 360px); overflow:visible; }` (if the page uses a different selector for its main SVG, apply the same max-height rule to it; if there are two stacked SVGs, cap their combined height instead).
- `.slide { min-height: 0; }` (remove any fixed min-height).
- Control bar must fit on ONE row at 1280 px width where possible: sliders `width:150px` (`input[type=range]`), keep labels short (≤ 2 words), no extra text in the bar. If a page has 5+ dials it may wrap to two rows; that is acceptable.
- Verify with a headless screenshot at `--window-size=1280,720`: the whole page (slide + bar) must be visible with no clipping. Take one at 1920,1080 too and glance at it.

## 3. Process
- node `new Function(scriptBody)` syntax check after editing.
- One screenshot per page at 1280x720 (step 2 or the first step with code), one fix pass.
- Report ≤ 40 lines: per page, the code lines added (or "no code in notes"), and confirmation that it fits at 1280x720.
