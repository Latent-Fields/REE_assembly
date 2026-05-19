# Niv, Daw, Joel & Dayan (2007) — Tonic dopamine: opportunity costs and the control of response vigor

*According to PubMed. Psychopharmacology (Berl) 191(3):507-20. [DOI](https://doi.org/10.1007/s00213-006-0502-4) · PMID 17031711.*

## What the paper did

Niv and colleagues asked a question that, at the time, the reward-prediction-error account of dopamine had quietly stepped around: phasic dopamine may tell you *which* action to take, but what tells you *how hard, how fast, how often* to take it? They built an average-reward reinforcement-learning model of free-operant behaviour in which the agent chooses not only an action but the latency at which to emit it. Acting faster costs energy; waiting costs forgone reward. The quantity that prices the waiting is the long-run average reward rate — the opportunity cost of time. The model's central result is that optimal response vigor scales with this average reward rate, and the authors marshal pharmacological and lesion evidence that tonic dopamine, plausibly in the nucleus accumbens, is the physiological carrier of that quantity.

## Why it matters for MECH-320

MECH-320 is not merely *consistent* with this paper; it is, by its own functional restatement, an implementation of it. The claim posits a tonic vigor scalar `v_t` — a slow EWMA over the realised E3-score stream — that adds `v_t * w_action` to action trajectories and `v_t * w_passive` to no-op trajectories. That is the Niv opportunity-cost algebra transposed from response latency onto discrete E3 trajectory scoring. The recent collapse of ARC-068 (opportunity-cost no-op penalty) into MECH-320 is vindicated here: in the original formalism the no-op penalty and the action bonus are not two mechanisms but two faces of one signed scalar, exactly as the ARC-068 lit-pull R3 verdict concluded.

## Limitations and the honest caveat

The paper is a normative model, not a measurement, and that shapes how much it can underwrite. It establishes that *if* an agent is optimising average reward, a vigor signal proportional to the reward rate falls out for free — it does not establish that any particular substrate (biological or artificial) must compute it that way, nor does it adjudicate whether the vigor signal is separable from a learning signal. That separability is precisely where MECH-320 stakes a distinctness claim (against MECH-313's noise floor and against learning-rate effects), and this paper is silent on it; Hamid et al. (2016), in the same review folder, actually finds a *single* shared decision variable, which is a more pointed test of that boundary. The transfer here is computational rather than anatomical: REE earns the formalism, not the striatal pharmacology.

## Confidence

I assign 0.88, `supports`. Source quality is as high as this literature offers (the canonical Dayan/Daw/Niv treatment). Mapping fidelity is near-exact because MECH-320 adopts the formalism by name. The discount is the ordinary risk of moving a normative result from rodent free-operant latency into REE's E3 scorer — real, but small, and outweighed by the directness of the mapping for a mechanistic claim of this kind.
