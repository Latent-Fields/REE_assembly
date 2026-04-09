# Summary: Dayan & Huys 2009 -- Serotonin in Affective Control

**Entry:** 2026-04-09_inv_052_serotonin_affective_control_dayan2009
**Claim tested:** INV-052
**Evidence direction:** supports

## What the paper did

Dayan and Huys wrote this Annual Review of Neuroscience piece as the canonical computational treatment of serotonin's role in motivated behaviour, tracing the evidence from invertebrates through to mammals. The review does something unusual for its era: rather than treating 5-HT as a single-dimensional "mood regulator," it attempts a principled computational decomposition of what serotonin actually does in the architecture of decision-making under aversive conditions. The core move is to treat serotonin as playing a role analogous to, but importantly asymmetric with, dopamine -- dopamine codes opportunity cost for reward; serotonin codes something analogous for the aversive side, but the natural statistics of punishments are not simply the inverse of rewards.

## Key findings

The key computational argument is the asymmetry claim: aversive statistics in natural environments do not mirror appetitive statistics, which means a tonic regulatory system specifically calibrated for harm environments is architecturally necessary -- you cannot simply run dopamine backwards. The review also establishes that serotonin's role extends across multiple timescales: phasic 5-HT responses encode immediate aversive prediction errors, while tonic 5-HT levels modulate the sustained regulation of approach vs avoidance in ongoing behavioural sequences. The paper documents that reducing 5-HT tone (via depletion or receptor blockade) impairs sustained goal pursuit in environments with intermittent punishment, not just the processing of individual aversive events. This dissociation between phasic signal and tonic floor is the empirical crux supporting INV-052.

## Translation to INV-052

The asymmetry argument is the strongest single piece of support for INV-052's core claim. INV-052 asserts that a *tonic* regulatory system is required -- not just that serotonin participates in aversive processing. The Dayan-Huys asymmetry argument explains *why* tonicity is required: if punishment statistics were mirror-symmetric with reward statistics, one could imagine a unified phasic system handling both. The natural asymmetry (punishments cluster differently, carry different uncertainty structure, and have different temporal dynamics) necessitates a dedicated regulatory layer that operates on longer timescales than individual events. In REE terms, this is exactly what MECH-186 provides: a tonic floor that maintains the benefit gradient representation even when harm signals are locally dominant.

The review's multi-timescale framing also provides indirect support for MECH-187 and MECH-188. The finding that 5-HT depletion impairs sustained goal pursuit -- not just single-trial aversive processing -- is the behavioural signature of transduction and maintenance stage failure: the animal can still sense harm and approach, but cannot sustain the benefit-oriented trajectory across terrain.

## Limitations

The review is theoretical-computational: it synthesises evidence but does not present original data. The mapping from RL value functions to REE's latent terrain architecture requires an additional translation step that Dayan and Huys do not take. More importantly, the review acknowledges that human behavioural data on tonic 5-HT's role remains inconsistent -- the tonic floor claim rests more firmly on rodent pharmacology and invertebrate circuitry than on direct human evidence. The three-stage INV-052 decomposition is not present in the source; it is an REE-side inference from the review's unified treatment.

## Confidence reasoning

Annual Review of Neuroscience is the field's gold standard for authoritative reviews; Dayan and Huys are the canonical computational voices on serotonin. The asymmetry argument is logically compelling and empirically grounded in multi-species data. Confidence at 0.75: slightly higher than the 2008 paper because the review makes the tonic vs phasic distinction more explicitly and provides the asymmetry argument that is the strongest positive case for INV-052's necessity claim.
