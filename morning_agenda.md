# Morning Agenda — 2026-08-09

Generated: 2026-08-09T12:19:03Z

> **MISSED RUNS — first digest in 11 days** (prior: 2026-07-29). The scheduler fires at 05:07 but
> the Mac was likely asleep/hibernated at that time on the intervening days, so the Check-1
> stale-skip guard correctly aborted each late fire. Fix is a repeating RTC wake before 05:07
> (`sudo pmset repeat wakeorpoweron MTWRF 05:00:00`); confirm the Mac is on AC overnight. This run
> was invoked **manually, out of slot**, at the user's request.

> **DEGRADED RUN — `governance.sh` was NOT run.** Live sessions at generation time:
> `atomic-write build_experiment_indexes`
> (`metaworker-chip-20260809-atomic-write-build-indexes`, age `1`h);
> `taskclaim close-wrote-wrong-entry rootcause`
> (`metaworker-chip-20260809-taskclaim-close-wrote-wrong-entry`, age `0.8`h);
> `de-flake amend two-closed-claims test`
> (`metaworker-chip-20260809-flaky-amend-two-closed-claims`, age `0.01`h). The Governance Agenda,
> Experiments Awaiting Review, and granularity/category audit sections below reflect the **last**
> pipeline run, not today's state. Re-run `/morning-digest` manually once sessions are clear to
> refresh them.
>
> Mitigating note: the pipeline artifacts read below are **fresh** despite the skip —
> `pending_review.md` was generated `2026-08-09T06:43Z` and
> `promotion_demotion_recommendations.md` at `2026-08-09T07:51Z`, both about 4.5h before this run.

---

## Headlines — Positive Results & Live Decisions

11 days of accumulated results. **20 runs landed `supports`, all PASS.** The two clusters that
change what to do next:

- **MECH-322 (sleep replay carve-out) — CLUSTER CLOSED, 3/3 PASS** — the standout of the window.
  - **V3-EXQ-873a** (2026-08-04, diagnostic) — `replay_carveout_fires_and_fails_closed`: the
    carve-out both fires and fails *closed*, i.e. the safety property holds under gate stress.
  - **V3-EXQ-892** (2026-08-08, diagnostic) — `replay_corroboration_survives_under_realistic_conditions`.
  - **V3-EXQ-896** (2026-08-08, evidence) — `mech322_confirmed_safety_and_functional_signature`.
  - **Moves:** MECH-322 — safety signature *and* functional signature both confirmed, on
    independent arms (deadline-stressed and strict-flag-off).
  - **Makes live:** MECH-322 is now a promotion candidate on evidence — it does **not** appear in
    today's `pending_user` queue, so the next `/governance` cycle should be asked explicitly
    whether the recommendation engine has caught up with these three runs.
  - **Gate on acting:** none identified; all three PASSed their load-bearing criteria.

- **MECH-074 family (read/write head routing) — 2 PASS, two levels of the same structure**
  - **V3-EXQ-888** (2026-08-04) — `mech074_readwrite_head_two_route_separability_supports`,
    tagged MECH-074 / 074a / 074b — the two-route separability holds.
  - **V3-EXQ-895** (2026-08-08) — `mech074c_fast_prime_dynamics_confirmed` (CeA fast-prime).
  - **Moves:** MECH-074, 074a, 074b, 074c all in the supporting direction.
  - **Gate on acting:** **MECH-074d is moving the other way** — V3-EXQ-894 (2026-08-08) and
    894a (2026-08-08) both `weakens`, and 894b (2026-08-09, trainable attribution head) also
    `weakens`. So the family is separating: the routing/dynamics sub-claims confirm while the
    *attribution-selectivity* sub-claim (074d) does not. That split is itself the finding, and
    it is a live `/claim-synthesis` shape — see the granularity note below.

Other `supports` PASSes in the window, one line each (all evidence-class unless noted):

| Date | Claim(s) | Run | Finding |
|---|---|---|---|
| 07-30 | MECH-217 | 842 (diag) | offline wanting-spread readiness verified |
| 07-31 | ARC-005 | 846 | channel-occupancy authority attributed |
| 08-01 | SD-036 | 854 | GABA-tone dose response confirmed |
| 08-01 | MECH-324, MECH-323 | 829a | reacquisition-window isolation fix confirmed |
| 08-02 | MECH-292 | 868 | goal-relevant trace outranks goal-irrelevant |
| 08-02 | INV-087 | 872 | proxy-tethering dissociation confirmed |
| 08-02 | MECH-293 | 881 | ghost cluster separates from value-flat and aims at target |
| 08-02 | ARC-014 | 880 | commitment world-state suppressed (7-criterion AND, two channels) |
| 08-03 | MECH-427 | 883 | cross-level subgoal credit |
| 08-04 | Q-004 | 149b | slow tau preferred (large-budget calibration) |
| 08-07 | MECH-286 | 891 | three-term sleep-onset conjunction confirmed (C1-C5 all true) |
| 08-08 | MECH-232 | 893 | DA representational expansion produces approach *without* valence gradient |
| 08-08 | SD-014 | 887b | node valence separable and drive-gated |
| 08-08 | SD-024 | 900 | DA cluster allocation both representational and functional |
| 08-08 | ARC-070 | 904 | decomposition-trigger selectivity confirmed (both manipulation checks) |

**Counter-context, so the headline is not read as a clean sweep.** The same 11 days produced
**~30 `weakens` and ~35 `non_contributory`** runs. Notable negatives that bear on live threads:
MECH-476 consolidation (836a/836d/836e all `weakens` after three `superseded` predecessors),
MECH-321 (844, 867a `weakens`), SD-017/MECH-166 (436b/436c/436d all `weakens`), ARC-032 theta
bypass (228b, 228c both `does_not_support`, the latter landing 2026-08-09T11:02Z — the most
recent run in the repo).

---

## Queue Status

- **Total pending: 4** (Mac: 0 | PC: 0 | EWIN: 0 | any: 3 | ree-cloud-4: 1) — plus **4 claimed**
  (running), 8 live total.
- Pending is **at the floor** — 4 against the alert threshold of 3. One more completion without a
  refill drops it under.
- Live queue: `324d` (SD-020 harm-surprise PE real flagpath, prio 35), `906b` (fishtank, prio 50,
  cloud-4), `907` / `908` (SD-016 H1 ctxdiv / H3 hard selection, prio 20). Claimed/running:
  `603s`, `876a`, `903a`, `905a`.
- **Fleet-idle watcher** (snapshot `2026-08-09T11:20:47Z`, ~1h old — fresh): `idle_risk=false`,
  claimable backlog **3** against threshold **3** — sitting exactly on the line.
  `ready_sd_validation_candidates` is **EMPTY** against 69 ready SDs, with
  `excluded_validation_already_ran=35`, `excluded_no_queueable_validation=30`. Refill therefore
  needs a **fresh `/queue-experiment` design**, not a re-queue — every built SD's validation has
  already been attempted or has no queueable validation.
- **Owed successors: none.** Every plan-named `Owner-EXQ` checked (699b, 689i, 724, 737, 738)
  failed the Step 7c gate at check (b) — all have manifests on disk. See Active Plans below.
- **Phantom Owner-EXQ ids: none found** this cycle.

---

## Experiments Awaiting Review (0 indexed / 0 runner-only)

`pending_review.md` (generated 2026-08-09T06:43Z) reports **2 pending**, both *unclaimed
manifests* rather than claim-tagged results — no PASS/FAIL awaiting governance, no ERROR
manifests, no diagnostic self-routes flagged:

- **FAIL** `v3_exq_906a_full_stack_observational_fishtank_20260809T062526Z_v3` —
  `non_contributory`, no claim tags. Its successor **V3-EXQ-906b is already queued** (prio 50,
  cloud-4).
- **FAIL** `zzz_scratch_probe_hazard002_906a_20260809T064139Z_v3` — `non_contributory`, a
  `zzz_scratch_` probe. Almost certainly a scratch artifact that should be marked discussed
  rather than reviewed as a result.

Both clear by adding the **manifest stem** to `discussed_experiment_dirs` — not the queue_id.

---

## Errors to Diagnose (0 new)

`runner_status.json` holds 87 historical ERROR entries, but the **most recent is 2026-05-31**
(V3-EXQ-621) — under Phase 3 this file lags badly and is not the live error source. Today's
`pending_review.md` reports **0 runner-only (ERROR/UNKNOWN/smoke) and 0 ERROR manifests**, so
there is nothing fresh for `/diagnose-errors`.

---

## Governance Agenda (5 recommendations)

- **SD-020** (`candidate`) — Recommendation: **promote to provisional** ← *the only promotion in
  the queue*
  - Evidence: 8 supporting, 0 opposing, 2 mixed — `conflict_ratio 0.0`, `exp_conf 0.765`,
    5 experiment entries + 5 literature entries.
  - Note: **V3-EXQ-324d is currently pending in the queue for SD-020** (harm-surprise PE real
    flagpath). Worth deciding whether to promote now or hold for 324d — the recommendation was
    generated without reference to the queued run.
- **MECH-143** (`candidate`) — **hold, resolve conflict**. 1 supporting, 2 weakening, 3 mixed;
  `conflict_ratio 0.667`, `exp_conf 0.28`, 1 exp entry / 5 lit entries. Also appears on the
  literature-pull list below.
- **SD-009** (`candidate`) — **hold, resolve conflict**. 3 supporting, 1 weakening;
  `conflict_ratio 0.5`, `exp_conf 0.323`, 1 exp entry / 3 lit entries. (V3-EXQ-897 SD-009 event-CE
  ablation ran 2026-08-08 with direction `unknown` — may resolve this once adjudicated.)
- **MECH-357** (`candidate`, `v3_pending: true`) — **hold pending V3 substrate**. 0 supporting,
  1 weakening. Blocked by explicit manual gate.
- **SD-033e** (`candidate`, `v3_pending: false`) — **hold pending V3 substrate**:
  `implementation_phase=v3` but no V3 runs yet, despite **12 supporting / 0 weakening** from
  other sources. Matches the standing memory note that SD-033e is built but co-blocked.

**Granularity-debt recurrence (GOV-GRAN-1):** `dropped_handoff` **0** (P0 clean — no chip needed).
`unflagged_recurrence` **40** (P1, list-only, no action taken); 71 excluded as metabolized, 186
claims with hits. The six carrying an actual `weakened` in their alignment distribution — i.e. the
only ones where the distribution leans toward genuine granularity debt rather than measurement
debt — are:

- **Q-034** — 6 hits / 2 signatures, alignment `other=3, weakened=3` — the strongest P1 signal
- **INV-054** — 4 hits / 2 sigs, `other=2, weakened=2`
- **MECH-111** — 5 hits / 3 sigs, `other=4, weakened=1`
- **SD-005** — 3 hits / 1 sig, `weakened=3` (single signature — likely a coherent campaign, not
  granularity debt)
- **ARC-038** — 3 hits / 1 sig, `weakened=3` (same read as SD-005)
- **ARC-018** — 2 hits / 2 sigs, `unclear=1, weakened=1`

The high-count entries are **not** granularity debt on the distribution test: MECH-058 (13 hits)
and MECH-059 (12 hits) are `unclear` across the board with **1 signature each** — one repeated
failure mode, no weakening. Same for SD-017 (10 hits, 4 sigs, no weakened) and MECH-075 (6 hits,
`intact=4, other=2`). Count alone would have flagged all four; the distribution says measurement
or implementation debt.

**Epistemic-category completeness (GOV-CAT-1): clean** — `missing_category` **0**,
`invalid_category` **0**, `malformed_markers` **0**, `claimless_missing` **0**, with **10**
legacy `unkeyed_schema` warns (singular `claim_id` targets, P1 list-only, cannot corrupt a count).
The 674 `invalid_baselined` are the excluded historical backlog, correctly suppressed by the
hit-scoped snapshot — **do not regenerate that snapshot**. The 2026-08-09 enum finding
(INV-034 / Q-021 / MECH-074d carrying `competence_implementation_gap`) is now baselined and no
new out-of-enum values have appeared since.

---

## Fleet Git Health — **ACTION REQUIRED**

`runner_git_health.py` (active ssh probe) reports **ree-cloud-2 REE_assembly: SKEW**, plus
divergent-manifest findings on two boxes. This is the most consequential item in today's digest —
none of it is visible in heartbeats or telemetry.

- **ree-cloud-2 / REE_assembly — SKEW** (4 HEAD/worktree skew paths: files in HEAD never written
  to disk), **plus 1 STRANDED untracked run manifest**:
  - `v3_exq_899_arc030_mech307_g0_readiness_20260808T153148Z_v3` **[FAIL]**, **18790s ≈ 5.2h of
    compute**, at `evidence/experiments/v3_exq_899_..._v3.json`. It has **no counterpart on origin
    at any path** — flat, pack, or de-`.bak`'d. This is real evidence loss the moment that
    checkout is reset, cleaned or gc'd.
  - Note there **is** a `v3_exq_899_arc030_mech307_g0_readiness_20260808T214833Z_v3` on origin
    (`non_contributory`, diagnostic) — a *later* run of the same EXQ. The stranded 15:31Z manifest
    is a **different, earlier** run, so the origin copy does not make it redundant.
- **ree-cloud-2 — 1 same-run_id-different-content manifest**:
  `v3_exq_850_mech204_sd076_h2_exposure_budget_probe_20260801T005937Z_v3` [FAIL] — local flat copy
  vs origin packed copy, **different content**. This is the phantom-completion / partial-write
  shape. Diff both before deleting either; do not assume origin is the good one.
- **ree-cloud-3 — 1 same-run_id-different-content manifest** (checkout otherwise OK):
  `v3_exq_864_sd076_wci_rv_trajectory_crossover_diagnostic_20260801T195304Z_v3` **[PASS]** — same
  shape, and this one is a PASS, so the stakes on picking the wrong copy are higher.
- OK: DLAPTOP-4 (both repos), ree-cloud-1 hub (both), ree-cloud-2 ree-v3, ree-cloud-3 ree-v3,
  ree-cloud-4 (both).

**Not repaired from this skill** — a skew/strand needs the preserve-before-reset procedure. Recover
the stranded manifest **first** (scp it off; the coordinator-DB signature is
`experiments.status=completed` with zero rows in `results`), then land it. Worked example:
`evidence/planning/recovered_stranded_manifests/README_ree-cloud-2_2026-07-30.md`.

---

## Active Plans Heartbeat

No plan carries a literal `status: active`; the closest are below. Note none of these files uses
the canonical 7-column `## Status table` format the digest parses, so the counts are read from
their own tables.

| Plan | Status | In-flight | Blocked | Notes |
|---|---|---|---|---|
| `conversion_ceiling_campaign_plan` | `assembling` | 6 nodes | 1 (`:GENERATION`) | converged on competence gate; `:P4` retired EXHAUSTED |
| `sd_037_axis_b_sustained_threat_curriculum_plan` | `assembling` | Phase 1b knobs | — | gate-target table, no owner-EXQ rows |
| `ree_ai_design_critique_plan` | `in_progress` | WS-1 | WS-2/10/11 NOT STARTED | 10 of 14 WS DONE |
| `e3_fresh_select_migration_plan` | `IN PROGRESS` | 1 of 3 call sites | 2 | **rows are stale — see below** |
| `psychiatric_failure_modes_plan` | `partial` | — | — | no status table |

**`e3_fresh_select_migration_plan` — stale rows, NOT owed work.** The plan states V3-EXQ-699b and
V3-EXQ-689i are *"still `pending`"* / *"blocked, still queued"*. Neither is in the live queue, and
**both have run**:

- **699b** — ran **twice**, 2026-07-24T12:35Z and 2026-07-24T20:59Z (flat + packed manifests).
- **689i** — ran 2026-07-22T16:28Z (flat + packed manifests).

So the migration plan's §5 table is ~2.5 weeks behind reality. This is a **plan-prose
reconciliation**, not a queue run — the rows should be updated with the run outcomes and the
call-site migration state re-derived from them.

**`conversion_ceiling_campaign_plan` — V3-EXQ-724 described as "running"; it ran 2026-07-09.**
Manifest present. The `:CAMPAIGN` and `:FULLSTACK` rows both name it as in-flight and are stale by
a month. `:GENERATION` is correctly **gated** (blocked-on-upstream INV-088 z_world
differentiation), not owed.

**Owed successors: none.** All five candidate ids failed Step 7c check (b).

**PLAN STALING:** `conversion_ceiling_campaign_plan` and `e3_fresh_select_migration_plan` both
have in-flight rows whose stated state is contradicted by landed evidence, and neither carries a
`## Decision log` section to date-check against.

---

## Literature Pull Candidates

All 8 literature-flagged backlog items are priority `medium`. **Seven of eight have zero existing
entries** (checked authoritatively against `claim_ids_tested` in each `record.json`, not by
directory glob):

| # | Claim | Priority | Existing entries |
|---|---|---|---|
| 1 | MECH-137 | medium | 0 |
| 2 | MECH-138 | medium | 0 |
| 3 | MECH-139 | medium | 0 |
| 4 | MECH-142 | medium | 0 |
| 5 | MECH-357 | medium | 0 |
| 6 | MECH-467 | medium | 0 |
| 7 | MECH-480 | medium | 0 |
| — | Q-019 | medium | **26** (well covered — drop from the list) |

MECH-137/138/139/142 are contiguous and likely one cluster — a single `/lit-pull` may cover all
four. **MECH-357** is the highest-value single pull: it is also a `pending_user` governance item
sitting at 0 supporting / 1 weakening, so literature is the only channel that can move it while
the V3 gate holds. **MECH-467** and **MECH-480** both had `weakens`/`does_not_support`
experimental runs in this window (874 `does_not_support` 2026-08-02; 870a `weakens` 2026-08-02),
so literature triangulation is timely for both.

---

## Stale Claims

**None** — `audit_stale_claims.py` reports zero active claims older than 6h. Clean steady state.
All three live claims at generation time were metaworker chips under 1h old.

---

## Serve.py Status

**RUNNING** on port 8000 (PID 2698).

---

## Blocked Items

1. **`governance.sh` skipped** (Tier 2 degraded) — three active metaworker-chip claims. The
   pipeline artifacts read here are ~4.5h old, so the staleness cost this cycle is low.
2. **`WORKSPACE_STATE.md` append skipped** — per Tier 2 rule, to avoid adopting live sessions'
   uncommitted edits in a whole-file read-modify-write.
3. **Duplicate claim entries flagged by `task_claim.py`** on open — two exact-duplicate pairs
   (`metaworker-chip-20260809-epistemic-category-vocab-audit` and
   `...-vocab-audit-artifact`). Not removed automatically; needs a hand check and a
   `ree_commit.py` cleanup once the pairing is confirmed.
4. **11-day digest gap** — see the banner. The scheduler fired but the Mac was asleep;
   `pmset repeat wakeorpoweron` is the fix.
