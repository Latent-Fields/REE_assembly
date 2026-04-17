# Invariant Types: Universal vs Emergent

**Status:** architecture doc, 2026-04-17
**Triggering claim:** INV-012 (responsibility arises through commitment) depending on SD-026 (prospective precision template write channel).

---

## The Distinction

The REE claim registry distinguishes two kinds of invariant:

- **Universal invariants** hold regardless of the substrate. They can be stated using only information-theoretic, thermodynamic, decision-theoretic, or logical vocabulary, and would remain defensible under a substantially different E1/E2/E3 implementation.
- **Emergent invariants** are only well-formed given a specific substrate design. They reference representations or functional roles that exist because of a particular SD/ARC choice. Retract that substrate and the invariant's *subject* becomes ill-defined, not merely unevidenced.

A third value, **grey_zone**, marks invariants where the classification is non-obvious and awaits per-invariant governance review. This is a legitimate outcome of the audit, not a fallback.

---

## Why It Matters

Before this distinction, the registry treated all invariants as substrate-independent. This was wrong in two ways:

1. **Silent fragility.** An emergent invariant whose substrate is demoted or redesigned should enter a "re-derivation required" state. Without the distinction, nothing in the pipeline marks this.
2. **Category error.** Some invariants survive any reasonable design of the system (conservation-style constraints). Others only become stateable once we commit to a particular architecture (e.g., anything referencing z_goal, z_world, residue, commitment boundaries). Treating them identically overstates the robustness of the emergent ones and understates the generality of the universal ones.

---

## Physics Analogy

**Conservation of energy** is universal. No theory of matter is required to state it. Replacing Newtonian mechanics with general relativity or quantum field theory does not threaten the invariant — the derivation changes but the claim survives.

**Conservation of electric charge** is emergent on electromagnetic theory. The invariant requires a substrate that defines "charge" to be well-formed. If we replaced Maxwell's theory with one whose ontology had no charge-carrier analogue, charge conservation would not be "falsified" — it would become un-stateable. The invariant rides on the substrate that gives it content.

Both are genuine invariants. Both are legitimate. They have different failure modes.

---

## The Worked Example: INV-012 on SD-026

INV-012 states: "Responsibility arises through commitment, not prediction alone."

For this invariant to have ethical content, "commitment" must refer to something distinct from "whatever was already conditioned." If all attention is reflexive or residue-driven, then the system cannot *choose* to attend — it only tracks what history biases it toward — and "commitment" collapses into "the system executed what its prior made likely." That is not responsibility in any meaningful sense.

SD-026 (prospective precision template write channel, DAN analogue) provides the mechanism by which endogenous goal-derived templates can write precision biases into E1/E2 before a decision is made. This is what makes deliberate attention distinct from residue-driven attention. Without SD-026 (or an equivalent successor substrate), the subject of INV-012 — "commitment" as a load-bearing ethical concept — does not exist as a coherent object in the architecture.

Hence INV-012 is **emergent** on SD-026. The substrate does not *evidence* INV-012; it *gives INV-012 its subject matter*. Different logical relation, different governance implications.

---

## Classification Criteria

**Universal** if the invariant would still be stateable and defensible:
- under a substantially different E1/E2/E3 substrate,
- without committing to any specific SD-xxx or ARC-xxx,
- using only information-theoretic, thermodynamic, decision-theoretic, or logical vocabulary.

**Emergent** if any of the following is true:
- the invariant references a representation that only exists because a specific SD introduced it (e.g., z_world, z_harm, z_goal, commitment boundary, residue field),
- the invariant references a functional role that is only well-formed given a substrate design (e.g., "prospective attention", "commitment"),
- retracting a specific SD or ARC would leave the invariant's subject ill-defined.

**Grey zone** if:
- the invariant could be restated in universal terms but as currently written references REE-specific machinery (candidate: re-write or classify emergent),
- the substrate it appears to reference has ambiguous status itself,
- the auditor is not confident in either direction.

Grey zones are resolved in dedicated per-invariant governance sessions, with full context. Better to mark 15 entries honestly than to force-classify all of them and corrupt the registry.

---

## Schema

All invariants carry an `invariant_type` field. Emergent invariants additionally carry `emergent_from` listing the substrate designs that give them content.

```yaml
- id: INV-xxx
  claim_type: invariant
  invariant_type: universal          # or: emergent | grey_zone
  emergent_from: []                  # required and non-empty when invariant_type: emergent
  candidate_emergent_from: []        # optional, grey_zone only
  pending_substrate_reconfirmation: false   # flag, see "Governance Cycle" below
  depends_on: [...]
```

Rules enforced by `scripts/validate_claims.py`:

- `invariant_type` is mandatory on all invariants.
- `invariant_type: emergent` requires non-empty `emergent_from`.
- `emergent_from` must be a subset of `depends_on`.
- `emergent_from` must be absent or empty on `universal` invariants.
- `grey_zone` entries are permissive — they pass validation regardless of `emergent_from` content.

---

## Governance Cycle

The load-bearing question this schema lets us answer: **what happens to an emergent invariant when its substrate-of-origin is demoted, retracted, or substantially redesigned?**

### Rule 1: Substrate demoted or retracted

When an SD/ARC listed in some invariant's `emergent_from` moves below `active` status (demoted to `candidate`, retracted, superseded), all dependent emergent invariants get `pending_substrate_reconfirmation: true`.

This flag does not demote the invariant. It marks that the invariant cannot be cited as supporting evidence for new claims until governance explicitly reconfirms or reclassifies it. The flag is orthogonal to status — an invariant can be `active` and `pending_substrate_reconfirmation` simultaneously.

### Rule 2: Substrate replaced by successor

When a substrate is replaced (e.g., SD-026 superseded by SD-026b), governance must explicitly choose per dependent invariant:

- **transfer** — update `emergent_from` to the successor substrate, claim remains active,
- **re-derive** — demote invariant to `candidate`, require fresh evidence on the new substrate,
- **retract** — withdraw the invariant because the new substrate does not support its well-formedness.

### Rule 3: Substrate promoted

When a substrate rises in status (candidate → provisional → active), dependent emergent invariants do **not** auto-promote. Invariant confidence is scored independently. The promotion only removes the `pending_substrate_reconfirmation` flag from dependents that had one.

Rationale: an invariant and its substrate can fail independently — a substrate can be the correct design while the invariant claim about it is wrong, and vice versa. Coupling their promotion would contaminate both evidence records.

### Rule 4: Universal invariants

Universal invariants are unaffected by substrate changes. No `emergent_from`, no coupling, no flag.

---

## What This Is Not

- Not a change to how evidence is weighted or how confidence is scored.
- Not a change to how substrates (SDs) themselves are promoted.
- Not a change to the V3-pending gate.
- Not a claim that universal invariants are more valuable than emergent ones. Both are legitimate; they have different failure modes and different dependencies.

The change is structural: make the registry represent a relationship that already exists in the architecture (some invariants rest on substrate choices, some don't) and make governance act on it when substrates change.

---

## Related: `derived_prediction` claim_type

Introduced 2026-04-17 as part of Session C batch grey-zone resolution.

Some entries previously carried as `claim_type: invariant` are not invariants of
the REE architecture itself — they are predictions about a target domain (human
psychiatric syndromes, clinical pharmacology, dream phenomenology, cognitive
pathology progression) that hold **only conditional on REE being a correct model
of that target domain**. That conditional is a separate commitment from the
architectural invariants, with different failure modes and different governance
implications.

- A universal invariant holds in any agent.
- An emergent invariant holds in any agent with the relevant substrates.
- A `derived_prediction` holds iff (a) the architecture's invariants hold **and**
  (b) REE correctly models the domain the prediction targets. Falsification of a
  `derived_prediction` can therefore reflect either a wrong architectural claim or
  a wrong domain-modelling assumption — these must be distinguished during
  investigation.

`derived_prediction` entries do **not** carry `invariant_type` or `emergent_from`
fields (those are meaningful only on invariants). They may carry a free-form
`prediction_domain` note in `notes` or as a dedicated field. Validator ignores
`derived_prediction` entries (no invariant-schema checks apply). Governance
moves these entries out of the invariants section of any reference doc into a
predictions section or dedicated `docs/predictions/` file when convenient; the
location change is not required for the type change to take effect.

First reclassifications under this type: INV-047, INV-048, INV-061, INV-062
(Session C batch, 2026-04-17). The 'INV-' ID prefix is retained for provenance
but is no longer semantic — these entries are predictions, not invariants.

---

## References

- Planning doc: `docs/thoughts/2026-04-17_invariant_types_governance.md`
- Triggering commits: dcb44d478 (SD-026 and INV-012 edit), 47227c255 (planning doc)
- Audit registry (populated by Session B): `docs/governance/invariant_classification_audit.md`
