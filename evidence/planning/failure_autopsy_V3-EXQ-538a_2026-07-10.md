# Failure Autopsy -- V3-EXQ-538a (SD-049 Phase-2 reef behavioural validation, sleep-on ablation)

- **generated_utc:** 2026-07-10T06:33:30Z
- **run_id:** `v3_exq_538a_sd049_phase2_with_sleep_20260710T035148Z_v3`
- **queue_id:** V3-EXQ-538a
- **claim_ids:** SD-049, SD-015, SD-017, MECH-229, MECH-230
- **experiment_purpose:** evidence
- **outcome:** FAIL (self-declared `evidence_direction=weakens`)
- **supersedes:** V3-EXQ-538 (infra-ERROR / SIGTERM on cloud-1, not a scientific result)
- **supersedes_diagnostic:** V3-EXQ-514f
- **scope:** single (but read against the SD-049 cluster; re-derive brake fires)
- **status:** confirmed (interactive; user adjudicated 2026-07-10)

---

## 1. Facts (no interpretation)

538a took the **514f "canonical fail-to-discriminate" reef config** verbatim -- 3-type SD-049,
`classifier_loss_weight=0.1` (unchanged "to isolate the sleep axis"), reef ON,
`hazard_food_attraction=0.7`, 10x10 grid, 3 seeds x 3 arms -- and added a **sleep axis**:

| Arm | config | neigh probe (mean) | cons probe (mean) | sws / rem writes | classifier updates / seed |
|---|---|---|---|---|---|
| ARM_0_off | sws=F rem=F loop=F | 0.517 | 0.286 | 0 / 0 | 29-48 |
| ARM_1_sd017_only | sws=T rem=T loop=F (manual) | 0.443 | 0.433 | 160 / 160 | 32-35 |
| ARM_2_phase_a | sws=T rem=T loop=T K=3 | 0.516 | 0.139 | 40 / 40 | 24-57 |

**Pre-registered acceptance:** PASS = C0 AND C1a AND C1b AND C2a AND C2b AND (C3a OR C3b) AND C4.

**Binding failure = C4 alone.** C0/C1a/C1b/C2a/C2b all PASS (substrate liveness). C3b passed as a
noise-dominated OR, so `(C3a OR C3b)` = true. The sole gate that fails:

- **C4 (sleep lift on the neighborhood probe >= 0.10):** `max(0.443, 0.516) - 0.517 = -0.001`. FAIL.
- (C3a, neighborhood probe >= 0.60, also false: 0.443 / 0.516 both < 0.60.)

The neighborhood probe is the **well-powered** metric (~9,000 pooled samples). The consumption
probe (n_identity_samples_consumption 45-72 total) is a **secondary readout, not in the pass
criteria**. Its non-monotone spread (0.286 / 0.433 / 0.139, chance ~0.33 for 3 types) is pure
small-sample noise (10-33 samples/seed).

**Failed criterion type: discrimination (C4 sleep-lift) -- but see Section 5, the discrimination
metric is starved.**

### Two substrate defects in the reconstruction

1. **Consumption/identity starvation.** The identity classifier only updates on consumption ticks
   (`id_loss > 0`): **~30-50 gradient updates over 9,000 steps (~0.4% of steps)**, across 3
   classes, on *every* seed regardless of run length. The waking pass never encodes
   consumption-identity. This is the **identical signature** recorded in
   `failure_autopsy_V3-EXQ-514l` ("~0.2% consumption rate, 23 vs 818 neighborhood samples").
2. **Seed 44 is a degenerate / truncated run.** prox updates 1,088-1,364 vs 9,000 for seeds 42/43
   (episodes dying at ~step 40), peak per-axis drive ~0.11 vs 0.45, neighborhood samples ~470 vs
   4,500. It pollutes every aggregate; the "well-powered" neighborhood probe is effectively 2
   usable seeds.

---

## 2. Claim-layer map

| Claim | type / status | epistemic_category | note |
|---|---|---|---|
| SD-049 | design_decision / candidate, v3_pending | substrate_ceiling | Phase-2 behavioural deliverable NOT met across 514l/693/693a; foraging-competence ceiling. |
| SD-015 | design_decision / candidate | substrate_ceiling | z_resource discriminability; 693 showed identity probe 0.71-0.77 when the *harness works*. |
| SD-017 | design_decision / **stable** | (n/a) | Already has a genuine support (V3-EXQ-691). Sleep substrate implemented; not the gap. |
| MECH-229 | mechanism / provisional | standard | Narrowed umbrella (leg a, wanting!=liking); drive-leg carried by MECH-436. |
| MECH-230 | mechanism / provisional | substrate_ceiling | Structured-z_goal attractor; 514m gave first genuine support on scaffolded substrate. |

**Did the experiment let the claims express themselves? No.** The sleep intervention operates on a
waking substrate that never encoded the consumption-identity target it was meant to consolidate. An
implementation-adjacent starvation gap is being read as a claim test. The manifest's tags are
inherited from the 514f lineage without re-evaluating against the June 514l/514m foraging-competence
diagnosis.

---

## 3. Biological-reference triage (the core move)

Sleep-dependent schema consolidation -- the exact literature the script cites (Lansink et al. 2009
hippocampus-leads-striatum SWR replay; Stickgold 2013; Walker 2017 REM generalisation) -- is
**downstream of waking encoding**. SWR replay consolidates experiences the animal actually had. At
~0.4% consumption there are almost no consumption episodes to replay, so there is nothing for SWS/REM
to etch.

The FAIL therefore matches the biological **missing-dependency signature** (absent foraging
experience -> absent consolidation substrate), which is a *discovered prerequisite*, not a
falsification of sleep-consolidation. If anything it is weak positive evidence for the
encoding-precedes-consolidation ordering.

**The hypothesis was aimed at the wrong root cause.** 514f attributed the classifier divergence to
"missing offline consolidation." The June 514l/514m autopsies proved the real root was
**foraging-competence starvation**. Decisively: `failure_autopsy_V3-EXQ-514m` recorded the identity
probe at **0.926 (n=3,455) with NO sleep** once foraging-competence was scaffolded
(`scaffolded_sd054_onboarding`, ready 2026-06-11). So "sleep recovers identity" is not merely
untested here -- it is likely *unnecessary*: identity recovers fine with foraging-competence and no
sleep. 538a is a 2026-05-08 script that predates the entire 514l -> 514o -> 693 substrate-enrichment
arc and re-ran the pre-enrichment starved reef config.

**is_formal_import:** partial. SD-017's biological grounding is strong (5+ lit entries, promoted on
consolidated sleep-phase biology). The failure is not a formal-import divergence; it is an
environment/measurement starvation. No `/lit-pull` commission owed.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear (untested)** | Waking pass never encoded consumption-identity; sleep can't consolidate the absent representation. |
| Biological reference | **clear** | Consolidation is downstream of encoding; FAIL matches missing-dependency signature. Weak positive for the dependency. |
| Prerequisites | **missing** | Foraging-competence on the 3-type SD-049 reef substrate (goal_pipeline:GAP-2); ARM_2 contact-rate gap open per 693a. |
| Implementation | **complete** | SWS/REM writes fire (160/40). Sleep substrate is not the gap. |
| Environment | **too sparse** | ~0.4% consumption -> identity pathway starved at both training and eval. |
| Measurement | **under-instrumented / misleading** | Consumption probe n=45-72 (chance-straddling noise); classifier ~30-50 updates; seed-44 truncation. |
| Integration | isolated | Sleep runs; downstream target absent. |
| Scale / capacity | adequate on 2 seeds | Seed 44 degenerate (12-15% of steps, peak drive ~0.11). |

**Recommended epistemic_category: `substrate_ceiling`.**

---

## 5. Cluster context + re-derive brake (MOVE-3 -- FIRES)

538a is not an isolated FAIL; it is the latest lap of the SD-049 Phase-2 substrate-ceiling loop.
Prior `substrate_ceiling` / `non_contributory` autopsies by claim:

- **SD-049:** 514l, 693, 693a (3 prior) -> **538a is the 4th**
- **SD-015:** 514l, 693, 693a (3 prior)
- **MECH-229:** 514l, 514m, 514p, 514q (4 prior) -> **538a is the 5th**
- **MECH-230:** 514l, 632 (2 prior)

`RE_DERIVE_BRAKE_THRESHOLD` = 2. Every claim in this autopsy's target set is far past it, and 538a
re-ran the **same starved reef config** the ceiling was diagnosed on (not the enriched
`scaffolded_sd054_onboarding` substrate that is already ready). **The brake fires.**

- **Routing = `implement-substrate`** on the 3-type foraging-competence gap.
- **REFUSE a same-config re-queue.** No further SD-049-Phase-2 sleep letter on the 514f reef config.
  User-adjudicated 2026-07-10: also declining to pre-authorize a redesigned sleep test on the
  scaffolded substrate now -- a sleep experiment is only in scope *after* the 3-type ARM_2
  contact-rate gap is built (at which point it would be a new-EXQ, different-substrate design, brake-exempt).
- **upstream_substrate:** SD-049-PHASE-2 (the 3-type ARM_2 foraging-contact shortfall; same track as
  693a's failure record on `scaffolded_sd054_onboarding`).

This is the producer half of MOVE-3; `/queue-experiment` Step 2.5 is the consumer half and will
refuse the re-test until the upstream substrate lands.

---

## 6. Learning extracted

1. **The 514f -> 538a sleep hypothesis was a misdiagnosis.** The classifier divergence 514f blamed
   on "missing offline consolidation" was foraging-competence starvation (~0.4% consumption,
   ~30-50 classifier updates). Sleep cannot consolidate an unencoded representation.
2. **Identity recovery does not need sleep once foraging-competence exists** (514m probe 0.926,
   n=3,455, sleep off). The sleep axis was targeting a symptom of the wrong root cause.
3. **Well-powered != claim-relevant.** The C4 neighborhood null is a clean, ~9k-sample null -- but
   of a mis-specified intervention on an untrained substrate. It carries no signal about whether
   sleep consolidates consumption-identity, nor about SD-049 Phase-2.
4. **Manifest self-declared directions are unreliable here.** Top-level `weakens` is the crude
   FAIL->weakens default and contradicts the per-claim block (SD-049/SD-017 "supports"). Those
   "supports" are vacuous (noise-OR C3b; sleep-write liveness). Governance should override with
   `non_contributory` across the board.
5. **Seed-44 truncation** is a recurring per-seed instability on this reef config worth watching in
   any successor harness (early episode death at ~step 40).

---

## 7. Recommended governance writes (draft -- do NOT apply here)

**evidence_direction (all five claims): `non_contributory`**, `pending_retest_after_substrate: true`,
`epistemic_category: substrate_ceiling`. No status changes. SD-017 stays `stable` unchanged.

Draft `evidence_quality_note` (governance to write, verbatim intent):

> 2026-07-10 (failure_autopsy_V3-EXQ-538a, confirmed): V3-EXQ-538a (SD-049 Phase-2 reef behavioural
> validation, sleep-on ablation; supersedes the 538 SIGTERM) FAILed on C4 (sleep lift over ARM_0 on
> the neighborhood probe = -0.001) and self-declared weakens. Re-tagged **non_contributory /
> substrate_ceiling / pending_retest_after_substrate** for all five tagged claims. The run re-ran the
> pre-enrichment 514f reef config (classifier_loss_weight=0.1, ~0.4% consumption): the identity
> classifier gets only ~30-50 gradient updates over 9,000 steps and the consumption probe is
> starved (n=45-72), so the waking pass never encoded consumption-identity for sleep to consolidate.
> Sleep substrate fired (SWS/REM writes 160/40) but has nothing to etch -- a missing-dependency
> signature (consolidation is downstream of encoding; Lansink/Stickgold/Walker), not a falsification.
> 514m already recovered identity to probe 0.926 (n=3,455) with sleep OFF once foraging-competence
> was scaffolded, so the sleep hypothesis targeted a symptom of the wrong root cause. Seed 44 was a
> truncated run (12-15% of steps). The manifest's per-claim "supports" for SD-049 (noise-OR C3b) and
> SD-017 (SWS/REM-write liveness) are vacuous and NOT counted; SD-017 stays stable/unchanged (its
> genuine support is V3-EXQ-691). Re-derive brake fired (4th substrate_ceiling autopsy for SD-049,
> 5th for MECH-229): route to /implement-substrate on the 3-type ARM_2 foraging-contact gap
> (SD-049-PHASE-2 / scaffolded_sd054_onboarding, same track as the 693a failure record); REFUSE a
> same-config SD-049-Phase-2 sleep re-queue.

**Substrate routing:** `action: amend`, target `SD-049-PHASE-2` (equivalently the
`scaffolded_sd054_onboarding` foraging-competence leg) -- append the 538a failure record to the
existing 3-type ARM_2 foraging-contact gap already recorded by 693a. Do NOT create a new entry (the
gap is already articulated). See JSON `recommended_substrate_queue_entry`.

**Routing: `implement-substrate`.** No `/queue-experiment` for another same-config sleep letter
(brake). No `/lit-pull` (biology is well-grounded; the gap is environment/measurement). Not
`/claim-synthesis` -- the 514q split already resolved the MECH-229 lineage granularity debt, and this
FAIL is a same-granularity re-derive against the same ceiling, which is exactly what the brake (not
synthesis) handles.
