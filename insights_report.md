# Project Insights — 2026-04-18

Generated: 2026-04-18T16:20:39Z

---

## Experiment Health

- **Total runs:** 517 (PASS: 102 | FAIL: 238 | ERROR: 63 | UNKNOWN: 114 | error rate: 12.2%)
  - High UNKNOWN count (22%) indicates runner/indexer regex parsing gaps — many runs never classified.
- **High-iteration experiments** (3+ lettered iterations):
  - **V3-EXQ-085 — 14 iterations** (085 through 085o, all FAIL). Homeostatic drive / z_goal seeding chain. Predominantly MECH-071/SD-012 territory. No successor currently queued — the chain appears abandoned without a PASS.
  - **V3-EXQ-047 — 9 iterations** (047 → 047k PASS). Closed by 047k PASS.
  - V3-EXQ-002 — 6 iterations (SD-003 chain, all FAIL; superseded by later SD-003 redesigns e.g. EXQ-330).
  - V3-EXQ-020 — 6 iterations (MECH-057 / event supervision, all FAIL).
  - V3-EXQ-074 — 6 iterations (closed by 074f PASS).
  - V3-EXQ-076 — 6 iterations (all ERROR/FAIL, no PASS; SD-012/MECH-114 allostatic gating).
  - V3-EXQ-166 — 6 iterations (all UNKNOWN — runner did not classify outputs).
- **Recurring ERROR claims** (≥2 ERROR entries):
  - MECH-112 (4 ERRORs) — goal/structured-latent tests repeatedly crash
  - SD-003, SD-012, SD-018, ARC-007, MECH-113, MECH-116, MECH-163, MECH-188, INV-052 (2 each)
- **Top FAIL accumulators:**
  - SD-003 (28 FAILs) — dominant failure sink; counterfactual attribution is still the hardest open pipeline
  - MECH-102 (8), SD-005 (7), MECH-100 (7), MECH-099 (6), SD-007 (6), MECH-071 (5)
- **Stalled V3 chains** (latest FAIL, no successor in queue): ~128 base IDs. Many are superseded by redesigns under new numbers (e.g. SD-003 chain migrated to EXQ-320/330 series), so the raw count overstates abandonment. Genuine stall candidates worth auditing:
  - V3-EXQ-085 (homeostatic drive, 14 FAILs)
  - V3-EXQ-166 (6 UNKNOWNs — needs manifest repair)
  - V3-EXQ-076 (SD-012 allostatic gating, 6 FAIL/ERROR)

---

## Substrate Bottlenecks

- **Substrate queue contains 6 items — all marked `implementation_status: implemented`.** No ready-but-unimplemented SDs; no blocked SDs.
- **SDs with failure_records** (implemented but validation experiments not yet passing):
  - **SD-013** (E2_harm_s interventional training) — 1 failure; EXQ-330a claimed, running
  - **SD-015** (z_resource encoder) — 3 failures; EXQ-326a queued
  - **SD-019** (harm affective non-redundancy) — pending validation
  - **SD-020** (z_harm_a affective surprise PE) — EXQ-324c pending (EWIN-PC requeue)
  - **SD-021** (descending pain modulation) — EXQ-325b pending
  - **SD-022** (directional limb damage) — implemented, pending downstream validation
- Bottom line: substrate is not the blocker — implementations are in place for 5 active open SDs. The bottleneck is validation experiments finishing on the new substrate.

---

## Governance State

- Claims with `v3_pending: true`: **4**
- Claims with `implementation_phase: v3`: **100**
- Promotion/demotion queue: **36 decisions, all `applied` — 0 pending**. Governance cycle is caught up.
- Superseded manifests (rework-excluded from scoring): **59 runs**

---

## Literature Coverage

- Backlog total: 132 items, all `status: open` (the backlog does not flip to `covered`).
- Literature-required items: 19 total, **0 at priority 1**.
- Medium-priority literature open: SD-003-prereq, SD-018, ARC-028, MECH-057, MECH-122, Q-019, Q-036, onboarding.
- Recent lit-pulls (WORKSPACE_STATE 2026-03-28/29 + 2026-04-05): SD-003 (4 entries), ARC-016 (6), ARC-024 (3), Q-claims low-priority (51), INV-044/MECH-166/ARC-045 (9), medication-sleep-dementia (6). Coverage is healthy — no urgent gaps.

---

## Human-Intervention Patterns

Derived from runner_status and WORKSPACE_STATE sessions:

- **EWIN-PC setup crashes** — multiple 2026-04-18 entries show experiments ERROR at ~0.1s on EWIN-PC and get re-queued to Mac (EXQ-321c, 324c, 325b, 355b, 375a, 385b, 395a, 397a, 418b). This is a recurring machine-affinity friction; the second machine is still losing setup-path time. Pattern: write once, ERROR on EWIN-PC, manually requeue for Mac.
- **diagnose-errors sessions are frequent** — 2026-03-28/29/30 sessions each cleared 5–22 ERROR/UNKNOWN chains. Pattern repeats when runner regex fails to classify new script output formats.
- **Long iteration tails on homeostatic/goal claims** — EXQ-085 (14x) and EXQ-074/076 series required many manual redesigns before any PASS. Suggests pre-registration / smoke-testing is catching some issues but not the ones that matter (drive calibration, z_goal seeding).
- **Low-friction tasks** — lit-pull, morning-digest, queue-experiment dry-runs consistently complete in a single session without rework.

---

## Recommendations

1. **Audit EXQ-085 chain and decide: resurrect or retire.** 14 FAIL iterations with no successor — either V3-EXQ-326/326a now supersedes the scientific question and EXQ-085* should all be marked `superseded`, or the underlying SD-012 drive hypothesis needs a fresh design pass. Leaving the chain dangling inflates the "stalled" count without scoring impact.
2. **Fix EWIN-PC setup path.** Nine 2026-04-18 requeues trace to the same ~0.1s setup crash. One diagnose-errors cycle on the second machine would stop the manual requeue loop and unblock ~half a day of parallel compute.
3. **Repair V3-EXQ-166 chain manifests** (6 UNKNOWNs). Runner regex / output-format mismatch is suppressing evidence signal. Quick win for the indexer.
4. **SD-003 decision point.** 28 FAILs accumulated across V2 and V3 iterations. With SD-013 now implemented and EXQ-330a running, the next result should be treated as a go/no-go: if cf_gap_ratio still fails to exceed 2.0, SD-003 needs a substrate redesign (ARC-033 extension) rather than another experiment tweak.
