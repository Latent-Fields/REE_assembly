# Claim synthesis -- MECH-157: which quantity do "sensory gain" and "hippocampal drive" condition?

- **Date:** 2026-09-25 (UTC 07:41)
- **Session:** orch0925-mech157-synth (supervised subagent of orchestrate-20260924-breakthrough)
- **Chip:** chip-20260925-mech157-mech039-claimsynth (user decision rec-20260925-cd2e8b3f: route Q-MECH157 to claim-synthesis so it returns as a concrete choice)
- **Claim:** MECH-157 (`candidate`), `docs/architecture/modes_of_cognition.md#mech-157`
- **Blocked proposal:** EXP-0861 / EVB-1442 (`blocked_substrate`); source chip `chip-20260902-mech157-sensory-hc-gate-wiring` (open, AMBER pre-flight)
- **Code state measured:** ree-v3 `main` @ `2ce89ce`
- **Scope:** design options plus one recommendation. **Nothing is applied here.** No `claims.yaml` edit, no substrate build, no blocked_note edit. The decision goes to the user through a `kind:decision` chip.

## 0. Skill fit (Step 1-3 gate), stated so this is not read as a decomposition

/claim-synthesis normally decomposes a recurring FAIL cluster. MECH-157 has **no FAIL cluster**. It has never been run, because EXP-0861 is blocked on substrate. Under the Step-3 gate the blockage is **substrate-not-ready**, so it is not granularity debt. **This document proposes no child claims.** What it does is the skill's Step 4-5 work on a design question: it names what the claim needs, grounds that in literature, lays out the options, and has the options red-teamed. The node is `complicated (buildable)` once the choice is made. Until then it is gated on a human choice between buildable options.

## 1. Premises re-measured against live code (several were wrong or incomplete)

| # | Premise (source) | Re-measured 2026-09-25 | Consequence |
|---|---|---|---|
| P1 | "No sensory-gain-shaped knob exists under any name" (pre-flight, keyword grep) | **Partly false.** There are two sensory-weighting scalars, and neither is mode-conditioned. (a) `LatentStack.encode` EMA blend `alpha_world` / `alpha_self` (`ree_core/latent/stack.py:1538-1584`; `encode` does not currently take an `operating_mode`): `z_world = alpha_world * z_world_new + (1 - alpha_world) * prev.z_world`. This is literally the weight on the current observation against the carried prior. (b) `SplitEncoder.world_precision_logit` (`stack.py:946-947, 1019-1026`): a learned per-dimension sigmoid that **multiplies z_world's magnitude**. The grep missed both because they are named `alpha_*` / `*_precision_logit`. | Sensory gain does not need to be invented from nothing. It needs a mode term on an existing scalar. This is the MECH-267 shape after all. |
| P2 | Sensory "precision" means precision-weighted prediction error | **The precision-weighted PE path is dead.** `LatentStack.compute_prediction_error` (`stack.py:1716`) is the only place `precision["world"]` weights an error, and it has **zero callers** in `ree_core/` and `experiments/`. `prec_world` acts only as a multiplicative gain on z_world. | If `prec_world` is scaled by mode, what changes is the **magnitude** of every downstream input, not the reallocation of precision. That is a confound. `alpha_world` is the only live scalar with the prior-vs-evidence meaning that MECH-157 asserts. |
| P3 | `hc_viability` should gate a "hippocampal drive" consumer (source chip) | In `salience_coordinator.py:234-240`, `hc_viability` is labelled "Hippocampal viability map (ARC-038)". Semantically it is the write gate on replay-driven **viability-map consolidation**. The waking replay call (`agent.py`, `replay_trajs = self.hippocampal.replay(...)` in the quiescent-E3 block) **throws its output away**: `replay_trajs` is never read. A replay-rate knob placed there would condition nothing. **Red-team correction:** the offline replay paths (`agent.py` ~13858 forward replay, ~13946 reverse replay) **do** consume `replay()` output, so this finding holds for the waking path only. | The MECH-267-shaped option for hippocampal drive (scale `num_replay_steps` by mode) gives a **degenerate consumer on the waking path**. Offline it has a consumer, but the knob then conditions consolidation (MECH-261/ARC-038 territory), not waking precision routing. |
| P4 | Wiring the two write-gate targets makes MECH-157 testable (source chip framing) | **Conflicts with the registered falsifier.** The MECH-157 `what_would_answer` (2026-09-21 falsifier audit, disposition R4) says: *"Consumer / boundary: the precision-application path on the shared E1 substrate ... not write gating or CEM noise, which are the consumers that actually exist."* The DV it registers is "the ratio of sensory to hippocampal precision applied on each tick". | Wiring `sensory_buffer` / `hc_viability` **as write gates** would test MECH-261, not MECH-157. The source chip and the falsifier disagree. The falsifier is the later and more deliberate record. |
| P5 | Mode dimension is live | **Not live.** From the MECH-157 precondition (measured 2026-09-18): locking the SalienceCoordinator mode changed zero committed actions and moved every telemetry channel by exactly 0.0. `mode_conditioning_enabled` and `use_salience_coordinator` both default to False. MECH-261's own disposition also records that measured coordinator occupancy is saturated on the external_task side. | Every consumer option below sits **behind** this precondition. A consumer can be built, but EXP-0861 stays degenerate until something drives the coordinator into non-external modes. |
| P6 | No "Mixed" mode (pre-flight) | Confirmed. `DEFAULT_MODE_NAMES` is external_task, internal_planning, internal_replay, offline_consolidation (`salience_coordinator.py:75-80`). The operating mode is a **soft probability vector** (MECH-261 title). | A soft vector already represents "Mixed" as a region, meaning an intermediate mixture. No enum entry is needed. |
| P7 | Rollout dimension has a consumer | Confirmed. `mode_noise_scale` + `mode_horizon_scale` (`hippocampal/module.py:1989-2031`). The ordered 4-mode gradient is still not fully restored (V3-EXQ-928). | Rollout is not part of this decision. |

## 2. Common thread (Step 4)

MECH-157 claims that one E1 substrate is switched between perception and imagination by **re-balancing how much the current state is driven by sensory evidence versus internally generated content**. The code has a live scalar for the first half: `alpha_world`, the weight on new observation against the carried prior. It has **no path at all** by which hippocampal content drives the shared z_world. Hippocampal rollouts feed E3 selection, not E1 state. So "hippocampal drive" as the claim's table defines it has no direct locus. The nearest real one (found in the red-team pass) is to couple z_world to the **E2 forward-model prediction**, the kernel the hippocampus chains, using the pattern SELF-1 already uses for z_self.

## 3. Literature grounding (Step 5)

Based on articles retrieved from PubMed:

- **Encoding/retrieval as an afferent-vs-recurrent balance set by one neuromodulator.** Cholinergic presynaptic inhibition suppresses recurrent (CA3 Schaffer / associational) transmission more than perforant-path afferent input. Extrinsic afferent input then dominates during encoding, and recurrent retrieval dominates when ACh is low. Kremin & Hasselmo 2007 ([DOI](https://doi.org/10.1016/j.neuroscience.2007.07.007)). Hasselmo & Fehlau 2001 also time the slow ACh switch (seconds) against the fast GABA switch within a theta cycle ([DOI](https://doi.org/10.1152/jn.2001.86.4.1792)). *Implication:* the biological analogue is a **balance between two content sources**, external afferent input and internally generated or recurrent content. It is not a pair of free-floating gains. The second source has to be real internally generated content, not a relabelled prior (see red-team D3, Section 7).
- **Attention as optimisation of sensory precision.** Feldman & Friston 2010 treat attention as inferring the precision of sensory data relative to prior predictions ([DOI](https://doi.org/10.3389/fnhum.2010.00215)). *Implication:* the precision locus is the weight of sensory evidence against the prior. In REE that is the job `alpha_world` does. The magnitude of the encoder output (`prec_world`) is not that locus.
- **Perceptual decoupling during internally directed cognition.** Mind-wandering attenuates the sensory P1 and theta phase-locking to stimuli: Baird, Smallwood, Lutz & Schooler 2014 ([DOI](https://doi.org/10.1162/jocn_a_00656)). Inward-directed imagery attenuates P1 and raises alpha: Villena-Gonzalez et al. 2016 ([DOI](https://doi.org/10.1016/j.neuroimage.2016.02.013)). *Implication:* in internal modes, reduced sensory weighting is the predicted phenotype. Its REE analogue is the SD-008 "event suppression" that low `alpha_world` produces, and that suppression is exactly what the Internal row should show.

A formal `/lit-pull` for MECH-157 (LIT-0862, `proposed`) has not been run. The entries above are targeted grounding for this design choice only and have not been ingested into `evidence/literature/`.

## 4. Options

Each option says where sensory gain lives, where hippocampal drive lives, how Mixed is handled, and what it costs. Every build option copies the MECH-267 idiom: a per-mode dict, a weighted sum over the soft `operating_mode` vector, a gate on `mode_conditioning_enabled`, bit-identical when OFF.

### Option A -- two per-mode scalars on one z_world blend: absolute sensory alpha plus coupling to the E2 generative prediction (RECOMMENDED; revised after red-team)

*The first draft's Option A, "hippocampal drive := 1 - alpha_eff", was **CONTESTED and withdrawn**. The complement of `alpha_world` weights the agent's own previous smoothed z_world (`stack.py:1584`). That is neither hippocampal nor generative content, so calling it "hippocampal drive" was a relabel that quietly dropped a claim dimension. Its DV `alpha_eff/(1-alpha_eff)` was also fixed by the config, so "differs by mode" would have been true by construction. See Section 7.*

- **Sensory gain:** a per-mode **absolute** `alpha_world` (a new `LatentConfig.mode_alpha_world` dict, not a multiplier on the shipped 0.3 default). It is applied in `LatentStack.encode` when `mode_conditioning_enabled` is on and an `operating_mode` is supplied. `external_task` is pinned at >= 0.9 so SD-008 is respected (red-team D2: a multiplicative scale on the 0.3 default would leave external_task below the SD-008 floor).
- **Generative ("hippocampal") drive:** a per-mode coupling `g_m` that blends z_world toward the **E2 forward-model prediction** `E2.world_forward(z_world_prev, a_prev)`. This is the kernel the hippocampus chains into rollouts (control_plane.md: "hippocampus chains those kernels into explicit rollouts"). It mirrors the existing SELF-1 / DR-13 `self_e1_anchor` pattern exactly (`stack.py:1556-1567`, `agent.py:5561-5568`, `config.py:200-201`), which blends z_self toward the cached E1 prediction with `self_recurrence_e1_coupling`. The prediction is cached at the previous tick, so no extra forward pass runs during encode.
- **Two independently settable scalars per mode**, so the claim's two dimensions are **not collapsed**. The honest narrowing is note-level only (proposed, not applied): "Hippocampal Drive is operationalised as coupling of the shared z_world to the E2/hippocampal generative prediction. A direct hippocampus -> E1 state edge is not implemented."
- **Mixed:** a region of the soft vector (intermediate alpha and g). No enum change.
- **Non-vacuous DV (red-team D1):** not the config values. Per mode, measure: (i) the **SD-008 event-selectivity margin**, i.e. how much z_world responds to environment events versus the no-event baseline, which should fall in internal modes (the perceptual-decoupling prediction); (ii) the **observation-vs-prediction divergence** `||z_world - z_obs||` and `||z_world - z_world_pred||`; (iii) downstream commitment consequences. All of this runs with the registered MECH-025-027 orthogonality control. Logging `_last_alpha_eff` and `_last_gen_coupling` is only a manipulation check.
- **Cost:** two config dicts, one blend line, one cached prediction. This is small, and on the same order as the first draft of A.
- **Risks and ownership:** (1) **MECH-245** (hallucination = generative-model dominance without sensory grounding) uses **the same locus**. A high `g_m` in external_task is MECH-245's pathological pole. That is a coupling to record in both claims' notes, not a conflict, and it gives MECH-157 a built-in pathological-arm contrast. (2) **SD-008** needs a scoping note saying that low alpha in internal modes is intended, not the regression SD-008 fixed. (3) **MECH-249** owns the ACh/NA-balance reading for hippocampal **write** profiles. Option A leaves write profiles alone and does not claim that reading.
- **Variant A-min (cheapest):** build only the per-mode absolute alpha and declare hippocampal drive "not operationalised" in the MECH-157 note. This tests half the table honestly and leaves the other half open.

### Option B -- two independent new consumers, keeping the 3-dimension table literal

- **Sensory gain:** scale `prec_world` by `write_gate("sensory_buffer")` or a new `mode_sensory_gain` dict.
- **Hippocampal drive:** scale `GhostGoalBank.rank()` retrieval weight or the AnchorSet-derived goal bias by `write_gate("hc_viability")`.
- **Mixed:** a soft-vector region.
- **Cost:** two new consumers on two unrelated paths.
- **Risks:** (1) P2: scaling `prec_world` rescales the magnitude of z_world for every downstream reader (E2, E3, residue, harm heads). That is a representation-magnitude intervention, and any effect is confounded with it. (2) Goal-retrieval gain is an **action-selection** channel, so the "hippocampal drive" DV would plausibly co-vary with the Action axis (MECH-025). That is the very orthogonality the falsifier tests, so the confound works against the claim. (3) Neither consumer is the hippocampus -> E1 path the claim describes, so this is still a proxy.

### Option C -- literal MECH-261 write gates (the source chip's original framing)

- `sensory_buffer` gates writes into a new cortical-sensory replay buffer (Rothschild/Eban/Frank 2017, cited in the gate table). `hc_viability` gates viability-map consolidation writes from replay.
- **Cost:** a buffer that does not exist, plus a consolidation consumer for replay output that is currently thrown away (P3).
- **Why not recommended:** it tests **MECH-261** write-gating semantics, which the MECH-157 falsifier explicitly excludes as the DV locus (P4). It may be worth building for MECH-261 and ARC-038, but it does not unblock EXP-0861.

### Option D -- no consumer build until the mode dimension is live

- Park EXP-0861. Route MECH-157 to the mode-governance-engagement lineage, so that the coordinator actually leaves external_task and locking it changes behaviour. Choose the consumer afterwards.
- **Cost:** zero now. **Risk:** MECH-157 stays untestable with no end date, and the consumer question comes back unchanged.

## 5. Decision block

| Option | Sensory gain locus | Hippocampal drive locus | Claim-text change | Build size | Unblocks EXP-0861? |
|---|---|---|---|---|---|
| **A (rec)** | per-mode absolute `alpha_world` (external_task >= 0.9) | per-mode coupling to E2 `z_world_pred` (SELF-1 pattern) | note: hippocampal drive operationalised as generative-prediction coupling | small | yes, once modes are live (P5) |
| B | mode-scaled `prec_world` | GhostGoalBank retrieval gain | none | medium, 2 consumers | yes, but magnitude and action-axis confounds |
| C | new sensory replay buffer write | viability-map consolidation write | none | medium-large | no: tests MECH-261, not MECH-157 |
| D | deferred | deferred | none | none now | no |

**Recommendation: A (as revised).** Its sensory-gain locus is the only live scalar that means evidence-versus-prior, which is the registered DV locus. Its drive locus is real generative content, reached through an established pattern (SELF-1) rather than an invented hippocampus -> E1 edge. The two dimensions stay independent. It pairs naturally with MECH-245's pathological pole. The biology is the afferent-versus-internally-generated balance of Kremin & Hasselmo 2007 and Feldman & Friston 2010: two content sources, weighted against each other. Choose A-min if the user wants the smallest step. **Sequencing caveat:** the knob is cheap and bit-identical OFF, but EXP-0861 must not be queued until P5 (mode liveness) is cleared, because a forced-mode arm alone does not meet the falsifier's "coordinator-driven within-life transition" required event.

**Owed after the decision, whichever option is chosen (not done here):** (1) update EXP-0861's blocked_note to reflect the choice. (2) If A is chosen, `/governance` applies the MECH-157 note narrowing and `/implement-substrate` builds the knob. (3) Resolve or re-scope `chip-20260902-mech157-sensory-hc-gate-wiring`, whose "wire the two write gates" framing is superseded by P4 under options A, B and D.

## 6. Red-team (Step 6b)

Run on a **different model (fable)**, with the proposal author's reasoning withheld. Full findings: `evidence/planning/claim_synthesis_MECH-157-039_redteam_20260925.md`.

## 7. Red-team outcome and what changed

**Verdict: CONTESTED** on the first draft's Option A. Every defect was checked against code before it was accepted:
- **D1 (accepted):** the DV was entailed by construction. Replaced with the event-selectivity and divergence DVs (Option A, "Non-vacuous DV").
- **D2 (accepted):** a multiplicative scale on the 0.3 default breaks SD-008. Replaced with absolute per-mode alpha and external_task >= 0.9.
- **D3 (accepted):** `1 - alpha` is the agent's own prior, not hippocampal content. The relabel was withdrawn, and the red-team's **missing option** (a z_world blend toward the E2 forward prediction, mirroring SELF-1; verified at `stack.py:1556-1567`) became the revised Option A.
- **P3 (accepted, narrowed):** offline replay does consume `replay()` output. The degeneracy applies to the waking path only.
- **Ownership (accepted):** MECH-245 shares the locus (coupling note), MECH-249 owns the write-profile reading, SD-008 needs a scoping note.
- **Hygiene (fixed):** `LatentStack.sense` -> `LatentStack.encode`. Line references corrected.
The other premises (P1, P2, P4-P7) were CONFIRMED by the red-team.
