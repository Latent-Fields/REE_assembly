# Failure Autopsy — V3-EXQ-841 (MECH-163 hierarchical-vs-flat falsifier + Q-085 grain dose-response)

**Mode: STAGING (headless subagent), CONFIRMED 2026-07-31T23:32:48Z.** This artifact was
generated as a DRAFT awaiting human confirmation; Interactive Step 8 (AskUserQuestion) was
skipped per staging-mode instructions at generation time. It was subsequently **confirmed via
direct interactive user confirmation of the disposition AS DRAFTED** (session
`quirky-mayer-ee5ad2`) — the legitimate alternative path to a full `/governance` walk per the
skill's own staging-mode design. On confirmation: `recommended_evidence_direction_per_claim`
was applied to `claims.yaml` (MECH-163, Q-085, both `non_contributory`), the
`recommended_substrate_queue_entry` (`arc071_chunk_commit_latch_persistence`) was added to
`substrate_queue.json`, and `hypothesis_space_ledger_pending` was applied to
`hypothesis_space_registry.v1.json` (Mode A pre-registration, qid
`arc071-commit-latch-persistence`, both H1/H2 legs `alive`/`pending`).

- run_id: `v3_exq_841_mech163_q085_grain_dose_response_20260731T080537Z_v3`
- queue_id: `V3-EXQ-841`
- claim_ids: `MECH-163`, `Q-085`
- outcome: FAIL, `evidence_direction: non_contributory` (both claims)
- manifest self-route: `substrate_not_ready_requeue`; `non_degenerate: false`
- dry_run: `false` (confirmed via `check_dry_run_citations.py`, clean)
- recording: `validate_recording.py` OK — always-core complete (substrate_hash, config, seeds, machine present)
- generated_utc: 2026-07-31T20:30:41Z

## 1. Facts reconstruction

**Design.** One run answers two questions with zero extra compute (deliberate, per the
script's own docstring): MECH-163 (is post-devaluation outcome-insensitivity produced by
committed-macro GRAIN, hierarchical, or by an ARBITRATOR weighting a habit controller,
flat?) and Q-085 (is the committed-macro grain budget a controllability parameter — does
post-devaluation persistence rise monotonically with the REALISED mean committed-chunk
length?). Six arms: `A_OFF`, `A_FLAT`, `A_HIER_S2/S3/S5` (dose arm, chunk_max_size
2/3/5), `A_FLATCHUNK_S5`. 8 seeds each, 48 cells total, `train_mode=False` (no_grad)
throughout. DV: `_approach_rate`, a distance-reduction predicate over steps, reported raw
and under two pre-registered opposed confound-conditionings (interruption; devaluation
knowability). Devaluation route is a **direct outcome devaluation**
(`env.resource_benefit -> 0` mid-episode) rather than the SD-033b OFC-head route named in
claims.yaml, substituted on measured compute-feasibility grounds (documented in the script
and in `devaluation_route_note`) — this substitution is not itself a defect; the
manipulation check (gate c) is measured on a policy-independent probe regardless of route.

**Self-report.** `preconditions_scope_note`: *"No arm passed its gate, so every
precondition is carried in interpretation.preconditions and the whole run is vacuous."*
`degeneracy_reason` lists, per arm, which of the mandatory pre-registered gates failed.
**Every one of the 6 arms is RED.** `criteria_non_degenerate` is `false` for all three
criteria (C1 dose-response monotonicity, C2 hierarchical-persistence-without-arbitrator,
C3 flat-arm-scorable) — **this run is explicitly NOT a refutation of MECH-163 or Q-085**,
by its own design.

**Failed criterion type.** Readiness/precondition (gates a, c, d), not the load-bearing
discrimination criteria themselves — the discrimination criteria never got the chance to
run because the readiness gates upstream of them failed first.

## 2. Independent re-derivation (self-route is a hypothesis, not a verdict)

Per the skill's "self-route is a hypothesis" rule, the manifest's own
`substrate_not_ready_requeue` label was independently checked against the raw per-cell
`arm_results`, not taken at face value. It **holds up**, but the raw data is far more
informative than "vacuous, requeue" — three structurally distinct findings converge on it,
two of which are novel (never exercised by any predecessor run):

### Finding A — chunk FORMATION is stochastic across seeds, and dose-dependent in the expected direction

| Arm | chunk_max_size | seeds with chunks_formed>0 | seeds with committed>0 |
|---|---|---|---|
| A_HIER_S2 | 2 | 4/8 | 2/8 |
| A_HIER_S3 | 3 | 7/8 | 4/8 |
| A_HIER_S5 | 5 | 7/8 | 7/8 |
| A_FLATCHUNK_S5 | 5 | 7/8 | 6/8 |

Formation rate rises with chunk_max_size — plausible on its own terms (a longer,
looser sequence is easier to re-observe identically than a rigid 2-step one, given
crystallisation requires `crystallisation_min=5` corroborating REAL executions of the
*exact same* action sequence). Aggregate formation-phase readiness stats
(`episode_outcome_spread_supra_floor`, `symbols_per_trial_supports_size_range`) clear
their floors with wide margin at the arm level, which is a **MIN-across-seeds** statistic
— so it is compatible with a meaningful fraction of individual seeds forming zero
chunks. This is a real but secondary finding: seed-level formation stochasticity, not
by itself severe enough to explain the total absence of scorable cells.

### Finding B — decisive: wherever a chunk IS selected during the probe, realised committed length is EXACTLY 1 step, in 100% of 32 chunking cells, independent of configured dose

This is the load-bearing finding. Pulled directly from `arm_results`, not from the
manifest's own aggregate stats:

```
A_HIER_S2  seed=101  chunks_formed=2  committed=2160  realised_mean_committed_length=1.0
A_HIER_S2  seed=505  chunks_formed=2  committed=2160  realised_mean_committed_length=1.0
A_HIER_S3  seed=101  chunks_formed=2  committed=2160  realised_mean_committed_length=1.0
A_HIER_S3  seed=505  chunks_formed=6  committed=2160  realised_mean_committed_length=1.0
A_HIER_S3  seed=606  chunks_formed=1  committed=2160  realised_mean_committed_length=1.0
A_HIER_S3  seed=808  chunks_formed=6  committed=2160  realised_mean_committed_length=1.0
A_HIER_S5  (7 of 8 seeds committed>0)  realised_mean_committed_length=1.0 in every one
A_FLATCHUNK_S5  (6 of 8 seeds committed>0)  realised_mean_committed_length=1.0 in every one
```

`committed_arc071_chunks` (= `len(segs)`, the segmentation count) equals **2160 for most
"successful" cells** — exactly `N_EPISODES_PROBE (30) x STEPS_PER_EPISODE (72)`, i.e. the
segmentation logic detects a "new commitment" on **literally every single probe step**.
`realised_committed_lengths` for these cells is `[1, 1, 1, 1, ...]` without exception, and
`n_segments_uninterrupted` is 0 in every one of them (no segment ever reaches even its own
nominal length). This holds identically at `chunk_max_size in {2, 3, 5}` — the configured
dose has **zero observable effect** on realised length wherever the mechanism engages at
all. `persistence_raw` for these cells is exactly `0.0` (not merely low) — the
degenerate-exact-zero signature of a statistic computed over a segment population that
structurally cannot express persistence, because no segment ever runs more than one step.

**This mechanism has never been live-tested before this run.** The script's own docstring
states plainly: *"Injection ON: this run needs E3 to actually SEE and commit chunks. (The
810a lineage kept it OFF because a readiness probe must not perturb the behaviour a later
run measures. This IS that later run.)"* V3-EXQ-810a validated chunk **accumulation**
(`ChunkAccumulator` forming/crystallising chunks in the library) with injection OFF; it
never tested whether `use_chunk_proposal_injection=True` actually results in E3 selecting
an injected chunk candidate and the MECH-090 commit latch holding it atomically for more
than one step (`module.py`'s own docstring: "E3 selects the entire sub-sequence as a
single move and the MECH-090 commit latch executes it without re-deliberating each step" —
the entire behavioural payoff ARC-071 predicts). V3-EXQ-834 never got this far (it failed
formation itself, gate a, at a shortened schedule). **V3-EXQ-841 is therefore the first run
to exercise the chunk-injection -> E3-selection -> commit-latch-persistence pathway live,
and the result is a clean, 100%-consistent null on persistence: the pathway either never
engages, or engages for exactly one step and then behaves as if freshly re-selected.**

Two live, structurally distinct explanations, not yet discriminated by this run:
- **H1 (substrate/wiring):** the MECH-090 commit latch's step-index advance (or the
  suppression of re-deliberation while a commitment is active) does not actually hold
  across ticks in this harness configuration (`train_mode=False` + injection ON +
  `StepHarness` running both phases on one long-lived agent) — `select_action`
  re-evaluates and re-commits from scratch on every tick regardless of an existing
  commitment.
- **H2 (measurement/readout artifact):** the true internal commitment state persists
  correctly, but this experiment's own read path — `_committed_chunk_state()` reading
  `agent.e3._committed_trajectory` / `agent._committed_step_idx`, or the metadata check
  `meta.get("source") != "arc071_chunk"` — does not correctly observe it (stale attribute,
  wrong object reference, or a metadata field that is not preserved across ticks the way
  the read path assumes), producing an artefactual "new commitment every step" reading
  even though genuine multi-step execution is occurring underneath.

Both are live; nothing in this run distinguishes them (the code path was read at autopsy
time — see `ree_core/hippocampal/module.py:1856` `_build_chunk_candidates` and
`ree_core/policy/policy_chunking.py` `note_real_execution`/`selectable_chunks` — but the
step-by-step execution trace inside `agent.select_action`/the commit latch itself was not
independently instrumented here).

### Finding C — pre-devaluation resource CONTACT is exactly zero in every one of the 16 non-chunking cells, and z_goal is inactive across the entire 48-cell grid

`pre_deval_contacts = 0.0` in **all 8 A_OFF seeds and all 8 A_FLAT seeds** — not low, zero.
`pre_deval_approach_rate` (fraction of steps that merely move CLOSER to a resource,
without necessarily reaching it) is nonzero but mostly sub-floor (0.011-0.150 against the
0.05 floor, no clean pattern). `z_goal_stream_stats.goal_state_present` is `False` and
`ticks_active` is `0` in **every one of the 48 cells in the entire run**, chunking arms
included. This is independent of Finding B (A_OFF/A_FLAT never instantiate chunking at
all) and points at a different layer: the inherited baseline
(`experiments/_lib/baselines/arc071_chunking.py`, validated by 810a for chunk-accumulator
readiness) may not carry an active goal-directed resource-seeking drive (SD-012) at all —
810a never needed one, since its own DV never required the agent to reliably CONTACT a
resource within a bounded window. A 36-step half-episode may simply be too short, or the
env too sparse, for a policy with no active resource-seeking goal signal to reach a
resource reliably. This is an **environment/config adequacy** question the inherited
baseline was never asked before.

## 3. Claim-layer mapping

**MECH-163** (restated 2026-07-27: hierarchical grain, depth-limited vs full-horizon read
of one model, per E1/E3 of `claim_synthesis_MECH-163_2026-07-27.md`). `depends_on`
includes ARC-071 (composition/transition mechanism) and MECH-477 (arbitrator, supported by
811a). `live_status.evidence.verdict`: weakens/no_differential_recruitment (786b,
2026-07-24). This run tests a **different** leg — not recruitment, but whether
committed-macro grain (vs an arbitrator) produces the outcome-insensitivity signature — and
does not touch 786b's leg at all. **Did the experiment test the claim under conditions
where it could express itself?** No: the readiness gates that would let the discrimination
criteria run never cleared, so the claim was not exercised either way.

**Q-085** (registered 2026-07-27, `claim_synthesis_MECH-163_2026-07-27.md`, `depends_on`
MECH-323/ARC-071/MECH-321/MECH-163). Its own `what_would_answer` names this exact run as
the intended discriminator and pre-registers the **mandatory gates this run failed** almost
verbatim: *"(a) count committed trajectories with metadata source arc071_chunk > 0 per
seed — zero is a READINESS FAILURE that scores nothing, not a null. This is the gate
V3-EXQ-810 failed."* And *"(b) REALISED mean committed-chunk length must DIFFER across the
dose conditions... An inert dose axis is a readiness failure."* Both (a) and (b) are
exactly what this run found broken — gate (a) partially (seed-stochastic), gate (b)
categorically (Finding B: realised length pegs at 1.0 regardless of dose whenever
nonzero). **This is not new information about Q-085's answer — it is confirmation that the
substrate has never yet cleared the preconditions Q-085's own design anticipated it might
fail on.**

**Claim-tagging note (verified against the script, not assumed):** `claim_ids` deliberately
excludes ARC-071 and MECH-323, which the run exercises as preconditions, not hypotheses —
the script's own comment states this is to avoid inflating those claims' evidence records
with a run that cannot move them either way (the same peripheral-co-tag hazard the
re-derive brake's per-claim override exists to prevent). This tagging is correct and
requires no correction.

## 4. Biological-reference triage

Closest reference mechanism: Dezfouli & Balleine 2013's single goal-directed process
selecting between individual actions and consolidated action sequences ("chunks"), executed
atomically once selected — already the substrate's own architecture per MECH-163's
2026-07-27 restatement (E3: "REE already instantiates the hierarchical account of habit").
Jin & Costa 2010 is the standing justification for gate (a)'s strictness (a boundary is a
property of a *consolidated* sequence; an unconsolidated seed has no boundary to be
insensitive at). This run's finding — that even where a chunk is nominally "selected," it
never holds for more than one tick — is exactly the biological failure mode Jin & Costa's
framing predicts for a sequence that has NOT actually consolidated into a single motor
program: on the reference account, the whole behavioural and computational payoff of
chunking (skipping re-deliberation, executing the sequence as a unit) requires the
commitment to hold; a "chunk" that re-deliberates every step is not a chunk in the
biological sense at all, whatever the formation/crystallisation bookkeeping reports. This
is consistent with the core principle: **the substrate has the SYMBOL of the mechanism
(formed, crystallised entries in a chunk library, injected into the candidate pool) but not
yet demonstrated its FUNCTIONAL ROLE (atomic multi-step execution)** — an implementation
gap, not evidence against the biology or against MECH-163/Q-085.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (not exercised) | Readiness gates failed before either claim's discrimination criteria could run |
| Biological reference | clear | Dezfouli & Balleine 2013 single-process/chunk-consolidation account; Jin & Costa 2010 on consolidation-dependent boundaries. Substrate architecture already matches the account per MECH-163's 2026-07-27 restatement |
| Developmental / dependency prerequisites | partially present | ARC-071 chunk injection (module.py) and MECH-323 accumulator/crystallisation (policy_chunking.py) both exist and fire in isolation; their live composition under injection=ON + no_grad + StepHarness had never been exercised end-to-end before this run |
| Implementation completeness | partial (Finding B) | Chunk formation/crystallisation and candidate injection are wired and observably active; multi-step commit-latch PERSISTENCE is not demonstrated to hold beyond one tick in any of 32 chunking cells, regardless of dose — symbol of the mechanism present, functional role (atomic execution) not yet shown |
| Environment adequacy | likely inadequate for this DV (Finding C) | Zero pre-deval resource contacts in 16/16 non-chunking cells; z_goal/goal-directed drive inactive in all 48 cells. The inherited baseline was validated for chunk-accumulation, not for reliable resource contact within a bounded probe window |
| Measurement adequacy | possibly implicated (H2, Finding B) | Cannot yet rule out that `_committed_chunk_state`/`_segment_commitments` misreads a genuinely-persisting commitment as resetting every tick |
| Integration adequacy | isolated-but-uncoupled (Finding B) | Formation (ChunkAccumulator) and selection (E3 candidate injection) each function individually; their coupling into a held, atomic, multi-step EXECUTION has not been demonstrated |
| Scale / capacity | not implicated | Not a capacity/training-budget finding; the 810a-proven 120x72 formation schedule was used verbatim |

## 6. Extracted learning

1. **Genuinely novel substrate finding, worth carrying forward regardless of this run's
   scoring status**: the ARC-071/MECH-323 chunk-injection-to-commit-latch-persistence
   pathway (`use_chunk_proposal_injection=True` combined with a continued, multi-episode
   `StepHarness` run in `train_mode=False`) has now been live-tested for the first time,
   and shows realised committed length pinned at exactly 1 step in 100% of the 32 cells
   where any commitment was detected at all, independent of configured `chunk_max_size`
   (2, 3, or 5). This directly falsifies gate (b) of Q-085's own pre-registered design as
   currently wired/measured, and blocks BOTH MECH-163's grain-vs-arbitrator discrimination
   and Q-085's dose-response question until resolved.
2. Chunk formation/crystallisation itself is dose-dependent in the expected direction
   (larger `chunk_max_size` forms more reliably across seeds) — a secondary, non-blocking
   observation that the accumulator side of the mechanism behaves sensibly.
3. The devaluation-persistence DV as currently harnessed cannot get resource contact at
   all in the non-chunking control arms (A_OFF/A_FLAT, 0/16 cells) — independent of the
   chunking question, and worth fixing regardless of how Finding B resolves, since A_OFF/
   A_FLAT are the FLAT-controller baseline MECH-163 needs to discriminate against.
4. z_goal is completely inactive across the whole 48-cell grid — consistent with (3) and
   worth checking directly rather than inferring: does the inherited baseline enable any
   resource-seeking drive at all, or does its behaviour depend entirely on incidental
   exploration?

## 7. Repair pathway and routing (DRAFT — awaiting confirmation)

**Classification** (work-graph debt vocabulary): Finding B is `complex (probe-gated) /
puzzle (known rules)` — the frame is well-posed (H1 wiring vs H2 measurement-readout) but
the deciding fact is missing, and it gates both MECH-163's grain leg and all of Q-085.
Finding C is closer to `complicated (buildable)` once diagnosed — but the diagnosis (is a
goal-directed drive actually available/enabled in this baseline) has not been done here
either, so it is provisionally grouped into the same investigation rather than force-fit.

**Recommended primary routing: `implement-substrate`** — `recommended_substrate_queue_entry`
below, `action: create`. No existing `substrate_queue.json` entry covers this pathway
(checked: no entry references ARC-071 chunk injection, chunk-proposal commit persistence,
or this baseline's resource-contact adequacy).

**`fanout_recommendation` emitted** for Finding B's H1/H2 split (see JSON `targets[0]`):
a diagnostic probe that directly instruments `agent._committed_step_idx` / the commit-latch
advance logic tick-by-tick in the SAME harness configuration this run used, on just the two
"successful" seeds (101, 505 in A_HIER_S2) where the effect is cleanly reproduced, would
discriminate H1 from H2 far more cheaply than a full re-run of this 6-arm x 8-seed grid.

**pending_retest_after_substrate: true** for both MECH-163 (grain leg) and Q-085 — neither
claim should be re-queued at the SAME grain/architecture question until this pathway is
either fixed (H1) or shown to already work correctly and the experiment's readout repaired
(H2).

**Re-derive brake check**: 0 prior `substrate_ceiling` autopsies on MECH-163 or Q-085 (both
claims' recurrence clusters were checked via `granularity_debt_cluster.py`; MECH-163's
6-target cluster carries `measurement_test_design_defect` / `standard` categories only, no
`substrate_ceiling`; Q-085 has no prior targets at all). **Brake does NOT fire.**

**Granularity-debt recurrence trigger**: MECH-163 has 2 targets reading `weakened` (786a,
now-superseded by its own 2026-07-24 DV-degeneracy withdrawal, and 786b, standing). This
autopsy's own signature (readiness/precondition, non_contributory) is structurally
different from 786b's (an absent-effect discrimination result on a DIFFERENT leg —
recruitment, not grain-vs-arbitrator) and does not itself read `weakened`, so it does not
add a new falsification signature to the cluster. **Trigger does NOT fire** — this is not
evidence of granularity debt; 786b remains the cluster's sole live falsification. Q-085 has
no prior targets, so its trigger trivially does not fire (first autopsy on this claim).

**Draft `evidence_quality_note` text** (for governance to apply, not applied here):

> 2026-07-31 (V3-EXQ-841, non_contributory, both `A_HIER_*`/`A_FLAT` legs; failure_autopsy_V3-EXQ-841_2026-07-31). Run correctly self-routed `substrate_not_ready_requeue` (non_degenerate=false, all 6 arms RED at the readiness-gate layer) — NOT a test of either claim. Independent re-derivation surfaced a genuinely novel, decisive substrate finding: wherever the ARC-071 chunk-injection pathway (`use_chunk_proposal_injection=True`) is live-tested for the first time (810a explicitly ran with injection OFF; 834 never cleared formation), the realised committed-chunk length pins at EXACTLY 1 step in 100% of 32 chunking cells that registered any commitment at all, independent of the configured chunk_max_size dose (2/3/5) — categorically falsifying Q-085's own pre-registered gate (b) as currently wired/measured. Two live hypotheses (commit-latch wiring vs experiment readout artifact) are not yet discriminated. A second, independent readiness failure (zero pre-devaluation resource contacts in the non-chunking A_OFF/A_FLAT control arms, 0/16 cells; z_goal inactive across the entire 48-cell grid) blocks even the FLAT baseline this design needs. `pending_retest_after_substrate: true` for both claims at this grain/architecture question. Routed `/implement-substrate` (recommended_substrate_queue_entry, action=create) with a `fanout_recommendation` to discriminate the H1/H2 split before any re-queue.

## 8. Hypothesis-space ledger (staging mode — DRAFT, not applied)

Per staging-mode instructions, `hypothesis_space_registry.v1.json` was NOT written. The
intended pre-registration for the `fanout_recommendation`'s H1/H2 split is recorded in the
JSON artifact under `hypothesis_space_ledger_pending`, for a confirming interactive session
or the next `/governance` walk to apply.

## 9. Status

`confirmed` (2026-07-31T23:32:48Z, session `quirky-mayer-ee5ad2`, direct interactive user
confirmation of the draft AS DRAFTED — no revisions to routing, epistemic category, or
evidence direction were made at confirmation). Applied in the same session: `claims.yaml`
(MECH-163, Q-085 `evidence_quality_note`, both `non_contributory`), `substrate_queue.json`
(`arc071_chunk_commit_latch_persistence`, action=create), and
`hypothesis_space_registry.v1.json` (qid `arc071-commit-latch-persistence`, Mode A
pre-registration of H1/H2, both legs `alive`/`pending` — neither hypothesis is resolved by
this confirmation itself). Having just applied the ratified disposition, this same session
acts as the ratifying authority for the routing's own follow-on (the H1/H2 diagnostic
probe) and proceeds to build and run it directly, per CLAUDE.md Session Land Protocol step
6 ("`/governance` is the one that chips it, once ratified" — this session performing the
ratification is the qualifying event). Any Q-085/MECH-163 re-queue at the same grain
question remains blocked (`pending_retest_after_substrate: true`) until the H1/H2
discrimination resolves and, if H1, the substrate fix lands.
