# Failure autopsy -- V3-EXQ-1075 (SD-PP-B5 validation: does the action-margin loss make e2.world_forward read its action?)

- **Run:** `v3_exq_1075_sdppb5_action_sensitivity_validation_20260923T033329Z_v3`
- **Queue id:** V3-EXQ-1075 | **Claims:** *none* (`claim_ids: []`, deliberately) | **validates_substrate:** `SD-PP-B5-z-world-per-step-displacement-range`
- **Outcome:** FAIL | **experiment_purpose:** diagnostic | **self-route:** `readability_bought_at_reconstruction_cost` (FAIL-b)
- **Machine:** ree-cloud-2 | **elapsed:** 157 s | **Seeds:** 42, 123, 456 | **substrate_hash:** `440f7aa5…129bc2`
- **Status:** awaiting_human_confirmation | **Trigger:** `experiment_purpose: diagnostic` (and a FAIL)

`bears_on`: `SD-PP-B5`, `v3_binding_constraint_observation_interface`. **Required** -- `claim_ids` is empty, so this target accumulates on neither the re-derive brake nor GOV-CEIL-1, and `check_diagnostic_chain_recurrence.py` keys on this field alone.

## 0. Dry-run gate and provenance

`check_dry_run_citations.py`: 0 dry cited, clean. `validate_recording.py` **OK**.

## 1. Facts -- the full ladder, per seed

Five arms x 3 seeds. Only the margin term differs; rollout, budget, optimiser regime and the frozen 64-row / 5-distinct-action battery are bit-identical, enforced by two separate RNG streams.

| arm | margin | ratio (42/123/456) | skill vs identity | conv_rel_drop | MSE / OFF | margin_loss (% of margin) |
|---|---|---|---|---|---|---|
| ARM_OFF | -- | 0.8336 / 0.8790 / 0.7068 | -5.82 / -2.24 / -8.39 | .9847 / .9849 / .9916 | 1.00 | -- |
| M001 | 0.01 | 0.8628 / 0.7026 / 0.7377 | -4.47 / -1.99 / -4.93 | .9877 / .9860 / .9947 | 0.80 / 0.92 / 0.63 | 0.002-0.008% |
| M005 | 0.05 | 0.9949 / **1.0258** / 0.9106 | -12.06 / -18.10 / -9.81 | .9706 / .9108 / .9904 | 1.92 / **5.90** / 1.15 | 0.037-0.055% |
| M010 | **0.10** (config default) | **1.0540** / **1.0099** / 0.9826 | -32.89 / -30.18 / -47.57 | .9238 / .8543 / .9567 | 4.97 / **9.63** / 5.17 | 0.077-0.100% |
| M050 | 0.50 | **1.0109** / **1.0026** / **1.0015** | **-431 / -563 / -675** | .0282 / **-1.637** / .3977 | 63.4 / **174.2** / 72.0 | 0.68-1.04% |

Scored: A1 (ratio > 1.0) **0/1/2/3**; A3 (conv_rel_drop >= 0.99) **1/1/0/0**; A4 (MSE <= 2x OFF) **3/2/0/0**; A2 (skill vs identity, RECORDED not gated) **0/3 at every rung**. `passing_rungs: []`.

All five non-degeneracy preconditions met, including **N3** (ARM_OFF reproduces V3-EXQ-1073's blindness 3/3) and a **canary** replaying 1073's landed values on 3/3 seeds.

## 2. Claim layer

**No claim is tagged, and that is correct.** An earlier driver draft tagged MECH-573; once A2 was withdrawn as a gate (user decision `rec-20260923-cb59ede6`) the run no longer tests MECH-573's CONFIRMING clause, which needs a matched-`conv_rel_drop` comparison between a skill>0 and a skill<=0 base. `per_claim_recommendation` is empty.

## 3. Biological reference

Closest mechanism: action-conditioned forward models in sensorimotor prediction (efference-copy comparator). The contrastive margin is a **formal-definition import** -- a separation objective in z_world L2 units. The divergence is load-bearing: biology does not buy action-discriminability by degrading reconstruction. Literature present; **no `/lit-pull` owed.**

The dependency assumed and not supplied: a latent whose per-step displacement exceeds the noise floor. `identity_predictor_mse` 1.0e-05 to 1.7e-05 over `world_dim = 16` puts the true per-step L2 displacement at **~0.013-0.016**.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **n/a** | `claim_ids: []` by design |
| Biological reference | **partial** | class supported; load-bearing half needs a head that reads its action |
| Prerequisites | **present** | all five N-preconditions met |
| Implementation | **complete** | the margin term landed (`8f10214`) and demonstrably acts |
| Environment | **too sparse** | z_world moves ~3e-3 RMS/dim per step |
| Measurement | **partial** | two load-bearing gaps -- see 5b and 5c |
| Integration | **coupled and LIVE** | reconstruction effect monotone; *sensitivity* effect is not |
| Scale / capacity | **representation-range insufficient** | the SD-PP-B5 bound, measured |

### Failure-location summary (GOV-FAILLOC-1)

`mechanism: established` / `measures: not_established` / `environment: not_established` / `ree: false`.

**Net: MIXED -- MEASURES + ENVIRONMENT. Not chargeable to REE.**

## 5. The central adjudication

### 5a. FAIL-b is the right route, and it rests on A4

A1 is met at some rung while A3 and A4 are 0/3 there -- by the pre-registered combination rule, **FAIL-b**, not a PASS. **A4 is the sound leg**: it is the one criterion denominated *on the control*, on a bit-identical battery, and it moves cleanly 3 -> 2 -> 0 -> 0 with inflation up to 174x. Everything below narrows what the *other* legs can carry; none of it disturbs A4.

### 5b. The A1 criterion cannot discriminate at the degenerate end

`action_sensitivity_gate.py`'s own docstring names the degenerate case:

> "If a battery contains ONE distinct action, permuting actions is a no-op: **the ratio comes back EXACTLY 1.0.**"

The module guards that on the **battery** side, and the guard held (`n_distinct_actions` 5, `n_rows` 64 everywhere). **There is no corresponding guard on the HEAD side** -- and a head whose predictions have become action-independent produces the same ratio ~1.0 for the same reason.

At M050 the three A1-**passing** ratios are **1.0109 / 1.0026 / 1.0015** on heads with `skill_vs_identity` -431 / -563 / -675, `conv_rel_drop` 0.028 / **-1.637** / 0.398, and `battery_mse_final/init` of 0.97 / **2.64** / 0.60 -- at or worse than initialisation. A1's bar is a bare `ratio > 1.0` with no margin and no head-health condition, so a destroyed head scores as action-sensitive.

**And the per-seed ratio is not monotone.** Seed 42 peaks at **1.0540** (margin 0.10) then falls to 1.0109; seed 123 peaks at **1.0258** (0.05) then falls to 1.0026; only seed 456 rises throughout. Two of three seeds peak mid-ladder and **decay toward 1.0** -- which is the decay an action-independent head produces.

> Corrected at the red-team pass: an earlier draft asserted "A1 and A4 are monotonically anti-correlated" and read the seed counts 0/1/2/3 as a rising trend. The seed-count monotonicity is manufactured by the bar sitting at exactly 1.0 and the top rung collapsing onto it.

**So the honest ladder is A1 0/1/2 against A4 3/2/0 over margins 0.01/0.05/0.10, and the real support for the trade is SEED-COUPLED at the middle two rungs:** the seeds that fire A1 are the seeds whose MSE inflates -- seed 123 at 0.05 (ratio 1.026, inflation 5.90x), seed 42 at 0.10 (ratio 1.054, inflation 4.97x). That coupling is the strongest evidence in the run. **The maximum ratio anywhere is 1.0540.**

### 5c. A3 is a guard its own control fails

A3's bar is `conv_rel_drop >= 0.99`. **ARM_OFF clears it on 1/3 seeds** (0.98466 / 0.98486 / 0.99163). So a margin preserving reconstruction *exactly at OFF quality* would still fail A3 on two seeds: **PASS was unreachable by construction there**, and only a margin that *improved* convergence over OFF could have satisfied it. No precondition checks that the control clears it.

V3-EXQ-1073 reached 0.998 at the same `P0_STEPS` and LR, and the driver itself records that this OFF arm does not reproduce 1073's baseline with the cause unidentified -- so the base is materially less converged than the run whose values justified the bar.

### 5d. The margin term DOES go silent -- the rationale is confirmed, its premise is what fails

`margin_loss_mean` is **0.002-0.008%** of margin at 0.01, **0.037-0.055%** at 0.05, **0.077-0.100%** at 0.10 and **0.68-1.04%** at 0.50. The hinge is satisfied -- silent -- for essentially the whole applied-step budget at every rung.

> Corrected at the red-team pass: an earlier draft asserted "at margin 0.10 and 0.50 the term never goes silent." That is flatly contradicted by every cell.

So `e2_fast.py`'s design rationale ("the margin form goes silent once the head is separated enough", `:247-248`) is **confirmed**. What fails is its **premise**: silence does not undo the deformation already imposed. A margin of 0.05-0.50 in z units forces predictions apart by **3.5-35x the true action-conditioned separation (~0.014 L2)**; the head reaches that separation, goes quiet, and stays wrecked.

Consequently the InfoNCE contrast ("competes with reconstruction throughout training") is **still open**, not settled: the margin form does not compete throughout -- it deforms once and stops.

### 5e. The low rung HELPS the head

Mean `skill_vs_identity` by rung: OFF **-5.48**, M001 **-3.80**, M005 -13.32, M010 -36.88, M050 -556.41. At margin 0.01 the term slightly *improves* reconstruction over the control (A4 3/3 at 0.63-0.92x OFF MSE) and delivers **zero** action-sensitivity (A1 0/3).

So the ladder has a rung that helps the head and gives nothing, and rungs that give apparent sensitivity only by wrecking it.

### 5f. What this means for SD-PP-B5

The entry is `implemented_pending_validation`, `ready: true`, escalated to `/implement-substrate` by the user at the V3-EXQ-1073 gate. **This run is that validation and it fails it** -- no rung shows genuine action-discrimination. Governance owes the status flip off `implemented_pending_validation` in addition to the failure record.

**But the elimination is NARROWER than an earlier draft claimed.** The rungs are 0.01 (0.7x the true separation: inert) and 0.05 (3.5x: already over-shooting). **The interval (0.01, 0.05) -- which brackets the true separation of ~0.014 -- was never sampled**, and it is the one place a hinge could push an action-blind head *toward* the true separation without exceeding reality. "No overlapping operating point" is true of the four rungs tested; "structural rather than tuning" is an inference across that untested gap.

## 6. Interpretable signal

1. The margin form is **eliminated at margin >= 0.05 and inert at 0.01**; the bracketing interval is untested.
2. The anti-sensitivity V3-EXQ-1073 found **is removable** (ratio ~0.81 -> ~1.00) -- a real fact about what the term reaches.
3. `identity_predictor_mse` puts the true per-step displacement at ~0.014 L2 -- a direct quantification of the SD-PP-B5 bound, and the number the ladder should have been centred on.
4. **Two instrument defects** in a gate that is otherwise the best negative instrument in this corpus (5b, 5c).

## 7. Instrument findings

1. **No head-health guard** in `action_sensitivity_gate.py` (5b). Remedy: return `cannot_determine` when `skill_vs_identity` is materially worse than the control's, and require a ratio *margin* rather than a bare `> 1.0`.
2. **A3 is denominated absolutely, not on the control** (5c).
3. **The config default is a broken rung.** `world_interventional_margin` defaults to **0.10** (`config.py:910`) -- A3 0/3, A4 0/3, MSE 5.0-9.6x. `use_world_interventional` defaults to `False` (`:908`), which keeps the blast radius to opt-in consumers.
4. **The canary's scope is narrower than it reads.** It feeds 1073's *published* (ratio, skill) pairs into `readiness_verdict` and checks the returned class -- so it certifies the **classifier's threshold logic**, not the measurement path (battery collection, `battery_pair_ratio`, the inverted env, the head). The measurement-path check is N3, which passes on the ratio *class* while this run's OFF arm sits 30-100x off 1073's skill at 0.985 convergence vs 0.998. Read it as "classifier verified; measurement path reproduces 1073's ratio class but not its skill or convergence."

## 7b. Mechanical pre-routing checks

One fire, **C7, DISMISSED in writing**: `identity_predictor_mse` is bit-identical across arms within each seed. That is a design guarantee -- it is the copy-the-input baseline on the frozen battery, whose rows and targets are bit-identical across arms, and its constancy is precisely what makes `skill_vs_identity` comparable across arms. Same shape as the C7 dismissal in `failure_autopsy_V3-EXQ-1073_2026-09-22`.

**C1 / C2 / C3 returned `inapplicable`** (claim-keyed; `claim_ids: []`). Per the skill's warning, *inapplicable is not "no fire"* -- those checks were structurally blind, so Step 7c carried the whole mechanical load here.

## 8. Routing

**`/implement-substrate`**, with a cheap `/queue-experiment` re-rung first.

**Substrate: `amend` `SD-PP-B5`** -- append this run's failure record, flip the status off `implemented_pending_validation`, severity **`degrading`** (the flag is default-OFF, so only opt-in consumers are exposed), paths `ree_core/predictors/e2_fast.py::world_forward`, `ree_core/utils/config.py`, `experiments/_lib/action_sensitivity_gate.py`.

**GOV-FANOUT-1: three legs.**

| leg | axis | probe | declared null |
|---|---|---|---|
| **H-margin-form** *(narrowed, not eliminated)* | learning-signal | **re-rung at 0.015 / 0.02 / 0.03** -- the untested interval bracketing ~0.014 -- with A3 re-denominated on OFF and an A1 margin bar | A1 and A4 remain unsatisfiable together there too |
| **H-infonce-form** | learning-signal | same battery, repaired bars, SD-056's InfoNCE objective | same coupling, no workable rung |
| **H-encoder-displacement** | representation-update-rate | raise z_world per-step displacement, re-measure at fixed margin | coupling survives at every displacement |

**The re-rung comes first: it is the one thing that could still rescue the shipped form, and it is a `/queue-experiment` item, not `/implement-substrate`.**

> **Two stale pointers were removed at the red-team pass and must not be reinstated.** An earlier draft routed the encoder leg to "SD-018-amend / SD-009 / SD-106", copied forward from SD-PP-B5's own stale `implementation_hint`. Checked against `substrate_queue.json`: **SD-009 has no queue entry at all**; **SD-018** is `amend_implemented_pending_validation` but its own record reads *VALIDATED NEGATIVE for shape (a) by V3-EXQ-978* and its subject is resource-proximity supervision; **SD-106** is `implemented_pending_validation` with V3-EXQ-1023/1023a already run at 0/3 seeds, on generic bottleneck variance. **None targets per-step displacement.** The encoder leg needs a **new** entry and is named here as a gap, not routed to an existing id.

### Judgement call flagged for the user

**Severity `degrading`, not `corrupting`.** A consumer enabling `use_world_interventional` at its shipped default 0.10 gets A1 scoring 2/3 -- reading as "the head now passes the action-sensitivity gate" -- on a head with skill -33 to -48 and MSE inflated 5.0-9.6x. That is evidence that looks valid and is not, which argues `corrupting`. Against it: the flag is default-**OFF**, so no running experiment is affected unless it opts in, and `corrupting` would make Step 2.5c **block** new work touching `action_sensitivity_gate.py` -- a shared instrument. `degrading` is recommended for consistency with the sibling V3-EXQ-1062a call, which turns on the identical default-off argument.

## 9. Red-team record (Step 7c)

**Model: `fable` (claude-fable-5-1)** -- cross-model; this session drafted on Opus 5, reasoning withheld. **Verdict: CONTESTED**, five contested findings, **all accepted**.

Independently re-verified from the cells before acceptance: the three per-seed ratio sequences (non-monotone on 2/3 seeds); `margin_loss_mean` as a fraction of margin at every rung; and the three SD ids against `substrate_queue.json`.

**Convergent validation:** F-75-1 (A3's control fails its own bar) had already been found independently by this session and corrected in a draft the red team never saw -- recorded as convergence rather than as a caught defect.

It did **not** move: the FAIL-b route, `degrading`, the amend to SD-PP-B5, the `/implement-substrate` routing, the A1 degeneracy finding at the 0.50 rung, or A4 as the sound leg.

**Two of the five contested findings were squarely the corpus's measured #1 failure mode -- recommendations that ignore state which already exists (the three stale SD pointers) or infer across an untested interval (the "structural" claim).**

## Step 8 gate

**CONFIRMED by the user, 2026-09-23T07:52:00Z.** Three judgement calls put to the gate, all confirmed as recommended, no change to the drafted routing required:

1. **MECH-055 `epistemic_category`: HOLD `standard`** (`rec-20260923-120f3c68`) -- the ceiling reading is carried by `pending_retest_after_substrate` and the note, keeping the falsifier-(i) / C2 lane open.
2. **Severity `degrading` on BOTH substrate entries** (`rec-20260923-30611285`) -- consistent across the pair on the identical default-OFF argument; no Step 2.5c block on the dACC family or on the shared `action_sensitivity_gate.py`.
3. **Cheap probes FIRST** (`rec-20260923-0ecb56f1`) -- the under-training probe (V3-EXQ-1062a) and the margin re-rung (V3-EXQ-1075) run as `/queue-experiment` diagnostics before any substrate build is commissioned. Both are new EXQ numbers on different mechanisms, falling under the re-derive brake's explicit redesign exemption.

## Step 9b -- frozen hypothesis-space ledger

Integrity audit after the append: **a=0 b=2 c=3 d=0** -- all five flags are **pre-existing on other questions** (`zworld_actor_adequacy_locus`, `mech467_legc_event_denominator_cause`, `sd_e1_var_bar_readout_crush`). **Zero flags on this question**, and its growth appears in the *Advisory -- labelled fan-out growth* section, which is where a legitimate append belongs. Pre-registration provenance: 27 git-witnessed, 0 unverifiable.
The question registered here reads `convergence_class: static` -- nothing is resolved at the elimination bar yet, which is correct: `H-margin-form` is recorded **alive** (narrowed, `met_elimination_bar: false`) rather than eliminated, because the interval bracketing the true separation was never sampled.
