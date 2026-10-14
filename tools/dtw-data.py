"""Builds the data for ch4/dtw-alignment.html.

rowing   : the chapter's two rowing recordings (UCI Daily and Sports Activities, activity a17, right-arm gyroscope magnitude at
           25 Hz, three strokes of subject p4, fast, and subject p6, slow), read from the earlier version of the page so the
           numbers match the book's figure.
templates: one recording of each of a few other activities by subject p4, right-arm gyroscope magnitude, the same length as
           p4's rowing, lightly smoothed (moving average over 3 samples), for the "DTW distance as a feature" step.

Usage: python3 tools/dtw-data.py   (writes tools/dtw-data.json)
"""
import json, pathlib, re
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
VIZ = HERE.parent
DSA = VIZ.parent / "CS328-Notebooks" / "data" / "UCI-DSA" / "data"
OTHERS = {"a14": "cross trainer", "a15": "cycling", "a18": "jumping", "a12": "running on a treadmill"}


def gyro_mag(act, subj, seg="s01"):
    x = np.loadtxt(DSA / act / subj / f"{seg}.txt", delimiter=",")
    g = x[:, 12:15]                      # right arm unit: columns 9-17, its gyroscope x y z are 12-14
    m = np.linalg.norm(g, axis=1)
    return np.convolve(m, np.ones(3) / 3, "same")


def main():
    src = (VIZ / "backups" / "dtw-alignment-2026-10-14.html").read_text()
    row = {k: json.loads(re.search(k + r" = (\[.*?\]);", src).group(1)) for k in ["ROW_A", "ROW_B"]}
    n = len(row["ROW_A"])
    out = {"fs": 25, "rowA": row["ROW_A"], "rowB": row["ROW_B"],
           "templates": {name: [round(float(v), 3) for v in gyro_mag(a, "p4")[:n]] for a, name in OTHERS.items()}}
    (HERE / "dtw-data.json").write_text(json.dumps(out, separators=(",", ":")))
    print(n, "samples per template;", list(out["templates"]))


if __name__ == "__main__":
    main()
