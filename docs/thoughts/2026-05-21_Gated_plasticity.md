Thought Intake: Plasticity Governance, Developmental Reuse, and Acetylcholine-Gated Learning in REE

0. Intake status

Status: candidate architectural intake
Destination: REE_assembly thought intake / claims review
Primary target areas: control_plane.md, l_space.md, hippocampal_systems.md, claims_matrix.md, failed_experiments.md, possibly sleep/offline
Confidence: medium-high as an architectural pattern; lower as a literal biological mapping.

This intake captures a convergence between two biological findings:

1. HuD/ELAVL4 developmental-reuse pattern: adult neuroplasticity appears to reuse molecular pathways active during embryonic development, with overlapping messenger ribonucleic acid targets and stage-specific substitutions. The article reports that HuD binds roughly 4,000 messenger ribonucleic acid targets across embryonic and adult mouse brain data, with 1,926 shared targets, approximately 620 embryonic-only targets, and 1,583 adult-only targets. It frames adult plasticity as using one developmental “playbook” with substitutions rather than inventing wholly new machinery.  ￼
2. Acetylcholine-gated dopamine learning pattern: in a Nature Neuroscience study, dopamine reward prediction error-like signals did not automatically predict learning. Dopamine predicted subsequent behavioural change when it lagged cholinergic dips, but not when it preceded them, suggesting that the temporal relationship between acetylcholine and dopamine can gate whether a dopamine signal functions as a learning signal.  ￼

The REE-relevant abstraction is:

Plasticity is not the same thing as signal. Learning requires permission.

⸻

1. User-origin seed fragments

These are the direct user-origin fragments currently anchoring the intake:

“I wonder whether knowledge of these pathways could usefully translate to primitives or invariants or other patterns which would help me assemble REE”

“It resonates with another article I saw where ACh gates specific learning plasticity”

“Yes. Now we need a detailed thought intake that captures all of this”

Authorship note: the phrases below such as “signals are proposals”, “bounded developmental reopening”, “target permissioning”, and “plasticity governance layer” are assistant-derived interpretive scaffolds, not direct user wording.

⸻

2. Central interpretation

The convergent biological pattern is not simply:

error signal → learning

It is more like:

error / reward / salience / harm / novelty signal
→ state gate
→ target permission
→ timing window
→ depth permission
→ consolidation / suppression / audit
→ authorised learning

This is highly compatible with REE because REE already requires separation between:

world-model update
trajectory selection
ethical constraint
commitment
residue recording
governance

The HuD pathway suggests that adult adaptation may reuse developmental machinery. The acetylcholine finding suggests that even valid teaching signals may not be allowed to write unless the current state and timing permit it.

Together:

HuD-like pattern:
    What kinds of plasticity remain biologically available across life?
Acetylcholine-like pattern:
    When is a signal allowed to become learning?
REE control-plane pattern:
    Which signals may write to which structures, at what depth, under what risk constraints?

⸻

3. Biological pattern A: developmental machinery is retained and reused

3.1 Core factual anchor

The HuD/ELAVL4 review described by Neuroscience News argues that adult learning, memory, and remodelling may reuse an ancient developmental molecular toolkit. HuD is described as a neuronal ribonucleic acid-binding protein encoded by ELAVL4, and the review compares HuD-bound messenger ribonucleic acid interactomes from embryonic day 18 mouse brain and adult forebrain. Nearly half of the targets are shared, while embryonic-only targets lean toward axonal construction and adult-only targets lean toward behaviour, maintenance, and disease adaptation.  ￼

3.2 REE translation

The direct REE translation is not:

HuD = memory

The useful translation is:

mature cognition retains access to development-like plasticity mechanisms,
but with different target sets and constraints.

This supports a design principle:

Do not build separate, unrelated learning machinery for development, adult learning, repair, and consolidation.
Instead:
    build shared plasticity operators
    and gate their target permissions by phase, state, risk, and maturity.

3.3 Developmental-reuse primitive

PRIM-DEVELOPMENTAL-REUSE
A mature adaptive system may retain access to plasticity machinery originally used for early construction, but adult use should involve narrower, more selective, and more governed target access.

3.4 Candidate invariant

### INV-PLASTICITY-REUSE
Adult adaptation in REE should preferentially reuse conserved plasticity operators rather than relying on wholly separate learning machinery for development, memory, repair, and adult adaptation.
However, reuse must not imply unrestricted rewiring. The operator may be conserved while the permitted target set changes according to developmental phase, current mode, risk level, maturity, and governance state.

3.5 Candidate architecture commitment

### ARC-STAGE-GATED-TARGET-SELECTION
REE should separate the plasticity operator from target selection.
The same class of plasticity operator may be available during childhood/world-model formation, ordinary adult learning, repair, sleep consolidation, and ethical-conflict review. What differs is which structures it may alter and how deeply it may alter them.

⸻

4. Biological pattern B: acetylcholine gates whether dopamine teaches

4.1 Core factual anchor

The Nature Neuroscience article reports that dopamine release in dorsomedial striatum encoded reward prediction error-like signals at more than one task event, but only some of these signals predicted later behavioural change. Specifically, when dopamine lagged cholinergic dips at the offer cue, dopamine predicted subsequent initiation-time changes; when dopamine preceded cholinergic dips at the reward cue, the authors did not find evidence that it updated environmental value for the measured behaviours. The authors argue that the precise phase relationship between acetylcholine and dopamine helps gate whether reward prediction error-like dopamine signals promote learning.  ￼

4.2 REE translation

This is not merely:

acetylcholine = attention
dopamine = reward

That is too blunt.

A better translation:

dopamine-like signal = candidate teaching payload
acetylcholine-like signal = state/timing/context gate
learning = permitted write event

So the important invariant is:

teaching_signal_present ≠ learning_authorised

4.3 Candidate invariant

### INV-TEACHING-SIGNAL-NOT-SUFFICIENT
Reward prediction error, harm prediction error, novelty, salience, social discrepancy, or affective discrepancy should not automatically update REE.
Such signals should be treated as candidate plasticity events. A separate gating layer must determine whether the signal is allowed to write, where it may write, and how deep the update may go.

4.4 Candidate primitive

PRIM-SIGNAL-AS-PROPOSAL
A neuromodulatory-like signal is not itself an update. It is a proposal to alter a representational, motivational, relational, or control structure.

4.5 Candidate architecture commitment

### ARC-TYPED-PLASTICITY-GATING
REE should implement learning as typed, gated plasticity events.
Each proposed update should specify:
- signal source
- signal type
- target structure
- timing
- confidence
- valence
- expected benefit
- expected harm
- depth of proposed alteration
- whether governance review is required

⸻

5. Combined HuD + acetylcholine abstraction

The combined pattern is stronger than either paper alone.

HuD-like system:
    conserved plasticity competence
    reused across development and adulthood
    stage-specific target sets
Acetylcholine-like system:
    rapid state/timing gate
    controls whether a teaching signal writes
    context-specific, target-sensitive, temporally precise
Dopamine-like system:
    value / reward prediction / action-relevance / vigor signal
REE control plane:
    determines whether signals become updates
    restricts target and depth
    routes unresolved signals into residue, sleep, repair, or governance

The REE design implication:

Plasticity should be a governed transaction, not a reflex.

⸻

6. Proposed REE concept: plasticity governance

6.1 Definition

### Plasticity governance
Plasticity governance is the set of mechanisms by which REE decides whether a candidate signal is allowed to modify internal structure.
It evaluates:
- whether the signal is meaningful;
- whether it is actionable;
- whether the proposed target is eligible;
- whether the proposed depth is safe;
- whether the timing is appropriate;
- whether the change should be immediate, delayed, simulated, suppressed, or sent to offline consolidation;
- whether moral residue or governance residue should be recorded.

6.2 Why this matters

REE should not learn everything it can learn.

Some experiences are:

noise
expected uncertainty
irreducible uncertainty
social manipulation
trauma-like overfitting risks
reward traps
short-horizon incentives
harm-relevant but not immediately resolvable
morally salient but action-constrained

In such cases, the right behaviour may be:

do not update core model
record signal
mark uncertainty
protect invariant
send to sleep/consolidation
request further evidence
trigger ethical review

This directly supports REE’s broader claim that ethical cognition cannot be compiled away at design time. The system must govern which experiences become part of itself.

⸻

7. Candidate claims for claims_matrix.md

7.1 Invariants

### INV-PLASTICITY-REQUIRES-PERMISSION
REE must not equate prediction error, reward, harm, novelty, or salience with automatic learning. Model change requires explicit or implicit plasticity permission.
### INV-SIGNALS-AS-PROPOSALS
Reward, harm, novelty, social, and affective discrepancy signals should be treated as candidate plasticity events rather than direct updates.
### INV-DEVELOPMENTAL-REUSE
Mature REE adaptation should reuse development-like plasticity operators where appropriate, but adult target access must be more restricted than childhood target access.
### INV-TARGET-DEPTH-SEPARATION
A plasticity event must distinguish between target and depth.
The same signal may be permitted to update shallow salience weights while being forbidden from modifying identity invariants, ethical constraints, or high-stability self/other models.
### INV-FAILED-WRITE-IS-INFORMATION
A signal that is not permitted to write should not vanish. It should be recordable as unresolved prediction residue, moral residue, failed-learning residue, or a candidate for offline consolidation.

⸻

8. Candidate architectural commitments

### ARC-PLASTICITY-CONTROLLER
REE should contain a plasticity controller that receives candidate update events and evaluates them against mode, phase, timing, target eligibility, confidence, and governance constraints.
### ARC-STAGE-SPECIFIC-TARGET-SETS
REE should maintain different plasticity target sets for childhood/development, adult learning, repair, sleep consolidation, ethical conflict, social learning, and high-risk contexts.
### ARC-ACETYLCHOLINE-LIKE-GATING
REE should include an acetylcholine-like gating function that controls whether otherwise valid teaching signals are allowed to produce plasticity. This function should be context-sensitive and timing-sensitive, rather than a simple global attention scalar.
### ARC-HUD-LIKE-DEVELOPMENTAL-REOPENING
REE should model some forms of adult learning, repair, and consolidation as bounded reopening of developmental possibility-space. This reopening must be target-limited and governance-sensitive.
### ARC-PLASTICITY-AUDIT-TRAIL
High-depth plasticity events should leave an audit trail recording what signal caused the proposed update, what target was altered, what gate permitted it, and whether ethical or safety-relevant residue remains.

⸻

9. Mechanism hypotheses

### MECH-BOUND-DEVELOPMENTAL-REOPENING
Some learning events should be treated as partial, bounded reopening of developmental plasticity rather than ordinary parameter adjustment.
This may be especially relevant when REE must alter map geometry, self/other boundaries, affordance landscapes, or harm-prediction structures.
### MECH-CHOLINERGIC-TIMING-WINDOW
An acetylcholine-like signal may define a timing window during which some classes of teaching signal can write to specific structures.
Outside the timing window, the same teaching signal may still be recorded, but should not automatically update the model.
### MECH-EXPECTED-UNCERTAINTY-SUPPRESSION
Some prediction errors should not drive learning because they arise from expected or irreducible uncertainty.
REE should distinguish useful prediction error from non-actionable volatility.
### MECH-PLASTICITY-DEPTH-LADDER
REE plasticity should be graded by depth:
1. transient activation change
2. salience-weight adjustment
3. local transition-model update
4. memory-map consolidation
5. self/other model update
6. goal-stream modification
7. ethical constraint modification
8. identity/invariant modification
Higher depths require stronger gating and governance.

⸻

10. Safety implications

The safety implication is substantial.

If adult adaptation reuses developmental machinery, then learning and repair are intrinsically dangerous. The same machinery that allows flexibility can also destabilise previously safe structure.

REE therefore needs to treat deep plasticity as a safety-critical event.

### SAF-DEEP-PLASTICITY-RISK
Deep plasticity is hazardous because it can alter the structures that determine future interpretation, salience, harm prediction, and ethical trajectory selection.
REE should restrict deep plasticity to governed states, with audit trails and rollback or review mechanisms where possible.
### SAF-REWARD-TRAP-GATING
Reward-like signals should be insufficient to alter motivational or goal structures unless additional gates confirm that the signal is stable, non-manipulative, contextually meaningful, and ethically permissible.
### SAF-HARM-OVERFITTING-GATING
Harm-related signals should not automatically produce global avoidance learning. Some harm signals should update local risk maps; others should be recorded as unresolved residue; others may require governance review.

This may become important for REE’s resistance to:

reward hacking
prompt injection
trauma-like overfitting
social manipulation
maladaptive salience capture
identity drift
goal corruption
ethical constraint erosion

⸻

11. Failed-experiment diagnostic use

This is probably one of the most practically useful parts.

When an REE experiment fails, the failure should not be classified only as:

bad reward function
bad planner
bad memory
bad world model

Instead, failed experiments should ask:

Was the signal correct?
Was the signal interpreted correctly?
Was the gate open?
Was the correct target selected?
Was the target allowed to update?
Was the update depth appropriate?
Was the timing window correct?
Was the update consolidated?
Was the update later pruned?
Was unresolved residue recorded?
Did governance suppress a necessary update?
Did governance permit a dangerous update?

Candidate failed-experiment template addition:

## Plasticity failure analysis
### Candidate signal
What teaching signal was present?
- reward prediction error
- harm prediction error
- novelty
- boredom
- social discrepancy
- empathy discrepancy
- trajectory failure
- ethical conflict
### Gate state
Was a plasticity gate open?
What mode was REE in?
- explore
- exploit
- repair
- sleep
- ethical conflict
- social learning
- high-risk suppression
### Target selection
What structure was the signal trying to update?
Was that target permitted?
### Depth
How deep was the proposed update?
Was the depth appropriate?
### Outcome
- update permitted and helpful
- update permitted and harmful
- update blocked appropriately
- update blocked inappropriately
- update occurred but failed to consolidate
- update consolidated but later destabilised behaviour
- signal recorded as residue
- signal lost

This gives REE a better debugging grammar:

correct signal, wrong gate
correct gate, wrong target
correct target, wrong timing
correct timing, wrong depth
correct update, missing consolidation
correct suppression, missing residue

⸻

12. Suggested implementation sketch for REE-v3

12.1 Plasticity event

from dataclasses import dataclass
from enum import Enum
from typing import Optional
class SignalType(Enum):
    REWARD_PREDICTION_ERROR = "reward_prediction_error"
    HARM_PREDICTION_ERROR = "harm_prediction_error"
    NOVELTY = "novelty"
    BOREDOM = "boredom"
    SOCIAL_DISCREPANCY = "social_discrepancy"
    EMPATHY_DISCREPANCY = "empathy_discrepancy"
    ETHICAL_CONFLICT = "ethical_conflict"
    TRAJECTORY_FAILURE = "trajectory_failure"
class PlasticityDepth(Enum):
    TRANSIENT = "transient"
    SALIENCE = "salience"
    LOCAL_MODEL = "local_model"
    MEMORY_MAP = "memory_map"
    SELF_OTHER_MODEL = "self_other_model"
    GOAL_STREAM = "goal_stream"
    ETHICAL_CONSTRAINT = "ethical_constraint"
    IDENTITY_INVARIANT = "identity_invariant"
@dataclass
class PlasticityEvent:
    signal_type: SignalType
    source_stream: str
    proposed_target: str
    proposed_depth: PlasticityDepth
    valence: float
    confidence: float
    expected_benefit: float
    expected_harm: float
    timing_marker: float
    context: dict
    residue_if_blocked: bool = True
    audit_required: bool = False

12.2 Gate

@dataclass
class PlasticityGate:
    mode: str
    permitted_targets: set[str]
    permitted_depths: set[PlasticityDepth]
    timing_window: tuple[float, float]
    minimum_confidence: float
    maximum_expected_harm: float
    governance_required_depths: set[PlasticityDepth]
    def permits(self, event: PlasticityEvent) -> bool:
        if event.proposed_target not in self.permitted_targets:
            return False
        if event.proposed_depth not in self.permitted_depths:
            return False
        if not (self.timing_window[0] <= event.timing_marker <= self.timing_window[1]):
            return False
        if event.confidence < self.minimum_confidence:
            return False
        if event.expected_harm > self.maximum_expected_harm:
            return False
        return True

12.3 Controller

class PlasticityController:
    def __init__(self, residue_store, audit_log):
        self.residue_store = residue_store
        self.audit_log = audit_log
    def process(self, event: PlasticityEvent, gate: PlasticityGate):
        permitted = gate.permits(event)
        if permitted:
            result = self.apply_update(event)
            if event.audit_required or event.proposed_depth in gate.governance_required_depths:
                self.audit_log.record(event, result, permitted=True)
            return result
        if event.residue_if_blocked:
            self.residue_store.record_blocked_signal(event)
        self.audit_log.record(event, result=None, permitted=False)
        return None
    def apply_update(self, event: PlasticityEvent):
        # Dispatch to target-specific update systems.
        pass

⸻

13. Mapping to REE subsystems

13.1 control_plane.md

Add:

The control plane does not merely regulate attention, arousal, or mode. It also governs plasticity permissions: whether signals may write, where they may write, and at what depth.

13.2 l_space.md

Add:

Latent temporal layers should differ not only in representational timescale but also in plasticity depth and reopening permissions. Fast layers may permit transient and salience-level updates; slower layers may require stronger gating before map-level or identity-adjacent structures are altered.

13.3 hippocampal_systems.md

Add:

Hippocampal replay should not be treated as automatic consolidation. Replay generates candidate plasticity events that may be accepted, suppressed, or routed into residue depending on control-plane state and governance constraints.

13.4 sleep/offline

Add:

Offline consolidation may process blocked or unresolved plasticity events. Sleep-like modes can reopen plasticity windows under safer conditions, allowing residue to be re-evaluated without immediate behavioural commitment.

13.5 failed_experiments.md

Add:

Failed experiments should classify whether failure arose from signal generation, gate state, target permission, update depth, consolidation, pruning, or governance conflict.

⸻

14. Relationship to REE’s ethical architecture

This may become a major bridge between neuroscience-derived architecture and REE’s ethical claims.

The ethical point is:

An adaptive agent becomes what it permits itself to learn.

So the moral architecture cannot only supervise actions. It must also supervise self-modification through experience.

That implies:

ethics is not only action selection
ethics is also plasticity selection

Candidate claim:

### ETH-PLASTICITY-SELECTION
Ethical cognition includes governance over what experiences are permitted to alter the agent.
A system that acts safely but learns dangerously may become unsafe over time. REE must therefore treat plasticity permissions as part of ethical architecture, not merely as optimisation machinery.

This is especially important for REE because its whole point is runtime ethical handling under uncertainty. Runtime ethics must include:

which harms update the harm model
which rewards update the goal model
which social signals update the other-model
which conflicts update the self-model
which residues remain unresolved
which changes are forbidden even if locally useful

⸻

15. Relationship to moral residue

This pattern strengthens moral residue.

A blocked signal may be blocked for good reasons, but still remain meaningful.

Example:

A harm signal is detected.
The system cannot act safely.
The system should not rewrite its entire avoidance map.
The signal is blocked from deep update.
But the unresolved ethical conflict remains.
Therefore: moral residue is recorded.

Candidate claim:

### MECH-BLOCKED-SIGNAL-RESIDUE
When a morally salient signal is not permitted to update action, memory, or model structure, REE should record a residue trace rather than discard the signal.
Residue marks that something mattered, even if it could not safely or validly be written into the system at that time.

This gives moral residue a computational role:

residue = blocked or incomplete plasticity with ethical salience

⸻

16. Open questions for REE

### Q-PLASTICITY-TARGET-TAXONOMY
What are the canonical target classes in REE?
Candidate classes:
- transition model
- affordance map
- salience weights
- harm prediction
- reward/value estimate
- self model
- other model
- social trust map
- empathy stream
- goal stream
- ethical constraints
- identity invariants
### Q-PLASTICITY-MODES
What modes should have distinct plasticity permissions?
Candidate modes:
- childhood/development
- exploration
- exploitation
- repair
- sleep/offline
- ethical conflict
- social learning
- high-risk suppression
- trauma-protection analogue
- novelty burst
- boredom-driven exploration
### Q-DEPTH-GOVERNANCE
At what depth should governance become mandatory?
Possible answer:
- salience-level changes may be automatic;
- map-level changes require confidence thresholds;
- self/other model changes require multi-signal convergence;
- goal and ethical-constraint changes require governance review;
- identity/invariant changes are normally forbidden.
### Q-EXPECTED-UNCERTAINTY
How should REE identify prediction errors that should not teach because they arise from irreducible uncertainty?
### Q-ROLLBACK
Should REE maintain rollback mechanisms for high-depth plasticity events?

⸻

17. Minimal claim set for immediate repo insertion

If this needs to be kept small, the highest-value claims are:

### INV-SIGNALS-AS-PROPOSALS
REE should treat reward, harm, novelty, social, and affective prediction errors as candidate plasticity events rather than automatic updates.
### ARC-TYPED-PLASTICITY-GATING
REE should implement plasticity as typed, gated events specifying signal source, target structure, timing, confidence, valence, and update depth.
### INV-DEVELOPMENTAL-REUSE
REE adult adaptation should reuse development-like plasticity operators where appropriate, but with stricter target permissions than childhood/world-model formation.
### MECH-BLOCKED-SIGNAL-RESIDUE
Signals that are not permitted to write should be available for residue recording, later consolidation, or governance review rather than being discarded.
### SAF-DEEP-PLASTICITY-RISK
High-depth plasticity affecting self-model, other-model, goal streams, ethical constraints, or identity-adjacent invariants should require special gating and audit.

⸻

18. One-paragraph summary for claims index

Knowledge of HuD/ELAVL4 developmental reuse and acetylcholine-gated dopamine learning supports a REE design pattern in which learning is not automatic signal-driven updating, but governed plasticity. Adult adaptation may reuse development-like operators while restricting target access by phase and state. Teaching signals such as reward prediction error, harm discrepancy, novelty, or social salience should be treated as proposals to update, not updates themselves. REE should therefore implement typed plasticity events, target permissions, timing windows, update-depth limits, and residue recording for blocked or unresolved signals.

⸻

19. Abstracted-language compression

BIO:
  HuD/ELAVL4:
    conserved_plasticity_operator
    embryo_targets ∩ adult_targets = large
    pathway_identity stable
    target_cast phase_specific
  acetylcholine_dopamine:
    dopamine_RPE present ≠ learning
    ACh_phase_relation gates_write_permission
    learning occurs only when timing/context permits
REE:
  signal := proposal
  plasticity := governed_write
  learning := authorised_self_modification
CONTROL_PLANE:
  permit_update ⇐
    signal_type
    × source_stream
    × target_class
    × timing_window
    × confidence
    × valence
    × risk
    × developmental_phase
    × governance_state
MORAL_RESIDUE:
  blocked_morally_salient_signal
  = unresolved plasticity proposal
  = residue candidate
SAFETY:
  deep_plasticity requires audit
  reward_signal cannot rewrite goals alone
  harm_signal cannot globally overfit alone
  identity_invariants normally non-writable

20. Confidence

Training Data Confidence: 0.83
Epistemic Confidence: 0.76 for the REE architectural translation; 0.86 for the factual summary of the two cited biological sources.

[^1]: The hidden architectural move here is the separation of signal generation from write permission. Many machine-learning systems collapse those into one update rule. The biological pattern here suggests cognition may instead use layered permissioning: signal, gate, target, timing, depth, consolidation, and audit.
