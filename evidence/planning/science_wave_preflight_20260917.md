# Science-wave pre-flight record -- 2026-09-17

First use of the SCIENCE lane on the dispatch curation ledger (REE_Working
`0ae48e3f7`). Four candidate `/queue-experiment` chips were pre-flighted
read-only (metaworker-orchestrate Step 1d-iii) before any Opus session was
spent. Session `science-wave-20260917`.

**Outcome: 2 AMBER (curatable), 2 RED (withdrawn).** A 2-of-4 refusal rate is
itself the 1d-ii "two refusals means stop" signal -- the named-chip population
was staler than it looked from titles and provenance alone. Total pre-flight
cost ~750k tokens across four Sonnet passes; the two REDs would each have
consumed a full Opus design+red-team session to reach the same conclusion.

| Chip | Verdict | Disposition |
|---|---|---|
| `chip-20260916-arc029-p1p3-redesign-queue` | AMBER | curated `science-20260917-arc029-p1p3` |
| `chip-20260916-mech268-nonsaturating-harm-gradedness-queue` | AMBER | curated `science-20260917-mech268-gradedness` |
| `chip-20260914-mech428-c1-redesign-v2-attained-signature` | RED | withdrawn; superseded by `chip-20260917-mech428-parent-goal-alpha-sweep` |
| `chip-20260916-exq1012b-placebo-rescaling-null-queue` | RED | withdrawn; routed to GFLAG-0297 (`/failure-autopsy`, not `/queue-experiment`) |

> **The two curated entries were subsequently ERASED** by the hub materializer
> (see "Transport defect" at the end). They must be re-curated once the
> coordinator accepts the science lane -- the verdicts below are the record
> that makes that a cheap re-run rather than another 750k tokens.

---

## RED 1 -- `chip-20260914-mech428-c1-redesign-v2-attained-signature`

**Blocker.** The chip's stated root cause (F4 strong form: post-arrival
crediting cannot carry the waypoint signature at all) was measured FALSE one
day after the chip was written, by the same lineage --
`evidence/planning/exq884c_mech428_c1_ema_self_overlap_redteam_blocking_20260916.md`
(ree-v3 `bda53ea` / `5cc777a`). The raw post-arrival observation separates at
the 100th percentile of its own null on 3/3 seeds; the dominant loss is the
SENSE PATH, not the marker overwrite. Both fix directions the chip offers were
already tried to a conclusion there: direction 1 works only jointly with
`alpha_world=0.9` (never mentioned in the chip; at the `REEConfig` default 0.3
it is at-chance 3/3) and then fails on a newly-confirmed EMA self-overlap
defect (F1: biased positive with ZERO signal, 12/12 false-positive on synthetic
zero-information data); direction 2 was implemented and rejected as at-chance.

Also surfaced: GFLAG-0293 (since resolved, below). The marker-overwrite bug at
`ree_core/environment/causal_grid_world.py:57-69` is real and still present,
but is not the binding constraint.

## RED 2 -- `chip-20260916-exq1012b-placebo-rescaling-null-queue`

**Blocker.** The exact task was attempted and REFUSED ~14h before the
pre-flight, by session `science-batch6-20260916-exq-1012b` (closed
2026-09-16T21:12:49Z), which raised GFLAG-0297 and released the slot.
Re-derived independently from the 1012a manifest: exactly 3 live channels in
all 8 cells (`benefit_weighted`/`goal_weighted` = 0.0 everywhere), so a
permutation of the fitted per-channel scales has exactly 2 derangements, and
the originally-dominant channel keeps dominance under BOTH in 8/8 cells
(`a*c > b^2` holds throughout). The placebo's flip rate is ~0 by construction,
so the pre-registered `|operator_flip - placebo_flip| >= 0.10` criterion
degenerates to "the operator flips at all" -- which V3-EXQ-1012a already
showed. A PASS would have read as a reference-bearing rung-3 validation it is
not.

GFLAG-0297 specifies the correct next step: a structurally DIFFERENT
discriminator (the operator's own assignment is the unique permutation that
equalises the channels, so a permutation-style null is structurally
unavailable), routed via `/failure-autopsy` or `/governance` -- NOT another
`/queue-experiment` pass. 1012a's own result stands (`non_contributory`,
ratified governance-20260916, REE_assembly `db6d20ebee0`).

---

## AMBER 1 -- ARC-029 P1-P3-clean commitment-gate redesign

READ-ONLY PRE-FLIGHT -- VERDICT: AMBER
Run 2026-09-17 by science-wave-20260917 (Sonnet, read-only, no writes).

VERIFIED (proceed on these; do not re-derive):
- (a) Producer trace CONFIRMED -- these are real writes, not bare consumer sites:
  * BreathOscillator threshold formula: ree_core/heartbeat/clock.py:113
    (effective = base_threshold * (1.0 - sweep_amplitude)); consumed at
    ree_core/predictors/e3_selector.py:3770-3772. Does NOT touch running_variance.
  * current_precision getter: e3_selector.py:815-817 = 1.0/(running_variance + 1e-6)
    -- confirms P2's stated confound mechanism is real, not hypothetical.
  * beta_gate_bistable default False at ree_core/utils/config.py:3296;
    should_admit_elevation is real at ree_core/heartbeat/beta_gate.py:218; the
    legacy re-evaluate-every-E3-tick branch that fires when bistable=False is real
    code at agent.py:9855-9880.
  * use_natural_commit_latch_hold gated branches real at agent.py:1463-1515,
    :7162-7164, :9756-9774 (the chip's cited line ranges match the live file).
- (b) Criteria are NON-DEGENERATE. claims.yaml:14042-14068 (ARC-029 what_would_answer)
  separates a genuine FALSIFYING outcome (P1-P3 clean, null harm difference) from a
  non_contributory instrument failure (P1/P2 fails cleanly) -- exactly the split the
  063a autopsy found missing. A relative bar (0.002 abs / floor 0.01 harm/step = 20%
  relative) replaces the stale 2026-03 absolute magnitudes.
- (c) Both arms (ALTERNATING BreathOscillator sweep vs STATIC no-sweep control) resolve
  to real, already-exercised code; a prior smoke run produced real numbers
  (0.0056-0.0136 harm/step), so the arms execute at real episode length.
- (d) ARC-029 is status: candidate in claims.yaml:13886 (matches the chip's premise that
  governance-20260916 demoted it). experiment_queue.json holds only V3-EXQ-1023a
  (unrelated) -- the redesign is NOT queued and no duplicate open chip exists.
  EXP-1394 present in experiment_proposals.v1.json (related_claims ARC-029/ARC-016/
  MECH-090), still 'proposed' -- placeholder not yet consumed.
- (e) 5 seeds [0..4], consistent with ARC-029's lineage convention. NOT independently
  powered: no manifest exists at the recalibrated operating point (hazard_harm=0.05,
  proximity_harm_scale=0.10), so the 0.002-floor/20%-relative bar is unconfirmed at n=5.
  The script embeds a _calibrate() smoke step to check this -- correct mitigation, but
  never run to completion.

CAVEAT -- do these two things FIRST, before claiming anything:
1. RE-RUN `task_claim.py check --resources ree-v3/experiment_queue.json` FRESH. At
   pre-flight time (2026-09-17T14:35Z) an ACTIVE claim
   igw-auto-igw-242-proposal-for-mech-021-20260917T143001Z owned that exact file for
   unrelated MECH-021 queue-experiment work. If it still owns it, you are NOT the owner:
   stop and report per CLAUDE.md Conflict resolution. Do not edit through it.
2. DETERMINE THE LIVE NEXT EXQ ID FROM SCRATCH. Both V3-EXQ-1049 and V3-EXQ-1050 have
   been reserved AND abandoned by other sessions today (three independent claim records;
   igw-241-mech019-exq-1049 released both). Neither is safe even as a starting guess.

ALSO KNOW: an UNTRACKED 1253-line script from a dead session sits at
ree-v3/experiments/v3_exq_1049_arc029_threshold_side_commitment_harm.py (plus
_scratch_probe_arc029.py and a .bak). It is not committed and not queued. Read it before
writing anything new -- it may be most of the work -- but treat it as unreviewed: its
session died before finishing calibration, and it carries the now-unsafe 1049 id in its
filename.

---

## AMBER 2 -- MECH-268 ecological gradedness successor

READ-ONLY PRE-FLIGHT -- VERDICT: AMBER
Run 2026-09-17 by science-wave-20260917 (Sonnet, read-only, no writes).

VERIFIED (proceed on these; do not re-derive):
- PREDECESSOR V3-EXQ-729 re-read numerically from both manifests
  (evidence/experiments/v3_exq_729_mech268_dacc_saturation_liveloop_20260710T{065147,
  113825}Z_v3.json) plus failure_autopsy_V3-EXQ-729_2026-09-14.md:
  mean_sat_factor_final_third = 0.25 (ON) / 1.0 (OFF), bit-identical in all 6x2 cells;
  harm_class_fraction = 1.0 in EVERY cell (degenerate, non_degenerate:false);
  mean_z_harm_a_norm varies 0.510-1.452 across seeds. Only C4a is genuinely contingent;
  C2/C3/C5 are code-structural tautologies (dacc.py:237-238 early return) and C1's 0.25
  is arithmetic (f_sat = 1/(1+0.5*(8-2))). So the chip's premise is CORRECT: gradedness
  has zero loop-level evidence, only unit-level (V3-EXQ-463 UC4_monotone_in_recurrences).
- (a) Producer trace CONFIRMED: DACC._saturation_factor at ree_core/cingulate/dacc.py:229-251
  (sat_factor = 1/(1+strength*excess), excess = max(0, n_rec-grace)); live-path writer at
  ree_core/agent.py:10173-10198 (select_action tail, gated on dacc_saturation_enabled,
  outcome class from z_harm_a.norm() > contextual_safety_harm_threshold at :10196,
  dacc.record_outcome at :10198).
- STAGE-H HARM UNTRAINED: confirmed and NOT a blocker here. experiments/
  v3_exq_729_...py:40-44 states P0 warmup trains only E1+E2; z_harm_a is a fixed
  (untrained) projection of harm_obs_a. The mechanism under test is the recurrence-counting
  saturation function over a CLASSIFIED outcome stream, not a learned harm representation.
- (d) MECH-268 is status: provisional, epistemic_category: standard in claims.yaml
  (45449-45465), matching the chip's stated authority. No MECH-268/729a/1048 entry exists
  in experiment_queue.json -- nothing landed.

CAVEAT -- READ GFLAG-0299 IN FULL BEFORE DESIGNING ANYTHING
(REE_assembly/evidence/planning/governance_flags.v1.json, flag_id GFLAG-0299, status OPEN).
This exact task was already attempted and REFUSED at /queue-experiment Step 4.5 on
2026-09-16 (session science-batch6-20260916-exq-1048; WORKSPACE_STATE line 357; script
deleted). The chip carries NO trace of this, and its own START-TIME STOP-CHECK will NOT
surface it -- none of its four checks reads governance_flags.v1.json.

GFLAG-0299's verified findings, which your design must respect:
1. An IID-shuffle matched-noise control is the WRONG null for a recurrence-count statistic
   -- it is the maximum-mixing extreme, not the middle. Its interior-band probability
   (0.9297 at p=0.5) makes the pre-registered ON-NOISE >= 0.10 bar mathematically
   unreachable AND its sign is backwards. Do NOT reuse that construction. Build a
   two-sided contrast, or a statistic not monotone in mixing.
2. Gate on PER-RUNG mixedness, not cross-rung spread -- the latter misclassifies an
   all-no-harm degenerate ladder as informative.
3. The noise-density spy was wired outside the injection wrapper (measured the live
   stream, not the injected one).
4. The assumed E3 tick period (8) measures 9 in smoke -- undercounts the sample-size bar.
5. The eval env was unseeded across ON/NOISE/OFF cells, breaking ecology pairing.

BANKED AND REUSABLE (from the same flag -- do not rediscover):
- EVAL_HAZARDS is INERT as a lever: z_harm_a.norm() sits 0.55-0.70, an order of magnitude
  above contextual_safety_harm_threshold=0.05 regardless of hazard count.
- THE WORKING LEVER is contextual_safety_harm_threshold. Smoke sweep over {0.05, 0.55,
  0.75} moved harm_class_fraction 1.000 / 0.625 / 0.450 (spread 0.45).
- Post-saturation PE readout = _last_pe_unsaturated * _last_saturation_factor.
- Per-seed training reuse via a state_dict snapshot -- NOT copy.deepcopy, which fails on
  a trained REEAgent.

POWER: only smoke-scale numbers exist for the working lever (0.45 spread over 3 rungs). The
predecessor's continuous-metric seed variance was non-trivial (mean_pe_unsaturated_final_third
2.15-4.49 across seeds at FIXED dose), so seed count AND rung count both need explicit
justification. Do not default to the predecessor's counts.

ID: V3-EXQ-1048 was REASSIGNED to an unrelated MECH-017 experiment (e592f65, landed
2026-09-17). Pick a fresh number at write time; max observed ~V3-EXQ-1050, and both 1049
and 1050 have been reserved-and-abandoned today. Resolve GFLAG-0299 citing the successor's
queue entry once it lands.

---

## GFLAG-0293 -- found by this pre-flight, resolved as already-applied

The MECH-428 pre-flight surfaced GFLAG-0293 ("QUEUE-FLOOR BLOCKER"): that
`/queue-experiment` Step 2.5c refuses every agent-stepping experiment. Verified
independently and found **already remedied** -- `substrate_queue.json` entry
`f_dominance_conversion_ceiling` carries `implementation_status: wontfix`,
applied 2026-09-16 by `orchestrate-20260916-1305` under a user decision. Running
Step 2.5c's own snippet verbatim, that entry no longer lists, and the four
`corrupting` entries that do list are all on peripheral modules
(`policy/tonic_vigor.py`, `predictors/e1_deep.py::ContextMemory.write`,
`affect/blocked_agency.py`, `regulators/selection_entropy_floor.py`) -- none on
the core agent path. Only `corrupting` blocks; the eight core-path hits are all
`degrading`/`cosmetic`/unset. Flag resolved 2026-09-17.

**Correction recorded on the flag**: it offered two remedies as equivalent, but
option (b) -- narrow the overlap test from file-level to the named `::function`
-- would NOT have worked. The entry's paths are already function-qualified
(`e3_selector.py::score_trajectory`) and the flag's own measurement shows a
scripted-action driver reaching `score_trajectory` 352x, so a function-level
test fires just the same. Only the status fix unblocks.

**Residual, not blocking**: 13 of 37 entries with `substrate_paths` still carry
free-text statuses, so this shape recurs entry-by-entry until that axis is
cleaned. A sweep was offered and declined in favour of the narrow fix.

## Transport defect -- why the two AMBER entries are not in the ledger

`scripts/dispatch_campaigns.json` is COORDINATOR-MATERIALIZED. The coordinator
rejected both science entries (`HTTP 400`, its `campaign_id` regex predated the
science lane), `dispatch_campaigns.py` fell back to the git path, committed and
pushed (`0ad328bd3`, `84b4c8328`), and they verified as present on origin --
then the hub materializer deleted them 2 minutes later (`fd7730f70`, -128
lines) because the DB never had them. A leased `ree-cloud-5` cycle in between
read "2 live campaign(s)" in its preexit check and then reported "Zero science
entries" at Step 4, because `list --live` is coordinator-first while
`dispatch_candidate_order` is file-based.

Two follow-ons, both since RESOLVED:
- **Server half** -- `chip-20260917-coordinator-science-lane-schema`, LANDED
  ree-v3 `2e2bd598af` and deployed on the hub. (`campaign_is_live()` carried the
  same `lane != CAMPAIGN_LANE` test, so the id regex alone was not sufficient --
  the fix covered both.)
- **Client half** -- LANDED, REE_Working `382333121`: `dispatch_campaigns.py`
  now DIES on a coordinator rejection rather than falling back to git, so this
  failure can never again read as success.

## The lane needed THREE fixes, and only the first was visible by inspection

Recorded because a future re-curation will otherwise stop at the first one and
repeat the other two. Each layer was correct in isolation and failed at the seam
with the next; each was found only by actually trying to dispatch, never by
reading:

1. **The lane itself** (REE_Working `0ae48e3f7`). Science was refused from the
   curation ledger, so it could not be a cloud candidate at all. Found by reading.
2. **The coordinator** (ree-v3 `2e2bd598af`). `/campaign/add` rejected
   `lane: science` on its `campaign_id` regex; the git fallback then wrote entries
   that verified on origin and were deleted by the materializer two minutes later.
   Found by curating and watching them vanish.
3. **The launcher** (REE_Working `41d771ce3`,
   `chip-20260917-dispatchremote-selftarget-ssh-gap`). A resident cycle on
   `ree-cloud-5` could not launch a campaign whose `target_box` is `ree-cloud-5`:
   `dispatch_remote_launch.py` coupled the EXECUTION target (SSH vs local
   subprocess) to the CAMPAIGN-TARGET-MATCH identity through the single `--box`
   string. `--box ree-cloud-5` self-SSHed and got `Permission denied` (no box has
   a self-SSH key); `--box local` set `this_host=None` and `machine_class="mac"`,
   failing `targets_box()`. Fixed with `is_self_target()`, resolved through
   `machine_identity.canonical_machine_name` (allowlist, never a raw hostname
   compare). Found by `orchestrate-20260917-1532` triggering a real cycle: 9
   minutes, 1m51s CPU, both entries listed, neither launched.

**The generalisable bit: LISTING IS NOT LAUNCHING.** This session verified that
`ree-cloud-5` listed both entries, ordered them ahead of the bundles and exempted
them from the starvation withhold -- all true, all verified -- and inferred from
that that a cycle trigger would dispatch them. It would not. A `--dry-run` from
the target box is the cheap predicate that distinguishes the two; prefer it over
any amount of candidate-listing evidence.

Note also that the obvious workaround does NOT work: re-curating to
`--target-box cloud` still fails, because `--box local` hardcodes
`machine_class="mac"`. `--target-box any` would have passed (`targets_box`
short-circuits on `any` before consulting either field), at the cost of recording
the launch as `box: "local"` in the ledger's provenance.
