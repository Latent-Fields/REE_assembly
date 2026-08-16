# MECH-151 affordance-set-size instrumentation -- staged design (BLOCKED at /queue-experiment Step 2.5c)

**Status: AWAITING USER REVIEW / BLOCKED ON SUBSTRATE. Nothing was queued. No experiment script was written.**

- **Generated (UTC):** 2026-08-16T20:42:35Z
- **Session:** `metaworker-chip-20260816-queueexp-mech151-affordance-set-instrumentation-v2` (headless metaworker chip, Mac / `DLAPTOP`)
- **Chip:** `chip-20260816-queueexp-mech151-affordance-set-instrumentation-v2`
- **Skill:** `/queue-experiment`, halted at **Step 2.5c** (substrate-path overlap gate) -- a `corrupting` stop-gate
- **Claims in scope:** MECH-151 (primary), SD-016, SD-055

---

## 0. What this document is

The chip asked for a MECH-151 driver recording the size of the live affordance set alongside
`mean_cue_action_bias_norm`, to disambiguate a confound the 2026-08-16 literature pull exposed
(Pastor-Bernier & Cisek 2011: premotor value biasing is competition-conditioned and relative, so a
correctly-functioning relative-bias mechanism reads at floor wherever the affordance set is
effectively single-option).

The design work was done. It is recorded here in full because it is reusable the moment the blocker
below clears. **What is NOT here is a queue entry or a script** -- `/queue-experiment` Step 2.5c
refuses both, and the refusal is correct (Section 2).

Two findings came out of the design pass that are worth more than the queue entry would have been,
and both revise premises this chip and the literature entry were written on. They are Sections 1 and 3.

---

## 1. CORRECTION: the V3-EXQ-640a null was SD-016 being OFF, not a dead gradient

The chip brief, and the Pastor-Bernier entry it draws on, both treat
`failure_autopsy_V3-EXQ-640a_2026-06-06`'s finding -- `mean_cue_action_bias_norm` NULL in all 6 cells
-- as a **dead-gradient defect** (the SD-055 gradient-flow question), and propose the affordance-set
confound as a **second** reading to rule out first. There is a **third** reading, and it is the
correct one. It dominates both.

The metric is computed in `ree-v3/experiments/v3_exq_640a_scaffold_cue_authority_gain_sweep.py:295`
as `sum_cue_action_bias_norm / n_cue_action_bias_present`. Both accumulators are written in
`ree-v3/experiments/scaffolded_sd054_onboarding.py:3554-3560`, guarded by:

```python
cab = getattr(agent, "_cue_action_bias", None)
if cab is not None:
    post_cue_diag["sum_cue_action_bias_norm"] += float(torch.as_tensor(cab).norm().item())
    post_cue_diag["n_cue_action_bias_present"] += 1
```

`agent._cue_action_bias` is set in `ree_core/agent.py:5402-5421` inside
`if hasattr(self.e1, 'world_query_proj'):` -- and `world_query_proj` exists **only when
`sd016_enabled=True`** (`ree_core/predictors/e1_deep.py:245-256`, `E1Config.sd016_enabled`,
default `False`). With SD-016 off, `_cue_action_bias` is set to `None` on every tick, so
`n_cue_action_bias_present` never increments and the mean is NULL.

**The scaffold says so itself**, at `scaffolded_sd054_onboarding.py:1112-1114`:

> `# SD-016 cue_action_proj bias norm (agent._cue_action_bias); usually 0 in`
> `# the 638a config (SD-016 off) -- captured for completeness so a future`
> `# SD-016-on arm is comparable.`

So the 640a null means **"the projection was never instantiated"**, not "the projection produced
zero" and not "the gradient was dead". `n_cue_action_bias_present = 0` is a *count of measurements
taken*, and it was zero. This is consistent with the 640a autopsy's own Section 3 point 2, which
already scoped the null out as "a *separate* known issue, not the cue-recall mechanism's fault" --
that scoping is right, but the autopsy attributes it to SD-016's documented ungroundedness rather
than to the arm simply not being armed.

**Consequences that matter downstream:**

1. **The affordance-set confound cannot be tested on the 640a lineage at all.** Under
   `sd016_enabled=False` the bias is structurally absent regardless of how many affordances are
   live, so no conditioning on affordance-set size can separate the hypotheses. Any successor must
   run `sd016_enabled=True` first. This is a **readiness precondition**, not a design choice.
2. **MECH-151's `evidence_quality_note` should not cite 640a as a dead-gradient datum.** It
   currently reads "the dead-gradient defect `failure_autopsy_V3-EXQ-640a_2026-06-06` found under
   DEFAULT settings (`mean_cue_action_bias_norm` NULL in all 6 cells) remains untested by this run".
   The parenthetical is accurate; the characterisation of it as a dead-gradient defect is not. The
   genuine dead-gradient evidence is **V3-EXQ-449** (`cue_action_proj.weight` receives exactly 0.0
   gradient through the CEM argmax; `ree-v3/CLAUDE.md` SD-016 section) -- that finding stands on its
   own and does not need 640a. Recommend a governance-side wording fix; **not** applied here (this
   session holds no `claims.yaml` claim, and claims.yaml is governance-only).
3. **The literature entry's inference is still valuable, just re-pointed.** "Record the size of the
   live affordance set alongside the bias norm, or the two hypotheses stay entangled" remains the
   right instruction. It should be aimed at an SD-016-armed successor, not retrospectively at 640a.

---

## 2. THE BLOCKER: `/queue-experiment` Step 2.5c, `corrupting` overlap on `e1_deep.py`

Step 2.5c cross-references the modules a driver will exercise against open `substrate_queue.json`
entries with a recorded code footprint. One `corrupting` entry overlaps:

| field | value |
|---|---|
| `sd_id` | `contextmemory-write-path-addressing-degeneracy` |
| `severity` | **`corrupting`** |
| `status` | `pending_implementation` (`status_phase: build_owed`, `ready: true`) |
| `priority` | 1 |
| `substrate_paths` | `ree_core/predictors/e1_deep.py` |
| `added_utc` | 2026-08-16T19:11:21Z (~1.5h before this session) |
| `unblocks_claims` | SD-017, ARC-045, MECH-166 |

**Title:** ContextMemory.write() hard-argmin addressing has a deterministic single-slot fixed point
under a low-variance query stream -- give the WRITE path the non-degenerate selection the READ path
already has.

**Why the overlap is material rather than incidental.** The entire measurement in this design runs
through `E1DeepPredictor.extract_cue_context()` (`e1_deep.py:494`), which produces `action_bias =
cue_action_proj(cat([cue_context, z_world]))`. `cue_context` is read out of ContextMemory. The
defect collapses ContextMemory to **1 occupied slot of 16**, so `cue_context` is near-constant and
`action_bias` degenerates to a deterministic function of `z_world` alone -- context-blind, which is
the negation of the "cue-indexed" property MECH-151 asserts. This is exactly the EXQ-449a failure
mode the `cat([cue_context, z_world])` concatenation was introduced to paper over ("cue_context is
constant under uniform attention", `e1_deep.py:251-254`): the concatenation keeps the *output* live
while the *cue-indexing* is gone.

**The decisive point, and the reason this is not an over-cautious reading:** the failure record was
measured under the **exact configuration this design would use**. `V3-EXQ-436f`
(`v3_exq_436f_sd017_mech166_sd016_armed_retest_20260814T194313Z_v3`) ran the full SD-016 production
combination ARMED and confirmed engaged (pooled applied ctxdiv loss 25,796.28 against a 1e-9 floor)
and still recorded `n_occupied_slots = 1 of 16 in BOTH arms on 3/5 seeds` despite 2,837-4,903
`ContextMemory.write()` calls per arm. The entry states plainly: *"The read-path fix (cue_slot_tagger
+ gumbel selection + context_divergence_weight 0.5 + 922 ctxdiv training-loop wiring) changes
write-path occupancy by ZERO seeds."* That read-path fix **is** the production combo V3-EXQ-922
validated and that this design inherits. So the defect is not merely on a shared file -- it has been
measured, twice (436e, 436f), to survive the precise config this experiment would run.

**What running anyway would produce.** A well-formed manifest reporting bias norm and bias effect
conditioned on affordance-set size, from which the three-way prediction table in Section 4 would be
read -- against a bias that was never genuinely cue-indexed. The entry's own `severity_rationale`
names this outcome: *"Nothing errors, the readout is well-formed, and the resulting null looks like
a genuine finding. That is the definition of `corrupting` -- evidence that LOOKS valid but is not."*
Under the affordance-set framing the corruption is worse than a plain null, because a context-blind
bias would most likely read at floor in **both** regimes -- which is precisely the
"dead-gradient defect" cell of the prediction table. The run would manufacture a false confirmation
of the very reading Section 1 shows was never established.

**In-flight check (Step 2.5c requires it):** no `/implement-substrate` is in flight on this `sd_id`.
Zero active `TASK_CLAIMS.json` entries reference contextmemory / e1_deep / write-path; zero hits in
`igw_routine_ledger.json` and `igw_assignments.json`. The single `TASK_CHIPS.json` hit is
`chip-20260816-step25c-inert-corrupting-stamp`, which is about the Step 2.5c *gate's* own
status-matching, not this build. A chip has been spawned by this session to give the build an owner
(Section 6).

---

## 3. Design finding: the affordance-set instrument already exists in the substrate

Nothing needs to be built to measure affordance-set size. `HippocampalModule.propose_trajectories()`
already populates `self._last_propose_diagnostics` (`ree_core/hippocampal/module.py:2263-2288`) with:

- **`candidate_unique_first_action_classes`** -- the count of distinct first-action classes across
  the returned candidate set. **This is the live affordance-set size** the Pastor-Bernier entry asks
  for, in the most direct form the substrate offers.
- `candidate_first_action_entropy` -- a graded companion (a set of 8 candidates that is 7:1 is not
  the same competition as 4:4).
- `candidate_first_action_counts`, `candidate_samples_collected`.
- `cem_iteration_diagnostics[]` -- the same three quantities per CEM iteration, so the affordance
  set can be tracked as it narrows across the search rather than only at its end.

**A trap the substrate flags in its own source, which any successor must respect.** The same block
records `action_object_roundtrip_recovery` with this comment:

> `# roundtrip_unique_classes == 1 while true_unique_classes > 1 means`
> `# any driver selecting via the decoder round trip is inert. See`
> `# candidate_first_action_class() for the mechanism and the correct accessor.`

So affordance-set size must be read via `candidate_first_action_class()`, **not** by decoding
action-objects back through `action_object_decoder`. A driver that measures the affordance set
through the round trip can report 1 where the true set is larger, which would silently manufacture
the "single-option" regime this design contrasts against -- an instrument that fabricates its own
independent variable. Record `action_object_roundtrip_recovery` alongside, as a guard.

---

## 4. The staged design (queue this once Section 2 clears)

### 4.1 Purpose and framing

`EXPERIMENT_PURPOSE = "diagnostic"`. This discriminates *why* a bias readout sits where it does; it
does not test a claim hypothesis directly. `claim_ids` should be `["MECH-151"]` only -- SD-016 and
SD-055 are exercised but not tested (per-claim tagging rule; do not inherit 922's four-claim tag).

### 4.2 The architectural fact that shapes the whole design

`action_bias = cue_action_proj(cat([cue_context, z_world]))` takes **no input from the candidate
set**. MECH-151 as implemented is therefore *structurally incapable* of competition-conditioning:
the bias vector cannot vary with affordance-set size, because affordance-set size is not an
argument to the function that computes it.

This makes the chip's prediction table ill-posed **for the norm alone** -- `||action_bias||` cannot
be conditioned on affordance-set size by construction, so "non-zero in multi-option, floor in
single-option" is not a reachable outcome for that statistic. What *can* vary with the affordance
set is the bias's **effect**: with one viable action-object there is nothing to reorder; with many,
an additive shift can change which candidate wins. So the design needs a **pair** of DVs, and the
prediction table must be restated over both (Section 4.5).

This is itself a reportable finding about MECH-151's functional form, and it sharpens rather than
weakens the Pastor-Bernier comparison: the primate arrangement is competition-conditioned because
the biasing signal is computed *relative to the alternatives*; MECH-151's is computed before the
alternatives are known.

### 4.3 DVs

1. **`mean_cue_action_bias_norm`** -- `||action_bias||`, via 922's `_action_bias_mean_norm()`
   (`v3_exq_922_...py:515`). Tests whether the projection is live at all. Under SD-016-on this is
   expected non-null; a null here reproduces the 640a signature and would mean SD-016 failed to arm.
2. **`bias_selection_divergence`** -- the effect measure, and the load-bearing one. Paired forward
   passes through `propose_trajectories()` on **identical RNG state**, once with `action_bias=b` and
   once with `action_bias=None`, comparing the resulting first-action class distribution
   (total-variation distance) and the selected candidate. Measurement-only: no backprop through the
   CEM, so this avoids the "materially different, higher-engineering-risk training loop with no
   existing validated recipe" that `v3_exq_922`'s docstring correctly declares out of scope.
3. **`candidate_unique_first_action_classes`** -- the conditioning covariate (Section 3).

### 4.4 Manipulation and conditioning -- both, deliberately

- **Manipulated axis:** `num_candidates` high vs low, giving a genuinely multi-option and an
  effectively single-option regime. Clean contrast, but it also changes CEM search quality, so it
  is confounded on its own.
- **Measured covariate:** per-selection `candidate_unique_first_action_classes`, used to condition
  the analysis *within* each arm. Unconfounded by construction but observational.

Neither is sufficient alone; reported together, agreement between them is the result and
disagreement localises the confound. This is what the literature entry's "record the size of the
live affordance set alongside the bias norm" actually requires -- the conditioning, not just the
contrast.

### 4.5 Restated prediction table (declare all three in the queue-entry description)

| outcome | `||action_bias||` | `bias_selection_divergence` (multi-option) | (single-option) | reading |
|---|---|---|---|---|
| Inert projection | floor in both | floor | floor | the dead-gradient / ungrounded reading; consistent with V3-EXQ-449's `action_bias_divergence = 0.0` |
| Working, competition-conditioned effect | non-zero in both | non-zero | floor | the bias exists unconditionally but only *expresses* under competition -- the Pastor-Bernier-compatible outcome |
| Working additive bias, MECH-151 as written | non-zero in both | non-zero | non-zero | MECH-151's literal form holds and **diverges from the primate data** -- a finding about the claim's functional form, not a defect |

The third row is the one to flag explicitly to governance. Per
[memory] `feedback_diagnostic_experiment_descriptions`, all three directions go in the queue entry
description, not just the hoped-for one.

### 4.6 Readiness preconditions (all four are load-bearing)

Per the P0 readiness-assert rule, each must carry numeric `measured` + `threshold` + `control`,
and a below-floor reading self-routes to **`substrate_not_ready_requeue`** -- never to a
substrate-verdict label.

1. **`sd016_armed`** -- `hasattr(agent.e1, 'world_query_proj')` and `agent._cue_action_bias is not
   None` after a real tick. This is the Section 1 precondition; without it the run reproduces 640a
   and measures nothing.
2. **`contextmemory_occupancy`** -- `n_occupied_slots >= 2`. **This is the Section 2 blocker
   expressed as a runtime gate.** It must be present even after the substrate build lands, as the
   regression guard.
3. **`affordance_set_non_degenerate`** -- in the multi-option arm,
   `candidate_unique_first_action_classes >= 2` on a positive control. Same-statistic rule: the
   load-bearing criterion routes on the affordance-set count, so the readiness check must assert
   that count, not a proxy for it.
4. **`roundtrip_recovery_non_inert`** -- `action_object_roundtrip_recovery` shows
   `roundtrip_unique_classes > 1` where `true_unique_classes > 1` (Section 3's trap).

**Regime-conditioning:** precondition 3 is meaningful only for the multi-option arm. Declare it with
`PreconditionSpec(..., applies_to=...)` from `experiments/_lib/precondition_gate.py` and aggregate
with `aggregate_arm_gates` so a red single-option arm cannot vacate a green multi-option arm --
the V3-EXQ-785 defect. Do **not** hand-roll the gate.

### 4.7 DV-symmetry declaration (mandatory, per arm)

`action_bias` is a **broadcast additive shift applied to every candidate's action-object**. The
symmetry table in the skill is explicit: a uniform additive constant across candidates is invisible
to argmax/softmax selection. **This is the V3-EXQ-604c failure mode and this design sits directly in
its path** -- it is the single largest design risk here, larger than the compute.

The bias is *not* a per-candidate quantity, so whether it can move selection at all depends on
whether it enters before or after a candidate-dependent transformation. `propose_trajectories`
passes `action_bias` into every `E2.rollout_with_world()` call, where it shifts each candidate's
action-object *before* the rollout -- and the rollout is non-linear in the action-object, so the
downstream score shift is candidate-dependent and does **not** cancel. That is the argument that
this design measures something. **It must be verified empirically in the smoke test, not asserted**:
assert `bias_selection_divergence > 0` for at least one seed in the multi-option arm before
committing to the full grid. If it is exactly 0.0 across all seeds, the arm is DV-symmetry-invariant,
must be scoped out of scoring, and routed `non_contributory` under `substrate_ceiling` -- explicitly
**not** `mixed`, which would connote a measured weak effect where nothing was measured.

Record `candidate_first_action_entropy` **range** across candidates as well as the norm: per the
604c worked example, a broadcast term cancels in a range but not in a magnitude, so the two
statistics disagree in exactly the diagnostic way.

### 4.8 Base recipe, cost, and the secondary question

- **Recipe:** `v3_exq_922_sd016_mech151_152_arc041_production_combo.py` is the closest working
  lineage. Config: `world_dim=128`, `alpha_world=0.9`, `sd016_enabled=True`,
  `sd016_cue_slot_tagger=True`, `sd016_cue_slot_tagger_selection="gumbel"`,
  `sd016_context_divergence_weight=0.5`, `use_differentiable_cem=True`. Train `cue_action_proj` by
  922's validated phased direct-supervision recipe (`compute_cue_action_loss`, MSE against
  `e2.action_object(z, action).detach()`), P0A 60 episodes (`zworld_p0_episodes=60`, SD-070's
  validated operating point -- grep every `_train_all_on_agent(` call site), P1 40.
  **Full `/queue-experiment` discipline applies -- this is a copy-and-modify base, which the skill
  explicitly denies a fast path.**
- **Cost:** low. V3-EXQ-922a recorded `elapsed_seconds: 79.50` for 3 seeds on `ree-worker-3`. Two
  arms x 3 seeds plus a paired measurement phase should stay well inside 30 minutes.
  `machine_affinity: any` (cloud), so the in-line mint is cloud-machine-class and reusable.
- **Mint as you go:** emit the OFF/baseline arm reuse-ELIGIBLE with
  `include_driver_script_in_hash=False`, and factor the OFF path into
  `experiments/_lib/baselines/<lineage>.py`. Do **not** queue a separate mint job -- neither
  exception case applies.
- **Secondary (Gourley) question -- do NOT include.** "Does the bias survive devaluation of the
  outcome it points at?" is a genuinely open and valuable question (dorsolateral stimulus-response
  shortcut vs ventrolateral outcome-model-dependent reweighting), and nobody has asked it. But it
  needs a devaluation manipulation that does not exist in this design, and the chip is explicit that
  it must not displace the primary contrast. It is recorded here as a successor, not folded in.

---

## 5. What a reviewer should decide

1. **Accept or overturn the Step 2.5c block.** Section 2 argues it is correct and materially
   grounded, not precautionary. Overturning it means accepting a run whose bias may be
   context-blind.
2. **The Section 1 correction to MECH-151's `evidence_quality_note`** -- governance-owned, not
   applied by this session.
3. **Whether Section 4.2's structural point** (MECH-151's bias takes no input from the candidate
   set, so it cannot be competition-conditioned as implemented) is better handled as a claim-wording
   amendment than as an experiment. It may be that the experiment is only worth running to measure
   the *effect*, the *norm* half being settled by inspection.

## 6. Follow-on spawned by this session

- `chip-20260816-implsub-contextmemory-writepath-degeneracy` -- `/implement-substrate` on
  `contextmemory-write-path-addressing-degeneracy`. Priority 1, `ready: true`, no design doc owed,
  unblocks SD-017 / ARC-045 / MECH-166 **and** this experiment. The implementation hint is specific:
  apply the annealed Gumbel-softmax selection V3-EXQ-908 already confirmed for the READ path to the
  WRITE address, or add an occupancy/usage-balancing term. Note `compute_diversification_loss()`
  already acts on `self.memory`, but the write update runs under `torch.no_grad()` and is unaffected
  by it.
