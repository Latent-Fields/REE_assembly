# Sweep — `--dry-run` smoke manifests carrying governance-grade metadata, and dry-run citations outside the autopsy corpus

- **Generated (UTC):** 2026-07-28T21:42:03Z
- **Session:** `fervent-benz-b5cbaa` (GOV-DRY-1 standing scan)
- **Base commit:** REE_assembly `0416d3ab72`
- **Trigger:** the "Standing lesson" of
  [`dry_run_smoke_in_autopsy_audit_2026-07-28.md`](dry_run_smoke_in_autopsy_audit_2026-07-28.md) — the
  defect was patched per-instance at least four times without the pipeline being fixed. That audit
  checked the 542 `failure_autopsy_*` files against the then-known **23** dry run_ids. `--list-dry`
  now reports **36**. Nothing had checked the rest of the corpus.
- **Scope:** all 2670 manifests on disk (flat + `runs/<run_id>/manifest.json` packs); all
  `evidence/planning/*.md` + `*.json`; `docs/claims/claims.yaml`; `docs/**/*.md`.
- **THIS DOCUMENT APPLIES NOTHING.** Manifest `evidence_direction` edits, `substrate_queue.json`
  and `claims.yaml` writes are governance's. Recomputed values and recommended writes are stated
  for governance to apply, exactly as the 2026-07-28 audit did.

---

## Headline

**All 36 dry run_ids carry at least one governance-grade field — 58 manifest files. But the stamps
are not equivalent, and the distinction is the finding.** 19 of the 36 carry only a *quarantine*
stamp (`superseded` / `non_contributory`), which is the CORRECT response to a smoke and should not
be touched. **17 carry a stamp that ASSERTS something a smoke cannot support.**

| bucket | run_ids | reading |
|---|---|---|
| quarantine-only (`superseded` / `non_contributory`, no category) | **19** | correct; leave alone |
| **directional stamp on a backfill SKELETON pack** | **8** | worst class — a direction with no run behind it |
| **directional stamp on a real dry manifest** | **4** | asserts supports/weakens/mixed from smoke metrics |
| **`epistemic_category: substrate_ceiling` (the audit's known set)** | **5** | family-match stamp, `a6fda79367` |
| total with >=1 asserting stamp | **17** | |

(19 + 17 = 36. A single run_id can hold a quarantine stamp on one file and an asserting stamp on
its sibling — see the flat/pack split below — so the per-file counts overlap; the per-run_id
partition above does not.)

**Scoring is NOT affected, and that is the whole point.** Zero of the 12 directional-stamped dry
run_ids appear anywhere in `evidence/experiments/claim_evidence.v1.json`. The scoring path is gated
at `build_experiment_indexes.py:1174` (`run_id in dry_run_ids or _is_dry_run(manifest)`) as of
`cb7298c1c4`. Every finding below is **scoring-inert and adjudication-live** — it is metadata that
looks exactly like adjudicated evidence to a human or agent reading the manifest, which is
precisely the residual gap the audit named ("the remaining gap is procedural, not mechanical").

---

## Finding 1 — eight backfill SKELETON packs carry a directional verdict with no run behind them

**This is new, and it is the worst-shaped item in the sweep.** Eight dry packs are *synthesised
skeletons*, not records of an execution: `status: "UNKNOWN"`, `timestamp_utc: ""`,
`source_repo.commit: ""`, every environment hash `"unknown"`, `failure_signatures: []`,
`evidence_direction_per_claim: {}` — and a populated `evidence_direction`.

| run_id | `evidence_direction` | `claim_ids_tested` | added by |
|---|---|---|---|
| `v3_exq_207_mech155_general_indexing_probe_1775167615_v3` | `mixed` | MECH-155 | `2231599bab` |
| `v3_exq_208_arc022_hierarchical_pipeline_probe_1775167807_v3` | **`supports`** | ARC-022 | `2231599bab` |
| `v3_exq_209_mech075_bg_hippocampal_gain_probe_1775167993_v3` | **`weakens`** | MECH-075 | `2231599bab` |
| `v3_exq_210_mech156_theta_traversal_probe_1775168257_v3` | `mixed` | MECH-156 | `2231599bab` |
| `v3_exq_211_mech153_arc042_supervised_labeling_1775168828_v3` | **`weakens`** (+ per-claim `MECH-153: weakens`, `ARC-042: weakens`) | MECH-153, ARC-042 | `2231599bab` |
| `v3_exq_212_mech070_e2_motor_model_pair_1775169183_v3` | **`weakens`** | MECH-070 | `2231599bab` |
| `v3_exq_212_mech070_e2_motor_model_pair_1775169288_v3` | **`weakens`** | MECH-070 | `2231599bab` |
| `v3_exq_407_mech231_e2_short_horizon_1776099758_v3` | **`supports`** | MECH-231 | `c3750789f4` |

- `2231599bab` (2026-04-03) *"Governance: review 36 experiments, apply 9 pending decisions"*
- `c3750789f4` (2026-04-13) *"governance-2026-04-13-b: 7 experiments reviewed, SD-013 promoted to provisional"*

Each pack has been touched by exactly two commits and carried its direction **at ADD time** — the
field was not edited later. These are pack-only (no flat sibling on disk for 207-212 / 407), so the
skeleton is the only artifact for that run_id.

**Why it matters.** A reader opening `v3_exq_209_.../manifest.json` sees `evidence_direction:
"weakens"` against MECH-075. There is no timestamp, no commit, no metrics behind it, and the run is
a smoke. `status: "UNKNOWN"` is the only tell, and it is easy to read as "outcome not recorded"
rather than "this pack is a stub". Eight claims are exposed this way: MECH-155, ARC-022, MECH-075,
MECH-156, MECH-153, ARC-042, MECH-070, MECH-231.

**Recommended write (governance):** strip `evidence_direction` (and the `211` per-claim map) on
these eight, or replace with `non_contributory` plus an `evidence_direction_note` naming both facts
— `dry_run=true` **and** skeleton-backfill provenance (`status=UNKNOWN`, no timestamp/commit). The
note matters more than the value here: the next reader needs to know there is no measurement, not
merely that the direction was withdrawn. **No claim confidence changes** — none of these eight
reaches `claim_evidence.v1.json`.

---

## Finding 2 — four real dry manifests assert a direction from smoke metrics

| run_id | file | `evidence_direction` | claims | added by |
|---|---|---|---|---|
| `v3_exq_157_q017_control_axis_minimal_subset_20260329T081401Z_v3` | **flat** | `mixed` | Q-017 | `1a3c70b1a1` (2026-03-29) |
| `v3_exq_161_q024_trajectory_representation_triple_20260329T104847Z_v3` | **flat** | `mixed` | Q-024 | `61a60a0129` (2026-03-29) |
| `v3_exq_365_mech104_surprise_gate_pair_dry_20260413T074306Z_v3` | pack (`status: FAIL`) | `mixed` | MECH-104 | `c3750789f4` (2026-04-13) |
| `v3_exq_570_e2_rollout_collapse_diagnostic_20260515T232232Z_v3` | pack (`status: PASS`) | `unknown` | *(claimless)* | `d1f7663609` (2026-05-16) |

**157 and 161 are ALREADY a documented, deliberately-deferred category — do not re-litigate them.**
Both packs carry `superseded` with a note explicitly naming `dry_run=true`; only the flats still say
`mixed`. That is exactly bucket **(b)** of
[`flat_vs_runs_direction_mismatch_triage_2026_05_31.md`](flat_vs_runs_direction_mismatch_triage_2026_05_31.md)
— *"runs has reclassification the flat lacks — flag only (regenerating flat is out of scope this
pass)"* — where both run_ids are listed by name. The quarantine was applied; it just was not
mirrored back to the flat. Since the indexer reads the pack, this is cosmetic for scoring and only
matters to a reader who opens the flat.

**570 is low-severity:** `unknown` is not an assertion of direction, and the target is claimless.

**Recommended write (governance):** mirror the pack's `superseded` + dry-run note onto the 157/161
flats when the deferred flat-regeneration pass of the 2026-05-31 triage is next picked up — not as
a separate action. For 365, set `non_contributory` with a dry-run note (its `mixed` is a real
directional claim on a 1-seed smoke). Leave 570.

---

## Finding 3 — the `a6fda79367` family sweep stamped the 543f FLATS but not their PACKS

The audit's secondary finding was that five 543f/g/h smokes carry a byte-identical
`evidence_direction: superseded` + `epistemic_category: substrate_ceiling` applied by `a6fda79367`
by family match. Confirmed exactly: 5 files, `543f x3 (flat)`, `543g (flat)`, `543h (flat)`.

**What the audit did not surface: the sweep never reached the 543f packs, and they still assert a
directional verdict on a smoke today.** `git show --name-only a6fda79367` touches the three 543f
*flats* and the 543h/543i *packs* — but no 543f pack. So all three 543f packs still hold, verified
at `0416d3ab72`:

```
evidence_direction: "non_contributory"
evidence_direction_per_claim: {"ARC-062": "weakens", "MECH-309": "non_contributory"}
```

`ARC-062: weakens`, from a `dry_run: true` manifest, in the canonical pack file — the file the
indexer reads and the one an adjudicating session is most likely to open. It is the runner's own
emit-time self-report (present at ADD time in `f7c59f3980`), never corrected.

This is the same shape as the defect the audit diagnosed, one layer down: a family-match sweep with
no `dry_run` filter, incompletely applied. It also means the 543f evidence record is internally
contradictory — flat says `superseded`/ceiling, pack says `weakens` on ARC-062.

**Recommended write (governance):** on the three 543f packs, drop `ARC-062: weakens` (set
`superseded` or `non_contributory`, matching the flats) and add a note naming `dry_run=true` and the
`a6fda79367` incompleteness. ARC-062 is the claim the whole Case-1 chain runs through, so leaving a
`weakens` on it is the highest-value single correction in this sweep. **No confidence change** —
the run does not score.

---

## Finding 4 — dry-run citations outside the manifest layer

### `substrate_queue.json` — one hit, already adjudicated

`/queue[68]/failure_record[3]/run_id` = `v3_exq_543i_..._20260518T063711Z_v3`. This is the confirmed
Case-1 item; the audit already recommended striking it and dropping the
`K>=3 repeated same-machine runs` / `basin selection deterministic w.r.t. init RNG` bar from the
`target` of `[3]` and `[4]`. **No new recommendation — carry the audit's.** Nothing else in the file
cites a dry run.

### `docs/claims/claims.yaml` — clean

**Zero** dry run_ids cited anywhere in the registry.

### `evidence/planning/` — 5 files, no new contamination

| file | dry run_ids cited | verdict |
|---|---|---|
| `failure_autopsy_543i_2026-05-19.{json,md}` | 543i | Case 1, adjudicated |
| `failure_autopsy_V3-EXQ-543i_2026-05-19.json` | 543i | Case 1 (the CORRECT 01:13Z autopsy), adjudicated |
| `failure_autopsy_sd081-spearman-degenerate-dv_2026-07-27.json` | 543f x3, 543g, 543h, 543i | Case 2, adjudicated |
| `flat_vs_runs_direction_mismatch_triage_2026_05_31.md` | 157, 161, 429, 543f x3, 543g, 543h, 570 | **benign — see below** |

`flat_vs_runs_direction_mismatch_triage_2026_05_31.md` reasons about the `evidence_direction`
**stamps**, not about any run's metrics. It is a metadata-consistency scan, so citing a dry run_id
is correct and load-bearing there. No action.

### `docs/**` — 1 hit, benign

`docs/roadmap.md:1054` names the 543i smoke as the lone **pending-review item** in a dated status
log. It cites the run as a queue state, not as evidence. No action.

---

## Recommended writes — consolidated, for governance

| # | target | write | claim impact |
|---|---|---|---|
| 1 | 8 skeleton packs (207, 208, 209, 210, 211, 212 x2, 407) | strip / neutralise `evidence_direction`; note must name **both** `dry_run=true` and skeleton-backfill provenance | none (absent from `claim_evidence.v1.json`) |
| 2 | 3x `543f` **packs** | replace `{"ARC-062": "weakens"}` with `superseded`/`non_contributory`; note the `a6fda79367` incompleteness | none (does not score) — but removes a `weakens` on the Case-1 claim |
| 3 | `v3_exq_365_...` pack | `mixed` -> `non_contributory` + dry-run note | none |
| 4 | 157 / 161 flats | mirror the packs' `superseded` + dry-run note — **fold into the deferred flat-regeneration pass** of the 2026-05-31 triage, not as separate work | none |
| 5 | `substrate_queue.json` `/queue[68]` | as already recommended by the 2026-07-28 audit | per that audit |
| 6 | 19 quarantine-only run_ids, 570, `flat_vs_runs` triage, `docs/roadmap.md` | **no action** | none |

**Nothing here changes any claim's confidence.** The dry-run scoring gate landed before this sweep
and is fully effective; every item above is adjudication-surface metadata.

---

## What is now mechanical

The per-instance patching this sweep documents is exactly what the audit's Standing lesson warned
about. `scripts/check_dry_run_adjudication_leak.py` (**GOV-DRY-1**, governance Step 3i) now sweeps
the confirmed `failure_autopsy_*.json` corpus and `substrate_queue.json` for dry-run citations, and
reports dry manifests carrying `evidence_direction` / `epistemic_category`, every governance cycle.
It is warn-only and never gates a cycle, per the standing GOV-* convention. Everything adjudicated
above is carried in its exclusion set (`_ADJUDICATED_*`) so it does not re-fire forever — following
GOV-GRAN-1's `granularity_debt_disposition` marker pattern. Only genuinely new contamination
surfaces.
