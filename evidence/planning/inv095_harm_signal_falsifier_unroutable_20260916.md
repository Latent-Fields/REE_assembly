# INV-095: the pre-registered harm-signal falsifier is UNROUTABLE as written

**Generated:** 2026-09-16T01:37:00Z
**Session:** `igw-235-proposal-for-inv-095` (IGW-20260916-235, lane `experiment`, skill `/queue-experiment`)
**Proposal:** `EVB-1368` (`experimental`) -- marked `blocked_substrate` by this session
**Outcome:** REFUSED at `/queue-experiment` Step 4.5 (adversarial design review, verdict **BLOCKING**).
No experiment was queued. `V3-EXQ-1042` was reserved, then released unused; its driver was
written, smoke-tested, validator-clean, calibrated at full scale, and then **deleted** rather
than queued (CLAUDE.md: never leave an experiment script unqueued).

---

## 1. What was attempted, and why it looked runnable

INV-095 (Axiom 2, "existence has value sufficient to justify its continuation") splits into an
out-of-domain leg and a testable leg. The testable leg is named by the axiom's own text: *"this
axiom makes the harm gradient non-arbitrary... If existence had no value, harm signals would be
noise rather than information."* The claim pre-registers the contrast as:

- confirming -- replacing the harm signal with distribution-matched noise produces **measurable
  degradation** in E3 trajectory selection;
- falsifying -- it produces **no** measurable degradation, so the signal is architecturally
  decorative.

Evidence state at authoring (`claim_evidence.v1.json`): **0 experimental entries**, 5 literature
entries, `lit_conf` 0.83, `exp_conf` 0.0 -- i.e. exactly the `lit_only_above_cap` /
`missing_experimental_evidence` the IGW brief flagged.

The **behavioural** version was ruled out first, on measurement rather than on caution:

- **V3-EXQ-919** (MECH-321, 40 seeds, 2026-08-11) measured harm-aware selection's effect on
  executed task harm with the **intact** signal: `harm_delta_mean` -0.0037, `rel_improvement`
  -0.031, direction `weakens`; 21 of 40 seeds never decomposed. With the intact signal producing
  no behavioural effect, noise substitution has nothing to degrade.
- **V3-EXQ-800** (ARC-007, 2026-07-24) ran the closest behavioural ablation shape
  (`A2_RESIDUE_PERMUTED` / `A3_RESIDUE_FROZEN`) and self-routed `substrate_not_ready_requeue`
  with its non-vacuity gate RED in **every** arm (`executed_action_diversity`).

So a measurement-only design was built instead, reading the degradation at the E3 selector rather
than the actuator -- which the claim's own falsifier wording permits ("degradation in E3
trajectory selection"). It avoided both documented predecessor defects: V3-EXQ-533's
policy-blindness (`np.random.randint`, independent of the sensed latent, per
`failure_autopsy_V3-EXQ-059c-533_2026-07-26.md`) and V3-EXQ-059c's frozen random `z_world`
carrying four trained heads.

---

## 2. Why it was refused

`/queue-experiment` Step 4.5 red-team (model: **fable**; this session ran on Opus) returned
**BLOCKING**. Two findings were verified against source and against this session's own
full-scale calibration data, and both hold. Full review preserved in section 6.

### F1 -- the load-bearing criterion cannot fail

The DV was `rho_truth[arm]` = Spearman(candidate harm cost under `arm`, candidate TRUE cumulative
hazard exposure), and C1 required veridicality **degradation** from the intact arm.

`CausalGridWorldV2.reset()` re-draws hazard placement every episode, so a harm latent taken from
any *other* tick carries nothing about **this** tick's truth ordering. The numerator of any
degradation statistic is therefore structurally ~0, whatever the intact arm achieves. Measured
over the 20 state-uninformative cells of the 5-seed calibration (4 substituted arms x 5 seeds):

    max |rho_truth| over all state-uninformative cells = 0.1162

This defect survived a fix attempt, which is the part worth recording. C1 was first written as an
absolute drop (`rho_truth[A0] - rho_truth[arm] >= 0.10`); that was caught **before** the red-team
as a precondition-dominance failure (readiness gate R6 forces `rho_truth[A0] > 0.15`, so R6 GREEN
already implied the 0.10 drop -- cf. memory `feedback_precondition_can_dominate_its_criterion`)
and was replaced by a conjunction whose binding half was the scale-free retention ratio
`rho_truth[arm] / rho_truth[A0] <= 0.50`. The retention form removed C1's dependence on R6's
LEVEL but **not** the structural guarantee, because the numerator is still ~0:

    per-seed retention, shuffle / matched-noise / zero-information-constant arms
      seed 42   -0.0841  -0.2779  -0.2129
      seed 43   +0.0756  +0.0687  +0.0826
      seed 45   +0.0520  -0.1224  +0.0161
      seed 46   +0.0303  +0.0540  +0.1029
      seed 47   -0.0042  -0.0204  +0.0807

Every cell clears a 0.50 ceiling by an order of magnitude. **Two independent formulations of the
same criterion were both structurally satisfied.** That is the signature of a criterion whose
outcome is fixed by the environment's geometry rather than by anything about the substrate under
test.

### F2 -- the claim's own falsifying scenario routes AWAY from `weakens`

If REE's harm machinery really were "noise rather than information", the intact arm would not
track hazard: `rho_truth[A0] ~ 0`. That trips readiness gate R6 (`intact_rho_truth > 0.15`), the
seed becomes unreadable, and the run self-routes `substrate_not_ready_requeue` /
`non_contributory`.

So the state of the world the claim pre-registers as **falsifying** was routed by this design to
"instrument not ready". The driver's own docstring argued R6 was "a measurement precondition, not
a hidden verdict" -- that argument is wrong for this claim, and naming it here is the point: for
INV-095 specifically, "the intact signal does not track hazard" **is** the falsifier. `weakens`
was reachable only in the narrow band `rho_truth[A0]` in (0.15, ~0.24]; the five calibration seeds
sat at 0.29-0.68.

### F3 -- and the DV was narrower than the claim's language

P0 trains `HarmEncoder` to predict `harm_obs[12]` (hazard-at-agent, a coordinate of its own
input); P1 trains `harm_eval_z_harm_head` on the same label (calibration
`harm_eval_test_rho_vs_proximity` 0.988-0.998); ground truth is that same quantity un-normalised.
Substituting the input of a deterministic trained function changes its output; a PASS therefore
establishes "a trained regressor beats noise", and the step from there to "INV-095's named
architectural consequence holds for E3 trajectory **selection**" is a leap. `score_trajectory`
-- the actual selection score -- never entered the load-bearing criterion, because its F /
benefit / residue channels run on an untrained `z_world` (calibration:
`mean_harm_term_range_share_of_score` 0.95, i.e. the harm term dominated an untrained score).

### Minor findings, accepted

- **F4** the outcome was already observed on all five queued seeds (see section 4).
- **F5** R3 (`candidate_action_distinct_frac`, exhaustive product) and R4
  (`noise_dist_match_max_dev`, bank standardised to match exactly, measured 7.9e-07 vs a 0.25
  ceiling) cannot fail; defensible as construction stamps, but they must not be cited as
  rhetorical support for "every readiness gate GREEN".
- **F6** R1 certified the forward model on the measurement pool's own held-out tail -- the same
  ticks the DV is read on.
- **F7** the absolute 0.10 floor was not scaled to the intact level.

---

## 3. The durable findings this refusal DID produce

### 3a. z_harm_a cannot change E3's harm-channel candidate ranking -- by arithmetic

A source-level structural result about INV-095's `z_harm_a` half, independent of any experiment:

`z_harm_a`'s only path into E3 trajectory scoring is
`lambda_eff = lambda_ethical * (1 + affective_harm_scale * ||z_harm_a||)`
(`ree-v3/ree_core/predictors/e3_selector.py`, `score_trajectory`, ~line 1490) -- a **candidate-
uniform positive scalar gain** on the harm term. `compute_harm_forward_cost` (~line 1276) does not
take `z_harm_a` as an argument at all. A positive rescaling of a cost vector is order-preserving,
so it cannot move an argmin or a Spearman rho: **the affective harm stream is rank-invariant
within the harm channel on every substrate, at every seed.**

Confirmed at runtime on 5 seeds x 400 measurement ticks: substituting `z_harm_a` from another tick
left the harm-only DV **bit-identical** (`top1_change_rate` 0.000, retention 1.000). On the full
score it moved the argmin on 0.3% of ticks -- a scalar gain reweighting competing channels.

Consequence for INV-095: its falsifier names "z_harm_a / z_harm_s / ResidueField output" as
interchangeable ablation targets. For `z_harm_a` at the trajectory-ranking level that is not a
measurement question at all.

### 3b. The action-generic baseline is ~0 on this environment

Scoring candidates from a **constant** (pool-mean) harm latent -- zero state information -- gives
`rho_truth` 0.021 against an intact 0.517. There is essentially no action-generic shortcut
("moving is worse than staying") by which a state-blind ranking could track true hazard in this
env. This is what makes F1 structural rather than incidental: it is the environment's geometry,
not the substrate's competence, that fixes the criterion's outcome.

---

## 4. Pre-registration disclosure

This design was executed **at full scale, all five seeds, twice** (once pre-fix, once with the
corrected criteria) on the Mac during authoring -- not merely smoke-tested. Thresholds were all
pre-registered beforehand and none was changed in consequence, and no manifest was written to
`evidence/experiments/` (output went to a scratch path, so the indexer never saw it). But the
outcome on `darwin-arm64` was known before any queue decision, and that is a genuine weakening of
pre-registration, recorded rather than glossed.

It was also load-bearing in the right direction: the calibration is what produced the numbers in
F1 and section 3, and it caught the precondition-dominance defect and the per-seed-gating defect
(readiness had been gated on the worst cell ACROSS seeds, so one untrained seed would have vacated
all five -- the V3-EXQ-785 shape). Had the run been queued on smoke-testing alone, it would have
returned a confident PASS that no one had reason to doubt.

---

## 5. What is owed -- and its work-graph classification

**INV-095's testable leg is `complex (probe-gated)` -> now resolved to `complicated (buildable)`.**
The blocking substrate is not the harm machinery; it is the **absence of a trained competing
channel at the selection layer**:

- A discriminating test has to be read on `E3.score_trajectory`, where the harm term competes with
  F / benefit / residue, because that is the only place "the harm signal is load-bearing for
  selection" is a non-tautological question.
- That requires a trained `z_world` / E1 / E2 (via `act()` / `_e1_tick()` / `record_transition()`
  -- the pathway whose absence is the documented 032-family / 059c defect), and for the behavioural
  form, the action-commitment layer.
- With an untrained F the harm term simply dominates (measured: 0.95 of the cross-candidate score
  range), so the selection-level reading is unavailable, not merely noisy.

Route: `/implement-substrate`, not another `/queue-experiment` iteration on this claim. Until then
the claim's `what_would_answer` should not be read as prescribing a runnable measurement.

**Governance action owed on the claim itself (raised as a flag, not applied here):** INV-095's
pre-registered falsifier needs restating. As written -- "replacing the signal with noise produces
no measurable degradation" -- the falsifying state of the world is one in which the degradation
statistic is undefined (there is no veridicality to decrement), so no design can route it to
`weakens`. A restatement has to name the **selection-level** contrast against a trained competing
channel, and say what instrument-failure it is to be distinguished from.

**Also still owed, unchanged:** the ResidueField third of the falsifier. Deliberately out of scope
here; V3-EXQ-800 ran that shape and hit its own readiness wall, so it needs its own design.

---

## 6. Red-team review, preserved verbatim

The full adversarial design review (fable, 36 tool calls) is reproduced below. It is preserved in
this artifact because it was written to a worktree scratch path that will be garbage-collected,
and because its source citations are the evidence for sections 2 and 5.

# V3-EXQ-1042 adversarial design review (causal chain only)

Script: /Users/dgolden/REE_Working/ree-v3/experiments/v3_exq_1042_inv095_harm_signal_vs_noise_e3_ranking.py
Reviewed 2026-09-16. Facts only; no adjudication, no edits.

## Verified-sound (no finding)

- Manipulation reaches DV. `compute_harm_forward_cost` (e3_selector.py:1276-1305) reads
  `trajectory.actions` and `z_harm_s_current` only; script substitutes `zh_k` per arm at
  873-874 into a pure function; `traj` is shared and never re-rolled. No cache, no warmup
  state (commensurability default False config.py:1073; benefit default False :1206).
- `_true_hazard` (script 486-509) matches `step()` for this config: `_action_map` == ACTIONS
  (world_rule_shift_enabled default False, env:791; never permuted, so the end-of-collection
  snapshot at script:642 is correct); wall rule env:2418; border walls env:1543-1547;
  limb-failure revert env:2766-2769 off (default :242); action-block off (:374); reef off
  (:558); no hazard removal on contact (no `.remove` path); drift prob 0.0. Truth and DV sum
  the same cells t=1..3. `prox = ho[12]` is the 5x5 view centre = hazard_field[agent]/max
  (env:3805, index 2*5+2). `CausalGridWorldV2` factory (env:5373) forces the view on.
- P0/P1 train/measure split does not leak: split at tick 3360 = episode-28 boundary (40x120,
  0 nonfinite skips in calibration); `t_tr < split-1`, `t_te >= split` (script 712-713).
- `_spearman`: mergesort avg-ranks, degenerate -> 0.0, guarded on the intact side by R2.
- z_harm_a arithmetic invariance holds (score_trajectory :1488-1490 candidate-uniform gain).

## Findings

### F1 (family 4 + 2) -- C1 is IMPLIED by R6 plus the construction of the substitutes; a PASS carries no information beyond the gate
Claim: given a readable seed, `drop >= 0.10` follows arithmetically from `rho_A0 > 0.15`
because the substituted arms' rho_truth is ~0 by construction.
Source: R6 floor script:366 `R6_INTACT_RHO_TRUTH_FLOOR = 0.15`; C1 floor :368
`C1_VERIDICALITY_DROP_FLOOR = 0.10`; drop := rho_A0 - rho_arm (:925-926); C1 test :950-952;
readability requires A0 green incl. R6 (:1145-1148). The substitutes destroy the LAYOUT: env
`reset()` re-shuffles hazard placement every episode (env:1560-1640, `_rng.shuffle(available)`),
so a z from another tick (A1, 1/12 same-episode) or mu+noise (A2) carries no information about
THIS tick's truth ordering. Measured (scratch_1042/fullrun_manifest.json, 5 seeds):
rho_truth[A1] = -0.025/+0.047/+0.023/+0.016/-0.003; rho_truth[A2] = -0.082/+0.043/-0.055/
+0.029/-0.014. All |rho_arm| < 0.09. Hence drop >= 0.10 <=> rho_A0 >= ~0.10-0.19, i.e. the
gate. The only band where C1 can fail on a readable seed is rho_A0 in (0.15, ~0.24]; every
calibration seed sits at 0.29-0.68.
Not circular in the STATISTIC (R6 gates the level, C1 the decrement) but circular in the
IMPLICATION: R6 green => C1 green, unless the substitute retains veridicality, which the
per-episode layout re-draw prevents.
Confirmer: from fullrun_manifest.json, for every seed assert
`abs(rho_truth[arm]) < 0.10` for A1/A2, then `drop >= 0.10` is equivalent to `rho_A0 >= 0.20`
-- a one-line check on the table above. (Done: holds on 5/5 seeds.)

### F2 (family 3) -- The claim's own FALSIFYING scenario is routed to `non_contributory`, never `weakens`
Claim: if REE's harm signal really were "noise rather than information", rho_truth[A0] ~ 0,
R6 goes red, the seed is unreadable, and the run self-routes `substrate_not_ready_requeue` /
`non_contributory` (script:1189-1198). `weakens` (:1212-1226) is reachable only in F1's
marginal band. So "signal is decorative" cannot produce the direction the claim pre-registers
for it; the design converts the falsifier into an instrument fault.
Source: :1145-1148 readability; :1189-1192 branch; :245-253 docstring says an R6-red run "is
NOT a verdict on INV-095".
Confirmer: paper walk -- set rho_A0 = 0.05 on all seeds; trace to `direction`. It is
`non_contributory`, with drop values never consulted.

### F3 (family 3) -- The DV is the harm evaluator's own output, not "E3 trajectory selection"; PASS reduces to "a regressor trained on its own input coordinate beats noise"
Claim: P0 trains HarmEncoder to predict `prox = ho[12]`, which is coordinate 12 of its own
input (script:602, :677-690); P1 trains `harm_eval_z_harm_head` on the same label from the
frozen latent (:731-752); truth is the un-normalised same quantity summed along the path
(:486-509). Calibration `harm_eval_test_rho_vs_proximity` = 0.988-0.998, i.e. eval o encoder
is near-identity on the label; `zharm_pool_eff_rank` = 4.3-4.7 of 32 dims. The only
non-trivial learned element is ResidualHarmForward's action-conditional delta (stack.py:
528-576). Substituting the input of a deterministic function of (z, actions) changes its
output tautologically; whether the change is a DEGRADATION depends only on whether the
intact z tracks hazard -- which is what R6 already certifies (F1). Selection itself
(`score_trajectory`, argmin over J) is reported-only and its F/residue channels run on
untrained z_world (:87-90, :1406-1414). The step from "harm-term veridicality dropped" to
"INV-095's named consequence holds for E3 trajectory selection" (:1204-1211) is a leap: the
result is a property of any supervised regressor, not of REE's harm machinery.
Confirmer: replace `harm_enc`+`hfwd`+`eval_head` with any generic MLP regressor on harm_obs
trained on the same label; the run PASSes identically. Cheaper: note that no arm ever
consults `score_trajectory` in `c1_met` (:950-952).

### F4 (family 3) -- The result is already known: all 5 seeds ran at full scale during authoring
Claim: docstring :160-170 discloses ONE seed (42) run at full scale and says "the other four
seeds are unseen". scratch_1042/fullrun.py ran `run_experiment(m.SEEDS, ...)` (all 5) with the
queued constants; fullrun.log shows 5x `verdict: PASS`, n_readable 5, c1_seeds_met 5, every
seed's drop 0.32-0.70. The script is deterministic per seed (`reset_all_rng(seed)` :656,
`RandomState(10_000 + seed)` :801; no multinomial, so the cross-platform caveat does not
apply). The queued "evidence" run reproduces a known PASS; the disclosure is inaccurate.
Confirmer: `grep -c 'verdict: PASS' scratch_1042/fullrun.log` -> 5; compare per-seed
`[P2]` lines in fullrun.log to the future manifest.

### F5 (family 2) -- Two readiness gates cannot fail (stamps, not gates)
R4: noise bank standardised to match mu/sd exactly (:821-823, admitted :814-820);
measured 6e-07 vs ceiling 0.25. R3: `distinct_frac` = 1.0 by `itertools.product` (:478, :794).
Both are counted in "every readiness gate GREEN" (:1217-1220) that licenses `weakens`.
Confirmer: R4 < 1e-5 on every seed in fullrun_manifest.json.

### F6 (family 4, minor) -- R1 is certified on the measurement pool's own transitions
R1 uses `t_te` (:713, ticks >= split) and the measurement pool is subsampled from the same
tail (:781). Not circular with C1 (different statistic), but the forward-model gate is
denominated on the data it must license. Also `true_d.std()` (:767) is a scalar over the
whole [n, 32] matrix, so a per-dimension-heterogeneous residual can pass.
Confirmer: `set(pool) <= set(t_te) | set(t_te+1)` -- true by construction.

### F7 (family 2, minor) -- Absolute drop floor not scaled to intact level; degenerate substitute reads as maximal degradation
A seed with rho_A0 = 0.16 and rho_arm = 0.07 (56% of veridicality lost) fails C1 and counts
toward `weakens`. Conversely, R2 checks only the INTACT arm's cross-candidate range (:883,
:909); a constant cost vector in a substituted arm gives `_spearman` -> 0.0 (:418-419) and
therefore drop = rho_A0, a guaranteed C1 pass for that arm. Neither bites on the calibration
seeds; both are routes to an unattributable verdict on a different seed set.

## Overall verdict

BLOCKING. The load-bearing criterion C1 does not discriminate within this design: given a
readable seed it is implied by the readiness gate R6 together with the per-episode layout
re-draw that makes every substitute state-decorrelated (F1, measured on 5/5 seeds), and the
claim's pre-registered falsifying scenario is routed to `non_contributory` rather than to
`weakens` (F2). Independently, the outcome is already observed at full scale on all five
queued seeds (F4). Hedge, stated: C1 is formally fail-able in the band rho_A0 in (0.15, ~0.24];
if that band is read as "can discriminate", the verdict is CONTESTED on F1-F4 rather than
BLOCKING. Either way the run as designed answers "does a trained regressor beat noise",
not "does REE's harm machinery implement INV-095's consequence for E3 selection" (F3).

---

## 7. Addendum (2026-09-16T01:55Z): the blocker was already owned, and Step 2.5c should have said so

Two corrections to sections 2 and 5, made after the refusal was already committed.

### 7a. `blocked_by` relinked to the existing owner -- no new substrate id, no chip

Section 5 named the owed build as if it were new. It is not. The owning entry already exists:

**`f_dominance_conversion_ceiling`** (`substrate_queue.json`; MECH-439; severity **corrupting**;
`ready: false`), titled *"F-dominance committed-selection variance monopoly (MECH-439):
rebalance/bound the primary harm/goal score F so per-candidate diversity converts"*, with

    substrate_paths: ree_core/predictors/e3_selector.py::score_trajectory
                     ree_core/residue/field.py::add_residue
                     ree_core/residue/field.py::RBFLayer.forward
    unblocks_claims: ARC-062, ARC-063, ARC-107, MECH-260, MECH-263, MECH-280, MECH-281,
                     MECH-309, MECH-313, MECH-341, MECH-439, MECH-445..449, Q-045, Q-078, SD-037

`score_trajectory` is the exact function INV-095's selection-level reading has to be taken on, and
"bound F so per-candidate diversity converts" is exactly the release condition this refusal
derived independently. So `blocked_by` has been relinked from an invented id
(`z_world-trained-competing-channel-at-selection-layer`) to `[f_dominance_conversion_ceiling,
MECH-439]`, and **no `/implement-substrate` chip was spawned** -- it would duplicate an open entry
whose own status string records the conversion route of record as EXHAUSTED (709/711/713 autopsy
2026-07-05, "no new build owed"). INV-095 should be added to that entry's `unblocks_claims` by
governance; this session did not edit the substrate entry.

This also reframes the refusal usefully: INV-095's testable leg is not blocked on something
nobody has looked at. It is blocked behind the **known conversion ceiling**, alongside 19 other
claims. That is a much better-understood place to be blocked, and it is why the honest route is
governance restating the falsifier (GFLAG-0291) rather than anyone building anything new.

### 7b. Step 2.5c's gate should have fired here, and silently did not -- fleet-wide

The Step 2.5c check this session ran (section 2's call trace) concluded "no open `corrupting`
entry overlaps". That conclusion was WRONG, and the reason is a defect in the gate's own recipe
rather than in this session's trace.

The recipe classifies an entry CLOSED by **substring**:

    CLOSED = ('implemented','implemented_validated','validated','wontfix','closed_aleatoric')
    if 'pending' in s1 or 'pending' in s2: pass
    elif any(m in s1 or m in s2 for m in CLOSED): continue

`f_dominance_conversion_ceiling`'s `status` is a **619-character prose blob**, and it contains the
substring `validated` -- inside `mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional`. It has
no `pending`, so it is skipped as closed despite `ready: false` and severity `corrupting`.

Measured over the live `substrate_queue.json`: **6 entries with `substrate_paths` and
`ready: false` are hidden this way, 3 of them at `corrupting` severity** --

    SD-056                                          corrupting
    f_dominance_conversion_ceiling                  corrupting
    MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION     corrupting
    INF-ENV-001                                     degrading
    SD-E3-SCORER-COMPLETION                         degrading
    waypoint-proximity-field-observable             degrading

`SD-056` and `f_dominance_conversion_ceiling` both name paths in the E3 scorer / residue field,
which a large fraction of drivers touch. Step 2.5c's own prose says the check "fails toward
blocking, not toward silence"; on these six it does the exact opposite, for every session that
runs it. Chipped separately as an infrastructure defect nothing audits.

Suggested direction (not implemented here -- it is a standing-rule/recipe change and needs its own
GOV-HELDOUT-1 check): stop inferring openness from free-text status substrings. Prefer the
structured fields the entries already carry (`ready`, `severity`), and treat a status that is
prose rather than an enum as OPEN by default, which is the direction the gate claims to fail in.
