# pack_writer Single-Writer Migration Plan (chokepoint fix)

**Status:** IN PROGRESS (v0.1). Authored 2026-07-12.
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

Shape families (survey; total 1,028; migrate top-down):

| # | Family | ~count | Distinguishing keys | Migration note | Status |
|---|---|---|---|---|---|
| 1 | A. Legacy status/metrics | 268 | `status`, `metrics`, `summary_markdown`, `fatal_error_count` | shares backbone w/ B+I | pending |
| 2 | B. Criteria / per-claim diagnostic | 273 | `experiment_purpose`, `evidence_direction_per_claim`, `criteria`, `config_summary` | shares backbone | pending |
| 3 | I. Other minimal | 131 | `status`/`outcome`/`metrics` only | shares backbone | pending |
| — | **(A+B+I = 672, ~65% — one "flat metrics + evidence fields" backbone; do first)** | | | | |
| 4 | D. arm_results / per_arm grid | 172 | `arm_results`, `per_arm`, `acceptance` | multi-arm hoist path | pending |
| 5 | F. Recent interpretation+result | 57 | `interpretation`, `non_degenerate`, `env_kwargs`, `result` | the 724/73x lineage | pending |
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

---

## 7. Follow-ups (deferred; sequence after the top-3 families migrate)

1. **Unify the pack skeleton.** Make `sync_v3_results.build_runpack_docs` and `pack_writer.write_pack` delegate to ONE shared skeleton so they cannot drift. Update the golden byte-shape test (`coordinator/test_phase3_runpack_materialize.py`) in the same change.
2. **Carry the always-core through sync into the pack** (`substrate_hash`/`config`/`seeds`/`machine`/`elapsed_seconds` + `non_degenerate`/`arm_results`/`label_balance`), so the indexer can eventually score on always-core inputs. This is the standard §4 "deliberately still open: making these fields load-bearing to confidence scoring" — needs user sign-off (changes promotion math).
3. **Harden the lint to a `validate_queue`/commit gate** once the backlog is mostly cleared (mirrors the arm-fingerprint gate's trajectory).

---

## 8. Cross-links

- Standard: [`experimental_recording_standard_2026-07-12.md`](experimental_recording_standard_2026-07-12.md) §4.
- Stamper: `ree-v3/experiments/_lib/manifest_core.stamp_recording_core`; soft-validate linter `ree-v3/validate_recording.py`.
- Writer + lint (this session): `ree-v3/experiments/pack_writer.write_flat_manifest`, `ree-v3/validate_experiments.manifest_writer_lint`.
- Converter + scorer: `REE_assembly/evidence/experiments/scripts/sync_v3_results.py`, `build_experiment_indexes.py`.
</content>
</invoke>
