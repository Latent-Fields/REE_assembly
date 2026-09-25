"""A1 integrated closed-loop acceptance -- SCRIPT SKELETON (DRAFT; NOT QUEUED; NOT an experiment).

Pre-registration: REE_assembly/evidence/planning/coupled_a1_preregistration_draft_20260925.md
Plan of record:   REE_assembly/evidence/planning/coupled_loop_repair_campaign_plan.md (sec 5, 6, 9)
Author: bt0925-a1prereg, chip_ref chip-20260925-coupled-a1-preregistration-draft, 2026-09-25.
v2:     bt0925-a1v2, chip_ref chip-20260925-coupled-a1-prereg-v2, 2026-09-25. Folds in the user decisions
        (rec-20260925-5fc6c256 floors + P1g, -aa066e96 change floor 1.44, -38b81685 hold for both
        variants, -c2519d92 NOVAL arms, -b9652a9b consumer-mediated gate leg on both variants) and the
        action-space design's A1 edits E1-E9 (action_space_proposals_design_20260925.md sec 5.2):
        INT-ASP -> INT-ACT, one CEM scoring window + one W3 buffer action format for both variants,
        the pre-A1 member-gate hold (a1_queueable), NOVAL attribution, and a mutation self-check.

WHAT THIS FILE IS
  * The ARM WIRING and the ORDER OF OPERATIONS of the A1 run, with every call site of the I1
    instruments (ree-v3 experiments/_lib/coupled_acceptance.py) marked "I1-n".
  * The SCORING half (margins, criteria P1b/P1t/P1g/P2/P3/P4, the verdict ladder, the head-to-head
    rule) implemented in full as PURE functions, because those are what the pre-registration fixes.
    `--selftest` runs them on synthetic seeds and shows every criterion can FAIL and every
    CANNOT_DETERMINE / INVALID branch is reachable.
  * `--describe` prints the arm table and the per-seed order of operations.
  * `--selftest` ALSO runs a mutation check: it restores each pre-v2 / pre-red-team rule one at a time
    (0.92 change floor, `>= 0` P1g, no balloon guard, no consumer-mediated leg in the CODEC gate,
    old "ASP" tie winner) and requires the case written for that rule to flip.

WHAT THIS FILE IS NOT
  * Runnable against an agent. The agent-facing functions raise NotImplementedError until W6
    (the integrated preset) and I1 exist on their respective refs. /queue-experiment turns this
    into ree-v3/experiments/<name>.py; it must not be copied into experiments/ from here.
  * The I1 API names below are those in bt0925-i1's UNCOMMITTED draft at 2026-09-25T12:35Z
    (wt-i1, based on cc20be5). They are a guide, not a contract: re-read coupled_acceptance.py
    on origin/main when porting.

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
STRATUM_WINDOW = 600                                                # NATIVE closed-loop steps 0..599
N_PER_STRATUM = 5                                                   # accepted rec-20260925-7e7e9825
RESERVE_PER_STRATUM = 2
SCREEN_CEILING = 80
SEED_START = 301
AGENT_SEED_OFFSET = 10_000                                          # NATIVE-Rk agent seed = env seed + k*offset
N_RESEED = 3
MIN_RESEED_PER_SEED = 2
MIN_DELTAS_PER_STRATUM = 8
FRAC_REQUIRED = 4                                                   # ">= 4/5"
MIN_INT_DELTAS_PER_STRATUM = 4                                      # INT-v vs INT-v-R1, one reseed per seed
BALLOON_FACTOR = 3.0                                                # RT-2: sampled 2xRMS > 3x floor -> non-inferiority CD

# Absolute floors (per 100 steps). Derivation + record in prereg sec 6 (floor_grounding.py).
# Superiority floors (reward, reward_change) use the conservative (larger) estimate; the benign reward
# floor is from the harm-bearing seeds 64-65 only (red-team RT-3). The non-inferiority floor (contacts)
# keeps the pooled estimate, which is the conservative (smaller) direction for a non-inferiority test.
# v2: accepted by the user (rec-20260925-5fc6c256); reward_change 1.44 = 2 x 0.643 x sqrt(1.25), the
# harm-bearing-seed value (rec-20260925-aa066e96), replacing the pooled 0.92.
FLOORS = {
    "benign": {"reward": 0.90, "contacts": 1.6, "reward_change": 1.44},
    "hazard_trapped": {"reward": 2.4, "contacts": 4.8, "reward_change": None},  # P4 is benign-only
}

VARIANTS = ("CODEC", "ACT")          # user decision rec-20260925-6a675285: both, head-to-head.
                                     # E1: "INT-ASP" is renamed "INT-ACT"; ASP stays the mechanism's name.
SIMPLER_VARIANT = "ACT"              # E9 / DRAFT tie rule (prereg 8.3): the user may override at A1 time.
P1G_STRICT = True                    # RT-1, accepted (rec-20260925-5fc6c256): a 0 = 0 tie does NOT hold.

# E3/E6/E7 (action_space_proposals_design sec 5.2): variant configs and the two parity constants.
# CEM_SCORE_WINDOW: ONE CEM elite scoring window for BOTH variants (E6). "full" = today's behaviour;
#   the value is fixed when W4 lands (user decision U4 still open; if W4 selects a discount rather than a
#   depth, both CEM scorers use that same aggregation). Never set per variant.
# W3_BUFFER_ACTION_FORMAT: the W3 member stores the executed vector AS FED TO E2 in both variants (E7).
#   For INT-ACT that vector is an exact one-hot; for INT-CODEC it is the bounded continuous decode.
CEM_SCORE_WINDOW = "full"            # DRAFT until W4 (U4)
W3_BUFFER_ACTION_FORMAT = "executed_as_fed_to_e2"
VARIANT_CONFIG = {
    "CODEC": dict(members=("codec", "terrain_prior"), use_action_space_proposals=False,
                  cem_score_window=CEM_SCORE_WINDOW, w3_buffer_action_format=W3_BUFFER_ACTION_FORMAT),
    "ACT": dict(members=(), use_action_space_proposals=True, action_space_first_action_mode="stratified",
                action_space_cem_score_horizon=CEM_SCORE_WINDOW, use_action_class_scaffold_candidates=False,
                w3_buffer_action_format=W3_BUFFER_ACTION_FORMAT),   # codec + prior NOT registered (E3)
}
# E4: what each variant's SHUF permutes. INT-ACT-SHUF destroys strictly less (no codec labels, no prior
# target exist in INT-ACT). P3 compares each variant with its OWN SHUF, so each test stays fair.
SHUF_TARGETS = {
    "CODEC": ("harm_eval", "benefit_eval", "valuation_stream[GROUNDED]", "terrain_prior_target",
              "codec_decode_labels", "e2_world_action_labels(+babbling)"),
    "ACT": ("harm_eval", "benefit_eval", "valuation_stream[GROUNDED]", "e2_world_action_labels(+babbling)"),
}

# Pre-A1 member gates (user decisions rec-20260925-38b81685 hold-for-both, -b9652a9b consumer leg on
# both; orchestrator decision log 2026-09-25T14:19Z for W4). A1 is QUEUEABLE only when every one is True.
# W4 (b) is NOT here: it moved after W5 (N3-pre: E3's valuation caps pick-in-Q-best at chance).
# v2b (user decision rec-20260925-a16786f5): the consumer-mediated (e) legs of BOTH variants moved after
# W5 too, for the same reason. Before W5 the hold clears on (a)-(d) + containment + (f); the (e) legs and
# W4 (b) are REPORTED (REPORTED_UNTIL_W5), never gating. A1 stays runnable in GROUNDED and ABSENT modes.
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

BENIGN, TRAPPED = "benign", "hazard_trapped"
PASS, FAIL, CD, INVALID = "PASS", "FAIL", "CANNOT_DETERMINE", "INVALID"


def arm_table(valuation_mode: str) -> List[Dict[str, Any]]:
    """Every arm, what it is, and whether it is scored. Order = execution order within a seed.
    v2: the NOVAL arms are REQUIRED in GROUNDED mode (user decision rec-20260925-c2519d92). In ABSENT mode
    INT-v already has no valuation, so INT-v-NOVAL would be the same arm; it is not run."""
    arms = [dict(name="NATIVE", agent_seed_offset=0, preset=None, trainer=False, shuffle=False,
                 role="stratum source (sidecar) + comparator")]
    for k in range(1, N_RESEED + 1):
        arms.append(dict(name="NATIVE-R%d" % k, agent_seed_offset=k * AGENT_SEED_OFFSET, preset=None,
                         trainer=False, shuffle=False, role="margin calibration ONLY"))
    for v in VARIANTS:
        base = dict(preset="W6:%s:%s" % (v, valuation_mode), agent_seed_offset=0, config=VARIANT_CONFIG[v])
        arms.append(dict(name="INT-%s" % v, trainer=True, shuffle=False, role="tested", **base))
        arms.append(dict(name="INT-%s-SHUF" % v, trainer=True, shuffle=True, role="grounding control (P3)", **base))
        arms.append(dict(name="INT-%s-FROZEN" % v, trainer="off_in_closed_loop", shuffle=False,
                         role="learning control (P4)", **base))
        arms.append(dict(name="INT-%s-R1" % v, trainer=True, shuffle=False, preset=base["preset"],
                         config=VARIANT_CONFIG[v], agent_seed_offset=AGENT_SEED_OFFSET,
                         role="INT margin calibration ONLY (RT-2)"))
        if valuation_mode == "GROUNDED":
            arms.append(dict(name="INT-%s-NOVAL" % v, trainer=True, shuffle=False,
                             preset="W6:%s:ABSENT" % v, config=VARIANT_CONFIG[v], agent_seed_offset=0,
                             role="attribution ONLY (valuation vs other repairs; no verdict effect)"))
    return arms


# ----------------------------------------------------------------------------- run side (skeleton)
def pin_substrate(pinned_sha: str) -> Dict[str, Any]:
    """MUST run before the first `import ree_core` (substrate_pin.py docstring).
    The sha is the 40-hex branch head recorded in the pre-registration/queue entry -- never a branch
    NAME (the head moves). Marker: a symbol present on the branch and absent on main (the W6 preset
    builder; name fixed when W6 lands)."""
    from experiments._lib.substrate_pin import pin_ree_core, verify_pin, pin_manifest_block  # noqa: F401
    pin = pin_ree_core(pinned_sha)
    if len(pinned_sha) != 40 or pin.get("sha") != pinned_sha:   # R6 (see prereg sec 7)
        raise RuntimeError("R6: pinned sha mismatch")
    # verify_pin(pin, marker_module="ree_core.<W6 preset module>", marker_attr="<W6 preset builder>",
    #            marker_expected_present=True)
    raise NotImplementedError("W6 preset marker not yet defined (W6 not built)")


def build_env_agent(env_seed: int, agent_seed: int, preset: Optional[str]):
    """env seed and agent seed are SEPARATE (prereg sec 3). CausalGridWorldV2 draws only from its own
    self._rng = default_rng(seed) (causal_grid_world.py:1604 @ 23714f0562), so seeding the agent with
    agent_seed after constructing the env leaves env dynamics seeded by env_seed.
    Today's probe harnesses call seed_all(seed) once for both -- A1 must not."""
    raise NotImplementedError


def run_arm(env_seed: int, arm: Dict[str, Any], sidecar_path: str, arms_already_read: List[str]):
    """Per-arm protocol: [dev epoch DEV_EPOCH_STEPS] -> [encoder warmup, identical protocol] ->
    [CLOSED_LOOP_STEPS closed-loop steps, recording per step: env reward, transition_type (I1-6
    step_outcome), done flag, action class]."""
    # Order guard -- I1-5: a non-NATIVE arm may not even START before the NATIVE sidecar exists.
    # if arm["name"] != "NATIVE":
    #     stratum = coupled_acceptance.require_stratum_sidecar(sidecar_path, env_seed)
    # NATIVE only, immediately after its closed-loop step 599 and BEFORE step 600:
    #     res = coupled_acceptance.classify_stratum(dones[:STRATUM_WINDOW], window=600, early_len=200,
    #                                               min_early=10, max_episode_steps=200)
    #     coupled_acceptance.write_stratum_sidecar(sidecar_path, seed=env_seed, result=res,
    #                                              arm="NATIVE", arms_already_read=arms_already_read)
    # Per window (FIRST, LAST) -- I1-6:
    #     coupled_acceptance.outcome_decomposition(tts[lo:hi], rewards[lo:hi])  -> CD on unknown type
    # INT-* arms, end of run (preconditions, prereg sec 7):
    #     R0  trainer.guard_verdicts()                                  (C0 guard; every group PASS)
    #     R1  CODEC: I1-4 cem_codec_trace / codec_ranges / codec_roundtrip_accuracy = W1 (b)-(d)
    #         ACT:   G-ASP (b)-(d) from the propose diagnostics (one-hots, decoder calls 0, bounded
    #                rollouts, stratified coverage) (E5). Gate (e) of BOTH is pre-A1 (a1_queueable).
    #     R2  I1-1 action_discrimination(e2_world_predictor(agent.e2), held-out uniform set)
    #         real head meets W3(a); SHUF head does NOT
    #     R3  I1-2 collect_probe_states + I1-3 head_swap_flip_rate (W4(c), RE-REFERENCED 14:19Z:
    #         real-head flip rate vs a TRAINED action-blind head, minus shuffled-head flip rate)
    #     R4  1105a primary detector D_N silent on INT (GROUNDED mode only)
    #     R5  per-group held-out loss at LAST < FROZEN's
    # Reported (no criterion): E3-picked class modal share over probe states, both variants (E8);
    #     proposal_m4 CODEC only (degenerate for the stratified ACT pool, E8); pool_qbest_coverage;
    #     W4(b)-style pick-in-Q-best, both variants (moved after W5; reported); action entropy; ARC-016
    #     running_variance + commit rate; early terminations; per-group losses.
    raise NotImplementedError


# ----------------------------------------------------------------------------- scoring side (full)
def _rms(xs: Sequence[float]) -> float:
    return math.sqrt(sum(x * x for x in xs) / len(xs))


def window_stats(rec: Dict[str, Any]) -> Dict[str, float]:
    """rec per arm: {"reward_LAST", "reward_FIRST", "contacts_LAST", "grounded_LAST"} (per 100)."""
    out = dict(rec)
    out["reward_change"] = rec["reward_LAST"] - rec["reward_FIRST"]
    return out


def margins(seeds: List[Dict[str, Any]], stratum: str) -> Dict[str, Any]:
    """margin_m = max(2 x RMS over the stratum of per-seed (NATIVE - NATIVE-Rk) deltas, floor_m).
    CD if any seed has < MIN_RESEED_PER_SEED reseeds or the stratum has < MIN_DELTAS_PER_STRATUM deltas."""
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
    """RT-2: INT-vs-INT noise from INT-v vs INT-v-R1 (agent reseed of the tested preset).
    Superiority criteria use max(NATIVE margin, 2 x RMS of these deltas)."""
    out: Dict[str, Any] = {}
    for m, key in (("reward", "reward_LAST"), ("reward_change", "reward_change")):
        ds = [window_stats(s["arms"]["INT-%s" % v])[key] - window_stats(s["arms"]["INT-%s-R1" % v])[key]
              for s in seeds if "INT-%s-R1" % v in s["arms"]]
        if len(ds) < MIN_INT_DELTAS_PER_STRATUM:
            out[m] = {"verdict": CD, "reason": "%d INT reseed deltas" % len(ds)}
        else:
            out[m] = {"verdict": "MEASURED", "two_x": 2 * _rms(ds), "n_deltas": len(ds)}
    return out


def _count(seeds, pred) -> int:
    return sum(1 for s in seeds if pred(s))


def score_variant(v: str, strata: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
    """Verdict ladder (prereg sec 8), evaluated in this order:
      1. INVALID  if any admitted seed has a failed precondition R0-R7 for this variant.
      2. CANNOT_DETERMINE if a stratum has < N_PER_STRATUM admitted seeds, or a needed margin is CD.
      3. PASS iff P1b, P1g, P1t, P2 (both strata), P3 (both strata), P4 all hold; else FAIL."""
    T, S, F = "INT-%s" % v, "INT-%s-SHUF" % v, "INT-%s-FROZEN" % v
    res: Dict[str, Any] = {"variant": v, "criteria": {}}
    bad = [(s["seed"], s["preconditions"][v]) for g in strata.values() for s in g
           if not all(s["preconditions"][v].values())]
    if bad:
        res.update(verdict=INVALID, reason="precondition failed: %s" % bad)
        return res
    for g in (BENIGN, TRAPPED):
        if len(strata.get(g, [])) < N_PER_STRATUM:
            res.update(verdict=CD, reason="stratum %s under-admitted (%d)" % (g, len(strata.get(g, []))))
            return res
    M = {g: margins(strata[g], g) for g in (BENIGN, TRAPPED)}
    need = [(BENIGN, "reward"), (BENIGN, "contacts"), (BENIGN, "reward_change"), (TRAPPED, "reward"), (TRAPPED, "contacts")]
    IM = {g: int_margins(strata[g], g, v) for g in (BENIGN, TRAPPED)}
    cdm = [(g, m) for g, m in need if M[g][m]["verdict"] == CD]
    cdm += [("INT:" + g, m) for g, m in ((BENIGN, "reward"), (BENIGN, "reward_change"), (TRAPPED, "reward"))
            if IM[g][m]["verdict"] == CD]
    if cdm:
        res.update(verdict=CD, reason="margin not computable: %s" % cdm, margins=M)
        return res
    # RT-2: a non-inferiority margin that balloons makes P1t / P2 near-unfalsifiable -> CD, never PASS.
    bal = [(g, m) for g, m in ((TRAPPED, "reward"), (BENIGN, "contacts"), (TRAPPED, "contacts")) if M[g][m]["ballooned"]]
    if bal:
        res.update(verdict=CD, reason="margin_ballooned (non-inferiority unfalsifiable): %s" % bal, margins=M)
        return res
    W = lambda s, a: window_stats(s["arms"][a])  # noqa: E731
    b, t = strata[BENIGN], strata[TRAPPED]
    mb, mt = M[BENIGN], M[TRAPPED]
    # superiority margins: the larger of NATIVE-reseed and INT-reseed noise (RT-2)
    sup_b = max(mb["reward"]["margin"], IM[BENIGN]["reward"]["two_x"])
    sup_t = max(mt["reward"]["margin"], IM[TRAPPED]["reward"]["two_x"])
    sup_chg = max(mb["reward_change"]["margin"], IM[BENIGN]["reward_change"]["two_x"])
    c = res["criteria"]
    c["P1b"] = _count(b, lambda s: W(s, T)["reward_LAST"] - W(s, "NATIVE")["reward_LAST"] > sup_b)
    # RT-1: STRICT. A 0 = 0 tie (no contacts or consumptions in either arm) does NOT hold: a gain carried
    # only by approach/proximity shaping must not pass.
    if P1G_STRICT:
        c["P1g"] = _count(b, lambda s: W(s, T)["grounded_LAST"] - W(s, "NATIVE")["grounded_LAST"] > 0.0)
    else:  # pre-red-team rule; kept ONLY so the mutation check can show the RT-1 case depends on it
        c["P1g"] = _count(b, lambda s: W(s, T)["grounded_LAST"] - W(s, "NATIVE")["grounded_LAST"] >= 0.0)
    c["P1t"] = _count(t, lambda s: W(s, "NATIVE")["reward_LAST"] - W(s, T)["reward_LAST"] <= mt["reward"]["margin"])
    c["P2b"] = _count(b, lambda s: W(s, T)["contacts_LAST"] - W(s, "NATIVE")["contacts_LAST"] <= mb["contacts"]["margin"])
    c["P2t"] = _count(t, lambda s: W(s, T)["contacts_LAST"] - W(s, "NATIVE")["contacts_LAST"] <= mt["contacts"]["margin"])
    c["P3b"] = _count(b, lambda s: W(s, T)["reward_LAST"] - W(s, S)["reward_LAST"] > sup_b)
    c["P3t"] = _count(t, lambda s: W(s, T)["reward_LAST"] - W(s, S)["reward_LAST"] > sup_t)
    c["P4"] = _count(b, lambda s: W(s, T)["reward_change"] - W(s, F)["reward_change"] > sup_chg)
    held = {k: n >= FRAC_REQUIRED for k, n in c.items()}
    res["held"] = held
    res["margins"] = M
    res["superiority_margins"] = {"benign_reward": sup_b, "trapped_reward": sup_t, "benign_change": sup_chg}
    res["gain_P1b_mean"] = sum(W(s, T)["reward_LAST"] - W(s, "NATIVE")["reward_LAST"] for s in b) / len(b)
    res["verdict"] = PASS if all(held.values()) else FAIL
    res["attribution"] = attribution(v, b, sup_b)
    if res["verdict"] == FAIL:
        # named FAIL signatures (prereg sec 8), reported, not re-scored
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
        # v2 (prereg 6.4 / 8.1): P4 is the only missing criterion and INT's FIRST window sits near NATIVE's
        # -> the 1.44 change floor may be out of reach by construction; reported, never re-scored.
        others = [k for k in held if k != "P4"]
        near = _count(b, lambda s: abs(W(s, T)["reward_FIRST"] - W(s, "NATIVE")["reward_FIRST"]) <= mb["reward"]["margin"])
        if (not held["P4"]) and all(held[k] for k in others) and near >= FRAC_REQUIRED:
            sig.append("P4 headroom-limited (6.4)")
        res["fail_signatures"] = sig
    return res


def head_to_head(results: Dict[str, Dict[str, Any]], margin_benign_reward: Optional[float]) -> Dict[str, Any]:
    """A1 verdict over the two proposal variants (prereg sec 8.3)."""
    passed = [v for v, r in results.items() if r["verdict"] == PASS]
    if any(r["verdict"] == INVALID for r in results.values()):
        return {"verdict": INVALID, "winner": None, "note": "a variant is INVALID; fix and re-run (lettered id)"}
    if not passed:
        cds = [v for v, r in results.items() if r["verdict"] == CD]
        return {"verdict": CD if len(cds) == len(results) else FAIL, "winner": None}
    if len(passed) == 1:
        return {"verdict": PASS, "winner": passed[0]}
    g = {v: results[v]["gain_P1b_mean"] for v in passed}
    hi, lo = max(g, key=g.get), min(g, key=g.get)
    m = margin_benign_reward
    if m is None:
        m = max(results[v]["superiority_margins"]["benign_reward"] for v in passed)
    if g[hi] - g[lo] > m:
        return {"verdict": PASS, "winner": hi, "note": "both PASS; larger mean benign gain by > margin"}
    return {"verdict": PASS, "winner": SIMPLER_VARIANT,
            "note": "both PASS within margin; DRAFT tie rule: INT-ACT is simpler -- it removes the decoder and "
                    "terrain_prior from the act path (constructed but unused) and adds no trainable parameters. "
                    "Tie rule owner: the user, at A1 time"}


def attribution(v: str, benign: List[Dict[str, Any]], sup_b: float) -> Dict[str, Any]:
    """NOVAL attribution (user decision rec-20260925-c2519d92). REPORTED ONLY: it never changes a verdict.
    GROUNDED mode only (ABSENT mode has no NOVAL arm, since INT-v already has no valuation).
      valuation_carries  : INT-v - INT-v-NOVAL > sup_b on >= 4/5 benign AND NOVAL does not meet P1b alone
      other_repairs_carry: INT-v-NOVAL - NATIVE > sup_b on >= 4/5 benign (valuation not needed for the gain)
      both / undetermined otherwise. A NOVAL arm missing on some seed of a GROUNDED run -> CANNOT_DETERMINE."""
    TN = "INT-%s-NOVAL" % v
    have = [s for s in benign if TN in s["arms"]]
    if not have:
        return {"label": "not_run (ABSENT mode)"}
    if len(have) < len(benign):
        return {"label": CD, "reason": "NOVAL missing on %d seed(s)" % (len(benign) - len(have))}
    W = lambda s, a: window_stats(s["arms"][a])  # noqa: E731
    val = _count(have, lambda s: W(s, "INT-%s" % v)["reward_LAST"] - W(s, TN)["reward_LAST"] > sup_b)
    oth = _count(have, lambda s: W(s, TN)["reward_LAST"] - W(s, "NATIVE")["reward_LAST"] > sup_b)
    vc, oc = val >= FRAC_REQUIRED, oth >= FRAC_REQUIRED
    label = ("valuation_carries" if vc and not oc else "other_repairs_carry" if oc and not vc
             else "both" if vc and oc else "undetermined")
    return {"label": label, "n_valuation_gt_margin": val, "n_noval_beats_native": oth}


def a1_queueable(gates: Dict[str, Dict[str, bool]], valuation_mode: Optional[str]) -> Dict[str, Any]:
    """Pre-A1 hold (user decision rec-20260925-38b81685): A1 queues only when BOTH variants pass their
    member gates plus the shared gates, and only once valuation_mode is fixed. Any missing or False gate
    -> HOLD, naming it. v2b (rec-20260925-a16786f5): the consumer-mediated (e) legs and W4 (b) are in
    REPORTED_UNTIL_W5 -- their values are passed through as `reported`, and they never cause a HOLD."""
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
    """REPORT-ONLY oracle diagnostic (user decision rec-20260925-a16786f5). Each probe state carries env-Q per
    first-action class (`q`: {class: value}, the ADDENDUM 3 estimator) and each pool's first-action classes
    (`pools`: {pool_name: [class, ...]}). env-Q stands in for E3's valuation: the oracle picks the pool's
    best class. Per pool: the fraction of states where that pick is in the env-Q-best set (within 1e-9 of the
    max over ALL classes), and the mean regret max_all Q - max_pool Q. It answers "does the pool itself carry
    better options?", independently of E3's (pre-W5, chance-level) valuation. It feeds no criterion, no
    precondition and no hold. NOTE: a stratified INT-ACT pool contains every class, so its value is 1.0 / 0.0
    by construction -- reported as such; the informative comparison is INT-CODEC vs NATIVE-POOL."""
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


# ----------------------------------------------------------------------------- self-test (synthetic)
def _synthetic(stratum: str, seed: int, gain: float, *, shuf_gain: Optional[float] = None, frozen_learn: float = 0.0,
               contacts_up: float = 0.0, grounded_delta: float = 0.1, noise: float = 0.05, n_reseed: int = 3,
               pre_ok: bool = True, int_noise: float = 0.05, g_tie: bool = False,
               noval_gain: Optional[float] = None) -> Dict[str, Any]:
    base = -0.5 if stratum == BENIGN else -3.0
    def rec(r_last, r_first, c_last, g_last):
        return {"reward_LAST": r_last, "reward_FIRST": r_first, "contacts_LAST": c_last, "grounded_LAST": g_last}
    g0 = 0.0 if g_tie else -0.2
    arms = {"NATIVE": rec(base, base, 2.0, g0)}
    for k in range(1, n_reseed + 1):
        d = noise * (1 if (seed + k) % 2 else -1)
        arms["NATIVE-R%d" % k] = rec(base + d, base + d, 2.0 + d, -0.2)
    sg = gain / 2 if shuf_gain is None else shuf_gain
    for v in VARIANTS:
        arms["INT-%s" % v] = rec(base + gain, base, 2.0 + contacts_up, g0 if g_tie else -0.2 + grounded_delta)
        d = int_noise * (1 if seed % 2 else -1)
        arms["INT-%s-R1" % v] = rec(base + gain + d, base, 2.0 + contacts_up, -0.2 + grounded_delta)
        arms["INT-%s-SHUF" % v] = rec(base + sg, base, 2.0, -0.2)
        arms["INT-%s-FROZEN" % v] = rec(base + frozen_learn, base, 2.0, -0.2)
        if noval_gain is not None:
            arms["INT-%s-NOVAL" % v] = rec(base + noval_gain, base, 2.0, -0.2)
    return {"seed": seed, "stratum": stratum, "arms": arms,
            "preconditions": {v: {"R0": pre_ok, "R1": True, "R2": True, "R3": True, "R4": True, "R5": True,
                                  "R6": True, "R7": True} for v in VARIANTS}}


def _good(g: str, **kw) -> List[Dict[str, Any]]:
    # P3t needs INT > SHUF by margin on trapped too: give SHUF a large deficit there.
    return [_synthetic(g, s, 1.5 if g == BENIGN else 0.0, shuf_gain=0.0 if g == BENIGN else -3.0, **kw)
            for s in range(5)]


def _all_gates(**off) -> Dict[str, Dict[str, bool]]:
    g = {grp: {n: True for n in names} for grp, names in REQUIRED_GATES.items()}
    for key, val in off.items():
        grp, n = key.split("__", 1)
        g[grp][n] = val
    return g


def _cases() -> List[Any]:
    """(name, kind, thunk, want). kind: 'score' -> score_variant verdict; 'h2h' -> (verdict, winner);
    'attr' -> (verdict, attribution label); 'queue' -> a1_queueable verdict; 'sig' -> named FAIL signature present;
    'oracle' -> oracle_diagnostic values."""
    B, T = BENIGN, TRAPPED
    sv = lambda strata: score_variant("CODEC", strata)["verdict"]  # noqa: E731
    C = []
    add = lambda name, kind, th, want: C.append((name, kind, th, want))  # noqa: E731
    add("all criteria hold", "score", lambda: sv({B: _good(B), T: _good(T)}), PASS)
    add("P1b fails (no benign gain)", "score",
        lambda: sv({B: [_synthetic(B, s, 0.1, shuf_gain=-1.0) for s in range(5)], T: _good(T)}), FAIL)
    add("P1g fails (gain carried by shaping)", "score",
        lambda: sv({B: [_synthetic(B, s, 1.5, shuf_gain=0.0, grounded_delta=-0.3) for s in range(5)], T: _good(T)}), FAIL)
    add("P2 fails (undirected: contacts up)", "score",
        lambda: sv({B: [_synthetic(B, s, 1.5, shuf_gain=0.0, contacts_up=3.0) for s in range(5)], T: _good(T)}), FAIL)
    add("P3 fails (SHUF as good)", "score",
        lambda: sv({B: [_synthetic(B, s, 1.5, shuf_gain=1.5) for s in range(5)], T: _good(T)}), FAIL)
    add("P4 fails (FROZEN learns as much)", "score",
        lambda: sv({B: [_synthetic(B, s, 1.5, shuf_gain=0.0, frozen_learn=1.5) for s in range(5)], T: _good(T)}), FAIL)
    add("P1t fails (trapped much worse)", "score",
        lambda: sv({B: _good(B), T: [_synthetic(T, s, -5.0, shuf_gain=-9.0) for s in range(5)]}), FAIL)
    add("stratum under-admitted", "score", lambda: sv({B: _good(B), T: _good(T)[:4]}), CD)
    add("reseeds short -> margin CD", "score",
        lambda: sv({B: [_synthetic(B, s, 1.5, shuf_gain=0.0, n_reseed=1) for s in range(5)], T: _good(T)}), CD)
    add("precondition failed -> INVALID", "score",
        lambda: sv({B: [_synthetic(B, 0, 1.5, pre_ok=False)] + _good(B)[1:], T: _good(T)}), INVALID)
    add("zero reseed noise: floor binds (gain 0.6 < 0.90)", "score",
        lambda: sv({B: [_synthetic(B, s, 0.6, shuf_gain=-1.0, noise=0.0) for s in range(5)], T: _good(T)}), FAIL)
    add("RT-1 P1g tie 0=0 (shaping-only gain) fails", "score",
        lambda: sv({B: [_synthetic(B, s, 1.5, shuf_gain=0.0, g_tie=True) for s in range(5)], T: _good(T)}), FAIL)
    add("RT-2 non-inferiority margin balloons -> CD", "score",
        lambda: sv({B: _good(B), T: [_synthetic(T, s, 0.0, shuf_gain=-40.0, noise=8.0) for s in range(5)]}), CD)
    add("RT-2 INT reseed noise large -> P1b fails", "score",
        lambda: sv({B: [_synthetic(B, s, 1.5, shuf_gain=0.0, int_noise=2.0) for s in range(5)], T: _good(T)}), FAIL)
    # v2: the 1.44 change floor (rec-20260925-aa066e96). Learning gain over FROZEN = 1.2: above 0.92, below 1.44.
    add("v2 P4 change 1.2 < floor 1.44 fails", "score",
        lambda: sv({B: [_synthetic(B, s, 1.5, shuf_gain=0.0, frozen_learn=0.3) for s in range(5)], T: _good(T)}), FAIL)
    add("v2 P4-only FAIL, FIRST near NATIVE -> headroom signature", "sig",
        lambda: "P4 headroom-limited (6.4)" in score_variant("CODEC", {B: [_synthetic(B, s, 1.5, shuf_gain=0.0, frozen_learn=0.3)
                                                                          for s in range(5)], T: _good(T)}).get("fail_signatures", []), True)
    # v2: head-to-head (8.3) -- previously untested
    def h2h(rc, ra, gc=2.0, ga=1.2, m=0.9):
        r = {"CODEC": {"verdict": rc, "gain_P1b_mean": gc, "superiority_margins": {"benign_reward": m}},
             "ACT": {"verdict": ra, "gain_P1b_mean": ga, "superiority_margins": {"benign_reward": m}}}
        out = head_to_head(r, None)
        return (out["verdict"], out["winner"])
    add("h2h both PASS within margin -> tie rule (ACT)", "h2h", lambda: h2h(PASS, PASS), (PASS, "ACT"))
    add("h2h both PASS, CODEC ahead by > margin", "h2h", lambda: h2h(PASS, PASS, gc=2.5), (PASS, "CODEC"))
    add("h2h only CODEC PASS", "h2h", lambda: h2h(PASS, FAIL), (PASS, "CODEC"))
    add("h2h one INVALID -> A1 INVALID", "h2h", lambda: h2h(INVALID, PASS), (INVALID, None))
    add("h2h both CD -> CD", "h2h", lambda: h2h(CD, CD), (CD, None))
    add("h2h FAIL + CD -> FAIL", "h2h", lambda: h2h(FAIL, CD), (FAIL, None))
    # v2: NOVAL attribution (rec-20260925-c2519d92) -- reported only; the verdict must not move
    def attr(benign):
        r = score_variant("CODEC", {B: benign, T: _good(T)})
        return (r["verdict"], r["attribution"]["label"])
    add("attr NOVAL no gain -> valuation carries", "attr",
        lambda: attr(_good(B, noval_gain=0.0)), (PASS, "valuation_carries"))
    add("attr NOVAL full gain -> other repairs carry", "attr",
        lambda: attr(_good(B, noval_gain=1.5)), (PASS, "other_repairs_carry"))
    add("attr NOVAL missing on a seed -> CD (verdict unchanged)", "attr",
        lambda: attr(_good(B, noval_gain=0.0)[:4] + _good(B)[4:]), (PASS, CD))
    add("attr ABSENT mode -> not run", "attr", lambda: attr(_good(B)), (PASS, "not_run (ABSENT mode)"))
    # v2: pre-A1 hold (rec-20260925-38b81685, -b9652a9b)
    add("queue: every gate green, mode fixed", "queue", lambda: a1_queueable(_all_gates(), "GROUNDED")["verdict"], "QUEUEABLE")
    # v2b (rec-20260925-a16786f5): the consumer-mediated (e) legs no longer gate; they are reported.
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
    # v2b: oracle diagnostic (report-only) computes, and the variant verdict does not read it
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
    return C


def _run_cases(verbose: bool = True) -> Dict[str, bool]:
    res = {}
    for name, kind, th, want in _cases():
        got = th()
        res[name] = got == want
        if verbose:
            print("%s %-54s -> %s" % ("ok " if got == want else "BAD", name, got))
    return res


# Each mutation restores ONE retired rule; the named case must then stop matching its expectation.
MUTATIONS = [
    ("change floor back to pooled 0.92", "v2 P4 change 1.2 < floor 1.44 fails",
     lambda g: g["FLOORS"]["benign"].__setitem__("reward_change", 0.92)),
    ("P1g back to >= 0 (pre-RT-1)", "RT-1 P1g tie 0=0 (shaping-only gain) fails",
     lambda g: g.__setitem__("P1G_STRICT", False)),
    ("balloon guard off (pre-RT-2)", "RT-2 non-inferiority margin balloons -> CD",
     lambda g: g.__setitem__("BALLOON_FACTOR", float("inf"))),
    ("old gating: (e) consumer legs gate A1 (pre-v2b)", "queue v2b: (e) consumer legs FAIL pre-W5 -> still QUEUEABLE, reported",
     lambda g: (g["REQUIRED_GATES"].__setitem__("CODEC", g["REQUIRED_GATES"]["CODEC"] + ("W1_e_consumer_mediated",)),
                g["REQUIRED_GATES"].__setitem__("ACT", g["REQUIRED_GATES"]["ACT"] + ("GASP_e_consumer_mediated",)))),
    ("tie winner back to the v1 name 'ASP'", "h2h both PASS within margin -> tie rule (ACT)",
     lambda g: g.__setitem__("SIMPLER_VARIANT", "ASP")),
]


def mutation_check() -> bool:
    import copy
    g = globals()
    ok = True
    for label, case_name, mutate in MUTATIONS:
        saved = {k: copy.deepcopy(g[k]) for k in ("FLOORS", "P1G_STRICT", "BALLOON_FACTOR", "REQUIRED_GATES",
                                                  "SIMPLER_VARIANT")}
        try:
            mutate(g)
            res = _run_cases(verbose=False)
        finally:
            g.update(saved)
        caught = not res[case_name]
        ok &= caught
        print("%s mutation %-46s -> case '%s' %s" % ("ok " if caught else "BAD", label, case_name,
                                                      "FLIPS (caught)" if caught else "still passes (NOT caught)"))
    return ok


def selftest() -> int:
    res = _run_cases(verbose=True)
    ok = all(res.values())
    print("cases: %d/%d as expected" % (sum(res.values()), len(res)))
    mok = mutation_check()
    # the mutations must not leak: re-run clean
    ok2 = all(_run_cases(verbose=False).values())
    print("SELFTEST %s" % ("PASS" if (ok and mok and ok2) else "FAIL"))
    return 0 if (ok and mok and ok2) else 1


def describe() -> None:
    for mode in VALUATION_MODES:
        print("valuation_mode=%s (%d arms per seed)" % (mode, len(arm_table(mode))))
        for a in arm_table(mode):
            print("  %-18s trainer=%-20s shuffle=%-5s seed_offset=%-6d %s"
                  % (a["name"], a["trainer"], a["shuffle"], a["agent_seed_offset"], a["role"]))
    print("per-seed order: pin(R6) -> NATIVE to closed-loop step 599 -> classify + write sidecar (I1-5)"
          " -> NATIVE to 3000 -> NATIVE-R1..R3 -> INT-* arms (each calls require_stratum_sidecar first)")
    print("floors: %s" % json.dumps(FLOORS))
    print("parity: CEM_SCORE_WINDOW=%s (both variants), W3_BUFFER_ACTION_FORMAT=%s (both variants)"
          % (CEM_SCORE_WINDOW, W3_BUFFER_ACTION_FORMAT))
    for v in VARIANTS:
        print("SHUF targets %-5s: %s" % (v, ", ".join(SHUF_TARGETS[v])))
    print("pre-A1 gates (all must be green to queue): %s" % json.dumps(REQUIRED_GATES))
    print("reported until W5 (never gating; rec-20260925-a16786f5): %s" % json.dumps(REPORTED_UNTIL_W5))
    print("oracle diagnostic (report-only): env-Q stands in for E3's valuation on each variant's pool")


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
