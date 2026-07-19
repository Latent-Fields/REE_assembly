---
closure_plan:
  id: arm_reuse_fingerprint
  # generation: process -- this is an infrastructure/tooling lane, not V3
  # substrate science. It owns no scientific claims, so it is segmented out of
  # the V3 closure % (read_closure counts only generation: v3) and rendered on
  # the shared `process` tab alongside the convergence intake pipeline.
  generation: process
  title: "Arm-Reuse Fingerprint (baseline-arm reuse via substrate fingerprint)"
  registered: 2026-06-10
  last_updated: 2026-06-10
  # Infrastructure / tooling plan -- owns no scientific claims directly. It only
  # touches the INV-074 (610 crystallization) and modulatory-authority (643)
  # OFF-baseline lineages via the canonical baseline modules it mints from.
  scope_claims: []
  sibling_plans: []
  nodes:
    - id: "arm_reuse_fingerprint:P0"
      title: "Phase 0 -- instrument only: arm_fingerprint lib (substrate content-hash + per-cell fingerprint), complete per-cell RNG reset, would-be-savings report. Zero validity risk."
      phase: 0
      status: done
      severity: medium
      owner_exq: null
      last_updated: 2026-06-06
      completion_note: "experiments/_lib/arm_fingerprint.py (substrate_hash over ree_core/** + env + _harness + _lib/** + OFF-path source; config_slice; seed; regime), reset_all_rng helper + template/queue-experiment smoke step, and scripts/arm_reuse_report.py (group-by-fingerprint would-be-hits) all landed. Phase-0 emits fields + a report only; nothing can invalidate an experiment."
    - id: "arm_reuse_fingerprint:MINT"
      title: "Baseline pre-minting -- canonical baseline modules + low-priority cloud mint experiments for the 610 (INV-074) and 643 (modulatory-authority) OFF baselines."
      phase: 0
      status: done
      severity: low
      owner_exq: "V3-EXQ-644 / V3-EXQ-645 (610, cloud-2/3); V3-EXQ-646 (643, cloud-4)"
      last_updated: 2026-06-07
      completion_note: "Canonical modules exq610_inv074_crystallization_baseline.py + exq643_modulatory_authority_baseline.py (byte-for-byte fidelity to the source OFF arms, auto-bound into substrate_hash via the _lib/** glob). Mint scripts landed + queued low-priority (10) on the cloud machine-class; all three mints PASSed Phase-0 emit-only with reuse_eligible=true."
    - id: "arm_reuse_fingerprint:GATE"
      title: "Section 9.0 hard prerequisite -- cross-instance determinism gate (610 OFF baseline minted on cloud-2 AND cloud-3; agree within pre-registered tolerance)."
      phase: 0
      status: done
      severity: high
      owner_exq: "V3-EXQ-644 (cloud-2) + V3-EXQ-645 (cloud-3)"
      last_updated: 2026-06-07
      completion_note: "PASSED -- user-ratified 2026-06-07T13:30Z. Fingerprint-scoped comparison of the two cloud mints: seeds 42/43 agree to <= 1.56e-2, well within the pre-registered 0.05 TIER-2 tolerance; zero false collisions (Phase-0 exit criterion met). Seed 44 correctly excluded (cloud-3 source drifted mid-run -> different substrate_hash -> the fingerprint refused, not a false hit). Regime A (distributional reuse) confirmed + SANCTIONED on the linux-x86_64-py3.10 cloud machine-class. Reproduce via scripts/arm_reuse_determinism_check.py."
    - id: "arm_reuse_fingerprint:P1-build"
      title: "Phase 1 consumer machinery -- arm_fingerprint_index.json writer, try_reuse_cell refuse-by-default helper, provenance/supersession reverse-index, /queue-experiment opt-in step."
      phase: 1
      status: done
      severity: medium
      owner_exq: null
      last_updated: 2026-06-09
      completion_note: "_write_arm_fingerprint_index in build_experiment_indexes.py (runs in governance.sh; indexes only reuse_eligible + non-ERROR + non-superseded cells; reverse_index + pending_reuse_revalidation). experiments/_lib/arm_reuse.py::try_reuse_cell over every section-9.2 refuse rule with provenance stamping. tests/contracts/test_arm_reuse.py 24/24 green. queue-experiment opt-in step mirrored to both skill dirs; arm_reuse_report.py extended with a consumed-vs-fresh + refused-with-reason audit."
    - id: "arm_reuse_fingerprint:P1-fix"
      title: "Driver-script_path coupling fix -- include_driver_script_in_hash so a consumer with its own driver can match a mint's fingerprint (the automated index-HIT enabler)."
      phase: 1
      status: done
      severity: medium
      owner_exq: null
      last_updated: 2026-06-09
      completion_note: "Phase-0 mint folded its own script_path into substrate_hash, so a consumer's distinct driver got a different hash -> no index entry -> the automated path could never HIT. Fixed 2026-06-09 via include_driver_script_in_hash (default True = legacy coupling, existing 644/645/646 fingerprints unchanged). With BOTH mint and consumer passing False, the OFF cell anchors on the canonical baseline module (already in the substrate glob) + config_slice + seed + machine_class; a discriminator keeps the two modes isolated. Regression test_arm_reuse.py 24/24 (+3: cross-driver HIT, default-mode refuse, mode-isolation)."
    - id: "arm_reuse_fingerprint:P1-cite"
      title: "First live use -- explicit-cite consumer (V3-EXQ-647) reuses all three 646 OFF-baseline cells with full provenance, runs treatment arms fresh."
      phase: 1
      status: done
      severity: low
      owner_exq: "V3-EXQ-647"
      last_updated: 2026-06-09
      completion_note: "v3_exq_647_modulatory_authority_reuse_split (cloud-4, 2026-06-06, user-supervised) reused ARM_A seeds 42/43/44 from the V3-EXQ-646 mint with section-9.3 provenance stamps (reused_from_run_id / reused_fingerprint / reused_at_utc + full arm_fp/v1 block) and ran ARM_B/ARM_C fresh -- section-9.5 step-6 core acceptance met. Note: in 647 the AUTOMATED try_reuse_cell still refused (fingerprint_not_in_index, the driver-coupling bug since fixed in P1-fix); the explicit-cite copy carried the reuse."
    - id: "arm_reuse_fingerprint:P1-auto"
      title: "First AUTOMATED index-HIT in the wild -- next genuinely-needed iteration (610g / 643c) re-mints its OFF baseline AND consumes it via try_reuse_cell(include_driver_script_in_hash=False); confirm reused_from_run_id in-manifest + that flipping one config byte flips back to a fresh run."
      phase: 1
      status: done
      severity: low
      owner_exq: "V3-EXQ-685 -- LANDED PASS 2026-06-15 (run_id v3_exq_685_arm_reuse_automated_hit_demo_v3exq685_20260615T095533Z_v3; experiment_purpose=baseline, claim_ids=[]; interpretation.label=arm_reuse_automated_index_hit_demonstrated). A minimal purpose-built consumer; superseded the now-cancelled 610g/643c natural-trigger plan."
      completion_note: "P1-auto CLOSED 2026-06-15 (/governance). V3-EXQ-685 landed PASS -- the first AUTOMATED index-HIT in the wild: mint a False-mode (include_driver_script_in_hash=False) OFF cell, run the real indexer over a temp corpus, consume via try_reuse_cell from a DISTINCT driver (reused_from_run_id/reused_fingerprint/reused_at_utc stamped in-manifest), and confirm a one-byte config flip refuses (fingerprint_not_in_index). Section-9.5 step-6 acceptance demonstrated on the fleet. claim-free baseline (no claim weighting); marked reviewed in review_tracker. The Phase-1 arm-reuse machinery is now end-to-end proven (mint -> index -> automated cross-driver HIT -> flip-refuses)."
      depends_on: []
      last_updated: 2026-06-15
      blocking_on: "The natural trigger is GONE: the WATCH MARKER fork resolved to (b). V3-EXQ-655 LANDED 2026-06-13T07:04Z (FAIL, non_contributory) -- the stripped REINFORCE control did NOT collapse (D2 0.065<0.10, D1~0 sign-inconsistent, ARM_4 bit-identical to ARM_0); per failure_autopsy_V3-EXQ-655_2026-06-13 + USER DECISION 2026-06-13, INV-074 accepted as substrate_ceiling and the 610 cascade STOPPED (no re-queue, no substrate_queue entry; claims.yaml governance_note_2026_06_13). So 610g will NEVER run and 643c is not needed -- the automated index-HIT cannot arise naturally. RESOLUTION (user-directed 2026-06-15): mint a minimal purpose-built consumer instead -> V3-EXQ-685 (queued). It mints a False-mode OFF cell from the 610 canonical module, runs the REAL indexer over a temp corpus, consumes via try_reuse_cell from a DIFFERENT driver (the automated index-HIT), and confirms a one-byte config flip refuses -- self-contained, never touches the committed arm_fingerprint_index.json. Smoke 2026-06-15: full 4-pass demo PASS (mint fp reuse_eligible -> indexed -> cross-driver HIT with reused_from_run_id/reused_fingerprint/reused_at_utc stamped -> flip refused fingerprint_not_in_index). Status STAYS blocked until 685 RUNS + PASSes on the fleet (fleet idle as of 2026-06-15T06:29Z; entry distributes via git on origin/main, awaits operator-started reconcile). Machinery fully built + unit-tested (P1-build/P1-fix); determinism gate passed (GATE)."
      governance_2026_06_10: "Closure-map onboarding. Case 3 in closure-drift terms: legitimately non-terminal -- the Phase-1 consumer is built, tested, and sanctioned; the single remaining item is a demonstration that can only happen when a real successor experiment (610g via the 610f redesign successor, or 643c) is independently needed. Arm-reuse is a compute optimisation, not a v3-closure blocker."
      governance_2026_06_11: "WATCH MARKER: re-evaluate P1-auto when governance runs on V3-EXQ-655 results. 655 is the decisive INV-074 crystallization-necessity redesign (true task-distribution shift, supersedes 610f). FORK: (a) if the task-shift collapses the stripped control -> necessity premise instantiated -> 610g warranted -> 610g's run is the first automated arm-reuse consumer (closes P1-auto). (b) if it ALSO fails to collapse -> accept INV-074 substrate_ceiling, STOP the 610 cascade with evidence -> 610g likely never runs -> P1-auto stays Case-3 blocked (or repoints to 643c). Also corrected the owner ref: the live successor is the in-flight 655, not 656 (656 is its unqueued backup)."
      governance_2026_06_15: "WATCH MARKER RESOLVED -> fork (b). 655 landed FAIL/substrate_ceiling 2026-06-13; user STOPPED the 610 cascade, so 610g is cancelled and 643c is not needed -- the natural trigger is dead. Rather than leave P1-auto parked on a dead trigger (or re-park it on the not-needed 643c), the user directed minting a minimal purpose-built consumer: V3-EXQ-685 (queued, ree-v3 main 51906a9). Owner repointed 610g -> 685. Status stays blocked until 685 runs + PASSes (verification-before-complete); on PASS this node closes (the section-9.5 step-6 acceptance is demonstrated in 685's --dry-run smoke and will be confirmed by the fleet run). closure_status.md regenerates from this frontmatter on the next /governance run (status unchanged -> snapshot tables do not shift; last_updated bump resets the stale-since-review clock)."
---

# Arm-Reuse Fingerprint -- Design Plan

**Status:** IMPLEMENTED through Phase 1. Phase 0 instrument + Phase 1 consumer machinery landed and unit-tested; §9.0 determinism gate PASSED + user-ratified 2026-06-07; Regime-A reuse SANCTIONED on the cloud machine-class; explicit-cite live use exercised (V3-EXQ-647). Driver-`script_path` coupling fixed 2026-06-09 (§9.7) so the automated index-HIT path can fire. Remaining: first *automated* index-HIT in the wild. The 610g/643c natural trigger is **cancelled** -- V3-EXQ-655 landed FAIL 2026-06-13 (fork (b): INV-074 accepted as substrate_ceiling, 610 cascade STOPPED by user decision). Per user direction 2026-06-15 the automated-HIT is demonstrated by a minimal purpose-built consumer, **V3-EXQ-685 (queued)**, which mints a False-mode OFF cell, indexes it via the real indexer, and automated-HITs it from a distinct driver (4-pass --dry-run smoke PASS 2026-06-15). P1-auto closes on the 685 fleet run. Original decisions resolved in §7.
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
    "machine_class": "<system>-<arch>-py<major>.<minor>-torch<version>",
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
- **machine_class** -- the class the hash is valid within (Regime A reuses only
  within one class). `<system>-<arch>-py<major>.<minor>-torch<version>`. The torch
  component was added 2026-07-19; see §12 for why its absence was a live false-HIT
  hazard and what the hard cut cost. (This bullet and the `machine_class` line in the
  block above also correct a long-standing doc bug: `machine_class` has always been in
  the hash -- `arm_fingerprint.compute_arm_fingerprint` puts it there -- but the §3.2
  spec omitted it while §3.3 correctly listed it as a refuse condition.)
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

> **MACHINE-CLASS TAG CHANGED 2026-07-19 (§12) — every baseline minted before that date is
> dead.** `machine_class` now includes the torch version, so the whole pre-cut bank (1212
> fingerprints) no longer matches and cannot be migrated. Nothing about the minting
> *procedure* below changes; what changes is that a mint's reuse class is now
> `<system>-<arch>-py<major>.<minor>-torch<version>`, and a **fleet torch upgrade retires a
> banked baseline exactly as an OS or python change always did**. When declaring a mint's
> reuse class (in prose, in a `reuse_machine_class` metadata field, or in a baseline
> module's header), name the torch build too — several existing scripts still carry the old
> bare tag and are now wrong (listed at the end of §12).

> **POLICY RECONCILIATION (2026-07-14, user-directed) — the default is now IN-LINE minting, not a separate mint job.** The machinery below is correct, but the *authoring default* it seeded (queue a dedicated baseline-only MINT experiment for every multi-arm run) was retired. The first experiment of a lineage already fingerprints its OFF arm for free (§7b step 1 / Phase-0 emit); the ONLY thing that makes that in-line fingerprint reusable by a later, different-driver sibling is (a) factoring the OFF arm into the canonical `_lib/baselines/<lineage>.py` module and (b) emitting it with `include_driver_script_in_hash=False`. With both, **the first real run IS the mint** — zero extra compute. A separate, dedicated OFF-arm×seeds mint job is therefore redundant by default and is queued **only** in two cases: (1) **bank-before-consumer** — a consumer is already planned and you want the baseline finished on idle cloud workers *before* the consumer's driver runs (the original §7b use-case, still valid); or (2) the **Mac machine-class escape** — the first run is `darwin-arm64`-only, so a cloud-class baseline needs its own cloud job. This does not change any fingerprint semantics, the refuse-gate, or §9 — it only moves the *producer* from "second job" to "the first experiment itself" everywhere except those two cases. Standing instructions updated in `CLAUDE.md` ("The FIRST experiment of a lineage mints its own baseline in-line") and the `/queue-experiment` skill "Saving a baseline for reuse (PRODUCER side)" block. The rest of §7b below is preserved as the historical design record of the (now-exceptional) separate-mint path.

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
- **Cross-instance determinism result: PENDING cloud-3.** `V3-EXQ-644` (cloud-2)
  landed PASS 2026-06-07T05:10Z (3 OFF cells, seeds 42/43/44). `V3-EXQ-645`
  (cloud-3) is **in-flight** -- seed 44 (final), episode 700/2500, overall 76% as
  of 2026-06-07T08:13Z heartbeat; not wedged, just slow (CX22). The check is on
  the *metrics*; the `arm_fingerprint` hash is identical across the two **by
  construction** (coarse `machine_class = linux-x86_64-py3.10`).

- **PRE-REGISTERED TOLERANCE + METHOD (fixed 2026-06-07T08:22Z, BEFORE V3-EXQ-645
  metrics were visible).** Pre-registering avoids choosing the tolerance after
  seeing the data, which would hollow out the gate. Method + tiers are encoded in
  `REE_assembly/scripts/arm_reuse_determinism_check.py` (run it when 645 lands):
  - Per seed `s in {42,43,44}`, per metric `m in {end_phase_2_entropy,
    end_phase_3_entropy, mean_reward}`: `d = |cloud2[s,m] - cloud3[s,m]|`.
  - **TIER 1 (bit-near):** all `d <= 1e-6` -> instances effectively bit-identical
    on CPU torch; Regime A solid (approaches Regime B for free).
  - **TIER 2 (distributional):** all entropy `d <= 0.05` AND all reward
    `d <= 0.05` -> cached cell is a valid representative draw for matched-control
    use. Rationale: `0.05` is ~7% of the ~`0.68` cross-**seed** entropy spread
    (`0.67..1.35` in the 644 mint) -- the spread that defines the OFF arm's role
    as a per-seed matched reference -- so a drift this small cannot change which
    seed-arm comparison a treatment is measured against. Scientifically immaterial.
  - **FAIL (any `d > 0.05`):** Regime A invalid as built -> **STOP**; escalate the
    Regime A-vs-B decision to the user; leave NO experiment wired to skip an arm.
  - **False-collision guard:** equal per-seed fingerprints WITH out-of-tolerance
    metrics is the exact failure the gate exists to catch; the script flags it
    loudly. (644 cloud-2 OFF metrics for reference: seed42 p2=1.347902 p3=1.349533
    r=-1.019894; seed43 p2=0.669239 p3=0.691710 r=-1.146585; seed44 p2=1.162011
    p3=1.144879 r=-1.076574; substrate_hash `cebea8b3...`.)
  - _Record the measured worst `|diff|` + final verdict on the line below once 645
    lands._
  - **MEASURED RESULT (2026-06-07T13:16Z; V3-EXQ-645 landed PASS on cloud-3):**
    - **FINGERPRINT-SCOPED VERDICT: PASS (TIER 2 distributional). Regime A confirmed.**
      The gate's predicate (plan 9.0) is a claim about cells the reuse system would
      actually collide -- equal-fingerprint pairs. Both such pairs agree well within
      tolerance:
      - seed 42 (fp `3dac296b…`, substrate `cebea8b3…` both instances): worst
        `|diff|` = 8.32e-3 (p3_entropy).
      - seed 43 (fp `c1c21648…`, substrate `cebea8b3…` both): worst `|diff|` =
        1.56e-2 (p2_entropy).
      - **scoped worst entropy `|diff|` = 1.56e-2, worst reward `|diff|` = 8.31e-3**
        -- both << TIER2 `0.05`. **Zero false collisions** (Phase-0 exit criterion
        met). Two CX22 instances are mutually *distributionally* deterministic
        (NOT bit-exact -- diffs are 1e-3..1e-2, exactly the Regime-A regime; Regime
        B is neither achieved nor claimed).
    - **Seed 44 EXCLUDED -- substrate drift, not a failure.** cloud-3's seed-44 cell
      ran against a DIFFERENT source (`substrate_hash` `8599c533…` vs cloud-2's
      `cebea8b3…`, same 90 files -> content changed). Three `ree_core` commits landed
      during seed-44's ~06:00-13:16Z window and were pulled in by the heartbeat
      `git pull --rebase --autostash`: `71dfb2b` (ARC-065 GAP-A e2.world_forward
      source), `84c091c` (MECH-314a Phase-2), `e3b5c9b` (ControlVector logging). The
      fingerprint **correctly** gave seed 44 a different hash, so the reuse system
      would refuse to collide it (cache MISS, not a false hit). Its positional
      `|diff|` = 5.43e-2 is expected (different code -> different trajectory) and
      harmless. This is a live demonstration that the fingerprint catches mid-run
      drift -- a positive for the design.
    - **POSITIONAL VERDICT (literal pre-registered, all 3 seed-pairs): FAIL** by
      4.3e-3 on one metric (seed-44 p3_entropy 5.43e-2 > 0.05). Recorded for full
      transparency. The positional comparison did not enforce the equal-fingerprint
      precondition that plan 9.0's predicate requires (a same-`(substrate,config,seed)`
      claim), so it compared two *different* computations on seed 44. The
      fingerprint-scoped verdict is the correct scoping; the script's `--json`
      emits both. Reproduce: `python3 scripts/arm_reuse_determinism_check.py`.
    - **GATE DISPOSITION: PASS -- RATIFIED by user 2026-06-07T13:30Z.** The
      fingerprint-scoped reading is accepted (2/2 comparable pairs within tolerance,
      zero false collisions, seed-44 drift correctly excluded). The re-mint-seed-44
      option was offered and declined. **Regime-A reuse is now SANCTIONED** on the
      `linux-x86_64-py3.10` cloud machine-class, which retroactively legitimises the
      `646 -> 647 / 643b` cloud-class reuse already exercised. Reuse remains
      refuse-by-default per cell (every plan 9.2 rule still applies); the gate
      lifting only removes the "do-not-enable" hold, it does not relax any guard.
    - **SCHEDULED RE-VERIFY (2026-06-07T19:14Z, arm-reuse-determinism-check task):**
      Independent re-run of `scripts/arm_reuse_determinism_check.py` against both
      manifests on origin/master reproduces the ratified numbers exactly
      (fingerprint-scoped: 2 comparable pairs, scoped worst entropy |diff|=1.56e-2,
      worst reward |diff|=8.31e-3, both << TIER2 0.05; seed 44 excluded for substrate
      drift). SCOPED VERDICT PASS_TIER2_DISTRIBUTIONAL = POSITIONAL FAIL_REGIME_A_INVALID
      (seed-44 p3_entropy 5.43e-2). No change to the gate disposition; this line is
      an audit-trail confirmation that the scheduled check fired and concurred.

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
- **Queued (low priority 10):** `V3-EXQ-646` -> `ree-cloud-4` (re-affinitied from
  cloud-2 2026-06-06T16:17Z, confirmed upserted in the coordinator DB). **643 moved
  to the cloud machine-class** (constraint 1 above; 643a ran on `DLAPTOP-4`/`darwin-arm64`,
  which a cloud 643b could never reuse). (Single-instance: the cross-instance determinism
  check is being established by the 610 cloud-2/cloud-3 pair; 643's OFF baseline rides
  on that Regime-A confirmation rather than re-running the same check.)
- **Why cloud-4, and the 643b plan (user-directed 2026-06-06):** cloud-2/3 are busy
  with the 610 baselines (`V3-EXQ-644`/`645`); cloud-4 frees up as 643a finishes on
  the Mac. **The 643a successor (`643b`, if 643a's result needs one) will ALSO be
  pinned to `ree-cloud-4`** -- co-locating the 643 OFF baseline + 643b on one box.
  Reuse-validity is unaffected by the choice of which CX22 (the `machine_class` tag is
  coarse `linux-x86_64-pyX.Y`, identical across cloud-2/3/4); this is operational
  routing. **cloud-4 (`ree-worker-4`) is cloud-scaler mode `surge`** -- it will NOT
  auto-start for a single pending item, so it was **woken manually** for this run
  (`hcloud server poweron ree-worker-4`, 2026-06-06T16:18Z). Once 646 is `claimed`
  the scaler's held-by-self veto keeps cloud-4 up; after it completes the scaler may
  shut cloud-4 down again, so **643b will need cloud-4 woken the same way** when it is
  queued (the surge-mode worker is not auto-started by a low backlog).
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

> **TORCH IS NOW PART OF THE REUSE KEY (2026-07-19, §12).** The consumer path below is
> unchanged in structure -- `machine_class` was always in the fingerprint and always a
> refuse condition (§3.3) -- but the tag now carries the torch version, so a torch upgrade
> produces a visible MISS instead of a silent HIT against a differently-numeric baseline.
> No change was needed in `arm_reuse.py`: it looks up by fingerprint, and the fingerprint
> is derived from the tag, so the discrimination is inherited. Consequently **every entry
> in the pre-cut `arm_fingerprint_index.json` is now unreachable** -- consumers written
> against those mints will MISS and re-run until the baselines are re-minted under the new
> class. The index now also surfaces `torch_version` per entry (`None` for pre-cut
> entries) so a miss can be triaged at the lookup site.

### 9.0 Hard prerequisite gate (do not build/enable before this passes)

> **STATUS: PASSED -- user-ratified 2026-06-07T13:30Z. Reuse is now SANCTIONED**
> on the `linux-x86_64-py3.10` cloud machine-class. See §9.7 and the §7b
> "MEASURED RESULT" block. The rule below is preserved as the standing definition.

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

**Substrate-scope threading (added 2026-07-12, §11 generalization).** `try_reuse_cell`
/ `evaluate_reuse` now accept an optional `substrate_scope` (default `None` = whole-tree,
byte-unchanged). If the mint declared a dependency scope (§11) when emitting its
fingerprint, the consumer MUST pass the SAME scope here to reproduce the mint's
fingerprint and HIT -- exactly as `include_driver_script_in_hash` must match on both
sides. A mismatched or absent scope simply yields a different fingerprint that is not in
the index -> reuse REFUSED (the safe, false-miss-only outcome). Fingerprint equality
therefore still implies matched substrate content **at the mint's declared granularity**,
plus config_slice + seed + machine_class + regime.

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
**canonical baseline module** (§7b); (b) passing
`include_driver_script_in_hash=False` to BOTH the mint's `compute_arm_fingerprint`
and the consumer's `try_reuse_cell` (the 2026-06-09 fix -- this is what makes the
fingerprint match across the mint's and consumer's different driver scripts; see
§9.7); and (c) declaring `reuse_baseline_from: <mint_run_id>` in the queue entry.
The script calls `try_reuse_cell(..., cite_run_id=<that run_id>,
include_driver_script_in_hash=False, needed_keys=<the OFF metrics it reads>)`; on
`None` it runs the arm normally and logs `reuse_refused: <reason>`. Add this as a
documented (checklist) step in the skill, mirrored to both skill dirs.

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

## 9.7 Build + gate status (2026-06-06; gate CLOSED 2026-06-07)

The Phase 1 consumer **machinery is built and unit-tested**, and as of
2026-06-07 the §9.0 hard determinism gate has **PASSED (user-ratified)** --
**Regime-A reuse is now SANCTIONED** on the `linux-x86_64-py3.10` cloud
machine-class.

**Determinism gate (§9.0): PASSED -- ratified 2026-06-07T13:30Z.** Both 610
OFF-baseline mints ran: V3-EXQ-644 (ree-cloud-2, PASS 2026-06-07T05:10Z) and
V3-EXQ-645 (ree-cloud-3, PASS 2026-06-07T13:16Z), same
`v3_exq_610_inv074_crystallization_baseline_mint.py`. Fingerprint-scoped
comparison (only equal-fingerprint pairs -- the predicate §9.0 states):
**seeds 42/43 agree to <= 1.56e-2, well within the pre-registered 0.05 tolerance;
zero false collisions; Regime A (distributional) confirmed.** Seed 44 was
excluded because cloud-3's source drifted mid-run (three `ree_core` commits pulled
by the heartbeat autostash -> different `substrate_hash`), which the fingerprint
correctly flagged (refuse, not false-hit). Full numbers + the literal positional
FAIL-by-4.3e-3 (recorded for transparency) are in §7b "MEASURED RESULT". Verdict
reproducible via `scripts/arm_reuse_determinism_check.py`. **Experiments MAY now
opt in to skip a baseline arm** by citing a mint (plan §9.4), still under every
refuse-by-default rule of §9.2.

**Built this session (inert until the gate passes):**

1. `arm_fingerprint_index.json` writer -- `_write_arm_fingerprint_index` in
   `evidence/experiments/scripts/build_experiment_indexes.py`, called from `main()`
   so `governance.sh` refreshes it every run. Indexes only `reuse_eligible` +
   non-ERROR + non-superseded cells; collapses same-fingerprint runs (prefers
   newest); records `cell_keys`, `machine_class`, `outcome`, `superseded`. Builds
   `reverse_index` (source_run_id -> consumers) and flags
   `pending_reuse_revalidation` when a cited source is superseded / ERROR / missing.
   A reused cell (carrying `reused_from_run_id`) is a pointer, **not** re-indexed as
   a source (no double-count). Currently 0 fingerprints (no instrumented manifest
   has landed yet).
2. `ree-v3/experiments/_lib/arm_reuse.py` -- `try_reuse_cell(config_slice, seed,
   script_path, needed_keys, cite_run_id=None) -> dict | None` (+ `evaluate_reuse`
   returning a structured `ReuseDecision`). Refuse-by-default over every §9.2 rule;
   stamps `reused_from_run_id` / `reused_fingerprint` / `reused_at_utc` on a hit.
3. `ree-v3/tests/contracts/test_arm_reuse.py` -- 21 tests: every refuse branch
   (fingerprint mismatch, config mismatch, ineligible, ERROR parent, superseded,
   missing needed_keys, schema mismatch, cite mismatch, no-index,
   manifest-unreadable) + happy path + the indexer writer (non-double-count,
   reverse-index, pending flag, collapse-prefer-newest,
   eligibility/ERROR/superseded exclusion). All pass.
4. `/queue-experiment` opt-in step (mirrored to `.claude` + `.agents` skill dirs)
   and `scripts/arm_reuse_report.py` consumed-vs-fresh + refused-with-reason audit.

**First live use -- DONE via explicit-cite (V3-EXQ-647, 2026-06-06), reconciled
2026-06-09.** The earlier "Not done: first live use" reading here was stale and
contradicted the section-7b "MEASURED RESULT" line ("646 -> 647 / 643b cloud-class
reuse already exercised"). The accurate picture:

- **Explicit-cite consumer: EXERCISED.** `V3-EXQ-647`
  (`v3_exq_647_modulatory_authority_reuse_split`, cloud-4, 2026-06-06,
  user-supervised) reused all three OFF-baseline cells (ARM_A, seeds 42/43/44)
  from the `V3-EXQ-646` mint with full section-9.3 provenance stamps
  (`reused_from_run_id` / `reused_fingerprint` / `reused_at_utc` + the complete
  `arm_fp/v1` block, `reuse_eligible: true`) and ran ARM_B/ARM_C fresh. So
  section-9.5 step 6's core acceptance is met: the OFF cell shows
  `reused_from_run_id`, treatment arms ran fresh.
- **Automated index-HIT path: was the real remaining gap, now UNBLOCKED.** In
  647 the automated `try_reuse_cell` REFUSED all 3 seeds (`fingerprint_not_in_index`)
  because of the driver-`script_path` coupling below; the explicit-cite copy
  carried the reuse instead. So the automated `arm_fingerprint_index.json` path had
  produced zero real HITs.

**Driver-`script_path` coupling -- FIXED 2026-06-09.** The Phase-0 mint folded its
own `script_path=Path(__file__)` into `substrate_hash`, so a consumer with its own
driver got a different `substrate_hash` -> no index entry -> refuse. This made the
automated index-HIT path unreachable in practice (a real consumer never shares the
mint's driver). Resolved by `include_driver_script_in_hash` (default `True` =
legacy coupling, bit-identical; existing 644/645/646 fingerprints unchanged) in
`experiments/_lib/arm_fingerprint.py` + `arm_reuse.py`. When BOTH the mint and the
consumer pass `include_driver_script_in_hash=False`, the driver script is excluded
from the reuse-critical hash and the OFF cell is anchored on the canonical baseline
module under `experiments/_lib/**` (already in the substrate glob) + `config_slice`
+ `seed` + `machine_class` -- so two different drivers built from the same canonical
module produce the SAME fingerprint and the automated consumer HITs. A discriminator
enters the hash on the excluded path so excluded- and included-driver fingerprints
can never collide (the two modes are isolated; mint and consumer must agree on the
flag). The driver's content hash is still recorded (`driver_script_hash`,
observability only). Regression: `tests/contracts/test_arm_reuse.py` 24/24
(+3 new: cross-driver HIT enabled, default-mode cross-driver refuse, mode-isolation).

**Still genuinely not done:** the first *automated* index-HIT in the wild -- i.e.
the next genuinely-needed iteration (610g / 643c) re-minting its OFF baseline AND
consuming it with `include_driver_script_in_hash=False`, confirming in its manifest
that the OFF cell shows `reused_from_run_id` and that flipping one config byte flips
it back to a fresh run. (610g is gated on the 610f autopsy's redesign successor,
the **in-flight `V3-EXQ-655`** -- which supersedes 610f and is currently running on
ree-cloud-1. `V3-EXQ-656` is an unqueued backup variant of 655, not the queued
successor. **Re-evaluate this item when governance runs on the 655 results** -- a
collapse outcome warrants 610g, a no-collapse outcome accepts INV-074
substrate_ceiling and 610g likely never runs.)

---

## 10. Frozen-prefix tensor cache (added 2026-07-12; the maturation-curriculum family)

**Mechanism, not a phase of §§1-9.** §§1-9 describe *whole-cell, metrics-only*
reuse: a consumer skips an OFF arm by reading a prior cell's recorded scalar
metrics from a manifest (§6: "whole-cell reuse only"; §9: "no warm-start"). §10 is
a **distinct, complementary** mechanism for a family whose members share an
expensive UPSTREAM PREFIX but compute DIFFERENT downstream metrics off it -- where
the metrics-only path structurally cannot help (a differently-targeted sibling has
no matching recorded metric to read).

**Motivating family.** The maturation-curriculum frozen-representation experiments
INV-064 (`V3-EXQ-740a`, z_world IV leg), INV-088 (`V3-EXQ-744`/`744a`, z_world DV
coupling) and INV-089 (`V3-EXQ-743`, z_harm leg). Each runs an expensive prefix --
`warmup_train(onset)` (z_world) or a standalone `HarmEncoder` maturation (z_harm),
then a FIXED frozen-dataset collection -- and diverges only in a cheap tail (which
target it ridge-probes / trains an evaluator head on). The earlier
`frozen_representation_from_maturation_trajectory` reuse-ineligible flag on these
cells was **empirically FALSE**: verified bit-identical 2026-07-12 (two in-process
runs of `v3_exq_744` `_run_cell(42, 4)` -> identical `arm_fingerprint`
`ddce40b7...` and every metric to full float precision). The trajectory is
regenerated deterministically inside the cell (`warmup_train(seed, onset)`, RNG
reset by `arm_cell` on entry), so the prefix is a pure function of
`(substrate, config_slice, seed)` -- the same Regime-A determinism §§2-3 assume.

**Implementation:** `ree-v3/experiments/_lib/baselines/maturation_curriculum.py`.
Exposes, per leg, `build_*_agent` + `collect_*_dataset` + a cache-aware
`mature_and_collect_world / mature_and_collect_harm` returning a target-agnostic
SUPERSET (z_world leg: `{Z, Y, Hcur, Hnext, Zprev, A, Zcurr}`; z_harm leg:
`{Zharm, Y, Prox}`) plus the FRESH pre-maturation evaluator-head inits. The
`frozen_prefix_cache` memoises the frozen encoder (agent / HarmEncoder
`state_dict`) + the dataset tensors as a `torch.save` blob under a machine-local
dir (`REE_PREFIX_CACHE_DIR`, default `~/.ree_maturation_prefix_cache`).

**Not the §6-excluded partial-training warm-start.** §6 excludes "caching *partial
training* (checkpoint/warm-start reuse)". This cache does NOT warm-start training:
the downstream evaluator head still trains FRESH from a fixed init on every cell.
It memoises only the *completed* deterministic frozen (encoder, dataset). So the
soundness surface is the whole-cell one §§2-3 already ratified, applied to the
shared prefix rather than the whole cell.

**Soundness.** Governing asymmetry unchanged (§2): the cache key is OVER-inclusive
-- `substrate_hash` (ree_core + `experiments/_lib/**` content, so any substrate or
recipe edit invalidates) + FULL `env_kwargs` + every recipe scalar + `machine_class`
+ `seed` + `onset` + the leg tag -- so a false HIT is structurally excluded and only
(cheap) false MISSes remain. The stored key is re-verified on load; any
mismatch / unreadable / partial blob is a MISS. A cache HIT skips warmup+collect but
still rebuilds a fresh agent in the same RNG order (so the fresh head inits are
bit-identical) and the downstream tail re-seeds explicitly
(`torch.manual_seed(EVAL_TRAIN_SEED)`, local `default_rng`) -- so a HIT is
bit-identical to a cold MISS. **Verified** by
`test_maturation_bitidentity` (scratch): the module reproduces `740a`/`744`/`743`
inline output exactly across every tensor, and a HIT reproduces a cold MISS
(dataset + warmed E2-forward readout).

**Relation to the arm_fingerprint (§§0-1).** Independent and coexisting. The cells
are ALSO emitted arm_fingerprint reuse-ELIGIBLE (`include_driver_script_in_hash=False`)
so the scalar §9 path can serve an exact-config re-run; the tensor cache serves the
differently-targeted-sibling case the scalar path cannot.

**First minting consumer: `V3-EXQ-744a`** (queued 2026-07-12) -- an 8-seed
re-estimate of `744` built via `mature_and_collect_world`. `744` ran inline so
744a's run is fully cold (mints all 40 prefix cells); the tensor-reuse saving is
realized by a later world-leg sibling / a 744a re-run. Forward work: (a) a z_harm-leg
minting consumer (a `743` successor) to exercise the harm-leg cache in the wild;
(b) optional promotion of the machine-local cache to a shared (per-machine-class)
location if cross-session reuse on one worker proves valuable.

**Re-verified independently 2026-07-12** (session `friendly-ptolemy-7f207b`) in
isolated cache dirs on a stable working tree: (1) 744's 3 seeds x 5 onsets --
every warm-HIT cell reproduced its cold-MISS `arm_fingerprint` and every row
metric bit-identically; (2) all 7 frozen-prefix tensors `torch.equal` cold vs
warm; (3) two independent fresh processes produced identical `substrate_hash`
`ff1220aa4d2f` + prefix key -- so the fingerprint/key are cross-process
deterministic. NOTE ON DIRTY-TREE FALSE MISSES: the first full run showed the
process's *first* seed's key/fingerprint transiently differing for ~5 cells, then
stabilising -- traced to a concurrent working-tree edit to a substrate `.py`
(parallel session / heartbeat autostash window) shifting `compute_substrate_hash`
mid-run. Per the section 3.2 content-hash-of-the-working-tree choice this is the
*designed* behaviour and its only effect is a cheap false MISS (over-inclusive key
= false-miss-only); it is NOT a defect and must NOT be "fixed" by hashing the git
SHA (that reintroduces the section 3.2 dirty-tree false-HIT hazard). It does,
however, motivate section 11.

---

## 11. Dependency-scoped substrate hashing (addendum, 2026-07-12; user-directed)

**The gap.** Section 3.2 defines `substrate_hash` as a content hash over *"the source
files the cell **depends on**."* The implementation (`arm_fingerprint._SUBSTRATE_GLOBS`)
instead hashes the WHOLE trees `ree_core/**/*.py` + `experiments/_lib/**/*.py`. That is
the coarsest possible over-approximation of "depends on": an edit to *any* module in
those trees -- sleep, the hippocampal proposer, an unrelated env, a comment -- busts a
`z_world` prefix arm that never executes a line of it. Given how continuously `ree_core`
churns, this makes cross-substrate-version reuse rarer than the validity model actually
requires, and is the dominant source of (cheap but real) false misses on top of the
section 10 tensor cache and the section 9 scalar path alike.

**The invariant that bounds every option (unchanged, section 2).** A false MISS wastes
compute; a false HIT corrupts a conclusion. So looseness is sound **only** in the
"ignore inputs that provably cannot change the cell's result" direction, **never** the
"treat two genuinely-different cells as equal" direction. Narrowing the hashed set is
safe **iff the set stays a SUPERSET of everything the cell can execute** -- then the only
new error mode remains a false miss.

**Design: author-declared scope, safe-default-to-ALL (mirrors `config_slice`).** Exactly
as `config_slice_declared` narrows the config with a conservative default (whole config
when undeclared), add an optional per-cell **substrate scope** -- the set of
`ree_core` subpackages / `_lib` modules the arm's build+collect path touches. When
undeclared, `compute_substrate_hash` hashes everything (today's behaviour, so existing
fingerprints are byte-unchanged and this ships shadow-safe). When declared, it hashes
only the declared closure. A `substrate_scope_declared: bool` + the declared glob list
are recorded in the fingerprint for audit, precisely like the config-slice discriminator.

**Conservatism requirement (the one thing that must not be wrong).** A declared scope
that UNDER-approximates -- omits a module the cell actually executes -- is a false-HIT
bug. So the declared scope must be a provable over-approximation. Acceptable ways to
obtain one, in decreasing order of safety:
  - **Static import-closure at module granularity** from the arm's entry function
    (e.g. the transitive `import` graph reachable from `build_world_agent` +
    `warmup_train` + `collect_world_dataset`). Over-includes (imports not exercised on a
    given path are still hashed) -> false-miss-only. Dynamic imports / `getattr`
    dispatch / registry lookups are the trap: if any pulls in a module NOT in the static
    graph, the scope is unsound. A guard (assert no import outside the declared closure
    fires during a smoke run, via an import hook) converts that trap into a loud failure.
  - **Author-declared subpackage list**, reviewed like `config_slice`. Lower automation,
    same safe default; relies on review rather than a tool for conservatism.

**Concrete first target: the section 10 maturation-curriculum prefix.** Its dependency
slice is unusually clean and narrow -- `CausalGridWorldV2` (env), the
`E1` + `E2.world_transition` + `E2.world_action_encoder` + `latent_stack` encoder path,
`_lib.goal_pipeline_tier1.{ArmSpec, build_config, warmup_train}`, and this baseline
module. It does NOT touch the E3 evaluator heads (trained fresh downstream, so head-code
edits are correctly irrelevant to the frozen prefix), the harm stream, the hippocampal
proposer, sleep/consolidation, or most of `ree_core`. Scoping the frozen-prefix cache key
(`maturation_curriculum._prefix_key`) to that closure turns the majority of `ree_core`
churn from a cache-bust into a legitimate hit, while staying strictly false-miss-only.
This is the natural prototype: the cache is new, self-contained, machine-local, and
already has a bit-identity harness to prove the narrowed key still refuses on any change
inside the declared closure.

**AST-normalised hashing (orthogonal, cheap).** Independent of scoping: hash the
comment/whitespace/docstring-stripped AST of each depended-on file instead of raw bytes,
so a comment-only or reformat edit to an in-scope file stops busting the arm. Semantics-
preserving, low risk, stacks with dependency scoping.

**Explicitly rejected (all reintroduce false-HIT risk):**
  - Hashing the committed git SHA / blob set instead of working-tree content -- section 3.2
    rejects this: the tree is dirty continuously (heartbeat autostash, in-flight edits),
    so a SHA would falsely match across an uncommitted edit that matters. The transient
    dirty-tree MISS noted at the end of section 10 is the accepted cost of that safety, not
    a problem this addendum should "solve" by weakening the key.
  - Behavioural / output canaries as the equality test -- can false-hit when the canary is
    blind to a change that matters downstream, and you must run the arm to compare, which
    defeats a lookup key. Distributional equivalence (Regime A, section 2.3) belongs at the
    ACCEPTANCE layer where it already lives, not the key layer.
  - Manual "recipe version" tags a human bumps -- a forgotten bump is a false hit; the
    whole section 2 apparatus exists so correctness never depends on a human remembering.

**Prototype scope (chip):** implement declared substrate-scope for
`maturation_curriculum._prefix_key` only (default-to-all preserved elsewhere), with the
static-import-closure guard and a test that (a) an edit inside the declared closure still
refuses the cached prefix and (b) an edit to an out-of-closure `ree_core` module now HITS
where it previously missed -- both while the section 10 bit-identity harness still passes.
Generalising the declared scope to the section 9 arm_fingerprint path is a later step,
gated on the prototype proving the conservatism guard holds.

### Status -- prototype BUILT + guard proven (2026-07-12, session focused-lehmann-caed72)

Implemented in `ree-v3/experiments/_lib/arm_fingerprint.py` (optional `scope=` param on
`compute_substrate_hash`; `scope=None` DEFAULT hashes everything = today's behaviour,
BYTE-unchanged -- regression-asserted, so the sec-9 path + every existing fingerprint are
untouched) and `ree-v3/experiments/_lib/baselines/maturation_curriculum.py` (`_prefix_key`
now hashes only the per-leg DECLARED SCOPE; schema bumped `maturation_prefix/v1 -> v2`).

**Static-import closure was NOT viable** (the preferred option): `ree_core/agent.py`
(REEAgent) statically imports ~all of `ree_core` at module level (sleep, pfc, amygdala,
governance, most of policy, ...), so the transitive import closure from the entry
functions is essentially the whole tree -- zero benefit. Both legs build a REEAgent, so
this is unavoidable. The prototype therefore uses the **author-declared scope +
conservatism guard** path, grounded in EXECUTION rather than imports.

**Declared scope = (executed-file closure) UNION (data-closure), per leg.** Ground truth
is a call-trace of `build+warmup+collect`: only the files whose code actually RUNS on the
frozen-prefix path. REEAgent's `__init__` is config-gated, so in this env config it
constructs only a narrow sub-graph -- sleep/pfc/amygdala/governance/most-of-policy never
execute. Result: **WORLD 24 files, HARM 19 files, vs 121 in the old whole-tree glob**
(HARM subset of WORLD). The one residual data-read channel (a scope file value-importing a
module-level CONSTANT from an un-executed module -- here only `ree_core.regulators`
`SITE_GATED_POLICY`/`SITE_LATERAL_PFC` string labels, re-exported through
`regulators/__init__` from `simulation_mode_rule_gate`) is closed by folding those 2 files
into scope; a leaf-kind AST data-closure proves nothing else escapes. Class/function
imports of un-executed modules are correctly EXCLUDED (the trace proves they are never
called, so their bodies cannot affect the deterministic prefix).

**Conservatism guard (`verify_scope_conservatism`) HOLDS -- the gate is met:**
- guard 1 (call-trace): every executed repo file is in the declared scope (PASS both legs).
- guard 2 (static AST): the scope is a data-closed FIXPOINT of existing files (PASS both
  legs). Runs opt-in at key time via `REE_PREFIX_SCOPE_GUARD=1`, and in the contract test.

**Which substrate edits now HIT that previously MISSed:** any edit to a `ree_core` module
the frozen prefix does not execute -- `sleep/**`, `hippocampal/{anchor_set,event_segmenter,
ghost_goal_bank,...}` (only `hippocampal/module` executes), the E3 downstream-head training
code, `amygdala/**`, `pfc/**` (except the `lateral_pfc`/`ofc` *config classes* that are
data-closed but uncalled -> still HIT), `governance/**`, `safety/**`, `pag/**`, `entities`,
`attribution`, `comparator`, `affect`, and most of `policy/**` -- as well as any edit to an
UNRELATED env or another `_lib` experiment helper. All of `ree_core`'s continuous churn in
those areas is now a cache HIT instead of a bust. An edit INSIDE the declared closure
(env, E1/E2 encoder path, `latent/stack`, `goal_pipeline_tier1`, `agent.py` build path,
the regulators SITE_ leaf, this module) still REFUSES the cached prefix.

**Tests:** committed fast contract `ree-v3/tests/contracts/test_maturation_scope.py`
(regression: default byte-unchanged; scope sizes 24/19; IN-CLOSURE refuses / OUT-OF-CLOSURE
hits at hash+key layer; static guard 2 tripwire; provenance record). The slow guard 1
(call-trace) + the cold-MISS/warm-HIT bit-identity harness (all 7 world tensors + fresh
head inits + warmed E2-forward readout + frozen state_dict `torch.equal`, provenance
`substrate_scope_declared`) ran GREEN as a scratch harness (23/23) and live in
`verify_scope_conservatism(run_once=...)`. Full `pytest tests/` clean (no regression).

`substrate_scope_declared` + the glob list are recorded in the cache blob + returned
provenance for audit (mirrors `config_slice_declared`). **The sec-9 generalisation gate is
now met** -- the conservatism guard is demonstrated sound; extending declared substrate
scope to the global `arm_fingerprint` path (a broader author-declared surface) is the
sanctioned next step, still opt-in + default-to-all.

### Status -- sec-9 generalization LANDED (2026-07-12, session relaxed-matsumoto-6aef13)

The author-declared substrate scope is now available on the GLOBAL `arm_fingerprint` path,
so any multi-arm experiment (not just the maturation-curriculum prefix cache) can narrow
its substrate hash the same way -- strictly opt-in + default-to-all + false-miss-only.

**Guard machinery PROMOTED to a shared module.** The two conservatism guards were lifted
out of `maturation_curriculum.py` into scope-generic `ree-v3/experiments/_lib/`
`substrate_scope_guard.py` (stdlib-only: `ast` + `pathlib` + `sys`, importable without
ree_core/torch). Public surface: `expand_scope`, `static_data_closure`, `verify_scope_static`
(guard 2), `traced_execution_files` + `verify_scope_conservatism(scope, run_once=None)`
(guard 1). A `scope` is a sequence of repo-root-relative globs (exact one-file paths are
valid single-match globs; wildcards expand against the tree, matching
`compute_substrate_hash`'s own glob semantics). `maturation_curriculum.py` now keeps ONLY
the per-leg scope declarations + thin leg-keyed wrappers (`_verify_scope_static(leg)`,
`verify_scope_conservatism(leg, run_once)`) that delegate to the shared module; its behaviour
is byte-preserved (the sec-10 tensor-cache keys are unchanged -- `test_maturation_scope.py`
6/6 green after the refactor).

**Opt-in surface (`ree-v3/experiments/_lib/arm_fingerprint.py`).** `compute_arm_fingerprint`
and `arm_cell` / `_ArmCell` take an optional `substrate_scope=None`. `None` (DEFAULT) hashes
the whole `_SUBSTRATE_GLOBS` trees -- regression-asserted BYTE-identical to before, so every
existing fingerprint + the whole prior sec-9 corpus is untouched. A non-None value is folded
into `compute_substrate_hash(scope=...)` AND into the fingerprint hash as a discriminator
(mirrors the `driver_script_excluded` discriminator + the maturation `_prefix_key` scope
fold): a scoped fingerprint can NEVER collide with a whole-tree one, and two different
declared scopes key differently (narrowing/widening the reuse contract must change the key).
`substrate_scope_declared` + the glob list are recorded in the returned payload for audit
(like `config_slice_declared`), surfaced into `arm_fingerprint_index.json`
(`substrate_scope_declared` per entry), and threaded through `arm_reuse.py`
(`evaluate_reuse` / `try_reuse_cell` -- see §9.2) so a scoped mint is reusable via the scalar
path when the consumer declares the same scope.

**Conservatism is the CALLER's obligation (governing asymmetry, §2).** Exactly as the
prototype required, `compute_arm_fingerprint` does NOT itself prove a declared scope is a
superset of what a cell executes -- an UNDER-approximating scope is a false-HIT bug that
corrupts a conclusion. Every consumer MUST run BOTH guards on its scope BEFORE trusting it:
guard 1 (`verify_scope_conservatism(scope, run_once=...)` -- call-trace: every executed repo
file is in scope) in its smoke/contract test, and guard 2 (static AST data-closure fixpoint)
which also runs opt-in at emit time via `REE_ARM_SCOPE_GUARD=1` (lazy-imported cheap
tripwire; off by default so the normal path is byte-unchanged and stays stdlib-only). Note
guard 1 captures ANY repo file whose code runs -- including the file that DEFINES `run_once`
(the cell driver) -- so a scope must name its driver, or the driver harness must live outside
the repo tree (as the maturation scratch harness did).

**Tests (all green; full `pytest tests/` = 1437 passed, 0 regressions):**
- `ree-v3/tests/contracts/test_substrate_scope_guard.py` -- the promoted guard module
  standalone: glob expansion, data-closure fixpoint, guard 2 catches a non-data-closed scope
  (dropping the regulators SITE_* leaf) + a missing declared file, guard 1 catches an
  under-approximating scope + passes a covering one.
- `ree-v3/tests/contracts/test_arm_fingerprint_scope.py` -- the global surface: default path
  byte-identical; scope folds into the key (no collision with whole-tree; declared-whole-tree
  != undeclared; two scopes differ); an OUT-OF-scope substrate edit now HITS while an IN-scope
  edit refuses; `arm_cell` threads the scope identically; the `REE_ARM_SCOPE_GUARD=1` tripwire.

**Not yet done (forward work, not blocking):** no live experiment declares a global
`substrate_scope` yet -- the surface is available + guarded, but the first real consumer (a
multi-arm script whose OFF closure is clean enough to declare + guard) is a follow-on. The
`/queue-experiment` opt-in step (§9.4) documents `include_driver_script_in_hash`; a
`substrate_scope` opt-in note there is the natural next addition when the first consumer lands.

---

## 12. Torch version in `machine_class` (addendum, 2026-07-19; user-directed)

**The hazard (a live, silent false-HIT channel).** `machine_class()` was
`"{system}-{arch}-py{major}.{minor}"` -- e.g. `linux-x86_64-py3.10`. Its own docstring
carried the safety assumption that *"float-rounding determinism is assumed stable within
a class"*, but the tag captured nothing about the numerics library that actually does the
float work. Upgrading torch on the cloud fleet leaves python at 3.10, so **the class tag
stays byte-identical across the upgrade while float behaviour underneath changes.** Every
one of the 1170 banked `linux-x86_64-py3.10` fingerprints would have remained matchable by
a post-upgrade consumer, which would then have compared new-torch treatment arms against
old-torch baselines -- **no cache miss, no warning, no provenance trace.** Under §2's
governing asymmetry that is the failure mode the entire design exists to prevent: a false
MISS wastes compute, a false HIT corrupts a conclusion.

This was not hypothetical. At the time of writing the fleet ran py3.10.12 / torch
2.5.1+cu121 and the Mac ran py3.13 / torch 2.10.0, with a fleet torch upgrade under
consideration. The ordering was explicit: **land this before any fleet torch upgrade** --
the whole point is that the upgrade must be visible to the cache.

**Corpus at cut time** (`evidence/experiments/arm_fingerprint_index.json`, 2026-07-19):
`n_fingerprints=1212` (1170 `linux-x86_64-py3.10` + 42 `darwin-arm64-py3.13`), all
`reuse_eligible=true`, `n_reused_cells=6`, `n_source_cells=1301`, regime A.

### Decision: HARD CUT in the hash (user-ratified 2026-07-19)

`machine_class()` now returns `<system>-<arch>-py<major>.<minor>-torch<version>`, e.g.
`linux-x86_64-py3.10-torch2.5.1+cu121`. The torch string is `torch.__version__` verbatim,
**including the local version segment**, so a CUDA-build swap is also a new class
(over-inclusion -> false misses only, per §2). A host where torch cannot be imported gets
the reserved token `torchNA`, which can never collide with a real version, so a torchless
host takes its own class rather than silently joining a torch-bearing one.

**This invalidates all 1212 pre-cut fingerprints, deliberately.** They stop matching; every
consumer that would have hit now takes a visible MISS and re-runs. That is the correct
failure direction.

**Why no migration or re-grandfathering path was offered.** Not a judgement call -- it is
structurally impossible. The fingerprint hashes `config_slice`, and **`config_slice` is
persisted nowhere**: not in the index entry (`cell_keys, experiment_type, machine_class,
manifest_path, outcome, regime, reuse_eligible, run_id, seed, substrate_scope_declared,
superseded`) and not in the stored per-cell `arm_fingerprint` payload (which keeps only
`config_slice_declared`). An old fingerprint therefore cannot be recomputed under any new
tag by any means. Separately, no pre-cut run records a torch version anywhere, so legacy
entries could only have been assigned one by assumption ("the fleet was on 2.5.1+cu121").

**Why the hash and not a side-band guard.** The considered alternative was to leave the hash
formula alone, record `torch_version` beside it, and have `arm_reuse.evaluate_reuse` refuse
on mismatch -- preserving the bank for pre-upgrade consumers. Rejected because
**`machine_class()` keys three independent caches, not one**:
`arm_fingerprint.compute_arm_fingerprint` (§9 scalar path),
`_lib/baselines/maturation_curriculum._prefix_key` (§10 frozen prefix **tensors** on disk --
the artefact most sensitive to a torch change), and `_lib/probe_warmup._cache_key`. Putting
torch in the tag protects all three from one change; the side-band guard would have lived
only in `arm_reuse.py` and left the two tensor/warmup caches unguarded. The hash route also
makes a false hit impossible *by construction* rather than contingent on a guard nobody
forgets to call.

**Cost accepted.** Small, because arm-reuse saving is prospective-only: a banked fingerprint
is worth what it would have paid out later, not what it cost to bank. With `n_reused_cells=6`
the realized loss is negligible; the forward cost is that the recently-minted reusable
baselines (`exq742_mech457_bias_head_baseline`, `exq700c_arc108_settling_baseline`, the
maturation-curriculum legs) go dead and need re-minting when next consumed.

### Also landed: `torch_version` as an observability field

`compute_arm_fingerprint`'s returned payload now carries `torch_version` **separately** from
`machine_class` (observability only -- `machine_class` is what enters the hash). Two reasons:
a future miss can be triaged as *"missed because torch moved"* instead of being an
unexplained miss; and it closes the exact data gap that made THIS cut unmigratable -- a later
tag change will have the per-run torch identity that the pre-2026-07-19 corpus lacks.

### Implementation notes

- `torch_version_tag()` is **lazy + memoised**. A module-level `import torch` would break
  `arm_fingerprint.py`'s stdlib-only importability, which `manifest_core.py` documents and
  depends on ("importable without torch/ree_core"). Resolving on first CALL preserves that.
  It deliberately does NOT use `sys.modules.get("torch")` -- that would make the tag depend
  on whether torch happened to be imported yet, i.e. nondeterministic across call sites.
- **No format-parsing fallout.** The tag is opaque everywhere in the codebase -- nothing
  splits or pattern-matches it. The `"linux-x86_64-py3.10"` occurrences in
  `test_validate_recording.py` / `test_phase3_runpack_materialize.py` are fixture literals,
  not calls, so they remain valid fixtures.
- **`validate_experiments.py` was deliberately NOT changed.** Its gates are static lints over
  experiment *scripts* (fingerprint emission, RNG reset, recording keys); torch discrimination
  is a runtime property of one library function, and a lint there would be noise rather than a
  guard. The invariant belongs in the contract suite, beside the other determinism-key
  contracts.

**Tests:** `ree-v3/tests/contracts/test_machine_class_torch.py` (6 tests, green). The
load-bearing one is `test_tag_discriminates_on_torch_version` -- same OS/arch/python,
different torch, asserted to produce different classes AND different fingerprints. That is
the regression guard: if it ever fails, a torch upgrade is silent to the cache again.
Related suites re-run green (67 passed): `test_arm_reuse.py`, `test_arm_fingerprint_scope.py`,
`test_substrate_scope_guard.py`, `test_maturation_scope.py`, `test_recording_standard.py`,
`test_arm_fingerprint_lint.py`.

**Known documentation debt (not fixed here, out of scope).** Several mint scripts and baseline
modules hardcode the OLD bare tag in prose and in one manifest metadata field --
`v3_exq_742m_..._mint.py` (`reuse_machine_class: "linux-x86_64-py3.10 (ree-cloud worker)"`),
`v3_exq_700c_mint_...py`, `_lib/baselines/exq742_mech457_bias_head_baseline.py`,
`_lib/baselines/exq700_arc108_settling_baseline.py`, `v3_exq_714_...py`. These are now
factually wrong about their reuse class. None is load-bearing (comments + one human-facing
metadata string), but they will mislead the next author; edits to experiment scripts route
through `/queue-experiment` per `CLAUDE.md`.
