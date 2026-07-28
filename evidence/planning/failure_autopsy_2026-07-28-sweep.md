# Failure Autopsy Sweep — 2026-07-28

**Session:** `relaxed-montalcini-eb02e1` (worktree). **Generated:** 2026-07-28T21:04:30Z.

## Scope

Regenerating `pending_review.md` from current disk state (full derive chain: `sync_v3_results.py` → `build_experiment_indexes.py` → `generate_pending_review.py`) surfaced 13 FAIL + 2 flagged diagnostics since the last governance walk (2026-07-26). Several of the original items turned out to already be autopsied in prior confirmed sessions from 2026-07-26:

- `failure_autopsy_batch-822a-826-817a-827_2026-07-26` — covers 826 (original), 822a, 817a, 827 (original). Routed same-question redesigns for 826, 822a, 827; routed `governance-demotion` for 817a (still unapplied pending a governance walk — noted for completeness, no new autopsy needed).
- `failure_autopsy_V3-EXQ-824_2026-07-26` — covers 824 (original). Routed a redesign (824a).
- `failure_autopsy_816-820-policy-decomposition-cluster_2026-07-26` + `failure_autopsy_V3-EXQ-816b_2026-07-26` — cover 816, 820, 816b. Routed environment-axis dose escalation.

The redesigns those autopsies called for produced the lettered/follow-on runs this sweep actually diagnoses: **822b, 826a, 824a, 827a, 828, 816d, 830, 829, 831** — 9 targets, each getting its own full four-layer analysis below, per the user's explicit instruction that a landed fix does not exempt the follow-on run from full attention (it may still find a genuine gap, even where the specific bug that motivated the redesign is confirmed fixed).

All 9 run_ids were checked against `check_dry_run_citations.py` — 0 dry-run hits, 14/14 clean (the check covered all candidate run_ids including the already-autopsied originals for context).

---

## 1. V3-EXQ-822b — SD-078 / SD-082

**Facts.** 822a (SD-082-consumer re-run of superseded 822) again found `propagation_non_vacuity` exactly 0.0 on both arms despite a strong, non-degenerate upstream chain (cue-centered pool differentiation → differentiated rule_state, 0.644). The prior confirmed autopsy routed `implement-substrate`: amend SD-082 with head-internals instrumentation. 822b is that follow-on — adding two per-tick diagnostics (`hidden_dead_relu_frac`, `rule_summary_magnitude_ratio`, gated by `head_diag_samples_sufficient`) and four **unconditional** phase-boundary weight-norm snapshots.

**Why flagged.** `head_diag_samples_sufficient` fails: worst cell `ARM_OFF/seed101` recorded zero per-tick head-diagnostic samples (rule inactive there during measurement). This gates only the two new tick-sampled diagnostics.

**The load-bearing finding, unaffected by the flag.** `on_last_layer_weight_delta_init_to_p1_mean = 0.0`, `diagnostic_flags.head_untrained_last_layer_static = true` — an unconditional parameter-norm read, not gated by tick-sampling. The REINFORCE-trained head's last linear layer moved **exactly zero** from init through the 70-episode P1 phase, in both 822a and 822b.

**Claim layer.** SD-078 and SD-082 (both `candidate_substrate_landed`, `design_decision`) — implementation questions about the substrate itself.

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | Downstream behavioral consequence still untested. |
| Biological reference | clear | Corticostriatal rule→action gating requires a trained, sensitive mapping. |
| Prerequisites | present | Upstream chain fully validated and healthy. |
| Implementation | **absent** | Last layer receives zero REINFORCE gradient. |
| Environment | adequate | |
| Measurement | partial | Tick-sampled diagnostics under-sampled on one cell; unconditional weight-norm reads fully sampled. |
| Integration | isolated | Break is inside the trained head's own optimizer/gradient path. |
| Scale | adequate for readable metrics | |

**Learning:** SD-082's fix resolved the mechanism it targeted (clamp saturation) but a second, independent defect sits upstream in the same head. The 822→822a→822b chain progressively narrowed the diagnosis — consumer absent → input-stage broken → output-stage fixed but gradient never reaches the layer — rather than repeating the same finding.

**Recommended:** `competence_implementation_gap`, `non_contributory`, routing **`implement-substrate`** — amend SD-082's substrate_queue entry to trace why REINFORCE never updates `rule_bias_head`'s last layer (optimizer param registration / gradient flow through the tanh bound / whether `ADV_MIN_THRESHOLD=0.005` ever fires). Secondary: bias P2 sampling so `ARM_OFF/seed101` clears the sample floor for the other two diagnostics. Re-derive brake: SD-078 has 2 prior targets, neither `substrate_ceiling` — does not fire, but this is the third same-shape finding in the chain.

---

## 2. V3-EXQ-826a — MECH-244

**Facts.** 826's E1-tick bug (random-action rollout never called `agent.act*()`, so `compute_prediction_loss()` returned a permanent zero-gradient stub) is confirmed **fixed**: `pe_precision_manipulation_took` now reads 2.06 (≥1.5 floor). This is the first genuine (non-buggy) readiness read for MECH-244.

**But** two of three readiness gates still fail: `world_model_converged_phaseA_control` (0.152 vs 0.25) and `regime_change_disconfirms_control` (0.966 vs 1.15), despite 240,000 E1 ticks.

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | First genuine test attempt. |
| Biological reference | clear | Precision-weighted PE gating, well-grounded predictive-processing mechanism. |
| Prerequisites | present | |
| Implementation | **complete now** | Fix confirmed working. |
| Environment | adequate | |
| Measurement | adequate | Readiness gates caught a real shortfall, not an artifact. |
| Integration | isolated | |
| Scale | possibly insufficient | Non-trivial tick count but convergence *ratio* still under floor — training-budget/regime-shape question, not yet a ceiling. |

**Recommended:** `standard`, `non_contributory`, routing **`queue-experiment`** for 826b — extended phase-A budget and/or sharper regime-B contrast. Re-derive brake: does not fire (first genuine attempt). Flag for next time: if 826b fails these same two gates near-identically, that's the trigger to stop dose-escalating.

---

## 3. V3-EXQ-824a — Q-081

**Facts.** 824's defect (`use_invalidation_trigger` alone has no causal reach) is confirmed fixed at the reach-check level: `landmark_arm_behavioural_reach` now reads MET (via `use_anchor_sets=True`, mirroring INV-091's working fix). But the new sanity check, `arm_statistics_not_degenerately_bit_identical`, still fails — `rv_primary` is bit-identical across all 5 valid seeds, **despite** the reach-check passing.

**Why this matters.** `rv_primary` is a joint statistic over `z_world` (reached via `use_anchor_sets`, confirmed working for INV-091's different stream pairs) and `operating_mode` (the salience coordinator's mode-probability computation). The `REACH_CONSUMERS` "and/or" check confirms *a* reach path exists, not that it reaches the *specific* pair this run measures.

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | |
| Biological reference | n/a | Q-081 is a cross-stream-organisation question. |
| Prerequisites | partial | z_world reach confirmed; operating_mode sensitivity unconfirmed. |
| Implementation | partial | Reach-check is a coarse, blanket proxy. |
| Environment | adequate | |
| Measurement | **the reach-check itself is under-specified** — core finding | |
| Integration | n/a | |
| Scale | adequate | |

**Recommended:** `measurement_test_design_defect`, `non_contributory`, routing **`implement-substrate`** — amend `q081_landmark_removal.py`'s `assert_behavioural_reach` to check reach against the specific measured pair (add `use_per_region_vs=True` and re-verify, or build a pair-specific assertion). Re-derive brake: does not fire, but this is the **second** consecutive same-shape failure (bit-identical arms) on Q-081.

---

## 4 & 5. V3-EXQ-827a and V3-EXQ-828 — INV-091

**827a.** 827's tick-rate/sampling-density confound (forcing lockstep by collapsing all stream rates to 1) is confirmed fixed by this phase-sync redesign — the directional reversal seen in 827 is gone (decouple 0.224 ≈ intact 0.223 < lockstep 0.324). Neither load-bearing criterion passes, on real (non-degenerate) data. `null_validation.checked: false` for every arm/seed — needed 2064–2576 steps, got 258–1099.

**828.** Self-labeled `weakens` already in the manifest. `C1` passes, `C2` fails: `intact` sits in the middle of the ranked-similarity pack (`intact_vs_min: -0.005`, `intact_vs_max: +0.007`), while an *ablation* (`residue_off`) has the best composite reward — directly contradicting INV-091's Goldilocks-band prediction. Same null-validation gap: needed 2464–2848 steps, got 1500.

**Campaign-wide finding:** all three INV-091 runs (827, 827a, 828) have never once cleared the surrogate-null validation.

| Layer | Status (campaign-level) | Notes |
|---|---|---|
| Claim alignment | unclear (827a) / weakens (828) | |
| Biological reference | clear | Cross-stream phase-coupling as integration substrate. |
| Prerequisites | present | Tick-rate confound fixed. |
| Implementation | complete for the manipulation | |
| Environment | adequate | |
| Measurement | **systematically under-powered** | Null validation never clears — every run needs ~2–2.8x more steps. |
| Integration | n/a | |
| Scale | insufficient for null, adequate for ablation-contrast | |

**Resolved per user's confirmation:** Q-081's own adjudication logic treats ablation-contrast as sufficient on its own ("clearing the null is necessary and nowhere near sufficient"). INV-091 follows the same convention here — 828's `weakens` stands on the ablation-contrast alone; the null-validation gap is recorded as a standing recording/design note, not a blocker.

**Recommended:** 827a → `standard`/`non_contributory`, routing `queue-experiment` for a longer 827b (≥2576 steps). 828 → `standard`/`weakens`, routing `governance-demotion`-ready. Both: recommend a substrate_queue entry bumping the INV-091 driver family's default step budget to ≥2848 so the null actually validates going forward.

---

## 6 & 7. V3-EXQ-816d and V3-EXQ-830 — MECH-321 / ARC-070

**816d.** Third consecutive environment-axis escalation (816 → 816b → 816d). Forward-PE: 0.0080 → 0.0086 → 0.0087 — each within noise of the last, each still short of the 0.01 discrimination floor. The run's own metrics explicitly record `predecessor_816b_off_pe_mean_worst` for direct comparison.

**830.** A separate diagnostic testing whether the "slow" decomposition pathway ever engages. Result: zero "slow" fires in 2393 sweeps across both arms; ON and OFF produced *bit-identical* behavior (`net_harm_per_step_mean` identical to 15 decimals). `outcome: PASS` but the manifest's own `evidence_direction: non_contributory` already flags this as vacuous — all positive controls green, the actual test-relevant pathway never exercised.

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | Core prediction still untestable — environment never produces the trigger. |
| Biological reference | clear | Zacks 2007 / Schapiro 2017 faithfully operationalised. |
| Prerequisites | present | MECH-288 substrate landed, fires abundantly once triggered. |
| Implementation | complete | |
| Environment | **the identified bottleneck, now saturating** | Three escalations moved PE by <0.0007 total. |
| Measurement | adequate | |
| Integration | isolated | |
| Scale | n/a | |

**Recommended:** both `standard`/`non_contributory`, routing **`queue-experiment`** with a **`fanout_recommendation`** (GOV-FANOUT-1) rather than a fourth environment escalation:
- **H-representation-axis**: recompute forward-PE at finer granularity/different normalization on the *same* environment config.
- **H-algorithm-axis**: lower the R1 V_s-drop trigger's 0.01 floor (an engineering parameter per ARC-070's own registration, not literature-derived).

Re-derive brake: does not fire (still `standard`, 0 confirmed ceiling hits for either claim) — but three same-axis attempts converging within noise of each other is exactly the GOV-FANOUT-1 signal.

---

## 8. V3-EXQ-829 — MECH-323 / MECH-324

**Facts.** First test of MECH-324's registered rapid-reacquisition falsifier. `on_arm_any_revived: true`, `off_arm_any_revived: false` — real support for MECH-323's retention-not-erasure structure. But the rate prediction falsifies in the **wrong direction**: median 90 reps vs predicted ~5 (`f_reacq=0.25 × R_min=20`), slower even than original formation (20 reps).

**The verdict-aliasing finding.** The script's own pre-registered authoring probe (disclosed *before* running) predicted this exact pattern: `r_reacq` flat at 28/46/90 for `W=30/50/100`, identical across every tested `f_reacq` (1.0, 0.5, 0.25, 0.1). The manifest reproduces it precisely. **The reduced-repetition-bar lever is inert by construction** — reacquisition timing is dominated by how long the sliding-window variance takes to clear the dissolution episode's own contamination (`W`), not by the counter-threshold `f_reacq` is meant to lower.

**User-contributed reframe, verified buildable.** Biological rapid reacquisition (Barnes 2005, Bouton 2012) comes from paradigms with **sleep between real trials/sessions**. If biological "rapid" reacquisition is achieved via offline consolidation *compressing the real-trial requirement*, rather than an intrinsically lower repetition threshold, then `f_reacq` — a repetition-count multiplier — targets the wrong lever entirely, independent of (and in addition to) the confirmed W-gating defect. Checked: `use_chunk_replay_origin_path` (MECH-322's sleep-replay carve-out) is fully wired (`ree_core/agent.py:1351-1352`, `ree_core/policy/policy_chunking.py:722/1303`, `ree_core/utils/config.py:3774/5714/6925`), depends on SD-017 (sleep-phase infrastructure, `status: stable`), and 829 explicitly disabled it (`use_chunk_replay_origin_path=False`, line 363). MECH-322 itself is `candidate/v3_pending` as a *claim* but the substrate plumbing exists — a follow-up is `complicated (buildable)`, not gated on missing substrate.

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | strengthened (MECH-323) / weakened on the specific quantitative prediction (MECH-324) | |
| Biological reference | clear, with a load-bearing divergence | f_reacq operationalises rapid reacquisition as repetition-count reduction; biology's paradigms have sleep between sessions — a mismatch in what's being modeled, not just a wrong parameter value. |
| Prerequisites | present for tested mechanism; **untested for sleep-replay** | MECH-322 substrate wired, deliberately disabled here. |
| Implementation | confirmed gating defect | Crystallisation-counter reset dominated by window-contamination clearing, not by f_reacq. |
| Environment | n/a | Isolated operator-level test by design. |
| Measurement | thorough, self-aware | Pre-registered verdict-aliasing check anticipated and confirmed this exact result. |
| Integration | isolated by design | Correctly scoped per 810's finding that the accumulator is silent under full-agent control. |
| Scale | adequate | 6 seeds, multiple W/severity/f_reacq combinations. |

**Recommended:** `competence_implementation_gap`, `evidence_direction_per_claim: {MECH-323: supports, MECH-324: mixed}`. **Two routings**: (1) `implement-substrate` — decouple the crystallisation-counter reset from raw window-contamination time so `f_reacq` has causal effect; (2) `queue-experiment` for 829a with `use_chunk_replay_origin_path=True`, explicitly framed as testing whether offline-replay corroboration — not a lower repetition threshold — is the real mechanism behind biological rapid reacquisition. Registered as a **newly discovered candidate missing prerequisite** (sleep-replay engagement), not merely a mixed numeric verdict.

---

## 9. V3-EXQ-831 — MECH-466

**Facts.** First test. All four preconditions clear cleanly. Load-bearing criterion fails on real data: event-minus-clock delta = -0.091 vs a 0.171 floor. Self-labeled `weakens`, correctly per the project's non-standard-directions convention. Explicitly scoped **waking-only** (`use_sleep_loop=False`); its own `scope_note` calls itself "sibling of V3-EXQ-824" and defers the sleep-phase-transition landmark class (Outcome E).

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened | Coordination no tighter around events than clock points, waking-only. |
| Biological reference | clear | Event-segmentation-locked coordination, reasonable operationalisation. |
| Prerequisites | present | MECH-288 boundary detection landed and well-behaved. |
| Implementation | complete | |
| Environment | adequate | |
| Measurement | thorough | Explicit non-degeneracy band, union-event sufficiency check. |
| Integration | isolated | |
| Scale | adequate | 3/3 seeds valid. |

**Recommended:** `standard`, `weakens`, routing **`governance-demotion`**-ready as-is — complete, self-consistent, no further diagnostic work needed. **Read alongside 829**: this strengthens a cross-claim pattern — sleep/offline-consolidation engagement may be a load-bearing missing prerequisite spanning MECH-324 (rapid reacquisition) and MECH-466 (Outcome E, explicitly deferred here). Worth prioritising a sleep-engaged lettered follow-up (`use_sleep_loop=True`) before MECH-466's full claim can be considered adequately tested.

---

## Cluster pattern

Three independent lettered-iteration campaigns (SD-078/082, MECH-244, Q-081/INV-091) each fixed their first identified bug, then hit a **second, deeper** gap on the same axis in their very next attempt — this is the expected and correct shape of progressive narrowing, not repeated failure:

- SD-078/082: consumer absent → input-stage broken → output-stage fixed but the trained layer receives zero gradient.
- Q-081: no reach path → a reach path exists but not to the specific measured pair.
- MECH-321/ARC-070: a third consecutive environment-axis escalation confirms the axis is saturated (816d), independently corroborated by 830's "slow never fires" finding.

Separately, 829's sleep-replay reframe (user-contributed) surfaces a new cross-claim theme: **offline consolidation may be a load-bearing missing prerequisite** spanning MECH-324 (rapid reacquisition, sleep-replay substrate-wired but disabled) and MECH-466 (event-relative coordination, explicitly waking-only tested, Outcome E deferred). This is worth surfacing to governance as a standing theme across the chunking/consolidation claim family, not a one-off finding.

## Interactive gate

Presented in full to the user (2026-07-28). User confirmed the overall analysis and added the sleep-replay reframe for 829 (verified buildable — MECH-322 substrate wired, SD-017 landed). Proceeded with the recommended default on the one remaining open item (INV-091's ablation-contrast-is-sufficient convention for 828, per Q-081 precedent, not separately objected to).

## Routing summary

| Target | Category | Direction | Routing |
|---|---|---|---|
| 822b (SD-078/082) | competence_implementation_gap | non_contributory | implement-substrate |
| 826a (MECH-244) | standard | non_contributory | queue-experiment |
| 824a (Q-081) | measurement_test_design_defect | non_contributory | implement-substrate |
| 827a (INV-091) | standard | non_contributory | queue-experiment |
| 828 (INV-091) | standard | weakens | governance-demotion |
| 816d (MECH-321/ARC-070) | standard | non_contributory | queue-experiment (fanout) |
| 830 (MECH-321/ARC-070) | measurement_gap | non_contributory | queue-experiment (fanout, shares 816d) |
| 829 (MECH-323/324) | competence_implementation_gap | mixed/supports | implement-substrate + queue-experiment |
| 831 (MECH-466) | standard | weakens | governance-demotion |
