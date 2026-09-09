# Run-pack always-core heal -- scoring-impact measurement

- Date: 2026-09-09T02:13:51Z
- Session: `angry-pascal-6fd799` (chip `chip-20260909-heal-existing-packs-always-core`)
- Trigger: REE_assembly `91ed465a64` + ree-v3 `abafa84` made `build_runpack_docs`
  carry the four non-provenance Experimental Recording Standard always-core keys
  (`recording_schema`, `elapsed_seconds`, `config`, `seeds`) and harvest `readout`
  as a fourth metrics spelling. Both changes are forward-only, so the existing
  corpus never got them.

## 1. The chip's premise did not survive measurement

The chip asked for "an explicit opt-in forced-regeneration path" and said every
pack must "come from `build_runpack_docs` itself". Measured against the tree,
a literal regeneration is a large-scale revert of governance state, not a backfill.

`build_runpack_docs` is a **whitelist**: it emits exactly the keys it names. But a
run-pack manifest stops being a pure function of its flat sibling the moment it
exists -- `/governance` and `/failure-autopsy` write their adjudications onto the
**pack**, while the flat manifest stays the raw as-emitted artifact.

Over the 1638 packs that still have a reachable flat source, a full regeneration
would have:

| Direction | Count | Examples |
|---|---|---|
| Keys **dropped** (pack has, whitelist does not emit) | 1124 occurrences / 77 keys | `evidence_direction_note` (643), `epistemic_category` (94), `superseded_by` (62), `supersedes_reason` (30), `scoring_excluded` (15), `governance_applied_utc` (11), `source_autopsy` (8), `failure_autopsy_ref` (6), `governance_override_from`/`_utc` (2), `adjudicated_by_autopsy`, `claim_tag_removed_by_governance` |
| Values **reverted** | 619 occurrences / 9 keys | `evidence_direction_per_claim` (265), `evidence_direction` (238), `timestamp_utc` (38), `status` (27) |
| Keys added | 3284 occurrences / 22 keys | the intended always-core payload, plus scoring-relevant extras |

Sample reverts:

- `v3_exq_085h_sd015_resource_indicator_diag_...`: `status` **SUPERSEDED -> FAIL**
- `v3_exq_033_training_depth_calibration_...`: `evidence_direction` **supports -> mixed**
- `v3_exq_026_mech071_v3_...`: `evidence_direction_per_claim` **{MECH-071: weakens, SD-003: weakens, SD-005: weakens} -> {}**

A second premise also failed: the chip expected to reach ~2929 packs. Only **1638**
of the 2931 packs have a flat source the converter can still read, so a
flat-sourced heal can never reach the other 1293 by any route.

**Decision: no destructive `--force` was shipped.** The opt-in path is
`--heal`, an additive merge -- it only ever ADDS a manifest key the pack does
not already have, from an explicit allowlist, and the value still comes from
`build_runpack_docs` (nothing is hand-authored). It never overwrites and never
deletes. Rationale is recorded inline in `sync_v3_results.py` so the next reader
does not "simplify" it back into a regeneration. Default (no-flag) behaviour is
unchanged, which `governance.sh:244` and the hub `sync_daemon` depend on.

## 2. Scope A -- always-core keys (LANDED)

Allowlist: `recording_schema`, `elapsed_seconds`, `config`, `seeds`.

- **1012 packs** gain at least one key; **2286 keys** added total
  (`config` 719, `seeds` 601, `elapsed_seconds` 548, `recording_schema` 418).
- **0 existing-value conflicts** -- every one of these is an add onto an absent
  key, so additive mode loses nothing.

**Scoring impact: none, and this is checked rather than assumed.**
`build_experiment_indexes.py` contains **zero** references to `recording_schema`,
`elapsed_seconds` or `seeds`, and makes no manifest read of `config`. The heal
changes each pack's self-description and its `validate_recording.check_manifest`
verdict, and cannot move a score.

**`substrate_hash` and `machine_class` are deliberately EXCLUDED** even though
they are also always-core. The indexer *does* read both (17 and 18 references --
the SD-024 gate class and the arm-fingerprint reuse key), so backfilling them is
a scoring change that needs its own measurement and its own governance
disposition. 56 packs would gain each; that is left unqueued here, not done
quietly as part of this.

## 3. Scope B -- metrics.values fill (PARTIALLY HELD)

28 packs would go from `values == {}` to populated. Two scoring surfaces open up
for those runs, and both were simulated against the real `stop_criteria.v1.yaml`.

### 3a. `fail_if` stop thresholds -- 0 flips

For each of the 28, the applicable merged criteria were evaluated against the
newly-populated numeric metrics and `final_status` recomputed per
`_evaluate_runs`. **No run changes `final_status`.**

The reason is structural, not luck: the only `default` rule is
`fatal_error_count > 0`, and the six per-experiment blocks
(`trajectory_integrity`, `claim_probe_mech_062/arc_017/mech_064/mech_065`,
`meta_invariant_compression_audit`) match none of the 28 experiment types. No
newly-gained metric is named by any applicable rule.

Note this direction is one-way regardless: filling metrics can only ever turn
PASS -> FAIL via a `fail_if` hit; it can never rescue a FAIL, since
`manifest_fail` is evaluated independently.

### 3b. Duplicate-emission supersession -- 2 clusters, HELD

`_detect_and_mark_duplicate_emissions` cannot fingerprint a run with no numeric
metrics, so filling `values` newly exposes these runs to it. Simulation found
**2 new clusters that would actually take effect** (neither experiment_type has a
hand-resolved run, so the back-off does not apply):

| experiment_type | runs (earlier -> superseded) | queue_id |
|---|---|---|
| `v3_exq_170_q002_r_field_resolution_pair` | `..._20260329T213812Z_v3` superseded by `..._20260330T070234Z_v3` | `''` (blank) |
| `v3_exq_171_mech033_kernel_chain_pair` | `..._20260329T213946Z_v3` superseded by `..._20260330T070404Z_v3` | `''` (blank) |

Both look like genuine byte-identical re-emissions a day apart, which is exactly
what the detector exists to catch -- but auto-marking `evidence_direction:
superseded` is an evidence verdict change, and the chip's own instruction is to
stop and route a flip through `/governance` rather than land it as housekeeping.

**Held: the 4 run_ids in those 2 clusters are excluded from the fill.** The
other **24** fills land, since they have no scoring consequence on either surface.

Both clusters carry a **blank `queue_id`**, so they group only with other blanks
-- worth `/governance` confirming the supersession is real before it is enabled,
because a blank-queue_id grouping is the weakest form of the identity match that
`_detect_and_mark_duplicate_emissions` documents as load-bearing.

## 4. What a future session should pick up

1. `/governance` disposition on the 2 duplicate-emission clusters in 3b; if
   accepted, re-run the heal without `--exclude-run-id` for those 4 runs.
2. `substrate_hash` / `machine_class` backfill (56 packs each) -- scoring-relevant,
   unmeasured here.
3. The 1293 packs with no reachable flat source are unreachable by this route
   entirely and need a different one if their always-core gap matters.
