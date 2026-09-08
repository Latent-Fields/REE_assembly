# Wave 5 -- campaign programme: token-bounded housekeeping, queue-first science (2026-09-08)

**Status: PLAN OF RECORD. Ledger actions in section 6 applied by the writing session. Section 7 lists the decisions only the user can make; nothing in sections 2-5 is gated on them except where a row says so.**

- Written: 2026-09-08T07:05Z-08:30Z by session `campaign-w5-20260908` (Mac `DLAPTOP`, main checkout; `TASK_CLAIMS` claim `campaign-w5-20260908`). No experiment was queued by this session.
- User instruction: look at the IGW ledger and the durable chip ledger and devise a campaign-based programme that balances token efficiency against progression of REE, getting through a large amount of the open work; orchestrate sessions, using the metaworker skills where appropriate.
- Sources read: `igw_routine_ledger.json` (188 entries: 103 completed, 81 completed_resumable, 1 staged, 3 spawn_failed; 137 dispositions; tick PAUSED by the live governance cycle) + `igw_routine_audit.md` (09-07: 58% USEFUL_LANDED, 39% unproductive) + `igw_assignments.json` (467 rows, 0 live); `inter_governance_workset.v1.json` (05:13Z: 246 items, 29 ready of which 5 suppressed by permanent disposition, 3 by AUTO_DEFER, 20 plan-reconcile rows the tick skips); `TASK_CHIPS.json` (3175 chips: 111 open, 0 claimed; 108 work / 2 decision / 1 report); `hold_lane.v1.json` (69 held, 15 of them already resolved); `TASK_CLAIMS.json` (4 active at 07:13Z: `governance-20260908-0703`, `governance-sh-DLAPTOP-4`, `dual-insights-20260908`, `lit-pull-am-b-arc044-arc047-20260908`); `ree-v3/experiment_queue.json` (EMPTY on origin; floor detector STARVED, depth 0 < 3); `pending_review.md` (regenerated 07:1xZ by the live cycle: 6 PASS pending, all with confirmed autopsy drafts or clean evidence); `substrate_queue.json`; `CURRENT_FRONT.md` (07:12Z); FLEET_STATUS (live-status 07:05Z); `hcloud server list`; `dispatcher_control.py status` (all three dispatchers STOP since 09-03); the local phone-dispatch queue (`ree-v3/dispatch/dispatch.db`, 8 staged jobs mirroring recent chips); the scheduled tasks (`ree-morning-digest-b`, `ree-lit-pull-am-b`); commits since 2026-09-07T16:00Z on all three repos.
- Predecessor: [`science_wave_campaign_plan_20260907.md`](science_wave_campaign_plan_20260907.md) (wave 4). Its execution record is section 0 here.

---

## 0. What happened since wave 4 (facts, 2026-09-07T16:45Z -> 09-08T07:15Z)

| Wave-4 item | Outcome |
|---|---|
| HK-A (IGW generator idempotence) | **Done**, 10 items / 12 commits (`19d72a849a` ... `3ad2e12b91`). The re-spawn bleed is closed at the source; `igw_routine_tick.py status` now prints "Ready items suppressed by a permanent disposition: 5 of 29". |
| HK-B (pipeline exit / lint / throughput) | **Done, 7 of 12**: dv_headroom gate moved to COMMITTED content (`ree-v3 620b4856f7`, the cross-session commit-gate bypass is closed); developmental register; from_dims drop; 993a precondition index; reason string; brake counters; ctxmem lint. Items 8-12 (the governance `mixed` verdict, bears_on, use-before-def, subcase-b, corpus-reds repin) all resolved by other sessions the same day. `com.ree.autopsystaging` is LOADED and has minted five staging chips (1006, 970a, 972a, 1009, 1008). |
| HK-C (checkout / worktree / ledger hygiene) | **Done** except the two ree-cloud-5-only chips. queuefloor g8 ROOT-CAUSED: the queue sat below floor 3 for 88% of 17 days (median depth 2, ~4.3 ids/day consumed at the rate they are authored) -- starvation is the steady state and the floor sits above the operating depth. Routed to `/metaworker-learning` as `chip-20260907-queuefloor-detector-respec` (done). |
| HK-D, HK-E | **Not started** (D: 2 of 7 done by others; E: 0 of 10, two withdrawn). |
| S1 z_world front | Item 1 **ran**: V3-EXQ-1008 PASS diagnostic, autopsy CONFIRMED (`3f86587d6d`, red-teamed, CONTESTED->applied). Headline: at width 32 the TRAINED z_world reads 0.669 against raw field 0.979 / random projection 0.772 / untrained 0.695 (bar 0.80) -- the observation->z_world encoding DISCARDS the decision-relevant content of its own input; neither width nor geometry. H-E eliminated, H-C split, new H-F. It routes a NEW EXQ (over-capacity decoder sweep on the banked latents + fitted-linear-readout arm) and an SD-018 amend append; a lettered 1008b is REFUSED. Item 3 **built**: E3 channel-commensurability operator (`ree-v3 c47b885`, rung 3 of `f_dominance_conversion_ceiling`); its validation EXQ is owed (`chip-20260907-e3-commensurability-validation`). Items 2, 4, 5 not started. |
| S2 ratified successors | Item 0 (1005) **refused** at red-team with a 286-line record (`48e804b28b`). A1 (waypoint consumer-reach) attempted: three records, NO run -- the corrected H2 criterion fails its own headroom gate (`2a67c36dcf`, `8bd564d9ff`, `0c74ba26d2`); design fix owed. A2-B6 + tail: **not started**, held on the pacing gate. |
| S3 ContextMemory content | **Done** (970a, 972a both PASS; V3-EXQ-939 stays HOLD for governance). The cluster autopsy (`cb4a71fbd9`) found the write-content harness trains `write_addr_tagger` on DETACHED latents (LINEAGE bit-identical to UNTRAINED_ENCODER 8/8 seeds across 970/971/972/970a). |
| S4 zero-compute closure | Items 1-2 **done** (ARC-130 closed on existing evidence; ARC-120 cross-tag + GFLAG-0225). Items 3 (SD-056 confirm) and 4 (design-gap lane) not started. |
| Science outside the plan | V3-EXQ-1007 PASS (MECH-535/536 supports; C3 failed: a latch costs a good representation 88%; stochastic_sample is the only PPO-reader arm clearing the competence floor, measuring GFLAG-0131's confound at ~7x). 12 new claims registered from three thoughts (`eed648e8f8`...): ARC-139/MECH-537-540/INV-105 (mutual legibility), ARC-140/MECH-541, ARC-141/MECH-542-544 (MECH-542 proposes an INV-011 decomposition -- governance decision owed). Lit-pulls landed for INV-063 (5), INV-092 (5), INV-093, ARC-020/031 (7), ARC-034/043 (5), MECH-535 (12). |
| Coordination plane | REE_assembly shared checkout wedge (ahead 73 / behind 71 overnight) has CONVERGED (0/0 at 07:13Z; the 12 thought-intake claims are on origin). Fleet-idle watcher repaired after 9 days dead (`be4eef015`). /intent/replace activated on the hub. |
| **Live right now** | `governance-20260908-0703` (user present) is running the cycle that applies the confirmed autopsies -- it has paused the IGW tick and holds `evidence/`, `claims.yaml`, `substrate_queue.json`, the proposals and the experiment queue. |

Fleet: hub (ree-worker-1) + ree-cloud-4 + ree-cloud-5 POWERED ON per `hcloud`, all three idle; cloud-2/3 off; all dispatchers STOP; ree-explorer and ree-sync-daemon on the hub run 4-day-stale code (`chip-daemondrift-*-g2/g3`). The experiment queue is EMPTY.

---

## 1. Where the tokens go now, and the three levers this programme pulls

**The IGW tick's re-spawn class is closed (HK-A); the remaining spend is in three places.**

1. **Un-claimed campaign briefs and per-item sessions.** Wave 4 planned ~25 sessions; 13 ran in 17 hours, every one at the ~100k-token Opus floor. The per-item shape is right for science (each queue write needs a foreground red-team) and wrong for housekeeping (six prose fixes at six session floors). **Lever: housekeeping only as Sonnet bundles of <= 6 items sharing a class, run as supervised subagents of one coordinating session rather than as clickable chips** (three launched by this session at 07:16Z, section 5). The W4 recipe already said "Sonnet, bundles"; what was missing was a launcher that does not wait for a click.
2. **Adjudication, not compute, bounds the science** (W4 section 1 point 3 -- still true). But two things moved: `com.ree.autopsystaging` is loaded and minting (the W4 clause that lifts "three un-adjudicated" to "queue freely" is MET), and the live governance cycle is applying the backlog now. The bound is now user-present governance time. **Lever: pace by governance cadence, not by result count** -- queue freely to a soft cap of SIX un-adjudicated results on origin, prefer `experiment_purpose: evidence` designs (review-only) over `diagnostic` (autopsy each), and run one `/governance` cycle per ~2 days rather than after every result.
3. **Compute is idle and paid for.** The queue has been below its floor 88% of the last 17 days; cloud-4 and cloud-5 are on with nothing to run. **Lever: S2 queue-fill FIRST, in two batches of the cheapest ratified successors, so the scaler has >= 4 items to wake workers for once, not 1-2 at a time.** A run costs the fleet nothing extra; an idle powered-on worker costs money for nothing.

What this plan does NOT do: touch worker power state (section 7), unpause the IGW tick (governance Step 9 does), withdraw held chips, or queue anything itself.

---

## 2. Campaign HK -- housekeeping, Sonnet bundles (supervised subagents; no click needed)

Each bundle: one Sonnet session, <= 6 items sharing a class, own `TASK_CLAIMS` claim, per-item STOP-CHECK, `chip_ledger.py claim` on start, land each item separately with `ree_commit.py --push`, resolve the member chip as it lands, targeted tests only (the coordinator runs the full `scripts/` corpus once after the bundles land). Excluded from every bundle while `governance-20260908-0703` is live: `evidence/**`, `claims.yaml`, `substrate_queue.json`, the proposals, `experiment_queue.json`.

| Bundle | Class | Items (member chips) | Model / launch |
|---|---|---|---|
| **HK-G** commit + test gates | scripts + ree-v3 test gates | `chip-20260908-ree-commit-docstring-syntaxwarning`, `chip-20260907-ree-commit-reapply-new-path`, `chip-20260908-dev-doctor-bash32-heredoc`, `chip-20260907-precommit-remote-pytest-worktree-resolution`, `chip-20260907-cloud-scaler-veto-test-not-hermetic`, `chip-scriptscorpus-dlaptop-sweep-8-*` (diagnosis only: 8 FAIL + 14 TIMEOUT, 2h04m elapsed) | Sonnet subagent, **launched 07:16Z** |
| **HK-F** IGW / ledger writers | writer code that reverted or stalled | `chip-20260908-igw-retire-proposal-reads-stale-worktree` (Guard 2 reads the local tree; ensure_ascii diff), `chip-20260906-wsappend-worktree-scope`, `chip-20260903-igw-id-collision-shared-chipref`, `chip-20260901-igwworkset-md-mergegap`, `chip-20260907-chipledger-similar-false-negative`, `chip-20260907-servepy-autopull-abort-no-recovery` | Sonnet subagent, **launched 07:16Z** |
| **HK-I** docs / skills / config prose | stale instructions | `chip-20260907-umbrella-claude-md-stale-1800-contracts`, `chip-20260907-implsub-step6-post-wi1-substrate-split`, `chip-20260907-governance-bears-on-note-stale`, `chip-20260903-handover-retired-timer-gate`, `chip-20260902-settingslocal-wildcard-permission-rules`, `chip-20260908-exq1008-provenance-string` (text-only) | Sonnet subagent, **launched 07:16Z** |
| **HK-E** registry + literature bookkeeping | evidence/ and proposals edits -- **after governance closes** | `chip-20260908-per-type-index-stale-v2`, `chip-20260908-evidence-strip-drift`, `chip-20260907-arc027-lit-schema-fix`, `chip-20260907-impl027-citation-fix`, `chip-20260902-ext009-exp0534-blocked-substrate-status`, `chip-20260902-plan-prose-460k-724-ran-not-queued`, plus (budget permitting) `chip-20260903-impl022-uncertainty-nondissipation-field`, `chip-20260901-gflag0091-unblocks-claims-edge-repair`, `chip-20260904-refwedge-r1-rate-cost-remeasure`, `chip-20260827-capability-contract-plasticity-vocab` | Sonnet, chip `chip-20260908-w5-hk-e-registry-bookkeeping` (click, or the coordinator launches it as a subagent once `governance-20260908-0703` closes) |
| **HK-H** fleet / daemon operations | box-side operator work | `chip-daemondrift-ree-cloud-1-ree-sync-daemon-g2`, `chip-daemondrift-ree-cloud-1-ree-explorer-g3` (generation 3: route the CLASS to `/metaworker-learning`, restart the two daemons once with the OPERATOR_GUIDE pre-flight), `chip-20260907-deployed-script-drift-detector`, `chip-20260907-cloud3-missing-umbrella-checkout`, `chip-20260902-cloud5-stash-scripts-wip-verify`, `chip-metaworkergc-sweep-154-*` (cloud-5 is ON now -- do both while it is) | Opus, `/metaworker-repair`, chip `chip-20260908-w5-hk-h-fleet-ops` |
| **HK-D residue** | coordination-plane code, held | `chip-20260903-worktree-guard-bash-blindspot`, `chip-20260907-flag-registry-commit-time-gate` (decide-or-leave), `chip-20260902-r5-per-repo-divergence-threshold-gated` (gated on R4), the three 08-28 chip-ledger/bash-gate chips, `chip-20260903-prepull-grader-changed-field`, `chip-20260901-dispatch-bg-wait-ceiling-kills-fanout` | HOLD lane, review 2026-09-11 |

Verification for the whole campaign: after HK-G/F/I land, the coordinator runs `scripts/run_scripts_tests.sh` from the main checkout once and records the red count against today's 8 FAIL / 14 TIMEOUT baseline.

---

## 3. Science campaigns

All experiments `machine_affinity: any`, cloud-class, via `/queue-experiment` with the red-team in the FOREGROUND. **Pacing rule (replaces wave 4's three):** queue freely while the number of un-adjudicated results on origin (count `pending_review.md` on ORIGIN, regenerate if older than the newest manifest) is <= 6; above that, hold the next queue write until a governance cycle clears one. Prefer `experiment_purpose: evidence` where the pre-registered design permits; a diagnostic run costs an autopsy. Every session declares `dv_headroom` where a range is measured.

### S2 -- ratified autopsy successors, queue-fill (`chip-20260908-w5-s2a-queue-fill`, `chip-20260908-w5-s2b-queue-fill`) -- Opus, FIRST

The cheapest science per token in the repo: every design is pre-registered by a confirmed, user-gated autopsy. Two batches so the fleet gets >= 4 items at once.

| Batch | Item | Gate / note |
|---|---|---|
| S2a-1 | `chip-20260905-exq884a-mech428-two-kwarg-retest` -- two SD-094 env kwargs on the existing 884 driver | none; cheapest |
| S2a-2 | `chip-20260904-exq997a-mech162-three-permutation-retest` | HK-B item 3 landed (`fromdims` fix) -- verify still done |
| S2a-3 | `chip-20260905-exq993a-arc021-portfolio` (3 legs, ~80 s runs) | HK-B item 4 landed -- verify |
| S2a-4 | `chip-20260905-exq642d-withdraw-representable` | none |
| S2b-1 | `chip-20260904-sd031-shortcut-vs-model-portfolio` | none |
| S2b-2 | `chip-20260905-exq822f-init-head-control` | never re-run 822e's config |
| S2b-3 | `chip-20260904-exq999a-mech161-decision-tick-readout` | none |
| S2b-4 | `chip-20260906-exq983-lineage-latching-spike-then-avoidance` -- cheap per-seed repertoire spike first | none |
| S2 tail | `chip-20260905-waypoint-consumer-reach-portfolio` (DESIGN FIX only -- the corrected H2 fails its own headroom gate; read `2a67c36dcf`, `8bd564d9ff`, `0c74ba26d2` first), `chip-20260901-gflag0080-mech235-arbitration-rerun`, `chip-20260904-arc046-infant-zgoal-reachability-probe` (>= 1500 ep, only if ARC-019 is wanted this month) | budget |

One session per batch is the target (two queue writes per session is acceptable when both drivers already exist and each gets its own foreground red-team); split into two sessions if the first red-team runs long.

### S1 -- the z_world interface front (`chip-20260908-w5-s1-zworld-front`) -- Opus

`CURRENT_FRONT.md`: 39 of 43 remaining v3 nodes chain to observation -> z_world -> E1/E2. Order matters.

| # | Item | Gate |
|---|---|---|
| 1 | **1008's routed successor** (governance chips it after Step 2b -- if the live cycle has done so, take that chip; otherwise this row): NEW EXQ, over-capacity decoder sweep on the banked 1008 latents + the fitted-linear-readout arm the red-team added; settles whether the content is recoverable at ANY capacity. 1008b at more power is REFUSED. | governance applied the 1008 autopsy |
| 2 | `chip-20260907-e3-commensurability-validation` -- regime-level validation EXQ for the landed operator (rung 3, MECH-439). | none |
| 3 | `chip-20260905-mech465-warmup-budget-sweep` -- diagnostic (GFLAG-0136). | none |
| 4 | **SD-018 directional-field amend** (`/implement-substrate`; substrate entry minted by governance from the 1006 + 1008 autopsies), then its validation contrast -- the MECH-535 direction-blind ambitendency ON/OFF on 978's boards IS that validation; do not design a separate MECH-535 run. | substrate_queue.json carries the SD-018 amend entry |
| 5 | `chip-20260904-regulatory-anchoring-matched-aux` -- three-condition z_world experiment with the matched arbitrary-auxiliary control (INV-104 / GOV-MATCHAUX-1). 1008's result is on origin, so its gate is met; what "matched" must match is now known (content discarded at encode, not geometry). | none |

### S4 -- zero-compute closure and design gaps (`chip-20260908-w5-s4-zero-compute-closure`) -- Opus, one item per governance cycle

| # | Item | Note |
|---|---|---|
| 1 | SD-056 GOV-CONFIRM-1 confirm (workset IGW-20260908-246, lit 0.62, exp ~0; dispositioned DEFER here). The confirmer lane now remembers verdicts (HK-A.1). | after governance closes |
| 2 | `chip-20260908-inv092-falsifier-panel-refinement` -- `/claim-synthesis` over the 09-08 INV-092 lit-pull (four concrete falsifier corrections; mirror to INV-093) + `chip-20260908-inv093-suppression-sibling-readiness` (verify the 6-week-old "no refinement-strength knob" assertion against live config; queue one experiment or mark EXP-0717 blocked_substrate -- it already IS blocked_substrate on origin, so this is a verification pass). One session, both chips. | after governance closes |
| 3 | Design-gap lane: `chip-20260903-exq981a-mech027-requeue` (check the inverted hazard-band assignment first), `chip-20260903-exq991-redesign-action-level-dv`, 963b's SD-105 freeze/share API (registration only). Each ends in a ratified design or a refusal. | none |
| 4 | `chip-20260905-mech095-sd047-valid-retest-design` -- design artifact only. | budget |
| 5 | `chip-20260906-mech057b-hippocampal-completion-gate-substrate` stays HOLD (ARC-065 GAP-A co-blocks). | hold lane |

### L -- literature bundle (`chip-20260908-w5-lit-bundle`) -- Sonnet, or the scheduled morning pull

Four open lit chips: `chip-20260908-litpull-latent-interface-v2` (9 papers behind ARC-139/MECH-537-540/INV-105), `chip-20260908-litpull-compensation-culture-v2` (ARC-140/141, MECH-541-544), `chip-20260904-litpull-grounded-compression-authority-field` (Pezzulo 2026, Jiang 2026, C3T, the authority-field bibliography), `chip-20260907-orexin-zdrug-headtohead-lit` (IMPL-026, SUNRISE-1). One Sonnet session, `/lit-pull` per chip, verify-and-bank only, no confidence edits. Alternative at zero marginal session cost: the daily `ree-lit-pull-am-b` task's selector picks uncovered claims from the backlog -- these 14 claims are uncovered, so it will reach them in ~4 mornings unaided; the bundle is for doing it in one.

### Not a campaign: substrate builds and proposal-exp chips stay HELD

Unchanged from wave 4 (`mech035`, `mech494`, `mech039`, `mech037`, `mech065`, `mech468`, `mech157`, `mech320`, `zgoal-parent`, `arc131`, the 8 `chip-proposal-exp-*` + 3 `-paced`, the three audit chips, `chip-20260814-queue-causal-sleep-matched-arm`, `chip-20260818-mech152-redesign-queue-gated` (governance decides on 972a)), plus new: `chip-20260908-sleep-integrated-world-model-update-validation` (INV-063 leg B; not on the front), `chip-20260908-compute-ledger-v2` (tooling; the compute-economics thought registered no claims), `chip-20260907-mech267-persist-injection-state` (lineage is refused at red-team; fold into whichever MECH-267 successor is next designed), `chip-20260907-dv-floor-control-check-2b` (its blocker HK-B is done -- release to HK-E's budget list), `chip-20260826-*` (two Remote-Control research sessions; user-initiated only). Reason unchanged: not on the 39-of-43 chain, each >= one Opus session floor. Review 2026-09-11.

---

## 4. Decision lane and metaworker routing

- **Decision chips** (raise as real `AskUserQuestion`s in the next user-present session; both are the veto point the metaworker-learning skill requires): `chip-20260906-decision-pausepressure-hold-lane` (keep the hold-lane predicate in the pause-pressure gate? recommendation: keep) and `chip-pausepressure-dlaptop-g5` (generation 5: the gate tripped on authored open_chips 72 > 40 and proposal_tick 71%; both drivers have since been fixed at source -- HK-A gates impl-note proposals, W5a hysteresis -- recommendation: resolve with the root-cause note, do not respec again).
- **`/metaworker-learning` candidates** (genuine recurrence, one class each): daemon code drift on the hub (g3 -- a landed fix never reaches a running daemon; durable fix = drift-aware restart with the OPERATOR_GUIDE pre-flight, decision chip first); the scripts/ corpus timeouts class if HK-G confirms they are coordinator-bound tests hanging on the Mac.
- **Cloud dispatchers stay STOP.** The dispatcher pays a ~117k-token fleet-state floor per tick and would chew through the hold lane; the bundles above are cheaper and supervised. Re-grant a lease only for HK-H if the user prefers the Healer to run resident on cloud-5 (section 7).
- **IGW tick:** stays paused until governance Step 9 resumes it. Post-HK-A it is safe to leave running: 21 spawnable ready items are plan-reconcile rows it skips plus lit rows the scheduled lit-pull covers.

---

## 5. Dispatch recipe and expected shape

| Slot | Sessions | Depends on |
|---|---|---|
| Now (07:16Z) | HK-G, HK-F, HK-I as Sonnet subagents of `campaign-w5-20260908` | -- |
| When `governance-20260908-0703` closes | **S2a** (Opus, queue-fill batch 1); HK-E (Sonnet); L (Sonnet) | governance releases the queue + evidence/ |
| Next | S2b; S1 items 1-2; S4 item 1 | S2a landed (so the scaler has >= 4 items) |
| Paced, one per governance cycle | S1 items 3-5; S4 items 2-4; HK-H (Opus healer) | pending_review <= 6 |
| Next governance cycle | apply S2a/S2b results (evidence runs: review only); mint SD-018 if not yet minted; decide V3-EXQ-939 on 972a; MECH-542's INV-011 decomposition; INV-092/093 `experiment_gate` fields | user present |

Expected: HK 3 Sonnet subagents now + 2 Sonnet + 1 Opus later; S2 2 Opus; S1 4-5 Opus (one is a build); S4 3 Opus; L 1 Sonnet. About 16 sessions, 6 of them Sonnet and 3 of those already running, against wave 4's ~25 planned -- and with the queue filled to >= 8 items in the first two science sessions instead of one at a time.

---

## 6. Ledger actions taken by this session

- Resolved done (work verified already landed): `chip-20260908-ree-assembly-local-divergence-unpushed` (checkout converged 0/0; the 12 thought-intake claims are on origin), `chip-refwedge-dlaptop-ree-assembly-master-g2` (same wedge, cleared), `chip-igw-20260903-242` (IGW-242 executed 09-03, disposition DONE).
- Withdrawn as superseded, each note naming its successor: `chip-20260907-w4-hk-bundles-bcde`, `chip-20260907-w4-s1-front-items2to5`, `chip-20260907-w4-s2-successors-remaining`, `chip-20260907-w4-s4-closure-remaining`.
- Recorded 7 campaign chips: `chip-20260908-w5-s2a-queue-fill`, `-w5-s2b-queue-fill`, `-w5-s1-zworld-front`, `-w5-s4-zero-compute-closure`, `-w5-hk-e-registry-bookkeeping`, `-w5-hk-h-fleet-ops`, `-w5-lit-bundle`. Member chips untouched (open, unclaimed -- never-preclaim rule).
- `hold_lane.v1.json` regenerated from section 3's "not a campaign" list plus the HK-D residue; 15 stale (already-resolved) entries dropped; review date stays **2026-09-11**.
- Launched HK-G, HK-F, HK-I (section 2).

---

## 7. Decisions for the user

1. **Power.** ree-cloud-4 and ree-cloud-5 are ON and idle (dispatchers STOP, queue empty). Either let S2a fill the queue today so they earn their keep, or power them off until the scaler wakes them. The 09-06 decision was "4/5 off"; something powered them on again -- worth knowing what.
2. **Release S2a as soon as the governance cycle closes** -- it is the highest-value click in the programme (four ratified runs, zero design work, fills the starved queue). The coordinator can run it as an Opus subagent instead if you prefer not to click; say so.
3. **Healer on cloud-5 or on the Mac?** HK-H needs ssh to the hub for two daemon restarts. Recommendation: run `/metaworker-repair` from the Mac (chip `chip-20260908-w5-hk-h-fleet-ops`), dispatchers stay STOP.
4. **The two decision chips** in section 4 (recommendations given).
5. **MECH-542's proposed INV-011 decomposition** and the `experiment_gate` structured field for INV-092/093 -- both governance-owned; if the live cycle did not reach them, they are first on the next one.
