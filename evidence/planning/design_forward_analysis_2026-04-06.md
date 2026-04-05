# Design-Forward Analysis: Non-Contributory Experiment Signals

Created: 2026-04-06
Source: governance-2026-04-06-evening review of 10 experiments (8 FAIL, 1 PASS, 1 diagnostic)
Purpose: Extract design requirements from experiments that governance classified as non-contributory

## Principle

"Non-contributory" is a governance classification (don't weight against the claim). It is NOT a
scientific classification. Every non-contributory experiment carries a design signal. This document
captures those signals and translates them into substrate requirements and superseding experiment
specifications.

---

## 1. z_goal Substrate Failure Cluster

**Affected experiments**: EXQ-228a, EXQ-235, EXQ-237a (+ EXQ-233, EXQ-238 prior sessions)
**Pattern**: z_goal either absent (norm < 0.05) or present but misaligned (norm ok, corr ~ 0)
**Root cause**: SD-012 (homeostatic drive -> z_goal seeding) has never produced z_goal_norm > 0.1

### Failure Taxonomy

| Experiment | z_goal_norm | Alignment | Diagnosis |
|------------|-------------|-----------|-----------|
| EXQ-228a | 0.031 | N/A (below threshold) | z_goal absent -- drive_level not seeding |
| EXQ-235 | 0.182 | corr = -0.046 | z_goal alive but not encoding resource proximity |
| EXQ-237a | 0.011 (long) | N/A | z_goal absent in planning-horizon tasks |
| EXQ-233 | < 0.1 | N/A | SD-012 drive_weight ablation: no weight produces z_goal |
| EXQ-238 | < 0.1 | N/A | SD-012 drive_weight fix: still no z_goal |

### Design Requirements

**DR-1**: z_goal seeding requires more than drive_level scaling. The current formula
(drive_level * benefit_exposure) produces near-zero values because benefit_exposure is sparse.
**Implication**: Either benefit_exposure needs amplification (contact-gated seeding, SD-015),
or z_goal seeding needs a non-homeostatic pathway (e.g., E1 prior association, curiosity signal).

**DR-2**: z_goal norm and z_goal alignment are independent failure modes. EXQ-235 shows norm=0.18
(above threshold) but alignment=-0.046 (random). Even after SD-012 resolves norm, alignment may
still fail. **Implication**: SD-015 (resource indicator encoding) is a separate prerequisite that
creates the mapping from environmental state to z_goal direction.

**DR-3**: z_goal seeding needs different timescales for different tasks. EXQ-237a's simple task
(habit) should work without z_goal, but the long task (planned) requires it. The dual-system test
needs both pathways to be observable independently. **Implication**: Task design must include a
habit-detection phase before testing planned-system added value.

### Superseding Experiment Chain

1. **Gate**: EXQ-247 (SD-011/SD-012 co-integration, currently running)
   - If PASS (z_goal_norm >= 0.1): proceed to step 2
   - If FAIL: SD-012 redesign needed (see DR-1)

2. **Alignment test**: Re-run EXQ-235 protocol with EXQ-247's substrate
   - Success criterion: align_corr > 0.2 (z_goal correlated with resource proximity)
   - If FAIL: SD-015 implementation needed before further testing

3. **Mechanism tests** (require both norm AND alignment):
   - Re-queue EXQ-228a (ARC-032 theta bypass) -- protocol unchanged
   - Re-queue EXQ-237a (MECH-163 dual system) -- redesigned task (see DR-3)
   - New EXQ for ARC-030 Go/NoGo with real z_goal

---

## 2. SD-011 Affective Stream Indistinction

**Affected experiment**: EXQ-241 (both runs: morning + afternoon)
**Pattern**: D3 consistently fails -- R^2(affective) > R^2(sensory) in all 10/10 seeds across 2 runs
**Root cause**: AffectiveHarmEncoder produces output that is a monotone function of HarmEncoder output

### Design Signal

The forward-probe R^2 values tell a clear story:
- R^2_sensory ~ 0.92 (high, as expected -- sensory stream IS the main harm signal)
- R^2_affective ~ 0.97 (HIGHER -- affective is more predictable from harm events)
- cos_sim between streams ~ 0.0 (orthogonal -- the encoder IS producing distinct vectors)

Orthogonality (D1 PASS) without predictability asymmetry (D3 FAIL) means the affective stream
encodes the same information as the sensory stream but in a rotated coordinate system. It's
geometrically different but informationally identical.

### Design Requirements

**DR-4**: The affective stream needs access to information the sensory stream cannot reach:
- Context/history (which environment am I in? what happened before this harm event?)
- Residue field state (accumulated harm map -- spatial/temporal integration)
- Agent state (commitment level, drive_level, goal proximity at time of harm)
This creates genuine functional distinction: sensory = "what hurts now", affective = "what this
harm means in context."

**DR-5**: EXQ-247's SD-011 integration wires z_harm_a into E3 commit gating (urgency_weight,
affective_harm_scale). This creates a functional distinction at the *output* level (different
downstream targets) even if the encoding is informationally similar. D3 should be re-evaluated
after EXQ-247 because the functional role may create a training signal that differentiates the
streams over time.

### Superseding Experiment

EXQ-247 is the gate. If it passes, re-run the SD-011 diagnostic (same D1-D4 protocol).
If D3 still fails: implement DR-4 (contextual input to AffectiveHarmEncoder -- requires
ResidueField.query() as input channel).

---

## 3. Sleep Phase Representational-Behavioral Gap

**Affected experiment**: EXQ-242 (SD-017, ARC-045, MECH-166)
**Pattern**: Slot differentiation WORKS (4/5 seeds) but harm reduction doesn't follow
**Root cause**: Context representation doesn't flow into action selection

### Design Signal

This is the most architecturally informative failure. It means:
- The SWS-analog (context_memory.write of interleaved SAFE/DANGEROUS experiences) successfully
  creates distinct context representations. The mechanism for context abstraction works at the
  representational level.
- But the agent's action selection doesn't read from context_memory. Trajectories are evaluated
  the same way regardless of which context slot is active.

The missing link: **context-conditioned trajectory evaluation**. In the full architecture, E3
should weight trajectories differently based on context (avoid harm-dense trajectories in
DANGEROUS context, explore freely in SAFE context). Without this path, sleep produces knowledge
the agent can't use.

### Design Requirements

**DR-6**: The superseding experiment needs one of:
- Full E3 context-conditioned evaluation (E3 reads context_memory to modulate trajectory scoring)
- A simpler proxy: context-conditioned harm_eval threshold (harm_threshold_dangerous < harm_threshold_safe)
- Even simpler: context_id as an input to action selection (the agent knows which context it's in)

**DR-7**: EXQ-243 (INV-045 phase ordering) also failed for related reasons. The proxy phases
(write to context_memory, gradient update on harm events) don't capture the actual computational
content of SWS (SHY normalization + replay) and REM (precision recalibration via SFSR). The
ordering constraint may only be testable when the phases perform their real computations.
**Implication**: INV-045 is blocked until MECH-120 (SHY), MECH-121 (replay), and MECH-123
(precision recalibration) have first-class implementations. EXQ-245 and EXQ-246 are moving in
this direction but are themselves queued.

### Superseding Experiment Chain

1. Implement context-conditioned E3 evaluation (SD-017 design decision)
2. Re-run EXQ-242 protocol with context->action pathway
3. If slot differentiation still works AND harm reduction now follows: SD-017 PASS
4. Then test INV-045 (ordering) with real SWS/REM computations (post EXQ-245/246)

---

## 4. MECH-153 Context Memory Differentiation

**Affected experiment**: EXQ-239 (supersedes EXQ-187a)
**Pattern**: cosine_sim=1.0 in both supervised AND ablated conditions
**Root cause**: context_memory infrastructure too immature for either pathway

### Design Signal

The supervised loss trains a classification head (terrain_accuracy=0.60) but doesn't push the
underlying latent representation apart (cosine_sim stays 1.0). This means:
- The context_memory write operation may not be differentiable w.r.t. the terrain loss
- Or the cosine_sim metric measures the wrong thing (maybe context vectors are always
  identical because context_memory.write produces a fixed template)
- Or the context_memory capacity is too low (a single vector can't encode context differences
  that the classification head captures via its own parameters)

### Design Requirements

**DR-8**: Before redesigning the experiment, a first-principles analysis is needed:
- What mathematical function must context_memory implement for attribution to work?
- What is the minimal set of operations (read, write, compare, condition-on) that context
  representations must support?
- What training signal should drive differentiation (supervised terrain label, contrastive
  loss between contexts, predictive error difference, or reconstruction loss)?

This is a design exercise, not an experiment. The answer may reframe MECH-153 entirely (e.g.,
from "requires supervised labeling" to "requires contrastive training" or "requires architectural
separation").

---

## 5. MECH-165 Replay Diversity Source Problem

**Affected experiment**: EXQ-244
**Pattern**: Balanced replay did not reliably increase behavioral diversity vs forward-only

### Design Signal

Replay can only diversify behavior if there ARE diverse strategies to replay. In the current
substrate, the agent converges to monostrategy (action_entropy near 0) in most seeds. Forward
replay reinforces this; reverse replay adds the same experience in reverse order -- but the
same monostrategy played backwards is still monostrategy.

### Design Requirements

**DR-9**: The superseding experiment must:
1. Generate diverse behavioral candidates BEFORE replay (random walks, epsilon-greedy exploration,
   explicit strategy injection in warmup)
2. Then test whether balanced replay preserves this diversity (FORWARD should lose it, BALANCED
   should maintain it)
3. The current test asks replay to CREATE diversity from nothing; the correct test asks replay to
   MAINTAIN diversity that exploration created

---

## Summary: Prerequisite Dependency Graph

```
EXQ-247 (SD-011/SD-012 co-integration) [RUNNING]
  |
  +-> z_goal_norm >= 0.1?
  |     YES -> Re-queue: EXQ-228a (ARC-032), EXQ-235 (alignment test)
  |              +-> alignment pass? -> EXQ-237a-redesign (MECH-163), ARC-030 test
  |     NO  -> SD-012 redesign (DR-1: non-homeostatic z_goal pathway?)
  |
  +-> z_harm_a functional distinction?
        D3 pass? -> SD-011 evidence experiment
        D3 fail? -> DR-4: contextual input to AffectiveHarmEncoder

EXQ-245/246 (MECH-120/122 SHY + spindle) [QUEUED]
  |
  +-> First-class offline phases available?
        YES -> Re-run EXQ-242 with context->action pathway (DR-6)
                +-> PASS -> Test INV-045 ordering with real phases (DR-7)
        NO  -> Fix SHY/spindle substrate

MECH-153: needs pipeline mathematical analysis (DR-8) before any experiment
MECH-165: needs exploration+replay paired test design (DR-9)
```
