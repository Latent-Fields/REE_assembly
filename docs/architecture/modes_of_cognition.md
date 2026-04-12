---
nav_exclude: true
---

# Modes of Cognition as Control-Plane Regimes

**Claim Type:** architectural_commitment  
**Scope:** Control-plane regimes that shape cognitive modes  
**Depends On:** ARC-005 (control plane)  
**Status:** provisional  
**Claim ID:** ARC-016, MECH-157
<a id="arc-016"></a>

---

The system should not be understood as running a single mode of cognition. Instead, different cognitive modes emerge from distinct control-plane regimes applied to the same underlying predictive machinery.

These modes are not modules. They are patterns of tuning: changes in gain, horizon, suppression, learning eligibility, and hippocampal gating.
Modes are labels over stable regions of control-channel space (arousal baseline/volatility, readiness, veto, precision/gain), not separate control units.

**Subsystem abstract (core claims):** ARC‑016 establishes modes as control‑plane regimes, while MECH‑025 through MECH‑028
define the action, vigilance, pathological, and ethical implications of those regimes. Supporting context includes ARC‑005
(control plane), ARC‑015 (responsibility flow), INV‑012 (commitment gates responsibility), and MECH‑019/MECH‑020.

This reframing clarified the architecture significantly.

Source: `docs/thoughts/2026-02-08_modes_of_cognition_control_plane_regimes.md`

---

<a id="mech-025"></a>
## Action / Doing Mode (MECH-025)

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

Source: `docs/thoughts/2026-02-08_modes_of_cognition_control_plane_regimes.md`

---

<a id="mech-026"></a>
## Ready Vigilance (MECH-026)

Ready vigilance is distinct from action.

In this mode:
- the system maintains high sensitivity to external change,
- prediction horizons remain short-to-mid,
- learning eligibility is conservative,
- motor outputs are inhibited but primed,
- hippocampal injection is limited to context-setting rather than replay.

This is a morally important mode: the system is responsible *for restraint*. Many ethical failures occur not during action, but during the failure to maintain vigilance when action was possible.

Source: `docs/thoughts/2026-02-08_modes_of_cognition_control_plane_regimes.md`

---

<a id="mech-027"></a>
## Pathological or Extreme Modes (MECH-027)

The same architecture explains pathological modes:

- Hypervigilance: excessive gain, shortened horizons, suppressed replay.
- Dissociation: weakened self-impact attribution, disrupted binding.
- Rumination: excessive hippocampal replay without control-plane resolution.
- Mania: elevated precision and learning eligibility without constraint.
- Psychosis-like states: failure to suppress internally generated hypotheses.

These are not separate mechanisms; they are mis-tuned control regimes.

This reinforces the idea that ethics, stability, and mental health are co-regulated properties of the same control-plane machinery.

Source: `docs/thoughts/2026-02-08_modes_of_cognition_control_plane_regimes.md`

---

<a id="mech-028"></a>
## Architectural Implication (MECH-028)

Modes of cognition should be treated as first-class architectural phenomena.

They are:
- configurations of the control plane,
- applied to shared predictive engines,
- governing when learning is committed,
- and determining where responsibility can accrue.

There is no single “ethical mode.” Ethical behaviour depends on appropriate transitions between modes, and on the preservation of learning across them.

This makes upbringing, environment, fatigue, trauma, and care structurally relevant — not incidental.

Source: `docs/thoughts/2026-02-08_modes_of_cognition_control_plane_regimes.md`

---

<a id="mech-157"></a>
## External/Internal Precision-Routing Table (MECH-157)

The MECH-025 through MECH-028 modes (Action/Vigilance/Pathological) describe one
dimension of mode space — oriented around readiness, responsibility, and pathology.
An orthogonal dimension describes the **degree of external vs internal coupling**:

| Mode | Sensory Gain | Hippocampal Drive | Rollout | Primary Function |
|------|-------------|------------------|---------|-----------------|
| External | High | Low | Low | Perceptual grounding in current environment |
| Internal | Low | High | High | Simulation, imagination, planning |
| Mixed | Medium | Medium | Medium | Grounded planning; working memory |
| Replay | Very Low | Very High | Structured | Offline learning, consolidation |

These are not separate systems — they are precision-routing configurations applied to
the same E1 associative substrate (MECH-154). The same deep world model supports
both perceptual coupling (External) and generative imagination (Internal); what
differs is the balance of sensory precision vs hippocampal drive.

**Relationship to MECH-025-028:** These two mode dimensions cross each other:
- Action mode (MECH-025) is typically External or Mixed
- Ready Vigilance (MECH-026) is External
- Replay corresponds to a maintenance/quiescent sub-mode of the system
- Pathological modes (MECH-027) can involve being stuck in one pole of the
  External/Internal axis (hypervigilance = locked External; rumination = locked Internal)

**Developmental prerequisite:** The External mode must be trained before Internal
mode can be productive. Rollout on an untrained E1 manifold produces unstable
simulation (hallucination, confabulation analogues). This is the developmental ordering
captured in ARC-042 and INV-041.

**Control-plane implementation:** Switching between External and Internal coupling is
a control-plane operation (precision routing on alpha_S, tau_E2, and hippocampal drive
gain), not a local circuit property. This is an architectural commitment: mode switching
is not passive or emergent — it requires explicit control.

Source: `docs/thoughts/2026-04-01_Parietal_systems_thought.md`

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- ARC-016
- MECH-025
- MECH-026
- MECH-027
- MECH-028
- ARC-005
- ARC-015
- INV-012
- MECH-154 (E1 as associative manifold — substrate for mode switching)
- MECH-157 (External/Internal precision-routing table)
- ARC-042 (E3 dark until E1/E2 substrate ready -- developmental prerequisite)
- INV-041 (Childhood phase as architectural prerequisite)

## References / Source Fragments

- `docs/thoughts/2026-02-08_modes_of_cognition_control_plane_regimes.md`
- `docs/thoughts/2026-04-01_Parietal_systems_thought.md`
