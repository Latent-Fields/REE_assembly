---
nav_exclude: true
status: candidate/v3_pending
status_asof: 2026-09-01
status_claim: MECH-317
---

# MECH-317 Absorption Check

**Date:** 2026-09-01
**Status:** complete
**Verdict:** **(B) Partially absorbed — the compression MECHANISM absorbs into ARC-071/MECH-323/MECH-324; the behavioural-boundary DEPENDENT VARIABLE does not, and no instrument for it exists anywhere in the substrate.**
**Authoring context:** Commissioned by node `arc_062_rule_apprehension:GAP-I-absorption` (`unblocks_claims: [MECH-316, MECH-317]`), which has owed this check since it was un-deferred on 2026-08-18 and whose own adjudication note records that the memo half is *"`complicated (buildable)` right now — the absorption-check memo needs no substrate at all, only the MECH-318 template applied to two siblings."* Directly answers GFLAG-0066 and GFLAG-0087; bears on GFLAG-0084. Session `mech317-absorption-20260901`. **This memo produces a verdict; it applies no disposition.** MECH-316's half of the node is out of scope for this pass, exactly as the MECH-318 check scoped out its own siblings.

---

## Question

Does the already-built ARC-071 / MECH-323 (`ChunkAccumulator`) / MECH-324 (`ChunkLibrary`) cluster already implement the behavioural-pattern compression MECH-317 names (Smith & Graybiel 2013/2016 DLS sequence consolidation; Sutton, Precup & Singh 1999 options; Bacon, Harb & Precup 2017 option-critic)? Or does MECH-317 assert something the built cluster does not?

Three independent passes have converged on "duplicate": proposal **EXP-0263/EVB-0227** was gated 2026-08-02 with a `gating_reason` recommending `superseded_by ARC-071/MECH-323/MECH-324`; **GFLAG-0066** (2026-08-27) reached the same conclusion by the same reasoning without citing it; **GFLAG-0087** (2026-08-28) extended it with two residuals. This memo tests that convergence property-by-property rather than by family resemblance.

---

## Sutton 1999 / Smith & Graybiel specification

The five load-bearing properties of MECH-317, taken from its own `functional_restatement` and its literature anchors:

| # | Property | What the claim/literature requires |
|---|---|---|
| S1 | Options triple | An option is a temporally-extended action with an **initiation set**, a **policy**, and a **termination condition** (Sutton, Precup & Singh 1999). |
| S2 | Compressibility trigger | The mechanism **detects which behavioural patterns are compressible** — repeated across many instances — rather than compressing indiscriminately. |
| S3 | Reusable-unit creation | The compressed sequence becomes a **single reusable unit** at the level of the representation (Smith & Graybiel: DLS start–stop bracketing of a sequence into one striatal unit). |
| S4 | Temporally-extended selection | The resulting unit **supports temporally-extended action selection** — it is selectable atomically, its sub-elements no longer independently chosen. |
| S5 | Boundary detectability in the action stream | **The claim's own falsifier:** MECH-317-ON agents produce stereotyped chunks *"with chunk boundaries detectable in action-distribution entropy troughs"*; MECH-317-OFF agents produce unchunked streams without boundaries. |

S1–S4 are the *mechanism*. **S5 is the dependent variable** — the observable by which the claim was registered to be falsified. The distinction is the whole content of this memo.

---

## Candidate 1 — MECH-323 `ChunkAccumulator` (`ree-v3/ree_core/policy/policy_chunking.py`)

| Property | Verdict | Evidence |
|---|---|---|
| S1 options triple | **YES** | `ChunkedPrimitive` carries `initiation_set: frozenset` and `termination_condition: str` as first-class fields (`policy_chunking.py:513-514`), with the docstring at `:464-465` stating explicitly that *"The Sutton 1999 options structure (R4) requires initiation_set and termination_condition as first-class fields: a macro selected atomically…"*. Same formalism, same citation. |
| S2 compressibility trigger | **YES** | `record_step` accumulates sequences (`:1059`); `note_outcome` supplies outcome consistency (`:1087`); `formation_candidates` (`:1139`) selects on repetition-count **and** outcome-consistency. This is the trigger design MECH-317 describes, independently re-derived. |
| S3 reusable-unit creation | **YES** | `mint()` (`:1261`) constructs the `ChunkedPrimitive`; `ChunkLibrary.register` (`:1447`) makes it a persistent addressable unit. |
| S4 temporally-extended selection | **YES, flag-gated** | `use_chunk_proposal_injection` (`config.py:2263`, default False) injects chunks into the proposal pool at `hippocampal/module.py:2393`; `ChunkedPrimitive.is_selectable` (`:535`) gates atomic selectability. |
| S5 boundary DV | **NO** | Nothing in this module emits a boundary statistic. Its DVs are library counters — `crystallisation_counter` (`:521`), `n_reacquisitions` (`:525`), formation counts. |

**Subtotal:** the formation mechanism absorbs completely. `policy_chunking.py` never references MECH-317, ARC-064 or MECH-318 — it re-derived the same mechanism under a different architectural parent (ARC-069 dynamic regranularisation, not ARC-064 bottom-up rule discovery). Convergent derivation is *stronger* evidence of duplication than shared lineage would be.

---

## Candidate 2 — MECH-324 `ChunkLibrary` maintenance (`policy_chunking.py:1416+`)

| Property | Verdict | Evidence |
|---|---|---|
| S3 persistence of the reusable unit | **YES, and beyond MECH-317's ask** | `note_real_execution` (`:1499`), `tick_maintenance` (`:1651`), `_mark_dissolved` (`:1570`), `revive` (`:1598`), `dormant_chunks` (`:1585`). MECH-317 asserts creation; MECH-324 adds crystallisation, dissolution and reacquisition — the IL/vmPFC-analog half Smith & Graybiel 2013's optogenetic result requires and which MECH-317 does **not** name. |
| S5 boundary DV | **NO** | Same as above. |

**Subtotal:** MECH-324 covers more of the Smith & Graybiel biology than MECH-317 does. On the *mechanism* axis MECH-317 is a proper subset of the built cluster.

---

## Candidate 3 — the near-miss: `first_action_entropy` (`hippocampal/module.py:757`)

Recorded because a future session searching for "action entropy" will find this and could reasonably conclude S5's instrument already exists. **It does not.**

`first_action_entropy` (`module.py:757`, via `_entropy_from_counts(first_counts)`) is the entropy of the distribution over the **first action class of a candidate proposal pool at a single decision point**. It is a *diversity* statistic over proposals, consumed by the support-preserving injection path (`:1455`, `:1532`) and the CEM refit (`:2222`).

S5 requires entropy **over the executed action stream, across time**, so that a *trough* localises a chunk boundary. Those are different objects: one is spatial-over-candidates at one tick, the other temporal-over-actions across many. No transformation of the former yields the latter.

Exhaustive search for the real instrument across `ree_core/` returns nothing: `entropy_trough`, `chunk_boundary`, `action_distribution_entropy`, `boundary_detect`, `boundary_readout` — **zero hits each**.

| Property | Verdict | Evidence |
|---|---|---|
| S5 boundary DV | **NOT ABSORBED** | No action-stream boundary readout exists anywhere in the substrate. MECH-317's own `evidence_quality_note` already concedes this: *"Falsifying experiments are SD-054-tractable but require new instrumentation (action-chunk boundary detection); EXQ design deferred."* |

---

## Verdict (B) — Partially absorbed

| Property | Absorbed by | Notes |
|---|---|---|
| S1 options triple | MECH-323 `ChunkedPrimitive` | Same Sutton 1999 formalism, cited in the module's own docstring. |
| S2 compressibility trigger | MECH-323 `formation_candidates` | Repetition-count + outcome-consistency, independently re-derived. |
| S3 reusable-unit creation | MECH-323 `mint` + MECH-324 `ChunkLibrary` | The built cluster exceeds MECH-317 here (dissolution/reacquisition). |
| S4 temporally-extended selection | `use_chunk_proposal_injection` → `module.py:2393` | Flag-gated, default OFF, byte-identical when off. |
| S5 boundary DV in the action stream | **NOT ABSORBED** | No instrument exists. The only similarly-named statistic measures a different object (Candidate 3). |

**The mechanism absorbs. The dependent variable does not.** That asymmetry is the finding, and it is what separates this from a clean supersede.

### Why full supersede is not warranted on the present evidence

The case for full supersede rests on absorbing into a *validated survivor*. The evidence tree does not support that description:

| claim | `genuine_exp_count` | `exp_conf` | quadrant |
|---|---|---|---|
| MECH-317 (proposed absorbed) | 0 | 0.0 | `plausible_unproven` |
| **ARC-071 (proposed survivor)** | **0** | **0.0** | **`plausible_unproven`** |
| MECH-323 | 2 | 0.746 | `confirmed_established` |
| MECH-324 | 2 | 0.744 | `confirmed_established` |

ARC-071 sits in **the same quadrant as the claim it would absorb**. The evidence-tree discriminator that decided the 2026-08-15 orphan-claim adjudication — the sharpest tool this registry has for merge questions — **does not separate them at parent level**. All six of ARC-071's experimental entries are scoring-excluded diagnostics, and the V3-EXQ-810a autopsy states plainly that *"ARC-071's behavioural-benefit clause remains untested."*

Separation exists only at the children, and it is thinner than it looks:

- **V3-EXQ-829** is a scored, non-degenerate `experiment_purpose: evidence` **FAIL with no `failure_autopsy` artifact** — verified by exhaustive search across 2,576 autopsy files.
- **V3-EXQ-829a**'s PASS is **degenerate on its load-bearing criterion**: `interpretation.criteria_non_degenerate.C2 = False`, with `all_iso_on_cells_sit_on_forced_bar: true` and ρ = 0.9999999999999998. With the window contamination removed, `r_reacq` lands exactly on `ceil(R_min · f_reacq)` in every cell — ρ = 1.0 is an arithmetic identity, not a measurement. Note that the run's **top-level `non_degenerate` reads `True`**, so the run-level gate reports clean over a degenerate verdict criterion. What 829a establishes is that the *instrument* now works, not anything empirical about MECH-324's prediction.

So the honest description is not "absorb an untested claim into a validated one" but **"absorb an untested behavioural claim into an untested behavioural claim that happens to have code."** That is still a defensible merge on mechanism grounds — but it does not license discarding the DV.

### Two consumer edges a full supersede would orphan

Verified: no claim in the ARC-071 family mentions rule-state abstraction or practice-maturity weighting anywhere in its record.

- **MECH-318** (`depends_on: [ARC-064, ARC-065, MECH-316, MECH-317]`) — rule-state abstraction. MECH-317 is its compression input under ARC-064.
- **MECH-312b** (`depends_on: [MECH-312, MECH-317]`) — practice-maturity weighting. **Named in no flag's `claim_ids`**, so a disposition applied from GFLAG-0066/0087's claim lists alone would orphan it silently.

---

## Recommended disposition (for governance to apply, not applied here)

**Partial absorption with a named residual**, mirroring the MECH-318 check's own verdict (B) — the in-house precedent for exactly this shape:

1. Absorb **mechanism-identity** (S1–S4) into ARC-071 / MECH-323 / MECH-324. Record it on MECH-317 rather than deleting the claim.
2. Retain **MECH-317 narrowly as the behavioural-readout claim** (S5), `epistemic_category: substrate_conditional`, falsifier reused verbatim.
3. Name the **instrument debt on ARC-071 LEG 3** *and* register it as its own `substrate_queue` entry — not prose alone. Carrying a gap only in a claim's narrative is the failure mode GFLAG-0083 documents (ARC-071's live text still names a superseded `sd_id`).
4. Re-point **MECH-318 and MECH-312b** — both, explicitly — with a note that neither rule-state abstraction nor practice-maturity weighting is asserted by the ARC-071 family.
5. Ratify or overturn **EXP-0263**'s 2026-08-02 recommendation explicitly, so the proposal stops sitting gated on an unratified rationale.

**What would justify full supersede instead:** if `initiation_set` / `termination_condition` plus a chunk-execution timing readout can express the entropy-trough DV without new instrumentation. This memo did not find such a path, but it is a substrate-design question, not a registry one, and a build session may see one.

---

## Separable, and better lifted out than cycled with the merge

GFLAG-0084 bundles three items with the merge question that are independent of it and settleable on their own:

- **V3-EXQ-829's missing autopsy** — a `/failure-autopsy` routing question. The mechanism is already diagnosed and source-cited in the queue entry's `implementation_hint`, so the autopsy is largely transcription.
- **The `SD-083` id collision.** `claims.yaml` `SD-083` is `consolidation.offline_policy_consolidation_window`; `substrate_queue.json` `sd_id: "SD-083"` is the MECH-324 reacquisition read. The queue reserved the id two days before the registry issued it elsewhere, and `v4_prerequisite_cut_20260901.md` already reads it through the wrong lens. **Any action on "SD-083" without disambiguation hits the wrong object.** Separately, the entry's `DO_NOT_BUILD_YET` gate is obsolete: the build it guards (`use_reacquisition_window_isolation`) landed ree-v3 `7747a01` on 2026-07-31 with contract tests and a design doc.
- **V3-EXQ-834's unmeasured growable-ceiling prediction** — needs its level constraint re-derived before anything is queued (its successor proposal still mandates operator-level on a premise V3-EXQ-810a closed).

---

## What this memo does NOT do

- It does **not** change any claim's `status`, `epistemic_category`, `v3_pending` or `depends_on`. No disposition is applied.
- It does **not** adjudicate MECH-316's half of the GAP-I-absorption node.
- It does **not** commission substrate. The instrument debt in recommendation 3 is a registration, not a build authorisation.
- It does **not** resolve GFLAG-0066 / 0084 / 0087. It supplies the verdict those flags were waiting on.

---

## Cross-references

- Template and precedent verdict: `docs/architecture/mech_318_absorption_check.md`
- Substrate: `ree-v3/ree_core/policy/policy_chunking.py`; injection at `ree-v3/ree_core/hippocampal/module.py:2393`
- Commissioning node: `evidence/planning/arc_062_rule_apprehension_plan.md` → `arc_062_rule_apprehension:GAP-I-absorption`
- Prior unratified adjudication: `evidence/planning/experiment_proposals.v1.json` → EXP-0263 / EVB-0227
- Flags answered: GFLAG-0066, GFLAG-0087; bears on GFLAG-0084, GFLAG-0083
- Triage context: `evidence/planning/governance_flag_triage_20260901.md` Part 2
