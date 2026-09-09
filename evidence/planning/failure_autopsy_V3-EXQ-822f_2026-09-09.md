# Failure autopsy -- V3-EXQ-822f (SD-082 candidate-discriminating readout, init-head control)

- **Status:** `confirmed` (user gate 2026-09-09T00:55:13Z) -- drafted interactively by session `fa-20260909-batch`
  (DLAPTOP main checkout, batch with V3-EXQ-1015 and V3-EXQ-1014), red-teamed cross-model at
  Step 7c (**CONTESTED**, five findings, all applied -- Section 9), Step 8 gate held (Section 9).
- **Generated (UTC):** 2026-09-09T00:26:26Z
- **Scope:** single
- **Run:** `v3_exq_822f_sd082_candidate_discriminating_init_head_control_20260908T231145Z_v3`
- **Queue id:** V3-EXQ-822f (`supersedes` V3-EXQ-822e) -- `experiment_purpose: evidence`,
  campaign W5-S2b item 2, chip `chip-20260905-exq822f-init-head-control`, the DESIGN-CHANGED
  successor the confirmed 822e autopsy ratified ("No replay; 822f = init-head control + new seeds").
- **Claims:** SD-078, SD-082 (both `candidate_substrate_landed`, `epistemic_category: standard`,
  `pending_retest_after_substrate: false`).
- **Outcome:** FAIL (family convention: FAIL covers every inconclusive path), `evidence_direction:
  inconclusive` on both claims, self-route `discrimination_within_init_head_spread_inconclusive`,
  `readiness_failure_class: none` -- **readiness 19/19 met, the first time in this lineage.**
- **Ran:** 10,700 s (2h58m) on `ree-worker-3`, `linux-x86_64-py3.10-torch2.12.0+cpu`, substrate
  hash `0bb2203187d9...` stable across the run.
- **Dry-run gate:** clean (0 dry / 2 real in family: 822e, 822f).
- **Recording:** flat JSON complete (`per_seed_rows` with trained and init indices AND flips per
  cell, `head_diag_by_phase`, per-tensor param distances, `n_p1_optimizer_updates`; `config`,
  `seeds` 611-655, `elapsed_seconds`, `recording_schema` rec/v1). Run-pack `manifest.json` thin
  (`validate_recording.py` flags it; `source_repo.commit` empty). No recording gap for this
  adjudication.

**Headline.** With the control the 822e autopsy demanded finally in place, registry leg H1 --
*the TRAINED readout adds candidate-discrimination beyond its initialisation* -- is **rejected at
adequate power**: the paired trained-minus-init index sits 4.9 standard errors below the
pre-registered 0.5, on a criterion the design could reach. That is a null on H1, not on SD-082's
own text: the claim's three predicates (common-mode-invariant, gradient-trainable, maps
rule_state to a per-candidate bias) were each positively observed. Nor is it "training did
nothing": the trained head flips the argmax **less** than the init head in 10 of 10 cells --
training shaped the readout toward a less rule-sensitive function at unchanged index. The
pre-registered rule labels all this `inconclusive`, and on this run its `weakens` branch was
unreachable by construction. Sixth letter on this claim pair; the next probe changes axis
(learning-signal content and sign), not power.

---

## 1. Facts (no interpretation)

### 1a. Design (what 822f changed, per the 822e autopsy's five ratified requirements)

(a) Load-bearing criterion is **C1'**: at every live P2 tick the raw pre-tanh discrimination index
is read through the TRAINED head and through the INIT head (deep-copied before the first
optimizer step) on the SAME summaries and SAME rule_state; `D = trained - init`, paired per tick,
per-cell median; per-arm requirement `max(0.5, 1 sd of D across seeds)` plus D > 0 on >= 4/5
seeds. (b) New seeds 611/622/633/644/655. (c) Liveness gate = summed Frobenius `||W_p1 - W_init||`
over every head tensor, ARM_ON only, floor 1e-3. (d) C4 (SD-078 ON-minus-OFF contrast) kept,
three-valued through a detectability clause (|t| >= 2.132). (e) 822e's offline re-score carried
as provenance only. Both arms carry SD-082's `candidate_summary_source="proposer_post_action"`;
the arm axis is `crf_cue_centering` (SD-078's knob). P1: one Adam step (lr 5e-4) per episode
on an episode-summed harm return assigned to every selection in that episode; 70 P1 episodes.
Red-team fixes F1-F3, N4-N7 recorded in the docstring; the `weakens` route additionally
requires dead-ReLU masks comparable on every ON cell (< 0.50) AND the trained head failing
absolute C1.

### 1b. Criteria, as scored

| Criterion | Claim | Load-bearing | Result | Number |
|---|---|---|---|---|
| C1' trained-minus-init index, ARM_ON, mean D >= 0.5 AND D>0 on >= 4/5 | SD-082 | yes | **FAIL** | mean D 0.0627, sd 0.2005, se 0.0897, D>0 on 2/5; CI95 [-0.186, 0.312]; t(4) vs 0.5 = -4.88 |
| weakens route (D <= -0.5 AND controls) | SD-082 | -- | **unreachable** | `dead_relu_masks_comparable_all_on_cells` false (4/5 ON cells >= 0.50); `trained_head_fails_absolute_c1` false |
| C1 raw index >= 1.0 on >= 3/5 ON seeds | -- | reported | pass | 4/5 (init head: 4/5, same failing seed 622) |
| C1b same floor on ARM_OFF | -- | reported | pass | 3/5 |
| C2 pooled argmax-flip fraction >= 0.02 | -- | reported | pass | 260/1701 = 0.153 (init head 493/1701 = 0.290) |
| C4 SD-078 contrast >= 0.25 on >= 4/5 AND |t| >= 2.132 | SD-078 | yes (dir_078 only) | **inconclusive** | 2/5 clear; mean 0.0694, sd 0.898, t 0.173; detectable 0.86; ~59 seeds for the margin |
| C3 legacy magnitude floor both arms | -- | diagnostic | cannot discriminate | ON 0.00120 / OFF 0.00155 |

### 1c. The per-cell numbers that carry the read

| arm | seed | trained index | init index | D (median) | P1 updates | last-layer ||dW|| | dead ReLU (P2) | rule_state_diff | flips trained / init |
|---|---|---|---|---|---|---|---|---|---|
| ON | 611 | 1.865 | 1.374 | **+0.323** | 70 | 0.0448 | 0.505 | 0.618 | 23 / 26 |
| ON | 622 | 0.535 | 0.625 | **-0.088** | 69 | 0.0281 | 0.438 | 0.685 | 39 / 49 |
| ON | 633 | 2.278 | 1.875 | **-0.001** | 70 | 0.0351 | 0.627 | 0.767 | 28 / 38 |
| ON | 644 | 2.018 | 1.711 | **+0.221** | 70 | 0.0233 | 0.657 | 0.634 | 47 / 50 |
| ON | 655 | 1.455 | 1.923 | **-0.141** | 70 | 0.0406 | 0.541 | 0.718 | 11 / 31 |
| OFF | 611 | 3.059 | 2.033 | +1.020 | 70 | 0.0405 | 0.556 | 0.0 | 16 / 17 |
| OFF | 622 | 0.358 | 0.543 | -0.200 | 69 | 0.0360 | 0.434 | 0.0 | 15 / 61 |
| OFF | 633 | 1.688 | **4.698** | -2.946 | 70 | 0.0322 | 0.650 | 0.0 | 56 / 122 |
| OFF | 644 | 0.876 | 0.580 | +0.234 | 70 | 0.0296 | 0.689 | 0.0 | 23 / 74 |
| OFF | 655 | 1.823 | 0.918 | +0.907 | 70 | 0.0411 | 0.550 | 0.0 | 2 / 25 |

Trained flips < init flips in **10/10 cells** (sign test p = 2^-10 = 0.001); pooled 260 vs 493.
Readiness (19/19): cone 0.933; ON pool differentiated 5/5, OFF pinned 5/5; prop samples >= 122;
raw replica error 7.5e-9; uniform control 0.000; liveness worst ON total param distance 0.188;
`dv_headroom_trained_minus_init_index` 0.625 vs 0.5 (a post-hoc bound; the in-loop positive
control reaches 5.28 and the index ceiling is K = 32, so D = +0.5 was reachable on every cell).
iid reference index (K=32): median 5.15, p5/p95 4.12/6.57. Last-layer weights moved 16-32% of
their init norm (0.142). Adam displacement at lr 5e-4 over 70 steps on a 32-weight tensor: zero
gradient 0; random-sign gradient ~0.025 [0.018, 0.032]; SNR ~1 ~0.041; consistent sign 0.198.

### 1d. The 822e provenance re-score

Carried as required (`provenance_822e_offline_rescore`): instrument defect only; not used.

---

## 2. Claim layer

| | SD-078 | SD-082 |
|---|---|---|
| title (short) | common-mode-invariant (centered) CandidateRuleField context key | `pfc.lateral_pfc.rule_selection_action_consumer`: a common-mode-invariant, **gradient-trainable read-out** mapping SD-078's rule_state to the SD-033a per-candidate action bias |
| status / category | candidate_substrate_landed / standard | candidate_substrate_landed / standard |
| pending_retest | false | false |
| role here | co-tag (arm axis); C4 only | subject; C1' only |

**Did the run let SD-082 express itself?** Its three predicates were each positively observed:
centering engaged (invariant); every tensor moved over 69-70 updates (trainable); rule_state
changes the per-candidate bias and flips the argmax on 15% of ticks (maps). What was rejected is
registry leg **H1** -- a stronger proposition the claim's text does not assert, as the driver's own
F3 comment says in terms. H1 is rejected at adequate power (t(4) = -4.9 against 0.5 on a reachable
criterion), yet the head is demonstrably shaped by training (flips halved 10/10; OFF-arm index
moved by up to -2.95). **Not `weakens`**: (a) the mirrored clause (D <= -0.5, training REMOVES
discrimination) is not H1's negation; (b) on this run that branch was **unreachable by
construction** -- both `weakens_route_controls` read false because 4/5 ON cells exceed the 0.50
dead-ReLU floor and absolute C1 passed -- so the rule was two-valued whatever D was; (c) the
learning signal's content is unmeasured. `inconclusive` for SD-082, content stated. **SD-078:** C4
inconclusive by its own detectability clause; co-tag, note-only. `claim_ids` correct.

---

## 3. Biological-reference triage

Corticostriatal rule-to-action readout (lit present). The topology is not implicated. The
formal-import half is the **learning rule**: an episode-summed harm return applied to every
selection in the episode, one Adam step per episode. The last layer's measured movement
(0.023-0.045) matches a direction-inconsistent gradient walk (random-sign ~0.025; SNR ~1 ~0.041),
12-23% of the consistent-sign budget; a zero gradient would not move Adam at all. Biological
readouts of this kind are shaped by dense credit with a persistent direction. Load-bearing for the
next probe, not for the claim. No `/lit-pull` owed.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** (both) | SD-082: H1 rejected at adequate power; claim predicates positively observed; head shaped by training; signal content unmeasured. SD-078: C4 inconclusive by construction. |
| Biological reference | **clear** | Learning-rule divergence noted. |
| Prerequisites | **present** | SD-078 pool differentiates 5/5 ON; SD-082 amend engaged; replica 7.5e-9. |
| Implementation | **partial** | Index init-like on ARM_ON (D ~ 0; init head clears C1 on the same 4/5; OFF/633 init index 4.70 vs iid 5.15) -- but the trained head is a different function: flips halved 10/10 (p 0.001), OFF-arm index moved up to -2.95, last layer moved 16-32% of its norm. Dead ReLU 0.44-0.66 on ON (H4). |
| Environment | **adequate** | Unchanged. |
| Measurement | **partial** | Inputs sound. Emissions: the weakens branch was foreclosed by the dead-ReLU control (4/5 ON cells >= 0.50); no branch for "no trained increment at adequate power"; the supports rule has ~50% power at a true 0.5 (99% at 0.7), so "a consistent 0.5 would have registered" is not a claim the design supports -- what is well-powered is REJECTING 0.5. |
| Integration | **coupled** | Flips occur; E2 -> summaries -> readout -> argmax chain live. |
| Scale | adequate for rejecting H1 at 0.5; supports rule under-powered at exactly 0.5; C4 by design inconclusive at n=5 | |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Verdict |
|---|---|
| MECHANISM FAILED | **partial** -- H1 rejected; head shaped toward less rule-sensitivity; signal content unmeasured |
| MEASURES FAILED | **established** -- weakens branch foreclosed by construction; no branch for the outcome found |
| ENVIRONMENT FAILED | not established |
| REE FAILED | **false** |

**Net: MIXED (MECHANISM partial, MEASURES established), not chargeable to REE.**

### Recommended `epistemic_category`

`standard` for both -- confirms the stored value.

---

## 5. Learning extracted

1. **The lineage's discrimination INDEX is init-like, but the readout is not the init head.** The
   init head clears absolute C1 on the same 4/5 seeds (same failing seed 622); OFF/633 init index
   4.70 vs iid reference 5.15 -- the raw index reads summary geometry through a random projection.
   Yet training reduced argmax flips in 10/10 cells (260 vs 493; p = 0.001) and moved the OFF-arm
   index by up to -2.95. "Within the init spread" describes the index, not the function.
2. **The head moved as an optimiser with a direction-INCONSISTENT gradient would**: 0.023-0.045
   over 69-70 Adam steps at lr 5e-4 matches a random-sign walk (~0.025) to SNR ~1 (~0.041), 12-23%
   of the consistent-sign budget (0.198); a zero gradient moves Adam not at all. The update count
   is not evidence the return varied (EMA baseline starts at 0; stale buffer entries carry
   advantage under a constant return). Gradient content and direction persistence are unrecorded.
3. **The three-valued rule was two-valued on this run**: the weakens branch's dead-ReLU control
   (< 0.50 on every ON cell) failed on 4/5 cells and absolute C1 passed, so `weakens` could not fire
   for any D. A branch a control can foreclose must report the foreclosure as an outcome; a
   one-sided requirement also needs a branch for "no trained increment at adequate power".
4. **State power against the rule that fires**: the supports rule (mean D >= 0.5 AND 4/5 positive)
   has ~50% power at a true 0.5 and ~99% at 0.7; rejecting D >= 0.5 on the observed sd is what the
   design does well (t(4) = -4.9).
5. **Six letters, five instrument defects, one clean rejection of H1** with the claim's own
   predicates positively observed. The brake (SD-082 3, SD-078 5) does not fire because none is a
   ceiling reading -- correct -- but the next probe must change axis (signal content and sign),
   not power: a direction-inconsistent walk grows as sqrt(steps).
6. **A resolved defect left `severity: corrupting`** (a deliberate 2026-09-05 choice) keeps warning
   unrelated experiments through Step 2.5c (V3-EXQ-1015 recorded SD-082 as an open corrupting
   overlap and disposed of it as NOT REACHABLE). Worth revisiting with that information.
7. **Recording:** complete for this adjudication; gaps for the next run: per-update gradient norm,
   step-direction persistence, per-episode return variance and flip-rate trajectory, advantage sign
   on flip vs non-flip selections. Driver docstring L74-77 still describes a superseded C1'
   headroom statistic -- stale, do not re-import.

### Granularity-debt recurrence trigger: DOES NOT FIRE

`granularity_debt_cluster.py`: SD-082 4 tagging targets (unclear=4), SD-078 6 (unclear=6); no
`weakened`. Instrument debt, not a coarse claim.

### Re-derive brake (R1-R3 recount, 2026-09-09)

Prior counted hits: **SD-082 3**, **SD-078 5** -- identical to the 822e autopsy's recount,
independently reproduced by the red team. This target: per-claim `standard`, direction
`inconclusive` -> does not count; the brake does **not** fire. Release basis: not a ceiling
reading. **Refused:** V3-EXQ-822g or any same-design letter -- not on power grounds but because
the missing axis is the SIGNAL. **Licensed:** a NEW EXQ on the learning-signal axis; separate
probes for H2/H3/H4 (H4 first among them).

---

## 6. Repair pathway and routing (confirmed at the gate)

**Node classification:** `complex (probe-gated) / puzzle (known rules)` -- the missing facts are
the P1 gradient's direction persistence and the sign of the advantage on rule-driven flips; both
obtainable by named measurements in the existing loop.

**Routing: `queue-experiment`**, NEW EXQ number, `experiment_purpose: diagnostic`,
`claim_ids: [SD-082]`:

- **Learning-signal probe (first):** 3-5 seeds; record per-P1-update gradient norm on
  `rule_bias_head`, per-tensor step-direction persistence (||sum of steps|| / sum of ||steps||),
  per-episode return variance, per-episode trained-head flip rate (trajectory), and the sign of the
  advantage on flip vs non-flip selections; positive control = the same head on a dense synthetic
  credit must move D past 0.5 with persistence near 1. Adjudicates **H-learning-signal-noisy**
  (provenance: driver note N6, whose shipped `training_signal_absent` class detects only zero
  updates) and **H-learning-signal-sign** (REINFORCE learns to reduce rule-driven flips) under one
  measurement.

**Fan-out (GOV-FANOUT-1)** -- H-init-structure (consistent on the index), the two learning-signal
legs, **H4-dead-head-capacity (priority raised: the same dead fractions foreclosed the weakens
branch)**, H3, H2. Probe sketches in the JSON. Do not queue H2/H3/H4 off this artifact; governance
chips them.

**Governance:** note-only dispositions (`-> stamp this artifact`); amend the SD-082 substrate entry
(append the 822f record; mark the open 822d item **superseded** with the half-answered note --
discriminating-vs-uniform answered, ON > OFF inconclusive by construction and not carried forward;
advance `validation_experiment`; **revisit `severity: corrupting`** with the 1015 gate hit as new
information); Step 9b as in Section 7.

**Explicitly not recommended:** 822g / same-design power bump; `weakens` on SD-082 (its own
predicates observed; the branch was foreclosed by construction); `supports` off absolute C1/C2;
`/implement-substrate`; `/lit-pull`; `/claim-synthesis`; demotion.

### Per-claim recommendation

Both note-only; both `change` strings end on `-> stamp this artifact`. Exact `evidence_quality_note`
in the JSON. `recommended_diagnostic_evidence_adjudicated` NOT set (purpose `evidence`).

---

## 7. Hypothesis-space ledger (Step 9b, applied after the gate)

Question `sd082_candidate_discriminating_readout_locus` (`growth_restriction` empty). **Mode B:**
H1 -> `alive` (rejected at adequate power on the index; not eliminated: weakens branch foreclosed,
signal rival open); H-init-structure -> `alive` (consistent on the index; not confirmed as the
account of the readout -- flips halved 10/10). **Mode A (one labelled fan-out growth event, +2):**
pre-register `H-learning-signal-noisy` and `H-learning-signal-sign` (axis `learning-signal`, in
`axis_families.map`), adjudicating run = the probe once queued; `initial_frozen_count` 5 -> 7;
`initial_frozen_count_at_registration` stays 5; `pre_registration_source` = this artifact.

## 8. Mechanical checks

- Dry-run gate: clean. `validate_recording.py`: pack thin, flat complete. Lint: silent.
- Step 7b: **0 fires** on the draft and the revised pair (C6/C7 inapplicable to `per_seed_rows`).
- Step 7c: Section 9.

## 9. Step 7c red team and Step 8 gate

**Step 7c -- cross-model, read-only. Model Fable 5.1 (`claude-fable-5-1`). Verdict: CONTESTED.**
Findings file `redteam_822f.md` (session scratchpad; one scratch script `adam_walk_sim_822f.py`).
It reproduced the C1' arithmetic, the init counts, the headroom, the liveness gate, the reward
construction, C4, the brake counts and the severity state (confirmations block). Five findings
moved assertions; all applied:

| # | Finding | Disposition |
|---|---|---|
| F1 | "Adam minimum displacement = no gradient content" is the wrong quantity; zero gradient moves Adam 0; measured matches a direction-inconsistent gradient | **APPLIED** -- arithmetic withdrawn; leg renamed `noisy`; basis rewritten |
| F2 | the readout does not "stay at init": trained flips < init in 10/10 cells (p 0.001); OFF-arm index moved up to -2.95; new rival (signal sign) | **APPLIED** -- implementation row, learning 1, H-init-structure basis rewritten; `H-learning-signal-sign` added |
| F3 | the weakens branch was unreachable by construction (dead-ReLU control false on 4/5 ON cells) | **APPLIED** -- measurement row `partial`, failure-location MEASURES `established`; H4 priority raised |
| F4 | the 822d "superseded" note over-claims: ON > OFF half unanswered | **APPLIED** -- note narrowed |
| F5 | "a consistent 0.5 would have registered" is false (supports rule 50% power at 0.5); rejection of >= 0.5 holds | **APPLIED** -- power claims restated; 822g refusal re-grounded on signal, not length |

Hygiene H1-H9 applied (H1 vs claim text distinguished; N6 provenance; power wording; severity
revisit framed as revisiting a deliberate choice; "warning" not "blocking"; stale driver docstring
noted; "one Adam step's worth" removed; probe recordings added).

**Step 8 gate -- user decision, binding (2026-09-09T00:55:13Z):**

> Accept: inconclusive/standard note-only; learning-signal probe; 822g refused (Recommended).

The routing above is confirmed as drafted; the hypothesis-space ledger moves in Section 7 are applied in this session.
