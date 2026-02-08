# Thoughts: Modes of Cognition as Control-Plane Regimes

Status: processed

Processed in:
- `docs/architecture/modes_of_cognition.md` (ARC-016, MECH-025, MECH-026, MECH-027, MECH-028)
- `docs/architecture/default_mode.md` (MECH-029)
- `docs/architecture/sleep.md` (MECH-030)

---

## Modes of cognition as control-plane regimes

The system should not be understood as running a single mode of cognition. Instead, different cognitive modes emerge from distinct control-plane regimes applied to the same underlying predictive machinery.

These modes are not modules. They are patterns of tuning: changes in gain, horizon, suppression, learning eligibility, and hippocampal gating.

This reframing clarified the architecture significantly.

## Action / Doing mode

In action-oriented cognition:
- prediction horizons are short,
- fast forward models dominate,
- precision is high for motor-relevant errors,
- learning eligibility is tightly coupled to intervention outcomes,
- hippocampal replay is suppressed or tightly constrained.

This is the mode where:
- predictions become interventions,
- interventions generate attributable consequences,
- responsibility learning is strongest.

Ethically, this is where harm can be caused most directly — and where self-impact attribution must be sharp.

## Ready vigilance (alert but not acting)

Ready vigilance is distinct from action.

In this mode:
- the system maintains high sensitivity to external change,
- prediction horizons remain short-to-mid,
- learning eligibility is conservative,
- motor outputs are inhibited but primed,
- hippocampal injection is limited to context-setting rather than replay.

This is a morally important mode: the system is responsible *for restraint*. Many ethical failures occur not during action, but during the failure to maintain vigilance when action was possible.

## Default mode network (DMN) / reflective mode

In DMN-like cognition:
- external precision is lowered,
- internal prediction and replay dominate,
- hippocampal systems inject episodic material freely,
- long-horizon models are explored,
- learning is tentative and low-commitment.

This is not “offline” cognition in a trivial sense. It is where:
- identity is rehearsed,
- narratives are integrated,
- moral simulations occur,
- regret and counterfactuals are explored without immediate consequence.

Ethically, this mode allows learning without harm. Control-plane gating of what *can* be replayed here becomes crucial: excessive replay can destabilise, insufficient replay can freeze growth.

## Sleep modes and consolidation

Sleep is not a single state but a family of control regimes.

Across sleep modes:
- sensory input is largely gated off,
- motor output is inhibited,
- hippocampal replay and cortical consolidation dominate,
- learning occurs without immediate control pressure.

Different sleep stages likely correspond to different balances between:
- replay vs abstraction,
- local vs global consolidation,
- emotional reweighting vs factual integration.

From an ethical perspective, sleep modes are where:
- responsibility learning is integrated,
- emotionally charged interventions are softened or reweighted,
- long-term constraints are stabilised.

This suggests that ethical development depends not only on waking control, but on how learning is consolidated when action is impossible.

## Pathological or extreme modes

The same architecture explains pathological modes:

- Hypervigilance: excessive gain, shortened horizons, suppressed replay.
- Dissociation: weakened self-impact attribution, disrupted binding.
- Rumination: excessive hippocampal replay without control-plane resolution.
- Mania: elevated precision and learning eligibility without constraint.
- Psychosis-like states: failure to suppress internally generated hypotheses.

These are not separate mechanisms; they are mis-tuned control regimes.

This reinforces the idea that ethics, stability, and mental health are co-regulated properties of the same control-plane machinery.

## Architectural implication

Modes of cognition should be treated as first-class architectural phenomena.

They are:
- configurations of the control plane,
- applied to shared predictive engines,
- governing when learning is committed,
- and determining where responsibility can accrue.

There is no single “ethical mode.” Ethical behaviour depends on appropriate transitions between modes, and on the preservation of learning across them.

This makes upbringing, environment, fatigue, trauma, and care structurally relevant — not incidental.

---

Possible affected components:
- control_plane
- mode_manager
- default_mode
- sleep
- responsibility
- E3
