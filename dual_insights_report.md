# Dual-System Insights — 2026-08-01

Generated: 2026-08-01T10:46:41Z
Companion to `/insights` (REE_assembly/insights_report.md) — this report never edits
that skill or its output, and vice versa. Both reports were regenerated together in this
session; REE-side figures below reuse the `/insights` gather rather than re-reading the same
files twice, per this skill's Key Rules.

---

## REE-side (cognitive substrate)

- **Competence-floor campaign (MECH-457 cluster, `hypothesis_space_registry.v1.json` qid
  `competence_floor`):** 20 hypotheses registered since 2026-07-13 (hero question). Current
  state: 12 eliminated, 2 split into successor questions, 4 confirmed, **2 genuinely alive**:
  `H-mech476-dose-response` and `H-mech476-novelty-tagging` (the two Krakauer/Moncada-&-Viola
  over-training and behavioural-tagging paradigms ported into MECH-476). These map directly onto
  the live EXQ-836 chain (5 iterations, last outcome FAIL, claim MECH-476 — see `/insights`
  Experiment Health) — the campaign's active front, not a dead end. The re-derive brake has fired
  on at least one prior axis in this cluster (capacity axis, per `failure_autopsy_V3-EXQ-769`)
  and stands: same-axis re-queues on eliminated legs are refused.
- **Conversion-ceiling campaign (F-dominance cluster, qid `conversion_ceiling_root`):** 6
  hypotheses registered 2026-07-11, grown by 2 fanout events. Current state: 2 eliminated
  (`H-reward-balance`, plus one other), **4 alive**: `H-substrate-ceiling`, `H-f-dominance`,
  `H-objective-misspecification`, `H-observation-interface`. This is the wider, less-narrowed of
  the two campaigns — 4 of 6 original candidate roots are still live after 3 weeks, versus the
  competence-floor cluster's 2 of 20 (which has fanned out and eliminated far more aggressively
  in the same period). Read as a REE-side fact this says the conversion ceiling's root cause is
  less understood today than the competence-floor mechanism is, independent of either campaign's
  process health.
- **High-iteration chains by confidence trend** (reusing `/insights` Step 2 iteration counts,
  relabeled by claim trajectory rather than "owned/unowned"): EXQ-603 (MECH-260/313/358/Q-045/
  SD-059, 18 iterations) and EXQ-460 (8 claims incl. SD-034/MECH-090/445/446, 15 iterations) both
  terminated PASS — confidence gaining. EXQ-485 (SD-033b/MECH-263, 14 iterations) and EXQ-543
  (ARC-062/MECH-309/INV-074/MECH-334, 12 iterations) both terminated FAIL but are liveness-confirmed
  live campaigns, not losing confidence so much as still being actively discriminated. EXQ-445
  (7 iterations, no claim tags, last outcome `weakens`) is the one chain in the top 20 whose last
  labeled direction is an explicit confidence loss rather than a FAIL/PASS binary — worth a closer
  look outside this report's scope if a claim owner wants to trace which claim it currently maps to.
- **Ready-and-unbuilt substrate count:** 18 `substrate_queue.json` entries carry `ready: true`
  and an `implementation_status` other than `implemented` (SD-047, SD-048, INF-ENV-002,
  INF-ENV-004, MECH-341, MECH-090, `scaffolded_sd054_onboarding`,
  `test_bed_enrichment_crystallization_necessity`, `modulatory-bias-selection-authority`,
  `crf-availability-maintenance`, `sd_actor_critic_action_learning`,
  `agency_comparator_testbed_sd047`, `rebinding-harness-p0-coverage-decoupling`, SD-074,
  SD-PROBE-WARMUP, `sd_zworld_warmup_optimizer_group`, SD-MEL-PRODUCER,
  MECH324-REACQ-WINDOW-GATING-DECOUPLE) — treat as an upper bound; several carry substantial
  free-text amend history this pass did not fully parse (see `/insights` Substrate Bottlenecks
  caveat).

---

## REE_assembly-side (governance throughput)

- **Autopsy turnaround:** matched 68 single-run-named autopsies against their target manifest
  timestamp within the last 30 days — **median 1.0 day**. The distribution has a fat tail from a
  backlog-clearing cycle on 2026-07-19/20: the 5 longest-outstanding cases in the window are all
  from that clearing (EXQ-604c 43 days, EXQ-689d 29, EXQ-699 27, EXQ-708 21, EXQ-707b 21); outside
  that cluster, turnaround is same-day to next-day (5 of the fastest matched cases resolved same
  calendar day as the manifest landed). Separately, the current pending-review queue
  (`pending_review.md`, regenerated 2026-08-01T10:09Z) holds 6 unadjudicated FAILs, the
  longest-outstanding of which is V3-EXQ-841 (landed 2026-07-31T08:05Z, ~26.5h old as of this
  report) — already claimed by an active TASK_CLAIMS session (`elastic-merkle-e0cca8`,
  2026-08-01T10:11Z), so not an unowned delay.
- **Decision backlog age:** **0** — all 169 rows in the current `promotion_demotion_recommendations.md`
  Decision Queue (regenerated 2026-08-01T10:09Z) read `decision_status: applied`. The 2026-07-30
  and 2026-07-31 governance cycles (commits `a3c411ad00`, `39664fc765`, `eabe9c453b`, `37f1af866f`)
  cleared what the 2026-07-26 run of this report flagged as a 12-row `pending_user` backlog
  (oldest ~118 days at the time) — that backlog no longer exists.
- **Claim churn:** `TASK_CLAIMS.json` currently holds 76 entries spanning 2026-07-29T23:37Z to
  2026-08-01T10:21Z (~2.5 days — the file is periodically pruned of `done` entries older than 24h
  per `prune_task_claims_done.py`, so this is the observable window, not a true trailing-7-day
  rate). 76 opened / 74 closed in that window; **2 active** currently
  (`igw-214-proposal-for-mech-203`, `elastic-merkle-e0cca8`); **1 stale by the 6-hour rule**
  (`igw-214-proposal-for-mech-203`, claimed 2026-07-30T19:11Z, ~39.5h old as of this report — a
  staged IGW proposal, not necessarily an abandoned claim; worth a stale-claims audit pass but not
  flagged here as a live conflict).
- **Concurrency friction rate:** 20 of 42 dated WORKSPACE_STATE.md entries in the trailing-200-line
  tail (2026-07-20 to 2026-08-01) contain at least one of the documented friction signatures
  ("throwaway worktree", "swept", "read-modify-write", "contamination", "skew", "index.lock") —
  **~48%**. Caveat: this count includes entries that *describe fixing or documenting* a friction
  mechanism (e.g. "Fixed worktree-blindness in ree-v3/experiments/pack_writer.py") alongside
  entries reporting a live incident that actually cost a session work (e.g. the 2026-07-20T09:57Z
  governance-apply abort on a collision, and the 2026-07-30T19:10Z TASK_CLAIMS foreign-entry sweep
  surfaced and preserved under remedy (a)) — so 48% is an upper bound on true incident rate, not a
  clean measurement. The two confirmed live-incident entries in the tail both self-resolved within
  the same session (collision cleared; swept content preserved verbatim, owning session named) —
  no unresolved friction currently sitting open.
- **Literature-pull cadence:** 7 lit-pull mentions in the WORKSPACE_STATE tail; the
  `evidence/literature/` directory shows 6 `targeted_review_*` entries landed in the trailing 4
  days (connectome/MECH-204 today, MECH-457 consolidation + MECH-457 baseline-informativeness +
  Q-085 + SD-082 on 2026-07-29, connectome/MECH-324 on 2026-07-28) — roughly one review every
  1-2 days, matching `/insights`' "healthy, active cadence" read.

---

## Where the two overlap

- **EXQ-604c (MECH-314b/314c/Q-044) is the one confirmed case of "hard problem plus slow
  adjudication" this cycle.** REE-side: the confirmed autopsy (`failure_autopsy_V3-EXQ-604c_2026-07-20`)
  found MECH-314b/314c are Phase-1 broadcast scalars, argmax-invariant *by construction* — an
  observation bottleneck no amount of seeds or re-queuing can resolve, and the re-derive brake has
  fired (3rd `substrate_ceiling` adjudication on this axis). That is a real, structural finding,
  not a process failure. REE_assembly-side: the run that produced this finding sat **43 days**
  between manifest and autopsy — the single longest turnaround in the 30-day autopsy-turnaround
  sample above. Only the second half is actionable by changing process: the scientific verdict
  (observation bottleneck, no further same-axis build owed) would not have changed by adjudicating
  it sooner, but the 43 days during which MECH-314's failure volume accumulated unexplained (it
  was the second-highest July FAIL count per `/insights`' prior runs) is a throughput cost, not a
  ceiling.
- **EXQ-689d, EXQ-699, EXQ-708, EXQ-707b** (29/27/21/21-day turnarounds, same 2026-07-19/20
  clearing batch) are worth the identical REE-side-vs-REE_assembly-side check — this pass
  identified them as slow-adjudication candidates but did not run the corresponding REE-side
  liveness read for each; flagging rather than asserting an overlap to avoid overclaiming.
- **No overlap found on the competence-floor or conversion-ceiling campaigns themselves** — both
  are actively and rapidly adjudicated (competence-floor has fanned out and eliminated 12 of 20
  hypotheses in under 3 weeks; the 30-day autopsy-turnaround median of 1.0 day covers this period).
  Their remaining "alive" hypothesis counts (2 and 4 respectively) reflect real unresolved science,
  not a stuck governance queue.
