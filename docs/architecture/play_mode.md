# Play Mode

## Definition

**Play** is a bounded behavioral mode defined by three properties:

1. **Synthetic goal and harm signals** — z_goal and z_harm are set arbitrarily (not by homeostatic drive or actual sensory harm), for the duration of the episode
2. **No actual damage or benefit** — the agent's actions have no lasting residue in the environment during play; real stakes are suspended
3. **Learning proceeds as if real** — weight updates flow through E3/E2/E1 as if the synthetic signals were genuine homeostatic and harm signals

The play frame is opened and closed by a **bilateral social signal** co-maintained by the agent and its environment or partner. The signal is externally legible and mutually monitored (see INV-059, ARC-049).

---

## Why Play Is Structurally Necessary (INV-058)

A system that can only learn from real-consequence episodes faces a dilemma:

- **Restrict exploration** to known-safe strategies → safe but non-adaptive; cannot acquire novel goal-pursuit competence
- **Accept harm exposure** during strategy acquisition → adaptive but costly; every novel exploration run risks real harm

Play resolves this by decoupling **strategy acquisition** from **harm exposure**. The agent learns HOW to pursue goals during play; real episodes supply the calibration for WHAT the correct goal intensities and harm thresholds are.

This makes play the **online complement to offline consolidation** (INV-049). Offline consolidation (SWR replay, REM precision recalibration) processes already-acquired experience. Play generates novel experience cheaply enough that consolidation is affordable.

---

## Mechanism: Synthetic Signal Substitution (MECH-194)

During a play episode:

- `z_goal` is seeded synthetically — set to an arbitrary target without requiring `drive_level` elevation (SD-012)
- `z_harm` is set synthetically — harm signals flow but correspond to no real-world harm event
- The play frame tag (ARC-049) marks the episode as authorized-synthetic
- Gradient flow through E3/E2/E1 is **not suppressed** — weights update as if signals were real

Contrast with **simulation** (pre-commit channel, MECH-094): simulation suppresses post-commit learning to prevent counterfactual updates from contaminating real-world weight state. Play does the opposite — it permits full learning while authorizing the synthetic signals as legitimate training targets.

| Mode | Signals | Actions | Learning |
|------|---------|---------|----------|
| Normal | Real | Real | Full |
| Simulation (pre-commit) | Real | Virtual | Suppressed |
| **Play** | Synthetic | Real | Full |
| Sleep replay | Real (consolidated) | None | Full (offline) |

---

## Strategy/Calibration Dissociation (MECH-195)

At play episode close, two things are distinguished:

**What transfers to real episodes:**
- Trajectory competence — E3 has learned goal-pursuit structure
- Action-object associations — which action sequences lead toward goal states
- Policy shape — the general form of goal-directed navigation

**What does NOT transfer directly:**
- Goal magnitude calibration — what intensity of z_goal is appropriate for real drives
- Harm threshold calibration — where the actual harm boundary is

The magnitude calibration is **re-anchored by real homeostatic and harm signals** after play ends (MECH-196). The agent learned how to pursue goals during play; real experience tells it how urgently to pursue them and where the real danger lies.

This dissociation is what makes play productive rather than contaminating. Without it, play-derived goal/harm magnitudes would corrupt real decision-making.

---

## Episode Close and Recalibration (MECH-196)

At play episode termination — triggered by the bilateral frame signal dropping (INV-059, ARC-049) — the agent transitions from synthetic to real signal mode:

1. Frame signal drops (mutual — both agent and environment/partner signal episode end)
2. Real homeostatic drive level overrides synthetic z_goal magnitude
3. Real harm exposure overrides synthetic z_harm thresholds
4. Play-acquired policy structure persists; only the magnitude calibration is reset

**Safety property**: if the frame signal collapses mid-episode (unilateral or signaling failure), recalibration is triggered immediately. This limits the exploitation window: unilateral frame collapse forces real-signal re-entry, not continued synthetic-harm masking.

---

## Frame Maintenance Signal Architecture (ARC-049)

The play frame is architecturally distinct from the hypothesis tag (MECH-094):

| Feature | Hypothesis tag (MECH-094) | Play frame tag (ARC-049) |
|---------|--------------------------|--------------------------|
| Scope | Agent-internal | Bilateral: agent + environment/partner |
| Purpose | Prevents counterfactual learning during simulation | Authorizes synthetic signals as training targets |
| Monitoring | Self-monitored | Mutually monitored, externally legible |
| Failure mode | Tag loss = PTSD/psychosis mechanism | Frame collapse = exploitation or recalibration |

In the **V3 single-agent degenerate case**, the environment is complicit by design (the experimenter sets play mode parameters). The bilateral architecture is the **V4 multi-agent** requirement, where two agents must co-maintain the play frame.

The primate analogue is the **play bow** (episode open signal) and **play face** (ongoing frame maintenance signal). Q-035 asks whether open/close transitions are sufficient or ongoing exchange is required.

---

## Play as SD-012 Curriculum (ARC-050)

SD-012 (homeostatic drive) is currently blocked: `drive_level` must scale `benefit_exposure` to enable z_goal seeding, but EXQ-085 through 085d all fail (z_goal_norm < 0.1).

Play provides an alternative path:

1. Set z_goal synthetically during a play episode (ARC-049 authorizes this)
2. E3 learns goal-pursuit structure against the synthetic z_goal
3. When real homeostatic drive does activate z_goal, E3 already has goal-pursuit competence
4. SD-012 validation becomes: does real drive_level correctly elevate z_goal and engage the already-learned pursuit structure?

This **reverses the apparent dependency**: play enables SD-012 experiments, rather than requiring SD-012 to be solved before play is possible. Play is a prerequisite enabler for SD-012 validation, not blocked by it.

---

## Play Type Developmental Progression (INV-060, MECH-197)

Play is not monolithic. The type of play changes as the agent's subsystem competence develops,
with each type training specific architectural components in dependency order:

### Sensorimotor Play (earliest)

"What happens if I do this?" Repetitive action-outcome exploration.

- **Subsystems trained:** E1 world model (sensory prediction), E2 motor model (action-outcome mapping)
- **Synthetic signal complexity:** single-step goal, binary harm
- **Developmental position:** transition point out of the infant phase (INV-055). The infant's novelty-driven exploration becomes structured as soon as synthetic goals can be set.
- **Frame complexity:** minimal — caregiver maintains frame unilaterally; agent does not yet monitor frame state

### Constructive Play

Building, sequencing, multi-step assembly toward a target state.

- **Subsystems trained:** E2 rollout competence (multi-step forward model), E3 trajectory selection (action sequencing)
- **Synthetic signal complexity:** compositional goals — agent chains actions toward a synthetic target
- **Developmental position:** requires sensorimotor play competence (E1/E2 world and motor models must be functional)
- **What emerges:** trajectory competence (MECH-195's transferable output) first develops here

### Pretend Play (MECH-198)

"This stick is a sword." Counterfactual representation within a play frame.

- **Subsystems trained:** MECH-094 hypothesis tag + ARC-049 play tag intersection; E3 commitment architecture in synthetic mode
- **Synthetic signal complexity:** synthetic *entities* layered on top of synthetic goals — representational substitution
- **Developmental position:** requires constructive play competence (trajectory selection must be functional). This is the first point where the hypothesis tag and play tag co-operate: the agent maintains a counterfactual representation it knows is synthetic, within a play frame with synthetic stakes.
- **What emerges:** full commitment architecture exercised in low-stakes mode; counterfactual reasoning under play-frame protection
- **Testable prediction:** agents whose curriculum skips pretend play should show commitment architecture failures in adult real-consequence operation — specifically: false commits, frame confusion between real and hypothetical (treating real consequences as synthetic), and undertrained commitment gating. A developmental_ablation_discriminative_pair (FULL_PLAY_CURRICULUM vs SKIP_PRETEND) should show this signature.

### Games with Rules

Structured play with agreed-upon constraints, turn-taking, defined roles.

- **Subsystems trained:** social coordination (ARC-047), constraint satisfaction, shared-state monitoring
- **Synthetic signal complexity:** synthetic rules as frame-internal constraints — the play frame has internal structure beyond "this is play"
- **Developmental position:** requires pretend play competence (commitment architecture and counterfactual reasoning must be functional)
- **Frame complexity:** ARC-049 frame becomes structured — not just "this is play" but "this is play with these specific shared constraints." This answers Q-035 empirically: games with rules *require* ongoing shared-state monitoring, not just open/close transitions.

### Cooperative/Social Play

Joint goals, role negotiation, coordinated multi-agent strategy.

- **Subsystems trained:** full multi-agent ARC-049 with mutual frame maintenance, MECH-127 counterfactual other-cost
- **Synthetic signal complexity:** coordinated synthetic goals across agents; shared play-frame
- **Developmental position:** requires games-with-rules competence (shared-state monitoring must be functional)
- **Frame complexity:** full bilateral ARC-049 — agents co-maintain frame as peers. The social harness (ARC-047) scaffolds this until the agents can maintain frames without caregiver assistance.

### Caregiver Role Transition (MECH-199)

The caregiver's role shifts at each developmental transition:

| Phase | Caregiver role | Frame function |
|-------|---------------|----------------|
| Infant (INV-055) | Damage protection (ARC-046) | No play frame; caregiver attenuates real harm |
| Child — sensorimotor play | Frame-setter | Caregiver unilaterally opens/closes play frame |
| Child — constructive/pretend play | Frame-maintainer | Caregiver monitors frame and intervenes if real harm intrudes |
| Child — games with rules | Frame co-participant | Caregiver participates in structured play, models rule-following |
| Child — cooperative play | Scaffolded withdrawal | Caregiver facilitates peer play, begins stepping back |
| Adult | Peer | Mutual frame maintenance without asymmetric authority |

This maps the caregiver requirement (INV-043) onto specific play-type phases: the caregiver
is not just "protecting the child" but *actively maintaining the play frame* that enables
strategy acquisition. The caregiver IS the bilateral frame-maintainer that ARC-049 requires
during the developmental period when the agent cannot yet self-monitor frame integrity.

---

## Frame Integrity: Play vs. Manipulation (INV-059)

If an agent can assert play-frame unilaterally while the partner continues acting under real-harm assumptions, the frame distinction becomes exploitable:

- Agent A asserts play (synthetic harm for itself)
- Agent B believes frame is real (acts under real-harm calibration)
- A causes real harm to B while B's defensive responses are suppressed (B expects play-level harm)

Preventing this requires the frame signal to be **bilateral and monitored**: both parties sustain the signal for the frame to hold. Frame collapse without mutual signal = real harm with reduced defensive response = manipulation.

This is structurally equivalent to the consent requirement in human play: both parties must agree the frame is play, and either party can exit the frame, forcing recalibration.

---

## Open Question (Q-035)

What is the minimal signal architecture for play frame maintenance?

- **Hypothesis A**: A single bilateral open/close signal is sufficient. The frame is established at episode start and terminated at episode end; no intermediate monitoring is needed.
- **Hypothesis B**: Ongoing signal exchange (a continuous play-face equivalent) is required. The frame must be actively re-affirmed throughout the episode.

The answer determines:
- Whether mid-episode frame collapse is detectable before close
- The strength of INV-059's exploitation-limiting property
- Whether ARC-049's implementation requires a heartbeat signal or just open/close transitions

Empirical reference: animal play uses both play bow (open) and ongoing play face (maintenance), suggesting ongoing exchange — but whether both are *necessary* or just *observed* is unknown.

---

## Connections

| Claim | Relationship |
|-------|-------------|
| INV-049 | Play is online complement to offline consolidation |
| MECH-094 | Hypothesis tag analogue; play tag is bilateral where hypothesis tag is internal |
| SD-012 | Play bypasses SD-012 drive_level requirement; enables SD-012 curriculum |
| EXQ-223 | Minimal mind (E1+E2+hippocampus) may use play episodes as training regime |
| ARC-014 | Commitment architecture; play suspends real commit consequences |
| MECH-182-185 | Social signal repertoire; play bow/face are stereotyped signals in this repertoire |
| INV-055 | Infant stage; sensorimotor play is the transition out of infancy |
| INV-041 | Child stage; play-type progression IS the child developmental curriculum |
| INV-043 | Caregiver requirement; caregiver provides frame maintenance during childhood play |
| ARC-046 | Infant hazard protection; predecessor to play-frame protection |
| ARC-047 | Social harness; scaffolds cooperative play before peer-level frame maintenance |
| MECH-189 | Super-ordinal goal formation; constructive and pretend play provide the contexts |
