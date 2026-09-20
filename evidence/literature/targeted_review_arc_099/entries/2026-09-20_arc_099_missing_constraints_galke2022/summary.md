# Emergent Communication for Understanding Human Language Evolution: What's Missing? (Galke, Ram & Raviv, EmeCom @ ICLR 2022)

## What the paper does

This is a short position paper from a group that sits on the language-evolution side of the fence rather than the machine-learning side -- Raviv in particular is known for human group-size experiments in which participants invent miniature languages under controlled conditions. The paper asks a pointed question of the deep-learning emergent-communication literature: do neural agents and humans actually produce the same phenomena, and if not, why not?

The authors take three phenomena concerning compositionality and check them across both literatures. *Ease-of-learning* -- compositional languages are easier to acquire -- replicates. *Generalization* to unseen meanings does not fully replicate in neural agents. And the *group-size effect* -- the robust human finding that larger communities converge on more systematic, more compositional languages -- does not fully replicate either. Their diagnosis is that the simulations are missing constraints that are load-bearing in humans. They name two: bounded memory, and the alternation between speaker and listener roles.

## Why this is mixed rather than supporting, and what it does to ARC-099

ARC-099 is not a mechanism claim. Its entire content is an *inventory* asserted to be jointly necessary, and its value is as a machine-checkable V6-entry gate. That makes it unusually vulnerable to a particular kind of evidence: a credible argument that the list is wrong. This paper is that argument, from people whose day job is running the human version of the experiment.

The supporting half is real and should not be lost. Galke et al. share ARC-099's methodological premise outright -- that emergent structure is a function of specific cognitive and communicative constraints, and that when structure fails to appear, the honest first hypothesis is a missing constraint rather than a missing architecture. That is the V6-entry gate's whole justification, argued independently and from the other direction.

The weakening half is in two parts, and the second is worse than the first.

**Part one: two conditions ARC-099 does not list.** Bounded memory and speaker/listener role alternation. Role alternation is the one that should sting, because it is not a property of any agent's substrate -- it is a property of the *interaction protocol of the ecology*, and nothing in ARC-099's fourteen items implies it. Every referential-game substrate REE would naturally reuse (including Kottur's, the sibling entry in this directory) has a fixed sender and a fixed receiver. A V6 ecology could satisfy all fourteen of ARC-099's conditions and still omit role alternation entirely, by construction, without anything in the gate noticing. Note also that "bounded memory" does not simply duplicate ARC-099's existing "episodic memory" item -- it inverts its polarity. The inventory says memory must be *present*; this paper says it must be *limited*. Both can be true, but ARC-099 currently says only one of them.

**Part two: a listed condition that may not transfer.** ARC-099 lists partner variation. Galke et al. report that partner variation produces the group-size systematicity effect in humans and fails to reproduce it in neural agents. If that holds, then a V6 ecology can satisfy the partner-variation condition on paper -- multiple partners, genuine variation -- and get none of the structure the condition was put on the list to deliver. A gate item that is satisfiable but inert is worse than a missing one, because it passes.

## Limitations, stated plainly

This is a four-page non-archival workshop paper with no new data. Every empirical claim in it is an assertion about a literature, and "not fully replicated" is doing quiet work throughout -- the paper does not quantify the gap, does not specify which simulations were compared against which human studies, and does not distinguish "fails to replicate" from "has not been properly tested". Before anyone rewrites the V6-entry gate on the strength of this, the primary group-size work it leans on should be pulled and read directly.

There is also a target mismatch worth being explicit about. Galke et al. care whether emergent-communication simulations are valid *models of human language evolution*. ARC-099 cares whether a signalling probe in REE would be *non-vacuous*. These are adjacent, not identical. REE does not owe human-likeness. An emergent REE protocol that failed to reproduce human group-size effects would be a serious problem for this paper's research programme and might be no problem at all for REE's -- unless one thinks, as ARC-009 and MECH-010 arguably do, that the human bootstrap sequence is the thing being modelled. That is a question about REE's commitments, not one this paper can settle.

## Confidence

0.66, `mixed`. The component profile is inverted relative to everything else in this pull: mapping fidelity 0.80 -- the highest here, because the paper's question is nearly verbatim ARC-099's question -- against source quality 0.62, the lowest, because the empirical weight is entirely borrowed. I have deliberately held the aggregate below the component mean rather than above it. A finding that an enumerated inventory is missing two items is exactly the sort of thing that should change a contract, and therefore exactly the sort of thing that should be verified against primary sources first. The right next move is a follow-up pull on Raviv's group-size experiments; the right move today is to record the two candidate conditions in the inventory's open questions rather than to add them.
