# Duvelle et al. 2019 — Insensitivity of place cells to the value of spatial goals in a two-choice flexible navigation task

**Claim tested:** SD-024 (DA-modulated RBF center density)
**Direction:** weakens · **Confidence:** 0.70
**DOI:** [10.1523/JNEUROSCI.1578-18.2018](https://doi.org/10.1523/JNEUROSCI.1578-18.2018) (retrieved via PubMed, PMID 30696727)

## What the paper did

Rats navigated to one of two freely chosen, unmarked goal locations and waited there; waiting triggered release of reward, which was then located and consumed *elsewhere*. The design is deliberate: it separates the spatial goal from the place of reward consumption, so place fields at the goal can be sampled without contamination from consummatory behaviour. The two goals differed in reward amount.

The rats learned the task and preferred the higher-value goal — so they were demonstrably tracking value. CA1 and CA3 place cells were recorded. The authors replicated the known out-of-field goal-related activity (a firing-rate ramp during the waiting period), but found **no general over-representation of goals by place fields** in either region, and **no modulation of place-cell activity by goal value**. Their conclusion: the dorsal hippocampal map is value-free, and links to value represented elsewhere.

## Why this belongs in SD-024's record

This is the principal counter-evidence, and it should be logged as such rather than quietly omitted. It challenges two distinct things SD-024 asserts.

First, the phenomenon itself. SD-024 takes reward-location over-representation as its starting fact. Duvelle et al. looked for it, in two hippocampal subfields, with adequate sampling, and did not find it. That is not a null from a weak experiment — it sits alongside a successful positive replication of the out-of-field goal ramp in the same dataset, which is about as good a positive control as one gets for "we could have seen goal-related signal if it were there in this form."

Second, the scaling. `dopamine_signal = benefit_magnitude * drive_level` implies density should scale with how good the reward is. These animals behaved as though they knew one goal was worth more, and their place cells did not care. If REE's ablation shows density scaling cleanly with `benefit_magnitude`, that is a divergence from the biology, not a convergence with it.

And the authors' positive interpretation — a value-free map that links out to value elsewhere — is an architectural alternative to SD-024's whole premise. It says the hippocampal residue field is the wrong place to put reward-conditioned structure.

## The caveat, which is substantial

The task moves reward consumption *away from the goal*. If the allocating event is reward delivery — as Xiao et al. 2020 report for reward-responsive CA1 cells — then this design may have relocated the dopaminergic event rather than demonstrated its absence. The animal gets its reward somewhere else; nothing DA-driven should be allocating extra resource at the goal.

That distinction matters for how much this paper should move the claim. It is strong against "goal *value* is coded in the map," which is a real and load-bearing part of SD-024's scaling. It is considerably weaker against "*reward encounters* drive local expansion," which is the form the claim actually implements — `accumulate_benefit` fires on a benefit exposure event, at the location of that event. Reading this as a flat refutation would over-state it.

Two further boundaries: dorsal hippocampus only, and a waiting-based task where the goal is defined by a behavioural act rather than by a stimulus, which is unusual and may itself shape what the map represents.

## Confidence reasoning

Source quality 0.85 — J Neurosci, careful controls, both CA1 and CA3 sampled, an internal positive control in the replicated out-of-field effect. Transfer risk standard. Mapping fidelity held down to 0.6 entirely by the goal/consumption dissociation, which is a real confound for reading this result against SD-024's specific triggering mechanism. Logged as **weakens** rather than mixed because the paper's own stated conclusion is squarely against the claim's premise, and the governance record should not soften that by filing it as ambiguous.
