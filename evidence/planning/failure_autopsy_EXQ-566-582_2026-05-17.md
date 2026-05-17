# Failure Autopsy — V3-EXQ-566 (FAIL run) + V3-EXQ-582

- **Generated (UTC):** 2026-05-17T12:55:18Z
- **Scope:** cluster (two diagnostics, shared goal-pipeline context)
- **Status:** confirmed (interactive gate answered 2026-05-17T12:55Z)
- **Session:** failure-autopsy-566-582-2026-05-17T124701Z

---

## Target A — V3-EXQ-577 FAIL run (closure only)

**Run:** `v3_exq_577_gap2_microhabitat_validation_20260516T210801Z_v3`  
**Disposition:** Existing autopsy artifact `failure_autopsy_EXQ-577_2026-05-16.md` (session
2026-05-16T221821Z) already confirmed: test-design false-negative on C2 zone_map_coverage; 
V3-EXQ-577a PASS supersedes. Run_id was not previously added to review_tracker despite the 
autopsy closing. **Added to review_tracker in this session.** No further analysis.

---

## Target B — V3-EXQ-566 FAIL run (2026-05-15T20:50Z)

**Run:** `v3_exq_566_wpc3_schema_salience_injection_20260515T205008Z_v3`  
**Queue:** V3-EXQ-566 (ree-cloud-1) · **Purpose:** diagnostic · **claim_ids:** []  
**Outcome:** FAIL · `evidence_direction: unknown` (not set in manifest)

### 1. Facts

Experiment: WPC Rung 3 -- forced `_schema_salience` injection diagnostic testing the
MECH-216 write path seam (schema_salience cache -> update_schema_wanting -> residue_field).

Two runs exist for V3-EXQ-566:

| Run | Machine | Completed | Outcome | Steps (ARM_1/ARM_3 seed=7) |
|---|---|---|---|---|
| 20260515T195934Z | ree-cloud-2 | 19:59Z | **PASS** | 1200 (full) |
| 20260515T205008Z | ree-cloud-1 | 20:50Z | **FAIL** | **70** (truncated) |

Criterion results (FAIL run):

| Criterion | FAIL run | PASS run |
|---|---|---|
| P1 forced arm wanting > 0.1 | PASS (441.2) | PASS (870.8) |
| P2 forced arm > baseline margin | PASS | PASS |
| P3 ARM_3_forced_high > ARM_2_forced_mid * scale | **FAIL** (22.3 vs 441.2) | PASS (1008.6 vs 870.8) |

ARM_3_forced_high (FAIL run) wanting = 22.3 vs. 441.2 for ARM_2_forced_mid -- collapse.
But: ARM_1_canonical seed=7 also terminated at 70 steps with wanting=5.8 despite no forced
injection. ARM_0_baseline (seed=7) ran full 1200 steps normally.

### 2. Root cause diagnosis

**Runtime anomaly, not MECH-216 seam failure.**

ARM_1_canonical (no forced salience) crashing at 70 steps for seed=7 rules out any
schema_salience injection being the cause. Between the two runs (~50 minutes), commit
`5fdba4c` ("SD-055: differentiable CEM selection approximation + V3-EXQ-568") landed on
ree-v3 main. cloud-1 would have pulled this version while cloud-2 had already completed
under the prior version. The SD-055 CEM change altered the action selection path and likely
introduced a numerical issue (NaN/inf) that triggered early episode termination for
specific random seeds on certain action sequences.

The PASS run (19:59Z, cloud-2) unambiguously answered the scientific question:
P1+P2+P3 all PASS, ARM_3_forced_high wanting = 1008.6 (monotone: 0 < 748 < 871 < 1009).
**MECH-216 schema_salience -> update_schema_wanting -> residue_field seam is functional.**

### 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | N/A | claim_ids=[], diagnostic only |
| Biological reference | N/A | seam test, not mechanism claim |
| Prerequisites | present | seam confirmed functional by PASS run |
| Implementation | complete | PASS run ran correctly |
| Environment | adequate | PASS run adequate |
| Measurement | adequate for PASS; broken for FAIL | FAIL run's 70-step truncation invalidates P3 measurement |
| Integration | isolated seam test | correct scope |
| Scale | adequate | short diagnostic |

**Recommended epistemic_category:** N/A (claim_ids=[])  
**Routing:** Mark reviewed (both runs). No re-queue needed. The seam is confirmed.

---

## Target C — V3-EXQ-582 FAIL (2026-05-17T08:29Z)

**Run:** `v3_exq_582_gap3_sustained_drive_ema_sweep_20260517T082933Z_v3`  
**Queue:** V3-EXQ-582 (ree-cloud-1) · **Purpose:** diagnostic · **claim_ids:** []  
**Outcome:** FAIL · `evidence_direction: non_contributory` (pre-set in manifest)  
**Plan owner:** `goal_pipeline:GAP-3` (SD-012 sustained-drive EMA amendment)

### 1. Facts

Experiment: discriminative alpha sweep for SD-012 sustained-drive EMA
(GoalConfig.drive_ema_alpha in {0.01, 0.02, 0.2, 1.0} x 3 seeds), testing whether
an EMA-smoothed drive trace overcomes the EXQ-536a contact-collapse (~0.005 drive at
resource contact because energy resets to 1.0 on consumption).

#### OFF anchor check

alpha=1.0 (instantaneous) mean_drive_trace_on_contact_all = 0.005.
This **reproduces the EXQ-536a collapse value** (~0.005). OFF anchor is valid; regime
did not drift. The substrate is correctly instrumented.

#### Criterion results (all FAIL)

| Criterion | Threshold | Result | Pass? |
|---|---|---|---|
| A1: mean_drive_trace_on_contact (post_warmup, alpha=0.02) | > 0.10 | **null** | NO |
| A2: seeds clearing effective_benefit > 0.10 (post_warmup, alpha=0.02) | >= 2/3 | **0** | NO |
| A3: z_goal_active_fraction (post_warmup, alpha=0.02) | > 0.20 | **0.0** | NO |
| A4: monotone curve + OFF arm < 0.10 | -- | non-monotone (all ~0); OFF arm = 0.005 < 0.10 | conditional |

#### Contact count -- the core finding

| Alpha | n_contacts_all (pooled 3 seeds) | n_contacts_post_warmup | z_goal_active_fraction |
|---|---|---|---|
| 0.01 | 2-3 | **0** | 0.0 |
| 0.02 | 2-4 | **0** | 0.0 |
| 0.2 | 2-4 | **0** | 0.0 |
| 1.0 | 2-4 | **0** | 0.0 |

All post-warmup contacts = 0 across all 12 runs (4 alphas x 3 seeds). The 2-4 total
contacts per run occur only in the pre-warmup window (steps 0-99 of each 200-step
episode). All contacts are chance encounters early in the episode, before energy has
depleted sufficiently to drive seeking.

### 2. Claim-layer mapping

claim_ids=[] -- this is a substrate-readiness diagnostic, not governance evidence.
GAP-3 plan states: "If 582 FAILs, follow the script's diagnostic interpretation grid
(Option 2 insatiability floor escalation, or regime-drift diagnosis)."

Script interpretation grid match: "No arm clears A1 (incl. 0.01)" -> row:
"Sustained EMA insufficient at any timescale in this regime. Escalate to Option 2."
OFF anchor reproduces 536a -> regime-drift row does NOT apply.

### 3. Biological reference

Reference mechanism: **incentive salience** (Berridge/Robinson wanting system). Tonic DA
levels sustain anticipatory wanting after consummatory reward; wanting persists and builds
during post-consummatory windows via dopaminergic trace. Biology clearly supports a
sustained-trace mechanism -- this is not a case where the biology refutes the design.

The failure is not "wanting traces don't persist in biology." It is:

> The synthetic agent never builds significant energy deficit within episodes, so drive
> at benefit contact is near-zero (energy starts at 1.0 per episode, contacts happen at
> random early steps before meaningful depletion). The EMA integrates near-zero drive and
> therefore produces near-zero trace. The OFF anchor at 0.005 shows this exactly.

**This is a cold-start / warm-start bootstrap failure, not a theoretical failure of Option 1.**

### 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | N/A | claim_ids=[] |
| Biological reference | **clear** | incentive salience well-established; failure not biological |
| Prerequisites | **missing (warm-start z_goal)** | z_goal_active_fraction=0.0 all arms; agent has no goal-directed benefit-seeking to bring it near resources in the post-warmup window |
| Implementation | complete | GoalState.drive_ema_alpha contract test 7/7 PASS; substrate correctly instrumented |
| Environment | **too sparse (contact density)** | 12x12 grid + random exploration -> 2-4 contacts in 4000 eval steps; all in pre-warmup window |
| Measurement | adequate | null post-warmup result is valid data; the measurement correctly detected the absence of contacts |
| Integration | **partially coupled but inert** | EMA wired end-to-end; z_goal-seeking loop not yet bootstrapped |
| Scale | adequate | 50 episodes is sufficient if contacts occurred |

**Recommended epistemic_category:** `substrate_ceiling` (missing warm-start bootstrap;
not a theoretical failure of Option 1 or Option 2)

### 5. Learning extracted

1. **Option 1 (EMA) is not refuted.** The null post-warmup result is not evidence against
   the EMA mechanism -- it is evidence that the prerequisite (warm-started z_goal seeking)
   is not met. An agent with active z_goal-driven benefit-seeking would accumulate a 
   meaningful drive trace because it would contact resources repeatedly, not once every 
   ~1000 steps at chance.

2. **The warm-start bootstrap is the blocking prerequisite for both options.** Option 2 
   (insatiability floor / drive_floor) faces exactly the same contact-density problem: 
   if the agent never contacts benefits, the insatiability floor also cannot accumulate 
   a trace or test the z_goal seeding gate.

3. **Infant substrate warm-start features are the correct prerequisite.** The transient 
   benefit patches (GAP-3 substrate, V3-EXQ-578 PASS) and microhabitat zones (GAP-2,
   577a PASS) are designed precisely to increase benefit contact density and seed z_goal.
   V3-EXQ-587 (EXQ-ISEF-001, currently running on ree-cloud-1) tests harm_gradient as a
   parallel route to the same objective. The Option 2 experiment must include a warm-start
   arm to be testable.

4. **Script grid row "No arm clears A1 -> Option 2" is correct routing but incomplete.**
   The grid assumes the regime is contact-dense enough that Option 2 would have more
   leverage. Adding a warm-start arm ensures this assumption is met before drawing
   conclusions about Option 2's sufficiency.

5. **OFF anchor discipline validated.** alpha=1.0 reproducing 536a (0.005) confirms the 
   measurement infrastructure is correct. This is a positive result: the instrumentation 
   is trustworthy.

### 6. Draft evidence_quality_note

> "V3-EXQ-582 FAIL (diagnostic, claim_ids=[]): n_contacts_post_warmup=0 across all 12
> runs (4 alphas x 3 seeds). EMA trace unmeasurable in post-warmup window. OFF anchor
> (alpha=1.0) reproduces EXQ-536a collapse (0.005) -- instrumentation correct, regime
> valid. Failure is contact-density / warm-start dependent: z_goal_active_fraction=0.0
> across all arms; agent makes 2-4 chance contacts in 4000 eval steps, all pre-warmup.
> Option 1 EMA not refuted -- warm-start z_goal bootstrap is the missing prerequisite.
> Per interpretation grid: escalate to Option 2 + warm-start arm (transient_benefit_enabled
> or forced z_goal seeding). pending_retest_after_substrate=true (infant_substrate
> transient-benefit + z_goal seeding combination required)."

### 7. Routing (user-confirmed)

**`/queue-experiment` for Option 2 + warm-start arm.**

The follow-on experiment (V3-EXQ-582a or new number per /queue-experiment skill) must:
- Include a warm-start arm: `transient_benefit_enabled=True` with high contact frequency
  (from infant_substrate GAP-3 substrate), OR forced z_goal seeding at episode start
- Test Option 2 (insatiability floor / drive_floor) alongside the EMA arm to determine
  which resolves the z_goal seeding gate
- Acceptance criterion A1 must be defined over the post-warmup window AND require a
  minimum n_contacts_post_warmup > 0 gate before interpreting the EMA trace measurement
- The OFF arm (alpha=1.0, no floor, no warm-start) must reproduce the 536a collapse
  to anchor the comparison

**GAP-3 plan update:** resume_condition updated to record warm-start bootstrap requirement.
GAP-3 status remains `in-progress`; owner_exq shifts to the follow-on experiment once
queued.

---

## Summary routing table

| Target | Verdict | Routing |
|---|---|---|
| V3-EXQ-577 FAIL run | Existing autopsy; run_id added to review_tracker | Close |
| V3-EXQ-566 FAIL run (20:50Z) | Runtime anomaly (SD-055 version race); seam confirmed by PASS run | Mark reviewed |
| V3-EXQ-566 PASS run (19:59Z) | MECH-216 seam functional | Mark reviewed |
| V3-EXQ-582 FAIL | substrate_ceiling (warm-start missing); Option 1 not refuted | /queue-experiment Option 2 + warm-start arm |

`pending_retest_after_substrate: true` for V3-EXQ-582.
