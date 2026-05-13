# Thought Intake: Completing the Curiosity System in ree-v3
**Date:** 2026-05-13  
**Status:** Candidate completion plan / integration intake  
**Scope:** Curiosity, behavioural diversity, exploration, rule-apprehension preconditions, novelty, uncertainty, learning progress, stochasticity, tonic vigor.  
**Related repositories:** `Latent-Fields/ree-v3`, `Latent-Fields/REE_assembly`  
**Related claims / mechanisms:** ARC-065, MECH-313, MECH-314, MECH-314a, MECH-314b, MECH-314c, MECH-320, MECH-260, MECH-216, MECH-292, MECH-293, ARC-062, ARC-064.
---
## 1. Core intake
The curiosity system is already partly built. It should not be treated as an absent drive. It is better understood as a **substrate-landed but not yet closed-loop behavioural-diversity system**.
The repos already contain a named architectural cluster:
```text id="u1j96a"
ARC-065 behavioural-diversity-generation pathway

This cluster exists because repeated experiments became non-contributory when the agent collapsed into monomodal behaviour. Without behavioural diversity, top-down rule application and bottom-up rule discovery have too little behavioural variation to work from. The ARC-065 synthesis explicitly frames behavioural diversity as an upstream precondition for ARC-062 and ARC-064.  ￼

The current curiosity system has three major landed substrates:

MECH-313: stochastic noise floor
MECH-314: structured curiosity bonus
MECH-320: tonic vigor coupling

These should be completed as a coordinated drive family rather than as isolated policy tweaks.

⸻

2. Present architecture

2.1 ARC-065 behavioural diversity pathway

The ARC-065 literature synthesis concludes that behavioural diversity requires both:

structured curiosity
and
stochastic policy noise

not one or the other. Noise-only fails because it does not produce directed information-seeking. Curiosity-only fails because biological agents still have irreducible stochasticity.  ￼

Therefore the architecture should preserve two distinct axes:

Axis	Mechanism	Function
Stochasticity	MECH-313	keeps action-selection entropy from collapsing
Structured curiosity	MECH-314	biases candidates toward novelty, uncertainty, or learning progress
Vigor	MECH-320	biases toward action rather than no-op when action has recently been profitable

The shape is already good. The completion task is to make it behaviourally alive, measurable, calibrated, and integrated with memory/replay.

⸻

2.2 MECH-313 stochastic noise floor

MECH-313 raises the softmax temperature used by E3 trajectory selection. It does not prefer any specific candidate; it prevents deterministic collapse.  ￼

Current form:

effective_temperature =
    max(baseline_temperature + noise_floor_alpha,
        noise_floor_min_temperature)

Architectural role:

prevent total policy collapse
preserve low-level behavioural variability
allow exploration among alternatives

Completion need:

calibrate magnitude
show that it increases diversity without destroying commitment
distinguish it from MECH-260 dACC anti-recency

Here, dACC means dorsal anterior cingulate cortex analogue.

⸻

2.3 MECH-314 structured curiosity

MECH-314 is the main curiosity module. It acts at the E3 candidate-scoring seam, adding a score bias that makes curiosity-relevant candidate trajectories more attractive. It is explicitly split into three sub-flavours.  ￼

Current sub-flavours:

MECH-314a: novelty curiosity
MECH-314b: uncertainty curiosity
MECH-314c: learning-progress curiosity

MECH-314a novelty

Current implementation:

candidate first-step z_world
→ distance from active residue-field centres
→ novelty score
→ per-candidate score bias

This is the most mature part because it is genuinely per-candidate in Phase 1.  ￼

MECH-314b uncertainty

Current implementation:

E3 running variance
→ global uncertainty scalar
→ broadcast score bias across candidates

This exists, but it is not yet candidate-specific. The code itself states that per-candidate refinement is deferred to Phase 2.  ￼

MECH-314c learning progress

Current implementation:

exponential moving average of |prediction_error_t - prediction_error_t-K|
→ broadcast score bias across candidates

This also exists, but is currently global rather than candidate-specific.  ￼

⸻

2.4 MECH-320 tonic vigor

MECH-320 is not curiosity itself, but it is a necessary sibling drive. It biases toward action rather than no-op based on a slow exponentially weighted moving average of realised E3 score receipt.  ￼

Its role:

curiosity says:
    this candidate may be worth exploring
vigor says:
    act rather than remain passive
noise floor says:
    do not collapse into a single deterministic policy

Completion of curiosity probably requires all three.

⸻

3. Diagnosis

The curiosity system is currently:

architecturally coherent
code-substrate landed
contract-tested
partly wired into E3 selection
but not yet proven as a closed behavioural drive

The main gap is not “make a curiosity module.” That already exists.

The main gap is:

make curiosity create useful behavioural diversity
without becoming mere noise,
without destabilising commitment,
and without collapsing into reward-seeking or novelty addiction.

The contract tests show strong substrate-level readiness. They check default-off no-op behaviour, independent sub-flavour firing, additive composition, simulation-mode gating, and backward compatibility across configuration combinations.  ￼

But substrate readiness is not the same as behavioural completion.

⸻

4. Completion plan

Phase 0 — Define curiosity-stream observability

Before modifying mechanisms, standardise diagnostics.

Required metrics:

policy_entropy
action_class_entropy
trajectory_diversity
unique_state_visitation_count
state_coverage
residue_field_n_active_centres
mean_candidate_novelty
max_candidate_novelty
curiosity_bias_max_abs
curiosity_subflavours_fired
noise_floor_effective_temperature
tonic_vigor_v_t
no_op_rate
action_rate
commitment_rate
beta_gate_release_rate
prediction_error_mean
prediction_error_variance
learning_progress_signal
resource_contact_rate
hazard_contact_rate
rule-relevant transition count

Acceptance:

Every curiosity experiment must distinguish:
1. no-stream condition,
2. noise-only exploration,
3. structured curiosity,
4. vigor-driven action,
5. combined behavioural-diversity pathway,
6. destabilised / chaotic exploration.

Without this, behavioural PASS/FAIL results will remain ambiguous.

⸻

Phase 1 — Prove the existing system can increase behavioural diversity

Run a clean five-arm experiment:

ARM 0: baseline
ARM 1: MECH-313 noise floor only
ARM 2: MECH-314 structured curiosity only
ARM 3: MECH-320 tonic vigor only
ARM 4: MECH-313 + MECH-314 + MECH-320

Primary acceptance criteria:

ARM 4 > ARM 0 on action_class_entropy
ARM 4 > ARM 0 on state_coverage
ARM 4 > ARM 0 on trajectory_diversity
ARM 4 does not catastrophically reduce task viability
ARM 4 produces more rule-relevant transition records

Key interpretation grid:

If ARM 1 increases entropy but not useful coverage:
    noise floor works but is insufficient.
If ARM 2 increases novelty-directed visitation:
    structured curiosity is behaviourally live.
If ARM 3 reduces no-op collapse:
    vigor is behaviourally live.
If ARM 4 outperforms all single arms:
    ARC-065 combined pathway is supported.
If ARM 4 is chaotic:
    weights are too high or gating is missing.

This is the immediate “heartbeat” test for curiosity.

⸻

Phase 2 — Calibrate relative weights

The literature synthesis explicitly leaves magnitude calibration unsettled.  ￼

Run a parameter sweep over:

noise_floor_alpha
noise_floor_min_temperature
curiosity_novelty_weight
curiosity_uncertainty_weight
curiosity_learning_progress_weight
curiosity_bias_scale
tonic_vigor_w_action
tonic_vigor_w_passive
tonic_vigor_bias_scale

The goal is not maximal entropy. The goal is:

maximal useful behavioural diversity
under preserved commitment and survivability

Candidate composite score:

diversity_score =
    action_class_entropy
  + state_coverage
  + rule_relevant_transition_count
  - hazard_excess_penalty
  - commitment_collapse_penalty
  - random_walk_penalty

Acceptance:

Identify a stable low, medium, and high curiosity profile.

Suggested named profiles:

curiosity_low
curiosity_default
curiosity_high
curiosity_stress_test

These should become reusable experiment presets.

⸻

Phase 3 — Make uncertainty curiosity candidate-specific

Current MECH-314b uncertainty is a broadcast scalar. That is acceptable as a Phase 1 substrate but incomplete as curiosity.

Completion target:

candidate trajectory
→ predicted future latent sequence
→ uncertainty estimate per candidate
→ candidate-specific uncertainty curiosity bonus

Possible implementation routes:

Option A — E1 forward-variance head

Add an E1 variance readout:

E1 predicts candidate future z_world
E1 also estimates uncertainty / variance
candidate_uncertainty[i] = predicted variance along candidate i

Option B — ensemble or dropout approximation

Use repeated candidate rollouts:

same candidate
→ multiple stochastic forward predictions
→ variance across predictions

Option C — residue-field uncertainty proxy

Use regional familiarity:

low residue density
or high stale-anchor uncertainty
→ higher uncertainty curiosity

Recommended order:

start with Option C as cheap proxy
then add Option A as canonical E1-based uncertainty

Acceptance:

MECH-314b produces different bias values across candidates
and candidate-specific uncertainty predicts future prediction error.

⸻

Phase 4 — Make learning-progress curiosity candidate-specific

Current MECH-314c learning progress is also broadcast. It says, globally, “learning seems to be happening,” but not “this candidate is learnable.”

Completion target:

candidate trajectory
→ expected prediction-error reduction
→ learning-progress estimate
→ candidate-specific learning-progress bonus

Possible implementation:

For each region / anchor / trajectory class:
    maintain prediction-error history
    compute local learning-progress slope
    bias candidates toward regions where error is falling but not yet solved

This avoids two bad extremes:

Bad attractor	Meaning
Boredom trap	agent ignores learnable uncertainty too early
Noise trap	agent chases irreducible error forever

Candidate formula:

learning_progress(region) =
    previous_error_ema(region) - current_error_ema(region)

Curiosity should be highest when:

error is still present
and
error is decreasing

not when error is merely high.

Acceptance:

MECH-314c favours compressible novelty over irreducible noise.

Critical falsifier:

If the agent repeatedly visits stochastic/noisy regions with no model improvement,
learning-progress curiosity is mis-specified.

⸻

Phase 5 — Add curiosity residue / curiosity memory

At present, curiosity acts mostly at candidate scoring. A fuller REE drive should leave memory traces.

Add a curiosity-specific residue channel or tag.

Candidate additions:

VALENCE_NOVELTY
VALENCE_UNCERTAINTY
VALENCE_LEARNING_PROGRESS

or, if avoiding new valence channels:

curiosity_tag on ResidueField updates
curiosity_payload on AnchorSet
curiosity_priority in replay sampler

A conservative route:

Do not add permanent valence channels first.
Instead add curiosity metadata to residue / anchor writes.

Curiosity payload could include:

novelty_at_visit
uncertainty_at_visit
learning_progress_at_visit
prediction_error_before
prediction_error_after
visited_step
region_key
candidate_id

Acceptance:

Curiosity-driven visits become available to replay and sleep.
Replay can distinguish:
    useful exploration,
    useless random wandering,
    dangerous exploration,
    resolved familiar territory.

This is the point where curiosity begins to become a true REE stream rather than a policy regulator.

⸻

Phase 6 — Wire curiosity into hippocampal proposal generation

Current curiosity affects candidate scoring. It should also influence candidate proposal.

Add curiosity to hippocampal proposal generation:

known goal proposals
ghost-goal proposals
safety proposals
novel-region proposals
uncertain-region proposals
learning-progress proposals

This should be a minority branch, not dominant.

Candidate allocation:

70% ordinary proposals
10% novelty proposals
10% uncertainty proposals
10% learning-progress proposals

Then sweep.

Acceptance:

Curiosity increases the diversity of proposed candidates,
not only the scoring of already-proposed candidates.

This matters because score bias cannot select a curiosity-relevant trajectory if no such trajectory is proposed.

⸻

Phase 7 — Add boredom / satiation control

A mature curiosity system should not keep sampling the same once-novel thing forever.

Add curiosity satiation:

novelty decays with repeated visit
uncertainty decays with successful prediction
learning-progress decays when error plateaus

Candidate boredom signal:

boredom(region) =
    repeated visitation
  + low prediction-error improvement
  + low novelty

Effect:

decrease curiosity bonus for saturated regions
increase search for alternative regions

Acceptance:

Agent leaves a now-familiar region after learning saturates.
Agent does not perseverate on solved novelty.

This connects naturally to the existing boredom review if that claim remains active.

⸻

Phase 8 — Add danger-aware curiosity gating

Curiosity cannot simply override harm avoidance.

Add gating from harm streams:

if z_harm_a high:
    reduce curiosity dominance
    preserve urgent avoidance
if z_harm_s predicts manageable hazard:
    allow cautious exploration
if uncertainty is high and harm is high:
    prefer information-gathering from safe distance

This gives three curiosity modes:

free exploration
cautious exploration
suppressed exploration

Acceptance:

Curiosity increases exploration of safe uncertainty
but does not increase catastrophic hazard contact beyond threshold.

Important distinction:

curiosity should explore uncertainty;
it should not be blind risk-seeking.

⸻

Phase 9 — Integrate curiosity with sleep and consolidation

Curiosity-driven experiences should become privileged candidates for offline processing.

Sleep replay priority should include:

high novelty
high uncertainty
high learning-progress
high prediction-error reduction
unresolved prediction-error
high behavioural consequence

Candidate replay priority:

replay_priority =
    staleness
  + unresolved_uncertainty
  + learning_progress
  + novelty
  + consequence_weight

Expected sleep functions:

distinguish true rules from accidental novelty
downgrade irreducible noise
strengthen useful schemas
update residue familiarity
reduce curiosity for now-explained regions
preserve curiosity for unresolved but promising regions

Acceptance:

After sleep:
    repeated useless exploration decreases
    useful rule-relevant exploration increases
    prediction error in learnable regions falls

This is where curiosity becomes developmentally important rather than merely exploratory.

⸻

Phase 10 — Connect curiosity to rule apprehension

ARC-065 exists partly to unblock ARC-062 and ARC-064.

The sequence should be:

curiosity creates behavioural diversity
→ behavioural diversity creates varied trajectory records
→ bottom-up rule discovery can cluster patterns
→ top-down rule application has contexts to discriminate
→ sleep consolidates candidate rules

Acceptance:

With ARC-065 off:
    rule discovery receives monomodal records.
With ARC-065 on:
    rule discovery receives separable behavioural clusters.
With ARC-065 too high:
    records are noisy and unstable.
With calibrated ARC-065:
    records support rule extraction.

This is probably the most important behavioural validation.

⸻

5. Minimal experiment sequence

Experiment A — Curiosity heartbeat

Question:
    Does the existing curiosity stack produce non-zero behavioural diversity?
Arms:
    baseline
    noise only
    curiosity only
    vigor only
    combined
Primary metrics:
    action_class_entropy
    state_coverage
    trajectory_diversity
    no_op_rate
    commitment_rate

⸻

Experiment B — Sub-flavour independence

Question:
    Do novelty, uncertainty, and learning progress have separable behavioural effects?
Arms:
    novelty only
    uncertainty only
    learning progress only
    novelty + uncertainty
    novelty + learning progress
    uncertainty + learning progress
    all three

Expected:

novelty → unfamiliar regions
uncertainty → high prediction-error regions
learning progress → learnable-but-not-solved regions

⸻

Experiment C — Noise versus structured curiosity

Question:
    Is MECH-314 doing more than raising entropy?
Arms:
    matched entropy noise floor
    structured curiosity
    combined
Acceptance:
    structured curiosity produces more rule-relevant transitions
    at matched policy entropy.

This is crucial.

⸻

Experiment D — Candidate-specific upgrade test

Question:
    Does per-candidate uncertainty / learning-progress improve over broadcast scalar versions?
Arms:
    broadcast uncertainty
    candidate-specific uncertainty
    broadcast learning progress
    candidate-specific learning progress

Acceptance:

candidate-specific versions improve targeted exploration
without increasing random wandering.

⸻

Experiment E — Curiosity plus sleep

Question:
    Does sleep convert curiosity-driven experience into better future behaviour?
Arms:
    curiosity without sleep
    curiosity with sleep
    sleep without curiosity
    neither
Acceptance:
    curiosity + sleep improves rule-relevant behaviour after consolidation.

⸻

Experiment F — Curiosity safety boundary

Question:
    Does curiosity respect harm streams?
Arms:
    curiosity ungated
    curiosity harm-gated
    curiosity harm-gated + cautious-distance exploration
Acceptance:
    harm-gated curiosity preserves exploration while reducing catastrophic contact.

⸻

6. Proposed implementation order

1. Standardise ARC-065 diagnostics.
2. Run five-arm heartbeat experiment.
3. Calibrate MECH-313 / MECH-314 / MECH-320 weights.
4. Add candidate-specific uncertainty curiosity.
5. Add candidate-specific learning-progress curiosity.
6. Add curiosity metadata to residue / anchors.
7. Add curiosity branch to hippocampal proposal generation.
8. Add boredom / satiation control.
9. Add harm-aware curiosity gating.
10. Add sleep replay priority for curiosity-tagged experience.
11. Retest ARC-062 and ARC-064 rule-apprehension pathways.

⸻

7. Suggested claim updates

ARC-065

ARC-065 should be framed as the upstream behavioural-diversity-generation pathway required for both top-down rule application and bottom-up rule discovery. It is not merely exploration noise; it is the coordinated interaction of stochasticity, structured curiosity, and tonic vigor.

MECH-313

MECH-313 should remain distinct from MECH-260. MECH-313 supplies state-independent policy entropy; MECH-260 supplies state-dependent anti-recency. Behavioural validation should show whether they have separable effects.

MECH-314

MECH-314 should be promoted only after structured curiosity produces useful behavioural diversity beyond matched-entropy noise. Its Phase 1 substrate is landed, but Phase 2 requires candidate-specific uncertainty and learning-progress estimation.

MECH-314a

MECH-314a is the most mature sub-flavour because it is already per-candidate and residue-field grounded. It should be used as the first behavioural proof of structured curiosity.

MECH-314b

MECH-314b remains incomplete while uncertainty is broadcast globally. Candidate-specific uncertainty readout is required before it can count as fully structured curiosity.

MECH-314c

MECH-314c remains incomplete while learning progress is broadcast globally. A region- or candidate-specific learning-progress memory is required to prevent attraction to irreducible noise.

MECH-320

MECH-320 should be treated as a sibling drive that enables curiosity to become action. It should not be collapsed into curiosity, because it biases action over passivity rather than novelty or information gain.

⸻

8. Risk register

Risk	Meaning	Mitigation
Noise mistaken for curiosity	Entropy rises but exploration is not directed	Matched-entropy comparison
Novelty addiction	Agent keeps chasing newness without learning	Boredom / satiation control
White-noise trap	Agent is attracted to irreducible prediction error	Learning-progress, not error magnitude
Commitment collapse	Curiosity prevents stable action sequences	Beta-gate and commitment-rate diagnostics
Harm-blind exploration	Curiosity drives hazard contact	Harm-aware gating
Passive curiosity	Interesting candidates are scored but not acted on	Tonic vigor and no-op diagnostics
Proposal bottleneck	Curiosity cannot select candidates that are never proposed	Hippocampal curiosity proposal branch
Replay neglect	Curiosity experiences do not consolidate	Curiosity-tagged sleep replay
Rule-discovery starvation	Diversity remains insufficient for ARC-064	Rule-relevant transition count
Overfitting to toy novelty	Agent learns map-specific novelty rather than general curiosity	Multi-environment validation

⸻

9. Bottom line

The curiosity system can probably be completed by moving it through four developmental stages:

1. Policy regulator
    current state:
        noise floor + curiosity score bias + tonic vigor
2. Behavioural diversity generator
    next target:
        prove increased useful diversity
3. Memory-linked curiosity stream
    next layer:
        curiosity-tagged residue, anchors, replay priority
4. Developmental learning driver
    final V3/V4 target:
        curiosity creates the behavioural variation from which rules,
        schemas, and self/world regularities can be discovered

The immediate completion task is therefore:

Do not add another curiosity module.
Do not collapse curiosity into reward.
Do not confuse noise with curiosity.
Instead:
    measure behavioural diversity,
    calibrate noise + curiosity + vigor,
    make uncertainty and learning-progress candidate-specific,
    write curiosity into memory,
    replay it during sleep,
    and prove that it enables rule discovery.

Curiosity should become the system that says:

There is something here I do not yet understand,
and understanding it may change what I can do.

That is different from wanting, different from liking, different from vigor, and different from random noise.

[^1]: The important hidden-process distinction is between **exploration pressure** and **curiosity proper**. A temperature lift can make an agent move differently, but curiosity should preferentially move it toward places where model-improving information is expected. This is why matched-entropy experiments are essential: they separate “more random” from “more knowledge-seeking.”
