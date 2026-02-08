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
