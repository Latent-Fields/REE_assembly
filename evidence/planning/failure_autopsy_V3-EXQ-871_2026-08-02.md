# Failure Autopsy: V3-EXQ-871 (MECH-090 / ARC-071 commit-latch post-fix validation)

Generated: `2026-08-02T11:33:36Z`
Status: confirmed (user-confirmed routing 2026-08-02)
Scope: single

**Addendum 2026-08-02T11:45Z (user-requested follow-on check, CLOSED -- no defect found):** Section 5's "Learning extracted" flagged `experiments/_lib/baselines/sd084_midexec_reachability.py:271` (the precedent this run's script cited for a script-local flag override) as worth checking for the same whole-cell-vs-probe-only scoping issue. Checked directly, including the full driving loop in its consumer `experiments/v3_exq_839_sd084_midexec_reachability.py` (`_build`, `_register_chunk`, `_run_cell`). **It does not have the defect**, for three structural reasons that all trace back to how the two modules differ:

1. **No organic-formation dependency for the flag to perturb.** The 871 defect required a multi-episode *organic accumulation* phase whose dynamics needed to replicate a *different, differently-flagged* prior run (V3-EXQ-841). `sd084_midexec_reachability.py`'s consumer instead **directly injects** a pre-built, already-`CRYSTALLISED` chunk (`_register_chunk`, `SEEDED_CHUNK_SEQUENCE`) at the start of the run and re-injects it whenever the library empties -- there is no accumulator dynamics for the flag to perturb, by design (module docstring: "WHY A CRYSTALLISED CHUNK MUST BE REGISTERED... is a PRECONDITION of the measurement rather than the manipulation").
2. **No cross-run inheritance claim.** 871's `ANCHOR_REACHABILITY_EXEMPT` explicitly claimed readiness was inherited by construction from a *different* run that used a *different* flag value. Neither `sd084_midexec_reachability.py` nor its consumer makes an analogous claim -- `_arm_flags(arm_id)` applies one flag value uniformly across the WHOLE cell for that arm (`_build` -> `_run_cell`, one continuous loop over all `episodes`, no formation/probe split), and each arm is evaluated entirely on its own terms.
3. **The OFF-vs-ON divergence is the intended measurement, independently verified against exactly this failure mode.** The module docstring states the two arms "take different action sequences by design" once a multi-action commit fires (that IS mid-execution reachability), and separately reports the negative-control check: on seeds where no multi-action chunk ever commits, OFF and ON are measured **bit-identical in every recorded field** (module docstring "THREE THINGS THIS TABLE ESTABLISHES", point 3). That is precisely the check that would have caught 871's bug -- confirmed already done and passing here, prior to this addendum.

No code change made; no follow-on queued. This closes the open item from Section 5 and the `learning_extracted` field in the companion JSON.

## 1. Facts

**Run:** `v3_exq_855_mech090_commit_latch_persistence_diagnostic_20260802T104333Z_v3`
**Queue ID:** `V3-EXQ-871` (queued as the real placeholder for a never-committed draft `V3-EXQ-855` -- see `TASK_CLAIMS.json` closed entry `session_label: "queue-experiment: V3-EXQ-855 MECH-090 commit-latch"`, `completion_note` starting "ree-v3 fd7d7edfaf on origin/main: V3-EXQ-871 queued...". The experiment_type / script filename still reads `v3_exq_855_...` -- this is the same convention already used for e.g. `v3_exq_857a` where the queue_id and the experiment_type diverge.)
**Claims:** MECH-090, ARC-071
**Outcome:** FAIL. Self-route label: `substrate_not_ready_requeue`. Adjudication flag: `precondition_unmet`.
**Dry-run gate (Step 2a):** clean -- `scripts/check_dry_run_citations.py` reports 1 clean, 0 dry, 0 ambiguous. `dry_run: false` confirmed on the manifest.
**Recording standard (Step 2 provenance check):** `ree-v3/validate_recording.py` reports OK -- `substrate_hash`, `config`, `seeds`, `machine`/`machine_class`, `elapsed_seconds` all present. No recording gap.
**Re-derive brake:** MECH-090 has 7 prior confirmed `substrate_ceiling` hits (R1-R3 convention), all from a *different* sub-mechanism (delayed-reward persistence / commitment-vs-contradiction / control-plane-ramp / readiness-conjunction -- SD-033a/SD-034/MECH-268/MECH-342/MECH-445/MECH-446/ARC-108 clusters), none touching commit-latch cross-tick persistence. Matches the queuing session's own prior check ("raw count 9, all a different sub-mechanism ... exempt"). ARC-071 has 0 ceiling hits. **Brake does not fire** -- and would not route here anyway, since the finding below is not a ceiling reading.
**Granularity-debt trigger:** ran `scripts/granularity_debt_cluster.py` for both claims. MECH-090: 11 targets, alignment distribution intact=6/other=3/strengthened=1/unclear=1/unstamped=1, **no target reads `weakened`** -- does not fire. ARC-071: 4 targets, strengthened=2/unclear=2, **no target reads `weakened`** -- does not fire, and the reader explicitly flags "measurement or implementation debt, NOT granularity debt." ARC-071's own most recent prior autopsy (V3-EXQ-834) landed on the *same* `measurement_test_design_defect` category this autopsy lands on -- a second instance of the same category, not a new pattern needing `/claim-synthesis`.

### Script and design intent

The driver (`experiments/v3_exq_855_mech090_commit_latch_persistence_diagnostic.py`) is a GOV-FANOUT-1 discrimination probe descending from `failure_autopsy_V3-EXQ-841_2026-07-31.json targets[0].fanout_recommendation`. Its own docstring records that H1 (real wiring defect) vs H2 (readout artifact) was **already resolved** by an ad hoc probe on 2026-07-31 (H1 confirmed, H2 refuted -- see the `arc071-commit-latch-persistence` hypothesis-space question, both hypotheses closed). One of the two wiring gaps that diagnosis found was fixed on ree-v3 main the same day as drafting (`278599a`, gated behind new flag `use_persistent_committed_program_handle`, default False). The script's own "STATUS UPDATE (2026-08-02)" section states this run is **not** a live H1/H2 discrimination -- it validates whether the landed fix restores meaningful multi-step persistence under REAL organically-formed chunks (as opposed to the ad hoc probe's forced/monkeypatched setup), by setting `use_persistent_committed_program_handle=True` as a script-local override.

### What happened

The precondition `arc071_chunk_commitments_observed_supra_floor` (>=10 probe ticks with a genuine ARC-071 chunk-sourced persistent commitment, worst seed) measured **0.0** on both seeds (101 and 505). `overall_pass=False`, `evidence_direction=non_contributory`, `evidence_direction_per_claim={"MECH-090":"unknown","ARC-071":"unknown"}` (the script only assigns a definitive direction when C2 discrimination is actually reached).

Per-seed breakdown (from `arm_results`):

| Seed | chunks_formed | chunks_crystallised | n_probe_ticks | n_persistent_present_ticks | cell_verdict |
|---|---|---|---|---|---|
| 101 | 1.0 | 1.0 | 702 | 0 | insufficient_commitments |
| 505 | 0.0 | 0.0 | 640 | 0 | insufficient_commitments |

This is a **formation-phase** failure, not a probe-phase one -- the probe couldn't observe a chunk-sourced commitment because too few chunks (1 and 0) formed during the 120-episode formation phase to begin with.

### The load-bearing finding: the readiness gate failed because of the probe's own construction, not the substrate

The script's `ANCHOR_REACHABILITY_EXEMPT` note claims readiness is "established by construction" because the formation phase is "IDENTICAL" to `arc071_chunking`'s proven schedule, citing V3-EXQ-810a (8/8 seeds form chunks) and V3-EXQ-841 (32/32 chunking cells committed >=1 chunk) on "the IDENTICAL inherited formation schedule/config."

Direct comparison against V3-EXQ-841's own manifest (`v3_exq_841_mech163_q085_grain_dose_response_20260731T080537Z_v3.json`), same arm (A_HIER_S2), same two seeds (101, 505), same `chunk_max_size=2`, same `N_EPISODES_TRAIN=120` / `STEPS_PER_EPISODE=72`:

| Seed | chunks_formed, V3-EXQ-841 (flag OFF, lineage default) | chunks_formed, V3-EXQ-871 (flag ON for the whole cell) |
|---|---|---|
| 101 | 2.0 | 1.0 |
| 505 | 2.0 | 0.0 |

Same seeds, same nominal schedule -- a direct same-seed comparison, not a statistical inference across different runs.

**Mechanism, read directly against ree-v3 HEAD (`agent.py:5985-6023`):** `_arm_flags()` in this script sets `use_persistent_committed_program_handle: True` for the whole cell -- it is included in the single `flags` dict passed to `base.build_agent(env, flags)` at the top of `_run_cell`, used identically through both `_run_formation` and `_run_instrumented_probe` on the same agent. That flag changes the between-E3-tick fast path:

```python
_step_traj = (
    self.e3._committed_trajectory
    or self.e3._closure_committed_trajectory
)
if _step_traj is None and getattr(
    self.config, "use_persistent_committed_program_handle", False
):
    _step_traj = self.e3._persistent_committed_trajectory
if self.beta_gate.is_elevated and _step_traj is not None:
    traj = _step_traj
    horizon = traj.actions.shape[1]
    step_idx = min(self._committed_step_idx, horizon - 1)
    action = traj.actions[:, step_idx, :]
    self._committed_step_idx += 1
else:
    action = self._last_action
```

With the flag OFF (841's construction), `_committed_trajectory`/`_closure_committed_trajectory` are torn down every tick (`e3_selector.py:3910`), so `_step_traj` is `None` on essentially every between-tick step and the agent falls through to `action = self._last_action` (hold). With the flag ON (871's construction), `_persistent_committed_trajectory` is the SD-084 handle that is **not** torn down every tick and is set on **any** committed selection regardless of candidate provenance (per the script's own `_analyze_cell` docstring) -- so as soon as the *first* commitment of any kind happens during formation, every subsequent between-tick step where beta is elevated now steps a planned macro-action from that trajectory instead of holding.

`experiments/_lib/arm_fingerprint.py:457-480` confirms RNG (`random`, `numpy`, `torch`) is deterministically reset from the seed at the top of `arm_cell`, identically in both scripts. So the two runs start from bit-identical RNG state for a given seed; the divergence in `chunks_formed` can only come from the agent taking a **different sequence of actions** once the flag-driven fast-path change first fires, which changes the environment trajectory, which changes what gets experienced (and hence what gets proposed/crystallised as a chunk) for the rest of formation.

This is fully sufficient to explain the collapse from 2/2 to 1/0 chunks. It is a genuine, mechanistically-traceable consequence of applying the flag to the **entire** cell rather than scoping it to the probe phase -- the ANCHOR_REACHABILITY_EXEMPT's "inherited by construction" claim only holds when the flag stays at its lineage default (False) during formation, which this run's own construction violates.

## 2. Claim-layer mapping

**MECH-090** (`BG-level beta oscillations gate E3-to-action-selection propagation, not E3 internal updating`, status active, `implementation_phase: v3`). Prior `live_status.evidence` already cites `failure_autopsy_V3-EXQ-732_2026-07-10` as `non_contributory/precondition_unmet` -- this run adds a second `non_contributory/precondition_unmet` instance, for an unrelated reason (a probe-construction confound, not the 732 finding's cause). Not falsified; not fairly tested.

**ARC-071** (`policy_composition_via_repeated_grounding`, status candidate, `v3_pending: true`). Prior `live_status.evidence` cites `failure_autopsy_V3-EXQ-810a_2026-07-30` as `supports/standard` (chunk-accumulator readiness confirmed). This run does not contradict that -- 810a's readiness proof used the lineage-default flag configuration; this run's collapsed formation count is a consequence of *this script's* flag override, not evidence that 810a's readiness finding was wrong.

**Did the experiment test the claims under conditions where they could express themselves?** No. The precondition gate that exists specifically to catch "nothing ARC-071-specific to discriminate with" correctly fired -- but the reason it fired is that the probe's own construction (flag scoped over the whole cell) suppressed chunk formation below the floor, not that MECH-090/ARC-071 failed to hold up under a fair test.

## 3. Biological-reference triage

Neither claim's biology is in question here. MECH-090 is grounded in beta-oscillatory gating of BG output to action selection (STN/striatum beta-band literature, already cited in the claim's own EXQ-049/EXQ-059b evidence history). ARC-071 draws on well-established striatal sequence-chunking literature (Graybiel 1998/2008, Sakai 2003, Wymbs 2012, Smith & Graybiel 2013, Yin & Knowlton 2006) already cited directly in the claim text, plus the Sutton 1999 options-framework formal analog. This autopsy's finding is a pure software probe-construction artifact (a flag scoped too broadly) with no bearing on either mechanism's biological grounding -- there is no formal-import-vs-biology divergence to adjudicate.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | Neither claim was fairly exercised; the precondition failure traces to the probe's own construction, not to claim/substrate incapacity. Matches the vocabulary used for the sibling MECH-090 cluster ("intact -- ... never let to express"). |
| Biological reference | clear | Both mechanisms have solid, directly-cited biological grounding; not implicated by this failure. |
| Developmental / dependency prerequisites | present | V3-EXQ-810a already proved 8/8-seed chunk formation and V3-EXQ-841 proved 2/2-chunk formation on these exact two seeds, under the lineage-default flag. The substrate's formation prerequisites are present; this run's own flag choice suppressed them. |
| Implementation completeness | complete | Fix `278599a` is landed and functioning exactly as designed -- the persistent-handle fallback DOES change agent behavior as intended. What's incomplete is the *probe's* handling of that flag's formation-phase side effects, not the substrate. |
| Environment adequacy | adequate | CausalGridWorldV2 8x8/2-hazard/6-resource, unchanged from 810a/841; not implicated. |
| Measurement adequacy | **under-instrumented / misleading -- primary defect layer** | `use_persistent_committed_program_handle=True` was applied for the whole cell instead of scoped to the probe phase, invalidating the "readiness inherited by construction" assumption the readiness gate depends on. |
| Integration adequacy | n/a | No cross-module integration failure; this is a single-flag scoping issue within one experiment driver. |
| Scale / capacity | n/a | Not implicated. |

**Recording-debt vs measurement-debt:** this is measurement-debt (test design), not recording-debt. The readout that would answer the post-fix persistence question (organic-formation chunk commitments during the probe) never existed to be recorded, because formation itself was suppressed by the probe's own flag scoping -- nothing was computed-but-discarded.

## 5. Learning extracted

- Applying a behavior-changing config override across an experiment cell's *entire* lifetime (formation + probe), when the override is only meant to be tested during the probe phase, can retroactively invalidate an "inherited readiness" claim that depends on formation replaying prior, differently-configured runs -- even when the override's intended effect (the between-tick fast path) is not directly about chunk formation. The RNG is seeded deterministically, but once agent behavior diverges (a different action taken on some tick), the environment trajectory diverges too, and that cascades into different downstream measurements (here, chunk-formation counts) that have nothing conceptually to do with the flag being tested.
- This is the second ARC-071 diagnostic in a row (after V3-EXQ-834) to land on `measurement_test_design_defect` rather than a substrate-level finding -- both times the substrate itself, when exercised under a design that doesn't perturb formation, behaves as expected (810a, 841). Worth watching if a third instance appears; not yet a granularity-debt pattern (see Step 9b question `arc071-commit-latch-postfix-persistence` for the open thread).
- The `sd084_midexec_reachability.py:271` precedent cited by this script's docstring as justification for a script-local flag override should be checked for the same whole-cell-vs-probe-only scoping question if it, too, sets a behavior-changing flag before formation runs -- flagged as a follow-on, not investigated here (out of scope for this autopsy).

## 6. Routing (user-confirmed 2026-08-02)

**Routing: `/queue-experiment`, same-question redesign, alphabetic suffix -- V3-EXQ-871a.**

Fix: scope `use_persistent_committed_program_handle=True` to the **probe phase only** -- flip it on the agent's live config object *after* `_run_formation` completes and *before* `_run_instrumented_probe` begins (rather than baking it into `_arm_flags()` / `base.build_agent()`), so formation replays V3-EXQ-841's proven 2/2-chunk dynamics under the lineage-default flag, and the persistence-restoration question is then tested against organically-formed chunks under the fix. All the existing instrumentation, thresholds, and verdict logic (`_analyze_cell`, `PERSISTENCE_RESTORED_MEAN_LENGTH_FLOOR` etc.) remain correct and reusable -- only the flag's scope needs to change.

Not `/implement-substrate` (nothing wrong with the substrate; 278599a works as designed). Not demotion (neither claim was fairly tested). Not `/lit-pull` (no biology divergence). Not a re-derive-brake case (0 prior ceiling hits for this sub-mechanism on either claim).

**Draft `evidence_quality_note` for governance to apply (both claims, `non_contributory` direction retained, category corrected):**

> V3-EXQ-871 (2026-08-02) self-routed `substrate_not_ready_requeue` (precondition `arc071_chunk_commitments_observed_supra_floor`: measured 0.0 vs threshold 10.0, worst seed) -- adjudicated `measurement_test_design_defect`, not a substrate ceiling. Root cause: `use_persistent_committed_program_handle=True` was set for the ENTIRE cell (formation + probe), not scoped to the probe phase. That flag changes `select_action`'s between-E3-tick fast path (`agent.py:5999-6014`): once any commitment is present (chunk-sourced or not) and beta_gate is elevated, the agent now steps a planned macro-action from the committed trajectory instead of holding `_last_action`. This alters the action sequence from the first relevant tick onward, which (via RNG-coupled environment dynamics -- RNG reset confirmed deterministic per seed) cascades into materially different chunk-formation outcomes: this run's seeds 101/505 formed only 1/0 chunks respectively during the identical 120ep formation schedule, versus 2/2 chunks for the SAME two seeds under V3-EXQ-841 (flag at lineage default False) on 2026-07-31 -- a direct same-seed comparison. V3-EXQ-810a's/841's "readiness inherited by construction" claim does not hold once the flag is set globally; it only holds when the flag stays at its lineage default during formation. Fix: scope the flag to the probe phase only (V3-EXQ-871a). Neither MECH-090 nor ARC-071 evidence changes (`non_contributory`, `precondition_unmet`).

**Per-target JSON fields:** see `failure_autopsy_V3-EXQ-871_2026-08-02.json`.

## 7. Hypothesis-space ledger (Step 9b)

Registered a new question `arc071-commit-latch-postfix-persistence` in `hypothesis_space_registry.v1.json` (claims MECH-090, ARC-071; `fanout_sources: ["failure_autopsy_V3-EXQ-871_2026-08-02.json"]`), with two pre-registered hypotheses (`persistence_restored_post_fix`, `persistence_still_broken_post_fix`), both left `alive` -- this run recorded as a `resolving_runs` entry with `epistemic_category: measurement_test_design_defect`, `control_passed: false`, `non_degenerate: false`, `met_elimination_bar: false`. The run narrows nothing (an uninformative/starved-by-design result, not a discrimination), matching the precedent set by several existing `alive`-with-`resolving_runs` entries in the registry (e.g. `q081-cross-stream-shared-organisation` H-reach-per-region-vs, `mech204-sd076-...` H1/H2). `decision.decidable: false`; `observation_bottleneck` states that a redesigned probe (V3-EXQ-871a, flag scoped to probe-only) is needed before either hypothesis can be discriminated. Ran `build_hypothesis_space.py` + `check_hypothesis_space_integrity.py` after the append; no `(a)/(b)/(c)/(d)` flags on the new question (see integrity report).
