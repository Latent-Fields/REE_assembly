# Failure Autopsy -- V3-EXQ-693a (SD-049 Phase-2 4-arm substrate-gradient validation)

- **Generated:** 2026-06-21T11:46:35Z (staging mode -- headless scheduled `failure-autopsy-sweep`)
- **Status:** `awaiting_human_confirmation` (a draft for the next interactive `/governance` walk -- routing is NOT finalised and NEVER auto-applies)
- **Run:** `v3_exq_693a_sd049_phase2_4arm_substrate_gradient_validation_20260621T093032Z_v3` (machine `ree-cloud-1`)
- **Queue id:** V3-EXQ-693a (supersedes V3-EXQ-693)
- **Outcome:** FAIL, self-routed `evidence_direction: non_contributory` (SD-049 + SD-015), `readiness_route: substrate_not_ready_requeue`, `route_reason: non_vacuity_unmet`, `non_degenerate: false`
- **Claims under test:** SD-049 (multi_resource_heterogeneity; candidate / substrate_ceiling / v3_pending / pending_retest) + SD-015 (z_resource_encoder; candidate / substrate_ceiling / pending_retest)
- **Scope:** single (read against the 514 lineage; see Granularity-debt)

## Verdict (staging draft -- to confirm)

**The 514t WL-scoring harness port WORKED. The run self-routed not because the WL channel is broken (that was the *predecessor* 693's cause) but because the PRIMARY measured arm ARM_2 (3type+novelty) produced ZERO contributing runs -- a foraging-competence / survival shortfall (goal_pipeline:GAP-2), not a WL-harness recurrence and not a falsification.** The self-route disposition (`substrate_not_ready_requeue` / `non_contributory` / never a weakens) is CORRECT; the manifest `degeneracy_reason` text ("WL channel not fireable -> the V3-EXQ-693 stale-harness signature") **mislabels the cause** (the canonical V3-EXQ-642 self-route-is-a-hypothesis lesson). Route: **implement-substrate** amend (ARM_2 foraging competence) **then `/queue-experiment` 693b** (NEW letter, same scientific question on the competence-fixed substrate).

---

## 1. Facts -- why the run self-routed

The composite acceptance gates on three non-vacuity legs, **all keyed on the PRIMARY arm ARM_2** (`PRIMARY_ARM = "ARM_2"`, `CONTROL_ARM = "ARM_0"`):

| guard | rule | value |
|---|---|---|
| R1 consumption | `control.contribute_frac >= 2/3 AND primary.contribute_frac >= 2/3` | **false** (ARM_2 contribute_frac = **0.0**) |
| R2 identity-probe-fireable | `primary.pooled_n_identity_samples >= 30` | **false** (ARM_2 pooled = **0**) |
| R3 WL-channel-fireable | `pc_separation >= 1.0 AND primary.run_bank_populated_frac >= 2/3` | **false** (ARM_2 run_bank_populated_frac = **0.0**) |
| non_vacuity_met | R1 AND R2 AND R3 | false -> `substrate_not_ready_requeue` |

All three legs are False for the **same** reason: **ARM_2 has zero contributing runs.** `contributes = guard_pass AND behav_contact_rate > CONSUMPTION_FLOOR(0.02)`, where `guard_pass = (p2.contact_rate > 0.0) AND (p2.z_goal_norm_at_contact_peak > 0.4)`:

| ARM_2 seed | guard_pass | behav_contact_rate | contributes | why not |
|---|---|---|---|---|
| 42 | true | 0.0188 | **false** | contact 0.0188 < CONSUMPTION_FLOOR 0.02 (a whisker short) |
| 43 | false | 0.0099 | false | hazard_stage_survival_pass=false; contact below floor |
| 44 | false | 0.0131 | false | guard_pass false; contact below floor |

**What DID fire (this is the load-bearing signal):** the WL-scoring port works wherever a run contributes.

| arm | n_contributing | n_scored_wl_steps_total | mean_probe_acc_identity | per_axis_drive_anova_f_max | mean_discrimination_margin |
|---|---|---|---|---|---|
| ARM_0 (OFF, 1 type) | 2/3 | 0 (by design, single type) | 0.0 | 0.0 | 0.0 |
| ARM_1 (2type) | 1/3 | **15** | 0.779 | 426.7 | 0.0019 |
| ARM_2 (3type+novelty, **PRIMARY**) | **0/3** | 0 | 0.0 | 0.0 | 0.0 |
| ARM_3 (5type) | 2/3 | **20** | 0.519 | 1761.6 | -0.003 |

So z_resource binds (distinct tokens 2/3/5), per-axis drive differentiates (ANOVA F up to 1761), identity recovers (0.78 / 0.52), and the object-bound wanting!=liking leg SCORES (15 / 20 steps) on the arms that have contributing runs. **The 693 stale-514l-harness instrumentation gap is fixed.**

---

## 2. The self-route label vs the real cause

693's autopsy correctly diagnosed `R3 WL-channel-fireable=false` as a stale-harness instrumentation gap (n_scored_wl_steps_total **0 across every arm/seed**). 693a ported the 514r/s/t harness -- and it works. But 693a's `degeneracy_reason` carries the predecessor's language verbatim ("WL channel not fireable -> the V3-EXQ-693 stale-harness signature"), which reads as if the instrumentation gap recurred. It did not. The unmet non-vacuity gate is attributable to **ARM_2 contribution-collapse** (foraging competence / hazard-stage survival), one link downstream of the WL harness.

This is the canonical **self-route-is-a-hypothesis** failure mode (V3-EXQ-642 `failure_autopsy_V3-EXQ-642_2026-06-06`): the manifest's `interpretation.label` is correct as a *disposition* (do not score; re-queue) but mis-attributes the *cause*. Governance should record the corrected attribution.

---

## 3. Claim-layer mapping

- **SD-049** (multi_resource_heterogeneity): the WL-dissociation deliverable is the load-bearing test; it was reached on ARM_1/ARM_3 but not on the PRIMARY arm ARM_2. **Correctly `non_contributory`** at the run level -- no WL-dissociation information about SD-049 from a vacuous primary arm. Substrate (Phase-1 env + Phase-2 encoder) NOT implicated.
- **SD-015** (z_resource_encoder): identity-recovery **fired and passed non-vacuously** on the contributing arms (ARM_1 0.779 / ARM_3 0.519; pooled identity samples 2021 / 4629). The blanket composite-FAIL `non_contributory` under-credits this leg -> **narrow_supports_flag = true** (a note on the claim, NOT a supports entry; the composite run FAILed and the primary arm was vacuous). Consistent with the 693 disposition.

`claim_ids = [SD-049, SD-015]` are accurate for what the experiment intends to test; both correctly held `non_contributory` at the run level.

---

## 4. Biological-reference triage

- **Closest mechanism:** object-bound, drive-modulated incentive salience (wanting) dissociable from consummatory liking (Berridge; specific PIT, Corbit/Balleine). Grounded; the dissociation is a sound biological reading, structurally validated by the 514 lineage.
- **Formal import?** No.
- **Does the failure match a missing dependency?** No -- it matches a FORAGING-COMPETENCE signature on the primary arm (3-type + novelty contact below floor, 2/3 seeds failing hazard-stage survival). The wanting!=liking mechanism is not implicated; brains remain the existence proof. The discovered prerequisite is goal_pipeline:GAP-2 contact competence on the multi-resource substrate.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | primary arm never let the claim express itself; SD-015 expressed on contributing arms |
| Biological reference | clear | mechanism not implicated; failure is foraging-competence |
| Prerequisites | **missing** | ARM_2 contact 0.0099-0.0188 < floor 0.02; 2/3 seeds fail hazard-stage survival (goal_pipeline:GAP-2) |
| Implementation | **complete** | 514t WL-harness port fires (15/20 steps); the 693 gap is fixed |
| Environment | too sparse (primary arm) | 3-type+novelty forages less; novelty_decay + guarded P2 starves contact on the measured arm |
| Measurement | adequate | non-vacuity gate correctly refused a vacuous run; reporting under-attributes the cause |
| Integration | partially coupled | WL leg works; the contribution gate on the 3-type arm is the bottleneck |
| Scale | likely insufficient (primary arm) | foraging-competence/survival budget on the 3-type substrate |

Recommended REE-native `epistemic_category`: **substrate_ceiling** (unchanged; the right response is substrate enrichment / foraging competence, then re-queue).

---

## 6. Learning extracted

1. The WL-scoring harness port (693 -> 693a) succeeded -- object-bound wanting!=liking scored wherever a run contributed (ARM_1 15, ARM_3 20).
2. The blocker MOVED one link downstream: WL-harness instrumentation (693) -> PRIMARY-arm foraging competence (693a, ARM_2). The self-route is correct; its cause-attribution is wrong.
3. Where WL fired, the C_GR discrimination margin is near-zero (0.0019 / -0.003) -- the pre-registered `c_gr_watch_item` is now PARTIALLY observable and is the likely real SD-049 Phase-2 conversion question once a contributing primary arm exists.
4. Non-vacuity gates keyed solely on the primary arm can trip on a primary-arm competence shortfall while the instrument is sound -- consider per-arm WL-fireability reporting so a future autopsy distinguishes "harness broken" from "primary arm starved".

---

## 7. Repair pathway (recommended; not applied)

| Diagnosis | Routing |
|---|---|
| Missing primary-arm foraging competence (3type+novelty contact below floor + survival fail) | **implement-substrate** amend onto `scaffolded_sd054_onboarding` (or `SD-049-PHASE-2`) -- ARM_2 foraging competence; governance materialises the `recommended_substrate_queue_entry` |
| Same scientific question on the fixed substrate | **/queue-experiment 693b** (NEW letter; do NOT re-run under 693a) once ARM_2 yields contributing runs on >=2/3 seeds |
| 9th autopsy on the SD-049 / WL-dissociation lineage | **/claim-synthesis recurrence flag** -- surface at the human gate to decide decompose-vs-long-substrate-chain (see below); NOT this autopsy's own routing |

**Draft `evidence_quality_note` (governance to write, NOT written here):**

> V3-EXQ-693a (2026-06-21, failure-autopsy): non_contributory CONFIRMED for SD-049 + SD-015. The 514t WL-scoring harness port WORKED (n_scored_wl_steps_total 15/20 on contributing arms ARM_1/ARM_3; identity probe 0.78/0.52; per-axis drive ANOVA F up to 1761), so the 693 stale-harness instrumentation gap is FIXED. The run self-routed substrate_not_ready_requeue because the PRIMARY arm ARM_2 (3type+novelty) produced 0 contributing runs -- contact rates 0.0099-0.0188 below CONSUMPTION_FLOOR 0.02 and 2/3 seeds failing the hazard-stage survival / p2 z_goal guard. This is the goal_pipeline:GAP-2 foraging-competence ceiling, NOT a WL-harness recurrence and NOT a falsification. Where WL fired, the C_GR discrimination margin was near-zero (ARM_1 0.0019, ARM_3 -0.003) = the pre-registered c_gr_watch_item. SD-015 identity recovery fired non-vacuously on the contributing arms -> narrow_supports note. Re-test in 693b once ARM_2 foraging competence clears.

---

## 8. Granularity-debt recurrence flag

This is the **9th** failure-autopsy circling the SD-049 / wanting!=liking dissociation: 514l, 514m, 514p, 514q, 514r, 514s, 514t, 693, **693a**. The recurrence is real, but most members share the **same** failure shape (substrate / instrumentation not ready), which reads as iterative substrate-readiness debt rather than the "coarse claim needs splitting in structurally-different ways" signal. **Surface a `/claim-synthesis` review at the human gate** to decide whether the SD-049 Phase-2 measurement has accumulated enough *distinct* failure signatures to warrant decomposition, OR is simply a long substrate-readiness chain. Do not auto-route to `/claim-synthesis`.

---

## 9. Evidence protection (no governance risk)

SD-049 and SD-015 are both `candidate / substrate_ceiling / pending_retest_after_substrate` (SD-049 also `v3_pending`); promote/demote is suppressed for `substrate_ceiling`. The 693a manifest already self-reports `non_degenerate: false` with a `degeneracy_reason`, so the indexer marks it `scoring_excluded: degenerate` and it does not weight confidence or conflict. **This run cannot move governance; this autopsy is a diagnosis + substrate hand-off only.**

## 10. Governance actions owed (next interactive walk)

- Confirm the routing (staging draft; never auto-applies).
- Optionally write the SD-015 narrow_supports `evidence_quality_note` + the corrected `degeneracy_reason` attribution.
- Materialise the `recommended_substrate_queue_entry` (amend) onto the chosen substrate_queue entry.
- Mark V3-EXQ-693a discussed in `review_tracker.json` (manifest stem `v3_exq_693a_sd049_phase2_4arm_substrate_gradient_validation_20260621T093032Z_v3`) once reviewed -- left untouched here (failure-autopsy never edits review_tracker).
