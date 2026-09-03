# Failure autopsy — EXT claim-probe cluster (V3-EXQ-983, 991, 993, 994)

**Generated:** 2026-09-03T20:04:14Z · **Scope:** cluster (4 targets) · **Status:** confirmed at the /failure-autopsy Step 8 interactive gate, 2026-09-03
**Machine-readable:** `failure_autopsy_ext-claim-probe-cluster_2026-09-03.json`

---

## 1. What these four runs are

Four claim-probe experiments, run 2026-09-03, each against one `external_failure_mode` claim:

| Run | Claim(s) | Recorded direction | Corrected to |
|---|---|---|---|
| V3-EXQ-983 | EXT-002 (hallucination / persistent error residue) | `weakens` | **`non_contributory`** |
| V3-EXQ-991 | EXT-004 (goal misgeneralization / cross-context carry) | `does_not_support` | **`non_contributory`** |
| V3-EXQ-993 | ARC-021, EXT-003, MECH-069 (three-loop separation) | `unknown` | **`non_contributory`** (all three) |
| V3-EXQ-994 | EXT-007 (context amnesia / consolidation) | `non_contributory` | `non_contributory` (unchanged) |

None is a dry run. All four pass `validate_recording.py` with zero always-core gaps. No prior autopsy has ever adjudicated an EXT-* claim, so this cluster sets the precedent for the battery.

---

## 2. The load-bearing finding: DV dynamic-range failure

In all four runs the load-bearing comparison was **never adjudicated**, because a control-arm or DV property fell outside the range the configuration could produce:

| Run | The quantity that had no room | Achievable | Registered threshold | Shortfall |
|---|---|---|---|---|
| 993 | `calibration_gap`, SEPARATED (control) arm | max 0.00152 over 12 cells | `SEPARATED_SIGNAL_FLOOR` 0.02 | **13.1x** |
| 994 | retention excursion in the control arm | spread 0.00078 | 0.02 | **25.6x** |
| 983 | `decline_gap` (the DV) | realised range 0.0468 | C1 0.15 | **3.2x** |
| 991 | — | DV varies 59x but measures hazard-field occupancy, not action suppression | — | construct-invalid |

**This is not confined to the EXT battery.** The same shape recurs in V3-EXQ-981 (a 2x threshold on a DV bounded in [0,1]; a 51x shortfall against a saturated baseline's arithmetic ceiling), V3-EXQ-951c (a classification outcome with zero reachable ticks) and V3-EXQ-978 (an arm difference one third of the DV's quantum) in the same pending-review batch. Six of those seven runs **passed all their preconditions**.

The common mechanism: **readiness gates certify that the INTERVENTION was applied — was the channel perturbed, did the head train, were there enough samples — and nothing certifies that the DEPENDENT variable had room to move.** That is why the substrate recommendation below is scoped to the experiment programme, not to these four runs.

---

## 3. The claim-layer argument that was tested and WITHDRAWN

An earlier draft of this autopsy argued that EXT-002/003/004/007 should take `epistemic_category: out_of_domain`, on the grounds that their `subject` fields are `llm.hallucination`, `llm.reward_hacking`, `llm.goal_misgeneralization`, `llm.context_amnesia` with `polarity: asserts` — i.e. they assert deficiencies of transformer systems, with REE's answer carried as a rider in `notes`, so no REE run could bear on them.

**That recommendation is withdrawn.** The cross-model red-team pass found, and the drafting session independently verified:

- EXT-003's own `evidence_quality_note` carries a **user ruling made at the /governance Step 3 gate on 2026-09-03 — the same day** — stating verbatim: *"What this claim actually waits on is EXPERIMENTAL evidence, the load-bearing channel. Status stays candidate for THAT reason, not for conflict resolution."*
- `out_of_domain` is a member of `_UNTESTABLE_EPISTEMIC` (`generate_inter_governance_workset.py:988-991`), so the stamp would make the claim structurally unable to receive the very channel that ruling says it waits on.
- All four probes were dispatched from `experiment_proposals.v1.json` as `proposal_type: experimental` rows against the EXT ids themselves. The draft would have overturned a standing convention, not set one.

The category is **`standard`** for all four; all keep full v3 experiment lanes. The observation about `subject` survives only as a note on how these probes should be *constructed* — they must be built to test the `ree_mechanism` rider explicitly.

> **Boundary case worth keeping.** `external_failure_mode` is not a uniform class. EXT-009's subject is `ree.similarity_gated_care_collapse` — an explicitly **reflexive** failure mode of REE itself — and EXT-008's is `meta_agent.*`. Any future rule keyed to this `claim_type` would give the wrong answer on both.

---

## 4. Per-target diagnosis

### V3-EXQ-983 (EXT-002) — corrected from `weakens`

All nine preconditions passed. The residue manipulation was clean (32/32 active centres, coverage 1.0 in A0; confirmed empty in A1) and reached behaviour (action-stream divergence 0.186–0.295). The positive control passed at 51x. What defeats the run:

- **DV headroom.** `decline_gap`'s realised range across all six cells is 0.0468 against a C1 threshold of 0.15. Underlying `repeat_rate` is high but *not* pinned — 8 of 12 readings exceed 0.95, 6 exceed 0.985, observed range 0.864–0.993.
- **Seed population.** `steps_realized_frac` is 0.077 / 0.085 / 0.965 on seeds 42 / 123 / 456 — a ~12x spread in realised training, recorded in the manifest and gated by nothing. The two barely-trained seeds sit at `harm_rate_train` 0.73–0.75; the fully-trained seed at 0.0236. Equal-weight pooling across that population is what produces the −0.4pp `decline_gap`.

> **An inference this autopsy made and withdrew.** An earlier draft argued harm was unavoidable *by construction* from grid geometry (size=6 → 4×4 interior; minimum hazard field 1/(1+0.5×6) = 0.25, above the 0.15 proximity threshold). The arithmetic is right; the inference is refuted by the run's own cells — **seed 456 ran 57,900 steps at 2.4% harm on the same board.** Recorded rather than deleted, so the next session knows the reading was tested.

Still standing: guard **P5 names this DV-pinning signature in its own description** yet measures `harm_rate_train` (0.743/0.752 against a 0.90 ceiling) rather than `repeat_rate`. Nothing in the gate watches the quantity P5 exists to protect.

### V3-EXQ-991 (EXT-004) — corrected from `does_not_support`

The manipulation was confirmed real on both sides (NAIVE Context A: 0 harm events, 0.0 residue, all five seeds). But Context B (size=8 → 6×6 interior) has minimum hazard field 0.1667, above the 0.15 proximity threshold, so `harm_rate` measures mean hazard-field occupancy rather than the action-level suppression the claim's rider names. The driver's **own `attribution_caveat`** records that the design does not isolate ARC-013's residue field from ARC-108 `w_chan`/`V-hat_t` or MECH-165's exploration buffer — the manipulation replaces the entire Context-A experience stream. There is no positive control, and the `non_contributory` self-route branch was structurally unreachable: `naive_control_clean` is a constant-TRUE detector by construction.

### V3-EXQ-993 (ARC-021, EXT-003, MECH-069)

Both *named* preconditions passed with large headroom (forward-head action sensitivity 0.0893 vs floor 0.005 = 17.9x; P1 harm events 1208 vs floor 10 = 120.8x). What failed is an **unnamed non-degeneracy gate inside `_condition_verdict()`** — `SEPARATED_SIGNAL_FLOOR = 0.02` — not met in *either* condition. The unablated control arm's `calibration_gap` read −0.00065 (DENSE) and −0.00022 (SPARSE), negative in 4 of 6 baseline cells. An ablation of a signal the control arm never produced discriminates nothing.

Mechanically the flatness is **downstream of the forward head**, which is action-sensitive (0.089–0.137): the harm head compresses two well-separated predicted latents onto near-identical sigmoids, so `causal_sig` occupies ~0.2% of its [−1,+1] range. The author's red-team note N3 predicted this regime and **declined to lower the floor — that judgement was correct and the floor must not be relaxed.** The readout compression is the thing to fix.

ARC-021 and MECH-069 stay `standard`: a readout dynamic-range ceiling is measurement debt, not a substrate ceiling on the claims, and stamping otherwise would wrongly suppress them from v3 lanes.

### V3-EXQ-994 (EXT-007) — self-declared degenerate, confirmed

Both preconditions honestly read `met: false` and `criteria_non_degenerate.C1_retention_score` is false.

- **The control arm could not be disturbed.** Retention at ceiling in *both* arms (all six cells ≥ 0.9992; spread 0.00078 against a required 0.02).
- **Addressing is degenerate on 2 of 3 seeds** (`n_encode_written_slots` = 1, 1, 16) under the default `contextmemory_write_selection=argmin` — the signature of the registered `corrupting`-severity defect `contextmemory-write-path-addressing-degeneracy`, which this run neither guarded against nor mentions. **Contributory but not sufficient:** seed 56 wrote all 16 slots and retention was *still* pinned.

> **A second inference this autopsy made and withdrew.** Within each seed, eleven of thirteen recorded fields are bit-identical across arms to 16 significant figures — `test_residue` included, read *after* the TEST boundary. An earlier draft read that as "the consolidation arm left no mechanistic footprint" and as the first experimental corroboration of `mech092-replay-consumer-missing`. The red-team pass refuted it from the same `arm_results` block: **`memory_matrix_retention_score` is 0.99792 WITH against 0.9999983 WITHOUT** on seeds 42 and 49 — the consolidation arm's ContextMemory matrix moved ~1000x further from unity than the control's, consistent with the driver's statement that sleep writes B-content into ContextMemory. Consolidation *did* act; residue simply is not the channel it writes to. The proposed amend to `mech092-replay-consumer-missing` was dropped.

---

## 5. Failure location (GOV-FAILLOC-1)

None of the four reaches REE FAILED. Implementation, measurement and environment do not each independently read adequate in any of them.

| Run | Mechanism | Measures | Environment | Net |
|---|---|---|---|---|
| 983 | not established | not established | not established | MIXED (MEASURES dominant + ungated seed-population defect) |
| 991 | not established | not established | not established | MIXED (MEASURES + ENVIRONMENT) |
| 993 | partial | not established | partial | MEASURES |
| 994 | not established | not established | not established | MIXED (MEASURES + ENVIRONMENT) |

---

## 6. Routing

- **993 → `/implement-substrate`**, with a `create` recommendation: **`dv-dynamic-range-precondition-class`** (priority 1, severity `corrupting`). Extend `validate_experiments.py` with a `criterion_exceeds_achievable_range` check in the same WARN-only family as the existing `dry_run_unreachable_criterion` lint, plus a runtime `dv_headroom` precondition kind in `experiments/_metrics.py::p0_readiness_gate()` that measures the control arm's realised DV range and routes to `substrate_not_ready_requeue` when the registered threshold exceeds it. Two sub-cases it must catch: a multiplicative threshold on a bounded DV, and a threshold above the arithmetic ceiling implied by a saturated baseline.
- **994 → `/implement-substrate`**, `amend` `contextmemory-write-path-addressing-degeneracy` with a fresh failure_record item (a hit taken *without* the fix knob enabled — recording it is what makes the Step 2.5c defect gate protect the next experiment).
- **983, 991 → `/queue-experiment`** redesigns, each requiring a DV with demonstrated headroom and, for 983, a training-completion gate before pooling seeds.

> **Pre-routing check C1 fired and was acted on.** Three drivers for the ARC-021/MECH-069 family already exist on disk and have **never produced a manifest**: `v3_exq_004_arc021_incommensurability.py`, `v3_exq_005_mech069_error_scale.py`, `v3_spark_arc021_three_loop_scale.py`. Whoever re-poses the three-loop question must first evaluate whether these already cover it rather than authoring a fourth.

---

## 7. Learning extracted

1. Readiness gates in this corpus certify the intervention, never the DV's headroom. Six of seven runs in this batch passed all preconditions and still could not discriminate.
2. A guard can name the exact failure signature it exists to catch and still miss it by measuring a different quantity (983's P5).
3. A non-degeneracy gate living inside `_condition_verdict()` rather than in `interpretation.preconditions` is invisible to the readiness report and to every downstream reader (993).
4. `slot_overlap_frac = 1.0` is compatible with only ONE slot ever being written; overlap fraction is the wrong statistic when the denominator can be 1 (994).
5. Before reading an arm-invariant metric as "the mechanism did nothing", check which channel the mechanism actually writes to (994).
6. Declining to lower a floor the data misses by 13x was the correct call and is recorded as such, so a later session does not "fix" the run by relaxing it (993).
