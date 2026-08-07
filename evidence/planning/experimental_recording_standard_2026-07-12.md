# Experimental Recording Standard (V3+)

**Status:** PROPOSED (v0.1) — authoring standard, adopt-forward. Landed 2026-07-12.
**Owner doc for:** what every experiment manifest must durably record, regardless of the immediate scientific question.
**Sibling policy:** [`arm_reuse_fingerprint_plan.md`](arm_reuse_fingerprint_plan.md) — the arm-reuse fingerprint is ONE instance of the general principle this doc generalises (see §1).
**Enforced via:** `/queue-experiment` skill Step 3 (authoring) + Step 3.5 (code review). Consumed by `evidence/experiments/scripts/build_experiment_indexes.py`.

---

## 1. Why this exists (the general principle)

REE already runs one form of *prospective epistemic-uncertainty management*: the **arm-reuse fingerprint** mints reusable baseline arms so a later iteration skips re-training a byte-identical baseline (`arm_reuse_fingerprint_plan.md` §7b/§9). That is not a one-off trick — it is one instance of a general rule:

> **Cheaply record now what a future question might need. Storage is far cheaper than recompute, so bias toward GENEROUS over-recording of readouts, from more points, durably.**

The specific gap this standard closes: **experiment manifests record only the readouts relevant to the immediate scientific question.** Later we repeatedly discover that the SAME run could have answered a *different* question had more readouts been durably recorded — and the answer is a re-run instead of a re-read. The arm-reuse fingerprint fixed this for baseline *arms*; this standard extends the same logic to *readouts*.

### The empirical case (why this is real, not hypothetical)

A corpus audit (2026-07-12, 564 flat manifests + 2487 pack manifests, EXQ 028–741) plus the arm-reuse plan's own scan (2026-06-06, 315 manifests) found systemic under-recording of high-reuse readouts:

| Readout | Recorded in | Reuse value |
|---|---|---|
| Raw per-episode returns / trajectories | **0%** | learning curves, variance, early-stopping analysis |
| Substrate commit / code hash | **0%** (flat) / present only in `arm_fp/v1` cells | proving "last week's baseline == this week's" — the reuse prerequisite |
| Latent-representation stats (`eff_rank`, forward-model R2) | **5%**, flat across eras | the substrate thesis is *about* representation quality |
| Exploration / coverage stats | **5%** | any exploration question |
| Full `config` snapshot | **29%** (era-erratic: one era only 2/120) | reproducibility, arm-reuse fingerprinting |
| Explicit seed **list** | **15%** | per-seed re-analysis, reproducibility |
| Timing / wallclock / compute cost | **23% and regressing** (recent era 15/145) | cost accounting, mint prioritisation |
| Per-seed distributions (not just mean±std) | **60%** | recovering individual seed values; 40% still collapse to mean |
| Arm-reuse fingerprint (`arm_fp/v1`) | 28% overall, **77% in recent era** | the counter-trend — the model this standard copies |

### Concrete incidents where recording-debt forced a re-run

- **V3-EXQ-732a** (30x-budget PPO re-run) was avoidable had a **local-view-achievable competence ceiling** been recorded at 724-time. Its absence forced both the confounded 732a re-run AND a *wholly dedicated* run (**V3-EXQ-738**) whose only job was to belatedly record that one denominator (6.05 @D0 → 48.05 @D3). Once recorded, 738's ceiling became the reusable anchor for the entire 734/735/736/737 fan-out — one well-recorded readout retired a confound for four downstream diagnostics. (`failure_autopsy_V3-EXQ-732a_2026-07-10.json`; MEMORY `reference_competence_floor_observability_confound.md`)
- **V3-EXQ-047m** self-stamped `non_degenerate: true` (a false clear) because it recorded only the *probe* partition balance, not the **training-label** class balance (`is_world` ran ~93% positive). The autopsy had to reconstruct the saturation arithmetically. A recorded training-label balance field would have caught the invalidity pre-run and averted the 047m→741 rebuild. (`failure_autopsy_V3-EXQ-047m_2026-07-11.md`)
- **V3-EXQ-643** re-trained, from scratch, a baseline that 604a/569d already computed — because no substrate hash was recorded, the earlier cell could not be *proven* identical and reused. This is the motivating incident for the arm-reuse fingerprint programme itself. (`arm_reuse_fingerprint_plan.md:100-106`)

The recurring shape: **the run that would have answered the later question already happened; it just didn't durably write down the readout.** A false cache-miss on a readout is free; the cost of the omission is a multi-hour re-run.

---

## 2. Design principles (from industry standards)

Distilled from MLflow, Weights & Biases, FAIR, W3C PROV, RO-Crate, Model Cards / Datasheets, and the Allotrope Simple Model (ASM). Attribution in parentheses.

1. **Small mandatory identity+provenance core beneath a large typed optional payload.** Every record carries the same fixed provenance skeleton; the scientific body is family-typed and open-ended. (*ASM: mandatory data-system + device-system documents beneath 65 typed technique schemas; MLflow: auto RunInfo + system tags vs optional params/metrics.*)
2. **Auto-capture provenance; log readouts deliberately.** The "how it was made" (code version, git commit, inputs used, outputs generated, environment, agent) is exactly what the immediate question ignores but reuse depends on — so capture it automatically and always. (*MLflow system tags; W&B auto git+system capture; PROV Entity/Activity/Agent + used/wasGeneratedBy/wasDerivedFrom.*)
3. **Over-record because metadata outlives data and recompute is expensive.** FAIR A2 mandates metadata survive the data itself; reuse (R1) needs more attributes than the originating question used. A `custom_information` catch-all makes over-recording lossless. (*FAIR A2/R1; ASM custom-information-document.*)
4. **Version the record from the inside; evolve additively; validate softly.** A self-declared `schema_version`, additive-only fields, and warn-don't-fail validation keep old records interpretable as the schema grows. Correction is a *new superseding record*, not an edit — matching REE's existing EXQ-letter supersession. (*RO-Crate `conformsTo`; ASM dated schemas + soft validation.*)
5. **Separate raw from derived; make every derived value traceable to its source.** Raw readings and calculated values live in distinct sections; each derived value back-points to the raw ids + the parameters that produced it. (*ASM measurement vs calculated-data with data-source back-pointer; PROV wasDerivedFrom.*)

Sources: MLflow <https://mlflow.org/docs/latest/ml/tracking/>; W&B <https://docs.wandb.ai/guides/track/>, <https://docs.wandb.ai/guides/artifacts/>; FAIR <https://www.go-fair.org/fair-principles/>; PROV <https://www.w3.org/TR/prov-primer/>; RO-Crate <https://www.researchobject.org/ro-crate/>; Model Cards <https://arxiv.org/abs/1810.03993>; Datasheets <https://arxiv.org/abs/1803.09010>; ASM <https://www.allotrope.org/asm> (also the local `bio-research:instrument-data-to-allotrope` skill, read as a worked example).

---

## 3. The standard

### 3a. `recording_schema` version

Every manifest SHOULD carry a top-level string `recording_schema: "rec/v1"`. This is the self-declaring version primitive (principle 4): a future reader/validator keys interpretation off it, and it lets the standard evolve additively without breaking old records. Absent = pre-standard (grandfathered), interpreted best-effort. This does NOT replace `architecture_epoch` (which versions the *substrate*); `recording_schema` versions the *manifest shape*.

### 3b. ALWAYS-record core (every manifest, every experiment_purpose)

Most of these are already conventions; this consolidates them as a mandatory floor. **Bold = currently under-recorded, newly mandatory.**

**Identity & lineage**
- `run_id` (ends `_v3`), `architecture_epoch: "ree_hybrid_guardrails_v1"`, `queue_id`
- `claim_ids` (list actually tested); `experiment_purpose` ∈ {evidence, diagnostic, baseline}
- `supersedes` (if a lettered correction), `recording_schema`
- `timestamp_utc` — ISO-8601 string via `datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")`, never `int(time.time())`

**Provenance (auto-capture — principle 2)**
- **`substrate_hash`** — content hash over the substrate the run executed against (`ree_core/**` + env + `_lib/**`). This is the single highest-value newly-mandatory field: 0% of flat manifests carry it today, and its absence is *the* reason no historical baseline can be safely reused (`arm_reuse_fingerprint_plan.md:128-133`). Reuse it from the arm-fingerprint machinery: `arm_results[i].arm_fingerprint.substrate_hash` already computes exactly this — hoist one copy to the top level. For a single-arm run, compute it via `experiments/_lib/arm_fingerprint.py` helpers.
- **`substrate_commit`** *(added 2026-07-30)* — `{commit, dirty, branch?, dirty_count?, dirty_paths?}`: **which ree-v3 commit** the `substrate_hash` above corresponds to. (`dirty_paths` is capped at 20 with `dirty_count` recording the true total, so a truncated list cannot read as the complete set.) Stamped automatically by `stamp_recording_core`; no driver change needed. **This is the diagnosis half of a detect/diagnose pair, and neither field replaces the other.** `substrate_hash` proves two runs executed different substrate and covers uncommitted edits no SHA can express — but it is opaque, so it cannot say *what* differed. Motivating case: V3-EXQ-614 vs 614a had bit-identical driver bodies, identical seeds and a field-for-field identical `config_summary`, and flipped a verdict FAIL -> PASS purely because `e3_diversity_entropy_lambda` went 0.05 -> 0.5 in ree-v3 `a45ca7f` between the runs; a hash pair says "these differ", a commit pair reduces it to one `git diff` (`recovered_stranded_manifests/RESOLVED_arm2_allon_nonreproducibility_2026-07-30.md`). `dirty` is scoped to exactly the trees `substrate_hash` hashes — an unscoped `git status` would read dirty on nearly every run in these shared multi-session checkouts (one open `experiment_queue.json` edit suffices) and carry no information. It is the one always-core field with an **environmental** dependency: it needs a real git checkout, so it is legitimately absent in the `.git`-less tree `remote_pytest.sh` stages. Absent always beats wrong — the helper fails open rather than recording a SHA resolved against some parent process's repo.
- **`substrate_identity`** *(added 2026-08-07)* — `{source, resolved_at_utc, stamped_at_utc, lag_seconds, drifted_since_resolved, stability_snapshots, hash_on_disk_at_stamp?, commit_source, commit_resolved_at_utc, commit_describes_recorded_hash?}`: **when** the two fields above were captured, not only what they were. Stamped automatically by `stamp_recording_core`; no driver change needed. **A substrate hash is a claim about the past, and until this field existed nothing recorded whether the recording instrument was looking at the past or at the present.** `source: process_snapshot` means the identity was frozen at the first arm cell (or by an explicit `pin_recording_substrate` call) and so *is* the executed substrate; `per_cell_fingerprint_hoist` inherits a cell's; `manifest_write_disk_read` means the stamp was the first look, so the value describes the checkout **as it is at manifest-write time** and coincides with what executed only if nothing moved. Motivating case: **V3-EXQ-866b**, a diagnostic whose entire purpose was certifying that the substrate still reproduced V3-EXQ-603q, recorded a top-level hash (`8e275408`) read **2h26m after** its seed cells, which had themselves pinned `bb755658` — so the one run that most needed to name its own substrate could not (`failure_autopsy_V3-EXQ-866b_2026-08-07.md` §2). Root cause was `manifest_core.compute_single_arm_substrate_hash` calling `compute_substrate_hash` directly, bypassing the 2026-07-20 process-snapshot fix that the per-cell path already used; the two disagreed by construction on any multi-hour run against the shared hub checkout. **Fixed at the value level too** — the single-arm path now resolves through the process snapshot, so every driver that stamps at least one `arm_cell(script_path=Path(__file__))` records the executed hash automatically. Corpus at the time of the fix: 10 of the 249 manifests carrying a `substrate_hash` recorded the write-time read instead of the executed one, with lags up to two days.
  - **A driver that stamps NO arm cell should call `manifest_core.pin_recording_substrate(script_path=Path(__file__))` once at run start** (560 of 915 manifest-writing drivers are in this class). Nothing else can pin the identity for them, and the **commit** half in particular is unrecoverable after the fact: `git rev-parse HEAD` at manifest-write time answers about the tree that *replaced* the executed one. Without the pin such a run still records honestly — `source: manifest_write_disk_read`, and `commit_describes_recorded_hash: false` when the tree moved — but the value is a write-time read.
  - **`stability_snapshots` is how you tell a vacuous `substrate_stable_across_run: true` from an earned one.** A process that froze no identity has nothing to re-check, so its stability verdict is true by default and looks identical on the page to a real one.
- **`machine` / `machine_class`** — where it ran (Mac vs `linux-x86_64-py3.10` cloud); already 56%, make it universal (fingerprint equality is machine-class-bound).
- **`elapsed_seconds`** — wallclock; already 23% and *regressing*. Cheap, and load-bearing for mint-cost accounting and cost-bimodality analysis.

**Outcome & interpretation contract**
- `outcome` ∈ {PASS, FAIL, ERROR} (this exact field name)
- `evidence_direction` (+ `evidence_direction_per_claim` if `len(claim_ids) > 1`)
- `interpretation.preconditions[]` + `interpretation.criteria_non_degenerate{}` (required for diagnostic/baseline — existing gate)
- `non_degenerate` (+ `degeneracy_reason` when false) — existing scoring net

**Reproducibility core (principle 5 prerequisite)**
- **`config`** — the full config snapshot (env params, hyperparameters, schedule). Only 29% today, era-erratic. Without it a run cannot be reproduced OR fingerprinted.
- **`seeds`** — the explicit seed *list* (not a single `seed` int). Only 15% today.

### 3c. GENEROUS optional payload (record by default; bias to over-record — principle 3)

These are the readouts whose omission has repeatedly forced re-runs. **Record them by default unless there is a specific reason not to** — the burden of proof is on *skipping*, exactly as for the arm-mint (`/queue-experiment` "Saving a baseline for reuse"). A false record is free; a false omission is a multi-hour re-run.

Keyed by experiment family:

**All multi-arm / multi-seed experiments**
- `per_seed_*[]` — every seed's full readout, never just mean±std (recover the distribution). 40% still collapse to mean.
- `arm_results[]` — per-arm structured rows, with OFF/baseline internals recorded **as richly as the ON arm** (principle: negative-class symmetry — do not drop OFF-arm latent/coverage internals).
- `arm_fingerprint` per cell (already validator-enforced for multi-arm; `arm_fp/v1`).

**Any experiment that trains or reads a label / classifier**
- **Training-label AND eval-label class balance** — the positive fraction of every binary/categorical label used, for training and eval separately. This is the 047m false-clear fix: the probe-partition guard is not enough; a saturated *training* label invalidates a run silently. Record it as `label_balance: {"<label>": {"train_pos_frac": ..., "eval_pos_frac": ...}}`.

**Any experiment where representation quality could matter (most of them)**
- Latent-representation stats: `zworld_eff_rank`, `e2_forward_r2`, `harm_r2_train/test`, effective rank of any encoder output touched. Only 5% today and NOT trending up despite being central to the substrate thesis. Copy the `v3_exq_740` block.

**Any experiment with exploration / a foraging or navigation env**
- Coverage / visitation-entropy / state-coverage stats (copy `449*/563/569/577`).

**Any diagnostic that gates on an achievable ceiling**
- The **achievable-ceiling denominator computed under the LEARNER's own observability** (not a privileged global oracle). The 732a→738 incident is the canonical cost of omitting this. If a criterion divides by "what's achievable", record the achievable number, its observability regime, and the policy that achieved it.

**Derived-vs-raw discipline (principle 5)**
- Where a manifest reports a calculated value (a ratio, a delta, an aggregate), also record the raw inputs it was computed from, or a back-pointer to them. Do not store only the derived scalar.

**Catch-all (principle 3, makes over-recording safe)**
- `custom_information: {}` — any readout that doesn't map to a standard field goes here verbatim rather than being dropped. Nothing observed should be discarded for lack of a slot.

### 3d. Storage & versioning guidance

- **Additive-only.** New fields are optional additions; never repurpose or remove an existing field's meaning (principle 4). Old manifests stay forward-readable by construction.
- **Correction = supersession, not edit.** A re-run with corrected recording gets a new letter and `supersedes` the prior; the predecessor is marked `evidence_direction: superseded`, not overwritten (existing EXQ-letter policy).
- **Large artifacts by reference.** Checkpoints and bulky arrays: store a content-addressed path/pointer in the manifest, not the blob inline (W&B/MLflow artifact-store pattern). Manifests stay diffable; the git-tracked coordination plane stays lean.
- **Storage is cheap relative to compute.** Run cost is bimodal — most runs are ~23s, a minority run tens of minutes to ~19h (`arm_reuse_fingerprint_plan.md:117-126`). The readouts worth over-recording are concentrated on the expensive runs, where a re-run is exactly what over-recording avoids. Over-record without agonising over per-field storage.

---

## 4. Enforcement surface (where this bites)

The audit found **no single enforcement point today**: only 1 script imports the sanctioned `ree-v3/experiments/pack_writer.py`; 79 scripts define their own `write_manifest`, and 106 write JSON directly with bespoke schemas. And `pack_writer._clean_numeric_metrics` (line ~236) *coerces every metric to a scalar* — it structurally cannot store per-seed lists, `arm_results`, or nested readouts, which is the mechanical reason packs are flat and rich readouts survive only in hand-rolled manifests. So enforcement is **authoring-time discipline via the skill**, backstopped by review, now with a shared mechanical stamper + a relaxed writer + a linter beneath it (below):

1. **`/queue-experiment` Step 3 (authoring)** — a "Record generously" block instructs the author to emit the always-core + the family-keyed optional payload. (Landed 2026-07-12.)
2. **`/queue-experiment` Step 3.5 (code review)** — a checklist group verifies the always-core is present and the family-appropriate optional readouts are recorded before smoke test. (Landed 2026-07-12.)
3. **`failure-autopsy`** — when an autopsy concludes "we couldn't tell because X wasn't recorded", it should cite this standard and route the fix to *recording* X in the re-run, not just re-running. (Reference added; see that skill.)
4. **`view-experiments`** — surfaces which manifests carry the rich readouts vs which are thin (reader-side visibility; optional follow-up).
5. **`experiments/_lib/manifest_core.stamp_recording_core(...)`** — the shared always-core stamper: one no-op-safe call stamps `recording_schema` + `substrate_hash` (multi-arm hoist / single-arm compute via `arm_fingerprint.py`) + `machine`/`machine_class` + `elapsed_seconds` + full `config` + explicit `seeds`. This is the highest-value item (0% of flat manifests carried a substrate hash). (Landed 2026-07-12.)

### Deferred-hardening status (landed 2026-07-12)

- ✅ **Relaxed `pack_writer`** to carry structured `per_seed`/`latent`/`config`/`timing` sections VERBATIM beside the scalar `values` block (`_clean_structured_sections`), so the sanctioned writer no longer drops rich readouts. `values` stays scalar (indexer-safe); the change is backward-compatible (a scalar-only caller is byte-identical). **Still open:** making `pack_writer` the *mandatory single writer* across the ~106 direct-writers (a larger migration).
- ✅ **Widened `build_experiment_indexes.py`** so `substrate_hash` + `label_balance` are surfaced/queryable on index entries (`_FLAT_AUTHORITATIVE_FIELDS`, `RunRecord`, `_scan_runs`, the entry + `unlinked_runs` emitters). Verified inert on the current corpus (a full rebuild is byte-identical modulo `generated_at`). **Deliberately still open:** making these fields *load-bearing* to confidence scoring — that changes promotion math and needs user sign-off.
- ✅ **Added `ree-v3/validate_recording.py`** — soft-validate linter: WARN on a manifest missing the always-core, `--strict` to exit non-zero; forward-compatible (unknown `recording_schema` warns, never fails) per §3d.

---

## 5. Relationship to the epistemic system

This standard is the *input-quality* sibling of the governance epistemic system. Better-recorded readouts mean:
- More runs are reusable (fewer forced re-derivations → the arm-reuse fingerprint gets more cache hits).
- More readouts are available to become *load-bearing* evidence if the indexer's consumed-field set is later widened (§4 deferred).
- The confidence-scoring layer (`build_experiment_indexes.py`) has richer, more auditable inputs.
- **A *later* scientific question can sometimes be answered from data a prior run already recorded — no re-run.** This payoff is realized by the **consumer rule `GOV-REUSE-1`** (registered `governance_rule`, 2026-07-12): before a new experiment is queued, `/queue-experiment` **Step 2.4 (existing-evidence / reanalysis-first check)** asks whether the decisive readout is already recorded on a compatible `substrate_hash` (or derivable post-hoc from recorded raw inputs) and, if so, routes to a **recorded post-hoc reanalysis** citing the source `run_id`s instead of burning compute. Tooling: **`scripts/reanalysis_query.py`** (`query` groups manifests by `substrate_hash` and flags `MATCH`/`INCOMPATIBLE`/`UNVERIFIABLE` for a named readout; `emit` writes the recorded `reanalysis/v1` artifact under `evidence/reanalysis/` and refuses unless the sources share a compatible substrate). (The reanalysis artifact is recorded but not yet wired into `build_experiment_indexes.py` confidence scoring — a deliberate deferred follow-up.) `GOV-REUSE-1` is the forward `mystery (known-data)` router and the reason over-recording here is not waste; `substrate_hash` is the compatibility key that makes a reused readout trustworthy. (`/failure-autopsy`'s recording-gap pathway is the reverse case: a *past* run under-recorded.)

The recording standard *itself* could additionally be registered as a `governance_rule`-type claim (like GOV-DIAG-1 / GOV-FANOUT-1 / the now-registered GOV-REUSE-1) if it proves out — deferred pending adoption evidence. See the sibling analysis [`epistemic_system_formalization_options_2026-07-12.md`](epistemic_system_formalization_options_2026-07-12.md) for how the downstream representation could be formalised.

---

## 6. Changelog

- **2026-07-12** — v0.1 PROPOSED. Authored from a four-thread audit (manifest corpus survey, lineage re-run tracing, industry-standard research, epistemic-system survey). Skill enforcement landed in `/queue-experiment` Steps 3 + 3.5.
