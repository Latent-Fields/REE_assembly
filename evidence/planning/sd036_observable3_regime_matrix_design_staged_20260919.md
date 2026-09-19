# SD-036 observable #3 -- shared harm-stream regime matrix: staged design + four open decisions

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml, experiment_queue.json, substrate_queue.json, or any other registry. NO experiment was queued and NO experiment script was written.**

- Session: `metaworker-science-20260919-sd036-observable3-regime-matrix` (headless, ree-cloud-4)
- Chip: `chip-20260919-sd036-observable3-regime-matrix`; campaign `science-20260919-sd036-observable3-regime-matrix`
- Written 2026-09-19T22:28Z against `ree-v3` origin/main `2be3c89a` and `REE_assembly` origin/master `4180b198f8`
- User consent this executes (2026-09-19T22:12:50Z, orchestrate-20260919-2125 campaign lane):
  *"DISPATCH WITH CONSENT MID-FLIGHT. Draft the design against the V3-EXQ-854 harness and the
  SD-036 / SD-011 claim texts, then STOP and raise ONE kind:decision chip laying out the four
  un-written choices ... Queue NOTHING before that chip is answered."*
- Kind: **design draft + decision brief**. No `ree_core` edit, no queue append, no claims.yaml edit.

---

## 0. STOP-CHECK (run 2026-09-19T22:22Z, all four clauses)

- `experiment_queue.json` on `origin/main`: **0 items**. No SD-036 / gaba / regime-matrix entry.
- `origin/main experiments/`: SD-036 drivers are `v3_exq_475_*`, `v3_exq_475a_*`,
  `v3_exq_854_sd036_gaba_tone_dose_response.py`, plus `_lib/baselines/sd036_decay.py`.
  **No regime-matrix successor exists.**
- `origin/master evidence/experiments/`: the only landed SD-036 manifests are the EXQ-475 run and
  `v3_exq_854_sd036_gaba_tone_dose_response_20260801T062503Z_v3` (PASS / supports).
- Chip fresh-read: `status: open`, `claimed_by: null` at claim time. Claimed under this session's uuid.
- `task_claim.py check`: `ree-v3/experiment_queue.json` + `ree-v3/experiments` are **owned by a
  sibling session** (`metaworker-science-20260919-arc029-p1p3-retest`, 22:20:51Z; also
  `...-mech204-541d-guard-validation`). Because this pass queues nothing, the claim opened here was
  narrowed to **this file's path only**, which had no overlap. The queue resources were deliberately
  NOT claimed -- see section 8.

Everything matched the scout's expectation. Nothing was already done.

---

## 1. One-paragraph answer

The design is buildable and the base harness (V3-EXQ-854) is closer to fit-for-purpose than the
pre-flight suggests -- it already runs `harm_history_len=10` **and** `limb_damage_enabled=True`,
which is the *non-vacuous* SD-011 regime, not the legacy rank-2 one. But the four decisions cannot
be answered as posed, because **the pre-flight's central empirical premise is wrong**. It describes
observable #3's problem as a 70x spread asymmetry between `z_harm` (1.4e-03) and `z_harm_a`
(1.0e-01) that makes a bare sign test "close to a coin flip". The landed V3-EXQ-854 manifest says
something different and worse: across the registered 5-tone sweep, **only one of the three streams
responds to `gaba_tone` at all**. Per-seed Spearman rho of sustain ratio against tone is
**-1.00 / -1.00 / -1.00 for `z_harm_a`**, **+0.10 / +0.70 / -0.50 for `z_harm`**, and
**+0.60 / +0.20 / -0.10 for `z_beta`** -- i.e. the two non-primary streams have no tone ordering
whatsoever, with mean rho pointing the *wrong* way. `1.4e-03` is **`z_beta`'s** sweep spread, not
`z_harm`'s; `z_harm`'s is 4.8e-02 to 1.5e-01, 30-110x larger than the claim text states, and
entirely unordered. Consequently D1 (a magnitude bar) does not rescue the conjunction -- it makes it
fail harder -- and D2 (tau-ordering) is mechanistically ill-posed against this substrate, whose own
composition law makes effect magnitude a function of `alpha` at least as much as `tau`. The
decision owed is therefore prior to and larger than the four as written: **is observable #3
scoreable at all on `sustain_ratio` as the per-stream DV, given that one stream's DV is at ceiling
and another's is noise-dominated?** Running it unchanged would record a FALSIFICATION of SD-036's
sole architectural commitment that is substantially a DV-validity artifact.

---

## 2. Measured facts, computed this session from the landed manifest

Source: `REE_assembly/evidence/experiments/v3_exq_854_sd036_gaba_tone_dose_response_20260801T062503Z_v3.json`
(`outcome: PASS`, `evidence_direction: supports`, `non_degenerate: true`), ON arm (`decay_on`),
trained agents, `EVAL_STEPS=300`, seeds 42/43/44, registered sweep `[0.3, 0.5, 1.0, 1.5, 2.0]`.

### 2a. Per-stream dose-response across the full sweep

Spearman rho(`gaba_tone`, `sustain_ratio`). C1's registered bar is rho <= -0.9.

| stream | tau | seed 42 | seed 43 | seed 44 | mean | verdict |
|---|---|---|---|---|---|---|
| `z_harm_a` | 0.02 | -1.00 | -1.00 | -1.00 | **-1.00** | clean monotone decrease |
| `z_harm`   | 0.05 | +0.10 | +0.70 | -0.50 | **+0.10** | **no tone ordering** |
| `z_beta`   | 0.03 | +0.60 | +0.20 | -0.10 | **+0.23** | **no tone ordering** |

### 2b. Sweep spread per stream (the quantity precondition (i) gates on, floor 1e-3)

| stream | seed 42 | seed 43 | seed 44 | relative |
|---|---|---|---|---|
| `z_harm_a` | 1.13e-01 | 9.89e-02 | 1.02e-01 | ~10-12% |
| `z_harm`   | 4.84e-02 | 5.72e-02 | 1.54e-01 | ~6-19% |
| `z_beta`   | 1.62e-03 | 1.39e-03 | 1.43e-03 | ~0.14-0.16% |

**The `1.4e-03` figure quoted in SD-036's precondition (iii) and in the driver docstring as
`z_harm`'s spread is `z_beta`'s.** `z_harm`'s spread is 30-110x larger than stated, and unordered.
This is a `stale_note`-class correction in its own right (section 5).

### 2c. The 0.3-vs-2.0 contrast that C2 actually scores

Relative effect `(lo(0.3) - hi(2.0)) / hi(2.0)`. Positive = the direction C2 requires.

| stream | seed 42 | seed 43 | seed 44 |
|---|---|---|---|
| `z_harm_a` | +13.15% | +11.34% | +11.70% |
| `z_harm`   | **-1.59%** | **-5.69%** | +0.15% |
| `z_beta`   | **-0.0099%** | +0.0286% | +0.0289% |

Note the shape of the `z_harm` failures: seed 43's wrong-direction move (-5.69%) is **38x larger**
than seed 44's correct-direction move (+0.15%). This is not an underpowered test of a small effect;
it is a large-magnitude effect with no stable sign. A magnitude bar makes it fail harder.

And `z_beta`'s effects are order 1e-4 relative -- roughly **400x smaller** than `z_harm_a`'s.

### 2d. Why `z_beta` is inert: its DV is at ceiling, and its readiness was never tested

`z_beta`'s sustain ratio sits at **0.9896-0.9923 across every tone and every seed** -- a nearly flat
trajectory, whose mean/peak is pinned near 1 regardless of the pole. The DV has ~0.15% of dynamic
range in which to express anything.

This is not because the regulator skips `z_beta`. It does decay it
(`ree_core/regulators/gabaergic_decay.py:238-242`, `decay_z_beta=True`, `tau_z_beta=0.03`), and
`z_beta` does carry temporal state (`ree_core/latent/stack.py:1594`,
`alpha_shared = 0.3`, so 70% of the previous value persists). The pole is comparable to
`z_harm_a`'s. **The DV, not the mechanism, is what cannot resolve it.**

Critically: V3-EXQ-854's readiness control (`readiness_control()`, driver :232-255) measures the
spread of **`harm_a` only**. `z_beta` and `z_harm` were **never subjected to the
`READINESS_SPREAD_FLOOR = 1e-3` gate that SD-036 precondition (i) requires of "EVERY stream it
scores"**. `z_beta`'s measured spread (1.39e-03) clears that floor by 39%, which is not a margin
anyone should score a claim's sole architectural commitment on.

### 2e. Why the tau-ordering clause is ill-posed against this substrate

The composed pole is `(1 - alpha_s) * exp(-tau_s * gaba_tone)` (driver docstring; blend at
`stack.py:1655-1670`). Registered values:

| stream | tau | alpha | retained fraction `(1-alpha)` | pole at tone 0.3 -> 2.0 |
|---|---|---|---|---|
| `z_harm_s` | 0.05 | 0.5 | 0.5 | 0.4926 -> 0.4524 |
| `z_harm_a` | 0.02 | 0.2 | 0.8 | 0.7952 -> 0.7686 |
| `z_beta`   | 0.03 | 0.3 (`alpha_shared`) | 0.7 | 0.6969 -> 0.6592 |

Sustain-ratio sensitivity to the pole is strongly nonlinear and grows as the pole approaches 1.
Expressed as a memory time constant `-1/ln(pole)`, the sweep moves `z_harm_a` by ~0.56 steps
(4.36 -> 3.80) but `z_harm_s` by only ~0.15 steps (1.41 -> 1.26). **The substrate therefore predicts
the largest sustain-ratio effect on the stream with the SMALLEST tau**, which is exactly what was
measured -- and is the reverse of what "effect magnitudes ordered by their registered taus" would
score as CONFIRMING.

So SD-036's CONFIRMING clause, read literally, predicts an ordering its own substrate contradicts by
construction. Scoring it as written would register a FALSIFICATION of the claim that is really a
falsification of the claim's own magnitude-ordering prediction. `alpha` is not mentioned anywhere in
SD-036's `what_would_answer`.

---

## 3. What the existing data already implies about observable #3

SD-036's FALSIFYING clause, verbatim: *"at gaba_tone=0.3 the three streams degrade INDEPENDENTLY --
one or two respond while the others do not, or the magnitudes do not track the registered taus, or
the cluster can be reproduced by decaying any single stream in isolation."*

On the landed V3-EXQ-854 data, **two of those three disjuncts are already satisfied**: one stream
responds and two do not (2a), and the magnitudes do not track the registered taus (2e). The third
(single-stream isolation) has never been tested.

**This does not license recording a falsification, and the reason is SD-036's own precondition (i).**
That precondition exists to stop a stream being scored where the instrument cannot register an
effect, and it was applied to only one of the three streams. On the two streams that "do not
respond":

- `z_beta` -- DV at ceiling, dynamic range 0.15%, readiness never tested. **Vacuous, not falsifying.**
- `z_harm` -- large but unordered variance (up to 0.154 spread at rho ~ 0), i.e. the trajectory is
  dominated by behaviour and environment rather than by the regulator, at n=3 seeds. **Underpowered,
  not falsifying.**

Reporting either as a `weakens` would be the mirror image of the "confident-but-wrong confirmation"
that precondition (i) was written to prevent: a confident-but-wrong *refutation*. SD-011's clause (i)
sets the precedent for the correct handling -- a run that cannot express the effect "must be
reported as such rather than as a weakens."

---

## 4. The design, as far as it can be specified without the decisions

Everything in this section is already ratified by the chip, the claim texts, or the base harness,
and is stated so the decisions in section 6 are the only open items.

### 4a. Base harness and what it already gives us

`ree-v3/experiments/v3_exq_854_sd036_gaba_tone_dose_response.py` + `_lib/baselines/sd036_decay.py`.
Verified live at `2be3c89a`:

- Registered sweep `TONE_SWEEP = [0.3, 0.5, 1.0, 1.5, 2.0]` -- includes both tones CONFIRMING and
  FALSIFYING compare.
- Control arm `use_gabaergic_decay=False` (`ARM_OFF = decay_off_legacy`), **not** `gaba_tone=0.0`.
  Precondition (ii) satisfied.
- All three sustain ratios already computed per tone (`harm_sustain_ratio`,
  `harm_a_sustain_ratio`, `beta_sustain_ratio`) plus full trajectories banked.
- `use_pag_freeze_gate=False` throughout -- the de-confounding convention SD-036 names.
- Encoder floor measured every run (`B.encoder_floor_norms`), relative DVs only. Preconditions
  (ii)/(iv) satisfied.
- Readiness gate `READINESS_SPREAD_FLOOR = 1e-3` and vacuity ceiling `1e-5` implemented -- **but on
  `harm_a` only** (the gap in 2d).
- **`harm_history_len = 10`** (`_lib/baselines/sd036_decay.py:93,118`) -- SD-011 precondition (i)
  **already satisfied**. The 854 lineage is *not* one of the vacuous `harm_history_len=0` runs.
- **`limb_damage_enabled = True`** (`sd036_decay.py:94`) -- the **SD-022 body path**, rank 4 free /
  5 numerical, **not** the legacy rank-2 proximity path. See section 5 correction 3.
- Cost: 2 arms x 3 seeds x 80 train episodes x 200 steps, plus 5 frozen tone evals x 300 steps, plus
  the readiness tape. The 854 run's recorded `elapsed_seconds` is the calibration point for any
  successor; adding isolation arms multiplies the ON-arm cell count.

### 4b. Arms, as ratified

| arm | levers | purpose |
|---|---|---|
| `decay_off_legacy` | `use_gabaergic_decay=False`, `gaba_recurrence_z_harm_s/_a=False` | control (precondition (ii)) |
| `decay_on` | `use_gabaergic_decay=True`, swept over `TONE_SWEEP` | observable #3 primary |
| isolation arms | `gaba_recurrence_z_harm_s` / `_a` toggled independently | FALSIFYING's 3rd disjunct -- **D3** |
| SD-011 leg | `harm_history_len=10` (already default in lib), sourcing stated | `stream_corr`, `autocorr_gap`, `harm_fwd_r2`, D3 direction |
| MECH-279 leg | `pag_n_commits` at `theta_freeze` 2.0 and 0.8, gate ON **only here** | MECH-279's outstanding question |

### 4c. Tagging

`CLAIM_IDS = ["SD-036", "SD-011", "MECH-279"]`; `EXPERIMENT_PURPOSE = "evidence"`;
`architecture_epoch = "ree_hybrid_guardrails_v1"`; `run_id` ends `_v3`;
`machine_affinity: "any"`. Next free queue id at write time is **V3-EXQ-1068** (1065/1066/1067 are
in flight under sibling campaign claims; highest landed script `v3_exq_1064_*`) -- re-read at write
time, do not trust this line later.

### 4d. Scored and excluded, to be stated in the docstring and manifest

- **Scored: observable #3 only.**
- Observable #1 -- WITHDRAWN AS WORDED, permanently. Not re-registered. (Encoder floor ~0.509
  exceeds the 471-lineage avoid threshold 0.25.)
- Observable #2 -- discharged by V3-EXQ-854 (C1 rho -1.0, 3/3). Not re-run.
- Observable #4 -- belongs to MECH-279, ran as V3-EXQ-776. Not scored here.
- MECH-258 -- **PARKED** by user decision 2026-09-08. Not attached.
- SD-036 does **not** undercut MECH-279: `agent.py` passes `gaba_tone` to `PAGFreezeGate.tick()` as a
  direct scalar (`exit_threshold = theta_freeze * gaba_tone`), never through the decay path.

### 4e. Readiness gate, as it must be extended regardless of the decisions

Precondition (i) requires a non-zero sweep spread on **every stream scored**. The 854 readiness
control tests `harm_a` only. Any successor must run the fixed-tape readiness sweep **per stream**
and report `z_harm` and `z_beta` spreads against the floor, routing a below-floor stream to
`substrate_not_ready` / vacuous **for that stream** rather than to a `weakens`. This is not a
decision -- it is the precondition applied as written -- but it is the mechanism by which the
answers to D1/D2 become consequential.

---

## 5. Corrections owed to /governance (stale_note class), independent of any decision

1. **SD-036 says observable #3 was "NEVER RUN. This is the live falsifier and the whole content of
   the claim." It has been run.** V3-EXQ-854 carries `C2_multi_stream_cluster`,
   `load_bearing: false`, which **failed** (1 of 3 seeds passing: seed 42 z_harm F / z_harm_a T /
   z_beta F; seed 43 F/T/T; seed 44 T/T/T), inside a run recorded `PASS` / `supports`.
2. **SD-036 precondition (iii) misattributes the `1.4e-03` spread to `z_harm`.** It is `z_beta`'s.
   `z_harm`'s sweep spread is 4.84e-02 / 5.72e-02 / 1.54e-01 -- 30-110x larger, and unordered
   (rho +0.10 mean). The sentence "The z_harm effect is real but modest (1.4e-03) beside z_harm_a
   (1.0e-01)" is wrong in both the number and the characterisation: `z_harm`'s effect is not modest,
   it is absent-but-noisy.
3. **The pre-flight's D4 premise is wrong about the harness.** It states the SD-011 leg would run on
   "the LEGACY default path ... numerical rank 2" and thereby reproduce the rank-2 construct-validity
   problem. The 854 harness explicitly sets `limb_damage_enabled=True` and `harm_history_len=10`
   (`_lib/baselines/sd036_decay.py:93-94,118`), i.e. the **SD-022 body path in the regime SD-011's
   preconditions (i) and (iii) ask for**. D4's first half is therefore largely already answered by
   the base harness; what is owed is that the mode be **stated**, not chosen.
4. **SD-036's CONFIRMING clause omits `alpha`.** The composed pole is `(1-alpha)*exp(-tau*tone)`, so
   effect-magnitude ordering is governed by `alpha` at least as much as by `tau` (section 2e). As
   written, the tau-ordering test predicts an ordering the substrate contradicts by construction.

These are reported here and in the chip resolution note; **nothing was written to claims.yaml.**

---

## 6. The four decisions, re-framed against what was measured

Each gives options, what each would measure, and a recommendation with its reason. **None was
acted on.**

### D0 (PRIOR, and it subsumes D1) -- is observable #3 scoreable on `sustain_ratio` at all?

The pre-flight did not ask this because it believed all three streams responded, one weakly. They do
not (2a). Before a magnitude bar can be set, the run has to decide what to do about a stream whose
DV is at ceiling and a stream whose DV is noise-dominated.

- **Option A -- extend the per-stream readiness gate, and let it disqualify streams.** Run the
  fixed-tape readiness sweep on all three streams; any stream below `READINESS_SPREAD_FLOOR`, or
  whose DV range is at ceiling, is reported **vacuous for that stream** and observable #3 is recorded
  as **not scoreable at n=3 on this DV** rather than as confirmed or falsified. Measures: whether the
  instrument can see the effect, before asking whether the effect is there.
- **Option B -- change the per-stream DV to one with dynamic range.** Keep `sustain_ratio` for
  `z_harm_a` (where it works) and score `z_harm`/`z_beta` on a DV that is not ceiling-bound --
  e.g. `shape_deviation` vs the tone=1.0 reference, which the driver already computes for `harm_a`
  (`B.shape_deviation`, driver :334-340) and which was the readout that was exactly zero pre-fix.
  Measures: the regulator's temporal authority per stream, on a DV chosen to have range.
- **Option C -- score observable #3 as written and accept the result.** Measures: the conjunction as
  registered. Would, on current evidence, record a falsification of SD-036's sole architectural
  commitment.

**Recommendation: A combined with B** -- extend the readiness gate to all three streams (that is
precondition (i) applied as written, not a new rule), and pre-register `shape_deviation` as the
per-stream DV for any stream the gate disqualifies on `sustain_ratio`. Reason: it is the only option
that can return a *falsification we would believe*. Under C, a refutation is indistinguishable from
`z_beta`'s DV having 0.15% of range; under A alone, the likely outcome is "not scoreable", which
leaves the claim unadjudicated exactly as it is today. B is not DV-shopping if the alternative DV is
**pre-registered before the run and applied to all streams symmetrically**, and `shape_deviation` is
already in the harness with a measured pre-fix null.

### D1 -- the per-stream magnitude bar

As posed ("a floor-robust relative bar replacing the bare sign test"), this presumes the streams
differ in *effect size*. They differ in *whether they have an effect* (2a/2c). A magnitude bar
applied to current data rejects `z_beta` on every seed (0.01-0.03% relative) and rejects `z_harm` on
2 of 3 (wrong sign at 1.6-5.7% magnitude). It makes C2 fail harder, not more honestly.

- **Option A -- relative effect floor, e.g. `(lo - hi)/hi >= 1%` per stream, sign-correct.**
  Measures: joint degradation of a size worth calling degradation. On current data: 0/3 seeds.
- **Option B -- require per-stream monotonicity instead of a two-point contrast** (per-stream
  Spearman rho <= -0.9 across the full sweep, the same bar C1 already uses for `z_harm_a`).
  Measures: a genuine per-stream dose-response, using the whole sweep rather than 2 of 5 points.
  On current data: 1/3 streams, 3/3 seeds for that one.
- **Option C -- keep the sign test, add only the readiness gate** (D0-A). Measures: the registered
  conjunction, with vacuous streams excluded rather than counted as failures.

**Recommendation: B, conditional on D0.** Reason: the two-point 0.3-vs-2.0 contrast discards 3 of
the 5 registered tones and is exactly where `z_harm`'s unordered variance does its damage; rho over
the full sweep is the bar the claim's own load-bearing criterion already uses, so it is not a new
invention, and it distinguishes "responds" from "is noisy" in a way no two-point magnitude bar can.
It also makes the CONFIRMING/FALSIFYING language literal: "degrade together" becomes "all three show
a dose-response", not "all three happened to sit lower at one of five tones".

### D2 -- how the tau-ordering test is scored

Section 2e shows the clause is ill-posed as written: the substrate's composition law makes effect
magnitude depend on `alpha` as much as `tau`, and predicts the observed (tau-inverted) ordering.

- **Option A -- score rank correlation between per-stream effect magnitude and registered tau,
  against a stated noise band.** Measures: the clause as literally written. Would record FAIL on
  current data -- but for a reason the substrate guarantees, not a reason about regulator layering.
- **Option B -- re-derive the predicted ordering from the composed pole `(1-alpha)*exp(-tau*tone)`
  and score against THAT.** Measures: whether one scalar moves all three streams by the amount the
  shared mechanism predicts -- which is the regulator-layer commitment the clause is trying to test.
  Requires amending SD-036's CONFIRMING text (a governance act, not an experiment-design act).
- **Option C -- drop the ordering test from this run and score only joint response**, recording the
  ill-posedness as a governance finding for SD-036's text.

**Recommendation: C now, B after governance amends the clause.** Reason: B is the scientifically
right test and I can state its form, but adopting it means *rewriting SD-036's registered CONFIRMING
criterion*, which is squarely a user/governance decision and not one a design pass may take.
A is worse than useless -- it would bank a falsification whose cause is a modelling error in the
claim text. C is the honest interim: it scores the part of CONFIRMING that is well-posed ("degrade
together") and routes the part that is not to governance. **This is the decision I am least willing
to take alone, because either B or C changes what the registered falsifier means.**

### D3 -- is the single-stream-isolation control arm in scope?

FALSIFYING's third disjunct ("the cluster can be reproduced by decaying any single stream in
isolation") has never been tested; 854 has no such arm. Levers exist and are verified:
`gaba_recurrence_z_harm_s` / `gaba_recurrence_z_harm_a` (`config.py:128-129`, both default True).

- **Option A -- in scope, two extra ON arms** (`_s` only, `_a` only). Measures: whether the joint
  cluster is reducible to one stream's decay. Cost: ON-arm cells x3.
- **Option B -- out of scope this run; observable #3's joint test first**, isolation as a successor
  conditional on a joint response being found. Measures: nothing extra now.
- **Option C -- in scope but cheap**: run isolation arms at the two contrast tones (0.3, 2.0) only,
  not the full sweep.

**Recommendation: B, and this one I hold weakly.** Reason: the isolation disjunct only becomes
decision-relevant *if a cluster is observed*. On current evidence there is no cluster to reduce --
`z_harm` and `z_beta` do not respond at all -- so isolation arms would spend ON-arm cells
distinguishing between explanations of a phenomenon that has not been demonstrated. If D0/D1 are
answered such that the run is expected to find a cluster, C is the right compromise. **Note the
interaction: there is a real argument for A regardless, because
`gaba_recurrence_z_harm_s/_a=False` is also the control-arm lever precondition (ii) names, so the
isolation arms double as a sharper control. I flag that rather than resolve it.**

### D4 -- SD-011's sourcing path and the P0h warmup

The first half is **largely already answered by the base harness** (correction 3 in section 5):
`_lib/baselines/sd036_decay.py` sets `harm_history_len=10` and `limb_damage_enabled=True`. That is
the SD-022 body path with the second source live -- precisely the regime SD-011's preconditions (i)
and (iii) require, and *not* the rank-2 legacy path the pre-flight feared. What is owed is that the
mode be **stated in the manifest**, which is a requirement, not a choice.

The live half is the **P0h affective-encoder warmup**. It is a driver-side library
(`ree-v3 experiments/_lib/zharm_a_p0_warmup.py`, `ZHarmAP0Config.p0_precision_norm_floor` default
0.1), not a config flag, so arming it is an explicit import in the successor driver.

- **Option A -- do not arm P0h.** `z_harm_a` is whatever the 854 training schedule produces, exactly
  comparable to the landed 854 run. Measures: the dissociation in the same regime the dose-response
  was measured in. Loses nothing on SD-011's own target, which P0h does not clear (mean lift
  -1108.379, readiness 0/3).
- **Option B -- arm P0h under the SD-020 PE target** (the one that clears: +0.9302, 3/3). Measures:
  the dissociation with a *trained* affective encoder rather than a near-frozen projection. But it
  changes the training schedule relative to 854, so the SD-036 dose-response arm is no longer
  directly comparable to the landed run.
- **Option C -- both, as a crossed factor.** Measures: both, and whether the dissociation depends on
  the encoder being trained. Doubles the cell count.

**Recommendation: A, plus explicitly stating all three regime facts
(`harm_history_len=10`, `limb_damage_enabled=True`, `p0h_armed=False`) in the manifest** as SD-011
precondition (iii) requires. Reason: this run's primary job is observable #3, and P0h does not clear
readiness on SD-011's own target, so arming it buys no SD-011 power while breaking comparability
with the one landed SD-036 measurement. If the user's priority is SD-011's leg rather than SD-036's,
B becomes right -- which is why this is a decision and not a default.

---

## 7. What I recommend overall

Answer **D0 first**; D1 collapses into it. My combined recommendation is
**D0 = A+B, D1 = B, D2 = C (with B routed to governance), D3 = B, D4 = A**, plus the four stale_note
corrections in section 5 raised against SD-036 and SD-011 independently of whether this run is ever
queued.

If the user prefers not to reopen SD-036's registered criteria at all, the coherent alternative is
**D0 = A alone**: run the regime matrix with the readiness gate extended to all three streams and
accept "observable #3 is not scoreable at n=3 on `sustain_ratio`" as the recorded outcome. That is a
real, publishable result about the instrument, and it is honest. What I recommend against in every
branch is **D0 = C** -- scoring the conjunction as written -- because it would retire SD-036's sole
architectural commitment on a measurement in which one of the three streams has 0.15% of dynamic
range.

---

## 8. What was NOT done, and why

- **No experiment was queued and no experiment script was written.** The user's consent
  (2026-09-19T22:12:50Z) is explicit: *"Queue NOTHING before that chip is answered."*
- **`/queue-experiment` was not invoked.** It is the mandatory path for writing a driver + queue
  entry, and this pass writes neither. It is the correct path for the session that resumes with
  D0-D4 answered.
- **The red-team review was not run.** It reviews a written design against a driver; there is no
  driver. It is owed by the resuming session.
- **`ree-v3/experiment_queue.json` and `ree-v3/experiments` were not claimed.** Two sibling campaign
  sessions own them (section 0). Because this pass queues nothing, claiming them would have
  manufactured a contention over resources this session never touches. The resuming session must
  re-run `task_claim.py check` on them.
- **Nothing was written to `claims.yaml`.** The four corrections in section 5 are reported for
  /governance to raise, not applied.
