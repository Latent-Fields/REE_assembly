# Failure autopsy -- V3-EXQ-1062a (MECH-055, affect channel separation, post-shift)

- **Run:** `v3_exq_1062a_mech055_affect_channel_separation_postshift_20260923T002356Z_v3`
- **Queue id:** V3-EXQ-1062a | **Claim:** MECH-055 | **supersedes:** V3-EXQ-1062
- **Outcome:** FAIL | **experiment_purpose:** diagnostic | **self-route:** `substrate_not_ready_requeue`
- **Machine:** ree-cloud-2 (`linux-x86_64-py3.10-torch2.12.0+cpu`) | **elapsed:** 12,676 s (~3.5 h)
- **Seeds:** 42, 137, 2026 | **substrate_hash:** `091d4a02…a628b`
- **Status:** awaiting_human_confirmation
- **Autopsy triggers:** BOTH -- a FAIL, and an `experiment_purpose: diagnostic` result.

## 0. Dry-run gate (Step 2a)

`check_dry_run_citations.py` over both cited run_ids: **0 dry cited, 2 clean** (exit 0). `dry_run_checked: true` means the checker was run, not a raw field read (GOV-DRY-1). `excluded_dry_run_ids: []`.

`validate_recording.py` **OK** -- always-core complete. One advisory: `C1_harm_channels_not_redundant` carries no attainable bar (`measured: NaN`), which is correct here and is the finding, not a gap.

## 1. Facts

| arm | interval | gate | harm_a_forward_r2 | **persistence_r2** | **skill vs persistence** | action sens. |
|---|---|---|---|---|---|---|
| ARM_0_STATIONARY | 0 | **GREEN** | 0.947 / 0.941 / 0.977 | 0.9993 / 0.9881 / 0.9991 | **-71.67 / -3.98 / -23.48** | 0.460 / 1.135 / 0.716 |
| ARM_2_HIGH_SHIFT | 10 | **RED** | 0.896 / 0.941 / 0.934 | 0.9851 / 0.9820 / 0.9693 | **-5.99 / -2.28 / -1.16** | 0.461 / 1.185 / 1.021 |

Shift arm failed exactly two readiness preconditions, both cross-arm:

| precondition | measured | threshold | V3-EXQ-1062 |
|---|---|---|---|
| `harm_exposure_relative_deviation_bounded` | **3.282** (~4.28x) | 0.25 upper | 3.276 -- **unmoved** |
| `pe_load_elevated_vs_stationary` | **+0.0242** | 0.05 lower | -0.0332 -- sign flipped |

Its other six passed, including `world_rule_shift_fired_in_p2` (180 vs a 0.5 floor).

Criteria: C1 **not evaluated** (`scored_arms: []`, `NaN`); C2 **PASSED** (0.0851 vs 0.8 ceiling, 3/3 seeds); C3 not evaluated; C4 passed.

### 1a. The onset fix worked -- verified in the cells

- `n_world_rule_shifts_before_p2` = **0 in all six cells** (V3-EXQ-1062: ~810)
- `action_map_canonical_at_p2_onset` = **true in all six cells**
- `n_world_rule_shifts_p2` = **180** per shift cell

The trained-then-shifted premise was instantiated for the first time. That is what makes this the first clean test of H2.

## 2. Claim layer

MECH-055: `candidate`, `epistemic_category: standard`, `diagnostic_evidence_adjudicated: true`, `depends_on` ARC-005 / MECH-048 / MECH-054 / MECH-035. **No `pending_retest_after_substrate` field** (absent, not set false), no `evidence_quality_note`. `claim_ids` is exactly `["MECH-055"]` -- correctly scoped.

Per the no-blending rule: a **strong-lit / zero-exp** claim (5 literature entries, `genuine_exp_count` 0). Reported separately.

## 3. Biological reference

V3-EXQ-1062's triage stands: BLA valence-specific level coding (Namburi 2015) vs dACC surprise signalling (Hayden 2011), wanting/liking inside the valence channel (Berridge 2009). A **faithful translation, not a formal import**; literature present; **no `/lit-pull` owed.**

What this run adds is a dependency the biology assumes and the substrate does not supply: a forward model whose residual carries *world surprise* rather than *model error*.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact -- untested** | C1/C3 never evaluated |
| Biological reference | **clear** | no divergence, no lit owed |
| Prerequisites | **missing** | head fails to beat z(t-1) in **6/6 cells** |
| Implementation | **partial** | head present, trained, action-sensitive -- and net worse than identity |
| Environment | **partial -- wrong pressures PERSIST** | onset fixed; **exposure unchanged at 4.28x** |
| Measurement | **under-instrumented at the GATE** | persistence baseline recorded and fired; the gating precondition still has no baseline |
| Integration | **coupled but inert -- BY STARVED UPSTREAM** | Implementation not downgraded on this account |
| Scale / capacity | **adequate** | worst cell clears the fresh-select floor by 19% |

### Failure-location summary (GOV-FAILLOC-1)

`mechanism: not_established` / `measures: not_established` / `environment: not_established` / `ree: false`.

**Net: MIXED across all three. Not chargeable to REE, not chargeable to MECH-055.**

> Corrected at the Step 7c red-team pass. An earlier draft graded Environment `established` on the strength of the onset fix alone -- while the exposure deviation the predecessor had filed under Environment was **unchanged** (3.276 -> 3.282). Fixing one half of a layer does not earn the layer.

## 5. The central adjudication

### 5a. The harm-forward head does not beat the trivial predictor, anywhere

`skill = 1 - SSE_model / SSE_persistence` against `z_pred = z_harm_a(t-1)`. **Negative in 6 of 6 cells**, both arms, every seed. `persistence_r2` is 0.969-0.999: `z_harm_a` is a `harm_history_len=10` latent, very nearly a random walk at this step size.

So `dacc._affective_pe`, which axis 3 routes on, is dominated by model error. It is neither the clean LEVEL the readiness gate was written to exclude nor the forward-model residual the claim requires.

**Magnitude caveat, and it matters for citation.** Skill is denominator-driven: `1-persistence_r2` spans 0.00073 to 0.01194 -- a **16.4x spread across three seeds at an identical config** -- so -71.7 is a seed whose latent barely moved, not a 72x-worse model. **The robust claim is the SIGN (6/6), not the magnitude.**

**What the arithmetic says about the CAUSE.** `(1-r2)/(1-persistence_r2)` = 72.7 / 5.0 / 24.5 (stationary), 7.0 / 3.3 / 2.2 (shift): the model's residual RMS is **1.5-8.5x the latent's true per-step displacement**. This matters because it points *away* from the displacement-ceiling story an earlier draft assumed. `ResidualHarmForward` is `z + delta(z, a)`; at the MSE optimum the conditional-mean delta is inside its hypothesis space, so a displacement ceiling predicts delta -> 0 and **skill ~ 0, not -72**. A skill of -72 requires the head to be *actively adding* error -- non-convergence, train/eval mismatch (P1 epsilon 0.1 vs P2 epsilon 0.0), or overfitting. **And the manifest records no training-loss trajectory for `e2_harm_a`, so convergence cannot be checked from the artifact at all.**

### 5b. The readiness gate that certified it cannot discriminate

`harm_a_forward_r2_supra_floor` exists, in its own words, so that "axis 3 is [not] a LEVEL rather than a forward-model residual ... a starved criterion, not a falsified one." It gates on an **absolute** R^2 floor of 0.30 (`FORWARD_R2_MIN`, in the **driver** at `:496`, not in `ree_core`). It passed at **0.9405** while the trivial predictor scores **0.9955**.

This is the CLAUDE.md negative-instrument failure in textbook form: a gate with no baseline, uninformative on an autocorrelated signal. The run **already computes** the discriminating statistic as a RECORDED, deliberately non-gating instrument. The change is to gate on it.

**Read-across (recorded per Step 1, out of this target's scope):** this retro-weakens the `Prerequisites: present` row of `failure_autopsy_V3-EXQ-1062_2026-09-22.md` section 4, which rested on exactly the figure now shown to be below baseline, and removes the corroborating force of its section 5a. That is not a criticism of the predecessor -- it is the instrument that autopsy prescribed, doing its job one run later. No re-adjudication of V3-EXQ-1062 is proposed.

### 5c. H2 is PARTIALLY supported; H3 splits

- **H2 (the model adapted because it TRAINED under the shift) -- PARTIALLY SUPPORTED on 2/3 seeds.** Read on the raw `harm_a_forward_r2` gap (0.0315 mean) this looks unsupported. Read on **unexplained variance** it does not: `1-r2` goes 0.0528 -> 0.1042 (**1.97x**) on seed 42 and 0.0227 -> 0.0664 (**2.93x**) on seed 2026, with seed 137 flat at 0.99x. With the confound removed, the lever **does** reach the harm-forward model's residual on two of three seeds. What fails is the dACC PE *magnitude* floor (+2.4% pooled vs +5.0%; per-seed +6.9% / -1.2% / -1.9%). No pre-registered threshold existed for the gap itself, so this is a directional read, not a verdict.
  > Corrected at the red-team pass: an earlier draft read this as "the predicted divergence did not appear."
- **H3 (persistence-dominated) -- SPLITS.** Its *consequence* is **confirmed** (6/6 cells). The mechanism **eliminated** is the one the **1062a driver** stated (a delta driven toward zero, an action-BLIND head; `drv62a:100-105`) -- *not* the V3-EXQ-1062 autopsy's wording, which named no delta->0 mechanism. `harm_forward_action_sensitivity` is 0.46-1.19, above its floor.

  Caveat on that statistic: it is normalised by the model's **own** predicted delta, which section 5a shows is 1.5-8.5x too large. So it means "the action moves a wrong delta by 46-119% of its wrong size" -- it must not be quoted as evidence the head reads the action *correctly*.

### 5d. Three successor routes are closed -- and one cheap one is open

1. **A longer P0** -- closed by the predecessor: neither failing precondition is a function of warmup length.
2. **A dose ladder** -- closed. The predecessor's routing step 3 was conditional: *"Only then ladder the dose -- and only if (1)+(2) show the residual can move at all."* Instrument (2) reports it cannot.
3. **A shorter measurement window** -- closed by the non-gating early-window copies recorded to answer exactly this: `harm_exposure_rel_dev_early` **1.804** (vs a 0.25 ceiling) and `pe_elevation_early` **0.0132** (vs a 0.05 floor). A windowed successor does not clear the pre-registered bars without moving them.

**Open and cheap:** the **under-training** probe (section 8 fan-out). It is a `/queue-experiment` diagnostic on a different mechanism, not a re-run of C1.

## 6. Interpretable signal

1. **The head is worse than trivial, 6/6 cells** -- first measurement of its kind on this channel.
2. **H2 partially supported under a clean test** -- the lever reaches the model's residual on 2/3 seeds; the PE magnitude floor is what fails.
3. **The onset fix works and moved PE elevation the right way** (-0.0332 -> +0.0242) while leaving exposure untouched -- so the 4.28x exposure deviation is a property of *the lever*, not of the schedule.
4. **C2 passed again, 3/3 seeds** against falsifier (i) -- evidence against the collapsed-harm-scalar reading *at rest*, twice now.

## 6b. Instrument findings

1. **LOAD-BEARING** -- the readiness gate has no baseline (5b). Remedy: gate on skill-vs-persistence.
2. **RECORDING GAP** -- no training-loss trajectory for `e2_harm_a`, so convergence is uncheckable from the manifest. This is *recording*-debt, not measurement-debt: the readout existed at run time and was not written. Cite the Experimental Recording Standard in the successor spec.
3. **CARRIED FORWARD, not fixed** -- `dv_symmetry_note` still says "three arms" while `config.arms` carries **two**. Instrument finding #4 of the predecessor, recurring verbatim after being explicitly prescribed.
4. **CARRIED FORWARD, reader caution** -- `substrate_stable_across_run: false` over-reads again: one distinct cell hash, post-run *disk* drift only. Do not discard the run on it.
5. **POSITIVE -- two of four prescriptions WERE applied**: `structural_min`/`structural_max` now declared (9 occurrences), `mean_prec_norm` rolled into the flat readout.

## 6c. Mechanical pre-routing checks (7b)

One fire, **C2, ACTED ON**: `action='create'` while `SD-PP-B4` already unblocks MECH-055 and went unmentioned. The entry now names B4, records why it is not the amend target, and carries two annotations owed on its open record. Re-run clean.

## 7. Re-derive brake and recurrence

**Brake FIRES.** `RE_DERIVE_BRAKE_THRESHOLD = 2`. Counted under R1-R3: 1 prior hit (`failure_autopsy_V3-EXQ-1062_2026-09-22`) + this target = **2**. The red-team pass independently executed `validate_queue._autopsy_counts_toward_brake` on both targets and reproduced the count.

- Routing is **`/implement-substrate`** on a named upstream entry.
- **A same-claim re-queue is REFUSED**: no V3-EXQ-1062b at any dose, schedule or measurement window -- all three routes are closed (5d).
- **Scope of the refusal, stated because it matters here:** it is *not* a refusal of the under-training probe. That is a new EXQ number on a different mechanism (head convergence) with a different DV (skill-vs-persistence) and no MECH-055 tag -- the redesign exemption the brake rule states explicitly. Flagged, because the brake routes to `/implement-substrate` while the cheapest next step is a `/queue-experiment` diagnostic.

**Granularity-debt trigger: does NOT fire.** 1 tagging target, alignment `intact=1`, **no target reads `weakened`** -- measurement/implementation debt.

## 8. Routing

**`/implement-substrate`**, with the cheapest leg running first as a `/queue-experiment` diagnostic.

**Substrate: `create` `SD-PP-B9-harm-forward-below-persistence-baseline`**, severity **`degrading`**, priority 1, paths `ree_core/latent/stack.py::ResidualHarmForward` and `ree_core/predictors/e2_harm_a.py::E2HarmAForward`.

> The entry's registered subject is the **observation**, not an asserted cause -- corrected at the red-team pass, where an earlier draft named it `…-z-harm-a-per-step-displacement-range` and asserted a displacement ceiling the arithmetic points away from (5a).

> `severity` was lowered from `corrupting`. Both consumers are default-OFF (`use_e2_harm_a` config.py:3883, `use_dacc` config.py:3910) -- the same fact the sibling V3-EXQ-1075 artifact uses to argue `degrading`, and applying it there but not here would be inconsistent. No landed evidence is shown to be corrupted. `corrupting` would have blocked every dACC and `e2_harm_a` experiment at priority 1, including the MECH-258/268 family.

> `ree_core/cingulate/dacc.py::_affective_pe` was **removed** from `substrate_paths`: it is a consumer (`pe = ||z_harm_a - z_harm_a_pred||`) and nothing in it is defective. `unblocks_claims` was narrowed to MECH-055 **partial**, and **MECH-054 removed** -- its registered precondition is a *benefit*-side channel, which a harm-head fix does not supply.

**Why `create` and not an amend of SD-PP-B4:** B4's subject is the ONSET lever, and that gap is no longer what blocks this claim -- its own documented workaround was applied and worked. Two annotations are owed on its open record: the workaround is now *demonstrated*, and its "no prior run has ever measured whether this lever moves the dACC harm-PE channel" is **PARTIALLY answered** -- the lever reaches the model's residual on 2/3 seeds but not the PE magnitude floor. (Not "it does not": writing that into a shared substrate record would misinform every future consumer of the lever.)

**GOV-FANOUT-1: four legs, four axes.** The single-unambiguous-build exemption is not claimed.

| leg | axis | probe | declared null |
|---|---|---|---|
| **H1-exposure-error-coupling** | environment | exposure-matched decoupling design, or a different lever | no setting holds exposure within 1.25x while moving the PE |
| **H-harm-head-undertrained** *(cheapest)* | learning-signal | train to convergence on a **recorded** loss curve, batch > 1, matched epsilon | skill stays <= 0 at convergence |
| **H-pe-source-structurally-wrong** | readout | ensemble-disagreement / innovation-variance PE vs the residual-head PE | no better separated from the VALENCE_HARM level |
| **H-harm-head-representation-ceiling** | representation-update-rate | vary `harm_history_len` / displacement | skill stays <= 0 at every setting |

Ordering matters: **the under-training leg is cheapest and the arithmetic favours it, so the substrate build must not be commissioned ahead of it.** The instrument fix and the recording fix are owed on *all four* branches and gated on none.

**Claim layer:** direction `non_contributory`; category **HOLD `standard`**. What moves is `pending_retest_after_substrate` -> **true** (the field is currently *absent*; the predecessor recommended `false` and governance applied only `diagnostic_evidence_adjudicated`).

### Judgement calls flagged for the user

- **Category held at `standard`, not `substrate_ceiling`.** The substance is a ceiling. But `substrate_ceiling` puts MECH-055 into `_EPI_SUPPRESS_PROPOSAL` *and* marks it not-v3-testable, starving it of lanes -- while falsifier (i) / C2 remains scoreable today and has passed 3/3 seeds twice. Same call the predecessor made, now under more pressure.
- **The brake routes to `/implement-substrate` while the cheapest probe is a `/queue-experiment` diagnostic.** Handled above under the redesign exemption, but flagged explicitly so governance does not read the brake as forbidding the under-training run.

## 9. Red-team record (Step 7c)

**Model: `fable` (claude-fable-5-1)** -- cross-model; this session drafted on Opus 5, and the drafting reasoning was withheld. **Verdict: CONTESTED**, four contested findings, **all accepted**.

Independently re-verified from the cells before acceptance: the per-seed `1-r2` ratios (1.97x / 0.99x / 2.93x); `(1-r2)/(1-persistence_r2)` = 72.7 / 5.0 / 24.5 with a 16.4x denominator spread; and both default-off config flags.

It did **not** move: the 6/6 negative-skill finding, the verified onset fix, the gate's inability to discriminate, the brake firing, `non_contributory`, or the `standard` category.

**The pass was aimed at routing rather than arithmetic, per the skill's measured guidance, and that is exactly where it landed: all four contested findings changed recommendations -- an environment grade, a shared substrate record's wording, the created entry's registered subject, and a severity that would have blocked the dACC experiment family. None changed the science.**

## Step 8 gate

**CONFIRMED by the user, 2026-09-23T07:52:00Z.** Three judgement calls put to the gate, all confirmed as recommended, no change to the drafted routing required:

1. **MECH-055 `epistemic_category`: HOLD `standard`** (`rec-20260923-120f3c68`) -- the ceiling reading is carried by `pending_retest_after_substrate` and the note, keeping the falsifier-(i) / C2 lane open.
2. **Severity `degrading` on BOTH substrate entries** (`rec-20260923-30611285`) -- consistent across the pair on the identical default-OFF argument; no Step 2.5c block on the dACC family or on the shared `action_sensitivity_gate.py`.
3. **Cheap probes FIRST** (`rec-20260923-0ecb56f1`) -- the under-training probe (V3-EXQ-1062a) and the margin re-rung (V3-EXQ-1075) run as `/queue-experiment` diagnostics before any substrate build is commissioned. Both are new EXQ numbers on different mechanisms, falling under the re-derive brake's explicit redesign exemption.

## Step 9b -- frozen hypothesis-space ledger

Integrity audit after the append: **a=0 b=2 c=3 d=0** -- all five flags are **pre-existing on other questions** (`zworld_actor_adequacy_locus`, `mech467_legc_event_denominator_cause`, `sd_e1_var_bar_readout_crush`). **Zero flags on this question**, and its growth appears in the *Advisory -- labelled fan-out growth* section, which is where a legitimate append belongs. Pre-registration provenance: 27 git-witnessed, 0 unverifiable.
The question registered here reads `convergence_class: scattering`. That is the honest verdict and worth stating: after this run the question spans **five** axis families rather than narrowing, because the Step 7c pass demoted the draft's assumed displacement-ceiling cause to one hypothesis among four. Scattering is not a failure -- but it is a further reason to run the cheapest leg before commissioning any build.
