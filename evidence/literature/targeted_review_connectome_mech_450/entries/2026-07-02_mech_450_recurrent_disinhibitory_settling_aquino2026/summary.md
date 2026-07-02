# MECH-450 <- Gallo Aquino, Kim & Rungratsameetaweemana (PLOS Biology 2026)

**"Disinhibitory signaling enables flexible coding of top-down information in cortical networks"** -- DOI 10.1371/journal.pbio.3003831. Columbia Engineering.

## The mapping, stated plainly

MECH-450 is the "minimal recurrent settling step" claim: replace the one-shot pallidal-readout argmin at the end of the E3 selector with a bounded settling competition -- a few rounds of mutual lateral inhibition over the eligible set -- so that selection resolves as a competitive settle rather than a single additive readout. The relevance of this paper is that its whole account of flexible context routing is *recurrent*: a biologically-constrained excitatory/inhibitory network whose disinhibitory connectivity lets it settle into context-appropriate processing states, with the recurrent inhibition-on-inhibition dynamics causally necessary for switching between them. That is congenial to MECH-450's premise -- context-dependent selection is naturally carried by recurrent inhibitory dynamics that settle, not by a one-shot feedforward readout.

## Why I have scored this the lowest of the three

I want to be candid that this is the weakest of the three claim-mappings for this paper, and I have logged it as principle-level corroboration rather than direct evidence. The paper does not isolate a settling *step* as an object of study, it does not benchmark a settling implementation against a one-shot readout (which is the actual comparison MECH-450 lives or dies by), and its recurrence is cortical sensory-context routing, not the basal-ganglia thalamocortical settling MECH-450 targets. So it tells us that recurrent inhibitory dynamics are how this kind of flexible selection gets done in a trained biological-style network -- useful background -- but it does not adjudicate the specific argmin-vs-settle substitution.

The direct-mechanism evidence for MECH-450 already sits in this directory and is stronger on the specific point: Wang 2002 (recurrent-attractor decision dynamics), Morita 2016 and Spreizer 2017 (striatal winner-take-all and its sensitivity), and Rolls 2021 (attractor dynamics and psychiatric failure modes). This entry adds a recent, task-trained, causally-validated instance of "recurrent inhibitory settling beats one-shot readout for flexible context selection," without pretending to be the head-to-head test.

## Confidence

0.48, supports. Source quality is high (0.85), but mapping fidelity is only 0.40 and transfer risk 0.50 because MECH-450's load-bearing content -- the bounded settling step replacing argmin -- is not directly tested here. Honest principle-level corroboration; the argmin-vs-settle comparison still has to come from REE's own falsifier (the ARC-108/MECH-450 learned-gating settling line, e.g. the V3-EXQ-700/707/709 lineage).
