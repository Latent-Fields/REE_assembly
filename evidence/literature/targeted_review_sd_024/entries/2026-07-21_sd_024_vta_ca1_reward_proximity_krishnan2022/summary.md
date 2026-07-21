# Krishnan et al. 2022 — Reward expectation extinction restructures and degrades CA1 spatial maps through loss of a dopaminergic reward proximity signal

**Claim tested:** SD-024 (DA-modulated RBF center density)
**Direction:** supports · **Confidence:** 0.82
**DOI:** [10.1038/s41467-022-34465-5](https://doi.org/10.1038/s41467-022-34465-5) (retrieved via PubMed, PMID 36333323)

## What the paper did

Mice ran a virtual-reality linear track with a reward at a fixed location, under two-photon calcium imaging of CA1 — and, crucially, of VTA dopaminergic axons *within* CA1. The authors then extinguished reward expectation and asked what happened to the map. They also ran the complementary causal manipulation: optogenetic inhibition of VTA dopaminergic neurons, with reward still present.

The dopaminergic axons in CA1 turned out to carry a ramping signal that grows as the animal approaches reward — a reward-proximity signal — and that ramp is itself dependent on the animal expecting reward, not merely on proximity as a geometric fact. When expectation was extinguished, place-cell over-representation of the reward location vanished, remapping across the whole environment increased, and trial-to-trial field reliability fell. Inhibiting the VTA dopaminergic neurons largely reproduced that whole pattern.

## Why this matters for SD-024

This is the closest thing in the literature to a direct causal test of what SD-024 assumes. The claim's premise is not that reward locations happen to be better represented — that could fall out of visit frequency, or of sensory salience, or of the environment simply being richer near the goal. The premise is that a *dopaminergic signal* is the thing doing the allocating. Krishnan et al. supply exactly that arrow: remove the DA signal, lose the over-representation, with the animal still engaged and the environment unchanged.

It also, more quietly, supports the SD-012 scaling decision. The measured signal is expectation-dependent, which is what `dopamine_signal = benefit_magnitude * drive_level` is trying to capture — a reward encounter matters more when the agent wanted it. A purely delivery-triggered signal would not have shown the ramping-to-expectation profile the imaging found.

And the extinction result speaks directly to one of SD-024's declared informative failure modes. When reward stops arriving, the biological over-representation *goes away*. That is what the FIFO center lifecycle is supposed to reproduce by natural decay. If REE's expansion persisted after reward removal, the claim's own note calls that "craving" — and this paper says the healthy pattern is the opposite.

## Limitations and the honest caveat

The dependent variable here is the distribution and reliability of place *fields* in a real CA1 population. SD-024 asserts something narrower and more architectural: that extra RBF centers get allocated, in a fixed-capacity field, per DA-scaled reward event. A dopaminergic gain change on an existing population would produce everything this paper measured without producing anything SD-024 specifically claims. So the paper licenses the *dependency* — DA causes reward-location representational advantage — and is silent on the *implementation*. That silence is precisely why `compute_local_density` was built weight-independent, and why MECH-232 is still candidate.

The setting is also thin: head-fixed mice, virtual-reality linear track. That is a narrower world than the z_world neighbourhood SD-024's jittered cluster is meant to abstract, and one could reasonably worry that a 1D track with one reward is where over-representation is easiest to find.

## Confidence reasoning

Source quality is high — circuit-specific optogenetics converging with a behavioural manipulation, in a strong venue. Transfer risk is moderate but tolerable, because what is being transferred is a dependency structure rather than a parameter. The limiting term is mapping fidelity at 0.7: right causal arrow, wrong grain. That is what holds the aggregate at 0.82 rather than higher.
