# The opposing hypothesis, recorded as such (Silver, Singh, Precup & Sutton, 2021) — EXT-003

**Source:** Silver D, Singh S, Precup D, Sutton RS. *Reward is enough*. Artificial Intelligence 299:103535 (2021). DOI 10.1016/j.artint.2021.103535.

## Why this entry is here

EXT-003 asserts that scalar reward conflates incommensurable error signals, and that this conflation is what permits reward hacking. That premise has a live, authoritative opponent, published in a leading journal by four principals of the reinforcement learning field. A pull that assembled only the supporting side would misrepresent the state of the field, so this is recorded as a `weakens` entry — deliberately, and with the reasoning for its confidence spelled out rather than left implicit.

## What the paper argues

The authors hypothesise that intelligence and its associated abilities "can be understood as subserving the maximisation of reward," and that reward is enough to drive behaviour exhibiting the abilities studied in natural and artificial intelligence — knowledge, learning, perception, social intelligence, language, generalisation, imitation. They advance this, in their own words, "in contrast to the view that specialised problem formulations are needed for each ability, based on other signals or objectives." They conclude that agents learning by trial and error to maximise reward could exhibit most if not all of these abilities, and so that powerful RL agents could constitute a solution to AGI.

The argument proceeds ability by ability, considering for each how reward maximisation could give rise to it. There are no experiments and no theorems; the paper is explicitly a hypothesis.

## What it does to EXT-003

The opposition here is structural, not incidental, and it is worth noticing how precisely the contrast case lands. "Specialised problem formulations for each ability, based on other signals or objectives" is a fair description of ARC-021. REE's three cortico-striatal-like loops are exactly that: one per class of ability, each defined by its own error signal. So REE is a named target of this argument rather than a case its authors did not consider.

If the reward-is-enough hypothesis holds, three consequences follow for the REE claim graph, and they are the falsifier this entry registers. ARC-021's channel separation becomes optimisation overhead rather than a requirement for correct credit assignment. MECH-069's incommensurability becomes a claim about convenience rather than about information — the signals could be collapsed, and the objection would be efficiency, not correctness. And observed reward hacking becomes a reward-*design* problem to be engineered away, which would reclassify EXT-003 itself from a failure mode of scalarisation to an implementation defect of particular reward functions.

## The two limits on how much force this carries

First, and decisively for the confidence: this is argument, not evidence. It advances a conjecture and defends its plausibility. It measures nothing and proves nothing. Its weakening force is the force of a credible unrefuted conjecture held by people with standing — which is real, and is why it belongs in the record, but is bounded in a way a measurement would not be.

Second, and more specific: the paper's thesis is the sufficiency of *reward maximisation*. The **scalar**-valuedness of that reward is an auxiliary assumption it never separately defends — it is assumed and carried along. EXT-003 attacks only the auxiliary assumption. So the two positions are not exact contradictories. One could accept the reward-is-enough framing wholesale and still hold, with Vamplew et al., that the reward must be vector-valued; on that reading this paper does not weaken EXT-003 at all. I have scored it as weakening on the reading Silver et al. plainly intend and that Vamplew et al. attribute to them, but that is an interpretation, and a reader is entitled to the narrower one.

This is also why the two papers in this pull are best read as a pair rather than as two independent votes. Vamplew et al. is a direct reply to this paper, and the gap it exploits is exactly the undefended auxiliary assumption named above.

## Confidence, and a note on the number

0.50. The calibration guide puts `<0.5` at "weak or ambiguous mapping," and I want to be explicit that **this is not the situation here** — the mapping is unusually clean for a weakening entry (0.78), because the paper's own stated contrast case describes REE's architecture. What is weak is the *evidentiary form*: a hypothesis paper with no experiment and no proof. Source quality 0.85 certifies venue and authorship, not evidential weight. Transfer risk 0.35 covers the interpretive step from an argument about intelligence in general to REE's specific three-channel commitment.

The aggregate is deliberately set below what the components' tenor would suggest, and the reason is recorded here and in `confidence_components.notes` so that a later reader does not "correct" it upward on the mistaken assumption that it was scored down for mapping ambiguity.
