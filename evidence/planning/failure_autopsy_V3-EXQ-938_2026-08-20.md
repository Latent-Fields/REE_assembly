# Failure autopsy -- V3-EXQ-938 (ARC-070 / MECH-321 PE-selectivity, rate-matched yoked, whole-episode)

- **Generated (UTC):** 2026-08-20T02:39:17Z
- **Scope:** single
- **Status:** confirmed (user gate 2026-08-20)
- **Session:** failure-autopsy-multi-20260819
- **Dry-run gate:** manifest checked, top-level `dry_run` absent -- not a smoke.

## 1. Facts

`v3_exq_938_arc070_mech321_pe_selectivity_yoked_wholeepisode_20260818T215558Z_v3`
-- FAIL, self-stamped `evidence_direction: weakens` on both `claim_ids`
(`evidence_direction_per_claim` = `{ARC-070: weakens, MECH-321: weakens}`),
label `pe_selectivity_refuted_rate_matched_wholeepisode`, `non_degenerate: true`,
machine `ree-worker-1`, elapsed 49455 s (13.7 h).

### The load-bearing criterion

`C1_PE_SELECTIVITY_IMPROVES_OUTCOME` -- load-bearing, **failed**:
measured **-0.001338403**, threshold 0.0.

Statement, verbatim: *"Over ALL measured seeds (no screen, no tiering, no post-hoc
selection, no occupancy gate), the unconditional whole-episode mean harm signal is
LESS harmful under decomposition placed at top-20% forward-PE loci (ARM_PE) than
under the SAME per-episode amount of decomposition placed at PE-uninformative loci
(ARM_YOKED), by an effect exceeding 1.0 x SE over >= 40 paired seeds.
PRE-DECLARED NULL: a delta <= 0 within that bound REFUTES ARC-070's
prediction-failure-selectivity leg at this grain. Both directions are verdicts."*

### This is a clean run -- the execution is not in question

| readout | value | reading |
|---|---|---|
| n_seeds | 40 (min required 40) | floor met exactly |
| harm delta (PE - YOKED) | -0.001338 | |
| sd / SE | 0.017481 / 0.002764 | **t = -0.484** |
| seeds negative / positive | **19 / 17** | a coin flip |
| MDE at 80% power, alpha .05 | ~0.007739 | observed \|delta\| is **17.3% of MDE** |
| `rate_match_ok` | true, arm_rel_gap **0.0185**, 0 seeds outside tol | the rate matching WORKED |
| `aa_control_ok` | true, max_abs_delta **0.0** | A-A null control bit-identical |
| `forced_fires_min` | **91** on both ON arms | the manipulation FIRED |
| `boundary_fires_mean` | 276.95 (PE) / 287.325 (YOKED) | decomposition occurred throughout |
| `decomposed_max_off_arm` | 0.0 | OFF arm is a true structural zero |
| all 15 readiness preconditions | met | |

**This is a null, cleanly measured -- not a detected negative effect.** The
pre-declared null's condition (delta <= 0 within 1.0 x SE) is satisfied exactly as
written, so the run delivered the verdict it promised. It is also the **first run
in this six-run chain to reach any verdict at all**: 816/820 died on a
`vs_heterogeneity_low_vs_steps_present` gate at 0.0/5.0, and 816b/816d saturated
the environment axis within 0.0007 across two escalations.

### Secondary readouts worth carrying

- `secondary_fwd_pe_delta_yoked_minus_pe` = **-2.6e-05** -- the proximal readout did
  not move either. Decomposition at high-PE loci did not reduce forward-PE there.
- `C2_DECOMPOSITION_PER_SE_VS_OFF` (non-load-bearing) = **-0.03681** -- decomposition
  *per se* is associated with ~27x the harm delta that selectivity is, in the
  harmful direction. Not adjudicated here (no SE reported for it, and it cannot
  separate selectivity from decomposition per se, which is why it is not
  load-bearing), but it is the larger signal in the manifest and should not be lost.

### Provenance defect

`substrate_stable_across_run: **false**`. `per_cell_hashes_disagree: false` -- all
132 cells share one hash `3a9826d0...`, so the run was internally consistent -- but
`process_snapshot_drift` records `on_disk_now: a0abd50e...` and the stated
`substrate_commit` is `839ffe03`, which does not correspond to the hash actually
used (lag 49112 s). **We cannot map this run to a substrate commit.** That is
recording-debt, not a validity defect: the run used one substrate throughout.

## 2. Claim-layer mapping -- the decisive question

### ARC-070's own registered falsifier EXCLUDES this DV class

`claims.yaml` ARC-070 `what_would_answer`, verbatim (53865-53869):

> **EXPLICITLY NOT FALSIFYING:** a failure of the DOWNSTREAM task-level benefit
> (decomposition fires but does not reduce harm/improve reward, as V3-EXQ-844's C1
> and the V3-EXQ-867/867a/867b family found) does not by itself falsify ARC-070 --
> that is MECH-321's separate, narrower functional claim about the QUALITY of
> harm-aware selection among re-tiled candidates, not about whether re-segmentation
> occurs at all.

And its actual FALSIFYING clause (53859-53863) is the *opposite* of what happened:

> FALSIFYING: ... the WITH-ARC-070 agent nonetheless commits blind and executes the
> ungrounded remainder ... even though its own trigger condition ... is genuinely
> met -- **the mechanism does not engage when it architecturally should.**

938's DV is a whole-episode mean harm signal -- squarely the excluded class -- and
the mechanism **demonstrably engaged** (>=91 forced fires per arm, ~277-287 boundary
fires per arm). ARC-070's registered falsifier is not merely unmet; the run
evidences its negation.

### The tension this exposes, and it is a real governance question

Two authorities are on record and they disagree:

- **`govdiag1_repose_mech321_chain_2026-08-12.md` section 5f** pre-declares that a
  null "REFUTES ARC-070's prediction-failure-selectivity leg **at this grain**".
- **`claims.yaml` ARC-070 `what_would_answer`** says downstream task-benefit failure
  does not falsify ARC-070.

These are reconcilable if 5f is read as scoping a *leg at a grain* rather than the
claim -- which is exactly what its own words say, and what the whole document says
of itself: *"This document promotes and demotes nothing."* A blanket `weakens`
applied to ARC-070 is what over-reaches, not the pre-registration.

**An experiment's pre-declared null defines what the EXPERIMENT concludes. It
cannot unilaterally widen a claim's registered falsifier.** Surfaced to governance
rather than settled here.

### The alive measurement rival the run cannot exclude

`hypothesis_space_registry.v1.json`, `policy_decomposition_discrimination`, carries
**`H-representation-axis` as `alive`**: *"forward-PE as currently computed is too
coarse-grained to register the environment's actual uncertainty."*

938's forward-PE delta of -2.6e-05 is precisely what that hypothesis predicts. A
within-run rank normalisation (938's design) does not fix a readout that is too
coarse -- ranking a coarse signal leaves it coarse. **So 938 cannot discriminate
"selectivity is false" from "the PE readout cannot locate the loci where
decomposition would help."** The same question's `H-vs-proxy-saturation` is already
`confirmed` (region-V_s saturating at 0.9338 with 0 of 1654 low-V_s steps, spearman
0.083 vs a 0.2 coupled floor), which is the established precedent that this
campaign's readouts have been the problem rather than the mechanism.

### MECH-321 is the weaker fit of the two

- MECH-321 is *"the QUALITY of harm-aware selection among re-tiled candidates"*.
  938 tests **placement** selectivity (where decomposition goes), not selection
  quality among candidates.
- MECH-321's declared PRIMARY trigger is the V_s drop, and `claims.yaml` records
  `arm1_vs_trigger_total = 0` across the whole campaign -- **it has never fired
  once**. 938 deliberately uses forward-PE instead, per the re-pose.
- MECH-321 already carries `pending_retest_after_substrate: true` awaiting
  `SD-hazard-aware-policy-decomposition`, and the V3-EXQ-919 autopsy (2026-08-13,
  user-confirmed) routed `implement-substrate/amend` with an explicit *"Do not
  re-queue the magnitude-only design under a new letter."*
- `claims.yaml` records the substrate finding that the decomposition step *"read no
  harm-valence signal and performs no ranked selection among candidate re-tilings
  at all"*. A harm-outcome null from a mechanism with no harm input is an
  implementation gap, not claim evidence.

## 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment (ARC-070) | **intact** | DV class explicitly excluded by the claim's own falsifier; mechanism engaged, which is the negation of its FALSIFYING clause. |
| Claim alignment (MECH-321) | **unclear** | Tests placement, not selection quality; uses a trigger that is not MECH-321's declared primary; harm-valence input found absent in substrate. |
| Biological reference | clear | Zacks 2007 event-segmentation theory (PE as canonical boundary trigger), Schapiro 2017 pattern separation, Pfeiffer & Foster 2013 forward sweeps. Not a formal-definition import for the primary trigger; the McGovern-Barto bottleneck path is an acknowledged import and is not what 938 tests. The run does not bear on translation fidelity either way. |
| Prerequisites | **present** | Mechanism fired (91 forced, ~280 boundary). SD-084 mid-execution handle validated by V3-EXQ-839. |
| Implementation | complete | For what was tested. Rate-matching verified at 1.85% gap. |
| Environment | adequate | The env-underdrives-uncertainty leg is `superseded`; forward-PE was heterogeneous (`pe_var_best` 8.64e-7 vs a 1e-9 floor). |
| Measurement | **under-instrumented** | `H-representation-axis` alive and unexcluded; forward-PE delta -2.6e-05 is consistent with a readout too coarse to locate the loci. |
| Integration | n/a | |
| Scale / capacity | **adequate** | n=40 met exactly; MDE ~0.0077; observed 17.3% of MDE. Powered for its pre-registered band. |

### Failure-location summary (GOV-FAILLOC-1)

- **MECHANISM FAILED:** not_established -- it fired; selectivity benefit not demonstrated.
- **MEASURES FAILED:** **established** -- `H-representation-axis` alive and unexcluded.
- **ENVIRONMENT FAILED:** not_established.
- **REE FAILED:** false.

**Net classification: MIXED -- not chargeable to REE.** Reaching "REE FAILED" would
require measurement to read adequate, and it does not.

## 4. Recurrence

- Re-derive brake: **does not fire.** ARC-070 ceiling hits 0, MECH-321 ceiling hits 1,
  against a threshold of 2. Independently matches the queue note's own count.
- Granularity-debt trigger: **does not fire.** No target reads `weakened` in either
  claim's cluster; the reader's own verdict is *"measurement or implementation debt,
  NOT granularity debt"*.
- Chain shape: six prior runs, of which four (816, 816b, 816d, 820) died on
  instrument/occupancy gates and two (816c, 830) returned instrument findings. The
  recurrence is **not** the claim being re-tested at one granularity -- it is a
  campaign that has never had a working readout. That is why the correct response to
  938 is not a demotion and not another letter.

## 5. Routing -- CONFIRMED at the user gate (2026-08-20)

**`governance`**, applying a SCOPED per-claim disposition, not the stamped blanket
`weakens`.

- **ARC-070 -> `non_contributory`** (not `weakens`, not `mixed`). Record the
  selectivity-leg null AT THIS GRAIN in the note, honouring the pre-registration,
  while declining the claim-level weakens against the claim's own registered
  exclusion. `epistemic_category` stays `standard`.
- **MECH-321 -> `non_contributory`.** Keep `pending_retest_after_substrate: true`
  and the standing V3-EXQ-919 routing to `SD-hazard-aware-policy-decomposition`.
  `epistemic_category`: MECH-321 currently has **no** `epistemic_category` field at
  all; recommend `standard` so GOV-CAT-1 has something to read.
- **Surface the 5f-vs-`what_would_answer` conflict to governance** as its own
  decision item. It is not this autopsy's to settle, and it will recur on the next
  run in this chain.
- **REFUSE** a fourth environment-axis escalation and any re-queue keyed on
  region-V_s as the prediction-failure readout -- both already standing refusals
  from govdiag1 section 6, unaffected by this result.
- **Do NOT queue a lettered successor to 938 on the strength of this null.** The
  live question is now whether the forward-PE readout can locate the loci at all
  (`H-representation-axis`), which is a *measurement* question and needs a readout
  spike, not another outcome comparison.
- `recommended_substrate_queue_entry.action: "none"` -- govdiag1 section 8 already
  established that no substrate build is warranted by this chain (*"the substrate
  fires the mechanism ... the defect was in the question, not the code"*), and 938
  confirms the firing directly.
- **Recording-debt owed:** the successor must resolve `substrate_stable_across_run`
  so the run maps to a commit. Cite `experimental_recording_standard_2026-07-12.md`.

## 6. Closure-plan node

`policy_decomposition_trigger:REPOSE` (`owner_exq: V3-EXQ-938`, status
`in_progress` since 2026-08-18) **advances but does not close.** Its
`resume_condition` says it "advances/closes on the V3-EXQ-938 RESULT" and that both
directions are verdicts -- so the node has its result. What it does not have is a
claim-layer disposition, because the null's scope is narrower than the node's
framing assumed.

Three stale artifacts to correct, all downstream and all mechanical:
- the node's blocker *"queued in git but not yet coordinator-registered"* is stale --
  the run executed and landed a manifest;
- `closure_status.md:63` and `morning_agenda.md:200,212` still show the node `open`/0%;
- the node's history sidecar does not yet carry the 938 manifest.

## 7. Learning extracted

1. **A claim's registered `what_would_answer` is the authority on what falsifies it.**
   A pre-declared null in a planning document scopes what the *experiment* concludes;
   it cannot widen the claim's falsifier. When the two disagree, the artifact must
   surface the conflict rather than silently take the wider reading -- which a
   blanket `weakens` stamp does.
2. **A null cannot eliminate a hypothesis that predicts it.** `H-representation-axis`
   was alive before this run and remains alive after it; 938's own proximal readout
   (forward-PE delta -2.6e-05) is that hypothesis's signature.
3. **"Well-powered" is relative to a declared band, not to any effect.** 938 met its
   n=40 floor and its pre-declared 1-SE band, but a 1-SE equivalence band is a weak
   bound: an effect between 1 and 2.8 SE would be neither detected by C1 nor excluded
   by the null. Record what the run could and could not have seen.
4. **The first run in a chain to reach a verdict deserves its verdict recorded even
   when the claim-layer disposition is narrower than the label suggests.** 938 is a
   genuine methodological advance over six predecessors; the scoping here is not a
   criticism of the design.
