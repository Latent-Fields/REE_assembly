# Capkova, Ainsworth, Mansouri & Buckley 2025 — Frontal lobe lesion dissociation of rule-value-learning sub-functions

According to PubMed: Capkova, Ainsworth, Mansouri & Buckley 2025, *eNeuro* 12(5). [DOI 10.1523/ENEURO.0117-25.2025](https://doi.org/10.1523/ENEURO.0117-25.2025) (PMID 40393730, PMC12184873).

## What the paper does

Macaques with circumscribed lesions to one of five frontal regions — principal sulcus (PS), anterior cingulate cortex (ACC), orbitofrontal cortex (OFC), superior dorsolateral PFC (sdlPFC), and frontopolar cortex (FPC) — performed a WCST analog (Wisconsin Card Sorting Task). Behavioural data fit with a three-parameter feedback-dependent reinforcement learning model. Model-parameter recovery dissociates which sub-function each lesion impairs.

## What the dissociation shows

Three distinct findings, each on a different region:

1. **OFC lesions** decreased the rate at which rule values were updated from both positive and negative feedback. The OFC's role is *value-updating bandwidth*: how fast outcomes change the agent's estimate of which rule is correct.

2. **PS lesions** left rule-value updating intact but made monkeys *less likely to repeat correct choices when rule values were well established*. This is a working-memory-maintenance deficit: the PS holds the active rule across the inter-trial interval, and without it the agent forgets what it learnt even though it learnt it correctly.

3. **ACC lesions** produced a specific deficit in *learning from negative feedback* and impaired the ability to repeat choices following highly surprising reward. The authors interpret this as ACC's role in flexibly *switching between trial-and-error and working-memory modes* in response to increased error likelihood.

So three orthogonal sub-functions (value-updating speed, rule-state maintenance, mode-switching driven by negative-feedback surprise) map to three distinct frontal regions.

## What this means for ARC-062 / MECH-309 / ARC-063

This is the strongest single-paper anchor for the *distributed multi-region* commitment that ARC-063 strong reading bakes in. The WCST analog dissociation says: rule-context modulation is not implemented at one site, even within the frontal lobes. Three regions, three sub-functions, all needed.

Mapping to REE substrate:

- **PS (rule-state maintenance) ↔ SD-033a `lateral_pfc_analog.rule_state`**. The buffer that holds the active rule across ticks within an episode is exactly the PS-lesion-impaired function. ARC-062 weak reading operates here.
- **OFC (rule-value updating) ↔ SD-033b `ofc_analog`** (already implemented 2026-04-26, oracle path 2026-05-04). The rule-value-updating-rate machinery is not yet wired to feed the discriminator's training signal.
- **ACC (mode-switching from negative feedback) ↔ SD-032b dACC + SD-034 closure operator**. The SD-034 closure operator handles rule completion; the dACC dual-stream signal handles negative-feedback-driven mode-switching. Both are landed; the rule-context coupling is not yet wired.

The implication for ARC-062 weak reading is sober: the gated-policy + discriminator architecture is operating on the *rule-maintenance leg* (PS analog) only. PASS on SD-054 is plausible, but the performance ceiling depends on whether the OFC and ACC analog functions become rate-limiting. ARC-062 is necessary but possibly insufficient; the cluster's Phase 4 / GAP-E successor experiments are the place where the multi-region requirement either confirms or excludes itself.

## Why this is mixed-favourable rather than weakening for ARC-062

The dissociation does *not* say ARC-062 weak reading is wrong. It says ARC-062 alone is *less than complete* — the cluster's own framing (ARC-062 weak / ARC-063 strong) anticipates this. The Phase 2 falsifier on SD-054 tests whether ARC-062 alone breaks monomodal collapse; the WCST evidence predicts a partial-success regime where ARC-062 succeeds but generalisation to richer task structure surfaces additional sub-function gaps.

## Mapping caveat

The WCST analog tests abstract dimensional rules (shape vs colour vs other features). The reef-vs-forage discriminative cut on SD-054 is a *context* rule rather than a dimensional rule. The mapping from PS-rule-maintenance to SD-033a's `rule_state` is direct because both are working-memory-style buffer maintenance. The OFC-rule-value-updating mapping is the weakest: REE has SD-033b OFCAnalog substrate but does not yet have an explicit rule-value-updating-rate parameter (the closest analog is the oracle path's `query_outcome` round-trip). The negative-feedback-mode-switching mapping is moderate — dACC's MECH-268 PE saturation handles outcome-history but the trial-by-trial rule-update gating is not yet wired.

## Confidence reasoning

Source quality 0.88 — recent (2025) peer-reviewed lesion study with quantitative model-based dissociation, methodologically clean (multiple lesion groups, RL parameter recovery, established WCST analog). Mapping fidelity 0.80 — three regions map to three REE substrates, two of which are already in implementation. Transfer risk 0.25 — dimensional vs context rule difference, plus the rule-value-updating-rate machinery is the weakest substrate cross-mapping. Confidence 0.84 reflects: strongest single anchor for distributed multi-region requirement, with the dimensional-vs-context-rule transfer caveat captured in `failure_signatures`.

## Failure signatures for the cluster

1. **Generalisation ceiling under task-perturbation**: if ARC-062 weak reading PASSes the SD-054 falsifier but generalisation to substrate enrichment (SD-049 multi-resource heterogeneity, SD-047 multi-source dynamics) shows a learning-rate ceiling, Capkova et al's data predicts the missing functionality is OFC-rule-value-updating-rate. Diagnostic: rule-value-update rate as a function of feedback consistency.

2. **Negative-feedback asymmetry**: if ARC-062 PASSes Phase 2 falsifier but fails on a learning-rate-asymmetry probe (positive-feedback rule reinforcement vs negative-feedback rule revision), the data predicts the missing functionality maps to ACC analog. V3 substrate has dACC (SD-032b) but the rule-context coupling is not yet wired. The cluster's GAP-E or a sibling Phase 4 experiment becomes load-bearing.
