# Failure autopsy -- V3-EXQ-1020 (SD-082 learning-signal probe)

- **Generated:** 2026-09-11T16:39:06Z
- **Status:** confirmed (user-gated, `/governance` cycle `gov-20260911-1612`, Step 1.5 route A -- run inline)
- **Scope:** single
- **Run:** `v3_exq_1020_sd082_learning_signal_probe_20260911T003146Z_v3`
- **Claims:** SD-082
- **Routing:** `queue-experiment` (four-leg fan-out portfolio) -- no substrate build owed
- **Dry-run gate:** checked via `check_dry_run_citations.py`; 1 clean, 0 dry. `dry_run: false`.

---

## 1. Why this run existed

V3-EXQ-822f rejected SD-082's registry leg H1 at adequate power (t(4) = -4.9 against the
0.5 bar) while SD-082's own three predicates were positively observed, and the trained head
flipped LESS than init in 10 of 10 cells. The `weakens` branch was foreclosed by the
dead-ReLU control, so the run read `inconclusive` and nothing moved.
`failure_autopsy_V3-EXQ-822f_2026-09-09` routed exactly one open question to
`/queue-experiment`:

> **Is there a learning signal at all -- and can the instrument see it?**

V3-EXQ-1020 is that probe. It is a NEW EXQ on a NEW axis (`learning-signal`), not a lettered
iteration of 822f's readout-index design; 822g and any same-design letter were explicitly
refused by that autopsy.

## 2. Facts

Two arms x five seeds (822f's own seeds, deliberately), 70 P1 updates per cell. The swept
variable is `crf_cue_centering` alone; `lateral_pfc_train_rule_bias_head` and
`lateral_pfc_rule_readout_consumer` are True in BOTH arms. No criterion contrasts ARM_ON
against ARM_OFF -- the arms exist only so the telemetry spans the same 10 cells as 822f's
headline observation.

**All four preconditions met.** The dense-synthetic-credit positive control learned its own
task (held-out expected-reward gain +0.00223..+0.00327, POSITIVE in 10/10 cells) and
persisted (0.719-0.770); `proposer_post_action` supplied every candidate summary (zero manual
fallbacks in all 10 cells); the flip fraction was resolvable (1707 measured ticks against a
200 floor).

| Criterion | load_bearing | passed | measured | threshold | seeds (OFF / ON, of 5; 3 required) |
|---|---|---|---|---|---|
| C1 gradient present | yes | **PASS** | 0.00593 | 1e-6 | 5 / 5 |
| C2 persistence low | yes | **PASS** | 0.6552 (worst cell) | 0.6030 | **3 / 3** |
| C3 advantage negative on flips | yes | **FAIL** | +0.2858 | 0.0 | 0 / 1 |
| C4 return variance present | no | PASS | 0.1614 | 1e-4 | 5 / 5 |

Independently recomputed from `arm_results[]`: C2's passing cells are seeds **622, 633 and
644 in BOTH arms**; 611 and 655 sit above their midpoints in both. `c2_midpoint` equals
(noise floor + positive-control ceiling)/2 exactly to 1e-12 in all ten cells. C3's per-cell
fresh-select flip-sample counts are 4, 4, 8, 9, 16, 17, 29, 42, 52, 61 -- **only four of ten
cells clear `MIN_FLIP_SAMPLES = 20`**.

## 3. Adjudication

### 3.1 The run achieved its stated purpose

822f could not distinguish "the trained coupling carries no signal" from "the instrument
cannot see it". The in-run positive control closes that: the same head, optimiser and loss
demonstrably learn and accumulate on dense synthetic credit. **A low-persistence reading here
is a measurement of the real signal, not a blind instrument.** This is the run's genuine
contribution and it should not be lost in the inconclusive verdict below.

### 3.2 Neither pre-registered leg is settled

**C2 is a bare majority.** Three of five seeds per arm, and the SAME three in both, so the
ten cells are not ten independent tests of the proposition.

**C3 is unadjudicated, NOT rejected.** Its non-degeneracy guard requires >=20 fresh-select
flip samples per cell and the worst cell has 4. That guard is the driver's own F4 red-team
disposition, raised from `n_flip_samples > 0` precisely because the fresh-only count runs
~10x below the hold-weighted one. **The design anticipated this failure mode and guarded it
correctly; the budget simply did not deliver the samples.** A starved criterion is not a null.

**The self-routed label overstates what C2 licenses -- and the driver says so itself.** F2 of
the driver's own red-team pass records the replay/`rule_state`-mismatch rival as unexcluded
and states verbatim:

> Do NOT read a C2 PASS as establishing H-learning-signal-noisy over this rival.

`H_learning_signal_noisy_supported` is a legitimate output of the interpretation grid (it
routes at `elif c2_pass:`), but its plain-English name asserts more than the design carries.

### 3.3 The `vacuous_pass` flag -- a verdict-level false positive, by a route worth recording

The flag is correct to fire and wrong in what it implies. The indexer's live rule is check
**(3b)**, `evidence/experiments/scripts/build_experiment_indexes.py:639-648`: on a PASS, any
`load_bearing: true` criterion with `passed: false` fires `vacuous_pass`, with
`criteria_aggregation` defaulting to `"all"`. It returns **before** the legacy
`criteria_non_degenerate` path. C3 fires it simply by being a load-bearing criterion that did
not pass.

It is a false positive at the verdict level because the label never read C3. But the manifest
never declares `criteria_aggregation`, so the indexer cannot know that -- while the driver's
own `combination_rule` asserts in prose that C2 and C3 are "reported INDEPENDENTLY ... NOT
AND-ed". **The fix is one declaration** (see 5.2); `vacuous_pass` sits in
`BLOCKING_ADJUDICATIONS`, so left alone it will block every successor on this design from
minting a substrate entry or clearing a gate.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | SD-082's own predicates are not re-tested here; the probe is about the training signal that feeds them |
| Biological reference | partial | mechanism class sound; **training signal is a formal import, divergence load-bearing** |
| Prerequisites | present | SD-078 rule pool live and differentiated; head trainable and trained |
| Implementation | complete | every tensor moved; 70 updates; no non-finite gradients |
| Environment | adequate | CausalGridWorldV2 supplied return variance 0.16-0.34 against a 1e-4 floor |
| **Measurement** | **under-instrumented** | C3 starved (4 of 20 samples in the worst cell); C2 under-determined against an unexcluded rival |
| Integration | partially coupled | the head trains, but its output has no selection authority in this configuration (5.1) |
| Scale | likely insufficient | T=70 against a measured Adam noise-floor crossing at T~300 |

**Failure-location (GOV-FAILLOC-1): MEASURES.** Implementation reads `complete` and
Environment reads `adequate`, but Measurement does not, so this is not MECHANISM and
emphatically not REE FAILED.

### Biological-reference triage

The closest reference is dorsolateral-PFC rule-coding biasing premotor/striatal action
selection -- a mechanism class with a solid existence proof, and `targeted_review_sd_082`
already exists, so **no `/lit-pull` is owed**.

The divergence is in the *training signal*, and it is load-bearing. Episode-level REINFORCE
over a replay buffer scores every sampled tuple at ONE shared end-of-episode
`lpfc.rule_state`. Brains bind credit to the state active **at the time of the action**
(eligibility traces), never to a single current state. So the biology independently favours
the F2 replay-mismatch rival over both pre-registered hypotheses -- and names the repair:
**per-sample `rule_state` at update time is the eligibility-trace analogue.** That is why it
is the first leg of the portfolio.

## 5. Learning extracted

### 5.1 A configuration fact that is NOT an SD-082 finding

`per_episode_returns` are **bit-identical between ARM_ON and ARM_OFF across all five seeds x
70 episodes**. An earlier draft of this autopsy read that as fresh behavioural-silence
evidence for SD-082. **That reading was wrong and the Step 7c red team caught it.** Three
independent reasons, each verified:

1. **Wrong counterfactual.** The swept variable is `crf_cue_centering` alone; both arms hold
   the head flags fixed and there is no head-ablated arm. The null is about CRF centering,
   not about the head.
2. **A behavioural difference was impossible by construction.**
   `use_modulatory_selection_authority` is `False` (default, `ree_core/utils/config.py:1273`)
   and this driver never sets it; `bias_scale = 0.1` is tanh-bounded
   (`lateral_pfc_analog.py:154`, `:479-481`). `config.py:1262-1263` states the root cause
   verbatim: *"fixed small bias magnitudes (~0.05-0.1) added to primary scores whose
   raw_score_range is much larger never change the argmin."*
3. **The supporting numbers were the pseudo-replicated ones.** The de-replicated figures are
   `n_fresh_flip_ticks` **5 -> 6** for seed 611, not the hold-weighted `n_flip_ticks` 49 -> 57
   -- the very statistic the driver's own F4 disposition demotes.

What it **does** establish, and it matters for successor design: **any behavioural probe on
this path is inert until selection authority is enabled.** That is why the Step 8 gate added
a constitution-axis leg to the portfolio.

### 5.2 Driver-declaration fix (forward-only)

The successor driver should declare `interpretation.criteria_aggregation = "any"`, making the
C2/C3 independence its `combination_rule` already asserts machine-readable and stopping this
design from re-tripping a BLOCKING `vacuous_pass`. **Do not retro-edit the landed 1020 driver**
-- its run is complete.

### 5.3 Lineage

Eight runs (V3-EXQ-822, 822a-822f, 1020) from 2026-07-26 to 2026-09-11 have never settled
SD-082. The **granularity-debt trigger does NOT fire**: `granularity_debt_cluster.py SD-082`
returns 5 tagging targets with alignment distribution `unclear=5` and **zero `weakened``, and
its own verdict is measurement/implementation debt rather than granularity debt. The
**re-derive brake** stands at 3 (822b/822c/822d), released by
`failure_autopsy_V3-EXQ-822f_2026-09-09` on its own explicit record; this autopsy's
`inconclusive`/`standard` reading adds no fourth hit. **A further lettered iteration of the
same design is refused.**

## 6. Routing -- four-leg fan-out (GOV-FANOUT-1)

All four legs were selected by the user at the Step 8 gate.

| Leg | Axis | Sketch |
|---|---|---|
| `H-replay-rule-state-mismatch` | process | Store each sample's OWN `rule_state` in the replay tuple (index 4, currently `None`) and re-score at update time; contrast persistence against the faithful-to-822f path. `rule_state_norm_at_update[]` telemetry already emitted. Highest value on both the F2 reading and the eligibility-trace biology. |
| `H-learning-signal-sign` | measurement | Raise P1 budget and/or flip yield until EVERY cell clears 20 fresh-select flip samples, so C3 is scoreable rather than degenerate. |
| `H-selection-authority-bounded` | constitution | Set `use_modulatory_selection_authority=True` and/or add a head-ablated arm, so a behavioural reading is possible at all. |
| `H-learning-signal-noisy` | process | Extend P1 past T~300 updates, where the measured Adam pure-noise persistence floor first crosses 0.25; this run does 70. |

**Substrate queue: `amend`, not a build.** Append the 1020 record to SD-082's
`failure_record` and extend `validation_experiment` to name V3-EXQ-1020 -- which also
discharges the substance of open flag **GFLAG-0260**. `severity` and `substrate_paths` are
left unchanged: the entry reads `severity: corrupting` with `substrate_paths: []` because
governance deliberately emptied the paths on 2026-09-09 to stop spurious Step 2.5c gating of
the whole programme, and nothing here changes that.

## 7. Step 7b / 7c

- **Step 7b mechanical pre-routing checks: 0 fires** (C5 inapplicable -- no sibling `.md` at
  draft time).
- **Step 7c adversarial red team: CONTESTED**, and both defects were accepted after
  independent verification of every citation. Run on **claude-opus-5, the SAME model as the
  drafter** -- `claude-fable-5-1` was unavailable this session ("You've hit your monthly spend
  limit"). Per the skill this is a valid pass but **not** the preferred cross-model one, and
  the verdict should be read accordingly.
  - Primary: the bit-identity inference (5.1) -- rewritten.
  - Secondary: the `vacuous_pass` mechanism was misattributed to `criteria_non_degenerate`
    (3.3) -- corrected, and it concealed the cheap fix now carried as 5.2.
  - Hygiene accepted: `outcome: PASS` rests on readiness + C1 only (`driver:1448`), not C1+C2
    -- C2 selects the LABEL (`driver:1427`); `C2_bracket_valid` could not have come out false
    given the readiness precondition, so citing it as non-degeneracy support is weak; the
    manifest's top-level `config` block records `crf_cue_centering: true` only, misrepresenting
    ARM_OFF (per-cell `centering` is recorded correctly, so no information is lost).
