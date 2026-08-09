# `epistemic_category` vocabulary audit — autopsy corpus vs the `claims.yaml` enum

**Date:** 2026-08-09 · **Chip:** `chip-20260809-epistemic-category-vocab-audit`
**Corpus:** 380 `REE_assembly/evidence/planning/failure_autopsy_*.json` (373 `confirmed`)
**Fields audited:** `targets[].recommended_epistemic_category` and `recommended_epistemic_category_per_claim`
**Enum source of truth:** `VALID_EPISTEMIC_CATEGORIES`, `REE_assembly/scripts/validate_claims.py` (8 values, unchanged)

## Headline

**683 of 1187 value-instances (57.5%) are outside the `claims.yaml` enum, spread over 62 distinct values.**
This is the corpus norm, not a stray typo. `claims.yaml` itself is currently **clean** — all 521 structured
`epistemic_category:` values are valid — so the defect has been contained downstream rather than prevented.

## Why it was never caught

The field is written into `claims.yaml` **verbatim** by `/governance` Step 6 ("apply its
`recommended_evidence_quality_note` ... and `recommended_epistemic_category` to the claim in claims.yaml"),
and nothing upstream of that write validates it:

| stage | checks presence | checks enum validity |
|---|---|---|
| `/failure-autopsy` SKILL.md (pre-fix) | — | no — gave one example (`substrate_ceiling`), never the enum |
| GOV-CAT-1 `check_epistemic_category_completeness.py` | **yes** | **no** |
| `/governance` Step 6 apply | — | no |
| `validate_claims.py --strict` | — | **yes (ERROR)** — but only *after* the value is in the registry |

So `--strict` at commit time is the sole gate. It worked on 2026-08-08/09: applying three confirmed autopsies
put `competence_implementation_gap` on INV-034, Q-021 and MECH-074d, `--strict` raised 3 ERRORs, and the values
were corrected to `substrate_conditional` before the commit landed (`REE_assembly` `6be9e3b98f`). A
non-interactive cycle, or one that commits without `--strict`, would have landed them.

## The deeper finding: the field is overloaded

The out-of-enum vocabulary is not noise — it is a **failure-mode diagnosis** vocabulary
(`measurement_test_design_defect`, `precondition_unmet`, `competence_implementation_gap`, `measurement_degeneracy`),
answering *why did this run fail*. The `claims.yaml` enum answers a different question: *how should the registry
now treat this claim*. The two overlap at `substrate_ceiling` / `standard` / `substrate_conditional` /
`out_of_domain`, which is exactly what makes the collision easy to miss — a governance session sees a
familiar-looking token and applies it.

The always-stamp rule (`/failure-autopsy` Step 5, "ALWAYS STAMP IT, including when the verdict is 'no category
applies'") is the direct cause of a second family of junk values: `n/a` (13), `not_applicable_claim_free_diagnostic`
(9), `N/A`, `none -- claimless diagnostic; ...`, plus ~15 multi-sentence prose values sitting in a field
governance writes verbatim into the registry. These satisfy GOV-CAT-1's presence check while being unusable
downstream — the scan goes quiet and the value still cannot be applied.

## Choosing a replacement is consequential, not cosmetic

Six of the eight enum values sit in `_EPI_SUPPRESS_PROPOSAL` (`check_granularity_debt_recurrence.py`), which
excludes the claim from GOV-GRAN-1 granularity-debt surfacing. Four (`substrate_ceiling`, `substrate_conditional`,
`out_of_domain`, `derivational`) additionally make the claim **not v3-testable** (`_claim_v3_testable`,
`generate_inter_governance_workset.py`), starving it of experiment lanes. Only **`standard`** and **`answer_state`**
are outside the suppress set.

Every one of the 62 out-of-enum values is *currently* outside `_EPI_SUPPRESS_PROPOSAL`, so:

- mapping the measurement / test-design / precondition-unmet family to **`standard`** is **behaviour-preserving**
  for GOV-GRAN-1, for the R3 re-derive brake (not a ceiling), and for v3-testability;
- mapping it to `substrate_conditional` **silently changes** all three.

### Consequence of the 2026-08-09 correction (flagged, not changed)

The three claims corrected in `6be9e3b98f` all landed on `substrate_conditional`, which is in the suppress set
and in the not-v3-testable set:

| claim | status | `v3_pending` | now | side effect |
|---|---|---|---|---|
| INV-034 | candidate | absent | `substrate_conditional` | newly **not v3-testable**; excluded from GOV-GRAN-1 |
| MECH-074d | provisional | `false` (cleared 2026-04-22 after V3-EXQ-474 PASS x2) | `substrate_conditional` | newly **not v3-testable** — reverses the April testability clearance |
| Q-021 | open | absent | `substrate_conditional` | already excluded by `status: open`; no change |

`substrate_conditional` is defensible for all three on the reading that their answer is gated on substrate work.
But it was chosen under time pressure as the nearest valid token to `competence_implementation_gap`, not as a
deliberate testability disposition, and for MECH-074d it quietly undoes a cleared `v3_pending`. **Left unchanged
here** — this is a governance disposition, and the chip scoped this work to investigation plus the skill fix.
Recommend `/governance` re-examine whether `standard` is the better reading for INV-034 and MECH-074d.

## Fix applied

`REE_Working` `18313837` (both mirrors, `.claude/` and `.agents/`):

1. Step 5 — states the eight-value enum at the field definition, names `VALID_EPISTEMIC_CATEGORIES` as the source
   of truth, records the verbatim write-through and the missing gate.
2. Step 5 — "a failure-mode diagnosis is NOT an `epistemic_category`": route it to `four_layer_diagnosis`,
   `recommended_evidence_quality_note`, or `recommended_epistemic_category_note`.
3. Step 5 — the suppress-set / v3-testability consequences, with `standard` named as the behaviour-preserving
   mapping for the diagnostic family.
4. Step 9 JSON schema — the placeholder `"substrate_ceiling | ..."` replaced with the full enum.
5. The always-stamp rule — "no category applies" is spelled `standard`, not `n/a` / `none` / a sentence.

No `claims.yaml` values were changed by this chip.

## Not done (deliberate)

- **No corpus-wide artifact rewrite.** 683 instances across 380 confirmed artifacts are historical records;
  CLAUDE.md's standing guidance on this corpus is that re-attribution happens per-artifact with reason, never as
  a sweep. The values are inert for every current consumer (all sit outside the suppress set), so the exposure is
  prospective — a *future* governance session applying one — which the skill fix addresses at source.
- **No new gate.** A validity check in GOV-CAT-1 (which already parses every artifact and already knows the field)
  would flag 683 pre-existing instances on its first run and would need a metabolized-exclusion mechanism to be
  usable. Worth doing, but it is a scoped build, not a passing addition — see below.

## Follow-on

**Recommended: extend GOV-CAT-1 (`check_epistemic_category_completeness.py`) from a presence check to a
presence-and-validity check**, warn-only, scoped to artifacts written after a cutoff date (or with a
metabolized-exclusion marker) so the 683-instance backlog does not drown the signal. That is the standing scan
that would catch the next out-of-enum stamp *before* it reaches `claims.yaml`, rather than relying on
`validate_claims.py --strict` being run at the right moment. The skill fix is prevention at source; this is the net.

---

## Full tables

### Valid values in use

| value | in `_EPI_SUPPRESS_PROPOSAL` | instances | confirmed | files |
|---|---|---:|---:|---:|
| `substrate_ceiling` | yes | 247 | 247 | 126 |
| `standard` | no | 234 | 233 | 83 |
| `substrate_conditional` | yes | 15 | 15 | 11 |
| `out_of_domain` | yes | 8 | 8 | 4 |

**Valid total: 504 instances.**

### Out-of-enum values in use

Long free-prose values are truncated to 70 chars; none of them is a category.

| value | instances | confirmed | files |
|---|---:|---:|---:|
| `measurement_test_design_defect` | 263 | 259 | 91 |
| `competence_implementation_gap` | 117 | 117 | 43 |
| `precondition_unmet` | 77 | 77 | 23 |
| `measurement_degeneracy` | 65 | 65 | 12 |
| `measurement_gap` | 46 | 46 | 27 |
| `n/a` | 13 | 13 | 3 |
| `test_design_defect` | 11 | 11 | 3 |
| `not_applicable_claim_free_diagnostic` | 9 | 9 | 8 |
| `non_contributory` | 9 | 9 | 6 |
| `substrate_not_ready_requeue` | 6 | 6 | 4 |
| `<null>` | 3 | 0 | 1 |
| `n/a (diagnostic; no claim status change)` | 3 | 3 | 3 |
| `substrate` | 3 | 3 | 1 |
| `measurement_gap_timescale` | 2 | 2 | 1 |
| `N/A` | 2 | 2 | 1 |
| `measurement_artifact` | 2 | 2 | 2 |
| `none_stays_non_contributory_per_diagnostic_purpose` | 2 | 2 | 1 |
| `environment_adequacy_defect` | 2 | 2 | 2 |
| `verified` | 2 | 2 | 2 |
| `instrument_repair_validated` | 2 | 2 | 2 |
| `substrate_ready` | 2 | 2 | 2 |
| `n/a (degenerate)` | 2 | 2 | 1 |
| `measurement_regime_mismatch` | 1 | 1 | 1 |
| `measurement_saturation` | 1 | 1 | 1 |
| `measurement_design_broken_predicate` | 1 | 1 | 1 |
| `measurement_design_seed_truncation` | 1 | 1 | 1 |
| `measurement_design_broken_criterion` | 1 | 1 | 1 |
| `implementation_bug` | 1 | 1 | 1 |
| `dual: configuration_error (dACC axis) + substrate_under_fed (ARC-06...` | 1 | 0 | 1 |
| `implementation_gap` | 1 | 1 | 1 |
| `N/A (claim_ids=[])` | 1 | 1 | 1 |
| `measurement_reframe` | 1 | 1 | 1 |
| `substrate_starved_precondition_unmet` | 1 | 1 | 1 |
| `substrate_not_ready_requeue_confirmed` | 1 | 1 | 1 |
| `non_contributory_run_not_substrate_ceiling` | 1 | 1 | 1 |
| `no_change (self-route substrate_not_ready_requeue is correct; SD-03...` | 1 | 1 | 1 |
| `non_contributory (substrate CONVERSION ceiling -- same class as the...` | 1 | 1 | 1 |
| `does_not_support_state_authority` | 1 | 1 | 1 |
| `n/a (claim-free substrate-readiness diagnostic; substrate-queue not...` | 1 | 1 | 1 |
| `vacuous_pass` | 1 | 1 | 1 |
| `instrumentation_defect` | 1 | 1 | 1 |
| `none (claimless-in-effect substrate-readiness diagnostic; already n...` | 1 | 1 | 1 |
| `substrate_not_ready` | 1 | 1 | 1 |
| `n/a (claim_ids=[]); finding is measurement_gap + behavioural diagno...` | 1 | 1 | 1 |
| `n/a (claim_ids=[]); finding is behavioural-diagnostic / integration...` | 1 | 1 | 1 |
| `measurement_test_design_gap (N/A for governance -- no claim; manife...` | 1 | 1 | 1 |
| `none -- claimless diagnostic; characterise as a measurement / test-...` | 1 | 1 | 1 |
| `n/a (claim-free diagnostic; MECH-294 stays candidate/v3_pending, un...` | 1 | 1 | 1 |
| `substrate_ceiling (autopsy) -- USER DISPOSITION: v3_pending hold (c...` | 1 | 1 | 1 |
| `unchanged (non_contributory re-queue; NOT substrate_ceiling)` | 1 | 1 | 1 |
| `precondition_unmet (642-pattern, NOT substrate_ceiling)` | 1 | 1 | 1 |
| `measurement_calibration_not_substrate_ceiling` | 1 | 1 | 1 |
| `substrate_conditional (preserved); diagnosis = missing-dependency (...` | 1 | 1 | 1 |
| `measurement_invalid` | 1 | 1 | 1 |
| `measurement_gap (environment / test-bed producer gap; NOT substrate...` | 1 | 1 | 1 |
| `untrained_substrate_artifact` | 1 | 1 | 1 |
| `genuine_fair_test_negative_coherence_specificity_unsupported (NOT s...` | 1 | 1 | 1 |
| `test_design_ceiling` | 1 | 1 | 1 |
| `instrument_validated_cause_discriminated` | 1 | 1 | 1 |
| `substrate_ceiling (parent unchanged); failure routed as granularity...` | 1 | 1 | 1 |
| `standard (parent unchanged); failure routed as granularity debt` | 1 | 1 | 1 |
| `substrate_ceiling (selection-authority sub-type; readiness-gate mis...` | 1 | 1 | 1 |

**Out-of-enum total: 683 instances across 62 distinct values.**