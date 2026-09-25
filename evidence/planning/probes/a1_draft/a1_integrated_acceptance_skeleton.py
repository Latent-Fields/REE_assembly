"""A1 integrated closed-loop acceptance -- SCRIPT SKELETON (DRAFT; NOT QUEUED; NOT an experiment).

Pre-registration: REE_assembly/evidence/planning/coupled_a1_preregistration_draft_20260925.md
Plan of record:   REE_assembly/evidence/planning/coupled_loop_repair_campaign_plan.md (sec 5, 6, 9)
Author: bt0925-a1prereg, chip_ref chip-20260925-coupled-a1-preregistration-draft, 2026-09-25.
v2:     bt0925-a1v2, chip_ref chip-20260925-coupled-a1-prereg-v2, 2026-09-25. Folds in the user decisions
        (rec-20260925-5fc6c256 floors + P1g, -aa066e96 change floor 1.44, -38b81685 hold for both
        variants, -c2519d92 NOVAL arms, -b9652a9b consumer-mediated gate leg on both variants) and the
        action-space design's A1 edits E1-E9 (action_space_proposals_design_20260925.md sec 5.2).
v2b:    bt0925-a1v2b, rec-20260925-a16786f5 (consumer-mediated (e) legs reported until W5; oracle diagnostic).
v3:     bt0925-a1v3, chip_ref chip-20260925-coupled-a1-prereg-v3, 2026-09-25. Folds in RT-5
        (a1_rt5_native_reseed_probe_20260925.md, 332ab3f7f8) and three user decisions:
          O11 power   rec-20260925-42ed9d20: PAIRED MEAN test across seeds replaces the per-seed ">= 4/5 exceed
                      margin" counts; more seeds (N_PER_STRATUM 12 + 12). Floors stay floors on the margin.
          O12 stratum rec-20260925-a6132a2d: env-only classifier (fixed-seed RandomPolicy rollout on the env
                      seed) + SHARED INIT of INT/NATIVE common modules. v3 adds a validity gate on the env-only
                      classifier (the pilot measured it DEGENERATE: ICC 0.02) with a pre-registered fallback,
                      and the harness-side shared-init hook (share_init; ree_core change not needed).
          floor       rec-20260925-b89fe715: benign reward-change floor 0.43 (measured), superseding 1.44.
        v3 addendum (user direction 2026-09-25 ~18:20Z, via the orchestrator): REPORT-ONLY "init-dominance" readout
        (init_dominance) from the reseed arms A1 already runs; never gating (selftest shows it cannot flip a verdict).
v3b:    bt0925-a1v3b, user answers 2026-09-25 (relayed by the orchestrator, received by 18:36Z): O12b stratum = the (env seed,
        agent seed) PAIR classified from NATIVE's closed-loop steps 0-599, relying on shared init (STRATUM_DECIDED);
        O13 keep the reseed arms; O14 confirm the paired form for P1g / head-to-head / NOVAL attribution; O15 ADD the
        babble-attribution arms INT-v-NOBABBLE and INT-v-BABBLE-DATA with a pre-registered SECONDARY contrast
        (babble_attribution) that has its own rule and never moves A1's verdict.

WHAT THIS FILE IS
  * The ARM WIRING and the ORDER OF OPERATIONS of the A1 run, with every call site of the I1
    instruments (ree-v3 experiments/_lib/coupled_acceptance.py) marked "I1-n".
  * The SCORING half (paired-mean superiority / non-inferiority tests, criteria P1b/P1t/P1g/P2/P3/P4, the
    verdict ladder, the head-to-head rule, NOVAL attribution, the pre-A1 hold, the stratum-rule choice and
    the shared-init merge) implemented in full as PURE functions, because those are what the
    pre-registration fixes. `--selftest` runs them on synthetic seeds.
  * `--selftest` ALSO runs a mutation check: it restores each retired rule one at a time (per-seed counting,
    1.44 change floor, `>= 0` P1g, no underpowered-CD guard, (e) legs gating, the v1 tie-winner name, no
    env-only-classifier validity gate, no shared init) and requires the case written for that rule to flip.

WHAT THIS FILE IS NOT
  * Runnable against an agent. The agent-facing functions raise NotImplementedError until W6
    (the integrated preset) and I1 exist on their respective refs. /queue-experiment turns this
    into ree-v3/experiments/<name>.py; it must not be copied into experiments/ from here.
  * The I1 API names below are a guide, not a contract: re-read coupled_acceptance.py on origin/main when
    porting.

No ree_core import happens at module import time (so --describe/--selftest run anywhere).
ASCII-only output.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from typing import Any, Dict, List, Optional, Sequence

# ----------------------------------------------------------------------------- constants (pre-registered)
PREREG_ID = "coupled_a1_preregistration_draft_20260925"
ENV_KW = dict(size=8, num_hazards=2, num_resources=3, max_episode_steps=200,
              proximity_approach_magnitude_tiebreak=True)          # user decision rec-20260925-b4355023
WORLD_DIM = 32                                                      # deployed value
DEV_EPOCH_STEPS = 2400                                              # plan sec 5 phase 1 (DRAFT, see prereg sec 4)
CLOSED_LOOP_STEPS = 3000                                            # accepted rec-20260925-7e7e9825
FIRST = (0, 600)
LAST = (2400, 3000)
STRATUM_WINDOW = 600                                                # classifier window (steps 0..599)
BENIGN, TRAPPED = "benign", "hazard_trapped"
# v3 (O11, rec-20260925-42ed9d20): more seeds, chosen from RT-5's measured SDs (prereg sec 6.5).
N_PER_STRATUM = {BENIGN: 12, TRAPPED: 12}
RESERVE_PER_STRATUM = 2
SCREEN_CEILING = 80
SEED_START = 301
AGENT_SEED_OFFSET = 10_000                                          # NATIVE-Rk agent seed = env seed + k*offset
N_RESEED = 3                                                        # v3: REPORTED noise only (prereg 6.2)

# v3 scoring rule (O11). "paired_mean": for each criterion the per-seed paired deltas (INT - comparator) are
# tested on their MEAN across the stratum's admitted seeds with SE = SD_used / sqrt(n), SD_used =
# max(sample SD, floor / 2). Superiority holds iff mean > SE_MULT x SE (the floor enters as floor / sqrt(n):
# the floor is 2 x a per-seed replicate SD, so it floors the SD, not the mean). Non-inferiority holds iff
# mean deficit + SE_MULT x SE <= delta, delta = the accepted absolute floor; CANNOT_DETERMINE
# (ni_underpowered) iff SE_MULT x SE > delta and the interval straddles delta (the re-expressed balloon guard).
# "per_seed_count" is the RETIRED v2 rule (>= 4/5 seeds exceed max(2 x reseed RMS, floor)); it is kept ONLY
# so the mutation check can show the O11 case depends on the change.
SCORING = "paired_mean"
SE_MULT = 2.0
NI_UNDERPOWERED_CD = True
# retired-rule constants (per_seed_count mode only)
FRAC_REQUIRED = 0.8                                                 # ">= 4/5", generalised to ceil(0.8 n)
MIN_RESEED_PER_SEED = 2
MIN_DELTAS_PER_STRATUM = 8
MIN_INT_DELTAS_PER_STRATUM = 4
BALLOON_FACTOR = 3.0

# Absolute floors (per 100 steps; contacts are a per-100 RATE over the 600-step window, not a count).
# v2 accepted rec-20260925-5fc6c256 (reward 0.90 / 2.4, contacts 1.6 / 4.8). v3: reward_change 0.43
# (rec-20260925-b89fe715; RT-5's measured NATIVE-reseed benign change noise), superseding 1.44
# (rec-20260925-aa066e96). Superiority tests use a floor as a floor on the per-seed SD (floor / 2);
# non-inferiority tests use it as the non-inferiority margin delta AND as the SD floor.
FLOORS = {
    BENIGN: {"reward": 0.90, "contacts": 1.6, "reward_change": 0.43},
    TRAPPED: {"reward": 2.4, "contacts": 4.8, "reward_change": None},  # P4 is benign-only
}

# v3 (O12, rec-20260925-a6132a2d). Stratum rule: env-only classifier, validity-gated.
#   env-only: CausalGridWorldV2(ENV_KW, seed=s) rolled CLS_STEPS steps by RandomPolicy(seed=s) (a function of
#   the env seed only), reset on done; hazard_trapped iff >= EARLY_MIN episodes end with length < 200.
#   VALIDITY GATE (v3, pre-registered because the pilot failed it): on a pilot of >= 20 env seeds x
#   CLS_VALIDITY_POLICY_SEEDS policy seeds, the one-way ICC of the early-termination count must be >=
#   ENV_ONLY_MIN_ICC AND each stratum must hold >= ENV_ONLY_MIN_CLASS_FRAC of the env seeds. Otherwise the
#   classifier is DEGENERATE and the pre-registered FALLBACK applies: the (env seed, agent seed) PAIR is
#   classified from NATIVE's own closed-loop steps 0-599 (the v2 rule), which is meaningful for the INT arms
#   only because they share NATIVE's init (SHARED_INIT). The fallback is a flagged open item (O12b).
STRATUM_RULE = "env_only_random_policy"
STRATUM_FALLBACK = "native_pair_shared_init"
# v3b (O12b, user 2026-09-25 ~18:50Z): the pair rule is DECIDED. The env-only classifier and its validity check are
# kept report-only (they document why); choose_stratum_rule returns the decided rule whatever the validity says.
STRATUM_DECIDED: Optional[str] = STRATUM_FALLBACK
CLS_STEPS = STRATUM_WINDOW
EARLY_MIN = 10
EP_CAP = 200
CLS_VALIDITY_POLICY_SEEDS = 5
ENV_ONLY_MIN_ICC = 0.5
ENV_ONLY_MIN_CLASS_FRAC = 0.10
# Pilot (bt0925-a1v3, ree-v3 origin/main f0331054133a, env seeds 2001-2040 x policy seeds s..s+4, 600 steps):
# every env seed had 18-28 early terminations (all health_depleted); ICC 0.023. First 8 env seeds verbatim
# (full table: evidence/planning/probes/a1_draft/env_only_classifier_pilot.json).
PILOT_ENV_ONLY_EARLY600 = {
    2001: [23, 22, 25, 24, 20], 2002: [21, 25, 23, 25, 22], 2003: [22, 23, 25, 20, 24], 2004: [23, 26, 21, 26, 21],
    2005: [22, 19, 21, 23, 25], 2006: [20, 25, 25, 22, 25], 2007: [20, 22, 23, 23, 23], 2008: [21, 23, 22, 22, 21],
}

# v3 (O12) shared init. NATIVE's module set is built from the agent seed FIRST; INT-only modules come from a
# separate generator (agent seed + INT_ONLY_OFFSET); every state_dict key the two agents share (same name,
# same shape) is copied from NATIVE into INT; then the global RNG is re-seeded with the agent seed before
# phase 1, identically in every arm. Harness-side (share_init); the probe showed seeding alone does not do it
# (flag-on modules registered before the obs encoders shift their init), and the copy does it exactly.
SHARED_INIT = True
INT_ONLY_OFFSET = 20_000

VARIANTS = ("CODEC", "ACT")          # user decision rec-20260925-6a675285: both, head-to-head.
SIMPLER_VARIANT = "ACT"              # E9 / DRAFT tie rule (prereg 8.3): the user may override at A1 time.
P1G_STRICT = True                    # RT-1, accepted (rec-20260925-5fc6c256): a 0 = 0 tie does NOT hold.

CEM_SCORE_WINDOW = "full"            # DRAFT until W4 (U4); one window for BOTH variants (E6)
W3_BUFFER_ACTION_FORMAT = "executed_as_fed_to_e2"                   # one format for BOTH variants (E7)
VARIANT_CONFIG = {
    "CODEC": dict(members=("codec", "terrain_prior"), use_action_space_proposals=False,
                  cem_score_window=CEM_SCORE_WINDOW, w3_buffer_action_format=W3_BUFFER_ACTION_FORMAT),
    "ACT": dict(members=(), use_action_space_proposals=True, action_space_first_action_mode="stratified",
                action_space_cem_score_horizon=CEM_SCORE_WINDOW, use_action_class_scaffold_candidates=False,
                w3_buffer_action_format=W3_BUFFER_ACTION_FORMAT),   # codec + prior NOT registered (E3)
}
SHUF_TARGETS = {
    "CODEC": ("harm_eval", "benefit_eval", "valuation_stream[GROUNDED]", "terrain_prior_target",
              "codec_decode_labels", "e2_world_action_labels(+babbling)"),
    "ACT": ("harm_eval", "benefit_eval", "valuation_stream[GROUNDED]", "e2_world_action_labels(+babbling)"),
}

REQUIRED_GATES = {
    "shared": ("C2_verdict_recorded", "I1_on_main", "W3_L2R_bar", "W4_a_spearman", "W4_c_vs_trained_action_blind",
               "W6_guard_green", "N0_pin_fetch"),
    "CODEC": ("W1_a_guard", "W1_b_roundtrip", "W1_c_decoded_norm", "W1_d_iter0_range",
              "W1_e_containment_vs_shuffled"),
    "ACT": ("GASP_a_guard", "GASP_b_valid_onehots", "GASP_c_bounded_rollouts", "GASP_d_coverage",
            "GASP_f_not_state_invariant"),
}
REPORTED_UNTIL_W5 = {
    "shared": ("W4_b_pick_in_qbest",),
    "CODEC": ("W1_e_consumer_mediated",),
    "ACT": ("GASP_e_consumer_mediated",),
}
VALUATION_MODES = ("GROUNDED", "ABSENT")  # fixed from C2 (V3-EXQ-1105a) verdict BEFORE any admitted seed runs

PASS, FAIL, CD, INVALID = "PASS", "FAIL", "CANNOT_DETERMINE", "INVALID"
HOLDS, NOT_HELD = "HOLDS", "NOT_HELD"


def arm_table(valuation_mode: str) -> List[Dict[str, Any]]:
    """Every arm, what it is, and whether it is scored. Order = execution order within a seed.
    v3: NATIVE-R1..R3 and INT-v-R1 no longer set a margin (the paired test's SD comes from the scored arms);
    they are REPORTED noise (RT-5 continuity; O13 asks the user whether to drop them)."""
    arms = [dict(name="NATIVE", agent_seed_offset=0, preset=None, trainer=False, shuffle=False,
                 role="comparator + (fallback rule) stratum source")]
    for k in range(1, N_RESEED + 1):
        arms.append(dict(name="NATIVE-R%d" % k, agent_seed_offset=k * AGENT_SEED_OFFSET, preset=None,
                         trainer=False, shuffle=False, role="REPORTED reseed noise only (v3)"))
    for v in VARIANTS:
        base = dict(preset="W6:%s:%s" % (v, valuation_mode), agent_seed_offset=0, config=VARIANT_CONFIG[v])
        arms.append(dict(name="INT-%s" % v, trainer=True, shuffle=False, role="tested", **base))
        arms.append(dict(name="INT-%s-SHUF" % v, trainer=True, shuffle=True, role="grounding control (P3)", **base))
        arms.append(dict(name="INT-%s-FROZEN" % v, trainer="off_in_closed_loop", shuffle=False,
                         role="learning control (P4)", **base))
        arms.append(dict(name="INT-%s-R1" % v, trainer=True, shuffle=False, preset=base["preset"],
                         config=VARIANT_CONFIG[v], agent_seed_offset=AGENT_SEED_OFFSET,
                         role="REPORTED INT reseed noise only (v3)"))
        if valuation_mode == "GROUNDED":
            arms.append(dict(name="INT-%s-NOVAL" % v, trainer=True, shuffle=False,
                             preset="W6:%s:ABSENT" % v, config=VARIANT_CONFIG[v], agent_seed_offset=0,
                             role="attribution ONLY (valuation vs other repairs; no verdict effect)"))
        # v3b (O15): babble attribution. Same agent seed + shared init as INT-v, same valuation_mode, trainer ON.
        arms.append(dict(name="INT-%s-NOBABBLE" % v, trainer=True, shuffle=False, preset=base["preset"],
                         config=dict(VARIANT_CONFIG[v], babbling_source="off"), agent_seed_offset=0,
                         role="babble attribution ONLY (secondary contrast; no verdict effect)"))
        arms.append(dict(name="INT-%s-BABBLE-DATA" % v, trainer=True, shuffle=False, preset=base["preset"],
                         config=dict(VARIANT_CONFIG[v], babbling_source="off", w3_inject="INT-%s retained babbling" % v),
                         agent_seed_offset=0, role="babble attribution ONLY (secondary contrast; no verdict effect)"))
    return arms


# ----------------------------------------------------------------------------- run side (skeleton)
def pin_substrate(pinned_sha: str) -> Dict[str, Any]:
    """MUST run before the first `import ree_core`. The sha is the 40-hex branch head recorded in the
    pre-registration/queue entry -- never a branch NAME. Marker: the W6 preset builder (fixed when W6 lands)."""
    from experiments._lib.substrate_pin import pin_ree_core, verify_pin, pin_manifest_block  # noqa: F401
    pin = pin_ree_core(pinned_sha)
    if len(pinned_sha) != 40 or pin.get("sha") != pinned_sha:   # R6 (see prereg sec 7)
        raise RuntimeError("R6: pinned sha mismatch")
    raise NotImplementedError("W6 preset marker not yet defined (W6 not built)")


def classify_stratum_env_only(env_seed: int, policy_seed: Optional[int] = None) -> Dict[str, Any]:
    """v3 O12 (rec-20260925-a6132a2d) CALL SITE. Env-only: no agent is constructed, so agent init cannot move it.
        env = CausalGridWorldV2(seed=env_seed, **ENV_KW); pol = RandomPolicy(env_seed if policy_seed is None
        else policy_seed)   # experiments/_lib/capability_eval.py RandomPolicy
        roll CLS_STEPS steps, env.reset() on done; early = #episodes ending with length < EP_CAP
        return {"stratum": TRAPPED if early >= EARLY_MIN else BENIGN, "early": early, "rule": STRATUM_RULE}
    Used ONLY if env_only_classifier_validity(...) on the pinned sha returns VALID (choose_stratum_rule).
    Stage S runs the validity pilot first (>= 20 env seeds x CLS_VALIDITY_POLICY_SEEDS policy seeds; env steps only,
    about 70 s on the Mac for 40 seeds). Reference implementation of the rollout:
    probes/a1_draft/env_only_classifier_pilot.py."""
    raise NotImplementedError


def build_env_agent(env_seed: int, agent_seed: int, preset: Optional[str]):
    """env seed and agent seed are SEPARATE (prereg sec 3): the env is constructed with seed=env_seed BEFORE any
    agent seeding. v3 SHARED INIT (O12), order of operations for EVERY arm:
      1. seed_all(agent_seed); native = REEAgent(NATIVE config)              # the NATIVE module set, from the agent seed
      2. if preset is None: agent = native
         else: seed_all(agent_seed + INT_ONLY_OFFSET); agent = REEAgent(preset config)   # INT-only modules: separate gen
               merged, report = share_init(native.state_dict(), agent.state_dict())
               agent.load_state_dict(merged, strict=True)                 # every shared key now == NATIVE's
               assert report["shape_mismatch"] is reported in the manifest (those keys stay INT-specific)
      3. seed_all(agent_seed)                                              # common runtime stream start, every arm
    The ree-v3 probe (prereg sec 3.2) showed step 2 without the copy does NOT share init: any flag-on module built
    in REEAgent.__init__ before the obs encoders (ree_core/agent.py:3416-3420 @ f0331054133a) shifts their init.
    Re-run probes/a1_draft/shared_init_probe.py against the W6 preset on the pinned sha before queueing (the W6
    members are not built yet)."""
    raise NotImplementedError


def run_arm(env_seed: int, arm: Dict[str, Any], sidecar_path: str, arms_already_read: List[str]):
    """Per-arm protocol: [dev epoch DEV_EPOCH_STEPS] -> [encoder warmup, identical protocol] ->
    [CLOSED_LOOP_STEPS closed-loop steps, recording per step: env reward, transition_type (I1-6
    step_outcome), done flag, action class]."""
    # Stratum (v3): if choose_stratum_rule(...) == STRATUM_RULE, the sidecar is written by Stage S from
    #     classify_stratum_env_only(env_seed) BEFORE any arm runs, and every arm (NATIVE included) calls
    #     require_stratum_sidecar first. Under STRATUM_FALLBACK it is the v2 order: NATIVE classifies itself at
    #     closed-loop step 599 (I1-5 classify_stratum), writes the sidecar before step 600, and every other arm
    #     calls require_stratum_sidecar before its first step.
    # Per window (FIRST, LAST) -- I1-6: coupled_acceptance.outcome_decomposition(tts[lo:hi], rewards[lo:hi])
    # INT-* arms, end of run: preconditions R0-R7 (prereg sec 7), as v2.
    # Reported: E3-picked class modal share (both), proposal_m4 (CODEC only), W4(b)-style pick-in-Q-best,
    #     action entropy, ARC-016 running_variance + commit rate, early terminations, per-group losses,
    #     share_init report (copied / shape-mismatch keys).
    raise NotImplementedError


# ----------------------------------------------------------------------------- shared init (pure)
def share_init(native_sd: Dict[str, Any], int_sd: Dict[str, Any]) -> Any:
    """v3 O12 shared-init merge (pure; works on any mapping whose values have a `.shape`).
    Returns (merged, report): merged = int_sd with every key that native_sd also has AT THE SAME SHAPE replaced by
    NATIVE's value. Shape-mismatched shared names are NOT copied (they are architecturally different modules)
    and are listed; INT-only keys are untouched (they carry the separate generator's init)."""
    if not SHARED_INIT:   # retired v2 behaviour (INT built from the same agent seed, nothing copied)
        return dict(int_sd), {"copied": [], "shape_mismatch": [], "int_only": sorted(k for k in int_sd if k not in native_sd),
                              "shared_init": False}
    merged, copied, mism = dict(int_sd), [], []
    for k, v in native_sd.items():
        if k not in int_sd:
            continue
        if tuple(getattr(v, "shape", ())) == tuple(getattr(int_sd[k], "shape", ())):
            merged[k] = v
            copied.append(k)
        else:
            mism.append(k)
    return merged, {"copied": copied, "shape_mismatch": mism,
                    "int_only": sorted(k for k in int_sd if k not in native_sd), "shared_init": True}


# ----------------------------------------------------------------------------- stratum rule (pure)
def env_only_classifier_validity(counts: Dict[int, List[int]]) -> Dict[str, Any]:
    """counts: env seed -> early-termination counts under CLS_VALIDITY_POLICY_SEEDS policy seeds (first = the
    classifier's own seed). One-way ICC(1) of the count across env seeds, and the class split under the
    classifier's own seed. VALID iff ICC >= ENV_ONLY_MIN_ICC and each class holds >= ENV_ONLY_MIN_CLASS_FRAC."""
    rows = [list(v) for v in counts.values()]
    n, k = len(rows), min(len(r) for r in rows)
    if n < 2 or k < 2:
        return {"verdict": CD, "reason": "need >= 2 env seeds x >= 2 policy seeds"}
    rows = [r[:k] for r in rows]
    gm = sum(sum(r) for r in rows) / (n * k)
    means = [sum(r) / k for r in rows]
    msb = k * sum((m - gm) ** 2 for m in means) / (n - 1)
    msw = sum((x - m) ** 2 for r, m in zip(rows, means) for x in r) / (n * (k - 1))
    icc = (msb - msw) / (msb + (k - 1) * msw) if (msb + (k - 1) * msw) > 0 else 0.0
    trapped = sum(1 for r in rows if r[0] >= EARLY_MIN)
    minority = min(trapped, n - trapped) / n
    ok = icc >= ENV_ONLY_MIN_ICC and minority >= ENV_ONLY_MIN_CLASS_FRAC
    return {"verdict": "VALID" if ok else "DEGENERATE", "icc": icc, "n_env": n, "k_policy": k,
            "trapped_frac": trapped / n, "minority_frac": minority}


def choose_stratum_rule(validity: Dict[str, Any]) -> Dict[str, Any]:
    """Pre-registered: the env-only rule (user decision) if its validity pilot is VALID on the pinned sha, else the
    fallback (flagged, O12b). Fixed before any admitted seed runs; recorded in the queue entry.
    v3b: O12b is decided (STRATUM_DECIDED) -- the pair rule applies regardless of the validity result, which is
    reported alongside."""
    if STRATUM_DECIDED is not None:
        return {"rule": STRATUM_DECIDED, "flag": None, "decided": "user 2026-09-25 (O12b)",
                "env_only_validity_reported": validity.get("verdict")}
    if validity.get("verdict") == "VALID":
        return {"rule": STRATUM_RULE, "flag": None}
    return {"rule": STRATUM_FALLBACK,
            "flag": "O12b: env-only classifier %s (ICC %s); pair-level NATIVE classification under shared init"
                    % (validity.get("verdict"), validity.get("icc"))}


# ----------------------------------------------------------------------------- scoring side (full)
def _rms(xs: Sequence[float]) -> float:
    return math.sqrt(sum(x * x for x in xs) / len(xs))


def _mean_sd(xs: Sequence[float]):
    n = len(xs)
    m = sum(xs) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1)) if n > 1 else float("inf")
    return n, m, sd


def window_stats(rec: Dict[str, Any]) -> Dict[str, float]:
    """rec per arm: {"reward_LAST", "reward_FIRST", "contacts_LAST", "grounded_LAST"} (per 100)."""
    out = dict(rec)
    out["reward_change"] = rec["reward_LAST"] - rec["reward_FIRST"]
    return out


def superiority(deltas: Sequence[float], floor: Optional[float], strict: bool = True) -> Dict[str, Any]:
    """Paired-mean superiority (O11): holds iff mean > SE_MULT x SD_used / sqrt(n), SD_used = max(SD, floor / 2).
    floor None -> no SD floor (P1g). strict=False is the retired `>=` P1g rule (mutation check only)."""
    n, m, sd = _mean_sd(deltas)
    sd_used = max(sd, floor / 2.0) if floor is not None else sd
    bound = SE_MULT * sd_used / math.sqrt(n)
    ok = (m > bound) if strict else (m >= bound)
    return {"kind": "superiority", "n": n, "mean": m, "sd": sd, "sd_used": sd_used, "bound": bound,
            "status": HOLDS if ok else NOT_HELD}


def noninferiority(deficits: Sequence[float], delta: float) -> Dict[str, Any]:
    """Paired-mean non-inferiority (O11): deficits are oriented so larger = worse for INT.
    HOLDS iff mean + h <= delta, h = SE_MULT x max(SD, delta / 2) / sqrt(n).
    CANNOT_DETERMINE (ni_underpowered; the re-expressed RT-2 balloon guard) iff h > delta and mean - h <= delta:
    even a zero observed deficit could not pass, and the data do not show INT worse than delta. Else NOT_HELD."""
    n, m, sd = _mean_sd(deficits)
    sd_used = max(sd, delta / 2.0)
    h = SE_MULT * sd_used / math.sqrt(n)
    if m + h <= delta:
        st = HOLDS
    elif NI_UNDERPOWERED_CD and h > delta and m - h <= delta:
        st = CD
    else:
        st = NOT_HELD
    return {"kind": "non_inferiority", "n": n, "mean": m, "sd": sd, "sd_used": sd_used, "half_width": h,
            "delta": delta, "upper": m + h, "status": st}


def margins(seeds: List[Dict[str, Any]], stratum: str) -> Dict[str, Any]:
    """NATIVE vs NATIVE-Rk noise: 2 x RMS of per-seed deltas, and (retired v2 rule) max(that, floor).
    v3: REPORTED (RT-5 continuity). Load-bearing only in the retired per_seed_count mode."""
    out: Dict[str, Any] = {}
    for m, key in (("reward", "reward_LAST"), ("contacts", "contacts_LAST"), ("reward_change", "reward_change")):
        floor = FLOORS[stratum][m]
        if floor is None:
            continue
        deltas, short = [], []
        for s in seeds:
            nat = window_stats(s["arms"]["NATIVE"])
            reps = [window_stats(s["arms"][a]) for a in s["arms"] if a.startswith("NATIVE-R")]
            if len(reps) < MIN_RESEED_PER_SEED:
                short.append(s["seed"])
            deltas += [nat[key] - r[key] for r in reps]
        if short or len(deltas) < MIN_DELTAS_PER_STRATUM:
            out[m] = {"verdict": CD, "reason": "reseeds short on %s / %d deltas" % (short, len(deltas))}
            continue
        sd = _rms(deltas)
        out[m] = {"verdict": "MEASURED", "rms": sd, "two_x": 2 * sd, "floor": floor,
                  "margin": max(2 * sd, floor), "floor_binding": floor >= 2 * sd, "n_deltas": len(deltas),
                  "ballooned": 2 * sd > BALLOON_FACTOR * floor}
    return out


def int_margins(seeds: List[Dict[str, Any]], stratum: str, v: str) -> Dict[str, Any]:
    """INT-v vs INT-v-R1 noise (RT-2). v3: REPORTED; load-bearing only in the retired per_seed_count mode."""
    out: Dict[str, Any] = {}
    for m, key in (("reward", "reward_LAST"), ("reward_change", "reward_change")):
        ds = [window_stats(s["arms"]["INT-%s" % v])[key] - window_stats(s["arms"]["INT-%s-R1" % v])[key]
              for s in seeds if "INT-%s-R1" % v in s["arms"]]
        if len(ds) < MIN_INT_DELTAS_PER_STRATUM:
            out[m] = {"verdict": CD, "reason": "%d INT reseed deltas" % len(ds)}
        else:
            out[m] = {"verdict": "MEASURED", "two_x": 2 * _rms(ds), "n_deltas": len(ds)}
    return out


def _need(n: int) -> int:
    return int(math.ceil(FRAC_REQUIRED * n - 1e-9))


def _per_seed_sup(deltas, margin, strict=True):
    c = sum(1 for d in deltas if (d > margin if strict else d >= margin))
    return {"kind": "superiority(per_seed_count)", "count": c, "n": len(deltas), "margin": margin,
            "status": HOLDS if c >= _need(len(deltas)) else NOT_HELD}


def _per_seed_ni(deficits, margin):
    c = sum(1 for d in deficits if d <= margin)
    return {"kind": "non_inferiority(per_seed_count)", "count": c, "n": len(deficits), "margin": margin,
            "status": HOLDS if c >= _need(len(deficits)) else NOT_HELD}


def score_variant(v: str, strata: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
    """Verdict ladder (prereg sec 8), evaluated in this order:
      1. INVALID  if any admitted seed has a failed precondition R0-R7 for this variant.
      2. CANNOT_DETERMINE if a stratum has < N_PER_STRATUM admitted seeds, or any criterion is CANNOT_DETERMINE
         (v3: a non-inferiority test that is underpowered, `ni_underpowered`).
      3. PASS iff P1b, P1g, P1t, P2 (both strata), P3 (both strata), P4 all HOLD; else FAIL."""
    T, S, F, N = "INT-%s" % v, "INT-%s-SHUF" % v, "INT-%s-FROZEN" % v, "NATIVE"
    res: Dict[str, Any] = {"variant": v, "criteria": {}, "scoring": SCORING}
    bad = [(s["seed"], s["preconditions"][v]) for g in strata.values() for s in g
           if not all(s["preconditions"][v].values())]
    if bad:
        res.update(verdict=INVALID, reason="precondition failed: %s" % bad)
        return res
    for g in (BENIGN, TRAPPED):
        if len(strata.get(g, [])) < N_PER_STRATUM[g]:
            res.update(verdict=CD, reason="stratum %s under-admitted (%d < %d)" % (g, len(strata.get(g, [])),
                                                                                  N_PER_STRATUM[g]))
            return res
    W = lambda s, a: window_stats(s["arms"][a])  # noqa: E731
    b, t = strata[BENIGN], strata[TRAPPED]
    fb, ft = FLOORS[BENIGN], FLOORS[TRAPPED]
    d = {
        "P1b": [W(s, T)["reward_LAST"] - W(s, N)["reward_LAST"] for s in b],
        "P1g": [W(s, T)["grounded_LAST"] - W(s, N)["grounded_LAST"] for s in b],
        "P1t": [W(s, N)["reward_LAST"] - W(s, T)["reward_LAST"] for s in t],          # deficit
        "P2b": [W(s, T)["contacts_LAST"] - W(s, N)["contacts_LAST"] for s in b],       # deficit
        "P2t": [W(s, T)["contacts_LAST"] - W(s, N)["contacts_LAST"] for s in t],       # deficit
        "P3b": [W(s, T)["reward_LAST"] - W(s, S)["reward_LAST"] for s in b],
        "P3t": [W(s, T)["reward_LAST"] - W(s, S)["reward_LAST"] for s in t],
        "P4": [W(s, T)["reward_change"] - W(s, F)["reward_change"] for s in b],
    }
    M = {g: margins(strata[g], g) for g in (BENIGN, TRAPPED)}
    IM = {g: int_margins(strata[g], g, v) for g in (BENIGN, TRAPPED)}
    res["reported_reseed_noise"] = {"native": M, "int": IM}
    c = res["criteria"]
    if SCORING == "paired_mean":
        c["P1b"] = superiority(d["P1b"], fb["reward"])
        c["P1g"] = superiority(d["P1g"], None, strict=P1G_STRICT)      # RT-1: a 0 = 0 tie never holds
        c["P1t"] = noninferiority(d["P1t"], ft["reward"])
        c["P2b"] = noninferiority(d["P2b"], fb["contacts"])
        c["P2t"] = noninferiority(d["P2t"], ft["contacts"])
        c["P3b"] = superiority(d["P3b"], fb["reward"])
        c["P3t"] = superiority(d["P3t"], ft["reward"])
        c["P4"] = superiority(d["P4"], fb["reward_change"])
        sup_b = c["P1b"]["bound"]
    else:  # retired v2 rule: per-seed counts against max(NATIVE reseed, INT reseed, floor) margins + balloon guard
        need = [(BENIGN, "reward"), (BENIGN, "contacts"), (BENIGN, "reward_change"), (TRAPPED, "reward"),
                (TRAPPED, "contacts")]
        cdm = [(g, m) for g, m in need if M[g][m]["verdict"] == CD]
        cdm += [("INT:" + g, m) for g, m in ((BENIGN, "reward"), (BENIGN, "reward_change"), (TRAPPED, "reward"))
                if IM[g][m]["verdict"] == CD]
        if cdm:
            res.update(verdict=CD, reason="margin not computable: %s" % cdm)
            return res
        bal = [(g, m) for g, m in ((TRAPPED, "reward"), (BENIGN, "contacts"), (TRAPPED, "contacts"))
               if M[g][m]["ballooned"]]
        if bal:
            res.update(verdict=CD, reason="margin_ballooned: %s" % bal)
            return res
        sup_b = max(M[BENIGN]["reward"]["margin"], IM[BENIGN]["reward"]["two_x"])
        sup_t = max(M[TRAPPED]["reward"]["margin"], IM[TRAPPED]["reward"]["two_x"])
        sup_chg = max(M[BENIGN]["reward_change"]["margin"], IM[BENIGN]["reward_change"]["two_x"])
        c["P1b"] = _per_seed_sup(d["P1b"], sup_b)
        c["P1g"] = _per_seed_sup(d["P1g"], 0.0, strict=P1G_STRICT)
        c["P1t"] = _per_seed_ni(d["P1t"], M[TRAPPED]["reward"]["margin"])
        c["P2b"] = _per_seed_ni(d["P2b"], M[BENIGN]["contacts"]["margin"])
        c["P2t"] = _per_seed_ni(d["P2t"], M[TRAPPED]["contacts"]["margin"])
        c["P3b"] = _per_seed_sup(d["P3b"], sup_b)
        c["P3t"] = _per_seed_sup(d["P3t"], sup_t)
        c["P4"] = _per_seed_sup(d["P4"], sup_chg)
    held = {k: r["status"] == HOLDS for k, r in c.items()}
    res["held"] = held
    res["gains_P1b"] = {s["seed"]: g for s, g in zip(b, d["P1b"])}
    res["gain_P1b_mean"] = sum(d["P1b"]) / len(d["P1b"])
    res["attribution"] = attribution(v, b)
    res["init_dominance"] = init_dominance(strata, v)     # REPORT-ONLY (prereg 6.6); nothing below reads it
    res["babble_attribution"] = babble_attribution(strata, v)   # SECONDARY (prereg 6.7); own rule, no verdict effect
    cds = [k for k, r in c.items() if r["status"] == CD]
    if cds:
        res.update(verdict=CD, reason="ni_underpowered (non-inferiority cannot pass at this noise): %s" % cds)
        return res
    res["verdict"] = PASS if all(held.values()) else FAIL
    if BABBLE_CONTRAST_GATES and res["babble_attribution"]["label"] != "behaviour_babbling_carries":
        res["verdict"] = FAIL   # RETIRED/NEVER-ADOPTED rule, present only so the mutation check can show the separation
    if res["verdict"] == FAIL:
        sig = []
        if held["P1t"] and not held["P1b"]:
            sig.append("trapped-only gain (R5b+R2 signature)")
        if held["P1b"] and not held["P1g"]:
            sig.append("reward gain carried by approach shaping, not contacts/consumptions")
        if held["P1b"] and not (held["P3b"] and held["P3t"]):
            sig.append("grounding does not matter")
        if held["P1b"] and not held["P4"]:
            sig.append("architecture helps, waking learning does not")
        if (not held["P1b"]) and held["P1g"] and held["P2b"] and held["P2t"] and held["P3b"] and held["P3t"]:
            sig.append("gain too small for the margin (6.4)")
        # P4 is the only missing criterion and INT's FIRST window is, on the paired mean, within the benign reward
        # bound of NATIVE's -> headroom-limited; reported, never re-scored.
        others = [k for k in held if k != "P4"]
        first_d = [W(s, T)["reward_FIRST"] - W(s, N)["reward_FIRST"] for s in b]
        near = abs(sum(first_d) / len(first_d)) <= sup_b
        if (not held["P4"]) and all(held[k] for k in others) and near:
            sig.append("P4 headroom-limited (6.4)")
        res["fail_signatures"] = sig
    return res


# ----------------------------------------------------------------------------- init-dominance readout (REPORT-ONLY)
def _entropy_bits(counts: Dict[Any, float]) -> float:
    tot = float(sum(counts.values()))
    return -sum((c / tot) * math.log(c / tot, 2) for c in counts.values() if c > 0) if tot else float("nan")


def _modal_share(counts: Dict[Any, float]) -> float:
    tot = float(sum(counts.values()))   # probes/a1_rt5/analyze_rt5.py modal_share, same definition
    return max(counts.values()) / tot if tot else float("nan")


def _tv(a: Dict[Any, float], b: Dict[Any, float]) -> float:
    ta, tb = float(sum(a.values())), float(sum(b.values()))
    keys = set(a) | set(b)
    return 0.5 * sum(abs(a.get(k, 0) / ta - b.get(k, 0) / tb) for k in keys) if ta and tb else float("nan")


def init_dominance(strata: Dict[str, List[Dict[str, Any]]], v: str) -> Dict[str, Any]:
    """v3 addendum (user direction 2026-09-25 ~18:20Z; prereg 6.6). PRE-REGISTERED, REPORT-ONLY, NEVER GATING.
    Uses only arms A1 already runs: family NATIVE = NATIVE vs NATIVE-R1..R3; family INT = INT-v vs INT-v-R1.
    Per arm (optional fields, RT-5 format): `action_counts` {class: count} over the closed loop, `own_stratum` (the
    RT-5 / I1-5 classify rule applied to THAT arm's own closed-loop steps 0-599).
    Per family and stratum: mean modal-action share and action entropy (bits) over base + reseed arms; between-reseed
    spread 2 x RMS of (base - reseed) reward_LAST and contacts_LAST (probes/a1_rt5/analyze_rt5.py two_rms); mean
    total-variation distance between base and reseed action histograms; own-label concordance (reseed own_stratum ==
    base own_stratum). Predicted direction, STATED NOT ASSUMED: INT spread < NATIVE spread, INT concordance >
    NATIVE concordance, INT modal share lower / entropy higher. `direction_observed` reports it; nothing reads it."""
    fam = {"NATIVE": ("NATIVE", [a for a in ("NATIVE-R%d" % k for k in range(1, N_RESEED + 1))]),
           "INT": ("INT-%s" % v, ["INT-%s-R1" % v])}
    out: Dict[str, Any] = {"report_only": True, "gates_nothing": True}
    for g in (BENIGN, TRAPPED):
        blk: Dict[str, Any] = {}
        for fname, (base, reps) in fam.items():
            dr, dc, tvs, conc, ms, ent = [], [], [], [0, 0], [], []
            for s in strata.get(g, []):
                arms = s["arms"]
                if base not in arms:
                    continue
                b = arms[base]
                for r in [x for x in reps if x in arms]:
                    ra = arms[r]
                    dr.append(b["reward_LAST"] - ra["reward_LAST"])
                    dc.append(b["contacts_LAST"] - ra["contacts_LAST"])
                    if b.get("action_counts") and ra.get("action_counts"):
                        tvs.append(_tv(b["action_counts"], ra["action_counts"]))
                    if b.get("own_stratum") is not None and ra.get("own_stratum") is not None:
                        conc[0] += int(ra["own_stratum"] == b["own_stratum"])
                        conc[1] += 1
                for a in [base] + reps:
                    if a in arms and arms[a].get("action_counts"):
                        ms.append(_modal_share(arms[a]["action_counts"]))
                        ent.append(_entropy_bits(arms[a]["action_counts"]))
            avg = lambda xs: (sum(xs) / len(xs)) if xs else None  # noqa: E731
            blk[fname] = {"n_pairs": len(dr), "spread_reward_2rms": 2 * _rms(dr) if dr else None,
                          "spread_contacts_2rms": 2 * _rms(dc) if dc else None, "action_tv_mean": avg(tvs),
                          "own_label_concordance": (conc[0] / conc[1]) if conc[1] else None, "concordance_n": conc,
                          "modal_share_mean": avg(ms), "entropy_bits_mean": avg(ent)}
        n_, i_ = blk["NATIVE"], blk["INT"]
        cmp = lambda a, b, f: (None if a is None or b is None else f(a, b))  # noqa: E731
        blk["direction_observed"] = {
            "int_reward_spread_lower": cmp(i_["spread_reward_2rms"], n_["spread_reward_2rms"], lambda a, b: a < b),
            "int_contacts_spread_lower": cmp(i_["spread_contacts_2rms"], n_["spread_contacts_2rms"], lambda a, b: a < b),
            "int_concordance_higher": cmp(i_["own_label_concordance"], n_["own_label_concordance"], lambda a, b: a > b),
            "int_entropy_higher": cmp(i_["entropy_bits_mean"], n_["entropy_bits_mean"], lambda a, b: a > b),
        }
        out[g] = blk
    return out


# ----------------------------------------------------------------------------- babble attribution (SECONDARY, own rule)
BABBLE_CONTRAST_GATES = False        # pre-registered False: the contrast never moves A1's verdict (mutation-checked)
MODAL_SHARE_FLOOR = 0.05             # DRAFT SD floor (2 x 0.025) for modal-share deltas; no prior measurement


def babble_attribution(strata: Dict[str, List[Dict[str, Any]]], v: str) -> Dict[str, Any]:
    """v3b O15 (user 2026-09-25). SECONDARY, pre-registered, own rule; never an A1 criterion.
    Arms (same agent seed, shared init): T = INT-v (behaviour babbling), D = INT-v-BABBLE-DATA (own phase 1 native,
    W3 member fed T's retained babbling transitions at the same phase-1 step indices), O = INT-v-NOBABBLE (no babbling).
    Init-dominance measure per arm: modal-action share over the closed loop (lower = weaker init attractor); under shared
    init also TV(arm, NATIVE same seed) (higher = further from the init's native policy). Pooled over all admitted seeds.
      behaviour  = sup(modal(D) - modal(T), MODAL_SHARE_FLOOR)   behaviour babbling beyond its data
      data       = sup(modal(O) - modal(D), MODAL_SHARE_FLOOR)   babbling data alone
      label: behaviour_babbling_carries (behaviour and not data) | babbling_data_carries (data and not behaviour) |
             both | neither_detected. CANNOT_DETERMINE if any seed lacks T/D/O action counts.
    Prediction (stated, not assumed): if babbling prevents an init attractor, behaviour holds and D ~ O; if babbling only
    supplies world-head data, data holds and D ~ T. Reward contrasts (benign, floor 0.90) are reported alongside."""
    T, D, O = "INT-%s" % v, "INT-%s-BABBLE-DATA" % v, "INT-%s-NOBABBLE" % v
    seeds = [s for g in (BENIGN, TRAPPED) for s in strata.get(g, [])]
    have = [s for s in seeds if all(a in s["arms"] and s["arms"][a].get("action_counts") for a in (T, D, O))]
    if not seeds or len(have) < len(seeds):
        return {"label": CD, "reason": "babble arms or action counts missing on %d seed(s)" % (len(seeds) - len(have)),
                "secondary": True}
    ms = lambda s, a: _modal_share(s["arms"][a]["action_counts"])  # noqa: E731
    beh = superiority([ms(s, D) - ms(s, T) for s in have], MODAL_SHARE_FLOOR)
    dat = superiority([ms(s, O) - ms(s, D) for s in have], MODAL_SHARE_FLOOR)
    bh, dh = beh["status"] == HOLDS, dat["status"] == HOLDS
    label = ("behaviour_babbling_carries" if bh and not dh else "babbling_data_carries" if dh and not bh
             else "both" if bh and dh else "neither_detected")
    tv = {}
    for a in (T, D, O):
        xs = [_tv(s["arms"][a]["action_counts"], s["arms"]["NATIVE"]["action_counts"]) for s in have
              if s["arms"]["NATIVE"].get("action_counts")]
        tv[a] = (sum(xs) / len(xs)) if xs else None
    b = [s for s in strata.get(BENIGN, []) if s in have]
    rw = {}
    if len(b) >= 2:
        W = lambda s, a: s["arms"][a]["reward_LAST"]  # noqa: E731
        rw = {"behaviour_reward": superiority([W(s, T) - W(s, D) for s in b], FLOORS[BENIGN]["reward"])["status"],
              "data_reward": superiority([W(s, D) - W(s, O) for s in b], FLOORS[BENIGN]["reward"])["status"]}
    return {"label": label, "secondary": True, "gates_a1": BABBLE_CONTRAST_GATES, "behaviour_test": beh,
            "data_test": dat, "tv_to_native_mean": tv, "reward_contrasts_benign": rw}


def head_to_head(results: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """A1 verdict over the two proposal variants (prereg sec 8.3). v3: the both-PASS comparison is a paired-mean
    superiority test on the per-seed difference of the two variants' benign P1b gains (floor: benign reward)."""
    passed = [v for v, r in results.items() if r["verdict"] == PASS]
    if any(r["verdict"] == INVALID for r in results.values()):
        return {"verdict": INVALID, "winner": None, "note": "a variant is INVALID; fix and re-run (lettered id)"}
    if not passed:
        cds = [v for v, r in results.items() if r["verdict"] == CD]
        return {"verdict": CD if len(cds) == len(results) else FAIL, "winner": None}
    if len(passed) == 1:
        return {"verdict": PASS, "winner": passed[0]}
    a, c = passed[0], passed[1]
    seeds = sorted(set(results[a]["gains_P1b"]) & set(results[c]["gains_P1b"]))
    diff = [results[a]["gains_P1b"][s] - results[c]["gains_P1b"][s] for s in seeds]
    fwd = superiority(diff, FLOORS[BENIGN]["reward"])
    rev = superiority([-x for x in diff], FLOORS[BENIGN]["reward"])
    if fwd["status"] == HOLDS:
        return {"verdict": PASS, "winner": a, "note": "both PASS; paired gain difference beyond its bound"}
    if rev["status"] == HOLDS:
        return {"verdict": PASS, "winner": c, "note": "both PASS; paired gain difference beyond its bound"}
    return {"verdict": PASS, "winner": SIMPLER_VARIANT,
            "note": "both PASS within the paired bound; DRAFT tie rule: INT-ACT is simpler -- it removes the decoder "
                    "and terrain_prior from the act path (constructed but unused) and adds no trainable parameters. "
                    "Tie rule owner: the user, at A1 time (O2)"}


def attribution(v: str, benign: List[Dict[str, Any]]) -> Dict[str, Any]:
    """NOVAL attribution (rec-20260925-c2519d92). REPORTED ONLY: it never changes a verdict. GROUNDED mode only.
    v3: paired-mean superiority tests (floor: benign reward), like the criteria.
      valuation_carries  : INT-v beats INT-v-NOVAL, AND INT-v-NOVAL does not beat NATIVE
      other_repairs_carry: INT-v-NOVAL beats NATIVE, AND INT-v does not beat INT-v-NOVAL
      both / undetermined otherwise. A NOVAL arm missing on some seed of a GROUNDED run -> CANNOT_DETERMINE."""
    TN = "INT-%s-NOVAL" % v
    have = [s for s in benign if TN in s["arms"]]
    if not have:
        return {"label": "not_run (ABSENT mode)"}
    if len(have) < len(benign):
        return {"label": CD, "reason": "NOVAL missing on %d seed(s)" % (len(benign) - len(have))}
    W = lambda s, a: window_stats(s["arms"][a])  # noqa: E731
    fl = FLOORS[BENIGN]["reward"]
    val = superiority([W(s, "INT-%s" % v)["reward_LAST"] - W(s, TN)["reward_LAST"] for s in have], fl)
    oth = superiority([W(s, TN)["reward_LAST"] - W(s, "NATIVE")["reward_LAST"] for s in have], fl)
    vc, oc = val["status"] == HOLDS, oth["status"] == HOLDS
    label = ("valuation_carries" if vc and not oc else "other_repairs_carry" if oc and not vc
             else "both" if vc and oc else "undetermined")
    return {"label": label, "valuation_test": val, "noval_vs_native_test": oth}


def a1_queueable(gates: Dict[str, Dict[str, bool]], valuation_mode: Optional[str]) -> Dict[str, Any]:
    """Pre-A1 hold (rec-20260925-38b81685): A1 queues only when BOTH variants pass their member gates plus the shared
    gates, and only once valuation_mode is fixed. v2b (rec-20260925-a16786f5): REPORTED_UNTIL_W5 never HOLDs."""
    missing = []
    if valuation_mode not in VALUATION_MODES:
        missing.append("valuation_mode not fixed (C2 verdict)")
    for grp, names in REQUIRED_GATES.items():
        for n in names:
            if not gates.get(grp, {}).get(n, False):
                missing.append("%s:%s" % (grp, n))
    reported = {"%s:%s" % (grp, n): gates.get(grp, {}).get(n, "not_run")
                for grp, names in REPORTED_UNTIL_W5.items() for n in names}
    return {"verdict": "QUEUEABLE" if not missing else "HOLD", "missing": missing, "reported": reported}


def oracle_diagnostic(states: List[Dict[str, Any]], pools: Sequence[str] = ("INT-CODEC", "INT-ACT", "NATIVE-POOL")
                      ) -> Dict[str, Any]:
    """REPORT-ONLY oracle diagnostic (rec-20260925-a16786f5): env-Q stands in for E3's valuation on each pool.
    Per pool: fraction of states whose oracle pick is in the env-Q-best set, and mean regret. Feeds nothing."""
    out: Dict[str, Any] = {"report_only": True}
    for p in pools:
        hit, regret, n = 0, 0.0, 0
        for st in states:
            if p not in st["pools"] or not st["pools"][p]:
                continue
            q = st["q"]
            qmax = max(q.values())
            best_in_pool = max(q[c] for c in st["pools"][p])
            hit += int(best_in_pool >= qmax - 1e-9)
            regret += qmax - best_in_pool
            n += 1
        out[p] = ({"n_states": n, "oracle_pick_in_qbest": hit / n, "mean_regret": regret / n} if n
                  else {"n_states": 0, "verdict": CD})
    return out


def cost_estimate(valuation_mode: str, s_native_arm=(123.0, 180.0, 439.0), int_mult=(1.2, 1.3, 1.4),
                  int_arm_s_t2_trapped: Optional[float] = None) -> Dict[str, Any]:
    """v3 cost (prereg sec 11): per-arm wall from RT-5's MEASURED NATIVE full arms (123 / ~180 / 439 s for
    5,400 agent steps on the shared Mac), INT arms x the DRAFT trainer multiplier. Optional scenario: INT arms on
    trapped seeds at the T2 agent's measured 0.2 s/step (int_arm_s_t2_trapped seconds per INT arm)."""
    arms = arm_table(valuation_mode)
    n_nat = sum(1 for a in arms if a["preset"] is None)
    n_int = len(arms) - n_nat
    n_seeds = N_PER_STRATUM[BENIGN] + N_PER_STRATUM[TRAPPED]
    out = {"arms_native_family": n_nat, "arms_int": n_int, "admitted_seeds": n_seeds}
    for lab, sn, mu in zip(("low", "mid", "high"), s_native_arm, int_mult):
        per_seed = n_nat * sn + n_int * sn * mu
        out[lab] = {"per_seed_h": per_seed / 3600.0, "total_cpu_h": n_seeds * per_seed / 3600.0}
    if int_arm_s_t2_trapped is not None:
        per_b = n_nat * s_native_arm[1] + n_int * s_native_arm[1] * int_mult[1]
        per_t = n_nat * s_native_arm[1] + n_int * int_arm_s_t2_trapped * int_mult[1]
        out["t2_like_trapped"] = {"total_cpu_h": (N_PER_STRATUM[BENIGN] * per_b + N_PER_STRATUM[TRAPPED] * per_t) / 3600.0}
    return out


# ----------------------------------------------------------------------------- self-test (synthetic)
def _sgn(seed: int) -> int:
    return 1 if seed % 2 else -1


def _synthetic(stratum: str, seed: int, gain: float, *, shuf_gain: Optional[float] = None, frozen_learn: float = 0.0,
               contacts_up: float = 0.0, grounded_delta: float = 0.1, noise: float = 0.05, n_reseed: int = 3,
               pre_ok: bool = True, int_noise: float = 0.05, g_tie: bool = False,
               noval_gain: Optional[float] = None, jit: float = 0.0, cjit: float = 0.0,
               babble: Optional[Sequence[float]] = None) -> Dict[str, Any]:
    """jit / cjit: INT-v's reward_LAST / contacts_LAST move by +-jit / +-cjit alternating over seeds, so the paired
    deltas have a nonzero across-seed SD (mean unchanged over an even number of seeds)."""
    base = -0.5 if stratum == BENIGN else -3.0
    def rec(r_last, r_first, c_last, g_last):
        return {"reward_LAST": r_last, "reward_FIRST": r_first, "contacts_LAST": c_last, "grounded_LAST": g_last}
    g0 = 0.0 if g_tie else -0.2
    arms = {"NATIVE": rec(base, base, 2.0, g0)}
    for k in range(1, n_reseed + 1):
        d = noise * (1 if (seed + k) % 2 else -1)
        arms["NATIVE-R%d" % k] = rec(base + d, base + d, 2.0 + d, -0.2)
    sg = gain / 2 if shuf_gain is None else shuf_gain
    j, cj = jit * _sgn(seed), cjit * _sgn(seed)
    for v in VARIANTS:
        arms["INT-%s" % v] = rec(base + gain + j, base, 2.0 + contacts_up + cj, g0 if g_tie else -0.2 + grounded_delta)
        d = int_noise * _sgn(seed)
        arms["INT-%s-R1" % v] = rec(base + gain + d, base, 2.0 + contacts_up, -0.2 + grounded_delta)
        arms["INT-%s-SHUF" % v] = rec(base + sg, base, 2.0, -0.2)
        arms["INT-%s-FROZEN" % v] = rec(base + frozen_learn, base, 2.0, -0.2)
        if noval_gain is not None:
            arms["INT-%s-NOVAL" % v] = rec(base + noval_gain, base, 2.0, -0.2)
        if babble is not None:   # (modal share of T, D, O); NATIVE collapsed at 0.9
            arms["NATIVE"]["action_counts"] = {0: 900, 1: 100}
            for nm, m in zip(("INT-%s" % v, "INT-%s-BABBLE-DATA" % v, "INT-%s-NOBABBLE" % v), babble):
                mj = m + 0.02 * _sgn(seed)
                if nm != "INT-%s" % v:
                    arms[nm] = rec(base + gain / 2, base, 2.0, -0.2)
                arms[nm]["action_counts"] = {0: round(1000 * mj), 1: 1000 - round(1000 * mj)}
    return {"seed": seed, "stratum": stratum, "arms": arms,
            "preconditions": {v: {"R0": pre_ok, "R1": True, "R2": True, "R3": True, "R4": True, "R5": True,
                                  "R6": True, "R7": True} for v in VARIANTS}}


def _n(g: str) -> int:
    return N_PER_STRATUM[g]


def _seeds(g: str, gain: float, **kw) -> List[Dict[str, Any]]:
    return [_synthetic(g, s, gain, **kw) for s in range(_n(g))]


def _good(g: str, **kw) -> List[Dict[str, Any]]:
    # P3t needs INT > SHUF on trapped too: give SHUF a large deficit there.
    return _seeds(g, 1.5 if g == BENIGN else 0.0, shuf_gain=0.0 if g == BENIGN else -3.0, **kw)


def _all_gates(**off) -> Dict[str, Dict[str, bool]]:
    g = {grp: {n: True for n in names} for grp, names in REQUIRED_GATES.items()}
    for key, val in off.items():
        grp, n = key.split("__", 1)
        g[grp][n] = val
    return g


class _T:
    """Toy tensor for the share_init cases (shape + a value)."""
    def __init__(self, shape, val):
        self.shape, self.val = tuple(shape), val

    def __eq__(self, o):
        return isinstance(o, _T) and self.shape == o.shape and self.val == o.val


def _cases() -> List[Any]:
    """(name, kind, thunk, want)."""
    B, T = BENIGN, TRAPPED
    sv = lambda strata: score_variant("CODEC", strata)["verdict"]  # noqa: E731
    C = []
    add = lambda name, kind, th, want: C.append((name, kind, th, want))  # noqa: E731
    add("all criteria hold", "score", lambda: sv({B: _good(B), T: _good(T)}), PASS)
    add("P1b fails (no benign gain)", "score", lambda: sv({B: _seeds(B, 0.1, shuf_gain=-1.0), T: _good(T)}), FAIL)
    add("P1g fails (gain carried by shaping)", "score",
        lambda: sv({B: _seeds(B, 1.5, shuf_gain=0.0, grounded_delta=-0.3), T: _good(T)}), FAIL)
    add("P2 fails (undirected: contacts up)", "score",
        lambda: sv({B: _seeds(B, 1.5, shuf_gain=0.0, contacts_up=3.0), T: _good(T)}), FAIL)
    add("P3 fails (SHUF as good)", "score", lambda: sv({B: _seeds(B, 1.5, shuf_gain=1.5), T: _good(T)}), FAIL)
    add("P4 fails (FROZEN learns as much)", "score",
        lambda: sv({B: _seeds(B, 1.5, shuf_gain=0.0, frozen_learn=1.5), T: _good(T)}), FAIL)
    add("P1t fails (trapped much worse)", "score",
        lambda: sv({B: _good(B), T: _seeds(T, -5.0, shuf_gain=-9.0)}), FAIL)
    add("stratum under-admitted", "score", lambda: sv({B: _good(B), T: _good(T)[:-1]}), CD)
    add("v3 reseeds short -> still scored (reseed noise is reported only)", "score",
        lambda: sv({B: _seeds(B, 1.5, shuf_gain=0.0, n_reseed=1), T: _good(T)}), PASS)
    add("precondition failed -> INVALID", "score",
        lambda: sv({B: [_synthetic(B, 0, 1.5, pre_ok=False)] + _good(B)[1:], T: _good(T)}), INVALID)
    add("floor binds: constant gain 0.2 < 0.90/sqrt(12)", "score",
        lambda: sv({B: _seeds(B, 0.2, shuf_gain=-1.0, noise=0.0), T: _good(T)}), FAIL)
    add("RT-1 P1g tie 0=0 (shaping-only gain) fails", "score",
        lambda: sv({B: _seeds(B, 1.5, shuf_gain=0.0, g_tie=True), T: _good(T)}), FAIL)
    add("RT-2 re-expressed: noisy non-inferiority -> CD ni_underpowered", "score",
        lambda: sv({B: _good(B), T: _seeds(T, 0.0, shuf_gain=-40.0, jit=8.0)}), CD)
    add("RT-2: INT noisier (paired SD) -> P1b fails", "score",
        lambda: sv({B: _seeds(B, 1.5, shuf_gain=0.0, jit=3.0), T: _good(T)}), FAIL)
    # v3 O11 core cases
    add("O11 per-seed counting fails, paired mean passes (gain 0.7 +- 0.3, reseed noise 0.85)", "score",
        lambda: sv({B: _seeds(B, 0.7, shuf_gain=0.0, jit=0.3, noise=0.85), T: _good(T)}), PASS)
    add("O11 noise must NOT pass (gain 0.1 +- 1.0)", "score",
        lambda: sv({B: _seeds(B, 0.1, shuf_gain=-2.0, jit=1.0), T: _good(T)}), FAIL)
    add("O11 pure noise, zero mean gain -> P1b not held", "crit",
        lambda: score_variant("CODEC", {B: _seeds(B, 0.0, shuf_gain=-2.0, jit=1.5), T: _good(T)})["held"]["P1b"], False)
    # NI with the SD floored at delta/2: a tight deficit must sit below delta - 2 x (delta/2)/sqrt(n) = 2.4 - 0.69.
    add("O11 NI: INT reliably worse by 1.5 (tight) on trapped -> P1t holds", "crit",
        lambda: score_variant("CODEC", {B: _good(B), T: _seeds(T, -1.5, shuf_gain=-9.0, jit=0.1)})["held"]["P1t"], True)
    add("O11 NI: INT reliably worse by 2.0 (tight) -> P1t not held (SD floor delta/2)", "crit",
        lambda: score_variant("CODEC", {B: _good(B), T: _seeds(T, -2.0, shuf_gain=-9.0, jit=0.1)})["held"]["P1t"], False)
    # v3 change floor 0.43 (rec-20260925-b89fe715): learning gain over FROZEN 0.3 > 0.43/sqrt(12) = 0.124; < 1.44/sqrt(12)
    add("v3 P4 learning gain 0.3 holds at floor 0.43", "score",
        lambda: sv({B: _seeds(B, 1.5, shuf_gain=0.0, frozen_learn=1.2), T: _good(T)}), PASS)
    add("P4-only FAIL, FIRST near NATIVE -> headroom signature", "sig",
        lambda: "P4 headroom-limited (6.4)" in score_variant("CODEC", {B: _seeds(B, 1.5, shuf_gain=0.0, frozen_learn=1.45),
                                                                     T: _good(T)}).get("fail_signatures", []), True)
    # head-to-head (8.3), v3 paired
    def h2h(rc, ra, gc=1.3, ga=1.2, jc=0.0):
        n = _n(B)
        r = {"CODEC": {"verdict": rc, "gains_P1b": {s: gc + jc * _sgn(s) for s in range(n)}},
             "ACT": {"verdict": ra, "gains_P1b": {s: ga for s in range(n)}}}
        out = head_to_head(r)
        return (out["verdict"], out["winner"])
    add("h2h both PASS within bound -> tie rule (ACT)", "h2h", lambda: h2h(PASS, PASS), (PASS, "ACT"))
    add("h2h both PASS, CODEC ahead beyond the paired bound", "h2h", lambda: h2h(PASS, PASS, gc=2.5), (PASS, "CODEC"))
    add("h2h both PASS, CODEC ahead on mean but noisy -> tie rule", "h2h", lambda: h2h(PASS, PASS, gc=2.0, jc=2.0), (PASS, "ACT"))
    add("h2h only CODEC PASS", "h2h", lambda: h2h(PASS, FAIL), (PASS, "CODEC"))
    add("h2h one INVALID -> A1 INVALID", "h2h", lambda: h2h(INVALID, PASS), (INVALID, None))
    add("h2h both CD -> CD", "h2h", lambda: h2h(CD, CD), (CD, None))
    add("h2h FAIL + CD -> FAIL", "h2h", lambda: h2h(FAIL, CD), (FAIL, None))
    def attr(benign):
        r = score_variant("CODEC", {B: benign, T: _good(T)})
        return (r["verdict"], r["attribution"]["label"])
    add("attr NOVAL no gain -> valuation carries", "attr", lambda: attr(_good(B, noval_gain=0.0)), (PASS, "valuation_carries"))
    add("attr NOVAL full gain -> other repairs carry", "attr", lambda: attr(_good(B, noval_gain=1.5)), (PASS, "other_repairs_carry"))
    add("attr NOVAL missing on a seed -> CD (verdict unchanged)", "attr",
        lambda: attr(_good(B, noval_gain=0.0)[:-1] + _good(B)[-1:]), (PASS, CD))
    add("attr ABSENT mode -> not run", "attr", lambda: attr(_good(B)), (PASS, "not_run (ABSENT mode)"))
    add("queue: every gate green, mode fixed", "queue", lambda: a1_queueable(_all_gates(), "GROUNDED")["verdict"], "QUEUEABLE")
    def _q_no_e(mode):
        g = _all_gates()
        g["CODEC"]["W1_e_consumer_mediated"] = False
        g["ACT"] = dict(g["ACT"], GASP_e_consumer_mediated=False)
        r = a1_queueable(g, mode)
        return (r["verdict"], r["reported"]["CODEC:W1_e_consumer_mediated"], r["reported"]["ACT:GASP_e_consumer_mediated"])
    add("queue v2b: (e) consumer legs FAIL pre-W5 -> still QUEUEABLE, reported", "queue",
        lambda: _q_no_e("ABSENT"), ("QUEUEABLE", False, False))
    add("queue v2b: CODEC containment fails -> HOLD", "queue",
        lambda: a1_queueable(_all_gates(CODEC__W1_e_containment_vs_shuffled=False), "ABSENT")["verdict"], "HOLD")
    add("queue v2b: ACT (f) fails -> HOLD", "queue",
        lambda: a1_queueable(_all_gates(ACT__GASP_f_not_state_invariant=False), "GROUNDED")["verdict"], "HOLD")
    def _oracle():
        st = [{"q": {0: 0.1, 1: 0.5, 2: -0.2, 3: 0.0, 4: 0.0},
               "pools": {"INT-CODEC": [0, 1], "INT-ACT": [0, 1, 2, 3, 4], "NATIVE-POOL": [2]}},
              {"q": {0: 0.3, 1: 0.1, 2: 0.0, 3: 0.3, 4: -0.1},
               "pools": {"INT-CODEC": [1, 2], "INT-ACT": [0, 1, 2, 3, 4], "NATIVE-POOL": [3]}}]
        o = oracle_diagnostic(st)
        return (o["report_only"], o["INT-ACT"]["oracle_pick_in_qbest"], o["INT-CODEC"]["oracle_pick_in_qbest"],
                o["NATIVE-POOL"]["oracle_pick_in_qbest"])
    add("oracle diagnostic (report-only) values", "oracle", _oracle, (True, 1.0, 0.5, 0.5))
    add("queue: valuation_mode not fixed -> HOLD", "queue", lambda: a1_queueable(_all_gates(), None)["verdict"], "HOLD")
    # v3 O12: stratum rule
    add("O12 env-only classifier on the measured pilot -> DEGENERATE -> fallback rule", "stratum",
        lambda: choose_stratum_rule(env_only_classifier_validity(PILOT_ENV_ONLY_EARLY600))["rule"], STRATUM_FALLBACK)
    def _discriminative():
        cnt = {s: ([30, 29, 31, 30, 28] if s % 3 == 0 else [3, 4, 2, 3, 5]) for s in range(30)}
        return choose_stratum_rule(env_only_classifier_validity(cnt))["rule"]
    add("O12b decided: pair rule even when env-only would be VALID", "stratum", _discriminative, STRATUM_FALLBACK)
    # v3 O12: shared init
    def _share():
        nat = {"enc.w": _T((4, 3), "N"), "e3.w": _T((5,), "N"), "e2.in": _T((8, 3), "N")}
        itn = {"enc.w": _T((4, 3), "I"), "e3.w": _T((5,), "I"), "e2.in": _T((8, 5), "I"), "trainer.w": _T((2,), "I")}
        merged, rep = share_init(nat, itn)
        return (merged["enc.w"].val, merged["e3.w"].val, merged["e2.in"].val, merged["trainer.w"].val,
                len(rep["copied"]), rep["shape_mismatch"], rep["int_only"])
    add("O12 share_init: shared same-shape keys from NATIVE; mismatch + INT-only kept", "share",
        _share, ("N", "N", "I", "I", 2, ["e2.in"], ["trainer.w"]))
    # v3 addendum: init-dominance readout is report-only -- perturbing every field it reads cannot move any verdict
    def _initdom():
        def dress(seeds, collapse):
            for s in seeds:
                for a, r in s["arms"].items():
                    k = 0 if collapse or a.startswith("NATIVE") else (s["seed"] + len(a)) % 5
                    r["action_counts"] = {k: 900, (k + 1) % 5: 100} if collapse else {c: 200 + 10 * ((c + k) % 3) for c in range(5)}
                    r["own_stratum"] = (TRAPPED if (collapse and a.endswith("R1")) else s["stratum"])
            return seeds
        verdicts, reads = [], []
        for strata in ({B: _good(B), T: _good(T)}, {B: _seeds(B, 0.1, shuf_gain=-1.0), T: _good(T)},
                       {B: _good(B), T: _seeds(T, 0.0, shuf_gain=-40.0, jit=8.0)}):
            pair = []
            for collapse in (False, True):
                st = {g: dress([dict(x, arms={a: dict(r) for a, r in x["arms"].items()}) for x in seeds], collapse)
                      for g, seeds in strata.items()}
                r = score_variant("CODEC", st)
                pair.append(r["verdict"])
                reads.append(r.get("init_dominance", {}).get(BENIGN, {}).get("INT", {}).get("modal_share_mean"))
            verdicts.append(pair[0] == pair[1])
        return (all(verdicts), len(set(round(x, 3) for x in reads if x is not None)) > 1)
    add("init-dominance readout cannot flip any verdict (report-only), yet it moves", "initdom", _initdom, (True, True))
    # v3b O15: babble attribution (secondary, own rule)
    def _bab(triple, strata_fn=None):
        st = {B: _good(B, babble=triple), T: _good(T, babble=triple)} if strata_fn is None else strata_fn(triple)
        r = score_variant("CODEC", st)
        return (r["verdict"], r["babble_attribution"]["label"])
    add("O15 babble: behaviour babbling carries (T 0.5, D 0.85, O 0.85)", "babble",
        lambda: _bab((0.5, 0.85, 0.85)), (PASS, "behaviour_babbling_carries"))
    add("O15 babble: data carries (T 0.52, D 0.5, O 0.85)", "babble",
        lambda: _bab((0.52, 0.5, 0.85)), (PASS, "babbling_data_carries"))
    add("O15 babble: nothing detected (all 0.85)", "babble", lambda: _bab((0.85, 0.85, 0.85)), (PASS, "neither_detected"))
    def _bab_noflip():
        out = []
        for base_strata in (lambda tr: {B: _good(B, babble=tr), T: _good(T, babble=tr)},
                            lambda tr: {B: _seeds(B, 0.1, shuf_gain=-1.0, babble=tr), T: _good(T, babble=tr)}):
            vs = {score_variant("CODEC", base_strata(tr))["verdict"] for tr in ((0.5, 0.85, 0.85), (0.85, 0.85, 0.85),
                                                                                 (0.52, 0.5, 0.85))}
            out.append(len(vs) == 1)
        return all(out)
    add("O15 babble-attribution arms cannot flip A1's verdict (secondary, own rule)", "babble", _bab_noflip, True)
    add("O15 babble arms missing -> contrast CD, verdict unchanged", "babble",
        lambda: (score_variant("CODEC", {B: _good(B), T: _good(T)})["verdict"],
                 score_variant("CODEC", {B: _good(B), T: _good(T)})["babble_attribution"]["label"]), (PASS, CD))
    add("cost estimate: 24 admitted seeds, 16 arms ABSENT (v3b: +4 babble arms)", "cost",
        lambda: (cost_estimate("ABSENT")["admitted_seeds"], cost_estimate("ABSENT")["arms_native_family"] +
                 cost_estimate("ABSENT")["arms_int"]), (24, 16))
    return C


def _run_cases(verbose: bool = True) -> Dict[str, bool]:
    res = {}
    for name, kind, th, want in _cases():
        got = th()
        res[name] = got == want
        if verbose:
            print("%s %-72s -> %s" % ("ok " if got == want else "BAD", name[:72], got))
    return res


# Each mutation restores ONE retired rule; the named case must then stop matching its expectation.
MUTATIONS = [
    ("O11: per-seed counting restored (v2)", "O11 per-seed counting fails, paired mean passes (gain 0.7 +- 0.3, reseed noise 0.85)",
     lambda g: g.__setitem__("SCORING", "per_seed_count")),
    ("change floor back to 1.44 (v2)", "v3 P4 learning gain 0.3 holds at floor 0.43",
     lambda g: g["FLOORS"][BENIGN].__setitem__("reward_change", 1.44)),
    ("P1g back to >= (pre-RT-1)", "RT-1 P1g tie 0=0 (shaping-only gain) fails",
     lambda g: g.__setitem__("P1G_STRICT", False)),
    ("underpowered-NI CD guard off (pre-RT-2)", "RT-2 re-expressed: noisy non-inferiority -> CD ni_underpowered",
     lambda g: g.__setitem__("NI_UNDERPOWERED_CD", False)),
    ("old gating: (e) consumer legs gate A1 (pre-v2b)", "queue v2b: (e) consumer legs FAIL pre-W5 -> still QUEUEABLE, reported",
     lambda g: (g["REQUIRED_GATES"].__setitem__("CODEC", g["REQUIRED_GATES"]["CODEC"] + ("W1_e_consumer_mediated",)),
                g["REQUIRED_GATES"].__setitem__("ACT", g["REQUIRED_GATES"]["ACT"] + ("GASP_e_consumer_mediated",)))),
    ("tie winner back to the v1 name 'ASP'", "h2h both PASS within bound -> tie rule (ACT)",
     lambda g: g.__setitem__("SIMPLER_VARIANT", "ASP")),
    ("O12: env-only validity gate off (and O12b undecided)", "O12 env-only classifier on the measured pilot -> DEGENERATE -> fallback rule",
     lambda g: (g.__setitem__("STRATUM_DECIDED", None), g.__setitem__("ENV_ONLY_MIN_ICC", -1.0),
                g.__setitem__("ENV_ONLY_MIN_CLASS_FRAC", 0.0))),
    ("O12b undecided (v3: validity-gated env-only rule)", "O12b decided: pair rule even when env-only would be VALID",
     lambda g: g.__setitem__("STRATUM_DECIDED", None)),
    ("O15: babble contrast leaks into the A1 verdict", "O15 babble-attribution arms cannot flip A1's verdict (secondary, own rule)",
     lambda g: g.__setitem__("BABBLE_CONTRAST_GATES", True)),
    ("O12: shared init off (v2: same seed, nothing copied)", "O12 share_init: shared same-shape keys from NATIVE; mismatch + INT-only kept",
     lambda g: g.__setitem__("SHARED_INIT", False)),
]
_MUTABLE = ("FLOORS", "P1G_STRICT", "NI_UNDERPOWERED_CD", "REQUIRED_GATES", "SIMPLER_VARIANT", "SCORING",
            "ENV_ONLY_MIN_ICC", "ENV_ONLY_MIN_CLASS_FRAC", "SHARED_INIT", "STRATUM_DECIDED", "BABBLE_CONTRAST_GATES")


def mutation_check() -> bool:
    import copy
    g = globals()
    ok = True
    for label, case_name, mutate in MUTATIONS:
        saved = {k: copy.deepcopy(g[k]) for k in _MUTABLE}
        try:
            mutate(g)
            res = _run_cases(verbose=False)
        finally:
            g.update(saved)
        caught = not res[case_name]
        ok &= caught
        print("%s mutation %-52s -> %s" % ("ok " if caught else "BAD", label,
                                           "case FLIPS (caught)" if caught else "case still passes (NOT caught)"))
    return ok


def selftest() -> int:
    res = _run_cases(verbose=True)
    ok = all(res.values())
    print("cases: %d/%d as expected" % (sum(res.values()), len(res)))
    mok = mutation_check()
    ok2 = all(_run_cases(verbose=False).values())   # the mutations must not leak
    print("SELFTEST %s" % ("PASS" if (ok and mok and ok2) else "FAIL"))
    return 0 if (ok and mok and ok2) else 1


def describe() -> None:
    for mode in VALUATION_MODES:
        print("valuation_mode=%s (%d arms per seed)" % (mode, len(arm_table(mode))))
        for a in arm_table(mode):
            print("  %-18s trainer=%-20s shuffle=%-5s seed_offset=%-6d %s"
                  % (a["name"], a["trainer"], a["shuffle"], a["agent_seed_offset"], a["role"]))
    print("seeds: %s admitted per stratum (+%d reserves each); scoring=%s (SE_MULT %.1f)"
          % (json.dumps(N_PER_STRATUM), RESERVE_PER_STRATUM, SCORING, SE_MULT))
    print("stratum rule: %s (DECIDED, O12b user 2026-09-25); env-only %s kept report-only" % (STRATUM_DECIDED, STRATUM_RULE))
    print("pilot validity: %s" % json.dumps(env_only_classifier_validity(PILOT_ENV_ONLY_EARLY600)))
    print("per-seed order: pin(R6) -> [stratum sidecar] -> NATIVE -> NATIVE-R1..R3 -> INT-* arms (each built with"
          " share_init from a NATIVE built at its own agent seed; require_stratum_sidecar first)")
    print("floors: %s" % json.dumps(FLOORS))
    print("parity: CEM_SCORE_WINDOW=%s, W3_BUFFER_ACTION_FORMAT=%s (both variants)" % (CEM_SCORE_WINDOW,
                                                                                    W3_BUFFER_ACTION_FORMAT))
    for v in VARIANTS:
        print("SHUF targets %-5s: %s" % (v, ", ".join(SHUF_TARGETS[v])))
    print("pre-A1 gates: %s" % json.dumps(REQUIRED_GATES))
    print("reported until W5: %s" % json.dumps(REPORTED_UNTIL_W5))
    print("init-dominance readout (report-only, never gating): NATIVE vs NATIVE-R1..R3 and INT-v vs INT-v-R1 --"
          " modal share, action entropy, reseed spread (reward, contacts, action TV), own-label concordance")
    for mode in VALUATION_MODES:
        print("cost %s: %s" % (mode, json.dumps(cost_estimate(mode, int_arm_s_t2_trapped=1080.0), default=str)))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--describe", action="store_true")
    a = ap.parse_args()
    if a.describe:
        describe()
    if a.selftest:
        sys.exit(selftest())
    if not (a.describe or a.selftest):
        print("skeleton only: use --describe or --selftest")
