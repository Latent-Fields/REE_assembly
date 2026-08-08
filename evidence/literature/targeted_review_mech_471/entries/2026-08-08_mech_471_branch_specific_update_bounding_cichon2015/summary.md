# Cichon & Gan (2015) — Branch-specific dendritic Ca²⁺ spikes cause persistent synaptic plasticity

**Nature 520(7546):180-5 · [10.1038/nature14251](https://doi.org/10.1038/nature14251) · retrieved via PubMed (PMID 25822789)**
**Claim tested: MECH-471 · direction: supports · confidence: 0.80**

## What the paper did

Cichon and Gan imaged apical tuft dendrites of layer V pyramidal neurons in mouse motor cortex with in vivo two-photon microscopy while the animals learned two *different* forelimb motor tasks. Their question is the one MECH-471 is built around, and they state it in the first line of the abstract: the brain has an extraordinary capacity for memory storage, but how it stores new information *without disrupting previously acquired memories* remains unknown.

What they found is that the two tasks do not share substrate. Each task induces dendritic Ca²⁺ spikes on its *own* apical tuft branches, and those branch-specific spikes cause long-lasting potentiation of the postsynaptic spines that happen to be active when the spike is generated. Different competences are written to different addresses.

Then they removed the address separation. Inactivating somatostatin-expressing interneurons made the two tasks frequently induce Ca²⁺ spikes on the *same* branches — and on those shared branches, spines potentiated during one task were depotentiated when they were active seconds before the other task's Ca²⁺ spikes. The consequence was behavioural, not merely synaptic: the increased neuronal activity and the performance improvement the animal had gained from the first task were disrupted when the second task was learned.

## Why this speaks to MECH-471

MECH-471's proposed falsifier is a local-update interference test — train a targeted competence improvement, then measure performance on unrelated previously-acquired competences, and treat measurable degradation as the FAIL that motivates building the discipline. This paper has already run that experiment in a mouse, and it did something better than observe the outcome: it produced the outcome *causally*, by switching off the mechanism that normally prevents it. That gives a much stronger inference than an interference correlation would. Bounding is not incidental to competence storage here; it is load-bearing, and it is a mechanism the animal actively maintains rather than a static fact about how the tissue is wired.

It also, unprompted, satisfies MECH-471's own non-degeneracy guard. The claim warns that testing interference against competences the agent never had is vacuous and should self-route `substrate_not_ready`. Here the interfered-with competence was demonstrably acquired first — there was a measured performance gain to lose — so the disruption is a real degradation of real learning.

The design lesson I take is narrower than "bound your updates", and I think more useful. The bound is enforced by *inhibition* — by SST interneurons keeping the two tasks' spikes on separate branches. That means competence isolation is an active, failable gate rather than a property the substrate gets for free. If REE builds this, the equivalent component is something that can itself be misconfigured or fall over, and it will need its own observability, not just a correctness proof at design time.

## Limitations and what this does not license

Three boundaries, and the first is the one to keep in front of you. The two tasks are both forelimb motor tasks encoded in the same cortical region — they are *adjacent* competences, not "unrelated" in the sense MECH-471's falsifier specifies. So the paper demonstrates interference at closer competence distance than the claim targets. Whether that makes it a stronger or weaker piece of evidence depends on which way you read it: adjacent competences are the *easy* case for interference, so showing it there does not establish that distant competences interfere. It establishes that the substrate needs the bound, not how wide the blast radius would be without it.

Second, the bounding mechanism is biophysical compartmentalisation of a dendritic tree. REE's competence substrate — action objects, learned affordances, predictive models, goal-conditioned policies, rule-state persistence — has no dendrite. The transfer is at the level of design principle, not implementation, and anyone reaching for this entry to justify a *specific* isolation scheme is reaching too far.

Third, and this constrains the whole MECH-471 pull: the paper speaks only to **bounding**. It says nothing about provenance records and nothing about rollback. MECH-471 registers three properties, and this entry evidences one. The Hayashi-Takagi entry in this directory covers the other two, and the two should be read together rather than either being treated as support for the full triple.

## Confidence reasoning

Source quality 0.90 — Nature, in vivo, causal manipulation rather than correlation. Discounted from higher only because this is single-lab work and the behavioural disruption result is the least independently replicated part of it. Mapping fidelity 0.75 — the architectural mapping is genuinely good, held down by the adjacent-versus-unrelated competence gap. Transfer risk 0.35 — mouse motor cortex to an artificial agent is a real distance, mitigated by the fact that what transfers is an abstract constraint on update scope rather than any biological detail. Aggregate 0.80, weighted toward mapping fidelity because MECH-471 is an architectural claim about what discipline is required, not an empirical claim about mice.
