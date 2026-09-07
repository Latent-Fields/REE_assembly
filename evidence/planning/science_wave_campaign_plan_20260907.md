# Wave 4 -- housekeeping campaign + science campaigns, plan of record (2026-09-07)

**Status: PLAN OF RECORD. Ledger actions in section 5 have been applied. Section 6 lists the decisions only the user can make; nothing else is gated on them.**

- Written: 2026-09-07T07:26Z-08:40Z by session `campaign-split-20260907` (Mac `DLAPTOP`, main checkout; `TASK_CLAIMS` claims `campaign-split-20260907` + `campaign-split-20260907-igw`). No experiment was queued by this session.
- User instruction: split the outstanding IGW work and the durable chip ledger into ONE housekeeping campaign and SEPARATE science campaigns, to cut token spend and move the science faster.
- Sources read: `igw_routine_ledger.json` (178 entries: 89 completed, 82 completed_resumable, 4 staged, 3 spawn_failed; 120 dispositions) + `igw_routine_log.md` + `igw_assignments.json` (0 live); `inter_governance_workset.v1.json` (04:21Z: 247 items, 29 ready, 0 in flight); `TASK_CHIPS.json` (126 open: 118 work, 2 decision, 1 report; 0 claimed); `hold_lane.v1.json` (78 held, review 2026-09-11); `TASK_CLAIMS.json` (1 active); `ree-v3/experiment_queue.json` on origin (empty; V3-EXQ-1007 claimed on ree-cloud-2); `pending_review.md` (1: V3-EXQ-1006 PASS, diagnostic, autopsy owed); `substrate_queue.json`; `CURRENT_FRONT.md` (04:21Z); the V3-EXQ-1006 manifest; `hcloud server list`; commits since 2026-09-06T14:00Z on all three repos.
- Predecessor: [`science_wave_campaign_plan_20260906.md`](science_wave_campaign_plan_20260906.md) (wave 3, W3-C0..C4). Its execution record is section 0 here; its HOLD lane is carried forward in section 4.

---

## 0. What happened since wave 3 (facts)

| Wave-3 item | Outcome |
|---|---|
| C0 (inline governance) | **Done.** 983a autopsied + ratified (`governance-20260906-1604`); the 47-claim thought-digestion batch applied (`ada5d97af0`) and 80 flags raised (GFLAG-0139..0218); ContextMemory decision recorded (`7a21722fee`); all five user decisions applied (workers 4/5 off, R7 done, pause-pressure hold-lane predicate landed). |
| C1.1 SD-e1 var-bar portfolio | **Ran.** V3-EXQ-1006 (`790e95a`) PASS, all three legs supported: `anchor_restores_centroid_lifts_var` / `realvar_below_bar` / `rsd_goal_orthogonal`. Diagnostic, so it needs a confirmed `/failure-autopsy` before governance applies it. It is the only pending review. |
| C1.2-C1.5, C2 (all 8 successors), C3, C4 | **Not started.** Every member chip still open, none claimed. `chip-20260906-campaign-w3c1..w3c4` never claimed. |
| C3.4 "disposition the workset duplicates, do NOT spawn" | **Not executed, and the tick spawned them anyway:** IGW-20260906-240 (MECH-057b confirm -> substrate-blocked, nothing queued), IGW-20260906-241 (MECH-489 confirm -> THIRD do-not-queue), IGW-20260907-211 (ARC-019 retest -> DECLINED, and it found the regen had reverted the 09-04 `blocked_substrate` disposition: `52e37f8ec4`, new chip `chip-20260907-proposal-status-revert-regen`). Three sessions, every one correct, every one ~100k tokens for zero science. |
| New science landed outside the plan | MECH-535/536 registered from the ambitendency thought (`4c7a07319a`), 12-entry lit-pull (`d7b7fc7d6e`), **V3-EXQ-1007** queued (MECH-536 eval-time persistence discriminator, ree-v3 `1bbcfd8`), now running on ree-cloud-2. |
| Coordination plane | Cutover close-out done (`baf61c000`); retired-telemetry doctrine shrink landed on all three repos; `autopsy_staging_tick.py` landed, its launchd plist **still not loaded**. |

Fleet: hub + ree-worker-2 running (1007), 3/4/5 off. Untracked on the shared `ree-v3` checkout: `v3_exq_1005_*` (design-complete, claim still active), `v3_exq_981a_*`, `v3_exq_1003_*`, three `_probe_seg981a*` scratch files.

---

## 1. Where the tokens went, and what this plan changes

**The IGW tick is the largest un-owned token sink, and it spends on adjudication, not science.** `igw_routine_log.md`, 2026-09-01 to 09-07: **37 spawns**. Of the 32 completions with a recorded outcome, **19 produced no experiment, no build and no literature** -- DUPLICATE (3), NO_OP (4), or a USEFUL_LANDED whose entire content is "nothing queued / declined / marked blocked_substrate / do-not-queue" (12). At the measured ~102k-token worker floor (`dispatch_budget_gate.py`) that is roughly **1.9M tokens in six days spent establishing that work should not be done**, most of it re-establishing verdicts already on record.

Three mechanisms, all housekeeping, all now owned (HK-A below):

1. **The reaper's 48h AUTO_DEFER expires and the item re-spawns** if the workset still lists it ready (MECH-267 confirm expired 14:02Z today; EXT-009 pair expired 09-05). Worse, the `disposition` verb matched on hash alone and **refused to upgrade an AUTO_DEFER to a permanent decision** -- so wave 3's "disposition, do not spawn" instruction could not have worked even if run. **Fixed this session** (`scripts/igw_routine_tick.py` `upsert_user_disposition`, +2 tests); eight items dispositioned (section 5).
2. **The generator has no memory of prior adjudications in two lanes**: the confirmer lane ignores `diagnostic_evidence_adjudicated` and excludes `status=executed` from its only memory hook (`chip-20260906-confirmer-lane-diagnostic-adjudicated-flag` -- MECH-489 has now burned three workers), and `implementation_note` claims seed undesignable EXP/LIT proposals every cycle (`chip-20260906-impl-note-proposal-gate`, the two `impl-note-proposal-triage` chips).
3. **The regen reverts hand-set dispositions** (`chip-20260907-proposal-status-revert-regen`: carry-forward from the generated proposals file overwrites a manual `blocked_substrate` and re-arms the spawn; the twin-bleed / carry-forward / id-rot family in the 09-02 data-integrity campaign is the same class).

Second sink: **campaign briefs that nobody claims**. Wave 3 spawned four campaign chips and 16 member chips; 0 of 20 were claimed in 16 hours while the tick spent three sessions on duplicates. A plan is only cheaper than the tick if its sessions actually run. Section 5's dispatch recipe therefore names the order and the slot, and section 6.1 asks the user to release the first slot explicitly.

Third: **adjudication is the true bound, not compute.** Every queued run costs one inline autopsy in a user-present governance cycle. `autopsy_staging_tick.py` moves the DRAFTING off that path but is not loaded (HK-B item 8). Until it runs, science campaigns are paced at what one governance cycle per day can ratify (~3-4 results).

What this plan does NOT do: withdraw held chips (a hold is a reason plus a review date), touch worker power state, or queue anything.

---

## 2. Campaign HK -- housekeeping (`chip-20260907-campaign-w4-hk-housekeeping`)

One campaign chip, five bundles, five sessions (A, D Opus; B, C, E Sonnet). Each session claims the campaign chip when it starts, works ONE bundle, lands each item separately with `ree_commit.py`, resolves the member chip as it lands, and runs the umbrella corpus (`scripts/run_scripts_tests.sh --changed`, from the MAIN checkout) before landing anything under `scripts/`. Per-item STOP-CHECK before touching: `task_claim.py check --resources`, fresh `TASK_CHIPS.json` read, `git log` on the target.

### HK-A -- IGW generator idempotence: stop the re-spawn bleed (Opus, first)

Ordered by tokens saved per hour of work.

| # | Item | Member chip(s) |
|---|---|---|
| 1 | Confirmer lane: consume `diagnostic_evidence_adjudicated`; include `status=executed` in the FM10 memory hook; a claim with an adjudicated DO-NOT-QUEUE never re-enters `ready`. Contract test with the MECH-489 shape. | `chip-20260906-confirmer-lane-diagnostic-adjudicated-flag` |
| 2 | Regen must not revert a hand-set proposal status: manual `blocked_substrate` (and any terminal manual status) wins over generated carry-forward; write-back into `manual_proposals.v1.json` only when the manual file has no entry. Contract with the ARC-019 shape (EVB-1189). | `chip-20260907-proposal-status-revert-regen` |
| 3 | `implementation_note` claims: gate at the generator (`_resolve_epistemic_category` -> not `standard`), then triage the ~17 LIT + ~16 EXP rows already minted (keep the two with genuine external referents). This also retires workset IGW-*-235 (IMPL-016 lit), dispositioned DEFER today pending this item. | `chip-20260906-impl-note-proposal-gate`, `chip-20260904-litlane-impl-note-proposal-triage`, `chip-20260905-explane-impl-note-proposal-triage` |
| 4 | Retire-lane displacement: `retire_proposal_for_entry()` must filter on `proposal_type`, never flip the LIT twin when the EXP row is blocked (LIT-0629 reverted twice already). | `chip-20260902-igwtick-retire-proposal-lane-displacement` |
| 5 | The 09-02 data-integrity bundle, absorbed here (its campaign chip is withdrawn as superseded): carry-forward backlog-id spill; EXP/LIT twin status bleed; proposal-id reference rot; dry-run manifest-shape blind spot (GFLAG-0117/0120); dry-run scoring-exclusion gap; indexer run-timestamp rendering drift; indexer minting gated claims as blocked; substrate-stability flag mint scope. Check whether items 2 and 5a share one fix before writing two. | `chip-20260901-proposal-carryforward-backlogid-spill`, `chip-20260902-proposal-twin-bleed-repair`, `chip-20260902-proposal-id-reference-rot`, `chip-20260902T1250-dryfilter-manifest-shape-blindspot`, `chip-20260902-dryrun-scoring-exclusion-gap`, `chip-20260902-indexer-run-timestamp-rendering-drift`, `chip-20260904-indexer-mints-gated-claims-as-blocked`, `chip-20260904-substrate-stability-flag-mint-scope` |
| 6 | Re-mint class root cause, one paragraph in `generate_inter_governance_workset.py`'s docstring: retest/confirm items are re-minted under a new date-stamped id after a disposition on the OLD id; the stable-hash disposition covers it only if the hash is content-keyed (it is) -- document, and add a `status` line to the tick that prints the count of ready items currently suppressed by a permanent disposition, so a wave planner can see the delta. | (no chip; part of item 1) |

Verification for the whole bundle: after landing, regenerate the workset and confirm the ready list no longer contains any item whose claim has an adjudicated do-not-queue, any IMPL-* lit/exp proposal, or ARC-019.

### HK-B -- governance-pipeline exit, lint and adjudication throughput (Sonnet)

| # | Item | Member chip |
|---|---|---|
| 1 | Add the 10 (now 11) developmental claims to the needs register so `governance.sh` exits 0 without `SKIP_TRACEABILITY=1` (used two cycles running). | `chip-20260904-developmental-register-10-claims` |
| 2 | Dispose the `dv_headroom` corpus-lint commit blocker (allowlist is already inconsistent; every S1/S2 driver declares it). | `chip-20260904-dvheadroom-corpuslint-disposition` |
| 3 | Fix the `from_dims` `wanting_weight` drop site (trunk red; gates S2-A item 2). | `chip-20260904-fromdims-drop-wantingweight-997` |
| 4 | 993a precondition-index by-name lookup + warn-only lint + contract (gates S2-B item 1). | `chip-20260905-exq993a-recording-defect-precondition-index` |
| 5 | `dv_headroom_gate.reason` string generator fix + pin. | `chip-20260906-dv-headroom-reason-string` |
| 6 | Re-derive-brake counters: one per-claim semantics across the three sites + contract. | `chip-20260906-brake-counter-per-claim-lockstep` |
| 7 | ContextMemory interim-enablement warn-only lint in `validate_experiments` (the user's 09-06 rule; gates S3). | `chip-20260906-ctxmem-enablement-lint` |
| 8 | **Load `scripts/com.ree.autopsystaging.plist`** (hourly `autopsy_staging_tick.py`) -- user-present session, it is a launchd change on the Mac. Until it runs, the pacing cap in section 5 stands. | (no chip; wave-3 decision 4) |
| 9 | Governance skill `mixed` verdict for diagnostic FAILs; failure-autopsy instructs `bears_on` tagging; use-before-def lint; the two pre-existing ree-v3 trunk reds. Held in wave 3; pull forward only if a session finishes 1-8 with budget left. | `chip-20260902-governance-mixed-diagnostic-fail`, `chip-20260902-failure-autopsy-bears-on-tagging`, `chip-20260902-use-before-def-lint-b`, `chip-20260902-subcase-b-trunk-red`, `chip-20260902-preexisting-corpus-reds-repin` |

### HK-C -- shared checkout, worktrees and ledger hygiene (Sonnet)

| # | Item | Member chip / target |
|---|---|---|
| 1 | Land `v3_exq_981a_*` and `v3_exq_1003_*` UNQUEUED with a `NOT QUEUED -- BLOCKED at review, see chip` header (precedent 963b `d2104f8`); delete the three `_probe_seg981a*` scratch files. **Do not touch `v3_exq_1005_*`** -- that is S2 item 0. | wave-3 C3.2 |
| 2 | Staged `/implement-substrate` worktrees IGW-20260831-220 (`SD-PROBE-WARMUP`, substrate `implemented_validated`), -224 (`sd_blocked_agency_mismatch_floor_calibration`, validated by 642c + amended 09-05), -225 (`sd_epistemic_deficit_multitarget_readiness`, `implemented_pending_validation` -- the build is done; validation is an experiment, not this worktree), IGW-20260904-213 (`MECH465-COMMIT-GATE-HEADROOM`, route RETIRED 09-04). All four: `igw_routine_tick.py disposition <id> RESOLVE` then `gc`; never `rm -rf`. | wave-3 C3.3 |
| 3 | Close out the 1005 claim residue once S2 item 0 lands: `chip-staleclaim-igw-238-*` and `chip-igw-20260905-238` resolve done; `igw-238-confirm-evidence-mech-267-lit-0-exq-1005` closed by that session. If S2 item 0 has not run within 3 days, this bundle does NOT close the claim -- it reports. | `chip-staleclaim-igw-238-confirm-evidence-mech-20260905T130405Z`, `chip-igw-20260905-238` |
| 4 | Umbrella worktree graveyard: 68 worktrees on the Mac (`git worktree list`), the 154-worktree metaworker GC sweep chip is cloud-side. Per-worktree audit before any removal (dev-doctor buckets LIVE / DIRTY / candidate; cross-check the Claude session list). | `chip-20260826-worktree-graveyard-triage-and-gc`, `chip-metaworkergc-sweep-154-67fd3ce5efc53055`, `chip-metaworkergc-sweep-1-2687350d9ad53512` |
| 5 | REE_assembly stash `da74e32025` (hand-authored content: a plan doc + substrate changes) -- contain per `ree_v3_orphaned_autostash_triage.md`, archive-tag, then decide. The dirty `behavioral_diversity_isolation_plan.md` in the shared REE_assembly checkout may be the same content -- check before either is touched. | `chip-stash-ree-assembly-da74e32025` |
| 6 | Retroactive duplicate-chip sweep (pairs already in the backlog) -- resolve-as-you-go, `chip_ledger.py resolve --status withdrawn` naming the survivor. | `chip-20260903-retroactive-duplicate-chip-sweep` |
| 7 | cloud-4 state repair (the 09-02 fleet-hygiene campaign, superseded into this bundle): stranded worktree, staged-revert skew, GC candidate, divergent 862a/869a manifests, role-arbitration inconsistency. **cloud-4 is powered OFF** -- do these in the next power-on window only; until then the chips stay open and this row is a NOTE. | `chip-stagedskew-ree-cloud-4-ree-assembly`, `chip-20260902-cloud4-divergent-manifests-862a-869a`, `chip-rolearb-dlaptop-ree-cloud-4`, `chip-20260904-cloud4-runner-failsafe` (orchestrator's), `chip-20260902-cloud5-stash-scripts-wip-verify` |
| 8 | `chip-queuefloor-fleet-g8` (report, generation 8): resolve with the root-cause note the chip asks for -- the floor is a symptom of pacing results to adjudication capacity, and the wave plans are the backlog arm; the generator fix is to exempt a queue whose plan-of-record lists >= 3 queue-ready sessions from the starvation trip (mirror of the hold-lane predicate). | `chip-queuefloor-fleet-g8` |

### HK-D -- coordination-plane code (Opus, two sessions)

| # | Item | Member chip |
|---|---|---|
| 1 | `WORKSPACE_STATE` append from a worktree silently falls back to a local side-branch commit (coordinator scope check rejects a worktree root): make it worktree-aware or loud; pin; fix the skill guidance. | `chip-20260906-wsappend-worktree-scope` |
| 2 | **Coordinator `/intent/replace` HTTP 500** -- was 3 sightings on 09-04, held pending "a fourth on a queue write". **This session saw it on 8 of 8 ledger writes** (every `igw_routine_tick.py disposition` fell back to git). Pull forward: reproduce against the hub, fix or document the fallback as the design. | `chip-20260904-coordinator-intent-replace-http500` |
| 3 | `checkoutdiverged` full-scope fix R1+R2+R3/4/5 (user-approved 09-02). Its own session; R5 stays gated on R4's puller. | `chip-20260902-checkoutdiverged-fullfix-r1r2r345`, `chip-20260902-r4-cloud-workrepo-puller-gap`, `chip-20260902-r5-per-repo-divergence-threshold-gated` |
| 4 | CLAUDE.md registry git-fallback doctrine -> one archaeology note (A-94). **Confirm with the user first** (the chip says so; memory `feedback_no_fallback_doctrine_bloat` records the standing guidance). | `chip-20260906-registry-git-fallback-doctrine-shrink` |
| 5 | Held tooling items, pull forward only with budget: worktree_edit_guard Bash blind spot; settings.local wildcard rules; igw workset .md merge gap; dispatch background-wait ceiling (the class that killed 1005 -- the mitigation is procedural: red-team in the foreground); the three 08-28 chip-ledger/bash-gate chips; prepull grader; handover retired-timer gate; igw id collision. | `chip-20260903-worktree-guard-bash-blindspot`, `chip-20260902-settingslocal-wildcard-permission-rules`, `chip-20260901-igwworkset-md-mergegap`, `chip-20260901-dispatch-bg-wait-ceiling-kills-fanout`, `chip-20260828-*` (3), `chip-20260903-prepull-grader-changed-field`, `chip-20260903-handover-retired-timer-gate`, `chip-20260903-igw-id-collision-shared-chipref` |

### HK-E -- registry and literature bookkeeping, zero compute (Sonnet)

| # | Item | Member chip |
|---|---|---|
| 1 | Verify and bank the five cited sources (Pezzulo 2026, Jiang 2026, C3T, the authority-field bibliography) against ARC-138 / INV-104 / MECH-534 / Q-103. | `chip-20260904-litpull-grounded-compression-authority-field` |
| 2 | INV-077 re-audit, structural vs procedural, table into the claim notes; resolves GFLAG-0138's INV-077 half. | `chip-20260905-inv077-reaudit` |
| 3 | Intake-hygiene register (~36 candidates, user-gated batch via `/thought-ingestion`) -- stage the batch; the user walks it. | `chip-20260906-intake-hygiene-register` |
| 4 | Small registry fixes: ARC-027 lit schema keys; IMPL-022 non-dissipation field; EXP-0534 (EXT-009) `blocked_substrate`; stale "queued" prose for 460k/724; GFLAG-0091's 33 unmatchable build-links; plasticity-vocab stub. | `chip-20260903-arc027-lit-schema-undeclared-keys`, `chip-20260903-impl022-uncertainty-nondissipation-field`, `chip-20260902-ext009-exp0534-blocked-substrate-status`, `chip-20260902-plan-prose-460k-724-ran-not-queued`, `chip-20260901-gflag0091-unblocks-claims-edge-repair`, `chip-20260827-capability-contract-plasticity-vocab` |
| 5 | Refwedge R1 rate/cost re-measure (dated 7 days after R1; due now). | `chip-20260904-refwedge-r1-rate-cost-remeasure` |

---

## 3. Science campaigns

Each is its own chip and its own session lineage. All experiments `machine_affinity: any`, cloud-class, via `/queue-experiment` (red-team in the FOREGROUND). Every session declares `dv_headroom` where the design measures a range, and reads the adjudication pacing rule in section 5 before queueing.

### S1 -- the z_world interface front (`chip-20260907-campaign-w4-s1-zworld-front`) -- Opus

`CURRENT_FRONT.md`: 39 of 43 remaining v3 nodes chain to observation -> z_world -> E1/E2. Order matters; each item is one session.

| # | Item | Gate / note |
|---|---|---|
| 0 (inline, not chipped) | **Adjudicate V3-EXQ-1006** -- `/failure-autopsy` (diagnostic) then `/governance`. All three legs supported: the fidelity anchor restores the centroid and lifts variance; real endpoint variance sits below the bar (readout saturation); RSD dispersion is goal-orthogonal. Read together with 948 (z_world discards the resource gradient in its own input) this is direct support for the SD-018 directional-field amend and says the var-bar is partly a readout bar. Governance ratifies before item 4 is minted. | user present |
| 1 | `chip-20260905-exq1002-zworld-adequacy-portfolio` -- 250-dim `world_state` projection control + rotation corroborator on the banked 1002 dataset. Cheap (no rollouts). Decides SD-018's shape. | none; run first |
| 2 | `chip-20260905-mech465-warmup-budget-sweep` -- diagnostic sweep (GFLAG-0136); decides whether the gate-rescale route is exhausted without minting a build. | none |
| 3 | `chip-20260902-e3-channel-commensurability` -- divisive-normalisation operator before E3's additive sum (`/implement-substrate`, `integration/<slug>`, contracts on a cloud worker, delete on merge). Third `depends_on_unresolved` of `f_dominance_conversion_ceiling`. | independent of 1-2 |
| 4 (minted by governance) | **SD-018 directional-field amend** (`/implement-substrate`), then its validation contrast. **The MECH-535 experiment IS this validation**: direction-blind reactive ambitendency (the 978 two-cell approach/withdraw limit cycle) is the behavioural signature of a z_world that carries proximity but not direction; the ON/OFF contrast on 978's boards is the falsifier for both. IGW-20260907-231 (MECH-535 proposal) is dispositioned DEFER to here so the tick does not spawn a generic design. | after 1006 + item 1 are ratified |
| 5 | `chip-20260904-regulatory-anchoring-matched-aux` -- three-condition z_world experiment with the matched arbitrary-auxiliary control (INV-104 / GOV-MATCHAUX-1). | after item 1 returns (its result decides what "matched" must match) |
| 6 (inline) | **V3-EXQ-1007** (MECH-536, running on ree-cloud-2) -- adjudicate when it lands; its persist_k2/k4 result feeds item 4's design if the persistence lever alone breaks the limit cycle. | when the manifest lands |

### S2 -- ratified autopsy successors (`chip-20260907-campaign-w4-s2-ratified-successors`) -- Opus

Designs already ratified by confirmed, user-gated autopsies: the cheapest science per token in the repo. Nine items, paced.

| order | Item | Gate |
|---|---|---|
| 0 | **Resume V3-EXQ-1005** (MECH-267 mode/content location separation; IGW-20260905-238). Driver is design-complete, smoke-green, untracked on the shared `ree-v3` checkout; the ledger carries the resume command. Remaining: foreground red-team, verdict into the queue note, `ree_commit.py --repo ree-v3 --push`, `POST /queue/add`, `igw_routine_tick.py complete IGW-20260905-238 --outcome USEFUL_LANDED`, close claim `igw-238-...`, resolve the two 238 chips. Paid-for work; run first. | none |
| A1 | `chip-20260905-waypoint-consumer-reach-portfolio` -- objective/exploration vs observation-interface legs (1004 successor). Front-adjacent. | none |
| A2 | `chip-20260905-exq884a-mech428-two-kwarg-retest` -- two SD-094 env kwargs on the existing 884 driver. Cheapest item. | none |
| A3 | `chip-20260904-exq997a-mech162-three-permutation-retest` | **HK-B item 3** (from_dims drop) |
| B1 | `chip-20260905-exq993a-arc021-portfolio` (3-leg, ~80 s runs) | **HK-B item 4** (precondition index) |
| B2 | `chip-20260905-exq642d-withdraw-representable` | none |
| B3 | `chip-20260904-sd031-shortcut-vs-model-portfolio` | none |
| B4 | `chip-20260905-exq822f-init-head-control` | none; never re-run 822e's config |
| B5 | `chip-20260904-exq999a-mech161-decision-tick-readout` | none |
| B6 | `chip-20260906-exq983-lineage-latching-spike-then-avoidance` -- cheap per-seed repertoire spike first; the redesigned residue-ablation only if a repertoire exists. | none |
| tail | `chip-20260901-gflag0080-mech235-arbitration-rerun`; `chip-20260904-arc046-infant-zgoal-reachability-probe` (>= 1500 ep, the expensive one; only if the ARC-019 lineage is wanted this month). | budget |

### S3 -- ContextMemory content half (`chip-20260907-campaign-w4-s3-contextmemory-content`) -- Opus

The user's 09-06 decision: the content half is measured, not decided. Two runs, then the gate on V3-EXQ-939 / ARC-045 retest / GFLAG-0044 either opens or the redesign is refused with evidence.

| # | Item | Gate |
|---|---|---|
| 1 | `chip-20260906-ctxmem-instrument-redesign-970a` -- H1 contrastive leg on the redesigned mutual-information instrument (interim rule: refractory k=2 for any ContextMemory-reading driver; gumbel_learned only with the addressing loss). | HK-B item 7 (lint) preferred but not required -- declare the enablement by hand if the lint has not landed |
| 2 | `chip-20260906-sd070-write-stream-heldout-probe` -- held-out linear probe on the 972 write stream; answer routes to SD-070. | none |
| 3 (gated) | `chip-20260818-mech152-redesign-queue-gated` (V3-EXQ-939) -- leaves HOLD the cycle items 1-2 are adjudicated. | governance |

### S4 -- zero-compute claim closure and design gaps (`chip-20260907-campaign-w4-s4-zero-compute-closure`) -- Opus, paced one per governance cycle

| # | Item | Note |
|---|---|---|
| 1 | `chip-20260905-arc130-claim-synthesis-tagging` -- `/claim-synthesis` tagging over the confirmed 931 autopsy + three convergent instances; clears EXP-1344's blocker. | governance already decided ARC-130 closes on existing evidence |
| 2 | `chip-20260903-arc120-framing-evidence-tagging` -- framing-level cross-tagging of ARC-107 / SD-032b / MECH-261 / MECH-094 to ARC-120. | avoid the peripheral-co-tag error ARC-130's gating names |
| 3 | GOV-CONFIRM-1 confirm for **SD-056** (IGW-20260907-247, lit 0.62, dispositioned DEFER to here). The one genuinely new confirmer item. | **after HK-A item 1 lands**, so the session cannot re-derive a prior verdict |
| 4 | Design-gap lane (design sessions, NOT queue sessions): `chip-20260903-exq981a-mech027-requeue` (check the inverted hazard-band assignment first), `chip-20260903-exq991-redesign-action-level-dv`, 963b's SD-105 freeze/share API (governance mints the entry -- no chip yet). | each ends in a ratified design or a refusal, not a run |
| 5 | `chip-20260906-mech057b-hippocampal-completion-gate-substrate` -- HOLD (off-chain build; ARC-065 GAP-A co-blocks). Listed so it is not mistaken for S4 work. | hold lane |

### Not a campaign: substrate builds and proposal-exp chips stay HELD

`chip-20260901-mech035-vector-valence-substrate`, `-mech494-context-arbitrator-substrate`, `-mech039-control-channel-substrate-gap`, `-mech037-provenance-gate-substrate`, `-mech065-rc-conflict-s5-substrate`, `-mech468-anchor-relational-dump-substrate`, `-mech157-sensory-hc-gate-wiring`, `-mech320-implement-noop-margin-dv`, `-zgoal-parent-e3-consumer`, `-arc131-coalition-endogenous-recruitment-driver`, the 8 `chip-proposal-exp-*` + 2 `-paced`, the audit chips (e3eb inert marker, dea001 channel exposure, arc044 no-shared-readout), `chip-20260905-mech095-sd047-valid-retest-design`, `chip-20260814-queue-causal-sleep-matched-arm`. Reason unchanged: not on the 39-of-43 chain, each >= one Opus session floor. Review 2026-09-11.

---

## 4. HOLD lane

`hold_lane.v1.json` regenerated by this session: the wave-3 set minus ten entries whose chips resolved on 09-06/07 (doctrine shrink, heartbeat runbook, ARC-113 audit, cloud-5 puller, untracked-manifest class, depproc/explorer coupled_with, thought-sweep marker, classifierblock, daemondrift), minus `chip-20260902-campaign-fleethygiene-cloud4-staterepair` (withdrawn, superseded by HK-C.7), plus `chip-20260906-mech057b-hippocampal-completion-gate-substrate` and `chip-20260906-decision-pausepressure-hold-lane` (decision chip, section 6). Review date stays **2026-09-11**. Every campaign member above is deliberately NOT in the hold lane -- it is planned work, and the pause-pressure backlog arm should see it.

---

## 5. Ledger actions taken by this session, and the dispatch recipe

**Applied (all on origin):**

- `scripts/igw_routine_tick.py`: `upsert_user_disposition()` -- a user disposition now promotes an existing AUTO_DEFER in place instead of being refused; `cmd_disposition` uses it; 2 tests in `test_igw_routine_tick_reap.py` (96/96 pass). Umbrella commit named in `WORKSPACE_STATE.md`.
- IGW dispositions (permanent): **RESOLVE** IGW-20260907-236 (MECH-267 confirm = 1005); **DONE** -241 (MECH-489, third do-not-queue), -233/-234 (EXT-009 pair, executed 09-03), -232 (MECH-536 = V3-EXQ-1007); **DEFER** -235 (IMPL-016 lit -> HK-A.3), -231 (MECH-535 -> S1.4), -247 (SD-056 confirm -> S4.3). The ready list drops from 29 to 21; none of the 21 is an experiment-lane item the tick can spawn without a runner heartbeat except the three plan-reconcile rows it already skips.
- Chips: recorded 5 campaign chips (`chip-20260907-campaign-w4-hk-housekeeping`, `-s1-zworld-front`, `-s2-ratified-successors`, `-s3-contextmemory-content`, `-s4-zero-compute-closure`). Withdrawn as superseded, each note naming its successor: `chip-20260906-campaign-w3c1..w3c4-*`, `chip-20260902-campaign-proposalindexer-dataintegrity`, `chip-20260902-campaign-fleethygiene-cloud4-staterepair`. Member chips untouched (open, unclaimed -- never-preclaim rule).
- `hold_lane.v1.json` regenerated (section 4).

**Dispatch recipe.** Mac-coordinated named sessions from the main checkout, dispatchers off. Every session: own `TASK_CLAIMS` claim first; `chip_ledger.py claim` the campaign chip only when it starts; per-item STOP-CHECK; land per item; resolve the member chip; `/session-land`.

| Slot | Sessions | Depends on |
|---|---|---|
| Now | **HK-A** (Opus, the token lever); S1.0 inline (1006 autopsy + governance, user present); S2.0 (1005 resume); HK-B (Sonnet) | -- |
| Next | S1.1 (1002 adequacy); S2.A1, S2.A2; HK-C (Sonnet); S3.1 | -- |
| After HK-B lands | S2.A3 (997a), S2.B1 (993a); S1.2 (MECH-465 sweep); S1.3 (e3 commensurability, integration branch) | HK-B.3, HK-B.4 |
| After S1.0 + S1.1 ratified | governance mints SD-018 (S1.4); S1.5 | governance |
| Paced, one per governance cycle | S2.B2..B6; S3.2; S4.1-S4.4; HK-D x2; HK-E | pending_review depth <= 3 |

**Pacing rule (replaces wave 3's "two per day"):** queue freely up to **three un-adjudicated results** on origin; beyond that, hold the next queue session until a governance cycle clears one. Lifts to "queue freely" the day `autopsy_staging_tick` is loaded and mints its first staging chip (HK-B.8).

Expected: HK 5-6 sessions (2 Opus, 3-4 Sonnet); S1 4 Opus + 1 build; S2 3 now + 6 paced; S3 2; S4 3-4. Roughly 25 sessions over two weeks against wave 3's ~20 planned / ~20 run in two days plus 37 tick spawns -- and the tick's re-spawn class is closed at the source, which is where the saving is.

---

## 6. Decisions for the user

1. **Release the first slot explicitly.** Wave 3's briefs sat unclaimed while the tick spent three sessions on duplicates. Say which of HK-A / S2.0 / S1.0 runs first; the recommendation is HK-A then S1.0 inline in the same sitting.
2. **Load the autopsy-staging launchd agent** (HK-B.8) -- a Mac launchd change; the session will not do it without you present.
3. **HK-D.4 doctrine shrink** -- the chip asks for explicit confirmation before moving the registry git-fallback prose to an archaeology note.
4. **`chip-20260906-decision-pausepressure-hold-lane`** -- keep the hold-lane predicate in the pause-pressure gate? (Landed under the 09-06 blanket authorisation; this is the veto point.)
5. **cloud-4 power-on window** for HK-C.7 -- only if you want those five repairs done before the scaler next surges it on.
6. **The three dispositioned DEFERs** (IMPL-016 lit, MECH-535 proposal, SD-056 confirm) are re-routed, not refused; say if any should run as a plain IGW session instead.
