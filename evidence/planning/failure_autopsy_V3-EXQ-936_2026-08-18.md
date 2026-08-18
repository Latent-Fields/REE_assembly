# Failure autopsy -- V3-EXQ-936 (MECH-439) + GFLAG-0039 / MECH-151 evidence basis

- **Generated (UTC):** 2026-08-18T18:48:59Z
- **Scope:** cluster (2 targets; see Section 7 for why they are reported together)
- **Status:** confirmed (Step 8 interactive gate cleared 2026-08-18)
- **Session:** `pending-task-009a3a`
- **Targets:**
  1. `v3_exq_936_mech439_f_variance_share_under_f_demotion_20260817T062038Z_v3` (V3-EXQ-936, MECH-439)
  2. `GFLAG-0039` / `GFLAG-0043` -- the MECH-151 evidence basis, via
     `v3_exq_922_sd016_mech151_152_arc041_production_combo_20260812T035119Z_v3`

## Headline

**Both targets are the same failure shape: a pre-registered criterion that a substrate
degeneracy satisfies exactly as well as the mechanism would.** Neither run tested its claim.

1. **V3-EXQ-936.** The load-bearing C2 statistic (`f_variance_share`) is pinned at 1.0 to
   float64 resolution in all 8 cells. The paired reduction it requires (>= 0.05) would need
   the modulatory channels to gain **3.7e14 to 2.5e43** times more variance. Two cells' paired
   delta is *exactly* 0.0. The manifest's `weakens` direction is therefore vacuous: C2 did not
   fail, C2 could not be evaluated.
2. **The 1e72 F magnitudes are real unbounded growth, and their cause is a config-parity
   regression, not an unguarded substrate.** SD-056's rollout-norm clamp -- built 2026-05-31
   for exactly this signature, validated by V3-EXQ-617 -- is armed by this run's own declared
   parity ancestor V3-EXQ-689i and is **absent from V3-EXQ-936's baseline module**.
3. **GFLAG-0039 is CONFIRMED, on a stronger basis than the flag states.** MECH-151's only
   experimental support is a bare sign test (2 of 3 seeds, no effect-size margin, null
   false-positive rate exactly 0.5) on a quantity the driver's own training objective
   guarantees, measured on a pathway that reaches no ranking site in E3.

---

## 1. Dry-run gate (Step 2a)

`scripts/check_dry_run_citations.py` over every run this autopsy cites -- 936, 922, 689i, 571,
436f -- plus `--family v3_exq_936`: **0 dry cited, 0 dry in named families, 0 ambiguous,
0 unknown**. `dry_run: false` on the 936 manifest top level. No smoke enters any denominator.

`validate_experiments.py --checks dry_run_unreachable_criterion` reports 11 warnings, **all** in
the `v3_exq_543` b-l lineage; **silent on this driver**. Manual read of 936's dry-run reduction
block (`DRY_RUN_SEEDS=[42]`, `P0=2`, `P1_CAP=2`, `STEPS=40`, `FRESH_TARGET=4`): no criterion is
gated on an absolute episode index; C1/C2 are computed from decomposition series, and the
readiness floors (`MIN_FRESH_SELECT_PER_CELL=60`) would refuse a smoke rather than latch a
vacuous false. Clean.

Real-run denominator throughout: **4 seeds x 2 arms = 8 cells** (936); **3 seeds x 2 arms = 6
cells** (922).

## 2. Recording provenance

`ree-v3/validate_recording.py --paths <936 manifest>`: **OK -- 1 complete, 0 always-core gaps,
0 thin-pack drops, 0 schema warnings.** `substrate_hash`, `substrate_commit`, `machine`
(`ree-cloud-2`), `machine_class` (`linux-x86_64-py3.10-torch2.12.0+cpu`), `config`, `seeds`,
`elapsed_seconds` (6299.6s) all present. Single substrate hash across all 8 cells
(`per_cell_hashes_disagree: false`).

One note, not a finding: `substrate_stability_detail.process_snapshot_drift` records the on-disk
tree moving after the run resolved its identity. That is the normal
`arm-fingerprint-executed-substrate-identity` behaviour (identity resolved at process start,
disk moved later); the executed substrate is unambiguous.

**There IS a recording gap, and it is the reason this diagnosis had to be inferred rather than
read.** The run records `f_variance_abs` but no rollout-magnitude readout -- no `||z_world||`,
no per-step transition norm, no raw score range. Those quantities existed at run time (they are
computed inside `E2.rollout_with_world` and `compute_reality_cost` on every candidate) and were
discarded. Had any one of them been in the manifest, the divergence would have been visible on
first read instead of requiring the back-solve in Section 4. This is **recording-debt, not
measurement-debt** (Step 5 distinction): the repair is *recording it*, not redesigning the
metric.

## 3. Facts -- Target 1 (V3-EXQ-936)

### 3a. What the run measured

`outcome: PASS`, `evidence_direction: weakens`, `experiment_purpose: evidence`,
`claim_ids: [MECH-439]`. Two load-bearing criteria:

- **C1** `C1_a_treatment_arm_converts` -- **passed**. ARM_DEMOTION lifted committed-action-class
  entropy above ARM_OFF on 3 of 4 seeds (deltas -0.0616, +0.1043, +0.0294, +0.0695).
- **C2** `C2_converting_arm_reduces_f_variance_share` -- **failed**. Requires a per-seed paired
  reduction >= `MIN_F_SHARE_REDUCTION` (0.05) on >= 3 seeds. `n_reducing: 0`.

Combination rule: `C1 true` + `C2 false` -> `weakens`, described in the driver as "MECH-439's own
registered falsifying signature: a lever that converts WITHOUT reducing F's variance share."

All four readiness preconditions reported met.

### 3b. The numbers

| cell | var(F) | var(non-F) | `f_variance_share` | paired delta vs OFF |
|---|---|---|---|---|
| ARM_OFF / 42 | 6.387e18 | 9.418e4 | 0.999999784728175 | -- |
| ARM_OFF / 43 | **4.066e72** | 5.117e32 | 1.000000000000000 | -- |
| ARM_OFF / 45 | 9.806e65 | 1.143e28 | 1.000000000000000 | -- |
| ARM_OFF / 46 | 1.011e53 | 2.948e19 | 1.000000000000000 | -- |
| ARM_DEMOTION / 42 | 9.697e18 | 1.394e3 | 0.999999981829909 | -1.971e-07 |
| ARM_DEMOTION / 43 | **5.663e72** | 1.209e28 | 1.000000000000000 | **0.000e+00** |
| ARM_DEMOTION / 45 | 2.984e66 | 8.463e25 | 1.000000000000000 | **0.000e+00** |
| ARM_DEMOTION / 46 | 8.786e42 | 7.291e16 | 0.999999999999826 | +1.744e-13 |

`off_arm_mean_f_variance_share = 0.9999999461820437` against MECH-439's cited 571 baseline of
**0.886**.

**Headroom for C2 to fire.** ARM_DEMOTION's share would have to fall to `OFF - 0.05`, i.e.
var(non-F) >= 0.0526 x var(F):

| seed | required var(non-F) | observed | shortfall |
|---|---|---|---|
| 42 | 5.100e17 | 1.394e3 | **3.66e14 x** |
| 43 | 2.979e71 | 1.209e28 | **2.46e43 x** |
| 45 | 1.570e65 | 8.463e25 | **1.86e39 x** |
| 46 | 4.621e41 | 7.291e16 | **6.34e24 x** |

The criterion is not "not met". It is **arithmetically unreachable**, and on two seeds the
statistic has literally zero resolution in float64.

### 3c. Why the readiness guard did not catch it

The driver anticipated this exact failure mode. P3's own docstring:

> `nonf_variance_nondegenerate` -- "The NON-F (modulatory) components carry non-zero variance in
> every cell. SAME STATISTIC (a variance) that the load-bearing C2 share routes on -- **if these
> are flat, f_variance_share is ~1.0 by STARVATION and the falsifier is unmeasurable, not
> confirmed**."

The diagnosis is correct and the guard is inert: it is implemented as an **absolute** floor
(`MIN_NONF_VARIANCE = 1e-9`) against a **ratio** statistic, and passed at 1394.44. The
non-F channels were not flat in absolute terms; they were flat *relative to F*, which is the only
sense in which C2 can see them. The `/queue-experiment` rule that a readiness statistic must be
"the *same* statistic the load-bearing criterion routes on" was satisfied in name (a variance)
and violated in substance (an absolute, where C2 routes on a ratio).

**This is the single most reusable lesson in this autopsy.** A ratio-valued DV needs a
ratio-valued readiness floor.

### 3d. Float32 annihilation -- the defect is stronger than "F dominates"

`score = f + lambda_eff * m + rho_residue * phi + [benefit/novelty/goal terms]` is accumulated in
float32 (torch default; `e3_selector.py` uses no float64 anywhere on the scoring path).
float32 eps = 1.192e-07. Comparing std(non-F)/std(F) against it:

| cell | std ratio | x eps | verdict |
|---|---|---|---|
| OFF / 42 | 1.214e-07 | 1.02 | marginal |
| OFF / 43 | 1.122e-20 | 9.4e-14 | **annihilated** |
| OFF / 45 | 1.080e-19 | 9.1e-13 | **annihilated** |
| OFF / 46 | 1.708e-17 | 1.4e-10 | **annihilated** |
| DEM / 42 | 1.199e-08 | 1.0e-01 | **annihilated** |
| DEM / 43 | 4.620e-23 | 3.9e-16 | **annihilated** |
| DEM / 45 | 5.325e-21 | 4.5e-14 | **annihilated** |
| DEM / 46 | 9.110e-14 | 7.6e-07 | **annihilated** |

In **7 of 8 cells** the entire modulatory stack -- harm, residue, benefit, novelty, goal -- is
below float32 epsilon relative to F and is *additively annihilated* in the score sum. E3's
committed selection in those cells was, to machine precision, `argmin(F)` alone.

**This explains C1 rather than contradicting it.** MECH-448's F->eligibility demotion acts on
*which candidates survive to compete*, not on the additive sum, so it is the one lever whose
channel survives the annihilation. The lineage's long history -- every additive/bias-channel
diversity lever failing, the eligibility-mask lever converting -- is consistent with this being
a numerical property of the score sum rather than a fact about selection architecture.

## 4. The 1e72: is it a real substrate defect?

**Yes -- real unbounded growth in the E2 imagination rollout -- but with a named, already-built
guard that this run did not arm.**

### 4a. Mechanism: F is quadratic where the modulatory channels are linear

`compute_reality_cost` (`e3_selector.py:935-960`) is, with the untrained fallback scorer gated
out by default:

```python
transitions = world_seq[:, 1:, :] - world_seq[:, :-1, :]
coherence_cost = transitions.pow(2).sum(dim=-1).mean(dim=-1)
```

F is the **squared** z_world step norm. The modulatory channels are at most linear in the latent
scale (piecewise-linear MLP heads over states). So if the rollout scale grows by k, var(F) grows
by ~k^4 while var(non-F) grows by ~k^2 -- i.e. **var(F) ~ var(non-F)^2**.

Tested against the run's own 8 cells, OLS of log10 var(F) on log10 var(non-F):

```
log10(var_F) = 11.235 + 2.0203 * log10(var_nonF)     R^2 = 0.97834,  n = 8
OFF arm alone (n=4): slope 1.9514      DEMOTION arm alone (n=4): slope 2.1485
```

Predicted slope 2.000; measured 2.020 across **54 orders of magnitude**. The share statistic is
therefore not measuring F's selective grip at all in this regime -- it is measuring the
rollout's divergence rate, and it saturates at 1 for any latent scale above ~1.

### 4b. Magnitude: the same defect, at the same scale, as V3-EXQ-569e

Back-solving the rollout magnitude from var(F):

| cell | var(F) | F | inferred `||dz_world||` |
|---|---|---|---|
| OFF / 42 | 6.39e18 | 2.53e9 | 5.03e4 |
| OFF / 46 | 1.01e53 | 3.18e26 | 1.78e13 |
| OFF / 45 | 9.81e65 | 9.90e32 | 3.15e16 |
| OFF / 43 | 4.07e72 | 2.02e36 | **1.42e18** |

The `substrate_queue.json` SD-056 entry's own `failure_record` (V3-EXQ-569e, 2026-05-31) reads:

> "world_forward rollout magnitudes **overflow to 1e16-1e18** on most ON-arm seeds ... ARM_0 OFF
> baseline clean (rollout magnitudes **0.39-0.77**, 0 NaN). M1 rollout-divergence ratio =
> 3.79e16."

The two worst 936 seeds land **inside that band**. 1e72 is not an exotic new number: it is
`(1e18)^2` squared once more by the variance. Same code path
(`e2_fast.py::rollout_with_world`), same training scheme (SD-056 contrastive), same signature.

### 4c. The guard exists, is validated, and was dropped

`e2_fast.py:694-747` carries the SD-056 amend's lever (b):

```python
clamp_enabled = bool(getattr(cfg, "e2_rollout_output_norm_clamp_enabled", False))
...
scale = torch.clamp(max_allowed_norm / current_norm, max=1.0)
z_world = z_world * scale
```

`config.py:564`: `e2_rollout_output_norm_clamp_enabled: bool = False` -- **default OFF**,
deliberately ("bit-identical to pre-amend SD-056"). The SD-056 entry records
`V3-EXQ-617 substrate-readiness PASS 2026-05-31T11:31Z`.

V3-EXQ-936's baseline module `experiments/_lib/baselines/mech439_f_variance_share.py` declares
its `CONFIG_FLAGS` block as **"689i parity"** and mirrors 689i's adjacent lines verbatim. It
contains **zero** occurrences of `e2_rollout_output_norm_clamp`.

V3-EXQ-689i (`v3_exq_689i_mech448_f_eligibility_demotion_falsifier_repair.py:467-468`), directly
above the very lines 936 copied:

```python
e2_rollout_output_norm_clamp_enabled=True,
e2_rollout_output_norm_clamp_ratio=2.0,
```

936 kept 689i's lever (a) -- gradient clipping, `MAX_GRAD_NORM = 1.0`, applied in the driver at
line 448 -- and dropped lever (b). It ran SD-056's training without SD-056's own stability guard.

### 4d. The closest thing to an A/B the existing record supplies

689i's manifest (`v3_exq_689i_..._20260722T162850Z_v3.json`) contains **no value above 1e6**, and
its scale-sensitive readouts sit at order unity: `route_range_per_arm_mean` 0.483 (OFF) / 0.392
(ON). 936's reach 5.66e72.

**Stated honestly: this is consistent-with, not proof.** 689i recorded no variance decomposition,
and most of its readouts (entropies, rates, fractions) are bounded by construction and could not
have shown the divergence. The missing clamp is the *identified, sufficient, guard-shaped*
difference from the declared parity ancestor, matching a documented signature at matching
magnitude -- but the counterfactual has not been run. Running it **is** the recommended repair
(Section 8), so the A/B is the successor, not this artifact's claim.

### 4e. Blast radius

Of the **117** drivers in `ree-v3/experiments/` that call `world_forward_contrastive_loss`,
**20** have no `e2_rollout_output_norm_clamp_enabled` setting reachable from the driver or its
imported baseline module:

```
allon_training.py, v3_exq_149b, v3_exq_485f/g/h/i/j/k/l/m,
v3_exq_569a/b/c/d/e, v3_exq_604a, v3_exq_613, v3_exq_643, v3_exq_696, v3_exq_936
```

Five of those (569a-e) predate the 2026-05-31 amend, and 569e is the run that *discovered* the
defect -- correctly clamp-less. 613 is the pre-amend readiness probe. The remainder are
candidates for the same silent divergence, and **V3-EXQ-936 is the most recent, 78 days after
the guard landed**. Of the 97 that do set it, 63 pass `True` literally and 57 route it through a
per-driver `SD056_OUTPUT_NORM_CLAMP` constant -- i.e. arming it is the settled convention, and
936's omission is the outlier.

**Nothing in this section is offered as a corpus-wide re-adjudication.** The 19 other drivers are
named so a lint can find them; whether any of their *conclusions* moved is a separate question
this autopsy does not answer and does not assert.

## 5. Facts -- Target 2 (GFLAG-0039 / GFLAG-0043, MECH-151 evidence basis)

MECH-151: *"The cue-indexed E1 context vector (MECH-150) projects to an action_bias signal that
is added to E2.action_object() outputs, producing top-down contextual weighting of the
action-affordance manifold prior to HippocampalModule search."* Its `notes` add: *"E1 biases
which action-objects RANK HIGHLY, but E3 still selects."*

Current `live_status`: `supports -- narrow context-conditioning mechanism confirmed on 2/3 seeds`,
`from: failure_autopsy_V3-EXQ-922_2026-08-13`, and its `evidence_quality_note` records this as
the **first-ever experimental evidence entry for this claim**. `evidence: []`.

### 5a. The entire support is one bare sign test

`acceptance_checks.mech151` has exactly one criterion,
`action_bias_div_beats_off_control`, `load_bearing: true`, `seeds_pass: 2`, `majority: 2`, and
**no threshold field**:

| seed | `action_bias_div` A1 | A0 | A1 > A0 |
|---|---|---|---|
| 42 | 0.03223 | 0.03894 | no |
| 43 | 0.05261 | 0.03674 | yes |
| 44 | 0.06798 | 0.01596 | yes |

A sign test with no minimum effect size on n=3. Under the null of no effect,
`P(X >= 2), X ~ Bin(3, 0.5) = 0.5` -- **a 50% false-positive rate, exactly**. Arm means overlap
(A0 0.0305, A1 0.0509) and one seed inverts. This does not meet the repo's own standing
effect-size-gate practice (scale on the SD of the delta plus an absolute floor).

### 5b. The DV is guaranteed by the training objective

Verified in `experiments/v3_exq_922_sd016_mech151_152_arc041_production_combo.py`:

```python
# line 491
def compute_cue_action_loss(agent, z_world_detached, action):
    action_bias, _ = agent.e1.extract_cue_context(z_world_detached)
    with torch.no_grad():
        ao_target = agent.e2.action_object(z_world_detached, action.detach())
    return F.mse_loss(action_bias, ao_target.detach())

# line 523
def _action_bias_divergence(agent, z_safe, z_dang) -> float:
    ab_safe, _ = agent.e1.extract_cue_context(z_safe)
    ab_dang, _ = agent.e1.extract_cue_context(z_dang)
    return float((ab_safe.mean(dim=0) - ab_dang.mean(dim=0)).norm().item())
```

`cue_action_proj` is trained by **direct MSE regression onto `action_object(z_world, action)`**,
and `action_bias = cue_action_proj(cat([cue_context, z_world]))` (`e1_deep.py`). The regression
target is itself a function of `z_world`. A well-fitted regressor must therefore produce
different outputs on the safe vs dangerous `z_world` distributions **through the z_world half of
its input alone**, with no cue-indexing involved.

This makes GFLAG-0039's central inference -- *"the surviving action_bias variation is
attributable to the concatenated raw z_world rather than to cue indexing"* -- **entailed by the
driver's own objective**, not merely a plausible consequence of the slot-bank degeneracy. That
is a strictly stronger and more robust footing than the flag claims for itself, and it does not
depend on the contested ContextMemory premise.

The A0_OFF arm is a *real* control (it holds the same training and varies only
`cue_slot_tagger` / `selection` / `ctxdiv_weight`), so the design is the right shape. What it
cannot survive is the combination of a 50%-null criterion and overlapping arm means.

### 5c. Correction to GFLAG-0039's stated mechanism: the write path was OFF

The flag argues 922 ran "against a 1-of-16-occupied ContextMemory slot bank". The manifest's
`params` and the driver (`:429`) both record:

```
sd016_writepath_mode = "off"
```

`ContextMemory.write()` was **disabled in both arms**. 922 did not run against a degenerate slot
bank; it wrote no cue-indexed associations at all. **The conclusion is unchanged and if anything
strengthened** -- `cue_context` cannot carry learned cue-indexed content that was never written
-- but the operative confound for 922 specifically is *not* the
`contextmemory-write-path-addressing-degeneracy` entry. That distinction matters for routing:
implementing that substrate item does **not** by itself make 922's reading recoverable.

### 5d. The read-side statistic is aliased (bears on MECH-150, flagged not adjudicated)

`per_arm_summaries.sel_entropy_mean_mean`: A0_OFF **2.7725860** (= ln 16 = 2.7725887, the
`uniform_reference`, i.e. exactly uniform); A1_PRODUCTION **1.0969e-08** -- a fully deterministic
single-slot read. MECH-150's C1 (`sel_entropy < 2.5`) passed on that.

Sharp cue-indexed retrieval and degenerate collapse onto one slot produce the **same** entropy
reading, and 922 recorded no occupancy statistic (`n_occupied_slots` and every near-synonym are
absent from the manifest) to break the tie. This is the identical aliasing shape as 936's C2 --
a criterion a degeneracy satisfies as well as the mechanism does.

MECH-150 is outside this autopsy's target scope (its adjudication belongs to the confirmed
`failure_autopsy_V3-EXQ-922_2026-08-13`). **Flagged for governance, not adjudicated here.**

### 5e. GFLAG-0043's structural finding, independently verified

`grep -c "action_object\|action_bias" ree_core/predictors/e3_selector.py` -> **0**. E3 has no
action-object input channel of any kind. Confirmed contract-pinned at
`ree-v3/tests/contracts/test_exp0155_action_bias_no_scoring_authority.py`.

MECH-151's asserted "elevate which action-objects rank highly, E3 still selects" therefore has
**no implementation site**. The claim is unimplemented in its ranking half, not merely untrained
-- and per GFLAG-0043, ARC-007 STRICT ("HippocampalModule generates VALUE-FLAT proposals ... E3
introduces ALL weighting") forbids the obvious repair in `_score_trajectory`, so the claim as
stated may be incompatible with ARC-007 as stated.

## 6. Four-layer diagnosis

### Target 1 -- V3-EXQ-936 / MECH-439

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | MECH-439 could not express itself; the DV had no dynamic range. Not weakened, not supported. |
| Biological reference | **partial (divergence, load-bearing)** | F is a formal coherence proxy (squared transition smoothness), not a biological import. But no biological valuation system lets one cost channel exceed the others by 20+ orders of magnitude; divisive normalisation / gain control on competing value signals is ubiquitous (Carandini & Heeger canonical-computation line). The **absence of any normalisation on the E3 score sum** is itself a biology divergence and is load-bearing by default. No `targeted_review` covers it. |
| Prerequisites | **missing** | SD-056's rollout-stability lever (b) not armed, though the run uses SD-056 contrastive training. |
| Implementation completeness | **partial** | Guard exists, validated, and is carried by the declared parity ancestor; dropped by this lineage's baseline module. |
| Environment adequacy | **adequate** | GAP-A reef-bipartite foraging substrate, 689i-derived, 12x12, 4 hazards. |
| Measurement adequacy | **misleading** | A [0,1]-bounded ratio over an unbounded quantity; saturates by construction. Readiness guard absolute where the criterion is relative. |
| Integration adequacy | **coupled but unstable** | E2 rollout -> E3 scorer coupling is numerically unbounded end to end. |
| Scale / capacity | **the defect** | Rollout scale ~1e18; modulatory stack below float32 eps in 7 of 8 cells. |

**Failure-location summary (GOV-FAILLOC-1): MIXED -- MEASURES + MECHANISM. NOT chargeable to
REE.** Measurement `not_established` (DV structurally unsettable). Mechanism `partial` (guard
present but unarmed; parity with declared ancestor broken). Environment `established`. REE FAILED
requires all three adequate -> **not reached**.

### Target 2 -- GFLAG-0039 / MECH-151

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | 922 tested a projection's output variability, not the claim's asserted ranking modulation. Neither supports nor weakens. |
| Biological reference | **partial (divergence, load-bearing)** | vmPFC->striatum/premotor projections (Haber & Behrens 2014) are the stated analog; the 2026-08-16 Pastor-Bernier & Cisek 2011 entry describes **competition-conditioned relative** valuation. MECH-151's additive, candidate-independent form is structurally incapable of that. The 922 autopsy already recorded MECH-151's lit as "thin -- no dedicated targeted review". |
| Prerequisites | **missing** | `sd016_writepath_mode="off"`; MECH-150's own retrieval content never written. |
| Implementation completeness | **stub** | The projection exists and trains; the *ranking* half it asserts has no site (0 references in `e3_selector.py`). |
| Environment adequacy | **adequate** | Env-entropy precondition resolved by the SD-070 P0a recipe (readiness gates passed 6/6). |
| Measurement adequacy | **misleading** | DV guaranteed by the training objective through the z_world route; bare sign test, null FPR 0.5; no occupancy control. |
| Integration adequacy | **isolated** | `action_bias_divergence` is computed on `extract_cue_context()` output with zero calls into HippocampalModule, E2 rollout or E3.select. |
| Scale / capacity | **unknown** | Not reached. |

**Failure-location summary (GOV-FAILLOC-1): MIXED -- MEASURES + MECHANISM. NOT chargeable to
REE.** Measurement `not_established`; Mechanism `not_established` (ranking half unimplemented);
Environment `established`. Not a falsification of MECH-151 and not support for it.

## 7. Cluster pattern

| Target | Claim | Absolute / negative-control criterion | Discrimination criterion | Read |
|---|---|---|---|---|
| V3-EXQ-936 | MECH-439 | P1-P4 readiness all met; C1 conversion PASS 3/4 | **C2 share reduction -- arithmetically unreachable (needs 1e14-1e43x more non-F variance)** | Criterion satisfied-or-refuted identically by a substrate degeneracy |
| V3-EXQ-922 | MECH-151 | MECH-150 gate PASS 3/3; `n_cue_action_bias_present` control absent | **`action_bias_div(A1) > A0` -- guaranteed by the training objective, null FPR 0.5** | Same |

**These are NOT two independent bugs. They are one structural property, at two sites:**

> A pre-registered criterion whose *satisfaction* and whose *refutation* are both produced by an
> upstream substrate degeneracy, on a run whose readiness preconditions all report met -- because
> the readiness statistic is measured in different units (absolute) from the statistic the
> criterion routes on (relative/aliased).

Both runs recorded the readout that would have broken the tie *nowhere*: 936 discarded the
rollout magnitude, 922 discarded slot occupancy. Both readouts existed at run time. This is a
**recording-debt** pattern, not a measurement-design pattern -- the instruments could see it,
the manifests did not carry it.

Two live readings, and this autopsy does not choose between them:
- **`instrument_starvation`** -- the DVs are fine and the substrate is degenerate; fix the
  substrate and re-measure. (Favoured for 936: the fix is named and one line.)
- **`criterion_aliasing`** -- the DVs cannot in principle discriminate the mechanism from its
  degenerate look-alike, whatever the substrate does; they need redesign. (Favoured for 151:
  even a healthy ContextMemory leaves `action_bias_divergence` guaranteed by the objective.)

## 8. Learning extracted

1. **A ratio-valued DV needs a ratio-valued readiness floor.** 936's P3 stated the starvation
   hazard verbatim and then guarded it in absolute units. This is a general, cheap, reusable
   check for `/queue-experiment`.
2. **A bounded statistic over an unbounded quantity is not a measurement.** `f_variance_share`
   is in [0,1] by construction and therefore *looks* well-behaved at 1.0; the pathology is
   invisible in the DV and visible only in the magnitudes the manifest did not record.
3. **Record one scale anchor per run.** A single `||z_world||` or raw score range in the manifest
   converts a multi-hour forensic back-solve into a first-read observation, and would have caught
   this on 936, and plausibly on several of the other 19 clamp-less drivers.
4. **A default-OFF guard is adoption-dependent.** SD-056's lever (b) is correct, validated, and
   the settled convention (97 of 117 drivers) -- and still absent from the most recent run in the
   lineage it was built for, in a module that declares parity with a driver that arms it.
   "Parity with X" in a baseline module needs mechanical checking, not a comment.
5. **A bare sign test on 3 seeds has a 50% null false-positive rate.** MECH-151's only support
   entry rests on one, with no effect-size margin. Standing practice already requires a
   delta-SD-scaled gate plus an absolute floor.
6. **"The DV moved" is not evidence when the training objective moves it.** 922 regressed
   `action_bias` onto a z_world-derived target and then measured whether `action_bias` varies
   with z_world. This is the DV-symmetry failure class, arriving one layer upstream of where
   `/queue-experiment`'s existing check looks.
7. **An unapplied withdrawal decays into a positive claim.** MECH-151's `live_status` is its
   first-ever evidence entry and reads `supports`; left alone it hardens. Recorded in
   `per_claim_recommendation` so GOV-APPLY-1 can see it.

## 9. Routing (Step 8 gate cleared 2026-08-18)

### Target 1 -- V3-EXQ-936 / MECH-439

- **`recommended_evidence_direction`: `non_contributory`** (manifest currently `weakens` --
  governance should change it). C2 was not evaluated; the falsifier never fired either way.
- **`recommended_epistemic_category`: `standard`.** Deliberately **not** `substrate_ceiling`.
  MECH-439 carries 9 counted ceiling hits under R1-R3; adding a 10th for a run that measured
  nothing is exactly the inversion R3 exists to prevent (a broken instrument is not evidence of a
  ceiling). `standard` also preserves current GOV-GRAN-1 and v3-testability behaviour.
- **Routing: `queue-experiment`** -- V3-EXQ-**936a**, same question, alphabetic suffix. Two
  changes only: (a) restore 689i clamp parity
  (`e2_rollout_output_norm_clamp_enabled=True, ratio=2.0`) in the baseline module's
  `CONFIG_FLAGS`; (b) **record** a rollout scale anchor per cell (mean/max `||z_world||` and raw
  E3 score range) per the Experimental Recording Standard, plus a **relative** P3 floor
  (`var_nonF / var_F >= <pre-registered epsilon>`, epsilon comfortably above float32 eps).
- **Re-derive brake: FIRED (10th-order for MECH-439) but EXEMPT, user-confirmed at the Step 8
  gate.** The brake refuses another letter circling the *same* ceiling against the *same*
  substrate. 936a runs against a materially changed config in which an identified,
  instrument-destroying defect is repaired -- so it is the first *measurable* instance of this
  DV, not a re-pose. Stated explicitly here because it is a judgement call, and the user made it.
- **Substrate entry: `amend` SD-056** -- `severity: corrupting`, `substrate_paths`
  `ree_core/predictors/e2_fast.py::rollout_with_world` + `ree_core/utils/config.py` +
  `ree_core/predictors/e3_selector.py::compute_reality_cost`; new `failure_record` item for 936;
  `implementation_hint` = add a WARN-only corpus lint
  `validate_experiments.py --checks sd056_training_without_rollout_clamp` flagging any driver
  that calls `world_forward_contrastive_loss` with no reachable
  `e2_rollout_output_norm_clamp_enabled`, matching the repo's existing advisory-lint pattern
  (20 hits today, 5 of them legitimately pre-amend).
- **Config default NOT flipped** (user-confirmed): flipping `e2_rollout_output_norm_clamp_enabled`
  to `True` would change bit-identity for every run relying on the default, including completed
  runs being reproduced. Registered as a separate question for governance, not done here.
- **Biology divergence -> `/lit-pull` commission** (secondary): no targeted review covers
  normalisation / divisive gain control over competing value channels in E3-analogous
  selection. The absence of any score normalisation is a formal-import divergence and is
  load-bearing by default (SD-003 is the canonical cost of treating one as a caveat).

### Target 2 -- GFLAG-0039 / MECH-151

- **`recommended_evidence_direction`: `non_contributory`** for MECH-151 (**supersedes**, per R2,
  the `supports` in `failure_autopsy_V3-EXQ-922_2026-08-13`; this is a re-adjudication of the
  same run, not a second hit).
- **`recommended_epistemic_category`: `standard`** (unchanged). **Status stays `candidate`**;
  `pending_retest_after_substrate` stays `true`.
- **`live_status` should be withdrawn** from `supports -- narrow context-conditioning mechanism
  confirmed (V3-EXQ-922, 2/3 seeds)` to a non-contributory reading. This is **not** a demotion:
  the demotion bar (tested fairly + biology supports + still fails) is not met, because the claim
  was not tested fairly.
- **Routing: `queue-experiment`** -- the corrected design already exists at
  `evidence/planning/mech151_affordance_set_instrumentation_design_blocked_20260818.md` Section 4
  (paired ON/OFF `action_bias` ablation at matched state, measuring *selection authority* rather
  than bias norm). Two additions from this autopsy: an `n_occupied_slots >= 2` readiness
  precondition **and** a `sd016_writepath_mode != "off"` precondition (Section 5c -- the existing
  design doc names the first but not the second, and 922 shows the second is the one that
  actually bit).
- **Secondary, for governance to adjudicate rather than this autopsy:** GFLAG-0043's ARC-007
  contradiction. MECH-151 needs a ranking site; ARC-007 STRICT forbids one in `_score_trajectory`;
  `e3_selector.py` has no action-object channel. That is a **framing** problem
  (`complex (probe-gated) / mystery (known data)` -- the data is in hand and the frame is wrong),
  which points at `/claim-synthesis` reframing rather than at any experiment. Recorded, not
  routed, because the user's Step 8 answer scoped this autopsy's recommendation to the
  `live_status` withdrawal.
- **GFLAG-0039 and GFLAG-0043 should both be resolved** by governance once the withdrawal is
  applied, with the Section 5c correction noted (write path off, not 1-of-16 occupancy).
- **Flagged, not adjudicated:** MECH-150's C1 entropy criterion is aliased (Section 5d). Its
  adjudication belongs to a re-reading of `failure_autopsy_V3-EXQ-922_2026-08-13`, which this
  autopsy does not perform.

## 10. Granularity-debt recurrence trigger

**MECH-439: DOES NOT FIRE.** `granularity_debt_cluster.py MECH-439` reports **16 targets across
14 files**, alignment distribution `intact=8, unclear=4, other=2, n/a=1, strengthened=1` --
**zero targets read `weakened`**. Per the standing rule, a cluster with no `weakened` target is
measurement or implementation debt, not granularity debt, however many autopsies exist. The count
alone would have fired it; the distribution is what refuses it, and that distribution is itself
the finding: MECH-439 has been autopsied 16 times and never once fairly tested.

**MECH-151: DOES NOT FIRE.** 1 target across 1 file
(`failure_autopsy_V3-EXQ-922_2026-08-13`, alignment `other`), 0 ceiling hits. This autopsy is the
second reading of that *same* run, which under R2 supersedes rather than adds -- so it does not
make MECH-151 a two-autopsy recurrence either.

## 11. Re-derive brake counts (R1-R3, recomputed 2026-08-18)

- **MECH-439: 9** ceiling hits -- 689a, 700, 700a, 700b, 700c, 700d, 709, 711, 713. Unchanged by
  this autopsy (recommends `standard`).
- **MECH-151: 0** ceiling hits.
