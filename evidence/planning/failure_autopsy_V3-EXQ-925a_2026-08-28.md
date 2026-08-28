# Failure Autopsy (diagnostic adjudication): V3-EXQ-925a -- F-dominance committed-regime causal harness

**Generated:** 2026-08-28T17:11:55Z | **Scope:** single | **Status:** confirmed (interactive gate 2026-08-28)
**Session:** failure-autopsy-20260828-diagbatch | **Trigger:** `experiment_purpose: "diagnostic"`, clean unflagged PASS, no prior autopsy coverage.
**Run:** `v3_exq_925a_e3_fdominance_committed_regime_causal_harness_20260825T220607Z_v3` (ree-cloud-4, clean substrate 6bd4a990, recording complete, dry-run gate clean, ~6.2h, 7047 fresh events). Supersedes run V3-EXQ-925.
**RE-ADJUDICATION NOTICE:** this artifact PARTIALLY SUPERSEDES `failure_autopsy_V3-EXQ-925_2026-08-12` (read end-to-end per the Step 1 rule before this recommendation was written).

## Facts

Corrected instrument for the H1-H4 causal discrimination about MECH-439's mechanism (claim-free; adjudicates no claim). Changes vs 925: (1) the missing per-step `post_action_update` call added; (2) 2-arm GSCT axis; (3) committed-conditioned re-aggregation; (4) commit-gate scalars recorded (closes 925's recording debt). Everything else verbatim 925.

- committed_fraction = 1.000 in every cell (floor 0.05, a deadlock detector ~20x below the measurement); n_committed = n_total = 7047. Replay validity worst abs err 8.67e-9. All readiness preconditions met; GSCT teff_spread 0.141 (Factor B genuinely active for the first time: argmin-match 0.167 vs ARM_COMMIT's 1.0).
- Red-team verified AT THE 925-ERA COMMIT 9bcde4cb: both GSCT call sites sat inside `elif committed:` -- a dead branch while commitment was deadlocked. `update_running_variance`'s only in-substrate call site is `post_action_update`; the 925 driver never called it, pinning `_running_variance` at precision_init 0.5 > threshold 0.4. Controlled demonstration: authoring-time probe, same substrate, one added call, committed_fraction 0.000 -> 0.959.
- Config identity 925 vs 925a verified (env_kwargs byte-identical; only declared changes differ).

## What is withdrawn vs retained from the 925 autopsy

**Withdrawn:** its Implementation-layer attribution ("GSCT default False is mechanically why commitment never engaged" -- wrong against the substrate as it stood at run time); its H0-as-substrate-property reading; its learning point 2 ("this substrate at default config essentially never engages committed selection"); the premise of its Section 7 candidate MECH-439 note (never applied; GFLAG-0048 blocks it).
**Retained:** its learning point 1 (temporal variance-share vs cross-candidate steering divergence); its biological H3-qualitative reading; its H3-near-miss numbers; its routing (the redesign it called for is 925a itself, correctly executed).
**Read-across:** `mech439_commit_regime_audit_2026-08-12.md` already concluded its literal audit was not runnable -- mechanically unaffected. GFLAG-0048/0049 (both open, verified) are the vehicles for the claim-side and registry-side corrections; recommended H0 re-scope wording is in the JSON `per_claim_recommendation_note`.

## The corrected scientific reading (7c red-team disposition)

Red team **CONTESTED** the draft's retained reading and was right -- the mirror-image trap: ARM_COMMIT's selection was exactly deterministic (`c0_argmin_matches_factual_rate = 1.0`); the entropy-0.9988 softmax is a labelled diagnostic (`last_precommit_probs`) that generated no behaviour. So "near-uniform SELECTION persists" and the manifest's own "NO channel is meaningfully steering the choice" are wrong as stated. What the run shows: **score FLATNESS persists**, and the F-lesion flips the ACTUAL committed winner on 9.7% (ARM_COMMIT) / 19.2% (GSCT) of events (F-scramble 19.2% / 30.4%) -- real argmin-level F authority -- but chance-directionally (frac_toward_safer 0.530 / 0.484). H1-H4 remain undiscriminated on directionless-winner-flip evidence, not tiny-delta evidence. The manifest inherited the conflation (regime-unconditioned note builder; stale "running UNCOMMITTED" driver comment; dangling failure_localisation pointer) -- driver hygiene for any successor.

## Four-layer diagnosis

| Layer | Status |
|---|---|
| Claim alignment | n/a (claim-free) |
| Biological reference | partial -- DDM low-SNR reading retained; flat scores persist committed |
| Prerequisites | present; seed 43 competitor channel ~7e-9 both arms (persistent soft spot) |
| Implementation | complete (instrument corrected; recording debt closed) |
| Environment | adequate |
| Measurement | adequate |
| Integration | coupled; zero uncommitted events -> no within-run regime contrast (by design) |
| Scale | adequate |

GOV-FAILLOC-1: not applicable (PASS). Corollary: H1-H4 remain untested-fairly for a score-scale reason (H5), no longer a commitment reason.

## Adjudication (user-confirmed at the gate)

Self-route label CONFIRMED. `standard` / `non_contributory`. Step 9b applied (Mode B): 925a appended as a resolving run on H1-H4, all four stay alive, basis strings carry the corrected wording; H0 untouched (GFLAG-0049's decision); no growth, no growth_restriction.

## Routing

`queue-experiment` (once governance ratifies): the next discriminating design controls ABSOLUTE SCORE SCALE via channel-scale normalisation (H5's mechanism) -- NOT temperature, which is argmin-invariant and inert on the plain committed path. Governance first applies GFLAG-0048/0049. This autopsy spawns nothing.
