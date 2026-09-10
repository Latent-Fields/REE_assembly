#!/usr/bin/env python3
"""Provenance P3-R2 -- the healthy-replay REACHABILITY SPIKE (design section 5, section 10).

ONE cell: `VERIDICAL / rehearsal / in_place`, on PILOT seeds that are discarded. It asks the
single gated precondition of the whole P3 rung, and nothing else:

    can content rehearsal under intact ancestry raise retrieval fidelity
    WITHOUT appending a countable descendant?

Design section 5 makes this a GATE rather than an arm: "If replay is descendant-generating
only, then every replay event adds a node by construction, the count rises in every arm
including VERIDICAL, and P3 measures replay exposure. This is the single most likely way for
P3 to be built unfalsifiable, and it is invisible until the results are in."

Section 10 fixes the routing in the work-graph debt vocabulary:
    spike passes -> the P3 rung reduces to `complicated (buildable)`
    spike fails  -> `puzzle (known rules)` -- the missing fact is a harness capability that
                    can simply be added, not a reframing.

A FAILING SPIKE IS A SUCCESSFUL SPIKE. It is one cell precisely so that a negative costs a
cell instead of a grid. Nothing here is tuned to make it pass.


TWO STAGES, BOTH REPORTED -- and why the script runs unchanged against both
---------------------------------------------------------------------------

This script is version-agnostic about the harness on purpose, so that the SAME preregistered
criteria evaluate both:

  STAGE 0 (as-built): the harness as it stood at REE_assembly 062d774289 / 1d72f60073.
      `replay(mode='in_place')` incremented a retrieval-event counter and changed nothing
      else, so `retrieval_fidelity` was bit-identical at every replay count.
  STAGE 1 (gap closed): with `reinstate()` -- the second half of requirement H2, which
      design section 2.2 states ("`mode = in_place` raises the source node's retrieval
      fidelity and adds no node") and which the built harness did not implement.

`harness_has_reinstate` is recorded in the payload, and the call adapts. Stage 0 is the
empirical record of the gap; Stage 1 asks whether closing it makes the arm REACHABLE.


WHAT IS AND IS NOT INFORMATIVE HERE, STATED PLAINLY
----------------------------------------------------

Stated up front rather than discovered by a reader, because half this spike is close to
structurally determined once the mechanism exists, and dressing that up as an empirical
discovery would be the dishonest version of this report:

  * `G2`/`G3` (count and cardinality flat) are near-STRUCTURAL under Stage 1.
    `effective_source_count` reaches content only through `shared_ancestry_prob`, which
    reads `edge_target` and `edge_w` -- never `content`. `reinstate()` writes `content`
    only. They are measured anyway because that decoupling is an ASSERTION about the
    implementation, and an assertion worth failing loudly if it is ever untrue.
  * `G1` (fidelity rises) is near-structural under Stage 1 and EXACTLY FALSE under Stage 0.
    The informative half is the Stage 0 measurement, not the Stage 1 one.
  * `S1` is the genuinely uncertain check and the one worth running. A mechanism that
    raised fidelity UNCONDITIONALLY would let P3's healthy arm pass in every ancestry
    condition, which makes the confirmatory grid uninterpretable -- the mirror of the
    section 8.2 STOP row ("count rises in every condition including VERIDICAL -> instrument
    artefact"). S1 asks whether the rise is ancestry-MEDIATED. It is not part of the gate,
    and its failure is a STOP.


PREREGISTRATION -- fixed BEFORE the first run of either stage
--------------------------------------------------------------

PRIMARY GATE (all four must hold, on VERIDICAL / rehearsal / in_place):

  G1  fidelity rises   mean retrieval fidelity over the rehearsed descendant set rises by
                       at least +0.02 from r=0 to r=16, AND the series is non-decreasing.
                       The +0.02 floor is design section 6's own matching tolerance, used
                       here as the minimum resolvable move, per section 8.3's requirement
                       that a gate carry an ABSOLUTE floor and not only a relative test.
                       Deliberately NOT a rank correlation: a constant series -- exactly
                       what Stage 0 produces -- makes Spearman's rho undefined, and P1's
                       disclosure 2 is the record of that trap being walked into. rho is
                       computed and reported, and gates nothing.
  G2  count flat       |N_eff(r=16) - N_eff(r=0)| <= 0.05.
  G3  cardinality flat the trace count is identical at every r.
  G4  regime preserved VERIDICAL rate is 1.00 at every r -- reinstatement must not itself
                       corrupt the genealogy it reads.

SECONDARY, declared, REPORTED, NOT PART OF THE GATE:

  S1  ancestry-mediated  fidelity rise under a corrupted-ancestry comparator is at most
                         0.5x the rise under VERIDICAL. FAILURE IS A STOP, not a gate miss.
  S2  depth bound        a gen-2 descendant saturates BELOW a gen-1 descendant, because
                         reinstatement inherits its ancestor's own error. Reported only.
  S3  route location     confidence and calibration deltas at flat count, located against
                         design section 8.1a's three routes (strength / cardinality /
                         fidelity).

SEEDS ARE PILOT AND DISCARDED (design section 5). Content seed 101, dynamics seed 103,
selection seed 107 -- deliberately NOT P1's authoritative 17/23, so that no number here can
be mistaken for, or pooled with, a confirmatory measurement.

This is a synthetic reachability probe. It registers no claim, promotes nothing, queues
nothing, and is not evidence about psychosis.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Dict, List, Sequence

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import provenance_genealogy_harness as H  # noqa: E402


# --- pilot seeds, discarded (design section 5) -----------------------------------------
CONTENT_SEED = 101
DYNAMICS_SEED = 103
SELECT_SEED = 107

REPLAY_COUNTS = (0, 1, 2, 4, 8, 16)   # design section 2.3
N_DESC = 4                             # cardinality 5 with the seed, as in P1-R7
SIGNAL = 1.0
WORLD_NOISE = 1.484                    # P1's value: single-trace vote reliability p ~ 0.75
ETA = 0.40                             # P1's value
READ_NOISE = 2.0                       # P1's value
DECAY_KNOB_ABSENT = 2.5                # P1's heaviest decay knob -- the ABSENT comparator
DEGRADE_STEPS = 12

# Preregistered thresholds
G1_MIN_RISE = 0.02
G2_MAX_COUNT_DRIFT = 0.05
S1_MAX_RATIO = 0.5

HAS_REINSTATE = hasattr(H, "reinstate")


def _replay_in_place(store, truth, trace_id: int, n: int, rng) -> None:
    """Version-agnostic in-place replay, so one script measures both stages."""
    if HAS_REINSTATE:
        H.replay(store, truth, trace_id, n, rng, mode="in_place", kind="rehearsal")
    else:
        H.replay(store, truth, trace_id, n, rng, mode="in_place")


def _rank(x: np.ndarray) -> np.ndarray:
    order = np.argsort(x, kind="mergesort")
    r = np.empty(len(x), dtype=float)
    r[order] = np.arange(len(x), dtype=float)
    _, inv, cnt = np.unique(x, return_inverse=True, return_counts=True)
    sums = np.zeros(len(cnt))
    np.add.at(sums, inv, r)
    return (sums / cnt)[inv]


def spearman(a: Sequence[float], b: Sequence[float]) -> float:
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    ra, rb = _rank(a), _rank(b)
    sa, sb = ra.std(), rb.std()
    if sa == 0 or sb == 0:
        return float("nan")   # constant series: undefined, and must NOT gate (P1 disclosure 2)
    return float(((ra - ra.mean()) * (rb - rb.mean())).mean() / (sa * sb))


def build_episode(ep: int, n_desc: int = N_DESC):
    """Seed e0 plus `n_desc` gen-1 rehearsal descendants, then FROZEN.

    All descendants are the `replay` content generator: this is the rehearsal cell, and a
    homogeneous population is what makes a mean fidelity readout interpretable.
    """
    crng = np.random.default_rng([CONTENT_SEED, 7, ep])
    Hh = 1 if crng.random() < 0.5 else -1
    store, truth = H.new_episode(crng, Hh, SIGNAL, WORLD_NOISE)
    for k in range(n_desc):
        H.spawn_descendant(store, truth, 0, "replay", crng, t=float(1 + k % 6),
                           eta=ETA, alpha=1.0, signal=SIGNAL, noise=WORLD_NOISE)
    if hasattr(H, "freeze"):
        H.freeze(store)   # H6: after t0 no new world observation may enter
    return store, truth


def build_chain(ep: int, depth: int = 2):
    """e0 -> d1 -> d2 ... a single lineage, for the S2 depth readout."""
    crng = np.random.default_rng([CONTENT_SEED, 9, ep])
    Hh = 1 if crng.random() < 0.5 else -1
    store, truth = H.new_episode(crng, Hh, SIGNAL, WORLD_NOISE)
    prev, chain = 0, []
    for d in range(depth):
        prev = H.spawn_descendant(store, truth, prev, "replay", crng, t=float(1 + d),
                                  eta=ETA, alpha=1.0, signal=SIGNAL, noise=WORLD_NOISE)
        chain.append(prev)
    if hasattr(H, "freeze"):
        H.freeze(store)
    return store, truth, chain


def run_cell(episodes: int, degrade_knob: float = None) -> List[Dict[str, float]]:
    """The cell. `degrade_knob=None` is VERIDICAL; a value is the S1 corrupted comparator.

    Degradation, when present, is applied BEFORE any replay, so that replay count and
    cumulative corruption do not vary together (design section 2.4: this is the P3-A
    accumulation shape, not the P3-B compounding one).
    """
    rows = []
    for r in REPLAY_COUNTS:
        fid, ne, ne_true, card, ver, conf, acc = [], [], [], [], [], [], []
        vrng = np.random.default_rng([CONTENT_SEED, 61, r])
        for ep in range(episodes):
            store, truth = build_episode(ep)
            desc = [i for i in range(store.n()) if store.edge_target[i] >= 0]
            if degrade_knob is not None:
                H.degrade(store, "decay", degrade_knob, DEGRADE_STEPS,
                          np.random.default_rng([DYNAMICS_SEED, 63, ep]), dyn_noise=0.35)
            if r:
                srng = np.random.default_rng([SELECT_SEED, 71, ep, r])
                for _ in range(r):   # uniform selection over the descendant set (sec 2.5)
                    _replay_in_place(store, truth, int(srng.choice(desc)), 1,
                                     np.random.default_rng([CONTENT_SEED, 72, ep, r]))
            ids = list(range(store.n()))
            fid.append(float(np.mean([H.retrieval_fidelity(store, truth, i) for i in desc])))
            n_eff = H.effective_source_count(store, ids)
            votes = [H.read_vote(store, i, vrng, READ_NOISE, 1) for i in ids]
            ne.append(n_eff)
            ne_true.append(H.true_effective_source_count(truth, ids))   # H4, scorer-side
            card.append(len(ids))
            ver.append(int(H.classify_regime(store, truth) == "VERIDICAL"))
            conf.append(H.confidence(votes, P_EST, n_eff))
            acc.append(int(H.belief(store, ids) == truth.H))
        rows.append({
            "r": r,
            "fidelity": float(np.mean(fid)),
            "n_eff": float(np.mean(ne)),
            "n_eff_true": float(np.mean(ne_true)),
            "cardinality": float(np.mean(card)),
            "veridical_rate": float(np.mean(ver)),
            "confidence": float(np.mean(conf)),
            "accuracy": float(np.mean(acc)),
            "signed_error": float(np.mean(conf) - np.mean(acc)),
        })
    return rows


def run_depth(episodes: int) -> Dict[str, object]:
    """S2: does reinstatement saturate lower for a deeper descendant?"""
    out = {}
    for r in (0, 16):
        g1, g2 = [], []
        for ep in range(episodes):
            store, truth, chain = build_chain(ep, depth=2)
            if r:
                for _ in range(r):
                    for c in chain:
                        _replay_in_place(store, truth, c, 1,
                                         np.random.default_rng([CONTENT_SEED, 73, ep, c]))
            g1.append(H.retrieval_fidelity(store, truth, chain[0]))
            g2.append(H.retrieval_fidelity(store, truth, chain[1]))
        out["gen1_r%d" % r] = float(np.mean(g1))
        out["gen2_r%d" % r] = float(np.mean(g2))
    return out


def estimate_p(episodes: int) -> float:
    """Single-trace vote reliability, over the population actually combined (P1 disclosure 3)."""
    ok, tot = 0, 0
    vrng = np.random.default_rng([CONTENT_SEED, 31])
    for ep in range(episodes):
        store, truth = build_episode(ep)
        for i in range(store.n()):
            ok += int(H.read_vote(store, i, vrng, READ_NOISE, 1) == truth.H)
            tot += 1
    return ok / max(tot, 1)


def evaluate_preregistered_criteria(res: Dict[str, object]) -> Dict[str, object]:
    """Fixed before the first run of either stage. See the module docstring."""
    v = res["veridical_cell"]
    fid = [row["fidelity"] for row in v]
    ne = [row["n_eff"] for row in v]
    card = [row["cardinality"] for row in v]
    ver = [row["veridical_rate"] for row in v]
    x = [math.log2(1 + row["r"]) for row in v]

    rise = fid[-1] - fid[0]
    non_decreasing = all(fid[i + 1] >= fid[i] - 1e-12 for i in range(len(fid) - 1))
    g1 = bool(rise >= G1_MIN_RISE and non_decreasing)
    g2 = bool(abs(ne[-1] - ne[0]) <= G2_MAX_COUNT_DRIFT)
    g3 = bool(max(card) - min(card) == 0)
    g4 = bool(all(abs(z - 1.0) < 1e-12 for z in ver))

    c = res["corrupted_cell"]
    rise_corrupt = c[-1]["fidelity"] - c[0]["fidelity"]
    ratio = (rise_corrupt / rise) if rise > 1e-12 else float("nan")
    s1 = bool(rise > 1e-12 and rise_corrupt <= S1_MAX_RATIO * rise)

    d = res["depth"]
    s2 = bool(d["gen2_r16"] < d["gen1_r16"])

    gate = bool(g1 and g2 and g3 and g4)
    return {
        "G1_fidelity_rises": {
            "pass": g1, "rise_r0_to_r16": rise, "floor": G1_MIN_RISE,
            "non_decreasing": non_decreasing,
            "rho_fidelity_vs_log2_1_plus_r": spearman(x, fid),
            "note": "rho is REPORTED, never gated -- undefined on the constant series "
                    "Stage 0 produces (P1 disclosure 2).",
        },
        "G2_count_flat": {"pass": g2, "n_eff_r0": ne[0], "n_eff_r16": ne[-1],
                          "drift": ne[-1] - ne[0], "tolerance": G2_MAX_COUNT_DRIFT},
        "G3_cardinality_flat": {"pass": g3, "cardinality": card[0]},
        "G4_regime_preserved": {"pass": g4, "veridical_rates": ver},
        "GATE_PASS": gate,
        "S1_ancestry_mediated": {
            "pass": s1, "rise_veridical": rise, "rise_corrupted": rise_corrupt,
            "ratio": ratio, "max_ratio": S1_MAX_RATIO,
            "meaning_if_fail": "STOP -- the rise is unconditional, so P3's healthy arm would "
                               "pass in EVERY ancestry condition and the grid is "
                               "uninterpretable (mirror of design 8.2's STOP row).",
        },
        "S2_depth_bound": {"pass": s2, **d},
        "S3_route_location": {
            "delta_confidence": v[-1]["confidence"] - v[0]["confidence"],
            "delta_signed_error": v[-1]["signed_error"] - v[0]["signed_error"],
            "delta_accuracy": v[-1]["accuracy"] - v[0]["accuracy"],
            "n_eff_true_flat": abs(v[-1]["n_eff_true"] - v[0]["n_eff_true"]) < 1e-12,
            "note": "design 8.1a: strength route = confidence up / count flat / calibration "
                    "DEGRADES; fidelity route = confidence up / count flat / calibration "
                    "IMPROVES; cardinality route = readout 3 moves at all.",
        },
        "ROUTING": (
            "spike PASSES -> P3 rung reduces to `complicated (buildable)`" if gate
            else "spike FAILS -> `puzzle (known rules)`: the missing fact is a harness "
                 "capability that can be added, not a reframing"
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="P3-R2 healthy-replay reachability spike")
    ap.add_argument("--episodes", type=int, default=600)
    ap.add_argument("--out-json", type=Path, default=None)
    args = ap.parse_args()

    global P_EST
    P_EST = estimate_p(min(args.episodes, 800))

    res: Dict[str, object] = {}
    res["veridical_cell"] = run_cell(args.episodes, degrade_knob=None)
    res["corrupted_cell"] = run_cell(args.episodes, degrade_knob=DECAY_KNOB_ABSENT)
    res["depth"] = run_depth(args.episodes)
    res["p_est"] = P_EST

    criteria = evaluate_preregistered_criteria(res)
    payload = {
        "assay": "provenance_p3_r2_reachability_spike",
        "status": "synthetic_pilot_spike_only -- seeds discarded, not confirmatory evidence",
        "cell": "VERIDICAL / rehearsal / in_place",
        "stage": "gap_closed" if HAS_REINSTATE else "as_built",
        "harness_has_reinstate": HAS_REINSTATE,
        "harness_has_freeze": hasattr(H, "freeze"),
        "seeds": {"content": CONTENT_SEED, "dynamics": DYNAMICS_SEED,
                  "selection": SELECT_SEED, "note": "pilot, discarded (design section 5)"},
        "params": {"episodes": args.episodes, "n_desc": N_DESC, "eta": ETA,
                   "read_noise": READ_NOISE, "replay_counts": list(REPLAY_COUNTS),
                   "reinstate_gain": getattr(H, "REINSTATE_GAIN", None)},
        "results": res,
        "criteria": criteria,
    }
    print(json.dumps(payload, indent=2, sort_keys=True, default=float))
    if args.out_json:
        args.out_json.parent.mkdir(parents=True, exist_ok=True)
        args.out_json.write_text(
            json.dumps(payload, indent=2, sort_keys=True, default=float) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
