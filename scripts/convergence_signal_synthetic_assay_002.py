#!/usr/bin/env python3
"""Synthetic Convergence Assay 002: exact-Bayes ceiling vs cheap dependency topology.

Standalone measurement assay. It does not mutate REE creature state, claims, or the
experiment queue. See evidence/planning/convergence_signal_synthetic_assay_002_bayes_ceiling.md.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import numpy as np

REGIMES = (
    "independent_5",
    "copies_5",
    "shared_cluster_5",
    "two_clusters_3_2",
    "mixed_3_plus_2",
    "minority_expert",
)
CORRELATED = ("shared_cluster_5", "two_clusters_3_2", "mixed_3_plus_2")


def _logit(p: np.ndarray | float) -> np.ndarray:
    p = np.clip(np.asarray(p, dtype=float), 1e-9, 1 - 1e-9)
    return np.log(p / (1 - p))


def _posterior(log_odds: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(log_odds, -50, 50)))


def _independent_votes(rng, y, ps):
    ps = np.asarray(ps, dtype=float)
    correct = rng.random((len(y), len(ps))) < ps
    return np.where(correct, y[:, None], -y[:, None]).astype(np.int8)


def _cluster_votes(rng, y, size, p, alpha):
    use_shared = rng.random(len(y)) < alpha
    shared_correct = rng.random(len(y)) < p
    shared_vote = np.where(shared_correct, y, -y)
    independent_correct = rng.random((len(y), size)) < p
    votes = np.where(independent_correct, y[:, None], -y[:, None]).astype(np.int8)
    votes[use_shared] = shared_vote[use_shared, None]
    return votes


def generate(rng, n: int, regime: str, alpha: float = 0.70):
    y = rng.choice(np.array([-1, 1], dtype=np.int8), size=n)
    if regime == "independent_5":
        votes = _independent_votes(rng, y, [0.70] * 5)
        clusters = [[0], [1], [2], [3], [4]]
    elif regime == "copies_5":
        base = _independent_votes(rng, y, [0.70])[:, 0]
        votes = np.repeat(base[:, None], 5, axis=1)
        clusters = [[0, 1, 2, 3, 4]]
    elif regime == "shared_cluster_5":
        votes = _cluster_votes(rng, y, 5, 0.70, alpha)
        clusters = [[0, 1, 2, 3, 4]]
    elif regime == "two_clusters_3_2":
        votes = np.concatenate(
            [_cluster_votes(rng, y, 3, 0.70, alpha), _cluster_votes(rng, y, 2, 0.70, alpha)],
            axis=1,
        )
        clusters = [[0, 1, 2], [3, 4]]
    elif regime == "mixed_3_plus_2":
        votes = np.concatenate(
            [_cluster_votes(rng, y, 3, 0.70, alpha), _independent_votes(rng, y, [0.70, 0.70])],
            axis=1,
        )
        clusters = [[0, 1, 2], [3], [4]]
    elif regime == "minority_expert":
        votes = _independent_votes(rng, y, [0.65, 0.65, 0.65, 0.65, 0.90])
        clusters = [[0], [1], [2], [3], [4]]
    else:
        raise ValueError(regime)
    return y, votes, clusters


def calibrate(y: np.ndarray, votes: np.ndarray, clusters: List[List[int]]):
    correctness = (votes == y[:, None]).astype(float)
    p_est = correctness.mean(axis=0)
    corr = np.corrcoef(correctness, rowvar=False)
    if votes.shape[1] > 1:
        ii = np.triu_indices(votes.shape[1], 1)
        global_rho = max(0.0, float(np.nanmean(corr[ii])))
    else:
        global_rho = 0.0
    cluster_rho = []
    for cl in clusters:
        if len(cl) == 1:
            cluster_rho.append(0.0)
        else:
            sub = corr[np.ix_(cl, cl)]
            ii = np.triu_indices(len(cl), 1)
            cluster_rho.append(max(0.0, float(np.nanmean(sub[ii]))))
    return p_est, global_rho, cluster_rho


def m0(votes, p_est):
    return _posterior((votes * _logit(p_est)[None, :]).sum(axis=1))


def m1(votes, p_est, global_rho):
    n = votes.shape[1]
    n_eff = n / (1 + (n - 1) * min(global_rho, 0.999))
    lod = (votes * _logit(p_est)[None, :]).sum(axis=1) * (n_eff / n)
    return _posterior(lod)


def m2(votes, p_est, clusters, cluster_rho):
    lod = np.zeros(len(votes), dtype=float)
    for cl, rho in zip(clusters, cluster_rho):
        if len(cl) == 1:
            j = cl[0]
            lod += votes[:, j] * _logit(p_est[j])
        else:
            m = len(cl)
            n_eff = m / (1 + (m - 1) * min(rho, 0.999))
            lod += (votes[:, cl] * _logit(p_est[cl])[None, :]).sum(axis=1) * (n_eff / m)
    return _posterior(lod)


def _cluster_like(votes, y_value, p, alpha):
    matches = votes == y_value
    independent = np.prod(np.where(matches, p, 1 - p), axis=1)
    unanimous = np.all(votes == votes[:, [0]], axis=1)
    shared = np.zeros(len(votes), dtype=float)
    same = votes[:, 0] == y_value
    shared[unanimous & same] = p
    shared[unanimous & ~same] = 1 - p
    return alpha * shared + (1 - alpha) * independent


def m3(votes, regime: str, alpha: float = 0.70):
    if regime == "independent_5":
        ps = np.array([0.70] * 5)
        lp = np.prod(np.where(votes == 1, ps, 1 - ps), axis=1)
        lm = np.prod(np.where(votes == -1, ps, 1 - ps), axis=1)
    elif regime == "copies_5":
        unanimous = np.all(votes == votes[:, [0]], axis=1)
        lp = np.where(unanimous, np.where(votes[:, 0] == 1, 0.70, 0.30), 0.0)
        lm = np.where(unanimous, np.where(votes[:, 0] == -1, 0.70, 0.30), 0.0)
    elif regime == "shared_cluster_5":
        lp = _cluster_like(votes, 1, 0.70, alpha)
        lm = _cluster_like(votes, -1, 0.70, alpha)
    elif regime == "two_clusters_3_2":
        lp = _cluster_like(votes[:, :3], 1, 0.70, alpha) * _cluster_like(votes[:, 3:], 1, 0.70, alpha)
        lm = _cluster_like(votes[:, :3], -1, 0.70, alpha) * _cluster_like(votes[:, 3:], -1, 0.70, alpha)
    elif regime == "mixed_3_plus_2":
        lp = _cluster_like(votes[:, :3], 1, 0.70, alpha)
        lm = _cluster_like(votes[:, :3], -1, 0.70, alpha)
        for j in (3, 4):
            lp *= np.where(votes[:, j] == 1, 0.70, 0.30)
            lm *= np.where(votes[:, j] == -1, 0.70, 0.30)
    elif regime == "minority_expert":
        ps = np.array([0.65, 0.65, 0.65, 0.65, 0.90])
        lp = np.prod(np.where(votes == 1, ps, 1 - ps), axis=1)
        lm = np.prod(np.where(votes == -1, ps, 1 - ps), axis=1)
    else:
        raise ValueError(regime)
    den = lp + lm
    return np.divide(lp, den, out=np.full(len(votes), 0.5), where=den > 0)


def score(post, y):
    target = (y == 1).astype(float)
    clipped = np.clip(post, 1e-12, 1 - 1e-12)
    brier = float(np.mean((post - target) ** 2))
    logloss = float(np.mean(-(target * np.log(clipped) + (1 - target) * np.log(1 - clipped))))
    bins = np.minimum((post * 10).astype(int), 9)
    ece = 0.0
    for b in range(10):
        mask = bins == b
        if mask.any():
            ece += float(mask.mean()) * abs(float(post[mask].mean()) - float(target[mask].mean()))
    return {"brier": brier, "log_loss": logloss, "ece10": ece}


def selected_confidence(post, votes):
    majority = np.sign(votes.sum(axis=1))
    return np.where(majority == 1, post, 1 - post)


def run(seed=11, calibration_trials=200_000, test_trials=200_000):
    rng = np.random.default_rng(seed)
    calibration = {}
    for regime in REGIMES:
        y, votes, clusters = generate(rng, calibration_trials, regime, 0.70)
        p_est, global_rho, cluster_rho = calibrate(y, votes, clusters)
        calibration[regime] = {
            "clusters": clusters,
            "p_est": p_est,
            "global_rho": global_rho,
            "cluster_rho": cluster_rho,
        }

    in_dist = {}
    retained = {}
    for regime in REGIMES:
        y, votes, _ = generate(rng, test_trials, regime, 0.70)
        c = calibration[regime]
        posts = {
            "M0": m0(votes, c["p_est"]),
            "M1": m1(votes, c["p_est"], c["global_rho"]),
            "M2": m2(votes, c["p_est"], c["clusters"], c["cluster_rho"]),
            "M3": m3(votes, regime, 0.70),
        }
        in_dist[regime] = {method: score(post, y) for method, post in posts.items()}
        retained[regime] = (y, votes, posts)

    shifts = {}
    for regime in CORRELATED:
        c = calibration[regime]
        shifts[regime] = {}
        for alpha in (0.30, 0.70, 0.90):
            y, votes, _ = generate(rng, test_trials, regime, alpha)
            posts = {
                "M0": m0(votes, c["p_est"]),
                "M1": m1(votes, c["p_est"], c["global_rho"]),
                "M2": m2(votes, c["p_est"], c["clusters"], c["cluster_rho"]),
                "M3": m3(votes, regime, alpha),
            }
            shifts[regime][str(alpha)] = {method: score(post, y) for method, post in posts.items()}

    # C1
    c1_improvements = [
        in_dist[r]["M1"]["brier"] - in_dist[r]["M2"]["brier"]
        for r in ("two_clusters_3_2", "mixed_3_plus_2")
    ]
    c1_mean = float(np.mean(c1_improvements))
    c1 = c1_mean >= 0.005 and min(c1_improvements) >= -0.002

    # C2
    c2_deltas = {r: in_dist[r]["M3"]["brier"] - in_dist[r]["M2"]["brier"] for r in REGIMES}
    c2 = all(delta <= 0.001 for delta in c2_deltas.values())

    # C3
    y, votes, posts = retained["copies_5"]
    empirical_copy_accuracy = float((np.sign(votes.sum(axis=1)) == y).mean())
    m0_copy_conf = float(selected_confidence(posts["M0"], votes).mean())
    m2_copy_conf = float(selected_confidence(posts["M2"], votes).mean())
    c3 = abs(m2_copy_conf - empirical_copy_accuracy) <= 0.03 and (m0_copy_conf - m2_copy_conf) >= 0.15

    # C4
    y, votes, posts = retained["minority_expert"]
    dissent = np.all(votes[:, :4] == votes[:, [0]], axis=1) & (votes[:, 4] == -votes[:, 0])
    m2_majority_conf = float(np.where(votes[:, 0] == 1, posts["M2"], 1 - posts["M2"])[dissent].mean())
    m0_majority_conf = float(np.where(votes[:, 0] == 1, posts["M0"], 1 - posts["M0"])[dissent].mean())
    exact_majority_conf = float(np.where(votes[:, 0] == 1, posts["M3"], 1 - posts["M3"])[dissent].mean())
    raw_majority_conf = 0.80
    c4 = m2_majority_conf < raw_majority_conf and m2_majority_conf <= m0_majority_conf + 1e-9

    # C5: compare mean Brier change from alpha=.70 across correlated regimes.
    shift_details = {}
    c5 = True
    for alpha in (0.30, 0.90):
        m1_changes = []
        m2_changes = []
        for r in CORRELATED:
            base1 = shifts[r]["0.7"]["M1"]["brier"]
            base2 = shifts[r]["0.7"]["M2"]["brier"]
            m1_changes.append(shifts[r][str(alpha)]["M1"]["brier"] - base1)
            m2_changes.append(shifts[r][str(alpha)]["M2"]["brier"] - base2)
        mean1 = float(np.mean(m1_changes))
        mean2 = float(np.mean(m2_changes))
        shift_details[str(alpha)] = {"M1_mean_brier_change": mean1, "M2_mean_brier_change": mean2, "M2_minus_M1": mean2 - mean1}
        if mean2 - mean1 > 0.005:
            c5 = False

    criteria = {
        "C1_topology_beats_global_Neff": c1,
        "C1_regime_improvements": c1_improvements,
        "C1_mean_brier_improvement": c1_mean,
        "C2_exact_bayes_ceiling": c2,
        "C2_M3_minus_M2_brier": c2_deltas,
        "C3_duplicate_trap": c3,
        "C3_empirical_copy_accuracy": empirical_copy_accuracy,
        "C3_M0_copy_confidence": m0_copy_conf,
        "C3_M2_copy_confidence": m2_copy_conf,
        "C4_minority_expert_protection": c4,
        "C4_dissent_pattern_rate": float(dissent.mean()),
        "C4_raw_majority_confidence": raw_majority_conf,
        "C4_M0_majority_confidence": m0_majority_conf,
        "C4_M2_majority_confidence": m2_majority_conf,
        "C4_exact_majority_confidence": exact_majority_conf,
        "C5_shift_graceful": c5,
        "C5_shift_details": shift_details,
    }
    criteria["measurement_pass_C1_to_C5"] = bool(c1 and c2 and c3 and c4 and c5)

    return {
        "assay": "convergence_signal_synthetic_assay_002",
        "status": "synthetic_reference_run_only",
        "seed": seed,
        "calibration_trials": calibration_trials,
        "test_trials": test_trials,
        "calibration": {
            r: {
                "clusters": c["clusters"],
                "p_est": [float(x) for x in c["p_est"]],
                "global_rho": float(c["global_rho"]),
                "cluster_rho": [float(x) for x in c["cluster_rho"]],
            }
            for r, c in calibration.items()
        },
        "in_distribution": in_dist,
        "dependency_shift": shifts,
        "criteria": criteria,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=11)
    parser.add_argument("--calibration-trials", type=int, default=200_000)
    parser.add_argument("--test-trials", type=int, default=200_000)
    parser.add_argument("--out-json", type=Path, default=None)
    args = parser.parse_args()
    payload = run(args.seed, args.calibration_trials, args.test_trials)
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.out_json:
        args.out_json.parent.mkdir(parents=True, exist_ok=True)
        args.out_json.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
