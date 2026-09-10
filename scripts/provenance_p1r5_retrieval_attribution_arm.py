#!/usr/bin/env python3
"""Provenance P1-R5 -- the retrieval-attribution arm, and the stored-tag/attribution
discriminator.

Companion to `provenance_p1_false_independence_assay.py` (the stored-tag driver, whose
result is `evidence/planning/provenance_p1_result.md`, REE_assembly 062d774289) and to
`provenance_genealogy_harness.py` (the shared state layer).

WHY THIS EXISTS
---------------

P1 predeclared its route: "This harness implements the STORED-TAG route. Source structure
lives in persistent ancestry edges that the dynamics degrade; `source_attribution` READS
that stored structure at retrieval time." Its epistemic boundary is correspondingly
narrow -- "the result is about the stored-tag route only (P1-R5, predeclared). A
read-time-attribution architecture is a different system, not a parameter of this one."

`provenance_branch_hippocampal_audit_verification_20260910.md` section 6 argues that the
founding source-monitoring framework (Johnson, Hashtroudi & Lindsay 1993, PMID 8346328)
DENIES the stored-tag premise: memories do not arrive labelled; source is reconstructed at
retrieval from qualitative features weighed against a criterion that shifts with task,
motivation and care. Section 7 specifies P1-R5 as the remedy -- an ARM, not a redesign.

This module is that arm. It is not evidence about humans, about psychosis, or about which
route the human effect runs on. It is a measurement of two synthetic architectures.


WHY THE HARNESS IS NOT EDITED, AND WHAT IS REIMPLEMENTED INSTEAD
----------------------------------------------------------------

The harness's module docstring predeclares it as the stored-tag route and says a read-time
variant "is a different architecture, not a parameter of this one". Adding a read-time path
to that file would falsify its own predeclaration and would touch a file P1's landed result
and P3's design both depend on. So the attribution route lives HERE and the harness is
imported unmodified.

The cost of that choice is that the N_eff AGGREGATION -- the `absent_policy` fill plus
`sum_i 1 / (1 + dep_i)` -- had to be reimplemented here so that it can be applied to a
pairwise matrix the attribution route computes rather than to a store. A reimplementation
that drifted from the harness would silently invalidate every route comparison in this
file, because the whole design rests on the two routes differing in EXACTLY ONE place (how
the pairwise matrix P is built) and sharing everything downstream.

That risk is closed by a hard gate rather than by care: `assert_aggregation_equivalence()`
builds randomised stores, computes P from `H.shared_ancestry_prob`, and asserts
`aggregate_n_eff(P, policy) == H.effective_source_count(store, ids, policy)` to 1e-12 for
all three policies. It runs first, and a mismatch aborts the run. Every result below is
therefore computed by the harness's own aggregation semantics, verified, not assumed.


THE TWO ROUTES, STATED AS THE ONE DIFFERENCE THEY ARE
------------------------------------------------------

Both routes end in the identical aggregation and the identical confidence rule
(`H.confidence`). Both see identical content, identical votes and identical accuracy at a
given content seed -- P1's content-fixed discipline (design note 4.4) extended across
routes, which is what makes a confidence difference between routes attributable to N_eff
alone. They differ only in how the pairwise matrix is built:

  STORED-TAG    P[i][j] = H.shared_ancestry_prob(store, i, j)
                -- the product of STORED binding strengths along the ancestry paths to the
                   lowest common ancestor. Degradation acts on those strengths. No
                   read-time parameter enters at all.

  ATTRIBUTION   P[i][j] = sigmoid(BETA * (score(i,j) - C))
                -- a judgement made at read time from QUALITATIVE TRACE FEATURES, against a
                   shiftable criterion C. The stored ancestry edge set is HELD CONSTANT and
                   never consulted.

`score` is Johnson 1993's three feature families, mapped onto what a harness trace
actually carries:

  perceptual / content detail        -> rectified cosine similarity of stored content
  contextual, semantic accompaniment -> temporal proximity, exp(-|t_i - t_j| / TAU_CTX)
  recorded cognitive operations      -> `store.retrieval_events`, the count of retrieval /
                                        reinstatement events the architecture has recorded
                                        against a trace. In Johnson's account recollected
                                        cognitive operations are diagnostic of INTERNAL
                                        generation, so a pair both of whose members carry
                                        operation records is more likely one lineage.

The association edge set is deliberately NOT a feature. Feeding it into the count is
exactly the "collapses distinct sources" failure that the harness's two-edge-set separation
exists to prevent (harness docstring, P1-R2), and it would make this route fail P1-R2 for a
structural reason rather than an empirical one.

Weights and BETA are FIXED CONSTANTS declared below, not fitted. The one fitted quantity is
the reference criterion C_STAR, and it is fitted on a CALIBRATION SPLIT with a different
content seed from every reported number -- the same discipline `estimate_p` uses in the P1
driver, and for the same reason.


WHAT "INFLATION" MEANS ON A ROUTE WITH NO STORAGE-LOSS AXIS
------------------------------------------------------------

The stored-tag route's dose-response axis is degradation: intact ancestry -> corrupted
ancestry. The attribution route has no such axis; nothing about it degrades, because it
reads no stored structure. Its analogue of "corruption" is the CRITERION: a strict
criterion demands strong featural evidence before judging two traces to share a source, and
therefore proliferates apparent independent sources.

So the two routes are made commensurable at their INTACT ends and compared on the range
they can reach:

  stored-tag   intact = no degradation;         corrupted = the P1 decay grid's far end
  attribution  intact = criterion C_STAR, fitted so that its N_eff matches the stored-tag
                        route's UNDEGRADED N_eff on the calibration split;
               corrupted = the far end of the criterion grid

Fitting C_STAR is what makes A5 (magnitude comparability) a fair test rather than an
artifact of where the criterion grid happens to start.


PREREGISTERED CRITERIA -- fixed in this docstring, in the same commit as the code, before
the authoritative run. Thresholds declared up front; results reported whichever way they
come out. Amendments made after smoke runs and BEFORE the authoritative run are disclosed
in full at the bottom of this docstring.

Three of the ten are labelled STRUCTURAL. They are entailments of the two routes'
definitions and are included as IMPLEMENTATION CHECKS, not findings -- exactly as the P1
result note records "accuracy being exactly flat is enforced by construction, not
discovered", and as the design note's P0 correction records that "decay never yields
FALSE_SPLIT" is definitional. A structural check that FAILED would indicate a bug here.

  A1  STRUCTURAL. Stored-tag N_eff is invariant across the criterion grid at fixed storage.
      range <= 1e-12.

  A2  Attribution N_eff MOVES with the criterion at fixed storage: range >= 1.000. (The P1
      count instrument's own worst signed error is 0.2215; 1.000 clears that floor by 4.5x,
      so a pass cannot be instrument bias.)

  A3  STRUCTURAL. Attribution N_eff is invariant across the decay grid at fixed criterion.
      range <= 1e-12.

  A4  REPRODUCTION. Stored-tag N_eff moves across the decay grid: range >= 3.000. This
      re-derives P1's headline (1.117 -> 4.869, +3.753) through this module's own episode
      builder, and a failure would mean this module does not reproduce the run it compares
      against.

  A5  MAGNITUDE COMPARABILITY. The attribution route's criterion-driven inflation, measured
      from C_STAR, reaches >= 3.753 (P1's landed stored-tag inflation) somewhere on the
      criterion grid.
        PASS  -> BOTH routes inflate; the effect is architecture-independent.
        FAIL  -> only the stored-tag route reaches it; P1's positive result is about REE's
                 chosen implementation rather than about provenance representation.
      **A PASS HERE IS NEAR-DEFINITIONAL AND MUST BE REPORTED AS SUCH.** Both routes feed
      the identical aggregation, and that aggregation returns N_eff = n whenever every
      pairwise entry is driven to zero. Any route with a parameter that can drive its
      pairwise matrix to zero therefore inflates. That is not a weakness of the test -- it
      is the result, and it is the same shape as P1's own "the count inflation is
      near-definitional given an independence default". The substantive content of this
      module is A1/A3 (the two axes are orthogonal), A6 (whether the same readout default
      is the locus on both routes), A7/A8 (WHERE similarity acts) and A9 (which readout
      fluency reaches). To keep the magnitude interpretable rather than merely large,
      `frac_pairs_above_criterion` is reported at every grid point: it says directly how
      much of the judgement distribution the criterion has swept past.

  A6  ABSENT-POLICY CROSSING. Predeclared prediction, tested on BOTH routes over the MAX of
      each route's own axis (not its endpoint -- a policy that eliminates inflation at the
      extreme while permitting it mid-axis has not eliminated it): the `dependent` policy
      eliminates the inflation (|inflation| <= 0.30) and the `soft` policy degenerates to
      `independent` (|inflation_soft - inflation_independent| <= 0.30). P1 found exactly
      this on the stored-tag route (+3.753 / -0.117 / +3.883); the prediction under test is
      that it also holds on a route with no stored tag to lose.

  A7  READ-TIME SIMILARITY SENSITIVITY. With storage entirely untouched (zero degradation),
      the attribution route's CROSS-FAMILY CONFUSION -- mean judged shared-source
      probability between traces of genuinely different world events, a scorer-side
      measure -- rises with the candidate-source similarity dial: Spearman rho >= 0.90.

  A7b CONTROL for A7. The similarity dial must not move the vote axis. Accuracy range
      across the kappa grid <= 0.020. (It is NOT exactly invariant -- see amendment 5.)

  A8  MEASUREMENT, two-branch decision rule, no pass/fail. Section 6 credits the stored-tag
      route with a similarity sensitivity reached through the misbinding process. This
      measures whether that is realised: stored-tag cross-family confusion across the kappa
      grid, with no degradation and under misbinding, against the attribution route's.
        branch STORAGE_TIME_REALISED  -- stored-tag X_max > 0.010: similarity reaches the
              stored-tag edge set via misbinding, as section 6 supposed, and the routes
              differ in WHEN similarity acts rather than in whether it can.
        branch ATTRIBUTION_ONLY       -- stored-tag X_max <= 0.010 while attribution
              X_max > 0.010: similarity-driven cross-family confusion is available on the
              attribution route ONLY, and section 6's supposition is not realised here.
      The cross-family re-point FRACTION is reported alongside, so the branch is explained
      by a measured mechanism rather than inferred from a null.

  A9  FLUENCY (P1-R7's axis, crossed with route), split across TWO READOUTS because the
      branch's standing rule is never to collapse them. In-place retrieval events at FIXED
      descendant cardinality and fixed storage.
        A9a readout 3, cardinality.  Stored-tag |delta N_eff| <= 1e-12 (STRUCTURAL --
            retrieval_events is not an input to shared_ancestry_prob). Attribution
            |delta N_eff| >= 0.050.
        A9b readout 2, source attribution. Stored-tag |relative delta p_external| <= 1e-12
            (STRUCTURAL). Attribution |relative delta p_external| >= 0.100.
      Direction on the attribution route is predeclared NEGATIVE on both readouts
      (recorded cognitive operations are diagnostic of internal generation, so repeated
      retrieval should make traces read as MORE likely to share a source and LESS likely to
      be external) and is reported whichever way it comes out.

SEEDS. The primary run uses content 17 / dynamics 23 -- P1's own seeds, which A4's
reproduction check requires. Because several thresholds above were set with smoke runs on
that pair in view, two further seed pairs are run as CONFIRMATION and are genuinely
held out from the threshold-setting. Per-pair criteria are reported separately; a criterion
that passes on the primary pair alone is reported as such and not as a result.

SCOPE: no claim registered or promoted, no queue entry, no edit to the harness, the P1
driver, the design note, the ladder or the supplement. Synthetic assay only.

PRE-RUN AMENDMENTS
------------------
All five were found in smoke runs and applied BEFORE the authoritative run. Two of them
(1 and 4) make a criterion EASIER to pass and are flagged as such; amendment 3 REVERSED an
expectation this module was written around, and amendment 5 corrects a claim in this
docstring that was simply false.

1. **The criterion grid was truncating the route, so A5 was measuring the grid.** The grid
   ended at C = 0.95, where the attribution route reached N_eff 4.42 and was still rising
   (its asymptote is n = 5). The measured maximum was therefore set by where the grid
   stopped, not by the route. Extended to 1.20. DIRECTION: makes A5 easier to pass. This is
   the same class of fix as P1's amendment 3 (READ_NOISE raised because the arm "had no
   resolvable range") -- an instrument that cannot reach the region the question is about
   measures the instrument.

2. **A6 summarised the two routes asymmetrically**, taking axis ENDPOINTS on the stored-tag
   route and the MAX over the grid on the attribution route. Since "does this policy
   eliminate the inflation?" must hold everywhere on the axis, both routes now use the max
   over their own axis. DIRECTION: makes A6 strictly harder to pass, on both routes.

3. **A8's premise was wrong, and the smoke run reversed it.** A8 originally predicted, from
   section 6, that the stored-tag route's cross-family confusion would be positive under
   misbinding. Measured at a fixed kappa = 1.0 it was 0.00000; swept to kappa = 9.0 it
   reached only 0.00068. The reason is structural: misbinding re-points an edge to the
   trace of highest rectified content similarity, and a descendant's SIBLINGS all derive
   from the same ancestor's content, so they dominate any cross-family candidate --
   and raising kappa raises within-family similarity too, because siblings inherit the
   shared context vector from their common ancestor. A8 is therefore restated as a
   two-branch MEASUREMENT rather than a prediction, with the cross-family re-point fraction
   reported as the mechanism. The misbinding arm now sweeps the whole kappa grid rather
   than sitting at 1.0.

4. **A9 conflated two readouts.** The single |delta N_eff| >= 0.050 clause failed on the
   attribution route (measured -0.025) while the SOURCE-ATTRIBUTION readout moved by 34%
   relative (0.0839 -> 0.0555) in the same cells. Reporting one number would have recorded
   "fluency is not live" when what is true is that it is live on readout 2 and not on
   readout 3 -- which is precisely the readout dissociation the branch exists to preserve
   (verification doc section 5, Goff & Roediger 1998 versus Sharman 2004). Split into A9a
   and A9b. DIRECTION: A9a's threshold is unchanged and still expected to fail on the
   cardinality readout; A9b is new.

5. **The claimed orthogonality of the similarity dial was false for descendants.** This
   docstring asserted that the shared context vector, drawn in dims 2..DIM-1, leaves every
   vote bit-identical. That holds for the two world-event SEEDS but not for their
   descendants: the `prediction` generator's forward model `_A = I + 0.12 * roll(I, 1)`
   couples dim 15 into dim 0, which IS the vote direction, and `retrieved_memory` scales by
   `norm(base)`, which kappa changes. Accuracy is therefore near-invariant, not exactly
   invariant. A7b was added as an explicit control on the realised accuracy range rather
   than leaving a false invariance claim standing.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import provenance_genealogy_harness as H  # noqa: E402


ROUTES = ("stored_tag", "attribution")

# --- episode parameters: IDENTICAL to the P1 driver, so the stored-tag arm here is the
# --- same architecture P1 measured and A4 is a real reproduction check.
SIGNAL = 1.0
WORLD_NOISE = 1.484
ETA = 0.40
READ_NOISE = 2.0

DECAY_KNOBS = (1e6, 20.0, 12.0, 9.5, 8.0, 6.0, 4.0, 2.5)
MISBIND_KNOB = 0.5
X_THRESHOLD = 0.010  # A8's branch boundary on cross-family confusion
RETRIEVAL_COUNTS = (0, 1, 2, 4, 8, 16)

# --- attribution-route constants. FIXED, declared, not fitted.
W_SIM = 0.60  # perceptual / content detail
W_CTX = 0.25  # contextual and semantic accompaniment
W_OPS = 0.15  # recorded cognitive operations
TAU_CTX = 3.0  # temporal-proximity length scale, on the harness's t in [0, 6]
BETA = 12.0  # criterion decisiveness

# Spans the realised score range (measured on a calibration split: mean 0.657, sd 0.045,
# support [0.501, 0.767] with no retrieval events) and runs PAST it at both ends, so that
# the grid is not truncating the route's reach -- see pre-run amendment 1.
CRITERION_GRID = (0.35, 0.45, 0.55, 0.60, 0.65, 0.70, 0.75, 0.85, 0.95, 1.05, 1.20)

# The candidate-source similarity dial of A7: the weight on a shared context vector drawn
# in the subspace ORTHOGONAL to both the vote direction _W (dim 0) and the retrieval cue
# _CUE (dim 1). Orthogonality is load-bearing -- it raises cross-family content similarity
# while leaving every vote, hence accuracy and p, bit-identical.
KAPPA_GRID = (0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.5)

P1_LANDED_INFLATION = 3.753  # REE_assembly 062d774289, section 1
P1_INSTRUMENT_FLOOR = 0.2215  # ibid., section 3


# --------------------------------------------------------------------------------------
# Aggregation -- reimplemented from the harness, and GATED against it (see docstring)
# --------------------------------------------------------------------------------------


def aggregate_n_eff(
    P: np.ndarray, absent_policy: str = "independent", unknown_below: float = 0.25
) -> float:
    """The harness's `effective_source_count` aggregation, over a pairwise matrix.

    Byte-for-byte the same semantics as `H.effective_source_count`'s second half, verified
    by `assert_aggregation_equivalence`. Split out here ONLY because the attribution route
    produces P from features rather than from ancestry paths.
    """
    if absent_policy not in H.ABSENT_POLICIES:
        raise ValueError("unknown absent_policy: %s" % absent_policy)
    m = P.shape[0]
    if m == 0:
        return 0.0
    P = P.copy()
    if absent_policy != "independent":
        known = P[np.triu_indices(m, 1)] if m > 1 else np.array([0.0])
        usable = known[known >= unknown_below]
        prior = float(usable.mean()) if usable.size else 0.0
        fill = 1.0 if absent_policy == "dependent" else prior
        for a in range(m):
            for b in range(m):
                if a != b and P[a, b] < unknown_below:
                    P[a, b] = fill
    dep = P.sum(axis=1) - 1.0
    return float(np.sum(1.0 / (1.0 + np.maximum(dep, 0.0))))


def stored_p_matrix(store: H.GenealogyStore, ids: Sequence[int]) -> np.ndarray:
    m = len(ids)
    P = np.zeros((m, m))
    for a in range(m):
        for b in range(m):
            P[a, b] = 1.0 if a == b else H.shared_ancestry_prob(store, ids[a], ids[b])
    return P


def assert_aggregation_equivalence(n_cases: int = 240, seed: int = 4242) -> Dict[str, object]:
    """HARD GATE. Aborts the run if the local aggregation has drifted from the harness's.

    Randomised stores, spanning intact / decayed / misbound / mixed structures, so the
    `absent_policy` fill is exercised in every branch rather than only where it is inert.
    """
    rng = np.random.default_rng(seed)
    worst = 0.0
    for case in range(n_cases):
        crng = np.random.default_rng([seed, case])
        Hh = 1 if crng.random() < 0.5 else -1
        store, truth = H.new_episode(crng, Hh, SIGNAL, WORLD_NOISE)
        n_desc = int(rng.integers(1, 6))
        kinds = list(H.DESCENDANT_KINDS)
        for k in range(n_desc):
            H.spawn_descendant(
                store, truth, 0, kinds[k % len(kinds)], crng,
                t=float(1 + k % 6), eta=ETA, alpha=float(rng.random()),
                signal=SIGNAL, noise=WORLD_NOISE,
            )
        if rng.random() < 0.5:
            H.add_world_event(store, truth, crng, SIGNAL, WORLD_NOISE, t=2.0)
        proc = ("decay", "interference", "misbinding")[int(rng.integers(0, 3))]
        knob = float(rng.choice([1e6, 12.0, 4.0])) if proc != "misbinding" else float(
            rng.choice([0.0, 0.1, 0.5])
        )
        H.degrade(store, proc, knob, 12, np.random.default_rng([seed, 77, case]))
        ids = list(range(store.n()))
        P = stored_p_matrix(store, ids)
        for policy in H.ABSENT_POLICIES:
            a = aggregate_n_eff(P, policy)
            b = H.effective_source_count(store, ids, policy)
            worst = max(worst, abs(a - b))
    if worst > 1e-12:
        raise AssertionError(
            "local aggregation has DRIFTED from the harness: worst |delta| = %.3e over %d "
            "cases. Every route comparison in this module is invalid until this is fixed."
            % (worst, n_cases)
        )
    return {"cases": n_cases, "worst_abs_delta": worst, "passed": True}


# --------------------------------------------------------------------------------------
# The attribution route
# --------------------------------------------------------------------------------------


def _unit(v: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(v)
    return v / n if n > 0 else v


def attribution_score(store: H.GenealogyStore, i: int, j: int) -> float:
    """Johnson 1993's three feature families over what a harness trace carries.

    Reads ONLY content, timestamps and recorded retrieval events. It does not read
    `edge_target`, `edge_w`, `explicit_family` or `assoc` -- so the stored ancestry edge set
    is held constant and never consulted, which is what makes A3 structural.
    """
    sim = max(0.0, float(np.dot(_unit(store.content[i]), _unit(store.content[j]))))
    ctx = math.exp(-abs(store.t[i] - store.t[j]) / TAU_CTX)
    ri, rj = store.retrieval_events[i], store.retrieval_events[j]
    ops = 0.5 * (ri / (1.0 + ri) + rj / (1.0 + rj))
    return W_SIM * sim + W_CTX * ctx + W_OPS * ops


def attribution_p_matrix(
    store: H.GenealogyStore, ids: Sequence[int], criterion: float
) -> np.ndarray:
    m = len(ids)
    P = np.zeros((m, m))
    for a in range(m):
        P[a, a] = 1.0
        for b in range(a + 1, m):
            p = H.sigmoid(BETA * (attribution_score(store, ids[a], ids[b]) - criterion))
            P[a, b] = P[b, a] = p
    return P


def route_p_matrix(
    store: H.GenealogyStore, ids: Sequence[int], route: str, criterion: float
) -> np.ndarray:
    if route == "stored_tag":
        return stored_p_matrix(store, ids)
    if route == "attribution":
        return attribution_p_matrix(store, ids, criterion)
    raise ValueError("unknown route: %s" % route)


def attribution_p_external(
    store: H.GenealogyStore, ids: Sequence[int], trace_id: int, criterion: float
) -> float:
    """The attribution route's analogue of `H.source_attribution`'s `p_external`.

    Reconstructed, not read: a trace is judged externally derived to the extent that no
    EARLIER trace in the store is judged to share its source. Candidates are restricted to
    traces preceding it in time, because a source must precede what it sources; a trace with
    no predecessor reads as external, matching the stored-tag route's treatment of a trace
    with no ancestry edge.
    """
    cands = [j for j in ids if j != trace_id and store.t[j] < store.t[trace_id]]
    if not cands:
        return 1.0
    best = max(
        H.sigmoid(BETA * (attribution_score(store, trace_id, j) - criterion)) for j in cands
    )
    return float(1.0 - best)


# --------------------------------------------------------------------------------------
# Episodes
# --------------------------------------------------------------------------------------


def build_episode(content_seed: int, ep: int, n_desc: int, alpha: float = 1.0):
    """IDENTICAL to the P1 driver's `build_episode` (design note 4.4). Reproduced rather
    than imported so that importing the P1 driver -- which runs a 2000-episode assay at
    import time only if invoked as main, but whose constants could drift -- is not a hidden
    dependency of this module. A4 is what checks the reproduction empirically."""
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


def build_two_family_episode(content_seed: int, ep: int, n_desc: int, kappa: float):
    """Two genuinely independent world events, each with descendants, sharing a context
    vector of weight `kappa` in the subspace orthogonal to the vote direction and the cue.

    `kappa` is the A7 candidate-source similarity dial. The shared vector lies in dims
    2..DIM-1 and the vote is `dot(content, _W)` with `_W` supported on dim 0 alone, so the
    two SEEDS' votes are bit-identical across the whole dial.

    That invariance does NOT extend to their descendants, and pre-run amendment 5 corrects
    an earlier claim here that it did: the `prediction` generator's forward model
    `_A = I + 0.12 * roll(I, 1, axis=0)` couples dim 15 into dim 0 -- the vote direction --
    and `retrieved_memory` rescales by `norm(base)`, which kappa changes. Accuracy is
    therefore NEAR-invariant, and A7b measures the residual rather than asserting it away.
    """
    crng = np.random.default_rng([content_seed, 31, ep])
    Hh = 1 if crng.random() < 0.5 else -1
    u = np.zeros(H.DIM)
    u[2:] = crng.normal(size=H.DIM - 2)
    u = u / max(np.linalg.norm(u), 1e-12)

    store, truth = H.new_episode(crng, Hh, SIGNAL, WORLD_NOISE)
    store.content[0] = store.content[0] + kappa * u
    truth.seed_content[0] = store.content[0].copy()
    e1 = H.add_world_event(store, truth, crng, SIGNAL, WORLD_NOISE, t=0.0)
    store.content[e1] = store.content[e1] + kappa * u
    truth.seed_content[e1] = store.content[e1].copy()

    kinds = ["replay", "prediction", "retrieved_memory", "ambiguous_perception"]
    for anc in (0, e1):
        for k in range(n_desc):
            H.spawn_descendant(
                store, truth, anc, kinds[k % len(kinds)], crng,
                t=float(1 + k % 6), eta=ETA, alpha=1.0, signal=SIGNAL, noise=WORLD_NOISE,
            )
    return store, truth


def estimate_p(content_seed: int, episodes: int, n_desc: int) -> float:
    """Single-trace reliability over the same population the belief combines. Mirrors the
    P1 driver's `estimate_p(population='all')`."""
    rng = np.random.default_rng([content_seed, 555, 1])
    ok = tot = 0
    for ep in range(episodes):
        store, truth = build_episode(content_seed, 10_000 + ep, n_desc)
        for i in range(store.n()):
            ok += int(H.read_vote(store, i, rng, READ_NOISE, 1) == truth.H)
            tot += 1
    return ok / max(tot, 1)


def score_distribution(args, content_seed: int, episodes: int) -> Dict[str, float]:
    """The realised pairwise score distribution on a calibration split.

    Reported so that a criterion value is interpretable as a POSITION IN THE JUDGEMENT
    DISTRIBUTION rather than as a bare number -- which is what keeps A5's magnitude honest
    (see the A5 note on near-definitional passes)."""
    vals = []
    for ep in range(episodes):
        store, _ = build_episode(content_seed, 20_000 + ep, args.n_desc)
        ids = list(range(store.n()))
        for a in range(len(ids)):
            for b in range(a + 1, len(ids)):
                vals.append(attribution_score(store, ids[a], ids[b]))
    v = np.asarray(vals)
    return {"mean": float(v.mean()), "sd": float(v.std()),
            "min": float(v.min()), "max": float(v.max()), "n_pairs": int(v.size)}


def frac_pairs_above(args, content_seed: int, episodes: int, criterion: float) -> float:
    """Fraction of pairwise judgements whose score exceeds the criterion -- i.e. the share
    of the store the reader is currently willing to call one source."""
    above = tot = 0
    for ep in range(episodes):
        store, _ = build_episode(content_seed, ep, args.n_desc)
        ids = list(range(store.n()))
        for a in range(len(ids)):
            for b in range(a + 1, len(ids)):
                above += int(attribution_score(store, ids[a], ids[b]) > criterion)
                tot += 1
    return above / max(tot, 1)


def cross_family_repoint_fraction(store: H.GenealogyStore, truth: H.GroundTruth) -> Tuple[int, int]:
    """(re-points that landed CROSS-family, total re-points). The mechanism behind A8.

    Post-hoc from state, so the harness needs no instrumentation: a descendant whose current
    ancestry edge points somewhere other than its true ancestor has been re-pointed, and the
    families of the two tell you whether it crossed.
    """
    cross = tot = 0
    for d in truth.descendants():
        tgt = store.edge_target[d]
        if tgt < 0 or tgt == truth.true_ancestor[d]:
            continue
        tot += 1
        cross += int(truth.true_family[tgt] != truth.true_family[d])
    return cross, tot


def cross_family_confusion(
    store: H.GenealogyStore, truth: H.GroundTruth, ids: Sequence[int], route: str, criterion: float
) -> float:
    """SCORER. Mean judged shared-source probability between pairs of GENUINELY DIFFERENT
    true families. Ground truth enters only here, to select which pairs to average over --
    never into the judgement itself."""
    P = route_p_matrix(store, ids, route, criterion)
    vals = []
    for a in range(len(ids)):
        for b in range(a + 1, len(ids)):
            if truth.true_family[ids[a]] != truth.true_family[ids[b]]:
                vals.append(P[a, b])
    return float(np.mean(vals)) if vals else float("nan")


# --------------------------------------------------------------------------------------
# Measurement
# --------------------------------------------------------------------------------------


@dataclass
class Cell:
    n_eff: float = 0.0
    n_eff_true: float = 0.0
    confidence: float = 0.0
    accuracy: float = 0.0
    signed_error: float = 0.0
    p_external: float = 0.0


def measure(
    args,
    p_est: float,
    route: str,
    criterion: float,
    absent_policy: str = "independent",
    process: Optional[str] = None,
    knob: Optional[float] = None,
    replay_n: int = 0,
    content_seed: Optional[int] = None,
) -> Cell:
    """One cell: `episodes` episodes at one (route, criterion, policy, storage) point."""
    cs = args.content_seed if content_seed is None else content_seed
    ne, net, conf, corr, pext = [], [], [], [], []
    vrng = np.random.default_rng([cs, 909])
    for ep in range(args.episodes):
        store, truth = build_episode(cs, ep, args.n_desc)
        if process is not None and knob is not None:
            drng = np.random.default_rng([args.dynamics_seed, 11, ep])
            H.degrade(store, process, knob, args.steps, drng, dyn_noise=args.dyn_noise)
        if replay_n:
            H.replay(store, truth, 0, replay_n, np.random.default_rng([cs, 3, ep]),
                     mode="in_place")
        ids = list(range(store.n()))
        votes = [H.read_vote(store, i, vrng, READ_NOISE, 1) for i in ids]
        P = route_p_matrix(store, ids, route, criterion)
        n_eff = aggregate_n_eff(P, absent_policy)
        c = H.confidence(votes, p_est, n_eff)
        b = 1 if sum(votes) >= 0 else -1
        d = truth.descendants()
        if route == "stored_tag":
            pe = float(np.mean([H.source_attribution(store, i)["p_external"] for i in d]))
        else:
            pe = float(np.mean([attribution_p_external(store, ids, i, criterion) for i in d]))
        ne.append(n_eff)
        net.append(H.true_effective_source_count(truth, ids))
        conf.append(c)
        corr.append(int(b == truth.H))
        pext.append(pe)
    cell = Cell()
    cell.n_eff, cell.n_eff_true = float(np.mean(ne)), float(np.mean(net))
    cell.confidence, cell.accuracy = float(np.mean(conf)), float(np.mean(corr))
    cell.signed_error = cell.confidence - cell.accuracy
    cell.p_external = float(np.mean(pext))
    return cell


def fit_c_star(args, target_n_eff: float) -> float:
    """Fit the reference criterion on a CALIBRATION SPLIT (a different content seed from
    every reported number), by bisection, so that the attribution route's intact N_eff
    matches the stored-tag route's undegraded N_eff. See the docstring on why this is what
    makes A5 a fair test.

    N_eff is monotonically INCREASING in the criterion: a stricter criterion lowers every
    p_same, lowers each dependency sum, and raises the count.
    """
    cs = args.cal_seed

    def n_eff_at(c: float) -> float:
        vals = []
        for ep in range(args.cal_episodes_criterion):
            store, _ = build_episode(cs, 20_000 + ep, args.n_desc)
            ids = list(range(store.n()))
            vals.append(aggregate_n_eff(attribution_p_matrix(store, ids, c), "independent"))
        return float(np.mean(vals))

    lo, hi = 0.0, 1.5
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if n_eff_at(mid) < target_n_eff:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def _rank(x: np.ndarray) -> np.ndarray:
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
# Arms
# --------------------------------------------------------------------------------------


def arm_criterion_sweep(args, p_est: float, c_star: float) -> Dict[str, object]:
    """D1 -- the criterion axis at FIXED storage, both routes, all three absent policies.
    Feeds A1, A2, A5 and the attribution half of A6."""
    out: Dict[str, object] = {"c_star": c_star, "rows": []}
    for route in ROUTES:
        for policy in H.ABSENT_POLICIES:
            for c in (c_star,) + CRITERION_GRID:
                cell = measure(args, p_est, route, c, policy)
                out["rows"].append(
                    {
                        "route": route, "absent_policy": policy, "criterion": c,
                        "is_c_star": bool(c == c_star),
                        "n_eff": cell.n_eff, "n_eff_true": cell.n_eff_true,
                        "confidence": cell.confidence, "accuracy": cell.accuracy,
                        "signed_error": cell.signed_error, "p_external": cell.p_external,
                    }
                )
    return out


def arm_storage_sweep(args, p_est: float, c_star: float) -> Dict[str, object]:
    """D2 -- the decay (elapsed-interval) axis at FIXED criterion, both routes, all three
    absent policies. Feeds A3, A4 and the stored-tag half of A6."""
    out: Dict[str, object] = {"rows": []}
    for route in ROUTES:
        for policy in H.ABSENT_POLICIES:
            for knob in DECAY_KNOBS:
                cell = measure(args, p_est, route, c_star, policy, process="decay", knob=knob)
                out["rows"].append(
                    {
                        "route": route, "absent_policy": policy, "knob": knob,
                        "n_eff": cell.n_eff, "confidence": cell.confidence,
                        "accuracy": cell.accuracy, "signed_error": cell.signed_error,
                        "p_external": cell.p_external,
                    }
                )
    return out


def arm_similarity(args, p_est: float, c_star: float) -> Dict[str, object]:
    """D3 -- candidate-source similarity, on two-family episodes with storage PRISTINE.
    Feeds A7 and the zero-degradation half of A8."""
    rows = []
    for route in ROUTES:
        for kappa in KAPPA_GRID:
            xs, nes, accs = [], [], []
            vrng = np.random.default_rng([args.content_seed, 4242])
            for ep in range(args.sim_episodes):
                store, truth = build_two_family_episode(
                    args.content_seed, ep, args.n_desc, kappa
                )
                ids = list(range(store.n()))
                xs.append(cross_family_confusion(store, truth, ids, route, c_star))
                nes.append(aggregate_n_eff(route_p_matrix(store, ids, route, c_star)))
                votes = [H.read_vote(store, i, vrng, READ_NOISE, 1) for i in ids]
                accs.append(int((1 if sum(votes) >= 0 else -1) == truth.H))
            rows.append(
                {
                    "route": route, "kappa": kappa,
                    "cross_family_confusion": float(np.mean(xs)),
                    "n_eff": float(np.mean(nes)),
                    "accuracy": float(np.mean(accs)),
                }
            )
    return {"rows": rows}


def arm_misbinding_similarity(args, p_est: float, c_star: float) -> Dict[str, object]:
    """D4 -- the storage-time half of A8: the stored-tag route's cross-family confusion
    under the misbinding process, which is the only route by which similarity can reach its
    edge set at all."""
    rows = []
    for route in ROUTES:
        for label, proc, knob in (("none", None, None), ("misbinding", "misbinding", MISBIND_KNOB)):
            for kappa in KAPPA_GRID:
                xs, cross, tot = [], 0, 0
                for ep in range(args.sim_episodes):
                    store, truth = build_two_family_episode(
                        args.content_seed, ep, args.n_desc, kappa
                    )
                    if proc is not None:
                        H.degrade(store, proc, knob, args.steps,
                                  np.random.default_rng([args.dynamics_seed, 13, ep]),
                                  dyn_noise=args.dyn_noise)
                    ids = list(range(store.n()))
                    xs.append(cross_family_confusion(store, truth, ids, route, c_star))
                    c, t = cross_family_repoint_fraction(store, truth)
                    cross += c
                    tot += t
                rows.append({
                    "route": route, "process": label, "kappa": kappa,
                    "cross_family_confusion": float(np.mean(xs)),
                    "repoints": tot, "cross_family_repoints": cross,
                    "cross_family_repoint_frac": (cross / tot) if tot else float("nan"),
                })
    return {"rows": rows}


def arm_fluency(args, p_est: float, c_star: float) -> Dict[str, object]:
    """D5 -- P1-R7's in-place retrieval axis, crossed with route. Feeds A9.

    `replay(mode='in_place')` moves the recorded retrieval-event count while creating no
    descendants, so cardinality and storage are both fixed and only the operations feature
    moves."""
    rows = []
    for route in ROUTES:
        for n in RETRIEVAL_COUNTS:
            cell = measure(args, p_est, route, c_star, "independent", replay_n=n)
            rows.append(
                {
                    "route": route, "retrieval_events": n, "n_eff": cell.n_eff,
                    "confidence": cell.confidence, "p_external": cell.p_external,
                }
            )
    return {"rows": rows}


def assert_content_fixed(args, c_star: float) -> Dict[str, object]:
    """C1, extended across ROUTES rather than across ancestry conditions: content hashes
    and per-episode votes must be bit-identical between the two routes, so that any
    confidence difference is attributable to N_eff alone."""
    hashes = {}
    votes_by_route = {}
    for route in ROUTES:
        vrng = np.random.default_rng([args.content_seed, 909])
        hs, vs = [], []
        for ep in range(min(args.episodes, 200)):
            store, _ = build_episode(args.content_seed, ep, args.n_desc)
            ids = list(range(store.n()))
            _ = route_p_matrix(store, ids, route, c_star)  # must not mutate content
            hs.append(store.content_hash())
            vs.append([H.read_vote(store, i, vrng, READ_NOISE, 1) for i in ids])
        hashes[route] = hs
        votes_by_route[route] = vs
    same_content = hashes[ROUTES[0]] == hashes[ROUTES[1]]
    same_votes = votes_by_route[ROUTES[0]] == votes_by_route[ROUTES[1]]
    if not (same_content and same_votes):
        raise AssertionError(
            "C1 FAILED: routes do not see identical content/votes "
            "(content_identical=%s votes_identical=%s)" % (same_content, same_votes)
        )
    return {"content_identical": same_content, "votes_identical": same_votes, "passed": True}


# --------------------------------------------------------------------------------------
# Preregistered criteria
# --------------------------------------------------------------------------------------


def _rows(block, **kw):
    out = []
    for r in block["rows"]:
        if all(r.get(k) == v for k, v in kw.items()):
            out.append(r)
    return out


def evaluate(res: Dict[str, object]) -> Dict[str, object]:
    crit: Dict[str, object] = {}
    cs = res["criterion_sweep"]
    ss = res["storage_sweep"]
    c_star = cs["c_star"]

    def grid_rows(route, policy):
        return [r for r in _rows(cs, route=route, absent_policy=policy) if not r["is_c_star"]]

    def star_row(route, policy):
        return [r for r in _rows(cs, route=route, absent_policy=policy) if r["is_c_star"]][0]

    st = [r["n_eff"] for r in grid_rows("stored_tag", "independent")]
    at = [r["n_eff"] for r in grid_rows("attribution", "independent")]
    crit["A1_stored_tag_criterion_invariant"] = {
        "kind": "STRUCTURAL", "range": max(st) - min(st), "threshold": 1e-12,
        "passed": bool(max(st) - min(st) <= 1e-12),
    }
    crit["A2_attribution_criterion_movable"] = {
        "kind": "EMPIRICAL", "range": max(at) - min(at), "threshold": 1.000,
        "instrument_floor": P1_INSTRUMENT_FLOOR,
        "passed": bool(max(at) - min(at) >= 1.000),
    }

    st_s = [r["n_eff"] for r in _rows(ss, route="stored_tag", absent_policy="independent")]
    at_s = [r["n_eff"] for r in _rows(ss, route="attribution", absent_policy="independent")]
    crit["A3_attribution_storage_invariant"] = {
        "kind": "STRUCTURAL", "range": max(at_s) - min(at_s), "threshold": 1e-12,
        "passed": bool(max(at_s) - min(at_s) <= 1e-12),
    }
    crit["A4_stored_tag_reproduces_P1"] = {
        "kind": "REPRODUCTION", "range": max(st_s) - min(st_s), "threshold": 3.000,
        "p1_landed_inflation": P1_LANDED_INFLATION,
        "n_eff_intact": st_s[0], "n_eff_corrupted": st_s[-1],
        "inflation": st_s[-1] - st_s[0],
        "passed": bool(max(st_s) - min(st_s) >= 3.000),
    }

    star = star_row("attribution", "independent")["n_eff"]
    reach = max(at) - star
    argmax_row = max(grid_rows("attribution", "independent"), key=lambda r: r["n_eff"])
    crit["A5_attribution_reaches_P1_magnitude"] = {
        "kind": "EMPIRICAL", "c_star": c_star, "n_eff_at_c_star": star,
        "n_eff_max_on_grid": max(at), "inflation_reached": reach,
        "criterion_at_max": argmax_row["criterion"],
        "frac_pairs_above_c_star": res["criterion_position"]["frac_above_c_star"],
        "frac_pairs_above_criterion_at_max": res["criterion_position"]["frac_above"].get(
            str(argmax_row["criterion"])
        ),
        "threshold": P1_LANDED_INFLATION, "passed": bool(reach >= P1_LANDED_INFLATION),
        "note": "a pass here is NEAR-DEFINITIONAL given the shared aggregation -- see the "
                "module docstring's A5 entry",
        "meaning_if_pass": "BOTH routes inflate -- architecture-independent",
        "meaning_if_fail": "only the stored-tag route -- P1 is about REE's implementation",
    }

    # A6 -- max over each route's OWN axis, symmetrically (pre-run amendment 2).
    pol: Dict[str, object] = {}
    for route in ROUTES:
        per = {}
        for policy in H.ABSENT_POLICIES:
            if route == "stored_tag":
                rr = _rows(ss, route=route, absent_policy=policy)
                intact = rr[0]["n_eff"]
                axis = [r["n_eff"] for r in rr]
                endpoint = rr[-1]["n_eff"]
            else:
                intact = star_row(route, policy)["n_eff"]
                g = grid_rows(route, policy)
                axis = [r["n_eff"] for r in g]
                endpoint = g[-1]["n_eff"]
            per[policy] = {
                "intact": intact, "axis_max": max(axis), "axis_endpoint": endpoint,
                "inflation": max(axis) - intact,
                "inflation_at_endpoint": endpoint - intact,
            }
        dep_ok = abs(per["dependent"]["inflation"]) <= 0.30
        soft_ok = abs(per["soft"]["inflation"] - per["independent"]["inflation"]) <= 0.30
        pol[route] = {"per_policy": per, "dependent_eliminates": dep_ok,
                      "soft_degenerates_to_independent": soft_ok,
                      "passed": bool(dep_ok and soft_ok)}
    crit["A6_absent_policy_crossing"] = {
        "kind": "EMPIRICAL", "summarised_over": "max of each route's own axis", "by_route": pol,
        "passed": bool(all(pol[r]["passed"] for r in ROUTES)),
    }

    sim = res["similarity"]
    at_sim = _rows(sim, route="attribution")
    st_sim = _rows(sim, route="stored_tag")
    rho = spearman([r["kappa"] for r in at_sim], [r["cross_family_confusion"] for r in at_sim])
    crit["A7_attribution_read_time_similarity"] = {
        "kind": "EMPIRICAL", "rho": rho, "threshold": 0.90,
        "x_min": min(r["cross_family_confusion"] for r in at_sim),
        "x_max": max(r["cross_family_confusion"] for r in at_sim),
        "stored_tag_x_max": max(r["cross_family_confusion"] for r in st_sim),
        "passed": bool(np.isfinite(rho) and rho >= 0.90),
    }
    acc = [r["accuracy"] for r in at_sim]
    crit["A7b_similarity_dial_vote_control"] = {
        "kind": "CONTROL", "accuracy_range": max(acc) - min(acc), "threshold": 0.020,
        "accuracy_min": min(acc), "accuracy_max": max(acc),
        "passed": bool(max(acc) - min(acc) <= 0.020),
    }

    # A8 -- two-branch measurement (pre-run amendment 3).
    mb = res["misbinding_similarity"]
    st_none = max(r["cross_family_confusion"] for r in _rows(mb, route="stored_tag", process="none"))
    st_mis_rows = _rows(mb, route="stored_tag", process="misbinding")
    st_mis = max(r["cross_family_confusion"] for r in st_mis_rows)
    at_mis = max(r["cross_family_confusion"] for r in _rows(mb, route="attribution", process="none"))
    rp_tot = sum(r["repoints"] for r in st_mis_rows)
    rp_cross = sum(r["cross_family_repoints"] for r in st_mis_rows)
    if st_mis > X_THRESHOLD:
        branch = "STORAGE_TIME_REALISED"
    elif at_mis > X_THRESHOLD:
        branch = "ATTRIBUTION_ONLY"
    else:
        branch = "NEITHER_ROUTE_CONFUSES"
    crit["A8_where_similarity_acts"] = {
        "kind": "MEASUREMENT", "branch": branch, "threshold": X_THRESHOLD,
        "stored_tag_x_max_no_degradation": st_none,
        "stored_tag_x_max_misbinding": st_mis,
        "attribution_x_max_no_degradation": at_mis,
        "misbinding_repoints": rp_tot, "misbinding_cross_family_repoints": rp_cross,
        "cross_family_repoint_frac": (rp_cross / rp_tot) if rp_tot else float("nan"),
        "passed": True,  # a measurement, not a gate; the branch IS the result
    }

    # A9 -- split by readout (pre-run amendment 4).
    fl = res["fluency"]
    d = {}
    for route in ROUTES:
        rr = _rows(fl, route=route)
        p0, p16 = rr[0]["p_external"], rr[-1]["p_external"]
        d[route] = {
            "n_eff_0": rr[0]["n_eff"], "n_eff_16": rr[-1]["n_eff"],
            "delta_n_eff": rr[-1]["n_eff"] - rr[0]["n_eff"],
            "p_external_0": p0, "p_external_16": p16,
            "delta_p_external": p16 - p0,
            "rel_delta_p_external": (p16 - p0) / p0 if p0 else float("nan"),
            "confidence_delta": rr[-1]["confidence"] - rr[0]["confidence"],
        }
    a9a_st = abs(d["stored_tag"]["delta_n_eff"]) <= 1e-12
    a9a_at = abs(d["attribution"]["delta_n_eff"]) >= 0.050
    a9b_st = abs(d["stored_tag"]["rel_delta_p_external"]) <= 1e-12
    a9b_at = abs(d["attribution"]["rel_delta_p_external"]) >= 0.100
    crit["A9a_fluency_readout3_cardinality"] = {
        "kind": "MIXED", "stored_tag": d["stored_tag"]["delta_n_eff"],
        "attribution": d["attribution"]["delta_n_eff"],
        "threshold_stored_tag": 1e-12, "threshold_attribution": 0.050,
        "structural_passed": bool(a9a_st), "empirical_passed": bool(a9a_at),
        "passed": bool(a9a_st and a9a_at),
    }
    crit["A9b_fluency_readout2_source_attribution"] = {
        "kind": "MIXED",
        "stored_tag_rel": d["stored_tag"]["rel_delta_p_external"],
        "attribution_rel": d["attribution"]["rel_delta_p_external"],
        "attribution_abs": d["attribution"]["delta_p_external"],
        "threshold_stored_tag": 1e-12, "threshold_attribution": 0.100,
        "predeclared_direction": "negative",
        "structural_passed": bool(a9b_st), "empirical_passed": bool(a9b_at),
        "passed": bool(a9b_st and a9b_at),
    }
    crit["_fluency_detail"] = d

    # The discriminator of verification-doc section 6, read off A1-A4.
    crit["_discriminator_verdict"] = {
        "stored_tag_moves_with_storage": crit["A4_stored_tag_reproduces_P1"]["passed"],
        "stored_tag_unchanged_by_criterion": crit["A1_stored_tag_criterion_invariant"]["passed"],
        "attribution_moves_with_criterion": crit["A2_attribution_criterion_movable"]["passed"],
        "attribution_unchanged_by_storage": crit["A3_attribution_storage_invariant"]["passed"],
        "section6_table_realised": bool(
            crit["A4_stored_tag_reproduces_P1"]["passed"]
            and crit["A1_stored_tag_criterion_invariant"]["passed"]
            and crit["A2_attribution_criterion_movable"]["passed"]
            and crit["A3_attribution_storage_invariant"]["passed"]
        ),
    }

    gates = [k for k, v in crit.items() if not k.startswith("_")]
    empirical = [k for k in gates if crit[k].get("kind") in ("EMPIRICAL", "REPRODUCTION",
                                                            "MIXED", "CONTROL")]
    structural = ["A1_stored_tag_criterion_invariant", "A3_attribution_storage_invariant"]
    crit["_summary"] = {
        "all_passed": bool(all(crit[k]["passed"] for k in gates)),
        "empirical_passed": bool(all(crit[k]["passed"] for k in empirical)),
        "structural_passed": bool(all(crit[k]["passed"] for k in structural)),
        "failed": [k for k in gates if not crit[k]["passed"]],
    }
    return crit


def run_one_pair(args, content_seed: int, dynamics_seed: int) -> Dict[str, object]:
    """One (content, dynamics) seed pair, end to end."""
    import copy

    a = copy.copy(args)
    a.content_seed = content_seed
    a.dynamics_seed = dynamics_seed

    res: Dict[str, object] = {"content_seed": content_seed, "dynamics_seed": dynamics_seed}
    p_est = estimate_p(content_seed, a.cal_episodes, a.n_desc)
    res["p_est"] = p_est

    # The stored-tag route's UNDEGRADED N_eff, measured on the CALIBRATION split -- the
    # target C_STAR is fitted to. Never measured on the reported seed.
    _tgt_vals = []
    for ep in range(a.cal_episodes_criterion):
        _store, _ = build_episode(a.cal_seed, 20_000 + ep, a.n_desc)
        _tgt_vals.append(
            H.effective_source_count(_store, list(range(_store.n())), "independent")
        )
    tgt = float(np.mean(_tgt_vals))
    c_star = fit_c_star(a, tgt)
    res["c_star_fit"] = {"target_stored_tag_intact_n_eff": tgt, "c_star": c_star,
                         "cal_seed": a.cal_seed}

    res["criterion_position"] = {
        "score_distribution_on_cal_split": score_distribution(a, a.cal_seed,
                                                             a.cal_episodes_criterion),
        "frac_above_c_star": frac_pairs_above(a, content_seed, min(a.episodes, 400), c_star),
        "frac_above": {
            str(c): frac_pairs_above(a, content_seed, min(a.episodes, 400), c)
            for c in CRITERION_GRID
        },
    }

    res["content_fixed"] = assert_content_fixed(a, c_star)
    res["criterion_sweep"] = arm_criterion_sweep(a, p_est, c_star)
    res["storage_sweep"] = arm_storage_sweep(a, p_est, c_star)
    res["similarity"] = arm_similarity(a, p_est, c_star)
    res["misbinding_similarity"] = arm_misbinding_similarity(a, p_est, c_star)
    res["fluency"] = arm_fluency(a, p_est, c_star)
    return res


def main() -> int:
    ap = argparse.ArgumentParser(description="Provenance P1-R5 -- retrieval-attribution arm")
    ap.add_argument("--content-seed", type=int, default=17)
    ap.add_argument("--dynamics-seed", type=int, default=23)
    ap.add_argument("--cal-seed", type=int, default=101)
    ap.add_argument(
        "--confirm-seeds", type=str, default="41:53,67:71",
        help="held-out confirmation pairs as content:dynamics, comma separated; '' to skip",
    )
    ap.add_argument("--episodes", type=int, default=2000)
    ap.add_argument("--sim-episodes", type=int, default=1000)
    ap.add_argument("--cal-episodes", type=int, default=4000)
    ap.add_argument("--cal-episodes-criterion", type=int, default=600)
    ap.add_argument("--n-desc", type=int, default=4)
    ap.add_argument("--steps", type=int, default=12)
    ap.add_argument("--dyn-noise", type=float, default=0.35)
    ap.add_argument("--out-json", type=Path, default=None)
    args = ap.parse_args()

    pairs = [(args.content_seed, args.dynamics_seed, "primary")]
    if args.confirm_seeds.strip():
        for tok in args.confirm_seeds.split(","):
            c, d = tok.split(":")
            pairs.append((int(c), int(d), "confirmation"))

    gate = assert_aggregation_equivalence()

    runs = []
    for cseed, dseed, role in pairs:
        res = run_one_pair(args, cseed, dseed)
        runs.append({
            "role": role, "content_seed": cseed, "dynamics_seed": dseed,
            "results": res, "criteria": evaluate(res),
        })

    primary = runs[0]
    gates = [k for k in primary["criteria"] if not k.startswith("_")]
    across = {
        k: {
            "primary": primary["criteria"][k]["passed"],
            "confirmation": [r["criteria"][k]["passed"] for r in runs[1:]],
            "holds_on_all_pairs": bool(all(r["criteria"][k]["passed"] for r in runs)),
        }
        for k in gates
    }

    payload = {
        "assay": "provenance_p1r5_retrieval_attribution_arm",
        "status": "synthetic_arm_run_only",
        "compares_against": "provenance_p1_false_independence_assay (REE_assembly 062d774289)",
        "routes": list(ROUTES),
        "aggregation_equivalence": gate,
        "constants": {"W_SIM": W_SIM, "W_CTX": W_CTX, "W_OPS": W_OPS, "TAU_CTX": TAU_CTX,
                      "BETA": BETA, "CRITERION_GRID": list(CRITERION_GRID),
                      "KAPPA_GRID": list(KAPPA_GRID), "DECAY_KNOBS": list(DECAY_KNOBS),
                      "MISBIND_KNOB": MISBIND_KNOB, "X_THRESHOLD": X_THRESHOLD},
        "params": {k: (str(v) if isinstance(v, Path) else v) for k, v in vars(args).items()},
        "runs": runs,
        "criteria_across_seed_pairs": across,
        "discriminator_verdict": primary["criteria"]["_discriminator_verdict"],
        "summary": primary["criteria"]["_summary"],
    }
    print(json.dumps(payload, indent=2, sort_keys=True, default=float))
    if args.out_json:
        args.out_json.parent.mkdir(parents=True, exist_ok=True)
        args.out_json.write_text(
            json.dumps(payload, indent=2, sort_keys=True, default=float) + "\n", encoding="utf-8"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
