# Diagnostic — ARC-071/MECH-090 E3 re-selection cadence vs committed-chunk horizon

**qid:** `arc071_e3_reselection_on_committed_program` (substrate_queue.json)
**Parent:** `arc071_chunk_commit_latch_persistence`'s `implementation_note.fix_c_decision` (deferred fix (c) question), itself descended from `failure_autopsy_V3-EXQ-841_2026-07-31` and `diagnostic_arc071_commit_latch_h1h2_probe_2026-07-31.md`
**Session:** `frosty-satoshi-2e7cbc`
**Generated:** 2026-08-01T13:45:38Z
**Verdict: REAL, non-trivial defect confirmed at chunk sizes already in practical use (chunk_max_size=5, one of V3-EXQ-841's three tested dose arms) and growing sharply at larger sizes (8, 15). NOT aleatoric. `complex (probe-gated)` -> `complicated (buildable)`, with a named fix.**

## Method

Unlike the sibling H1/H2 probe (which forced a guaranteed-selectable chunk and a
permanent commit condition to stress-test index *persistence*), this question is
about the ADAPTIVE E3 heartbeat cadence, which a forced/monkeypatched scenario
cannot exercise. This probe drives a REAL rollout: the canonical
`experiments/_lib/baselines/arc071_chunking.py` env/agent builders (the same
`CausalGridWorldV2` config with `num_hazards=2` that V3-EXQ-841 and the 810
lineage use, load-bearing per that module's own docstring because
`harm_signal < 0` is the sole trigger for MECH-091's `clock.phase_reset()`), the
canonical `experiments/_harness.StepHarness` loop, a real agent with
`use_policy_chunking=True` + the full V3-EXQ-841 `CHUNKING_ON_ARMS` flag set
(`use_chunk_maintenance`, `use_chunk_proposal_injection`,
`use_chunk_all_position_credit`) plus the just-landed
`use_persistent_committed_program_handle=True` (ree-v3 main `278599a`) so the
already-fixed persistence mechanism is in effect while this separate cadence
question is tested.

`ree_core/heartbeat/clock.py`'s `update_e3_rate_from_beta` (read in full before
writing probe code, lines ~201-220) was confirmed to interpolate
`e3_steps_per_tick` linearly between `beta_rate_max_steps=20` (low arousal) and
`beta_rate_min_steps=5` (high arousal) as `beta_mag = z_beta.norm()` sweeps
`[0, 1/beta_magnitude_scale]` (`beta_magnitude_scale=1.0` by default), clamped to
`[5, 20]`.

**A second, more consequential mechanism was found while reading the wiring,
and is central to the result below**: `ree_core/agent.py`'s residue-update path
calls `self.clock.phase_reset()` unconditionally on every `harm_signal < 0` step
(MECH-091, "harm is salient -> phase reset") — this forces an E3 tick on the
very NEXT `clock.advance()` regardless of the periodic `e3_steps_per_tick`
counter. `arc071_chunking.py`'s own docstring already flags this as load-bearing
for a DIFFERENT reason (810's 24-step, hazard-free episode never exercised it,
making its E3 tick perfectly periodic and its accumulator inert). For this
probe it means the *effective* E3-tick cadence in a real hazard-exposed episode
is set by whichever fires first — the adaptive periodic counter, or the next
harm event — not by the periodic counter alone.

**Chunk formation requires the trial-boundary outcome report.** An early version
of this probe (fixed mid-session, see "False start" below) omitted
`agent.note_chunk_outcome(ep_reward)` at episode boundaries — the call
`arc071_chunking.py`'s own canonical `run_cell()` makes and that chunk
formation/crystallisation depends on. Without it, `chunk_lib_n_crystallised`
stayed at 0 for the full 120-episode formation schedule and every "committed"
trajectory observed was an ordinary CEM candidate (`metadata=None` or
`support_preserving_cem_injected`), never an `arc071_chunk`-sourced one — i.e.
the mechanism under test never actually engaged. Confirmed via a dedicated
debug script (`debug_chunk_source.py`) run both ways on identical
config/seed/schedule: `chunk_lib_n_crystallised=0` without the call,
`chunk_lib_n_crystallised=12` (15 formed) with it, `arc071_chunk`-sourced
commitments becoming the dominant source (2877 vs 768 ordinary) by episode 120.

**Full run**, after the fix: `N_EPISODES=120, STEPS_PER_EPISODE=72` (`base.N_EPISODES`/
`base.STEPS_PER_EPISODE` — the exact 810a-proven formation schedule V3-EXQ-841
itself uses, not a truncated schedule), `chunk_max_size` in `{2, 3, 5, 8, 15}`
(the three values V3-EXQ-841 tested, plus two at/above `beta_rate_min_steps=5`
per the brief), seeds `{101, 202}`. `chunk_ceiling_hard_max` was raised to
`max(12, chunk_max_size)` for the `chunk_max_size=15` cells only (the
`PolicyChunkingConfig` default hard cap is 12 and `validate()` rejects a
`max_chunk_size` above it — bit-identical override for `chunk_max_size<=12`).

`agent.select_action` was instrumented via `StepHooks` (`on_sense` for the
PRE-select_action snapshot — after `clock.advance()` sets `ticks['e3_tick']` for
this step but before `select_action` runs; `on_action` for the POST snapshot),
logging per step: `ticks['e3_tick']`, the LIVE `agent.clock.e3_steps_per_tick`,
`z_beta.norm()`, `agent.beta_gate.is_elevated`, `agent._committed_step_idx`
before/after, and the `id()` + chunk length (`metadata['chunk_sequence']`,
falling back to `traj.actions.shape[1]`) of `agent.e3._persistent_committed_trajectory`
before/after. Classification per E3 tick, in priority order: `fresh_commit` (no
prior commitment), `no_change` (same object retained — did not occur, 0/12952
across the whole run), `non_chunk_reselect` (a prior commitment existed but
carried no `arc071_chunk` metadata — not classifiable against a chunk horizon,
kept SEPARATE rather than silently folded into "reached horizon", which was the
exact bug in the pre-fix version of this script), `premature_reselection`
(`pre_committed_step_idx < pre_chunk_length - 1`), else
`natural_completion_reselect`.

Script: `/private/tmp/.../scratchpad/e3_reselection_probe.py` (ad hoc
diagnostic, not queued as a formal EXQ, per CLAUDE.md judgement — mirrors the
sibling H1/H2 probe's convention).

**False start (documented for the next reader, not swept):** the first full
sweep (`n_episodes=40`, chosen to keep to "a few thousand steps" per the brief)
ran to completion (10 cells, 1698s) with `frac_premature_of_committed_decisions
= 0.0` in EVERY cell — a result that looked like a clean "aleatoric, never
happens" verdict. It was not: `pre_persistent_chunk_len` was `None` for 100% of
the 5286 "committed_decisions" in that run (verified by direct inspection of
the raw classified records), meaning every one of those events was silently
defaulting into "natural completion" for lack of chunk metadata to check against
— not because chunks had genuinely run to horizon. Root cause: 40 episodes is
below the formation threshold this substrate needs even fixed, and (found only
via the dedicated debug script) `note_chunk_outcome` was never being called at
all. **A near-miss worth flagging generally**: an all-zero result that looks
like exactly the finding you were expecting is the case that most wants a
"why is the denominator what it is" check before being trusted.

## Result

53,063 total steps, 12,952 E3 ticks, 8,682 chunk-committed decisions (E3 ticks
where a prior `arc071_chunk`-sourced commitment existed and could be checked
against its own horizon) across the full 10-cell sweep.

| chunk_max_size | seed | n_steps | E3 ticks | fresh | non-chunk | natural | **premature** | committed_dec | frac premature | z_beta [min/max] | live rate [min/max] |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 2 | 101 | 4889 | 1201 | 3 | 568 | 630 | **0** | 630 | 0.000 | 0.202/0.678 | 9/16 |
| 2 | 202 | 2900 | 1461 | 2 | 236 | 1223 | **0** | 1223 | 0.000 | 0.233/0.781 | 8/16 |
| 3 | 101 | 4234 | 1277 | 2 | 532 | 743 | **0** | 743 | 0.000 | 0.202/0.679 | 9/16 |
| 3 | 202 | 2936 | 1471 | 5 | 86 | 1380 | **0** | 1380 | 0.000 | 0.216/0.721 | 9/16 |
| 5 | 101 | 8521 | 1231 | 3 | 1228 | 0 | **0** | 0 | n/a (no chunk commits this seed) | 0.189/0.633 | 10/17 |
| 5 | 202 | 8080 | 1214 | 2 | 273 | 593 | **346** | 939 | 0.368 | 0.192/0.643 | 10/17 |
| 8 | 101 | 8400 | 1245 | 1 | 112 | 748 | **384** | 1132 | 0.339 | 0.216/0.726 | 9/16 |
| 8 | 202 | 2763 | 1258 | 2 | 1032 | 46 | **178** | 224 | 0.795 | 0.191/0.644 | 10/17 |
| 15 | 101 | 5718 | 1265 | 3 | 76 | 362 | **824** | 1186 | 0.695 | 0.223/0.749 | 8/16 |
| 15 | 202 | 4622 | 1329 | 1 | 103 | 721 | **504** | 1225 | 0.411 | 0.221/0.741 | 8/16 |

**Aggregate by chunk_max_size (both seeds combined):**

| chunk_max_size | premature | natural | committed_decisions | **frac premature** |
|---:|---:|---:|---:|---:|
| 2 | 0 | 1853 | 1853 | **0.000** |
| 3 | 0 | 2123 | 2123 | **0.000** |
| 5 | 346 | 593 | 939 | **0.368** |
| 8 | 562 | 794 | 1356 | **0.414** |
| 15 | 1328 | 1083 | 2411 | **0.551** |

**Live `e3_steps_per_tick` distribution across the whole run**: min 8, max 17 —
`beta_rate_min_steps=5` was NEVER reached in 53,063 steps of real hazard
exposure (z_beta norm ranged 0.189-0.781; recall the interpolation clamps at
`beta_mag>=1.0`, and observed magnitudes topped out under 0.8). The periodic
rate alone therefore never approached the substrate's own documented worst
case. **Premature re-selection at chunk_max_size 5/8/15 is happening at a
"mild arousal, steady-state ~8-10-step cadence" regime, not only at the
adaptive floor** — see Interpretation.

**Representative trace** (chunk_max_size=15, seed=101; a length-12 crystallised
chunk, committed and re-committed to across two full episodes, cut short at the
same point on 8 consecutive E3 ticks):

```
step gap live_rate beta_elev pre_idx post_idx pre_len  class
   1  -23        14 True         1        1     12    premature_reselection  (episode boundary; gap stat not meaningful here)
  10    9         9 True         9        1     12    premature_reselection
  18    8         8 True         8        1     12    premature_reselection
  26    8         8 True         8        1     12    premature_reselection
  34    8         8 True         8        1     12    premature_reselection
  42    8         8 True         8        1     12    premature_reselection
  50    8         8 True         8        1     12    premature_reselection
  58    8         8 True         8        1     12    premature_reselection
  66    8         8 True         8        1     12    premature_reselection
   3  -63        11 True         3        1     12    premature_reselection  (next episode)
  12    9         8 True         9        1     12    premature_reselection
  20    8         8 True         8        1     12    premature_reselection
  28    8         8 True         8        1     12    premature_reselection
  36    8         8 True         8        1     12    premature_reselection
```

Every one of these ticks installs a distinct object (`id()` differs tick to
tick, consistent with the sibling H1/H2 probe's finding that E3 unconditionally
re-deliberates and re-installs on every tick with no "already committed, skip
re-selection" check). The live `e3_steps_per_tick` stabilises at 8 — below the
chunk's own horizon of 12 — so the periodic component of the cadence alone is
enough to guarantee this chunk can never run to completion; `post_idx=1` on
every row shows the freshly-installed commitment is itself immediately stepped
once before the next between-tick interval, then cut again at the same ~8-step
mark.

**Caveat on the `gap`/"early_fire" statistic** (does not affect the premature
classification, which depends only on `pre_committed_step_idx` vs
`pre_persistent_chunk_len`, not on `gap`): `step` in these records is
per-episode (`StepHarness.reset()` zeroes `_step_count`), so a `gap` computed
naively across an episode boundary is negative/meaningless (see `step=1,
gap=-23` above). The `n_early_fire_gap_lt_live_rate` summary field inherits this
noise and should be read as directional, not exact — most (though not
episode-boundary-corrected) E3 ticks in every cell fired at a shorter gap than
the live periodic rate would predict, consistent with MECH-091 `phase_reset()`
(harm-triggered) rather than the periodic counter being the dominant tick
source in this hazard-rich env.

**Caveat on cross-cell seeding**: `torch.manual_seed(0)` is called once at
process start; `CausalGridWorldV2(seed=...)` independently seeds the
environment, but the agent's own stochastic draws (CEM sampling, action
selection) run on the global torch RNG, whose state carries over cumulatively
across the 10 sequential cells rather than being independently reset per cell.
This is why `chunk_max_size=5, seed=101` registered zero chunk commitments in
the full run despite the standalone smoke test (same nominal seed, isolated
process) registering 117 premature / 244 natural at 45 episodes — the two runs'
agents experienced different torch RNG streams despite the same env seed. Not a
defect in the finding (every classified event is still a real, correctly
attributed observation), but a reason not to over-read any single seed's number
in isolation; the aggregate-by-chunk_max_size table combines both seeds for
exactly this reason, and the qualitative pattern (0 at 2/3, present and growing
at 5/8/15) is what the write-up leans on, not any single cell's fraction.

## Interpretation

1. **The effect is real, not aleatoric, and is not confined to the untested
   large sizes.** `chunk_max_size=5` is one of V3-EXQ-841's own three tested
   dose arms (`A_HIER_S5`, alongside `A_HIER_S2=2` and `A_HIER_S3=3`) — the
   exact substrate configuration currently in practical use. It shows a
   non-trivial 36.8% premature-reselection rate in the one seed that
   registered any chunk commitments at all. `chunk_max_size=2` and `=3` (the
   other two tested dose arms) show a clean, decisive 0/1853 and 0/2123 —
   genuinely never occurs at those sizes, across two full 120-episode formation
   runs each.
2. **The mechanism is cadence vs. chunk-length, not adaptive-floor vs.
   chunk-length.** The task's framing (and the substrate_queue.json entry's own
   `implementation_hint`) centred on whether `e3_steps_per_tick` could shrink to
   `beta_rate_min_steps=5` under elevated z_beta. It never did — the observed
   live-rate floor across the entire 53k-step run was 8, well above 5, because
   observed `z_beta` magnitudes (up to 0.78) never reached the
   `beta_magnitude_scale`-implied saturation point (1.0). **The dominant
   trigger is instead MECH-091's unconditional `clock.phase_reset()` on every
   `harm_signal < 0` step** (confirmed by reading `agent.py`'s residue-update
   path, and consistent with `arc071_chunking.py`'s own docstring naming this
   the reason `num_hazards>0` is load-bearing for the OFF arm too) — this
   forces an E3 tick independent of the periodic counter, and even the
   *periodic* component alone (min observed 8) already sits below
   `chunk_max_size` for the 8 and 15 arms, and below the 12-step chunk length
   that crystallised and was repeatedly interrupted in the representative
   trace. **A chunk longer than roughly the steady-state cadence (~8-10 steps
   in this env) structurally cannot complete before the next re-deliberation**,
   regardless of whether the adaptive floor is ever touched.
3. **This refines rather than confirms the substrate_queue.json entry's own
   framing** — it names MECH-093 (the adaptive floor) as the mechanism to test;
   the data says MECH-091 (salient-event phase reset) plus the ordinary
   mid-range periodic rate are jointly sufficient, and the extreme adaptive
   floor is not actually necessary for the effect to bite at practically-used
   chunk sizes. The `implementation_hint`'s proposed fix (an "unexpired
   commitment, skip re-selection" short-circuit in the E3-tick branch) is
   unaffected by this correction — it would address the symptom regardless of
   which of the two tick-cadence drivers dominates — but a future
   `/implement-substrate` session should know the MECH-091 phase-reset path is
   the one to reason about first, not primarily the MECH-093 interpolation.
4. **`chunk_max_size 2` and `3` are safe as currently used; `5` already carries
   real, non-negligible risk; `8`/`15` are substantially worse.** This is
   consistent with a simple horizon-vs-cadence account: at cadence ~8-10 steps,
   a 2- or 3-step chunk always finishes with room to spare; a 5-step chunk is
   close enough to the cadence that whether it survives depends on the
   realised inter-tick gap (hence the seed-dependent 0.0 vs 0.368 split); 8 and
   15-step chunks are reliably longer than the cadence and get interrupted most
   of the time.

## Classification (work-graph debt vocabulary)

Per `REE_assembly/docs/architecture/work_graph_debt_vocabulary.md`: this
started as `complex (probe-gated)` (substrate_queue.json's own prior
classification) — a reducible unknown, answerable by a spike. This probe IS
that spike, and it returns a decisive, non-aleatoric answer: **`complicated
(buildable)`**, with the fix already named in the parent entry's own
`implementation_hint` (not re-derived here, and NOT implemented in this
session — diagnosis only, per the task brief and the same discipline the
sibling H1/H2 probe used when `agent.py` was under a contended claim).

**Named follow-on fix** (for a future `/implement-substrate` session, not this
one): an "already committed to this exact unexpired program, skip
re-selection" short-circuit inside `select_action`'s E3-tick branch — checking,
before falling through to full E3 deliberation, whether
`e3._persistent_committed_trajectory` is non-None, still `arc071_chunk`-sourced,
and `_committed_step_idx < chunk_length - 1`, and if so holding the existing
commitment (or at minimum not force-installing a fresh object for an
identically-reselected candidate). This is a materially larger change to E3's
core re-deliberation loop than fix (a) (mirroring an existing fallback
pattern) — it needs its own design review of interaction surface with MECH-091
(which SHOULD still be able to interrupt on a genuine acute threat spike; this
short-circuit must not swallow that release) and with the natural-commit
latch-hold machinery adjacent to it in `agent.py`. Scoping that review is out
of scope for this diagnostic.

## Status

**NOT implemented this session** — diagnosis only, per the task brief.
`substrate_queue.json` entry `arc071_e3_reselection_on_committed_program`
updated in the same commit as this file: `status` ->
`diagnosed_needs_fix`, `node_class` -> `complicated (buildable)`, plus a
`diagnosis` block naming this file, the finding, and the recommended next step.
No other `substrate_queue.json` entry touched.

Probe script (not committed, ad hoc scratchpad per CLAUDE.md judgement):
`/private/tmp/claude-501/-Users-dgolden-REE-Working--claude-worktrees-frosty-satoshi-2e7cbc/d8d49dc9-9379-4f7d-a8e8-7547ad72ad98/scratchpad/e3_reselection_probe.py`,
with a supporting debug script
`debug_chunk_source.py` in the same directory (kept locally for anyone
retracing this probe's false start; not part of the tracked repo).
