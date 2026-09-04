# Failure autopsy -- V3-EXQ-997 (MECH-162)

- **Status:** `awaiting_human_confirmation` (staging mode; the Step 8 interactive gate is OWED and has not been held)
- **Generated (UTC):** `2026-09-04T14:23:32Z`
- **Session:** `governance-20260904-1347`
- **Scope:** single
- **Target:** `v3_exq_997_mech162_zresource_zworld_planning_reconvergence_20260904T032212Z_v3` -- FAIL, self-declared `weakens`, `experiment_purpose: evidence`, `claim_ids: ["MECH-162"]`, `ree-cloud-2`, 990.7 s
- **Facts file:** `facts_V3-EXQ-997.md` (all numbers below are recomputed there from the manifest's own cells)

---

## 1. One-paragraph verdict

V3-EXQ-997 is a carefully built experiment that asked a question its apparatus could not reach. MECH-162 asserts that `z_resource` and `z_world` **re-converge** at the hippocampal planning stage; the run compared a `z_resource`-seeded planning cue against a `z_world`-seeded one. Those are two **substitutions**, not a convergence, and a code read shows the omission is forced rather than chosen: `update_z_goal` selects one latent or the other by a strict XOR, and `GhostGoalBank.rank()` never reads `z_world` at all. Both arms therefore instantiate the claim's *negative* condition. On top of that scope problem, the arm that was supposed to carry object identity used an untrained `ResourceEncoder` (its own source documents a P0 training phase that was skipped), no manipulation check was recorded to show that arm's cue carried identity content at all, and the failing statistic inverts to a PASS under an equally defensible aggregation of data already in the same manifest. The recommendation is therefore `non_contributory` rather than `weakens`, `epistemic_category: substrate_ceiling`, and a routing to `implement-substrate` for a fused planning input -- with an explicit refusal of any two-arm lettered re-issue.

---

## 2. What failed, precisely

The single load-bearing criterion `C1_discrimination_delta_floor` is a **discrimination** criterion (arm vs arm), not an absolute or negative-control one. It has two halves:

| half | measured | threshold | result |
|---|---|---|---|
| mean cross-arm delta | 0.06359 | >= 0.02 | **passed** |
| seed consistency (`ZR > ZW`) | 0.40 | >= 0.60 | **failed** |

All four readiness preconditions read `measured: 0.8, threshold: 0.8, met: true`, so the driver did not self-route `substrate_not_ready_requeue`; `criteria_non_degenerate.C1_discrimination_delta` is `true` and the run is not flagged by the indexer. `pending_review.md` lists it under plain "FAIL (action required)" with no failure signature.

This is **not** the substrate-ceiling fingerprint ("negative control passes, every discrimination criterion fails") -- there is only one criterion and no scored absolute control. The R0 mechanism-off leg that was meant to serve as a control observed a single E3 tick and recorded zero `no_z_goal` reasons (`all_no_z_goal: false`), so **it is vacuous as executed** and nothing gated on it.

### Per-seed table

| seed | ZR delta | ZW delta | d = ZR - ZW | ZR ticks | ZW ticks | ZR steps | ZW steps | readiness |
|---|---|---|---|---|---|---|---|---|
| 42 | 0.19555 | 0.07273 | **+0.12282** | 133 | 51 | 2173 | 1642 | met |
| 43 | 0.00000 | 0.00000 | +0.00000 | 0 | 0 | 191 | 175 | **failed both arms** |
| 45 | 0.12082 | 0.13164 | **-0.01082** | 27 | 137 | 874 | 2957 | met |
| 46 | 0.18090 | 0.25611 | **-0.07521** | **3** | 177 | 300 | 2952 | met |
| 47 | 0.30256 | 0.02141 | **+0.28115** | 126 | 33 | 2218 | 708 | met |

Recomputed mean = `0.06358935228319865`, byte-identical to the manifest. The arithmetic is right; the statistic is the problem.

---

## 3. Adjudication question 1 -- is `weakens` the right reading of "mean clears 3x, only 2/5 seeds"?

**No, on four independent grounds. Any one of them would be enough to withhold `weakens`; together they make `non_contributory` the only honest direction.**

### 3a. The starved seed sits inside the criterion's own denominator, with a value it can never satisfy

`run_experiment()` computes C1 over **all five** seeds, not over the seeds that cleared readiness. `_run_cell` returns `statistics.fmean(discrim_samples) if discrim_samples else 0.0` -- so seed 43, which failed R1 and R2 in *both* arms (1 and 0 contacts across a 3750-step budget), contributes a **hardcoded 0.0**, not a measurement. Two mechanical consequences:

- It adds `d = 0.0 - 0.0 = 0.0` to the mean, diluting it toward zero.
- The seed test is a strict `gm_zr > gm_zw`, so `0.0 > 0.0` is **False**. Seed 43 can *never* enter the numerator while permanently occupying a denominator slot.

Maximum attainable seed fraction is therefore **0.8**, and the pre-registered 0.6 bar in practice demands **3 of the 4 informative seeds (75%)**, not 60%. This is the "completeness guard denominated on the realized seed list" shape: a gate that certifies the very under-run it should have excluded.

Readiness itself passed *only* because exactly one seed died -- every precondition reads 4/5 = 0.8 against a 0.8 threshold. A second dead seed anywhere would have driven all four to 0.6 and self-routed the whole run `non_contributory` / `substrate_not_ready_requeue`. **The run sits on the knife edge of its own readiness gate, and the seed that put it there is also inside the criterion it gates.**

### 3b. The three failing seeds are not near-zero -- and the direction is a coin flip

The brief asked whether the three non-passing seeds are near-zero or negative. Answer, precisely: one is a structural zero (seed 43, above) and **two are genuinely negative** -- seed 45 at `-0.01082` and seed 46 at `-0.07521`. So on the 4 informative seeds the split is **2 positive / 2 negative**:

- exact two-sided sign test: **p = 1.000**
- one-sample t on the 4 informative deltas: mean 0.07949, SD 0.15773, **t(3) = 1.008** (p ~ 0.39)
- **mean/SD = 0.504**

A per-seed *sign* bar of 3/5 requires an effect roughly the size of its own cross-seed SD (mean/SD near 1) to be reached reliably. The measured ratio is half that. **The bar was pre-registered (`SEED_PASS_FRACTION = 3.0/5.0`, driver line 322) but was not attainable at the measured dispersion at n = 5** -- and, per recording gap RG-3, no dispersion estimate was written to the manifest, so nobody could have checked that at the time.

### 3c. The mean that "clears the floor 3x" is carried by one seed

Leave-one-out on the as-run mean:

| dropped seed | mean | vs floor 0.02 |
|---|---|---|
| 42 | +0.04878 | clears |
| 43 | +0.07949 | clears |
| 45 | +0.08219 | clears |
| 46 | +0.09829 | clears |
| **47** | **+0.00920** | **below** |

On informative seeds only (n = 3 after the drop) it is +0.01226, also below. The mean half of C1 is one seed deep. Reporting "the mean clears the floor 3x" alongside "only 2/5 seeds" as if these were two independent facts overstates the first: they are the same seed talking twice.

### 3d. The verdict inverts under an aggregation the manifest already records

`mean_discrimination_delta` is a mean over **per-tick** contrasts. `mean_same_type_goal_match` and `mean_diff_type_goal_match` are means over **pooled entries**. Both are in the manifest. Recomputing C1 from the pooled form:

| variant | statistic | seeds | mean delta | seed fraction | C1 |
|---|---|---|---|---|---|
| A (as run, pre-registered) | per-tick | all 5 | +0.06359 | 0.40 | **FAIL** |
| B | per-tick | 4 informative | +0.07949 | 0.50 | **FAIL** |
| **C** | **pooled entry-weighted** | **all 5** | **+0.10317** | **0.60** | **PASS** |
| D | pooled entry-weighted | 4 informative | +0.12897 | 0.75 | **PASS** |

Variant C meets **both halves exactly as pre-registered** (`0.10317 >= 0.02`, `0.60 >= 0.60`). The two forms even disagree in **sign** on two `ARM_ZWORLD` cells (seed 42: pooled `-0.00460` vs per-tick `+0.07273`; seed 47: pooled `-0.01282` vs per-tick `+0.02141`) -- both flips in the direction that helps `ZWORLD`.

The driver is **not** in breach of its pre-registration: the per-tick form is what the docstring declares, and it followed it. The finding is that the pre-registration did not pin a *robust* statistic. The per-tick form weights every qualifying tick equally regardless of anchor-pool size, so early-in-episode ticks comparing one same-type against one different-type anchor count as much as late ticks with a well-populated pool -- and RG-2 (per-tick pool sizes never recorded) means the cause cannot be localised from the manifest.

**A PASS/FAIL verdict that inverts on an undeclared analysis choice is not evidence against a claim in either direction.**

### 3e. And the DV is confounded with survival

| seed | more `total_steps` | higher delta | agree |
|---|---|---|---|
| 42 | ZR (2173 vs 1642) | ZR | yes |
| 45 | ZW (874 vs 2957) | ZW | yes |
| 46 | ZW (300 vs 2952) | ZW | yes |
| 47 | ZR (2218 vs 708) | ZR | yes |

**4 of 4.** Across the 8 informative cells, Spearman(`total_steps`, delta) = 0.50 and Spearman(`n_qualifying_ticks`, delta) = 0.48. `total_steps` ranges 191-2957 against a 3750 budget with `num_hazards = 0`, so episodes terminate early by very different amounts per cell. Because `agent.reset()` wipes the SD-039 anchor set at every episode boundary, pool size is bound to episode length -- and pool size is what the DV is computed over. The manipulated flag changes behaviour, behaviour changes episode length, episode length changes the DV. The driver's DV-SYMMETRY block enumerates and dismisses exactly one confound (type-clustered spatial resource placement, correctly dismissed by construction) and does not consider this one.

**Conclusion on question 1:** neither `weakens` nor a simple "under-powered but real". The run is `non_contributory` for MECH-162 -- and would remain so even if it had passed, because of question 2.

---

## 4. Adjudication question 2 -- did the test let the claim express itself?

**No. It tested a substitution where the claim asserts a convergence, and the claim's own notes said so in advance.**

MECH-162, verbatim: "z_resource ... and z_world ... separate at the feedforward representation stage but **must re-converge at the hippocampal planning stage** for goal-directed navigation."

Its notes are more specific still:

- "whether z_resource feeds into the hippocampal planning module **alongside** z_world, enabling the planner to reason about 'where resources are likely to be' **given current spatial context**" -- *alongside*, and a joint computation of what-given-where;
- "the hippocampal module needs **both** 'what to seek' (z_resource) **and** 'where things are' (z_world)";
- "The different permutations of having **z_resource alone, z_world alone, and both fused** ... are unresolved and need systematic experimental testing. See Q-030."

**The claim named three permutations. The run built two -- the two "alone" arms -- and omitted the fused one, which is the only arm that instantiates the claim's positive condition.** A contrast between two instances of a claim's negative condition cannot weaken it.

This is not a criticism the driver could easily have avoided, because the omission is a **substrate absence**:

- `ree-v3/ree_core/agent.py::update_z_goal` (~11504):
  ```python
  use_resource = (getattr(self.config.latent, "use_resource_encoder", False)
                  and self._current_latent.z_resource is not None)
  seed_latent = (self._current_latent.z_resource if use_resource
                 else self._current_latent.z_world)
  ```
  A strict XOR. No config flag reaches a both-streams state.
- `ree-v3/ree_core/hippocampal/ghost_goal_bank.py::GhostGoalBank.rank` -- `grep -n z_world` returns exactly one hit, inside a comment. The four live scoring terms are `wanting` (weight 0.0 this run), `goal_match` (cosine of the single seeded latent against the stored `z_goal_snapshot`), `staleness`, `recoverability`. The anchors this driver writes **do** carry `z_world` and it is never consulted.
- The one composite-cue channel that exists, MECH-339 `use_composite_cue_outshining`, defaults `False` with `context_weight 0.0` (`config.py:2364-2366`), is absent from this run's `enabled_default_off_flags`, and -- checked, because it looked like a candidate convergence path -- even when switched on derives its context term from `payload.arousal_tag` (`ghost_goal_bank.py:437`), explicitly **not** from spatial context. So it is not a re-convergence path either.

**Net: at the planning stage this run exercises, exactly one latent stream reaches the retrieval cue in either arm, and no operator anywhere in the substrate fuses the two.** MECH-162's own notes anticipated this -- "Current REE architecture treats z_resource and z_world as independent streams" -- and the claim exists precisely to assert that this should change.

### The second precondition failure: the identity arm had no identity

`ree_core/latent/stack.py:288-291` documents `ResourceEncoder`'s phased protocol in terms:

> P0: Train ResourceEncoder on benefit_exposure supervision (aux head).
> P1: Activate goal seeding from z_resource in `update_z_goal()`.

This run activated **P1 with no P0**, and no gradient training of any kind (grep of the 940-line driver for `optim|backward|.train()|requires_grad|use_identity_classifier|pretrain` returns nothing). `z_resource` is the output of an untrained two-layer MLP on `world_obs`; `z_world` is a different untrained projection of the same observation. The arm contrast is between two random projections.

SD-015's own `what_would_answer` gives the size of that gap: `goal_resource_r` **0.93-0.96** trained (V3-EXQ-514o, under SD-057 on the `scaffolded_sd054_onboarding` curriculum) "up from the EXQ-085g baseline of **0.066-0.087**". And **no manipulation check was recorded here** (RG-1), so it is not established that `ARM_ZRESOURCE`'s cue carried *any* resource-identity information -- which is the one thing the whole design depends on.

The driver's defence -- "untrained predictors are the correct substrate state" because "MECH-162 asks whether the WIRING exists and carries type-discriminative content" -- is sound for the *wiring* half and does not transfer to the *content* half. Whether a latent encodes object identity invariant to position is exactly the property training produces; SD-015's own numbers say so.

Note also that this run does **not** meet SD-015's stated non-degeneracy preconditions (a)-(d): no SD-057 incentive token bank, no scaffolded curriculum, no MECH-306 drive floor, and `proximity_benefit_scale = 0.05` against SD-015's stated `>= 0.18`. Those preconditions are written for SD-015's own behavioural retest and are not formally binding on MECH-162; they are recorded because they name the configuration under which `z_resource` is *known* to carry identity content.

---

## 5. Biological-reference triage

**Closest mechanism:** dentate-gyrus binding of an internally-generated spatial map with externally-derived object identity, fed by parallel lateral (item) and medial (spatial) entorhinal streams originating in perirhinal and parahippocampal/postrhinal cortex.

The biology is not neutral here -- it is a direct existence proof *for* the claim:

- **Kim et al. 2015** (DG disruption, delayed-non-match-to-place; causal lesion-style, not correlational). The `targeted_review_q_030` entry states that DG "binds spatial map (z_world-equivalent) with object/event (z_resource-equivalent) information. **This supports MECH-162.**"
- **Staresina, Duncan & Davachi 2011** (PrC/PhC double dissociation with perceptual input equated): separate encoders feeding a shared associative locus; the entry says it "**directly supports** two REE commitments: SD-015 ... and MECH-162". It also notes a graded transitional zone, i.e. the separation is not strict.
- **Lee et al. 2021** (GIST; aggregate confidence 0.82, the strongest single anchor): "**The hippocampus should be the convergence point** where flexible integration happens (consistent with MECH-162 and ARC-007)."

**Is this a formal-definition import?** No. `is_formal_import: false`. REE's translation here is *incomplete*, not divergent: the separation half (SD-015's `z_resource` vs `z_world`) is a faithful translation of the PrC/PhC dissociation and is built; the convergence half -- the DG-analog operator that takes both afferents and produces a bound representation -- has no counterpart in the substrate at all.

**Does the failure resemble a missing-dependency signature?** Directly. What was observed is what the biology predicts if the binding locus were removed and only one afferent stream at a time were allowed to the planner: each single stream still carries *some* same-vs-different discrimination (both arms did, on every informative cell, 0.021-0.303), and neither dominates. Under the skill's core principle this is a **discovered prerequisite, not a falsification** -- and arguably weak positive evidence for the dependency itself.

**`lit_status: present`, scoped honestly.** PRESENT for the convergence claim: 11 entries across `targeted_review_q_030` (5, three naming MECH-162 explicitly) and `targeted_review_sd_015` (6, including Whittington 2022, the Tolman-Eichenbaum source the claim's notes cite). **ABSENT for the binding OPERATOR** -- named as an explicit gap by the strongest anchor: Lee 2021's entry records that "the convergence locus is named but the binding mechanism (concatenation, multiplicative gating, cross-attention, factor-graph product) is not specified". Neither review directory carries a `SYNTHESIS.md`, only `entries/`, so there is no roll-up to cite. **No `/lit-pull` is owed on the existence of the convergence**; a narrow one on the operator would serve the build below, and is the same gap Q-030 axis 3 already tracks.

---

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | The test could not let the claim express itself: two single-stream arms against a claim about two-stream convergence; the claim's own notes name a third, fused permutation that the substrate cannot provide. |
| Biological reference | **clear** | DG binding of spatial map with object identity; causal lesion evidence (Kim 2015), double dissociation (Staresina 2011), convergence-locus review (Lee 2021, conf 0.82). Existence proof for the class. The open biological question is the operator, not the convergence. |
| Prerequisites | **missing** | ResourceEncoder P0 training skipped while P1 activated; SD-015 (a direct `depends_on`) is itself `substrate_ceiling` / `pending_retest_after_substrate: true`; SD-015's non-degeneracy preconditions (a)-(d) unmet. |
| Implementation completeness | **absent** (for the claim's mechanism) / complete (for the channel exercised) | MECH-292/293 ghost retrieval is built and firing (`mech293_n_ghost_admitted_nonzero_frac` 0.50-0.965, `z_goal_stream.active_frac` 0.9815, no writer defect). The convergence operator does not exist: `update_z_goal` XOR; `rank()` never reads `z_world`; MECH-339's composite channel is off and arousal-sourced. |
| Environment adequacy | **partial** | 20% density gave abundant dual-type contact on 4/5 seeds (13-126 contacts/cell), but seed 43 got 1 and 0 contacts across 3750 steps, and `ARM_ZRESOURCE` seed 46 sustained ~12 steps/episode against `ARM_ZWORLD`'s ~118 on the same seed with `num_hazards = 0`. `proximity_benefit_scale 0.05` vs SD-015's stated `>= 0.18`. |
| Measurement adequacy | **under-instrumented** | Sections 3a-3e: readiness-failed seed inside the denominator with a structurally-unsatisfiable 0.0; 59x unequal per-seed n weighted equally (3 to 177 ticks); verdict inverts under the pooled contrast in the same manifest; leave-one-out kills the mean; no dispersion, no pool sizes, no manipulation check recorded. |
| Integration adequacy | **partially coupled** | The manipulated flag changes behaviour; behaviour changes episode length; episode length changes the within-episode anchor pool the DV is computed over. 4/4 within-pair concordance with `total_steps`. |
| Scale / capacity | **likely insufficient** | Untrained predictors throughout; 4 informative seeds; one decisive cell estimated from 3 ticks; the R0 control leg observed a single tick and is vacuous as executed. |

### Failure-location summary (GOV-FAILLOC-1)

| bucket | verdict |
|---|---|
| MECHANISM | `not_established` -- the operator MECH-162 asserts is absent from the substrate |
| MEASURES | `not_established` -- see 3a-3d |
| ENVIRONMENT | `partial` -- one starved seed, 10x within-pair episode-length asymmetry |
| REE | **false** |

**Net classification: MIXED. Not chargeable to REE, and REE FAILED is neither reached nor asserted.** No prose anywhere in this artifact should be read as saying REE failed to do something; what happened is that an experiment asked a question its substrate could not represent, measured it with a statistic that does not survive its own sensitivity analysis, and did so on an untrained encoder.

---

## 7. Adjudication question 3 -- mixed vs weakens vs non_contributory

**Recommended: `non_contributory`.** The reasoning, stated against each alternative:

- **`weakens` is wrong** because the run never posed the claim. MECH-162 asserts that both streams must reach the planner; both arms give it one. A null between two negative conditions carries no information about the positive one. Independently, the direction is not stable (2/2 sign split, p = 1.000) and the verdict inverts under a same-manifest aggregation (section 3d). `weakens` would put the claim's only experimental entry on record as evidence against it, on a run that could not have produced evidence for it either.
- **`mixed` is wrong** because `mixed` asserts the evidence points both ways *on the claim*. It points **neither** way on the claim. The genuine positive in this run -- that the ghost-retrieval channel is live and content-sensitive from both latents -- is evidence about MECH-236/292/293, which are not tagged here. Calling it `mixed` would smuggle a read-across into MECH-162's own ledger.
- **`non_contributory` is right**, and the skill requires me to state the interpretable signal explicitly before using it. **The interpretable signal is:** (i) the MECH-292/293 waking ghost-goal retrieval channel is live and carries a genuine positive same-type-over-different-type discrimination from *both* seed latents on every informative cell, and (ii) the substrate contains no path by which the two latents can jointly reach the planning cue -- which is itself a concrete, actionable discovery about where MECH-162 is blocked. Both are recorded; neither is evidence for or against the claim's assertion.

**And the honest cost, stated rather than hidden.** MECH-162's `evidence:` list in `claims.yaml` is `[]`; the derived rollup carries exactly one entry, this run. So this recommendation returns MECH-162 to **zero scoring experimental entries**, resting on literature alone. The skill's illusory-conflict warning asks whether the remaining "supports" are narrow or single-pathway -- here there are no remaining supports at all, so no conflict is being resolved away; but the claim becomes explicitly lit-only and that must be visible in the note, not inferred. Given that the literature basis is unusually strong (causal DG-lesion evidence plus a double dissociation, both recorded by the reviews as supporting MECH-162), lit-only is a defensible resting state for a `candidate` claim pending its substrate.

**Recommended `epistemic_category`: `substrate_ceiling`** (one of the eight enum values; verified against `VALID_EPISTEMIC_CATEGORIES`). This is a deliberate assertion, not a placeholder, and the skill is explicit that the assertion is what GOV-CEIL-1 and the re-derive brake count. The assertion is: **MECH-162's answer is gated on substrate work that does not exist.** No config flag reaches the claim's positive condition, so no lettered re-issue of a two-arm design can decide it. The stamp is paired with a `recommended_substrate_queue_entry` with `action: create` naming the build, which is what distinguishes a ceiling from an instrument complaint. Consequences accepted knowingly: `substrate_ceiling` suppresses GOV-GRAN-1 granularity surfacing and marks MECH-162 not-v3-testable -- correct here, because MECH-162 should *not* be handed another two-arm experiment lane until the fused path exists. The failure-mode labels for this run (scope error, unmet training precondition, aggregation non-robustness, survival confound) live in the diagnosis and note fields, never in the category.

**Considered and rejected: `standard`.** The skill's default for "this run told us nothing about the claim" is `standard`, and part of this diagnosis (the measurement half) fits that family exactly. I am not choosing `standard` because the measurement problems are not the binding constraint: even a perfectly instrumented, adequately powered, trained-encoder version of *this design* still could not test MECH-162, because the apparatus has no fused arm. That is a substrate gate, and `standard` would leave MECH-162 in the v3-testable pool where the next session could reasonably queue V3-EXQ-997b and burn the same compute on the same unaskable question. **Recorded as a live disagreement for the Step 8 gate:** a reviewer who thinks the untrained encoder is the dominant fault -- and it is a serious one -- would land on `standard` plus a re-queue, and that reading is not unreasonable. It turns on whether one weights the scope error or the precondition error as primary. I weight the scope error primary because it is the one no re-run can fix.

**Considered and rejected: the V3-EXQ-642 shape.** The canonical warning is a run that self-routed `substrate_ceiling` on an untrained substrate where the correct route was re-queue. This target has the untrained-substrate feature, so the warning was checked directly. It does not apply, for two reasons: (i) here the *run* self-routed `weakens`, not a ceiling -- the ceiling is this autopsy's own reading, reached from a code read rather than from the run's numbers; (ii) the ceiling rests on a structural absence in the substrate (XOR seeding, no `z_world` in `rank()`) that no amount of training or re-running reaches, whereas 642's block was dissolved by re-queuing. The training gap is real and is routed separately, as the H1 probe explicitly **not** tagged as MECH-162 evidence.

---

## 8. Recurrence, brake, and cluster

- `granularity_debt_cluster.py MECH-162` -> **"0 target(s) across 0 file(s) -- no tagging targets. The trigger does NOT fire."** The `claim_alignment` distribution is empty because there are no prior tagging targets to classify. **Granularity-debt recurrence trigger: DOES NOT FIRE.** (Per the skill: a cluster in which no target reads `weakened` is not granularity debt -- here there is no cluster at all.)
- **Re-derive brake: DOES NOT FIRE.** The R1-R3 counting recipe run from `/Users/dgolden/REE_Working` with `CLAIM=MECH-162` returns **0** prior ceiling hits against a threshold of 2. This target is hit **1 of 2** under the convention: it carries a genuine `substrate_ceiling` category and owes a build (`action: create`), so it counts at predicate step 1. A second same-claim ceiling reading would fire the brake.
- `grep -rl MECH-162 REE_assembly/evidence/planning/failure_autopsy_*.json` -> no hits; no prior autopsy, confirmed or draft, touches MECH-162. This is the **first** adjudication of the claim.
- **Cluster scope: none.** No other pending or recently-reviewed FAIL shares MECH-162, the ghost-goal-bank substrate, or this failure shape. `scope: single`.

**Requeue is nonetheless refused, on scope grounds rather than brake grounds.** A two-arm lettered re-issue (`V3-EXQ-997a/b/...`) against the same substrate is explicitly refused: no two-arm substitution design can reach MECH-162's assertion, so another letter would spend compute on a question the apparatus cannot ask. A re-run of the two-arm design is worth queuing **only** as the H1 probe -- an SD-015 precondition test, tagged to SD-015, not to MECH-162.

---

## 9. Learning extracted

1. **A criterion computed over all seeds while its readiness gate is a run-level seed fraction lets a readiness-failed seed sit permanently in the denominator.** The `fmean(samples) if samples else 0.0` fallback made seed 43's contribution a hardcoded zero, and because the seed test is a strict `>`, that zero can never enter the numerator -- silently raising the effective bar from 60% to 75% of informative seeds. Aggregate over seeds that cleared readiness, or make the readiness gate per-seed-exclusionary.
2. **Pre-registering a DV formula is not the same as pre-registering a robust one.** Both aggregations are in this manifest, they differ in sign on two cells, and they invert the run's verdict. A driver that computes both owes a declaration of which is decisive and a reported sensitivity on the other.
3. **Recording gap, cheap and decision-blocking:** when the manipulation *is* "which latent seeds the cue", a per-arm manipulation check on the cue's content is owed. Per the Experimental Recording Standard the repair is *recording the readout* in the re-run, not re-running blind.
4. **Activating a module's P1 while skipping the P0 its own source documents is a precondition violation, not a scoping choice**, whenever the DV concerns the content the module encodes rather than the existence of its wiring.
5. **A claim asserting convergence of two streams is not tested by a substitution contrast between them.** MECH-162's notes enumerated three permutations; the run built two. Reading a claim's own notes for its named design space is the cheapest guard against this class of scope error.
6. **When the manipulated flag changes behaviour and the DV accumulates within an episode, episode length is a nuisance variable on the DV path.** DV-symmetry declarations should enumerate behaviour-mediated confounds, not only stimulus-side ones.
7. **A negative-control leg that observes a single tick has not run.** R0 recorded `n_e3_ticks_observed: 1`, `n_no_z_goal_reason: 0`, `all_no_z_goal: false` -- vacuous as executed, and because nothing gated on it, invisible in the verdict.

---

## 10. Routing

**`implement-substrate`.** Node classification (`work_graph_debt_vocabulary`):

- the fused-input smallest step is `complicated (buildable)` -- a named build with no open question, so build it rather than spiking to re-confirm it;
- the **operator** choice beyond that smallest step (concatenation vs multiplicative gating vs cross-attention vs factor-graph product -- the four Lee 2021's review names as unspecified) is `complex (probe-gated) / puzzle (known rules)` and belongs to Q-030 axis 3;
- the aggregation question (H2) is `mystery (known data)` -- the data that settles it is already in this manifest and **no new run is needed**.

### `recommended_substrate_queue_entry`: `action: create`

Checked first: `evidence/planning/substrate_queue.json` (169 entries) was searched by keyword over the full serialized queue for `z_resource`, `reconverg`, `re-converg`, `fusion`, `update_z_goal`, `z_goal`, `ghost_goal`, `MECH-162`, `Q-030`. `SD-015` exists (`implemented`, priority 1, `unblocks_claims: ["MECH-162", "Q-030", "INV-065"]`), as do `SD-039`, `MECH-292`, `MECH-293` (all `implemented`). **No entry, under any id, describes a fused or joint z_resource+z_world planning input, a change to `update_z_goal`'s XOR, or a `z_world` channel in the ghost-goal cue.** `create` is therefore correct rather than `amend`.

- `sd_id_suggested`: `zresource-zworld-planning-fusion`
- `priority_suggested`: **1** (governance Step 6a-ii.6 rule: >= 1 fresh failure record OR blocks >= 3 claims; this autopsy is a fresh failure record)
- `unblocks_claims`: `MECH-162`, `Q-030`
- `depends_on_unresolved`: SD-015 (its trained-encoder configuration is what makes any `z_resource` arm carry identity content; the fused arm inherits that precondition), MECH-339 (the existing composite-cue gate this build would extend)
- `substrate_paths`: `ree_core/agent.py::update_z_goal`, `ree_core/hippocampal/ghost_goal_bank.py::GhostGoalBank.rank`, `ree_core/hippocampal/ghost_goal_bank.py::_context_salience_for_anchor`, `ree_core/utils/config.py::GhostGoalBankConfig`
- **`severity`: deliberately LEFT UNSET.** Per the skill's own rule, `severity` is for a defect that has already been exercised; this is an *absent capability*, not a corrupting or degrading one. Nothing in the corpus produces wrong evidence because of it -- V3-EXQ-997 is the first run whose question required it, and the harm was a scope error in the experiment, not corrupted metrics. Leaving it unset is what keeps the `/queue-experiment` Step 2.5c gate from blocking unrelated experiments that merely touch `agent.py` or `ghost_goal_bank.py`, which would be the wrong outcome.
- `resolves_prior_failure_record`: none. This is a new, independent failure on a substrate gap nothing had articulated.

### `fanout_recommendation` (GOV-FANOUT-1) -- four live hypotheses, four axes

| id | hypothesis | axis | declared null |
|---|---|---|---|
| H1 | untrained-encoder artifact | representation | the trained arm's cue-identity readout is indistinguishable from the untrained one |
| H2 | aggregation artifact | instrumentation | per-tick and entry-weighted forms agree in sign on >= 4/5 seeds |
| H3 | fusion required, not substitution | world | the FUSED arm's discrimination does not exceed the max of the two single-stream arms by more than the cross-seed SD on a majority of seeds |
| H4 | survival/engagement confound | process | with episode length and tick count matched within seed, the arm contrast and its seed split are unchanged |

Sequencing and audit note: **H2 first** -- it needs no compute at all. H3 is gated on the build landing. H1 and H4 are independent and can run in parallel, but they **alias** (a trained encoder may also survive longer), so the H1 probe must carry H4's step/tick matching or the two verdicts cannot be separated.

### Follow-on this session does NOT chip

Per CLAUDE.md Session Land Protocol step 6 and the skill's Step 8 rule, a `/failure-autopsy` session does not `spawn_task` follow-on that depends on its own not-yet-ratified finding. Recorded here for `/governance` to chip after Step 2b/4/6a ratification: the H2 re-analysis, the H1 SD-015-tagged probe, the fused-input build via the substrate entry above, and an optional narrow `/lit-pull` on the binding operator (Q-030 axis 3). Governance should first check `evidence/planning/igw_routine_ledger.json` / `igw_assignments.json` for an auto-discovered duplicate of the build.

---

## 11. Draft `evidence_quality_note` for MECH-162

The exact text `/governance` should write is in the JSON artifact at `targets[0].recommended_evidence_quality_note`. It is not restated here to avoid the two copies drifting.

**`per_claim_recommendation` summary** (full text in the JSON):

| field | value |
|---|---|
| `recommended_evidence_direction` | `non_contributory` |
| `recommended_epistemic_category` | `substrate_ceiling` |
| `pending_retest_after_substrate` | `true` |
| `status_change` | `none -- stays candidate` |
| `change` tail | ends on `-> epistemic_category: substrate_ceiling` |

**Why that tail, checked against the claim's current values as the skill requires.** MECH-162 today carries `status: candidate`, `live_status.reading: candidate`, `evidence: []`, and **no `epistemic_category` field at all**, no `pending_retest_after_substrate`, and no `evidence_quality_note`. So `epistemic_category: substrate_ceiling` is both **storable** (a real `claims.yaml` field GOV-APPLY-1 can match) and **not yet true** (the field does not exist), which is exactly the working idiom the skill names for a claim whose status legitimately does not move. `STANDS` would be wrong -- there are three fields to write. A direction tail would have been wrong too: `evidence_direction` is a per-manifest field, not a claim field, so it clears only by provenance. The disposition changes more than one field, so the structured keys `recommended_epistemic_category` and `pending_retest_after_substrate` are set alongside `change` for GOV-APPLY-1 to check independently.

**`recommended_diagnostic_evidence_adjudicated` is deliberately NOT set.** `experiment_purpose` is `evidence`, not `diagnostic` or `baseline`; the skill is explicit that the flag must not be set for an evidence-purpose target, because it exists to mark an adjudicated-and-expected zero rather than to paper over a genuine evidence gap -- and a genuine evidence gap is precisely what MECH-162 has.

---

## 12. Step 7b fires

```
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/autopsy_pre_routing_checks.py \
  --artifact failure_autopsy_V3-EXQ-997_2026-09-04.json --json
```

**`fire_count: 0`, `inapplicable: []`.** No check fired, and on the second pass every check was able to look. Full output preserved at `7b_output.json`.

| check | outcome | disposition |
|---|---|---|
| C1-strict (a driver already exists for the recommended experiment) | no fire | Correct as far as it can see. The routing recommends a **build**, not an experiment; the eventual three-arm driver does not exist. Noted rather than dismissed: `experiments/v3_exq_997_...py` exists and a successor would likely reuse much of it, but a two-arm driver is not a driver for a three-arm design. |
| C2-strict (the recommended substrate entry already exists) | no fire | Consistent with my own keyword sweep of all 169 `substrate_queue.json` entries (section 10). `create` stands. |
| C3 (literature exists for a question declared ABSENT) | no fire | Expected -- `lit_status` is declared `present` with an explicit scope string ("PRESENT for the convergence claim itself ... ABSENT for the binding OPERATOR"). C3 cannot read scope, so its silence here is genuine rather than lucky. The scoped claim is nonetheless flagged for the Step 8 gate, which is where the skill says a human separates a correctly-scoped `absent` from a false one. |
| C5 (a run has already scored on a bed the prose calls unique or unrun) | no fire | Two-pass. The first pass, run before this `.md` existed, reported `inapplicable -- prose-keyed check, but no sibling .md narrative`; the check was re-run after writing this file and returned `fire_count: 0` with an EMPTY `inapplicable` list, i.e. C5 was able to read the prose and found nothing. Correct: this artifact makes no uniqueness or never-run assertion about the bed -- it says the opposite, that the two-arm design has been run and reproduced exactly (the queue note's internal-verification figures are byte-identical to the official run's). |
| C6-narrow (a metric agrees across arms in most seeds and dissents in a minority, against a prose absolute) | no fire | Worth stating why this is not a false negative: C6-narrow looks for a dissenting minority against a prose absolute. This artifact asserts no such absolute -- it asserts the opposite, that the metric splits 2/2 and is not robust. The skill's warning is that C6-narrow **cannot** see the mirror-image shape (a metric constant where the design requires it to vary), which must be tested by hand. Tested: the DV is *not* constant (per-tick 0.021-0.303 across informative cells, `non_degenerate: true`), so that shape does not apply. What the DV *is* pinned by is examined in section 3e -- episode length, not the manipulation. |

`inapplicable` is not "no fire" -- but `claim_ids` is non-empty (`["MECH-162"]`) and the claim resolves in `claims.yaml`, so the claim-keyed checks C1/C2/C3 were able to look. The load carried by the Step 7c red-team pass is therefore normal, not elevated.

**Step 7c red-team:** deliberately NOT run by this session. Per the staging brief, the parent `/governance` session owns the 7c pass, and this session does not hold the Step 8 gate.

---

## 13. Open questions this autopsy could not settle

1. **Why do the per-tick and entry-weighted contrasts disagree in sign on two `ARM_ZWORLD` cells?** The mechanism is presumably unequal pool sizes across ticks (a Simpson-style reweighting), but per-tick `n_same` / `n_diff` were computed and discarded (RG-2), so it cannot be confirmed from the manifest. This is H2's probe and is settleable from a re-instrumented re-run, or possibly from the run pack if per-tick data were retained anywhere (it was not -- `metrics.json` is `{"values": {}}`).
2. **Did `ARM_ZRESOURCE`'s cue carry *any* identity content?** Unanswerable from what was recorded (RG-1). SD-015's 0.066-0.087 untrained baseline is the best available prior, not a measurement of this run.
3. **Which fusion operator?** Genuinely open, and named as open by the literature itself (Lee 2021). The build above deliberately proposes the cheapest operator as a smallest step rather than settling this.
4. **Should the `epistemic_category` be `substrate_ceiling` or `standard`?** Set out as a live disagreement in section 7. It turns on whether the scope error or the training precondition is primary. This is exactly the kind of call the Step 8 gate exists for, and it should be put to the user rather than treated as settled by this draft.


## Red-team pass (Step 7c) and revision -- 2026-09-04T14:40:25Z

**Reviewer:** Fable 5.1 (separate agent, reasoning withheld, JSON-first). **Verdict: CONTESTED. Contest ACCEPTED** by the confirming governance session (governance-20260904-1347).

**F1 (verdict-moving, confirmed by the session at `ree_core/hippocampal/module.py:2658`).** The draft's absolute -- no operator anywhere fuses z_resource with z_world at the planning stage; the positive condition is unobservable -- is FALSE. `HippocampalModule._propose_ghost_seeded` (module.py:2576-2706) ranks MECH-292 bank anchors by `goal_match` against the z_resource-derived `current_z_goal`, then seeds each ghost probe's CEM init and E2 rollout at `anchor.z_world`. That is a live identity-cue -> spatial-content retrieval operator, and it was ON in this run (ghost probes admitted 0.50-0.965). The draft had grepped `z_world` inside `GhostGoalBank.rank()` only. What survives: `update_z_goal` is XOR and `rank()` never reads z_world, so no JOINT-REPRESENTATION operator exists -- the binding-operator gap Lee 2021 names is real -- but the claim's positive condition is not structurally unobservable.

**Consequences applied:** `recommended_epistemic_category` substrate_ceiling -> **standard** (measurement-primary; R3 clause 2, does not count toward the MECH-162 brake); H0 ALIVE, not eliminated on structure; `recommended_substrate_queue_entry.action` create -> **none** (the create text is retained under `withdrawn_readings_2026_09_04` for reuse if the redesign shows a joint operator is genuinely absent); routing implement-substrate -> **queue-experiment** (explicit three-permutation retest with the retrieval form on and the instrument defects fixed -- a same-claim re-issue is legitimate at brake count 0). Q-030's standing 2026-05-02 note ('hippocampal fusion ... no substrate enrichment required') is now consistent with this artifact rather than contradicted by it.

**F2.** Episode length is downstream of navigation competence (`done = _health_depleted or _step_cap_reached`, causal_grid_world.py:3206-3208; no hazards -> starvation), so H4's 'nuisance variable' framing had an unstated premise; it is a mediator. Direction unaffected.

**F3 (hygiene, strengthens).** The R0 mechanism-off leg is structurally unpassable: disabling `use_mech293_ghost_probes` disables all four `mech293_reason` emit sites, hence `reasons_observed: [""]`.

**F4.** The entry-weighted 'inverts to PASS' recompute is carried entirely by ARM_ZRESOURCE seed 46 (3 qualifying ticks) and lands exactly on the 0.60 bar. Non-robustness of the verdict survives; the PASS rhetoric is softened accordingly.

**What survived unchanged:** `non_contributory` over the manifest's `weakens` on measurement grounds alone; every recomputed number (per-tick 0.06359 / 0.40; entry-weighted 0.10317 / 0.60; LOO-47 0.0092; t(3)=1.008; Spearman 0.50/0.48; 4/4 longer-arm wins; 0.8 attainable-fraction cap); the untrained-ResourceEncoder premise; the literature citations; no duplicate registry question.

Withdrawn readings are recorded, not deleted: see `withdrawn_readings_2026_09_04` in the JSON.


## Confirmation -- 2026-09-04T18:55:13Z

Status **confirmed** at the /governance Step 8 gate (session governance-20260904-1347, user present). Decisions: {"Q1": "Apply all four as revised", "Q2_SD031_gate": "Amend SD-031 what_would_answer + self_attribution GAP-6 to accept construction-balanced (RandomPolicy, offline-scored) comparator-only designs for the ARC-065 diversity half", "Q3": "Add 6 buildable v3 substrate stubs", "Q4": "Apply the three August staging-autopsy ledger blocks now", "recommendation_agreement": "3 of 4 recommended options selected (Q4 against); logged via record_recommendation_outcome.py"}
