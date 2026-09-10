#!/usr/bin/env python3
"""Provenance genealogy harness -- the shared state layer for assays P1 and P3.

Implements the eight-operation contract of
`evidence/planning/provenance_harness_generated_ancestry_design.md` section 6, on top of
the genealogy representation (5.1) and degradation processes (5.2) whose endogeneity was
gated by probe P0 (`provenance_genealogy_probe_p0.py`, REE_assembly b81f9764bc).

P0 stays frozen as the record of that gate; this module is the production state layer and
is structurally derived from it rather than importing it, so a change here cannot
retroactively alter the landed gate result.

This is a synthetic measurement harness, not a REE creature experiment and not claim
evidence until an authoritative run is reviewed and banked separately.


WHAT THE ENDOGENEITY CRITERION FORCES, STRUCTURALLY (design note section 3)
--------------------------------------------------------------------------

  * `GroundTruth` holds true ancestry, true family, the per-descendant `alpha` values and
    `H`. It is passed ONLY to scorer operations (`calibration`, `classify_regime`,
    `true_effective_source_count`, `retrieval_fidelity`'s target).
  * `GenealogyStore` holds content, timestamps, the current ancestry edge set, the
    association edge set and explicit family assignments -- and nothing else. Every
    inference-path operation takes only the store.
  * `degrade()` takes no ancestry-indexed argument. Its signature cannot express one.
  * No descendant generator reads `H` or the world, with the single parameterised
    exception of `ambiguous_perception`'s world term (design note 4.1), which is declared
    in `GroundTruth.alpha` and enters the scorer's derived true source count (4.3).


TWO EDGE TYPES, AND WHY CONFLATING THEM WOULD BREAK P1-R2
----------------------------------------------------------

The store carries **ancestry** edges (`descendant -> ancestor`, "was derived from") and
**association** edges (`a <-> b`, "was linked to") as SEPARATE structures. Only ancestry
feeds the effective-source count.

This is load-bearing rather than tidy. P1-R2 (design note 7.1, from E43) links two
descendants of genuinely DIFFERENT world events and requires association strength to rise
while the effective independent-source count stays at 2. An implementation with one edge
set cannot pass that control: linking would raise the pairwise dependency term and drive
the count DOWN, which is precisely the "collapses distinct sources" failure the control
exists to detect. Keeping the two apart is what makes the control's correct outcome
reachable at all -- and an architecture that merged them would fail P1-R2 for a structural
reason, which is worth reporting as such rather than as an empirical result.


WHAT `N_eff` MEANS HERE, AND THE `absent_policy` KNOB (P2 as a sub-measurement)
-------------------------------------------------------------------------------

`effective_source_count` reads the ARCHITECTURE's own ancestry edges, never ground truth:

    p_share(i, j) = product of binding strengths from i and j up to their lowest common
                    ancestor, 0 if they have none
    dep_i         = sum over j != i of p_share(i, j)
    N_eff         = sum over i of 1 / (1 + dep_i)

which is assay 005's soft-provenance form (`soft_posterior`) read as a count. It gives
N_eff = 1 when a seed and its k descendants are bound at full strength, and N_eff = k + 1
when the bindings are gone.

That last equality is the point of `absent_policy`. `ABSENT` (ancestry unknown) and
`FALSE_SPLIT` (a positive, confident, wrong independence claim) produce the SAME count
under the default policy, because the default consumes unknown ancestry AS independence.
Design note 5.3 says whether that happens is a property of the readout rule and is
measurable in the same run -- which is P2. The knob makes it measurable instead of
assumed: `independent` (unknown -> separate sources), `dependent` (unknown -> assume shared
ancestry), `soft` (unknown -> the prior rate of shared ancestry in the store).


P1-R5 -- PREDECLARED ARCHITECTURE ROUTE (companion artifact section 7)
----------------------------------------------------------------------

P1-R5 requires the build to declare which route it implements BEFORE running, because the
design implements one without recording that a choice was made. Declared here:

  **This harness implements the STORED-TAG route.** Source structure lives in persistent
  ancestry edges that the dynamics degrade; `source_attribution` READS that stored
  structure at retrieval time. It does NOT reconstruct source structure at retrieval from
  a shiftable criterion over content similarity. A read-time-attribution variant is a
  different architecture, not a parameter of this one, and any result here is a result
  about the stored-tag route only.
"""

from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np


REGIMES = ("VERIDICAL", "SOFT", "ABSENT", "FALSE_SPLIT")
DESCENDANT_KINDS = ("replay", "prediction", "retrieved_memory", "ambiguous_perception")
PROCESSES = ("decay", "interference", "misbinding")
ABSENT_POLICIES = ("independent", "dependent", "soft")

DIM = 16
# A fixed evidence-readout direction. Global and constant so that a vote means the same
# thing in every episode and every arm; it is not drawn per run.
_W = np.zeros(DIM)
_W[0] = 1.0

# A fixed near-identity forward model for the `prediction` generator.
_A = np.eye(DIM) + 0.12 * np.roll(np.eye(DIM), 1, axis=0)
# A fixed retrieval cue for the `retrieved_memory` generator.
_CUE = np.zeros(DIM)
_CUE[1] = 1.0


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-max(-500.0, min(500.0, x))))


def logit(p: float) -> float:
    p = min(max(p, 1e-9), 1.0 - 1e-9)
    return math.log(p / (1.0 - p))


def _unit(v: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(v)
    return v / n if n > 0 else v


def _rel_noise(rng: np.random.Generator, scale: float, ref: np.ndarray) -> np.ndarray:
    """Noise whose norm is `scale` times the reference vector's norm.

    Expressed relative to the reference rather than per-component, so that a generator's
    `eta` means the same thing regardless of DIM and regardless of how large the world
    noise made the seed trace. Without this the two noise scales interact and the
    ancestor-descendant similarity -- which sets the initial binding strength below --
    drifts with unrelated parameters.
    """
    nz = rng.normal(size=DIM)
    nz = nz / max(np.linalg.norm(nz), 1e-12)
    return scale * float(np.linalg.norm(ref)) * nz


def initial_binding(descendant: np.ndarray, ancestor: np.ndarray) -> float:
    """Binding strength recorded when a descendant is spawned, from CONTENT ALONE.

    NOT 1.0. How strongly the architecture binds a descendant to its ancestor is how well
    the ancestor's stored content explains the descendant's -- rectified cosine similarity.
    This is inference-path legal (it reads two stored traces and nothing else) and it is
    what gives the effective-source-count readout DYNAMIC RANGE across the
    ambiguous-perception `alpha` dial of design note 4.3.

    With a flat 1.0 the architecture would bind an `alpha = 0` descendant -- a genuinely
    independent new observation -- as tightly as a pure replay, N_eff would sit at 1 across
    the whole dial, and P1-R4 (design note 7.3) could not pass by construction: the count
    readout would have no correct-direction dynamic range, which 7.3 says is exactly what
    makes a null under corruption uninterpretable. The architecture still does not know
    `alpha` -- that is world knowledge held only by the scorer; it infers a proxy for it
    from content it already stores.
    """
    return float(max(0.0, np.dot(_unit(descendant), _unit(ancestor))))


# --------------------------------------------------------------------------------------
# State
# --------------------------------------------------------------------------------------


@dataclass
class GroundTruth:
    """SCORER ONLY. Never passed to an inference-path operation."""

    H: int
    true_ancestor: List[int] = field(default_factory=list)  # -1 for a world event
    true_family: List[int] = field(default_factory=list)
    alpha: List[float] = field(default_factory=list)  # 1.0 = pure descendant
    seed_content: Dict[int, np.ndarray] = field(default_factory=dict)  # for fidelity
    kinds: List[str] = field(default_factory=list)

    def descendants(self) -> List[int]:
        return [i for i, a in enumerate(self.true_ancestor) if a >= 0]

    def world_events(self) -> List[int]:
        return [i for i, a in enumerate(self.true_ancestor) if a < 0]


@dataclass
class GenealogyStore:
    """Design note 5.1. Carries NO ground truth."""

    content: List[np.ndarray] = field(default_factory=list)
    t: List[float] = field(default_factory=list)
    edge_target: List[int] = field(default_factory=list)  # ancestry: -1 = none
    edge_w: List[float] = field(default_factory=list)
    explicit_family: List[int] = field(default_factory=list)  # asserted fresh family, -1
    assoc: Dict[Tuple[int, int], float] = field(default_factory=dict)  # association edges
    retrieval_events: List[int] = field(default_factory=list)  # per-trace read count
    next_family_id: int = 5000

    def n(self) -> int:
        return len(self.content)

    def add_trace(self, content: np.ndarray, t: float, ancestor: int, w: float) -> int:
        self.content.append(content)
        self.t.append(t)
        self.edge_target.append(ancestor)
        self.edge_w.append(w)
        self.explicit_family.append(-1)
        self.retrieval_events.append(0)
        return len(self.content) - 1

    def copy(self) -> "GenealogyStore":
        return GenealogyStore(
            content=list(self.content),
            t=list(self.t),
            edge_target=list(self.edge_target),
            edge_w=list(self.edge_w),
            explicit_family=list(self.explicit_family),
            assoc=dict(self.assoc),
            retrieval_events=list(self.retrieval_events),
            next_family_id=self.next_family_id,
        )

    def content_hash(self) -> str:
        h = hashlib.sha256()
        for c in self.content:
            h.update(np.asarray(c, dtype=np.float64).tobytes())
        return h.hexdigest()


# --------------------------------------------------------------------------------------
# Seeding and generation (contract op 1)
# --------------------------------------------------------------------------------------


def new_episode(
    content_rng: np.random.Generator, H: int, signal: float, noise: float, t0: float = 0.0
) -> Tuple[GenealogyStore, GroundTruth]:
    """One latent proposition H and one world event e0 (design note 4.1)."""
    store = GenealogyStore()
    truth = GroundTruth(H=H)
    c = H * signal * _W + noise * content_rng.normal(size=DIM)
    idx = store.add_trace(c, t0, -1, 0.0)
    truth.true_ancestor.append(-1)
    truth.true_family.append(0)
    truth.alpha.append(0.0)  # a world event contributes a full independent source
    truth.kinds.append("world_event")
    truth.seed_content[idx] = c.copy()
    return store, truth


def add_world_event(
    store: GenealogyStore,
    truth: GroundTruth,
    content_rng: np.random.Generator,
    signal: float,
    noise: float,
    t: float,
) -> int:
    """A genuinely independent second observation (P1-R2 and P1-R4 at alpha = 0)."""
    c = truth.H * signal * _W + noise * content_rng.normal(size=DIM)
    idx = store.add_trace(c, t, -1, 0.0)
    truth.true_ancestor.append(-1)
    truth.true_family.append(max(truth.true_family) + 1)
    truth.alpha.append(0.0)
    truth.kinds.append("world_event")
    truth.seed_content[idx] = c.copy()
    return idx


def spawn_descendant(
    store: GenealogyStore,
    truth: GroundTruth,
    ancestor_id: int,
    kind: str,
    content_rng: np.random.Generator,
    t: float,
    eta: float = 0.25,
    alpha: float = 1.0,
    signal: float = 1.0,
    noise: float = 1.0,
) -> int:
    """Contract op 1. Content derives from the ANCESTOR'S STORED TRACE, never from H.

    The one exception is `ambiguous_perception`, whose world term is explicit,
    parameterised by `alpha`, and recorded in `GroundTruth.alpha` so that the scorer's
    derived true source count (design note 4.3) accounts for it. `alpha = 1` is a pure
    descendant; `alpha = 0` is a genuinely independent new observation.
    """
    if kind not in DESCENDANT_KINDS:
        raise ValueError("unknown descendant kind: %s" % kind)
    base = store.content[ancestor_id]

    if kind == "replay":
        c = base + _rel_noise(content_rng, eta, base)
        eff_alpha = 1.0
    elif kind == "prediction":
        c = _A @ base + _rel_noise(content_rng, eta, base)
        eff_alpha = 1.0
    elif kind == "retrieved_memory":
        g = 0.5 * (1.0 + float(np.dot(_unit(base), _CUE)))  # cue-trace similarity bias
        g = min(max(g, 0.0), 1.0)
        c = (1.0 - 0.4 * g) * base + 0.4 * g * float(np.linalg.norm(base)) * _CUE
        c = c + _rel_noise(content_rng, eta, base)
        eff_alpha = 1.0
    else:  # ambiguous_perception
        world = truth.H * signal * _W + noise * content_rng.normal(size=DIM)
        c = alpha * base + (1.0 - alpha) * world + _rel_noise(content_rng, eta, base)
        eff_alpha = alpha

    idx = store.add_trace(c, t, ancestor_id, initial_binding(c, base))
    truth.true_ancestor.append(ancestor_id)
    truth.true_family.append(truth.true_family[ancestor_id])
    truth.alpha.append(eff_alpha)
    truth.kinds.append(kind)
    truth.seed_content[idx] = truth.seed_content.get(ancestor_id, base).copy()
    return idx


# --------------------------------------------------------------------------------------
# Degradation (contract op 2) -- the three processes P0 gated
# --------------------------------------------------------------------------------------


def _sim_matrix(store: GenealogyStore) -> np.ndarray:
    C = np.asarray([_unit(c) for c in store.content])
    return C @ C.T


def degrade(
    store: GenealogyStore,
    process: str,
    knob: float,
    steps: int,
    rng: np.random.Generator,
    dyn_noise: float = 0.35,
    mis_gamma: float = 2.0,
    mis_split_frac: float = 0.5,
) -> Dict[str, object]:
    """Contract op 2. Takes NO ancestry-indexed argument; returns a report, not an order.

    Reinstatement noise SCALES the pressure rather than perturbing the binding directly --
    P0 found that an additive multiplicative walk on the binding has a reflecting ceiling
    at 1.0 and therefore drifts downward, acting as a second uncontrolled degradation
    process that leaves the knob's null end already degraded.
    """
    if process not in PROCESSES:
        raise ValueError("unknown process: %s" % process)
    sim = _sim_matrix(store)
    relu = np.maximum(sim, 0.0)
    n = store.n()
    before = list(store.edge_w)
    n_repoint = 0
    n_relabel = 0

    for step in range(1, steps + 1):
        idx = [
            i
            for i in range(n)
            if store.edge_target[i] >= 0 and store.t[i] <= step and store.explicit_family[i] < 0
        ]
        if not idx:
            continue
        tgt = [store.edge_target[i] for i in idx]

        if process == "misbinding":
            for i, a in zip(idx, tgt):
                row = relu[i].copy()
                row[i] = -1.0
                row[a] = -1.0
                comp = int(row.argmax())
                p_fire = min(max(knob * max(sim[i, comp], 0.0) ** mis_gamma, 0.0), 1.0)
                if rng.random() < p_fire:
                    if rng.random() < mis_split_frac:
                        store.explicit_family[i] = store.next_family_id
                        store.next_family_id += 1
                        store.edge_target[i] = -1
                        n_relabel += 1
                    else:
                        store.edge_target[i] = comp
                        n_repoint += 1
            continue

        if process == "decay":
            pressure = np.full(len(idx), 1.0 / knob if knob > 0 else 0.0)
        else:  # interference
            rows = np.asarray(
                [relu[i].sum() - relu[i, i] - relu[i, a] for i, a in zip(idx, tgt)]
            )
            pressure = knob * rows / max(n - 2, 1)

        if dyn_noise > 0:
            pressure = np.maximum(pressure * (1.0 + dyn_noise * rng.normal(size=len(idx))), 0.0)
        for k, i in enumerate(idx):
            store.edge_w[i] = min(max(store.edge_w[i] * math.exp(-pressure[k]), 0.0), 1.0)

    return {
        "process": process,
        "knob": knob,
        "steps": steps,
        "mean_binding_before": float(np.mean([b for b in before if b > 0])) if any(before) else 0.0,
        "mean_binding_after": float(
            np.mean([w for i, w in enumerate(store.edge_w) if store.edge_target[i] >= 0])
        )
        if any(t >= 0 for t in store.edge_target)
        else 0.0,
        "repointed": n_repoint,
        "relabelled": n_relabel,
    }


# --------------------------------------------------------------------------------------
# Replay (contract op 3)
# --------------------------------------------------------------------------------------


def replay(
    store: GenealogyStore,
    truth: GroundTruth,
    trace_id: int,
    n: int,
    content_rng: np.random.Generator,
    mode: str = "spawn",
    t: float = 1.0,
    eta: float = 0.25,
) -> List[int]:
    """Contract op 3. `mode='spawn'` produces descendants; `mode='in_place'` performs
    retrieval/reinstatement events over the EXISTING trace without creating any.

    `in_place` is what P1-R7 (fluency versus cardinality) needs and what P3's healthy-replay
    gate depends on: it moves retrieval-event count while holding descendant cardinality
    fixed, which is the only way to separate the two confounded causes.

    Deliberately does NOT advance `degrade` -- design note section 6 requires the two to be
    orthogonal so P3 can hold one fixed while sweeping the other.
    """
    if mode == "in_place":
        store.retrieval_events[trace_id] += n
        return []
    out = []
    for _ in range(n):
        d = spawn_descendant(store, truth, trace_id, "replay", content_rng, t, eta=eta)
        store.retrieval_events[trace_id] += 1
        out.append(d)
    return out


def link(store: GenealogyStore, a: int, b: int, strength: float = 1.0) -> None:
    """Offline associative linking (E43). Writes an ASSOCIATION edge, never an ancestry
    edge -- see the module docstring on why that separation is what lets P1-R2 pass."""
    key = (min(a, b), max(a, b))
    store.assoc[key] = min(1.0, store.assoc.get(key, 0.0) + strength)


# --------------------------------------------------------------------------------------
# Readouts (contract ops 4-8). Ops 4, 5, 6, 8 see only the store.
# --------------------------------------------------------------------------------------


def _ancestry_path(store: GenealogyStore, i: int) -> Dict[int, float]:
    """Reachable ancestors of i with cumulative binding strength. Halts at an explicitly
    asserted fresh family: such a trace claims to have no ancestry at all."""
    out = {i: 1.0}
    cur, acc, guard = i, 1.0, 0
    while guard < 64:
        guard += 1
        if store.explicit_family[cur] >= 0:
            break
        a = store.edge_target[cur]
        if a < 0:
            break
        acc *= store.edge_w[cur]
        if acc <= 0.0:
            break
        out[a] = max(out.get(a, 0.0), acc)
        cur = a
    return out


def shared_ancestry_prob(store: GenealogyStore, i: int, j: int) -> float:
    if i == j:
        return 1.0
    pi, pj = _ancestry_path(store, i), _ancestry_path(store, j)
    common = set(pi) & set(pj)
    return max((pi[c] * pj[c] for c in common), default=0.0)


def association_strength(store: GenealogyStore, a: int, b: int) -> float:
    """Contract op 4 -- did a relation form? Reads the ASSOCIATION edge set plus any
    ancestry-mediated relation, and is a PAIR-level primitive; it is not the set-level
    aggregate op 6 computes, and neither is derived from the other."""
    key = (min(a, b), max(a, b))
    return max(store.assoc.get(key, 0.0), shared_ancestry_prob(store, a, b))


def source_attribution(store: GenealogyStore, trace_id: int) -> Dict[str, float]:
    """Contract op 5 -- P(external | representation), from the STORED tag (P1-R5 route).

    A trace the architecture believes is bound to an ancestor is internally generated; one
    with no surviving binding reads as an external observation. Note this is a different
    function of the edge set from op 6, and they dissociate: a re-pointed edge keeps
    attribution low (a strong binding survives, to the wrong trace) while the count rises.
    """
    if store.explicit_family[trace_id] >= 0:
        return {"p_external": 1.0, "family": float(store.explicit_family[trace_id])}
    w = store.edge_w[trace_id] if store.edge_target[trace_id] >= 0 else 0.0
    return {"p_external": float(1.0 - w), "family": float(_root_of(store, trace_id))}


def _root_of(store: GenealogyStore, i: int) -> int:
    cur, guard = i, 0
    while guard < 64:
        guard += 1
        if store.explicit_family[cur] >= 0:
            return store.explicit_family[cur]
        a = store.edge_target[cur]
        if a < 0 or store.edge_w[cur] <= 0.0:
            return cur
        cur = a
    return cur


def effective_source_count(
    store: GenealogyStore,
    trace_set: Sequence[int],
    absent_policy: str = "independent",
    unknown_below: float = 0.25,
) -> float:
    """Contract op 6 -- N_eff as the ARCHITECTURE computes it from its own genealogy.

    Never from ground truth. See the module docstring for the formula and for what
    `absent_policy` measures (P2 as a sub-measurement of this readout layer).
    """
    if absent_policy not in ABSENT_POLICIES:
        raise ValueError("unknown absent_policy: %s" % absent_policy)
    ids = list(trace_set)
    if not ids:
        return 0.0
    m = len(ids)
    P = np.zeros((m, m))
    for a in range(m):
        for b in range(m):
            P[a, b] = 1.0 if a == b else shared_ancestry_prob(store, ids[a], ids[b])

    if absent_policy != "independent":
        # An "unknown" pair is one the architecture holds no USABLE ancestry evidence about.
        # The default consumes that as independence; these policies do not.
        #
        # The threshold is `unknown_below`, NOT exact zero. Decay drives a binding strength
        # toward zero asymptotically and essentially never reaches it, so an
        # exact-zero test leaves the policy INERT -- measured: identical inflation of
        # +3.753 under all three policies, because the fill never fired. The boundary is
        # the regime classifier's own uncertain-band floor (`theta_low`), which is where
        # the architecture stops treating a binding as evidence of anything.
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


def true_effective_source_count(truth: GroundTruth, trace_set: Sequence[int]) -> float:
    """SCORER. The derived target of design note 4.3: independent world information is an
    analytic function of the alpha values, not an experimenter-declared '1'."""
    total = 0.0
    seen_families = set()
    for i in trace_set:
        if truth.true_ancestor[i] < 0:
            if truth.true_family[i] not in seen_families:
                seen_families.add(truth.true_family[i])
                total += 1.0
        else:
            total += 1.0 - truth.alpha[i]
    return total


def retrieval_fidelity(store: GenealogyStore, truth: GroundTruth, trace_id: int) -> float:
    """Contract op 8. Reconstruction quality against the true seed content. Distinct from
    op 7 (about H) and op 4 (about a relation); P3-R3 matches on it."""
    tgt = truth.seed_content.get(trace_id)
    if tgt is None:
        return float("nan")
    return float(np.dot(_unit(store.content[trace_id]), _unit(tgt)))


# --------------------------------------------------------------------------------------
# Belief and calibration (contract op 7 -- SCORER)
# --------------------------------------------------------------------------------------


def vote(store: GenealogyStore, trace_id: int) -> int:
    """The evidence a stored trace carries about H, as a function of CONTENT only."""
    return 1 if float(np.dot(store.content[trace_id], _W)) >= 0 else -1


def read_vote(
    store: GenealogyStore,
    trace_id: int,
    rng: np.random.Generator,
    read_noise: float,
    n_reads: int = 1,
) -> int:
    """A vote formed by READING the stored trace `n_reads` times through a noisy channel.

    This is what makes P1-R3's legitimate-computation arm mechanical rather than asserted.
    Repeated computation over a FIXED observation set averages the read noise down, so the
    single-source reliability `p` genuinely rises and ground-truth accuracy rises with it --
    E30's regime, a readout tracking a drifting code without any new evidence. Nothing
    about the ancestry representation is touched, so `N_eff` must stay at 1.

    `n_reads = 1` recovers an ordinary noisy read; `read_noise = 0` recovers `vote`.
    """
    base = float(np.dot(store.content[trace_id], _W))
    if read_noise <= 0 or n_reads <= 1:
        acc = base + (read_noise * float(rng.normal()) if read_noise > 0 else 0.0)
    else:
        acc = base + read_noise * float(rng.normal(size=n_reads).mean())
    return 1 if acc >= 0 else -1


def confidence(votes: Sequence[int], p_est: float, n_eff: float) -> float:
    """assay 001's `independence_aware_confidence`, in the two-term form design note 7.2
    requires: log-odds(H) = (N_eff / n) * |sum of votes| * logit(p).

    ONE rule, not conditioned on which arm or condition is running (design note section 3's
    non-tautology corollary). Legitimate computation is licensed to raise `p` and forbidden
    to raise `N_eff`; false independence does the reverse. Both raise confidence; only one
    of them is entitled to.
    """
    n = len(votes)
    if n == 0:
        return 0.5
    signed = abs(sum(votes))
    return sigmoid(signed * (n_eff / n) * logit(p_est))


def belief(store: GenealogyStore, trace_set: Sequence[int]) -> int:
    s = sum(vote(store, i) for i in trace_set)
    return 1 if s >= 0 else -1


# --------------------------------------------------------------------------------------
# Regime classification (design note 5.3) -- SCORER
# --------------------------------------------------------------------------------------


class _UF:
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


def _components(store: GenealogyStore, theta_high: float):
    uf = _UF(store.n())
    conf = [
        store.edge_target[i] >= 0
        and store.edge_w[i] >= theta_high
        and store.explicit_family[i] < 0
        for i in range(store.n())
    ]
    for i in range(store.n()):
        if conf[i]:
            uf.union(i, store.edge_target[i])
    return uf, conf


def classify_edges(
    store: GenealogyStore, truth: GroundTruth, theta_high: float = 0.60, theta_low: float = 0.25
) -> Dict[str, int]:
    """Per-EDGE regime counts.

    P0 found that the episode-level classifier scores an episode by its WORST surviving
    edge, so episode-level SOFT goes as (1 - p_absent_edge)^n_edges and the transition
    compresses into a narrow knob window. The edge-level view is therefore the PRIMARY
    stratification here (P0 result note section 7, recommendation 2), with the episode-level
    view kept as the secondary, literature-comparable one.
    """
    uf, conf = _components(store, theta_high)
    counts = {r: 0 for r in REGIMES}
    for d in truth.descendants():
        a = truth.true_ancestor[d]
        if store.explicit_family[d] >= 0 or (conf[d] and uf.find(d) != uf.find(a)):
            counts["FALSE_SPLIT"] += 1
            continue
        eff = store.edge_w[d] if store.edge_target[d] == a else 0.0
        if eff >= theta_high:
            counts["VERIDICAL"] += 1
        elif eff >= theta_low:
            counts["SOFT"] += 1
        else:
            counts["ABSENT"] += 1
    return counts


def classify_regime(
    store: GenealogyStore, truth: GroundTruth, theta_high: float = 0.60, theta_low: float = 0.25
) -> str:
    """Per-EPISODE regime, by the worst surviving true edge, with FALSE_SPLIT dominating."""
    uf, conf = _components(store, theta_high)
    desc = truth.descendants()
    for d in desc:
        a = truth.true_ancestor[d]
        if store.explicit_family[d] >= 0 or (conf[d] and uf.find(d) != uf.find(a)):
            return "FALSE_SPLIT"
    if not desc:
        return "VERIDICAL"
    eff = [store.edge_w[d] if store.edge_target[d] == truth.true_ancestor[d] else 0.0 for d in desc]
    if min(eff) >= theta_high:
        return "VERIDICAL"
    if min(eff) >= theta_low:
        return "SOFT"
    return "ABSENT"
