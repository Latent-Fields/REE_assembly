# Failure Autopsy — V3-EXQ-640 (SD-057 cue-recall post-cue action / gradient diagnostic)

**Date:** 2026-06-05T14:34:59Z
**Scope:** single (638a / 638 / 634c / 610e as context)
**Status:** confirmed (interactive gate passed; routing = cue-authority sweep, gates 638b)
**Target run:** `v3_exq_640_scaffold_cue_postcue_action_gradient_diagnostic_20260605T125802Z_v3`
**Queue id:** V3-EXQ-640  |  **claim_ids:** [] (measurement-only behavioural diagnostic, NOT governance evidence)
**Machine:** ree-cloud-1  |  **Manifest outcome:** PASS (measurement-success gates only)  |  **evidence_direction:** non_contributory

> Why this is a `/failure-autopsy` target despite `outcome=PASS`: 640's PASS reflects only
> the measurement gates (C1 cue fires, C2 post-cue trace captured). `evidence_direction =
> non_contributory` is the diagnosis-pending signal — 640 was built (by
> failure_autopsy_V3-EXQ-638a_2026-06-05 Sections 7-8) to MEASURE the branch 638a's C3
> contact-lift FAIL could not discriminate. The discriminator grid applied to the captured
> trace IS the diagnosis 640 was waiting for.

---

## 1. Facts (no interpretation)

Two arms x 3 seeds (42/43/44), behaviourally identical to 638a, both arms with
`scaffold_post_cue_instrumentation=True`. ARM_OFF fires no cue but supplies the
cue-independent background baselines. Both arms set the landed 634c ARM_3 seeding
regime (`drive_floor=0.9`, `benefit_threshold=0.02`) directly; self-contained.

**ARM_CUE_ON (1557 cue fires total across 3 seeds):**

| seed | cue fires | P2 contact | cue z_goal pull | mean z_goal Δ post-cue | ‖z_goal‖ at fire | post-cue approach | background approach | hazard-interrupt rate | oscillation |
|---|---|---|---|---|---|---|---|---|---|
| 42 | 713 | 0.000 | 0.0022 | +1.04e-05 | 0.526 | 0.0888 | 0.0898 | 0.498 | 0.230 |
| 43 | 296 | 0.000 | 0.0027 | +7.67e-06 | 0.432 | 0.0569 | 0.0541 | 0.865 | 0.399 |
| 44 | 548 | 0.288 | 0.00044 | +1.28e-04 | 0.443 | 0.101 | 0.117 | 0.447 | 0.027 |

**ARM_OFF (no cue; baseline):**

| seed | P2 contact | background approach | mean ‖z_goal‖ all steps |
|---|---|---|---|
| 42 | 0.000 | 0.121 | 0.438 |
| 43 | 0.287 | 0.040 | 0.443 |
| 44 | 0.283 | 0.358 | 0.408 |

Cross-arm: `n_cue_action_bias_present = 0` on every seed / every fire (the SD-016
`agent._cue_action_bias` channel was `None` throughout — see §2 caveat).

**Pre-registered measurement gates:** C1 cue fires ON (PASS), C2 post-cue trace
captured (PASS), overall PASS. These gate only that the discriminator grid is
*computable* — they are not a scientific pass.

## 2. Three reads that settle 638a's open branch

1. **Displacement is REFUTED.** 638a raised the hypothesis that the cue overwrites a
   stronger wild-seeded z_goal attractor with a weaker token (net-negative authority;
   post-cue ‖z_goal‖ should be LOWER than the ARM_OFF attractor norm). 640 shows the
   opposite: ‖z_goal‖ at cue fire (0.526 / 0.432 / 0.443) is equal-or-higher than the
   ARM_OFF attractor norm (0.438 / 0.443 / 0.408), and the cue moves z_goal by ~0.002
   against a norm of ~0.45 — a **~0.4% nudge**. The cue does not displace the attractor;
   it barely touches it.

2. **Cue-to-action authority is the gap (grid row 1, confirmed).** Post-cue approach rate
   is statistically indistinguishable from the cue-independent background
   (0.0888 vs 0.0898; 0.0569 vs 0.0541) and *lower* on seed 44 (0.101 vs 0.117). The cue
   fires 713 / 296 / 548 times and produces **zero approach lift**. ARM_CUE_ON contact
   ([0.0, 0.0, 0.288]) ≈ ARM_OFF contact ([0.0, 0.287, 0.283]) on every seed — the contact
   that occurs is wild foraging at background rate, NOT cue-driven. The cue is
   **behaviourally inert, not counterproductive** — a sharper read than 638a's "mildly
   counterproductive."

3. **The interoceptive reading is not the proximate cause.** Seed 42 fired 713 times with
   z_goal norm preserved (0.526) and STILL produced zero approach lift. The cue's failure
   is gain / authority, not need-gating. (Layer-2 interoceptive meaning on top of a cue
   that has no Layer-1 behavioural authority would be premature — 638a's argument, now
   confirmed with the action trace.)

**Measurement-interpretation caveat (so governance does not misread it):**
`n_cue_action_bias_present = 0` is the SD-016 `cue_action_proj` channel
(`agent._cue_action_bias`), which is known-ungrounded (EXP-0155 / V3-EXQ-449:
exactly-zero gradient, action_bias_divergence 0.0). The SD-057 cue acts via
`GoalState.cue_pull` on z_goal, NOT via the SD-016 action projection, so the
SD-016 channel being `None` is **expected-absent, not the finding**. The
load-bearing measures are `cue_zgoal_pull_norm` (~0.002) and `post_cue_approach_rate`
(== background).

## 3. Mechanistic root (repo-grounded)

`cue_recall_gain = 0.2` (config) × the weak stored token value (matched_token_strength
~0.2 from 638a, a forced-feed Stage-0 EMA of received benefit) → `GoalState.cue_pull`
applies `cue_recall_gain * clamp(wanting)` as a directional nudge, yielding the measured
~0.002 z_goal movement — ~3 orders of magnitude too small to redirect the committed
attractor. The **first link (cue → z_goal) is near-zero**; the **second link
(z_goal → approach via MECH-295 / E3 goal_proximity) cannot yet be tested** because z_goal
never moved enough to exercise it. This is the precise pair of links the cue-authority
sweep (§7) is designed to separate.

## 4. Biological-reference triage

Closest reference: cue-triggered incentive salience / sign-tracking / Pavlovian-
instrumental transfer (Berridge & Robinson incentive salience; Schultz DA-transfer-to-cue;
Corbit & Balleine specific PIT). In biology a Pavlovian cue acquires *substantial*
approach authority — a sign-tracker approaches and contacts the cue. The REE cue fires
(MECH-347 `cue_recall_wanting` executes and is logged 1557 times) but exerts ~0.4%
influence on the goal attractor. The biological existence proof says cue → approach
authority is real and strong; the REE translation has the recall event but the
cue → z_goal → approach **gain set ~3 orders too low** to produce behavioural authority.
This is a **magnitude / wiring gap (translation incomplete), not a falsification** of
cue-recall. It is a faithful-but-partial translation, not a formal-definition import.
claim_ids = [] → no governance weighting in either direction.

## 5. Multi-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | diagnostic, claim_ids=[]; no governance weighting |
| Biological reference | clear (magnitude gap) | sign-tracking / PIT; cue → approach authority is real and strong in biology; REE gain set ~3 orders too low |
| Developmental / dependency prereqs | present (formation + recall) / under-gained (authority) | Stage-0 token formation works (638a), cue recall fires (640); the cue → z_goal pull gain is the missing strength |
| Implementation completeness | present-but-under-powered | `GoalState.cue_pull` + MECH-347 wired and firing; pull magnitude ~3 orders too small to move the attractor |
| Environment adequacy | adequate | CausalGridWorld 4-dir approach; ARM_OFF reaches contact, so the env supports it |
| **Measurement adequacy** | **resolved (was the 638a gap)** | 640 captured the post-cue z_goal/approach trace 638a lacked — this is why 640 PASSed C1/C2 |
| **Integration adequacy** | **near-zero coupling (dominant gap)** | cue fires hard but its effect on z_goal (~0.4%) and on approach (== background) is negligible |
| Scale / capacity | likely insufficient | cue_recall_gain 0.2 × token value ~0.2 → sub-threshold pull |

**Recommended `epistemic_category`:** n/a for governance (claim_ids=[]); for the finding,
this is a **behavioural diagnostic / integration-and-gain gap**, not a substrate_ceiling
and not a falsification.

## 6. Learning extracted

- 640 resolves the 638a un-discriminated branch at the action-trace resolution:
  **cue-to-action authority is missing** (grid row 1), **displacement is refuted**, the cue
  is **inert not counterproductive**, and the **interoceptive reading is not the proximate
  cause** (seed 42 depleted-yet-firing-yet-flat).
- The cue → z_goal link is near-zero (~0.4% nudge); the z_goal → approach link is
  *untestable until z_goal actually moves*. The next experiment must move z_goal a
  measurable amount to separate the two.
- 638b interoceptive build remains correctly gated: Layer-2 meaning on a cue with no
  Layer-1 authority is premature, now confirmed with the action trace (not just inferred).

## 7. Repair pathway (routing) — confirmed with user

**Routing: `/queue-experiment` — cue-authority strengthening diagnostic, gating 638b.**

Smallest next step (NOT yet queued; goes through /queue-experiment): re-run the
behaviourally-instrumented ablation with a **`cue_recall_gain` sweep** (and/or a stronger
seeded token), so z_goal is pulled a *measurable* amount, then re-measure
`post_cue_approach_rate` against background. Discriminator for the successor:

| Successor result | Read | Next route |
|---|---|---|
| z_goal pull rises with gain AND post-cue approach lifts above background | cue → z_goal → approach bridge works, was under-gained | promote the authority bridge; THEN consider 638b interoceptive |
| z_goal pull rises with gain BUT approach stays flat | the z_goal → approach link (MECH-295 / E3 goal_proximity) is the real gap | diagnose that link before 638b |
| z_goal pull does not rise even at high gain | cue_pull mechanism itself under-powered / clipped | substrate-level cue-authority bridge revisit |

`recommended_substrate_queue_entry.action = "none"` — the `cue_pull` and approach pathways
already exist; this is a gain / parameter question on the existing substrate, not a new
primitive. **No demotion** (claim_ids=[]). **No Berridge/Toates/Cabanac Layer-2 lit-pull
yet** (still the Layer-1 authority question; the interoceptive pull is a prerequisite only
IF the successor routes to interoceptive). The 638a-named `targeted_review_object_bound_incentive_salience`
still does not exist and is not needed yet.

## 8. Do-not-do-yet (V3 scope-creep guards)

- Do NOT build the 638b interoceptive need-gating substrate yet (640 confirms the cue lacks
  Layer-1 behavioural authority — gate 638b behind the cue-authority sweep result).
- Do NOT build orienting/surveying mode, safe-gradient-following primitive, hazard-clearance
  scaffold, four-direction forced-choice env, stable->moving curriculum, or safe-weaning
  scaffold — none justified until the authority sweep says the bridge works.
- Do NOT read `n_cue_action_bias_present=0` as the finding (SD-016 channel, expected-absent;
  see §2 caveat).
- Do NOT tune to pass; the sweep MEASURES the gain → authority relationship, it does not
  hunt for a passing config.
- Do NOT activate ARC-063 CandidateRuleField as the nursery-to-forager fix (V3-EXQ-639 is
  substrate-readiness only; the bottleneck is the cue-authority gain, upstream of rule
  apprehension).

## 9. Cross-references

- failure_autopsy_V3-EXQ-638a_2026-06-05.{md,json} (the FAIL whose un-discriminated branch
  640 measured; Sections 7-8 prescribed 640; 640 REFUTES that autopsy's Section-3
  displacement hypothesis and CONFIRMS its branch-1 cue-to-action authority ranking).
- failure_autopsy_V3-EXQ-638_2026-06-04.{md,json} (predecessor formation autopsy).
- thought_intake_2026-06-04_cue_ecology_weaning_nursery_to_forager.md (Layers 1/2; 638b
  plan; the working read there carries the displacement hypothesis as branch (b) — now
  refuted by 640; left to /governance to reconcile per the confirmed disposition).
- ree-v3 goal.py `GoalState.cue_pull` + `IncentiveTokenBank`; agent.py
  `cue_recall_wanting` (MECH-347 L6); cue_recall_gain config (0.2).
- ree-v3 CLAUDE.md SD-016 entry (EXP-0155 / V3-EXQ-449 — the ungrounded cue_action_proj
  channel that `n_cue_action_bias_present=0` reflects).
- goal_pipeline:GAP-2 (foraging-contact ceiling), GAP-7 (object-bound incentive salience,
  SD-057).
