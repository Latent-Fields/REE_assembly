# Failure autopsy -- V3-EXQ-996 (diagnostic PASS adjudication)

**status: awaiting_human_confirmation** (STAGING MODE -- Step 8 interactive gate NOT held; Step 7c
red-team NOT run here, the parent `/governance` session owns it)

- run_id `v3_exq_996_isef005_phase_gate_live_channels_20260904T062128Z_v3`
- queue_id **V3-EXQ-996**, `supersedes` / `redesign_of` **V3-EXQ-591h**
- generated_utc `2026-09-04T14:20:27Z` | session `governance-20260904-1347`
- outcome **PASS**, `experiment_purpose: diagnostic`, `claim_ids: []`,
  `evidence_direction: non_contributory` (manifest's own)
- self-route label `crossing_count_gate_discriminates_live_closed_loop`
- bears_on **`["ARC-046", "infant_substrate:GAP-14"]`**

Facts reconstruction, all per-seed/per-arm tables, the six probe scripts and their raw output are in
`facts_V3-EXQ-996.md` in this directory. This document is the adjudication.

---

## 1. Verdict in one paragraph

V3-EXQ-996 is a **genuine advance over V3-EXQ-591h whose self-route label overstates what it shows**.
It DOES close the vacuity that made 591h uninterpretable: 591h's two arms were bit-identical on
`per_episode_h_pos` across 5/5 seeds, 996 measures **135 diverging episodes on 4/5 seeds**, and
independent probing confirms the divergence is caused by the curriculum's own `env_kwargs()` rather
than by an RNG or layout shift. It does NOT establish that the crossing-count gate *discriminates*.
The honest reading is: **the crossing-count gate is strictly MORE CONSERVATIVE than the legacy spike
gate in a live closed loop, and on this 5-seed draw the single seed it additionally withholds happens
to be the one the oracle calls non-genuine -- n = 1, decided by one crossing, at zero precondition
margin.** No decision flips: the node this re-validates (`infant_substrate:GAP-14-c2`) has been
`done` since 2026-06-23. Routing is **implement-substrate** on a newly-found, separate substrate
defect; a 996 successor is **refused**.

---

## 2. Facts (Step 2) -- the load-bearing numbers, recomputed

Dry-run gate: target `dry_run: false`; `check_dry_run_citations.py` over every run_id cited here
(996, 591h, 591f) returns **3 clean, 0 dry, 0 ambiguous**. Recording provenance:
`validate_recording.py` -> **OK, 0 always-core gaps, 0 thin-pack drops**.

| seed | pre-window mean h_pos | pre-window crossings | oracle | SPIKE advance | CROSSING advance | CROSSING count | diverging eps |
|---|---|---|---|---|---|---|---|
| 42 | 0.5804 | 25 | genuine | ep 104 | ep 116 | 3 | 47 |
| 43 | 0.3197 | 8 | genuine | ep 114 | ep 138 | 3 | 26 |
| 44 | 0.6325 | 28 | genuine | ep 100 | ep 106 | 3 | 59 |
| 45 | 0.0959 | 2 | NON-genuine | ep 137 | **never** | **2** | 3 |
| 46 | 0.0453 | 0 | NON-genuine | never | never | 0 | 0 |

All six preconditions MET; `readiness_gate_green: true`; no dropout bypass; zero missing-telemetry
episodes. Both load-bearing criteria pass and all three `criteria_non_degenerate` are true.

---

## 3. Did the PASS hold for a real reason? (adjudication question 1)

### 3a. The non-vacuity guard is REAL -- and correctly attributed

P6 (`raw_trajectory_divergence_present`, measured 135 vs floor 1) is the guard the 591h autopsy
prescribed, and it fires on genuine data. I verified the attribution rather than accepting it:

- **`probe_channel_reach.py`** -- phase-0 vs phase-1 env under an **identical 200-action stream**,
  3 seeds: `harm_signal` differs on **182 / 172 / 166 of 200** ticks, `pos_entropy` on **185 / 164 /
  184**. The manipulation reaches behaviour.
- **`probe_layout_rng.py`** -- initial hazard / resource / agent layouts are **identical** between
  phase-0 and phase-1 at the same seed, and identical under either sub-flag alone. So the divergence
  is dynamics, **not** an env-construction RNG or layout shift -- which is exactly the confound the
  driver's own docstring worried about for the *other* (unwired) channel.

That is a real result and it discharges the 591h vacuity finding. Credit where due.

### 3b. But the crossing-count DV is read on a path that is only HALF live

`n_harm_gradient_ticks = 0` in **all ten cells**, including ARM_SPIKE seeds that spent 55 / 45 / 59 /
22 episodes in Phase 1 with `harm_gradient_enabled=True`. The run added this counter *specifically*
as red-team fix F3 -- "a direct behavioural confirmation that channel (a) engaged, not merely that it
was wired" -- and then nothing read it. The queue entry states the channel was **"verified firing live
in the final script via a diagnostic tick counter"**; the run's own manifest says 0.

I traced why, because a zero from a detector that cannot fire is vacuous, not negative:

- `causal_grid_world.py:2617` gates the harm-gradient reward on `transition_type == "none"`.
- `causal_grid_world.py:2592` -- the `hazard_approach` branch, gated on
  `self.use_proxy_fields and transition_type == "none"` -- fires whenever the hazard proximity FIELD
  at the agent's cell clears `proximity_approach_threshold`, i.e. **on exactly the near-hazard ticks
  the gradient branch exists for**, and sets `transition_type` first.
- `CausalGridWorldV2` (`:5373`) is a factory that **always** sets `use_proxy_fields=True`.

Measured (`probe_harm_gradient_reach.py`, random policy, phase-1 kwargs, 600 ticks):
`{none: 61, hazard_approach: 502, resource: 16, agent_caused_hazard: 9, env_caused_hazard: 12}`,
**`harm_gradient` 0/600**, `harm_gradient_reward_this_tick` nonzero on **0/600**.

And the decisive isolation (`probe_first_divergence.py`, 2 seeds):

| sub-channel enabled alone | first divergent tick | differing harm_signal ticks |
|---|---|---|
| full phase-1 kwargs | 10 / 6 | 182 / 166 |
| **`harm_gradient_enabled` only** | **none** | **0 / 200** |
| **`transient_benefit_enabled` only** | 10 / 6 (same) | 182 / 166 (same) |

**`transient_benefit` alone reproduces the entire phase-1 divergence; `harm_gradient` alone produces
none.** So the ARC-046 mechanistic story the driver docstring and the queue entry foreground -- 
`harm_gradient_enabled -> update_residue() -> ResidueField.accumulate() -> ARC-046 hazard-avoidance
term in E3 trajectory scoring` -- **was not exercised**. The live channel is real; the *account* of it
is half wrong.

This is a **new substrate finding**, not a driver error: V3-EXQ-576, which validated
`harm_gradient` (838/5895, 814/5823, 691/5987 fires), ran with `use_proxy_fields=False` **explicitly**
-- the only mode in which the branch is reachable. The interaction has been unexercised since
2026-05-16 while `substrate_queue` entry `INF-ENV-001`'s own title advertises the feature as being
"in CausalGridWorldV2". See routing.

### 3c. Is the oracle circular?

**Not by window -- but not independent either, and the earlier autopsy already said so.**

The run's headline red-team fix (F2) moved the oracle from `h_pos_mean_full_run` to
`h_pos_mean_pre_ep_min` on ARM_SPIKE, over episodes `[0, 100)`, which is **provably arm-invariant**
(`PHASE_EP_MIN[1] = 100` forbids any advance before ep 100, and the manifest confirms
`h_pos_mean_pre_ep_min` is identical between arms on every seed). The gate's own count runs over
`[100, 160)`. The windows are disjoint. That much is a real improvement over 591h and removes the
post-advance contamination 591h had.

But the 591h autopsy's learning #3 asked for an oracle **"computed from a signal the gate does not
read"**, and 996 changed the WINDOW, not the SIGNAL -- both are still read-outs of `h_pos`. Recomputed
from the manifest's own cells:

```
ORACLE       (pre-window mean h_pos >= 0.20)  = [T, T, T, F, F]
PRE-WINDOW crossing rule (crossings >= 3)     = [T, T, T, F, F]   <- identical
```

on the vector `[25, 8, 28, 2, 0]`. **This is the same reproduction, on the same vector, that the
confirmed 591h autopsy already recorded** (`"n_pre_ep_min_crossings >= 3, i.e. [25,8,28,2,0],
reproduces the oracle exactly"`), together with its learning #4: *"A partition already determined
before the decision window opens cannot be evidence about a decision rule applied inside that
window."* By defining the oracle **on** `[0, 100)`, 996 makes that objection explicit rather than
answering it. The partition is a stable per-seed property; both read-outs recover it; their agreement
measures threshold monotonicity, not the gate's competence.

Step 7b's **C7** fired on exactly this metric, independently and mechanically (see section 6).

### 3d. Is the readiness gate load-bearing?

Two of the six preconditions are weak in a way worth recording:

- **P2 `crossing_counts_reach_gate_minimum` is arithmetically pinned.**
  `_try_phase_0_to_1` returns early once `current_phase != 0`, so `scheduler_crossing_count` stops
  incrementing at advance and an advancing seed reads **exactly 3**. "MAX over seeds >= 3" is
  therefore logically equivalent to "at least one ARM_CROSSING seed advanced", and it reads at its
  floor in every advancing cell. It also **cannot distinguish "the gate is starved" from "the gate is
  maximally conservative and correctly rejected every seed"** -- both read below floor and both
  self-route `substrate_not_ready_requeue`. The refutation surface is asymmetric.
- **P5 `live_false_advancer_present` sits at zero margin** (measured 1, threshold 1) -- the same
  zero-margin condition the 591h autopsy flagged, unchanged.

---

## 4. "Discriminates" or "more conservative"? (adjudication question 2)

**More conservative.** The structure settles it from the run's own cells:

- **The admitted sets are strictly nested.** SPIKE admits `{42, 43, 44, 45}`; CROSSING admits
  `{42, 43, 44}`. **There is no seed the crossing gate admits and the spike gate refuses.**
- **The crossing gate advances LATER on every co-admitted seed**: 104 -> 116, 114 -> 138, 100 -> 106.
- Agreement with the oracle: **SPIKE 4/5, CROSSING 5/5.** The whole delta is **seed 45**.
- Seed 45's decision turns on **one crossing**: the crossing arm counts 2 against a threshold of 3,
  while the spike arm reads exactly 3 on the same seed. The 1-count gap arises from the arms' own
  3-episode divergence -- the thinnest possible margin.
- Seed 46 is a **trivially agreeing** cell: it never crosses the spike bar at all
  (`h_pos_max 0.741 < 0.994`), so both gates reject and the oracle agrees with both.

So 4 of 5 cells are cells where the CONTROL gate is also correct. **The effective n for the
discrimination claim is 1**, and 591h's own measured delta was likewise exactly one seed -- a defect
its autopsy named and this run did not address.

### Which pre-registered hypothesis does this map to?

The driver carries **no `=== HYPOTHESES UNDER TEST ===` / `=== INTERPRETATION GRID ===` block**
(grep count 0; sections present are QUESTION / DESIGN / ACCEPTANCE / DV-SYMMETRY / SCOPE LIMITATION /
RED-TEAM VERDICT). Its de facto grid is the four-branch label ladder at lines 849-862:
`substrate_not_ready_requeue` (x3 routes) -> `crossing_count_gate_discriminates_live_closed_loop` ->
`..._self_defeating_holds_back_genuine_explorers` -> `..._discrimination_lost_in_closed_loop`.

The result maps to the third branch **only because the ladder has no "more conservative, delta = one
seed" rung**. `ACCEPTANCE` states the criterion as "for EVERY seed, the live phase-advance decision
agrees with the ORACLE label" -- an agreement criterion, not a discrimination criterion. It was met.
The *label attached to meeting it* is what overstates.

---

## 5. Does anything change? (adjudication questions 3 and 4)

**Nothing unblocks. Nothing is licensed. No successor is owed.**

- **`infant_substrate:GAP-14-c2`** ("Phase 0->1 gate over-permissiveness") has status **`done` since
  2026-06-23**: the criterion was identified by V3-EXQ-591f (PASS, 2026-06-15) and **wired into
  `InfantCurriculumScheduler` on 2026-06-19**. **996 re-validates an already-closed node in a live
  loop.** That is worth having -- it retires the 591h vacuity -- but it clears nothing.
- **`infant_substrate:GAP-14`** (parent) remains `blocked_pending_substrate`, gated **only on c-1**
  (seed-46 exploration-strength collapse), whose gate was repointed 2026-07-21 to the
  behavioural-competence wall (V3-EXQ-724 `competence_deficit_diffuse`).
  **996's seed 46 reproduces c-1 exactly** (`h_pos_max 0.741` below the 0.994 bar, 0 crossings, 0
  diverging episodes), confirming c-1 is open. **EXQ-ISEF-005 stays blocked.**
- **ARC-019**: 996 is claim-free and bears on it in neither direction. ARC-019 **already carries
  `diagnostic_evidence_adjudicated: true`** (set by this same governance cycle applying the 591h
  autopsy), so a `-> diagnostic_evidence_adjudicated: true` change tail would be **already true** and
  would self-clear its GOV-APPLY-1 row spuriously. **No `per_claim_recommendation` is emitted.** The
  substantive read-across -- the phase channel is now live, but via `transient_benefit` only, with the
  harm-gradient half inert for a *new* reason -- is recorded under `read_across_not_adjudicated`.
- **A 996 successor is REFUSED.** The two residual weaknesses are real, and fixing them would spend
  roughly another 10 machine-hours strengthening a node closed for two and a half months, on a
  question nothing downstream waits on. If it is ever revived it must (a) compute the oracle from a
  signal the gate does not read -- foraging / benefit-contact competence, not `h_pos`; (b) power the
  **discriminating** cells rather than the total seed count; (c) verify a nonzero harm-gradient fire
  count or drop that sub-channel from its account.

**What IS actionable** is the substrate defect section 3b uncovered: an `amend` on `substrate_queue` entry
**`INF-ENV-001`** (which exists, status `implemented`, `failure_record: []`) recording that
`harm_gradient_enabled` is structurally inert under `CausalGridWorldV2` proxy-field mode. Severity
**`degrading`**, deliberately not `corrupting`: nothing measured so far is invalidated (996's own DVs
are sound; 576's PASS stands in the mode it tested), and `corrupting` would arm the
`/queue-experiment` Step 2.5c gate against every new experiment touching `causal_grid_world.py` for a
defect that has invalidated nothing. The proportionate mitigation is the WARN plus a standing
instruction that any experiment enabling `harm_gradient_enabled` must record a per-cell fire count and
treat zero as a **readiness failure, not a measurement**.

`node_class`: **`complicated (buildable)`** -- a named repair with no open question (make the gradient
branch composable with `hazard_approach`, or refuse/warn on the inert combination). Hence
`routing: implement-substrate`.

Two substrate defects the run itself recorded are **already handled and must not be re-routed**:
`REEAgent.offline_integration()`'s `torch.cat` `dim=0` bug is **GFLAG-0130, FIXED** in ree-v3
`2b345217c7` (2026-09-03) with contract `tests/contracts/test_offline_integration_cat_dim.py`;
`ResidueField.integrate()` training nothing is recorded and carried as a read-across, not adjudicated.

---

## 6. Step 7b fires and disposition

`autopsy_pre_routing_checks.py --artifact <draft>.json --json` -> **fire_count 1** (one check, naming
two metrics).

- **C7 -- ACT ON, not dismissed.** *"2 metric(s) named in this artifact vary across seeds but are
  BIT-IDENTICAL across every arm in every seed ... `h_pos_mean_pre_ep_min`, `n_pre_ep_min_crossings`"*.
  This is independent, mechanical corroboration of section 3c, reached without reading the substrate,
  and it names the ORACLE STATISTIC ITSELF. Read carefully, because the arm-invariance is not itself
  the defect: it is guaranteed by `PHASE_EP_MIN[1] = 100`, and it is precisely what makes the oracle
  UNCONTAMINATED -- the whole point of red-team fix F2. The defect is the CONJUNCTION -- the oracle is
  computed on a window in which the arms cannot differ, and that same arm-invariant window already
  reproduces the partition exactly (`n_pre_ep_min_crossings >= 3` gives the identical labels), so the
  oracle cannot be evidence about a decision rule applied after episode 100. Acted on: it is the basis
  of the measurement finding, of the `not_established` measures bucket, and of requirement (a) on any
  revived successor.
- **C1 / C2 / C3 -- `inapplicable`, and `inapplicable` is NOT "no fire".** All three are claim-keyed
  and this target carries `claim_ids: []`, so they were structurally unable to look. A quiet report
  from them means nothing here; **Step 7c carries the whole load on this artifact**, and the parent
  `/governance` session runs it.
- **C5 -- inapplicable on the first pass** (no sibling `.md` existed at check time); re-run after this
  document was written, and recorded in the final line of section 7.

---

## 7. Four-layer diagnosis and failure location

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | `claim_ids: []` by design; the 591h ARC-019 tag was removed by this governance cycle |
| Biological reference | clear | competence-gated stage transitions are well-evidenced; not what is at issue |
| Prerequisites | **partial** | `env_kwargs()` applied as prescribed, but only `transient_benefit` is operative; the second prescribed channel (`offline_integration_frequency`) is unwired for documented, defensible reasons |
| Implementation | **partial** | `harm_gradient_enabled` structurally inert in proxy-field mode (0/10 cells, 0/600 probe ticks, 0/200 divergence) |
| Environment | adequate | real seed spread, both classes present, 135 diverging episodes, identical initial layouts |
| Measurement | **under-instrumented / misleading** | non-independent oracle; delta = 1 seed at zero P5 margin; P2 arithmetically pinned; F3 liveness counter reads 0 unflagged |
| Integration | coupled | the arms genuinely interact with the env differently -- the precise defect 591h had and this run fixed |
| Scale | likely insufficient | 5 seeds, 4 of them trivially agreeing; effective n = 1 |

**Failure-location (GOV-FAILLOC-1): MIXED (MECHANISM + MEASURES).**
`mechanism: partial`, `measures: not_established`, `environment: established`, `ree: false`.
**Not chargeable to REE and not a substrate ceiling** -- the environment cleared every readiness anchor
and the manipulation reached behaviour. No organism-level "REE failed" reading is asserted anywhere in
this artifact, and none would be admissible: two of the three buckets are not established.

`recommended_epistemic_category`: **`standard`** (claim-free diagnostic -- asserts no epistemic
suppression, which is the verdict). The failure-mode label
`measurement_test_design_defect over competence_implementation_gap` lives in the notes, not the
category field.

**Step 7b re-run after this `.md` existed: fire_count 1 (C7 only, unchanged); C5 now applicable and
did NOT fire.**

---

## 8. Learning extracted

1. **A precondition computed on the same statistic the outcome routes on can be arithmetically
   pinned rather than informative.** P2 reads the crossing count that *stops incrementing at advance*,
   so an advancing seed reads exactly the threshold. It also aliases "starved" with "maximally
   conservative and correct" -- both self-route `substrate_not_ready_requeue`.
2. **Moving an oracle's WINDOW is not moving its SIGNAL.** The prescription was "an oracle computed
   from a signal the gate does not read"; disjoint windows on the same signal still recover the same
   stable per-seed partition.
3. **When one gate's admitted set is a strict SUBSET of the other's, "agrees 5/5" can carry an
   effective n of 1.** Report the delta over the control and the per-seed decision margin, not the
   agreement count.
4. **A channel-liveness counter is only as good as somebody reading it.** `n_harm_gradient_ticks` was
   added by a red-team pass to confirm engagement, then read 0 in all ten cells while the queue entry
   recorded the channel as "verified firing live". A liveness counter needs a **registered floor that
   self-routes on zero**, exactly as the trajectory-divergence precondition does.
5. **A feature validated in one env mode can be structurally inert in another -- and the validating
   experiment can be the reason nobody noticed.** V3-EXQ-576 validated `harm_gradient` with
   `use_proxy_fields=False`, the only mode in which the branch is reachable, so the proxy-mode
   pre-emption went unexercised for four months while the substrate_queue title advertised the feature
   as being "in CausalGridWorldV2".

---

## 9. Recording-accuracy defects (report to governance; neither blocks adjudication)

1. `metrics.max_post_ep_min_crossings_spike` is **mislabelled**: driver line 902 assigns
   `max_crossings`, computed at line 713 over **ARM_CROSSING**'s `scheduler_crossing_count`, not
   ARM_SPIKE. A leftover key name from 591h, where the statistic genuinely was a post-hoc recount off
   the control arm.
2. Two precondition `control` strings (and one `description`) still say
   `"full-run h_pos_mean measured on ARM_SPIKE"` while the code uses `h_pos_mean_pre_ep_min`. The
   pre-ep_min substitution is this run's own headline red-team fix; its manifest still describes the
   statistic it replaced.
3. The driver carries no `=== HYPOTHESES UNDER TEST ===` / `=== INTERPRETATION GRID ===` block, which
   the skill requires of every diagnostic script. The label ladder serves the purpose but is not
   discoverable as a grid.

---

## 10. Step 9b -- hypothesis-space ledger (DRAFT ONLY, registry NOT written)

No existing `questions[]` entry in `hypothesis_space_registry.v1.json` covers this work-stream (all 45
qids checked). This autopsy adjudicates a leg and emits no fanout, so **Mode B** applies to a **new**
question -- and the growth-restriction check does not, since a question opened in this edit cannot
carry a restriction. The intended entry (`qid: curriculum_phase_gate_live_loop`, 2 hypotheses,
`initial_frozen_count: 2`) is drafted under `hypothesis_space_ledger_pending` in the JSON:

- `H-live-channel-closes-591h-vacuity` -> **confirmed** (`control_passed: true`,
  `non_degenerate: true`, `met_elimination_bar: false`, resolved at the run's own timestamp).
- `H-crossing-gate-discriminates-vs-more-conservative` -> **alive**, with `resolving_runs` and a
  `basis` recorded. **Deliberately not eliminated**: an uninformative run narrows nothing, and its
  adjudicating successor is refused above -- which is recorded here rather than papered over.

The confirming session must verify `axis_families.map` contains both `instrumentation` and `process`
before appending, or the question's `convergence_class` forces to `indeterminate`.

---

## 11. Open question I could not settle

**Is `harm_gradient` reachable at all under `use_proxy_fields=True`, or only vanishingly rarely?**
I established it fires 0/600 under a random policy at phase-1 kwargs and contributes 0/200 divergence,
and I traced the pre-emption mechanism. What I did not settle is whether a narrow band exists (agent
within `harm_gradient_outer_radius = 3.0` but with the hazard proximity field *below*
`proximity_approach_threshold`) in which it can still fire -- which would make the defect
"vanishingly rare" rather than "strictly impossible". That distinction does not change the routing or
the severity, but it does change how the `INF-ENV-001` amend should be worded, and the implementing
session should measure it.


## Red-team pass (Step 7c) and revision -- 2026-09-04T14:49:17Z

**Reviewer:** Fable 5.1 (separate agent, reasoning withheld, JSON-first). **Verdict: CONTESTED. Contest ACCEPTED** by the confirming governance session (governance-20260904-1347). Routing survives; the amend's factual content did not.

- **F1.** `tests/contracts/test_harm_gradient_gap1.py::test_c3_suppressed_by_proxy_approach` (use_proxy_fields=True, landed 2026-05-16 with the feature) already pins that the gradient stays zero when proxy approach fires. The draft's "contract covers proxy=False only" and "never exercised" are withdrawn. The inertness was designed in; letting the gradient fire under proxy mode would break a pinned contract, so it is a design decision owed to the user, not a `complicated (buildable)` bug fix.
- **F2.** V3-EXQ-587 (ISEF-001, V2 mode, 2026-05-19: C1 0/5, ratios ~1.0) first measured the inertness and was read as a "null on geometry"; `infant_substrate:GAP-10` is `done`, stamped at queue time. The amend now names 587 as the first measurement and records the owed GAP-10 reconcile.
- **F3 (settles section 11's open question).** Structural at DEFAULT V2 parameters -- the approach band (Manhattan <= 11 at threshold 0.15, decay 0.5) strictly contains the gradient band (Euclid <= 3.0); 0/4000 fires -- but REACHABLE when `proximity_approach_threshold` exceeds ~0.33 (0.9 -> 24/2000). Wording qualified accordingly.
- **Survived:** every recomputed cell (135 diverging episodes 47/26/59/3/0; oracle partition reproduced by pre-window crossings on [25,8,28,2,0]; nested admitted sets; delta = seed 45 at zero P5 margin; P2 pinned; 0 harm_gradient ticks 10/10); the non-vacuity guard (private env RNG, identical layouts); "strictly more conservative, n = 1"; INF-ENV-001 as the amend target; severity `degrading`; the successor refusal.
- **Hygiene:** line numbers cited from the working tree (:2592/:5373) rather than commit 8f88b89 (:2507/:5231); DEV-NEED-004 absent from claims.yaml; stale `live:` blocks on GAP-10/14 citing an unrelated cluster autopsy.

Withdrawn amend text retained under `withdrawn_readings_2026_09_04` in the JSON.


## Confirmation -- 2026-09-04T18:55:13Z

Status **confirmed** at the /governance Step 8 gate (session governance-20260904-1347, user present). Decisions: {"Q1": "Apply all four as revised", "Q2_SD031_gate": "Amend SD-031 what_would_answer + self_attribution GAP-6 to accept construction-balanced (RandomPolicy, offline-scored) comparator-only designs for the ARC-065 diversity half", "Q3": "Add 6 buildable v3 substrate stubs", "Q4": "Apply the three August staging-autopsy ledger blocks now", "recommendation_agreement": "3 of 4 recommended options selected (Q4 against); logged via record_recommendation_outcome.py"}
