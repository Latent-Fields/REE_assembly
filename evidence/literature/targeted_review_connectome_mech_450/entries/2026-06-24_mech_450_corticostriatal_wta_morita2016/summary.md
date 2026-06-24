# Morita, Jitsev & Morrison (2016) — Corticostriatal circuit mechanisms of value-based action selection

*According to PubMed.* Morita K, Jitsev J, Morrison A, *Behavioural Brain Research* 311:110-121, 2016. [DOI](https://doi.org/10.1016/j.bbr.2016.05.017)

## What the paper did

This is a review that knits together the theoretical and experimental literature on how the corticostriatal loop implements value-based action selection, and how that implementation relates to reinforcement-learning algorithms (Q-learning, SARSA, soft-max policies). It is unusually well-matched to MECH-450 because it treats *exactly* the circuit MECH-450 abstracts: striatal projection neurons competing through inhibition, cortex feeding value-weighted inputs, and the question of whether selection is a hard "max" or a probabilistic "soft-max."

## Key findings relevant to MECH-450

Two messages run through the review, and MECH-450 needs both.

The supporting message: the striatum is *mostly inhibitory*, and **lateral inhibition among striatal neurons has classically been proposed to realize winner-take-all selection of the maximum-valued action** — i.e. a "max" operation. This is the textbook justification for MECH-450's central move: a surround-inhibition settling competition is the biologically motivated way to pick a committed action, and it is a more faithful model of the substrate than a feed-forward argmin computed outside any competitive dynamics.

The cautionary message: the classical clean-WTA view "has been challenged by the revealed weakness, sparseness, and asymmetry of lateral inhibition." So a true hard max may only be achievable on short timescales, and the cortical side of the loop — which *does* have recurrent excitation — may instead support temporal integration and a **probabilistic soft-max**. On longer timescales the authors suggest the circuit behaves as a *sequence of short WTA fragments* rather than one stable competition.

## How it maps to REE

This is strong support for the *form* of MECH-450 while sharpening its tuning risk. The claim already hedges toward "winner-take-MOST" rather than strict winner-take-all, and this review vindicates that hedge: biological lateral inhibition produces a graded, soft competition, not an idealized max. So the qualitative prediction — a recurrent surround-inhibition step can convert an additive `_modulatory_accum` blend into a competitive selection that a strong modulatory channel can tip — sits comfortably on the known physiology.

But the review names the exact failure mode that threatens the V3-bounded implementation. MECH-450 uses *fixed* (unlearned) inhibition for the minimal step. The review says real lateral inhibition is weak/sparse/asymmetric. If the fixed kernel is set too weak, the settling competition will not have enough gain to flip an F-dominated winner — the additive blend simply re-emerges and the conversion ceiling persists. If set too strong, the network over-commits to a locked attractor (MECH-450's perseveration pole). The "right" fixed gain is left open here; it is a tuning question the eventual REE experiment must answer empirically, not assume.

## Limitations and caveats

It is a narrative review, not new data, so it inherits the uncertainty of the primary literature it surveys. And its "sequence of short WTA fragments" observation raises a subtle worry for MECH-450's "a few rounds before commit": a small fixed number of settling iterations might capture a transient fragment rather than a settled winner, making the committed action sensitive to exactly how many rounds are run. That, too, is a design parameter the experiment should sweep rather than fix by fiat.

## Confidence reasoning

Source quality good (authoritative review, weak-data caveat for a non-empirical source). Mapping fidelity high — it addresses MECH-450's precise circuit and its precise known weakness. Net **0.70, mixed**: it endorses the mechanism's biological motivation and its soft-competition character while flagging that the very property MECH-450 relies on (inhibition strong enough to flip the winner) is empirically the weak link.
