# Science-chip pre-flight verdicts, 2026-09-10/11

**Why this file exists.** These verdicts were recorded onto the chips themselves, twice, by two
different mechanisms, and were lost both times. This note is the durable copy. Read
`amend_prompt_hollow_ack` below before trusting any chip-borne finding.

Produced by `orchestrate-20260910-2213` and `orchestrate-20260911-0330` (metaworker-orchestrate
Step 1d-iii), as a read-only pass against live `ree-v3` before spending an Opus queue session.
Result: **1 RED, 5 AMBER, 0 GREEN** over six queue-ready chips.

## amend_prompt_hollow_ack -- READ THIS FIRST

Two recording channels have now silently failed for chip-borne findings:

1. **`claim_note`** (the route `metaworker-orchestrate` Step 1d-iii originally prescribed:
   `chip_ledger.py claim --note "<verdict>"` then `unclaim`). `claim_note` is a SINGLE
   OVERWRITABLE field, so the mandatory release step overwrites the verdict with its own
   boilerplate. Found 2026-09-10; fixed in `REE_Working 8e3832816`, which changed the skill to
   prescribe `amend-prompt` instead.

2. **`amend-prompt`** -- the replacement -- **is also not durable.** Six calls across two
   sessions (2026-09-10T23:11Z and 2026-09-11T03:3xZ) each returned
   `prompt amended ... previous prompt preserved in prompt_history -- coordinator-acknowledged;
   git write suppressed`, and NONE reached `origin/master:TASK_CHIPS.json`. Every affected chip
   is back to its original prompt length with `prompt_history` empty or holding only an
   unrelated older entry. Verified 4.5h after the first call against a 2-minute materializer, so
   this is not lag. `resolution_note` and `claim_note` written by the SAME sessions DID persist,
   which isolates the failure to the `prompt` field on the suppressed coordinator path
   (`chip_ledger.coordinator_amend_prompt`, ~line 3009).

   Consequence: last cycle's fix replaced one silently-lossy channel with another, so the skill
   currently prescribes a route that does not work. Until that is resolved, **record durable
   findings in a git-tracked note like this one**, not on the chip.

## Verdicts

### RED -- do not spend a queue session

**`chip-20260908-mech002-precision-monotonicity`** -- the chip's premise is false. `alpha_k` does
not exist anywhere in the live tree (0 hits across `ree_core/` and `experiments/`). The only
implementation of "precision x prediction error" -- `LatentStack.compute_prediction_error()`
(`ree_core/latent/stack.py:1665`) and `modulate_precision()` (`:1690`) -- has **zero callers**
anywhere in `ree_core`, `agent.py`, any experiment script, or any worktree. Both are dead code.
The live precision mechanism (`SplitEncoder` / `SharedDepthEncoder.precision_logit`,
`stack.py:938-939`, `1006-1039`) multiplies the STATE ENCODING, not prediction error, and is a
trained `nn.Parameter`, not a sweepable hyperparameter. E3's `current_precision`
(`e3_selector.py:814`) is DERIVED FROM prediction-error variance -- the opposite causal direction.

Trap if built anyway: the obvious form (`belief_update = alpha_k * pred_error`, no downstream
clamp) makes MONOTONE true by construction -- vacuous arithmetic. Only a build routed through a
real saturating nonlinearity could answer the question, and the chip's text does not specify one.
**Owed: an `/implement-substrate` proposal against MECH-002, not a `/queue-experiment` sweep.**

### AMBER -- queueable only with the named change

**`chip-20260909-exq935a-margin-cap-rerun`** -- REFUSED at `/queue-experiment` Step 2.5c on
2026-09-10, on stronger and DIFFERENT grounds than the pre-flight predicted. The gate fires on
`severity: corrupting`, whose `severity_note` named a live successor defect:
`classify_regime_shape()` returned `"graded"` on `any(floor < f < ceiling)` -- a 1-of-N
EXISTENTIAL -- while the entry's own `failure_record` bar is ">=2/3 seeds at >=2 adjacent
ratios". **CRITICAL CORRECTION TO THE PRE-FLIGHT:** its own recommended change (wire the unwired
H-KNIFE branch to `graded_at_some_r_fraction`) would have made that defective predicate
LOAD-BEARING, and its stated residual ("seed 42 never grades even at r=2.65") is exactly the data
shape the predicate launders into a clean pass. Do not apply that change as written.

STATUS 2026-09-11: the predicate is FIXED -- `ree-v3 606aea2` ("gradedness is a reproducibility
test, not an existential one"), 388 lines in the module plus 330 lines of contract tests in
`tests/contracts/test_regime_occupancy_gate.py`, design doc
`ree-v3/docs/substrate/mode-governance-engagement-regime-occupancy-reproducibility.md`. But
`substrate_queue.json` still reads `severity: corrupting` describing the fixed defect, so Step
2.5c keeps refusing. Raised as **GFLAG-0262**. Once governance clears it, 935a is queueable:
apply the autopsy's `required_changes` 1-6 with H-KNIFE pointed at the CORRECTED predicate, and
keep `_r_values()`'s hardcoded dry-run subset (`:729-741`) synced to the new `R_STAR` or the
already-fixed dry-run short-circuit regresses silently. Still true: re-scoring 935's banked cells
at r=2.45/2.65 gives C1/C2/C3 passing on out-of-sample seeds, monotone across two adjacent points.

**`chip-20260909-sd082-learning-signal-probe`** -- RESOLVED. Queued as V3-EXQ-1020
(`ree-v3 bd79a5ea74`), RAN 2026-09-11T00:31Z, **PASS** (3/4 criteria), verdict
`H_learning_signal_noisy_supported`. The load-bearing dense-synthetic-credit positive control
measured **1.0 against a 0.8 floor**, so the instrument was demonstrably NOT blind -- which is
what makes the answer interpretable and is exactly the ambiguity 822f could not resolve. The
red-team caught C2's 0.25 persistence ceiling being SGD-derived while measured over Adam deltas
(SGD pure-noise 0.120 vs Adam 0.449, crossing 0.25 only at ~300 updates vs this design's 70), so
C2 could not have fired even with its hypothesis maximally true; fixed at cause by bracketing C2
with pure-noise negative and dense-credit positive controls.

**`chip-20260909-mech465-conjunct3-queue`** -- substrate live for both arms (`urgency_weight`,
`config.py:1223`, consumer `e3_selector.py:3789-3795`); urgency-off arm mechanically trivial.
Blocker was the absent per-seed P2 floor, the only candidate figure being circular against
V3-EXQ-1015's own pass/fail split. **RESOLVED NEGATIVE 2026-09-11:** a COLD-arm-null calibration
was attempted on banked data and the floor **cannot be credibly derived** -- see
`mech465_p2_floor_cold_null_calibration_20260911.md` (`REE_assembly 5d98d46e1f`). The autopsy's
candidate statistic `P(rv < 0.874*median)` is identically 0.0000 on COLD for all 3 seeds and all
400 bootstrap replicates, so the floor is 0.0000 at every FPR and every WARM/PHASED cell clears it
-- including the seed-1 cells that are supposed to fail. The fallback IQR/median statistic gives a
non-degenerate null but still fails to separate seed 1 from seeds 0/3. What is missing is a
statistic of a different KIND -- keyed to distribution shape near the u=0.04 threshold rather than
a global dispersion ratio -- not more COLD seeds. The urgency-off baseline gap (precondition 2)
is separately owed and untouched.

**`chip-20260908-arc021-h1-drive-axis-leg`** -- NOT substrate-blocked: the ContextMemory crash
that blocked the H2 leg cannot reproduce here, because the 993a driver imports only
`ree_core.environment.causal_grid_world` (`993a:444`) -- no `ree_core.agent`, no E1/E2/E3 module,
no cross-step retained graph (corroborated by the H2-blocked record's own statement). But it is
NOT the one-line unfreeze the chip implies: deleting the `requires_grad_(False)` loop
(`993a:858-860`) changes nothing on its own, because the encoder calls below are wrapped in a
SEPARATE `torch.no_grad()` block (`:865-867`); a real unfreeze also needs the optimiser to hold
`encoder.parameters()` (none of `opt_sensory`/`opt_forward`/`opt_harm`/`self.opt` does) and must
resolve that `z_t`/`z_t1` are simultaneously MSE targets (`:700,701,787,788`) and differentiable
inputs. Also owed: attribution accuracy (absent everywhere, 0 grep hits) and the
`dv_bounds=[0.0,1.0]` fix. Calibration: V3-EXQ-1011 tested the frozen-encoder trunk-merge at n=96
paired seeds and found essentially no degradation (DENSE -0.0102, SPARSE +0.0524, wrong
direction), so H1's entire hypothesised effect must come from the unfreezing itself. FAIL is the
higher prior; the question is still live.

**`chip-20260909-ext002-latching-stage2`** -- substrate path real, no new flags, but stage 2 is a
genuinely DIFFERENT driver (983a's A0/A1 residue-freeze mechanics combined with a held-tick-aware
revisit-avoidance DV that exists in neither script; `MIN_POOLED_SEEDS` appears nowhere in
`ree-v3`). Blocker: **no numeric pass/fail threshold is specified anywhere** for stage 2's DV --
983a's calibrated `C1 = decline_gap >= 0.04` belongs to the repeat-rate DV stage 2 is explicitly
BARRED from reusing, and nothing replaces it. Second, independent risk: 983a's own P4
`revisit_denominator` precondition already failed once (seed 31 logged 0 erred keys and 0 revisits
in both arms), and stage 2's pool is expected to be dominated by exactly that low-harm
constant-mover profile. Pre-register a numeric DV threshold AND a revisit-volume precondition
BEFORE committing to the 27-38h cloud run.

## Standing lesson

Question (b) of the pre-flight -- *can the load-bearing criterion actually FAIL?* -- is the one
that pays. It caught MECH-002 (RED), and on 2026-09-08 it was the failure shape of 884a, 1007a
and 1012, two of which were FRESH governance-ratified designs. Age is not the trigger; the batch
is.
