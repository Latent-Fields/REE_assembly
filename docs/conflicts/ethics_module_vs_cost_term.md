# Conflict: No Ethics Module vs Explicit Ethical Cost Term

## Conflicting Claim IDs

- INV-001
- ARC-003

## Verbatim Excerpts (with preserved sources)

From `docs/processed/legacy_tree/README.md`:
> "REE does not add an explicit moral objective, moral reward, or ethical scoring function on top of action selection."

From `docs/processed/legacy_tree/REE_CORE.md`:
> "Each candidate trajectory is scored using: a reality constraint, an ethical cost M, a residue field R."

## Why They Conflict (or What Would Reconcile Them)

INV-001 rejects an explicit moral scoring layer on top of action selection, while ARC-003 (via the E3 scoring description) includes an explicit ethical cost term in trajectory scoring. These can be reconciled if M is interpreted as an intrinsic prediction of self/other degradation that falls out of shared generative dynamics, not as a separate moral objective or module.

## Reconciliation Question

Is M a descriptive prediction of harm within the shared generative model (and therefore not a separate ethics module), or does it function as an explicit moral scoring layer that violates INV-001?

---

## Resolution (2026-02-08)

Decision: E3 does not require any explicit ethics module or ethical cost term. Ethical consequence is handled via residue, mirror modelling, control-plane gating, hippocampal systems, and commitment-gated learning.
Resolution note: `docs/conflicts/resolutions/2026-02-08_ethics-module-vs-cost-term.md`

Resulting updates:
- Canonical E3 documentation now states that explicit ethical cost terms are legacy formulations.
- INV-001 remains in force without exception.
