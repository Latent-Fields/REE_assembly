# Cooper 2016 -- Fleeing to refuge: escape decisions in the race for life

**Source**: Cooper WE (2016). *Journal of Theoretical Biology* 406:129-136. [DOI 10.1016/j.jtbi.2016.06.023](https://doi.org/10.1016/j.jtbi.2016.06.023). PMID 27343624.

## What the paper did

This paper extends the classical economic theory of escape (Ydenberg & Dill 1986's break-even flight-initiation-distance model, and Cooper & Frederick's 2007 optimality refinement) to handle multiple risk factors JOINTLY rather than one at a time. The core idea: escape from a predator is not just a function of how dangerous the predator is, but a literal race to reach refuge before the predator arrives — so the model treats flight-initiation distance (FID, the predator-prey distance at which the prey begins to flee) as a function of the prey's distance to refuge, predator attack speed, and the angle between the prey's and predator's respective paths to that refuge.

## Key findings relevant to the claim

FID increases as distance to refuge increases, as predator attack speed increases, and as the prey is forced to flee more directly TOWARD (rather than away from) the predator to reach safety. The paper's most specific, testable prediction is that FID increases SIGMOIDALLY — not linearly — as the angle between predator and prey paths to refuge increases. The overall message: escapability is not reducible to raw predation risk; it is jointly determined by geometric and kinematic variables that must be evaluated alongside danger level, and the two interact rather than being interchangeable or substitutable.

## How this translates to REE

This paper grounds the design question's "which features beyond raw magnitude matter" half for the specific feature of ESCAPABILITY. Its central lesson for SD-hazard-aware-policy-decomposition is architectural: a harm-valence-weighted selection step built on `z_harm_a`/BLA `threat_scale` alone — a pure danger-magnitude signal — is incomplete relative to what this model shows the biological target actually depends on. A fuller implementation should incorporate some REE-side analog of "how likely is this candidate re-tiling to actually reach a safe or low-harm completion," plausibly derivable from something like z_world reachability or the tile's own predicted trajectory outcome, evaluated ALONGSIDE raw harm magnitude rather than as a substitute for it. Separately, the paper's specific sigmoidal (not linear) functional form for one escapability variable is independent evidence — arrived at via an entirely different route (ecological optimality modeling rather than neuroscience) — against a purely linear graded-weighting design, reinforcing this pull's SYNTHESIS.md recommendation for a non-linear, regime-sensitive functional form.

## Limitations and caveats

This is a theoretical/geometric model, not a neural-circuit or REE-specific study — its underlying empirical support comes from ecological flight-initiation-distance literature (largely lizards, birds, and small mammals), and its escapability variables (literal distance to refuge, relative speed, path angle) are 2D spatial-navigation quantities with no direct REE equivalent, since REE's redecomposition step operates over abstract policy tiles rather than literal geometry. The transfer to REE is conceptual — "escapability is a distinct, jointly-necessary, non-linearly-related feature" — not a specific functional form that could be imported verbatim.

## Confidence reasoning

Well-regarded theoretical-biology model extending a canonical, extensively-cited framework (Ydenberg & Dill 1986), with broad support in the empirical ecology literature it builds on. Confidence 0.74: it strongly and independently supports the design question's escapability and non-linearity points, but mapping fidelity is capped at moderate because its concrete variables have no literal REE analog — this is the least neuroscience-grounded, and therefore highest-transfer-risk, entry in the pull.
