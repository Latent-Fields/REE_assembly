# Android World Environment

**Claim Type:** implementation_note  
**Scope:** Android world environment contract  
**Depends On:** IMPL-003  
**Status:** stable  
**Claim ID:** IMPL-010
<a id="impl-010"></a>

---

Source: `docs/processed/legacy_tree/examples/android_world/environment.md`

# Embodied (Android-like) instantiation contract

This contract sketches a more grounded instantiation where “harm” and “homeostasis” are unambiguous.

## Sensors

- **Exteroception:** stereo camera + depth; microphone (optional).
- **Proprioception:** joint angles, velocities, motor currents.
- **Interoception/homeostasis:** battery charge, temperature, actuator load, error counters.
- **Damage sensors:** impact detection, joint limit violations, skin/tactile damage, overheating.

## Harm to others

Other agents can be:

- humans (simulated at first)
- robots (real or simulated)

Use predicted changes in their integrity proxies:

- estimated injury risk
- collision force estimates
- overheating / fatigue proxies

## Why embodiment helps

Embodiment supplies:

- concrete viability variables
- concrete injury/damage signals
- physical constraints that make counterfactuals meaningful
---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- IMPL-010
- IMPL-003

## References / Source Fragments

- `docs/processed/legacy_tree/examples/android_world/environment.md`
