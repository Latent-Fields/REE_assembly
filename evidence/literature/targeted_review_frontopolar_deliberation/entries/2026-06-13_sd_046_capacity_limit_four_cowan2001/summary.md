# Cowan 2001 -- The magical number 4: a capacity prior for the slot count

**Claims:** SD-046 (primary), SD-027, MECH-254
**Direction:** supports
**Confidence:** 0.62

## What the paper did

Cowan's BBS target article reconsiders the famous "magical number seven." He marshals a wide range of evidence -- from tasks that block chunking and rehearsal to performance discontinuities and indirect capacity effects -- to argue that the *pure* capacity of the **focus of attention** is a small fixed number averaging about **4 chunks** (range 3-5), considerably smaller than Miller's 7 (which Cowan argues was a compound estimate inflated by chunking and rehearsal). He carefully distinguishes this capacity-limited focal store from non-capacity-limited stores (sensory memory, activated long-term memory) that operate alongside it.

## Findings relevant to the claims

The goal-deliberation roadmap (GDL-8, layer L3) asks for the capacity-resource grounding behind the multi-slot fork. Before this pull, SD-046, SD-027, and MECH-254 had **zero** literature grounding -- they imported "N = 2-4 slots" and "top-k, k ~ 3-7" with no formal biological anchor, exactly the situation the project's biology-before-formal-definitions rule warns against. Cowan supplies the anchor:

- **SD-046 (multi-slot GoalState, N>=2).** The roadmap hedges "n=2-4 plausibly." Cowan converts that hedge into a principled prior: the focal capacity is small and fixed, around 4. The honest reading is that SD-046's slot count should be set *at* this bound, not as a free hyperparameter, and that combined with Koechlin's structural-2 branching limit the conservative default is N = 2 with N = 3-4 as a capacity-bounded extension.
- **SD-027 / MECH-254 (capacity-limited E3 access gate).** The claim that a top-k selector (k ~ 3-7) gates which E1/E2 content reaches E3 is the same capacity limit applied at the access boundary rather than to goals. Cowan's number constrains k toward the low end of the claim's stated range.

The deeper contribution is the **focal-vs-activated distinction**. Cowan's capacity limit is on the focus of attention, not on everything that is active. That maps directly onto a design REE has not yet committed: a *small* focal set of goal slots that occupy capacity, plus a *larger* activated pool (the ghost-goal bank, MECH-292) that does not. This is the right shape for SD-046 -- the arbitrator competes a handful of focal slots, while many candidate goals sit activated-but-not-focal.

## Limitations and caveats

The transfer risk here is the highest in this pull (0.42). Cowan measures human short-term storage of *chunks* -- digits, words, visual items -- not goal slots or latent broadcast units. The ~4 number transfers as an order-of-magnitude prior on N and k, not as a measured value for goal maintenance; "chunk" is not "goal slot." And the focal/activated distinction is a warning as much as a mapping: an SD-046 design that forced every maintained goal into the capacity-limited focus would over-constrain, since the biology explicitly allows many activated goals beside a small focal set.

## Confidence reasoning

Foundational, canonical BBS synthesis (source_quality 0.88). Held to 0.62 overall because mapping_fidelity is moderate (it bounds the count as a prior, across a domain gap) and transfer_risk is the pull's highest. Its real value is categorical: it takes SD-046/SD-027/MECH-254 from *no* literature grounding to a genuine capacity anchor. Promotes nothing (all candidate / v4; exp_conf stays 0).
