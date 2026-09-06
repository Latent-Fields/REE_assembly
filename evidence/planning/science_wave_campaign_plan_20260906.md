# Science wave 3 -- campaign plan of record (2026-09-06)

**Status: PLAN OF RECORD. Ledger curation in section 4 has been applied. Section 6 lists the decisions only the user can make; nothing in this plan is gated on them except where a row says so.**

- Written: 2026-09-06T16:11Z by session `science-wave-coord-20260906` (Mac `DLAPTOP`, `TASK_CLAIMS` claim of the same name). No experiment was queued by this session.
- Sources read: `docs/CURRENT_FRONT.md` (generated 2026-09-05T02:32Z), `insights_report.md` Recommendations (fixed 2026-09-02), `evidence/planning/inter_governance_workset.v1.json` (generated 2026-09-06T15:09Z: 247 items, 30 ready, 0 in flight), `igw_routine_ledger.json` + `igw_routine_log.md`, `TASK_CHIPS.json` (120 open at read time: 115 work, 4 decision, 1 report), `TASK_CLAIMS.json` (2 active), `ree-v3/experiment_queue.json` on origin (empty), the `live-status` branch, `hcloud server list` + SSH to `ree-cloud-4`/`-5`, the 2026-09-05 `governance-20260905` cycle record in `WORKSPACE_STATE.md`, the 983a/1002/1004/822e manifests, and the open governance-flag list.
- Predecessor: [`science_wave_campaign_plan_20260904.md`](science_wave_campaign_plan_20260904.md) (wave 2, C0-C5, executed 2026-09-04; section 7 there is the execution record this plan starts from). Its HOLD lane (section 3) is carried forward unchanged, review date 2026-09-11.

---

## 0. State at planning time (facts, no interpretation)

| Fact | Value |
|---|---|
| Experiment queue on `origin/main` | **empty** (0 pending, 0 claimed). Coordinator agrees. The starvation report chip `chip-queuefloor-fleet-g8` is generation 8 of its class. |
| Wave-2 output | 6 runs queued 09-04: 1002, 983a, 993a, 642c, 1004, 822e. All six have manifests. Five were autopsied inline and ratified by `governance-20260905` (993a mixed; 642c vacuous-PASS upheld; 1004 non_contributory + gate released; 1002 H-B eliminated / H-C confirmed with caveat; 822e voided, byte-identical replay of 822d). **983a (FAIL, non_contributory, manifest 2026-09-05T14:14Z) landed AFTER that cycle's `pending_review.md` regen (11:08Z) and is NOT in `review_tracker.json` -- it is the one un-adjudicated result.** |
| Governance follow-on already chipped | 09-04/09-05 governance spawned 12 successor chips (SD-e1 var-bar portfolio; 999a; 997a; SD-031 portfolio; 993a 3-leg portfolio; 642d; 884a; waypoint consumer-reach; 1002 parallel portfolio; 822f; MECH-465 warmup sweep; ARC-130 tagging; MECH-095/SD-047 design; INV-077 re-audit; developmental register; dv_headroom allowlist disposition). None started. |
| Stranded in flight | **V3-EXQ-1005** (MECH-267, IGW-20260905-238): driver `experiments/v3_exq_1005_mech267_mode_content_location_separation.py` (1118 lines) sits UNTRACKED on the shared `ree-v3` checkout, `validate_experiments --strict` clean, smoke green, design verified -- the headless session was killed at the 600 s background-wait ceiling while awaiting its red-team pass (the class `chip-20260901-dispatch-bg-wait-ceiling-kills-fanout` names). Ledger status `completed_resumable`, resume command in the ledger, `TASK_CLAIMS` claim `igw-238-confirm-evidence-mech-267-lit-0-exq-1005` still active. Two more untracked handover drivers on the same checkout: `v3_exq_981a_*` and `v3_exq_1003_*` (both BLOCKED at review 09-04, chips released this session -- section 4). |
| Fleet | `ree-worker-1` hub running (runner retired). `ree-worker-2`/`-3` off. **`ree-worker-4` and `ree-worker-5` powered on and idle** (load 0.03 / 0.58; `ree-metaworker.timer` and `ree-runner.service` inactive on both) -- unchanged since wave 2 decision 2, i.e. billable-idle since 2026-09-01T19:15Z. Resident dispatchers are OFF. |
| Live-status "V3-EXQ-906c on DLAPTOP-4.local" | stale heartbeat (668 h old); the Mac runner is deliberately off. Not a live run. |
| Workset ready items (non-plan), 10 | 3 GOV-CONFIRM-1 items (MECH-267/057b/489), EXT-009 proposal + lit, IMPL-016/019 lit, IMPL-023 proposal, ARC-019 retest, queue-depth ops. Dispositions in section 2 (C3) -- **at most 1 of the 10 is worth a session this wave**. |
| Pending user reviews | `thought_digestion_staged_2026-09-04_v3closure.md`: 47/47 claims drafted, AWAITING USER REVIEW, nothing applied; the `thought-digestion-v3-20260904` claim is idle on it. 4 decision chips (section 6). |
| Open governance flags bearing on this wave | GFLAG-0131 (978 eval-protocol confound, open by design), GFLAG-0138 (EXT-008/INV-077 wording), GFLAG-0117/0120 (dry-run filter blind spot), GFLAG-0115 (hero decision block stale). |
| Umbrella checkout | `REE_Working` master diverged (ahead 1, behind 29, 1 staged path). All ledger writes this session went through the coordinator; no umbrella git write. |

---

## 1. Where the tokens go, and the levers this wave

Measured floors (`scripts/dispatch_budget_gate.py`, 2026-08-23): a worker session pays **~102k tokens** before its first useful action, a dispatcher tick **~181k**. Wave 2 planned 12 sessions and ran roughly 20 once resumes are counted (three-experiments-per-session overflowed context twice). The levers, in order of what they save:

1. **The binding constraint is adjudication, not authoring.** Every result costs an inline autopsy (Opus draft + Fable red-team + user gate); `governance-20260905` did five and that is about one cycle's capacity. Queueing more than ~5 results per governance cycle only converts tokens into an un-reviewed backlog (983a is already one). **So C2-B is PACED: two queue sessions per day, not eight at once.**
2. **Resume, never restart.** V3-EXQ-1005 is a ~15-minute resume (red-team, note, commit, queue). Rewriting it would be a full Opus session. Same for the two staged-worktree `/implement-substrate` items in C3.
3. **Refuse duplicates at the workset.** 4 of the 10 ready workset items duplicate work in flight or already dispositioned this week (section 2, C3). Each would be a full headless session ending in `DUPLICATE`.
4. **One experiment per session; Sonnet for registry work.** Model routing per `dispatch_remote_launch.WORK_TYPE_MODEL_DEFAULTS` (Opus: queue-experiment, implement-substrate, claim-synthesis, redesign; Sonnet: record-drift, single-call-site-fix, stale-flag, gc-sweep). C4 bundles seven Sonnet-class items into one session.
5. **Dispatchers stay off.** Same reasoning as wave 2 lever 2: they are category-blind within a lane and would resume against ~90 held chips. Named Mac-coordinated sessions, campaign chips with STOP-CHECKs.
6. **Front first.** Ordering is distance from the one live front (observation -> z_world -> E1/E2 interface; 39 of 43 remaining v3 nodes chain to it). Off-front successors run only in the paced lane.

Expected shape: **10 core sessions** (C1 x4, C2-A x3, C3 x2, C4 x1) plus the user-present C0, then up to 8 paced sessions (C2-B x5, claim-synthesis x2, C1 gated item x1) as governance capacity allows.

---

## 2. Campaigns

### W3-C0 -- Adjudicate what is already in (governance + autopsy; inline, NOT chipped)

`/governance` and `/failure-autopsy` re-derive their own worklists (CLAUDE.md "Report inline, do not chip"). One session, user present.

1. **V3-EXQ-983a** (EXT-002 + ARC-013, FAIL/non_contributory, 2026-09-05T14:14Z): regenerate `pending_review.md`, autopsy, ratify the claim-tag divergence wave 2 left owed (EXT-002+ARC-013, not ARC-005/INV-008 -- GFLAG-0124 is the open flag on exactly this).
2. **The ContextMemory content-half human call** (GFLAG-0132 field corrected, "corrupting defect stays OPEN on the content half"): whether occupancy-without-addressing closes the 1-slot-bank defect. It is the only thing gating V3-EXQ-939 (`chip-20260818-mech152-redesign-queue-gated`), the ARC-045 retest and GFLAG-0044. `puzzle (known rules)`: a decision, not a run. Gated on this since 2026-08-21.
3. **Apply the 47-claim thought-digestion staged review** (`thought_digestion_staged_2026-09-04_v3closure.md`, dispositions a=22 b=2 c=13 c2=2 f=5 g=3). Whole-batch user review, then the orchestrator applies and closes `thought-digestion-v3-20260904`. This is the largest pending human item and costs no compute.
4. Run `chip-20260904-developmental-register-10-claims` FIRST if it has not landed (C4 item 1): without it `governance.sh` exits non-zero on the traceability check and needs `SKIP_TRACEABILITY=1`.
5. Decision chips, section 6.

### W3-C1 -- The live front: z_world interface (`chip-20260906-campaign-w3c1-zworld-front`)

`CURRENT_FRONT.md`'s two named critical-path items plus the 1002 follow-through. All Opus. Order matters.

| # | Item | Skill | Note |
|---|---|---|---|
| 1 | `chip-20260904-sde1-var-bar-portfolio` -- SD-e1 OFF / RSD / RSD+anchor var-bar portfolio (`sd_e1_var_bar_readout_crush`) | `/queue-experiment` | **Critical-path item 1.** V3-EXQ-1000 cleared `cr_ratio` 6/6 but `e1coe_score_var` stays 36x-1700x short; the 3-leg fan-out is ratified and registered. One new experiment, three arms. Declares `dv_headroom`. |
| 2 | `chip-20260905-exq1002-zworld-adequacy-portfolio` -- 250-dim `world_state` projection control + rotation corroborator on the **banked 1002 dataset** | `/queue-experiment` | Cheap compute (no new rollouts). Decides whether the H-C geometry deficit is a 250->32 channel-input property. **Gates SD-018's shape choice** (governance-20260905: "SD-018 shape (b) stays held"), so this runs BEFORE any SD-018 build is minted. |
| 3 | `chip-20260905-mech465-warmup-budget-sweep` -- warmup-budget sweep probe | `/queue-experiment` (diagnostic) | GFLAG-0136 resolution. The 09-04 spike ran 6 min on the Mac; a sweep is the same order. Decides whether the gate-rescale route is exhausted instead of minting the build. Same latent as items 1-2. |
| 4 | `chip-20260902-e3-channel-commensurability` -- divisive-normalisation operator before E3's additive sum | `/implement-substrate` | The third `depends_on_unresolved` on `f_dominance_conversion_ceiling`; user-decided V3 (2026-09-04), never started. Touches `ree_core/predictors/e3_selector.py`: land on `integration/<slug>`, contracts on a cloud worker, delete on merge. Independent of items 1-3. |
| 5 (gated) | `chip-20260904-regulatory-anchoring-matched-aux` -- three-condition z_world experiment with matched arbitrary-auxiliary control (INV-104 / GOV-MATCHAUX-1) | `/queue-experiment` | Its own gate was "1002 must land": 1002 eliminated the consumer hypothesis, so the gate is open -- but its design should read item 2's result (the 250-dim control decides what "matched auxiliary" must match). Run after item 2 returns. |
| -- (not chipped) | **SD-018 directional-field amend** | `/implement-substrate` | Still the un-owned buildable-now item in `CURRENT_FRONT.md`. Deliberately NOT chipped here: the shape decision is held by governance pending item 2, and chipping ahead of that ratification is the autopsy-follow-on race. **C0 mints it** the cycle item 2 is adjudicated. |

Sessions: A = item 1; B = item 2; C = item 3; D = item 4 (integration branch); E = item 5 after B's result.

### W3-C2 -- Ratified successors (`chip-20260906-campaign-w3c2-ratified-successors`)

Every item here is a pre-registered successor from a confirmed, user-gated autopsy; the design decisions are already made, so these are the cheapest science per token. Split by front distance.

**C2-A, front-adjacent -- run now (3 sessions, Opus, `/queue-experiment`):**

| # | Item | Why front-adjacent |
|---|---|---|
| 1 | `chip-20260905-waypoint-consumer-reach-portfolio` -- objective/exploration vs observation-interface legs | 1004 validated the field for a supervised reader, not the RL consumer: the observation-interface leg IS the front's question in a second environment. |
| 2 | `chip-20260904-exq997a-mech162-three-permutation-retest` -- explicit three-permutation z_resource / z_world planning reconvergence | z_world content. **Depends on C4 item 3** (`chip-20260904-fromdims-drop-wantingweight-997`: an unregistered `from_dims` drop site means an ablated arm may equal its control -- fix and verify before re-lettering). |
| 3 | `chip-20260905-exq884a-mech428-two-kwarg-retest` -- set the two SD-094 env kwargs on the EXISTING 884 driver | Cheapest item in the wave (two-kwarg edit + episode-length/done-cause recording). MECH-428 navigation DV, waypoint-dependent. |

**C2-B, off-front, PACED at two sessions per day behind governance capacity (5 sessions, Opus):**

| order | Item | Note |
|---|---|---|
| 1 | `chip-20260905-exq993a-arc021-portfolio` (3-leg) | Runs are ~80 s on cloud; cheap compute. Uses the repaired spark driver. **Apply C4 item 4's precondition-index fix first** (the manifest's recorded harm-head sensitivity is currently the coverage count). |
| 2 | `chip-20260905-exq642d-withdraw-representable` | Whole 642 family could never express withdraw; hazards arm + per-tick series + self-attributable-cancellation arm. |
| 3 | `chip-20260904-sd031-shortcut-vs-model-portfolio` | EXT-005 / SD-031 gate amended by governance; scratch-init same-budget control is the discriminator. |
| 4 | `chip-20260905-exq822f-init-head-control` | Design-changed successor (trained-vs-init discrimination index, new seeds). Byte-identical replay was refused; do not re-run 822e's config. |
| 5 | `chip-20260904-exq999a-mech161-decision-tick-readout` | Readout scored only at decision ticks, oracle/null-derived bars. |
| tail | `chip-20260901-gflag0080-mech235-arbitration-rerun`; `chip-20260904-arc046-infant-zgoal-reachability-probe` (>=1500 ep -- the expensive one; it is what unblocks ARC-019, so it earns its place only if the ARC-019 lineage is wanted this month) | Both from the wave-2 HOLD "science candidates" list. |

**Design-gap lane (NOT queue sessions -- each needs a substrate or design decision first; chips released, unclaimed, open):** `chip-20260903-exq981a-mech027-requeue` (replay anchor pool emptied per episode; MECH-272 routing consumer never enabled -- a MECH-027 design gap), `chip-20260903-exq991-redesign-action-level-dv` (1003: Context-B policy direction-locked, needs a readout with free-policy range), 963b (needs an SD-105 freeze/share API -- a build, no chip yet: **C0 should mint it or fold it into the SD-104/105 entry**), `chip-20260905-mech095-sd047-valid-retest-design` (design artifact, may not be queueable).

### W3-C3 -- Stranded and duplicate work: recover what is paid for, refuse what is not (`chip-20260906-campaign-w3c3-stranded-recovery`)

| # | Item | Skill / model | Action |
|---|---|---|---|
| 1 | **Resume V3-EXQ-1005** (IGW-20260905-238, MECH-267) | `claude --resume` per the ledger's `resume_command`, Opus | Remaining steps only: red-team pass (`/queue-experiment` Step 4.5), verdict into the queue entry `note`, commit driver + queue entry with `ree_commit.py --repo ree-v3 --push`, coordinator `POST /queue/add`, `igw_routine_tick.py complete --outcome USEFUL_LANDED`, close claim `igw-238-confirm-evidence-mech-267-lit-0-exq-1005`, resolve `chip-staleclaim-igw-238-...` done. Run the red-team **in the foreground** -- the 600 s background ceiling is what killed it. |
| 2 | Untracked handover drivers `v3_exq_981a_*`, `v3_exq_1003_*` (+ three `_probe_seg981a*` scratch files) on the shared `ree-v3` checkout | Sonnet | Land the two drivers UNQUEUED with a `NOT QUEUED -- BLOCKED at review, see chip` header (precedent: 963b `d2104f8`), delete the probe scratch files, so the shared checkout stops carrying other sessions' untracked work. Do not queue either. |
| 3 | Staged `/implement-substrate` worktrees from 2026-08-31: IGW-220 (`SD-PROBE-WARMUP`), IGW-224 (`sd_blocked_agency_mismatch_floor_calibration`), IGW-225 (`sd_epistemic_deficit_multitarget_readiness`); IGW-213 already retired | Sonnet | 224's entry was validated by 642c and amended by governance-20260905 -> `disposition RESOLVE`, GC the worktree. 220 and 225: check `substrate_queue.json` status; if still `ready`, they are wave-3 build candidates for the HOLD review on 09-11, else RESOLVE. Use `igw_routine_tick.py disposition` / `gc`, never `rm -rf`. |
| 4 | Workset duplicates -- disposition, do NOT spawn | Sonnet, `igw_routine_tick.py disposition` | IGW-20260906-236 (MECH-267 confirm) = duplicate of 1005 in flight. IGW-20260906-241 (MECH-489 confirm) = duplicate of IGW-152 `in_progress` (V3-EXQ-910b MIXED; the open question is a governance read of the C1 tap discrepancy, not a new run). IGW-20260906-214 (ARC-019 retest) = re-mint of IGW-20260904-214, dispositioned `blocked_substrate` on 09-04 (EVB-1189). IGW-20260906-232 (EXT-009 lit) = IGW-20260903-243 already completed. **Root cause to note for the generator:** retest/confirm items re-mint after disposition -- one line in the disposition note each; a generator fix is a C4-class chip only if a third instance appears. |
| 5 | IGW-20260906-240 (MECH-057b confirm-evidence) | -- | The one genuinely new ready item. MECH-057b is `candidate` with EMPTY notes: a GOV-CONFIRM-1 run against a claim with no recorded mechanism text would spend an Opus session establishing what the claim even asserts. HOLD until the thought-digestion apply (C0.3) or a lit-pull gives it content. |

### W3-C4 -- Registry, lint and literature bundle (`chip-20260906-campaign-w3c4-registry-lit-bundle`)

One Sonnet session, resolve-as-you-go, each item landed separately with `ree_commit.py`. Ordered by what unblocks other campaigns.

1. `chip-20260904-developmental-register-10-claims` -- governance exits non-zero without it (unblocks C0).
2. `chip-20260904-dvheadroom-corpuslint-disposition` -- the allowlist is already inconsistent (helper-call form bypasses the literal grep); every C2 session declares `dv_headroom`.
3. `chip-20260904-fromdims-drop-wantingweight-997` -- trunk red + evidence-validity for MECH-162 (unblocks C2-A item 2).
4. `chip-20260905-exq993a-recording-defect-precondition-index` -- fix by-name lookup, warn-only lint, contract (unblocks C2-B item 1).
5. `chip-20260904-litlane-impl-note-proposal-triage` + `chip-20260905-explane-impl-note-proposal-triage` -- same root cause (IMPL-* proposals whose truthmaker is the repo); this also disposes workset items IGW-20260906-233/234/235 (IMPL-016/019 lit, IMPL-023 proposal) without spawning them. Two have genuine external referents -- keep those.
6. `chip-20260904-litpull-grounded-compression-authority-field` -- verify and bank the five cited sources (Pezzulo 2026, Jiang 2026, C3T, the authority-field bibliography) against ARC-138 / INV-104 / MECH-534 / Q-103. Can ride `ree-lit-pull-am` instead.
7. `chip-20260905-inv077-reaudit` -- structural vs procedural write-path audit; resolves GFLAG-0138's INV-077 half. Read-only audit, table into the claim notes.

**Two Opus `/claim-synthesis` sessions, paced with C2-B (they close claims with zero compute but are not cheap in tokens):** `chip-20260905-arc130-claim-synthesis-tagging` (governance decided ARC-130 closes on existing evidence; clears EXP-1344's blocker) and `chip-20260903-arc120-framing-evidence-tagging` (wave-2 C4.5, still open).

---

## 3. HOLD lane

**Wave 2's HOLD lane (`science_wave_campaign_plan_20260904.md` section 3) is carried forward verbatim, review date 2026-09-11 or the next wave-planning session.** Changes only:

- **Left HOLD -> this wave:** `chip-20260902-e3-channel-commensurability` (C1.4, already released 09-04); `chip-20260901-gflag0080-mech235-arbitration-rerun` and `chip-20260904-arc046-infant-zgoal-reachability-probe` (C2-B tail); `chip-20260903-arc120-framing-evidence-tagging` (C4 paced).
- **Added to HOLD (science):** IGW-20260906-240 MECH-057b confirm (C3.5 reason); `chip-20260904-exq999a-...` and `chip-20260904-sd031-...` are NOT held -- they are C2-B items 5 and 3, paced.
- **Added to HOLD (design/decision-gated):** `chip-20260905-mech095-sd047-valid-retest-design` (design artifact; run when a `/queue-experiment` session is idle), `chip-20260904-substrate-stability-flag-mint-scope`, `chip-20260904-indexer-mints-gated-claims-as-blocked`, `chip-20260904-explorer-coupled-with`, `chip-20260904-depproc-coupled-with-labels`, `chip-20260904-thought-sweep-intake-marker`, `chip-20260904-coordinator-intent-replace-http500` (3 sightings, falls back to git -- pull forward only if a fourth sighting lands on a queue write), `chip-20260904-cloud4-runner-failsafe` (x5 -- the runner is INACTIVE on cloud-4 by the orchestrator's choice; belongs to `/metaworker-orchestrate`), `chip-20260903-e3eb-inert-marker-audit`, `chip-20260903-dea001-v3-channel-exposure-audit`, `chip-20260902-arc113-stage-implementation-audit`, `chip-20260902-arc044-mech152-arc016-no-shared-readout`, the 8 coherent `chip-proposal-exp-*` + 2 `-paced` chips.
- **Unchanged:** the 12 off-chain substrate builds (11 now that e3-commensurability left), coordination-plane/fleet bundle, design/thought chips, the wave-2 registry-hygiene list, `chip-20260814-queue-causal-sleep-matched-arm` (still gated on the 920 retrospective), `chip-20260818-mech152-redesign-queue-gated` (moves to C2 the cycle C0.2 is decided).

A held chip keeps `open`; nothing here is withdrawn. Reason for every hold: it is not on the 39-of-43 chain and costs at least one Opus session floor.

---

## 4. Ledger actions taken by this session (all coordinator-acknowledged, no git write)

- **Resolved done:** `chip-20260904-reev3-queue-file-skew-shared-checkout` (verified: `experiment_queue.json` clean in the shared `ree-v3` checkout, no diff vs `origin/main` -- the skew self-cleared); `chip-20260904-campaign-c2-dv-headroom` (wave-2 C2 executed per its section 7).
- **Unclaimed** (claimant campaign sessions closed 09-04, items BLOCKED with handovers): `chip-20260903-exq981a-mech027-requeue`, `chip-20260903-exq991-redesign-action-level-dv`. Now in the design-gap lane (C2), not queue candidates.
- **Recorded** four campaign chips `chip-20260906-campaign-w3c1..w3c4-*`. Member chips stay open; each campaign brief tells its session to resolve members as they land. No chip was claimed (never-preclaim rule).
- **Not touched:** the active claim `igw-238-confirm-evidence-mech-267-lit-0-exq-1005` (its session is dead but the work is resumable and paid for -- C3.1 closes it); the `thought-digestion-v3-20260904` claim (idle, awaiting the user); the 4 decision chips; worker power state.

---

## 5. Dispatch recipe

Named Mac-coordinated sessions (interactive or `claude -p` background agents from this checkout), one experiment per session, dispatchers off. Every session: open its own `TASK_CLAIMS` claim first; `chip_ledger.py claim` the campaign chip only when it actually starts; per-item STOP-CHECK (`task_claim.py check --resources`, fresh ledger read, `git log` on the target, `experiment_queue.json` on origin for the queue_id) before each item; land each item with `ree_commit.py`; resolve the member chip; close with `/session-land`.

| Slot | Sessions | Depends on |
|---|---|---|
| Now | C0 (user present); C3.1 (1005 resume, foreground red-team); C4 bundle (Sonnet); C1-A (SD-e1 portfolio); C1-B (1002 parallel portfolio); C1-D (e3-commensurability, integration branch) | -- |
| After C4 items 3-4 land | C2-A x3 (waypoint reach; 997a; 884a); C1-C (MECH-465 sweep) | C4.3 for 997a |
| After C1-B returns | C1-E (regulatory-anchoring matched-aux); C0 mints SD-018 | C1.2 result |
| Paced, <= 2/day, each after the previous governance cycle has capacity | C2-B in order 1..5; claim-synthesis x2; C3.2-C3.5 (Sonnet, any idle slot) | pending_review depth <= 3 |

Compute: every queued run here is cloud-class (`machine_affinity: any`); the scaler powers workers 2/3 on for claimable work. Workers 4/5 are the orchestrator's (section 6.1).

Expected queue output: SD-e1 portfolio, 1002 parallel portfolio, MECH-465 sweep, 1005, waypoint reach portfolio, 997a, 884a (core: 7 runs, ~4 of them cheap re-analyses or probes), then 993a portfolio / 642d / SD-031 / 822f / 999a paced. Adjudication load: 7 core results across two governance cycles.

---

## 6. Decisions for the user

1. **`ree-worker-4` and `ree-worker-5` are still powered on and idle** (since 2026-09-01T19:15Z: dispatchers off, runner inactive on both, orchestrator veto keyed on a stale `chips_open_work > 0` heartbeat). Five days billable for nothing this wave uses. Owned by `/metaworker-orchestrate`; this plan neither needs them nor touches them. Power off, or leave for a future dispatcher restart -- a cost decision only.
2. **ContextMemory content-half call (C0.2).** Sole gate on V3-EXQ-939, the ARC-045 retest and GFLAG-0044 since 2026-08-21. Evidence on both sides is recorded in the entry.
3. **Apply the 47-claim thought-digestion review (C0.3).** Zero compute; the biggest un-applied batch in the repo.
4. **Pacing cap.** This plan holds C2-B to two queue sessions per day so results never outrun adjudication. If you would rather fill the queue to the floor of 3 immediately, C2-B items 1-3 are the ones to release (cheapest compute, designs already ratified) -- but 983a is already an un-reviewed result, and each extra result is one more inline autopsy.
5. **The four standing decision chips**, unchanged from wave 2: `chip-pausepressure-dlaptop-g5` (this plan is again the backlog-arm answer), `chip-20260901-heartbeat-retirement-runbook` (R1-R7 need live SSH/sudo), `chip-20260903-untracked-manifest-collision-recurring-class`, `chip-20260903-cloud5-no-puller-for-work-repos` (sudo systemd change).

---

## 7. Decisions record (2026-09-06, user, evening)

1. **Workers 4/5: powered off** (`hcloud server shutdown`, verified `off`); cloud-4 may come back via the scaler's surge rule when the queue grows.
2. **ContextMemory:** the human call was already made by governance-20260905 (occupancy does not close the defect). The delegated remainder is recorded on the substrate entry as `decision_2026_09_06` (REE_assembly `7a21722fee`): interim enablement rule (refractory k=2 for any ContextMemory-reading driver; gumbel_learned only with the addressing loss; library default unchanged) + a decision-log line; the content half gets evidence work, not a call: `chip-20260906-ctxmem-instrument-redesign-970a`, `chip-20260906-sd070-write-stream-heldout-probe`, `chip-20260906-ctxmem-enablement-lint`.
3. **Thought-digestion apply: yes** -- being executed group by group by the concurrent user-present session (recommendation log 17:37Z, G2); this coordinator did not touch `claims.yaml`.
4. **Adjudication throughput:** `scripts/autopsy_staging_tick.py` (+ tests, + `scripts/com.ree.autopsystaging.plist`, hourly, not yet loaded) detects every un-autopsied FAIL / diagnostic / adjudication-flagged result on ORIGIN (never the regen, so the 983a "untracked" class cannot recur) and mints one staging-mode `/failure-autopsy` chip per result, content-deduplicated against the artifact corpus. The pacing cap in section 6.4 is therefore replaced by: queue freely; the DRAFTING moves off the governance critical path; the human GATE (Step 1.5) is the remaining bound and is now a batch of drafts per cycle rather than a batch of runs.
5. **Standing decision chips, all actioned:** heartbeat runbook R5 done on the Mac (cloud configs in the same power-on window as the deploys), **R7 blocked** -- the `git rm -r` of the 32 frozen `runner_heartbeats/ runner_status/ runner_commands/` files was refused by the session's auto-mode classifier as destructive; every consumer was verified absent-dir-safe and the hub is clean under those dirs, so the user can run it directly:
   `cd /Users/dgolden/REE_Working/REE_assembly && git rm -r -q evidence/experiments/runner_heartbeats evidence/experiments/runner_status evidence/experiments/runner_commands && git commit -m "R7: retire the frozen telemetry dirs (heartbeat retirement runbook)" && git push origin HEAD:master`. Untracked-manifest collision: option B built, tested (12/12) and landed (ree-v3, `coordinator/deploy/ree-git-sync-repair.sh`), deployed to the workers in the power-on window. cloud-5 puller: `ree-git-sync-repair.timer` installed on cloud-5 in the same window. Pause-pressure g5: `/metaworker-learning` root-cause pass -- the hold lane the gate could not see; `hold_lane.v1.json` + predicate landed (record appended to `pause_pressure_recurrence_rootcause_staged_20260902.md`).
