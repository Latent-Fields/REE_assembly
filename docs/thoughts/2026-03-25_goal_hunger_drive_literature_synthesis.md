Status: processed

Source: Literature hunt session, 2026-03-25 (Claude Code)
Triggered by: EXQ-085 through EXQ-085d all failing at z_goal_norm < 0.1 -- investigation
of root cause revealed missing homeostatic drive modulation as the mechanism gap.

Processed in:
- SD-012 (registered in claims.yaml 2026-03-25): environment.homeostatic_drive
- EXQ-085e design: drive-modulated goal latent experiment

---

## 1. Root Cause: Why z_goal Never Seeds

Codebase investigation confirmed the z_goal wiring is architecturally complete:
- GoalState.update(z_world, benefit_exposure): EMA pull toward z_world when benefit > threshold
- E1 goal conditioning via goal_input_proj (MECH-116)
- E3 trajectory scoring via goal_proximity (MECH-112/117)
- Agent loop calls update_z_goal(benefit_exposure) where benefit_exposure = obs_body[11]

The failure is not a wiring bug. The root cause:
- benefit_exposure is an EMA of raw benefit signals (alpha=0.1)
- Single resource contact -> benefit_exposure += 0.1 * 0.3 = 0.03 (below threshold=0.05)
- Decays at (1-alpha)^n per step: after 10 steps without contact: 0.03 * 0.9^10 = 0.01
- Random-walk rarely produces back-to-back resource contacts
- Goal latent z_goal cannot overcome decay without a reliable above-threshold signal

Underlying biological gap: incentive salience (wanting) scales with drive state, not just
stimulus value. A sated agent encountering food experiences low wanting; a hungry agent
encounters the same food with high wanting and a strong predictive signal. The current
architecture has no drive state in the goal update path.

Agent_energy IS tracked in CausalGridWorld (decays at 0.01/step, restored by resource
contact) and IS in obs_body at index 3. drive_level = 1 - energy is computable without
any environment observation changes. What's missing is using drive_level to gate
GoalState.update() magnitude.

---

## 2. Berridge & Robinson (2016): Wanting vs. Liking

Paper: "Liking, wanting and the incentive-salience theory of addiction"
PMID: 27977239 | DOI: 10.1037/amp0000059

### Core mechanism
Wanting (incentive salience) and liking (hedonic impact) are neurologically dissociable:
- WANTING: large, robust mesolimbic dopamine system. Motivation toward reward-predicting cues.
  Scales with drive state. Can persist and intensify without any subjective liking.
- LIKING: smaller, fragile opioid-mediated systems (nucleus accumbens shell, ventral
  pallidum, parabrachial nucleus). NOT dependent on dopamine.

### Critical dissociation
Dopamine-depleted animals cannot want food but can still show hedonic liking responses
(orofacial 'yum' reactions) if food is placed in their mouths. Conversely, dopamine
activation can produce intense wanting without pleasure.

### Architectural implication for z_goal
z_goal encodes incentive salience (wanting), NOT hedonic value. This means:
- z_goal should be gated/amplified by dopamine-analog signal (which scales with drive level)
- Benefit signals that do not activate wanting (sated state) should NOT strongly update z_goal
- Drive modulation: z_goal update magnitude = f(drive_level) * f(benefit_encountered)
- Specifically: when drive_level ~ 0 (sated), benefit encounters barely update z_goal.
  When drive_level ~ 1 (starving), benefit encounters strongly update z_goal.

The EXQ-085* failures make sense: random-walk in a world with no drive accumulation
produces encounters with resources but without the wanting-amplification that would make
them motivationally salient. z_goal never forms because the agent is effectively always
"sated" (no drive signal present).

---

## 3. Balleine & Dickinson (1998): Goal-Directed Action and Incentive Learning

Paper: "Goal-directed instrumental action: contingency and incentive learning and their
cortical substrates."
PMID: 9704982 | DOI: 10.1016/s0028-3908(98)00033-1

### Core mechanism
Goal-directed action decomposes into two dissociable learning systems:
1. CONTINGENCY LEARNING: the causal link between action and outcome (what produces what).
   Prelimbic prefrontal cortex. Sensitive to action-outcome contingency degradation.
2. INCENTIVE LEARNING: the motivational value of the outcome, dependent on current
   homeostatic state. Insular cortex. Sensitive to outcome devaluation (if you're sated,
   the goal loses motivational pull even if you learned the contingency perfectly).

### Devaluation test (key finding)
Hungry rats trained for two foods (salt-flavored / lemon-flavored polycose) selectively
reduce lever-pressing for the outcome they were just allowed to eat to satiety.
This demonstrates that performance is sensitive to PRIMARY MOTIVATIONAL STATE, not just
to learned values. The goal representation carries current drive information, not a fixed
cached value.

### Architectural implication for z_goal
1. z_goal must implement INCENTIVE LEARNING, not just contingency learning.
   - Agent must know the action-outcome relationship (E2 world model -- contingency)
   - AND the outcome must be valued according to current drive state (drive_level gate)
2. Insular cortex role: interoceptive signals (hunger, thirst) must feed directly into
   the goal-value computation. In REE: drive_level (from obs_body[3]: energy) must
   gate the z_goal update.
3. REPEATED CYCLES REQUIRED: goal representations require multiple cycles of:
   drive-buildup -> action -> outcome -> drive-reduction
   A single resource encounter is insufficient. Resources must respawn to enable
   repeated cycles (resource_respawn_on_consume=True in CausalGridWorld).

---

## 4. Schultz et al. (1997): Dopamine Prediction Errors

Paper: "A neural substrate of prediction and reward."
PMID: 9054347 | DOI: 10.1126/science.275.5306.1593

### Core mechanism
Dopamine neurons in primate midbrain signal REWARD PREDICTION ERRORS:
- Unexpected reward -> dopamine spike (+PE)
- Fully predicted reward -> dopamine at baseline (0 PE)
- Predicted reward omitted -> dopamine dip (-PE)

During learning, dopamine responses TRANSFER from primary rewards to earlier
reward-predicting stimuli (Pavlovian conditioning). The agent learns to predict reward
several steps ahead.

### Architectural implication for z_goal
Goal latent formation is a PE-learning process:
1. Drive builds up (energy decreases)
2. Resource encountered -> drive reduction (unexpected benefit = +PE)
3. z_goal latches onto z_world state that preceded the benefit (+PE signal amplifies update)
4. On repeat cycles, z_goal strengthens each time the drive-reduction PE fires
5. Eventually z_goal reliably predicts drive-reduction: agent has a persistent goal state

This means:
- Goal formation is GRADUAL over multiple reward cycles (not one-shot)
- The PE signal (effective benefit * drive_level) should drive z_goal update
- Without drive_level modulating the "value" of the PE, z_goal cannot distinguish
  a salient hunger-driven benefit from an incidental one

Single resource contacts in EXQ-085d do not produce PE signals because the agent
doesn't have a prior prediction to be surprised by. With drive_level modulation, the
unexpected drive-reduction creates the spike that initiates z_goal formation.

---

## 5. Homeostatic Reinforcement Learning (Keramati & Gutkin 2014)

Paper: "Homeostatic reinforcement learning for integrating reward collection and
physiological stability."
eLife reference (PMC4270100)

### Core framework
Reward = drive reduction, not raw stimulus value:
- Reward_t = -dD/dt where D is drive level
- Encountering food when hungry (drive=0.8): large drive reduction = large reward
- Encountering food when sated (drive=0.05): near-zero drive reduction = near-zero reward

The drive state (D) is a function of homeostatic variables (glucose, hydration, etc.)
Drive is a VECTOR in a multidimensional homeostatic space.

### Architectural implication for z_goal
The benefit signal in REEAgent must be:
  effective_benefit = raw_benefit * drive_level

Not just: effective_benefit = raw_benefit

In current GoalState.update(), the benefit threshold of 0.05 is applied to raw benefit_exposure.
If we instead apply it to drive_level-scaled benefit, the threshold becomes meaningful:
  scaled_benefit = benefit_exposure * (1 + drive_weight * drive_level)
  if scaled_benefit > benefit_threshold: update z_goal

This makes goal formation contingent on BOTH having encountered a resource AND having
been in a sufficiently deprived state -- exactly the HRRL framework.

---

## 6. Oudeyer & Kaplan: Intrinsic Motivation and Learning Progress

Reference: Oudeyer, P-Y, Gottlieb, J & Lopes, M. (2016). Intrinsic motivation, curiosity,
and learning: theory and applications in educational technologies.

### Core mechanism
Curiosity = sensitivity to regions where learning progress (change in prediction error) is
highest. Neither fully predictable nor fully random -- the "zone of proximal development."
Robots develop complex behaviors by chasing their own learning frontier.

### Architectural implication for z_goal
For GOAL LATENT formation specifically, intrinsic motivation via learning progress is
less relevant than homeostatic drive (above). However, it grounds MECH-111 (curiosity /
novelty drive) as a SEPARATE mechanism from z_goal:
- z_goal: approach drive from persistent homeostatic goal (food, safety)
- MECH-111 curiosity: approach drive from novelty/learning progress
These are independent drives with independent activating conditions. Conflating them (as
attempted in EXQ-085c which tried to use curiosity to seed z_goal) is a category error.
Curiosity enables goal-DISCOVERY but doesn't sustain the persistent z_goal latent.

---

## 7. Synthesis: How to Wire z_goal

### What's already correct (no changes needed):
- CausalGridWorld tracks agent_energy (decays, restored by resources)
- drive_level = 1 - energy is in obs_body[3]
- GoalState EMA mechanism is sound
- E1 goal conditioning (MECH-116) and E3 goal scoring (MECH-112) are wired

### What needs to change:
1. GoalState.update(z_world, benefit_exposure, drive_level=1.0):
   effective_benefit = benefit_exposure * (1.0 + drive_weight * drive_level)
   Use effective_benefit for threshold check and update magnitude
   GoalConfig: add drive_weight: float = 1.0

2. REEAgent.update_z_goal(benefit_exposure, drive_level=1.0):
   Pass drive_level through to GoalState
   Caller computes: drive_level = 1.0 - float(obs_body[0, 3])

3. CausalGridWorld: add resource_respawn_on_consume: bool = False
   When True: after resource consumption, spawn a new resource at random available cell
   Recompute resource_field if use_proxy_fields=True
   Required for repeated drive-reduction cycles

4. EXQ-085e experiment:
   - resource_respawn_on_consume=True
   - drive_weight=2.0 in GoalConfig
   - decay_goal=0.003 (slower decay -- half-life ~230 steps instead of ~139)
   - alpha_goal=0.1
   - Curriculum: first 100 episodes, place one resource within 3 cells of agent spawn
   - 500 training episodes per seed (3 seeds x 2 conditions)

### Expected outcome
With drive modulation: benefit_exposure * (1 + 2.0 * 0.8) = 2.6 * benefit_exposure.
At benefit_exposure=0.03 (single contact), effective_benefit=0.078 > threshold=0.05.
z_goal should seed within first ~20 resource contacts (each drive-reduction cycle).
By episode ~100-150, z_goal_norm should reliably exceed 0.1.
