# Summary: Schmidt et al. 2013 -- Neural race model for action cancellation point of no return

**Citation:** Schmidt R, Leventhal DK, Mallet N, Chen F, Berke JD. "Canceling actions involves a race between basal ganglia pathways." Nature Neuroscience. 2013;16(8):1118-24. DOI: 10.1038/nn.3456. PMID: 23852117. (PubMed)

---

## What the paper shows

Schmidt et al. provide direct multi-structure electrophysiology evidence in rats performing a stop-signal task for a "race model" of action cancellation:

- **STN neurons** respond to Stop cues rapidly and non-selectively, regardless of whether cancellation succeeds
- **SNr neurons** only show Stop-cue responses in trials where cancellation is successful
- The race: STN excitation (from Stop cue via hyperdirect pathway) competes with striatal movement-related inhibition (direct pathway) arriving at SNr
- If STN wins the race -- Stop signal arrives at SNr before striatal Go input reaches threshold -- cancellation succeeds
- If striatum wins -- Go momentum reaches the SNr point of no return before Stop signal arrives -- the action is committed and cannot be halted

The paper also demonstrates this through anatomical specificity: the SNr dorsolateral "core" subregion is the site where the race resolves, receiving both inputs.

---

## Relevance to ARC-029

ARC-029's committed-mode gate operates at the moment of action selection, before the point of no return. Schmidt et al. establish what that point of no return is in neural terms:

1. **Point of no return is empirically real**: The commit boundary is not merely a theoretical construct -- it is the moment when striatal Go momentum at SNr exceeds the STN's ability to cancel. This validates the architectural claim that committed and uncommitted modes are distinct states separated by a sharp boundary.

2. **Pre-commitment evaluation window**: The STN win corresponds to the pre-commitment phase where harm-avoidance evaluation can still occur. ARC-016/ARC-029's BetaGate extends this window: higher beta prolongs the STN evaluation phase before striatal momentum closes it.

3. **Harm mechanism**: Actions that pass through committed mode without being canceled during the evaluation window are fully executed. In an environment with hazards, the proportion of harmful committed actions depends on how well the evaluation window screened them. Committed mode with proper evaluation (high BetaGate) should produce lower harm than uncommitted mode (low or absent BetaGate, actions committed without evaluation window).

4. **Environment stability qualifier**: In stable environments, the STN evaluation can reliably classify safe vs. harmful trajectories because the harm-state mapping is predictable. In volatile environments, the evaluation window may be insufficient regardless of its length.

---

## Limitations for REE mapping

- The paper studies single-trial stop-signal cancellation, not sustained committed-mode harm accumulation
- Harm rate in a navigation environment is not measured; cancellation success is the proxy
- The race model describes in-flight action cancellation; REE's commit gate operates at selection/planning time (upstream of the race)
- Rodent stop-signal task to grid-world trajectory: substantial generalization required

---

## Evidence verdict

**Supports ARC-029** (confidence: 0.67). The race model provides neural evidence that the commit boundary is a real, time-resolved neural event with specific anatomy. This validates the existence of the distinct committed/uncommitted neural states that ARC-029's harm prediction is built on. The point-of-no-return mechanism also explains why pre-commitment evaluation (BetaGate) is the only window in which harm avoidance can occur -- once committed, the action cannot be stopped.
