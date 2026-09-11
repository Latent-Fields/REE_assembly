#!/usr/bin/env python3
"""Re-derive reanalysis_mech536_persistence_2x2_confinement_20260911T142130Z.json.

Companion to that artifact. Reads V3-EXQ-1007's banked manifest + episode log and writes
NOTHING. Run it to reproduce every number in the artifact, and to re-check the re-posed C1
against the incumbent detector it replaces.

  /opt/local/bin/python3 REE_assembly/evidence/reanalysis/rederive_mech536_persistence_2x2_confinement.py

Design record for the re-posed criterion (GFLAG-0233):
  REE_assembly/evidence/planning/mech536_c1_reposed_confinement_criterion_20260911.md
"""
import json
from collections import OrderedDict
from typing import Optional, Sequence, Tuple

BASE = "/Users/dgolden/REE_Working/REE_assembly/evidence/experiments/"
STEM = "v3_exq_1007_mech536_eval_persistence_discriminator_20260907T072349Z_v3"
MANIFEST = BASE + STEM + ".json"
EPISODE_LOG = BASE + STEM + "_episode_log.json"

MIN_TAIL = 4

# Longest period each arm's manipulation can produce: a k-latch re-periodises a period-2
# alternation to period 2k. This is what makes the reach requirement scale WITH k -- a bigger
# k demands MORE episode, never less (the direct repair of GFLAG-0233 finding 2).
ARM_MAX_PERIOD = {
    "greedy_argmax": 2, "greedy_argmax@contamination_off": 2,
    "persist_k2": 4, "persist_k2@contamination_off": 4,
    "persist_k4": 8, "switch_cost": 8,
    "stochastic_sample": 2, "random_walk": 2,
    "local_view_greedy": 2, "local_view_greedy_persist_k2": 4,
}


# ---- the INCUMBENT criterion, verbatim from the 1007 driver (for the identity check) ------
def period2_cycle_present(positions: Sequence[Tuple[int, int]], min_len: int = 6) -> bool:
    pos = [tuple(p) for p in positions]
    n = len(pos)
    if n < min_len:
        return False
    for i in range(n - min_len + 1):
        w = pos[i:i + min_len]
        if w[0] == w[1]:
            continue
        if all(w[j] == w[j + 2] for j in range(min_len - 2)):
            return True
    return False


# ---- the RE-POSED criterion ---------------------------------------------------------------
def confinement(positions: Sequence[Tuple[int, int]], max_period: int) -> Optional[bool]:
    """True = confined, False = escaped, None = UNDETERMINED.

    Period-agnostic and amplitude-agnostic: an orbit of ANY period over ANY number of cells
    stops producing new cells once it closes; a boundary-press fixed point produces none at
    all; an escaping trajectory keeps producing them. Fails CLOSED -- an episode whose head is
    too short to have contained a full period reads UNDETERMINED, never 'escaped'.
    """
    pos = [tuple(p) for p in positions]
    n = len(pos)
    tail_len = (n + 1) // 2
    head_len = n - tail_len
    if tail_len < MIN_TAIL or head_len < max_period:
        return None
    head, tail = set(pos[:head_len]), pos[head_len:]
    return len(set(tail) - head) == 0


def field_confined(ep: dict) -> bool:
    """CONSERVATIVE confinement from recorded per-episode fields, available for all 20
    episodes/cell. Can only positively DETECT confinement, never escape -- so the percentages
    it yields are lower bounds, which is the safe direction."""
    return bool(ep.get("fixed_point")) or (ep.get("orbit_period") is not None)


def main() -> None:
    man = json.load(open(MANIFEST))
    rows = list(man["eval_results"]) + list(man.get("anchor_results") or [])
    per_arm = OrderedDict()
    for r in rows:
        per_arm.setdefault(r["arm_id"], []).append(r)

    print("=" * 108)
    print("FULL SAMPLE (20 eps x 3 seeds = 60/arm) -- conservative field-determined confinement")
    print("=" * 108)
    print("%-32s %7s %10s %8s %26s" % ("arm", "n_eps", "confined%", "uniq", "competence (42/43/44)"))
    print("-" * 108)
    for arm, cells in per_arm.items():
        n = conf = 0
        comps, uniqs = [], []
        for c in sorted(cells, key=lambda z: z["seed"]):
            comps.append(c["foraging_competence"])
            uniqs.append(c["trace"]["mean_unique_cells"])
            for ep in c["trace"]["per_episode"]:
                n += 1
                conf += 1 if field_confined(ep) else 0
        print("%-32s %7d %9.0f%% %8.1f %26s"
              % (arm, n, 100.0 * conf / n, sum(uniqs) / len(uniqs),
                 "/".join("%.2f" % x for x in comps)))

    log = json.load(open(EPISODE_LOG))
    print()
    print("=" * 108)
    print("POSITION-LEVEL (6 logged eps/arm) -- re-posed C1 vs the incumbent it replaces")
    print("=" * 108)
    print("%-32s %4s %8s %10s %9s %7s" % ("arm", "P", "eps", "C1 period2", "CONFINED", "undet"))
    print("-" * 108)
    for arm, P in ARM_MAX_PERIOD.items():
        eps = [[tuple(s["pos"]) for s in e["steps"]]
               for sd in log["seeds"] for e in sd["episodes"] if e["arm"] == arm]
        if not eps:
            continue
        v = [confinement(p, P) for p in eps]
        print("%-32s %4d %8d %10s %8d/%-6d %7d"
              % (arm, P, len(eps),
                 "%d/%d" % (sum(1 for p in eps if period2_cycle_present(p)), len(eps)),
                 sum(1 for x in v if x is True), sum(1 for x in v if x is not None),
                 sum(1 for x in v if x is None)))

    print()
    print("=" * 108)
    print("THE 2x2 -- representation quality x the SAME k=2 latch")
    print("=" * 108)
    print("%-24s %-16s %-32s %10s %22s" % ("representation", "persistence", "arm", "confined%", "res/100 surv"))
    print("-" * 108)
    for repr_, pers, arm in (
        ("direction-blind", "none", "greedy_argmax"),
        ("direction-blind", "k=2 latch", "persist_k2"),
        ("adequate (local view)", "none", "local_view_greedy"),
        ("adequate (local view)", "k=2 latch", "local_view_greedy_persist_k2"),
    ):
        cells = sorted(per_arm[arm], key=lambda z: z["seed"])
        n = sum(len(c["trace"]["per_episode"]) for c in cells)
        conf = sum(1 for c in cells for ep in c["trace"]["per_episode"] if field_confined(ep))
        rps = "/".join("%.2f" % c["resources_per_100_survived_steps"] for c in cells)
        print("%-24s %-16s %-32s %9.0f%% %22s" % (repr_, pers, arm, 100.0 * conf / n, rps))

    print()
    print("NOTE: the incumbent C1 (period2_cycle_present) is False for EVERY latch arm by")
    print("      construction -- a k>=2 latch never flips the action on consecutive steps, so")
    print("      strict single-step alternation is unreachable. That is the identity GFLAG-0233")
    print("      reports, and it is why C1 passed while the agent stayed confined.")


if __name__ == "__main__":
    main()
