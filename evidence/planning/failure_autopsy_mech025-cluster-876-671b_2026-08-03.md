# Failure Autopsy — MECH-025 / MECH-025b sibling cluster (V3-EXQ-876, V3-EXQ-671b)

**Generated:** 2026-08-03T09:18:08Z
**Scope:** cluster (two sibling claims, same substrate lineage — E3 precision/commitment)
**Status:** confirmed

---

## Why this is a cluster, not two independent targets

MECH-025 ("action mode prioritizes short-horizon, high-precision control via
context-dependent precision modulation") and MECH-025b ("high-precision action
mode carries responsibility attribution") were decomposed from one original
claim on 2026-04-02: MECH-025 keeps the mechanistic precision-modulation core
(Friston 2013 active-inference grounding); MECH-025b is a philosophical bridge
(precision level implies degree of ethical accountability), explicitly *not* a
neuroscience finding per its own claims.yaml notes. Both retests share:

- the same substrate mechanism under test (E3 commitment / `SelectionResult.committed`,
  `E3TrajectorySelector.current_precision = 1/(running_variance+1e-6)`, ARC-016,
  `status: stable`),
- the same historical instrument-defect lineage (wrong commitment field read as
  a cache or a torn-down flag; missing `update_residue()` call freezing
  `running_variance` during eval) — independently discovered and fixed on the
  same day (2026-08-02) for both scripts,
- the same shape of outcome once the instrument was actually fixed: precision/
  commitment itself is unambiguous and huge-magnitude (definitional, via
  ARC-016), but the **downstream functional consequence** each claim predicts
  from that precision separation does not appear.

Both run_ids were checked and are **not** dry-run smokes
(`check_dry_run_citations.py`: 0 dry cited, 2 clean).

---

## Target 1 — V3-EXQ-876 (MECH-025, doing-mode causal signal)

### Facts

- **Manifest**: `v3_exq_876_mech025_doing_mode_causal_signal_20260802T214005Z_v3`,
  5 seeds [42, 123, 7, 99, 256], machine `ree-cloud-2`, `substrate_hash` present.
  `verdict: FAIL`, `evidence_direction: mixed` (26/30 criteria across 5 seeds).
- **Recording gap** (Step 2b): `validate_recording.py` flags `elapsed_seconds`
  and `config` missing from the always-core. Traced to the script itself
  (`experiments/v3_exq_876_mech025_doing_mode_causal_signal.py:1023`):
  `write_flat_manifest(..., config=None, ...)` — the full `REEConfig` built at
  line 589 is available at that point but never passed through. Does not block
  this adjudication (the summary_markdown records the load-bearing
  hyperparameters — breath_period/amplitude/duration, alpha_world — and the
  metrics themselves are complete), but full reproducibility of a redesign
  needs this fixed.
- **Script** (`v3_exq_876_mech025_doing_mode_causal_signal.py`): this is the
  *third* MECH-025 V3 attempt (supersedes V3-EXQ-199 in lineage, not formal
  `supersedes` — different instrument, same claim). Root-caused and fixed all
  three known instrument defects from 050/050b/199 before this run: (1) reads
  `SelectionResult.committed` (the real per-tick BetaGate/E3 outcome), never
  `_committed_candidates` (a stale cache) or `_committed_trajectory` (torn
  down before read); (2) calls `agent.update_residue(...)` every eval tick so
  `running_variance` — what the commit decision is computed from — is live,
  not frozen at its post-training value; (3) BreathOscillator
  (`sweep_threshold_reduction` fed directly into the same `agent.e3.select()`
  call that produces `result.committed`) guarantees periodic genuine
  uncommitted windows.
  - DV: `causal_sig = E3.harm_eval(E2.world_forward(z_world, a_actual)) -
    E3.harm_eval(E2.world_forward(z_world, a_cf))`, `doing_mode_delta =
    mean|causal_sig|_committed - mean|causal_sig|_uncommitted`.
  - C1 (load-bearing): `doing_mode_delta > 0.002`.
  - Positive-control gate: `committed_step_count >= 20` AND
    `uncommitted_step_count >= 20` per seed, plus a `check_degeneracy()` net
    on both sample lists' spread.
- **Queue entry**: `V3-EXQ-876`, `supersedes: V3-EXQ-199`, `experiment_purpose`
  not explicitly re-checked here but the docstring frames this as a direct
  confirmation attempt, not a diagnostic.
- **Observed**: positive-control gate cleared cleanly in every seed
  (committed_step_count 903–9818, uncommitted_step_count 165–216, both far
  above the 20-step floor — this alone is new information: MECH-025 has
  *never* before had a fair sample of both regimes in V3). `check_degeneracy`
  confirms real spread. `doing_mode_delta` is **negative** in 4/5 seeds
  (−0.031, −0.066, −0.081, −0.087) and barely positive in 1/5 (+0.0025,
  seed 256) — i.e. committed/"doing" steps show a *smaller* harm-counterfactual
  contrast than uncommitted steps, the opposite of the predicted direction.
  C4 (world_forward_r2 0.92–0.99) and C5 (harm_pred_std 0.04–0.13) both pass
  comfortably in every seed — the world model and harm evaluator are
  functional; this is not a broken substrate.
  - `precision_committed_mean` (1808–41702) vs `precision_uncommitted_mean`
    (0.04–0.17): a ~10,000–300,000× separation in **every** seed. This is a
    near-tautological consequence of the commit rule itself
    (`committed = running_variance < threshold`, `precision = 1/variance`),
    not fresh evidence — but it is the most direct, unambiguous confirmation
    in this run of the literal words "high-precision control," and it was
    never scored as a criterion.

### Claim-layer map

MECH-025, `status: candidate`, `evidence: None` (verified fresh 2026-08-02 per
the script's own docstring — no V3 confirmation has ever landed before this
run). `depends_on: [ARC-016, ARC-005, ARC-015, ARC-021, INV-012, ARC-044]` —
ARC-016 (dynamic E3 precision) is `stable`/V3-confirmed and is exactly the
mechanism this run's precision separation exercises. The claim text is about
**control precision** ("high-precision control"); the operationalization
tests a **harm-outcome differentiation** proxy (does the counterfactual harm
gap widen). These are not the same quantity, and the gap between them is the
crux of this diagnosis (see below).

### Biological-reference triage

- **Friston et al. 2013** (`targeted_review_connectome_mech_025`, confidence
  0.72, `evidence_direction: supports`) is MECH-025's own primary literature
  grounding — but its own recorded `failure_signatures` state: *"The active
  inference framework treats precision as a property of beliefs about
  policies, not a dedicated action-mode regime — it is continuous, not a
  discrete mode switch."* MECH-025's V3 operationalization is exactly a
  discrete mode switch (committed vs. uncommitted) tested for a categorical
  signature gap — a formal-import mismatch flagged in the corpus's own lit
  entry, not discovered fresh here.
- **Thura & Cisek 2014** (Neuron, `targeted_review_connectome_mech_025`,
  confidence 0.81) is the closer biological reference for the *specific*
  operationalization (committed vs. deliberating): premotor/M1 activity
  **converges** during the deliberation-to-commitment transition — i.e. the
  represented alternatives narrow, not widen, once committed. A converging
  representation predicts a *smaller* counterfactual gap between the actual
  action and an alternative once committed — which is exactly the negative
  `doing_mode_delta` observed in 4/5 seeds.
- Read together, the two lit entries this claim already cites point toward the
  operationalization's predicted *sign* (C1: committed > uncommitted) being
  backwards relative to the closest biological reference, not toward MECH-025
  being false. This is a **biology-divergence / operationalization mismatch**,
  not a substrate ceiling — the substrate (world model, harm evaluator,
  precision/commitment machinery) is all demonstrably functional in this run.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | test let the *mechanism* (precision separation) express itself unambiguously, but the *downstream DV* (harm-counterfactual differentiation) may test the wrong quantity/sign |
| Biological reference | partial | Friston 2013 (this claim's own support) flags precision as continuous not categorical; Thura & Cisek 2014 predicts convergence (narrowing), the opposite of what C1 tests for |
| Developmental / dependency prerequisites | present | ARC-016 stable/confirmed; no other `depends_on` claim blocks this test |
| Implementation completeness | complete | all three known instrument defects (050/050b/199 lineage) fixed and verified this run |
| Environment adequacy | adequate | CausalGridWorldV2 size=6/hazards=4, same tuned env as 199; both regimes well-sampled |
| Measurement adequacy | **under-instrumented / possibly mis-signed** | precision itself (the claim's literal subject) separates unambiguously (4–5 orders of magnitude) but was never scored as a criterion; the scored DV (harm-counterfactual gap, predicted-positive) may have the wrong predicted sign per the literature above |
| Integration adequacy | coupled | E2.world_forward, E3.harm_eval, commitment machinery all interact as designed |
| Scale / capacity | adequate | world_forward_r2 0.92–0.99, harm_pred_std 0.04–0.13 in every seed |
| Recording | gap | `config`/`elapsed_seconds` not recorded (script passes `config=None` to `write_flat_manifest`) — fix in any redesign |

**Recommended `epistemic_category`: `measurement_test_design_defect`.**
**Recommended `evidence_direction`: `non_contributory`** (do not read as claim
pressure against MECH-025 — the operationalization itself is in question).

**User-confirmed routing: re-operationalize.** `/queue-experiment` a redesign
(same-question letter, `V3-EXQ-876a` or similar) that either (a) flips the
predicted sign of C1 per the Thura-Cisek convergence account (predict
`doing_mode_delta < 0`, i.e. commitment *narrows* the counterfactual-harm
contrast) as the primary test, or (b) replaces the harm-counterfactual proxy
with a direct control-precision DV — `precision_committed_mean` vs
`precision_uncommitted_mean` is already recorded and unambiguous but was never
gated as a criterion. Also fix the recording gap (`config=` not `None` in the
`write_flat_manifest` call) so the redesign carries a reproducible always-core.

**Draft `evidence_quality_note` for governance:**

> V3-EXQ-876 (2026-08-02) is the first fair V3 test of MECH-025 — all three
> prior instrument defects (050/050b/199: cache-field/torn-down-field
> commitment read, frozen running_variance during eval) are fixed and
> verified (committed/uncommitted regimes both well-sampled every seed,
> non-degenerate). `doing_mode_delta` is consistently negative (4/5 seeds),
> opposite the predicted sign. This is read as `non_contributory` /
> `measurement_test_design_defect`, not claim pressure: the claim's own cited
> literature (Friston 2013's recorded failure_signature: precision is
> continuous, not a discrete mode switch; Thura & Cisek 2014: PMd/M1
> representations *converge*, not diverge, during commitment) predicts the
> operationalization's sign convention may be backwards. Precision itself
> separates by 4–5 orders of magnitude in every seed (unambiguous, but a
> near-tautological consequence of ARC-016's commit rule, and not currently
> scored as a criterion). Route: /queue-experiment redesign, testing either
> the reversed sign or precision itself as the primary DV.

---

## Target 2 — V3-EXQ-671b (MECH-025b, precision-responsibility)

### Facts

- **Manifest**: `v3_exq_671b_mech025b_precision_responsibility_20260803T022036Z_v3`,
  4 seeds [0, 1, 2, 3]. `verdict: FAIL`, `evidence_direction: mixed` (4/6
  criteria). `supersedes: v3_exq_671a_...` (formal supersession, same
  question). Recording: clean (`validate_recording.py` OK — `config`,
  `elapsed_seconds`, `seeds_used`, `z_goal_stream_stats` all present).
- **Script**: third MECH-025b iteration (671 → 671a → 671b), correcting 671a's
  own confirmed autopsy finding (asymmetric positive-control gap — a gate
  existed on residue accumulation but not on precision variance itself, plus
  671a's single-seed n=29 underpowering). 671b adds a
  `precision_shows_adequate_variance` P0 gate (pooled max–min precision spread
  > 1.0 floor) and per-seed `check_degeneracy` over `precision_samples`, plus
  4-seed pooling.
- **Positive-control gates, both cleared**: `residue_accumulates_under_committed_harm`
  measured 14.76 vs floor 1e-6; `precision_shows_adequate_variance` measured
  160658 vs floor 1. `criteria_non_degenerate` true.
- **Observed** (pooled, n=179 across 4 seeds — though seed 3 contributes only
  n=1 committed step, seeds 0/1/2 contribute 29/72/77 respectively):
  `precision_residue_correlation = -0.0446` (bar: `> 0.15`),
  `high_precision_residue_ratio = 1.0618` (bar: `> 1.1`). Both fail cleanly.
  Per-seed diagnostics (non-gating) show the same near-zero-to-negative
  pattern in every seed with real precision spread (seeds 0/1/2: correlations
  0.0505 / 0.1017 / 0.0651, none clearing 0.15; ratios 0.9214 / 1.1327 /
  1.1471, mixed but centered near 1). C3–C6 (sample size, world model, harm
  evaluator, no fatal errors) all pass comfortably.

### Claim-layer map

MECH-025b, `status: candidate`, `depends_on: [MECH-025, ARC-016, INV-012,
SD-003]`. Its own notes are explicit that this is "a claim about the
RELATIONSHIP between precision and ethical accountability... a philosophical
bridge, not a neuroscience finding." Unlike a MECH-025-dependent test, 671b's
design does **not** require MECH-025's causal-signature claim to hold — it
correlates E3's own `result.precision` (definitionally live per ARC-016,
`stable`) directly against `ResidueField.total_residue` accumulation (cleared
its own positive control). So this is a fair, self-contained test of the
bridge claim on its own terms, independent of Target 1's unresolved
operationalization question.

### Biological-reference triage

No direct biological mechanism exists to check against — MECH-025b is
explicitly a philosophical construct (precision-implies-accountability),
not a translated neuroscience finding. The two MECH-025b-tagged lit entries
(Caspar 2021 coercion/responsibility, Kahane 2012 dual-process critique) are
about human moral-responsibility judgments, not about a neural
precision-to-residue-weighting mechanism, so they cannot arbitrate this
result either way. This is the one target in the cluster where the
"biology as existence proof" move does not apply — there is no working
biological mechanism this claim translates, by its own design.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened | first fair, self-contained test; both preconditions the prior autopsy (671a) flagged as missing are now gated and cleared |
| Biological reference | absent (by design) | philosophical bridge, not a neuroscience finding — no mechanism to fall back on |
| Developmental / dependency prerequisites | present | ARC-016 stable; residue accumulation confirmed live this run |
| Implementation completeness | complete | both known gaps from 671/671a fixed and verified |
| Environment adequacy | adequate | same tuned env as sibling lineage |
| Measurement adequacy | adequate, modest power | pooled n=179 but seed-3 contributes only n=1; 3 of 4 seeds carry the real signal |
| Integration adequacy | coupled | precision/commitment + residue accumulation both live and interacting |
| Scale / capacity | adequate | WF R2 0.93–0.98, harm_std 0.05–0.15 |

**Recommended `epistemic_category`: `standard`.**
**Recommended `evidence_direction`: `weakens`** (against MECH-025b
specifically — this result says nothing about MECH-025 itself).

**User-confirmed routing: weakens, note only — no demotion this cycle.** Single
well-powered result; record the finding in `claims.yaml` but do not
recommend a status change yet (highest-threshold caution for demotion, and
the claim's own philosophical-bridge framing means this null is expected to
need more than one confirmation before real claim pressure is asserted).

**Draft `evidence_quality_note` for governance:**

> V3-EXQ-671b (2026-08-03) is the first fair, fully-gated test of MECH-025b.
> Both positive-control gates (residue accumulation, precision variance)
> clear cleanly; the correlation the claim predicts
> (`precision_residue_correlation > 0.15`) reads -0.0446, and the ratio test
> (`> 1.1`) reads 1.0618 — both null, consistently across the 3 seeds with
> real committed-step spread. Unlike MECH-025 (Target 1, same cluster), this
> test does not depend on MECH-025's own operationalization succeeding — it
> correlates E3's own precision value directly against residue accumulation,
> both independently confirmed live this run. Read as `weakens` /
> `standard` — real claim pressure against the precision-implies-
> accountability bridge specifically. No biological reference exists to
> check this against (the claim is explicitly a philosophical construct, not
> a translated neuroscience finding, per its own 2026-04-02 decomposition
> note). No demotion recommended this cycle — single result, and pooled n is
> modest (179, unevenly distributed across seeds).

---

## Cluster pattern

| Experiment | Claim | Negative-control / absolute criterion | Discrimination criterion | Read |
|---|---|---|---|---|
| V3-EXQ-876 | MECH-025 | C2–C6 all pass (committed/uncommitted well-sampled, world model + harm evaluator functional) | C1 (doing_mode_delta > 0.002): FAILs, wrong sign, 4/5 seeds | operationalization/sign mismatch, not substrate failure |
| V3-EXQ-671b | MECH-025b | C3–C6 all pass (sample size, world model, harm evaluator, no errors) | C1 (correlation) + C2 (ratio): FAIL, near-zero/null | genuine null on the bridge mechanism |

**Reading: one shared structural property, not two independent bugs.** Both
targets now have a fully instrument-clean measurement of E3
precision/commitment (ARC-016's confirmed mechanism), and in both cases the
precision/commitment signal is unambiguous while the **downstream functional
consequence each sibling claim predicts from it fails to appear** — for
different specific reasons (876: the predicted *direction* may be backwards
per the claim's own cited literature; 671b: no correlation at all, even
allowing either sign). The shared structural fact is: **precision separation
is real and large, but neither of the two hypothesized functional readouts
built on top of it (harm-differentiation signature, responsibility-residue
weighting) has yet been shown to track it.** This is not evidence the
precision mechanism (ARC-016) is wrong — it is evidence that the two
higher-level claims layered on top of it need re-examination independently:
876's DV/sign, and 671b's bridge-claim status itself.

**Granularity-debt recurrence trigger**: checked via
`granularity_debt_cluster.py` for both claims. MECH-025: 0 prior tagging
targets — this is its first-ever confirmed autopsy, trigger does not apply.
MECH-025b: 2 prior tagging targets (671: `intact`/degenerate-not-tested;
671a: `unclear`/measurement_gap), neither reads `weakened` before this
autopsy — trigger did not fire going in. This autopsy's own 671b target now
reads `weakened` for the first time, but that is 1 of 3 targets, not (yet) a
recurrent pattern with structurally differing failure signatures — **does
not fire** the granularity-debt trigger. Flagging for a future session: if a
follow-up MECH-025b test also weakens, re-run this check.

**Re-derive brake**: MECH-025 0 prior `substrate_ceiling` hits (does not
fire; this run itself is not stamped `substrate_ceiling` either).
MECH-025b 0 prior `substrate_ceiling` hits across its 2 prior targets
(`measurement_gap`, degenerate) — does not fire; this run is `standard`,
not `substrate_ceiling`.

**Fan-out / hypothesis-space ledger (Step 9b)**: no pre-existing
`hypothesis_space_registry.v1.json` question names MECH-025 or MECH-025b, and
neither target here emits a `fanout_recommendation` (876's redesign is a
single well-specified re-operationalization, not a ≥2-live-hypothesis
discrimination portfolio; 671b's routing is a note, not a re-queue). Step 9b
skipped cleanly per its own applicability condition.

**Recording-standard gap (876 only)**: flagged above — `config=None` passed
to `write_flat_manifest` in `v3_exq_876_mech025_doing_mode_causal_signal.py`.
Worth a one-line fix (`config=config`) whenever this script is next touched
for the redesign.

---

## Follow-on (reported inline, not chipped — `/failure-autopsy` work-type per Session Land Protocol)

- `/queue-experiment` V3-EXQ-876a (or next letter): MECH-025 redesign per the
  routing above (sign-flip and/or precision-as-DV), fixing the `config=None`
  recording gap in the same pass.
- `/governance`: apply both `evidence_quality_note`s above; no `claims.yaml`
  status changes recommended by this autopsy for either claim.
