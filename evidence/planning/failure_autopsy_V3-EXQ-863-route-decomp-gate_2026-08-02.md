# Failure Autopsy: V3-EXQ-863 (`vacuous_pass` diagnostic self-route) — corrective re-adjudication

**Generated:** 2026-08-02T23:11:59Z
**Scope:** single target, with a correction that bears on the sibling runs V3-EXQ-851/859/858
**Status:** confirmed (user-confirmed 2026-08-02: "Confirm and land as-is" — accept `measurement_test_design_defect`, confirm the substrate_queue fix recommendation, flag the sibling artifact's Section 2 for correction in `WORKSPACE_STATE.md` without editing it directly)
**Supersedes (for the 863 target only):** `failure_autopsy_V3-EXQ-847a-863_2026-08-02.md` / `.json` Section 2's reading of V3-EXQ-863 — its 847a target and routing are untouched by this finding, and that artifact itself has not been edited.

## 0. Why this autopsy exists, and why it revisits an already-`confirmed` sibling

`pending_review.md` (regenerated this session) flags `v3_exq_863_arc062_lateral_pfc_route_mech448_449_full_replication_20260802T121313Z_v3` in "Diagnostic adjudication required (self-route unverified)" — self-route label `mixed_partial_result_needs_expert_review`, adjudication `vacuous_pass`. That is this skill's canonical trigger.

Partway through this investigation I found that `failure_autopsy_V3-EXQ-847a-863_2026-08-02.md` (git `6965227b57`, committed ~50 minutes before this session began reading the manifest) had **already** adjudicated the same run, with status `confirmed`, concluding the `vacuous_pass` flag was miscalibrated and the true reading is a **clean, informative null** ("route_source has no causal effect... confirmed... rules out training-duration-dependence"). I read that artifact in full before finalizing anything here (Section 2 below).

Independently, before I found that artifact, I had already traced `modulatory_channel_route_range_mean` and `modulatory_channel_route_active_frac` down to their source in `ree_core/agent.py` because the vacuous-pass criteria (`mech448_ablation_discriminates: false`, `mech449_ablation_discriminates: false`) didn't explain *why* MECH-448 read alive-in-both-arms rather than reproducing V3-EXQ-851's claimed collapse. That trace surfaced a confirmed, mechanical wiring defect (Section 1c) that the other autopsy's per-seed table does not address and that changes the correct reading of both targets. I'm reporting it as a correction rather than silently overriding the `confirmed` artifact — per CLAUDE.md's arbitration and "read-modify-write contamination" doctrine, a landed conclusion from another session is not something to revert unilaterally; it's something to surface with the specific evidence and let the user adjudicate.

## 1. Facts

### 1a. Dry-run gate

`check_dry_run_citations.py` was not re-run standalone this session, but every run_id cited below (`v3_exq_863_...`, `v3_exq_851_...`, `v3_exq_654j_...`) was read directly from its manifest's top-level `dry_run` field: all `false`. `validate_recording.py --paths` on 863's manifest: OK, always-core complete (this only covers `substrate_hash`/`config`/`seeds`/`machine`/`elapsed_seconds` — see the recording-gap correction in 1b below for what it does *not* cover).

### 1b. V3-EXQ-863 as designed and as read by its own interpretation grid

Full P0=200/P1=90/P2=60 budget matching V3-EXQ-851's own schedule exactly (350 episodes/cell x 3 seeds x 2 arms), built to distinguish two readings 859's cheap short probe left open: (a) `modulatory_channel_route_source` has no causal effect on MECH-448/449, or (b) the effect is training-duration-dependent and 859's ~45-minute probe couldn't see it. Sample adequacy precondition: `min(n_p2_fresh_select)=1144` vs floor 600 — well-powered, not the failure mode here.

**Correction: `arm_results` is NOT missing from the manifest.** I initially (incorrectly) read only `interpretation`/`result` top-level keys from the run-pack copy and concluded the per-arm raw diagnostics were a recording gap. They are present in the **flat** manifest (`evidence/experiments/v3_exq_863_..._v3.json`, `result.arm_results`, 6 entries) — this was my own oversight mid-investigation, not a defect in the run. Correcting it here so it isn't miscited downstream.

The interpretation grid's label logic ANDs MECH-448 and MECH-449 liveness into a single `arm_engaged` boolean per arm, then routes to `mixed_partial_result_needs_expert_review` whenever the two mechanisms disagree *within* an arm (448 live, 449 dead) — which happens on every seed in both arms here (448: 3/3 live both arms; 449: 0/3 live both arms, `suppressed_per_tick_mean` exactly 0.0 in every cell). Decomposed per-mechanism, both reads are internally consistent and well-powered on their own terms; the compound-AND label design simply has no slot for "the two mechanisms cleanly diverge from each other but each is individually clean" — a labeling-grid coverage gap, not evidence of a muddled measurement. **This much I agree with the prior autopsy on.**

### 1c. The actual root cause — `e3_score_decomp_enabled` silently no-ops four of six routing channels

This is the finding that changes the reading. Traced directly in `ree-v3/ree_core/agent.py` and `ree_core/predictors/e3_selector.py`:

- `E3Selector.__init__` (`e3_selector.py:424`): `self.e3_score_decomp_enabled: bool = False` — defaults off, and **there is no `REEConfig` field that sets it**; the only way to enable it is `agent.e3.e3_score_decomp_enabled = True` as a post-construction statement (confirmed by grepping every driver script that ever sets it — all 20+ hits are `agent.e3.e3_score_decomp_enabled = True` lines, none is a `REEConfig.from_dims(...)` kwarg).
- `agent.py:6194`: `_bdc_lpfc: Optional[torch.Tensor] = None` (initialized, not yet populated).
- `agent.py:6718-6719`:
  ```python
  if self.e3.e3_score_decomp_enabled:
      _bdc_lpfc = lpfc_bias.detach().clone()
  ```
  `lpfc_bias` (`self.lateral_pfc.compute_bias(...)`, computed unconditionally just above) is only ever assigned into `_bdc_lpfc` when the diagnostic flag is on. If it's off, `_bdc_lpfc` stays `None` for the entire episode.
- `agent.py:7626-7635` (the actual routing branch):
  ```python
  elif _route_source == "lateral_pfc":
      _route_repr = _bdc_lpfc
  ...
  if _route_repr is not None:
      channel_route_bias = project_channel_range(_route_repr)
  ```
  Since `_bdc_lpfc` is `None`, `_route_repr is not None` is false, so `channel_route_bias` is **never computed** — it stays `None` for the entire `lateral_pfc` arm, functionally **identical to `route_source="none"`**, regardless of the nominal config.

The identical pattern gates `_bdc_gp` (`gated_policy`, `agent.py:6530-6531`), `_bdc_m295` (`mech295`, `agent.py:6909-6910`), and `_bdc_curiosity` (`curiosity`, `agent.py:6997-6998`) behind the same `if self.e3.e3_score_decomp_enabled:` check. Only `cand_world_summary` (a structurally different code path, `agent.py:7611-7617`) and `coherence` (gated on `_tp_bias is not None`, not the decomp flag, `agent.py:7460-7461`) are unaffected. **Four of six `modulatory_channel_route_source` values are silently inert unless a scriptwriter happens to also set an unrelated diagnostic-instrumentation flag** — nothing in `agent.py`'s own routing comment block (lines 7595-7606) or in `REEConfig`'s docstring for `modulatory_channel_route_source` mentions this prerequisite. One contract test comment (`tests/contracts/test_e3_score_bias_candidate_support.py:498`, `# populates _bdc_lpfc (agent.py gate)`) shows the coupling was known to *someone* at some point, but it never propagated into the routing code's own documentation or into a runtime assertion.

**Confirmed empirically, not just by code trace:** `grep -n "e3_score_decomp_enabled" experiments/v3_exq_851_...py experiments/v3_exq_859_...py experiments/v3_exq_863_...py` returns **no hits in any of the three scripts**. All three build their agent via `REEConfig.from_dims(...)` and never touch `agent.e3.e3_score_decomp_enabled` afterward. And the manifests confirm the predicted symptom exactly:

| Run | Arm | `modulatory_channel_route_range_mean` | `modulatory_channel_route_active_frac` |
|---|---|---|---|
| 863, seed 42/43/44 | ARM_LPFC | **0.0** (all 3) | **0.0** (all 3) |
| 863, seed 42/43/44 | ARM_NONE | 0.0 (all 3, expected — `none` routes nothing) | 0.0 (all 3, expected) |
| 851, seed 42/43/44 | ARM_OFF & ARM_ON (both use `route_source="lateral_pfc"` as a matched constant) | **0.0** (all 6 cells) | **0.0** (all 6 cells) — `route_ready: False` on every cell |

ARM_LPFC's range/active_frac reading **0.0 exactly, identical to ARM_NONE's**, is not noise or a marginal effect — it is the exact, deterministic signature of `channel_route_bias=None` on every tick. This also directly contradicts 851's own **declared expectation**, stated in its DV-symmetry section: "the routed 'lateral_pfc' bias is a per-candidate `[K]` vector (identity-routed), NOT a broadcast scalar" — a real per-candidate `[K]` vector with genuine variation would not produce an *exact* 0.0 range on every one of 6 cells; only a `None`/never-computed channel does.

**851's own C1g readiness gate caught exactly this, correctly, and 851 self-routed accordingly.** `lateral_pfc_route_range_supra_floor_and_sample_adequate_both_arms | met: False | measured: 0.0 | threshold: 2.0` in 851's own interpretation block — 851 correctly detected that its route wasn't demonstrably active and self-routed `substrate_not_ready_requeue`, **not** a confirmed collapse finding. 859's and 863's simplified interpretation grids dropped this specific readiness check (they only gate on `n_p2_fresh_select`, not on route range), so neither could self-catch the same defect — the diagnostic lineage lost a gate on the way from 851 to 859/863, and that gate turns out to be the one that would have caught this.

### 1d. What this means for the "851 found MECH-448 dead under lateral_pfc (0.0), alive under cand_world_summary in 654j (17.76)" premise

I pulled 851's and 654j's actual `arm_results` (both present in their flat manifests) to check this literally:

- 851's `f_eligibility_demotion_active_frac` ranges **0.24–0.58** across its 6 cells (not 0.0), and `f_eligibility_excluded_count_mean` ranges **17–28** (comparable to — not dramatically below — 654j's 17.76–29.09 range). Neither is "completely dead (0.0)" as characterized in 863's docstring.
- The one metric that *is* exactly 0.0 in 851 is `modulatory_channel_route_range_mean`/`route_active_frac` — i.e., the **route itself**, not MECH-448.
- 654j predates the `lateral_pfc`/`curiosity`/`gated_policy`/`mech295` routing feature's route-range instrumentation entirely (no `modulatory_channel_route_range_mean` field in its schema) and used `cand_world_summary` — the one route-source value that does **not** go through the `e3_score_decomp_enabled` gate, so 654j's routing genuinely worked.

Put together: **851 never validly tested `route_source="lateral_pfc"` at all.** Its own docstring's premise ("851 found MECH-448 dead specifically under lateral_pfc, vs alive under cand_world_summary in 654j") appears to conflate "the route itself measured 0.0" with "MECH-448 measured 0.0" — two different metrics that happen to share the literal value. The actual, substantive comparison (851 vs 654j) contrasts a run where the *claimed* manipulation (lateral_pfc routing) never executed against a run where a *different* manipulation (cand_world_summary routing) did — not a controlled test of route_source at all. 851 correctly flagged this uncertainty itself (`substrate_not_ready_requeue`); the docstring language in 859 and 863 that inherited "851 found MECH-448 dead under lateral_pfc" overstated 851's own, more cautious self-assessment.

### 1e. Substrate drift and config-mismatch, checked and ruled out as alternate explanations

Before finding the gating defect, I checked two other candidate explanations for the 851-vs-863 discrepancy, both negative:

- **Substrate drift.** `substrate_hash` differs between 851 (2026-08-01T11:08Z) and 863 (2026-08-02T12:13Z) — 4 commits touched `ree_core/` in that window (MECH-122 spindle content-packaging, SD-057 L7 dacc_goal_readout fix, SD-hazard-aware-policy-decomposition, ARC-071/MECH-090 E3-reselection short-circuit). All four are explicitly default-False/bit-identical-off per their own commit messages, and none of their new `REEConfig` flags appears in 863's driver. Ruled out as behaviorally relevant.
- **Config mismatch beyond the swept variable.** Diffed 851's and 863's `_make_agent` bodies field-by-field; all matched-stack constants align (comments differ, values don't). Not the explanation.

## 2. Where I agree and disagree with `failure_autopsy_V3-EXQ-847a-863_2026-08-02`

**Agree:** 847a's own finding (H4 measurement-aliasing refuted) is untouched by anything here — different target, different mechanism, not re-examined this session. Agree that 863's `vacuous_pass` flag is miscalibrated in the sense that the chosen label doesn't state a clean discrimination even though the underlying reads are individually well-powered (Section 1b).

**Disagree, with the evidence above:** Section 2 of that artifact reads the bit-identical arms as **confirming** "route_source has no causal effect" and **ruling out** duration-dependence, and extends this to reinterpret 851/858's duty-cycle variation as "seed-correlated, not manipulation-correlated." That reasoning treats bit-identical arms as diagnostic of a genuine null. Given `modulatory_channel_route_range_mean=0.0` exactly on the treatment arm — the same exact-zero signature 851's own (now-explained) C1g gate failure produced — bit-identical arms are at least as consistent with "the manipulation never fired" as with "the manipulation fires and has no effect," and the code trace in 1c shows definitively that it's the former: `channel_route_bias` is `None` on **every** tick of the `lateral_pfc` arm in both 851 and 863, by construction, independent of anything about MECH-448/449's true causal relationship to routing. The other autopsy's own per-seed table (which I could not initially locate — see 1b — and which does correctly reproduce the manifest's `arm_results`) does not include `modulatory_channel_route_range_mean`/`route_active_frac`, which is why this signature wasn't visible from the table alone.

**I have not touched or reverted anything the other autopsy did** — no claims.yaml write exists to revert (`claim_ids=[]` on both targets), and I have not edited `failure_autopsy_V3-EXQ-847a-863_2026-08-02.{md,json}`. This artifact is offered as a correction for the user to weigh, per CLAUDE.md's guidance for a contradicting finding on already-landed work.

## 3. Claim-layer mapping

`claim_ids=[]` on V3-EXQ-863, matching 851/859/858's own convention (diagnostic-purpose runs in this GOV-FANOUT-1 ARC-062/MECH-309 lineage don't move claim confidence directly). No claims.yaml write is implicated by this correction.

## 4. Biological-reference triage

Not load-bearing — this is a pure instrumentation/wiring defect in the modulatory-channel-routing control plane, not a question about whether a biological mechanism translation is sound. The underlying LateralPFCAnalog / rule-apprehension routing concept (SD-033a) is untouched; the bug is in how its computed bias reaches the accumulator, gated on an unrelated diagnostic flag.

## 5. Four-layer diagnosis

| Layer | Reading |
|---|---|
| Claim alignment | n/a — `claim_ids=[]` |
| Biological reference | not load-bearing |
| Prerequisites | **defect found**: `e3_score_decomp_enabled` (an unrelated diagnostic-instrumentation flag) silently gates whether `lateral_pfc`/`curiosity`/`gated_policy`/`mech295` channel routing ever reaches the modulatory accumulator |
| Implementation | the routing dispatch itself (`agent.py:7607-7635`) is correctly structured; the defect is the unstated cross-dependency on `_bdc_*` population, which is itself correctly gated *for its own diagnostic purpose* but was never meant to double as a functional precondition |
| Environment | n/a |
| Measurement | 863's own reads (MECH-448/449 per-arm) are individually well-powered and correctly computed; what's uninterpretable is the *causal attribution to route_source*, because route_source's own effect was never actually exercised |
| Integration | the routing feature and the diagnostic-decomposition feature are coupled in a way neither's own design intended — a genuine substrate integration defect |
| Scale | n/a — not a power/budget issue; a full 7.7h budget doesn't fix a `None` channel |

## 6. Learning extracted

1. **A precondition/readiness gate that a later, "simplified" script drops can be exactly the gate that would have caught the real defect.** 851's C1g (route-range readiness) correctly self-routed `substrate_not_ready_requeue`; 859 and 863 simplified the interpretation grid down to a sample-adequacy check only, losing the one signal that would have flagged the actual problem. Simplifying a diagnostic's own self-checks between iterations is not free.
2. **Bit-identical arms across a manipulation are not self-evidently a clean null — check whether the manipulation's own magnitude/range read as genuinely zero, not just whether the two arms match each other.** Two arms that are identical because the treatment never fired look identical to two arms that are identical because the treatment has no effect; only the raw pre-outcome instrumentation (route range here) distinguishes them.
3. **A diagnostic-instrumentation flag (`e3_score_decomp_enabled`, meant to expose a per-channel score breakdown for analysis) silently doubles as an undocumented functional precondition for four of six routing channels.** This is a design smell worth fixing at the substrate level, not just working around per-script — see the recommended substrate_queue entry below.
4. **A causal narrative that gets restated across a chain of docstrings (851 → 859 → 863) can drift from the originating run's own more cautious self-assessment.** 851 self-routed `substrate_not_ready_requeue`; by the time 863's docstring restates it, it reads as "851 found MECH-448 completely dead (0.0) under lateral_pfc" — a confirmed-finding framing 851's own manifest does not support.
5. **An autopsy session's own read is not automatically more trustworthy than a differently-scoped read of the same run — cross-check the raw per-arm fields the interpretation grid didn't surface, especially when the auto-flagged reason (`criteria_non_degenerate`) and the human-adjudicated reason for concurring don't independently corroborate each other via a third data source.**

## 7. Recommended routing (user-confirmed 2026-08-02 — Step 8)

**863 — evidence_direction: `non_contributory`** (unchanged — `claim_ids=[]`). **epistemic_category: `measurement_test_design_defect`**, NOT `standard`. Recommended `evidence_quality_note`: *"V3-EXQ-863 (and its predecessor V3-EXQ-859, and V3-EXQ-851's own lateral_pfc arm) never validly exercised `modulatory_channel_route_source='lateral_pfc'`: the routing branch's per-candidate bias is populated only when the unrelated diagnostic flag `agent.e3.e3_score_decomp_enabled` is set, which none of these three driver scripts do, so `channel_route_bias` stayed `None` throughout — confirmed via `modulatory_channel_route_range_mean`/`route_active_frac` reading exactly 0.0 on every cell of both runs, matching the code trace in `ree_core/agent.py:6718-6719`/`7626-7635`. The bit-identical MECH-448/449 statistics between the `lateral_pfc` and `none` arms are the expected artifact of the manipulation never firing, not a confirmed null result. Whether `route_source` has a genuine causal effect on MECH-448/449 remains OPEN — no valid test of it exists yet."*

**Substrate fix — `recommended_substrate_queue_entry.action: create`** (Section 9 JSON): decouple `_bdc_lpfc`/`_bdc_gp`/`_bdc_m295`/`_bdc_curiosity` population from `e3_score_decomp_enabled` (populate them unconditionally for routing purposes; gate only the *diagnostic exposure* — `last_score_decomp` / component trackers — behind the flag as originally intended), or at minimum raise/warn when `modulatory_channel_route_source` selects one of the four affected values while `e3_score_decomp_enabled` is False. Either fix removes the silent-no-op failure mode for every future experiment using these four route-source values.

**Follow-on experiment — recommend `/queue-experiment`, new EXQ number (not a lettered continuation of 863):** once the substrate fix lands, a genuinely valid `lateral_pfc`-vs-`none` ablation is still an open, answerable question — this is NOT the same question 863 already answered (863 answered nothing about route_source causality; it validated only that a broken channel produces bit-identical arms). Recommend reusing 863's design (full budget, same seeds) with the fix applied, plus **reinstating an explicit route-range readiness gate** (851's C1g pattern) so a future recurrence self-catches rather than silently passing.

**V3-EXQ-858 (currently suspended) — recommend it REMAIN suspended, and flag it for a targeted check, not resumption.** 858 reuses the "IDENTICAL lateral_pfc-routed + MECH-448/449-active matched-stack config as V3-EXQ-851" per 863's own docstring. If 858's own design also routes through the `lateral_pfc` branch expecting it to function, 858 is likely affected by the identical wiring defect. This autopsy did not audit 858's own driver script or manifest in depth (out of scope for this session) — flagging for whoever next touches this family to check `modulatory_channel_route_range_mean` in 858's own arm_results before drawing any conclusion from its f_weight sweep that assumes lateral_pfc routing was functionally active.

**Re-derive brake:** does not apply — `claim_ids=[]`.

**Granularity-debt recurrence trigger:** does not apply — no claim-tagged `weakened` target in this family.

**GOV-FANOUT-1 hypothesis-space ledger:** no fan-out recommended (Section 9b skipped) — the correct next step is a single, unambiguous substrate fix (`complicated (buildable)`), not a multi-hypothesis discrimination.

## 8. Not investigated this session (flagged, not chipped — `/failure-autopsy` work per CLAUDE.md Session Land Protocol step 6)

- 858's own manifest/driver for the same route-range signature (see above).
- Full audit of every other experiment that has ever used `modulatory_channel_route_source` in `{lateral_pfc, curiosity, gated_policy, mech295}` without setting `e3_score_decomp_enabled` — the blast radius beyond this GOV-FANOUT-1 lineage is unknown and potentially large (this coupling has existed since at least V3-EXQ-571's introduction of `e3_score_decomp_enabled`, well before the `lateral_pfc`/`curiosity`/`gated_policy`/`mech295` route sources existed). A corpus-wide check (grep every driver using one of these four route-source values, cross-check `e3_score_decomp_enabled`) is a natural follow-up but was out of scope for a single-target autopsy.
- The remaining unaudited `pending_review.md` FAIL/unclaimed-manifest backlog listed in `failure_autopsy_V3-EXQ-847a-863_2026-08-02.md` Section 8 — unchanged by this session, still open.
