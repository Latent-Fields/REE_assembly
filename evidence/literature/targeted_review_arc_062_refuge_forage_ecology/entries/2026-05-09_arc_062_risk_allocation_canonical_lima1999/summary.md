# Lima & Bednekoff 1999 — The predation risk allocation hypothesis

According to PubMed: Lima & Bednekoff 1999, *American Naturalist* 153(6):649–659. [DOI 10.1086/303202](https://doi.org/10.1086/303202) (PMID 29585647).

## What the paper argues

A theoretical paper proposing that animals exposed to *temporally variable* predation risk allocate their antipredator effort across risk situations rather than maintaining a constant antipredator level. Three load-bearing predictions: (1) the greatest antipredator behaviour should appear in *brief, infrequent* high-risk situations; (2) antipredator effort in low-risk situations should drop as the proportion of time spent at high risk increases — under chronic high risk, animals have to feed despite the risk; (3) the standard experimental protocol of low-risk-baseline-with-pulse-of-high-risk *overestimates* the antipredator intensity expected in field conditions or under chronic exposure. The hypothesis follows from a state-dependent optimisation: prey have to feed sometime, so the relevant variable is the *contrast* between low-risk and high-risk windows, not the absolute risk level.

## Why this matters for R4 (Phase 2 calibration target)

R4 asks: under what hazard density and resource availability do real vertebrates allocate behaviour between safe-zone use and forage activity? The risk-allocation hypothesis says: the allocation is a *function* of the temporal risk pattern, not a fixed ratio. The arbitrary EXQ-522 hand-coded heuristic at `reef_visit_fraction in [0.3, 0.7]` is biologically defensible only if SD-054's hazard regime matches the pattern where 0.3-0.7 was the empirical mode.

Three architectural implications for ARC-062 and the Phase 2 falsifier:

1. **The Phase 2 falsifier should test ARC-062's allocation across a hazard-density gradient**, not at a single point. The acceptance threshold should be a *function shape* (allocation tracks density) rather than a single ratio. ARM_1 of the falsifier should run at multiple hazard-density settings; PASS = monotone relationship between hazard density and refuge-use; FAIL = invariant allocation across regimes.

2. **Under chronic high-risk regimes, refuge-use should REDUCE** — not increase — because the agent has to forage sometime to survive. This is the counterintuitive prediction that distinguishes a biologically honest gated-policy from a naive "always-flee-when-hazard-present" architecture. ARC-062 weak reading at the score_bias level (option iii) needs to compute *relative* risk across temporal windows; if it computes only *absolute* risk it will fail this prediction.

3. **The SD-054 substrate uses persistent reef and persistent food-attracted hazards** (not pulses). Lima-Bednekoff says pulsed-risk paradigms overestimate antipredator intensity — so calibration data from chronic-risk empirical work (Sundell 2004 voles, Eccard 2020 voles, Balaban-Feld 2019 fish — all sibling entries in this pull) is the right reference, not pulsed-risk work.

## Why this matters for MECH-309

MECH-309's logical-necessity claim says strict Bayesian / parametric-policy learners cannot invent rules. The risk-allocation hypothesis is itself a *rule* — "allocate more antipredator effort when relative risk is briefly high, less when it is chronically high". Real animals follow this rule (with empirical caveats — see Sundell 2004 sibling entry). For an agent to follow it, the rule has to *exist as a candidate* in the agent's policy repertoire. ARC-062's discriminator architecture is the structural mechanism that lets the trainer weight this rule once it has been proposed; MECH-309 says without ARC-062 (or ARC-063 strong reading) the trainer would converge on a single strategy that does not respect the relative-risk variable. Direct test on SD-054: if ARM_0 single-head E3 settles at one fixed allocation regardless of hazard density, that is the MECH-309 monomodal-collapse signature; if ARM_1 ARC-062 tracks Lima-Bednekoff's predictions across a density gradient, the rule-apprehension layer is doing its job.

## Mapping caveat

This is a theoretical paper, not direct quantitative calibration. It predicts the *shape* of the allocation function (how it changes with risk pattern) but does not provide a numerical "X% refuge / Y% forage" ratio for any specific hazard regime. Numerical calibration requires the empirical sibling entries in this directory (Sundell 2004 voles, Balaban-Feld 2019 fish, Eccard 2020 voles, Crowell 2016 rabbits). The theory is species-general; specific constants for fish-in-coral-reef ecology may differ from the rodent-and-vole literature where most direct empirical tests run.

## Confidence reasoning

Source quality 0.95 — foundational paper in *American Naturalist*, extensively cited, decades of empirical testing both supporting and challenging it (see sibling entry Beauchamp & Ruxton 2010 critique; Sundell 2004 partial-replication failure). Mapping fidelity 0.85 — the theoretical structure transfers cleanly to ARC-062's gated-policy + risk-context discriminator architecture. Transfer risk 0.20 — the theory is species-general and the SD-054 reef-vs-forage partition is exactly the kind of allocation problem it addresses. Confidence 0.88 reflects: foundational theoretical anchor with the empirical-calibration-elsewhere caveat captured in `failure_signatures` and the per-sibling-entry quantitative data.

## Failure signatures for the cluster

1. **Density-invariance**: if ARC-062 weak reading produces antipredator allocation that is invariant across SD-054 hazard density (reef_visit_fraction the same whether 1 hazard or 10 are active), Lima-Bednekoff predicts this is a failure of context-discrimination — the agent is treating all hazard regimes as equivalent. The discriminator is not gating on the relative-risk variable.

2. **Chronic-risk over-protection**: under chronic-high-risk SD-054 regimes (many persistent food-attracted hazards), if ARC-062 maintains high refuge-use and the agent starves, the architectural commitment is suppressing risk-allocation logic in a biologically inappropriate way. Real animals reduce antipredator effort under chronic high risk because they must feed. ARM_1 should show this reduction; if it does not, the discriminator output is not gated on the *temporal-variability* signal that Lima-Bednekoff identifies as the load-bearing variable.
