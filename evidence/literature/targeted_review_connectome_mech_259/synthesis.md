# Synthesis: MECH-259 — Salience-Network Switch Threshold

**Pull date:** 2026-04-20
**Claim:** MECH-259 — When the precision-weighted salience of any input to the salience-network coordinator (SD-032a) exceeds a threshold, the coordinator fires a whole-system mode switch rather than an incremental policy update.

---

## Two-paper biological argument

The case for MECH-259's discrete-switch claim rests on two converging lines of evidence:

**1. Menon & Uddin 2010 (Brain Structure and Function)** establish that the AI/dACC salience network's output is characterised as switching between large-scale networks (DMN and CEN), not merely modulating them. The right anterior insula is the "causal outflow hub" whose activity temporally precedes network transitions. This supports the "switch not modulate" characterisation.

**2. Corbetta, Patel, Shulman 2008 (Neuron)** describe the ventral attention network (anchored in anterior insula) as a "circuit breaker" that interrupts ongoing dorsal-network processing when a salient event is detected. The interruption is event-triggered and transient -- consistent with a threshold-crossing model rather than a continuous gain function.

Together: the salience network produces event-triggered, discrete-class state changes (not smooth adjustments), and the anterior insula is the causal trigger node.

---

## What the evidence grounds vs what remains extrapolated

**Grounded by evidence:**
- The AI/dACC complex drives network-level state transitions when salient events occur.
- The interruption is event-triggered (consistent with threshold-crossing, not continuous integration).
- The output of the AI is a "causal outflow" signal that commits other networks to a new configuration.

**Extrapolated / not yet grounded:**
- The specific threshold mechanism (MECH-259 implements Schmitt-trigger hysteresis).
- The multi-mode operating_mode space (external_task, internal_planning, safe_exploration); the biological literature is largely about a two-network toggle (CEN vs DMN).
- Whether the switch mechanism scales from external-salience (the attentional reorienting domain these papers study) to internally-driven salience (e.g., harm-drive triggered transition from task-focus to internal planning).

---

## Key mapping risk

Both papers study attentional reorienting driven by external stimuli. MECH-259's coordinator also handles internally-driven mode transitions (harm salience from z_harm_a, drive_level, offline-state flags). The biological analogue for internal-state-triggered mode switching is less well-established. This is the main gap to be closed by future pulls.

---

## Confidence summary

| Entry | Confidence | Direction |
|-------|-----------|-----------|
| Menon & Uddin 2010 | 0.72 | supports |
| Corbetta et al. 2008 | 0.67 | supports |
| **Mean** | **0.70** | **supports** |

---

## Suggested follow-up

A third pull targeting papers on the LC-NE (norepinephrine) precision signal and its relationship to discrete attentional mode transitions would strengthen the threshold-mechanism story (Corbetta et al. already implicate the LC-NE system in enabling rapid reconfiguration; this is underexplored in the current pull).
