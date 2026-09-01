**Status: AWAITING USER REVIEW.**

# Flat-only experiment manifests are structurally invisible to claim_evidence.v1.json

chip: `chip-20260830-exq547-runid-index-invisible`
session: `metaworker-chip-20260830-exq547-runid-index-invisible` (headless)
date: 2026-09-01T15:59:49Z

## Origin

Found 2026-08-30 by `failure_autopsy_966-436g-951-959-822d-cluster_2026-08-30` (Step 7b C1
acted-on finding, its Section 3) while autopsying V3-EXQ-951. That autopsy diagnosed the
symptom as: V3-EXQ-547's manifest
(`REE_assembly/evidence/experiments/v3_exq_547_mech320_tonic_vigor_substrate_readiness_v3_20260510T205612Z.json`)
has `_v3` sitting mid-string rather than at the run_id's end, in apparent violation of
CLAUDE.md's V3 Experiment Tagging convention, and hypothesized that this caused the manifest's
absence from `claim_evidence.v1.json`.

**That hypothesis is checked and is FALSE.** The real root cause is structural and unrelated to
run_id suffix position -- see below. This doc corrects the diagnosis and reports the true, wider
scope.

## The actual root cause (verified by code read, not guessed)

`REE_assembly/evidence/experiments/scripts/build_experiment_indexes.py`'s `_scan_runs` (its sole
discovery loop) is:

```python
for manifest_path in sorted(base_dir.glob("**/runs/**/manifest.json")):   # line 1731
```

This is the **only** way a run enters the index. A flat manifest at
`evidence/experiments/<run_id>.json` is read by `_scan_runs` **exclusively** as a governance-
annotation *overlay* for an *already-discovered* pack (`_resolve_flat_sibling` +
`_merge_flat_manifest_overrides`, ~line 1774-1808) -- never as an independent discovery source.
The module's own comment at line 1427-1438 states this plainly: flat-file corrections are "NOT
the `runs/<run_id>/manifest.json` 'pack' copy the indexer scans for scoring."

So a manifest that has **no** sibling `<experiment_type>/runs/<run_id>/manifest.json` anywhere
under `evidence/experiments/` is invisible to the index **regardless of what its `run_id` field
says** -- renaming V3-EXQ-547's run_id to end in `_v3` would not have fixed anything; the glob at
line 1731 never looks at a flat top-level file to begin with.

Confirmed with two positive controls in the existing corpus: `V3-EXQ-628` and `V3-EXQ-668` both
have run_ids with `_v3` sitting mid-string (`..._v3_20260602T191625Z`, `..._v3_20260611T135309Z`)
-- identical shape to V3-EXQ-547 -- and **are** visible in `claim_evidence.v1.json`, because both
have a matching run pack. Suffix position is a correlate, not a cause.

## Why this isn't a one-off data bug

`ree-v3/experiments/pack_writer.py`'s `write_flat_manifest` (line 431+) is, by its own docstring,
**"The single sanctioned writer for a FLAT V3 experiment manifest"** -- a deliberate,
intentionally-flat-only chokepoint, distinct from the same module's `write_pack` (which creates
the `runs/<run_id>/manifest.json` pack the indexer actually scans). An entire family of
`v3_exq_*_substrate_readiness.py` "diagnostic" scripts calls `write_flat_manifest` directly and
**never** calls `write_pack`. So this is a standing structural gap between a sanctioned authoring
path and the indexer's discovery path, not a mis-keyed one-off.

`experiment_purpose: "diagnostic"` does **not** categorically exclude evidence from scoring:
550 of 559 diagnostic-purpose **pack-based** manifests in the corpus today are visible in the
index. The 100% exclusion rate is specific to flat-only, pack-less manifests.

## Corpus scan

`REE_assembly/scripts/audit_flat_only_orphaned_manifests.py` (new, read-only, committed
alongside this doc) finds every flat manifest with a real resolved status, not a `--dry-run`
smoke, and no matching run pack anywhere in the corpus. Run 2026-09-01:

```
python3 scripts/audit_flat_only_orphaned_manifests.py --list
```

23 findings total. Triaged into three buckets:

### Bucket A -- current epoch (`ree_hybrid_guardrails_v1`), scoring-relevant (non-empty
`claim_ids`, `evidence_direction` in `{supports, does_not_support, weakens}`) -- **making these
visible would change claim confidence today:**

| run_id | evidence_direction | claim_ids |
|---|---|---|
| `v3_exq_542_arc062_gated_policy_substrate_readiness_v3_20260509T202211Z` | supports | ARC-062, MECH-309 |
| `v3_exq_544_mech313_noise_floor_substrate_readiness_v3_20260510T104458Z` | supports | MECH-313, ARC-065 |
| `v3_exq_544a_mech313_noise_floor_substrate_readiness_v3_20260529T154903Z` | supports | MECH-313, ARC-065 |
| `v3_exq_395_mech220_harm_hub_dry_20260413T074905Z` | weakens | MECH-220 |
| `v3_exq_395_mech220_harm_hub_dry_20260413T075133Z` | weakens | MECH-220 |
| `v3_exq_259_wanting_gradient_navigation_1775666895` | does_not_support | SD-015, MECH-112, ARC-030, SD-012 |

Caution on the two `v3_exq_395` rows: despite carrying `_dry_` in their run_id/filename, neither
has a truthy `dry_run` field and both are `experiment_purpose: "evidence"` (not diagnostic) --
so the audit script (which checks the `dry_run` flag and filename convention the same way
`build_experiment_indexes._is_dry_run` / `_load_dry_run_run_ids` do) does not treat them as
smokes. A **third** sibling run in the same directory
(`v3_exq_395_mech220_harm_hub_dry_20260413T075033Z`) already carries
`evidence_direction: "superseded"` and is excluded from this table on that basis (superseded is
inactive regardless of visibility). Whether the `_dry_` naming on the other two is a leftover
misnomer or an actual un-flagged smoke is a provenance question this session did not adjudicate
-- flagged to governance below rather than guessed.

### Bucket B -- current epoch, but visibility would **not** change scoring (evidence_direction
`non_contributory`, or no `claim_ids` at all): `v3_exq_542a` (x3, `non_contributory`),
`v3_exq_545` (x2, `non_contributory`), `v3_exq_546` (x2, `non_contributory`), **`v3_exq_547`**
(`non_contributory` -- the run that originated this chip), `v3_exq_613` / `v3_exq_617` /
`v3_exq_639` (no `claim_ids`). Per the chip brief, V3-EXQ-547's scientific content is
deliberately **not** adjudicated here -- and per this scan it would not matter if it were, since
its own `evidence_direction_note` already reclassified it `non_contributory` during the
2026-05-11 governance walk that produced it. No autopsy is owed on this run specifically; it
carries zero weight toward MECH-320 / ARC-066 whether or not it is index-visible.

### Bucket C -- ambiguous / likely out of scope, not acted on:
- `v3_exq_472_sd011_platform_stability_pilot_output` -- `architecture_epoch` absent, no
  parseable `timestamp_utc`; pre-epoch/legacy shape, cannot even be epoch-backfilled by the
  indexer's own fallback logic (needs a timestamp).
- `v3_exq_518_sd019a_20260504T150257Z` -- current epoch but `claim_ids: []`,
  `evidence_direction: None`; nothing to score even if visible.
- `v4_exq_001/002/003_..._v4` (x3) -- `architecture_epoch: "ree_self_model_v1"`, a **different**
  substrate generation from the current V3 epoch (`ree_hybrid_guardrails_v1`). Likely correctly
  out of `claim_evidence.v1.json`'s scope by epoch filtering rather than a defect; not asserted
  either way here.

## What this session did NOT do, and why

- **Did not rename any run_id.** Per the corrected root cause, a rename would not fix visibility
  (the glob never reads flat files as a discovery source), and CLAUDE.md's own EXQ-versioning
  section treats a run_id as part of the run's provenance record -- not something to retro-edit.
- **Did not touch `_scan_runs` / `build_experiment_indexes.py`'s discovery logic.** Two candidate
  remediations exist and this is a scoring-semantics decision, not a mechanical one:
  1. **Indexer-side**: teach `_scan_runs` to also discover pack-less flat manifests meeting the
     same non-dry-run / non-smoke bar packs already meet, scoring them directly from the flat
     file. Lowest-friction, but changes what counts as "scored evidence" fleet-wide without a
     human decision point.
  2. **Backfill**: write a matching `runs/<experiment_type>/runs/<run_id>/manifest.json` pack
     for each Bucket-A manifest (via `pack_writer.write_pack`), mirroring the flat content
     exactly. Narrower blast radius (touches only Bucket A), but is 6 separate hand-authored
     packs and needs the same care `_resolve_flat_sibling`'s docstring already gives to
     pack/flat provenance.

  Either changes claim confidence for ARC-062, MECH-309, MECH-313, ARC-065, MECH-220, SD-015,
  MECH-112, ARC-030, SD-012 the moment it lands -- **/governance's call, not this session's.**
- **Did not run a full index regen.** `build_experiment_indexes.py` touches ~1200 files corpus-
  wide (CLAUDE.md "Narrow Edits Only"); nothing here justifies that blast radius for a scan-only
  finding.
- **Did not adjudicate any run's scientific content**, per the originating chip's explicit
  instruction.

## What this session DID do

- Corrected the root-cause diagnosis (this doc).
- Added `REE_assembly/scripts/audit_flat_only_orphaned_manifests.py`: read-only, detects this
  defect class going forward (`--list` for full findings, exit 1 on any finding). No pinned
  baseline (unlike `check_run_id_letter_hygiene.py`) -- deliberately simpler, since the interesting
  work here is triage-by-a-human (which bucket a new finding lands in), not a fire-count regression
  gate.
- Raised `governance_flag.py --flag-type evidence_discrepancy` naming Bucket A's claim_ids, so
  /governance picks up the scoring-relevant subset without needing to re-derive it from this doc.

## Recommendation

/governance reviews Bucket A first (the 6 runs that would move claim confidence), chooses a
remediation path (indexer-side vs backfill) per claim family, and separately adjudicates the two
ambiguous `v3_exq_395` `_dry_`-named-but-not-flagged rows for genuine dry-run status. Bucket C
items are lower priority and may not need action at all.
