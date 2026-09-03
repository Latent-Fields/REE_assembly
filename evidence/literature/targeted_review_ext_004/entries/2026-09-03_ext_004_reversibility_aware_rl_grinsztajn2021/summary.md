# Irreversibility is learnable — but forwards, not backwards (Grinsztajn et al., NeurIPS 2021) — EXT-004

**Source:** Grinsztajn N, Ferret J, Pietquin O, Preux P, Geist M. *There Is No Turning Back: A Self-Supervised Approach for Reversibility-Aware Reinforcement Learning*. Advances in Neural Information Processing Systems 34 (NeurIPS 2021). Preprint: arXiv:2106.04480.

## Why it is here

EXT-004's `ree_mechanism` list leads with an irreversibility idea, and REE's architecture posits a **commit boundary** at which an action passes from revisable simulation into irreversible execution. The reviewer's first objection to any such structure is that the boundary has to be hand-placed — that "irreversible" is a designer annotation smuggled in as an architectural fact. This paper is the strongest existing answer to that objection, so it belongs in the pull even though, as it turns out, it does not speak to EXT-004's central assertion.

## What the paper does

The trick is elegant and worth stating precisely, because the elegance is the evidence. Take an agent's trajectories, sample pairs of events at random, and train a network to rank them in **chronological order**. The intuition: if two events are *always* observed in the same order, something irreversible probably lies between them — you never see the box come back out of the corner. Ranking accuracy therefore becomes an estimate of reversibility, and the estimate is obtained **fully self-supervised, from experience, with no priors and no reward function**.

Two algorithms follow, one for exploration (RAE) and one for control (RAC). Evaluation includes Sokoban, which is the canonical hard case precisely because pushing a box into a corner cannot be undone. On synthetic tasks the authors report control policies that "never fail" and that "reduce to zero the side-effects of interactions, even without access to the reward function."

## What this settles, and what it does not

**Settled:** a commit-boundary-like signal can be *discovered* rather than *declared*. That is the harder half of making ARC-013's substrate story architecturally credible, and it is now demonstrated. REE can stop treating irreversibility-detection as an open engineering problem.

**Not settled, and this is the crux:** the estimator runs *forwards*. It asks "is this action irreversible **from here**?" EXT-004 asks something else entirely — "did I do this before, at what cost, and does that cost follow me into a context that merely resembles the old one?" The first is prospective and state-local. The second is retrospective and cross-context. They share the word "irreversible" and almost nothing else, and the shared vocabulary is exactly what makes the mis-mapping tempting.

There is a second, quieter problem. The reversibility signal is inferred from the chronological structure of events the agent *has already observed in that environment*. A freshly deployed agent in a genuinely novel context has no estimate at all — which is precisely the deployment situation goal misgeneralization is about. The mechanism arrives exactly when it is least needed and is absent exactly when EXT-004 says it matters.

And a third, which is awkward rather than fatal. Side-effects go to zero **without access to the reward function**. So an irreversibility signal is obtainable entirely independently of any harm or value representation. REE couples the commit boundary to the residue field; this result shows that coupling is not *forced* by the need for irreversibility detection. It may still be right — a boundary that knows nothing of harm is a boundary that cannot weight one irreversibility above another — but it is now an additional architectural commitment requiring its own justification rather than a consequence of something already established.

## A registry discrepancy found while doing this

This needs recording because it affects whether the entry is testing what it appears to test.

EXT-004's `ree_mechanism` list in `claims.yaml` reads:

- `ARC-013  # commit boundary: authority transition for irreversible actions`
- `INV-008  # residue couples into selection across episodes`

Neither gloss matches the claim it annotates. **ARC-013** is registered as *"Residue is persistent latent-space curvature; hippocampal paths form a cognitive map"* — a residue-geometry claim, not a commit-boundary claim. **INV-008** is registered as *"Precision is routed and depth-specific, not global"* — a precision-routing invariant with no residue content at all. The commit-boundary material lives elsewhere in the registry; ARC-003 and MECH-061 are the visible candidates. The same INV-008 mis-gloss appears on EXT-002, so this is drift across the `EXT-*` block rather than a one-off typo.

I have not edited `claims.yaml` — mechanism re-mapping is a governance decision, and a literature pull is the wrong place to make it. A governance flag has been raised instead. The practical consequence for *this* entry is that it is scored against the mechanism EXT-004's **notes** describe, which are unambiguous, rather than against the mechanism its `ree_mechanism` list names, which may be wrong.

## Confidence

0.62, the lowest of the four non-counterweight entries. Source quality is high (0.84): NeurIPS main track, a clean theoretical motivation for the surrogate task, two concrete algorithms, Sokoban as the hard case. Transfer risk is the highest here (0.45) — gridworld reversibility to an embodied action loop is a substantial step. But mapping fidelity (0.48) is what determines the aggregate: the paper's quantity and the claim's quantity are different objects wearing the same word. The entry earns its place by settling the "can it be learned at all" question and by surfacing the registry discrepancy, not by supporting EXT-004's central assertion, and the number should not be read as though it did.
