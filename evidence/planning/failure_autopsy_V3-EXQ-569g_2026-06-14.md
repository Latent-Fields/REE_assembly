# Failure Autopsy — V3-EXQ-569g (ARC-065 GAP-A route-range matched-entropy falsifier)

**Generated:** 2026-06-14T20:14:00Z
**Scope:** single (lineage member; see recurrence note)
**Status:** confirmed (user adjudicated routing via AskUserQuestion 2026-06-14 — diagnose-first)
**Target:** `v3_exq_569g_gapa_routerange_matched_entropy_falsifier_20260611T224954Z_v3`
**Queue id:** V3-EXQ-569g · **claim_ids:** [ARC-065] · **evidence_direction:** non_contributory
**Routing:** queue-experiment (claim-free in-arm collapse diagnostic) — NOT a 4th implement-substrate amend

---

## The adjudicated question

569g self-routed `r1a_entropy_only_artefact` ("readiness met, committed entropy is
not above matched noise — an entropy-only artefact / genuine ceiling"). Is that
the right reading, or does it **mis-label the cause** the way V3-EXQ-642 did
(self-routed `substrate_ceiling` on a substrate that was never actually active)?

**Verdict: it mis-labels.** The `r1a_entropy_only_artefact` self-route reads
"readiness met → ceiling," but the routing/authority mechanism the readiness gate
certified was **not active in the arms where the primary DV was scored**. This is a
**precondition-unmet / instrumentation defect** (the readiness gate guards a
*different statistic* than the one applied at committed selection), not a genuine
substrate ceiling. The correct route is a focused diagnostic to locate the
collapse, then a targeted fix — not a 4th blind substrate amend.

---

## 1. Facts (no interpretation)

From the 569g manifest:

- `acceptance_criteria`: `readiness_route_range_ready=TRUE`,
  `readiness_consumed_spread_ready=TRUE`, `readiness_substrate_ready=TRUE`,
  `C1_arm1_e2_world_forward_divergent=TRUE`,
  **`C_R1B_selected_entropy_strict_above_matched_noise=FALSE`** → `overall_pass=FALSE`.
- `summary.readiness.arm1_route_range_mean = 0.179852` (clears `route_range_floor=0.01`).
- **`arm_results[0/1/2].modulatory_channel_route_range_mean = 0.0`** and
  **`_max = 0.0`** for ALL THREE falsifier arms (ARM_0 proposer, ARM_1 e2_world_forward,
  ARM_2 matched-noise).
- Selected-action class entropy bit-identical across PROPOSER / E2WF / MATCHED-NOISE
  (the `r1a_entropy_only_artefact` signature); 0/3 seeds strict-above-both.

**Smoking gun:** the **readiness probe** measures ARM_1 route_range **= 0.18**;
the **falsifier arms** apply route_range **= 0.0** (all three). The readiness gate
and the scored arms disagree on the *same quantity* (`modulatory_channel_route_range`).

**Failed criterion:** discrimination (`C_R1B`), scored on arms whose enabling
mechanism (`modulatory_channel_route_range`) reads exactly 0.

## 2. Why this is instrumentation, not a ceiling

`project_channel_range` (e3_selector.py:61) is **range-preserving by construction**
(center across K → project onto the leading right-singular vector → [K] scalar). A
0.18-spread input therefore yields a *non-zero* projected per-candidate range. So an
applied `modulatory_channel_route_range = 0.0` in the arms means the **input** to
`project_channel_range` at the live select tick — the in-arm `cand_world_summaries` —
**re-collapsed to ~0 spread**, OR the routing block did not fire in the arm path at
all. Either way the channel-range the readiness gate certified (0.18, measured in a
separate probe) is **not reproduced where the DV was scored**. C_R1B tested nothing.

This is the V3-EXQ-642 pattern: a self-routed "ceiling" on a run where the
mechanism-under-test was inert in the measured condition.

## 3. Claim-layer map

`claim_ids=[ARC-065]` (provisional architectural commitment; v3_pending already
cleared 2026-05-31). 569g does NOT and CANNOT falsify ARC-065 — the diversity-reaching-
committed-action mechanism it would falsify reads 0.0 in the arms. The result is
correctly `non_contributory`; ARC-065 unmoved. claim_ids accurate (single claim,
not inherited).

## 4. Biological-reference triage

Mechanism under test: a modulatory/contextual bias channel reaching the **committed**
action while competing with a forward-model-dominated primary score (BG-like
action selection where neuromodulatory/contextual biases shift the committed
choice only with sufficient gain relative to the value gap). **Not a formal-import**;
**no lit gap** — the failure is wiring/instrumentation, not biology divergence. No
`/lit-pull` warranted.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | ARC-065 not tested under expressible conditions (applied route_range=0.0); non_contributory, not falsification |
| Biological reference | clear | BG-like modulatory-bias-vs-value-gap selection; no formal import; no lit gap |
| Prerequisites | present-but-inactive | route-range substrate (663 PASS) + authority (643a PASS) landed, but inactive at the live arm select site |
| Implementation completeness | **partial — instrumentation defect** | readiness gate certifies channel-representation spread (probe), NOT the applied per-candidate routed bias at select; the two diverge 0.18 vs 0.0 |
| Environment | adequate | — |
| Measurement | **MISLEADING (load-bearing)** | C_R1B scored on arms where the enabling mechanism reads 0.0; the readiness gate guards the wrong statistic |
| Integration | partially coupled | channel→authority→committed-action validated piecewise in probes; live arm shows 0 conversion |
| Scale | adequate | — |

**Recommended `epistemic_category`:** the result stays `non_contributory`. It is NOT
`substrate_ceiling` — that is the mis-label. The shape is **precondition-unmet /
instrumentation defect** (same class as V3-EXQ-642).

## 6. Recurrence — substrate iteration, not claim-granularity debt

This is the **6th autopsy** circling the GAP-A channel→committed-action conversion:
569c → 569e → 614e → 643 → 569f-661-654a → 569g. The recurrence is **substrate
iteration** (each amend fixed an isolated-probe statistic while the live arm
re-collapsed), NOT granularity debt on a coarse claim — ARC-065 is one architectural
commitment, not several mechanisms. So the route is **diagnose-first** (locate the
substrate collapse), explicitly **not** `/claim-synthesis`.

The three readiness-validated amends (gain-relative authority 06-03; float32 fix
06-06; route-range 06-10) each certified the mechanism **in a probe** and the
falsifier kept scoring its DV on arms where the applied conversion reads 0.0. A 4th
amend on an unlocated cause would be the 4th iteration of the same mistake.

## 7. Learning extracted

1. **The GAP-A falsifier's readiness gate certifies the wrong statistic.** It guards
   the channel *representation* spread (a probe: consumed-summary / route_range
   measured outside the scored arms), not the *applied* per-candidate
   `modulatory_channel_route_range` at the live committed-selection tick. The two
   diverge (0.18 vs 0.0). Any future GAP-A falsifier MUST gate on the **in-arm
   applied** route_range, measured on the same ticks as C_R1B.
2. **Locate before amend.** The applied 0.0 has three candidate causes — (i) in-arm
   `cand_world_summaries` re-collapse despite `candidate_summary_source=e2_world_forward`
   (upstream monostrategy at the live select tick), (ii) `project_channel_range`
   degeneracy on the live input, (iii) routing-source wiring not plumbed into the arm
   agent config (vs only the readiness probe). A claim-free diagnostic must
   disambiguate before any /implement-substrate.
3. The SD-056-NaN prime suspect is disconfirmed for this lineage: 569f/569g
   `C1_arm1_e2_world_forward_divergent=TRUE`; V3-EXQ-617 already validated the SD-056
   multistep stability amend. The blocker is the conversion, not the predictor.

## 8. Routing (user-confirmed, diagnose-first)

- **queue-experiment**: a claim-free (`claim_ids=[]`) in-arm route-range collapse
  diagnostic — measure the LIVE in-arm per-candidate `cand_world_summaries` spread
  AND the applied `modulatory_channel_route_range` at the actual select tick across
  ARM_0/ARM_1/ARM_2, plus enough internal probes to attribute the 0.0 to (i)/(ii)/(iii).
- **implement-substrate**: GATED on the diagnostic locating the collapse. Not now.
- **Then** a real GAP-A falsifier (V3-EXQ-569h-successor) with an **in-arm**
  applied-route-range non-vacuity gate (assert applied route_range > floor *in the
  scored arms*, not just a probe).
- `recommended_substrate_queue_entry.action = none`: the
  `modulatory-bias-selection-authority` entry already exists and already carries the
  569f/661/654a failure records; do NOT add a new substrate entry or a 4th amend on
  an unlocated cause. The diagnostic must locate it first.

## Draft `evidence_quality_note` (for /governance — do NOT write here)

> [2026-06-14 autopsy V3-EXQ-569g]: 569g FAIL/non_contributory `r1a_entropy_only_artefact`
> MIS-LABELS the cause. The readiness probe certified ARM_1 `modulatory_channel_route_range`
> = 0.18 (clears floor), but ALL THREE falsifier arms applied route_range = 0.0 at the
> committed-selection site — so C_R1B was scored on runs where the routing/authority
> mechanism-under-test was inert (V3-EXQ-642 precondition-unmet pattern, NOT a substrate
> ceiling). `project_channel_range` is range-preserving, so the in-arm `cand_world_summaries`
> re-collapsed (or routing did not fire in the arm path). ARC-065 unmoved (non_contributory,
> not a falsification). Routed diagnose-first: a claim-free in-arm route-range collapse
> diagnostic locates (i) live-arm summary re-collapse / (ii) project_channel_range / (iii)
> routing-source wiring BEFORE any 4th modulatory-bias-selection-authority amend; the next
> real GAP-A falsifier must gate on the IN-ARM applied route_range, not a probe statistic.
