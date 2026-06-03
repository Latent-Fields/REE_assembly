# Failure Autopsy -- V3-EXQ-610d (INV-074 crystallization necessity)

- **Generated (UTC):** 2026-06-03T17:57:37Z
- **Scope:** single (lineage cluster member; see Cluster section)
- **Status:** confirmed (interactive gate: routing "re-queue 610e + flag process failure")
- **Run:** `v3_exq_610d_inv074_crystallization_necessity_20260603T173519Z_v3` (machine ree-cloud-2, completed 2026-06-03T17:35:19Z)
- **Supersedes:** V3-EXQ-610c
- **Claims:** INV-074 (primary, universal invariant), MECH-334 (v3_pending, epistemic_category substrate_ceiling), MECH-333

---

## 1. Facts (reconstruction, no interpretation)

2-arm discriminative test of INV-074's core claim: plasticity crystallization is necessary for diversity persistence post-Phase-3. ARM_0 control (no crystallize), ARM_1 test (crystallize at Phase-3 entry). 3 matched seeds (42/43/44), 2500 episodes x 200 steps, infant_curriculum 4-phase training with IGW-023 Phase-3 destabilising pressure (SD-047 multi-source + SD-048 interoceptive noise + accelerated drift).

Pre-registered acceptance (each Delta >= +0.10 nats; PASS = D1 AND D2 AND D3):

| Criterion | Requirement | Observed | Result |
|---|---|---|---|
| D1 crystallization preserves diversity | ARM_1 - ARM_0 phase-3 entropy >= +0.10 | **-0.013** | FAIL |
| D2 control collapses | ARM_0 phase-2 - phase-3 entropy >= +0.10 | **+0.047** | FAIL |
| D3 sanity (both diverse at phase-2) | both > 0.4 | 1.120 / 1.120 | PASS |

Per-seed phase-2 entropy is **identical** across arms (1.0908 / 0.9581 / 1.3110), confirming crystallization is applied only at the Phase-3 boundary (arms are correctly matched through phase 2). Per-seed control collapse is noisy and small: seed 42 1.091->0.972 (drop 0.119), seed 43 0.958->0.992 (rose 0.034), seed 44 1.311->1.257 (drop 0.054); mean 0.047. All entropies sit at 1.06-1.12 of the ln(5)=1.609 maximum -- near-uniform.

**Failed criterion:** discrimination (D1 + D2). The absolute/sanity criterion (D3) passes -> substrate-ceiling fingerprint.

## 2. Root cause (decisive)

610d did **not** implement the fix 610c's autopsy prescribed; it is the same harness no-op, reproduced. Script `experiments/v3_exq_610d_inv074_crystallization_necessity.py` lines 575-585:

```python
# Policy training (simplified REINFORCE-like update on outcome).
if agent.gated_policy is not None and harm_signal < 0:
    policy_loss = -harm_signal * 0.01  # Small learning signal.
    policy_loss_t = torch.tensor(policy_loss, device=device, requires_grad=False)
    pass  # Omit policy training in this substrate diagnostic.
```

- `requires_grad=False` + `pass` -> **the policy is never trained**. There is no `policy_optimizer.step()` anywhere in the file (the only `.step()` calls are aux/e2_wf/harm_eval/e1 optimizers).
- The expansion optimizer rebuilt at line 635 (`policy_optimizer = optim.Adam(agent.gated_policy.expansion_parameters(), ...)`) is **never stepped**.
- `ewc_penalty()` has **zero call sites** in the file -- it is never added to any loss.

So `crystallize()` freezes never-trained heads; the expansion layer never learns; the EWC write-protect never enters the loss. Crystallization is a behavioral no-op and INV-074's predicted winner-take-all collapse is never instantiated. The near-uniform entropies (1.06-1.12) are the signature of an untrained policy -- identical to 610c.

The IGW-023 Phase-3 destabilising-pressure substrate **did partially work**: control collapse rose from ~0 (610b, no pressure) to +0.047 (610d, with pressure), moving toward but not clearing the 0.10 floor. The substrate is not the blocker; the untrained policy is.

## 3. Claim-layer map

| Claim | Type / status | Did the test let it express? |
|---|---|---|
| INV-074 | universal invariant, candidate | No -- claim never under test; **not weakened**, not falsified |
| MECH-334 | candidate, v3_pending, implementation_phase v3, epistemic_category substrate_ceiling | No -- write-protect (EWC) never exercised |
| MECH-333 | candidate | No -- plasticity-injection channel never exercised (expansion never stepped) |

claim_ids are correctly tagged (inherited from 610c, and the test does target the crystallization machinery these claims assert -- the machinery is just never exercised). No mis-attribution.

## 4. Biological-reference triage

Closest mechanism: ocular-dominance critical-period plasticity (open-window competitive plasticity, then PNN / Lynx1 / NgR1 closure); monocular-deprivation = monostrategy capture when the window never closes. INV-074 is a **biology-faithful translation, not a formal-definition import** -- divergence none, lit present (lit_conf ~0.82). The FAIL matches a **missing prerequisite** of the reference mechanism (a competitive learning dynamic that would collapse without closure -- i.e. a trained WTA-prone policy), not a divergence and not a falsification.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | claim never allowed to express; not weakened |
| Biological reference | clear + faithful | OD critical-period / BCM; lit present; no divergence |
| Prerequisites | missing | requires a trained WTA-prone policy; harness omits policy training |
| Implementation | stub | crystallize() fires (symbol) but functional role absent: heads never trained, expansion never stepped, EWC never in loss |
| Environment | adequate-but-irrelevant | IGW-023 pressure present and partially working; not the blocker |
| Measurement | misleading | D1/D2 measure an untrained near-uniform distribution crystallization cannot move |
| Integration | n/a | |
| Scale | n/a | |

**Recommended epistemic_category:** `measurement_test_design_defect` (carry forward 610c's).

## 6. Cluster

8th non_contributory crystallization-arm result in the **543h/i/k/l + 610a/b/c/d** lineage. One structural property: *a functional, trained, WTA-prone policy has never actually been placed under the crystallization mechanism.* (543 sub-lineage: heads never differentiated; 610 sub-lineage: no policy training / no collapse pressure.)

**Not a cluster member with V3-EXQ-632/634.** Those are the goal-pipeline foraging-competence ceiling (MECH-229/230, scaffolded_sd054_onboarding substrate) -- different substrate, claims, and structural property. 610d shares only the abstract sanity-passes / discrimination-fails *shape*, not the underlying cause.

## 7. Process finding (load-bearing for routing)

The 610c autopsy (confirmed, 2026-06-03) routed to `/queue-experiment` for a 610d that would (a) train the policy, (b) step `expansion_parameters()`, and (c) add `ewc_penalty()` to the loss. **610d implemented none of the three** -- it is a near-copy of 610c with the same `pass  # Omit policy training` no-op. The autopsy->queue-experiment handoff silently dropped the prescription. The 610e re-queue must carry a pre-run assertion verifying all three fixes are present so the prescription is not dropped a third time.

## 8. Learning extracted

1. 610d reproduced 610c's harness no-op verbatim despite the prescription -- process control gap in the autopsy->queue-experiment handoff for harness-level fixes.
2. The crystallization machinery is wired + contract-tested but behaviorally inert in any harness that does not train the policy AND step `expansion_parameters()` AND add `residue_field.ewc_penalty()` to the loss.
3. The IGW-023 Phase-3 destabilising-pressure substrate partially worked (control collapse ~0 -> +0.047); the substrate is not the blocker.
4. D3 passing while D1/D2 fail is the substrate-ceiling fingerprint -- here harness-driven.
5. 8th non_contributory crystallization-arm result; one structural property across 543h/i/k/l + 610a/b/c/d.
6. Not a 632/634 cluster member.

## 9. Repair pathway / routing

**Routing: `/queue-experiment` redesign V3-EXQ-610e** (user-confirmed at the interactive gate, with the process failure flagged). 610e must:

- Train the policy with a real REINFORCE update (stored log_probs + advantages, a stepped `policy_optimizer`).
- Step `gated_policy.expansion_parameters()` post-crystallization.
- Add `residue_field.ewc_penalty()` to the loss.
- Carry a **pre-run assertion in the queue rationale** that `policy_optimizer.step()` is called, `ewc_penalty()` is summed into the loss, and `expansion_parameters()` are stepped -- so the prescription is not dropped a third time.
- Pre-register the substrate-ceiling fork: a trained-policy control that STILL does not collapse strengthens MECH-341 / MECH-313 (diversity preservation robust), it does not weaken INV-074.

`recommended_substrate_queue_entry.action = none` -- the env substrate (IGW-023) already landed and is not the blocker; leave substrate_queue unchanged.

Draft `evidence_quality_note` for governance: see the JSON artifact `recommended_evidence_quality_note`.

---

*Artifact pair: `failure_autopsy_V3-EXQ-610d_2026-06-03.{md,json}`. This skill produces the diagnosis; `/governance` applies the manifest/claim writes; `/queue-experiment` produces 610e.*
