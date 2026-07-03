# Failure Autopsy -- V3-EXQ-709 (ARC-108 x ARC-110 learned/DA-gated cross-loop arbitration validation)

- **generated_utc:** 2026-07-03T13:30:39Z
- **run_id:** v3_exq_709_learned_cross_loop_arbitration_validation_20260702T052508Z_v3
- **queue_id:** V3-EXQ-709
- **claim_ids:** MECH-439, ARC-108, ARC-110
- **experiment_purpose:** evidence
- **scope:** single
- **status:** confirmed (user-approved routing 2026-07-03)
- **outcome:** FAIL / non_degenerate=False / evidence_direction=`non_contributory` (all three claims; NEVER a weakens)
- **self-route:** `substrate_not_ready_requeue`
- **machine:** ree-cloud-1

---

## 1. Scope

V3-EXQ-709 is the SEPARATE new-EXQ falsifier that `failure_autopsy_V3-EXQ-707b_2026-06-29` routing **item 3** named: "the natural next test is A1_LOOPS coupled with dopamine-gated cross-loop arbitration -- a redesign testing a DIFFERENT mechanism (new EXQ number, different claim_ids), gated on that arbitration-plasticity substrate being built." That substrate landed 2026-07-01 (ree-v3 main `832afd1`, learned `W_cross = I + M_cross`), and 709 tests it. Single-experiment autopsy (not a cluster) -- though it is the latest node in the long F-dominance conversion-ceiling lineage.

## 2. Facts reconstruction (no interpretation)

Two arms on the GAP-A reef-bipartite foraging substrate, seeds 42-47, matched envelope (finer gating + learned settling + named-channel routing + limbic input modules + ARC-109 D1/D2 + MECH-452 loop-local traces ON on BOTH arms). The **only** swept factor is `use_learned_cross_loop_arbitration`:

- `A1_LOOPS_STATIC` -- the 707b static-arithmetic control (`final = m_a*motor_z + g_a*assoc_z + g_l*limbic_z`, fixed gains).
- `A1_LOOPS_LEARNED` -- learned `eff = (I + M_cross) @ [motor_z; assoc_z; limbic_z]`, M_cross updated by the ARC-108 signed-RPE three-factor rule (shared dopaminergic delta_t / V-hat / D1-D2 asym; outer-product Hebbian coactivation at the committed candidate). At init M_cross==0 -> W_cross==I -> the arms are bit-identical; they diverge only as M_cross learns.

**Readiness gates -- 6 of 7 met (the mechanism ENGAGED):**

| Gate | measured | threshold | met |
|---|---|---|---|
| enough_divergent_seeds | 4 | 3 | yes |
| loops_carry_live_cross_loop_variance | 1.0 | 1.0 | yes |
| named_channel_routing_live (limbic routed per-candidate range) | **1.414** | 0.001 | yes |
| learned_cross_loop_weights_moved_off_init (M_cross range) | **0.116** | 1e-6 | yes |
| **limbic_loop_can_win** (n divergent seeds where w_eff[limbic] >= w_eff[motor]) | **1.0** | **2.0** | **NO** |
| learning_engaged (w_chan_finer moved + delta_t non-flat) | 0.00144 | 1e-4 | yes |
| candidate_pool_divergent | (GAP-A) | -- | yes |

**The one unmet gate.** On the four GAP-A-divergent seeds (42, 44, 46, 47), the limbic loop reached/exceeded the motor loop's effective column weight on only **1 of 4** (seed 47: 1795 P2 ticks limbic>=motor). Seed 45 also had `limbic_can_win=True` but is NOT GAP-A divergent, so it does not count toward the conversion question. Per-seed effective weights: `w_limbic_eff` peaked ~1.03-1.15 against `w_motor_eff` ~1.03-1.22; the plastic ascending-spiral coupling `M_cross[motor,limbic]` (`clg_limbic_to_motor_peak`) peaked at only **~0.003-0.031** across seeds. The load-bearing criterion `C1_learned_strict_above_static` = FALSE (1/4 seeds); committed-class entropy LEARNED 0.877 ~ STATIC 0.887.

**Which criterion failed:** a **readiness / mechanism-non-vacuity precondition** (`limbic_loop_can_win`), NOT the C1 discrimination criterion on its merits. Because the precondition is unmet, the C1 "no-lift" is vacuous: the limbic loop never got the chance to win, so a no-lift does not test whether learned arbitration CAN convert.

## 3. Claim-layer mapping

| Claim | type | status | phase | epistemic | pending_retest |
|---|---|---|---|---|---|
| MECH-439 | mechanism_hypothesis | candidate | v3 | substrate_ceiling | true |
| ARC-108 | architectural_commitment | candidate | v3 | substrate_conditional | true |
| ARC-110 | architectural_commitment | candidate | v3 | substrate_conditional | true |

**Did the test let the claims express themselves? NO.** The pre-registered grid makes the mechanism-non-vacuity preconditions gate the C1 evaluation precisely so that an inert limbic loop cannot be mistaken for "the ceiling is intrinsic." With `limbic_loop_can_win` unmet on the divergent seeds, the ARC-108 x ARC-110 learned-arbitration conversion question was **not measured**. Therefore:
- **MECH-439** is NOT supported (ceiling is NOT shown intrinsic -- the learned route never got a fair shot).
- **ARC-108 / ARC-110** are NOT weakened (the learned-arbitration coupling was present and learning, but structurally too weak to let a non-motor loop win).

The `claim_ids` tags are accurate and were re-evaluated for this specific mechanism (they are the ARC-108 x ARC-110 intersection the 707b narrowing named; not blindly inherited).

## 4. Biological-reference triage (the core move)

- **Closest mammalian mechanism:** the basal-ganglia **striato-nigro-striatal ascending spiral** (Haber 2000). Limbic/motivational cortico-BG-thalamic loops influence motor loops via progressively dorsal dopaminergic "spirals," and that ascending influence is strengthened by DA-gated plasticity over extended learning. `M_cross[motor,limbic]` + the ARC-108 signed-RPE three-factor update is a **faithful biological translation** of that spiral, NOT a formal-definition import (no Pearl/Shannon/optimal-control symbol here). Lit grounding: `docs/architecture/learned_cross_loop_arbitration.md` ARC-106 ladder -- **partial** (grounding ladder present; no dedicated targeted_review of ascending-spiral gain/maturation dynamics).
- **Divergence (load-bearing).** In real brains a limbic loop overrides a motor habit only when (a) the ascending spiral is *strong / developmentally matured*, and (b) the motor loop is not a pinned high-weight default -- habits form and dissolve. In the REE substrate w_motor is effectively pinned by F-dominance, and the learned coupling is bounded small (eta=0.01, ~2500-6500 updates, motor<-limbic column peak ~0.03). The mechanism has the **symbol** of the spiral but not enough of its **functional strength**.
- **Does the failure match a missing-dependency signature? YES.** "Non-motor loop cannot reach motor effective weight" is exactly what an under-developed / too-weak ascending spiral would produce. So the FAIL is a **discovered prerequisite** (the arbitration coupling must be strong / matured enough for a non-motor loop to win), not a falsification -- and mild positive evidence that the *ascending-spiral strength itself* is the load-bearing dependency.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact / not-tested | limbic couldn't win on divergent seeds -> C1 vacuous; no claim weakened |
| Biological reference | clear / partial | BG striato-nigro-striatal ascending spiral (Haber 2000); symbol faithful, functional strength insufficient; lit partial |
| Prerequisites | present-but-insufficient | learned arbitration substrate landed (832afd1); M_cross moves, but the coupling magnitude/training depth to let a non-motor loop win is missing |
| Implementation | partial | symbol of mechanism present (learned M_cross), functional role (limbic CAN win) unmet at current eta/training/normalization |
| Environment | partial (too sparse) | GAP-A divergent seeds few (4/6); on divergent seeds the motor F-dominance is strong; env may not present sustained motivational pressure to drive the spiral |
| Measurement | adequate (a WIN) | the `limbic_loop_can_win` sub-gate correctly caught the vacuity a naive C1 read would have mislabelled "ceiling intrinsic" |
| Integration | partially coupled but too weak | loops live + arbitration learns, but cross-loop coupling too weak to flip the arbitration winner |
| Scale / capacity | likely insufficient | eta=0.01, ~100 P2 episodes; aggregate M_cross range peaked 0.116 but the motor<-limbic column peaked only ~0.03 |

**Dominant diagnosis -> epistemic_category `substrate_ceiling`** (a loop-effective-weight ceiling in the cross-loop arbitration layer), **evidence_direction `non_contributory`** (never a weakens), paired with `pending_retest_after_substrate: true` on all three claims.

## 6. Re-derive brake (MOVE-3) -- FIRES

Prior `substrate_ceiling` / `non_contributory` autopsies tagging each claim:
- **MECH-439: 7** (700d-708-single-arena-ceiling, 689, 689a, 700-cluster, 700b, 700c, f-dominance-conversion-cluster)
- **ARC-108: 5** (700d-708-single-arena-ceiling, 460l, 700-cluster, 700b, 700c)
- **ARC-110: 0**

Including this reading, MECH-439 (8th) and ARC-108 (6th) are far past `RE_DERIVE_BRAKE_THRESHOLD` (2). The brake **fires**:
- Routing MUST be `implement-substrate` on the named upstream substrate.
- The autopsy **REFUSES a same-claim test re-queue**: do NOT queue another lettered/new-EXQ MECH-439 conversion falsifier against the *current* arbitration substrate -- that is the loop the brake exists to stop. A redesign testing a DIFFERENT mechanism (new EXQ number, different claim_ids), or a commitment-free read, remains allowed; another test circling the same loop-effective-weight ceiling on the same substrate is not.

**Granularity-debt hook: already consumed.** 707b routing item 2 fired the contingent MECH-439 `/claim-synthesis` on 2026-06-29 (DROP-MECH-453 decision -- the ARC-108 x ARC-110 intersection is a coupling, not a new child claim). No new synthesis is owed by this autopsy.

## 7. Learning extracted

1. **A NEW, deeper sub-gate beyond the 707b static-arithmetic diagnosis:** even a LEARNED [3,3] cross-loop matrix updated by the ARC-108 three-factor rule (eta=0.01, ~100 P2 episodes) lifts the limbic loop to motor effective weight on only 1/4 divergent seeds. 707b said "the combine can't learn -> build learned arbitration"; 709 shows the arbitration DOES learn (M_cross moved 0.116) yet the ascending coupling is too weak to overturn the motor(F)-loop effective-weight dominance.
2. **The ceiling is a loop-effective-weight property, not a combine-arithmetic property.** The load-bearing constraint is now "can a non-motor loop reach motor effective weight on the seeds that matter," measured directly by `clg_w_limbic_eff` vs `clg_w_motor_eff` and `clg_limbic_to_motor_peak`.
3. **Biological dependency sharpened:** the ascending-spiral *gain / maturation* is the load-bearing dependency, not merely the existence of a learnable coupling. A working substrate needs a stronger / longer-trained / structurally-boosted ascending path (or a de-pinning of the motor loop's default weight).
4. **Measurement win:** the `limbic_loop_can_win` non-vacuity gate is the correct guard -- it kept a vacuous "no-lift" from being mislabelled MECH-439-intrinsic. Keep it in any successor.

## 8. Repair pathway (routing = implement-substrate; AMEND v4_loop_segregation)

Only `v4_loop_segregation` lists all three claim_ids (MECH-439, ARC-108, ARC-110) in `unblocks_claims`; `f_dominance_conversion_ceiling` lists MECH-439 only. Both currently have empty `failure_records`. **AMEND `v4_loop_segregation`** with a failure_record for the limbic-effective-weight sub-gate:

- **metric:** on the LEARNED arm, the limbic loop reached >= motor effective weight on only 1/4 GAP-A-divergent seeds (25%); w_limbic_eff peak ~1.03-1.15 vs w_motor_eff ~1.03-1.22; plastic motor<-limbic coupling `M_cross[motor,limbic]` peaked ~0.03.
- **target:** a working impl must let a non-motor loop reach/exceed motor effective weight on a strict-majority (>=3/4) of divergent seeds so C1 (learned strict-above static) can be validly evaluated.
- **implementation hint:** strengthen / mature the ascending-spiral coupling so a non-motor loop CAN win the cross-loop arbitration on divergent seeds -- e.g. a larger / annealed learned_cross_loop_eta, longer P2 adaptation, an explicit ascending-spiral gain term on M_cross[motor,limbic], or a structural change to loop-weight normalization that de-pins the motor(F) loop's default effective weight. Then retest via a redesign (NOT a same-claim re-queue against the current substrate).

Governance applies the AMEND at its Step 6a sweep; the workset generator then surfaces the strengthened-arbitration build as an actionable `Implement substrate` item and links the retest IGW `blocked_by` to it.

## 9. Draft evidence_quality_note (for governance to write; NOT written here)

> V3-EXQ-709 (2026-07-02, ARC-108 x ARC-110 learned/DA-gated cross-loop arbitration validation; the separate new-EXQ falsifier 707b routing item 3 named; claim_ids [MECH-439, ARC-108, ARC-110]) FAIL / **non_contributory** / non_degenerate=False / self-route substrate_not_ready_requeue. The learned mechanism ENGAGED -- 6/7 readiness gates met: M_cross MOVED off init (range 0.116, not bit-identical to STATIC), limbic routing live (1.414), loops live, learning engaged. The ONE unmet gate is the deeper mechanism-non-vacuity sub-gate `limbic_loop_can_win`: on the 4 GAP-A-divergent seeds the limbic loop reached >= motor effective weight on only 1/4 (w_limbic_eff ~1.03-1.15 vs w_motor_eff ~1.03-1.22; plastic motor<-limbic coupling peak ~0.03), so C1 (learned strict-above static) could not be validly evaluated. NEVER a weakens: the ARC-108 x ARC-110 conversion question was NOT measured, so MECH-439 is NOT shown intrinsic and ARC-108/ARC-110 are NOT weakened. NEW substrate datum beyond 707b's static-arithmetic ceiling: even a LEARNED [3,3] cross-loop matrix at eta=0.01 over 100 P2 episodes cannot lift a non-motor loop to motor effective weight on the seeds that matter -- a loop-effective-weight ceiling in the cross-loop arbitration layer. Biology: the BG striato-nigro-striatal ascending spiral (Haber 2000) is faithfully translated in symbol but functionally too weak/underdeveloped; the failure matches an under-developed-spiral missing-dependency signature (a discovered prerequisite, not a falsification). Re-derive brake FIRES (MECH-439 x7, ARC-108 x5 prior substrate_ceiling/non_contributory autopsies) -> routed implement-substrate; a same-claim test re-queue against the current arbitration substrate is REFUSED. Substrate hand-off: AMEND v4_loop_segregation failure_record (strengthen the ascending-spiral coupling so a non-motor loop can win on >=3/4 divergent seeds). Stays candidate / (MECH-439 substrate_ceiling; ARC-108/ARC-110 substrate_conditional) / pending_retest_after_substrate / PROMOTES NOTHING.

## 10. Routing decision (user-confirmed 2026-07-03)

- **evidence_direction:** `non_contributory` (MECH-439, ARC-108, ARC-110) -- confirmed, never a weakens.
- **epistemic_category (recommended):** `substrate_ceiling`.
- **routing:** `implement-substrate`; re_derive_brake FIRED (MECH-439, ARC-108); same-claim re-queue REFUSED.
- **substrate hand-off:** AMEND `v4_loop_segregation` -- append the limbic-effective-weight failure_record (the only substrate entry covering all three claim_ids).
- **pending_retest_after_substrate:** true (already set on all three; check that remaining "supports" on these claims are not narrow/single-pathway when governance rebuilds).
- **claims edits:** none beyond the evidence_quality_note; PROMOTES NOTHING.
