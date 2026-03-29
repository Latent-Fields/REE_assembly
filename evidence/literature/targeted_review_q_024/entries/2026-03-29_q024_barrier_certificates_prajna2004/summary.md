# Prajna & Jadbabaie (2004) — Safety Verification of Hybrid Systems Using Barrier Certificates

## What the paper did

Prajna and Jadbabaie proposed barrier certificates as a Lyapunov-inspired framework for proving the safety of hybrid systems. A barrier certificate is a real-valued function of the system state whose zero-level set separates the unsafe region from all possible trajectories starting from a given initial set. The key insight is that if such a function exists -- satisfying three conditions involving the initial set, the unsafe set, and the time derivative along system dynamics -- then the system is provably safe over an infinite time horizon, without ever explicitly computing the reachable set. The construction of barrier certificates is formulated as a sum-of-squares (SOS) programming problem, enabling automated computation for polynomial systems.

## Key findings

Three advantages distinguish barrier certificates from reachable set computation: they apply over infinite time horizons, they handle nonlinear dynamics directly, and they are robust to uncertain inputs or parameters. The barrier certificate approach is complementary to Lyapunov stability theory: where Lyapunov certificates prove that trajectories *converge* to a target (stability), barrier certificates prove that trajectories *avoid* a forbidden region (safety). Together, they provide the formal vocabulary for both convergence and bounding guarantees simultaneously.

## REE translation

For Q-024, Prajna and Jadbabaie provide the verification-focused formal representation that complements Ames et al.'s synthesis-focused CBF framework. The distinction matters for Q-024's three variants. A CBF (Ames 2017) is used to *design* a controller that maintains safety. A barrier certificate (Prajna and Jadbabaie) is used to *verify* that an existing system is safe. For REE, the prescriptive variant involves designing training or policy constraints to ensure bounded harm convergence -- this is CBF territory. The diagnostic variant involves checking whether a specific trajectory (or counterfactual trajectory) violated the harm bound -- this is barrier certificate territory.

The hybrid system applicability is especially relevant for REE. REE's architecture has a commit boundary: pre-commit dynamics (simulation mode, reversible) differ from post-commit dynamics (realized mode, irreversible). Prajna and Jadbabaie's framework is designed for exactly this kind of hybrid system with discrete mode transitions. A barrier certificate could be separately defined for each mode, with conditions at the mode transition (commit boundary) ensuring that transitioning from simulation to committed action does not violate the harm certificate.

For Q-024's question about whether all three variants (descriptive, prescriptive, diagnostic) are needed: this paper argues implicitly yes. Barrier certificates are verification tools (diagnostic, post-hoc); they tell you that a system is safe but do not tell you what the attractor looks like (descriptive) or how to ensure convergence (prescriptive). Each variant serves a distinct purpose in the formal characterization of REE's ethical trajectory constraint.

## Limitations and honest caveats

The SOS programming approach requires polynomial dynamics. REE's neural network policy and forward model are not polynomial -- extension to neural barrier certificates (a more recent line of work, not covered here) provides approximate certificates but without completeness guarantees. Neural barrier certificates are learned from data and may fail to detect unsafe regions that are underrepresented in training trajectories. The framework verifies given systems, not learning systems; REE's policies change during training, requiring certificates to be updated or checked online. MECH-127's counterfactual utility -- harm that depends on unobserved alternative trajectories -- cannot be expressed as a deterministic function of the current state, complicating the barrier certificate condition.

## Confidence reasoning

HSCC 2004, highly cited, formally complete for polynomial hybrid systems. The vocabulary (barrier certificate, zero-level set separation, hybrid system mode transitions) maps cleanly onto Q-024's formal requirements. The polynomial dynamics assumption is the main limitation for REE. The verification-vs-synthesis distinction from Ames is important and needed for Q-024's diagnostic variant. Overall confidence 0.70 -- the framework is directly applicable conceptually, with a known technical gap (non-polynomial dynamics) that the neural barrier certificate literature addresses partially but incompletely.
