# Stranded/divergent manifest recovery -- ree-cloud-2, 2026-08-09

**Triaged:** 2026-08-09T20:02Z -- 20:07Z, session `process-goal-topology-thoughts-262b36`
(chip `chip-20260809-cloud2-stranded-manifest-recovery`)
**Source:** `ree-cloud-2` (hcloud `ree-worker-2`, 116.203.216.181),
`~/REE_Working/REE_assembly`.
**Probe:** `REE_assembly/scripts/runner_git_health.py --host ree-cloud-2`, run as part of the
2026-08-09 morning digest's fleet git-health sweep.

Sibling exercise to [`README_ree-cloud-2_2026-07-30.md`](README_ree-cloud-2_2026-07-30.md).
Same worker, same failure class (`git pull` retries falling through without a stash pop),
different occasion.

---

## 1. Genuinely stranded run: `v3_exq_899_arc030_mech307_g0_readiness_20260808T153148Z_v3` -- RECOVERED

**Finding:** a completed 5.2h run (`elapsed_seconds = 18790.75`) existed only as an untracked
file in cloud-2's working tree, with **zero** counterpart on origin at any path (flat, pack,
or `.bak` stem) and **zero** rows in the coordinator `results` table for that attempt.

**Why it happened:** `V3-EXQ-899` ran on cloud-2 **twice**. The coordinator `experiments`
table shows exactly one `results` row for `queue_id=V3-EXQ-899`, `received_at
2026-08-08T21:48:34Z` -- matching the **second**, later run
(`..._20260808T214833Z_v3`, already on origin, `non_contributory`). The **first** run
(`..._20260808T153148Z_v3`, started 15:31Z, ~5.2h compute, finished ~20:52Z) never reached
the coordinator spool -- consistent with a `git pull` failure or a spool-write miss on that
attempt, after which the queue entry was evidently re-claimed and re-run rather than retried
from the same attempt. **Do not conclude "already on origin" from an EXQ-number match** --
the two runs have distinct `run_id` timestamps, distinct `elapsed_seconds`, and are genuinely
different executions of the same queue entry.

**Verification before recovery (per [memory] `reference-phantom-completion-crash-before-manifest`
-- absence from origin does not by itself prove a real run):**
- Coordinator DB (`ree-cloud-1:/home/ree/REE_Working/ree-v3/coordinator/coordinator.db`):
  `experiments.status=completed`, exactly 1 `results` row, matching the 21:48Z run only.
- The recovered manifest is structurally complete: 21 top-level keys including a full
  `interpretation` block (2 preconditions with measured/threshold/met, a load-bearing
  criterion, `criteria_non_degenerate`), `arm_results`, `per_seed_results`,
  `per_seed_diagnostics`, `summary_markdown`, `metrics`, `config`. Not a partial write.
- `outcome=FAIL`, `evidence_direction=non_contributory` -- same disposition shape as the
  sibling 21:48Z run already on origin, so no governance re-adjudication is implied by
  admitting it.

**Recovery:** scp'd off cloud-2 before touching anything else on that checkout (verified
byte-identical via `git hash-object` on both sides:
`fa52678a97c65dc12ea380a979ae8d4d97879541`). Landed in three places, mirroring the
`v3_exq_673` / `v3_exq_614` precedent (path 3 of the three pack-writer paths --
see [`../pack_third_writer_path_staged_20260808.md`](../pack_third_writer_path_staged_20260808.md)):

- `evidence/experiments/v3_exq_899_arc030_mech307_g0_readiness_20260808T153148Z_v3.json` (flat)
- `evidence/experiments/v3_exq_899_arc030_mech307_g0_readiness/runs/v3_exq_899_arc030_mech307_g0_readiness_20260808T153148Z_v3/manifest.json`
  (pack, verbatim flat-schema copy, no `metrics.json`/`summary.md` sibling -- same
  degrades-gracefully gap the third-writer-path report documents for the other 6 path-3 packs)
- `evidence/planning/recovered_stranded_manifests/v3_exq_899_arc030_mech307_g0_readiness_20260808T153148Z_v3.json`
  (this recovery's own archive copy)

**No `supersedes` relationship added.** This is not a bug-fix lettered iteration of the
21:48Z run -- both are independent FAIL/`non_contributory` readiness checks of the same
queue entry, and the recovered run is additional evidence, not a correction. **Nothing
marked reviewed** -- that is `/governance`'s call, same as the `v3_exq_673` precedent.

---

## 2. Divergent manifest: `v3_exq_850_..._20260801T005937Z_v3` -- BENIGN, origin authoritative, no action

**Finding:** cloud-2 carries an untracked flat manifest for this run_id that differs in
content from the packed manifest already on origin.

**Diffed both before concluding anything**, per CLAUDE.md remedy (a)/(a2):

- **Schema**: origin is `schema_version: experiment_pack/v1` (the standard
  `build_runpack_docs` pack shape); cloud-2's copy is the pre-pack raw runner dump (no
  `schema_version` key at all).
- **Governance disposition**: origin carries `evidence_direction: superseded` with a
  2026-08-01 governance note explaining `V3-EXQ-850`/`853` was superseded by `V3-EXQ-860`
  (a redesign removing a confound this run carried) -- see
  `failure_autopsy_V3-EXQ-860_2026-08-01` and `failure_autopsy_V3-EXQ-853_2026-08-01`
  Section 6. Cloud-2's copy predates that review: `evidence_direction: inconclusive`, no
  disposition note.
- **The load-bearing content is identical.** The full `interpretation` block (preconditions,
  `measured`/`threshold`/`met` triples, criteria) matches byte-for-byte between the two
  copies -- verified by structural diff, not just eyeballing. Sampled measured values
  (`0.495663999904952`, `0.0013405698274115208`, `3.945531861515511e-05`, ...) are identical
  on both sides.
- **Keys present only in the cloud-2 copy** (`config`, `arm_results`, `aggregates`,
  `per_seed_cells`, `reference_values`, `thresholds`, `elapsed_seconds`, `seeds`, `notes`,
  `degeneracy_reason`, `non_degenerate`, `dose_levels_separable`, `per_arm_gate`) look at
  first glance like real data origin is missing. **Confirmed this is NOT a loss**: the
  `experiment_pack/v1` schema deliberately does not carry these fields in `manifest.json` --
  checked a known-good, non-recovered sibling pack
  (`v3_exq_794a_..._20260724T063301Z_v3/manifest.json`, the fanout source this run cites) and
  it has the identical reduced key set. The pack's curated numeric summary lives in
  `metrics.json`'s `values` block instead (`arm_overconfidence_score`,
  `arm_calibration_ratio`, `per_level`, `readiness_ok`, etc.), which was also pulled and
  checked against the raw copy's own per-arm numbers -- consistent.
- **Keys present only in origin** (`schema_version`, `source_repo`, `runner`, `artifacts`,
  `stop_criteria_version`, `environment`, `failure_signatures`, `evidence_class`,
  `producer_capabilities`, `status`) are the standard pack-schema metadata fields the raw
  runner dump never had.

**Verdict:** origin is the reviewed, schema-compliant, governance-annotated authoritative
copy; cloud-2's untracked file is pre-review runner residue that the packing step already
correctly superseded. Same shape as the CONTENT-DIFFERS-benign class in
[`README_ree-cloud-2_2026-07-30.md`](README_ree-cloud-2_2026-07-30.md) -- origin holds
strictly more (or equally informative, schema-projected) content. **Nothing landed for this
one.** The untracked cloud-2 copy was deliberately **left in place, not deleted** --
"never drop on a judgement call" per CLAUDE.md remedy (a); it is non-evidence residue, not a
loss risk, so there is no urgency to clear it, and `runner_git_health.py` will keep
reporting it as a same-run_id-different-content finding on future probes until someone
does. That is expected and low-cost noise, not a regression.

---

## 3. HEAD/worktree skew repair (4 paths, all deletion-shape)

`runner_git_health.py` additionally reported 4 HEAD/worktree skew paths on cloud-2, all
under the already-landed `v3_exq_876_mech025_doing_mode_causal_signal` run
(`20260802T214005Z`): the flat manifest plus the 3-file `runs/` pack (manifest, metrics,
summary), all showing as `D `/` D` (files in HEAD, never written to cloud-2's disk --
adoption-lag skew per CLAUDE.md, not a real deletion). All 4 are `D `-shape (unconditionally
safe to materialise, per the same section) -- confirmed by checking their content against
`origin/master` before restoring:

```
git -C ~/REE_Working/REE_assembly diff --name-only --diff-filter=D -z HEAD -- :/ \
  | xargs -0 git checkout HEAD --
```

Re-ran `runner_git_health.py --host ree-cloud-2` after repair: `ree-cloud-2 (worker)
REE_assembly OK`.

---

## Related

- [`README_ree-cloud-2_2026-07-30.md`](README_ree-cloud-2_2026-07-30.md) -- same worker, prior
  occasion, same underlying `git pull` retry-without-restore defect
- [`../pack_third_writer_path_staged_20260808.md`](../pack_third_writer_path_staged_20260808.md)
  -- the manual-recovery pack-writer path this landing follows (path 3 of 3)
- `REE_assembly/scripts/runner_git_health.py` -- the active probe that surfaced both findings
