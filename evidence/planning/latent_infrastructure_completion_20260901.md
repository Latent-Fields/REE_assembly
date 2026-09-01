# Latent Infrastructure Completion -- 2026-09-01

**One-session campaign handoff.** Two already-designed infrastructure capabilities
that the autonomous machinery would not have executed, because both live in the
`generation: process` plan lane rather than the active V3 experiment / literature /
substrate dispatch lanes. Detail lives in the owning plan nodes; this is the
cross-cutting summary and the list of things deliberately NOT done.

Owning plans (read these for the full completion notes):
- `derived_evidence_index_plan.md` -- nodes `P1`, `P2`, both now `done`
- `substrate_stability_and_drift_detection_plan.md` -- nodes
  `substrate-commit-coverage` (now `done`) and the new `P1c-central-propagation`

## Commits landed

| Repo | Commit | Contents |
|---|---|---|
| `REE_assembly` | `80ccc2c76a` (on `origin/master`) | Derived evidence index P1 + P2, review-tracker lost-update fix, `runner_status.json` live-state fix, plan nodes, closure regen |
| `ree-v3` | `be7a901ec4` (on `origin/main`) | Prospective provenance: conditional `substrate_commit` enforcement + the observed-REEConfig registry |

`be7a901ec4` was landed with `--no-verify`, on an explicit user decision, and the
reasoning is recorded in its own commit message rather than only here. The
pre-commit contract gate blocked on exactly one test --
`test_no_unregistered_from_dims_drop_site` -- which is the pre-existing trunk red
described in section 4, reproduced failing in a detached worktree at clean `HEAD`
containing none of this code. The gate run was 1 failed / 4422 passed; this tree's
own full-suite run on the hub was 1 failed / 5412 passed, the same single test. The
gate exists to stop a session breaking trunk and is currently red for an unrelated
reason, so it would block every session equally until the chip is worked.

## 1. Derived Evidence Index -- final state

**P1.** `evidence/experiments/scripts/derived_evidence_db.py` emits
`evidence/experiments/.derived/evidence.sqlite` -- gitignored, 3.35 MB, ~1.0 s,
built as an additional writer inside `build_experiment_indexes.py` at the point it
already writes `claim_evidence.v1.json`. `governance.sh` needed **no** change (the
plan expected one line; the emit rides the indexer step that already runs).

**Git-tracked manifests remain the authoritative scientific record.** The DB is
rebuilt from scratch every governance run, is safe to delete at any moment, and no
code treats a row in it as evidence of anything.

*Skew gate.* Refuses on **tracked-but-absent**, not on the plan's literal
`on_disk != in_git` -- that predicate fires on the normal state of a live box
(measured: 10,778 on disk vs 10,777 in git, zero files actually missing). Both
counts and the verdict are recorded in `build_meta`, so the benign direction stays
auditable and a consumer can tell whether the build it is reading was checked. This
is a *second* independent check; the indexer's own `_guard_worktree_materialised`
already runs first.

**P2 -- measured A/B in a real browser against the live server:**

| | before | after | change |
|---|---|---|---|
| Claims Explorer page-load transfer | 25,644,142 B | 7,329,619 B | **-71.4%, 3.50x** |
| claim-loading step (fetch + parse) | 484 ms | 12 ms | **~40x** |
| `/api/claims/summary` payload | (did not exist) | 498,834 B | replaces 18.81 MB |
| `/api/claims/summary` latency | -- | 1.9 s cold / 3 ms warm | mtime-keyed cache |
| derived DB size / build | -- | 3.35 MB / ~1.0 s | inside a 22 s `--index-only` |
| steady-state JS heap | 12.8 MB | 15.2 MB | **no improvement** |

The heap row is stated rather than glossed: the two big files were **transient**,
parsed and discarded, so the win is transfer and parse time, not resident memory.

*The claims.yaml half was not in the plan.* Profiling the actual page found the
explorer also downloads the whole 6.44 MB `claims.yaml` and regex-scans it in the
browser -- by 2026-09-01 the larger of the two costs. `claims.yaml` stays canonical;
the server parses it with real YAML behind an mtime cache.

*That cutover is a correctness fix, and a visible change to the graph.* Measured
against a real YAML parse of the same file, the browser's regex parser:

- yielded **1025** "claims", ~31 of them spurious mid-claim splits;
- **missed 83** genuine registry entries (every `GOV-*`, `SENT-*`, `SOC-HUM-*` and
  every lettered claim -- `MECH-057a`, `SD-032b`, ...);
- set `v3_pending` for **0 of 1025** claims -- an entirely dead filter;
- gave **43** claims the wrong `depends_on`, and 19/29/15 the wrong
  `claim_type`/`subject`/`status`.

After: **1077** claims, **261** `v3_pending`, `ARC-072` with its real 5 dependencies
instead of 1. `explorer.html` keeps the client parser as a fallback so an older
server and the static GitHub Pages export (no API at all) still work.

*Review-tracker lost update -- fixed, but NOT the way the plan proposed.* Plan
section 3 says `INSERT INTO discussed_dirs`. That would move canonical,
non-derivable, git-tracked state into the disposable read-model whose own contract
says deleting it is always safe -- trading a rare lost update for a routine total
loss. `review_tracker.json` stays canonical; `serve.py:update_review_tracker()`
re-reads **inside** a lock (the re-read is the half that actually fixes it) held as
both a `threading.Lock` and a best-effort `flock`, and `save_review_tracker` is now
atomic. The negative control measured the old shape at 24 concurrent writers: it did
not merely lose appends -- **16 of 24 readers got a torn file mid-truncation**,
because the bare `write_text` truncates to zero before refilling.

*Deliberately NOT cut over, measured not assumed.* `generate_pending_review.py` and
`generate_inter_governance_workset.py`. The plan lists both as "two full 10 MB
parses"; Phase 0 already halved that, and the remaining single parse costs **50 ms
and ~50 MB peak** in a one-shot script that runs once per governance cycle. Both
need the full `entries` list and sit inside governance logic where a subtle default
or ordering difference changes what appears in `pending_review`. Revisit only if the
corpus grows enough to change that measurement.

*`runner_status.json`.* The frozen monolith (untracked since 2026-03-22, frozen on
disk since 2026-07-20) is no longer served as **live** state:
`read_merged_runner_status()` returned it verbatim -- `runner_pid` / `idle` /
`current` included -- whenever the per-machine split was absent. History
(`completed`, `queue`) is kept and the withholding is declared in the payload. The
legitimate historical consumers were checked and **left alone**:
`generate_pending_review.py` (completed-run corpus; and its other use feeds a
staleness check that the frozen mtime makes self-correcting) and
`scripts/experiment_error_rate.py`, which documents the file as the only record for
its era.

## 2. Prospective provenance -- final state

Historical manifests were **not** rewritten. Both fixes are prospective, at the most
central chokepoint available.

**`substrate_commit` -- resolved.** First the measurement the plan node was waiting
for: flat-manifest coverage **2026-07: 0/218 -> 2026-08: 207/212 (98%) -> 2026-09:
2/2**. The field was already reaching new manifests, because
`write_flat_manifest -> stamp_recording_core` fills it and **1046 of 1046** driver
files route through that chokepoint. The node's 69%-unassessable figure is a
property of the pre-2026-08 corpus and stays so.

What was genuinely open is that nothing *enforced* it. `substrate_commit` is now
**conditionally mandatory**: a manifest must carry the commit **or** the new
`substrate_commit_unavailable` block (machine-readable reason, checked-at timestamp,
resolved repo root). It is still not in `MANDATORY_CORE_KEYS` -- a git-less checkout
is legitimate (`remote_pytest.sh` rsyncs its staged tree without `.git/` on purpose,
which is why hard-enforcing this broke 10/84 tests when first tried on 2026-08-12).
Measured before landing: of the 22 `experiments/*.py` using `stamp=False`, **21
already stamp upstream and the 22nd is `pack_writer.py` itself -- zero real drivers
break.**

**`enabled_default_off_flags` -- YES, it can be automatic, and now is.** The
question the brief asked. AST census of `ree-v3/experiments`, 2026-09-01: of 1046
driver files calling the chokepoint, **210 (20%)** pass `agent=`, while **1046
(100%)** pass `config=` -- but `config=` is a hand-built dict summary in *every*
case (686 `.get(...)`, 199 `full_config`, 34 dict literals; **zero** pass a real
`REEConfig`), so a `config=` fallback was a dead end.

The chokepoint that works is **REEConfig construction**. `REEConfig.__post_init__`
now registers itself in a process-wide registry, and `stamp_recording_core` reads it
when no `agent=` was passed. **A driver changes nothing.** The two sides share a
`sys` attribute *name* only -- `manifest_core` keeps its stdlib-only guarantee and
never imports `ree_core`, and `ree_core` never imports `manifest_core`.

Verified end-to-end on a **real, unmodified driver**
(`v3_exq_903_mech075_ventral_vta_rpe_probe.py --dry-run`, which passes no `agent=`):
`enabled_default_off_flags_source: process_observed_config`, **7 flags captured**
(including nested ones like `e3.use_habenula_decommit` and
`latent.use_event_classifier`), alongside `substrate_commit`. Also verified on
`goal.use_hierarchical_goal_credit` -- the exact flag the plan's `P1d` node reported
as structurally invisible to its AST analysis, because `GoalConfig` is declared
outside `config.py`. Runtime introspection of the live dataclass tree has no such
blind spot.

**Coverage numbers, honestly framed.** Corpus coverage today is 33 of 968 flat
manifests (~16% of 2026-08). That number describes runs recorded *before* this
change; the mechanism is verified but future coverage can only be *observed* once
new runs land. This is the same "genuinely prospective" framing the `P1c` node used.

**Two carry-through gaps found in the same pass** -- without which the coverage
number is unreadable rather than untrue. `sync_v3_results.build_runpack_docs`' pack
whitelist did not map `enabled_default_off_flags`: measured, **33 flat manifests had
it and 0 of their pack copies did**, so the indexer scored 0 of 1832 runs as having
recorded it. Fixed for future packs, plus a flat-sibling backfill in
`build_experiment_indexes.py` for the existing corpus -- with a **field-aware**
emptiness rule, because the shared `_prov_is_empty` treats `{}` as
nothing-to-backfill (right for `z_goal_stream`, and it would have destroyed the
measured-empty-vs-never-measured distinction here, one layer up from where `P1c`'s
own first draft made the identical mistake). Index coverage for 2026-08: **0 -> 33**.

## 3. What could not be centralised, and why

- **A run whose process never builds a `REEConfig`** (a scalar-only driver) still
  records no `enabled_default_off_flags`. There is nothing to observe. The field is
  correctly *omitted*, never fabricated.
- **Per-arm attribution.** The registry pools configs run-wide with later-wins on a
  key collision -- the same simplification `P1c` documented for the agent path.
  `enabled_default_off_flags` is a run-level field and a multi-arm run builds one
  config per arm.
- **The registry is PROCESS-scoped, not run-scoped**, and the two coincide only
  because a driver process exists to execute one run. In a long-lived
  multi-purpose process they do not: measured on the first full contract-suite
  run, a pytest process had built **2,063** `REEConfig`s for unrelated tests and
  the pooled result was a meaningless union of all of them -- with
  `enabled_default_off_flags_truncated: 1551` correctly declaring it incomplete.
  This is why `enabled_default_off_flags_source` is recorded and why `agent=`
  keeps precedence: a consumer must be able to tell a precise agent-scoped reading
  from a process-scoped one rather than infer precision from the value. Production
  drivers are the coinciding case; the caveat is documented at the source.
- **A >512-config run** truncates; the overflow count is recorded as
  `enabled_default_off_flags_truncated` rather than left silent.
- **The pre-2026-08 corpus** stays retroactively unassessable for `substrate_commit`
  by design. `substrate_stability:P2-governance-surface` remains `open` and its
  2026-08-07 reframing still stands: ship the surface as 84 real candidates plus a
  standing unassessable-pair count.
- **Not touched, mentioned for the record:** with the two big files gone, the
  largest remaining explorer page-load asset is
  `docs/assets/data/claim_dependency_process.v1.json` at **3.40 MB**. It is a
  derived artifact, not canonical, and out of scope here.
- **`/queue-experiment`'s template** no longer needs the "pass `agent=` so the flag
  block gets recorded" step that `P1c`'s status row named as its next action. That
  row has been superseded; the skill itself was not edited (out of scope).

## 4. Found in passing -- one PRE-EXISTING trunk red, not caused here

The first full contract-suite run surfaced
`tests/contracts/test_from_dims_flag_reachability.py::test_no_unregistered_from_dims_drop_site`
failing. It was **confirmed pre-existing** by running that single test in a
detached worktree at clean `HEAD` with no local modifications -- it fails
identically there. Two drivers added by ree-v3 `0fa2959`
(`v3_exq_966_...`, `v3_exq_967_...`) pass `wanting_weight` into
`REEConfig.from_dims()`, which silently drops it; in that test's own words, an arm
that looks ablated may be identical to its control. V3-EXQ-967 has already run
(manifest `..._20260901T062344Z_v3.json`), so whether its evidence is affected is a
governance question, not a lint fix.

Not adjudicated or fixed here -- out of scope. Recorded durably as
`chip-20260901-fromdims-wanting-weight-trunk-red` (task `task_e6742b90`), which
carries the reproduction and both remedies the test names.

Nothing audits this test on a schedule; it was found because an unrelated session
happened to run the full suite.

## 5. Tests

| Suite | Count | Where |
|---|---|---|
| Derived read-model | 17 | `REE_assembly/evidence/experiments/scripts/test_derived_evidence_db.py` |
| Review-tracker concurrency | 7 | `REE_assembly/tests/test_review_tracker_lost_update.py` |
| Prospective provenance | 28 | `ree-v3/tests/contracts/test_prospective_provenance.py` |

Real sqlite, real git repos in tempdirs, real threads; roughly half are negative
controls. Two are worth knowing about specifically: the review-tracker control
*reproduces* the old breakage and fails loudly if the race does not fire on the
machine running it (otherwise the positive tests would be vacuous), and the
provenance suite asserts that a **stock `REEConfig` reports nothing enabled** -- if
that ever fails, every manifest is wrong, which is worse than the gap this closed.
