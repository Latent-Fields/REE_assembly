# Eysenbach et al. 2018 -- DIAYN: Diversity is All You Need

## What the paper did

Eysenbach, Gupta, Ibarz and Levine introduced DIAYN ("Diversity Is All You Need"), an unsupervised skill-discovery algorithm. The agent samples a discrete (or continuous) skill index `z` at the start of each episode, and is trained to (a) act so that a learned discriminator can recover `z` from visited states (skill-state mutual-information maximisation) and (b) maintain high action-entropy conditional on state and `z` (within-skill exploration). With no reward signal, the agent learns a diverse repertoire of skills -- e.g. running, jumping, and crawling in simulated robotics -- which can then be composed or fine-tuned for downstream tasks.

## Key findings relevant to the rule-apprehension vocabulary question

This paper is uniquely relevant to Pull 4 because it unifies in a single objective the two pathways Pulls 1 and 2 carefully separated: ARC-065 (behavioural diversity generation) and ARC-064 (bottom-up rule discovery / skill extraction). DIAYN's mutual-information objective `I(s; z)` is *both*:

- a diversity-generation force (because the gradient pushes different skills to occupy different state regions, which requires the agent to behave diversely), AND
- a rule-extraction force (because the discriminator that recovers `z` from `s` is exactly the OFC-cognitive-map / MECH-318 rule-state-abstraction-substrate, hosting state-to-skill labels).

For Pull 4's vocabulary-mapping question this matters: in the DIAYN reading, MECH-313 (stochastic-noise-floor) and MECH-316 (cross-episode-regularity-extraction) are not two separate substrates -- they are two readings of one mutual-information objective with different gradient terms. That is a meaningful architectural-economy implication for the planned ARC-064 + ARC-065 cluster registration.

## How the findings translate to REE

If REE adopts DIAYN-style vocabulary, the planned cluster collapses:

- ARC-065 + MECH-313 + MECH-314 -> "max-entropy / skill-conditioned policy" (the action-entropy term H[A | S, z]).
- ARC-064 + MECH-316 + MECH-318 -> "skill discriminator network" (the state-to-skill decoder I(s; z)).
- ARC-062 + gated_policy -> "skill-conditioning input z" (the gating signal that selects which skill is active).

This is a more parsimonious architecture than the current REE proposal. But the parsimony comes at a cost: DIAYN does not naturally model the *online-vs-offline* timing distinction Pull 2 R3 verdict identified (online during waking, offline consolidation), nor the simulation-vs-action gating that REE's MECH-094 hypothesis-tag does. So the mapping is faithful conceptually but loses some REE-specific machinery. That is exactly the kind of trade-off Pull 4 R3 (genuine REE divergences) needs to surface.

## Limitations and caveats

DIAYN's diversity term enforces skill discrimination *via state visitation distinctness*. In environments where skills naturally produce different state distributions (e.g. legged robotics) this works beautifully; in environments where multiple skills can occupy similar states it degenerates. REE's grid-world substrate is borderline -- whether DIAYN-style discrimination works there is an empirical question, not a literature-decidable one.

The other caveat is the offline-then-reuse training schedule. DIAYN typically pre-trains skills without reward, then composes / fine-tunes them for tasks. REE's bottom-up rule discovery is supposed to be continual and online. The closer ML analog for that regime is option-critic with continuous discovery (Bacon 2017) plus a DIAYN-style auxiliary information loss to prevent collapse. That hybrid is sketched in the literature but not packaged as cleanly.

## Confidence reasoning

Scored 0.78. Source quality is strong (ICLR, 4000+ citations, replicated, code public). Mapping_fidelity is high (0.78) because DIAYN gives the cleanest single-objective unification of ARC-065 + ARC-064 we will find in the literature. Transfer_risk is moderate (0.40) because the simulated-robotics empirical regime and offline-then-reuse schedule don't match REE's continual-online substrate; the mapping is conceptually faithful but the operational regime is non-trivial to translate. The verdict this paper feeds: a strong KEEP-AS-IS argument for whatever REE machinery genuinely needs the online-vs-offline / simulation-vs-action distinctions DIAYN cannot represent (Pull 4 R3).
