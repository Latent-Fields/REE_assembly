# Failure autopsy -- V3-EXQ-830 (MECH-321 scale-resolved rollout boundary diagnostic)

**Generated:** 2026-07-29T07:16:51Z
**Session:** `cranky-blackburn-d11b32` (worktree)
**Scope:** single
**Status:** confirmed (user-adjudicated at the Step 8 gate)
**Target:** `v3_exq_830_mech321_scale_resolved_rollout_boundary_20260727T204927Z_v3` (V3-EXQ-830)
**Trigger:** `pending_review.md` -> "Diagnostic adjudication required (self-route unverified)" -- **PASS flagged `vacuous_pass`**

**Changes no claim status, confidence, live_status or v3_pending.** Analysis + handoff only.

---

## Verdict in one paragraph

**The `vacuous_pass` flag is a FALSE POSITIVE, and the flagged self-route `slow_never_fires_on_rollout` STANDS.** The flag is an artifact of a key-naming mismatch inside the manifest's own `interpretation` block, not a degenerate gate: `criteria_non_degenerate{}` uses short keys (`C_DISSOCIABLE`) while `criteria[].name` uses long names (`C_DISSOCIABLE_low_cofire_distinct_positions`), so the indexer's V3-EXQ-783 `load_bearing:false` exclusion -- which matches on exact `name` -- cannot fire, and the legacy vacuity check trips on a criterion the author had explicitly declared non-load-bearing. Renaming the keys to match yields `verified`. Separately, and more consequentially, this autopsy scoped **why MECH-321's R4 mid-execution hook has never executed**: it is **structurally unreachable** under the standard driver loop, because `E3Selector.post_action_update` unconditionally destroys `_committed_trajectory` on every step while the hook requires that trajectory to survive *across* ticks. This is not an environment or harness property -- `decomp_n_evaluated_midexec = 0` is guaranteed for **any** experiment using the standard `select_action -> update_residue` loop. The substrate already contains the correct fix pattern (`_closure_committed_trajectory`, built for exactly this reason), so the node is `complicated (buildable)`.

---

## 1. Facts reconstruction (no interpretation)

### 1a. Manifest

| Field | Value |
|---|---|
| `outcome` | `PASS` |
| `experiment_purpose` | `diagnostic` |
| `evidence_direction` | `non_contributory` |
| `claim_ids` | `[]` (diagnostic; weights nothing) |
| `bears_on` | `MECH-321`, `MECH-288`, `ARC-070` |
| `interpretation.label` | `slow_never_fires_on_rollout` |
| indexer `adjudication` | **`vacuous_pass`** |
| `machine` / `machine_class` | `DLAPTOP-5.local` / `darwin-arm64-py3.13-torch2.12.0` |
| `elapsed_seconds` | 8540.5 |
| `substrate_hash` | `6b5f1090fa2aeddb94462b685b6419d101c6fa9377d39236b8195962022d7ce2` |

**Recording provenance: always-core COMPLETE.** All seven Experimental Recording Standard §3b fields are present (`recording_schema` `rec/v1`, top-level `substrate_hash`, `machine`, `machine_class`, `elapsed_seconds`, full `config`, explicit `seeds`). **There is no recording gap**, so the readings below are falsifiable against a known substrate and no re-run is owed on recording grounds.

**Caveat recorded, not fatal: `substrate_stable_across_run: false`.** Two distinct per-cell substrate hashes were observed within the run, and both differ from on-disk-now (drift resolved at 18:37:23Z and 19:50:09Z while the run executed to 20:49:30Z) -- other sessions were landing `ree-v3` commits mid-run. This does **not** undermine the readings: the decisive counters are uniform across all 10 cells and both hashes, and ARM_PROBE_OFF/ARM_PROBE_ON produced bit-identical position histograms and identical `net_harm_per_step`. Flagged so a later reader is not surprised by it.

### 1b. Criteria as declared

| Criterion (`criteria[].name`) | `load_bearing` | `passed` | `criteria_non_degenerate` key -> value |
|---|---|---|---|
| `C_DECIDABLE_instrument_returned_a_reading` | **true** | **true** | `C_DECIDABLE` -> true |
| `C_SLOW_FIRES_on_rollout` | false | false | `C_SLOW_FIRES` -> true |
| `C_DISSOCIABLE_low_cofire_distinct_positions` | false | false | `C_DISSOCIABLE` -> **false** |
| `C_CONTROL_slow_silent_with_flag_off` | false | true | `C_CONTROL` -> true |

The load-bearing criterion **passed** and is **non-degenerate**. The design deliberately made `C_DECIDABLE` (did the instrument return a reading) load-bearing rather than `C_SLOW_FIRES`, so that all three pre-registered spike readings score as informative and only a not-ready instrument FAILs. That is correct diagnostic design.

### 1c. Decisive metrics

| Metric | Value |
|---|---|
| `on_n_sweeps` | 2393 |
| `on_n_sweeps_with_slow` / `on_n_seeds_with_slow` | **0 / 0** |
| `on_n_sweeps_cofire` | 0 |
| `on_fast_fires_total` | 1387 |
| `on_zgoal_present_frac` | 0.870 |
| `on_zgoal_norm_std_best_cell` | 0.0700 (floor 1e-4) |
| `on_instrumentation_coverage_worst` | 1.000 (floor 0.99) |
| `control_arm_slow_fires_total` | 0 |
| `on_n_evaluated_precommit` | 11423 |
| **`on_n_evaluated_midexec`** | **0** |
| **`on_midexec_dilution_frac`** | **0.0** |
| `on_slow_frac_naive` / `on_slow_frac_precommit_corrected` | 0.0 / 0.0 |
| `n_seeds_action_seq_differs` | 0 |

Per-cell: `decomp_n_evaluated_midexec = 0` in **all 10 cells** (5 seeds x 2 arms) while `decomp_n_evaluated_precommit` ran **1862-2618** and `decomp_n_decomposed_precommit` ran **214-322**. Decomposition demonstrably fired pre-commit; the mid-execution phase never occurred once.

### 1d. Which criterion "failed"

Neither an absolute nor a negative-control criterion failed. The negative control (`C_CONTROL`, the OFF arm's slow scale silent) **passed**, and the load-bearing decidability criterion **passed**. The two failing criteria (`C_SLOW_FIRES`, `C_DISSOCIABLE`) are the *content* of the pre-registered null, not defects.

---

## 2. The `vacuous_pass` flag -- adjudicated a FALSE POSITIVE

### 2a. Mechanism

`build_experiment_indexes._compute_adjudication` runs an author-free check (3b) that honours the explicit `load_bearing` tag, then falls through to a **legacy author-trusted** check that is load_bearing-blind except for an exclusion set built at lines 456-466:

```python
non_load_bearing = set()
for c in interp.get("criteria"):
    if c.get("load_bearing") is False:
        non_load_bearing.add(c.get("name"))          # LONG names
degeneracy_assertions = [v for k, v in crit.items()
                         if not str(k).endswith("_branch")
                         and str(k) not in non_load_bearing]   # SHORT keys -- never match
if status == "PASS" and any(v is False for v in degeneracy_assertions):
    return label, "vacuous_pass"
```

830's exclusion set is `{C_SLOW_FIRES_on_rollout, C_DISSOCIABLE_low_cofire_distinct_positions, C_CONTROL_slow_silent_with_flag_off}`; its `criteria_non_degenerate` keys are `{C_DECIDABLE, C_SLOW_FIRES, C_DISSOCIABLE, C_CONTROL}`. **No key matches any name**, so nothing is excluded, and `C_DISSOCIABLE: false` fires the flag.

Verified by direct execution of `_compute_adjudication` on the manifest:

- as-shipped -> `('slow_never_fires_on_rollout', 'vacuous_pass')`
- with `criteria_non_degenerate` keys renamed to the matching `criteria[].name` -> `('slow_never_fires_on_rollout', 'verified')`

Nothing else about the manifest changes. The flag is entirely an effect of the key spelling.

### 2b. Why the degeneracy itself is CORRECT

`C_DISSOCIABLE` is genuinely degenerate, and the author was right to record it so: **dissociability cannot be measured when the slow scale never fires.** With `on_n_sweeps_with_slow = 0` there is nothing to dissociate from the fast scale, so the criterion cannot discriminate. Recording `false` is honest; tagging it `load_bearing: false` is also correct, because the run's decidability does not rest on it. The manifest is scientifically well-formed. The **only** defect is that the two blocks spell the same criteria differently.

### 2c. Corpus scope -- SINGLE, not a cluster

Swept all 159 diagnostic/baseline manifests carrying both an `interpretation.criteria[]` and a `criteria_non_degenerate{}` block, looking for a `vacuous_pass` caused by a short-key/long-name mismatch on a criterion tagged `load_bearing: false`. **Exactly one hit: V3-EXQ-830.** This is an authoring slip in one manifest, not a systemic corpus defect -- so this autopsy is `scope: single` and no cluster table applies.

It is nonetheless a **latent** defect class: nothing anywhere requires `criteria_non_degenerate` keys to match `criteria[].name`, so the exclusion added for V3-EXQ-783 can be silently defeated again by any author who abbreviates. Both fix loci below were confirmed by the user at the Step 8 gate.

### 2d. Relation to V3-EXQ-783

Same **outcome class** (a legacy-path `vacuous_pass` on a criterion the author declared non-load-bearing), **different route**. 783 was blocked because the legacy path was blind to the `load_bearing` tag; the fix added the exclusion set. 830 is blocked *despite* that fix, because the exclusion is keyed on exact string equality and the manifest uses two spellings. The 783 fix is not wrong -- it is under-specified about the join key.

---

## 3. Scoping: why the MECH-321 R4 mid-execution hook never fires

This was the second half of the commission. The finding is stronger than "it is rare in this harness".

### 3a. The hook and its gate conjunction

`ree_core/agent.py:5519` onward, inside `select_action` (def at 5252):

1. `policy_decomposition is not None`
2. `beta_gate.is_elevated`
3. `hippocampal is not None and hippocampal.event_segmenter is not None`
4. **`e3._committed_trajectory is not None`**
5. `_mid_meta["source"] in ("arc071_chunk", "mech321_decomposed")`
6. `len(_mid_remaining) > 1`
7. `_current_latent is not None`

830 ran with `use_policy_decomposition`, `use_policy_chunking`, `use_chunk_proposal_injection` and `use_event_segmenter` all True, so (1) and (3) held throughout. Gates (5) and (6) are satisfiable in principle: the metadata sources are genuinely emitted by `ree_core/hippocampal/module.py:889` (`mech321_decomposed`) and `:1041` (`arc071_chunk`), and the harness's `seeded_chunk_sequence` is `[0,1,2]`, which would leave 3 then 2 remaining actions -- both above the `> 1` floor.

### 3b. Gate (4) is the binding one, and it is structural

`_committed_trajectory` has exactly **one** setter, `E3Selector.select` at `e3_selector.py:3499`, under `if committed:`. It has an unconditional destroyer: the **last statement** of `E3Selector.post_action_update` (`e3_selector.py:3874`, def at 3595, next def at 3877) is

```python
self._committed_trajectory = None
return metrics
```

`post_action_update` is called from `REEAgent.update_residue` (`agent.py:8599`), and the 816-family driver -- which 830 inherits verbatim -- calls `agent.update_residue(harm_signal)` on **every** step (line 293), immediately after `agent.select_action(cands, ticks)` (line 290).

So the per-step sequence is:

```
select_action(...)          # midexec hook at agent.py:5501 tests gate (4) HERE
   ... env.step ...
update_residue(...) -> e3.post_action_update(...) -> _committed_trajectory = None
```

The hook needs a trajectory committed on a **previous** tick -- its own comment says it re-evaluates *"the REMAINING (unexecuted) content of an already-committed ARC-071 chunk trajectory"*, which is inherently cross-tick. Every previous tick ends by destroying it.

Nor can the trajectory be set earlier **within** the same `select_action`: the hook sits at line 5501, while both `self.e3.select(...)` call sites inside `select_action` are at 7513 and 8520 -- **after** it -- and the other selection path, `_e3_tick`, is invoked at line 5151, i.e. outside `select_action` entirely. Two conditional release sites (`agent.py:5435`, `:5493`) also clear the handle *before* the hook.

The design comment at `e3_selector.py:345` states the property directly: `_committed_trajectory` is *"set ONLY under the F-driven `if committed:` path and torn down every tick by post_action_update"*.

### 3c. Six converging lines of evidence

| # | Evidence |
|---|---|
| 1 | Unconditional teardown is the final statement of `post_action_update` (`e3_selector.py:3874`) |
| 2 | `update_residue` calls it every step (`agent.py:8599`); the 816/830 driver calls `update_residue` every step (line 293) |
| 3 | The hook (5501) precedes every in-`select_action` `e3.select()` call (7513, 8520) -- the sole setter |
| 4 | `_e3_tick`, the other selection path, is called at 5151, outside `select_action` |
| 5 | Empirically `decomp_n_evaluated_midexec = 0` in all 10 cells, against 1862-2618 pre-commit evaluations |
| 6 | The contract `test_mech321_scale_resolved_boundary.py` reaches the hook **only** by hand-injecting `fake_traj.metadata`, `_committed_step_idx = 1` and a forced `beta_gate.elevate()`, behind an explicit anti-vacuity guard |

**Conclusion: `decomp_n_evaluated_midexec = 0` is a structural guarantee of the standard driver loop, not a property of the 816 harness, the harshened environment, or the commitment configuration.** MECH-321's R4 second phase has never executed and, under the current commit lifecycle, cannot.

### 3d. Three consequences

1. **830's `midexec_dilution_frac = 0.0` is correct and structural, not a small sample.** The mid-execution asymmetry documented in the manifest's own `follow_on_named_not_done` is *bounded at exactly zero*, so the `slow_never_fires_on_rollout` reading carries no mid-execution dilution confound. This **strengthens** the 2026-07-29 closure of the scoping spike's section 5b rather than qualifying it.
2. **`use_decomposition_scale_resolved_probe_midexec` (ree-v3 `aaf5caac26`) is not merely unexercised -- it is unreachable.** The flag is correct and contract-covered, and it modifies a signature dict inside a block that never runs. It should not be read as validated by 830.
3. **The fix pattern already exists in the substrate.** `_closure_committed_trajectory` was introduced precisely because of this teardown -- its own docstring says *"Unlike `_committed_trajectory` it is NOT torn down by post_action_update -- it persists across ticks so the between-E3-tick stepping path can advance a closure-formed committed PROGRAM (C-STEP) rather than repeating `_last_action`."* That is the same requirement the mid-execution hook has. The node is therefore `complicated (buildable)`: a named build with no open question, not a probe-gated unknown.

---

## 4. Claim-layer mapping

`claim_ids` is **empty** (correct -- 830 is a diagnostic and weights nothing). It `bears_on` three claims:

| Claim | Type | Status | Bearing of this run |
|---|---|---|---|
| MECH-321 | MECH | `candidate` / `v3_pending` | R1 pre-commitment half exercised heavily (11423 evaluations); **R4 mid-execution half shown never to have executed**. No status change. |
| MECH-288 | MECH | -- | Slow BOCPD scale shown not to fire *on the rollout stream*. Says nothing about the observation stream, where the slow scale is separately contracted. **Does not weaken MECH-288.** |
| ARC-070 | ARC | -- | Decomposition machinery demonstrably functional pre-commit. No pressure. |

The tags are accurate and were not inherited stale from a predecessor. No claim is falsified or weakened by this run; a diagnostic PASS with a pre-registered null is exactly the intended output.

---

## 5. Biological-reference triage

**Closest reference mechanism.** The R4 mid-execution re-evaluation is a *within-action-sequence monitoring and abort* function: the ability to re-open an already-committed motor program part-way through when the world stops matching the plan. In mammals this is the supplementary/pre-SMA and dorsomedial frontal contribution to ongoing-action monitoring, with the basal-ganglia stop pathway providing the abort, and it is unambiguously a real capability -- interrupting a reach mid-flight when the target moves is the canonical behavioural demonstration.

**Is this a formal-definition import?** No. MECH-321's R4 is a mechanism translation, not a formalism (unlike SD-003's Pearl-counterfactual import). The trigger it reuses (MECH-288 boundary detection) is likewise mechanism-shaped.

**Does the failure resemble a missing biological dependency?** Yes, and precisely. In brains, a committed motor program has a **persistent representation** that outlives the moment of commitment -- that persistence is what monitoring acts *on*. REE's `_committed_trajectory` is destroyed at the end of every tick, so the substrate has the *monitor* (the hook, correctly written) but not the *persistent program representation* the monitor needs. This is a missing-dependency signature, not evidence against the claim: **the mechanism has never had the substrate it requires in order to express itself.**

**Literature status.** No `targeted_review_MECH-321` dossier exists. Because this is a mechanism translation rather than a formal import, and because the diagnosis is a concrete substrate gap rather than a biology divergence, a `/lit-pull` is **not** the primary output here. Worth registering as a lower-priority gap if the build below proceeds and the abort semantics need grounding.

---

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact (R4 half untested)** | The R1 half was exercised at scale; the R4 half could not express itself. Nothing falsified. |
| Biological reference | **clear** | Mid-flight action monitoring / abort; SMA-preSMA + BG stop. Failure matches a missing persistent-program dependency. |
| Developmental / dependency prerequisites | **missing** | A commit handle surviving `post_action_update` is a prerequisite the substrate does not provide to this hook. |
| Implementation completeness | **partial -- symbol without functional role** | The hook is written, correct, flagged and contract-covered, and sits behind a gate that no standard run can satisfy. |
| Environment adequacy | **adequate (not the cause)** | The harshened 816d env is irrelevant to the finding; the teardown is unconditional. |
| Measurement adequacy | **adequate** | Instrumentation coverage 1.000; the phase-split counters are exactly what exposed this. The counters did their job. |
| Integration adequacy | **coupled but inconsistent** | Two subsystems each internally correct: E3's per-tick commitment teardown, and a hook requiring cross-tick persistence. The contradiction lives in the seam. |
| Scale / capacity | **not implicated** | 2393 sweeps, 5 seeds, 11423 pre-commit evaluations -- ample. |

**Recommended `epistemic_category`: `competence_implementation_gap`.** Deliberately **NOT** `substrate_ceiling`: nothing was tested and found wanting: the mechanism was never reachable. Calling this a ceiling would inflate the re-derive brake against MECH-321 for a mechanism that has never once run.

**Re-derive brake (MOVE-3): does NOT fire.** Counted under the R1-R3 convention: MECH-321 **0**, MECH-288 **0**, ARC-070 **0** prior `substrate_ceiling` hits. Threshold is 2. No re-queue refusal is owed.

**Granularity-debt recurrence trigger: does NOT fire.** `granularity_debt_cluster.py MECH-321` reports **2 targets across 1 file** (`failure_autopsy_816-820-policy-decomposition-cluster_2026-07-26`, runs V3-EXQ-816 and V3-EXQ-820), alignment distribution **`intact=2`** -- **no target reads `weakened`**. Per the standing rule that is measurement/implementation debt, not granularity debt, regardless of count. No `/claim-synthesis` handoff.

---

## 7. Learning extracted

1. **MECH-321's R4 mid-execution phase has never executed in any experiment, and is structurally unreachable under the standard `select_action -> update_residue` loop.** `post_action_update` unconditionally destroys `_committed_trajectory` every step; the hook requires it to survive across ticks.
2. **A `load_bearing` exclusion keyed on exact string equality can be silently defeated by an author using two spellings for one criterion.** The V3-EXQ-783 fix is correct but under-specified about its join key; nothing validates that `criteria_non_degenerate` keys correspond to `criteria[].name`.
3. **A contract that reaches its target only via hand-injected preconditions proves reachability-in-principle, never reachability-in-practice.** `test_mech321_scale_resolved_boundary.py` has a correct anti-vacuity guard and still could not have caught this: the guard asserts the hook was reached *given* the injected state. A "does this fire in a real rollout?" assertion is a different and missing test.
4. **Phase-split counters earn their keep.** `decomp_n_evaluated_{precommit,midexec}` were added to bound a dilution; they instead exposed that an entire declared mechanism phase never runs. Cheap generous recording surfaced a structural defect no criterion was looking for.
5. **A flag added to close a measurement asymmetry can be unreachable for the same reason the asymmetry was invisible.** `use_decomposition_scale_resolved_probe_midexec` modifies a dict inside a block that never executes -- correct, contract-covered, and inert.
6. **830's zero dilution is structural, which strengthens rather than qualifies the 5b closure.** The mid-execution confound is bounded at exactly zero for reasons independent of the harness.

---

## 8. Repair pathway and routing (user-confirmed at the Step 8 gate)

### 8a. Primary -- `/implement-substrate`: a commit handle that survives the per-tick teardown

Node: `complicated (buildable)`. Build a persistent committed-program handle for the mid-execution hook, mirroring the existing `_closure_committed_trajectory` precedent (set on commit entry, cleared on principled release / closure fire / episode reset, **not** cleared by `post_action_update`), and point gate (4) at it. Default-off behind a flag so the OFF path stays bit-identical -- note this is **not** a pure diagnostic change: a reachable mid-execution hook can fire `boundary.fired` and **release the commit latch**, aborting the remaining macro.

Only once that lands does `use_decomposition_scale_resolved_probe_midexec` become exercisable, and only then is MECH-321's R4 half measurable at all.

### 8b. Secondary -- adjudication-machinery hardening (both loci confirmed)

- **`ree-v3/validate_experiments.py`** -- author-time lint: WARN when a `criteria_non_degenerate` key matches no `interpretation.criteria[].name`. Prevents new manifests acquiring the defect. No retroactive re-scoring.
- **`REE_assembly/evidence/experiments/scripts/build_experiment_indexes.py`** -- make the `non_load_bearing` exclusion tolerate the short-key/long-name relationship (a key that is a prefix of exactly one `criteria[].name`), so 830 and any future case adjudicate correctly without editing manifests. Must be conservative: match only on an unambiguous single prefix hit, never a fuzzy match.

Both are infrastructure, not governance-plane objects. Neither is applied by this skill.

### 8c. Explicitly NOT recommended

- **No re-queue of 830.** Its instrument worked, its coverage was 1.000, and its reading is sound. A re-run changes nothing.
- **No claim demotion.** Nothing was tested and found wanting.
- **No `substrate_ceiling` reading**, and therefore no re-derive-brake increment against MECH-321.
- **No GOV-FANOUT-1 portfolio.** The bottleneck routes to a single unambiguous build, which is the stated exemption.

### 8d. Draft `evidence_quality_note` for governance (text only -- not written by this skill)

> V3-EXQ-830 (2026-07-27, diagnostic, PASS/non_contributory) exercised MECH-321's R1
> pre-commitment decomposition at scale (11423 evaluations, 2393 sweeps, 5 seeds) and
> returned the pre-registered null `slow_never_fires_on_rollout`: with a live, varying
> z_goal stream present on 87% of sweeps (`zgoal_norm_std` 0.070 vs a 1e-4 floor) the
> MECH-288 slow BOCPD scale fired zero times on the rollout stream. The run's
> `vacuous_pass` adjudication flag was investigated and adjudicated a FALSE POSITIVE
> (failure_autopsy_V3-EXQ-830_2026-07-29): it is caused by `criteria_non_degenerate`
> keys being spelled shorter than the matching `criteria[].name`, defeating the
> V3-EXQ-783 `load_bearing:false` exclusion; corrected key spelling adjudicates
> `verified`. Separately, the same run establishes that MECH-321's R4 MID-EXECUTION
> phase has NEVER executed and is structurally unreachable under the standard driver
> loop -- `E3Selector.post_action_update` unconditionally clears `_committed_trajectory`
> every step (e3_selector.py:3874) while the hook requires cross-tick persistence
> (agent.py:5519, gate 4). MECH-321's R4 half is therefore UNTESTED, not unsupported;
> no ceiling reading applies. Retest after the persistent-commit-handle substrate lands.

---

## 9. Hypothesis-space ledger delta (Step 9b)

**No `fanout_recommendation` is emitted** (single unambiguous build -- the GOV-FANOUT-1 exemption).

830 does adjudicate a leg, but not one belonging to the existing `policy_decomposition_discrimination` question (whose six hypotheses concern whether R1 reduces forward-PE and is dissociable from R5). 830 answers the **scale-heterogeneity** question frozen by the 2026-07-27 scoping spike's section 5b decision table -- a three-row, mutually-exclusive, genuinely pre-registered rival set. That is registered here as a **new question**, which is invariant 6's sanctioned growth path and needs no fan-out-growth witness.

New question `decomposition_scale_heterogeneity` (claims MECH-321 / MECH-288 / ARC-070), `initial_frozen_count = 3`, `pre_registered_utc = 2026-07-27T00:00:00Z` (the spike doc's date, committed **before** 830 resolved at 2026-07-27T20:49:27Z, so the ordering invariant holds honestly):

| hid | axis | resolution | basis |
|---|---|---|---|
| `H-scales-dissociable-on-rollout` | arbitration | **eliminated** | 0 slow fires, 0 cofire across 2393 sweeps / 5 seeds with a live varying z_goal stream; control arm silent; `C_SLOW_FIRES` non-degenerate. |
| `H-slow-fires-only-with-fast` | arbitration | **eliminated** | Same evidence: the slow scale fired zero times, so it does not fire coincidently with fast either. |
| `H-slow-never-fires-on-rollout` | representation | **confirmed** | 830's reading. z_goal varies across sweeps (std 0.070) but not informatively *within* one -- a rollout is too short to carry two timescales. `control_passed: true`. |

Net: 3 pre-registered, 3 resolved (2 eliminated, 1 confirmed) -- a clean 3 -> 1 narrowing. Both axes (`arbitration`, `representation`) already exist in the `axis_families.map`, so no new family row is required.

---

## 10. Confirmed routing

| Item | Routing |
|---|---|
| Persistent commit handle for the mid-execution hook | **`/implement-substrate`** (`recommended_substrate_queue_entry.action = create`) |
| `validate_experiments.py` key-correspondence lint | infrastructure fix (confirmed) |
| `build_experiment_indexes.py` prefix-tolerant exclusion | infrastructure fix (confirmed) |
| V3-EXQ-830 itself | mark adjudicated at the next `/governance` walk; **no re-queue** |
| MECH-321 / MECH-288 / ARC-070 | **no status, confidence, live_status or v3_pending change** |
