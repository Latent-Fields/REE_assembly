# Third pack-writer path: traced (2026-08-08)

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml, to any evidence manifest, or to any run pack.** This is an investigation report. No pack was rewritten.

Chip: `chip-20260808-mech138-pack-third-writer-path`. Follow-on from
`chip-20260808-mech138-orphaned-evidence-indexer-stub` (REE_assembly `b0bbc0d662`),
whose background research agent flagged `v3_exq_707c` as "a third, distinct writer
path (not `build_runpack_docs`) also produces mismatched packs -- flagged but not
traced further given scope."

---

## Verdict in one line

**The third writer path is real, but it is not code and it is not multi-arm: it is a
MANUAL governance procedure -- hand-copying a recovered stranded run's flat manifest
into `runs/<run_id>/manifest.json` -- and the indexer already tolerates its output.**
Nothing is orphaned. The residual defect is a missing `metrics.json` sibling on 6 runs,
which degrades gracefully.

This is **not** a second instance of the MECH-137/138/139 orphaned-evidence bug.

---

## What was scanned

All **2759** run packs under `REE_assembly/evidence/experiments/*/runs/*/manifest.json`,
by parsed top-level keys (not grep -- see "Correction" below).

| Category | Count | Share |
|---|---|---|
| Packs total | 2759 | 100% |
| `schema_version == "experiment_pack/v1"` (i.e. `build_runpack_docs` output) | 2748 | 99.6% |
| **NOT `build_runpack_docs` output** | **11** | **0.4%** |
| -- of those, byte-identical verbatim copies of their flat sibling | **6** | |
| -- of those, legacy pre-schema format (differs from flat) | 5 | |
| Packs missing their `metrics.json` sibling (any schema) | 13 | 0.5% |

### Correction to the originating report

The originating agent's grep-based signal over-counted. `grep -l arm_results` on pack
manifests returns **5** files, but 4 of them (`588d`, `588e`, `699b` x2) are correctly
projected `experiment_pack/v1` packs whose match is on a *nested* string inside
`interpretation` / `failure_signatures`, not a top-level key. Only **one** pack
(`v3_exq_707c ... 20260722T041239Z_v3`) actually carries top-level `arm_results`.
Provenance confirms the distinction: those 4 came from `phase3:` writer commits
(`c0242115b0`, `90893ad933`, `a8cad57572`, `c6d8ee76f4`), each staging a full 3-file
pack -- exactly what `sync_daemon._materialize_runpacks` produces via `runpack_for_flat`.

---

## The three writer paths

| # | Path | Mechanism | Output shape |
|---|---|---|---|
| 1 | `sync_v3_results.convert_flat_to_runpack` | run by `governance.sh` | `experiment_pack/v1`, 3 files |
| 2 | `sync_daemon._materialize_runpacks` -> `runpack_for_flat` | Phase-3 hub git writer | `experiment_pack/v1`, 3 files (same function, byte-identical by design) |
| **3** | **Manual stranded-run recovery** | **a governance session copying the flat manifest by hand** | **flat schema verbatim, `manifest.json` only** |

Paths 1 and 2 both funnel through `build_runpack_docs()`, which is documented in
`sync_v3_results.py:151` as "the single source of truth for the run-pack byte shape".
Path 3 bypasses it entirely.

**There is no script implementing path 3.** A search for a stranded-run recovery tool
across `REE_assembly/scripts/` and `evidence/experiments/scripts/` finds none. The
recoveries were performed by hand, which is why the output is a verbatim `cp`.

### The 6 path-3 packs, with their landing commits

All six are **byte-identical** to their flat sibling (verified by parsed-dict equality),
and all six carry `manifest.json` and nothing else:

| Run | Landing commit | Commit subject |
|---|---|---|
| `v3_exq_614_mech341_p3_behavioural_falsifier_3arm_20260529T191318Z_v3` | `39664fc765` (2026-07-30) | govern: ADMIT recovered V3-EXQ-614 as superseded |
| `v3_exq_673_mech171_..._20260611T224744Z_v3` | `1a4ad27d9e` (2026-07-20) | evidence: recover 3 stranded V3-EXQ-673 MECH-171 runs from ree-cloud-2 |
| `v3_exq_673_mech171_..._20260612T005615Z_v3` | `1a4ad27d9e` | (same) |
| `v3_exq_673_mech171_..._20260612T010234Z_v3` | `1a4ad27d9e` | (same) |
| `v3_exq_673_mech171_..._20260612T033246Z_v3` | `eabe9c453b` (2026-07-30) | evidence: correct false arm-degeneracy assertion |
| `v3_exq_707c_arc110_..._20260722T041239Z_v3` | `37f1af866f` (2026-07-30) | govern: ADMIT 2 recovered stranded runs |

**This is a live, recurring path, not a one-off**: three separate incidents inside
eleven days (2026-07-20, 2026-07-30 x2), by two different identities (`nooarche`,
`REE Automation (Mac)`).

The remaining 5 non-projected packs (`241a`, `241b`, `247` x2, `628`) are dated
2026-04-06 to 2026-06-06 and predate the `experiment_pack/v1` schema. They are historical
residue, not an active writer.

---

## Multi-arm is NOT the driver -- the hypothesis is disconfirmed

The originating report inferred that a multi-arm experiment pattern might have its own
pack writer. It does not:

- **448** experiment drivers under `ree-v3/experiments/` use `arm_results`.
- Exactly **1** pack in the whole tree carries top-level `arm_results`.

Multi-arm runs go through `pack_writer.write_flat_manifest` -> flat manifest ->
`build_runpack_docs`, which projects `arm_results` away into the fixed pack shape. That
works correctly at scale. `v3_exq_707c` being multi-arm is **incidental** -- it is in this
set because it was stranded and hand-recovered, not because it is multi-arm.

**There is no systemic multi-arm pack gap.** The 27-pair scan from the prior chip did not
under-count multi-arm packs.

---

## Indexer impact: the alternate schema is already supported

`build_experiment_indexes.py` reads both spellings, so path-3 packs score correctly:

- `build_experiment_indexes.py:1308` -- `status = str(manifest.get("status") or manifest.get("outcome", "UNKNOWN")).upper()`
- `build_experiment_indexes.py:1312` -- `claim_ids_raw = manifest.get("claim_ids_tested") or manifest.get("claim_ids", [])`

`evidence_direction`, `evidence_direction_per_claim`, `evidence_class`,
`experiment_purpose` and `architecture_epoch` are spelled identically in both schemas,
so they carry through unchanged.

**Verified empirically, not just by reading:** all five probed run_ids -- including
`707c`, `614`, `673` and the two legacy ones -- are present in
`evidence/experiments/claim_evidence.v1.json` (3839 run_ids indexed). **No evidence is
orphaned by this path.**

### The one real gap: missing `metrics.json`

`manifest.get("artifacts", {}).get("metrics_path", "metrics.json")` defaults correctly,
but the file does not exist for these 6 runs, so `run.metrics` is `{}`. **13 packs** tree-wide
are in this state (the 6 path-3 ones plus 7 projected packs: `247` x2, `588`, `595` x3, `606`).

Consequences, all of which **degrade gracefully** -- every consumer guards on empty:

| Site | Behaviour with empty metrics | Cost |
|---|---|---|
| `:1476` duplicate fingerprinting | `if not run.metrics: continue` | run cannot be auto-superseded as a duplicate |
| `:1723` stop-criteria evaluation | `if value is None: continue` | no automatic FAIL-hit detection |
| `:2055` index display | metric omitted from key-values line | no metric numbers in `INDEX.md` |

**Claim scoring, evidence direction and conflict ratios are unaffected.** This is a
completeness gap in the derived indexes, not an evidence-loss or mis-scoring event.

---

## Recommendation (NOT executed -- needs a decision)

Deliberately **not** fixed in this chip, per its own instruction to stop rather than build
a large fix. The mechanical fix is easy; the *governance* consequence is not, which is why
it is staged here rather than applied.

**Option A -- document only (lowest risk).** Record path 3 as a known, tolerated alternate
pack schema. Justified by the indexer already handling it and nothing being orphaned.

**Option B -- regenerate the 6 packs through `runpack_for_flat` (narrow, but NOT risk-free).**
All 6 flat siblings exist, so `runpack_for_flat` would produce correct 3-file packs
mechanically. **The hazard is that this is not a no-op on governance state:** adding a
populated `metrics.json` newly exposes those runs to the duplicate-fingerprinting pass at
`:1476` and to stop-criteria evaluation at `:1723`, either of which can flip a run to
`superseded` or add FAIL hits. Two of the six (`673` on `eabe9c453b`, `614` on `39664fc765`)
also carry **hand-curated corrections** -- a false arm-degeneracy assertion was deliberately
corrected, and `614` was deliberately admitted `superseded`. A blind regeneration could
revert curated content. Any execution must diff the resulting index before landing.

**Option C -- close the path (addresses the cause, not the symptom).** The durable defect is
that path 3 exists as an undocumented manual procedure with no tool and no guard. Either:
- add a small `recover_stranded_run.py` that calls `runpack_for_flat`, so the next recovery
  cannot produce a verbatim copy; and/or
- add a detector -- no contract currently pins pack shape anywhere in the evidence tree
  (`grep -rln "experiment_pack/v1"` over `ree-v3/tests/` matches only
  `test_emit_outcome_dry_run_lint.py`, which is unrelated). A check that every
  `runs/*/manifest.json` either carries `schema_version == "experiment_pack/v1"` or is
  explicitly allow-listed as legacy would have caught all 6 the day they landed.

**Recommended: A + C.** Document the tolerated schema, and add the detector so the count
cannot grow silently. Hold B until someone is willing to review the index diff, since its
only benefit is restoring metric display and duplicate detection on 6 already-correctly-scored runs.

---

## Reproduction

```bash
cd /Users/dgolden/REE_Working/REE_assembly/evidence/experiments
/opt/local/bin/python3 - <<'EOF'
import json, pathlib
base = pathlib.Path('.')
for p in sorted(base.glob('*/runs/*/manifest.json')):
    d = json.load(open(p))
    if d.get('schema_version') == 'experiment_pack/v1':
        continue
    flat = base / (p.parent.name + '.json')
    same = flat.exists() and json.load(open(flat)) == d
    print(('VERBATIM-COPY ' if same else 'legacy/differs'), p.parent.name)
EOF
```

Expected today: 6 `VERBATIM-COPY`, 5 `legacy/differs`. **A count above 6 means path 3 has
been used again since 2026-08-08.**
