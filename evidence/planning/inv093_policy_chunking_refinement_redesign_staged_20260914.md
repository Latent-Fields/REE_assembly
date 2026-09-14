**Status: AWAITING USER / FUTURE-SESSION REVIEW. This is a staged experimental DESIGN, not a queued experiment. Nothing here has been written to `ree-v3/experiment_queue.json` or `claims.yaml`, and no run has been executed.**

# INV-093 / EXP-0717 redesign: policy_chunking formation-eagerness as the refinement-strength IV

Generated: 2026-09-14T15:49:21Z
Chip: `chip-20260910-gflag0237-policy-chunking-refinement-redesign` (headless metaworker dispatch, cycle 859, ree-cloud-4)
Provenance: the owed residual of GFLAG-0237 (`REE_assembly/evidence/planning/governance_flag_adjudication_20260909.md` section "GFLAG-0237 [contested_disposition] -- INV-093"; registry disposition applied 2026-09-10). The governance ruling's own text names exactly this gap: *"OWED and not done here: redesigning the experiment around policy_chunking as the IV once (b) clears -- V3-EXQ-871a already runs it ON with three of the four panel axes instrumented"* (`experiment_proposals.v1.json`, EXP-0717 `blocked_note`).

## 1. Why this is a design doc, not a queue entry

**EXP-0717 (backlog EVB-1366, claim INV-093) is still `status: blocked_substrate` in `REE_assembly/evidence/planning/experiment_proposals.v1.json`, and this document does not change that.** Its `release_condition` requires BOTH:

- **(a)** a graded strength knob over a planned-to-habitual transition mechanism, reachable and sweepable at runtime -- **SATISFIED 2026-09-10 by GFLAG-0237** (`use_policy_chunking`'s formation-eagerness family; see section 2).
- **(b)** competence acquisition reliable enough to carry a gain axis (a majority of seeds must move on the targeted update, not 5 of 16 -- `V3-EXQ-890`, autopsy `failure_autopsy_V3-EXQ-890_2026-08-07`). **STILL UNMET.** Practically: `MECH-457`'s `mech457_competence_bootstrap_explorer` remains `blocked_pending_discrimination`, and `MECH-471`'s own local-update-interference falsifier has not reached a real verdict (both of its full-budget attempts, V3-EXQ-875/875a, died on this same precondition rather than on the phenomenon).

The 2026-09-10 ruling is explicit that the fix for (b) is **`/implement-substrate` + `/claim-synthesis`, "NOT via another experiment on this proposal."** So this chip's job is the redesign itself -- ready to become a real `/queue-experiment` pass the moment (b) clears -- not a live run today. **Do not add this to `ree-v3/experiment_queue.json` until condition (b) is independently confirmed cleared** (check `claims.yaml` MECH-457/MECH-471 status and `experiment_proposals.v1.json` EXP-0717's own `status` field first -- a future governance pass will flip these when the precondition is met).

## 2. The mechanism (confirms release_condition (a))

`ree-v3/ree_core/policy/policy_chunking.py` (2115 lines) is ARC-071 "policy_composition_via_repeated_grounding" -- the striatal-style planned->habitual TRANSITION mechanism MECH-163 presupposes (MECH-323 formation / MECH-324 lifecycle). Wired at `ree_core/agent.py:1537-1606` behind the master switch `use_policy_chunking` (default `False`, bit-identical when off).

**The "formation-eagerness family" is four independent, jointly-AND-gated config knobs** (`REEConfig`, `ree_core/utils/config.py:5254-5259`; internally `PolicyChunkingConfig`, `policy_chunking.py:720-725`):

| Field | Default | Role |
|---|---|---|
| `chunk_min_repetitions` | 20 | R_min: repetitions of a sub-sequence within the sliding window required before formation is even considered |
| `chunk_variance_low` | 0.15 | F_low: outcome variance must be below this to **form** |
| `chunk_variance_high` | 0.45 | F_high: variance above this starts **dissolution** of an already-crystallised chunk (hysteresis gap; must be `> chunk_variance_low`, enforced by `PolicyChunkingConfig.validate()`) |
| `chunk_evaluative_margin` | 0.05 | accumulated outcome mean must exceed running baseline + this margin to form (Graybiel 2008 evaluative gate) |

There is **no single derived "eagerness" scalar anywhere in the code** -- confirmed by grep across `policy_chunking.py`, `config.py`, `agent.py` (zero hits for "eagerness"). `ChunkAccumulator.formation_candidates()` (`policy_chunking.py:1139-1161`) ANDs three independent conditions (repetitions, variance-low, evaluative-margin); `chunk_variance_high` gates only maintenance/dissolution (`ChunkLibrary.note_real_execution`, lines 1542-1548), not formation. "Formation eagerness" is governance/dispatch-brief shorthand for this four-field family, not a codebase term -- the redesign below treats the four fields as what they are: independent levers, not one dial.

**Behavioral payoff of formation** (`ree_core/hippocampal/module.py`, `set_chunk_source`/`_build_chunk_candidates`, lines 866-1254): a CRYSTALLISED chunk is spliced into the proposal pool as one atomic multi-step `Trajectory`; the MECH-090 commit latch then executes the whole sequence without re-deliberating each step -- this is literally the planned->habitual transition the invariant is about.

**Rollback / un-chunking**: dissolution (`CRYSTALLISED -> DISSOLVING -> DISSOLVED`, `policy_chunking.py:1542-1678`) is forward-only lifecycle, not an undo. Under `use_chunk_dissolution_retention=True` (default off) a dissolved chunk survives as DORMANT and can be revived via `ChunkLibrary.revive()` at a reduced bar. There is a separate pre-commitment un-chunk mechanism, ARC-070 `policy_decomposition` (`hippocampal/module.py::_apply_policy_decomposition`), but it decomposes a *candidate* before commit, not an executed one.

**Prior art on the sweep surface -- confirmed empirically, not assumed.** Grepped every script under `ree-v3/experiments/*.py` and `_lib/**/*.py`: `chunk_variance_low`, `chunk_variance_high`, and `chunk_evaluative_margin` appear in **zero** experiment scripts anywhere in the corpus. Only `chunk_min_repetitions` has ever been touched, and only via one shared constant: `experiments/_lib/baselines/arc071_chunking.py`'s `CHUNK_MIN_REPETITIONS = 5` (probe-scaled down from the registered default 20; module comment, lines 96-99: *"Do NOT lower CHUNK_MIN_REPETITIONS further. V3-EXQ-810's autopsy measured repetition reaching 37 against a bar of 5, with the variance gate passing too: repetition was never the binding constraint."* This is a load-bearing design fact for section 4.

## 3. Prior instrumentation precedent (co-instrumentation already demonstrated)

`ree-v3/experiments/v3_exq_871a_mech090_commit_latch_persistence_diagnostic.py` is a MECH-090 diagnostic (not an INV-093 run), but it already runs `use_policy_chunking=True` (line 414) plus `use_chunk_maintenance/proposal_injection/all_position_credit=True` while co-instrumenting three of INV-093's four panel axes on the SAME execution trace, at the SAME `chunk_min_repetitions=5` baseline (it never touches variance/margin, riding `arc071_chunking.py` defaults):

- **Harm sensitivity**: `ep_reward = sum(r.harm_signal for r in results)` per episode (`v3_exq_871a...py:474`), against `experiments/_harness.StepHarness` results.
- **Residue accumulation**: `agent.py:8701` calls `e3.post_action_update` unconditionally inside `update_residue()` every env step (`ree_core/residue/field.py` live since V3-EXQ-603k/603n).
- **Commitment integrity**: MECH-090 commit-latch readouts -- `agent.get_chunking_state()` (facade, `policy_chunking.py:2097-2114`, merging `ChunkAccumulator`/`ChunkLibrary` state) and the identity-based genuine-commit counter pattern (`_committed_chunk_state()`, `v3_exq_871a...py`).
- **Not instrumented (the 4th axis, competence gain)**: this is exactly the axis release_condition (b) blocks. V3-EXQ-890 / MECH-471's own script (`experiments/v3_exq_890_mech471_acquisition_reliability_probe.py`) is the template for it, once unblocked -- reuse its targeted-update + bimodal-split-discrimination readout rather than re-deriving one.

**Known open confound to account for, not ignore**: V3-EXQ-871a's own confirmed autopsy found E3 still unconditionally recreates a fresh committed-trajectory object at the AT-tick selection site regardless of an existing unexpired commitment (`n_genuine_commits_identity_based == n_e3_ticks + n_episodes_probe` exactly, both tested seeds) -- routed to `/implement-substrate` (`mech090-arc071-attick-persistent-handle-fix`), `pending_retest_after_substrate=true`. If the redesigned experiment leans on the commit-latch genuine-commit-count readout for "commitment integrity," it should either (i) check whether that substrate fix has landed first, or (ii) use a readout that does not depend on cross-tick persistence (e.g. `chunk_lib_n_crystallised`, `chunk_lib_n_dissolved`, `chunk_acc_n_formed` from `get_chunking_state()`, which are unaffected by the AT-tick persistence gap) rather than the identity-based genuine-commit count 871a used for its own (different) diagnostic purpose.

## 4. The redesigned experiment

**Working ID**: `V3-EXQ-1031` (anticipated, NOT formally reserved by this document -- see section 6 on the stale claim). **Working name**: `v3_exq_1031_inv093_policy_chunking_refinement_eagerness_panel.py`.

**IV: sweep the formation-eagerness family, NOT as one scalar but as named eagerness LEVELS that co-vary the three fields the joint-AND gate actually reads for formation, holding `chunk_min_repetitions` fixed at the lineage baseline.**

Design rationale for what to fix vs. sweep:
- **Fix `chunk_min_repetitions = 5`** (the `arc071_chunking.py` lineage baseline) across every ON arm. Two independent reasons converge: (i) V3-EXQ-810's autopsy already found repetition is not the binding constraint at this value (measured reaching 37 against a bar of 5), so sweeping it is unlikely to be informative on its own; (ii) fixing it at the established baseline keeps this experiment's OFF arm and harness construction reusable from `experiments/_lib/baselines/arc071_chunking.py` (`off_arm_flags()`, `shared_config_kwargs()`, `StepHarness` loop) rather than hand-rolling a new loop -- the module's own docstring is explicit that hand-rolling the loop is how V3-EXQ-810 originally under-measured this mechanism (never called `update_residue`, so `MECH-091`'s salient-event `clock.phase_reset()` never fired and the E3 tick was perfectly periodic).
- **Sweep `chunk_variance_low`, `chunk_variance_high`, `chunk_evaluative_margin` jointly, as three named eagerness levels**, since this is the entirely-unswept part of the family and is where a genuine formation-eagerness gradient lives (variance_low/margin gate formation; variance_high gates retention):

| Arm | `chunk_variance_low` | `chunk_variance_high` | `chunk_evaluative_margin` | Reading |
|---|---|---|---|---|
| OFF (baseline) | -- | -- | -- | `use_policy_chunking=False`; calibrates the harm/residue/commitment readouts against no-chunking behavior |
| TIGHT (conservative) | 0.08 | 0.30 | 0.10 | forms only on very stable, clearly-good sequences; dissolves early on variance; the "cautious" end of the family |
| DEFAULT (registered) | 0.15 | 0.45 | 0.05 | the REEConfig registered default, unswept in the corpus to date |
| LOOSE (eager) | 0.25 | 0.60 | 0.02 | forms readily, tolerates more outcome noise, retains longer before dissolving; the "eager" end |

(Hysteresis constraint `variance_low < variance_high` holds for all three ON arms, per `PolicyChunkingConfig.validate()`.) This is a **3-level ordinal sweep with an OFF calibration arm**, not a full factorial across the three fields independently -- a full factorial would multiply arm count for a joint effect the mechanism doesn't obviously decompose into independent contributions (variance_low/margin both gate formation jointly; treating them as one "how eager to form" axis and variance_high as a correlated "how eager to retain" axis, co-varied together, is the more scientifically motivated design than 3^3=27 independent cells). A future session with more compute budget could refine this to a fuller factorial once the ordinal sweep establishes whether there is a monotonic or threshold effect (Pan et al. 2022, cited in INV-093's `what_would_answer`, motivates checking for a threshold/phase transition rather than assuming monotonicity).

**Harness**: reuse `experiments/_lib/baselines/arc071_chunking.py` construction (`ENV_KWARGS` -- 8x8 grid, `num_hazards=2`, load-bearing per that module's own docstring for triggering `MECH-091` phase-resets; `N_EPISODES=120`, `STEPS_PER_EPISODE=72`) and `experiments/_harness.StepHarness` for the step loop, exactly as V3-EXQ-871a and the 810-series do -- do not hand-roll a reduced loop (see section 3's confound discussion for why that specific mistake matters here).

**DV panel -- four axes, NEVER collapsed to one score, per GFLAG-0236's Pareto/joint-bound acceptance shape**:

1. **Harm sensitivity**: mean `harm_signal` per episode (`sum(r.harm_signal for r in results)` pattern from V3-EXQ-871a) across the probe window, per arm. Consider also an off-distribution harm probe per INV-093's `what_would_answer` correction #2 (out-of-loop harm scoring) if budget allows -- flagged as an enhancement, not a requirement for the first pass.
2. **Residue accumulation**: residue field state (`ree_core/residue/field.py`) sampled at the same cadence, per arm.
3. **Commitment integrity**: `agent.get_chunking_state()` readouts -- `chunk_lib_n_crystallised`, `chunk_lib_n_dissolved`, `chunk_lib_by_state`, `chunk_acc_n_formed` -- NOT the identity-based genuine-commit count (see section 3's open-confound note) unless the AT-tick persistence fix has landed by the time this is built.
4. **Competence gain** (STILL GATED by release_condition (b) -- NOT measured in this design as written; slot reserved). When (b) clears, wire this axis using `experiments/v3_exq_890_mech471_acquisition_reliability_probe.py`'s targeted-update + bimodal-split discrimination as the template, and re-check whether its 16-seed protocol needs to be widened now that a majority (not 5/16) must clear for the gain axis to be admissible per the release condition's own text.

**Declared nulls** (GOV-FANOUT-1 discipline, applied even though this is not a braked lineage): a `non_contributory` reading on any one axis should state explicitly what it does and does not mean --
- Flat harm/residue/commitment-integrity readouts across TIGHT/DEFAULT/LOOSE would mean the formation-eagerness family does **not** modulate the three protected axes in this env/budget regime -- informative for INV-093 (a mechanism that cannot even move the protected axes cannot be shown to trade them away, which is itself evidence toward, not against, the "no forced trade" invariant, though it would not positively confirm the invariant either without the 4th axis moving).
- A monotonic or threshold shift in harm/residue/commitment across the three levels, absent the competence axis, would be a real finding about the *cost side* of the trade but cannot resolve INV-093 alone (the invariant is about competence gain traded against the other three -- no gain axis, no trade to evaluate). Record it as a `reanalysis`-eligible partial result, not a claim-resolving PASS/FAIL, once (b) clears and the full panel runs.

**`claim_ids` / `evidence_direction_per_claim`**: `["INV-093"]` primarily; consider co-tagging `ARC-071`/`MECH-323`/`MECH-324` (the mechanism itself) as the panel also exercises their formation/lifecycle machinery, following the `bears_on`-style non-scoring disposition pattern (GFLAG-0247 registry-half convention) rather than scoring credit onto claims the run does not adjudicate. Per the skill's `claim_ids` accuracy rule, this needs re-evaluating against whatever the script actually measures at write time, not inherited verbatim from this doc.

## 5. What a future `/queue-experiment` session still needs to do

This document is the design, not the finished, reviewed, smoke-tested artifact. Before queuing for real:

1. **Re-check release_condition (b)** against live `claims.yaml` (MECH-457, MECH-471 status) and `experiment_proposals.v1.json` (EXP-0717's own `status` field) -- do not trust this document's staleness date.
2. Run `/queue-experiment` Steps 2 (ID reservation -- see section 6 below on the existing stale claim), 2.5a (empirical runtime confirmation that the four config fields are still wired exactly as described here -- `reference-reeconfig-from-dims-silent-kwargs` warns a doc-level "implemented" can still be unreachable at some call sites), 2.5c (substrate-path overlap gate -- check `substrate_queue.json` for any open `corrupting` entry touching `ree_core/policy/policy_chunking.py` or `ree_core/hippocampal/module.py` that didn't exist at this writing).
3. Write the actual script (this document is prose design, not code), run it through code review (Step 3.5), smoke test, and the adversarial red-team design review (Step 4.5) per the skill's mandatory path -- none of that has happened here.
4. Decide the arm count / seed count against actual compute budget available at that time; V3-EXQ-890's 16-seed, ~10.3h precedent is the closest cost comparable for a similar-scale probe.

## 6. Note on a stale-looking claim (flagged, not acted on)

`TASK_CLAIMS.json` carries an `active` claim, `session_id: "metaworker-chip-20260910-gflag0237-exq-1031"`, `claimed_at: 2026-09-14T12:15:04Z`, `task: "Reserve + queue V3-EXQ-1031 (INV-093 policy_chunking eagerness panel)"`, naming resources `ree-v3/experiment_queue.json/V3-EXQ-1031` and `ree-v3/experiments/v3_exq_1031_inv093_policy_chunking_refinement_eagerness_panel.py` -- the exact same working ID/filename independently arrived at in section 4 above. As of this writing (2026-09-14T15:49Z, ~3.6h after that claim was opened) there is no script at that path, no `V3-EXQ-1031` entry in `experiment_queue.json`, and no worktree anywhere on this machine other than the one this chip is running in, which carries no commits from that session. It is very likely an earlier, incomplete attempt at this same chip that never wrote or committed anything before its process ended. It is **not yet stale by the 6-hour `audit_stale_claims.py` threshold** (would cross at ~2026-09-14T18:15Z), and per CLAUDE.md ("every OTHER session claim is still never auto-closed"), this session has deliberately **not** touched or closed it. **This document does not queue `V3-EXQ-1031` live, so it does not collide with that claim's named resources.** A future session that DOES reach Step 2 of `/queue-experiment` for this redesign should check that claim's live status first (past 18:15Z UTC 2026-09-14, `audit_stale_claims.py` should classify and report it) before assuming the ID is free.
