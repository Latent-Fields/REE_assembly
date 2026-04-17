# Invariant Types and Governance — Planning Doc

**Status:** draft for review
**Date:** 2026-04-17
**Triggering context:** Registering SD-026 forced INV-012 to declare `depends_on: [SD-026]`, making INV-012 the first invariant in the registry that depends on a substrate design rather than standing on purely architecture-independent grounds. The philosophical observation (commit dcb44d478) was that this is not an oddity — it is a general pattern. Invariants of a designed system come in two flavors: those that hold regardless of the system's construction (universal) and those that only become well-formed once specific design choices create the conceptual space in which they can be stated (emergent).

This doc plans the schema, audit, governance-cycle, pipeline, and documentation changes required to make that distinction load-bearing in the registry.

---

## 1. Problem Statement

The current registry treats all invariants identically. This causes two concrete problems:

1. **Silent fragility.** If SD-026 is demoted or retracted, INV-012 does not automatically enter a "re-derivation required" state — the `depends_on` edge exists but no pipeline reads it as load-bearing on the invariant's well-formedness.
2. **Category confusion.** An invariant like INV-009 (some conservation-style claim about the architecture's information flow) is true of any system that instantiates the relevant constraints, regardless of how we build E1/E2/E3. INV-012 (commitment as load-bearing on prospective attention) is only well-formed *given* that prospective attention is a thing the system does — which requires SD-026. Treating these the same overstates the robustness of INV-012 and understates the generality of INV-009.

The physics analogy: conservation of energy is universal (no theory of matter required to state it). Conservation of electric charge is emergent on electromagnetic theory — the invariant requires the substrate that defines "charge" to be well-formed. Both are invariants, but demoting Maxwell would not endanger energy conservation while demoting the charge-carrier ontology *would* force charge conservation to be re-derived in whatever replaces it.

We want the registry to make this distinction explicit and the governance cycle to act on it.

---

## 2. Schema Change

Proposed additions to the `type: invariant` schema in `docs/claims/claims.yaml`:

```yaml
- id: INV-xxx
  type: invariant
  subject: ...
  title: ...
  status: ...
  invariant_type: universal          # or: emergent | grey_zone
  emergent_from: []                  # required when invariant_type: emergent
  candidate_emergent_from: []        # optional when invariant_type: grey_zone
  pending_substrate_reconfirmation: false   # flag, see §4
  depends_on: [...]
```

Rules:
- `invariant_type` is **mandatory** on all invariants. Three values: `universal`, `emergent`, `grey_zone`.
- `grey_zone` means "classification pending governance discussion" — the audit flagged the entry as non-obvious and it awaits a per-invariant session (see §3, Q1 resolution).
- `emergent_from` is **mandatory and non-empty** when `invariant_type: emergent`; **must be empty or omitted** when `universal`; **optional** when `grey_zone` (may be populated as `candidate_emergent_from` for reviewer reference).
- `emergent_from` is a subset of `depends_on` — specifically, the substrate designs that create the conceptual space the invariant lives in. `depends_on` may contain additional entries that are not substrate-of-origin.
- `pending_substrate_reconfirmation` is a boolean flag (not a status value) — see §4 rule 1. Modeled on existing `v3_pending` flag precedent in the registry.

**Validation** (`scripts/validate_claims.py`, new): fail loudly when:
- an invariant lacks `invariant_type`,
- `invariant_type: emergent` has empty `emergent_from`,
- `emergent_from` contains IDs not present in `depends_on`,
- `emergent_from` is set on a `universal` invariant.

`grey_zone` entries pass validation regardless of `emergent_from` content (this is the whole point — they're parked pending review).

---

## 3. Audit Criteria

A classification heuristic for passing over the ~72 existing invariants:

**Universal** if the invariant would still be stateable and defensible:
- under a substantially different E1/E2/E3 substrate,
- without committing to any specific SD-xxx or ARC-xxx,
- using only information-theoretic, thermodynamic, decision-theoretic, or logical vocabulary.

**Emergent** if any of the following is true:
- the invariant references a representation that only exists because a specific SD introduced it (e.g., z_world, z_harm, z_goal, commitment boundary, residue field),
- the invariant references a functional role (e.g., "prospective attention", "commitment") that is only well-formed given a substrate design,
- retracting a specific SD/ARC would leave the invariant's subject ill-defined, not merely unevidenced.

**Grey-zone cases (explicit, not silent):** invariants where classification is non-obvious — e.g., could be restated in universal terms with effort but as written reference REE-specific machinery; or reference machinery whose status is itself ambiguous. These are tagged `invariant_type: grey_zone` with `candidate_emergent_from` populated where useful, and deferred to per-invariant governance sessions (see Q1 resolution below). This is a first-class outcome of the audit, not a fallback — better to mark 15 grey zones honestly than to force-classify all of them and be wrong on 5.

**Candidates likely to be emergent** (hypothesis, not verdict — needs audit):
- INV-012 (commitment/responsibility — confirmed emergent on SD-026)
- INV-034 (goal maintenance necessary for ethical agency — references z_goal)
- INV-037, INV-038 (stored/active distinction, EVR pattern — references vmPFC decomposition)
- INV-043 (if it references residue-field structure)
- INV-049 ("offline phases as mathematical necessity for model-building agents" — borderline; may be universal)

**Candidates likely to be universal:**
- INV-009 (information-flow constraint)
- INV-001–008 (foundational — needs check)
- Any invariant cast in purely decision-theoretic or thermodynamic terms

**Audit mechanics (revised per Q1 resolution):** single pass through all `type: invariant` entries produces an **audit registry** at `docs/governance/invariant_classification_audit.md` (new file). The registry is structured as three sections:

1. **Clear universal** — entries the auditor is confident are universal. One-line rationale each. These get `invariant_type: universal` applied directly.
2. **Clear emergent** — entries the auditor is confident are emergent on a specific substrate. One-line rationale each, with `emergent_from` listed. These get `invariant_type: emergent` and the `emergent_from` field applied directly.
3. **Grey zone** — entries where the audit cannot confidently classify. Each gets:
   - a short description of why it is ambiguous,
   - candidate classifications (e.g., "emergent on SD-xxx" or "universal if re-stated as ..."),
   - a self-contained prompt for a follow-up session to resolve it.
   These get `invariant_type: grey_zone` in claims.yaml until resolved.

This keeps the audit pass tight (bulk classification on the clear cases) and isolates judgment calls (grey zones handled with full context in dedicated sessions). Expected split: roughly 50–60 clear / 10–20 grey out of ~72.

---

## 4. Governance-Cycle Rule

The load-bearing question this change answers: **what happens to an emergent invariant when its substrate-of-origin is demoted, retracted, or substantially redesigned?**

Proposed rule (add to governance pipeline):

1. **Substrate demoted to `candidate` or retracted** → all invariants with that substrate in `emergent_from` enter a new status: `pending_substrate_reconfirmation`. They are not automatically demoted (the invariant may still hold under a replacement substrate), but they cannot be cited as supporting evidence for new claims until a governance decision clears them.

2. **Substrate replaced by successor** (e.g., SD-026 superseded by SD-026b) → governance must explicitly choose one of:
   - **transfer**: invariant's `emergent_from` is updated to the successor substrate, claim remains active,
   - **re-derive**: invariant is demoted to `candidate` and must accumulate its own evidence on the new substrate,
   - **retract**: invariant is withdrawn (the new substrate does not support the invariant's well-formedness).

3. **Substrate promoted (candidate → provisional → active)** → dependent emergent invariants do **not** auto-promote. Invariant confidence is scored independently; the substrate change only removes the `pending_substrate_reconfirmation` flag.

4. **Universal invariants** are unaffected by substrate changes. No `emergent_from` means no substrate coupling.

**Rationale for not auto-promoting emergent invariants with their substrate:** the invariant and its substrate can fail independently — a substrate can be the correct design while the invariant claim about it is wrong, and vice versa. Coupling their promotion would contaminate both evidence records.

---

## 5. Pipeline Changes

Minimal, in order:

1. **`scripts/validate_claims.py`** (new, ~50 lines): enforce schema rules from §2. Called at the top of `build_claims_json.py` and `governance.sh`. Fail loud.

2. **`scripts/build_claims_json.py`**: include `invariant_type` and `emergent_from` in the emitted JSON (currently outputs only `status, subject, title, type`). Explorer tooltips can then show the distinction.

3. **`scripts/generate_pending_review.py`**: add a new section to `promotion_demotion_recommendations.md` — "Substrate changes with dependent invariants" — that flags any SD/ARC whose status changed since last governance and lists the emergent invariants pointing at it. This is the mechanism that makes §4 rule 1 actionable.

4. **`governance.sh`**: no change beyond calling `validate_claims.py` at start.

Deferred (not in this pass): explorer UI changes to visually mark emergent vs universal invariants; upstream cascades in evidence scoring.

---

## 6. Documentation

Files to create or edit:

- **NEW** `docs/architecture/invariant_types.md` — the canonical explainer. Contents: the distinction, the physics analogy (charge conservation / Maxwell), INV-012 / SD-026 as the worked example, classification criteria mirroring §3, governance-cycle implications mirroring §4. Target length: ~200 lines.
- **EDIT** `docs/claims/claims.yaml` — update the schema comment header at the top of the file to document `invariant_type` and `emergent_from`.
- **EDIT** `REE_assembly/CLAUDE.md` — add a short subsection under "Governance Pipeline" titled "Invariant types" with a pointer to the architecture doc and the §4 rule in 3–4 lines. Also note the new `validate_claims.py` gate.
- **EDIT** `REE_Working/CLAUDE.md` — one-line pointer under "Claims governance" work-area row, if appropriate.
- **EDIT** `MEMORY.md` entry for governance — add a line noting the two invariant types and the substrate-reconfirmation rule, so future sessions inherit it.

No updates to `ree-v3/CLAUDE.md` — this is purely REE_assembly/registry concerns.

---

## 7. Open Questions — Resolved

Decisions taken 2026-04-17:

**Q1. Audit scope — RESOLVED.** Single pass produces a **classification registry** (`docs/governance/invariant_classification_audit.md`) with three buckets: clear-universal, clear-emergent, grey-zone. Clear entries are applied to `claims.yaml` immediately. Grey-zone entries get `invariant_type: grey_zone` as a placeholder and self-contained follow-up prompts — each resolved in its own session for maximum clarity. Rationale: tight transition, no bulk misclassification, grey zones get full context per session.

**Q2. Validation strictness — RESOLVED.** `validate_claims.py` ships in **warn-only mode** for a grace period. Hard-fail is a separate later commit, gated on the audit registry being cleared of grey-zone entries (or an explicit governance decision to flip the switch earlier). Rationale: protects against the audit stalling mid-way if token budget or time runs out — the registry stays usable in the intermediate state.

**Q3. `pending_substrate_reconfirmation` — RESOLVED.** Implemented as a **boolean flag** on the claim entry, not a new status value. Follows existing `v3_pending` precedent. Status values stay clean (candidate/provisional/active/retracted); the flag layers orthogonally.

**Q4. Retroactive application — RESOLVED with checkpoint.** Apply rule 1 retroactively at audit time (any substrate currently below `active` flags its dependent emergent invariants). Implementation is reversible — the flag is a single boolean per claim, `git revert` of the audit commit clears it. **Checkpoint:** after the flagging pass, count how many invariants are flagged. If the number is large (threshold: >10 or >20% of classified emergent invariants — to decide at the time), pause before any downstream action (re-scoring, pipeline changes acting on the flag) and review with the user whether the rule needs refinement before cascading.

**Q5. Audit delivery — RESOLVED.** Separate sessions are fine. The audit registry is explicitly designed (Q1 resolution) to produce self-contained follow-up prompts for grey-zone entries. Each such prompt can be fed to a fresh session without this conversation's context. The classification pass itself can also be delegated to a separate session once this plan is committed.

---

## 8. Execution Order

Sessions are numbered; each is designed to stand alone with a self-contained prompt.

**Session A — Foundations** (this plan's author or next session):
1. Draft `docs/architecture/invariant_types.md`.
2. Write `scripts/validate_claims.py` in warn-only mode.
3. Update `claims.yaml` schema header comment.
4. Formalize INV-012 with `invariant_type: emergent`, `emergent_from: [SD-026]`.
5. Update `build_claims_json.py` to emit the new fields.
6. Short updates to `REE_assembly/CLAUDE.md`, `REE_Working/CLAUDE.md`, MEMORY.md.
7. Commit and push.

**Session B — Audit pass**:
1. Single pass through all `type: invariant` entries (~72).
2. Produce `docs/governance/invariant_classification_audit.md` with three-section registry (clear-universal / clear-emergent / grey-zone).
3. Apply `invariant_type` + `emergent_from` to claims.yaml for all clear entries.
4. Apply `invariant_type: grey_zone` to ambiguous entries.
5. Apply retroactive `pending_substrate_reconfirmation` flags per Q4 resolution; count and report.
6. **Checkpoint with user** if flag count exceeds threshold (see Q4).
7. Commit and push.

**Sessions C₁, C₂, …** — one per grey-zone invariant, each launched with its self-contained prompt from the audit registry. Each produces a governance decision: universal / emergent-on-X / re-stated / retract. Updates claims.yaml for the one entry and marks it resolved in the registry.

**Session D — Pipeline completion**:
1. Flip `validate_claims.py` to hard-fail (assuming grey-zone entries cleared, or explicit override).
2. Update `generate_pending_review.py` to emit the "Substrate changes with dependent invariants" section (§5 item 3).
3. Verify full governance pipeline runs cleanly.
4. Commit and push.

**Session count estimate:** A, B, D are one session each; C is N sessions where N = grey-zone count (probably 10–20). Total: ~15–25 sessions, but most are short (single-invariant decisions). The plan is designed so any session can be interrupted without leaving the registry in a broken state — grey-zone placeholders and warn-only validation absorb partial completion.

---

## 9. What This Is Not

- Not a change to what counts as evidence or how confidence is scored.
- Not a change to how substrates (SDs) themselves are promoted.
- Not a change to the V3-pending gate.
- Not a claim that universal invariants are more valuable than emergent ones — both are legitimate, they just have different failure modes.

The change is structural: make the registry represent the relationship that already exists (some invariants rest on substrate choices, some don't) and make governance act on it when substrates change.
