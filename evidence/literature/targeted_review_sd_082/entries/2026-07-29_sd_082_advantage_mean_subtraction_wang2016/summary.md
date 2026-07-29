# Wang et al. 2016 — the same subtraction, for the same two reasons

**Claim:** SD-082 (`pfc.lateral_pfc.common_mode_invariant_trained_rule_to_action_readout`)
**Direction:** supports · **Confidence:** 0.80
**Source:** ICML 2016 (PMLR 48:1995–2003, Best Paper); preprint [arXiv:1511.06581](https://arxiv.org/abs/1511.06581)

## What the paper did

The dueling architecture splits a Q-network into two streams — a state-value estimate and a
state-dependent action-advantage estimate — and then has to recombine them. The obvious
recombination, `Q = V + A`, does not work, and the paper is unusually explicit about why: it "is
unidentifiable in the sense that given Q we cannot recover V and A uniquely." Add a constant to V,
subtract it from A, and Q is unchanged. The network has a degree of freedom that its output cannot
see.

Their fix is to subtract, from each action's advantage, the mean advantage across the action set:

```
Q(s,a) = V(s) + ( A(s,a) − (1/|A|) Σ_a' A(s,a') )
```

They considered subtracting the *max* instead (which forces the advantage of the greedy action to
zero, a cleaner identifiability argument) and chose the mean anyway, because "it increases the
stability of the optimization: with (9) the advantages only need to change as fast as the mean,
instead of having to compensate any change to the optimal action's advantage." The architecture
gave state-of-the-art Atari results, with the paper noting the benefit is largest in the presence
of many similar-valued actions.

## Why it matters for SD-082

SD-082(i) subtracts the per-tick mean candidate summary across the candidate set before the
lateral-PFC bias head. This paper is the reason that should not be read as an ad-hoc patch around
SD-008. Centering a per-alternative quantity against the mean over its own alternative set is an
established primitive in deep RL, and it was adopted for the same two reasons SD-082 gives.

The identifiability argument is the sharper of the two, and it explains something about V3-EXQ-822
that "the clamp saturated" alone does not. A component shared additively across every alternative
is *invisible in the output*, so no gradient can resolve it. That is why `prop_delta` was exactly
`0.0` rather than merely small, and why 70 episodes of REINFORCE moved nothing: the head was not
learning slowly, it was learning in a direction the output could not express. The stability
argument then supplies the second half — with the shared component removed, the trainable part no
longer has to track a large common signal, which is the trainability side of SD-082's problem
(head grad-norm `0.0` → `~6.1`).

The detail I find most persuasive is the incidental one: dueling's advantage is largest when there
are *many similar-valued actions*. That is about as close as the deep-RL literature comes to
describing REE's near-collinear candidate cone (`zworld_cone_min_cosine` 0.963) from the outside,
and it says the remedy helps most exactly where we need it to.

## Limitations — and one that should be recorded as a design constraint

The site differs, and this is not pedantry. Dueling subtracts the mean of the head's **output**;
SD-082 subtracts the mean of the head's **input**. For a linear map those are related by a
reparameterisation, but the SD-033a bias head is a nonlinear MLP. Centering the input relocates
each candidate within the nonlinearity — it changes which part of the function each candidate is
evaluated on — and dueling's linear identifiability argument says nothing about that. If the
differentiation is actually being lost at the head's first-layer nonlinearity rather than at the
output bound, input-centering could move the problem rather than remove it.

The second limitation is the one worth carrying forward into governance. In dueling, the shared
component is a **gauge freedom in the parameterisation**: it exists for any input, always, as a
property of writing `Q = V + A`. In SD-082, the common mode is a **contingent pathology of a
specific broken encoder**. Those are different kinds of thing. So this precedent licenses SD-082's
centering as a *read-out-stage mitigation for SD-008*, and it does **not** license inheriting it as
an encoder-independent architectural commitment. If SD-008 / SD-070 are ever repaired upstream, the
dueling analogy gives no reason to keep the centering, and it should be re-ablated rather than
assumed. Worth stating now, while the reason is fresh, because a default-off flag that quietly
becomes default-on is exactly how that kind of thing gets forgotten.

Finally, the optimisation regimes are not the same. Dueling is off-policy value-based learning with
a replay buffer and a target network; SD-082's head trains under on-policy REINFORCE in a short P1
window that has already been shown insufficient at the clamp. Nothing here predicts that centering
alone makes the head trainable *within the budget available*. It predicts only that the degeneracy
which made the budget irrelevant is gone.

## Confidence reasoning

Source quality 0.90 — ICML Best Paper, heavily replicated, and crucially the mean-aggregation
choice is *argued in the text* rather than buried as an implementation detail, which is what makes
it usable as evidence for a design_decision claim instead of a decoration on one.

Mapping fidelity 0.82, the highest in this pull. The operation, the stated motivation, and even the
stated favourable regime all correspond directly to SD-082(i) and to the 822 signature. The
deduction is for the input-vs-output site difference.

Transfer risk 0.35 — engineering to engineering, no species or modality leap, but different
optimisation regime and a different underlying cause for the shared component.

Aggregate 0.80. This is the entry that most directly de-risks SD-082(i) as a design choice. It
should not be read as saying anything about SD-082(ii), the tanh bound — the dueling architecture
has no bounded output and no saturation problem, so it is silent there. That half is where the
counter-evidence lives (see the Hausknecht & Stone entry).
