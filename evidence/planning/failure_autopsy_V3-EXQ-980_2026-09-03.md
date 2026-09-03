# Failure autopsy -- V3-EXQ-980 (SD-e1 H-c: E1-alone rollout readout regime)

- **Generated (UTC):** 2026-09-03T04:15:52Z
- **Scope:** single
- **Status:** confirmed (user, interactive Step 8 gate, 2026-09-03T05:04:52Z)
- **Session:** autopsy-20260903-fails-diagnostics
- **Run:** `v3_exq_980_sd_e1_h1c_readout_regime_e1_alone_20260902T212300Z_v3` -- PASS, `experiment_purpose: diagnostic`, `claim_ids: []`
- **Self-route label:** `readout_regime_consistent_damping_replicates`
- **Ledger question:** `sd_e1_residual_crush_locus`, leg `H-c` / `H-readout-regime`
- **Source autopsy:** `failure_autopsy_V3-EXQ-976_2026-09-02` (confirmed)

## 0. One-paragraph summary

This is the cheap sibling probe the V3-EXQ-976 autopsy designated as *"a sibling, never a gate"*, and it
did its job: it **eliminated** its leg. The evaluator's hybrid E1/E2 rollout regime is not what suppresses
E1-side per-action divergence at depth. The elimination meets the full bar -- a live control, a
non-degenerate run, and a criterion that could have gone the other way -- and the margin is large. Four
bounds are disclosed below, of which the most interesting is that the run's own PASS token carries no
scientific information at all.

## 1. Facts reconstruction

### 1.1 Dry-run gate and recording

`check_dry_run_citations.py`: clean; `dry_run` is not a manifest key. `validate_recording.py`: OK, 1
complete, 0 always-core gaps. Flat manifest (no run pack) by design. `elapsed_seconds` 497 on
`ree-cloud-4`. **No recording debt.**

### 1.2 Substrate health -- all 16 cells genuinely trained

4 arms (`single_step`, `single_step_stateful`, `rc_flat`, `rc_decay`) x 4 seeds (42, 123, 7, 2024).

| check | observed | verdict |
|---|---|---|
| `n_e1_grad_steps` | 2,614 - 2,705, identical across arms at each seed (`e1_grad_step_gap_per_seed` all 0) | healthy |
| `grad_cos_samples` | 262 - 271, none 0 | healthy |
| `trained_loss_last_over_first_fifth` | 0.405 - 0.729 | training |
| `cr_real_h1` | 0.1998 - 0.2677 against a 1e-4 floor | healthy |
| `missing_action_calls` | 0.0 on all 16 | healthy |
| criteria coverage | `n_total = expected_total = 8` per (arm x readout); no cell dropped by the NaN guard | complete |

## 2. The finding: H-c eliminated

### 2.1 The arithmetic

With `growth_X(h) = cr_ratio_X(h) / cr_ratio_X(1)` and `damped <=> growth_on < growth_off` (same readout
both sides), and because `cr_ratio_hybrid(1) == cr_ratio_e1alone(1)` by exact float equality on all 16
cells, `growth_e1alone_X(h) = growth_hybrid_X(h) * r_X(h)` is an **identity**. A flip to "not damped"
under E1-alone therefore requires

`r_on / r_off >= growth_hybrid_off / growth_hybrid_on`  (the flip bar).

- **flip bar, measured:** 1.828 - 7.975
- **`R = r_on/r_off`, measured:** 0.4922 - 0.9200 on **16 of 16** decision cells
- **equivalently:** under the E1-alone readout, OFF-arm depth growth exceeds ON-arm depth growth by
  **2.52x - 10.99x** on every cell (against 1.83x - 7.98x under hybrid)

Every cell moved **further onto the damped side**, never toward the discriminating one. Verdict: 8/8
damped under both readouts on both ON arms.

Worked example (`rc_flat` seed 123, h=30 -- the minimum R): hybrid ON {1: 3.40e-03 -> 30: 6.352e-03} gives
`gH_on = 1.8720`; hybrid OFF {1: 5.897e-04 -> 30: 2.644e-03} gives `gH_off = 4.4841`. E1-alone ON
{1: 3.40e-03 -> 30: 2.694e-03} gives `gE_on = 0.7939`; E1-alone OFF {1: 5.897e-04 -> 30: 2.279e-03} gives
`gE_off = 3.8637`. So `r_on = 0.4241`, `r_off = 0.8616`, `R = 0.4922`, flip bar `= 2.395` -- R sits 4.9x
below the bar.

### 2.2 The sign is opposite to the hypothesis, on the consumer's own statistic

H-c is directional: it asserts the hybrid regime *suppresses* the divergence an E1 objective produces at
depth. Measured `r_on` of 0.41-0.87 means the **hybrid** readout reports **more** ON-arm divergence growth
than E1's own autoregressive map does. And on the statistic the MECH-135 consumer actually reads --
absolute `cr_ratio` at h=30 -- the hybrid reads **1.16x - 2.36x higher** than E1-alone on every ON cell
(~1.0x on OFF). The hybrid consumer is, if anything, over-generous to the ON arms at depth.

### 2.3 The elimination bar

| requirement | evidence |
|---|---|
| **Control passed** | the OFF arm grows 2.44-4.48x from h=1 under hybrid and 2.53-3.86x under E1-alone on every seed -- a live, non-flat control under both readouts. Notably **not** the analytically-zero control that made V3-EXQ-965's C1 unsound. |
| **Non-degenerate** | `non_degenerate: true`; all 11 readiness preconditions met; full criteria coverage (section 1.2). |
| **Could have gone the other way** | the flip bar is finite (1.83-7.98), and the run's own data prove this readout pair *can* disagree by two orders of magnitude on this substrate -- see bound (3). |

### 2.4 The null is the pre-registered one

Verbatim from `failure_autopsy_V3-EXQ-976_2026-09-02`, hid `H-readout-regime`:

> "Declared null: on the same trained cells, the ON-vs-OFF depth-growth contrast under an E1-alone rollout
> readout (`predict_long_horizon` on the identical 40 sequences) matches the hybrid readout's (damping in
> both)."

That is exactly what was run, and exactly what held.

## 3. Four bounds on the result

1. **The PASS token carries no scientific information.** `status`/`outcome`/`verdict` are all assigned
   unconditionally once readiness passes (`driver:1577`, inside the `else:` of `if not non_degenerate:`),
   and every criterion is emitted `"passed": true` (`driver:1587`, commented *"this criterion CLASSIFIES,
   it does not gate PASS/FAIL"*). The outcome lives entirely in `interpretation.label`. This matters
   beyond this run: `pending_review.md` and every other downstream consumer read the PASS token.
2. **The hybrid half is a byte-level re-emission of V3-EXQ-976**, not an independent replication sample:
   96 of 112 cell fields are exactly equal across all 7 horizons, and the 16 differences are all
   `arm_fingerprint` (driver hash / substrate hash / file count). This cuts both ways -- "replicates" in
   the self-route label overstates, but the bit-identity is also what makes the pre-registered null's
   *"on the same trained cells"* clause literally true. Only the E1-alone series is new evidence.
3. **A 109x readout discrepancy in the discriminating direction exists -- on the excluded anchor arm.**
   `ARM_single_step_stateful` seed 2024: hybrid growth 0.347 vs E1-alone 37.9 at h=30 (24.8x at h=2,
   66.3x at h=5). Three things make this a disclosed limitation rather than a defect. The arm's exclusion
   from the verdict is **pre-registered** in the driver's `ON_ARMS` / `OFF_ARM` / `DEPTH0_ARMS`
   definitions (`driver:279-321`) -- what the V3-EXQ-976 autopsy separately labelled *post hoc at n=4* was
   treating that **cell** as an outlier in anchor-vs-ON comparisons, a different exclusion. The
   discrepancy is a degenerate-base artifact: the cell's h=1 `cr_ratio` is 2.98e-05, about 100x below
   every other cell, while its E1-alone h=30 value sits inside the ordinary band. And substituting that
   arm as OFF leaves both readouts still agreeing (`neither_damped`).
4. **Scope.** The null was measured on trajectory-accuracy arms only, because no divergence-preserving arm
   exists yet. That the hybrid consumer would not under-read *such* an objective is extrapolated by sign,
   not measured. The confirmer is free: keep this run's E1-alone readout beside the hybrid at h=30 in the
   ITEM-3 driver.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | `claim_ids: []`; bears on INV-088 / MECH-135 through its question, not a tag |
| Biological reference | clear | forward-model rollout divergence under candidate action sequences; this run probes the READOUT, not the mechanism |
| Prerequisites | present | ITEM 1's action channel landed and works (V3-EXQ-965); all 16 cells trained |
| Implementation | complete | both readouts computed on the identical 40 sequences; bit-identical at h=1 as designed |
| Environment | adequate | see the substrate-stability note below |
| Measurement | under-instrumented | the criterion discriminates, but see section 5 |
| Integration | coupled, stable | |
| Scale | adequate | |

**Substrate-stability note**, for a reader of the manifest alone: `substrate_stable_across_run` is
`false` (12 cells at hash `56b47d5a`, 4 at `3020335a`, produced by
`include_driver_script_in_hash=(arm != OFF_ARM)`), and `substrate_commit.dirty` is `true` on one unrelated
path. The bit-identity to V3-EXQ-976 -- which ran clean -- proves this had no numerical effect.

### Failure-location summary (GOV-FAILLOC-1)

| bucket | verdict |
|---|---|
| MECHANISM | not established |
| MEASURES | not established |
| ENVIRONMENT | established |
| **REE FAILED** | **no** |

**Net: MIXED.** The scientific finding stands on a real directional margin, but the test-design defects in
section 5 sit alongside it. Not chargeable to REE -- this run tests a readout, not a competence.

## 5. Test-design defects (latent here, not exercised)

None of these changed this run's result; all are worth fixing before the pattern is reused.

- **The completeness guard is denominated on the invocation's own seed list.**
  `expected_total = len(seeds) * len(depth_horizons_for_damping)` (`driver:1497`), where `seeds` comes
  from `--seeds` and is truncated to 2 under `--dry-run`. A 2-seed run yields `expected_total = 4`,
  `majority = 3`, and can still emit `verdict: "damped"`. The one pre-registered seed-count constant,
  `registered_majority_seeds = 3`, is written to the manifest (`driver:1636`) and **read by no verdict**.
  Latent here -- the run used its full 4 seeds -- and corrupting in a short-seed invocation.
- **The reported threshold is not the applied rule.** Criteria report `"threshold": 0.5`
  (`driver:1593`) while the applied rule is `majority = n_total // 2 + 1` = 5 of 8 = 0.625
  (`driver:1508`). Measured fractions were 1.0, so nothing turned on it.
- **The `undetermined` escape hatch is unreachable** whenever `non_degenerate` is true: the
  `cr_ratio_finite_at_decision_horizons` precondition asserts finiteness over exactly the value set
  `_damping_verdict` excludes on. The driver says so itself (`driver:1499-1504`).
- **`registered_rc_non_vacuity_floor` (0.01) is recorded and never applied** -- the driver marks it
  "RECORDED diagnostic only" at its definition (`driver:275`).
- **The whole-run vacuity conjunct is the weaker of the two computed:** `non_degenerate` uses
  `p_some_on_arm_non_vacuous` (one non-vacuous ON arm suffices) rather than the stricter
  `p_rc_non_vacuous_all`, which is computed and surfaced but not conjoined.

## 6. Repair pathway

**Node classification:** `complicated (buildable)` -- and the build is already named and already chipped.

**Routing: `implement-substrate`**, amending `SD-e1-rollout-consistency-training`.

**The amend is deliberately small, and governance should expect that.** The entry's status already reads
`item2_candidate1_null_MET_under_entry_text__rollout_endpoint_contrastive_LICENSED_item3`; its hint
already records that the E1-alone probe is *"NOT a gate, in parallel"*; and the build already has a chip
(`chip-20260902-sde1-item3-rollout-endpoint-contrastive`). Priority, severity, `substrate_paths` and
`unblocks_claims` are unchanged no-ops. The operational content is **one paragraph plus the 980 record**:
that H-c is eliminated, and the scope clause asking the ITEM-3 driver to retain the E1-alone readout.

**Recorded as an `implementation_log` entry, not a `failure_record`.** The three existing failure records
(108b, 965, 976) name the SD's bars as `target` and are genuinely open. This run's "target" is a
counterfactual readout that did not materialise -- that is the null holding, not an open failure.

**Re-derive brake: does NOT fire.** This run eliminated a leg rather than re-testing a claim against a
known ceiling, and it is the probe the source autopsy explicitly designated non-gating. No refusal
applies.

**No fan-out recommendation.** The V3-EXQ-976 autopsy already pre-registered the successor portfolio
(`H-objective-class-divergence`, `H-readout-regime`, `H-objective-horizon-budget`); this run closes one of
those three. Opening more legs before the lead build runs would duplicate that portfolio.

## 7. Step 9b -- the ledger, and a carried-forward debt

**The leg this run adjudicated does not exist in the registry.** `sd_e1_residual_crush_locus` still holds
exactly three hypotheses; `H-readout-regime` greps to zero. The reason is that
`failure_autopsy_V3-EXQ-976_2026-09-02` ran in **staging mode**, drafted its ledger edits into a
`hypothesis_space_ledger_pending` block, and could not write the registry. Those edits were never applied.

This session is interactive, holds the Step 8 gate, and therefore applies **both** halves in one pass:

1. **Carried forward from the 976 autopsy** -- labelled fan-out growth (invariant 3a) adding
   `H-objective-class-divergence`, `H-readout-regime` and `H-objective-horizon-budget`; `initial_frozen_count`
   3 -> 6 with `initial_frozen_count_at_registration` preserved at 3; a `fanout_growth_events` entry; and
   the `H-training-objective` resolution patch that artifact drafted for V3-EXQ-976.
2. **This run's own Mode B resolve** -- `H-readout-regime` -> `eliminated`, all three bar fields true,
   `resolved_utc` = the run's completion.

**Invariant 3a(a) -- git witness.** The pre-registering artifact was added at REE_assembly `985c619de5`,
committer date **2026-09-02T14:09:21Z**, and confirmed at `baf4941661`, **15:26:50Z**. V3-EXQ-980 ran at
**21:23Z**. Pre-registration precedes adjudication and is witnessed in git, not merely asserted by a
timestamp field.

**Growth-restriction check:** `sd_e1_residual_crush_locus` carries **no** `growth_restriction` field
(re-read 2026-09-03). No STOP. Surfaced at the Step 8 gate regardless, because this is growth on an
adjudicated question.

**Axis families:** both new axis labels (`learning-signal`, `eval-dynamics`) are already in
`axis_families.map`. No map addition needed.

**`fanout_growth_note` is set on the question**, recording that it has grown once (3 -> 6), has not
converged, and that two of the three added legs are on the `learning-signal` family which already held
`H-training-objective` -- so the convergence class should be read before treating the growth as
refinement.

## 8. Step 7b / 7c

- **7b (`autopsy_pre_routing_checks.py`):** `fire_count: 1` -- **C7**, naming `cr_real_h1` and
  `grad_cos_samples` as bit-identical across arms in every seed. **Dismissed with reason:** both are
  arm-invariant by construction rather than discriminating DVs. `cr_real` is a real-trajectory denominator
  common to all arms -- it cancels exactly from the `growth_on < growth_off` comparison -- and
  `grad_cos_samples` is a sampling count set by `grad_cos_sample_every`. The quantities the verdict
  actually reads (`cr_ratio_{hybrid,e1alone}_by_h`) vary across arms as required. C1/C2/C3 report
  **inapplicable** (claim-keyed; no `claim_ids`), so 7c carried that load.
- **7c (adversarial red-team, Fable -- a different model from the drafter): CONFIRMED.** The reviewer
  recomputed the full 16-cell R and flip-bar table from the manifest's own `cr_ratio_*_by_h` dicts and
  matched every figure to four decimals, verified the bit-identity to 976 field by field, verified the
  null against the pre-registration verbatim, verified the git witness, and confirmed the anchor
  exclusion is pre-registered rather than post hoc. It found no defect that would change what this
  artifact asserts or recommends. Six hygiene items were raised and **all are applied above**: the
  "2.0x-11.0x" phrasing (which mixed two statistics) is replaced with the two correctly-bounded
  quantities; caveat (3) no longer conflates the arm's pre-registered exclusion with the 976 autopsy's
  post-hoc cell exclusion; the bit-identity is now stated as satisfying the null's "same trained cells"
  clause as well as limiting the "replicates" wording; the `failure_record` shape is replaced by an
  `implementation_log` entry; the substrate-stability split is noted with its bit-identity proof; and the
  scope clause for the ITEM-3 driver is added.

**A CONFIRMED verdict is not proof the artifact is clean** -- and 7b's claim-keyed checks were
structurally blind here. Both layers ran; neither suppressed the other.

## 9. What governance should apply

1. **Amend** `SD-e1-rollout-consistency-training`: the one-paragraph hint update and the
   `implementation_log` entry. No priority/severity/path change.
2. **No claim edits.** `claim_ids: []`; `evidence_direction` `non_contributory`;
   `epistemic_category` `standard`. INV-088 and MECH-135 are untouched by this run.
3. **Ledger:** apply both halves of section 7 (the carried-forward 976 growth + this run's resolve), then
   run `build_hypothesis_space.py` and `check_hypothesis_space_integrity.py` and confirm the growth
   appears under **Advisory -- labelled fan-out growth**, not as a bucket-(b) violation.
4. **Note the staging-mode debt pattern**: a confirmed autopsy's `hypothesis_space_ledger_pending` block
   is not self-applying, and nothing sweeps for unapplied ones. This is the second artifact in this
   lineage to carry one.
