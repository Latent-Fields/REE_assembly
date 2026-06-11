# Non-degeneracy scoring net — empirical validation against history

- **Generated (UTC):** 2026-06-11T17:44:26Z
- **Scope:** validation of the non-degeneracy scoring net (landed 2026-06-11) against
  the full historical `non_contributory` backlog.
- **Status:** analysis + one applied refinement (see §4). No `claims.yaml` edits.
- **Net under test:** `ree-v3/experiments/_metrics.py` `check_degeneracy()` /
  `metric_is_degenerate()` (producer) → REE_assembly indexer
  `build_experiment_indexes.py` `non_degenerate=false → scoring_excluded="degenerate"`
  (consumer, parallel to `superseded`).

## 0. What was measured

Every `scoring_excluded: "non_contributory"` entry in
`evidence/experiments/claim_evidence.v1.json` — **308 claim-entries across 172 unique
run manifests** — was opened and classified by reading the recorded load-bearing metric
arrays (per-seed / per-arm / `arm_results` / `criteria`), not just the prose
`evidence_direction_note`. Each run was placed in one bucket:

- **DEGENERATE** — the net would auto-catch it: the load-bearing discriminative metric is
  pinned at a constant (zero cross-arm/cross-seed spread), floor-pinned, ceiling-saturated,
  empty, or non-finite, so its criterion is structurally incapable of firing regardless of
  behaviour (the V3-EXQ-514m / V3-EXQ-642 pattern).
- **NOT_DEGENERATE_SUBSTRATE** — a required substrate / mechanism / training was absent or
  untrained, but the load-bearing metric *varied* across cells (it was not pinned).
- **NOT_DEGENERATE_PRECONDITION** — a measurement precondition was unmet (dry-run scale,
  too-few events / samples / contacts, undertrained graduation gate) — too little/too noisy
  data rather than a structurally-pinned criterion.
- **NOT_DEGENERATE_SCOPE** — claim co-tagged but not actually tested / superseded by a
  per-claim cleanup / wrong-mechanism-under-test.
- **UNCLEAR** — the manifest persisted only an empty `metrics.json` and no informative note;
  the metric shape is unrecoverable.

Classification used the net's exact `metric_is_degenerate` rule and the tiebreak the
producer follows: **classify by metric SHAPE, not by the prose cause.** A run whose note
blames a "substrate gap" but whose recorded load-bearing metric is in fact a flat constant
across all cells is DEGENERATE — the net catches it by shape regardless of the upstream
reason (env bug, swallowed exception, untrained encoder, inert consumer, …).

## 1. Coverage — how much manual-autopsy load the net removes

| Bucket | Runs (n=172) | % runs | Entries (n=308) | % entries |
|---|---:|---:|---:|---:|
| **DEGENERATE (net auto-catches)** | **75** | **43.6%** | **129** | **41.9%** |
| NOT_DEGENERATE_SUBSTRATE | 46 | 26.7% | 94 | 30.5% |
| NOT_DEGENERATE_PRECONDITION | 29 | 16.9% | 56 | 18.2% |
| NOT_DEGENERATE_SCOPE | 14 | 8.1% | 18 | 5.8% |
| UNCLEAR (undeterminable from manifest) | 8 | 4.7% | 11 | 3.6% |

**Headline: the net would have auto-flagged ≈ 44% of the historical `non_contributory`
backlog by metric shape** (45.7% of the 164 determinable runs). Each of these previously
needed a manual `/failure-autopsy` to reclassify a `weakens` / `does_not_support` /
`superseded` direction down to `non_contributory`. Going forward those self-report at
measurement time.

Two qualifications on the headline:

- **It is a producer-side catch.** The net only fires if the experiment author calls
  `check_degeneracy()` and feeds it the *load-bearing criterion's* discriminative quantity.
  44% is the ceiling of automatic catch under correct usage — the net cannot retroactively
  catch a run nobody instrumented. Its strength is that, once wrapped, it catches the
  degenerate shape *regardless of the upstream cause* — and a large share of historical
  degenerate runs were caused by bugs the author did not anticipate (env.step() zeroing the
  channel in 256/255; a swallowed `TypeError` nulling `goal_state` in 490e; an untrained
  encoder flooring the comparator in 642/523a/528). Those are exactly the cases prose-level
  self-routing got wrong and shape-level self-report gets right.
- **A meaningful slice of the 75 were NOT manual-autopsy cases — they were mis-scored
  evidence the net would have *corrected*.** e.g. V3-EXQ-267 / V3-EXQ-355 were scored
  `does_not_support` for ARC-038 with `phase1_harm_rate` **byte-identical** (0.012966…)
  between ENABLED and ABLATED arms; V3-EXQ-418 scored `does_not_support` for SD-017 with the
  primary DV `action_bias_divergence = 0.0` in both arms. The net would have excluded these
  from scoring instead of letting a vacuous `does_not_support` weight the claim.

## 2. Per-claim view (top non_contributory claims)

`DEG` = net auto-catches; `SUB`/`PRE`/`SCO` = the three reasons it does not; `UNC` = unknown.

| claim | total | DEG | SUB | PRE | SCO | UNC |
|---|---:|---:|---:|---:|---:|---:|
| MECH-112 | 19 | 5 | 8 | 4 | 0 | 2 |
| MECH-309 | 17 | 5 | 9 | 0 | 3 | 0 |
| SD-029 | 14 | 4 | 5 | 5 | 0 | 0 |
| SD-012 | 13 | 3 | 2 | 8 | 0 | 0 |
| SD-015 | 12 | 5 | 2 | 5 | 0 | 0 |
| MECH-256 | 11 | 3 | 3 | 5 | 0 | 0 |
| ARC-062 | 11 | 3 | 7 | 0 | 1 | 0 |
| ARC-030 | 9 | 3 | 3 | 1 | 0 | 2 |
| SD-017 | 9 | 7 | 1 | 0 | 1 | 0 |
| SD-011 | 8 | 2 | 1 | 1 | 4 | 0 |
| ARC-033 | 8 | 4 | 1 | 3 | 0 | 0 |
| MECH-230 | 8 | 2 | 4 | 1 | 0 | 1 |

Read-out: the net's value is **claim-dependent**. It clears most of SD-017's backlog (7/9 —
the SD-016/SD-017 "context-conditioning never wired to policy → `action_bias_divergence`
bit-identical" family) and half of SD-015's, but barely dents MECH-309 (5/17 — that backlog
is dominated by the ARC-062 GatedPolicy substrate-ceiling family where the metric genuinely
*varied* across arms) and SD-012 (3/13 — dominated by dry-run / insufficient-event
preconditions). SD-011's backlog is mostly SCOPE (over-broad co-tags from the SD-003/ARC-033
era), which the net is not designed to touch.

## 3. Gaps — what `non_contributory` causes fall OUTSIDE "degenerate"

The 89 NOT_DEGENERATE runs (51.7%) need mechanisms other than the degeneracy net. They split
into three causes, each with an existing or recommended counterpart:

### 3a. SUBSTRATE-not-ready (46 runs / 26.7%) — the largest gap
A required substrate/mechanism was absent or untrained, but the load-bearing metric varied
across cells (so the shape net correctly does NOT fire). Examples: V3-EXQ-074f (wanting
resource-rate 0.15/0.25/0.37 across arms; missing serotonergic gain), V3-EXQ-543f/g/i/j
(GatedPolicy `rho` varied per seed but head-differentiation does not robustly persist — a
genuine substrate ceiling), V3-EXQ-262 (`fwd_r2` varied; ARC-033 prerequisite absent),
V3-EXQ-506 (agency separation ratios 1.005/1.002/0.99 — at the no-separation ceiling but not
pinned).

**Counterpart: `p0_readiness_gate()` (already shipped alongside the net) is the right tool —
not the degeneracy net.** A SUBSTRATE case is precisely "the substrate was not trained enough
to make the measurement non-vacuous"; the pre-registered P0 abort gate is designed to catch
that BEFORE the measurement phase and self-route `substrate_not_ready_requeue`. The
historical SUBSTRATE runs are the evidence that `p0_readiness_gate` carries at least as much
load as `check_degeneracy`, and the two are complementary (one fires before P0, one at
measurement). Several recent runs already do this correctly (654a/654b self-route on a
`crf_frac_active < 0.30` readiness floor; 642a/643a re-issues add `pred_mag` /
`raw_score_range` readiness preconditions). The gap is that the gate is opt-in; consider
making a P0 readiness assertion a soft requirement for any substrate-readiness diagnostic.

### 3b. PRECONDITION-unmet (29 runs / 16.9%)
Dry-run smoke scale (326/328a/330a/353 — 3 ep × 10 steps, no training signal),
insufficient-event starvation (431/433e/433f — `agent_caused` hazard trials below the
sufficiency floor), or undertrained graduation gates (523/537b/537c — phase-2 `r2` below the
0.9 graduation threshold so the comparison phase never ran). The metric is not pinned; there
is simply too little / too noisy data, or a calibration mismatch (330a's 2.0× threshold,
396a's train-vs-eval variance mismatch).

**Counterpart: a *sample/event-count precondition*, distinct from both degeneracy and P0
readiness.** Many of these already encode an `n >= floor` trial-sufficiency gate (the SD-029
`c0_trials_sufficient` gate, the 514m contact guard) — the gap is that the gate's outcome was
historically scored FAIL/non_contributory rather than self-routed `substrate_not_ready` /
`inconclusive_undersampled`. `p0_readiness_gate` with `direction:"lower"` on a sample count
covers the structural ones; the dry-run cases are arguably a queue-hygiene matter (a dry-run
manifest should never reach the index — `experiment_purpose` / a `dry_run:true` exclude would
be cleaner than relying on degeneracy).

### 3c. SCOPE / tag mismatch (14 runs / 8.1%)
The claim was co-tagged but not the mechanism actually under test (V3-EXQ-095/095b/324:
SD-011 co-tagged on runs that tested ARC-033/SD-020), superseded by a per-claim cleanup
(543f/543h superseded by 543i), or a diagnostic probe that self-passed its own localization
(563), or an env-confounded attribution (630). The metric is often fine; the run just does
not bear on THIS claim.

**Counterpart: this is the `claim_ids` accuracy discipline (REE_assembly CLAUDE.md "claim_ids
Accuracy Rule") + `evidence_direction: superseded`, not a metric net.** No automatic
shape-based catch is appropriate or possible here — scope is a judgement about *what the
experiment tests*, which is upstream of any metric.

**Summary of the gap structure:** the degeneracy net is the right tool for exactly one of the
four `non_contributory` causes (vacuous criterion). The other three already have, or should
get, distinct mechanisms: `p0_readiness_gate` for substrate-not-ready, a sample-count
readiness/queue-hygiene gate for precondition-unmet, and `claim_ids` discipline for scope.
The net is correctly *narrow*; it should not be widened to absorb these.

## 4. Shape-logic findings — and the applied refinement

The classification surfaced the actual degenerate shapes in the manifests. The original
`metric_is_degenerate` (zero-spread `spread<=eps`, empty-array, non-finite, low `floor`)
**correctly covers the dominant families**, all confirmed against real data:

- **Zero cross-arm/cross-seed spread / bit-identical arms** — the largest family (418a, 436,
  436a, 483e, 543d, 543e, 543k, 569, 590, 261, 325, 325a, 355, 355a, 603, …). Caught by
  `spread <= eps` **when fed the discriminative quantity** (see footgun below).
- **Floor-pinned at 0 / never-written channel / n=0 events** (514m, 514k, 514l, 248, 255,
  536, 247, 321, 595). Caught by all-zeros `spread<=eps` or explicit `floor`.
- **Empty-array (size 0)** (322: `n_cosine_samples=0`). Caught by `arr.size==0`. Validated.
- **Non-finite (NaN / null correlations)** (597: null `corr_*`; 117: nan sentinel). Caught by
  `np.all(np.isfinite)`. Validated.

Two shapes the original logic did **not** robustly catch were found, and motivated a
backward-compatible refinement (applied to `_metrics.py`, validated, preflight 7/7):

1. **Ceiling-saturation with residual jitter — a genuine logic gap.** V3-EXQ-651
   (`arc060_blocked_goal_recovery`): the load-bearing `goal_prox` readout is **ceiling-pinned
   at ≈ 0.98** in both arms; the on-vs-off delta is 0.0079 / −0.0008 — tiny but NOT exactly
   zero. Feeding the raw values gives spread ≈ 0.02 (> eps); feeding the deltas gives spread
   ≈ 0.009 (> eps) — so **neither** the bare zero-spread test nor a paired-delta feed catches
   it. The criterion can't fire because the readout is saturated against its 1.0 rail, below
   its own resolution. **Fix: added a `ceiling` parameter** symmetric to `floor` — degenerate
   if `min >= ceiling`. `check_degeneracy({"goal_prox":{"values":[…], "ceiling":0.95}})` now
   flags it. (Saturated-low readouts were already coverable via `floor`; saturated-high were
   not.)

2. **Per-seed/per-arm paired pinning — a feed-discipline footgun.** V3-EXQ-603 (and the whole
   543e/543d/569 family): ARM pairs are **bit-identical within each seed** (entropy 0.0=0.0,
   0.406=0.406, 0.326=0.326) but the metric **varies across seeds**. The criterion fires on
   the *within-seed cross-arm* difference, which is 0 for every seed — degenerate. But pooling
   all `(seed × arm)` values into one flat list gives spread 0.41 (> eps), so a naive flat
   feed to `metric_is_degenerate` **wrongly passes**. The docstring already says to feed
   "per-arm-per-seed *separations*" (which would be `[0,0,0]` → caught), but the raw-pool feed
   is an easy mistake on the single largest degenerate family. **Fix: added
   `metric_groups_are_degenerate()` and a `"groups"` key** — pass per-seed arm tuples and it
   checks each group in isolation (degenerate iff *every* group is internally pinned, even
   when cross-group varies). Correctly does NOT fire when one seed genuinely differs.

**Deliberately NOT changed: `eps` stays 1e-9 (tight).** Several near-constant cases are
degenerate-in-spirit (396a's eval-variance `0.07106827 / 0.07106826`, spread ≈ 1e-8). It is
tempting to widen eps to absorb them, but that would false-positive **genuine small-but-real
spreads that are weak results, not vacuous criteria** — e.g. V3-EXQ-614b's necessity-delta
0.0866 (a near-miss, a real signal) and V3-EXQ-632's `c1=[3.011, 0, 0]` (a genuine
structured-vs-ablated dissociation on the one foraging seed). The right tool for near-constant
saturation is the new `ceiling`/`floor` rails keyed to the metric's own bounds, **not** a
loosened equality tolerance. The exact-zero / bit-identical family is the safe catch and
1e-9 is correct for it. This is documented in the refined `metric_is_degenerate` docstring.

### Refinement summary (applied)
`ree-v3/experiments/_metrics.py`:
- `metric_is_degenerate(...)` gains `ceiling` (degenerate if `min >= ceiling`).
- new `metric_groups_are_degenerate(groups, ...)` for within-group/paired criteria.
- `check_degeneracy(...)` spec dict gains `"ceiling"` and `"groups"` keys; flat list and
  `{"values","floor"}` forms are **bit-identical** to before.
- Validation (run 2026-06-11): 514m / floor / genuine-spread / near-miss / 632 all behave as
  before; 651 caught via `ceiling`; 603 caught via `groups`; one-real-diff group not flagged.
  `python3 scripts/run_regression_suite.py --preflight` → 7/7 passed.

## 5. Bottom line

- **Coverage (a):** the net removes ≈ 42–46% of the historical `non_contributory`
  manual-autopsy load by metric shape (75/172 runs; 129/308 entries; 45.7% of determinable
  runs). It is genuinely load-bearing and, on top of the manual backlog, would have *corrected*
  a handful of mis-scored `does_not_support`/`weakens`/`superseded` directions.
- **Gaps (b):** the other ≈ 52% are substrate-not-ready (26.7% → `p0_readiness_gate`),
  precondition-unmet (16.9% → sample-count readiness / dry-run queue hygiene), and scope/tag
  mismatch (8.1% → `claim_ids` discipline / `superseded`). The net is correctly narrow; these
  want different mechanisms, all of which exist or are recommended. The single highest-value
  complementary mechanism is broader adoption of the already-shipped `p0_readiness_gate`.
- **Shape-logic (c):** zero-spread + non-finite + floor + empty-array are validated against
  real shapes. Added `ceiling` (genuine gap: ceiling-saturation with jitter, V3-EXQ-651) and a
  `groups`/paired mode (footgun-hardening for the bit-identical-arms-per-seed family,
  V3-EXQ-603). Kept `eps` tight on purpose — widening it would convert weak-but-real results
  into false degenerates.

### Appendix — 8 UNCLEAR runs (unrecoverable shape)
147a, 235 (×2 timestamps), 237a, 325a, 514b, 539 persisted only an empty `metrics.json` + a
one-line "FAIL" summary with no `evidence_direction_note`; the load-bearing metric shape is
not recoverable from `evidence/`. They are old run-dir-format manifests; deciding their bucket
would require the original runner logs. Excluded from the coverage denominator's
"determinable" figure.
