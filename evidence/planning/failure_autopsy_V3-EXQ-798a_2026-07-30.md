# Failure Autopsy: V3-EXQ-798a (SD-MEL-PRODUCER test-bed validation, PASS)

**Generated:** 2026-07-30T06:49:10Z
**Scope:** single
**Status:** confirmed
**Chip:** chip-20260730-autopsy-798a (spawned by the 2026-07-29/30 `/governance` cycle -- 4 decision-routing diagnostic PASSes, 798a/810a/819a/839, left pending per user Route B)

## Why this needed an autopsy despite a neutral `evidence_direction`

The manifest self-reports `evidence_direction: non_contributory` and `claim_ids: []` --
by design, since the script validates a test-bed, not a claim (`experiment_purpose:
diagnostic`). But its own `evidence_direction_note` states this PASS is what "licenses
the SEPARATE, still-gated MECH-180 ecological end-to-end run" -- i.e. it is a
decision-routing diagnostic (CLAUDE.md Step 1.5a) despite the neutral label, so it
needs a confirmed autopsy before that unblock can be trusted.

## Target

- `run_id`: `v3_exq_798a_sdmelproducer_graded_nonconverging_world_c4readable_20260729T125858Z_v3`
- `queue_id`: V3-EXQ-798a (supersedes V3-EXQ-798)
- `outcome`: PASS, label `producer_validated_graded_learnable`
- `claim_ids`: `[]` (deliberate -- validates SD-MEL-PRODUCER, tags no claim)
- `machine`: ree-worker-3, `machine_class`: linux-x86_64-py3.10-torch2.12.0+cpu
- `elapsed_seconds`: 45318.6 (~12.6h)

## Step 2a -- dry-run gate

```
$ python3 scripts/check_dry_run_citations.py v3_exq_798a_sdmelproducer_graded_nonconverging_world_c4readable_20260729T125858Z_v3
-- 0 dry cited, 0 dry in named families, 0 ambiguous, 1 clean, 0 unknown
```
Top-level `dry_run` is `None` (falsy). **Not a smoke.** `dry_run_checked: true`,
`excluded_dry_run_ids: []`.

## Step 2b -- facts

**Recording provenance.** `validate_recording.py --paths <manifest>` -> `OK`, 0
always-core gaps. `recording_schema: rec/v1`, `substrate_hash` present, `config` and
`seeds` ([42, 123, 456]) present. No recording gap.

**798a fixes three defects in its predecessor V3-EXQ-798** (FAIL,
`producer_graded_but_not_learnable`, adjudicated informally in the 2026-07-27T23:42Z
`WORKSPACE_STATE.md` entry that authored 798a -- no formal `failure_autopsy_V3-EXQ-798_*`
artifact exists; that gap is noted below but is out of this autopsy's scope):

1. **C4 was unreadable by construction.** 798's absolute-edge binning
   (`SSL_BIN_EDGES=(2,5,12)`) put the top bin at `steps_since_shift > 12`, but both
   arms C4 read ran at `interval=10`, so the counter (which cycles `0..interval-1`)
   never reached it -- bin 3 held 0 samples on all 3 seeds of both arms,
   deterministically, not by sparse sampling. 798a replaces this with **cycle-quartile
   binning** (`q = min(3, 4*counter // interval)`), whose top bin is non-empty for any
   `interval >= 4` by construction, and proves reachability at import time via
   `_assert_quartile_reachability()` before any compute is spent.
2. **The noise control was not actually elevated** (798: `ARM_4_NOISE` mel 2.36e-05 <
   `ARM_3_HIGH` mel 3.58e-05 at sigma 0.05). 798a derives `NOISE_SIGMA_LO=0.12` /
   `NOISE_SIGMA_HI=0.24` from 798's own landed measurement under a pre-stated
   sigma^2 model, and selects the control via a pre-registered rule (lowest-sigma arm
   that is at least as elevated as the anchor on every seed).
3. **The routing ignored readability**, asserting a "does not decay" verdict about a
   quantity that was never measured (798's own `learnability_bins_populated`
   precondition recorded `met: false`, contradicting its own manifest). 798a adds a
   `c4_measurable = c4_bins_readable AND c4_control_fair` gate; when false, the run
   routes to an explicit `c4_unreadable_requeue` label rather than asserting a
   learnability verdict.

C4 is anchored on `ARM_1_LOW` (interval 60, most re-learning headroom), pre-registered
before the run -- not selected from its outcomes -- so a null there would be an
unaliased negative (GOV-FANOUT-1 verdict-aliasing check).

**Observed vs expected.** All four criteria passed on real margins, not marginally:

| Criterion | Result | Margin |
|---|---|---|
| C1 grading (load-bearing) | PASS, 2/3 seeds | monotone NONE<LOW<MED<HIGH, spread >= 0.25 |
| C2 above-reference | PASS, 2/3 seeds | every graded arm > NONE + 1e-6 |
| C3 sustained non-convergence | PASS, 3/3 seeds, late-quartile readable all 3 | HIGH stays above stable ref late in its own cycle |
| C4 learnability (load-bearing, anti-artifact) | PASS, measurable | anchor decay 0.283 (floor 0.15); control decay 0.0042 (ceiling 0.10) |

Noise-control fairness: `ARM_4_NOISE_LO` worst-seed ratio vs anchor = **1.2466** (>= 1.0
required) -- the control is genuinely at least as elevated as the anchor on every
seed, not a marginal pass.

**Failed criterion**: none -- clean PASS, all four (readiness + C1-C4) cleared.

## Step 3 -- claim-layer mapping

`claim_ids: []` by design. No claim is tested or adjudicated by this run; it validates
infrastructure (the SD-MEL-PRODUCER test-bed) that MECH-180 / INV-050 depend on.
MECH-180 itself (read separately, `docs/claims/claims.yaml`): `status: candidate`,
`v3_pending: true`, `pending_retest_after_substrate: true`, `epistemic_category:
substrate_ceiling` (mirrors INV-050 per the 2026-07-16 GOV-GRAN-1 metabolization --
a deliberate labeling choice, not a claim this run touches).

**Granularity-debt recurrence check** (`granularity_debt_cluster.py MECH-180`): 3 prior
targets (677, 718, 718a), alignment distribution = `unclear` x3, **no target reads
`weakened`** -- trigger does NOT fire; this is measurement/environment debt, not
granularity debt, consistent with the 2026-07-16 verdict already on record. 798a adds
no new claim-tagged target to this count (`claim_ids: []`).

**Re-derive brake**: not applicable to this target (claim_ids empty). The MECH-180
brake fired at 3 ceiling autopsies (677/718/718a) and was already released for the
SD-MEL-PRODUCER *build* on 2026-07-21 per the claims.yaml
`ceiling_routing_note`/`granularity_debt_recurrence_note` -- 798a is that build's
validation run, not a new same-question re-queue of 677/718/718a's ecological
question, so it is not a brake violation.

## Step 4 -- biological-reference triage

Not directly applicable in the usual sense: this run validates an *engineering*
test-bed (does a periodic action->displacement re-permutation produce graded,
above-reference, and genuinely re-learnable prediction-error load, as distinct from
graded noise), not a biological claim per se. The underlying biological question MECH-180
answers -- does novelty-driven learning load adaptively upregulate offline consolidation
-- is independently and extensively cited in MECH-180's own `claims.yaml` `notes`
(Wilson & McNaughton 1994; Tononi & Cirelli 2003; Stickgold et al. 2001; Louie & Wilson
2001; `lit_conf` 0.887), untouched by this run.

The mechanism under test here (rule-shift invalidates a learned action->displacement
mapping, which must be re-learned, vs. additive observation noise which is
irreducible by construction) is a DV-symmetry-aware engineering design, not a formal
import needing a biology lit-pull. No `/lit-pull` commission is owed.

## Step 5 -- four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | not_applicable | claim_ids=[] by design; validates infrastructure, not a claim |
| Biological reference | present (at the claim level, not this run) | MECH-180's own citations are untouched and sufficient; no lit-pull owed |
| Developmental / dependency prerequisites | present | SD-MEL-CONSUMER (link ii) already built+proven (718a); this run builds link (i)'s test-bed |
| Implementation completeness | complete | 3 defects fixed with mechanical, pre-registered, in-script-asserted proofs (`_assert_quartile_reachability`), plus a 4th latent routing gap (C1+C2+C4 pass/C3 fail) found and closed |
| Environment adequacy | adequate, now demonstrated | the graded ladder is both above-reference AND genuinely learnable (C4), where 798's own env_drift-based predecessor (677/718/718a) was noise-level and irreducible |
| Measurement adequacy | adequate | large margins on both load-bearing criteria (C1 spread, C4 decay 0.283 vs 0.15 floor / 0.0042 vs 0.10 ceiling); non-degenerate on all 4 criteria |
| Integration adequacy | isolated, arm-symmetric | dead z_goal stream verified structurally inert (below) and identical across all 6 arms, so it cannot confound the C1-C4 comparison |
| Scale / capacity | adequate for this diagnostic's purpose | 3 seeds x 6 arms, 900-step measurement + 900-step training windows, matches the recon-only P0 base already proven convergent on this instrument (798/701c) |

**z_goal dead-stream verification (independently re-checked in this autopsy, not just
trusted from the docstring).** Confirmed in the live code, not merely asserted:
`ree_core/predictors/e3_selector.py:1207` gates the E3 goal term on
`goal_state.is_active()`; `ree_core/agent.py` gates E1 goal-conditioning on the same
predicate at multiple sites (e.g. line 4875); `agent.update_residue` (the function that
produces the DV, `e3_prediction_error`) has no goal reference at all. The manifest's
own `z_goal_stream` block shows `writer_calls: 0`, `active_frac: 0.0`,
`writer_defect: true` -- confirming `goal_state.is_active()` was False throughout,
so both gated paths were inert for the entire run. `_make_agent` takes only env
dimensions (no arm-specific config), so the inertness is identical across all 6 arms --
it cannot differentially confound the C1-C4 comparison. This matches the docstring's
own claim and the 2026-07-27 adjudication it cites (`DEAD_Z_GOAL_STREAM_EXEMPT`);
this autopsy independently re-derived the gating from source rather than taking the
citation on faith.

**Substrate-stability caveat (found in this autopsy, not previously flagged).**
`substrate_stable_across_run: False`. `substrate_stability_detail` shows
`per_cell_hashes_disagree: False` (all 6 arms x 3 seeds ran against ONE consistent
substrate hash throughout the run -- internal comparability of the C1-C4 grid is
unaffected) but `process_snapshot_drift` shows the on-disk `ree_core/**` hash at
manifest-stamp time (`12:58:58Z`) differs from what the process hashed at start
(`resolved_at_utc: 2026-07-29T00:57:24Z`). Per `experiments/_lib/manifest_core.py`'s
own documentation, this is expected for a ~12.6h run on a shared checkout where other
work landed on `ree-v3/main` mid-run -- it is a **reuse-safety** signal (`arm_reuse`
correctly refuses to serve this run's cells as a baseline arm for a future
differently-driven experiment), not a validity defect for this run's own C1-C4
adjudication. Recorded here so a future consumer checking `arm_reuse` against this
run_id understands why it will be refused, and so the caveat is not lost.

## Step 6 -- cluster pattern

Not a cluster autopsy (single target). For context, 798a is the 4th run in the
MECH-180 link-(i) producer lineage (677 -> 718 -> 718a -> 798/798a), each a
progressive localization of the same producer gap (per the 2026-07-16
`granularity_debt_recurrence_note`), culminating in a built-and-now-validated
test-bed rather than a claim disposition.

## Step 7 -- learning extracted and repair pathway

**Learning extracted:**
1. The SD-MEL-PRODUCER test-bed (periodic action->displacement re-permutation) DOES
   produce a graded, above-reference, and genuinely learnable (re-learnable, hence
   reducible) prediction-error load, cleanly separable from a matched noise control on
   real margins -- the env_drift-based predecessor (677/718/718a) could not do this
   because drift only added sampling noise, not learning load.
2. All three concrete defects in V3-EXQ-798's C4 measurement (unreachable top bin,
   under-elevated control, a routing gap that asserted an unmeasured verdict) were
   fixed with design-time, pre-registered, mechanically-asserted proofs rather than
   post-hoc tuning -- a repeatable pattern for future criterion-readability repairs.
3. A long-running (~12.6h), shared-checkout experiment can legitimately show
   `substrate_stable_across_run: False` from process-snapshot drift alone (not
   per-cell disagreement); this is a reuse-safety signal, and future long single-arm
   or multi-arm runs on shared workers should expect and correctly interpret it rather
   than treating it as a run-validity red flag.

**Diagnosis**: implementation gap in the predecessor (798), now closed; environment
adequacy achieved. No claim pressure, no biology divergence, no measurement gap, no
recording gap.

**Recommended routing** (both report-only -- neither is built by this autopsy):

1. **Documentation update** (governance / a quick doc-edit session, not
   `/implement-substrate` -- the substrate is already built and landed, nothing to
   queue): `docs/architecture/sd_mel_producer.md` `Status: PENDING` should become
   `VALIDATED (V3-EXQ-798a, 2026-07-29)`, and MECH-180's `claims.yaml` `live_status` /
   `ceiling_routing_note` should record that the test-bed is now validated -- still
   explicitly **NOT** MECH-180 evidence (`claim_ids=[]`), still gating on the separate
   ecological end-to-end run.
2. **`/queue-experiment`** may now propose the still-gated MECH-180 ecological
   end-to-end run using the SD-MEL-PRODUCER world-rule-shift environment as the
   novelty knob (replacing env_drift) -- a NEW scientific question (new EXQ number,
   not a re-letter of 677/718/718a, which tested a different, now-abandoned knob).
   This autopsy does not queue it; per Scope Discipline this is reported as follow-on,
   not built here.

`recommended_substrate_queue_entry.action: "none"` -- SD-MEL-PRODUCER is already built
and landed (2026-07-21); no substrate_queue.json entry exists or is needed for it, by
design (per the `ceiling_routing_note`).

**Draft `evidence_quality_note` for governance** (to append to MECH-180, not as a
target-claim tag since `claim_ids=[]`, but as a related-substrate update):

> SD-MEL-PRODUCER test-bed VALIDATED 2026-07-29 (confirmed
> `failure_autopsy_V3-EXQ-798a_2026-07-30`; V3-EXQ-798a PASS, `producer_validated_graded_learnable`,
> claim_ids=[] by design). The environment now demonstrably produces a graded,
> above-reference, and genuinely learnable (re-learnable) waking MEL load, cleanly
> separated from a matched noise control (anchor decay 0.283 vs floor 0.15; control
> decay 0.0042 vs ceiling 0.10; noise-control worst-seed ratio 1.25x >= 1.0 fair).
> This licenses (does not itself constitute) a SEPARATE, still-gated MECH-180
> ecological end-to-end run using this environment as the novelty knob. v3_pending
> STAYS; pending_retest_after_substrate STAYS until that ecological run scores.
> PROMOTES/DEMOTES NOTHING.

## Step 9b -- hypothesis-space ledger

Not applicable: no `fanout_recommendation` (single test-bed validation, not a
discrimination among live rival hypotheses) and `claim_ids=[]`, so there is no leg to
pre-register or resolve. Skipped cleanly per the skill's own gating condition.

## Gate (Step 8)

Presented to the user via AskUserQuestion 2026-07-30. User confirmed: "Confirm as
read" -- the PASS reading and the routing above are accepted as-is.

## Out-of-scope note (not actioned here)

No formal `failure_autopsy_V3-EXQ-798_*` artifact exists for 798's own FAIL, even
though it was informally diagnosed (in full technical detail) in the
2026-07-27T23:42Z `WORKSPACE_STATE.md` entry that authored 798a. Since 798 is
`superseded` by 798a and carries no independent decision-routing role, this gap is
noted but not pursued as part of this autopsy (scope discipline) -- flag only if a
future governance cycle needs a formal artifact for 798 specifically.
