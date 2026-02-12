# Conflict: Rollout Entropy Floor vs Residue Persistence

## Conflicting Claim IDs

- Q-011
- INV-006
- ARC-011
- MECH-056

## Verbatim Excerpts (with preserved sources)

From `docs/architecture/hippocampal_systems.md`:
> "Should REE enforce a non-zero rollout-diversity floor to prevent pathological trajectory collapse?"

From `docs/invariants.md`:
> "Moral residue cannot be erased, only integrated."

## Why They Conflict (or What Would Reconcile Them)

Q-011 proposes forcing exploration diversity under repeated harm, while INV-006 and ARC-011 require preserving
residue and genuine harm structure. The tension is whether entropy-floor interventions can restore option space without
implicitly flattening residue or bypassing safety gating.

## Reconciliation Question

Where should diversity restoration act (sampling, control-plane temperature, offline replay) so trajectory space
reopens while residue remains intact and harm-relevant constraints stay authoritative?

---

## Status

Open. No resolution note recorded yet.
