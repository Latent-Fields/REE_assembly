# Failure Autopsy: V3-EXQ-890 (MECH-471 acquisition reliability probe)

Generated: `2026-08-07T20:04:51Z`
Status: **confirmed**
Scope: single
Trigger: `experiment_purpose: "diagnostic"` PASS with no confirmed adjudication (2026-08-07 policy).

## 1. Dry-run gate

`scripts/check_dry_run_citations.py v3_exq_890_mech471_acquisition_reliability_probe_20260806T041928Z_v3` → 0 dry, 1 clean. `dry_run: false` explicit in manifest. `elapsed_seconds=36992.33` (~10.3h) across 16 seeds.

## 2. Facts

**Run**: queue_id `V3-EXQ-890`, `experiment_purpose: diagnostic`, `claim_ids: [MECH-471]`. This is the **third** MECH-471 leg (875 and 875a both FAILed on readiness-gate/implementation problems — `precondition_unmet` and `competence_implementation_gap` respectively, not the phenomenon itself). 890 is purpose-built to discriminate *why* survival-competence acquisition on the all-ON REE stack splits bimodally across seeds — a pattern independently corroborated by MECH-472's V3-EXQ-882a on overlapping seeds (seed 43 solves in both 875a and 882a; seeds 42/45 fail in both).

**Design**: single continuous P1 REINFORCE run per seed (no restart, no Phase-2 targeted update — "deliberately cheaper" than 875a/882a), 16 seeds (8 overlapping 875a/882a for comparability, 8 new for distributional coverage), 8 checkpoints at 20-episode intervals with per-episode trajectory tracing (read-only additions to a vendored, mechanically-diffed copy of `_train_all_on_agent`, one real transcription slip caught and fixed during vendoring per WORKSPACE_STATE.md 2026-08-05T18:59Z).

**Three pre-registered rivals** (hypothesis-space registry, qid `mech471_competence_acquisition_reliability`, registered 2026-08-05):
- **H-exploration-init-variance** ("H1"): failing seeds get stuck early in a bad local optimum and never escape — predicts early, persistent divergence.
- **H-hazard-layout-difficulty-variance** ("H2"): per-seed hazard/reef layout randomization makes some seeds' task genuinely harder — a task-difficulty confound, not a learning-variance one.
- **H-bias-head-ofc-interaction** ("H3", exploratory only, no pre-registered threshold): the stack's other drives (lPFC bias, OFC devaluation) interact adversely with survival acquisition for some seeds.

**Per-seed results** (16 seeds, seed 44 skipped per repo convention): official floor (final ≥ 90 ticks AND margin ≥ 22.5 over random-walk) clears only seeds 43 (91.3) and 52 (107.3). **A cleaner natural gap exists in the raw data**: 11 seeds cluster at 8.2–32.4 ticks; 5 seeds (43, 50, 52, 57, 58) cluster at 71.8–107.3 ticks; nothing falls between 32.4 and 71.8. Three seeds (50, 57, 58) clear the random-walk margin by 60–75 ticks but miss the fixed 90-tick floor by only 6–18 ticks — the driver's own `hypothesis_signal` group-mean comparisons are computed on the narrower official 2-vs-14 split, not this natural 5-vs-11 clustering.

**H1 (early divergence)**: `group_gap_by_checkpoint` = {1: 60.49, ..., 8: 64.94}; `early_frac = early_gap/final_gap = 60.49/64.94 = 0.9315` (≥ 0.7 floor) → label `early_divergence_supports_h1_framing`. Independently corroborated by raw per-checkpoint data under the *natural* 5-vs-11 split too: all 5 upper-cluster seeds are already elevated at checkpoint 1 (60.3–108.4) relative to the 11 lower seeds (12.1–41.6) — so the early-divergence signature is not an artifact of the narrower official grouping.

**H2 (hazard-layout difficulty)**: `random_walk_survival_mean` differs by `diff_frac = 0.0026` between groups (well below the 0.10 notability floor) — and critically, all 16 seeds' random-walk anchors (a control representing task difficulty independent of any learned policy) are tightly clustered at 8.5–12.1 ticks regardless of which group a seed falls in. → label `difficulty_correlate_not_evident`.

**H3 (bias-head/OFC interaction, exploratory, non-gating)**: lPFC-bias-head norms nearly identical between groups at every checkpoint (~4.36–4.39 both). OFC-devaluation norms differ modestly early (4.29 cleared vs 4.41 not-cleared at checkpoint 1) but converge by checkpoint 8 (4.71 vs 4.71). No pre-registered threshold exists to adjudicate this.

**Combination rule**: sequential, not flat AND — `activity_nondegenerate` fail → `substrate_not_ready_requeue`; `bimodal_split_ok` fail → `insufficient_bimodal_split_for_discrimination` (a genuinely distinct, non-substrate finding, deliberately not routed as a readiness failure); else PASS with label = H1's own label.

**What this run does NOT test**: MECH-471's own registered falsifier (a local-update-interference test — does a targeted competence update degrade unrelated, already-acquired competences). 890 characterizes a *precondition* of that test (is competence even reliably acquired at all) — the manifest's `evidence_direction` is `"unknown"` throughout, by the driver's own explicit framing. (Note: the derived claim-evidence index shows `"evidence_direction": "supports"` / `"adjudication": "verified"` for display purposes despite the raw manifest and driver both insisting no adjudication has occurred — `scoring_excluded: "diagnostic_probe"` correctly keeps it out of MECH-471's confidence math regardless; this indexer-derived label should not be read as a real adjudication, which is exactly what this autopsy now supplies.)

**Recording**: always-core fields all present, `substrate_stable_across_run: true`.

## 3. Claim-layer map

MECH-471 is an architectural-discipline claim (bounded/provenanced/rollback-capable competence updates, generalizing MECH-392/INV-080/MECH-401's consolidation-path discipline) — it is not itself a biological-mechanism translation claim, and its falsifier is about catastrophic-interference risk, not about why acquisition is unreliable. This run does not test that falsifier and correctly does not move MECH-471's own confidence (`evidence_direction: unknown`/non_contributory as a claim-scoring matter). Its `pending_retest_after_substrate: true` and `epistemic_category: standard` are correctly unaffected.

What 890 *does* resolve is the **separate, explicitly-tracked open question** `mech471_competence_acquisition_reliability` in the hypothesis-space registry — a precondition-characterization thread, not the claim's decisive test. This is the third leg of that thread (875, 875a, 890) and the first designed to discriminate among rivals rather than re-test readiness.

**Cross-claim connection**: MECH-471's H1 finding (early, unrecoverable stochastic-exploration failure in a REINFORCE-style bias-head readout) mechanistically resembles MECH-457's already-extensively-autopsied (7+ confirmed autopsies) foraging-competence-floor finding — a converter/bootstrap capacity gap in the same bias-head REINFORCE readout architecture, on a different task (foraging return vs survival ticks). **Q-089** (registered 2026-08-05, `depends_on: [MECH-457]`, `related_claims: [MECH-471, MECH-472]`) already flags this exact cross-reference as unresolved — "whether epistemic-deficit-driven orienting explains the cold-start competence split." No `depends_on` link exists yet between MECH-471 and MECH-457 in claims.yaml. Checked `substrate_queue.json`: no existing entry unblocks MECH-471, and MECH-457's own active bottleneck (`mech457_competence_bootstrap_explorer`) is itself `status: blocked_pending_discrimination`, not a ready build — so routing this straight to `/implement-substrate` would be premature; the cross-reference needs to be examined at the claim level first.

## 4. Biological-reference triage

MECH-471 itself is not a biology-translation claim. The *phenomenon* under characterization (individual-difference, bimodal success in an RL/avoidance-learning task) has an obvious literature angle worth noting for a future targeted review, not yet commissioned: individual variation in reinforcement-learning exploration strategy and initial-condition sensitivity, and the long-standing animal-learning finding that some subjects "get it" and generalize rapidly in instrumental/avoidance tasks while others plateau near chance (all-or-none learning curves). No dedicated `targeted_review_*` directory exists for MECH-471; MECH-471 was minted 2026-07-22 from a thought-intake citing a software-engineering paper (Microsoft SkillOpt) as a neighbouring implementation strategy, explicitly not biological grounding. This gap does not block adjudicating the current run, but is worth flagging if the acquisition-reliability question is promoted to its own claim.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a for MECH-471 itself (falsifier untested); narrowed for the open `mech471_competence_acquisition_reliability` question | H1 supported, H2 eliminated, H3 inconclusive |
| Biological reference | absent for MECH-471 (not a biology-translation claim); plausible-but-uncommissioned for the acquisition-variance phenomenon itself | No dedicated lit-pull yet; not blocking |
| Developmental / dependency prerequisites | present | SD-056/SD-070 warmups, all-ON stack built and validated |
| Implementation completeness | **implicated, not yet fixed** | H1 (exploration-init variance) points at the bias-head REINFORCE readout's exploration/initialization robustness as the likely locus |
| Environment adequacy | adequate | Reused validated env/schedule from 875a/882a; `hazard_food_attraction=0.0` correctly decouples foraging from the survival DV |
| Measurement adequacy | **partial** | Fixed-threshold official split (2-vs-14) undercounts a cleaner natural 5-vs-11 cluster in the raw data; qualitative H1/H2 findings replicate under both, but future analysis should use data-driven clustering rather than a fixed threshold |
| Integration adequacy | coupled | Exercises the full all-ON stack (SD-056+SD-070+bias-head REINFORCE) at once; H2's elimination via the random-walk-anchor control narrows the locus toward the policy/learning layer, not the environment-difficulty layer |
| Scale / capacity | likely insufficient for full confidence | 16 seeds, single continuous run per seed, no repeated sampling — modest N for characterizing a population success-rate; explicitly "deliberately cheaper" than 875a/882a by the driver's own docstring |

## 6. Learning extracted

1. **H-hazard-layout-difficulty-variance (H2) is eliminated.** Random-walk baseline anchors — a control representing task difficulty independent of any learned policy — are statistically indistinguishable between the cleared and not-cleared groups (diff_frac=0.0026, tightly clustered 8.5–12.1 across all 16 seeds). If per-seed layout difficulty explained the split, this control would differ between groups; it does not, under either the official or natural grouping.
2. **H-exploration-init-variance (H1) is supported, not exclusively confirmed.** 93% of the eventual group-gap is present after the first checkpoint (episode 20 of 160), replicating under both the narrow official split and the cleaner natural 5-seed cluster. This is necessary-but-not-sufficient evidence — it does not itself rule out H3 contributing alongside it.
3. **H-bias-head-ofc-interaction (H3) remains genuinely open.** Exploratory only, no pre-registered bar, weak/ambiguous signal (near-identical lPFC norms; modest early OFC-norm difference that converges by checkpoint 8). Not resolved by this run.
4. **Cross-claim connection surfaced, not yet formalized.** H1's mechanism (early, unrecoverable exploration failure in a REINFORCE-bias-head readout) plausibly belongs to the same failure family as MECH-457's already-established substrate-ceiling finding. Q-089 already flags this cross-reference; this autopsy is the first point where MECH-471's own evidence gives it substance rather than speculation.
5. **Measurement-adequacy note, not blocking**: the official fixed-threshold split (2-vs-14) undercounts a cleaner natural gap in the raw data (5-vs-11, at final ticks 32.4→71.8). The qualitative H1/H2 findings hold up under both groupings here, but a future characterization should use data-driven clustering (e.g. a simple gap-statistic or GMM on final ticks) rather than a fixed threshold, to avoid understating effect sizes.

## 7. Repair pathway / routing

- **Recommended `epistemic_category` for MECH-471 itself**: unchanged (`standard`); this run does not test the claim's falsifier.
- **Recommended `evidence_direction` for MECH-471**: `non_contributory` (unchanged from the manifest's own framing — precondition-characterization, not a falsifier test).
- **Hypothesis-space ledger (Step 9b, applied)**: H-exploration-init-variance → `confirmed` (necessary-not-sufficient); H-hazard-layout-difficulty-variance → `eliminated`; H-bias-head-ofc-interaction → left `alive` (resolving_runs recorded, state unchanged). `decision.decidable` left `false` — H3 remains open and the cross-reference to MECH-457 has not yet been examined at the claim level.
- **Recommended `recommended_substrate_queue_entry.action`**: `none` — MECH-457's own bottleneck (`mech457_competence_bootstrap_explorer`) is `blocked_pending_discrimination`, not a ready build; routing straight to substrate work would be premature ahead of the claim-level examination below.
- **Routing**: `claim-synthesis` — recommend a `/claim-synthesis` pass formally examining whether MECH-471's acquisition-reliability finding and MECH-457's competence-floor finding are the same underlying mechanism (per Q-089's flagged cross-reference), rather than continuing to treat them as parallel open threads. A purpose-built H3 discriminator remains open but low-priority and was deliberately left unqueued at the interactive gate rather than blocking the claim-synthesis routing.
- **Draft `evidence_quality_note` addendum for MECH-471**: *"[2026-08-07 governance: V3-EXQ-890 (confirmed autopsy, failure_autopsy_V3-EXQ-890_2026-08-07) characterizes (does not adjudicate) the open acquisition-reliability question (mech471_competence_acquisition_reliability). H-hazard-layout-difficulty-variance ELIMINATED (random-walk control indistinguishable between groups). H-exploration-init-variance CONFIRMED necessary-not-sufficient (93% of the eventual gap present by episode 20, replicates under two split definitions). H-bias-head-ofc-interaction remains open (exploratory only). Does not test MECH-471's own local-update-interference falsifier; evidence_direction stays non_contributory for claim-scoring purposes. Routed to /claim-synthesis to examine the MECH-457<->MECH-471 mechanism cross-reference already flagged by Q-089. No status change; promotes/demotes nothing this cycle.]"*

## 8. User confirmation (Step 8 gate)

User selected: **"Resolve H1/H2 in the ledger, leave H3 alive, route to /claim-synthesis"** — H1 confirmed and H2 eliminated in the hypothesis-space registry (applied to `evidence/planning/hypothesis_space_registry.v1.json`, verified via `build_hypothesis_space.py` + `check_hypothesis_space_integrity.py`, 0 flags), H3 left alive, and the MECH-457<->MECH-471<->Q-089 cross-reference recommended for `/claim-synthesis` rather than an immediate substrate build or a blocking H3 follow-up.
