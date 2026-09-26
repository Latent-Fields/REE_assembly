"""Paired analysis: w3rel (OFF, committed) vs w3relon (ON, this probe).
Pre-registration: chip-20260926-w3-reliability-with-ema-fix (Z_w3relon.md).
ASCII output only. No scipy assumed available.
"""
import glob, json, math, sys

OFF_DIR = "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/w3rel/results"
ON_DIR = "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/w3relon/results"
SEEDS = list(range(901, 916))


def load(dirpath, tag, seed):
    f = "%s/%s_s%d.json" % (dirpath, tag, seed)
    return json.load(open(f))


def row_from(d):
    r = d["arms"]["real"]
    return {
        "seed": d["seed"], "gate_a": r["gate_a"], "post_disc4": r["post"]["disc4_h1"],
        "post_k": r["post"]["k"], "B0": d["B0"], "INIT": d["init"]["disc4_h1"],
        "guard_pass": all(v == "PASS" for v in r["guard"].values()),
        "frozen_ok": r["frozen_retained_unchanged_after_post"],
        "stratum": r["hazard_stratum_A1"].get("stratum", "CANNOT_DETERMINE"),
    }


def wilson(k, n, z=1.96):
    if n == 0:
        return (None, None, None)
    p = k / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = (z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / denom
    return (p, max(0.0, center - half), min(1.0, center + half))


def cohend(a, b):
    if len(a) < 2 or len(b) < 2:
        return None
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    va = sum((x - ma) ** 2 for x in a) / (len(a) - 1)
    vb = sum((x - mb) ** 2 for x in b) / (len(b) - 1)
    sp = math.sqrt(((len(a) - 1) * va + (len(b) - 1) * vb) / (len(a) + len(b) - 2))
    if sp == 0:
        return None
    return (ma - mb) / sp


def paired_ci(diffs, z=1.96):
    n = len(diffs)
    m = sum(diffs) / n
    if n < 2:
        return (m, None, None)
    var = sum((x - m) ** 2 for x in diffs) / (n - 1)
    se = math.sqrt(var / n)
    return (m, m - z * se, m + z * se)


# ---- canary check ----
print("=== CANARY (OFF re-run, must match committed w3rel bit-exact) ===")
canary_ok = True
for f in sorted(glob.glob("%s/CANARY_s*.json" % ON_DIR)):
    d_new = json.load(open(f))
    seed = d_new["seed"]
    d_old = load(OFF_DIR, "W3REL", seed)
    for arm in ("real", "shuf"):
        for key in ("disc4_h1", "k"):
            v_new = d_new["arms"][arm]["post"][key]
            v_old = d_old["arms"][arm]["post"][key]
            same = (v_new == v_old) if isinstance(v_old, int) else abs(v_new - v_old) < 1e-12
            print("  seed=%d arm=%s post.%s new=%s old=%s %s" % (
                seed, arm, key, v_new, v_old, "MATCH" if same else "MISMATCH"))
            canary_ok = canary_ok and same
    b0_same = abs(d_new["B0"] - d_old["B0"]) < 1e-12
    print("  seed=%d B0 new=%s old=%s %s" % (seed, d_new["B0"], d_old["B0"], "MATCH" if b0_same else "MISMATCH"))
    canary_ok = canary_ok and b0_same
print("CANARY RESULT: %s" % ("PASS (bit-exact)" if canary_ok else "FAIL -- CANNOT_DETERMINE"))

if not canary_ok:
    print("\nVERDICT: CANNOT_DETERMINE (canary failed -- ON results not trustworthy against OFF baseline)")
    sys.exit(0)

# ---- paired ON vs OFF over the 15 registered seeds ----
off_rows, on_rows = {}, {}
missing = []
for s in SEEDS:
    try:
        off_rows[s] = row_from(load(OFF_DIR, "W3REL", s))
    except FileNotFoundError:
        missing.append(("OFF", s))
    try:
        on_rows[s] = row_from(load(ON_DIR, "ON", s))
    except FileNotFoundError:
        missing.append(("ON", s))

have = sorted(set(off_rows) & set(on_rows))
print("\n=== PAIRED SEEDS AVAILABLE: %d / %d (%s) ===" % (len(have), len(SEEDS), have))
if missing:
    print("MISSING: %s" % missing)

n_off_pass = sum(1 for s in have if off_rows[s]["gate_a"])
n_on_pass = sum(1 for s in have if on_rows[s]["gate_a"])
p_off, lo_off, hi_off = wilson(n_off_pass, len(have))
p_on, lo_on, hi_on = wilson(n_on_pass, len(have))
print("\nOFF pass: %d/%d = %.3f  Wilson [%.3f, %.3f]" % (n_off_pass, len(have), p_off, lo_off, hi_off))
print("ON  pass: %d/%d = %.3f  Wilson [%.3f, %.3f]" % (n_on_pass, len(have), p_on, lo_on, hi_on))

# McNemar-style 2x2
both_pass = sum(1 for s in have if off_rows[s]["gate_a"] and on_rows[s]["gate_a"])
off_pass_on_miss = sum(1 for s in have if off_rows[s]["gate_a"] and not on_rows[s]["gate_a"])
off_miss_on_pass = sum(1 for s in have if not off_rows[s]["gate_a"] and on_rows[s]["gate_a"])
both_miss = sum(1 for s in have if not off_rows[s]["gate_a"] and not on_rows[s]["gate_a"])
net_flips = off_miss_on_pass - off_pass_on_miss
print("\nMcNemar 2x2 (rows=OFF, cols=ON):")
print("               ON-pass   ON-miss")
print("  OFF-pass     %5d     %5d" % (both_pass, off_pass_on_miss))
print("  OFF-miss     %5d     %5d" % (off_miss_on_pass, both_miss))
print("  net flips (OFF-miss->ON-pass minus OFF-pass->ON-miss) = %d" % net_flips)
per_seed_flip = [(s, off_rows[s]["gate_a"], on_rows[s]["gate_a"]) for s in have if off_rows[s]["gate_a"] != on_rows[s]["gate_a"]]
print("  flipped seeds (seed, off_pass, on_pass): %s" % per_seed_flip)

# disc4 paired delta
diffs = [on_rows[s]["post_disc4"] - off_rows[s]["post_disc4"] for s in have]
m, lo, hi = paired_ci(diffs)
print("\nMean disc4 delta (ON - OFF), paired: %.4f  95%% CI [%s, %s]  (n=%d)" % (
    m, ("%.4f" % lo) if lo is not None else "NA", ("%.4f" % hi) if hi is not None else "NA", len(diffs)))
print("Per-seed disc4 (seed off->on delta):")
for s in have:
    print("  %4d  %.4f -> %.4f  delta=%+.4f  off_pass=%s on_pass=%s" % (
        s, off_rows[s]["post_disc4"], on_rows[s]["post_disc4"],
        on_rows[s]["post_disc4"] - off_rows[s]["post_disc4"], off_rows[s]["gate_a"], on_rows[s]["gate_a"]))

# B0 disc4 ON vs OFF (secondary)
b0_diffs = [on_rows[s]["B0"] - off_rows[s]["B0"] for s in have]
m_b0, lo_b0, hi_b0 = paired_ci(b0_diffs)
print("\nB0 disc4 mean delta (ON - OFF), paired: %.4f  95%% CI [%s, %s]" % (
    m_b0, ("%.4f" % lo_b0) if lo_b0 is not None else "NA", ("%.4f" % hi_b0) if hi_b0 is not None else "NA"))

# B0 disc4 still separating under ON?
on_pass_b0 = [on_rows[s]["B0"] for s in have if on_rows[s]["gate_a"]]
on_miss_b0 = [on_rows[s]["B0"] for s in have if not on_rows[s]["gate_a"]]
d_on = cohend(on_pass_b0, on_miss_b0)
print("\nUnder ON: B0 disc4 pass_mean=%s miss_mean=%s d=%s %s" % (
    ("%.4f" % (sum(on_pass_b0)/len(on_pass_b0))) if on_pass_b0 else "NA",
    ("%.4f" % (sum(on_miss_b0)/len(on_miss_b0))) if on_miss_b0 else "NA",
    ("%.3f" % d_on) if d_on is not None else "CANNOT_DETERMINE (empty group)",
    ("SEPARATING" if (d_on is not None and abs(d_on) >= 0.8) else ("no" if d_on is not None else ""))))

# Verdict
print("\n=== VERDICT ===")
if n_on_pass > n_off_pass and net_flips >= 3:
    verdict = "RAISES"
elif n_on_pass < n_off_pass and (off_pass_on_miss - off_miss_on_pass) >= 3:
    verdict = "LOWERS"
else:
    verdict = "NO-EFFECT"
print("pass rate OFF=%.3f ON=%.3f net_flips=%+d -> %s" % (p_off, p_on, net_flips, verdict))

json.dump({
    "have": have, "n_off_pass": n_off_pass, "n_on_pass": n_on_pass,
    "p_off": p_off, "p_on": p_on, "wilson_off": [lo_off, hi_off], "wilson_on": [lo_on, hi_on],
    "mcnemar": {"both_pass": both_pass, "off_pass_on_miss": off_pass_on_miss,
                "off_miss_on_pass": off_miss_on_pass, "both_miss": both_miss, "net_flips": net_flips},
    "flipped_seeds": per_seed_flip,
    "disc4_delta_mean": m, "disc4_delta_ci": [lo, hi],
    "b0_delta_mean": m_b0, "b0_delta_ci": [lo_b0, hi_b0],
    "b0_separating_under_on": (abs(d_on) >= 0.8) if d_on is not None else None,
    "b0_cohend_on": d_on,
    "verdict": verdict,
}, open("%s/PAIRED_SUMMARY.json" % ON_DIR, "w"), indent=1)
