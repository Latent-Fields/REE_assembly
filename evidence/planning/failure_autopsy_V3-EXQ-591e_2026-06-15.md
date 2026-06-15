# Failure Autopsy — V3-EXQ-591e

**Generated:** 2026-06-15T16:10:30Z
**Scope:** single
**Status:** confirmed (user-adjudicated 2026-06-15)
**Target:** `v3_exq_591e_isef005_phase01_gate_criterion_20260615T095228Z_v3`
**Predecessor autopsy:** `failure_autopsy_V3-EXQ-591d_2026-06-15` (which prescribed this EMA-of-level@0.2 fix and predicted it would discriminate). Lineage: 591 -> 591b -> 591c -> 591d -> **591e**. This is the **2nd** autopsy on the gate-CRITERION question specifically (the c-2 leg of GAP-14).
**Bears on:** ARC-046 / infant_substrate:GAP-14 prereq (c-2) (claim-free; no claim weighted)

---

## Verdict in one line

Genuine, non-degenerate, fairly-run **FAIL** — not a precondition_unmet / vacuous flag, not a
claim falsification. The 591d-prescribed **EMA-of-LEVEL@0.2 criterion does not discriminate**: it
**ADMITS the seed-45 false-advancer** (`ema_level.advanced @ ep137`). It fails in the **opposite
direction from 591d** (591d was over-conservative and rejected genuine explorers; 591e is
over-permissive and admits a false-advancer). Root cause: a **causal one-way-latching** gate keyed on
a **short-memory EMA (alpha=0.2, ~5-10 ep)** latches on seed-45's late transient burst, whereas the
discrimination oracle is the **retrospective full-run mean**. The mismatch is the **statistic family**,
not the floor value. **Routing (user-confirmed 2026-06-15): `/queue-experiment` 591f — persist the
full per-episode traces and run an OFFLINE multi-candidate criterion sweep** (cumulative-mean-since-ep_min,
large-window mean, EMA+dwell/hysteresis), choosing the discriminating criterion against the recorded
traces *before* it drives any gate.

---

## 1. Facts (no interpretation)

- **Manifest:** outcome FAIL, `experiment_purpose: diagnostic`, `claim_ids: []`,
  `evidence_direction: non_contributory`, label `ema_of_level_does_not_discriminate_needs_alternative`,
  `supersedes: V3-EXQ-591d`, machine `ree-cloud-3`.
- **Design:** re-runs the SAME diversity-armed Phase 0->1 reachability probe as 591d (5 seeds 42-46,
  160 ep, 200 steps/ep, grid 12; MECH-313 noise-floor + MECH-314 curiosity at landed defaults,
  SP-CEM main-path), deterministic (a reproducibility check of the 591c/591d traces). Each seed's
  per-episode h_pos is replayed OFFLINE through two Phase 0->1 criteria gated by `ep_min=100`. The
  shared `infant_curriculum.py` scheduler is NOT mutated.
  - (A) BASELINE single-episode SPIKE crossing of 0.994 — informational (the current scheduler
    behaviour + false-advancer classifier).
  - (B) **EMA-of-LEVEL** — `EMA(alpha=0.2)` of per-episode h_pos, advance on first episode `>= ep_min`
    where `EMA >= GENUINE_EXPLORATION_H_POS_MEAN_FLOOR (0.20)`. The **load-bearing** candidate.
- **Preconditions (all MET; non-degenerate):** `early_policy_produces_nontrivial_h_pos` 2.485 > 0.2;
  `genuine_explorers_present` 3 >= 2; `false_advancer_present` 1 >= 1.
  `criteria_non_degenerate.C_gate_discriminates = true`. The FAIL is a real verdict.

| seed | h_pos_mean | h_pos_max | crossings (>=0.994) | genuine | false-adv | baseline SPIKE | EMA-of-level@0.2 |
|------|-----------|-----------|---------------------|---------|-----------|----------------|------------------|
| 42 | 0.5621 | 1.8384 | 7 | yes | - | adv@104 | adv@100 (admit, correct) |
| 43 | 0.3226 | 1.3118 | 6 | yes | - | adv@114 | adv@100 (admit, correct) |
| 44 | 0.8424 | 2.4849 | 36 | yes | - | adv@100 | adv@100 (admit, correct) |
| **45** | **0.1404** | **1.4530** | **2** | **-** | **yes** | adv@142 | **adv@137 (ADMIT — WRONG; should reject)** |
| 46 | 0.0375 | 0.6899 | 0 | - | - (OOS) | reject | reject (correct) |

- **Failed criterion:** `C_gate_discriminates` (sole load-bearing) = false. Failed leg =
  **"rejects every false-advancer"** (seed-45 admitted). The **"admits every genuine explorer"** leg
  now PASSES (42/43/44 all admitted @ ep100) — the 591d over-conservatism is fixed. So the failure
  has flipped sign relative to 591d.
- Seed 46 (exploration-STRENGTH collapse) is OUT OF SCOPE by design (Q-043/667->667a thread); it
  stays in Phase 0 under every criterion as expected.

## 2. The load-bearing insight (the mechanism, read directly from the data — not predicted)

591d *predicted* (from per-seed summary stats) that EMA-of-level@0.2 would reject seed-45 because the
EMA "converges toward the per-episode MEAN level" (seed-45 mean 0.14 < 0.2). The prediction was wrong
because it reasoned about the EMA's **asymptotic value** while the gate decides on the EMA's **first
floor-crossing**:

- `_advance_ema_level` (script L296-310) is a **one-way latching** gate: it returns the first
  `ep >= ep_min` where `EMA >= floor`, and never un-latches.
- `alpha=0.2` gives the EMA an effective memory of ~5-10 episodes. Seed-45 has a **late burst**
  (`h_pos_max 1.45`, 2 supra-0.994 episodes) around ep 137. A single ~1.45 episode lifts the EMA in one
  step: `EMA' = 0.8*0.1 + 0.2*1.45 ~= 0.37`, comfortably over the 0.20 floor. The gate **latches @ ep137**.
  That the EMA then decays back below 0.2 is irrelevant — the latch has fired.
- The **discrimination oracle** is the genuine-explorer definition: **global full-run mean** `h_pos_mean
  >= 0.20` (AND `>= 2` crossings). That is a **retrospective, full-memory, offline** statistic. Seed-45's
  global mean (0.14) correctly fails it; its 2 isolated bursts are diluted across 160 episodes.

**The mismatch is structural, not parametric.** A *causal* gate must decide at episode *t* using only
episodes 0..*t*; a *retrospective* oracle sees the whole run. A short-memory EMA is dominated by a
transient that the full-run mean averages away. **No floor value fixes this** — `seed-45` would clear
*any* floor that the genuine explorers (means 0.32-0.84) also clear, on its burst. The criterion
**family** is wrong: it needs to be a **long-integration / dwell-gated** statistic so an isolated
transient cannot latch it.

## 3. Claim-layer mapping

`claim_ids: []`. ARC-046 (architectural_commitment, status candidate, confidence 0.0,
epistemic_category `substrate_ceiling`) is the bears-on target only — **no claim is weighted; none can be
promoted or demoted** by this run (architectural_commitment AND substrate_ceiling both promote/demote
suppressed). The constructive content is substrate-readiness / test-design information about the
InfantCurriculumScheduler Phase-0 exit gate, not claim truth. **ARC-046 NOT weakened.**

## 4. Biological-reference triage

- **Closest mechanism:** a developmental Phase-0 exit gate — early motor-babbling competence threshold
  gating a curriculum transition (BG/dopaminergic developmental-milestone gating).
- **Faithful translation or formal import?** Faithful, and the biology *sharpens the fix*. Developmental
  competence transitions advance on **sustained** competence with **hysteresis** — not a single good
  episode. The biologically-faithful form is therefore a **dwell-gated / long-integration** statistic
  (you do not advance a developmental stage on one transient spike). This is exactly the property the
  short-memory latching EMA lacks. Not a formal-definition import -> **no `/lit-pull` commission**.
- **Missing-dependency signature?** No. Both classes (3 genuine explorers + 1 false-advancer) are present
  and the oracle fires; the gap is purely how the candidate criterion reads them online.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | not applicable (claim-free) | ARC-046 not weighted/movable; substrate-readiness gate diagnostic |
| Biological reference | clear | competence gates advance on sustained competence with hysteresis; dwell/long-integration is the faithful form |
| Prerequisites / dependency | present | diversity stack armed (landed defaults); 3 genuine explorers + 1 false-advancer present |
| Implementation completeness | partial | candidate carries the SYMBOL (smoothed level) but the WRONG statistic family (short-memory causal latch vs retrospective full-memory oracle) |
| Environment adequacy | adequate | 5-seed reachability probe produced both genuine explorers and a false-advancer |
| Measurement adequacy | under-instrumented / misleading | (a) EMA latches on a transient the oracle averages away; (b) the full per-episode traces are computed (script L272) then DISCARDED, so no candidate can be verified offline |
| Integration adequacy | not applicable | offline replay over one substrate |
| Scale / capacity | adequate | full 160-ep budget; seed-44 (mean 0.84) proves a discriminating regime exists |

**Recommended epistemic_category:** `not_applicable_claim_free_diagnostic`.
**Recommended evidence_direction:** `non_contributory` (unchanged — claim-free substrate-readiness diagnostic).

## 6. Recurrence checks

### 6a. Granularity-debt / `/claim-synthesis` — does NOT fire
This is the 2nd autopsy on the gate-criterion `bears_on` target (591d, 591e) **with opposite failure
signatures** (591d over-conservative; 591e over-permissive), which is the textbook granularity-debt
*shape*. But `/claim-synthesis` operates on `claims.yaml` claims, and this target is **claim-free**:
ARC-046 is `architectural_commitment` + `substrate_ceiling` (promote/demote suppressed, unweighted).
There is no coarse claim to decompose into testable children — the recurrence is **criterion-design
iteration on an offline diagnostic**, not claim granularity debt. `/claim-synthesis` is **not** routed.

### 6b. Process recurrence — the real lesson
Two consecutive single-candidate criterion guesses (591d: K-of-N / EMA-vs-0.994; 591e: EMA-of-level@0.2),
both derived by **predicting a causal latching gate's behaviour from global summary statistics**, both
wrong — and each cost a full fleet run because the per-episode traces are discarded. The fix is
**process-level**, and it is what 591f encodes: persist the traces and convert criterion selection into a
**pure offline sweep** verifiable before any candidate drives the gate.

## 7. Learning extracted

1. A **causal one-way-latching** gate keyed on a **short-memory EMA (alpha=0.2)** is gamed by an isolated
   transient: one ~1.45 episode latches the gate over the 0.20 floor regardless of the long-run mean
   (seed-45 admitted @ ep137 despite global mean 0.14). The discrimination oracle is the **retrospective
   full-run mean** — a full-memory offline statistic. The mismatch is the **statistic family**, not the
   floor; **no floor value fixes it**.
2. The failure **flipped sign** from 591d (over-conservative -> over-permissive), which confirms the
   genuine-explorer-vs-false-advancer boundary is real and narrow: 42/43/44 (means 0.32-0.84) vs 45
   (0.14). The right criterion is a **long-integration / dwell-gated** statistic that admits the former and
   rejects the latter's transient.
3. **Biology sharpens the fix:** developmental competence gates advance on sustained competence with
   hysteresis — a dwell-time / cumulative-mean form is the faithful translation, not a recency-weighted
   spike-sensitive EMA.
4. **Stop predicting causal-gate behaviour from summary stats.** 591e computes the full per-episode
   `h_pos_sequence` (script L272) but discards it. 591f must **persist the traces** and select the
   criterion by an **offline multi-candidate sweep** against them — converging in one run instead of one
   guess per fleet run.

## 8. Repair pathway (user-confirmed 2026-06-15)

- **`/queue-experiment` -> V3-EXQ-591f** (alphabetic suffix; same scientific question — which causal
  criterion replaces the single-episode Phase 0->1 gate — with a corrected *statistic family* and a
  trace-persisting, offline-verifiable design; `supersedes: V3-EXQ-591e`). Design:
  1. **Persist** the full per-episode `h_pos_sequence` for every seed in the manifest (the input the
     591e run discarded), so criterion selection is reproducible offline with zero further fleet runs.
  2. **Sweep** multiple causal criterion *families* OFFLINE against the recorded traces, all gated by
     `ep_min=100` and evaluated as latching gates exactly as production would run them:
     - **cumulative-mean-since-ep_min @ ~0.20** (full memory: a late isolated burst is diluted);
     - **large-window rolling mean @ ~0.20** (window long enough that 2 spikes cannot lift it);
     - **EMA + dwell/hysteresis** (require the EMA to hold `>= floor` for K consecutive episodes —
       the biologically-faithful sustained-competence form);
     optionally a **small-alpha EMA** (longer effective memory) as a continuity check with 591e.
  3. Keep the SAME non-vacuity preconditions and the SAME two-leg `C_gate_discriminates` acceptance
     (rejects every false-advancer AND admits every genuine explorer). **PASS** = the winning criterion
     routes to `/implement-substrate` on `infant_curriculum.py:_try_phase_0_to_1`. If **no** candidate in
     the sweep discriminates, the result is genuine substrate/oracle pressure (re-open the oracle
     definition), not another re-parameterization.
  4. The orthogonal seed-46 exploration-STRENGTH collapse (Q-043/667->667a) stays OUT OF SCOPE.
- **No `/lit-pull`** (biology already aligns with the sustained-competence / dwell form).
- **No substrate-ceiling / no `pending_retest_after_substrate`** — this is a test-design fix on the
  offline criterion, not a substrate gap. `recommended_substrate_queue_entry.action = none`.
- EXQ-ISEF-005 (the full curriculum-vs-flat, V3-EXQ-591 successor) stays blocked until BOTH GAP-14 legs
  resolve: (c-2) gate-criterion [this -> 591f] AND (c-1) seed-46 exploration-strength [Q-043/667 -> 667a].

### Draft evidence_quality_note for governance (claim-free; recorded on the 591e manifest)

> V3-EXQ-591e (claim-free ARC-046 / infant_substrate:GAP-14 c-2 Phase 0->1 gate-CRITERION diagnostic;
> diversity stack armed at landed defaults; scheduler not mutated; supersedes 591d). FAIL,
> non_contributory, genuine non-degenerate (all 3 preconditions met, criteria_non_degenerate true). The
> 591d-prescribed EMA-of-LEVEL@0.2 candidate does NOT discriminate: it ADMITS the seed-45 false-advancer
> (ema_level advanced @ ep137) while correctly admitting genuine explorers 42/43/44 — failing in the
> OPPOSITE direction from 591d (over-permissive, not over-conservative). Root cause: a causal one-way
> latching gate keyed on a short-memory EMA (alpha=0.2) latches on seed-45's late transient burst
> (h_pos_max 1.45, 2 supra-threshold episodes) over the 0.20 floor, whereas the discrimination oracle is
> the retrospective full-run mean (seed-45 global mean 0.14 < 0.20). The mismatch is the statistic FAMILY
> (causal short-memory latch vs retrospective full-memory oracle), not the floor value — no floor fixes
> it. Measurement / test-design gap, NOT a substrate ceiling and NOT a claim falsification (claim-free;
> ARC-046 NOT weakened). Pre-registered next: V3-EXQ-591f persists the full per-episode traces and runs an
> OFFLINE multi-candidate criterion sweep (cumulative-mean-since-ep_min / large-window mean / EMA+dwell)
> verifiable before any candidate drives the gate (supersedes 591e for the gate-criterion question).

## 9. Routing

`routing: queue-experiment` (V3-EXQ-591f; persist traces + offline multi-candidate criterion sweep;
supersedes 591e). `recommended_substrate_queue_entry.action: none`. No claim demotion, no lit-pull, no
substrate enrichment, no `/claim-synthesis`. Governance records the non_contributory +
evidence_quality_note on the 591e manifest; this skill produced the diagnosis only.
