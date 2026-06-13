# Tonic dopamine: opportunity costs and the control of response vigor (Niv, Daw, Joel & Dayan 2007)

**Claim(s):** MECH-394 (multidrive arbitration policy) · cross-ref SD-012 (drive-scaled benefit)
**Direction:** supports · **Confidence:** 0.70
**Source:** Niv, Daw, Joel & Dayan (2007), *Psychopharmacology (Berl)* 191(3):507-520. According to PubMed, [DOI: 10.1007/s00213-006-0502-4](https://doi.org/10.1007/s00213-006-0502-4).

## What the paper did

Niv and colleagues set out to give a normative, computational account of a fact long known to pharmacologists but never properly explained: dopamine controls the *vigour* -- the strength, rate, latency -- of responding, not just which action is chosen. They built an average-reward reinforcement-learning model in which the agent decides not only *what* to do but also *how fast* to do it, paying a cost for acting quickly and reaping the benefit of getting reward sooner. The optimal latency falls out of balancing those two terms.

## Key findings relevant to the claim

The pivotal construct is the long-run **average reward rate**, which in their model plays the role of an **opportunity cost** -- the cost of time. If the world is rich (high average reward), then every second spent dawdling is a second of forgone reward elsewhere, so the optimal policy is to act vigorously; if the world is lean, sloth is cheap. They marshal evidence that this average-reward signal is reported by *tonic* (slowly varying, background) dopamine levels, putatively in nucleus accumbens, distinct from the phasic dopamine that signals prediction error for discrete action selection. The result unifies psychological and computational accounts: higher tonic dopamine maps to more vigorous responding because it represents a higher opportunity cost of inaction.

## How it translates to REE

MECH-394 proposes that behaviour under several simultaneously-active drives is set by a soft-competitive orchestration rather than a fixed priority. The hard problem any such policy faces is *commensurability*: how do you compare the pull of hunger against the pull of fear against the pull of exploration when they are measured on different scales? Niv et al. hand REE the missing common currency. The opportunity cost of time is the universal price tag: committing to one drive axis means forgoing whatever benefit the other axes would have yielded in the same interval. An arbitration policy that allocates behaviour across drives is, structurally, solving the same average-reward optimisation Niv formalises -- and the slowly-varying tonic signal they describe is exactly the kind of global modulator that would set the overall vigour with which the *winning* drive is then pursued. This is why the entry also cross-references SD-012: REE already commits to drive-scaled benefit signals, and Niv's tonic opportunity-cost term is the global complement that sits above the per-candidate liking-stream score_bias of MECH-295.

## Limitations and caveats

The crucial honesty here: Niv et al. model how vigorously to perform an *already-selected* action, not which of several competing drives to select. The reading I have given -- that opportunity cost is the currency over which arbitration optimises -- is a reasoned extension licensed by the structure of the average-reward framework, but it is not the paper's own claim, and I have set mapping fidelity (0.68) and overall confidence (0.70) to reflect that. It would be an over-read to cite this as evidence that MECH-394's *winner* is chosen by opportunity cost alone. A second caveat matters for design: the average-reward currency is a single global scalar. If REE's arbitration needs per-axis differentiated valuations -- so that fear and hunger are priced on genuinely different scales rather than reduced to one number -- then a lone opportunity-cost term is insufficient and must be combined with axis-specific benefit terms. This connects to the candidate-differentiated-affect concern already live elsewhere in the registry: a global vigour signal with no cross-axis gradient cannot, by itself, carve which drive wins.

## Confidence reasoning

Source quality is high: this is a foundational, heavily-cited normative theory with a clear pharmacological anchor. I cap mapping fidelity because the model's explicit target is vigour/latency and the inter-drive-arbitration use is extension rather than direct test. Transfer risk is moderate -- the average-reward principle is computational and should be substrate-general, but its tonic-dopamine/accumbens grounding is rodent-specific. Net 0.70, raising MECH-394's literature confidence only; the claim stays substrate_conditional V4 with exp_conf = 0.
