# Reward Shaping in Episodic Reinforcement Learning (Grzes, 2017) -> INV-087

**Claim tested:** INV-087 (`proxy_tethering_constraint`) -- direction **weakens**, confidence **0.68**. This is the disconfirming source the proposal required, and it is not a token one: it targets the exact regime REE operates in.

## What the paper did

The Ng, Harada & Russell (1999) theorem is stated for infinite-horizon MDPs. Grzes asks what happens to the "potential-based shaping preserves the optimal policy" guarantee when the task is *episodic* -- finite trajectories that terminate, which is what almost every goal-directed task (including REE's) actually is. He derives the relation between shaped and unshaped returns for an episode of length `n`:

```
G(pi') = G(pi) + gamma^n * Phi(s_n) - Phi(s_0)
```

The `- Phi(s_0)` term is a constant (same start distribution) and is harmless. The `gamma^n * Phi(s_n)` term is not: it depends on *which state the episode terminates in*, so it can differ across policies and therefore change which policy is optimal. The consequence is a necessary-and-sufficient condition the infinite-horizon statement hides: potential-based shaping is policy-invariant in episodic tasks **only if the potential of every terminal state is zero**. His proposed fix is exactly that -- assume `Phi = 0` for terminal states, while letting the same physical state keep its normal potential when it is *not* terminal in a given trajectory.

## Why this weakens INV-087 as worded

INV-087's `what_would_answer` and `description` assert, without qualification, that the potential-difference form `gamma*Phi(s') - Phi(s)` "leaves the true-goal optimal policy INVARIANT." Grzes shows that in REE's setting this is *conditional*. And the condition bites REE specifically and hard: the tethering potential INV-087 gestures at is a **goal-proximity** potential, which is by construction **largest at the goal**; and the goal is a **terminal** state (attaining it ends the episode). So REE's natural tethering candidate violates the terminal-zero requirement *maximally, at exactly the state the guard is supposed to protect*. A literal implementation -- "add `gamma*Phi(s') - Phi(s)` over goal-proximity and trust invariance" -- would still admit divergence through the `gamma^n * Phi(s_goal)` term. That is not a peripheral caveat; it is a load-bearing correction to the claim's design target.

The honest reading is that INV-087 is not *refuted* -- the repair is known and cheap (zero out, or subtract off, the potential at goal-attainment / episode end, per Grzes). But the claim's current wording overstates the guarantee by importing the infinite-horizon theorem into an episodic architecture without carrying the terminal condition. The V3-EXQ-872 probe that PASSed for INV-087 used a *no-env, no-training, single-hop* E3-selection landscape (deliberately, to dodge the monostrategy confounds), which is precisely a setting where the episodic terminal term does not arise -- so that PASS does not exercise this failure mode, and should not be read as having cleared it.

## Mapping caveat

Grzes analyses a clean single-objective discounted episodic MDP with well-defined terminal states. REE's "episode" and "goal attainment" are softer, multi-drive, and not always cleanly absorbing, so the `gamma^n * Phi(s_n)` decomposition does not transcribe term-for-term into REE. What transfers is the structural warning, not the exact algebra: a nonzero potential at a terminating goal re-opens the very divergence INV-087 exists to close. The magnitude of the effect on REE's substrate is untested -- it could be small in practice, which is why the transfer_risk (0.50) is non-trivial and the direction is `weakens` rather than a stronger refutation.

## Confidence reasoning

Source quality 0.78 -- rigorous and directly on-point, but a single-author conference paper. Mapping fidelity 0.66 -- the result maps cleanly onto the tethering form but REE's terminal states are not the idealised absorbing states of the analysis. Transfer risk 0.50 -- the effect is structurally guaranteed to exist for a goal-proximity potential but its size in REE's substrate is unmeasured. Direction **weakens**, assigned confidently: this is the counterweight to the Ng1999/Devlin2012 supports, and it should feed the claim's `pending_substrate_reconfirmation` flag -- specifically, a substrate reconfirmation of INV-087 should test the potential-difference proxy *with a nonzero goal potential in an episodic setting*, not only in the terminal-free single-hop landscape V3-EXQ-872 used.
