#!/usr/bin/env python3
"""Provenance probe P0 -- genealogy store, degradation processes, endogeneity gate.

This is the GATE for the provenance P1 generated-ancestry harness, specified in
`evidence/planning/provenance_harness_generated_ancestry_design.md` section 9.3.
It builds ONLY the state layer -- a genealogy representation (section 5.1), the three
degradation processes (section 5.2), and the regime classifier (section 5.3) -- and asks
the two questions that decide whether P1 has any content beyond published human work.

It deliberately contains NO descendant content generators, NO confidence computation,
NO posterior over H, NO N_eff readout, NO calibration against world truth, and NO replay
loop. Trace content exists only as a vector supporting a similarity metric, because the
interference and misbinding processes need something to act on. If this file grows a
descendant generator, it has become P1 and the gate has been bypassed.

This is a synthetic measurement probe, not a REE creature experiment, not a queue entry,
and not claim evidence until an authoritative run is reviewed and banked separately.


THE TWO QUESTIONS
-----------------

(a) NON-DEGENERACY   Does a sweep over the decay/interference knob and the misbinding
                     knob produce all four regimes at usable frequencies -- in particular,
                     does the decay axis produce SOFT and ABSENT as DISTINCT, POPULATED
                     regimes rather than collapsing straight to ABSENT?

(b) ENDOGENEITY      At a fixed knob value, does the SET of degraded edges vary across
                     DYNAMICS seeds (store held fixed), and does it correlate with a
                     content/timing statistic of the traces? If the degraded set is
                     predictable from the knob alone, the process is stipulation with
                     extra steps and P1 has no content beyond Yousif 2019 (PMID 31291546),
                     Connor Desai 2022 (PMID 35149359) and Weaver 2007 (PMID 17484607).


PREREGISTERED CRITERIA -- declared here BEFORE any run
------------------------------------------------------

Sweep (a), non-degeneracy. Over the knob grids below, using the three endogenous
processes only (decay, interference, misbinding):

  A1  The decay axis populates SOFT and ABSENT as distinct regimes:
      there is at least one tau at which SOFT   >= 0.15 of episodes,
      at least one tau at which ABSENT >= 0.15 of episodes, and
      at least one tau at which SOFT >= 0.10 AND ABSENT >= 0.10 simultaneously.
      The third clause is the load-bearing one: it is what "distinct and populated
      rather than collapsing straight to ABSENT" means operationally.
  A2  The interference axis satisfies the same three clauses as A1.
  A3  The misbinding axis produces FALSE_SPLIT >= 0.15 of episodes at some rate.
  A4  Classifier non-degeneracy: at the null (zero/negligible) end of all three
      grids, VERIDICAL >= 0.80 of episodes.

  Sweep (a) PASSES iff A1 and A2 and A3 and A4.

Sweep (b), endogeneity. Knob selection rule, declared in advance so it is a rule and
not a tune: for each process, use the knob value from the sweep-(a) grid whose mean
degraded-edge fraction is closest to 0.50 (the maximum-information point; a knob at
which nothing or everything degrades makes the set comparison vacuous).

  B1  Seed-to-seed variation. With the store HELD FIXED and only the dynamics seed
      varying, the mean pairwise Jaccard DISTANCE between degraded-edge sets is
      >= 0.10, for each of decay, interference and misbinding.
  B2  Content/timing dependence. Per store, Spearman rho between each edge's
      degradation PROPENSITY (fraction of dynamics seeds in which it degraded) and
      that process's content/timing statistic. Required, for each of the three:
      mean rho >= 0.30, at least 0.80 of stores with rho > 0, and a within-store
      permutation p < 0.01.
  B3  Discriminative validity -- the test must be able to FAIL, in both directions.
      Three comparators, run identically:
        B3a  stipulation_index    degrades edges chosen by trace index alone.
                                  MUST FAIL B1 and MUST FAIL B2.
        B3b  decay_deterministic  decay with reinstatement noise set to zero.
                                  MUST FAIL B1. (It may pass B2: its degraded set is
                                  content/timing-determined but seed-invariant.)
        B3c  pure_noise           reinstatement noise with no pressure term.
                                  MUST FAIL B2. (It passes B1 trivially.)

  Sweep (b) PASSES iff B1 and B2 hold for all three endogenous processes AND all
  three B3 clauses hold. B1 without B2 is satisfiable by pure noise; B2 without B1
  is satisfiable by a deterministic rule. The conjunction is the criterion, and B3
  is what demonstrates the conjunction is not vacuous.

A FAILING PROBE IS A SUCCESSFUL PROBE. If (b) fails, design-note falsifier 1 and
supplement falsifier 2 fire, and P1 should not be built. That is the outcome this
probe exists to reach for the cost of a probe rather than the cost of a harness.


THE ENDOGENEITY CRITERION, ENFORCED STRUCTURALLY
------------------------------------------------

Design note section 3 requires that no degradation process take an ancestry-indexed
argument and that nothing on the inference path read true ancestry. That is enforced
here by construction, not by discipline:

  * `GenealogyStore` carries content, timestamps, the current edge set and explicit
    family assignments. It carries NO ground-truth ancestry and NO ground-truth family.
  * `GroundTruth` carries those, and is passed ONLY to the scorer (`classify_regime`,
    `degraded_set`) -- never to `run_dynamics` or any process function.
  * The store's edge set is INITIALISED to the true ancestry (the architecture starts
    veridical) and diverges from it under the dynamics. Reading the store's current
    edges is therefore a measurement, not a copy of ground truth.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import numpy as np


REGIMES = ("VERIDICAL", "SOFT", "ABSENT", "FALSE_SPLIT")

ENDOGENOUS_PROCESSES = ("decay", "interference", "misbinding")
COMPARATORS = ("stipulation_index", "decay_deterministic", "pure_noise")
ALL_PROCESSES = ENDOGENOUS_PROCESSES + COMPARATORS

# Knob grids, fixed in advance. Index 0 of each is the null end used by criterion A4.
KNOB_GRIDS: Dict[str, Tuple[float, ...]] = {
    # decay: tau (LARGE tau = slow decay). Pressure per active step is 1/tau.
    "decay": (1e6, 40.0, 20.0, 12.0, 8.0, 5.0, 3.5, 2.5, 1.5),
    "decay_deterministic": (1e6, 40.0, 20.0, 12.0, 8.0, 5.0, 3.5, 2.5, 1.5),
    # interference: gain on the descendant's similarity to OTHER traces.
    "interference": (0.0, 0.05, 0.12, 0.25, 0.45, 0.8, 1.3, 2.2, 3.5),
    # misbinding: per-step re-pointing / relabel rate, scaled by competitor similarity.
    "misbinding": (0.0, 0.005, 0.012, 0.025, 0.05, 0.09, 0.16, 0.28, 0.5),
    # pure_noise: reinstatement-noise magnitude, no pressure term.
    "pure_noise": (0.0, 0.05, 0.12, 0.22, 0.35, 0.5, 0.75, 1.1, 1.7),
    # stipulation_index: fraction of descendants degraded, chosen by index.
    "stipulation_index": (0.0, 0.1, 0.2, 0.3, 0.45, 0.6, 0.75, 0.9, 1.0),
}

# The content/timing statistic each process's degraded set is tested against (B2).
B2_STATISTIC: Dict[str, str] = {
    "decay": "edge_age",
    "decay_deterministic": "edge_age",
    "interference": "sim_to_other_traces",
    "misbinding": "sim_to_nearest_competitor",
    "pure_noise": "edge_age",
    "stipulation_index": "edge_age",
}


# --------------------------------------------------------------------------------------
# State layer: ground truth (scorer only) and the genealogy store (architecture side)
# --------------------------------------------------------------------------------------


@dataclass
class GroundTruth:
    """Scorer-only. Never passed to a degradation process."""

    true_ancestor: np.ndarray  # (n,) int, -1 for roots
    true_family: np.ndarray  # (n,) int
    descendants: np.ndarray  # (n_desc,) int indices with a true ancestor


@dataclass
class GenealogyStore:
    """Design note section 5.1. Carries no ground-truth ancestry or family."""

    content: np.ndarray  # (n, dim) unit-norm
    t: np.ndarray  # (n,) creation time
    sim: np.ndarray  # (n, n) cosine similarity, precomputed (content is static)
    edge_target: np.ndarray  # (n,) int, current ancestor index or -1 (no edge)
    edge_w: np.ndarray  # (n,) binding strength in [0,1]; meaningless where target < 0
    explicit_family: np.ndarray  # (n,) int, an ASSERTED fresh family id, or -1
    next_family_id: int = 0

    def copy(self) -> "GenealogyStore":
        return GenealogyStore(
            content=self.content,  # static, shared
            t=self.t,  # static, shared
            sim=self.sim,  # static, shared
            edge_target=self.edge_target.copy(),
            edge_w=self.edge_w.copy(),
            explicit_family=self.explicit_family.copy(),
            next_family_id=self.next_family_id,
        )


def make_episode(
    rng: np.random.Generator,
    n_roots: int,
    max_desc: int,
    dim: int,
    desc_sigma: float,
    t_max: int,
) -> Tuple[GenealogyStore, GroundTruth]:
    """Build one episode's traces and its veridical initial genealogy.

    Roots are independent source families. Each root gets a variable number of
    descendants whose content is the root's content plus noise -- this is a placeholder
    GEOMETRY so that interference and misbinding have something to act on, NOT one of the
    four descendant kinds of design note section 4.2, which are out of scope for P0.
    Family sizes are deliberately unequal so that the realised content geometry is
    heterogeneous across edges within an episode.
    """
    contents: List[np.ndarray] = []
    times: List[float] = []
    true_anc: List[int] = []
    true_fam: List[int] = []

    for r in range(n_roots):
        c = rng.normal(size=dim)
        c /= np.linalg.norm(c)
        contents.append(c)
        times.append(0.0)
        true_anc.append(-1)
        true_fam.append(r)

    for r in range(n_roots):
        k = int(rng.integers(1, max_desc + 1))
        for _ in range(k):
            c = contents[r] + desc_sigma * rng.normal(size=dim)
            c /= np.linalg.norm(c)
            contents.append(c)
            times.append(float(rng.integers(0, t_max + 1)))
            true_anc.append(r)
            true_fam.append(r)

    content = np.asarray(contents, dtype=float)
    n = content.shape[0]
    sim = content @ content.T
    ta = np.asarray(true_anc, dtype=int)
    tf = np.asarray(true_fam, dtype=int)

    store = GenealogyStore(
        content=content,
        t=np.asarray(times, dtype=float),
        sim=sim,
        edge_target=ta.copy(),  # architecture starts veridical, then diverges
        edge_w=np.where(ta >= 0, 1.0, 0.0),
        explicit_family=np.full(n, -1, dtype=int),
        next_family_id=n_roots + 1000,
    )
    truth = GroundTruth(
        true_ancestor=ta, true_family=tf, descendants=np.where(ta >= 0)[0]
    )
    return store, truth


# --------------------------------------------------------------------------------------
# The three degradation processes (design note section 5.2) and the three comparators.
# Every function below takes ONLY the store, a knob, noise and an rng. None of them can
# see ground-truth ancestry: it is not in scope.
# --------------------------------------------------------------------------------------


def _sim_to_other_traces(store: GenealogyStore, idx: np.ndarray, tgt: np.ndarray) -> np.ndarray:
    """Mean rectified similarity of each descendant to traces OTHER than itself and its
    current ancestor. This is the interference pressure, and it depends only on the
    realised content geometry."""
    relu = np.maximum(store.sim, 0.0)
    n = store.sim.shape[0]
    rows = relu[idx].sum(axis=1) - relu[idx, idx] - relu[idx, tgt]
    return rows / max(n - 2, 1)


def _nearest_competitor(store: GenealogyStore, idx: np.ndarray, tgt: np.ndarray) -> np.ndarray:
    """Index of the most similar trace that is neither the descendant nor its current
    ancestor -- the trace a misbinding would re-point to."""
    relu = np.maximum(store.sim, 0.0)
    m = relu[idx].copy()
    ar = np.arange(len(idx))
    m[ar, idx] = -1.0
    m[ar, tgt] = -1.0
    return m.argmax(axis=1)


def run_dynamics(
    store: GenealogyStore,
    process: str,
    knob: float,
    rng: np.random.Generator,
    steps: int,
    dyn_noise: float,
    mis_gamma: float,
    mis_split_frac: float,
) -> None:
    """Run `process` at `knob` for `steps` steps, mutating `store` in place.

    An edge only degrades once its descendant exists (t_d <= step), so total accumulated
    pressure scales with the edge's AGE. That is what makes the decay axis depend on the
    realised timing pattern rather than on the knob alone.
    """
    if process == "stipulation_index":
        # Applied once, at the end. Degrades descendants chosen by INDEX -- a rule that
        # reads neither content, nor timing, nor the dynamics seed. This is the thing the
        # endogeneity criterion is supposed to reject.
        desc = np.where(store.edge_target >= 0)[0]
        k = int(math.ceil(knob * len(desc)))
        if k > 0:
            store.edge_w[desc[:k]] = 0.05
        return

    eta = 0.0 if process == "decay_deterministic" else dyn_noise
    if process == "pure_noise":
        eta = knob

    if process == "pure_noise":
        # The comparator: an unstructured multiplicative walk on binding strength with NO
        # pressure term -- "degradation driven by noise alone", which is what it must
        # instantiate in order to fail B2.
        #
        # EXPOSURE-MATCHED, deliberately, and this is the whole subtlety of the control.
        # The endogenous processes act on an edge only once its descendant exists
        # (t_d <= step), so an older edge accumulates more applications and its degradation
        # correlates with age for that reason ALONE. A noise comparator gated the same way
        # inherits that correlation and passes B2 while carrying no content or timing
        # structure of its own -- it is then not a negative control at all. Applying the
        # noise to every edge on every step removes the exposure channel and leaves only
        # the seed, which is the intended comparator.
        idx_all = np.where(store.edge_target >= 0)[0]
        if idx_all.size:
            for _ in range(steps):
                store.edge_w[idx_all] = np.clip(
                    store.edge_w[idx_all]
                    * np.exp(-np.abs(knob * rng.normal(size=idx_all.size))),
                    0.0,
                    1.0,
                )
        return

    for step in range(1, steps + 1):
        active = (store.edge_target >= 0) & (store.t <= step)
        idx = np.where(active)[0]
        if idx.size == 0:
            continue
        tgt = store.edge_target[idx]

        if process == "misbinding":
            comp = _nearest_competitor(store, idx, tgt)
            p_fire = np.clip(
                knob * np.maximum(store.sim[idx, comp], 0.0) ** mis_gamma, 0.0, 1.0
            )
            fires = rng.random(idx.size) < p_fire
            splits = rng.random(idx.size) < mis_split_frac
            for j in np.where(fires)[0]:
                d = int(idx[j])
                if splits[j]:
                    # Assert a fresh source family: a POSITIVE, confident claim of
                    # independence. This is the only route to FALSE_SPLIT that does not
                    # require an emergent confident mis-attachment.
                    store.explicit_family[d] = store.next_family_id
                    store.next_family_id += 1
                    store.edge_target[d] = -1
                else:
                    # Re-point the edge, preserving strength: a confident wrong binding.
                    store.edge_target[d] = int(comp[j])
            continue

        if process in ("decay", "decay_deterministic"):
            pressure = np.full(idx.size, 1.0 / knob if knob > 0 else 0.0)
        elif process == "interference":
            pressure = knob * _sim_to_other_traces(store, idx, tgt)
        else:  # pragma: no cover - guarded by argparse choices
            raise ValueError("unknown process: %s" % process)

        # Reinstatement noise SCALES the pressure rather than being added to the binding
        # strength directly. This matters: an additive multiplicative walk on w has a
        # reflecting ceiling at 1.0 and therefore drifts downward, so it acts as a second,
        # uncontrolled degradation process and leaves the knob's null end already
        # degraded. Scaling the pressure keeps the null end veridical and keeps the noise
        # a genuine trial-to-trial perturbation of how much a retrieval costs a binding.
        if eta > 0:
            pressure = np.maximum(pressure * (1.0 + eta * rng.normal(size=idx.size)), 0.0)
        store.edge_w[idx] = np.clip(store.edge_w[idx] * np.exp(-pressure), 0.0, 1.0)


# --------------------------------------------------------------------------------------
# Scorer: regime classification (design note section 5.3) and the degraded set.
# These are the ONLY functions that see GroundTruth.
# --------------------------------------------------------------------------------------


class _UnionFind:
    def __init__(self, n: int) -> None:
        self.p = list(range(n))

    def find(self, a: int) -> int:
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra


def classify_regime(
    store: GenealogyStore, truth: GroundTruth, theta_high: float, theta_low: float
) -> str:
    """Classify one episode into VERIDICAL / SOFT / ABSENT / FALSE_SPLIT.

    Order of precedence, and why:

      FALSE_SPLIT dominates, because it is a POSITIVE and wrong belief and therefore the
      most consequential state, and because it is exactly what design note section 5.3
      insists must not be collapsed into ABSENT. A descendant counts as falsely split
      only if the architecture CONFIDENTLY places it outside its true ancestor's derived
      family -- either by asserting a fresh family id, or by holding an above-threshold
      edge into a component that does not contain the true ancestor. An edge that has
      merely faded leaves the descendant UNASSIGNED, which is ABSENT, not a false split.

      Otherwise the episode is scored by its WORST surviving true edge: all above
      theta_high -> VERIDICAL; none below theta_low -> SOFT; otherwise ABSENT. A true
      edge that has been re-pointed or removed has effective strength 0.
    """
    n = store.content.shape[0]
    uf = _UnionFind(n)
    confident = (store.edge_target >= 0) & (store.edge_w >= theta_high)
    for d in np.where(confident)[0]:
        if store.explicit_family[d] < 0:
            uf.union(int(d), int(store.edge_target[d]))

    false_split = False
    for d in truth.descendants:
        d = int(d)
        a = int(truth.true_ancestor[d])
        if store.explicit_family[d] >= 0:
            false_split = True
            break
        if confident[d] and uf.find(d) != uf.find(a):
            false_split = True
            break
    if false_split:
        return "FALSE_SPLIT"

    eff = np.zeros(len(truth.descendants))
    for i, d in enumerate(truth.descendants):
        d = int(d)
        if store.edge_target[d] == truth.true_ancestor[d]:
            eff[i] = store.edge_w[d]
    if eff.size == 0:
        return "VERIDICAL"
    if eff.min() >= theta_high:
        return "VERIDICAL"
    if eff.min() >= theta_low:
        return "SOFT"
    return "ABSENT"


def classify_edges(
    store: GenealogyStore, truth: GroundTruth, theta_high: float, theta_low: float
) -> Dict[str, int]:
    """Per-EDGE regime counts, using the same precedence as `classify_regime`.

    Reported as a DIAGNOSTIC, never as a preregistered criterion: design note section 5.3
    defines the four conditions per EPISODE, and criterion A is evaluated on episodes.
    The edge-level view exists because the episode-level classifier scores an episode by
    its WORST surviving true edge, which can make SOFT and ABSENT look nearly mutually
    exclusive at episode level even when both are well populated at edge level.
    """
    n = store.content.shape[0]
    uf = _UnionFind(n)
    confident = (store.edge_target >= 0) & (store.edge_w >= theta_high)
    for d in np.where(confident)[0]:
        if store.explicit_family[d] < 0:
            uf.union(int(d), int(store.edge_target[d]))

    counts = {r: 0 for r in REGIMES}
    for d in truth.descendants:
        d = int(d)
        a = int(truth.true_ancestor[d])
        if store.explicit_family[d] >= 0 or (confident[d] and uf.find(d) != uf.find(a)):
            counts["FALSE_SPLIT"] += 1
            continue
        eff = store.edge_w[d] if store.edge_target[d] == truth.true_ancestor[d] else 0.0
        if eff >= theta_high:
            counts["VERIDICAL"] += 1
        elif eff >= theta_low:
            counts["SOFT"] += 1
        else:
            counts["ABSENT"] += 1
    return counts


def degraded_set(
    store: GenealogyStore, truth: GroundTruth, theta_high: float
) -> np.ndarray:
    """Boolean vector over descendants: which true ancestry edges left the veridical band,
    by fading, re-pointing or relabelling."""
    out = np.zeros(len(truth.descendants), dtype=bool)
    for i, d in enumerate(truth.descendants):
        d = int(d)
        if store.explicit_family[d] >= 0:
            out[i] = True
        elif store.edge_target[d] != truth.true_ancestor[d]:
            out[i] = True
        elif store.edge_w[d] < theta_high:
            out[i] = True
    return out


def b2_statistic(
    store: GenealogyStore, truth: GroundTruth, process: str, steps: int
) -> np.ndarray:
    """The content/timing statistic the degraded set is tested against, computed on the
    INITIAL (undegraded) store, so it is a property of the episode and not of any run."""
    desc = truth.descendants
    tgt = truth.true_ancestor[desc]
    if B2_STATISTIC[process] == "edge_age":
        return steps - store.t[desc]
    if B2_STATISTIC[process] == "sim_to_other_traces":
        return _sim_to_other_traces(store, desc, tgt)
    comp = _nearest_competitor(store, desc, tgt)
    return np.maximum(store.sim[desc, comp], 0.0)


# --------------------------------------------------------------------------------------
# Statistics
# --------------------------------------------------------------------------------------


def _avg_rank(x: np.ndarray) -> np.ndarray:
    order = np.argsort(x, kind="mergesort")
    ranks = np.empty(x.size, dtype=float)
    ranks[order] = np.arange(x.size, dtype=float)
    xs = x[order]
    i = 0
    while i < xs.size:
        j = i
        while j + 1 < xs.size and xs[j + 1] == xs[i]:
            j += 1
        if j > i:
            ranks[order[i : j + 1]] = np.mean(ranks[order[i : j + 1]])
        i = j + 1
    return ranks


def spearman(a: np.ndarray, b: np.ndarray) -> float:
    if a.size < 3:
        return float("nan")
    ra, rb = _avg_rank(a), _avg_rank(b)
    sa, sb = ra.std(), rb.std()
    if sa == 0.0 or sb == 0.0:
        return float("nan")
    return float(((ra - ra.mean()) * (rb - rb.mean())).mean() / (sa * sb))


def mean_pairwise_jaccard_distance(sets: np.ndarray) -> float:
    """`sets` is (n_seeds, n_edges) boolean. Two seeds that degraded nothing are treated
    as identical (distance 0) -- the conservative choice, since it counts against B1."""
    n = sets.shape[0]
    dists: List[float] = []
    for i in range(n):
        for j in range(i + 1, n):
            inter = np.logical_and(sets[i], sets[j]).sum()
            union = np.logical_or(sets[i], sets[j]).sum()
            dists.append(0.0 if union == 0 else 1.0 - inter / union)
    return float(np.mean(dists)) if dists else float("nan")


def permutation_p_mean_rho(
    props: Sequence[np.ndarray],
    stats: Sequence[np.ndarray],
    observed: float,
    rng: np.random.Generator,
    n_perm: int,
) -> float:
    """One-sided permutation test on the mean per-store Spearman rho, permuting the
    statistic WITHIN each store so the store structure is preserved."""
    if not np.isfinite(observed):
        return float("nan")
    hits = 0
    for _ in range(n_perm):
        rhos = []
        for p, s in zip(props, stats):
            r = spearman(p, s[rng.permutation(s.size)])
            if np.isfinite(r):
                rhos.append(r)
        m = float(np.mean(rhos)) if rhos else float("nan")
        if np.isfinite(m) and m >= observed:
            hits += 1
    return (hits + 1.0) / (n_perm + 1.0)


# --------------------------------------------------------------------------------------
# Sweeps
# --------------------------------------------------------------------------------------


@dataclass
class SweepRow:
    process: str
    knob: float
    n_episodes: int
    veridical: float = 0.0
    soft: float = 0.0
    absent: float = 0.0
    false_split: float = 0.0
    mean_degraded_fraction: float = 0.0
    regime_counts: Dict[str, int] = field(default_factory=dict)
    edge_fractions: Dict[str, float] = field(default_factory=dict)


def sweep_non_degeneracy(args: argparse.Namespace) -> Dict[str, List[SweepRow]]:
    out: Dict[str, List[SweepRow]] = {}
    for process in ALL_PROCESSES:
        rows: List[SweepRow] = []
        for knob in KNOB_GRIDS[process]:
            counts = {r: 0 for r in REGIMES}
            edge_counts = {r: 0 for r in REGIMES}
            degraded_fracs: List[float] = []
            for ep in range(args.episodes):
                store_rng = np.random.default_rng([args.seed, 101, ep])
                store, truth = make_episode(
                    store_rng, args.roots, args.max_desc, args.dim, args.desc_sigma, args.t_max
                )
                dyn_rng = np.random.default_rng([args.seed, 202, ep])
                run_dynamics(
                    store, process, knob, dyn_rng, args.steps,
                    args.dyn_noise, args.mis_gamma, args.mis_split_frac,
                )
                counts[classify_regime(store, truth, args.theta_high, args.theta_low)] += 1
                for r, c in classify_edges(store, truth, args.theta_high, args.theta_low).items():
                    edge_counts[r] += c
                degraded_fracs.append(float(degraded_set(store, truth, args.theta_high).mean()))
            n = float(args.episodes)
            rows.append(
                SweepRow(
                    process=process,
                    knob=knob,
                    n_episodes=args.episodes,
                    veridical=counts["VERIDICAL"] / n,
                    soft=counts["SOFT"] / n,
                    absent=counts["ABSENT"] / n,
                    false_split=counts["FALSE_SPLIT"] / n,
                    mean_degraded_fraction=float(np.mean(degraded_fracs)),
                    regime_counts=counts,
                    edge_fractions={
                        r: edge_counts[r] / max(sum(edge_counts.values()), 1) for r in REGIMES
                    },
                )
            )
        out[process] = rows
    return out


def select_knob_for_endogeneity(rows: List[SweepRow]) -> float:
    """Declared rule: the grid value whose mean degraded fraction is closest to 0.50."""
    return min(rows, key=lambda r: abs(r.mean_degraded_fraction - 0.50)).knob


def sweep_endogeneity(
    args: argparse.Namespace, sweep_a: Dict[str, List[SweepRow]]
) -> Dict[str, Dict[str, object]]:
    results: Dict[str, Dict[str, object]] = {}
    perm_rng = np.random.default_rng([args.seed, 999])

    for process in ALL_PROCESSES:
        knob = select_knob_for_endogeneity(sweep_a[process])
        jaccards: List[float] = []
        props: List[np.ndarray] = []
        stats: List[np.ndarray] = []

        for st in range(args.stores):
            store_rng = np.random.default_rng([args.seed, 303, st])
            base_store, truth = make_episode(
                store_rng, args.roots, args.max_desc, args.dim, args.desc_sigma, args.t_max
            )
            stat = b2_statistic(base_store, truth, process, args.steps)

            sets = np.zeros((args.dyn_seeds, len(truth.descendants)), dtype=bool)
            for k in range(args.dyn_seeds):
                store = base_store.copy()
                dyn_rng = np.random.default_rng([args.seed, 404, st, k])
                run_dynamics(
                    store, process, knob, dyn_rng, args.steps,
                    args.dyn_noise, args.mis_gamma, args.mis_split_frac,
                )
                sets[k] = degraded_set(store, truth, args.theta_high)

            jaccards.append(mean_pairwise_jaccard_distance(sets))
            props.append(sets.mean(axis=0))
            stats.append(stat)

        rhos = [spearman(p, s) for p, s in zip(props, stats)]
        finite = [r for r in rhos if np.isfinite(r)]
        mean_rho = float(np.mean(finite)) if finite else float("nan")
        frac_pos = float(np.mean([r > 0 for r in finite])) if finite else float("nan")
        p_perm = permutation_p_mean_rho(props, stats, mean_rho, perm_rng, args.permutations)
        mean_jac = float(np.nanmean(jaccards))

        results[process] = {
            "knob_selected": knob,
            "knob_selection_rule": "grid value with mean degraded fraction closest to 0.50",
            "mean_degraded_fraction_at_knob": next(
                r.mean_degraded_fraction for r in sweep_a[process] if r.knob == knob
            ),
            "statistic": B2_STATISTIC[process],
            "B1_mean_pairwise_jaccard_distance": mean_jac,
            "B1_pass": bool(np.isfinite(mean_jac) and mean_jac >= args.b1_threshold),
            "B2_mean_spearman_rho": mean_rho,
            "B2_fraction_stores_rho_positive": frac_pos,
            "B2_permutation_p": p_perm,
            "B2_pass": bool(
                np.isfinite(mean_rho)
                and mean_rho >= args.b2_rho_threshold
                and np.isfinite(frac_pos)
                and frac_pos >= 0.80
                and np.isfinite(p_perm)
                and p_perm < 0.01
            ),
            "n_stores": args.stores,
            "n_dynamics_seeds": args.dyn_seeds,
        }
    return results


# --------------------------------------------------------------------------------------
# Preregistered criteria
# --------------------------------------------------------------------------------------


def evaluate_preregistered_criteria(
    sweep_a: Dict[str, List[SweepRow]], sweep_b: Dict[str, Dict[str, object]]
) -> Dict[str, object]:
    def clauses(process: str) -> Dict[str, object]:
        rows = sweep_a[process]
        has_soft = any(r.soft >= 0.15 for r in rows)
        has_absent = any(r.absent >= 0.15 for r in rows)
        coexist = any(r.soft >= 0.10 and r.absent >= 0.10 for r in rows)
        return {
            "soft_reaches_0.15": has_soft,
            "absent_reaches_0.15": has_absent,
            "soft_and_absent_coexist_at_0.10": coexist,
            "max_soft": max(r.soft for r in rows),
            "max_absent": max(r.absent for r in rows),
            "max_min_of_soft_absent": max(min(r.soft, r.absent) for r in rows),
            "pass": bool(has_soft and has_absent and coexist),
            "DIAGNOSTIC_edge_level_max_min_of_soft_absent": max(
                min(r.edge_fractions["SOFT"], r.edge_fractions["ABSENT"]) for r in rows
            ),
        }

    a1 = clauses("decay")
    a2 = clauses("interference")
    max_fs = max(r.false_split for r in sweep_a["misbinding"])
    a3 = {"max_false_split": max_fs, "pass": bool(max_fs >= 0.15)}
    nulls = {p: sweep_a[p][0].veridical for p in ENDOGENOUS_PROCESSES}
    a4 = {
        "veridical_at_null_end": nulls,
        "pass": bool(all(v >= 0.80 for v in nulls.values())),
    }
    sweep_a_pass = bool(a1["pass"] and a2["pass"] and a3["pass"] and a4["pass"])

    b1 = {p: sweep_b[p]["B1_pass"] for p in ENDOGENOUS_PROCESSES}
    b2 = {p: sweep_b[p]["B2_pass"] for p in ENDOGENOUS_PROCESSES}
    b3 = {
        "B3a_stipulation_index_fails_B1": not sweep_b["stipulation_index"]["B1_pass"],
        "B3a_stipulation_index_fails_B2": not sweep_b["stipulation_index"]["B2_pass"],
        "B3b_decay_deterministic_fails_B1": not sweep_b["decay_deterministic"]["B1_pass"],
        "B3c_pure_noise_fails_B2": not sweep_b["pure_noise"]["B2_pass"],
    }
    sweep_b_pass = bool(all(b1.values()) and all(b2.values()) and all(b3.values()))

    return {
        "A1_decay_axis_soft_and_absent_distinct": a1,
        "A2_interference_axis_soft_and_absent_distinct": a2,
        "A3_misbinding_axis_produces_false_split": a3,
        "A4_classifier_non_degenerate_at_null": a4,
        "sweep_a_non_degeneracy_PASS": sweep_a_pass,
        "B1_seed_to_seed_variation": b1,
        "B2_content_timing_dependence": b2,
        "B3_discriminative_validity": b3,
        "sweep_b_endogeneity_PASS": sweep_b_pass,
        "verdict_build_P1": bool(sweep_a_pass and sweep_b_pass),
        "verdict_note": (
            "sweep (b) is the decisive gate: if it fails, design-note falsifier 1 and "
            "supplement falsifier 2 fire and P1 should not be built. If (a) fails while "
            "(b) passes, the process families need reworking before P1, not abandonment."
        ),
    }


# --------------------------------------------------------------------------------------


def write_csv(path: Path, sweep_a: Dict[str, List[SweepRow]]) -> None:
    fields = [
        "process", "knob", "n_episodes", "veridical", "soft", "absent",
        "false_split", "mean_degraded_fraction",
        "edge_veridical", "edge_soft", "edge_absent", "edge_false_split",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for process in ALL_PROCESSES:
            for r in sweep_a[process]:
                row = {k: getattr(r, k) for k in fields if not k.startswith("edge_")}
                for reg in REGIMES:
                    row["edge_" + reg.lower()] = r.edge_fractions.get(reg, 0.0)
                w.writerow(row)


def main() -> int:
    p = argparse.ArgumentParser(description="Provenance probe P0 -- genealogy endogeneity gate")
    p.add_argument("--seed", type=int, default=11)
    p.add_argument("--episodes", type=int, default=200, help="episodes per knob value, sweep (a)")
    p.add_argument("--stores", type=int, default=40, help="distinct stores, sweep (b)")
    p.add_argument("--dyn-seeds", type=int, default=30, help="dynamics seeds per store, sweep (b)")
    p.add_argument("--permutations", type=int, default=1000)
    p.add_argument("--roots", type=int, default=4)
    p.add_argument("--max-desc", type=int, default=4)
    p.add_argument("--dim", type=int, default=8)
    p.add_argument("--desc-sigma", type=float, default=0.55)
    p.add_argument("--t-max", type=int, default=8)
    p.add_argument("--steps", type=int, default=12)
    p.add_argument("--dyn-noise", type=float, default=0.35, help="reinstatement noise (permitted knob, design note section 3)")
    p.add_argument("--mis-gamma", type=float, default=2.0)
    p.add_argument("--mis-split-frac", type=float, default=0.5)
    p.add_argument("--theta-high", type=float, default=0.60)
    p.add_argument("--theta-low", type=float, default=0.25)
    p.add_argument("--b1-threshold", type=float, default=0.10)
    p.add_argument("--b2-rho-threshold", type=float, default=0.30)
    p.add_argument("--out-json", type=Path, default=None)
    p.add_argument("--out-csv", type=Path, default=None)
    args = p.parse_args()

    if not 0.0 <= args.theta_low < args.theta_high <= 1.0:
        raise SystemExit("require 0 <= --theta-low < --theta-high <= 1")

    sweep_a = sweep_non_degeneracy(args)
    sweep_b = sweep_endogeneity(args, sweep_a)
    criteria = evaluate_preregistered_criteria(sweep_a, sweep_b)

    payload = {
        "probe": "provenance_genealogy_probe_p0",
        "status": "synthetic_probe_run_only",
        "gates": "provenance P1 generated-ancestry harness (design note section 9.3)",
        "params": {k: (str(v) if isinstance(v, Path) else v) for k, v in vars(args).items()},
        "knob_grids": {k: list(v) for k, v in KNOB_GRIDS.items()},
        "sweep_a_non_degeneracy": {
            proc: [
                {
                    "knob": r.knob,
                    "VERIDICAL": r.veridical,
                    "SOFT": r.soft,
                    "ABSENT": r.absent,
                    "FALSE_SPLIT": r.false_split,
                    "mean_degraded_fraction": r.mean_degraded_fraction,
                    "edge_level": r.edge_fractions,
                }
                for r in rows
            ]
            for proc, rows in sweep_a.items()
        },
        "sweep_b_endogeneity": sweep_b,
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
        write_csv(args.out_csv, sweep_a)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
