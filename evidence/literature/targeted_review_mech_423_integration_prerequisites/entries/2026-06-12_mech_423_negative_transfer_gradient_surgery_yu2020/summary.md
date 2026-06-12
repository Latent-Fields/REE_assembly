# Yu et al. (2020), PCGrad — negative transfer is real, and the gradient-cosine that detects it is the readiness metric

**Claim grounded:** MECH-423 (cross-model super-additivity) — readiness condition R1 (the shared latent must do genuine, non-destructive cross-module work) and the negative-transfer failure mode.
**Direction:** mixed. **Confidence:** 0.70.

## What the paper did

"Gradient Surgery for Multi-Task Learning" diagnoses why shared-representation multi-task models sometimes train poorly. The mechanism is *conflicting gradients*: two tasks' gradients on the shared parameters conflict when they point away from each other, formally when their cosine similarity is negative. The authors show this conflict is detrimental specifically when three things coincide — the "tragic triad": (a) conflicting gradients, (b) high positive curvature in the loss landscape, and (c) a large difference in the gradients' magnitudes. Under that combination, the shared optimisation step helps one task at the expense of another and the multi-task model underperforms separate single-task models — *negative transfer*. Their fix, PCGrad, projects each task's gradient onto the normal plane of any gradient it conflicts with, removing the destructive component and measurably reducing negative transfer on vision benchmarks and MT10/MT50 robotic manipulation.

## Why it speaks to MECH-423 — and why it is the most operationally useful entry

This is the paper that turns the readiness precondition from a slogan into an instrument. MECH-423's what_would_answer demands that "the shared latent carries non-zero cross-module gradient (measured)" before the test means anything. Yu et al. supply the exact measurable quantity: the *cosine similarity between the per-module gradients on the shared latent*. That gives the readiness gate a concrete, pre-registerable, two-sided form:

- **Coupling must be non-zero.** If the per-module gradients on the shared L-space latent are orthogonal or the shared-latent gradient norm is ~0, the modules are not actually integrated — the integrated arm equals the isolated arm by construction. Degenerate; route substrate_not_ready.
- **Coupling must not be net-conflicting.** If the mean inter-module gradient cosine is net-negative, the system is in the negative-transfer regime. A sub-additive result there is the *expected* consequence of gradient conflict, not a refutation of super-additivity-when-aligned. The gate should detect net-conflict and route substrate_not_ready / re-scope rather than record a FAIL.

That is the headline deliverable of this lit-pull: the readiness metric is **mean per-module gradient cosine on the shared latent**, with thresholds (non-zero magnitude; cosine not net-negative) that must be calibrated on REE's own substrate.

The entry is **mixed** because its primary content is the *failure* mode: a shared representation is not automatically super-additive. It can be sub-additive purely by gradient conflict. That cuts both ways for MECH-423 — it warns that a naive integrated arm can lose, and it explains exactly when that loss is uninformative about the claim.

## Limitations and mapping caveats

PCGrad's analysis is for supervised and reinforcement multi-task networks; REE's E1/E2/object-spine coupling is a generative-predictive setting. The gradient-cosine readiness metric transfers in *form*, but the numeric thresholds (the non-zero floor, any required positive margin) are design choices to be set on REE's substrate, not values the paper hands over. And the paper studies how to *fix* conflict, not a super-additivity benchmark — it is a tool for the readiness gate, not a test of the claim.

## Confidence reasoning

Source quality 0.82 (a widely-adopted NeurIPS method). Mapping fidelity 0.72 — the metric maps directly, the threshold needs REE calibration. Overall 0.70, mixed, reflecting that this is chiefly evidence of the negative-transfer failure mode while simultaneously being the most actionable entry for building the readiness gate.
