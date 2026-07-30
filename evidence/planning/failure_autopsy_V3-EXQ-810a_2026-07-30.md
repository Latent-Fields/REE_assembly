# Failure Autopsy: V3-EXQ-810a (ARC-071 / MECH-323 / MECH-324 chunk-accumulator readiness)

**Generated:** 2026-07-30T06:47:38Z
**Scope:** single
**Status:** confirmed
**Chip:** chip-20260730-autopsy-810a (spawned by the 2026-07-29/30 `/governance` cycle: this diagnostic PASS routes a governance decision but had no confirmed or in-flight autopsy)

**Why this autopsy was owed despite the run looking clean.** V3-EXQ-810a is a *readiness* diagnostic (`experiment_purpose: diagnostic`, self-routed `chunk_accumulator_fires`, PASS). A separate confirmed autopsy — `failure_autopsy_V3-EXQ-822b-834_2026-07-29.json` (target `v3_exq_834_...`) — already cites 810a's result as settled fact: *"V3-EXQ-810a already validated the chunk-accumulator readiness fix on the identical substrate_hash."* That is a downstream session treating a never-autopsied self-report as ground truth. This autopsy closes that gap.

## 1. Facts reconstruction

**Run:** `v3_exq_810a_arc071_chunk_accumulator_readiness_20260728T204535Z_v3` (queue_id V3-EXQ-810a), machine `ree-cloud-2`, `linux-x86_64-py3.10-torch2.12.0+cpu`, elapsed 13191.76s (~3h40m). `experiment_purpose: diagnostic`. `architecture_epoch: ree_hybrid_guardrails_v1`. `supersedes: v3_exq_810_arc071_chunk_accumulator_readiness`.

**Dry-run check (Step 2a):** `check_dry_run_citations.py` on this run_id — `0 dry cited, 1 clean`. Not a smoke. `dry_run_checked: true`, `excluded_dry_run_ids: []`.

**Recording provenance:** `ree-v3/validate_recording.py --paths <manifest>` — OK, 0 always-core gaps. `recording_schema: rec/v1`, `substrate_hash` present (`12dc9bfda051930e4b090e18fe9c375b3174a7991b7622a6f24debc9c0170882`), `machine`/`machine_class` present, `elapsed_seconds` present, full `config` and explicit `seeds: [101,202,303,404,505,606,707,808]` present.

**What the script measures and why (from the driver's own docstring).** 810a is the corrected successor to V3-EXQ-810 (FAIL, `chunk_accumulator_silent`, form_seed_frac 0.333). 810's own confirmed autopsy (`failure_autopsy_backlog_2026-07-24`, category `competence_implementation_gap`, direction `non_contributory`) found the negative was starvation, not a substrate ceiling: 810's reduced driver loop never called `update_residue` (where MECH-091's `clock.phase_reset()` lives) and ran `num_hazards=0`, so the E3 tick was perfectly periodic (exactly 3.00 symbols/trial on every seed), making chunk sizes 4-5 structurally unreachable. 810a applies four corrections, each mapped to a specific 810 finding: (1) full agent loop via `StepHarness` + `num_hazards=2` so MECH-091 phase-resets actually fire; (2) 72-step x 120-episode schedule (not halved, unlike an earlier 60-episode probe); (3) 8 seeds (810's C1 was a 3-seed binary vote, underpowered at a true per-seed rate of 0.8); (4) `ARM_FULL_TRAILING` vs `ARM_FULL` isolates `use_chunk_all_position_credit` at the corrected episode length. Chunk-formation trigger parameters (`chunk_min_repetitions=5`, `chunk_window_trials=60`) are explicitly probe-scaled down from the registered defaults (R_min=20, W=100) — declared in `experiments/_lib/baselines/arc071_chunking.py`, same ratios/structural properties preserved, and justified by 810's own measurement that repetition reached 37 against a bar of 5 (repetition was never the binding constraint, so this scaling does not manufacture the pass).

**Three arms, 8 seeds each:** `ARM_OFF` (chunking off, C3 inertness control), `ARM_FULL_TRAILING` (810's exact credit configuration at the corrected episode length), `ARM_FULL` (all-position credit, the primary arm; C1 is load-bearing here).

**Readiness preconditions (three, `kind: readiness`), each asserting the SAME statistic the downstream gate consumes (not a proxy):**

| Precondition | Floor | Worst-seed measured | Margin | Met |
|---|---|---|---|---|
| `salient_harm_events_fire` (harm_step_fraction) | 0.01 | 0.0267 (ARM_OFF/seed202) | 2.7x | yes |
| `episode_outcome_spread_supra_floor` | 0.05 | 0.3488 (ARM_FULL/seed202) | 7.0x | yes |
| `chunk_buffer_supports_size_range` (symbols/trial) | 4.0 | 9.408 (ARM_FULL_TRAILING/seed303) | 2.4x | yes |

All three arms' gates are green (`gate_any_arm_green: true`, `gate_c1_arms_green: true` — the load-bearing criterion's own credit-ON arms, not just the aggregate, are ready). None of these are knife-edge passes.

**Pre-registered criteria (all pass):** C1 (load-bearing, accumulator fires): `c1_full_seed_frac = 0.875` (7/8 seeds) against a 0.75 bar — verified directly from per-seed rows (ARM_FULL: seeds 101/303/404/505/606/707/808 formed 6-45 chunks each; seed 202 formed 0). C2 (crystallisation): passes, `full_n_crystallised_mean = 17.0`. C3 (ARM_OFF inert): passes, `chunking_instantiated=false` and 0 formed on every ARM_OFF row. C4 (MECH-094 safety, no replay-origin chunks): passes, `n_replay_formed_total = 0`. C6 (size budget exercised): passes, `max_formed_chunk_length = 5` (810 could never exceed 3). C7 (credit rule separable): passes, `full_n_credit_events_mean = 2385.0` vs `full_trailing_n_credit_events_mean = 478.625` — a 5x separation, not a marginal one. `overall_pass = true` -> self-route label `chunk_accumulator_fires`, matching the manifest exactly. All `criteria_non_degenerate` flags are `true`.

**One genuine caveat, not a defect.** ARM_FULL seed 202 formed **zero** chunks despite its own readiness preconditions being met with wide margin (spread 0.3488 = 7x floor; harm-fraction 0.0267 = 2.7x floor — seed 202 is in fact the *worst* cell on both, yet still comfortably above floor). This is a genuine single-seed behavioural non-formation under full-margin readiness, not a readiness-gate failure. It does not threaten the aggregate PASS (7/8 = 0.875 clears the pre-registered 0.75 bar with one seed of headroom), and the driver's own docstring anticipated exactly this shape of result ("IF C1 STILL FAILS UNDER THE FULL LOOP WITH HAZARDS, THAT IS THE FINDING... a real and reportable result about the agent's behavioural repertoire"). At the aggregate level C1 does not fail, but the seed-202 pattern is worth a targeted look (see Step 8 outcome / recommended routing).

## 2. Claim-layer mapping

| Claim | Type | Status before this run | `v3_pending` | Prior evidence |
|---|---|---|---|---|
| ARC-071 | architectural_commitment | candidate | true | none ("NO EXPERIMENTAL EVIDENCE YET" per claim note as of 2026-07-22) |
| MECH-323 | mechanism_hypothesis | candidate | true | none |
| MECH-324 | mechanism_hypothesis | candidate | true | `pending_retest_after_substrate: true` |

All three depend on a mix of stable (MECH-094) and still-candidate substrate (ARC-069, MECH-322, SD-014, SD-039, MECH-269, INV-037, INV-038). The candidate status of those dependency *claims* is a claim-maturity axis, separate from whether their *substrate code* runs correctly — C3/C4 (MECH-094 safety pin, ARM_OFF inertness) passing non-degenerately confirms the dependency substrate that this run actually exercises is functioning.

**Did the run let the claims express themselves?** ARC-071's registered claim text includes a benefit clause ("rollout deliberation budget drops massively") that this run explicitly does not test — `use_chunk_proposal_injection=False` in every arm, stated plainly in the driver docstring under "WHAT THIS RUN DOES NOT CLAIM." So the run tests the *formation/maintenance mechanism* (MECH-323's trigger + MECH-324's crystallisation), which is the substrate ARC-071's behavioural claim depends on, but not ARC-071's headline behavioural prediction itself.

## 3. Biological-reference triage

Closest reference mechanism: striatal (dorsolateral striatum) chunking of repeated action sequences into single behavioural units, with prefrontal (IL/vmPFC) maintenance — Graybiel 1998/2008 (repetition + outcome-consistency trigger, hundreds-of-trials onset), Yin & Knowlton 2006 (DLS as the formation locus), Smith & Graybiel 2013 (IL optogenetic disruption as causal evidence for the maintenance operator MECH-324 instantiates). This is not a formal-definition import — it is a direct biological translation, and the literature grounding was already pulled and is on record: `targeted_review_arc_071_composition` (registered 2026-05-10, aggregate `lit_conf 0.848`). Biological reference: **clear**, and the divergence-vs-formal-import question does not arise here (no formal counterfactual/information-theoretic construct is being substituted for the biology).

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | strengthened | First experimental evidence for all three claims; corrects 810's starvation artifact under a realistic full-loop workload; appropriately scoped by `experiment_purpose=diagnostic` (see below) |
| Biological reference | clear | Graybiel / Yin & Knowlton / Smith & Graybiel striatal chunking; lit_conf 0.848 already on file |
| Developmental / dependency prerequisites | present | MECH-094 (stable) confirmed functioning via C4; MECH-322 carve-out correctly inert; other `depends_on` entries remain candidate-status claims but their substrate is exercised without incident |
| Implementation completeness | complete | ChunkAccumulator formation + maintenance operators both fire and crystallise under the full agent loop; probe-scaled trigger parameters explicitly justified against 810's own measurement, not degenerate |
| Environment adequacy | adequate | 8x8 hazard(2)+resource(6) grid, full `StepHarness` loop (one `update_residue` per env step), 72-step x 120-episode schedule — directly repairs 810's three starvation causes |
| Measurement adequacy | adequate | Readiness preconditions assert the *same* statistic the downstream gates consume (no proxy substitution); worst-seed methodology; `validate_recording.py` clean |
| Integration adequacy | coupled | Full realistic agent loop, not an isolated stub — this is precisely what 810 lacked |
| Scale / capacity | adequate | 8 seeds (vs 810's underpowered 3), 120 episodes x 72 steps; C1 margin (7/8 vs 6/8 bar) leaves one seed of headroom |

**Recommended `epistemic_category`:** not applicable in the FAIL-taxonomy sense (this is a confirmed PASS, not a ceiling/gap reading) — closest equivalent is "verified readiness confirmation." The indexer's own `adjudication: verified` (computed from `criteria_non_degenerate` + preconditions, independent of this autopsy) agrees.

**Scope check — does the self-report over-claim?** The manifest sets `evidence_direction: supports` / `evidence_direction_per_claim: supports` for all three claims. Read naively, that could overstate what a diagnostic-purpose, injection-off run demonstrates about ARC-071's behavioural-benefit clause. Checked directly against the built index (`evidence/experiments/claim_evidence.v1.json`): all three entries carry `scoring_excluded: "diagnostic_probe"` alongside `adjudication: "verified"` — the pipeline already excludes `experiment_purpose=diagnostic` runs from claim-confidence scoring (`build_experiment_indexes.py` line ~2640), so the `supports` direction is descriptive metadata, not a scored confidence contribution. **No correction to the manifest or the index is owed.** This is the pipeline working as designed, not a gap this autopsy needed to close.

## 5. Downstream citation check (V3-EXQ-822b-834)

`failure_autopsy_V3-EXQ-822b-834_2026-07-29.json` cites 810a's result twice: "prerequisites: present — V3-EXQ-810a already validated the chunk-accumulator readiness fix on the identical substrate_hash" and "does not reproduce the V3-EXQ-810 too-few-symbols defect that V3-EXQ-810a already confirmed fixed on the identical substrate build (substrate_hash 12dc9bf..., both started within 8s of each other)." Verified directly: `v3_exq_834_...` and `v3_exq_810a_...` manifests carry the byte-identical `substrate_hash` (`12dc9bfda051930e4b090e18fe9c375b3174a7991b7622a6f24debc9c0170882`) — the citation's substrate claim is correct. That autopsy is also self-aware about the gap this session closes: its own `re_derive_brake.not_fired_reason` explicitly lists "V3-EXQ-810a (PASS, no autopsy target)," and it does not rely solely on 810a — 834 carries its own independent corroborating data (4/5 seeds forming 8-44 chunks on the same substrate). **The citation is accurate and was appropriately hedged even before this autopsy existed; this autopsy retroactively confirms the fact it was citing.**

## 6. Learning extracted

- Existing dependency **strengthened**: this is a positive-negative-turned-positive result — 810's starvation diagnosis (autopsy-confirmed `competence_implementation_gap`, not a ceiling) predicted that fixing the three starvation causes would let the mechanism fire, and it did, robustly, across 7/8 seeds with wide readiness margins.
- The `diagnostic` / `scoring_excluded` machinery is working correctly here: it lets a substrate-readiness confirmation self-report `supports` for narrative/routing purposes without inflating claim confidence prematurely (ARC-071's behavioural-benefit clause remains untested).
- Seed 202's zero-formation-despite-ample-readiness-margin is a genuine, reportable residual signal about single-seed behavioural variability, distinct from readiness. Not load-bearing against the aggregate PASS, but worth a targeted follow-up rather than being silently absorbed into "7/8 is fine."

## 7. Routing (user-confirmed at Step 8 gate)

**Primary: confirm, no repair pathway needed.** The self-report holds up under independent re-derivation from raw per-seed data, the recording is complete, the readiness margins are non-vacuous, and the pipeline already correctly scopes the evidence via `scoring_excluded`. No claims.yaml correction, no re-queue, no substrate work is owed for the core PASS.

**Secondary (user-selected): flag seed 202 for a targeted follow-up.** Recommend a `/queue-experiment` diagnostic isolating why ARM_FULL/seed202 formed zero chunks despite readiness preconditions holding at 7x-9x their floors — e.g. a seed-conditioned behavioural-repertoire probe (does seed 202's action distribution differ systematically from the forming seeds under the same full-loop+hazard conditions?). This is `complex (probe-gated) / puzzle (known rules)` in the work-graph-debt vocabulary: the frame (readiness is necessary but evidently not sufficient for formation on every seed) is well-posed, but the specific behavioural fact about seed 202 is missing. Not a substrate gap (readiness margin rules that out), not a granularity-debt signal (no `weakened` target exists for these claims — confirmed via `granularity_debt_cluster.py`), and not load-bearing enough to block anything currently queued.

**Re-derive brake:** not applicable — this is a PASS, not a `substrate_ceiling`/`non_contributory` FAIL. `re_derive_brake.fired: false`.

**Granularity-debt recurrence trigger:** checked via `granularity_debt_cluster.py` for all three claims. ARC-071: 2 targets / 2 files, alignment distribution `unclear=2`. MECH-323: adds one `strengthened` target from an unrelated 2026-07-28 sweep autopsy. MECH-324: `strengthened=1, unclear=1` (one target reads mixed: strengthened on retention structure, weakened on the specific quantitative f_reacq prediction — from a different, already-existing autopsy, not this run). **No target across any of the three claims reads `weakened` from *this* run's own diagnosis; the pre-existing MECH-324 `weakened` component belongs to a separate, already-autopsied target (the rapid-reacquisition falsifier), not to 810a.** Trigger does **not** fire.

**Recommended substrate_queue_entry:** `action: none` — no substrate gap; the substrate is confirmed ready.

## 8. Chip resolution

`chip_ref: chip-20260730-autopsy-810a` — resolved `done` at session close via `chip_ledger.py`, noting this artifact and that the follow-on seed-202 probe is spawned as its own chip per the "chip everything except /governance and /failure-autopsy work" default.
