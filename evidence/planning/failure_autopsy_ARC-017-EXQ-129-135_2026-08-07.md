# Failure autopsy — ARC-017: V3-EXQ-129 (stream tag pair) + V3-EXQ-135 (reality coherence pair) — 2026-08-07

**Targets:**
- `v3_exq_129_arc017_stream_tag_pair_20260329T031933Z_v3` (V3-EXQ-129)
- `v3_exq_135_arc017_reality_coherence_pair_20260329T032442Z_v3` (V3-EXQ-135)

**Outcome:** both `FAIL` · claim `ARC-017` · `evidence_direction` (original, manifest-side) `mixed` for both
**Scope:** cluster (two facets of one claim, sharing one root-cause structure)
**Status:** confirmed (interactive gate completed 2026-08-07)
**Recommended `epistemic_category`:** `measurement_test_design_defect` (both)
**Recommended `evidence_direction`:** `non_contributory` (both)
**Routing:** EXQ-129 → `/queue-experiment` new EXQ number (redesign on existing substrate) · EXQ-135 → `/queue-experiment` same-facet retest (135a)

Spawned from a `/thought-digestion` deferral on ARC-017 (session `cool-torvalds-a82359`, 2026-08-07); chip `chip-20260807-arc017-exq129-135-autopsy`.

---

## 1. Facts

Both runs are five months old (2026-03-29), pre-date the Experimental Recording Standard (`validate_recording.py` reports 8 always-core gaps each — `recording_schema`, `substrate_hash`, `substrate_commit`, `machine`, `machine_class`, `elapsed_seconds`, `config`, `seeds`; both driver scripts carry their own `MANIFEST_WRITER_EXEMPT = "archival early-era manifest..."` marker acknowledging this), and were never touched again after their original queue commits (verified via `git log --all -- experiments/v3_exq_129*.py experiments/v3_exq_135*.py`: only the original queue commit plus one mechanical `emit_outcome` retrofit each). This is a genuine recording gap by today's standard, but not one that blocks adjudication here — full metrics and the complete driver source are available and were read directly rather than inferred.

**Dry-run check (Step 2a):** `scripts/check_dry_run_citations.py` on both run_ids → 0 dry, 2 clean. Confirmed independently: both driver scripts `sys.exit(0)` immediately after printing `[dry-run] Skipping file output.` and *before* the manifest-write block — a `--dry-run` invocation of either script physically cannot produce the manifest files that exist on disk. The manifests are real runs by construction.

**V3-EXQ-129 design:** `TYPED_TAGS_ON` (world_obs → z_world exclusively, harm_obs "routed to z_harm encoder" per docstring) vs `TYPED_TAGS_ABLATED` (`cat(world_obs, harm_obs)` → single merged encoder). Pre-registered: C1 `gap_typed >= 0.04` (both seeds), C2 per-seed delta (TYPED − ABLATED) `>= 0.02`, C3 `gap_ablated >= 0.0`, C4 `n_harm_eval_min >= 20`, C5 no fatal errors. Result: C1 FAIL (`gap_typed=0.0153`), C2 FAIL (per-seed deltas **negative**, `[-0.0098, -0.011]` — ABLATED scored *higher* than the arm meant to win), C3/C4/C5 PASS. 3/5 → FAIL.

**V3-EXQ-135 design:** `REALITY_COHERENCE_ON` (z_world trains only on real observations) vs `REALITY_COHERENCE_ABLATED` (z_world also trains on Gaussian-noise-perturbed replay of past `world_obs`, simulating "imagined" input). C1 `gap_on >= 0.04`, C2 delta `>= 0.02`, C3 `gap_ablated >= 0.0`, C4 `n_harm_eval_min >= 20`, C5 `n_replay_contamination_min >= 50` (manipulation check). Result: C1 FAIL (`gap_on=0.0153`), C2 FAIL (delta `+0.0002`, essentially zero), C3/C4/C5 PASS. 3/5 → FAIL.

**Failed criterion in both cases: C1, the absolute/floor criterion on the intact arm itself** — not merely the discrimination criterion. This is the shape the digestion note flagged as suspicious, and it is correctly suspicious, though not for the reason first hypothesized (see §4).

### 1a. The two "intact" arms are bit-identical — not independent measurements

`gap_typed_on` (EXQ-129, TYPED_TAGS_ON) = `0.015299121729194565`. `gap_reality_on` (EXQ-135, REALITY_COHERENCE_ON) = `0.015299121729194565`. **Identical to 15 significant figures.** Reading both drivers confirms why: `TYPED_TAGS_ON` in EXQ-129 builds its world input as `_build_world_input(obs_world, obs_harm) → obs_world` (harm channel dropped, see §2 below) and trains via plain `agent.sense(obs_body, obs_world)` + E1/E2 loss. `REALITY_COHERENCE_ON` in EXQ-135 calls `agent.sense(obs_body, obs_world_raw)` directly, with `config = REEConfig.from_dims(..., world_obs_dim=world_obs_dim)` — i.e. **the exact same config, same seeds (42, 123), same training loop, no manipulation applied.** These are not two independent tests of two different ARC-017 facets converging on the same floor by coincidence; they are **the same underlying measurement, computed twice under two different experiment names.** This is deterministic (`torch.manual_seed(seed)` fixes it), not a noise artifact — which is itself informative: whatever produces 0.0153 is a *stable, reproducible* property of this exact recipe, not something a different random draw would move.

### 1b. Neither arm ever gives `z_world` a reason to encode harm information

In both drivers: `z_world_curr = latent.z_world.detach()` — **detached** before being buffered for the `harm_eval_head`'s online training. The only signal that ever reaches the world encoder's own gradient is `e1_loss` (prediction) `+ e2_loss`, in *both* experiments' *both* arms. `harm_eval_head` is trained as a downstream probe on a frozen snapshot of whatever `z_world` the encoder happens to produce — it never backpropagates into the encoder. So **no experimental condition in either script ever creates training pressure for `z_world` to be harm-discriminative.** Whatever harm-relevant structure survives in `z_world` is purely incidental to world-model prediction. A floor value of ~0.015 (against `mean_harm≈0.52` vs `mean_safe≈0.50` — small but consistently nonzero and reproducible) is the expected size of an *emergent, unsupervised* signal, not evidence about whether typed routing or reality-coherence changes it, because the experiment never lets either manipulation act on a quantity that has any dedicated reason to represent harm in the first place.

**This is the more fundamental finding than "insufficient warmup."** More episodes would not close this gap, because it is not a training-duration problem — it is a training-*objective* problem common to every arm of both experiments. The original manifests' own hedge ("a FAIL here may reflect insufficient warmup rather than a genuine claim refutation") undersold the actual defect and pointed at the wrong lever.

### 1c. EXQ-129's "typed routing" arm never implements typed routing

The docstring states: "harm_obs routed to z_harm encoder (ARC-017 typed separation)." Reading `_build_world_input()`:

```python
def _build_world_input(obs_world, obs_harm):
    if typed_tags_on:
        return obs_world              # obs_harm silently discarded
    else:
        return torch.cat([obs_world, obs_harm], dim=-1)
```

`obs_harm_raw` is read from `obs_dict.get("harm_obs", ...)` and passed into this function — and then **dropped on the floor** whenever `typed_tags_on=True`. There is no `z_harm` encoder anywhere in this script; `agent.e3.harm_eval()` operates only on `z_world`. So `TYPED_TAGS_ON` is not "route harm to a dedicated encoder" — it is "give the model strictly less information than the ablated arm," which is the exact opposite of what ARC-017's hypothesis needs to be fairly tested. This single-handedly explains the wrong-direction result (ABLATED gap `0.0257` > TYPED gap `0.0153`, consistently across both seeds): the arm meant to demonstrate typed separation's advantage instead demonstrates the cost of discarding a channel outright, because no separate channel for it was ever built.

### 1d. The substrate this needed has since been built — for other claims, never applied back to ARC-017

`ree_core/latent/stack.py`'s `SplitEncoder` now has a `lateral_head` (MECH-099, "three-stream architecture," `harm_dim > 0`) that maps hazard + contamination channels directly to a genuine `z_harm`, bypassing `z_world` entirely. `ree_core/predictors/e3_selector.py` has `harm_eval_z_harm()` (SD-010): *"z_harm is the output of `HarmEncoder(harm_obs)`, NOT of the z_world encoder... resolves the EXQ-027b over-correction paradox."* This is exactly the mechanism ARC-017 asserts and exactly what EXQ-129's docstring claimed to build but didn't. It is heavily used elsewhere — `grep` over `ree-v3/experiments/*.py` for `MECH-099|harm_eval_z_harm|lateral_head` returns **~40 experiment scripts** (`v3_exq_098_mech099_three_stream.py`, `v3_exq_056_sd010_harm_stream_baseline.py`, `v3_exq_058_sd010_sd003_attribution.py`, the INV-089 `v3_exq_743/746*` family, etc.) — but **none carry `claim_ids: ["ARC-017"]`**. Confirmed via `claim_evidence.v1.json`: ARC-017's only two experimental entries, still today, are these exact two March FAILs (`latest_run_id` = the EXQ-135 manifest, unchanged since). The claim has never been retested against the substrate that was built, for other reasons, to do precisely what its own hypothesis requires.

### 1e. Reality-coherence (EXQ-135) has no comparable fix available today

Grepped `ree_core/` for provenance/source-tagging machinery (`provenance`, `reality_coherence`, `is_imagined`, `source_tag`) — nothing resembling a hippocampal-trace-based "real vs. imagined" tag exists. `e3_selector.py`'s `reality_scorer` / `compute_reality_cost()` scores trajectory *viability/smoothness*, not provenance of the observation that produced a given `z_world` state. The Gaussian-noise-replay proxy EXQ-135 built by hand remains the best available approximation — same limitation as March. Its floor-failure is still explained by §1b (shared with EXQ-129: no harm-training-pressure in any arm), independent of whether the reality-coherence manipulation itself is a good proxy.

---

## 2. Claim-layer mapping (ARC-017)

`claims.yaml`: `claim_type: architectural_commitment`, `status: provisional`, `live_status.reading: provisional` (as_of 2026-07-11), `depends_on: [INV-008, INV-012, ARC-004, ARC-005, ARC-003, ARC-015]`. `claim_evidence.v1.json`: `experimental_confidence=0.33` (2 mixed FAILs, both these runs), `literature_confidence=0.789` (2 supporting lit entries, connectome + vestibular anatomy — see §3), `overall_confidence=0.559`, quadrant `plausible_unproven`.

**Did the experiments let the claim express itself?** No, for two independent, sufficient reasons: (a) neither arm of either experiment ever created training pressure for `z_world` to represent harm at all (§1b — a defect in the shared measurement scaffold, not the manipulation), and (b) EXQ-129 specifically never implemented the "typed routing to a dedicated encoder" mechanism it claims to test (§1c — a defect in that experiment's manipulation itself). Both defects independently prevent either C1 floor-failure from being read as evidence about ARC-017's truth value.

**`claim_ids` accuracy:** correct — single claim, both experiments genuinely aimed at ARC-017's two named facets (stream-type routing, reality-coherence). No mis-tagging.

---

## 3. Biological-reference triage

ARC-017 corresponds to well-documented neuroanatomical stream separation: nociceptive/exteroceptive pathways are anatomically distinct from general somatosensory/visual pathways in mammals, and "reality-coherence" (distinguishing genuinely perceived from internally-generated/imagined content) maps to the reality-monitoring literature (Johnson & Raye) and hippocampal source-memory mechanisms. This grounding is **already on file and strong**, not a formal-definition import needing a fresh `/lit-pull`:

- `2026-03-17_three_streams_haak2018` (confidence 0.86): large-sample HCP resting-state fMRI (n=470), data-driven triple dissociation of visual pathways with a probabilistic atlas of 22 areas — direct connectome evidence for three anatomically distinct pathways matching REE's three error channels.
- Lopez & Blanke vestibular-anatomy review (confidence 0.85): thalamocortical vestibular system, multiple relay nuclei, PIVC as core cortical region — grounds the VESTIBULAR stream tag specifically.

`lit_confidence=0.789` reflects this. **No new `/lit-pull` is recommended** — the stream-typing facet's biological grounding is solid; what was missing was a proxy that actually implemented the mechanism, not literature support for it.

**Does the failure resemble a missing-dependency signature?** For EXQ-129: no — the biology is not in question; the *implementation* of the typed pathway in this specific 2026-03 proxy is what was missing, and it has since been built (§1d) for unrelated reasons. For EXQ-135: partially — genuine hippocampal-trace-based provenance tracking is itself an unbuilt dependency (§1e), which is closer to a real missing-substrate signature, though the shared §1b defect means even a correct provenance mechanism would need the detached-gradient issue fixed to be fairly tested.

---

## 4. Four-layer diagnosis

| Layer | V3-EXQ-129 (stream tags) | V3-EXQ-135 (reality coherence) |
|---|---|---|
| Claim alignment | unclear — test never let the claim express itself | unclear — same |
| Biological reference | clear, strongly supported (connectome n=470 + vestibular anatomy, already on file) | clear for the general architecture; no dedicated lit for "reality-coherence" mechanism specifically, but not the binding constraint here |
| Prerequisites (dependency) | **missing at run time, now present** — MECH-099 lateral head + SD-010 `harm_eval_z_harm` did not exist in March; both exist and are validated today (~40 experiments) but were never applied to ARC-017 | **still missing** — no hippocampal-trace-based provenance/imagined-vs-real tracking substrate exists in `ree_core` today |
| Implementation completeness | **defective** — docstring claims typed routing to a z_harm encoder; code silently drops `harm_obs` instead; no z_harm encoder exists in the script at all | matches its own (limited) design intent — the noise-injection proxy does what it says, it's just a weak proxy |
| Environment adequacy | adequate — CausalGridWorldV2 provides genuine harm-relevant signal (ABLATED arm's nonzero gap proves the raw channel carries information) | adequate |
| Measurement adequacy | **under-instrumented, decisively** — `harm_eval_head` trained on `.detach()`ed `z_world`; no arm of either experiment gives the encoder any harm-relevant training pressure | **under-instrumented, decisively** — identical detached-gradient defect, inherited from the same measurement scaffold |
| Integration adequacy | n/a — single-agent, no cross-module coupling question | n/a |
| Scale/capacity | open, secondary question — whether 400 episodes with a *correctly wired* harm-training objective clears a 0.04 gap floor is untested; should be calibrated in the redesign, informed by the SD-070/V3-EXQ-728 precedent for validating training sufficiency before trusting a discrimination floor | same open question, secondary to the shared measurement defect |

---

## 5. Cluster pattern

**Not two independent bugs — one shared structural defect (§1b) plus one experiment-specific implementation gap (§1c).** The shared defect (detached-gradient harm probe, present identically in both drivers) means neither experiment's intact arm was ever a fair test of *anything* about harm-representation quality — this alone is sufficient to explain both C1 floor-failures without invoking undertraining, ceiling, or genuine claim pressure. EXQ-129 carries an additional, independent defect (the "typed" arm never routes the channel it claims to route), which explains its wrong-direction C2 result on top of the shared floor problem. Read together: **this is a proxy-generation-era defect** (both experiments share a hand-rolled `_train_all_on_agent`-style loop, written before the shared substrate — `SplitEncoder.lateral_head`, `harm_eval_z_harm` — existed), not evidence that ARC-017's typed-stream or reality-coherence mechanisms are architecturally wrong.

---

## 6. Learning extracted

- **A floor-failing intact arm is not always the SD-070 "frozen encoder" pattern** — that precedent (V3-EXQ-728/875/882, confirmed 2026-07/08) is specifically a *zero-gradient* defect (tensor deltas of exactly `0.000e+00`). Here the encoder trains throughout (`total_loss.backward()` reaches every "standard" param including the world encoder); the defect is that *no arm's training objective ever targets the property being measured*. Both are "the intact arm never had a fair chance," but for structurally different, independently-diagnosable reasons — worth distinguishing explicitly rather than pattern-matching to the first precedent found.
- **A docstring claiming a mechanism is implemented is not evidence that it is.** EXQ-129's docstring asserted "harm_obs routed to z_harm encoder" in four separate places; the actual code routes it nowhere. Reading the driver source directly (not just the manifest/summary) was necessary and sufficient to catch this — the manifest's own `summary_markdown` never mentions it either, because the summary is generated from the same (wrong) mental model as the docstring.
- **Substrate built for one claim can silently leave a sibling claim un-retested indefinitely.** MECH-099/SD-010 have been validated by ~40 experiments across many claims since March, but nothing flagged that ARC-017 — the claim whose own hypothesis this substrate most directly instantiates — was never re-run against it. There is no standing mechanism that surfaces "substrate X now exists and claim Y (whose FAIL predates X) has never been retested with it" — this is a real gap; a future session could consider whether `check_epistemic_category_completeness.py`-style tooling should also flag claims with a stale FAIL under substrate that has since matured, though this is out of scope to build here.
- **Bit-identical results across two differently-named experiments is itself a diagnostic signal**, not a coincidence to explain away — it directly proves the "intact" condition in both cases is the same computation, which is what made the shared-defect reading legible rather than merely suspected.

---

## 7. Repair pathway / routing (user-confirmed, interactive gate 2026-08-07)

**Diagnosis category (work-graph debt vocabulary):**
- V3-EXQ-129: `complicated (buildable)` in the narrow sense that the needed substrate (MECH-099/SD-010) already exists — this is "wire an existing, validated mechanism into a new experiment," not a build from scratch, and not a probe-gated unknown.
- V3-EXQ-135: `complex (probe-gated) / puzzle (known rules)` remains open for the *reality-coherence* facet specifically (whether genuine provenance-tracking substrate is ever built is a separate, larger design question deferred beyond this autopsy) — but the *immediate* fix (repair the shared measurement defect, retest with the existing noise-injection proxy) is itself a known, buildable redesign, not something requiring a new spike.

**V3-EXQ-129 — routing: `/queue-experiment`, new EXQ number** (major redesign — the mechanism under test changes from an unimplemented ad-hoc proxy to the real MECH-099 lateral-head / SD-010 `harm_eval_z_harm` pathway, which is a different mechanism, not a bug-fix letter on the same one). Redesign must:
1. Use `SplitEncoder(harm_dim>0)`'s `lateral_head` to produce a genuine `z_harm` from hazard+contamination channels for the "typed" arm, and evaluate via `harm_eval_z_harm()`, rather than the drop/merge proxy.
2. Fix the shared detached-gradient defect (§1b) — either give `harm_eval_head`/`harm_eval_z_harm_head` training a path that creates real pressure on the encoder producing the state being evaluated, or explicitly justify keeping it detached and calibrate the floor threshold accordingly. This should not be silently inherited from the old proxy.
3. Reuse the existing precedent scripts (`v3_exq_098_mech099_three_stream.py`, `v3_exq_056_sd010_harm_stream_baseline.py` and family) as design templates — this substrate is well-trodden, not novel.
4. Given the SD-070 precedent (V3-EXQ-728/875), validate training sufficiency (e.g. a throwaway probe confirming the relevant encoder actually moves and the floor is achievable in principle) before trusting a floor-failure as informative.

**`recommended_substrate_queue_entry.action: none`** — no new substrate build required; MECH-099/SD-010 already exist and are validated by ~40 other experiments. The gap was never having applied them to ARC-017, not their absence.

**V3-EXQ-135 — routing: `/queue-experiment`, same-facet retest (alphabetic suffix, V3-EXQ-135a)** — same scientific question (does reality-coherent training improve harm discrimination vs. contaminated training), implementation fix only:
1. Fix the shared detached-gradient defect (§1b), same as above.
2. Keep the existing noise-injection proxy for the ABLATED arm (no better provenance-tracking substrate exists to swap in — see §1e); this remains the practical test available today.
3. Do not treat this facet as `/implement-substrate`-gated — building genuine hippocampal-trace provenance tracking is a much larger, separate architectural question that this autopsy does not resolve and does not recommend queuing as a prerequisite. The corrected proxy, once the shared defect is fixed, is a legitimate (if imperfect) test in the interim.

**No refusal applies.** This is the first autopsy for ARC-017 (re-derive brake count = 0 for this claim, confirmed via `granularity_debt_cluster.py ARC-017` → 0 tagging targets) and the recommended category (`measurement_test_design_defect`) is explicitly excluded from the re-derive brake's R3 counting rule (only `substrate_ceiling` counts) — neither retest is a letter circling a ceiling.

**Granularity-debt trigger: does not fire.** `granularity_debt_cluster.py ARC-017` → 0 tagging targets (this is the first autopsy for this claim; no recurrence pattern exists yet).

**Fan-out (GOV-FANOUT-1): not applicable.** Neither target is a discrimination bottleneck between live rival hypotheses about ARC-017's mechanism — both root causes are established directly from source-code archaeology, not inferred from ambiguous data requiring a portfolio of probes to disambiguate.

---

## 8. Draft `evidence_quality_note` (for `/governance` to apply, NOT written by this skill)

> [2026-08-07 failure-autopsy, V3-EXQ-129 + V3-EXQ-135, confirmed `failure_autopsy_ARC-017-EXQ-129-135_2026-08-07`]: Both 2026-03-29 FAILs reclassified `non_contributory` / `measurement_test_design_defect` — neither is evidence against ARC-017. Root cause, verified against driver source: (1) both experiments train `harm_eval_head` on a `.detach()`ed `z_world`, so no arm of either experiment ever gave the world encoder training pressure to represent harm — the ~0.015 floor-failure is the expected size of a purely incidental signal, not evidence about either manipulation, and is NOT a training-duration/warmup problem (more episodes would not fix a training-*objective* gap). (2) V3-EXQ-129's "TYPED_TAGS_ON" arm never implements typed routing despite its docstring's claim — `harm_obs` is read from the environment and silently discarded, with no `z_harm` encoder anywhere in the script; this alone explains the wrong-direction C2 result (ABLATED > ON). The two "intact" arms across both experiments are bit-identical (confirmed to 15 significant figures), confirming both experiments share one deterministic underlying measurement rather than being independent results. Substrate now exists (since March) to correctly test the stream-typing facet — `SplitEncoder.lateral_head` (MECH-099) + `harm_eval_z_harm()` (SD-010), validated by ~40 other experiments, never applied to ARC-017 (`claim_evidence.v1.json` confirms these two March FAILs remain the claim's only experimental entries). Biology is strongly supportive and already on file (`lit_confidence=0.789`: HCP n=470 connectome dissociation + vestibular anatomy review) — no lit gap. Reality-coherence (EXQ-135) still lacks a genuine provenance-tracking substrate; the noise-injection proxy remains the practical test available. Routed: V3-EXQ-129 → new EXQ number using the existing MECH-099/SD-010 pathway (no substrate build needed, just correct wiring); V3-EXQ-135 → same-facet retest (135a) with the shared measurement defect fixed. **For INV-012's sake** (which the digestion note that spawned this autopsy flagged as a concern, since ARC-017's reality-coherence lane is architecturally relevant to responsibility/commitment gating): neither FAIL constitutes genuine negative evidence against ARC-017's reality-coherence lane — both are non-contributory test-design artifacts, so INV-012 is not resting on a weakening result here, stale or otherwise. Stays `provisional`; `v3_pending` not applicable (was not set).

---

## 9. Dry-run / recording checks (Step 2a / Step 2)

- `dry_run_checked: true`, `excluded_dry_run_ids: []` — both targets clean (confirmed both via `check_dry_run_citations.py` and via direct code-path proof that `--dry-run` cannot produce a manifest for either script).
- `ree-v3/validate_recording.py`: 8 always-core gaps each (`recording_schema`, `substrate_hash`, `substrate_commit`, `machine`, `machine_class`, `elapsed_seconds`, `config`, `seeds`) — pre-Recording-Standard archival manifests, acknowledged in-source (`MANIFEST_WRITER_EXEMPT`). Not a blocker: full metrics + driver source were sufficient for this diagnosis; no re-run is being requested to recover a missing readout, so this is not routed as a "recording gap" fix.

## 10. Frozen hypothesis-space ledger (Step 9b)

**Skipped, deliberately.** Both targets carry `recommended_evidence_direction` (`non_contributory`), technically meeting condition (ii) of the Step 9b trigger, but this is the skill's own named skip case: a reclassification of old FAILs into non-contributory, not a discrimination event that opens or resolves a rival hypothesis set. No `fanout_recommendation` is emitted. Checked `hypothesis_space_registry.v1.json` for an existing question covering ARC-017 or this design (by claim id and by title/short_title substring match on "stream"/"reality"): 28 questions total, 2 substring matches (`decomposition_scale_heterogeneity`, `q081-cross-stream-shared-organisation`), neither covering ARC-017 or this proxy design. Registering a new question solely to record "2 non-contributory runs, resolved as measurement defect, no rival hypotheses" was judged not worth the denominator overhead — skipping cleanly per the skill's own guidance (matching the V3-EXQ-875 precedent).

## 11. Session notes

- **Coordination-plane pause claim failed arbitration** (exit 3): `WORKSPACE_STATE.md` is already claimed by session `lucid-spence-efbee6` (`predictive-harm-success-assessment thought intake`, claimed 2026-08-07T17:09:08Z, earlier than this session's pause attempt at 17:14:51Z). Per CLAUDE.md's arbitration rule, this session is not the owner and did not proceed with the pause claim (nothing was written beyond the initial artifact-scope claim, which succeeded independently and does not name `WORKSPACE_STATE.md`). This autopsy does not touch `claims.yaml`, `substrate_queue.json`, or `experiment_queue.json` directly — those writes are left to `/governance` per the skill's analysis-only scope — so the lack of a coordination-plane pause does not affect this autopsy's own correctness. The `WORKSPACE_STATE.md` Recent Work line at session close (Step 10) will be a narrow structural append, re-reading immediately before editing, consistent with the "different task, same shared log" overlap the umbrella CLAUDE.md's arbitration rule anticipates for non-identical work on a shared log file.
- The active claim on `docs/claims/claims.yaml` / `docs/assets/data/claims.json` / `manual_proposals.v1.json` / `WORKSPACE_STATE.md` held by the spawning digestion session (`cool-torvalds-a82359`) does not conflict with this autopsy's own resources (the two artifact files + `hypothesis_space_registry.v1.json`, none of which that session claims) — this autopsy does not write to `claims.yaml` in any case (analysis-only, per skill scope).

---

*Adjudicated by session `eager-wilbur-caae55` (worktree). Inputs: EXQ-129/135 flat + run-pack manifests; `ree-v3/experiments/v3_exq_129_arc017_stream_tag_pair.py` and `v3_exq_135_arc017_reality_coherence_pair.py` (full source read); `ree_core/latent/stack.py` (`SplitEncoder`); `ree_core/predictors/e3_selector.py` (`harm_eval_z_harm`, `harm_eval_lateral`); `claims.yaml` ARC-017/INV-012; `claim_evidence.v1.json` ARC-017 entry; `granularity_debt_cluster.py ARC-017`; `check_dry_run_citations.py`; `ree-v3/validate_recording.py`; `hypothesis_space_registry.v1.json`; precedent autopsies `failure_autopsy_V3-EXQ-728_2026-07-20`, `failure_autopsy_V3-EXQ-875_2026-08-03`, `failure_autopsy_V3-EXQ-882_2026-08-03` (SD-070 pattern, read for method — not directly applicable here, see §6). Per CLAUDE.md, `/failure-autopsy` does not mark runs reviewed — `review_tracker.json` is left to the governance walk.*
