# Failure autopsy -- V3-EXQ-935a (MECH-266 / SD-032a)

**STATUS: `confirmed`** -- the interactive Step 8 gate this staging draft could not hold was held 2026-09-17 (session `failure-autopsy-batch-20260917`). Routing below is CONFIRMED.

| | |
|---|---|
| run_id | `v3_exq_935a_mech266_margin_normalised_cap_rule_20260916T095809Z_v3` |
| queue_id | V3-EXQ-935a |
| claims | MECH-266, SD-032a |
| purpose | `diagnostic` (excluded from confidence scoring) |
| outcome | FAIL -- C1 failed, C2 passed |
| self-route | `rule_right_r_wrong_requeue` |
| machine | ree-worker-3, `linux-x86_64-py3.10-torch2.12.0+cpu`, 165,148 s |
| generated | 2026-09-16T14:14:41Z |
| predecessor autopsy | `failure_autopsy_V3-EXQ-935_2026-08-18` (confirmed) |

Written headless by subagent `autopsy-staging-935a-20260916` under metaworker orchestration
session `orchestrate-20260916-1305`. **Step 8's interactive gate was not held.** Nothing was
written to `claims.yaml`, `substrate_queue.json`, `review_tracker.json`,
`hypothesis_space_registry.v1.json`, or the manifest's `evidence_direction`, and no follow-on
chip was spawned. The next `/governance` walk gates this at its Step 1.5 / 2b.

---

## 1. Facts

`check_dry_run_citations.py` over every cited id: **1 clean, 0 dry, 0 ambiguous**
(`dry_run_checked: true`, `excluded_dry_run_ids: []`).
`validate_recording.py`: **complete** -- all always-core fields present, no thin-pack
provenance drop, no criteria re-derivability finding.

Per seed: train one curriculum agent, then frozen-policy eval cells on clones. A calibration
cell at `CAP_REF = 0.75` gives that seed's baseline margin `m_seed`; `ARM_NORM` cells run at
`cap = r * m_seed` for `r` in `[2.25, 2.45, 2.65, 2.85, 3.05]`; an `ARM_ABS` control runs at a
fixed cap of 1.75. Seeds 47-51 are fully out of sample -- they played no part in deriving
`R_STAR = 2.45` or the sweep.

**Criteria.** `PASS iff C1 AND C2`.

| criterion | measured | threshold | passed |
|---|---|---|---|
| C1 rule grades at R_STAR | 0.60 (3/5) | >= 0.667 | **false** |
| C2 beats best absolute cap | 3 graded | > 1 graded | true |

**`fraction_in_external_task` per (seed, r)**, recomputed from
`interpretation.occupancy_gate.cells`. `G` = strictly inside the (0.1, 0.9) graded band.

| seed | r=2.25 | r=2.45 (R_STAR) | r=2.65 | r=2.85 | r=3.05 | graded r | calib spread (p90-p10) |
|---|---|---|---|---|---|---|---|
| 47 | 0.7098 G | 0.7312 G | 0.6899 G | 0.6716 G | 0.4243 G | 5 | 0.2484 |
| 48 | 1.0000 | 0.9617 | 0.4086 G | 0.0000 | 0.0000 | 1 | 0.0077 |
| 49 | 0.9605 | 0.8656 G | 0.8362 G | 0.7660 G | 0.8177 G | 4 | 0.2252 |
| 50 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0 | 0.0000 |
| 51 | 0.8475 G | 0.8093 G | 0.7172 G | 0.0000 | 0.0000 | 3 | 0.0401 |
| **graded / 5** | **2** | **3** | **4** | **2** | **2** | | |

The two seeds that failed C1 failed *above* the ceiling (0.9617 and 1.0000) -- external_task
still saturating at R_STAR, i.e. the cap was too tight, not too loose.

**Readiness.** All four anchors cleared 5/5 against a 2/3 floor (contact guard, drive engages,
calibration statistic alive, R_STAR cell measured); `manipulation_landed = true`. Nothing was
starved.

**H-KNIFE.** `r = 2.65` clears the seed bar (4/5), so the driver routed
`rule_right_r_wrong_requeue` rather than H-IDIO. The wiring is correct and is exactly the fix
935's autopsy asked for.

**Two facts the run records and the routing does not read:**

1. `substrate_hash_matches_v3_935 = false`. `R_STAR = 2.45` was derived on 935's substrate
   (`921d0af6...`) and tested on `3984b01e...`.
2. `interpretation.occupancy_gate` -- the stricter, substrate-specified reproducibility bar
   (>= 2 *adjacent* swept values, each mixed on >= 2/3 of seeds; the bar
   `mode-governance-engagement`'s own `failure_record` names) -- returns
   `graded: false`, `regime_shape: "mixed_not_reproducible"`, `longest_adjacent_run: 1`,
   `reproducible_conditions: [2.65]`.

**Cross-set comparison** (recomputed from 935's own `per_seed` cells; 935's
`occupancy_gate.cells` is empty):

| r | 1.85 | 2.05 | 2.25 | 2.45 | 2.65 | 2.85 | 3.05 |
|---|---|---|---|---|---|---|---|
| 935, seeds 42-46 | 1/5 | 1/5 | 2/5 | **4/5** | **4/5** | -- | -- |
| 935a, seeds 47-51 | -- | -- | 2/5 | 3/5 | **4/5** | 2/5 | 2/5 |

So `r = 2.65` grades 4/5 in **both** independent seed sets (8/10 pooled) -- a genuine
out-of-sample replication for one specific `r`. `R_STAR = 2.45` was chosen over it as "the more
conservative pre-registration" and gives 7/10 pooled. The graded-count curve is **peaked**, not
monotone: extending the sweep upward (which 935's autopsy asked for) found the window's upper
edge, and it falls off sharply above 2.65.

---

## 2. Claim layer

**MECH-266** (`mechanism_hypothesis`, provisional, `epistemic_category: standard`,
`pending_retest_after_substrate: true`) asserts asymmetric, mode-specific Schmitt-trigger
hysteresis on the SD-032a mode register.

**It was not exercised, for the eighth consecutive run.** This driver sweeps a single
*symmetric* affinity cap and contains no asymmetric-threshold arm; and
`salience_coordinator.py:514` falls back to a `1.0` exit sentinel when `exit_thresholds` has no
entry for the current mode -- always satisfied for a proper softmax. The Schmitt trigger is not
merely un-swept here, it is **inert**. MECH-266 is PERIPHERAL on this run.

**SD-032a** (`design_decision`, stable, 28 supports / 0 weakens) was not under test either: the
run self-routed H-KNIFE, which the driver pre-registered as `non_contributory` for SD-032a.
Worth recording without weight: on the live-margin seeds the register alternated genuinely (57
and 59 switches over 15 episodes at R_STAR on seeds 47 and 49), and on the saturated seeds it
produced a clean step -- which is SD-032a's own `functional_restatement` ("mode transitions are
discrete, not graded") behaving as written, not evidence against it.

Claim tags are accurate for the lineage but **over-broad for this run**: it is a calibration
step upstream of any MECH-266 test.

---

## 3. Biological reference

Closest mechanism: gain control in cortico-basal-ganglia salience arbitration -- divisive
normalisation (Carandini & Heeger; in BG via lateral inhibition / FSI-mediated pooling) -- with
the mode register as a BG action-selection analogue.

The substrate is a **formal-definition import with a live divergence**, unchanged since 935 and
unchanged in code (`git log` shows no commit to
`ree_core/cingulate/salience_coordinator.py` between 2026-08-16 and 2026-09-17):
`tick()` hard-clips each affinity input to `[-cap, +cap]` before its per-mode weight while
`external_task_bias` enters the external_task logit unclamped. A clip is scale-*sensitive* by
construction; biological divisive normalisation is scale-*free*.

**This run adds quantitative support for that divergence.** On the seeds whose external_task
probability is near-constant (935a 48/50/51; 935 45/46), `ext_margin_mean` is **linear in cap at
R^2 0.9996-0.9999** -- the signature of an input clipped at every cap tested. The clip is
erasing the within-cell variation a mixed regime needs, for those agents. Stated against the
over-read: saturation does **not** preclude grading -- 935's seeds 45 and 46 are equally
saturated and graded at 2 and 3 `r` values.

**Literature.** PRESENT for both tagged claims' own questions (6 MECH-266 hysteresis entries;
5 SD-032a salience-switching entries). ADJACENT for the gain-stage question
(`targeted_review_striatal_gain_control_bounding`; MECH-439's canonical-normalisation and
value-divisive-normalisation entries). The commissioned
`targeted_review_salience_gain_normalisation` does not exist on disk -- **and is not owed**: the
user marked the H4 lit gate satisfied by the existing corpus at a Step 8 gate on 2026-08-25
(`mech266_circling_review_20260825.md` sections 4-5, logged to `RECOMMENDATION_LOG.jsonl`).

---

## 4. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | **intact** (both); MECH-266 peripheral | no asymmetric arm; `exit_thresholds` unset throughout |
| Biological reference | **partial** | hysteresis lit present; clip-vs-normalisation divergence live and newly supported |
| Prerequisites | **present** | all four readiness anchors 5/5 against a 2/3 floor |
| Implementation | **partial** | cap functional; Schmitt trigger inert; gain stage still a hard clip |
| Environment | **partial** | 3/5 seeds ran with the affinity input clipped at every tested cap |
| Measurement | **under-instrumented -- DOMINANT** | see below |
| Integration | **coupled but unstable** | curriculum x clip x latched register; window 2 adjacent `r` wide in-sample, 1 wide out of sample |
| Scale / capacity | **likely insufficient** | n=5 against a >= 4-of-5 bar |

### The measurement layer, in detail

**(1) Power.** `MIN_FRACTION = 2/3` on n=5 is **">= 4 of 5"**: attainable fractions are
0/.2/.4/.6/.8/1.0 and the bar falls between two of them, so one seed decides the verdict. At the
generalisation rate the pooled two-set data supports for 2.45 (7/10), that bar clears with
probability **0.53**; even at 2.65's 8/10, **0.74**. The criterion cannot separate a rule that
generalises at 0.7 from one that does not, in either direction.

**(2) The graded predicate is occupancy-only, over a latched register.** `_graded(occ)` tests
`0.1 < occ < 0.9` and nothing else -- no alternation requirement. And
`salience_coordinator.py:517-523` updates `current_mode` only when
`salience_aggregate > enter_threshold AND current_mode_prob < exit_threshold AND soft_argmax !=
current_mode`, so occupancy can be pinned by the *aggregate* gate independently of the cap under
test. At R_STAR the three "graded" seeds carry 57, 59 and **24** switches over 15 episodes: 47
and 49 are genuine alternation, 51 is barely above the known-vacuous `n_switches == n_episodes`
signature this lineage was already burned by (2026-06-12). MECH-266's hysteresis lives in the
alternation, not the time-average.

**(3) The non-degeneracy flag is mis-scoped.** `criteria_non_degenerate` maps *both* criteria to
one run-level `base_non_degenerate` readiness conjunction (driver lines 1376-1383). It is
per-criterion in name only and certifies nothing about the cells that decided C1 -- and it is
exactly the field the frozen-ledger elimination bar reads.

**(4) A recorded control the routing does not consume.** `substrate_hash_matches_v3_935 = false`
is stamped as an auditable fact, correctly, and then neither the routing nor the self-route label
reads it. That is the same defect class 935 was autopsied for (H-KNIFE computed, not wired),
recurring at one remove.

**(0) FLAGGED, NOT DIAGNOSED.** Within this run, the number of graded `r` values is perfectly
rank-ordered by calibration-cell dispersion (50: 0.0000 -> 0; 48: 0.0077 -> 1; 51: 0.0401 -> 3;
49: 0.2252 -> 4; 47: 0.2484 -> 5; Spearman rho = 1.000, n=5). **It fails its first out-of-sample
check** -- see the withdrawn arguments below. Carried only as the declared null of the
zero-compute re-score leg.

### Failure location (GOV-FAILLOC-1)

| bucket | verdict |
|---|---|
| MECHANISM failed | **not established** -- implementation partial, Schmitt trigger inert |
| MEASURES failed | **not established** -- under-instrumented on four counts |
| ENVIRONMENT failed | **partial** |
| REE failed | **false** |

**Net: MIXED, MEASURES-dominant. Not chargeable to REE, and not to MECH-266.**

---

## 5. Adjudicating the self-route

The manifest's `interpretation.label` is a hypothesis, not a verdict. **Both directions:**

**For `rule_right_r_wrong_requeue`.** `r = 2.65` grades 4/5 on 42-46 *and* 4/5 on 47-51 -- a real
out-of-sample replication for a specific operating point. The pre-registration picked the more
conservative of two co-equal candidates and picked the wrong one. H-IDIO ("no rule anywhere") is
refuted, and the H-KNIFE branch that says so is the repair 935's autopsy asked for, working.

**Against adopting it as written.** (i) The run's own *stricter* bar -- the adjacency
reproducibility bar the substrate entry itself specifies -- returns `graded: false`,
`longest_adjacent_run: 1`. H-KNIFE is deliberately looser (one `r` suffices), so the re-queue
recommendation rests on the relaxed bar while the pre-registered strict one says the opposite.
(ii) The criterion is coarse and under-powered: one seed moved the verdict, and the bar clears
53-74% of the time at the rates observed. (iii) `substrate_hash_matches_v3_935 = false` -- the
constant was carried across a substrate move that the run detected and the routing ignored.

**Verdict: the self-route is CONTESTED, not refuted.** Its positive content (the rule form is
supported; H-IDIO is wrong) stands. Its implied action (re-queue at 2.65) is narrowed: see
routing.

---

## 6. Repair pathway and routing

**Primary: `queue-experiment`, sequenced.**

1. **Zero-compute re-score first** (gates the rest). Re-score the banked 935 + 935a cells (10
   seeds, 60 `ARM_NORM` cells) and report, per seed: the graded **window width in `r`** rather
   than the count of grid points hit; per-cell `n_switches` against the `n_episodes` vacuity
   floor; and the dispersion-vs-graded-count rank correlation **pooled over all 10 seeds**.
   Declared nulls: (a) the graded window at 2.65 is no wider than one grid step on >= 2/3 of
   seeds; (b) pooled dispersion rho is indistinguishable from 0. Debt class:
   `complicated (buildable)`.
2. **Then, conditional on it: a POWERED same-question re-test** at `r = 2.65`
   (alphabetic suffix, V3-EXQ-935b) with the four instrument repairs listed in
   `routing_detail.required_changes`. Debt class: `complex (probe-gated) / puzzle (known rules)`.
3. **Last, gated: the H-D substrate proposal** -- a saturating / divisive bounding operator in
   place of `max(-cap, min(cap, v))`, which is what `mode-governance-engagement` is *already
   titled for*. Its lit gate is already satisfied (2026-08-25 user decision), so what it owes is
   a proposal, not a pull.

**REFUSED:** a same-design, n=5 V3-EXQ-935b pre-registering 2.65 with no instrument repair and no
power calculation. This is a **design refusal, not a brake firing** -- see below.

**Secondary routing: none, and explicitly NOT a lit-pull** (see section 3).

**Substrate queue: `amend` on `mode-governance-engagement`, bookkeeping only** -- append one
`failure_record` item. No new build is requested. `severity` and `substrate_paths` are
deliberately left as governance has them (`cosmetic`, four paths, reassessed at
`gov-20260911-1612` / GFLAG-0262): nothing here shows the clip *corrupting* evidence.

### Draft `evidence_quality_note` text

> **MECH-266** -- [2026-09-16 | V3-EXQ-935a | failure_autopsy_V3-EXQ-935a_2026-09-16]
> `non_contributory`, diagnostic, excluded from scoring. PERIPHERAL / not exercised for the
> eighth consecutive run: V3-EXQ-935a sweeps a single symmetric `affinity_input_cap`, contains no
> asymmetric-threshold arm, and ran with `exit_thresholds` unset (the 1.0 no-op sentinel), so the
> Schmitt trigger was inert. `pending_retest_after_substrate` stays true; no `substrate_ceiling`
> attribution accrues and the re-derive brake count stays at 7.

> **SD-032a** -- [2026-09-16 | V3-EXQ-935a | failure_autopsy_V3-EXQ-935a_2026-09-16]
> `non_contributory`, diagnostic, excluded from scoring. The run routed
> `rule_right_r_wrong_requeue`, which the driver pre-registered as non_contributory for SD-032a;
> the register was not under test. Narrow non-scoring observation: it alternated genuinely on the
> live-margin seeds (57 / 59 switches over 15 episodes at R_STAR) and produced a clean step on the
> saturated ones, which is SD-032a's own "transitions are discrete, not graded" behaving as
> written. Status stays stable.

---

## 7. Gates and mechanical checks

**Re-derive brake: DOES NOT FIRE.** Count = **7** for each claim (464b, 467b, 464c, 467c, 464d,
467d, 797), obtained by running the R1-R3 recipe verbatim over the committed corpus. This target
contributes **0**: the recipe exits at the per-claim branch, because
`recommended_epistemic_category_per_claim` declares `standard` for both claims. (The clause-3
producer release is also stamped and is independently valid -- the `amend` target
`mode-governance-engagement` is recorded IMPLEMENTED, and the counter's own `landed` resolution
returns True for it -- but it is belt-and-braces, not load-bearing.)

**Granularity-debt trigger: DOES NOT FIRE.** `granularity_debt_cluster.py MECH-266` reports 11
targets across 7 files; alignment distribution `intact=6, unclear=2, weakened=2, unstamped=1`. At
least one target reads `weakened`, so the first condition holds -- but the second does not:
every target carries the **same** signature (MECH-266 is never reached, because the arbitration
is mis-calibrated: unreachable in 464b-d/467b-d, saturated in 464e/467e, mis-centred in
934/935/935a). Eight repetitions of one signature is calibration and measurement debt, not
granularity debt. Routing to `/claim-synthesis` would decompose a claim whose decomposition is
not the problem.

**Step 7b pre-routing checks: 2 fires after revision, both dispositioned.**

| check | fired on | disposition |
|---|---|---|
| C1 | 3 unlettered drivers | **Partly FALSE and dismissed.** 464 and 467 *did* score (twice each, 2026-04-21), with a non-canonical `_v3_<stamp>_v3` run_id tail that the checker's lookup appears to miss; 455a genuinely never scored. All three are 2026-04-era drivers predating `use_external_task_drive`. Cleared by naming them. |
| C3 x2 | MECH-266 + SD-032a lit | **Dismissed -- correctly-scoped `ABSENT`.** C3 cannot read scope; the entries it names are the ones this artifact declares PRESENT. The ABSENT clause is scoped to the gain-stage question only. |

**Step 7c adversarial red-team: VERDICT `CONTESTED`**, run in the foreground on **fable**
(cross-model: this drafting session is Opus 5), reasoning withheld. It independently recomputed
the C1-per-`r` table, the cross-set 4/5 figures, the adjacency verdict, the 0.528 / 0.737 power
figures, the R1-R3 brake recipe, and both `change` tails -- all matched. **Four of its five
findings changed what this artifact asserts**, and one of them caught a closed user decision
being re-opened.

---

## 8. Withdrawn arguments

Recorded rather than deleted: an argument tested and dropped is a signal to the next session.

**W1 -- "~1 seed in 5 is structurally un-gradeable at any cap; 4/5 is a population ceiling;
SPLIT the eliminated H2."** Withdrawn. 935's seed 42 is not a second instance (its external_task
probability *varies*, spreads 0.098-0.173, and 935's confirmed autopsy already recorded its zero
graded count as an untested-range fact). The prose absolute "3/5 seeds fall to exactly 0.0 with
no intermediate" is contradicted by this run's own cells -- seeds 48 (0.4086) and 51 (0.7172)
pass through interior values first; only seed 50 is a pure step. And for seed 50 alone,
"structural" is not distinguishable from "window narrower than the grid": its transition lies in
the untested cap interval (0.988, 1.063). Kept as an observation with no disposition.

**W2 -- "within-cell dispersion, not the cap/mean ratio, governs gradedness."** Withdrawn as a
diagnosis. rho = 1.000 within 935a; **rho = -0.05** on 935's seeds 42-46, where the baseline
*mean* margin -- the quantity this argument called the wrong moment -- orders them at
**rho = -0.975**. 935's seed 44 is a direct counterexample: calibration spread 0.0004, yet
0.16-0.32 at the swept caps, and graded at 2 `r` values. Dispersion measured at `CAP_REF` is
itself cap-dependent. Retained as a flagged observation and as a declared null.

**W3 -- "route a reframed redesign under a new EXQ number; refuse any re-queue at 2.65."**
Withdrawn/narrowed. The redesign was keyed on W2's covariate and falls with it; the blanket
refusal was over-broad. The surviving grounds argue against a *same-design n=5 re-pose*, not
against a powered re-test.

**W4 -- "935's lit-pull commission is still owed."** Withdrawn. The user closed it on 2026-08-25.

---

## 9. OWED to `/governance` (nothing below was applied)

1. **Gate this draft** and flip `status` to `confirmed` (or revise). Step 8 was not held.
2. **Apply `per_claim_recommendation`** -- both claims: `diagnostic_evidence_adjudicated: true`
   (neither currently carries the field), direction `non_contributory`, category `standard`,
   plus the drafted `evidence_quality_note` text. MECH-266 keeps
   `pending_retest_after_substrate: true`.
3. **Set `evidence_direction`** on the manifest / index for this run (this skill does not).
4. **Mark the run reviewed** in `review_tracker.json` (this skill does not).
5. **Amend `mode-governance-engagement`** with the drafted `failure_record_entry`; leave
   `severity` / `substrate_paths` unchanged.
6. **Decide two flagged discrepancies**, both left exactly as found:
   (a) `mode-governance-engagement` is *titled* for the clip -> normalising-operator replacement
   and marked `implemented_pending_validation` / `cosmetic` / `ready: true`, while the hard clip
   is still in the code; (b) `criteria_non_degenerate` is a run-level flag that the frozen-ledger
   elimination bar reads as a per-criterion certificate.
7. **Frozen ledger** (`hypothesis_space_registry.v1.json`, NOT written): three basis addenda
   only -- H1 (strengthened, bar not met), H3 (three new instances of its family), H4 (new
   quantitative support). **No new leg and no denominator change is proposed**; the growth
   restriction on `mech266_mode_arbitration_saturation` was checked and is absent/null.
8. **Chip the follow-on.** This session deliberately spawned none (CLAUDE.md: a
   `/failure-autopsy` session does not chip follow-on off its own unreviewed finding).
   Governance chips the re-score leg and, conditional on it, the powered re-test.

---

## 10. Step 8 gate -- held 2026-09-17 (this was written as a staging draft)

The staging run could not hold Step 8; the gate was held interactively on 2026-09-17 by the `failure-autopsy-batch-20260917` session, which also re-verified the draft before putting it to the user:

- **Dry-run gate**: re-confirmed clean (4 ids, 0 dry).
- **Re-derive brake**: re-counted with the R1-R3 recipe over the committed corpus -- **7** for each claim, this target contributing **0**. Does not fire.
- **`change` tails**: both end on `diagnostic_evidence_adjudicated: true`, and the claim registry was checked at confirmation time -- **neither MECH-266 nor SD-032a currently carries that field**, so both tails are actionable and not already-true (the A-24 trap).
- **Step 7b re-run against current state**: the same **two C3 fires** and, notably, **no C1 fire** this time. The draft's dispositions stand.

**USER DECISION: CONFIRMED AS-IS**, including the C3 literature-scope dismissal. C3 cannot read scope and fires identically on a flatly-false `ABSENT` and on a correctly-scoped one; the user adjudicated that this artifact's `ABSENT` is correctly scoped to the gain-stage question only, and that the 2026-08-25 closure of the lit commission stands.

**One factual slip corrected at confirmation.** The ledger-pending note said the question "already carries three fan-out growth events against one elimination". The registry carries **one** (`initial_frozen_count` 4 vs `initial_frozen_count_at_registration` 3). The restraint conclusion it argues for -- propose no new leg and no denominator change -- is unchanged, and if anything rests on slightly weaker grounds than the draft claimed.

**Ledger addenda applied by the confirming session.** The three Mode-B basis addenda (H1 strengthened but bar not met; H3 three new instances of its family; H4 new quantitative support) are now written to `hypothesis_space_registry.v1.json` as `basis_addenda` entries on the existing legs. **No state change, no new leg, no denominator change** -- `initial_frozen_count` stays 4. The growth-restriction check was re-run at apply time and the field is absent/null, as the draft recorded.
