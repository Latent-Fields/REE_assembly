# V3-EXQ-1005 (MECH-267 mode-content LOCATION separation) -- DESIGN REFUSED at `/queue-experiment` Step 4.5 (red-team BLOCKING, confirmed)

**Status: NOT QUEUED. No queue entry, no coordinator row, no manifest. The design-complete driver and the two probes that confirm the refusal are landed under `ree-v3/experiments/_scratch/` so the paid-for work is recoverable; nothing in this file has been written to `claims.yaml`, `substrate_queue.json`, or `experiment_queue.json`. A governance flag (`evidence_discrepancy`, MECH-267) and a spike chip carry the follow-on.**

- **Written:** 2026-09-07T12:45:20Z
- **Session:** `hopeful-solomon-01a60c` (Mac `DLAPTOP`, umbrella worktree), campaign W4-S2 item 0 (`chip-20260907-campaign-w4-s2-ratified-successors`), resuming IGW-20260905-238 whose session died at the background-wait ceiling with the driver untracked.
- **Red-team model:** `fable` (Fable 5.1), one pass, foreground, 2026-09-07T08:57Z-09:07Z. Verdict **BLOCKING**. Findings preserved verbatim in section 4.
- **Verification:** every source citation checked against `ree_core` (section 2); the numerical claims reproduced by the red-team's probe AND by an independent probe written by this session (section 3).

---

## 1. What the run was designed to measure, and why it cannot

MECH-267 asserts mode-conditioned proposal CONTENT. Every prior run in the lineage (V3-EXQ-869 / 869a / 923 / 927 / 928) scored proposal BREADTH (`mean_raw_std_by_dim`). V3-EXQ-1005 was designed to read the never-read `mean_by_action_dim` and score a per-dimension-standardised cross-mode centroid separation, paired per seed against a mode-blind control, with the scored arms (H2_ONLY `mode_value_weight`, HORIZON_ONLY `mode_horizon_scale`) held to a C4 breadth-invariance guard and NOISE_H3_REF as the DV-can-move positive control (P4).

**The refusal, in one sentence:** at the production CEM settings the design deliberately targets (`num_cem_iterations=3`, live `HippocampalConfig` defaults), the ONLY channel through which a breadth-matched scored arm can move the proposal centroid -- elite selection feeding the refit mean -- is capped at roughly 0.001-0.01 standardised units on this bench, against a pre-registered C1 floor of 0.02; while the positive control moves the DV by ~0.27 through a channel (per-mode `ao_std` rescaling acting on a non-linear decoder) that the scored arms shut by construction. So the near-certain 30-seed outcome -- FAIL / `mode_content_location_null_dispersion_only` / `weakens`, `non_degenerate: true`, all four preconditions met -- would be produced by the substrate's default CEM configuration whether or not MECH-267 is true. A null on the scored arms cannot be told apart from "the elite-refit channel is inert on this bench". That is the definition of a result nobody can attribute, and Step 4.5 says do not queue it.

## 2. Source verification (all in `ree-v3` at the shared checkout, 2026-09-07)

| claim | where | verified |
|---|---|---|
| Support-preserving CEM is the live default | `ree_core/utils/config.py:2477` `use_support_preserving_cem: bool = True`; `:2486` `support_preserving_stratified_elites: bool = True`; `:2495` `support_preserving_ao_std_floor: float = 0.2` | yes; the driver sets none of these (grep: no hits) |
| Refit reads E2's RE-COMPUTED action objects, not the sampled ones | `ree_core/hippocampal/module.py` refit block: `trajectories[idx].get_action_object_sequence()` stacked, `ao_mean = elite_ao_tensor.mean(dim=0)` | yes |
| `ao_std` is clamped to the 0.2 floor after every refit | same block: `ao_std = torch.clamp(ao_std, min=_std_floor)` gated on `use_support_preserving_cem` | yes |
| H3 multiplies `ao_std` by the per-mode scale AFTER the clamp | same block, `if mode_partitioned_cem and mode_scale is not None: ao_std = ao_std * mode_scale` | yes |
| Iteration-0 `ao_std` = ones x mode scale | `propose_trajectories`: `ao_std = torch.ones_like(ao_mean)`; `if mode_scale is not None: ao_std = ao_std * mode_scale` | yes |
| Elite indices go through `_support_preserving_elite_indices` after the argsort | `elite_indices = torch.argsort(scores_tensor)[:num_elite]` then `self._support_preserving_elite_indices(...)` | yes (bears on finding 3) |

## 3. Numerical confirmation (two probes, both landed in `ree-v3/experiments/_scratch/`)

**Probe A -- `exq1005_probe_aostd_clamp.py` (this session, independent of the red-team's script).** Seed 0, the driver's own `_make_hippocampal` / seeding, reading `cem_iteration_diagnostics`:

| arm | mode | iter0 ao_std | iter1 ao_std | iter2 ao_std | E2-recomputed ao across-candidate std (mean / max) | elite first-action classes iters 1-2 |
|---|---|---|---|---|---|---|
| CTRL_OFF | internal_planning | 1.000 | **0.200** (min=max) | **0.200** | 0.0051 / 0.0198 | {2: 3} (single class) |
| H2_ONLY | internal_planning | 1.000 | **0.200** | **0.200** | 0.0051 / 0.0197 | {2: 3} |
| NOISE_H3_REF | internal_planning | 1.300 | 0.260 | 0.260 | 0.0056 / 0.0200 | {2: 3} |
| NOISE_H3_REF | offline_consolidation | 0.300 | 0.060 | 0.060 | 0.0041 / 0.0197 | {2: 3} |

The clamp binds on every element from iteration 1 on, in every arm; E2's action-object head (untrained, Linear-ReLU-Linear) varies across candidates by ~0.005, so the elite mean cannot move `ao_mean` by more than that; and the elite set collapses to a single first-action class in every arm and mode by iteration 1.

**Probe B -- `exq1005_probe_elite_channel.py` (red-team's, re-run by this session; numbers below are from this session's run).**
- B (oracle elite bound): elites pushed +u vs -u along four random directions at EVERY iteration, identical noise: `d(A,B)` = 0.0024..0.0126 across 12 trials; per-seed means 0.0036 / 0.0070 / 0.0088. The strongest possible content re-ranker never reaches the 0.02 floor.
- C (oracle under the driver's real per-mode seeds, i.e. the best case for a scored arm): `dbar(ORACLE) - dbar(CTRL_OFF)` = **+0.00010, +0.00009, +0.00096** vs floor 0.02002; breadth spread unchanged (C4 passes). Misses C1 by 20-200x.
- D (readout-only scale leak): CTRL_OFF final-iteration samples, deviations rescaled about the SAME sample mean with IDENTICAL eps, re-decoded: `d(s=1.3 vs 0.3)` = **0.272 / 0.259** (seeds 0/1) -- larger than the whole control dbar (~0.13). A linear decoder would give exactly 0; the movement is decoder curvature. 48 decode calls per cell, so nothing else consumes RNG.

**Reading.** P4 (NOISE_H3_REF) certifies that the DV responds to per-mode `ao_std` rescaling through decoder non-linearity -- a channel the scored arms pin at 1.0 by design. The recorded `dv_headroom` entry is computed from the same deltas and inherits the defect. C1 is unreachable by the scored arms by construction; C2/C3 would pass on any mode-dependent re-ranking (E[(Delta+delta)^2] = Delta^2 + Var(delta) is structurally positive), so the only discriminating criterion is the one that cannot be met.

## 4. Red-team findings, verbatim (model: fable)

# V3-EXQ-1005 adversarial design review -- findings

Reviewer scope: attribution only (not code/style/API). Every line cited was read.
Probe used for the measurements below (re-runnable, ~40 s CPU, touches nothing):
`/private/tmp/claude-501/-Users-dgolden-REE-Working--claude-worktrees-hopeful-solomon-01a60c/dd05e864-1dec-4e58-92ac-57a4dcb355a4/scratchpad/exq1005_probe_elite_channel.py`

## VERDICT: BLOCKING

**The result nobody could attribute:** the near-certain outcome of the 30-seed run --
`FAIL / mode_content_location_null_dispersion_only / evidence_direction "weakens"` with
`non_degenerate: true` and all four preconditions met -- is produced by the substrate's
default CEM configuration regardless of whether MECH-267 is true. The C1 floor (0.02) sits
20-200x above the ceiling of the ONLY channel the scored arms can use, while P4 (the
"DV-can-move" positive control) certifies a channel (sampling-std -> decoder nonlinearity)
that the scored arms shut by construction. So a null on H2_ONLY / HORIZON_ONLY cannot be
told apart from "the elite-refit path is inert at production settings", which is exactly
the unattributability P4 was added to prevent.

---

## Finding 1 (BLOCKING, families 1+2+4): C1 is unreachable by the scored arms by construction; P4 certifies a different channel

### Mechanism, from source

1. **The refit averages E2's RE-COMPUTED action objects, not the sampled ones.**
   `module.py:2102` samples `action_objects_sample = ao_mean + ao_std * noise`; `:2105`
   decodes to actions; `:2109-2111` rolls out with `compute_action_objects=True`, and
   E2 recomputes `o_t = self.action_object(z_world, action, ...)` per step
   (`e2_fast.py:723-725`, head at `:144-148`, Linear-ReLU-Linear, untrained). The refit
   then reads `trajectories[idx].get_action_object_sequence()` (`module.py:2296`,
   `e2_fast.py:89-93`) and sets `ao_mean = elite_ao_tensor.mean(dim=0)` (`:2301`).
   So whatever the sampled content was, ao_mean is pulled onto E2's action-object ball.

2. **That ball is tiny, so elite identity has almost no leverage on ao_mean.** Probe
   section A, seed 0, internal_planning: at iteration 0 the sampled ao noise has std 1.0
   but the across-candidate std of E2's o_t is **0.014 mean / 0.029 max**; at iterations
   1-2 it is **0.003 mean / 0.005 max**. Any two 3-of-16 elite subsets therefore have
   means within ~0.01 in ao space.

3. **ao_std is clamped to a constant 0.2 floor on every dimension from iteration 1 on.**
   `config.py:2477` `use_support_preserving_cem: bool = True`; `:2495`
   `support_preserving_ao_std_floor: float = 0.2`; `module.py:2302` computes the elite
   std (~0.01), `:2309` `ao_std = torch.clamp(ao_std, min=_std_floor)`. The script never
   overrides either (grep: no `support_preserving` in the script). Probe A confirms
   `ao_std_in (mean/min/max) = (0.200, 0.200, 0.200)` at iterations 1 and 2 for CTRL_OFF
   and H2_ONLY alike -- the clamp is binding on every element.

4. **The DV is the mean over the FINAL iteration's 16 samples** (`module.py:2325`
   `all_trajectories = trajectories`; `:2494` `final_summary`; `:729-761`
   `_summarize_action_tensor` -> `mean_by_action_dim`). Each sample is
   `decode(ao_mean_2 + 0.2 * eps_k)`. The centroid is therefore
   decode(ao_mean_2 + 0.2*eps_bar) plus a ReLU-nonlinearity term, where eps_bar (mean of
   16 unit normals, ~0.25/dim) contributes ~0.05 in ao space -- an order of magnitude
   above the ~0.005 that elite choice can move ao_mean_2.

### Measured ceiling of the elite-selection channel (probe B, C)

- **B -- oracle elites, identical noise:** replacing `_support_preserving_elite_indices`
  with an oracle that, at EVERY iteration, picks the 3 candidates that push the decoded
  action mean along +u (mode A) vs -u (mode B), same sampling seed for both, gives
  `d(A,B)` = 0.0024 .. 0.0126 (seed means 0.0036 / 0.0070 / 0.0088). This is the maximum
  any content-selective re-ranking can produce on this instrument -- and it is BELOW the
  0.02 floor on every one of 12 trials, with no sampling-noise penalty at all.
- **C -- oracle under the script's actual per-mode seeds:** each mode gets its own
  oracle direction; `dbar(ORACLE) - dbar(CTRL_OFF)` = **+0.00010, +0.00009, +0.00096**
  (seeds 0-2) against the floor 0.02002. Breadth spread unchanged (C4 would pass). So
  the best possible content arm clears C4 and misses C1 by 20-200x.
- The smoke's real H2_ONLY delta (+0.00177, elite overlap 0.0, authority ratio 106-190x)
  is consistent: the ranking is fully mode-controlled and the centroid still does not
  move, because the refit discards the ranking's leverage (points 1-3).

### What P4 actually certifies (probe D, family 4)

NOISE_H3_REF reaches the DV through `ao_std`: `module.py:1976` `ao_std = ones_like`,
`:1985` `ao_std = ao_std * mode_scale` (iteration 0), and `:2322` `ao_std = ao_std *
mode_scale` applied AFTER the 0.2 clamp (so final-sample std = 0.2 * {1.3, 1.0, 0.5,
0.3}). Probe D takes CTRL_OFF's own final-iteration samples, holds ao_mean and eps
IDENTICAL, rescales only the deviations about the sample mean, and re-decodes:
`d(s=1.3 vs s=0.3)` = **0.272 / 0.259** (seeds 0, 1) -- larger than the entire control
dbar (0.13). With a linear decoder this would be exactly 0; it is non-zero because the
decoder is Linear-ReLU-Linear (`module.py:125-129`), so E[decode(mu + s*delta)] depends
on s. That is the reference arm's channel, and it matches the manifest
(NOISE_H3_REF internal_planning|offline_consolidation pair d = 0.238 vs control 0.114).

The scored arms pin noise at 1.0 (script `:273`, `:311-319`), so their ao_std is
bit-identical to CTRL_OFF on every iteration (probe A). **P4 therefore proves the DV
responds to a knob the scored arms do not touch, and says nothing about whether it can
respond to the knob they do touch.** The `dv_headroom` entry (script `:812-845`) is
computed from the same NOISE_H3_REF deltas and inherits the defect verbatim.

### Why this changes what the run can conclude

Script `:886-898` routes "P1-P4 met, no scored arm clears" to `weakens` with the note
"no breadth-matched mode-conditioning facet shifts WHERE the proposer samples, only HOW
BROADLY". Under points 1-4 that branch fires whether or not mode conditioning selects
content: the instrument cannot register a WHERE shift smaller than ~20x the channel's
ceiling. `non_degenerate` (`:971`) reads True because it is keyed on P4, so the manifest
will assert the measurement "COULD have discriminated" (`:965-970`) when the scored
channel could not.

### Cheap confirmers

- **Grep:** `grep -n "support_preserving_ao_std_floor\|use_support_preserving_cem" ree_core/utils/config.py` (0.2 / True) and the same grep on the script (no hits).
- **One dry-run assertion:** on every CTRL_OFF and scored-arm cell,
  `hip.get_last_propose_diagnostics()["cem_iteration_diagnostics"][i]["ao_std_min"] == ["ao_std_max"] == 0.2` for i in {1, 2}. If true, the clamp is binding and the refit std carries no elite information.
- **Paper arithmetic:** elite-subset mean shift in ao space <= 2 x max across-candidate E2-ao std at iter 1 (~0.005-0.01); final-sample noise term 0.2 x |eps_bar| ~ 0.05; ratio ~0.1-0.2 -> d contribution ~0.001-0.01 (before per-mode seed decorrelation), vs floor 0.02.
- **Run the probe** (path above); sections B/C/D reproduce the numbers here.

---

## Finding 2 (CONTESTED, family 3): the "weakens" note would mis-describe a statistically robust positive effect

H2_ONLY's smoke delta is +0.00177 with t = 4.35 and 3/3 positive at n=3. At n=30 with
the same SD (0.0007) the paired t is ~14, so C2 and C3 will be met and C1 alone decides.
The evidence_direction_note (`:890-898`) then says "no ... facet shifts WHERE the
proposer samples". The manifest would carry a significant, consistent positive location
shift labelled "null". Moreover the positive sign is structural, not content: any
mode-dependent perturbation of the centroids adds independent displacement to
already-separated centroids, and E[(Delta+delta)^2] = Delta^2 + Var(delta) > Delta^2, so
dbar rises in expectation for ANY re-ranking, content-bearing or not. C2/C3 are thus
near-guaranteed for H2 and carry no content information; the note should not read a
sub-floor-but-significant positive as "does not shift WHERE".

Confirmer: the smoke manifest already shows it (`per_arm_results.H2_ONLY`: t 4.35,
n_pos 3/3, C1 false). Paper: t(n=30) = 0.00177 / (0.0007/sqrt(30)) = 13.9.

---

## Finding 3 (CONTESTED, family 1): the recorded `ranking_authority` elite set is not the substrate's elite set

Script `:468-471` recomputes elites as its own `argsort` top-`int(16*0.2)=3`. The
substrate runs `_support_preserving_elite_indices` (`module.py:2201-2208`) with
`support_preserving_stratified_elites: bool = True` (`config.py:2486`), which forces the
best candidate per first-action class before filling by score. Probe A, CTRL_OFF iter 0:
argsort top = [12, 14, 2], substrate elites = [12, 14, 13] (class-forced). So
`elite_set_overlap_frac` and `ranking_changed` in the manifest describe a hypothetical
pure-argsort elite, not what refit actually used. Non-gating, but it is the diagnostic
the docstring (`:437-452`) relies on to say a null is "a finding about the MECHANISM"
rather than an under-powered knob -- and per Finding 1 the mechanism finding is about
the std floor, not about re-ranking authority.

Confirmer: record `support_preserving_elite_active` and the returned indices from
`cem_iteration_diagnostics` in the dry run and compare to the script's own argsort.

---

## Finding 4 (CONTESTED, family 4 / standardisation): the confound model in the docstring and manifest is mis-located

Docstring `:36-46` and `custom_information.breadth_to_location_confound` (`:1107-1115`)
attribute NOISE_H3_REF's location movement to "a wider sample feeding top-k elite refit
pulls the refit ao_mean away from the terrain prior", and the invariance declaration
`:173-176` says a pure scale change is "invariant under the per-dim STANDARDIZED
statistic in expectation -- but NOT through the elite-refit path". Probe D shows the
opposite allocation: with the elite-refit path frozen (identical ao_mean, identical
eps), a scale change alone moves d by ~0.27 via decoder nonlinearity, while the elite
path (probe B) moves it by <= 0.013. The standardisation is not scale-invariant on this
decoder even per-realisation with common random numbers. C4 still guards it (breadth
spread), so the scored arms are not contaminated -- but the manifest's stated reason
for excluding the reference arm is wrong, and a reader would draw the wrong mechanism
lesson ("refit-driven") from a PASS on P4.

Confirmer: probe D (two seeds shown); or on paper, note that centring the deviations
removes the eps_bar term, so any residual centroid shift under rescaling is decoder
curvature.

---

## Checked and CLEAR

- **P1 exact-zero leak check** is satisfiable and correct: uniform maps give
  `mode_scale = 1.0` (`module.py:1826-1834`) and `effective_horizon = round(4*1.0) = 4`
  (`:2007-2016`), slicing `world_seq[:, :5, :]` to full length (`:1621-1623`) --
  bit-identical, confirmed in the smoke (delta exactly 0.0).
- **HORIZON_ONLY engages** on 2 of 4 modes only (effective horizons 4/2/3/4;
  `config.py:2574-2579`); the ip|oc pair is identical to CTRL_OFF (manifest confirms
  0.11399788669382714 on both). Averaging six pairs handles this as intended; the
  channel ceiling of Finding 1 applies equally.
- **C3 count** uses `ceil(0.7 * len(seeds))` = 21 at n=30, 3 at n=3; `n_pos` counts only
  non-None deltas, and any None routes to `measurement_degenerate` first (`:849-856`), so
  no realised-vs-intended mismatch.
- **P2/P3** engagement and readout checks are consistent with the substrate diagnostics
  (`module.py:1983`, `:1991-1999`, `:2016`); the reference arm's external_task cell (scale
  1.0, bit-identical to CTRL_OFF) still passes `_cell_engaged` (`:606-612`).
- **Verdict grid** otherwise routes every precondition failure to `non_contributory`
  (`:849-875`), never to a claim verdict. The defect is that the preconditions cannot
  fail for the reason that matters (Finding 1).
- **No extra RNG consumers** alter the final pool at these settings: exactly 48 decoder
  calls per cell (probe D), and `_inject_support_preserving_candidates` (`module.py:1423`,
  early-return at the class-count gate) only fires when the final pool's first-action class count is
  below target; the ReLU class pin makes this possible in principle, but the smoke's
  bit-identical CTRL_OFF/CTRL_UNIFORM cells show it is deterministic and arm-independent.

## Not adjudicated (observations only)

- The 0.2 std floor is the production default the run explicitly targets ("production
  num_cem_iterations=3"), so a null here IS a statement about the production substrate's
  proposal-content plasticity -- but it is a `substrate`/instrument statement (the CEM
  refit projects onto E2's ao ball and re-samples at a fixed 0.2 std), not evidence
  about MECH-267's content assertion, and it should route accordingly rather than to
  `weakens`.
- A positive control that shares the scored arms' channel would be an oracle-elite arm
  (as in probe B/C) or a `mode_value_weight` arm on a substrate whose E2 action-object
  head has enough action-dependence that elite identity moves ao_mean by more than the
  floor. Either would make P4 license the scored null; the current P4 cannot.

## 5. Disposition of each finding

| # | severity | disposition |
|---|---|---|
| 1 | BLOCKING | **CONFIRMED** (sections 2-3). Not fixable by an edit to this driver: withdrawing or lowering C1 would fit the gate to the null; adding an oracle-elite positive control (the channel-matched control the finding asks for) would, on this bench, fail its own readiness gate every time (probe C), so the run would abort at P0 on every seed -- a run whose readiness gate is known-unmet at authoring time is not queued (Step 2.5a). Route: the bench gap below. |
| 2 | CONTESTED | Confirmed as stated (smoke H2_ONLY t=4.35 at n=3; the sign is structural). Moot while finding 1 stands; the successor design must not let C2/C3 carry content information (a paired t on a structurally positive quantity is not evidence of content). Recorded, not edited. |
| 3 | CONTESTED | Confirmed (probe A: argsort top-3 [12,14,2] vs substrate elites [12,14,13] at iter 0 -- stratified elites active). The \`ranking_authority\` diagnostic recomputes a hypothetical elite set. Recorded; the successor should read \`support_preserving_elite_*\` from \`cem_iteration_diagnostics\` instead of recomputing an argsort. |
| 4 | CONTESTED | Confirmed (probe D). The docstring's "breadth -> elite-refit -> location" confound story is mis-located: the dominant path is decoder curvature under \`ao_std\` rescaling, not elite refit. The driver docstring is left as authored (it is a refused design, not a shipped one); this record is the correction. |

## 6. The gap, named in the work-graph vocabulary

The node is **`complex (probe-gated)` -> `puzzle (known rules)`**, not `complicated (buildable)`: the missing fact is whether the elite-selection channel can relocate the proposal centroid above the sampling floor on a bench whose E2 action-object head is TRAINED (the 1005 bench instantiates an untrained E2, whose recomputed action objects barely depend on the candidate -- ~0.005 across-candidate std). Two causes are entangled and a 2x2 spike separates them:

- **Spike (chipped: `chip-20260907-exq1005-elite-channel-ceiling-spike`):** cells = {E2 untrained (the 1005 bench), E2 trained (a warmed agent's E2, e.g. from the 978/1006 warmup path)} x {`support_preserving_ao_std_floor` 0.2 (production), 0.0 (legacy opt-out, with `use_support_preserving_cem=False`)}. DV = the oracle-elite centroid ceiling of probe C (`dbar(ORACLE) - dbar(CTRL_OFF)`), 3-5 seeds, proposer-only. Decision: a cell clearing 0.02 says the 1005 design is runnable in that regime (successor `V3-EXQ-1005a` with that bench); no cell clearing says MECH-267's content assertion is not measurable by proposal-output centroid at production CEM settings on any bench, and governance should either narrow `what_would_answer` to the breadth channel or register a `complicated (buildable)` build (ao_std floor policy under mode conditioning, or E2 action-object action-dependence) in `substrate_queue.json`.
- **Not registered as a build now** because the spike may show the trained-E2 cell already clears; registering a build ahead of that fact is the `complicated`-before-`complex` inversion the vocabulary warns against.

## 7. What this says about the existing MECH-267 evidence (for `/governance`)

- V3-EXQ-928's H3 result (+0.0167 on the breadth DV) is consistent with everything here: H3 acts on `ao_std` after the clamp, which IS breadth. Nothing in this record contradicts 928.
- The lineage's "wash-out at iters=3" is at least partly the support-preserving `ao_std` floor (0.2) re-sampling every iteration about a refit mean pinned to E2's action-object ball -- a property of the production CEM configuration on an untrained bench, not (yet) evidence about the claim's content assertion. `what_would_answer`'s CONFIRMING branch ("a properly-powered paired-contrast gate ... restores production-settings mode-content persistence") presumes the content half is measurable on this bench; it is not, for the reasons above. Flagged as `evidence_discrepancy` on MECH-267 so governance can decide whether to annotate the claim's `what_would_answer` now or wait for the spike.

## 8. Identifiers and where things are

| item | state |
|---|---|
| `V3-EXQ-1005` | never reached `experiment_queue.json` or the coordinator DB; not burned. The successor may reuse it as `V3-EXQ-1005a` (the design changes: bench and positive control), which keeps this record unambiguous. |
| driver | `ree-v3/experiments/_scratch/v3_exq_1005_mech267_mode_content_location_separation.py` (design-complete, smoke-green, refused; docstring carries the verdict line). Moved out of `experiments/` so `audit_unqueued_experiment_scripts.py` does not report it as a forgotten script. |
| probes | `ree-v3/experiments/_scratch/exq1005_probe_elite_channel.py` (red-team's), `ree-v3/experiments/_scratch/exq1005_probe_aostd_clamp.py` (this session's) |
| IGW | IGW-20260905-238 completed with outcome USEFUL_LANDED (this record + the landed driver); IGW-20260907-236 was RESOLVE'd to 1005 by the 09-07 plan session -- superseded by the spike chip; a user disposition on both points here so the confirmer does not respawn a generic MECH-267 confirm. |
| claims | `igw-238-confirm-evidence-mech-267-lit-0-exq-1005` closed NOT QUEUED; `hopeful-solomon-01a60c*` closed. |
| chips | `chip-igw-20260905-238` and `chip-staleclaim-igw-238-confirm-evidence-mech-20260905T130405Z` resolved done (blocked-triage); campaign chip `chip-20260907-campaign-w4-s2-ratified-successors` unclaimed with item 0 dispositioned and A1..tail remaining. |
