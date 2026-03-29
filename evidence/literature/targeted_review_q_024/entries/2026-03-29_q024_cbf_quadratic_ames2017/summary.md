# Ames et al. (2017) — Control Barrier Function Based Quadratic Programs for Safety Critical Systems

## What the paper did

Ames, Xu, Grizzle, and Tabuada developed a formal methodology for synthesizing controllers that simultaneously guarantee safety (forward invariance of a safe set) and performance (stability). Safety is specified by a Control Barrier Function (CBF) h: the safe set C is the superlevel set {x : h(x) >= 0}. A CBF must satisfy a Lyapunov-like condition on its time derivative along system trajectories. A Zero Barrier Function (ZBF) additionally makes C asymptotically stable. Safety and stability constraints are unified in a real-time Quadratic Program (QP) that selects the nearest-to-nominal control input satisfying both the CBF and Control Lyapunov Function (CLF) conditions simultaneously.

## Key findings

If a CBF exists for a given safe set and system dynamics, forward invariance of the safe set is formally certified. The QP formulation allows safety constraints to override performance objectives only when necessary -- a "minimally invasive" safety filter. The connection to attractor theory is direct: a ZBF makes the safe set C an asymptotically stable invariant set -- meaning trajectories starting outside C converge to it, and trajectories starting inside never leave. This unifies reachability (convergence into C) and safety (remaining in C) in a single Lyapunov-based framework.

## REE translation

Q-024 asks for the correct formal representation for threshold/feedback processes bounded by {x...x_n} reliably reaching emergent state q. The paper maps directly onto Q-024's prescriptive variant: the CBF h certifies that the system's trajectory cannot violate the ethical constraint boundary (harm exceeding threshold). The ZBF extension certifies that the system actively converges to the ethical set rather than merely staying within it once entered. For Q-024's three variants: the CBF condition is the prescriptive certificate; the geometry of the safe set C is the descriptive representation; and diagnostically, checking whether h(x) < 0 along a trajectory identifies a counterfactual deviation from the ethical bound (directly relevant to MECH-127's counterfactual structure).

The QP formulation is particularly relevant because REE's architecture involves competing objectives: E3 optimizes trajectories for goal achievement, while harm constraints should override when necessary. The CBF-CLF-QP framework formalizes exactly this arbitration -- at each timestep, the nearest-to-goal policy that satisfies the harm barrier function constraint is selected.

## Limitations and honest caveats

CBFs as formalized here require a continuously differentiable h and deterministic, control-affine dynamics. REE's dynamics are neither: the policy network introduces non-differentiability, the system is stochastic, and the harm constraint may not be expressible as a single smooth superlevel set. Extending CBFs to stochastic systems is an active area (stochastic CBFs, probabilistic safety certificates) not covered in this foundational paper. MECH-127's counterfactual utility -- where harm depends on what would have happened absent the agent's action -- is not a function of the current state alone and thus cannot be straightforwardly encoded in a standard CBF condition.

There is also a practical concern noted in the literature: CBF-based controllers can introduce spurious attractors (locally stable states that were not the intended equilibrium), which is especially problematic when the CBF is learned or approximated rather than analytically specified.

## Confidence reasoning

IEEE TAC 2017 -- a foundational paper that has become the standard reference for safety-critical control. Source quality is very high. The mapping from CBF to REE's prescriptive variant is direct and clean at the conceptual level. The implementation gap is real: smooth safe set assumption, deterministic dynamics, and the counterfactual utility complication all require extensions beyond this paper. Overall confidence 0.73 -- the CBF framework is the right formal vocabulary for Q-024's prescriptive variant, with the caveat that REE's specifics (stochastic, learned, counterfactual) require further technical work to instantiate the certificate.
