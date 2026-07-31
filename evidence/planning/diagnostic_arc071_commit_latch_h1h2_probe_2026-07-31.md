# Diagnostic — ARC-071 commit-latch persistence H1/H2 probe

**qid:** `arc071-commit-latch-persistence` (hypothesis_space_registry.v1.json)
**Parent:** `failure_autopsy_V3-EXQ-841_2026-07-31` Finding B, `fanout_recommendation`
**Session:** `quirky-mayer-ee5ad2`
**Generated:** 2026-07-31T23:46:08Z
**Verdict: H1 (ree_core wiring defect) CONFIRMED. H2 (experiment readout artifact) REFUTED.**

## Method

Rather than reproducing the full ~8600-step formation phase, this probe tests the
persistence mechanism directly: `agent.policy_chunking.selectable_chunks` was
monkeypatched to always return one guaranteed-selectable, already-crystallised
3-step chunk `(0, 1, 2)`, and `agent.e3._running_variance` was forced to `-1.0`
(guaranteed below any `commit_threshold`) so a commit fires immediately and stays
eligible every tick. `agent.select_action` was wrapped to record, for every tick
of an 80-step episode: whether E3 ticked this step (`ticks["e3_tick"]`, the exact
parameter `select_action` receives), `agent._committed_step_idx` before/after,
and the python `id()` + `chunk_sequence` of both `e3._committed_trajectory`
(F-driven handle) and `e3._persistent_committed_trajectory` (SD-084 handle)
before/after — plus the experiment's own `_committed_chunk_state()` read at the
same instant, to directly compare the readout against ground truth. Run on
seeds 101 and 505, `A_HIER_S2` flags (`chunk_max_size=2`), per the
`fanout_recommendation`'s suggested probe. Script:
`/private/tmp/.../scratchpad/h1h2_probe.py` (ad hoc diagnostic, not queued as a
formal EXQ per CLAUDE.md judgement — produces a clear, decisive result directly).

## Result

| | seed 101 | seed 505 |
|---|---|---|
| ticks logged | 80 | 80 |
| E3 ticks fired | 8 | 10 |
| max `_committed_step_idx` observed, ANY tick | **1** | **1** |
| ticks with non-null persistent handle | 80/80 | 80/80 |
| distinct persistent-handle object ids seen | 9 | 11 |
| distinct F-driven `_committed_trajectory` ids (post-tick, non-null) | 9 | 11 |
| readout (`_committed_chunk_state()`) vs direct-attribute-read mismatches | 0 | 0* |

\* One apparent mismatch at seed 505 tick 0 is an artifact of this probe's own
crude same-line summary heuristic (pre-commit tick, beta not yet elevated), not
a mismatch in `_committed_chunk_state()` itself — its raw output at every one of
160 ticks across both seeds matches the real underlying state exactly.

Representative trace (seed 101, first 15 ticks; `pt` = persistent handle
sequence, `ct` = F-driven handle sequence, `exp` = experiment's own read
function output):

```
tick e3t pre_idx post_idx  ct(pre->post)              pt(pre->post)              exp(seq,idx)
   0   F       0        1  None->(0,1,2)               None->(0,1,2)             ((0,1,2),1)
   1   F       1        1  None->None                  (0,1,2)->(0,1,2)          ((0,1,2),1)
   2   F       1        1  None->None                  (0,1,2)->(0,1,2)          ((0,1,2),1)
 ...   F       1        1  None->None                  (0,1,2)->(0,1,2)          ((0,1,2),1)
   8   T       1        1  None->(0,1,2)  [NEW OBJECT]  (0,1,2)->(0,1,2) [NEW OBJECT]  ((0,1,2),1)
```

## Interpretation

1. **`_committed_step_idx` never advances past 1**, in either seed, across 80
   ticks and 8-10 full E3 re-deliberation cycles, even though the forced chunk
   has 3 steps and is re-selected as the ONLY candidate every single time E3
   ticks. This is not a dose/formation artefact — the mechanism structurally
   cannot advance the index past its first post-commit value.
2. **The SD-084 persistent handle (`_persistent_committed_trajectory`) correctly
   holds the SAME chunk_sequence across every non-E3-tick step** (`pt` column:
   `(0,1,2)->(0,1,2)`, never reset) — the *state* genuinely persists where it is
   supposed to.
3. **But on every single E3 tick (8-10 per seed), a BRAND NEW trajectory object
   is created and installed** (distinct `id()` at every one of the 8-10 E3
   ticks, despite selecting the identical candidate sequence every time) — E3
   unconditionally re-deliberates and re-commits from scratch on every E3 tick;
   there is no check for "already committed to this exact program, horizon not
   reached, skip re-selection."
4. **Between E3 ticks, the index-advance path never engages either**, for a
   distinct, second reason: `agent.py`'s "between-E3-tick: step through
   committed trajectory" branch (`select_action`, the block starting
   `if not ticks["e3_tick"] and self._last_action is not None:`) reads
   `_step_traj = self.e3._committed_trajectory or self.e3._closure_committed_trajectory`
   — and `e3._committed_trajectory` (the F-driven handle) is unconditionally
   cleared to `None` at the end of **every** tick by
   `E3Selector.post_action_update` (`ree_core/predictors/e3_selector.py:3910`,
   `self._committed_trajectory = None`, unconditional, by design — see the
   SD-084 comment at `agent.py:5522-5539`: "the F-driven one dies at the end of
   the tick, the persistent one lives until REEAgent reaps it"). The
   between-tick branch **never consults `e3._persistent_committed_trajectory`**
   — unlike the MECH-321 mid-execution decomposition hook a few dozen lines
   away (`agent.py:5584-5588`), which DOES fall back to the persistent handle
   when `use_persistent_committed_program_handle` is enabled. So `_step_traj`
   is always `None` on non-E3-tick steps, the branch falls to
   `action = self._last_action` (repeat the previous physical action, no chunk
   bookkeeping), and the increment at `agent.py:5981`
   (`self._committed_step_idx += 1`) — the ONLY site that advances the index —
   is simply never reached.
5. **The readout (`_committed_chunk_state()`) faithfully reports this real,
   broken state at every tick tested (0 genuine mismatches across 160
   ticks).** H2 is refuted: the experiment's read path is not misreading a
   genuinely-persisting commitment — there is no genuinely multi-step-persisting
   commitment to misread. The pinned-at-1 finding in V3-EXQ-841 is real
   substrate behaviour, not a measurement artefact.

## Root cause and exact fix (NOT applied this session — see Status)

Two independent, compounding wiring gaps, both in the already-designed-for-this
SD-084 persistence machinery:

**(a) `agent.py` between-E3-tick stepping branch never consults the persistent
handle.** `use_persistent_committed_program_handle` (default `False`,
`ree_core/utils/config.py:4062`) already exists and is already consulted by the
MECH-321 hook (`agent.py:5584-5588`) — the between-tick stepping branch
(`agent.py:5965-5987`) was never updated to do the same. Minimal fix, mirroring
the existing MECH-321 pattern exactly:

```python
_step_traj = (
    self.e3._committed_trajectory
    or self.e3._closure_committed_trajectory
)
if _step_traj is None and getattr(
    self.config, "use_persistent_committed_program_handle", False
):
    _step_traj = self.e3._persistent_committed_trajectory
if self.beta_gate.is_elevated and _step_traj is not None:
    ...  # unchanged
```

Bit-identical for every existing run with the flag off (matches the codebase's
own default-off doctrine stated at the MECH-321 site).

**(b) The chunk-injection arms never enable the flag.**
`experiments/_lib/baselines/arc071_chunking.py`'s `off_arm_flags()` /
chunking-on flags, and `V3-EXQ-841`'s own `_arm_flags()`, never set
`use_persistent_committed_program_handle=True`. Fix (a) alone changes nothing
for any existing chunk-injection run unless this is also turned on for the
chunking arms. This second change touches shared `_lib/**` baseline
infrastructure that is bound into `substrate_hash` (per the module's own
docstring) — flipping a default-off flag on for chunking arms changes that
fingerprint for every `arc071_chunking` consumer, including the 810a mint, and
needs a governance-aware review of blast radius, not a same-session drive-by
edit.

**Also worth checking, not yet diagnosed here:** whether E3 SHOULD skip
re-selection entirely on an E3 tick when already committed to an unexpired
program (item 3 above) — that is a second, independent behavioural question
(does the substrate need a "still-committed, don't re-deliberate" short-circuit
inside the full E3-tick branch itself, on top of fix (a)/(b) above) that this
probe surfaces but does not resolve. Flagging it for whoever picks up the
implementation rather than asserting a fix.

## Status

**NOT applied this session.** `ree-v3/ree_core/agent.py` is under an active
`TASK_CLAIMS.json` claim by session `elated-germain-9aff71`
("SD-036 merge integration branch", claimed 2026-07-31T22:37:07Z) at the time
this diagnosis was written — editing it now would collide with an in-progress
merge in the shared checkout. This is also, independently, a two-part fix
spanning `ree_core/agent.py` (behavioural change) and a `_lib/**` baseline
fingerprint change (`experiments/_lib/baselines/arc071_chunking.py`) — properly
`/implement-substrate` scoped work, not a same-session drive-by patch.

Recorded as a follow-on chip (title: fix ARC-071 commit-latch persistence,
H1 confirmed) rather than implemented directly, per CLAUDE.md Session Land
Protocol step 6 (chip-everything-else) and the claim-contention handling in the
Concurrency Rules section (do not implement against a file another active
session owns).

`substrate_queue.json` entry `arc071_chunk_commit_latch_persistence` and
`hypothesis_space_registry.v1.json` qid `arc071-commit-latch-persistence`
updated to reflect this diagnosis in the same commit as this file.
