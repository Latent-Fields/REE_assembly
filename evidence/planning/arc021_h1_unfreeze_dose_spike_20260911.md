# ARC-021 H1 unfreeze-DOSE spike -- a workable dose does NOT exist, and the binding constraint is NOT the dose

**Verdict: NO WORKABLE DOSE.** H1 as posed is unanswerable in this surrogate, and the honest
route to ARC-021's necessity half is the **H2** leg (substrate-blocked, GFLAG-0229). The
substrate queue should be re-prioritised on that blocker.

The reason is **stronger and more general than the one the refusal anticipated.** The refusal
record's hypothesis was that a small enough dose might keep the readout alive. It does -- the
readout survives comfortably at doses 2-15. What does not exist at ANY dose is (a) a runnable
`attribution_auc` falsifier and (b) an encoder-level effect big enough for the leg's own
pre-registered MARGIN. Both of those failures are present at **dose 0**, where the encoder is
frozen and there is no manipulation at all, so neither is caused by unfreezing.

- **Written:** 2026-09-11T16:27:28Z
- **Session:** `arc021-h1-unfreeze-dose-spike-20260911` (Mac `DLAPTOP`, umbrella worktree
  `jolly-neumann-a8857e`). **Chip:** `chip-20260911-arc021-h1-unfreeze-dose-spike`.
- **Work-graph token:** `complex (probe-gated)`. The deliverable is KNOWLEDGE. **Nothing was
  queued, no EXQ number consumed, no manifest written, nothing entered the evidence record.**
- **Prior record this supersedes in part:**
  `arc021_h1_leg_refused_readout_dies_under_unfreeze_20260911.md` (session
  `queue-arc021-h1-20260911`, GFLAG-0264, evidence_discrepancy, ARC-021 / MECH-069). That
  record's REFUSAL stands and is reinforced. Two of its subsidiary claims are CORRECTED
  below (sections 5 and 6).
- **Sibling records:** H2 -- `arc021_h2_leg_blocked_substrate_merged_arm_crash_20260908.md`.
  H3 -- ran as V3-EXQ-1011, `submargin_degradation_ruled_out`.
- **Substrate:** `ree-v3` `4b112b6`. **Assembly:** `REE_assembly` `8c2bc85817`.

---

## 1. What was measured

**320 cells**: 10 doses x 2 criterion arms x 2 conditions x 8 seeds, 810 s wall across five
parallel shards. DOSE = the number of **trailing** P1 episodes for which the encoder is
unfrozen, out of 80 (dose 0 = the frozen reference regime; dose 80 = the leg as specified).
Seeds are probe 3's `[1001 + 7i]`, disjoint from the driver's own `SEEDS`, so nothing
calibrated here could later be scored.

Artifacts, all under `ree-v3/experiments/_scratch/`:

| file | what it is |
|---|---|
| `arc021_h1_unfreeze_dose_sweep.py` | the sweep. Pre-registers its decision criteria **in its own docstring, before it was run** |
| `arc021_h1_unfreeze_dose_analyse.py` | the analysis, incl. `--addendum` (section 6) |
| `arc021_h1_unfreeze_dose_sweep.rows.json` | all 320 cells, every field |
| `arc021_h1_unfreeze_dose_sweep.analysis.json` | the derived tables below |

The raw shards carried a 64x32 latent matrix per cell (~10 MB of `_z_end` over 320 cells),
retained only long enough to compute the pairwise cross-arm divergence M-B. The condenser
attaches that scalar to both rows of each arm pair as `cross_arm_fn_div_rel` and drops the
matrices, so **every statistic in this document is re-derivable from the committed artifact**
-- verified by re-running the analysis against the condensed file and getting the tables
below bit-identically. The raw latents themselves are not retained.

Cell construction **mirrors the driver's own `_run_cell`** exactly -- `reset_all_rng(seed)`
(which is precisely what `arm_cell(do_reset=True)` does on enter), then env, codec, P0,
`_make_channels`, P1, `_harm_action_sensitivity`, `_eval_probes` through
`channels.harm_encoder`. Gating wraps the arm's own `_encode` in `torch.no_grad()` during
frozen episodes -- generic over arms, numerically identical to probe 5's hand-written
SEPARATED-only version. Every added measurement is taken under `no_grad` or via
`torch.autograd.grad`, and the probe/diagnostic batches are built inside an RNG sandbox that
saves and restores Python, numpy, torch and the harness fallback RNG, so nothing this file
measures perturbs the stream it measures. **The detach decision is untouched**
(refusal record 3e), so `arc021_h1_detach_probe.py` did not need re-running.

**Reproduction checks, both passed.** Dose 80 reproduces the refusal's own h3 figure to the
digit (`min(control AUC) - 0.5 = -0.01857`, section 3) and its control gap means
(+0.02144 DENSE / +0.01421 SPARSE -- identical, same seeds). Dose 0 lands at +0.3388 /
+0.3478, the frozen regime (probe 4: +0.21685 on 4 seeds). Fully-frozen cells record
`enc_fn_drift_rel` of exactly 0.00000, which is the gate's own positive control.

---

## 2. THE TRAP, and how this spike is built against it

**A dose chosen BECAUSE it keeps the control arm above its own floor is a tuned knob, not a
design choice.** Pre-registering an H1 criterion at a dose selected that way would be tuning
the design toward a pass and would invalidate any later H1 result. Three structural defences,
all in place before a number was seen:

1. **The criteria are constants in the sweep's docstring, fixed before it ran.** The survival
   half is not invented here at all -- it is the driver's OWN gates, recomputed with the
   driver's OWN constants (`SEPARATED_SIGNAL_FLOOR`, `MARGIN`, `MARGIN_AUC`) exactly as
   `_build_preconditions` computes them.
2. **Every dose is reported, including the failing ones** (sections 3, 4, 6). The tables
   below are the whole sweep, not a selection from it.
3. **The merge-vs-separate contrast is reported but is NOT an input to any verdict.** That is
   the load-bearing one: a contrast that varies with dose is EVIDENCE THE CONTRAST IS A TEST
   OF THE DOSE -- the very thing the spike was posed to detect -- so using it to pick a dose
   would destroy the finding it exists to produce.

**No dose is fixed by this document, because the answer is that none is licensed.**

---

## 3. (S) Does the instrument survive? -- control arm (SEPARATED) only

The driver's own four gates. S1 = non-degeneracy per condition (control mean gap >= 0.20);
S2 = `dv_headroom_margin_room_below_control` (range >= 2 x MARGIN = 0.30); S3 =
`dv_headroom_control_signal_floor_reachable` (max_abs >= 2 x floor = 0.40); S4 =
`dv_headroom_auc_room_below_control` (min control AUC - 0.5 >= MARGIN_AUC = 0.105).

| dose | gap DENSE | gap SPARSE | S1 | range | S2 | max_abs | S3 | minAUC-0.5 | S4 | mean AUC |
|---|---|---|---|---|---|---|---|---|---|---|
| 0  | +0.33880 | +0.34779 | Y | 0.70594 | Y | 0.78449 | Y | +0.05342 | **n** | 0.6625 |
| 2  | +0.26155 | +0.26857 | Y | 0.71278 | Y | 0.71358 | Y | +0.02489 | **n** | 0.6343 |
| 5  | +0.26350 | +0.27067 | Y | 0.62050 | Y | 0.65680 | Y | +0.05199 | **n** | 0.6323 |
| 10 | +0.21775 | +0.19906 | n | 0.52207 | Y | 0.54164 | Y | +0.03039 | **n** | 0.6313 |
| 15 | +0.20298 | +0.21534 | Y | 0.51872 | Y | 0.51619 | Y | +0.01469 | **n** | 0.6423 |
| 20 | +0.16820 | +0.14257 | n | 0.48175 | Y | 0.46629 | Y | -0.00814 | **n** | 0.6231 |
| 30 | +0.14958 | +0.13804 | n | 0.32662 | Y | 0.35158 | n | +0.01067 | **n** | 0.6209 |
| 40 | +0.14045 | +0.13291 | n | 0.37639 | Y | 0.38725 | n | +0.00417 | **n** | 0.6151 |
| 60 | +0.14047 | +0.13422 | n | 0.38856 | Y | 0.38084 | n | +0.01972 | **n** | 0.6250 |
| 80 | +0.02144 | +0.01421 | n | 0.09262 | n | 0.06268 | n | -0.01857 | **n** | 0.5366 |

Two readings, and they must be kept apart.

**The gap DV has a real surviving window: doses 2-15** (dose 10 misses S1 by 0.00094 on
SPARSE alone; doses 2 and 5 clear it by 30%). Survival decays monotonically with dose and the
transition is between 15 and 20. **The readout does NOT die at low dose** -- the refusal
record's repair hypothesis is confirmed on that point.

**S4 FAILS AT EVERY DOSE, INCLUDING DOSE 0.** At dose 0 the encoder is frozen in both arms:
there is no manipulation at all, and the gate still reads +0.053 against a 0.105 requirement.
So **S4's failure is not caused by unfreezing.** It is a property of the surrogate: the gate
is `min()` over the 16 control cells, so it is dominated by the worst cell and gets stricter
as n grows (the intended run is 48 seeds x 2 conditions = 96 control cells, where the min can
only fall further). See section 5 -- this corrects the refusal record.

---

## 4. (M) Is the manipulation still real? -- function space, normalised by ||z_P0||

All three statistics are measured on a fixed 64-observation probe batch, identical across
every cell of a given (condition, seed). M-A = how far the MERGED arm's shared encoder moved
from its P0 solution. M-B = how different the two arms' HARM-READOUT representations actually
are. M-C = M-B divided by the within-control-arm divergence between `enc_harm` and
`enc_sensory` (two encoders from the identical P0 start, the same number of steps, DIFFERENT
channel objectives) -- internally calibrated, no arbitrary constant.

| dose | M-A merged drift | SEP drift | M-B cross-arm | interchannel | M-C ratio | M-A ok (>=0.05) | M-C ok (>=1.0) |
|---|---|---|---|---|---|---|---|
| 0  | 0.00000 | 0.00000 | 0.00000 | 0.00000 | -- | n | n |
| 2  | 0.27530 | 0.27743 | 0.33240 | 0.44949 | 0.7395 | Y | n |
| 5  | 0.30835 | 0.36254 | 0.40813 | 0.50828 | 0.8030 | Y | n |
| 10 | 0.35280 | 0.46376 | 0.44616 | 0.59586 | 0.7488 | Y | n |
| 15 | 0.35161 | 0.45908 | 0.44319 | 0.58323 | 0.7599 | Y | n |
| 20 | 0.38445 | 0.55398 | 0.50338 | 0.69795 | 0.7212 | Y | n |
| 30 | 0.45095 | 0.64281 | 0.59283 | 0.74845 | 0.7921 | Y | n |
| 40 | 0.48171 | 0.68166 | 0.60873 | 0.78649 | 0.7740 | Y | n |
| 60 | 0.58761 | 0.89286 | 0.81734 | 1.04644 | 0.7811 | Y | n |
| 80 | 0.89867 | 2.42192 | 2.44378 | 2.76704 | 0.8832 | Y | n |

**The manipulation IS real from dose 2 upward.** At dose 2 the merged encoder has already
moved 27.5% of the latent's own scale from P0, and the two arms' harm-readout representations
differ by 33% of it. Nothing here is a nominal perturbation.

**The pre-registered M-C bar of 1.0 is not met at any dose -- but it fails FLATLY** (0.72 to
0.88 over a 40x span of dose), so **M-C does not measure dose.** Reported as pre-registered,
it refuses everywhere; read honestly, it is a constant structural property of the surrogate --
merging the encoder always moves the harm readout about three-quarters as far as ordinary
channel-specific shaping does. The manipulation-reality question is therefore answered by M-A
and M-B, and they say YES from dose 2 up. **Stating this rather than leaning on a bar that
turns out to be dose-blind is the point**; a gate that fails identically at every dose cannot
be the reason a dose is refused.

**(X) supporting -- the cross-channel gradient actually arriving at the harm-readout
encoder.** `g_other` (from sensory + forward) versus `g_harm`, decomposed on a fixed batch at
P1 end. In ARM_SEPARATED `g_other` is **0.000000 at every dose** -- `enc_harm` is in no other
channel's graph -- which is this decomposition's own positive control, and it held. In
ARM_MERGED the ratio runs 0.067 (dose 0) to 0.175 (dose 80), cos(other, harm) +0.20 to +0.36.
**Clip asymmetry** (refusal record's third binding constraint), over unfrozen steps only:
SEPARATED 0.121-0.133 vs MERGED 0.145-0.164 for doses 2-60 -- a mild asymmetry that does NOT
reproduce the 18.6% / 44.2% split the refusal measured, which appears only at dose 80
(0.186 / 0.442). **The clip asymmetry is a full-unfreeze phenomenon, not a general one.**

---

## 5. CORRECTION 1 to the refusal record: the AUC gate failure is not an unfreeze effect

The refusal record's section 3d table lists `dv_headroom_auc_room_below_control` (measured
-0.01857, required 0.105, "UNMET, negative") among three preconditions said to fail "before a
single treatment cell is trained" because of the unfreeze. The dose-0 row of section 3 above
shows the same gate at +0.05342 -- **still short of 0.105, with the encoder frozen and the two
arms differing only in trunk topology.** The unfreeze makes it worse; it did not cause it.

**Consequence, and it is the load-bearing one for routing:** `attribution_auc` is one of the
two DVs ARC-021's falsifying signature names ("calibration_gap AND attribution accuracy").
A leg that cannot gate it cannot measure half of what the claim is posed against, **at any
dose, including no dose at all**. This is an argument for H2 that is entirely independent of
the dose axis, and it was not available before this sweep.

## 6. CORRECTION 2: probe 5's "short unfreeze CLEARS FLOOR" was measured off the driver's path

The refusal record's section 4 cites probe 5's short-unfreeze cell at **+0.21158**, above the
0.20 floor, as the evidence that shortening the unfreeze rescues the readout. Probe 5 calls
`_eval_probes` directly and **does not call `_harm_action_sensitivity` first**; the driver's
own `_run_cell` does, and that call performs 16 `env.reset()`s, so it advances the RNG and the
env state that `_eval_probes` then samples. Measured directly, on probe 5's own three seeds at
dose 10:

| path | mean control gap |
|---|---|
| WITH `_harm_action_sensitivity` (the driver's `_run_cell` path -- what a scored run takes) | **+0.17008** |
| WITHOUT it (probe 5's path) | +0.21026 |
| probe 5 as reported | +0.21158 |

A **+0.040 probe-draw artifact**, straddling the 0.20 floor. The conclusion survives with 8
seeds -- dose 10 reads +0.21775 DENSE / +0.19906 SPARSE on the canonical path, so the rescue
is real -- but it is **marginal at K=10, not comfortable**, and comfort only arrives at
K=2-5. Any successor must quote the `_run_cell` path.

---

## 7. THE ACTUAL BINDING CONSTRAINT: survival and encoder-level effect size trade off, and never both clear

At dose 0 both arms are frozen, so they differ ONLY in trunk topology -- which is exactly
V3-EXQ-993a/1011's comparison, already adjudicated null. Any contrast at dose 0 is therefore
the **trunk-level** effect. The part this leg is named for ("H-encoder-level-merge-degrades")
is the **increment over that baseline**.

| dose | DENSE contrast | encoder incr | incr / MARGIN | sign | SPARSE contrast | encoder incr | incr / MARGIN | sign | survives (S1-S3) |
|---|---|---|---|---|---|---|---|---|---|
| 0  | +0.03554 | +0.00000 | 0.00 | 5/8 | +0.15837 | +0.00000 | 0.00 | 7/8 | Y (no manipulation) |
| 2  | +0.06915 | +0.03362 | 0.22 | 6/8 | +0.19387 | +0.03550 | 0.24 | 7/8 | **Y** |
| 5  | +0.08547 | +0.04994 | 0.33 | 6/8 | +0.18402 | +0.02565 | 0.17 | 7/8 | **Y** |
| 10 | +0.08384 | +0.04830 | 0.32 | 7/8 | +0.19661 | +0.03824 | 0.25 | 8/8 | marginal |
| 15 | +0.09126 | +0.05572 | 0.37 | 7/8 | +0.19335 | +0.03498 | 0.23 | 7/8 | **Y** |
| 20 | +0.12846 | +0.09292 | 0.62 | 7/8 | +0.21985 | +0.06148 | 0.41 | 8/8 | n |
| 30 | +0.15605 | +0.12052 | 0.80 | 7/8 | +0.20767 | +0.04930 | 0.33 | 8/8 | n |
| 40 | +0.17116 | +0.13562 | **0.90** | 7/8 | +0.19410 | +0.03573 | 0.24 | 8/8 | n |
| 60 | +0.12419 | +0.08866 | 0.59 | 7/8 | +0.21124 | +0.05287 | 0.35 | 7/8 | n |
| 80 | +0.03696 | +0.00142 | 0.01 | 7/8 | +0.12454 | -0.03383 | -0.23 | 8/8 | n |

**The two requirements move in opposite directions along the dose axis and never both clear.**
Where the readout survives (2-15), the encoder-level increment is 0.17-0.37 of the leg's own
pre-registered MARGIN -- 3 to 6 times too small. Where the increment approaches MARGIN (0.90
at dose 40), the control arm has already fallen to +0.140 / +0.133, well under its 0.20 floor.
There is no dose at which an encoder-level effect of the pre-registered size is both reachable
and readable.

**And the contrast is dose-dependent by ~5x and non-monotone** on DENSE (+0.036 -> +0.171 ->
+0.037), peaking at 40 and collapsing at 80. That is the spike's framing question answered
directly: **what a merge-vs-separate criterion would score at a chosen dose is mostly a
function of the dose**, not of channel separation.

### 7a. The manipulation is confounded with auxiliary supervision, at every dose

The sign column is uniform: **MERGED > SEPARATED in 5/8 to 8/8 cells at every dose, in both
conditions** -- the OPPOSITE of ARC-021's H1 prediction. That is not the uninterpretable
noise-scale sign the refusal saw at dose 80; it holds where the control arm is fully alive.

The mechanism is visible in the training objective itself. Mean P1 harm loss:

| dose | SEPARATED | MERGED |
|---|---|---|
| 0  | 0.37685 | 0.35745 |
| 5  | 0.39038 | 0.36183 |
| 15 | 0.40589 | 0.37061 |
| 40 | 0.43398 | 0.38750 |
| 80 | 0.44560 | 0.38641 |

**MERGED fits the harm task strictly better at every dose, and the advantage widens with
dose.** In ARM_SEPARATED the harm-readout encoder receives gradient from the harm BCE ALONE --
a sparse binary signal at a 2-4% base rate. In ARM_MERGED the same encoder additionally
receives two DENSE MSE gradients. So in this surrogate, "merge the encoder" is inseparable
from **"give the harm representation dense auxiliary self-supervision"**, and those two make
OPPOSITE predictions for the DV. Unfreezing is precisely what switches the confound on at the
encoder level, which is why the advantage tracks the dose.

**This confound is a property of the manipulation, not of the dose, so no dose removes it** --
and the instrument's third arm cannot separate it either: `SHARED_ENC_SEP_HEADS` also gives
its single encoder all three losses, so it was designed to attribute encoder-level vs
trunk-level, not supervision-density. Probe 5's "anchored" candidate (a maintained
reconstruction term in both arms) is the right SHAPE of repair for this, and it was already
measured and did not restore the readout at full dose -- but it was never evaluated as a
CONFOUND fix at a surviving dose. That is the one remaining cheap probe if anyone wants to
reopen H1; it is not recommended, for the reasons in section 5.

---

## 8. Routing

**H1 is unanswerable in this surrogate.** Not "under-powered at the doses tried" -- three of
the blocking facts (S4, M-C flatness, the supervision confound) are present at dose 0, where
there is no manipulation, so they are properties of the instrument and of the manipulation,
not of the dose. **Nothing routes to `/queue-experiment`.**

**The owed work is H2** -- the leg ARC-021's `what_would_answer` literally names -- currently
substrate-blocked on the `ContextMemory` in-place write (`ree_core/predictors/e1_deep.py:127`
and `:272-273`; GFLAG-0229; record
`arc021_h2_leg_blocked_substrate_merged_arm_crash_20260908.md`). **Recommendation: raise that
blocker's priority in `substrate_queue.json`.** It is now the only remaining route to
ARC-021's necessity half: H3 ran (V3-EXQ-1011, `submargin_degradation_ruled_out`) and H1 is
closed as un-instrumentable.

**For `/governance`, attached to the existing GFLAG-0264** (evidence_discrepancy,
ARC-021 / MECH-069) rather than as a new flag -- that flag already carries the H1 follow-on:

1. **Sections 5 and 6 correct the landed refusal record**, which over-attributes the AUC gate
   failure to the unfreeze and cites a probe-draw-inflated figure for the short-unfreeze
   repair. Both corrections are measurements, not re-readings.
2. **Registry leg `H-encoder-level-merge-degrades` should move off `alive`.** It has not been
   falsified and has not been tested -- it has now been shown un-instrumentable in this
   surrogate across the whole dose axis, which is a stronger statement than the refusal could
   make from two endpoints. The disposition is governance's to set; **nothing in
   `hypothesis_space_registry.v1.json` was edited by this session.**
3. **Section 7a is an OBSERVATION, not evidence, and must never be cited as such.** Nothing
   here was pre-registered as a test of ARC-021, no manifest exists, and the direction it
   reports is confounded with supervision density by construction. It is recorded because a
   uniform wrong-direction result across 320 cells and 10 doses is worth a governance reading
   of MECH-069, not because it adjudicates anything.
4. **`ARC-021` and `MECH-069` are untouched.** No evidence was produced in either direction.

**Instrument note for any future leg in this family**, independent of ARC-021:
`dv_headroom_auc_room_below_control` as written takes `min()` over control cells, so it gets
monotonically stricter as the seed count rises and can refuse a regime that is perfectly
healthy in the mean (dose 0 here: mean AUC 0.6625, gate reads the worst cell at 0.5534). A
successor should either denominate it on a quantile or state explicitly that it is a
worst-cell gate. Raised here as a finding, not fixed -- fixing it is not this spike's scope.
