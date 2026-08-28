# Failure Autopsy (diagnostic adjudication): V3-EXQ-933a -- sleep GAP-9 entry-pressure fix validation

**Generated:** 2026-08-28T17:11:55Z | **Scope:** single | **Status:** confirmed (interactive gate 2026-08-28)
**Session:** failure-autopsy-20260828-diagbatch | **Trigger:** `experiment_purpose: "diagnostic"`, clean unflagged PASS, no prior autopsy coverage.
**Run:** `v3_exq_933a_sleep_gap9_entry_pressure_fix_20260826T072405Z_v3` (ree-cloud-4, recording complete, dry-run gate clean, 1.3s). Successor validation of the SD-SLEEP-ENTRY-PRESSURE build routed by the confirmed `failure_autopsy_929-933-sleep-gap9-cluster_2026-08-16`. Run directly per GOV-REUSE-1 (no queue entry, deliberate and documented in three places).

## Facts

Validates the EntryPressureAccumulator (running sum, Process-S discharge) + refractory floor (ree-v3 63e70d6) against the SD's own failure_record target, at V3-EXQ-933's exact injected-demand levels, 3 arms x 3 seeds:

- **C1** (sub-threshold crossing): PRESSURE_SUB (0.1/step vs threshold 0.5) first fire at step 5 = the analytic crossing (bound 8), 24 fires/life, every fire pressure-attributed. 933's NEED_SUB: 0 need-arm fires in 120 steps.
- **C2** (bounded rate): PRESSURE_HIGH (1.0/step) 60 fires / 120 steps, rate 0.5 = exactly 1/refractory_steps (bound 61), first fire 2. 933's NEED_HIGH: 120/120 chatter, no refractory.
- **C3** (OFF-arm inertness): 4 ceiling fires, first fire 25 -- the pre-fix ceiling-only numeric signature reproduced exactly (schemas differ; the identity is numeric). Structurally unfailable (OFF flag zeroes the accumulator) -- a reproduction check mirroring contract G17, same shape the cluster autopsy documented for 933's c4.
- Readiness: pressure arms wired 1.0; PRESSURE_HIGH stimulus genuinely crossed at fire time (min pressure 2.0 >= 0.5).
- **Provenance closed empirically:** the run executed the fix as uncommitted working-tree code (dirty_paths = exactly the four fix files; commit 63e70d6 landed ~2.5 min later; one unrelated, unreachable commit intervening). This autopsy re-ran the driver dry-run on today's committed substrate: per-cell numbers reproduce exactly (deterministic trigger arithmetic).

## Four-layer diagnosis

| Layer | Status |
|---|---|
| Claim alignment | n/a (claim-free; GAP-9 is a plan node -- note the claims.yaml "GAP-9" hits are the unrelated commitment_closure namespace, a grep trap) |
| Biological reference | clear -- Process S + refractory, exactly the divergence-1 fix the cluster triage demanded; MECH-286/Saper stabiliser still separate |
| Prerequisites | present |
| Implementation | complete for the within-life pressure arm; boundary path (entry_permitted -> need_crossed level detector) deliberately untouched and untested |
| Environment | adequate for consumer validation (controlled injection; ecological producer parked per GAP-5b) |
| Measurement | adequate -- C1/C2 informative (each falsified by a registered defect mode: pre-fix detector, unwired flag, absent refractory, dead accumulator); C3 reproduction-only |
| Integration | partial by scope (within-life arm only) |
| Scale | adequate |

GOV-FAILLOC-1: not applicable (PASS). Corollary: controlled-injection-only environment -- no organism-level sleep-timing conclusions from this apparatus.

## 7b / 7c

7b: 0 fires (claim-free target). 7c red team: **CONFIRMED** -- all recomputations match (C1 bound mechanics traced through the inject-before-update ordering; C2 fire schedule 2,4,...,120; committed-substrate re-run matches). One genuine coverage caveat folded in: C1's first-fire bound is one-sided, so a swallowed entry_pressure_threshold (default 0.0 -> first fire step 2) would also have passed the RULE; the recorded values (first fire exactly 5; pressure-at-fire exactly 0.5 == threshold) prove the threshold threaded, verified here. A future rerun should use a two-sided first-fire band. Marginal information over contracts G15-G19 ~ 0, consistent with the run's own GOV-REUSE-1 framing -- the manifest is the durable decisive readout.

## Adjudication (user-confirmed at the gate)

Self-route label CONFIRMED. `standard` / `non_contributory` (retained). **User decision: flip the v3_exq_933 failure_record on SD-SLEEP-ENTRY-PRESSURE to resolved** -- the entry's implementation_note_update reserved the flip for exactly this rerun. Residuals the flip does NOT close (all already owned elsewhere): boundary-path level-detector inheritance, MECH-286 re-shaping, 929a recording re-run, GAP-5b ecological producer.

## Routing

`governance-amend` -- the record flip is the only action; no new experiment or substrate work is routed (existing follow-ons keep their owners; duplicating them here would create second trackers). The sleep plan's GAP-9 follow-up row already cites this PASS; this adjudication confirms that row's basis.
