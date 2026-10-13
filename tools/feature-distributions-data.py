"""Builds the data for ch4/feature-distributions.html: for each activity, 4-second windows pooled across several people,
the features of every window, the sampled values of |a| and of each axis (for the value histograms), and one example window.

Sources (as in tools/spot-the-difference-data.py)
  uci    : UCI HAR, phone at the waist; 8 subjects × 4 non-overlapping windows, stitched from the 50 % overlapping windows
  recofit: RecoFit, sensor on the forearm; 8 people × 4 non-overlapping windows from each person's longest set
  pocket : the chapter 3 phone-in-pocket recording (one person, 10 s; windows every 0.5 s), for walking vs running only

Features match the page: mean of each axis, standard deviation / minimum / dominant frequency of |a|, peaks per second and
average peak height (find_peaks on |a| smoothed over ±0.1 s, prominence 1 m/s², 15 samples apart), mean and standard
deviation of |ω| where there is a gyroscope.

Usage: python3 tools/feature-distributions-data.py   (writes tools/feature-distributions-data.json)
"""
import json, pathlib, pickle, re
import numpy as np
from scipy.signal import find_peaks

HERE = pathlib.Path(__file__).resolve().parent
VIZ = HERE.parent
DATA = VIZ.parent / "CS328-Notebooks" / "data"
G, FS, WN = 9.81, 50, 200
PEOPLE, PER = 8, 4


def features(a, g):
    m = np.linalg.norm(a, axis=1)
    X = np.abs(np.fft.rfft(m - m.mean())) * 2 / len(m)
    f = np.fft.rfftfreq(len(m), 1 / FS)
    band = (f >= 0.3) & (f <= 8)
    fdom = float(f[band][X[band].argmax()]) if X[band].max() >= 0.3 else 0.0
    sm = np.convolve(m, np.ones(11), "same") / np.convolve(np.ones_like(m), np.ones(11), "same")
    pk, _ = find_peaks(sm, distance=15, prominence=1.0)
    out = {"mx": a[:, 0].mean(), "my": a[:, 1].mean(), "mz": a[:, 2].mean(), "std": m.std(), "min": m.min(), "freq": fdom,
           "rate": len(pk) / (WN / FS), "height": float(sm[pk].mean()) if len(pk) else 0.0}
    if g is not None:
        w = np.linalg.norm(g, axis=1)
        out.update({"wmean": w.mean(), "wstd": w.std()})
    return {k: round(float(v), 3) for k, v in out.items()}


def pack(wins, people):
    """wins: list of (a[200,3] in m/s², g[200,3] or None)"""
    feats = [features(a, g) for a, g in wins]
    allA = np.concatenate([a for a, _ in wins])[::8]                     # every 8th sample is enough for a histogram
    # the example: the window whose spread of |a| is the median, so the trace looks like a typical person
    order = np.argsort([w["std"] for w in feats]); a0, g0 = wins[int(order[len(order) // 2])]
    rec = {"people": people, "n": len(wins), "f": {k: [w[k] for w in feats] for k in feats[0]},
           "vals": {"m": [round(float(v), 2) for v in np.linalg.norm(allA, axis=1)], **{c: [round(float(v), 2) for v in allA[:, i]] for i, c in enumerate("xyz")}},
           "ex": {"a": [[round(float(v), 2) for v in a0[:, i]] for i in range(3)]}}
    if g0 is not None:
        rec["ex"]["w"] = [round(float(v), 3) for v in np.linalg.norm(g0, axis=1)]
    return rec


def one(wins):
    """features of windows from a single person, for the one-person versus many-people comparison"""
    feats = [features(a, g) for a, g in wins]
    return {"n": len(feats), "f": {k: [w[k] for w in feats] for k in feats[0]}}


def uci(label):
    root = DATA / "UCI-HAR" / "UCI HAR Dataset" / "train"
    y = np.loadtxt(root / "y_train.txt", dtype=int)
    subj = np.loadtxt(root / "subject_train.txt", dtype=int)
    sig = {k: np.loadtxt(root / "Inertial Signals" / f"{k}_train.txt") for k in
           ["total_acc_x", "total_acc_y", "total_acc_z", "body_gyro_x", "body_gyro_y", "body_gyro_z"]}
    wins, used, i, solo = [], [], 0, None
    # one subject's longest stretch of this activity, windows every 0.5 s
    j = 0
    while j < len(y):
        k = j
        while k < len(y) and y[k] == label and subj[k] == subj[j]: k += 1
        if k - j >= 30 and solo is None:
            run = {kk: np.concatenate([v[j + 2 * t] for t in range((k - j) // 2)]) for kk, v in sig.items()}
            a = np.column_stack([run[f"total_acc_{c}"] for c in "xyz"]) * G
            g = np.column_stack([run[f"body_gyro_{c}"] for c in "xyz"])
            solo = one([(a[o:o + WN], g[o:o + WN]) for o in range(0, min(len(a) - WN + 1, 32 * 25), 25)])
        j = max(k, j + 1)
    while i < len(y) - 14 and len(used) < PEOPLE:
        if subj[i] not in used and all(y[k] == label and subj[k] == subj[i] for k in range(i, i + 14)):
            run = {k: np.concatenate([v[i + 2 * j] for j in range(7)]) for k, v in sig.items()}   # 7 half-overlapped windows tile 896 samples
            a = np.column_stack([run[f"total_acc_{c}"] for c in "xyz"]) * G
            g = np.column_stack([run[f"body_gyro_{c}"] for c in "xyz"])
            wins += [(a[o:o + WN], g[o:o + WN]) for o in range(0, PER * WN, WN)]
            used.append(int(subj[i])); i += 14
        else:
            i += 1
    return dict(pack(wins, len(used)), one=solo)


def recofit(db, name):
    wins, used = [], set()
    longest = max(db[name], key=lambda s: len(s[3]))
    solo = one([(longest[3][o:o + WN] * G, longest[2][o:o + WN]) for o in range(100, min(len(longest[3]) - WN + 1, 100 + 32 * 25), 25)])
    for s in sorted(db[name], key=lambda s: -len(s[3])):
        if s[0] in used or len(s[3]) < 100 + PER * WN:
            continue
        used.add(s[0])
        a, g = s[3] * G, s[2]
        wins += [(a[o:o + WN], g[o:o + WN]) for o in range(100, 100 + PER * WN, WN)]
        if len(used) >= PEOPLE:
            break
    return dict(pack(wins, len(used)), one=solo)


def pocket(act):
    s = (VIZ / "ch3" / "activity-traces.html").read_text()
    body = re.search(r"const TRACES = (\{.*?\n\});", s, re.S).group(1)
    tr = json.loads(re.sub(r"(\w+):", r'"\1":', body))[act]
    a = np.column_stack([tr["x"], tr["y"], tr["z"]]).astype(float)
    return pack([(a[o:o + WN], None) for o in range(0, len(a) - WN + 1, 25)], 1)


def main():
    db = pickle.load(open(DATA / "RecoFit-Exercises" / "all_exercises_6axis.pkl", "rb"))
    R = {}
    for k, lab in {"Walking": 1, "Upstairs": 2, "Downstairs": 3, "Sitting": 4, "Standing": 5, "Lying": 6}.items():
        R["uci:" + k] = uci(lab)
    for k in ["Walking", "Running"]:
        R["pk:" + k] = pocket(k)
    for name in ["Bicep Curl", "Squat (arms in front of body, parallel to ground)", "Lateral Raise", "Jumping Jacks",
                 "Lunge (alternating both legs, weight optional)", "Walk", "Squat Jump", "Burpee", "Plank", "Side Plank Left side",
                 "Crunch", "Sit-up (hands positioned behind head)", "Jump Rope", "Running (treadmill)", "Rowing machine",
                 "Elliptical machine", "Kettlebell Swing", "Medicine Ball Slam", "Fast Alternating Punches",
                 "Lawnmower (right arm)", "Lawnmower (left arm)"]:
        R["rf:" + name] = recofit(db, name)
    (HERE / "feature-distributions-data.json").write_text(json.dumps(R, separators=(",", ":")))
    print(len(R), "activities,", round(len(json.dumps(R)) / 1024), "KB;", {k: (v["people"], v["n"]) for k, v in R.items()})


if __name__ == "__main__":
    main()
