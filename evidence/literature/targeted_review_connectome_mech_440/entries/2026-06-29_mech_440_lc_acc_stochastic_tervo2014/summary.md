# Tervo et al. (2014) — Behavioral variability through stochastic choice and its gating by anterior cingulate cortex

**Claim tested:** MECH-440 (state-conditioned self-annealing tonic exploration noise floor)
**Direction:** supports · **Confidence:** 0.80
**Source:** *Cell* 159(1):21–32. According to PubMed (PMID 25259917), [DOI 10.1016/j.cell.2014.08.037](https://doi.org/10.1016/j.cell.2014.08.037).

## What the paper did

Tervo and colleagues put rats up against virtual competitors in a matching-pennies-style game. Like primates, the rats default to history- and model-based strategies — they try to *out-predict* the opponent. But when the competitor is built so that counter-prediction cannot win, the animals switch into a qualitatively different "stochastic" mode: they stop letting the outcomes of their own actions guide the next choice, and their behaviour becomes genuinely variable. Using circuit perturbations in transgenic rats, the authors show this switch is not incidental — it is causally controlled by **locus-coeruleus (noradrenergic) input into the anterior cingulate cortex (ACC)**. Normal ACC engagement is suppressed in the stochastic mode, and LC→ACC signalling is what flips it. Their interpretation: under uncertainty about the environment's rules, raised noradrenergic input alters ACC output and *prevents erroneous beliefs from guiding decisions*, thereby releasing behavioural variation.

## Why it grounds MECH-440's biological shape

MECH-440 does not just ask for noise — it asks for noise with a particular character: **state-conditioned** (engaged where it pays) and **self-annealing** (suppressed where a strategy is working). The hard part of justifying that claim is not the ML side (NoisyNet supplies the mechanism, see the companion entry) but the biological side: is there a real neuromodulatory system that turns exploration *up* exactly when the current policy stops paying off? Tervo et al. are the causal answer. The LC-NE system, gated by the utility of the ongoing strategy, injects behavioural stochasticity precisely when model-based selection fails — and withdraws it when counter-prediction works. That is the state-conditioned, pays-its-way profile MECH-440 wants its floor to have, demonstrated causally rather than merely correlated. This paper was cited at the MECH-440 adjudication (supports 0.82) as part of the biology-before-formal-definitions gate, alongside Aston-Jones & Cohen (2005); it is the more *causal* of the two.

## Where the analogy strains — and why I did not score it higher

Three gaps keep this at 0.80 rather than near the NoisyNet entry's 0.85:

1. **Granularity.** Tervo's effect is a near-*global mode switch* — suppress ACC, ignore outcomes — not a graded, per-parameter floor. MECH-440 implements continuous learned weight noise at the selection head. The *function* (more noise where exploration pays) maps cleanly; the *grain* (all-or-none mode vs. continuous floor) does not.
2. **Task structure.** The stochastic mode is triggered by an *unbeatable adversarial* competitor. REE's committed-action-diversity problem is not adversarial in that sense, so it is an open question whether a tonic floor helps committed-action diversity in a cooperative/foraging-type task the way mode-switching helps against an unbeatable opponent.
3. **Controller.** The biological control is LC→ACC gating. MECH-440's self-annealing is a *gradient on a sigma parameter*. So MECH-440 reproduces the *function* of the Tervo mechanism, not its biological controller — which is consistent with the ARC-106 stance of grounding by function, not homology, but should be stated plainly rather than glossed.

Net: strong causal support for the *shape* of MECH-440's floor (state-conditioned, withdrawn when strategy works), with the honest caveat that a behavioural mode switch in an adversarial rat task is not the same object as a per-parameter weight-noise floor in REE's non-adversarial selection head. The cross-species, cross-substrate transfer is the dominant uncertainty (transfer_risk 0.45).
