---
closure_plan:
  id: derived_evidence_index
  # generation: process -- infrastructure/tooling lane. Owns no scientific
  # claims, so it is segmented out of the V3 closure % (read_closure counts
  # only generation: v3) and renders on the shared `process` tab alongside
  # arm_reuse_fingerprint and the convergence intake pipeline.
  generation: process
  title: "Derived Evidence Index (queryable read-model over the git evidence tree)"
  registered: 2026-07-18
  last_updated: 2026-07-18
  # Pure infrastructure. It READS the evidence tree and claims rollup; it owns
  # no claim and can promote/demote nothing.
  scope_claims: []
  sibling_plans: []
  nodes:
    - id: "derived_evidence_index:P0"
      title: "Phase 0 -- caching only, no DB. Memoize the uncached claim_evidence.v1.json loads in serve.py on file mtime; eliminate the double full-file parses in generate_pending_review.py and generate_inter_governance_workset.py."
      phase: 0
      status: done
      severity: medium
      owner_exq: null
      last_updated: 2026-07-18
      completion_note: "Landed 2026-07-18. Shared mtime-keyed loader in serve.py replaces two uncached per-request 10 MB parses (/api/brain-map, /api/timeline/events); generate_pending_review.py and generate_inter_governance_workset.py each drop from two full parses per run to one. Behaviour-identical: old-vs-new function equivalence verified on all four batch call sites, and live HTTP responses from an old-code and a new-code server differ ONLY in the per-request generated_at timestamp. BUT the endpoint-level win is ~2%, not the predicted 'most' -- profiling found the real hot spot is claims.yaml, not this file. See P0b and section 2a."
    - id: "derived_evidence_index:P0b"
      title: "Phase 0b -- cache the uncached 3.7 MB claims.yaml yaml.safe_load in serve.py:_tl_load_claims, which profiling shows is 99.5% of /api/brain-map latency and runs TWICE per request."
      phase: 0
      status: pending
      severity: high
      owner_exq: null
      last_updated: 2026-07-18
    - id: "derived_evidence_index:P1"
      title: "Phase 1 -- emit a derived gitignored SQLite read-model from build_experiment_indexes.py at the point it already writes claim_evidence.v1.json, plus the build_meta skew gate that refuses a build when on-disk manifest count diverges from the git-tracked count."
      phase: 1
      status: pending
      severity: high
      owner_exq: null
      last_updated: 2026-07-18
    - id: "derived_evidence_index:P2"
      title: "Phase 2 -- cut over the six identified consumers, incl. a /api/claims/summary endpoint replacing explorer.html's 10 MB per-page-load fetch, and the review-tracker POST read-modify-write lost-update fix."
      phase: 2
      status: pending
      severity: medium
      owner_exq: null
      last_updated: 2026-07-18
      depends_on: ["derived_evidence_index:P1"]
---

# Derived Evidence Index

**Status: Phase 0 done (2026-07-18). Phases 1-2 pending, not started.**

A derived, disposable, gitignored SQLite read-model over the experiment evidence
tree. It is **never a source of truth**: it is rebuilt from git-tracked evidence by
the existing indexer, is safe to delete at any time, and promotes/demotes nothing.

## 1. Why this exists (and why it is not a migration)

The experiments and their results are increasingly *described* as a database. For
the **coordination-data plane** that description is already literally true: Phase 3
(2026-05-28/29) made `coordinator.db` authoritative for the queue and demoted
`ree-v3/experiment_queue.json` to a materialised view. That is why
`PHASE3_QUEUE_CONFLICT_RECOVERY=1` can safely `reset --hard origin/main` and
re-materialise from the DB -- the file is a projection, not the record.

For the **evidence plane** the description is misleading, and should stay that way.
Content-addressed, append-only, tamper-evident history is not incidental to an
experimental record; it *is* the record. A mutable row asserting `outcome=PASS` is
strictly weaker evidence than a signed commit. Evidence manifests stay in git.

What is genuinely missing is neither storage nor transactions but a **read model**.
Today there is no way to ask

> which runs support MECH-457 with `evidence_direction=supports` and
> `exp_conf > 0.6`, excluding superseded?

without loading and scanning a 10 MB JSON blob. This plan builds that query surface
and nothing else.

### Measured baseline (2026-07-18)

| Quantity | Value |
|---|---|
| `REE_assembly` commits | 50,350 |
| `REE_assembly/.git` | 272 MB |
| Commits last 30 days | 720 `phase3-heartbeats:` + 578 `igw-ledger:` + 166 `phase3:` vs ~56 human/doc (~96% machine-written) |
| `claim_evidence.v1.json` | 10.2 MB -- 486 claims, 4,983 entries |
| Flat manifests | 628 |

## 2. The finding that sets the scope

A consumer sweep found **eleven** readers of `claim_evidence.v1.json`. **Nine of
them do keyed lookup into the 486-entry `claims` map and never touch `entries`.**
Only `generate_pending_review.py` scans the 4,983-entry list.

This matters: once loaded, a 486-entry dict is already fast. The DB is therefore
*not* mainly buying faster lookups. It earns its place on four specific things:

1. **Payload.** `explorer.html:8949` downloads and parses the full 10 MB in the
   browser on every page load in order to keep **four fields per claim**.
2. **Integrity.** A `build_meta` row makes HEAD/worktree skew a *build failure*
   instead of a silent evidence-loss commit (see §5).
3. **A correctness bug.** See §3.
4. **Ad-hoc query**, which does not exist today at all.

Everything else is a caching problem, and Phase 0 solves it without a database.
Stating this plainly is deliberate: it is the honest reason this plan is phased
rather than a migration.

## 2a. Correction (measured 2026-07-18, after Phase 0 landed)

**The original claim in this section -- that Phase 0 would capture "the cheap 80%"
of server-side cost -- was wrong, and the measurement that falsified it is worth
recording.**

Phase 0's cache does exactly what it says at the unit level: the
`claim_evidence.v1.json` load drops from 30.8 ms to 0.026 ms (~1,200x). But
`/api/brain-map` takes ~1.8-4.0 s end-to-end, so that saving is **~2% of the
request**, not most of it.

`cProfile` on `read_brain_map()` with the new cache already warm:

```
11,795,594 function calls in 3.967 seconds
  3.946s (99.5%)  yaml.safe_load        <- ncalls = 2
  3.902s          serve.py:5642 _tl_load_claims
```

The dominant cost is **`yaml.safe_load` of the 3.7 MB `docs/claims/claims.yaml`,
uncached, called twice per request**. YAML parsing is roughly two orders of
magnitude slower per byte than JSON, so the 3.7 MB YAML file utterly dwarfs the
10 MB JSON one. `_tl_load_claims` (serve.py:5642) has no cache at all.

Consequences for this plan:

- **P0b** (cache `_tl_load_claims` on mtime, reusing the loader pattern Phase 0
  already built and tested) is now the highest-value remaining item, and it is
  *cheaper* than Phase 1. Do it first.
- **Phases 1-2 are unaffected in their real justification.** They were never
  primarily about server latency -- they rest on the skew gate (§5), the
  lost-update fix (§3), the 10 MB browser payload (§7), and the absent query
  surface. Those all still stand. Only the latency argument moves to P0b.
- Generalisable lesson: the double-parse and the big-file-per-request smells were
  both real, but neither was the bottleneck. **Profile before phasing.** This plan
  was scoped from a consumer sweep (which reads call sites) rather than a profile
  (which reads cost), and that is precisely the error mode a call-site sweep has.

## 3. The correctness bug (Phase 2)

`serve.py:6187` -- `POST /api/review/discuss` performs a full read-modify-write of
the 521 KB `review_tracker.json` to append one string to a list. Two concurrent
review actions produce a **lost update**, silently.

`review_tracker.json` is documented (CLAUDE.md, "Experiment Review Tracking") as
*the sole source of truth* for whether an experiment has been discussed. This is
the one place in the evidence plane where "it's a database" is load-bearing and a
JSON file is actively the wrong tool. `INSERT INTO discussed_dirs` is the fix.

## 4. Schema (Phase 1)

Derived artifact at `evidence/experiments/.derived/evidence.sqlite`, **gitignored**.

```sql
runs(run_id PK, experiment_type, timestamp_utc, outcome,
     machine, architecture_epoch, manifest_path, manifest_sha256,
     scoring_excluded, superseded_by)

entries(rowid, claim_id, run_id FK, source_type, evidence_direction,
        evidence_class, evidence_level, confidence, status,
        experiment_purpose, timestamp_utc, scoring_excluded)
        -- 4,983 rows; indexed on (claim_id), (run_id), (evidence_direction)

claim_rollup(claim_id PK, genuine_exp_count, pass_runs, fail_runs,
             evidence_quadrant, overall_confidence,
             experimental_confidence_decoupled, literature_confidence_parallel,
             entries_total, runs_total, latest_run_id, latest_timestamp_utc,
             exp_posterior_json, lit_posterior_json, direction_counts_json)
             -- 486 rows, flattened from the `claims` map

review(run_id PK, reviewed_at)          -- replaces reviewed_run_ids
discussed_dirs(dir PK, discussed_at)    -- replaces discussed_experiment_dirs

build_meta(generated_at_utc, source_commit, indexer_version,
           n_manifests_on_disk, n_manifests_in_git, n_entries)
```

## 5. The skew gate

`build_meta` is where the integrity invariant lives:

```
n_manifests_on_disk != n_manifests_in_git  ->  BUILD REFUSES
```

This is the confirmed 2026-07-18 SD-068 incident (first index rebuild reported
**1517 runs instead of 1519** after two `git reset origin/master` operations left
8 upstream-added files never materialised on disk) converted from a silent
evidence-loss event into a loud exception. See CLAUDE.md, "HEAD/worktree skew".

The gate is the single strongest justification for Phase 1 and stands independently
of whether the query surface ever gets heavy use.

## 6. Where it hooks (why Phase 1 is cheap)

`build_experiment_indexes.py:2189` already holds the entire structure in memory at
the moment it writes `claim_evidence.v1.json`. The SQLite emit is an **additional
writer at that same point** -- not a refactor of the 6,051-line indexer. Both
artifacts are written; the JSON is unchanged.

`governance.sh` gains one line after Step 2. None of its other ~30 steps change.

## 7. Consumer cutover (Phase 2)

| Consumer | Today | After |
|---|---|---|
| `explorer.html:8949` | fetches 10 MB per page load for 4 fields/claim | `GET /api/claims/summary` -> ~60 KB |
| `serve.py:1811` `/api/brain-map` | uncached 10 MB parse per request | 5-column query |
| `serve.py:5720` `/api/timeline/events` | uncached 10 MB parse per request | `ORDER BY timestamp` query |
| `serve.py:6187` review POST | 521 KB read-modify-write | `INSERT` (fixes §3) |
| `generate_pending_review.py` | two full 10 MB parses | one filtered query |
| `generate_inter_governance_workset.py` | two full 10 MB parses | two single-column selects |

Migration is **opt-in and per-consumer**. `claim_evidence.v1.json` keeps being
written throughout, so every un-migrated reader keeps working and the whole thing
is reversible by deleting the derived file.

## 8. Explicitly out of scope

- **Evidence manifests stay in git.** This reads them; it never becomes their home.
- **No writer changes.** Nothing in the coordinator, `sync_daemon`, or the phase3
  writers is touched. This plan is read-side only.
- **`INDEX.md`** -- has *no programmatic reader at all* (written by the indexer,
  linked from prose). Pure human artifact. Left alone.
- **`pending_review.md`** -- five consumers, all regex-scraping a single integer
  out of a 1.7 KB file. Nothing to win.
- **`arm_fingerprint_index.json`** -- one CLI reader (`arm_reuse_report.py`),
  count-plus-head access. Low priority; not in Phase 2.

## 9. Known open risk

Whether the ad-hoc query surface actually gets used is a **prediction, not a
measurement**. The reasoning for it: claim adjudication and the three recurrence
audits (`check_substrate_ceiling_audit.py`, `check_diagnostic_chain_recurrence.py`,
`check_granularity_debt_recurrence.py`) all hand-roll scans that are natural
`GROUP BY`s. But that is an argument, not evidence. The skew gate (§5) and the
lost-update fix (§3) justify Phases 1-2 on their own; if the query surface goes
unused, those two still stand.

## 10. Incidental findings from the consumer sweep

Logged here so they are not lost; neither is addressed by this plan.

- `scripts/build_hypothesis_space.py:48` defines a `CLAIM_EVIDENCE` path and its
  docstring says it reads the Beta posteriors, but **nothing dereferences it**.
  Stale constant or a lost code path -- worth a look.
- `serve.py`'s `_DIR_RUN_CACHE` (60 s TTL) takes ~2 s to scan ~430 dirs on miss.
  Not on this plan's path, but it is the other uncached hot spot in the same file.
