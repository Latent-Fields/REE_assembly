#!/usr/bin/env python3
"""Provenance P1 -- generated-ancestry false-independence assay.

Driver for the P1 design in
`evidence/planning/provenance_harness_generated_ancestry_design.md`, built on the state
layer in `provenance_genealogy_harness.py` and gated by probe P0
(`provenance_genealogy_probe_p0.py`, REE_assembly b81f9764bc), whose endogeneity sweep
established that ancestry loss in a harness of this class is GENERATED rather than
stipulated.

THE QUESTION. Humans already show confidence inflation when ancestry is PRESENTED to them
(Yousif 2019 PMID 31291546, Connor Desai 2022 PMID 35149359, Weaver 2007 PMID 17484607).
P1 earns its place only by corrupting a genealogy representation from the INSIDE, through
memory dynamics, and asking whether the architecture's own effective-source count inflates
and its calibration degrades as a result.

This is a synthetic measurement assay, not a REE creature experiment, not a queue entry,
and not claim evidence until an authoritative run is reviewed and banked separately.


WHAT IS MEASURED, AND WHAT IS NEVER COLLAPSED (design note section 8)
---------------------------------------------------------------------

    1. association strength                 did a relation form?          (E43/E33 class)
    2. source attribution                   P(external | representation)  (C2/C3 class)
    3. effective independent-source count   the cardinality variable
    4. calibration against world truth      confidence vs observed accuracy

Readouts 3 and 4 are reported separately and both, never one derived from the other.

`P1-R6` boundary declaration (companion artifact section 7): readouts 1, 2 and 4 alone are
`MECH-544`'s territory. P1's distinctive product is **readout 3**. A result that moves only
1, 2 and 4 is not a P1 result, and must not be counted as evidence for two claims at once.

`P1-R5` architecture route: the harness implements the **stored-tag** route, declared in
its module docstring before this run. Results here are results about that route only.


PREREGISTERED CRITERIA -- declared BEFORE any execution
--------------------------------------------------------

MAIN dose-response (H1). Over the decay axis and the misbinding axis, at fixed content:

  M1  The architecture's N_eff rises with the degradation knob on BOTH axes
      (Spearman rho >= 0.80 against knob rank).
  M2  Mean confidence rises with the knob on both axes (rho >= 0.80), while observed
      accuracy does NOT rise (rho <= 0.30). Confidence rising on evidence that has not
      improved is the whole hypothesis.
  M3  Calibration signed error (confidence - accuracy) rises with the knob (rho >= 0.80)
      and is positive (overconfident) at the high-knob end.
  M4  INTERPRETABILITY FLOOR (design note 8.2). The measured N_eff inflation
      (N_eff at the high-knob end minus N_eff at VERIDICAL) must EXCEED the instrument's
      own worst |signed error| measured against known topology in the same run. If it does
      not, the result is reported as UNINTERPRETABLE -- neither positive nor null.

  MAIN passes iff M1 and M2 and M3 and M4.

P1-R2 adaptive linking (design note 7.1, from E43). Two descendants of genuinely DIFFERENT
world events, linked offline:

  R2  association strength rises by >= 0.50 over its pre-link baseline AND the effective
      source count stays at 2 (|N_eff - 2| <= 0.30). N_eff < 1.70 is the FAILURE
      direction -- distinct sources collapsed by the act of linking -- and is reported as
      a failure, never scored as a clean null.

P1-R3 legitimate computation (design note 7.2, anchored to E30). THE control that decides
whether the hypothesis is testable as posed:

  R3a Both arms' confidence RISES. If the legitimate arm's confidence stayed flat the
      contrast would be trivial and would test nothing.
  R3b Legitimate arm: N_eff stays at 1 (|N_eff - 1| <= 0.30) AND calibration does not
      degrade (signed error rises by <= 0.02).
  R3c Corrupted arm: N_eff rises by >= 0.50 AND calibration degrades (signed error rises
      by >= 0.05).

  R3 passes iff a and b and c. FAILURE FIRES SUPPLEMENT FALSIFIER 5: the hypothesis is
  untestable under these instruments and they must be rebuilt before any result is read.

P1-R4 genuinely independent new observation (design note 7.3), as the alpha dial of 4.3:

  R4  N_eff tracks the derived ground-truth count across the dial (rho >= 0.80),
      confidence rises as alpha falls, and calibration is PRESERVED (|signed error| at
      alpha = 0 is no worse than at alpha = 1 by more than 0.05).

P1-R7 fluency versus cardinality (design note 7.5, MANDATORY):

  R7  With ancestry held VERIDICAL (verified by the 5.3 classifier, not assumed) and
      descendant cardinality FIXED, confidence is FLAT across retrieval-event count
      (|delta confidence| <= 0.01 from 0 to 16 events).
  R7pc POSITIVE CONTROL: the spawn-mode arm, where retrieval events AND cardinality both
      rise, MUST show confidence rising by >= 0.02. Without it the flatness in R7 is
      vacuous -- it would show only that the measurement moved nothing at all.

  If R7 fails (confidence rises with retrieval events at fixed cardinality), fluency is
  live and uncontrolled, and the main result is reported as NOT ATTRIBUTABLE to cardinality
  regardless of how M1-M4 came out.

C1 content-fixed assertion (design note 4.4): content hashes bit-identical across all
ancestry conditions within a content seed. A HARD assertion -- content drift is the single
failure that would invalidate every readout at once and would be visible in none of them.


PRE-RUN AMENDMENTS -- four defects found in smoke runs, fixed BEFORE the authoritative run
-------------------------------------------------------------------------------------------

Disclosed here rather than silently folded in. None changed a threshold or a knob grid; two
were outright bugs in the measurement, and two of the four were making criteria FAIL, which
is the direction that deserves the most scrutiny.

  1. `spearman` did not average tied ranks. A CONSTANT series therefore received ranks
     0..n-1 in input order and correlated perfectly with any monotone x, so the perfectly
     flat accuracy curve scored `rho_accuracy = 1.00` -- the exact opposite of what it is,
     and M2 failed on it. Fixed to average ties (P0's implementation already did).
  2. M2's accuracy clause was preregistered as `rho_accuracy <= 0.30`. Accuracy is EXACTLY
     constant across every knob on both axes, and a rank correlation is undefined on a
     constant series, so even with (1) fixed the statistic returns nan and `nan <= 0.30` is
     False. The clause is now evaluated on a flatness test that is well defined when the
     series is constant; the literal preregistered `rho_accuracy` is still computed and
     reported. The intent -- "accuracy does not rise" -- is satisfied in its strongest
     possible form, so this repairs an ill-defined statistic rather than moving a goalpost.
  3. P1-R3's `p` was estimated over the wrong population (seed plus descendants) while the
     legitimate arm forms its belief from `e0` alone. In that arm `n = 1` and `N_eff = 1`,
     so confidence collapses to exactly `p_est` and the arm was measuring the estimator
     rather than the architecture. Now estimated on the population actually combined.
     Relatedly, `READ_NOISE` was raised 0.9 -> 2.0: at 0.9 the legitimate effect was
     p 0.718 -> 0.747, SMALLER than the standard error of `p_est` itself, so the arm had no
     resolvable range at all (measured `legit_confidence_rise` was exactly 0.000).
  4. P1-R7's positive control was mis-specified. It required the spawn arm's confidence to
     RISE as cardinality rose -- but those spawned traces are replays with ancestry intact,
     and a CORRECT architecture must discount them (measured: cardinality 5 -> 21 while
     N_eff stayed 1.118 -> 1.146 and confidence moved -0.011). The old control was therefore
     unpassable by a correct architecture. Replaced by a three-arm design: `in_place`
     (the fluency test), `spawn_bound` (reported, not gated -- correct replay discounting),
     and `spawn_degraded` (the real dynamic-range control, where N_eff genuinely rises).
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import provenance_genealogy_harness as H  # noqa: E402


DECAY_KNOBS = (1e6, 20.0, 12.0, 9.5, 8.0, 6.0, 4.0, 2.5)
MISBIND_KNOBS = (0.0, 0.01, 0.025, 0.05, 0.09, 0.16, 0.28, 0.5)
ALPHA_DIAL = (1.0, 0.8, 0.6, 0.4, 0.2, 0.0)
RETRIEVAL_COUNTS = (0, 1, 2, 4, 8, 16)

SIGNAL = 1.0
WORLD_NOISE = 1.484  # sets single-trace vote reliability p to ~0.75
ETA = 0.40
# Read noise is a deliberately large share of the total, so that P1-R3's legitimate arm has
# RANGE: averaging 16 reads must produce a confidence rise the estimator can actually
# resolve. At READ_NOISE = 0.9 the effect was p 0.718 -> 0.747, smaller than the standard
# error of p_est itself, and the arm measured nothing. At 2.0 it is 0.656 -> 0.739.
READ_NOISE = 2.0


def _rank(x: np.ndarray) -> np.ndarray:
    """Average ranks. Tie-averaging is load-bearing, not a nicety: without it a CONSTANT
    series receives ranks 0..n-1 in input order and therefore correlates perfectly with any
    monotone x, so a perfectly flat accuracy curve would score rho = 1.0 -- the exact
    opposite of what it is."""
    order = np.argsort(x, kind="mergesort")
    r = np.empty(x.size, dtype=float)
    r[order] = np.arange(x.size, dtype=float)
    xs = x[order]
    i = 0
    while i < xs.size:
        j = i
        while j + 1 < xs.size and xs[j + 1] == xs[i]:
            j += 1
        if j > i:
            r[order[i : j + 1]] = float(np.mean(r[order[i : j + 1]]))
        i = j + 1
    return r


def spearman(a: Sequence[float], b: Sequence[float]) -> float:
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    ok = np.isfinite(a) & np.isfinite(b)
    a, b = a[ok], b[ok]
    if a.size < 3:
        return float("nan")
    ra, rb = _rank(a), _rank(b)
    if ra.std() == 0 or rb.std() == 0:
        return float("nan")
    return float(((ra - ra.mean()) * (rb - rb.mean())).mean() / (ra.std() * rb.std()))


# --------------------------------------------------------------------------------------
# Episode construction -- content under a CONTENT seed, dynamics under a DYNAMICS seed
# --------------------------------------------------------------------------------------


def build_episode(content_seed: int, ep: int, n_desc: int, alpha: float = 1.0):
    """Design note 4.4: all content from a content seed INDEPENDENT of the dynamics seed,
    so that ancestry conditions differ only in the dynamics."""
    crng = np.random.default_rng([content_seed, 7, ep])
    Hh = 1 if crng.random() < 0.5 else -1
    store, truth = H.new_episode(crng, Hh, SIGNAL, WORLD_NOISE)
    kinds = ["replay", "prediction", "retrieved_memory", "ambiguous_perception"]
    for k in range(n_desc):
        H.spawn_descendant(
            store, truth, 0, kinds[k % len(kinds)], crng,
            t=float(1 + k % 6), eta=ETA, alpha=alpha, signal=SIGNAL, noise=WORLD_NOISE,
        )
    return store, truth


def estimate_p(
    content_seed: int,
    episodes: int,
    n_desc: int,
    read_noise: float,
    n_reads: int,
    population: str = "all",
) -> float:
    """Single-trace reliability, estimated on a calibration split.

    `population` selects WHICH traces the estimate is over, and it must match the trace set
    the belief actually combines -- `all` for the main arm (seed plus descendants),
    `seed_only` for P1-R3's legitimate arm, which forms its belief from `e0` alone.

    This is not arm-conditioning of the confidence RULE, which stays fixed; it is
    estimating the rule's `p` parameter on the right population. Estimating it on a
    different population is simply a mis-estimate, and it matters disproportionately in the
    legitimate arm: there `n = 1` and `N_eff = 1`, so confidence collapses to exactly
    `p_est` and the arm's calibration measures the estimator rather than the architecture.
    """
    rng = np.random.default_rng([content_seed, 555, n_reads])
    ok = tot = 0
    for ep in range(episodes):
        store, truth = build_episode(content_seed, 10_000 + ep, n_desc)
        ids = [0] if population == "seed_only" else list(range(store.n()))
        for i in ids:
            ok += int(H.read_vote(store, i, rng, read_noise, n_reads) == truth.H)
            tot += 1
    return ok / max(tot, 1)


@dataclass
class Readouts:
    n_eff: float = 0.0
    n_eff_true: float = 0.0
    confidence: float = 0.0
    accuracy: float = 0.0
    signed_error: float = 0.0
    assoc: float = 0.0
    p_external: float = 0.0
    fidelity: float = 0.0
    edge_regimes: Dict[str, float] = field(default_factory=dict)
    episode_regimes: Dict[str, float] = field(default_factory=dict)


def measure(
    process: str, knob: float, args, p_est: float, absent_policy: str = "independent"
) -> Tuple[Readouts, List[Tuple[str, float, float, int]]]:
    """Run `episodes` episodes at one knob value and return the four readouts.

    Also returns per-episode (edge_regime_of_that_episode, n_eff, confidence, correct)
    rows for the regime-stratified table, which is the PRIMARY stratification per P0's
    recommendation 2 -- episode-level regimes are kept as the secondary view because the
    worst-edge rule makes them a near-binary function of the per-edge rate.
    """
    r = Readouts()
    ne, net, conf, corr, assoc, pext, fid = [], [], [], [], [], [], []
    ec = {k: 0 for k in H.REGIMES}
    pc = {k: 0 for k in H.REGIMES}
    rows: List[Tuple[str, float, float, int]] = []
    vrng = np.random.default_rng([args.content_seed, 909])

    for ep in range(args.episodes):
        store, truth = build_episode(args.content_seed, ep, args.n_desc)
        drng = np.random.default_rng([args.dynamics_seed, 11, ep])
        if knob is not None and process is not None:
            H.degrade(store, process, knob, args.steps, drng, dyn_noise=args.dyn_noise)

        ids = list(range(store.n()))
        votes = [H.read_vote(store, i, vrng, READ_NOISE, 1) for i in ids]
        n_eff = H.effective_source_count(store, ids, absent_policy)
        c = H.confidence(votes, p_est, n_eff)
        b = 1 if sum(votes) >= 0 else -1

        ne.append(n_eff)
        net.append(H.true_effective_source_count(truth, ids))
        conf.append(c)
        corr.append(int(b == truth.H))
        d = truth.descendants()
        if len(d) >= 2:
            assoc.append(H.association_strength(store, d[0], d[1]))
        pext.append(float(np.mean([H.source_attribution(store, i)["p_external"] for i in d])))
        fid.append(float(np.mean([H.retrieval_fidelity(store, truth, i) for i in d])))

        e = H.classify_edges(store, truth)
        for k, v in e.items():
            ec[k] += v
        dominant = max(e, key=lambda k: e[k])
        pr = H.classify_regime(store, truth)
        pc[pr] += 1
        rows.append((dominant, n_eff, c, int(b == truth.H)))

    tot_e = max(sum(ec.values()), 1)
    r.n_eff, r.n_eff_true = float(np.mean(ne)), float(np.mean(net))
    r.confidence, r.accuracy = float(np.mean(conf)), float(np.mean(corr))
    r.signed_error = r.confidence - r.accuracy
    r.assoc = float(np.mean(assoc)) if assoc else float("nan")
    r.p_external, r.fidelity = float(np.mean(pext)), float(np.mean(fid))
    r.edge_regimes = {k: ec[k] / tot_e for k in H.REGIMES}
    r.episode_regimes = {k: pc[k] / max(args.episodes, 1) for k in H.REGIMES}
    return r, rows


# --------------------------------------------------------------------------------------
# Arms
# --------------------------------------------------------------------------------------


def arm_instrument_floor(args, p_est: float) -> Dict[str, object]:
    """Design note 8.2. The count instrument's own signed error against KNOWN topology,
    measured in the same run, on the undegraded alpha dial where the scorer holds the
    derived true count. This is the instrument's BIAS, not its variance."""
    rows = []
    for a in ALPHA_DIAL:
        ne, net = [], []
        for ep in range(args.episodes):
            store, truth = build_episode(args.content_seed, 20_000 + ep, args.n_desc, alpha=a)
            ids = list(range(store.n()))
            ne.append(H.effective_source_count(store, ids))
            net.append(H.true_effective_source_count(truth, ids))
        rows.append(
            {
                "alpha": a,
                "n_eff_arch": float(np.mean(ne)),
                "n_eff_true": float(np.mean(net)),
                "signed_error": float(np.mean(ne) - np.mean(net)),
            }
        )
    worst = max(abs(r["signed_error"]) for r in rows)
    return {"rows": rows, "worst_abs_signed_error": worst}


def arm_r2(args, p_est: float) -> Dict[str, object]:
    """P1-R2 adaptive linking (E43): two descendants of genuinely DIFFERENT world events."""
    pre, post, ne_post = [], [], []
    for ep in range(args.episodes):
        crng = np.random.default_rng([args.content_seed, 31, ep])
        Hh = 1 if crng.random() < 0.5 else -1
        store, truth = H.new_episode(crng, Hh, SIGNAL, WORLD_NOISE)
        e1 = H.add_world_event(store, truth, crng, SIGNAL, WORLD_NOISE, t=1.0)
        d0 = H.spawn_descendant(store, truth, 0, "replay", crng, t=2.0, eta=ETA)
        d1 = H.spawn_descendant(store, truth, e1, "replay", crng, t=2.0, eta=ETA)
        pre.append(H.association_strength(store, d0, d1))
        H.link(store, d0, d1, 1.0)
        post.append(H.association_strength(store, d0, d1))
        ne_post.append(H.effective_source_count(store, [0, e1, d0, d1]))
    return {
        "assoc_pre": float(np.mean(pre)),
        "assoc_post": float(np.mean(post)),
        "assoc_rise": float(np.mean(post) - np.mean(pre)),
        "n_eff_after_link": float(np.mean(ne_post)),
    }


def arm_r3(args) -> Dict[str, object]:
    """P1-R3. Two arms, ONE confidence rule, each licensed to move a different term."""
    out: Dict[str, object] = {}

    # Legitimate: fixed observation set (e0 alone), repeated computation lowers read noise.
    legit = []
    for n_reads in (1, 4, 16):
        p_n = estimate_p(
            args.content_seed, args.cal_episodes, args.n_desc, READ_NOISE, n_reads,
            population="seed_only",
        )
        conf, corr, ne = [], [], []
        vrng = np.random.default_rng([args.content_seed, 41, n_reads])
        for ep in range(args.episodes):
            store, truth = build_episode(args.content_seed, 30_000 + ep, args.n_desc)
            votes = [H.read_vote(store, 0, vrng, READ_NOISE, n_reads)]
            n_eff = H.effective_source_count(store, [0])
            c = H.confidence(votes, p_n, n_eff)
            conf.append(c)
            corr.append(int(votes[0] == truth.H))
            ne.append(n_eff)
        legit.append(
            {
                "n_reads": n_reads,
                "p_est": p_n,
                "confidence": float(np.mean(conf)),
                "accuracy": float(np.mean(corr)),
                "signed_error": float(np.mean(conf) - np.mean(corr)),
                "n_eff": float(np.mean(ne)),
            }
        )
    out["legitimate"] = legit

    # Corrupted: same observation set, ancestry degraded, p held fixed.
    p_fixed = estimate_p(args.content_seed, args.cal_episodes, args.n_desc, READ_NOISE, 1)
    corrupt = []
    for knob in (1e6, 9.5, 4.0):
        r, _ = measure("decay", knob, args, p_fixed)
        corrupt.append(
            {
                "decay_tau": knob,
                "p_est": p_fixed,
                "confidence": r.confidence,
                "accuracy": r.accuracy,
                "signed_error": r.signed_error,
                "n_eff": r.n_eff,
            }
        )
    out["corrupted"] = corrupt
    return out


def arm_r4(args, p_est: float) -> Dict[str, object]:
    """P1-R4 as the alpha dial (design note 4.3/7.3), with NO ancestry degradation."""
    rows = []
    vrng = np.random.default_rng([args.content_seed, 51])
    for a in ALPHA_DIAL:
        ne, net, conf, corr = [], [], [], []
        for ep in range(args.episodes):
            store, truth = build_episode(args.content_seed, 40_000 + ep, args.n_desc, alpha=a)
            ids = list(range(store.n()))
            votes = [H.read_vote(store, i, vrng, READ_NOISE, 1) for i in ids]
            n_eff = H.effective_source_count(store, ids)
            ne.append(n_eff)
            net.append(H.true_effective_source_count(truth, ids))
            conf.append(H.confidence(votes, p_est, n_eff))
            corr.append(int((1 if sum(votes) >= 0 else -1) == truth.H))
        rows.append(
            {
                "alpha": a,
                "n_eff_arch": float(np.mean(ne)),
                "n_eff_true": float(np.mean(net)),
                "confidence": float(np.mean(conf)),
                "accuracy": float(np.mean(corr)),
                "signed_error": float(np.mean(conf) - np.mean(corr)),
            }
        )
    return {"rows": rows}


def arm_r7(args, p_est: float) -> Dict[str, object]:
    """P1-R7 fluency versus cardinality (design note 7.5, MANDATORY).

    in_place: ancestry VERIDICAL and cardinality FIXED, only retrieval events move.
    spawn:    the positive control, where retrieval events AND cardinality both move.
    """
    out: Dict[str, List[Dict[str, float]]] = {"in_place": [], "spawn_bound": [], "spawn_degraded": []}
    for mode in ("in_place", "spawn_bound", "spawn_degraded"):
        for n_ret in RETRIEVAL_COUNTS:
            conf, ne, ver, ncard = [], [], [], []
            vrng = np.random.default_rng([args.content_seed, 61, n_ret])
            for ep in range(args.episodes):
                store, truth = build_episode(args.content_seed, 50_000 + ep, args.n_desc)
                crng = np.random.default_rng([args.content_seed, 62, ep, n_ret])
                if n_ret:
                    H.replay(
                        store, truth, 0, n_ret, crng,
                        mode="in_place" if mode == "in_place" else "spawn", t=1.0, eta=ETA,
                    )
                if mode == "spawn_degraded":
                    H.degrade(
                        store, "decay", 9.5, args.steps,
                        np.random.default_rng([args.dynamics_seed, 63, ep, n_ret]),
                        dyn_noise=args.dyn_noise,
                    )
                ids = list(range(store.n()))
                votes = [H.read_vote(store, i, vrng, READ_NOISE, 1) for i in ids]
                n_eff = H.effective_source_count(store, ids)
                conf.append(H.confidence(votes, p_est, n_eff))
                ne.append(n_eff)
                ver.append(int(H.classify_regime(store, truth) == "VERIDICAL"))
                ncard.append(len(ids))
            out[mode].append(
                {
                    "retrieval_events": n_ret,
                    "confidence": float(np.mean(conf)),
                    "n_eff": float(np.mean(ne)),
                    "veridical_rate": float(np.mean(ver)),
                    "n_traces": float(np.mean(ncard)),
                }
            )
    return out


def assert_content_fixed(args) -> Dict[str, object]:
    """C1 / design note 4.4. Content must be bit-identical across ancestry conditions."""
    hashes = {}
    for knob in (1e6, 9.5, 2.5):
        h = []
        for ep in range(min(args.episodes, 40)):
            store, _ = build_episode(args.content_seed, ep, args.n_desc)
            drng = np.random.default_rng([args.dynamics_seed, 11, ep])
            pre = store.content_hash()
            H.degrade(store, "decay", knob, args.steps, drng, dyn_noise=args.dyn_noise)
            assert store.content_hash() == pre, "degrade() mutated trace CONTENT"
            h.append(pre)
        hashes[str(knob)] = h
    ref = list(hashes.values())[0]
    identical = all(v == ref for v in hashes.values())
    if not identical:
        raise SystemExit("C1 FAILED: content differs across ancestry conditions")
    return {"C1_content_identical_across_conditions": identical, "n_checked": len(ref)}


# --------------------------------------------------------------------------------------


def evaluate_preregistered_criteria(res: Dict[str, object]) -> Dict[str, object]:
    out: Dict[str, object] = {}

    # ---- MAIN
    main_ok = {}
    for axis in ("decay", "misbinding"):
        rows = res["main"][axis]
        knobrank = list(range(len(rows)))  # grids are ordered null -> strongest
        ne = [r["n_eff"] for r in rows]
        cf = [r["confidence"] for r in rows]
        ac = [r["accuracy"] for r in rows]
        se = [r["signed_error"] for r in rows]
        main_ok[axis] = {
            "rho_n_eff": spearman(knobrank, ne),
            "rho_confidence": spearman(knobrank, cf),
            "rho_accuracy": spearman(knobrank, ac),
            "rho_signed_error": spearman(knobrank, se),
            "signed_error_at_high_knob": se[-1],
            "n_eff_inflation": ne[-1] - ne[0],
        }
    floor = res["instrument_floor"]["worst_abs_signed_error"]
    infl = min(main_ok[a]["n_eff_inflation"] for a in ("decay", "misbinding"))
    m1 = all(main_ok[a]["rho_n_eff"] >= 0.80 for a in main_ok)

    # M2's accuracy clause was preregistered as "rho_accuracy <= 0.30". Observed accuracy is
    # EXACTLY constant across every knob on both axes -- the strongest possible form of
    # "accuracy does not rise", and a direct consequence of the content-fixed enforcement
    # (design note 4.4): the votes, and therefore the beliefs, are identical across ancestry
    # conditions, so only the genealogy differs. A rank correlation is UNDEFINED on a
    # constant series, so the preregistered statistic returns nan and `nan <= 0.30` is False
    # -- the clause would fail on the ideal outcome. The literal preregistered value is kept
    # and reported; the clause is evaluated on a flatness test that is well defined when the
    # series is constant, which is what the criterion was written to mean.
    def _acc_flat(a: str) -> bool:
        rows = res["main"][a]
        acc = [r["accuracy"] for r in rows]
        rise = acc[-1] - acc[0]
        rho = main_ok[a]["rho_accuracy"]
        main_ok[a]["accuracy_rise_low_to_high_knob"] = rise
        main_ok[a]["accuracy_is_constant"] = bool(len(set(acc)) == 1)
        return rise <= 0.02 and (not np.isfinite(rho) or rho <= 0.30)

    # Evaluated eagerly for BOTH axes so the diagnostics are always populated; `all()` would
    # short-circuit and leave the second axis's flatness fields missing from the report.
    acc_flat = {a: _acc_flat(a) for a in main_ok}
    m2 = all(main_ok[a]["rho_confidence"] >= 0.80 and acc_flat[a] for a in main_ok)
    m3 = all(
        main_ok[a]["rho_signed_error"] >= 0.80 and main_ok[a]["signed_error_at_high_knob"] > 0
        for a in main_ok
    )
    m4 = infl > floor
    out["M_axes"] = main_ok
    out["M1_n_eff_rises"] = m1
    out["M2_confidence_rises_accuracy_flat"] = m2
    out["M3_calibration_degrades"] = m3
    out["M4_clears_instrument_floor"] = {
        "pass": bool(m4),
        "min_n_eff_inflation": infl,
        "instrument_worst_abs_error": floor,
    }
    out["MAIN_PASS"] = bool(m1 and m2 and m3 and m4)

    # ---- R2
    r2 = res["r2"]
    out["R2"] = {
        "assoc_rise": r2["assoc_rise"],
        "n_eff_after_link": r2["n_eff_after_link"],
        "pass": bool(r2["assoc_rise"] >= 0.50 and abs(r2["n_eff_after_link"] - 2.0) <= 0.30),
        "collapse_failure_direction": bool(r2["n_eff_after_link"] < 1.70),
    }

    # ---- R3
    lg, cr = res["r3"]["legitimate"], res["r3"]["corrupted"]
    r3a = (lg[-1]["confidence"] - lg[0]["confidence"] > 0) and (
        cr[-1]["confidence"] - cr[0]["confidence"] > 0
    )
    r3b = abs(lg[-1]["n_eff"] - 1.0) <= 0.30 and (
        lg[-1]["signed_error"] - lg[0]["signed_error"]
    ) <= 0.02
    r3c = (cr[-1]["n_eff"] - cr[0]["n_eff"]) >= 0.50 and (
        cr[-1]["signed_error"] - cr[0]["signed_error"]
    ) >= 0.05
    out["R3"] = {
        "a_both_arms_confidence_rises": bool(r3a),
        "legit_confidence_rise": lg[-1]["confidence"] - lg[0]["confidence"],
        "corrupt_confidence_rise": cr[-1]["confidence"] - cr[0]["confidence"],
        "b_legit_count_flat_calibration_held": bool(r3b),
        "legit_n_eff": lg[-1]["n_eff"],
        "legit_signed_error_delta": lg[-1]["signed_error"] - lg[0]["signed_error"],
        "c_corrupt_count_rises_calibration_degrades": bool(r3c),
        "corrupt_n_eff_rise": cr[-1]["n_eff"] - cr[0]["n_eff"],
        "corrupt_signed_error_delta": cr[-1]["signed_error"] - cr[0]["signed_error"],
        "pass": bool(r3a and r3b and r3c),
        "note": "failure fires supplement falsifier 5 -- untestable as posed, rebuild instruments",
    }

    # ---- R4
    rows = res["r4"]["rows"]
    rho = spearman([r["n_eff_true"] for r in rows], [r["n_eff_arch"] for r in rows])
    conf_rise = rows[-1]["confidence"] - rows[0]["confidence"]
    cal_ok = abs(rows[-1]["signed_error"]) <= abs(rows[0]["signed_error"]) + 0.05
    out["R4"] = {
        "rho_arch_vs_true_count": rho,
        "confidence_rise_alpha1_to_0": conf_rise,
        "calibration_preserved": bool(cal_ok),
        "signed_error_alpha1": rows[0]["signed_error"],
        "signed_error_alpha0": rows[-1]["signed_error"],
        "pass": bool(rho >= 0.80 and conf_rise > 0 and cal_ok),
    }

    # ---- R7
    ip = res["r7"]["in_place"]
    sb, sd = res["r7"]["spawn_bound"], res["r7"]["spawn_degraded"]
    d_ip = ip[-1]["confidence"] - ip[0]["confidence"]
    d_sb = sb[-1]["confidence"] - sb[0]["confidence"]
    d_sd = sd[-1]["confidence"] - sd[0]["confidence"]
    r7pc = d_sd >= 0.02
    r7 = abs(d_ip) <= 0.01
    out["R7"] = {
        "delta_confidence_in_place": d_ip,
        "delta_confidence_spawn_bound": d_sb,
        "delta_confidence_spawn_degraded": d_sd,
        "n_eff_spawn_bound_start_end": [sb[0]["n_eff"], sb[-1]["n_eff"]],
        "n_eff_spawn_degraded_start_end": [sd[0]["n_eff"], sd[-1]["n_eff"]],
        "veridical_rate_in_place": ip[-1]["veridical_rate"],
        "cardinality_in_place_start_end": [ip[0]["n_traces"], ip[-1]["n_traces"]],
        "cardinality_spawn_start_end": [sb[0]["n_traces"], sb[-1]["n_traces"]],
        "pc_pass_dynamic_range": bool(r7pc),
        "pass": bool(r7 and r7pc),
        "fluency_live": bool(not r7),
        "secondary_replay_discounting": (
            "spawn_bound raises cardinality with ancestry INTACT; a correct architecture "
            "must NOT inflate there, so its delta is expected flat and is reported, not gated."
        ),
    }

    out["C1"] = res["content_fixed"]
    out["HEADLINE"] = {
        "main_result_attributable_to_cardinality": bool(out["MAIN_PASS"] and out["R7"]["pass"]),
        "note": (
            "A MAIN pass is reportable as a cardinality effect only if R7 also passes; a "
            "live fluency channel makes the inflation NOT ATTRIBUTABLE (design note 7.5). "
            "R3 failing fires supplement falsifier 5 regardless of MAIN."
        ),
    }
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Provenance P1 -- generated-ancestry assay")
    ap.add_argument("--content-seed", type=int, default=17)
    ap.add_argument("--dynamics-seed", type=int, default=23)
    ap.add_argument("--episodes", type=int, default=2000)
    ap.add_argument("--cal-episodes", type=int, default=4000)
    ap.add_argument("--n-desc", type=int, default=4)
    ap.add_argument("--steps", type=int, default=12)
    ap.add_argument("--dyn-noise", type=float, default=0.35)
    ap.add_argument("--absent-policy", type=str, default="independent", choices=H.ABSENT_POLICIES)
    ap.add_argument("--out-json", type=Path, default=None)
    ap.add_argument("--out-csv", type=Path, default=None)
    args = ap.parse_args()

    res: Dict[str, object] = {}
    res["content_fixed"] = assert_content_fixed(args)
    p_est = estimate_p(args.content_seed, args.cal_episodes, args.n_desc, READ_NOISE, 1)

    main_rows: Dict[str, List[Dict[str, float]]] = {"decay": [], "misbinding": []}
    strat: Dict[str, Dict[str, List[float]]] = {}
    for axis, grid in (("decay", DECAY_KNOBS), ("misbinding", MISBIND_KNOBS)):
        for knob in grid:
            r, rows = measure(axis, knob, args, p_est, args.absent_policy)
            main_rows[axis].append(
                {
                    "knob": knob,
                    "n_eff": r.n_eff,
                    "n_eff_true": r.n_eff_true,
                    "confidence": r.confidence,
                    "accuracy": r.accuracy,
                    "signed_error": r.signed_error,
                    "assoc": r.assoc,
                    "p_external": r.p_external,
                    "fidelity": r.fidelity,
                    "edge_regimes": r.edge_regimes,
                    "episode_regimes": r.episode_regimes,
                }
            )
            for reg, nev, cv, ok in rows:
                s = strat.setdefault(reg, {"n_eff": [], "confidence": [], "correct": []})
                s["n_eff"].append(nev)
                s["confidence"].append(cv)
                s["correct"].append(ok)
    res["main"] = main_rows
    res["stratified_by_edge_regime"] = {
        reg: {
            "n": len(v["n_eff"]),
            "n_eff": float(np.mean(v["n_eff"])),
            "confidence": float(np.mean(v["confidence"])),
            "accuracy": float(np.mean(v["correct"])),
            "signed_error": float(np.mean(v["confidence"]) - np.mean(v["correct"])),
        }
        for reg, v in strat.items()
    }

    res["instrument_floor"] = arm_instrument_floor(args, p_est)
    res["r2"] = arm_r2(args, p_est)
    res["r3"] = arm_r3(args)
    res["r4"] = arm_r4(args, p_est)
    res["r7"] = arm_r7(args, p_est)
    res["p_est"] = p_est

    criteria = evaluate_preregistered_criteria(res)
    payload = {
        "assay": "provenance_p1_false_independence_assay",
        "status": "synthetic_reference_run_only",
        "gated_by": "provenance_genealogy_probe_p0 (REE_assembly b81f9764bc)",
        "architecture_route": "stored-tag (P1-R5 predeclared)",
        "params": {k: (str(v) if isinstance(v, Path) else v) for k, v in vars(args).items()},
        "results": res,
        "criteria": criteria,
    }
    print(json.dumps(payload, indent=2, sort_keys=True, default=float))
    if args.out_json:
        args.out_json.parent.mkdir(parents=True, exist_ok=True)
        args.out_json.write_text(
            json.dumps(payload, indent=2, sort_keys=True, default=float) + "\n", encoding="utf-8"
        )
    if args.out_csv:
        args.out_csv.parent.mkdir(parents=True, exist_ok=True)
        with args.out_csv.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["axis", "knob", "n_eff", "confidence", "accuracy", "signed_error",
                        "p_external", "assoc", "edge_VERIDICAL", "edge_SOFT", "edge_ABSENT",
                        "edge_FALSE_SPLIT"])
            for axis, rows in main_rows.items():
                for r in rows:
                    w.writerow([axis, r["knob"], r["n_eff"], r["confidence"], r["accuracy"],
                                r["signed_error"], r["p_external"], r["assoc"]]
                               + [r["edge_regimes"][k] for k in H.REGIMES])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
