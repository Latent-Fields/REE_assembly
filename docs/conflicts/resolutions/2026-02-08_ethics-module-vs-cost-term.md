# Resolution: No Ethics Module vs Explicit Ethical Cost Term

## Conflict Reference(s)

- `docs/conflicts/ethics_module_vs_cost_term.md`

## Resolution Decision

E3 does not require a standalone ethical cost term. Ethical consequence is implemented through residue geometry,
mirror modelling, control-plane gating, hippocampal replay/path memory, and commitment-gated learning. Legacy
notations that include an explicit \(M\) term are retained as historical framing, not architectural requirement.

## Claims Affected (IDs)

- INV-001
- ARC-003
- ARC-012
- IMPL-017

## Superseded Claims

- None. The conflict was resolved by clarifying interpretation and canonical wording.

## Canonical Docs Updated (paths)

- `docs/architecture/e3.md`
- `docs/conflicts/ethics_module_vs_cost_term.md`
- `docs/claims/claims.yaml`
- `docs/claims/claim_index.md`

## Open Follow-Ups

- Confirm that legacy references to \(M\) remain clearly labeled as non-required in all architecture docs that mention
  trajectory scoring.
