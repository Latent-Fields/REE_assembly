#!/usr/bin/env python3
"""
Build docs/assets/data/epistemic_overlay.json -- the epistemic-overlay GRAPH layer
(Phase 1, Option C + C-slice of Option D).

DERIVE-ONLY. Reads two inputs and writes one derived output:
  reads : docs/claims/claims.yaml                       (emergent_from edges)
          evidence/experiments/claim_evidence.v1.json   (per-node Beta posteriors)
  writes: docs/assets/data/epistemic_overlay.json       (viz-ready graph overlay)

It NEVER mutates a hand-authored source and PROMOTES/DEMOTES NOTHING. It surfaces:
  1. a per-claim viz bundle: the exp/lit Beta posteriors (mirrored from the
     canonical claim_evidence matrix), own-evidence belief, and a support/weaken
     conflict split for split-fill rendering.
  2. a promotion-gate HONESTY surface: how the candidate->provisional gate WOULD
     read under "posterior mean >= 0.62 AND credible interval excludes 0.5",
     compared against the current bare-threshold heuristic. Informational only.
  3. the emergent_from SINGLE-HOP alarm: a claim believed while a claim it is
     emergent_from is contradicted (unsupported_foundation) or untested
     (untested_foundation). ONE hop -- not belief propagation.

Phase-2 seed: this is the graph layer a factor-graph/MRF grows into. The unary
potentials it reads (exp_posterior/lit_posterior) do not change; pairwise
potentials and damped loopy BP replace the single-hop alarm here. Plan:
evidence/planning/epistemic_overlay_plan.md.

Output is labelled "model-based, not yet calibrated" -- there is no resolved-claim
validation set yet. Do not overstate rigour downstream.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CLAIMS_YAML = REPO_ROOT / "docs" / "claims" / "claims.yaml"
CLAIM_EVIDENCE = REPO_ROOT / "evidence" / "experiments" / "claim_evidence.v1.json"
OUTPUT_JSON = REPO_ROOT / "docs" / "assets" / "data" / "epistemic_overlay.json"

# Thresholds (mirror the existing gate + memo sec 4).
GATE_MEAN = 0.62          # candidate->provisional exp_conf gate (decision_criteria.v1)
BELIEF_HIGH = 0.62        # "believed" child
BELIEF_LOW = 0.45         # "contradicted/weak" foundation

# ---------------------------------------------------------------------------
# Phase 2 (Option B): pairwise MRF + damped loopy belief propagation.
# The ONLY invented objects are the pairwise potentials -- initialised WEAK.
# Unary potentials are the EXISTING per-node Beta posteriors, reused unchanged.
# Plan: evidence/planning/epistemic_overlay_plan.md (Phase 2 section).
# ---------------------------------------------------------------------------
W_EMERGENT = 1.6          # STRONG directional coupling on emergent_from edges
W_DEPENDS = 0.15          # WEAK near-uniform coupling on generic depends_on (w=0 -> per-node scoring)
BP_DAMPING = 0.5          # message-space damping lambda (oscillation control)
BP_MAX_ITERS = 200        # loopy BP iteration cap
BP_TOL = 1e-6             # convergence tolerance on max |delta message|_inf
BP_OSC_WINDOW = 10        # trailing window used to detect non-monotone (oscillating) deltas
_PROB_EPS = 1e-9          # clamp to keep logs finite
MOVE_EPS = 0.01           # |propagated - unary| above which a belief is counted "moved"


def _clamp01(x):
    return max(_PROB_EPS, min(1.0 - _PROB_EPS, float(x)))


def _build_graph(claims):
    """Undirected edge set over ALL claims for the MRF. emergent_from takes
    precedence over depends_on for the same pair (it carries the strong,
    directional potential). Returns:
      node_ids     : ordered list of every claim id (connector nodes included)
      edges        : list of (a, b, kind, child) -- kind in {emergent_from,
                     depends_on}; child = the emergent claim for emergent_from,
                     else None (depends_on is symmetric so orientation is moot).
    A pair is added at most once; self-loops are dropped."""
    node_ids = [c["id"] for c in claims if c.get("id")]
    id_set = set(node_ids)
    edge_map = {}  # frozenset({a,b}) -> (kind, child_or_None)

    # emergent_from first (precedence + directional).
    for c in claims:
        cid = c.get("id")
        if not cid:
            continue
        for parent in (c.get("emergent_from") or []):
            if parent == cid or parent not in id_set:
                continue
            edge_map[frozenset((cid, parent))] = ("emergent_from", cid)

    # depends_on + coupled_with: symmetric, weak; skip any pair already carrying
    # emergent_from. Since the 2026-09-04 edge-type split (GOV-EDGE-1,
    # scripts/split_claim_edge_types.py) `depends_on` is the DAG prerequisite
    # layer and `coupled_with` the undirected reciprocal-architecture layer. The
    # MRF never used orientation, so BOTH feed the same weak associative
    # potential and the overlay is byte-identical before and after the split
    # (verified 2026-09-04). Do not weight them differently without re-running
    # that parity check.
    for field in ("depends_on", "coupled_with"):
        for c in claims:
            cid = c.get("id")
            if not cid:
                continue
            for parent in (c.get(field) or []):
                if parent == cid or parent not in id_set:
                    continue
                key = frozenset((cid, parent))
                if key in edge_map:
                    continue
                edge_map[key] = (field, None)

    edges = []
    for key, (kind, child) in edge_map.items():
        a, b = tuple(key) if len(key) == 2 else (next(iter(key)), next(iter(key)))
        edges.append((a, b, kind, child))
    return node_ids, edges


def _pairwise_from_i(kind, child, i, w):
    """2x2 pairwise potential psi[x_i][x_j] for the directed message i->j at
    EFFECTIVE coupling strength `w` (degree-normalised by the caller).
      depends_on : symmetric associative Potts, exp(+w) on agree / exp(-w) on disagree.
      emergent_from (child C emergent_from parent P): directional -- penalise the
        single incoherent corner (C=supported, P=unsupported). Base matrix is in
        (x_C, x_P) order; if i is the parent we transpose."""
    import math
    if kind in ("depends_on", "coupled_with"):
        a = math.exp(w)
        d = math.exp(-w)
        return [[a, d], [d, a]]
    # emergent_from base in (child, parent) order.
    pen = math.exp(-w)
    base = [[1.0, 1.0], [pen, 1.0]]
    if i == child:
        return base
    # i is the parent -> psi[x_parent][x_child] = base[x_child][x_parent] (transpose).
    return [[base[0][0], base[1][0]], [base[0][1], base[1][1]]]


def _edge_weights(node_ids, edges):
    """Type-specific degree-normalised effective coupling per edge. Dense,
    untyped depends_on hubs must NOT saturate under loopy BP, so their coupling
    is scaled by 1/sqrt(dep_deg_a * dep_deg_b) (a symmetric normalised-adjacency
    regularisation). The sparse, load-bearing emergent_from edges are normalised
    only by emergent-degree (usually 1-3), so a child with few foundations keeps
    a strong pull while a hub-foundation with many emergents does not saturate.
    Returns {(a,b,kind,child): w_eff} keyed by the edge tuple identity index."""
    import math
    dep_deg = {nid: 0 for nid in node_ids}
    ef_deg = {nid: 0 for nid in node_ids}
    for (a, b, kind, _child) in edges:
        if kind in ("depends_on", "coupled_with"):
            dep_deg[a] += 1
            dep_deg[b] += 1
        else:
            ef_deg[a] += 1
            ef_deg[b] += 1
    weights = []
    for (a, b, kind, _child) in edges:
        if kind in ("depends_on", "coupled_with"):
            denom = math.sqrt(max(1, dep_deg[a]) * max(1, dep_deg[b]))
            weights.append(W_DEPENDS / denom)
        else:
            denom = math.sqrt(max(1, ef_deg[a]) * max(1, ef_deg[b]))
            weights.append(W_EMERGENT / denom)
    return weights


def _loopy_bp(node_ids, edges, unary):
    """Damped loopy sum-product BP over the pairwise MRF for ONE channel.
      unary : dict id -> P(supported) in [0,1] (the reused Beta posterior mean;
              0.5 for connector nodes with no own evidence in this channel).
    Returns (beliefs, report):
      beliefs : dict id -> propagated P(supported)
      report  : {iterations, converged, final_max_delta, oscillating, damping,
                 max_iters, tol}
    Message space is 2-vectors normalised to sum 1. Damping in message space.
    The 132 cycles are tolerated natively (loopy BP); damping controls oscillation."""
    import math
    # phi[node] = [P(unsupported), P(supported)], clamped for finite logs.
    phi = {}
    for nid in node_ids:
        m = _clamp01(unary.get(nid, 0.5))
        phi[nid] = [1.0 - m, m]

    # Directed message list. Each directed edge i->j records the potential
    # psi[x_i][x_j] and the reverse-key (j,i) needed for the exclude-j product.
    edge_w = _edge_weights(node_ids, edges)
    neighbors = {nid: [] for nid in node_ids}  # nid -> list of (neighbor, dkey_incoming (k,nid))
    messages = {}  # (i,j) -> [m0, m1]
    directed = []  # (i, j, psi_ij)
    for idx, (a, b, kind, child) in enumerate(edges):
        w = edge_w[idx]
        psi_ab = _pairwise_from_i(kind, child, a, w)  # psi[x_a][x_b] for a->b
        psi_ba = _pairwise_from_i(kind, child, b, w)  # psi[x_b][x_a] for b->a
        directed.append((a, b, psi_ab))
        directed.append((b, a, psi_ba))
        messages[(a, b)] = [0.5, 0.5]
        messages[(b, a)] = [0.5, 0.5]
        neighbors[a].append((b, (b, a)))
        neighbors[b].append((a, (a, b)))

    deltas = []
    converged = False
    iters = 0
    for it in range(1, BP_MAX_ITERS + 1):
        iters = it
        # Per-node log-product of phi and ALL incoming messages (stable exclude-j).
        logprod = {}
        for nid in node_ids:
            lp0 = math.log(phi[nid][0])
            lp1 = math.log(phi[nid][1])
            for (_k, dkey) in neighbors[nid]:
                mk = messages[dkey]
                lp0 += math.log(max(mk[0], _PROB_EPS))
                lp1 += math.log(max(mk[1], _PROB_EPS))
            logprod[nid] = (lp0, lp1)

        max_delta = 0.0
        new_messages = {}
        for (i, j, psi) in directed:
            mji = messages[(j, i)]  # divide this out of i's product
            lp = logprod[i]
            # excl_i[x_i] = phi_i(x_i) * prod_{k != j} m_{k->i}(x_i)
            e0 = math.exp(lp[0] - math.log(max(mji[0], _PROB_EPS)))
            e1 = math.exp(lp[1] - math.log(max(mji[1], _PROB_EPS)))
            # m_{i->j}(x_j) = sum_{x_i} excl_i(x_i) * psi[x_i][x_j]
            n0 = e0 * psi[0][0] + e1 * psi[1][0]
            n1 = e0 * psi[0][1] + e1 * psi[1][1]
            s = n0 + n1
            if s <= 0.0:
                n0, n1 = 0.5, 0.5
            else:
                n0, n1 = n0 / s, n1 / s
            old = messages[(i, j)]
            d0 = (1.0 - BP_DAMPING) * n0 + BP_DAMPING * old[0]
            d1 = (1.0 - BP_DAMPING) * n1 + BP_DAMPING * old[1]
            sd = d0 + d1
            d0, d1 = d0 / sd, d1 / sd
            new_messages[(i, j)] = [d0, d1]
            delta = max(abs(d0 - old[0]), abs(d1 - old[1]))
            if delta > max_delta:
                max_delta = delta
        messages = new_messages
        deltas.append(max_delta)
        if max_delta < BP_TOL:
            converged = True
            break

    # Final beliefs from the converged (or capped) messages.
    beliefs = {}
    for nid in node_ids:
        lp0 = math.log(phi[nid][0])
        lp1 = math.log(phi[nid][1])
        for (_k, dkey) in neighbors[nid]:
            mk = messages[dkey]
            lp0 += math.log(max(mk[0], _PROB_EPS))
            lp1 += math.log(max(mk[1], _PROB_EPS))
        b0 = math.exp(lp0)
        b1 = math.exp(lp1)
        s = b0 + b1
        beliefs[nid] = 0.5 if s <= 0.0 else b1 / s

    # Oscillation: not converged AND the trailing deltas are non-monotone/rising.
    oscillating = False
    if not converged and len(deltas) >= BP_OSC_WINDOW:
        window = deltas[-BP_OSC_WINDOW:]
        # rising or bouncing rather than steadily shrinking.
        if window[-1] >= window[0] or any(
            window[k] > window[k - 1] for k in range(1, len(window))
        ):
            oscillating = True

    report = {
        "iterations": iters,
        "converged": converged,
        "final_max_delta": round(deltas[-1], 10) if deltas else None,
        "oscillating": oscillating,
        "damping": BP_DAMPING,
        "max_iters": BP_MAX_ITERS,
        "tol": BP_TOL,
    }
    return beliefs, report


def _conflict_split(direction_counts):
    """Support/weaken split for split-fill rendering + conflict_ratio.
    conflict_ratio = 2*min(s,w)/(s+w): 0 = no conflict, 1 = perfectly split."""
    supports = int(direction_counts.get("supports", 0))
    weakens = int(direction_counts.get("weakens", 0))
    total = supports + weakens
    ratio = round((2.0 * min(supports, weakens)) / float(total), 3) if total else 0.0
    return {"supports": supports, "weakens": weakens, "conflict_ratio": ratio}


def _own_belief(meta):
    """Own-evidence (unary) belief: prefer experimental, fall back to literature,
    else None (untested). Returns (source, mean, posterior_dict) or (None, None, None)."""
    exp = meta.get("exp_posterior") or {}
    lit = meta.get("lit_posterior") or {}
    if int(exp.get("n_entries", 0)) > 0:
        return "exp", exp.get("mean"), exp
    if int(lit.get("n_entries", 0)) > 0:
        return "lit", lit.get("mean"), lit
    return None, None, None


def _posterior_gate(meta):
    """Honest promotion-gate surface for candidate->provisional. Compares the
    posterior reading (mean >= 0.62 AND CI excludes 0.5) against the current
    bare exp_conf >= 0.62 heuristic. Informational -- flips no status."""
    exp = meta.get("exp_posterior") or {}
    mean = exp.get("mean")
    ci_low = exp.get("ci_low")
    ci_high = exp.get("ci_high")
    exp_conf = float(meta.get("experimental_confidence", 0.0) or 0.0)
    if mean is None or ci_low is None or ci_high is None:
        return None
    ci_excludes_half = (ci_low > 0.5) or (ci_high < 0.5)
    would_promote = (mean >= GATE_MEAN) and (ci_low > 0.5)
    heuristic_would_promote = exp_conf >= GATE_MEAN
    return {
        "mean": mean,
        "ci_low": ci_low,
        "ci_high": ci_high,
        "ci_excludes_half": ci_excludes_half,
        "would_promote_candidate_to_provisional": would_promote,
        "heuristic_exp_conf": round(exp_conf, 3),
        "heuristic_would_promote": heuristic_would_promote,
        "agrees_with_current_heuristic": would_promote == heuristic_would_promote,
        "note": "confidence dimension only; the live gate also requires entry"
                " count, conflict_ratio and >=1 supporting entry",
    }


def _emergent_alarm(child_id, parents, ev_claims):
    """Single-hop emergent_from alarm. Fires ONLY when the child is itself
    believed (own-evidence >= HIGH). Distinguishes a contradicted foundation
    (unsupported_foundation: parent has evidence and belief <= LOW) from an
    untested one (untested_foundation: parent has no evidence at all). Absence of
    evidence is NOT evidence of absence -- kept as a separate, softer flag."""
    child_meta = ev_claims.get(child_id)
    if not child_meta:
        return None
    _, child_mean, _ = _own_belief(child_meta)
    if child_mean is None or child_mean < BELIEF_HIGH:
        return None  # child not believed -> a weak foundation is unremarkable

    unsupported = []
    untested = []
    for p in parents:
        p_meta = ev_claims.get(p)
        if not p_meta:
            untested.append({"parent": p, "reason": "no_evidence_entries"})
            continue
        _, p_mean, _ = _own_belief(p_meta)
        if p_mean is None:
            untested.append({"parent": p, "reason": "no_directional_evidence"})
        elif p_mean <= BELIEF_LOW:
            unsupported.append({
                "parent": p,
                "parent_mean": p_mean,
                "gap": round(child_mean - p_mean, 4),
            })

    if not unsupported and not untested:
        return None
    out = {"child_mean": child_mean}
    if unsupported:
        unsupported.sort(key=lambda d: d["parent_mean"])  # weakest first
        out["unsupported_foundation"] = {
            "weakest_parent": unsupported[0]["parent"],
            "weakest_parent_mean": unsupported[0]["parent_mean"],
            "gap": unsupported[0]["gap"],
            "all": unsupported,
        }
    if untested:
        out["untested_foundation"] = {"parents": untested}
    return out


def main():
    if not CLAIMS_YAML.exists():
        print(f"ERROR: {CLAIMS_YAML} not found", file=sys.stderr)
        sys.exit(1)
    if not CLAIM_EVIDENCE.exists():
        print(f"ERROR: {CLAIM_EVIDENCE} not found -- run build_experiment_indexes.py first",
              file=sys.stderr)
        sys.exit(1)

    with open(CLAIMS_YAML, encoding="utf-8") as f:
        claims = yaml.safe_load(f)
    if not isinstance(claims, list):
        print("ERROR: claims.yaml top level must be a list", file=sys.stderr)
        sys.exit(1)

    ev = json.loads(CLAIM_EVIDENCE.read_text(encoding="utf-8"))
    ev_claims = ev.get("claims", {}) if isinstance(ev, dict) else {}
    posterior_model = ev.get("posterior_model", {})

    emergent_map = {}
    for c in claims:
        cid = c.get("id")
        if not cid:
            continue
        efrom = c.get("emergent_from") or []
        if efrom:
            emergent_map[cid] = list(efrom)

    overlay = {}
    n_unsupported = 0
    n_untested = 0
    n_gate_disagree = 0
    for cid, meta in ev_claims.items():
        source, mean, _post = _own_belief(meta)
        entry = {
            "exp_posterior": meta.get("exp_posterior"),
            "lit_posterior": meta.get("lit_posterior"),
            "own_belief": {"source": source, "mean": mean},
            "conflict": _conflict_split(meta.get("direction_counts", {})),
        }
        gate = _posterior_gate(meta)
        if gate:
            entry["posterior_gate"] = gate
            if not gate["agrees_with_current_heuristic"]:
                n_gate_disagree += 1
        if cid in emergent_map:
            entry["emergent_from"] = emergent_map[cid]
        overlay[cid] = entry

    # Emergent alarms: iterate over claims WITH emergent_from (child may or may
    # not itself have an evidence row -- if it has none it cannot be "believed",
    # so the alarm self-suppresses inside _emergent_alarm).
    for cid, parents in emergent_map.items():
        alarm = _emergent_alarm(cid, parents, ev_claims)
        if alarm:
            overlay.setdefault(cid, {"exp_posterior": None, "lit_posterior": None,
                                     "own_belief": {"source": None, "mean": None},
                                     "conflict": _conflict_split({}),
                                     "emergent_from": parents})
            overlay[cid]["alarms"] = alarm
            if "unsupported_foundation" in alarm:
                n_unsupported += 1
            if "untested_foundation" in alarm:
                n_untested += 1

    # -----------------------------------------------------------------------
    # Phase 2: pairwise MRF + damped loopy BP. Two DECOUPLED channels (exp, lit).
    # Unary = the reused Beta posterior mean; connector nodes (no own evidence in
    # a channel) get a uniform 0.5 unary but still pass messages. Only pairwise
    # potentials are invented, initialised weak. Promotes/demotes nothing.
    # -----------------------------------------------------------------------
    node_ids, edges = _build_graph(claims)

    def _channel_unary(post_key):
        u = {}
        for nid in node_ids:
            meta = ev_claims.get(nid)
            post = (meta or {}).get(post_key) or {}
            if int(post.get("n_entries", 0)) > 0 and isinstance(post.get("mean"), (int, float)):
                u[nid] = float(post["mean"])
            else:
                u[nid] = 0.5  # connector / no own evidence in this channel
        return u

    exp_unary = _channel_unary("exp_posterior")
    lit_unary = _channel_unary("lit_posterior")
    exp_prop, exp_report = _loopy_bp(node_ids, edges, exp_unary)
    lit_prop, lit_report = _loopy_bp(node_ids, edges, lit_unary)

    # Neighbour degree (for the per-node n_neighbors field + animation).
    degree = {nid: 0 for nid in node_ids}
    for (a, b, _kind, _child) in edges:
        degree[a] = degree.get(a, 0) + 1
        degree[b] = degree.get(b, 0) + 1

    # Attach propagated belief ONLY where the node has own evidence in that
    # channel (guardrail: propagated is always shown beside its own unary).
    n_moved_exp = 0
    n_moved_lit = 0
    movers = []
    for cid, entry in overlay.items():
        ep = entry.get("exp_posterior") or {}
        lp = entry.get("lit_posterior") or {}
        if int(ep.get("n_entries", 0)) > 0 and isinstance(ep.get("mean"), (int, float)):
            unary = float(ep["mean"])
            prop = exp_prop.get(cid, unary)
            delta = round(prop - unary, 4)
            entry["exp_propagated"] = {
                "mean": round(prop, 4),
                "delta_vs_unary": delta,
                "n_neighbors": degree.get(cid, 0),
            }
            if abs(delta) > MOVE_EPS:
                n_moved_exp += 1
                movers.append({"id": cid, "channel": "exp", "unary": round(unary, 4),
                               "propagated": round(prop, 4), "delta": delta})
        if int(lp.get("n_entries", 0)) > 0 and isinstance(lp.get("mean"), (int, float)):
            unary = float(lp["mean"])
            prop = lit_prop.get(cid, unary)
            delta = round(prop - unary, 4)
            entry["lit_propagated"] = {
                "mean": round(prop, 4),
                "delta_vs_unary": delta,
                "n_neighbors": degree.get(cid, 0),
            }
            if abs(delta) > MOVE_EPS:
                n_moved_lit += 1
                movers.append({"id": cid, "channel": "lit", "unary": round(unary, 4),
                               "propagated": round(prop, 4), "delta": delta})

    movers.sort(key=lambda d: abs(d["delta"]), reverse=True)
    movers = movers[:40]

    n_emergent_edges = sum(1 for e in edges if e[2] == "emergent_from")
    n_depends_edges = sum(1 for e in edges if e[2] == "depends_on")
    n_coupled_edges = sum(1 for e in edges if e[2] == "coupled_with")
    mrf_block = {
        "model": "pairwise-mrf-loopy-bp",
        "pairwise": {
            "emergent_from": {
                "coupling": W_EMERGENT,
                "form": "directional; penalizes child-supported-while-parent-unsupported",
                "degree_norm": "1/sqrt(ef_deg_a * ef_deg_b)",
            },
            "depends_on": {
                "coupling": W_DEPENDS,
                "form": "symmetric-associative (near-uniform); w=0 -> per-node scoring",
                "degree_norm": "1/sqrt(dep_deg_a * dep_deg_b)",
            },
            "note": "only pairwise potentials are invented; unary = existing Beta"
                    " posteriors, reused unchanged. Coupling is degree-normalised"
                    " (symmetric normalised-adjacency) so dense untyped depends_on"
                    " hubs do not saturate under loopy BP; w=0 -> per-node scoring.",
        },
        "bp": {
            "damping": BP_DAMPING,
            "max_iters": BP_MAX_ITERS,
            "tol": BP_TOL,
            "states": ["unsupported", "supported"],
        },
        "convergence": {"exp": exp_report, "lit": lit_report},
        "graph": {
            "nodes": len(node_ids),
            "depends_on_edges": n_depends_edges,
            "coupled_with_edges": n_coupled_edges,
            "emergent_from_edges": n_emergent_edges,
        },
        "movers": movers,
        "calibration": "model-based, not yet calibrated",
    }

    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    out = {
        "schema_version": "epistemic_overlay/v1",
        "generated_at_utc": generated_at,
        "phase": "1 (Option C + C-slice of D)",
        "derive_only": True,
        "promotes_demotes": "nothing",
        "posterior_model": posterior_model,
        "calibration": posterior_model.get("calibration", "model-based, not yet calibrated"),
        "thresholds": {
            "gate_mean": GATE_MEAN,
            "belief_high": BELIEF_HIGH,
            "belief_low": BELIEF_LOW,
        },
        "mrf": mrf_block,
        "counts": {
            "claims": len(overlay),
            "emergent_from_claims": len(emergent_map),
            "unsupported_foundation_alarms": n_unsupported,
            "untested_foundation_alarms": n_untested,
            "posterior_gate_disagreements": n_gate_disagree,
            "beliefs_moved_exp": n_moved_exp,
            "beliefs_moved_lit": n_moved_lit,
        },
        "plan": "evidence/planning/epistemic_overlay_plan.md",
        "claims": dict(sorted(overlay.items())),
    }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, sort_keys=False)
        f.write("\n")

    print(f"Written {len(overlay)} claims -> {OUTPUT_JSON}")
    print(f"  emergent_from claims: {len(emergent_map)}")
    print(f"  alarms: unsupported_foundation={n_unsupported} "
          f"untested_foundation={n_untested}")
    print(f"  posterior_gate disagreements vs heuristic: {n_gate_disagree}")
    print(f"  MRF graph: {len(node_ids)} nodes, {n_depends_edges} depends_on + "
          f"{n_coupled_edges} coupled_with + {n_emergent_edges} emergent_from edges")
    print(f"  BP exp: converged={exp_report['converged']} iters={exp_report['iterations']} "
          f"max_delta={exp_report['final_max_delta']} oscillating={exp_report['oscillating']} "
          f"beliefs_moved={n_moved_exp}")
    print(f"  BP lit: converged={lit_report['converged']} iters={lit_report['iterations']} "
          f"max_delta={lit_report['final_max_delta']} oscillating={lit_report['oscillating']} "
          f"beliefs_moved={n_moved_lit}")
    print(f"  calibration: {out['calibration']}")


if __name__ == "__main__":
    main()
