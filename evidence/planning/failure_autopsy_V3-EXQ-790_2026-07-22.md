# Failure autopsy — V3-EXQ-790/791 (channel-routing cross-class magnitude replication)

**Scope:** single. **Status:** confirmed (user-adjudicated 2026-07-22).
**Generated:** 2026-07-22T03:48:30Z. **Promotes and demotes nothing.**

Run: `v3_exq_790_channel_routing_cross_class_magnitude_replication_20260722T021558Z_v3` ·
`queue_id V3-EXQ-791` · `claim_ids []` · purpose `diagnostic` · outcome **FAIL** ·
direction `non_contributory` · self-route `substrate_not_ready_requeue`,
indexer flag **`precondition_unmet`**.

---

## 1. Facts

Recording complete (`rec/v1`, `substrate_hash`, `machine_class`
`darwin-arm64-py3.13-torch2.12.0`, `config`, `seeds [42..51]`,
`substrate_stable_across_run`, `arm_knobs_effective`). **No recording debt.**

**Both science criteria PASSED.**

| Criterion | Result |
|---|---|
| **C1** route active in ARM_1, inactive in ARM_0 | ✅ — `route_active_frac` 1.0 vs 0.0; 10/10 seeds active, 10/10 inactive |
| **C2** committed-class TV above floor in ARM_1 | ✅ — 8/10 seeds (bar 7) |
| `arm1_routed_bias_range_supra_floor` | ✅ 0.334 vs 0.01 floor |
| `routed_range_bounded` | ✅ 1.644 vs 1e6 ceiling |
| `arm1_seeds_above_floor` | ✅ 10 vs 7 required |
| **`adequate_fresh_selection_sample`** | ✗ — worst cell **53** vs floor **200** |

The sole failure is the fresh-selection sample floor, and the offending cell is
**`ARM_0_NO_ROUTE::seed49`** — one seed of the **control** arm, whose `route_range` is
structurally **0.0** by construction (`route_range_per_arm_mean.ARM_0_NO_ROUTE: 0.0`,
`route_active_frac 0.0`).

The floor of 200 was derived from the *nominal default* cadence: "nominal window
P1×(steps−measure_after)=3600 ticks yields ~360 selections at the default
`heartbeat.e3_steps_per_tick=10`". But the live E3 cadence is **MECH-093-modulated
across 5–20 steps**, so 3600 ticks yields between 180 and 720 selections depending on
arousal — and 53 implies a cell that sat at the slow end for most of the window.
**The floor was computed against a cadence the substrate does not actually run.**

---

## 2. Adjudicating the self-route

**The self-route `substrate_not_ready_requeue` is WITHDRAWN. The readiness gate is
defective; the science stands.**

Two independent reasons, either sufficient:

1. **The gate is arm-blind where it must be arm-scoped.** `ARM_0_NO_ROUTE` is the
   *control* arm: routing is off, `route_range` is identically 0, and no C1 or C2
   statistic is estimated from it beyond "route is inactive" — which was established
   at 10/10 seeds. A starved sample in a cell whose measured quantity is structurally
   zero cannot invalidate an effect measured in a different arm at 10/10 seeds. This
   is exactly the hazard the V3-EXQ-785 autopsy (sections 2a/8) already ruled on and
   that **V3-EXQ-794 and V3-EXQ-737 have both already fixed** in their own drivers —
   794 via `per_arm_gate` with green/red arms and an explicit
   `preconditions_scope_note`, 737 by moving a non-gating guard into
   `recorded_preconditions`. 790's driver did not adopt either pattern, so its one
   starved control cell propagates to a whole-run `precondition_unmet` through the
   indexer's flat, arm-blind `_compute_adjudication`.

2. **The floor itself is mis-derived.** 200 was computed from
   `e3_steps_per_tick=10`, ignoring the MECH-093 5–20-step modulation that governs the
   real cadence. A gate whose threshold assumes a cadence the substrate does not run
   will fire on healthy runs indefinitely.

**Consequence.** The gate's stated purpose was to close the ~9× pseudo-replication
defect the shared 662/663 driver carried (`route_range_mean` was a mean over latched
repeats, inflating effective n ~9-fold). That purpose is **fully served** in the arm
that matters: ARM_1's routed-range statistics are computed on the corrected
denominator and clear their floors at 10/10 seeds. Refusing the run over a starved
control cell does not protect against pseudo-replication; it discards a clean result.

---

## 3. Claim-layer mapping

`claim_ids: []` by design — this is a substrate-readiness diagnostic and weights no
claim's confidence. Its function is to **unblock** the per-claim behavioural retests of
**ARC-065 / MECH-294 / ARC-062 / MECH-309 / MECH-341**, each a separate
`/queue-experiment` session. Those five claims stay `candidate` / `v3_pending` /
`pending_retest_after_substrate` and are **not** weakened by this run either way.

The practical cost of upholding the requeue is therefore concrete: five downstream
retests stay stalled on a gate defect rather than on a substrate fact.

---

## 4. Biological-reference triage

Not the operative axis — this is an instrumentation adjudication on a landed substrate
feature (`E3Config.use_modulatory_channel_routing` + `project_channel_range`, landed
2026-06-10), not a mechanism test. Recorded for completeness: the routed quantity is a
cross-candidate *range* projected into a modulatory bias, whose biological analogue is
neuromodulatory gain control scaling a competition among candidates rather than
selecting among them. `is_formal_import: false`; no divergence at issue here.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **n/a** | No claims tagged; readiness diagnostic. |
| Biological reference | **partial** | Not the operative axis for this adjudication. |
| Prerequisites | **present** | Routing wired and active; range supra-floor and bounded. |
| Implementation completeness | **complete** | The substrate feature under test works: 10/10 seeds route-active in ARM_1, 0/10 in ARM_0. |
| Environment adequacy | adequate | — |
| Measurement adequacy | **misleading — DOMINANT LAYER** | Readiness floor derived from a nominal cadence (`e3_steps_per_tick=10`) that the MECH-093-modulated 5–20-step substrate does not run; and applied arm-blind to a structurally-zero control arm. |
| Integration adequacy | coupled | — |
| Scale / capacity | adequate | 10 seeds; ARM_1 fully sampled. |

**Recommended `epistemic_category`: `measurement_test_design_defect`.**
Explicitly **NOT** `substrate_ceiling` and **NOT** a substrate verdict.

---

## 6. Learning extracted

1. **The route-range routing substrate IS ready.** C1 and C2 both pass on the
   corrected, non-pseudo-replicated denominator: routing is active in 10/10 ARM_1
   seeds and inactive in 10/10 ARM_0 seeds, the routed bias range is supra-floor
   (0.334 vs 0.01) and bounded (1.644 vs 1e6), and committed-class TV clears the floor
   on 8/10 seeds against a bar of 7. This is the finding the run was commissioned to
   produce and it is not in doubt.
2. **A readiness floor must be derived from the LIVE cadence, not the default knob.**
   The 200-selection floor assumed `e3_steps_per_tick=10`; the live cadence is
   MECH-093-modulated over 5–20 steps, giving 180–720 selections for the same nominal
   window. Any floor keyed to the default will fire spuriously on arousal-slow cells.
   **Derive sample floors from the modulated range's worst case, or scale them to the
   observed tick count.**
3. **The arm-scoped precondition pattern exists and is not being adopted uniformly.**
   794 (`per_arm_gate` green/red with a `preconditions_scope_note`) and 737
   (`recorded_preconditions` for non-gating guards) both solve this; 790's driver
   carries neither. The indexer's `_compute_adjudication` is flat and arm-blind by
   design, so **the driver is the only place this can be fixed** — and a driver that
   omits the pattern silently converts one bad control cell into a whole-run refusal.
   Worth a manifest-local lint.
4. **Recording debt: none.** The per-arm route statistics, per-seed committed TV, the
   offending cell identity and the fresh-select denominator were all recorded — which
   is precisely why this could be adjudicated from the manifest without a re-run.

---

## 7. Repair pathway

**Node classification:** `complicated (buildable)` — the fix is a named change to the
gate with no open question.

**Re-derive brake:** no claims tagged; not applicable. This autopsy records no
`substrate_ceiling` reading against any claim.

**Granularity-debt recurrence:** not applicable (`claim_ids: []`).

**Routing: `/queue-experiment` — same-question re-run, alphabetic suffix (790a/791a),
gate fix only.** Two changes, no substrate build:

1. **Arm-scope the readiness gate.** Adopt the 794 `per_arm_gate` pattern: apply
   `adequate_fresh_selection_sample` to the arms whose statistics are actually
   estimated from the sample (ARM_1), carry the control arm's sample count as a
   `recorded_precondition`, and keep the flat `interpretation.preconditions` list free
   of scored-out cells so the indexer cannot re-vacate a green arm.
2. **Re-derive the floor from the live cadence.** Scale `FRESH_SELECT_FLOOR` to the
   MECH-093-modulated worst case, or express it as a fraction of the cell's observed
   E3 tick count rather than an absolute derived from `e3_steps_per_tick=10`.

`recommended_substrate_queue_entry.action = "none"` — the substrate under test works.
**Do not route to `/implement-substrate`.**

**Downstream, and this is the point of the run:** the route-range readiness finding is
recorded here as **upheld**, so the five per-claim behavioural retests it was
commissioned to unblock (**ARC-065 / MECH-294 / ARC-062 / MECH-309 / MECH-341**) may
proceed as separate `/queue-experiment` sessions. Governance should treat 790's C1/C2
pass as the readiness evidence, with the caveat that 791a will re-confirm it under a
correctly-scoped gate.

### Draft `evidence_direction_note` (governance to write — do not apply here)

> 2026-07-22 (V3-EXQ-790/791, diagnostic, claim_ids=[], `non_contributory` — weights
> nothing; failure_autopsy_V3-EXQ-790_2026-07-22). The `substrate_not_ready_requeue`
> self-route and its `precondition_unmet` flag are **WITHDRAWN as a gate defect**.
> Both science criteria PASSED: routing active in 10/10 ARM_1 seeds and inactive in
> 10/10 ARM_0 seeds, routed bias range supra-floor (0.334 vs 0.01) and bounded (1.644),
> committed-class TV above floor on 8/10 seeds against a bar of 7 — all on the
> CORRECTED, non-pseudo-replicated denominator the gate was built to enforce. The sole
> failed precondition is `adequate_fresh_selection_sample` (53 vs a floor of 200) on
> `ARM_0_NO_ROUTE::seed49` — one seed of the CONTROL arm, whose `route_range` is
> structurally 0.0 and from which no C1/C2 statistic is estimated. Two defects: the
> gate is applied arm-blind where 794 (`per_arm_gate`) and 737 (`recorded_preconditions`)
> already demonstrate the arm-scoped pattern, and the 200-selection floor was derived
> from `e3_steps_per_tick=10` while the live cadence is MECH-093-modulated over 5–20
> steps (180–720 selections for the same window). The route-range routing substrate is
> READY. The per-claim behavioural retests of ARC-065 / MECH-294 / ARC-062 / MECH-309 /
> MECH-341 are unblocked; those claims are not weakened. Re-run as 791a with an
> arm-scoped gate and a cadence-derived floor to re-confirm.

---

## 8. Confirmed routing (user-adjudicated 2026-07-22)

User selected **"Gate defect — uphold the science"** over upholding
`substrate_not_ready_requeue` and over the provisional-evidence middle option.
