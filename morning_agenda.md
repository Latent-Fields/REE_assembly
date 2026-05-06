# Morning Agenda -- 2026-05-06

Generated: 2026-05-06T04:25:03Z

---

## Queue Status
- Total pending: 5 (Mac: 0 | PC: 0 | EWIN: 0 | any: 5)
- Plus 2 claimed/in-flight: V3-EXQ-514c (any), V3-EXQ-514e (DLAPTOP-4.local)
- [ALERT] V3-EXQ-525 still listed `pending` in the queue but a FAIL manifest exists at 2026-05-05T22:04 (`v3_exq_525_sd003_attribution_anchor_20260505T220444Z`). Confirm whether this is a re-queue, a stale entry to clean, or a duplicate before it gets re-run.

---

## Experiments Awaiting Review (8 indexed / 5 runner-only)

### V3-EXQ-418f -- SD-016 attention-uniformity probe -- PASS (diagnostic)
- **Claims tested:** SD-016 (status: implemented, exp_conf=0.525, lit_conf=0.788, quadrant: plausible_unproven, 9 entries: 2S/6W/1M)
- **Key metrics:** D2 attn_entropy_mean=2.716 (uniform_ref=2.773); D3 raw_dotprod_std=3.14; D4 q_norm_mean=1.81, k_norm_mean=1.00 (k std=2.44, range 0.09-7.28). All 4 acceptance checks PASS.
- **Classification:** diagnostic probe (`evidence_class: diagnostic_probe`, `evidence_direction: diagnostic`)
- **Governance impact if confirmed:** **None.** Manifest note explicitly states: "MUST NOT update SD-016 claim confidence -- this is instrumentation, not evidence." Mark discussed; do not score.
- **Supersedes:** V3-EXQ-418e

### V3-EXQ-452a -- MECH-257 dual-function E2 (reef) -- FAIL (diagnostic)
- **Run #1:** `v3_exq_452a_mech257_dual_function_e2_reef_20260505T184639Z_v3`
- **Run #2:** `v3_exq_452a_mech257_dual_function_e2_reef_20260505T215753Z_v3`
- **Claims tested:**
  - MECH-257 (candidate, exp_conf=0.000, lit_conf=0.772, plausible_unproven, 2 entries 2S/0W) -- per-claim direction: `weakens`
  - SD-013 (provisional, exp_conf=0.766, lit_conf=0.868, confirmed_established, 8 entries 7S/1W) -- per-claim: `mixed`
  - ARC-033 (provisional, exp_conf=0.793, lit_conf=0.797, confirmed_established, 36 entries 21S/7W/8M) -- per-claim: `mixed`
- **Classification:** diagnostic (per-claim splits set; `evidence_direction: diagnostic` at run level)
- **Governance impact if confirmed:** Two `weakens` entries land on MECH-257 (already exp_conf=0.000); SD-013/ARC-033 absorb `mixed` entries -- minor downward nudge to both, neither cross a gate.
- **Note:** Two run manifests with the same outcome -- decide whether to discard one (likely identical replicate) before review.

### V3-EXQ-454a -- ARC-016 adaptive commitment (reef) -- FAIL
- **Claims tested:** ARC-016 (provisional, exp_conf=0.702, lit_conf=0.864, confirmed_established, 31 entries 16S/12W/3M)
- **Classification:** evidence (`evidence_direction: weakens`)
- **Governance impact if confirmed:** Adds 1 `weakens` to ARC-016 (12 -> 13); exp_conf will tick down from 0.702 toward demote zone but ARC-016 still well above the 0.62 promote-floor.
- **Supersedes:** none in queue (reef-superseding wave, but no `supersedes` field set)

### V3-EXQ-525 -- SD-003 attribution anchor -- FAIL
- **Run:** `v3_exq_525_sd003_attribution_anchor_20260505T220444Z_v3` (note: this is the queue-supersedes-V3-EXQ-205 anchor)
- **Claims tested:**
  - SD-003 (status: superseded, exp_conf=0.669, lit_conf=0.842, confirmed_established, 89 entries 27S/39W/23M) -- per-claim: `weakens`
  - ARC-033 (provisional, exp_conf=0.793) -- per-claim: `weakens`
- **Key metrics:** hf_r2_mean=0.336 (low), attribution_gap_mean=-0.00156, intact_vs_ablated_mean=-0.00063 (no separation)
- **Classification:** evidence
- **Governance impact if confirmed:** Adds 1 `weakens` each to SD-003 and ARC-033. SD-003 is already `superseded` so the entry is bookkeeping; ARC-033 ticks slightly down (21S/8W -> 21S/9W).
- **Caveat:** SD-003 status=superseded -- check whether this experiment should still be scored against it, or routed to its successor claim.

### V3-EXQ-445g -- SD-032b dACC (reef) -- FAIL
- **Run:** `v3_exq_445g_sd032b_dacc_reef_20260505T223845Z_v3`
- **Claims tested:**
  - SD-032b (candidate, exp_conf=0.503, lit_conf=0.885, plausible_unproven, 22 entries 12S/1W/9M) -- per-claim: `does_not_support`
  - MECH-258 (candidate, exp_conf=0.954, lit_conf=0.882, confirmed_established, 17 entries 16S/0W/1M) -- per-claim: `supports`
  - MECH-260 (candidate, exp_conf=0.954, lit_conf=0.715, confirmed_established, 9 entries 9S/0W) -- per-claim: `supports`
- **Classification:** evidence (per-claim splits already set)
- **Governance impact if confirmed:** SD-032b absorbs another `does_not_support` (W will go 1->2, M still 9), pushes exp_conf below promote threshold -- consistent with current `hold_pending_v3_substrate` recommendation. MECH-258/260 each gain a clean `supports`, but both already saturated.

### V3-EXQ-517b -- MECH-302 relief-completion discriminative pair -- FAIL (non_contributory)
- **Run:** `v3_exq_517b_mech302_relief_completion_discriminative_pair_20260506T013515Z_v3`
- **Claims tested:** MECH-302 (candidate, exp_conf=0.422, lit_conf=0.903, plausible_unproven, 9 entries 4S/3W/2M)
- **Classification:** diagnostic / scope correction (`evidence_direction: non_contributory`)
- **Governance impact if confirmed:** None -- `non_contributory` is excluded from scoring. Note states EXQ-517a's mean 0.33 events/seed was a length artifact (heal_rate=0.002/step needs ~500 steps; 517b extended episode length 150 -> 300 but still failed). MECH-302 already has a `pending_user` hold_pending_v3_substrate recommendation; this run does not move the needle.

### V3-EXQ-418k -- SD-016 context memory reef -- FAIL (run_id parsed as bare timestamp)
- **File:** `evidence/experiments/v3_exq_418k_sd016_context_memory_reef_20260505T223834Z_v3.json` (untracked)
- The indexer extracted only the trailing timestamp as the run_id, so the run shows up as `20260505T223834Z_v3` in `pending_review.md`. Likely a parser-pattern miss on the `context_memory_reef` token; not a bad manifest.
- **Action:** add the file to git (it is currently untracked alongside its parent directory `v3_exq_418k_sd016_context_memory_reef/`), and inspect the run_id parsing rule in `build_experiment_indexes.py` if other reef-suffixed runs are also being mis-parsed. Currently being credited to SD-016 as one `weakens` entry.

---

## Errors to Diagnose (4)

These ERROR entries in `runner_status.json` have no later lettered successor and no fix queued. Onboarding smoke runs (`V3-ONBOARD-smoke-EWIN-PC`, `V3-ONBOARD-smoke-ree-cloud-1`) are excluded -- they belong to the contributor onboarding flow, not the science queue.

- **V3-EXQ-418j** (2026-05-05T21:31, exit 1, 62.5s on ree-cloud-1) -- "SD-016 context memory reef fix: 2x2 factorial" -- **needs /diagnose-errors** (most recent; reef substrate experiment)
  - Claimed by: SD-016 / SD-050 reef substrate
- **V3-EXQ-495** (2026-04-28T21:13, exit -15 SIGTERM, 14383s on ree-cloud-1) -- "MECH-163 V3 full-completion gate (VTA / hippocampally-planned arm)" -- **cloud timeout pattern (matches EXQ-514a)**; may need DLAPTOP-4.local routing
  - Claimed by: MECH-163
- **V3-EXQ-455a** (2026-04-23T23:23, exit 1, 0.0s on DLAPTOP-4.local) -- "SD-032a salience coordinator behavioural -- V_s-enabled re-run" -- **immediate-exit failure, looks like an import/config bug**
- **V3-EXQ-449c** (2026-04-24T02:18, exit 1, 0.1s on DLAPTOP-4.local) -- "MECH-074b BLA retrieval bias on action selection -- V_s-gated" -- **immediate-exit failure, same pattern as 455a**

The pending-review file also lists 4 UNKNOWN runner-only entries (V3-EXQ-418k, V3-EXQ-445g, V3-EXQ-514d, V3-EXQ-517b). The 445g, 514d, 517b ones already have indexed manifests (they are really PASS/FAIL, not UNKNOWN -- pending-review hint suggests build_experiment_indexes.py needs re-running after these landed). Re-running governance.sh did not clear them -- worth a closer look at why the indexer is not picking them up by queue_id.

---

## Governance Agenda (6 recommendations)

| Claim | Status | Recommendation | Evidence (S/W/M) | exp_conf | lit_conf |
|-------|--------|----------------|------------------|----------|----------|
| **MECH-302** | candidate | hold_pending_v3_substrate | 4/3/2 | 0.422 | 0.903 |
| **MECH-303** | candidate | hold_pending_v3_substrate | (new claim, low evidence) | -- | -- |
| **MECH-304** | candidate | hold_pending_v3_substrate | (new claim, low evidence) | -- | -- |
| **Q-036** | open | narrow_open_question | (open question, conflict_ratio < 0.35) | -- | -- |
| **SD-048** | candidate | hold_pending_v3_substrate | (V3-pending) | -- | -- |
| **SD-049** | candidate | hold_pending_v3_substrate | (V3-pending; V3-EXQ-514c/d/e in flight) | -- | -- |

All other 12 hold_pending_v3 entries appearing alongside these have status `applied` (already actioned in prior governance cycle).

---

## Literature Pull Candidates (Top 5)

Backlog has only 2 literature-needed items remaining (after the 2026-05-05 epoch-filter fix that exempted lit entries from staleness). Both at priority `medium`.

| # | Backlog ID | Claim | Subject | Priority | Existing entries |
|---|-----------|-------|---------|----------|-----------------|
| 1 | EVB-PINNED-Q019 | Q-019 | Three-Gate BG Architecture: Literature Extraction | medium | 0 |
| 2 | EVB-0131 | (onboarding phantom) | -- | medium | 0 |

EVB-0131 is a known phantom (referenced in WORKSPACE_STATE.md / fix-backlog-lit-epoch-filter completion note as the only remaining `missing_literature_evidence` reason after the surgical fix). EVB-PINNED-Q019 is the only genuine literature backlog item -- worth queuing a `/lit-pull` for the BG three-gate cluster.

---

## Serve.py Status
- RUNNING on port 8000 (PID 9657)

---

## Blocked Items

- **Indexer warnings (informational, not blocking):** 13 multi-claim runs lacking `evidence_direction_per_claim` are still falling back to blanket direction. Most are `non_contributory` or `superseded` blanket applications, so the impact on scoring is contained. Two new ones from this cycle worth flagging:
  - `v3_exq_433e_sd029_eventcond_comparator_reef_20260505T072754Z_v3` -- blanket `weakens` applied to [SD-029, MECH-256]
  - `v3_exq_433c_sd029_eventcond_comparator_20260423T232350Z_v3` -- same pattern
- **review_tracker.json fall-throughs:** 4 of the 5 runner-only entries in pending_review (445g, 514d, 517b, plus 418k) have indexed manifests but pending-review still flags them as UNKNOWN with the hint "run build_experiment_indexes.py" -- governance.sh just ran and the issue persists. Likely a queue_id <-> run_id reconciliation gap in `generate_pending_review.py`.
- **TASK_CLAIMS.json was malformed at session start** (missing `},` between two entries). Repaired before writing this agenda; no other writers were active so nothing was at risk.
- **Duplicate EXQ-525 manifest vs. queue:** see Queue Status alert above.
- **EXQ-452a duplicate run manifests** (18:46 + 21:57, identical outcome): worth deciding whether to mark one superseded or treat as a legitimate replicate before review.
