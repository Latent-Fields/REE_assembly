# Failure Autopsy: V3-EXQ-878 (MECH-332, efference-copy vs AIC dissociation)

**Generated:** 2026-08-03T10:35:00Z
**Scope:** single
**Status:** confirmed (user-confirmed at Step 8 gate, 2026-08-03)

---

## 1. Facts reconstruction

**Run:** `v3_exq_878_mech332_efference_aic_dissociation_20260803T023041Z_v3`
**Queue ID:** V3-EXQ-878 (`experiment_purpose: evidence`, `backlog_id: EVB-0268`)
**Claim:** MECH-332 only.
**Outcome:** FAIL. `non_degenerate: false`. `evidence_direction: non_contributory`.
**Self-route label:** `substrate_not_ready_requeue`.
**Dry-run check:** confirmed real (`dry_run: false`), not a smoke.

MECH-332 asserts nociceptive attenuation on `z_harm_s` is produced by two
mechanistically independent pathways:

- **Pathway 1** (per-step efference-copy comparator, MECH-256/SD-029):
  `residual = z_harm_s_observed - E2_harm_s(z_harm_s_{t-1}, a_actual)`.
  Substrate: `ree_core/predictors/e2_harm_s.py` (`E2HarmSForward`, ARC-033),
  gated on `use_e2_harm_s_forward`.
- **Pathway 2** (commitment-gated PAG/RVM descending suppression, SD-021,
  now subsumed by SD-032c): `harm_s_gain = f(operating_mode, drive) < 1.0`
  **when committed**. Substrate: `ree_core/cingulate/aic_analog.py`
  (`AICAnalog`), gated on `use_aic_analog` + `harm_descending_mod_enabled`.
  Its own docstring: "subsumes SD-021 descending pain modulation." The
  claim's own text is explicit that this pathway's trigger is **E3
  commitment state (beta_gate elevated, trajectory through expected harm)**
  — commitment is not incidental to this pathway, it is the precondition
  the claim itself names.

Design: 2x2 factorial (ARM_BOTH / ARM_E2_ONLY / ARM_AIC_ONLY / ARM_NEITHER)
x 3 seeds (42, 7, 13), on the SD-022 body-damage arena (`limb_damage_enabled`)
+ SD-029 balanced-event curriculum (EXQ-479 calibrated params), with
`HeartbeatConfig(beta_gate_bistable=True)` for the E3 commitment substrate.
D1/D2/D3 dissociation predictions pre-registered; non-degeneracy gated on
(a) `n_committed_steps >= 8` in ARM_AIC_ONLY and ARM_BOTH, (b) both event
types (`agent_caused_hazard`, `env_caused_hazard`) reaching >= 6 trials in
ARM_E2_ONLY and ARM_BOTH.

**What actually happened, per seed** (`analysis.per_seed`):

| Seed | d1_pass | d2_pass | d3_pass | n_committed (AIC_ONLY / BOTH) | n_agent/env trials (E2_ONLY / BOTH) |
|---|---|---|---|---|---|
| 7  | false | true | true | 0 / 0 | 12/12 |
| 13 | false | true | true | 0 / 0 | 0/12 (agent_caused) |
| 42 | false | true | true | 0 / 0 | 12/12 |

`n_committed_ok` fails on **every seed, in both AIC-active arms** (floor=8,
actual=0). This alone forces `seed_non_degenerate=false` for all 3 seeds,
which forces `overall_non_degenerate=false`, which is what the driver's own
decision tree correctly routes to `substrate_not_ready_requeue` /
`non_contributory` — **before** D1/D2/D3 are ever used as a verdict.

**A second, latent finding inside the same data:** `z_harm_s_ratio` is
computed as `mean(z_committed)/mean(z_uncommitted)` **only if both lists are
non-empty; otherwise it silently defaults to `1.0`** (`eval_arm`,
`v3_exq_878...py:559-562`). With zero committed samples, `ratio_both`,
`ratio_aic_only`, and `ratio_neither` are **all exactly 1.0** for every seed
— not a measured "no attenuation," but an unconditional fallback constant.
This is what mechanically drives `d1_pass=false` in every seed (the three
identical 1.0s trivially satisfy "near-equal" but trivially fail
"attenuation below `ratio_neither - 0.03`"). **This fallback never reaches
the evidence_direction verdict** because the non-degeneracy gate already
catches the same zero-commitment condition first and short-circuits to
`non_contributory` — so it is a measurement-hygiene wrinkle, not a live bug,
but worth flagging: a `NaN`/`None` sentinel would make a future gate-bypass
(e.g., a threshold change that lowers `N_COMMITTED_FLOOR`) fail loudly
instead of silently reporting spurious "no attenuation."

**Pathway 1 (D2) is a genuine, clean positive result inside the overall
FAIL**: `d2_pass=true` in all 3 seeds — the efference-copy comparator
dissociates correctly (near-equal self/other discrimination with/without
AIC active, both clearing the 1.15 discrimination floor) whenever its own
non-degeneracy condition (event-trial counts) is met.

---

## 2. Claim-layer mapping

**MECH-332**: `status: candidate`, `v3_pending: true`,
`implementation_phase: v3`, `depends_on: [MECH-256, SD-021, SD-011, SD-029]`.
Registered 2026-05-17. Held `hold_pending_v3_substrate/applied` since
2026-05-19T21:27:25Z. **This is the first experiment ever run against this
claim** — zero prior autopsies, zero prior evidence
(`genuine_exp_count: 0`, `experimental_confidence: 0.0` per
`claim_evidence.v1.json`, one literature-only entry, `lit_conf: 0.739`).

**The v3_pending gate is stale.** It predates (or never incorporated) the
fact that both pathway substrates now demonstrably exist and are
independently wireable via config flags — confirmed by direct code
inspection this run (`agent.py`'s `_update_scientist_attribution` "Self
domain — ARC-033 E2HarmSForward" block for Pathway 1; the "SD-021:
descending pain modulation" block multiplying `z_harm` by `aic.harm_s_gain`
for Pathway 2). The driver's own `custom_information.v3_pending_gate_stale_note`
flags this; **user-confirmed 2026-08-03 to recommend governance lift it** as
a companion action, independent of this run's own disposition.

**Did the experiment let the claim express itself?** Only partially.
Pathway 1's leg (D2) got a valid, non-degenerate test and passed. Pathway
2's leg (D1) never got a valid test at all — its trigger condition
(sustained E3 commitment) never occurred in the eval window, so the claim's
Pathway-2 prediction is **untested**, not weakened, by this run.

---

## 3. Biological-reference triage

MECH-332's biological grounding is solid and specific, not a
formal-definition import:

- **Pathway 1**: Wolpert/Kawato efference-copy forward-model attenuation
  (corollary discharge cancels self-predicted sensory consequences),
  localized to spinal dorsal horn / S1-insula forward-model subtraction.
  Directly analogous to Blakemore/Shergill self-touch attenuation
  paradigms already cited elsewhere in this claim family (MECH-136).
- **Pathway 2**: pgACC -> PAG -> RVM descending inhibitory circuit,
  contextual behavioral-state gating (De Preter & Heinricher 2024) —
  explicitly triggered by a **sustained committed approach/traversal of
  expected harm**, not by any single action.

The observed failure does **not** resemble a biological absence of PAG/RVM
modulation. It resembles what would happen if you tried to measure
descending pain modulation in an animal that **never commits to a sustained
threat-approach trajectory in the first place** — the modulatory mechanism
cannot be observed because the precipitating behavioral state (sustained
commitment near expected harm) never arises. That is a missing-precondition
signature, not a mechanism-absent signature: the biology is consistent with
the claim; the **test's own behavioral precondition** (E3/BetaGate
commitment) did not arise within this schedule/arena, in an experiment that
had never previously been run and so had no calibrated precedent for how
much exposure this specific 8x8/limb-damage arena needs before E3 commits.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | untested (Pathway 2) / intact (Pathway 1) | Pathway 1's D2 got a valid test and passed cleanly in 3/3 seeds; Pathway 2's D1 never got a valid test — its trigger (sustained commitment) never occurred. |
| Biological reference | clear | Wolpert efference-copy (Pathway 1) + PAG/RVM descending modulation triggered by committed threat-approach (Pathway 2), both directly cited, non-formal. |
| Developmental / dependency prerequisites | present but not engaged (Pathway 2) | MECH-090 (BetaGate commit-entry) and MECH-342 (commitment-release coupling) are both `implemented`/`implemented_validated` in `substrate_queue.json` — the dependency exists and works elsewhere; it simply didn't fire in THIS arena/schedule. |
| Implementation completeness | complete | Both pathway modules exist, are independently wireable via config flags, code-verified fresh against `agent.py` this run (not inherited from a prior assumption). |
| Environment adequacy | likely inadequate | 8x8 grid, 2 hazards, 3 resources, 150 steps/episode, only 50 eval episodes; first-of-lineage — no prior calibration exists for how much exposure this specific arena needs before E3 reliably commits. |
| Measurement adequacy | adequate for Pathway 1; latent hygiene issue for Pathway 2 | `z_harm_s_ratio`'s silent 1.0-fallback-on-empty-data is currently harmless (screened by the non-degeneracy gate) but should emit `NaN`/`None` for future audit safety. |
| Integration adequacy | not exercised | Cannot assess pathway-interaction (D3) — Pathway 2 never fired, so independence-under-co-activity is untested. |
| Scale / capacity | likely insufficient | P0+P1 = 180 training episodes may be below the competence/exposure level needed for E3 to sustain a committed trajectory near threat in this arena (consistent with the project's broader MECH-457 cold-start/competence-floor precedent). |

**Dominant diagnosis: environment/schedule calibration gap (test-design), not
a substrate gap, not a claim-layer verdict, not a biology divergence.** The
mechanism this test needs (E3 commitment engaging under threat-approach) is
built and validated elsewhere; this specific arena+schedule combination, on
its first outing, simply didn't produce it.

---

## 5. Learning extracted

1. **New dependency made explicit**: MECH-332's Pathway-2 test has a
   claim-intrinsic precondition (sustained E3 commitment via BetaGate) that
   is not guaranteed by `beta_gate_bistable=True` alone — it needs
   arena/schedule calibration tuned to produce sustained committed
   threat-approach, which this first-of-lineage run did not yet have.
2. **Existing dependency partially confirmed (positive, buried in an
   overall FAIL)**: Pathway 1 (efference-copy comparator) is fully
   functional and cleanly dissociable — D2 passes in all 3 seeds whenever
   its own non-degeneracy condition is met.
3. **Latent measurement-hygiene gap (non-blocking)**: `z_harm_s_ratio`'s
   silent 1.0 fallback on empty committed-sample data should be hardened to
   `NaN`/`None` so a future threshold change can't silently launder a
   zero-commitment run into a false "no attenuation" reading.
4. **Recording note**: claims.yaml's `v3_pending`/`hold_pending_v3_substrate`
   gate (2026-05-19) is stale relative to the now-confirmed substrate
   mapping; recommend governance lift it as a companion action
   (user-confirmed).

**Work-graph classification**: `complex (probe-gated) / puzzle (known
rules)` — the mechanism (BetaGate/E3 commitment) is built; what is missing
is the empirical fact of what schedule/arena calibration reliably produces
it here. Re-derive brake: 0 prior autopsies tag MECH-332 (fresh claim) —
does not fire. No granularity-debt cluster (single data point).

---

## 6. Repair pathway (user-confirmed 2026-08-03)

**Routing: `/queue-experiment`**, same-question lettered re-run
(V3-EXQ-878a), NOT `/implement-substrate` (both pathway modules already
implemented and wired) and NOT a claim-layer verdict (untested, not
falsified).

Recommended redesign spec for V3-EXQ-878a:
- **Calibration pilot first**: before repeating the full 3-seed 2x2
  dissociation, run a smaller sweep (training budget / eval episode count
  / arena richness) that watches `n_committed_steps` as its own pass/fail
  gate, to find a schedule that reliably clears `N_COMMITTED_FLOOR=8` in
  ARM_AIC_ONLY and ARM_BOTH. Reuse any already-calibrated commitment-
  inducing schedule from the MECH-090/MECH-342 validation lineage if one
  exists on a compatible arena.
- **Harden the measurement wrinkle**: change `z_harm_s_ratio`'s empty-data
  fallback from `1.0` to `NaN`/`None`, so a future gate change fails loudly
  rather than silently reporting a spurious "no attenuation."
- Pathway 1's D2 result does not need re-testing — it is already valid,
  clean, and consistent across all 3 seeds; a re-run should preserve
  `ARM_E2_ONLY`/`ARM_BOTH`'s current schedule for that leg and vary only
  what's needed to get Pathway 2 committing.

**Companion governance action (user-confirmed)**: recommend lifting
MECH-332's `v3_pending` gate — the substrate mapping (E2HarmSForward/
ARC-033 for Pathway 1, AICAnalog/SD-032c for Pathway 2) is now confirmed
implemented and wireable, independent of this run's own disposition.

**Draft `evidence_quality_note`** (for governance to apply verbatim or
adapt):

> [2026-08-03, V3-EXQ-878, confirmed failure_autopsy_V3-EXQ-878_2026-08-03]:
> First experiment against this claim. FAIL via self-route
> `substrate_not_ready_requeue` (non_degenerate=false): E3's commitment gate
> (BetaGate/MECH-090) never elevated during eval in either AIC-active arm
> across all 3 seeds (n_committed_steps=0 vs floor=8), so Pathway 2's
> claim-intrinsic trigger (sustained committed threat-approach) never
> occurred — Pathway 2 (SD-021/AICAnalog descending modulation) remains
> UNTESTED, not falsified. Pathway 1 (efference-copy comparator,
> MECH-256/SD-029) DID get a valid test and passed cleanly (D2, 3/3 seeds).
> non_contributory; PROMOTES/DEMOTES NOTHING. Routed
> `/queue-experiment` V3-EXQ-878a: calibration pilot to find a
> schedule/arena exposure that reliably produces sustained E3 commitment in
> this arena, before repeating the full dissociation. Companion action:
> `v3_pending`/`hold_pending_v3_substrate` (2026-05-19) is stale — both
> pathway substrates are confirmed implemented and wireable; recommend
> lifting.
