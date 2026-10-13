"""Builds the data for ch4/window-to-feature.html and ch4/good-feature.html.

window-to-feature: 30 s of acceleration magnitude (m/s², 50 Hz) from one UCI HAR subject (phone at the waist) while standing
                   and while walking, stitched from the dataset's 50 % overlapping 2.56-s windows.
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
    """30 s of one subject's activity: windows j, j+2, j+4, ... tile the recording with no overlap"""
    need = -(-N // 128)
    for j in range(len(y) - 2 * need):
        if subj[j] == who and all(y[j + k] == label and subj[j + k] == who for k in range(2 * need)):
            a = np.column_stack([np.concatenate([c[j + 2 * t] for t in range(need)])[:N] for c in acc]) * G
            return [round(float(v), 2) for v in np.linalg.norm(a, axis=1)]
    return None


def main():
    y, subj, acc = uci_runs()
    # the first subject with 30 s of both standing (5) and walking (1)
    for who in sorted(set(subj)):
        st, wk = stretch(y, subj, acc, 5, who), stretch(y, subj, acc, 1, who)
        if st and wk:
            break
    D = json.loads((HERE / "feature-distributions-data.json").read_text())
    keys = ["uci:Walking", "uci:Upstairs", "rf:Jump Rope", "rf:Running (treadmill)"]
    feats = {k: {"people": D[k]["people"], "many": D[k]["f"], "one": D[k]["one"]["f"]} for k in keys}
    out = {"trace": {"subject": int(who), "standing": st, "walking": wk}, "feats": feats}
    (HERE / "feature-basics-data.json").write_text(json.dumps(out, separators=(",", ":")))
    print("subject", who, round(len(json.dumps(out)) / 1024), "KB")


if __name__ == "__main__":
    main()
