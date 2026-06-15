# Failure Autopsy — V3-EXQ-684 (GAP-A modulatory-conversion-readiness sweep)

- **schema:** failure_autopsy/v1
- **generated_utc:** 2026-06-15T17:39:14Z
- **scope:** single
- **status:** confirmed (user-adjudicated 2026-06-15 — diagnosis accepted)
- **run_id:** v3_exq_684_modulatory_conversion_readiness_20260615T164543Z_v3
- **queue_id:** V3-EXQ-684
- **claim_ids:** [] (claim-free; ARC-065 behavioral_diversity_isolation:GAP-A substrate-readiness diagnostic)
- **outcome:** FAIL — self-route `substrate_not_ready_requeue`; indexer adjudication flag `precondition_unmet`

## 1. Scope

V3-EXQ-684 is the claim-free 6-arm readiness sweep authored by the GAP-A 682-gated
conversion-amend session (landed `gapa-682-gated-conversion-amend`, ree-v3 main `1acc343`).
Its job: identify WHICH conversion lever (gain/contrast normalization basis, or
shortlist-then-modulate) makes the routed per-candidate modulatory channel range MOVE the
committed argmax — to select the config for the SEPARATE V3-EXQ-569h GAP-A falsifier
(gated on this PASS). It ran to completion; it is NOT a crash → `/failure-autopsy` applies,
not `/diagnose-errors`.

## 2. Facts (reconstruction; no interpretation)

Per-arm aggregate (`summary`):

| arm | route_range_mean | selected_action_entropy_mean | C_CONVERSION pass seeds |
|---|---|---|---|
| ARM_PROPOSER (proposer src, T=1.0) | 0.0 | 0.549141 | (reference) |
| ARM_MATCHED_NOISE (proposer src, T=2.5) | 0.0 | **0.549141** | (control) |
| ARM_LEGACY_E2WF (e2wf src, additive range, gain 0.5) | 0.187306 | 0.774586 | (no-conversion bar) |
| ARM_STD_G1 (e2wf, additive std, gain 1.0) | 0.134903 | 0.667236 | 1/3 |
| **ARM_STD_G2 (e2wf, additive std, gain 2.0)** | 0.426777 | **0.988649** | **2/3** |
| ARM_SHORTLIST (e2wf, shortlist margin 0.25) | 0.349735 | 0.336824 | 0/3 |

Readiness block (`summary.readiness`):
- `route_range_floor` 0.01 → ARM_LEGACY_E2WF route_range 0.187 (3/3 seeds above floor) → `route_ready: true`.
- `c1_pairwise_dist_floor` 0.03 → ARM_LEGACY_E2WF e2 pairwise dist 0.060 (3/3 divergent) → `pdist_ready: true`.
- `matched_noise_lift_seeds_over_proposer` **0** → `control_ready: false`.
- `readiness_ok: false` (because control_ready is false).

`c_conversion`: `winning_arms: [ARM_STD_G2]`, `c_conversion_pass: true`, `selected_entropy_floor` 0.3.

**The failing criterion is a READINESS precondition**, not the load-bearing criterion:
the load-bearing `C_CONVERSION` PASSED; the precondition
`matched_noise_control_verify_lifts_over_proposer` is the lone FAIL → self-route
`substrate_not_ready_requeue`. **Smoking gun:** ARM_MATCHED_NOISE selected-action entropy
(0.549141) is **byte-identical** to ARM_PROPOSER (0.549141) — raising proposer temperature
to T=2.5 produced exactly zero committed-entropy lift.

## 3. Claim layer

Claim-free. ARC-065 (behavioral_diversity_isolation:GAP-A) is the home claim; it is NOT
tagged and NOT weighted by a readiness diagnostic (the script's own framing: "claim-free →
cannot weaken any claim"). MECH-341 / ARC-062 / MECH-309 / MECH-294 (the downstream
conversion beneficiaries) are untouched.

## 4. Root cause — the matched-noise positive control is mis-designed

The script (docstring lines 46-50, "READINESS-2 the 569g gap") requires ARM_MATCHED_NOISE to
**verify-lift** committed entropy strictly above ARM_PROPOSER — added precisely because
569g's temperature-matched control under-lifted (`entropy==proposer`), making 569g's
"beats-noise" bar vacuous. The intent: prove the entropy metric CAN move under undirected
variance, so a conversion arm beating it is non-vacuous.

**684's matched-noise control under-lifted in the exact same way** (0.549141 == 0.549141).
The cause is structural: the matched-noise arm raises the **PROPOSER** (candidate-generation)
temperature, but selected-action entropy is measured at the **COMMITTED** selection — the
F-dominated argmax (88-89% of E3 variance, V3-EXQ-571). The conversion ceiling under study
washes out undirected proposer variance before it reaches committed selection. So
proposer-temperature noise **cannot lift committed entropy on this substrate by construction**
— the matched-noise positive control is subject to the very ceiling it is meant to provide a
clean baseline *above*, making the readiness gate **structurally unsatisfiable** regardless of
whether the conversion mechanism works.

Meanwhile the **directed** gain lever injects at the E3 **selection-authority** layer
(downstream of F, where the modulatory channel is rescaled relative to the primary):
**ARM_STD_G2 (gain=2) DID convert** — committed entropy 0.774586 (legacy) → 0.988649, route
range amplified 0.187 → 0.427, 2/3 seeds clear C_CONVERSION. Directed gain reaches committed
action where undirected proposer-noise cannot — the discrimination GAP-A has been chasing.

### Self-route adjudication (the `precondition_unmet` flag)

The precondition is **genuinely unmet** (the control did not lift), so the self-route
correctly does NOT promote to 569h. But the label's IMPLIED cause ("re-queue at higher P0 /
check route-range wiring") is **wrong**: the route-range wiring is fine (preconditions 1+2
met 3/3) and a higher P0 cannot fix a structurally-unsatisfiable positive control. This is
the **V3-EXQ-642 pattern** — the precondition *test itself* is mis-designed, so the label
mislabels the cause → route to **redesign** (queue-experiment), not a naive re-queue.

C_CONVERSION's pass is **partially meaningful**: STD_G2 beating *legacy* (0.775 → 0.989, the
no-conversion routed bar) is the genuine conversion signal; STD_G2 beating *noise* is vacuous
(the noise control is broken). Encouraging, but cannot promote until the readiness control is
fixed.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (claim-free) | ARC-065 GAP-A readiness; not weighted |
| Biological reference | n/a | measurement/test-design question, not a formal-definition import |
| Prerequisites | present | route-range 0.187 (3/3) + e2 divergence 0.060 (3/3) both clear |
| Implementation | complete + functional | gain/contrast conversion amend works — STD_G2 (gain=2) converts |
| Environment | adequate | identical 569g stack |
| **Measurement** | **mis-designed** | matched-noise positive control injects at the PROPOSER, blocked by the conversion ceiling → can never lift → readiness gate unsatisfiable |
| Integration | fine | |
| Scale / capacity | n/a | |

**Dominant diagnosis layer:** measurement / test-design defect (mis-designed readiness
positive-control). Recommended `epistemic_category`: not applicable (claim-free diagnostic);
recommended `evidence_direction`: `non_contributory`.

## 6. Recurrence (process, not granularity-debt)

This is the Nth GAP-A autopsy (569c / 569e / 569f-661-654a cluster / 569g / 684). Target is
claim-free; `/claim-synthesis` does **not** fire (no coarse claim hiding finer claims — this
is a sequential instrumentation chain converging on a working conversion mechanism, and 684
shows PROGRESS: the gain lever converts). The load-bearing recurrence is a PROCESS pattern:
**matched-noise-at-proposer has now under-lifted twice (569g + 684), same signature** — that
control is the wrong instrument for an F-dominated substrate. This is consistent with the
critical-path-synthesis finding that instrumentation defects, not falsifications, dominate
the GAP-A frontier.

## 7. Learning extracted

1. The matched-noise "verify-lift" positive control MUST be injected at the committed-selection
   layer (post-F), not at the proposer — a proposer-temperature control is washed out by the
   F-dominated argmax and can never serve as a metric-can-move proof on this substrate.
2. The directed gain=2 lever (ARM_STD_G2, additive std basis) is the identified working
   conversion config: committed entropy 0.775 → 0.989 over legacy, route range amplified
   0.187 → 0.427, 2/3 seeds. Carry it forward as the leading 684a → 569h candidate.
3. STD_G2's lift over LEGACY (the routed-but-unconverted bar) is the non-vacuous conversion
   signal; the beats-noise comparison is the vacuous part (the noise control is broken).
4. ARM_SHORTLIST HURT (entropy 0.337, below proposer 0.549) on this config — the gain path,
   not shortlist-then-modulate, is the lever that converts here.

## 8. Repair pathway / routing — `/queue-experiment` V3-EXQ-684a (test-design fix)

Same scientific question, alphabetic suffix (implementation/test-design fix). **Carry
ARM_STD_G2 (gain=2, additive std basis) forward as the leading conversion config.** On 684a
PASS, V3-EXQ-569h is queued with the winning config. NOT `/implement-substrate` (substrate +
gain lever both work — NOT conversion_ceiling_persists). NOT governance-demotion (claim-free).
`recommended_substrate_queue_entry.action: none`.

Two fix designs (user deferred the choice to the queue session; both recorded, recommendation below):

- **Option (a) — committed-layer metric-can-move control:** replace the matched-noise positive
  control with matched-magnitude undirected variance injected at the COMMITTED-selection layer
  (post-F score / argmax), so it CAN lift committed entropy if the metric is alive — a valid
  "structured-beats-noise" non-vacuity bar. Keep matched-noise-at-proposer as a NEGATIVE
  control (it should NOT lift; now a confirmed property).

- **Option (b) — beats-legacy bar (lighter):** reinterpret matched-noise-at-proposer as a
  NEGATIVE control (should NOT lift), and make the load-bearing C_CONVERSION =
  directed-gain-arm strict-above LEGACY (the no-conversion routed bar) on ≥2/3 seeds — the
  non-vacuous bar STD_G2 already clears (0.989 > 0.775, 2/3). The metric-can-move proof comes
  from STD_G2's and LEGACY's own lift over proposer (the metric is demonstrably alive).

**Recommendation:** the robust design is the HYBRID — keep matched-noise-at-proposer as a
negative control (it MUST NOT lift), make the load-bearing bar beats-LEGACY on ≥2/3 (option b,
which STD_G2 already clears so 684a likely PASSes immediately and unblocks 569h), AND add the
committed-layer metric-can-move control (option a) as a non-vacuity guard. Final design is the
`/queue-experiment` session's call.

## 9. Recommended evidence_quality_note (governance to record on the 684 manifest)

> V3-EXQ-684 (claim-free GAP-A modulatory-conversion-readiness sweep) FAIL/non_contributory:
> the load-bearing C_CONVERSION PASSED (ARM_STD_G2 gain=2 committed entropy 0.989 strict-above
> legacy 0.775 + noise 0.549, 2/3 seeds) but the readiness precondition
> matched_noise_control_verify_lifts_over_proposer FAILed (matched-noise entropy 0.549
> byte-identical to proposer, 0/3). Confirmed failure_autopsy_V3-EXQ-684_2026-06-15: the
> matched-noise positive control is MIS-DESIGNED — it raises proposer temperature, but the
> F-dominated committed argmax (88-89% E3 variance, V3-EXQ-571) washes out undirected proposer
> variance, so it can never lift committed entropy on this substrate (the conversion ceiling it
> is meant to baseline above). The route-range + e2-divergence preconditions both cleared 3/3,
> and the DIRECTED gain lever (STD_G2) DID convert — so this is a test-design defect, NOT a
> substrate ceiling and NOT a conversion-ceiling-persists verdict. The self-route
> substrate_not_ready_requeue is correct to not-promote but mislabels the cause (V3-EXQ-642
> pattern). Route: /queue-experiment V3-EXQ-684a with a committed-layer metric-can-move control
> (or matched-noise reinterpreted as a negative control + C_CONVERSION = beats-legacy on ≥2/3),
> carrying ARM_STD_G2 (gain=2) forward as the leading conversion config; on PASS, queue
> V3-EXQ-569h. ARC-065 / MECH-341 / ARC-062 / MECH-309 / MECH-294 NOT weakened. No
> substrate_queue create/amend (the conversion amend is implemented and functional).
