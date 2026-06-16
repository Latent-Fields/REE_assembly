# Failure Autopsy -- V3-EXQ-569h (ARC-065 GAP-A conversion-ceiling falsifier on the 684a STD_G2 conversion substrate)

**Generated:** 2026-06-16T19:37:30Z
**Scope:** single (lineage member -- 7th GAP-A conversion autopsy; see Section 7)
**Status:** confirmed (user adjudicated via AskUserQuestion 2026-06-16 -- "Amend + surface /claim-synthesis"; core read "Confirmed as stated")
**Target:** `v3_exq_569h_gapa_conversion_committed_action_falsifier_20260616T101100Z_v3`
**Queue id:** V3-EXQ-569h - **claim_ids:** [ARC-065] - **supersedes:** V3-EXQ-569g - **evidence_direction:** non_contributory
**Routing:** implement-substrate (amend `modulatory-bias-selection-authority`) **+ surface /claim-synthesis** (7th-autopsy granularity-debt recurrence; user-confirmed)
**Governance handoff:** the 2026-06-16T12:52Z governance cycle reviewed 569h, accepted non_contributory with NO ARC-065 weaken, and already appended the 569h failure_record to BOTH the `ARC-065` and `modulatory-bias-selection-authority` substrate_queue slots. This autopsy is the routed deep adjudication; it confirms `action: amend` (the slot exists, the record is present) -- do NOT create a duplicate substrate entry.

---

## 1. The adjudicated question

569h is the **real GAP-A committed-action-diversity falsifier** the 569g autopsy called for: ported onto the CONVERSION-armed selection-authority substrate (the `ARM_STD_G2` config -- `use_modulatory_channel_routing` + `candidate_summary_source=e2_world_forward` + `use_modulatory_selection_authority` + `authority_gain=2.0` + `authority_normalize_basis=std` -- identified by V3-EXQ-684a PASS as `conversion_mechanism_identified`), held constant on ALL arms. The single swept axis is `candidate_summary_source` + temperature.

It self-routed `conversion_ceiling_persists_despite_routing`. **Is that the right reading?**

**Verdict: yes, and it is the pre-registered OFF-RAMP, not a falsification.** The modulatory authority demonstrably reaches the select tick with genuine cross-candidate range (route_range 0.31, 3/3 seeds -- higher than 569g's 0.18, so the std-basis gain=2 amplified the reach), yet the committed-action distribution does not robustly diversify (1/3 seeds, needed 2/3). Signal present at the modulation layer; does not convert to committed-action diversity. This is a genuine substrate **conversion ceiling**, advanced one link past 569g (which proved REACH and isolated CONVERSION as the residual).

---

## 2. Facts (no interpretation)

Indexed via `summary.*_per_arm_mean` and the per-arm/per-seed `arm_results` (seed-major within arm).

**Arms (STD_G2 conversion config constant on all three):**

- `ARM_0_PROPOSER` -- `candidate_summary_source=proposer`, T=1.0 (collapsed-channel baseline; routed range ~0 by design)
- `ARM_1_E2WF_STD_G2` -- `candidate_summary_source=e2_world_forward`, T=1.0 (the 649 GAP-A fix routed + converted via STD_G2; **under test**)
- `ARM_2_MATCHED_NOISE` -- `candidate_summary_source=proposer`, T=2.5 (matched-entropy NEGATIVE control)

**Acceptance:**
`readiness_route_range_ready=TRUE`, `readiness_e2_divergent_ready=TRUE`, `readiness_substrate_ready=TRUE`, `negative_control_does_not_lift=TRUE`, **`C_R1B_selected_entropy_strict_above_both=FALSE`** -> `overall_pass=FALSE`. `non_degenerate=TRUE`. `criteria_non_degenerate={C1:true, C_R1B:true}`.

**Preconditions (both held, RANGE statistics, 3/3 seeds):**

| Precondition | floor | ARM_1 per-seed | mean | seeds-above | met |
|---|---|---|---|---|---|
| `arm1_modulatory_channel_route_range_supra_floor` (V3-EXQ-662 stat, live at select tick) | 0.01 | [0.316, 0.477, 0.136] | 0.309562 | 3/3 | TRUE |
| `arm1_e2_world_forward_prediction_spread_supra_floor` (cand_world_pairwise_dist; SD-056 trained) | 0.03 | [0.099, 0.137, 0.051] | 0.095262 | 3/3 | TRUE |

So the substrate **is** armed and reaching the accumulator in the scored arm -- not a wiring/training null.

**Discrimination (C_R1B = ARM_1 selected_action_class_entropy strict-above BOTH ARM_0 and ARM_2 on the same seed, >= 2/3 seeds):**

| seed | ARM_1 (e2wf STD_G2) | ARM_0 (proposer T=1.0) | ARM_2 (proposer T=2.5) | ARM_1 strict-above-both? |
|---|---|---|---|---|
| 42 | 0.874133 | 0.905132 | 0.905132 | NO (proposer already diverse: 5 classes) |
| 43 | 0.688620 | 0.000000 | 0.000000 | **YES** (proposer collapsed to 1 class; routing rescued it) |
| 44 | 0.790942 | 0.928613 | 0.928613 | NO (proposer already diverse: 3 classes) |

`arm1_seeds_strict_above_both = 1`; `min_seeds_for_pass = 2` -> **FAIL**.

`selected_action_entropy_per_arm_mean = {ARM_0: 0.611248, ARM_1: 0.784565, ARM_2: 0.611248}`. **The per-arm mean is misleading**: ARM_1's mean (0.785) sits above ARM_0/ARM_2 (0.611) ONLY because seed 43's proposer collapsed to entropy 0.0, dragging the control mean down. On the discrimination criterion that actually matters (same-seed strict-above-both), ARM_1 wins only the collapse seed.

**Failed criterion:** discrimination (`C_R1B`), scored on an arm whose enabling mechanism **is** active (route_range 0.31).

**Negative control note:** `ARM_2_MATCHED_NOISE` (proposer @ T=2.5) returned committed entropy **bit-identical to ARM_0** (proposer @ T=1.0) on all seeds -- temperature variance washed out by the F-dominated committed argmax. The manifest correctly frames this as the **confirmed 684/684a property** ("informational sanity only; does NOT gate the verdict"), not a control defect. Because ARM_2 == ARM_0, the strict-above-BOTH criterion reduces in practice to strict-above-proposer, which ARM_1 clears only in the collapse seed.

---

## 3. Why this is a conversion ceiling, not a wiring null -- and the decisive new datum

The decisive diagnostic nuance: **ARM_1 only wins in the one seed where the proposer baseline collapsed to a single action class** (seed 43: ARM_0/ARM_2 entropy 0.0, single class; ARM_1 = 0.689, 2 classes -- routing moved it 1 -> 2 classes). In seeds 42 and 44, where the proposer is already diverse (5 and 3 classes), the routed STD_G2 channel produces **slightly less** committed entropy than the un-routed proposer.

So the 684a-identified conversion config delivers a committed-argmax **SHIFT** but **not a diversity GAIN** over an already-diverse proposer: it rescues the collapse case but adds no *net* committed-action diversity beyond the proposer's own softmax sampling when the proposer isn't collapsed.

This is the load-bearing distinction between 684a (PASS) and 569h (FAIL):

- **684a criterion:** committed entropy strict-above-LEGACY (a single within-config comparison -- does turning the config on beat the legacy baseline). PASSed -- the config DOES move committed entropy vs legacy.
- **569h criterion:** committed entropy strict-above BOTH a collapsed-proposer AND a temperature-matched noise control on >= 2/3 seeds (a matched-entropy *discrimination*). FAILed -- the config does NOT add STRUCTURED committed diversity beyond proposer sampling in the non-collapsed regime.

684a measured "config moves committed entropy vs legacy" (true); 569h measures "config adds committed-action diversity GAIN over an already-diverse proposer" (false in 2/3). The residual gap is that the conversion is a shift, not a gain. Consistent with the 569g mechanism account: the authority is a gap-relative rescale operating against an F-dominated primary (V3-EXQ-571: F = 88-89% of E3 score variance), so even at gain=2.0 std-basis it can flip the committed argmax toward a different mode but cannot manufacture a more-diverse committed distribution than the proposer's intrinsic stochasticity already produces.

---

## 4. Claim-layer map

`claim_ids=[ARC-065]` (architectural_commitment, **provisional**, `epistemic_category=substrate_ceiling`, `v3_pending=false`, `depends_on: []`). Tag is **accurate and not inherited** -- single claim, re-evaluated for this run.

569h does **not** falsify ARC-065. Its diversity pathway (SP-CEM child, shared-channel consumption) demonstrably produces real upstream range (route_range 0.31, e2-divergence 0.095, both 3/3) -- positive evidence the **source exists**. The FAIL is on reach->committed-action **conversion**, not source existence. There is **no weakens path** in the design (the falsifier treats "diversity present + routed but not reaching committed action" as a CONVERSION CEILING by construction). Result correctly **non_contributory**; ARC-065 **unmoved / stays provisional**.

**Contamination guard (held):** MECH-341 GAP-B (E3 score-diversity preservation) is NOT active in this lineage (`use_e3_score_diversity=False`); tagging it would contaminate its record. ARC-062 / MECH-309 / MECH-294 untouched. Confirmed in config and manifest.

**Illusory-conflict-resolution guard:** ARC-065's remaining "supports" are narrow / single-pathway -- they are source-existence readiness probes (route-range reaches, e2 diverges). The committed-action-diversity DV has **never** passed. So the non_contributory recommendation is explicitly paired with `pending_retest_after_substrate=true`; it must NOT be read as resolving the GAP-A conversion conflict -- the conflict persists, the substrate is the named blocker.

---

## 5. Biological-reference triage

Mechanism class: a BG-like / cortico-striatal committed-action selection gate applying DA-modulated **gain/contrast** to convert small representational differences into a discrete choice, competing against a forward-model-dominated primary value.

- **Not a formal-definition import.** The conversion coupling is an engineering instantiation of a known biological dependency (BG gain modulation of action selection), not a Pearl/Shannon/optimal-control formalism imported as a mechanism.
- **Lit status: PRESENT for the generation source; the conversion gap is a known dependency, not a divergence.** `evidence/literature/targeted_review_arc_065_behavioral_diversity_generation` grounds the diversity-GENERATION side (LC-NE tonic noise floor, frontopolar uncertainty-driven curiosity; R1 verdict = both-channels-needed). It does NOT cover the reach->commit selection-coupling, because that is a substrate-engineering gap (how much a gain-rescaled additive/normalized bias can diversify a committed argmax against an F-dominated primary), not a question the biology literature would adjudicate differently.
- **Does the failure resemble a missing-dependency signature?** Yes -- it matches what would happen if a BG selection gate's gain were sub-dominant to a strong upstream value signal: the gate shifts choice at near-ties but cannot reweight the committed distribution toward diversity when the upstream sampler is already diverse. That is a discovered prerequisite (sufficient arbitration authority / a within-shortlist arbitration architecture), not a falsification.

**No `/lit-pull` warranted** -- consistent with the 569g finding.

---

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | source exists (route_range 0.31, e2-div 0.095, both 3/3); FAIL is on conversion, not falsification -> non_contributory; ARC-065 unmoved |
| Biological reference | clear / present | BG gain/contrast committed-action selection gate; conversion under-power is a known dependency, not a formal-import divergence; lit present (generation side); no lit gap |
| Developmental / dependency prerequisites | present | route-range substrate + STD_G2 selection authority armed AND active in the scored arm (3/3); SD-056 trained (e2 divergent 3/3) |
| Implementation completeness | **partial -- conversion is a SHIFT, not a diversity GAIN** | STD_G2 moves the committed argmax vs legacy (684a) but does not add net committed-action diversity over an already-diverse proposer; only rescues the collapse seed (1/3) |
| Environment adequacy | adequate | matched-noise + collapsed-proposer controls present; matched-noise washed out BY DESIGN (684/684a property), not a defect |
| Measurement adequacy | adequate (load-bearing) | C_R1B scored on an arm where the mechanism IS active (route_range 0.31); the negative is real, not an artefact; per-arm mean cross-checked against per-seed (mean is collapse-seed-inflated) |
| Integration adequacy | partially coupled | range reaches authority + shifts the argmax but conversion != committed-diversity gain vs the proposer |
| Scale / capacity | adequate | not budget/warmup (1/3-seed conversion + reach amplified to 0.31 rule it out) |

**Recommended `epistemic_category`:** `substrate_ceiling`. The shape is a substrate conversion ceiling (same class as the 569f-661-654a / 569g cluster), advanced to the post-identification link. Not `substrate_ceiling`-as-coarse-claim-only and not the V3-EXQ-642 precondition-unmet pattern (preconditions held 3/3 here).

---

## 7. Recurrence -- substrate iteration vs granularity debt (the open scientific question)

This is the **7th autopsy** circling the GAP-A channel->committed-action conversion:
569c -> 569e -> 614e -> 643 -> 569f-661-654a -> 569g -> **569h**.

The 569g autopsy (Section 7) firmly adjudicated the recurrence as **substrate iteration, NOT granularity debt** -- "ARC-065 is one architectural commitment, each amend fixed the next isolated link." That reading held through 569g because each amend genuinely fixed a distinct broken link (643 dead-gate -> 06-06 float32 cancellation -> 06-10 route-range reach).

**569h is the datum that re-opens the question.** It is the **first falsifier run AFTER the conversion config was supposedly *identified*** (V3-EXQ-684a PASS, `conversion_mechanism_identified`). The substrate-iteration thesis predicts that once the conversion config is identified and armed, the properly-armed falsifier should clear. It did not -- the identified STD_G2 config delivers a committed-argmax SHIFT but not a diversity GAIN, and the matched falsifier still converts 1/3. That **post-identification failure, with an evolving signature**, is exactly the granularity-debt recurrence fingerprint the autopsy skill flags: the broad ARC-065 "diversity generation pathway" commitment may not name the finer, distinct mechanism that keeps failing -- *committed-action diversity GAIN over an already-diverse proposer, against an F-dominated primary*, which is a separable testable function from *diversity generation* (source) and from *reach* (route-range).

**User adjudication (2026-06-16):** route BOTH -- `/implement-substrate amend` as the immediate substrate action (one residual architectural lever remains: shortlist-then-modulate, never run in a properly-armed falsifier with a verified-lifting noise control) **AND surface a `/claim-synthesis` recommendation** for proposal-first, lit-grounded decomposition of the GAP-A conversion cluster into testable children. The two are complementary: the amend tests whether one more substrate lever closes the conversion; the synthesis names the finer claim the recurrence implies if it does not.

---

## 8. Learning extracted

1. **CONVERSION is a committed-argmax SHIFT, not a committed-diversity GAIN.** The 684a-identified STD_G2 config (std-basis gain=2.0) reaches the select tick with even more range than 569g (0.31 vs 0.18) and moves the committed argmax vs legacy, but does not add net committed-action diversity over an already-diverse proposer -- it only rescues the collapse seed (1/3).
2. **684a PASS and 569h FAIL are consistent, not contradictory** -- they measure different things. 684a: "config moves committed entropy vs legacy" (true). 569h: "config adds committed diversity over a matched proposer + noise control" (false in 2/3). The identification diagnostic over-promised relative to the matched falsifier.
3. **Per-arm-mean is collapse-seed-inflated here.** ARM_1's mean entropy (0.785) clears ARM_0/ARM_2 (0.611) only because seed 43's proposer collapsed to 0.0. Always cross-check the discrimination claim against per-seed strict-above-both (1/3), never the aggregate mean (which would falsely read as a lift).
4. **The matched-noise control still does not lift** (ARM_2 == ARM_0 byte-identical) -- but this run correctly reframes that as the expected 684/684a F-dominance property (informational, non-gating), not a control defect. A successor falsifier should still prefer a noise control that demonstrably lifts, so structured-vs-noise is discriminable rather than collapsing to strict-above-proposer.
5. **The live levers remain authority STRUCTURE, not magnitude.** Upstream magnitude is range-renormalized away (667/640a flat); reach is solved (route_range 0.31); the residual is whether a within-shortlist arbitration (shortlist-then-modulate) can make the structured channel load-bearing without out-magnituding F. If it cannot, the recurrence is granularity debt, not iteration -- hence the dual route.
6. **SD-056 disconfirmed as the blocker for this lineage** (e2-divergence 3/3; C1 PASS). The blocker is the conversion arbitration, not the predictor.

---

## 9. Routing (user-confirmed: Amend + surface /claim-synthesis)

- **implement-substrate** (`action: amend` the existing `modulatory-bias-selection-authority` entry -- NOT create, NOT none). Governance already appended the 569h failure_record to this slot and to the ARC-065 slot on 2026-06-16; the amend should pursue the **one residual architectural lever** the 569g plan pre-registered but that has NOT yet been run in a properly-armed falsifier:
  - **shortlist-then-modulate arbitration:** F filters to a near-tie candidate set, then the modulatory channel arbitrates *within* it -- so the structured channel is load-bearing without having to out-magnitude the F-dominated primary. 684 ran a version at 0/3 inside its identification harness; it has NOT been run in the 569-lineage matched-entropy falsifier with the STD_G2 config + a verified-lifting noise control. That is the discriminating test.
  - The gain/contrast lever (a) is exhausted: 684a already identified gain=2.0 std-basis as the best gain/contrast config, and 569h shows it converts only the collapse seed.
- **surface /claim-synthesis** (recurrence-trigger, user-confirmed): 7th GAP-A conversion autopsy + first post-identification failure = granularity-debt signal. Hand the GAP-A conversion cluster (569c/569e/614e/643/569f-661-654a/569g/569h) to `/claim-synthesis` for proposal-first, lit-grounded decomposition. Candidate finer claim to put to the discrimination gate: **"committed-action diversity GAIN over an already-diverse proposer is a separable mechanism from diversity GENERATION (source) and from channel REACH (route-range); it is gated by the F-dominance ratio and requires within-shortlist arbitration, not a gain-rescaled additive/normalized bias on the global argmax."** This is testable (the shortlist-then-modulate amend IS its first falsifier), so it passes the synthesis non-vacuity gate. NOT a demotion -- ARC-065 is not wrong, it is coarse.
- **No claim demotions.** ARC-065 stays **provisional / non_contributory / `pending_retest_after_substrate`**. Cross-reference MECH-341 (within-class temperature lever shares this exact conversion bottleneck), ARC-062 / MECH-309 (rule-field channel), MECH-294 (coherence channel) -- one shared conversion fix; whichever the synthesis names becomes their shared finer child.

---

## Draft `evidence_quality_note` (for /governance -- do NOT write here)

> [2026-06-16 autopsy V3-EXQ-569h, confirmed]: 569h FAIL/non_contributory; ARC-065 unmoved (provisional, pending_retest_after_substrate). The GAP-A committed-action-diversity falsifier, ported onto the 684a-identified STD_G2 conversion substrate (use_modulatory_channel_routing + e2_world_forward summary + std-basis authority gain=2.0, ON all arms; supersedes 569g). Both non-vacuity preconditions HELD 3/3 (ARM_1 route_range 0.31 > 0.01 floor; e2-divergence cand_world_pairwise_dist 0.095 > 0.03 floor) -- the substrate IS armed and reaching the select tick (reach amplified vs 569g's 0.18). Discrimination FAILED: ARM_1 committed-action entropy strict-above BOTH the collapsed-proposer and the matched-noise (T=2.5) control on only 1/3 seeds (needed 2/3), and ARM_1 wins ONLY seed 43 -- the one seed where the proposer collapsed to a single action class. In the 2 seeds where the proposer is already diverse, ARM_1 entropy is slightly BELOW it. So the STD_G2 config delivers a committed-argmax SHIFT (consistent with 684a beating legacy) but NOT a committed-diversity GAIN over an already-diverse proposer -- a genuine substrate CONVERSION CEILING (signal reaches modulation layer, does not convert to committed-action diversity), NOT a falsification of ARC-065. Matched-noise control bit-identical to proposer (the confirmed 684/684a F-dominance property; informational, non-gating). Per-arm-mean (ARM_1 0.785 vs 0.611) is collapse-seed-inflated -- the per-seed strict-above-both (1/3) is load-bearing. Routed to /implement-substrate (amend modulatory-bias-selection-authority): the one residual lever is shortlist-then-modulate arbitration, never yet run in a 569-lineage matched falsifier with a verified-lifting noise control. ALSO surfaced /claim-synthesis: 7th GAP-A conversion autopsy + first post-identification (684a) failure = granularity-debt recurrence; candidate finer claim = "committed-action diversity GAIN over an already-diverse proposer is separable from diversity GENERATION and channel REACH, gated by F-dominance, requires within-shortlist arbitration." xref MECH-341/ARC-062/MECH-309/MECH-294 (one shared conversion fix). illusory-conflict guard: ARC-065's supports are narrow/single-pathway (source-existence probes only); committed-diversity DV has never passed -> conflict persists, substrate is the named blocker.
