# Failure Autopsy: V3-EXQ-1026 (MECH-423 sleep-integrated E2 consolidation)

**Status: DRAFT -- staging mode, awaiting human confirmation. Nothing in this file has been applied to claims.yaml or substrate_queue.json.**

- Generated: 2026-09-14T17:47:24Z
- Scope: single target
- run_id: `v3_exq_1026_mech423_sleep_integrated_e2_consolidation_20260914T111100Z_v3`
- queue_id: `V3-EXQ-1026`
- claim_ids: `MECH-423`
- experiment_purpose: `diagnostic`
- outcome: **PASS** (clean, all 4 load-bearing criteria passed non-degenerately, for the narrow question the driver actually poses)
- Step 7c red-team verdict: **CONTESTED** (see Section 6b) -- the PASS is real; the causal scope the drafting artifact initially attached to it (an "INV-063 unblock") was wrong and has been corrected below.

## Why this autopsy exists

`V3-EXQ-1026` is `experiment_purpose: "diagnostic"`. Per the skill's trigger rule, **every**
diagnostic-purpose result -- PASS or FAIL, flagged or not -- requires this autopsy before
governance can act on it. This one landed a clean PASS with no indexer adjudication flag; the
central question is whether the PASS is real, and what exactly it establishes.

## 1. Facts reconstruction

**What the driver tests.** `ree-v3/experiments/v3_exq_1026_mech423_sleep_integrated_e2_consolidation.py`
validates the SLEEP-INTEGRATED call site (`SleepLoopManager.force_cycle -> phase_manager.py
_run_cycle`, ~lines 669-693) that wires MECH-423's R3 `CrossModuleConsolidator` into a real sleep
cycle. This is distinct from `V3-EXQ-680e` (already-PASSed, cloud class), which validated R3 only
via a DIRECT `CrossModuleConsolidator.consolidate()` call (`sleep_driver_pattern: "N/A ... no
sleep cycle"`). Confirmed 2026-09-08 by grep over `evidence/experiments/*.json`: no prior landed
manifest exercised the integrated call site.

**Design.** Two arms, seed-matched, 3 seeds (42/123/456):
- `ARM_SLEEP_INTEGRATED_ON` -- `use_cross_module_consolidation=True`, `cmc_steps=8`. The hook fires
  inside `force_cycle()`.
- `ARM_SLEEP_INTEGRATED_OFF` -- `use_cross_module_consolidation=False` (consolidator is `None`,
  guard skips the hook). Same seed, same waking rollout, same sleep cycle otherwise. This is the
  negative control: `agent.e2` parameters must be bit-identical before/after.

Each cell: a real waking rollout (3 episodes x 60 steps = 180 real `record_transition()` calls,
>10x the 16-transition floor) populates a real E2 transition buffer, then exactly ONE
`agent.sleep_loop.force_cycle(agent)` fires, and `max|delta|` over `agent.e2.parameters()` /
`agent.e1.parameters()` is measured before/after.

**Load-bearing criteria (ON arm) + negative control (OFF arm):**

| Criterion | Measured (min/max across 3 seeds) | Threshold | Passed |
|---|---|---|---|
| C1 cross_module_consolidation metrics merged (all ON cells) | true (all 3) | -- | yes |
| C2 E2 touched under interleaved schedule (`updates_e2`) | min 8.0 | >= 1.0 | yes |
| C3 E2 weight delta positive, sleep-integrated (ON) | min max\|delta_e2\| = 0.00769036 | > 0.0 | yes |
| C4 OFF-arm E2 bit-identical negative control | max max\|delta_e2\| = 0.0 (exact) | <= 0.0 | yes |

Combination rule: PASS iff ALL of C1-C4 (plain AND). All 4 passed -> outcome PASS,
`evidence_direction: supports`, `interpretation.label: sleep_integrated_e2_consolidation_confirmed`.

**Preconditions (readiness gate, all met, all 3 seeds x 2 arms):** `e2_transition_buffer_populated`
(measured 180 >= floor 16), `e2_loss_nonzero_on_real_transitions` (measured > 0, rules out a
degenerate all-zero replay buffer masquerading as "hook didn't fire"), `sleep_cycle_fired`
(the unconditionally-merged `post_sleep_z_goal_retention` key present in both arms).

**Design-time red-team (already run, pre-queue, by a different model -- opus, per the driver's own
docstring).** CONTESTED, 2 findings, both fixed before this run was queued (the
`e2_loss_nonzero_on_real_transitions` precondition and the `sleep_cycle_fired` assertion). This
autopsy's Step 7c red-team (Section 6b) is a SEPARATE, post-hoc pass over the actual landed
manifest and found a different, more consequential issue.

**2a. Dry-run gate.** `check_dry_run_citations.py` on this run_id: 0 dry cited, 1 clean. Not a
smoke -- full 3-episode x 60-step waking rollout, 3 seeds, both arms (re-confirmed independently by
the Step 7c red-team). `dry_run_unreachable_criterion` lint: no hit for this driver.

**Recording provenance.** `validate_recording.py --strict` over this manifest: **0 always-core
gaps** (re-run independently by the Step 7c red-team, same result). `substrate_hash`, `config`,
full `seeds: [42, 123, 456]`, `machine`/`machine_class`, `elapsed_seconds`, `substrate_commit`
(non-dirty) all present. `substrate_stable_across_run: true`.

**Queue entry.** Not present in the live `ree-v3/experiment_queue.json` (already cleared, normal
queue-completion behaviour for a scored PASS). `claim_ids: ["MECH-423"]`, `experiment_purpose:
"diagnostic"` confirmed from the manifest itself.

**Failed criterion:** none -- clean PASS. (No absolute/discrimination/negative-control criterion
failed; C4 is itself the negative control and it passed.)

## 2. Claim-layer mapping

**MECH-423** (`claims.yaml`): "Cross-model super-additivity... integrated beats a
param/compute-matched bag of isolated modules." Status `provisional`, `epistemic_category:
standard`, `implementation_phase: v3`. Promoted to provisional 2026-07-16 on `V3-EXQ-680e`'s clean
experimental PASS (direct-call validation of the same R3 consolidator).

**Does this run test the claim under conditions where it could express itself?** Not directly --
and the driver says so itself: `experiment_purpose: "diagnostic"` is explicitly scoped as
"substrate-readiness validation of an already-implemented wiring path, not new evidence for the
MECH-423 hypothesis itself (that evidence is 680e's)." `claim_ids: ["MECH-423"]` is present for
context/traceability, matching the skill's own guidance that a diagnostic run's claim tag does not
imply it should move confidence/conflict scoring. **No evidence_direction/epistemic_category
change is recommended for MECH-423.**

**Bears on INV-063 -- CORRECTED after Step 7c red-team (see Section 6b for the full finding).**
`substrate_queue.json`'s `mech423-sleep-integrated-e2-consolidation-hook` entry states, in its own
`unblocks_note`, that `INV-063` leg B (across-sleep world-forward prediction-error improvement) "is
blocked_substrate on exactly this: its leg B DV is structurally 0.0 in every arm at every seed
until a sleep-integrated world-model update is shown to exist. This entry is that showing." **That
framing is inaccurate for THIS run's result.** `E2` has two disjoint heads --
`predict_next_self` (trained by `agent.compute_e2_loss`, the only loss this hook computes for E2)
and `world_forward` (its own docstring: "NOT trained as E2's primary objective"). This run's C3
delta is confined entirely to the self-forward head; an independent per-named-parameter probe
(Step 7c) confirms `world_forward` moved by exactly 0 in every ON-arm cell. `INV-063` leg B's
frozen-probe DV (`V3-EXQ-701b`/`701c`) reads `agent.e2.world_forward` specifically. **So this run
does NOT unblock INV-063 leg B** -- it shows the hook fires and trains E2's self-forward head
through a real sleep cycle, which is a real and useful confirmation, but a narrower one than the
substrate_queue entry's own prior framing claimed.

## 3. Biological-reference triage

**Closest mammalian/human reference mechanism:** sleep-dependent offline consolidation of a
forward/predictive model via local, replay-driven synaptic reweighting during a designated offline
phase -- the systems-consolidation family (hippocampal-to-cortical replay, sleep-dependent synaptic
reweighting) that motivates SD-017 and MECH-121 generally.

**Formal import or faithful translation?** Faithful, and narrowly scoped: `CrossModuleConsolidator
.consolidate()` builds LOCAL, per-module Adam optimizers scoped only to `agent.e1.parameters()` /
`agent.e2.parameters()` -- not a global objective, not a formal-definition import. No divergence
from biology is introduced by this run.

**Literature status:** MECH-423 / SD-017 already carry literature grounding from prior work; no
fresh `/lit-pull` is owed here.

**Does the result resemble a missing-dependency signature?** No -- this is a clean confirming PASS
with a decisive negative control (exact-zero OFF-arm delta over all E2 parameters, including
`world_forward`), not a failure pattern to diagnose against a missing prerequisite. The red-team
finding is a SCOPE correction (what the PASS establishes), not evidence of a missing dependency in
the mechanism this run actually tests.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | Driver correctly scopes itself as diagnostic substrate-readiness, not new MECH-423 super-additivity evidence; claim tag is for traceability only. |
| Biological reference | clear | Local, module-scoped consolidation optimizer during sleep -- direct mechanistic analogue, not a formal import. |
| Developmental / dependency prerequisites | present | Real waking rollout (180 transitions, >10x floor); consolidator built per-arm; readiness preconditions all met and non-degenerate. |
| Implementation completeness | complete for the self-forward/predict_next_self question this driver tests; **partial** for a "world-model update" claim -- E2.world_forward has no trainer anywhere in `ree_core` (Step 7c F1; new buildable gap identified, Section 6b). |
| Environment adequacy | adequate | 5x5 grid, 1 hazard, 1 resource is sufficient for a binary mechanism-firing question; not a competence/scale claim. |
| Measurement adequacy | adequate | Direct parameter-level `max|delta|`, not a proxy; recording-standard always-core fully present (0 gaps, independently re-verified). |
| Integration adequacy | coupled | Exercised via the actual production call path, specifically `SleepLoopManager.force_cycle` -- NOT reachable via a bare `agent.run_sleep_cycle()` (Step 7c F3; the manifest's own `sleep_driver_pattern` field mislabels this). |
| Scale / capacity | n/a | Binary firing test, not a capacity claim. |

**Failure-location (GOV-FAILLOC-1), recorded for completeness though no "REE failed" read is being
made:** Implementation `established`, Measurement `established`, Environment `established` for the
narrow question this driver poses. The red-team finding narrows the SCOPE of what the PASS
establishes; it does not turn the result into a failure.

## 5. Learning extracted

1. The sleep-INTEGRATED call site now has landed-manifest coverage for the first time; prior
   coverage of R3 was direct-call only (the 680/680a-e family).
2. Attribution of the C3 delta to this hook alone is confirmed by direct measurement (C4: exact-zero
   OFF-arm delta over ALL E2 parameters). The driver docstring's supporting analysis of "the other
   two offline writer sites" is itself wrong (`agent.offline_integration()` has zero callers in
   `ree_core`; the true OFF-arm E1 writer is a ContextMemory memory-slot update during SWS/REM
   replay) -- this does not weaken the E2 conclusion, but the docstring should be corrected.
3. **CORRECTED (Step 7c red-team F1):** E2's `predict_next_self` (self-forward) and `world_forward`
   heads are disjoint parameter sets; `compute_e2_loss` trains only the former. This run's C3 delta
   is confined to the self-forward head; `world_forward` moved by exactly 0. `INV-063` leg B reads
   `world_forward` specifically, so this run does NOT unblock it. A genuine, named, buildable gap
   remains: no waking- or sleep-time pathway anywhere in `ree_core` trains `world_forward` at all.
4. Recording-standard always-core compliance was full (0 gaps, independently re-verified).
5. The manifest's `sleep_driver_pattern` field mislabels the actual call path (says
   "manual-cycle-loop / `run_sleep_cycle()`"; the driver actually calls
   `agent.sleep_loop.force_cycle(agent)`, reachable only via `SleepLoopManager`).

## 6. Routing

**Two distinct routing actions**, per the red-team correction:

**(a) `governance-apply`** -- amend the EXISTING `substrate_queue.json` entry
`mech423-sleep-integrated-e2-consolidation-hook`: the entry's own literal `current_blocker`
condition (C1-C4 as stated) is satisfied verbatim by this run's data, so `ready: true` and
`implementation_status: "implemented"` are warranted. **WITH the F1 wording correction**: the
entry's title/status_note/`unblocks_note` currently describe the validated update as a
"sleep-integrated world-model update" and claim this run unblocks INV-063 -- both inaccurate.
Governance should correct the wording to "self-forward (`predict_next_self`) update" and drop (or
annotate) `INV-063` in `unblocks_claims`. Full amend note in the JSON artifact.

**(b) `implement-substrate`** -- a genuinely new, named, `complicated (buildable)` gap surfaced by
this autopsy's own red-team analysis (not anticipated before the run): `E2.world_forward` has no
trainer anywhere in `ree_core`. See `secondary_substrate_queue_entries[0]` in the JSON artifact
(`sd_id_suggested: mech423-e2-world-forward-sleep-training-gap`) for the full build recommendation
-- a world_forward loss closure over the already-populated `_world_experience_buffer` +
`_action_experience_buffer`, wired into `CrossModuleConsolidator` or a parallel local-optimizer
pass. This is what INV-063 leg B is actually waiting on.

- `per_claim_recommendation.MECH-423`: no evidence_direction/epistemic_category/status change;
  set `recommended_diagnostic_evidence_adjudicated: true` per the skill's SD-099/MECH-489 fix shape.
- Re-derive brake: not applicable (`fired: false`) -- not a `substrate_ceiling` reading.
- No `/lit-pull`, `/queue-experiment`, or `/diagnose-errors` follow-on is owed.

**Step 7b mechanical pre-routing checks:** 0 fires, 0 inapplicable (`autopsy_pre_routing_checks.py`,
re-run against the corrected artifact).

## 6b. Step 7c adversarial red-team -- full verdict

**Run on `fable`** (this drafting session is on Sonnet 5, per the skill's model-diversity rule).
The agent was given the raw manifest, driver, substrate_queue.json entry, and claims.yaml entry,
withheld this session's reasoning, and was required to recompute at least one load-bearing number
independently from the manifest's own cells before reading this prose.

**Verdict: CONTESTED.**

**Independent recomputation** (all matched the artifact's claims): min ON-arm `e2_max_abs_delta`
(0.007690362632274628, seed 42), max OFF-arm `e2_max_abs_delta` (0.0 exactly, all 3 seeds), min
`updates_e2` (8.0), `cmc_metrics_merged` true on all ON cells / false+empty on all OFF cells,
config confirming a full run (not dry-run: `waking_episodes=3, steps_per_episode=60`,
3 seeds x 2 arms), `validate_recording.py --strict` re-run independently (0 gaps).

**F1 (verdict-moving, independently CONFIRMED by this drafting session -- see Section 1/2 above for
the source citations and the artifact-level correction already applied):** the C3 delta is in E2's
self-forward head only; `world_forward` -- the parameter set INV-063 leg B's frozen-probe DV
actually reads -- moved by exactly 0 (confirmed via a per-named-parameter probe re-run
independently: `sed -n '179,222p' ree_core/predictors/e2_fast.py` shows `predict_next_self` uses
`self_action_encoder`/`self_transition` while `world_forward` uses disjoint
`world_action_encoder`/`world_transition`, docstring: "NOT trained as E2's primary objective";
`sed -n '12230,12247p' ree_core/agent.py` shows `compute_e2_loss` calls only
`self.e2.predict_next_self`). **Cheap confirmer:** `sed -n 179,222p
ree_core/predictors/e2_fast.py` + `sed -n 12230,12247p ree_core/agent.py`.

**F2 (moderate, independently CONFIRMED):** the driver docstring's claim that
`agent.offline_integration()`'s `e1.integrate_experience` call explains the OFF-arm E1 delta is
wrong -- `grep -rn "offline_integration()" ree_core/` has zero callers besides the `def` itself.
Does not affect the E2 attribution (which rests on the direct C4 measurement, not on this
docstring analysis). **Cheap confirmer:** `grep -rn "offline_integration()" ree-v3/ree_core/`.

**F3 (moderate, confirmed):** the hook is reachable only via `SleepLoopManager` (`force_cycle` /
`notify_episode_end` / `notify_waking_step`); a bare `agent.run_sleep_cycle()` driver never reaches
it (`ree_core/agent.py`'s `run_sleep_cycle` contains no reference to `sleep_loop` or the
consolidator). The manifest's `sleep_driver_pattern` field says "manual-cycle-loop
(`run_sleep_cycle()` called once per cycle...)" but the driver actually calls
`agent.sleep_loop.force_cycle(agent)`. **Cheap confirmer:** `grep -n "sleep_loop\|consolidat"
ree_core/agent.py | awk -F: '$1>=12722 && $1<=12760'` (expect nothing).

**Things the red-team tried to break and could not:** dry-run masquerading as a full run (no);
"0 always-core gaps" (re-confirmed); "exactly bit-identical" OFF-arm (re-confirmed, all 18 named E2
parameters at 0); the C4 negative control being pinned-by-construction rather than a genuine
measurement (rejected -- corroborated by non-zero OFF-arm E1 deltas and the unconditional
sleep-cycle-fired key); substrate drift between run and audit (none, `git diff` empty on all
relevant files at the run's `substrate_commit`); the substrate_queue entry's LITERAL unblock
condition (satisfied verbatim -- the ready-flip for the hook-fires question is warranted); MECH-423
handling (no contradiction found).

**Minor hygiene (do not move the verdict):** `criteria_non_degenerate["C4_..."]` is hard-coded
`True` in the driver rather than computed (supported by measurement, but worth noting);
`interpretation.preconditions` flattens 18 entries with no arm/seed key (reconstructable from
`arm_results[]`, not a recording gap); `substrate_queue.json`'s `design_doc` pointer
(`docs/substrate/MECH-423-readiness-substrate-r2-iterative.md`) does not exist in `REE_assembly`
(fold into the amend, Section 6a).

## 7. Granularity-debt recurrence check (MECH-423)

Not run via the `granularity_debt_cluster.py` reader in this staging pass because this target's
diagnosis carries no `weakened` claim_alignment read (Section 4: `intact`) -- the trigger's own
precondition ("at least one target reads `weakened`") is not met. `claims.yaml`'s own
`granularity_debt_disposition: coherent_campaign` (set 2026-07-16, GOV-GRAN-1 P1) already covers
the 680-family recurrence and explicitly contraindicates `/claim-synthesis` for MECH-423. This run
does not disturb that disposition.

## 8. Re-derive brake (MECH-423)

Not fired. This target's `recommended_epistemic_category` is `standard`, not `substrate_ceiling`,
and its `recommended_evidence_direction` is `supports`, not `non_contributory`.

## 9. Hypothesis-space ledger (Step 9b)

No `fanout_recommendation` emitted (this target does not discriminate among live rival hypotheses
-- it is a confirming substrate-wiring validation, with a scope correction from the red-team, not a
discrimination among named alternatives). Staging-mode: Step 9b is drafted-only and nothing is
written to the live registry. No ledger action is deferred -- there is nothing to pre-register or
resolve for this target.
