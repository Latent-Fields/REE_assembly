# Salamone & Correa 2003 -- Activational motivation and accumbens DA

**Citation:** Salamone JD, Correa M. Motivational views of reinforcement: implications for understanding the behavioral functions of nucleus accumbens dopamine. *Behav Brain Res*. 2003;137(1-2):3-25. PMID: 12445713. [DOI](https://doi.org/10.1016/s0166-4328(02)00282-6).

## What the paper does

Salamone and Correa write a canonical review establishing that nucleus accumbens dopamine mediates the ACTIVATIONAL aspect of motivation -- the willingness to expend effort and overcome work-related response costs -- separately from primary appetitive / hedonic processes. The empirical signature is robust: low to moderate doses of DA antagonists, and accumbens DA depletions, suppress instrumental responding for food (especially under high ratio requirements) while leaving primary motivation, appetite, and unconditioned reinforcement intact. In concurrent-choice tasks, DA-depleted animals do not become anhedonic; they reallocate AWAY from high-effort high-reward options TOWARD low-effort low-reward options. They still want food, they just prefer to pay less for it. The paper frames this in behavioural-economics terms as a sensitivity to elasticity of demand, and in motivational-theory terms as a separation of "wanting" into directional (appetite to consume) and activational (effort to obtain) components.

## Why this matters for ARC-068

The R4 verdict (effort-cost vs opportunity-cost separation) is the question this paper most directly answers. Salamone's effort cost is mechanically distinct from Niv's opportunity cost. Salamone's term scales with action-energy / response-rate requirements (the cost of expensive ACTION); Niv's term scales with elapsed time against the avg-reward-rate history (the cost of INACTION). They are DIFFERENT terms with DIFFERENT temporal kernels and DIFFERENT signs on different candidates: effort cost makes hard ACTION less attractive (penalises high-cost trajectories regardless of duration); opportunity cost makes INACTION less attractive (penalises long-duration trajectories regardless of action cost). The two are simultaneously load-bearing and architecturally separable. REE already has the effort-cost machinery -- MECH-258 (cingulate.precision_weighted_pain_PE) plus the SD-032b dacc_effort_cost bundle component (default 0.1, see SD-032b implementation_note). The R4 verdict that the synthesis must produce is: ARC-068 is NOT redundant with the existing effort-cost machinery and should not be absorbed into it.

Both terms ride on the same DA system biologically, which is why they're easy to confuse. Salamone's review explicitly engages this confusion: a naive read of the DA-depletion data could fold opportunity cost into effort cost (the Salamone result is then "DA depletion reduces willingness to pay any cost"), but the careful experimental dissociations in the paper -- particularly the high-vs-low ratio schedule comparison and the concurrent-choice reallocation pattern -- show the costs respond to different task variables. In REE's E3 score-aggregation chain, the two terms should appear as separate additive components even when their upstream DA modulators are coupled.

This paper also provides indirect support for the R1 verdict (ARC-068 vs SD-032b boundary). The DA-mediated activational scalar is most cleanly anchored to mesolimbic / accumbens DA (Salamone, Niv), not to dACC. SD-032b's dACC anchor (Kolling) is computing a current-environmental-value signal that is downstream of the DA substrate. The architectural separation between ARC-068 (DA-substrate-anchored, long-run kernel) and SD-032b (dACC-substrate-anchored, current-environmental kernel) survives even under the Shenhav reinterpretation of the dACC signal.

## Caveats

The 2003 review is an early synthesis. Salamone & Correa 2012 (Neuron, already cited in the parallel ARC-066 entry) is the canonical refinement of the effort-vigor framework; subsequent papers (Salamone et al. 2018 Nat Rev Neurosci) integrate it with broader effort-cost computational accounts. The load-bearing claim from the 2003 paper -- the activational-vs-primary-reinforcement dissociation -- is uncontested in the subsequent literature, but the specific computational shape of the effort-cost term has been refined.

A second caveat: the project briefing cites "Salamone et al. 2003" (multi-author). The PubMed match closest to that citation is Salamone & Correa 2003 (two authors). There is a related four-author paper (Salamone, Correa, Mingote, Weber 2003 J Pharmacol Exp Ther) but it is a different publication. This entry uses the Behav Brain Res paper because it is the canonical review and matches the briefing's intent.

A third caveat: rodent operant evidence. The behavioural readouts are lever-pressing rate, latency, and concurrent-choice reallocation. The transfer to REE's open-ended episodic environments is at the algorithmic level (effort-cost and opportunity-cost as architecturally separate score terms), not at the readout level.

## Confidence reasoning

Source quality high (canonical Salamone-Correa review, heavily cited, integrates broad rodent operant pharmacology). Mapping fidelity strong on the effort-vs-opportunity dissociation (R4) and adequate on substrate (DA system as activational); the specific opportunity-cost-on-time formulation comes more directly from Niv 2007, with Salamone providing the contrast that licenses architectural separation from existing effort-cost machinery. Transfer risk moderate (rodent operant tasks; algorithmic-level commitment). Aggregate 0.78.

According to PubMed, this paper appears under the cited PMID with the DOI as listed.
