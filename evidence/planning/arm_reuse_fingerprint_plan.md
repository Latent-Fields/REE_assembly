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

## 7. Open decisions (need user input before Phase 0 build)

1. **Determinism regime:** ship Regime A (distributional, same-machine-class) as
   recommended, or invest in Regime B (bit-exact, cross-machine) up front?
2. **Stopping phase:** authorise Phase 0 (instrument + measure) only, and decide
   1/2 after seeing real would-be-savings data? (Recommended.) Or pre-authorise
   through Phase 1?
3. **Config-slice declaration:** require authors to declare the OFF-path config
   slice (more savings, more author burden), or always hash the whole config
   (safer, fewer hits)? Recommend: whole-config default, opt-in narrowing.
4. **Where the cache index lives** (Phase 2 only): coordinator DB vs a committed
   index file under `evidence/`.

---

## 8. First concrete deliverable if approved

Phase 0, smallest useful unit:
1. `experiments/_lib/arm_fingerprint.py` (substrate content hash + cell fingerprint).
2. Per-cell complete-RNG-reset helper + template update.
3. `/queue-experiment` smoke step: assert RNG reset + emit fingerprint fields.
4. `scripts/arm_reuse_report.py`: group manifests by fingerprint, report would-be
   hits + compute saved. **No reuse executed.**

Nothing in Phase 0 can invalidate an experiment -- it only adds fields and a report.
