# Failure autopsy (diagnostic adjudication) -- V3-EXQ-1012a, MECH-439 commensurability selection-level validation

- **Status:** `awaiting_human_confirmation` -- **STAGING-MODE DRAFT**, headless. Routing is NOT finalised; the Step 8 interactive gate is OWED.
- **Generated (UTC):** 2026-09-15T00:35:57Z
- **Session:** `autopsy-staging-trio-20260914` (dispatched by metaworker orchestrator `orchestrate-20260914-2323`)
- **Scope:** single
- **Target:** `v3_exq_1012a_e3_commensurability_selection_level_regime_validation_20260914T221427Z_v3` (queue_id `V3-EXQ-1012a`)
- **Trigger:** `experiment_purpose: diagnostic`. A **PASS** -- exactly the case the blanket diagnostic trigger exists for.
- **Dry-run gate:** `check_dry_run_citations.py` on the run_id, `V3-EXQ-1012a` and `V3-EXQ-1012`: `0 dry cited, 0 dry in named families, 0 ambiguous, 1 clean, 0 unknown`. `dry_run_checked: true`, `excluded_dry_run_ids: []`.
- **Step 9b:** nothing owed -- see section 10.
- **Headline governance fact:** the **re-derive brake FIRES** on MECH-439 at **15** counted hits against a threshold of 2. What that does and does not mean is section 7c -- it does **not** condemn this run.

---

## 1. Facts (no interpretation)

### 1a. What the run is, and why it exists

`SD-E3-CHANNEL-COMMENSURABILITY` (MECH-439 rung 3, `ree_core/predictors/e3_selector.py`, IMPLEMENTED 2026-09-07) divides each declared E3 channel's per-candidate term by a running EMA of that channel's own cross-candidate standard deviation before the additive sum, so channel authority is decided by content rather than by units. It exists because the confirmed `failure_autopsy_V3-EXQ-571c_2026-09-02` measured one channel holding 0.98-0.99999 of the cross-candidate variance in 15 of 16 cells.

Its original readiness target -- ">= 2 channels simultaneously above a 1e-3 relative cross-candidate share" -- was found on 2026-09-08 to be **an arithmetic identity of the operator it was meant to validate**: dividing each channel by its own SD drives every share toward `1/k`, so the build-time ON row (`n_live 2, top_share 0.500000` = exactly 1/2) is the identity's fingerprint, not an effect. `/governance` GFLAG-0234 (option A, user-approved 2026-09-10, REE_assembly `5dc661badc`) **amended the target** to a **selection-level DV: commit-flip rate under shadow OFF/ON scoring on the same tick and the same candidate set**, and marked the rung **"IMPLEMENTED but UNVALIDATABLE AS SPECIFIED"**. The original V3-EXQ-1012 was parked, never queued.

**V3-EXQ-1012a is the instrument built for that amended target.**

### 1b. Design

Two arms, **both with the operator ON always** -- `C_fed_operator_on` (residue fed per step) and `C_starved_operator_on` -- x 4 seeds (42, 43, 45, 46). Per cell: 60 P0 warmup episodes, then P1 to a `fresh_select_target` of 200 genuine latch-gated selections (episode cap 40, 200 steps/episode). Every `score_trajectory` call is captured, then replayed twice per genuine tick:

1. **SHADOW (toggle OFF)** -- the counterfactual with the operator disabled. `primary_argmin_flip = 1` iff `argmin(shadow) != argmin(live)`.
2. **SELF-CHECK (toggle to the SAME value)** -- a harness-bug detector. With the EMA state frozen, replaying at the live config value **must** reproduce the live scores exactly, or the driver refuses to report.

`xcand_commit_flip_rate` per cell = mean `primary_argmin_flip` over every genuine P1 tick.

### 1c. What the manifest reports

| arm | seed | P1 eps | n_fresh | n_latched | yield | **flip rate** | mean abs delta (live vs shadow) |
|---|---|---|---|---|---|---|---|
| fed | 42 | 18 | 209 | 126 | 0.624 | **0.9856** | 4633.6 |
| fed | 43 | 7 | 201 | 1199 | 0.144 | **0.7413** | 2000.4 |
| fed | 45 | 9 | 258 | 956 | 0.213 | **0.7132** | 9207.2 |
| fed | 46 | 21 | 220 | 222 | 0.498 | **0.8455** | 3800.1 |
| starved | 42 | 40 | 158 | 934 | 0.145 | **0.9177** | 5339.1 |
| starved | 43 | 10 | 200 | 1800 | 0.100 | **0.3400** | 12509.7 |
| starved | 45 | 17 | 205 | 1718 | 0.107 | **0.9366** | 12867.4 |
| starved | 46 | 32 | 205 | 1289 | 0.137 | **0.7024** | 2572.5 |

**Criteria** (both load-bearing, both passed):

| criterion | role | measured | bar | rule |
|---|---|---|---|---|
| `flip_rate_lift` | verdict | fed **0.8214**, starved **0.7242** | fed **0.2137**, starved **0.4803** | PASS iff **either** regime individually passes |
| `self_check_clean` | instrument correctness gate | 0.0 failures | 0.0 | 0 failures across 8 cells |

`regimes_differ: true` (gap 0.0972 against a `REGIME_DIFFERENCE_FLOOR` of 0.02). `non_degenerate: true`. `outcome: PASS`. `evidence_direction: "diagnostic"`.

**Per-arm gate:** `green_arms = [C_fed_operator_on, C_starved_operator_on]`, `red_arms = []`, no structurally vacuous arms. Four named readiness preconditions per arm -- `decomp_samples_sufficient` (worst seed 201 vs floor 60), `operator_engaged`, `clamp_config_landed`, `residue_protocol_landed` -- plus `shadow_scores_measurably_different`.

**Channel scale estimates**, the quantity the operator divides by (fed seed 42): `f_weighted 6.63e-05`, `harm_weighted 2.57e-03`, `residue_weighted 0.675`, `benefit_weighted 0.0`, `goal_weighted 0.0`. The regime manipulation landed cleanly -- `residue_weighted` runs **0.48-6.03 fed** against **9.3e-05-6.9e-04 starved**, a ~4-order-of-magnitude separation.

### 1d. Recording provenance

`validate_recording.py`: **1 complete, 0 always-core gaps** -- the only one of the three manifests in this staging batch with none. `config`, `seeds`, `elapsed_seconds` (7381.9 s), `recording_schema rec/v1`, `substrate_hash`, `substrate_commit` (clean), `substrate_identity`, `machine ree-cloud-2`, `machine_class linux-x86_64-py3.10-torch2.12.0+cpu`, plus an `arm_fingerprint` per cell. One advisory finding: two load-bearing criteria with no top-level `combination_rule` (though `flip_rate_lift` carries its own).

### 1e. Expected vs observed, and which criterion failed

**None failed.** The adjudication is not about a failed criterion -- it is about **what the passing criterion can support**.

---

## 2. Claim-layer mapping

| Field | MECH-439 |
|---|---|
| claim_type | `mechanism_hypothesis` |
| status | `candidate` |
| epistemic_category | `standard` |
| `pending_retest_after_substrate` | **true** |
| `diagnostic_evidence_adjudicated` | **true** |
| `evidence` | **0 entries** |
| `live_status.evidence.from` | `failure_autopsy_V3-EXQ-571b_2026-09-01` |

**Did the experiment test the claim under conditions where it could express itself? No -- and it was never meant to.** MECH-439's `what_would_answer` requires F's E3 committed-selection-variance share measured per arm against **both** a collapsed-proposer control **and** a matched-noise control with non-zero cross-arm variance on committed-action-class entropy. None of that is instantiated. This run is the **acceptance instrument for a substrate rung**, and the driver states the boundary itself in `outcome_note`: *"MECH-439's direction does not move on this record: this run says only whether the operator's rescaling changes which candidate the primary score alone would prefer, not whether it does or does not 'work'."*

`non_contributory` is correct. No claim-layer field moves.

---

## 3. Biological-reference triage

**Closest reference mechanism:** divisive normalisation / gain control at a value-integration stage, so heterogeneous afferent channels compete on content rather than on the accident of their units.

**Faithful translation or formal import?** Faithful in kind -- not a formal-definition import, and the normalisation-model literature is adjacent and well known. **No `/lit-pull` commission is the primary output here.**

**Two divergences, recorded rather than adjudicated:**

- **(a)** Equalising cross-candidate SD is *a* normalisation, not obviously *the* one. The biology motivates gain control; it does not prescribe equal variance. That target is a strong and, in this lineage, unargued commitment about what "commensurable" should mean.
- **(b)** The third dependency of the reference mechanism -- that the channels are live enough to be worth normalising -- is **empirically unmet here**: two of the five declared channels carry a scale estimate of exactly `0.0` in all 8 cells (section 5d).

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **not exercised** | correctly so -- substrate acceptance instrument, not a claim test |
| Biological reference | **partial** | faithful in kind; the equal-variance target is unargued, and 2/5 channels are dead |
| Dependency prerequisites | **present** | operator implemented; clamp and residue protocols asserted per cell; regime manipulation landed |
| Implementation completeness | **complete** | one of the better-instrumented drivers in the corpus -- see 5f |
| Environment adequacy | **adequate** | the full 571/936-lineage 12x12 reef configuration; fed/starved is a genuine manipulation |
| Measurement adequacy | **under-instrumented** | **the dominant layer** -- about *interpretability*, not correctness (5b, 5c, 5e) |
| Integration adequacy | **isolated by design** | primary-score stage only; the driver is explicit that this is a scoping decision |
| Scale / capacity | **adequate denominator, thin between-seed** | 158-258 fresh selections/cell vs a floor of 60; but only 4 seeds, which is what makes 5c fragile |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Established? |
|---|---|
| MECHANISM FAILED | not established |
| MEASURES FAILED | **not established** (measurement reads `under-instrumented`) |
| ENVIRONMENT FAILED | established (environment reads `adequate`) |
| REE FAILED | **false** |

**Net: MEASURES -- single-bucket, not chargeable to REE.** This is a PASS, so no organism-level failure read is in play; the classification is recorded because the skill requires it before any prose could describe REE as having failed, and nothing here does.

---

## 5. The diagnosis

### 5a. What the run legitimately establishes

The operator is **not a no-op at the primary-score selection stage**. That is a real result, it is what the amended target asked for, and the instrument that produced it is sound (5f). It is also a *necessary and much weaker* thing than "the operator works".

### 5b. Not-an-identity is not interpretable -- the central adjudication

The driver argues, correctly and at length, that this DV escapes the defect that sank the original target: only a **common** positive rescaling of every channel is provably argmin-invariant; this operator rescales each channel by a **different** factor; so whether an argmin flips is a genuine function of the data with no closed form forcing it. That is right, and it is why the amended target was a real improvement.

**But escaping identity-hood is weaker than being interpretable.** There is no measured reference against which 0.82 can be graded. Nothing in the run says what an *uninformative* differential rescaling would produce on this substrate, so the number establishes that the operator moves the argmin and stops there.

**The first draft of this autopsy argued that point badly, and the argument is withdrawn rather than quietly edited.** It reasoned that OFF and ON rankings are computed over "effectively disjoint information" -- OFF decided by residue alone, ON by an equalised three-way sum -- and therefore agree at roughly chance, `1/k`, making 0.82 unremarkable. **That premise is false:** the ON score *retains* residue, at roughly 1/3 weight rather than at monopoly weight, so the two rankings are correlated, not independent. Under genuine independence at `k=8` the flip rate would be about **0.63**, and the observed **0.82 exceeds it**. If anything that is mildly favourable to the operator.

So the honest statement is the narrow one: **there is no measured null, so the number cannot be graded** -- not that the number is at chance. (The candidate count `k` is also not recorded in the manifest, which is a recording gap in its own right and the reason no analytic correction is available even in principle.)

**What the missing reference should be** -- and *not* the construction this artifact first proposed, which is withdrawn in 5c-bis below.

### 5c. The verdict criterion is effectively unfailable -- and this artifact's own first draft understated it

The first draft of this autopsy described `flip_rate_lift` as `mean_rate > 2 * sd` -- a coefficient-of-variation test against a bar derived from the same four seeds. That is half of it. **The driver's actual predicate is weaker in two compounding ways:**

```
bar    = max(FLIP_RATE_SD_MULTIPLIER * sd, FLIP_RATE_ABS_FLOOR)   # 2.0, 0.01
passed = mean_clears_bar OR majority_clears_floor                  # floor = rate > 0.01
```

Any arm in which **half the seeds flip the argmin more than 1% of the time** passes on the second disjunct alone, whatever the first says -- and the manifest's own `criteria[0].detail` records `majority_clears_floor: True` for **both** arms.

**Further: every *content* branch of the verdict ladder emits PASS**, including `operator_selection_inconsequential_primary_stage`. The only FAIL branches are instrument-defect, arm-gate-red, and the hidden-identity flag. So **`outcome: PASS` carries no information about the direction of the measurement at all.**

A self-derived bar is a legitimate consistency check; it must not be the only gate on a DV whose magnitude is the finding, and a disjunct that cannot fail should not be in the predicate at all. Recorded as a correction to this artifact's own first draft, not only to the driver: **reading a criterion's reported cells is not reading its predicate**, and the two differed here.

**Hygiene on the same criterion** (recorded so a later recompute does not read as a discrepancy): the reported `sd` is the **population** sd, not the sample sd. Fed 0.10687 is `pstdev` (sample `stdev` is 0.12340); starved 0.24013 is `pstdev` (sample 0.27727). At n=4, `pstdev` under-estimates by `sqrt(3/4) = 0.866`, so the bar sits ~13% below a sample-sd bar. Recomputed both ways: fed 0.8214 clears both 0.2137 and 0.2468; starved 0.7242 clears both 0.4803 and 0.5545. **Neither verdict flips**, so this is hygiene, not a finding -- but the successor should pick the convention deliberately and say which.

### 5c-bis. The placebo this autopsy first proposed was a straw null -- withdrawn

The first draft recommended, as the missing reference, a **permutation of the fitted per-channel scales across channels** -- argmin-affecting, magnitude-matched, information-free. The magnitude-matching is exactly what breaks it.

From this run's **own** fed seed-42 scales (`f 6.63e-05`, `harm 2.57e-03`, `residue 0.675`), a permutation does not *equalise* the channels; it installs a **new monopoly**. Four of the five non-identity permutations leave `residue_weighted` the monopolist by ratios from 6.8 to 4e5 -- i.e. they reproduce the OFF ranking, so the placebo's flip rate would be near zero -- and the fifth crowns harm at 39:1. **None equalises.** So "operator flip rate > placebo flip rate" could not have failed: the autopsy would have shipped, as its repair, **the same defect class the tautology doc found in the target it was repairing**.

Recorded rather than silently swapped, because the near-miss is the lesson: **a null must be checked against the run's own measured scales before it is recommended**, not argued for in the abstract.

**The replacements** (section 7a, change 1), neither of which has this property:

- **Preferred, and it needs no new arm at all** -- the construction the prior tautology finding already recommends (`exq1012_blocked_readiness_target_tautological_20260908.md`, option 2): **per-channel argmin agreement with the commit, OFF vs ON**. This asks whether the operator moves the committed candidate *toward a consensus of the individual channels' own preferences*, rather than merely moving it -- a statement about whether the re-weighting is principled, not just consequential. It is computable from the per-candidate per-channel terms the shadow replay already captures. **That it was already on record and was not carried into 1012a is itself worth noting at the gate.**
- **If a null arm is still wanted** -- a **tick-shuffled scale estimator**: divide each channel by an estimate of *its own* scale taken from a different tick. This preserves the operator's equalising structure exactly (every channel still ends near unit spread, so it is not a new monopoly) while destroying the tick-local content that is supposed to be doing the work.

### 5d. Two of five declared commensurability channels are structurally dead in every cell

`benefit_weighted` and `goal_weighted` carry a scale estimate of **exactly 0.0 in all 8 cells**. The first draft read that as "no cross-candidate spread on any tick", which is true but misleading: **their branches were never entered at all.** The benefit branch is never fed by this driver's warmup, and the goal branch is never active -- the manifest's own `z_goal_stream` reads `ticks_active: 0` and `active_frac: 0.0` against `writer_calls: 53837`. They are not low-variance channels; they are **absent** ones.

**The substrate handles this correctly, and I checked the source rather than assuming.** `_commensurability_scale` returns the `1.0` no-op for any channel whose estimate sits at or below `e3_commensurability_floor`, with the docstring giving exactly this reason: *"a structurally-dead channel divided by its own near-zero spread would otherwise explode."* **So there is no blow-up.**

The finding is **scope, not correctness**: the operator, whose declared job is to make channel authority a contest, arbitrated among **3 live channels rather than the 5 it declares** -- and `goal_weighted` was dead despite the arm config carrying `z_goal_enabled: true` and `goal_weight: 0.5`. Anything this run says about the operator is said about a 3-channel instance of it. **The cause matters for the successor: reviving those channels is a harness change, not a tuning one.**

### 5e. The driver's docstring promises a readout the build does not emit -- and it is the one that bounds the DV's reach

The docstring states that `final_commit_by_primary_frac` *"is recorded per cell (matching the parked driver's own C6 diagnostic) as **mandatory interpretive context**"*, and explains exactly why it matters: on a cell where it is low, a primary-stage flip rate does not tell you whether the operator changed the **executed** action.

It is **absent from `arm_results`** (whose 27 keys are listed above), and both `outcome_note` and `custom_information.build_scoping_decision` say it was *"deliberately not carried in this build"*. So the build scoping decision is honestly recorded in two places and **the docstring is stale relative to it**.

The consequence is real: this run measures flips at the primary-score stage and **nothing relates them to the action the agent took**. A reader who trusts the docstring will believe that bound exists.

**Related, and its own finding:** `mean_abs_score_delta_live_vs_shadow` (2000-12867) is **not a decision-relevance measure**, and the `shadow_scores_measurably_different` readiness precondition leans on it. That precondition was added by the driver's own Step 4.5 red-team (finding 4a) to close a real gap -- `operator_engaged` is a pure tick-count gate and would read green even if every channel's EMA sat at or below the floor, leaving `live == shadow` identically. The intent is right. But the statistic measures score **movement**, and the driver's own DV-symmetry declaration states that a per-tick offset uniform across candidates is *"correctly invisible, argmin-invariant"* -- so a large delta can be produced by a common-mode component that provably cannot change any decision. The magnitudes here are explained by `f_weighted`'s scale sitting at ~1e-04, so its term is multiplied by ~3,600-15,000. **No harm materialised** (the flip rate is high, so decision movement plainly did occur), but the check certifies score movement where the thing it guards is decision movement -- and the decision-relevant quantity is already the DV.

### 5f. What this driver got right

Recorded because it is the standard the rest of this batch should be read against.

- **Recording is COMPLETE** -- the only one of the three manifests in this staging batch with no always-core gap.
- **The shadow comparison is intra-tick** on captured calls with the EMA state frozen, so the counterfactual is genuinely same-tick and same-candidate-set.
- **The self-check replay is a working instrument-correctness gate, not a decorative one** -- it must reproduce the live scores exactly or the driver refuses to report, and it found **10/10 failures in its own pre-fix smoke** against **0/8 here**.
- **Readiness is asserted per arm** with four named preconditions including `clamp_config_landed` and `residue_protocol_landed`, both of which guard against the silent-kwargs class of failure.
- **The regime manipulation demonstrably landed** (`residue_weighted` 0.48-6.03 fed vs 9.3e-05-6.9e-04 starved).

### 5g. Two emission defects

- **`evidence_direction: "diagnostic"` is not merely a dead letter -- it is currently scoring this run as `supports` for MECH-439 in the LIVE index.** The first draft got the mechanism half right and the consequence badly wrong. The chain, every link verified in source and in the landed index:
  1. `build_experiment_indexes._normalize_direction` allows exactly `{supports, weakens, mixed, unknown, superseded, non_contributory, inconclusive, does_not_support}` and returns `unknown` for anything else -- so `"diagnostic"` becomes `unknown`.
  2. `direction_explicitly_set` is computed as `bool(manifest.get("evidence_direction_note"))`, and **this manifest carries no `evidence_direction_note`** (nor an `evidence_direction_per_claim`), so the flag is `False`.
  3. The indexer then **re-infers**: `if inferred_direction == "unknown" and not run.direction_explicitly_set: inferred_direction = "supports" if run.final_status == "PASS" else "weakens"`. The run is a PASS.
  4. The result is live in `evidence/experiments/claim_evidence.v1.json` **right now**: `claim_id: MECH-439`, `evidence_direction: "supports"`, `confidence: 0.75`, `confidence_rationale: "PASS with supporting direction"`, `adjudication: "verified"`.

  So a run whose own driver says *"MECH-439's direction does not move on this record"* is recorded in the index as **verified supporting evidence for MECH-439** -- on a claim simultaneously under a fired re-derive brake at 15 ceiling hits. The **only** thing keeping it out of the posterior is `scoring_excluded: "diagnostic_probe"`.

  **The fix is cheap and must be both halves:** emit `evidence_direction: non_contributory` (in the allowed set, so no normalisation loss) **and** emit an `evidence_direction_note` (which sets `direction_explicitly_set` and blocks the re-inference outright). Either alone helps; only both close it.

  This is the same failure family as the `claim_directions` dead letter the confirmed `failure_autopsy_V3-EXQ-1004_2026-09-05` found one lineage over -- and it is **worse**, because this one does not merely fail to record an intent, it records the opposite of it.
- **`regimes_differ: true` is a non-forced-ness flag whose name oversells it.** The driver's prose is precise -- the check exists so a DV reading identically in both regimes would be caught as evidence of a hidden identity, hence the 0.02 floor. But the emitted field reads `true` on a gap of |0.8214 - 0.7242| = 0.0972 against per-seed sds of 0.107 and 0.240, which is deep inside noise. Nothing here turns on it and the driver did not overclaim; the **emitted field name** should match the prose.

---

## 6. Cluster pattern

Not a cluster. Single target.

---

## 7. Learning extracted and repair pathway

### 7a. Routing

**Work-graph debt class: `complicated (buildable)`** -- and here, unlike the other two autopsies in this batch, **the routing and the work-graph mapping agree**: `complicated (buildable)` maps to the missing/immature-substrate row and the primary routing **is** `/implement-substrate`. It is also what the fired brake mandates. The buildable work is named and has no open question.

**Primary routing: `/implement-substrate` against `f_dominance_conversion_ceiling`** (the substrate_queue entry into which the SD-E3-CHANNEL-COMMENSURABILITY rung is folded), `action: amend`.

A successor **measurement** (V3-EXQ-1012b) implementing the placebo arm is the natural instrument -- but it must be queued by `/governance` as **substrate-validation work off the amended target, NOT as a MECH-439 test**. That distinction is not pedantry: the re-derive brake refuses the latter and permits the former, and 1012a's own driver navigated exactly this line correctly at queue time.

**Required changes for the successor:**

1. **Supply the missing reference -- and not with the permutation placebo, which is withdrawn** (5c-bis). Preferred: the prior tautology doc's own **option (2)**, per-channel argmin agreement with the commit OFF vs ON, which needs **no new arm**. If a null arm is still wanted: a **tick-shuffled scale estimator** (each channel divided by its own scale from a different tick), which preserves equalisation while destroying tick-local content. Pre-register the margin.
2. **Fix `evidence_direction`, in both places -- highest priority in this list, because the defect is LIVE rather than latent.** Emit `non_contributory` **and** an `evidence_direction_note`; consider `evidence_direction_per_claim` too. See 5g.
3. **Fix the verdict predicate, not just the bar.** Remove the `majority_clears_floor` disjunct (or demote it to a diagnostic) -- it makes the criterion effectively unfailable. State in a `combination_rule` that `outcome` is not directional for this measurement. If a self-derived bar is retained, pick the sd convention deliberately -- the current one is the population sd over 4 seeds.
4. **Record the candidate count `k` per tick** (its distribution, not a nominal config value) -- the denominator of every chance-agreement baseline anyone will compute from this DV.
5. **Emit `final_commit_by_primary_frac` per cell**, or state its absence in the manifest rather than only in the docstring. Whichever way it resolves, docstring and build must agree.
6. **Rename the emitted `regimes_differ` field** to match the prose it implements.
7. **Report which commensurability channels were live, and why a dead one is dead** -- two of five were dead here, and the cause was that their branches were never entered, which makes reviving them a harness change rather than a tuning one.

**Explicitly NOT recommended:**

- **REFUSED, and this is the brake's own refusal rather than a preference:** do **not** queue another lettered iteration testing MECH-439's hypothesis against the same substrate. A redesign testing a **different** mechanism under a new EXQ number with different `claim_ids` remains permitted, and so does substrate-validation work like the successor above; another letter circling the same ceiling does not.
- Do **not** read the PASS as evidence that the commensurability operator *works*.
- Do **not** change this entry's `severity` or `substrate_paths` -- the amend is to the target and the failure record.
- Do **not** treat the V3-EXQ-571c failure record as closed. `resolves_prior_failure_record` records it as **`open`** with a context note (revised down from the first draft's `superseded`, which was overreach: nothing here replaces 571c's read).
- Do **not** build the final-commit-level replay as part of the successor unless governance scopes it separately. The driver's estimate (an `e3_selector.py` refactor, or ~150 hand-duplicated lines needing re-audit on every future change) is credible, and it is different work from the placebo arm.

### 7b. Substrate routing -- `amend` `f_dominance_conversion_ceiling`

**Amend, not create:** the SD-E3-CHANNEL-COMMENSURABILITY rung has no separate entry -- its `readiness_target` and its "IMPLEMENTED but UNVALIDATABLE AS SPECIFIED" status already live on `f_dominance_conversion_ceiling` (severity `corrupting`, `status_phase: build_owed`, 27 failure records).

What to record:

1. **The amended target got its instrument, and the instrument is sound.** V3-EXQ-1012a delivered the selection-level DV GFLAG-0234 specified, and it is **not** an arithmetic identity -- which was the defect that sank the original target.
2. **But the amended target is still not sufficient as specified, for a different reason than the first one failed:** it names a statistic with **no reference value**. *Proposed amendment:* require the flip rate to be read against a **placebo differential rescaling** (5b).
3. **Record the two scope bounds 1012a itself names** -- the DV is primary-stage only with `final_commit_by_primary_frac` unemitted, and 2 of 5 channels were structurally dead.
4. **Note for the gate, carried over from the V3-EXQ-1038 autopsy landed the same day:** this entry reads **CLOSED** to `/queue-experiment` Step 2.5c, because `check_substrate_path_overlap.py` decides OPEN vs CLOSED from the `status` **string** and this entry's status contains `VALIDATED`. So despite `severity: corrupting` and `status_phase: build_owed`, **it gates nothing**. That is a governance decision, not this autopsy's to make -- but any amend should be made knowing the severity is currently unenforceable.

`severity` and `substrate_paths` are left **unchanged**, exactly as governance has them; this run surfaces no new corrupted file.

**`resolves_prior_failure_record` leaves the V3-EXQ-571c item `open`** -- revised down from the first draft's `superseded` after the Step 7c red-team judged that overreach, and the judgement is accepted. 1012a supplies a sound *instrument* for the amended target, but `superseded` means a later run *replaced* the prior item's read, and nothing here replaces 571c's: the monopoly finding stands untouched and the validation is still owed, now for a second reason. Recorded as **context** on the item, not a state change.

### 7c. Re-derive brake (MOVE-3) -- **FIRES**, at 15 against a threshold of 2

R1-R3 recipe run 2026-09-15 over the confirmed corpus (unsettled statuses skipped). The 15 counted slugs span 2026-06-19 to 2026-09-02 and cover three lineages: the **689/700/709/711/713** learned-gating and cross-loop-arbitration work, the **936/936a** f-variance-share work, and the **571b/571c** monopoly-presence work.

What that record says is that MECH-439 has been approached from many directions and has **never once been tested under conditions where it could express itself** -- every reading is a ceiling or a non-contributory instrument finding.

**Three things the firing does and does not mean,** stated because the stamp is easy to misread:

1. **It does NOT condemn V3-EXQ-1012a.** This run adds **0** to the count (its per-claim category is `standard`, which the counter's per-claim short-circuit excludes), and it is not the thing the brake exists to stop. The brake stops a claim being re-tested at the same granularity against the same substrate ceiling, letter after letter; **this run is the acceptance instrument for the upstream substrate rung, which is the work the brake routes *to*.** The driver's own `custom_information.brake_count_note` reached the same queue-time determination and was right to.
2. **It DOES bind the follow-on** -- which is why the stamp is here rather than omitted. No lettered re-queue testing MECH-439's hypothesis may be recommended out of this autopsy, and none is.
3. **The brake's mandated route and this autopsy's independently-derived route converge** on the same place: `/implement-substrate` against `f_dominance_conversion_ceiling`. That convergence is a reason to trust the routing.

### 7d. Granularity-debt recurrence trigger -- does **not** fire

`granularity_debt_cluster.py`: MECH-439 carries **20 tagging targets**, alignment distribution `intact=8, unclear=8, other=2, n/a=1, strengthened=1`. **No target reads `weakened`.** The reader's caution about the 2 free-text targets was discharged by reading both strings -- `failure_autopsy_f-dominance-conversion-cluster_2026-06-20` reads *"strengthened (convergence is positive-adjacent evidence; not a counted supports; stays candidate)"*, the opposite of weakened, and `failure_autopsy_grandfathered-r5-batch23-mixed-findings_2026-08-08` reads *"n/a, already reconciled"*.

Per the skill's own rule, a cluster with no `weakened` target is measurement or implementation debt rather than granularity debt, **however many autopsies exist** -- and 20 is a lot, which is exactly the case that rule is written to stop over-firing on. This is the **re-derive brake's** territory (and the brake does fire), not `/claim-synthesis`'s: the signatures do not differ structurally, they are one long measurement-and-substrate story about the same score-scale monopoly.

### 7e. `pending_retest_after_substrate` and the narrow-supports check

`pending_retest_after_substrate` **stays true** -- this run is the substrate rung's acceptance instrument, not the claim's retest, and the retest MECH-439's `what_would_answer` describes has still never run.

The paired narrow-supports check was run, as the skill requires alongside a non-contributory / substrate-limitation reading: **MECH-439's `evidence` list is empty (0 entries)**, so there are no existing "supports" that could be narrow or single-pathway. The flag is false because there is nothing to flag, not because a check was skipped.

---

## 8. Draft `evidence_quality_note` for governance

> [2026-09-14, V3-EXQ-1012a, PASS, diagnostic] The acceptance instrument for SD-E3-CHANNEL-COMMENSURABILITY's AMENDED readiness target (GFLAG-0234, /governance option A, user-approved 2026-09-10), superseding the parked V3-EXQ-1012 whose original share-based target was found to be an arithmetic identity of the operator it was meant to validate. NOT a test of MECH-439 -- non_contributory, and the driver's own outcome_note says so: "MECH-439's direction does not move on this record." WHAT IT ESTABLISHES: the operator is not a no-op at the primary-score selection stage. Shadow OFF/ON replay, intra-tick with the EMA state frozen and a self-check replay that must reproduce the live scores exactly (0 failures in 8 of 8 cells), gives a primary-argmin flip rate of 0.821 fed / 0.724 starved over 158-258 genuine fresh selections per cell. WHAT IT DOES NOT ESTABLISH, and what a reader must not infer: that the flip is principled. There is no null arm. The criterion's bar is computed from the same four seeds it tests (bar = 2 x sd of the arm's own rates, so it is a coefficient-of-variation test, not a test against any reference), and a differential rescaling that spans four orders of magnitude between the live channels would be expected to move the argmin at roughly the rate two unrelated rankings disagree -- so this run cannot distinguish "the operator imposes a different, principled ranking" from "the operator scrambles the ranking". The reference it needs is a PLACEBO differential rescaling carrying no commensurability content. Two further scope bounds: the DV characterises the primary-score stage only, and the `final_commit_by_primary_frac` readout the driver's own docstring calls mandatory interpretive context was not emitted, so nothing relates these flips to the executed action; and two of the five declared commensurability channels (benefit_weighted, goal_weighted) have a scale estimate of exactly 0.0 in every cell, so the operator arbitrated among 3 live channels, not 5.

No claim-layer field moves. The `change` string ends on `stamp this artifact` so `live_status.evidence.from` moves off `failure_autopsy_V3-EXQ-571b_2026-09-01`.

---

## 9. Step 7b mechanical pre-routing checks

`fire_count: 0`. C5 reported `inapplicable` (prose-keyed, no sibling narrative at check time) -- and the skill's rule that **`inapplicable` is not "no fire"** applies. Section 7c-red-team carries the load.

---

## 10. Step 9b -- frozen ledger: nothing owed

Step 9b fires when the autopsy either emits a `fanout_recommendation` or adjudicates a leg of a registered question. **Neither holds**, so it is skipped cleanly.

- No fan-out is emitted -- the open question routes to one named build (the skill's stated exemption).
- The registry carries no question whose `claims` include MECH-439, and no hypothesis whose `adjudicating_runs` name V3-EXQ-1012a or V3-EXQ-1012.
- The growth-restriction check is therefore not engaged.

Recorded explicitly rather than left silent, because an absent check is indistinguishable from a passed one.

---

## 11. Step 7c red-team

**Verdict: CONTESTED.** Run on **Fable 5.1** while this drafting session runs on **Opus** -- a **cross-model** pass. Findings file: `redteam_1012a.md`; full disposition in the JSON `red_team` block.

**Three verdict-moving findings, all applied -- and two of them were defects in THIS autopsy's own recommendation and reasoning, not in the run:**

- **F1** -- the proposed permutation placebo is a **straw null**, satisfied by construction on this run's own scales. *Applied:* withdrawn and replaced (5c-bis, change 1), with the near-miss recorded rather than swapped away.
- **F2** -- the verdict criterion was **misdescribed** and is effectively unfailable (`max(2sd, 0.01)` disjuncted with a majority-above-0.01 test; every content branch emits PASS). *Applied:* corrected throughout, and change 3 now targets the predicate (5c).
- **F3** -- `evidence_direction: "diagnostic"` does not merely dead-letter: the indexer **re-infers `supports`**, and the live `claim_evidence.v1.json` already records MECH-439 supports / 0.75 / "PASS with supporting direction" / verified. *Applied:* rewritten from latent to **live**, fix specified as both halves, promoted to the highest-priority change (5g, change 2).

**Four non-moving findings applied:** F4 (the `~1-1/k` argument rested on a false disjoint-information premise -- reasoning withdrawn, conclusion retained on narrower grounds, 5b); F5 (the dead channels were never *entered*, not merely low-variance, 5d); F6 (the per-claim self-exclusion from the brake count is inconsistent with 571b/571c -- surfaced to governance, nothing here turns on it); F7 (`superseded` downgraded to `open`, 7b). Hygiene: `ree-cloud-2` resolved, arm_results key count corrected to 27.

**Verified sound and left standing:** the routing (implement-substrate, amend `f_dominance_conversion_ceiling`, action, target, severity and paths unchanged, and the Step 2.5c overlap-gate note); the bar being 2 x sd on the same four seeds and the sd being the population sd (both conventions recomputed, neither flips a verdict); the two dead channels and the `1.0` no-op that prevents a blow-up; `final_commit_by_primary_frac` absent while the docstring promises it; the brake count of 15 reproducing exactly with this run adding 0; the `-> stamp this artifact` tail being machine-checkable and not already true; and all arithmetic.

**Third pass in this staging batch to contest the recommendations rather than the science** -- and the first to catch an autopsy about to ship the very defect class it was diagnosing.

---

## 12. What is OWED before this can be applied

1. **The Step 8 interactive gate** -- this draft's routing is a proposal, not a decision.
2. **Nothing was marked reviewed.** `review_tracker.json`, `claims.yaml`, `substrate_queue.json`, the queue and the registry are untouched by this session.
3. Per CLAUDE.md, this autopsy **does not `spawn_task` its own follow-on**. `/governance` chips the substrate amend and the V3-EXQ-1012b successor once Step 2b ratifies the routing.
