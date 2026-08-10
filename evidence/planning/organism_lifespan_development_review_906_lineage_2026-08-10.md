# Organism-Level Lifespan & Development Review: V3-EXQ-906 Lineage

**Generated:** 2026-08-10T05:36Z
**Type:** organism-level observational review, continuation of `observational_review_V3-EXQ-906b_2026-08-09.md`
(all runs below are diagnostic showcases, `claim_ids=[]`; nothing here weights governance directly)
**Scope:** verify survivability/censoring across 906->906a->906b->906c(+911); establish exactly what
"continuous life" means mechanically; synthesize the three unreviewed successor runs that landed
overnight (V3-EXQ-909, -910, -906c); run a novel bout-level + within-life developmental analysis directly
on already-collected episode logs (no new experiment); duplication-check before proposing anything new.
**Sources newly read this session:** `v3_exq_906/906a/906b/906c/911` driver scripts + `ree_core/agent.py`
`reset()`, `ree_core/environment/causal_grid_world.py` `reset()`/`step()`, all seven runs'
manifest.json/metrics.json/summary.md, the 906b/906c/909 episode logs (direct python3 inspection),
`claims.yaml` (MECH-357/439/482/483), `sleep_substrate_plan.md`, `TASK_CLAIMS.json`,
`observational_review_V3-EXQ-906b_2026-08-09.md` (full, 690 lines).

---

## 0. Verdict

The user's framing -- "has the Fishtank crossed from testing whether an integrated stack can stay alive
long enough to observe, into studying whether an inexperienced persistent agent develops through
accumulated experience?" -- is **half right, precisely along the line the evidence draws**:

1. **The survivability increase is real, enormous, and almost entirely NOT a REE-competence effect.**
   It is a chain of environment/mechanism bug fixes (Section 2). By V3-EXQ-911 the step cap is now binding
   on 8/8 segments -- literally zero deaths occurred in that run. Mean segment length has stopped
   measuring survival at all; it measures "how long we chose to keep recording."
2. **"Continuous life" is real and well-characterized within one run (up to ~4000 steps across 8
   segments), but does NOT extend across the lettered lineage** (906a/b/c/911 each train a brand-new
   agent from scratch). So within-lifetime development can currently only be probed inside one run's
   ~4000-step window, and the statistical power to do so is very low (n=8 segments/run, n=2 runs
   analysed).
3. **A direct test for within-life development was run this session** (Section 5) on the two long
   continuous runs available (906b, 906c). It found a pattern **consistent with** improvement in 906b
   (declining harm rate, rising benefit rate, falling behavioural entropy across segments) that **does
   not replicate** in 906c (flat-to-opposite on the same measures). Given the environment re-randomises
   its hazard/resource layout at every segment boundary (Section 1), this is exactly what an
   environment-luck artefact would also produce. **The evidence does not currently distinguish "REE
   developed within its life" from "segment-to-segment layout variance."**
4. **Three successor runs landed since the 906b review and are synthesized here for the first time**:
   V3-EXQ-910 (defensive-orienting validation) **FAILED**, cleanly and instructively; V3-EXQ-909 (sleep DV)
   **PASSED on a very shallow bar** and, critically, **contains zero pre/post-sleep behavioural
   comparison** -- the user's central sleep question remains completely untested; V3-EXQ-906c
   (appetitive-coupling instrumentation) surfaces one new plumbing bug (`residue_wanting` is dead, not
   floor) and extends an already-known measurement defect (unclamped valence accumulation) to `liking`.
5. **A novel bout-level analysis** (Section 6, this session's own pass over the raw 906b/906c episode
   logs) does **not** rescue the 906b review's "affect channels don't organise behaviour" finding --
   if anything it corroborates it, and adds a genuinely new structural observation: most step-time is
   consumed by two long, low-`z_goal` "settled" regimes (`assert`, `shelter`), not by sustained
   goal-directed pursuit.

No item below is charged cleanly to "REE." Per GOV-FAILLOC-1, most of what looks like organism failure in
this section is MEASURES- or MECHANISM-layer, and the strongest REE-candidate finding (within-life
learning is undemonstrated) is undemonstrated because of a design confound, not because it was tested and
failed.

---

## 1. What "continuous life" currently means -- established from code, not inference

Read directly: `ree-v3/experiments/v3_exq_906a_full_stack_observational_fishtank.py` (the "CONTINUITY
REDESIGN" docstring + segment loop), `ree_core/agent.py` `reset()` (~380 lines, lines 3119-3505),
`ree_core/environment/causal_grid_world.py` `reset()`/`step()`. 906b/906c/911 all import the identical
`_observational_run` loop from 906b unchanged.

**The loop, exactly:**
```python
for ep_idx in range(num_episodes):
    flat_obs, obs_dict = env.reset()          # ALWAYS fires, every boundary, every done_cause
    if ep_idx == 0:
        agent.reset()                          # FULL cognitive reset -- boundary 0 ONLY
    else:
        _segment_boundary_consolidate(agent)   # PARTIAL -- every other boundary, regardless of cause
```

**The single most important fact this investigation needed:** `done_cause` (`health_depleted` vs
`step_limit`) is **never branched on**. Both are handled by exactly the same code. Concretely:

- **`env.reset()` fires unconditionally at every boundary**: it re-rolls hazard/resource positions and
  agent position, rebuilds the contamination/footprint grids, zeroes the environment's own step counter,
  and **revives `agent_health` to 1.0** (`causal_grid_world.py:1422-1446,1508,1620`). This happens whether
  the preceding segment ended by running out of health or by running out of the 500-step clock.
- **The agent's cognitive/affective substrate gets a full wipe only once, at the very start of eval**
  (`ep_idx==0`) -- E1 hidden state, harm/replay buffers, dACC/salience/coalition/AIC state, theta_buffer,
  beta_gate, serotonin, cached E1 prior, and dozens of other named submodules. Every later boundary instead
  calls `_segment_boundary_consolidate()`, which does exactly two things: flush the exploration episode
  into the hippocampal buffer, and notify the sleep-loop manager the episode ended.
- **Explicitly persists always, even through the boundary-0 full reset** (by documented design invariant,
  `agent.py:3120`): the residue field (`ResidueField` valence vectors -- the substrate for wanting/liking/
  surprise/excite/dread). **Persists across all non-zero boundaries** (never touched outside `ep_idx==0`):
  learned policy weights (never touched at all, any boundary), the hippocampal exploration/memory buffer
  (accumulates continuously), sleep-machinery cadence state (`notify_episode_end` called at every boundary
  specifically to keep the cadence running), E1 hidden state, theta_buffer/z_self/z_world continuity,
  dACC/salience/coalition state. **Resets every boundary unconditionally** (belongs to the environment, not
  the agent): `agent_health`, hazard/resource/agent positions, the grid layout, contamination/footprint
  grids, the environment's own step counter.

**Consequence, stated exactly:** a `health_depleted` segment ending, when followed by another segment in
the same run, mechanically means **health regenerated on the same persisting agent** -- there is no
agent-re-instantiation branch anywhere in the loop. This substrate, as currently coded, has **no permanent
death mechanic within a run**. "Death" in every manifest/summary.md to date (`health_depleted` counts,
"segment endings") is a **recoverable body-state event on a continuing mind**, not a terminal event for the
organism -- the two are conflated only by the natural-language framing ("episode terminates," `done` flag),
not by anything the code actually does differently. Whether that is the right substrate design is a
separate question (Section 3 below); the finding here is only about what the current code implements.

**So "continuous life" today = one uninterrupted cognitive/affective/mnemonic trajectory of up to ~4000
steps within a single queue run, observed through 8 recording chunks of up to 500 steps each, where each
chunk boundary refreshes the body and immediate surroundings but not the mind.** It does **not** extend
across the 906->906a->906b->906c(->911) lineage: every lettered run independently trains a brand-new
`REEAgent` from scratch (confirmed via grep for `checkpoint`/`load_state_dict` across all five driver
scripts and their shared curriculum modules -- the only checkpoint-loading code anywhere in the tree,
`clone_trained_agent()` in `scaffolded_sd054_onboarding.py`, is for an unrelated V3-EXQ-620 arm and is
never called by any 906-family script). Each run's own `harm-pathway train steps (total): ~3750-3940`
figure in its summary.md is exactly this from-scratch training, repeated per letter.

**One further gap worth flagging for future instrumentation:** no manifest or episode-log field stores a
cumulative/monotonic step counter across the whole run -- every segment's per-step `t` restarts at 0. A
reader must reconstruct cumulative position by manually summing prior segments' `realized_steps`. This is a
minor telemetry gap, cheap to fix, and would materially help any future within-life analysis (Section 5
below had to reconstruct it by hand).

---

## 2. Survivability and censoring, verified

| run | eval steps | segments | mean steps/segment | health_depleted | step_cap | % right-censored | primary driver of the change vs prior letter |
|---|---|---|---|---|---|---|---|
| 906 | 447 | 30 | **14.9** | n/a (pre-continuity: 30 independent fresh resets, not comparable to the rest) | | | contamination-death bug (SD-094 trap #2) |
| 906a | 203 | 8 | **25.4** | 8 | 0 | **0%** | continuity redesign landed; contamination fixed; grid-wide proximity-harm radius (~11 cells) still untouched |
| 906b | 3909 | 8 | **488.6** | 2 | 6 | **75%** | proximity-harm radius tightened to ~1.33 cells (inside the sensory window) |
| 906c | 3793 | 8 | **474.1** | 1 | 7 | **87.5%** | unchanged ecology from 906b (telemetry-only iteration) -- within-seed replication |
| 911 | 4000 | 8 | **500.0** | 0 | 8 | **100%** | resource-side field-decay fix (unrelated to hazard side, incidental to survivability) |

All five figures verified directly against `metrics.json`/`manifest.json`/`summary.md` (all three agree;
906b spot-checked in full, others cross-checked against summary.md's own numbers, which is a computed field
in each run's script, not a manually transcribed one). The user's cited numbers (906 ~14.9, 906a ~25.4,
906b ~488.6 with 6/8 capped, 906c ~474 with 7/8 capped) are **confirmed exactly**.

**Reading, per GOV-FAILLOC-1:** the ~33x increase in mean segment length from 906a to 906b, and the
progression to 100% censoring by 911, is **overwhelmingly ENVIRONMENT/MECHANISM** (a sequence of
specifically-diagnosed and specifically-fixed bugs: contamination-death, grid-wide proximity-damage radius,
resource-field decay) -- **not** a demonstration that REE became more competent at surviving. 906a's own
0% censoring is the sharpest illustration: with the contamination bug still fresh but the radius bug not
yet found, literally every one of 8 segments died the same way, at essentially the same rate (25.4 mean
steps, presumably fairly tight variance -- not checked here) regardless of anything the agent did. This is
a hazard that was environmental in origin and was removed environmentally; it never tested REE's
avoidance competence at all.

**The user's caution about right-censoring is now sharper than "heavily censored" -- it is total.**
V3-EXQ-911, the most recent letter with a clean survivability read, shows **zero deaths across all 8
segments**. Mean segment length has stopped being informative about survival at all; every run since 906b
is now measuring "we stopped watching at 500 steps," not "the organism could not continue." **A genuine
survival-curve / hazard-of-death-over-age measure requires an uncensored design** -- see Section 7's
successor proposal.

---

## 3. Successor 1 -- V3-EXQ-910 (MECH-489/SD-099 defensive-orienting validation): FAIL

2-arm ablation (`orienting_off`/`orienting_on`), seeds [0,1], validating the fright->freeze->orient->
epistemic-override->approach/withdraw/resume chain built 2026-08-09T20:45Z per the 906b review's Section
11b/11d. **Outcome: FAIL**, label `defensive_orienting_partial_or_unmet`. No `failure_autopsy` exists yet
for this run -- the finding below is a first read of the manifest, not a re-statement of one.

**Criterion (a) -- does the trigger fire on the ground-truth events it exists to catch? No, decisively:**

| event | n | alignment_rate |
|---|---|---|
| `limb_damage_injected` | 76 | **2.6%** |
| `external_hazard_injected` | 65 | **1.5%** |
| `world_rule_shift_occurred` | 30 | **0.0%** |

This is a **direct, higher-power confirmation** of the risk the 906b review's Section 12h explicitly
flagged in advance (single-seed, n=15-31, "a real risk signal, not a definitive refutation" at the time).
910 pools 2 seeds to n=76/65/30 and the alignment collapses to near-zero across the board -- sharper than
12h predicted, not merely consistent with it.

**Criterion (b) and the arm comparison -- the mechanism does something large, just not the targeted
thing:**

| metric | OFF (legacy proxy) | ON | 12b baseline (906b) |
|---|---|---|---|
| n_spike (surprise-spike candidate events) | 463 | **50** | -- |
| p(moved \| spike) | 0.296 | 0.28 | 0.443 |
| p(mode-change \| spike) | 0.283 | 0.14 | 0.154 |
| p(moved), unconditional | 0.200 | **0.013** | 0.24 |
| p(mode-change), unconditional | 0.173 | 0.093 | 0.111 |
| decision_alignment (206 valence-gated decisions, ON arm) | -- | **approach=0, withdraw=206, resume=0** | -- |

Turning orienting on collapses unconditional movement ~15x (0.200 -> 0.013) and produces a decision
distribution that is **100% withdraw, 0% approach, 0% resume** across all 206 logged overrides. The
mechanism is not inert -- it is doing something pervasive and measurable -- but it is a **crude, one-sided
lockup** (perpetual defensive withdrawal whenever it engages), not the intended nuanced,
event-appropriate approach/withdraw/resume gating, and it is not gated by the ground-truth events it was
built to detect.

**Net classification (GOV-FAILLOC-1): MECHANISM-layer, and specifically the calibration step, not the
architecture.** The 906b review's own Section 12h/13-A explicitly warned, *before this run existed*: "a
naive absolute-value-spike trigger at [the p90] threshold would likely under-fire on the paradigm cases...
re-derive the threshold... use a per-episode-relative spike (derivative against a rolling baseline)... or
combine `residue_surprise` with the `mode`-change signal, which responds more reliably." The manifest
contains no record of which trigger implementation was actually used, but the result pattern (near-total
misalignment, worst on exactly the event types 12h flagged) is the fingerprint of the naive
absolute-threshold design the review warned against, not the derivative/onset-detector design it
recommended. **This is a case where the write-up's own prior warning appears not to have been carried into
the build's calibration step** -- worth a `/failure-autopsy` to confirm which trigger form was actually
implemented and close the loop explicitly (flagged as follow-on, Section 7; not investigated further here
since it needs the actual `defensive_orienting.py` trigger-condition code cross-referenced against the run,
which is squarely `/failure-autopsy` scope).

---

## 4. Successor 2 -- V3-EXQ-909 (sleep-refinement DV, multi-firing/multi-seed): PASS on a shallow bar, and it does not test what "does behaviour improve after sleep" needs

Status `PASS`, label `sleep_dv_nonnull_detected`. **What "non-null" actually means, verbatim from the
manifest's pre-registered rule:** "a firing is 'non-null' if `sws_slot_diversity > 0.01` OR
`replay_diversity_index > 0.01`... label='sleep_dv_nonnull_detected' iff frac_nonnull >= 0.1." This is a
binary check that the sleep mechanism's internal diversity channels are not stuck at the `-1.0` zero-draws
sentinel (the structural bug 906b's one firing exposed, Section 12d of the prior review) -- **it is not a
behavioural measure, and it is not what the label's plain-English reading suggests.**

**The magnitudes themselves are close to degenerate, not "diverse":**
- `sws_slot_diversity` (mean pairwise cosine *distance* between memory slots): min 1.14e-05, mean 2.3e-04,
  max 9.2e-04 across all 45 firings -- cosine *similarity* between memory slots is ~0.9998-0.99999
  essentially everywhere. This clears the `>0.01` bar only via its OR-partner; taken alone it reads as a
  near-fully-collapsed memory, not a diverse one.
- `replay_diversity_index` (`distinct_regions_replayed / n_draws`, `draws_per_cycle=50` fixed): **exactly
  0.02 on every single one of the 45 firings, all 3 seeds, zero variance.** Exactly one unique region
  replayed out of 50 draws, every time, with no variation at all. This is itself a strongly degenerate
  result (`r(waking mode-entropy, replay_diversity_index)` is reported `None` in the summary precisely
  because there is no variance to correlate against).
- The one correlation reported, `r(waking mode-entropy, sws_slot_diversity) = 0.393`, is the weak
  relationship between two quantities that are both mostly floor/noise. Given the near-total lack of
  practical magnitude on both sides, this should not be read as "sleep registers waking diversity" --
  if anything it is more consistent with the sleep mechanism's diversity channels still being essentially
  collapsed on this substrate, which **leans toward corroborating**, not resolving, the 906b review
  Section 11a's "expected null" prediction for the repertoire-vs-conversion question.

**The load-bearing gap for the user's actual question: there is no pre/post-sleep behavioural comparison
anywhere in this run's data.** Grepped both the manifest and the full episode log for any
before/after-sleep behavioural field. The only "before/after" pair that exists is
`post_sleep_z_goal_before`/`post_sleep_z_goal_after` -- an internal-state numeric-retention check
(bit-identical in every sampled record; it verifies the goal-latent vector survives the sleep pass
intact, nothing about observed behaviour). The per-firing record (`sleep_firing_records`, 45 entries)
captures only the **preceding** segment's `waking_mode_entropy_bits_prior_segment` /
`waking_unique_cells_prior_segment` / `waking_steps_prior_segment` -- there is **no corresponding field
for the segment that follows** a firing. Route efficiency, hazard exposure, resource acquisition, action
entropy of the post-sleep segment, repeated-action structure, goal persistence, or prediction error on
previously-seen situations are not logged before OR after in a form that lets them be compared.

**Consequence for the user's brief:** "compare matched windows immediately before and after sleep" is
exactly the right next test, and **it cannot currently be run even from already-collected data** -- this is
a genuine instrumentation gap, not an unexamined-but-available analysis. It needs a new run (or a
re-instrumented successor) that logs a matched post-firing waking window keyed to the same
`(seed, boundary_index)`, not a re-read of 909's existing artifact.

No `failure_autopsy` or `/governance` review exists yet for 909; it is currently only listed as a pending
item in `inter_governance_workset.md`. `sleep_substrate_plan.md`'s GAP-2 status table has **not** been
updated to reflect this result (last substantive GAP-2 edit predates 909's landing) -- flagged as a small
housekeeping follow-on (Section 7), not fixed in this session (scope discipline: this doc is the
observational record; the plan-of-record table is a `/governance`/plan-maintenance edit).

---

## 5. Successor 3 -- V3-EXQ-906c (appetitive-sequence + coupling instrumentation): decoupling replicates under a fresh seed; two measurement bugs found

906c reuses 906b's ecology **byte-identically** (confirmed: `use_defensive_orienting` is absent from
config -> defaults `False`; 906c's `_make_config()` is imported unchanged from 906b) -- so 906c is a
**second seed on the unchanged substrate**, not a test of the newly-built defensive-orienting mechanism,
even though the mechanism's code (commit `c1c24c6`) is an ancestor of 906c's substrate commit. Any
coupling-metric differences from 906b are seed variation, not a mechanism effect; important not to
conflate the two.

**Coupling metrics -- five of six replicate within noise, one does not:**

| metric | 906b | 906c | read |
|---|---|---|---|
| dread(t) -> harm t+1..t+3 | 0.065 | 0.105 | same sign/order -- replication |
| z_goal(t) -> approach t+1 | 0.064 | 0.069 | replication |
| z_goal(t) -> benefit t+1..t+3 | -0.036 | -0.048 | replication |
| **dread <-> z_harm_a (contemporaneous)** | **+0.032** | **-0.175** | **sign flip, ~5x magnitude -- outlier, unexplained; single-seed, cannot attribute to signal vs noise** |
| surprise-spike -> mode-change | 15.4%/11.1% | 17.1%/12.0% | replication |
| surprise-spike -> moved | 44.3%/24.0% | 45.5%/20.8% | replication (spike arm); no-spike arm ~13% relatively lower |

**This is a genuine, useful corroboration the manifest itself does not state**: the 906b review's central
Section-4 finding -- affect channels vary but essentially do not predict subsequent behaviour or events --
**replicates under a fresh seed with no architectural change**, which is exactly the kind of second
independent data point that turns a single-seed observation into a more durable one. It should be recorded
as strengthening, not merely repeating, the original finding.

**New measurement bug #1 -- `residue_wanting` is exact zero because it is never written, not because the
channel is at floor.** `residue_wanting: mean=0.0000 std=0.0000` across all 3793 steps. The read path is
correct (`VALENCE_WANTING = 0`, read via `evaluate_valence(z_world)[0, 0]`). But the two writer methods
that populate that index -- `update_benefit_salience()` and `update_schema_wanting()` in `ree_core/agent.py`
-- are **never called from inside the agent's own step loop** (confirmed by grep: their only callers
anywhere in the repo are unrelated experiment scripts, none in the 664/665/906-family). This is a
**different channel from `z_goal`** (the wanting-adjacent channel the 906b review's Section 3a already
characterized as sparse-but-real, p50=0/mean=0.024/max=0.476) -- `residue_wanting` (VALENCE_WANTING,
residue index 0) is a second, additional wanting-adjacent signal that is simply orphaned in this driver
family. Classification: **MEASURES/plumbing**, not a REE or mechanism finding -- the write path exists and
works elsewhere in the codebase, it is just never invoked here.

**New measurement bug #2 (extends an existing finding) -- `liking` shares the unclamped-accumulator defect
already flagged for `excite`.** `liking: mean=19.8812 std=10.4847` -- not on a bounded per-tick scale. Every
one of the 6 residue valence components (wanting=0, **liking=1**, harm_discriminative=2, surprise=3,
excite=4, dread=5) is written through the identical `RBFLayer.update_valence()` code path, documented in
`ree_core/residue/field.py` as an unclamped `+=` that "accumulates across visits" with no decay -- exactly
the mechanism the 906a autopsy already flagged for `excite`/`dread` under `SD-RESIDUE-VALENCE-BOUND`. A dry
run smoke test (commit `bd90e8d`) glimpsed liking maxing at 0.39 over ~60 steps; the full 3793-step eval
reaching mean=19.88 (~50x that per-step ceiling) is consistent with a per-tick-accumulating total, not a
bounded hedonic-impact readout. **`liking`, like `excite`, should not yet be read as a trustworthy
quantitative appetitive signal** -- the manifest's own contamination caveat is currently written only
against `excite`; it should extend to `liking` when SD-RESIDUE-VALENCE-BOUND is fixed and re-checked.

`is_committed` (the 906b review's Section 12a `e3_selector.get_commitment_state()` signal, 0/3909 in
906b) is **not reported** in 906c's manifest/metrics -- absent, not re-confirmed. It is present in the raw
episode log schema (see Section 6 below), so a future pass can recompute it; not treated as a regression,
just noted as an unclosed loose end.

---

## 6. Bout-level analysis (novel this session -- direct re-read of the already-collected 906b/906c episode
logs, no new experiment)

The user's brief asked whether a bout-level unit reconciles visually-purposive behaviour with the 906b
review's weak adjacent-step correlations. This was investigated directly: segmented both runs' `mode`
field (already logged per-step) into maximal contiguous same-mode runs ("bouts"), then tested whether
internal-state levels during a bout, or a bout's mean internal-state, predict the bout's outcome.

**Bout inventory -- both runs:**

| mode | 906b n_bouts | 906b mean len | 906b total steps | 906c n_bouts | 906c mean len | 906c total steps |
|---|---|---|---|---|---|---|
| shelter | 54 | 27.1 | 1463 (37%) | 54 | 8.2 | 441 (12%) |
| assert | 11 | 67.1 | 738 (19%) | 7 | **184.9** | 1294 (34%) |
| neutral | 120 | 6.5 | 774 (20%) | 127 | 9.1 | 1155 (30%) |
| approach | 142 | **4.5** | 643 (16%) | 123 | **3.7** | 456 (12%) |
| avoid | 20 | 8.5 | 169 (4%) | 27 | 10.9 | 294 (8%) |
| explore | 110 | **1.1** | 122 (3%) | 131 | **1.2** | 153 (4%) |

**Robust structural finding, replicated across both runs: goal-directed modes (`approach`, `explore`) are
short flickers, not sustained pursuit.** `explore` bouts average ~1.1-1.2 steps with a max of 3 in both
runs -- essentially every "explore" step is an isolated blip surrounded by other modes, not a sustained
program (candidate MEASURES-layer artefact: the classifier's explore threshold may sit right on a decision
boundary that gets crossed only fleetingly, rather than the substrate genuinely lacking exploratory
persistence -- not resolved here). `approach` bouts average 3.7-4.5 steps. By contrast, `assert` and
`shelter` are long, sustained regimes that together consume 56% (906b) to 46% (906c) of all step-time.
**What a human watching the fishtank reads as coherent, purposive-looking behaviour is substantially the
agent settling into and holding two long low-arousal regimes, punctuated by short bursts of
directional activity** -- the long regimes are themselves a real, comprehensible behavioural pattern
(genuinely coherent, in the sense of being sustained and non-random), but they are not goal-pursuit in the
sense the internal `z_goal`/wanting channels would organise.

**Internal-state elevation during bouts, robust across both runs:** `avoid`-mode bouts show elevated
`z_harm_norm` relative to baseline in both runs (906b 1.42x, 906c 1.42x -- identical), and elevated dread in
both (906b 1.22x, 906c 2.24x). `assert`-mode bouts show low `z_goal` and low `z_harm_a` in both runs (906b
0.60x/0.19x, 906c 0.11x/0.42x) -- consistent with a genuinely settled/at-rest state, not a
goal-suppressed-by-threat state. These are modest-to-moderate elevations, not sharp on/off signatures.

**Outcome-predictive tests -- do NOT replicate across the two runs, and should be read as unresolved, not
as evidence either way:**

| test | 906b | 906c |
|---|---|---|
| approach-bout mean z_goal: benefit bouts vs no-benefit bouts | benefit LOWER (0.032 vs 0.046, n=128/14) | benefit HIGHER (0.044 vs 0.014, n=108/15) |
| avoid-bout mean dread: harmed bouts vs clean bouts | harmed LOWER (1.05 vs 1.86, n=11/9) | harmed HIGHER (0.65 vs 0.45, n=19/8) |

Both tests **flip sign** between the two runs. Given the small per-bucket n (single digits to low
hundreds) in both cases, the honest read is that neither run provides a reliable directional signal, and
the two together actively argue against over-reading either single-run result. The within-approach-bout
z_goal trajectory (checked by normalized-position decile, bouts len>=5) shows no monotonic build-up in
either run -- values bounce in a narrow band with no rising-then-acting profile.

**Answer to the user's specific question: bout-level analysis does not reconcile the discrepancy -- it
corroborates the review's existing `is_committed`=0/N finding from a second, independent angle.** Grouping
by contiguous same-mode runs and testing bout-level (rather than step-level) coupling still finds no
reliable, cross-seed-consistent relationship between motivational channels and behavioural outcome. The
structural bout-length finding (approach/explore are brief, assert/shelter dominate step-time) is the
genuinely new and reproducible piece; it reframes "purposive-looking" as substantially "settled-looking,"
which is a real but different thing.

---

## 7. Within-lifetime development: a direct test was run; the result is genuinely inconclusive, and the
design reason why is now clear

Per-segment behavioural metrics were computed directly from the same two episode logs, treating segment
index (and reconstructed cumulative step position, since none is stored -- Section 1) as a proxy for
"age"/cumulative lived experience within the one continuous run.

**906b (n=8 segments): a pattern consistent with improvement.**

| | ep0-3 (early) | ep4-7 (late) | r(segment index) |
|---|---|---|---|
| harm rate | 0.113 | 0.035 | **-0.34** |
| benefit rate | 0.284 | 0.425 | **+0.49** |
| mode entropy | 2.03 | 1.52 | **-0.76** |
| move rate | 0.250 | 0.270 | +0.41 |
| blocked-action rate | 0.042 | 0.036 | -0.31 |

Taken alone, this is exactly the developmental signature the user's brief hypothesized: harm declining,
benefit rising, behaviour becoming less entropic (more organised/less exploratory) over the course of one
continuous life.

**906c (n=8 segments): the same measures, same run design, do not replicate the direction.**

| | ep0-3 (early) | ep4-7 (late) | r(segment index) |
|---|---|---|---|
| harm rate | 0.079 | 0.081 | **+0.36** (opposite sign to 906b) |
| benefit rate | 0.213 | 0.268 | +0.03 (much weaker than 906b) |
| mode entropy | 1.86 | 1.69 | +0.19 (opposite sign to 906b) |
| move rate | 0.197 | 0.234 | +0.56 |
| blocked-action rate | 0.049 | 0.039 | -0.55 |

Harm rate and mode entropy **flip sign** between the two runs; benefit rate shows the same direction in
both but is far weaker in 906c (+0.03 vs +0.49 correlation).

**This is not merely "n too small" (though n=8 segments and n=2 runs genuinely is small) -- there is a
specific, identified design confound that would produce exactly this pattern even with zero real
learning.** Section 1 established that `env.reset()` **re-rolls the hazard/resource layout at every
segment boundary**, unconditionally. So segment-to-segment differences in harm/benefit rate are contaminated
by which random layout that particular segment happened to draw, in a way that is entangled with, and
currently indistinguishable from, genuine within-life behavioural change. 906b's clean-looking trend and
906c's failure to replicate it is exactly the pattern this confound predicts, and is at least as consistent
with "906b got a lucky/friendlier draw of layouts in its later segments" as with "REE got better."

**Per the user's own instruction ("if nothing relevant persists, say so... apparent improvement could
otherwise be an artefact"): a great deal DOES persist mechanically (Section 1 -- weights, residue field,
memory, sleep state), so this is not a case of nothing being available to develop. But the current
experimental design cannot yet isolate a developmental signal from an environmental-randomization
confound with only 8 segments per run.** A successor that either (a) holds the layout fixed or
seed-paired across segments within a run (so segment-to-segment differences can only be attributed to the
agent, not the world), or (b) runs many more segments per continuous life (raising n well past 8) is needed
before this question can be answered either way. Neither currently exists in the queue (Section 8).

**One structural mechanism relevant to this question that already exists but is untested in this context:**
`claims.yaml`'s **MECH-357** (candidate, `v3_pending`) is an eligibility-trace avoidance-efficacy learner --
credited when a directed action under threat reduces `z_harm_a` -- built and validated via the Stage-H
training curriculum. It was **not investigated in this session** whether MECH-357 is active in the fishtank
config (`_make_config()`), nor whether its training-time credit-assignment would produce a measurable
within-episode signature on a continuous-life ecology. This is a concrete, cheap next check (grep the
fishtank `_make_config()` for the relevant flag, then re-read the episode log for the specific "hurt once ->
avoids sooner" signature the user described) rather than a new experiment, and is recorded as a follow-on
(Section 8), not resolved here.

---

## 8. GOV-FAILLOC-1 four-layer summary (this session's findings only -- see the 906b review's own Section 7
for its findings)

| Observation | REE | MECHANISM | MEASURES | ENVIRONMENT | Net |
|---|---|---|---|---|---|
| 906->911 survivability increase (~34x, then to 0 deaths) | -- | yes (contamination, radius bugs) | -- | yes (bug fixes) | **ENVIRONMENT/MECHANISM, not REE competence** |
| 906b/906c/911 heavily-to-totally right-censored | -- | -- | yes (step cap no longer discriminating) | -- | **MEASURES -- design now needs an uncensored successor** |
| "Death" (health_depleted) is recoverable, not terminal | -- | candidate (by design, not bug) | -- | -- | **MECHANISM/design -- flag for `/governance`, not a defect per se** |
| V3-EXQ-910 trigger near-zero alignment on ground-truth events | -- | **yes** (naive-threshold calibration, warned against in advance) | -- | -- | **MECHANISM (calibration step)** |
| V3-EXQ-910 orienting_on = crude 100%-withdraw lockup | candidate | yes (architecture produces one-sided output) | -- | -- | **MIXED -- needs `/failure-autopsy`** |
| V3-EXQ-909 "non-null" sleep DV is a shallow bar; magnitudes near-degenerate | -- | candidate (sleep replay still near-collapsed) | yes (label overstates the result) | -- | **MIXED, leans MEASURES** |
| V3-EXQ-909 has zero pre/post-sleep behavioural comparison | -- | -- | **yes** (never instrumented) | -- | **MEASURES -- genuine gap, needs new instrumentation** |
| 906c `residue_wanting` exact zero | -- | **yes** (orphaned writer calls) | -- | -- | **MECHANISM/plumbing, not REE** |
| 906c `liking` unbounded, mean=19.88 | -- | **yes** (shares excite's unclamped accumulator) | yes (not flagged as contaminated in the manifest) | -- | **MECHANISM+MEASURES (extends SD-RESIDUE-VALENCE-BOUND)** |
| 906b/906c coupling nulls replicate cross-seed | candidate | -- | -- | -- | **Strengthens the existing 906b Section-4 finding, still MIXED/uncertain per that section** |
| Bout-level analysis doesn't rescue step-level nulls | candidate | -- | possible (mode classifier / bout-boundary definition) | -- | **MIXED, corroborates existing `is_committed`=0 reading** |
| `explore` bouts are ~1-step blips in both runs | -- | -- | candidate (classifier threshold artefact) | -- | **Likely MEASURES, not investigated to closure** |
| Early-vs-late-segment "development" signal doesn't replicate across seeds | undetermined | undetermined | -- | **yes** (per-segment layout re-randomisation confound identified) | **ENVIRONMENT confound -- design gap, not evidence against development** |

No observation here is cleanly and solely "REE FAILED." The two REE-candidate rows (defensive-orienting
lockup, within-life development) are both flagged for further work rather than resolved either way.

---

## 9. Already-tracked vs novel (dedup against the 906b review and existing claims)

**Already tracked -- reference, do not re-register:**
- Affect->behaviour decoupling (906b review Section 4) -- 906c and this session's bout analysis both
  extend/corroborate it, not duplicate it.
- SD-RESIDUE-VALENCE-BOUND (excite contamination) -- already routed, pending `/governance`.
- MECH-439/F-dominance conversion-ceiling corroboration (906b review Section 11a/13-B) -- confirmed still
  `candidate` status, Track-B harvest reported inline but not yet applied to `claims.yaml` (per duplication
  check).
- SD-099/MECH-489 defensive-orienting mechanism -- already built and registered; V3-EXQ-910 is its
  validation result (Section 3), not a duplicate proposal.
- `sleep_substrate_plan.md` GAP-2 -- already tracked; its status table is stale relative to the V3-EXQ-909
  result (flagged as housekeeping, Section 4/10).

**Genuinely novel, recorded here for the first time:**
1. Exact code-level characterization of "continuous life" (Section 1) -- what persists, what resets, and
   that `health_depleted` is currently a recoverable event, not a terminal one.
2. Quantified censoring progression across the full lineage, culminating in V3-EXQ-911's zero deaths in
   8/8 segments (Section 2).
3. V3-EXQ-910 FAIL synthesis: near-zero ground-truth trigger alignment + the orienting_on 100%-withdraw
   lockup signature (Section 3) -- first read of this manifest anywhere.
4. V3-EXQ-909's "non-null" label decomposed: near-degenerate magnitudes, and the discovery that **no
   pre/post-sleep behavioural comparison exists anywhere in the collected data** (Section 4) -- a load-bearing
   instrumentation gap for the user's central sleep question.
5. Two new/extended measurement defects in 906c: `residue_wanting` orphaned-writer bug (novel), and
   `liking` sharing the unclamped-accumulator defect with `excite` (extends SD-RESIDUE-VALENCE-BOUND's
   scope, Section 5).
6. Bout-level analysis (Section 6) -- first attempt at this unit of analysis on this substrate; corroborates
   rather than resolves the step-level decoupling finding; new structural finding that `assert`/`shelter`
   dominate step-time while `approach`/`explore` are brief flickers.
7. Direct within-life early-vs-late-segment test (Section 7) with the specific identified confound
   (per-segment environmental re-randomisation) that currently prevents it from discriminating development
   from luck.

---

## 10. Proposed successors and follow-ons (NOT queued/built here -- mandatory-skill-path: `/queue-experiment`
for new runs, `/implement-substrate` for mechanism changes, `/failure-autopsy` for the two FAIL/gap items,
`/governance` for the Track-B harvest and plan-doc housekeeping)

1. **Uncensored survival design (new, directly answers the user's central lifespan question).** Instantiate
   REE once in the 906b/906c/911-tier survivable ecology and let it run until genuine `health_depleted`
   with NO step cap (or a cap far beyond anything currently observed), with resources regenerating and
   ordinary environmental dynamics continuing, to obtain an uncensored distribution of lived steps. Given
   Section 3's finding that `health_depleted` currently triggers a body-respawn rather than a true
   terminus, this design should **either** (a) explicitly decide and document that a body-respawn *is* the
   intended "death" unit for this measure (in which case report inter-respawn survival times, which the
   current substrate already supports without change), **or** (b) add an actual terminal-death branch for
   a dedicated long-run variant. This choice should be made explicitly, not left implicit as it currently
   is. **Duplication-checked: no existing queue entry, planning note, or claim proposes this** (Section
   confirmed via full-text search of `experiment_queue.json`, `substrate_queue.json`,
   `experiment_proposals.v1.json`, `docs/thoughts/`, and `evidence/planning/*.md`).
2. **Layout-controlled within-life development probe (new).** To separate genuine within-life learning from
   the per-segment environmental-randomisation confound identified in Section 7, either fix/pair the
   hazard-resource layout across segments within one run, or substantially increase segments-per-run (n=8
   is underpowered for any per-segment trend). This directly answers "does the same persisting agent
   improve over its own lived experience," which Section 7 could not resolve with current data.
3. **Post-sleep behavioural window instrumentation (extends V3-EXQ-909, not a duplicate).** Add a matched
   post-firing waking-segment record (route efficiency, hazard exposure, resource acquisition, action
   entropy) keyed to the same `(seed, boundary_index)` as 909's existing `sleep_firing_records`, so the
   user's "matched windows immediately before and after sleep" comparison becomes possible from data, not
   only from visual impression.
4. **`/failure-autopsy` on V3-EXQ-910.** Confirm which trigger implementation (naive absolute p90 vs the
   derivative/onset-detector design the 906b review specified) was actually built, and whether the
   100%-withdraw lockup is a calibration artefact of the same miscalibrated trigger or a separate
   architectural issue in the action-decision step.
5. **Top-N surprise-peak inspectability tool (new, user-proposed, no existing tool found).** Extract the
   top-N `residue_surprise` peaks from a lifetime's episode log and present the surrounding trajectory
   (~10-20 steps before/after: environment state, nearby entities, internal state, subsequent behaviour).
   No bout-segmentation or peak-inspection tool exists anywhere in `ree-v3/experiments/_lib/` or
   `REE_assembly/evidence/experiments/scripts/` today (duplication-checked). This is the direct empirical
   tool for testing the user's "surprise should reflect REE's prediction error, not the experimenter's
   judgement of event importance" framing, and for investigating the visually-salient jellyfish-appearing
   example.
6. **`/governance` housekeeping (small, inline per the governance-work exception, not chipped):** apply the
   Track-B MECH-439 corroboration harvest (still pending since the 906b review), and update
   `sleep_substrate_plan.md` GAP-2's status table to reflect the V3-EXQ-909 result.
7. **Cheap check, not a new experiment:** confirm whether MECH-357 (avoidance-efficacy eligibility learner)
   is active in the fishtank `_make_config()`, and if so, re-read the existing 906b/906c episode logs for
   its specific signature (earlier avoidance of a hazard type after being hurt by it) before proposing any
   new experience-specific-learning probe.

---

## 11. What this session did not resolve

- Whether the `explore`-mode ~1-step bout length (Section 6) is a genuine substrate limit on sustained
  exploration or a classifier-threshold artefact -- not investigated to closure.
- Why `dread<->z_harm_a` sign-flipped between 906b and 906c (Section 5) -- flagged, not explained; n=1 per
  run, cannot attribute to signal vs noise from available evidence.
- Whether MECH-357 is enabled in this ecology and what signature it would leave (Section 7/10.7).
- Whether the 906b ep6 mode-entropy dip (0.757 vs 1.2-2.3 elsewhere, noticed incidentally during the
  within-life analysis) has any relation to the run's one sleep-cycle firing -- the 906b review places the
  sleep firing at the boundary before ep7, not ep6, so this was not asserted as sleep-related and is left
  as an unexplained single-run observation.
- The intended design question raised by Section 1 (should `health_depleted` be a true terminus for at
  least one experimental variant) -- flagged for explicit `/governance`/design decision, not decided here.
