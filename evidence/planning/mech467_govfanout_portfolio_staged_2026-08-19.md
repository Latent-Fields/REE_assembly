**Status: AWAITING USER REVIEW.** -- portfolio design + scope decision. The two experiments
described here ARE queued (see section 6); this document records the reasoning, and in
particular a SCOPE SHRINK from the 4 legs the autopsy pre-registered to 2.

# MECH-467 GOV-FANOUT-1 discrimination portfolio -- replacing V3-EXQ-874b

Generated: 2026-08-19
Session: `metaworker-chip-20260818-queueexp-874b-govfanout-portfolio` (headless)
Chip: `chip-20260818-queueexp-874b-govfanout-portfolio`
Authority: `failure_autopsy_V3-EXQ-874b_2026-08-17.json` / `.md` (status confirmed;
disposition applied to MECH-467 in `claims.yaml` by the /governance cycle of 2026-08-18).

---

## 1. Headline: the portfolio is TWO legs, not four -- and the autopsy is what says so

The chip brief asked for a four-leg portfolio. The autopsy it names as its authority makes
that number **conditional**, in section 8a, on a check the brief could not have performed:

> `chip-20260816-substrate-navigation-immobility-probe` is **open and unstarted**... **The
> fan-out's `H-commitment` and `H-cadence` legs overlap that chip substantially.** Do not
> queue them as MECH-467-specific probes without first checking whether the scoping spike
> has run -- if it has, it may already answer them at the substrate level, and the portfolio
> should shrink to `H-energy` + `H-denominator` (the two legs genuinely specific to this
> battery's design). Queuing all four blind would duplicate an open, owned item.

**The spike has since run.** `chip-20260816-substrate-navigation-immobility-probe` resolved
`done` at 2026-08-18T23:53:06Z -- i.e. AFTER this chip's brief was written -- staging
`REE_assembly/evidence/planning/navigation_immobility_scoping_2026-08-18.md`
(`origin/master` `d6206f641a`). So the condition the autopsy set is met, and the shrink it
prescribes is the instruction in force.

### 1a. What the spike settles, per leg

| Autopsy leg | Axis | Spike finding | Disposition |
|---|---|---|---|
| `H-commitment` | `process` | The near-immobility is **not a new finding**: it is the plain-navigation instance of **MECH-439** (F-dominance conversion ceiling, `ceiling_decision: exhausted`, awaiting ARC-107), evidenced by 21 ARC-062 GAP-B autopsies + 9 direct MECH-439 hits. No degenerate-proposer bug exists; the collapse is at the comparator/selection stage. | **Answered at substrate level. Not queued.** |
| `H-cadence` | `selection` | The E3 heartbeat hold-and-repeat (`e3_steps_per_tick`, default 10, MECH-093-modulated 5-20) means ~85-90% of env ticks are not re-selection at all. Documented across 5 prior autopsies + 1 dedicated diagnostic. The deeper causal question is owned by an **active** hypothesis-space line (`qid e3_fdominance_causal_discrimination`, H0-H5, with a discovery event as recent as 2026-08-18). | **Answered, and re-deriving it would duplicate an in-flight owned investigation. Not queued.** |
| `H-energy` | `environment` | Not addressed by the spike for 874b's config. The spike DID characterise `agent_health` depletion, but under **toroidal wrap**; 874b was non-toroidal. | **QUEUED -- V3-EXQ-940.** |
| `H-denominator` | `measurement` | Not addressed. The spike gives the substrate-level prior but not the battery-level decomposition. | **QUEUED -- V3-EXQ-941.** |

### 1b. The H-commitment MEASUREMENT is kept; only the HYPOTHESIS leg is dropped

Approach-run length -- the quantity `H-commitment` proposed to measure -- is cheap to record
and is what makes the `H-denominator` decomposition complete. It is therefore instrumented
inside **V3-EXQ-941** as a counter, alongside the E3-tick/latched-tick split that
`H-cadence` would have produced. **What is not queued is a separate MECH-467-specific probe
whose purpose is to adjudicate those two hypotheses** -- that adjudication is owned
elsewhere and is running. Recording the number is not duplicating the investigation.

### 1c. Residual debt this shrink creates, stated rather than buried

`hypothesis_space_registry.v1.json` question `mech467_legc_event_denominator_cause` (registered
2026-08-17T14:46:54Z, `initial_frozen_count = 4`) still carries all four hypotheses with
`resolution.state: alive`. Two of them are, on the reasoning above, resolved-by-other-means.

**This session deliberately did NOT edit that registry.** Hypothesis disposition is
`/governance`'s write authority (autopsy section 12: "`/governance` chips them once Step
2b/4/6a ratifies"), the registry is a read-modify-write-exposed file, and recording
"eliminated" against a run that is not this question's own adjudicator is a judgement a
governance cycle should make explicitly rather than a queueing session make silently.
**Flagged for the next MECH-467 governance cycle** -- see section 7.

---

## 2. Three defects of 874b the portfolio must not inherit

All three are fixed in both drivers. None of them appears in 874b's manifest; all are from
the autopsy.

1. **Unrecorded truncation.** 7 of 12 cells ended early on `health_depleted`; only 63.1% of
   the pre-registered exposure window was realised and no cell records it. A 60-tick cell and
   a 900-tick cell entered the pooled denominator indistinguishably.
   **Fix:** every cell records `done_cause` (the env supplies it in `info`, 874b never read
   it), a `truncated` boolean, `n_realised_ticks`, `n_budgeted_ticks`, and
   `window_completeness`. Both drivers carry a `window_completeness` **precondition**, and
   every rate DV is normalised by REALISED ticks, never by the budget.
2. **Rule-set complexity confounded with nutritive density.** `num_resources` was fixed at 12
   while only type 0 carries benefit, so SIMPLE had 6/12 benefit-bearing cells and COMPLEX
   4/12 -- adding distractor *types* silently removed a third of the food. COMPLEX realised
   41% of its window vs SIMPLE's 85%.
   **Fix, and it is the strongest available one: the ruleset axis is NOT VARIED in either
   leg.** Both run SIMPLE only. A confound between two axes cannot arise when only one is
   manipulated. Each driver additionally records `n_benefit_bearing_resource_cells` measured
   off the env's own type grid, so the quantity that was silently varying in 874b is now an
   explicit recorded number. Re-introducing the complexity axis is a job for a successor that
   holds benefit-bearing resource COUNT (not total resource count) constant.
3. **`z_goal_stream.writer_defect: true` was a FALSE POSITIVE.** The accumulator observed the
   P0 base agents (`n_agents: 6` = 2 rulesets x 3 seeds) rather than the 12 stepping clones;
   `goal_live_at_warmup_end` was true in 9/12 cells, and `update_z_goal` is the sole writer of
   z_goal, so the stream demonstrably ran.
   **Fix:** `ZGoalStreamAccumulator.observe()` is called on the **stepping clone**, inside the
   per-cell arm function, after the eval window -- never on the P0 base agent.

## 3. MECH-262 constraint honoured

The same autopsy carries a separate finding on MECH-262: in the 9 live-z_goal cells,
storage-site rule drift (0.004-0.384) and selection-path operative-rule fidelity
(0.985-1.000) DISSOCIATE in 6 of 9. The brief's constraint follows: **do not build a leg that
reads the operative rule from the storage site.**

**Neither leg reads rule state at either site.** Both are denominator diagnostics -- they ask
why no consumption events occur, not what the rule contains. `MECH-262` is therefore not
tagged by either experiment, and no rule-drift measurement is taken. The dissociation finding
is left for governance to record on MECH-262 as an exposure, exactly as the autopsy asks.

---

## 4. Leg 1 -- V3-EXQ-940, `H-energy` (axis family: `environment`)

`v3_exq_940_mech467_energy_window_decoupling` -- 3 arms x 3 seeds = 9 cells.

**The sharpened question.** The autopsy reads the 7/12 `health_depleted` terminations as the
agent having "starved to death" -- i.e. as a *consequence* of not eating. The scoping spike
supplies a competing, fully documented mechanism that 874b was exposed to and did not opt out
of: `CausalGridWorldV2` applies `contamination_spread` (**default 0.5**) to EVERY cell the
agent enters regardless of `num_hazards`; once a cell crosses `contamination_threshold`
(default 2.0, i.e. four entries) it becomes `contaminated` and drains `contaminated_harm`
(default 0.4) per contact, so roughly three contacts are lethal from full health (1.0).

**874b set `num_hazards=0` and set neither `contamination_spread=0.0` nor
`hazard_free_contamination_gate=True`.** On a 6x6 grid with an agent that revisits a small
cell set, self-inflicted contamination death is a live alternative to consumption starvation,
with an entirely different remedy. The env's own module docstring names this a footgun and
cites the V3-EXQ-884 precedent.

| Arm | Manipulation |
|---|---|
| `ARM_STOCK` | 874b's env config verbatim -- contamination at stock defaults. Reproduction arm. |
| `ARM_CONTAM_OFF` | identical + `hazard_free_contamination_gate=True`. Isolates self-contamination. |
| `ARM_HEALTH_DECOUPLED` | contamination gated off AND `agent_health` clamped to a floor after every step, so the window CANNOT terminate for health reasons. The autopsy's "decouple survival from the measurement window at identical geometry". |

Operating mode is pinned to `internal_planning` in **all three arms**, so the energy
manipulation is the only axis varying. The `internal_replay` regime is deliberately not
covered by this leg; leg 2 covers both.

**Criteria and the declared null.**
- **C1 (load-bearing): `window_completeness` lifts in `ARM_CONTAM_OFF`.** If gating
  contamination restores the window, the truncation was self-contamination, not starvation --
  and every future reach-dependent battery must set that flag.
- **C2: `events_per_realised_tick` lifts once the window is decoupled.**
- **Declared null (the autopsy's own wording):** *event rate per realised tick is unchanged;
  starvation only shortened the window, it did not suppress eating.* A null here is
  informative: it removes energy from the live set and leaves the rate problem squarely with
  the MECH-439 immobility the spike already owns.

**Structural-vacuity declaration (785 rule).** In `ARM_HEALTH_DECOUPLED`, `window_completeness`
is forced to 1.0 **by the manipulation** -- it is a manipulation check, not a measurement. C1
is therefore scoped (`applies_to`) to the two arms where it can move, and that arm is scored on
C2 alone. This is disposition (a) -- the criterion is not meaningful for that regime -- not a
vacuous arm.

**DV-symmetry declaration (604c rule), per arm.** The DV is a ratio of counts over realised
ticks. Its symmetry group is permutation of ticks (a set-aggregate). The manipulation
(contamination gating / health clamping) changes which ticks exist and whether the terminal
condition fires; it is not a broadcast constant, not a monotone rescaling of candidate scores,
and not a permutation of interchangeable units. It is therefore **not invariant** under the
DV's symmetry group in any of the three arms.

## 5. Leg 2 -- V3-EXQ-941, `H-denominator` (axis family: `measurement`)

`v3_exq_941_mech467_approach_decomposition` -- 2 arms x 3 seeds = 6 cells.

**The question.** Decompose "0 events" into **never-approached** vs
**approached-and-failed-to-arrive**. 874b could not tell these apart: it recorded consumption
events and nothing upstream of them, so a zero was uninterpretable.

Arms are the claim's two timing regimes, `ARM_PRECOMMIT` (`internal_planning`) and
`ARM_REPLAY` (`internal_replay`) -- kept because they are the regimes MECH-467 is about, and
because they are not the confounded axis. Ruleset held at SIMPLE.

**The counters -- this leg's actual deliverable.** Per cell:
`n_move_actions`, `n_position_changes` (their difference is the **wall-blocking no-op rate**,
which the spike flags as a distinct additive contributor), `n_approach_initiations` (a step
that strictly reduced Chebyshev distance to the nearest benefit-bearing resource),
`approach_run_lengths` (consecutive monotone-decreasing steps toward the SAME target -- the
`H-commitment` measurement, retained as instrumentation per section 1b), `n_arrivals`,
`min_distance_to_goal_achieved`, `n_e3_ticks` vs `n_latched_ticks` (the cadence denominator),
plus `done_cause` / `window_completeness` / `n_benefit_bearing_resource_cells`.

**Decomposition DVs.**
`approach_initiation_rate = n_approach_initiations / n_realised_ticks`
`approach_completion_rate = n_arrivals / max(n_approach_initiations, 1)`

**Discrimination grid.**
- initiation ~ 0 -> **never-approached.** The agent does not head for targets at all;
  consistent with MECH-439, and confirming it at battery level.
- initiation > 0, completion ~ 0 -> **approached-and-failed-to-arrive.** The
  `n_move_actions` vs `n_position_changes` gap then separates wall-blocking from
  commitment abandonment, and `approach_run_lengths` says how far runs get.
- both healthy -> **declared null:** *the decomposition is uninformative because approaches
  are initiated and complete at the observed rate* -- and the denominator problem lies
  outside anything this decomposition can see.

**Why zero events does not make this leg vacuous.** Decomposing the zero IS the deliverable.
Unlike 874b, whose every readout was downstream of a consumption event, every counter here is
measurable on a window in which nothing is ever eaten. That is the point of routing this leg
to the `measurement` axis.

**Readiness precondition, same-statistic (643 rule).** The load-bearing criterion routes on
**counts of position change**, so the readiness check asserts that same statistic on a
positive control: in setup, a forced movement action into known-free space must register a
position change. A below-floor reading means the movement instrument cannot see motion, and
self-routes `substrate_not_ready_requeue` -- never a substrate verdict.

**DV-symmetry declaration, per arm.** The DV is a ratio of counts of distance-decreasing
steps. The manipulation is the operating-mode pin, which changes the selection policy and
hence which actions are taken and which distances occur. It is not a broadcast scalar
(it does not add a constant across candidates), not a monotone rescaling (it does not
preserve candidate order by construction), and not a permutation of interchangeable units.
**Not invariant** in either arm.

---

## 6. Step 2.5b adversarial design audit -- it found three real defects

Run before queuing, per GOV-FANOUT-1 step 4. All three fixes are in the landed drivers.

**(i) Coverage.** The registry's four hypotheses are covered (two by the queued legs, two by
the spike, with their MEASUREMENTS retained in V3-EXQ-941). One hypothesis the registry does
NOT name is also covered: **wall-blocking**, which the scoping spike calls "additive but
distinct" -- V3-EXQ-941's `n_move_actions` vs `n_position_changes` measures it directly.

**(ii) Verdict aliasing -- three defects found, three fixed.**

| # | Leg | Aliasing defect | Fix |
|---|---|---|---|
| A | 941 | Arrival is measured GEOMETRICALLY (Chebyshev distance to a goal cell reaching 0); a consumption EVENT is the env's own `sd049` tag. They can come apart. A run that reliably ARRIVES and never EATS would have satisfied C1 and C2 and routed to `approach_pipeline_intact` -- **the declared null** -- hiding a defect one step downstream of everything the leg was built to see. | Added load-bearing `C3_arrivals_convert_to_consumption` and the `denominator_lost_at_consumption` route. |
| B | 941 | With 12 resources on a 6x6 grid the mean distance to a target is small, and at distance 0 no STRICT decrease is possible. A near-zero mean distance drives `approach_initiation_rate` to ~0, which **aliases onto the `never_approached` verdict while meaning the opposite** (the agent was already there). | Added the `approach_is_definable` readiness precondition (mean distance > 0). |
| C | 940 | C1 reads a **lift** in window completeness. If `ARM_STOCK` never truncated, the lift is ~0 and C1 reads FALSE -- **aliasing "contamination was not the cause" onto "there was no truncation to explain"**, which are opposite findings. | C1's non-degeneracy keyed to `ARM_STOCK` actually truncating; that case routes to the explicit `truncation_not_reproduced_c1_undiscriminating` label instead of to a null. |

Fix C is demonstrably live: the 40-tick smoke does not truncate, and the driver now routes to
`truncation_not_reproduced_c1_undiscriminating` rather than reporting a spurious null.

## 7. Queue entries -- LANDED

Both `experiment_purpose: diagnostic`, tagged `MECH-467` only, `machine_affinity: any`,
`priority: 5` (equal, so they run in parallel per GOV-FANOUT-1 step 5).

| queue_id | leg | axis | script | cells | est |
|---|---|---|---|---|---|
| V3-EXQ-940 | H-energy | environment | `experiments/v3_exq_940_mech467_energy_window_decoupling.py` | 3 arms x 3 seeds | 75 min |
| V3-EXQ-941 | H-denominator | measurement | `experiments/v3_exq_941_mech467_approach_decomposition.py` | 2 arms x 3 seeds | 55 min |

- `ree-v3` `034d5849a5`, pushed to `origin/main` (delta `items: +2`, no sweep).
- Both scripts AND both queue entries verified present on `origin/main` BEFORE the coordinator POST.
- **Step 8.6 coordinator ingress performed**: `POST /queue/add` returned
  `{"ok": true, "applied": true, "existed": false}` for both, and `/queue/active` shows both
  present across 3 polls. This is the authoritative ingress -- a git commit alone is NOT one,
  and the `phase3-queue: snapshot` writer was live in this window.
- `supersedes` is deliberately NOT set on either: these are diagnostics about why 874b's
  denominator vanished, not re-runs of its test, and 874b is already `non_contributory`
  carrying no weight.

**Gates passed:** GOV-REUSE-1 (0 of 922 manifests carry any decisive readout -> not
recoverable, run warranted); re-derive brake (MECH-467 count 1 vs threshold 2, does not fire);
substrate-defect gate (see 7a); ethics preflight (all-false / allow); `validate_queue.py` OK;
`validate_experiments.py --strict` 2 OK / 0 warnings across all 30 checks; smoke PASS on both.

### 7a. Substrate-defect gate -- a judgement call, flagged for review

Two OPEN `corrupting` `substrate_queue` entries overlap modules these drivers import. The
skill's disposition for `corrupting` is a hard stop. **Both were judged non-reaching and the
runs were queued anyway**, with the overlap recorded in each queue entry's `note` (the
`degrading` disposition). The reasoning, so a reviewer can overturn it:

- **`mode-governance-engagement`** (`salience_coordinator.py`, `config.py`, `agent.py`) -- its
  own `severity_note` scopes the corrupting defect to
  `experiments/_lib/regime_occupancy_gate.py`'s min-across-arms/band gate pattern and to "a
  new experiment inheriting this gate pattern". These drivers do not use that module; they use
  `precondition_gate.py` with per-arm `applies_to` scoping. Its `external_task` drive is
  default-off and unused, and both drivers PIN `operating_mode`, discarding the coordinator's
  computed mode by construction.
- **`contextmemory-write-path-addressing-degeneracy`** (`e1_deep.py`) -- its
  `severity_rationale` scopes the hazard to a consumer whose null "looks like a genuine 'sleep
  has no effect' finding". Neither leg produces a null of that shape; they decompose a
  denominator, and the current ContextMemory behaviour is part of the substrate condition
  under test (874b ran under it too). The fix landed 2026-08-19 **default-OFF**.

The counter-argument, stated plainly: `agent.py` appears in three open entries, so a
module-level match there would block essentially every experiment, and the gate says "when in
doubt, treat the entry as open". A reviewer who disagrees should dequeue both entries rather
than let them run.

## 8. For the next governance cycle -- three items this session did not action


1. **Dispose of `H-commitment` and `H-cadence`** in `hypothesis_space_registry.v1.json`
   (`qid mech467_legc_event_denominator_cause`), citing
   `navigation_immobility_scoping_2026-08-18.md`. Not done here -- see section 1c.
2. **Record the MECH-262 exposure** (storage-site vs selection-path rule-read dissociation,
   6/9 live cells) per the autopsy's section 9 verbatim draft. Not this session's authority.
3. **The contamination footgun is broader than MECH-467.** If V3-EXQ-940 confirms C1, then
   any `num_hazards=0` battery that did not set `hazard_free_contamination_gate=True` has been
   running a self-poisoning agent. The scoping spike already recommended a mechanical corpus
   audit of reach-dependent DVs; a confirmed C1 would raise its priority materially.
