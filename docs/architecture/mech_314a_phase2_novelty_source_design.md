---
title: MECH-314a Phase-2 Novelty-Source Architecture Design
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 10
status: provisional
status_asof: 2026-07-10
status_claim: MECH-314A
---

# MECH-314a Phase-2 Novelty-Source Architecture Design

**Build:** IMPLEMENTED 2026-06-05 (design Candidate 5A). User assent on
Candidate 5A granted 2026-06-05; the implementation landed via the
`MECH-314a-Phase-2-impl` substrate_queue entry (status
`implemented_pending_validation`) by session
`implement-mech314a-phase2-cand5a-20260605T2016Z`. Module changes:
`ree-v3/ree_core/agent.py` (rolling z_world visitation buffer, MECH-094-gated),
`ree-v3/ree_core/policy/structured_curiosity.py` (`_compute_novelty` extended
for the visitation source + first-action one-hot augmentation),
`ree-v3/ree_core/utils/config.py` (6 bit-identical-OFF knobs). Contract test
`ree-v3/tests/contracts/test_mech_314a_phase2.py` (14/14 PASS); 826 contracts +
7 preflight PASS (bit-identical OFF). The section-8 governance/claims updates
remain GATED on validation acceptance and are NOT applied. The validation
EXPERIMENT (section 6 falsifier sketch, 3 arms x 3 seeds x 30 episodes) is the
remaining gate; on PASS the follow-on is `/queue-experiment` V3-EXQ-590b
Goldilocks retest.

**AMEND 2026-06-07 (Candidate 1 source on the 5A machinery).** The first
validation run, V3-EXQ-648, FAILed `precondition_unmet` (run
`v3_exq_648_..._20260607T025417Z`; autopsy
`evidence/planning/failure_autopsy_V3-EXQ-648_2026-06-07.{md,json}`): the
landed 5A path computed the per-candidate novelty (and the auto-augmentation
`_candidate_spread` key) from the hippocampal proposer's first-step z_world
(`trajectory.world_states[:,0,:]`), whose cross-candidate spread collapses to
<0.01 under monostrategy, while the readiness precondition measured a
*different* representation (`e2.cand_world_pairwise_dist`=0.1147) -> false
READY. Fix (this amend, session
`mech314a-e2wf-novelty-amend-then-648a-20260607T0545Z`): a no-op-default
config flag `curiosity_candidate_source` (`"proposer"` default, bit-identical |
`"e2_world_forward"`) that rebuilds the consumed `candidate_world_summaries`
from the SD-056-trained action-conditional `e2.world_forward(z0, a_i)`
predictions -- i.e. **Candidate 1 (section 3) as the source for the landed
Candidate-5A novelty/augmentation machinery**. `structured_curiosity.py` is
unchanged (both `_compute_novelty` and `_candidate_spread` already key on the
`candidate_world_summaries` argument). Re-validation is V3-EXQ-648a (supersedes
648), enabling the flag and re-targeting the readiness precondition to the
consumed representation. The section-8 governance/claims updates remain GATED
on the 648a PASS.

**Authoring session:** mech314a-phase2-novelty-source-arch-design-20260531T125133Z
(TASK_CLAIMS).

**Companion artifact.** This document is the architecture-level companion to
the planning-level design doc
[`evidence/planning/mech_314a_phase2_novelty_source_design.md`](../../evidence/planning/mech_314a_phase2_novelty_source_design.md)
(authored 2026-05-26, commit `5ec31e39c8`). The planning doc is the
exhaustive option-by-option ledger. This doc revisits the same design
question against the substrate landscape as of 2026-05-31 -- specifically
the SD-056 contrastive next-state landing (2026-05-29) and the SD-056
multistep-stability amend (2026-05-31T11:25Z) -- and weighs the user-named
five candidate novelty sources against the three-loop learning-channel
commitments (ARC-021 / MECH-069). It does not re-derive the planning
doc's six-option matrix.

---

## 1. Design question

Which signal (or combination of signals) should the MECH-314a per-candidate
curiosity bias compute novelty over, such that:

1. Per-candidate spread is non-zero in the regimes the diversity-isolation
   experiments target (untrained / harm-free during Goldilocks calibration;
   trained / mixed-stream during ARC-065 behavioural-diversity validation).
2. The signal source is consistent with the three-loop learning-channel
   commitments (ARC-021 / MECH-069) -- in particular, the score_bias
   modulator on the E3 planning-gates loop should not silently smuggle a
   foreign-loop error signal into selection.
3. The biological / formal anchor of MECH-314a (Wittmann 2008 ventral-striatum
   novelty response; Bellemare 2016 / Burda 2018 count-based / RND
   computational analog) survives -- or is consciously broken with a new
   sibling-claim registration.

---

## 2. What changed since the 2026-05-26 planning doc

The 2026-05-26 planning doc concluded **Option A: rolling z_world visitation
buffer always-on**. That recommendation was scoped against the empirical
finding that all K CEM candidates produced identical `cand_world_pairwise_dist`
(0.0000 across K=32) after one E2 world-forward step, even with diverse
first-action one-hots in the pool. Two upstream failure modes were named:

- **F1**: ResidueField empty on untrained / harm-free episodes.
- **F2**: E2 world-forward collapsing K candidates' first-step z_world.

Since that doc landed, three pieces of substrate have moved:

| Substrate | Status as of 2026-05-31 | Effect on Phase 2 design |
|-----------|-------------------------|--------------------------|
| **SD-056** contrastive next-state in E2 world-forward | Implemented 2026-05-29 (V3-EXQ-613 substrate-readiness PASS); multistep-stability amend landed 2026-05-31T11:25Z; V3-EXQ-617 amended-substrate readiness PASS 2026-05-31T11:31Z | F2 has a substrate fix. Per-candidate z_world divergence at t=1 is non-zero when SD-056 contrastive training is enabled (`e2_action_contrastive_*`). The Option A recommendation in the planning doc is now MORE viable because z_world novelty against a rolling buffer is no longer collapsed to zero by E2's compression. |
| **MECH-269b** symmetric V_s gating (staleness-corrected variant via followup-A) | Implemented 2026-04-26; staleness wiring 2026-04-29; canonical V3-EXQ-601 PASS 2026-05-21 | Orthogonal to the novelty-source question (gates the rollout horizon on staleness, not the score_bias signal source). |
| **MECH-307** anticipatory affect conjunction (goal_pipeline GAP-1) | Implemented 2026-05-08 / 2026-05-11; V3-EXQ-540g PASS 2026-05-15 | Defines the consumer side for z_goal -> approach pathways. Relevant to candidate (4) below. |
| **goal_pipeline:GAP-4** z_goal-collapse blocker | Open, load-bearing. z_goal collapses to ~1e-7 across all V3-EXQ-591 arms. | Candidate (4) (z_goal as novelty signal) is structurally unfunded until GAP-4 clears. |
| **ARC-065** behavioral-diversity-generation pathway | Phase-1 implemented; GAP-A (CEM-collapse) substrate-landed 2026-05-17 SP-CEM main-path; GAP-A FP-2 falsifier V3-EXQ-569a queued 2026-05-31 on SD-056-corrected substrate | Parent context. ARC-065 GAP-A is the load-bearing claim that the per-candidate curiosity channel was supposed to confirm; SD-056 made the test re-runnable. |
| **MECH-313** stochastic noise floor (LC-NE tonic / SAC analog) | candidate_substrate_landed 2026-05-10 V3-EXQ-544 PASS | Sibling ARC-065 child. Pure-arithmetic; orthogonal signal-source question. |
| **MECH-341** E3 score diversity preservation | retune_validated 2026-05-29 V3-EXQ-611c PASS; V3-EXQ-614a behavioural PASS 2026-05-30 (C2+C3); V3-EXQ-614b in-flight on SD-056-amended substrate | Sibling Layer-B substrate at the E3-selection layer. Demonstrates the score_bias plumbing works when fed non-zero per-candidate signal -- a separate confirmation that Phase 2's job is the upstream signal source, not the e3_selector.py:737 site. |

**Net effect.** Failure mode F2 (E2 z_world collapse) is no longer a hard
blocker for any candidate signal source -- it is now configurable on a
per-experiment basis via the SD-056 amend levers. Failure mode F1
(empty ResidueField on harm-free runs) is unchanged -- it depends on the
chosen novelty source.

The Phase 2 recommendation in the planning doc was made under "F2 is
unaddressed; A fixes F1 but not F2." Under the current substrate
landscape: "F2 is addressed at the substrate layer; the question is whether
to consume the SD-056-corrected z_world signal directly or to bypass it."

---

## 3. Five candidate novelty sources

Each candidate is keyed to the user brief's naming. The planning doc's
options A-F overlap partially but are not identical; cross-references below.

### Candidate 1 -- Per-candidate z_world after SD-056-corrected forward

**Signal.** RBF novelty (or k-NN distance) over the per-candidate first-step
z_world tensor `cand_world_summaries[k]` produced by E2's contrastive-trained
world-forward predictor. The comparison set is either a rolling buffer of
recent waking-tick z_world states (planning-doc Option A) or the existing
harm-coupled ResidueField centers (Phase-1 status quo) or both
(planning-doc Option D hybrid).

**F1 fix.** Conditional on the comparison set. Rolling buffer -> YES
(populates from tick 1). ResidueField only -> NO. Hybrid -> YES.

**F2 fix.** YES when SD-056 contrastive levers are ON. The whole
candidate becomes structurally dependent on SD-056 being ON in the
deployed configuration.

**Cost.** LOW (rolling buffer ~30-50 lines; mirrors planning-doc Option A's
implementation budget). The cost rises if Phase 2 also needs to gate
behaviour on whether SD-056 is ON in the current run -- but the SD-056
substrate is well-instrumented (V3-EXQ-613/617 readiness PASS) so the gate
can be a simple config-read.

**Three-loop alignment.** ALLOWED CROSS-LOOP MODULATOR. The signal is
sourced from the action-enacting loop (E2's z_gamma transitions) and used
as a score-bias modulator on the planning-gates loop (E3 selection). Per
MECH-069 the *error signals* must stay separated, but MECH-314 explicitly
designs a substrate where state-novelty from the world model modulates
planning-gates selection (this is what the ventral-striatum-to-OFC-to-vmPFC
projection does biologically). The cross-loop wiring is at the gain-modulator
layer, not the error-signal layer, so MECH-069 is not violated.

**Semantic fidelity to MECH-314a.** HIGH. Wittmann 2008 ventral-striatum
novelty fires on state novelty -- z_world (the unified latent object world)
is the closest computational analog. Bellemare 2016 / Burda 2018
count-based / RND analogs also compute distance in a learned state
embedding space.

**Sensitivity to substrate state.** HIGH. If SD-056 is OFF in a given
experiment (or its amend levers are not engaged), per-candidate spread
collapses again. Phase 2 must either gate behaviour on SD-056 state or
silently produce zero spread when SD-056 is OFF (the latter risks
reintroducing the V3-EXQ-571 false-positive "channel doesn't propagate"
headline in any SD-056-OFF experiment).

### Candidate 2 -- Per-candidate first-action class

**Signal.** Categorical novelty over the candidate's first-action one-hot,
against either a rolling history of recently-selected first actions or a
candidate-pool relative-frequency map. Mirrors the 2026-05-17 ARC-062
GAP-B fix template, where `gated_policy_use_first_action_onehot`
concatenates the first-action one-hot onto the head's input features to
bypass E2's z_world collapse.

**F1 fix.** Conditional on the comparison set (action-class history populates
from tick 1, so YES with a rolling buffer).

**F2 fix.** YES by construction. Action one-hots are per-candidate by
definition; they never pass through E2's compression.

**Cost.** LOW-MEDIUM. ~40-60 lines. Action-class buffer in the agent +
plumbing into `_compute_novelty` accepting a categorical novelty signal.

**Three-loop alignment.** MIXED. Action-conditional novelty is closer to
the action-enacting-loop error signal (MECH-070's "motor-sensory mismatch
at the object level") than to the planning-gates-loop's outcome-level harm /
goal error. Using action novelty as a score_bias modulator on E3 selection
is semantically closer to "this action class is under-explored" than to
"this state is novel." Whether this is a violation depends on how strictly
one reads MECH-069's incommensurability -- the error signal is not being
mixed, but the source-loop semantics of the modulator are different.

**Semantic fidelity to MECH-314a.** LOW-MEDIUM. Wittmann 2008 is about
*stimulus* novelty, not action novelty. The MECH-314c learning-progress
sub-flavour is the existing claim that owns action-conditional novelty
readings; action-class novelty here risks conflation with MECH-314c at
the candidate-selection level.

**Sensitivity to substrate state.** LOW. Works regardless of SD-056 state.
This is the candidate's main argument: it produces non-zero per-candidate
spread under every substrate configuration, including SD-056-OFF runs and
including post-V4 substrate changes.

### Candidate 3 -- Per-candidate residue-coverage delta

**Signal.** For each candidate, compute the predicted change in
ResidueField RBF coverage if that candidate's first action (or first few
actions) were committed. Concrete arithmetic: take the candidate's predicted
first-step trajectory footprint (z_world projection), compute the RBF
coverage value of nearest active centers, sum or average across centers.
The per-candidate value is the *delta* between the candidate's projected
footprint and the agent's current position's footprint.

**F1 fix.** NO. ResidueField only accumulates on harm + commitment; harm-free
runs have empty residue and delta is zero across all K.

**F2 fix.** Conditional. If the residue-coverage delta is computed against
the pre-E2 candidate's first-step z_world, the answer mirrors candidate 1.
If computed against a richer trajectory representation (e.g. the rolled-out
z_world over multiple E2 steps), it can survive z_world collapse at t=1 if
later steps re-diverge -- but this depends on whether SD-056 multistep
amend preserves divergence beyond t=1.

**Cost.** MEDIUM. ~60-100 lines. Requires extending `_compute_novelty` to
read ResidueField coverage values rather than just RBF centers; potentially
also extends ResidueField API to expose a per-candidate coverage probe.

**Three-loop alignment.** STRONGEST. The signal is sourced from the
planning-gates loop's own terrain (ResidueField accumulates harm signal on
committed trajectories) and used as a modulator on planning-gates selection.
The error signal stays within-loop. This is the only candidate that is
purely within-loop with respect to the three-loop schema.

**Semantic fidelity to MECH-314a.** MEDIUM. Wittmann 2008 ventral-striatum
novelty is not explicitly harm-coupled in the original paper; the
harm-coupling here is a consequence of REE's design choice to make the
residue field accumulate on harm + commitment only. The biological reading
is closer to "novelty of harm landscape," which is a defensible
neuroscientific reading (the ventral striatum integrates novelty with
valence) but a sharper claim than Wittmann's pure-state-novelty result.

**Sensitivity to substrate state.** HIGH on harm-free runs (F1 makes the
channel silent). MEDIUM on trained runs (depends on residue population rate
under the actual policy).

### Candidate 4 -- Per-candidate z_goal contribution

**Signal.** For each candidate, compute the candidate's contribution to or
distance from the current z_goal vector. Concrete arithmetic: dot-product of
candidate-predicted z_world with z_goal direction (alignment readout), or
RBF novelty over per-candidate z_goal-difference vectors.

**F1 fix.** YES on episodes where z_goal is populated (training has produced
non-trivial goal state). NO on first-encounter / pre-training runs where
z_goal is still null.

**F2 fix.** Conditional. z_goal is computed in `GoalState.update()` from
z_resource + z_world signals; whether per-candidate spread survives depends
on whether the candidate-conditional z_goal projection collapses under E2
the same way z_world does. Almost certainly does collapse under the same
mechanism unless SD-056 is ON (z_goal pipeline reads z_world).

**Cost.** Cannot be estimated until goal_pipeline:GAP-4 clears -- the
z_goal pipeline currently collapses to ~1e-7 across all V3-EXQ-591 arms,
which means per-candidate spread is structurally zero regardless of any
Phase-2 wiring choice. STRUCTURALLY UNFUNDED at the substrate layer.

**Three-loop alignment.** STRONG. z_goal is a planning-gates-loop signal
(goal error feeds E3 / hippocampal trajectory proposer). Within-loop
modulator.

**Semantic fidelity to MECH-314a.** LOW. This is a goal-relevance signal,
not a novelty signal. The biological reading is closer to MECH-295
(drive->liking->approach bridge) or MECH-216 (goal-conditioned wanting)
than to Wittmann 2008 striatal novelty. Probably warrants a NEW sibling
claim if pursued -- MECH-314a's identity does not survive this
substitution.

**Sensitivity to substrate state.** EXTREME. Cannot land until
goal_pipeline:GAP-4 clears AND z_goal-conditioned candidate projection is
working AND SD-056 (or equivalent) preserves per-candidate z_goal spread.
Three upstream substrate dependencies.

### Candidate 5 -- Hybrid

**Sub-flavour A: candidate 1 + candidate 2.** Rolling z_world buffer
(planning-doc Option A) as the primary signal source, plus a small
additive first-action one-hot bypass term (candidate 2) as
substrate-robustness insurance. Hybrid term is activated only when
candidate 1's signal carries below-threshold per-candidate spread.

Cost: LOW + LOW = LOW. F1 fix: YES (buffer source). F2 fix: YES (action
one-hot fallback when SD-056 collapses). Three-loop: CROSS-LOOP +
ACTION-CONDITIONAL. Semantic fidelity: MEDIUM (Wittmann anchor preserved as
primary; action-onehot bypass is acknowledged as substrate-robustness
hedge).

**Sub-flavour B: candidate 1 + candidate 3.** Rolling z_world buffer primary
plus harm-residue-coverage secondary. Mirrors the planning doc's Option D
(hybrid). The harm-residue term is a smaller-weight overlay that becomes
load-bearing on trained-policy runs where residue is populated.

Cost: LOW + MEDIUM = MEDIUM. F1 fix: YES (buffer). F2 fix: YES on
SD-056-ON, conditional on SD-056-OFF. Three-loop: CROSS-LOOP + WITHIN-LOOP.
Semantic fidelity: HIGH (Wittmann anchor primary; residue-coverage is the
literal-biological "novelty of harm landscape" reading).

**Sub-flavour C: candidate 2 + candidate 3.** First-action one-hot primary
plus harm-residue-coverage secondary. Skips candidate 1 entirely.

Cost: LOW + MEDIUM = MEDIUM. F1 fix: YES (action one-hot from tick 1).
F2 fix: YES by construction. Three-loop: ACTION-CONDITIONAL + WITHIN-LOOP.
Semantic fidelity: LOW (no Wittmann channel).

---

## 4. Substrate dependency map

This table summarises how each candidate maps to existing substrate state.
"Substrate-ready" = the substrate Phase-2 would consume is landed and
validated. "Substrate-fragile" = depends on a configuration knob; works
when ON but silent when OFF. "Substrate-blocked" = a load-bearing upstream
substrate is not landed.

| Candidate | SD-056 (E2 z_world divergence) | MECH-269b (V_s rollout gating) | MECH-307 (anticipatory affect) | ARC-065 (diversity-generation) | MECH-313 (noise floor) | MECH-341 (E3 score diversity) | goal_pipeline:GAP-4 (z_goal) | Net status |
|-----------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|------------------------|-------------------------------|------------------------------|------------|
| 1 -- z_world (post-SD-056) | LOAD-BEARING | n/a | n/a | parent | sibling | sibling | n/a | Substrate-fragile (SD-056-ON-required) |
| 2 -- first-action one-hot | n/a | n/a | n/a | parent | sibling | sibling | n/a | Substrate-ready |
| 3 -- residue-coverage delta | n/a (post-E2 trajectory footprint may benefit) | n/a | n/a | parent | sibling | sibling | n/a | Substrate-fragile (harm-free silent) |
| 4 -- z_goal contribution | LOAD-BEARING | LOAD-BEARING | LOAD-BEARING | parent | sibling | sibling | LOAD-BEARING + BLOCKED | Substrate-blocked |
| 5A -- 1+2 | conditional | n/a | n/a | parent | sibling | sibling | n/a | Substrate-ready (with hedge) |
| 5B -- 1+3 | LOAD-BEARING | n/a | n/a | parent | sibling | sibling | n/a | Substrate-fragile + harm-free-silent |
| 5C -- 2+3 | n/a | n/a | n/a | parent | sibling | sibling | n/a | Substrate-ready (no Wittmann channel) |

---

## 5. Three-loop alignment analysis

Per [`docs/architecture/three_loop_learning_channels.md`](three_loop_learning_channels.md)
(ARC-021 / MECH-069 / MECH-070):

- **E1 sensorium loop**: sensory PE on raw sensory latent state.
- **E2 action-enacting loop**: motor-sensory PE on z_gamma (conceptual sensorium).
- **E3 planning-gates loop**: harm/goal error on outcomes; residue accumulates.

The three error signals are incommensurable (MECH-069). Collapsing them
into a single scalar misattributes credit.

MECH-314a's score_bias is a *gain modulator* on E3 selection. It does not
participate in any loop's error signal directly -- it shifts which
candidate the planning-gates loop selects. The question is whether the
source from which the modulator is computed should be in-loop with E3
(strictest reading of MECH-069) or whether cross-loop modulators are
allowed (less strict reading).

**Two defensible readings:**

(a) **Strict within-loop.** MECH-314a's novelty signal should come from
the planning-gates loop's own terrain. Per the three-loop schema, that
means the residue field. Candidate 3 (residue-coverage delta) is the only
within-loop candidate. Candidate 4 (z_goal) is also within-loop and would
qualify if goal_pipeline:GAP-4 weren't blocking. The strict reading rejects
candidate 1 (z_world is action-enacting-loop) and candidate 2
(action-conditional is closer to action-enacting-loop).

(b) **Cross-loop modulators allowed.** The biological substrate for
MECH-314a is ventral striatum, which sits at the BG hub where the three
loops converge via the cortico-striatal projection. The ventral-striatum
novelty response (Wittmann 2008) is computed against world-model novelty
and *projects to* planning-gates selection -- this is precisely a
cross-loop modulator wired through the BG hub. Under this reading,
candidate 1 (z_world novelty) is the biology-faithful choice; the
cross-loop wiring is at the modulator layer (allowed) not the error-signal
layer (forbidden).

**Resolving the tension.** MECH-069's incommensurability principle is
about *credit assignment*. A modulator that shifts which candidate gets
selected does not assign credit -- the actual learning signal is still
the loop-appropriate error (harm/goal error for E3). So cross-loop
modulators are allowed under the principle's spirit. Reading (b) is the
right reading.

**Architectural verdict.** Cross-loop modulators are permitted at the
gain-modulator layer. Candidate 1 (z_world post-SD-056) is the most
biology-faithful and three-loop-permissible choice. Candidate 3
(residue-coverage delta) is the within-loop "purist" choice but requires
giving up the Wittmann biological anchor. The hybrid 5B (1+3) is the
defense-in-depth play: biology-faithful primary, within-loop secondary.

---

## 6. Recommendation

**Recommended option: Candidate 5A (rolling z_world buffer + first-action
one-hot bypass).**

This is a sharpening of the 2026-05-26 planning doc's Option A
recommendation under the post-SD-056 substrate landscape:

1. **Primary signal source: rolling z_world visitation buffer**
   (per planning-doc Option A, sections 3 and 4). Buffer populates on
   every waking tick via the agent's `sense()` hook. RBF novelty is
   computed against this buffer. Under SD-056-ON, per-candidate spread is
   non-zero. Wittmann 2008 / Bellemare 2016 / Burda 2018 anchors survive.

2. **Substrate-robustness bypass: first-action one-hot augmentation**
   (per planning-doc Option B, sections 3 and 4). When the per-candidate
   z_world spread falls below a configurable threshold (canonical case:
   SD-056 is OFF in this run, or the contrastive training has not yet
   converged), the per-candidate signature is augmented with the
   first-action one-hot before RBF distance is computed. The action
   one-hot carries per-candidate spread by construction.

3. **Activation rule.** The augmentation is silent when SD-056 produces
   sufficient z_world spread (planning-doc Option A unchanged). The
   augmentation engages when it doesn't. This prevents the augmentation
   from contaminating SD-056-ON runs while guaranteeing non-zero
   per-candidate signal on SD-056-OFF runs.

4. **Three-loop alignment.** Primary signal is cross-loop modulator at
   the ventral-striatum-analog layer (permitted). Bypass signal is
   action-conditional (also permitted as gain-modulator). Both feed the
   score_bias kwarg to e3.select(); neither participates in any loop's
   error signal.

5. **Why not 5B (z_world + residue-coverage).** 5B is the planning doc's
   Option D resurrected with the within-loop residue-coverage term as the
   secondary. The cost difference vs 5A is MEDIUM vs LOW. The residue-
   coverage secondary is silent on harm-free episodes (F1 still fires for
   that term), which means 5B's defense-in-depth only kicks in on
   trained-policy runs where SD-056 is most likely to be ON anyway.
   Defense-in-depth where the secondary is silent in the same regime
   where the primary works is not actually defense-in-depth.

6. **Why not 5C (action-onehot + residue).** Drops the Wittmann anchor
   entirely. Saves the substrate-robustness story but at the cost of
   re-specifying MECH-314a away from striatal novelty.

7. **Why not pure candidate 1.** Without the substrate-robustness bypass,
   any SD-056-OFF experiment would produce a zero per-candidate signal
   and re-trigger the V3-EXQ-571 false-positive headline. The bypass is
   cheap and prevents the methodology problem from recurring.

8. **Why not pure candidate 3 (within-loop purist).** Three-loop-strict
   reading is defensible but rejected on biological-anchor grounds (see
   section 5). Residue-coverage delta also fails F1 (harm-free episodes
   silent), which makes it strictly worse than 5A for the V3-EXQ-590-series
   Goldilocks calibration regime.

9. **Why not candidate 4.** Structurally blocked by goal_pipeline:GAP-4
   (z_goal collapses to ~1e-7). Even after GAP-4 clears, candidate 4 is
   semantically a goal-alignment signal rather than a novelty signal --
   probably warrants a new sibling claim under MECH-216/MECH-307, not a
   re-spec of MECH-314a.

### What candidate 5A specifically commits to

Implementation-shape (NOT a code spec):

- **Per-agent rolling z_world visitation buffer**: deque, configurable
  length (default ~256 waking ticks), MECH-094-gated (waking-only writes).
- **Augmentation flag** `curiosity_use_first_action_onehot` (default `False`
  for bit-identical OFF). When True, candidate signatures are augmented
  with first-action one-hot before RBF distance.
- **Auto-augmentation policy** (default `"auto"`): if per-candidate spread
  in the un-augmented signature falls below `curiosity_min_spread_threshold`
  (default 0.01) for `N` consecutive ticks, auto-engage augmentation. If
  the un-augmented spread recovers above threshold, auto-disengage.
  Explicit `"always"` and `"never"` options bypass the auto-detection.
- **Config knobs**: `curiosity_novelty_source` (`"residue"` / `"visitation"`
  / `"auto"`, default `"residue"` for bit-identical OFF),
  `curiosity_visitation_buffer_len` (default 256),
  `curiosity_use_first_action_onehot` (default `False`),
  `curiosity_first_action_augmentation_policy` (`"never"` / `"auto"` /
  `"always"`, default `"never"`), `curiosity_min_spread_threshold`
  (default 0.01), `curiosity_min_spread_consecutive_ticks` (default 5).
- **Bit-identical OFF**: all new code paths gated behind defaults that
  reproduce current MECH-314a behaviour. Experiments opt in to Phase 2 via
  explicit config.

### Falsifier experiment sketch (NOT queued)

`v3_exq_NEW_mech314a_phase2_substrate_readiness.py` (substrate-readiness
diagnostic; copy V3-EXQ-545 template):

- **Arms** (3 arms x 3 seeds x 30 episodes):
  - ARM_0 BASELINE: Phase-2 OFF entirely (`curiosity_novelty_source="residue"`,
    `curiosity_first_action_augmentation_policy="never"`). Should be
    bit-identical to current MECH-314a behaviour. Acceptance: per-candidate
    spread distribution matches V3-EXQ-571 / V3-EXQ-609 baselines.
  - ARM_1 VISITATION_ONLY: Phase-2 visitation buffer ON, action-onehot OFF
    (`curiosity_novelty_source="visitation"`,
    `curiosity_first_action_augmentation_policy="never"`,
    SD-056 contrastive ON). Tests candidate 1 in isolation.
  - ARM_2 VISITATION_PLUS_ONEHOT: candidate 5A (visitation buffer + auto
    augmentation, SD-056 contrastive ON). Tests the recommended Phase-2
    configuration.
- **Acceptance criteria**:
  - **C1 baseline matches**: ARM_0 reproduces V3-EXQ-571's bias_fraction =
    zero across all bias channels.
  - **C2 visitation lifts spread (SD-056-ON)**: ARM_1 `cand_world_pairwise_dist`
    > 0.05 in >=2/3 seeds; `_bdc_curiosity.std()` > 0 in >=80% of waking
    ticks past tick 20.
  - **C3 augmentation engages when needed**: ARM_2 augmentation engages on
    >=80% of waking ticks past tick 20 when SD-056 is ARTIFICIALLY DISABLED
    mid-run (probe condition); augmentation does NOT engage when SD-056 is
    ON throughout.
  - **C4 MECH-094 simulation gate**: visitation buffer does not accumulate
    on replay/DMN ticks (sentinel: simulation-tick counter = N expected,
    buffer-append counter = 0 on simulation ticks).
- **PASS = C1 + C2 + C3 + C4 all fire** (substrate-readiness criterion
  unanimous). FAIL on any single C-criterion fail -> /diagnose-errors on
  the Phase-2 wiring.
- **Routing**: PASS -> /queue-experiment V3-EXQ-590b (Goldilocks calibration
  retest with `curiosity_novelty_source="visitation"`); FAIL ->
  /diagnose-errors.

---

## 7. Phase-2 substrate_queue staging

The following entry is **staged** for insertion into
`evidence/planning/substrate_queue.json` by a subsequent
`/implement-substrate` session (NOT this design chip). The existing
`design_question` entry (sd_id `MECH-314a-Phase-2`) is being updated by
this session to point at this doc; the entry below is the *implementation*
follow-on, distinct from the design question itself.

```json
{
  "added_session": "<TO_FILL_AT_IMPLEMENT_LANDING>",
  "added_utc": "<TO_FILL_AT_IMPLEMENT_LANDING>",
  "cross_ref": "docs/architecture/mech_314a_phase2_novelty_source_design.md section 6 recommendation; evidence/planning/mech_314a_phase2_novelty_source_design.md (2026-05-26 commit 5ec31e39c8) Option A; evidence/planning/v3_exq_571_root_cause_2026-05-25.md disposition #5 (commit a79915151b)",
  "depends_on_unresolved": [
    "User assent on Candidate 5A recommendation (architecture-doc section 6) vs alternatives (5B hybrid with residue-coverage; 5C action-onehot + residue; strict candidate 3 within-loop purist)"
  ],
  "design_doc": "docs/architecture/mech_314a_phase2_novelty_source_design.md",
  "failure_record": [],
  "implementation_hint": "Phase 2 substrate implementation for MECH-314a per architecture doc section 6 (Candidate 5A). Three module-level changes: (1) ree-v3/ree_core/agent.py REEAgent rolling z_world visitation buffer (collections.deque, default maxlen 256), append in sense() after update_per_stream_vs, MECH-094-gated; (2) ree-v3/ree_core/policy/structured_curiosity.py StructuredCuriosity._compute_novelty extended to accept an alternate active-source argument (visitation deque) AND optional first-action-onehot augmentation tensor; (3) ree-v3/ree_core/utils/config.py REEConfig new knobs curiosity_novelty_source (Literal['residue','visitation','auto'], default 'residue' for bit-identical OFF), curiosity_visitation_buffer_len (int, default 256), curiosity_use_first_action_onehot (bool, default False), curiosity_first_action_augmentation_policy (Literal['never','auto','always'], default 'never'), curiosity_min_spread_threshold (float, default 0.01), curiosity_min_spread_consecutive_ticks (int, default 5). Bit-identical OFF guaranteed by defaults. Contract test ree-v3/tests/contracts/test_mech_314a_phase2.py covering bit-identical OFF, visitation buffer accumulates only on waking ticks (MECH-094 gate), per-candidate spread >0 on harm-free runs with visitation ON and SD-056 ON, augmentation engages when per-candidate spread falls below threshold for N consecutive ticks. Validation experiment V3-EXQ-NEW substrate-readiness diagnostic per architecture-doc section 6 falsifier sketch (3 arms x 3 seeds x 30 episodes); PASS -> /queue-experiment V3-EXQ-590b Goldilocks retest.",
  "last_seen_session": "<TO_FILL_AT_IMPLEMENT_LANDING>",
  "priority": 2,
  "ready": true,
  "ready_blocked_by": null,
  "ready_gates_cleared": [
    "SD-056 contrastive next-state landed 2026-05-29 (V3-EXQ-613 PASS)",
    "SD-056 multistep-stability amend landed 2026-05-31T11:25Z (V3-EXQ-617 PASS 11:31Z)",
    "MECH-094 simulation-gate substrate (waking-only writes) already implemented per StructuredCuriosity Phase 1"
  ],
  "sd_id": "MECH-314a-Phase-2-impl",
  "status": "pending_implementation",
  "title": "MECH-314a Phase-2 implementation: rolling z_world visitation buffer (primary) + first-action one-hot augmentation (substrate-robustness bypass). Architecture-doc Candidate 5A. Bit-identical-OFF default; experiments opt in via config.",
  "unblocks_claims": [
    "MECH-314a",
    "MECH-314",
    "ARC-065"
  ]
}
```

The existing `MECH-314a-Phase-2` `design_question` entry should be updated
to:

- `design_doc`: append the new architecture-doc path alongside the existing
  planning-doc path.
- `cross_ref`: append architecture-doc reference.
- `last_seen_session`: bump to this session ID.
- `status`: stay `design_question` (the implementation entry above carries
  the `pending_implementation` status).
- `ready_blocked_by`: replace "Governance design decision pending across
  four candidate novelty sources" wording with "User assent on architecture-
  doc section 6 Candidate 5A recommendation".

---

## 8. Updates to land on Phase-2 implementation acceptance

Do NOT update any of these in this session. List for the implementation
landing session and the post-implementation governance session:

1. **`docs/claims/claims.yaml` MECH-314a `evidence_quality_note`.** Update
   Phase-1 signal-source wording to acknowledge rolling buffer + optional
   first-action augmentation as Phase-2 signal sources.
2. **`docs/claims/claims.yaml` MECH-314 parent `functional_restatement`.**
   Mirror the table update for MECH-314a's row.
3. **`docs/architecture/mech_314_structured_curiosity_bonus.md`.** Extend
   sub-flavours table with Phase-2 signal-source column; add Phase-2
   section linking to this doc.
4. **`evidence/planning/substrate_queue.json` MECH-314 entry.** Update
   `pending_retests[V3-EXQ-590b].gated_on` to reflect F1 cleared by
   Phase-2 implementation + F2 cleared by SD-056 substrate-side.
5. **`evidence/planning/substrate_queue.json` ARC-065 entry.** Mirror
   cross-link gate-status update.
6. **`evidence/planning/v3_exq_571_root_cause_2026-05-25.md`.** Add
   resolution note at the bottom referencing this doc, the implementation
   landing session, and the V3-EXQ-NEW substrate-readiness PASS.
7. **`evidence/planning/behavioral_diversity_isolation_plan.md` GAP-A
   node.** Annotate that Phase-2 MECH-314a implementation cleared the
   per-candidate-bias-channel-structurally-zero blocker for diversity-isolation
   testing on harm-free episodes; cross-link to this architecture doc.

---

## 9. Out of scope (deferred)

- **Strict candidate 4 (z_goal contribution).** Structurally blocked by
  goal_pipeline:GAP-4. Re-evaluate when GAP-4 clears -- but likely as a
  separate sibling MECH-claim, not a MECH-314a re-spec.
- **Strict candidate 3 (residue-coverage delta) as MECH-314a re-spec.**
  Three-loop-strict reading. If user prefers this within-loop-purist option
  over the cross-loop Candidate 5A, this doc should be revised before
  any implementation lands.
- **Per-candidate refinement of MECH-314b (frontopolar uncertainty) and
  MECH-314c (learning progress).** Phase 1 broadcast-scalar; per-candidate
  Phase 2 follow-on deferred until Q-044 surfaces concrete need (per
  MECH-314 parent design doc out-of-scope section).
- **V4 substrate (action-object-grain residues).** Planning-doc Option F.
  V4-or-later.
- **Action-onehot dimensionality projection question.** When the candidate
  signature is augmented with the first-action one-hot, the RBF distance
  is computed in a `world_dim + action_dim` space; the ResidueField centers
  live in `world_dim` only. Two solutions: pad centers with zeros, or
  project augmented features back to `world_dim`. Padding is cheap and
  preserves the action-component spread; projection collapses spread and
  defeats the purpose. The implementation session should pad. Documented
  here as a heads-up.

---

## 10. Recommendation summary

| Aspect | Choice |
|--------|--------|
| Recommended candidate | 5A -- rolling z_world buffer + first-action one-hot augmentation |
| Substrate-readiness | YES (SD-056 + amend landed; MECH-094 substrate already in place) |
| F1 fix (harm-free episodes) | YES (visitation buffer always populates) |
| F2 fix (E2 z_world collapse) | YES via SD-056-ON; substrate-robustness bypass guarantees non-zero spread when SD-056 is OFF |
| Three-loop alignment | Cross-loop modulator at gain-modulator layer (permitted under MECH-069 spirit; biological substrate is ventral-striatum-to-OFC projection) |
| Semantic fidelity to MECH-314a | HIGH (Wittmann 2008 / Bellemare 2016 / Burda 2018 anchors survive) |
| Registry implications | Re-spec of MECH-314a signal source (Phase-1-caveat-level update); no new claim ID required |
| Cost | LOW (~50-80 lines) |
| Bit-identical OFF | Guaranteed by defaults |
| Falsifier experiment | V3-EXQ-NEW 3-arm substrate-readiness diagnostic (BASELINE / VISITATION_ONLY / VISITATION_PLUS_ONEHOT); PASS routes to V3-EXQ-590b Goldilocks retest |
| Runner-up | 5B (z_world buffer + residue-coverage delta) -- preserves harm-coupled reading as secondary; rejected on cost + "secondary is silent in the regime where primary works" grounds |
| Rejected | 3 strict (within-loop purist; gives up Wittmann anchor + F1 silent), 4 (structurally blocked by goal_pipeline:GAP-4), 5C (no Wittmann channel) |

Pending user assent to Candidate 5A, the next session should:

1. Insert the staged Phase-2 implementation entry into
   `evidence/planning/substrate_queue.json` (section 7).
2. Update the existing `MECH-314a-Phase-2` design-question entry per the
   section 7 update list.
3. Land the implementation per the substrate-queue entry's
   `implementation_hint`.
4. Queue the V3-EXQ-NEW substrate-readiness diagnostic per section 6
   falsifier sketch.
5. After V3-EXQ-NEW PASS, queue V3-EXQ-590b Goldilocks retest with
   `curiosity_novelty_source="visitation"`.
6. After V3-EXQ-590b PASS, run the registry / plan-doc / substrate-queue
   updates listed in section 8.

---

## 11. Cross-references

- Companion planning doc: [`evidence/planning/mech_314a_phase2_novelty_source_design.md`](../../evidence/planning/mech_314a_phase2_novelty_source_design.md)
  (2026-05-26 commit `5ec31e39c8`).
- Root-cause finding: [`evidence/planning/v3_exq_571_root_cause_2026-05-25.md`](../../evidence/planning/v3_exq_571_root_cause_2026-05-25.md)
  (REE_assembly master `a79915151b`).
- Substrate-queue entries: `evidence/planning/substrate_queue.json` MECH-314
  (parent), MECH-314a-Phase-2 (design question), MECH-341, SD-056,
  ARC-065.
- Claim registry: `docs/claims/claims.yaml` MECH-314 (parent), MECH-314a/b/c,
  Q-044.
- Phase-1 design doc: [`docs/architecture/mech_314_structured_curiosity_bonus.md`](mech_314_structured_curiosity_bonus.md).
- Three-loop schema: [`docs/architecture/three_loop_learning_channels.md`](three_loop_learning_channels.md)
  (ARC-021 / MECH-069 / MECH-070).
- ARC-062 GAP-B autopsy precedent: `ree-v3/CLAUDE.md` "ARC-062 GatedPolicy
  GAP-B head-input first-action one-hot augmentation" (2026-05-17). The
  canonical first-action one-hot bypass template used in Candidate 2 and
  Candidate 5A's augmentation leg.
- MECH-341 E3 score diversity preservation: [`docs/architecture/mech_341_e3_score_diversity_preservation.md`](mech_341_e3_score_diversity_preservation.md)
  -- Layer-B sibling at the e3_selector site.
- Diversity-isolation plan: [`evidence/planning/behavioral_diversity_isolation_plan.md`](../../evidence/planning/behavioral_diversity_isolation_plan.md)
  GAP-A / GAP-B sections.
- Implementation site (Phase 1): `ree-v3/ree_core/policy/structured_curiosity.py`
  StructuredCuriosity, `_compute_novelty`.
- Score-bias landing site: `ree-v3/ree_core/predictors/e3_selector.py:737`
  (`scores = scores + bias_tensor`).
