# Bonsai trees in your head: how the Pavlovian system sculpts goal-directed choices by pruning decision trees

**Huys, Eshel, O'Nions, Sheridan, Dayan & Roiser (2012). PLoS Computational Biology, 8(3), e1002410.**
**DOI:** 10.1371/journal.pcbi.1002410 | **PMID:** 22412360

---

## What the paper did

Huys and colleagues studied how avoidance reflexes interact with deliberate planning in healthy humans. Subjects performed a sequential decision task requiring them to evaluate multi-step choice sequences with monetary outcomes. The key feature was that high-punishment outcomes were embedded within sequences that -- if evaluated fully -- would yield better net results than sequences without punishment. The question was whether subjects would continue evaluating sequences after encountering losses, or curtail evaluation prematurely.

They fitted computational models to capture the degree to which subjects 'pruned' their decision trees after encountering losses, and correlated this pruning tendency with sub-clinical mood measures (BDI-SF).

## Key findings

The results were clear: subjects systematically curtailed evaluation of sequences after encountering large losses, even when this pruning cost them better outcomes. The behavior was reflexive in the sense that it was independent of whether continuing would have been profitable -- the loss triggered inhibition regardless of downstream value. Computational modeling confirmed this was best characterized as Pavlovian behavioral inhibition: an automatic loss-triggered halting of search, mediated by Pavlovian aversion rather than deliberate cost-benefit analysis.

Crucially, subjects with higher sub-clinical depressive symptoms showed significantly stronger pruning. Those with more mild depressive features were more likely to abandon evaluation after losses, and more likely to miss better long-term outcomes as a result.

## Mapping to ARC-030

ARC-030 asserts that the three BG-like loops require symmetric Go (approach) and NoGo (avoidance) sub-channels, and that a pure-NoGo architecture produces behavioral flatness. Huys et al. provide behavioral evidence for the failure mode: when avoidance inhibition operates without adequate approach counterweight, it produces a systematically restricted search -- the agent's planning space contracts around harm-avoidance, and approach-relevant paths are never evaluated.

The architectural translation is direct. REE's E3 module evaluates hippocampal trajectory proposals through both a harm channel (SD-010, nociceptive stream, NoGo analog) and -- if ARC-030 is implemented -- a goal channel (MECH-112, goal attractor, Go analog). Without the goal channel, E3 acts as a pure harm evaluator: any trajectory passing through a harm-proximate state triggers inhibition, and the planning horizon contracts to the immediate neighborhood of harm-free states. This is precisely the Pavlovian pruning Huys et al. document. The quiescent policy that ARC-030 predicts as the degenerate attractor of pure-avoidance training is the decision-tree analog of the pruned tree with no evaluated branches remaining.

The depression correlation provides an epidemiological anchor for Q-021. The claim that pure-avoidance architecture produces behavioral flatness is not merely a theoretical prediction; it has a clinical instantiation in subclinical depression, where heightened Pavlovian inhibition (over-weighting of loss-avoidance relative to approach) measurably restricts motivated behavior and planning horizon. The serotonergic mechanism the authors invoke is a somewhat different biological story from the dopaminergic Go/NoGo balance of ARC-030, but functionally the outcome -- suppression of approach evaluation by avoidance dominance -- is equivalent.

## Limitations and caveats

This paper does not directly measure BG Go/NoGo pathway activity. The 'Pavlovian pruning' mechanism is theorized to involve serotonin-mediated behavioral inhibition rather than purely dopaminergic D1/D2 competition, so there is a biological level-shift between this paper's mechanism and ARC-030's. The pruning behavior is not identical to behavioral flatness: a subject who prunes decision trees after losses is not quiescent -- they are actively choosing the less-evaluated option. The full flatness predicted by ARC-030 (minimal action rate, near-zero goal-state visits) requires a stronger condition: not merely that avoidance prunes search, but that avoidance-only training converges to quiescence as the globally optimal policy. Huys et al. document the directional trend and the clinical correlation, but not the full degenerate attractor.

The cross-sectional design and sub-clinical population limit causal inference. The finding that depressive symptoms correlate with stronger avoidance-pruning does not demonstrate that the architecture causes the flatness; it may be that both co-vary with a common underlying vulnerability.

## Confidence reasoning

Confidence 0.71. Source quality is good -- peer-reviewed, well-cited, combines rigorous computational modeling with clean behavioral paradigm and clinical correlate. Mapping fidelity is moderate: the Pavlovian pruning phenomenon is a genuine behavioral demonstration of avoidance dominance restricting approach planning, which is directly relevant to ARC-030's prediction about pure-NoGo architectures, but the mapping requires a theoretical bridging step from Pavlovian inhibition to BG pathway competition. Transfer risk is moderate: the level-shift from serotonergic Pavlovian inhibition to dopaminergic D1/D2 balance, and from binary tree search to REE's geometric trajectory planning, both introduce interpretive uncertainty.
