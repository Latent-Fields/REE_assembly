"""A1 integrated closed-loop acceptance -- SCRIPT SKELETON (DRAFT; NOT QUEUED; NOT an experiment).

Pre-registration: REE_assembly/evidence/planning/coupled_a1_preregistration_draft_20260925.md
Plan of record:   REE_assembly/evidence/planning/coupled_loop_repair_campaign_plan.md (sec 5, 6, 9)
Author: bt0925-a1prereg, chip_ref chip-20260925-coupled-a1-preregistration-draft, 2026-09-25.

WHAT THIS FILE IS
  * The ARM WIRING and the ORDER OF OPERATIONS of the A1 run, with every call site of the I1
    instruments (ree-v3 experiments/_lib/coupled_acceptance.py) marked "I1-n".
  * The SCORING half (margins, criteria P1b/P1t/P1g/P2/P3/P4, the verdict ladder, the head-to-head
    rule) implemented in full as PURE functions, because those are what the pre-registration fixes.
    `--selftest` runs them on synthetic seeds and shows every criterion can FAIL and every
    CANNOT_DETERMINE / INVALID branch is reachable.
  * `--describe` prints the arm table and the per-seed order of operations.

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
FLOORS = {
    "benign": {"reward": 0.90, "contacts": 1.6, "reward_change": 0.92},
    "hazard_trapped": {"reward": 2.4, "contacts": 4.8, "reward_change": None},  # P4 is benign-only
}

VARIANTS = ("CODEC", "ASP")          # user decision rec-20260925-6a675285: both, head-to-head
VALUATION_MODES = ("GROUNDED", "ABSENT")  # fixed from C2 (V3-EXQ-1105a) verdict BEFORE any admitted seed runs

BENIGN, TRAPPED = "benign", "hazard_trapped"
PASS, FAIL, CD, INVALID = "PASS", "FAIL", "CANNOT_DETERMINE", "INVALID"


def arm_table(valuation_mode: str, noval_diag: bool = True) -> List[Dict[str, Any]]:
    """Every arm, what it is, and whether it is scored. Order = execution order within a seed."""
    arms = [dict(name="NATIVE", agent_seed_offset=0, preset=None, trainer=False, shuffle=False,
                 role="stratum source (sidecar) + comparator")]
    for k in range(1, N_RESEED + 1):
        arms.append(dict(name="NATIVE-R%d" % k, agent_seed_offset=k * AGENT_SEED_OFFSET, preset=None,
                         trainer=False, shuffle=False, role="margin calibration ONLY"))
    for v in VARIANTS:
        base = dict(preset="W6:%s:%s" % (v, valuation_mode), agent_seed_offset=0)
        arms.append(dict(name="INT-%s" % v, trainer=True, shuffle=False, role="tested", **base))
        arms.append(dict(name="INT-%s-SHUF" % v, trainer=True, shuffle=True, role="grounding control (P3)", **base))
        arms.append(dict(name="INT-%s-FROZEN" % v, trainer="off_in_closed_loop", shuffle=False,
                         role="learning control (P4)", **base))
        arms.append(dict(name="INT-%s-R1" % v, trainer=True, shuffle=False, preset=base["preset"],
                         agent_seed_offset=AGENT_SEED_OFFSET, role="INT margin calibration ONLY (RT-2)"))
        if valuation_mode == "GROUNDED" and noval_diag:
            arms.append(dict(name="INT-%s-NOVAL" % v, trainer=True, shuffle=False,
                             preset="W6:%s:ABSENT" % v, agent_seed_offset=0,
                             role="REPORTED ONLY (valuation contribution; no criterion)"))
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
    #     R1  I1-4 cem_codec_trace / codec_ranges / codec_roundtrip_accuracy   (CODEC variant only)
    #     R2  I1-1 action_discrimination(e2_world_predictor(agent.e2), held-out uniform set)
    #         real head meets W3(a); SHUF head does NOT
    #     R3  I1-2 collect_probe_states + I1-3 e3_depth_structure / head_swap_flip_rate (W4(c))
    #     R4  1105a primary detector D_N silent on INT (GROUNDED mode only)
    #     R5  per-group held-out loss at LAST < FROZEN's
    # Reported (no criterion): I1-4 proposal_m4, pool_qbest_coverage; action entropy; ARC-016
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
      1. INVALID  if any admitted seed has a failed precondition R0-R6 for this variant.
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
    c["P1g"] = _count(b, lambda s: W(s, T)["grounded_LAST"] - W(s, "NATIVE")["grounded_LAST"] > 0.0)
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
    return {"verdict": PASS, "winner": "ASP", "note": "both PASS within margin; simpler variant (ASP deletes the codec)"}


# ----------------------------------------------------------------------------- self-test (synthetic)
def _synthetic(stratum: str, seed: int, gain: float, *, shuf_gain: Optional[float] = None, frozen_learn: float = 0.0,
               contacts_up: float = 0.0, grounded_delta: float = 0.1, noise: float = 0.05, n_reseed: int = 3,
               pre_ok: bool = True, int_noise: float = 0.05, g_tie: bool = False) -> Dict[str, Any]:
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
    return {"seed": seed, "stratum": stratum, "arms": arms,
            "preconditions": {v: {"R0": pre_ok, "R1": True, "R2": True, "R3": True, "R4": True, "R5": True, "R6": True}
                              for v in VARIANTS}}


def selftest() -> int:
    ok = True
    def case(name, strata, want):
        nonlocal ok
        r = score_variant("CODEC", strata)
        got = r["verdict"]
        flag = "ok " if got == want else "BAD"
        ok &= got == want
        print("%s %-44s -> %-16s %s" % (flag, name, got, r.get("fail_signatures", r.get("reason", ""))))
    good = lambda g: [_synthetic(g, s, 1.5 if g == BENIGN else 0.0, shuf_gain=0.0 if g == BENIGN else -3.0)  # noqa: E731
                      for s in range(5)]
    # P3t needs INT > SHUF by margin on trapped too: give SHUF a large deficit there.
    case("all criteria hold", {BENIGN: good(BENIGN), TRAPPED: good(TRAPPED)}, PASS)
    case("P1b fails (no benign gain)", {BENIGN: [_synthetic(BENIGN, s, 0.1, shuf_gain=-1.0) for s in range(5)],
                                        TRAPPED: good(TRAPPED)}, FAIL)
    case("P1g fails (gain carried by shaping)", {BENIGN: [_synthetic(BENIGN, s, 1.5, shuf_gain=0.0, grounded_delta=-0.3)
                                                          for s in range(5)], TRAPPED: good(TRAPPED)}, FAIL)
    case("P2 fails (undirected: contacts up)", {BENIGN: [_synthetic(BENIGN, s, 1.5, shuf_gain=0.0, contacts_up=3.0)
                                                         for s in range(5)], TRAPPED: good(TRAPPED)}, FAIL)
    case("P3 fails (SHUF as good)", {BENIGN: [_synthetic(BENIGN, s, 1.5, shuf_gain=1.5) for s in range(5)],
                                     TRAPPED: good(TRAPPED)}, FAIL)
    case("P4 fails (FROZEN learns as much)", {BENIGN: [_synthetic(BENIGN, s, 1.5, shuf_gain=0.0, frozen_learn=1.5)
                                                       for s in range(5)], TRAPPED: good(TRAPPED)}, FAIL)
    case("P1t fails (trapped much worse)", {BENIGN: good(BENIGN),
                                            TRAPPED: [_synthetic(TRAPPED, s, -5.0, shuf_gain=-9.0) for s in range(5)]}, FAIL)
    case("stratum under-admitted", {BENIGN: good(BENIGN), TRAPPED: good(TRAPPED)[:4]}, CD)
    case("reseeds short -> margin CD", {BENIGN: [_synthetic(BENIGN, s, 1.5, shuf_gain=0.0, n_reseed=1) for s in range(5)],
                                        TRAPPED: good(TRAPPED)}, CD)
    case("precondition failed -> INVALID", {BENIGN: [_synthetic(BENIGN, 0, 1.5, pre_ok=False)] + good(BENIGN)[1:],
                                            TRAPPED: good(TRAPPED)}, INVALID)
    # floor binding: zero reseed noise must not make the margin vacuous
    z = {BENIGN: [_synthetic(BENIGN, s, 0.6, shuf_gain=-1.0, noise=0.0) for s in range(5)], TRAPPED: good(TRAPPED)}
    case("zero reseed noise: floor binds (gain 0.6 < 0.90)", z, FAIL)
    case("RT-1 P1g tie 0=0 (shaping-only gain) fails", {BENIGN: [_synthetic(BENIGN, s, 1.5, shuf_gain=0.0, g_tie=True)
                                                               for s in range(5)], TRAPPED: good(TRAPPED)}, FAIL)
    case("RT-2 non-inferiority margin balloons -> CD", {BENIGN: good(BENIGN),
                                                       TRAPPED: [_synthetic(TRAPPED, s, 0.0, shuf_gain=-40.0, noise=8.0)
                                                                 for s in range(5)]}, CD)
    case("RT-2 INT reseed noise large -> P1b fails", {BENIGN: [_synthetic(BENIGN, s, 1.5, shuf_gain=0.0, int_noise=2.0)
                                                             for s in range(5)], TRAPPED: good(TRAPPED)}, FAIL)
    print("SELFTEST %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def describe() -> None:
    for mode in VALUATION_MODES:
        print("valuation_mode=%s" % mode)
        for a in arm_table(mode):
            print("  %-18s trainer=%-20s shuffle=%-5s seed_offset=%-6d %s"
                  % (a["name"], a["trainer"], a["shuffle"], a["agent_seed_offset"], a["role"]))
    print("per-seed order: pin(R6) -> NATIVE to closed-loop step 599 -> classify + write sidecar (I1-5)"
          " -> NATIVE to 3000 -> NATIVE-R1..R3 -> INT-* arms (each calls require_stratum_sidecar first)")
    print("floors: %s" % json.dumps(FLOORS))


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
