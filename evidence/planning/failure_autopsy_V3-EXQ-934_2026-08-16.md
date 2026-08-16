# Failure autopsy -- V3-EXQ-934 (MECH-266 / SD-032a)

- **Generated (UTC):** 2026-08-16T18:26:35Z
- **Status:** `awaiting_human_confirmation` (STAGING MODE -- Step 8 interactive gate not run; routing drafted, not finalised)
- **Scope:** single
- **Target run_id:** `v3_exq_934_mech266_cap_sweep_mode_occupancy_20260815T015216Z_v3`
- **Queue id:** V3-EXQ-934 | **outcome:** PASS | **experiment_purpose:** `diagnostic`
- **Self-route label:** `cap_recalibration_admits_mixed_regime`
- **Claims tagged:** MECH-266, SD-032a
- **Trigger:** `experiment_purpose: "diagnostic"` -- a clean, UNFLAGGED diagnostic PASS still
  requires this autopsy (2026-08-07 user-instructed correction). The run appears in
  `pending_review.md` under "Diagnostic -- autopsy required (no confirmed adjudication)",
  NOT under "Diagnostic adjudication required" (no `vacuous_pass` / `precondition_unmet` flag).

---

## 0. Gates run before any metric was read

**Already-done check (by CONTENT, not filename glob).** Every
`evidence/planning/failure_autopsy_*.json` was parsed and its `targets[].run_id` compared
against this run_id. **No coverage.** (A filename glob would not have been sufficient: the
neighbouring MECH-267 work is filed as `failure_autopsy_927-928-mech267-cluster_2026-08-16`,
invisible to a `failure_autopsy_V3-EXQ-927*` glob.)

**Dry-run gate (Step 2a).**

```
scripts/check_dry_run_citations.py v3_exq_934_mech266_cap_sweep_mode_occupancy_20260815T015216Z_v3
-- 0 dry cited, 0 dry in named families, 0 ambiguous, 1 clean, 0 unknown   (exit 0)
```

Manifest top-level `dry_run` is absent/null. **The target is a real run.** No dry runs are
cited anywhere in this autopsy; `excluded_dry_run_ids: []`.

**Recording provenance (Step 2b).** `ree-v3/validate_recording.py` -> `OK`, 1 complete,
0 always-core gaps, 0 thin-pack drops, 0 schema warnings. `substrate_hash`
`f53db12dd0a7e00dcf351e3ba024c861173ac53d435d507d493288f8f138ddeb`; `substrate_commit`
`6f46a703cbcd1e6badfef24d46a9c75ce5d0b177`, `dirty: false`, branch `main`;
`substrate_stable_across_run: true`, `lag_seconds: 0`. `machine` `ree-worker-3`,
`machine_class` `linux-x86_64-py3.10-torch2.12.0+cpu`, `elapsed_seconds` 23800.9,
`seeds` [42, 43, 44]. **One recording gap, minor but on-point** -- see section 8, item 6.

**z_goal stream.** `writer_calls` 5262, `ticks_active` 173441 / 173444
(`active_frac` 0.99998), `writer_defect: false`, `goal_state_present: true`, 33 agents.
Live; no z_goal defect.

---

## 1. Facts -- what the run actually did

**Design.** Train ONE scaffolded-curriculum agent per seed (603n config: stage0 20 /
stage0b 10 / P0 100 / hazard 40 / P1 50 / P2 15 episodes, 3 resource types), holding
`salience_affinity_input_cap = 2.0` at TRAIN time. Then, at EVAL time, clone that agent and
override `coord.config.affinity_input_cap` across `CAP_SWEEP = [0.75, 1.0, 1.25, 1.5, 1.75]`
(read live at `SalienceCoordinator.tick()`, so no retraining). Two arms:

- **`ARM_SYMMETRIC`** -- legacy MECH-259, no per-mode rails. **PRIMARY** for the H1 verdict.
- **`ARM_ASYM_STICKY_TASK`** -- MECH-266 sticky exit rail (`sticky_exit = 0.05`). Reported as
  context, explicitly **not load-bearing** (the driver says so).

10 cells per seed (5 caps x 2 arms), 15 episodes per cell.

**Preconditions (both `met: true`).** Both are genuinely MEASURED quantities, not constants
that cannot fail -- but they differ sharply in how binding they are:

| Precondition | Statistic | Measured | Threshold | Headroom |
|---|---|---|---|---|
| `foraging_contact_guard` | fraction of seeds with P2 `contact_rate > 0` AND `z_goal_norm_at_contact_peak > 0.4` | 1.0 (3/3) | 0.667 | z_goal peaks 0.4920 / 0.4330 / 0.4414 vs a 0.4 gate -- **8-23% above**, genuinely capable of failing |
| `external_task_drive_engages` | fraction of guard-passing seeds whose best cell's `ext_margin_mean > 0.05` | 1.0 (3/3) | 0.667 | max margins 0.3373 / 0.7705 / 0.7850 vs a 0.05 floor -- **7-16x**, effectively non-binding |

Per-seed P2 contact rates 0.2515 / 0.2570 / 0.3064; 107 contact events on seed 42. Both
preconditions are real measurements. The **contact guard discriminates**; the **margin guard
is a liveness check with 7-16x headroom and should not be read as a strong control** -- it can
only fail on a dead drive, which is exactly what the driver says it is for.

**The single load-bearing criterion.**

```
H1_symmetric_arm_graded_regime_reachable   load_bearing: true   passed: true
criteria_non_degenerate.H1_symmetric_arm_graded_regime_reachable: true
```

Its definition, from the driver and `interpretation.regime_gate`:

> per (seed, arm), build one `OccupancyCell` per cap; `regime_shape` is `graded` iff
> **at least one cap** yields `fraction_in_external_task` strictly in (0.1, 0.9).
> H1 supported iff `ARM_SYMMETRIC` is `graded` on **>= 2/3** guard-passing seeds.

**Measured: `sym_graded_fraction = 0.6667` -- exactly the 2/3 minimum, 2 of 3 seeds.**

**The primary-arm data in full (`fraction_in_external_task`, ARM_SYMMETRIC):**

| seed | cap 0.75 | cap 1.0 | cap 1.25 | cap 1.5 | cap 1.75 | mixed caps | `sym_graded` |
|---|---|---|---|---|---|---|---|
| 42 | **0.5606** | 0.0317 | 0.0 | 0.0 | 0.0 | {0.75} | true |
| 43 | 1.0 | 1.0 | 1.0 | 1.0 | **0.4447** | {1.75} | true |
| 44 | 1.0 | 1.0 | 1.0 | 1.0 | 0.9002 | {} | **false** |

**Read the columns, not the rows.** Per-cap, across seeds, the count in the mixed band is:

| cap | 0.75 | 1.0 | 1.25 | 1.5 | 1.75 |
|---|---|---|---|---|---|
| seeds graded | **1/3** | 0/3 | 0/3 | 0/3 | **1/3** |

**No single cap value grades on more than one of three seeds.** The manifest's
`winning_cap_band_symmetric = [0.75, 1.75]` is the min and max of two **disjoint singletons at
opposite ends of the swept range** -- it is not a band and there is nothing contiguous inside
it. Seed 44 never grades: its minimum is 0.9002 against a 0.9 ceiling, missing by 0.0002.

**Continuous margin (`ext_margin_mean`, ARM_SYMMETRIC) falls monotonically with cap in every
seed:** seed 42 0.3373 -> 0.3038 -> 0.2653 -> 0.2359 -> 0.1997; seed 43 0.7681 -> 0.7392 ->
0.6370 -> 0.5620 -> 0.4852; seed 44 0.7850 -> 0.7581 -> 0.7142 -> 0.6411 -> 0.5732. The cap
manipulation lands and is monotone; **the seeds differ by roughly 2.3x in the LEVEL of that
margin** (seed 42 ~0.20-0.34, seeds 43/44 ~0.49-0.79), which is what moves the crossing.

**The mixed cells are genuinely non-degenerate.** seed 42 @ 0.75: 19 switches, 24
external_task runs over 15 episodes, mode-conditioned `ext_dwell_mean` 43.2 steps, 1022 /
1823 steps external. seed 43 @ 1.75: 18 switches, 22 runs, `ext_dwell_mean` 53.5, 1161 / 2611
steps. Real alternation, not a per-episode settle.

**The manipulation arm is saturated everywhere.** `ARM_ASYM_STICKY_TASK` reads
`fraction_in_external_task = 1.0` with `n_switches = 0` in **all 15 cells** (3 seeds x 5 caps).
This is the intended effect of a sticky exit rail, and it is why the arm is not load-bearing --
but it also means the arm carries **zero information about a MECH-266 dose-response**.

**Manifest's own directions.** `evidence_direction: non_contributory`;
`evidence_direction_per_claim`: MECH-266 `non_contributory`, SD-032a `supports`. The driver
pre-declared that mapping.

---

## 2. Does the label overstate what the criterion establishes? -- **YES, on three counts**

The self-routed label is `cap_recalibration_admits_mixed_regime`. The skill's standing rule is
that a self-route is a hypothesis, never a verdict. Here it overstates in three independent
ways.

### 2a. "recalibration" implies a settable value. There is none.

A recalibration is something you can ship: one cap value the system runs at. The criterion is an
**existential over the cap grid evaluated PER SEED**, then a fraction over seeds. That is
satisfied by three seeds each having their own private winning cap -- and that is precisely what
happened, with the two winners at **opposite ends** of the swept range (0.75 vs 1.75, a factor of
2.33 apart) and the third seed having none. Under a criterion that required a *common* cap, the
run reads **1/3 at best, at every cap** -- a clean FAIL of the same 2/3 bar.

### 2b. "mixed regime" implies a regime. What exists is a knife-edge crossing.

In every seed that graded, the mixed band is **at most one grid step (0.25 cap units) wide**:
seed 42 goes 0.5606 -> 0.0317 across a single step; seed 43 goes 1.0 -> 0.4447 across a single
step (and the training cap 2.0, one further step up, is not sampled). Seed 44's crossing sits at
or above the top of the grid.

This is the load-bearing methodological point: **a "some grid point lands in (0.1, 0.9)"
predicate on a 5-point grid detects a CROSSING, not GRADEDNESS.** Any monotone switching
function -- however steep, including a near-step function -- will place a grid point inside the
band once the grid is fine enough relative to the crossing width. The criterion's pass
probability is therefore a function of grid density, not of the arbitration's smoothness. **It
cannot discriminate H1 (graded arbitration reachable by recalibration) from H2 (structurally
bang-bang with a narrow crossing) -- which is exactly the discrimination the GOV-FANOUT-1
portfolio was opened to make.** H2 is not eliminated by this run and must not be recorded as
such.

### 2c. The mechanism says most of the sweep never touched the drive at all

`SalienceCoordinator.tick()` (`ree_core/cingulate/salience_coordinator.py:455-465`) applies
`value = max(-cap, min(cap, value))` to **every** affinity input before per-mode weighting. But
the `external_task_drive` signal is already bounded to [0, 1] by construction
(`ree_core/agent.py:6958`: `_et_engagement = max(0.0, min(1.0, _et_commit + _et_prox))`).

**Therefore the clamp is a NO-OP on `external_task_drive` at every cap >= 1.0.** Only
cap = 0.75 actually clamps it. At caps 1.0 / 1.25 / 1.5 / 1.75 the sweep is manipulating only
the *competing* unbounded affinity inputs -- canonically `dacc_pe`, whose magnitude the
pre-authoring probe recorded at ~16 -- letting them push `internal_planning`'s logit
progressively harder. The monotone fall of `ext_margin_mean` with cap is the direct signature
of that. So the "graded regime" is the point at which two logits cross, slid past each other by
loosening the competitor's clamp. It is a crossing location, not a gradedness property.

**A second, cap-INDEPENDENT discreteness source is present and no cap can grade it.**
`ree_core/agent.py:6944`: `_et_commit = _et_commit_w * (1.0 if self.beta_gate.is_elevated else
0.0)`. The commitment term is a **boolean latch**; at the default `commit_weight = 1.0` the
engagement scalar saturates at exactly 1.0 whenever the latch is on, regardless of the
proximity term. (The `mode-governance-engagement` substrate entry already records this from
the 2026-08-13 synthetic probe: "H1 and H2 are not mutually exclusive as originally framed".)
This run's data is consistent with that and does nothing to separate them.

### The defensible reading

> A mixed `external_task` occupancy is **reachable per seed at a seed-specific cap sitting on
> the argmax crossing**; the mode register alternates genuinely where it does. **No common cap
> operating point was demonstrated in [0.75, 1.75], the crossing is at most one grid step wide,
> and H2 is not eliminated.**

---

## 3. Is the finding conditional on a non-production configuration? -- **YES, twice over**

`enabled_default_off_flags` is **null** in the manifest, so this had to be established from the
substrate rather than the record.

| Knob | Production default | This run |
|---|---|---|
| `REEConfig.salience_affinity_input_cap` | **`None`** = no clamp at all (`config.py:3055`; comment: "None (default) = bit-identical to the pre-2026-08-12 substrate (no clamp; matches every landed V3-EXQ-464/467 manifest)") | 2.0 at train, swept 0.75-1.75 at eval |
| `REEConfig.use_external_task_drive` | **`False`** (opt-in; `agent.py:2393`, `agent.py:6933`; claims.yaml SD-032a governance note: "still default=False / opt-in") | `True` |

So the swept configuration is non-production on **two** independent axes. Worse for the
"recalibration" reading: the driver's own pre-authoring probe recorded
`operating_mode['external_task'] = 0.0` at **cap = None / dacc_pe = 16** -- i.e. at the
production default the external_task signal collapses entirely. The production point is not
merely outside the sweep; it is known to be degenerate.

And the training cap (2.0) is **also outside the swept range**, one grid step above the top.
Nothing here characterises the configuration the agent was trained under, nor the one a
default REEConfig would run.

**This is the same production-inertness hazard as the neighbouring MECH-267 cluster**
(`failure_autopsy_927-928-mech267-cluster_2026-08-16` section 5: "the validated fix is a no-op
by default"; `mode_partitioned_cem` / `mode_value_weight` both default OFF), and the same
standing memory: `reference_claim_status_vs_default_off_flag` -- "claim status != flag default;
check the knob first." **This condition MUST appear in the `evidence_quality_note`**, and it
does (section 9).

The difference from 927/928 is worth stating so the parallel is not over-read: there, the fix
*worked* and was merely un-shipped, so the route was a clean default flip. Here the winning cap
is **seed-idiosyncratic**, so there is no single value to flip a default *to* -- the
production-inertness and the no-common-operating-point findings compound rather than being two
views of one thing.

---

## 4. Claim-layer mapping -- MECH-266 is PERIPHERAL here

### MECH-266 (`salience.asymmetric_mode_hysteresis`, `mechanism_hypothesis`, **provisional**)

Asymmetric (Schmitt-trigger) enter/exit thresholds per mode; over-binding = exit threshold -> 0.
`epistemic_category: standard`, `pending_retest_after_substrate: true`,
`depends_on: [SD-032a, MECH-259, SD-033]`. Lit complete (six entries,
`targeted_review_connectome_mech_266`: Cools 2008, Cools 2019, Cools & D'Esposito 2011,
Collins & Frank 2014 OPAL, O'Reilly 2006, Fallon 2016).

**This run did not exercise MECH-266.** The MECH-266 manipulation is the sticky exit rail, and
`ARM_ASYM_STICKY_TASK` sat at `fraction_in_external_task = 1.0` with `n_switches = 0` in **all
15 cells**. That is the manipulation working as designed and it produces **no dose-response
gradient of any kind**. The driver says so in terms ("NOT load-bearing for H1 -- the sticky rail
deliberately pushes occupancy toward saturation, so a saturated reading there is the intended
manipulation, not evidence against H1"). The load-bearing criterion is evaluated on the
*symmetric* arm, i.e. on the arm with **no MECH-266 mechanism in it at all**.

Per the skill's PERIPHERAL co-tag rule (2026-07-21), a blanket category must not be attributed
to a claim the run did not exercise -- so this autopsy declares
`recommended_epistemic_category_per_claim` explicitly. MECH-266 takes `standard`, and **no
`substrate_ceiling` attribution accrues to it from this run** (its brake count is unchanged at
6; see section 7).

### SD-032a (`cingulate.salience_network_coordinator`, `design_decision`, **stable**)

Discrete `operating_mode` register + `mode_switch_trigger`. `epistemic_category: standard`,
28 supports / 0 weakens, conf 0.928, conflict_ratio 0, `v3_pending: false`.

**A claim-layer point that materially changes how the bang-bang result reads.** SD-032a's own
`functional_restatement` says: *"Mode transitions are discrete, not graded -- though the switch
threshold itself may be graded and learnable."* **Discrete, knife-edge transitions are what
SD-032a asserts.** So the bang-bang arbitration that 464e/467e reported, and the narrow crossing
this run found, are SD-032a **behaving as specified** -- they are not evidence against it, and
the H1-vs-H2 framing ("structural bang-bang" as a *problem*) is really a MECH-266 problem, not
an SD-032a one. What is genuinely unresolved is whether a *contested-occupancy window wide
enough for MECH-266's hysteresis to express* is obtainable on this substrate.

What SD-032a legitimately gains here is narrow and real: at the crossing, the register produced
genuine discrete alternation (18-19 switches, mode-conditioned dwell 43-54 steps) with the
MECH-259 trigger firing, on the built curriculum substrate -- the first time this lineage has
seen the mode register alternate rather than pin at 0.0 or 1.0. `supports`, tightly scoped.

**Conditional-category check (Step 5).** SD-032a's stored `live_status.evidence` cites
`failure_autopsy_SD-034-closure-cluster-ext_2026-06-12#V3-EXQ-467c` with verdict
`non_contributory/substrate_ceiling` as of 2026-06-12, while its `reading` is `stable` as of
2026-07-11. MECH-266's `live_status` was refreshed 2026-08-13 by the 464e/467e cluster. Neither
stored `epistemic_category` (both `standard`) carries a stated re-check condition that this run
satisfies. Nothing stale to trip here.

---

## 5. Biological-reference triage

**Closest reference mechanisms.** For SD-032a: the AIC-dACC coupled salience network switching
between large-scale networks (Menon & Uddin 2010; Craig 2009 AIC account) -- the claim's own
cited basis. For MECH-266: basal-ganglia direct/indirect pathway asymmetry and tonic-DA
hysteresis (Cools 2008; Collins & Frank 2014 OPAL D1/D2 opponency).

**Surrounding dependencies in real brains:** graded lateral inhibition among competing
striatal/cortical populations, divisive (canonical) normalization of competing inputs,
neuromodulatory gain setting, and a commitment signal that is itself graded (vigour /
eligibility), not a latch.

**Is `affinity_input_cap` a faithful biological translation? -- NO. It is a formal-engineering
import, and the divergence is load-bearing.**

The substrate bounds an unbounded competing input with a **hard box clamp**,
`max(-cap, min(cap, value))`. Biology does not bound competing drives that way. It bounds them
with **saturating gain and divisive normalization** -- sigmoidal f-I curves, canonical
normalization (Carandini & Heeger; the `targeted_review_connectome_mech_439` corpus already
holds `canonical_normalization_carandini2012` and `normalization_attention_reynolds2009`), and
graded lateral inhibition (`da_graded_lateral_inhibition_kohnomi2016`, `spn_lateral_inhibition
_pommer2021` under `targeted_review_striatal_gain_control_bounding`).

**The functional difference is exactly the observed failure.** A box clamp has a discontinuous
derivative: below the clamp the signal is linear, above it is flat, and the transition between
"competitor dominates" and "drive dominates" happens over a vanishingly narrow parameter window
-- a knife-edge, precisely what the data show. A saturating / normalizing transform compresses
smoothly and produces a **wide** graded crossing, which is the regime MECH-266's hysteresis
needs in order to express at all. So "the cap is mis-calibrated" (H1) and "the register is
structurally bang-bang" (H2) may both be answering the wrong question: **the bounding operator
itself is the wrong shape.**

The same divergence appears one level down in the drive: biological commitment is graded
(vigour, eligibility), whereas `_et_commit = commit_w * float(beta_gate.is_elevated)` is a
boolean. This is the same complaint as the standing memory
`project_bg_commitment_over_f_dominance_route`.

**Does the failure resemble a missing biological dependency?** Yes -- it resembles what happens
when competing population drives lack normalization: whichever input is larger wins totally,
with no mixture. Under the skill's default stance this is a **discovered translation gap**, not
pressure on either claim.

**`lit_status: partial`.** The relevant biology is in the corpus (under MECH-439 / ARC-110), but
there is **no targeted review of bounding/normalizing competing affinity signals tagged to
SD-032a or MECH-266**. A small `/lit-pull` would ground the replacement operator; it is a
secondary recommendation, not the primary route (section 8).

---

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear (MECH-266) / intact (SD-032a)** | MECH-266 not exercised: its arm saturated at 1.0 with 0 switches in all 15 cells. SD-032a intact and narrowly strengthened -- discrete transitions are what it specifies, and the register alternated at the crossing. |
| Biological reference | **partial** | AIC-dACC switching (Menon & Uddin 2010) and BG Schmitt trigger (Collins & Frank 2014) are clear; the `affinity_input_cap` box clamp is a formal-engineering import diverging load-bearingly from saturating gain / divisive normalization. Lit present in the corpus but not tagged to these claims. |
| Prerequisites | **present** | `mode-governance-engagement` landed (`use_external_task_drive`, `salience_affinity_input_cap`, ree-v3 `9bcde4cb63`); the `_clone_for_arm` GoalState-drop fix landed; `experiments/_lib/regime_occupancy_gate.py` built and consumed; contact guard 3/3. |
| Implementation completeness | **partial** | Both required knobs default OFF (`salience_affinity_input_cap = None`, `use_external_task_drive = False`) -> inert in production. Boolean commit latch is a second, cap-independent discreteness source. Box clamp rather than saturating gain. |
| Environment adequacy | **adequate** | Full 603n scaffolded curriculum, foraging competence demonstrated (contact rates 0.25-0.31, 107+ contact events), 15 episodes x 10 cells x 3 seeds, hazard + P1 + P2 stages all passed. |
| Measurement adequacy | **under-instrumented** | The `graded` predicate is an existential over a 5-point grid evaluated PER SEED; it is grid-resolution dependent and cannot separate H1 from H2. No common-cap statistic was computed. `winning_cap_band_symmetric` is a min/max over two disjoint singletons but is named and read as a band. No crossing-steepness readout. `enabled_default_off_flags` null. |
| Integration adequacy | **coupled but unstable** | Drive + coordinator + curriculum do interoperate and produce occupancy for the first time in this lineage, but the operating point is seed-idiosyncratic (winning caps 2.33x apart; one seed with none). |
| Scale / capacity | **adequate for the question asked, thin for the question implied** | 3 seeds x 5 caps x 2 arms x 15 episodes is adequate for a reachability existential; 3 seeds is thin for a common-operating-point claim (V3-EXQ-935 adds seeds 45/46). |

### Failure-location summary (GOV-FAILLOC-1)

The adverse observation to classify is: *"no common cap operating point exists, and the
arbitration remains effectively bang-bang."*

| Bucket | Reads from | Verdict |
|---|---|---|
| MECHANISM FAILED | Implementation completeness = `partial` | **not_established** |
| MEASURES FAILED | Measurement adequacy = `under-instrumented` | **not_established** |
| ENVIRONMENT FAILED | Environment adequacy = `adequate` | **established** |
| REE FAILED | all three | **false** |

**Net classification: MIXED (MECHANISM + MEASURES) -- not chargeable to REE.** The environment
is the only one of the three that reads adequate; both the implementation (default-off facet,
boolean commit latch, box clamp) and the measurement (grid-dependent existential predicate, no
common-cap statistic) are independently inadequate, so REE FAILED is not reachable. This is a
translation-and-instrument finding, exactly the default stance the skill prescribes.

---

## 7. Re-derive brake (R1-R3)

Computed with the skill's binding recipe over confirmed artifacts only (R1 unit = RUN, R2 latest
adjudication supersedes, R3 `substrate_ceiling` only, honouring
`recommended_epistemic_category_per_claim`):

| Claim | Ceiling hits | Counted runs |
|---|---|---|
| **MECH-266** | **6** | 464b, 467b (`failure_autopsy_V3-EXQ-460b-461b-464b-466b_2026-06-04`); 464c, 467c (`failure_autopsy_SD-034-closure-cluster-ext_2026-06-12`); 464d, 467d (`failure_autopsy_grandfathered-r5-batch23-mixed-findings_2026-08-08`) |
| **SD-032a** | **6** | identical set (SD-032a is co-tagged on every one) |

Not counted, correctly: `v3_exq_797` (`substrate_conditional`), and 464e / 467e
(`failure_autopsy_mech266-464e-467e-cluster_2026-08-13`, both stamped `standard` per-claim).

**The brake is ALREADY FIRED** -- the 464e/467e cluster stamped `fired: true`,
`count_at_fire: 6`, `refused_requeue: true`, `route_to: implement-substrate`. **This run adds
nothing to either count** (its recommended category is `standard`, not `substrate_ceiling`), and
it is not a re-adjudication of any prior run, so `supersedes_autopsy: null`.

**V3-EXQ-934 was itself the sanctioned H1 leg** the prior brake explicitly permitted while
refusing "a naked V3-EXQ-464f/467f re-queue at the same cap behind the same min()-based gate".
That refusal **remains in force**.

**Caveat on SD-032a's count, recorded but not acted on.** All 6 of SD-032a's hits are co-tags on
MECH-266 experiments, and SD-032a is `stable` at conf 0.928 with 0 weakens. Its count is
plausibly inflated by the same peripheral-co-tag mechanism this autopsy guards against for
MECH-266. Per the skill's scope caution, a target is re-attributed **only** when its own artifact
says the claim was peripheral -- so no retro-fit is proposed here, and this is flagged for the
human, not fixed.

### Granularity-debt recurrence trigger: **DOES NOT FIRE**

Reading the `claim_alignment` distribution alongside the count, per the skill's rule that the
count alone is a weak signal: across the confirmed targets tagging MECH-266 / SD-032a, **no
target reads `weakened`** -- every one is a measurement / precondition / substrate-readiness
verdict, and this target reads `unclear` (MECH-266) / `intact` (SD-032a). A cluster in which no
target reads `weakened` is measurement or implementation debt, not granularity debt, however
many autopsies exist. **No `/claim-synthesis` routing.**

---

## 8. Learning extracted

1. **An existential over a swept parameter, evaluated PER SEED, cannot establish a shippable
   operating point.** Always report the per-cap cross-seed count beside the per-seed
   existential. Here they disagree completely: 2/3 seeds "graded", but 1/3 seeds at the best
   single cap.
2. **A "some grid point falls in the mixed band" predicate on a coarse grid detects a CROSSING,
   not GRADEDNESS**, and its pass probability rises with grid density regardless of the
   arbitration's smoothness. It therefore cannot separate a graded-arbitration hypothesis from a
   steep-switching one. A gate meant to discriminate those needs a **width/steepness** readout
   (band width in parameter units, or d(occupancy)/d(cap) at the crossing), not an existential.
3. **An aggregate that implies contiguity it does not have is a misleading statistic.**
   `winning_cap_band_symmetric = [min, max]` over disjoint singletons reads as a band and is not
   one. Report the actual `mixed_band_caps` set per seed and their intersection.
4. **Bounding an unbounded competing input with a hard box clamp is a formal-engineering import**
   diverging load-bearingly from biology's saturating gain / divisive normalization -- and the
   divergence *is* the observed knife-edge. Load-bearing by default, per SD-003 precedent.
5. **H1 and H2 are not mutually exclusive**, because a second cap-INDEPENDENT discreteness source
   exists (`_et_commit` is a boolean latch on `beta_gate.is_elevated`). The frozen-ledger
   question's framing needs updating; the portfolio was posed as an exclusive three-way choice
   and the substrate is not.
6. **Recording gap (minor, but exactly on point):** `enabled_default_off_flags` is `null`, yet
   this run's entire finding is conditional on two default-off knobs. `use_external_task_drive`
   appears only inside a prose `substrate` string; `affinity_input_cap_train` is in `config` but
   the production default (`None`) is nowhere. A run whose finding is configuration-conditional
   should record the enabled default-off flags machine-readably -- that field is precisely what a
   later reader needs to detect production-inertness without reading the substrate.
7. **Same production-inertness class as the MECH-267 sibling** (927/928, same day): validated
   facet, default-off knob. Recurrence across two unrelated claim families in one week suggests
   this is a standing pattern worth a governance-level check, not two incidents.
8. **A precondition can be measured and still be non-binding.** `external_task_drive_engages`
   cleared at 7-16x its floor; it is a liveness check and should not be presented alongside the
   contact guard (8-23% headroom) as though both are equally strong controls.

---

## 9. Draft `evidence_quality_note` (governance to write -- NOT written here)

> V3-EXQ-934 (diagnostic, excluded from confidence scoring; GOV-FANOUT-1 leg H1 of frozen-ledger
> question `mech266_mode_arbitration_saturation`). Both readiness preconditions cleared on
> measured, non-vacuous values (contact guard 3/3 seeds, contact rates 0.25-0.31, z_goal peaks
> 0.433-0.492 against a 0.4 gate; margin guard 3/3, though at 7-16x its floor it is a liveness
> check rather than a strong control). On the primary ARM_SYMMETRIC the single load-bearing
> criterion passed at exactly the 2/3 minimum. READ IT NARROWLY. The criterion is an EXISTENTIAL
> over the 5-point cap grid evaluated PER SEED, and the two passing seeds' mixed cells sit at
> OPPOSITE ENDS of the sweep (seed 42 only at cap 0.75, occupancy 0.5606; seed 43 only at cap
> 1.75, occupancy 0.4447; seed 44 never, minimum 0.9002 against a 0.9 ceiling). NO single cap
> grades on more than 1 of 3 seeds (0.75 -> 1/3; 1.0/1.25/1.5 -> 0/3; 1.75 -> 1/3), so
> `winning_cap_band_symmetric = [0.75, 1.75]` is the min/max of two disjoint singletons, not a
> band, and no common operating point was demonstrated. The mixed cells ARE non-degenerate (18-19
> switches, mode-conditioned external_task dwell 43-54 steps), so the SD-032a mode register does
> genuinely alternate where the argmax crossing sits -- but that crossing is at most one grid
> step (0.25 cap units) wide in every seed showing it, and its location differs by >= 1.0 cap
> units across seeds, so an existential on a 5-point grid detects a CROSSING and cannot
> discriminate H1 (graded arbitration) from H2 (structurally bang-bang). H2 is NOT eliminated by
> this run. TWICE NON-PRODUCTION: `salience_affinity_input_cap` defaults to `None` (no clamp) and
> `use_external_task_drive` defaults to `False`, so the swept configuration is not production;
> training was held at cap 2.0, itself outside the swept range; and the driver's own
> pre-authoring probe recorded `operating_mode['external_task'] = 0.0` at the production default
> cap=None. Mechanistically the clamp is a no-op on `external_task_drive` at every cap >= 1.0
> (that signal is already bounded to [0,1] at `agent.py:6958`), so 4 of the 5 swept cells
> manipulate only the competing unbounded affinity inputs; and `_et_commit = commit_weight *
> float(beta_gate.is_elevated)` (`agent.py:6944`) is a boolean latch -- a second, cap-INDEPENDENT
> discreteness source no cap can grade. Failure-location (GOV-FAILLOC-1): MIXED (MECHANISM +
> MEASURES); environment adequate, implementation partial, measurement under-instrumented; not
> chargeable to REE. Successor V3-EXQ-935 (claimed 2026-08-16T13:01Z) already tests the
> common-operating-point question via a margin-normalised cap rule on 5 seeds.

**Per-claim notes.**

- **MECH-266:** PERIPHERAL in V3-EXQ-934 -- not exercised. The MECH-266 manipulation arm
  (`ARM_ASYM_STICKY_TASK`, sticky exit rail) sat at `fraction_in_external_task = 1.0` with
  `n_switches = 0` in all 15 cells (3 seeds x 5 caps), which is the intended manipulation and
  not a dose-response, so no over-binding gradient could express; the load-bearing criterion was
  evaluated on the symmetric arm, which contains no MECH-266 mechanism. The run establishes a
  measurement precondition for a future MECH-266 test and weighs nothing for or against the
  claim. No `substrate_ceiling` attribution accrues to MECH-266 from this run
  (`pending_retest_after_substrate` holds).
- **SD-032a:** Narrow diagnostic support only. Where the argmax crossing sits, the SD-032a mode
  register produced genuine discrete alternation (seed 42 @ cap 0.75: 19 switches,
  `ext_dwell_mean` 43.2; seed 43 @ cap 1.75: 18 switches, `ext_dwell_mean` 53.5) with the
  MECH-259 switch trigger firing -- the first alternating occupancy in this lineage, which
  previously read 0.0 or 1.0 everywhere. Note SD-032a's own `functional_restatement` specifies
  that mode transitions ARE discrete, not graded, so the bang-bang shape reported by 464e/467e is
  SD-032a behaving as written and is not evidence against it; what remains unresolved is whether
  a contested-occupancy window wide enough for MECH-266's hysteresis to express is obtainable,
  which is V3-EXQ-935's question.

---

## 10. Repair pathway and routing (DRAFT -- staging mode, not finalised)

**Work-graph node classification.** The primary open item is `complicated (buildable)`: replace
the box clamp with a saturating/normalizing bounding operator and decide the production default.
There is no missing fact -- the mechanism, the biology, and the measured shortfall are all in
hand. The secondary item (does a common operating point exist) is `complex (probe-gated) /
puzzle (known rules)` and **is already in flight as V3-EXQ-935** -- so it is not routed here.

**Primary routing: `implement-substrate`** -- `amend` the existing `mode-governance-engagement`
entry (`substrate_queue.json` queue[100], status `implemented_pending_validation`,
`severity: corrupting`, priority 1, `unblocks_claims: [MECH-266, SD-032a]`). Do **not** create a
new entry; this is the same gap one level deeper.

The amend carries three items:

1. **Replace the hard box clamp with a saturating bounding operator** on the affinity inputs
   (e.g. `cap * tanh(value / cap)`, or divisive normalization across the affinity-input set),
   grounded in canonical normalization / graded lateral inhibition. Rationale: a box clamp's
   discontinuous derivative is what produces the observed <= 1-grid-step crossing; a saturating
   operator widens it, which is the precondition MECH-266's hysteresis needs. Keep the existing
   clamp reachable behind a mode selector so the 934 baseline stays reproducible.
2. **Grade the commitment term.** `_et_commit = commit_w * float(beta_gate.is_elevated)`
   (`agent.py:6944`) is a boolean latch and a cap-independent discreteness source. Replace with a
   graded commitment strength (vigour / eligibility) so that H1 and H2 stop being entangled.
3. **Decide and record the production default.** `salience_affinity_input_cap = None` and
   `use_external_task_drive = False` mean this whole lineage is inert in production. This is
   NOT a simple default flip (unlike the 927/928 sibling) because no single cap value works
   across seeds -- so the deliverable is either a normalised rule (pending V3-EXQ-935) or an
   explicit, documented decision that the facet stays opt-in with the reason recorded on the
   claim.

**`severity` stays `corrupting`, with an updated reason.** The entry's corrupting classification
was for the min()-across-arms non-vacuity gate, which `experiments/_lib/regime_occupancy_gate.py`
resolved. This autopsy identifies a **successor defect in the same file**: the per-seed
existential `graded` predicate plus the `[min, max]` "band" summary produce a reading that looks
valid and is not (the run routes `cap_recalibration_admits_mixed_regime` from data in which no
cap recalibrates more than one seed). That is the `corrupting` definition exactly. `substrate_paths`
gains `ree_core/agent.py`.

**Secondary, NOT the primary route: `/lit-pull` commission.** A `targeted_review` on bounding /
normalizing competing drive signals tagged to SD-032a + MECH-266, drawing the existing
`canonical_normalization_carandini2012`, `normalization_attention_reynolds2009` (MECH-439
corpus) and `da_graded_lateral_inhibition_kohnomi2016`, `spn_lateral_inhibition_pommer2021`
(`targeted_review_striatal_gain_control_bounding`) into the SD-032a/MECH-266 evidence line, to
ground the replacement operator in item 1. Recorded here; governance to chip if it accepts the
routing.

**Explicitly NOT routed (and why).**

- **No `/queue-experiment`.** V3-EXQ-935 is already **claimed and running** (ree-cloud-1,
  2026-08-16T13:01:18Z) and asks precisely the common-operating-point question this autopsy
  identifies, on 5 seeds with a margin-normalised cap rule and a matched absolute control. Its
  own queue note already records the same 1/3-per-cap re-read independently. Queuing anything on
  this question would duplicate it.
- **The re-derive brake's refusal stands.** No naked V3-EXQ-464f / 467f re-queue at the same cap
  behind the same gate.
- **No `/claim-synthesis`.** Granularity-debt trigger does not fire (section 7).
- **No demotion.** The demotion gate (tested fairly + biology supports + still fails) is not met
  on any of its three limbs.

**Per the skill's Step 8 rule, this session does NOT `spawn_task` its own routing's follow-on** --
the recommendations above are proposals for `/governance` to ratify at its Step 2b, and it is
governance that chips them. Governance should first check
`evidence/planning/igw_routine_ledger.json` / `igw_assignments.json` for an existing
`mode-governance-engagement` assignment before spawning, since IGW auto-discovery may already have
staged the identical build.

---

## 11. Frozen-ledger pre-registration (STAGING -- drafted only, NOT written)

Per the hard constraints for this run, `hypothesis_space_registry.v1.json` was **read but not
written**. The intended append is recorded in the JSON artifact under
`hypothesis_space_ledger_pending` for the confirming session to apply.

**Growth-restriction check (Step 9b, run before any disposition):** question
`mech266_mode_arbitration_saturation` carries `growth_restriction: null`. **Absent -> proceed
normally, nothing to surface at the gate.**

**No denominator growth is proposed.** `initial_frozen_count` stays 3,
`initial_frozen_count_at_registration` stays 3. The proposal is a Mode B **resolve** of the
existing leg `H1-cap-miscalibration` (axis `representation`, already in `axis_families.map`) to
state **`split`**, with children `H1a-per-seed-cap-admits-mixed` (confirmed) and
`H1b-common-cap-operating-point` (alive, adjudicated by V3-EXQ-935). Children live inside the
resolution, so no new `hypotheses[]` entries and no invariant-3 growth event.

`H2-structural-bang-bang` and `H3-instrument-illposed` are **left untouched and `alive`**. This
autopsy explicitly does **not** eliminate H2 -- section 2b is the argument for why this run
cannot -- and offers the human the alternative disposition of leaving H1 `alive` on the same
grounds, since a criterion that cannot discriminate H1 from H2 arguably narrows nothing.

**A note for the confirming session:** the portfolio was posed as an exclusive three-way choice,
and the boolean commit latch (section 2c) shows H1 and H2 are not exclusive on this substrate.
Whoever applies this should consider recording that on the question's `decision` block rather
than silently resolving legs against a framing the substrate has outgrown.

---

## 12. For the human at the confirmation gate

1. **Is `split` the right disposition for H1, or should it stay `alive`?** The criterion passed,
   but section 2b argues it cannot do the discrimination it was pre-registered to do.
2. **The label `cap_recalibration_admits_mixed_regime` should not be quoted downstream without
   the "no common operating point / <= 1 grid step / non-production" qualifier.** It is already in
   `pending_review.md`.
3. **SD-032a's brake count of 6 is all peripheral co-tags** on MECH-266 experiments. Worth a
   decision on whether the corpus should be re-attributed; this autopsy deliberately did not.
4. **Production-inertness has now appeared twice in one week** (927/928 MECH-267;
   934 MECH-266/SD-032a). Governance may want a standing check that a validated facet's knob is
   not left default-off, rather than catching it per-autopsy.
