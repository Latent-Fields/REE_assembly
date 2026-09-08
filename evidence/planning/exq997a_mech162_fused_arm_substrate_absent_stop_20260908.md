# V3-EXQ-997a (MECH-162 three-permutation re-convergence retest) -- STOPPED at the chip's own pre-authorised gate: the FUSED arm cannot be instantiated without new substrate

**Status: NOT QUEUED. No queue entry, no driver, no coordinator row, no manifest.** This is the outcome `chip-20260904-exq997a-mech162-three-permutation-retest` explicitly pre-authorised ("if no such path exists without substrate, say so and STOP -- that finding mints the withheld create entry `zresource-zworld-planning-fusion` via a governance flag, do not build substrate here"). A governance flag (`evidence_discrepancy`, MECH-162) carries the mint request.

- **Written:** 2026-09-08T16:19:13Z
- **Session:** `w5-s2a-queue-fill-20260908` (Mac `DLAPTOP`, main checkout), campaign W5-S2a item 2.
- **Basis:** direct source read of `ree-v3` at the shared checkout, 2026-09-08. No red-team pass was reached -- the design cannot be written, so there is nothing to review.

---

## 1. Why the retest cannot be written as specified

The confirmed autopsy `failure_autopsy_V3-EXQ-997_2026-09-04` found V3-EXQ-997 `non_contributory` on measurement grounds, and its `four_layer_diagnosis.claim_alignment` (as CORRECTED after the Fable red-team's F1) names the design fix: MECH-162's own notes call for **three** permutations -- z_resource alone, z_world alone, and **both fused** -- and 997 built only the two "alone" arms. The retest's whole point is the third arm.

That third arm has no substrate path. Verified this session, at three independent sites:

| site | what it does | fused cue possible? |
|---|---|---|
| `ree_core/agent.py:11609-11617` (`update_z_goal`) | `use_resource = config.latent.use_resource_encoder and current_latent.z_resource is not None`; then `seed_latent = z_resource if use_resource else z_world` | **No.** A strict XOR. There is no third branch and no config flag that reaches one. |
| `ree_core/hippocampal/ghost_goal_bank.py:184-190` (`GhostGoalBank.rank`) | signature is `rank(current_z_goal, persistence_appraisal=None, simulation_mode=False)` -- ONE cue vector | **No.** `z_world` appears in the whole file exactly once, in a comment at line 209; every anchor stores a `z_world` and the bank never consults it. |
| `ree_core/hippocampal/ghost_goal_bank.py:437` (`_context_salience_for_anchor`, MECH-339 composite cue) | the only composite channel in the bank; `context_salience = 1 - exp(-arousal_tag / arousal_scale)` | **No.** It is default-off (`use_composite_cue_outshining: bool = False`, `context_weight: float = 0.0`, `config.py:2437-2438`) and, even switched on, sources its context term from `payload.arousal_tag` -- explicitly *not* from spatial context. It is not a re-convergence path. |

The one operator that *does* combine the two streams is the **retrieval form** the red-team's F1 identified -- `HippocampalModule._propose_ghost_seeded` seeds CEM init and the E2 rollout at `anchor.z_world` after `goal_match` ranking on the goal cue (`module.py:2576-2706`, notably `:2658`). That is an identity-cue -> spatial-retrieval sequence, and it was already live in **both** of 997's arms, which is precisely why the autopsy re-read 997 as "which stream seeds the goal cue under an always-on retrieval fusion" rather than as two negative conditions. It is a *serial* composition, not a joint input, so it cannot serve as the FUSED arm: turning it on in a third arm changes nothing relative to the other two.

**Consequence:** a 997a built from the two available arms would repeat V3-EXQ-997's scope error under a new letter -- two single-stream conditions contrasted against each other, unable to bear on a claim about their convergence. H0 ("a fused input adds nothing over either stream alone") and H3 ("fusion required, not substitution") both stay `alive` in registry question `zresource-zworld-planning-convergence`, and neither can be moved by a run that cannot express fusion.

## 2. What is owed

**Mint the substrate entry the autopsy deliberately withheld.** `failure_autopsy_V3-EXQ-997_2026-09-04` set `recommended_substrate_queue_entry.action = "none"` with the reasoning: *"minting a corrupting-free create from a verdict whose structural premise just failed would be a substrate entry ahead of its evidence. Route: the redesign below first runs the explicit three-permutation test ... if the fused arm cannot be instantiated without a new operator, THAT run's autopsy mints the entry (`sd_id_suggested: zresource-zworld-planning-fusion` retained in `withdrawn_readings` for reuse)."*

The condition it named has now been met -- established by source read rather than by a run, which is cheaper and equally decisive, since the absence is structural rather than empirical. The withheld entry's own `implementation_hint` (preserved verbatim in the autopsy's `withdrawn_readings_2026_09_04.recommended_substrate_queue_entry_original`) already specifies the smallest step: a third, explicitly-flagged goal-seeding mode forming `z_goal` from BOTH latents (starting with concatenation/projection, the cheapest of the four operators Lee et al. 2021's review names as unspecified), plus a spatially-sourced context channel in the ghost cue -- most cheaply by generalising `_context_salience_for_anchor` to an optional `z_world`-similarity term reusing MECH-339's existing outshining gate, rather than adding a parallel mechanism.

Governance owns the mint (`/governance` Step 2b/6a), then `/implement-substrate` builds it, then this retest becomes writable. This session raised the flag and built nothing.

**Independently runnable in the meantime, and NOT blocked on the fused arm** -- from the autopsy's own `fanout_recommendation` (its note puts H2 first on cost grounds):

- **H2 (instrumentation, no new run at all):** re-analyse 997's landed manifest -- record per-tick pool sizes and per-seed dispersion, pre-declare ONE decisive aggregation, report the other as a sensitivity. This is a **GOV-REUSE-1 reanalysis**, not an experiment; `reanalysis_query.py emit` is the right vehicle. It directly addresses the verdict-inversion that made 997 non-robust.
- **H1 (representation):** re-run the existing two-arm design on a **P0-trained** ResourceEncoder in SD-015's own measured configuration (SD-057 incentive bank on `scaffolded_sd054_onboarding`, MECH-306 drive floor, `proximity_benefit_scale >= 0.18`), recording `goal_resource_r` as a load-bearing manipulation check (SD-015's precedent: 0.93-0.96 trained vs 0.066-0.087 untrained). This is a legitimate, buildable experiment *today* -- it just is not the three-permutation retest, and it is a materially larger build than this chip scoped (a different harness). The autopsy warns it can **alias with H4**, since a trained encoder may also survive longer, so it must carry the matched-window control from H4's probe.
- **H4 (process):** truncate every cell to a common step budget and a common qualifying-tick count, reporting `total_steps` and pool size as covariates.

Chipping H1+H4 as one design (they must be co-designed to avoid the aliasing the autopsy names) and H2 as a reanalysis is the correct follow-on. This session records it rather than spawning it: the mint decision above may change what H1 should look like, and `/governance` is the ratifying step.

## 3. Registry

`zresource-zworld-planning-convergence` legs H0-H4 are all `alive` with `adjudicating_runs: null`. **Left untouched** -- there is no queued run to record against them, and writing a run id that does not exist is the failure mode `adjudicating_runs` exists to prevent.

## 4. Gate checks completed before the stop

- **Chip gate** `chip-20260904-fromdims-drop-wantingweight-997`: resolved `done` (ree-v3 `91c10b7`, verified `880a82f`-era trunk green). Its resolution note records that the chip's own premise was wrong -- `wanting_weight` is NOT silently dropped; `REEConfig.from_dims(..., wanting_weight=w)` lands on `hippocampal.wanting_weight`, and the PARTIAL sweep reading is a **name collision** with the independent `GhostGoalBankConfig.wanting_weight` (whose `from_dims` name is `mech292_wanting_weight`). The registry entry explicitly warns against "repairing" it by plumbing `from_dims` into the ghost bank, which would silently couple two unrelated knobs. **So the ablated-arm-equals-control hazard the chip told me to verify does not exist**, and 997's `wanting_weight=0.0` isolation did take effect on the knob its own comment names. Checked, as instructed; it was not the blocker.
- **Re-derive brake, MECH-162:** not the reason for the stop (the autopsy's category is measurement/instrument, which correctly does not count).
- **Queue contention:** `ree-v3/experiment_queue.json` owned by this session; no `/governance` or `/failure-autopsy` claim active at start (checked 2026-09-08T15:55Z, and again before any write).
