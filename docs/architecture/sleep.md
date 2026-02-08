# Offline Integration and Sleep

**Claim Type:** architectural_commitment  
**Scope:** Offline integration subsystem required for long-term viability  
**Depends On:** INV-010 (offline integration), ARC-007 (hippocampal systems), ARC-005 (control plane)  
**Status:** stable  
**Claim ID:** ARC-011
<a id="arc-011"></a>

---

> **Elaborates Section 4.6 (Offline Integration / Sleep) of `REE_CORE.md`.**

## Offline Sleep & Integration (REE)

This folder specifies the **offline integration ("sleep") subsystem** required by the
Reflective-Ethical Engine (REE).

Sleep is not optional at the architectural level. It is required to:
- Preserve moral continuity without paralysis
- Integrate and contextualise moral residue
- Recalibrate precision and reopen option space
- Improve the fidelity of the world model

Implementations MAY differ.
The interfaces defined here MUST exist.

Source: `docs/processed/legacy_tree/architecture/sleep/README.md`

---

## Sleep Contract (Required Interface)

### Purpose
Offline sleep integrates experience accumulated during online action.
It preserves harm facts while preventing runaway residue and rigidity.

### Inputs
- Replay buffer: (observations, actions, latents, trajectories)
- Residue traces: R values associated with contexts and latent regions
- Precision history: alpha_k values over time

### Outputs
- Updated world model parameters
- Updated residue field R (cleaned, contextualised, compressed)
- Updated precision gains alpha_k

### Invariants
- Genuine harm MUST NOT be erased
- Spurious or misattributed residue MAY be reduced
- Sleep operates on slower timescales than online action

### Failure if omitted
- Residue overgeneralisation
- Moral paralysis or burnout
- Brittle or frozen policy selection

Source: `docs/processed/legacy_tree/architecture/sleep/sleep_contract.md`

---

<a id="mech-030"></a>
## Sleep Modes and Ethical Consolidation (MECH-030)

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

Source: `docs/thoughts/2026-02-08_modes_of_cognition_control_plane_regimes.md`

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- ARC-011
- ARC-007
- ARC-005
- INV-010
- INV-006
- MECH-030

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/sleep/README.md`
- `docs/processed/legacy_tree/architecture/sleep/sleep_contract.md`
- `docs/thoughts/2026-02-08_modes_of_cognition_control_plane_regimes.md`
