**Status: RESOLVED 2026-09-18T22:58Z -- the user chose OPTION B (real AskUserQuestion, via decision chip `chip-20260918-exq1039a-readiness-gate-amendment`). Applied and queued; see section 7. Nothing in this file was written to claims.yaml, substrate_queue.json or hypothesis_space_registry.v1.json, then or now.**

# V3-EXQ-1039a -- absorption-gated re-run: red-team CONTESTED, one gate decision owed

- **Session:** `metaworker-science-20260918-exq1039a-absorption-rerun` (headless, ree-cloud-5)
- **Campaign:** `science-20260918-exq1039a-absorption-rerun`
- **Chip:** `chip-20260916-exq1039a-absorption-precondition-queue`
- **Written:** 2026-09-18
- **Authority for the design:** CONFIRMED `failure_autopsy_V3-EXQ-1039_2026-09-16.md` (+ `.json`), user Step 8 gate 2026-09-16T13:06:22Z, applied by governance-20260916 (REE_assembly `db6d20ebee`).

## 1. What was done

The V3-EXQ-1039a driver is **written, validator-clean and smoke-passing**, implementing the
autopsy's section 14 items 1-5. It is **NOT QUEUED**: the mandatory Step 4.5 adversarial
red-team returned **CONTESTED**, and two of its five findings can only be resolved by
amending a gate set that a user gate ratified. Under the campaign's consent rule that is a
STOP, not a judgement call for a headless session.

Driver (not on `origin/main`; see section 5 for where it lives):
`ree-v3/experiments/v3_exq_1039a_mech428_inv086_waypoint_field_consumer_drive_signal_absorption_gated.py`

### Pre-queue gates, all cleared

| Gate | Result |
|---|---|
| STOP-CHECK (queue / manifest / ID) | `V3-EXQ-1039a` free in all three namespaces; queue depth 0 |
| 2.4 GOV-REUSE-1 | Not recoverable. V3-EXQ-1039's manifest (`substrate_hash 5a74d527...`) carries none of `absorption`, `conversion`, `adv_surviving_frac`, `distinct_first_action_classes`, `candidate_summary_degenerate_computed`; the telemetry build post-dates it and edits `_lib/**`, which is inside `substrate_hash`, so no prior run is substrate-compatible |
| 2.5b re-derive brake | INV-086 = 0 counted autopsies, MECH-428 = 1 -- below threshold 2, does not fire |
| **2.5c substrate-path overlap** | **CLEARED.** SD-082's footprint is empty on `origin/master` (`261660bfa3`), confirmed an ancestor of HEAD. The other open `corrupting` entries were probed empirically, not argued by shape -- see section 2 |
| 2.6 ethics | all-`false`, `decision: allow` |
| `validate_experiments.py --strict` | OK, 0 non-conforming; 1 advisory anchor-reachability warning, left unexempted as V3-EXQ-1039/1030 did for a first-of-lineage statistic |
| `--dry-run` smoke | rc=0 end-to-end, correct self-route `substrate_not_ready_requeue` at the dry budget, manifest relocated, z_goal wired (`no writer defect`) |

## 2. Step 2.5c: the corrupting entries were probed, not argued

The orchestrator's brief required an honest reachability assessment of
`contextmemory-write-path-addressing-degeneracy` (severity `corrupting`, still open by user
ratification) for this driver's DV. Measured rather than reasoned:

- `sd016_writepath_mode` is **absent from the config object** this recipe builds, so
  `ree_core/agent.py:5492`'s `getattr(..., "off")` takes the OFF branch.
- A 12-tick probe on the exact agent this driver constructs recorded
  **`ContextMemory.write()` CALLS: 0**.
- `contextmemory_write_addressing_loss_weight = 0.0`, `sd016_diversification_weight = 0.0`.
- 1039a's DVs (per-arm returns, advantage survival, E3 modulatory readouts, first-action
  diversity, bias-head norm delta, eval waypoint counts) read the ContextMemory bank nowhere.

**Verdict: NOT REACHABLE.** The defect is in `ContextMemory.write()`'s addressing; the
function is never called.

The other open `corrupting` entries are likewise inert in this recipe, probed the same way:
`use_blocked_agency = False` (`agent.blocked_agency is None`);
`use_selection_entropy_floor = False` (module `None`); `agent.tonic_vigor is None` (MECH-320).

`degrading` overlaps to acknowledge in the queue note when it is eventually written:
`sd-allon-training-signal-absorption-telemetry`, `SD-ZWORLD-SENSE-PATH-PARITY`, `SD-018`,
`SD-106`, `SD-091`, `SD-MECH303-THRESHOLD-SOURCING`, `SD-MECH267-CEM-SELECTION-FIX`.

## 3. Two defects found by this session's own smoke, both fixed

- **D1.** `capture_head_diagnostics=True` is **silently swallowed** by `REEConfig.from_dims`
  -- it neither raises nor sets an attribute. The correct key is
  `lateral_pfc_capture_head_diagnostics`; `ree_core/agent.py:1006` reads that and passes it
  into `LateralPFCConfig`. Until fixed, `absorption.hidden_dead_relu_frac_available` came back
  `False` with `n=0`, i.e. autopsy item (d) was not recorded at all. Fixed, plus a
  construction-time assert so it cannot regress silently. (Instance of memory
  `reference-reeconfig-from-dims-silent-kwargs`.)
- **D2.** Precondition A1's separation denominator used only the sparse arm's SD, which the
  dry run measured at exactly 0.0, so it divided by `RETURN_SD_EPS` and reported a
  separation of `3000000.0` -- an artifact of the epsilon, not a measurement. Now
  `max(sparse_sd, shaped_sd, EPS)` with a declared cap; the same cell now reads `1.38873`.

## 4. Step 4.5 red-team: CONTESTED (fable 5.1, cross-model, one pass)

Every finding was verified against the source before disposition.

### FIXED in this session (no ratified criterion changed)

- **F5 -- the per-tick tap counted env steps, not fresh E3 selections.**
  `_distinct_first_action_classes` is called on every P1 env step
  (`allon_training.py:707-710`, not gated on `ticks["e3_tick"]`), while
  `agent.generate_trajectories` returns the **same cached `_committed_candidates` object**
  between E3 ticks (`ree_core/agent.py:6315-6320`). One selection was therefore re-counted
  ~10x and the RATIFIED "majority of ticks" was weighted by commitment-hold duration.
  Confirmed in the dry run: `hist.n_ticks == p1_n_ticks == 30` over 30 env steps.
  **Fixed** by identity-deduplicating the cached object, with `n_held_ticks` recorded so the
  denominator stays auditable. This makes the instrument match the ratified wording ("per E3
  tick"); it is a correction, not a redesign.
- **F1 (recording half) / F4 -- recorded, not gated.** Now recorded per fresh tick:
  `lpfc_bias_abs_mean` against `lateral_pfc.config.bias_scale`, `lpfc_bias_saturated_frac`,
  and `modulatory_shortlist_size`.

### What the post-fix smoke then MEASURED (dry budget; the strongest item here)

Re-running the smoke after the F5 fix turned two of the red-team's predictions into
measurements. Read with the dry budget in mind (1 seed, 2/2/3/2 episodes, 10 steps, so the
heads are close to initialisation); these are not full-scale results, but they are not
speculation either.

| Measured, all three treatment arms | Value |
|---|---|
| `p1_n_ticks` (env steps) vs `first_action_class_hist_p1.n_ticks` (fresh E3 selections) | 30 vs **6**, with `n_held_ticks = 24` |
| `lpfc_bias_scale` | 0.1 |
| `lpfc_bias_abs_mean_mean` | **0.10000000894069672** |
| `lpfc_bias_saturated_frac` | **1.000** |
| `modulatory_shortlist_size` (n/mean/min/max) | 6 / **0.0** / 0.0 / 0.0 |
| `first_action_diversity_majority_ticks` (B1) | 1.0, MET |

- **F5 was a 5x pseudo-replication.** The ratified "majority of ticks" was being evaluated
  over 30 hold-weighted env steps where only 6 distinct E3 selections occurred. Now
  corrected; `6 + 24 = 30` reconciles exactly.
- **F1 is not hypothetical: the head is pinned at its clamp rail on 100% of fresh
  selections**, `bias_abs_mean == bias_scale` to float precision, in every arm. On this
  recipe that branch's gradient is exactly zero -- which is the mechanism behind the
  head weight-norm delta of exactly 0.0 that sits alongside `adv_surviving_frac = 1.0` in
  `shaped_rl`. A2 reads 1.0 through it.
- **F4's conversion surface reads zero.** `modulatory_shortlist_size` is 0.0 on every
  recorded tick. Stated precisely: that field is pre-seeded to 0 (`e3_selector.py:3553`) and
  only overwritten when the shortlist-then-modulate lever fires (`:4150`), so this shows the
  lever is **inert on this recipe** rather than that the shortlist is literally empty. Either
  reading has the same consequence for B1: its class count over the full 32-candidate pool is
  not counting the surface the lateral-PFC term can actually act on.

So B1 currently passes at 1.0 while the two quantities that would tell you whether conversion
was POSSIBLE both read at their degenerate end. That is the same shape as V3-EXQ-1039's C0d
passing at 0.667 with the head's output at chance -- one level down.

### RAISED AS A DECISION -- not decided by this session

**F2 (the load-bearing one). A2's "in every treatment cell" quantifier ranges over the
UNSHAPED sparse control, whose surviving-advantage fraction legitimately tends to 0 in
exactly the H1-favourable world.**

`adv = ep_return - EMA_baseline` with `EMA_DECAY=0.9` (`allon_training.py:412, 796-797`).
After one 0.2 waypoint visit the baseline is 0.02 and decays below `ADV_MIN_THRESHOLD=0.005`
in 14 reward-free episodes; zero-return terms are then skipped. V3-EXQ-1039 recorded
`sparse_rl@seed44` at **0.0 visits/ep** over 10 eval episodes. The dry run already shows the
shape: sparse and demo at `adv_surviving_frac = 0.0`, shaped at `1.0`.

Consequence: the outcome *"the sparse signal produced no gradient, the dense one did, and
behaviour still did not move"* -- a genuine, interpretable H1-negative result, and arguably
the most likely one -- self-routes to `substrate_not_ready_requeue` / FAIL naming
`adv_surviving_frac_clears_floor`. That is an instrument label on the manipulation's own
control regime, and a requeue that cannot clear by re-running.

The autopsy's wording is explicit ("in every treatment cell", section 14 item 1) and was
ratified. The chip's own framing is narrower -- "before any **flat null** is admissible" --
which would support gating only when the arms are actually flat. **Which reading governs is
the user's call.**

**F1 (gate half). A2 certifies the ADVANTAGE, never the gradient.**
`_lpfc_reinforce_loss` increments `n_adv_surviving` **before** `compute_bias` is called
(`allon_training.py:411-421`). On this recipe `rule_readout_consumer` is False, so
`compute_bias` takes the HARD-CLAMP branch `bias_raw.clamp(-bias_scale, +bias_scale)`
(`lateral_pfc_analog.py:483-486`) rather than the gradient-preserving scaled-tanh branch --
and that module's own comment (`:171-179`) states a saturated hard clamp has **zero
gradient**, so REINFORCE cannot move the head.

The dry run shows exactly that pair in `shaped_rl`: `lpfc_adv_surviving_frac = 1.0` with a
head last-linear weight-norm delta of **exactly 0.0**, while `hidden_dead_relu_frac = 0.4375`
(not dead) and `candidate_summary_degenerate_frac = 0.0` (not degenerate) rule out the two
zero-gradient routes the design already records. C0d's floor is `HEAD_DELTA_FLOOR = 1e-9`, an
existence check one unsaturated update clears. So a head saturated on nearly every tick can
pass the whole paired gate.

The saturation statistic is now RECORDED (above), which makes such a null attributable by a
later autopsy -- the difference from 1039. **Whether to also GATE on it is a criterion
change and is part of the same decision.**

**F3. Autopsy item 3's lPFC SHARE of the summed modulatory accumulator is not recorded.**
`_E3_CONVERSION_KEYS` (`allon_training.py:232-243`) carries `score_bias_*` and
`modulatory_authority_*`, all computed on `bias_detached` = the WHOLE summed score_bias
across channels, not the lateral-PFC channel's share. The per-channel breakdown exists
(`e3_selector.py:3745-3754`, `last_channel_terms`, keyed by channel name) but is gated on
`e3.e3_score_decomp_enabled`, which has ~24 gated call sites across `e3_selector.py` and
`agent.py` -- including one at `e3_selector.py:4259` whose comment mentions
decisiveness-margin consumers. **It could not be established as behaviour-neutral within this
session, so it was not switched on.** Turning it on would change what the agent does, which
is the one thing an instrument repair must not do silently.

## 5. The open decision

**Question.** The red-team shows the ratified readiness gate set has two problems. How should
V3-EXQ-1039a's gates be amended before it is queued?

| Option | What it measures | Cost |
|---|---|---|
| **A. Queue as ratified, unamended.** Keep A2 over every treatment cell; keep the saturation statistic recorded-not-gated. | The autopsy's literal wording. Accepts that a likely H1-negative outcome self-routes to `substrate_not_ready_requeue`, and that a saturated head can pass the gate (readable afterwards, not blocked). | ~110 min of fleet compute with a material chance of a non-answer. |
| **B. Narrow A2's quantifier to the arms whose manipulation IS the training signal** (`shaped_rl`; `demo_warmstart`'s absorption evidence is A3 by construction), recording `sparse_rl`'s fraction as telemetry. | Preserves the gate's purpose -- that a flat null is not read as "density does not matter" when no arm got gradient -- while letting the H1-negative result be reported. | Departs from the autopsy's literal "every treatment cell". |
| **C. B, plus add a saturation precondition** (`lpfc_bias_saturated_frac` below a declared ceiling in every treatment cell). | Closes F1's gate half: the third zero-gradient route becomes a gate, not just a record. | Adds an eleventh conjunctive gate; the ceiling would be an un-piloted bar. |
| **D. B or C, plus enable `e3.e3_score_decomp_enabled`** to record the lPFC share (autopsy item 3). | Discharges item 3 in full. | Requires auditing ~24 gated sites for behaviour-neutrality first -- a real piece of work, and a wrong call changes what the agent does. |

**This session's recommendation: B, and treat C as now well-motivated rather than speculative.**

The measured `lpfc_bias_saturated_frac = 1.0` moves C from "an extra un-piloted bar" toward
"the gate that would have caught 1039". The reason this session still does not simply apply it
is that the ceiling value is a scientific choice with no pilot behind it, and the whole point of
the consent rule is that such a choice is the user's. Restating the original reasoning for the
record: B is the minimum that lets the run
answer its own question, and it is consistent with the chip's own "before any **flat null** is
admissible" framing. C's ceiling would be a fourth un-piloted bar on a design that already
carries three; the saturation statistic being RECORDED already makes the failure mode
attributable, which is what this repair exists for. D is worth doing but belongs in its own
`/implement-substrate` pass against `e3_score_decomp_enabled`, not smuggled into an
experiment driver.

## 6. Where the work is

- **Driver:** LANDED and pushed at its canonical path on `ree-v3/main`, commit
  **`088157818e`** --
  `ree-v3/experiments/v3_exq_1039a_mech428_inv086_waypoint_field_consumer_drive_signal_absorption_gated.py`.
  It is **inert**: nothing runs an experiment script without an `experiment_queue.json`
  entry, and there is none. `audit_unqueued_experiment_scripts` will flag it, and that flag
  is CORRECT -- the queue step is genuinely owed, pending the decision below.
- **`V3-EXQ-1039a` is reserved** (`task_claim.py` slot `ree-v3/experiment_queue.json/V3-EXQ-1039a`) and free in all three namespaces.
- **Still owed once the decision lands:** apply it, re-smoke, write the queue entry (with the
  Step 2.4 / 2.5c / red-team lines), `validate_queue.py`, `ree_commit.py --push`, Step 8.6
  coordinator confirmation, and the `evidence_discrepancy` governance flag that lets
  `/governance` set V3-EXQ-1039's manifest `evidence_direction: superseded`.
- **Hypothesis space:** `waypoint_field_consumer_reach:H-wpfield-objective-sparsity` stays
  ALIVE; `hypothesis_space_registry.v1.json` is NOT edited by this session (single producer
  is `/failure-autopsy` Step 9b).


---

## 7. Resolution (appended 2026-09-18T23:10Z)

**Decision: OPTION B**, by the user via `AskUserQuestion` at 2026-09-18T22:58Z on decision
chip `chip-20260918-exq1039a-readiness-gate-amendment`.

- Precondition **A2 is narrowed to `A2_GATED_ARMS = ("shaped_rl",)`** -- the arms whose
  manipulation IS the training signal. `sparse_rl` and `demo_warmstart` surviving-advantage
  fractions are RECORDED per cell under the precondition's `ungated_arms_surviving_frac`,
  not gated. `demo_warmstart`'s absorption evidence remains precondition A3.
- **Option C DECLINED:** `lpfc_bias_saturated_frac` stays RECORDED, not gated. No ceiling.
- **Option D DECLINED:** `e3.e3_score_decomp_enabled` stays OFF; the lPFC-share readout
  (autopsy item 3's remaining half) is deferred to its own `/implement-substrate` pass and
  is NOT part of V3-EXQ-1039a.

**Applied and verified.** The post-amendment `--dry-run` re-run confirms
`adv_surviving_frac_clears_floor` now MET at 1.0 on `shaped_rl@seed42`, with
`sparse_rl@seed42: 0.0` and `demo_warmstart@seed42: 0.0` recorded as ungated telemetry --
i.e. exactly the configuration that would have failed the gate under the original
quantifier now passes it while still reporting the same numbers. The precondition carries
`scope_amendment: "user-ratified 2026-09-18 (option B); the autopsy's own wording was 'in
every treatment cell'"` so the departure from the autopsy is self-describing in every
manifest.

**Landed.**

| Artifact | Where |
|---|---|
| Driver + queue entry (one commit) | `ree-v3` **`80dae9b9bb`**, on `origin/main`; `ree_commit` delta `items: +1 (V3-EXQ-1039a)` |
| `validate_queue.py` | OK |
| `validate_experiments.py --strict` | OK, 0 non-conforming |
| `evidence_discrepancy` governance flag | **GFLAG-0353** (INV-086, MECH-428), on `origin/master` in `evidence/planning/governance_flags.v1.json` -- so `/governance` can set V3-EXQ-1039's manifest `evidence_direction: superseded` once 1039a lands. Its existing `non_contributory` stamp is left alone |

**Still open, deliberately:** autopsy item 3's lPFC SHARE of the summed modulatory
accumulator is NOT recorded by V3-EXQ-1039a (option D declined). The existing
`score_bias_*` / `modulatory_authority_*` keys are whole-`score_bias` aggregates across all
channels, not the lateral-PFC channel. If a 1039a null needs attributing to "the head was
outvoted in the arbitration" rather than "density does not convert", that readout is what
would settle it, and it needs `e3_score_decomp_enabled` audited for behaviour-neutrality
across its ~24 gated sites first.
