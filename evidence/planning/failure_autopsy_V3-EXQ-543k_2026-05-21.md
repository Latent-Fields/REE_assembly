# Failure autopsy: V3-EXQ-543k (ARC-062 GAP-B)

**Generated:** 2026-05-21T14:16:03Z  
**Status:** confirmed (user 2026-05-21)  
**Scope:** single (misrun artifact) + cluster context (543g--543j lineage)

---

## Executive summary

There is **no canonical `v3_exq_543k_*` manifest** on `origin/master` or locally. The only FAIL linked to queue slot `V3-EXQ-543k` is `_runner_signals/V3-EXQ-543k.json` pointing at `v3_exq_543i_arc062_differential_heads_falsifier_20260521T035802Z_v3.json` -- an experiment typed and queued as **543i**, without `mode_separation_floor`, `p1_w_deviation_aux_weight`, `k_identical_runs`, `basin_stable`, or `hostname`. Acceptance metrics are **byte-identical** to `V3-EXQ-543j` (cross-machine confirm, already governance non_contributory).

**User-confirmed read:** misrun / wrong experiment identity -- **non_contributory** for all tagged claims. This file does **not** test GAP-B (`mode_separation_floor` + P1 w-deviation aux + K=3 basin gate). Do **not** apply branch-e demotion from this artifact.

**If a real 543k run later FAILs with branch-e** (same collapse signature as 543i `20260518T191052Z`): that extends the existing **substrate_ceiling** cluster read from `failure_autopsy_V3-EXQ-543i_2026-05-19`, but **routing priority** is **GAP-C / GAP-D validation (`V3-EXQ-598`) before** another floor/aux letter (`543l`). Optional later: `543l` ablations isolating floor vs aux vs GAP-C/D wiring.

---

## 1. Facts reconstruction

### Target queue slot

| Field | Value |
|-------|-------|
| queue_id | V3-EXQ-543k |
| script (intended) | `v3_exq_543k_arc062_mode_separation_gap_b_falsifier.py` |
| supersedes | V3-EXQ-543i |
| purpose | evidence -- GAP-B post-543i retest |
| GAP-B substrate | `mode_separation_floor=0.25`, `p1_w_deviation_aux_weight=0.1` on gated arms; `K_IDENTICAL_RUNS=3` basin unanimity gate |

### Artifact actually on disk

| Field | Value |
|-------|-------|
| run_id | `v3_exq_543i_arc062_differential_heads_falsifier_20260521T035802Z_v3` |
| experiment_type / queue_id in manifest | **543i** (not 543k) |
| timestamp_utc | 2026-05-21T03:58:02Z |
| elapsed_seconds | ~21781 (~6 h) |
| outcome | FAIL |
| interpretation_branch | `e_collapse_survives_structure_MECH309_strong_ARC063_required` |
| governance stamp | non_contributory all claims (543j-equivalent metrics) |

### Pre-registered PASS criteria (543k script, current `origin/main`)

1. **basin_stable** -- K=3 identical reruns unanimous per gated arm (new vs 543i)  
2. **diff_primary_pass** = basin_stable AND diff_on_escape AND diff_off_reproduced_collapse AND c2c3_on_pass  
3. No per-claim direction unless basin_stable  

### What failed on the misrun artifact (543i criteria only)

| Criterion | Expected (543i branch) | Observed |
|-----------|------------------------|----------|
| diff_off_reproduced_collapse (negative-control / sanity) | true (all diff-OFF gated arms >=2/3 inert) | **true** |
| diff_on_escape (discrimination) | true (0 inert on all diff-ON arms) | **false** (3/3 inert on ARM_8..11) |
| c2c3_on_pass (discrimination) | true | **false** (c2_on_pass false, c3_on_pass false) |
| basin_stable (543k only) | not recorded | **absent** |

**Failed criterion for scientific read of metrics:** discrimination (diff-ON escape + C2/C3 routing).  
**Failed criterion for GAP-B claim:** experiment never ran -- **implementation/deployment gap** (543i manifest under 543k queue slot).

### Runner signal

```json
"queue_id": "V3-EXQ-543k",
"script": ".../v3_exq_543k_arc062_mode_separation_gap_b_falsifier.py",
"manifest_path": ".../v3_exq_543i_...20260521T035802Z_v3.json",
"outcome": "FAIL"
```

Worker executed a path labeled 543k but emitted a 543i manifest (stale script copy or wrong `EXPERIMENT_TYPE` on the host at run time).

---

## 2. Claim-layer map

| claim_id | type | status | v3_pending | Prior autopsy (543i 191052Z) |
|----------|------|--------|------------|------------------------------|
| ARC-062 | architectural_commitment | candidate | true | weakens at V3 substrate (not architectural falsification) |
| MECH-309 | mechanism_hypothesis | candidate | true | supports (narrow -- collapse-only evidence) |
| INV-074 | invariant | universal | true | non_contributory (gated policy non-functional) |
| MECH-334 | mechanism | candidate | true | non_contributory |

**Did this run test the claims under conditions where they could express?**  
**No** for GAP-B / 543k -- the floor and aux loss were not in the manifest and likely not active on the worker that produced this file.  
**Yes** for the 543i-style read only -- and that read duplicates `V3-EXQ-543j` + `543i` branch-e already covered by `failure_autopsy_V3-EXQ-543i_2026-05-19`.

**Claim tag accuracy:** tags inherited from 543i lineage are correct for the *metrics* but the *queue_id* attribution to 543k is wrong.

---

## 3. Biological-reference triage

- **Closest mechanism:** PFC rule-cells / mixed-selectivity / corticostriatal action gating (unchanged from 543i autopsy).  
- **Formal import:** no -- not a Pearl/Shannon formal-definition failure.  
- **Lit:** `targeted_review_arc_062_rule_apprehension` present (8 entries).  
- **Missing-dependency signature:** collapse with diff-OFF repro + diff-ON all inert matches **absent per-context differentiation / routing signal** (GAP-C discriminator -> LateralPFC; GAP-D trainable rule-bias head), not biology rejecting rule-gating as a class.  
- **543k floor (when actually run):** biologically motivated fix for w~0.5 canceling composed differential contrast under shared-return REINFORCE -- does not replace corticostriatal routing; user priority is validate C/D before stronger floor ablations.

---

## 4. Four-layer diagnosis

### Misrun artifact (`20260521T035802Z` under 543k slot)

| Layer | Status | Notes |
|-------|--------|-------|
| Claim alignment | unclear / non_contributory | GAP-B intervention not evidenced in manifest |
| Biological reference | present (from 543i lineage) | Not applicable to misrun identity |
| Developmental / dependency prerequisites | missing on worker | GAP-B config + 543k manifest fields absent |
| Implementation completeness | partial | Substrate on `origin/main` has floor; run did not publish 543k identity |
| Environment adequacy | adequate | diff-OFF collapse reproduced (valid 543i sanity) |
| Measurement adequacy | misleading for 543k | Wrong experiment_type; duplicates 543j |
| Integration adequacy | isolated | GAP-C/D still unwired for behavioral test |
| Scale / capacity | adequate | Full ~6 h budget |

**Recommended epistemic_category (this artifact):** `substrate_ceiling` is already stamped on the file from 543j equivalence -- governance should treat as **misrun non_contributory** (experiment-identity), not new claim pressure.

### Anticipated real 543k FAIL (if branch-e repeats)

| Layer | Status | Notes |
|-------|--------|-------|
| Claim alignment | intact for MECH-309 test; ARC-062 weak reading still cannot express | Floor may reduce w=0.5 cancellation but not supply routing signal |
| Biological reference | clear | Missing-dependency, not divergence |
| Prerequisites | missing | GAP-C/D substrate landed; **598** blocked on 543k contributory PASS |
| Implementation | partial | Floor+aux symbol present; functional role needs C/D consumer |
| Environment | adequate | |
| Measurement | adequate | Basin gate adds determinism check |
| Integration | isolated | Prioritize 598 before 543l |
| Scale | adequate | |

**Recommended epistemic_category (real 543k branch-e):** `substrate_ceiling` (extends 543i cluster).

---

## 5. Cluster pattern

| Experiment | Claim focus | Negative-control / absolute | Discrimination | Read |
|------------|-------------|----------------------------|----------------|------|
| V3-EXQ-543g | ARC-062 / MECH-309 | varies by basin | gated collapse | cross-machine bistability |
| V3-EXQ-543h | INV-074 / MECH-334 | branch c | xtal on collapsed policy | non_contributory |
| V3-EXQ-543i 191052Z | ARC-062 / MECH-309 | diff_off repro **pass** | diff_on 3/3 inert | branch **e** |
| V3-EXQ-543j | confirm 543i | same metrics as 035802Z | same | NC basin nondeterminism |
| V3-EXQ-543k slot 035802Z | (misrun 543i) | diff_off repro **pass** | diff_on 3/3 inert | **duplicate 543j**; not GAP-B |

**Structural property:** one attractor (head-collapse / inert gating) under outcome-coupled REINFORCE; structural non-equilibrium (MECH-333) and (if run) mode_separation_floor are insufficient without **context-routing consumer** (GAP-C/D).

**Readings:** substrate_enrichment (C/D first) vs test_design_ceiling -- user chose **substrate_enrichment priority: GAP-C/D before 543l floor ablations**.

---

## 6. Learning extracted

1. **Queue slot != science:** 543k runner signal + 543i manifest is a fleet/git-sync or stale-script incident -- governance must not weight branch-e from this file against ARC-062.  
2. **543j already consumed the metrics** -- no new information in 035802Z beyond confirming cloud-4 branch-e again.  
3. **GAP-B floor is necessary but likely not sufficient** -- biology and 543i autopsy point to discriminator->PFC routing (GAP-C) and trainable rule-bias head (GAP-D) as the unwired dependencies.  
4. **Retest order:** real **543k** (verify manifest identity + floor fields) -> **598** (C/D ablation) -> only then **543l** (floor/aux/C/D factorial ablations if 598 partial).

---

## 7. Repair pathway and routing (confirmed)

| Step | Action | Skill |
|------|--------|-------|
| 1 | Stamp misrun manifest + runner signal: non_contributory all claims; note `failure_autopsy_V3-EXQ-543k_2026-05-21` misrun | `/governance` |
| 2 | Ensure fleet `git pull` on `ree-v3` `main` before 543k rerun; verify manifest has `experiment_type` *543k*, `mode_separation_floor`, `basin_stable` | ops / coordinator |
| 3 | Complete re-queued **V3-EXQ-543k** (`force_rerun`, IGW-043) | runner |
| 4 | On contributory PASS -> unblock **V3-EXQ-598** (GAP-C/D 2-arm bias frozen vs trainable) | runner |
| 5 | On real 543k FAIL branch-e -> do **not** demote yet; run **598** first (C/D ablation) | `/governance` + runner |
| 6 | Defer **V3-EXQ-543l** (stronger floor/aux or C/D factorial) until 598 lands | `/queue-experiment` |

**Not routing:** governance demotion from this artifact; `/lit-pull` (lit present); `/diagnose-errors` (ran to completion).

---

## 8. Draft `evidence_quality_note` (governance to write)

**Misrun (035802Z / 543k slot):**

> V3-EXQ-543k queue slot FAIL 20260521T035802Z is a **misrun**: manifest is `v3_exq_543i_*` (no `mode_separation_floor`, no `basin_stable`, no `k_identical_runs`). Metrics match V3-EXQ-543j (branch-e, all gated arms 3/3 inert). **non_contributory** for ARC-062, MECH-309, INV-074, MECH-334 -- does not test GAP-B. failure_autopsy_V3-EXQ-543k_2026-05-21. pending_retest_after_substrate: true (real 543k + 598).

**If real 543k later FAILs branch-e (for governance after retest):**

> V3-EXQ-543k (valid manifest) FAIL branch-e: `mode_separation_floor` + P1 w-deviation aux did not escape MECH-309 monomodal collapse (diff-ON 3/3 inert; diff-OFF repro valid). Extends failure_autopsy_V3-EXQ-543i substrate_ceiling. **Do not demote ARC-062** until V3-EXQ-598 (GAP-C/D routing + trainable bias head) runs. narrow_supports_flag retained; pending_retest_after_substrate through 598 then optional 543l ablations.

---

## 9. User confirmation

- **Artifact:** misrun NC + overlap with 543i/543j branch-e (combined A+B).  
- **Priority:** GAP-C/D (`V3-EXQ-598`) before `543l` floor/aux/C/D ablations.
