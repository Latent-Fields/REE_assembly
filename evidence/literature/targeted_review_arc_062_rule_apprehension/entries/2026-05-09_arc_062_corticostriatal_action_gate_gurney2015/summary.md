# Gurney, Humphries & Redgrave 2015 — Cortico-striatal plasticity as the action-reinforcement interface

According to PubMed: Gurney, Humphries & Redgrave 2015, *PLoS Biology* 13(1):e1002034. [DOI 10.1371/journal.pbio.1002034](https://doi.org/10.1371/journal.pbio.1002034) (PMID 25562526, PMC4285402).

## What the paper builds

A computational framework that bridges three levels: in vitro cortico-striatal synaptic plasticity (the spike-timing- and dopamine-dependent rules), single-cell striatal output dynamics (D1 vs D2 pathways), and behavioural reinforcement-learning theory (acquisition, extinction, renewal, reacquisition). The framework treats the cortico-striatal synapse as the action-reinforcement interface — the place where phasic dopamine acting as reinforcement prediction error gates plasticity, changing the future likelihood of selecting the action coded by the striatal neurons. The two types of striatal output neuron co-operate to promote action selection in learning and compete to promote action suppression in extinction. Validated by replicating in vitro plasticity data and behavioural-level extinction / renewal / reacquisition phenomena.

## Why this matters for R3 (gating site)

R3 option (i) — score-aggregation-level gating at the BG-side — needs a biological anchor that goes beyond "BG-as-action-selector" platitudes. Gurney, Humphries & Redgrave provide it. The cortico-striatal synapse IS the action-selection / action-suppression decision point, with dopamine-gated plasticity changing the strength of "select this action" versus "suppress this action" signals. In REE terms, that maps to E3's score-aggregation step where harm and goal signals combine into a per-candidate score. ARC-062's weak-reading discriminator could route to this site by gating which cortical inputs contribute to the cortico-striatal synaptic strength, or equivalently by modulating the D1/D2 balance for the rule-active state.

## How this competes with R3 option (iii) — Miller & Cohen

Miller & Cohen 2001 anchor R3 option (iii) at PFC top-down bias projection. Gurney/Humphries/Redgrave anchor R3 option (i) at the cortico-striatal action-reinforcement interface. These are not contradictory — biology has both — but they are different *primary loci* for the rule-context modulation. The cluster's open question R3 is therefore better read as "*which* of these does ARC-062's discriminator output target?" rather than "which one exists biologically?" Both exist; the architectural commitment is a routing choice.

For Phase 1 of `arc_062_rule_apprehension_plan.md`, the leading candidate is option (iii) for engineering reasons: SD-033a substrate is already in place, and the score_bias entry point is clean. Phase 4 / GAP-E (multi-strategy scaling) is the natural place to test option (i) by routing the discriminator output through a different channel.

## Mapping caveat

Gurney/Humphries/Redgrave's framework targets *reinforcement-driven* action selection. The bridge to *rule-context-conditioned* policy gating requires a separate commitment about what the rule signal looks like at the BG synapse. Three options the paper does not arbitrate among:
- (a) The rule signal modulates the dopamine prediction error itself.
- (b) The rule signal modulates cortical input to the synapse (which then drives D1/D2 differentially).
- (c) The rule signal modulates D1/D2 balance directly.

ARC-062 does not need to commit to one of (a)/(b)/(c) at Phase 1, but Phase 4 / GAP-E experiments routing the discriminator to BG-side gating WILL need to commit. Flag for that future session.

## Confidence reasoning

Source quality high — PLoS Biology, validated against multiple behavioural phenomena and in vitro plasticity data, bridges-levels integration. Mapping fidelity reduced (0.70) because the paper is one structural step removed from the rule-context-gating question. Transfer risk moderate (0.30): REE's E3 score-aggregation has direct analogues to D1/D2 cooperative-then-competitive dynamics, but the dopamine-PE gating mechanism does not have a clean V3 substrate (REE does not have a dopamine-PE channel separate from harm/goal scoring). Confidence 0.78 reflects strong R3-(i) anchor minus the rule-vs-reinforcement gap.

## Failure signatures for the cluster

Two practical diagnostics the paper licenses:

1. **Sustained policy stability under SD-054**: if ARC-062 weak reading at option (iii) PASSes initial training but the discriminator output cannot be sustained without continuous teaching signal, the framework predicts the missing element is dopamine-gated plasticity at the action-reinforcement interface. The discriminator + policy heads converge in joint training, but without the cortico-striatal-analog plasticity rule, the partition does not stabilise. Diagnostic: monitor policy-head divergence vs episode count.

2. **D1/D2-imbalance signature in maladaptive partitions**: if two-head ARC-062 produces stable but maladaptive policy partitions on SD-054 (e.g. always reef, never forage despite resource cues), the framework predicts an action-promotion vs action-suppression imbalance — the gated-policy outputs over-weight the "select this action" signal in one head and under-weight the "suppress this action" signal in the other. Diagnostic: ratio of positive-vs-negative score contributions per head.
