# Structure learning inside active inference (Smith, Schwartenbeck, Parr & Friston 2020) — Q-079

**Source:** Ryan Smith, Philipp Schwartenbeck, Thomas Parr & Karl J. Friston, "An active inference approach to modeling structure learning: concept learning as an example case," Frontiers in Computational Neuroscience 14:41 (2020), DOI 10.3389/fncom.2020.00041.
**Direction:** weakens (the distinct-novel-object reading of Q-079).

## What the paper does

The paper builds concept learning as structure learning *within* active inference. Two processes do the work. **Model expansion** engages unused "slots" in the state space when an agent meets feature patterns its current concepts cannot explain — adding novel hidden causes (birth / split). **Bayesian model reduction** then operates on the learned concentration parameters, analytically identifying redundant states and resetting them to flat priors — merging and pruning (death / merge). Run together, the agent grows and prunes its own latent structure online, and even acquires a granularity ordering (basic-level categories first, then subordinate differentiation).

## Why it bears on Q-079

This is the capacity-**(c)** entry: latent-node birth / death / merge / split. The DLIF research map lists "unknown latent structure" and "graph transformation" as capacities that no single nearby formalism cleanly provides, and the minimal toy's "offline merge/split/reweight after outcome" step is exactly this. Smith et al. show the capacity is already native to active inference — and, with de Vries & Friston (action + factor-graph substrate) and the RGM paper (scale), it sits in the *same* framework as (a), (b) and (d). That is the heart of the ANSWERED-NEGATIVE finding: the four capacities do not need a new object to be combined; hierarchical active inference with structure learning already combines them.

## The decisive caveat — residue is the opposite of pruning

There is a sharp, useful negative here. Bayesian model reduction works by **erasing** redundant structure to gain parsimony and free capacity. REE's residue / non-erasure is the *opposite* commitment: an unresolved moral/epistemic trace that must persist precisely when parsimony would discard it. So this paper does double duty — it collapses capacity (c) into existing machinery, and it shows that the one capacity active inference does **not** contain is residue. That is the only candidate-distinct ingredient of DLIF, and the Q-079 falsifier is explicit that it counts toward ANSWERED-POSITIVE only if shown *separable* from salience + uncertainty (HA2 = ARC-013's open V3-EXQ-587) — which is an REE experiment, not something this literature can settle.

## Limits and caveats

Expansion here uses pre-allocated spare slots, not unbounded growth; truly open-ended latent cardinality is the Bayesian-nonparametric case (sticky HDP-HMM, Fox et al 2011, the companion entry). Transfer risk is moderate: REE's hippocampal candidacy/merge mechanism is not this model, so this is an existence proof that (c) lives in active inference, not a claim of identical implementation.

## Confidence reasoning

0.73. High source quality and the exact birth/merge/death vocabulary give strong mapping fidelity for the coverage claim. Held below 0.8 by the spare-slot (vs unbounded) expansion and the moderate mechanism-transfer risk.
