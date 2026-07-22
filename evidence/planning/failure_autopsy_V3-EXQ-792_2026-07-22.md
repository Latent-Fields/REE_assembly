# Failure autopsy — V3-EXQ-792 (MECH-457 retention consolidation)

**Scope:** single. **Status:** confirmed (user-adjudicated 2026-07-22).
**Generated:** 2026-07-22T03:48:30Z. **Promotes and demotes nothing.**

Run: `v3_exq_792_mech457_retention_consolidation_20260720T234440Z_v3` ·
claims `[MECH-457]` · purpose `diagnostic` · outcome **FAIL** ·
`evidence_direction: unknown` · self-route `retention_grid_nondiscriminative`.
Leg `H-retention-consolidation` of the `competence_floor` GOV-FANOUT-1 portfolio.

---

## 1. Facts

Recording complete (`rec/v1`, `substrate_hash`, `config`, `seeds [42,43,44]`,
`substrate_stable_across_run`). **No recording debt.** 22 preconditions, **all met** —
the BC install took on every arm (worst cell 17.75 vs a 1.0 floor), both achievability
anchors clear (local_view_greedy 48.05, oracle 57.2).

| Arm | `kl_anchor_coef` | `retained_fraction` | margin over unconstrained | realised mean KL |
|---|---|---|---|---|
| `retcons_unconstrained` | — | 0.525 | — | 0.0 (sentinel) |
| `retcons_kl0p03` | 0.03 | **0.871** | +0.346 | 0.868 |
| `retcons_kl0p10` | 0.10 | 0.389 | −0.136 | **1.143** |
| `retcons_kl0p30` | 0.30 | **0.778** | +0.252 | **0.278** |

**The load-bearing criterion PASSED.**
`C_anchored_arm_consolidates_installed_competence` — `retcons_kl0p30` holds a strict
majority of seeds at `retained_fraction >= 0.5`, beats the unconstrained arm by
**0.252** (margin 0.15), and **kept its plasticity** (realised KL 0.278 > 0.001; peak
above 1.05× install). It is scored `consolidates: true, frozen: false`. The
`headline.consolidation_protects_installed_competence` flag is **true**.

**What failed is a non-load-bearing leg**: `C_anchor_bound_dose_response`
(`load_bearing: false`) — realised KL is not monotone in the coefficient (0.868 →
1.143 → 0.278). `criteria_non_degenerate.anchor_bound_dose_response: false`. The
manifest's grid treats a failed dose-response as vacating the read, hence
`retention_grid_nondiscriminative`.

The 0.10 arm is the sole non-monotone point and is anomalous on **both** axes at once
— highest realised KL *and* lowest retention, i.e. the anchor failed to bind there.
At n=3 seeds that is one cell's worth of evidence.

---

## 2. Claim-layer mapping

MECH-457 (`candidate`, `v3_pending`, `implementation_phase v3`). The run is
`diagnostic` and tags MECH-457 with direction `unknown`; it weights nothing either
way. The manipulation is the **update constraint only** — the value estimator is
untouched (`use_distributional_critic False` on every arm) and the auxiliary is a
constant 0.5, which is what keeps this leg disjoint from V3-EXQ-789
(`H-retention-auxiliary-decay`, eliminated) and V3-EXQ-788 (`H-retention-critic`).
The claim was tested under conditions where it could express itself.

---

## 3. Biological-reference triage

**Closest mechanism:** synaptic consolidation / systems consolidation — a trust-region
constraint to a prior policy snapshot is a direct translation of *synaptic tagging and
capture* plus the protein-synthesis-dependent stabilisation window that protects a
recently-acquired trace from subsequent interference. Dependencies in real brains:
sleep-dependent replay, a consolidation signal that is *not* the reward signal, and
selective (not global) protection.

**Formal-definition import?** Partly. The KL trust region is a formal (Kullback–Leibler)
object; the biological consolidation mechanism is **selective and trace-specific**,
whereas a policy-wide KL anchor is **global and undifferentiated**. That divergence is
load-bearing and should be recorded: the biology predicts that *which* traces are
protected is itself learned, and a global coefficient cannot express that. It is not,
however, what caused this run's non-discrimination.

**Does the failure resemble a missing dependency?** No. The dependency (an installed
prior worth protecting) was present and verified on every arm. This is a statistical
result, not a dependency discovery.

**Lit status:** no `targeted_review_mech_457_consolidation` entry on file. A `/lit-pull`
on trace-specific vs global consolidation would sharpen the next iteration's design —
recorded as secondary, not the primary routing.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | Fair test; the constraint isolates the update and nothing else. |
| Biological reference | **partial** | Consolidation is well-evidenced; the *global* KL anchor diverges from trace-selective biology (recorded, not causal here). |
| Prerequisites | **present** | Install took on every arm (17.75 worst cell vs 1.0 floor); both achievability anchors clear. |
| Implementation completeness | **complete** | `SD-MECH457-POLICY-KL-ANCHOR` landed and demonstrably binds at coef 0.30 (KL 0.278 vs unconstrained). |
| Environment adequacy | **adequate** | D3, oracle 57.2, local-view 48.05. |
| Measurement adequacy | **under-instrumented — DOMINANT LAYER** | The dose-response proof is the only evidence that the anchor *bound*, because the control's KL is a hard-coded 0.0 sentinel rather than a measured drift. With n=3 and no measured control drift, a single anomalous coefficient vacates the whole grid. |
| Integration adequacy | coupled | — |
| Scale / capacity | **likely insufficient (statistical)** | n=3 seeds × 3 coefficients. |

**Recommended `epistemic_category`: `measurement_test_design_defect`** — specifically
**under-powered, with a structurally weak control**. Not `substrate_ceiling`.

---

## 5. Learning extracted

1. **A consolidation pathway for an acquired policy is CONSTRUCTIBLE and was
   constructed.** `retcons_kl0p30` retains 0.778 of installed competence against the
   unconstrained arm's 0.525, while remaining plastic. Whatever MECH-457 turns out to
   be, "there is no protection pathway" is not it. This is a **positive** result inside
   a FAIL and must not be lost.
2. **The control's `mean_policy_kl_to_anchor_recent` is a 0.0 sentinel, not a
   measurement.** That is why the dose-response had to carry the entire burden of
   proving the anchor bound — and why one anomalous cell could vacate a passing
   load-bearing criterion. **Fix the control before adding seeds:** measure the
   unconstrained arm's actual drift from the same frozen snapshot. Then "the anchor
   bound" is provable per-arm against a real comparator and does not depend on
   monotonicity across coefficients at all.
3. **A non-load-bearing criterion vacated a load-bearing PASS.** Worth a design rule:
   when a `load_bearing: false` leg can flip the overall label, it is load-bearing in
   fact. Either promote it or stop letting it gate.
4. **Recording debt: none.** Per-arm realised KL, per-arm retained fraction, per-arm
   plasticity flags and the reference band were all recorded. The trajectory probe
   (`mech457_retention_trajectory_probe`, ree-v3 `7e4f6e9`) did its job.

---

## 6. Repair pathway

**Node classification:** `complex (probe-gated) / puzzle (known rules)` — the frame is
right, the design is right, a fact is missing and one more measurement gets it.

**Re-derive brake:** MECH-457 = **0** confirmed `substrate_ceiling` hits under the
R1–R3 convention (19 autopsy targets). **Does not fire.** This autopsy adds no ceiling
reading.

**Granularity-debt recurrence:** fires for MECH-457 (see the cluster autopsy
`failure_autopsy_competence-objective-cluster-734-737b-742a_2026-07-22`); the
`/claim-synthesis` recommendation is raised once there, not duplicated here.

**Routing: `/queue-experiment` — same-question re-run, alphabetic suffix (792a).**
Two changes, both cheap:
1. **Measure the control's drift.** Replace the 0.0 sentinel with the unconstrained
   arm's realised mean KL to the same frozen post-install snapshot, so each anchored
   arm is provable against a real comparator.
2. **Raise n.** 3 → at least 6 seeds, and keep the three coefficients. With (1) in
   place, monotonicity across coefficients becomes a *secondary* check rather than the
   only proof the anchor bound.

Nothing in the substrate needs building: `recommended_substrate_queue_entry.action =
"none"`. Do **not** route this to `/implement-substrate`.

Secondary: a `/lit-pull` commission on **trace-selective vs global consolidation**
(`targeted_review_mech_457_consolidation`), to inform whether the next generation of
the anchor should be per-trace rather than a single global coefficient.

### Draft `evidence_quality_note` (governance to write — do not apply here)

> 2026-07-22 (V3-EXQ-792, diagnostic, claim_ids=[MECH-457], direction `unknown` —
> weights nothing; failure_autopsy_V3-EXQ-792_2026-07-22). The `H-retention-consolidation`
> leg is **not** refuted and stays alive. Its load-bearing criterion PASSED:
> `retcons_kl0p30` retained 0.778 of installed competence vs the unconstrained arm's
> 0.525 (margin +0.252 against a 0.15 bar) while keeping plasticity (realised KL 0.278;
> peak above 1.05× install), scored `consolidates: true, frozen: false`. A consolidation
> pathway for an acquired policy is therefore CONSTRUCTIBLE. The overall FAIL rests on
> a `load_bearing: false` dose-response leg: realised KL is non-monotone in the
> coefficient (0.868 / 1.143 / 0.278) because the 0.10 arm's anchor did not bind, and
> at n=3 with the control's KL hard-coded to a 0.0 sentinel that single cell vacates
> the grid. Under-powered with a structurally weak control, not a substrate ceiling.
> Re-run as 792a with a measured control drift and >= 6 seeds. MECH-457 stays
> `candidate` / `v3_pending`.

---

## 7. Frozen-ledger delta (Step 9b)

Question **`competence_floor`** (hero, `MECH-457` + `INV-088`), leg
**`H-retention-consolidation`**: stays **`alive`**. Record
`resolving_runs: ["V3-EXQ-792"]`, `evidence_direction: "unknown"`,
`epistemic_category: "measurement_test_design_defect"`,
`self_route_label: "retention_grid_nondiscriminative"`, `control_passed: true`
(every readiness anchor and the install-took precondition cleared),
`non_degenerate: false` (the manifest's own
`criteria_non_degenerate.anchor_bound_dose_response`), `met_elimination_bar: false`.

Per the Step 9b state-mapping table this is the "does not discriminate /
`non_degenerate: false`" row: **leave `alive`, record the run and the basis, move no
state.** No growth event; `initial_frozen_count` unchanged at 16.

## 8. Confirmed routing (user-adjudicated 2026-07-22)

User selected **"Re-power, keep leg alive"** over resolving the leg as `confirmed` on
the load-bearing PASS.
