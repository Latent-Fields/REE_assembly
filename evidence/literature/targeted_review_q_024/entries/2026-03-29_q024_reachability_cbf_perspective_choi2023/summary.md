# Choi et al. (2023) — A Forward Reachability Perspective on Control Barrier Functions

## What the paper did

Choi, Lee, Li, How, Sreenath, Herbert, and Tomlin investigated the relationship between two major formal tools for safety analysis: Hamilton-Jacobi (HJ) reachability analysis (which computes sets of states a system can reach) and Control Barrier Functions (which certify that a system stays within a safe set). They introduced the Forward Reachable Tube (FRT) -- the set of states that every trajectory starting from an initial set must pass through -- and proved it is a robust control invariant set when its boundary is smooth. They showed that valid CBFs function as forward reachability value functions, and that discount factors in the HJ differential game equation naturally generate barrier constraints. They also developed a method for learning neural CBFs that characterize control invariant supersets of the FRT.

## Key findings

The central unification is that reachability (where does the system go?) and invariance (where does the system stay?) are dual perspectives on the same formal structure. The FRT characterizes inevitable reachability -- not just what the system *can* reach, but what it *must* reach from a given initial condition under all admissible controls. The CBF condition then certifies the converse: that the system's trajectory is bounded within the region from which the target state is reachable. Discount factors in the HJ equation introduce a natural "decay" in the severity of constraint violations over time, which corresponds to temporal discounting in harm assessment.

## REE translation

For Q-024, this paper provides the link between the descriptive and prescriptive variants. The descriptive variant asks: what is the attractor that threshold/feedback processes converge to? The FRT answers this: given REE's initial policy state and its dynamics, the FRT characterizes which future states are inevitable. The prescriptive variant asks: can we certify that REE's trajectory reaches state q (the ethical equilibrium)? The CBF-as-reachability-value-function answers this: a CBF for the region containing q certifies forward invariance and reachability.

The discount factor connection is particularly interesting for REE. MECH-127's counterfactual utility structure discounts harm that would not have occurred without the agent's action -- a form of temporal-causal discounting. Choi et al.'s observation that discount factors naturally generate barrier constraints suggests a possible formal connection: MECH-127's counterfactual discount could be formalized as a discounted HJ reachability problem, potentially generating CBF conditions that remain valid despite the counterfactual structure that breaks the standard framework.

For the diagnostic variant (detecting counterfactual deviations): this requires backward reachability analysis -- characterizing which initial states would have led to a different outcome. The paper notes that backward reachability is underdeveloped relative to forward reachability, and flags this as a limitation. This is precisely the gap that makes the diagnostic variant of Q-024 the hardest to formalize.

## Limitations and honest caveats

This is a preprint (arXiv 2023) and has not undergone full peer review; the neural CBF learning method is relatively new. The FRT characterization requires smooth boundary conditions and is proved for deterministic dynamics; stochastic extension requires separate technical machinery. The backward reachability needed for the diagnostic variant is explicitly flagged as less developed. The connection to MECH-127 counterfactual utility and discounted HJ reachability is speculative at this stage -- a research direction, not an established result.

## Confidence reasoning

Strong research group, technically sound preprint, directly addresses the reachability-invariance unification that Q-024 needs. Source quality is slightly lower than a peer-reviewed paper. Mapping fidelity is moderate because the connection from the formal FRT structure to REE's specific harm-bounding problem requires several additional steps. Overall confidence 0.67 -- this paper fills the gap between the descriptive and prescriptive variants and points at (but does not solve) the diagnostic variant's backward reachability requirement.
