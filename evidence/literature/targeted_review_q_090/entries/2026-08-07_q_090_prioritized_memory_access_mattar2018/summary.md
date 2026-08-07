# Mattar & Daw 2018 -- the normative answer is a product, not a threshold

**Claim tested:** Q-090 -- is the retained-alternative admission criterion the interrupt's scale at a lower cut, or an independent relevance criterion such as goal-match?

**Direction:** mixed. **Confidence: 0.62** -- the highest in this pull.

## What the paper does

Mattar and Daw ask a question that is almost exactly Q-090's question in a different vocabulary: given that an agent cannot consider everything, which memories *should* it access when deliberating? They derive the answer normatively rather than fitting it to data. Each candidate memory gets a utility -- how much extra reward would be earned because accessing it improves the agent's future choices -- and access proceeds in that order.

That utility factorises into two terms. **Gain** is how much accessing this memory would change the policy: a memory that would not alter any decision has no gain no matter how dramatic its content. **Need** is how likely the agent is to actually find itself where that memory applies. Priority is their product. The theory then explains a striking range of hippocampal replay phenomena -- forward and reverse sweeps, their differing conditions, the relation to reward -- and unifies accounts of replay as planning, as learning, and as consolidation that had been treated as competitors.

## Why it bears on Q-090

Every other source in this pull argues for or against one of Q-090's two horns. This one dissolves the disjunction.

The same-scale horn says the criterion is a magnitude. The independent-criterion horn says it is relevance. Mattar and Daw derive, from optimality rather than from data, that a rational criterion must be *both*, combined multiplicatively. Gain is the magnitude-like term: it asks how much difference this alternative could make. Need is the relevance-like term: it asks whether the agent will be in a position for that difference to matter. Neither alone is a defensible rule, and the multiplication is not decorative -- either factor at zero kills the priority. A large predicted harm about a situation the agent will never re-enter is not worth retaining. A perfectly goal-matched alternative that would not change any future choice is not worth retaining either.

The consequence for MECH-485 leg 3 is concrete. Implementing retention as a low cut-point on the leg-1 magnitude is not a thrifty approximation of this account; it is a different rule that discards the need term entirely, and it will systematically retain the wrong alternatives. This converges with the Pupillo entry, which reaches a compatible conclusion empirically and from a different direction: a scalar cut cannot express what the retention rule actually does.

There is an internal-consistency argument too, and I weight it. This paper is already the normative anchor for MECH-292's ghost-goal bank, where priority scales with wanting, goal-match, staleness and recoverability rather than staleness alone. If leg 3's admission criterion adopts the same two-factor structure, then the retained-alternative store and the ghost-goal bank become two applications of one principle instead of two independently-invented rules that will drift apart. Q-090's own framing names MECH-292/293 as the source of the goal-match reading; it is worth noticing that the paper underwriting MECH-292 does not actually endorse a pure goal-match criterion either.

## Caveats and where the mapping strains

The structure transfers. The terms do not, and I would rather say so than let a convenient identification pass.

*Gain* is expected improvement in future decisions inside a well-specified MDP with a known reward function. It is not the magnitude of a predicted harm. These diverge in a case REE should care about: a large predicted harm the agent can do nothing about has high magnitude and near-zero gain, and this theory says discard it. For pure decision optimisation that is right. For responsibility attribution -- which is what leg 3 says the retained alternative is *for* -- it may be exactly wrong, since the harms we hold ourselves accountable for are not only the ones we could have re-optimised around. Nothing in this framework has any analogue of responsibility attribution at all.

*Need* is expected future state occupancy under the current policy: a formal quantity, not a semantic one. MECH-292's goal-match carries content about what the agent wants. Reading need as goal-match is an interpretation, and a loose one.

The deepest mismatch is about which operation is being modelled. Mattar and Daw prioritise *access to stored memories* -- which item to reactivate during deliberation or rest. Q-090 asks about *admission to storage*. Their theory presupposes the item is already in the store and says nothing about how it got there. Those may well be governed by related principles, but that is a hypothesis, not something the paper shows.

Finally, one observation the authors make deserves recording as a design warning rather than a caveat: they suggest dysfunction of this prioritisation mechanism may underlie rumination and craving. A leg-3 retention rule tuned toward over-admission has a named pathology waiting for it -- an agent that cannot stop revisiting the roads it did not take.

## Confidence reasoning

Source quality 0.9: Nature Neuroscience, a normative derivation rather than a fitted correlation, validated against a broad range of independent replay findings rather than a single effect, and extensively built upon since. Mapping fidelity 0.6: the two-factor multiplicative structure -- the load-bearing content -- transfers directly, while gain and need do not map term-by-term onto predicted-harm magnitude and goal-match, and the access-versus-admission gap is real. Transfer risk 0.4, held down because what is being transferred is a structural principle about what any rational prioritisation rule must contain, not a parameter or a species-specific result. The aggregate 0.62 makes this the entry I would build from, while recording that building from it means importing a structure and then doing the work of defining REE's own two terms.
