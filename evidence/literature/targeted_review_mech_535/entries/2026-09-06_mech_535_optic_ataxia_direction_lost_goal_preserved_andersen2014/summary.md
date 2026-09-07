# Andersen, Andersen, Hwang and Hauschild (2014) -- optic ataxia and the parietal reach region

**Question served:** Q2 (intention without direction, outside catatonia).

## What the paper is

A Neuron review that walks optic ataxia from Balint's 1909 syndrome to the modular account of posterior parietal cortex built from macaque recording and reversible inactivation. Optic ataxia is "a high-order deficit in reaching to visual goals that occurs with posterior parietal cortex lesions": misreaching in the contralesional visual field, difficulty preshaping the hand, and "an inability to correct reaches online." Patients with the isolated form "have intact visual fields, stereoscopic vision, oculomotor control, proprioception, motor abilities and cerebellar function." They show dysmetria -- overshoot and undershoot -- yet "once the patient receives proprioceptive or auditory cues, they are able to perform the task smoothly." The modular reading assigns reach to the parietal reach region (PRR inactivation produces optic ataxia for peripheral reaches, not saccades), saccades to LIP, grasp to AIP, and state estimation via efference copy to area 5d.

## Why it matters for MECH-535

MECH-535's premise is that a representation can carry goal proximity while losing goal direction, and that this is a real kind of degradation rather than an artefact of one fishtank run. Optic ataxia is the cleanest clinical demonstration that the brain does dissociate exactly here: the goal is seen, wanted and reached for; the motor apparatus is intact; the reach *vector* is wrong. In REE's vocabulary this is INV-088 -- the downstream reader is bounded by what the upstream representation carries -- located in the biological dorsal stream, with PRR as the directional head. So the first half of the claim has a clinical existence proof.

## Why the behavioural signature does not match, and why that is informative

The second half of MECH-535 -- that a reactive actor over such a representation produces a two-cell approach/withdraw cycle -- is not what optic ataxia looks like. The patient misreaches; nothing in the syndrome resembles alternation toward and away from the target. The reason is worth stating because it bears on MECH-536: the clinical actor is not a memoryless argmax that re-decides from the degraded map at every step. It commits to a reach (a wrong one) and executes it, and when online correction is unavailable it simply lands off target. That is a post-commit latch operating over a direction-blind representation -- the exact configuration MECH-536 predicts will "abolish the cycle without restoring competence" -- and the syndrome's phenotype is indeed *no cycle, wrong outcome*. The patient is, in a sense, what the 978 reader would look like with a latch added. That is a resemblance to record as analogy, not to score as evidence, but it is a tighter analogy than the catatonia literature offers.

## Caveats

Whether perceptual target localisation is preserved is debated in the source (spatial disorientation vs an eye-coordinate perceptual deficit), so "goal preserved" is not uncontested. The patient has substitute channels -- proprioception, audition, and Milner et al.'s (1999) delayed perceptual route -- with no counterpart in a reader whose only input is `z_world`. Macaque inactivation transfers to human syndromes with the usual caveats, and neither transfers to a 5x5 grid. Confidence 0.45: high source quality, mapping limited to the premise, high transfer risk.
