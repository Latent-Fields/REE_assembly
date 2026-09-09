# Assay 004 — Pre-run Sampling Amendment

**Date:** 2026-09-09  
**Status:** preregistration amendment made before authoritative seed `23` was inspected  
**Parent preregistration:** `convergence_signal_synthetic_assay_004_evidence_vs_downstream_leverage.md`

The parent preregistration fixed the candidate sets and criteria but omitted explicit sampling probabilities. Because those probabilities affect aggregate regret, this amendment freezes them before the authoritative run.

## Main assay sampling

Per candidate:

```text
P(evidence topology) = uniform over the five registered topologies

P(q=0.50) = 0.10
P(q=0.65) = 0.25
P(q=0.80) = 0.35
P(q=0.95) = 0.30

P(L=1) = P(L=2) = P(L=4) = P(L=8) = 0.25
```

Topology, query quality, downstream leverage and latent state are sampled independently.

Main assay size remains:

```text
20,000 episodes × 6 candidate queries
```

## Forced anti-conflation diagnostic

Run `20,000` paired episodes.

Both candidates receive the same query quality per episode, sampled uniformly from:

```text
q ∈ {0.65, 0.80, 0.95}
```

Candidate A remains `INDEPENDENT_5, L=1`; candidate B remains `COPIES_5, L=8`.

## Calibration

Dependency calibration uses a separate deterministic synthetic calibration stream, seed `1404`, with `100,000` calibration observations per evidence topology. Calibration labels may be used to estimate marginal reliability and correlation/provenance correction, as in Assays 001–003; test labels remain unavailable to M0–M3 scoring.

No change is made to C1–C5, the authoritative run seed, or the interpretation gates.

This amendment is implementation hygiene only and does not use seed-23 results.