# Diagnose-Errors Staging Report

**Session**: ree-diagnose-queue-2026-04-15-b / diagnose-errors wave 1
**Generated**: 2026-04-15
**Mode**: STAGING (headless, autonomous, cowork subagent)

---

## Summary (2026-04-15 update)

**0 unaddressed errors requiring new fix scripts.**

All 51 ERROR entries in runner_status.json were analyzed. No new EXQ IDs from the reserved
range (419-428) were used.

### Gap reconciliation

One entry was present in a per-machine file but missing from the monolithic runner_status.json:

| Queue ID | Machine | Result | Completed |
|---|---|---|---|
| V3-EXQ-353 | DLAPTOP-4.local | PASS | 2026-04-15T13:24:50Z |

V3-EXQ-353 (ARC-033/SD-003/SD-013 interventional vs observational training comparison)
was merged into runner_status.json. Total entries: 495.

### Error chain analysis

| Category | Count |
|---|---|
| ONBOARD smoke tests (excluded -- not scientific) | 2 |
| ERRORs with standard letter-suffix successors (chain resolved) | 48 |
| ERRORs addressed via older rN naming convention | 1 |
| **Truly unaddressed, requiring new fix script** | **0** |

**ONBOARD smoke tests:**
- V3-ONBOARD-smoke-EWIN-PC: Machine setup test. ree-cloud-1 is operational. EWIN-PC rerun is a machine operator task.
- V3-ONBOARD-smoke-ree-cloud-1: ree-cloud-1 is fully operational -- many successful runs since.

**The one apparent gap -- V3-EXQ-008:**

V3-EXQ-008 (SD-003 Larger World + 3x3 Observation, 2026-03-17) shows ERROR with no
standard alphabetic successor. However, it was immediately addressed via the older rN naming:

- V3-EXQ-008r2 (FAIL, same day): Fixed MRO init order bug. calibration_gap=0.020.
- V3-EXQ-008r3 (FAIL, same day): Scaled to 16x16, 800 episodes. calibration_gap=-0.007.

Scientific conclusion reached: observation-autocorrelation hypothesis rejected. SD-003 was
subsequently redesigned to use z_harm_s counterfactual pipeline (ARC-033). EXQ-205 PASS
confirms new design works (2026-04-02). No further action required.

**Standard letter-suffix chains (48 IDs) -- all resolved:**

| Last result | Example chains |
|---|---|
| PASS | EXQ-074f, EXQ-057b, EXQ-248b, EXQ-249b, EXQ-251b, EXQ-254c, EXQ-257b |
| FAIL | EXQ-075d, EXQ-076d/e/f, EXQ-084d, EXQ-260b, EXQ-261b, EXQ-262b, and many more |
| UNKNOWN | EXQ-250b, EXQ-263a/b (queue-done perspective) |

---

## Note on EXQ-263a/263b UNKNOWN Result Types

Both show `result=UNKNOWN` in runner_status.json with outcome strings in summary fields.
If governance scoring needs formal PASS/FAIL status for MECH-216, these manifests may
need manual result-type correction. Not urgent -- does not block other work.

---

## EXQ ID Reservation

Reserved range 419-428 for this session. None consumed -- all errors were addressed.

---

*Structured data: `evidence/planning/diagnose_staging.json`*
