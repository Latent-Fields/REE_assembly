# Diagnose Staging Report -- 2026-04-27

**Session:** afternoon scheduled diagnose-errors (staging mode)
**Generated UTC:** 2026-04-27T14:20:31Z
**Status:** **NO ACTIONABLE ERRORS**

---

## Summary

Three unaddressed ERROR entries surfaced by a successor scan of `runner_status.json`. All three are non-actionable:

| Queue ID | When | Class | Disposition |
|----------|------|-------|-------------|
| V3-EXQ-449c | 2026-04-24 | Intentional `NotImplementedError` stub | Gates not met (476/445d FAIL) |
| V3-EXQ-455a | 2026-04-23 | Intentional `NotImplementedError` stub | Gates not met (476 FAIL) |
| V3-EXQ-008  | 2026-03-17 | Old, already superseded                | Successors `008r2`/`008r3` exist (legacy r-suffix) |

The runner_status reconciliation merged 4 IDs from per-machine files (`V3-EXQ-490a`, `V3-EXQ-494`, `V3-EXQ-496`, `V3-EXQ-497`) into the monolithic `runner_status.json` (now 561 completed entries).

---

## V3-EXQ-449c (MECH-074b BLA retrieval bias on action selection -- V_s-gated)

**Root cause:** Intentional placeholder. Script raises `NotImplementedError` at line 115 of `experiments/v3_exq_449c_mech074b_bla_retrieval_bias.py` with the message:

> "V3-EXQ-449c full implementation pending: awaiting (a) V3-EXQ-476 PASS, (b) V3-EXQ-445d PASS, and (c) MECH-074b hippocampal consumer wiring landed on SD-035 (retrieval-bias-aware replay path must be added before the bias signal can influence behaviour)."

**Gate status (as of 2026-04-27):**
- V3-EXQ-476: ERROR. Successors V3-EXQ-476a, V3-EXQ-476b: both FAIL (2026-04-24).
- V3-EXQ-445d: ERROR. Successor V3-EXQ-445e: FAIL (2026-04-23).
- MECH-074b consumer wiring on SD-035: not landed.

**Disposition:** Leave in `discussed_experiment_dirs`. Re-queue only after MECH-269 V_s validation passes (currently being explored under MECH-269b in V3-EXQ-490a).

---

## V3-EXQ-455a (SD-032a salience coordinator behavioural -- V_s-enabled re-run)

**Root cause:** Intentional placeholder. Script raises `NotImplementedError` at line 107 of `experiments/v3_exq_455a_sd032a_salience_with_vs.py` with the message:

> "V3-EXQ-455a full implementation pending: awaiting V3-EXQ-476 cascade gate PASS and MECH-284 Phase 3 consumer landing. Do not run until V_s flags have been confirmed to break the baseline monostrategy lock."

**Gate status:** Same upstream gates as V3-EXQ-449c. Not met.

**Disposition:** Leave in `discussed_experiment_dirs`. Re-queue only after the V_s cascade gate passes.

---

## V3-EXQ-008 (SD-003 Larger World + 3x3 Observation)

**Root cause:** Surfaced as "unaddressed" because the successor scan uses regex `^V3-EXQ-(\d+)([a-z]*)$`, which does not match the legacy `r2`/`r3` suffixes used in March 2026 before the current alphabetic-suffix policy was adopted.

**Successors that already exist:**
- V3-EXQ-008r2: FAIL, 2026-03-17T18:37
- V3-EXQ-008r3: FAIL, 2026-03-17T18:49

**Disposition:** Already in `discussed_experiment_dirs` per the 2026-04-27T05:20 diagnose-errors session (TASK_CLAIMS.json). No further action. The SD-003 scientific question is otherwise carried forward by current SD-003 work in the V3 substrate.

---

## Runner status reconciliation

Merged 4 entries from per-machine files into monolithic `runner_status.json`:

- V3-EXQ-490a (ree-cloud-1)
- V3-EXQ-494 (Mac)
- V3-EXQ-496 (Mac)
- V3-EXQ-497 (Mac)

Monolithic `completed` count after merge: 561. No new ERRORs surfaced by the merge.

---

## Awaiting human confirmation

**None.** No diagnoses written; no draft scripts written; no queue edits made. This staging report is informational only.

**Recommended next action:** Continue Step 2 of the scheduled task (queue-experiment skill) to check for substrate-ready proposed experiments.
