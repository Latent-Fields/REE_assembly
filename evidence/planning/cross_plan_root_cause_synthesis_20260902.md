# Cross-plan root-cause synthesis -- the 33 remaining v3 nodes (2026-09-02)

**Session:** `crossplan-rootcause-synthesis-20260902`
**Generated:** 2026-09-02T05:30:36Z
**Status:** SYNTHESIS. Registers nothing in `claims.yaml`. Promotes nothing, demotes nothing. Its
outputs are three governance flags (GFLAG, raised through `governance_flag.py` in the same session),
a refreshed `insights_report.md` front section, and this record. Every disposition it names is for
`/governance` to make.
**Work-graph class of this task:** `mystery (known data)` -- no new run was needed; the answer was
already in the autopsy stream and the plan docs, distributed across ~90 confirmed autopsies since
2026-07-08 and never written back to the nodes that depend on it.

**Sources read end to end:** `closure_status.md` / `closure_drift.md` (2026-09-02T05:13Z snapshot);
every non-done node of the 17 v3 closure plans (43 nodes: 33 remaining + 10 assembling); the full
`f_dominance_conversion_ceiling` substrate-queue entry (92 KB, 26 failure records, 6-rung ladder,
2026-07-06 / 07-08 / 08-12 reconciles); `mech457_competence_bootstrap_explorer`, `v4_loop_segregation`,
`SD-018`, `SD-e1-rollout-consistency-training`, `sd_zworld_warmup_optimizer_group`; the
`hypothesis_space_registry.v1.json` questions `conversion_ceiling_root`, `competence_floor`,
`e3_fdominance_causal_discrimination`, `inv088_evaluator_degeneracy_cause`,
`zworld_underdifferentiation_cause`, `mech471_*`, `mech472_*`; the conversion-ceiling campaign plan and
its prong map; the 2026-09-01 governance-flag triage (Parts 1 and 2); and the confirmed autopsies
719a, 724, 732a, 734-737, 689d, 711-713, 707c, 808 (via the registry), 813/948, 108b, 954, 965, 925,
925a, 936, 936a, 937b, 571b, 642b, 938, 964, 910b, 866c, 948, plus the MECH-457 fan-out and retention
portfolios (747-755, 765, 769-772, 780-782, 788-792a, 819a, 821b, 836-cluster).

---

## 0. Headline

**The binding constraint on v3 closure is a single interface, not a selector.** The
observation -> `z_world` -> E1/E2-rollout pathway does not deliver resource-directional,
action-conditioned, horizon-stable candidate futures to E3. Three confirmed results pin it:

| result | what it establishes | status |
|---|---|---|
| V3-EXQ-813 + **V3-EXQ-948** (2026-08-25, confirmed, red-teamed) | A PPO reader of `z_world` alone forages 0.5 res/ep (floor 1.0); the same reader given `z_world` + the 25-dim local resource field clears the floor on 3/3 seeds (2.23). The missing content is NAMED: the directional resource gradient, present in the encoder's own input, is discarded -- even with SD-018's scalar proximity head already training it. | `H-observation-interface` **CONFIRMED** on `conversion_ceiling_root`. Routed `/implement-substrate` amend SD-018, user-confirmed 2026-08-25. **No build item, no chip, no owner exists** (SD-018 still reads `status: implemented, ready: true`). |
| V3-EXQ-108b -> 954 -> **965** (2026-08-02 .. 08-30) | The evaluator degeneracy over `z_world` is not undertraining and not a dim-32 ceiling; it is E1's forward rollout collapsing -- an action-blind, single-step-trained dynamics model rolled 30 steps. ITEM 1 (action conditioning) landed and moved `cr_ratio` 6455x, still 25-37x short of the 0.1 bar. | `SD-e1-rollout-consistency-training` ITEM 2 substrate landed 2026-08-30; **validation experiment owed, unminted, unqueued**. |
| V3-EXQ-925 -> 936 -> 936a -> **571b** (2026-08-12 .. 09-01) | At default config the selector never engages committed selection (`committed_fraction` 0.000, entropy 0.998). Under the SD-056 clamp the "F-monopoly" is REGIME-DEPENDENT: F in the unclamped 571 world, `harm_weighted` clamped in 571-shape, `residue_weighted` at 99.999% in the 936 family. The E3 additive score sum has no cross-channel normalisation, so the largest-SCALE channel is the monopolist. The clamp that fixes the rollout divergence collapses E3's committed score range ~800x. | `H0` selector-regime confound + `H5` uncontrolled score scale **CONFIRMED** on `e3_fdominance_causal_discrimination`; H1-H4 all still alive, untestable as posed. |

Read together: E3 is scoring candidate futures that carry no resource-directional information and
that collapse over horizon, so candidate scores are near-identical, committed selection never
engages, and whatever residual variance exists is a scale artifact of whichever channel is largest.
"F-dominance", "conversion ceiling", "monostrategy", "competence floor" and "candidate-pool collapse"
are five surface readings of that one gap, taken at five different points along the same pathway.

**This is `complicated (buildable)`, not `complex (probe-gated)`.** The probe chain has run
(719a -> 724 -> 732 -> 732a -> 737/738 -> 813 -> 948; 108b -> 954 -> 965). Two builds are named,
one landed-awaiting-validation, one un-owned. The `f_dominance_conversion_ceiling` entry still
carries `node_class: complex (probe-gated)` and `depends_on_unresolved: []`; that is the
undeclared gate the closure status is reporting.

---

## 1. What "not ready with no unresolved dependencies" actually means here

`f_dominance_conversion_ceiling` (`ready: false`, 26 failure records, priority 1, unblocks 18
claims) has had its `depends_on_unresolved` empty since the 2026-07-06 reconcile moved the 689g
falsifier out of it. Every later event that named its real upstream was written somewhere else:

- 2026-07-08, 719a: "committed-action dissociation DVs are UNDEFINED until competence exists;
  NEXT STEP = competence-localization diagnostic BEFORE any build" -- written into
  `reconcile_note_2026_07_08_719a` on the entry, but not into `depends_on_unresolved`.
- 2026-07-20, 689d / 711-713 withdrawals: neither the selection face nor the arbitration face
  carries a validly-measured conversion result (hold-weighted DV). Written into
  `stale_citation_correction_2026_08_12` three weeks later; the entry's `status` string still says
  `mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional`.
- 2026-08-12, campaign `P4-learned-gating` and `behavioral_diversity_isolation:GAP-K`: "parked
  behind MECH-457 + INV-088". Correct direction, but MECH-457 and INV-088 are claims, not
  substrate items, and `competence_floor` (the MECH-457 question) was CLOSED on 2026-08-08 with
  every hypothesis resolved -- so "parked behind MECH-457" points at a finished discrimination,
  not at a build.
- 2026-08-25, 948 (H-observation-interface CONFIRMED, SD-018 amend routed, user-confirmed):
  written to `conversion_ceiling_root` and to SD-018's `failure_record`. Not to
  `f_dominance_conversion_ceiling`, not to GAP-I, not to GAP-K, not to any campaign node, not to
  `CURRENT_FRONT.md` (whose hero question is still the closed `competence_floor`, per GFLAG-0093).
- 2026-08-30, 965 (SD-e1 ITEM 1 validated, ITEM 2 owed): written to the SD-e1 entry only.

So the gate exists and is well-specified; it is simply declared on the wrong objects. The closure
snapshot is right that nothing declared is blocking the entry, and the entry is right that it is
not ready. Both are true because the dependency edge was never drawn.

**The corrected dependency, stated so it can be copied into the entry:**

```
depends_on_unresolved:
  - "SD-018 amend (V3-EXQ-948, 2026-08-25): expose the directional resource field to z_world's
     consumers -- either re-scope SD-018's scalar proximity target to a directional readout, or
     route resource_field_view as an explicit channel alongside z_world. UNOWNED: no build item,
     no chip."
  - "SD-e1-rollout-consistency-training ITEM 2 validation (V3-EXQ-965 successor): TRAIN with
     rollout_consistency_loss (decay=1.0 flat control included); bar cr_ratio(h=1) >= 0.1,
     e1coe_score_var >= 0.002. OWED, unminted."
  - "E3 channel-scale normalisation (fallback_ladder rung 3, divisive_normalization_pooled_
     denominator) -- the H5 mechanism from 925a/936a/571b. Currently 'V4-leaning'; V3-required
     by phase-label-follows-dependency once the first two land, because no conversion DV is
     non-degenerate without it (see Section 4)."
node_class: complicated (buildable)      # was: complex (probe-gated) -- the probe has run
```

---

## 2. The 43 nodes, by what actually gates them

Method: for every non-done node in every v3 plan I read the node's own `resume_condition` /
`blocked_by` / `awaiting` / `upstream_block_reason` / `depends_on` and followed the chain until it
terminated in either (a) the interface gate above, (b) a sibling E1/E2-representation build, (c) a
governance decision, (d) an independent build, or (e) nothing declared. The chain, not the prose
label, decides the bucket.

### 2a. Chain to the interface gate via FULLSTACK / GAP-I / "competent all-ON substrate" -- 35 nodes

| plan | nodes | how the chain terminates |
|---|---|---|
| `conversion_ceiling_campaign` | CAMPAIGN, P-comp, P2-rootC, P3-ofc, FULLSTACK, P4-learned-gating, GENERATION (7, all `assembling`, **none with `revisit_after`**) | CAMPAIGN summary: "converged on competence gate". GENERATION: "ORDERING-GATED on INV-088 z_world differentiation". P4: "parked behind MECH-457 + INV-088". FULLSTACK 714: readiness abort, C2 never scored (GAP-A divergence 0.004, OFC range 0.0007 starved). |
| `behavioral_diversity_isolation` | GAP-I (root), GAP-K, GAP-B, GAP-C, GAP-G (5) | GAP-I closes "on the first downstream conversion" -- every downstream retest self-routed `substrate_not_ready` (719a: one competence root). GAP-K: "f_dominance_conversion_ceiling, unbuilt, parked behind MECH-457 + INV-088". GAP-B path (b), GAP-C "both legs must run on the SOTA conversion stack", GAP-G depends on GAP-B. |
| `arc_062_rule_apprehension` | GAP-B, GAP-H, GAP-I, GAP-I-absorption, GAP-J, GAP-K (6) | GAP-B closes only on a 654h-class C2 lift, whose DV is undefined until competence exists (719a; brake fired 21st ARC-062). The other five `depends_on` GAP-B. |
| `sd_037_axis_b` | P1b (assembling), P2, P3, P4 (4) | P1b `awaiting: conversion_ceiling_campaign:FULLSTACK`; P2 -> P3 -> P4 chain on P1b. |
| `self_attribution` | GAP-1, GAP-2, GAP-3, GAP-6 (4) | GAP-2 re-pointed 2026-08-18 to "resume once FULLSTACK demonstrates a behaviourally-validated non-monostrategy policy"; GAP-1 "same upstream gates as GAP-2"; GAP-3 depends on both; GAP-6's diversity half is GAP-2's gate. |
| `sleep_substrate` | GAP-2 (1) | `depends_on: arc_062:GAP-B`; "sleep refinement cannot register signal until the agent has waking diversity to refine". |
| `global_workspace_jlens` | A, GATE-B, B, MECH-191 (4) | A's declared blocker is literally "ext: observation-encoding competence build (V3-EXQ-732-localized H2_observation_interface_...)" -- the gate this document names, already written on the node in July. GATE-B: "a competent all-ON substrate". B and MECH-191 chain on A / GATE-B. |
| `infant_substrate` | GAP-13, GAP-14 (2) | GAP-13 residual = "the shared selection-AUTHORITY frontier" (cross-linked GAP-I). GAP-14 c-1 re-pointed 2026-07-21 to "the BEHAVIOURAL-COMPETENCE wall (V3-EXQ-724 competence_deficit_diffuse)". |
| `commitment_closure` | GAP-4, GAP-8 (2) | GAP-4 "advances on the 460k RESULT" -- 460k ran 2026-06-22 FAIL `closure_exclusive_eval_armed_hold 0/3` (in the f_dominance failure records); the 460 lineage's `substrate_not_ready` self-routes are the same competence root (719a). GAP-8 (SD-033b behavioural validation, `built`) "cycled 485i->j->k circling the F-dominance ceiling". |

### 2b. Chain to a SIBLING E1/E2-representation build (same pathway, distinct item) -- 4 nodes

| node | gate | why it is the same family |
|---|---|---|
| `orienting_epistemic_deficit_v3:ORNT-2` | (1) user review of `mech314bc_percandidate_extension_staged_2026-08-08.md`; (2) SD-063 `E2WorldUncertaintyHead` training loop, readiness `last_uncertainty_dev_range > 0` | Per-candidate E2 uncertainty is "the near-uniform vector an untrained head returns" -- the same per-candidate-differentiation failure 964 hit (`n_targets==1`, constant readout cannot move an argmax). |
| ORNT-3, ORNT-4 | depend on ORNT-2 | ORNT-4 is explicitly "does epistemic-deficit orienting explain the cold-start competence split" (Q-089 / MECH-471). |
| `policy_decomposition_trigger:REPOSE` | 938 terminal; "reopen only on a different operationalization". H-representation-axis alive: "forward-PE as currently computed is too coarse-grained to register the environment" | The forward-PE is E1's -- the same single-step, action-blind model 108b/965 diagnosed. A re-pose here should wait for SD-e1 ITEM 2 rather than mint a new env-axis letter. |

### 2c. Independent of the interface gate -- 4 nodes

| node | class | what it needs |
|---|---|---|
| `orienting_epistemic_deficit_v3:ORNT-6` | governance decision (`puzzle (known rules)`, decidable now) | Whether MECH-489's MIXED read (910b, C1 tap discrepancy) is the standing read or warrants one instrument check. No build, no run. |
| `mech357_avoidance_efficacy:BUILD` | `complicated (buildable)`, partial | Stage-H agent-directed hazard pursuit wiring (603 lineage, 22 letters). Curriculum-side; runs on the scaffolded onboarding path, not on E3 conversion. |
| `commitment_closure:GAP-4-battery` | in progress, partly independent | 466e PASSED; the SD-034 residue-discharge battery continues. Its *b behavioural cohort members will hit the interface gate; the non-behavioural members do not. |
| `orienting_epistemic_deficit_v3:ORNT-1` | **no declared blocker** | `status: blocked`, `unblocks: MECH-395`, empty blocker text in the closure snapshot. This is the one node whose gate genuinely is undeclared in the plan itself (as opposed to declared on the wrong object). Flagged below for the plan owner to name it. |

**Tally:** 39 of 43 nodes (91%) terminate in the observation -> latent -> rollout pathway; 35 of
those through one gate. The v3 closure map is not 33 independent problems. It is one build with a
33-node shadow.

---

## 3. Why the campaign's seven `assembling` nodes have no revisit date

`assembling` is deliberately restful (assembly_vs_closure_plan MOVE-1): it is not flagged stale and
needs no re-stamp, and `revisit_after` is the ONLY thing that disturbs it. The campaign nodes were
registered 2026-06-22 with `awaiting: routing=queue-experiment` -- i.e. awaiting the next
experiment, at a time when the next experiment was the FULLSTACK arm. FULLSTACK ran terminal on
2026-07-07, the competence reframe landed 2026-07-08, and `awaiting:` was never re-pointed
because nothing in the assembly machinery asks a resting node to re-check what it is awaiting.
Result: seven load-bearing nodes have rested for 10 weeks awaiting a routing that has since fired
and returned, with no date on which anyone would look.

Recommended (governance, plan-frontmatter only, no status change):
`awaiting: "SD-018 directional-field amend + SD-e1 ITEM 2 validation (see
cross_plan_root_cause_synthesis_20260902.md)"` on all seven, and `revisit_after` = the date the
SD-018 amend lands + one validation run. `assembly_status` stays as it is (`ran_exhausted_for_substrate`
is accurate: each face ran, and each was exhausted *for the substrate as it stood*).

---

## 4. The selection face is not testable until three instrument preconditions hold

Separately from competence, the record since 2026-07-20 shows that no conversion falsifier on the
selection face can currently be non-degenerate. These are measurement preconditions, and they are
also undeclared on the nodes that would run the falsifier:

1. **Hold-weighted DV.** Every pre-2026-07-20 conversion PASS/FAIL on `committed_class_entropy`
   (689d, 699, 710, 711, 713) was accumulated per env step while `agent.py:5430` returns the HELD
   action off E3 ticks. Withdrawn. The `GateDVRecorder` instrument landed 2026-08-19 (ree-v3
   `c309bc6486`). Any new falsifier must read it. Governance REFUSED a 713x re-letter on
   2026-08-21 (GFLAG-0045) -- correctly: instrument existence is not a lift.
2. **Class floor.** `support_preserving_min_first_action_classes` defaults to 2 at ~276 driver
   call sites, capping committed-class entropy at ~ln(3) arm-invariantly (GFLAG-0072, open).
   V3-EXQ-955 raised it to 5 for MECH-440 only; 571b (2026-09-01) still hard-sets 2.
3. **Score scale.** The E3 additive score sum has no cross-channel normalisation. 925a's
   routing note: "the next discriminating experiment should control ABSOLUTE SCORE SCALE via
   channel-scale normalisation (H5's mechanism) -- NOT via temperature (argmin-invariant, inert
   on the plain committed path)". 936's biological-reference finding: "No biological valuation
   system permits one cost channel to exceed competitors by 20+ orders of magnitude; divisive
   normalisation over competing value signals is ubiquitous. The absence of ANY normalisation on
   the E3 additive score sum is a formal-import divergence with no targeted_review covering it."
   This is rung 3 of the entry's own `fallback_ladder`, labelled "V4-leaning" on 2026-06-19 and
   never revisited after H5 was confirmed.

Consequence for MECH-439 itself: its quantitative premise (F = 88-89%, V3-EXQ-571) was measured
by a diagnostic run in the unclamped regime, 15 days before the clamp landed. Under the fixed
instrument the premise is regime-dependent and the monopolist is not F. MECH-439 as titled is
neither supported nor refuted; it is mis-posed at the channel level, and 571b's per-claim note
already says so ("channel-level reading does not transfer across the instrument change"). The
honest re-pose is scale-level: *the un-normalised E3 score sum lets the largest-scale channel
monopolise committed-selection variance, so per-candidate diversity in any smaller-scale channel
cannot convert.* That re-pose makes rung 3 the falsifier, not another eligibility lever.

---

## 5. What this synthesis does NOT claim, and what would refute it

- **948 tested an external PPO reader, not REE's own E2 -> E3 loop.** It confirms the CONTENT
  half (the field is recoverable and sufficient for a competent actor). The DYNAMICS half (E1/E2
  rollouts over that content stay informative across the horizon) is the SD-e1 ITEM 2 question,
  still owed. If both land and the all-ON REE agent *still* forages ~0 on 3/3 seeds, the
  constraint is downstream of the interface -- in E3 commit itself (ARC-003, whose own falsifier
  GFLAG-0091 records as unrunnable) or in the REINFORCE stack's seed bimodality (MECH-471
  H-exploration-init-variance, confirmed). That is the pre-registered refutation.
- **It does not resolve MECH-439's H1-H4.** They stay alive; the claim is that they cannot be
  discriminated until Section 4's preconditions hold, which is what 925/925a/936a/571b each
  independently concluded.
- **It does not say the selection-face builds were wasted.** MECH-448/449 (ARC-107) and the
  ARC-108/110 loop segregation are built, no-op default, and unmeasured. They become measurable
  once the interface delivers differentiated candidates. The 713 bounded-parity win survives.
- **It does not touch the retention findings.** `competence_floor` is decided (distributional
  critic + KL anchor set the retention half-life) and closed to fan-out. Those are process-family
  fixes that apply once competence installs; they are not the binding constraint.

---

## 6. Recommendations (ordered by value per unit effort; none applied here)

1. **Own the SD-018 amend.** It is the one confirmed, named, user-confirmed build on the critical
   path with no owner. `complicated (buildable)`. Two admissible shapes per the 948 autopsy:
   re-scope SD-018's target from scalar `max(resource_field_view)` to a directional readout, or
   route `resource_field_view` as an explicit channel alongside `z_world`. Chip to
   `/implement-substrate`; the design constraint from 948's red-team is that the SCALAR signal
   is already active and insufficient.
2. **Queue the SD-e1 ITEM 2 validation.** Owed since 2026-08-30; the entry's own hint says
   "THE NEXT ACTION IS AN EXPERIMENT, NOT A BUILD" and specifies the design (train WITH
   `rollout_consistency_loss`; decay=1.0 flat control). Chip to `/queue-experiment`.
3. **Declare the gate** on `f_dominance_conversion_ceiling` (Section 1 block), on
   `behavioral_diversity_isolation:GAP-I` / `GAP-K`, and on the seven campaign nodes
   (Section 3), so the closure snapshot and drift report stop reporting "no unresolved
   dependencies" for an entry that has three.
4. **Recoup rung 3 to V3** (E3 channel-scale normalisation) and decide it TOGETHER with
   GFLAG-0051 (ARC-007: does E3 get an action-object input channel, or is "E3 introduces ALL
   weighting" strict?) -- both are the same question about what E3's score sum is allowed to
   contain and on what scale. A contested-disposition flag is raised for this.
5. **Re-point the hypothesis-space hero** from `competence_floor` (decided 2026-07-25, closed
   2026-08-08) to `conversion_ceiling_root`, and correct that question's `decision.live_gate`,
   which still reads "return-decomposition diagnostic NOT yet queued" although V3-EXQ-808 ran
   2026-07-24 and the leg's own resolution cites it. Extends GFLAG-0093.
6. **Name ORNT-1's blocker** in the plan frontmatter (the only node whose gate is undeclared
   in its own plan).
7. **Refresh `insights_report.md`'s front section** so `CURRENT_FRONT.md` derives a headline
   again (it has printed "could not derive" on 39 of the last 48 regenerations). Done in this
   session; see the report's provenance note for what was and was not re-measured.

---

## 7. Bearing on the 2026-09-01 flag triage

The triage found 0 of 33 stale/discrepancy flags self-resolved and left 12 contested briefs
unapplied. This synthesis does not re-do that work; it gives governance a single criterion that
decides several of them at once:

- **Decided by the binding constraint:** GFLAG-0058 (MECH-263/SD-033b notes end at 485m; the
  FULLSTACK handoff closes into Section 1), GFLAG-0069 (ARC-108/MECH-450 upstream is the
  interface gate, already corrected on the node 2026-09-01), GFLAG-0072 (class floor -- a
  Section 4 precondition), GFLAG-0093 (front-doc hero -- Recommendation 5).
- **Contested, and the constraint is the deciding fact:** GFLAG-0051 (ARC-007 / MECH-151 --
  Recommendation 4), GFLAG-0091 (ARC-003's unrunnable falsifier is unrunnable for exactly the
  Section 5 reason; it becomes runnable when the interface lands, which is an edge, not a status).
- **Unaffected:** the ARC-004, replay/consolidation, MECH-317 and phase-label clusters
  (GFLAG-0055/0088, 0076/0086, 0066/0084/0087, 0109/0112/0113). Those stand on their own briefs.

---

*Held-out check (GOV-HELDOUT-1) not applicable: this record changes no standing rule. The
falsification condition in Section 5 is the check that applies to a synthesis.*
