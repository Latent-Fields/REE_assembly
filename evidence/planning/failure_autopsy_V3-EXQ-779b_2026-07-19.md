# Failure Autopsy — V3-EXQ-779b (MECH-063 sub-claim ii, tonic/phasic dissociation)

- **generated_utc**: 2026-07-19T10:52:50Z
- **run_id**: `v3_exq_779b_mech063_tonic_phasic_dissociation_20260718T233554Z_v3`
- **queue_id**: V3-EXQ-779b · **supersedes** `v3_exq_779a_mech063_tonic_phasic_dissociation`
- **claim**: MECH-063 sub-claim (ii) · **outcome**: FAIL · **self-route**: `sample_starvation_requeue`
- **substrate_hash**: `849de508bf4f4e44e6b612271f48fd590385957843481e7c6bf63706a85e538b` · machine_class `linux-x86_64-py3.10` · elapsed 8897 s
- **scope**: single · **status**: confirmed (user gate 2026-07-19)

## Headline

779b was a one-parameter exposure fix for 779a. **The fix took effect and the result did not move.** The
starvation hypothesis is refuted. But the reading that follows is *not* that the gate is spurious — it is
that **the gate is correctly flagging the result's single point of failure.**

779b books **no experimental support** for MECH-063. The claim stays lit-only (exp_conf 0.0).

## 1. Facts — the fix reached the cell

| | 779a | 779b |
|---|---|---|
| T1P1/seed23 `n_env_steps` | 835 | **2400** |
| `rollout_stop_reason` | `episode_cap` | **`step_cap`** |
| `rollout_episode_cap_can_bind` | (absent) | **False** |
| T1P1/seed23 `n_event_ticks` | 6 | **13** |

`MAX_EPISODES_PER_CELL = MAX_ENV_STEPS_PER_CELL` with the module-level assert (script:292-295) holds, and
`episode_cap_can_bind` is False in all 20 cells. **This is a science result, not an instrumentation bug.**

The targeted cell responded (6 → 13, near the predicted ~17). The reported MIN stayed 6 because it
**migrated**: T0P1/seed23 went 10 → 6 while its exposure nearly tripled.

## 2. Why exposure cannot move it — episode length, not step count

Mean episode length (779b): seed 23 = **6.9 steps**; seeds 11/17 = 48–66; seeds 29/37 = **300** (the cap).
A 43× spread.

`PhasicSurpriseBurst.reset()` clears the surprise-EMA **cold at every episode boundary**, and the first
waking tick of each episode can never fire an event (it seeds the baseline). With
`PHASIC_EMA_DECAY = 0.1` the baseline has a **~10-tick time constant — longer than seed 23's entire
episode**. Seed 23 burns ~1 of every ~7 ticks re-seeding and never runs against a converged baseline.

779b delivered seed 23's 2400 steps as **345 episodes of 7**, not as longer episodes. Exposure was added
on an axis **orthogonal to the binding constraint**. No further step-budget increase can help.

## 3. The gate is load-bearing — leave-one-out

`diss_seed_count` = 4 at `MIN_SEEDS` = 4: the verdict passes at **exactly the floor**.

| dropped seed | dissociating | threshold | verdict |
|---|---|---|---|
| none | 4/5 | 4 | **True** |
| 11 | 3/4 | 4 | False |
| 17 | 4/4 | 4 | True |
| **23** | **3/4** | 4 | **False** |
| 29 | 3/4 | 4 | False |
| 37 | 3/4 | 4 | False |

**The gate flags seed 23; the verdict depends on seed 23.** The withholding is correct.

(The prior autopsy's own ledger basis already recorded this — "excluding it leaves 3 < min_seeds 4" — and
then exempted the brake on an exposure theory that 779b has now falsified.)

## 4. The anti-correlation, and why it is not the exculpating evidence it looks like

| seed | mean ticks | dR_phasic | C2 | dissociates |
|---|---|---|---|---|
| 23 | **9.5** (fewest) | **−0.110** (strongest) | ✓ | ✓ |
| 29 | 25.5 | −0.092 | ✓ | ✓ |
| 37 | 35.0 | −0.040 | ✓ | ✓ |
| 11 | 85.0 | −0.027 | ✓ | ✓ |
| 17 | 58.0 | **−0.011** | ✗ | ✗ |

Spearman ρ(ticks, |dR_phasic|) = **−0.90** (n=5). This *looks* like "the gate measures the wrong thing."

It is at least as well explained by **small-sample effect-size inflation**: fewer ticks → noisier,
magnitude-inflated |dR|. Seed 23's −0.110 on ~9.5 ticks is precisely the estimate a ≥10-tick floor exists
to exclude — and the verdict rests on it. **With n=5 the data cannot discriminate the two readings.** Any
argument from seed 23's effect size presupposes the effect is real, which is the thing in question.

## 5. Robustness bar — already retired as defective

`robust: true` was computed with the **mean-minus-population-SD** idiom that MECH-063 autopsy follow-up #4
retired (`ree-v3` `de09887093`, `_lib/robustness_bars.py`).

| leg | \|mean\| | SEM | margin | k=1 | k=2 | retired pstdev bar |
|---|---|---|---|---|---|---|
| dS_tonic | 0.2681 | 0.0394 | 0.05 | +0.2287 ✓ | +0.1893 ✓ | ✓ |
| dR_phasic | 0.0561 | 0.0191 | 0.02 | +0.0370 ✓ | **+0.0179 ✗** | ✓ |

The **phasic leg — which is the sub-claim** — fails the corrected bar at k=2. The tonic leg is solid.

## 6. Two precondition-schema defects found by parallel sessions — both adjudication-inert here

1. **Two-sided bound** (`REE_assembly` `e8f736d405`, `ree-v3` `6e595c99bc`): `baseline_entropy_headroom`
   declared `direction: "upper"` but its check is `E_SAT_LOW < S < E_SAT_HIGH`; the 0.02 floor leg was
   unrepresentable. Now emits the strict interval.
2. **mean-vs-all** (`ree-v3` `42b38c800a`): `measured` reports a MEAN while `met` resolves an `all()`.
   Corpus fire rate 5/1136 scripts — **all of them the MECH-063 lineage** (777/777a/779/779a/779b), a full
   true-positive set. Not retro-edited (user decision: changing `measured` alters pre-registered reporting
   on a completed lineage).

**Neither changes 779b's adjudication.** All five T0P0 baselines sit well inside the band (0.145–0.609),
`all()` is True, and the other session's replay over 1553 precondition entries produced 0 diffs. Their
value was **directing attention to seed 23**, which is what reopened this autopsy.

## 7. Environment adequacy — a real finding, logged not routed

Baseline entropy is **highest** on seed 23 (0.609), and its tonic-ON arms reach **0.849 / 0.859** — within
0.12 of `E_SAT_HIGH` = 0.98. Seed 23 is the **least** converged seed, terminating in ~7 steps with a
near-uniform policy (failing fast, not solving fast).

Two consequences:
- **R5 checks T0P0 baseline rows only.** It guarantees baseline headroom but **never checks whether the
  treatment arms saturate.** Seed 23's tonic-ON arms are an unguarded near-ceiling exposure on the same seed.
- **Episode length spans 7 → 300 steps (43×) across seeds.** The seeds are arguably not sampling one task
  distribution. Logged as an environment-adequacy finding per the user gate; not separately queued.

## 8. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | the probe cannot yet let sub-claim (ii) express itself on short-episode seeds |
| Biological reference | **clear** | LC-NE tonic/phasic mode-switching (Aston-Jones & Cohen). Faithful class translation, not a formal import; no lit commission owed |
| Prerequisites | **present** | SD-069 IMPLEMENTED; `burst_level_max` = 1.00 in every PHASIC-ON cell |
| Implementation | **partial** | SD-069 fires correctly; its **per-episode cold EMA reset** is incompatible with short-episode rollouts |
| Environment | **wrong pressures** | 43× episode-length spread; seed 23 near entropy ceiling in treatment arms |
| Measurement | **under-instrumented** | MIN-across-cells gate on a high-variance statistic; `MIN_SEEDS` passing at exactly the floor; retired robustness bar |
| Integration | **partially coupled** | regulator ↔ rollout-length interaction is the defect; neither component is wrong alone |
| Scale / capacity | **likely insufficient** | corrected SEM bar on the phasic leg needs more informative seeds |

**Recommended `epistemic_category`: `substrate_ceiling`** on a **named** upstream.
**Recommended `evidence_direction`: `non_contributory`** · `pending_retest_after_substrate: true`.

## 9. Re-derive brake — FIRES, both halves

Third MECH-063 autopsy reaching the bar. The 779a exemption was granted on the explicit predicate that the
one-parameter exposure fix would work and that the criterion "passed non-degenerately and robustly."
**Both halves of that predicate are now falsified** (§1, §3, §5). The exemption is **not inherited.**

- `refused_requeue: true` — **a V3-EXQ-779c is REFUSED.** No further lettered iteration of the tonic/phasic
  probe against the current regulator. A redesign of a *different* mechanism under a new EXQ number remains permitted.
- `route_to: implement-substrate`, `upstream_substrate: sd_phasic_ema_episode_continuity`.

Correction to an intermediate reading in this session: the routing half **does** apply. The diagnosis is a
named buildable substrate defect, not a bare measurement complaint.

**GOV-FANOUT-1: exempt.** The bottleneck routes to a single unambiguous build. The H-A/H-B discrimination
(§4) is not fannable until the regulator can produce a converged baseline on short-episode seeds — the
build must precede the portfolio.

## 10. Granularity-debt trigger

Fires on count (3rd autopsy on MECH-063) but is **assessed as NOT indicating granularity debt**: sub-claims
(i) and (ii) are already separated and already route differently (777 lineage → SD-074/PROBE-WARMUP;
779 lineage → this entry). The recurrence reflects one probe family repeatedly hitting substrate
limits, not a coarse claim. Recorded honestly for the GOV-GRAN-1 standing scan.

## 11. Learning extracted

1. **A per-episode cold EMA reset makes an event-rate readout a function of episode length.** Any
   surprise-baseline regulator reset at episode boundaries silently under-reports on short-episode seeds;
   more total steps cannot compensate, because they arrive as more cold restarts.
2. **A MIN-across-cells precondition on a high-variance statistic is a noise draw**, and the cell it
   selects is by construction the least reliable one.
3. **`MIN_SEEDS` passing at exactly the floor should be reported as fragile.** Leave-one-out collapsed
   4 of 5 seeds here; that fragility was invisible in the PASS flag.
4. **An effect size measured on few samples cannot be used to argue that few samples suffice.** The
   inference is circular; it needs an independent reliability estimate.
5. **A saturation-headroom precondition checked only on baseline arms does not protect the treatment arms.**
6. Recording note: the always-core is complete (`substrate_hash`, `config`, `seeds`, `machine_class`,
   `elapsed_seconds` all present). **No recording debt.** The script carries **no
   `=== HYPOTHESES UNDER TEST ===` / `=== INTERPRETATION GRID ===` block**, contrary to the skill's
   requirement for diagnostics — a template-compliance gap for successor authors.

## 12. Draft `evidence_quality_note` for governance (do NOT apply here)

> V3-EXQ-779b (MECH-063 sub-claim ii) — non_contributory, substrate_ceiling. The 779a episode-cap fix
> verifiably took effect (seed 23 / T1P1: 835 → 2400 env steps, stop_reason episode_cap → step_cap,
> episode_cap_can_bind False) and the precondition did not move: phasic_fires_real_events measured 6 vs
> threshold 10, the MIN having migrated from T1P1/seed23 (6 → 13) to T0P1/seed23 (10 → 6). Root cause is
> NOT exposure and NOT SD-069 capability (burst_level_max = 1.00 in every PHASIC-ON cell): the phasic
> regulator resets its surprise-EMA cold at each episode boundary with a ~10-tick time constant, while
> seed 23's episodes last ~6.9 steps, so its baseline never converges and added steps arrive as more cold
> restarts. The withholding is CORRECT rather than spurious: diss_seed_count 4 sits at exactly MIN_SEEDS 4
> and leave-one-out collapses the verdict for 4 of 5 seeds INCLUDING seed 23, so the load-bearing criterion
> depends on the very cell the gate flags; seed 23's dR_phasic −0.110 on ~9.5 event ticks is equally well
> read as small-sample effect-size inflation, and n=5 cannot discriminate. Separately, `robust: true` used
> the mean-minus-population-SD idiom retired by MECH-063 autopsy follow-up #4; under the corrected SEM bar
> the phasic leg fails at k=2 (+0.0179 vs margin 0.02) while the tonic leg passes. Booked as
> pending_retest_after_substrate against sd_phasic_ema_episode_continuity. MECH-063 remains lit-only
> (exp_conf 0.0); no demotion — the probe has not yet let the claim express itself.

## 13. Routing

**`implement-substrate`** → `sd_phasic_ema_episode_continuity` (substrate_queue `action: create`,
priority 1). Re-derive brake fired, both halves. V3-EXQ-779c refused.
