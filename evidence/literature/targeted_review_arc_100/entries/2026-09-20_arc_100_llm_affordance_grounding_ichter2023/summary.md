# Do As I Can, Not As I Say: Grounding Language in Robotic Affordances (Ichter et al., CoRL 2022 / PMLR 205)

## What the system does

SayCan is a robot that takes a high-level English instruction -- "I spilled my drink, can you help?" -- and carries it out in a real kitchen. It has two components that matter here. A large language model scores candidate next actions by how plausible they are as continuations of the instruction: *say*. A learned value function over a library of pretrained visuomotor skills scores those same candidates by how likely the robot is to succeed at them from its current state: *can*. The product of the two scores selects the action. The language model proposes; the affordance function vetoes.

Evaluation is on 101 real-world instructions across 7 instruction families. In a mock kitchen the full system reaches 84% plan success and 74% execution success; in a real kitchen, 81% and 60%. The ablation that makes this entry worth writing is the *no value function* baseline -- selection by language-model score alone, no affordance grounding -- which reaches 67% plan success. Seventeen percentage points is what grounding buys.

## Why this entry is here, and why it is scored mixed

A literature directory for a prohibition that contains only confirming sources is not a governance record; it is an advocacy file. ARC-100 is a strong negative commitment -- no imported transformer block, no LLM as cognitive authority -- and it deserves at least one entry that pushes back. This is that entry, and it is useful precisely because it pushes in one direction while supporting strongly in another.

**The supporting direction.** ARC-100's operational criterion says a mined cut counts as grounded only if it changes perception, attention, action, memory, rule-availability or coordination. Until now that has been a stipulation -- reasonable, but asserted. SayCan measures it. Linguistic plausibility and executable appropriateness come apart, they come apart on real hardware in real kitchens across 101 tasks, and the distance between them is 17 points of plan success. That is the criterion with a number attached, and it is the cleanest such number I found in this pull. It is worth noting that the paper's title is itself a statement of ARC-100's criterion: *do as I can, not as I say*.

There is a second, subtler gift in the numbers. Plan success 84% against execution success 74%, and in the real kitchen 81% against 60%. Even a grounded plan degrades badly on contact with the world. ARC-100's criterion is binary -- a cut either changes one of the six behaviours or it does not -- and this gap suggests the binary is too coarse. Changing action is necessary for a cut to be grounded; it is plainly not sufficient for the cut to be *useful*. The current criterion cannot express that difference.

**The pushing-back direction.** The system that produces all of the above imports a large language model wholesale and uses it as the source of task decomposition. ARC-100 forbids this. And the 67% floor is the awkward part: the imported model was not a decorative front end contributing nothing. Left entirely to itself, with no affordance grounding at all, it produced correct plans for two thirds of 101 real instructions. Whatever structure that is, it is real, and ARC-100's blanket prohibition forgoes it.

## How much the counterexample actually bites

Less than it first appears, but not nothing, and I want to separate those carefully.

ARC-100's prohibition has two clauses that are usually read together and are in fact different. *No LLM as cognitive authority* is aimed at letting a language model sit in REE's value and decision path -- deciding what matters, what follows, what is permitted. SayCan does not do that. The LLM proposes and the affordance function disposes; a linguistically perfect suggestion the robot cannot execute is vetoed. That architecture is arguably much closer to *mining under veto* than to *import as authority*, and on this reading SayCan is not a counterexample to ARC-100 at all but an unusually literal instance of its method: mine the model for candidates, ground them against what the substrate can actually do, keep only what changes action.

But the second clause -- *no imported transformer block* -- is stated as an architectural fact, not as a relation. SayCan does import one. On the text as written, the counterexample stands, and it stands with a measured benefit attached. My reading is that ARC-100's prohibition is currently broader than its own justification supports, and that the two clauses should be separated, with the authority clause kept absolute and the import clause restated as conditional on the veto relation. That is a recommendation for governance, not a finding, and I have not acted on it.

## Limitations

Domain distance is severe and I have scored it accordingly. This is instruction-following for a robot with a *pre-existing* library of skills and value functions; the language is human English supplied from outside; the grounding is a value function over skills that already work. REE's V6 problem is the reverse and much harder: mining candidate *pre-linguistic* primitive cuts and asking whether they change a substrate that does not exist yet. Nothing in this paper bears on the question GRAM-2 actually asks -- whether grammatical categories identify real cognitive joints. The 17-point ablation travels. Very little else does.

## Confidence

0.68, `mixed`. Source quality 0.82 -- CoRL, real hardware, 101 tasks, and crucially the ablations are reported rather than inferred by me. Mapping fidelity 0.55 and transfer risk 0.48 are the lowest and highest in this pull respectively, for the same reason. I have set the aggregate above the fidelity component rather than at it, because the single datum this contributes is unusually clean and speaks directly to a criterion REE has otherwise been asserting without measurement -- but a reader should treat this entry as one number plus a useful argument, not as broad support.
