---
title: "Evidence Defeaters (GOV-DEFEAT-1)"
parent: "Foundations & Rationale"
grandparent: Architecture
nav_order: 22
status: candidate
status_asof: 2026-09-25
status_claim: GOV-DEFEAT-1
---

# Evidence Defeaters

**Status:** candidate governance rule, registered 2026-09-25 from
`docs/thoughts/2026-09-24_ree_assembly_as_continuous_scientific_assurance.md`
(intake: `evidence/planning/thought_intake_2026-09-24_ree_assembly_as_continuous_scientific_assurance.md`).

## What a defeater is here

A defeater is a named, specific doubt that, if upheld, removes a result's ability to support the
inference drawn from it. For example: the PASS is vacuous, the consumer was unreachable, the
control was inert, the premise is stale, a D1 result is being narrated as D3.

REE already has the three halves of a defeater system:

- **Kinds:** GOV-CAPCONTRACT-1, GOV-PATHVALID-1, GOV-DRY-1, GOV-CRITBAR-1, GOV-MATCHAUX-1,
  GOV-JURIS-1.
- **Raising channels:** `scripts/governance_flag.py` (`evidence_discrepancy`,
  `contested_disposition`), GOV-APPLY-1, GOV-SUBPATH-1.
- **Resolved forms:** per-edge qualifiers in `claim_evidence.v1.json` (`scoring_excluded`,
  `degeneracy_reason`, `duplicate_of`, `superseded_by_substrate`, `non_contributory`).

## GOV-DEFEAT-1 {#gov-defeat-1}

**Open-defeater rule.** Between raising and resolution, an edge named by an open flag is
**contested**. It keeps its score, but it loses its standing as uncontested support.

- Summary surfaces name the open flag beside the claim, worded "open, unadjudicated", never
  "defeated".
- No promotion, and no "confirmed/established" wording, rests only on contested edges.
- "No open defeaters" must be able to say cannot-determine.

Scoped to counted edges (see the GFLAG-0197 bounding case in the claim notes).

Kill condition: the raw thought's falsifier 4. If the display changes no decision in >= 3
governance cycles, demote.

## Not registered from this thought

Everything else. See the intake's novelty table: interface contracts (ARC-144, 07-31
causal-realisation pilot), execution state (Phase-3 coordinator), hermeticity (Narrow Edits,
idempotency tests, arm-reuse fingerprint), stable identity (2026-09-04 proposal-id allocation),
event sourcing (coordinator logs, status-history plane), vertical-slice assay (GOV-ECOL-1 and
functional-organism P4).
