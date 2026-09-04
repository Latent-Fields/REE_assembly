# Claim-graph edge-type split: `depends_on` DAG + `coupled_with` (GOV-EDGE-1)

**Date:** 2026-09-04
**Claim:** GOV-EDGE-1 (`docs/claims/claims.yaml`, status `candidate`)
**Tool:** `scripts/split_claim_edge_types.py` (idempotent; `--dry-run` / `--apply --audit-json`)
**Audit of every moved edge:** `claims_edge_type_split_20260904.json` (same directory)
**Enforcement:** `scripts/validate_claims.py::validate_edge_types` -- a `depends_on` cycle is an ERROR (blocks `governance.sh --strict`); `coupled_with` hygiene is WARN.

## 1. The question that started it

"Should the claims matrix be a DAG, and does circular reasoning mean it needs work?"

Half right. The registry's own design note (IMPL-018 in `docs/claims/claim_index.md`) already said `depends_on` "must stay acyclic; runtime feedback loops are documented in architecture flow specs". But `scripts/validate_claims.py` had been amended on 2026-09-01 to say the opposite: the graph "is a conceptual dependency web, not a build DAG", cycles are tolerated, and "this would introduce a cycle" must not be used as an objection. The epistemic overlay went further and treated `depends_on` as an undirected weak coupling. Two authoritative artefacts, opposite intent.

The cycles were **not** circular reasoning in the evidential sense: support attaches per claim from experiment manifests, and the only propagation step (the overlay's loopy BP) is symmetric and weak, so no cycle could bootstrap A's confidence from B's and B's from A's. The real cost was that **one field carried three meanings** -- directed prerequisite, undirected architectural coupling, mutual explanation -- and while it did, the one meaning with an enforceable invariant (prerequisite => acyclic) could not be enforced anywhere.

## 2. Measured state before the split

| measure | value |
|---|---|
| claims | 1100 |
| `depends_on` edges | 4012 |
| cyclic strongly-connected components | 25 |
| claims inside a cycle | 262 (24%) |
| largest cycle cluster | 197 claims, 710 internal edges, 61 mutual pairs (114 MECH / 31 ARC / 29 SD / 17 INV / 5 Q / 1 IMPL) |
| `emergent_from` edges | 79, already acyclic |
| self-loops | 0 |
| dangling `depends_on` targets | 0 |

Representative cycles: ARC-007 <-> ARC-018 (hippocampus stores/replays vs generates rollouts: mutually constitutive); MECH-302 / MECH-303 / MECH-304 (relief-completion, context safety, cue safety: mutual explanation); GOV-ANALOGY-1 / GOV-HELDOUT-1 / GOV-STRAT-1 (governance rules citing each other); ARC-021 -> Q-019 (an architecture claim "depending on" an open question).

## 3. The mechanical rule

Two rules, in order. Neither ever moves an `emergent_from` edge (directional by definition; `validate_invariant` keeps it a subset of `depends_on`).

1. **Mutual pair.** A `depends_on` B and B `depends_on` A: neither can be a prerequisite of the other, so both directions move to `coupled_with`. Unambiguous. If one direction is `emergent_from`, only the other moves, and the pair is then a legitimate mixed shape (prerequisite one way, coupling the other) that the validator accepts.
2. **Residual feedback arc set.** For the cycles that survive rule 1, repeatedly find one cycle and move ONE edge, chosen by a cost that prefers (a) the edge running **down** the abstraction ladder (ARC/SD/INV -> MECH/Q: the direction a prerequisite does not normally run), then (b) the edge whose source has the most out-edges (least specific), then (c) lexical order for determinism. Heuristic. Every such edge carries the inline comment `cycle-break; re-judge (cycle ...)`.

`coupled_with` is written **symmetric**: for a cycle-break edge A -> B, A gets `coupled_with: [B]` and B gets `coupled_with: [A]` with a `reverse of ...` comment.

The edit is **text-level** (claims.yaml carries ~2500 inline comments a `yaml.dump` would destroy). Before writing, the script re-parses its output and asserts that for every claim every field other than `depends_on`/`coupled_with` is unchanged, that `depends_on` equals the old list minus exactly the planned removals, that `coupled_with` equals exactly the planned additions, and that `depends_on` is now acyclic. It refuses to write otherwise.

## 4. What moved

| | count |
|---|---|
| edges moved out of `depends_on` | 193 |
| of which mutual-pair (rule 1) | 185 |
| of which cycle-break (rule 2) | 8 |
| `depends_on` edges after | 3819 (acyclic; 3822 once GOV-EDGE-1's own three edges are added) |
| distinct `coupled_with` pairs | 102 (99 pure coupling + 3 mixed pairs where the reverse direction is an `emergent_from` prerequisite: ARC-046/INV-055, MECH-413/INV-082, MECH-414/INV-082) |
| claims with a `coupled_with` field | 138 |

**The 8 cycle-break edges, owed a human re-judgement** (each is an architecture/substrate claim depending on a mechanism, question, or invariant it gives rise to):

| moved edge | cycle it broke |
|---|---|
| ARC-003 -> INV-012 | ARC-003 -> INV-012 -> MECH-095 -> ARC-021 -> Q-019 -> MECH-057a -> ARC-003 |
| ARC-017 -> INV-012 | (second pass through the same INV-012 / MECH-095 chain) |
| ARC-015 -> MECH-095 | ARC-015 -> MECH-095 -> ARC-021 -> Q-019 -> MECH-057a -> ARC-015 |
| ARC-021 -> Q-019 | ARC-021 -> Q-019 -> MECH-057a -> ARC-023 -> ARC-021 |
| SD-026 -> INV-034 | SD-026 / INV-034 / SD-012 / SD-014 chain |
| ARC-036 -> MECH-030 | ARC-036 / MECH-030 / MECH-092 / MECH-124 sleep-consolidation chain |
| ARC-036 -> MECH-124 | same cluster |
| SD-014 -> MECH-030 | same cluster |

Exact cycles for each are in the JSON audit under `moves[].cycle`. To swap which edge of a cycle is the coupled one: move the chosen edge back to `depends_on` on its source, move the alternative edge to `coupled_with` on both endpoints, run `validate_claims.py --strict`.

## 5. Consumers checked

| consumer | reads | effect of the split |
|---|---|---|
| `scripts/build_epistemic_overlay.py` | `depends_on`, `emergent_from` | Now also reads `coupled_with`, with the identical weak symmetric potential. Overlay output **byte-identical in every belief** before vs after (only the `mrf.graph` edge counters differ: 3839 `depends_on` before = 3740 `depends_on` + 99 `coupled_with` after). |
| `scripts/check_claim_phase_consistency.py` (phase provenance) | `depends_on` as a prerequisite walk | Ignores `coupled_with` by design (it propagates no phase pressure). Its per-seed `visited` cycle guard is now defence in depth. Documented in `docs/architecture/claim_phase_provenance.md` 3.2/3.3. |
| `scripts/validate_claims.py` | both | New `validate_edge_types`: cycle = ERROR, coupling hygiene = WARN. Stale "not acyclic and not meant to be" hint text replaced. |
| `scripts/build_claim_dependency_process.py` | `depends_on` | Unchanged. Its cycle taxonomy (`accepted_reciprocal_architecture`, `semantic_explanation_cycle`, `co_definition_module_function`, `edge_type_cleanup_candidate`) now finds zero cyclic components; those categories are the natural labels to carry onto `coupled_with` pairs in a follow-on. |
| `serve.py`, `scripts/export_public_explorer.py` | `depends_on` | Unchanged: `coupled_with` is not rendered in the explorer yet. Follow-on. |
| `docs/claims/claim_index.md` (IMPL-018), `docs/architecture/invariant_types.md`, `claims.yaml` header schema | prose | Reconciled to the two-layer model. |

## 6. GOV-HELDOUT-1 record

Manual check of the new rule against cases it was not written from. Only cases where the old wordings and the new rule give **different** calls count.

| case | IMPL-018 wording ("must be acyclic") | 2026-09-01 validator wording ("cycles tolerated") | GOV-EDGE-1 |
|---|---|---|---|
| (a) SD-013 -> SD-003 repoint objection, 2026-09-01 | refuse the repoint (cycle-closing) | permit it (harmless) | a cycle-closing repoint is evidence the pair is coupling -> `coupled_with`; separately, a provenance mention is not a prerequisite, so drop. Same drop the session made, by a route that also refuses "cycles are fine". |
| (b) ARC-007 <-> ARC-018 | delete one edge (loses real coupling) | keep the cycle | both edges to `coupled_with`, DAG restored, information kept |
| (c) ARC-021 -> Q-019 | bare defect | tolerated | `coupled_with` (a question cannot be a prerequisite of an architecture claim) |
| (d) GOV-ANALOGY-1 / HELDOUT-1 / STRAT-1 triangle | defect | tolerated | `coupled_with` |
| negative control: INV `emergent_from` SD | prerequisite | prerequisite | prerequisite -- identical under all three, so **not counted** |

Outcome: **passed cleanly**, no narrowing needed. The check did surface that the 2026-09-01 comment had over-corrected from "one cycle is disqualifying" to "no cycle is", the over-broad form GOV-HELDOUT-1 exists to catch.

## 7. Deliberately not done

- **No third, DAG-checked `supports` layer.** Circular reasoning in prose (an autopsy citing MECH-303 as active to argue for MECH-304, where 303 was argued from 304) is not caught by this split. A support edge would be the tool for it. That is a separate decision with its own consumers; introducing it here would widen the change past what was asked.
- **No re-weighting of `coupled_with` in the overlay.** The parity check above is the reason: the split must not silently move beliefs. Weighting the layers differently is a modelling decision for the overlay plan, not a side effect of a schema split.
- **No hand re-judgement of the 8 cycle-break edges.** They are tagged and listed for governance.
