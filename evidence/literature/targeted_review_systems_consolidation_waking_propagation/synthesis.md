# Synthesis -- Waking consolidation and propagation to action selection (MECH-261 grounding)

**Pull date:** 2026-04-19
**Target claim:** MECH-261 (mode-conditioned write gating), with cross-support for MECH-092, ARC-038, ARC-039, INV-049, SD-032a
**Entries:** 5

## Question framed

Before implementing MECH-261, we asked: does the biology support the specific
architectural move that an operating-mode variable (from SD-032a) gates which
substrates can write to E3, episodic memory, policy, and autonomic coupling?
MECH-261 generalises MECH-094 (the hypothesis tag) from a single categorical
write-gate to a four-mode family: external_task, internal_planning,
internal_replay, offline_consolidation. The implementation risk is
over-specification -- if biology uses local per-substrate gating rather than
a shared mode variable, MECH-261 is a wrong abstraction.

The specific sub-question this pull addresses is the waking-consolidation bridge:
during waking internal_replay (micro-quiescence, MECH-092), does replayed
content propagate forward into substrates that will subsequently drive action
selection in external_task mode? If it does not, the internal_replay mode is
pointless and should not be distinguished from offline_consolidation. If it
does, the gate architecture is load-bearing.

## What the pull establishes

| Entry | Key contribution |
|---|---|
| Frankland & Bontempi 2005 (NRN review) | Canonical foundation: consolidation redistributes traces from MTL to cortex over time; hippocampal-cortical dialogue drives this. Establishes that the substrates that *could* be written to genuinely differ by mode. |
| Carr, Jadhav & Frank 2011 (Nat Neurosci review) | Awake SWRs split into consolidation-like (quiescence-flanked) and retrieval-like (planning-flanked) subpopulations. Same generator, behaviourally gated downstream effects -- a direct biological precedent for mode-conditioned gating. |
| Rothschild, Eban & Frank 2017 (Nat Neurosci) | Bidirectional cortex-hippocampus-cortex loop around SWR events: hippocampal replay content causally predicts subsequent cortical reactivation. Forward propagation is real. |
| Tambini & Davachi 2019 (TiCS) | Human fMRI: awake reactivation during rest biases subsequent cognition; emotionally arousing replay particularly persistent across mode transitions. The waking propagation bridge. |
| Peyrache et al 2009 (Nat Neurosci) | SWR-coupled replay reaches medial PFC (rule / action-selection cortex), not just sensory cortex. The propagation target includes action-relevant representations. |

## Net biological verdict for MECH-261

**Supports the architectural commitment, with three refinements:**

1. **The four modes do differ in write-eligibility at the biological level**, but
   the segregation is more graded and behaviourally-conditioned than strictly
   categorical. V3 implementation should treat the operating-mode variable as
   a coordinator of gate states rather than a hard switch. A soft-boundary
   implementation (e.g., a vector of per-mode probabilities rather than a one-hot
   categorical) is likely truer to biology.

2. **The salience-network-as-coordinator framing (SD-032a drives operating_mode)
   is a plausible overlay but is not directly validated in the rodent replay
   literature.** The replay-subpopulation segregation Carr/Jadhav/Frank document
   is behavioural-context-driven in their framing; REE posits the salience
   network as the proximate cause. This is a V3-specific prediction that
   implementation should make testable.

3. **The write targets for internal_replay specifically include
   action-relevant cortex** (Peyrache 2009), not just sensory or spatial cortex.
   The V3 implementation should map internal_replay write-eligibility onto a
   PFC-analog / policy-level substrate, not only onto the viability map.

## Load-bearing prediction for V3 design

If MECH-261 is implemented faithfully, the following should hold empirically in
ree-v3 experiments:

- Content active during internal_replay (micro-quiescence, MECH-092) leaves a
  measurable signature on the policy or action-selection substrate that persists
  into the subsequent external_task window -- consistent with Tambini & Davachi's
  cognitive-bias finding.
- Lesioning the SD-032a coordinator (setting operating_mode to a fixed external_task
  value regardless of state) should abolish the forward-propagation bias --
  this would be the causal test of the coordinator overlay.
- The strength of forward propagation should scale with replay intensity, not
  with task context alone -- otherwise the mode gate is redundant.

## Falsification target for MECH-261

If a V3 implementation without the mode variable (pure local per-substrate
gating) reproduces the same behavioural phenomena, MECH-261 is over-specification.
The key behavioural phenomena to reproduce:
- Post-quiescence action-selection bias toward recently replayed trajectories.
- Attenuated cross-mode write bleed during external_task commitment.
- Distinct downstream consequences of quiescence-flanked vs planning-flanked
  replay events.

## Gaps the pull does not fill

- **Direct waking hippocampal-cortical-action-cortex recording** is not
  represented. The waking propagation evidence is human fMRI (Tambini/Davachi)
  or inferred from sleep rodent data (Rothschild, Peyrache). A rodent study
  with simultaneous waking HC + action-relevant cortex during micro-quiescence
  would be the missing piece; it may exist but was not surfaced by this pull.
- **Causal perturbation of the salience-network coordinator hypothesis** is
  absent. Whether lesioning insula/ACC abolishes replay-subpopulation
  segregation is unresolved.
- **Action-selection biasing specifically** (as opposed to memory or perceptual
  biasing) is under-represented. Tambini & Davachi 2019 covers cognition
  broadly but not action-selection narrowly.

These gaps are candidate follow-up lit pulls, not blockers for MECH-261
implementation.
