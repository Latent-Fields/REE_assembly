# Friston 2010 — The free-energy principle: a unified brain theory?

[DOI](https://doi.org/10.1038/nrn2787) · PMID 20068583 · *Nat Rev Neurosci* 11(2):127–38

## What the paper argues

Friston synthesises a decade of his own theoretical work into the free-energy principle (FEP): biological systems minimise the variational free energy (or equivalently, surprise) of their sensory states. The principle is offered as a unified framework spanning perception (variational Bayes inference), action (active inference), and learning (parameter updating to reduce expected free energy). Exploration is recast as the minimisation of *expected* free energy, which decomposes into extrinsic-value (reward-seeking, the standard RL objective) and epistemic-value (uncertainty-reducing, the curiosity term).

## Why this matters for ARC-065

This is the load-bearing theoretical anchor for the structured-exploration arm of R1. The argument: behavioural diversity is not just noise, and not just goal-seeking — there is a principled reason agents should bias their actions toward states that reduce model uncertainty (epistemic value), and that bias has the same mathematical form as a curiosity bonus. MECH-314 (curiosity bonus on E3 score_bias) gets its theoretical justification here; the free-energy framing makes it a derivable consequence of the same optimisation principle that drives all the other REE substrates that already commit to precision-weighted prediction error (MECH-269b V_s rollout gating, SD-032b dACC PE-precision modulation).

The cluster registration consequence: ARC-065 is FEP-aligned in a way that makes MECH-314 not an extra mechanism bolted on but a direct consequence of the same optimisation principle. This is architecturally satisfying and matches the broader REE commitment to precision-weighted prediction error. The downside is that FEP-as-empirical-substrate is contested: Friston's claim is that all brain function reduces to free-energy minimisation; many neuroscientists treat this as too strong. ARC-065's exposure to FEP truth depends on which sub-MECHs are wired in FEP-explicit form (the Friston 2015 active-inference instantiation is the operational version that would be most exposed) versus pragmatic curiosity instantiations (Schmidhuber/Pathak intrinsic-motivation tradition that do not require FEP truth).

## Limitations and confidence

The FEP is a unified theory whose status as an empirical claim is contested. The 2010 paper is theoretical synthesis, not empirical demonstration. Confidence aggregate 0.72 — high venue, foundational status, but moderate mapping fidelity and elevated transfer risk because the empirical substrate-level commitments require additional instantiation papers (Friston 2015 active inference + epistemic value, paired entry in this pull). The existence of the FEP framing as theoretical anchor is not in doubt; whether REE should commit to FEP-explicit instantiation of MECH-314 vs pragmatic-curiosity instantiation is a downstream registration choice.

## Failure signature it would falsify

If FEP is fundamentally wrong about the substrate of exploration — if epistemic-value-as-free-energy is not a real biological computation — then any MECH-314 instantiation that depends on FEP-explicit precision arithmetic loses its theoretical grounding. Pragmatic curiosity instantiations (Schmidhuber/Pathak intrinsic-motivation tradition) survive independently of FEP truth.
