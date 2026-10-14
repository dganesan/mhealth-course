"""Builds the data for ch4/window-to-feature.html and ch4/good-feature.html.

window-to-feature: 30 s of acceleration magnitude (m/s², 50 Hz) from one UCI HAR subject (phone at the waist) while walking
                   and while walking downstairs, stitched from the dataset's 50 % overlapping 2.56-s windows; and, for the
                   same subject and all six activities, two features per half-overlapping window (the mean of y and the
                   standard deviation of the magnitude) for the feature-plane step.
good-feature     : the per-window feature values of three pairs, for one person and pooled over 8 people, taken from
                   tools/feature-distributions-data.json (run tools/feature-distributions-data.py first).

Usage: python3 tools/feature-basics-data.py   (writes tools/feature-basics-data.json)
"""
import json, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent.parent / "CS328-Notebooks" / "data"
G, N = 9.81, 1500                         # 30 s at 50 Hz


def uci_runs():
    root = DATA / "UCI-HAR" / "UCI HAR Dataset" / "train"
    y = np.loadtxt(root / "y_train.txt", dtype=int)
    subj = np.loadtxt(root / "subject_train.txt", dtype=int)
    acc = [np.loadtxt(root / "Inertial Signals" / f"total_acc_{c}_train.txt") for c in "xyz"]
    return y, subj, acc


def stretch(y, subj, acc, label, who):
    """30 s of one subject's activity (x y z in m/s²): windows j, j+2, j+4, ... tile the recording with no overlap"""
    need = -(-N // 128)
    for j in range(len(y) - 2 * need):
        if subj[j] == who and all(y[j + k] == label and subj[j + k] == who for k in range(2 * need)):
            return np.column_stack([np.concatenate([c[j + 2 * t] for t in range(need)])[:N] for c in acc]) * G
    return None


def mag(a):
    return [round(float(v), 2) for v in np.linalg.norm(a, axis=1)]


def main():
    y, subj, acc = uci_runs()
    # subject 6: walking downstairs is clearly more vigorous than walking, and all six activities have 30 s
    who = 6
    run = {n: stretch(y, subj, acc, lab, who) for lab, n in
           [(1, "walking"), (2, "walking upstairs"), (3, "walking downstairs"), (4, "sitting"), (5, "standing"), (6, "lying down")]}
    plane = {n: [[round(float(a[o:o + 200, 1].mean()), 2), round(float(np.linalg.norm(a[o:o + 200], axis=1).std()), 3)]
                 for o in range(0, N - 200 + 1, 100)] for n, a in run.items()}
    D = json.loads((HERE / "feature-distributions-data.json").read_text())
    keys = ["uci:Walking", "uci:Upstairs", "rf:Jump Rope", "rf:Running (treadmill)"]
    feats = {k: {"people": D[k]["people"], "many": D[k]["f"], "one": D[k]["one"]["f"]} for k in keys}
    out = {"trace": {"subject": who, "walking": mag(run["walking"]), "downstairs": mag(run["walking downstairs"])}, "plane": plane, "feats": feats}
    (HERE / "feature-basics-data.json").write_text(json.dumps(out, separators=(",", ":")))
    print("subject", who, round(len(json.dumps(out)) / 1024), "KB")


if __name__ == "__main__":
    main()
