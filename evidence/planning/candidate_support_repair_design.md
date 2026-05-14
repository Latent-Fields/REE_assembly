# Candidate-Support Repair Design

Date: 2026-05-14

Context: V3-EXQ-563 showed that forced score bias could not move behavior when
the first-action class was absent from the candidate set. V3-EXQ-563a showed
that E3 uses the bias when scaffolded candidates provide a real support
surface. The next repair therefore targets proposal support, not another
motivation drive.

## Literature Pull

Focused review:
`evidence/literature/targeted_review_candidate_support_preserving_cem/`

Design readout:

- Cross-Entropy Method elite refit can collapse support because it explicitly
  concentrates probability mass on low-cost elites.
- MPC/CEM variants support conservative proposal-side repairs, but broad
  mixture-proposal redesign is not needed for this diagnostic step.
- Entropy-regularized MPC and maximum-entropy RL are useful analogies for
  measuring proposal support and bias magnitude, not dependencies to import.
- Gumbel-Softmax and categorical-first-action sampling are later options if a
  default-off support-preserving CEM patch fails to touch the live proposal
  path.

## Implementation Sequence

1. Expose candidate-support diagnostics on `HippocampalModule`.
2. Keep `use_action_class_scaffold_candidates=False` by default as a diagnostic
   support floor.
3. Add `use_support_preserving_cem=False` as a separate experimental flag.
4. Use `candidate_support_preflight()` to mark behavioural interpretation
   `NOT_RUN: candidate_support_collapse` when support is absent.
5. Run V3-EXQ-563b over normal CEM, scaffold support, support-preserving CEM,
   and weak forced-bias arms.

## Interpretation Rule

V3-EXQ-563a confirms that E3 can use score bias when candidate support exists.
It does not solve behavioural agency. Natural goal, curiosity, tonic-vigor, and
rule-bias tests remain blocked until the live proposer supplies measurable
first-action alternatives and the effective bias magnitude is calibrated.
