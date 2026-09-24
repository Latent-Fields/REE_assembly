# MECH-287 four-arm invalidation factorial -- BLOCKED on an unregistered read-side flag

**Status: AWAITING USER REVIEW. Nothing was queued. No experiment script was written, no
`experiment_queue.json` entry was appended, and nothing was written to `claims.yaml` or
`experiment_proposals.v1.json`.**

- Session: `metaworker-science-20260924-orchb-mech287-invalidation-factorial`
- Campaign: `science-20260924-orchb-mech287-invalidation-factorial` (orchestrate-20260924-b)
- Chip: `chip-proposal-exp-0371` (EXP-0371 / MECH-287), pre-flight verdict AMBER
- Written: 2026-09-24T11:54:39Z
- Source refs: `ree-v3` `bbbef60c` (= `origin/main`), `REE_assembly` `b9c92ba7ae` (= `origin/master`)

## 1. Summary

The MECH-287 four-arm trigger-vs-accumulator dissociation factorial (the outstanding
V3-EXQ-476) **cannot produce a live behavioural DV using only the flags its own
pre-registration names.** With exactly the registered flag set, anchor invalidation is
behaviourally inert: the run would reproduce V3-EXQ-478's null by construction and would
satisfy MECH-287's FALSIFYING clause for a reason that has nothing to do with MECH-287.

Making the DV live requires turning on at least one flag that is **not** named in
MECH-287's `what_would_answer`, not named in its SUBSTRATE / INSTRUMENT REQUIREMENT, and
not named in the pre-flight. The available routes measure different things and attach the
evidence to different claim sets, so the choice is the user's, not this session's.

This finding is **additional to** the pre-flight's AMBER caveat, not a restatement of it.
The pre-flight's named change is confirmed correct and is necessary; it is not sufficient.

## 2. What the pre-flight got right (re-measured, not taken on report)

Every premise in the pre-flight's AMBER verdict was re-measured against the live tree and
holds:

- **All manipulated flags exist and are wired.** `ree-v3/ree_core/utils/config.py`:
  `use_event_segmenter` :3007, `use_invalidation_trigger` :3016, `use_anchor_sets` :3025,
  `use_per_region_vs` :3040, `use_staleness_accumulator` :3048, `use_mech284_hysteresis`
  :3058. (Pre-flight cited :3029/:3038/:3053/:3061/:3071 -- a uniform ~13-line offset;
  `config.py` has shifted since the pre-flight, all flags present, substance unchanged.)
- **No MECH-287 queue entry exists.** `grep MECH-287 ree-v3/experiment_queue.json` -> zero
  hits; the queue holds 3 items, max numeric id V3-EXQ-1087.
- **V3-EXQ-478's `freeze_recommit_count` is floor-pinned at 1** in all four recorded cells
  (`v3_exq_478_mech284_phase3_diagnostic_20260424T131455Z_v3.json`), with
  `anchor_reset_count` 63 and 31 in the ON arms. Outcome FAIL / `inconclusive`.
- **V3-EXQ-475 reproduces the catatonic-lock regime with genuine headroom.**
  `pag_n_releases` 6 / 5 / 5 and `pag_n_commits` 71 / 70 / 64 over seeds 0-2
  (~12x re-commits per release), `freeze_active_steps` 1000/1000 -- matching MECH-287's
  `functional_restatement` verbatim. Its env kwargs are recorded in the run's
  `..._episode_log.json` under `env_config` (the main manifest's `config` is null).
- **The named change is therefore correct**: the comparator must be built on V3-EXQ-475's
  config (`use_gabaergic_decay=True`, `use_pag_freeze_gate=True`, the SD-010/011/018/012/022
  stack, 60 warmup episodes), per `ree-v3/experiments/v3_exq_475_sd036_decay_unlocks_exq471.py`
  :65-183.

### 2b. Why V3-EXQ-478 was degenerate -- sharper than "no headroom"

Two mechanisms the pre-flight did not separate:

1. **478's `freeze_recommit_count` is not MECH-287's DV.** 478 counts
   "consecutive-repeat action-class runs of length >= 3" over the executed action sequence
   (`v3_exq_478_mech284_phase3_diagnostic.py` :43-47, :237). Its manifest records
   `action_class_entropy: 0.0` with a single action class across all 1200 ticks in every
   cell -- so the whole run collapses into **one** repeat-run and the metric reads 1. That
   is a *saturated ceiling misreported as a floor*, not an absence of freezing. 478 also
   runs no warmup training (EPISODES=6, no warmup phase), against 475's 60 warmup episodes.
2. **MECH-287's actual DV is PAG-gate-conditioned** -- "freeze re-commit count per PAG
   release". That quantity only exists when MECH-279's PAG freeze gate is on, which 478
   never enabled. 478 could not have measured MECH-287's DV under any outcome.

## 3. The blocking finding: anchor invalidation is behaviourally inert under the registered flag set

MECH-287's DV is behavioural ("Freeze re-commit count per PAG release and time-to-mode-flip
from avoid back to goal-seeking"). Its registered substrate list stops at the **write side**:

> `invalidation_trigger.py` emits BroadcastEvents; `module.py` drains them via
> `apply_invalidation_broadcasts_to_regions` (gated on `use_per_region_vs`) and
> `tick_anchor_set` (gated on `use_anchor_sets`)

Verified at source, every consumer of anchor active/inactive state in the agent:

| Site | Consumer | Gated on | Behavioural? |
|---|---|---|---|
| `agent.py:7375-7391` | commit release: `beta_gate.release()` + `_committed_step_idx = 0` when a snapshot anchor key leaves `active_anchors()` | **`use_vs_commit_release`** | **YES -- the only one** |
| `agent.py:10223`, `:10281` | commit-entry anchor-key snapshot | `use_vs_commit_release` | supporting half of the above |
| `agent.py:4517` | `_scientist_attribution_region()` -- MECH-276 attribution keying | (ungated) | no |
| `hippocampal/ghost_goal_bank.py:574` | ghost-goal ranking | `use_mech292_ghost_bank` | only via MECH-293 |
| `hippocampal/staleness_accumulator.py:80-97` | staleness integration | `use_staleness_accumulator` | bookkeeping only |

`use_vs_commit_release` defaults False (`config.py:3073`) and **its own docstring names this
experiment as the reproduction case**:

> "This is the read-side closure of the V_s invalidation runtime: anchor invalidation events
> authored by MECH-287/MECH-288/MECH-284 (write-side) become observable behavioural changes
> (commitment release) only when this flag is on. Backward compatible: disabled by default;
> **with flag off, EXQ-478/480 wired-but-inert behaviour reproduces.**"
> -- `ree-v3/ree_core/utils/config.py` :3060-3072

### 3b. The claim's own mechanism narrative does not match the substrate

MECH-287's `functional_restatement` explains the 475 phenotype as "The hippocampal proposer
keeps drawing trajectories from the original anchor." **The proposer does not consult anchors
at all.** `HippocampalModule.propose_trajectories` (`module.py:2037`, the sole caller is
`agent.py:6473`) is terrain-guided CEM seeded from the current `z_world` and the E1 prior;
its only anchor-sensitive branch is the MECH-293 ghost-probe seeding at :2510, gated on
`use_mech293_ghost_probes` (`config.py:3150`, default False), which itself requires
`use_mech292_ghost_bank` (:3126, default False).

So the narrative route by which invalidation was supposed to reduce re-commits is, in the
current substrate, either absent (proposer) or behind an unregistered flag (MECH-292/293).

## 4. Consequence if built as pre-registered

Four arms over `use_invalidation_trigger` x (`use_staleness_accumulator` +
`use_mech284_hysteresis`), on 475's config, with `use_anchor_sets`/`use_event_segmenter`/
`use_per_region_vs` held on as substrate and **no read-side flag**, gives:

- broadcasts fire (trigger arms), staleness integrates (accumulator arms), anchors reset --
  all the write-side instruments move, exactly as 478 already showed (63/31 resets);
- and **no arm can differ from any other on the behavioural DV**, because no code path
  connects anchor state to commitment or proposal.

That is MECH-287's FALSIFYING clause satisfied verbatim -- "broadcasts firing and staleness
integrating yet freeze re-commit counts and mode-flip latency indistinguishable from the
both-lesioned arm" -- on a comparator that *does* reproduce the lock regime, so the claim's
own "failure under unmet preconditions is not evidence against the claim" escape does not
obviously apply. It would read as a clean refutation of MECH-287 and would be an artifact of
a missing read-side hook. This is the Step 2.5d INERT shape.

## 5. The decision (the reason this session stopped)

Three routes. They are not interchangeable -- they measure different chains and attach
evidence to different claims.

**Option A -- `use_vs_commit_release=True`, held fixed ON across all arms.**
Measures: does the MECH-287 write-side chain, *read out through the MECH-269/MECH-090
commitment-release hook*, reduce per-release re-commits and shorten time-to-mode-flip? The
four-arm dissociation (trigger-loss -> zero broadcasts; accumulator-loss -> broadcasts that
never integrate) still works inside that conjunction, which is what MECH-287's secondary
falsifiable asks for. Cost: one flag beyond the registered set; a positive result supports
the conjunction MECH-287 + MECH-284 + the MECH-269 read-side hook, not MECH-287 alone.
Precedent exists in-tree (V3-EXQ-490b/490c/490e/490f/596/601 all set it True).

**Option B -- `use_mech292_ghost_bank=True` + `use_mech293_ghost_probes=True`.**
Measures the claim's literal narrative (invalidation changes what the proposer draws).
Cost: inserts MECH-292 and MECH-293 into the causal chain, so a null is ambiguous across
three claims; substantially more substrate in the loop; no precedent run at this operating
point.

**Option C -- build it exactly as registered (no read-side flag).**
Measures: whether the write-side chain alone moves behaviour. The answer is knowable in
advance from the code (it cannot), so this spends fleet time to produce a false-looking
refutation of MECH-287.

**Recommendation: Option A**, with `use_vs_commit_release` held ON and identical in all four
arms (so it cannot confound the trigger x accumulator contrast), the comparator built on
V3-EXQ-475's config per the pre-flight's named change, and MECH-287's
`what_would_answer` + SUBSTRATE / INSTRUMENT REQUIREMENT amended to name the read-side flag
as a precondition -- because the pre-registration is currently under-specified in a way that
would have produced a confident false null. Option A is the narrowest change that makes the
registered DV live, and it keeps the registered manipulation exactly as ratified.

A secondary point the user may want to rule on at the same time: MECH-287's
non-degeneracy precondition is written against V3-EXQ-475's regime, but 475 ran with **no
anchor substrate at all** (no `use_anchor_sets`). The comparator arm here is 475's config
*plus* the anchor/segmenter/per-region substrate held on -- a configuration never run. That
the lock regime survives that addition is checkable by a dry run and is treated here as an
authoring-side smoke-test obligation, not a user decision.

## 6. What was verified vs assumed

Verified at source this session: all six config flag definitions and defaults; the four
`active_anchors()` consumers in `agent.py` and their gates; `propose_trajectories`' signature,
sole caller and anchor-branch gating; 478's manifest cells and its driver's metric definition
and flag block; 475's metrics, env_config and driver config block; the absence of any
MECH-287 queue entry; the absence of any OPEN governance flag naming MECH-287 (six hits, all
`resolved`; note GFLAG-0452 resolved 2026-09-24T10:25:37Z moved MECH-287 provisional ->
candidate and re-read V3-EXQ-757 as `non_contributory`).

Not verified: whether the lock regime reproduces under 475-config-plus-anchor-substrate
(requires a run); the numeric thresholds for "drops materially" and "bounded re-commit
budget", which remain unspecified in `what_would_answer` and would need pre-registering
once the option above is chosen.
