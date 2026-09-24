# MECH-288 slow scale: the BOCPD rail is unreachable in-agent by arithmetic

**Status: FINDINGS RECORD + REFUSAL. No claim status, confidence, queue entry or manifest was
changed by the session that wrote this. EXP-1388 is recorded as refused with a named blocker;
no experiment was queued.**

- Session: `metaworker-science-20260924-orchb-mech288-boundary-anchor` (headless, ree-cloud-4)
- Campaign: `science-20260924-orchb-mech288-boundary-anchor`
- Written: 2026-09-24T13:34:17Z
- Part 1 (the in-agent liveness measurement): [`mech288_exp1388_inagent_slow_scale_liveness_20260924.md`](mech288_exp1388_inagent_slow_scale_liveness_20260924.md), REE_assembly `a576b2a819`; GFLAG-0468.

## Summary

Part 1 measured MECH-288's slow/outer BOCPD scale firing ZERO times on the agent observation
path and framed the open question as `complex (probe-gated)`: *does a WARMED agent's z_goal
stream ever cross the rail?* The user ratified running that probe (option (b), decision chip
`chip-20260924-mech288-slow-scale-inert`).

The probe was authored (V3-EXQ-1096), passed `validate_experiments.py --strict`, and passed its
dry-run smoke. It was then **REFUSED at the mandatory adversarial red-team design review with a
BLOCKING verdict**, and the refusal is correct: the question is not probe-gated at all. It is
`puzzle (known rules)`, the missing rule is detector arithmetic, and the answer follows from the
source without running anything.

**The slow scale cannot fire on the in-agent observation path, for reasons that have nothing to
do with z_goal liveness, warmup, or the benefit gate.** Every step below was verified against
source by this session, independently of the reviewer that raised it.

## The arithmetic

### 1. The Bayesian posterior route is dead by construction

`_BOCPDGaussianDetector.step` builds the new run distribution as

```
growth_i = P_i * exp(pred_log_i) * (1 - hazard)        # event_segmenter.py:315-318
cp_prob  = sum_i P_i * exp(pred_log_i) * hazard        # event_segmenter.py:320-323
new_run_probs = [cp_prob] + growth                     # event_segmenter.py:327-328
total = sum(new_run_probs); new_run_probs /= total     # event_segmenter.py:343-352
fired = p_zero > posterior_threshold                   # event_segmenter.py:378-384
```

Let `S = sum_i P_i * exp(pred_log_i)`. Then `cp_prob = S*hazard` and `sum(growth) = S*(1-hazard)`,
so `total = S` and

```
p(r=0) = S*hazard / S = hazard,  IDENTICALLY, for every observation.
```

The likelihood terms cancel exactly. With the canonical slow-scale config
(`hazard = 1/40 = 0.025`, `posterior_threshold = 0.5`; `config.py:2283`, `:2307`), `p_zero` is
**0.025 on every tick regardless of the data**, and `0.025 > 0.5` is never true. Top-k pruning
(`top_k = 20`, `:2308`) cannot rescue it: at most one run is pruned per tick, so renormalisation
moves `p_zero` by a negligible factor, and if `r=0` is itself pruned the lookup raises and
`p_zero` is set to `0.0` (`:379-382`) -- still no fire.

So the posterior path NEVER fires, on any stream, in-agent or otherwise.

### 2. The only live route is the implausibility fast path, and its cutoff is 6.178

```python
if pred_log and max(pred_log) < -20.0:        # event_segmenter.py:303-312
    ... return True, 1.0, sources
```

The run created at the previous tick is always present with `n = 0`, so `n < 2` and it falls back
to `var = prior_var = 1.0` (`:257-260`), with `mu` = the previous tick's aggregate. Its predictive
log-prob is therefore `-0.5 * (ln(2*pi) + d^2)` where `d` is the one-tick change in the aggregate.
`max(pred_log) < -20` requires in particular that this run be below `-20`, so

```
ln(2*pi) + d^2 > 40   ->   d > sqrt(40 - ln(2*pi)) = 6.1775
```

is a NECESSARY condition for any slow-scale fire. (The `total <= 0.0` underflow branch at `:344-352`
is a strictly more extreme version of the same condition.)

**What `d` is.** The BOCPD does not read the z_goal vector. It reads its SCALAR NORM:

```python
agg += float(z_d.norm().item())               # event_segmenter.py:282
```

So `d = | ||z_goal(t)|| - ||z_goal(t-1)|| |` must exceed 6.1775 in ONE tick.

### 3. The z_goal write rule cannot produce that step

`GoalState.update` is the sole writer:

```python
self._z_goal = self._z_goal * (1.0 - decay_goal)                       # goal.py:871
if effective_benefit > benefit_threshold:
    self._z_goal = (1 - alpha_goal) * self._z_goal + alpha_goal * z_w  # goal.py:912-919
```

with `alpha_goal = 0.05` and `decay_goal = 0.005` (`goal.py:29`, `:33`). The per-tick norm change is
bounded by `0.005*||z_goal|| + 0.05*||z_world - 0.995*z_goal||`, so a single-tick crossing of 6.1775
needs roughly

```
||z_world|| >= 6.1775 / 0.05 = 123.6
```

### 4. The measured scale is ~400x short

V3-EXQ-830's landed manifest (`evidence/experiments/v3_exq_830_mech321_scale_resolved_rollout_boundary_20260727T204927Z_v3.json`,
5 seeds) records the live z_goal stream at

```
zgoal_norm_mean 0.110 - 0.163      zgoal_norm_max 0.209 - 0.305
```

The required ONE-TICK jump (6.1775) is ~20x the largest value `||z_goal||` ever attains across that
whole run, and the `||z_world||` it would take (~124) is ~400x the observed goal-norm scale. This is
not a margin that warmup, a longer run, more seeds, or a more open benefit gate can close.

### 5. Independent corroboration from the one run that ever fired this scale

V3-EXQ-757 is the only experiment that has ever fired MECH-288's slow scale, and it did so 27/27.
Its planted levels are

```python
GOAL_LEVELS = [5.0, 15.0, 25.0, 10.0, 20.0, 30.0]    # v3_exq_757_...functional.py:154
```

Consecutive gaps are 10, 10, 15, 10, 10 (and 25 on the wrap) -- **every one above 6.1775**, and none
below. The driver's own comment says the gaps were "chosen to hit BOCPD's decisive rail". That is
this cutoff, found empirically. It also explains the GFLAG-0452 D1 cluster autopsy's finding that
the smooth arm's silence was by construction: at `GOAL_NOISE = 0.02` the arm is ~300x below the rail,
so 0 fires was arithmetically guaranteed.

## What this means

- **MECH-288's slow/outer scale has no reachable firing route on the in-agent observation path.**
  Precondition (1) of its own `what_would_answer` ("boundary fires > 0 on BOTH scales") cannot be
  satisfied in-agent as the substrate stands. The fast scale fires (measured: 2/499 and 2/236 in
  Part 1), so the hierarchy reduces to a single scale in practice.
- **EXP-1388 is unrunnable as designed** -- its primary criterion C1 is defined on the slow scale.
- **The Part 1 framing needs one correction, recorded here rather than quietly dropped.** Part 1
  attributed the zero to the z_goal stream being absent or constant, and named the open question as
  whether warming would make the stream live. That attribution is incomplete: even a fully live
  stream at the measured scale cannot fire this detector. Part 1's measurements stand; its causal
  story was one layer too shallow.
- **The node was mis-classified.** Part 1 called it `complex (probe-gated)`. It is
  `puzzle (known rules)` -- the missing fact was the detector's cancellation identity and its -20-nat
  cutoff, obtainable by reading the code. The probe would have spent ~150 minutes of fleet time to
  return a RED already derivable on paper, and would have reported it with the WRONG mechanism
  attached ("the live stream is N-fold below the rail", implying a stream/warmup remedy).
- **Consumers are affected, and this is not adjudicated here.** MECH-269 anchor sets, MECH-284
  staleness accumulators and MECH-287 broadcasts are all keyed on `(scale, segment_id)`. They still
  receive fast-scale boundaries, so they are not silent -- but the outer/slow index never advances
  in-agent, so every in-agent segment id has outer = 0. What that does to those claims is a
  governance question, not this session's call.

## Disposition

- **No experiment queued.** V3-EXQ-1096 was authored, passed `validate_experiments.py --strict` and
  passed its dry-run smoke, then was refused at red-team (BLOCKING) and NOT queued. The EXQ id was
  released. The driver was deliberately NOT committed to `ree-v3/experiments/`: an uncommitted,
  unqueued script there is a landmine for the next session's `git add`, and a committed one invites
  someone to queue a run now known to be futile. Its design is fully described in this document.
- **EXP-1388** recorded as refused via `record_proposal_refusal.py` with a named blocker (it was NOT
  left at `status: proposed`, so the standing blocked-proposal audit can see it).
- **Governance flag** raised carrying this arithmetic.
- **No remedy chosen.** Changing the stream the slow scale reads, its `prior_var`/`hazard`/
  `posterior_threshold`, or the `alpha_goal` write rule each changes what MECH-288 IS -- the claim
  commits to "BOCPD-Gaussian latent change-point on the slow scale (z_goal)". That is a claim-level
  `/implement-substrate` + governance decision and is explicitly NOT taken here.

## Reproducing

All five legs are static reads plus arithmetic; no run is needed.

```
ree-v3/ree_core/hippocampal/event_segmenter.py:282, 303-312, 315-323, 343-352, 378-384, 257-260
ree-v3/ree_core/goal.py:29, 33, 871, 912-919
ree-v3/ree_core/utils/config.py:2283, 2300-2310
ree-v3/experiments/v3_exq_757_mech288_mech287_event_boundary_trigger_functional.py:154
REE_assembly/evidence/experiments/v3_exq_830_mech321_scale_resolved_rollout_boundary_20260727T204927Z_v3.json
python3 -c "import math; print(math.sqrt(40.0 - math.log(2*math.pi)))"   # 6.177549913484362
```

## Provenance

The BLOCKING finding was raised by the mandatory Step 4.5 adversarial red-team pass
(`/queue-experiment`), run on Fable against an Opus-authored design, and every load-bearing leg was
then re-verified against source by the authoring session before being acted on. The red-team pass
is a candidate practice registered with a falsifier ("if after ~10 uses no CONTESTED or BLOCKING
finding has survived verification, remove this step"); this is one surviving BLOCKING finding, and
it prevented a 150-minute run whose recorded conclusion would have named the wrong mechanism.
