# ARC-021 H2 (real-stack merge) leg -- NOT QUEUED, refused at `/queue-experiment` Step 2.5d: the merge manipulation is INERT on the current stack

**Status: NOT QUEUED. No EXQ number consumed, no driver in `experiments/`, no queue entry, no coordinator row.** The substrate blocker recorded on 2026-09-08 is gone (ree-v3 `b6f6733`, `REEConfig.detach_carried_prev_action`; re-confirmed here, MERGED 60/60 clean steps). But the leg's own design cannot answer its question, and fixing that is a design choice about **what "merged" means**, which belongs to the user. It is raised as decision chip `chip-20260924-decision-arc021-h2-shared-trunk-definition`.

- **Written:** 2026-09-24T13:05Z
- **Session:** `metaworker-science-20260924-arc021-h2-merged-leg`, headless on `ree-cloud-5`, working chip `chip-20260924-arc021-h2-merged-leg-queue` (campaign `science-20260924-arc021-h2-merged-leg`, orchestrate-20260924-0808).
- **Reproducer:** `ree-v3/experiments/_scratch/arc021_h2_merged_leg_param_reach_probe.py` (writes nothing, about 1 min on a worker).
- **Sibling records:** H2 substrate block `arc021_h2_leg_blocked_substrate_merged_arm_crash_20260908.md` (now discharged by `b6f6733`); H1 refusal `arc021_h1_leg_refused_readout_dies_under_unfreeze_20260911.md`; H1 dose spike `arc021_h1_unfreeze_dose_spike_20260911.md`; H3 ran as V3-EXQ-1011.

---

## 1. The finding: the three losses touch disjoint parameters

The chip, and `failure_autopsy_V3-EXQ-993a_2026-09-05` section 8, say to start from `ree-v3/experiments/v3_spark_arc021_three_loop_scale.py`: SEPARATE uses three Adam optimizers; MERGED uses one Adam over `agent.parameters()` with combined loss E1 + E2 + harm. Before designing around that manipulation, this session measured which parameters each loss can reach. Setup: ree-v3 `351f0364`, `REEConfig.large`, flag ON, 12 untrained steps with `record_transition` so both replay buffers are populated.

| loss | parameters with nonzero grad (top-level module: count) |
|---|---|
| E1 `compute_prediction_loss()` | `e1`: 28 |
| E2 `compute_e2_loss()` | `e2`: 8 |
| harm, `harm_eval(z_world.detach())` (spark SEPARATE) | `e3`: 4 |
| harm, `harm_eval(z_world)` undetached (spark MERGED) | `e3`: 4, `latent_stack`: 41, `body_obs_encoder`: 2, `world_obs_encoder`: 2 |

**No two of these sets overlap.** The overlap is ruled out by construction, not just absent in this sample. E1 and E2 train by replay over **detached** buffered latents: `agent.py:6171-6172` appends `z_self/z_world.detach().clone()` to the experience buffers, and `agent.py:11252` stores `z_self_t.detach()` in `_e2_transition_buffer`. So neither loss reaches the encoder, and neither reaches `e3`. Harm reaches `e3`, plus the encoder when undetached, and never reaches `e1` or `e2`.

**Consequence.** Adam is elementwise per parameter, and the spark applies no gradient clipping. So one optimizer over a sum of losses that touch disjoint parameters gives each parameter exactly the update a separate optimizer would. That holds for the gradient, the moment estimates and the step. On this stack, the spark's MERGED arm differs from SEPARATE in exactly two things:

1. **Learning rates.** MERGED uses `1e-3` everywhere; SEPARATE uses E1 `1e-4`, E2 `3e-4`, E3 `1e-3`. The autopsy's repair list does not mention this confound.
2. **Whether the harm gradient reaches the encoder.** This is the autopsy's repair 4, which that autopsy already names as the **H1** drive axis.

Neither difference is the one ARC-021 is about: **cross-channel credit contamination**, meaning E3 parameters moved by sensory/motor error and E1/E2 parameters moved by harm error. On this stack a combined loss cannot make that happen, because no parameter receives gradient from more than one channel.

## 2. Why this is a STOP, not a design choice this session could make

Repair 4 asks for the encoder-gradient difference to be a separate factor (2x2) or symmetric across arms. Either way:

- **Symmetric** (both detached or both undetached) plus matched learning rates: the arms are **mathematically the same training procedure**. Any measured difference would be noise. That is Step 2.5d's **INERT** shape: the manipulation cannot reach the DV.
- **Symmetric without matched learning rates:** the only contrast is the learning rate. That is a learning-rate ablation, not a channel-separation test.
- **2x2:** the topology factor stays inert, and the detach factor is the H1 leg, already refused on 2026-09-11 for a separate reason (the control readout dies under unfreeze).

ARC-021's `what_would_answer` specifies the manipulation as *"Collapse E1, E2 and E3 into a **shared trunk** under a single optimizer and one combined loss"*. The current real stack has **no shared trunk to collapse into**: E1/E2 never train the encoder. A real H2 therefore needs a design decision about what the shared trunk is. The obvious candidate is to let the E1/E2 replay losses train through the live `latent_stack` rather than detached buffers. That changes what is measured, and it is not specified by the chip, the pre-flight, the autopsy or the WWA, so it goes to the user (decision chip, section 4).

**The 2026-09-08 blocked-substrate record was right that H2 could not run, and incomplete about why it could not answer.** Had the crash never existed, the spark MERGED arm as written would have run, reported a SEPARATE-vs-MERGED delta, and been read as an H2 result. That delta would have been an H1 (encoder-gradient) effect mixed with a learning-rate effect.

## 3. What this does and does not decide about ARC-021

- **It decides nothing about the claim's truth.** No run, no evidence, `adjudicating_runs` untouched.
- **It is a real structural observation that governance may want recorded:** on the V3 real stack, E1/E2/E3 are **already channel-separated at the parameter level by construction**, because E1/E2 learn from detached replay. That is consistent with ARC-021 as an architectural commitment, but it is not evidence for its *necessity* half. Nothing has tested what happens when the separation is removed.
- **The time cost matters for any redesign.** Measured on this box (a 2-vCPU `ree-cloud-5` under load average about 6, so treat these as upper bounds): SEPARATE 6.4 s/step, MERGED 4.5 s/step at `REEConfig.large`. The spark schedule is (350 + 50) episodes x 200 steps = 80k steps per arm per seed, roughly 100+ h per arm-seed on this box. Even a several-fold faster worker leaves a multi-seed paired design at days of fleet time. So the episode budget is also a design parameter for the user. Before the user sets it, it should be re-measured on an idle worker.

## 4. What is owed

1. **User decision:** `chip-20260924-decision-arc021-h2-shared-trunk-definition`. It asks what "shared trunk" means for H2, lays out the options with what each would measure, and gives a recommendation.
2. **Governance flag:** an `evidence_discrepancy` flag on ARC-021 / MECH-069, recording the disjoint-reach finding and the unlisted learning-rate confound, so `/governance` sees the H2 leg's state. No H2 proposal row exists to write a refusal onto: EXP-0008 and EXP-0006 are `executed` by V3-EXQ-993a and are deliberately left untouched, as in the 2026-09-08 record.
3. **Carry-forward for whoever authors H2 once the decision lands:** the autopsy's six repairs still apply. Add a seventh: **equalise learning rates** across arms, or make the learning rate an explicit, declared factor. Run the reach probe above against the chosen design before any smoke: the arms must show at least one parameter that receives gradient from two or more channels in MERGED and from only one in SEPARATE. Otherwise the leg is inert again.
