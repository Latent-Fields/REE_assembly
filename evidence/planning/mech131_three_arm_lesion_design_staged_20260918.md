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

---

# ADDENDUM 2026-09-19 (2) -- OPTION A implemented; the ratified readiness gate CANNOT clear

**User decision OPTION A (2026-09-19T02:32Z)** was implemented in full: V3-EXQ-042's
terrain_prior warmup (E3 behavioural cloning,
`MSE(terrain_prior_ao_mean, selected_trajectory_ao_sequence.detach())`, `Adam(lr=5e-4)`,
600 episodes x 200 steps -- 042's own numbers) plus 042's `hippo_quality_gap` as a
readiness gate. Landed in `ree-v3/experiments/v3_exq_1061_mech131_anticipatory_residue_lesion.py`.

**V3-EXQ-1061 edited in place, not lettered.** The EXQ versioning policy's letters
supersede a *queued* entry or a *recorded run*; 1061 has neither -- authored, landed
unqueued, never executed. No evidence to supersede and no `runner_status` collision.

**Design point the decision settled implicitly:** "the gate must clear *before any arm is
lesioned*" fixes this as **train one intact agent per seed, then read all three arms off it
by toggling the two live read gates at evaluation**. Weights identical across arms, so the
arms differ only by the lesion -- a within-subject lesion, and a third of the compute. Only
possible because both knobs are read live off `HippocampalConfig` rather than cached.

## Measured (hub, 2026-09-19): the gate does not clear, and cannot

20 episodes x 100 steps x 3 seeds, 9m36s wall (~10.4 steps/s, so 042's full 600x200x3 is
**~9.6 hours**):

| seed | hippo_mean_residue | random_mean_residue | hippo_quality_gap (needs > 0) |
|---|---|---|---|
| 11 | 9.888 | 6.943 | **-2.946** |
| 23 | 12.029 | 7.674 | **-4.355** |
| 37 | 16.968 | 7.735 | **-9.232** |

`effect_over_noise` rose from ~0.01 (untrained) to **0.035** -- the right direction, but
parity needs ~1.0, so ~30x short.

**The gap is strongly NEGATIVE, not merely short.** Undertraining would put it near zero.
The cause is in 042's own recorded manifest
(`v3_exq_042_hippocampal_terrain_training_20260319T090529Z.json`):

```
hippo_mean_residue = 0.0      random_mean_residue = 0.392646      gap = +0.392646
```

**042's positive gap was entirely "hippocampal proposals evaluate to exactly zero
residue".** 042 ran 2026-03-19, two months before the **2026-05-17** support-preserving-CEM
defaults (`use_support_preserving_cem`, `support_preserving_stratified_elites`,
`support_preserving_ao_std_floor = 0.2`), whose own comment states the floor exists *"so the
sampling distribution cannot collapse to a point"*. That collapse is what put 042's proposals
off the residue support, and it was **deliberately retired as degenerate** -- CLAUDE.md
records it as the monostrategy that left SD-029 / ARC-062 Rung 2 / goal_pipeline /
self_attribution `non_contributory`.

On today's non-collapsing CEM, proposals stay on the visited manifold where residue actually
lives, while `generate_candidates_random` flings the state off that manifold into
never-visited (hence zero-residue) space. **The gap inverts for a structural reason and no
amount of warmup fixes it: 042's metric measures "did the proposals leave the residue
support", which the current substrate is specifically built not to do.**

Per the user's instruction -- *"if it still does not, stop and report the numbers rather than
queueing"* -- nothing was queued. Decision chip
**`chip-20260919-mech131-readiness-gate-inverts`**.

## What this implies for the DV itself, stated because it is the deeper issue

The same manifold argument applies to DV1. Residue is an RBF field over *visited* states, so
"low residue" and "off the visited manifold" are nearly the same measurement. A residue-
avoidance DV computed over rollout candidates will therefore always be partly a proxy for
novelty rather than for harm avoidance. That is not a coding defect; it is a property of
using a visitation-seeded residue field as the DV, and it is worth a governance-level look
before more compute goes into this claim.

**Banked and needing no redoing:** both lesion knobs (contract-pinned C1-C9); the warmup and
readiness-gate implementation; the within-subject lesion-at-eval design; every
`/queue-experiment` gate cleared with evidence; the ratified criteria; the full-scale cost
measurement (~9.6 h).

---

# ADDENDUM 2026-09-19 (3) -- OPTION B: requirement (1) satisfied, requirement (2) failed

**User decision OPTION B (2026-09-19T04:48Z)** implemented: DV re-operationalised onto a
harm-prediction readout; residue kept purely as the STORED quantity the two lesion knobs gate.
Landed in `ree-v3/experiments/v3_exq_1061_mech131_anticipatory_residue_lesion.py`. **Nothing
queued.**

## (1) Readout choice and liveness -- ESTABLISHED by measurement

Uses **`E3.harm_eval(z_world)`** (`harm_eval_head`), **not** `harm_eval_z_harm`. The
`z_harm_a` frozen-random-projection and `harm_obs_a` rank-2 hazards the decision flagged belong
to the **affective** stream (SD-086 / `zharm_a_p0_warmup`, ree-v3 `e10d6c5c`), which this driver
never touches -- checked, not assumed.

`harm_eval` is a random sigmoid head at init, so 042's BCE training (balanced harm/non-harm
`z_world` batches labelled by `info["transition_type"]`, every 8 steps, `Adam(lr=1e-3)` over
`main_params`) is mirrored here. **Optimizer coverage is asserted at runtime** -- the driver
refuses unless every `harm_eval_head` parameter is in the stepped optimizer, which is the
MECH-307 failure shape applied to a training path.

Measured at only 20 warmup episodes, ~250 BCE steps/seed:

| seed | mean harm_eval on harm states | on non-harm states | gap (needs > 0) |
|---|---|---|---|
| 11 | 0.6996 | 0.2531 | **+0.4466** |
| 23 | 0.6507 | 0.3360 | **+0.3147** |
| 37 | 0.6775 | 0.2982 | **+0.3793** |

A constant predictor scores exactly 0.0 whatever constant it emits, so this is literally
"beats a constant baseline". **The new readiness gate clears** -- and it replaces 042's
inverted `hippo_quality_gap` using an already-written rule (042's own calibration-gap
criterion), so no further decision was needed for the gate's form. 042's gap is still computed
and reported as the diagnostic that explains why the residue DV was abandoned (it stayed at
about -5.5).

## (2) Lesion effect vs between-candidate noise -- FAILS

With **all three** of 042's training components verified live -- terrain BC, harm_eval BCE, and
`world_forward` MSE at `wf_loss = 1.1e-4` over 496 steps:

| seed | ARM_1 intact | ARM_3 complete lesion | effect | between-candidate SD | effect/noise |
|---|---|---|---|---|---|
| 11 | 0.201039 | 0.201175 | +0.000137 | 0.008404 | **+0.0163** |
| 23 | 0.311395 | 0.311587 | +0.000192 | 0.013480 | **+0.0142** |
| 37 | 0.716806 | 0.716446 | -0.000360 | 0.005168 | **-0.0696** |

C1 clears 2/3 seeds and seed 37's effect is **negative**. The lesion moves the DV by ~1.5% of
the noise it must exceed. For context: the residue DV measured 0.035, and adding
`world_forward` training moved the harm DV from 0.0025 to 0.013 -- real progress, nowhere near
the ~1.0 a resolvable DV needs.

**`world_forward` was genuinely a binding constraint, just not the only one.** Before it was
trained, a 59% shift in the proposal mean under the CH1 lesion (`ao_mean` absmean
0.128819 -> 0.052828) produced candidate action objects (SD 0.011096 vs 0.011101), decoded
actions (0.044267 vs 0.044271) and world states (0.060645 vs 0.060672) identical to 4+ decimal
places -- with a world-state range of 42.5 against a mean magnitude of 1.97, the signature of
wild action-independent dynamics.

## Root cause: the channel lacks AUTHORITY, and the reason is load-bearing

    support_preserving_ao_std_floor = 0.2
    terrain_prior proposal-mean magnitude = 0.1288
    -> the mandated CEM exploration noise is 1.55x the entire anticipatory signal

That floor landed **2026-05-17** specifically "so the sampling distribution cannot collapse to
a point" -- it is the fix for the monostrategy that left SD-029 / ARC-062 Rung 2 /
goal_pipeline / self_attribution `non_contributory`. So it is not a bug to remove casually.

**On this substrate, at default CEM exploration settings, the anticipatory residue channels do
not have enough authority over the proposed candidate set for a lesion to be detectable through
any candidate-set DV.** That is a statement about the substrate's wiring and about MECH-131's
*testability*, not about the claim being false.

## Smallest design -- measured, per the decision's request

The readiness gate clears at **20 warmup episodes**, and 20 eps x 100 steps x 3 seeds runs in
**~10 min wall** with all three trainers live. 042's 600 x 200 (~15.7 h extrapolated) is
therefore **~30x more warmup than this design needs**. Size warmup off the gate, not off 042's
constant. This is the one piece of good news in this addendum: whatever comes next is cheap.

Decision chip: **`chip-20260919-mech131-channel-authority`**.

**Banked:** both knobs (contracts C1-C9); all three 042 trainers implemented and verified live;
the harm-prediction DV with runtime optimizer-coverage assertion; the working readiness gate;
the within-subject lesion-at-eval design; every `/queue-experiment` gate cleared; the ratified
ordinal criteria; and measured costs at both scales.

---

# ADDENDUM 2026-09-19 (4) -- OPTION A: guard REFUSED, authority hypothesis NOT supported

**User decision OPTION A (2026-09-19T09:25Z)** implemented: `support_preserving_ao_std_floor`
as a declared `config_slice` axis with levels `[0.2 production, 0.05 lowered]`; mandatory
`selected_action_entropy` guard that **self-routes** (no verdict about MECH-131) on collapse,
with the refusal threshold pre-registered at **0.25445 nats** -- the midpoint of V3-EXQ-567's
recorded 0.0124 (collapsed) and 0.4965 (healthy), stated as a midpoint because no already-written
rule fixes it. Same estimator and units as `exq643_modulatory_authority_baseline`. Landed in
`ree-v3/experiments/v3_exq_1061_mech131_anticipatory_residue_lesion.py`. **Nothing queued.**

18 cells (2 floors x 3 seeds x 3 arms), 20 eps x 100 steps, **29m47s**.

## Selected-action entropy (nats) -- the guard fired

| floor | seed 11 | seed 23 | seed 37 |
|---|---|---|---|
| 0.20 (production) | 0.1169 | 0.0000 | 0.0000 |
| 0.05 (lowered) | 0.0000 | 0.0000 | 0.0000 |

Identical across all three arms at each (floor, seed): **39/40 or 40/40 probe states commit the
same action.** Refusal floor 0.25445; healthy reference 0.4965.

## Lesion effect / between-candidate noise

| floor | seed 11 | seed 23 | seed 37 |
|---|---|---|---|
| 0.20 | +0.0032 | +0.0175 | -0.0630 |
| 0.05 | +0.0012 | +0.0071 | -0.0566 |

## What this shows

1. **The monostrategy is NOT caused by lowering the floor -- it is already present at the
   PRODUCTION floor 0.2.** So this is not the guard catching the risk the floor exists to
   prevent; it is the policy being degenerate at this scale regardless of the floor. The guard
   still refuses, correctly and as pre-registered.
2. **The authority hypothesis is NOT supported.** Lowering the floor 4x -- from 1.55x the
   terrain_prior proposal-mean magnitude (0.1288) to 0.39x it -- did not increase the lesion's
   measurable influence; if anything it decreased slightly. "Sub-dominant to exploration noise"
   was therefore not the binding explanation it appeared to be in addendum 3.
3. **Why no candidate-set DV can work here.** E3 commits the same action at essentially every
   probe state, so the committed action is not reading the candidate pool. While that holds, no
   DV over the proposed candidate set can register a lesion of the proposal mechanism --
   residue, harm prediction, or anything else. This **subsumes** the residue-manifold diagnosis
   (addendum 2) and the ao_std-floor diagnosis (addendum 3) rather than competing with them.

## Honest caveat, stated rather than papered over

This may be an **undertrained-policy artifact**. 20 warmup episodes is ~1/30th of 042's 600, and
V3-EXQ-567's healthy 0.4965 comes from a full-scale run. The policy may diversify with more
warmup and the DV may become resolvable. That was **not** tested: 6 cells at 042 scale
extrapolates to ~30 h. Distinguishing the two possibilities needs either that run, or a cheap
**policy-diversity readiness gate** placed ahead of the DV and swept over warmup scale in
~10-min increments to find where entropy clears.

## Disposition

Per the decision's own stop condition -- *"if it still does not, STOP and report ... the honest
answer is your option C"* -- the recommended disposition is **option C**, refined by this probe:
MECH-131's mechanism is **implemented and activated but has no measurable authority over
committed selection at tested scale**, and the proximate blocker is a degenerate policy, not the
residue representation and not the exploration floor. Decision chip
**`chip-20260919-mech131-monostrategy-precondition`**.

**Banked:** both knobs (contracts C1-C9); all three 042 trainers; the harm-prediction DV with
runtime optimizer-coverage assertion; the working harm-calibration readiness gate; the
monostrategy guard with a pre-registered, derivation-documented threshold; the floor axis; the
within-subject lesion-at-eval design; every `/queue-experiment` gate cleared; ratified ordinal
criteria; and measured costs at three scales (10 min / 16 min / 30 min per probe shape).

---

# FINAL ADDENDUM 2026-09-19 (5) -- DISPOSITION: registered, compute stopped

**User decision OPTION C (2026-09-19T21:39:15Z, real `AskUserQuestion` via Orchestrator
`orchestrate-20260919-2125`)** on `chip-20260919-mech131-monostrategy-precondition`: register the
finding and stop spending compute. **No experiment was ever queued for MECH-131 by this line of
work**, by decision at each of four stops. This addendum closes the series.

## The disposition, as recorded

> MECH-131's mechanism is **IMPLEMENTED and ACTIVATED** -- contracts C1-C9 prove both
> anticipatory channels are live and that the post-hoc path stays intact under lesion -- but it
> has **NO MEASURABLE AUTHORITY OVER COMMITTED SELECTION** at tested scale. The proximate blocker
> is a **degenerate policy**: E3 commits the same action at 39-40 of 40 probe states, at BOTH the
> production and the lowered exploration floor. It is **not** the residue representation and
> **not** the exploration floor. The **undertrained-policy caveat is stated as untested**: 20
> warmup episodes against V3-EXQ-042's 600, with the healthy entropy reference (0.4965 nats)
> coming from a full-scale run; settling it would cost ~30 h at 6 cells and was not spent.

This is a **citable partial answer** to MECH-131, not a null. The claim asserts that residue must
be activated as an anticipatory pre-candidate-generation bias; V3 does activate it, on two
independent channels, and the activation is contract-pinned. What the probes could not establish
is that the activation *reaches committed behaviour* at any scale we were willing to pay for.

## The four stops, in order -- each a user decision, none a failure

| # | Stop | What was measured | Outcome |
|---|---|---|---|
| 1 | Lesion completeness (addendum 1, chip `...lesion-completeness`) | CH1-only lesion leaves CEM score spread at 0.892, unchanged -- the pre-flight's single knob was not a lesion | OPTION C: build the second knob. Landed. |
| 2 | Evidential bar (chip `...evidential-bar`) | MECH-131 has no `what_would_answer`; EXP-0847 sets `require_pre_registered_thresholds: false` | DIAGNOSTIC, ordinal criteria, >= 3 seeds |
| 3 | Untrained substrate (chip `...untrained-substrate`) | Residue DV effect/noise 0.01 untrained, 0.035 warmed -- 042 says "if terrain_prior is random, proposals are uninformed" | OPTION A: 042's warmup + readiness gate |
| 3b | 042's gate inverts (chip `...readiness-gate-inverts`) | 042's own +0.3926 gap was `hippo_mean_residue == 0.0` under the pre-2026-05-17 collapsing CEM, retired as degenerate | OPTION B: harm-prediction DV |
| 4 | Channel authority (chip `...channel-authority`) | `ao_std_floor` 0.2 is 1.55x the 0.1288 proposal-mean magnitude | OPTION A: floor as an axis + entropy guard |
| 5 | Monostrategy precondition (chip `...monostrategy-precondition`) | Entropy 0.0-0.117 nats at BOTH floors; lowering the floor 4x did NOT raise effect/noise | **OPTION C: register, stop** |

Two of these stops corrected an earlier diagnosis of my own: the `ao_std`-floor explanation
(addendum 3) was superseded by the monostrategy finding (addendum 4), and 042's readiness gate --
which stop 3 adopted on instruction -- turned out to rest on a retired degenerate regime. Both
corrections came from measurement, not review.

## What was banked (all landed on origin, all default-preserving)

- **Two lesion knobs**, `ree-v3` `origin/main`: `HippocampalConfig.terrain_prior_residue_channel_enabled`
  (CH1, the `terrain_prior` residue channel) and `score_trajectory_residue_terrain_enabled`
  (CH2, `_score_trajectory`'s residue terrain score, gating BOTH its z_world and pre-SD-005
  z_self reads). **Both default `True` = bit-identical to the pre-instrument substrate**; the
  lesion is opt-in. Zeroing is out-of-place and preserves `terrain_input_dim`.
- **9 contracts**, `tests/contracts/test_mech131_terrain_prior_residue_channel.py`: C1/C7
  `from_dims` reachability (the MECH-307 swallowed-kwarg shape), C2/C9 default bit-identity,
  C3 CH1 liveness, C4 storage untouched, C5 post-hoc scorer untouched, C6 CH1-alone scope pin,
  C8 the COMPLETE two-channel lesion with storage and post-hoc both pinned live. Plus both flags
  registered in `tests/test_flag_inertness.PROBED`.
- **Substrate record**: `ree-v3/docs/substrate/MECH-131-terrain-prior-anticipatory-residue-channel-lesion.md`
  with the SCOPE table, indexed in `ree-v3/CLAUDE.md`.
- **The driver**, `experiments/v3_exq_1061_mech131_anticipatory_residue_lesion.py` -- unqueued and
  carrying its own status banner. Reusable parts: all three of 042's trainers (terrain BC,
  `harm_eval` BCE, `world_forward` MSE) with a **runtime optimizer-coverage assertion**; the
  harm-prediction DV; the harm-calibration readiness gate ("beats a constant baseline", gap > 0);
  the **monostrategy guard** with its pre-registered 0.25445-nat threshold; the `ao_std_floor`
  config_slice axis; and the within-subject lesion-at-eval design.
- **Cleared `/queue-experiment` gates, with evidence**: 2.5/2.5a substrate (built + probed),
  2.5b re-derive brake (0 across 523 autopsy artifacts), 2.5c substrate-path overlap (all four
  open `corrupting` entries measured inert at this config, with the specific defaulted flags
  named and asserted at runtime), 2.4 GOV-REUSE-1 (not recoverable), 2.6 ethics (`allow`).
- **Measured costs**, for whoever sizes the next attempt: ~10 min (3 cells, 12 probe states),
  ~16 min (harm DV), ~30 min (18 cells, 40 probe states); 042-scale extrapolations ~15.7 h at
  3 cells and ~30 h at 6.

## The precondition any future MECH-131 falsifier must clear first

**Establish policy diversity BEFORE measuring any candidate-set DV**: selected-action entropy
>= **0.25445 nats** (the pre-registered threshold, the midpoint of V3-EXQ-567's recorded 0.0124
collapsed / 0.4965 healthy, same estimator and units as
`experiments/_lib/baselines/exq643_modulatory_authority_baseline.py`). Until that clears, E3's
committed action does not vary with the candidate pool, and **no** DV over proposed candidates can
register a lesion of the proposal mechanism -- which is why the residue-manifold (addendum 2) and
`ao_std`-floor (addendum 3) diagnoses are subsumed rather than competing.

The cheapest unspent route to closing the untested caveat, if it is ever wanted: sweep warmup
scale (20 / 60 / 180 episodes, one floor, one seed) against that entropy gate alone, ~30 min, to
find whether and where diversity appears. Declined here as part of OPTION C.

## Registry action

Raised as a **`governance_flag.py` entry against MECH-131** (`stale_note`) carrying this
disposition and the precondition, so `/governance` can attach it to the claim and author
MECH-131's missing `what_would_answer`. **`claims.yaml` was deliberately NOT edited by this
session** -- the only claims.yaml change in this whole line of work is the factual
`implementation_note` added on 2026-09-18 recording the instrument, which remains accurate.
Work chip `chip-proposal-exp-0878-paced` resolved **`withdrawn`**: no experiment landed via it,
by decision.
