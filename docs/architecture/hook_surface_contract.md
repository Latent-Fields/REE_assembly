# Cross-Version Hook Surface Contract

**Claim Type:** implementation_note  
**Scope:** Versioned hook interfaces for REE-v2 and later phases  
**Depends On:** IMPL-022, IMPL-023, MECH-061, MECH-062, MECH-063  
**Status:** candidate  
**Claim ID:** IMPL-025
<a id="impl-025"></a>

---

## Purpose

Define a stable hook framework so v2 can expose extension points for v3/v4 without repeated interface churn.

This contract covers:
- hook metadata shape,
- compatibility/deprecation rules,
- tiering across roadmap phases.

---

## Hook Envelope (Required Fields)

Each hook entry must define:

- `hook_id`: immutable ID (`HK-xxx`).
- `hook_name`: concise semantic label.
- `tier`: `v2_required | v3_planned | v4_plus_reserved`.
- `status`: `active | planned | reserved | deprecated`.
- `producer_modules`: modules that emit the hook.
- `consumer_modules`: modules expected to consume it.
- `lifecycle_phase`: when it is emitted (`pre_predict`, `post_predict`, `pre_commit`, `post_commit`, `offline`).
- `payload_contract`: schema/key contract reference.
- `key_fields`: required payload keys.
- `availability`: `always | conditional`.
- `stability`: `stable | experimental | reserved`.

Registry path:
- `docs/architecture/hook_registry.v1.json`

---

## Compatibility Rules

1. Hook IDs are immutable once published.
2. `v2_required` hooks are breaking-change protected in v2.
3. New hooks must be additive; do not repurpose existing `hook_id`.
4. Deprecation requires:
- status change to `deprecated`,
- replacement hook reference,
- one full governance cycle before removal.
5. Payload key removals require major registry version bump (`hook_registry/v2`).

---

## Tier Semantics

- `v2_required`:
  - must exist in v2 qualification and stress lanes.
  - missing hook is a v2 readiness failure.

- `v3_planned`:
  - stubbed in v2 when possible,
  - required for v3 control-completion implementation.

- `v4_plus_reserved`:
  - reserved interface budget for later social/institutional complexity,
  - not required for v2 readiness.

## Bridge Hook Families (v2 Required)

To preserve v3-control completion viability, the v2 hook surface must include bridge families aligned to:

- `MECH-061`: commit-boundary token envelope fields (`commit_id`, `trajectory_id`, timing, TTL, mode snapshot).
- `MECH-062`: tri-loop arbitration traces (`gate_motor`, `gate_cognitive_set`, `gate_motivational`) and conflict resolution records.
- `MECH-063`: orthogonal control-axis telemetry with tonic/phasic decomposition and module readout tags.

These are interface commitments for evidence and routing continuity, not full v3 behavior commitments.

---

## Governance Expectations

- Hook registry updates must be reflected in:
  - `docs/claims/claims.yaml`
  - `docs/claims/claim_index.md`
  - `docs/changelog.md`
- Any hook conflict or ambiguity should be tracked as a claim-linked conflict note.

---

## Related Claims (IDs)

- IMPL-025
- IMPL-023
- IMPL-022
- MECH-061
- MECH-062
- MECH-063
