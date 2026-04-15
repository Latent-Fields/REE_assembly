# SD-019/020/021: Harm Stream Validation — Unblock the Dependency Chain

> Paste this into a new Claude Code session as your opening message.
> Created: 2026-04-14

## Prompt

Task: SD-019/020/021 harm stream validation — unblock the dependency chain

Three implemented-but-unvalidated substrate decisions form a dependency cluster in the harm/avoidance pathway. All are implemented in ree-v3 but blocked by upstream dependencies. The goal is to understand each blocker, determine whether it's been resolved by recent work, and design experiments that can validate them.

**SD-019 (affective nonredundancy constraint):** Penalizes cosine similarity between z_harm_s and z_harm_a projections, forcing the two harm streams to encode different information. BLOCKED because both encoders were receiving the same 50-dim proximity signal — nonredundancy loss had no discriminative signal. SD-022 (directional limb damage) was implemented to fix this by giving z_harm_a an independent body-damage source. EXQ-241b PASS confirmed the causal independence. **Question: is SD-019 now unblocked? Can we run the nonredundancy experiment with SD-022 active?**

**SD-020 (affective harm surprise PE):** z_harm_a should encode precision-weighted prediction error (unexpected threat escalation), not raw accumulated harm. BLOCKED because harm events were too rare in standard grids (10-20 per seed, need 50+ for EMA calibration). **Question: can we configure a hazard-dense environment to generate enough harm events? What hazard parameters are needed?**

**SD-021 (descending pain modulation):** During committed trajectories through expected harm, z_harm_s precision is attenuated (endogenous analgesia). BLOCKED because committed sequences weren't forming (MECH-090 dependency). **Question: if MECH-090 can't be fixed immediately, can we force committed state externally (commitment_threshold=-1) to test the descending modulation pathway in isolation?**

Start by reading: the SD-019, SD-020, SD-021 claim entries in REE_assembly/docs/claims/claims.yaml. Then read the relevant code in ree-v3/ree_core/ — look for harm_nonredundancy, harm_surprise_pe, descending in the config and agent files. Check whether EXQ-241b's SD-022 validation actually unblocks SD-019. For SD-021, check whether commitment_threshold=-1 would activate the descending modulation pathway or bypass it.
