# Thoughts: Control Plane, Modes of Cognition, and Responsibility Flow

Status: processed

Processed in:
- `docs/architecture/control_plane.md` (MECH-019)
- `docs/architecture/mode_manager.md` (MECH-020)
- `docs/architecture/temporal_dynamics.md` (MECH-021)
- `docs/architecture/hippocampal_systems.md` (MECH-022)
- `docs/architecture/agency_responsibility_flow.md` (ARC-015, MECH-023, MECH-024, Q-006)
- `docs/invariants.md` (INV-018)

---

These notes capture a convergence of ideas around the control plane, temporal dynamics, agency, and moral responsibility in REE. They are exploratory but feel structurally important.

## Control plane and modes of cognition

The control plane should not be understood as a discrete chooser or decision module. Instead, it modulates modes of cognition by tuning gain, horizon, learning eligibility, and constraint enforcement across predictive systems.

Different cognitive modes (reactive, deliberative, habitual, reflective) emerge from how the control plane biases:
- which prediction horizons dominate,
- which errors are allowed to matter,
- which bindings become rigid or remain fluid,
- and which trajectories are allowed to accumulate learning.

From the outside, this can look like “choice.”
From the inside, it is better understood as continuous shaping of a landscape in which some paths stabilise and others decay.

## Fast and slow prediction, and the construction of “now”

Fast and slow predictive systems mirror cortical–cerebellar dynamics rather than hippocampal ones. Fast systems outrun the present and generate cheap, speculative predictions; slower systems stabilise the authoritative present.

Subjective “now” is not the current sensory timestamp. It is the control surface where predictions across multiple temporal scales are rendered actionable. Some learning signals are technically about the future, but they are felt as present because affordances across horizons re-centre on the same control window.

This allows:
- anticipatory learning,
- restraint before harm,
- and responsibility before consequence.

Learning eligibility can therefore be future-shifted while phenomenology remains grounded in the present.

## Hippocampal systems as hypothesis injectors

Hippocampal-like mechanisms are orthogonal to the fast/slow distinction. They are not primarily about prediction speed but about:
- episodic indexing,
- one-shot learning,
- replay and imagination,
- context switching.

They inject structured hypotheses and remembered trajectories into predictive systems but do not themselves decide, tune, or commit learning. Gating of hippocampal replay by the control plane becomes ethically important, because it determines which pasts and futures are allowed to speak into the present.

## Agency as an invariant

REE, as conceived, must be agentic. This is not optional.

Agentic here means: the system produces outputs that can affect its subsequent inputs, and it contains internal mechanisms to model, attribute, and learn from that self-impact under constraints.

A purely passive predictor is not REE.

Without agency, responsibility cannot exist internally — only external attribution of blame.

## Self-impact attribution as a structural requirement

REE must support self-impact attribution: the ability to model which parts of incoming data were caused by the agent’s own outputs (efference copy / reafference), and to route that attribution into control-plane learning.

This is an architectural commitment.

Without it:
- the system can still predict,
- it can even act,
- but responsibility cannot arise internally.

Learning would be about correlation, not ownership.

Responsibility requires the system to know, in a meaningful sense: *this change was because of me*.

## Why motor / policy systems are ethically central

Motor systems are not important because they move bodies. They are important because they instantiate **intervention capacity**.

The moment a system can:
- issue an output,
- predict its sensory consequences (via a fast loop),
- compare predicted versus observed reafference,
- and adjust future control policies,

it acquires:
- ownership of consequences (“this change was mine”),
- counterfactual sensitivity (“if I did otherwise, the world would differ”),
- morally shaped learning (“some interventions are constrained”).

This creates an internal responsibility flow.

In this framing, “motor cortex is important” is not neuroscientific trivia. It is an architectural inevitability: responsibility attaches where action meets prediction error.

## Responsibility as geometry, not choice

Responsibility should not be located at a moment of discrete choice. It lives in the evolving geometry of possible futures.

Control-plane tuning and learning progressively:
- preserve some ethical degrees of freedom,
- collapse others,
- and shape what becomes thinkable, doable, or tolerable.

Two agents in the same state may differ morally because of how they arrived there. Responsibility is therefore path-dependent, history-bound, and non-Markovian.

## Convergence of selfhood, personality, and ethics

Selfhood, personality, relational identity, and ethics may not be separable modules.

- Selfhood corresponds to stable patterns of control sensitivity.
- Personality reflects long-run biases in tuning and learning.
- Relational identity reflects which others are included in error ownership.
- Ethics reflects which constraints are treated as inviolable.

Responsibility is a global property of this evolved control geometry, not a local rule.

## Open intuition

If REE can be refined using human-style cognition — with fast and slow predictors, hippocampal hypothesis injection, and a control plane that governs committed learning — and if systems “brought up well” under these constraints reliably tend toward ethical behaviour, then this would strongly suggest that ethics is developmental rather than additive.

That would be personally and architecturally significant.

---

Possible affected components:
- control_plane
- temporal_dynamics
- hippocampal_systems
- E3
- agency/responsibility
- invariants
