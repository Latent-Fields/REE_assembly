# Failure autopsy -- MECH-320 defect cluster (GFLAG-0403; ARC-068 folded from GFLAG-0399)

Generated 2026-09-23T19:41:57Z. Scope: cluster (4 runs + 1 claim-level read).
Status: **confirmed** (interactive gate 2026-09-23T20:05:26Z). Red-team pass: **fable** (cross-model;
drafted on opus), verdict **CONTESTED on characterisation, every disposition survived** -- both
contested points accepted and corrected below (919 Stage-2 exposure; ARC-068 v_t wording).
Chip: chip-20260923-mech320-defect-autopsy. Re-adjudicates, on ONE new question only, the confirmed
autopsies of V3-EXQ-844 (2026-08-01), V3-EXQ-904 (2026-08-09), V3-EXQ-919 (2026-08-13) and the
substrate-readiness cluster (2026-09-02, which covers 544a's predecessor 544 and discusses 544a).
All four were read end to end before this was written.

## The question

GFLAG-0403 (governance 2026-09-22): GOV-SUBPATH-1 reported runs whose drivers "import"
`ree_core/policy/tonic_vigor.py` after substrate_queue entry MECH-320 (severity corrupting) recorded
its defect. It named five scoring items needing adjudication: v3_exq_544a (supports, MECH-313 +
ARC-065), v3_exq_844 and v3_exq_919 (weakens, MECH-321), v3_exq_904 (supports, ARC-070), and a
fifth "read 844/919 together" note. The worry: a bias channel silently contributing zero can
manufacture a negative (844/919) or a readiness PASS (544a).

## Premise audit (re-measured before building on it)

1. **"Drivers import tonic_vigor.py" -- FALSE for all four (no direct import).** None imports
   `ree_core.policy.tonic_vigor`. (`ree_core/policy/__init__.py` itself imports tonic_vigor at load
   -- class/constant definitions only, inert while `use_tonic_vigor` is False.) All four do `from ree_core.policy import <X>` (ChunkedPrimitive in
   844:207 / 904:90 / 919:188; NoiseFloor in 544a:71). GOV-SUBPATH-1's `_modules_overlap()`
   (`REE_assembly/scripts/check_substrate_path_overlap.py:301-310`) returns True when
   `target.startswith(imp + ".")`, and `resolve_driver_imports()` adds the bare package of every
   from-import -- so importing ANY name from the `ree_core.policy` package reads as importing every
   submodule of it, tonic_vigor included.
2. **"Five are scoring" -- FALSE for 544a.** Both its claim_evidence rows carry
   `scoring_excluded=diagnostic_probe`; it weights nothing (the 2026-09-02 cluster autopsy already
   established this). Scoring runs in this set: 844, 919, 904.
3. **The quoted defect text is superseded.** The 571 failure_record text ("all diversity bias
   components contribute 0.0 ... not propagating") was corrected on 2026-05-26
   (`arc065-failure-record-correction-20260526T064946Z`, root cause in
   `evidence/planning/v3_exq_571_root_cause_2026-05-25.md`): the channels ARE composed into
   score_bias at `e3_selector.py:737`; per-candidate spread collapses because E2 world-forward
   maps K candidates to one first-step z_world. The correction reached the ARC-065 and MECH-314
   substrate_queue rows but NOT the MECH-320 or MECH-313 rows, which still carry the old text.
4. **What "corrupting" actually describes** is the tonic-vigor-specific 951c defect: under default
   `baseline_mode='none'` v_raw is never positive, so `v_t = max(v_t_floor, max(0, v_raw) * gates)`
   is pinned AT the floor independently of the gates (`tonic_vigor.py:432-433`) -- 0.0 at the
   shipped default, 0.05 where a driver forced it. The scalar never moves.
5. **Execution condition.** `use_tonic_vigor` defaults False (`ree_core/utils/config.py:5189`);
   `agent.py:2068-2089` builds the module only when True, and every call site is
   `is not None`-gated. `use_dacc`, `use_lateral_pfc_analog`, `use_ofc_analog`,
   `use_structured_curiosity` also default False. **None of the four drivers sets any of them**
   (driver config construction, manifest `config` / `enabled_default_off_flags` /
   `arm_config_slices` all checked).

Dry-run gate: `check_dry_run_citations.py` over the 4 targets + the 571 and 951c runs: 0 dry,
6 clean; `--family` for each target: 0 dry.

## Per-run adjudication

| Run | Claim(s) | Scoring? | Lever | Touches defect? | Disposition |
|---|---|---|---|---|---|
| 544a | MECH-313, ARC-065 | no (diagnostic_probe) | NoiseFloor softmax temperature; UC1-UC5 plumbing | no | supports STANDS (already neutralised) |
| 844 | MECH-321 | yes | persistent committed-program handle (commitment visibility) | no | weakens STANDS |
| 919 | MECH-321 | yes | two-stage harm-aware selection | MECH-320: no. Both stages exposed to E2 per-leaf collapse -- unmeasured | weakens STANDS, **conditional** + diagnostic |
| 904 | ARC-070 | yes | MECH-288 boundary trigger count | no | supports STANDS |

**544a.** A readiness diagnostic: instantiation, arithmetic of `max(baseline+alpha, min_T)`, a
wiring contract. No criterion measures selection. MECH-313's NoiseFloor is a uniform softmax
temperature (agent.py ~9200), not a per-candidate additive bias and not a `cand_world_summaries`
consumer -- outside both the corrected 571 root cause and the 951c defect. MECH-320's failure_record
"target" names MECH-313 on the superseded framing; 571's temporal-variance decomposition cannot
see a temperature-type effect at all (noise_floor_temp is near-constant by construction;
bias_fraction ~1e-32 while the lift arithmetic reads 1.0999999999999996).

**844.** The only manipulation is `use_persistent_committed_program_handle`. The 2026-08-01
autopsy code-traced the C1 failure to `_apply_policy_decomposition` having NO ranked-selection
step -- there was no scored selection for a zero-contributing bias to distort. No MECH-320-family
flag is on in either arm. *New hygiene finding (not in the prior artifact):*
`substrate_stable_across_run: false` with an arm-correlated split -- all six ARM_HANDLE_OFF cells
under substrate_hash 3ad9562b0b, all six ARM_HANDLE_ON cells under 697e8bd687. Inert for this run:
both fingerprints are per-arm snapshots ~20 min apart inside ONE in-process run (no subprocess),
so the executed code was imported once; the delta is exactly one `experiments/_lib` line plus two
new `_lib` files (dACC readout fix 51c3d3c), zero `ree_core`, none imported by this driver
(argument supplied by the red-team, adopted). Supporting but partial: on the three
non-decomposing seeds (47, 23, 53) action_sequence and per_tick_harm are bit-identical across arms
(recomputed) -- that covers the shared path, not the re-tiling path used only on seeds 3/71/89.

**919.** The MECH-320 defect is absent (no MECH-320-family flag set). A DIFFERENT exposure is
live and unmeasured. Both stages of harm-aware selection consume the SAME per-leaf `harm_penalty`
(`hippocampal/module.py:1263-1275`), read by `_decomposition_harm_penalty` (`module.py:1128`) off
each leaf's own `e2.rollout_with_world` predicted states. Stage 1 turns it into an additive term in
`dacc_score_bias` (`agent.py:8909-8950`); Stage 2 (`select_harm_aware_leaves`) takes an argmin over
it. If E2 world-forward collapsed per-leaf predictions (the corrected-571 root cause), Stage 1
would be a constant offset and Stage 2 a tie that keeps `items[0]` -- a harm-blind pool cut. Stage 2
fired on 6831 of 6977 decompositions (97.9%), so the recomputed ON-vs-OFF action divergence (mean
0.419, range 0.000-0.817, zero on 1 of 40 seeds) shows the treatment moved behaviour but CANNOT
show it was harm-informed.

*Withdrawn from the first draft (red-team B1, confirmed by source read):* "Stage 2 is categorical
pool admission and cannot be drowned" (false -- it consumes the same penalty) and "behaviour moved,
therefore not a defect artifact" (a non-sequitur for this exposure).

Bound, not measurement: contemporaneous August trained-agent runs record nonzero per-candidate
spread -- `consumed_summary_pairwise_dist_mean` 0.080-0.095 (847/847a/851/858; other cells
0.021-0.158), `cand_world_pairwise_dist_mean` 0.124 (925; other cells 0.024-0.157) -- against
0.0000 in the May untrained-agent measurement, with some cells below the 0.05 GAP-A floor.
Different drivers and configs; no 867/867a/867b/919 run recorded per-leaf penalty spread or the
Stage-2 tie rate. **Confirmed disposition: conditional weakens** -- see routing.

**904.** The load-bearing criterion counts MECH-288 boundary fires driving decompositions (180),
from rollout latents and PE. No read of score_bias or any of the five channels anywhere in the
chain. Detector statistics are out of reach of a score-bias propagation defect by construction.

## ARC-068 (claim-level, from GFLAG-0399)

GFLAG-0399 lists ARC-068 as having decisive runs "all tagged MECH-320". ARC-068's implementation
IS MECH-320's `w_passive * v_t` term (2026-05-16 collapse; `tonic_vigor.py:468, 481`). Its three
tagged runs (624a/b/c) are already non_contributory. Those runs and MECH-320's 951/951c forced
`v_t_floor=0.05`: v_t sat AT the floor (never moving, per the 951c defect) but was nonzero, so the
no-op cost reached the score -- and never flipped a selection (624a action_density byte-identical
ON vs OFF, selection-authority ceiling; 951 action_density saturated at 1.0). At the shipped
default floor 0.0 the term is identically zero. No MECH-320-tagged run is a hidden ARC-068 test;
exp=0 / v3_pending is correct, not a bookkeeping miss. Integration: coupled but inert -- inert by
DEFECT (pinned v_t; no selection headroom). *Withdrawn (red-team B2, confirmed by driver grep):*
first-draft "later MECH-320 runs have v_t pinned at 0.0" -- they set the floor to 0.05.

## Four-layer (cluster read)

| Layer | Status |
|---|---|
| Claim alignment | unchanged on every target; none invalidated by the defect |
| Biological reference | not implicated by this question |
| Prerequisites | ARC-068: missing (live v_t, selection authority); others unchanged |
| Implementation | 919 complete-as-built; discriminative harm input unmeasured; ARC-068 partial |
| Environment | unchanged |
| Measurement | 919 under-instrumented for "was it harm-informed" (no per-leaf spread / tie rate); 544a plumbing (contained) |
| Integration | ARC-068 coupled but inert (by defect) |
| Scale | unchanged |

**Failure-location (GOV-FAILLOC-1):** for 844 and 919 unchanged from their confirmed autopsies
(844 MECHANISM, implementation partial); 919 now MIXED (mechanism input-discriminability
unmeasured + MEASURES partial). Neither is chargeable to the MECH-320 defect; neither is REE FAILED.

## Cluster pattern

One structural property, not four bugs: the flag's signal (a package-prefix import match) is not
the defect's execution condition (`use_tonic_vigor=True`), and the failure_record text it quotes
was superseded on two of the four rows that carry it.

## Confirmed routing (interactive gate, 2026-09-23)

All three recommended options accepted (recommendation ledger rec-20260923-6f5786ff /
-fd1d6139 / -f0750907).

- **Dispositions:** 544a, 844, 904 STAND (no edit). **919: conditional weakens** -- direction stays
  weakens; append the per-leaf harm-input exposure caveat to MECH-321's evidence_quality_note
  (exact text in JSON). ARC-068: set `epistemic_category: standard` (it has none) and append the
  no-hidden-decisive-run note.
- **Follow-on for governance to chip after ratification (NOT spawned here):** `/queue-experiment`
  diagnostic -- replay 919's ARM_SELECTION_ON config on a few seeds reusing 867a's
  `_decomposition_harm_penalty` monkeypatch; record per-leaf harm_penalty spread per decomposed
  chunk, Stage-2 argmin tie rate, and per-candidate predicted-state distance. Both directions
  declared: high tie rate -> 919 re-adjudicates to non_contributory (MECH-321 then carries only
  844's weakens); low tie rate -> the conditional weakens becomes unconditional. Also for the
  successor: 919's OFF-arm forward-PE positive control is near-degenerate (var 5.6e-8 at mean
  0.0095) -- not load-bearing here.
- **substrate_queue bookkeeping:** propagate the 2026-05-26 corrected 571 text onto the MECH-320
  and MECH-313 rows (mark the old item `superseded`). Keep MECH-320 severity corrupting (the 951c
  item carries it); note its blast radius is runs with `use_tonic_vigor=True`. For MECH-313, note
  that 571's variance-fraction bar is the wrong instrument for a temperature mechanism.
- **Flags:** resolve GFLAG-0403; resolve GFLAG-0399's ARC-068 sub-item.
- **Not adjudicated here, governance-owned:** V3-EXQ-919's confirmed 2026-08-13 routing (amend
  SD-hazard-aware-policy-decomposition with escapability / threat-predictability + a 919
  failure_record) is unapplied -- that row holds only the 844 item, and the 919 artifact's null
  per_claim_recommendation hides it from GOV-APPLY-1.
- **Tooling (out of this autopsy's claim routing; user-approved chip):** GOV-SUBPATH-1's
  package-prefix over-match and its evidence_direction-only "scoring" test would keep re-presenting
  all 19 runs every cycle. Spawned `chip-20260923-govsubpath1-package-prefix-fix` (task_9ca1f55d),
  recorded in the chip ledger.

## Checks

- Re-derive brake: not fired on any claim (no ceiling readings; all categories `standard`).
- Granularity-debt: does not fire (MECH-321 distribution unchanged: weakened=2, signatures already
  judged structurally different on 2026-08-13; ARC-068/ARC-070 have no weakened target).
- Step 7b: 2 C2 fires (existing substrate entries unblocking MECH-313/ARC-065 and ARC-068) --
  dismissed: this autopsy changes no routing and owes no build; those entries proceed
  independently. C5 did not fire; nothing inapplicable.
- Step 7c red-team (fable): CONTESTED on characterisation, all arithmetic reproduced (919
  divergence 0.4186; Stage-2 sum 6831; 844 hash split and inert-seed identity). B1 and B2 accepted
  and corrected above; the 844 in-process-snapshot argument adopted; hygiene "not directly imported"
  adopted.
- Step 9b: no ledger write owed. `mech321_harm_aware_selection_task_effect` /
  `H-harm-aware-reduces-task-harm` stays eliminated by 919; no fan-out.
