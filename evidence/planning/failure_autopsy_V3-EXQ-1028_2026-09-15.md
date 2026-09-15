# Failure autopsy -- V3-EXQ-1028 (SD-082 fan-out portfolio, legs 2 + 4: the extended-budget learning-signal run)

- **Generated:** 2026-09-15T20:19:10Z
- **Status:** `awaiting_human_confirmation` -- **STAGING MODE draft.** The Step 8 interactive gate was NOT held and routing is NOT final. The next `/governance` walk (Step 1.5) gates this draft; that is where `evidence_direction` is applied.
- **Scope:** single (one run, two independently-scored legs of one GOV-FANOUT-1 portfolio)
- **Run:** `v3_exq_1028_sd082_learning_signal_extended_budget_20260914T223157Z_v3` -- **PASS**, `experiment_purpose: diagnostic`, self-route label `c2_noisy__c3_sign_null`. Autopsy required by trigger 2 (every diagnostic, PASS or FAIL, flagged or not).
- **Claim:** SD-082. Registry question `sd082_candidate_discriminating_readout_locus` (co-registered SD-078, not tagged).
- **Fan-out source:** confirmed `failure_autopsy_V3-EXQ-1020_2026-09-11`, ratified gov-20260911-1612; chip `chip-20260911-sd082-fanout-portfolio-v2`. Siblings V3-EXQ-1027 and V3-EXQ-1029 were adjudicated in confirmed `failure_autopsy_V3-EXQ-1027-1029-cluster_2026-09-14`, which explicitly did **not** adjudicate this run.
- **Revision adjudicated:** the flat manifest at **REE_assembly `141dc756ee70f6145548cb7c23746971b3e4d491`** (`HEAD == origin/master`), read via `git show origin/master:<path>`. The shared working-tree copy was byte-identical (171300 bytes) at read time; an earlier ` M` on the path had cleared. The manifest was **read only** and never modified.
- **Routing (DRAFT, not gated):** `governance-note-only`. No build owed, no new experiment owed by this autopsy, no `/lit-pull` owed. Substrate queue: `amend` SD-082 (bookkeeping -- failure record, `validation_experiment` extension, closure of the V3-EXQ-1020 record). `severity` / `substrate_paths` unchanged.
- **Step 7b:** 0 fires (C7 structurally inapplicable). **Step 7c:** **CONTESTED**, cross-model (Fable red team; Opus drafter), 3 substantive + 4 hygiene findings, **all verified by the drafter and folded in** -- section 10a. The largest change: the H-learning-signal-sign ledger recommendation moved from `eliminated` to `alive`.

---

## 0. THE P1 BUDGET READING (what `chip-20260915-sd082-readout-consequence-successor` is waiting for)

> ### **P1 = 300 updates.**
>
> **Primary number (the persistence reading the cluster asked for): `n_persistent = 0` of 5.**
> **Manifest field: `criteria[1].n_persistent`**, where `criteria[1].name == "C2_windowed_persistence_noisy"`; mirrored as **`readout.n_c2_persistent`**.
>
> Two independent routes converge on 300. **Route A (criterion power) is primary** and does not depend on any ceiling claim. **Route B (persistence) is the literal reading requested**, and is reported with its limits. **This is a recommended budget, not a refusal of anything larger** -- see "Do not over-read" below.

### Route A -- criterion power (primary)

The binding constraint on any successor is that the load-bearing C3 leg only *scores* when a cell has **>= 50 init-head flip ticks in each half of P1** and `n_eps >= 100`. Below that it returns `c3_starved` -- exactly the failure V3-EXQ-1020 hit. That question has a direct answer, recomputed here from the run's own per-episode cells (`arm_results[].per_episode_init_flip_ticks`, `[].per_episode_init_live_fresh_ticks`) by truncating P1 at T and re-applying the driver's own rule:

| Budget T | all 5 seeds scoreable? | worst half-count (floor 50) | margin |
|---|---|---|---|
| 150 | **NO** -- 611 (45) and 655 (48) starve | 45 | fails |
| 200 | yes | 54 | 1.08x -- no margin |
| **300** | **yes** | **70** | **1.40x -- recommended** |
| 400 | yes | 99 | 1.98x |
| 500 | yes | 132 | 2.64x (the realised run) |

**300 is the smallest budget at which the run's own load-bearing criterion scores on 5/5 seeds with real margin.**

### Route B -- the persistence reading

The pre-registered windowed classifier finds **no persistently-directed gradient anywhere in the 500-update budget**. `n_persistent = 0` of 5 in W4 = [300, realised end]:

| Seed | W4 persistence | noise floor | W4 midpoint | above noise by | below midpoint by |
|---|---|---|---|---|---|
| 611 | 0.2378 | 0.2889 | 0.4950 | -0.0511 | 0.2571 |
| 622 | 0.4550 | 0.2896 | 0.5014 | **+0.1654** | **0.0464** |
| 633 | 0.4945 | 0.2889 | 0.5053 | **+0.2056** | **0.0108** |
| 644 | 0.2909 | 0.2889 | 0.4879 | +0.0020 | 0.1969 |
| 655 | 0.3497 | 0.2889 | 0.4887 | +0.0608 | 0.1390 |

The full profile as **fractional position in the bracket** -- `(persistence - noise) / (synth - noise)`, where `0.5` is the midpoint C2 tests against -- shows the same across the whole budget:

| Seed | W1 [0,70] | W2 [70,150] | W3 [150,300] | W4 [300,end] | C2 class |
|---|---|---|---|---|---|
| 611 | **0.717** | 0.067 | 0.334 | -0.124 | exhausted |
| 622 | -0.186 | -0.046 | 0.012 | 0.390 | noisy |
| 633 | 0.355 | 0.139 | **0.517** | 0.475 | noisy |
| 644 | 0.119 | -0.014 | 0.383 | 0.005 | noisy |
| 655 | **0.594** | 0.388 | **0.584** | 0.152 | exhausted |
| **seed mean** | **0.320** | **0.107** | **0.366** | **0.180** | |

The seed mean never reaches the midpoint in any window; only **4 of 20** seed-windows sit at or above it, **none in W2 or W4**. So **a longer budget is not the lever** that resolves this lineage's question -- which is the useful negative the cluster wanted.

**Route B's limits, stated rather than assumed away (red-team F2, verified):**

- `n_persistent = 0` is a true **classifier count**, and must not be read as "nothing happens after update 300".
- **Seed 633's W4 is 0.0108 below its midpoint, while the W4 midpoint's own across-seed realisation spread is 0.0174** -- inside control-realisation noise of crossing.
- **Seed 622's W4 sits 0.1654 above the pure-noise floor and is that seed's *most* directed window**, on a profile that rises monotonically (-0.186 -> -0.046 -> +0.012 -> +0.390). The three-way classifier has no label for "late-rising", so that shape is invisible to it.
- The window brackets are **single realisations with no reported SE**, measured on **fresh-init heads** while the real run's late windows step a **mid-training Adam**. The driver records this as a known approximation; the **direction** of any residual bias is **not measured**. A genuine late signal on the two marginal seeds could be masked by a mis-set W4 bracket.

### What does NOT support the budget (withdrawn)

An earlier draft cited "76-96% (median 86) of the trained-head flip-rate decay is complete by episode 300" as corroboration. **That claim is withdrawn** (red-team F3, verified). It is an *additive* share denominated on the run's own endpoint and **front-loads by construction** for any monotone decay toward an asymptote, so it cannot evidence a ceiling. In **ratio** terms the 300-500 stretch is still doing substantial work: flip rate falls a further **1.30x (611), 5.02x (622), 2.06x (633), 13.22x (644), 1.44x (655)**.

What *is* robust from that readout: flip suppression is real and monotone on 5/5 seeds (Spearman -0.549 to -0.661). It corroborates that the head is learning throughout the budget -- **not** that there is a ceiling.

### Recommendation, and what not to derive from it

**Set P1 = 300 updates** (= 300 P1 episodes, one update per episode), on route A, with route B agreeing that more budget is not the lever.

**Do not over-read.** This artifact **does not refuse a budget above 300**, and no such refusal should be derived from it:

1. The ceiling reading rests on a bracket whose control approximation is **unmeasured in direction**, with two seeds at or near the boundary.
2. In ratio terms the flip rate is still falling materially after episode 300 on 2 of 5 seeds.
3. **Most importantly, the successor runs a different gradient** -- P1 under **authority ON** with the `gated_policy` channel controlled. Nothing measured under the authority-OFF imitation regime bounds what that regime needs.

300 is a well-founded **starting** budget with its criterion-power margin computed. The successor **must record its own** windowed-persistence profile and per-half init-flip-tick counts so its budget can be re-read in its own regime rather than inherited.

### Which cluster disposition this answers, and one citation correction

The obligation is carried by the **C1** pre-routing fire's disposition in `failure_autopsy_V3-EXQ-1027-1029-cluster_2026-09-14` ("the successor's P1 budget is to be set from 1028's persistence reading, and `/queue-experiment` must read 1028's confirmed autopsy before queuing it") and by that artifact's section 9 ("queue only after 1028's confirmed autopsy sets the P1 budget"). The chip brief for this autopsy cited it as the **C7** disposition; C7 in that artifact is the *dismissed* `live_rule_state_zero_frac` item. Substance unaffected -- recorded so the pointer resolves.

---

## 1. Why this run existed

`failure_autopsy_V3-EXQ-1020_2026-09-11` closed 822f's blind-instrument ambiguity but settled neither pre-registered learning-signal leg: C2 passed on a bare 3-of-5 majority, and C3 was **starved** -- 4 fresh-select flip samples in the worst cell against a floor of 20, only 4 of 10 cells eligible. The user selected a four-leg portfolio; V3-EXQ-1028 carries legs 2 and 4:

| Leg | Hypothesis | Axis | Run |
|---|---|---|---|
| 1 | H-replay-rule-state-mismatch | credit-assignment | V3-EXQ-1027 (**eliminated**, cluster artifact) |
| **2** | **H-learning-signal-sign** | **measurement** | **V3-EXQ-1028 (this artifact)** |
| 3 | H-selection-authority-bounded | intrinsic-architecture | V3-EXQ-1029 (**confirmed**, cluster artifact) |
| **4** | **H-learning-signal-noisy** | **process** | **V3-EXQ-1028 (this artifact)** |

The design is 1020's ARM_ON cell (same seeds, P0 60, 48 steps, optimiser hyperparameters imported from the 1020 module) with four changes: P1 = 500 instead of 70; one arm only; persistence snapshotted at 70/150/300/end to give four windows; and every fresh rule-live P1 tick additionally labelled with the **frozen init head's** flip. The driver was red-teamed at queue time (fable, CONTESTED, four findings all fixed -- section 5).

---

## 2. Facts

### 2.1 Gates

**Dry-run gate (Step 2a).** `check_dry_run_citations.py` over all four cited run_ids -> **0 dry cited, 0 ambiguous, 4 clean**, exit 0; `--family v3_exq_1028` -> **0 dry / 1 real**. The manifest carries `dry_run: false` **and** a non-dry `run_id` shape, so `_is_dry_run()` is negative on **both** disjuncts (not a raw-field read). `validate_experiments.py --checks dry_run_unreachable_criterion` -> 11 warnings fleet-wide, **all** in `v3_exq_543*`, **silent** on this driver. Moot in any case: this is a full-budget run (`update_realisation` 0.998-1.000), not a smoke. `excluded_dry_run_ids: []`.

**Recording provenance.** `validate_recording.py` -> **1 complete, 0 always-core gaps**, 0 thin-pack drops, 0 flat-scalar findings, 0 criteria-re-derivability findings, 0 schema warnings. `recording_schema` rec/v1; `substrate_hash` 30631916f9bdeb80...; `substrate_commit` ree-v3 `6e5c34f1548054...` (clean, main); `machine_class` darwin-arm64-py3.13-torch2.12.0; `elapsed_seconds` 27952.68; full `config`; explicit `seeds`. **No recording gap blocks this adjudication.** Two *notes*: (a) the flat readout surfaces only W1/W4 scalars, but `arm_results[].windows` carries all four windows with their controls -- which is what makes section 0 readable; (b) **the window controls are single realisations with no SE**, load-bearing for the two marginal seeds.

**Readiness -- 4 of 4 met.**

| Gate | measured | threshold |
|---|---|---|
| control bracket separates at every window length | 1.00 | >= 0.8 |
| worst cell realised updates / intended | 0.998 (seed 622) | >= 0.95 |
| candidate-summary fallbacks | 0.0 of 22188 calls | 0.0 |
| flip fraction resolvable (worst-cell P1 ticks) | 11830 | >= 200 |

### 2.2 Criteria

| Criterion | load-bearing | passed | measured / threshold | detail |
|---|---|---|---|---|
| C1_gradient_present | yes | **yes** | 5 / 3 | worst median grad norm 0.0106 vs a 1e-6 floor; 0 non-finite |
| C2_windowed_persistence_noisy | yes | **yes** | 3 / 3 | **3 noisy (622,633,644), 2 exhausted (611,655), 0 persistent** |
| C3_episode_advantage_on_init_flips_negative | yes | **no** | 0 / 3 | 5/5 scoreable; 0 negative, 0 positive |
| C4_return_variance_present | no | yes | 5 / 3 | return variance 0.16-0.34 vs a 1e-4 floor |
| R1020_C3 (1020's statistic, recorded) | **no** | n/a | -- | **points the other way -- section 6.2** |

`combination_rule`: **outcome PASS iff readiness AND C1**; C2 and C3 are independent legs (`criteria_aggregation: any`). `criteria_non_degenerate` true for all four.

**So the PASS is an instrument-liveness PASS, not a hypothesis confirmation.** It is not a `vacuous_pass` -- every non-degeneracy flag is true, the gradient is live, both legs returned real readings. Its scientific content lives entirely in the label, `c2_noisy__c3_sign_null`.

### 2.3 C3 -- the load-bearing statistic

| Seed | r_local | r_grand | +/-2 SE band | scoreable | n_eps | init-flip ticks (1st / 2nd half) |
|---|---|---|---|---|---|---|
| 611 | +0.0454 | +0.0512 | 0.0911 | yes | 482 | 160 / 186 |
| 622 | +0.0202 | +0.0172 | 0.0916 | yes | 477 | 220 / 178 |
| 633 | +0.0175 | +0.0149 | 0.0909 | yes | 484 | 251 / 291 |
| 644 | +0.0053 | -0.0203 | 0.0906 | yes | 487 | 341 / 345 |
| 655 | -0.0024 | +0.0081 | 0.0925 | yes | 468 | 145 / 132 |

Every seed clears the scoreability floor with 2.6x-6.9x headroom; every `r_local` sits well inside its band. **0 negative, 0 positive -> `sign_null`.** This is a well-powered null *on this statistic* -- see 6.2 for the statistic that disagrees.

---

## 3. Claim layer

SD-082 (`design_decision`; status `candidate_substrate_landed`; `epistemic_category: standard`; `pending_retest_after_substrate: false`; `diagnostic_evidence_adjudicated: true`; `live_status.evidence.from = failure_autopsy_V3-EXQ-1027-1029-cluster_2026-09-14`) asserts a **common-mode-invariant, gradient-trainable readout mapping the SD-078 rule_state to the SD-033a per-candidate action bias**.

**This run does not test that content.** It characterises the *learning signal* delivered to that head over a long budget. Per the confirmed cluster autopsy, with `use_modulatory_selection_authority` OFF the readout is empirically inert at selection (0 of 1694 raw-identical co-fresh ticks change E3's argmin; 0 of 13857 sampled actions), so the P1 REINFORCE surrogate is -- to measurement precision -- **advantage-weighted imitation of E3**. 1028 therefore measures the imitation gradient. SD-082 could not express itself here and is **neither supported nor weakened**: direction `non_contributory`.

`claim_ids` accurate (SD-082 only; SD-078 co-registered on the question but correctly untagged). SD-082's stored `standard` carries **no stale re-check condition** -- checked by reading the category's prose in `evidence_quality_note`, not just its value. No clinical / out-of-domain trap: SD-082 is a substrate design decision tested in its own substrate.

---

## 4. Biological triage

- **Closest reference:** three-factor (dopamine-gated) corticostriatal plasticity -- outcome credit binds to synapses that **participated** in the selected action, held by an eligibility trace until the outcome arrives.
- **Dependencies, and their status here:** participation of the modulatory signal in the selected action -- **absent** (authority OFF; 0/1694 by 1029); an eligibility trace binding credit to the action-time state -- **tested and eliminated as the binding constraint** by 1027; an outcome signal whose variance is attributable to the modulated pathway -- **absent** (per-episode returns bit-identical across arms differing only in the head, 1027).
- **The formal import, and the divergence.** The P1 optimiser is a REINFORCE surrogate `log_softmax(-bias/T)` over the head's **own** output, with the action chosen by E3 and one per-episode scalar advantage broadcast to every sample. Biology's credit assignment **requires** participation and so cannot be satisfied by a pathway that does not reach the action; the formal import does **not** require participation and therefore **cannot detect its own absence** -- it returns a well-formed gradient regardless. **1028 measures what that gradient looks like over a long budget.** Load-bearing for the successor's *design*, not for SD-082's truth.
- **Does the failure resemble a missing dependency?** Yes -- the signature of an optimiser fed a target uncorrelated with the quantity it is nominally credited for. Discovered-prerequisite reading, not falsification.
- **Literature:** `targeted_review_sd_082` exists (8 entries). **No `/lit-pull` owed.**

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | SD-082's content untested; the run measures the imitation gradient |
| Biological reference | partial | three-factor plasticity; the participation dependency is absent and the failure matches that absence |
| Prerequisites | **missing** | the readout's participation in selection (authority OFF) -- the *same* prerequisite the cluster located; 1028 was queued before that finding landed |
| Implementation | **complete** | 4/4 readiness gates; C1 5/5; 0 non-finite gradients; 0 summary fallbacks in 22188 calls |
| Environment | **adequate** | C4 return variance 5/5 (0.16-0.34) |
| Measurement | **adequate, with two construct-validity limits** | the queue-time fixes held and C3 scores 5/5; **but** C2 aggregates over non-exchangeable seeds, and the W4 bracket rests on an unmeasured control approximation |
| Integration | isolated | head trains but is decoupled from selection (established by 1029) |
| Scale | **adequate** | T = 500 is 7.1x 1020's T = 70 -- what makes both the exhaustion and the criterion-power questions answerable |

**Did the queue-time red-team fixes hold? Yes, all four** -- and this is the difference between this run and a confidently wrong one.

- **F1 (windowing).** Every seed's *cumulative* persistence at T=500 sits below the cumulative midpoint (`cumulative_below_midpoint_T` true 5/5), so the endpoint read the windowing replaced would have returned **5 of 5 "noisy"** -- a false unanimity. The windowed read returns 3 noisy / 2 exhausted. The controls confirm the drift the fix targeted: the synthetic ceiling falls from ~0.73 at L=70 to ~0.69-0.72 at L=500 while the noise floor falls from 0.449 to ~0.289.
- **F2 (episode-level C3 on frozen init-head labels).** Converted a starved leg (4 samples in 1020's worst cell) into 5/5 scoreable with 2.6x-6.9x headroom.
- **F3 (`c3_degenerate` branch).** Not exercised -- C4 passed 5/5 -- but present and correct.
- **F4 (realised-length controls + 95% gate).** Exercised: seed 622 realised 499/500, cleared at 0.998, and its W4 control ran at the realised length 199.

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Verdict |
|---|---|
| MECHANISM FAILED | **not_established** -- the mechanism SD-082 asserts was never in this run's causal path (authority OFF), so no verdict is available |
| MEASURES FAILED | **partial** -- all gates passed, but C2's majority rule cannot deliver a population verdict on non-exchangeable units, and the W4 bracket rests on an unmeasured approximation |
| ENVIRONMENT FAILED | **established** (adequate) |
| REE FAILED | **false** |

**Net: MIXED -- not chargeable to REE, and not a mechanism failure.** REE FAILED is not reachable here and is asserted nowhere in this artifact.

### Epistemic category

**`standard`** (in `VALID_EPISTEMIC_CATEGORIES`). The failure mode -- a measurement-construct question on both legs -- is recorded in `recommended_epistemic_category_note`, not in the category field.

**On the ceiling fingerprint (red-team F6).** "Absolute/negative-control passes, discrimination fails" *is* the substrate-ceiling fingerprint named in SKILL.md, and `failed_criterion: discrimination` is the key `check_granularity_debt_recurrence` reads -- so state plainly that **it is not a ceiling here.** A ceiling reading asserts the claim's answer is gated on substrate work; nothing here is. SD-082's mechanism was never in the run's causal path, so the discrimination criterion was not measuring the claim's substrate at all -- and the discrimination that failed belongs to a fan-out **leg**, not to SD-082. Nor is it an instrument defect: the four queue-time fixes held and the criterion 1020 starved now scores on 5/5.

---

## 6. The two leg readings

### 6.1 H-learning-signal-noisy -- supported on the bar, not generalisable

The rule: `>= 3 of 5 seeds "noisy"` -> supported. Measured: **3 noisy, 2 exhausted, 0 persistent** -- passing at *exactly* the threshold.

**The problem is the unit of aggregation, and this run establishes it.** The rule treats the 5 seeds as exchangeable. They are not -- the partition is a **deterministic function of seed identity**, reproduced three times:

| Seed | 1020 ARM_ON (T=70) | 1027 REPLAY_FAITHFUL (T=70) | 1028 W1 = [0,70] | delta 1028-1020 | class |
|---|---|---|---|---|---|
| 611 | 0.6523358904 | 0.6523358904 | 0.6523409881 | +5.1e-06 | high |
| 622 | 0.4059154962 | 0.4059154962 | 0.3966097002 | **-9.3e-03** | low |
| 633 | 0.5582378368 | 0.5582378368 | 0.5582631871 | +2.5e-05 | low |
| 644 | 0.4814996453 | 0.4814996453 | 0.4814964629 | -3.2e-06 | low |
| 655 | 0.6196014333 | 0.6196014333 | 0.6195964989 | -4.9e-06 | high |

1027's FAITHFUL arm is **bit-identical** to 1020's ARM_ON (same machine class). 1028's W1 agrees **within 2.5e-5** on the four seeds that realised all 70 updates -- **across machine classes** (linux-x86_64/py3.10-torch2.12.0+cpu vs darwin-arm64/py3.13-torch2.12.0) and three substrate hashes. Stronger still: **per-episode returns are bit-identical** between 1020 ARM_ON and 1028 for **all 5 seeds** over those first 70 P1 episodes. Seed 622's -9.3e-03 is the single seed that realised **69 of 70** updates in 1020/1027 (and 499/500 here), so its window covers a different update *set* by one -- a mechanically explained exception on identical trajectories.

The partition `{622,633,644}` low / `{611,655}` high is therefore fixed by the seed. A bare 3-of-5 over such units is a property of **the seed set** -- the identical criticism 1028's own driver levelled at 1020. **The extended budget reproduced that weakness rather than resolving it.** Seed 622 additionally carries a late-**rising** profile the three-way classifier has no label for.

**What the budget extension did settle:** the "directed then exhausted" alternative is measured rather than aliased -- 2 of 5 seeds genuinely directed early and exhausted late, 0 of 5 persistently directed by the classifier's bar.

### 6.2 H-learning-signal-sign -- two statistics that disagree, so the leg stays alive

This is where the red team changed the artifact's conclusion.

**The load-bearing statistic** (episode-level Pearson r on frozen-init-head labels -- the redesign that fixed 1020's starvation) returns `sign_null`: 5/5 scoreable, `r_local` +0.045 to -0.002 against bands of ~0.091, 0 negative and 0 positive. It excludes `|r| > ~0.09`. And this is *not* the same result as 1020's: 1020's C3 was **unscoreable**; this one is **measured**.

**But the run also records 1020's own statistic, and it points the other way** (`criteria[4]`, `R1020_C3_trained_head_drawn_samples_recorded`, `load_bearing: false`):

| Seed | adv_flip_minus_nonflip | detrended | hold-weighted | n_flip_samples |
|---|---|---|---|---|
| 611 | **-0.0326** | -0.0211 | -0.0275 | 18 (below 1020's floor of 20) |
| 622 | +0.0369 | +0.0474 | **-0.0453** | 59 |
| 633 | **-0.0472** | -0.0228 | -0.0383 | 56 |
| 644 | **-0.0227** | -0.0286 | -0.0002 | 88 |
| 655 | **-0.0605** | -0.0365 | +0.0892 | 37 |

**Negative on 4 of 5 seeds** -- the direction the hypothesis asserts. Restricted to the 4 seeds clearing 1020's own `MIN_FLIP_SAMPLES=20` floor, **3 of 4 read negative, which on 1020's pre-registered rule is SUPPORTED.** The detrended and hold-weighted variants are each negative on 4 of 5 -- **but not the same 4** (622 flips negative under hold-weighting, 655 flips positive), and per-seed magnitudes are within roughly 1 SE, so the recorded statistic does not make the leg *supported* either.

**So the honest verdict is not elimination.** There is a defensible case that the load-bearing statistic should win -- it exists precisely because the recorded one starves and is confounded by early-P1 return trend -- but **that case was never pre-registered as a tie-break**, and eliminating a registered leg on a post-hoc preference between two recorded statistics is exactly the move the frozen ledger exists to prevent. **Recommended ledger state: `alive`, with both readings recorded.**

**What is nonetheless established:** the leg is no longer **starved**. 1020's unscoreability is discharged; the sign question is now a *measurement* question rather than an *instrument* question.

**A scope caveat, recorded not adjudicated (red-team F1(ii)):** the registry leg's label is a **consequence** claim ("a rule-driven argmax change is on average penalised"). With authority OFF no argmax change reaches the action at all (1029: 0/1694), and the driver itself calls its C3 "correlational by construction". By the same reasoning this artifact uses to say SD-082 could not express itself here, the leg's consequence form may not be testable in this configuration either. That strengthens `alive`, and is a design constraint for whichever run next adjudicates it.

---

## 7. Lineage checks

**Granularity-debt trigger: does NOT fire.** `granularity_debt_cluster.py SD-082` -> **8 tagging targets, alignment distribution `unclear=8`, zero `weakened`.** The reader's standing rule applies verbatim: a cluster in which no target reads `weakened` is measurement or implementation debt however many autopsies exist. The recurrence here is configuration and measurement debt -- the claim has never been tested under a regime where its mechanism was in the causal path. **No `/claim-synthesis` handoff owed.**

**Re-derive brake (R1-R3): literal count 5, brake does NOT fire on this target.**

| Autopsy | Run | stamped category |
|---|---|---|
| failure_autopsy_2026-07-28-sweep | v3_exq_822b | `competence_implementation_gap` (pre-2026-08-09 grandfathered) |
| failure_autopsy_V3-EXQ-822c_2026-08-29 | v3_exq_822c | `standard` |
| failure_autopsy_966-436g-951-959-822d-cluster_2026-08-30 | v3_exq_822d | `standard` |
| failure_autopsy_V3-EXQ-1027-1029-cluster_2026-09-14 | v3_exq_1027 | `standard` |
| failure_autopsy_V3-EXQ-1027-1029-cluster_2026-09-14 | v3_exq_1029 | `standard` |

**Not one of the five is a `substrate_ceiling` reading** (red-team F4 corrected an earlier draft that said all five read `standard`; 822b's grandfathered label is not a ceiling either, so the substantive point stands). All five reach the count only through R3 step (4)'s direction fallback on `non_contributory`, and zero of the 8 targets read `weakened`. **SD-082 has never had a ceiling reading in its history.** This target likewise reads `non_contributory` / `standard` with **no substrate build owed**, so the brake does not fire on it and the routing is not `implement-substrate`.

**REFUSED regardless of the count:** V3-EXQ-1028a or any same-design letter of this run under authority OFF (a byte-identical replay adjudicates nothing, and the budget question is answered); any further lettered iteration of the 822 / 1020 / 1028 design under authority OFF.
**LICENSED:** the successor already confirmed by the cluster artifact's section 9 -- a **new EXQ number**, a new adjudicating run for the alive registry leg H1, under authority ON with the `gated_policy` channel controlled, whose **P1 budget this artifact supplies**.

> **Honest stamp -- the producer release will not take effect, and that is stated rather than concealed.** Step (3)'s producer release is guarded by `if not owes_build`, and `_autopsy_owes_substrate_build()` returns `True` for `action == "amend"`. Because this target recommends a **bookkeeping** amend, `validate_queue.py::_autopsy_counts_toward_brake` and the mirrored skill recipes **will** count it, taking SD-082 to 6. The red team ran the predicate independently and confirmed this. The same interaction already voided the release the cluster artifact recorded: it asserts "no build owed ... step (3) explicit producer release ... so neither adds a hit" while setting `action: amend`, and the predicate counts both its targets anyway -- which is why the count reads 5 here and not the 3 that artifact recorded. The root issue is that **`amend` is overloaded**: it covers both "amend because a build is owed" and "append a failure record, no build owed". **No disposition here turns on it** (SD-082 is above threshold either way and no ceiling reading exists), and **no fix is proposed** -- flagged to `/governance` in section 11.

**Stale conditional category:** none on SD-082.

---

## 8. Learning extracted

1. **Seed identity is deterministic for the persistence class, reproduced three times across two machine classes** (6.1). Per-episode returns are **bit-identical** cross-class over the shared 70 episodes on 5/5 seeds; W1 persistence agrees within 2.5e-5 on the four seeds with full update realisation; 1027's FAITHFUL arm is bit-identical to 1020's ARM_ON.
2. **That makes C2's majority rule a statement about the seed set, not the population** -- the flaw 1028's own driver diagnosed in 1020 and then inherited. Successors must pre-register **seed identity as a factor**, report per-seed, and either use enough seeds for a majority to mean something or drop the majority framing.
3. **The budget question is answered by criterion power, not by a ceiling argument** -- and the two routes agree on 300. A budget grounded in what the criterion *needs* is more robust than one grounded in what the gradient *stopped doing*.
4. **A "fraction of total decay complete by T" statistic cannot evidence a ceiling, because it front-loads by construction.** This artifact's own draft made that error and the Step 7c red team caught it; in ratio terms the same data show a further 1.3x-13.2x reduction after episode 300. Generalisable: an additive share of a decay says nothing about where the decay stops.
5. **The windowing fix mattered and prevented a false unanimity** -- the endpoint read it replaced would have returned 5/5 "noisy".
6. **C3's redesign worked, and the lesson is sharp:** *a criterion whose sample count is produced by the effect under test must be labelled by a frozen reference, not by the trained object.*
7. **A run can carry two statistics for one hypothesis that disagree in direction, and which one wins must be pre-registered.** 1028's load-bearing r reads null while the recorded 1020-style difference-of-means reads negative on 4/5. Good design reasons favour the load-bearing one, but no pre-registered tie-break exists, so the leg cannot be resolved on this run. Future fan-out drivers that retain a superseded statistic "for comparability" should state in advance what happens when the two disagree.
8. **The lineage's brake count is an artefact of the `amend` overload, not of a ceiling** (section 7).

---

## 9. Routing (DRAFT -- not gated)

**Work-graph token:** `complex (probe-gated) / puzzle (known rules)` -- the frame is well-posed (registry leg H1's `decision_question`) and the missing fact is a single manipulation away, now with its budget parameter supplied and its criterion-power margin computed.

| Item | Routing | Detail |
|---|---|---|
| V3-EXQ-1028 | `governance-note-only` | note + citation re-point; no build, no new experiment, no lit-pull owed |
| Substrate queue | `amend` SD-082 | **bookkeeping only**: append the 1028 failure record, extend `validation_experiment`, close the V3-EXQ-1020 record. `severity` (`corrupting`) and `substrate_paths` (`[]`, emptied on purpose 2026-09-09) **unchanged** |
| Successor | owned by the **cluster** artifact | `/queue-experiment` must read section 0 -- **both routes and "do not over-read"** -- before queuing; governance chips it, not this autopsy |

**Closing the V3-EXQ-1020 failure record.** Both clauses are dispositioned. The **C2 clause** was discharged by 1027 per the cluster artifact, and 1028's W1 reproduces the identical partition a third time on a different machine class. The **C3 clause** ("advantage-sign leg UNSCOREABLE: 4 fresh-select flip samples ... only 4 of 10 cells eligible") is discharged **here**: the redesigned episode-level C3 scored on 5 of 5 cells with 132-345 init-head flip ticks per half against a floor of 50. The **starvation** is fixed and measured; the record can close as `resolved`. Note that closing it does **not** settle the sign question itself -- that leg stays alive, for the reason in 6.2.

**Draft `evidence_quality_note`:** exact text in the JSON `recommended_evidence_quality_note`. NOTE-ONLY, direction `non_contributory`; nothing stored moves; `live_status.evidence.from` re-pointed at this artifact.

---

## 10. Step 7b / 7c

**Step 7b -- `autopsy_pre_routing_checks.py`: 0 fires.** Run **twice** -- once before the `.md` existed (C5 then reported inapplicable for want of a narrative) and again after, so C5 was actually exercised and did not fire. `inapplicable`: **C7 only** -- no target manifest carries an arm-structured array with >= 2 arms, since this run has a single ARM_ON arm across 5 seeds, so C7 is structurally blind *by construction*, not merely quiet. Per SKILL.md, "inapplicable is NOT no fire", so C7's blindness was handled by hand: its mirror image -- *a metric constant where the design requires it to vary* -- was tested manually and is clean (persistence varies across seeds and windows, flip rates vary across blocks, returns vary, `r_local` varies in sign). C1/C2/C3 were **not** reported inapplicable, so they did look and found nothing.

### 10a. Step 7c -- adversarial red-team pass

**Verdict: CONTESTED.** Run on **claude-fable-5-1**, cross-model (this session drafted on **claude-opus-5**), with the enforced reading order: draft JSON -> raw evidence with load-bearing numbers recomputed from the manifest's own cells -> the `.md`, read specifically to test its absolutes. **Every finding below was independently re-verified by the drafter against the manifest before being accepted. None was accepted on assertion.**

| # | Severity | Finding | Disposition |
|---|---|---|---|
| **F1** | **severe / routing** | `eliminated` for H-learning-signal-sign is not earned: the run records 1020's own statistic negative on **4 of 5** seeds (3 of 4 eligible under 1020's sample floor = SUPPORTED on that rule), which the draft never mentioned; the leg's label is a consequence claim possibly untestable at authority OFF; elimination was beyond the pre-registration. | **ACCEPTED.** Ledger recommendation changed `eliminated` -> `alive`; withdrawn reading recorded as the gate alternative rather than deleted; section 6.2 rewritten to report both statistics. **The single largest change from the draft.** |
| **F2** | **assertion / standing refusal** | "Updates 300-500 contributed NO direction-consistent gradient on ANY seed" is contradicted by the cells -- 622's W4 is +0.165 above the noise floor and its most directed window; 633 is 0.011 below a midpoint whose spread is 0.017; the fresh-init control approximation's bias direction was never stated. | **ACCEPTED.** `n_persistent = 0` retained as a *classifier count*; ceiling language withdrawn; recommendation re-grounded on route A; marginal seeds and the control approximation stated; an explicit **"do not over-read"** block added refusing any derivation that budgets above 300 are forbidden. |
| **F3** | assertion | "86% of decay complete by episode 300" front-loads by construction and cannot evidence a ceiling; in ratio terms 300-500 still reduces flip rate materially. | **ACCEPTED.** Claim withdrawn from the recommendation; ratio figures (1.30x-13.22x) reported; recorded as learning 4. The effect is **larger** than the red team stated on two seeds. |
| F4 | hygiene | "all five stamped `standard`" is false -- 822b is `competence_implementation_gap`. | **ACCEPTED**, corrected in section 7. Substantive point (no ceiling among the five) unaffected. |
| F5 | hygiene | Draft JSON's `pre_routing_checks` / `red_team` were placeholders while the `.md` asserted results. | **ACCEPTED**; both now filled. |
| F6 | hygiene / routing-adjacent | `failed_criterion: discrimination` on a PASS is the ceiling fingerprint and the key `check_granularity_debt_recurrence` reads. | **ACCEPTED**; stamp retained (it factually names the failing criterion) with an explicit note in section 5 on why it is not a ceiling here. |
| F7 | hygiene | "well-powered" applied loosely; it belongs to C3, not C2. | **ACCEPTED**; scoped throughout. |

**Attacks that failed** (worked and did not land): the cross-machine-class reproduction and the seed-622 one-update explanation -- both verified, and the attack *strengthened* the finding; the brake-predicate claim -- the red team ran the predicate itself and confirmed the honest stamp is exactly right; the `change`-tail check -- every "does not move" field verified unchanged in claims.yaml, and `-> stamp this artifact` is both storable and not-yet-true, so GOV-APPLY-1 will not clear the row prematurely; declining the pre-registered CONFIRMED on H-noisy -- judged a disclosed departure in the conservative direction; `epistemic_category: standard` -- survived.

**Under-claims adopted from the red team:** per-episode returns are **bit-identical** cross-class (stronger than the 2.5e-5 the draft cited); seed 622's monotonically rising profile is effectively a **fourth class** the three-way classifier cannot express.

**A CONFIRMED verdict would not have been proof the artifact was clean, and a CONTESTED one is not proof it is now.** The 7b layer (0 fires) and this 7c layer are not nested in either direction; neither suppresses the other.

---

## 11. Follow-on owed to `/governance` (this autopsy spawns no chips)

1. Apply the `per_claim_recommendation` to SD-082 -- append the note, re-point `live_status.evidence.from`. No status / category / flag changes.
2. Apply the substrate_queue `amend` on SD-082, including closing the V3-EXQ-1020 failure record. `severity` and `substrate_paths` unchanged.
3. **Gate the two ledger recommendations against their stated alternatives** (both are "stay alive, record basis"; both alternatives recorded), then apply, then `build_hypothesis_space.py` + `check_hypothesis_space_integrity.py`, committed with the registry's three derive-only siblings. **Net ledger delta if applied as recommended: 0 added, 0 resolved, `initial_frozen_count` unchanged at 9.**
4. Chip the SD-082 successor to `/queue-experiment` -- the cluster artifact's already-confirmed routing, now unblocked because section 0 supplies P1 = 300 with its criterion-power margin, the seed-as-factor constraint, and the requirement that the successor record its own profile rather than inherit this budget.
5. Resolve `chip-20260915-sd082-readout-consequence-successor`, which was waiting on exactly section 0.
6. **Infrastructure finding, not owed by this diagnosis:** the re-derive brake's step (3) producer release is unreachable whenever `recommended_substrate_queue_entry.action == "amend"` (section 7). Any fix touches `ree-v3/validate_queue.py` and **both** skill copies of the recipe in lockstep, with a corpus scan, per the lockstep rule in failure-autopsy SKILL.md Step 7.
7. **Consider, not owed:** fan-out drivers that retain a superseded statistic "for comparability" should pre-register what happens when it disagrees with the load-bearing one. 1028 is the case that shows the gap (learning 7).

---

## 12. Concurrency note

Written from the **main checkout** `/Users/dgolden/REE_Working` (not a worktree), under two claims: `autopsy-staging-1028-20260915` (directory scope `REE_assembly/evidence/experiments/`; overlap NOTES expected and seen) and `autopsy-staging-1028-20260915-artifact` (the two artifact paths, uncontended). The 1028 manifest was read from `origin/master` rather than the working tree because a concurrent writer had shown a ` M` on it at task-assignment time; by read time the two were byte-identical, and the manifest was never modified. `hypothesis_space_registry.v1.json` was **read only** -- staging mode does not write it -- so no registry claim was required and none was opened. No coordination-plane pause claim was opened: this session runs as a supervised subagent of the metaworker orchestrator, which owns that plane, and staging mode writes none of the resources the pause protects. No other dirty file in the shared checkout was touched.
