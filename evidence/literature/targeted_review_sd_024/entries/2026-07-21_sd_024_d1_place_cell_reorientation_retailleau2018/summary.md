# Retailleau & Morris 2018 — Spatial rule learning and corresponding CA1 place cell reorientation depend on local dopamine release

**Claim tested:** SD-024 (DA-modulated RBF center density)
**Direction:** supports · **Confidence:** 0.75
**DOI:** [10.1016/j.cub.2018.01.081](https://doi.org/10.1016/j.cub.2018.01.081) (retrieved via PubMed, PMID 29502949)

## What the paper did

Rats learned an extra-dimensional set-shift task: two orthogonal sets of spatial cues, one of which was rule-relevant. CA1 place cells were recorded throughout training. Once the animals had learned to rely on one cue set, the rule was shifted — and at that moment the authors locally infused SCH23390, a D1-receptor antagonist, into hippocampus.

Animals that learned the new rule showed place-cell reorientation to the now-relevant spatial dimension. Under D1 blockade, that reorientation did not happen, and the animals did not learn: they perseverated on the old reference frame.

## Why this matters for SD-024

SD-024's architecture note cites this paper as its biological grounding, and it does carry that weight. It establishes, causally and locally, that dopamine is the channel through which reward-relevant information reaches the hippocampal map. Block it inside hippocampus specifically — not systemically — and the map stops reorganising around what currently matters.

That also supplies the motivation for the MECH-094 gate. What D1 signalling is delivering here is information about *actual* reward-relevant experience. A replayed or simulated event carries no such warrant, so allowing it to drive the same reorganisation would be importing a signal the biology does not have. The gate is not a safety bolt-on; it follows from what the dopaminergic signal is for.

## The caveat that matters most

Reorientation is not expansion. What this paper measured is a *reference-frame change* — an existing map re-anchoring to a different cue set. SD-024 asserts *local density increase* at reward locations. These are dissociable in both directions: a map can reorient wholesale with no local over-representation anywhere, and a map can develop local over-representation without any reference-frame change. Reading this paper as evidence for density expansion specifically would over-read it. It evidences DA-gated reward-driven map plasticity — a necessary premise for SD-024, not a sufficient one.

There is a second wrinkle worth flagging, because it may indicate a genuine error in the claim's own failure-mode taxonomy. SD-024 lists perseveration as the failure mode arising when **DA is locked high** — all locations expanded, no reorientation possible. Retailleau & Morris found perseveration from **D1 blockade** — DA absent. Both stories are coherent (saturation destroys contrast; absence destroys the update signal), but they are not the same story, and the claim currently asserts only one of them. Worth a governance look at whether the taxonomy should carry both.

Third: intra-hippocampal pharmacological infusion is a tonic manipulation. It speaks to D1 receptor tone across the learning episode, not to the phasic, event-locked pulse that SD-024 actually models. And because learning failure and remapping failure co-occurred in every impaired animal, the design cannot separate whether the map change drives the behaviour or trails it.

## Confidence reasoning

Solid electrophysiology with a genuinely causal, anatomically local manipulation — source quality 0.8. Transfer risk is the usual rodent-to-artificial-agent discount. Mapping fidelity at 0.65 is the binding constraint, and it is what holds this below the Krishnan entry despite comparable methodological quality. I have kept it at 0.75 rather than lower deliberately: the claim's own documentation leans on this paper, so the governance record should state clearly what it does and does not license.
