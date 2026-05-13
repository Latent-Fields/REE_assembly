
# Thought Intake: Enabling the Goal Stream in ree-v3
**Date:** 2026-05-13
**Status:** Candidate implementation plan / integration intake
**Scope:** `ree-v3` goal stream, wanting/liking pathway, `z_goal` activation, resource-seeking behaviour, and behavioural validation.
**Related repositories:** `Latent-Fields/ree-v3`, `Latent-Fields/REE_assembly`
**Related claims / mechanisms:** SD-012, SD-014, SD-015, SD-018, SD-049, MECH-112, MECH-216, MECH-295, MECH-307, ARC-030, ARC-032, ARC-036, ARC-051.
---
## 1. Core intake
The current goal-stream problem should not be understood as absence of architecture. It should be understood as a **wired-but-inert loop**.
The ingredients for the goal stream already exist across the implementation and assembly documentation:
- homeostatic drive modulation;
- `z_goal` as a persistent latent attractor;
- resource encoding;
- resource proximity supervision;
- schema-based wanting;
- valence-field writing;
- hippocampal replay / proposal mechanisms;
- E3 trajectory scoring;
- beta-gated commitment;
- wanting/liking dissociation;
- drive-to-liking-to-approach bridge.
The problem is that these pieces do not yet reliably form a closed behavioural loop. The `goal_wanting_signal_chain.md` file explicitly identifies the bootstrap gap: `z_goal` is needed for approach, but approach is needed for resource contact, and contact is needed for `benefit_exposure`, which is currently the main trigger for `z_goal` seeding.  [oai_citation:0‡goal_wanting_signal_chain.md](https://scanner.topsec.com/?d=2120&r=show&u=https%3A%2F%2Fgithub.com%2FLatent-Fields%2FREE_assembly%2Fblob%2Fmaster%2Fdocs%2Farchitecture%2Fgoal_wanting_signal_chain.md&t=cd31ac712aae8f9d59f9373a363be95c12e68273)
This means the architecture is probably much closer to working than the behavioural failures imply. The failures are mainly **seam failures**, not conceptual failures.
---
## 2. Present diagnosis
### 2.1 The current loop
Current simplified chain:
```text
resource contact
→ benefit_exposure
→ drive-scaled benefit threshold
→ z_goal update
→ goal proximity scoring
→ approach behaviour

This is circular at cold start:

approach behaviour is needed to reach resources
but z_goal is needed to generate approach behaviour
but z_goal is only seeded after resource contact

Therefore, when random exploration does not produce enough resource contact, the goal stream remains zero.

The implementation confirms this: GoalState.update() decays z_goal each step, then only pulls it toward the current world latent when effective_benefit > benefit_threshold. effective_benefit is computed from benefit_exposure, z_goal_seeding_gain, and drive weighting.  ￼

2.2 Key failure signature

The repeated signature to watch for is:

update_z_goal calls > 0
but z_goal_norm_peak = 0
and approach_commit_rate = 0
and benefit_ratio = 0

This means the code path is being executed, but the stream is not functionally alive.

The goal_pipeline_plan.md names this overall condition directly: the drive-to-approach pipeline has its modules, and many pass unit or substrate-readiness tests in isolation, but the end-to-end loop still produces inert behavioural output.  ￼

⸻

3. Architectural interpretation

The goal stream should not be implemented as a reward scalar.

The correct Reflective–Ethical Engine formulation is:

predictive cue
→ wanting signal
→ valence terrain
→ hippocampal / E3 trajectory bias
→ beta-gated approach commitment
→ resource contact
→ liking / benefit signal
→ z_goal attractor seeding
→ replay consolidation

This preserves the distinction between:

Component       Trigger Function
Wanting cue / prediction / schema salience      motivates approach before contact
Liking  contact / benefit exposure      confirms value and seeds attractor
Goal    persistent latent target        stabilises repeated trajectory selection
Residue written valence history supports replay, path memory, and future proposal bias

The present architecture has liking-gated goal seeding. It now needs cue-gated wanting to become live.

⸻

4. Implementation plan

Phase 0 — Establish goal-stream observability

Before changing the architecture, create a standard diagnostic bundle for all goal-stream experiments.

Required metrics:

goal_norm
goal_norm_peak
n_z_goal_updates
n_effective_benefit_threshold_crossings
benefit_exposure_count
benefit_ratio
schema_salience_mean
schema_salience_histogram
schema_salience_threshold_crossings
VALENCE_WANTING_write_count
VALENCE_LIKING_write_count
total_VALENCE_WANTING_field_strength
cue_fires
dacc_bias
hippocampal_goal_branch_count
approach_commit_rate
resource_contact_rate

Acceptance for Phase 0:

Any goal-stream experiment must be classifiable as:
1. live contributory,
2. zero-stream non-contributory,
3. partial-stream seam failure,
4. downstream-action failure.

This prevents further false failures where a mechanism is judged behaviourally absent when its upstream signal never fired.

⸻

Phase 1 — Turn on the existing goal-stream components together

Run a minimal “heartbeat” configuration where the relevant switches are deliberately enabled together.

Candidate configuration:

z_goal_enabled = True
use_resource_encoder = True
use_resource_proximity_head = True
schema_wanting_enabled = True
valence_enabled = True
goal_weight > 0
wanting_weight > 0
drive_weight = 2.0
z_goal_seeding_gain = 1.0

This phase should not be used to claim success. It is only to confirm whether the existing path can produce non-zero stream activity.

Acceptance:

schema_salience_threshold_crossings > 0
VALENCE_WANTING_write_count > 0
total_VALENCE_WANTING_field_strength > 0
hippocampal / E3 scoring reads wanting field
approach_commit_rate detectably non-zero in at least one permissive condition

Failure interpretation:

If schema_salience fires but VALENCE_WANTING is zero:
    write-site failure.
If VALENCE_WANTING writes but hippocampal/E3 scores unchanged:
    read-side consumer failure.
If scores change but actions do not:
    commitment / policy / beta-gate failure.
If contact occurs but z_goal remains zero:
    benefit-threshold / drive-collapse failure.

⸻

Phase 2 — Add predictive wanting as the cold-start breaker

The key amendment is to let wanting fire before contact.

Canonical pathway:

E1 schema salience
→ predicted future resource encounter
→ VALENCE_WANTING write
→ hippocampal / E3 trajectory preference
→ resource approach

The supervision target for schema wanting should shift from merely detecting current resource proximity to predicting future resource encounter.

Candidate training target:

future_resource_encounter_N =
    1 if resource contact occurs within next N steps
    0 otherwise

Recommended initial N:

N = 5, 10, 20 step sweep

Acceptance:

corr(schema_salience, future_resource_encounter_N)
    > corr(schema_salience, current_resource_proximity)

and:

schema_salience fires before contact
VALENCE_WANTING writes before contact
approach_commit_rate rises before z_goal is seeded

This implements the missing “appetite before food-in-mouth” pathway described in the goal-chain analysis.  ￼

⸻

Phase 3 — Add reactive wanting as an ablation, not the canonical route

There is already a resource-proximity prediction output from the resource encoder. The goal-chain document notes that this is computed and trained but not consumed downstream as a behavioural drive signal.  ￼

Use it as a diagnostic arm:

resource_prox_pred_r
→ VALENCE_WANTING write
→ trajectory bias

This should be marked as reactive wanting, not predictive wanting.

Purpose:

If reactive wanting works but predictive wanting does not:
    E1/schema prediction is the weak point.
If neither works:
    wanting read-side or action-selection path is the weak point.
If predictive wanting works and reactive wanting is weaker:
    architecture is behaving as intended.

This arm is useful because it gives a simpler signal path. It should not become the final architecture unless predictive wanting repeatedly fails.

⸻

Phase 4 — Implement sustained-drive memory

The GoalState.update() pathway currently depends on instantaneous drive at the moment benefit fires. The goal_pipeline_plan.md identifies a likely problem: drive can collapse at the point of resource contact because energy is restored, cancelling the intended amplification.  ￼

Add a sustained-drive exponential moving average.

Candidate implementation:

drive_ema = (1 - alpha) * drive_ema + alpha * current_drive
effective_drive = max(current_drive, drive_ema)

Initial sweep:

alpha = 0.01
alpha = 0.03
alpha = 0.05
alpha = 0.10
instantaneous-only baseline

Acceptance:

After deprivation, resource contact crosses benefit_threshold
even if instantaneous drive has collapsed at the contact step.

Expected result:

n_effective_benefit_threshold_crossings increases
z_goal_norm_peak becomes non-zero
z_goal persists after first contact

This is probably the smallest high-yield code change.

⸻

Phase 5 — Validate MECH-307 conjunction

The goal_pipeline_plan.md identifies MECH-307 as the load-bearing conjunction fix for the goal pipeline. It concerns signed anticipatory affect, coupling of schema wanting to affect/arousal, and writing at predicted rather than merely current locations.  ￼

Validation should use a lesion-style design:

Arm 0: baseline
Arm 1: predictive wanting only
Arm 2: predictive wanting + anticipatory liking/arousal
Arm 3: predictive wanting + anticipatory liking/arousal + predicted-location write
Arm 4: full conjunction
Arm 5+: each component lesioned from full conjunction

Acceptance:

Full conjunction:
    cue_fires > 0
    dacc_bias > 0
    approach_commit_rate > 0
    resource_contact_rate increases
    z_goal_norm_peak > 0 after contact
Lesioned arms:
    specific collapse pattern identifies required component.

The goal is not merely to show improvement. The goal is to show that the conjunction is necessary in the expected way.

⸻

Phase 6 — Retest MECH-295 drive → liking → approach bridge

Only after Phases 2–5 should the MECH-295 cascade be retested behaviourally.

The bridge has reportedly passed isolation tests, but the full cascade has remained inert. The plan document explicitly distinguishes isolated substrate success from cascade behavioural validation.  ￼

Retest conditions:

predictive wanting enabled
sustained drive enabled
MECH-307 conjunction enabled
canonical update order enforced
wanting read-side weights non-zero

Acceptance:

drive state modulates approach cue strength
approach cue strength modulates dACC / E3 score bias
score bias modulates selected trajectory
selected trajectory increases resource approach
resource contact seeds z_goal

Failure interpretation:

If bridge signal fires but score bias does not:
    MECH-295 → E3 seam failure.
If score bias changes but selected action does not:
    action-selection / beta-gate failure.
If action changes but resources are not reached:
    environment / policy / exploration failure.
If resources are reached but z_goal does not seed:
    GoalState threshold / sustained-drive / benefit_exposure failure.

⸻

Phase 7 — Defer broad consumer-cascade migration unless needed

The goal_pipeline_plan.md lists SD-049 Phase 3 consumer-cascade migration as deferred and lower priority. It is described as cleanup-of-substrate coverage rather than an acceptance-criterion prerequisite.  ￼

Do not begin with this.

Only migrate consumers to per-axis drive once the simpler scalar-drive loop is alive.

Trigger condition:

Goal stream works in scalar-drive setting
but fails in multi-resource / per-axis-drive setting.

Then migrate:

MECH-295 liking bridge
salience coordinator
dACC adaptive control
AIC urgency system
PCC metastability
pACC drive-bias system
override regulator

Each migration should preserve bit-identical behaviour when per-axis drive is disabled.

⸻

5. Minimal viable experiment sequence

Experiment A — Goal-stream heartbeat

Purpose:

Can any goal-stream activity be made non-zero with existing switches?

Acceptance:

VALENCE_WANTING_write_count > 0
schema_salience_threshold_crossings > 0
some detectable trajectory-score effect

⸻

Experiment B — Reactive wanting ablation

Purpose:

Can resource_prox_pred_r drive wanting if directly consumed?

Acceptance:

reactive wanting increases approach relative to baseline

Interpretation:

Positive result proves downstream wanting consumers can work.
Negative result points to read-side or action-selection failure.

⸻

Experiment C — Predictive wanting

Purpose:

Can E1 schema salience predict future resource encounter and write wanting before contact?

Acceptance:

schema_salience predicts future contact
wanting writes precede contact
approach_commit_rate increases

⸻

Experiment D — Sustained-drive sweep

Purpose:

Does drive memory allow benefit contact to seed z_goal?

Acceptance:

drive_ema arm produces more threshold crossings and non-zero z_goal_norm_peak

⸻

Experiment E — MECH-307 conjunction lesion test

Purpose:

Which anticipatory-affect components are required for behavioural activation?

Acceptance:

full conjunction works
lesions collapse in interpretable ways

⸻

Experiment F — MECH-295 cascade retest

Purpose:

Does drive now modulate approach through the liking bridge under realistic policy state?

Acceptance:

drive → cue_fires → dacc_bias → approach_commit → resource_contact → z_goal

⸻

6. Suggested implementation order for Codex / Copilot

1. Add standard goal-stream diagnostics.
2. Add experiment harness for heartbeat run.
3. Confirm canonical update order.
4. Add optional reactive_wanting_from_resource_prox_pred_r flag.
5. Add predictive future-resource-encounter target for schema_readout_head.
6. Add sustained_drive_ema to GoalState or GoalStreamState.
7. Add MECH-307 validation harness / lesion switches.
8. Retest MECH-295 cascade.
9. Only then consider per-axis-drive consumer migration.

⸻

7. Proposed branch names

feature/goal-stream-diagnostics
feature/reactive-wanting-ablation
feature/predictive-wanting-target
feature/sustained-drive-ema
experiment/mech307-goal-conjunction
experiment/mech295-cascade-retest

⸻

8. Candidate claim updates

Candidate update to SD-012

SD-012 should distinguish instantaneous depletion from sustained motivational drive.
The current drive multiplier is vulnerable to contact-time collapse when resource consumption restores energy before or during benefit-threshold evaluation. A sustained-drive trace is required for drive-scaled benefit seeding to remain behaviourally meaningful.

Candidate update to MECH-216

MECH-216 should be treated as the preferred cold-start route for goal-stream activation. Schema salience should be trained against future resource encounter, not only current resource proximity, so that wanting precedes liking/contact.

Candidate update to MECH-112

MECH-112 remains blocked until cue-triggered wanting and contact-triggered liking are both independently live and behaviourally dissociable.

Candidate update to MECH-295

MECH-295 should not be promoted on isolation tests alone. Promotion requires cascade evidence showing drive modulation propagates through cue bias into action selection and resource approach.

⸻

9. Key risk register

Risk    Meaning Mitigation
Zero-stream false failure       Experiment fails because upstream stream never fired    Mandatory diagnostics
Reward-function shortcut        Resource navigation is solved by scalar reward rather than REE pathway  Keep wanting/liking/residue/trajectory route explicit
Reactive wanting overfit        Agent learns visible-resource attraction but not predictive approach    Keep reactive wanting as ablation only
Drive collapse  Energy restoration cancels drive at contact     Sustained-drive exponential moving average
Read-side inertness     Wanting writes exist but are not consumed by E3/hippocampus     Separate write-side and read-side diagnostics
Commitment bottleneck   Scores change but actions do not        Inspect beta gate / policy / dACC path
Multi-resource premature complexity     Per-axis drive confounds basic stream activation        Defer SD-049 Phase 3 migration

⸻

10. Bottom line

The way forward is:

Do not invent a new goal system.
Do not add a reward shortcut.
Do not start with broad refactors.
First make the stream observable.
Then make wanting fire before contact.
Then preserve drive across contact.
Then prove that wanting writes are read by trajectory selection.
Then prove the approach bridge changes committed behaviour.
Then seed z_goal from successful contact.
Then allow replay and residue to consolidate the loop.

The gaps look completable because the missing work is mostly:

diagnostics
configuration
signal timing
write-side/read-side binding
sustained-drive memory
behavioural validation

rather than a missing conceptual substrate.

The goal stream is therefore best treated as an integration closure problem.
