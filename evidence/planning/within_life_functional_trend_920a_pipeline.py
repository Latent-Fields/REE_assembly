#!/usr/bin/env python3
"""Reference implementation of the Section 6 pre-registered pipeline, as run over
the V3-EXQ-920a multi-seed episode log to produce Section 7 of
`within_life_functional_trend_920_lineage_2026-08-14.md`.

Landed as a TRACKED file deliberately: the n=1 pass's reference implementation was
left in a session scratchpad and did not survive, which the parent document flags.

DESCRIPTIVE ONLY. N=8 is not a reliability claim. No p-values are computed anywhere
in this file, by design (Section 6 step 6).

Run:  /opt/local/bin/python3 within_life_functional_trend_920a_pipeline.py
ASCII-only output (CLAUDE.md).
"""
import json
import statistics as st
from collections import Counter
from pathlib import Path

LOG = Path(
    "/Users/dgolden/REE_Working/REE_assembly/evidence/experiments/"
    "v3_exq_920_uncensored_survival_single_life_fishtank/"
    "v3_exq_920_uncensored_survival_single_life_fishtank_20260814T223432Z_episode_log.json"
)

# Section 5 DV set. `benefit_exposure` is NOT recorded by this driver (structurally
# absent, per the 916a recording gap), so resource COUNT is the benefit covariate.
DVS = ["z_goal", "drive", "surprise", "excite", "z_block", "liking",
       "override", "dread", "z_harm_a", "energy"]

# Energy drain is a fixed 0.0015/step in this env, so energy reaches 0 at t=666.
ENERGY_CLOCK_ZERO = 666


def med_iqr(vals):
    if not vals:
        return None
    if len(vals) < 4:
        return (st.median(vals), None, None)
    q = st.quantiles(vals, n=4, method="inclusive")
    return (st.median(vals), q[0], q[2])


def fmt(mi, nd=3):
    if mi is None:
        return "n/a"
    m, lo, hi = mi
    return f"{m:.{nd}f}" if lo is None else f"{m:.{nd}f} [{lo:.{nd}f},{hi:.{nd}f}]"


def pearson(a, b):
    ma, mb = st.mean(a), st.mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    da = sum((x - ma) ** 2 for x in a) ** 0.5
    db = sum((y - mb) ** 2 for y in b) ** 0.5
    return num / (da * db) if da and db else float("nan")


def boundaries(steps):
    """Section 6 step 1. (a) first SUSTAINED resources==0, (b) first energy<=0,
    (c) health milestones. (a) is the pre-registered primary; it does not fire in
    any 920a seed, which is itself a reported finding."""
    n = len(steps)
    nres = [len(s["resources"]) for s in steps]
    energy = [s["energy"] for s in steps]
    health = [s["health"] for s in steps]
    exh = None
    for i in range(n):
        if nres[i] == 0 and all(v == 0 for v in nres[i:]):
            exh = i
            break
    return dict(
        n=n,
        exhaustion=exh,
        energy_collapse=next((i for i in range(n) if energy[i] <= 0.0), None),
        health_lt50=next((i for i in range(n) if health[i] < 0.5), None),
        health_lt10=next((i for i in range(n) if health[i] < 0.1), None),
        res_start=nres[0], res_min=min(nres), res_end=nres[-1],
    )


def windows(b):
    """Regime A = t < (a) if it fires, else (b), else whole life. Thirds + POST."""
    n = b["n"]
    a_end, basis = b["exhaustion"], "resource_exhaustion (pre-registered primary)"
    if a_end is None:
        a_end, basis = b["energy_collapse"], "energy_collapse (primary did not fire)"
    if a_end is None or a_end < 30:
        a_end, basis = n, "whole life (died before either boundary)"
    w = a_end // 3
    out = [("early", 0, w), ("mid", w, 2 * w), ("late-preExh", 2 * w, a_end)]
    if a_end < n:
        out.append(("POST-exh", a_end, n))
    return out, a_end, basis


def familiarity(steps, lo, hi, seen):
    """Section 6 step 3. NOT raw footprint_at_cell. `seen` is carried across
    windows so cumulative-distinct is life-cumulative, not per-window."""
    before = len(seen)
    revisits = 0
    for s in steps[lo:hi]:
        p = tuple(s["pos"])
        if p in seen:
            revisits += 1
        seen.add(p)
    return len(seen), len(seen) - before, revisits / max(1, hi - lo)


def coherence(steps, lo, hi):
    """Section 6 step 4. mode-run length + switch rate. is_committed reported
    separately (expected ~0 -- commitment never engages in a single episode)."""
    modes = [s["mode"] for s in steps[lo:hi]]
    if not modes:
        return None, None, None
    runs, cur = [], 1
    for i in range(1, len(modes)):
        if modes[i] == modes[i - 1]:
            cur += 1
        else:
            runs.append(cur)
            cur = 1
    runs.append(cur)
    switches = sum(1 for i in range(1, len(modes)) if modes[i] != modes[i - 1])
    return st.mean(runs), switches / max(1, len(modes) - 1), max(runs)


def direction(vals):
    if any(v is None for v in vals):
        return "n/a"
    m = [v[0] for v in vals]
    if m[0] > m[1] > m[2]:
        return "down"
    if m[0] < m[1] < m[2]:
        return "up"
    return "non-monotone"


def main():
    doc = json.loads(LOG.read_text())
    seeds = doc["seeds"]
    N = len(seeds)
    per = {}

    print("=== STEP 1: per-seed regime boundaries ===")
    print(f"{'seed':>4}{'life':>6}{'exh':>6}{'eColl':>7}{'h<.5':>6}{'h<.1':>6}"
          f"{'res s/min/end':>15}{'A_end':>7}  basis")
    for sd in seeds:
        steps = sd["life"]["steps"]
        b = boundaries(steps)
        wins, a_end, basis = windows(b)
        per[sd["seed"]] = dict(b=b, wins=wins, a_end=a_end, basis=basis, steps=steps)
        res = f"{b['res_start']}/{b['res_min']}/{b['res_end']}"
        print(f"{sd['seed']:>4}{b['n']:>6}{str(b['exhaustion']):>6}"
              f"{str(b['energy_collapse']):>7}{str(b['health_lt50']):>6}"
              f"{str(b['health_lt10']):>6}{res:>15}{a_end:>7}  {basis}")

    print("\n=== STEP 2-5: Regime-A thirds, median [Q1,Q3] ===")
    for seed, R in per.items():
        print(f"\n-- seed {seed} (A_end={R['a_end']}) --")
        seen = set()
        R["rows"] = []
        head = f"{'win':<12}{'n':>5}"
        show = ["z_goal", "drive", "surprise", "excite", "z_block", "energy"]
        for dv in show:
            head += f"{dv:>22}"
        print(head)
        for name, lo, hi in R["wins"]:
            seg = R["steps"][lo:hi]
            row = {"window": name, "n": len(seg)}
            for dv in DVS:
                row[dv] = med_iqr([s[dv] for s in seg])
            row["n_resources"] = med_iqr([float(len(s["resources"])) for s in seg])
            cum, new, rev = familiarity(R["steps"], lo, hi, seen)
            row.update(cum_cells=cum, new_cells=new, revisit=rev)
            mr, msr, mx = coherence(R["steps"], lo, hi)
            row.update(mode_run=mr, switch_rate=msr, run_max=mx)
            row["committed_frac"] = sum(1 for s in seg if s["is_committed"]) / max(1, len(seg))
            row["zblock_frac"] = sum(1 for s in seg if s["z_block"] > 0.05) / max(1, len(seg))
            row["harm_rate"] = sum(1 for s in seg if s["harm_event"]) / max(1, len(seg))
            R["rows"].append(row)
            line = f"{name:<12}{len(seg):>5}" + "".join(f"{fmt(row[dv]):>22}" for dv in show)
            print(line)
        print(f"{'win':<12}{'cumCell':>8}{'newCell':>8}{'revisit':>8}{'modeRun':>9}"
              f"{'switchR':>9}{'zblkFrac':>9}{'harmRate':>9}{'commit':>7}")
        for row in R["rows"]:
            print(f"{row['window']:<12}{row['cum_cells']:>8}{row['new_cells']:>8}"
                  f"{row['revisit']:>8.3f}{(row['mode_run'] or 0):>9.2f}"
                  f"{(row['switch_rate'] or 0):>9.3f}{row['zblock_frac']:>9.3f}"
                  f"{row['harm_rate']:>9.3f}{row['committed_frac']:>7.3f}")

    print("\n=== STEP 6: cross-seed consistency (k/N monotone in Regime A) ===")
    print("DESCRIPTIVE ONLY -- no p-values, N=8 is not a reliability claim.")
    for dv in DVS + ["n_resources"]:
        dirs = [direction([r[dv] for r in per[s]["rows"] if r["window"] != "POST-exh"][:3])
                for s in per]
        print(f"{dv:<13} down={dirs.count('down')}/{N} up={dirs.count('up')}/{N} "
              f"non-monotone={dirs.count('non-monotone')}/{N}")

    print("\n=== DEGENERACY CHECK: is the 'consistency' an independent replication? ===")
    base = [round(s["energy"], 9) for s in seeds[0]["life"]["steps"][:ENERGY_CLOCK_ZERO]]
    for sd in seeds:
        e = [round(s["energy"], 9) for s in sd["life"]["steps"][:ENERGY_CLOCK_ZERO]]
        drift = max(abs(s["drive"] - (1.0 - s["energy"]))
                    for s in sd["life"]["steps"][:ENERGY_CLOCK_ZERO])
        a = [s["surprise"] for s in sd["life"]["steps"][:ENERGY_CLOCK_ZERO]]
        x = [s["excite"] for s in sd["life"]["steps"][:ENERGY_CLOCK_ZERO]]
        g = [s["z_goal"] for s in sd["life"]["steps"][:ENERGY_CLOCK_ZERO]]
        en = [s["energy"] for s in sd["life"]["steps"][:ENERGY_CLOCK_ZERO]]
        print(f"seed {sd['seed']}: energy_trace_identical_to_seed0={e == base} "
              f"max|drive-(1-energy)|={drift:.6f} r(surprise,excite)={pearson(a, x):.4f} "
              f"r(z_goal,energy)={pearson(g, en):.4f}")

    print("\n=== STEP 7: driven-perturbation audit (injury must stay driven-only) ===")
    for seed, R in per.items():
        steps = R["steps"]
        limb = [s["t"] for s in steps if s["limb_damage_injected"]]
        haz = [s["t"] for s in steps if s["external_hazard_injected"]]
        blk = [s["t"] for s in steps if s["action_blocked"]]
        shifts = [s["t"] for s in steps if s["world_rule_shift_occurred"]]
        harm = [s["t"] for s in steps if s["harm_event"]]
        gaps = sorted({shifts[i + 1] - shifts[i] for i in range(len(shifts) - 1)})
        print(f"seed {seed}: limb={len(limb)} offgrid50={sum(1 for t in limb if t % 50)} "
              f"haz={len(haz)} offgrid50={sum(1 for t in haz if t % 50)} "
              f"blocked={len(blk)} offgrid10={sum(1 for t in blk if t % 10)} "
              f"shifts={len(shifts)} gaps={gaps} "
              f"harm_events={len(harm)} offgrid50={sum(1 for t in harm if t % 50)}")
        print(f"         dead-channels: residue_wanting_max="
              f"{max(s['residue_wanting'] for s in steps)} "
              f"vigor_max={max(s['vigor'] for s in steps):.4f} "
              f"orienting_active_steps={sum(1 for s in steps if s['orienting_active'])} "
              f"committed_steps={sum(1 for s in steps if s['is_committed'])}")
        print(f"         modes: {dict(Counter(s['mode'] for s in steps).most_common())}")


if __name__ == "__main__":
    main()
