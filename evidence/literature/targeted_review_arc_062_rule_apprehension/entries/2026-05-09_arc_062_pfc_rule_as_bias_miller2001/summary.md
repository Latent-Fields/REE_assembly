# Miller & Cohen 2001 — An integrative theory of prefrontal cortex function

According to PubMed: Miller & Cohen 2001, *Annu Rev Neurosci* 24:167-202. [DOI 10.1146/annurev.neuro.24.1.167](https://doi.org/10.1146/annurev.neuro.24.1.167) (PMID 11283309).

## What the paper argues

Cognitive control rests on PFC actively maintaining patterns of neural activity that represent goals and the means to achieve them. These patterns are not motor commands and not perceptual templates; they are bias signals projected from PFC to posterior cortex, basal ganglia, and brainstem. The bias signals do not by themselves cause action — they shape the *flow of activity* along neural pathways that establish proper mappings between inputs, internal states, and outputs for the current task. The framework integrates single-unit recording in primate PFC, neuropsychological lesion data, neuroimaging, and connectionist computational models into a single architectural commitment: PFC is a bias-generation system, and rules are the patterns that get biased.

## What this means for ARC-062 / MECH-309 / ARC-063

Two distinct things land here. **For R1 (discriminator input streams):** the explicit phrase "establish the proper mappings between inputs, internal states, and outputs" is the multi-stream commitment in plain language. The bias-generating substrate reads from at least three classes — exteroceptive perception, internal motivation/state, and ongoing motor context. In REE terms that is `z_world + z_self + z_harm_a`. Single-stream (`z_world` only) is the impoverished case; the framework supports the maximal-input default for ARC-062's discriminator.

**For R3 (gating site):** Miller & Cohen place the rule substrate at PFC and the bias-projection mechanism at PFC-to-posterior-cortex/BG. That maps cleanly to REE option (iii), the score_bias level — exactly where SD-033a's `lateral_pfc_analog.compute_bias()` already lives. The framework treats the bias as additive and continuous, modulating the flow of activity rather than gating discrete action selection. ARC-062's weak-reading two-head + discriminator is a *discrete approximation* of this continuous mechanism; that gap matters and surfaces again in the Rigotti 2013 mixed-selectivity entry.

## What the framework does not arbitrate

It does not pick option (iii) over (i) or (ii). The 2001 review pre-dates the strong hippocampal-replay literature (Pfeiffer & Foster 2013, Carr/Frank/Jadhav) that establishes goal-biased preplay as a real trajectory-proposal-level mechanism, and it does not engage the BG-as-action-reinforcement-interface literature (Gurney/Humphries/Redgrave) that establishes site (i) at the cortico-striatal synapse. So Miller & Cohen anchor option (iii) firmly but do not exclude (i) and (ii). The cleanest reading for ARC-062 is: option (iii) has the strongest single foundational anchor in this body of work, but the existence of (i) and (ii) is not in dispute — the question is which one is *load-bearing* for the SD-054 monomodal-collapse falsifier.

## Confidence reasoning

Source quality is exceptional — this is the canonical PFC integrative theory paper with extensive subsequent empirical support across primate electrophysiology, human fMRI, and computational modelling. Confidence is held below 0.9 because the framework is *general* — it endorses bias-as-rule-substrate but does not adjudicate ARC-062's specific weak-reading architecture (two heads + learned discriminator) versus continuous mixed-selectivity gating. Transfer risk is low: REE's substrate has direct analogues at every level (`lateral_pfc_analog` ↔ PFC, E3 score-aggregation ↔ posterior-cortex/BG bias targets, `rule_state` buffer ↔ active maintenance). The mapping is honest as long as we do not over-claim that this paper *predicts* a discrete two-head architecture — it predicts a bias-projection substrate, and ARC-062 is one valid instantiation of that.

## Failure signature for the cluster

If ARC-062's weak-reading instantiation FAILs the monomodal-collapse falsifier on SD-054, Miller & Cohen's framework points the next investigation at *training* rather than architecture. Their core empirical claim is that PFC bias patterns *develop* with experience (active maintenance is shaped by repeated task performance); a randomly-initialised gated-policy might lack the patterns the bias mechanism is supposed to project. That diagnostic complements (does not replace) the architectural alternative of ARC-063 strong-reading.
