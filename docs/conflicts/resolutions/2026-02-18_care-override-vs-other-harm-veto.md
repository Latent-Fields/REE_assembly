# Resolution: Care Override vs Other-Harm Veto

## Conflict Reference(s)

- `docs/conflicts/care_override_vs_other_harm_veto.md`

## Resolution Decision

REE adopts a bounded override policy. Catastrophic high-certainty irreversible other-harm remains a hard veto.
Care-investment weighting can influence ranking and can override only in non-catastrophic regimes when necessity,
imminence, proportionality, and explainability gates are satisfied, followed by mandatory post-commit accountability
logging. This preserves third-party protection while preventing paralysis in constrained tradeoff cases.

## Claims Affected (IDs)

- Q-009
- MECH-036
- MECH-051
- MECH-052
- IMPL-017

## Superseded Claims

- None. Conflict resolved by narrowing policy scope and explicitly constraining override legality; Q-009 is retained as
  a legacy question ID.

## Canonical Docs Updated (paths)

- `docs/architecture/social.md`
- `docs/conflicts/care_override_vs_other_harm_veto.md`
- `docs/conflicts/README.md`
- `docs/claims/claims.yaml`
- `docs/claims/claim_index.md`

## Open Follow-Ups

- Keep threshold calibration and false-positive/false-negative tradeoffs under social-control tuning work, not as a
  binary architecture conflict.
