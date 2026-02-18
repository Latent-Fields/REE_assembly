# Conflict: Care Override vs Other-Harm Veto

## Conflicting Claim IDs

- Q-009
- MECH-036
- MECH-051
- MECH-052

## Verbatim Excerpts (with preserved sources)

From `docs/architecture/social.md`:
> "Other-harm should trigger a hard veto only under high-certainty, catastrophic, or irreversible outcomes."

From `docs/architecture/social.md`:
> "Should high care-investment weights ever override other-harm veto thresholds ... ?"

## Why They Conflict (or What Would Reconcile Them)

MECH-036 sets a catastrophic-veto framing, while Q-009 asks whether care persistence and relational weights can
override that veto in edge cases to avoid paralysis. This creates an unresolved policy boundary between third-party
protection and care-driven action under constrained alternatives.

## Reconciliation Question

What formal threshold policy should govern overrides: never override catastrophic veto, or allow override only under
strict necessity/proportionality/imminence constraints with explicit accountability logging?

---

## Status

Resolved on 2026-02-18.

Resolution summary:
- Catastrophic high-certainty irreversible other-harm remains a hard veto.
- Care-driven overrides are permitted only for non-catastrophic cases under necessity, imminence, proportionality,
  and explainability gates, with mandatory post-commit accountability logging.
- This is a bounded override policy, not an unrestricted care override.

Resolution note:
- `docs/conflicts/resolutions/2026-02-18_care-override-vs-other-harm-veto.md`
