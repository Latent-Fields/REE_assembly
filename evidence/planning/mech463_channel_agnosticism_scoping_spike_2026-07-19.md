# MECH-463 channel-agnosticism scoping spike

**Date:** 2026-07-19T16:43:44Z
**Session:** `vibrant-lewin-132fa6`
**Status:** COMPLETE -- viable second incumbent identity FOUND; probe queued as V3-EXQ-785b
**Amended:** 2026-07-19T20:31:26Z -- section 6 RETRACTED (the "785a never seeds torch" finding
was wrong; the unseeded harness was this spike's own scratch script). Sections 1-5 and 7-9
stand; see section 6 for what this does and does not affect.
**Predecessor:** `failure_autopsy_V3-EXQ-785_2026-07-19.md` section 9a; V3-EXQ-785a
(adjudicated 2026-07-19, REE_assembly `e8d4325cbd`)

---

## 1. Question

V3-EXQ-785a refuted MECH-463's registered concentration prediction under exogenous urgency
(`var_total` fold 0.970, incumbent share gap +0.0036, under 1 SE). MECH-463 was deliberately
left at `candidate` rather than demoted, because 785a tested exactly **one** incumbent
identity (`harm_weighted`), while MECH-463 asserts the amplification is **channel-agnostic
across incumbent identities**.

This spike asks the narrow prerequisite question:

> Is there ANY configuration of the E3 score decomposition in which (a) a component OTHER
> than `harm_weighted` is the incumbent, and (b) at least 2 components hold `|share| > 0.01`,
> so the decomposition is genuinely **measured** rather than **arithmetically forced**?

The obvious second regime (`entropy_incumbent`) was already tried and recorded non-viable by
785a's authors: `CH:mech341` absorbs ~99-115% of cross-candidate variance at every
`entropy_bias_scale` in {0.15, 0.30, 0.50, 1.00}, so shares-sum-to-1.0 forces every other
component below the floor. That axis is **excluded, not re-tested here.**

## 2. Answer

**YES.** Two viable second identities exist, both replicating across seeds 0/1/2. The
stronger is a **`residue_weighted` incumbent with harm still ON** -- a genuine reweighting
in which a different channel takes the incumbency while the harm channel remains alive,
which is precisely the channel-agnosticism contrast MECH-463 needs.

## 3. What the baseline decomposition actually contains

Aggregating the 1765 per-tick rows embedded in the 785a manifest
(`custom_information.per_tick_rows`), only **three of seven** components are alive at all:

| component | mean share | sd | note |
|---|---|---|---|
| `harm_weighted` | +0.9390 | 0.0778 | the 785a incumbent |
| `f` | +0.0533 | 0.0684 | alive, small |
| `residue_weighted` | +0.0077 | 0.0251 | alive, sub-floor at baseline |
| `benefit_weighted` | +0.0000 | 0.0000 | config-gated off |
| `novelty_weighted` | +0.0000 | 0.0000 | **dead by construction** |
| `goal_weighted` | +0.0000 | 0.0000 | needs an active `goal_state` |
| `CH:residual` | +0.0000 | 0.0000 | -- |

Three of the four zeros are **structural, not incidental**, and this is the spike's main
negative result:

- **`novelty_weighted` is dead by construction.** `e3_selector.py:963-971` hardcodes
  `_dc_novelty_w = 0.0`; the MECH-111 broadcast branch that populated it was deleted
  2026-05-25 as dead-by-construction (a uniform scalar shift is argmin-invariant), and the
  field is retained only for `last_score_decomp` schema backward-compat. A novelty-weighted
  incumbent is **not reachable by configuration** -- it needs substrate work.
- **`benefit_weighted`** is reachable but triple-gated (`benefit_eval_enabled` AND
  `benefit_weight > 0` AND `_benefit_samples_seen >= 50`), and in scan config B1 the warmup
  never cleared inside the horizon, collapsing to `n_nontrivial = 1`.
- **`goal_weighted`** needs an active `goal_state`, which the CausalGridWorldV2 harness in
  this lineage does not supply.

### The two global-scalar routes named in the spike brief are structurally ineligible

Both were checked in code and **neither can change the incumbent identity**, so neither was
scanned:

- **D1/D2 dopamine gain** (`e3_selector.py:1553-1570`, applied at 1728-1729) operates on a
  loop **accumulator** (`assoc_accum`, `limbic_accum`) *after* channel composition. It
  re-gains the aggregate; it is not an additive component in the decomposition.
- **Softmax temperature** (`e3_selector.py:2682`, `3102`) divides the composed score inside
  the softmax, strictly downstream of the per-candidate component vectors the shares are
  computed from. It can move which candidate commits; it cannot move a component share.

The viable axis is therefore the **component-weight** axis (`lambda_ethical`, `rho_residue`),
not the global-scalar axis.

## 4. Scan

Method mirrors the entropy scan already recorded in 785a's
`custom_information.dropped_regime_evidence`: seed 0, 150 ticks, same
`_build_agent_and_env` / tick loop, same `_component_shares` covariance-correct estimator
imported directly from the 785a driver. Baseline reproduced the published incumbent share
(0.9313 / 0.9649 across two runs vs 785a's 0.9368) -- close enough to confirm the estimator
and the tick loop were wired correctly, which is what this scan needed.

**But note what that 0.9313 / 0.9649 spread actually was**: not run-to-run noise in 785a, but
this scratch harness building agents outside an `arm_cell` and therefore without the RNG
reset (see the section 6 retraction). Every number in the table below was produced through
that unseeded harness, so treat the table as **indicative-only** -- a viability screen, not a
measurement. The regime selection rests on the seeded replication in section 5, not here.

| config | incumbent | share | n_nontrivial | viable |
|---|---|---|---|---|
| A0 baseline (785a harm regime) | `harm_weighted` | +0.9649 | 3 | no |
| A1 `hazard_harm=0.0` | `harm_weighted` | +1.1021 | 3 | no |
| **A2 `lambda_ethical=0.05`** | **`f`** | **+0.7632** | **3** | **yes** |
| A3 `lambda_ethical=0.0` | `f` | +1.0491 | 2 | forced |
| A4 `lambda=0.0` + `rho_residue=5.0` | `residue_weighted` | +1.0140 | 2 | forced |
| **A5 `rho_residue=20.0` (harm ON)** | **`residue_weighted`** | **+0.5018** | **3** | **yes** |
| B1 `benefit_eval` on, `lambda=0.0` | `f` | +1.0095 | 1 | no |
| B2 `benefit_eval` on, warmup cleared | `f` | +0.8879 | 2 | yes (weak) |
| C1 `goal_weight=1.0`, `lambda=0.0` | `f` | +1.0151 | 2 | forced |

**Reading the `forced` rows.** A3/A4/C1 all put the incumbent at ~1.0 with a *negative*
remainder. That is the same cancellation pathology as the excluded entropy regime, in a
different costume: the incumbent absorbs the whole budget and the residual components are
sign-flipped noise, not measured structure. They technically clear `n_nontrivial >= 2` and
should still be rejected. **The discriminating criterion is incumbent share comfortably
below 1.0 with same-signed runners-up**, which only A2 and A5 satisfy.

## 5. Replication (torch seeded, seeds 0/1/2)

| regime | seed | incumbent | share | non-trivial components |
|---|---|---|---|---|
| A2 `lambda_ethical=0.05` | 0 | `f` | 0.8254 | f .825 / harm .090 / residue .084 |
| A2 | 1 | `f` | 0.9836 | f .984 / residue .047 / harm -.031 |
| A2 | 2 | `f` | 0.6831 | f .683 / residue .185 / harm .132 |
| **A5 `rho_residue=20.0`** | 0 | `residue_weighted` | 0.5848 | residue .585 / harm .358 / f .057 |
| **A5** | 1 | `residue_weighted` | 0.8870 | residue .887 / harm .097 / f .016 |
| **A5** | 2 | `residue_weighted` | 0.8679 | residue .868 / harm .123 |

**A5 is the primary regime.** Incumbency is stable (`residue_weighted` at all three seeds,
never `harm_weighted`), every share is below 1.0 with no negative runner-up, and
`harm_weighted` survives as a genuine second component (0.358 / 0.097 / 0.123). Critically
it keeps the harm channel **ON**: it is a reweighting, not an ablation, so a PASS/FAIL here
speaks to channel-agnosticism rather than to harm-channel necessity. Mean incumbent share
across seeds 0.780 -- comfortably under 1.0, so the `>= 2` non-trivial-component
pre-condition (P7) is **satisfiable in principle**, which is exactly what the entropy regime
could never claim.

A2 is retained as a **secondary** regime. It replicates, but seed 1 lands at 0.9836 with a
negative harm share -- close to the forced boundary -- so it is the weaker of the two.

## 6. RETRACTED: the "785a never seeds torch" finding was wrong

**This section originally reported a defect in 785a. That report was incorrect and is
retracted.** It is kept rather than deleted so the claim is not re-derived by the next
reader of this file.

**What was claimed:** `v3_exq_785a_...py` never calls `torch.manual_seed`, so agent weight
init varies run to run -- evidenced by an identical baseline config producing incumbent
share 0.9313 and 0.9649 on two runs of the same seed. Concluded: 785a's individual cells are
not reproducible and its `arm_cell` fingerprint cannot be reuse-matched with confidence.

**Why it is wrong.** 785a builds its operative agent inside `_collect_cell`, and
`_collect_cell` is invoked *inside* the `with arm_cell(seed, ...)` block. `arm_cell`'s entry
calls `reset_all_rng(seed)`, which seeds `random`, numpy, **torch (+cuda)**, and the
`_harness` module-level fallback RNG (`experiments/_lib/arm_fingerprint.py`). The absence of
a literal `torch.manual_seed` in the 785a file is therefore not evidence of an unseeded run
-- the seeding is discharged by the cell wrapper, which is the documented and intended
mechanism. **785a's cells ARE pure functions of `(substrate, config, seed)` and its
reuse-eligibility is sound.**

**Where the observed variation actually came from.** The spike's own scratch harness
(`mech463_incumbent_scan.py`, section 9) constructed agents by calling `build()` directly,
with no `arm_cell` wrapper and hence no RNG reset. The 0.9313 / 0.9649 pair was measured
through that harness. The defect was in the throwaway scan script, not in 785a. It was
corrected mid-spike by adding `torch.manual_seed(seed)` to the scratch `build()` before the
section 5 replication -- which is why section 5 is a genuine seed sweep and section 4 (run
before the fix) is not bit-reproducible.

**Consequences for the rest of this document.** Section 4's table was produced through the
unseeded harness and should be read as indicative-only -- which is all a viability scan needs
to be, and its qualitative conclusion (which regimes are viable) is confirmed by the seeded
section 5 replication. Section 5, the replication that actually selects the regimes, was run
seeded and stands. No other section depends on the retracted claim.

**Consequence for the queued probe.** V3-EXQ-785b keeps an explicit `torch.manual_seed` in
its builder, but it is documented there as REDUNDANT belt-and-braces for direct callers
outside a cell, NOT as a fix for a 785a defect.

## 7. Caveats

- **Short horizon.** 150 ticks yields only ~17-22 fresh selections per cell (the commitment
  latch holds most ticks). Adequate for identifying a viable regime, **not** for any
  scientific readout. Share point-estimates here carry real noise; the queued probe runs the
  full 3000-tick horizon.
- **The `z_world` under-differentiation caveat is not resolved, but is weakened.** The
  standing concern (participation ratio ~1.06 at `world_dim=128`, absolute variances
  ~1.2e-05) predicts that forced-single-component outcomes are a symptom of degenerate world
  representation rather than of decomposition design. A5 is mild evidence **against** that
  reading in this regime: at unchanged `world_dim` a three-way split of 0.585/0.358/0.057
  is attainable, so the baseline's single-component profile is at least partly a
  component-weight fact rather than purely a `z_world` fact. This does not clear the caveat
  for the absolute-variance readout, only for the share readout.
- **A5's regime is off the substrate's default operating point.** `rho_residue=20.0` against
  a default of 0.5 is a 40x reweighting. It is a legitimate probe of channel-agnosticism
  (the claim is about incumbent identity, not about the default configuration) but it is
  **not** a claim about how the agent normally behaves, and the queued probe's `note` says so.

## 8. Outcome

Viable second identity found -> the channel-agnosticism probe is queued via
`/queue-experiment`, reusing 785a's exogenous-urgency design (i.i.d. uniform assignment over
a pre-registered grid, per-tick rows embedded in the manifest,
`e3.last_score_diagnostics` cleared before every `select_action`).

**Not** routed to a substrate gap -- the untestability finding applies only to the
`novelty_weighted` identity (dead by construction) and, more weakly, to `benefit_weighted`
and `goal_weighted`. Those narrow the breadth of "channel-agnostic" that any V3 result can
license, and that limit belongs in the queued probe's interpretation section: a PASS across
{`harm_weighted`, `residue_weighted`} licenses agnosticism across **two cost-side
components**, not across the full registered channel set.

## 9. Reproduction

Scan scripts are scratchpad-only (spike, not experiment code):
`mech463_incumbent_scan.py` (9 configs, seed 0, 150 ticks) and `mech463_replicate.py`
(2 regimes x 3 seeds). Both import `_component_shares`, `_urgency_signal`,
`URGENCY_LEVELS` and `PRIMARY_COMPONENTS` directly from
`ree-v3/experiments/v3_exq_785a_mech463_arousal_exogenous_urgency_decomp.py`, so the
estimator is identical to the published one by construction. The tables above carry every
number produced; nothing is retained that the tables do not report.
