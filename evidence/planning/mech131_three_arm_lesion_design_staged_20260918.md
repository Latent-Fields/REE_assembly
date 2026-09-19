# MECH-131 three-arm anticipatory-residue lesion -- DESIGN

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml, experiment_proposals.v1.json, or experiment_queue.json.**

Authored by headless session `metaworker-science-20260918-mech131-vmpfc-analog` (ree-cloud-4)
under user decision **OPTION C** (2026-09-18T22:54Z) on chip
`chip-20260918-mech131-lesion-completeness`. Chip: `chip-proposal-exp-0878-paced`.
Proposal of record: **EXP-0847** (`backlog_id` EVB-1435, `proposal_type` experimental).

## Why this file exists rather than a queue entry

Everything the recorded text specifies is settled below. **One coupled criterion is not
derivable from any recorded text and was therefore NOT invented:** the PASS/FAIL bar for
"suppression" and "gradedness", and the coupled question of whether this run is a
`diagnostic` probe or governance evidence for MECH-131. MECH-131 has **no
`what_would_answer`**, and EXP-0847's `acceptance_checks` are auto-minted boilerplate
(`require_pre_registered_thresholds: false`). Raised as a decision chip; see the end of this
file.

## Substrate: READY (built by this session, landed and verified)

Two call-site knobs on `HippocampalConfig`, both default `True` = current behaviour,
bit-identical:

| Knob | Gates | Landed |
|---|---|---|
| `terrain_prior_residue_channel_enabled` | CH1 -- `residue_field.evaluate` -> `residue_val` -> `terrain_prior` -> initial action-object proposal mean | ree-v3 `a548f1f1` |
| `score_trajectory_residue_terrain_enabled` | CH2 -- `_score_trajectory` -> `residue_field.evaluate_trajectory` -> CEM elite `argsort` + refit (both the z_world path and the pre-SD-005 z_self fallback) | this session |

Contracts: `ree-v3/tests/contracts/test_mech131_terrain_prior_residue_channel.py`
(C1-C9, 10 tests). Measured on the hub 2026-09-18:

- CH1 lesion moves the proposal mean: max|delta| **0.449** (absmean 0.1288 -> 0.0528).
- CH2 lesion collapses the CEM terrain-score spread **0.892 -> exactly 0.0** over 32
  proposed candidates -- i.e. elite selection becomes provably residue-blind.
- Complete (CH1+CH2) lesion: spread 0.881 -> 0.0, proposal mean moved, **post-hoc scorer
  still live at 21.62**, storage totals identical to intact.

That last line is the claim's own precondition, pinned as a contract rather than assumed.

## Arms (user-specified -- do not vary without a new decision)

| Arm | CH1 | CH2 | Reads as |
|---|---|---|---|
| `ARM_1_intact` | True | True | full anticipatory activation |
| `ARM_2_ch1_lesion` | **False** | True | the design the AMBER pre-flight originally named |
| `ARM_3_complete_lesion` | **False** | **False** | no anticipatory read; storage + post-hoc still live |

`ARM_3` is the internal residue-blind reference for generation -- a *measured* structural
fact (CEM spread exactly 0.0), not an assumption, so no fourth control arm is needed.

## DVs, each mapped to a recorded prediction

MECH-131's `notes` state three predictions. Each maps to one DV; nothing below is invented.

- **DV1 <- prediction (1)** "...failing to shift trajectory distribution away from them in
  generation." `residue_avoidance` = mean `residue_field.evaluate_trajectory` over the
  **proposed candidate pool** (pre-E3-selection), at a state whose region has accumulated
  residue. LOWER = more avoidance. Direction predicted: `ARM_1 < ARM_3`.
- **DV2 <- prediction (3)** "The activation signal should be graded by residue curvature
  magnitude: high-residue trajectories produce stronger anticipatory suppression than
  low-residue trajectories." `gradedness_rho` = rank correlation, across candidates, between
  a candidate's residue magnitude and its suppression (loss of proposal mass) in `ARM_1`
  relative to `ARM_3`. Direction predicted: positive.
- **DV3 <- prediction (2)** "Residue activation must precede trajectory ranking, not follow
  it... a post-hoc filter is not an active state constraint -- INV-038 applies."
  Recorded as a structural dissociation, not a threshold: in `ARM_3`, generation is
  residue-blind (CEM spread 0.0) **while** `E3.compute_residue_cost` is non-zero. This is the
  contrast the claim rests on and it is already contract-pinned (C8).

`ARM_2` sits between them and is what makes the 3-arm design worth more than a 2-arm one: it
partitions the effect between the two channels, and it is the arm that tells us whether the
originally-pre-flighted single-knob design would have been able to detect anything at all.

## Preconditions the run must record and assert (all derivable)

1. `num_harm_events > 0` in every arm -- otherwise the probe is vacuous.
2. `total_residue` identical across arms -- "correctly stored but not activated". The lesion
   must not perturb storage.
3. `compute_residue_cost` non-zero in every arm -- the post-hoc null path survives.
4. CEM terrain-score spread: `> 0` in ARM_1/ARM_2, `== 0.0` in ARM_3.

## Recording obligations (from the Experimental Recording Standard, not invented)

- `run_id` ends `_v3`; `architecture_epoch: "ree_hybrid_guardrails_v1"`.
- A **flat** top-level `readout` block of numeric scalars: each criterion's measured value
  AND its bar, per-arm DVs, seed/arm censuses. **Booleans as `0`/`1` ints** (`_is_number`
  excludes `bool`, so a raw `True` is invisible to the indexer).
- Keep the nested `arm_results` / `per_seed_*` blocks as well -- flat block is the
  machine-readable projection, not a replacement.
- **GOV-ECOL-1 (2026-09-16): report TWO replication counts, never one.** `stochastic
  replication: N seeds` and `world-family replication: N families`. This design uses ONE
  world family, so the result must be written `ecological transfer untested`. Seeds alone
  never license "general" / "robust" / "transfers".
- Seeds: EXP-0847 says "At least 2 additional runs with distinct seeds",
  `seed_policy: distinct_seeds` -> **>= 3 distinct seeds**.
- `claim_ids_tested: ["MECH-131"]`, plus `evidence_class` / `evidence_direction` per
  EXP-0847's `required_pack_contract`.
- `emit_outcome(...)` as the single terminal call in `__main__` (runner conformance).

## Gates already cleared by this session

- **2.5 / 2.5a substrate readiness** -- CLEARED. Both knobs exist, are reachable through
  `REEConfig.from_dims` (all three sites, the MECH-307 failure shape explicitly contract-
  tested), and were empirically probed, not merely doc-checked.
- **2.5b re-derive brake** -- CLEARED. 0 braking autopsies for MECH-131 across 523 artifacts.
- **2.5c substrate-path overlap** -- CLEARED on measurement. Four open `corrupting`
  entries exist, and **every one is inert at the config this design uses**:
  `contextmemory-write-path-addressing-degeneracy` (both call sites gated:
  `sd016_writepath_mode` defaults `"off"`, `contextmemory_write_addressing_loss_weight`
  defaults `0.0`), `MECH-320` (`use_tonic_vigor=False`),
  `sd_blocked_agency_mismatch_floor_calibration` (`use_blocked_agency=False`),
  `sd105_frozen_shared_entropy_floor_multiplier` (`use_selection_entropy_floor=False`).
  The driver must keep all four at their defaults; if any is ever enabled, this gate
  re-fires and the design must stop.
- **`degrading` overlaps to record in the queue-entry `note`** (do not block, per the gate):
  `SD-MECH267-CEM-SELECTION-FIX` (`hippocampal/module.py`, `utils/config.py` -- directly on
  the CEM path this design measures), `SD-MECH303-THRESHOLD-SOURCING`, `SD-091`
  (`agent.py::select_action`), `SD-ZWORLD-SENSE-PATH-PARITY` (`agent.py::sense`),
  `SD-018` / `SD-106`.
- **2.4 existing-evidence / GOV-REUSE-1** -- NOT RECOVERABLE, so the run is warranted: the
  decisive readout is per-arm `residue_avoidance` under a lesion of the anticipatory residue
  channels, and **the manipulation did not exist in the substrate until 2026-09-18**, so no
  recorded manifest can carry it. MECH-131 has no entry in `claim_evidence.v1.json` and no
  completed run.
- **2.6 ethics preflight** -- all flags `false`, `decision: allow` (SENT-0: V3 is
  pre-ethical instrumentation).

## THE OPEN DECISION (the only thing blocking a queue entry)

The arms, DVs, directions, preconditions and recording are all fixed above. What is NOT
derivable from any recorded text is **the evidential bar, and the coupled purpose**:

- How much lower must `ARM_1`'s `residue_avoidance` be than `ARM_3`'s to count as
  "suppression"? An ordinal rule (strictly lower in every seed)? An effect-size floor? A
  statistical test with an alpha?
- How many seeds -- the floor of 3 from EXP-0847, or more?
- Does `gradedness_rho > 0` suffice for prediction (3), or is a magnitude floor required?
- Is this `EXPERIMENT_PURPOSE = "diagnostic"` (measures the effect, hands governance the
  numbers to author MECH-131's missing `what_would_answer`, does NOT weight confidence) or
  governance evidence that moves MECH-131's status?

These are coupled: a diagnostic legitimately reports the three arms' DVs with ordinal
criteria; governance evidence needs a pre-registered bar. Both change what the run concludes
and which claim the evidence attaches to, so neither was chosen here.

Recommendation stated for the record: **`diagnostic`, with ordinal criteria and >= 3 seeds**
-- it is the honest first move for a claim with no `what_would_answer`, it cannot generate a
misleading *weakens* verdict off an arbitrary threshold, and its output is exactly the
material needed to author the `what_would_answer` that a later governance-grade run would
pre-register against. The cost is that it does not itself move MECH-131's status.

---

# ADDENDUM 2026-09-19 -- the bar was ratified, then the DV failed a measurement

**User decision (2026-09-19T00:49Z) settled the open question above:** DIAGNOSTIC,
ORDINAL criteria, >= 3 seeds. Suppression = `ARM_1` `residue_avoidance` strictly lower
than `ARM_3` per seed, effect sizes reported with no invented floor; gradedness reported
as rho with its sign, no magnitude floor; the run does not move MECH-131's status.

The driver was authored against that: `ree-v3/experiments/v3_exq_1061_mech131_anticipatory_residue_lesion.py`
(`V3-EXQ-1061`, id arbitrated to this session after 1059 and 1060 were taken by siblings).
Its dry-run passes end to end on the hub -- 9/9 cells, all four preconditions met, C1 and
C2 met, gradedness computed.

**It was NOT queued, because the DV cannot detect its own manipulation.** Measured on the
hub 2026-09-19:

| charge steps | pool mean residue | between-candidate SD | intact vs complete-lesion effect |
|---|---|---|---|
| 60  | 31.405 | 0.056 (**0.18%**) | 0.0005 (**0.0017%**) |
| 200 | 99.477 | 0.181 (**0.18%**) | 0.0018 (**0.0018%**) |

The lesion effect is ~**100x smaller than the between-candidate noise**, and the ratio is
scale-invariant -- accumulating more residue does not help. All 32 candidates land in
essentially the same residue region, so residue-based selection has nothing to exploit.
C1's per-seed ordinal test would therefore be resolving differences two orders of magnitude
below candidate-level variance. It would "pass" or "fail" on noise. With no floor (correctly,
per the ratified decision), nothing in the criterion would catch that -- which is exactly why
this had to be measured before queuing rather than after.

**Root cause is the codebase's own documented expectation, not a new finding.**
V3-EXQ-042 (hippocampal terrain training) states it directly: *"if terrain_prior is random,
proposals are uninformed (equivalent to random candidates)"*. Residue avoidance is a LEARNED
competence in this architecture. This driver runs an **untrained** agent, so lesioning the
anticipatory channel removes a capability the substrate never acquired -- the null it would
return means "an untrained generate-rollout loop cannot express residue avoidance", not
"MECH-131 is false". Tellingly, V3-EXQ-042's own eval metric is this design's DV1 almost
verbatim: `hippo_quality_gap = mean_residue_random - mean_residue_hippo`.

## What the fix would be (NOT applied -- it changes what gets measured)

Train the generator before lesioning, following V3-EXQ-042's existing protocol rather than
inventing one: terrain_prior via E3 behavioural cloning,
`MSE(terrain_prior_ao_mean, selected_trajectory_ao_sequence.detach())`, with its
`hippo_quality_gap` (hippocampal vs random proposal residue) as the readiness gate that
confirms the generator actually acquired avoidance before any arm is lesioned. 12 existing
drivers train `terrain_prior`, so this is adoption of precedent, not novel design.

This was not applied unilaterally because it changes what gets measured -- trained vs
untrained substrate -- adds a training phase with its own episode counts and phasing
hazards, and multiplies runtime across 9 cells. The user's 2026-09-19 instruction was
explicit that any further un-pre-registered choice of that kind is another decision.

Raised as decision chip **`chip-20260918-mech131-untrained-substrate`**.

**What is already banked and needs no redoing:** both lesion knobs (ree-v3, contract-pinned,
C1-C9 green); every `/queue-experiment` gate cleared with evidence (2.5/2.5a substrate,
2.5b brake 0/523, 2.5c all four open corrupting entries measured inert, 2.4 not recoverable,
2.6 allow); the ratified criteria; and the driver itself, whose measurement/manifest/readout
machinery is verified working and would be reused unchanged -- only a warmup phase and a
readiness gate would be added ahead of it.
