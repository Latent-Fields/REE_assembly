---
status: candidate/v3_pending
status_asof: 2026-08-01
status_claim: MECH-324
---

# MECH-324 Reacquisition Window Isolation -- targeted bugfix design

**IGW item:** IGW-20260731-196 (`substrate_queue.json` sd_id
`MECH324-REACQ-WINDOW-GATING-DECOUPLE`)
**Claims:** MECH-324 (primary), MECH-323 (the formation gate this reuses)
**Subject:** `policy.composition.chunk_maintenance_dissolution` -- rapid-reacquisition
sub-mechanism only. Not a new architectural decision; this is a bugfix design for
already-built substrate.
**Status:** IMPLEMENTED 2026-07-31 (ree-v3 `7747a01c94`, human-confirmed after the
design pass below; see ree-v3/CLAUDE.md's MECH-324 reacquisition-window-isolation
entry for the full implementation record)
**Registered:** 2026-07-31
**Depends on:** none (patches existing MECH-324 code; both switches it touches,
`use_chunk_maintenance` and `use_chunk_dissolution_retention`, are already built and
already default OFF)
**Blocks:** re-validation of the MECH-324 rapid-reacquisition relapse falsifier --
V3-EXQ-829a queued (supersedes V3-EXQ-829), not yet run; no other claim is gated on
this fix.

This is a **targeted bugfix note**, not a brand-new SD doc, per the judgement call
offered in the IGW task brief: the base substrate (`ChunkAccumulator` / `ChunkLibrary`
in `ree-v3/ree_core/policy/policy_chunking.py`) already exists, is already documented in
its own ~420-line module docstring, and is already covered in `claims.yaml` MECH-323 /
MECH-324 `implementation_note`. What is missing is not an architecture decision but a
single incorrect data-flow inside an existing, already-flagged code path. A full
`sd_NNN_*.md` doc would duplicate context that already lives in those two places; this
doc instead states the bug, the fix, and the exact call sites, and is meant to be read
alongside the module docstring's "DISSOLUTION IS SUPPRESSION-WITH-RETENTION" section
(`policy_chunking.py` lines ~305-376) and the claims.yaml MECH-324 entry's 2026-07-27
V3-EXQ-829 paragraphs (`docs/claims/claims.yaml`, `id: MECH-324`, lines ~43325-43360).

---

## Problem

V3-EXQ-829 (`ree-v3` `77e3ddc`, run
`v3_exq_829_mech324_rapid_reacquisition_falsifier_20260727T170539Z_v3`, 66 cells = 6
seeds x 11 arms) is the first experimental evidence for MECH-324's rapid-reacquisition
prediction: a chunk forced to DISSOLVED and then re-presented with the same consistent,
above-baseline regime should re-form in **materially fewer** repetitions than original
acquisition, scaling with the configured `reacquisition_repetition_factor` (`f_reacq`).
The run returned **FAIL**, evidence_direction **MIXED** for MECH-324:

- `median_r_reacq` was **flat at 90.0** (W = window_trials = 100) and **flat at 28.0**
  (W = 30) across **all four** tested `f_reacq` values (1.0, 0.5, 0.25, 0.1) -- Spearman
  rho vs. `f_reacq` was undefined because the DV never moved.
- `r_reacq / window_trials` measured **0.908 +/- 0.029** across the whole sweep -- the
  DV tracks the window length, not the repetition bar `f_reacq` sets.
- The degeneracy check (are cells sitting exactly on the forced bar, which would make
  the flatness an arithmetic identity rather than a real measurement) was run and
  **passed** (`all_on_cells_sit_on_forced_bar = false`): the flatness is real.

The claim's own registered null (`f_reacq = 1.0`, reacquisition no faster than
acquisition -- what a pure erasure operator would predict) was **not** rejected: the
substrate as-built cannot currently exhibit the faster-reacquisition signature at any
tested `f_reacq`, because something else is the binding constraint on `r_reacq`.

**Target for a corrected implementation:** `median_r_reacq` scales measurably with
`f_reacq` at fixed `W` (the claim's own falsifiable prediction), and stops tracking `W`
once `f_reacq` is the binding constraint.

---

## Root cause

### The two things `_attempt_reacquisition` currently reads

`PolicyChunking._attempt_reacquisition()` (`policy_chunking.py:1917-1956`) is the
revival gate. For each dormant (DISSOLVED, non-replay-origin) chunk it checks, in
order:

1. `chunk.reacquisition_repetitions >= bar`, where `bar =
   config.reacquisition_min_repetitions = ceil(min_repetitions * f_reacq)` -- this is
   the ONLY place `f_reacq` enters the gate, and it is a dedicated counter
   (`ChunkedPrimitive.reacquisition_repetitions`) that already correctly counts real
   executions **since the most recent dissolution** (reset to 0 in `_mark_dissolved`
   and again in `revive()` -- see `policy_chunking.py:1538` and `:1599`).
2. `var = variances.get(chunk.key)` and `mu = _mean(self.accumulator._tally.get(chunk.key, ()))`
   -- variance and mean must clear the SAME two MECH-323 gates as original formation
   (`var < variance_low`, `mu > baseline + evaluative_margin`). Both are read from
   `variances`, computed one line earlier in `PolicyChunking.note_outcome()`
   (`policy_chunking.py:1887-1889`) as `_variance(accumulator._tally[key])` --
   **`accumulator._tally[key]` is the sequence's raw, whole-lifetime sliding window**,
   FIFO-capped at `window_trials` (W), never reset or segmented at dissolution.

Step 1 is correctly reacquisition-scoped. **Step 2 is not** -- it reads the same tally
bucket the original MECH-323 formation gate reads, and that bucket keeps accumulating
across the dissolution boundary rather than starting fresh.

### Why that makes `f_reacq` inert by construction

Reaching DISSOLVED at all requires `T_dissolve` (`dissolve_trials`, default 50) trials
of supra-`variance_high` outcomes for that exact sequence -- and those outcomes are
recorded into the *same* `accumulator._tally[key]` bucket that formed the chunk in the
first place (`ChunkAccumulator.note_outcome`, `policy_chunking.py:1055-1105`, is the
single write path for every sub-sequence credit regardless of the chunk's lifecycle
state). So at the moment a chunk reaches DISSOLVED, `accumulator._tally[key]` is, by
construction, saturated with the very high-variance stream that caused the dissolution
(up to `min(T_dissolve, W)` of the `W`-length window). Once P2 (re-presentation) begins
feeding fresh, low-variance outcomes for the same key into the same FIFO-capped bucket,
`var < variance_low` cannot clear until enough fresh entries have aged the
dissolution-episode entries **out of the window** -- which takes on the order of `W`
trials, independent of the repetition bar `bar` sitting on an entirely different
counter (`reacquisition_repetitions`).

Concretely, at the registered defaults (`R_min = 20`, `T_dissolve = 50`,
`variance_low = 0.15`, `variance_high = 0.45`) the window-clearing time dominates every
tested `bar` (20 / 10 / 5 / 2 for `f_reacq` in 1.0 / 0.5 / 0.25 / 0.1), so `r_reacq`
always resolves to "however long the window takes to clear," not to `bar`. That is
exactly the measured signature: `r_reacq` flat across `f_reacq`, and `r_reacq / W`
constant (~0.9) across the whole sweep. **The bug is a data-flow bug, not a value
miscalibration**: `reacquisition_min_repetitions` is being computed correctly from
`f_reacq`, but the variance/mean readout the revival gate ANDs it with is not scoped to
the reacquisition period at all.

### Why the existing contract suite did not catch this

`tests/contracts/test_arc071_policy_chunking.py`'s rapid-reacquisition tests
(`test_c10_rapid_reacquisition_needs_far_fewer_repetitions...`,
`test_c10_reacquisition_still_requires_consistency_and_contrast`) use a `_dissolve()`
helper (`test_arc071_policy_chunking.py:354-361`) that forces the state machine
directly -- `chunk.state = ChunkState.DISSOLVING` then repeated
`tick_maintenance({chunk.key: 0.99})` calls with a **hand-supplied** variance dict --
rather than driving dissolution through real high-variance executions of the target
sequence via `note_outcome`. Because `accumulator._tally[chunk.key]` is never touched
by `_dissolve()`, the existing unit tests' target-sequence tally contains **only** the
original consistent-outcome entries from `_run()` and is never actually contaminated.
`test_c10_rapid_reacquisition_needs_far_fewer_repetitions` therefore correctly measures
`reformed_after == bar` (5) -- but only because its harness happens to sidestep the
exact mechanism V3-EXQ-829's realistic driver exercises (P1 feeds real alternating
high/low outcomes into the SAME `note_outcome` call path for the SAME target sequence,
which is what actually contaminates the tally). **This is a pre-existing test-suite
gap, not evidence the substrate is correct**, and any new contract test added alongside
this fix must dissolve via the realistic path (real contaminating `note_outcome` calls
on the target sequence, matching `_run_cell()` in the V3-EXQ-829 driver) or it will not
exercise the bug it is meant to guard against.

---

## Solution

### 3a. Config changes

| Param | Type | Default | Purpose | Config class |
|---|---|---|---|---|
| `use_reacquisition_window_isolation` | `bool` | `False` | sub-switch under `use_chunk_dissolution_retention`. `False` = current (buggy) behaviour, bit-identical: the revival gate reads `accumulator._tally[key]` as today. `True` = the revival gate reads a dedicated per-chunk post-dissolution window instead. | `PolicyChunkingConfig` |

No other new params. `reacquisition_repetition_factor` (`f_reacq`), `min_repetitions`
(`R_min`), `variance_low` (`F_low`), `evaluative_margin` are all unchanged and keep
their current meaning -- the fix does not touch what the thresholds ARE, only which
window they are evaluated against.

`PolicyChunkingConfig.validate()` gains one precondition, following the exact pattern
already used for `use_chunk_dissolution_retention` requiring `use_chunk_maintenance`
(`policy_chunking.py:795-803`):

```python
if self.use_reacquisition_window_isolation and not self.use_chunk_dissolution_retention:
    raise ValueError(
        "use_reacquisition_window_isolation requires use_chunk_dissolution_retention "
        "(with retention off no chunk is ever dormant, so the isolated window is "
        "never populated and the flag would be silently inert)"
    )
```

This is a LOUD precondition, not silent tolerance, matching the module's established
convention for every prior sub-switch (see `use_chunk_dissolution_retention` requiring
`use_chunk_maintenance`, and the analogous docstring rationale for each).

### 3b. Data flow

```
[P1: real high-variance note_outcome() calls for the target sequence]
    -> accumulator._tally[key]  (FIFO window, capped at window_trials, UNCHANGED --
                                  still used by CRYSTALLISED/DISSOLVING hysteresis,
                                  which legitimately needs whole-lifetime windowing)
    -> chunk reaches DISSOLVED via ChunkLibrary._mark_dissolved()

[dissolution boundary: NEW]
    -> ChunkedPrimitive.reacquisition_outcomes cleared (mirrors the existing
       reacquisition_repetitions = 0 reset already in _mark_dissolved())

[P2: real note_outcome() calls for the target sequence, chunk state = DISSOLVED]
    -> PolicyChunking.note_outcome() passes the RAW outcome_signal (not just its
       derived variance) through to ChunkLibrary.note_real_execution()
    -> ChunkLibrary.note_real_execution()'s DISSOLVED branch appends outcome_signal
       to chunk.reacquisition_outcomes (FIFO-capped at window_trials, same cap
       discipline as the accumulator's own tally) -- alongside the EXISTING
       reacquisition_repetitions += 1, so the two stay in lockstep by construction
    -> PolicyChunking._attempt_reacquisition(): with use_reacquisition_window_isolation
       True, var/mu are computed from chunk.reacquisition_outcomes (POST-DISSOLUTION
       ONLY) instead of accumulator._tally[key] (WHOLE-LIFETIME, dissolution-episode-
       contaminated)
    -> ChunkLibrary.revive() on pass -> chunk.state = FORMING (unchanged: revival
       still restarts C_min crystallisation from zero, a separate sub-mechanism)
```

### 3c. `ChunkedPrimitive` field addition

```python
reacquisition_outcomes: List[float] = field(default_factory=list)
```

Placed next to `reacquisition_repetitions` in the dataclass and documented in the class
docstring the same way: "outcomes observed on real executions SINCE the most recent
dissolution, counted only under `use_chunk_dissolution_retention`. FIFO-capped at
`window_trials`. Populated regardless of `use_reacquisition_window_isolation` (mirrors
the existing convention that new fields are written under the enclosing flag and only
*consulted* under the sub-flag -- see the module docstring's note on
`n_dissolutions`/`n_reacquisitions` being 'inert when retention is off: the two new
fields are written but nothing reads them'); read only when
`use_reacquisition_window_isolation` is True."

### 3d. Code-level changes, by call site

**`ChunkLibrary._mark_dissolved()`** (`policy_chunking.py:1527-1539`) -- add one line
next to the existing `chunk.reacquisition_repetitions = 0`:

```python
chunk.reacquisition_repetitions = 0
chunk.reacquisition_outcomes = []          # NEW -- symmetric reset
```

**`ChunkLibrary.revive()`** (`policy_chunking.py:1554-1604`) -- add one line next to
the existing `chunk.reacquisition_repetitions = 0`:

```python
chunk.reacquisition_repetitions = 0
chunk.reacquisition_outcomes = []          # NEW -- symmetric reset
```

(Revival can be followed by a later re-dissolution of the same chunk; without this
reset a second dormancy cycle would start with a stale window left over from the first.)

**`ChunkLibrary.note_real_execution()`** (`policy_chunking.py:1467-1525`) -- add an
optional parameter and populate the window in the existing DISSOLVED branch:

```python
def note_real_execution(
    self,
    sequence: Sequence[int],
    outcome_variance: float,
    outcome_signal: Optional[float] = None,   # NEW, default None = fully backward compat
) -> Optional[ChunkState]:
    ...
    elif chunk.state is ChunkState.DISSOLVED:
        if c.use_chunk_dissolution_retention and chunk.is_dormant:
            chunk.reacquisition_repetitions += 1
            if outcome_signal is not None:                      # NEW
                chunk.reacquisition_outcomes.append(float(outcome_signal))
                if len(chunk.reacquisition_outcomes) > c.window_trials:
                    del chunk.reacquisition_outcomes[: -c.window_trials]
    return chunk.state
```

The new parameter is appended after the existing positional/keyword parameters with a
default of `None`, so the one existing call site inside this module is the only one
that needs updating and the two direct-call sites in
`tests/contracts/test_arc071_policy_chunking.py:177,254` (which call with
`outcome_variance=` as a keyword, never a 3rd positional arg) are unaffected.
Populating the window is gated only on `use_chunk_dissolution_retention` (the existing
enclosing condition), not on the new sub-flag -- see the field docstring rationale
above.

**`PolicyChunking.note_outcome()`** (`policy_chunking.py:1860-1915`) -- thread the raw
outcome through to the one call site that currently only passes `var`:

```python
def note_outcome(self, outcome_signal: float) -> List[ChunkedPrimitive]:
    ...
    for chunk in self.library.all_chunks():
        var = variances.get(chunk.key)
        if var is not None and self._was_executed(chunk):
            self.library.note_real_execution(
                chunk.key, var, outcome_signal=float(outcome_signal)   # NEW kwarg
            )
    ...
```

**`PolicyChunking._attempt_reacquisition()`** (`policy_chunking.py:1917-1956`) -- this
is the actual gate fix:

```python
def _attempt_reacquisition(
    self, variances: Dict[Tuple[int, ...], float]
) -> List[ChunkedPrimitive]:
    c = self.config
    if not (c.use_chunk_maintenance and c.use_chunk_dissolution_retention):
        return []
    bar = c.reacquisition_min_repetitions
    baseline = _mean(self.accumulator._outcome_history)
    revived: List[ChunkedPrimitive] = []
    for chunk in self.library.dormant_chunks():
        if chunk.reacquisition_repetitions < bar:
            continue
        if c.use_reacquisition_window_isolation:                       # NEW branch
            window = chunk.reacquisition_outcomes
            if len(window) < 2:
                # Numerical-stability floor, not a second bar: _variance()
                # returns 0.0 (not "undefined") below n=2, which would let a
                # single post-dissolution sample trivially clear the variance
                # gate on bar==1 settings. Mirrors the "None means no evidence"
                # convention used by marginal_return_at_ceiling() /
                # marginal_return_at_depth_ceiling() elsewhere in this module.
                continue
            var = _variance(window)
            mu = _mean(window)
        else:
            var = variances.get(chunk.key)
            if var is None:
                continue
            mu = _mean(self.accumulator._tally.get(chunk.key, ()))
        if var >= c.variance_low:
            continue
        if mu <= baseline + c.evaluative_margin:
            continue
        if self.library.revive(chunk.key, value_tag=mu):
            revived.append(chunk)
    return revived
```

Note the `len(window) < 2` floor is a deliberate, narrow deviation from "the window and
`reacquisition_repetitions` always agree" (they are populated at the same call site, so
in the ordinary case `len(window) == reacquisition_repetitions` once both are
non-empty): at `bar = 1` (possible when `f_reacq` is small and `R_min` is small) the
`bar` check alone would let a single post-dissolution sample -- for which `_variance`
is definitionally `0.0` -- trivially pass the variance gate with zero evidence of
consistency. The `< 2` floor costs at most one extra trial of latency and only matters
at the low end of `bar`; it should be pinned by its own contract case
(`bar == 1, one sample -> refused; two samples -> judged`) when this lands.

`variances` remains a required parameter of `_attempt_reacquisition` because the
non-isolated (`False`) branch still needs it -- no signature change there.

### 3e. Backward-compat statement

With `use_reacquisition_window_isolation` at its default (`False`):

- `_attempt_reacquisition()` takes the untouched `else` branch, reading
  `variances.get(chunk.key)` / `accumulator._tally[chunk.key]` exactly as today --
  **bit-identical output**.
- `reacquisition_outcomes` is still populated (see 3c's rationale for why: matching the
  existing "written under the enclosing flag, read under the sub-flag" convention), but
  since nothing reads it on this path, this is memory bookkeeping only and produces no
  observable difference in any manifest field, diagnostic counter, or chunk state
  transition.
- `note_real_execution()`'s new `outcome_signal` parameter defaults to `None` and every
  existing call site (module-internal and both direct calls in the contract test file)
  either passes it explicitly (the one internal site, updated as part of this fix) or
  omits it (the two test call sites), so no caller needs to change.
- The two switches gating this whole code path
  (`use_chunk_maintenance`, `use_chunk_dissolution_retention`) are BOTH already default
  `False`, so **every existing experiment with default config is completely unaffected
  regardless of this change** -- `_attempt_reacquisition` returns `[]` immediately on
  its first line whenever either is off, before any of the touched code runs.
- No existing default value changes. No existing field is removed or renamed.

### 3f. Phased-training note

Not applicable. `ChunkAccumulator` / `ChunkLibrary` are "pure-arithmetic, no learned
parameters, no `nn.Module` inheritance" (module docstring, `policy_chunking.py:950`).
There is no encoder head and no gradient-based training anywhere in this fix; P0/P1/P2
phasing as used by the V3-EXQ-829 driver is a *measurement* protocol (acquire, dissolve,
re-acquire), not a training-phase gate in the ARC-071/ML sense.

### 3g. ML/AI engineering notes (Layer 7)

- **Engineering problem**: this is a **windowed-statistic segmentation** problem --
  computing a "how consistent has recent behaviour been" statistic over a sliding
  window that must not straddle a regime-change boundary the window itself cannot see.
  The general ML/engineering parallel is a **changepoint-aware moving average /
  variance estimator**: a plain FIFO or exponential window silently blends pre- and
  post-changepoint data for a duration proportional to the window length, exactly the
  failure mode measured here (`r_reacq / W ~ 0.9`).
- **Technique adopted**: the fix is the simplest member of that family -- a **hard
  reset of the window at the known changepoint** (dissolution), rather than a
  changepoint-detection algorithm (CUSUM, Page-Hinkley, Bayesian online changepoint
  detection). This is the right level of complexity here because REE already KNOWS the
  changepoint exactly (it is the `_mark_dissolved()` call), so there is nothing to
  *detect* -- adopting a general changepoint detector would be importing complexity to
  solve a problem the substrate has already solved by having an explicit state machine.
  This is the same "REE encoders are 2-3 layer MLPs, don't import ImageNet-scale
  machinery" discipline applied to statistics instead of network architecture.
- **Numerical consideration incorporated**: the `len(window) < 2` floor (3d above)
  defends against the standard small-sample variance-estimator failure mode --
  `_variance` (population variance, two-pass mean, this module's existing helper) is
  identically `0.0` for `n < 2`, which is "no evidence" masquerading as "perfect
  consistency" if not guarded. This is the same class of bug the module's own
  `marginal_return_at_ceiling()` / `marginal_return_at_depth_ceiling()` already guard
  against by returning `None` (not `0.0`) when nothing is yet judgeable; this fix
  applies the identical judgeability discipline to the reacquisition gate rather than
  inventing a new convention.
- **What NOT adopted**: no EMA / exponential-decay smoothing was considered for the
  post-dissolution window. An EMA has the same straddling problem as a FIFO window
  (old high-variance mass decays but never fully drops out), so it would not close the
  measured `r_reacq/W` scaling defect -- a hard reset is the only member of this family
  that actually removes pre-changepoint contamination rather than merely down-weighting
  it.

### MECH-094 (`hypothesis_tag`) applicability

**Does not apply**, and this should be stated explicitly rather than left implicit. The
entire fix operates on `ChunkLibrary.note_real_execution()`'s existing DISSOLVED
branch, which is reached **only** from `PolicyChunking.note_outcome()` -- the
MECH-094-strict forward path -- and specifically only for chunks that were `_was_executed`
this trial, i.e. **real, committed, waking action executions**, exactly the same
provenance MECH-323's original formation gate requires. Nothing in this fix touches
`ChunkAccumulator.record_replay_sequence()` (the MECH-322 carve-out, the only path that
accepts `hypothesis_tag=True`), and replay-origin chunks remain explicitly excluded
from revival at all (`ChunkedPrimitive.is_dormant` returns `False` when
`replay_origin` is `True`, unchanged by this fix -- see
`policy_chunking.py:536-544`). This is committed-trajectory maintenance bookkeeping,
not simulation, replay, or any content written to memory during a non-waking state, so
MECH-094's `hypothesis_tag=True` carve-out requirement does not apply to the new
`reacquisition_outcomes` field or to anything that populates it.

---

## What this does NOT fix / is out of scope

- The two other MECH-324 relapse falsifiers (renewal, resurgence) remain
  substrate-blocked for the reasons already recorded in the module docstring
  (`policy_chunking.py:287-290`, `:364-375`) and in `claims.yaml`'s MECH-324
  `implementation_note` -- this fix does not touch context-scoping (`initiation_set`)
  or cross-candidate dissolution coupling, and does not change that status.
- `reacquisition_repetition_factor = 0.25` remains an uncalibrated engineering default
  (unchanged by this fix, and not addressed by it -- this is a data-flow correctness
  fix, not a calibration exercise).
- The CRYSTALLISED/DISSOLVING hysteresis logic in `note_real_execution` (the branches
  above the DISSOLVED one) is **unchanged** and continues reading the accumulator's
  whole-lifetime windowed variance, which is the biologically and statistically correct
  question for "has this chunk's behaviour become inconsistent" -- only the DISSOLVED
  (reacquisition) branch had the wrong window.
- No claims.yaml disposition change is proposed here (that is governance work, Step 7
  of `/implement-substrate`, and requires the code to actually be implemented and
  validated first).

## Validation (Step 8, not performed by this design pass)

A successor to V3-EXQ-829, re-running the same 6-seeds x 11-arms grid (or a reduced
version of it) with `use_reacquisition_window_isolation` added as a THIRD ablation axis
(isolation ON vs OFF, crossed with the existing `f_reacq` sweep and `W in {30, 100}`),
would be the natural validation experiment: acceptance criterion is `median_r_reacq`
scaling with `f_reacq` (Spearman rho >= the pre-registered `SCALING_RHO_FLOOR = 0.8`)
under isolation ON, reproducing the current flat/FAIL signature under isolation OFF as
an in-run negative control. Per this task's constraints, queuing that experiment is
explicitly Step 8 / `/queue-experiment` work and is NOT performed here.

---

## HARD CONSTRAINT NOTE (historical -- Steps 1-3 pass)

This document was originally produced by a headless, non-interactive
`/implement-substrate` design pass (IGW-20260731-196). Per `scripts/igw_routine_tick.py`
`REQUIRES_HUMAN_SKILLS = {"/implement-substrate"}`, that pass stopped at Steps 1-3
(gather spec, map codebase, design) -- no `ree_core/` code was written, no smoke test
was run, no experiment was queued -- and reported the plan above for human review.

**Implementation (Step 4 onward) subsequently confirmed and completed 2026-07-31**
in the same session, after explicit user confirmation ("yes implement it"): the code
changes in Section 3d landed verbatim in `ree_core/policy/policy_chunking.py` /
`ree_core/utils/config.py` / `ree_core/agent.py` (ree-v3 `7747a01c94`), the 5 contract
tests described in Section "Validation" were written and confirmed green (plus the
full `tests/contracts` suite, 3085 passed locally), and validation experiment
V3-EXQ-829a was queued (supersedes V3-EXQ-829, not yet run). See ree-v3/CLAUDE.md's
MECH-324 reacquisition-window-isolation entry for the authoritative implementation
record, and `claims.yaml`'s MECH-324 `implementation_note` for the claims-governance
note.
