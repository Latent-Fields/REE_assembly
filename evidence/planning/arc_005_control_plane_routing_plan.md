---
closure_plan:
  id: arc_005_control_plane_routing
  generation: v3
  title: "ARC-005 Control-Plane Routing (does the plane route, and which channel carries it)"
  registered: 2026-07-22
  last_updated: 2026-07-31
  scope_claims: [ARC-005]
  sibling_plans: [perceptual_adaptors_v4_plan.md, inference_belief_state_v4_plan.md]
  roadmap_note: >
    TWO-NODE VALIDATION LADDER for the registry's highest fan-in claim.
    GAP-A asked whether the control plane has ANY causal authority over precision
    and mode occupancy, dissociable from content (owner V3-EXQ-802). 802 LANDED
    2026-07-22T21:21:25Z (outcome FAIL, evidence_direction mixed, interpretation
    label control_plane_routing_weak) and was reviewed + adjudicated by governance
    2026-07-25 (989ac1bca0: "Directions for ... 802 ... already carried on their
    manifests" -- no claims.yaml edit; ARC-005 stays status active). GAP-A is now
    DONE. GAP-B asks WHICH of the four implemented channels carries the authority
    802 found -- it is strictly downstream of GAP-A and was UNOWNED, which is the
    reason this doc exists. Registered by a /queue-experiment session that was
    spawned to author GAP-B and correctly STOPPED at its start-time gate because
    802 had not yet run. RECONCILED 2026-07-31 (chip-20260731-arc005-802-reconcile):
    the doc had gone stale after 802 landed and was reviewed -- see the GAP-A
    reconcile_2026_07_31 note and GAP-B's re-scoped design_sketch below.
  nodes:
    - id: "arc_005_control_plane_routing:GAP-A"
      title: "Does the control plane route at all? Channel-vs-content double dissociation over precision and mode occupancy"
      phase: 0
      status: done
      severity: load-bearing
      owner_exq: "V3-EXQ-802"
      unblocks_claims: [ARC-005]
      depends_on: []
      last_updated: 2026-07-31
      completion_note: "V3-EXQ-802 landed 2026-07-22T21:21:25Z (all 6 arms green, 30/30 cells, non_degenerate=true). outcome FAIL, overall_pass false, evidence_direction mixed, interpretation.label control_plane_routing_weak. Read: MODE-OCCUPANCY dissociation is CLEAN and strong -- C1 PASS with d_channel_mean=1.0 (TV distance, channel manipulation moves argmax mode end-to-end: internal_planning at L0 -> external_task at L2, both content sets) vs d_content_mean=0.0 (content has ZERO effect on occupancy), delta 1.0 against an 0.8-SD-of-delta gate + 0.15 absolute floor -- occupancy is dissociably ROUTED by the channel, not read out from content. C3 PASS (10/10 units): identical channel settings reproduce the same argmax regime across both content sets. C2 monotonicity FAILED on ALL 10 units (0/10 satisfied) -- not because occupancy failed to track channel level (rho_external_task_occupancy 0.866-1.0 per unit, essentially monotonic) but because log10_precision_mean is BIT-IDENTICAL across L0/L1/L2 for matching (content,seed) pairs (e.g. content-A seed-0: 2.21044122 at ALL THREE channel levels; confirmed same pattern seeds 1-4 and content B) -- rho_log10_precision=0.0 by construction, a degenerate/undefined rank correlation, not a weak one. So: the claim's what_would_answer PASS bar (monotonic shift in BOTH DVs + occupancy-vs-content margin + reproducibility) is not met, and the FAIL/mixed label is correct -- but the finding is NOT a clean null result nor a single confounded corner: mode-occupancy routing is unambiguously demonstrated (refutes 'readout, not router' for occupancy specifically) while the continuous precision readout shows literally zero measured response to any of the four channels in this design, contradicting the pre-registered dv_symmetry_declaration's expectation that these channels are not precision-invariant. Reviewed + adjudicated by governance 2026-07-25 (REE_assembly 989ac1bca0, 'governance 2026-07-25: apply backlog-autopsy dispositions'): 802 was NOT among the two items held for /failure-autopsy that cycle (707c, 809); its direction is 'already carried on their manifest' -- no claims.yaml edit, ARC-005 stays status active. review_tracker.json: reviewed_run_ids + discussed_experiment_dirs both true for this run_id. No failure_autopsy_V3-EXQ-802*.md/json exists and none is indicated -- this is not a self_route/needs_review diagnostic flag case. Node closes here; GAP-B (below) is the live follow-on, re-scoped 2026-07-31 to the DV this run actually showed signal on."
    - id: "arc_005_control_plane_routing:GAP-B"
      title: "Which channel carries it? Per-channel leave-one-out ablation grid, RE-SCOPED to mode-occupancy after 802"
      phase: 1
      status: in-progress
      severity: load-bearing
      owner_exq: "V3-EXQ-846"
      unblocks_claims: [ARC-005]
      depends_on: ["arc_005_control_plane_routing:GAP-A"]
      last_updated: 2026-07-31
      queued_2026_07_31: "V3-EXQ-846 authored + queued via /queue-experiment (agent-executed, same chip chip-20260731-arc005-802-reconcile). Script ree-v3/experiments/v3_exq_846_arc005_control_plane_channel_occupancy_attribution.py, pushed ree-v3 main 964569c2ca, coordinator POST /queue/add applied=true, confirmed present in /queue/active. Design as re-scoped below: 6 arms x 5 seeds, content set A only (ARM_ALL_ON, 4x ARM_<channel>_OFF leave-one-out, ARM_ALL_OFF), scored on mode-occupancy TV-distance authority-drop only; precision recorded but out of scope for scoring. DV-symmetry declared per arm (all 5 non-baseline arms confirmed not argmax-invariant). Reuse attempted for BOTH ARM_ALL_ON and ARM_ALL_OFF against 802's mint (include_driver_script_in_hash=False) -- refused cleanly (fingerprint_not_in_index: 19 ree_core commits landed since 802, busting the whole-tree substrate_hash), so all 30 cells run fresh; this is the correct, safe refusal, not a design defect. Smoke PASS (12 cells), validate_experiments --strict 0 findings, validate_recording --strict OK. Node stays in-progress until 846 lands a manifest and is adjudicated."
      reconcile_2026_07_31: "V3-EXQ-802 landed (see GAP-A completion_note) and unblocks this node -- the 'blocked' status and blocked_by/resume_condition below are STALE and superseded. RE-SCOPE (not a straight replay of the original design_sketch): 802 showed strong, clean channel-vs-content dissociation on MODE OCCUPANCY (C1 PASS, d_channel=1.0 vs d_content=0.0) but LITERALLY ZERO measured response of log10_precision_mean to channel_level across all 10 (content,seed) units (bit-identical to 8 decimals at every level -- confirmed by direct read of arm_results, not inferred from C2's rho=0.0 alone). Building a leave-one-out contrast on the PRECISION DV as originally sketched would therefore measure a difference of two constant (non-responsive) terms -- exactly the ARITHMETIC-IDENTITY failure class the mandatory_design_check below already anticipated for channels 2 and 4-mu specifically, now empirically true of ALL FOUR channels' effect on this readout in this harness. GAP-B's per-channel attribution should therefore run on the MODE-OCCUPANCY DV only (where 802 demonstrated genuine signal to attribute) and scope the precision DV OUT of GAP-B's scoring a priori (non_contributory / substrate_ceiling on any precision-side arm, per mandatory_design_check -- never 'mixed', since nothing would be measured there either). Separately flagged (not GAP-B's job to diagnose): whether the precision-DV bit-identity is a genuine substrate null or a metric-wiring defect in the harness is an open question worth its own check -- see chip note in WORKSPACE_STATE.md. Authoring route unchanged: /queue-experiment (mandatory skill path), next free EXQ id AT WRITE TIME."
      resume_condition_SUPERSEDED: "(2026-07-22, kept for history) RESUME WHEN V3-EXQ-802 LANDS A MANIFEST. Nothing re-derives this node: it is /queue-experiment work, which has no standing worklist, and 802's completion triggers nothing that re-raises it. Authoring route: /queue-experiment (mandatory skill path -- do NOT hand-write into ree-v3/experiments/ or the queue). Pick the next free EXQ id AT WRITE TIME (several parallel sessions collided in the 800s: 802 ARC-005, 804 ARC-003, 805 ARC-016)."
      design_sketch: "RE-SCOPED 2026-07-31 (see reconcile note): leave-one-out at the L2 (fully perturbed) setting on content set A, scored on MODE-OCCUPANCY ONLY: ARM_ALL_ON plus four ARM_<channel>_OFF arms that each return EXACTLY ONE channel to its L0 value, contrasted against ARM_ALL_OFF (= L0). Per-channel occupancy authority = the DROP in the channel-vs-L0 occupancy effect (TV distance / argmax-mode shift) when that channel alone is returned to baseline. The precision DV is NOT scored per-channel in this design (802 showed no baseline precision effect to attribute from) -- may still be RECORDED per the generous-recording convention, but any precision-side criterion must be pre-declared non_contributory/substrate_ceiling, not scored as a finding. REUSE: ree-v3/experiments/_lib/baselines/exq802_arc005_control_plane.py (verified exports: CHANNEL_LEVELS=[0.0,0.5,1.0], channel_settings(level), agent_kwargs(level), content_env_kwargs(content,seed), off_path_config_slice(), cell_config_slice(level,content), arm_id(level,content)); cite reuse_baseline_from: <802 run_id> with include_driver_script_in_hash=False so the L0 cells are REUSED rather than re-run. This is a refinable sketch, not a fixed design."
      channels: "The four implemented control-plane channels, with the readiness-probe expectation that channels 3 and 4 carry most of the OCCUPANCY authority (600-tick probe -- an EXPECTATION to test, not an established finding): (1) 5-HT rigidity via serotonin gain_min/gain_max -> mainly PRECISION; (2) phasic-burst gain via phasic_burst_temp_delta -> mainly PRECISION, and it is an E3 SOFTMAX TEMPERATURE hence ARGMAX-INVARIANT; (3) mode prior via salience_external_task_bias -> DIRECT occupancy authority (per-mode logit shift); (4) pcc_stability mu via pcc_stability_baseline -> occupancy via the MECH-259 switch-threshold leg, while its MECH-048 mu leg is a softmax temperature and is ARGMAX-INVARIANT."
      mandatory_design_check: "DV-SYMMETRY, per the /queue-experiment rule -- do NOT skip. State per arm the symmetry group of that arm's DV and confirm the manipulation is NOT invariant under it. Channels 2 and 4-mu are BOTH pure softmax temperatures, so an arm ablating only one of them is at real risk of being ARGMAX-INVARIANT and therefore producing a delta that is an ARITHMETIC IDENTITY rather than a measurement. Such an arm must be scoped OUT of scoring and routed non_contributory under substrate_ceiling -- NEVER 'mixed'. This is exactly the V3-EXQ-604c failure class."
      substrate_notes: "Carried over from 802, ALL identical in every arm: (a) use_dacc=True AND use_aic_analog=True are REQUIRED -- with both off the SalienceCoordinator's salience_aggregate is identically 0, argmax is always external_task, and the discrete mode can NEVER switch (occupancy would be single-mode by configuration, not by substrate); (b) phasic_burst_signal_source='instantaneous_pe' with phasic_burst_baseline_continuity='carry' is REQUIRED or channel 2 fires zero events and is inert; (c) 5-HT must be set at the channel OUTPUT (cfg.serotonin.gain_min == gain_max) because harm suppression crushes any tonic baseline to ~0 within tens of steps; (d) NON-DEGENERACY gates on the DESIGN-level 'n_distinct_argmax_modes_across_design >= 2', NOT a per-arm 'arm occupies >= 2 modes' -- 802 measured that the per-arm form VACATES the strongest instance of the effect under test (every corner arm single-mode while the channel manipulation moved the mode end-to-end, TV 1.0, and content moved it not at all, TV 0.0). Keep within-arm multi-modality as a NON-GATING diagnostic."
      why_it_matters: "ARC-005 carries 88 reverse dependencies -- the highest fan-in in the registry -- on exp_conf 0.0 with ZERO experimental entries, held up entirely by lit_conf 0.783. A PASS on GAP-A establishes that THE PLANE is causal but NOT that each channel independently routes; 802's own docstring ('WHICH CHANNEL CARRIES A PASS') and its manifest custom_information.channel_attribution_limit both declare per-channel dissociation UNTESTED. Without GAP-B those 88 dependents cannot tell WHICH channel they may rely on."
    - id: "arc_005_control_plane_routing:GAP-A-precision-diagnostic"
      title: "Why is log10_precision_mean bit-identical across channel levels in 802? Harness defect, not a substrate null"
      phase: 0
      status: done
      severity: informational
      owner_exq: null
      unblocks_claims: []
      depends_on: ["arc_005_control_plane_routing:GAP-A"]
      last_updated: 2026-07-31
      completion_note: "Diagnosed chip-20260731-arc005-802-precision-anomaly (2026-07-31), the open question the GAP-B reconcile note deferred. VERDICT: (a) genuine harness/measurement-construction defect, NOT (b) a real substrate null -- the precision DV in 802's driven harness is MATHEMATICALLY GUARANTEED to be channel-invariant regardless of the true substrate, so its rho=0.0/bit-identical result carries zero evidential weight either way about whether the control plane routes precision. MECHANISM, confirmed empirically by re-running 802's exact _build/_run_cell logic (agent_kwargs/channel_settings from experiments/_lib/baselines/exq802_arc005_control_plane.py, reset_all_rng from experiments/_lib/arm_fingerprint.py) at L0 vs L2, same seed+content: (1) arm_cell's per-cell RNG reset (random/numpy/torch/cuda, a deliberate reproducibility hardening fix, plan section 2.2) reseeds to the SAME value for cells sharing a seed across channel levels, so the stochastic candidate-trajectory pool generated by agent.generate_trajectories is bit-identical across L0/L1/L2. (2) Given that identical pool, the e3.select() score tensor (agent.e3.last_scores) came back torch.equal()-TRUE between L0 and L2 at every one of 8 captured selection calls across a 70-tick probe -- not merely the same argmin, the SAME SCORES to float32 precision. (3) Root cause of (2): the dACC score_bias term (SD-032b, the pathway the pre-registered dv_symmetry_declaration cites for channel 1 -- '5-HT reshapes the dACC bundle') is computed from z_harm_a, candidate payoffs/effort/action_classes, e3.current_precision and drive_level -- NONE of which read serotonin.current_seeding_gain()/valence_wanting_floor in this call path (ree_core/agent.py select_action, the self.dacc(...) invocation ~line 6133), so it is bit-identical regardless of the channel-1 setting; channel_route_bias is unconditionally None because use_modulatory_channel_routing defaults False and BASE.agent_kwargs() never sets it; and effective_temperature (channel 2, phasic burst) DOES verifiably differ by level (captured 0.9 at L0 vs 0.1 at L2, confirming phasic_burst_temp_delta is live) but selection is a deterministic argmin over scores in agent.eval() -- exactly the argmax-invariant transform the docstring's OWN dv_symmetry_declaration admits for channel 2, so it never changes which candidate is chosen. Channels 3/4 (salience mode prior, pcc_stability) correctly drive agent.salience.current_mode (confirmed: L0 stayed internal_planning-only, L2 visited both internal_planning and external_task over the same 70 ticks) but that mode variable is read only for the OCCUPANCY diagnostic, never fed back into trajectory scoring. Net: the actually-EXECUTED action sequence is bit-identical across channel levels (confirmed directly, not just inferred from scores) -> the env trajectory, z_world stream, and the driver's manually-recomputed e2.world_forward prediction-error stream feeding e3.update_running_variance are ALL bit-identical -> log10_precision_mean is bit-identical BY CONSTRUCTION, independent of any true precision-routing property of the substrate. DECISION RELEVANCE: in 802's own manifest, rho_external_task_occupancy already clears the C2 0.60 floor in ALL 10/10 (content,seed) units (range 0.866-1.0) -- C2 failed 0/10 purely on the precision half's degenerate (undefined, non-weak) rho=0.0. Had the precision DV been validly measurable, C2's occupancy component alone would already have satisfied C2 (>=7/10 required), and since C1/C3 both PASS, 802's overall verdict would likely have been PASS/supports rather than FAIL/mixed/control_plane_routing_weak -- meaning the current FAIL verdict is an artifact of an unmeasurable DV component, not evidence that the plane fails to route precision. This does NOT mean precision routing is real (that remains genuinely untested); it means 802 supplies NO information about it either way, and the FAIL label should not be read as a negative finding on precision specifically. REMEDY NOT EXECUTED IN THIS CHIP (a substrate-wiring or DV-redesign decision, out of a diagnostic chip's scope, and /queue-experiment authoring is the mandatory path for any fix): a corrected re-run (V3-EXQ-802a) would need either (i) dACC's score_bias to genuinely read serotonin-driven z_goal_seeding_gain/valence_wanting_floor as the dv_symmetry_declaration assumed, or (ii) a precision DV construction that isn't bottlenecked through deterministic argmin selection over an RNG-matched candidate pool (e.g. reading the agent's own internally-tracked e3 state from its normal orchestration path rather than the driver's manual e2.world_forward recomputation) -- deciding between these is a design call for whoever next works this claim, not this chip. GAP-B (occupancy-only, V3-EXQ-846) is UNAFFECTED either way: it was already correctly scoped to occupancy, which this diagnostic confirms was the only validly-measured DV in 802. Probe scripts (not committed, throwaway): reproduced via experiments/_lib/baselines/exq802_arc005_control_plane.py + experiments/_lib/arm_fingerprint.py reset_all_rng, driving REEAgent directly outside the experiment harness."
---

# ARC-005 -- Control-Plane Routing (Plan of Record)

**Created:** 2026-07-22 &nbsp;|&nbsp; **Reconciled + GAP-B queued:** 2026-07-31 &nbsp;|&nbsp;
**Precision-DV diagnosed:** 2026-07-31
**Status:** GAP-A **done** (V3-EXQ-802 landed FAIL/mixed, reviewed + adjudicated by governance
2026-07-25, no claims.yaml change) — GAP-A precision-DV bit-identity **diagnosed as a harness
defect, not a substrate null** (see below) — GAP-B **in-progress** (V3-EXQ-846 queued, re-scoped
to mode-occupancy attribution only).

## Why this doc exists

ARC-005 ("Control plane routes precision and modes") has the **highest fan-in in the claims
registry — 88 reverse dependencies** — on `exp_conf 0.0` with **zero** experimental entries.
Its entire support is literature (`lit_conf 0.783`). V3-EXQ-802 was the first experiment of any
kind against it, and landed 2026-07-22T21:21:25Z.

The validation splits cleanly into two questions:

| Node | Question | Owner | Status |
|---|---|---|---|
| GAP-A | Does the plane route **at all**, dissociably from content? | V3-EXQ-802 (landed) | **done** |
| GAP-B | **Which channel** carries that authority (occupancy only — see re-scope below)? | V3-EXQ-846 (queued) | **in-progress** |

## GAP-A's result, in brief (full detail in the node's `completion_note`)

802's mode-occupancy dissociation was clean and strong (C1 PASS, channel TV=1.0 vs content
TV=0.0) and reproducible across content sets (C3 PASS, 10/10). Its continuous precision readout
showed **zero measured response to any of the four channels** — `log10_precision_mean` was
bit-identical across all three channel levels for every (content, seed) pair — so C2
monotonicity failed by construction, not by a weak/noisy signal. `outcome: FAIL`,
`evidence_direction: mixed`, `interpretation.label: control_plane_routing_weak`. Governance
reviewed this 2026-07-25 (`REE_assembly` `989ac1bca0`) and made no claims.yaml change; ARC-005
stays `status: active`.

## Why the precision DV was bit-identical: harness defect, not a substrate null (diagnosed 2026-07-31)

The open question the GAP-B reconcile note deferred ("whether the precision-DV bit-identity is
a genuine substrate null or a metric-wiring defect") is now resolved: **it is a harness defect.**
`log10_precision_mean` in 802's driven harness is mathematically guaranteed to be invariant to
all four channels, independent of the substrate's true behaviour, for three compounding reasons:

1. `arm_cell`'s per-cell RNG reset (a deliberate reproducibility hardening fix) reseeds Python
   `random`/numpy/torch/cuda to the same value for cells sharing a seed across channel levels, so
   the stochastic candidate-trajectory pool is bit-identical across L0/L1/L2.
2. Given that identical pool, `e3.select()`'s score tensor came back bit-identical between L0 and
   L2 at every captured selection call: the dACC `score_bias` term never reads
   `serotonin.current_seeding_gain()`/`valence_wanting_floor` in this call path (contradicting
   what the pre-registered `dv_symmetry_declaration` assumed for channel 1), and
   `channel_route_bias` is unconditionally `None` because `use_modulatory_channel_routing`
   defaults `False` and is never set here.
3. `effective_temperature` (channel 2) genuinely does differ by level (confirmed 0.9 at L0 vs 0.1
   at L2), but selection is a deterministic argmin over scores in `agent.eval()` — exactly the
   argmax-invariant transform the declaration itself already conceded for channel 2, so it never
   changes which candidate wins.

Channels 3/4 correctly drive `salience.current_mode` (confirmed directly: L0 stayed
`internal_planning`-only over 70 ticks while L2 visited both `internal_planning` and
`external_task`), but that state is read only for the occupancy diagnostic, never fed back into
scoring. The result: the actually-executed action sequence is bit-identical across channel
levels (confirmed directly), so the env trajectory, `z_world` stream, and the driver's manually
recomputed E2 prediction-error stream are all bit-identical too — `log10_precision_mean` is
bit-identical **by construction**.

**Decision relevance:** in 802's manifest, `rho_external_task_occupancy` already clears the C2
0.60 floor in all 10/10 units (range 0.866–1.0); C2 failed 0/10 purely on the precision half's
degenerate rho=0.0. Had precision been validly measurable, C2 would likely have passed on
occupancy alone, and with C1/C3 both PASS, 802's overall verdict may well have come out
PASS/supports rather than FAIL/mixed. This does **not** mean precision routing is real — it
means 802 supplies no information about it either way, and the FAIL label should not be read as
a negative finding on precision specifically. GAP-B (occupancy-only, V3-EXQ-846) is unaffected —
occupancy was always the only validly-measured DV here. A corrected re-run (V3-EXQ-802a) is a
substrate-wiring or DV-redesign decision out of scope for this diagnostic; full mechanism and
remedy options are in the `GAP-A-precision-diagnostic` node's `completion_note` above.

## The ownership gap this doc closes (history)

A `/queue-experiment` session was spawned on 2026-07-22 to author GAP-B. It **correctly stopped
at its start-time gate**: V3-EXQ-802 was still `status: "pending"` with no landed manifest, so
the per-channel design could not be written. That was the right outcome — but it left the
GAP-B specification living only in a session transcript, and nothing re-derives it (it is
`/queue-experiment` work, unlike `/governance`/`/failure-autopsy` which re-derive their own
worklists). This node is that record. It went **stale** after 802 actually landed and was
reviewed (2026-07-22 through 2026-07-25) — this doc was not reconciled with that until
2026-07-31 (chip `chip-20260731-arc005-802-reconcile`), which is the edit you are reading now.

## Why GAP-B waited for GAP-A, and why it is now re-scoped rather than run as originally sketched

The leave-one-out design measures *the drop in the channel-vs-L0 effect when one channel is
returned to baseline*. Three things would have failed had GAP-B been designed before 802 ran:

1. **802 returned FAIL** on the joint monotonicity bar — but the mode-occupancy half of that FAIL
   is a strong, clean dissociation, not a null; only the precision half is a genuine (bit-exact)
   null. A leave-one-out contrast on precision would measure a difference of two constant terms
   — an arithmetic identity, exactly the class `mandatory_design_check` already warns about for
   channels 2/4-mu specifically, now empirically confirmed for **all four channels** on this DV.
   **GAP-B is therefore scoped to mode-occupancy attribution only** (see the re-scoped
   `design_sketch` above) — this is the one substantive change 802's landing made to the design,
   not just an unblock.
2. **The baseline cells can now be reused**: `reuse_baseline_from: v3_exq_802_arc005_control_plane_routing_double_dissociation_20260722T212125Z_v3`
   is live via `ree-v3/experiments/_lib/baselines/exq802_arc005_control_plane.py`.
3. **The argmax-invariance risk is now checkable against real diagnostics**, not just asserted —
   802's `custom_information.dv_symmetry_declaration` and per-arm `realised_channel_state` /
   `mode_prior_diagnostics` give the actual per-channel behaviour to design the ablation against.

## Resume procedure

```bash
# 1. GAP-A has landed and been reviewed -- confirmed 2026-07-31:
grep -l v3_exq_802 /Users/dgolden/REE_Working/REE_assembly/evidence/experiments/*.json
python3 -c "import json; d=json.load(open('/Users/dgolden/REE_Working/REE_assembly/evidence/experiments/review_tracker.json')); rid='v3_exq_802_arc005_control_plane_routing_double_dissociation_20260722T212125Z_v3'; print(rid in d['reviewed_run_ids'], rid in d['discussed_experiment_dirs'])"
# 2. Read GAP-A's completion_note above for the verdict + channel diagnostics before designing GAP-B.
# 3. Author via the skill -- /queue-experiment. Never hand-write the script or queue entry.
```

Then work the GAP-B frontmatter fields in order: `design_sketch` (RE-SCOPED to occupancy-only,
refine further as needed, don't take as fixed), `channels`, `mandatory_design_check` (the
DV-symmetry rule — the V3-EXQ-604c failure class, now with an empirical precedent from 802 for
why it matters), `substrate_notes` (all four carry over from 802 unchanged).

## Scope

This plan owns **ARC-005's own V3 experimental validation only**. It is not the home for the V4
consumers that ride the control plane — `perceptual_adaptors_v4` names ARC-005 as the host for
its cross-modal negotiation/precision layer (PA-5) but is a forward roadmap with no experiments
and a dormant drift checker. Cross-plan edges belong there, not here.
