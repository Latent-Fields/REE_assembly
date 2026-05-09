# Mitchell et al. 2016 — A putative multiple-demand system in the macaque brain

According to PubMed: Mitchell, Bell, Buckley, Mitchell, Sallet & Duncan 2016, *J Neurosci* 36(33):8574–85. [DOI 10.1523/JNEUROSCI.0810-16.2016](https://doi.org/10.1523/JNEUROSCI.0810-16.2016) (PMID 27535906, PMC4987434).

## What the paper does

Resting-state fMRI in 35 rhesus macaques under anaesthesia. Putative MD regions, initially mapped from frontoparietal coordinates defined in humans, were found to be functionally connected. Iterative refinement using cross-validated connectivity identified seven clusters across **frontoparietal AND insular cortex** plus one unexpected cluster in the lateral fissure — closely matching the human MD counterpart. The paper provides macaque MD region maps that subsequent task-fMRI and electrophysiology can use to study rule-context modulation in the substrate Duncan's adaptive-coding framework predicts is load-bearing.

## Why this matters for R1 (input streams)

The insular cluster is the load-bearing finding for R1. Insular cortex is the canonical interoceptive integration site (Craig 2009; Critchley 2003). Its presence in the macaque MD network — at the same connectivity strength as the frontoparietal members — establishes that the biological substrate for rule-context modulation includes interoceptive input *as a first-class member*, not as an external afterthought modulating a cognitive frontoparietal core.

For ARC-062, this means: the discriminator should read `z_world + z_self + z_harm_a`, not `z_world` alone. Single-stream is the wrong architectural commitment; the biology is multi-stream by integration site. This complements the Miller & Cohen 2001 abstract endorsement of multi-stream integration — that paper licenses the commitment in principle, this paper grounds it anatomically.

## Why this matters for R3 (gating site)

The MD network is *distributed* across multiple frontoparietal sites: lateral PFC, dorsomedial frontal, parietal, insular. Single-site dominance is the wrong framing. R3 is better read as "which site does ARC-062's discriminator output target *first*?" rather than "which site is biologically primary?" All sites are biologically primary; the architectural commitment is a routing choice.

For Phase 1 of `arc_062_rule_apprehension_plan.md`, this favours the score_bias level (option iii) for engineering reasons (SD-033a substrate is in place) while explicitly recognising that the V3 architectural-end-state will need parallel routing to BG-side and trajectory-proposal-side substrates as part of the GAP-E multi-strategy work or under ARC-063 strong reading.

## Mapping caveat

The data is resting-state connectivity in *anaesthetised* macaques, not task-driven rule-context modulation. The "MD network is the rule-context substrate" inference is by anatomical analogy to the human MD literature, where task-driven adaptive coding (Erez & Duncan 2015 — sibling entry) has been demonstrated. The paper provides the substrate map; it does not directly demonstrate rule-context modulation across all identified sites under task. That extrapolation is biologically warranted but technically a transfer claim.

## Confidence reasoning

Source quality 0.78 — solid methodology, peer-reviewed, n=35, but the data is resting-state under anaesthesia rather than task-driven. Mapping fidelity 0.70 — the substrate-as-rule-network inference is by anatomical analogy to the human MD literature rather than direct measurement. Transfer risk 0.28 — macaque-to-REE mapping is direct for the regions involved (lateral PFC ↔ SD-033a; dACC ↔ SD-032b; AIC ↔ SD-032c; PCC ↔ SD-032d; pACC ↔ SD-032e are all already substrate). Confidence 0.72 reflects: strong R1 anatomical anchor (insular = interoceptive integration site) + R3 distributed-substrate commitment, minus the resting-state-to-task transfer gap.

## Failure signature for the cluster

If ARC-062 weak reading commits to a single-stream discriminator (`z_world` only) for engineering convenience and FAILs the SD-054 monomodal-collapse falsifier, Mitchell et al's insular finding predicts the missing input stream is interoceptive. Diagnostic: include an input-ablation arm in the Phase 2 falsifier comparing ARM_1a (`z_world` only) vs ARM_1b (`z_world + z_self`) vs ARM_1c (`z_world + z_self + z_harm_a`). If ARM_1c clears the falsifier and ARM_1a/b do not, the multi-stream commitment is empirically confirmed for the SD-054 substrate; if ARM_1a clears it, the multi-stream commitment is engineering-overhead-without-benefit at this scale and the V3 default can stay single-stream.
