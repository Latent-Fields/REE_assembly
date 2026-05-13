# Thought Intake: Calibration Debt Map for REE-v3
**Date:** 2026-05-13  
**Status:** Cross-substrate calibration intake / project-unblocking map  
**Scope:** Landed or partly landed substrates whose next progress may come less from new architecture and more from calibration, diagnostic sweeps, gate checks, read-side wiring, and behavioural effect-size testing.  
**Related repositories:** `Latent-Fields/ree-v3`, `Latent-Fields/REE_assembly`  
**Related clusters:** goal pipeline, ARC-065 behavioural diversity, MECH-320 tonic vigor, sleep substrate, ARC-062 rule apprehension, SD-049 / SD-015 resource-goal pathway, MECH-295 approach bridge.
---
## 1. Core intake
A significant part of the project may now be sitting in **calibration debt**.
This means:
the substrate has landed,
contract tests may pass,
local wiring may exist,
but the behavioural signal is zero, saturated, too small, mis-scaled,
or blocked by a gate / timing / measurement mismatch.

This is a different class of work from “invent the next mechanism.”

The current pattern across several plans is:

substrate exists
→ isolated tests pass
→ end-to-end behavioural effect is absent or weak
→ experiment is marked FAIL / weakens / non_contributory
→ likely next step is calibration, not conceptual abandonment

The goal-pipeline plan explicitly describes this pattern: the drive-to-approach pipeline has modules wired end-to-end, but the loop remains behaviourally inert; the plan says the fault is “at the seams, not in the components.”  ￼

The same style of problem appears in the sleep substrate plan, which says the sleep loop scaffolding landed end-to-end but read paths into it had not; several sleep experiments became non-contributory because waking behaviour lacked diversity for sleep to refine.  ￼

This suggests a new cross-project task:

Build a calibration map.
Prioritise already-landed substrates where tuning / sweep / read-side binding
could unlock multiple downstream claims.

⸻

2. Definition: calibration debt

A substrate enters calibration debt when at least one of the following is true:

1. Module exists but default flag leaves it silent.
2. Gate is open but signal remains zero.
3. Signal exists but effect size is too small.
4. Signal writes but is not read downstream.
5. Score-bias exists but action selection is unchanged.
6. Local contract tests pass but behavioural tests fail.
7. Metric is saturated at 0 or 1, making effect impossible to see.
8. Experiment uses mismatched action/no-op/stream conventions.
9. Thresholds were chosen conservatively and never swept.
10. Multiple substrates are active but relative weights are uncalibrated.

This category should be explicitly tracked in REE_assembly, because otherwise real mechanisms may be repeatedly misclassified as failed.

⸻

3. Highest-priority calibration targets

3.1 Goal stream / wanting / approach pipeline

Status: landed in pieces, behaviourally inert in several tests.
Priority: very high.
Reason: blocks goal-directed behaviour, resource-seeking, wanting/liking dissociation, approach side of basal ganglia analogue, and later ethical development.

Relevant substrate pieces:

SD-012 drive modulation
SD-015 resource encoder
SD-018 resource proximity supervision
MECH-216 schema wanting
MECH-295 drive → liking → approach bridge
MECH-307 anticipatory affect conjunction
ARC-030 approach/avoidance balance

Current failure pattern:

z_goal remains zero
approach_commit_rate remains zero
cue_fires remain zero
benefit contact is too sparse
drive may collapse at contact

The goal plan says the modules are wired, but end-to-end the loop repeatedly produces approach_commit_rate = 0, meaning the failure is likely seam/integration/calibration rather than missing substrate.  ￼

Calibration candidates

benefit_threshold
z_goal_seeding_gain
drive_weight
sustained_drive_ema_alpha
schema_wanting_threshold
schema_wanting_gain
VALENCE_WANTING write amplitude
E3 goal_weight
hippocampal wanting_weight
MECH-295 cue gain
dACC score-bias scale
MECH-307 conjunction gain

Next experiment family

Goal-stream calibration ladder:
1. forced z_goal injection
2. forced VALENCE_WANTING write
3. forced schema_salience
4. reactive resource-proximity wanting
5. predictive wanting
6. sustained-drive sweep
7. MECH-295 bridge sweep
8. full naturalistic run

Acceptance shape

Each rung should prove one seam:
write site works
read site works
score bias moves
action selection moves
resource contact occurs
z_goal seeds
replay consolidates

Suggested classification

Goal pipeline = calibration debt + seam-closure problem.
Do not add a new goal system until the existing signal ladder has been swept.

⸻

3.2 MECH-320 tonic vigor

Status: implemented, wired when enabled, contract-tested, behaviourally failed so far.
Priority: very high.
Reason: may be the primitive “do something rather than remain idle” substrate.

The module exists and is explicitly designed to bias action over no-op using a slow average-reward-rate signal. It is target-free and sits at the E3 score-bias seam.  ￼

The contract tests show that with use_tonic_vigor=True, the agent populates agent.tonic_vigor, a sense / propose / select tick runs, and the score-receipt update path advances.  ￼

But the behavioural discriminative pair V3-EXQ-549 failed:

ARM_OFF action_density mean = 0.5000
ARM_ON  action_density mean = 0.5000
paired lift = 0.0000
Pearson r(v_t, action_density) = 0.000
gate_product = 1.000
outcome = FAIL / weakens

The important clue is:

gates were open,
but v_t stayed zero.

￼

Calibration candidates

score-receipt sign
v_raw floor
tonic_vigor_floor
w_action
w_passive
bias_scale
half_life
noop_class mapping
action-density metric
selected-score scale
gate_energy_min
gate_drive_max
gate_pe_max

Immediate next test

Forced-vigor probe:
force v_raw = 1.0
or
set tonic_vigor_floor > 0
then check whether no-op candidates get positive bias
and action candidates get negative bias.

Interpretation

If forced vigor changes behaviour:
    downstream path works; score-receipt / v_raw generation is the issue.
If forced vigor does not change behaviour:
    score-bias composition, no-op mapping, or action-selection saturation is the issue.

Suggested claim status

MECH-320 = substrate-landed, behaviourally unvalidated, calibration-required.

⸻

3.3 ARC-065 behavioural diversity stack

Status: MECH-313 and MECH-314 substrate-landed; behavioural calibration still pending.
Priority: very high.
Reason: sleep and rule-apprehension experiments may be non-contributory until waking behaviour has enough diversity.

ARC-065 exists because monomodal-policy collapse repeatedly made experiments non-contributory. The synthesis concludes that behavioural diversity requires both structured curiosity and stochastic noise: neither alone is sufficient.  ￼

Current pieces:

MECH-313 stochastic noise floor
MECH-314 structured curiosity
MECH-314a novelty
MECH-314b uncertainty
MECH-314c learning progress
MECH-320 tonic vigor
MECH-260 anti-recency

MECH-313 raises softmax temperature. It is state-independent and prevents deterministic policy collapse.  ￼

MECH-314 adds curiosity-driven score bias, with novelty currently per-candidate and uncertainty / learning-progress still broadcast in Phase 1.  ￼

The rule-apprehension plan notes that MECH-313 and MECH-314 substrate-readiness diagnostics passed, but Q-043 / Q-044 / Q-045 ablation and calibration experiments remain to be authored.  ￼

Calibration candidates

noise_floor_alpha
noise_floor_min_temperature
curiosity_novelty_weight
curiosity_uncertainty_weight
curiosity_learning_progress_weight
curiosity_bias_scale
MECH-260 anti-recency weight
MECH-320 vigor floor / action bias
relative weighting among MECH-313 / MECH-314 / MECH-320 / MECH-260

Key experiment

Matched-entropy test:
ARM 0 baseline
ARM 1 MECH-313 noise only
ARM 2 MECH-314 structured curiosity
ARM 3 matched-entropy random noise
ARM 4 MECH-313 + MECH-314 + MECH-320

Acceptance

structured curiosity must produce more useful behavioural diversity
than matched entropy alone.

Metrics:

action_class_entropy
state_coverage
trajectory_diversity
rule-relevant transition count
hazard excess
commitment collapse
sleep-refinable variation

Suggested classification

ARC-065 = top-level calibration gate for many downstream experiments.
Until it is calibrated, sleep and rule-apprehension runs may remain non-contributory.

⸻

3.4 Sleep substrate

Status: major scaffold landed; several read paths / flags / driver patterns remain unresolved; one precision-calibration subproblem has already shown that calibration can work.
Priority: high.
Reason: sleep may be essential for consolidating goal, curiosity, rule, and self-attribution streams.

The sleep substrate plan says the sleep loop scaffolding has landed end-to-end, but read paths into it had not; it also notes Phase B-E master flags were default-false and the routing weights flipped without being consumed downstream.  ￼

MECH-204 precision recalibration is an instructive example. A step-size sweep initially failed overall because C4 did not meet the relative-divergence threshold, despite monotonic improvement with larger step sizes and no overshoot.  ￼

The sleep plan then records that a longer 16-cycle run, V3-EXQ-541c, passed all four criteria and led to a default recalibration step update from 0.1 to 0.25.  ￼

This is the clearest proof that calibration can move REE forward:

same substrate
→ better step size / exposure dose
→ behavioural criterion clears

Calibration candidates

rem_precision_recalibration_step
precision_zero_point_ema_alpha
sleep_loop_K
number_of_sleep_cycles
MECH-285 replay temperature
staleness replay weight
MECH-272 routing weights
MECH-275 posterior decay
MECH-273 offline learning rate
SWS / REM phase duration
sleep-entry frequency

Priority checks

1. Are Phase B-E flags on together in experiments?
2. Are routing weights consumed, not just logged?
3. Does replay-derived data replace synthetic offline targets?
4. Does sleep fire enough times to produce measurable dose-response?
5. Is waking behaviour diverse enough for sleep to refine?

Suggested classification

Sleep substrate = calibration + read-side-consumer + driver-frequency problem.
MECH-204 shows this class of work can convert a weak/failed run into a PASS.

⸻

3.5 ARC-062 rule apprehension / gated policy

Status: substrate landed, but behavioural divergence appears blocked by candidate indistinguishability and inert gating.
Priority: high.
Reason: rule apprehension depends on behavioural diversity, candidate distinguishability, and trainable gating.

The rule-apprehension plan says ARC-062 substrate landing is done, but the monomodal-collapse falsifier is blocked on CEM candidate distinguishability. It reports that V3-EXQ-543b found exact zero total-variation distance across seeds/windows/probe states and identified near-indistinguishable CEM candidates.  ￼

This may not be a classic “knob too low” problem. It may be a calibration-precondition problem:

the policy head cannot learn distinct rules
if all candidate inputs look nearly identical.

Calibration / precondition candidates

candidate-feature variance
first-action entropy
continuous-action L2 spread
world_states[1] pairwise distance
gated-policy bias scale
discriminator init scale
number of heads
head symmetry-breaking magnitude
training duration
MECH-313 / MECH-314 / MECH-320 diversity support

Next diagnostic

CEM-candidate-distinguishability substrate-readiness test:
measure whether candidates differ enough before asking ARC-062 to route rules.

If candidates remain indistinguishable

Possible routes:

1. augment gated-policy input with first-action features;
2. increase proposal diversity upstream;
3. activate ARC-065 diversity stack first;
4. redesign SD-054 or successor environment so rule-relevant candidate differences exist by construction.

Suggested classification

ARC-062 = not merely calibration of the gated-policy head;
it needs upstream candidate diversity calibration before behavioural testing is fair.

⸻

3.6 SD-015 / SD-049 resource identity and goal representation

Status: resource encoder exists; z_resource may be active, but its behavioural role and relative use versus z_world remain unsettled.
Priority: medium-high.
Reason: affects goal stream, wanting/liking, multi-resource identity, and later object-like goal representation.

The substrate queue records a complex SD-015 trajectory: early proximity regression worked, later z_goal seeding tests had measurement zeros, then correct wiring produced behavioural support in some wanting/liking and navigation contexts, but later EXQ-322a found z_world outperforming z_resource for goal alignment.  ￼

This suggests that calibration may not be “make z_resource stronger” alone. It may be:

learn when z_resource should supplement z_world
rather than replace it.

Calibration candidates

z_resource weight
z_world weight
hybrid seeding mixture
identity classifier loss weight
resource proximity loss weight
per-axis drive gain
goal_resource_r threshold
z_goal cluster readout temperature
resource-type classifier confidence threshold

Suggested experiment

Hybrid seed sweep:
z_goal_seed = a * z_resource + (1 - a) * z_world
where a ∈ {0.0, 0.25, 0.5, 0.75, 1.0}

Acceptance:

hybrid seeding should outperform pure z_world and pure z_resource
on resource relocation / identity recovery / wanting != liking measures.

Suggested classification

SD-015 = representational weighting calibration problem.
The question may be mixture, not replacement.

⸻

3.7 MECH-295 drive → liking → approach bridge

Status: isolation tests passed; cascade behavioural validation still not convincing.
Priority: medium-high.
Reason: likely bridge between primitive drive and action-directed approach.

The goal plan records that MECH-295 passed isolated substrate tests, but downstream cascade behavioural validation remained inert under realistic policy state.  ￼

Calibration candidates

cue activation floor
liking-stream gain
approach cue gain
drive multiplier
dACC bias weight
E3 score-bias scale
candidate summary construction
goal_proximity threshold

Suggested experiment

MECH-295 cascade ladder:
1. direct cue injection
2. direct liking-stream injection
3. drive-scaled liking injection
4. naturalistic resource-cue condition
5. lesion bridge

Acceptance:

Each step must produce monotonic movement in:
cue_fires
score_bias
selected trajectory
approach_commit
resource contact

Suggested classification

MECH-295 = cascade calibration problem.
Isolation PASS is not enough; it needs monotonic bridge-ladder validation.

⸻

4. Calibration priority ranking

Priority 1 — unblock many other claims

1. ARC-065 behavioural diversity stack
2. MECH-320 tonic vigor
3. Goal-stream wanting / z_goal seeding ladder
4. Sleep-substrate driver / routing / replay calibration

These are likely project multipliers.

Why:

without action/vigor/curiosity, waking behaviour is monomodal;
without behavioural diversity, sleep has little to refine;
without goal-stream activation, resource-seeking and approach remain inert;
without sleep calibration, rule and memory consolidation remain weak.

Priority 2 — close specific high-value seams

5. ARC-062 candidate distinguishability / gated-policy calibration
6. SD-015 hybrid z_resource/z_world seeding
7. MECH-295 approach bridge calibration
8. MECH-313 vs MECH-260 distinction

Priority 3 — later refinement after primary streams are alive

9. candidate-specific uncertainty curiosity
10. candidate-specific learning-progress curiosity
11. per-axis drive consumer cascade
12. sleep arousal-triggered entry
13. multi-strategy rule scaling

⸻

5. Proposed calibration framework

For each landed substrate, create a standard calibration_status block.

calibration_status:
  substrate_landed: true
  contract_tests_pass: true
  behavioural_effect_seen: false
  default_active: false
  gate_open_in_failed_run: unknown
  signal_nonzero_in_failed_run: unknown
  read_side_consumed: unknown
  effect_size_sweep_done: false
  saturation_checked: false
  sign_convention_checked: false
  identity_mapping_checked: false
  recommended_next_step: calibration_ladder

Add a corresponding calibration file per cluster:

evidence/calibration/goal_pipeline_calibration.md
evidence/calibration/arc065_diversity_calibration.md
evidence/calibration/mech320_vigor_calibration.md
evidence/calibration/sleep_calibration.md
evidence/calibration/rule_apprehension_calibration.md

⸻

6. Calibration ladder template

Each calibration should proceed in rungs:

Rung 0: module exists
Rung 1: flag on, no crash
Rung 2: internal signal non-zero
Rung 3: gate open
Rung 4: write-site fires
Rung 5: read-side consumes
Rung 6: score / latent changes
Rung 7: action or replay changes
Rung 8: behavioural metric changes
Rung 9: downstream claim becomes testable

Most recent failures can be reinterpreted by locating which rung failed.

Examples:

MECH-320:
    gate open, but v_t zero → Rung 2 failure.
Goal stream:
    update calls happen, z_goal zero → Rung 2/4 failure.
MECH-295:
    bridge works in isolation, cascade inert → Rung 5/6/7 failure.
Sleep:
    scaffold lands, routing weights not consumed → Rung 5 failure.
ARC-062:
    gated policy exists, candidates indistinguishable → pre-Rung 2 input-variance failure.

⸻

7. Suggested immediate work packages

Work Package A — Calibration registry

Create:

REE_assembly/evidence/calibration/calibration_debt_index.md

With rows:

claim_id
substrate_status
last_behavioural_experiment
failure_signature
likely_calibration_class
next_sweep
priority
downstream_unblocks

⸻

Work Package B — ARC-065 / MECH-320 combined heartbeat

Run:

baseline
noise only
curiosity only
vigor only
noise + curiosity
noise + curiosity + vigor

Primary output:

Does any combination reliably increase behavioural diversity
without random-walk collapse?

This should become the first calibration flagship.

⸻

Work Package C — Goal-stream ladder

Run forced-to-naturalistic sequence:

forced z_goal
forced VALENCE_WANTING
reactive wanting
predictive wanting
sustained drive
MECH-295 bridge
full naturalistic

This prevents another round of ambiguous zero-stream failures.

⸻

Work Package D — Sleep calibration and replay-readiness

Use MECH-204 as the positive exemplar:

step sweep
cycle-count sweep
routing-consumer check
replay-derived target check
waking-diversity precondition

Then retest sleep only after ARC-065 produces non-degenerate waking traces.

⸻

Work Package E — Rule-apprehension input distinguishability

Before rerunning ARC-062:

measure candidate variance
first-action entropy
world_states[1] separation
head-input separability

Only run rule-learning once the candidate substrate is distinguishable.

⸻

8. Candidate claim update

Several REE-v3 mechanisms should be marked as calibration-pending rather than failed.
A new evidence category should distinguish:
    substrate_not_landed,
    substrate_landed_contract_pass,
    calibration_pending,
    behaviourally_validated,
    behaviourally_failed_after_calibration.

This would prevent premature retirement of mechanisms that have passed substrate tests but not yet received adequate effect-size, timing, sign, threshold, or read-side-consumer calibration.

⸻

9. Bottom line

The project may have reached a new phase.

Earlier work was mostly:

Can we build the substrates?

The next phase may be:

Can we make the substrates speak to each other at the right strength,
at the right time,
through the right gates,
into the right consumers,
with enough behavioural variation to measure?

The likely high-yield move is therefore not another isolated mechanism.

It is:

a calibration and seam-closure programme.

The calibration debt map should become a standing artefact in REE_assembly.

Recommended first entry:

MECH-320 tonic vigor:
    substrate-landed;
    contract-tested;
    behavioural discriminative pair failed;
    gate open but v_t zero;
    next step = forced-vigor probe + no-op-class audit + tonic floor sweep.

Recommended second entry:

ARC-065 behavioural diversity:
    MECH-313 and MECH-314 substrate-landed;
    ablation and relative-weight calibration pending;
    required upstream for sleep and rule-apprehension experiments.

Recommended third entry:

Goal pipeline:
    multiple modules landed;
    approach loop inert;
    next step = forced-to-naturalistic signal ladder.

This reframes many current “failures” as useful diagnostics of where calibration has not yet been paid.

