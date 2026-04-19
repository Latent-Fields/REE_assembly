# Mayberg et al 2005 — sgACC DBS reverses treatment-resistant depression

## What the paper did

Mayberg and colleagues implanted bilateral deep brain stimulators targeting the subcallosal cingulate white matter (Brodmann area 25, the sgACC) in six patients with severe treatment-resistant depression. Stimulation suppressed local sgACC activity. Four of six patients reached clinical remission or near-remission within six months; PET imaging showed normalisation of resting metabolism across a distributed mood-regulation network (sgACC itself, orbitofrontal cortex, medial frontal cortex). The effect was durable at follow-up and reversed on stimulator interruption in case reports that followed.

## Key findings relevant to SD-032e

The paper established sgACC as a *setpoint node*: its sustained activity level appears to bias the entire affective system toward or away from depressive phenotype. This is mechanistically distinct from reactive signal generation — sgACC does not fire transiently in response to a sad stimulus; its *tonic* level acts as a slow bias on valence-processing downstream. That is a very close structural match for what SD-032e proposes: a pACC/sgACC-analog that integrates sustained affective pain and writes into a slow baseline which in turn biases downstream salience and evaluation.

## Translation to REE

This paper is the strongest direct evidence in the neuroscience literature that pACC/sgACC implements a write-into-setpoint architecture, as opposed to a reactive evaluator or a fast autonomic effector. If SD-032e accepts Mayberg as anchor, one architectural consequence follows sharply: the write target should be valence-signed. sgACC does not modulate an unsigned energetic variable; it modulates mood — an affective baseline with positive and negative poles. REE's current drive_level (SD-012) is effectively unsigned (1 - energy), which means a literal mapping of Mayberg onto drive_level is a shape mismatch.

The cleanest architectural options are: (a) register a separate valence setpoint variable alongside drive_level and have SD-032e write there; (b) extend drive_level to carry a valence component and have SD-032e write into that component; or (c) accept the shape mismatch and frame SD-032e as a simplification that compresses sgACC's valence-setpoint role onto REE's nearest existing scalar, with the mismatch documented. Option (c) is the lowest-cost move and is defensible for a first-pass substrate; it should not be defended as biologically tight.

## Limitations and caveats

The clinical trial is small (n=6) and open-label. Subsequent randomised trials of sgACC DBS (notably BROADEN) failed to replicate the effect size, though later stimulation-targeting refinements recovered some of it. DBS current spreads; sgACC-specific attribution is imperfect. Most importantly for our mapping: the clinical effect is embedded in dopaminergic and serotonergic neurochemistry that REE does not simulate, so the *mechanism* of the setpoint write may not transfer even if the *architecture* does.

## Confidence reasoning

Confidence is 0.65. Source quality is moderate-high — the paper is seminal and has shaped two decades of affective-circuit research, but the replication story is mixed. Mapping fidelity is limited by the valence-vs-unsigned-drive distinction: Mayberg unambiguously shows a write into a valence setpoint, and treating drive_level as a valence proxy is a real stretch. Transfer risk is elevated for the neurochemical reasons above. This paper anchors the architectural move (write-into-setpoint) but *refines* rather than confirms the specific choice of drive_level as the target.
