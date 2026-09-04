# Science wave 2 -- campaign plan of record (2026-09-04)

**Status: PLAN OF RECORD, awaiting the user's three decisions in section 6. Ledger curation in section 4 has been applied.**

- Written: 2026-09-04T08:15Z by session `science-wave-coord-20260904` (Mac, user-present, `TASK_CLAIMS` claim of the same name).
- Sources read: `docs/CURRENT_FRONT.md` (generated 2026-09-03T20:25Z), `insights_report.md` recommendations, `evidence/planning/inter_governance_workset.v1.json` (generated 2026-09-04T06:50Z), `evidence/planning/igw_routine_ledger.json`, `TASK_CHIPS.json` (283 open at read time), `ree-v3/experiment_queue.json` on origin, the live-status branch, `hcloud server list`, SSH to `ree-cloud-4`/`ree-cloud-5`, the 976/978/980/981/963a/642b/ext-cluster autopsies, and the 2026-09-03 governance + daily-science entries in `WORKSPACE_STATE.md`.
- Sister docs: `fleet_commit_sequencing_redesign_20260829.md` (sections 10-11, the pause pattern), `pause_pressure_recurrence_rootcause_staged_20260902.md` (why curation alone is not the lever), the 2026-09-01 `planning-metabolise-20260901` wave-1 close in `WORKSPACE_STATE.md` (the pattern this wave repeats: a small number of named campaign sessions, landed incrementally, not the resident dispatchers).

---

## 0. State at planning time (facts, no interpretation)

| Fact | Value |
|---|---|
| Experiment queue on `origin/main` | **empty** (0 pending, 0 claimed). The local Mac checkout was 1 commit behind and still showed 6 items -- stale. |
| Fleet | `ree-worker-1` hub running (runner retired); `ree-worker-2`/`-3` off; `ree-worker-4` and `ree-worker-5` **powered on and idle** (load 0.00 / 0.12). |
| Dispatchers (`ree-metaworker.service` on cloud-4/5) | **inactive since 2026-09-01T19:15Z** (user pause for the Claude update; confirmed by SSH, `systemctl` shows the unit dead and no timer). Heartbeat files still say `dispatching` -- they assert present tense after death, per memory. |
| Mac dispatch service | `max_claude_sessions: 0` -- dispatching nothing. |
| Runs landed since the last governance walk (2026-09-03T20:44Z) | V3-EXQ-996 PASS/diagnostic (GAP-14 live phase gate), **V3-EXQ-1000 PASS/diagnostic (SD-e1 ITEM 3: cr_ratio(h=1) bar cleared 6/6 -- the live front's critical-path run)**, V3-EXQ-997 FAIL/weakens (MECH-162), V3-EXQ-999 FAIL/substrate_not_ready (MECH-161), V3-EXQ-1001 FAIL/weakens (EXT-005/SD-031 -- after 995 gave first support). **All five unreviewed**; `pending_review.md` reads 0 only because it was generated before they landed. |
| SD-e1 line | ITEM 1 (965), output_proj A/B (968), **ITEM 2 (976, confirmed 09-02)**, H-c readout probe (980, confirmed 09-03: H-c eliminated, routed `implement-substrate` amend for two latent test-design defects), ITEM 3 (1000, unreviewed). `CURRENT_FRONT.md` and `substrate_queue.json`'s `f_dominance_conversion_ceiling.depends_on_unresolved` still say ITEM 2 is "owed, unminted" -- registry drift, not an open item. |
| SD-018 line | Amend landed 09-02; validation V3-EXQ-978 FAIL -> confirmed autopsy 09-03: shape (a) validated-negative, OFF arm already decodes the field (r2 0.71/0.86), so the deficit is consumer or geometry; routed to a capacity-matched frozen-latent oracle-adapter discriminator (chip below). New hypothesis-space question `zworld_actor_adequacy_locus` (H-B vs H-C). |
| Open chips | 283 at read time: **181 auto-minted `chip-proposal-exp-*`** (all minted 2026-09-02), 5 decision, 1 report, ~96 session-authored work chips. |
| Of the 181 proposal chips | 122 name an `EXP-` id that **no longer exists** in `experiment_proposals.v1.json` (ids renumbered on regen); 50 name an id whose claim **moved** under them (title says ARC-037, id now ARC-043, the off-by-one pattern); 1 points at a `blocked_substrate` proposal; **8 are coherent** (`VIABLE` in the triage file). |
| IGW workset | 253 items: 31 ready, 164 blocked, 0 in flight, 0 assigned. Ready items that are science: `MECH465-COMMIT-GATE-HEADROOM`, `dv-dynamic-range-precondition-class` (staged as worktree `igw-222-substrate-ready-dv-dynamic-range`, awaiting human launch), three `Confirm evidence` items (MECH-267/057b/489), proposals for EXT-008/EXT-009/IMPL-008/IMPL-016. The other ready items are `(plan reconcile)` rows on V4 plans. |

Triage file for the proposal chips: scratchpad `proposal_chip_triage.json` (per-chip bucket); the per-chip withdrawal notes in the ledger carry the same reason.

---

## 1. Where the tokens were going, and the four levers

The 2026-09-02 root-cause pass already showed curation is not the lever for the *generator*; this plan takes the generator arm as done (Fix A, floor 10) and acts on what is left.

1. **172 dead proposal chips withdrawn** (section 4). Each would have cost a full headless `/queue-experiment` session that ends at "proposal id not found" or queues the wrong claim. With the tick's floor at 10 the pool re-fills to 10 coherent chips, not 181.
2. **Do not restart the resident cloud dispatchers for this wave.** They are category-blind within a lane and would resume against 96 work chips of which perhaps 20 are on the front. This wave is **12 named sessions** (section 5), the same shape as the 2026-09-01 wave-1 close, each carrying a campaign brief with a START-TIME STOP-CHECK.
3. **Build-before-queue ordering.** Six of the seven 2026-09-03 FAILs shared one defect (criterion threshold outside the DV's achievable range). Queueing the five redesigns before the `dv_headroom` precondition kind exists would re-autopsy the same defect five times. C2 lands the lint first.
4. **HOLD, with a review date, everything not on the 39-of-43 chain.** Twelve substrate builds, all coordination-plane hygiene, and all V4 plan-reconcile rows are held to 2026-09-11 (section 3). Holding is a stated reason plus a date, per the curation lane rule; none of these are withdrawn.

Model routing follows `dispatch_remote_launch.WORK_TYPE_MODEL_DEFAULTS`: Opus for `/queue-experiment`, `/implement-substrate`, `/claim-synthesis`, root-cause code; Sonnet for registry writes, lit pulls, record-keeping. Subagent drafts stay in the scratchpad; the main session lands (memory `feedback_subagent_economy_by_model`).

---

## 2. Campaigns

Ordering is by dependency, then by distance from the front. C0 gates C1 and C2's queue sessions; C3, C4, C5 are independent of C0 and can start immediately.

### C0 -- Adjudicate the 2026-09-03 wave (governance + autopsy; inline, NOT chipped)

`/governance` and `/failure-autopsy` re-derive their own worklists, so this campaign is reported, not chipped (CLAUDE.md "Report inline, do not chip"). One session, Opus, user present, because three items are human calls.

1. Regenerate `pending_review.md`; it will list 996, 997, 999, 1000, 1001.
2. **V3-EXQ-1000 adjudication is the front-moving item.** cr_ratio(h=1) bar cleared 6/6 on the rollout-endpoint contrastive. Decide: does this license the INV-088 / MECH-135 `pending_retest_after_substrate` retest, and does it change the H-B/H-C prior for the 978 discriminator (C1.1)? Record the answer on the `SD-e1-rollout-consistency-training` entry and on `zworld_actor_adequacy_locus`.
3. Autopsy 997 (MECH-162 weakens), 999 (MECH-161 substrate_not_ready), 1001 (EXT-005/SD-031 weakens, one day after 995 supports -- a genuine conflict, not a re-derive).
4. Apply the deferred proposal writes EVB-1445 (blocked_substrate), EVB-1446 and EVB-1447 (executed). This absorbs the remainder of `chip-20260903-daily-science-deferred-registry-writes` (the ITEM 3 substrate_queue amend was already applied by governance-20260903 on the orchestrator's behalf); resolve that chip done when the three writes land.
5. **Human decision: E3 channel-scale normalisation (GFLAG-0116 + GFLAG-0051).** It is the third named `depends_on_unresolved` on `f_dominance_conversion_ceiling` and the insights report's recommendation 3. Until disposed, every 936-family / 654h-class conversion falsifier stays refused. This is a `puzzle (known rules)` node: the fact needed is a design decision, not a run.
6. Registry drift: remove "SD-e1 ITEM 2 validation run (owed, unminted)" from `f_dominance_conversion_ceiling.depends_on_unresolved` (976 ran and is confirmed); regenerate `CURRENT_FRONT.md` so the gate line no longer names ITEM 2.

### C1 -- Live front: is the z_world latent usable by an actor? (`chip-20260904-campaign-c1-zworld-actor-adequacy`)

The insights report's recommendation 1 and the 978 autopsy's routing. Two sessions after C0.

| # | Item | Skill / model | Note |
|---|---|---|---|
| 1 | `chip-20260903-exq978-oracle-adapter-discriminator` | `/queue-experiment`, Opus | Freeze z_world as 978 left it, behaviour-clone the `local_view_greedy` oracle with an adapter **capacity-matched to the policy head** (red-team amendment 5). Discriminates H-B (consumer) from H-C (geometry). Queue only this; the H-C corroborator is queued only if the adapter fails. |
| 2 | `chip-20260902-mech465-zworld-warmup-spike` | probe, Opus | IGW-20260904-217 ready; user-approved redirect: correct the `MECH465-COMMIT-GATE-HEADROOM` registry entry, then run the z_world-warmup-confound-free dispersion spike instead of the gate-rescale build. Same latent, same question. |
| 3 | SD-e1 next step, minted by C0 | `/implement-substrate` or `/queue-experiment` | Whatever C0 item 2 decides: either the INV-088/MECH-135 retest, or the 980-routed amend (the `registered_majority_seeds` constant read by no verdict; `_damping_verdict` excludes the ON arm). Not pre-chipped: doing so would race C0's ratification (the autopsy-follow-on rule). |
| 4 | `chip-20260903-gov-rotate-1-978-trial-record` | record, Sonnet | Gate is open (978 autopsy confirmed). Record the first GOV-ROTATE-1 trial on the claim; the autopsy's section 9 already answers it (smaller, cheaper, more discriminating). Ten-minute item. |

Session A = item 1. Session B = items 2 + 4. Item 3 gets its own session once minted.

### C2 -- Measurement validity: put the criterion inside the DV's range (`chip-20260904-campaign-c2-dv-headroom`)

Build first, then queue. One build session, then three queue sessions in parallel.

| Order | Item | Skill / model |
|---|---|---|
| 1 (build) | `chip-20260903-dv-headroom-precondition-build` -- the `criterion_exceeds_achievable_range` lint in `validate_experiments.py` plus a `dv_headroom` precondition kind. **This is the same work as IGW-20260904-222, already staged as worktree `.claude/worktrees/igw-222-substrate-ready-dv-dynamic-range` with an active auto-claim; launch that worktree rather than a fresh one, and resolve `chip-igw-20260904-222` (the human-launch decision chip) when you do.** | `/implement-substrate`, Opus |
| 2a | `chip-20260903-exq983-redesign-headroom-bar` (EXT-002), `chip-20260903-exq991-redesign-action-level-dv` (EXT-004), `chip-20260903-exq993-redesign-harm-readout` (ARC-021/MECH-069/EXT-003) -- one session, they share the ext-cluster autopsy and its weak-null residuals. 993 needs the MECH-069/ARC-021 lit pull from C4.2 only if the redesign wants the literature's effect sizes; do not block on it. | `/queue-experiment` x3, Opus |
| 2b | `chip-20260903-exq642c-blocked-agency-headroom-dv` + `chip-20260903-exq981a-mech027-requeue` (check the inverted hazard-band assignment first, per red-team amendment 3) | `/queue-experiment` x2, Opus |
| 2c | `chip-20260903-sd-phasic-burst-decay-warmup-headroom-build` (MECH-063 regulator defects from the 963a autopsy), then queue V3-EXQ-963b in the same session | `/implement-substrate` then `/queue-experiment`, Opus |
| 2d | `chip-20260901-exq822e-raw-stage-dv-redesign` (SD-082 validation; the tanh-manufactured range is this defect class). Stale claim released 2026-09-04T08:02Z; the untracked draft driver is still on the shared ree-v3 checkout. | `/queue-experiment`, Opus |

Every 2x session uses the new `dv_headroom` precondition kind; if the build has not landed on `origin/main` when a 2x session starts, that is its STOP.

### C3 -- Unblock the most retests per build (`chip-20260904-campaign-c3-unblockers`)

Chosen by `unblock_count` in the workset, not by novelty. Independent of C0.

| # | Item | Skill / model | Unblocks |
|---|---|---|---|
| 1 | **ContextMemory write-path validation** (entry `contextmemory-write-path-addressing-degeneracy`, `implemented_pending_validation` since 08-18, validation never queued): diagnostic ablation, flag ON vs OFF, `n_occupied_slots >= 2` in both arms on >= 3/5 seeds per the entry's own `failure_record`. Mint as `chip-20260904-contextmemory-writepath-validation` (recorded with this campaign). | `/queue-experiment`, Opus | IGW-20260904-226/227 (ARC-045 retest), `chip-20260818-mech152-redesign-queue-gated` (V3-EXQ-939, spec already written), GFLAG-0044 |
| 2 | `chip-20260902-waypoint-proximity-field-observable` -- waypoints only visible inside the 5x5 local view, so every goal-maintenance / subgoal DV sits at random-walk level | `/implement-substrate`, Opus | INV-086, MECH-428, every navigation-dependent DV |
| 3 | `chip-20260902-unowned-substrate-blockers` -- 13 blocked proposals name a substrate no queue entry owns | registry, Sonnet | routes 13 dead-ended proposals |

Follow-on, minted by item 1's session on a PASS: queue V3-EXQ-939 from `mech152_measurement_redesign_gated_20260818.md`.

### C4 -- Literature that a live experiment is waiting on (`chip-20260904-campaign-c4-lit`)

All Sonnet; can run as one session or ride the existing `ree-lit-pull-am` scheduled task (daily 07:00) over three mornings -- the campaign brief lists the order.

1. `chip-igw-20260901-233` -- ARC-052 (977 just gave its FIRST experimental support; the lit side is empty).
2. `chip-20260903-mech069-arc021-litpull` -- feeds the 993 redesign (C2.2a).
3. `chip-20260902-arc121-harm-ethics-lit-gap`.
4. `chip-20260903-litpull-sleep-reorg-remaining-nine`.
5. `chip-20260903-arc120-framing-evidence-tagging` (`/claim-synthesis`, Opus -- the one non-lit item; tag instance evidence at FRAMING level).

### C5 -- Stop the generator minting dead chips (`chip-20260904-campaign-c5-proposal-id-stability`)

Part 2 of `chip-20260902-campaign-proposalindexer-dataintegrity` (part 1 covers carry-forward bleed, id reference rot, retire-lane displacement, dry-run blind spot). One session, Opus, ordered:

1. **Stable proposal ids** -- `chip-20260902-exp-proposal-id-instability`, `chip-20260903-proposal-tick-unstable-expid`, `chip-20260903-proposal-id-reassigned-on-regen` are one defect: `EXP-*`/`LIT-*` ids are positional and renumber on any proposal-set change. This is the root cause of the 172 chips withdrawn today. Fix once; resolve all three.
2. `chip-20260903-proposal-tick-honors-claim-gates` -- the minter re-mints for claims whose notes carry an explicit gate.
3. `chip-20260904-litlane-nonevidenceable-claimtypes` -- lit proposals minted for claims with no external evidenceability.
4. `chip-20260902-proposalfloor-vs-queuestarvation-tuning` -- measure whether floor 10 sustains the science tier once ids are stable (it cannot be measured before).
5. `chip-20260902-proposal-chip-title-claim-mismatch-audit` -- explained by item 1; resolve with the finding, do not re-audit.

---

## 3. HOLD lane (reason + review date 2026-09-11, or the next wave-planning session, whichever is first)

Nothing here is withdrawn. A held chip keeps its `open` status; the hold is this section.

- **Substrate builds not on the 39-of-43 chain** (12): `chip-20260901-mech035-vector-valence-substrate`, `chip-20260902-mech494-context-arbitrator-substrate`, `chip-20260902-mech039-control-channel-substrate-gap`, `chip-20260902-e3-channel-commensurability` (**gated on C0.5** -- the GFLAG-0116/0051 disposition decides whether this is V3-required at all), `chip-20260902-mech037-provenance-gate-substrate`, `chip-20260902-mech065-rc-conflict-s5-substrate`, `chip-20260902-mech468-anchor-relational-dump-substrate`, `chip-20260902-mech157-sensory-hc-gate-wiring`, `chip-20260902-arc131-coalition-endogenous-recruitment-driver`, `chip-20260902-zgoal-parent-e3-consumer`, `chip-20260902-mech320-implement-noop-margin-dv` (scope amended by governance-20260903: a margin DV alone cannot move a vigor scalar with no source), `chip-20260903-impl022-uncertainty-nondissipation-field`. Reason: each is a full Opus `/implement-substrate` session on a node that does not move v3 closure this wave.
- **Science candidates for wave 3**: `chip-20260901-gflag0080-mech235-arbitration-rerun` (real, cheap, off-front), `chip-20260814-queue-causal-sleep-matched-arm` (gated on the 920 retrospective), `chip-20260818-mech152-redesign-queue-gated` (moves to C3 follow-on on the ContextMemory PASS), the 8 coherent proposal chips (`chip-proposal-exp-0893/0904/0934/0936/0973/1013/1069/1096`), the three IGW `Confirm evidence` items (MECH-267/057b/489), `chip-igw-20260903-242` (EXT-009), `chip-20260903-dea001-v3-channel-exposure-audit`, `chip-20260902-arc113-stage-implementation-audit`, `chip-20260902-arc044-mech152-arc016-no-shared-readout`, `chip-20260903-e3eb-inert-marker-audit`.
- **Registry/prose hygiene** (cheap, Sonnet, bundle at review): `chip-20260830-sd082-822d-queued-flag-stale`, `chip-20260902-plan-prose-460k-724-ran-not-queued`, `chip-20260902-ext009-exp0534-blocked-substrate-status`, `chip-20260903-arc027-lit-schema-undeclared-keys`, `chip-20260902-brake-wrapped-substrate-status`, `chip-20260902-governance-mixed-diagnostic-fail`, `chip-20260902-failure-autopsy-bears-on-tagging`, `chip-20260902-dryrun-scoring-exclusion-gap`, `chip-20260902T1250-dryfilter-manifest-shape-blindspot`, `chip-20260902-indexer-run-timestamp-rendering-drift`, `chip-20260902-use-before-def-lint-b`, `chip-20260903-retroactive-duplicate-chip-sweep`, `chip-20260903-igw-id-collision-shared-chipref`.
- **Coordination plane / fleet** (the existing `chip-20260902-campaign-fleethygiene-cloud4-staterepair` bundle plus): refwedge items, `chip-20260902-r4-cloud-workrepo-puller-gap`, `-r5-`, `-checkoutdiverged-fullfix-`, the two 2026-09-03 puller decision chips, `chip-20260902-cloud5-stash-scripts-wip-verify`, the two GC-sweep chips (154 + 1 worktrees), `chip-20260826-worktree-graveyard-triage-and-gc`, `chip-scriptscorpus-dlaptop-sweep-12-*` (12 red files in the umbrella corpus -- the one item here worth pulling forward if any C-session trips on it), `chip-20260902-fleetidle-syntax-error`, `chip-daemondrift-dlaptop-mac-serve`, `chip-stagedskew-ree-cloud-4-ree-assembly`, `chip-20260902-cloud4-divergent-manifests-862a-869a`, `chip-20260902-preexisting-corpus-reds-repin`, `chip-20260902-subcase-b-trunk-red`, `chip-20260902-settingslocal-wildcard-permission-rules`, `chip-20260828-bashgate-*`, `chip-20260903-worktree-guard-bash-blindspot`, `chip-20260903-handover-retired-timer-gate`, `chip-20260903-prepull-grader-changed-field`, `chip-20260828-chiparchive-*`, `chip-20260828-chipledger-noop-*`, `chip-20260901-igwworkset-md-mergegap`, `chip-20260901-dispatch-bg-wait-ceiling-kills-fanout`, `chip-20260901-doctrine-shrink-retired-telemetry`, `chip-20260904-refwedge-r1-rate-cost-remeasure` (dated: not before 2026-09-11 by its own text), `chip-20260901-gflag0091-unblocks-claims-edge-repair`, `chip-classifierblock-dlaptop-*`. Reason: none blocks running an experiment on the cloud (the runner pulls for itself; 995-1001 ran on cloud-2/3/4 on 09-03).
- **Design / thought**: `chip-20260826-representation-authority-selection-bottleneck`, `chip-20260826-thought-digestion-wave-grouping-design`, `chip-20260827-capability-contract-plasticity-vocab`.
- **Decision chips left for the user**: `chip-pausepressure-dlaptop-g5` (this plan is the backlog-arm answer it asked for; the generator arm is C5), `chip-20260901-heartbeat-retirement-runbook`, `chip-20260903-untracked-manifest-collision-recurring-class`, `chip-20260903-cloud5-no-puller-for-work-repos`.
- **Telemetry**: `chip-queuefloor-fleet-g6` (kind report; it clears itself when C1/C2 queue).

---

## 4. Ledger actions taken by this session (all coordinator-acknowledged)

- **Withdrawn 173 `chip-proposal-exp-*` chips** (1 by hand, 172 by `scratchpad/withdraw.sh`): 122 dead ids, 50 title/claim mismatches, 1 `blocked_substrate`. Each note names the reason and this file. Kept open: the 8 coherent ones (HOLD lane). Expected consequence: the next `com.ree.proposaldripfeed` tick mints up to 2 more to reach its floor of 10, with current ids.
- **Released** the stale claim on `chip-20260901-exq822e-raw-stage-dv-redesign` (claimant's TASK_CLAIMS entries closed NOT LANDED on 09-03; dispatchers dead since 09-01).
- **Withdrawn as duplicate**: `chip-20260903-igw-retire-lane-blind` (same defect as `chip-20260902-igwtick-retire-proposal-lane-displacement`, which part 1 of the proposal-indexer campaign already carries).
- **Recorded** five campaign chips `chip-20260904-campaign-c1..c5-*` and one new work chip `chip-20260904-contextmemory-writepath-validation` (C3.1). Member chips stay open; the campaign brief tells the session to resolve each member as it lands. No chip was claimed (the never-preclaim rule).

---

## 5. Dispatch recipe

Twelve sessions. Run as Mac-coordinated named sessions (interactive or `claude -p` background agents from this checkout), not by re-enabling the cloud dispatchers -- the dispatchers' lease/wrapper machinery belongs to the `/metaworker-orchestrate` session and is left alone.

| Slot | Sessions | Depends on |
|---|---|---|
| Now | C0 (1, user present); C3.1, C3.2, C3.3 (3); C4 (1); C5 (1); C2 build (1, launch the staged igw-222 worktree) | -- |
| After C0 | C1-A, C1-B (2) | C0.2 |
| After C2 build on origin | C2-2a, C2-2b, C2-2c, C2-2d (4; 2d may fold into 2b) | C2.1 |
| After C0 mints it | C1 item 3 (1) | C0.2 |

Every session: open its own `TASK_CLAIMS` claim first, `chip_ledger.py claim` the campaign chip, run the per-item STOP-CHECK (`task_claim.py check --resources`, fresh ledger read, `git log` on the target) before each item, land each item separately with `ree_commit.py`, resolve the member chip, and close with `/session-land`. Compute: the cloud scaler powers workers 2/3 on when the queue has claimable work; nothing here needs a manual power-on.

Expected queue output of the wave: 978-discriminator, MECH-465 spike readout, 983a/991a/993a, 642c, 981a, 963b, 822e, ContextMemory validation, plus whatever C0 mints for SD-e1 -- ten to eleven runs, all with pre-registered bars inside their DVs' measured ranges.

---

## 6. Decisions for the user

1. **Run mode.** This plan assumes named Mac-coordinated sessions and leaves the cloud dispatchers stopped. If you would rather restart the resident dispatchers, C1-C5 are already the campaign bundles the curation lane wants, but the HOLD lane in section 3 is then advisory only -- the dispatcher will eventually reach those chips.
2. **`ree-worker-4` and `ree-worker-5` are powered on and idle** since 2026-09-01T19:15Z (dispatchers dead, no runner on -5, runner failsafe dead on -4). The scaler's orchestrator veto reads a stale `chips_open_work > 0` heartbeat and keeps them up. Not touched by this session (orchestration is the orchestrator session's). Powering them off until a wave needs dispatch is a cost decision only.
3. **E3 channel-scale normalisation (GFLAG-0116 / GFLAG-0051)** -- C0.5. A design call, not a run; it un-gates or re-scopes `f_dominance_conversion_ceiling` and decides whether `chip-20260902-e3-channel-commensurability` is a V3 build.
