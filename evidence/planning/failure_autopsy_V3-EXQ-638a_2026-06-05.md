# Failure Autopsy — V3-EXQ-638a (nursery-to-forager cue->contact bridge)

**Date:** 2026-06-05T09:03:44Z
**Scope:** single (with 638 / 634c / 610e / 639 as context)
**Status:** confirmed (interactive gate passed; routing = measurement-first, gate 638b)
**Target run:** `v3_exq_638a_scaffold_cue_recall_contact_ablation_20260604T183612Z_v3`
**Queue id:** V3-EXQ-638a  |  **claim_ids:** [] (substrate-readiness / behavioural diagnostic, NOT governance evidence)
**Machine:** ree-cloud-2  |  **Outcome:** FAIL  |  **evidence_direction:** non_contributory

---

## 1. Facts (no interpretation)

Two arms x 3 seeds. ARM_CUE_ON sets `scaffold_stage0_bind_incentive_token=True`
(the 638 formation fix); ARM_OFF leaves the cue bridge off. Both arms set the
landed 634c ARM_3 seeding regime (`drive_floor=0.9`, `benefit_threshold=0.02`)
directly, so the run is self-contained (not dependent on the stalled 634c run).

Pre-registered gates and acceptance:

| Gate | Definition | Result |
|---|---|---|
| C1 cue fires (ON) | ARM_CUE_ON P2 `n_cue_recall_fires > 0` on >= 2/3 seeds | **PASS** |
| C2 cue silent (OFF) | ARM_OFF P2 `n_cue_recall_fires == 0` on ALL seeds | **PASS** |
| C3 contact lift | ARM_CUE_ON P2 `contact_rate` > ARM_OFF per matched seed on >= 2/3 | **FAIL** |
| C4 survival not regressed | — | PASS |
| overall | — | **FAIL** |

Per-seed P2 numbers:

| seed | ON contact | OFF contact | ON cue fires | ON token bank | ON drive_peak | ON matched_token_strength |
|---|---|---|---|---|---|---|
| 42 | 0.000 | 0.000 | 1050 | 3 | 0.280 | 0.200 |
| 43 | 0.000 | 0.197 | 180  | 3 | 0.039 | 0.199 |
| 44 | 0.267 | 0.648 | 446  | 3 | 0.144 | 0.023 |

Cross-arm, every seed/phase: `n_interoceptive_need_cues = 0`, `n_joint_cues = 0`,
`cue_nonfire_reason_counts = {}` (the cue always fires when attempted),
`best_prox_peak ~ 1.0` in ARM_CUE_ON. Stage-0 token bank populated 0 -> 3 in
ARM_CUE_ON (formation fix worked); ARM_OFF bank stayed 0 (correctly cue-silent).

**Failed criterion = discrimination (C3).** The absolute/wiring criteria (C1 cue
fires, C2 OFF silent, formation) all PASS.

## 2. The three facts that sharpen the read

1. **Cue-on is not behaviourally neutral — it is mildly counterproductive.**
   ARM_CUE_ON contact `[0.0, 0.0, 0.267]` is <= ARM_OFF `[0.0, 0.197, 0.648]` on
   EVERY matched seed (0/3 show ON > OFF). The cue-silent arm reaches contact via
   wild seeding alone; firing the cue 1050x produced *less* contact, not more.
   => contact competence EXISTS in the substrate (ARM_OFF seed 44 = 0.648); the
   cue is failing to recruit it and may be DISPLACING it.
2. **The interoceptive pathway is structurally absent, not merely weak.**
   `n_interoceptive_need_cues = 0` and `n_joint_cues = 0` in every arm/seed. The
   fired cue is purely exteroceptive ("a resource is perceived"), never "this
   restores me-now."
3. **drive_peak on seed 42 ARM_CUE_ON was 0.28** (depleted, not well-fed) with
   1050 fires and a matched token, and STILL 0 contact. So "the agent was sated,
   so the cue shouldn't drive approach" does NOT explain the seed-42 zero. This
   actively WEAKENS the pure-interoceptive reading as the sole/proximate cause.

## 3. Mechanistic candidate (repo-grounded)

The substrate has the wiring `cue_recall_wanting -> goal_state.z_goal ->
action_object(current_z_goal=...) + MECH-295 approach` (ree-v3
`agent.py:2834-2846`; cue context also yields `_cue_action_bias` via
`extract_cue_context`, `agent.py:2757-2763`). So the cue->action path is built.

Cue recall pulls z_goal toward a WEAK token (`matched_token_strength ~ 0.2`,
0.023 on seed 44). The wild-seeding regime (`drive_floor=0.9`) that produces
ARM_OFF contact builds a DIFFERENT z_goal attractor. **Displacement hypothesis:**
the cue overwrites a stronger working attractor with a weaker token-aligned one,
yielding net-negative authority rather than a missing one. Testable directly:
post-cue z_goal norm should be LOWER than the ARM_OFF attractor norm.

## 4. Biological-reference triage

Closest reference: cue-triggered incentive salience / Pavlovian-instrumental
transfer (Berridge & Robinson incentive salience; Toates motivational-state x
incentive-stimulus; Cabanac alliesthesia). In biology these are STATE-DEPENDENT:
a cue amplifies wanting conditionally on physiological need. REE's SD-057 cue is
currently state-INDEPENDENT (exteroceptive only) -- this is a faithful-but-partial
translation, not a formal-definition import. The missing interoceptive binding is
a genuine biological divergence AND is already captured as the Layer-2 design
(thought-intake doc S6). BUT biology also requires the cue to acquire
behavioural authority via the action/approach pathway; 638a does not establish
that the fired cue reaches action selection at all. So the biology supports BOTH
candidate bridges (authority and interoception) and does not adjudicate between
them -- which is exactly why a measurement pass is needed before building either.

`targeted_review_object_bound_incentive_salience` referenced by the thought-intake
doc DOES NOT EXIST in evidence/literature/ (only object_files_feature_binding and
object_permanence). A Layer-2 lit-pull (Berridge/Toates/Cabanac state-dependence)
is a prerequisite IF/WHEN 638b interoceptive work proceeds -- not now.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | diagnostic, claim_ids=[]; no governance weighting |
| Biological reference | partial | state-dependent incentive salience; REE cue is state-independent; biology supports both candidate bridges, adjudicates neither |
| Developmental / dependency prereqs | present (formation) / missing (authority+interoception untested) | Stage-0 token formation now works (bank 0->3); cue->action authority and interoceptive binding unverified |
| Implementation completeness | partial | cue_recall_wanting + z_goal + MECH-295 wired; interoceptive (n_interoceptive=0) and joint (n_joint=0) pathways not exercised |
| Environment adequacy | adequate / unknown for 4-dir gradient | CausalGridWorld 4-direction approach is multi-step axis search; not isolated |
| **Measurement adequacy** | **under-instrumented (dominant gap)** | measures cue_fires and contact_rate, NOTHING in between: no post-cue z_goal delta, action_bias magnitude, approach rate, gradient/distance delta, hazard-interrupt count |
| Integration adequacy | partially coupled / unstable | cue fires but its effect on action selection is unmeasured and possibly negative (displacement) |
| Scale / capacity | unknown | token strength ~0.2 may be sub-threshold for MECH-295 approach |

**Recommended epistemic_category:** n/a for governance (claim_ids=[]); for the
finding, this is a **measurement_gap + behavioural diagnostic**, not a
substrate_ceiling and not a falsification.

## 6. Branch ranking

| Rank | Branch | Why |
|---|---|---|
| 1 | **Cue-to-action authority** (incl. displacement) | cue fires hard, contact strictly <= cue-silent, drive adequate on the zero-contact seed |
| 2 | Safe gradient-following / 4-dir axis-decomposition | weak attractor in a 4-dir grid needs multi-step axis search; untested |
| 3 | Interoceptive need-gating (638b) | structurally absent and worth building EVENTUALLY, but seed-42 depleted-yet-zero argues it is not the proximate blocker |
| 4 | Orienting/surveying; hazard-interrupt/resume | plausible but unmeasured; cannot rank until the post-cue trace exists |

## 7. Learning extracted

- 638a settled branch (b) only at the resolution of "fires vs contact." It
  cannot distinguish cue-to-action authority / gradient-following / interoceptive
  / orienting / hazard-interrupt because NO post-cue action trace was logged.
- The ON<=OFF contact pattern raises a DISPLACEMENT hypothesis (weak token
  attractor overwriting the wild-seeded one) -- a net-negative authority reading
  not previously captured.
- Building the 638b interoceptive substrate now would add Layer-2 MEANING on top
  of an unestablished assumption that the cue has Layer-1 behavioural AUTHORITY.
- Contact competence is present in the substrate (ARM_OFF reaches 0.648); the
  open question is recruitment/authority, not whether contact is reachable.

## 8. Repair pathway (routing) — confirmed with user

**Routing: `queue-experiment` (measurement-only diagnostic), gating the
already-planned 638b interoceptive build.**

Proposed smallest next step (NOT yet queued; goes through /queue-experiment):
a measurement-only post-cue action/gradient diagnostic. Re-run the existing
`scaffolded_sd054_onboarding` ARM_OFF/ARM_CUE_ON ablation **behaviourally
unchanged**, adding per-cue-fire instrumentation only (no new substrate
primitive, no new env knob, no tuning). Windowed around each cue fire, log:

- `post_cue_z_goal_norm_delta`, `cue_action_bias_magnitude` (displacement test:
  is post-cue z_goal norm LOWER than the ARM_OFF attractor?)
- `post_cue_selected_action_approach_rate`,
  `post_cue_manhattan_distance_delta_to_resource` (uses best_prox / resource
  field already in cue_diag)
- `salience_interrupt_count_after_cue` / `post_cue_hazard_salience_spike_count`
  (MECH-259 / MECH-261 + z_harm)
- `cue_to_first_gradient_improving_move_latency`, `oscillation_rate_after_cue`
- (optional, field OFF) candidate-rule context->action->outcome tuple counts, so
  ARC-063 minting readiness can be assessed without enabling it.

**Naming:** a genuinely different scientific question (cue->action translation)
than 638's "does recall fire and lift contact" -> new number, **proposed
V3-EXQ-640**. The repo already reserves "638b" for the interoceptive
OFF/EXTERNAL_ONLY/JOINT arms; 640 GATES 638b.

**No substrate_queue entry** (`recommended_substrate_queue_entry.action = "none"`):
the next step is measurement, not substrate. **No demotion** (no claim tagged).
**No lit-pull yet** (the Berridge/Toates/Cabanac Layer-2 pull is a prerequisite
only IF 640 routes to the interoceptive build).

Discriminator map for V3-EXQ-640:

| 640 result | Read | Next route |
|---|---|---|
| cue fires, ~0 z_goal/action_bias delta (or negative) | cue-to-action authority missing / displacement | wire/strengthen cue->E3 authority BEFORE interoceptive; revisit token strength |
| cue fires, action delta but no gradient improvement | gradient-following / 4-dir axis-decomposition missing | safe-gradient-following diagnostic (or directional forced-choice) |
| cue fires, gradient improves, then hazard interrupt aborts | interrupt-without-resume | goal-persistence-across-salience-switch diagnostic |
| cue fires, gradient improves, no interrupt, still no contact | persistence / reorientation | orienting/surveying diagnostic |
| cue fires, gradient improves, contact lifts | (contradicts 638a) | promote authority bridge; only THEN consider 638b interoceptive |

## 9. Do-not-do-yet (V3 scope-creep guards)

- Do NOT build the 638b interoceptive need-gating substrate yet (gate behind 640).
- Do NOT build orienting/surveying mode, safe-gradient-following primitive,
  hazard-clearance scaffold, four-direction forced-choice env, stable->moving
  ecology curriculum, or safe-weaning scaffold. All validly captured as routing
  hypotheses; none justified until 640 says which.
- Do NOT activate CandidateRuleField (ARC-063) as the nursery-to-forager fix.
  639 shows substrate-readiness only; the bottleneck is upstream. At most, log
  candidate-rule tuples with the field OFF inside 640.
- Do NOT let 610e (crystallization-necessity, INV-074/MECH-333/334) or
  safe-weaning enter this thread. Separate cluster / later layer.
- Do NOT tune any parameter to pass C3.

## 10. Cross-references

- thought_intake_2026-06-04_cue_ecology_weaning_nursery_to_forager.md (Layers 1/2;
  638b plan; S8 safe-weaning; this autopsy's capture note appended to it).
- failure_autopsy_V3-EXQ-638_2026-06-04.{md,json} (predecessor formation autopsy).
- docs/thoughts/2026-06-04_Orienting_surveying_drive.md (orienting/surveying
  hypothesis + metric set, a candidate route OUT of 640).
- docs/thoughts/2026-06-04_attention_distributed_precision_selection.md (cue
  authority = precision-selection territory; containment-only for V3).
- ree-v3 agent.py:2757-2763 (_cue_action_bias), 2834-2846 (action_object
  current_z_goal + MECH-295); goal.py IncentiveTokenBank / cue_recall_wanting.
- goal_pipeline:GAP-2 (foraging-contact ceiling), GAP-7 (object-bound incentive).
