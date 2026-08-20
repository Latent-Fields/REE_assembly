---
title: "Probe: does the E1/E2/E3 control-plane ladder realise the designed 1:3:10 timescale separation?"
status: "structural evidence in hand; empirical measurement QUEUED, not yet run"
as_of: 2026-08-20T06:34:48Z
claim_ids: [INV-013, ARC-004, ARC-023, SD-006]
chip_ref: chip-20260820-probe-realised-e-ladder-timescale-separation
queued_experiment: V3-EXQ-942
queued_commit: ree-v3 cb095c78
---

# Probe: does the E1/E2/E3 control-plane ladder realise the designed 1:3:10 timescale separation?

**Status: STRUCTURAL findings below are established facts (source-verified, not run-dependent).
The EMPIRICAL autocorrelation measurement is QUEUED as V3-EXQ-942 (`ree-v3` commit `cb095c78`,
pushed to `origin/main`) but has NOT YET RUN — see "What this does NOT license concluding" and
"Operator handoff" below before treating any number here as a governance-grade result.**

## The distinction this probe exists to test

**Design intent (settled, not re-derived here):** the E-loop ladder (E1=sensorium/gamma-analog,
E2=action-enacting/beta-analog, E3=planning-gates/theta-analog) was deliberately built in
mimicry of EEG bands, documented in
[`docs/architecture/control_plane_heartbeat.md`](../../docs/architecture/control_plane_heartbeat.md)
(ARC-023, SD-006). `ree-v3/ree_core/heartbeat/clock.py`'s `MultiRateClock` defaults confirm the
designed tick ratio directly: `e1_steps_per_tick=1`, `e2_steps_per_tick=3`,
`e3_steps_per_tick=10`, `theta_buffer_size=10` — **E1:E2:E3 = 1:3:10**.

**Realised dynamics (the open question):** does the *running system* actually exhibit three
separated timescales in its own state, or do the three loops end up with a similar effective
persistence despite their different clock rates? A designed rate ratio does not guarantee a
realised timescale ratio — coupling, shared smoothing constants, and shared inputs can wash it
out. `claims.yaml` already documents one collapse of exactly this shape: MECH-058 predicted a
z_self/z_world "timescale separation" and was directly falsified by lag-k autocorrelation
(V3-EXQ-019, 2026-03-17) — the layers differ in *content*, not timescale, and the retirement note
says explicitly "ARC-004 could suffer the same fate." ARC-004's own non-degeneracy caveat records
that L-space's `z_beta`/`z_theta`/`z_delta` layers share a single EMA constant
(`alpha_shared=0.3`), so their "multi-timescale" character (if any) is carried by recursive
structure, not by a per-layer clock rate. This probe asks the same question of the **E-loops**
specifically (E1/E2/E3's own control-plane state), which had never been measured before this
session.

## Route taken: (c), queue a new experiment — with strong structural evidence gathered first

Per the dispatching brief's routing decision, existing evidence was checked before writing
anything new (GOV-REUSE-1):

- **`v3_exq_827a_inv091_cross_stream_similarity_band_phase_sync`** (named as the closest prior
  art) — checked its run pack
  (`evidence/experiments/v3_exq_827a_.../runs/.../{manifest,metrics,summary}.json`): **aggregate
  cross-stream-similarity statistics only, no raw per-step state arrays are persisted anywhere**.
  Same pattern confirmed on `v3_exq_627_mech306_sustained_drive_trace_validation`. This is the
  general manifest convention in this codebase — raw trajectories exist only in-memory during a
  run and are not banked to disk — so no experiment's existing manifest can answer this question
  by reanalysis.
- **`claim_probe_mech_058/runs/20260317T232028Z_v3_exq_019_timescale_v3_v3`** (MECH-058, now
  retired) — the one genuinely relevant partial prior-art run. It measured `z_self`
  (E2's domain) vs `z_world` raw/reafference-corrected (E1's domain) lag-k autocorrelation
  directly, using EXACTLY the methodology this probe reuses. But: (a) it recorded **no E3 signal
  at all**; (b) it used **RANDOM actions**, not `agent.select_action` — E3's own
  selection/commitment machinery was never exercised; (c) it **failed its own C4** (`n_steps=969
  < 3000`, single seed); (d) it predates the 2026-07-12 Experimental Recording Standard (no
  `substrate_hash` — unverifiable-substrate reuse per GOV-REUSE-1's own pre-standard caveat).
  **Not recoverable as a full answer, but its numbers are genuinely informative and are reported
  below.**

So: **not recoverable → route (c)**, a new queued experiment. `V3-EXQ-942`
(`v3_exq_942_inv013_e_ladder_realised_timescale_separation.py`) was authored via `/queue-experiment`
end-to-end (substrate readiness check, re-derive brake check, substrate-path overlap gate, code
review checklist, `validate_experiments.py --strict` clean, smoke-tested), committed and pushed
to `ree-v3` `origin/main` (`cb095c78`). **It has not run** — this box (`ree-cloud-5`) has no
`REE_assembly/coordinator.env`, so the coordinator-ingress POST (`/queue-experiment` Step 8.6)
could not be issued; the entry is durably on `origin/main` but unrunnable by the fleet until a
coordinator-capable box (the Mac) POSTs it from this commit. See "Operator handoff" below.

## Three structural findings (established by reading the current substrate source — NOT run-dependent)

These are code-level facts about the *wiring*, verifiable independent of any stochastic
measurement, and they bear directly on why the realised-dynamics answer is a priori more likely
to be "separation absent/non-monotonic" than "separation confirmed":

1. **`ticks["e2_tick"]` is dead code.** `ree_core/heartbeat/clock.py:143,174` computes it every
   `MultiRateClock.advance()` call (`global_step % e2_steps_per_tick == 0`), but it is **never
   read anywhere in `ree_core/`** — confirmed by exhaustive grep across the tree. No code path
   gates any computation on E2's own tick flag. The designed 1-in-3 E2 cadence exists as a clock
   counter and nowhere else. (The one textual hit for `e2_tick` outside `clock.py`,
   `agent.e2_tick(latent)` in `v3_exq_669_mech329_wanting_first_goal_seeding.py`, is an unrelated
   method name — no such method exists on `REEAgent` at all; that call site does not correspond
   to the clock's tick flag.)

2. **The entire LatentStack is re-encoded every env step, regardless of loop identity.**
   `ree-v3/experiments/_lib/stream_recorder.py:310-317` documents this directly (a 2026-07-26
   finding from the Q-081/V3-EXQ-824 investigation): `z_self`, `z_world`, `z_beta`, `z_theta`,
   `z_delta`, `z_harm`, `z_harm_a` are all logged with the note *"LatentState field; re-encoded
   every step (E1 rate)"*. This applies equally to **ARC-004's own L-space layers**
   (`z_beta`/`z_theta`/`z_delta`) — the representation-encoding rate carries no per-loop gating
   at all, for any of the seven latent channels.

3. **E3's own continuous control state also updates every env tick, not on its own cadence.**
   `ree-v3/experiments/_lib/stream_recorder.py:374-379` and
   `ree_core/predictors/e3_selector.py` (`update_running_variance`, called from
   `post_action_update` on **every** env tick via `agent.update_residue`, not gated to
   `e3_tick`) confirm that `precision` (`= 1/(running_variance+eps)`) and `running_variance`
   are mutated every env step. Only `commit_threshold` (static config) and
   `is_committed`/`committed_now` (the closure-latch-derived discrete flag,
   `get_commitment_state()`) are genuinely E3-cadence.

**Taken together:** of the seven-plus continuous state channels spanning E1/E2/E3 and L-space,
**none of the continuous representations are rate-gated by loop identity at all** — they are all
updated every env step. The *only* genuinely loop-paced signal identified anywhere in the
substrate is E3's **discrete** commitment/re-selection decision. This is the same collapse
already confirmed once (MECH-058/EXQ-019) and flagged as a live risk once (ARC-004's own
non-degeneracy caveat) — this probe finds it is not scoped to those two cases; it appears to be a
general property of how the current substrate wires state encoding versus loop cadence.

## Partial empirical evidence already on file (EXQ-019, underpowered, reported honestly)

From `claim_probe_mech_058/runs/20260317T232028Z_v3_exq_019_timescale_v3_v3/metrics.json`
(n=969 steps, single seed=0, RANDOM actions, no reafference/E3 signal):

| channel | mean |Δ| | autocorr lag=1 | autocorr lag=5 | autocorr lag=10 |
|---|---|---|---|---|
| z_self (E2 domain) | 0.0421 | **0.5235** | -0.0610 | -0.0192 |
| z_world raw (E1 domain) | 0.0532 | 0.3942 | -0.0322 | 0.0400 |
| z_world corrected (E1, post-SD-007) | 0.0554 | 0.4767 | -0.0379 | 0.0186 |

Two things worth naming plainly: (1) at lag 1, `z_self` (the nominally *faster* E2 domain) shows
*higher* autocorrelation than `z_world` raw or corrected — the opposite ordering from a naive
"world is slow, self is fast" reading; (2) by lag 5-10, **all three channels have decayed to
autocorrelation indistinguishable from zero/noise** — there is no persistence structure
differentiating them at the lags that would matter for a "monotonic ordering" claim. This is
consistent with, though not dispositive of (n=969, single seed, random-action policy), the
structural picture above.

## Method specified for V3-EXQ-942 (queued, not yet executed)

One `REEAgent` per seed (seeds 11/23/37, matching `v3_exq_827a`'s seed set for continuity),
phased P0/P1 warmup (`experiments/_lib/goal_pipeline_tier1.warmup_train` — the shared,
validated helper: E1 world model, E2 world-forward, E3 harm-eval head), then a frozen-policy
(`agent.eval()`, `torch.no_grad()`) eval rollout using the canonical
`sense → clock.advance → e1_tick → generate_trajectories → select_action` loop
(`StepHarness`, the same inner loop as `_lib.capability_eval.REEForwardPolicy` and
`v3_exq_827a`'s `_eval_pass` — so E3's real selection/commitment machinery is genuinely
exercised, unlike EXQ-019's random-action design). Per step: read `latent.z_world`/`z_self`
(E1/E2's own state) and `agent.e3.get_commitment_state()` (E3's own continuous state:
`precision`, `running_variance`, plus the discrete `is_committed` flag). Compute per-step
deltas (episode-boundary-reset, matching EXQ-019's own convention), lag-k autocorrelation
(`_compute_autocorr`, EXQ-019's implementation reused verbatim), and a persistence half-life
(smallest lag where autocorrelation crosses 0.5× its lag-1 value) per loop per seed. Also tally
realised tick-fire counts (`e1_tick`/`e2_tick`/`e3_tick`) to report the measured tick-rate ratio
directly against the designed 1:3:10, and `is_committed`'s own mean run-length as a second,
more directly interpretable persistence read for the one channel that *is* genuinely
E3-paced.

**Pre-registered PASS/FAIL criterion** (ARC-004's own wording, applied to the E-loops instead
of L-space's latent layers, quoted verbatim in the script's own module docstring):

> "monotonic ordering of effective persistence... by a margin exceeding cross-seed noise (>=
> 0.8 SD of the seed-to-seed half-life delta)... ANSWER 'layers differ in content, not
> timescale' (FAIL) if autocorrelation half-life is statistically indistinguishable."

`EXPERIMENT_PURPOSE = "diagnostic"` — excluded from governance confidence/conflict scoring by
purpose; the run is a probe, not itself a promotion/demotion input.

**Readiness/degeneracy machinery:** a `p0_readiness_gate` asserts (worst seed) both a minimum
step count (>=3000, clearing EXQ-019's own unmet C4) and non-trivial per-step delta variance
for all three channels before any verdict is computed, self-routing to
`substrate_not_ready_requeue` otherwise. Verified live during authoring: a tiny 2-episode smoke
correctly self-routed not-ready (n=40); a larger single-seed smoke (5 warmup / 21 eval episodes
— well below the production 40/25 settings) reached `n_steps_total=2950`, just short of the
3000 floor, correctly self-routing not-ready again. This is expected and reassuring, not a
defect: production settings (40 warmup vs. 5, ~93% more eval budget) give a materially better-
trained, more survival-capable policy and should clear the floor comfortably. The
`_monotonic_verdict`/`_halflife`/`_run_length_stats`/`_compute_autocorr` functions were
additionally unit-tested directly against synthetic monotonic and non-monotonic per-seed data,
both branches computing correctly.

## Realised tick ratio vs. designed 1:3:10

**Not yet measured empirically for V3-EXQ-942's own config** (the run hasn't executed), but
structurally guaranteed to match 1:3:10 essentially exactly, because `e1_tick`/`e2_tick`/
`e3_tick` are literally the clock's own modulo counters (`ticks[k] += 1` tallied directly from
`StepResult.ticks`, per-seed, in the script) — there is no mechanism by which they could drift
from the configured rates over a full run. **The tick-rate ratio being exactly as designed is
precisely why it is uninformative on its own**: finding #1 above (`e2_tick` is dead code) means
that ratio governs nothing about representation update rate. The interesting number is not
whether the clock ticks at 1:3:10 (it does, by construction) — it is whether the loops' *state*
shows a matching persistence ratio, which findings #2 and #3 predict it will not.

## What this probe licenses concluding — and what it does not

**Licensed now, from structural evidence alone (source-verified, not run-dependent):**

- The E1:E2:E3 = 1:3:10 tick ladder is real at the clock-counter level, and governs E3's
  discrete commitment/re-selection cadence.
- It does **not** currently gate any continuous representation-update rate anywhere in the
  substrate — not E1/E2/E3's own domains, and not L-space's `z_beta`/`z_theta`/`z_delta`
  layers either. This is a general property of the current wiring, not scoped to one channel.
- The one prior direct measurement of this shape (EXQ-019, E1-vs-E2) is consistent with (though
  underpowered to confirm) a lack of realised persistence-timescale separation between the two
  fastest loops.

**NOT licensed until V3-EXQ-942 actually runs:**

- No quantitative half-life, autocorrelation value, or monotonicity verdict for the properly-
  exercised E1/E2/E3 comparison (with E3 genuinely engaged via real action selection, adequate
  sample size, and multiple seeds) exists yet. The structural findings above predict the likely
  *direction* of that result; they are not a substitute for it.
- This probe does **not** promote or demote INV-013, ARC-004, ARC-023, or SD-006. That is a
  `/governance` decision to be made from whichever evidence — structural and/or, once run,
  empirical — accumulates here.
- **This document is not itself a governance-grade evidence artifact for V3-EXQ-942's own
  result** — only the run's own manifest is, once it exists.

## Operator handoff (Step 8.6 could not complete on this box)

`ree-cloud-5` has no `REE_assembly/coordinator.env`, so `POST /queue/add` could not be issued.
The entry is durably on `ree-v3` `origin/main` but **unrunnable by the fleet** until a
coordinator-capable box (the Mac) POSTs it:

```bash
# On a box with REE_assembly/coordinator.env (the Mac).
set -a; . /Users/dgolden/REE_Working/REE_assembly/coordinator.env; set +a
ITEM=$(git -C /Users/dgolden/REE_Working/ree-v3 show cb095c78:experiment_queue.json \
  | /opt/local/bin/python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps({'item': next(i for i in d['items'] if i.get('queue_id')=='V3-EXQ-942')}))")
curl -s -m 8 -X POST -H "Authorization: Bearer ${COORDINATOR_LOCAL_TOKEN}" \
  -H "Content-Type: application/json" -d "$ITEM" "${COORDINATOR_URL}/queue/add"
```

Once run, the next reader should: (a) pull the manifest's `monotonicity_verdict` and
`realised_tick_ratio_per_seed` blocks directly, (b) check `interpretation.label` for
`substrate_not_ready_requeue` (readiness gate fired — re-queue rather than trust the result) vs.
a genuine `e_ladder_realised_timescale_separation_confirmed` / `..._layers_differ_in_content_not_
timescale` verdict, and (c) route the result to `/governance` for any claims.yaml disposition —
this session deliberately makes none.
