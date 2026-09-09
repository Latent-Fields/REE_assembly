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
   unmeasured here. **DONE 2026-09-09: measured and landed, zero scoring impact --
   see sec 5.** The deferred skip-dirty packs are also cleared -- see sec 6.
3. The 1293 packs with no reachable flat source are unreachable by this route
   entirely and need a different one if their always-core gap matters.
   **Still open; scoped (not attempted) in sec 7.**

---

## 5. Scope C -- `substrate_hash` / `machine_class` (MEASURED, LANDED)

- Date: 2026-09-09T06:32:57Z
- Session: `wizardly-meninsky-e6c09c` (chip `chip-20260909-heal-substrate-hash-machine-class`)
- Follows sec 2's deliberate exclusion and sec 4 item 2.

**Verdict: zero scoring impact. Landed as housekeeping; no `/governance` route needed.**
No claim confidence, gate verdict, status, evidence direction or recommendation moves.

### 5a. Why the exclusion premise did not survive measurement

Sec 2 excluded these two because `build_experiment_indexes.py` references them
(17 and 18 times) where it references the other four zero times. Reference
*count* turned out to be the wrong test. Reading the reference *sites*:

- **`build_experiment_indexes` already backfills both onto the pack itself**, from
  the SAME flat sibling this heal reads, unconditionally and independently of the
  governance annotation gate -- `_FLAT_PROVENANCE_BACKFILL_FIELDS`
  (`machine`, `machine_class`, `substrate_hash`, `z_goal_stream`,
  `substrate_commit`, `substrate_commit_unavailable`,
  `enabled_default_off_flags`), added 2026-07-16 for exactly the whitelist gap
  this heal closes at the source. So the index has been reading these values all
  along; the heal only stops them being borrowed.
- Of the remaining sites, **none is a comparison, grouping or gate**: they are the
  `RunRecord` dataclass fields, the `_parse_run_manifest` reads, and two
  emit-into-the-index sites (`entry[...] = run.substrate_hash` and the unlinked-run
  equivalent). The indexer's own comment says it: "surfaced for queryability, NOT
  scored", and both fields are absent from `_FLAT_DIRECTION_FIELDS`.
- **The arm-fingerprint reuse key is a different field.** `arm_fingerprint_index.json`
  keys on `arm_results[].arm_fingerprint.machine_class` -- NESTED inside each arm
  cell, not the top-level manifest key. The heal never touches `arm_results`.

### 5b. Resolver and value equivalence (static, all 56 packs)

The static argument only holds if the heal and the indexer source from the same
flat file and agree on the value. Both were checked exhaustively, not sampled:

| Check | Result |
|---|---|
| `_resolve_flat_sibling` (indexer) vs `_derive_experiment_type_and_dir` (heal) pick the same flat file | **56/56 identical** |
| Value written by heal (`build_runpack_docs`) == value indexer already read (post-backfill) | **112/112 identical** (56 packs x 2 keys) |
| Flat siblings at top level vs subdirectory | 56/56 top level, 0 subdirectory |
| Flat value "absent" (indexer backfill would have skipped) | 0 |

The top-level/subdirectory split matters for a second consumer:
`generate_canonical_readiness.py` globs only `evidence_dir/*.json` for its flat
half, so a subdirectory-only flat would have been invisible to it and the heal
WOULD have moved its counts. There are none, so it does not.

### 5c. Other consumers (none affected)

| Consumer | Reads | Affected |
|---|---|---|
| `generate_canonical_readiness.py` | flat + pack field-level merge, flat fills what the pack lacks | no -- all 56 flats are top-level, already merged in |
| `check_substrate_staleness_candidates.py` | `load_flat_claim_tagged_manifests` -- FLAT only | no |
| `generate_experiment_profile.py` | `flat.get("substrate_hash")` | no |
| `reanalysis_query.py` | read-only query tool, writes no derived artifact | no |
| `arm_reuse_determinism_check.py` | nested `arm_fingerprint`, not the top-level key | no |
| `derived_evidence_db.py` | `RunRecord` attributes -- i.e. post-backfill values | no |

### 5d. Empirical pre/post rebuild, against a run-to-run noise control

Static reasoning was not trusted on its own. A full `build_experiment_indexes.py`
rebuild was run over an isolated copy of the corpus (`--root` at a scratch mirror
of `evidence/`, 23,186 files), healed and unhealed.

**The control matters and is the part to keep if this is ever re-run.** Two
identical back-to-back rebuilds with NO input change are not byte-identical:
recency-weighted confidences decay with wall-clock, so 11 derived artifacts
differ every time, with ~100-200 float changes of magnitude <= 0.001 and
occasional prose `confidence_rationale` strings echoing a rounded value. A naive
pre/post diff therefore shows changes whether or not the heal did anything. Every
number below is stated against that control.

| Comparison | Derived artifacts changed | Interpretation |
|---|---|---|
| healed -> healed (pure noise) | 11 | the floor |
| healed -> unhealed (the effect) | **11 -- the same 11, none added** | indistinguishable from the floor |

Row-level, on the derived `evidence.sqlite`:

- **`runs` table: NO column differs at all** -- healed vs unhealed. This is the
  direct confirmation, since `substrate_hash` / `machine_class` live in that table.
- `claim_rollup`: only decaying posterior blobs, plus one claim (`MECH-436`)
  whose `experimental_confidence` moved 0.597 -> 0.596. **`MECH-436` is tagged by
  none of the 56 healed runs**, so the heal cannot reach it -- decay, not effect.
  No `status`, count, or `n_entries` column differs anywhere.
- For the **27 claims** the 56 healed runs actually tag: the only differing columns
  are `lit_posterior_json` / `exp_posterior_json` at the 4th decimal. Every
  `n_entries` identical.
- For the **91 `entries` rows** belonging to the healed runs: **0 columns differ.**
- `arm_fingerprint_index.json`: **hash-identical** (`ec9a0377f941d6b2...`).
- The five prose artifacts (`TODOs.md`, `conflicts.md`,
  `promotion_demotion_recommendations.md`, `ARCHITECTURE_GAP_REGISTER.md`,
  `DORMANT_HIGH_CONFLICT_WATCHLIST.md`): **0 changed lines** once the `Generated:`
  stamp is excluded. Neither field appears in any of them.

### 5e. What was landed

`HEAL_MANIFEST_KEYS` extended to six members; the inline rationale above it
rewritten to record *why* the two were cleared, so the exclusion is not
reinstated from the reference count alone.

- **56 packs** gained `substrate_hash` + `machine_class` (112 keys).
- **1 pack** (`v3_exq_822f_sd082_candidate_discriminating_init_head_control_20260908T231145Z_v3`,
  newly converted since sec 2) gained the original four always-core keys.
- Additivity re-verified on the real repo against `HEAD`: every one of the 57
  differs from its committed copy by key ADDITIONS drawn from the allowlist only
  -- no key removed, no value changed.

**Benefit, stated honestly:** because the indexer already backfills, this does not
make the index more correct today. What it does is make each pack
**self-describing** rather than dependent on its flat sibling remaining
reachable -- which matters directly given sec 4 item 3, where 1293 packs have no
reachable flat and would have no backfill source at all if flats were ever pruned.

## 6. Sec 4 item 2 (deferred skip-dirty packs) -- CLEARED

Sec 3's heal deferred packs a concurrent `/governance` session had uncommitted.
Those are now committed, and the re-run cleared the remainder:

- `v3_exq_1015_mech465_zworld_warmup_budget_dispersion_sweep_20260908T202858Z_v3` --
  already healed by an intervening run; nothing owed.
- `v3_exq_1014_ext002_lineage_e3_latching_repertoire_spike_20260908T223415Z_v3` --
  `metrics.values` fill landed (6 keys: `casualty_latched_fraction`,
  `latched_fraction`, `latched_x_died_2x2`, `latching_dominant`,
  `per_seed_latched`, `per_seed_top_class`).

This is a scope-B (scoring-relevant) fill, so it was re-measured rather than
assumed from sec 3: on the isolated mirror it changed **no** `final_status`,
produced **byte-identical dedup-guard output** (no new duplicate-emission
cluster), and left every `status` / `evidence_direction` / `outcome` column in
the derived DB unchanged corpus-wide. Its one derived effect is its own
experiment `INDEX.md`, which now shows the metrics -- the intended benefit.

The **4 run_ids in the 2 held clusters of sec 3b remain excluded** and are still
owed a `/governance` disposition. They were passed as explicit
`--exclude-run-id` arguments, not left to chance.

## 7. Sec 4 item 3 (1293 flat-less packs) -- SCOPED, NOT ATTEMPTED

Unchanged by this session and deliberately not attempted. Scoping note for
whoever picks it up: no flat-sourced heal can ever reach these, because
`heal_pack` derives every value from `build_runpack_docs(flat)`. The three
candidate routes, none costed here:

1. **Accept the gap.** These are the oldest packs; their always-core fields were
   never recorded at source, so there is nothing to recover -- the gap is a true
   negative, not a mapping loss. Cheapest, and probably correct for most of them.
2. **Recover from a sibling run** in the same experiment_type that DOES have a
   flat, for the fields that are constant across a run group (`machine_class`,
   `substrate_hash`). This INFERS rather than records, so it would need a distinct
   provenance marker; do not let an inferred value become indistinguishable
   from a recorded one.
3. **Recover from the coordinator DB / git history** for runs whose flat was
   deleted rather than never written. Determining which of the 1293 those are is
   itself the first task.

Route 1 needs a decision, not a build; routes 2 and 3 need the count split first.
