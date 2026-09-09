#!/usr/bin/env python3
"""Reference driver for Convergence Signal Synthetic Assay 001.

This script is deliberately standalone and lightweight. It tests whether a cheap
independence-aware confidence heuristic can distinguish five genuinely independent
70%-reliable evaluators from five copies of one 70%-reliable evaluator, plus two
intermediate dependency regimes.

This is a synthetic measurement assay, not a REE creature experiment and not claim
evidence until an authoritative run is reviewed and banked separately.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Tuple

import numpy as np


REGIMES = ("independent", "copies", "shared_bias", "mixed")


@dataclass
class RegimeSummary:
    regime: str
    p_est: float
    rho_bar: float
    n_eff: float
    majority_accuracy: float
    unanimity_rate: float
    unanimity_accuracy: float
    naive_unanimity_confidence: float
    reliability_only_unanimity_confidence: float
    independence_aware_unanimity_confidence: float
    independence_aware_brier: float


def _draw_correct(rng: np.random.Generator, n: int, p: float) -> np.ndarray:
    return rng.random(n) < p


def generate_votes(
    rng: np.random.Generator,
    n: int,
    p: float,
    shared_rho: float,
    regime: str,
) -> Tuple[np.ndarray, np.ndarray]:
    """Return labels y in {-1,+1} and vote matrix shape [n,5]."""
    y = rng.choice(np.array([-1, 1], dtype=np.int8), size=n)

    if regime == "independent":
        correct = rng.random((n, 5)) < p
        votes = np.where(correct, y[:, None], -y[:, None])

    elif regime == "copies":
        base_correct = _draw_correct(rng, n, p)
        base = np.where(base_correct, y, -y)
        votes = np.repeat(base[:, None], 5, axis=1)

    elif regime == "shared_bias":
        use_shared = rng.random(n) < shared_rho
        shared_correct = _draw_correct(rng, n, p)
        shared_vote = np.where(shared_correct, y, -y)

        independent_correct = rng.random((n, 5)) < p
        votes = np.where(independent_correct, y[:, None], -y[:, None])
        votes[use_shared] = shared_vote[use_shared, None]

    elif regime == "mixed":
        use_shared = rng.random(n) < shared_rho
        shared_correct = _draw_correct(rng, n, p)
        shared_vote = np.where(shared_correct, y, -y)

        cluster_correct = rng.random((n, 3)) < p
        cluster = np.where(cluster_correct, y[:, None], -y[:, None])
        cluster[use_shared] = shared_vote[use_shared, None]

        independent_correct = rng.random((n, 2)) < p
        independent = np.where(independent_correct, y[:, None], -y[:, None])
        votes = np.concatenate([cluster, independent], axis=1)

    else:
        raise ValueError(f"unknown regime: {regime}")

    return y.astype(np.int8), votes.astype(np.int8)


def estimate_dependency(y: np.ndarray, votes: np.ndarray) -> Tuple[float, float, float]:
    """Estimate marginal accuracy, mean pairwise correctness correlation and N_eff.

    Label access is permitted only on the calibration split. The max(0, rho)
    truncation is intentionally conservative for this first positive-correlation
    assay; handling anti-correlated specialists belongs to a later experiment.
    """
    correct = (votes == y[:, None]).astype(np.float64)
    p_est = float(correct.mean())

    corr = np.corrcoef(correct, rowvar=False)
    offdiag = corr[np.triu_indices_from(corr, 1)]
    rho_bar = float(np.nanmean(offdiag))
    rho_bar = max(0.0, min(0.999, rho_bar))

    n = votes.shape[1]
    n_eff = float(n / (1.0 + (n - 1) * rho_bar))
    return p_est, rho_bar, n_eff


def sigmoid(x: np.ndarray | float) -> np.ndarray | float:
    x_arr = np.asarray(x, dtype=np.float64)
    out = 1.0 / (1.0 + np.exp(-x_arr))
    return float(out) if out.ndim == 0 else out


def reliability_only_confidence(votes: np.ndarray, p_est: float) -> np.ndarray:
    """Equal-reliability independent-source posterior approximation."""
    p = min(max(p_est, 1e-6), 1.0 - 1e-6)
    logit = math.log(p / (1.0 - p))
    signed_strength = np.abs(votes.sum(axis=1)).astype(np.float64)
    return np.asarray(sigmoid(signed_strength * logit))


def independence_aware_confidence(
    votes: np.ndarray, p_est: float, n_eff: float
) -> np.ndarray:
    """Cheap effective-source correction preregistered in the assay design."""
    p = min(max(p_est, 1e-6), 1.0 - 1e-6)
    logit = math.log(p / (1.0 - p))
    n = votes.shape[1]
    signed_strength = np.abs(votes.sum(axis=1)).astype(np.float64)
    corrected_log_odds = signed_strength * (n_eff / n) * logit
    return np.asarray(sigmoid(corrected_log_odds))


def summarize_regime(
    regime: str,
    y_cal: np.ndarray,
    votes_cal: np.ndarray,
    y_test: np.ndarray,
    votes_test: np.ndarray,
) -> RegimeSummary:
    p_est, rho_bar, n_eff = estimate_dependency(y_cal, votes_cal)

    majority = np.sign(votes_test.sum(axis=1)).astype(np.int8)
    correct = majority == y_test
    unanimous = np.abs(votes_test.sum(axis=1)) == votes_test.shape[1]

    rel_conf = reliability_only_confidence(votes_test, p_est)
    ind_conf = independence_aware_confidence(votes_test, p_est, n_eff)

    if unanimous.any():
        unanimity_accuracy = float(correct[unanimous].mean())
        rel_unanimity_confidence = float(rel_conf[unanimous].mean())
        ind_unanimity_confidence = float(ind_conf[unanimous].mean())
    else:
        unanimity_accuracy = float("nan")
        rel_unanimity_confidence = float("nan")
        ind_unanimity_confidence = float("nan")

    brier = float(np.mean((ind_conf - correct.astype(np.float64)) ** 2))

    return RegimeSummary(
        regime=regime,
        p_est=p_est,
        rho_bar=rho_bar,
        n_eff=n_eff,
        majority_accuracy=float(correct.mean()),
        unanimity_rate=float(unanimous.mean()),
        unanimity_accuracy=unanimity_accuracy,
        naive_unanimity_confidence=1.0,
        reliability_only_unanimity_confidence=rel_unanimity_confidence,
        independence_aware_unanimity_confidence=ind_unanimity_confidence,
        independence_aware_brier=brier,
    )


def evaluate_preregistered_criteria(results: Dict[str, RegimeSummary]) -> Dict[str, object]:
    independent = results["independent"]
    copies = results["copies"]
    shared = results["shared_bias"]
    mixed = results["mixed"]

    c1_gap = (
        independent.independence_aware_unanimity_confidence
        - copies.independence_aware_unanimity_confidence
    )
    c1 = c1_gap >= 0.15

    vals = [
        independent.independence_aware_unanimity_confidence,
        mixed.independence_aware_unanimity_confidence,
        shared.independence_aware_unanimity_confidence,
        copies.independence_aware_unanimity_confidence,
    ]
    c2 = vals[0] > vals[1] > vals[2] > vals[3]

    c3_ind_err = abs(
        independent.independence_aware_unanimity_confidence
        - independent.unanimity_accuracy
    )
    c3_copy_err = abs(
        copies.independence_aware_unanimity_confidence - copies.unanimity_accuracy
    )
    c3 = c3_ind_err <= 0.03 and c3_copy_err <= 0.03

    # Reliability-only assumes independence and therefore should give essentially
    # the same confidence to the matched independent and copy unanimous states.
    c4_delta = abs(
        independent.reliability_only_unanimity_confidence
        - copies.reliability_only_unanimity_confidence
    )
    c4 = c4_delta <= 0.02

    return {
        "C1_duplicate_evidence_discrimination": c1,
        "C1_confidence_gap": c1_gap,
        "C2_dependency_ordering": c2,
        "C3_endpoint_calibration": c3,
        "C3_independent_abs_error": c3_ind_err,
        "C3_copies_abs_error": c3_copy_err,
        "C4_reliability_only_insufficiency_visible": c4,
        "C4_reliability_only_endpoint_delta": c4_delta,
        "measurement_pass_C1_to_C4": bool(c1 and c2 and c3 and c4),
        "note_C5": "Rich joint-pattern/Bayes ceiling is intentionally reserved for the authoritative extension; M2 must not be claimed superior to exact Bayes.",
    }


def write_csv(path: Path, summaries: Dict[str, RegimeSummary]) -> None:
    rows = [asdict(summaries[r]) for r in REGIMES]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--p", type=float, default=0.70)
    parser.add_argument("--shared-rho", type=float, default=0.70)
    parser.add_argument("--calibration-trials", type=int, default=100_000)
    parser.add_argument("--test-trials", type=int, default=100_000)
    parser.add_argument("--out-json", type=Path, default=None)
    parser.add_argument("--out-csv", type=Path, default=None)
    args = parser.parse_args()

    if not 0.5 < args.p < 1.0:
        raise SystemExit("--p must be in (0.5, 1.0) for this assay")
    if not 0.0 <= args.shared_rho <= 1.0:
        raise SystemExit("--shared-rho must be in [0,1]")

    rng = np.random.default_rng(args.seed)
    summaries: Dict[str, RegimeSummary] = {}

    for regime in REGIMES:
        y_cal, v_cal = generate_votes(
            rng, args.calibration_trials, args.p, args.shared_rho, regime
        )
        y_test, v_test = generate_votes(
            rng, args.test_trials, args.p, args.shared_rho, regime
        )
        summaries[regime] = summarize_regime(regime, y_cal, v_cal, y_test, v_test)

    criteria = evaluate_preregistered_criteria(summaries)
    payload = {
        "assay": "convergence_signal_synthetic_assay_001",
        "status": "synthetic_reference_run_only",
        "seed": args.seed,
        "p": args.p,
        "shared_rho": args.shared_rho,
        "calibration_trials": args.calibration_trials,
        "test_trials": args.test_trials,
        "regimes": {k: asdict(v) for k, v in summaries.items()},
        "criteria": criteria,
    }

    print(json.dumps(payload, indent=2, sort_keys=True))

    if args.out_json:
        args.out_json.parent.mkdir(parents=True, exist_ok=True)
        args.out_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.out_csv:
        args.out_csv.parent.mkdir(parents=True, exist_ok=True)
        write_csv(args.out_csv, summaries)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
