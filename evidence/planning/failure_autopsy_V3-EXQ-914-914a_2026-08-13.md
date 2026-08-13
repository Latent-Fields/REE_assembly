# Failure Autopsy: MECH-236 hippocampal z_goal-injection channel cluster (V3-EXQ-914 + V3-EXQ-914a)

Generated: `2026-08-13T04:52:40Z`
Scope: cluster (predecessor + corrected successor, same claim, same lineage)
Status: confirmed

## Trigger

`pending_review.md`'s "Reviewed FAIL with no confirmed autopsy (blind-spot net)" flagged
`v3_exq_914_mech236_hippocampal_zgoal_channel_ablation_20260811T055126Z_v3` (V3-EXQ-914):
already marked reviewed with a rich `evidence_direction_note`, but no confirmed
`/failure-autopsy` artifact. Its corrected successor, V3-EXQ-914a, is a plain FAIL still
awaiting adjudication (`self-route is a hypothesis, not a verdict`). Both are claim-tagged
`MECH-236` only, sharing lineage (914 -> 914a per EXQ versioning/supersession policy), so run
as one cluster autopsy.

Pre-flight: two other pending FAIL candidates from the same `pending_review.md` sweep already
had confirmed autopsies not yet reflected there (V3-EXQ-910a/MECH-489, confirmed
2026-08-11; the MECH-266/SD-032a 464e/467e cluster, confirmed and committed
`783465c02b` minutes before this session started) -- `/failure-autopsy` does not mark
`review_tracker.json` reviewed, so their presence in `pending_review.md` does not mean they
lack an autopsy. Dry-run citation check (`check_dry_run_citations.py`) on both 914 and 914a:
clean, neither is a smoke. Recording standard (`validate_recording.py`): both complete, no
always-core gaps. Granularity-debt cluster for MECH-236: 0 tagging targets (this is the FIRST
autopsy ever run against this claim) -- trigger does not fire. Re-derive brake: N/A (first
occurrence; and this diagnosis does not read toward `substrate_ceiling` -- see below).

## 1. Facts

### V3-EXQ-914 (2026-08-11T05:51:26Z) -- superseded, instrument defect

`outcome: FAIL`, `evidence_direction: superseded` (already set on the manifest before this
autopsy). The manifest's own `evidence_direction_note` (written prior to this session, likely
during triage) documents: this run executed against a script snapshot a read-modify-write race
in the shared `ree-v3` checkout committed to `origin/main` at `bfda4c95df` -- a mid-edit version
using a **periodic** anchor-write trigger (every 8 ticks, `GRID_SIZE=8`) rather than the
corrected **proximity-gated** trigger (`ANCHOR_PROXIMITY_THRESHOLD`, `GRID_SIZE=16`) that landed
moments later at `1388f4061c`. The current script's own docstring documents, from a direct probe
of exactly this periodic-write version, that it produces a NEGATIVE/misleading proximity gap:
the ghost-probe channel seeded candidates toward stale, arbitrarily-timed past locations rather
than genuinely goal-relevant ones, actively steering the agent AWAY from the resource. Measured:
`c_main_gap_mean = -0.0265` (ARM_OPEN below ARM_CLOSED), consistent with the defect. Re-queued
as V3-EXQ-914a per the versioning policy. Correctly excluded from MECH-236 scoring
(`evidence_direction: superseded` is treated as inactive by the indexer).

This autopsy **ratifies** that existing diagnosis rather than re-investigating: it is a
genuine, well-documented instrument defect (a race between two concurrent commits), not a
claim-layer finding. No new work is owed here beyond formalizing it in a confirmed autopsy
artifact so the blind-spot net clears.

### V3-EXQ-914a (2026-08-11T06:59:11Z) -- weakens (per manifest self-route), clean test

`outcome: FAIL`, `evidence_direction: weakens` (manifest self-route). `queue_id: V3-EXQ-914a`.
Corrected script (proximity-gated anchor writes, `GRID_SIZE=16`). Both preconditions met:

- P1 `mech293_ghost_branch_live`: measured 0.0 (worst cell `ARM_OPEN/seed46`) vs threshold 0.0,
  `met: true` -- but see "Measurement adequacy" below; this threshold passes even a seed with
  literally zero engagement.
- P2 `zgoal_formed_comparably_closed_and_open`: measured 0.3138 (worst) vs threshold 0.1,
  `met: true`.

Load-bearing criterion `C_MAIN_open_beats_closed_resource_proximity`: **FAILED**.
`c_main_gap_mean = 0.0032` (need >= 0.015 PROXIMITY_GAP_FLOOR on >= 3/5 seeds; actual
`c_main_seed_pass_fraction = 0.2`, i.e. 1/5). `criteria_non_degenerate.C_MAIN = true`
(non-degenerate per the manifest's own gate).

Per-seed gaps (open - closed mean_resource_proximity), reconstructed from `per_seed_rows`:

| seed | nogoal | closed | open | gap | ghost_admitted_mean | n_latched_ticks |
|---|---|---|---|---|---|---|
| 42 | 0.6703 | 0.6703 | 0.6592 | -0.0110 | 3.143 | 118 |
| 43 | 0.6651 | 0.6651 | 0.6108 | -0.0543 | 2.972 | 334 |
| 45 | 0.5278 | 0.5278 | 0.5987 | +0.0708 | 0.750 | 94 |
| 46 | 0.5593 | 0.5593 | 0.5593 | **0.0000** | **0.000** | 76 |
| 47 | 0.4736 | 0.4736 | 0.4844 | +0.0108 | 0.789 | 207 |

`nogoal == closed` bit-identical on every seed -- confirms the driver's own calibration
finding (deterministic seeding + `wanting_weight=0` means z_goal existing-but-unweighted has
literally no behavioural channel). Seed 46's ghost branch never admitted a single candidate
across the whole run (`ghost_admitted_mean = 0.000`), so its `gap = 0.0000` is not "no effect
measured", it is "no channel activity to measure" -- a structurally uninformative data point
that the P1 gate (threshold >= 0.0) nonetheless counts as passing and includes in the 5-seed
C_MAIN denominator.

## 2. Claim mapping

**MECH-236** (`docs/claims/claims.yaml`): "Hippocampal trajectory proposals must be conditioned
on a goal signal (z_goal) injected from E3 via a dedicated input channel; without this
conditioning, the hippocampal module generates only position-based trajectories and cannot
produce goal-directed navigation toward target states." `status: candidate`,
`implementation_phase: v3`, `depends_on: [MECH-230, ARC-007, SD-004]`.

The driver's docstring (`ree-v3/experiments/v3_exq_914_mech236_hippocampal_zgoal_channel_ablation.py`,
lines 1-64) makes a code-verified case for claim-tag accuracy: a source grep of
`ree_core/agent.py:REEAgent._e3_tick` (~5437-5520) shows `current_z_goal` is threaded into
`HippocampalModule.propose_trajectories(current_z_goal=...)`, whose SOLE consumer is the
MECH-293 waking ghost-goal-probe branch, gated on `use_mech293_ghost_probes`
(default False) -- "the only call site in the current substrate where the raw z_goal tensor...
reaches trajectory PROPOSAL." The docstring also pre-emptively addresses and rejects the
"wanting_weight pathway" as the tested channel (its writer is `benefit_exposure`-driven, a
separate signal from `GoalState.z_goal` itself), holding `wanting_weight=0.0` in every arm to
isolate "the literal z_goal-injection channel". **This isolation choice is the crux of the
diagnosis below**: it is defensible as a scoping decision to avoid conflating two signal
sources, but it removes the only scoring-layer mechanism connecting the tested channel to
actual candidate selection (see Section 4).

Claim tagging verdict: **legitimate**, not inherited/stale. This is the first-ever V3
experimental run against MECH-236 (0 prior genuine_exp_count per the driver's own GOV-REUSE-1
check).

## 3. Biological-reference triage

Closest mammalian reference (already in `claims.yaml`'s `literature_evidence`):

- **Ito et al. 2015** (Nature, DOI 10.1038/nature14396): mPFC input via nucleus reuniens is
  causally required for trajectory-dependent CA1 firing during goal-directed navigation in
  rodents; disconnecting the prefrontal goal signal collapses CA1 activity to position-encoding
  only.
- **Yu et al. 2026 / Tang et al. 2026** (Nat Neurosci, added 2026-08-09 addendum): hippocampal
  theta sweeps form vectors toward remembered goal locations INDEPENDENT of current movement/
  head direction, with stronger goal-modulation preceding correct navigational choices.

Both citations describe a **continuous, online modulation** of ongoing trajectory-dependent
firing / theta-sweep content by a goal signal -- not a sparse, minority-budget candidate
injection. `lit_status: present` (already grounded; no `/lit-pull` needed).

**Is the REE mechanism a faithful translation, or a formal/structural stand-in?** The
MECH-293 ghost-probe channel (`mech293_ghost_fraction=0.2` -- a 20% minority probe budget
seeded around top-ranked MECH-292 bank entries) is a considerably sparser, more indirect
mechanism than continuous goal-vector biasing of ongoing trajectory generation. That gap alone
would be worth noting, but the decisive finding (Section 4) is not about sparsity -- it is that
the mechanism, as configured in this run, has **no functional consequence pathway at all**
regardless of how much candidate-injection occurs.

## 4. The load-bearing finding: CEM elite-selection is goal-blind under this configuration

Traced `HippocampalModule._score_trajectory` (`ree_core/hippocampal/module.py:1513-1578`), the
scoring function used both for CEM-refit ranking of ghost-mixed candidates
(`_mix_value_flat_with_ghost` -> `_score_trajectory` at line 2365-2367) and for the eventual
action-selection scoring (`agent.py:11415/11432/11449`):

```
terrain_score = residue_field.evaluate_trajectory(world_seq)        # ARC-007 STRICT, terrain-only
if wanting_weight > 0:  terrain_score -= wanting_weight * mean(VALENCE_WANTING)   # goal/benefit term
if curiosity_weight > 0: terrain_score -= curiosity_bonus(...)                    # unrelated
```

Three checks against this driver's actual configuration:

1. **`wanting_weight = 0.0`** in every arm (driver's deliberate isolation choice, Section 2) --
   the ONLY term in `_score_trajectory` that would translate goal/resource-relatedness into a
   candidate-selection preference is switched off.
2. **`benefit_terrain_enabled`** defaults `False` (`ResidueConfig`, `ree_core/utils/config.py:2384`)
   and is never set by `_make_agent` -- the second potential reward-linked terrain channel
   (ARC-030/MECH-117 "liking" terrain) is also off.
3. **`NUM_HAZARDS = 0`** in this driver (deliberate, to avoid an untrained-agent death confound
   documented in the docstring) -- so the one remaining term, the ARC-007 residue field, is
   fundamentally a harm-accumulation mechanism ("Harm adds to residue, never subtracts",
   `ree_core/residue/field.py:395`) with **nothing to accumulate** in a hazard-free environment.

Net: in this configuration, `_score_trajectory` has **no functional connection to
resource-benefit or goal-relatedness whatsoever**, identically in both ARM_CLOSED and
ARM_OPEN. Opening the ghost-probe channel changes which candidates are PROPOSED (more seeded
near a resource-proximal anchor) but not how they are SCORED -- scoring is content-blind to
exactly the property (goal-relatedness) the channel is supposed to inject. Any residual effect
on `mean_resource_proximity` can only come from a weak compositional/base-rate effect (more
resource-proximal candidates in the pool marginally raises the chance one gets picked under
otherwise-noisy tie-breaking among near-flat, untrained-neural-field scores) -- consistent with
the small, mixed-sign, noisy per-seed gaps actually observed (Section 1).

This is not a one-off idiosyncrasy of this driver. `substrate_queue.json`'s
`modulatory-bias-selection-authority` entry (status `implemented`, `ready: true`) documents an
extensively-confirmed, related pattern at a different call site (`E3.select`, not hippocampal
CEM refit): "modulatory/secondary score-bias channels are added to candidate scores... but are
dominated by the primary harm/goal score term, so they never change argmax" -- explicitly
"mirrors the z_goal-vs-harm salience gap (603e/626a/622)". That fix addresses E3's FINAL
action-selection authority; it does not reach into the hippocampal CEM's own internal
elite-selection/refit step, which happens BEFORE candidates ever reach E3 -- a goal-blind
refit could discard a genuinely more resource-proximal ghost-seeded candidate before E3 ever
sees it, independent of E3's own (already-fixed) selection authority. The substrate DOES already
have the lever that would close this gap at the hippocampal level -- `wanting_weight > 0` -- it
is simply held at zero by this driver's deliberate isolation choice. **This is a test-design
matter, not a missing-substrate matter**; see routing below.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened, with caveat | test let the claim partially express itself (channel fires, z_goal forms comparably) but selection scoring structurally cannot act on the injected signal under this configuration |
| Biological reference | clear | Ito 2015 (mPFC->CA1 causal requirement) + Yu/Tang 2026 (continuous theta-sweep goal-vectors); both describe continuous modulation, REE mechanism is sparser (20% minority probe budget) -- a secondary note, not the decisive issue |
| Developmental/dependency prerequisites | present | MECH-230 (z_goal formation) held constant/intact by design; confirmed via P2 |
| Implementation completeness | **partial** | ghost-probe channel proposes candidates correctly (P1/P2 both met); no scoring pathway lets that proposal-stage goal-relatedness survive CEM elite selection, given `wanting_weight=0` + `benefit_terrain_enabled=False` |
| Environment adequacy | partial | `NUM_HAZARDS=0` (deliberate, avoids a documented untrained-agent death confound) inadvertently removes the residue field's only signal source, given ARC-007 STRICT is a harm-accumulation mechanism |
| Measurement adequacy | **under-instrumented** | C_MAIN is close to structurally guaranteed null in this configuration, independent of MECH-236's truth; P1's threshold (>= 0.0, "lower") passes even seed 46 where the channel had zero engagement all run, which is then still counted in the 5-seed denominator |
| Integration adequacy | isolated | z_goal formation (MECH-230), the ghost-probe channel (MECH-293), and CEM scoring (`_score_trajectory`) are each individually functioning as coded, but the pipeline connecting them end-to-end has a dead link at the scoring step under this config |
| Scale/capacity | untrained E1/E2 throughout (deliberate) | defensible as an architectural-coupling test in principle; likely contributes to the noise floor on top of the scoring-blindness issue |

### Failure-location summary (GOV-FAILLOC-1)

- **MECHANISM FAILED**: not established (Implementation reads `partial`, not `complete` --
  the ghost-probe channel itself works as coded; the gap is downstream of it)
- **MEASURES FAILED**: **established** (Measurement reads under-instrumented; the load-bearing
  criterion is structurally close to a guaranteed null under this configuration, independent of
  substrate correctness)
- **ENVIRONMENT FAILED**: partial (the hazard-free environment choice, while independently
  well-motivated, removes the residue field's only signal source -- a secondary contributor)
- **REE FAILED**: not reached (Implementation and Environment are not both independently
  `adequate`/`complete`, so the bar for this bucket is not met)

**Net classification: MEASURES FAILED (test-design gap), not chargeable to the claim.** Per
Step 7's demotion gate ("tested fairly + biology supports the mechanism + still fails"), this
FAIL does not clear the "tested fairly" precondition -- the CEM elite-selection scoring
function cannot act on the injected signal in this configuration, so a null result here cannot
distinguish "the channel doesn't help" from "the channel cannot possibly show up in this
scoring configuration regardless of whether it helps".

## 6. Recommended routing

**V3-EXQ-914** (superseded, instrument defect): no further action. Already correctly excluded
from scoring (`evidence_direction: superseded`); this autopsy formalizes the existing
`evidence_direction_note`'s diagnosis and clears it from the blind-spot net. Recommended
`recommended_epistemic_category: standard` (no suppression warranted -- it is simply inactive).

**V3-EXQ-914a**: reclassify `evidence_direction` from `weakens` to **`non_contributory`** and
`recommended_epistemic_category: standard` (per Step 5's guidance: `standard` is the
behaviour-preserving mapping for a measurement/test-design finding -- it does not suppress
GOV-GRAN-1 surfacing or v3-testability, unlike `substrate_conditional`/`substrate_ceiling`,
neither of which applies here since the gap is test-design, not substrate-build).

**Routing: `/queue-experiment` redesign** (not `/implement-substrate` -- the lever
`wanting_weight` already exists in the substrate; no new build is owed;
`recommended_substrate_queue_entry.action = "none"`). A successor (V3-EXQ-914b, same-question
lettered fix per the EXQ versioning policy) should:

1. Keep the CLOSED/OPEN z_goal-channel contrast (the core MECH-236 test design is otherwise
   sound -- P1/P2 preconditions, seed-pass-fraction gating, and the proximity DV are all
   well-reasoned).
2. Give CEM elite-selection a genuine reward-linked scoring term reachable in BOTH arms --
   e.g. `wanting_weight > 0` paired with the ghost-probe channel (not isolated from it), and/or
   `benefit_terrain_enabled=True`, and/or restore a nonzero hazard/terrain signal so the residue
   field is not degenerate. The scoping concern that motivated isolating `wanting_weight` in
   914a (its writer is `benefit_exposure`, not literally z_goal) is real, but the fix is to
   report the two pathways' *joint* contribution honestly (both are part of the real deployed
   architecture; isolating them from each other tests neither of them fairly) rather than to
   zero the one term that would let the channel matter at all.
3. Explicitly exclude (or separately report) a seed whose ghost branch never fires
   (`mech293_n_ghost_admitted_mean == 0` for the whole run) from the C_MAIN seed-pass
   denominator, or tighten P1's threshold above the absolute floor of 0.0 -- seed 46 in 914a
   contributed a structurally uninformative `gap=0.0` that the current gate silently treats as
   a valid data point.

Draft `evidence_quality_note` for V3-EXQ-914a (governance to apply verbatim if accepted):

> "V3-EXQ-914a's null C_MAIN result (mean gap 0.0032, 1/5 seeds passing) is a test-design
> artifact, not evidence against MECH-236. Code trace of `_score_trajectory`
> (`ree_core/hippocampal/module.py:1513`) confirms the CEM elite-selection scoring function has
> no functional connection to resource-benefit/goal-relatedness under this run's configuration:
> `wanting_weight=0.0` (the only goal-weighted scoring term, deliberately zeroed to isolate the
> channel), `benefit_terrain_enabled=False` (default, unset), and `NUM_HAZARDS=0` (so the
> remaining ARC-007 residue-field term, a harm-accumulation mechanism, has nothing to
> accumulate). The ghost-probe channel itself functions correctly (P1/P2 preconditions both
> met) -- it proposes goal-tagged candidates, but nothing downstream can preferentially select
> them. See `failure_autopsy_V3-EXQ-914-914a_2026-08-13` for the full trace. Recommend
> `non_contributory` / `standard`, pending a redesign (V3-EXQ-914b) that gives CEM
> elite-selection a real reward-linked term reachable jointly with the ghost-probe channel."

## 7. Learning extracted

- The hippocampal CEM elite-selection scoring function (`_score_trajectory`) is goal-blind by
  default (`wanting_weight=0`, `benefit_terrain_enabled=False` are both the REEConfig
  defaults) -- any future MECH-236/MECH-292/MECH-293 evidence run must deliberately enable a
  reward-linked scoring term, or its result cannot discriminate the channel's effect from
  scoring-blindness.
- `NUM_HAZARDS=0` (a reasonable choice to avoid an untrained-agent death confound, itself
  well-documented elsewhere in this codebase) has the SIDE EFFECT of silencing ARC-007's residue
  field entirely when it is the sole scoring term -- worth flagging generally for any future
  driver relying on ARC-007 STRICT terrain scoring as its only differentiator in a
  zero-hazard environment.
- The `modulatory-bias-selection-authority` substrate fix (E3.select, already implemented)
  does not reach into hippocampal CEM's own internal refit step -- a goal-blind refit can
  discard a genuinely better candidate before E3 ever sees it. Worth a note on that SD entry (or
  a new, narrowly-scoped one) if a future session finds this call site is a recurring blocker
  across more than this one claim; not warranted as new substrate work from this single
  instance alone (the existing lever, `wanting_weight`, already covers it).
- The P1 precondition threshold (`>= 0.0`, "lower") passes even a fully-inert cell (0 candidates
  ever admitted for that seed across the whole run) -- a structural precondition-gate
  looseness worth tightening in any successor driver reusing this pattern.

## 8. User confirmation (Step 8 gate)

Presented via `AskUserQuestion` 2026-08-13. All three questions answered with the recommended
option: (1) diagnosis confirmed as a test-design gap, not genuine weakens; (2) routing
confirmed as `/queue-experiment` redesign; (3) V3-EXQ-914 ratified in this same cluster
artifact rather than autopsied separately. Logged to
`REE_Working/RECOMMENDATION_LOG.jsonl` (3 entries, all `matched_recommendation=true`).
