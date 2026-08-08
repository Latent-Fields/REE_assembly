# Florensa, Held, Geng & Abbeel (2018) — Automatic Goal Generation for Reinforcement Learning Agents

**ICML 2018, PMLR 80:1515-1528 · [proceedings](https://proceedings.mlr.press/v80/florensa18a.html) · [arXiv:1705.06366](https://arxiv.org/abs/1705.06366)**
**Claim tested: MECH-428 · direction: supports · confidence: 0.62**

## What the paper did

The starting observation is that an RL agent trained in the ordinary way "is only capable of achieving the single task that is specified via its reward function". Florensa and colleagues replace the single task with a *generator*: a network that proposes goals, each goal being a parametrized subset of the state space to reach. The generator is trained adversarially against the agent's own current competence, so that the goals it proposes are always at the appropriate level of difficulty — hard enough that success is not guaranteed, easy enough that success happens. This produces a curriculum automatically, and the agent learns a wide set of tasks under sparse reward with no prior knowledge of its environment.

## Why this speaks to MECH-428

MECH-428's mechanism rests on subgoals being **reliably attainable** — attainability is what generates the repeated attainment and the cross-level credit that does the seeding work. The claim states that requirement but does not say how it is met, and in a sparse-reward setting that is not a small gap: the whole difficulty is that nothing is reliably attainable to begin with.

This paper is the sharpest computational answer I know of. "Reliably attainable" cannot be a fixed property; it has to be *tracked*, held at the moving boundary of what the agent can currently do, and re-evaluated as competence changes. That is a zone of proximal development made mechanical, which is directly useful given that MECH-428's notes ask for a Vygotskian anchor — this converts the framing into something implementable rather than merely evocative. The Wood, Bruner & Ross entry in this directory supplies the developmental original; this supplies the algorithm.

It also demonstrates the precondition MECH-428 needs: under sparse reward, an appropriately-graded goal curriculum expands what the agent can reach, starting from an agent that can reach almost nothing.

## What this entry is not evidence for

I have set `mapping_fidelity` at 0.58, below the 0.6 line, and I want to be explicit about why rather than let the number pass unexplained.

**There is no goal hierarchy in GoalGAN.** It is flat goal-conditioned RL with a curriculum. Nothing in the architecture plays the role of the superordinate goal that MECH-428 says gets bootstrapped from below. So it cannot, even in principle, exhibit the formation-direction effect the claim asserts — it shows *reachability* expanding, which sits nearer to MECH-216/217 (populating the wanting landscape for reachability) than to MECH-428 proper. This entry evidences a precondition of the claim, not the claim, and reading it otherwise would inflate MECH-428's literature grounding with support it does not have.

Two smaller boundaries. The parametrized goal space is designer-supplied, so "without requiring any prior knowledge of its environment" is narrower than it reads — the agent discovers which goals within a given space are currently attainable, not what the space of goals is. And the environments are continuous-control navigation and manipulation tasks with well-behaved, densely connected state spaces, where an intermediate-difficulty goal reliably *exists* to be found. REE's goal-seeding failures occur in settings where the availability of any such intermediate rung is precisely what is in doubt. The method assumes the ladder has a next step; MECH-428's hard case is where it may not.

That last point is worth carrying into EXP-0390's design. The adversarial generator's failure mode is silent: if no intermediate-difficulty goal exists, it will still produce goals, they will simply all be too hard, and the run will look like a training failure rather than a diagnosis. An REE implementation should instrument the attainability distribution directly rather than inferring it from whether learning happened.

## Confidence reasoning

Source quality 0.80 — ICML 2018, a well-replicated idea that spawned a substantial automatic-curriculum literature. Mapping fidelity 0.58 — the dominant discount, set deliberately below 0.6 to record that this is honest evidence for a precondition and would be misleading as support for parent formation. Transfer risk 0.35 — same machine class as REE; the residual is the well-behaved-state-space assumption. Aggregate 0.62.
