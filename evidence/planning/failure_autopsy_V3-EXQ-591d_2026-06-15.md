# Failure Autopsy — V3-EXQ-591d

**Generated:** 2026-06-15T04:18:17Z
**Scope:** single
**Status:** confirmed (user-adjudicated)
**Target:** `v3_exq_591d_isef005_phase01_gate_robustness_20260614T232048Z_v3`
**Predecessor autopsy:** `failure_autopsy_V3-EXQ-591c_2026-06-11` (which flagged the seed-45 gate-permissiveness as an ARC-046 follow-on; 591d is the first dedicated test of it)
**Bears on:** ARC-046 / infant_substrate:GAP-14 (claim-free; no claim weighted)

---

## Verdict in one line

Genuine, non-degenerate, fairly-run FAIL — **not** a precondition_unmet/vacuous flag, **not** a
claim falsification. Neither candidate robust criterion (K-of-N, EMA) discriminates because BOTH
reuse the single-episode spike threshold (0.994) as the bar for a *sustained* statistic, so they
reject true-but-sparsely-spiking explorers (seeds 42/43) along with the false-advancer (seed 45).
The discriminating signal is the **mean h_pos level** (the oracle's own statistic, floor ~0.2),
not threshold-crossing density. **Routing: `/queue-experiment` 591e — EMA-of-LEVEL gated at the
~0.2 genuine-explorer floor** (user-confirmed 2026-06-15).

---

## 1. Facts (no interpretation)

- **Manifest:** outcome FAIL, `experiment_purpose: diagnostic`, `claim_ids: []`,
  `evidence_direction: non_contributory`, label `no_candidate_criterion_discriminates_needs_alternative`.
- **Design:** re-runs the V3-EXQ-591c diversity-armed Phase 0->1 reachability probe (5 seeds 42-46,
  160 ep, 200 steps/ep, grid 12; MECH-313 noise-floor + MECH-314 curiosity at landed defaults,
  SP-CEM main-path), records the full per-episode h_pos sequence per seed, and replays each OFFLINE
  through three Phase 0->1 criteria. The shared `infant_curriculum.py` scheduler is NOT mutated.
  Threshold = `H_POS_FRAC_OF_MAX * ln(144) = 0.20 * ln(144) ~= 0.994` (the 2026-05-31 recalibration);
  ep_min = `PHASE_EP_MIN[1] = 100`.
  - (A) BASELINE single-episode crossing (current scheduler behaviour).
  - (B) K-of-N: K=5 of last N=10 episodes cleared the threshold.
  - (C) EMA: EMA(alpha=0.2) of per-episode h_pos stays above the threshold.
- **Preconditions (all MET; non-degenerate):** `early_policy_produces_nontrivial_h_pos` measured
  2.485 > 0.2 floor; `genuine_explorers_present` 3 >= 2; `false_advancer_present` 1 >= 1.
  `criteria_non_degenerate.C_gate_discriminates = true`. The FAIL is a real verdict.

| seed | h_pos_mean | h_pos_max | n_eligible >= thr | genuine | false-adv | baseline | K-of-N | EMA |
|------|-----------|-----------|-------------------|---------|-----------|----------|--------|-----|
| 42 | 0.5621 | 1.8384 | 7 | yes | - | adv@104 | **reject** | **reject** |
| 43 | 0.3226 | 1.3118 | 6 | yes | - | adv@114 | **reject** | **reject** |
| 44 | 0.8424 | 2.4849 | 36 | yes | - | adv@100 | adv@105 | adv@104 |
| 45 | 0.1404 | 1.4530 | 2 | - | **yes** | adv@142 | reject | reject |
| 46 | 0.0375 | 0.6899 | 0 | - | - (OOS) | reject | reject | reject |

- **Failed criterion:** `C_gate_discriminates` (the sole load-bearing criterion) = false. Failed
  leg = **"admits every genuine explorer"** (42 and 43 rejected; only 44 admitted). The
  **"rejects every false-advancer"** leg PASSES for both K-of-N and EMA (seed-45 correctly rejected).
- Seed 46 (exploration-STRENGTH collapse) is OUT OF SCOPE by design (the orthogonal Q-043/667 thread);
  it stays in Phase 0 under every criterion as expected.

## 2. The load-bearing insight (which leg failed and why)

Robustification did exactly half its job: both candidates **reject the seed-45 false-advancer** —
the 591c single-episode over-permissiveness defect IS killed. The whole failure is on the
**over-conservatism** side: the candidates also reject genuine explorers 42 and 43.

The discriminating signal between genuine explorers and the false-advancer lives in the
**mean h_pos LEVEL** (genuine 0.32-0.84 vs false-advancer 0.14) — which is exactly the
genuine-explorer **oracle's own statistic** (`h_pos_mean >= 0.20`). But both candidate criteria
key on the **single-episode spike threshold (0.994)**, which the genuine explorers' typical level
sits far below:

- **K-of-N (5-of-10 supra-0.994):** requires dense supra-threshold clustering. Only seed 44
  (36 dense crossings of 160) ever has 5-in-10. Seeds 42/43 spike only 6-7 times across 160
  episodes — genuinely exploring (high mean), but too sparse to cluster 5-in-10.
- **EMA-of-level vs 0.994:** the EMA converges toward the mean (0.32-0.84), all BELOW 0.994.
  Only seed 44 (mean 0.84, max 2.48) has enough high episodes to transiently push the EMA over.

So the candidate criteria are **mis-parameterized**: a *sustained / aggregated* statistic needs a
*sustained-appropriate floor* (~0.2, the genuine-explorer mean floor), NOT the single-episode spike
bar (0.994). The criterion **FAMILY** (smoothed/sustained level) is sound; the candidate
**INSTANCES** reused the wrong threshold. The fix is a re-parameterization, not a new mechanism.

## 3. Claim-layer mapping

`claim_ids: []`. ARC-046 (architectural_commitment, status candidate, confidence 0.0,
epistemic_category `substrate_ceiling`) is the bears-on target only. **No claim is weighted; none can
be promoted or demoted** by this run (architectural_commitment AND substrate_ceiling are both
promote/demote-suppressed). The constructive content is substrate-readiness / test-design
information about the InfantCurriculumScheduler Phase-0 exit gate, not claim truth. ARC-046 NOT
weakened.

## 4. Biological-reference triage

- **Closest mechanism:** a developmental Phase-0 exit gate — early motor-babbling competence
  threshold gating a curriculum transition (BG/dopaminergic developmental milestone gating).
- **Faithful translation or formal import?** Faithful. Competence-graded developmental transitions
  integrate evidence over a window with hysteresis — a *sustained level*, not a single supra-threshold
  spike. The diagnosis therefore **aligns with biology**: the sustained-mean criterion at a moderate
  floor IS the biologically-faithful form; the single-episode spike threshold the candidates inherited
  as their bar is the impoverished translation.
- **Missing-dependency signature?** No. The genuine explorers ARE present and the oracle fires; the
  gap is purely in how the candidate criteria read them. Not a formal-definition import -> **no
  `/lit-pull` commission required.**

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | not applicable (claim-free) | ARC-046 not weighted/movable; substrate-readiness gate diagnostic |
| Biological reference | clear | competence gates integrate over a window; sustained-mean is the faithful form |
| Prerequisites / dependency | present | diversity stack armed (landed defaults); 3 genuine explorers + 1 false-advancer present |
| Implementation completeness | partial | candidates carry the SYMBOL (robust aggregation) but reuse the WRONG threshold (single-episode 0.994 vs sustained ~0.2) |
| Environment adequacy | adequate | 5-seed reachability probe produced both genuine explorers and a false-advancer |
| Measurement adequacy | under-instrumented / misleading | criteria binarize at 0.994 and discard the mean-LEVEL signal that separates the classes |
| Integration adequacy | not applicable | offline replay over one substrate |
| Scale / capacity | adequate | full 160-ep budget; seed-44 proves a discriminating regime exists |

**Recommended epistemic_category:** `not_applicable_claim_free_diagnostic`.
**Recommended evidence_direction:** `non_contributory` (unchanged — claim-free substrate-readiness diagnostic).

## 6. Granularity-debt recurrence check

591 / 591b / 591c / 591d is the 4th autopsy in the 591 lineage. These are a **developmental chain on
distinct defects**, NOT one claim circling with multiple distinct failure signatures:
- 591 (2026-05-27): canonical cluster autopsy; reachability + prereq enumeration; routed
  scaffolded_sd054 + the H_POS_FRAC_OF_MAX 0.70->0.20 recalibration.
- 591b (2026-06-10) / 591c (2026-06-11): reachability under the diversity stack; seed-46
  exploration-STRENGTH collapse (Q-043/667 thread) + first flag of seed-45 gate-permissiveness.
- **591d (this): first dedicated autopsy on the ARC-046 gate-criterion question (seed-45 leg).**

No prior `failure_autopsy_*` targets the ARC-046 gate-criterion. This is the FIRST autopsy on that
target, not a recurrence -> **no `/claim-synthesis` recommendation fires.**

## 7. Learning extracted

1. The genuine-explorer vs false-advancer discrimination is carried by the **mean h_pos LEVEL**
   (oracle floor 0.2), NOT by single-episode threshold-crossing density. Both candidate robust
   criteria keyed on the 0.994 single-episode spike threshold, so they reject true-but-sparse-spiking
   explorers (42/43) along with the false-advancer (45).
2. Robustification killed the seed-45 over-permissiveness 591c flagged (the "rejects false-advancer"
   leg PASSES for both K-of-N and EMA). The failure is entirely over-CONSERVATISM from the wrong
   threshold — a positive signal that the robust-criterion idea works; only its parameterization is off.
3. A discriminating criterion **exists in the data**: EMA (or windowed-mean) of h_pos gated at the
   ~0.2 genuine-explorer floor cleanly separates {0.32, 0.56, 0.84} from {0.14}. The fix is a
   re-parameterized criterion, not a new mechanism or a substrate enrichment.

## 8. Repair pathway (user-confirmed 2026-06-15)

- **`/queue-experiment` -> V3-EXQ-591e** (alphabetic suffix; same scientific question — which robust
  criterion replaces the single-episode Phase 0->1 gate — with corrected parameterization;
  `supersedes: V3-EXQ-591d` for the gate-criterion question). Replay the SAME 5-seed h_pos traces
  through an **EMA-of-LEVEL criterion (alpha ~0.2) compared against the genuine-explorer floor
  (~0.20 = `GENUINE_EXPLORATION_H_POS_MEAN_FLOOR`), NOT the single-episode spike threshold (0.994)**.
  Keep the same non-vacuity preconditions and the same C_gate_discriminates two-leg acceptance.
  Expected (from the 591d per-seed levels): EMA-of-level@0.2 admits 42/43/44 (means 0.32-0.84 > 0.2)
  and rejects 45 (0.14 < 0.2) -> discriminates -> routes the criterion to `/implement-substrate` on
  `infant_curriculum.py:_try_phase_0_to_1`.
  User chose EMA-of-level over windowed-mean / a multi-criterion sweep (AskUserQuestion 2026-06-15).
- **No `/lit-pull`** (biology already aligns with the sustained-mean form).
- **No substrate-ceiling / no `pending_retest_after_substrate`** added — this is a test-design fix on
  the offline criterion, not a substrate gap. The `recommended_substrate_queue_entry.action` is `none`.
- EXQ-ISEF-005 (the full curriculum-vs-flat) stays blocked until BOTH gate legs of GAP-14 resolve:
  (c-2) gate-criterion [this -> 591e] AND (c-1) seed-46 exploration-strength [Q-043/667 -> 667a].

### Draft evidence_quality_note for governance (claim-free; recorded on the 591d manifest)

> V3-EXQ-591d (claim-free ARC-046 / infant_substrate:GAP-14 Phase 0->1 gate-robustness diagnostic;
> diversity stack armed at landed defaults; scheduler not mutated). FAIL, non_contributory, genuine
> non-degenerate (all 3 preconditions met, criteria_non_degenerate true). Neither candidate robust
> criterion discriminates: K-of-N (5/10) and EMA (alpha 0.2) both REJECT the seed-45 false-advancer
> (the 591c over-permissiveness leg is fixed) AND reject genuine explorers 42/43 — because both reuse
> the single-episode spike threshold (0.994) as the bar for a sustained statistic, while the genuine
> explorers' mean level (0.32-0.84) sits below it (they spike supra-0.994 only 6-7x of 160). The
> discriminating signal is the mean h_pos LEVEL (the oracle's own floor ~0.20), not crossing density.
> Measurement / test-design gap, NOT a substrate ceiling and NOT a claim falsification (claim-free;
> ARC-046 NOT weakened). Pre-registered next: V3-EXQ-591e re-parameterizes the replay criterion to
> EMA-of-LEVEL gated at ~0.20 (supersedes 591d for the gate-criterion question).

## 9. Routing

`routing: queue-experiment` (V3-EXQ-591e, EMA-of-level @ ~0.2 floor; supersedes 591d).
`recommended_substrate_queue_entry.action: none`. No claim demotion, no lit-pull, no substrate enrichment.
Governance records the non_contributory + evidence_quality_note on the 591d manifest; this skill
produced the diagnosis only.
