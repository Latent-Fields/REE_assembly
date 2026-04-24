# Buckley et al 2009 — Dissociable components of rule-guided behavior depend on distinct medial and prefrontal regions

**Source:** Science 325(5936):52-58, 2009. DOI: [10.1126/science.1172377](https://doi.org/10.1126/science.1172377)

## What the paper did

Buckley and colleagues made circumscribed bilateral lesions to five distinct prefrontal regions in separate groups of macaques — orbitofrontal cortex (OFC), principal sulcus (PS, lateral PFC), superior dorsolateral PFC, ventrolateral PFC, and anterior cingulate cortex sulcus — and then tested each group on a Wisconsin Card Sorting Test analog. The WCST analog was designed to tax three separable cognitive components: maintaining abstract rules in working memory, updating rule-value representations based on reward feedback, and using recent choice outcomes to guide current decisions. The task therefore provided a natural dissection of prefrontal function across lesion groups.

## Key findings

The dissociation was striking and directly relevant to MECH-262. Only the principal sulcus (PS) lesion specifically impaired the **maintenance of abstract rules in working memory** — the PS group showed elevated perseverative errors after a rule shift, specifically when the new rule needed to be held across intervening choices. OFC lesions did not touch rule maintenance but instead impaired rapid reward-based updating of rule value. ACC sulcus lesions impaired the use of recent choice-outcome values during rule-based decisions. The superior dlPFC and vlPFC lesions produced no significant specific deficit in any of the three components.

The triple dissociation means that the PS is not just "involved" in rule maintenance but is selectively and causally necessary for it. Other prefrontal regions cannot substitute, at least acutely. The deficit was tied to abstract rule maintenance specifically: PS-lesioned animals could still respond to stimulus-reward associations when no rule-WM was required.

## REE translation

MECH-262 assigns rule-selective persistence to the lateral-PFC-analog (SD-033a), which is the REE implementation of the principal sulcus. Buckley et al provide the clearest causal evidence in the primate literature that this assignment is correct: when the PS is removed, abstract rule maintenance fails while other prefrontal functions (reward updating, outcome tracking) are spared. This double-dissociates the lateral-PFC-analog from the OFC-analog (reward-value substrate) and from the dACC-analog (effort/outcome-reference substrate, MECH-260).

The practical import for MECH-262 is that the claim's falsification condition — "if the lateral-PFC-analog substrate is ablated, rule-guided behavior should fail specifically for rule-maintenance demands" — has a direct biological precedent. In REE, disabling the SD-033a write channel or ablating the rule-representation layer should selectively impair tasks that require holding a rule across intervening events (distractors, replay episodes), without necessarily impairing reward-based updating (OFC-analog) or recent-outcome use (ACC-analog).

## Limitations and caveats

The lesion approach conflates encoding, maintenance, and retrieval of rules: it is not possible to say from this data whether the PS is specifically required for the persistence step versus the initial formation of the abstract rule representation. The small group sizes (n ≈ 5 per lesion group) limit statistical power for the dissociation claim. Furthermore, the WCST analog is a between-trial task where the "working memory" demands span seconds to tens of seconds — MECH-262 additionally requires persistence across internal_replay events and micro-quiescence cycles that may run on different timescales. The biological referent is nevertheless clear.

## Confidence

0.80. High source quality and the localization-plus-dissociation evidence is the strongest causal support available for the lateral-PFC-specific claim in MECH-262. The confidence cap reflects the coarseness of the behavioral measure relative to MECH-262's specific three-signature mechanistic framework, and the uncertainty about whether the lesion deficit is specifically about persistence versus encoding.
