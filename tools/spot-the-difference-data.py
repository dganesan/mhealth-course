"""Builds the recordings for ch4/spot-the-difference.html: 10 s of 50 Hz accelerometer (m/s², x y z) and,
where the source has it, gyroscope (rad/s, x y z) for every activity used by a pair.

Sources
  pocket : the chapter 3 phone-in-hip-pocket traces, read from ch3/activity-traces.html (accelerometer only)
  uci    : UCI HAR, phone at the waist (total acceleration in g, body gyroscope in rad/s); 50 % overlapping
           128-sample windows are stitched back into a continuous 10 s run of one subject
  recofit: RecoFit, sensor on the forearm (accelerometer in g, gyroscope in rad/s), from all_exercises_6axis.pkl

Usage: python3 tools/spot-the-difference-data.py   (writes tools/spot-the-difference-data.json)
"""
import json, pathlib, pickle, re
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
VIZ = HERE.parent
DATA = VIZ.parent / "CS328-Notebooks" / "data"
G = 9.81
N = 500                                    # 10 s at 50 Hz


def pocket():
    s = (VIZ / "ch3" / "activity-traces.html").read_text()
    body = re.search(r"const TRACES = (\{.*?\n\});", s, re.S).group(1)
    tr = json.loads(re.sub(r"(\w+):", r'"\1":', body)) if not body.lstrip("{").lstrip().startswith('"') else json.loads(body)
    return {k: {"a": [v["x"][:N], v["y"][:N], v["z"][:N]]} for k, v in tr.items()}


def uci(label, subject_pick=0):
    root = DATA / "UCI-HAR" / "UCI HAR Dataset" / "train"
    y = np.loadtxt(root / "y_train.txt", dtype=int)
    subj = np.loadtxt(root / "subject_train.txt", dtype=int)
    sig = {k: np.loadtxt(root / "Inertial Signals" / f"{k}_train.txt") for k in
           ["total_acc_x", "total_acc_y", "total_acc_z", "body_gyro_x", "body_gyro_y", "body_gyro_z"]}
    found = []
    for i in range(len(y) - 8):
        # windows i, i+2, i+4, i+6 are contiguous halves apart, so they tile 512 samples with no overlap
        idx = [i + 2 * j for j in range(4)]
        if all(y[k] == label and subj[k] == subj[i] for k in range(i, i + 7)):
            found.append(idx)
            if len(found) > subject_pick:
                break
    idx = found[subject_pick]
    run = {k: np.concatenate([v[j] for j in idx])[:N] for k, v in sig.items()}
    return {"a": [list(run[f"total_acc_{c}"] * G) for c in "xyz"], "g": [list(run[f"body_gyro_{c}"]) for c in "xyz"]}


def recofit_db():
    return pickle.load(open(DATA / "RecoFit-Exercises" / "all_exercises_6axis.pkl", "rb"))


def segment(entry, start_s=2.0):
    _, reps, g, a = entry
    o = int(start_s * 50)
    if len(a) < o + N:
        o = max(0, len(a) - N)
    return {"a": [list(a[o:o + N, k] * G) for k in range(3)], "g": [list(g[o:o + N, k]) for k in range(3)]}


def long_sets(sets, min_s=12):
    return [s for s in sets if len(s[3]) >= min_s * 50]


def typical(sets):
    """the set whose overall movement (std of |a|) is closest to the median of its exercise"""
    ss = long_sets(sets)
    v = [np.std(np.linalg.norm(s[3], axis=1)) for s in ss]
    return ss[int(np.argsort(v)[len(v) // 2])]


def rate(s):
    return s[1] / (len(s[3]) / 50) if s[1] == s[1] else np.nan   # reps per second; nan when the set has no rep count


def main():
    P = pocket()
    db = recofit_db()
    R = {}
    rec = {}
    for name in ["Bicep Curl", "Squat (arms in front of body, parallel to ground)", "Lateral Raise", "Jumping Jacks",
                 "Jump Rope", "Running (treadmill)", "Plank", "Side Plank Left side", "Rowing machine", "Elliptical machine",
                 "Kettlebell Swing", "Medicine Ball Slam", "Lawnmower (right arm)", "Lawnmower (left arm)", "Fast Alternating Punches",
                 "Lunge (alternating both legs, weight optional)", "Walk", "Squat Jump", "Burpee"]:
        rec[name] = segment(typical(db[name]))
    # the same exercise at two speeds, and the same exercise by two people
    curls = sorted([s for s in long_sets(db["Bicep Curl"]) if rate(s) == rate(s)], key=rate)
    rec["Bicep Curl, slow set"] = segment(curls[0])
    rec["Bicep Curl, fast set"] = segment(curls[-1])
    lat = sorted([s for s in long_sets(db["Lateral Raise"]) if rate(s) == rate(s)], key=rate)
    mid = len(lat) // 2
    a, b = lat[mid], next(s for s in lat[mid + 1:] + lat[:mid][::-1] if s[0] != lat[mid][0])
    rec["Lateral Raise, person A"] = segment(a)
    rec["Lateral Raise, person B"] = segment(b)
    for k, v in rec.items():
        R["rf:" + k] = v
    for k, v in P.items():
        R["pk:" + k] = v
    R["uci:Sitting"] = uci(4)
    R["uci:Lying"] = uci(6)
    rnd = lambda xs, d: [round(float(x), d) for x in xs]
    out = {k: {"a": [rnd(c, 1) for c in v["a"]], **({"g": [rnd(c, 2) for c in v["g"]]} if "g" in v else {})} for k, v in R.items()}
    (HERE / "spot-the-difference-data.json").write_text(json.dumps(out, separators=(",", ":")))
    print(len(out), "recordings,", round(len(json.dumps(out)) / 1024), "KB")
    print("slow curl", round(rate(curls[0]), 2), "reps/s · fast curl", round(rate(curls[-1]), 2), "reps/s · lateral raise subjects", a[0], b[0])


if __name__ == "__main__":
    main()
