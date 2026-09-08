# MECH-095 / SD-047: what a VALID retest would be

**Status:** design artifact only. **NOTHING IS QUEUED BY THIS DOCUMENT, and the primary design in
section 6 MUST NOT be queued until its release condition fires.**
**Written:** 2026-09-08T20:12:00Z, session `w6-s5a-closure-20260908`, campaign W6-S5a.
**Chip:** `chip-20260905-mech095-sd047-valid-retest-design` (item 4 of
`chip-20260908-w5-s4-zero-compute-closure`).
**Commissioned by:** governance `governance-20260905` user decision, recorded in the MECH-095
`claims.yaml` note: MECH-095 parked at 12 R1-R3 ceiling hits, parking STANDS, and "the only
V3-actionable debt is the SD-047 retest that has never validly run".

---

## 1. The tension this document exists to resolve, stated plainly

Governance asked for a **valid SD-047 retest**. MECH-095's own `what_would_answer` and the fired
re-derive brake **refuse any single-agent SD-047 run as a verdict-bearing test of MECH-095**. Both
are correct, and they are not actually in conflict once the equivocation on "SD-047 retest" is
removed:

- The debt governance names is real: the 047 lineage never produced a *valid* measurement of the
  comparator's contribution, so MECH-095's ceiling was, until 2026-07-12, asserted rather than
  demonstrated.
- That debt was **discharged** on 2026-07-12 by V3-EXQ-741, which is the only valid test the
  lineage ever produced. It is the reason `n_ceiling_hits` moved 0 -> 1.
- What remains owed is **not** a further single-agent SD-047 letter. MECH-095's
  NON-DEGENERACY PRECONDITION (HARD) is explicit: "a run on any single-agent substrate, including a
  further SD-047 letter, is explicitly REFUSED by the re-derive brake and should self-route
  `substrate_not_ready`, not count as a verdict." V3-EXQ-741's autopsy sets `refused_requeue: True`
  and names the only sanctioned successor: the retest against a built multi-agent substrate
  (`multi_agent_ecology_v5:MAE-3`).

**Therefore this document specifies two things, and keeps them rigidly apart:**

| | Design | Verdict-bearing for MECH-095? | Queueable now? |
|---|---|---|---|
| **A** | Section 6 -- the MAE-3 retest | YES | **NO** -- gated on MAE-1 -> MAE-2 -> MAE-3 |
| **B** | Section 7 -- the INV-012 Leg 4 single-agent consumer probe | **NO, by construction** | Design ready; queue only on the terms in 7.6 |

Design B exists because MECH-095's own notes (2026-08-25 cross-reference) and
`thought_intake_2026-08-12_responsibility_as_epistemic_hygiene.md:46` identify one downstream
consumer of the comparator's output that "does not itself require resolving MAE-3" -- an agent has
direct efference-copy access to its *own* committed action without needing to disambiguate it from
another agent's. Design B is **not** a back door to a MECH-095 verdict and must never be scored as
one; it tests a consumer, and its self-route on any MECH-095-shaped reading is
`substrate_not_ready`.

---

## 2. What MECH-095 asserts, and what any test must instantiate

At the `z_self` / `z_world` interface, an explicit agency-detection comparator (TPJ-equivalent)
compares **efference-copy-predicted** `z_self` change with **observed** `z_self` change. Match =>
self-caused (no residue). Divergence => attribute to `z_world` (potential residue).

Two properties of the claim constrain every design below and are the two the 047 lineage kept
violating:

1. **The readout must be ADDITIVE and QUERY-TIME.** MECH-095's confirming signature specifies "a
   query-time READ-OUT comparator ... additive -- not a gradient head reshaping `z_world`". A
   gradient head trained on an attribution label is a *different* mechanism: it can, and on
   V3-EXQ-047m did, corrupt a `z_world` representation that was already good (BASELINE 0.795 ->
   ROUTED -0.302).
2. **The comparator's discriminandum is SELF vs OTHER-CAUSED, not SELF vs AMBIENT DRIFT.** Every
   047-lineage operationalisation substituted environmental drift for the "other". That
   substitution is what V3-EXQ-741 measured and falsified as a test-bed.

Live substrate today: `ree-v3/ree_core/comparator/tpj_comparator.py` (`TPJComparator.compare()`,
`compute_agency_loss()`, `forward()`), gated by `use_tpj_comparator: bool = False` and
`tpj_agency_threshold: float = 0.5` at `ree_core/utils/config.py:4062-4069`. The module implements
exactly the claim's readout: `agency_signal = 1/(1 + ||z_self_pred - z_self_obs||)`.

---

## 3. Every prior attempt, and why it was invalid rather than merely negative

All artifacts under `REE_assembly/evidence/experiments/`.

| # | Attempt | Outcome | DV | Criterion | Measured | Invalidity class (sec. 4) |
|---|---|---|---|---|---|---|
| 1 | V3-EXQ-011 TPJ proxy | FAIL 4/5 | E2 efference mismatch, harm vs safe | gap > 0.005 | 0.00470 | **I** DV at floor (mismatch magnitudes 0.009-0.014); 1 seed, RANDOM policy |
| 2 | V3-EXQ-089 TPJ validation | FAIL 3/5 mixed | mismatch_world - mismatch_self | gap > 0.02; false_attr < 0.15 | 0.003798; false_attr **1.0000** | **IV** comparator untrained (eval-only); thin pre-SD-047 world |
| 3 | V3-EXQ-047i routing PoC | FAIL 2/5 weakens | contact_dissociation | > 0.05 | **+0.000 in BOTH arms** | **II** DV structurally pinned -- contact_world == contact_self exactly (0.911/0.911); routing loss 0.0000, comparator never active |
| 4 | V3-EXQ-047j CE-head | FAIL 4/5 mixed | contact_recall_world | C3 action_dissoc > 0 | -0.004 | Threshold call, not degeneracy (relaxed in 047k). 2 seeds |
| 5 | **V3-EXQ-047k** | **PASS 5/5 supports** | contact_recall_world | > 0.55 / > 0.04 / > -0.05 | 0.796 / +0.065 / -0.007 | Valid then. **Sole positive**, thin pre-SD-047 env, 4 seeds. Flagged single-positive-base under the illusory-conflict rule |
| 6 | V3-EXQ-098b three-stream | FAIL mixed | attribution AUC | delta >= 0.05 | 0.9942 vs 0.9989, **delta -0.0047** | **I** DV at CEILING -- both arms ~0.99 AUC, no headroom |
| 7 | V3-EXQ-121 agency pair | FAIL 1/5 weakens | attribution AUC ON vs ABLATED | delta >= 0.05 | **0.4110 vs 0.7450, delta -0.3340** | **IV** z_self 32-dim too noisy; comparator actively hurt |
| 8 | V3-EXQ-506 substrate comparator | FAIL non_contributory, `scoring_excluded` | counterfactual gap ratios | ratio >= 1.5 | 1.0054 / 1.0019 / 0.9915 | **III** `r2_s_to_a` invariant to action type (~0.99 everywhere) -- no self/env vocabulary. C4-only-PASS = the ceiling signature |
| 9 | V3-EXQ-509 SD-047 readiness | **PASS 7/7** | calibration ratio | in [0.5, 2.5] | **2.03:1** | Valid, but substrate-only; not a MECH-095 test |
| 10 | V3-EXQ-510 live-env gap | FAIL, WOO_SPELKE branch | 4-way causal gap ratios | >= 1.5 | ratios 1.145-1.206; **n_c1=n_c2=n_c3=0 in all arms** | **III** + missing SD-047 clause-(B) class-count/band guard; pools inverted at ARM_2/ARM_3 (agent:env ~1:2.5 then ~1:4.3) |
| 11 | V3-EXQ-047l SD-047 retest | FAIL 3/5 non_contributory | contact_recall_world | > 0.55 | **0.000 in BOTH arms** | **II** PROBE-PARTITION SATURATION -- `is_contact` folded `env_events>0`, true on every probe step; no-contact negative class EMPTY (126==126, 119==119, 113==113, 105==105). Recall pinned at 0.0. Not counted as a ceiling hit |
| 12 | V3-EXQ-047m corrected | FAIL 3/5 non_contributory | contact_recall_world | > 0.04 improvement | ROUTED 0.492 vs BASELINE 0.795, **-0.302** | **II** TRAINING-LABEL SATURATION -- `is_world ~ const 1` (env_ev_ticks ~4405-4484 of ~4800); routing head never saw a self-caused negative. Its guard checked only the PROBE partition, so `non_degenerate=true` was a **FALSE CLEAR**. Not counted as a ceiling hit |
| 13 | **V3-EXQ-741 test-bed** | FAIL non_contributory | recall_improvement A and B | >= 1 valid arm with impr > 0.04 | **best 0.0276**; mean_A -0.1139, mean_B +0.0033; `b_beats_a=True`; **all 4 arms valid** | **VALID.** `non_degenerate: True`, both guards cleared in every arm. **1st and only valid ceiling hit** (`n_ceiling_hits` 0 -> 1) |
| 14 | V3-EXQ-1001 | non_contributory for MECH-095 | -- | -- | -- | Not a test; no comparator instantiated. Declared `standard` so it mints no 13th hit |

### V3-EXQ-741 per-arm result -- the prior every new design must beat

| arm | intensity | recall_base | impr_A | impr_B | n_self/world_min | n_no_contact_min | valid |
|---|---|---|---|---|---|---|---|
| ARM_0 | 0.00 (SD-047 OFF) | 0.750 | **+0.028** | +0.018 | 164/5 | 11 | YES |
| ARM_1 | 0.25 | 0.796 | -0.078 | -0.034 | 114/5 | 10 | YES |
| ARM_2 | 1.00 | 0.824 | -0.071 | +0.010 | 103/7 | 7 | YES |
| ARM_3 | 4.00 | 0.647 | -0.024 | +0.014 | 68/7 | 4 | YES |

**The peak is at ARM_0, with SD-047 OFF.** The predicted inverted-U did not materialise: adding
multi-source dynamics monotonically failed to help. This is the single most important empirical
fact for the design, and it is why more SD-047 intensity is not the lever.

**Corroborating sibling:** V3-EXQ-529 tested SD-047's *other* named beneficiary MECH-098 on the same
substrate (ARM_0 neither / ARM_1 SD-047 only / ARM_2 SD-047 + reafference) -> FAIL / weakens.
SD-047's clause (B) -- the *enabling* clause -- has therefore fired FALSIFYING against both of its
named consumers: "Both named consumers, four valid exercises, zero positive discrimination."

---

## 4. The four invalidity classes (the taxonomy the retest must defeat)

Reading the 13 attempts together, the failures are not 13 independent mistakes. They are four
recurring classes, and a valid design must carry an explicit, *reported* guard against each.

- **Class I -- DV at floor or ceiling.** No headroom for any effect to appear in
  (011: 0.0047 against a 0.005 threshold; 098b: 0.9942 vs 0.9989 AUC). Guard: a **measured**
  headroom probe, section 8.
- **Class II -- Partition saturation.** One class of a binary partition is empty or near-empty, so
  the DV is pinned by construction (047i contact_world == contact_self; 047l no-contact class
  empty; 047m `is_world ~ 1`). Guard: minimum count in **both** classes of **every** partition the
  design uses, reported per cell. 047m is the cautionary case: it guarded the *probe* partition and
  not the *training-label* partition, and its `non_degenerate=true` was a false clear.
- **Class III -- Discriminandum absent from the substrate's causal vocabulary.** The environment
  cannot express the distinction being measured (506: `r2_s_to_a` invariant to action type; 510:
  `n_c1=n_c2=n_c3=0` in all arms). Guard: report per-condition class counts and require the
  calibration band **in the arm being read** -- SD-047's own clause-(B) guard, which 510 lacked.
- **Class IV -- Mechanism inert or actively harmful.** The comparator was untrained (089), or the
  gradient head corrupted a good representation (121: -0.3340; 047m: -0.302). Guard: the readout
  must be **additive and query-time** (MECH-095's own specification), which structurally cannot go
  negative the way a gradient head can. V3-EXQ-741's ROUTED_B is the correct form; `b_beats_a=True`
  in that run is the evidence.

**Class V, added by V3-EXQ-741 and the one no 047 letter can defeat: NO STRUCTURALLY-DISTINCT
OTHER.** All four arms were valid, all guards cleared, and the comparator still did no work,
because SD-047's world-caused drift is ambient, not agentive, and the baseline already carries the
contact signal (`baseline_carries_contact: True`). This is a substrate ceiling, and it is why
Design A is MAE-3-gated.

---

## 5. What "VALID" means here -- five gates, all reported, all pre-registered

A run counts as a verdict on MECH-095 only if **all five** hold and each is reported in the
manifest. Gates 1-2 mirror V3-EXQ-741's (MECH-095's `what_would_answer` requires exactly that);
3-5 close the gaps 741 did not have to face.

1. **Probe-partition non-degeneracy.** Both classes of the evaluation partition have
   `>= PROBE_NEG_FLOOR = 5` samples per cell (arm x seed x condition). Report `n_no_contact_min`.
2. **Self/world training-label balance.** Both classes have `>= SW_BALANCE_FLOOR = 5` samples per
   cell. Report `n_self_min` and `n_world_min` **separately**; a single pooled count is what made
   047m's clear false.
3. **Four-way class-count and calibration band, in the arm being read** (SD-047 clause-(B) guard,
   absent from 510). Report counts for `agent_caused / env_caused / agent_collateral /
   env_correlated`; the agent:env ratio must sit in `[0.5, 2.5]` in the arm scored. 510's pools
   inverted to ~1:4.3 by ARM_3 while the run reported only pool-non-emptiness.
4. **Measured DV headroom** (section 8). `recall_base <= 0.70` in at least one arm, established by
   the headroom probe **before** the confirmatory run.
5. **Structurally-distinct OTHER present**, whose actions are causally attributable separately from
   ambient drift, with an `other_caused` transition class carrying `>= 20` events per cell.
   *This is the gate no single-agent substrate can pass.*

**Additionally:** the readout is additive and query-time (the 741 ROUTED_B form). A gradient head
is permitted only as a clearly-labelled secondary arm, never as the scored one.

---

## 6. DESIGN A -- the verdict-bearing retest. GATED: DO NOT QUEUE

**Release condition:** `multi_agent_ecology_v5:MAE-3` implemented and validated, which requires
MAE-1 (`MultiAgentCausalGridWorldV4` + per-agent REEAgent) then MAE-2 (per-agent observation +
arbitration). All three are `blocked` in `closure_status.md` (lines 233, 302, 394) and
`grep -rln "other_agent\|n_agents\|multi_agent" ree-v3/ree_core/ --include="*.py"` returns
**nothing**. Until then any run of this design self-routes `substrate_not_ready` and is not a
verdict.

**Inherit the harness from `experiments/v3_exq_741_mech095_agency_comparator_testbed_sd047.py`** --
the only valid harness the lineage produced -- not from any 047 letter.

**Arms** (4, crossing the presence of the OTHER with ambient drift, so the two causes of `z_self`
divergence are separated rather than confounded -- the confound that sank the whole 047 lineage):

| arm | other agent | SD-047 multi-source | purpose |
|---|---|---|---|
| ARM_0 | absent | off | baseline; reproduces 741 ARM_0 as a positive control on the harness |
| ARM_1 | **present**, non-interacting | off | isolates OTHER-caused divergence with no ambient drift |
| ARM_2 | **present**, interacting | off | the informative arm: other-caused change is behaviourally consequential |
| ARM_3 | **present**, interacting | on, intensity 1.0 | ambient drift added; tests whether the comparator still discriminates OTHER from AMBIENT |

Note the deliberate inversion of the 047 design: intensity is **not** the swept variable. 741
showed the intensity sweep peaks at intensity 0. The swept variable is now the **presence and
interactivity of the other**, which is the claim's actual discriminandum.

**Conditions per (arm x seed):** BASELINE (no comparator) / ROUTED_B (query-time additive readout on
`concat([z_world_baseline, agency_residual])`; never backprops into `z_world`) / ROUTED_A (gradient
BCE head, secondary and labelled, retained only as the A-vs-B contrast that made `b_beats_a`
legible in 741).

**Primary DV:** `recall_improvement_B` = other-caused-event recall, ROUTED_B minus BASELINE, in the
scored arm. Secondary DVs, all pre-registered, from MECH-095's confirming signature: other-agent
event selectivity, counterfactual gap (agent-caused minus other-caused), attributor calibration
slope.

**Pre-registered criterion (all must hold in >= 1 arm, and that arm must pass all five gates):**

- `recall_improvement_B > 0.04`
- C1 other-agent-event selectivity `> 0.5`
- C2 counterfactual gap (agent-caused minus other-caused) `> 0.1`
- C3 attributor calibration, within-arm slope `< 0.5`

**Falsifying branch (pre-committed, and it is a real outcome, not a fallback):** with the OTHER
present and all five gates cleared, if no arm clears the criterion across the full sweep, this is
the **Woo/Spelke branch** -- route `substrate_ceiling -> substrate_conditional` and set
`evidence_direction: weakens`, **not** `non_contributory`. MECH-095's `what_would_answer` commits to
this in advance; it must not be re-litigated after seeing the numbers.

**Seeds:** 8 (`[42, 7, 123, 99, 5, 17, 256, 1024]`), the first four preserving 047k's set so the
sole historical positive is directly comparable. 741 used 4; 8 is the minimum for the
majority-of-seeds requirement release_condition (b) imposes elsewhere, and seed 123 was
catastrophic in 047m (world 0.111 / self 1.000), so per-seed reporting is mandatory -- no
seed-pooled headline.

**Analysis:** per-arm, per-seed, per-condition; no pooling across arms. Report all five gates and
all four criteria for every cell, including cells that fail a gate (a gate failure is data about the
substrate, not a row to drop).

---

## 7. DESIGN B -- the single-agent consumer probe. NOT a MECH-095 verdict

### 7.1 Why this is legitimate when another 047 letter is not

The re-derive brake refuses a further single-agent test **of MECH-095**. Design B does not test
MECH-095. It tests a *downstream consumer* of the comparator's output -- INV-012 Leg 4, epistemic
responsibility -- on the specific ground recorded in MECH-095's own notes and in
`thought_intake_2026-08-12_responsibility_as_epistemic_hygiene.md:46`: an agent has direct
efference-copy access to its **own** committed action without needing to disambiguate it from
another agent's, so the confound is constructible in a **single-agent** environment.

The distinction is not a technicality and must be preserved in the manifest: Design B's
discriminandum is **self-caused vs not-self-caused**, which a single agent can access from its own
efference copy. MECH-095's discriminandum is **self-caused vs OTHER-caused**, which it cannot.

### 7.2 Mandatory manifest declarations

- `claim_ids_tested`: **INV-012** (not MECH-095).
- MECH-095 appears only as `related_claims`, with `evidence_direction: non_contributory` and
  `scoring_excluded: single_agent_not_a_mech095_verdict`.
- The driver **must** self-route `substrate_not_ready` on any MECH-095-shaped reading, exactly as
  MECH-095's NON-DEGENERACY PRECONDITION requires.

### 7.3 Arms

| arm | comparator | external cause | purpose |
|---|---|---|---|
| ARM_0 | off | off | baseline |
| ARM_1 | ROUTED_B | off | comparator with nothing to attribute away -- a null-control |
| ARM_2 | ROUTED_B | **SD-029 scheduled external hazard** on | the informative arm |
| ARM_3 | ROUTED_B | SD-047 multi-source at 1.0 | ambient-drift contrast against ARM_2 |

**SD-029 rather than SD-047 is the deliberate choice.** `scheduled_external_hazard_enabled` /
`_interval=50` / `_prob=0.5` / `_adjacent_only=True`
(`ree_core/environment/causal_grid_world.py:267-275, 899-904, 3045-3048`) is the only single-agent
knob in V3 with any *directed, aimed-at-me* structure. It is scheduled rather than intentional, so
it is emphatically not a substitute for an OTHER -- but for a self-vs-not-self consumer probe,
directedness is not required, and SD-029 is untouched by the 047 lineage and therefore free of its
saturation history.

**Set `tag_env_caused_multisource_ttype = True` in ARM_3** (`causal_grid_world.py:439`, tagging at
3243-3257). This is the 047m fix: it fills residual `transition_type == "none"` with
`env_caused_multisource`, giving `is_world ~ 0.15` at intensity 1.0 instead of the saturated ~0.93
that made 047m's label constant. Without it, ARM_3 reproduces Class II by construction.

### 7.4 DV and criterion

**Primary DV:** self-attribution accuracy on committed actions -- the fraction of steps whose
`z_self` change the comparator attributes to self, on steps where the agent's own committed action
is the sole cause, minus the same on steps where an external cause is present. This is a
**within-run difference**, so it does not require the comparator to beat a baseline that already
solves the task -- the failure that pinned 741.

**Pre-registered criterion:** `self_attribution_gap > 0.15` in ARM_2, with gates 1-4 of section 5
cleared in that arm (gate 5 is inapplicable and its inapplicability is *why* this is not a MECH-095
verdict). Secondary: the gap in ARM_2 exceeds the gap in ARM_3, which would show the comparator
discriminates directed external cause from ambient drift.

**Seeds:** 8, same set as Design A.

### 7.5 What each outcome licenses -- and what it does not

- **PASS:** INV-012 Leg 4 gains a working consumer; MECH-095 gains **nothing**. It remains parked at
  its ceiling.
- **FAIL with gates cleared:** evidence against the *consumer*, and a genuine data point that the
  comparator readout is inert even where its discriminandum is accessible. Route to INV-012, not to
  MECH-095.
- **FAIL on a gate:** a measurement failure. Autopsy it; do not read it as evidence about either
  claim.

### 7.6 Terms of queueing

Design B is **not queued by this document**. Before queueing: (a) confirm with governance that the
INV-012 routing is accepted, since it re-points a MECH-095-commissioned chip onto a different
claim; (b) run the section 8 headroom probe first; (c) queue via `/queue-experiment` under a new
EXQ id, never an 047 letter -- the letter namespace carries the refused lineage and reusing it
invites exactly the misreading this document is written to prevent.

---

## 8. Measured `dv_headroom` plan (mandatory, and it runs FIRST)

Class I killed two attempts (011 at floor, 098b at ceiling) and Class V's mechanism in 741 was a
headroom problem in disguise: `baseline_carries_contact: True` meant the baseline already solved
the task, leaving the comparator 0.176-0.353 of range to work in while the criterion demanded 0.04
of it.

Headroom against the 741 priors, computed from the per-arm table:

| arm | recall_base | remaining headroom to 1.0 | 0.04 as a share of headroom |
|---|---|---|---|
| ARM_0 | 0.750 | 0.250 | 16.0% |
| ARM_1 | 0.796 | 0.204 | 19.6% |
| ARM_2 | 0.824 | 0.176 | **22.7%** |
| ARM_3 | 0.647 | 0.353 | 11.3% |

Best improvement actually observed was `+0.0276` at ARM_0 = 11.0% of that arm's headroom. The
criterion was therefore asking for roughly double the largest effect the design could produce.

**The plan, pre-registered:**

1. **Headroom probe first**, as a separate cheap run (2 seeds, no comparator): measure `recall_base`
   per arm.
2. **Gate 4 predicate:** an arm is *informative* only if `recall_base <= 0.70`, i.e. remaining
   headroom `>= 0.30` and the 0.04 criterion is `<= 13%` of it.
3. **If no arm clears 0.70,** do not run the confirmatory experiment. Change the DV or weaken the
   baseline (shorten training, reduce episode count) until one does, and re-probe. A confirmatory
   run against a saturated baseline is a Class I failure that will be indistinguishable from a
   negative result -- which is precisely what 098b and 741 produced.
4. **Report `dv_headroom` in the manifest** for every arm, whether or not it gated.

---

## 9. Bookkeeping notes for governance

- **The "12 ceiling hits" and the valid-hit count are different quantities and should not be
  conflated.** `n_ceiling_hits` = **1** (V3-EXQ-741 alone). The 12 is the mechanical R1-R3 counter
  (`failure_autopsy_V3-EXQ-1001_2026-09-04.md` sec. 6, lines 313-358): `047m`, `741`, and ten
  grandfathered cluster targets (`047i`, `047j`, `089` x2, `098b` x3, `121`, `011`, `510` x2).
  047l is **not** among them. The drift was already flagged for correction in
  `failure_autopsy_grandfathered-arc024-hippo-tpj-cluster_2026-08-08.md:33` (mechanical count 3 vs
  `claims.yaml` 1), and a third tally exists at
  `rederive_brake_run_dedup_blast_radius_20260819.md:97` (`| MECH-095 | 5 | 12 |`). **Three
  different numbers are live for the same quantity.** This is a bookkeeping defect, not a scientific
  one, but it should be reconciled before any promotion/demotion reads the count.
- **SD-047's clause (B) has fired FALSIFYING** and that is settled: both named consumers (MECH-095
  via 741, MECH-098 via V3-EXQ-529), four valid exercises, zero positive discrimination. Clause (A),
  the build clause, remains confirmed (V3-EXQ-509 PASS 7/7, ratio 2.03:1). The substrate is correct;
  it simply does not enable what it was hoped to enable.
- **`agency_comparator_testbed_sd047` is exhausted** as the MECH-095 ceiling substrate, by its own
  `implementation_hint`. No further entry should be minted against it.
- **The sole positive (047k) stands flagged** as a single-positive base under the
  illusory-conflict-resolution rule, on a thin pre-SD-047 operationalisation, never reproduced by
  any subsequent valid test.

---

## 10. Summary

| Question | Answer |
|---|---|
| Was the owed SD-047 retest ever validly run? | **Yes, once** -- V3-EXQ-741, 2026-07-12. It is the only valid run in the lineage and produced the only real ceiling hit. |
| Is further single-agent SD-047 work warranted? | **No.** The brake refuses it, the intensity sweep peaks at intensity 0, and clause (B) has fired falsifying against both named consumers. |
| What is the valid retest? | **Design A** (sec. 6), gated on MAE-3. Not queueable. |
| Is anything queueable now? | **Design B** (sec. 7) -- an INV-012 consumer probe, explicitly not a MECH-095 verdict, and only on the terms in 7.6. |
| What must run before either? | The **headroom probe** (sec. 8). Non-optional. |

**Nothing in this document is queued.**
