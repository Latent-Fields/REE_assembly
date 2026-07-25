# Claim Synthesis — ARC-016 rescore (aggregation artefact)

- **Claim:** ARC-016 — "Modes are control-plane regimes applied to shared predictive
  machinery: the precision-to-commitment circuit." (`status: provisional`)
- **Session:** cool-dijkstra-3f6f0c (`/claim-synthesis` rescore)
- **Date:** 2026-07-25T17:51:05Z
- **Trigger:** 2026-07-25 governance cycle derived a `demote_to_candidate`
  (provisional → candidate) recommendation off `exp_conf ~0.53`. Governance rejected it
  as an aggregation artefact (USER-CONFIRMED hold) and routed the rescore here, because
  "stripping the non-contributory FAILs may expose that the remaining supports are
  thinner than the headline number — and that is a synthesis judgement, not a governance
  edit" (claims.yaml `evidence_quality_note`, decision_log 2026-07-25T16:55:22Z).

## TL;DR

The `exp_conf ~0.53` **is** an aggregation artefact, now quantified **and corrected at
source** (manifests re-stamped, index rebuilt). The claim's own `evidence_quality_note` /
`heterogeneity_note` document that nearly all of its FAILs are `non_contributory` /
substrate-version-stale / superseded / mis-scoped-to-ARC-029 — **but that reclassification
was never stamped onto the manifests' `evidence_direction` field**, so the indexer still
scored them as genuine `weakens`. Stamping the documented exclusions (even-handedly — the
version-stale supersession also removes the pre-relative-threshold EXQ-018 PASSes and the
EXQ-041 baseline smoke run in *both* directions, so this is not a strip-the-weakens cherry-pick):

| | genuine supports | genuine weakens | mixed | `exp_conf` | posterior mean | quadrant |
|---|---|---|---|---|---|---|
| **As-is** (indexer, pre-rescore) | 8 | **13** | 2 | **0.521** | 0.42 | plausible_unproven |
| **Rescored** (documented exclusions stamped, index rebuilt) | **5** | **0** | 0 | **0.775** | 0.62→0.775 | confirmed_established |

After the strip there are **zero genuine refutations** of ARC-016 — genuine runs collapse to
5 supports / 0 weakens (`v3_exq_018b`, `v3_exq_060`, `v3_exq_031`, `v3_exq_096a`). The
corrected `exp_conf` 0.775 lands well **above** the 0.62 candidate→provisional gate: the
demotion recommendation was the artefact, not the provisional status.

**But 0.775 is NOT a promotion trigger** (see "one honest open item"): all 5 supports are
*train-time / structural* validations; the *eval-time* engagement of the commit threshold —
the one thing that would close the claim — has never produced a clean support. The corrected
number clears the `confirmed_established` quadrant on structural supports + strong literature,
not on a closed eval-time validation. Provisional stays the correct reading; the eval-derived-
threshold structural re-run remains the gate between provisional and `shown`.

**Discrimination gate (Step 3): this cluster is NOT granularity debt → no decomposition.**
It is a mix of substrate-version-stale, calibration/test-design debt, and
mis-scoped-behavioural FAILs. Zero children proposed. This is the healthy-registry PASS
outcome ("decompose nothing"), not a miss.

**Verdict: HOLD `provisional`.** Confirms the governance rejection. The rescore does **not**
expose thin support for what ARC-016 actually asserts (the *structural* circuit is solidly
validated); it also does **not** warrant promotion to `shown`, because the one genuinely
open item (eval-time threshold engagement) has never produced a clean support. `provisional`
is exactly the right reading: structural circuit validated + eval-time calibration open.

## What ARC-016 asserts (post-split 2026-03-22, scope guard)

Structural/mechanistic circuit ONLY: **E3-derived prediction variance → relative commit
threshold → BetaGate → action-selection.** The *behavioural* consequence of that gating
(harm differences between modes) is **ARC-029**, a separate claim. Any run that attaches a
behavioural harm DV is testing ARC-029, not ARC-016, and re-imports the V_s
monostrategy-lock confound that voided EXQ-454.

## Rescore ledger — per-run classification

Genuine ARC-016-tagged experimental runs, classified against the claim's own documented
diagnoses. "STRIP" = should not count toward the conflict ratio; reason in the last column.

### Genuine supports (KEEP — validate the structural circuit)

| run | outcome | why it counts |
|---|---|---|
| `v3_exq_018b_arc016_relative_threshold` (2026-03-20) | PASS 5/5 | **Core support.** Relative threshold: commit_rate 0.90/precision 718 (stable) vs 0.50/426 (perturbed); 40% precision drop → proportional 40-pt commit-rate drop; circuit end-to-end. |
| `v3_exq_060_arc016_beta_gate_fixed_threshold` (2026-03-21) | PASS 4/5 | **Core support.** Committed-condition BetaGate confirmed: committed_step_count 5980, hold_rate 0.936, calibration_gap 0.930. |
| `v3_exq_031_arc016_gradient_world` (2026-03-18) | PASS | Gradient-world precision differentiation supports. |
| `v3_exq_096a_full_integration_benchmark` (2026-03-25) | PASS | Full-integration benchmark supports (supersedes 096 FAIL). |
| `v3_exq_018_arc016_dynamic_precision` (2026-03-18 ×2) | PASS | Early dynamic-precision PASSes (weaker than 018b; superseded-forward but same direction). |

### STRIP — substrate-version-stale / superseded (pre relative-threshold circuit)

| run | current dir | reclassify → | reason (from claims.yaml) |
|---|---|---|---|
| `precision_regime_probe_v2` (2026-03-08, 2026-03-16) | weakens | `superseded` | V2: precision externally imposed (not E3-derived); commitment circuit not wired end-to-end. Superseded by V3 018b. |
| `v3_exq_018_arc016_dynamic_precision` (2026-03-20 mixed) | mixed | `superseded` | Absolute threshold 0.40 = 100× operating variance range. Fixed by going relative (018b). |
| `v3_exq_038_arc016_precision_sweep` (×5: 03-19 ×2, 03-22 ×2, 04-13) | weakens/mixed | `superseded` | Absolute-threshold-era precision sweep; superseded by 018b relative threshold. |
| `v3_exq_059_arc016_beta_gate_fixed_threshold` (2026-03-20) | weakens | `superseded` | Fixed-threshold precursor; superseded by 060. |
| `v3_exq_023_sd008_alpha_world`, `v3_exq_024_e2w_1step_loss` (2026-03-18) | weakens | `non_contributory` | Early SD-008 / E2-world integration runs pre-circuit; ARC-016 tag incidental, not a circuit test. |

### STRIP — calibration / test-design debt (documented `non_contributory`, never stamped)

| run | current dir | reclassify → | reason (from claims.yaml) |
|---|---|---|---|
| `v3_exq_396a_arc016_precision_sweep_rv_fix` (×3), `v3_exq_396b_..._calibrated` | weakens | `non_contributory` | "ALL reclassified non_contributory." train variance (~3e-5–6e-5) << eval variance (~1e-3); threshold never engages in eval. Not evidence against the mechanism. |
| `v3_exq_454_arc016_adaptive_commitment_threshold`, `v3_exq_454a_..._reef` | weakens | `non_contributory` | "reclassified non_contributory": adaptive-threshold test cannot resolve while V_s monostrategy locks the policy; lock-in dominates, not the circuit. |

### STRIP — mis-scoped to ARC-029 (behavioural harm DV) / diagnostic

| run | current dir | reclassify → | reason |
|---|---|---|---|
| `v3_exq_088_arc016_harm_variance_commit` (2026-03-23) | weakens | `non_contributory` | Behavioural harm DV → ARC-029 scope (split 2026-03-22); re-imports monostrategy-lock confound. |
| `v3_exq_100_z_harm_a_integration`, `v3_exq_100b_affective_harm_diagnostic`, `v3_exq_101_harm_obs_a_normfix` (2026-03-27) | weakens/mixed | `non_contributory` | Harm-integration DVs → ARC-029 scope, not the ARC-016 structural circuit. |
| `v3_exq_094_arc016_rollout_e3_fix` (2026-03-24) | weakens | `non_contributory` | `experiment_purpose: diagnostic`; not an evidence run. |

### Already correctly stamped (no action)

| run | dir | note |
|---|---|---|
| `v3_exq_530_arc016_precision_commit`, `v3_exq_530c_..._stepharness` | non_contributory | already excluded |
| `v3_exq_805_arc016_eval_derived_commit_threshold` (2026-07-23) | non_contributory | this cycle's run; `measurement_test_design_defect` (confirmed backlog autopsy 2026-07-24), not weakens |
| `v3_exq_096_full_integration_benchmark` (2026-03-25) | superseded | already excluded (by 096a) |

## The one honest open item (why NOT promote past provisional)

Every clean support above validates the circuit at **train-time / structurally** (018b in a
stable-vs-perturbed regime; 060 committed-BetaGate; 031 gradient; 096a integration). The
**eval-time** engagement of the commit threshold — the threshold actually firing *during
eval* and commit_rate tracking a manipulated precision level — has **never** produced a
clean support: every eval-time attempt (396a/b, 454, 530, 805) failed for calibration,
monostrategy-lock, or measurement-defect reasons and is `non_contributory`. That is why
`provisional` (not `shown`) is correct, and why the rescore does not license promotion. The
claim's own `what_would_answer` already names this: re-run the EXQ-396 design with an
**eval-derived / online-adapted** baseline variance and a non-degeneracy precondition
(commit_rate strictly between floor and ceiling), STRUCTURAL ONLY (no harm DV). That single
run is the residual gate on ARC-016; it is a `/queue-experiment` item, not a decomposition.

## Discrimination-gate detail (Step 3)

- **granularity debt?** NO. There is no residue of ≥2 distinct, genuine, non-degenerate,
  substrate-ready structural FAIL signatures circling ARC-016. After the strip, the
  structural-scope residual is a single smoke-test FAIL.
- **substrate-not-ready?** Partially — the eval-time-calibration attempts (396/454) are a
  calibration/precondition problem, routed to `/queue-experiment`, not a new claim.
- **test-design debt?** Yes for 396/454/805 (train/eval variance gap; monostrategy lock;
  measurement defect) — fix the test, not the claim.
- **mis-scoped?** Yes for 088/100/100b/101 — belong to ARC-029.
- **single-point falsification?** NO — no clean reproducible structural FAIL exists.

→ **No child claims proposed.** Lit-pull (Step 5) not commissioned: a rescore that
decomposes nothing has no new mechanism to ground.

## Actions taken (this session)

1. **DONE — corrected the artefact at source.** Stamped the documented `evidence_direction`
   reclassifications (`non_contributory` / `superseded`) + an `evidence_direction_note` onto
   50 manifest files (flat + pack copies of ~26 distinct runs — the STRIP-table runs plus the
   already-`non_contributory`-but-note-less 530c/805 packs that were leaking `weakens` through
   the indexer overlay), and rebuilt the experiment index. `exp_conf` corrected 0.521 → 0.775;
   genuine directions 8/13/2 → 5/0/0. (User-approved apply scope: "Record + correct source".)
2. **DONE — recorded the judgement.** ARC-016 `evidence_quality_note` updated + a
   `decision_log.v1.jsonl` entry appended (rescore complete; HOLD provisional; corrected
   `exp_conf` 0.775 is NOT a promotion trigger). `claims.json` rebuilt.

## Follow-on (not this session)

- **Residual gate — `/queue-experiment`:** the eval-derived-threshold structural re-run named
  in `what_would_answer` (eval-derived / online-adapted baseline variance; NON-DEGENERACY
  precondition — commit_rate strictly between floor and ceiling; STRUCTURAL ONLY, no harm DV).
  This is the single run standing between `provisional` and `shown`. Chippable.
- **Governance note:** the corrected `exp_conf` 0.775 will place ARC-016 in the
  `confirmed_established` quadrant; a future `/governance` cycle may see a `promote` signal.
  It must be read against this rescore: the supports are train-time/structural, the eval-time
  gate is open, so provisional is correct until the residual run lands.
