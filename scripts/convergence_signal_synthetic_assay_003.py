#!/usr/bin/env python3
"""Synthetic Convergence Assay 003: structured divergence and query allocation.

Uses Assay-002 aggregation primitives. Standalone synthetic measurement only;
no creature, claims, or queue mutation.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np

import convergence_signal_synthetic_assay_002 as a2

TOPOLOGIES = ("independent_5", "copies_5", "shared_cluster_5", "two_clusters_3_2", "mixed_3_plus_2")
TOPOLOGY_P = np.array([0.25, 0.15, 0.15, 0.20, 0.25])
CLUSTER_COUNT = {"independent_5": 5, "copies_5": 1, "shared_cluster_5": 1, "two_clusters_3_2": 2, "mixed_3_plus_2": 3}
Q_VALUES = (0.50, 0.65, 0.80, 0.95)
Q_P = np.array([0.20, 0.25, 0.30, 0.25])
W_ENTRIES = (1.0, 1.0, 1.0, 2.0, 4.0)


def hbin(p):
    p = min(max(float(p), 1e-12), 1 - 1e-12)
    return -(p * math.log(p) + (1 - p) * math.log(1 - p))


def eig(prior, q):
    prior = float(prior)
    px = prior * q + (1 - prior) * (1 - q)
    post_plus = prior * q / px
    pminus = 1 - px
    post_minus = prior * (1 - q) / pminus
    return hbin(prior) - (px * hbin(post_plus) + pminus * hbin(post_minus))


def conditioned_votes(rng, topology, theta):
    y = np.array([theta], dtype=np.int8)
    if topology == "independent_5":
        v = a2._independent_votes(rng, y, [0.70] * 5)[0]
    elif topology == "copies_5":
        base = a2._independent_votes(rng, y, [0.70])[0, 0]
        v = np.repeat(base, 5)
    elif topology == "shared_cluster_5":
        v = a2._cluster_votes(rng, y, 5, 0.70, 0.70)[0]
    elif topology == "two_clusters_3_2":
        v = np.concatenate([a2._cluster_votes(rng, y, 3, 0.70, 0.70)[0], a2._cluster_votes(rng, y, 2, 0.70, 0.70)[0]])
    elif topology == "mixed_3_plus_2":
        v = np.concatenate([a2._cluster_votes(rng, y, 3, 0.70, 0.70)[0], a2._independent_votes(rng, y, [0.70, 0.70])[0]])
    else:
        raise ValueError(topology)
    return tuple(int(x) for x in v)


def build_calibration(seed=1103, trials=200_000):
    rng = np.random.default_rng(seed)
    out = {}
    for topology in TOPOLOGIES:
        y, votes, clusters = a2.generate(rng, trials, topology, 0.70)
        p_est, global_rho, cluster_rho = a2.calibrate(y, votes, clusters)
        out[topology] = (clusters, p_est, float(global_rho), [float(x) for x in cluster_rho])
    return out


def build_cache(calibration):
    cache = {}
    for topology in TOPOLOGIES:
        clusters, p_est, global_rho, cluster_rho = calibration[topology]
        n_eff = 5 / (1 + 4 * global_rho)
        for vt in itertools.product((-1, 1), repeat=5):
            v = np.array(vt, dtype=np.int8)[None, :]
            p0 = float(a2.m0(v, p_est)[0])
            p1 = float(a2.m1(v, p_est, global_rho)[0])
            p2 = float(a2.m2(v, p_est, clusters, cluster_rho)[0])
            p3 = float(a2.m3(v, topology, 0.70)[0])
            frac = sum(x == 1 for x in vt) / 5
            raw_unc = 1 - abs(2 * frac - 1)
            raw_dis = 4 * frac * (1 - frac)
            for q in Q_VALUES:
                for w in (1.0, 2.0, 4.0):
                    cache[(topology, vt, q, w)] = {
                        "raw_unc": raw_unc,
                        "raw_dis": raw_dis,
                        "reliability_voi": 5 * w * eig(p0, q),
                        "global_neff_voi": n_eff * w * eig(p1, q),
                        "topology_voi": CLUSTER_COUNT[topology] * w * eig(p2, q),
                        "true": CLUSTER_COUNT[topology] * w * eig(p3, q),
                    }
    return cache


def run(seed=17, episodes=20_000, candidates=6):
    calibration = build_calibration()
    cache = build_cache(calibration)
    rng = np.random.default_rng(seed)
    methods = ("raw_unc", "raw_dis", "reliability_voi", "global_neff_voi", "topology_voi", "oracle")
    regret = {m: 0.0 for m in methods}
    hits = {m: 0 for m in methods}
    noise = {m: 0 for m in methods}
    utility = {m: 0.0 for m in methods}
    selected_topology = {m: {t: 0 for t in TOPOLOGIES} for m in methods}
    selected_weight = {m: {1.0: 0, 2.0: 0, 4.0: 0} for m in methods}
    oracle_total = 0.0
    oracle_violations = 0

    for _ in range(episodes):
        row = []
        for _ in range(candidates):
            topology = str(rng.choice(TOPOLOGIES, p=TOPOLOGY_P))
            theta = int(rng.choice((-1, 1)))
            votes = conditioned_votes(rng, topology, theta)
            q = float(rng.choice(Q_VALUES, p=Q_P))
            w = float(rng.choice(W_ENTRIES))
            row.append((topology, q, w, cache[(topology, votes, q, w)]))

        true_values = np.array([x[3]["true"] for x in row])
        best = float(true_values.max())
        oracle_total += best
        scores = {
            "raw_unc": np.array([x[3]["raw_unc"] for x in row]),
            "raw_dis": np.array([x[3]["raw_dis"] for x in row]),
            "reliability_voi": np.array([x[3]["reliability_voi"] for x in row]),
            "global_neff_voi": np.array([x[3]["global_neff_voi"] for x in row]),
            "topology_voi": np.array([x[3]["topology_voi"] for x in row]),
            "oracle": true_values,
        }
        for method in methods:
            idx = int(np.argmax(scores[method]))
            chosen = float(true_values[idx])
            if chosen > best + 1e-12:
                oracle_violations += 1
            regret[method] += best - chosen
            utility[method] += chosen
            hits[method] += abs(chosen - best) < 1e-12
            noise[method] += row[idx][1] == 0.50
            selected_topology[method][row[idx][0]] += 1
            selected_weight[method][row[idx][2]] += 1

    summary = {}
    for method in methods:
        summary[method] = {
            "mean_regret": regret[method] / episodes,
            "optimal_hit_rate": hits[method] / episodes,
            "irreducible_q05_select_rate": noise[method] / episodes,
            "oracle_utility_fraction": utility[method] / oracle_total,
            "selected_topology_fraction": {k: v / episodes for k, v in selected_topology[method].items()},
            "selected_weight_fraction": {str(k): v / episodes for k, v in selected_weight[method].items()},
        }

    c1 = summary["topology_voi"]["mean_regret"] <= 0.70 * summary["global_neff_voi"]["mean_regret"] and summary["topology_voi"]["mean_regret"] <= 0.020
    c2 = summary["topology_voi"]["optimal_hit_rate"] >= summary["global_neff_voi"]["optimal_hit_rate"] + 0.03
    c3 = summary["topology_voi"]["irreducible_q05_select_rate"] <= 0.01 and summary["raw_dis"]["irreducible_q05_select_rate"] - summary["topology_voi"]["irreducible_q05_select_rate"] >= 0.10
    c4 = summary["oracle"]["mean_regret"] < 1e-12 and oracle_violations == 0
    c5 = summary["topology_voi"]["mean_regret"] < summary["reliability_voi"]["mean_regret"] and summary["topology_voi"]["optimal_hit_rate"] >= summary["reliability_voi"]["optimal_hit_rate"]
    criteria = {
        "C1_topology_regret_gain": bool(c1),
        "C2_hit_rate_gain": bool(c2),
        "C3_irreducible_noise_avoidance": bool(c3),
        "C4_oracle_ceiling": bool(c4),
        "C5_beyond_reliability_consequence": bool(c5),
    }
    criteria["measurement_pass_C1_to_C5"] = all(criteria.values())
    return {
        "assay": "convergence_signal_synthetic_assay_003",
        "status": "synthetic_reference_run_only",
        "seed": seed,
        "episodes": episodes,
        "candidates_per_episode": candidates,
        "methods": summary,
        "criteria": criteria,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=17)
    parser.add_argument("--episodes", type=int, default=20_000)
    parser.add_argument("--candidates", type=int, default=6)
    parser.add_argument("--out-json", type=Path, default=None)
    args = parser.parse_args()
    payload = run(args.seed, args.episodes, args.candidates)
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.out_json:
        args.out_json.parent.mkdir(parents=True, exist_ok=True)
        args.out_json.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
