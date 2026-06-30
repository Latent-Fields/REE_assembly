---
title: "MECH-451: Intermediate finer-channel-granularity selection-gating"
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 13
---

# MECH-451: Intermediate finer-channel-granularity selection-gating

**Claim ID:** MECH-451
**Subject:** selection.intermediate_channel_granularity
**Status:** IMPLEMENTED 2026-06-24 (substrate; candidate / substrate_conditional / v3 — PROMOTES NOTHING until EXP-0391 scores)
**Registered:** 2026-06-23
**Depends on (built, V3-frozen):** ARC-108 (learned per-channel `w_chan` + signed-RPE three-factor rule), MECH-450 (recurrent settling step — *not* required by this slice; W_lat OFF), MECH-439 (the F-dominance conversion ceiling under test), ARC-106 (brain-like construction framework)
**Sequenced BEFORE:** ARC-110 / `v4_loop_segregation` (the expensive V4 full per-loop build — MECH-451 must be exhausted first; a PASS pre-empts it)
**Routing source:** `evidence/planning/failure_autopsy_V3-EXQ-700b_2026-06-24.{md,json}` (the V3-EXQ-700 lineage could not validly test learned-gating conversion on the single arena; the V4 escalation + this cheap V3 rung were opened concurrently)

---

## Problem

The committed-action-diversity **conversion ceiling** (MECH-439): the primary harm/goal
score **F monopolises ~88-89% of E3 committed-selection variance** (V3-EXQ-571), unmoved by
the full diversity stack. ARC-108 added the first LEARNING afferent to the ARC-107
arbitration layer — a single global learned weight `w_chan` over the modulatory channels
feeding the E3 `_modulatory_accum` composition site. But at that site **`score_bias` is
already the COMPRESSED dACC+lPFC+OFC+MECH-295+MECH-320+gated_policy blend, summed UPSTREAM in
`agent.py` before it reaches `select()`** (the ARC-108 comment names a "finer per-head
channel split" as the documented follow-on, out of step-1 scope). A learner that can only
re-weight a pre-compressed blend cannot dissociate the control functions compression fused —
it cannot learn that OFC devaluation should matter in one state while dACC conflict should
dominate in another.

## Solution

Expose the compressed `score_bias` channel as several **separately-learnable finer
channels**, each with its OWN learned `w_chan_finer` entry trained by the SAME ARC-108
signed-RPE three-factor rule, keeping **ONE shared arena** (NOT ARC-110 per-loop
competition). This is the cheap V3 rung BETWEEN ARC-108's one global weight vector and
ARC-110's full segregated loops.

### What this tests (the falsifier, EXP-0391)

- **A2_FINER lifts committed-action-class entropy strict-above BOTH A0_ENVELOPE_ONLY AND
  A1_GLOBAL_WCHAN (and a verified-lifting noise control), converting >=1 previously-F-dominated
  non-motor function** ⇒ the conversion ceiling is **REPRESENTATIONAL COMPRESSION**, and the V4
  ARC-110 loop build is **pre-empted**.
- **Finer channels move their weights but produce no lift beyond A1_GLOBAL_WCHAN** ⇒ compression
  is NOT the binding constraint; **positive evidence FOR ARC-110** (full per-loop competition
  implicated) — NOT evidence against ARC-108.

### Implementation (ree-v3 `e3_selector.py` + `agent.py` + `config.py`)

A strict ADDITIVE extension of the ARC-108 machinery behind a no-op-default master flag
`use_finer_channel_gating`. The ARC-108 `w_chan` path is left BYTE-IDENTICAL (ARC-106 G2
reuse-the-mechanism, parallel buffer, zero risk to the V3-frozen substrate).

- **Finer registry** (`e3_selector.py`): the single ARC-108 `"score_bias"` slot exploded into
  `("ofc", "dacc", "lpfc", "vigour", "liking", "gated_policy", "residual", "mech341", "route")`.
  The six **named** channels map onto the existing per-head biases (OFC←SD-033b, dACC←SD-032b
  adapter, lateral-PFC←SD-033a, vigour←MECH-320, liking←MECH-295, gated_policy←ARC-062); the
  preserved `mech341`/`route` channels are unchanged. **`residual` = `score_bias − Σ(named present)`**
  (computed by subtraction in `select()`) captures everything else summed into `score_bias`
  (MECH-314 curiosity / MECH-353 blocked-agency / SD-058 avoidance / SD-059 escape /
  any future term), so the decomposition is **EXHAUSTIVE** ⇒ `Σ(finer) == score_bias` exactly.

- **Parallel learned buffer** `w_chan_finer` (`register_buffer`, NOT `nn.Parameter`) + a finer
  eligibility trace `_fcg_elig_trace` + pending/diagnostic state. Init at `ln(e-1)` so
  `softplus(w_chan_finer[c]) == 1.0` for every channel ⇒ the finer decomposition reproduces the
  compressed blend EXACTLY at init (**bit-identical even when ON, until the weights train apart**).
  V-hat_t is SHARED with the ARC-108 baseline (the two gating modes are mutually exclusive — A1
  vs A2 arms).

- **Data flow:** `agent.select_action` captures each finer constituent's un-summed `[K]` bias
  into a `score_bias_channels` dict (the SAME tensors already summed into `dacc_score_bias`),
  passed to `e3.select()` (version-layering guard: only when the flag is on). `select()` registers
  one `_lcg_term` per present finer channel + the residual; the registry-agnostic recompose
  `_modulatory_accum = Σ_c softplus(w_chan_finer[c])·bias_c`, the eligibility `_fcg_elig_trace[c]
  += |bias_c[selected]|`, and the three-factor update `Δw_chan_finer[c] = η·delta_t·elig_c·asym`
  (one shared signed RPE) all ride the active registry/buffer. As the finer weights diverge under
  per-channel signed-RPE credit, `_modulatory_accum` becomes a per-candidate vector ≠ the uniform
  sum — the conversion MECH-451 tests. The authority rescale / top-k shortlist (the landed
  arithmetic envelope, run as a matched constant) carry the re-weighted accumulator into the
  committed argmax.

- **Backward compatible:** flag off ⇒ `score_bias_channels=None` ⇒ legacy single `"score_bias"`
  term ⇒ bit-identical; the A1 `use_learned_channel_gating` path is unchanged.

- **MECH-094:** waking-only (eligibility recorded only on a non-simulation `select()`; the
  three-factor update gated on a pending waking finer trace) — inherited from ARC-108.

- **Phased training: NO** — local non-backprop three-factor rule; reuses the already-trained
  valuation heads (R_t = benefit_eval − harm_eval); no encoder head, no collapse risk.

## ARC-106 cargo-cult guard

The degeneracy hazard is "the finer channels move IDENTICALLY = the compressed blend
re-labelled." Two protections, both built into EXP-0391 (not the substrate):
1. **Non-degeneracy readiness gate:** dissociable cross-channel `w_chan_finer` variance
   (`fcg_w_chan_finer_range`/`_std` diagnostics) + a divergent candidate pool (GAP-A guard) —
   self-routes `substrate_not_ready_requeue` if unmet.
2. **Load-bearing ablation = A1_GLOBAL_WCHAN** (collapse-to-blend = one global `w_chan` over the
   sum). If A1 reproduces A2's lift, the decomposition is NOT load-bearing. A1 *is* an EXP-0391 arm.

## What this enables

- **MECH-439** — a valid V3 test of whether the conversion ceiling is representational
  compression vs an intrinsic property requiring per-loop competition.
- **ARC-110 / `v4_loop_segregation`** — PRE-EMPTED on an A2 PASS; routed-to on an A2 no-lift.
- The minimal representational degree-of-freedom before any function-specific gating pathology
  (ARC-106 EARNS psychiatric-failure-mode modelling, weakest V3 form).

## Validation experiment

**EXP-0391** (`manual_proposals.v1.json`) → a `V3-EXQ-700`-sibling on the GAP-A-ready foraging
substrate: arms **A0_ENVELOPE_ONLY / A1_GLOBAL_WCHAN / A2_FINER_CHANNELS / ARM_NOISE**, settling
`W_lat` OFF on all arms, landed arithmetic envelope (demotion + top-k + authority) a matched
constant, SD-056-trained `e2.world_forward` + ARC-065 GAP-A `candidate_summary_source=e2_world_forward`
(the divergent-pool non-vacuity precondition). PRIMARY DV = committed-action-class entropy.

## Related claims

MECH-451, ARC-108, MECH-450, ARC-110, MECH-439, MECH-447, MECH-448, MECH-449, ARC-107, ARC-106,
SD-033a/b, SD-032b, MECH-320, MECH-295, ARC-062, MECH-094.
