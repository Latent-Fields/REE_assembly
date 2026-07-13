# pack_writer Single-Writer Migration Plan (chokepoint fix)

**Status:** IN PROGRESS (v0.4). Authored 2026-07-12; step 3 F-pilot + batch 1 (98 scripts) LANDED 2026-07-12 (ree-v3 main `d88c373`); step 3 batch 2 (135 scripts: local-run_id + write_text-manifest + default=str) LANDED 2026-07-12; step 3 batch 3 (247 scripts: with-open/dir-var name mismatch + non-adjacent out_path + non-`manifest`-var flat manifests + 5 onboard_smoke exempts) LANDED 2026-07-12 (ree-v3 main `e854b5c`); step 3 batch 4 (145 scripts: provably-safe idioms -- with-open `encoding=`/`.open()` spelling + `os.path.join` path + per-mvar run_id key + write_text `default=str` + Path-import guard + multi-write-site refusal) LANDED 2026-07-12 (ree-v3 main `681f490`); step 3 batch 5 (15 scripts: the non-canonical-filename class -- AST proof that the literal/`%s`/`{TYPE}_{ts}_v3` filename provably equals `f"{run_id}.json"`, write-only-rewrite with the original out_dir sub-expression; 69 of the 84 correctly REFUSED as genuine renames) LANDED 2026-07-12 (ree-v3 main `ae74b63`); step 3 **edge-case-A HYBRID** (276 scripts: 267 archival `MANIFEST_WRITER_EXEMPT` + 9 active corrected-and-routed; the `{TYPE}_{ts}.json` `result`-var `detect_manifest_var`→None class) LANDED 2026-07-12 (ree-v3 main `7b8c150`); step 3 batch 6 (9 scripts: the `no out_dir assignment` param-dir class via a `dir_bound_as_param` migrator generalization [8: `621`/`621a`/`622`/`626`/`626a`/`626b`/`636`/`637`] + `354` real-branch hand-migration; `540f` dropped to the concurrent 69-rename HYBRID, `241a`/`241b`/`247` refused as pack-subdir rename/relocate) LANDED 2026-07-13 (ree-v3 main `bf7724a`); step 3 **batch-5 non-canonical genuine-rename HYBRID** (69 scripts: the `detect_manifest_var` SUCCEEDED but the filename is not provably `== f"{run_id}.json"` class -- `{TYPE}_{ts}` missing `_v3` / `manifest.json` pack-style / `{run_id}_manifest.json` / filename-var / `ts`-`ts_utc`-order mismatch; classified **all 69 ARCHIVAL, ZERO active** -> `MANIFEST_WRITER_EXEMPT`; disjoint from the edge-case-A HYBRID [`detect_manifest_var`->None] by construction) LANDED 2026-07-13 (ree-v3 main `acd1a50`); step 3 **RUNID_only var-identity** (12 scripts: the `detect_manifest_var`->None class that ALREADY writes canonical `{run_id}.json` -- generalized `detect_manifest_var` to prove a non-dict-literal manifest var [assembled via literal/AnnAssign+subscript+`.update`, or a helper-return binding] carries run_id+arch+resolvable-status; routed the 12 byte-safe, honestly REFUSED the other 10 of 22 [8 no resolvable status, 2 non-canonical dir]) LANDED 2026-07-13 (ree-v3 main `31eb700`); step 3 **no-canonical-with-open HYBRID** (3 scripts: the migrator's `no canonical with open(<path>) above dump` refusal class -- early-era self-packing writers that dump the identity manifest to a pack-subdir `runs/<run_id>/manifest.json` path [not a flat `<run_id>.json`], `241a`/`241b` + a `<TYPE>_output.json` runner pointer, `247` no flat sibling at all; routing would relocate/rename -> classified **all 3 ARCHIVAL, ZERO active** [not queued, last run 2026-04 ~96d ago] -> `MANIFEST_WRITER_EXEMPT`) LANDED 2026-07-13; step 3 **RUNID_only no-resolvable-status HYBRID** (8 scripts: the RUNID_only var-identity batch's 8 honest refusals `028`/`212`/`255`/`256`/`407`/`470`/`470a`/`479` -- already write canonical `{run_id}.json` but carry `final_verdict`/`pass`/`verdict`/`passed`, NOT `status`|`outcome`|`overall_outcome`, so `write_flat_manifest` would raise on its status guard; classified **all 8 ARCHIVAL, ZERO active** [not queued, last run 79-114d ago] -> `MANIFEST_WRITER_EXEMPT`) LANDED 2026-07-13 (ree-v3 main `5c20b42`). Cumulative: **670 of 1028 scripts** now route through `write_flat_manifest` (+ **354** `MANIFEST_WRITER_EXEMPT`; migrator unmatched 402->8). step 3 **683/686 no-run_id non-canonical-dir HYBRID** (2 scripts: the last `no json.dump(manifest` NOT-byte-safe residual `683`/`686` -- both write `result` [a `run_experiment()` return with `architecture_epoch`+`outcome` but NO `run_id` key] to a single hardcoded relative f-string `../REE_assembly/evidence/experiments/{run_id}.json`, so routing is a correct-and-route [inject run_id + split dir], not byte-safe; classified **both ARCHIVAL, ZERO active** [not queued, never ran, substrate-blocked proxies] -> `MANIFEST_WRITER_EXEMPT`; empirically NOT lint-flagged [the STRING `"run_id"` is absent -> `manifest_writer_lint` never fired], so the exempt is inert w.r.t. the lint, its real effect migrator unmatched->skip; **this CLEARS the lint-flagged migration backlog** -- the residual 8 unmatched are all emit-only/harness with no raw flat-manifest `json.dump`, not lint-flagged) LANDED 2026-07-13. §7.4 elapsed_seconds retrofit (68 batch-1/2 scripts `47ed14a`; +35 batch-3 scripts `d57e893`, 103 total) landed in parallel. §7.4 batch-4 pass (2026-07-12, session `optimistic-babbage-363511`): **0 of the 145 batch-4 scripts eligible -- all 145 are by-design advisory gaps, no code change** (batch 4 is the older-era grab-bag that structurally predates the retrofit's `args = parser.parse_args()` + `datetime.now(timezone.utc)` in-function idiom); retrofit cumulative stayed **103**. §7.4 batch-5 pass (2026-07-13, session `pack_writer §7.4 batch-5 elapsed retrofit`, ree-v3 main `a442440`): **1 of the 15 batch-5 scripts eligible (527); the other 14 stay by-design advisory gaps** (2 no unaliased `timezone` import [`526` has `datetime` only], 5 no argparse at all, 7 scope-split like batch-4's 705/706); retrofit cumulative **104**. §7.4 batch-6 pass (2026-07-13, session `pack_writer §7.4 batch-6 elapsed retrofit`, NO ree-v3 commit): **0 of the 9 batch-6 scripts eligible -- all 9 stay by-design advisory gaps** (5 scope-split -- `parse_args` in the module `if __name__` guard while the write is inside `emit_manifest()` [`621`/`621a`/`622`/`626`/`626a`]; 3 import `datetime` only, no unaliased `timezone` [`626b`/`636`/`637`]; 1 imports `datetime as dt_mod` aliased [`354`]); `--apply` a verified no-op; retrofit cumulative stays **104**. §7.4 batch-7 pass (2026-07-13, session `pack_writer §7.4 batch-7 elapsed retrofit` [`nice-grothendieck-f7b58b`], NO ree-v3 commit): **0 of the 12 RUNID_only-batch scripts eligible -- all 12 stay by-design advisory gaps** (10 import `datetime` only, no unaliased `timezone` [`568`/`588c`/`588d`/`588e`/`669b`/`670`/`688`/`688a`/`730`/`731`]; 2 scope-split with `datetime`+`timezone` present -- `596` `parse_args` in `main()` while wfm in `run_experiment()`, `615` both under the `if __name__` guard so the anchor is nested in an `If` [0 direct anchors]); `--apply` a verified no-op; retrofit cumulative stays **104**.
**Closes:** the "no single enforcement chokepoint" gap named in the Experimental Recording Standard [`experimental_recording_standard_2026-07-12.md`](experimental_recording_standard_2026-07-12.md) §4.
**Owns:** making `ree-v3/experiments/pack_writer.py` the mandatory single manifest writer across the experiment corpus, incrementally, without breaking the flat -> sync -> pack -> indexer chain.
**Sibling:** [`arm_reuse_fingerprint_plan.md`](arm_reuse_fingerprint_plan.md) (the arm-reuse fingerprint is the readout-reuse instance of the same over-record principle).

This is a **multi-session** effort. This doc is the resume primitive — the staged migration table in §6 is the cross-session state.

---

## 1. The problem (restated from the standard §4)

The always-record core (`recording_schema`, `substrate_hash`, `machine`/`machine_class`, `elapsed_seconds`, `config`, `seeds`) can only be *guaranteed* if every manifest passes through one enforcement point. The 2026-07-12 audit found there is none:

- **1,028** experiment scripts write a run manifest; **0** route through the sanctioned writer. `ExperimentPackWriter`/`write_pack` is referenced only by `pack_writer.py` itself and `run.py`; `stamp_recording_core` is called by **no** experiment script. Every one of the 1,028 hand-builds a dict and `json.dump`s it.
- So the always-core is authoring-time discipline with no mechanical floor — exactly the recording-debt the standard closes (0% of flat manifests carry a `substrate_hash`, which is *the* reason no historical baseline can be safely reused).

---

## 2. How the pipeline actually runs (terrain the fix must not break)

```
experiment script (ree-v3/experiments/*.py)
  -> hand-built FLAT manifest -> REE_assembly/evidence/experiments/<run_id>.json
  -> experiment_protocol.emit_outcome(manifest_path=<flat path>)  [sentinel, not the bytes]
       -> runner -> coordinator_client.report_result() -> POST /result (bytes VERBATIM)
            -> coordinator manifest_spool (verbatim) -> sync_daemon.phase3_git_writer
                 -> commits FLAT bytes to evidence/experiments/<run_id>.json  ("phase3:")
                 -> (opt) _materialize_runpacks() -> sync_v3_results.runpack_for_flat
       (Mac/local path: script writes flat straight into REE_assembly; governance.sh
        later runs sync_v3_results.py -- same field mapping either way)
  ---------------------------------------------------------------------------
  sync_v3_results.build_runpack_docs  (THE single flat->pack converter; used by
     BOTH governance.sh locally AND the coordinator phase3 writer)
       -> evidence/experiments/<type>/runs/<run_id>/{manifest.json, metrics.json, summary.md}
  ---------------------------------------------------------------------------
  build_experiment_indexes.py  scores the PACK, then overlays flat governance fields
     (_merge_flat_manifest_overrides keyed on evidence/experiments/<run_id>.json)
```

**Five flat-manifest consumers** (each a hard constraint):

1. **`sync_v3_results.build_runpack_docs`** — the flat->pack converter. An **allowlist mapper**: reads `run_id`(required, KeyErrors if absent), `architecture_epoch`, status (from `status`|`overall_outcome`|`outcome`), timestamp (`run_timestamp`|`timestamp_utc`|`timestamp`), claims (`claim_ids`|`claim`), `evidence_direction`, `evidence_direction_per_claim`, `experiment_purpose`, `interpretation` (whole block), `metrics` -> `values`. **Drops** everything else (`arm_results`, `per_seed`, `non_degenerate`, `config`, `seeds`, `substrate_hash`, `label_balance`).
2. **`build_experiment_indexes.py`** — scores the pack, but for each run also reads the flat sibling `base_dir/<run_id>.json` and overlays `_FLAT_AUTHORITATIVE_FIELDS` (evidence_direction[/_per_claim/_note], `non_degenerate*`, `degeneracy_reason`, `superseded_by*`, `pending_retest_after_substrate*`, `substrate_hash`, `label_balance`) when the flat copy is annotated. **The flat file is authoritative for governance corrections** (`/failure-autopsy` edits it; 2026-06-14 mis-scoring incident).
3. **`serve.py` explorer** — `/api/experiment/detail` prefers the flat manifest and renders **every** top-level key via a catch-all (so `arm_results`/`interpretation`/`per_seed` surface from the flat file; they are not in the pack).
4. **`generate_pending_review.py`** — scans flat `*.json` for the `dry_run` exclusion set + PASS/FAIL.
5. **`scan_flat_vs_runs_direction_mismatch.py`** — pairs flat<->pack on `run_id`/`experiment_type`.

**Hard constraints a writer change MUST preserve** (see the constraints list in §2 sources):
- Flat path = `evidence/experiments/<run_id>.json`, keyed by the **exact** `run_id` string. Move it and every flat-only governance correction is silently ignored.
- `run_id` mandatory, ends `_v3` (or mid-string `_v3_<ts>`); `architecture_epoch == "ree_hybrid_guardrails_v1"`. Both gate `sync_v3_results._is_flat_v3`; miss either => no pack => never scored.
- Status resolvable from `status`|`overall_outcome`|`outcome`; timestamp from `run_timestamp`|`timestamp_utc`|`timestamp`; claims from `claim_ids`|`claim`. **Do not rename these.**
- Rich/extra fields (`arm_results`, `per_seed`, `interpretation`, experiment-specific keys) must stay on the flat file — a writer that strips unknown fields blanks the explorer detail and the adjudication overlay.
- Coordinator stores manifest bytes **verbatim** — the writer's output *is* what lands at the flat path; the pack is a pure re-derivation.
- `dry_run` top-level flag must survive; filename must not collide with the SKIP-name plumbing files.

Two independently-hardcoded copies of the same pack skeleton exist (`sync_v3_results.build_runpack_docs` and `pack_writer.write_pack`) — a drift source. A golden byte-shape test (`ree-v3/coordinator/test_phase3_runpack_materialize.py`) pins sync's output.

---

## 3. Decision (2026-07-12, user-confirmed): **author-side flat chokepoint**

Rejected: "scripts emit the pack shape directly via `write_pack`, deprecate flat + sync." It would rewire the explorer (reads flat), the coordinator `/result` (stores flat bytes), `emit_outcome` (flat sentinel), and — fatally — the `/failure-autopsy` flat-governance-correction overlay (documented "flat copy is authoritative"). High blast radius, breaks a live governance mechanism.

**Adopted:** ONE validated flat-manifest writer that scripts call in place of a raw `json.dump`. It stamps the always-core (via `stamp_recording_core`), enforces the identity invariants, preserves the corpus's field *names* verbatim, and writes to the exact flat path. Every downstream consumer is untouched. Incremental, low blast-radius, multi-session-friendly. `pack_writer` becomes the single **authority** for manifest emission (flat writer for scripts + `write_pack` for `run.py`); `sync_v3_results` remains the single flat->pack converter.

---

## 4. Landed this session (2026-07-12)

Purely additive + inert until adopted (no existing script changed), so landed direct to `ree-v3` main. Gate: `pytest tests/` — **861 passed**, plus the two directly-relevant suites (`tests/contracts/test_recording_standard.py` + `test_arm_fingerprint_lint.py`) green. One pre-existing unrelated failure (`test_runner_fail_branch_persists_result.py::test_c3_error_branch_manifest_guard_gated_on_output_file`, `assert -1 != -1`) fails identically with these changes stashed and references neither changed module — not introduced here.

1. **`experiments/pack_writer.write_flat_manifest(manifest, out_dir, *, dry_run, config, seeds, script_path, machine, elapsed_seconds, started_at, stamp, overwrite_core, require_v3)`** — the chokepoint. Validates `run_id`/`_v3` + `architecture_epoch` (default-fills) + resolvable status + SKIP-name collision; calls `stamp_recording_core` **after** the manifest (so a multi-arm run hoists `substrate_hash` from the per-cell fingerprints); does **not** reshape field names or strip rich fields; writes `<out_dir>/<run_id>.json` (`_dry_` prefix under `dry_run`); returns the Path for `emit_outcome`.
2. **`validate_experiments.manifest_writer_lint`** — AST lint: a script that carries manifest-identity tokens (`run_id` + `evidence_direction`) and does a raw `json.dump`/`json.dumps`, without routing through `write_flat_manifest`/`write_pack`/`ExperimentPackWriter`, is flagged. **HARD under `--paths`** (the `/queue-experiment` Step 3.5 authoring path — a NEW script is blocked), **advisory in full-glob** (grandfathers the 1,028-script backlog; never flips the exit code). Opt-out: `MANIFEST_WRITER_EXEMPT = "<reason>"`. Wired automatically — `/queue-experiment` already runs `validate_experiments.py --strict --paths <script>`.

Net effect: **new** scripts are forced onto the chokepoint from now on; the backlog migrates incrementally without ever breaking CI or a full sweep.

---

## 5. pack_writer field-coverage gap (survey, step 2)

The corpus's hand-rolled field names diverge from `pack_writer.write_pack`'s parameters. The **flat chokepoint sidesteps this** (it preserves names verbatim), so `write_flat_manifest` needs **no** new field parameters — it passes the whole dict through. The coverage gap only bites the *pack* path (`write_pack`) and the *sync converter*, which is the §7 unification follow-up, not a blocker for migration.

Recurring hand-rolled fields with no home in `write_pack`'s typed signature (approx script-counts):

| Field | ~scripts | Where it must live |
|---|---|---|
| `claim_ids` (not `claim_ids_tested`) | 1010 | flat verbatim; sync maps -> `claim_ids_tested` |
| `experiment_purpose` | 712 | flat + sync (already carried) |
| `outcome` (parallel to `status`) | 702 | flat verbatim; sync resolves status |
| `queue_id` | 399 | flat verbatim |
| `evidence_direction_per_claim` | 388 | flat + sync (already carried) + overlay |
| `supersedes` | 348 | flat verbatim |
| `criteria` | 345 | flat verbatim (summary derivation) |
| `interpretation{preconditions,criteria_non_degenerate,label}` | 253 | flat + sync (whole block) + adjudication |
| `arm_results` / `per_arm` | 197 / 30 | flat verbatim (explorer catch-all) |
| `evidence_direction_note` | 189 | flat + overlay |
| `per_seed_results` / `per_seed` | 189 / 138 | flat verbatim |
| `non_degenerate` / `degeneracy_reason` | 78 / 64 | flat + overlay |
| `label_balance` | (047m fix) | flat + overlay |

**Consequence for §7:** to make the always-core survive into the *pack* (so the indexer can eventually score on it), `sync_v3_results.build_runpack_docs` must be extended to carry `substrate_hash`/`config`/`seeds`/`machine`/`elapsed_seconds` and the rich governance fields — and, to kill the drift, `build_runpack_docs` and `pack_writer.write_pack` should delegate to ONE shared skeleton. That is deferred (changes the golden byte-shape test + touches the coordinator writer).

---

## 6. Staged migration backlog (step 3 — future sessions)

**Process constraint (mandatory):** editing an existing `v3_exq_*.py` experiment script goes through the `/queue-experiment` skill (root CLAUDE.md "Mandatory skill path"). A **batch mechanical migration** (swap the `json.dump` tail for `write_flat_manifest`, no logic change) is the efficient path but needs explicit user sanction to run outside the skill, and must be staged on an `integration/<slug>` branch off `ree-v3` main with `pytest tests/` as the merge gate (root CLAUDE.md code-plane policy). Migrate **most-common-shape-first**; verify each batch produces a byte-compatible flat manifest (same keys, plus the always-core) and that `sync_v3_results` + the indexer still score it.

### Progress — step 3, session 2026-07-12 (F pilot + batch 1 LANDED, ree-v3 main `d88c373`)

**Key correction to the family framing below.** "A+B+I = 672, one backbone" is a
*manifest-shape* clustering, NOT a single migratable *tail*. A precise per-script tail
survey (via the migrator, `ree-v3/tools/migrate_manifest_writers.py`) found only **98**
scripts across ALL families share the exact canonical tail that is safe to auto-migrate:
```
out_path = out_dir / f"{manifest['run_id']}.json"     [+ optional `_dry_` branch]
with open(out_path, "w") as f: json.dump(manifest, f, indent=2[, sort_keys=True])
```
So the batch is **tail-shape-first, not family-first.** The other ~940 need per-class
transforms (broadening taxonomy below).

**Landed (ree-v3 main):**
- **F pilot (4): 734/735/736/737** — commit `8f7ee9d`. Fully verified: dry-run smoke
  (737+734 ran clean), `validate_experiments --strict --paths` (0 manifest-writer-backlog),
  `validate_recording --strict` (always-core complete), `sync_v3_results.runpack_for_flat`
  -> valid pack with status resolved, indexer unaffected (sync mapper drops the always-core
  extras as designed; flat file keeps them for the overlay). `substrate_hash` now populated
  (was 0% of flat manifests). Pilot surfaced two per-script gaps folded into the recipe:
  (a) the sweep family carries config under `config_summary`, not `config` -> pass
  `config=manifest.get('config') or manifest.get('config_summary')`; (b) `elapsed_seconds`
  needs a `_run_started = datetime.now(timezone.utc)` timer at main entry + a
  `(now - _run_started).total_seconds()` arg (only 737 had it).
- **Batch 1 (98 canonical-tail): commit `0f153a4`** — applied by the migrator (validated
  byte-equivalent against the pilot hand-edit; caught 2 real tool bugs first: replacement
  indent used the json.dump BODY level -> IndentationError; import inserted inside a
  multi-line `import (` -> SyntaxError). **SAFE BY CONSTRUCTION:** the generated call
  references only names the original tail already used (`manifest`, `out_dir`, the dry cond)
  plus the module-level `SEEDS` global. All 98 py_compile clean; `pytest tests/` 1414 passed
  0 failed; non-conforming DROPS 155->59 vs origin/main baseline (fixes ~96 manifest-writer
  non-conformances, 0 new; the 59 remaining are pre-existing orthogonal degeneracy/readiness
  backlog, out of scope). `elapsed_seconds` NOT retrofitted in batch 1 (needs the per-script
  timer) -> these gain 6/7 always-core incl. substrate_hash; **elapsed retrofit is a
  follow-up** (see §7.4).
- Migrator tool committed `d88c373` at `ree-v3/tools/migrate_manifest_writers.py` (the
  resume primitive: `python3 tools/migrate_manifest_writers.py --report experiments/v3_*.py`).

**Broadening taxonomy for the next batches (precise per-tail counts, 1038 scripts scanned):**

| Unmatched class | ~count | Broadening needed | Risk |
|---|---|---|---|
| no `json.dump(manifest` — writes via `.write_text(json.dumps(<var>))`, var often `result` not `manifest` (early-era 001/002/003...) | 569 | accept `.write_text(json.dumps(X))` + non-`manifest` var, after verifying X is the manifest dict | med (var identity) |
| non-canonical out_path `out_dir / f"{run_id}.json"` (run_id LOCAL var) | subset of 221 | accept local `run_id` (== `manifest['run_id']` by construction) | low — do FIRST |
| non-canonical out_path `out_dir / f"{TYPE}_{ts}.json"` (early-era filename, edge-case A) | subset of 221 | correct `run_id`/out_dir first, or `MANIFEST_WRITER_EXEMPT` | high — RENAMES the flat file |
| no canonical `with open(out_path)` above dump | 100 | different write idiom | med |
| with-open path/handle name mismatch | 37 | generalize path/handle names | low |
| `json.dump(manifest` not `indent=2` (uses `default=str`) | 7 | `write_flat_manifest` has NO `default=str` -> clean the manifest OR extend the writer | med |

Recommended next-session order: the low-risk local-`run_id` sub-class first (broaden
`PRIMARY_RE`), then the `.write_text(json.dumps(result))` early-era class (with the
edge-case-A filename correction), then `default=str`. Re-run the migrator `--report` after
each broadening to re-measure.

### Progress — step 3 BATCH 2, session 2026-07-12 (135 scripts LANDED, ree-v3 main)

Migrator broadened **most-common-shape-first, lowest-risk-first** across three classes
(each validated byte-equivalent against a hand-migration diff, py_compile clean, and
`validate_experiments --strict --paths` with **0 new** non-conformances vs the origin/main
baseline + 0 manifest-writer-backlog). **Total 135 scripts** migrated this batch. Full
`pytest tests/` = **1413 passed, 1 pre-existing unseeded-stochastic flake**
(`test_scaffolded_sd054_onboarding.py::test_c12_build_env_hazard_spawn_in_reef_half_optional`
— 40 unseeded random hazard spawns asserting >=1 in the reef half; **passes in isolation**,
order/global-RNG dependent, orthogonal to the mechanical write swaps). The three suites that
directly exercise the change (`test_recording_standard` + `test_arm_fingerprint_lint` +
`test_arm_reuse`/indexer) = 44 passed. (Worktree note: `test_arm_reuse` computes the indexer
path as `<ree-v3-parent>/REE_assembly/...`; from a `.claude/worktrees/` worktree that needs a
`.claude/worktrees/REE_assembly` symlink to the real checkout, else 6 FileNotFound *errors*
unrelated to any code — with the symlink all 24 pass.)

1. **Local-`run_id` out_path (65 scripts).** Broadened `PRIMARY_RE`/`DRY_REASSIGN_RE` to accept
   `out_dir / f"{run_id}.json"` (local var) in addition to `{manifest['run_id']}`. **Safety
   guard** added: the bare-`run_id` form is accepted ONLY when the manifest sets
   `"run_id": run_id` (new `runid_is_manifest_runid`), proving the recomputed
   `out_dir / f"{manifest['run_id']}.json"` is byte-identical. All 65 carried that field (0
   guard rejections). Non-conforming 145->82 on the set (63 manifest-writer findings fixed).
2. **`write_text(json.dumps(manifest))` idiom (65 scripts).** Added `WRITETEXT_RE` as an
   alternative single-line write statement (`out_path.write_text(json.dumps(manifest, indent=2)
   [ + "\n"][, encoding="utf-8"])`) — restricted to the `manifest` var (same identity guarantee
   as the `json.dump(manifest` tail) and `path == out_path`. Correctly SKIPS multi-manifest
   writers (write to `manifest_path`, not `out_path`, e.g. 540f/540g) and non-adjacent out_path
   (e.g. 620). Non-conforming 70->10 on the set.
3. **`default=str` (5 scripts: 570/571/572/609/618).** Extended the writer, not the manifest:
   `write_flat_manifest` gained an optional `json_default: Optional[Callable] = None` param
   threaded into the final `json.dumps(..., default=json_default)`. `None` (the default) is
   byte-identical to the previous plain `json.dumps` for EVERY existing caller (backward-safe);
   the migrator emits `json_default=str` when the tail used `default=str`. `DUMP_RE` broadened
   to capture `default=str`. Runtime-verified: a non-JSON-native value (`Path`) stringifies
   identically to the original `default=str`, and omitting `json_default` raises `TypeError`
   exactly as a plain `json.dump` (proving no behaviour drift). 702/703 SKIP (non-adjacent
   out_path). Non-conforming 10->5 on the set.

Migrator changes are the resume primitive at `ree-v3/tools/migrate_manifest_writers.py`
(re-validated conservative-by-construction). `elapsed_seconds` still NOT retrofitted (batch
scripts gain 6/7 always-core incl. `substrate_hash`; a lone advisory elapsed gap remains, hard
`manifest_writer_lint` unaffected) — the §7.4 timer retrofit stays a deliberate follow-up
(injecting a `_run_started` timer far from the write tail is per-script-variable; deferred to
keep this batch's blast radius contained). **[RESOLVED 2026-07-12 — see §7 item 4: 68/237
retrofitted via a companion AST tool (ree-v3 main `47ed14a`); the remaining 165 are advisory
gaps by design (no `timezone` import / no in-scope anchor) + 4 already conform via `started_at`.]**

**Updated remaining-unmatched taxonomy (799 unmatched of 1039, post-batch-2):**

| Unmatched class | ~count | Broadening needed | Risk |
|---|---|---|---|
| `.write_text(json.dumps(<var>))` / `json.dump(<var>` where var is NOT `manifest` (often `result`/`episode_log`, early-era) | 496 | accept non-`manifest` var **after** proving it is the flat manifest dict | med (var identity) |
| non-canonical out_path — remaining `{TYPE}_{ts}.json` (edge-case A) + non-adjacent `{run_id}.json` | 156 | correct run_id/out_dir or `MANIFEST_WRITER_EXEMPT` (edge-A); relax adjacency (non-adjacent) | high (edge-A renames) / low (non-adjacent) |
| no canonical `with open(out_path)` above dump | 100 | different write idiom | med |
| with-open path/handle name mismatch | 37 | generalize path/handle names | low |
| no `out_dir` assignment above tail | 8 | different dir var | low |
| `write_text(json.dumps(manifest` non-canonical (multi-manifest / non-adjacent) | 2 | per-script decision | med |

Recommended next-session order: the low-risk **with-open handle/path name mismatch (37)** and
**non-adjacent `{run_id}.json`** sub-classes next (both provably safe, just idiom/adjacency
generalisation), then the **496 non-`manifest`-var** class ONLY with a per-script proof that
the written var IS the flat manifest (highest var-identity risk; the `v3_onboard_smoke_*`
crash-shapes in it must be `MANIFEST_WRITER_EXEMPT`, per §6 edge-cases). Re-run the migrator
`--report` after each broadening.

### Progress — step 3 BATCH 3, session 2026-07-12 (247 scripts LANDED, ree-v3 main `e854b5c`)

Migrator broadened **lowest-risk-first** across three classes (each validated byte-equivalent
against a hand-migration AND against the frozen origin/main migrator, py_compile + AST-`Path`-
bound clean, `validate_experiments --strict --paths` 0 manifest-writer-backlog + **0 NEW**
non-conformances vs origin/main). **Total 247 scripts** + 5 `MANIFEST_WRITER_EXEMPT`. Full
`pytest tests/` = **1414 passed, 0 failed, 39 subtests** (the batch-2 `test_c12` unseeded flake
passed this run). Landed as 4 commits, rebased twice past concurrent origin/main writers
(§7.4 elapsed retrofit `47ed14a` + maturation-cache `36a0a3c`) — **zero file overlap** with
either (verified by set-intersection before each rebase; the 3 direct suites re-ran green
post-rebase, 44 passed).

1. **With-open path/handle + dir-var name mismatch (12 scripts).** Generalised `PRIMARY_RE`/
   `DRY_REASSIGN_RE` to CAPTURE the LHS path var + dir var (were hardcoded `out_path`/`out_dir`),
   and the with-open handle check to accept any path var, so a script naming them differently
   migrates PROVIDED the write statement's path var == the primary-assignment var AND the dir
   var is assigned above (both guarantee `write_flat_manifest` recomputes a byte-location-
   identical target). Migrates `out_file = out_dir/...` (494/495/495a/496/497), `manifest_path =
   evidence_dir/...` (536/536a/536b/582/582a/627), `out_path = OUT_DIR/...` (697). Var name
   preserved in the replacement so downstream `print`/`return` refs stay valid.
2. **Non-adjacent out_path (123 scripts).** Relaxed the walk-up adjacency requirement: when the
   path var is assigned canonically but NOT immediately above the write (intervening manifest-
   building code, e.g. `620`), find the NEAREST assignment to the path var above the write —
   because it is the nearest, the var is provably not reassigned between, so the recomputed path
   is byte-identical. Transform rewrites ONLY the write statement (leaves the assignment +
   intervening code, which may read the path); the `wfm` return reassigns the var to the same
   value. An **independent oracle** re-proved all 123 (nearest-canonical, no reassignment
   between). Also a general with-block-extent fix: a with-open block may carry a trailing
   `<fh>.write("\n")` after `json.dump` (`610*/655/656/672*/685`) — `write_flat_manifest` already
   appends `"\n"`, so absorbing it is byte-identical; any OTHER block statement → refuse.
3. **Non-`manifest`-var flat manifests (112 scripts).** Added `detect_manifest_var`: an **AST
   proof** that a non-`manifest` var (early-era `result`/`output`/`pack`/`flat`/`result_doc`) IS
   a flat manifest — assigned a dict LITERAL whose keys include `run_id` + `architecture_epoch` +
   a status key, and is the UNIQUE such var written (>1 candidate → refuse). Migrator regexes +
   config expr + emit parameterised by the detected var. All other guards unchanged (canonical
   `<dir>/f"{run_id}.json"` path via `PRIMARY_RE` excludes edge-case-A `{TYPE}_{ts}.json` + pack-
   subdir paths; `runid_is_manifest_runid` proves path run_id == dict run_id). Migrates output 79
   / pack 27 / flat 5 / result_doc 1. An **independent AST oracle** re-proved all 112; all 112
   build a `_v3` run_id (`require_v3` passes); a runtime smoke confirmed `wfm` accepts the shape +
   stamps always-core. The 356 edge-case-A/non-canonical `result`-var scripts + the 5
   `v3_onboard_smoke_*` crash-shapes (subscript-built, no dict literal) are excluded by
   construction; the onboard_smokes were additionally marked `MANIFEST_WRITER_EXEMPT` (§6 edge-
   case hygiene; inert for the current counter — they carry no `evidence_direction` token).

Migrator changes are the resume primitive at `ree-v3/tools/migrate_manifest_writers.py` (all
generalisations conservative-by-construction; the frozen-origin byte-equivalence check on 25
canonical scripts guards against any behaviour drift for the batch-1/2 shape). `elapsed_seconds`
for these 247 was NOT retrofitted in batch 3 itself — **DONE as a follow-up 2026-07-12 (ree-v3
main `d57e893`): 35 of the 247 retrofitted** via the §7.4 companion tool
`tools/retrofit_elapsed_seconds.py`; see §7 item 4 for the breakdown (the other 212 are by-design
advisory gaps — no `timezone` import / no in-scope parse_args anchor).

**Updated remaining-unmatched taxonomy (547 unmatched of 1040, post-batch-3):**

| Unmatched class | ~count | Broadening needed | Risk |
|---|---|---|---|
| **edge-case-A `{TYPE}_{ts}.json`** early-era (write to ree-v3-local `parents[1]/evidence/experiments/<TYPE>/<TYPE>_<ts>.json`; `result`-var) | 319 | RENAMES the flat file + relocates it -> correct `run_id`/out_dir FIRST, or `MANIFEST_WRITER_EXEMPT` | high (rename+relocate) |
| **other idioms** (os.path.join writes, non-canonical with-open, multi-line dumps, subscript-built manifests, `episode_log`/`summary` non-manifest writes) | 211 | per-class idiom generalisation + per-script var-identity proof | med |
| pack-subdir / `runs/<id>/manifest.json` (pack-path, not flat) | 14 | route the FLAT sibling not the pack write, per §D multi-manifest | med |
| subscript-built manifest (`result["run_id"]=...`, no dict literal) | 3 | AST-detector needs subscript-assembly support | med |

Recommended next-session order: the **319 edge-case-A** class is the largest single remaining
block but the highest risk (migrating renames+relocates the flat file); it needs a run_id/out_dir
**correction** pass (rewrite the early-era scripts to the canonical `REE_assembly/evidence/
experiments/<run_id>.json` path) BEFORE routing — or a blanket `MANIFEST_WRITER_EXEMPT` if the
team decides these archival early-era manifests stay as-is. The **211 "other"** are a grab-bag of
idioms (do the os.path.join + non-canonical-with-open sub-shapes next; they are provably safe idiom
generalisations). Re-run the migrator `--report` after each broadening.

### Progress — step 3 BATCH 4, session 2026-07-12 (145 scripts LANDED, ree-v3 main `681f490`)

The **211 "other"** grab-bag's provably-safe canonical-`{run_id}.json`-path sub-shapes (the
recommended do-first from batch 3). Migrator broadened conservatively; **145 scripts** routed
(83 pathlib slash-path + 62 `os.path.join` ; 103 `manifest` + 42 non-`manifest` `output`/`pack`).
Every one is byte-location-identical — **no rename, no relocate** (the canonical `{run_id}.json`
path guard is preserved, so edge-case-A `{TYPE}_{ts}` scripts stay refused BY CONSTRUCTION).
Cumulative **625 of 1028**. Landed as 2 commits (migrator `c53f1dc`→ rebased; scripts) rebased
past concurrent origin/main writers (arm_fingerprint sec11 `9f91c4d` + elapsed-retrofit
`d57e893`) — **zero file overlap** (set-intersection verified before the rebase; the 145 are
previously-*unmatched* scripts, disjoint from the *already-routed* retrofit set by construction).

Generalisations (each preserves the batch-1/2/3 canonical guard; the `os.path.join` / non-
`manifest` alternatives only fire when the slash / `manifest` fast-path fails):

1. **With-open SPELLING variants (~80).** `WITH_RE` accepts a trailing `, encoding="..."` in the
   mode arg; new `WITH_METHOD_RE` accepts the bound-path method form `<path>.open("w", ...)`.
   Irrelevant to output bytes — `write_flat_manifest` always writes utf-8 + a trailing newline,
   and every matched dump is `ensure_ascii` JSON (`dump_re`/`writetext_re` never accept
   `ensure_ascii=False`).
2. **`os.path.join(<dir>, f"{run_id}.json")` path (62).** `primary_res`/`dry_res` add an
   `os.path.join` alternative to the pathlib slash form — byte-location-identical on POSIX (the
   only fleet platform), since `write_flat_manifest` does `Path(out_dir)` and accepts a `str` dir.
3. **Per-mvar run_id key.** The canonical path may key run_id off the detected non-`manifest` var
   (`pack['run_id']`/`output['run_id']`), not just `manifest['run_id']` — the run_id pattern is
   now built per detected mvar. Subscript form needs no proof (`write_flat_manifest` reads the same
   `<mvar>['run_id']`); the bare-`run_id` guard is generalised to `<mvar>`.
4. **write_text `default=str` capture + Path-import guard.** The emitted call uses
   `Path(__file__)`; the `os.path`-family scripts import only `os`, so `ensure_path_import` adds
   `from pathlib import Path` when the bare name is unbound (no-op for slash-form scripts, so the
   frozen-origin byte check stays 0-diff). **This was a real bug the AST-Path-bound check caught**
   (44 scripts would have `NameError`d at runtime before the fix).

**New guard — multi-write-site refusal.** A script whose mvar is written via `json.dump`/
`write_text` more than once (branchy `if dry: {..write..} else: {..write..}`, e.g. `v3_exq_354`)
is refused: the migrator rewrites only the FIRST write, so routing would leave a raw `json.dump`
behind AND mark the script already-routed. Correctly held for a dedicated pass.

Validation (batches 1-3 process): backward-compat 0-diff vs frozen origin/main migrator on 25
canonical; per-script `py_compile` + AST-Path-bound (145/145); `validate_experiments --strict
--paths` **0 NEW** non-conformances (144 raw-`json.dump` manifest-writer findings cleared; residual
degeneracy-self-report/readiness backlog orthogonal + unchanged); an **independent oracle**
(re-derives from origin source, not the migrator) proved 145/145 path-identity + the strict
flat-manifest dict-literal proof for the 42 non-`manifest` vars; runtime smoke (wfm accepts the
`os.path.join` `str` dir, recomputes the byte-identical path, stamps always-core); downstream
`str`→`Path` op-scan on the 62 `os.path.join` scripts (0 risky); byte-equivalence vs independent
hand-migrations of `244a` (os.path.join+output+default=str) and `460b` (encoding=+manifest slash);
merge gate `pytest tests/` = **1420 passed, 0 failed, 39 subtests**.

**Updated remaining-unmatched taxonomy (402 unmatched of 1040, post-batch-4):**

| Unmatched class | ~count | Broadening needed | Risk |
|---|---|---|---|
| **edge-case-A `{TYPE}_{ts}.json`** early-era (ree-v3-local; `result`-var; `detect_manifest_var`→None) | 306 | **TEAM DECISION 2026-07-12: HYBRID** — classify each vs the queue + recent-run history; blanket `MANIFEST_WRITER_EXEMPT` the truly-archival (never re-run), run the `run_id`/out_dir CORRECTION pass ONLY on any still actively re-queued/run. | high (rename+relocate) |
| non-canonical path (hardcoded literal filename `exq_051b_v3.json`; proven-var `{TYPE}_{ts}`; other) | 84 | per-script proof that the literal filename == `f"{run_id}.json"` | med |
| no `out_dir` assignment above tail | 8 | dir var assigned out of the walked region | med |
| pack-subdir / `runs/<id>/manifest.json` multi-manifest (`540f`), odd with-open, multi-write branchy (`354`) | ~4 | route the FLAT sibling per §D; multi-write needs both-branch rewrite | med |

Recommended next-session order: the **306 edge-case-A** class is now the dominant remaining block;
the **2026-07-12 team decision is HYBRID** — first classify each script against
`ree-v3/experiment_queue.json` + recent-run history (evidence manifests / `runner_status`), then
blanket `MANIFEST_WRITER_EXEMPT` the truly-archival (never re-run — the always-core stamp only
benefits NEW runs) and run the `run_id`/out_dir CORRECTION pass ONLY on any still actively
re-queued/run (a correction must also confirm the early-era `run_id` ends `_v3`, else
`write_flat_manifest` raises). The **84 non-canonical-path** (hardcoded literal filenames) are the
next-safest mechanical batch but need a per-script proof that the literal filename ==
`f"{run_id}.json"`. Re-run the migrator `--report` after each broadening.

### Progress — step 3 BATCH 5, session 2026-07-12 (`magical-jennings-84d86f`; 15 scripts LANDED, ree-v3 main `ae74b63`)

The **84 non-canonical-path** class (`detect_manifest_var` SUCCEEDED but the path is not the
canonical `<dir>/f"{run_id}.json"`). The migrator gained an **AST filename-proof** and migrated
the **15** genuinely-safe scripts; the other **69 are correctly REFUSED** (routing them would
RENAME the flat file). Cumulative **640 of 1028**.

Why only 15 of 84 — the whole point of the per-script proof. `write_flat_manifest` writes to
`Path(out_dir)/f"{manifest['run_id']}.json"`, so routing a non-canonical filename is byte-safe
**only** if that filename provably equals `f"{run_id}.json"`. A survey of the 84 found the
overwhelming early-era shape `out_path = out_dir / f"{EXPERIMENT_TYPE}_{ts}.json"` pairs with
`run_id = f"{EXPERIMENT_TYPE}_{ts}_v3"` — the **filename is missing the `_v3`**, so routing would
rename `{TYPE}_{ts}.json` -> `{TYPE}_{ts}_v3.json`. Those (31) plus `ts`-vs-`ts_utc` variable
mismatches (1: `451`), inline **second** `datetime.now()` reads in the run_id (`263`/`531`/`533`/
`534` etc.: the run_id timestamp is a different clock read than the filename's `ts`, so NOT
provably equal — 9 `filename-not-templatable`), `out_dir/"manifest.json"` pack-style writes (6:
`178`/`198`/`518`...), `{TYPE}_{run_id}` (`085m`), `{run_id}_manifest.json` (`610`/`610a`), and
un-extractable run_ids (5) are ALL genuine renames/relocations or non-deterministic → refused.

The 15 migrated (each `filename == f"{run_id}.json"` proven):
- **hardcoded literal** (`051b`: `"exq_051b_v3.json"` == `run_id "exq_051b_v3"`; compound dir
  `ROOT.parent / "REE_assembly" / "evidence" / "experiments"`);
- **`"%s.json" % run_id`** idiom (`184`, `308` — a spelling of `f"{run_id}.json"`);
- **`f"{TYPE}_{ts}_v3.json"` that already equals run_id** (`264`/`265`/`265a`/`266`/`266a`/`267`/
  `355`/`355a`/`429`/`430` via `os.path.join`; `526`/`527` via slash with `ts_utc`).

Generalisation (added to `migrate_manifest_writers.py`, fires ONLY when the canonical
`match_primary` walk-up fails — so the batch-1..4 canonical output is byte-unchanged):
`noncanonical_filename_proof()` reduces both the filename expr and the `<mvar>['run_id']` value
expr to a **template** (a list of atoms: literal chunks `('L',s)` + single-static-assignment
bare-Name leaves `('N',name)`), then proves `normalize(template(filename)) ==
normalize(template(run_id) + [('L','.json')])`. Soundness rails: f-string interpolations must be
BARE NAMES (an inline `Call` like `datetime.now()` -> refuse, catching the clock-read-twice
`263` bug); only `%s`-style `%`-formatting and `+` string-concat are accepted (any other `%`
code -> refuse); every `('N',name)` leaf must have EXACTLY ONE binding site NOT inside a loop, so
the run_id and the filename read the SAME runtime value (even a once-computed `ts =
datetime.now()...`, which is why a reused single-assignment `ts` is safe but an inline re-read is
not). On proof, the transform is a **write-only-rewrite** (like the batch-3 non-adjacent path):
the original `out_path = <dir>/<fn>` assignment + any `mkdir` are LEFT in place (so downstream
refs + the dir's free names stay valid), only the `with open/json.dump` (or `write_text`) is
swapped for `write_flat_manifest(<mvar>, <dir-sub-expression-verbatim>, ...)`. Because
`filename == f"{run_id}.json"` is proven and the ORIGINAL `out_dir` sub-expression is passed
verbatim (`ast.get_source_segment`, quote-style preserved), `write_flat_manifest` recomputes a
byte-location-identical target — no rename, no relocate.

Validation (batches 1-4 process): backward-compat **0-diff** vs the frozen origin/main migrator
on 25 canonical pre-migration scripts (the new path never fires for them); **byte-equivalent** vs
INDEPENDENT hand-migrations of `051b` (compound-dir literal), `264` (os.path.join + `output` var),
`184` (`%s` + `pack` var); `py_compile` + AST-`Path`-bound 15/15; `validate_experiments --strict
--paths` = **14 manifest-writer findings cleared, 0 NEW** non-conformances (`051b` was never in the
lint backlog — it carries no `evidence_direction` token — but is still routed); a **SEPARATELY-
IMPLEMENTED oracle** (different code from the migrator's proof, same spec, re-derives the mvar +
run_id + filename templates from the origin source) independently PROVED the same 15 and REFUSED
the same 69; `str`->`Path` op-scan on the 8
`os.path.join` scripts (0 risky post-write string ops on `out_path`); runtime smoke (`wfm`
recomputes the byte-identical filename for the literal / `os.path.join`-`str`-dir / `%s` shapes);
full-corpus regression NEW-vs-FROZEN migrator = **+15 migrate / -15 unmatched, 638 skip unchanged,
the 306 edge-case-A class UNTOUCHED**; merge gate `pytest tests/` = **1437 passed, 0 failed, 39
subtests** (2:36). `elapsed_seconds`
NOT retrofitted here (the §7.4 companion tool covers newly-routed scripts as a follow-up).

**Updated remaining-unmatched taxonomy (387 unmatched of 1040, post-batch-5):**

| Unmatched class | ~count | Broadening needed | Risk |
|---|---|---|---|
| **edge-case-A** (`detect_manifest_var`→None; `result`-var; ree-v3-local `{TYPE}_{ts}.json`) | 306 | **TEAM DECISION 2026-07-12: HYBRID** (classify vs queue/run history; exempt archival, correct still-active) | high (rename+relocate) |
| non-canonical filename provably **!=** run_id (`{TYPE}_{ts}` missing `_v3` (31); inline `datetime.now()` re-read (9); `manifest.json`/pack-path (6); un-extractable run_id (5+3); `ts`/`ts_utc` or order mismatch (4); `{run_id}_manifest.json` (2); filename-var (2); `{TYPE}_{run_id}` (1)) | 69 | genuine rename/relocate or non-determinism — **correctly refused**; correct `run_id`/out_dir first or `MANIFEST_WRITER_EXEMPT` | high |
| no `out_dir` assignment above tail | 8 | dir var assigned out of the walked region | med |
| odd with-open / multi-write branchy (`354`) / pack-subdir multi-manifest (`540f`) | ~4 | per-script; multi-write needs both-branch rewrite | med |

Recommended next-session order: the **306 edge-case-A** class **is now DONE** (edge-case-A HYBRID
section below). The remaining live block is the **69 non-canonical refusals** (`detect_manifest_var`
SUCCEEDED but the filename is a genuine rename) — these need the SAME HYBRID (exempt archival /
correct-and-route active) since they cannot be forced mechanically. The `no out_dir` (8) +
odd-idiom (~4) are small provably-safe-idiom tails. Re-run the migrator `--report` after each
broadening.

### Progress — step 3 edge-case-A HYBRID, session 2026-07-12 (`amazing-kepler-0c8b71`; 276 scripts LANDED, ree-v3 main `7b8c150`)

Executed the **2026-07-12 TEAM DECISION (HYBRID)** on the edge-case-A class
(`{TYPE}_{ts}.json`, `result`-var, `detect_manifest_var`→None; migrator-refused because routing
would rename the flat file). **Distinct from batch 5**: batch 5's 84 were `detect_manifest_var`
SUCCEEDED + non-canonical filename; this class is `detect_manifest_var`→None — disjoint by
construction (verified: zero file overlap; clean rebase past `ae74b63`).

**Enumerate + refine.** The migrator's `no json.dump(manifest tail` (`detect_manifest_var`→None)
reason = **306**. An independent AST classifier cross-checked the `{TYPE}_{ts}.json` path shape:
**276 genuine edge-A** (`{TYPE}_{ts}` filename → routing renames) = 25 ree-v3-local
(`parents[1]/evidence`) + 251 REE_assembly-location (`parents[2]/.../experiments/<TYPE>/`) —
both `result`-var, both migrator-refused. **30 out-of-scope, EXCLUDED** (not edge-A): 22
`RUNID_only` that already write the canonical `{run_id}.json` (a future *var-identity* batch —
relax `detect_manifest_var` to a non-dict-literal `result` var; exempting them would DISHONESTLY
suppress a routable lint) + 8 emit-only/harness with no raw flat-manifest `json.dump` (not
lint-flagged). Correctness check: the residual-from-306-still-unmatched is *exactly* these 30, with
**zero `{TYPE}_{ts}` writes** — every genuine edge-A script was handled.

**Classify (queue + recent-run history).** Live queue held only `V3-EXQ-742` (none of the 276
queued). Recency = canonical-manifest presence at `evidence/experiments/<run_id>.json` +
most-recent `runner_status/*.json` `completed_at` per queue_id.
- **267 ARCHIVAL** (not queued; no recent canonical manifest; last-completed >45d or never) →
  mechanical module-level `MANIFEST_WRITER_EXEMPT = "archival early-era manifest (pre-canonical
  {TYPE}_{ts} path/naming; not re-run)"` (dedicated AST inserter after the last top-level import;
  **no migrator change**). manifest-writer-backlog **249→0**; non-conforming findings **516→267**
  (the 267 residual are the PRE-EXISTING degeneracy-self-report backlog — orthogonal; the
  before/after non-conforming SCRIPT set is *identical*, **0 NEW**); 267/267 `py_compile`; merge
  gate `pytest tests/` **1437 passed, 0 failed**. (18 of the 267 were already lint-clean — no
  `evidence_direction` token — so their exempt is inert, per the batch-3 onboard_smoke precedent.)
- **9 ACTIVE** (`047l 047m 063a 623 630 664 665 671 741`; all `_v3`, REE_assembly-base, a canonical
  manifest present or completed ≤40d) → **run_id/out_dir CORRECTION** (hand-migrated, no migrator
  change): drop the `<TYPE>` subdir from the manifest dir → canonical top-level
  `REE_assembly/evidence/experiments/`, route `result` through `write_flat_manifest(...)`;
  `run_id` already `{TYPE}_{ts}_v3` (`require_v3` passes); `emit_outcome(manifest_path=<wfm return>)`
  preserved. 664/665 keep `out_dir` (the `<TYPE>` subdir) for their `episode_log` and route the
  manifest to `out_dir.parent`. Per-script dry var: `args.dry_run` (047l/047m/623/630/664/665/741),
  `False` (063a — no `--dry-run`; 671 — write inside `if not args.dry_run:`). manifest-writer
  **9→0**; **0 NEW** non-conforming (13→4, the 4 pre-existing degeneracy).

**Validation (batches 1-4 process).** 276/276 `py_compile`; `validate_experiments --strict --paths`
0 NEW; **independent AST oracle** 9/9 (single `write_flat_manifest(result, canonical-top-level)`,
no residual raw dump, run_id `_v3`, `<TYPE>`-subdir logic consistent) + **static scope oracle** 9/9
(every call ref bound); **dry-run smoke** — 047l end-to-end (canonical `<run_id>.json`,
**`substrate_hash` now populated** — was 0% — + machine/machine_class/recording_schema core, emit
relocated the `_dry_` file to scratch, **no evidence-dir leak**) and 664 episode_log variant
(manifest at canonical top-level with always-core, episode_log stays in the `<TYPE>/` subdir). The
664 smoke **CAUGHT a real bug**: the 664/665 write is at module-`__main__` scope, not `run()` —
`dry_run=dry_run` NameError'd → corrected to `args.dry_run`; re-smoke clean (this is exactly why the
runtime smoke is mandatory). Merge gate `pytest tests/` = **1437 passed, 0 failed** (post-rebase 3
direct suites 52 passed). Staged on `integration/pack-writer-edgeA-hybrid` in a dedicated worktree
off `ree-v3` main (`.claude/worktrees/REE_assembly` symlink for the `test_arm_reuse` gotcha).

**Cumulative: 649 of 1028** route through `write_flat_manifest` (640 + 9 corrected) **+ 272
`MANIFEST_WRITER_EXEMPT`** (267 archival edge-A + 5 pre-existing onboard_smoke). Migrator unmatched
**402→111** (267 exempt→skip + 9 routed; batch 5 also reduced its class in parallel). Remaining 111
unmatched (77 still lint-flagged): the **69 batch-5 non-canonical genuine-renames** (need the same
HYBRID) + the 22 RUNID_only var-identity + 8 emit-only + 8 no-out_dir + 3 no-with-open + 1 branchy
(`354`).

### Progress — step 3 BATCH 6, session 2026-07-13 (`nervous-greider-7677d7`; 9 scripts LANDED, ree-v3 main `bf7724a`)

The two SMALL provably-safe-idiom tails left after the edge-case-A HYBRID.
**8 scripts routed via a migrator generalization + 1 (`354`) hand-migrated.**
Cumulative **658 of 1028**; migrator unmatched **111→102**.

**(1) `no out_dir assignment above tail` (8: `621`/`621a`/`622`/`626`/`626a`/`626b`/
`636`/`637`).** All are the early-era `emit_manifest(cells, acceptance, out_dir: Path
[, dry_run])` shape: the canonical `out_path = out_dir / f"{run_id}.json"` + `with
open(out_path): json.dump(manifest, ...)` tail sits INSIDE `emit_manifest`, where
`out_dir` is a **formal parameter**, not an `out_dir = ...` statement — so
`has_dir_assignment` (a line-scan for `<dir> =`) missed it. A whole-file scan would be
**UNSOUND**: every one of these scripts ALSO assigns a *different*, `main()`-local
`out_dir = Path(args.output_dir)` **below** the write in another scope. **Generalisation**
(`dir_bound_as_param`, added to `migrate_manifest_writers.py`): accept `dirvar` when it is
a parameter of the function that lexically encloses the write AND is never rebound (Store)
before the write in that function — an **OR fallback fired ONLY when `has_dir_assignment`
already returned False**, so the canonical batch-1..5 output is byte-unchanged. Byte-safety:
`write_flat_manifest` recomputes `Path(out_dir) / f"{manifest['run_id']}.json"`; `out_dir`
is the enclosing param (a `Path`, used with `/`), never rebound, and the manifest sets
`"run_id": run_id` (so `manifest['run_id']==run_id`) — byte-location-identical, `dry_run=False`
matches the unconditional raw write (the `dry_run` param, when present, only enters the dict
as `"dry_run": dry_run`; it never gated the path). Emission = the exact canonical batch-1
transform (import insert + mkdir-absorb + `write_flat_manifest(manifest, out_dir,
dry_run=False, config=..., seeds=SEEDS, script_path=Path(__file__))`).

**(2a) `354` (branchy, hand-migrated real-branch-only).** `v3_exq_354` was refused by the
multi-write-site guard: an `if not args.dry_run: <write> else: <write>` where **both
branches write the IDENTICAL** `out_dir / f"{run_id}.json"` (`json.dump(output)`; only the
print string differs). **Both-branch routing is NOT byte-safe**: the dry-branch `run_id =
f"{EXPERIMENT_TYPE}_dry_{timestamp}"` has **no `_v3`**, so `write_flat_manifest` (require_v3)
would `raise` on the dry path where the raw `json.dump` did not (and `dry_run=True` would
additionally `_dry_`-prefix + relocate to scratch — not byte-identical to the original
real-`out_dir` write). So **only the `if not args.dry_run` branch is routed**
(`dry_run=False`; its `run_id` ends `_v3`), byte-location-identical for the real evidence
write; the dry-branch smoke write stays raw (harmless — dry runs are never real evidence).
The `manifest_writer_lint` is discharged by chokepoint-writer **name-presence**
(`validate_experiments.py:531`), so the residual dry-branch `json.dump` does not re-flag.
Hand-migrated (single idiosyncratic script) rather than relaxing the protective multi-write
guard.

**Refused (documented), NOT byte-safe mechanically:**
- **`540f`** — routable in principle (its flat sibling `run_pack` writes the canonical
  `out_dir / f"{run_id}.json"`; the `manifest` var is a pack-INDEX `{"runs":[...]}`), but
  it is in the **active `priceless-snyder-3ffc30` batch-5 non-canonical-rename HYBRID claim
  set** (`540f` classifies under `non-canonical filename not provably == run_id`). **Dropped
  for disjointness** — left to that session.
- **`241a`/`241b`** — pack-subdir multi-manifest: pack `evidence_dir/"manifest.json"` +
  `metrics.json` + a flat sibling `<TYPE>_output.json`. The flat sibling filename `≠
  {run_id}.json` → routing **renames** → HYBRID/§7 pack track, not byte-safe here.
- **`247`** — writes ONLY `output_dir/runs/<run_id>/manifest.json` (+ `raw_metrics.json`);
  no top-level flat sibling exists → routing would **relocate** a new file → §7 pack track.
- **`354` dry branch** — see above (`{TYPE}_dry_{ts}` lacks `_v3`).

**Validation (batches 1-5 process).** Backward-compat **0-diff** vs the frozen origin/main
migrator on 25 canonical pre-migration scripts (report + emitted source byte-identical — the
new `dir_bound_as_param` path never fires for them). Full-corpus regression NEW-vs-FROZEN
migrator = **exactly +8 migrate / −8 unmatched**, 929 skip unchanged, all 102 remaining
unmatched byte-identical (the 69 batch-5 renames + edge-A residual **untouched**). A
**SEPARATELY-IMPLEMENTED oracle** (reads the pre-migration source at `git HEAD`, different
code from the migrator) independently PROVED all 8: target `= out_dir/f"{run_id}.json"`,
`out_dir` a param of `emit_manifest()`, not rebound before the write, `"run_id": run_id`
field present, single in-fn write, `dry_run=False`. (The oracle first FALSE-refused all 8 on
a file-wide `out_path` assignment count — `main()` also does `out_path = emit_manifest(...)`;
scoping the count to the enclosing function fixed it, confirming the oracle is genuinely
independent.) 8/8 + `354` `py_compile` + AST-`Path`-bound + `write_flat_manifest` present +
no residual raw `json.dump(manifest`. `validate_experiments --strict --paths`: **manifest-
writer backlog cleared** (3 of the 8 were lint-flagged — `621`/`621a`/`622`; `354` also) and
**0 NEW** non-conformances (the pre-existing degeneracy-self-report / arm-fingerprint /
emit_outcome findings are byte-identical before vs after — orthogonal, out of scope).
**Runtime smoke**: `636` (`emit_manifest([], {"overall_pass":True}, tmp)`) and `621`
(`dry_run=True` param) both wrote the byte-location-identical `<tmp>/<run_id>.json` with the
always-core populated (`substrate_hash` now set — was 0%), `run_id` `_v3`, and NO `_dry_`
prefix (621 confirms the hardcoded `dry_run=False` is byte-faithful to the raw write). Merge
gate `pytest tests/` = **1437 passed, 0 failed, 39 subtests (7:18)**.

**Updated remaining-unmatched taxonomy (102 unmatched of 1040, post-batch-6):**

| Unmatched class | ~count | Broadening needed | Risk |
|---|---|---|---|
| ~~non-canonical filename provably **!=** run_id (batch-5 69 genuine renames; `540f` counted within)~~ **DONE 2026-07-13 (`acd1a50`): all 69 ARCHIVAL -> `MANIFEST_WRITER_EXEMPT`** | 0 | -- (section below) | -- |
| `no json.dump(manifest` tail (non-`manifest`-var / episode_log / write_text idioms not yet var-proven) | 30 | per-script var-identity proof (batch-3 class) or HYBRID | med |
| pack-subdir multi-manifest rename/relocate (`241a`/`241b` flat `<TYPE>_output.json`; `247` `runs/<id>/manifest.json`) | 3 | route the flat sibling only IFF `{run_id}.json`; else §7 pack track | med |
| misc (`no run_id in result dict literal`, un-templatable) | ~1 | per-script | low |

The remaining live blocks are the `priceless-snyder-3ffc30` rename HYBRID (**now DONE** --
section below) and the 30 `no json.dump(manifest` non-`manifest`-var tail (needs the batch-3
var-identity proof extended or its own HYBRID). Re-run the migrator `--report` after each
broadening.

### Progress — step 3 batch-5 non-canonical genuine-rename HYBRID, session 2026-07-13 (`priceless-snyder-3ffc30`; 69 scripts LANDED, ree-v3 main `acd1a50`)

Executed the **HYBRID** on the **69 batch-5 non-canonical genuine-rename refusals** --
scripts where the migrator's `detect_manifest_var` **SUCCEEDED** but it refused because the
output filename is not provably `== f"{run_id}.json"` (so routing would RENAME the flat file).
**Distinct from the edge-case-A HYBRID** (`detect_manifest_var`->None) by construction: this
class is `detect_manifest_var` SUCCEEDED + non-canonical filename. Enumerated via the migrator
`UNMATCH` reason `non-canonical filename not provably == run_id` = **69** (31 `{TYPE}_{ts}`
missing `_v3` + 8 un-templatable JoinedStr + 6 `manifest.json` pack-style + 5+3 no-run_id-in-dict
+ 4 `ts_unix` + 3 `TYPE`/`ts` order-swap + 2 `{run_id}_manifest.json` + 2 filename-var + 1
`ts_utc` + 1 `ts_compact` + 1 `{TYPE}_{run_id}`). `540f` is one of the 69 (batch-6's "+540f"
note counts it within, not additional).

**Classify (queue + recent-run history).** Live queue held only `V3-EXQ-742-m` (none of the 69
queued). Recency = canonical top-level manifest presence at `evidence/experiments/<run_id>.json`
+ most-recent `runner_status/*.json` `completed_at` per queue_id. **ALL 69 ARCHIVAL, ZERO ACTIVE**:
none queued; **none run within 40d** (nearest is `610a` at 44d completed / 41d manifest); and every
one of the 12 that carry a canonical manifest is **superseded by a later-lettered sibling that
already writes canonical** (`110`/`111`/`118`->`517*`/`529`/`623`; `418j`/`418k`->`418l`/`418m`;
`516`->`517*`; `563a`->`563b`/`563c`; `608`->`611`..`660b`; `610`/`610a`->`610b`..`610f`/`655`/`656`).
The `mech216` `263`/`332` pair has no successor but is 84-89d old + unqueued. The 12 manifests date
80-114d ago (several share the `2026-04-18T12:40:10Z` bulk-backfill timestamp, not a real run).
Because zero are active, the `run_id`/out_dir **CORRECTION + mandatory dry-run smoke** path was
**not exercised** (no active script to correct); the exempt path adds an inert module constant with
no runtime behaviour change, so no smoke is applicable (mirrors the edge-A archival 267).

-> mechanical module-level `MANIFEST_WRITER_EXEMPT = "archival early-era manifest (non-canonical
filename not provably == run_id.json; superseded lineage, not re-run)"`, inserted after the last
top-level import by a **dedicated AST inserter** (byte-preserving line insertion, idempotent; **no
migrator change**). Every changed file exactly **+2/-0**.

**Validation (batches 1-4 process).** 69/69 `py_compile`; `validate_experiments --strict --paths`
over the 69 = **manifest-writer findings 51->0, 0 NEW** (degeneracy-self-report backlog **67->67**
unchanged; total finding lines **189->138 = -51 exactly**; the before/after non-conforming finding
SET differs ONLY by the 51 removed manifest-writer lines -- `comm` proved 0 non-manifest-writer
removed + 0 NEW). **18 of the 69 carry no `evidence_direction` token** so their exempt is inert
(batch-3 onboard_smoke / edge-A 18/267 precedent). An **independent classification+writer oracle**
(separate code from the analysis: re-derives from git-HEAD source + the queue + the evidence dir)
confirmed **69/69 genuine raw-dump manifest writers AND 69/69 archival** (0 queued, 0 recent) --
the oracle initially flagged 3 "phantom" (AnnAssign / base-module-inherited / helper-param manifest
idioms its dict-literal detector missed) + 4 "not archival" (85d-manifest scripts its over-strict
supersession rule tripped on); both were oracle bugs, fixed (AnnAssign + name-based writer fallback;
archival = unqueued AND not-recent, supersession informational) -> clean 69/69. Post-rebase migrator:
the 69 all report `skip`/`MANIFEST_WRITER_EXEMPT`. Merge gate `pytest tests/` = **1436 passed, 1
pre-existing order/global-RNG flake** (`test_scaffolded_sd054_onboarding.py::test_c17_reinforce_loss_
gradient_reaches_rule_bias_head` -- unseeded within-test [its `manual_seed(0)` is in a *different*
test], **PASSES in isolation**, and this diff touches **0 test/`ree_core` files**; the same suite's
sibling `test_c12` was the documented batch-2 flake), 39 subtests passed; 3 direct suites
(`test_recording_standard` + `test_arm_fingerprint_lint` + `test_arm_reuse`) 44 passed pre- and
post-rebase. Staged on `integration/pack-writer-batch5-noncanonical-hybrid` in a dedicated worktree
off `ree-v3` main (`.claude/worktrees/REE_assembly` symlink for the `test_arm_reuse` gotcha),
rebased past the 4 concurrent commits (batch6 `52741e0`/`3e87734`/`bf7724a` + §7.4-b5 `a442440`;
**zero file overlap** verified), ff-merged to `main`, branch + worktree removed.

**Cumulative: 658 of 1028** route through `write_flat_manifest` (unchanged -- this pass routes 0)
**+ 341 `MANIFEST_WRITER_EXEMPT`** (272 + 69). Migrator unmatched **102->33** (the 69 exempt->skip).
Remaining 33 unmatched (still the live block): **30 `no json.dump(manifest` tail**
(`detect_manifest_var`->None: ~22 `RUNID_only` var-identity that already write canonical
`{run_id}.json` [a var-identity batch, relax `detect_manifest_var` to a non-dict-literal `result`
var] + ~8 emit-only/harness with no raw flat-manifest dump [not lint-flagged]) + **3
`no canonical with open`**.

### Progress — step 3 RUNID_only var-identity, session 2026-07-13 (`mystifying-wilbur-394a10`; 12 scripts LANDED, ree-v3 main `31eb700`)

The **22 RUNID_only** scripts (`detect_manifest_var`->None, but the write path is the
ALREADY-canonical `<dir>/f"{run_id}.json"` -- no rename, no relocate -- and the manifest var is
NOT a single dict LITERAL, so the batch-3 literal proof returned None). Generalized
`detect_manifest_var` to prove a non-literal manifest var IS a flat manifest, then routed the
byte-safe subset (**12**); the other **10 are honestly REFUSED** (routing them would BREAK the run,
not rename a file). Cumulative **670 of 1028** (658 + 12); migrator unmatched **33->21**. **Disjoint
from the concurrent batch-6** (`bf7724a`, param-out_dir class) AND the **batch-5 rename HYBRID**
(`acd1a50`) by construction -- verified ZERO script overlap; the two migrator generalizations touch
DIFFERENT functions (`detect_manifest_var` here vs `dir_bound_as_param` in batch 6); rebased cleanly
past both.

**Generalization** (added to `migrate_manifest_writers.detect_manifest_var`; scope-aware; fires ONLY
when the `manifest`-named fast path fails, so the batch-1..5 output is byte-unchanged). A written var
V routes IFF it provably resolves, **at its write site's lexical scope**, to a dict carrying `run_id`
(non-None) + `architecture_epoch` + a resolvable status (`status`|`outcome`|`overall_outcome`) --
EXACTLY write_flat_manifest's three raise guards (so a script that would raise stays refused). Two
binding kinds, both proven statically, conservative-by-construction:
- **(A) assembled** -- a dict literal / AnnAssign SEEDED then mutated by `result["k"]=...`
  subscript-assigns and/or `result.update({..literal..})` merges (key-UNION; a key-removal
  `del`/`.pop`/`.clear`, or a literal `"run_id": None`, voids the proof -> refuse);
- **(B) return-bound** -- `result = run_experiment(...)` where the helper builds the manifest
  (literal / AnnAssign / assembled) and returns it. EVERY direct return (scope-aware -- nested
  funcs/lambdas excluded) must be a proven manifest: keys = INTERSECTION over all return paths,
  run_id-non-None = AND over all paths (so a `return {..., "run_id": None}` dry-run stub REFUSES the
  whole helper); a `return result, out_path` tuple takes the first element; one extra level of
  return-tracing (a returned var itself `= helper(...)`). Mixed literal+call, >1 call, or a
  non-dict/non-call binding -> refuse. Uniqueness preserved: exactly one written var must prove out.

**The 12 routed** (each canonical `{run_id}.json`, run_id+arch+status proven): return-bound `result`
(568/588c/588d/588e/615/669b/670/688/688a/730/731) + assembled `output` written INSIDE the enclosing
`run_experiment` scope (596; bare-`run_id` path proven `== output['run_id']` via `"run_id": run_id`
+ the existing `runid_is_manifest_runid` guard). The other **10 of the 22 correctly REFUSED**: **8
have no resolvable status** (028/212/255/256/407/470/470a/479 carry `final_verdict`/`pass` but NOT
`status`|`outcome`|`overall_outcome` -- routing would `raise` in write_flat_manifest, NOT rename a
file) + **2 non-canonical dir** (683/686 write a hardcoded relative `f"../REE_assembly/.../{run_id}.
json"` single f-string, not a `<dir>/<fn>` split -- the migrator's path walk-up refuses). The other
8 UNMATCH in the 30-set are emit-only (187/445d/449c/455a/476/599/600/669; no raw flat-manifest
`json.dump` at all).

**Validation (batches 1-5 process).** Backward-compat **full-corpus NEW-vs-FROZEN** regression
(frozen = the post-batch-6 origin/main migrator): the ONLY decision change is the 12
UNMATCH->MIGRATE (every skip + all other unmatched byte-identical, incl. batch-6's own routes);
**0-diff** frozen-vs-new on 6 pre-migration canonical scripts (the new proof never fires for the
`manifest` fast path). **INDEPENDENT ORACLE** -- a SEPARATELY-implemented NodeVisitor scope model
(distinct code, same spec) re-derived from the immutable origin source PROVED the SAME 12 and
REFUSED the SAME 18; the oracle's OWN first cut CAUGHT a real nested-function scope-descent bug (a
nested predicate's `return` leaking into the helper's return set), and fixing it confirmed the
migrator's scope walker is the correct one. Per-script `py_compile` + AST-Path-bound 12/12 (exactly
one wfm call, one import, no residual raw dump of the mvar, `Path` bound). `validate_experiments
--strict --paths` over the 12: **12 manifest-writer findings CLEARED, 0 NEW** non-conforming
(`comm` diff: the residual degeneracy-self-report / arm-fingerprint / emit_outcome backlog is
finding-for-finding identical to origin -- orthogonal, out of scope). **Dry-run smoke**: 730
(return-bound) end-to-end -- **`substrate_hash` now populated** (was 0% of these flat manifests) +
machine/machine_class/recording_schema/seeds core, emit relocated the file to scratch (**no
evidence-dir leak**); 588c (write_text + AnnAssign) wfm-called (its dry-run leak into the `<TYPE>/`
subdir is PRE-EXISTING -- byte-identical to origin, whose `emit_outcome` likewise omits `dry_run`);
596 (assembled `output` INSIDE `run_experiment`) "DRY RUN OK" + a static scope proof that every name
in its wfm call is bound (its write early-returns in dry-run, so unreachable there -- the identical
transform is runtime-verified on 730/588c). Merge gate `pytest tests/` = **1437 passed, 0 failed,
39 subtests** (6:52). Staged on `integration/pack-writer-runid-varid` in a dedicated worktree off
`ree-v3` main (`.claude/worktrees/REE_assembly` symlink for the `test_arm_reuse` indexer-path
gotcha), rebased past batch-6 (`bf7724a`) + batch-5-HYBRID (`acd1a50`), ff-merged to `main`, branch
+ worktree removed. `elapsed_seconds` NOT retrofitted here (the §7.4 companion tool covers
newly-routed scripts as a follow-up).

**Updated remaining-unmatched taxonomy (21 unmatched of 1040, post-RUNID_only):**

| Unmatched class | ~count | Broadening needed | Risk |
|---|---|---|---|
| `no json.dump(manifest` tail, NOT byte-safe: **8 no resolvable status** (028/212/255/256/407/470/470a/479 -- `final_verdict`/`pass`, not status/outcome/overall_outcome) + **2 non-canonical dir** (683/686 hardcoded relative f-string path) | 10 | status-rename or dir-correction (a real edit, not mechanical) or `MANIFEST_WRITER_EXEMPT` | high |
| emit-only / harness, no raw flat-manifest `json.dump` (187/445d/449c/455a/476/599/600/669) | 8 | not lint-flagged -- no action needed | n/a |
| `no canonical with open` (3 idiosyncratic idioms) | 3 | per-script hand-migrate | med |

### Progress — step 3 no-canonical-with-open HYBRID, session 2026-07-13 (`vigorous-cohen-e338ad`; 3 scripts LANDED, ree-v3 main `46287fa`)

The **3 `no canonical with open` refusals** (`241a`/`241b`/`247`) — the migrator's
`no canonical with open(<path>, "w") as fh: above dump` UNMATCH reason. Inspected each write
idiom: all three are **early-era self-packing writers** that dump the identity-bearing
`manifest` (carrying `run_id` + `architecture_epoch` + `status` + `evidence_direction`)
straight to a **pack-subdir** path `REE_assembly/evidence/experiments/<TYPE>/runs/<run_id>/
manifest.json` (+ a sibling `metrics.json`), bypassing the flat→sync→pack chain — there is **no
canonical flat `<run_id>.json`**. `241a`/`241b` additionally write a thin runner pointer
`<TYPE>/<TYPE>_output.json` (filename ≠ `{run_id}.json`); `247` writes **only** the pack
manifest + `raw_metrics.json`, no flat sibling at all. So the migrator's refusal is correct:
`write_flat_manifest` writes `<out_dir>/f"{run_id}.json"`, so routing any of them would
**relocate** the manifest (pack-subdir → canonical flat) and/or **rename** the `<TYPE>_output.json`
pointer — a genuine *correction*, only justified for an ACTIVE script (and requiring a dry-run
smoke). **NOT a provably-safe idiom generalization** → no migrator change.

**Classify (queue + recent-run history).** Live queue held none of the 3. Recency = newest
`runs/<run_id>/` dir timestamp + `runner_status/*.json` `completed_at` per queue_id. **ALL 3
ARCHIVAL, ZERO active**: not queued; last actually run **2026-04-06…08 (~96–97d ago)** on
Daniel-PC / ree-cloud-1 / DLAPTOP-4 / EWIN-PC; the only on-disk manifests are the April bulk
backfill (`241a` supersedes `v3_exq_241_sd011_dual_nociceptive_stream_poc`; SD-011 lineage
carried forward by later `472_sd011_platform_stability_pilot`). Because zero are active, the
`run_id`/out_dir CORRECTION + dry-run-smoke path was **not exercised** (mirrors the edge-A / batch-5
archival exempts) — the exempt adds only an inert module constant.

→ mechanical module-level `MANIFEST_WRITER_EXEMPT` (per-script reason: `241a`/`241b` "writes
runs/<run_id>/manifest.json pack path + <TYPE>_output.json pointer; no canonical flat
<run_id>.json, so routing would relocate/rename; not queued, last run 2026-04, superseded lineage,
not re-run"; `247` the same minus the pointer, "routing would relocate"), inserted after the last
top-level import. Every changed file exactly **+2/-0**.

**Validation (batches 1-5 process).** 3/3 `py_compile`; `validate_experiments --strict --paths`
per-script **3→2 non-conforming** with a `comm` before/after diff proving the **only** removed
finding is the manifest-writer one and **0 NEW** (the residual 2 — missing `emit_outcome` +
degeneracy-self-report — are the pre-existing orthogonal backlog, out of scope). An **independent
classification oracle** (separate AST code, re-derives from git-HEAD source stripped of the exempt +
the queue + the evidence dir) confirmed **3/3 genuine raw-dump manifest writers AND non-canonical
[no `f"{run_id}.json"` write] AND archival [0 queued, 96–97d since last run]** → exempt justified.
Post-edit migrator: the 3 all report `skip`/`MANIFEST_WRITER_EXEMPT`; the `no canonical` class
**3→0**, full-corpus unmatched **21→18**. Merge gate `pytest tests/` = **1436 passed, 1 failed**
— the sole failure `tests/preflight/test_queue_integrity.py::test_queue_schema_valid` is a
**pre-existing live-fleet queue-snapshot race** (`V3-EXQ-749`, a concurrent-session MECH-457
GOV-FANOUT item, completed on ree-cloud-3 at 06:30:44Z while still in the `67fd2f8` snapshot); my
diff touches **0** of `experiment_queue.json` / tests / `ree_core`, so it fails identically on clean
origin/main. The 3 directly-exercising suites (`test_recording_standard` + `test_arm_fingerprint_lint`
+ `test_arm_reuse`) = **44 passed**. Staged on `integration/pack-writer-nocanonical-withopen-hybrid`
in a dedicated worktree off `ree-v3` main (`.claude/worktrees/REE_assembly` symlink for the
`test_arm_reuse` indexer-path gotcha), rebased past the concurrent `a059e33` queue snapshot (zero
file overlap), ff-merged to `main`, branch + worktree removed. `elapsed_seconds` N/A (exempt, not
routed).

**Cumulative: 670 of 1028** route through `write_flat_manifest` (unchanged — this pass routes 0)
**+ 344 `MANIFEST_WRITER_EXEMPT`** (341 + 3). Migrator unmatched **21→18** (the 3 exempt→skip). The
`no canonical with open` class is **DONE** (3→0). Remaining 18 unmatched (10 still lint-flagged):
the **10 `no json.dump(manifest` NOT byte-safe** (8 no resolvable status `028/212/255/256/407/470/
470a/479` + 2 non-canonical dir `683/686` — a status-rename or dir-correction, i.e. a real edit,
not mechanical; the `no-status` 8 are being handled by the concurrent `ree-v3-runid-nostatus`
session) + **8 emit-only/harness** (`187/445d/449c/455a/476/599/600/669`, no raw flat-manifest
`json.dump` — not lint-flagged, no action needed).

**Updated remaining-unmatched taxonomy (18 unmatched of 1043, post-no-canonical):**

| Unmatched class | ~count | Broadening needed | Risk |
|---|---|---|---|
| `no json.dump(manifest` tail, NOT byte-safe: **8 no resolvable status** (028/212/255/256/407/470/470a/479 — `final_verdict`/`pass`, not status/outcome/overall_outcome) + **2 non-canonical dir** (683/686 hardcoded relative f-string path) | 10 | status-rename or dir-correction (a real edit, not mechanical) or `MANIFEST_WRITER_EXEMPT` | high |
| emit-only / harness, no raw flat-manifest `json.dump` (187/445d/449c/455a/476/599/600/669) | 8 | not lint-flagged — no action needed | n/a |

### Progress — step 3 RUNID_only no-resolvable-status HYBRID, session 2026-07-13 (`charming-goldberg-195eca`; 8 scripts LANDED, ree-v3 main `5c20b42`)

The **8 "no resolvable status"** scripts honestly REFUSED by the RUNID_only var-identity batch
(`028`/`212`/`255`/`256`/`407`/`470`/`470a`/`479` — `detect_manifest_var`->None; the write path is
the ALREADY-canonical `<dir>/f"{run_id}.json"`, but the manifest carries
`final_verdict`/`pass`/`verdict`/`passed`, **NOT** `status`|`outcome`|`overall_outcome` — so routing
would `raise` on `write_flat_manifest`'s status guard, NOT rename a file). Applied the **HYBRID**
(classify vs queue + recent-run history; exempt archival / status-derive-and-route active).

**Classify (queue + recent-run history).** Live queue held **none** of the 8. Recency = canonical
top-level manifest presence at `evidence/experiments/<run_id>.json` + most-recent
`runner_status/*.json` `completed_at` per queue_id. **ALL 8 ARCHIVAL, ZERO ACTIVE**: none queued;
none run within the 40-45d window (last completions `028`=114d / `212`=100d / `255`=97d / `256`=97d /
`407`=89d / `470`=82d / `470a`=80d / `479`=79d ago); the `470`->`470a`->`479` sd029 lineage is
superseded within itself (`479` `_fix` is the latest, itself 79d unqueued); `255`/`256` (mech203
pair), `028`, `212`, `407` are each unqueued + >=89d. Because zero are active, the task's
status-derivation CORRECTION path (add a `status`/`outcome` field from the existing
`final_verdict`/`pass` via `/queue-experiment`, then route) was **not** exercised; the exempt path
adds an inert module constant with no runtime behaviour change, so no dry-run smoke applies (mirrors
the edge-A archival 267 + the batch-5 non-canonical 69 + the no-canonical-with-open 3).

-> mechanical module-level `MANIFEST_WRITER_EXEMPT = "archival early-era manifest (no resolvable
status key: carries final_verdict/pass/verdict/passed, not status/outcome/overall_outcome; unqueued,
last-run >=79d, not re-run)"`, inserted after the last top-level import by a **dedicated AST inserter**
(byte-preserving line insertion, idempotent; **no migrator change**). Every changed file exactly
**+1/-0**.

**Validation (batches 1-6 process).** 8/8 `py_compile`; `validate_experiments --strict --paths` over
the 8 = **manifest-writer findings 7->0, 0 NEW** non-conforming (`comm` diff BEFORE-vs-AFTER: the 7
removed lines are EXACTLY the 7 lint-flagged scripts' manifest-writer findings; the residual 15
`emit_outcome` / degeneracy-self-report backlog is finding-for-finding identical before vs after —
orthogonal, out of scope). **1 of the 8 (`028`) carries no `evidence_direction` token** so its exempt
is inert (batch-3 onboard_smoke / edge-A 18/267 / batch-5 18/69 precedent) — the other 7 are
lint-flagged. Merge gate `pytest tests/` at base `67fd2f8` = **1436 passed, 1 failed** — the sole
failure `tests/preflight/test_queue_integrity.py::test_queue_schema_valid` is the SAME
**live-fleet queue-snapshot race** the concurrent no-canonical session hit (`V3-EXQ-749`, a
MECH-457 GOV-FANOUT item, PASS on ree-cloud-3 at 06:30:44Z while still in the `67fd2f8` snapshot);
my diff touches **0** of `experiment_queue.json` / tests / `ree_core`, and the test **PASSES on clean
origin/main + on my rebased branch** (queue-integrity `2 passed` post-rebase onto `46287fa`, where the
snapshot no longer carries the 749 conflict). The 3 directly-exercising suites (`test_recording_standard`
+ `test_arm_fingerprint_lint` + `test_arm_reuse`) = **44 passed**. Staged on
`integration/pack-writer-runid-nostatus-exempt` in a dedicated worktree off `ree-v3` main
(`.claude/worktrees/REE_assembly` symlink for the `test_arm_reuse` indexer-path gotcha), rebased past
the concurrent `241a`/`241b`/`247` no-canonical exempt + queue snapshot (`46287fa`; **zero file
overlap**), ff-merged to `main`, branch + worktree removed. `elapsed_seconds` N/A (exempt, not routed).

**Cumulative: 670 of 1028** route through `write_flat_manifest` (unchanged — this pass routes 0)
**+ 352 `MANIFEST_WRITER_EXEMPT`** (344 + 8). Migrator unmatched **18->10** (the 8 exempt->skip).
Remaining 10 unmatched (2 still lint-flagged): **2 non-canonical dir** (`683`/`686` hardcoded relative
f-string path — a dir-correction, a real edit, only for an active script) + **8 emit-only / harness**
(`187`/`445d`/`449c`/`455a`/`476`/`599`/`600`/`669`; no raw flat-manifest `json.dump`, not
lint-flagged — no action). The `no json.dump(manifest` no-resolvable-status class is **DONE** (8->0).

**Updated remaining-unmatched taxonomy (10 unmatched of 1043, post-no-resolvable-status):**

| Unmatched class | ~count | Broadening needed | Risk |
|---|---|---|---|
| `no json.dump(manifest` tail, NOT byte-safe: **2 non-canonical dir** (683/686 hardcoded relative f-string path) | 2 | dir-correction (a real edit, only for an active script) or `MANIFEST_WRITER_EXEMPT` | high |
| emit-only / harness, no raw flat-manifest `json.dump` (187/445d/449c/455a/476/599/600/669) | 8 | not lint-flagged — no action needed | n/a |

### Progress — step 3 683/686 no-run_id non-canonical-dir HYBRID, session 2026-07-13 (`exciting-jang-7bee3b`; 2 scripts LANDED, ree-v3 main `7cb21eb`)

The **2 non-canonical-dir** residual (`683`/`686`) — the last entries in the `no json.dump(manifest`
NOT-byte-safe class. Applied the **HYBRID** (classify vs queue + recent-run history; exempt archival /
correct-and-route active). **Both ARCHIVAL → `MANIFEST_WRITER_EXEMPT`.** This **clears the lint-flagged
migration backlog** (the only residual is now the 8 emit-only/harness scripts, no action).

**Correction to the prior taxonomy's "2 still lint-flagged".** Empirically **neither 683 nor 686 was
flagged by `manifest_writer_lint`** — `validate_experiments --strict --paths` reported **0
manifest-writer-backlog** on both BEFORE the edit. The lint keys on the manifest-identity STRING tokens
`("run_id", "evidence_direction")` (`validate_experiments.py` `_MANIFEST_IDENTITY_TOKENS`); both scripts
carry the `"evidence_direction"` string but the STRING `"run_id"` is **absent** — their `result` dict has
no `"run_id"` KEY (`run_id` exists only as a local var in the `__main__` block), so `writes_manifest` is
False and the lint never fires. They were only ever in the **migrator UNMATCHED** set (reason
`no json.dump(manifest tail`, `detect_manifest_var`→None), not the lint backlog. So the exempt is **inert
w.r.t. `manifest_writer_lint`** (mirrors the batch-3 onboard_smoke / edge-A 18/267 / batch-5 18/69 /
no-status `028` inert-exempt precedent); its real effect is migrator unmatched→skip + an explicit archival
provenance record (and it robustly discharges the lint if a future `"run_id"` key is ever added — exactly
what a correct-and-route would do).

**Sharper than the prior "non-canonical dir" label.** Both write `result` (a `run_experiment()` return)
to a SINGLE hardcoded relative f-string `f"../REE_assembly/evidence/experiments/{run_id}.json"` (no
`<dir>/<fn>` split → the migrator's path walk-up refuses) AND `result` carries **no `run_id` key** (only
`architecture_epoch`+`outcome`). So routing through `write_flat_manifest` is a **correct-and-route**
(inject `result["run_id"] = run_id` + split the dir), NOT a byte-safe mechanical migration — only
justified for an ACTIVE script.

**Classify (queue + recent-run history).** Live queue held neither (2 items, neither 683/686). Recency =
canonical manifest at `evidence/experiments/<run_id>.json` + `runner_status/*.json` completion per
queue_id. **BOTH ARCHIVAL, ZERO active**: not queued; **never ran** — zero evidence manifest (flat or
pack run dir) for either TYPE, zero `runner_status` completion on any machine; `V3-EXQ-683` was queued
2026-06-15/17 + `V3-EXQ-686` 2026-06-16/18/21 then dropped from the snapshot without producing evidence.
Both are proxies for a substrate V3 lacks — `683`/MECH-048 uses temperature as a mu/kappa-stability-overlay
proxy ("V3 doesn't yet have dedicated mu/kappa modules"); `686`/MECH-191 is the within-agent precondition
for cross-arch signal legibility (substrate-blocked on V3, no multi-agent env). Because zero are active,
the `run_id`/dir CORRECTION + dry-run-smoke path was **not exercised** (mirrors every prior archival
exempt); the exempt adds only an inert module constant.

→ mechanical module-level `MANIFEST_WRITER_EXEMPT` (per-script reason: non-canonical relative f-string +
no `run_id` key → correct-and-route not byte-safe; unqueued, never ran, substrate-blocked proxy, not
re-run), inserted after the last top-level import. Every changed file exactly **+10/−0** (multi-line
reason string).

**Validation (batches 1-6 process).** 2/2 `py_compile`; migrator full-corpus **unmatched 10→8** (both now
report `skip`/`MANIFEST_WRITER_EXEMPT`; the frozen-vs-new decision change is exactly the 2 UNMATCH→skip,
every other skip/unmatched byte-identical); `validate_experiments --strict --paths` over the 2 = **0
removed / 0 NEW** (`comm` before/after: the finding SET is byte-identical — `0 manifest-writer-backlog`
before AND after, confirming the inert exempt; the sole residual non-conforming is `683`'s PRE-EXISTING
degeneracy-self-report finding, orthogonal + out of scope, unchanged). An **independent classification
oracle** (separate code from the migrator/lint; re-derives from the immutable `git origin/main:` source +
the live queue + the evidence dir + `runner_status`) confirmed **2/2 genuine raw-dump manifest writers**
(raw `json.dump`, `evidence_direction`, returned dict carries `architecture_epoch`+`outcome`) **AND 2/2
non-canonical + no-run_id-key** (single relative f-string, no `"run_id"` dict key, `run_id` local var)
**AND 2/2 archival** (0 queued, 0 evidence, 0 `runner_status`) → exempt-justified; the oracle first
FALSE-refused `683` on a `return <Name>` scan that missed the `summary = {..}; return summary` binding (a
real oracle bug → fixed by also collecting keys from a dict-literal bound to a returned name, confirming
the oracle is genuinely independent). The 3 directly-exercising suites (`test_recording_standard` +
`test_arm_fingerprint_lint` + `test_arm_reuse`) = **44 passed**. Merge gate `pytest tests/` = **1437
passed, 0 failed, 39 subtests (13:16)**. Staged on `integration/pack-writer-683-686-noruncanonical-exempt`
in a dedicated worktree off `ree-v3` origin/main (`.claude/worktrees/REE_assembly` symlink for the
`test_arm_reuse` indexer-path gotcha), ff-merged to `main`, branch + worktree removed. `elapsed_seconds`
N/A (exempt, not routed).

**Cumulative: 670 of 1028** route through `write_flat_manifest` (unchanged — this pass routes 0) **+ 354
`MANIFEST_WRITER_EXEMPT`** (352 + 2). Migrator unmatched **10→8** (the 2 exempt→skip). The
`no json.dump(manifest` NOT-byte-safe class is **DONE** (2 non-canonical-dir → 0). **The lint-flagged
migration backlog is FULLY CLEARED** — the remaining **8 unmatched** are all emit-only / harness
(`187`/`445d`/`449c`/`455a`/`476`/`599`/`600`/`669`) with no raw flat-manifest `json.dump` (not
lint-flagged, no action needed; `MANIFEST_WRITER_EXEMPT`-eligible only if a future pass wants them off the
unmatched count).

**Updated remaining-unmatched taxonomy (8 unmatched of 1043, post-683/686):**

| Unmatched class | ~count | Broadening needed | Risk |
|---|---|---|---|
| emit-only / harness, no raw flat-manifest `json.dump` (187/445d/449c/455a/476/599/600/669) | 8 | not lint-flagged — no action needed (exempt-eligible only to zero the unmatched count) | n/a |

### Progress — step 3 683/686 correct-and-route OVERRIDE, session 2026-07-13 (`admiring-pasteur-85116f`; 2 scripts LANDED, ree-v3 main `8f4a76a`)

**Supersedes the `7cb21eb` exempt above** (user-decided). The prior session `exciting-jang-7bee3b`
classified `683`/`686` ARCHIVAL → `MANIFEST_WRITER_EXEMPT` by the standing "unqueued + never-ran →
exempt" precedent. On review the user directed a **correct-and-route** instead, because the precedent's
exempt rule was written for a *different* condition than these two present:

- **The prior archival exempts (edge-A 267 / batch-5 69 / no-canonical 3 / no-status 8) were exempted
  because routing them would RENAME or RELOCATE the flat file** — a real risk with no upside for a dead
  script. **That condition does NOT hold for 683/686:** routing is **byte-location-identical** —
  `write_flat_manifest(result, Path("../REE_assembly/evidence/experiments"), ...)` writes to the exact same
  `.../{run_id}.json` the raw `json.dump` did (no rename, no relocate).
- **Routing repairs a genuine latent defect.** `result` carries **no `run_id` key** (only a `__main__`
  local var in the path f-string). `sync_v3_results._is_flat_v3` reads `run_id` **from the manifest dict**
  (`run_id = str(data.get("run_id",""))` → `if run_id.endswith("_v3")`); with no key it is `""` → the gate
  **fails → the manifest is never converted to a pack, never scored.** So if either ever ran, its result
  would be written and then **silently dropped** by the pipeline. Injecting `result["run_id"] = run_id`
  (what a correct-and-route does; what `write_flat_manifest` also requires) is what makes the manifest
  scoreable at all — exempt freezes the broken state in place.
- **Cost asymmetry favors routing.** Routing is correct whether or not the script ever runs again and adds
  the always-core; exempt is correct *only* if these are permanently dead, and a wrong-exempt is a silent,
  unscoreable run with the lint deliberately quieted. The correct-and-route is cheap and pre-designed.

**The edit (each script, +18/−19 net vs `7cb21eb`).** Remove the 10-line `MANIFEST_WRITER_EXEMPT`
constant + add `from experiments.pack_writer import write_flat_manifest`; in the non-dry `else:` branch,
add `result["run_id"] = run_id`, `out_dir = Path("../REE_assembly/evidence/experiments")`, and route the
raw `with open()/json.dump(result)` through `out_path = write_flat_manifest(result, out_dir, dry_run=False,
config=result.get("config"), seeds=result.get("seeds"), script_path=Path(__file__))`, preserving the
`emit_outcome(manifest_path=out_path)` handoff. `dry_run=False` is byte-faithful (the write is only reached
in the non-dry branch); `run_id` already ends `_v3` (`require_v3` passes); `Path` already imported.

**MATERIAL FINDING — both experiment BODIES are substrate-drifted and cannot currently run.** The write-tail
smoke (running each `run_experiment` for real against the current substrate) surfaced that **neither script
executes**: `683` → `CausalGridWorld.__init__() got an unexpected keyword argument 'device'` (env API dropped
`device=` since 2026-06-15); `686` → `mat1 and mat2 shapes cannot be multiplied (1x200 and 54x54)` (agent/env
shape drift). This is **identical on `origin/main`** (present in both the exempt and pre-exempt versions) and
**orthogonal to the write-tail migration** — but it means these are dormant-pending-a-body-fix, not merely
dormant-pending-substrate: any future resurrection must fix the body too. The value of routing now is that
the manifest write is already correct for that eventual run (and the missing-`run_id` scoring hole is closed).

**Validation (batches 1-6 process).** 2/2 `py_compile`. `validate_experiments --strict --paths` BEFORE
(`7cb21eb` exempt) vs AFTER (routed) = **identical**: `0 manifest-writer-backlog` both (exempt suppresses it
BEFORE; `write_flat_manifest` name-presence satisfies it AFTER), **0 NEW** non-conforming (the sole residual
is `683`'s PRE-EXISTING degeneracy-self-report finding — orthogonal, unchanged; `686` already calls
`check_degeneracy`). **Write-path smoke** (scratch out_dir, no evidence-dir leak): `683` via its real dry
result + `686` via a real-shaped result (with `seeds`) both land the canonical `<run_id>.json` with the
**always-core COMPLETE** — `substrate_hash` populated (was 0% of these flat manifests),
`machine`/`machine_class`/`recording_schema`/`seeds`/`run_id`/`architecture_epoch` all set — and the
`_is_flat_v3` `run_id`-endswith-`_v3` gate now **PASSES** (the defect the route repairs). (The dry-run branch
does NOT reach the write, so `--dry-run` alone cannot smoke `write_flat_manifest`; the scratch harness
exercises the real write tail.) Merge gate `pytest tests/` = **1437 passed, 0 failed, 39 subtests (1:18:48,
contention-slow)**. Staged on `integration/pack-writer-noncanonical-dir-683-686` in a dedicated worktree off
`ree-v3` origin/main (`.claude/worktrees/REE_assembly` symlink for the `test_arm_reuse` indexer-path gotcha),
ff-merged to `main`, branch + worktree removed. `elapsed_seconds` NOT retrofitted here (the §7.4 companion
tool covers newly-routed scripts as a follow-up; both would qualify only after a `datetime.now(timezone.utc)`
timer is added — they import `datetime` only, so they are by-design advisory gaps like the batch-7 12).

**Cumulative: 672 of 1028** route through `write_flat_manifest` (670 + 2) **+ 352 `MANIFEST_WRITER_EXEMPT`**
(354 − 2, the 683/686 exempts removed). Migrator unmatched stays **8** (683/686 move from exempt-skip to
routed-skip; both remain non-unmatched). The lint-flagged migration backlog remains fully cleared; the 8
emit-only/harness scripts are the only residual unmatched (no raw flat-manifest `json.dump`, not
lint-flagged — no action).

Shape families (survey; total 1,028; migrate top-down):

| # | Family | ~count | Distinguishing keys | Migration note | Status |
|---|---|---|---|---|---|
| 1 | A. Legacy status/metrics | 268 | `status`, `metrics`, `summary_markdown`, `fatal_error_count` | shares backbone w/ B+I | pending |
| 2 | B. Criteria / per-claim diagnostic | 273 | `experiment_purpose`, `evidence_direction_per_claim`, `criteria`, `config_summary` | shares backbone | pending |
| 3 | I. Other minimal | 131 | `status`/`outcome`/`metrics` only | shares backbone | pending |
| — | **(A+B+I = 672, ~65% — one "flat metrics + evidence fields" backbone; do first)** | | | | |
| 4 | D. arm_results / per_arm grid | 172 | `arm_results`, `per_arm`, `acceptance` | multi-arm hoist path | pending |
| 5 | F. Recent interpretation+result | 57 | `interpretation`, `non_degenerate`, `env_kwargs`, `result` | the 724/73x lineage | pilot 734/735/736/737 DONE (`8f7ee9d`); rest via canonical batch |
| 6 | E. Multi-arm acceptance | 39 | `acceptance_checks`, `per_arm_summaries`, `thresholds` | pending |
| 7 | C. schema_version + outcome (mid-era) | 76 | `schema_version`, `outcome`, `criteria_met`, `supersedes` | pending |
| 8 | G. INV maturational grid | 4 | `by_onset`, `preconditions_met`, `claim_pass` | pending |
| 9 | H. Ceiling/readiness probe | 3 | `readiness`, `per_rung`, `load_bearing_dv` | 737/738/742 | pending |
| 10 | Z. Unclassified | 5 | idiosyncratic | hand-migrate | pending |

**Migration edge-cases the batch must handle** (survey §D):
- **Early-era path (EXQ-001..~025, ~25 scripts)** write to a **ree-v3-local** `parents[1]/evidence/experiments/<TYPE>/<type>_<ts>.json`, not the canonical `REE_assembly/evidence/experiments/<run_id>.json`, and use a `<type>_<ts>.json` filename. `write_flat_manifest` keys on `run_id`; these need their `run_id` + out_dir corrected first (or an explicit exempt).
- **Multi-manifest writers (~24 scripts)** dump `runs/<run_id>/{manifest,metrics}.json` **plus** a flat `<type>_output.json` — decide per-script whether the flat or the pack write is the one to route.
- **ERROR-only onboarding smokes** (`v3_onboard_smoke_*`) write a `{status,error,traceback,run_id,...}` crash shape — mark `MANIFEST_WRITER_EXEMPT`.
- **`_lib/rebinding_functional_harness.py`** is an informal convergence point (recent F-family routes evidence-direction through `H.evidence_direction`); fold it onto the chokepoint too.

### Progress — step 3 `no json.dump(manifest` tail: independent all-refuse confirmation, session 2026-07-13 (`brave-ishizaka-fa60b4`; NO code change, doc-only)

Independent re-verification of the **18-script `no json.dump(manifest` residual** left after
the RUNID_only var-identity batch routed 12 (`31eb700`). This session was tasked to route the
byte-safe ones and REFUSE (documented) the rest; **the entire residual is genuinely un-routable
— 0 routed, 18 refused** — confirming the RUNID_only taxonomy table above from origin source, with
one sharpened finding. **Disjoint by construction** from the concurrent sessions carving up this
same tail: `charming-goldberg-195eca` (the 8 no-status → archival `MANIFEST_WRITER_EXEMPT`) and
`vigorous-cohen-e338ad` (241a/241b/247 `no canonical with open`). This session touched **only the
8 no-status's siblings** — the **2 non-canonical-dir + 8 emit-only** — and made **no ree-v3 change**
(exempt-insertion is those sessions' scope; the mandatory worktree/integration/pytest gates are
vacuous with 0 scripts routed).

Per-script proof (AST, from origin source) of why each refuses — all three failure modes hit
`write_flat_manifest`'s own raise-guards, so routing would BREAK the run, not rename a file:

- **8 no resolvable status** (`028`/`212`/`255`/`256`/`407`/`470`/`470a`/`479`) — the written var
  (`run_pack`/`result`/`output`/`summary`) carries `final_verdict` / `pass` / `verdict` / `passed`
  but NONE of `status`|`outcome`|`overall_outcome`, so `write_flat_manifest` raises at its
  `_resolve_flat_status(...) is None` guard. **Owned by `charming-goldberg`** (archival-exempt
  pass) — confirmed here, not modified.
- **2 non-canonical dir + no-run_id** (`683`/`686`) — SHARPER than the table's "non-canonical dir":
  both write `result` (a `run_experiment()` return) to a single hardcoded relative f-string
  `f"../REE_assembly/evidence/experiments/{run_id}.json"` (no `<dir>/<fn>` split → the migrator's
  path walk-up refuses) AND, independently, **`result` carries no `run_id` key at all** (verified:
  zero `"run_id"` literals in either file; `run_id` exists only as a local var consumed by the path
  f-string). Both carry `architecture_epoch`+`outcome`, so they are *almost* flat manifests, but the
  missing `run_id` trips `write_flat_manifest`'s "requires a non-empty string 'run_id'" guard on top
  of the dir issue. Routing is therefore a **correct-and-route** (inject `result["run_id"] = run_id`
  + split the dir), NOT a byte-safe mechanical migration — REFUSED here, left as a follow-up.
- **8 emit-only / harness** (`187`/`445d`/`449c`/`455a`/`476`/`599`/`600`/`669`) — no raw
  flat-manifest `json.dump` exists to route (already "not lint-flagged — no action needed" in the
  table). Sub-classified for the resume record: `187` is a 49-line STUB (`sys.exit(1)`);
  `445d`/`449c`/`455a`/`476` `raise NotImplementedError` (substrate-blocked, "do not run until
  SD-037 lands"); `599`/`600` call `experiment_protocol.emit_outcome(...)` (which writes only the
  runner sentinel `<signal_dir>/<queue_id>.json`) with NO `manifest_path` and no evidence write;
  `669` builds a flat `manifest` dict but **never persists it** — it passes it (malformed, dict as
  the first positional `outcome`) to `emit_outcome`, and its `run_id` lacks `_v3`. All correctly
  refused; the pure stubs (`187`/`445d`/`449c`/`455a`/`476`) + emit-only (`599`/`600`) are
  `MANIFEST_WRITER_EXEMPT`-eligible if a future pass wants to clear them from the unmatched count;
  `669`'s malformed emit_outcome + non-`_v3` run_id is a pre-existing script bug (out of scope).

**Net: the `no json.dump(manifest` tail is exhausted** — 12 routed (`31eb700`) + 18 refused (8 no-status
[charming-goldberg exempt], 2 non-canonical-dir+no-run_id [683/686, follow-up], 8 emit-only). No
migrator or script change in this session.

---

## 7. Follow-ups (deferred; sequence after the top-3 families migrate)

1. **Unify the pack skeleton.** Make `sync_v3_results.build_runpack_docs` and `pack_writer.write_pack` delegate to ONE shared skeleton so they cannot drift. Update the golden byte-shape test (`coordinator/test_phase3_runpack_materialize.py`) in the same change.
2. **Carry the always-core through sync into the pack** (`substrate_hash`/`config`/`seeds`/`machine`/`elapsed_seconds` + `non_degenerate`/`arm_results`/`label_balance`), so the indexer can eventually score on always-core inputs. This is the standard §4 "deliberately still open: making these fields load-bearing to confidence scoring" — needs user sign-off (changes promotion math).
3. **Harden the lint to a commit gate. DONE — 2026-07-13, session `zen-spence-0bb075` (`pack_writer §7.3 harden lint to commit gate`), ree-v3 main `7ce1721`.** With the backlog cleared (670 routed + 352 `MANIFEST_WRITER_EXEMPT` = ~1022/1028; ~10 irreducible residual), added a commit-time gate that blocks a NEW/modified experiment script from reintroducing a raw `json.dump` manifest tail. The lint (`validate_experiments.manifest_writer_lint`) was already HARD under `--strict --paths`; this was **wiring, not new lint logic** (§7 item 2's semantics unchanged). Three parts:
   - **`validate_experiments.py --checks` selector** (new): `CHECK_NAMES` + a `--checks` arg gate each check block; default (None) runs all (backward-compatible — only `test_arm_fingerprint_lint` + the new `test_manifest_writer_lint` reference this module, both green). `--checks manifest_writer` runs ONLY the manifest-writer lint, keeping the gate **surgical** — it does NOT expand the emit_outcome-conformance / degeneracy / arm-fingerprint contracts onto the broader `v3_*.py` set the gate scopes.
   - **`scripts/precommit_contracts.sh` Block 1b**: runs `validate_experiments.py --strict --quiet --checks manifest_writer --paths <staged>` over `git diff --cached --name-only --diff-filter=ACM -- 'experiments/v3_*.py'` (broader than Block 1's `v3_exq_*` glob — a raw dump is a regression in ANY v3 script; this is the **net-new coverage**, since Block 1 already ran the full lint on staged `v3_exq_*`). Blocks on any finding (exit 2), respects `MANIFEST_WRITER_EXEMPT`, no-op when no v3 script is staged (docs/queue-only commits unaffected). Invoked by the Claude Code `settings.json` PreToolUse hook (no `settings.json` change needed — it already calls `precommit_contracts.sh`; and `.claude/settings.json` is gitignored/untracked, so nothing to land there).
   - **Real git hook for ALL committers** (user-chosen 2026-07-13: "both"): `scripts/git-hooks/pre-commit.local` (tracked source) runs `precommit_contracts.sh`, installed via `scripts/install_precommit_gate.sh` into `.git/hooks/pre-commit.local` — the CHAIN SLOT the clinical-hours guard's top-level `pre-commit` already `exec`s (installer adds a minimal chainer if no top-level hook exists). Covers plain-CLI / other-agent commits, not just Claude Code. Deliberately does NOT run `validate_queue` in the git hook (it fails on a stale local queue — which the writers move every minute — and would block plain-CLI committers, the most likely to be a few commits behind, on state unrelated to their commit; queue integrity stays covered on the Claude Code path). Mac/dev only — never on cloud workers/hub.
   - **Full-glob advisory stays advisory** (per the task constraint): the ~10 irreducible residual + any un-migrated legacy never block unrelated commits — the gate keys strictly on staged/changed `v3_*.py`.
   - **Validation:** end-to-end via an isolated `GIT_INDEX_FILE` (no touch to the real index): gate BLOCKS a regressed staged script (raw `json.dump` + identity tokens; both a `v3_exq_` shape via Block 1's full run AND a non-`v3_exq_` `v3_mech` shape via Block 1b — proving the scope widening), PASSES a routed (`write_flat_manifest`) script and a `MANIFEST_WRITER_EXEMPT` one, PASSES a fully-conformant `v3_exq_` routed script through BOTH blocks, and is a silent no-op for docs-only / queue-only / nothing-staged commits. The installed `pre-commit` hook (clinical guard -> `pre-commit.local` -> `precommit_contracts.sh`) blocks a regression with exit 2 end-to-end. New suite `tests/contracts/test_manifest_writer_lint.py` (10 contracts: detection/route/exempt/no-identity/no-dump/no-main + the `--checks manifest_writer` HARD-block / surgical-isolation / exempt behaviours). Merge gate `pytest tests/` = **1447 passed, 39 subtests** (directly-exercising suites `test_manifest_writer_lint` + `test_arm_fingerprint_lint` + `test_recording_standard` + `test_arm_reuse` = 54 passed). Landed direct to ree-v3 `main` (single-session tooling change, not `ree_core`/`coordinator` — per the code-plane policy an integration branch is not required).
4. **`elapsed_seconds` retrofit for the batch. DONE (two passes) — batch-1/2: 2026-07-12, session `nifty-cerf-c06cab`, ree-v3 main `47ed14a`; batch-3: 2026-07-12, session `pack-writer-elapsed-b3`, ree-v3 main `d57e893`.** Companion tool [`ree-v3/tools/retrofit_elapsed_seconds.py`](../../../ree-v3/tools/retrofit_elapsed_seconds.py) — a SEPARATE tool from `migrate_manifest_writers.py`, to avoid a same-file conflict with the concurrent batch-3 migrator session. For each script routed through `write_flat_manifest`, it retrofits (mirroring the F pilot) `_run_started = datetime.now(timezone.utc)` immediately after the parse_args line + threads `elapsed_seconds=(datetime.now(timezone.utc) - _run_started).total_seconds()` into the `write_flat_manifest(...)` call, **ONLY where BOTH** (a) `datetime` AND `timezone` are imported unaliased (so `datetime.now(timezone.utc)` resolves; no shadowing bare `import datetime`) AND (b) there is exactly ONE unambiguous `args = <parser>.parse_args()` anchor that is a direct statement of its enclosing function body, with the (single) `write_flat_manifest` call in that **same** scope, after the anchor. Everything is AST-driven (parents/scope map), not regex.
   - **68 retrofitted.** Left as advisory gaps **BY DESIGN**: **165** — 163 never import `timezone` (they timestamp via `datetime.utcnow()`/`datetime.now()` without it; forcing a `timezone` import is out of scope), 5 have no in-scope parse_args anchor (e.g. the 705/706 mech314 family parse args inside `if __name__` but write inside `run_experiment()` — a module-global `_run_started` there would `NameError` if the function is imported without `__main__`). Plus **4 already conform** via `started_at=` — `stamp_recording_core` derives `elapsed_seconds` from `started_at` (perf_counter delta) when `elapsed_seconds` is absent, so the tool skips any call already passing `started_at`/`elapsed_seconds`.
   - **Validation:** byte-equivalent vs a hand retrofit of 611 (the tool's output is identical to the pilot-shape hand edit); every changed file exactly **+2/-0**; all 68 `py_compile` clean + AST-verified (exactly one `_run_started`, the call now carries `elapsed_seconds`, no stray `started_at`). Gap-close proven through the **real** `write_flat_manifest` → `stamp_recording_core` → `validate_recording --strict` path (BEFORE shape: "missing elapsed_seconds" blocking gap; AFTER the injected kwarg: "OK, 1 complete, 0 gaps"). `validate_experiments --strict --paths` over the 68: **0-new-non-conforming** (identical 16-finding pre-existing degeneracy-self-report / emit_outcome backlog before vs after — orthogonal, out of scope). Merge gate `pytest tests/` = **1414 passed, 0 failed** (the 3 directly-exercising suites — recording_standard + arm_fingerprint_lint + arm_reuse/indexer — 44 passed). Staged on `integration/pack-writer-elapsed-retrofit` in a dedicated worktree off `ree-v3` main.
   - **Batch-3 pass (35 retrofitted, ree-v3 main `d57e893`).** Re-ran the same tool over the batch-3-migrated set (`git ls-files experiments/v3_*.py`); the 68 batch-1/2 scripts correctly SKIP (already carry `elapsed_seconds`). Of the **412** scripts now routing through `write_flat_manifest` that pass neither `elapsed_seconds` nor `started_at`, **126** import `timezone` (upper-bound eligible); the parse_args-anchor check narrowed to **35 retrofitted** — all last-touched by the batch-3 migrator commits (30 class3 non-`manifest`-var `f407ddd` + 5 class2 non-adjacent-out_path `e636530`). The remaining **377** stay advisory gaps **BY DESIGN**: 286 never import `timezone`, 91 have no in-scope parse_args anchor. **Not touched** per the follow-up scope (no `timezone` import forced). **Validation:** byte-equivalent vs a hand retrofit of `481` (identical to the pilot-shape edit); every changed file exactly **+2/-0**; all 35 `py_compile` clean + AST-verified (exactly one `_run_started`, call carries `elapsed_seconds`, no stray `started_at`). Gap-close re-proven through the real `write_flat_manifest` → `stamp_recording_core` → `validate_recording --strict` path (BEFORE: "missing elapsed_seconds" exit 1; AFTER: "OK, 1 complete, 0 gaps" exit 0). `validate_experiments --strict --paths` over the 35: **0-NEW-non-conforming** (identical 15-OK / 55-finding pre-existing degeneracy-self-report / emit_outcome backlog before vs after — orthogonal, out of scope). Merge gate `pytest tests/` = **1420 passed, 0 failed, 39 subtests**. Staged on `integration/pack-writer-elapsed-retrofit-b3` in a dedicated worktree off `ree-v3` main (`.claude/worktrees/REE_assembly` symlink present for the `test_arm_reuse` indexer-path gotcha). Cumulative retrofit total: **103** (68 + 35).
   - **Batch-4 pass (0 retrofitted of 145; 2026-07-12, session `optimistic-babbage-363511`, NO ree-v3 commit).** Ran the same tool over exactly the **145** scripts routed by the batch-4 scripts commit (ree-v3 main `681f490`; file list = `git show 681f490 --name-only -- 'experiments/v3_*.py'`, disjoint from the batches-1/2/3 already-retrofitted set by construction). Result: **0 retrofit, 0 skip, 145 unmatched** — the tool's `--apply` was a verified **no-op (0 files changed, worktree clean)**, so there is no code delta to land in ree-v3 and the merge gate is vacuous. **All 145 are by-design advisory gaps**, split exactly by which precondition fails: **117** fail (a) — no unaliased `timezone` import (they timestamp via `datetime.utcnow()`/a bare `import datetime`/an internal `time.time()` timer; forcing a `timezone` import is out of scope); **28** fail (b) — no unambiguous in-scope `parse_args` anchor, of which **4** carry no argparse at all (the `write_flat_manifest` call sits in `run_experiment()` with no `args = ...parse_args()`) and **24** are the 705/706-style **scope-split** (`args = parser.parse_args()` lives in the module-level `if __name__` guard while the wfm call is inside a helper `main()`/`_write_manifest()` — injecting `_run_started` at the anchor would `NameError` in the helper). **Verification (why 0 is correct, not a tool miss):** the **12** of the 28 that DO import `timezone` unaliased (172/176/177/196 no-argparse; 461/481b/599a/600a/601/712/716/716a scope-split) were each AST-inspected — all 12 legitimately fail precondition (b), so the tool refuses them exactly per its documented contract; hand-retrofitting them via a different injection site would exceed the `retrofit_elapsed_seconds.py` contract and the §7.4 scope (the scope-split case is called out as a by-design gap). **Genuine-gap sizing (informational):** of the 145, only **106** actually lack `elapsed_seconds` after the full stamp path — the other **39** already carry it via an internal `time.time()`/`time.perf_counter()` timer written into the manifest dict, which `stamp_recording_core`'s fill-only `_fill` preserves (so those 39 are not even a recording gap). No `pytest`/`validate_experiments` diff to report (zero code change). **Cumulative retrofit total unchanged: 103** (68 + 35 + 0). This exhausts the mechanically-retrofittable population through batch 4; any future recovery of these 145 would need either the older scripts to migrate to the in-function `parse_args` idiom, or a scoped extension of the retrofit tool to inject at the wfm-enclosing-function head (out of current scope — a deliberate follow-up, not a bug).
   - **Batch-5 pass (1 retrofitted of 15; 2026-07-13T05:23Z, session `pack_writer §7.4 batch-5 elapsed retrofit`, ree-v3 main `a442440`).** Ran the same tool over exactly the **15** scripts routed by the batch-5 scripts commit (ree-v3 main `ae74b63` — the non-canonical-filename class). Result: **1 retrofit, 0 skip, 14 unmatched**. **Retrofitted (1):** `v3_exq_527_mech112_identity_goal_reef` — imports `datetime`+`timezone` unaliased AND has exactly one in-function `args = parser.parse_args()` anchor (in `_main()`) with the single `write_flat_manifest` call in the **same** scope after it; +2/-0. **By-design advisory gaps (14):** split by failing precondition — **2** fail (a) no unaliased `timezone` import: `051b` (no `from datetime import …` at all) + `526` (imports `datetime` **only**, no `timezone` — forcing a `timezone` import is out of scope, NOT done); **12** fail (b) no unambiguous in-scope `parse_args` anchor, of which **5** carry no argparse at all (`184`/`264`/`266`/`266a`/`308` — the `write_flat_manifest` call sits in `main()`/a nested block with no `args = …parse_args()`) and **7** are the 705/706-style **scope-split** (`265`/`265a`/`267`/`355`/`355a`/`429`/`430` — all import `timezone` unaliased but `args = parser.parse_args()` lives in the module-level `if __name__` guard while the wfm call is inside `main()`; injecting `_run_started` at the anchor would `NameError` in `main()`). All 7 scope-split scripts were AST-inspected and legitimately fail (b) — the tool refuses them exactly per its documented contract (same class as batch-4's 705/706). **Validation:** byte-equivalent vs an independent hand retrofit of `527` (**IDENTICAL**); the one changed file is exactly **+2/-0**; `py_compile` clean + AST-verified (exactly one `_run_started`, call carries `elapsed_seconds`, no stray `started_at`). Gap-close proven through the **real** `write_flat_manifest` → `stamp_recording_core` → `validate_recording --strict` path (BEFORE: "missing elapsed_seconds" exit 1; AFTER: "OK, 1 complete, 0 gaps" exit 0). `validate_experiments --strict --paths` over `527`: **0-NEW-non-conforming** (identical 2 pre-existing `emit_outcome` / degeneracy-self-report backlog findings before vs after — orthogonal, out of scope). Merge gate `pytest tests/` = **1437 passed, 0 failed, 39 subtests** (3 directly-exercising suites `test_recording_standard` + `test_arm_fingerprint_lint` + `test_arm_reuse`: **44 passed**). Staged on `integration/pack-writer-elapsed-retrofit-b5` in a dedicated worktree off `ree-v3` main (`.claude/worktrees/REE_assembly` symlink present for the `test_arm_reuse` indexer-path gotcha), ff-merged to `main`, branch deleted on merge. **Cumulative retrofit total: 104** (68 + 35 + 0 + 1).
   - **Batch-6 pass (0 retrofitted of 9; 2026-07-13, session `pack_writer §7.4 batch-6 elapsed retrofit` [`gifted-kilby-8e2491`], NO ree-v3 commit).** Ran the same tool over exactly the **9** scripts routed by batch 6 (ree-v3 main `bf7724a`; the `no out_dir assignment` param-dir class `621`/`621a`/`622`/`626`/`626a`/`626b`/`636`/`637` + the `354` real-branch hand-migration). Result: **0 retrofit, 0 skip, 9 unmatched** — `--apply` a **verified no-op** (`git status --porcelain` empty, `git diff --stat` empty; nothing to land in ree-v3, merge gate vacuous). **All 9 are by-design advisory gaps**, split by failing precondition — **5** fail (b) no unambiguous in-scope `parse_args` anchor: `621`/`621a`/`622`/`626`/`626a` are the early-era `emit_manifest(cells, acceptance, out_dir[, dry_run])` shape where `args = parser.parse_args()` lives in the module-level `if __name__` guard (nested in an `If` → **not** a direct body statement → 0 anchors) while the single `write_flat_manifest` call is inside `emit_manifest()`; injecting `_run_started` at the anchor would be out-of-scope / `NameError` in `emit_manifest()` (same scope-split class as batch-4's 705/706, batch-5's 265/…/430). These 5 DO import `datetime`+`timezone` unaliased (precond (a) passes). **4** fail (a) no unaliased `timezone` import: `626b`/`636`/`637` import `datetime` **only** (no `timezone` — forcing a `timezone` import is out of scope, NOT done) and `354` imports `datetime as dt_mod` **aliased** (so `datetime.now(timezone.utc)` would not resolve). **Verification (why 0 is correct, not a tool miss):** all 9 AST-inspected — the 5 that pass (a) legitimately fail (b) (parse_args at module `if __name__` scope, `direct=False`; wfm in `emit_manifest`), and the 4 that fail (a) genuinely lack an unaliased `datetime`+`timezone` binding; `354` uniquely PASSES (b) (single in-`main` `parse_args` + `wfm` both in `main`) but is refused solely at (a) by its aliased import — so the tool refuses every one exactly per its documented contract. **Genuine-gap sizing:** all 9 lack any internal `time.time()`/`perf_counter` timer, so each is a true (advisory) `elapsed_seconds` gap — unlike batch-4 where 39/145 already carried it. No `pytest`/`validate_experiments`/`validate_recording` diff to report (zero code change). Process: dedicated worktree `.claude/worktrees/ree-v3-elapsed-b6` off `ree-v3` origin/main on `integration/pack-writer-elapsed-retrofit-b6` (`.claude/worktrees/REE_assembly` symlink present for the `test_arm_reuse` indexer-path gotcha); `--apply` run there confirmed clean. **Cumulative retrofit total unchanged: 104** (68 + 35 + 0 + 1 + 0). This, with the 69-rename HYBRID class carrying no newly-routed scripts, exhausts the retrofittable population through batch 6.
   - **Batch-7 pass (0 retrofitted of 12; 2026-07-13, session `pack_writer §7.4 batch-7 elapsed retrofit` [`nice-grothendieck-f7b58b`], NO ree-v3 commit).** Ran the same tool over exactly the **12** scripts routed by the **RUNID_only var-identity** batch (ree-v3 main `31eb700`; `git show 31eb700 --name-only -- 'experiments/v3_*.py'`): `568`/`588c`/`588d`/`588e`/`596`/`615`/`669b`/`670`/`688`/`688a`/`730`/`731`. Result: **0 retrofit, 0 skip, 12 unmatched** — `--apply` a **verified no-op** (`git status --porcelain` empty, `git diff --stat` empty; nothing to land in ree-v3, merge gate vacuous). **All 12 are by-design advisory gaps**, split by failing precondition — **10** fail (a) no unaliased `timezone` import: `568`/`588c`/`588d`/`588e`/`669b`/`670`/`688`/`688a`/`730`/`731` import `datetime` **only** (they timestamp via `datetime.utcnow()`; no `timezone`, so `datetime.now(timezone.utc)` would not resolve — forcing a `timezone` import is out of scope, NOT done). **2** fail (b) no unambiguous in-scope `parse_args` anchor — both DO import `datetime`+`timezone` unaliased (precond (a) passes): `596` is **scope-split** (the single `args = parser.parse_args()` is a direct statement of `main()` [L527] but the lone `write_flat_manifest` call is inside `run_experiment()` [L502] → the tool reports "call not in the parse_args function scope"; injecting `_run_started` after the anchor in `main()` would not be visible at the write in `run_experiment()`), and `615` has **0 direct anchors** (both `parse_args` [L568] and the single `write_flat_manifest` [L578] sit inside the module-level `if __name__` guard [L565-596] → the `parse_args` nested in an `If` is **not** a direct body statement → 0 anchors, and the write is at module scope; a module-global `_run_started` at the guard scope is out of contract — same reasoning as batch-4's 705/706). Same scope-split class as batch-4's 705/706, batch-5's 265/…/430, batch-6's 621-family. **Verification (why 0 is correct, not a tool miss):** all 12 AST-inspected — the 2 that pass (a) legitimately fail (b) exactly per the documented contract (596 cross-function scope-split; 615 anchor nested in the `if __name__` `If`), and the 10 that fail (a) genuinely import `datetime` only with no unaliased `timezone` binding; all 12 `py_compile` clean (byte-unchanged, `--apply` a no-op). **Genuine-gap sizing:** all 12 lack any manifest-written `elapsed_seconds` — `670`'s lone `time.time()` timer feeds only a print (`Completed in ...s`, L424), NOT the manifest dict — so each is a true (advisory) `elapsed_seconds` gap, unlike batch-4 where 39/145 already carried it via an internal timer. No `pytest`/`validate_experiments`/`validate_recording` diff to report (zero code change). Process: dedicated worktree `.claude/worktrees/ree-v3-elapsed-b7` off `ree-v3` origin/main on `integration/pack-writer-elapsed-retrofit-b7` (`.claude/worktrees/REE_assembly` symlink present for the `test_arm_reuse` indexer-path gotcha); `--apply` run there confirmed clean. **Cumulative retrofit total unchanged: 104** (68 + 35 + 0 + 1 + 0 + 0). This exhausts the retrofittable population through the RUNID_only var-identity batch.

---

## 8. Cross-links

- Standard: [`experimental_recording_standard_2026-07-12.md`](experimental_recording_standard_2026-07-12.md) §4.
- Stamper: `ree-v3/experiments/_lib/manifest_core.stamp_recording_core`; soft-validate linter `ree-v3/validate_recording.py`.
- Writer + lint (this session): `ree-v3/experiments/pack_writer.write_flat_manifest`, `ree-v3/validate_experiments.manifest_writer_lint`.
- Converter + scorer: `REE_assembly/evidence/experiments/scripts/sync_v3_results.py`, `build_experiment_indexes.py`.
</content>
</invoke>
