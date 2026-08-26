# Thought-digestion wave 2 — DRAFTS FOR REVIEW (nothing applied)

**Date:** 2026-08-26 · **Session:** `insights-7fd98a-digestion`
**Status:** STAGED ONLY. No `claims.yaml` write made. Dispositions are the user's call.
**Claims:** MECH-464, MECH-465, ARC-134, MECH-519, MECH-520
**Method:** 5 parallel read-only agents; orchestrator sole writer; every load-bearing code
finding independently re-verified by the orchestrator before being recorded here.

---

## 0. THE CROSS-CUTTING FINDING: REE's compression sites are systematically UNTRAINED

Three independent agents, on three unrelated claims, each found the same shape. Verified:

| site | what it is | training status |
|---|---|---|
| **O** (`action_object_head`) | SD-004's action-object bottleneck, `ao_dim << world_dim`, searched by the CEM | **zero gradient from every REE path** (SD-080); frozen random projection; 99.5% of variance explained by the action label |
| **z_beta / z_theta / z_delta** | ARC-004's higher-order latent stack -- "the latent field" | **`beta_encoder`/`theta_encoder`/`delta_encoder` appear ZERO times in `agent.py`.** No loss, no optimiser, no predictive head at any horizon. An untrained random-projection cascade smoothed by ONE hardcoded shared EMA (`alpha_shared = 0.3`, `stack.py:1454`) |
| **any value objective -> encoder** | the "carve by usefulness" path | does not exist. The only value-shaped loss, `compute_benefit_eval_loss`, reads `z_world.detach()` (`agent.py:10302`) and trains `E3.benefit_eval_head` ONLY |

**This reframes the whole 2026-08-26 thought.** The user's diagnosis was "higher level latents
may be more abstract but without there being a funnel they are not necessarily compressed to
extract useful representative values." The measured situation is **worse and simpler**: the
funnels exist structurally -- a bottleneck at O, a depth cascade at z_beta/theta/delta -- and
**none of them is trained toward anything at all.** It is not that abstraction fails to become
compression; it is that there is no learning pressure on the abstraction in the first place.

**Consequence for ARC-004 specifically:** the claim that depth = timescale has **never been
measured**, and ARC-004's own `what_would_answer` records that it could fail exactly as MECH-058
did (retired on V3-EXQ-019 lag-k autocorrelation). If z_delta's autocorrelation half-life does
not exceed z_theta's exceeds z_beta's, then "across the temporal spread" names ONE timescale
wearing three labels -- and with all three encoders untrained and sharing one EMA constant,
that is the outcome to expect rather than a remote risk.

---

## 1. MECH-464 (D1/D2 order-changing) -- recommended (c) `substrate_conditional`

**Mechanism CONFIRMED** at `e3_selector.py:2103-2120` (claim's refs `:1553-1570` are ~550 lines
stale), applied at `:2274-2284` to `assoc_accum`/`limbic_accum` only. All four flags land through
`from_dims`.

**WHY IT SAT UNRUN FOR FIVE WEEKS -- one false sentence.** The `evidence_quality_note` says "the
instrument (per-candidate accumulators) is the same one V3-EXQ-785a/785b already persist, so the
falsifier needs no substrate change." **Verified false:** 785a line 551 reads
`agent.e3.last_score_decomp["per_candidate"]` -- the **F-score component decomposition**, not the
loop accumulators `_d1_d2_split` operates on. `grep straddle` over `ree_core/` returns **nothing**.
The claim's own mandatory non-vacuity gate is **unmeasurable**. That sentence made the claim look
queueable, so nobody built the ~15 lines it needed.

**Two further defects:** (i) **there is no exogenous `da` knob** -- `da = math.tanh(_lcg_value_baseline)`
(`:2277`), written only under an ARC-108 learning flag, so the falsifier's literal "sweep `da`
exogenously" is not executable, and a run with learning flags off sits at the bit-identical point
and returns a spurious REFUTES. Reparametrise: sweep `d1_da_gain`/`d2_da_gain` at fixed non-zero
`da` -- same surface, and better, since it moves the gains independently. (ii) **the zero-straddle
case is EXACTLY NIL, not weak**: `_loop_normalize` is a plain zscore, invariant to positive affine
scaling, so without straddle `net` is a pure scalar multiple that the zscore cancels *identically*.

**Proposal design (EXP-0590), owed AFTER the readout lands.** Arms: `A0_DA_NULL` (gains=0, floor);
`A1_ASYM` (swept); **`A2_SYM_CONTROL`** (`d1_da_gain = g`, `d2_da_gain = -g` -> equal gains -> pure
positive scalar -> **predicts A2 == A0 exactly** by zscore cancellation -- the arm that earns the
claim); `A3_MAGNITUDE_MATCHED_NOISE`. Primary DV: `reorder_rate` against a **`da=0` shadow argmin**
recomputed at the same tick -- an exact within-tick counterfactual rather than a between-arm
trajectory comparison. Preconditions: straddle >= 0.05, `|da| >= 0.01`, `d2_gain == 0` saturation
excluded (loop *silencing*, not reordering), and an expressivity positive control.

**Scoping trap:** `substrate_queue` entry `v4_loop_segregation` carries a governance hold
(2026-08-21) on the 709/711/713 **conversion-lift** question. MECH-464 is a different question
(expressivity). It must be worded as an expressivity probe and must **not** tag ARC-110/MECH-439
or claim a conversion DV, or it reads as a `713x` re-letter and is refused.

**Incidental defect:** `v3_exq_785a` line 593 writes `loop_d1_d2_conflict_signal` into a per-tick
field literally named `"da"`. Any reanalysis reading that column as dopamine level is wrong.

---

## 2. MECH-465 (commit-gate boundary) -- recommended (a) TESTABLE NOW; `substrate_conditional` is WRONG

**Ceiling CONFIRMED and understated.** On medians the gated quantity sits **47-68x** below its
bound (the claim's "25-48x" came from manifest means inflated by warmup rows); only 0.35-1.6% of
ticks have margin >= 0.5.

**The decisive observation the claim does not make:** median `commit_variance` is **flat at
0.00561-0.00564 across all six urgency levels** (0.5% span). Arousal moves the **bound**; nothing
writes the **gated quantity**. There is no wire.

**STALE AS OF THIS MORNING:** `ree-v3` `2023589` (2026-08-26T06:58Z, "fix SD-011 urgency-modulation
sign inversion on commit threshold") changed `threshold * (1 - urgency)` to `* (1 + urgency)`.
The claim quotes the DESCENDING table (0.3761 -> 0.2570) as proof the manipulation landed; current
`main` produces an ASCENDING threshold, so saturation gets **worse** with arousal.

**THE TAUTOLOGY, which is the load-bearing finding.** Because urgency moves only the bound while
the gated quantity is provably flat, a boundary-regime run asking "does commit rate vary with
urgency?" returns SUPPORTS **arithmetically**, from the shape of the running-variance CDF, for any
non-degenerate dispersion. **Running the claim's own falsifier as written would trade a
ceiling-effect FALSE NULL for a TAUTOLOGICAL FALSE POSITIVE -- the same defect, inverted.**

**Mandatory third conjunct:** build the counterfactual commit rate from the OFF-arm's empirical rv
CDF evaluated at each shifted threshold, and score only the **residual** (observed - predicted).
A residual of zero means "arousal slid the bound and nothing else happened", which is exactly what
MECH-463 must be distinguished from. Without conjunct 3 the experiment is not worth running.

**Reachability is CLOSED on recorded data:** `commitment_threshold ~ 0.0057` (set
post-construction; it does not land through `from_dims`) puts the gate inside the quantity's own
dispersion -> commit-rate span ~0.60-0.95 versus 785a's 0.0099, **35x more headroom**. Boundary
regime = `complicated (buildable)`; making the result interpretable = `mystery (known data)`
(the residual reframe needs no new run).

**ORCHESTRATOR CORRECTION -- one agent finding DISCOUNTED.** The agent reported that
`update_running_variance`'s caller is orphaned, concluding "the gate never fires; every tick is
uncommitted." **False.** It searched for a method named `update()`; the enclosing method is
`post_action_update()`, which IS wired at `agent.py:9992`, called **every step**, guarded only by
`_current_latent is not None`, with a comment recording that a previous harm-gated version "caused
rv deadlock". The gate fires normally.

---

## 3. ARC-134 (perceptual regranularisation) -- recommended (c) KEEP as registered

**The operator does not exist.** `object_file_buffer.py` has only `_birth`, `_enforce_capacity`,
`_evict_stale` -- **no merge, no split anywhere**. So `obf_n_active_tokens` measures the
ENVIRONMENT's entity count, not the agent's carving, and the perceptual analogue of ARC-070's
`decompose_sequence()` is absent. **This is the largest disanalogy with the policy axis**, where
the operator was BUILT (2026-07-24) *before* the claim was scored -- and it caps how much authority
the ARC-069 transfer argument can lend.

**The naive falsifier is worse than assumed -- three rungs, and rung 1 is VACUOUS.**
L1 VARIABILITY (unit count varies within a fixed scene) is **already trivially true**: births,
deaths and TTL evictions vary it with no regranularisation at all. L2 CONTINGENCY: grain moves in
the PREDICTED DIRECTION under a demand manipulation, with a selectivity check against a
structural-zero OFF arm. L3 NON-RANDOMNESS: beat a **yoked, rate-matched random-regrain control**
(same event count, same ticks, random targets) on MECH-126's overmerge/oversplit pair --
**versus the yoked arm, not versus OFF**, because ON-vs-OFF confounds "regrained at all" with
"regrained informatively".

**MY §9.9d STEP-2 RECOMMENDATION IS UNDERCUT** (the "MECH-288 two-scale arbitration probe, no
ephaptic content required"). Three verified reasons: (i) **largely already run** -- V3-EXQ-830
(2026-07-27, PASS/`non_contributory`, `claim_ids: []`) is the scale-resolved probe:
`on_n_sweeps_slow_only: 0`, `on_n_sweeps_cofire: 0`, `on_n_sweeps_with_slow: 0` across 2393 sweeps,
label `slow_never_fires_on_rollout`, suspected cause a near-static `z_goal` (`z_goal_enabled`
defaults False); (ii) **"nothing arbitrates" is BY DESIGN** -- every consumer keys on
`(scale, segment_id)` and both scales are maintained in parallel as separate region keys, so there
is no place an arbitrator would sit; (iii) **wrong axis** -- MECH-288's grain is along TIME, while
ARC-134 is about carving a SCENE; ARC-070 could borrow the segmenter because a policy IS a
sequence, and a percept has none. Retain the step as **instrument de-risking**, relabelled.

**Also:** ARC-069's own preconditions are still unmet (`use_e3_reselection_shortcircuit` referenced
by **zero** experiments), so the parent commitment is itself untested.

---

## 4. MECH-519 (epistemic value is episode-borne) -- recommended (c) KEEP, but NARROW the title

**THE PREMISE IS REFUTED AS LITERALLY WORDED.** `causal_grid_world.py:458-470` ships defaults
`resource_type_names=("food","water","novelty")`,
`resource_type_drive_axes=("hunger","thirst","curiosity")`, a `novelty_decay` benefit curve, and
per-cell familiarity dynamics that write it. **The axis, the object type, and a write rule all
exist as DEFAULTS.** The claim's "there is no environmental epistemic benefit-pulse to bind to an
object identity, and hence no natural write rule" is false.

**The narrower claim survives:** the available pulse is a **visit-count novelty proxy**, not
gain x need -- disqualified by the Carey 2019 constraint MECH-519 itself inherits from MECH-443.

**It is a two-way claim over a THREE-way space.** V3 actually implements a **global agent-level
scalar** carrier (MECH-314c feeds `e3._running_variance` into the curiosity LP EMA,
`agent.py:8874-8878`) -- neither episode- nor object-indexed. A global-scalar null arm is therefore
mandatory: if it matches both indexed arms, the carrier question is **unanswered**, not confirmed.

**Distinct from MECH-443 only in the NEGATIVE half.** The positive half ("the quantity is
gain x need on transitions") is verbatim MECH-443's premise, which MECH-519's notes explicitly
*inherit*. The non-redundant content is the denial that SD-057/SD-049 can carry it -- a different
module and write site, logically independent. Narrow the title to that, or the redundancy is
re-litigated every governance cycle.

**Also:** `implementation_phase: v4` is inconsistent with its deps (MECH-443/444 are both v3) and
with the substrate (both candidate carrier sites are landed V3 code, default-off).

---

## 5. MECH-520 (predictive obligation as anti-collapse) -- recommended (c) KEEP as registered

**Preconditions (a) and (b) are the headline and are in §0 above:** no value objective reaches any
encoder, and the ARC-004 higher-order latents have no gradient path at all. Both arms this claim
needs must be BUILT.

**SD-070 IS NOT MECH-520 IMPLEMENTED -- SD-070 IS MECH-520's MATCHED-CAPACITY CONTROL.** This is
the structural insight that makes the falsifier non-vacuous. SD-070's anti-collapse term is
`variance_covariance_penalty()` -- a **purely statistical** constraint (per-dimension std hinge +
off-diagonal covariance) on a **static single-frame** encoder, with no temporal content and no
horizon. MECH-520 asserts the work is done by **cross-horizon prediction**. Different mechanisms
for the same job -- so `CTRL_VAR` is not a control someone must invent, it is `ZWorldP0Trainer`
with its grounding heads swapped.

**And SD-070 got PR from 1.06 to ~5.1 with NO temporal term at all** -- direct existing evidence
that falsifier branch F4 (a generic variance penalty suffices, and MECH-520 is a redescription of
SD-070) is live rather than hypothetical.

**`CTRL_H1` is the other load-bearing arm:** restrict the predictive obligation to k=1. It
separates "prediction" from "prediction ACROSS HORIZONS", which is the only thing MECH-520 adds
over the incumbent single-step E1/E2 losses and the only thing its ARC-004 dependency buys.

**Three citation defects in the claim as registered:**
1. **INV-091's "measurable quantity" is NOT missing** -- `_cross_stream_similarity_stat` and
   `_anti_collapse_stat` are both instrumented (`v3_exq_827...py:268,:279`) and have been run four
   times. Worse, **INV-091 is empirically weakened 3/3** (`genuine_exp_direction_counts
   {weakens: 3, supports: 0}`, `experimental_confidence 0.372`). Citing it as the frame MECH-520
   completes leans on a claim REE's own runs push against.
2. **The MuZero intake carries nothing usable** -- `REE_convergence/sources/muzero/` has ZERO hits
   for `value.equivalen|Grimm|bisimulation|Ferns|collapse|reconstruction`. CDQ-005's extraction
   target was replay write-gating, a different lane. "Already an intake lane, so translation not
   import" is wrong.
3. **MECH-006 in `depends_on` does no work** and invites the misreading that a serotonin knob is
   the proposed mechanism. Demote to a cross-reference.

**One relevant lit entry exists and is mis-filed for this purpose:**
`targeted_review_e2_forward_model_action_divergence/.../contrastive_rssm_srivastava2021` (conf 0.68)
reports contrastive next-state prediction outperforming **reward-divergence-based bisimulation** --
MECH-520's thesis at k=1, and *only* at k=1, which is precisely why `CTRL_H1` is load-bearing.

---

## 6. Summary

| claim | recommended | headline |
|---|---|---|
| MECH-464 | **(c)** + build ~15-line readout, then EXP-0590 | one false sentence in `evidence_quality_note` made it look queueable for 5 weeks |
| MECH-465 | **(a)** -- `substrate_conditional` is wrong | its own falsifier is a tautology as written; needs a residual DV |
| ARC-134 | **(c)** keep | no merge/split operator exists; naive falsifier's rung 1 is vacuous |
| MECH-519 | **(c)** keep, NARROW title | premise refuted by SD-049 defaults; two-way claim over a three-way space |
| MECH-520 | **(c)** keep | SD-070 is its CONTROL, not its precursor; three citation defects |
