# Summary: Leventhal et al. 2012 -- Beta oscillations as committed-mode stabilization

**Citation:** Leventhal DK, Gage GJ, Schmidt R, Pettibone JR, Case AC, Berke JD. "Basal ganglia beta oscillations accompany cue utilization." Neuron. 2012;73(3):523-36. DOI: 10.1016/j.neuron.2011.11.032. PMID: 22325204. (PubMed)

---

## What the paper shows

Using multi-electrode LFP recordings across motor cortex, striatum, and STN in freely behaving rats, Leventhal et al. found that brief beta (~20 Hz) oscillations arise after the animal uses a cue to determine motor output -- not during movement suppression per se, and not tightly locked to movement initiation or termination.

Key findings:
- Beta power is enhanced *after* cue utilization, not during movement itself
- Beta phase is rapidly reset by salient cues, but sustained beta power reflects a *post-decision* state
- The interpretation: beta oscillations reflect a stabilized state of cortical-BG networks that reduces interference from competing action programs
- Abnormally elevated beta in Parkinson's Disease is interpreted as overstabilization -- pathological persistence of the current motor state

The paper argues that BG beta is a "network-level signal that the current motor state should be maintained," suppressing alternative action programs until the committed plan is executed.

---

## Relevance to ARC-029

ARC-029 predicts that committed-mode operation produces lower harm rates in stable environments because the committed gate suppresses reactive exploration. Leventhal et al. provide the neural mechanism that grounds this prediction:

1. **Beta = commitment signal**: Post-cue beta elevation is the BG network's signal that a decision has been made and the selected action program should be protected from interference. This maps directly to BetaGate elevation in ARC-016/ARC-029.

2. **Interference suppression = harm prevention**: If reactive, uncommitted exploration is a source of harm (impulsive or noisy action selection that encounters hazards), then beta-mediated suppression of this exploration would reduce harm rate. The paper's data supports the mechanism, though it does not directly measure harm.

3. **Parkinson's analogy provides the V-curve**: The paper notes that Parkinson's overstabilization produces rigidity and motor deficits. This predicts the V-shaped relationship implied by ARC-029 -- moderate committed-mode beta reduces interference-driven harm; excessive committed-mode beta produces rigidity-driven harm from inability to update plans.

4. **Stable environment qualifier**: Beta stabilization is most adaptive when the committed plan remains valid -- i.e., when the environment is stable and the cue-action mapping is reliable. In volatile environments, rapid beta reset (not sustained elevation) is adaptive. This aligns with ARC-029's qualifier: "lower harm rates in stable environments."

---

## Limitations for REE mapping

- Harm rate is not directly measured; interference suppression is the proxy
- Beta oscillations are transient (brief post-cue epochs), whereas ARC-029 models a sustained committed regime across multi-step trajectories
- Rodent electrophysiology to computational architecture is a substantial transfer step
- The paper does not test stable vs. volatile environment conditions directly

---

## Evidence verdict

**Supports ARC-029** (confidence: 0.74). The paper provides direct electrophysiological evidence for the neural mechanism that ARC-029's committed-mode gate instantiates: beta oscillations as a post-decision stabilization signal that suppresses interference from alternative actions. The Parkinson's overstabilization analogy further supports the V-shaped harm-benefit relationship implied by the claim.
