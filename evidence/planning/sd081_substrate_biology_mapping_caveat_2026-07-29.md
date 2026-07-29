# SD-081 substrate-vs-biology mapping caveat (MECH-477)

**Date:** 2026-07-29
**Author session:** `infallible-albattani-bb85cb` (post-crash reorientation of the 2026-07-22 /lit-pull)
**Status:** scoping note for `/governance` + `/claim-synthesis` to adopt onto MECH-477's evidence. **Nothing in `claims.yaml` was edited by this note** — applying an evidence caveat is governance work.
**Tag:** GOV-ANALOGY-1 (neuroscience mapped onto REE)

## What this note is

The 2026-07-22 /lit-pull landed MECH-477's first empirical grounding (Lee, Shimojo & O'Doherty 2014; Daw et al. 2011; REE_assembly `8ab26620e0`). Reading that literature back against the **landed SD-081 substrate** — verified at source in `ree-v3/ree_core/predictors/e3_selector.py`, not inferred — surfaces a mapping caveat that is not yet attached to MECH-477's experimental evidence. The V3-EXQ-811a PASS (`supports`, 6/7 divergent seeds, `w_planned` shift 0.194) is real, but it supports a **narrower** proposition than the biology the claim is named for, and the gap is invisible unless recorded.

This note records the gap. It does not dispute 811a and does not recommend reclassifying it.

## What SD-081 actually is (source-verified)

`_arbitrate_dual_system` in `e3_selector.py` (lines ~1244–1413):

- **The two SCORE reads are one world model at two grains.** `planned_scores` is the full-depth read; the habit read is the *same scorer* with `_score_depth_limit = max(2, dualsystem_habit_depth)` truncating the z_world sequence to 2 steps (lines 1329–1360). `ree_core` contains **zero** model-free / q_value / td_error code — confirmed by the 2026-07-27 /claim-synthesis (`dazzling-taussig-f58f4c`), which struck "model-free" from MECH-163's descriptor for exactly this reason.
- **The two UNCERTAINTY reads ARE separate scalars**, each EMA-normalised against its own running baseline: `u_h` (`habit_uncertainty`, passed in) and `u_p` (`_running_variance`), normalised to `u_h_n`/`u_p_n` (lines 1375–1388).
- **The blend is a graded, symmetric convex mix:** `w = sigmoid(gain * (u_h_n - u_p_n) + bias)`, then `blended = (1 - w) * z_h + w * z_p` (lines 1391–1397).
- **The manipulation-check series is emitted** (`last_arbitration`: `w_planned`, `u_habit_norm`, `u_planned_norm`, raw + EMA), which is what MECH-477's falsifier consumes.

## Where this matches Lee 2014, and where it diverges

**Faithful (3 of 4 parameterisation points):** graded not discrete (sigmoid); trial-by-trial EMA update; an explicit `dualsystem_arbitration_bias` term. The arbitration *dynamics* are a legitimate instantiation of the allocation mechanism MECH-477 asserts.

**Two divergences, both consequential:**

1. **Correlated reliabilities (the live over-read risk).** Deep and shallow reads of the *same* model do not fail independently — a systematically wrong world model poisons both grains. Lee 2014's two systems are dissociable precisely because model-free is reliable *where model-based is wrong*. SD-081 structurally cannot represent "the deep rollout is confidently misleading, trust the cache." So 811a establishes **"an uncertainty-weighted blend over two grains of one model produces differential recruitment,"** NOT the stronger biological claim of arbitration between dissociable systems. This is the exact hazard the Daw 2011 lit entry (filed `mixed 0.62`) already flagged at the literature level — an integrated single-model architecture yields graded recruitment *without* a genuine two-system arbitrator — and it is why MECH-477's mandatory manipulation check (weight must be shown to vary with measured uncertainty) is load-bearing. That caveat is on the *literature* entry but not yet on the *experimental* evidence.

2. **Symmetric blend vs. asymmetric suppression (the future boundary).** Lee 2014 found arbitration works by *suppressing* the model-free pathway, with **no reciprocal effect detected**. SD-081 uses a symmetric convex blend. Any future claim depending on the asymmetry — habits pathologically resistant to goal-directed override; goal-directed control failing to suppress an entrenched habit — will not reproduce from this substrate. This is not a defect in MECH-477; it is a boundary on what this code can *ever* be evidence for, and it should be recorded before such a claim is raised against the same substrate.

## The recurring pattern (not a one-off)

The 2026-07-22 /lit-pull hit the identical shape on **MECH-440**: the biological variability *channel* (LMAN, an anatomically separate basal-ganglia-forebrain input, doubly dissociable from HVC per Olveczky 2011) is instantiated as noise on the selection head's *own* parameters (NoisyNet form), not a separate proposing input. Across both claims, REE collapses a biologically-*separate* structure into one shared substrate plus a knob. This is often the correct minimal instantiation — but it silently narrows which future questions the substrate can answer, and the narrowing is invisible unless written down. That is the general reason this note exists.

## Recommended disposition (for governance/claim-synthesis, not applied here)

- Attach a `mapping_caveat` to MECH-477's experimental evidence recording that 811a establishes the **two-grain arbitration dynamics**, not arbitration between dissociable systems, and that the **symmetric blend** diverges from Lee 2014's asymmetric suppression.
- Keep 811a as `supports` — the caveat scopes what it supports, it does not weaken it.
- Do **not** relax the manipulation check on any successor experiment; correlated-reliability is exactly the confound it guards against.
- Separately (already-flagged, not this note's scope): MECH-477's `live_status.evidence` still cites `failure_autopsy_V3-EXQ-811_2026-07-24` though 811a landed a clean PASS.

## Source pointers

- `ree-v3/ree_core/predictors/e3_selector.py` `_arbitrate_dual_system` (~1244–1413), `_score_depth_limit` (887–902).
- Lit entries (REE_assembly `origin/master`, `8ab26620e0`): `evidence/literature/targeted_review_connectome_mech_163/entries/2026-07-22_mech_477_reliability_arbitration_lee2014/`, `.../2026-07-22_mech_477_striatal_integration_daw2011/`, `evidence/literature/targeted_review_connectome_mech_440/entries/2026-07-22_mech_440_lman_dedicated_variability_channel_olveczky2011/`.
- 2026-07-27 /claim-synthesis (WORKSPACE_STATE.md, session `dazzling-taussig-f58f4c`): the "one model at two grains / no model-free code" verification.
