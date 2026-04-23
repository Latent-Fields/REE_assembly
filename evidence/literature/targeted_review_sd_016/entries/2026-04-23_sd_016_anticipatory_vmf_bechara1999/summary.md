# Summary: Bechara et al. 1999 — Anticipatory vmPFC Signal Before Harm

**Source:** Bechara, Damasio, Damasio & Lee (1999). *Different Contributions of the Human Amygdala and Ventromedial Prefrontal Cortex to Decision-Making.* J Neuroscience 19(13): 5473–5481. [DOI: 10.1523/JNEUROSCI.19-13-05473.1999](https://doi.org/10.1523/JNEUROSCI.19-13-05473.1999)

## What the paper did

Bechara and colleagues administered the Iowa Gambling Task (IGT) to three groups: patients with bilateral VMF (ventromedial frontal) lesions, patients with bilateral amygdala lesions, and healthy controls. Skin conductance responses (SCRs) were measured as an index of somatic state. The critical manipulation was the timing of SCR measurement: SCRs were recorded both *anticipatorily* — during the 5 seconds before each card selection — and *reactively* — immediately after reward or punishment was received. This timing distinction turned out to be the hinge of the whole study.

## Key findings

Both VMF and amygdala patients were impaired on the IGT compared to controls, and neither group developed appropriate anticipatory SCRs (those *before* making a risky choice). However, the two patient groups diverged precisely in the post-outcome period: VMF patients could still generate SCRs *after* receiving punishment or reward; amygdala patients could not. A Pavlovian conditioning experiment confirmed the anatomical dissociation: VMF patients acquired a conditioned SCR to visual stimuli paired with aversive sound; amygdala patients failed to do so.

The dissociation, put plainly, is this: the amygdala is needed to learn that a stimulus is affectively significant at all; the vmPFC is needed to read that learned valence forward in time and generate an anticipatory signal *before harm contact* when the relevant cue is encountered.

## REE mapping

SD-016 explicitly invokes this dissociation in its functional_restatement: it implements the architectural prerequisite for the vmPFC anticipatory signal. The z_world-only ContextMemory query path (not blended with z_self) retrieves harm-associated context when z_world encodes a cue-dense environment. The two downstream signals — E2 action-affordance bias (MECH-151) and E3 terrain precision weight (MECH-152) — correspond to the two functional consequences of the vmPFC anticipatory state: biasing action selection toward harm-avoidance *before* harm occurs, and sharpening harm-sensitivity in the evaluation of candidate trajectories.

The anticipatory/outcome dissociation maps to a design constraint in REE: the z_world-only query must fire and influence E2/E3 *before* any harm signal arrives in the current episode. This is not a post-hoc outcome adjustment — it is cue-indexed pre-contact modulation.

## Limitations and caveats

The somatic marker hypothesis (SMH) as a broader theoretical framework has been critiqued (see Dunn et al. 2005 in this directory) on grounds that alternative explanations for IGT performance exist and that the causal chain from peripheral somatic feedback to vmPFC modulation lacks direct evidence. SD-016's implementation is not committed to a peripheral somatic loop — it is a latent-space internal operation — so the strongest objections to the SMH do not directly challenge SD-016's mechanism. What survives the critique is the empirical finding itself: vmPFC lesion specifically disrupts anticipatory (pre-outcome) signalling while leaving post-outcome reactivity intact. That dissociation is robustly replicated.

An additional caveat is vmPFC localisation: "vmPFC" in Bechara's lesion studies encompasses a broad region including portions of OFC, subgenual cingulate, and ventral prefrontal white matter. SD-016's z_world query path maps to E1's ContextMemory module, which corresponds anatomically to frontal-cue-indexed retrieval. The specific vmPFC subregion generating the anticipatory signal may differ from the subregion most relevant to SD-016's implementation.

## Confidence

0.82. The anticipatory/outcome dissociation is the single most directly relevant evidence for SD-016's design premise. High mapping fidelity because SD-016's functional_restatement explicitly references this paper's paradigm. Confidence is not higher because the vmPFC-specificity of the mechanism is at the level of a regional observation, not a circuit-level demonstration (for that, see Lichtenberg 2017 in this directory).
