# Failure autopsy -- V3-EXQ-1041 (diagnostic adjudication, STAGING DRAFT, REVISED after red-team)

- **Status:** `confirmed` -- Step 8 gate held with the user 2026-09-16 (account-handover walkthrough session; recorded 2026-09-16T13:06:22Z; red-team CONTESTED, findings applied before the gate). See "Step 8 gate outcome" at the end. Originally: Status: AWAITING HUMAN CONFIRMATION. Headless staging-mode draft, revised in place after a ...
Step 7c adversarial pass returned **CONTESTED with 10 findings**. Routing is NOT finalised and
nothing here has been applied to `claims.yaml`, `substrate_queue.json`, `review_tracker.json`, any
manifest, or `hypothesis_space_registry.v1.json`. Step 8 (the interactive gate) is held by the
coordinating session.

- **Target:** `v3_exq_1041_sd106_preservation_step_budget_metric_diagnostic_20260915T203743Z_v3` (queue `V3-EXQ-1041`)
- **Outcome:** PASS -- `experiment_purpose: "diagnostic"`, self-route `metrics_never_comparable`
- **Adjudicated reading: NOT the self-route.** The scored route is an artefact of the decomposition's ORDER. See Section 2.
- **Scope:** single. **Claims:** `SD-106`. **Generated:** 2026-09-16T12:18:33Z
- **Coverage:** `check_autopsy_coverage.py V3-EXQ-1041` -> `AVAILABLE: YES`. Predecessor read end to end (JSON + `.md`) with the driver docstring: `failure_autopsy_V3-EXQ-1023_2026-09-14` (`confirmed`).
- **Read-path note:** the `REE_assembly` main checkout was ref-wedged (50 commits behind `origin/master`), so `claims.yaml`, `substrate_queue.json`, `hypothesis_space_registry.v1.json`, `experiment_proposals.v1.json`, the literature corpus and all 510 committed autopsies were read from `origin/master` via `git show`. Manifests and the driver were read from disk.

> ### What the red-team pass changed
>
> The instrument is sound and every number the first draft printed recomputes exactly -- the
> reviewer verified that independently and could not break it. What did not survive is the
> **attribution** the routing rested on. Applied in full: the metric-vs-budget verdict is
> order-dependent (F1); the mechanism's effect size triples across the sweep and only the smallest
> was reported (F2); the ledger legs belong on an existing question, not a new one (F3); the
> routed lit-pull is already chipped and open (F4); the artifact contradicted itself on whether a
> live discrimination remained (F5); a cross-plane ratio was used as a ranking (F6); three write
> specifications were wrong against `origin/master` (F7, F8, F9); and the recommended direction
> was wrong against the artifact's own claim-layer section (F10). **Nothing was rejected.** One
> point inside F3 is partially disputed and recorded as such (Section 8).

---

## 1. Facts -- what ran and what it measured

**Dry-run gate (Step 2a).** `check_dry_run_citations.py` on the run_id and both queue_ids: `0 dry
cited, 0 dry in named families, 0 ambiguous, 1 clean`, exit 0. Family sweeps `--family v3_exq_1041`
and `--family v3_exq_1023`: **0 dry / 1 real** each. Not a smoke; `excluded_dry_run_ids` empty.

**Criterion-reachability lint.** `validate_experiments.py --checks dry_run_unreachable_criterion`:
11 warnings corpus-wide, **all on the `v3_exq_543*` family, none on this driver.**

**Recording provenance: complete.** `validate_recording.py`: `OK`, 0 always-core gaps, 0 thin-pack
drops, 0 flat-scalar findings, 0 criteria-re-derivability findings. `recording_schema` `rec/v1`;
`substrate_hash` `c991c69cdc...`; `substrate_commit` `311789f558`, clean, `main`;
`substrate_stable_across_run: true`; `machine` `ree-cloud-2` /
`linux-x86_64-py3.10-torch2.12.0+cpu`; `elapsed_seconds` 97.3; full `config`; `seeds [42, 43, 44]`.

**The design.** V3-EXQ-1041 implements, without paraphrase, the cheap P0-warmup-only probe the
CONFIRMED `failure_autopsy_V3-EXQ-1023_2026-09-14` routed. On the same frozen SD-106 latent at
`preservation_weight=200.0` + `use_world_encoder_skip=True`, per cell it reads `sgd_head_r2` (the
in-training jointly-SGD-trained head's holdout R^2 -- the number 1023 reported), `posthoc_ols_r2` (a
post-hoc OLS probe on the same buffer and the same held-out split, the substrate's own R^2
definition, differing only in the fit), `pca32_ols_r2` (the achievable ceiling, Eckart-Young) and
`identity_probe_r2` (a data-independent instrument gate). 2 tracks x 4 budgets x 3 seeds = 24 cells.
Budgets: `b_shipped` (60 eps/12 epochs ~348-396 steps, **1023's exact config**), `b_steps600`
(60/20), `b_steps1200` (60/40 ~1160-1320 steps, same data), `b_designref` (100/12 ~600 steps,
~4000-4500 obs, **the design doc's own named reference**). 3.3x in STEPS at fixed data, ~1.7x in
DATA at ~equal steps.

**All 11 preconditions met**, two of them data-independent by construction
(`identity_probe_recovers_unity` 1.0 vs 0.999, carrying its own measured reachability floor
`probe_system_overdetermined` 1640 vs 250; `pca32_is_the_optimal_32dim_linear_code` -0.0134 vs
+0.01), and one a reproduction gate against 1023's own recorded values reading **delta 0.0000 on all
three seeds**. The red-team pass separately confirmed the two ways the central measurement could
have been wrong and found neither: `sgd_head_r2` and `posthoc_ols_r2` **are** on the same data and
the same split (exact `mean_predictor_mse` identity, 0.0 on 3/3 cells), and the PCA-32 ceiling **is**
on the same data (byte-identical across tracks at the same seed/budget).

### The result as scored

| seed | gap | sgd_head | posthoc (shipped) | pca32 ceiling | posthoc (best) | OFF posthoc | sd106-off | metric | budget | residual | margin |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 42 | 0.1390 | 0.7490 | 0.8469 | 0.8880 | 0.8746 | 0.8209 | +0.0260 | 0.7047 | 0.1990 | 0.0962 | +0.506 |
| 43 | 0.1399 | 0.7464 | 0.8431 | 0.8863 | 0.8684 | 0.8269 | +0.0162 | 0.6913 | 0.1807 | 0.1280 | +0.511 |
| 44 | 0.1790 | 0.6999 | 0.8288 | 0.8789 | 0.8602 | 0.8119 | +0.0169 | 0.7201 | 0.1754 | 0.1045 | +0.545 |
| **median** | | | | | | | | **0.7047** | **0.1807** | **0.1045** | **+0.5240** |

`C1_metric_share_dominant` PASSED (0.5240 vs 0.15); C2 and C3 are the complementary arms of the same
partition. `gate_green: 1`, `non_degenerate: true`.

**Recomputed by hand.** Seed 43: `gap = 0.8863228360 - 0.7463981728 = 0.1399246631`;
`metric_share = (0.8431230127 - 0.7463981728)/0.1399246631 = 0.6912636965`;
`budget_share = (0.8684118798 - 0.8431230127)/0.1399246631 = 0.1807320207`. All match.

**Hygiene, self-flagged.** The three *medians* sum to 0.9899 because each is taken over seeds
independently; the per-seed shares each sum to 1.0 exactly. Nothing routes on the medians' sum.
And `pca32_ols_r2` is identical to all digits across `b_shipped`/`b_steps600`/`b_steps1200` and
moves only at `b_designref` -- correct by construction (the first three vary only epochs on the same
60-episode buffer), bounded by `ceiling_stable_across_budgets` at 0.0043 vs 0.02.

---

## 2. The scored route is order-dependent -- the central finding, and it is a correction

**The first draft adjudicated the self-route as correct. That adjudication is withdrawn.**

**The mechanism.** The driver's `budget_share` is measured on `posthoc_ols_r2` only
(`driver:819-841`), while `gap` is anchored at `sgd_head_r2` (`driver:126`). `sgd_head_r2` is stored
per cell and aggregated per budget in `readout` -- and is **never used in the shares**. Substituting
the identities, `metric_share = 1 - (1 - parity)*pca32/gap`, so C1 fires precisely when (i) the code
is near the PCA-32 ceiling **and** (ii) the SGD head is far below the code. Condition (ii) **is**
head under-training, which is exactly what the budget hypothesis asserts. So C1 and C2 are not a
partition of metric-vs-budget: **C1 measures head under-training and C2 measures code
under-training. Both are budget; one is labelled metric.**

**Three partitions of the identical gap, same cells, same best-budget cell** (`b_steps1200` is best
on BOTH statistics on 3/3 seeds, so there is no cherry-pick):

| ordering | metric | budget | residual | leader margin (per seed) | route at the pre-registered 0.15 |
|---|---|---|---|---|---|
| metric-first (**as shipped**) | 0.7047 | 0.1807 | 0.1045 | +0.506 / +0.511 / +0.545 | `metrics_never_comparable` |
| budget-first | 0.1041 | **0.7688** | 0.1045 | +0.696 / +0.641 / +0.629 | **`under_budgeted_p0a`** |
| **order-symmetric (mean)** | 0.4044 | 0.4748 | 0.1045 | **+0.095 / +0.078 / +0.042** | **`no_dominant_explanation`** |

Recomputed independently from the shipped manifest: budget-first per seed **0.799640 / 0.768843 /
0.762308**; order-symmetric leader margins **0.094899 / 0.077580 / 0.042204**, all **below 0.15 on
3/3 seeds**.

**This autopsy routes on the order-symmetric partition**, which is `no_dominant_explanation` -- and
that is not a failure state. The driver's own `combination_rule` pre-registers it as "a RESULT, not
an instrument failure: it says the shortfall has no single dominant cause, and the recorded shares
say how it splits."

**Two order-free facts corroborate that the budget account is not exhausted.** The head has **not
saturated**: `sgd_head_r2` medians run 0.746398 -> 0.806392 -> **0.853978** across the step sweep,
still rising at ~1160-1320 steps and still 0.014 below the post-hoc probe there. And at the design
doc's **own named reference budget** (`b_designref`) budget alone closes **0.362-0.444** of the gap
on the reported statistic.

**The irony, recorded because it is the generalisable lesson.** The driver's own red-team record
killed a transferred *bar* because "the equally defensible RESIDUAL transfer implies 0.933 ... and
the two give OPPOSITE routes on the authoring seed". The replacement *decomposition* carries the
identical non-uniqueness -- two equally defensible orderings, opposite routes, on all three seeds
rather than one -- and shipped un-flagged. The first draft of this autopsy did not catch it either.

---

## 3. The mechanism's effect size triples across the sweep

**Order-free** -- a straight paired difference at each budget, with no decomposition choice in it,
so it is untouched by anything in Section 2. SD-106 minus OFF `posthoc_ols_r2`, medians:

| | b_shipped | b_steps600 | b_steps1200 | b_designref |
|---|---|---|---|---|
| SD-106 - OFF | **+0.016931** | +0.031490 | **+0.050941** | +0.027747 |
| positive seeds | 3/3 | 3/3 | 3/3 | 3/3 |
| SD-106 parity | 0.951259 | 0.964158 | 0.979792 | 0.963862 |
| OFF parity | 0.924470 | 0.925960 | 0.920761 | 0.930338 |

SD-106's parity rises monotonically with budget while the OFF arm's stays flat. **V3-EXQ-1023's
acceptance measurement therefore measured this mechanism at roughly one third of its within-range
effect size** -- and the first draft quoted only the `b_shipped` value, which is the single number
its now-withdrawn refusal of an acceptance re-run was built on.

---

## 4. What the run settles, and the plane it does not cross

V3-EXQ-1023 measured at the **consumer rung** (held-out oracle-action agreement: SD-106 mean
0.719185, OFF 0.668200, PCA-32 anchor 0.868896, bar 0.85, 0/3 clearing). This run measures the
**encoder** plane and does not re-measure consumer-rung agreement at all.

**Settled, order-free:** the two statistics are not the same and the reported one under-reads the
code by **0.0979 / 0.0967 / 0.1289** absolute R^2; the code reaches 0.951-0.980 of the achievable
ceiling; the mechanism is not inert and its effect triples with budget; the head has not saturated.

**Not settled:** the metric-vs-budget split (Section 2), and which of two readings accounts for the
consumer-rung shortfall:

- **(a) transfer amplification** -- the consumer rung converts a small decodability deficit into a
  large agreement deficit through decision-boundary geometry alone. Note this is *not* the
  eliminated "consumer cannot learn it": it presumes the consumer can.
- **(b) which-directions** -- the retained variance is not the decision-relevant variance.

**The first draft ranked (b) above (a) as "the more economical account", on the ratio of a 0.043
held-out reconstruction-R^2 deficit to a 0.150 oracle-action-agreement deficit (~3.5x). That
ranking is WITHDRAWN.** They are different DVs in different units with no established transfer
function, and the slope is estimated from **one** point pair; a discrete-action decoder can convert
a small reconstruction deficit into a large agreement deficit through geometry alone. Graded
honestly in the other direction: V3-EXQ-1023's own capacity ladder partly defends the draft --
mlp2048 buys only ~0.005-0.026 over mlp128 and does not close 0.150, and the ledger's
`H-B-consumer-learning` is `eliminated` -- so "the consumer cannot learn it" **is** excluded. What
is not excluded is a steep monotone transfer. (b) is a **live reading worth grounding**, not a
ranked winner.

**The same slope is retained for the one use that ranks nothing:** generating (a)'s falsifiable
null. That is what turns an unranked pair into a discriminator -- see Section 10.

**Secondary, unaffected.** Within the swept range the effective budget coordinate is **STEPS, not
observations**: `b_steps1200` is best on 3/3 seeds on *both* statistics, and `b_designref` -- more
data at ~equal steps -- scores below it (post-hoc 0.850 vs 0.868; sgd 0.797 vs 0.854).

**Third explanation, first-class.** PCA-32 of the P0a rollout buffer reaches **0.888 held-out and
0.893 in-sample on seed 42** (agreeing to within 0.005, so not a split artefact; cross-seed held-out
median 0.886), against the design doc's 0.9983/0.9984. The design-time anchor was never on this
observation distribution, so the doc's 0.9974/0.9978 table is not comparable to any P0a acceptance
number. This compounds the recording gap 1023 already logged -- with no committed producer script,
the distribution cannot be recovered from the repo at all. Every criterion here is ceiling-relative,
so the routing is unaffected. *(Bases corrected per hygiene H2: the first draft mixed a cross-seed
median with a seed-42 value.)*

---

## 5. Claim layer

`claim_ids: ["SD-106"]`; SD-106 is itself the subject, so there is no parent claim to misattribute
to and no inherited co-tag. From `origin/master`:

| Field | Current value |
|---|---|
| `status` | `implemented` |
| `epistemic_category` | `standard` (no stated re-check condition) |
| `diagnostic_evidence_adjudicated` | `true` |
| `pending_retest_after_substrate` | `true` |
| `live_status.evidence.from` | `failure_autopsy_V3-EXQ-1023_2026-09-14` |
| `validation_experiment` | **a PROSE BLOCK beginning `V3-EXQ-1015 -- ...`, carrying the pre-set ACCEPTANCE TARGET** |

**Did the experiment test the claim under conditions where it could express itself?** It did not
test the *claim* at all -- it tested the *attribution of a prior measurement*, and left that
attribution open. Diagnostic purpose, excluded from confidence and conflict scoring.

**Recommended direction: `non_contributory`, revised from `mixed`.** The manifest's own
`evidence_direction` is `unknown`, and a `mixed` direction asserts the evidence bears on the claim in
both senses while this artifact's own position is that it bears on it in neither. The predecessor's
`mixed` was earned on an acceptance DV; this run has none. This is **not** a claim that the run
yielded no interpretable information -- it yielded a great deal (Section 11), which is why the
skill's "non-contributory only if no interpretable signal at any layer" test is discharged in prose.
Per the skill's pairing rule the reading is paired with `pending_retest_after_substrate: true` and
with an explicit narrow-supports check: **`narrow_supports_flag` is now `true`** (reversing the first
draft), because the positive leg this run establishes is genuinely single-pathway -- one encoder-level
DV, one rung, one weight, 3 seeds, one machine class, no consumer-rung measurement.

**Unapplied prior recommendation, at THREE sites.** The confirmed 1023 autopsy recommended correcting
the stale `V3-EXQ-1015` reference. Still unapplied in `claims.yaml`, in
`ree-v3/docs/substrate/SD-106-...md:19`, and -- named by the red-team and missed by the first draft --
in `REE_assembly/docs/architecture/sd_106_...md` lines 15 and 151, while line 104 of that same file
already says V3-EXQ-1023.

`bears_on: ["zworld_actor_adequacy_locus"]` -- carried verbatim from 1023. **Section 12 now acts on
that linkage instead of merely recording it.**

---

## 6. Biological-reference triage

**Closest reference:** DiCarlo-style ventral-stream manifold untangling -- a sensory hierarchy
trained under task/behavioural pressure that makes decision-relevant structure more linearly
accessible than the input's own statistics. Its dependencies include a downstream consumer whose
read-out *defines* which directions count as decision-relevant.

**A formal import.** SD-106 implements task-agnostic scale-normalised `(1 - R^2)` generic variance
preservation as a proxy for "the encoder should not discard decision-relevant content". The
reference's untangling is driven by task relevance, not generic variance. The divergence is
**load-bearing by default** and is unchanged by this run.

**What this run does NOT do, revised.** The first draft said this run makes the divergence "the
economical reading" and that V3-EXQ-1023's deferral of the biology question "was correct and it
paid". The second half stands; the first does not. 1023 deferred explicitly *because* a training-
budget explanation was live and cheaply testable first -- and **that deferral condition is not
discharged**: the budget explanation survives the order-symmetric partition alive. So the biology
question is **co-primary with the probe that would discharge it**, not promoted over it.

**Literature status: `partial`, scoped.** Checked on `origin/master` across all 540
`targeted_review_*` directories, and independently reproduced by the red-team pass.

- **PRESENT** for untangling: `targeted_review_sd_015/2026-04-02_..._dicarlo2007`, `targeted_review_perceptual_manifold_adaptors/2026-06-12_..._dicarlo2012`.
- **ABSENT** for generic-vs-task-relevant/selective compression. `git grep -l "SD-106" -- evidence/literature/` returns **zero** files; the only corpus hit for "information bottleneck" or "efficient coding" is one comparison-table row in `targeted_review_q_079/SYNTHESIS.md`, a DLIF formalism drill.

---

## 7. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear (net)** | more unclear after the red-team pass, not less. Strengthened order-free on implementation fidelity; the metric-vs-budget split and the (a)/(b) pair both unadjudicated. Not adjudicated at claim level at all -- diagnostic, unscored |
| Biological reference | partial | untangling present; the generic-vs-task-relevant question has no targeted review and its deferral condition is still unmet |
| Dependency / prerequisites | present | 11/11 preconditions; instrument sound and unbroken by the red-team pass |
| Implementation completeness | **complete** | bypass norm 4.133 matching 1023's 4.13-4.37; positive over OFF on every seed at every budget |
| Environment adequacy | adequate | same rung/recipe as x1002/x1010/x1023; only `ZWorldP0Trainer` under a `RandomPolicy` is exercised |
| Measurement adequacy | **adequate (this run)** | the probe is gated data-independently and uses the substrate's own R^2 definition. It establishes order-free that the PRIOR statistic under-reads by 0.098-0.129 -- but **not** that the mismatch dominates |
| Integration adequacy | isolated | P0-warmup-only frozen read |
| Scale / capacity | **partial / likely insufficient** -- REGRADED | the first draft read `adequate WITHIN the swept range`. That read the sweep through the order-dependent share instead of the readout's own trajectory: `sgd_head_r2` moves 0.746 -> 0.806 -> 0.854 (0.76-0.80 of the gap), **has not saturated**, and is still 0.014 below the probe at the top. V3-EXQ-1023's "likely insufficient, or unknown" **stands**, now quantified |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Reads from | Verdict |
|---|---|---|
| MECHANISM | Implementation completeness = `complete` | established |
| MEASURES | Measurement adequacy = `adequate` | established |
| ENVIRONMENT | Environment adequacy = `adequate` | established |
| **REE** | all three **and** REE still did not demonstrate the predicted competence | **false** |

**Net: NOT APPLICABLE as an organism-level failure read.** A diagnostic PASS; nothing chargeable to
REE. The fourth conjunct is not met -- REE did demonstrate the predicted proximal competence.

**Two claims from the first draft are WITHDRAWN here, recorded rather than deleted.** (i) That the
1023 shortfall is located dominantly in **MEASURES** -- it rested on the order-dependent metric
share; on the order-symmetric partition it has no dominant location. (ii) That this run settles
V3-EXQ-1023's own open Step 8 tension ("REE FAILED" vs "MIXED, grounded on Scale/capacity") in the
MIXED direction. It does not settle it, and the Scale/capacity leg of that tension is if anything
**strengthened** by the regraded row above.

**Recommended `epistemic_category`: `standard`** -- not `substrate_ceiling`/`substrate_conditional`.
Nothing asserts SD-106's answer is gated on substrate work: the owed next steps are a re-run on an
existing harness and a literature pull, neither a build. Either `substrate_*` value would drop
SD-106 into `_EPI_SUPPRESS_PROPOSAL` and make it not-v3-testable, starving the lane this routing
feeds. The failure-mode label lives in the note fields, never in the category.

---

## 8. Step 7c -- adversarial red-team pass

**Reviewer model: `claude-opus` (Opus). This was a SAME-MODEL pass** -- this draft was itself
written on Opus 5, so the cross-model independence the skill prefers was **not** obtained, and the
verdict must not later be read as cross-model. A same-model pass is still a valid pass. Independence
was preserved on the skill's other axis: the reviewer received the raw evidence and the stated
conclusion with the drafting session's reasoning withheld, read the JSON before the `.md`, and
recomputed load-bearing numbers from the manifest's own cells.

**Verdict: CONTESTED, 10 findings.** **All ten confirmers were re-run independently by this session
before any revision. Every one held. Nothing was rejected.**

| # | Finding | Confirmer | Disposition |
|---|---|---|---|
| **F1** | metric-vs-budget verdict set by decomposition ORDER | budget-first 0.7996/0.7688/0.7623; order-symmetric margins 0.0949/0.0776/0.0422, all < 0.15; head unsaturated 0.746->0.806->0.854 | **APPLIED IN FULL** -- all three partitions reported, routed on the order-symmetric one; `H-under-budgeted-p0a` NOT eliminated; third refusal clause withdrawn; lit-pull co-primary; Scale row regraded; MEASURES attribution withdrawn |
| **F2** | effect over paired control triples; only smallest reported | +0.016931 / +0.031490 / +0.050941 / +0.027747, 3/3 positive at every budget; OFF parity flat | **APPLIED IN FULL** -- all four budgets reported; the discriminator re-run is now the primary routing |
| **F3** | `bears_on` names an existing ledger question; the growth check was a string test | question exists, 5 hypotheses, `growth_restriction` absent, 2 prior fanout events, H-B `eliminated` / H-F `confirmed` | **APPLIED, one point partially disputed** -- see below |
| **F4** | the routed lit-pull is already chipped and open; the duplicate check points at blind registries | `chip-20260916-sd106-compression-litpull` (`task_861ccb12`, open, unclaimed, 2026-09-16T04:37:08Z); `LIT-0132` proposed | **APPLIED IN FULL** -- instruction now says reconcile, do not spawn a second |
| **F5** | `fanout_recommendation: null` + `mystery` contradict the artifact's own Section 4 | internal | **APPLIED IN FULL** -- reclassified `puzzle (known rules)`, fan-out emitted, "strong evidence" escalation rewritten as a withdrawal |
| **F6** | the ~3.5x cross-plane ratio used as a ranking | incommensurable DVs, slope from one point pair | **APPLIED** -- ranking withdrawn; slope retained only as (a)'s declared null |
| **F7** | `validation_experiment` write would destroy a pre-set acceptance target; third stale site unnamed | the field is a prose block; `docs/architecture/sd_106_...md` lines 15/151 confirmed | **APPLIED IN FULL** -- respecified as a leading-token string edit; all three sites enumerated |
| **F8** | amend narrows `unblocks_claims` 6->5; new record would open a second `open` item on an unmeasured DV | origin carries six incl. the goal-directed-pathway string | **APPLIED IN FULL** -- six restored; record respecified as an attribution note |
| **F9** | `H-anchor-off-distribution` pre-registered at its own resolution instant, sourced to a future document | driver first commit `febce39` 2026-09-15T20:33:32Z, **4m11s before** the run | **APPLIED IN FULL** -- and it simplified the block: the leg is ordinary git-witnessed fan-out growth, not a Mode C discovery |
| **F10** | direction `mixed` against the manifest's `unknown` and the artifact's own Section 5 | manifest reads `unknown` | **APPLIED** -- `non_contributory`, pairing rule discharged, granularity leg re-checked |

**The partial dispute, inside F3, recorded with its reason rather than dropped.** The reviewer maps
reading (a) onto the eliminated `H-B-consumer-learning` and reading (b) onto the confirmed
`H-F-content-discarded-at-encode`, and offers both as support "cutting in the draft's favour".
**The attachment is applied; the equivalences are not relied on.** (i) H-B asserts the consumer
*cannot learn* the mapping; (a) asserts it *can* and that the mapping is steep. H-B's elimination is
a **premise** of (a), not a disposal of it. (ii) H-F is confirmed for the **shipped, pre-SD-106**
encoder -- SD-106 is the build H-F's diagnosis motivated -- so it is not by itself a confirmation of
(b) for the SD-106 encoder. Taking both at full strength was the easier move and would have
overclaimed in this artifact's own favour.

**Hygiene, all dispositioned.** H1 -- the JSON said 0.0977 where the manifest says 0.0979246225
(the `.md` was already right); **fixed at both sites**. H2 -- "0.886 held-out / 0.893 in-sample"
mixed a cross-seed median with a seed-42 value; **fixed to seed 42's consistent pair 0.888/0.893**,
with the cross-seed median given alongside, including in the permanent-substrate-doc write. H3 --
the medians-sum note is correct; retained. H4 -- `narrow_supports_flag` contradicted its own note;
**fixed to `true`**. H5 -- the live `implementation_hint` says "the fourth on this entry" while
`failure_record` holds two; pre-existing, survives this amend, **flagged to governance, not silently
fixed**. H6, H7 -- no action; H7 records that the instrument is exemplary, which is what makes the
F1 re-partition possible at all.

---

## 9. Step 7b -- mechanical pre-routing checks

`autopsy_pre_routing_checks.py --artifact <draft> --json`: **`fire_count: 0`, `fires: []`,
`inapplicable: []`.** Run twice on the first draft (the first pass returned C5 `inapplicable` for
want of a sibling `.md`), and to be re-run on this revision, whose routing now recommends an
experiment -- C1-strict is live where before it was vacuous.

**The limit of that clean report, stated because this session just demonstrated it.** 7b found
nothing on the first draft, and 7c then returned CONTESTED with 10 findings, five of which changed
routing or writes. In particular the first draft recorded C1-strict as "no fire -- the routing
recommends no experiment, it recommends a `/lit-pull`": it **noticed** that 7b was structurally
blind to a duplicate lit-pull and did not compensate -- and an open duplicate chip did in fact exist
(F4). A clean 7b is not evidence of a clean artifact, and the two layers are not nested in either
direction.

---

## 10. Cluster, recurrence and the re-derive brake

**Scope: single.** No other pending FAIL shares SD-106, the `zworld_p0` substrate, or this shape.

**Re-derive brake (R1-R3): count 0 of threshold 2. DOES NOT FIRE.** Run over the committed corpus on
`origin/master` (510 artifacts) with the skill's recipe unmodified: exactly one prior target names
SD-106 (`failure_autopsy_V3-EXQ-1023_2026-09-14`) and it does not count (`standard` / `mixed`). This
target does not count either, and **the F10 direction change does not alter that**:
`recommended_epistemic_category_per_claim` declares `standard` for SD-106, which short-circuits
`counts()` at the per-claim branch *before* the direction disjunct is reached.

**`refused_requeue` stays TRUE but now carries TWO clauses, not three.** REFUSED: (1) a re-queue of
this diagnostic -- re-running the same decomposition reproduces the same order-dependence; (2) a
`preservation_weight` sweep -- 1023's refusal stands untouched and nothing here gives ground to
revisit it. **WITHDRAWN:** the third clause, "an acceptance-measurement re-run justified as a budget
fix (budget is measured at 0.181 ...)". Its stated numerical ground was the order-dependent 0.181;
budget-first the same cells give 0.769. **An acceptance re-run at a raised P0a budget is therefore
not refused -- it is the routed next step.**

**Granularity-debt trigger: DOES NOT FIRE.** `granularity_debt_cluster.py SD-106`: 1 target, 1 file,
alignment `weakened=1`. With this target SD-106 carries 2, meeting the bare count, but neither leg of
the reader's test is met: the signatures do not differ structurally (this is a **lineage** -- 1041 is
the probe 1023's routing commissioned), and this target's `claim_alignment` buckets as `unclear`, so
the distribution stays `weakened=1`. **Re-checked after F10** flagged that the second leg depended on
the direction field: the first leg holds independently and the bucket does not move, so the trigger
does not fire either way.

---

## 11. Routing (DRAFT -- not yet confirmed)

**Node classification: `complex (probe-gated) / puzzle (known rules)`** -- revised from the first
draft's `mystery (known data)`, which contradicted its own Section 4. The frame is well-posed and a
**fact is missing**, and one probe on an existing harness fetches it.

**PRIMARY: `/queue-experiment`.** Re-run `experiments/v3_exq_1010_zworld_overcapacity_decoder_sweep.py`
**UNCHANGED** -- the harness `claims.yaml`'s own `validation_experiment` already names -- against an
SD-106-ON warmup with P0a `epochs=40`: the `b_steps1200` cell this run already executed six times.
One config knob, no new driver, same 3 seeds, existing dataset recipe, calibration anchor and
negative control. An **alphabetic-suffix** iteration of the acceptance measurement (same question,
raised budget), not a new EXQ number. It discharges three things at once:

| It tests | Declared null |
|---|---|
| **(a) transfer amplification** | at post-hoc R^2 0.868412, interpolated slope 3.4655 predicts consumer agreement **~0.8068** |
| **(b) which-directions** | **~0.7192** -- no move from the shipped measurement |
| **H-under-budgeted-p0a** | a move toward or past the 0.85 bar |

Separation between the two nulls **~0.0876** on the shipped DV at 3 seeds.

**A second probe on a different axis**, offered so the fan-out is a portfolio rather than one
sequential re-pose: a subspace-overlap readout (principal angles between the SD-106 code and PCA-32
on the same P0a buffer) reported beside the existing post-hoc R^2. High decodability parity with low
subspace overlap is the direct signature of (b) and needs no consumer-rung run. Encoder plane only.

**CO-PRIMARY, not promoted above it: `/lit-pull`** on generic vs task-relevant/behaviourally-
conditioned selective compression. A real and confirmed corpus gap -- but its promotion to *sole*
primary in the first draft rested on the order-dependent budget share and the withdrawn cross-plane
ranking. **It is already chipped and open**: `chip-20260916-sd106-compression-litpull`
(`task_861ccb12`, unclaimed, spawned 2026-09-16T04:37:08Z, 7h41m before this artifact, with a prompt
citing this very run). Governance must **reconcile against that chip and `LIT-0132`, not spawn a
second**.

**SECONDARY, bookkeeping only, no build:** the `substrate_queue` `amend` (Section 12).

**NOT REFUSED:** the acceptance re-run at a raised budget (the first draft refused it; withdrawn),
and a different-mechanism redesign under a new `sd_id` and EXQ number once the lit-pull has grounded
it.

**Follow-on is recorded, not spawned.** Per CLAUDE.md Session Land Protocol step 6 and the
2026-07-30 rule, an autopsy does not `spawn_task` its own unratified routing. **Surfaced for the
user rather than adjudicated:** a chip spawned off exactly this run's routing already existed before
this artifact was written. This session did not spawn it and spawns nothing.

---

## 12. Recommended writes (governance applies these -- this skill writes none)

1. **`claims.yaml` SD-106** -- append the drafted `evidence_quality_note`; move
   `live_status.evidence.from` / `.verdict` / `.as_of` onto this artifact. Leave
   `epistemic_category: standard`, `diagnostic_evidence_adjudicated: true`,
   `pending_retest_after_substrate: true` and `status: implemented` untouched.
2. **`claims.yaml` SD-106 `validation_experiment` -- A LEADING-TOKEN STRING EDIT, NOT A FIELD
   REPLACEMENT.** The field is a prose block whose tail carries the governance-pre-set ACCEPTANCE
   TARGET and is **the only place that target is recorded in `claims.yaml`**. Replace only the
   leading `V3-EXQ-1015` with `V3-EXQ-1023`; preserve everything from ` -- re-runs
   ree-v3/experiments/v3_exq_1010_zworld_overcapacity_decoder_sweep.py UNCHANGED ...` through
   `... all already exist.` verbatim.
3. **`ree-v3/docs/substrate/SD-106-...md:19`** -- `Validation experiment: V3-EXQ-1015 queued` ->
   V3-EXQ-1023.
4. **`REE_assembly/docs/architecture/sd_106_...md` lines 15 and 151** -- third stale site (line 104
   already says V3-EXQ-1023, so the file is internally inconsistent).
5. **Same file, "Measured effect"** -- state the observation distribution the 0.9974/0.9978/0.9983/
   0.9984 table was measured on, and note PCA-32 on the P0a buffer reaches only 0.888 held-out /
   0.893 in-sample (seed 42; cross-seed held-out median 0.886).
6. **`substrate_queue.json` SD-106 `amend`** -- treat `unblocks_claims` (**all six**, including
   "goal-directed behaviour pathway (entire EXQ-085h..o cluster)"), `severity` and `substrate_paths`
   as **unchanged**; they are re-enumerated in the entry only so the amend cannot narrow them.
   Supersede `implementation_hint_2026_09_15`. Append the new record as an **attribution note**
   (`resolved: "attribution_note"`), or fold its text into the existing V3-EXQ-1023 item -- **do not
   create a second `open` item against a DV this run did not measure**. Leave the prior item `open`.
7. **`substrate_queue.json` SD-106, pre-existing (H5)** -- the older `implementation_hint` says "the
   fourth on this entry" while `failure_record` holds two. Not touched by this amend; flagged, not
   fixed.
8. **`review_tracker.json`** -- mark the run reviewed once confirmed.
9. **`hypothesis_space_registry.v1.json`** -- apply Section 13 onto the **existing** question, not a
   new one.
10. **Chips** -- reconcile the `/lit-pull` against the **already-open** `chip-20260916-sd106-
    compression-litpull` and `LIT-0132`; check the chip ledger before chipping the
    `/queue-experiment`. **The igw-ledger check the first draft specified is insufficient on its
    own**: both `igw_assignments.json` and `igw_routine_ledger.json` are clean for this item, so
    governance following that instruction alone would check two clean files and create a duplicate.

> On `resolves_prior_failure_record`: **deliberately empty.** The 1023 item is not `resolved` (no
> build closed the failure mode it names; this run did not re-measure that DV) and not `superseded`
> (it overturns nothing -- every number in that record stands). Filling either verb would repeat the
> D4 defect 1023's own red-team pass caught.

---

## 13. Step 9b -- frozen hypothesis ledger (DRAFTED ONLY, staging mode)

Nothing was written to the registry or its three derive-only siblings.

**REVISED after F3 and F9. The first draft opened a STANDALONE NEW QUESTION and booked zero growth
against the question its own `bears_on` names. Withdrawn.** Its justification was a **string test** --
no registered question mentions SD-106 / V3-EXQ-1023 / V3-EXQ-1041 / `sd106`. The string test is
accurate (0 hits across all 60 questions, independently reproduced); the conclusion drawn from it
was false. Attachment is by **subject**, and this target's own `bears_on` names
`zworld_actor_adequacy_locus`, which the registry keys to MECH-457/INV-088. SD-106 is the build that
question's confirmed H-F diagnosis named, and V3-EXQ-1023's `.md` states the linkage explicitly.
A parallel question would have split one lineage across two denominators and let these legs escape
growth accounting entirely.

**Growth-restriction check, re-run on the CORRECT question:** `zworld_actor_adequacy_locus` carries
**no** top-level `growth_restriction` -> proceed normally; nothing to carry to the Step 8 gate on
this axis. Recorded because the first draft's clean verdict was reached for the wrong reason.

**Mode:** labelled **FAN-OUT GROWTH (invariant 3a)**, in two events. Denominator
`initial_frozen_count` **5 -> 11** (delta 6 = 4 + 2, and the events sum to the move);
`initial_frozen_count_at_registration` **stays 2**, untouched.

| `hid` | axis (family) | state | basis, in one line |
|---|---|---|---|
| `H-metric-mismatch` | measurement (instrumentation) | **confirmed (narrow form only)** | the under-read is real and order-free (0.098/0.097/0.129); its **dominance** is not confirmed |
| `H-under-budgeted-p0a` | curriculum (process) | **alive** | budget-first 0.769, order-symmetric 0.475, head unsaturated -- **not** eliminated |
| `H-mechanism-defect` | learning-signal (constitution) | **split** | inert child **eliminated** order-free (>OFF 3/3 at every budget); below-ceiling child **alive** (0.043 / 0.018 residual gap) |
| `H-anchor-off-distribution` | instrumentation | **confirmed** | PCA-32 on the P0a buffer 0.888/0.893 (seed 42) vs the doc's 0.9983 |
| `H-transfer-amplification` | readout (representation) | **alive** (Mode A) | declared null ~0.8068 |
| `H-which-directions` | representation | **alive** (Mode A) | declared null ~0.7192 |

**Circling check -- required by invariant 3a and stated, not skipped.** Two new legs re-enter
families that already hold **eliminated** legs, which is the `circling` signature:

- `H-anchor-off-distribution` (instrumentation) re-enters `H-E-channel-input-capacity`'s family
  (eliminated 2026-09-07). Not that leg renamed: H-E asserted a 250->32 channel-**input capacity**
  bound; this asserts nothing about capacity, only that the design-time anchor sat on a different
  observation **distribution**.
- `H-transfer-amplification` (readout) re-enters `H-B-consumer-learning`'s family (eliminated
  2026-09-05). Not that leg renamed either: H-B asserted the consumer **cannot learn** the mapping;
  this asserts it **can** -- H-B's elimination is its premise -- and that the mapping is steep.

Governance should read the resulting `convergence_class` beside `h_fanout_recurrence`: this is the
question's **third and fourth** growth events, its denominator has moved 2 -> 5 -> 11, so it has not
converged and its headline narrowing ratio is deflated precisely now. `fanout_growth_note` is set on
the question to say so.

**Invariants.** (1) `initial_frozen_count` bumped to 11 in the same edit, matching
`len(hypotheses)`. (2) `pre_registered_utc <= resolved_utc` on every resolved leg: the four
retrospective legs carry **2026-09-15T20:33:32Z** -- the driver's git-witnessed first-commit time
(`ree-v3 febce39`) -- against `resolved_utc` **2026-09-15T20:37:43Z**, a real **4m11s** lead rather
than the first draft's zero-lead stamp, and witnessed by git rather than asserted. Three of the four
carry an earlier witness too (`failure_autopsy_V3-EXQ-1023_2026-09-14.json`, `REE_assembly
8418b0ed762`, 2026-09-14T17:13:28Z); the driver is cited as the single source because it is the one
document witnessing all four. (3) satisfied via the labelled 3a path, with
`pre_registration_source` on every added leg. (4)/(5) no leg is stamped `eliminated` or `split` in
this edit without the full bar on order-free evidence; both `confirmed` legs carry
`control_passed: true`. (7) `decision.decidable` and `decision_log_ref` untouched -- human-owned.

**Axis map:** every label used (`measurement`, `curriculum`, `learning-signal`, `instrumentation`,
`readout`, `representation`) is already a row in the human-owned `axis_families.map`; no new family
row is owed and `convergence_class` is not forced to `indeterminate`.

---

## 14. Step 8 gate -- HELD BY THE COORDINATING SESSION

Not run here. It should in particular resolve:

- **the routing inversion** -- the first draft routed `/lit-pull` as sole primary; this revision
  routes the consumer-rung discriminator primary with the lit-pull co-primary, on F1/F2;
- **whether `no_dominant_explanation` is accepted as the adjudicated reading** over the driver's
  scored `metrics_never_comparable` -- the driver pre-registered the tie branch as a legitimate
  result, but this is the autopsy declining to ratify its target's own self-route;
- **`H-under-budgeted-p0a` staying `alive`** rather than eliminated, and the consequent withdrawal
  of the refusal of an acceptance re-run;
- **the ledger attachment** to `zworld_actor_adequacy_locus` (a denominator move 5 -> 11 on a
  question keyed to MECH-457/INV-088) and the two circling justifications;
- **the already-open lit-pull chip** -- whether it is allowed to proceed as-is, retargeted, or
  withdrawn, given it was spawned off a routing this gate has not yet ratified;
- **the three stale-reference sites** and the string-edit specification that protects the pre-set
  acceptance target;
- **that the 7c pass was SAME-MODEL** (Opus reviewing an Opus draft), so its CONTESTED verdict
  should not be read as cross-model.

---

**Human confirmation:** NOT YET GIVEN. Status remains `awaiting_human_confirmation`.

## Step 8 gate outcome -- CONFIRMED 2026-09-16T13:06:22Z

CONFIRMED as recommended (Opus SAME-MODEL red-team, 10 findings applied, one partial disagreement recorded): the metric-vs-budget attribution was an artefact of decomposition ORDER; all three partitions reported and the run routed on the order-symmetric one -- the driver's own pre-registered no_dominant_explanation branch. Direction non_contributory (not mixed), category standard, SD-106 fields unchanged, change tail 'stamp this artifact', narrow_supports_flag true; routing queue-experiment PRIMARY (v3_exq_1010 decoder sweep unchanged against an SD-106-ON warmup at P0a epochs=40; declared nulls ~0.8068 vs ~0.7192) with /lit-pull CO-primary reconciled against the already-open chip-20260916-sd106-compression-litpull and LIT-0132 (governance chips the re-run, spawns no second lit-pull); substrate AMEND SD-106 as bookkeeping with the full six-item unblocks_claims and an attribution note rather than a duplicate open record; validation_experiment write specified as a leading-token STRING edit preserving the pre-set acceptance target, third stale site named. Ledger: six legs attached to the EXISTING question zworld_actor_adequacy_locus via two labelled fan-out growth events (5 -> 11), H-under-budgeted-p0a alive, H-mechanism-defect split -- applied at confirmation.
