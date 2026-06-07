#!/usr/bin/env python3
"""Arm-reuse Regime-A cross-instance determinism gate (plan 9.0 / 7b.4).

Compares the two 610 OFF-baseline mints -- V3-EXQ-644 (ree-cloud-2) and
V3-EXQ-645 (ree-cloud-3), same script/config -- to confirm two instances of the
SAME machine_class produce the same draw per (substrate, config_slice, seed).
That mutual determinism is the assumption Regime-A reuse rests on: a cached cell
is treated as a *representative draw* for its fingerprint, so cloud-2's OFF cell
may stand in for cloud-3's. If the two instances diverge beyond tolerance, Regime
A is invalid as built and reuse must wait for Regime B (bit-exact).

PRE-REGISTERED TOLERANCE (fixed 2026-06-07T08:22Z, BEFORE V3-EXQ-645 metrics were
visible -- choosing it after seeing the data would hollow out the gate):

  Per seed s in {42,43,44}, per metric m in
    {end_phase_2_entropy, end_phase_3_entropy, mean_reward}:
  compute d = |cloud2[s,m] - cloud3[s,m]|.

  TIER 1  (bit-near)      : all d <= 1e-6
      -> instances effectively bit-identical on CPU torch; Regime A is solid and
         approaches Regime B for free.
  TIER 2  (distributional): all entropy d <= 0.05 AND all reward d <= 0.05
      -> cached cell is a valid representative draw for matched-control use. The
         0.05 anchor is ~7% of the ~0.68 cross-SEED entropy spread (0.67..1.35
         in the 644 mint) -- the spread that actually defines the OFF arm's role
         as a per-seed matched reference. A drift this small cannot change which
         seed-arm comparison a treatment is measured against, so it is
         scientifically immaterial.
  FAIL    (beyond TIER 2) : any d > 0.05
      -> Regime A invalid as built. STOP; escalate the Regime A-vs-B decision to
         the user. Do NOT leave any experiment wired to skip an arm.

Also cross-checks that the per-seed arm_fingerprint hashes are IDENTICAL across
the two instances (they must be, by construction -- coarse machine_class +
content substrate_hash). Equal fingerprints WITH out-of-tolerance metrics is
exactly the "false-collision" failure the gate exists to catch, and is reported
loudly.

Usage:
  python3 scripts/arm_reuse_determinism_check.py
  python3 scripts/arm_reuse_determinism_check.py --evidence-dir <dir> [--json]

Exit code 0 = TIER1/TIER2 (gate PASS), 2 = FAIL, 3 = 645 not landed yet / inputs
missing.
"""
import argparse
import glob
import json
import os
import sys

SEEDS = [42, 43, 44]
METRICS = ["end_phase_2_entropy", "end_phase_3_entropy", "mean_reward"]
ENTROPY_METRICS = {"end_phase_2_entropy", "end_phase_3_entropy"}

TIER1_BITNEAR = 1e-6
TIER2_ENTROPY = 0.05
TIER2_REWARD = 0.05

CLOUD2_GLOB = "*v3exq644*_v3.json"
CLOUD3_GLOB = "*v3exq645*_v3.json"


def _find_one(evidence_dir, pattern, label):
    hits = sorted(glob.glob(os.path.join(evidence_dir, pattern)))
    if not hits:
        return None, f"{label}: no manifest matching {pattern}"
    if len(hits) > 1:
        # prefer newest by name (timestamped); warn
        return hits[-1], f"{label}: {len(hits)} matches, using newest {os.path.basename(hits[-1])}"
    return hits[0], None


def _cells_by_seed(manifest):
    out = {}
    for a in manifest.get("arm_results", []):
        out[a.get("seed")] = a
    return out


def main():
    ap = argparse.ArgumentParser()
    here = os.path.dirname(os.path.abspath(__file__))
    default_ev = os.path.normpath(os.path.join(here, "..", "evidence", "experiments"))
    ap.add_argument("--evidence-dir", default=default_ev)
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = ap.parse_args()

    p2, w2 = _find_one(args.evidence_dir, CLOUD2_GLOB, "cloud-2 (V3-EXQ-644)")
    p3, w3 = _find_one(args.evidence_dir, CLOUD3_GLOB, "cloud-3 (V3-EXQ-645)")
    for w in (w2, w3):
        if w and "no manifest" not in w:
            print("NOTE:", w, file=sys.stderr)

    if not p2 or not p3:
        msg = "Gate NOT evaluable yet:"
        if not p2:
            msg += " " + (w2 or "cloud-2 manifest missing")
        if not p3:
            msg += " " + (w3 or "cloud-3 manifest (V3-EXQ-645) has not landed")
        print(msg)
        print("V3-EXQ-645 must complete on ree-cloud-3 before the gate can close.")
        sys.exit(3)

    m2 = json.load(open(p2))
    m3 = json.load(open(p3))
    c2 = _cells_by_seed(m2)
    c3 = _cells_by_seed(m3)

    rows = []
    worst_entropy = 0.0
    worst_reward = 0.0
    fp_mismatch = []
    missing = []
    for s in SEEDS:
        a2, a3 = c2.get(s), c3.get(s)
        if a2 is None or a3 is None:
            missing.append(s)
            continue
        fp2 = (a2.get("arm_fingerprint") or {}).get("arm_fingerprint")
        fp3 = (a3.get("arm_fingerprint") or {}).get("arm_fingerprint")
        fp_equal = (fp2 is not None and fp2 == fp3)
        if not fp_equal:
            fp_mismatch.append(s)
        for m in METRICS:
            v2, v3 = a2.get(m), a3.get(m)
            if v2 is None or v3 is None:
                missing.append((s, m))
                continue
            d = abs(v2 - v3)
            if m in ENTROPY_METRICS:
                worst_entropy = max(worst_entropy, d)
            else:
                worst_reward = max(worst_reward, d)
            rows.append((s, m, v2, v3, d, fp_equal))

    if missing:
        print(f"Gate NOT evaluable: missing cells/metrics {missing}")
        sys.exit(3)

    all_d = [r[4] for r in rows]
    tier1 = all(d <= TIER1_BITNEAR for d in all_d)
    tier2 = (worst_entropy <= TIER2_ENTROPY) and (worst_reward <= TIER2_REWARD)
    if tier1:
        verdict = "PASS_TIER1_BITNEAR"
    elif tier2:
        verdict = "PASS_TIER2_DISTRIBUTIONAL"
    else:
        verdict = "FAIL_REGIME_A_INVALID"

    false_collision = (verdict.startswith("FAIL") and not fp_mismatch)

    if args.json:
        print(json.dumps({
            "verdict": verdict,
            "cloud2_manifest": os.path.basename(p2),
            "cloud3_manifest": os.path.basename(p3),
            "worst_entropy_diff": worst_entropy,
            "worst_reward_diff": worst_reward,
            "tolerance": {"tier1": TIER1_BITNEAR, "tier2_entropy": TIER2_ENTROPY, "tier2_reward": TIER2_REWARD},
            "fingerprint_mismatch_seeds": fp_mismatch,
            "false_collision": false_collision,
            "rows": [{"seed": s, "metric": m, "cloud2": v2, "cloud3": v3, "abs_diff": d, "fp_equal": fe}
                     for (s, m, v2, v3, d, fe) in rows],
        }, indent=2))
    else:
        print(f"cloud-2: {os.path.basename(p2)}")
        print(f"cloud-3: {os.path.basename(p3)}")
        print()
        print(f"{'seed':>4} {'metric':<22} {'cloud-2':>14} {'cloud-3':>14} {'|diff|':>12} fp")
        for (s, m, v2, v3, d, fe) in rows:
            flag = "" if fe else "  <-- FP MISMATCH"
            print(f"{s:>4} {m:<22} {v2:>14.8f} {v3:>14.8f} {d:>12.2e} {'=' if fe else 'x'}{flag}")
        print()
        print(f"worst entropy |diff| = {worst_entropy:.2e}  (tier2 <= {TIER2_ENTROPY})")
        print(f"worst reward  |diff| = {worst_reward:.2e}  (tier2 <= {TIER2_REWARD})")
        print(f"per-seed fingerprints identical: {not fp_mismatch}")
        print()
        print(f"VERDICT: {verdict}")
        if false_collision:
            print("!! FALSE COLLISION: equal fingerprints but out-of-tolerance metrics.")
            print("!! The fingerprint claims these cells are the same random variable; they are not.")
            print("!! Regime A is unsound as built -- escalate Regime A-vs-B to the user.")
        elif verdict.startswith("FAIL"):
            print("Regime A invalid as built -- STOP, escalate Regime A-vs-B to the user.")

    sys.exit(0 if verdict.startswith("PASS") else 2)


if __name__ == "__main__":
    main()
