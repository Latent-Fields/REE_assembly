# ==========================================================================
# WITHHELD DRIVER -- NOT QUEUED, NOT RUNNABLE AS EVIDENCE, DO NOT COPY INTO
# ree-v3/experiments/ AND QUEUE IT WITHOUT READING THE REFUSAL FIRST.
#
# Authored 2026-09-24 for V3-EXQ-671c (MECH-025b, proposal EXP-1283). It
# passed `validate_experiments.py --strict` and a --dry-run smoke, and it
# implements the claim's what_would_answer P1-P4 correctly. It was REFUSED at
# /queue-experiment Step 4.5 (adversarial red-team, fable) on a BLOCKING
# finding that is about the SUBSTRATE, not about this code:
#
#   MECH-025b's dependent variable -- residue accumulated per unit harm --
#   has NO precision input anywhere in its causal chain, so neither C1 nor C2
#   can discriminate the claim under ANY outcome. Verified from source:
#     * ResidueField.accumulate (ree_core/residue/field.py:697-704) computes
#       magnitude = |harm_magnitude| * accumulation_rate, optionally scaled by
#       world_delta. No precision, variance or commitment term. It is the ONLY
#       write site for total_residue.
#     * Owned harm is a CONSTANT: agent_caused_hazard sets
#       harm_signal = -contaminated_harm = -0.4
#       (ree_core/environment/causal_grid_world.py:2647). The driver's
#       hazard_harm=0.02 is a DIFFERENT parameter and applies to
#       env_caused_hazard, which the `owned` filter excludes.
#     * The only other contributor is E3.post_action_update
#       (ree_core/predictors/e3_selector.py:4691-4694), which accumulates a
#       hardcoded harm_magnitude=1.0 when a committed trajectory is held --
#       binary, never graded by precision.
#   With accumulation_rate=0.1 the per-window DV reduces exactly to
#       dv = (0.04*m + 0.10*I) / (0.4*m) = 0.1 + 0.25*I/m
#   where I in {0,1} is whether the commit tick itself landed on owned harm
#   and m is the owned-harm count in the window. Precision cannot enter.
#
# What is owed first is a substrate item -- precision-weighted residue
# accumulation -- not another estimator. Full refusal, verification and the
# secondary findings:
#   REE_assembly/evidence/planning/mech025b_within_seed_fisherz_design_staged_20260924.md
#
# WHAT IS STILL GOOD HERE, and why this file is kept rather than deleted:
# the within-seed Fisher-z estimator, the commit-window sampling unit (which
# fixes a real latch defect in 671b), the commit-time capture of
# precision_margin_norm, and the derived C1_MIN_FISHER_WEIGHT joint-
# satisfiability bound are all correct and reusable the moment the substrate
# gap is closed. Known defect to fix before reuse: the eval loop drops the
# `agent.eval()` call that 671b had at its line 392.
# ==========================================================================

"""
V3-EXQ-671c -- MECH-025b: Precision-Responsibility Attribution Linkage
(WITHIN-SEED Fisher-z re-estimator; supersedes V3-EXQ-671b)

Claims: MECH-025b

WHY THIS RETEST. V3-EXQ-671b (2026-08-03) is recorded `weakens/standard`, and
GFLAG-0151 (resolved 2026-09-10) established that read is a SEED-CONFOUNDED
artifact: 671b pooled its samples across 4 seeds whose per-seed precision
spreads differ ~37x (160611.76 / 5674.23 / 4300.25 / 0.00), so its pooled
median split approximates a seed-identity split. Every within-seed constituent
has the opposite sign to the pooled estimate (per-seed r +0.0505 / +0.1017 /
+0.0651 / 0.0000 against a pooled -0.0446), and 2 of the 3 non-degenerate seeds
clear the 1.1 ratio bar the pooled ratio misses. MECH-025b's what_would_answer
was rewritten (P1-P4) to require a within-seed estimator for future runs. This
driver is that estimator.

WHAT IS UNCHANGED FROM 671b (deliberately -- this is a lettered instrument fix,
not a new scientific question): the environment, the config, the warmup/eval
schedule, `_train`, `_compute_world_forward_r2`, and 671a's four instrument
fixes (update_residue called after every env.step; is_committed sourced from
SelectionResult.committed; owned sourced from info["transition_type"]; the
harm_signal < 0 AND owned eval filter). Those are copied verbatim.

FOUR CORRECTIONS OVER 671b
--------------------------

(P3a) THE ESTIMATOR IS WITHIN-SEED. Primary statistic is a per-seed Pearson r,
      Fisher-z averaged across seeds with (n-3) weights; the median split for
      the ratio test is taken WITHIN each seed; any seed with fewer than
      MIN_EVENTS_PER_SEED committed harm-events is excluded from the primary
      estimator and reported separately (671b's seed 3 contributed n=1 with a
      fill-value correlation of 0.0 into a pooled n of 179). A pooled statistic
      is still computed, but ONLY as a diagnostic, and pre-registration says a
      sign disagreement between pooled and within-seed resolves in favour of
      the within-seed estimate.

(P3b) THE REGRESSOR IS SCALE-FREE AND IS READ AT COMMIT TIME. 671b used raw
      `E3.current_precision`. This driver uses `precision_margin_norm`
      (= clamp(1 - commit_variance/effective_threshold, 0, 1); ree-v3 48f85f0,
      2026-09-02, i.e. 32 days AFTER 671b ran, so 671b could not have used it).
      It is bounded [0,1] by construction, so it is comparable across seeds
      without the 37x rescaling that confounded 671b.

      THE TIMING HALF OF THIS FIX MATTERS AS MUCH AS THE SCALE HALF, and was
      found by source-tracing while authoring this driver (it is NOT in the
      claim's P1-P4, nor in this experiment's pre-flight). `REEAgent.
      update_residue()` -- which 671a added, and which 671b calls after EVERY
      env.step() -- reaches `E3.post_action_update()` at agent.py:11070, which
      calls `update_running_variance()`. So running_variance, and therefore
      `current_precision`, moves on EVERY env tick, while `select()` (and the
      commit decision) fires only on an E3 tick (~1 in 10; measured 10.5 steps
      per selection in this env). ree_core/utils/config.py:1281 states the same
      asymmetry directly. 671b read `agent.e3.current_precision` at the env
      step where the HARM landed -- up to ~10 env ticks after the commit
      decision its `held_committed` latch attributes that harm to, and AFTER
      the harm's own prediction error has already been folded into the EMA.
      Its regressor is therefore not "the precision at which the action was
      committed" (the quantity MECH-025b names) but the variance EMA measured
      downstream of the dependent variable's own cause -- and because a harm
      event RAISES prediction error, raises running_variance and so LOWERS
      current_precision, the contamination has a negative sign, the direction
      671b's pooled estimate actually reported.
      `precision_margin_norm` is captured INSIDE the `select()` call that made
      the commit decision, so it is pre-harm by construction.

(P3c) ONE OBSERVATION PER COMMIT, NOT PER ENV STEP. 671b's `held_committed`
      latches across the ~10 env steps between E3 ticks and it appended one
      sample per qualifying env step, so two harm events inside one commit
      window were recorded as two independent observations of one selection.
      This driver accumulates residue and harm over the window a single
      selection governs and emits ONE observation per fresh committed
      selection, and records `n_latched_ticks` / `n_commit_windows` so the
      denominator is auditable rather than inferred from len(samples).
      (Harm events are rare relative to selections -- 671b logged 29/72/77
      against ~1000 selections per seed -- so this is expected to change n
      only modestly; it is recorded so that it is checkable, not assumed.)

(P4) THE PASS BAR IS DERIVED, NOT INHERITED. `C1 > 0.15` was carried unchanged
      from 671 -> 671a -> 671b and was never derived from an expected effect
      size. It is replaced by C1_BAR = 0.10, pre-registered as a STATED MINIMUM
      PRACTICALLY-RELEVANT EFFECT (what_would_answer P4, route 2), on a human
      decision recorded 2026-09-24 (decision chip chip-20260924-mech025b-c1-bar,
      option A). Route 1 (a measured range-restriction correction) was costed
      and rejected: the unrestricted margin distribution is unbounded below on
      uncommitted ticks, so S/s is set by an arbitrary tail rather than a
      stable population SD, and a full-scale pilot to measure it costs about
      what this experiment costs. Significance is carried SEPARATELY by the
      what_would_answer's own requirement that the 95% CI exclude 0 -- the bar
      is an effect-size floor, not a significance test. C2's bar stays 1.1 on
      >= 4/5 qualifying seeds (P4 challenges C1 only; the CONFIRMING clause
      restates the ratio bar unchanged).

DISCRIMINATIVE PAIR (EXP-1283 `dispatch_mode: discriminative_pair`). The
falsifier is a single-condition within-seed correlation, and the substrate has
NO discrete precision mode (no `precision_mode` / `high_precision` /
`action_precision` anywhere in ree_core/; MECH-025b's own INSTRUMENT NOTE says
the claim's "high-precision action mode" is testable only as a LEVEL), so a
forced high/low-precision arm is not constructible. The control is therefore a
WITHIN-SEED LABEL PERMUTATION of the regressor on the identical seeds: it
satisfies `matched_shared_seeds` / `min_shared_seeds: 2` by construction and
adds no substrate condition, so it cannot change what the substrate measures.
It is reported as a control (its 95th percentile and an empirical p-value),
NOT used as the pass bar -- using it as the bar would duplicate the
CI-excludes-0 requirement and would not answer P4's demand for an
effect-size-grounded bar.

SCOPE LIMIT ON A PASS (from the claim's own what_would_answer, not decorative).
A PASS confirms that precision SCALES RESIDUE WEIGHT. It does NOT confirm the
claim's stated rationale that higher precision implies higher ETHICAL
ACCOUNTABILITY -- that premise is INV-012 Leg 0, recorded as CURRENTLY UNMET.
Do not re-derive Leg 0 here. A PASS promotes the mechanistic half and leaves
the accountability bridge explicitly gated.

STEP 2.5c DISPOSITION (substrate-path overlap, measured 2026-09-24). Two OPEN
`corrupting` substrate_queue entries name files this driver imports, and BOTH
were checked to be unreachable in this driver's configuration rather than
argued away:
  - `contextmemory-write-path-addressing-degeneracy`
    (ree_core/predictors/e1_deep.py::ContextMemory.write): the sense()-path
    call at agent.py:5696 is gated on `sd016_writepath_mode`, which defaults
    to "off" and which this driver never sets. Measured: 0 of 16 slots
    occupied across 3 seeds x 1200 sense() calls (occupied_slots() counts
    slots written at least once, so 0 means write() was never called).
  - `SD-PP-B5-z-world-per-step-displacement-range`
    (ree_core/predictors/e2_fast.py::compute_world_interventional_loss): that
    function has zero callers anywhere in ree_core, and this driver trains the
    world-forward with a plain F.mse_loss (see _train).
Several `degrading` entries overlap and are recorded in the queue entry note.

SLEEP DRIVER: not applicable (no sleep flags set).

Red-team verdict is recorded in the queue entry note and below.
RED-TEAM: see queue entry note for V3-EXQ-671c.
"""

import sys
import math
import random
from pathlib import Path
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import torch
import torch.nn.functional as F
import torch.optim as optim

from ree_core.agent import REEAgent  # noqa: E402
from ree_core.environment.causal_grid_world import CausalGridWorldV2  # noqa: E402
from ree_core.utils.config import REEConfig  # noqa: E402
from experiment_protocol import emit_outcome  # noqa: E402
from experiments.pack_writer import write_flat_manifest  # noqa: E402
from experiments._metrics import (  # noqa: E402
    check_degeneracy,
    dv_headroom_check,
    p0_readiness_gate,
    P0NotReady,
)
from experiments._lib.z_goal_stream import ZGoalStreamAccumulator  # noqa: E402




EXPERIMENT_TYPE = "v3_exq_671c_mech025b_precision_responsibility"
CLAIM_IDS = ["MECH-025b"]
EXPERIMENT_PURPOSE = "evidence"
SUPERSEDES = "v3_exq_671b_mech025b_precision_responsibility_20260803T022036Z_v3"

# 10 seeds at 671b's per-seed scale. Derived from POWER, not from the
# what_would_answer's literal ">= 5 seeds": the CONFIRMING clause requires the
# 95% CI on the Fisher-z average to exclude 0, and at the effect size 671b's
# own per-seed table implies (Fisher-z average r = +0.0778) that needs
# sum(n_i - 3) ~= 632. 671b had 169. Ten seeds at 671b's observed per-seed
# event counts (29/72/77) puts sum(n-3) in the 600-700 range. At the literal 5
# seeds, sum(n-3) ~= 345 and the CI still spans 0 -- the run would be formally
# valid and yet unable to return EITHER verdict, which is the outcome this
# seed count exists to avoid.
SEEDS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- PRE-REGISTERED THRESHOLDS (fixed before the run; never derived from it) --

# C1: stated minimum practically-relevant effect (what_would_answer P4, route
# 2), set by human decision 2026-09-24 (chip-20260924-mech025b-c1-bar, option
# A). Replaces the never-derived 0.15 inherited by 671/671a/671b. NOTE it sits
# ABOVE the +0.0778 that 671b's own per-seed table yields under this estimator,
# so it is a genuine test rather than a bar the existing data already clears.
C1_BAR = 0.10

# C2: unchanged from 671/671a/671b. P4 challenges C1 only, and the CONFIRMING
# clause restates the ratio bar as 1.1 on >= 4/5 qualifying seeds.
C2_BAR = 1.1
C2_SEED_FRACTION_REQUIRED = 0.8  # ">= 4/5 of qualifying seeds"

# DERIVED, never typed as a literal: C1 has TWO load-bearing parts -- an effect
# floor (r > C1_BAR) and the what_would_answer's own significance requirement
# (95% CI excludes 0). They are JOINTLY satisfiable only above a minimum total
# Fisher weight. The CI on z is z +- 1.96/sqrt(W); it excludes 0 at exactly
# z = atanh(C1_BAR) iff 1.96/sqrt(W) < atanh(C1_BAR), i.e.
#     W > (1.96 / atanh(C1_BAR))^2
# At C1_BAR = 0.10 that is W > 381.6, so W >= 382. BELOW THIS THE RUN CANNOT
# PASS NO MATTER WHAT THE DATA SAY -- the two halves of C1 contradict each
# other -- which is a substrate_not_ready_requeue, not a null. This is why the
# seed count is 10 rather than the what_would_answer's literal 5: 671b's four
# seeds gave W = 169.
C1_MIN_FISHER_WEIGHT = math.ceil((1.96 / math.atanh(C1_BAR)) ** 2)

# Step 2.5c / lint disposition, on the record as the lint asks. This driver
# never enables the ContextMemory write path at all: the sense()-path call at
# agent.py:5696 is gated on `sd016_writepath_mode`, which defaults to "off" and
# which this driver never sets. Measured 2026-09-24 in this exact config: 0 of
# 16 slots occupied across 3 seeds x 1200 sense() calls (occupied_slots() counts
# slots written at least once, so 0 means write() was never called). The DV here
# is residue accumulated per unit harm, not bank occupancy or slot content, so
# it cannot depend on write addressing. The lint fires on this file only because
# the docstring RECORDS that measurement.
CONTEXTMEMORY_WRITE_ENABLEMENT_EXEMPT = (
    "write path never enabled (sd016_writepath_mode defaults 'off' and is never "
    "set here); measured 0/16 slots occupied across 3 seeds x 1200 sense() calls; "
    "DV is residue-per-harm, not bank occupancy"
)

# what_would_answer P3: a seed with fewer than this many committed harm-events
# is EXCLUDED from the primary estimator and reported separately.
MIN_EVENTS_PER_SEED = 20
# what_would_answer FALSIFYING clause: ">= 5 seeds each carrying >= 20 events".
MIN_QUALIFYING_SEEDS = 5

# P0-1 (unchanged from 671a/671b): residue must actually move under committed,
# agent-owned harm or the whole readout is vacuous.
RESIDUE_FLOOR = 1e-6

# P0-2 (NEW in 671c). Within-seed spread of the REGRESSOR, worst seed.
# This floor is STRUCTURAL, not empirically calibrated, and that is the point:
# precision_margin_norm is normalized to [0, 1] by construction, so "1% of the
# regressor's full range" is a scale-free statement about leverage that means
# the same thing on every seed and every substrate. 671b's equivalent floor had
# to be hand-calibrated (PRECISION_VARIANCE_FLOOR = 1.0 in units of
# 1/running_variance) precisely because its regressor had no bounded range.
# This gate closes a degeneracy mode NO run in this lineage could previously
# detect: because margin = 1 - commit_threshold_variance/current_precision is a
# saturating transform, current_precision spread is LARGEST exactly when the
# margin is most compressed against its ceiling, so 671a/671b's raw-precision
# spread gate would read "ample variance" on a margin that is effectively
# pinned. Worst-seed (not mean) per the manifest worst-cell convention.
MARGIN_SPREAD_FLOOR = 0.01

# P0-3 (NEW in 671c): the regressor must actually be emitted. precision_margin_
# norm is set only on the world-variance commit branch (e3_selector.py:4059);
# the harm-variance branch leaves the pre-seeded -1.0. This driver never passes
# a harm bridge, so the fraction of committed windows carrying a valid margin
# must be 1.0; a floor below 1.0 would let a silent branch flip pass.
MARGIN_AVAILABILITY_FLOOR = 1.0

# Within-seed label-permutation control (the EXP-1283 discriminative pair).
# Reported, never gating.
PERMUTATION_DRAWS = 2000
PERMUTATION_SEED = 20260924
def _action_to_onehot(action_idx: int, n: int, device) -> torch.Tensor:
    v = torch.zeros(1, n, device=device)
    v[0, action_idx] = 1.0
    return v


def _mean_safe(lst: List[float]) -> float:
    return float(sum(lst) / len(lst)) if lst else 0.0


def _pearson_correlation(x: List[float], y: List[float]) -> float:
    """Compute Pearson correlation coefficient between two lists."""
    if len(x) < 2 or len(y) < 2 or len(x) != len(y):
        return 0.0
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denom_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    denom_y = sum((y[i] - mean_y) ** 2 for i in range(n))
    if denom_x < 1e-9 or denom_y < 1e-9:
        return 0.0
    return numerator / ((denom_x * denom_y) ** 0.5)



# --- WITHIN-SEED ESTIMATOR (what_would_answer P3) ---------------------------


def _fisher_z(r: float) -> float:
    """atanh with the r -> +-1 singularity clamped."""
    r = max(-0.999999, min(0.999999, float(r)))
    return math.atanh(r)


def _fisher_z_inv(z: float) -> float:
    return math.tanh(float(z))


def _within_seed_fisher_z(
    per_seed: List[Dict],
) -> Dict:
    """Primary estimator: per-seed Pearson r, Fisher-z averaged with (n-3)
    weights across QUALIFYING seeds only.

    `per_seed` entries need `seed`, `n_events`, `correlation`. A seed with
    n_events < MIN_EVENTS_PER_SEED is excluded (P3) and reported separately.
    Returns the back-transformed point estimate, the 95% CI, and the weights,
    so a reader can re-derive every number without the raw samples.
    """
    qual = [s for s in per_seed if s["n_events"] >= MIN_EVENTS_PER_SEED]
    excluded = [s["seed"] for s in per_seed if s["n_events"] < MIN_EVENTS_PER_SEED]
    if not qual:
        return {
            "r_fisher_z": 0.0, "z_mean": 0.0, "se": 0.0,
            "ci_low": 0.0, "ci_high": 0.0, "ci_excludes_zero": False,
            "weight_total": 0.0, "n_qualifying_seeds": 0,
            "qualifying_seeds": [], "excluded_seeds": excluded,
            "estimable": False,
        }
    weights = [float(s["n_events"] - 3) for s in qual]
    wsum = sum(weights)
    if wsum <= 0:
        return {
            "r_fisher_z": 0.0, "z_mean": 0.0, "se": 0.0,
            "ci_low": 0.0, "ci_high": 0.0, "ci_excludes_zero": False,
            "weight_total": 0.0, "n_qualifying_seeds": len(qual),
            "qualifying_seeds": [s["seed"] for s in qual],
            "excluded_seeds": excluded, "estimable": False,
        }
    z_mean = sum(w * _fisher_z(s["correlation"]) for w, s in zip(weights, qual)) / wsum
    se = 1.0 / math.sqrt(wsum)
    lo_z, hi_z = z_mean - 1.96 * se, z_mean + 1.96 * se
    lo, hi = _fisher_z_inv(lo_z), _fisher_z_inv(hi_z)
    return {
        "r_fisher_z": _fisher_z_inv(z_mean),
        "z_mean": z_mean,
        "se": se,
        "ci_low": lo,
        "ci_high": hi,
        "ci_excludes_zero": bool(lo > 0.0 or hi < 0.0),
        "weight_total": wsum,
        "n_qualifying_seeds": len(qual),
        "qualifying_seeds": [s["seed"] for s in qual],
        "excluded_seeds": excluded,
        "estimable": True,
    }


def _within_seed_ratio(margins: List[float], dv: List[float]) -> float:
    """High/low residue-per-harm ratio on a median split taken WITHIN this
    seed (P3). 671b took the split on the POOLED list, which with a 37x
    cross-seed spread is close to a seed-identity split."""
    if len(margins) < 4:
        return 0.0
    med = sorted(margins)[len(margins) // 2]
    hi = [dv[i] for i in range(len(margins)) if margins[i] > med]
    lo = [dv[i] for i in range(len(margins)) if margins[i] <= med]
    if not hi or not lo:
        return 0.0
    mean_hi, mean_lo = _mean_safe(hi), _mean_safe(lo)
    return mean_hi / max(mean_lo, 1e-6)


def _permutation_control(
    per_seed_samples: List[Dict],
    observed_z: float,
    draws: int = PERMUTATION_DRAWS,
) -> Dict:
    """CONTROL ARM (EXP-1283 discriminative_pair): shuffle the regressor WITHIN
    each qualifying seed, recompute the same Fisher-z average, repeat.

    Matched by construction -- identical seeds, identical DV values, identical
    n. Reported (95th percentile + empirical p) and explicitly NOT used as the
    pass bar: it is a significance instrument and would duplicate the
    CI-excludes-0 requirement rather than answer P4's effect-size question.
    """
    qual = [s for s in per_seed_samples if len(s["margins"]) >= MIN_EVENTS_PER_SEED]
    if not qual:
        return {"ran": False, "reason": "no qualifying seeds", "draws": 0}
    rng = random.Random(PERMUTATION_SEED)
    null_z = []
    for _ in range(draws):
        zs, ws = [], []
        for s in qual:
            m = list(s["margins"])
            rng.shuffle(m)
            r = _pearson_correlation(m, s["dv"])
            w = float(len(m) - 3)
            if w > 0:
                zs.append(w * _fisher_z(r))
                ws.append(w)
        if ws:
            null_z.append(sum(zs) / sum(ws))
    if not null_z:
        return {"ran": False, "reason": "no draws produced a statistic", "draws": 0}
    null_z.sort()
    idx95 = min(len(null_z) - 1, int(0.95 * len(null_z)))
    n_ge = sum(1 for z in null_z if z >= observed_z)
    return {
        "ran": True,
        "draws": len(null_z),
        "null_z_p95": float(null_z[idx95]),
        "null_r_p95": float(_fisher_z_inv(null_z[idx95])),
        "null_z_mean": float(sum(null_z) / len(null_z)),
        "observed_z": float(observed_z),
        "p_empirical": float((n_ge + 1) / (len(null_z) + 1)),
        "note": (
            "within-seed label permutation of precision_margin_norm; matched "
            "seeds/DV/n by construction. Reported as the EXP-1283 "
            "discriminative-pair control, NOT used as the C1 bar."
        ),
    }


def _worst_cell(rows: List[Tuple[int, float]]) -> Tuple[float, Optional[int]]:
    """Return (minimum value, owning seed). Manifest worst-cell convention:
    a precondition whose `met` is an all()-style claim must report the WORST
    cell, not the mean, or the indexer's recompute passes on an in-band mean
    that masks an out-of-band seed."""
    if not rows:
        return 0.0, None
    v, s = min(rows, key=lambda t: t[1])[1], min(rows, key=lambda t: t[1])[0]
    return float(v), int(s)
def _train(
    agent: REEAgent,
    env: CausalGridWorldV2,
    optimizer: optim.Optimizer,
    wf_optimizer: optim.Optimizer,
    harm_eval_optimizer: optim.Optimizer,
    num_episodes: int,
    steps_per_episode: int,
    world_dim: int,
) -> Dict:
    """Standard full-pipeline training to get functional E3 + E2.world_forward.

    UNCHANGED from V3-EXQ-671/671a: C4 (world_forward_r2) and C5
    (harm_pred_std) were NOT degenerate in either prior attempt -- the defect
    was isolated to the eval loop's residue wiring, not training.
    """
    agent.train()
    harm_buf_pos: List[torch.Tensor] = []
    harm_buf_neg: List[torch.Tensor] = []
    wf_buf: List[Tuple[torch.Tensor, torch.Tensor, torch.Tensor]] = []
    total_harm = 0
    e3_tick_total = 0

    for ep in range(num_episodes):
        flat_obs, obs_dict = env.reset()
        agent.reset()
        z_world_prev: Optional[torch.Tensor] = None
        action_prev: Optional[torch.Tensor] = None
        z_self_prev: Optional[torch.Tensor] = None

        for _ in range(steps_per_episode):
            obs_body = obs_dict["body_state"]
            obs_world = obs_dict["world_state"]
            latent = agent.sense(obs_body, obs_world)

            if z_self_prev is not None and action_prev is not None:
                agent.record_transition(z_self_prev, action_prev, latent.z_self.detach())

            ticks = agent.clock.advance()
            e1_prior = (
                agent._e1_tick(latent) if ticks.get("e1_tick", False)
                else torch.zeros(1, world_dim, device=agent.device)
            )
            candidates = agent.generate_trajectories(latent, e1_prior, ticks)
            theta_z = agent.theta_buffer.summary()
            z_world_curr = latent.z_world.detach()

            if ticks.get("e3_tick", False) and candidates:
                e3_tick_total += 1
                result = agent.e3.select(candidates, temperature=1.0)
                action = result.selected_action.detach()
                agent._last_action = action
            else:
                action = agent._last_action
                if action is None:
                    action = _action_to_onehot(
                        random.randint(0, env.action_dim - 1), env.action_dim, agent.device
                    )
                    agent._last_action = action

            flat_obs, harm_signal, done, info, obs_dict = env.step(action)

            if z_world_prev is not None and action_prev is not None:
                wf_buf.append((z_world_prev.cpu(), action_prev.cpu(), z_world_curr.cpu()))
                if len(wf_buf) > 2000:
                    wf_buf = wf_buf[-2000:]

            if harm_signal < 0:
                total_harm += 1
                harm_buf_pos.append(theta_z.detach())
                if len(harm_buf_pos) > 1000:
                    harm_buf_pos = harm_buf_pos[-1000:]
            else:
                harm_buf_neg.append(theta_z.detach())
                if len(harm_buf_neg) > 1000:
                    harm_buf_neg = harm_buf_neg[-1000:]

            e1_loss = agent.compute_prediction_loss()
            if e1_loss.requires_grad:
                optimizer.zero_grad()
                e1_loss.backward()
                torch.nn.utils.clip_grad_norm_(agent.e1.parameters(), 1.0)
                optimizer.step()

            if len(wf_buf) >= 16:
                k = min(32, len(wf_buf))
                idxs = torch.randperm(len(wf_buf))[:k].tolist()
                zw_b = torch.cat([wf_buf[i][0] for i in idxs]).to(agent.device)
                a_b = torch.cat([wf_buf[i][1] for i in idxs]).to(agent.device)
                zw1_b = torch.cat([wf_buf[i][2] for i in idxs]).to(agent.device)
                wf_loss = F.mse_loss(agent.e2.world_forward(zw_b, a_b), zw1_b)
                if wf_loss.requires_grad:
                    wf_optimizer.zero_grad()
                    wf_loss.backward()
                    torch.nn.utils.clip_grad_norm_(
                        list(agent.e2.world_transition.parameters())
                        + list(agent.e2.world_action_encoder.parameters()),
                        1.0,
                    )
                    wf_optimizer.step()

            if len(harm_buf_pos) >= 4 and len(harm_buf_neg) >= 4:
                k_p = min(16, len(harm_buf_pos))
                k_n = min(16, len(harm_buf_neg))
                pi = torch.randperm(len(harm_buf_pos))[:k_p].tolist()
                ni = torch.randperm(len(harm_buf_neg))[:k_n].tolist()
                zw_b = torch.cat(
                    [harm_buf_pos[i] for i in pi] + [harm_buf_neg[i] for i in ni], dim=0
                )
                target = torch.cat(
                    [
                        torch.ones(k_p, 1, device=agent.device),
                        torch.zeros(k_n, 1, device=agent.device),
                    ],
                    dim=0,
                )
                pred = agent.e3.harm_eval(zw_b)
                harm_loss = F.mse_loss(pred, target)
                if harm_loss.requires_grad:
                    harm_eval_optimizer.zero_grad()
                    harm_loss.backward()
                    torch.nn.utils.clip_grad_norm_(agent.e3.harm_eval_head.parameters(), 0.5)
                    harm_eval_optimizer.step()

            z_world_prev = z_world_curr
            z_self_prev = latent.z_self.detach()
            action_prev = action.detach()
            if done:
                break

        if (ep + 1) % 100 == 0 or ep == num_episodes - 1:
            print(
                f"  [train] ep {ep+1}/{num_episodes}  harm={total_harm}"
                f"  e3_ticks={e3_tick_total}",
                flush=True,
            )

    return {"total_harm": total_harm, "wf_buf": wf_buf, "e3_tick_total": e3_tick_total}


def _compute_world_forward_r2(agent: REEAgent, wf_buf: List, n_test: int = 200) -> float:
    if len(wf_buf) < n_test:
        return 0.0
    idxs = list(range(len(wf_buf) - n_test, len(wf_buf)))
    with torch.no_grad():
        zw = torch.cat([wf_buf[i][0] for i in idxs]).to(agent.device)
        a = torch.cat([wf_buf[i][1] for i in idxs]).to(agent.device)
        zw1 = torch.cat([wf_buf[i][2] for i in idxs]).to(agent.device)
        pred = agent.e2.world_forward(zw, a)
        ss_res = ((zw1 - pred) ** 2).sum()
        ss_tot = ((zw1 - zw1.mean(dim=0, keepdim=True)) ** 2).sum()
    return float((1 - ss_res / (ss_tot + 1e-8)).item())




def _eval_precision_responsibility(
    agent: REEAgent,
    env: CausalGridWorldV2,
    eval_episodes: int,
    steps_per_episode: int,
    world_dim: int,
) -> Dict:
    """Eval phase, COMMIT-WINDOW sampled (671c P3b/P3c).

    Structure is 671b's, with the sampling unit corrected. The E3 selector
    ticks roughly once per `heartbeat.e3_steps_per_tick` (default 10; measured
    10.5 steps/selection in this env), and 671b appended one sample per
    qualifying ENV STEP using a `held_committed` latch, reading
    `E3.current_precision` at the harm step. Two consequences, both fixed here:

      * the regressor was read AFTER the harm (agent.update_residue ->
        E3.post_action_update -> update_running_variance, every env tick), so
        it was not the precision at which the action was committed; and
      * two harm events inside one commit window counted as two independent
        observations of a single selection.

    Here a COMMIT WINDOW opens at each fresh E3 selection, carrying the
    `precision_margin_norm` that selection's own `select()` call computed
    (pre-harm by construction), and closes at the next selection or at episode
    end. Residue delta and harm magnitude accumulate over the window; the
    window emits ONE observation iff it was committed and saw at least one
    agent-owned genuine-harm step.

    671a's four instrument fixes are retained unchanged:
      (1) agent.update_residue(...) after every env.step().
      (2) committed sourced from SelectionResult.committed.
      (3) owned sourced from info["transition_type"] == "agent_caused_hazard".
      (4) sample filter is harm_signal < 0 AND owned.
    """
    # PRIMARY unit: one entry per committed harm-bearing selection.
    margin_samples: List[float] = []
    dv_samples: List[float] = []           # residue accumulated per unit harm
    window_precision_samples: List[float] = []   # current_precision AT the selection

    # SECONDARY (comparability with 671b): 671b's per-env-step unit.
    legacy_precision_samples: List[float] = []
    legacy_residue_delta_samples: List[float] = []
    legacy_harm_magnitude_samples: List[float] = []

    all_harm_preds: List[float] = []
    n_commit_windows = 0          # fresh selections that committed
    n_selections = 0              # fresh selections, committed or not
    n_latched_ticks = 0           # env steps running on a held action
    n_margin_unavailable = 0      # committed windows with no valid margin
    n_env_steps = 0
    fatal = 0

    total_residue_start = float(agent.residue_field.total_residue.item())

    # Open window state.
    w_open = False
    w_committed = False
    w_margin: Optional[float] = None
    w_precision = 0.0
    w_residue = 0.0
    w_harm = 0.0
    w_harm_events = 0

    def _close_window():
        """Emit at most one observation for the window just finished."""
        nonlocal w_open, w_committed, w_margin, w_precision
        nonlocal w_residue, w_harm, w_harm_events, n_margin_unavailable
        if w_open and w_committed and w_harm_events > 0:
            if w_margin is None or w_margin < 0.0:
                # world-variance branch did not run -> regressor absent. Counted,
                # never silently substituted (P0-3 gates the fraction at 1.0).
                n_margin_unavailable += 1
            else:
                margin_samples.append(float(w_margin))
                dv_samples.append(float(w_residue) / max(float(w_harm), 1e-6))
                window_precision_samples.append(float(w_precision))
        w_open = False
        w_committed = False
        w_margin = None
        w_precision = 0.0
        w_residue = 0.0
        w_harm = 0.0
        w_harm_events = 0

    for _ep in range(eval_episodes):
        obs, obs_dict = env.reset()
        agent.reset()
        z_self_prev: Optional[torch.Tensor] = None
        action_prev: Optional[torch.Tensor] = None
        residue_prev = float(agent.residue_field.total_residue.item())
        _close_window()

        for _ in range(steps_per_episode):
            obs_body = obs_dict["body_state"]
            obs_world = obs_dict["world_state"]

            with torch.no_grad():
                latent = agent.sense(obs_body, obs_world)
                if z_self_prev is not None and action_prev is not None:
                    agent.record_transition(z_self_prev, action_prev, latent.z_self.detach())

                ticks = agent.clock.advance()
                e1_prior = (
                    agent._e1_tick(latent)
                    if ticks.get("e1_tick", False)
                    else torch.zeros(1, world_dim, device=agent.device)
                )
                candidates = agent.generate_trajectories(latent, e1_prior, ticks)

            try:
                if ticks.get("e3_tick", False) and candidates:
                    # A FRESH selection: close the previous window, open a new
                    # one, and capture the regressor from THIS select() call.
                    _close_window()
                    with torch.no_grad():
                        # Clear the latch first so a diagnostic left over from
                        # an earlier selection can never be re-read as this
                        # one's (CLAUDE.md / queue-experiment sample-size rule).
                        agent.e3.last_score_diagnostics = None
                        result = agent.e3.select(candidates, temperature=1.0)
                        action = result.selected_action.detach()
                        agent._last_action = action
                        diag = getattr(agent.e3, "last_score_diagnostics", None) or {}
                        n_selections += 1
                        w_open = True
                        w_committed = bool(result.committed)
                        w_margin = diag.get("precision_margin_norm")
                        w_precision = float(agent.e3.current_precision)
                        if w_committed:
                            n_commit_windows += 1
                            h_pred = float(agent.e3.harm_eval(latent.z_world).item())
                            all_harm_preds.append(h_pred)
                else:
                    n_latched_ticks += 1
                    action = agent._last_action
                    if action is None:
                        action = _action_to_onehot(
                            random.randint(0, env.action_dim - 1), env.action_dim, agent.device
                        )
                        agent._last_action = action

                flat_obs, harm_signal, done, info, obs_dict = env.step(action)
                n_env_steps += 1

                owned = info.get("transition_type") == "agent_caused_hazard"

                agent.update_residue(
                    harm_signal=float(harm_signal),
                    world_delta=None,
                    hypothesis_tag=False,
                    owned=owned,
                )
                residue_curr = float(agent.residue_field.total_residue.item())
                residue_delta = residue_curr - residue_prev
                residue_prev = residue_curr

                if w_open and w_committed and owned and harm_signal < -1e-6:
                    w_residue += residue_delta
                    w_harm += abs(harm_signal)
                    w_harm_events += 1
                    # 671b's unit, kept for direct comparability only.
                    legacy_precision_samples.append(float(agent.e3.current_precision))
                    legacy_residue_delta_samples.append(residue_delta)
                    legacy_harm_magnitude_samples.append(abs(harm_signal))

            except Exception:
                fatal += 1
                action = _action_to_onehot(
                    random.randint(0, env.action_dim - 1), env.action_dim, agent.device
                )
                agent._last_action = action
                flat_obs, harm_signal, done, info, obs_dict = env.step(action)
                residue_prev = float(agent.residue_field.total_residue.item())

            z_self_prev = latent.z_self.detach()
            action_prev = action.detach()
            if done:
                break

        _close_window()

    total_residue_end = float(agent.residue_field.total_residue.item())
    total_residue_accumulated = total_residue_end - total_residue_start

    harm_pred_std = (
        float(torch.tensor(all_harm_preds).std().item()) if len(all_harm_preds) > 1 else 0.0
    )

    return {
        "margin_samples": margin_samples,
        "dv_samples": dv_samples,
        "window_precision_samples": window_precision_samples,
        "legacy_precision_samples": legacy_precision_samples,
        "legacy_residue_delta_samples": legacy_residue_delta_samples,
        "legacy_harm_magnitude_samples": legacy_harm_magnitude_samples,
        "n_events": len(margin_samples),
        "n_commit_windows": n_commit_windows,
        "n_selections": n_selections,
        "n_latched_ticks": n_latched_ticks,
        "n_margin_unavailable": n_margin_unavailable,
        "n_env_steps": n_env_steps,
        "harm_pred_std": harm_pred_std,
        "fatal_errors": fatal,
        "total_residue_accumulated": total_residue_accumulated,
    }


def _run_one_seed(
    seed: int,
    warmup_episodes: int,
    eval_episodes: int,
    steps_per_episode: int,
    alpha_world: float,
    alpha_self: float,
    harm_scale: float,
    proximity_scale: float,
    lr: float,
    self_dim: int,
    world_dim: int,
    zg_accum: Optional["ZGoalStreamAccumulator"] = None,
) -> Dict:
    torch.manual_seed(seed)
    random.seed(seed)

    env = CausalGridWorldV2(
        seed=seed,
        size=12,
        num_hazards=4,
        num_resources=5,
        hazard_harm=harm_scale,
        env_drift_interval=5,
        env_drift_prob=0.1,
        proximity_harm_scale=proximity_scale,
        proximity_benefit_scale=proximity_scale * 0.6,
        proximity_approach_threshold=0.15,
        hazard_field_decay=0.5,
    )
    config = REEConfig.from_dims(
        body_obs_dim=env.body_obs_dim,
        world_obs_dim=env.world_obs_dim,
        action_dim=env.action_dim,
        self_dim=self_dim,
        world_dim=world_dim,
        alpha_world=alpha_world,
        alpha_self=alpha_self,
        reafference_action_dim=env.action_dim,
    )
    agent = REEAgent(config)

    optimizer = optim.Adam(list(agent.e1.parameters()), lr=lr)
    wf_optimizer = optim.Adam(
        list(agent.e2.world_transition.parameters())
        + list(agent.e2.world_action_encoder.parameters()),
        lr=1e-3,
    )
    harm_eval_optimizer = optim.Adam(
        list(agent.e3.harm_eval_head.parameters()),
        lr=1e-4,
    )

    # Runner boundary line (RE_SEED_CONDITION): resets episodes_in_run at the
    # start of each seed's run. Single condition ("single") -- the EXP-1283
    # discriminative-pair control is a post-hoc within-seed permutation over
    # these same samples, not a second substrate arm.
    print(f"Seed {seed} Condition single", flush=True)

    train_out = _train(
        agent,
        env,
        optimizer,
        wf_optimizer,
        harm_eval_optimizer,
        warmup_episodes,
        steps_per_episode,
        world_dim,
    )
    world_forward_r2 = _compute_world_forward_r2(agent, train_out["wf_buf"])

    eval_out = _eval_precision_responsibility(
        agent, env, eval_episodes, steps_per_episode, world_dim
    )

    margins = eval_out["margin_samples"]
    dv = eval_out["dv_samples"]

    # WITHIN-SEED statistics (P3): this seed's own Pearson r and its own
    # median-split ratio. No pooling anywhere.
    seed_correlation = _pearson_correlation(margins, dv)
    seed_ratio = _within_seed_ratio(margins, dv)
    margin_spread = (max(margins) - min(margins)) if margins else 0.0

    # Non-gating secondary regressor (what_would_answer P3 lists per-seed
    # z-scored current_precision as the alternative scale-free choice). It is
    # NOT interchangeable with the margin -- margin = 1 - thr/precision is a
    # saturating transform, so the two differ materially over a 4-5 order of
    # magnitude precision range -- so it is reported, never gated on.
    wp = eval_out["window_precision_samples"]
    if len(wp) > 1:
        m = sum(wp) / len(wp)
        sd = (sum((v - m) ** 2 for v in wp) / (len(wp) - 1)) ** 0.5
        zwp = [(v - m) / sd for v in wp] if sd > 1e-12 else [0.0] * len(wp)
        seed_correlation_zprec = _pearson_correlation(zwp, dv)
    else:
        seed_correlation_zprec = 0.0

    # 671b's own per-env-step unit, recomputed here for direct comparability.
    legacy_corr = _pearson_correlation(
        eval_out["legacy_precision_samples"], eval_out["legacy_residue_delta_samples"]
    )

    n_events = eval_out["n_events"]
    print(
        f"  [seed {seed}] wf_r2={world_forward_r2:.4f}"
        f"  harm_pred_std={eval_out['harm_pred_std']:.4f}"
        f"  n_events={n_events}"
        f"  commit_windows={eval_out['n_commit_windows']}"
        f"  selections={eval_out['n_selections']}"
        f"  latched_ticks={eval_out['n_latched_ticks']}"
        f"  margin_spread={margin_spread:.4f}"
        f"  r_within={seed_correlation:.4f}"
        f"  ratio={seed_ratio:.4f}"
        f"  r_legacy_perstep={legacy_corr:.4f}"
        f"  residue_accum={eval_out['total_residue_accumulated']:.6f}"
        f"  fatal={eval_out['fatal_errors']}",
        flush=True,
    )
    # Per-seed runner completion signal. DIAGNOSTIC ONLY -- the scientific
    # verdict is the across-seed Fisher-z one printed at the end of run(); this
    # is the per-seed proxy the runner's progress bar / ETA needs one of per
    # seed x condition unit, per the progress-instrumentation contract.
    seed_verdict_pass = (
        n_events >= MIN_EVENTS_PER_SEED
        and seed_correlation > C1_BAR
        and seed_ratio > C2_BAR
        and eval_out["fatal_errors"] == 0
    )
    print(f"verdict: {'PASS' if seed_verdict_pass else 'FAIL'}", flush=True)

    if zg_accum is not None:
        zg_accum.observe(agent)

    return {
        "seed": seed,
        "world_forward_r2": world_forward_r2,
        "harm_pred_std": eval_out["harm_pred_std"],
        "n_events": n_events,
        "n_commit_windows": eval_out["n_commit_windows"],
        "n_selections": eval_out["n_selections"],
        "n_latched_ticks": eval_out["n_latched_ticks"],
        "n_margin_unavailable": eval_out["n_margin_unavailable"],
        "n_env_steps": eval_out["n_env_steps"],
        "margins": margins,
        "dv": dv,
        "margin_spread": margin_spread,
        "correlation": seed_correlation,
        "correlation_zprec_secondary": seed_correlation_zprec,
        "correlation_legacy_perstep": legacy_corr,
        "ratio": seed_ratio,
        "legacy_n_samples": len(eval_out["legacy_precision_samples"]),
        "total_residue_accumulated": eval_out["total_residue_accumulated"],
        "fatal_errors": eval_out["fatal_errors"],
        "qualifies": bool(n_events >= MIN_EVENTS_PER_SEED),
    }


def run(
    seeds: Optional[List[int]] = None,
    warmup_episodes: int = 500,
    eval_episodes: int = 50,
    steps_per_episode: int = 200,
    alpha_world: float = 0.9,
    alpha_self: float = 0.3,
    harm_scale: float = 0.02,
    proximity_scale: float = 1.0,
    lr: float = 1e-3,
    self_dim: int = 32,
    world_dim: int = 32,
) -> Dict:
    seeds = list(seeds) if seeds else list(SEEDS)

    full_config = {
        "seeds": seeds,
        "warmup_episodes": warmup_episodes,
        "eval_episodes": eval_episodes,
        "steps_per_episode": steps_per_episode,
        "alpha_world": alpha_world,
        "alpha_self": alpha_self,
        "harm_scale": harm_scale,
        "proximity_scale": proximity_scale,
        "lr": lr,
        "self_dim": self_dim,
        "world_dim": world_dim,
        "env": "CausalGridWorldV2",
        "env_size": 12,
        "env_num_hazards": 4,
        "env_num_resources": 5,
        "regressor": "precision_margin_norm",
        "observation_unit": "commit_window",
        "residue_floor": RESIDUE_FLOOR,
        "margin_spread_floor": MARGIN_SPREAD_FLOOR,
        "margin_availability_floor": MARGIN_AVAILABILITY_FLOOR,
        "c1_bar": C1_BAR,
        "c2_bar": C2_BAR,
        "c2_seed_fraction_required": C2_SEED_FRACTION_REQUIRED,
        "min_events_per_seed": MIN_EVENTS_PER_SEED,
        "min_qualifying_seeds": MIN_QUALIFYING_SEEDS,
        "permutation_draws": PERMUTATION_DRAWS,
        "permutation_seed": PERMUTATION_SEED,
    }

    print(
        f"[V3-EXQ-671c] MECH-025b: Precision-Responsibility, WITHIN-SEED "
        f"Fisher-z estimator (supersedes 671b's pooled estimator)\n"
        f"  seeds={seeds}  warmup={warmup_episodes}  eval={eval_episodes}"
        f"  regressor=precision_margin_norm  unit=commit_window\n"
        f"  C1 bar={C1_BAR} (derived, P4 route 2)  C2 bar={C2_BAR} on "
        f">={C2_SEED_FRACTION_REQUIRED:.0%} of qualifying seeds",
        flush=True,
    )

    _zg_accum = ZGoalStreamAccumulator()
    per_seed_results = []
    for seed in seeds:
        print(f"\n[V3-EXQ-671c] Running seed={seed}...", flush=True)
        per_seed_results.append(
            _run_one_seed(
                seed, warmup_episodes, eval_episodes, steps_per_episode,
                alpha_world, alpha_self, harm_scale, proximity_scale,
                lr, self_dim, world_dim, zg_accum=_zg_accum,
            )
        )

    # --- PRIMARY: within-seed Fisher-z across QUALIFYING seeds (P3) ---------
    fz = _within_seed_fisher_z(per_seed_results)
    qualifying = [s for s in per_seed_results if s["qualifies"]]
    n_qualifying = len(qualifying)

    # C2: within-seed median-split ratio, counted over qualifying seeds only.
    c2_seeds_clear = sum(1 for s in qualifying if s["ratio"] > C2_BAR)
    c2_seeds_required = (
        int(math.ceil(C2_SEED_FRACTION_REQUIRED * n_qualifying)) if n_qualifying else 0
    )

    # --- DIAGNOSTIC ONLY: 671b's pooled estimator, recomputed here ----------
    # Pre-registered interpretation rule (P3): if this disagrees in SIGN with
    # the within-seed estimate, the WITHIN-SEED estimate governs.
    pooled_margins, pooled_dv = [], []
    for s in per_seed_results:
        pooled_margins.extend(s["margins"])
        pooled_dv.extend(s["dv"])
    pooled_correlation = _pearson_correlation(pooled_margins, pooled_dv)
    pooled_ratio = _within_seed_ratio(pooled_margins, pooled_dv)
    sign_disagreement = bool(
        fz["estimable"]
        and pooled_correlation != 0.0
        and (pooled_correlation > 0) != (fz["r_fisher_z"] > 0)
    )

    # --- CONTROL ARM: within-seed label permutation (EXP-1283 pair) ---------
    control = _permutation_control(
        [{"margins": s["margins"], "dv": s["dv"]} for s in per_seed_results],
        observed_z=fz["z_mean"],
    )

    # --- POSITIVE-CONTROL / READINESS GATES --------------------------------
    total_residue_accumulated = sum(s["total_residue_accumulated"] for s in per_seed_results)
    world_forward_r2 = _mean_safe([s["world_forward_r2"] for s in per_seed_results])
    harm_pred_std = _mean_safe([s["harm_pred_std"] for s in per_seed_results])
    fatal_errors = sum(s["fatal_errors"] for s in per_seed_results)

    # Worst-cell, not mean: an all()-style claim must report the offending seed.
    worst_spread, worst_spread_seed = _worst_cell(
        [(s["seed"], s["margin_spread"]) for s in qualifying]
    )
    total_commit_windows = sum(s["n_commit_windows"] for s in per_seed_results)
    total_margin_unavailable = sum(s["n_margin_unavailable"] for s in per_seed_results)
    total_events = sum(s["n_events"] for s in per_seed_results)
    margin_availability = (
        1.0 - (total_margin_unavailable / max(total_events + total_margin_unavailable, 1))
    )

    readiness_checks = [
        {
            "name": "residue_accumulates_under_committed_harm",
            "measured": float(total_residue_accumulated),
            "threshold": RESIDUE_FLOOR,
            "direction": "lower",
            "control": (
                "sum of ResidueField.total_residue deltas over committed, "
                "agent-owned harm-events during eval, across all seeds. Must "
                "move for the precision<->residue readout to be non-vacuous "
                "(failure_autopsy_batch9_2026-06-12 root cause: 671's residue "
                "field was mathematically pinned at 0)."
            ),
        },
        {
            "name": "margin_within_seed_spread_worst_seed",
            "measured": float(worst_spread),
            "threshold": MARGIN_SPREAD_FLOOR,
            "direction": "lower",
            "offending_cell": (
                f"seed={worst_spread_seed}" if worst_spread_seed is not None else "none"
            ),
            "control": (
                "WORST qualifying seed's max-min spread of precision_margin_"
                "norm over its own commit windows. precision_margin_norm is "
                "normalized to [0,1] by construction, so this floor is "
                "structural rather than calibrated. Closes a degeneracy mode "
                "671a/671b could not see: margin = 1 - thr/current_precision "
                "saturates, so current_precision spread is LARGEST exactly "
                "when the margin is most ceiling-compressed."
            ),
        },
        {
            "name": "margin_available_on_committed_windows",
            "measured": float(margin_availability),
            "threshold": MARGIN_AVAILABILITY_FLOOR,
            "direction": "lower",
            "control": (
                "fraction of committed harm-bearing windows carrying a valid "
                "precision_margin_norm. The regressor is emitted only on the "
                "world-variance commit branch (e3_selector.py:4059); this "
                "driver passes no harm bridge, so anything below 1.0 means a "
                "silent branch flip, not noise."
            ),
        },
        dv_headroom_check(
            "c1_jointly_satisfiable_at_realised_weight",
            dv_name="fisher_z_weight_sum",
            criterion_threshold=float(C1_MIN_FISHER_WEIGHT),
            achievable=float(fz["weight_total"]),
            control=(
                "sum of (n_i - 3) over qualifying seeds -- the realised Fisher "
                "weight. C1's two load-bearing halves (r > C1_BAR, and a 95% CI "
                "excluding 0) are JOINTLY satisfiable only when this clears "
                "(1.96/atanh(C1_BAR))^2. Below it the run cannot PASS whatever "
                "the data say, so it is a requeue at a larger eval budget, not "
                "a null -- the exact 'criteria not jointly satisfiable' shape "
                "the 2026-09-03 cluster spent its compute on."
            ),
        ),
        {
            "name": "qualifying_seeds_at_min_events",
            "measured": float(n_qualifying),
            "threshold": float(MIN_QUALIFYING_SEEDS),
            "direction": "lower",
            "control": (
                f"seeds carrying >= {MIN_EVENTS_PER_SEED} committed harm-events "
                f"(what_would_answer P3 exclusion + the FALSIFYING clause's "
                f">= {MIN_QUALIFYING_SEEDS}-seed requirement). Below this the "
                f"run cannot return EITHER verdict and is a requeue, not a null."
            ),
        },
    ]
    ready = True
    preconditions = []
    try:
        preconditions = p0_readiness_gate(readiness_checks)
    except P0NotReady as e:
        preconditions = e.preconditions
        ready = False

    # Secondary net: the discriminative quantities must have usable spread,
    # checked GROUPED BY SEED (never pooled -- pooling is the 671b defect).
    degeneracy = check_degeneracy(
        {
            "C1_dv_within_seed": {"groups": [s["dv"] for s in qualifying]},
            "C1_margin_within_seed": {"groups": [s["margins"] for s in qualifying]},
        }
    )
    non_degenerate = degeneracy["non_degenerate"]

    # --- PASS CRITERIA ------------------------------------------------------
    # C1 is TWO-PART and both parts are load-bearing: an effect-size floor
    # (C1_BAR, P4) and the what_would_answer's own significance requirement
    # (95% CI excluding 0). They are separate instruments and are reported
    # separately so a reader can see which one failed.
    c1_effect_pass = bool(fz["estimable"] and fz["r_fisher_z"] > C1_BAR)
    c1_ci_pass = bool(fz["ci_excludes_zero"] and fz["r_fisher_z"] > 0)
    c1_pass = bool(c1_effect_pass and c1_ci_pass)
    c2_pass = bool(n_qualifying > 0 and c2_seeds_clear >= c2_seeds_required)
    c3_pass = bool(n_qualifying >= MIN_QUALIFYING_SEEDS)
    c4_pass = bool(world_forward_r2 > 0.05)
    c5_pass = bool(harm_pred_std > 0.01)
    c6_pass = bool(fatal_errors == 0)

    # COMBINATION RULE (recorded, not just implied): plain AND over the six.
    combination_rule = (
        "PASS iff C1 AND C2 AND C3 AND C4 AND C5 AND C6, where C1 itself is "
        "(r_fisher_z > C1_BAR) AND (95% CI excludes 0). Load-bearing: C1, C2. "
        "C3-C6 are health/precondition checks and carry no direction."
    )
    all_pass = c1_pass and c2_pass and c3_pass and c4_pass and c5_pass and c6_pass
    criteria_met = sum([c1_pass, c2_pass, c3_pass, c4_pass, c5_pass, c6_pass])

    if not ready:
        status = "FAIL"
        evidence_direction = "non_contributory"
        label = "substrate_not_ready_requeue"
    elif not non_degenerate:
        status = "FAIL"
        evidence_direction = "non_contributory"
        label = "within_seed_estimator_degenerate_vacuous_test"
    elif all_pass:
        status = "PASS"
        evidence_direction = "supports"
        label = "precision_scales_residue_weight_within_seed"
    elif not (c4_pass and c5_pass and c6_pass):
        # A health-check failure is an instrument problem, not claim pressure.
        status = "FAIL"
        evidence_direction = "non_contributory"
        label = "substrate_health_check_failed_not_claim_pressure"
    else:
        # Both load-bearing criteria were genuinely measurable and did not
        # clear: this IS real claim pressure (what_would_answer FALSIFYING).
        status = "FAIL"
        evidence_direction = "weakens"
        label = "precision_does_not_scale_residue_weight_within_seed"

    failure_notes = []
    if not ready:
        for p in preconditions:
            if not p.get("met", True):
                failure_notes.append(
                    f"P0 FAIL: {p['name']} unmet -- measured={p.get('measured')} "
                    f"vs threshold={p.get('threshold')} (substrate_not_ready_requeue)"
                )
    if ready and not non_degenerate:
        failure_notes.append(f"DEGENERATE: {degeneracy['degeneracy_reason']}")
    if not c1_effect_pass:
        failure_notes.append(
            f"C1a FAIL: r_fisher_z={fz['r_fisher_z']:.4f} <= C1_BAR={C1_BAR}"
        )
    if not c1_ci_pass:
        failure_notes.append(
            f"C1b FAIL: 95% CI [{fz['ci_low']:.4f}, {fz['ci_high']:.4f}] does not exclude 0"
        )
    if not c2_pass:
        failure_notes.append(
            f"C2 FAIL: {c2_seeds_clear}/{n_qualifying} qualifying seeds clear "
            f"ratio>{C2_BAR}; required {c2_seeds_required}"
        )
    if not c3_pass:
        failure_notes.append(
            f"C3 FAIL: qualifying seeds={n_qualifying} < {MIN_QUALIFYING_SEEDS}"
        )
    if not c4_pass:
        failure_notes.append(f"C4 FAIL: world_forward_r2={world_forward_r2:.4f} <= 0.05")
    if not c5_pass:
        failure_notes.append(f"C5 FAIL: harm_pred_std={harm_pred_std:.4f} <= 0.01")
    if not c6_pass:
        failure_notes.append(f"C6 FAIL: fatal_errors={fatal_errors}")
    if sign_disagreement:
        failure_notes.append(
            f"NOTE (pre-registered, not a failure): pooled r={pooled_correlation:.4f} "
            f"disagrees in SIGN with within-seed r={fz['r_fisher_z']:.4f}. Per "
            f"what_would_answer P3 the WITHIN-SEED estimate governs; the pooled "
            f"value is a diagnostic only. This is the 671b defect reproducing."
        )

    print(f"\nV3-EXQ-671c verdict: {status}  label={label}  ({criteria_met}/6)", flush=True)
    for note in failure_notes:
        print(f"  {note}", flush=True)

    # FLAT SCALAR READOUT -- booleans as 0/1 ints, non-finite dropped.
    def _flat(d):
        out = {}
        for k, v in d.items():
            if isinstance(v, bool):
                out[k] = 1 if v else 0
            elif isinstance(v, (int, float)):
                fv = float(v)
                if fv == fv and abs(fv) != float("inf"):
                    out[k] = fv
        return out

    readout = _flat({
        "r_fisher_z_within_seed": fz["r_fisher_z"],
        "z_mean_within_seed": fz["z_mean"],
        "fisher_z_se": fz["se"],
        "ci_low": fz["ci_low"],
        "ci_high": fz["ci_high"],
        "ci_excludes_zero": fz["ci_excludes_zero"],
        "weight_total_n_minus_3": fz["weight_total"],
        "c1_min_fisher_weight_required": C1_MIN_FISHER_WEIGHT,
        "n_qualifying_seeds": n_qualifying,
        "n_seeds": len(seeds),
        "n_events_total": total_events,
        "n_commit_windows_total": total_commit_windows,
        "n_latched_ticks_total": sum(s["n_latched_ticks"] for s in per_seed_results),
        "n_selections_total": sum(s["n_selections"] for s in per_seed_results),
        "margin_availability": margin_availability,
        "margin_spread_worst_seed": worst_spread,
        "c2_seeds_clear": c2_seeds_clear,
        "c2_seeds_required": c2_seeds_required,
        "pooled_correlation_diagnostic": pooled_correlation,
        "pooled_ratio_diagnostic": pooled_ratio,
        "sign_disagreement_pooled_vs_within": sign_disagreement,
        "control_null_r_p95": control.get("null_r_p95"),
        "control_p_empirical": control.get("p_empirical"),
        "world_forward_r2": world_forward_r2,
        "harm_pred_std": harm_pred_std,
        "total_residue_accumulated": total_residue_accumulated,
        "fatal_error_count": fatal_errors,
        "c1_bar": C1_BAR,
        "c2_bar": C2_BAR,
        "crit1_pass": c1_pass,
        "crit1a_effect_pass": c1_effect_pass,
        "crit1b_ci_pass": c1_ci_pass,
        "crit2_pass": c2_pass,
        "crit3_pass": c3_pass,
        "crit4_pass": c4_pass,
        "crit5_pass": c5_pass,
        "crit6_pass": c6_pass,
        "criteria_met": criteria_met,
    })
    metrics = dict(readout)

    per_seed_diagnostics = [
        {
            "seed": s["seed"],
            "n_events": s["n_events"],
            "qualifies": s["qualifies"],
            "n_commit_windows": s["n_commit_windows"],
            "n_selections": s["n_selections"],
            "n_latched_ticks": s["n_latched_ticks"],
            "n_env_steps": s["n_env_steps"],
            "margin_spread": s["margin_spread"],
            "correlation_within_seed": s["correlation"],
            "correlation_zprec_secondary": s["correlation_zprec_secondary"],
            "correlation_legacy_perstep_671b_unit": s["correlation_legacy_perstep"],
            "legacy_n_samples_671b_unit": s["legacy_n_samples"],
            "ratio": s["ratio"],
            "world_forward_r2": s["world_forward_r2"],
            "harm_pred_std": s["harm_pred_std"],
            "total_residue_accumulated": s["total_residue_accumulated"],
            "fatal_errors": s["fatal_errors"],
        }
        for s in per_seed_results
    ]

    per_seed_table = "\n".join(
        f"| {d['seed']} | {d['n_events']} | {'yes' if d['qualifies'] else 'NO'} | "
        f"{d['margin_spread']:.4f} | {d['correlation_within_seed']:.4f} | "
        f"{d['ratio']:.4f} | {d['correlation_legacy_perstep_671b_unit']:.4f} | "
        f"{d['legacy_n_samples_671b_unit']} | {d['world_forward_r2']:.4f} |"
        for d in per_seed_diagnostics
    )

    failure_section = ""
    if failure_notes:
        failure_section = "\n## Notes\n\n" + "\n".join(f"- {n}" for n in failure_notes)

    summary_markdown = f"""# V3-EXQ-671c -- MECH-025b: Precision-Responsibility (WITHIN-SEED estimator)

**Status:** {status}
**Label:** {label}
**Claim:** MECH-025b -- precision at commit scales responsibility (residue) weight
**Supersedes:** V3-EXQ-671b (pooled, seed-confounded estimator; GFLAG-0151)
**Regressor:** precision_margin_norm (scale-free, captured INSIDE select())
**Observation unit:** commit window (one per fresh committed E3 selection)
**Warmup:** {warmup_episodes} eps/seed  |  Eval: {eval_episodes} eps/seed
**Seeds:** {seeds}

## Primary result -- within-seed Fisher-z (what_would_answer P3)

| Quantity | Value |
|---|---|
| r (Fisher-z averaged, back-transformed) | {fz['r_fisher_z']:.4f} |
| Fisher z mean | {fz['z_mean']:.4f} |
| SE (1/sqrt(sum n-3)) | {fz['se']:.4f} |
| 95% CI on r | [{fz['ci_low']:.4f}, {fz['ci_high']:.4f}] |
| CI excludes 0 | {fz['ci_excludes_zero']} |
| sum(n-3) | {fz['weight_total']:.0f} |
| Qualifying seeds (n_events >= {MIN_EVENTS_PER_SEED}) | {n_qualifying} of {len(seeds)} |
| Excluded seeds | {fz['excluded_seeds']} |

## Control arm -- within-seed label permutation (EXP-1283 discriminative pair)

| Quantity | Value |
|---|---|
| Draws | {control.get('draws', 0)} |
| Null Fisher-z 95th pct (as r) | {control.get('null_r_p95', float('nan')):.4f} |
| Empirical p (observed vs null) | {control.get('p_empirical', float('nan')):.4f} |

Reported as a control. NOT used as the C1 bar.

## Positive-control / readiness gates

| Check | Measured | Threshold | Met |
|---|---|---|---|
| residue_accumulates_under_committed_harm | {total_residue_accumulated:.6g} | {RESIDUE_FLOOR:g} | {total_residue_accumulated >= RESIDUE_FLOOR} |
| margin_within_seed_spread_worst_seed (seed {worst_spread_seed}) | {worst_spread:.6g} | {MARGIN_SPREAD_FLOOR:g} | {worst_spread >= MARGIN_SPREAD_FLOOR} |
| margin_available_on_committed_windows | {margin_availability:.6g} | {MARGIN_AVAILABILITY_FLOOR:g} | {margin_availability >= MARGIN_AVAILABILITY_FLOOR} |
| qualifying_seeds_at_min_events | {n_qualifying} | {MIN_QUALIFYING_SEEDS} | {n_qualifying >= MIN_QUALIFYING_SEEDS} |

Within-seed non-degeneracy: {non_degenerate} ({degeneracy['degeneracy_reason'] or 'ok'})

## Per-seed (the primary estimator's own constituents)

| Seed | n_events | Qualifies | Margin spread | r (within) | Ratio | r (671b per-step unit) | n (671b unit) | WF R2 |
|---|---|---|---|---|---|---|---|---|
{per_seed_table}

## Diagnostic -- 671b's pooled estimator, recomputed

| Quantity | Value |
|---|---|
| Pooled correlation | {pooled_correlation:.4f} |
| Pooled ratio | {pooled_ratio:.4f} |
| Sign disagreement with within-seed | {sign_disagreement} |

Pre-registered (P3): on a sign disagreement the WITHIN-SEED estimate governs.

## PASS criteria

Combination rule: {combination_rule}

| Criterion | Measured | Threshold | Result |
|---|---|---|---|
| C1a: r_fisher_z > C1_BAR | {fz['r_fisher_z']:.4f} | {C1_BAR} | {"PASS" if c1_effect_pass else "FAIL"} |
| C1b: 95% CI excludes 0 | [{fz['ci_low']:.4f}, {fz['ci_high']:.4f}] | excludes 0 | {"PASS" if c1_ci_pass else "FAIL"} |
| C2: qualifying seeds with ratio > {C2_BAR} | {c2_seeds_clear} | {c2_seeds_required} | {"PASS" if c2_pass else "FAIL"} |
| C3: qualifying seeds | {n_qualifying} | {MIN_QUALIFYING_SEEDS} | {"PASS" if c3_pass else "FAIL"} |
| C4: world_forward_r2 | {world_forward_r2:.4f} | 0.05 | {"PASS" if c4_pass else "FAIL"} |
| C5: harm_pred_std | {harm_pred_std:.4f} | 0.01 | {"PASS" if c5_pass else "FAIL"} |
| C6: fatal errors | {fatal_errors} | 0 | {"PASS" if c6_pass else "FAIL"} |

Criteria met: {criteria_met}/6 -> **{status}** (label: {label})

## Scope limit on a PASS

A PASS confirms precision SCALES RESIDUE WEIGHT. It does NOT confirm the claim's
stated rationale that higher precision implies higher ETHICAL ACCOUNTABILITY --
that premise is INV-012 Leg 0 and is recorded as CURRENTLY UNMET. A PASS
promotes the mechanistic half and leaves the accountability bridge gated.
{failure_section}
"""

    return {
        "status": status,
        "metrics": metrics,
        "readout": readout,
        "summary_markdown": summary_markdown,
        "claim_ids": CLAIM_IDS,
        "supersedes": SUPERSEDES,
        "evidence_direction": evidence_direction,
        "experiment_type": EXPERIMENT_TYPE,
        "experiment_purpose": EXPERIMENT_PURPOSE,
        "fatal_error_count": fatal_errors,
        "interpretation": {
            "label": label,
            "combination_rule": combination_rule,
            "preconditions": preconditions,
            "criteria_non_degenerate": {
                "C1": bool(non_degenerate and fz["estimable"]),
                "C2": bool(non_degenerate and n_qualifying > 0),
                "C3": True,
                "C4": True,
                "C5": True,
                "C6": True,
            },
            "criteria": [
                {"name": "C1a_r_fisher_z_within_seed", "load_bearing": True,
                 "passed": c1_effect_pass, "measured": float(fz["r_fisher_z"]),
                 "threshold": float(C1_BAR), "comparator": ">"},
                {"name": "C1b_ci_excludes_zero", "load_bearing": True,
                 "passed": c1_ci_pass, "measured": float(fz["ci_low"]),
                 "threshold": 0.0, "comparator": ">",
                 "note": f"CI [{fz['ci_low']:.4f}, {fz['ci_high']:.4f}]"},
                {"name": "C2_within_seed_ratio_seed_count", "load_bearing": True,
                 "passed": c2_pass, "measured": float(c2_seeds_clear),
                 "threshold": float(c2_seeds_required), "comparator": ">=",
                 "ratio_bar": float(C2_BAR)},
                {"name": "C3_qualifying_seeds", "load_bearing": False,
                 "passed": c3_pass, "measured": float(n_qualifying),
                 "threshold": float(MIN_QUALIFYING_SEEDS), "comparator": ">="},
                {"name": "C4_world_forward_r2", "load_bearing": False,
                 "passed": c4_pass, "measured": float(world_forward_r2),
                 "threshold": 0.05, "comparator": ">"},
                {"name": "C5_harm_pred_std", "load_bearing": False,
                 "passed": c5_pass, "measured": float(harm_pred_std),
                 "threshold": 0.01, "comparator": ">"},
                {"name": "C6_no_fatal_errors", "load_bearing": False,
                 "passed": c6_pass, "measured": float(fatal_errors),
                 "threshold": 0.0, "comparator": "<="},
            ],
            "per_seed_diagnostics": per_seed_diagnostics,
            "within_seed_fisher_z": fz,
            "control_arm_permutation": control,
            "pooled_diagnostic": {
                "correlation": pooled_correlation,
                "ratio": pooled_ratio,
                "sign_disagreement_with_within_seed": sign_disagreement,
                "note": (
                    "671b's estimator, recomputed on this run's samples. "
                    "DIAGNOSTIC ONLY -- pre-registered rule P3: on a sign "
                    "disagreement the within-seed estimate governs."
                ),
            },
        },
        "non_degenerate": non_degenerate,
        "degeneracy_reason": degeneracy["degeneracy_reason"],
        "config": full_config,
        "seeds_used": seeds,
        "z_goal_stream_stats": _zg_accum.stats(),
        "ethics_preflight": {
            "involves_negative_valence": False,
            "involves_suffering_like_state": False,
            "involves_self_model": False,
            "involves_inescapability_or_helplessness": False,
            "involves_offline_replay_over_harm": False,
            "involves_social_mind_or_language": False,
            "involves_human_data_or_clinical_context": False,
            "decision": "allow",
        },
    }


if __name__ == "__main__":
    import argparse
    import time
    from datetime import datetime, timezone

    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, nargs="+", default=None)
    parser.add_argument("--warmup", type=int, default=500)
    parser.add_argument("--eval-eps", type=int, default=50)
    parser.add_argument("--steps", type=int, default=200)
    parser.add_argument("--alpha-world", type=float, default=0.9)
    parser.add_argument("--harm-scale", type=float, default=0.02)
    parser.add_argument("--dry-run", action="store_true", help="Quick validation run")
    args = parser.parse_args()

    if args.dry_run:
        print("[DRY RUN] Quick validation mode", flush=True)
        args.warmup = 5
        args.eval_eps = 2
        args.steps = 50
        args.seeds = args.seeds or SEEDS[:2]

    _t0 = time.perf_counter()
    result = run(
        seeds=args.seeds,
        warmup_episodes=args.warmup,
        eval_episodes=args.eval_eps,
        steps_per_episode=args.steps,
        alpha_world=args.alpha_world,
        harm_scale=args.harm_scale,
    )

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    result["run_timestamp"] = ts
    result["timestamp_utc"] = ts
    result["claim"] = CLAIM_IDS[0]
    result["verdict"] = result["status"]
    result["outcome"] = result["status"]
    result["run_id"] = f"{EXPERIMENT_TYPE}_{ts}_v3"
    result["architecture_epoch"] = "ree_hybrid_guardrails_v1"

    # dry_run=True relocates the manifest out of evidence/experiments/ so a
    # smoke never lands a toy manifest the indexer scores (incident
    # V3-EXQ-696), while still exercising the full recording path.
    out_path = write_flat_manifest(
        result,
        out_dir=None,
        dry_run=args.dry_run,
        config=result.get("config"),
        seeds=result.get("seeds_used", SEEDS),
        script_path=Path(__file__),
        started_at=_t0,
        z_goal_stream_stats=result.get("z_goal_stream_stats"),
    )
    print(f"\nResult written to: {out_path}", flush=True)

    print(f"Status: {result['status']}", flush=True)
    for k, v in result["metrics"].items():
        print(f"  {k}: {v}", flush=True)

    _outcome_raw = str(result.get("status", "FAIL")).upper()
    emit_outcome(
        outcome=_outcome_raw if _outcome_raw in ("PASS", "FAIL") else "FAIL",
        manifest_path=out_path,
        dry_run=args.dry_run,
    )
