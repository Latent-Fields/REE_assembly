# Arm-Reuse Fingerprint -- Design Plan

**Status:** DESIGN / proposal. No code landed. Awaiting user decision on scope (see "Open Decisions").
**Created:** 2026-06-06T14:56Z
**Author session:** arm-reuse-fingerprint-design-20260606T1456Z
**Motivation chip:** user observation 2026-06-06 -- "some testing is repetitive with possible bit-identical arms for parts of the repeat experiments; could data be recorded so certain arms would not need re-running?"

---

## 1. Problem statement

V3 experiments are run as a grid of **(seed x arm)** cells. Each cell trains a
fresh agent from scratch and evaluates it. One arm is almost always an
**OFF / baseline / control** condition whose *only* purpose is to be the matched
reference for the treatment arm(s).

These baseline arms are frequently **deliberate replications** of a baseline that
a *previous* experiment already computed. The canonical example:

- `v3_exq_643_modulatory_authority_validation.py:144` -- `ARM_A` labelled
  `"authority_off_baseline_604a_replication"`.
- `:179` -- comment: `# ENV identical to V3-EXQ-604a / 569d so manifest-comparability holds`,
  same `SEEDS = [42, 43, 44]`, same `P0=60 / P1=20` schedule.

So EXQ-643 re-trains, from scratch, a baseline that 604a/569d already trained.
That is the redundancy the user noticed.

### Empirical scale (manifest corpus scan, 2026-06-06)

315 manifests under `evidence/experiments/`:

| Metric | Value |
|--------|-------|
| Manifests recording a **substrate commit / code hash** | **0** |
| Manifests with structured `arm_results[arm_id]` | 7 (100 arm rows) |
| Arm rows that are baseline/off/control | **41%** (`ARM_0_OFF` recurs 11x) |
| Manifests recording `elapsed_seconds` | 94 |
| Run elapsed: median / mean / max | 23s / **4084s (~68 min)** / **67270s (~18.7h)** |
| Total recorded compute | ~107 h across 94 timed runs |

**Two facts drive the whole design:**

1. **Cost is bimodal.** Most runs are cheap (diagnostics, dry runs ~23s). A
   minority are very expensive (tens of minutes to ~19h). Re-running a baseline
   arm only matters on the expensive multi-arm runs -- but that is exactly where
   the replication pattern recurs. The win is concentrated, not diffuse.

2. **No substrate version is recorded anywhere.** You cannot today prove that a
   baseline computed last week is the same computation as the baseline an
   experiment needs this week, because `ree_core` / `_harness.py` / the env may
   have changed in between. **This is the foundational gap. Until it is closed,
   no reuse is safe, and reuse can only ever be forward-looking** (historical
   manifests cannot be retro-fitted into a cache).

---

## 2. The validity model (the part that must not be wrong)

Reuse is only sound if a cached arm result is **the same random variable** the
new experiment would have drawn. The asymmetry that governs every decision below:

> **A false cache-HIT corrupts a scientific conclusion. A false cache-MISS only
> wastes compute.** The costs are wildly asymmetric, so the system must be
> **conservative: refuse to reuse whenever there is any doubt.**

### 2.1 When is reusing arm X from run R inside new experiment E valid?

A matched-control arm derives its scientific value from sharing the seed and
substrate with the treatment arm, isolating the single varied factor. A *cached*
baseline preserves that value **iff the cached cell is bit-for-bit (or, under the
weaker determinism regime, distribution-for-distribution) the cell E would
itself have produced.** That holds only when ALL of the following match between
R and E:

1. **Substrate content** -- the actual source the cell executes: `ree_core/**`,
   the environment module, `experiments/_harness.py`, `experiments/_lib/**`, and
   the arm's own script logic for the OFF path. (Content hash, not git commit --
   see 3.2; this workflow runs dirty trees constantly.)
2. **Arm config slice** -- every parameter the OFF computation reads:
   `env_kwargs`, training schedule (`p0`, `p1`, `steps_per_episode`), and every
   hyperparameter on the OFF code path (optimiser LRs, buffer sizes, weights,
   the arm's own flags). NOT parameters that only the ON arm reads.
3. **Seed.**
4. **Machine class** -- because determinism is not guaranteed across CPU/GPU
   architectures (see 2.3). Same `machine_class`, not necessarily same host.
5. **Cell independence** -- the cell must be a *pure function* of
   (substrate, config-slice, seed): no dependence on iteration order or any
   global mutable state carried in from earlier cells.

### 2.2 The cell-independence hazard (concrete, found in 643)

The 643 driver is `for arm in ARMS: for seed in seeds: _run_seed_arm(...)`
(`:767`). `_run_seed_arm` re-seeds `torch` and `numpy` on entry (`:371-372`) and
builds a fresh env + agent -- good. **But ARM_A always runs first.** If any RNG
is *not* reset per cell, ARM_A's result depends on it being "first", and a cached
ARM_A from another experiment (where the global RNG had consumed a different
amount before ARM_A) is a different draw. Known un-reset sources:

- Python's global `random` module (cells should use `random.Random(seed)`
  instances only -- 643 does at `:384`, but this is not enforced).
- The harness fallback `_action_random = random.Random()` -- **module-level,
  unseeded** (`experiments/_harness.py:70`, used at `:140` when `seed is None`).

**Mitigation = a precondition AND a hardening fix:** a reusable cell must perform
a *complete* RNG reset at entry -- `torch.manual_seed`, `torch.cuda.manual_seed_all`,
`np.random.seed`, `random.seed`, and a seeded harness RNG -- so the cell is
order-independent. Cells that cannot guarantee this are **ineligible** for reuse
(fingerprint marks them `reuse_eligible: false`).

### 2.3 Determinism regimes

There is no `torch.use_deterministic_algorithms()`, no cuDNN determinism pin
anywhere in `experiments/` or `ree_core/`. So today, "same seed" gives
*approximately* the same trajectory on the *same* machine and *diverging*
trajectories across machines (float rounding compounds over ~10^4 steps).

Two possible regimes; the design supports both and the fingerprint records which:

- **Regime A -- distributional reuse (default, low cost).** Accept that a cached
  cell is a valid *representative draw* for (substrate, config-slice, seed) on the
  same `machine_class`. Sound for matched-control purposes because the OFF arm is
  itself only ever a seed-matched reference, not a bit-exact oracle. Requires the
  machine-class guard and the independence precondition.
- **Regime B -- bit-exact reuse (opt-in, higher cost).** Add
  `torch.use_deterministic_algorithms(True)` + cuDNN pins + full RNG reset, and a
  post-hoc replay check can confirm bit-identity. Enables cross-`machine_class`
  reuse. Slower; some ops unsupported. Only worth it if cross-machine baseline
  sharing becomes a real need.

**Recommendation: ship Regime A.** It captures the concentrated win with a much
smaller validity surface. Reserve B for a specific demonstrated need.

---

## 3. The fingerprint

### 3.1 Where it is computed

**In the experiment script, per cell, at run time** -- NOT reconstructed from
manifests. Manifest arm schemas are heterogeneous (`arm_results`,
`per_seed_results`, `config.arms[]`), so reconstruction is unreliable. The script
has the canonical, resolved config in hand; it emits the fingerprint into the
manifest. This is a shared helper (`experiments/_lib/arm_fingerprint.py`), called
once per cell.

### 3.2 What it hashes

```
arm_fingerprint = sha256( canonical_json({
    "schema": "arm_fp/v1",
    "substrate_hash": <content hash, see below>,
    "config_slice": <OFF-path-relevant config, canonicalised>,
    "seed": <int>,
    "regime": "A" | "B",
}) )
```

- **substrate_hash** -- sha256 over the *content* of the source files the cell
  depends on (`ree_core/**/*.py`, the env module, `_harness.py`, `_lib/**`,
  plus the cell's own OFF-path source). Content hash, not `git rev-parse`,
  because **the workflow routinely runs with a dirty working tree** (heartbeat
  autostash, in-flight edits) -- a commit SHA would falsely match across
  uncommitted changes. Record the git SHA + `dirty` flag *alongside* for human
  triage, but the *content hash is authoritative*.
- **config_slice** -- explicitly enumerated by the script author as the set of
  params the OFF path reads. Default to the WHOLE config if the author does not
  narrow it (conservative: over-inclusion only causes false misses). A separate
  `config_slice_declared: bool` records whether narrowing was deliberate.
- The fingerprint is emitted per cell into `arm_results[i].arm_fingerprint`
  (and a top-level `substrate_hash`), plus `reuse_eligible: bool` and
  `reuse_eligible_reason` (e.g. `"ok"`, `"incomplete_rng_reset"`,
  `"shared_optimizer_across_arms"`).

### 3.3 Refuse-by-default rules (the cache may NOT serve a hit when)

- `substrate_hash` differs (any source change).
- `config_slice` differs.
- `machine_class` differs (Regime A).
- `reuse_eligible: false` on either the cached cell or the requesting cell.
- The cached cell's manifest is missing any fingerprint field (older schema).
- The cached run's `outcome` was `ERROR`, or the cell carried an `error_note`.
- Schema version mismatch (`arm_fp/v1` vs future).

When in doubt: re-run.

---

## 4. Phased rollout (shadow-first, per feedback_infra_shadow_first)

Mirrors the coordinator cutover discipline: prove the mechanism under real load
**before** any experiment's validity depends on it.

### Phase 0 -- INSTRUMENT ONLY (no reuse, zero validity risk)
- Add `_lib/arm_fingerprint.py`; record `substrate_hash` + per-cell
  `arm_fingerprint` + `reuse_eligible` into manifests of new experiments.
- Add complete per-cell RNG reset to the script template + `/queue-experiment`
  smoke checklist.
- Build a read-only report: scan manifests, group by `arm_fingerprint`, show
  **would-be cache hits** and the compute they *would* have saved.
- **Exit criterion:** N weeks of data showing (a) measurable would-be savings on
  expensive runs, and (b) **zero false-collision incidents** -- i.e. cells with
  equal fingerprints that, when both actually ran, produced
  out-of-tolerance-different results. This is the proof the fingerprint is sound.

### Phase 1 -- OPT-IN CITE-BASELINE (manual, auditable)
- An experiment that wants to skip its baseline arm declares
  `reuse_baseline_from: <run_id>` in its queue entry. The script, at the cell it
  would have run, recomputes the fingerprint, looks up the cited run, and
  **only** reuses if the fingerprint matches under the refuse-by-default rules;
  otherwise it runs the arm and logs `reuse_refused: <reason>`.
- The reused cell is copied into the new manifest with provenance
  (`reused_from_run_id`, `reused_fingerprint`) so the manifest is self-describing
  and governance can see exactly what was and wasn't freshly computed.
- Human picks the reference -- low blast radius, fully auditable.

### Phase 2 -- AUTO-CACHE (only if Phase 1 proves out)
- A fingerprint -> cell-result index (the coordinator DB is the natural home; it
  already holds per-run rows). Runner checks the index before training a cell.
- Still bound by every refuse-by-default rule.

**We stop at whatever phase delivers the value.** Phase 0 alone may show the
redundancy is small enough in practice that 1-2 are not worth the validity
surface; Phase 1 may be the sweet spot.

---

## 5. Governance / provenance guarantees

A reused manifest must be **indistinguishable in rigor** from a freshly-run one:

- Every reused cell carries `reused_from_run_id` + `reused_fingerprint`.
- The indexer / governance must treat a reused baseline exactly as it treats the
  original (no double-counting toward claim confidence; the reuse is a pointer,
  not new independent evidence).
- If the cited source run is later superseded / invalidated, downstream reusing
  runs must be flagged (`pending_reuse_revalidation`) -- analogous to
  `pending_substrate_reconfirmation`. This needs a back-reference index.
- A reused result NEVER changes how an experiment's `outcome` is computed -- the
  acceptance criteria run over the (possibly reused) cells identically.

---

## 6. Explicitly OUT of scope

- Retro-fitting historical manifests into a cache (no substrate hash exists; unsafe).
- Caching *partial* training (checkpoint/warm-start reuse) -- different, harder
  problem; this plan is whole-cell reuse only.
- Cross-`machine_class` reuse (needs Regime B).
- Any change to acceptance-criteria logic or the queue/coordinator claim path.

---

## 7. Decisions (RESOLVED 2026-06-06 by user)

1. **Determinism regime: Regime A** (distributional reuse, same machine-class).
   No torch determinism flags. Cross-machine reuse deferred to a future Regime-B
   opt-in only if a concrete need appears.
2. **Stopping phase: Phase 0 only authorised.** Build instrument + measure
   (fingerprint emission + would-be-savings report); decide Phase 1/2 after
   seeing real redundancy data. No reuse executed until Phase 0 data is reviewed.
3. **Config-slice: whole-config default**, opt-in narrowing. Authors are not
   required to declare the OFF-path slice; the whole resolved config is hashed
   unless an author deliberately narrows it (narrowing only raises hit rate).
4. **Cache index location (Phase 2 only): DEFERRED** -- decide if/when Phase 2 is
   authorised. Candidates unchanged: coordinator DB vs committed `evidence/` index.

---

## 7b. Baseline pre-minting (added 2026-06-06, user-directed)

**Idea (user):** while 643a / 610f run and further iterations (643b, 610g) are
likely, use idle cloud workers (cloud-2/3) to pre-compute the OFF/baseline arms
now so they are recorded and ready for reuse. "They may not be needed but we lose
nothing by minting them on free machines."

**Safety:** sound. The fingerprint gates reuse, so a stale pre-mint is *refused*
and the arm re-runs normally -- a pre-mint can never corrupt a result. Cost on
idle machines is acceptable. The only open question is hit-rate.

### Three constraints found while scoping

1. **Machine-class (Regime A reuses within one class only).**
   - **610 = cloud lineage** (610b/c/d ran on cloud-2, 610e/f on cloud-1, all
     `linux-x86_64`). Minting on cloud-2/3 is the correct class -> 610g (cloud)
     can reuse. Clean fit.
   - **643 = Mac lineage** (643a on DLAPTOP-4, `darwin-arm64`). A cloud mint is a
     different class and would be refused for a Mac 643b. **User decision: run
     643b on cloud** so a cloud-minted 643 baseline is reusable (and frees the Mac).

2. **Whole-config hashing is too brittle for cross-iteration reuse.** A
   letter-iteration almost always changes *something* in the config dict (proof:
   643->643a changed only the ARM_A label string -- which whole-config would
   treat as a mismatch and refuse). So whole-config (decision 3 default) would
   make minting almost never hit. **This is exactly the opt-in-narrowing case
   decision 3 anticipated, not a reversal of it.** The OFF baseline depends only
   on: `env_kwargs` + schedule (`p0`/`p1`/`steps`) + the substrate-operating
   config the OFF arm actually executes (in 643: SD-056 contrastive + curiosity,
   which fire for ALL arms) + the OFF arm's own flags. NOT ON-arm gains,
   acceptance thresholds, or labels.

3. **Substrate drift.** The mint is reused only while `ree_core` + the OFF path
   are unchanged when the next iteration runs. 610 has churned 7x; the
   fingerprint refuses a stale mint automatically (safe), so drift only costs
   (free) wasted compute, never correctness.

### Design: canonical-baseline-module (robust narrowing)

The risk of narrowing is *under-declaration* -> false hit -> corrupted science.
Avoid hand-listed slices: extract each lineage's OFF baseline into a single
**canonical baseline module** that 643a/643b/643c (and 610x) all construct their
OFF arm from. The "slice" identity then = the **content hash of that shared
module + the env/schedule it pins**, computed by `compute_substrate_hash` over
the module path. Any change to the baseline correctly refuses; nothing else can
silently drift it. This is the safest form of opt-in narrowing.

### Plan

1. Wire fingerprint emission into the experiment authoring path
   (`/queue-experiment` skill + per-arm `compute_arm_fingerprint` call) so every
   multi-arm run captures its OFF baseline for free, fingerprinted.
2. Define `experiments/_lib/baselines/` canonical modules for the 643 and 610
   OFF baselines (env + schedule + substrate-operating config + OFF flags).
3. Create baseline-only **mint** experiment scripts (OFF arm x SEEDS only) via
   `/queue-experiment`, `machine_affinity` pinned to a cloud worker, **low
   priority** (so real science preempts), emitting fingerprints with the
   canonical-baseline slice declared.
4. Mint the 610 baseline on cloud-2 **and** cloud-3 simultaneously: if the two
   results agree within tolerance, that confirms the cross-instance determinism
   assumption Regime A rests on (this is Phase 0's "zero false-collision" exit
   criterion, obtained for free).
5. Consuming the mint (643b/610g actually skipping the arm) is the **Phase 1
   consumer** + refuse-gate -- still to be built. Minting now only *records*
   (Phase-0-compatible); a minted baseline is at minimum an extra baseline run,
   never wasted.

### Status -- 610 OFF baseline minted (2026-06-06)

- **Canonical module landed:** `ree-v3/experiments/_lib/baselines/exq610_inv074_crystallization_baseline.py`
  -- a faithful extraction of `v3_exq_610f` **ARM_0_stripped_control** (the OFF
  baseline: `crystallize=False`, phase-3 entropy floor `0.0`, MECH-313/341/260
  floors OFF, structured curiosity decoupled). Exposes `build_off_arm(seed)`,
  `train_off_arm(...)`, `off_path_config_slice()`. It is auto-bound into the
  fingerprint `substrate_hash` via the `experiments/_lib/**/*.py` glob, so any
  drift refuses a stale reuse.
- **Mint script landed:** `ree-v3/experiments/v3_exq_610_inv074_crystallization_baseline_mint.py`
  (`experiment_purpose="baseline"`, `claim_ids=[]`). Per cell: `reset_all_rng(seed)`
  -> build/train OFF arm -> `compute_arm_fingerprint(config_slice=off_path_config_slice(),
  rng_fully_reset=True, config_slice_declared=True)`. Phase-0 emit-only.
- **Queued twice (low priority 10):** `V3-EXQ-644` -> `ree-cloud-2`,
  `V3-EXQ-645` -> `ree-cloud-3` (same script/config; the cross-instance
  determinism check). Runner not started; cloud-2/3 idle.
- **Cross-instance determinism result: PENDING both runs.** After `V3-EXQ-644`
  and `V3-EXQ-645` complete, compare the two manifests' OFF metrics
  (`arm_results[*].end_phase_2_entropy`, `end_phase_3_entropy`, `mean_reward`)
  within tolerance. Agreement confirms separate CX22 instances are mutually
  deterministic on CPU torch (the Regime-A assumption; Phase-0 zero-false-collision
  exit). The `arm_fingerprint` hash is identical across the two **by construction**
  (coarse `machine_class = linux-x86_64-pyX.Y`); the check is on the *metrics*.
  _Record the numeric comparison + verdict here once both manifests land._

### Status -- 643 OFF baseline minted (2026-06-06)

- **Canonical module landed:** `ree-v3/experiments/_lib/baselines/exq643_modulatory_authority_baseline.py`
  -- a faithful extraction of `v3_exq_643a` **ARM_A `authority_off_baseline`**
  (`use_modulatory_selection_authority=False`, gate inert; the rest of the
  substrate-operating config -- SD-056 online contrastive + MECH-314 curiosity
  ALL_ON + MECH-341 entropy bonus + ARC-065 SP-CEM + V_s -- fires for ALL arms).
  Exposes `make_off_env(seed)`, `make_off_agent(env)`, `run_off_cell(seed, ...)`,
  `off_path_config_slice()`. **It is the content-hashed contract a future 643b/643c
  must build its OFF arm from** (auto-bound into `substrate_hash` via the
  `experiments/_lib/**/*.py` glob, so any drift refuses a stale reuse).
- **Byte-for-byte fidelity to 643a ARM_A verified** (the under-declaration failure
  mode the design warns about): `ENV_KWARGS` identical, *resolved* `REEConfig`
  identical (full `from_dims` dict, OFF flags included), run-loop + SD-056 helpers
  identical. The one intended change -- `run_off_cell` does the complete
  `reset_all_rng(seed)` at cell entry vs 643a's `torch.manual_seed`+`np.random.seed`
  -- is a *strict superset*: the OFF loop draws only from torch / numpy / a local
  `random.Random(seed)`, never python-global `random` or the harness
  `_action_random`, so the extra resets touch unused RNGs and leave the OFF draw
  unchanged while making the cell order-independent (`reuse_eligible`). A reusing
  643b must likewise `reset_all_rng` at cell entry (now required by the
  `/queue-experiment` skill for all multi-arm experiments).
- **Mint script landed:** `ree-v3/experiments/v3_exq_646_mint_modulatory_authority_off_baseline.py`
  (`experiment_purpose="baseline"`, `claim_ids=[]`). Per cell: `run_off_cell` (which
  `reset_all_rng`s at entry) -> `compute_arm_fingerprint(config_slice=off_path_config_slice(),
  rng_fully_reset=True, config_slice_declared=True)`. Phase-0 emit-only. `--dry-run`
  PASS, `reuse_eligible=True`; `validate_experiments` + `validate_queue` clean.
- **Queued (low priority 10):** `V3-EXQ-646` -> `ree-cloud-2`. **643 moved to the
  cloud machine-class** (constraint 1 above; 643a ran on `DLAPTOP-4`/`darwin-arm64`,
  which a cloud 643b could never reuse). Confirmed `present` in the coordinator DB.
  Runner not started; cloud-2 idle. (Single-instance: the cross-instance determinism
  check is being established by the 610 cloud-2/cloud-3 pair; 643's OFF baseline rides
  on that Regime-A confirmation rather than re-running the same check.)
- **Consumption (643b actually skipping the OFF arm) is the Phase 1 consumer + refuse
  gate (section 9), gated on the determinism check passing.** This mint only *records*.

## 8. First concrete deliverable if approved

Phase 0, smallest useful unit:
1. `experiments/_lib/arm_fingerprint.py` (substrate content hash + cell fingerprint).
2. Per-cell complete-RNG-reset helper + template update.
3. `/queue-experiment` smoke step: assert RNG reset + emit fingerprint fields.
4. `scripts/arm_reuse_report.py`: group manifests by fingerprint, report would-be
   hits + compute saved. **No reuse executed.**

Nothing in Phase 0 can invalidate an experiment -- it only adds fields and a report.

---

## 9. Phase 1 consumer design (scoped 2026-06-06; build = chip)

Phase 0 *records* fingerprinted baselines. The Phase 1 **consumer** is what turns
those records into actual compute savings: it lets a new iteration (643b / 610g)
**skip re-training its OFF baseline arm** by reusing a previously-minted cell --
under a strict refuse-by-default gate so it can never substitute a non-identical
baseline.

### 9.0 Hard prerequisite gate (do not build/enable before this passes)

The consumer MUST NOT be enabled until the **cross-instance determinism check**
(Phase 0 step §7b.4: mint the 610 baseline on cloud-2 AND cloud-3) has come back
**agreeing within a written tolerance**. Reason: Regime A reuse treats a cached
cell as a *representative draw* for (substrate, config_slice, seed) on a
machine-class. That is only sound if two instances of the same machine-class
actually produce the same draw. If cloud-2 vs cloud-3 diverge beyond tolerance,
Regime A is invalid as built and reuse must wait for Regime B (bit-exact) instead.
Record the measured divergence + the chosen tolerance in §7b before enabling.

### 9.1 Lookup index (built by the indexer)

Add a fingerprint index materialised by `build_experiment_indexes.py` (so it
refreshes every governance run):

```
evidence/experiments/arm_fingerprint_index.json
  { "<arm_fingerprint>": {
      "run_id", "manifest_path", "experiment_type", "machine_class",
      "reuse_eligible", "outcome", "cell_keys": [...],   # metric keys recorded for the cell
      "superseded": bool                                 # mirrors manifest evidence_direction
  }, ... }
```

Only cells with `reuse_eligible: true` and a non-ERROR parent outcome are
indexed. Multiple runs sharing a fingerprint collapse to one entry (they are by
construction the same random variable); prefer the newest non-superseded run.

### 9.2 The consumer helper (refuse-by-default)

`experiments/_lib/arm_reuse.py :: try_reuse_cell(config_slice, seed, script_path,
needed_keys, cite_run_id=None) -> dict | None`

It recomputes the requesting cell's fingerprint (same function Phase 0 emits) and
returns a cached cell **only if ALL hold**, else `None` (caller then runs the arm):

1. An index entry exists for that exact fingerprint. (Fingerprint equality
   already implies same substrate_hash + config_slice + seed + machine_class +
   regime -- so the machine-class guard and substrate guard are intrinsic: a
   Mac-run iteration cannot match a cloud-minted baseline; it simply re-runs.)
2. `cite_run_id`, if given, matches the index entry's run_id (explicit-cite mode,
   Phase 1 default -- auditable, low blast radius). Automatic any-match is a
   later opt-in.
3. Cached `reuse_eligible: true` and parent `outcome != ERROR` and not
   `superseded`.
4. **`set(needed_keys) subset of set(cell_keys)`** -- the cached cell actually
   recorded every metric this experiment reads off its OFF arm. (If 643b measures
   a NEW OFF-arm quantity the mint didn't record, reuse cannot supply it -> refuse
   -> re-run. This is the easiest correctness trap to miss.)
5. Schema version matches (`arm_fp/v1`).

On reuse, the returned cell is stamped with provenance:
`reused_from_run_id`, `reused_fingerprint`, `reused_at_utc`.

### 9.3 Provenance + governance (a reused run must be as rigorous as a fresh one)

- Every reused cell in the consuming manifest carries the provenance fields above
  so it is self-describing and a reviewer sees exactly what was fresh vs reused.
- **No double-counting:** the indexer treats a reused cell as a pointer, not new
  independent evidence (moot for `baseline`/`diagnostic` arms which are already
  scoring-excluded, but enforce the rule generally).
- **Supersession back-reference:** maintain a reverse index run_id -> [runs that
  reused it]. If a source run is later marked superseded/invalidated, flag every
  downstream consumer `pending_reuse_revalidation` (analogous to
  `pending_substrate_reconfirmation`). A consumer must re-run the arm to clear it.
- Reuse NEVER changes how `outcome` / acceptance criteria are computed -- the
  criteria run over the (possibly reused) cells identically.

### 9.4 Opt-in path (/queue-experiment)

A new iteration opts in by: (a) constructing its OFF arm from the lineage's
**canonical baseline module** (§7b) -- this is what makes the fingerprint match by
construction; and (b) declaring `reuse_baseline_from: <mint_run_id>` in the queue
entry. The script calls `try_reuse_cell(..., cite_run_id=<that run_id>,
needed_keys=<the OFF metrics it reads>)`; on `None` it runs the arm normally and
logs `reuse_refused: <reason>`. Add this as a documented (checklist) step in the
skill, mirrored to both skill dirs.

### 9.5 Build checklist (the chip)

1. Gate-check: cross-instance determinism (§9.0) passed + tolerance recorded.
2. `arm_fingerprint_index.json` writer in `build_experiment_indexes.py` (+ run in
   `governance.sh`).
3. `experiments/_lib/arm_reuse.py :: try_reuse_cell` with all §9.2 refuse rules;
   unit-test each refuse branch (fingerprint mismatch, ineligible, ERROR,
   superseded, missing needed_keys, schema mismatch, cite mismatch).
4. Provenance stamping + indexer non-double-count + supersession reverse-index +
   `pending_reuse_revalidation` flag.
5. `/queue-experiment` opt-in step (both dirs) + extend `arm_reuse_report.py` with
   a consumed-vs-fresh audit (and a refused-with-reason tally).
6. First live use: write 643b (or 610g) via `/queue-experiment` citing the mint;
   confirm in its manifest that the OFF cell shows `reused_from_run_id` and the
   treatment arms ran fresh -- and that flipping one config byte flips it back to
   a fresh run (the refuse path actually fires).

### 9.6 Stop conditions / non-goals

- If §9.0 fails, STOP -- do not ship Regime A reuse; escalate the Regime A vs B
  decision to the user.
- Still whole-cell reuse only (no partial/warm-start). Still same-machine-class.
- Keep the refuse path the default everywhere: a false miss is cheap, a false hit
  corrupts science (plan §2).
