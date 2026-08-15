# Morning Agenda — 2026-08-15

Generated: 2026-08-15T04:45:11Z

> **MISSED RUNS — first digest in 5 days** (prior: 2026-08-09). The scheduler fires at 05:07 but
> the Mac was likely asleep/hibernated at that time on the intervening days. Fix is a repeating
> RTC wake before 05:07 (`sudo pmset repeat wakeorpoweron MTWRF 05:00:00`); confirm the Mac is on
> AC overnight.

> **DEGRADED RUN — `governance.sh` was NOT run.** Live sessions at generation time:
> `update-docs nightly` (`nightly-docs-20260815T0436Z`, age <0.1h). The Governance Agenda,
> Experiments Awaiting Review, and granularity/category audit sections below reflect the **last**
> pipeline run (2026-08-13), not today's state. Re-run `/morning-digest` manually once sessions
> are clear to refresh them.

> **READ NOTE — this agenda was built from `origin/*`, not the local working tree.** The Mac's
> `REE_assembly` checkout is **272 commits behind** origin and cannot fast-forward (see Blocked
> Items). All queue / evidence / claims / plan reads below were taken from `origin/master` and
> `origin/main` blobs so the content is current; the working tree was deliberately left untouched.

---

## Headlines — Positive Results & Live Decisions

Six days of results landed since 2026-08-09 (~36 runs). The decision-moving ones:

- **V3-EXQ-930 — MECH-303 dedicated proximity-signal validation — PASS** (`supports`, diagnostic)
  - **Moves:** MECH-303 (`provisional`) — verdict `mech303_dedicated_signal_discriminates_zharm_a_does_not`.
    The dedicated proximity-anticipatory signal discriminates across density; the shared
    `z_harm_a` damage-sourced signal does not.
  - **Makes live / unblocks:** ratifies the 2026-08-12 user-adjudicated routing (option a: build a
    dedicated signal, not retune the shared one) and makes `mech303_safety_threshold:BUILD` —
    the plan's only node, `open`/high — a validated build rather than a bet. Substrate queue entry
    `SD-MECH303-THRESHOLD-SOURCING` is `ready`.
  - **Gate on acting:** none — this is the go-signal. Two chips already cover the build
    (`chip-20260812-mech303-threshold-sourcing`, `chip-igw-20260812-216`); do not spawn a third.

- **V3-EXQ-926a — MECH-449 / ARC-107 perseveration no-go falsifier — PASS** (`supports`, evidence)
  - **Moves:** MECH-449 (`provisional`), ARC-107 (`candidate`) — verdict `perseveration_axis_converts`.
  - **Makes live / unblocks:** a conversion-ceiling axis that **does** convert — directly relevant
    to the conversion-ceiling root set. Also closes the V3-EXQ-926 ERROR (hardcoded Mac-only
    `EVIDENCE_DIR` crash on ree-cloud-2); 926a is the superseding fix and it ran clean 2026-08-14.
  - **Gate on acting:** none.

- **V3-EXQ-934 — MECH-266 / SD-032a cap sweep, mode occupancy — PASS** (`non_contributory`, diagnostic)
  - **Moves:** nothing scored, but the verdict is `cap_recalibration_admits_mixed_regime` —
    GOV-FANOUT-1 leg H1 resolves as **cap mis-calibration, not structural bang-bang**.
  - **Makes live / unblocks:** a graded regime is reachable on the symmetric arm; winning cap band
    `[0.75, 1.75]`. This turns a suspected structural ceiling into a tuning problem.
  - **Gate on acting:** none — but it is the newest run in the corpus (2026-08-15T01:52Z) and is
    not yet in `pending_review.md`.

- **V3-EXQ-922a — MECH-152 soft-selection ablation — PASS** (`mixed`, diagnostic)
  - **Moves:** MECH-152 (`provisional`) — verdict `selection_hardness_partial_recovery`.
  - **Makes live / unblocks:** MECH-152 is sitting in the governance queue on a
    **`demote_to_candidate` / `pending_user`** recommendation. A partial-recovery PASS is
    directly relevant to that adjudication and postdates the recommendation.
  - **Gate on acting:** partial recovery only — read alongside V3-EXQ-922 (FAIL, `weakens`
    MECH-150/151/152/ARC-041) before deciding the demotion.

- **V3-EXQ-927 + V3-EXQ-928 — MECH-267 CEM selection-fix validation — PASS x2**
  (`non_contributory`, diagnostic) — verdict `fix_effective::H3+BOTH` on both. Runtime engagement
  diagnostics confirm the two new facets actually fired. The fix works; MECH-267 (`provisional`)
  keeps its status and the fix is cleared for use.

- **V3-EXQ-907 + V3-EXQ-908 — SD-016 saddle-break recipe — PASS x2** (`diagnostic`)
  - `sd016_h1_ctxdiv_breaks_saddle` and `sd016_h3_hard_selection_breaks_saddle:A2_tagger_gumbel`.
  - Both clear the `world_encoder_weights_moved` precondition (measured 5.0 vs threshold 1.0) —
    i.e. they explicitly do **not** reproduce the V3-EXQ-737a/728 wiring-failure signature the
    recipe exists to fix. The encoder-wiring failure mode is closed.

- **V3-EXQ-876a — MECH-025 doing-mode convergence redesign — PASS** (`supports`, evidence) —
  `doing_mode_produces_convergent_causal_signature`. MECH-025 is `provisional`.

- **V3-EXQ-918a — SD residue valence-bound validation — PASS** (`supports`, diagnostic) —
  `sd_residue_valence_bound_validated`, all preconditions met at 1.0.

- **V3-EXQ-924 / V3-EXQ-925 — E3 scorer-fix remeasure + F-dominance frozen-replay causal harness
  — PASS x2** (`diagnostic`) — instrumentation validations; the F-dominance causal harness is now
  a working apparatus.

Counter-weight, so the headlines are not read alone: the same window also produced
**V3-EXQ-894b/894c** (`weakens` MECH-074d), **V3-EXQ-905a** (`weakens` MECH-075),
**V3-EXQ-910/910a** (`weakens` MECH-489), **V3-EXQ-914a** (`weakens` MECH-236),
**V3-EXQ-919** (`weakens` MECH-321) and **V3-EXQ-922** (`weakens` MECH-150/151/152/ARC-041).
None has a confirmed autopsy yet.

---

## Queue Status

- **Total pending: 0 — THE QUEUE IS EMPTY.** (`origin/main` snapshot `c062227`, 2026-08-15T02:07Z:
  zero items of any status. The on-disk copy still shows 4 (603u, 920a, 934, 861c) but is ~1 day
  stale — 934's own manifest landed 01:52Z, i.e. it completed and left.)
- **ALERT: Queue low — fewer than 3 pending experiments.** This is the top operational item.
- Fleet-idle watcher (`~/Library/Logs/ree_fleet_idle_status.json`, generated 2026-08-15T03:39Z):
  `idle_risk=true`, claimable backlog **0** (threshold 3), `claimed_running=0`.
  **`ready_sd_validation_candidates` is EMPTY** — of 78 ready SDs, 38 have had their validation
  already run, 37 have no queueable validation, 3 are known churn. So refill needs a **fresh
  `/queue-experiment` design**, not a re-queue of anything on the shelf.
- All three cloud workers (`ree-cloud-2/3/4`) are unreachable — consistent with the scaler having
  powered them down against an empty queue, not a fault.
- **Owed successors: none.** All 205 EXQ ids referenced by open/blocked plan nodes were run
  through the four Step 7c checks; every one either has a manifest, is in `runner_status`, or
  fails the provenance check. No id passed all four cleanly. (Details under Active Plans.)

---

## Experiments Awaiting Review (0 indexed / 1 runner-only)

Per `pending_review.md` (generated 2026-08-13T20:32Z — pre-dates the 926a/927/928/930/931/932/
933/934 runs, so it under-reports; that is the degraded-run staleness, not a discrepancy):

### V3-EXQ-926 — `mech449_perseveration_nogo_falsifier` — ERROR
- Manifest stem: `v3_v3_exq_926_runner_error_20260813T045041Z_v3`, machine `ree-cloud-2`
- Non-zero exit 1; no runner sentinel (stdout-derived 'PASS' not trusted)
- **Already resolved** — V3-EXQ-926a (hardcoded Mac-only `EVIDENCE_DIR` fix, `supersedes` 926)
  ran 2026-08-14T17:10Z and **PASSed** (`supports` MECH-449/ARC-107).
- Action: this is a bookkeeping close, not a diagnosis — add the manifest stem to
  `discussed_experiment_dirs` at the next `/governance`.

**Not yet in `pending_review.md`** (landed after its 08-13 generation, will appear on the next
pipeline run): 926a, 927, 928, 929, 930, 931, 932, 933, 934, 920, 922a.

---

## Errors to Diagnose (0 with no queued or completed fix)

- **V3-EXQ-926** — fix queued *and* completed (926a, PASS). No action.
- `runner_status.json`'s 87 historical ERROR entries are all pre-2026-06 and lag badly under
  Phase 3 (last entry 2026-05-31); the authoritative live ERROR set is `pending_review.md`.
- Three further ERROR manifests landed in this window and are all marked `superseded` /
  `non_contributory` already: V3-EXQ-821a, V3-EXQ-870, V3-EXQ-918.

---

## Governance Agenda (9 recommendations `pending_user`)

Source: `promotion_demotion_recommendations.md` generated 2026-08-13T19:53Z.

| Claim | Current status | Recommendation |
|---|---|---|
| `MECH-142` | candidate | `hold_candidate_resolve_conflict` |
| `MECH-143` | candidate | `hold_candidate_resolve_conflict` |
| **`MECH-152`** | **provisional** | **`demote_to_candidate`** |
| `MECH-236` | candidate | `hold_candidate_resolve_conflict` |
| `MECH-289` | candidate | `hold_pending_v3_substrate` |
| `MECH-357` | candidate | `hold_pending_v3_substrate` |
| `SD-009` | candidate | `hold_candidate_resolve_conflict` |
| `SD-027` | candidate | `hold_pending_v3_substrate` |
| `SD-033e` | candidate | `hold_pending_v3_substrate` |

Two are worth taking first: **MECH-152** (the only demotion, and V3-EXQ-922a landed a
partial-recovery PASS on it 2026-08-14, after this file was generated) and **MECH-236**
(V3-EXQ-914a `weakens` it, 2026-08-11). `MECH-074d` is listed `discussing`, not `pending_user`,
and now carries two `weakens` results (894b, 894c).

**Granularity-debt recurrence (GOV-GRAN-1):** **P0 `dropped_handoff`: 0 — clean.** No autopsy
fired a trigger without a matching synthesis proposal. `unflagged_recurrence` (P1): **45 claims**,
list-only, no action taken — a human must discriminate coarse-claim vs coherent substrate campaign.
The six where the alignment distribution actually contains `weakened` (i.e. leaning toward genuine
granularity debt rather than measurement debt) are:

- `Q-034` — 6 hits / 2 signatures, alignment other=3 **weakened=3**
- `SD-005` — 3 hits / 1 signature, alignment **weakened=3** (all)
- `ARC-038` — 3 hits / 1 signature, alignment **weakened=3** (all)
- `INV-054` — 4 hits / 2 signatures, alignment other=2 **weakened=2**
- `MECH-111` — 5 hits / 3 signatures, alignment other=4 **weakened=1**
- `ARC-018` — 2 hits / 2 signatures, alignment unclear=1 **weakened=1**

The high-count entries are the opposite case and should **not** be read as granularity debt on
count alone: `MECH-058` (13 hits, alignment unclear=13, no weakened), `MECH-059` (12 hits, all
unclear), `SD-017` (11 hits, unclear=7 intact=2 untested=2), `INV-050` (7 hits, unclear=4
intact=3), `MECH-075` (7 hits, **intact=5** other=2) — no `weakened` anywhere in those, so they
read as measurement or implementation debt.

**Epistemic-category completeness (GOV-CAT-1): clean** — `missing_category` 0, `invalid_category`
0, `malformed_markers` 0, with **10 legacy `unkeyed_schema` warns** (singular `claim_id` targets,
P1, list-only — they cannot corrupt a count). The 674 historical enum instances remain correctly
excluded by the hit-scoped snapshot; nothing new has been introduced since the 2026-08-09 baseline.

---

## Active Plans Heartbeat (41 plans with open nodes, 172 open/blocked nodes)

Plans now carry a YAML `closure_plan` frontmatter with typed nodes rather than the legacy
"Status table"; the counts below are parsed from that.

| Plan | Open/blocked nodes | Last updated | Age |
|---|---|---|---|
| `policy_decomposition_trigger` | 1 | 2026-08-14 | 1d |
| `mech303_safety_threshold` | 1 | 2026-08-13 | 2d |
| `mech357_avoidance_efficacy` | 1 | 2026-08-13 | 2d |
| `orienting_epistemic_deficit_v3` | 5 | 2026-08-13 | 2d |
| `drives_motivation_v4` | 1 | 2026-08-05 | 10d **stale** |
| `substrate_stability_and_drift_detection` | 3 | 2026-08-03 | 12d **stale** |
| `explorer_ui_improvement` | 1 | 2026-08-02 | 13d **stale** |
| `arc_062_rule_apprehension` | 3 | 2026-08-01 | 14d **stale** |
| `behavioral_diversity_isolation` | 2 | 2026-08-01 | 14d **stale** |
| `psychiatric_failure_modes` | 5 | 2026-07-30 | 16d **stale** |
| `biology_grounding_convergence_v4` | 4 | 2026-07-24 | 22d **stale** |
| `memory_lifecycle_v4` | 4 | 2026-07-14 | 32d **stale** |
| `epistemic_overlay` | 1 | 2026-07-12 | 34d **stale** |
| `commitment_closure` | 2 | 2026-07-10 | 36d **stale** |
| `global_workspace_jlens` | 4 | 2026-07-10 | 36d **stale** |
| `ree_ai_design_critique` | 4 | 2026-07-10 | 36d **stale** |
| `self_model_v4` | 6 | 2026-07-01 | 45d **stale** |
| `developmental_dmn_v4` | 6 | 2026-07-01 | 45d **stale** |
| *(23 further plans, all 59–77d stale)* | 119 | 2026-05-30 → 2026-06-17 | — |

**37 of 41 plans are stale (>7 days since `last_updated`).** The four current ones are exactly the
four registered or touched in the last two days.

**PLAN STALING (worst, all with load-bearing blocked nodes and no update in ~2 months):**
`infant_substrate` (77d), `self_attribution` (72d, 3 blocked/high),
`sd_037_axis_b_sustained_threat_curriculum` (71d, 3 blocked/high),
`hippocampal_planning_v4` (66d, 7 blocked incl. 2 load-bearing),
`mirror_modelling_other_self_v5` / `multi_agent_ecology_v5` / `language_affect_adaptor_v6` (66d each).
Most of the V5/V6 cluster is blocked behind the same missing multi-agent substrate, so the staleness
is structurally honest rather than neglect — but `self_attribution` and `sd_037_axis_b` are V3-level
and are the two worth a look.

**Owed successors: none.** Every EXQ referenced by an open/blocked node was checked against
(a) the live queue, (b) the `origin/master` evidence tree, (c) `runner_status.json`, and
(d) provenance in `ree-v3` queue history + `experiments/`. Four looked owed on the absence checks
alone and were each resolved by a superseding run — these are **unreconciled plan rows, not
missing work**:

**Ran under a successor — plan prose needs a pointer refresh (no queue run needed):**
- `569a` (`behavioral_diversity_isolation:GAP-B`) — superseded by 569b ("supersedes 569a NaN
  crash"); the lineage ran through 569c/569d/569e/569g/569h/569i, all with manifests.
- `654e` (`arc_062_rule_apprehension:GAP-B`) — superseded by **654f**, which ran 2026-06-18
  (verbatim re-queue after a phantom-completion).
- `871` (`commitment_closure:GAP-4`) — superseded by **871a**, which ran 2026-08-02.
- `737a` (`ree_ai_design_critique:WS-1`) — the work landed under the bare `737` lineage
  (4 manifests, incl. 2026-07-20 and 2026-07-21, straddling the 737a queue window).

**Phantom Owner-EXQ ids (never created — needs a plan-prose correction, NOT a queue run):**
No `"queue_id"` entry was ever added for any of these in `ree-v3` history, no script exists, and
no manifest exists.
- **`631`** (`commitment_closure:GAP-4`) — **this is the known 2026-07-21 phantom recurring.** It
  was retired then (`REE_assembly` `1b0b4db4ee`, "retire phantom V3-EXQ-631, repoint MECH-342
  ecological rows at the 629/629b lineage") — but that fix repointed the *MECH-342* rows only, and
  `commitment_closure:GAP-4` still names it. It is a duplicate id for the experiment that ran as
  **V3-EXQ-629** (and 629b). Repoint GAP-4 the same way.
- **`483f`** (`sd_037_axis_b:P1b/P3/P4`) — named as the Phase-4 behavioural validation across three
  nodes; never minted.
- **`445i`** (`self_attribution:GAP-1`)
- **`816e`** (`policy_decomposition_trigger:REPOSE`)
- **`732b`** (`ree_ai_design_critique:WS-1`) — treat separately: 732b was a *deliberately refused*
  experiment (competence-floor observability confound), so the prose reference is arguably a
  correct historical mention rather than an error. Confirm intent before editing.

---

## Literature Pull Candidates

Only **5** items in `evidence_backlog.v1.json` (412 total) list `literature` in `evidence_needed`:

| # | Claim | Priority | Existing lit entries |
|---|---|---|---|
| 1 | `MECH-489` | medium | 0 |
| 2 | `MECH-151` | medium | 0 |
| 3 | `MECH-467` | medium | 0 |
| 4 | `Q-092` | low | 0 |
| 5 | `Q-093` | low | 0 |

`MECH-489` is the timely one: V3-EXQ-910 and 910a both landed `weakens` against it on 2026-08-10,
so a lit pull would inform the autopsy rather than arrive after it.

---

## Stale Claims

**None — clean steady state.** `audit_stale_claims.py` reports `stale_active: 0` at
2026-08-15T04:39Z. All buckets (A/B/C/D/U) empty. The only active claim in the file is the
`update-docs nightly` session that triggered this degraded run, at age <0.1h.

---

## Serve.py Status

**RUNNING** on port 8000 (PID 92343).

---

## Blocked Items

1. **The Mac's `REE_assembly` checkout is 272 commits behind `origin/master` and cannot
   fast-forward** (`[ahead 64, behind 272]`; `ree-v3` is `[ahead 3, behind 22]`). `git pull`
   aborts with "Not possible to fast-forward". The behind-range spans only 2026-08-14T01:38Z →
   2026-08-15T04:35Z and is dominated by IGW automation and phase3 writers, so the *content* lag
   is ~27h, not months. **Not repaired from this run** — reconciling a shared checkout carrying
   another live session's work is a `git pull --rebase` decision for an interactive session, and
   `governance.sh` must not regenerate derived artifacts from a 272-behind tree. This agenda was
   therefore built from `origin/*` blobs throughout.
   - Note the 64 ahead commits include real work (`STUDY-HUM-1` sections, preservation runbook)
     alongside IGW automation. Do **not** clear this with `reset --hard` or a bare `update-ref` —
     use `scripts/safe_adopt_ref.py`, or rebase via a throwaway worktree.
2. **Umbrella `REE_Working` is `[ahead 3]`** with `ref_convergence` refusing to converge: 2 of 3
   ahead commits are not provably upstream (`9632f351da` claim-open, `1b1ed4bd51` chip-claim).
   Nothing lost, no ref moved. Clear by cherry-picking oldest-first from a throwaway worktree.
3. **`governance.sh` not run this cycle** (Tier 2 contention — see banner). Governance/pending-review
   sections reflect the 2026-08-13 pipeline run.
4. **Fleet git health otherwise clean** — hub `ree-cloud-1` OK on both repos; `ree-cloud-2/3/4`
   unreachable (powered off against an empty queue, not a fault); 0 stranded run manifests,
   0 same-run_id-different-content across 5 graded untracked paths.

---

## Suggested order of work

1. **Refill the queue** — it is empty and the fleet is idle. No shelf-ready validation exists, so
   this is a fresh `/queue-experiment` design session. The three best-supported leads are the
   MECH-303 dedicated-signal build (validated by 930), the MECH-266 cap recalibration (band
   `[0.75, 1.75]` from 934), and a MECH-152 follow-up given 922a's partial recovery.
2. **Reconcile the Mac's `REE_assembly` checkout** (item 1 above) — everything else is reading
   around it.
3. **Run `/governance`** — 9 `pending_user` items, 11 unreviewed runs not yet in `pending_review.md`,
   and six `weakens` results with no confirmed autopsy.
4. **Fix the five phantom Owner-EXQ ids** in plan prose (a doc edit, not a queue run); `631`
   especially, since it has now recurred after a partial 2026-07-21 fix.
