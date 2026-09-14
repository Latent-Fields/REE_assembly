# MECH-439 rung 3 (SD-E3-CHANNEL-COMMENSURABILITY): the re-posed selection-level target,
# specified for /queue-experiment to build

**Generated:** 2026-09-14T16:17:19Z
**Session:** `metaworker-chip-20260911-mech439-rung3-target-repose`
**Chip:** `chip-20260911-mech439-rung3-target-repose`
**Discharges:** the residual of GFLAG-0234 (RESOLVED, `governance_flags.v1.json`) this chip was cut
for -- see "Correction to the chip's own premise" below.
**Ratified direction (unchanged by this record):** `governance_flag_adjudication_20260909.md`
GFLAG-0234 option A, user-approved 2026-09-10.
**Predecessor design record:** `exq1012_blocked_readiness_target_tautological_20260908.md`
(the tautology proof; section 4 there names this DV as candidate 1, "the natural falsifier").
**Parked driver to build from:**
`ree-v3/experiments/_scratch/v3_exq_1012_e3_commensurability_regime_validation.py.blocked`
**Claim:** MECH-439. **Its direction does not move on this record** -- nothing here says the
operator does or does not work, only what a validatable target for it looks like.

---

## 0. Correction to the chip's own premise -- the doc amendment is ALREADY LANDED

The chip brief states "its registry half landed in the gov-flagbacklog-20260909 adjudication,
this half [the doc amendment] did not." That is **stale**. Verified directly against source: the
same commit, `REE_assembly 5dc661badc` ("governance: apply 26 user-approved decision-docket
flags (gov-flagbacklog-20260909)", 2026-09-10T07:53:17+01:00), already carries the full
four-carrier amendment --

- `docs/architecture/sd_e3_channel_commensurability.md` line 178
- `evidence/planning/failure_autopsy_V3-EXQ-571c_2026-09-02.md` line 98-103
- `evidence/planning/failure_autopsy_V3-EXQ-571c_2026-09-02.json` (`targets[0].failure_record_entry.target`)
- `evidence/planning/substrate_queue.json` (both the `failure_records` row at line 6062 and the
  `readiness_target_measured` field at line 6203)

-- each preserving the original tautological target verbatim and appending an `AMENDED
2026-09-10 (/governance GFLAG-0234, option A, user-approved)` block that states the SAME
selection-level replacement this record specifies precisely: "a SELECTION-level DV -- commit-flip
rate under shadow OFF/ON scoring on the same tick and the same candidate set." **So the target
text is already re-posed everywhere it lives.** What is still genuinely owed, and what this
record and its follow-on chip actually discharge, is turning that already-ratified prose into a
**buildable, non-tautological instrument** -- the four carriers describe the DV, they do not
define it precisely enough to code against (no committed-vs-stochastic-tick restriction, no
non-forced-ness argument, no RNG-safety analysis, no PASS-gate discipline). That is this record.

---

## 1. GOV-REUSE-1 existing-evidence check -- NEGATIVE, a new run is required

Checked before designing anything further, per `/queue-experiment` Step 2.4. The only banked
data against this substrate are V3-EXQ-571c's manifest and the 1012 driver's own authoring
smoke. Both record **per-cell aggregates only** -- `xcand_share`, `xcand_var_mean`,
`xcand_top_channel`, `n_live_channels`, `final_commit_by_primary_frac` -- computed by consuming
`E3TrajectorySelector._last_traj_components` after each tick and then discarding it. Verified
directly against `per_seed_results[0]` in
`v3_exq_571c_e3_variance_monopoly_presence_936_regime_20260902T152856Z_v3.json`: no per-tick,
per-candidate raw score record exists anywhere in the manifest. Commit-flip rate needs, for every
genuine tick, the full per-candidate score vector recomputed under the **opposite** commensurability
setting from whichever one the run actually used -- a quantity that was never computed, let alone
recorded, because the tick that produced it is gone the instant `_last_traj_components` is
overwritten by the next candidate. **Nothing here is recoverable from banked data; this is
unlike the MECH-536/GFLAG-0233 sibling case, and a live run is genuinely required.**

---

## 2. An unplanned but load-bearing finding: the primary stage rarely decides the final commit

571c's own manifest (its 936-regime CONFIG_FLAGS carry
`use_modulatory_shortlist_then_modulate=True`, matched by the 1012 driver) records
`final_commit_by_primary_frac` per cell -- the fraction of genuine selections whose final
committed candidate coincided with the argmin of the **primary** (commensurability-affected)
score alone:

| arm | seed 42 | seed 43 | seed 45 | seed 46 |
|---|---|---|---|---|
| B1 fed+warmup (the 936 regime) | 0.0337 | 0.1461 | 0.0047 | 0.0396 |
| B2 starved+warmup | 0.0846 | 0.0197 | 0.0297 | 0.0414 |
| B3 fed, no warmup | 0.0683 | 0.0986 | 0.0619 | 0.0591 |
| B4 starved, no warmup | 0.0398 | 0.0493 | 0.0640 | 0.0392 |

The primary stage decides the final commit on **0.5-14.6%** of genuine selections; the rest are
decided by the within-shortlist modulatory-accumulator argmin, which the commensurability
operator does not touch directly. **A commit-flip DV computed only on the primary-stage argmin
would be measuring a stage that almost never determines the actual executed action** -- itself
close to a second, subtler version of the same defect class this record exists to fix (a
technically-non-tautological DV that is nonetheless answering the wrong question). Section 3
below therefore specifies the DV at the **final commit**, not the primary argmin, and treats the
primary-argmin comparison as a secondary/diagnostic readout only (matching the parked driver's
existing, already-recorded C6 `final_commit_by_primary_frac`).

---

## 3. The re-posed DV, precisely specified

### 3.1 Mechanism (verified against `ree_core/predictors/e3_selector.py`, current HEAD)

`E3TrajectorySelector.select()` computes, per genuine tick and in this order:
1. `raw_scores` -- one call to `score_trajectory()` per candidate (`e3_selector.py:3081-3090`).
   This is the **only** place the commensurability toggle enters: `score_trajectory` reads
   `self.config.use_e3_channel_commensurability` fresh on every call (`:1509`) and, when True,
   divides each channel's raw term by `self._commensurability_scale(name)`
   (`:1523-1525`), an EMA read-only lookup into `self._chan_scale_ema`.
2. The running scale estimate is updated **once per tick, after all candidates are scored**, by
   `_update_channel_scale_estimates()` (`:3099-3100`), and **only when
   `use_e3_channel_commensurability` was True for that call** (`_comm_on_sel`, `:3060`). Toggling
   the config **off** for a rescoring pass therefore cannot mutate `_chan_scale_ema` at all --
   confirmed at source, not assumed.
3. Downstream of `raw_scores` -- shortlist formation (`:3913-4009`, margin/top-k/F-demotion
   modes plus the optional Go/No-Go gate), the within-eligible modulatory-accumulator argmin, and
   the `committed` boolean (`:3880`) -- is a **pure, deterministic function of `raw_scores`** plus
   inputs the commensurability toggle does not touch (`score_bias`, `channel_route_bias`,
   `_modulatory_accum`, the Go/No-Go signals). No RNG draw sits between `raw_scores` and the
   final committed index **on the `committed=True` path** (the stochastic softmax-sample branch
   is the `committed=False` alternative -- see 3.3).

This is exactly the shape the codebase already uses once, for a different manipulation: MECH-464's
"da=0 shadow argmin" (`:2713-2744`, "an EXACT within-tick counterfactual... deliberately the core
argmin on BOTH sides, not the stochastic"). The design below is the same pattern applied to the
commensurability toggle instead of the `da=0` perturbation, not a new technique.

### 3.2 The measurement

At every genuine (fresh, per `FreshSelectProbe`) P1 selection tick in an **ON** arm
(`C2_fed_operator_on`, `C4_starved_operator_on`) whose live `last_score_diagnostics["committed"]`
is `True`:

1. The **live** reading is already available: the actually-committed candidate index under
   commensurability ON, and `raw_scores` (already computed that tick).
2. Immediately after, with no env step or training step in between, temporarily set
   `agent.e3.config.use_e3_channel_commensurability = False`, recompute `raw_scores_shadow` by
   calling `score_trajectory()` on the **identical candidate list** (same `Trajectory` objects,
   same tick, same `_chan_scale_ema` state -- read-only, unaffected per 3.1.2), then restore the
   flag to `True` immediately. This never touches any state the live trajectory's continuation
   depends on.
3. Re-run **only** the deterministic downstream stretch (shortlist -> Go/No-Go -> within-eligible
   modulatory argmin -> commit-vs-sample gate) a second time, substituting `raw_scores_shadow` for
   `raw_scores` and holding every other live input from that tick fixed (`_modulatory_accum`,
   `score_bias`, `channel_route_bias`, Go/No-Go signals -- none of which the toggle affects).
   `/queue-experiment`'s build pass must isolate this stretch into a callable the live `select()`
   and the shadow pass both invoke, rather than re-deriving it inline, so the two paths cannot
   silently drift apart.
4. `final_commit_flip = 1` iff the shadow-recomputed final index differs from the live
   final index; else `0`. `xcand_commit_flip_rate` per cell = mean over all genuine
   `committed=True` ticks in that cell.

Recorded per cell, alongside the existing per-tick counters: `n_committed_ticks_scored`,
`n_flips`, `xcand_commit_flip_rate`, plus the secondary/diagnostic `primary_argmin_flip_rate`
(argmin of `raw_scores` vs `raw_scores_shadow` alone, no downstream replay -- cheap, and useful
for reading C6 `final_commit_by_primary_frac` against this record's own numbers).

### 3.3 Design rule (b) applied -- the harness's own blind spot maps to UNDETERMINED

Per the discipline `[memory] feedback_effect_size_pass_gate_margin` and the MECH-536 precedent
("a detector's blind spot must map to UNDETERMINED, never to a negative"):

- A tick where `select()` did not run at all (held/latched, per `FreshSelectProbe`) is already
  excluded by the existing fresh-selection gate -- unchanged.
- A tick where `select()` ran but `last_score_diagnostics["committed"]` is `False` (the
  softmax-sampled branch) is **UNDETERMINED for this DV**, not "no flip." Replaying that branch
  under a shadow score would require redrawing the same random sample without perturbing the live
  RNG stream, which is not safely reproducible -- reported and counted separately as
  `n_stochastic_ticks_excluded`, never folded into the flip-rate denominator as a false zero.
- A cell whose `n_committed_ticks_scored` falls below a pre-registered floor is UNDETERMINED for
  readiness, not a `0%`/`100%` flip-rate reading -- add a `PreconditionSpec` for it alongside the
  existing `decomp_samples_sufficient` one, scoped (`applies_to`) to the ON arms only, matching
  how `n_live_channels` is already scoped in the parked driver.

### 3.4 Harness self-check (bug detector, not a design-rule-(a) control)

Before trusting any real cell, the build's smoke test must include a **shadow==live config**
self-comparison (toggle to the SAME setting, i.e. shadow config = ON when live is ON): this MUST
read `xcand_commit_flip_rate == 0.0` exactly, on every tick, by construction (bit-identical
inputs, bit-identical deterministic replay). A nonzero self-comparison flip means the shadow
replay has drifted from the live path (missed a live input to the deterministic stretch) and the
run must refuse rather than report real numbers -- an assertion, not a routed criterion.

### 3.5 Design rule (a) applied -- the non-forced-ness argument

Two independent grounds, one algebraic and one empirical, per the discipline the MECH-536 sibling
case established (a replacement criterion is only admissible with evidence the manipulation does
not force its value):

**Algebraic.** The old target failed because `Var(term/s)/Var(term) = 1/s^2` **identically**, for
any data, whenever `s` is (an EMA of) `sqrt(Var(term))` itself -- a self-normalisation identity.
Commit-flip rate has no analogous closed form. Differentially rescaling channels by *different*
positive factors is **not** argmin-invariant in general (only a *common* positive rescaling of
every channel is, per the driver's own DV-symmetry declaration) -- but neither is it forced to
flip: whether an argmin changes depends on where each candidate's channel terms sit relative to
each other, which is data, not an identity of the rescaling operation. There is no algebraic
identity of the form "commit_flip_rate ~= constant" the way there is for a normalised share.

**Empirical (the natural control the metaworker brief asks for).** The manipulation being
measured is the ON/OFF toggle; the "pair that differs in the thing the claim is about but shares
the manipulation" is the **fed vs. starved regime**, both scored under the identical toggle
mechanism. 571c measured structurally different raw channel-magnitude relationships in the two
regimes (fed: `residue_weighted` variance ~452 vs `harm_weighted` ~0.005; starved: a different,
flatter relationship -- `xcand_share` in the 0.994-0.9998 range for the dominant channel rather
than fed's 0.98-0.99999). **If commit-flip rate were a forced identity of the toggle alone, it
would read the same in both regimes**, since both undergo the identical manipulation. Report
`xcand_commit_flip_rate` for C2 (fed) and C4 (starved) separately (the parked driver already
splits its ablation pairs this way) and treat a difference between them as the evidentiary check;
a run reporting numerically equal flip rates in both regimes independent of the actual channel
data would itself be evidence of a hidden identity and should be treated as BLOCKING at red-team,
not reported as a clean result.

---

## 4. PASS-gate discipline (per `[memory] feedback_effect_size_pass_gate_margin`)

Do not pre-register a numeric flip-rate floor now -- there is no run to derive one from yet. The
build must instead pre-register the **method**: PASS requires
`xcand_commit_flip_rate > max(K * SD_seeds(xcand_commit_flip_rate), ABS_FLOOR)` where `SD_seeds`
is the empirical matched-seed dispersion measured from this run's own seeds (the same worst-cell
discipline the parked driver already uses via `_worst_cell`), `K` a small integer (2-3, chosen at
build time against the smoke test's actual seed spread), and `ABS_FLOOR` a small absolute rate
(order 1%, so a single-seed fluke against near-zero dispersion cannot pass). This scales the bar
on the SD of the delta plus an absolute floor, per the standing discipline, rather than inventing
a number with no data behind it.

---

## 5. What this run validates and does not

Validates: whether the commensurability operator has a selection-consequential effect --
i.e. whether "which channel holds authority" (the property MECH-439/ARC-062 need) is a genuine
contest over the **executed action**, not merely over a post-hoc variance-share bookkeeping
statistic. Still `EXPERIMENT_PURPOSE = "diagnostic"`, still promotes nothing, still answers only
whether the readiness precondition is met -- not whether any downstream conversion improves.

---

## 6a. Build-time scoping addendum (2026-09-14, same session -- recorded before writing code)

Section 3.2 specified the DV at the **final commit** (post-shortlist, post-modulatory-argmin),
restricted to `committed=True` ticks to keep the shadow replay RNG-free. Building that requires
either refactoring `e3_selector.py`'s post-`raw_scores` stretch (shortlist -> Go/No-Go ->
modulatory argmin -> commit gate, `:3913-4009` and neighbouring blocks) into a shared callable, or
hand-duplicating ~150 lines of that logic inside the experiment driver and auditing it
line-by-line against source on every future `e3_selector.py` change. Both are `ree_core` surface
changes or maintenance liabilities disproportionate to a `diagnostic` readiness probe, and exactly
the kind of scope this skill's own guidance prefers to avoid inside an experiment script.

**What is actually built (V3-EXQ-1012a): the PRIMARY-stage argmin flip, not the final-commit
flip.** At every genuine (fresh) P1 selection tick in an ON arm, immediately after the live
`raw_scores` is computed (commensurability ON), toggle `use_e3_channel_commensurability` to
`False`, recompute `raw_scores_shadow` over the identical candidates via `score_trajectory()`
alone (source-verified side-effect-free per section 3.1.2 -- confirmed again by a live probe this
session: the OFF pass never mutates `_chan_scale_ema`, and rescoring ON afterward reproduces the
EMA state and the original scores exactly), restore ON. `primary_argmin_flip = 1` iff
`argmin(raw_scores)` differs from `argmin(raw_scores_shadow)`. This needs **no `committed=True`
restriction** -- unlike the final-commit stretch, `argmin` of a fixed score tensor has no RNG in
it, so every genuine tick is usable, not just the deterministic-commit subset.

This is the same shadow-argmin PATTERN the codebase already uses once (the MECH-464 `da=0`
precedent, section 3.1) applied at the level the operator directly acts on, and it is what the
ratified GFLAG-0234 target text ("commit-flip rate under shadow OFF/ON scoring on the same tick
and candidate set") most directly and safely supports without new `ree_core` surface. Report
`final_commit_by_primary_frac` per cell alongside it (already computed by the parked driver) as
mandatory interpretive context, and state explicitly in the script docstring and manifest that
this DV characterises PRIMARY-stage authority -- whether the operator's rescaling changes which
candidate the commensurability-affected score alone would prefer -- not a claim about the executed
action on cells where the modulatory shortlist stage dominates (which section 2 shows is most of
them). **The self-check (3.4) and the fed/starved non-forced-ness check (3.5) apply unchanged** at
this level -- both are just as meaningful for the primary argmin as for the final commit.

**Follow-on, not built here:** a small `E3TrajectorySelector` helper exposing the deterministic
post-`raw_scores` stretch as a shared callable, so both `select()` and a future final-commit-level
shadow probe can call it without duplication. Chip this as `/implement-substrate` work if a future
session wants the final-commit-level reading; do not hand-duplicate the shortlist/Go-No-Go/
modulatory-argmin logic inside an experiment driver to get it.

## 6. Build guidance for `/queue-experiment`

Reuse wholesale: `ARMS`, seeds, env, `config_slice_for`, `_make_agent`'s knob-survival assertion,
the OFF-arm control-reproduces-monopoly gate (step 1 of `_adjudicate_ablation`), the
operator-engaged gate (step 2), and the exposure recording (`_scale_estimates`). **Replace**:
`_adjudicate_ablation`'s content-reading step 3 (currently `n_live_channels >=
COMMENSURABILITY_TARGET_N_LIVE`) with the flip-rate routing in section 3 above, keeping the
control/engaged gates as the load-bearing pre-checks they already are (a drifted regime or an
inert operator must still route `substrate_not_ready_requeue` before any flip-rate content is
read). **Add**: the shadow-rescoring hook inside `run_cell`'s per-tick loop (requires either a
small `E3TrajectorySelector` helper exposing the deterministic post-`raw_scores` stretch as a
callable -- preferred, since it forces the live and shadow paths to share one implementation and
cannot drift -- or, if that refactor is out of scope for this driver, a faithful reproduction
audited line-by-line against `e3_selector.py:3913-4009` at build time); the
`committed`-vs-not split (3.3); the self-check assertion (3.4); the fed/starved flip-rate split
(3.5). Red-team focus per Step 4.5: confirm no RNG draw sits on the `committed=True` path between
`raw_scores` and the final index (audit `e3_selector.py` from the shortlist block through the
commit gate), and confirm the self-check (3.4) actually reads exactly zero in the authoring smoke
before trusting any other number the smoke produces.

ID: this is the same scientific question the parked `.blocked` driver asked (does the operator
lift the readiness condition), with only the acceptance instrument replaced -- per the EXQ
lettering convention ("bug fix / minor tweak... scientific question unchanged") this reads as a
lettered successor to V3-EXQ-1012 rather than a new number; `/queue-experiment` Step 2 is
authoritative on the final ID once current queue state is checked at write time.
