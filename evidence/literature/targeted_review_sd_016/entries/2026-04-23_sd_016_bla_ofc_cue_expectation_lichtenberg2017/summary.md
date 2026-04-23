# Summary: Lichtenberg et al. 2017 — BLA-to-OFC Projection for Cue-Triggered Expectations

**Source:** Lichtenberg, Pennington, Holley, Greenfield, Cepeda, Levine & Wassum (2017). *Basolateral Amygdala to Orbitofrontal Cortex Projections Enable Cue-Triggered Reward Expectations.* J Neuroscience 37(35): 8374–8384. [DOI: 10.1523/JNEUROSCI.0486-17.2017](https://doi.org/10.1523/JNEUROSCI.0486-17.2017)

## What the paper did

Wassum and colleagues used designer receptor-mediated inactivation (DREADDs/hM4Di) to selectively silence either BLA terminals in the OFC or OFC terminals in the BLA in separate groups of rats. This allowed them to ask whether the BLA→OFC projection, the OFC→BLA projection, or both are necessary for outcome-guided behaviour. The outcome-guided behaviours tested were: (1) Pavlovian-to-instrumental transfer (PIT) — whether a cue predicting a specific reward preferentially energises the action that earns that reward; (2) Pavlovian devaluation — whether conditioned approach to a food-predictive cue tracks the current value of that food. Additional control experiments tested instrumental reward-expectation-guided behaviour using non-cue-triggered contingencies.

## Key findings

Inactivating BLA terminals in the OFC (BLA→OFC pathway) selectively disrupted cue-triggered outcome expectations: PIT was impaired (cues could not motivate their specific action), and Pavlovian devaluation responses failed to track current reward value. Crucially, when actions were guided by action-reward contingencies (no cue) or when reward itself was present rather than signalled by a memory-retrieved cue, performance was intact. Inactivating OFC terminals in the BLA had no such effects.

The directionality and cue-selectivity findings together make a strong architectural claim: BLA *sends* outcome representations to OFC specifically when those representations are triggered by environmental cues; OFC-to-BLA feedback does not carry the same function. The OFC cannot retrieve the memory of a cue-associated outcome without BLA input.

## REE mapping

SD-016 registers a z_world-only ContextMemory query path in E1, and the two downstream consumers are E2 (action-affordance bias, MECH-151) and E3 (terrain precision weight, MECH-152). This paper provides the circuit-level evidence that such a path exists biologically: BLA provides the cue-context (cue-associated outcome memory) to OFC (frontal action-evaluation stage), specifically when a cue triggers memory retrieval — not when the outcome is directly presented.

The cue-selectivity finding is particularly important. SD-016's z_world query is designed to activate when E1's ContextMemory is queried by z_world (the exteroceptive latent). The Lichtenberg result confirms that the BLA→OFC channel is selective for *cue-triggered* expectations, not for all outcome-related processing — exactly the architectural boundary SD-016 draws between cue-indexed pre-harm signalling and direct-harm response learning.

The z_world-only (not [z_self, z_world]) query design is also supported: the BLA→OFC projection is a convergent sensory-afferent channel (BLA receives polymodal sensory input), not a proprioceptive-self channel. This maps to SD-016's explicit rationale that the query must be exteroceptive (z_world) not interoceptive (z_self) to match vmPFC/OFC afferent anatomy.

## Limitations and caveats

The paper uses an appetitive (food reward) paradigm in rats; SD-016 is implemented for harm avoidance. The BLA-to-frontal projection topology should be preserved for harm-associated cues — there is extensive evidence that BLA→vmPFC/OFC projections carry both reward and threat representations. However, the parameter regime (threshold, gain, timing) may differ between appetitive and aversive cue-retrieval. The mapping is architectural, not parametric.

This study does not directly test the OFC-to-action-selection pathway downstream of the cue-triggered expectation — it measures the Pavlovian-to-instrumental transfer effect as a proxy. SD-016's E2 action-affordance bias (MECH-151) is a more specific downstream target than the PIT paradigm measures, so there is some mapping indirection.

## Confidence

0.68. Strong method (DREADD directional inactivation, J Neurosci), clean cue-selective effect. Confidence moderate because (1) appetitive =/= harm avoidance, and (2) the architecture maps at the level of BLA-to-frontal projection principles, not at the specific z_world query mechanism.
