# Failure Autopsy (diagnostic adjudication): V3-EXQ-603v -- MECH-357 eligibility-trace repair validation

**Generated:** 2026-08-28T17:11:55Z | **Scope:** single | **Status:** confirmed (interactive gate 2026-08-28)
**Session:** failure-autopsy-20260828-diagbatch | **Trigger:** `experiment_purpose: "diagnostic"`, clean unflagged PASS (claim tag MECH-357), no prior autopsy coverage.
**Run:** `v3_exq_603v_mech357_eligibility_trace_repair_validation_20260827T184708Z_v3` (ree-cloud-2, clean substrate 8bfcf198, recording complete, dry-run gate clean, ~30.5h). Predecessor: V3-EXQ-603u.

## Facts

Validates substrate_queue `mech357-avoidance-efficacy-eligibility-trace-imbalance` (credit-eligibility windowing, ree-v3 93d5d98b80: freeze/no-op ticks under threat no longer decay avoidance_efficacy) against its OWN pre-registered failure_record target -- the rerun the entry's implementation_note_update explicitly reserved the resolved-flip for. "Instrument repair, NOT a claim retest" (driver's words). 2 arms x 3 seeds, config bit-for-bit 603u.

- **C1 (load-bearing):** last-10-episode window median of the LEARNED mech357_avoidance_efficacy = 0.494 / 0.924 / 0.033 on INTACT -- 3/3 seeds >= the 0.01 floor (target demanded 2/3). Pre-fix on the identical config: 6.5e-26 / 3.9e-29 / 3.6e-24. **C1R:** POSCTRL replication 3/3. **C2** (non-load-bearing peak-ratio form): 2/3 -- seed 44 at 4.2% of its run peak; the target's LITERAL "early-episode range" clause is met on all 3 (seed 44's median sits inside its episodes-0-5 range).
- Decay:credit ratios 2.3-5.9:1 (trajectory-final; were 61-131:1; the record's 86-188:1 is the same defect on a different denominator window). `mech357_n_freeze_noop` makes the mechanism legible: e.g. 29446 spurious decays removed vs 1091 genuine on seed 42.
- Readiness all met, incl. the same-statistic positive control (643 rule) that 603u cleared PRE-fix (fix-independent) and stage0 z_goal at exactly 2/3.
- **NOT single-variable** (7c correction): config is bit-for-bit, but the substrate advanced 227 commits (18 touching ree_core). The TRACE attribution stands -- the gate file was touched by exactly one commit in the range (the fix) and the freeze-noop accounting ties the recovery to it -- but cross-run BEHAVIOURAL deltas are not attributable to the fix alone.
- **Unremarked behavioural delta:** G_H survival dropped 3/3 -> 2/3 in BOTH gated arms; seed 43 -- the highest-trace seed -- collapsed to ~6-step episodes. See read-across below.

## Claim layer: MECH-357

candidate / standard / v3_pending / pending_retest_after_substrate. exp_conf 0.282, lit_conf 0.762 (plausible_unproven). live_status verdict (from 603t) now stale. Re-derive brake (R1-R3, recomputed): 0 ceiling hits. Granularity trigger: does not fire (3 unclear + 1 untested, zero weakened). This is the 7th consecutive run without a claim discrimination -- and the FIRST with a live instrument where the DV is measured.

**Direction adjudication:** the manifest's top-level `evidence_direction: "supports"` is driver-hardcoded on PASS in a script whose header says "NOT a claim retest"; the claim's confirming condition requires the INTACT-vs-LESION discrimination this run pre-declares it does not attempt; 603h precedent books mechanism-engagement as non_contributory; and the run is scoring-excluded (`diagnostic_probe`) regardless. **Adjudicated to `non_contributory` for MECH-357.**

## Four-layer diagnosis

| Layer | Status |
|---|---|
| Claim alignment | intact but untested -- instrument repaired; falsifier still unrun |
| Biological reference | clear -- decay-on-absence-of-attempt contradicted gradual acquisition (Debiec & Sullivan 2017); windowing restores eligibility-trace credit semantics |
| Prerequisites | present |
| Implementation | complete (unconditional fix; LESION arm invariant, deliberately dropped) |
| Environment | adequate for trace validation; inadequate for discrimination (lesion ceiling); not single-variable across runs (227 commits) |
| Measurement | adequate (scoring-window-scoped C1 per the 643 rule; DV symmetry declared per 604c; precondition_gate.py per-arm) |
| Integration | coupled |
| Scale | adequate |

GOV-FAILLOC-1: not applicable (PASS). Corollary: no organism-level MECH-357 conclusion licensed until the graded-DV retest runs.

## 7b / 7c

7b: 0 fires (C1-C3 evaluated on MECH-357 without firing). 7c red team: **CONTESTED** -- headline adjudications all confirmed on independent recomputation (window medians from raw trajectories; supports->non_contributory correct from both sides; failure_record clauses met verbatim; diagnostic_evidence_adjudicated confirmed absent; 603u-cluster pressure-up refusal verbatim). Two defects, disposed: (1) the "only changed variable" premise (fixed as above); (2) the routing had omitted the COMPLETED graded-DV reanalysis -- folded in below.

## Read-across, flagged for governance (NOT adjudicated here)

`mech357_h2_graded_dv_reanalysis_2026-08-25.md` refutes the 603u-cluster's declared null ("graded DVs also show INTACT ~= LESION"): in pre-fix 603s/t/u, the gated arms survive SHORTER than the ungated LESION control in 16/18 cells across three independently-designed pressure mechanisms (deficits 59-98 of 200 steps in 603u). 603v shows the same shape POST-fix (G_H 3/3 -> 2/3; highest-trace seed collapsing) -- which weighs AGAINST the reanalysis's story (a) (early cost of a mechanism extinct by scoring time), since here the trace was live through scoring. Governance owns: (i) whether 603s/t/u re-read `weakens` vs `non_contributory`; (ii) the one-line driver amendment persisting `episode_lengths` for ALL arms (ARM_LESION currently has no per-episode record -- a hard prerequisite for the graded-DV retest); (iii) `chip-20260827-mech357-trajectory-reanalysis` appears to be an open stale duplicate of the completed reanalysis.

## Adjudication (user-confirmed at the gate)

Self-route label CONFIRMED. Per-claim (MECH-357): direction `non_contributory`; category `standard` (stays); status stays candidate; note append (drafted in JSON); `diagnostic_evidence_adjudicated: true` (field absent today); pending_retest_after_substrate stays true with its first condition now MET. Substrate amend: **flip the 603u failure_record to resolved** (user-confirmed; note carries the trace-only scope and the behavioural-delta caveat).

## Routing

`queue-experiment` (once governance ratifies and adjudicates the read-across): MECH-357 retest as a NEW letter combining (a) the validated trace fix, (b) the graded scoring-window-scoped DV (proven workable by the reanalysis), (c) the episode_lengths-for-all-arms persistence amendment, (d) a restored ARM_LESION comparator. Explicitly NOT a bare pressure-up -- the 603u-cluster refusal of a 7th same-question pressure recalibration stands (the binary G_H gate saturates at the 200-step ceiling on 7/9 arm-seeds; headroom must come from the graded DV first). This autopsy spawns nothing itself.
