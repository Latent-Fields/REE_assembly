# V3-EXQ-642d (MECH-353 blocked-agency, withdraw-representable retest) -- NOT QUEUED: two of the six mandatory repairs cannot be instantiated on the current substrate

**Status: NOT QUEUED. No EXQ id consumed, no driver authored, no queue entry, no coordinator row.** Stopped at `/queue-experiment` Step 2.5a (empirical premise check). The probe is landed at `ree-v3/experiments/_scratch/exq642d_feasibility_probe.py`. A governance flag (`evidence_discrepancy`, MECH-353) carries the follow-on.

- **Written:** 2026-09-08T16:19:13Z
- **Session:** `w5-s2a-queue-fill-20260908` (Mac `DLAPTOP`, main checkout), campaign W5-S2a item 4 (`chip-20260905-exq642d-withdraw-representable`).
- **Spec under attempt:** `failure_autopsy_V3-EXQ-642c_2026-09-05` (confirmed), `recommended_next_experiments[0]` -- "642c protocol EXCEPT, and all six are required".

---

## 1. Verdict per mandatory repair

The autopsy is explicit that all six are required and that item (1) is "the decisive repair and is prior to the rest -- without it C3 stays vacuous a fifth time no matter what margin it is given". Item (1) turns out to be fine. Two others do not.

| # | repair | instantiable? | evidence |
|---|---|---|---|
| **(1)** | `action_dim=5` with `blocked_agency_noop_class=4` so WITHDRAW is expressible | **YES** | `agent.blocked_agency.config.noop_class` reads `4`; the consumer at `blocked_agency.py` (`if cls_i == c.noop_class: vals.append(passive_term)`) then gives the ASSERT bias's `passive_term` to the true stay action rather than to move-up. The family's inherited miswire is real and this fixes it. |
| **(2)** | an arm with `num_hazards > 0` so `z_harm_a` is free to vary | **NO** | `latent.z_harm_a` is `None` on **400/400 ticks** at `num_hazards=2` **with `use_affective_harm_stream=True` set and confirmed on the live config object**. The flag alone does not populate the stream; some further wiring prerequisite is unmet. C2's subtraction and C3's `no_suffering` conjunct stay dead. |
| **(3)** | a per-tick `external_block` / `action_blocked` flag series recorded to the run pack | **YES** | Both `blocked_agency.last_output().external_block_this_tick` and `info["action_blocked_this_step"]` are readable every tick. Immediately informative, too: in one config the detector fired **16 times against 428 env-blocked steps** in the EXTERNAL arm and **7 times against 0 blocked steps** in the FREE arm -- i.e. near-chance, which is exactly the confusion matrix the autopsy wanted measurable rather than assumed. |
| **(4)** | a third arm with SELF-attributable move cancellation | **NO** -- see section 2 | `motor_agency` never approaches the 0.5 attribution floor in any arm, in any of five configurations. |
| **(5)** | C3 with a pre-registered non-zero margin, counterbalanced arm order | (design-only; not blocked) | -- |
| **(6)** | `criteria_non_degenerate` re-keyed on every leg reading a pinned variable | (design-only; not blocked) | -- |

## 2. Why repair (4) is not instantiable, and why that is decisive

The autopsy calls the self-attributable arm "the H1-vs-H2 discriminator, and **the only arm that pushes `motor_agency` below the 0.5 attribution floor and therefore the only one that exercises the attribution clause at all**". It was implemented in the strongest available form: the efference copy is told the agent moved (`agent._last_action = one_hot(move)`) while the body executes the no-op, so the commanded action provably did not happen.

`motor_agency = 1 / (1 + ||predict_next_self(z_self_prev, a) - z_self_now||)` (`ree_core/agent.py`, the motor comparator immediately above the `blocked_agency.update(...)` call). Clearing the floor downward requires `motor_mismatch > 1.0`.

**Measured `motor_agency`, 900 ticks per cell:**

| configuration | FREE | EXTERNAL block | SELF (body fails) | frac < 0.5 |
|---|---|---|---|---|
| `action_dim=5`, noop=4, hazards=0, untrained self-forward | 0.722 | 0.722 | 0.717 | 0.000 |
| `action_dim=5`, noop=4, hazards=2, untrained self-forward | 0.720 | 0.721 | 0.717 | 0.000 |
| `action_dim=5`, noop=4, hazards=2, **P0-trained** self-forward | 0.968 | 0.975 | 0.937 | 0.000 |
| + `use_affective_harm_stream=True`, trained self-forward | 0.969 | 0.975 | 0.932 | 0.000 |

Never below 0.86 in any cell of any arm; `frac < 0.5` is **0.000 everywhere**. Training the self-forward model makes it *worse* (0.72 -> 0.97), because a trained model predicts `z_self` well whether or not the action was executed.

**The structural reason, measured directly.** A deterministic replay probe drove an identical 25-step prefix, then branched on the final action only:

```
|| z_self(executed move 0) - z_self(executed no-op) || = 0.010715
|| z_self(executed move 0) - z_self(executed move 1) || = 0.023517
|| z_self ||                                          = 0.648637
```

Executing a real move versus executing nothing moves `z_self` by **1.7% of its own norm**. The motor comparator would need a mismatch of `> 1.0` -- roughly **100x** the separation the substrate actually provides -- for `motor_agency` to cross the floor. `z_self` simply does not encode the executed action strongly enough for an execution failure to register.

**Consequence.** Queuing 642d with repair (1) but without (2) and (4) would deliver: the attribution clause unexercised for a fifth consecutive run (642c: true on 14400/14400 ticks), C3's `no_suffering` conjunct dead for a fifth time, and H1-vs-H2 untouched. The autopsy's `closes` field claims this run closes "H3 fully (item 2)" and "H1 vs H2 (item 4)"; on the current substrate it would close neither. That is a fifth vacuous C3, which is precisely what the autopsy wrote item (1) to prevent -- item (1) turns out to be necessary but nowhere near sufficient.

## 3. Honest limitation -- what this probe does NOT establish

**It does not establish anything about the `z_block` DV level, and it should not be read as doing so.** The probe's control configuration (`config A`, 642c-faithful apart from a 30- rather than 60-episode P0 and a flat rather than episodic measurement loop, built through 642c's own module so `CALIBRATION_CONFIG`, `ENV_KWARGS`, `CFG_KWARGS` and `GOAL_PIN` are inherited by construction) produced `outcome_mismatch` **identically 0.0000** and therefore `z_block` identically 0, whereas V3-EXQ-642c's real run recorded 867 `z_block` fires and control-arm means of 0.064-0.177. So the harness is **not** faithful to 642c's DV regime, and I could not resolve why within this session. The most likely lever is the P0 stopping point: `outcome_mismatch = max(0, ||zw_pred - zw_now|| - ||zw_now - zw_prev||) / pred_mag`, forced to 0 when `pred_mag < blocked_agency_predicted_effect_floor` (0.05), so how well `world_forward` is trained sets whether the DV has any range at all. (This is the same knife-edge the `/queue-experiment` skill already cites for this family: "V3-EXQ-642's `wf_mse ~ 2e-5`".)

**Findings (2) and (4) are unaffected by that gap**, which is why they are reported and the `z_block` numbers are not. `motor_agency` and `z_harm_a` are both computed **upstream** of the mismatch floor and are untouched by `CALIBRATION_CONFIG`: `motor_agency` depends only on `z_self` and E2's self-forward, and `z_harm_a` is `None` or not. Neither could be rescued by getting the `world_forward` training point right.

## 4. What is owed

1. **`/implement-substrate`, `z_self` action-encoding (blocks repair 4).** Either `z_self` must carry the executed action strongly enough for the comparator to see an execution failure, or `motor_agency` must be re-sourced from something that does (an efference-copy-vs-proprioception comparison rather than a learned `z_self` forward prediction). Until then MECH-353's attribution clause is not testable **by any design**, not merely by this one -- which is a materially stronger statement than the 642c autopsy makes, and it is what governance most needs to know.
2. **`/implement-substrate`, `z_harm_a` wiring (blocks repair 2).** Identify what `use_affective_harm_stream=True` additionally requires (`num_hazards > 0` is not enough; the stream stays `None`). Plausibly a harm-history observation prerequisite -- the SD-011 second-source input -- but that was not chased down here.
3. **MECH-353 `v3_pending` stays true.** Unchanged, and this record does not change it.
4. **The DEFERRED capacity-collapse experiment stays deferred.** The autopsy holds it "until V3-EXQ-642d demonstrates in a real run that withdraw is expressible". No such run happened. Repair (1) shows withdraw is *representable* in the action space, which is necessary; whether it is *expressible behaviourally* is still unshown.
5. **Repair (3) is worth banking now.** The per-tick series is free, is the only one of the six that both works and is immediately informative, and its first reading (a near-chance detector: 16 fires / 428 blocks, against 7 fires / 0 blocks) is a real finding about the external-block detector's specificity. Whoever builds the eventual 642d should record it from the first tick.

## 5. Gate checks completed

- **Re-derive brake, MECH-353: count 0.** No autopsy target carries MECH-353 in `claim_ids` (`failure_autopsy_V3-EXQ-642c_2026-09-05` has `claim_ids: []` and lists MECH-353 under `bears_on`). Not braked; not the reason for the stop.
- **Step 2.5c substrate-path overlap: `sd_blocked_agency_mismatch_floor_calibration` is OPEN (`implemented_pending_validation`) and `corrupting`, with `substrate_paths: ["ree_core/affect/blocked_agency.py"]` -- the exact module this driver exercises. It was deliberately NOT treated as a stop.** Step 2.5c asks whether the driver exercises a path an **UNRELATED** claim's autopsy flagged as broken ("`unblocks_claims` is claim-scoped, not code-scoped"). MECH-353 is *in* that entry's `unblocks_claims`, alongside SD-029, MECH-112, SD-011 and SD-019b -- it is the claim the fix exists **for**, and the 642b/642c lineage is that entry's own validation series. Firing the gate here would be circular: it would block the only experiments that can discharge the entry's `validation_owed`. Recorded so the disposition is auditable rather than silent.
- **Queue contention:** `ree-v3/experiment_queue.json` owned by this session; no `/governance` or `/failure-autopsy` claim active at any point.

## 6. Reproducer

`ree-v3/experiments/_scratch/exq642d_feasibility_probe.py` -- writes nothing. Runs four configurations (642c-faithful control, `+action_dim5/noop4`, `+hazards`, `+self-forward P0`) plus a round-2 pass with the affective-harm stream on and the deterministic `z_self` action-sensitivity replay. Its module docstring names each question and which autopsy item it comes from. Note the `z_block` caveat in section 3 before reading anything it reports about that DV.
