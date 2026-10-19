const $ = id => document.getElementById(id);
const NS = 'http://www.w3.org/2000/svg';
function el(parent, tag, attrs, text) {
  const e = document.createElementNS(NS, tag);
  for (const k in attrs) e.setAttribute(k, attrs[k]);
  if (text != null) e.textContent = text;
  parent.appendChild(e); return e;
}
const mono = { 'font-family': 'Menlo, monospace', fill: '#666' };

// ------------------------------------------------------------ data: windows from HAR-data/dataset1.csv, [mean of a_y, std dev of a_y, class]
// TRAIN is the chapter figure's 150-window subsample; TEST is the remaining windows of the same three activities
const DATA = __DATA__;
const TRAIN = DATA.train, TEST = DATA.test;
const CLS = ['Walking', 'Upstairs', 'Downstairs'], CCOL = ['#2a78d6', '#eb6834', '#1baf7a'];
const FN = ['mean', 'std dev'];
const BOX = [8.4, 10.3, 0.5, 8];   // the feature plane drawn: mean from 8.4 to 10.3, std dev from 0.5 to 8

// ------------------------------------------------------------ CART with gini impurity, binary splits at midpoints, as scikit-learn does
function gini(ct) { const n = ct[0] + ct[1] + ct[2]; if (!n) return 0; return 1 - ct.reduce((s, c) => s + (c / n) ** 2, 0); }
function growTree(data, { maxDepth = 99, minSplit = 2, minLeaf = 1 } = {}) {
  const X = data.map(d => [d[0], d[1]]), y = data.map(d => d[2]);
  function make(idx, depth, box) {
    const ct = [0, 0, 0]; idx.forEach(i => ct[y[i]]++);
    const node = { n: idx.length, ct, depth, box, imp: gini(ct), cls: ct.indexOf(Math.max(...ct)) };
    if (node.imp === 0 || node.n < minSplit || node.n < 2 * minLeaf || depth >= maxDepth) return node;
    let best = null;
    for (let f = 0; f < 2; f++) {
      const s = idx.slice().sort((a, b) => X[a][f] - X[b][f]), lc = [0, 0, 0], rc = ct.slice();
      for (let j = 0; j < s.length - 1; j++) {
        lc[y[s[j]]]++; rc[y[s[j]]]--;
        if (X[s[j]][f] === X[s[j + 1]][f]) continue;
        const nl = j + 1, nr = s.length - nl;
        if (nl < minLeaf || nr < minLeaf) continue;
        const avg = (nl * gini(lc) + nr * gini(rc)) / s.length;
        if (!best || avg < best.avg - 1e-12) best = { f, t: (X[s[j]][f] + X[s[j + 1]][f]) / 2, avg };
      }
    }
    if (!best || node.imp - best.avg <= 1e-12) return node;
    node.split = { f: best.f, t: best.t };
    const L = idx.filter(i => X[i][best.f] <= best.t), R = idx.filter(i => X[i][best.f] > best.t), bl = box.slice(), br = box.slice();
    if (best.f === 0) { bl[1] = best.t; br[0] = best.t; } else { bl[3] = best.t; br[2] = best.t; }
    node.kids = [make(L, depth + 1, bl), make(R, depth + 1, br)];
    return node;
  }
  return make(data.map((_, i) => i), 0, [-1e9, 1e9, -1e9, 1e9]);
}
const predict = (n, x) => { while (n.kids) n = x[n.split.f] <= n.split.t ? n.kids[0] : n.kids[1]; return n.cls; };
const leavesOf = n => n.kids ? n.kids.flatMap(leavesOf) : [n];
const depthOf = n => n.kids ? 1 + Math.max(...n.kids.map(depthOf)) : 0;
const acc = (t, data) => data.filter(d => predict(t, d) === d[2]).length / data.length;
const params = p => ({ maxDepth: p.depth >= 15 ? 99 : p.depth, minSplit: p.split, minLeaf: p.leaf });

// ------------------------------------------------------------ the feature plane: each leaf's region shaded in its class colour, the splits drawn, the windows on top
function plane(g, tree, X0, Y0, X1, Y1, opts = {}) {
  const xs = v => X0 + (v - BOX[0]) / (BOX[1] - BOX[0]) * (X1 - X0), ys = v => Y1 - (v - BOX[2]) / (BOX[3] - BOX[2]) * (Y1 - Y0);
  const clip = b => [Math.max(b[0], BOX[0]), Math.min(b[1], BOX[1]), Math.max(b[2], BOX[2]), Math.min(b[3], BOX[3])];
  const s = opts.s || 1;
  if (tree) leavesOf(tree).forEach(l => { const b = clip(l.box); if (b[1] > b[0] && b[3] > b[2]) el(g, 'rect', { x: xs(b[0]), y: ys(b[3]), width: xs(b[1]) - xs(b[0]), height: ys(b[2]) - ys(b[3]), fill: CCOL[l.cls], opacity: 0.26 }); });
  for (let v = 8.5; v <= BOX[1] + 1e-9; v += 0.5) { el(g, 'line', { x1: xs(v), x2: xs(v), y1: Y0, y2: Y1, stroke: '#000', 'stroke-opacity': 0.06, 'stroke-width': 1.3 }); el(g, 'text', { x: xs(v), y: Y1 + 26 * s, 'text-anchor': 'middle', 'font-size': 19 * s, ...mono }, v.toFixed(1)); }
  for (let v = 1; v <= BOX[3] + 1e-9; v += 1) { el(g, 'line', { x1: X0, x2: X1, y1: ys(v), y2: ys(v), stroke: '#000', 'stroke-opacity': 0.06, 'stroke-width': 1.3 }); el(g, 'text', { x: X0 - 10, y: ys(v) + 7, 'text-anchor': 'end', 'font-size': 19 * s, ...mono }, v); }
  (function lines(n) { if (!n.kids) return; const b = clip(n.box), t = n.split.t;
    el(g, 'line', Object.assign(n.split.f === 0 ? { x1: xs(t), x2: xs(t), y1: ys(b[2]), y2: ys(b[3]) } : { x1: xs(b[0]), x2: xs(b[1]), y1: ys(t), y2: ys(t) }, { stroke: '#333', 'stroke-width': 1.6 }));
    n.kids.forEach(lines); })(tree || {});
  el(g, 'rect', { x: X0, y: Y0, width: X1 - X0, height: Y1 - Y0, fill: 'none', stroke: '#666', 'stroke-width': 1.5 });
  (opts.points || TRAIN).forEach(d => { if (d[0] < BOX[0] || d[0] > BOX[1] || d[1] < BOX[2] || d[1] > BOX[3]) return; el(g, 'circle', { cx: xs(d[0]), cy: ys(d[1]), r: (opts.r || 5.5) * s, fill: CCOL[d[2]], stroke: '#fff', 'stroke-width': 1.2 }); });
  if (!opts.noAxes) {
    el(g, 'text', { x: (X0 + X1) / 2, y: Y1 + 58 * s, 'text-anchor': 'middle', 'font-size': 21 * s, fill: '#444' }, 'mean of aᵧ');
    el(g, 'text', { x: X0 - 52 * s, y: (Y0 + Y1) / 2, 'text-anchor': 'middle', 'font-size': 21 * s, fill: '#444', transform: `rotate(-90 ${X0 - 52 * s} ${(Y0 + Y1) / 2})` }, 'std dev of aᵧ');
  }
}
// the class key, as one row above the figure rather than on top of it
function legend(g, x, y, shading = true) {
  CLS.forEach((c, k) => { const xx = x + k * 165; el(g, 'circle', { cx: xx + 8, cy: y - 7, r: 8, fill: CCOL[k], stroke: '#fff' }); el(g, 'text', { x: xx + 24, y, 'font-size': 21, fill: '#444' }, c); });
  if (!shading) return;
  el(g, 'rect', { x: x + 520, y: y - 16, width: 22, height: 18, fill: '#888', opacity: 0.3 });
  el(g, 'text', { x: x + 550, y, 'font-size': 21, fill: '#444' }, 'shading: what the tree predicts');
}

// ------------------------------------------------------------ the tree itself: labelled boxes while it is small, a skeleton of dots once it is too big to read
function treeDiagram(g, tree, X, Y, W, H) {
  const L = leavesOf(tree).length, D = depthOf(tree), slot = W / L, lvl = D ? Math.min((H - 70) / D, 130) : 0, big = L > 10;
  const edges = el(g, 'g', {}), nodes = el(g, 'g', {});
  function place(n, first) {
    let cx;
    if (!n.kids) cx = X + (first + 0.5) * slot;
    else { const a = place(n.kids[0], first), b = place(n.kids[1], first + leavesOf(n.kids[0]).length); cx = (a + b) / 2;
      [a, b].forEach(k => el(edges, 'line', { x1: cx, y1: Y + n.depth * lvl, x2: k, y2: Y + (n.depth + 1) * lvl, stroke: '#9a9a9a', 'stroke-width': big ? 1 : 2 })); }
    const cy = Y + n.depth * lvl;
    if (big) el(nodes, 'circle', { cx, cy, r: Math.max(2, Math.min(6, slot / 3)), fill: n.kids ? '#9a9a9a' : CCOL[n.cls] });
    else if (n.kids) {
      const bw = Math.min(170, slot * 1.6);
      el(nodes, 'rect', { x: cx - bw / 2, y: cy - 26, width: bw, height: 52, rx: 8, fill: '#e8f1fd', stroke: '#2a78d6', 'stroke-width': 2 });
      el(nodes, 'text', { x: cx, y: cy - 3, 'text-anchor': 'middle', 'font-size': 19, 'font-weight': 700, fill: '#1d5fae' }, `${FN[n.split.f]} ≤ ${n.split.t.toFixed(2)}`);
      el(nodes, 'text', { x: cx, y: cy + 19, 'text-anchor': 'middle', 'font-size': 16, fill: '#444' }, `n = ${n.n}`);
    } else {
      const bw = Math.min(140, slot - 8);
      el(nodes, 'rect', { x: cx - bw / 2, y: cy - 26, width: bw, height: 52, rx: 8, fill: '#fff' });   // opaque under the tint, so edges do not show through
      el(nodes, 'rect', { x: cx - bw / 2, y: cy - 26, width: bw, height: 52, rx: 8, fill: CCOL[n.cls] + '33', stroke: CCOL[n.cls], 'stroke-width': 2 });
      if (bw > 100) el(nodes, 'text', { x: cx, y: cy - 3, 'text-anchor': 'middle', 'font-size': 17, 'font-weight': 700, fill: CCOL[n.cls] }, CLS[n.cls]);
      el(nodes, 'text', { x: cx, y: bw > 100 ? cy + 19 : cy + 6, 'text-anchor': 'middle', 'font-size': 16, fill: '#444' }, `n = ${n.n}`);
    }
    return cx;
  }
  place(tree, 0);
}
const statLine = (t, test) => `depth ${depthOf(t)} · ${leavesOf(t).length} leaves · training accuracy ${acc(t, TRAIN).toFixed(2)}` + (test ? ` · test accuracy ${acc(t, TEST).toFixed(2)}` : '');
