---
nav_exclude: true
---

# Canonical-Profile Constitution Document -- TEMPLATE

**This is scaffolding, not a filled-in document.** No canonical-profile version
has been declared yet -- the only artifact under this directory as of
2026-08-12 is `ree_v3_baseline@v0`, a placeholder with an **empty**
`overrides` dict, frozen specifically so the mechanism exists without
prejudging which flags belong in it. Do not fill this template in as part of
routine documentation work; it is filled in once, per profile version, at the
moment a human governance decision actually declares that version canonical
(see `../canonical_profile_admission_criteria.md`, Process step 5-6, and the
draft second-stage adjudication prompt in
`evidence/planning/architecture_epoch_investigation.md` Section 17).

**How to use this template.** Copy it to
`<profile_name>_v<version>_constitution.md` in this same directory, alongside
the frozen `<profile_name>.json` artifact it documents. Replace every
`[FILL IN: ...]` placeholder. Do not delete a section for being inapplicable
-- write "None" or "N/A" explicitly, so a reader can tell "nothing here" from
"this section was never filled in."

---

## 1. Identity

| Field | Value |
|---|---|
| Profile name | `[FILL IN: e.g. ree_v3_baseline]` |
| Version | `[FILL IN: e.g. v1]` |
| `canonical_profile` (manifest field value, `"<name>@<version>"`) | `[FILL IN]` |
| `canonical_profile_hash` | `[FILL IN: from the frozen JSON artifact -- do not hand-compute]` |
| `substrate_hash` | `[FILL IN: from the frozen JSON artifact]` |
| `substrate_n_files` | `[FILL IN]` |
| `frozen_at_utc` | `[FILL IN: date -u +"%Y-%m-%dT%H:%M:%SZ" at freeze time, per CLAUDE.md Timestamps rule]` |
| `architecture_epoch` this profile layers onto | `[FILL IN: e.g. ree_hybrid_guardrails_v1 -- this field is unchanged by profile adoption; see admission-criteria doc's "See also"]` |
| Frozen by (session/commit) | `[FILL IN]` |
| Declared canonical by (user decision reference) | `[FILL IN: link to the governance record / decision log entry -- do not declare unilaterally]` |

## 2. Purpose and scope

`[FILL IN: one paragraph. What is this profile version FOR -- e.g. "the first
populated V3 organism definition, admitted per architecture_epoch_investigation.md
Section 9" -- and what class of experiment is expected to construct its config
from it rather than hand-assembling overrides.]`

## 3. Admitted mechanisms -- Canonical core

Every row must have cleared all seven criteria in
`../canonical_profile_admission_criteria.md`. One row per admitted `REEConfig`
field (or tightly-coupled group of fields).

| Config field(s) | Claim id(s) | Corpus enablement count (guard run date) | Cited evidence run | Rationale for admission |
|---|---|---|---|---|
| `[FILL IN]` | `[FILL IN]` | `[FILL IN: N (as of YYYY-MM-DD default_off_drift_guard.py run)]` | `[FILL IN: run_id, confirmed to actually exercise this field per criterion 3]` | `[FILL IN]` |

`[FILL IN or delete: repeat the row above for every admitted core mechanism. If
none, write "None -- this version is a mechanism-only placeholder" and say why.]`

## 4. Admitted mechanisms -- Canonical but context-dependent

Same table shape as Section 3, plus the caveat under which each field is
admitted (the specific context it depends on, and what would need to change
for it to move to canonical core on a future version).

| Config field(s) | Claim id(s) | Corpus enablement count | Cited evidence run | Context-dependency caveat |
|---|---|---|---|---|
| `[FILL IN]` | `[FILL IN]` | `[FILL IN]` | `[FILL IN]` | `[FILL IN: e.g. "admitted only once chip-XXXX lands"]` |

## 5. Known limitations

`[FILL IN: what does this profile version NOT claim to do or fix? What
behaviour should a reader NOT infer just because a mechanism is admitted here?
Distinct from Section 7 (exclusions) -- this is about the admitted set's own
limits, not about what was left out.]`

## 6. Known interactions

Per admission criterion 5: every admitted candidate must be checked against
other admitted candidates in the same subsystem, under the actual combination,
not just individually.

| Subsystem | Interacting fields | Combination tested? (run/battery reference) | Outcome |
|---|---|---|---|
| `[FILL IN]` | `[FILL IN]` | `[FILL IN]` | `[FILL IN: catastrophic regression / expected architectural change / scientific regression / measurement incompatibility -- per criterion 4's four-way split]` |

`[FILL IN or delete: also name any known-risky combination that was
deliberately NOT admitted together as a result of this check, and why.]`

## 7. Explicit exclusions

Everything considered for this profile version and placed in one of the four
non-admitting categories from `../canonical_profile_admission_criteria.md`
(Experimental substrate / Diagnostic-only / Deprecated-superseded /
V4-deferred). Naming what was excluded, and why, is what keeps this a curated
decision rather than an unexamined default.

| Config field(s) | Category | Why not admitted this version |
|---|---|---|
| `[FILL IN]` | `[FILL IN]` | `[FILL IN]` |

## 8. Unresolved gaps / open governance debt carried forward

Per admission criterion 7, a candidate is not disqualified by unrelated open
debt. Name what is still open for anything admitted in Sections 3-4, so a
future reader can tell "known and accepted" from "silently forgotten."

`[FILL IN: e.g. "MECH-090's neighbours remain gated on the F-dominance
investigation (see Section 15 of architecture_epoch_investigation.md) and are
NOT admitted in this version regardless of individual status."]`

## 9. Qualification record

Summary of the qualification battery run against this profile version
(investigation doc Section 12): contract suite result, `v3_parity_smoke`-pattern
battery result (generalized per the admission-criteria doc's criterion 4), and
every observed delta classified per the four-way split. Link the full report
rather than reproducing it here.

| Battery component | Result | Report link |
|---|---|---|
| Contract suite | `[FILL IN]` | `[FILL IN]` |
| Profile-parity smoke (generalized `version_layering_doctrine.md` guard) | `[FILL IN]` | `[FILL IN]` |
| `test_flag_inertness.py` (admitted flags) | `[FILL IN]` | `[FILL IN]` |
| Fishtank whole-organism smoke | `[FILL IN]` | `[FILL IN]` |

`[FILL IN: for every delta observed, one line -- field, delta, classification
(catastrophic regression / expected architectural change / scientific
regression / measurement incompatibility), and how it was resolved. A
catastrophic regression anywhere in this table means this version was not
declared -- do not fill this table in retroactively to justify a decision
already made.]`

## 10. Relationship to the previous profile version / epoch

`[FILL IN: if this is not v0 -- what changed relative to the immediately prior
version of this profile? New admissions, removals, re-admissions after a
qualification fix? Is any prior evidence retagged as a result (it should not
be -- see architecture_epoch_investigation.md's repeated instruction not to
bulk-retag existing evidence)? If this is the first populated version, say so
explicitly and name what "v0" (the empty-overrides placeholder) established.]`

## 11. Amendment log

| Date (UTC) | Change | Session/commit |
|---|---|---|
| `[FILL IN]` | Initial declaration | `[FILL IN]` |
