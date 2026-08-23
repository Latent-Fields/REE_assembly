---
title: Canonical-Profile Admission Criteria
parent: "Foundations & Rationale"
grandparent: Architecture
nav_order: 4
---

# Canonical-Profile Admission Criteria

**Status:** design doctrine, 2026-08-12. Derived verbatim from
`evidence/planning/architecture_epoch_investigation.md` Section 9 (a design-now
investigation: no defaults changed, no epoch declared, no profile members
admitted by that document or this one).

**Triggering question:** "REE-v3" does not currently denote a unique canonical
organism (investigation doc Section 6) -- bare `REEConfig()` defaults, the
`ree_hybrid_guardrails_v1`-tagged corpus, any given script's hand-assembled flag
bundle, and the unwritten "on by convention" set are four different,
non-interchangeable things people mean by the phrase. The canonical-profile
mechanism (`ree-v3/ree_core/utils/canonical_profile.py`,
`ree-v3/experiments/_lib/canonical_profile_fingerprint.py`) exists to name and
freeze one of them on purpose. This document is the gate that mechanism sits
behind: the criteria a `REEConfig` flag must clear before a human curator adds
it to a profile's `overrides`.

**This document does not admit anything.** As of 2026-08-12 the only declared
profile is `ree_v3_baseline@v0`
(`docs/architecture/canonical_profiles/ree_v3_baseline.json`), frozen with an
**empty** `overrides` dict specifically so it layers onto bare `REEConfig()`
defaults with zero effective change until a real admission pass runs. Running
that pass is future work (investigation doc Section 16, chip
`chip-20260812-canonical-profile-mechanism-design` and neighbours), not this
document's job.

---

## Why multi-dimensional, not a single implemented-vs-canonical gate

A claim's `status` field alone is not a safe admission signal. The
`default_off_drift_audit_2026-07-21.md` corpus (re-run live for the
investigation via `scripts/default_off_drift_guard.py`, 132 candidate
claim/knob pairs as of 2026-08-12) contains multiple claims at `stable` or
`active` whose implementing flag is either never turned on anywhere in the
corpus, or is turned on only by a code path that does not actually exercise
the claim's described mechanism. Treating registry status as sufficient would
silently import that drift into the profile as if it were settled fact.
Conversely, requiring every candidate to have zero open governance debt before
admission would reproduce the paralysis the investigation explicitly warns
against (criterion 7 below) -- most of this codebase's real, useful mechanisms
carry *some* open thread.

The seven criteria below are the discriminators the drift-guard method and the
`version_layering_doctrine.md` guard pattern already proved out, reused rather
than reinvented.

## The criteria

1. **Substrate implemented.** Trivial gate -- the `REEConfig` field and its
   consuming code path exist. Necessary, never sufficient on its own.

2. **Corpus enablement count is non-trivial.**
   `scripts/default_off_drift_guard.py` is the load-bearing discriminator here,
   not a new check to build: it counts files under `ree-v3/experiments/` and
   `ree-v3/tests/` that set the knob `= True`. Near-zero enablement despite
   `stable`+ registry status is a red flag for admission **regardless of what
   the claim's status text says** -- this is exactly the shape of the
   `SD-020` / `MECH-089` / `SD-035` / `MECH-117` / `ARC-004` findings in the
   source audit (investigation doc Section 4c), where the registry read
   "settled" and the substrate read "never actually run this way." Run the
   guard fresh (`--out`/`--json` flags write a re-derivable report) rather than
   citing a stale enablement number -- the corpus and the guard's own parser
   coverage both grow over time (288 -> 341 default-off fields, 63 -> 132
   candidate pairs between the 2026-07-21 snapshot and the 2026-08-12 rerun).

3. **The cited evidence run actually exercises the same flag/path the claim
   describes.** Must be checked, not assumed from status text or from the
   claim id appearing in the field's comment. `SD-020` and `SD-035` both fail
   this in the source audit -- `SD-020`'s cited PASS run's causal path is a
   script-local prototype of a *superseded* predecessor that bypasses the flag
   entirely, and `SD-035`'s evidence is a module-level unit test, never an
   agent-integrated run. `default_off_drift_guard.py`'s own module docstring
   documents the general failure mode (the `MECH-104`/`use_phasic_burst` false
   positive: the claim id is present in the field's comment, but the cited
   evidence run manipulates a different, always-on parameter) and grades each
   attribution `decl` vs `mention` as an advisory signal for where to look
   first -- the `attr` column does not gate by itself; a human still has to
   open the cited run and confirm it touches the knob.

4. **Non-degenerate: no catastrophic disruption of unrelated core function.**
   Generalize the `version_layering_doctrine.md` Guard-C pattern
   (`test_version_layering_noop_default.py`'s C1-C4 structure: default-off
   assertion -> path-resolves-on-real-config -> bit-identical-when-off ->
   runs-without-error) from its original scope ("V4/V5 flags off") to "profile
   candidate flag off vs. on." Distinguish four outcomes when a candidate flag
   is flipped on against the qualification battery (Section 12 of the
   investigation doc), rather than auto-accepting or auto-rejecting any metric
   movement:
   - **Catastrophic regression** -- non-learning, NaN, degenerate, immobile.
     Reuse `design_implementation_audit_2026-07-09.md`'s confirmed per-flag
     inertness findings where they exist (e.g. `ARC-004`'s
     `inference_settle_iters=1` default resolving to `range(0)`, a
     no-op that also emits NaN) rather than re-deriving them. Blocking.
   - **Expected architectural change** -- a metric moves because an admitted
     mechanism genuinely changes behaviour. Must be explained in the admission
     record, not silently absorbed or silently rejected.
   - **Scientific regression** -- a previously-validated capability silently
     disappears. Blocking; investigate before proceeding.
   - **Measurement incompatibility** -- a metric's meaning changed under the
     new config, so the before/after comparison itself is not valid. Flag and
     re-derive the comparison; do not score it as pass or fail.

5. **Known-interaction check against other admitted candidates in the same
   subsystem.** At minimum, the already-known-risky combinations surfaced in
   the investigation's Section 5 gate admission of anything touching the same
   subsystem until re-verified **under the actual combination**, not just
   individually: MECH-303's production-default safety threshold never clears
   chance-level discrimination under the sourcing convention every production
   driver actually uses (open chip
   `chip-20260812-mech303-sourcing-mode-reconciliation` must land first); the
   V3-EXQ-922 three-knob MECH-151/152/ARC-041 combination dissociated on its
   first-ever joint run. A flag passing criteria 1-4 in isolation does not
   default to admission if it shares a subsystem with a flag on this list --
   re-run the combination first.

6. **Claim status floor: >= `provisional`**, with `stable` / `active` /
   `implemented` / `candidate_substrate_landed` preferred. Necessary,
   **explicitly not sufficient** given criteria 2-3 above -- this is the
   criterion most likely to be mistaken for the whole gate, and it is
   deliberately listed after the two that catch what it misses.

7. **Do not require zero open governance debt to admit.** A candidate carrying
   some unresolved thread (a pending autopsy on a *different* run, an open
   scoping chip on a *related* but distinct mechanism, a `candidate`-status
   claim elsewhere in the same subsystem) is not automatically disqualified.
   Requiring full closure before any admission reproduces the paralysis this
   whole design effort exists to avoid -- criteria 2-5 already catch the
   failure modes that matter (drift, unverified evidence, catastrophic
   interaction). Use the category structure below instead of a binary
   admit/reject gate: a candidate with real but bounded debt lands in
   "canonical but context-dependent," not in limbo.

## Categories

Every candidate flag sorts into exactly one of six categories (investigation
doc Sections 9 and 14). A profile version's `overrides` dict is drawn from the
first two categories only; the rest are recorded in the admission pass's
report for provenance, not written into the frozen artifact.

| Category | Admits into profile? | Populated example set (2026-08-12 snapshot -- re-derive, do not cite as current) |
|---|---|---|
| **Canonical core** | Yes | De facto canonical by corpus practice already (drift-audit bucket (b)): `use_harm_stream`/`use_affective_harm_stream` (434/402 enablements), `use_resource_proximity_head` (273), `use_per_stream_vs` (135), `use_lateral_pfc_analog` (143), `use_dacc` (149), `use_salience_coordinator` (57), `use_structured_curiosity` (45), `sws_enabled`/`use_sleep_loop` (40-47), `use_event_classifier` (38). |
| **Canonical but context-dependent** | Yes, with a recorded caveat | Validated substrate, real but limited exercise: `use_pcc_analog`/`use_aic_analog`, `use_amygdala_analog` (agent-integrated evidence specifically). The MECH-302/303/304 safety triad belongs here *only* once the MECH-303 sourcing-mode chip lands. |
| **Experimental substrate** | No | Landed but not yet corpus-exercised enough to clear criterion 2; candidate for promotion on the next admission pass. |
| **Diagnostic-only** | No | Deliberate, self-annotating holds -- not drift. Example: everything behind `use_differentiable_cem` (`ARC-007`/`SD-016`/`SD-055`), where manifests explicitly record `"NOT FLIPPED (default False; SD-055 safety note)"`. Leave on its own resolution track. |
| **Deprecated/superseded** | No | Drift-audit bucket (c) genuine divergence, or a flag a later mechanism has replaced. |
| **V4-deferred** | No, by construction | Anything registered in `ree-v3/ree_core/version_layering.py`'s `GENERATION_FLAGS` -- out of scope for a V3 profile by `version_layering_doctrine.md`'s own invariant, not re-litigated here. |

## Process for running an admission pass

1. Re-run `scripts/default_off_drift_guard.py` fresh (do not reuse a prior
   report's numbers -- both the corpus and the parser's field coverage grow).
2. Apply criteria 1-7 to every candidate pair the guard surfaces at claim
   status `provisional`+, sorting each into one of the six categories.
3. For every candidate proposed for **canonical core** or **canonical but
   context-dependent**, run the qualification battery (investigation doc
   Section 12: `version_layering_doctrine.md`'s guard pattern generalized,
   the ~3,500-test contract suite, `test_flag_inertness.py`, the Fishtank
   whole-organism smoke pattern) and classify every observed delta per
   criterion 4's four-way split.
4. Draft or update the profile's `overrides` via
   `ree_core.utils.canonical_profile.CanonicalProfileSpec`; freeze and persist
   it with `experiments/_lib/canonical_profile_fingerprint.py` under
   `docs/architecture/canonical_profiles/<name>.json`.
5. Fill in a constitution document for the new version using
   [`canonical_profiles/CONSTITUTION_TEMPLATE.md`](canonical_profiles/CONSTITUTION_TEMPLATE.md)
   alongside the frozen artifact.
6. Present the draft profile, its constitution document, and the
   qualification report to the user for an explicit go/no-go decision. Do not
   declare a profile version canonical unilaterally (investigation doc's
   draft second-stage adjudication prompt, Section 17, is the template for
   this step).

## Relationship to the F-dominance gate

Final admission of anything touching E3 selection/arbitration -- `MECH-090`'s
gating triad (`beta_gate_bistable`, `use_commit_readiness_gate`,
`use_vs_commit_release`, `use_coalition_controller`,
`use_mech090_readiness_conjunction`, `use_modulatory_selection_authority`,
`use_e3_reselection_shortcircuit`, `use_difficulty_gated_proposal_entropy`)
and anything touching `ree_core/predictors/e3_selector.py`'s committed-action
readout -- waits on the live F-dominance / conversion-ceiling investigation
(`MECH-439` and campaign; investigation doc Section 15) reaching a
governance-reviewed disposition. Re-check `claims.yaml` and
`substrate_queue.json` at the time of any admission pass rather than trusting
this document's framing of that campaign's state, which is a snapshot as of
2026-08-12.

**Not gated on F-dominance:** running this admission process against any
non-E3-adjacent candidate, and all of the profile mechanism's plumbing
(manifest fields, persisted fingerprint, this document, the constitution
template). None of it depends on F-dominance's outcome, only on there being an
outcome to plug into the "canonical but context-dependent" caveat when there
is one.

## See also

- `evidence/planning/architecture_epoch_investigation.md` -- full investigation
  this document extracts Section 9 from, including the option analysis
  (Sections 7-8) for why a curated profile layered above bare `REEConfig()`
  defaults was chosen over flipping global defaults or auto-assembling from
  live governance state.
- `evidence/planning/default_off_drift_audit_2026-07-21.md` and
  `scripts/default_off_drift_guard.py` -- the standing, re-runnable method
  behind criteria 2-3.
- `version_layering_doctrine.md` -- the guard pattern criterion 4 generalizes,
  and the source of the V4-deferred category's exclusion rule.
- `canonical_profiles/CONSTITUTION_TEMPLATE.md` -- the per-version write-up
  template a landed admission pass fills in.
- `ree-v3/ree_core/utils/canonical_profile.py`,
  `ree-v3/experiments/_lib/canonical_profile_fingerprint.py` -- the mechanism
  this gate feeds.
