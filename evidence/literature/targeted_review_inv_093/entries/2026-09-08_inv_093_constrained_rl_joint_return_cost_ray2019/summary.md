# Ray, Achiam & Amodei (2019) -- Benchmarking safe exploration in deep RL (Safety Gym)

**Claim tested:** INV-093 (skill optimisation must not trade harm sensitivity for competence)
**Direction:** supports | **Confidence:** 0.60

## What the report did

Two things, and the second is why it is here. First, it argues that safe exploration research should standardise on *constrained* RL as its formalism: the agent maximises return subject to a bound on cumulative constraint cost, and the two quantities stay separate objects throughout. Second, it ships Safety Gym -- a suite of high-dimensional continuous control environments in which a robot navigates toward goals among hazards and fragile objects, accruing a per-step cost signal distinct from its reward -- and evaluates Lagrangian-constrained PPO and TRPO alongside CPO as baselines, scoring every run on return *and* cumulative cost.

The empirical result is unflattering to the methods: constrained deep RL on these tasks does not actually guarantee constraint satisfaction. Algorithms trade violations against return, and the ones that violate least tend to do so by exploring less and therefore returning less.

## Why this matters for INV-093

INV-093's operative sentence is that a competence-refinement mechanism "must be evaluated JOINTLY on competence gain AND non-degradation of harm sensitivity, residue accumulation, and commitment integrity", and that "a single-axis competence metric CANNOT express this constraint, which is the whole reason the panel must stay uncollapsed."

That is, almost word for word, the argument this report makes for constrained RL. The ML safety field arrived independently at the same methodological position for the same reason: once you admit a protected quantity, any comparison that reports one number has silently chosen an exchange rate between the protected quantity and performance, and has thereby made the safety question unaskable. Safety Gym is what that position looks like when instrumented -- separate accumulators, separate logging, joint reporting, no aggregate score.

I want to be careful about what this entry is claiming, because it is not what the other four claim. This is a *methodology precedent*, not evidence that competence refinement degrades harm sensitivity. It tells REE how to measure INV-093's panel; it does not tell us that the panel will move. That is why it sits at 0.60 while the empirical entries sit near 0.80, and I would rather record the distinction than let a well-known citation borrow confidence from its reputation.

The empirical half does contribute one thing the other entries do not, and it cuts against a lazy reading of INV-093. Constrained methods here reduce violations partly by becoming timid, and their return falls accordingly. So the acceptance shape needs a competence *floor* as well as a harm ceiling, or the invariant is trivially satisfiable by a refinement mechanism that refines nothing. INV-093's wording -- "improvement in competence AND non-degradation of harm sensitivity" -- already has the floor in it, but the floor is doing more work than it looks like it is doing, and this is the evidence for why.

## Limitations and caveats

The constraint costs are hand-placed environment hazards. Bump into a region, incur a unit of cost. They were chosen to make a benchmark tractable, not because they represent anything independently valuable, and this is the deep disanalogy with INV-093. REE's protected panel is motivated in the other direction: harm sensitivity, residue accumulation and commitment integrity are properties we care about first and would need to build accumulators for second. The hard part of adopting this template is defining those three instruments, and the report offers no help with it -- it hands us the shape of the answer while the whole difficulty lives in the part it assumes given.

It is also an unrefereed technical report, now several years behind the constrained-RL literature it started, and its own baselines are the weakest part of it. I am citing it for the framing, which has held up, not for the algorithms, which have been superseded.

## Confidence reasoning

Source quality 0.65: influential, openly released with working code, and effectively field-standard, but not peer-reviewed and empirically superseded. Mapping fidelity 0.70 -- the methodological principle is close to a restatement of INV-093's uncollapsed-panel requirement, while the specific cost formulation transfers poorly. Transfer risk 0.45, the highest in this directory, because engineered navigation hazards standing in for an ethical panel is a substantial abstraction and I do not want the number to hide that. Aggregate 0.60, deliberately below the arithmetic the components alone would suggest, because the entry evidences the claim's *acceptance shape* rather than the claim.
