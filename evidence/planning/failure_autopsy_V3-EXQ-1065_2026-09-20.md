# Failure autopsy -- V3-EXQ-1065 (SD-106 PC-recoverability probe + MECH-566 reconditioning falsifier)

Status: confirmed (Step 8 gate held 2026-09-20, user present; red-team opus cross-model CONTESTED, revisions applied)
Target: `v3_exq_1065_sd106_subspace_overlap_mech566_recondition_20260919T223401Z_v3` -- diagnostic, run-level FAIL, self-route `recoverability_indeterminate__mech566_conditioning_falsified`, direction mixed (SD-106 unknown, MECH-566 weakens). ree-cloud-2, 183 s, seeds 42/43/44.

## 1. Facts (verified cell-by-cell by the red-team pass)
Dry-run gate clean. validate_recording OK. A real P0a training run (60 episodes x 200 steps, `dry_run: false`); short because only 2 of 17 arms per seed train and the rest are probe fits on the captured buffer. All 9 readiness gates green, both halves non-degenerate. The in-run diag cell reproduces V3-EXQ-1023a's consumer-rung values exactly (0.7542 / 0.7356 / 0.6921, delta 0.0).

| seed | parity | P1 PC-recoverability | class | best reconditioning lift (M1) | class |
|---|---|---|---|---|---|
| 42 | 0.985 | 0.869 | INDETERMINATE | -0.0042 | FALSIFY |
| 43 | 0.980 | 0.819 | INDETERMINATE | -0.0078 | FALSIFY |
| 44 | 0.979 | 0.817 | INDETERMINATE | +0.0107 | FALSIFY |

P1 bands: LOW < 0.75, HIGH > 0.90; untrained-encoder control reads 0.50 (the statistic can read low). M1 bars: confirm >= 0.05, falsify < 0.02 under every member. Transforms invertible (1e-9), non-trivial (condition number 13.4), and they reach the decoder (final CE differs from diag 3/3).
Recorded, unscored: converged L-BFGS linear probe SD-106 0.626 vs PCA-32 0.857 (gap 0.231); gap fraction closed by the best member -0.013.

Dry-run gate: check_dry_run_citations.py run 2026-09-20 over all 11 cited run_ids (1039, 1039a, 1043, 1043a, 1057, 1057a, 1060, 1063, 1065, 1069, 1070): 0 dry, 11 clean. validate_experiments --checks dry_run_unreachable_criterion: silent on all nine drivers; reduction blocks read by hand.

## Target V3-EXQ-1065 -- diagnostic FAIL, claims SD-106, MECH-566
`v3_exq_1065_sd106_subspace_overlap_mech566_recondition_20260919T223401Z_v3`

**Self-route** `recoverability_indeterminate__mech566_conditioning_falsified` -- adjudication: CONFIRMED on both halves, with the MECH-566 half NARROWED. The run-level FAIL is a combination-rule artefact (PASS required both halves determinate); all 9 readiness gates green, both halves non-degenerate. Half B executes the ZCA member of MECH-566's registered falsifier and it FALSIFIES on 3/3 seeds. Half A landed mid-band on all three seeds ('recorded, no routing').

**Failed criterion.** P1 (SD-106 PC-recoverability) INDETERMINATE 0.835 in [0.75, 0.90] on 3/3 seeds -> run-level FAIL. M1 (MECH-566) determinate FALSIFY 3/3.

### Four-layer diagnosis
- **claim_alignment**: MECH-566: weakened, NARROWLY (ZCA member vs a standardised baseline; standardisation member confounded with the baseline and unmeasured). SD-106: unclear -- P1 indeterminate by pre-registration.
- **biological_reference**: partial -- output-null vs output-potent subspaces (Kaufman 2014) and communication subspaces (Semedo 2019) ground the idea that geometry can gate what a reader sees; MECH-566 itself is a formal import (GL(32) invariance of a freely-decoded reconstruction loss, Baldi & Hornik 1989).
- **prerequisites**: present -- SD-106 trained at P0a epochs=40 (1320/1320/1160 steps), latent not collapsed (PR 16.3-17.7), in-run diag cell reproduces V3-EXQ-1023a EXACTLY (delta 0.0 on all three seeds).
- **implementation**: complete -- transforms invertible (1.05e-9), non-trivial (condition number 13.4), and they reach the decoder (final CE differs from diag on 3/3 seeds).
- **environment**: adequate
- **measurement**: adequate for the ZCA member, with a power caveat: the instrument's demonstrated sensitivity (V3-EXQ-1008, +0.03..+0.05) came from a DIFFERENT ZCA estimator (absolute 1e-6 floor; x1065 uses a relative ridge and logs the change as a fixed defect), a different agent family and a fuller warm-up, on a code with 2.4x more train-side headroom for whitening (+0.18 vs +0.077). The same-convention control that survives is LDA. M1 is NOT degenerate by construction: the consumer is not converged and whitening moved train agreement and CE substantially. P1 is certified on its LOW side only (untrained 0.50); nothing shows the statistic can reach >= 0.90.
- **integration**: coupled
- **scale**: adequate (3 seeds unanimous; seed-majority rule 2)

### Failure location (GOV-FAILLOC-1)
- **mechanism**: established
- **measures**: established
- **environment**: established
- **ree**: False
- **net_classification**: NOT a REE failure and not an instrument failure: a fair test of a candidate explanatory hypothesis (MECH-566) that came back negative. 'ree' stays false because the thing that failed is the hypothesis about WHY SD-106 under-transfers, not a REE competence.

### Biological reference
- **closest_mechanism**: output-null / output-potent geometry gating a downstream reader
- **dependencies**: []
- **is_formal_import**: True
- **divergence**: MECH-566 predicts a GL(32)-conditioning obstacle. ZCA removes that conditioning, fit improves, transfer does not. The claim's own falsifier names what is left: content OR nonlinear warp. The converged-linear gap (0.231) being LARGER than the MLP-rung gap (0.142) means a nonlinear reader recovers the difference -- evidence for warp, not for missing content.
- **lit_status**: present -- MECH-566: targeted_review_objective_consumer_transfer (11 entries); SD-106: targeted_review_sd_106 (5 entries landed 2026-09-18: Zhang 2021 task-relevant vs reconstruction, Poort 2015, Fu 2021, Tomar 2021 + one MI-objective entry) -- the generic-vs-task-relevant lit-pull the 1023a autopsy commissioned HAS landed; its two 'weakens' + three 'mixed/weakens' directions agree with the content reading here

### Claim-layer recommendation
- direction: `mixed` per claim {"SD-106": "unknown", "MECH-566": "weakens"}
- epistemic_category: `standard` -- MECH-566: fair test, negative result -- ordinary claim pressure, no suppression. SD-106: indeterminate read, nothing to assert.
- per claim: SD-106: STANDS [none -- stays implemented]; MECH-566: MECH-566 carries no adjudication flag yet and its evidence_quality_note still reads NO EXPERIMENTAL EVIDENCE; write the note above and -> set diagnostic_evidence_adjudicated true [none -- stays candidate (first evidence; one run on one code is not grounds for more)]

**Draft evidence_quality_note.** V3-EXQ-1065 (diagnostic; run-level FAIL by combination rule only; all readiness green). MECH-566: WEAKENS, narrowly -- the ZCA member of its registered family, applied to the frozen SD-106@epochs40 code, gave no held-out lift on 3/3 seeds (-0.0042 / -0.0078 / +0.0107; confirm bar 0.05) against an already per-component-standardised baseline; the family's other member (per-component standardisation) IS that baseline and is unmeasured here and lineage-wide; LDA (supervised, outside the registered family) was also null and is the only member sharing V3-EXQ-1008's ridge convention. The transform was not inert: it raised TRAIN agreement by +0.069 / +0.076 / +0.086 and cut final CE 38-44%, none of which transferred -- reconditioning accelerates the consumer's fit and buys no generalisation on this code. Registered supporting readout (b) fired: a converged linear probe trails PCA-32 by 0.231 (claim named ~0.14) -> the deficit is in the code, not the consumer's optimisation; per the falsifier's own wording what remains is 'content OR nonlinear warp', and a nonlinear reader recovers 6-13x more from the SD-106 code than from PCA-32, which points at warp. SD-106: UNKNOWN -- PC-recoverability 0.835 mid-band 3/3; the statistic's HIGH band has no reachability evidence. Pre-registered M1_FALSIFY route: MECH-567 (target-carrying head). failure_autopsy_V3-EXQ-1065_2026-09-20.

### Substrate queue
- **action**: amend
- **target_sd_id**: SD-106
- **note**: BOOKKEEPING ONLY -- no build. Attribution note for SD-106's failure_record: linear GL(32) reconditioning (ZCA) accelerates consumer fit and buys no held-out transfer on the epochs=40 code; remaining explanations are content OR nonlinear warp (nonlinear recovery ratio 6-13x favours warp). Also owed: GFLAG-0368 (EXP-0250 proposed -> executed by V3-EXQ-1065).
- **failure_record_entry**: {"run_id": "v3_exq_1065_sd106_subspace_overlap_mech566_recondition_20260919T223401Z_v3", "experiment_type": "v3_exq_1065_sd106_subspace_overlap_mech566_recondition", "metric": "attribution_note: ZCA held-out lift -0.0004 mean (3/3 FALSIFY) with TRAIN lift +0.077 and CE -38..-44%; converged linear probe SD-106 0.626 vs PCA-32 0.857; linear->mlp128 recovery +0.08..+0.12 on SD-106 vs +0.006..+0.019 on PCA-32", "target": "n/a -- attribution; SD-106's open acceptance target (>= 0.85 at the mlp128 consumer rung) is unchanged", "resolved": "open"}

### Brake, granularity, debt class
- re-derive brake: fired=False, literal count 0. SD-106 and MECH-566 literal count 0; this target is direction mixed / category standard and does not count.
- granularity trigger: fires=False. SD-106: 3 tagging targets, alignment weakened=2 unclear=1 -- but the signatures do NOT differ structurally (all three read the same consumer-rung shortfall), and this target adds 'unclear'. MECH-566: 0 targets. Does not fire. The standing h_other_event on zworld_actor_adequacy_locus (rotation -> /claim-synthesis on MECH-457/INV-088) is unaffected.
- debt class: MECH-566: resolved for this code. SD-106 which-directions: complex (probe-gated) / mystery (known data) -- the question is frozen pending a re-pose (GFLAG-0312), not pending another probe.

### Learning extracted
- A cheap pre-registered falsifier on a frozen code is the right shape: 183 s, unanimous, non-degenerate.
- Report the in-run effect of a manipulation, not only that it 'reached' the DV: +0.077 train agreement with 0.000 held-out lift is a sharper result than 'no lift'.
- When a claim's falsifier names a family, check every member against the BASELINE: here one of two members is the baseline.
- An imported positive control is only a control if the estimator is the same. Carry the convention (ridge, agent family, warm-up) with the number.
- A two-claim run should not AND its halves into one outcome.
- SD-106 lists MECH-566 in depends_on although MECH-566 is a later hypothesis about SD-106's shortfall; with MECH-566 weakened the edge deserves review (GOV-EDGE-1).

### Routing: `queue-experiment`
- **pre_registered_route**: M1_FALSIFY -> MECH-567 (target-carrying head: an oracle-action or reward/RPE cross-entropy head on the same latent during P0a, with its mandatory co-measurement and degeneracy pre-check). Registered candidate, v3_pending, in SD-106's depends_on; no chip, queue entry or claim carries it (2026-09-20). Reported for /governance to chip after ratification; this session spawns nothing.
- **ordering_constraint**: zworld_actor_adequacy_locus carries an h_other rotation (2026-09-17): /claim-synthesis on MECH-457 / INV-088 BEFORE any further rescue run on a surviving leg. V3-EXQ-1065 Half A probed the surviving leg H-which-directions AFTER that constraint (opening no leg, but probing one). Whether MECH-567 counts as a rescue run on that question is a user call.
- **gflag_0312**: OPEN and unassigned; it names /failure-autopsy as the only author of the re-pose. This sweep DECLINES to author it: a re-pose of a four-portfolio question needs its own session, not a paragraph in a nine-run sweep. Stated so it is not read as discharged.
- **sd106_literature**: landed 2026-09-18 (targeted_review_sd_106, 5 entries)

### Hypothesis ledger (Step 9b)
- **qid**: zworld_actor_adequacy_locus
- **mode**: B, minimal
- **H-which-directions**: alive, unchanged. resolving_runs += V3-EXQ-1065 with basis 'P1 PC-recoverability 0.835, INDETERMINATE on 3/3 seeds, pre-registered as recorded-no-routing; HIGH band unanchored'. No growth, no new leg; growth_restriction not engaged (no hypothesis added).

### Step 7b pre-routing fires
- C3: ACTED ON -- the first draft repeated the 1023a autopsy's 'literature ABSENT for SD-106'; 5 entries landed 2026-09-18. lit_status and routing corrected.

### Step 7c red-team
- **model**: opus (claude-opus-5[1m]); drafting session was fable -- cross-model pass
- **verdict**: CONTESTED
- **disposition_survived**: True
- **accepted**: ["F1 'content, not conditioning' dropped the registered 'or nonlinear warp' disjunct; cells favour warp", "F2 registered supporting readout (b) fired and was unmentioned", "F3 'same members' false for ZCA (ridge convention changed)", "F4 shipped predicate is ZCA-only; standardisation member is the baseline, unmeasured", "F5 large unreported in-run effect on train fit", "F6 pre-registered MECH-567 route dropped", "F7 P1 HIGH band unanchored", "F8 GFLAG-0312 treated as owned"]
- **cleared**: the primary attack -- M1 degenerate by construction (linear map absorbable by the MLP's first layer) -- did NOT hold: consumer unconverged, whitening moved train agreement +0.077 and CE -38..-44%
- **what_changed**: weakens KEPT but narrowed; routing governance-note-only -> queue-experiment (MECH-567, reported not spawned); 'content' -> 'content or warp, cells favour warp'; ledger note added; GFLAG-0312 explicitly declined.
- **cheap_confirmers_run**: all load-bearing numbers recomputed from cells and matched; brake 0

