# Failure autopsy -- V3-EXQ-591h (ISEF-005 Phase 0->1 crossing-count gate, "live closed loop")

- **Generated (UTC):** 2026-09-03T04:15:52Z
- **Scope:** single
- **Status:** confirmed (user, interactive Step 8 gate, 2026-09-03T05:04:52Z)
- **Session:** autopsy-20260903-fails-diagnostics
- **Run:** `v3_exq_591h_isef005_phase01_gate_live_20260903T024528Z_v3` -- PASS, `experiment_purpose: diagnostic`, `claim_ids: ["ARC-019"]`
- **Self-route label:** `crossing_count_gate_discriminates_live_closed_loop`

## 0. One-paragraph summary

This run PASSED cleanly -- 5/5 seed agreement, all five preconditions met, recording-complete, 4.8
hours of real compute -- and its result is nonetheless uninterpretable, because **the closed loop it is
named for was never wired**. The one phase->behaviour channel this driver applies had its consumer
deleted on 2026-05-25 as dead-by-construction, and the run's own data confirm zero feedback: the two
arms' per-episode trajectories are bit-identical on every seed. This is not an ARC-019 result and must
not be recorded as one.

> **This artifact was materially revised after an adversarial red-team pass.** The first draft attributed
> the problem to a **missing substrate capability** and proposed a new substrate entry. That attribution
> is **wrong and is withdrawn**: the scheduler exposes two *other* phase-varying channels that do have
> live `ree_core` consumers, and this driver family simply does not wire them. The finding is
> experiment-design debt, not a substrate gap, and the routing changes accordingly
> (`implement-substrate`/create -> `queue-experiment`/amend). Section 11 records the full disposition.

## 1. Facts reconstruction

### 1.1 Dry-run gate (Step 2a)

`dry_run: false` on the manifest; `check_dry_run_citations.py` reports the run clean. Not a smoke.
Budget arithmetic is consistent: 2 arms x 5 seeds x 160 episodes x 200 steps = 320,000 =
`z_goal_stream.ticks_total`; `elapsed_seconds` 17,179 (4.77 h) against a declared 6 h.

### 1.2 Recording provenance

`validate_recording.py`: OK, 1 complete, 0 always-core gaps. Flat manifest by design (no run pack).
**No recording debt.**

### 1.3 What the run reports

All five preconditions met; `criteria_non_degenerate` true; `per_seed_agreement` 5/5 between the
crossing-count gate and the oracle; `status`/`outcome` PASS. The legacy control (`ARM_SPIKE`) agrees
with the oracle on 4/5.

## 2. The finding: the wired feedback channel has no consumer -- but two unwired ones do

The driver's stated mechanism distinguishing this "live" run from V3-EXQ-591f's offline replay is
`agent.config.e3.novelty_bonus_weight` moving **0.5 -> 0.7** on phase advance
(`v3_exq_591h_...py:365-366`; `infant_curriculum.py:243,248`).

**Nothing reads it.** A full search of `ree_core` finds only the dataclass field
(`ree_core/utils/config.py:1074`), its setter (`:8189`), a docstring
(`ree_core/predictors/e3_selector.py:1025`) and a comment
(`ree_core/environment/causal_grid_world.py:5246`). The consuming branch was removed --
`e3_selector.py:1364-1371` records that the MECH-111 broadcast branch that populated it *"was deleted
2026-05-25 (dead-by-construction -- uniform scalar shift is argmin-invariant)"*. A uniform scalar
added to every candidate's score cannot change an argmin, so the knob could not have had an effect
even if it were still read.

**The run's own data confirm it.** `per_episode_h_pos` is **bit-identical between `ARM_SPIKE` and
`ARM_CROSSING` on all 5 seeds** -- 0 differing episodes each -- including seed 42, where the two arms
advanced 12 episodes apart (104 vs 116), and seed 45, where one arm advanced and the other never did.
Offline replay of `ARM_SPIKE`'s series reproduces the live `ARM_CROSSING` advance episode on **5/5**
seeds. The live-vs-offline distinction this experiment exists to test yielded **zero divergence**.

This was independently reproduced by the mechanical pre-routing check: `autopsy_pre_routing_checks.py`
C7 fired on `h_pos_mean_full_run`, `n_pre_ep_min_crossings` and `post_ep_min_crossings` -- all three
vary across seeds and are bit-identical across arms in every seed.

**Consequence: the failure mode the experiment was built to detect is unreachable by construction.**
The driver names it -- *"The failure mode that matters is a SELF-DEFEATING GATE -- a genuine explorer
held in Phase 0 at the lower novelty weight never reaches 3 crossings"* (`:49-52`) -- and the verdict
grid carries a dedicated label for it (`:667-670`). Since the wired channel has no behavioural effect,
holding a seed in Phase 0 cannot lower its crossing count. That label could never fire.

### 2.1 THE SUBSTRATE IS NOT MISSING THE CAPABILITY -- the driver does not use it

This is the correction the red-team forced, and it changes the routing. `InfantCurriculumScheduler`
exposes **three** phase-varying outputs, and two of them have live consumers:

| scheduler output | Phase 0 -> Phase 1 | consumer | live? |
|---|---|---|---|
| `env_kwargs()` -> `harm_gradient_enabled` | False -> True | `causal_grid_world.py:2617` | **YES** |
| `env_kwargs()` -> `transient_benefit_enabled` | False -> True | `causal_grid_world.py:3077` | **YES** |
| `config_overrides()` -> `offline_integration_frequency` | 10 -> 20 | `agent.py:12070` | **YES** |
| `config_overrides()` -> `novelty_bonus_weight` | 0.5 -> 0.7 | none (deleted 2026-05-25) | **no** |

The 591h driver applies **only the dead one** (`:369-371`), and calls `env_kwargs()` without spreading it
into the environment constructor. It states this openly (`:153-162`), along with its reasoning: it is
faithful to 591b-591f, and Phase-0 `env_kwargs` equal the `CausalGridWorldV2` constructor defaults, so
since phases never retreat, applying them could not change a Phase 0->1 decision. **Only the original
V3-EXQ-591 curriculum-vs-flat run applied `env_kwargs`.**

That reasoning is *correct about the decision* -- and it is exactly why the design cannot produce arm
divergence at all. Pre-advance, both arms are in Phase 0 with identical environments; post-advance, the
only wired channel is inert. The driver's justification for omitting the live channels is simultaneously
the proof that its manipulation has no effect.

So the correct diagnosis is **experiment-design debt**, not a missing substrate build.

## 3. Three further defects, independent of the dead channel

Even taking the discrimination at face value:

1. **Oracle and gate are two thresholds on the same signal.** `h_pos_mean_full_run` (oracle) and
   `post_ep_min_crossings` (gate) are computed from the identical `per_episode_h_pos` array (and the
   arms are bit-identical, section 2). Pearson r = 0.883, Spearman 0.9. Crossing thresholds
   T in {3,4,5,6} **all** reproduce the oracle partition exactly, and oracle floors
   F in {0.105, 0.11, 0.15, 0.20, 0.25, 0.30, 0.318} all reproduce the T=3 gate partition exactly.
   Agreement here measures threshold monotonicity, not criterion validity.
2. **The partition is already fixed before the decision window opens.** The gate window starts at
   episode 100 (`_try_phase_0_to_1` requires `episode >= 100`). On episodes 0-99 alone,
   `n_pre_ep_min_crossings >= 3` (25 / 8 / 28 / 2 / 0) reproduces the oracle partition exactly, as
   does `h_pos_mean_pre_ep_min >= 0.20` (0.5804 / 0.3197 / 0.6325 / 0.0959 / 0.0453). No decision made
   at or after episode 100 can influence those numbers.
3. **The discriminative delta over the control is exactly one seed, at zero margin.** The legacy SPIKE
   gate agrees with the oracle on 4/5; the crossing gate on 5/5. The single differing seed is 45,
   which is also the sole `live_false_advancer` (`n_live_false_advancers = 1` against
   `P5_MIN_LIVE_FALSE_ADVANCERS = 1` -- zero margin). Precondition P5's own description says the
   reject leg is *"never challenged"* below that floor.

For completeness in the other direction: **constant predictors do not pass.** The majority-class base
rate is 3/5 = 60%, and under the conjunctive `combination_rule` "always advance" yields 3/5 and "never
advance" 2/5 -- both FAIL. So the base rate alone does not make the PASS trivial; the weight falls on
the three points above.

## 4. Claim-layer mapping -- ARC-019

`ARC-019` ("REE requires staged developmental training with explicit curriculum gates",
`architectural_commitment`, status `provisional`, `epistemic_category: standard`) carries **no**
`confidence`, `v3_pending`, `implementation_phase`, `evidence_quality_note`,
`diagnostic_evidence_adjudicated`, `supports` or `weakens` fields, and no conditional re-check
trigger. Its epistemic overlay channel is **`lit`** -- literature-only, with no experimental evidence
attached.

Two things follow.

**(a) A note on ARC-019's non-degeneracy precondition -- weaker than the first draft claimed.**
ARC-019's `what_would_answer` states, verbatim: *"This precondition must be independently verified (e.g.
staged arm reaches at least Phase 1 in >=80% of seeds) before treating any outcome below as evidence
either way."* `ARM_CROSSING` reached Phase 1 in **3/5 = 60%**; `ARM_SPIKE` in 4/5 = 80%. Two
qualifications the red-team was right to insist on: the 80% figure is introduced with *"e.g."* and is an
example operationalisation rather than a stated bar, and the clause gates *"any outcome below"* -- the
CONFIRMING and FALSIFYING legs, which are staged-vs-unstaged **outcome** comparisons that this run's own
`scope_limitation` puts out of scope. **So the precondition is not binding on 591h's stated question**,
and this autopsy does not rest on it. It is recorded because the `claim_ids: ["ARC-019"]` tag invites
exactly the reading the clause guards against, and because `non_contributory` follows independently from
section 2 regardless.

**(b) The claim tag is discontinuous with its own lineage.** V3-EXQ-591d / 591e / 591f all carry
`claim_ids: []` and their own prose says they bear on **ARC-046 / `infant_substrate:GAP-14`**; 591g's
error record is also claim-free. **591h is the first in the lineage to tag a claim, and the only
manifest in the entire evidence tree tagged ARC-019.** `GAP-14`'s `bears_on` list does not include
ARC-019. On this autopsy's reading the tag is incorrect, and it is what put an untested claim into
`pending_review.md` as though it had been tested.

`granularity_debt_cluster.py ARC-019` returns **0 targets across 0 files** -- this is the first autopsy
target ever to name the claim. The recurrence trigger does not fire, and the re-derive brake has
nothing to count.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | ARC-019 tagged here for the first and only time; lineage predecessors bear on ARC-046 / GAP-14 |
| Biological reference | clear | competence-gated developmental stage transitions are well-evidenced; the biology is not at issue |
| Prerequisites | **present, unwired** | the substrate offers two live phase channels (`env_kwargs` -> harm_gradient/transient_benefit; `offline_integration_frequency`); this driver family applies neither |
| Implementation | **stub as wired** | the one channel the driver applies had its consumer deleted 2026-05-25 as dead-by-construction |
| Environment | adequate | |
| Measurement | **misleading** | oracle and gate are two thresholds on one signal; partition fixed pre-window; delta = one seed |
| Integration | isolated | the two arms are behaviourally identical |
| Scale | adequate | 320,000 ticks, budget as declared |

### Failure-location summary (GOV-FAILLOC-1)

| bucket | verdict |
|---|---|
| MECHANISM | not established -- the manipulation as wired is inert |
| MEASURES | not established -- circular oracle, pre-fixed partition, n=1 delta |
| ENVIRONMENT | established |
| **REE FAILED** | **no** |

**Net: MIXED -- an EXPERIMENT-DESIGN failure compounded by MEASURES defects.** The gate could not have
been tested because the driver wired the one dead phase channel and not the two live ones. Nothing here
is evidence that REE failed at anything, and nothing here is a substrate gap.

## 6. Biological-reference triage

The closest reference mechanism -- developmental stage transitions gated on demonstrated competence
(critical-period / readiness gating) -- is well-evidenced, and the REE construct is a faithful
translation in *intent*. The divergence is not in the translation but in the wiring: in the biology, a
stage transition changes what the organism does and what it is exposed to; in REE as it currently
stands, a stage transition changes a scalar nothing reads. This is a `competence_implementation_gap`,
not a biology divergence, and no `/lit-pull` is owed.

## 7. Repair pathway

**Node classification:** `complicated (buildable)` -- and smaller than the first draft judged. No
substrate build is owed; the capability exists and needs wiring.

**Routing: `queue-experiment`** (a successor that wires the live channels), with an **`amend`** on the
existing `infant_substrate:GAP-14` node. The first draft's proposed new entry
`infant-curriculum-phase-has-no-behavioural-consumer` is **WITHDRAWN** -- it would have commissioned a
build for a capability that already exists.

Any successor must:

1. **Apply `env_kwargs()` and `offline_integration_frequency`**, not `novelty_bonus_weight`. Those are
   the channels with live consumers (section 2.1), and the original V3-EXQ-591 already applied
   `env_kwargs`.
2. **Carry a divergence precondition** asserting that the two arms' *trajectories* differ somewhere
   before any verdict is computed. An `arms_differ` check reading only the derived decision
   (`reached_phase1` / `phase_01_at`) passes happily on bit-identical trajectories, as it did here. One
   line would have caught this before 4.8 hours of compute.
3. **Fix the oracle circularity** (section 3): compute the oracle from a signal the gate does not read,
   and site the decision window so the partition is not already fixed before it opens.
4. **Take a NEW EXQ number.** `infant_gap14_redesign_staged_20260827.md` says verbatim *"This proposal
   recommends a new EXQ number when it is eventually authored, not a `591g` letter"* and *"Any redesign
   turns this flag ON. Do not re-open the gate-criterion question."* Node `infant_substrate:GAP-14-c2`
   is `done`, and an online==offline replay contract already ships
   (`ree-v3/tests/contracts/test_infant_curriculum_gap9.py:495-524`). 591g and 591h are 591-letters
   re-opening exactly the question that document closed -- governance should reconcile that.
5. **Update the contract pin.** `test_infant_curriculum_gap9.py:262-264` currently pins the dead
   `novelty_bonus_weight` key `> 0`; any change to the wiring must touch it.

**Standing planning instructions cut against this run having been queued at all**, and governance
should note it: `infant_gap14_redesign_staged_20260827.md` says verbatim *"Any redesign turns this
flag ON. Do not re-open the gate-criterion question."* and *"This proposal recommends a new EXQ number
when it is eventually authored, not a `591g` letter."* Node `infant_substrate:GAP-14-c2` is `done`,
and an online==offline replay contract already ships
(`ree-v3/tests/contracts/test_infant_curriculum_gap9.py:495-524`). 591g and 591h are 591-letters
re-opening exactly the question that document closed.

## 8. Read-across -- noted, not adjudicated

- **The ARC-019 tag: this autopsy RECOMMENDS GOVERNANCE REMOVE IT** (user decision at the Step 8 gate,
  2026-09-03). The run bears on ARC-019 in neither direction -- its manipulation was inert -- and the tag
  is what placed an untested claim into `pending_review.md` as though it had been tested. Whether
  ARC-046 / GAP-14 is the correct tag *instead* is **not** adjudicated here; the run did not test that
  either, and this autopsy recommends removal, not substitution.
- **The dead-channel class.** `novelty_bonus_weight` joins the eleven default-ON flags measured inert
  on 2026-08-22 (WORKSPACE_STATE, authority-to-action trace part 2) via the same argmin-invariance
  mechanism catalogued as **F-C2** in the 2026-07-09 audit. The general question -- how many declared
  control channels have no cross-candidate spread and therefore no authority -- is larger than this
  run and is **not** adjudicated here.

## 9. Smaller flags

- The `--dry-run` short-circuit that hid the V3-EXQ-591g crash is still structurally present:
  `c_discriminates` leads with `gate_green` (`:627-628`), and a dry run sets `n_episodes = 3` while
  the gate needs `episode >= 100`, so every non-`substrate_not_ready_requeue` label remains unreachable
  by the mandatory pre-queue smoke. The queue note describes a bespoke stubbed-`_run_cell` positive
  control as the substitute; **no such test file exists** under `ree-v3/tests/`. (591h's own
  `UnboundLocal` is genuinely fixed.)
- "20 cells" in the docstring and queue note is arithmetically impossible: 5 seeds x 2 arms = **10**,
  and the manifest holds exactly 10 `arm_results`.
- `substrate_commit.dirty: true` on `experiments/_lib/baselines/arc019_curriculum_gating.py` -- a path
  that `git log --all` cannot find, is absent from the Mac checkout, and the driver never imports.
- Seed 44's crossings went **up** (36 -> 37) against the docstring's directional prediction.
- `final_z_goal_norm` is ~0 in all 10 cells (1.1e-14 / 9.2e-12 / exactly 0.0), consistent with the
  2026-08-27 finding that `InfantCurriculumScheduler` inherits no z_goal-forming scaffold.
- `phase_12_at` is null and `phase3_hook_fired` false in all 10 cells (Phase 1->2 needs episode >= 500,
  unreachable in a 160-episode run).

## 10. Step 7b / 7c

- **7b (`autopsy_pre_routing_checks.py`):** `fire_count: 1` -- **C7**, naming `h_pos_mean_full_run`,
  `n_pre_ep_min_crossings` and `post_ep_min_crossings` as bit-identical across arms in every seed.
  **Acted on, not dismissed:** this is independent mechanical confirmation of the section 2 finding,
  reached without reading the substrate. C1/C2/C3 applied (the target is claim-tagged) and did not
  fire; C5 inapplicable (no sibling `.md` at check time).
- **7c (adversarial red-team, Fable):** see section 11.

## 11. Red-team verdict -- CONTESTED, accepted in full

Run on **Fable**, a different model from the drafter, with the drafter's reasoning withheld.

**The central factual finding was CONFIRMED.** The reviewer's own whole-tree grep found no live consumer
of `novelty_bonus_weight` and identified the deletion commit (`ree-v3 099743e`); it verified the
bit-identical trajectories by direct float comparison (0 differing episodes, max |diff| 0.0 on 5/5) and
specifically tested and rejected the seeding objection, noting the arms sat in *different phases* for
6-24 episodes on four seeds; and it reproduced Pearson r = 0.8826 and the pre-window partition
`[25, 8, 28, 2, 0]`.

**But the ATTRIBUTION, and therefore the ROUTING, were wrong.** The scheduler exposes two other phase
channels with live `ree_core` consumers that this driver family does not wire (section 2.1). The drafter
independently verified this before accepting: `harm_gradient_enabled` at `causal_grid_world.py:2617`,
`transient_benefit_enabled` at `:3077`, `offline_integration_frequency` at `agent.py:12070`, and
confirmed that `ree_core/environment/infant_curriculum.py` -- a path the first draft cited -- does not
exist (the scheduler is `ree-v3/experiments/infant_curriculum.py`).

Applied in full:

| defect | disposition |
|---|---|
| "No behavioural consumer / not instantiable / build substrate" | **WITHDRAWN.** Recast as driver-wiring debt. |
| Routing `implement-substrate` + `create` | **CHANGED** to `queue-experiment` + `amend` on `infant_substrate:GAP-14`. |
| `substrate_paths` named a non-existent file | **CORRECTED** to the real files. |
| ARC-019 80% precondition presented as binding | **SOFTENED** -- "e.g.", and it gates an out-of-scope comparison (section 4a). |
| Dead-key contract pin at `test_infant_curriculum_gap9.py:262-264` unmentioned | **ADDED** to the amend (section 7, item 5). |
| Spearman reported as 0.9 | **CORRECTED** -- 0.975 / 0.959. Verdict-neutral. |

**7b independently corroborated the surviving finding** rather than the withdrawn one: C7 fired on the
three gate metrics being bit-identical across arms, which is the section 2 result reached mechanically,
without reading the substrate.

## 12. What governance should apply

1. **Amend** `infant_substrate:GAP-14` with the failure record and the successor requirements in section
   7. **Do not create a new substrate entry** -- the first draft's proposal is withdrawn.
2. **ARC-019:** status stays `provisional`, `epistemic_category` stays `standard`. Set
   `diagnostic_evidence_adjudicated: true` (the claim currently carries no such field) and write the
   `evidence_quality_note` drafted in the JSON. `evidence_direction` for this run is
   `non_contributory`.
3. **Remove the ARC-019 tag** from this manifest (this autopsy's recommendation, per the user decision
   at the Step 8 gate). Do not substitute ARC-046 -- the run tested neither.
4. **Ledger:** no frozen-ledger entry exists for this question or for ARC-019, and this autopsy does
   **not** create one -- the leg is not a pre-registered rival in any portfolio.
