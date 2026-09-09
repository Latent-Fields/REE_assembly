#!/usr/bin/env python3
"""Synthetic Convergence Assay 004: evidence independence vs downstream leverage.

Separates two graphs that Assay 003 intentionally conflated for convenience:
(1) dependence/provenance of current evidence and (2) number/weight of downstream
consumers that benefit from resolving the queried uncertainty.

Standalone synthetic measurement only; no creature, claims, or queue mutation.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np

import convergence_signal_synthetic_assay_002 as a2

TOPOLOGIES = (
    "independent_5",
    "copies_5",
    "shared_cluster_5",
    "two_clusters_3_2",
    "mixed_3_plus_2",
)
TOPOLOGY_P = np.array([0.20] * 5)
Q_VALUES = (0.50, 0.65, 0.80, 0.95)
Q_P = np.array([0.10, 0.25, 0.35, 0.30])
LEVERAGES = (1.0, 2.0, 4.0, 8.0)
LEVERAGE_P = np.array([0.25] * 4)


def hbin(p: float) -> float:
    p = min(max(float(p), 1e-12), 1.0 - 1e-12)
    return -(p * math.log(p) + (1.0 - p) * math.log(1.0 - p))


def eig(prior: float, q: float) -> float:
    """Expected binary entropy reduction from one q-reliable observation."""
    prior = float(prior)
    px = prior * q + (1.0 - prior) * (1.0 - q)
    post_plus = prior * q / px
    pminus = 1.0 - px
    post_minus = prior * (1.0 - q) / pminus
    return hbin(prior) - (px * hbin(post_plus) + pminus * hbin(post_minus))


def conditioned_votes(rng: np.random.Generator, topology: str, theta: int) -> tuple[int, ...]:
    y = np.array([theta], dtype=np.int8)
    if topology == "independent_5":
        v = a2._independent_votes(rng, y, [0.70] * 5)[0]
    elif topology == "copies_5":
        base = a2._independent_votes(rng, y, [0.70])[0, 0]
        v = np.repeat(base, 5)
    elif topology == "shared_cluster_5":
        v = a2._cluster_votes(rng, y, 5, 0.70, 0.70)[0]
    elif topology == "two_clusters_3_2":
        v = np.concatenate(
            [
                a2._cluster_votes(rng, y, 3, 0.70, 0.70)[0],
                a2._cluster_votes(rng, y, 2, 0.70, 0.70)[0],
            ]
        )
    elif topology == "mixed_3_plus_2":
        v = np.concatenate(
            [
                a2._cluster_votes(rng, y, 3, 0.70, 0.70)[0],
                a2._independent_votes(rng, y, [0.70, 0.70])[0],
            ]
        )
    else:
        raise ValueError(topology)
    return tuple(int(x) for x in v)


def build_calibration(seed: int = 1404, trials: int = 100_000):
    rng = np.random.default_rng(seed)
    out = {}
    for topology in TOPOLOGIES:
        y, votes, clusters = a2.generate(rng, trials, topology, 0.70)
        p_est, global_rho, cluster_rho = a2.calibrate(y, votes, clusters)
        out[topology] = {
            "clusters": clusters,
            "p_est": p_est,
            "global_rho": float(global_rho),
            "cluster_rho": [float(x) for x in cluster_rho],
        }
    return out


def score_bundle(topology: str, votes_t: tuple[int, ...], q: float, leverage: float, calibration):
    c = calibration[topology]
    v = np.array(votes_t, dtype=np.int8)[None, :]
    p_rel = float(a2.m0(v, c["p_est"])[0])
    p_global = float(a2.m1(v, c["p_est"], c["global_rho"])[0])
    p_top = float(a2.m2(v, c["p_est"], c["clusters"], c["cluster_rho"])[0])
    p_exact = float(a2.m3(v, topology, 0.70)[0])
    cluster_count = float(len(c["clusters"]))
    return {
        "M0_conflated": cluster_count * eig(p_top, q),
        "M1_leverage_only": leverage * eig(p_rel, q),
        "M2_global_factorized": leverage * eig(p_global, q),
        "M3_topology_factorized": leverage * eig(p_top, q),
        "M4_oracle": leverage * eig(p_exact, q),
    }


def build_cache(calibration):
    cache = {}
    for topology in TOPOLOGIES:
        for votes_t in itertools.product((-1, 1), repeat=5):
            for q in Q_VALUES:
                for leverage in LEVERAGES:
                    cache[(topology, votes_t, q, leverage)] = score_bundle(
                        topology, votes_t, q, leverage, calibration
                    )
    return cache


def choose_index(scores: np.ndarray) -> int:
    # Deterministic first-index tie-break, shared by every method.
    return int(np.argmax(scores))


def run_main(rng, cache, episodes: int, candidates: int):
    methods = (
        "M0_conflated",
        "M1_leverage_only",
        "M2_global_factorized",
        "M3_topology_factorized",
        "M4_oracle",
    )
    regret = {m: 0.0 for m in methods}
    hits = {m: 0 for m in methods}
    utility = {m: 0.0 for m in methods}
    oracle_total = 0.0
    oracle_violations = 0

    for _ in range(episodes):
        row = []
        for _ in range(candidates):
            topology = str(rng.choice(TOPOLOGIES, p=TOPOLOGY_P))
            theta = int(rng.choice((-1, 1)))
            votes_t = conditioned_votes(rng, topology, theta)
            q = float(rng.choice(Q_VALUES, p=Q_P))
            leverage = float(rng.choice(LEVERAGES, p=LEVERAGE_P))
            row.append(cache[(topology, votes_t, q, leverage)])

        true_values = np.array([x["M4_oracle"] for x in row], dtype=float)
        best = float(true_values.max())
        oracle_total += best

        for method in methods:
            scores = np.array([x[method] for x in row], dtype=float)
            idx = choose_index(scores)
            chosen = float(true_values[idx])
            if chosen > best + 1e-12:
                oracle_violations += 1
            regret[method] += best - chosen
            utility[method] += chosen
            hits[method] += abs(chosen - best) < 1e-12

    summary = {}
    for method in methods:
        summary[method] = {
            "mean_regret": regret[method] / episodes,
            "optimal_hit_rate": hits[method] / episodes,
            "oracle_utility_fraction": utility[method] / oracle_total,
        }
    return summary, oracle_violations


def run_forced_pair(rng, calibration, episodes: int):
    methods = (
        "M0_conflated",
        "M1_leverage_only",
        "M2_global_factorized",
        "M3_topology_factorized",
        "M4_oracle",
    )
    hits = {m: 0 for m in methods}
    regret = {m: 0.0 for m in methods}
    q_values = (0.65, 0.80, 0.95)

    for _ in range(episodes):
        q = float(rng.choice(q_values))
        row = []
        for topology, leverage in (("independent_5", 1.0), ("copies_5", 8.0)):
            theta = int(rng.choice((-1, 1)))
            votes_t = conditioned_votes(rng, topology, theta)
            row.append(score_bundle(topology, votes_t, q, leverage, calibration))

        true_values = np.array([x["M4_oracle"] for x in row], dtype=float)
        best = float(true_values.max())
        for method in methods:
            idx = choose_index(np.array([x[method] for x in row], dtype=float))
            chosen = float(true_values[idx])
            hits[method] += abs(chosen - best) < 1e-12
            regret[method] += best - chosen

    return {
        method: {
            "oracle_hit_rate": hits[method] / episodes,
            "mean_regret": regret[method] / episodes,
        }
        for method in methods
    }


def evaluate_criteria(main, forced, oracle_violations: int):
    r0 = main["M0_conflated"]["mean_regret"]
    r1 = main["M1_leverage_only"]["mean_regret"]
    r2 = main["M2_global_factorized"]["mean_regret"]
    r3 = main["M3_topology_factorized"]["mean_regret"]
    r4 = main["M4_oracle"]["mean_regret"]

    h2 = main["M2_global_factorized"]["optimal_hit_rate"]
    h3 = main["M3_topology_factorized"]["optimal_hit_rate"]

    c1 = r3 <= 0.10 * r0 and main["M3_topology_factorized"]["oracle_utility_fraction"] >= 0.98
    c2 = r3 <= 0.15 * r1
    c3 = r3 <= 0.90 * r2 and h3 >= h2 + 0.005
    c4 = forced["M3_topology_factorized"]["oracle_hit_rate"] >= 0.95 and forced["M0_conflated"]["oracle_hit_rate"] <= 0.40
    c5 = abs(r4) <= 1e-12 and oracle_violations == 0

    criteria = {
        "C1_factorization_defeats_conflation": bool(c1),
        "C1_M3_over_M0_regret_ratio": float(r3 / r0) if r0 > 0 else 0.0,
        "C1_M3_oracle_utility_fraction": main["M3_topology_factorized"]["oracle_utility_fraction"],
        "C2_both_axes_necessary": bool(c2),
        "C2_M3_over_M1_regret_ratio": float(r3 / r1) if r1 > 0 else 0.0,
        "C3_topology_beyond_global_scalar": bool(c3),
        "C3_M3_over_M2_regret_ratio": float(r3 / r2) if r2 > 0 else 0.0,
        "C3_hit_rate_gain": h3 - h2,
        "C4_forced_anti_conflation": bool(c4),
        "C4_M3_oracle_hit_rate": forced["M3_topology_factorized"]["oracle_hit_rate"],
        "C4_M0_oracle_hit_rate": forced["M0_conflated"]["oracle_hit_rate"],
        "C5_oracle_ceiling": bool(c5),
        "C5_oracle_violations": int(oracle_violations),
    }
    criteria["measurement_pass_C1_to_C5"] = bool(c1 and c2 and c3 and c4 and c5)
    return criteria


def run(seed: int = 23, episodes: int = 20_000, candidates: int = 6, forced_episodes: int = 20_000):
    calibration = build_calibration()
    cache = build_cache(calibration)
    rng = np.random.default_rng(seed)

    main, oracle_violations = run_main(rng, cache, episodes, candidates)
    forced = run_forced_pair(rng, calibration, forced_episodes)
    criteria = evaluate_criteria(main, forced, oracle_violations)

    return {
        "assay": "convergence_signal_synthetic_assay_004",
        "status": "synthetic_reference_run_only",
        "seed": seed,
        "calibration_seed": 1404,
        "calibration_trials_per_topology": 100_000,
        "episodes": episodes,
        "candidates_per_episode": candidates,
        "forced_pair_episodes": forced_episodes,
        "main": main,
        "forced_pair": forced,
        "criteria": criteria,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=23)
    parser.add_argument("--episodes", type=int, default=20_000)
    parser.add_argument("--candidates", type=int, default=6)
    parser.add_argument("--forced-episodes", type=int, default=20_000)
    parser.add_argument("--out-json", type=Path, default=None)
    args = parser.parse_args()

    payload = run(args.seed, args.episodes, args.candidates, args.forced_episodes)
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.out_json:
        args.out_json.parent.mkdir(parents=True, exist_ok=True)
        args.out_json.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
