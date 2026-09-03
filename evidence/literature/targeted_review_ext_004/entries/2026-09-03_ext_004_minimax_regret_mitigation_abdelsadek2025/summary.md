# The falsifier: if changing the objective fixes it, the memory story is not needed (Abdel Sadek et al., RLC 2025) — EXT-004

**Source:** Abdel Sadek K, Farrugia-Roberts M, Anwar U, Erlebach H, Schroeder de Witt C, Krueger D, Dennis M. *Mitigating Goal Misgeneralization via Minimax Regret*. Reinforcement Learning Conference (RLC 2025). Preprint: arXiv:2507.03068 (v1 3 Jul 2025, v2 18 Jul 2025).

## Why a weakening entry belongs in this pull

EXT-004 is not a report that goal misgeneralization exists. It is an *explanation* of it: causal consequences do not carry forward across contexts, each episode starts from a clean slate, and REE's residue field plus commit boundary are the structural remedy. An explanation has competitors, and this one has a formal, recent, refereed competitor. Leaving it out would present governance with a claim that looks unopposed when it is not — the same reasoning that put Silver et al. into the EXT-003 pull.

## What the paper does

The authors formalise the goal-misgeneralization setting and then ask a question nobody had asked precisely: does the failure depend on *what you told the optimiser to maximise*?

It does. They show that goal misgeneralization is **possible under approximate optimization of the maximum expected value (MEV) objective, but not under the minimax expected regret (MMER) objective**. Then they check it empirically: domain randomization — the standard MEV-based training method — exhibits goal misgeneralization in procedurally-generated grid-worlds, while current regret-based unsupervised environment design methods are more robust to it. They are careful to add that current UED methods "don't find MMER policies in all cases".

## What this does to EXT-004

Directly and unpleasantly: it dissolves the inference the claim depends on.

EXT-004's argument runs *goal misgeneralization occurs → causal consequences are not carrying forward → a persistent residue is needed*. This paper cuts the first arrow. If the phenomenon is provably absent under a different training objective, then its presence under the usual one is a fact about the objective, not a symptom of missing memory. No persistent trace, no cross-episode accumulation, no commit boundary appears anywhere in the remedy — and the remedy is *simpler* than REE's, which matters, because a simpler sufficient explanation is the standard reason to stop invoking a more elaborate one.

This is not an isolated result either. Put it beside the Langosco finding in this same pull that **2% of training levels with randomly placed coins** largely repairs CoinRun, and there are now two independent interventions — one distributional, one objective-level — that mitigate goal misgeneralization with no memory mechanism added at all. Two is a pattern.

It also puts pressure on the taxonomy. EXT-004's `ree_failure_mode_analog` is **`moral_amnesia`**, a label that presupposes a memory-shaped cause. If the cause is objective-shaped, the analogy is mis-drawn and IMPL-005 may be filing this failure mode under the wrong root — which is a governance question rather than a literature one, but it is this paper that raises it.

## How far this may be pushed, and where it stops

I do not think it retires the claim, and it is worth being exact about why not, because the reasons are structural rather than defensive.

The theoretical result is a statement about the authors' own formalisation under approximate optimisation of stated objectives — a property of that model, not a guarantee about any particular trained system. The empirical work is procedurally-generated grid-worlds, the same class of environment as Langosco and equally distant from an embodied agent facing genuine irreversibility. The authors themselves flag that current UED methods do not reach MMER policies in all cases, so the practical mitigation is partial and they say so.

And the limit that matters most: **MMER is a training-time objective.** It shapes what the agent learns. It says nothing whatever about an agent already deployed, encountering a context nobody anticipated — which is exactly where a residue field would operate. So the two proposals are not competing solutions to one problem; they intervene at different points in the lifecycle. What this paper undercuts is EXT-004's *inference from phenomenon to mechanism*. It does not establish that persistent consequence is useless, and nothing here shows that an MMER-trained agent carries the cost of a past harm into a novel context — it shows such an agent is less likely to have acquired the wrong goal in the first place.

## What REE now owes

The most useful thing this entry does is convert a comfortable position into an owed experiment. As things stand, EXT-004 cannot cite goal misgeneralization as evidence for the residue field, because a simpler intervention accounts for the same observations. What would restore the citation is a **discriminating test**: a setting in which consequence carry-forward helps and MMER-style training does not. The obvious shape is a deployment-time novelty that no training-distribution design could have anticipated, where the agent's *own prior harm* is the only available signal. Registering that as owed work is, I think, more valuable to REE than another demonstration of a phenomenon that is already beyond dispute.

## Confidence

0.58. Source quality 0.80 — a refereed venue, authorship overlapping the group that defined the problem, and a proved separation paired with a matching empirical comparison, which is an unusually complete shape for a mitigation paper. Mapping fidelity 0.70 is high *for a weakening entry*, and that is the substance rather than an accident: the paper is about the same phenomenon under the same name, so the two positions genuinely contradict on the causal question instead of talking past each other. Transfer risk 0.45 is the grid-world-to-embodied discount, identical to the one applied to Langosco. The aggregate sits below the components because of the training-time versus deployment-time scope limit — MMER cannot be a complete answer to EXT-004 because it acts at a different point in the lifecycle — and the number records that structural boundary, not any doubt about the result itself.
