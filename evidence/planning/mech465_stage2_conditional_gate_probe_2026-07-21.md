# MECH-465 stage-2 probe: can the SD-063 conditional head grade the commit gate?

- **Date:** 2026-07-21T05:42:42Z
- **Session:** `strange-payne-281125` (MECH-465 stage-2 SD-063 conditional-gate probe)
- **Type:** SPIKE (stage-2 of the `complex (probe-gated)` node opened by the stage-1 spike).
  No experiment queued, no queue entry, no script in `ree-v3/experiments/`.
- **Substrate:** ree-v3 @ `f06067d` (hub `ree-worker-1`, torch 2.12.0+cpu)
- **Claim:** MECH-465 (`candidate` / `substrate_conditional`)
- **Predecessor:** `mech465_commit_gate_boundary_spike_2026-07-20.md` (stage 1)

## Verdict

**The SD-063 conditional gate does NOT make the commit gate gradeable in the deployment
condition. MECH-465 remains substrate-gated -- but the gate is NOT the thing to build.**

The stage-1 spike routed here on the reasoning that `E2WorldUncertaintyHead.predictive_variance`
is state-dependent by construction, and so should supply the dispersion the running-variance EMA
structurally lacks. Wired and trained, it was measured against the 1.455x urgency bar:

| Gated quantity / driver | dispersion p99/p1 | vs 1.455x bar |
|---|---|---|
| `_running_variance` (EMA), stage-1 spike | 1.024-1.069x | FAILS |
| `predictive_variance`, held-out, **uniform-random** actions | **1.9896x** | *apparently CLEARS* |
| `predictive_variance`, per-FIXED-action (z_world only) | 1.219-1.459x | worst FAILS, best marginal |
| `predictive_variance`, **CEM leading-candidate** actions (deployment) | **1.2473x** | **FAILS** |

The apparent CLEARS is a **driver artefact**. Under the uniform-random driver, **88.4% of the
dispersion is action-driven, not state-driven**. The deployment gate reads the CEM-selected
leading candidate's action, and the untrained CEM policy is near-degenerate -- so that component
collapses and the measured dispersion falls to 1.2473x.

This is the **informative null** the stage-2 brief anticipated, and it lands with a sharper
diagnosis than a bare null: both the EMA path and the conditional path fail, by two structurally
different routes, and both failures localise to the **same upstream cause -- the untrained
agent**.

## Method

Agent/env construction copied from `v3_exq_785a` (`CausalGridWorldV2(hazard_harm=0.5,
use_proxy_fields=True)`, harm + affective-harm streams, SD-056 contrastive candidates, finer
channel gating, `agent.eval()` -- UNTRAINED, as the whole 785a family is). world_dim=32,
action_dim=5 (note: **5**, not the `E2WorldUncertaintyConfig` default of 4 -- a literal default
would have mis-sized the head).

Head: `E2WorldUncertaintyHead(z_world_dim=32, action_dim=5)`, hidden 128, 9 quantiles (the
V3-EXQ-712 winner set). Adam lr 1e-3, 400 epochs, batch 256, final pinball **0.00188**
(converged: 0.00232 @ ep100 -> 0.00206 @ ep200 -> 0.00188 @ ep400). Trained P1-style on 1349
warmed seed-0 transitions with **both inputs and target detached** (the SD-031 agency-residual
stop-gradient discipline). Offline-to-convergence is deliberately the STRONGEST case for the
hypothesis; an online-trained head would be weaker, not stronger.

Three measurement streams, all on env seeds **not** used for training:
- **seed 1, uniform-random actions** (650 warmed ticks) -- held-out generalization.
- **seed 1, per-fixed-action** -- the confound decomposition (below).
- **seed 2, CEM leading-candidate actions** (250 ticks) -- the **deployment condition**, the
  number that actually governs MECH-465.

**Design economy carried from stage 1.** `predictive_variance` REPLACES `_running_variance` at
`e3_selector.py:2788-2792`, so the gate remains a pure comparison of two scalars. Recording pvar
per tick lets commit rate for ANY (threshold x urgency) pair be computed offline from one run --
one probe, not one job per candidate threshold.

**Driver economy, and the trap in it.** The 785a CEM path (`generate_trajectories` +
`select_action`) costs ~4.6 s/tick on a contended cloud worker; 2300 ticks is hours. Since pvar
dispersion is a property of the z_world transition stream, the expensive action-SELECTION can be
swapped for random actions while keeping the REAL frozen z_world encoder (`agent.sense()`,
~ms/tick) -- ~50-100x cheaper, and justifiable at the time as *favorable* to the hypothesis
(uniform actions visit more states than a hazard-avoiding policy). **That swap is precisely what
manufactured the CLEARS.** The economy was sound; the headline number it produced was not
transferable, and only the decomposition + the CEM confirmation revealed it. Recorded here as a
methodological warning: when a cheap driver substitution touches an INPUT of the measured
quantity, the substitution must be validated, not just justified.

## Findings

### 1. The head genuinely does carry more dispersion than the EMA -- but not where it counts

Held-out warmed pvar under uniform-random actions (n=650): mean 1.920e-04, CV 0.185,
p1 1.256e-04, p99 2.500e-04, **p99/p1 = 1.9896x**. Against rv's 1.024-1.069x this is a change in
kind, not degree: the state-blind EMA structurally cannot carry per-point signal
(`precision_error_corr ~ 0` by construction -- the V3-EXQ-712 null), and the quantile head can.

Under that driver the offline threshold x urgency sweep satisfies **both halves of the stage-1
boundary condition at once**, which stage 1 proved impossible for rv:

| | u=0.04 | u=0.10 | u=0.16 | u=0.22 | u=0.28 | u=0.34 | in-band |
|---|---|---|---|---|---|---|---|
| commit rate @ T=2.096e-04 | 0.519 | 0.451 | 0.379 | 0.300 | 0.165 | 0.065 | **6/6** |

median gate margin 1.062x (< 2x), all six levels strictly inside (0.05, 0.95), monotone
decreasing. **This is what the stage-1 routing hoped for -- and Findings 2-3 show it does not
survive contact with the real action distribution.**

### 2. 88.4% of that dispersion is ACTION-driven, not state-driven

Fixing the action and varying only z_world across the held-out random-driver stream:

| fixed action | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| p99/p1 across z_world | 1.459 | **1.219** | 1.352 | 1.369 | 1.415 |

Variance decomposition over the joint (tick, action) grid:
`between_zworld = 1.422e-10`, `between_action = 1.085e-09` -> **z_world share = 0.116**.

Only one of five actions clears the bar, and then marginally (1.459 vs 1.455). So the head's
advantage over the EMA is predominantly **action-conditioning**, not the "HIGH exactly where THIS
prediction is about to be wrong" state-conditional property SD-063 is advertised on and that
MECH-059 names.

### 3. THE DEPLOYMENT CONDITION -- CEM collapses both components at once

The gate reads `predictive_variance(z_world_t, a_t)` at the **CEM-selected leading candidate's**
action (`e3_selector.py:2783`). Measured directly (seed 2, 250 CEM ticks, same trained head):

- dispersion **p99/p1 = 1.2473x** (mean 1.106e-04, median 1.084e-04, CV 0.061) -> **FAILS**
- **CEM action distribution = [0.08, 0.00, 0.92, 0.00, 0.00]**
- per-fixed-action dispersion on CEM-visited states: [1.049, 1.046, **1.027**, 1.031, 1.035]
- **z_world variance share = 0.002 (0.2%)**

The untrained CEM policy commits to **one action 92% of the time and never selects three of the
five**. So the action-driven component -- 88% of the random driver's signal -- collapses. And
because that near-degenerate policy also stops exploring, the state-conditional component falls
*further still*, from 1.22-1.46x on random-driver states to **1.03x** on CEM-visited states
(share 0.2%, i.e. essentially nothing). Both sources of dispersion collapse together.

The offline commit sweep confirms the precondition is unmet:

| best T = 1.293e-04 | u=0.04 | u=0.10 | u=0.16 | u=0.22 | u=0.28 | u=0.34 |
|---|---|---|---|---|---|---|
| commit rate | 0.920 | 0.920 | 0.616 | **0.000** | **0.000** | **0.000** |

median gate margin 1.192x (< 2x, so the margin half is met), but three levels are pinned at
**exactly 0**. The MECH-465 mandatory precondition is "median gate margin < 2x **AND commit rate
away from both 0 and 1 across the urgency grid**" -- the second half fails. The shape is a
**plateau-then-cliff**, the same tie-dominated degenerate profile stage 1 found for the MECH-108
sweep: a usable *operating point*, not a usable *dose-response*. A Spearman rho over it is
degenerate.

### 4. A threshold-calibration non-stationarity the EMA path does not have in this form

In-sample (seed 0, training states) mean pvar is 3.82e-05 with dispersion 3.297x; held-out
(seed 1) is 1.92e-04 with dispersion 1.990x -- a **5.0x scale gap**. This is ordinary
generalization behaviour (the head fits training states tightly, widens on unseen ones), but it
has an operational consequence: **the absolute scale of the gated quantity drifts by ~5x as the
head trains online**, so a static `commit_threshold` calibrated early saturates late.

Stage 1 concluded that for rv "a discard-first-N-ticks burn-in is sufficient -- a
variance-tracking threshold is NOT required", because rv's 81-89x drift is front-loaded then
flat. **That conclusion does not transfer to the conditional gate**: this drift tracks the head's
training progress, not a fixed warmup transient. Any future stage-2a run on this path needs a
frozen (pre-trained, then fixed) head or a quantile-referenced/adaptive threshold.

### 5. Both gate inputs remain driver-supplied (stage-1 Finding 7, re-confirmed)

`update_running_variance()` still has no caller in `ree_core`, and `E2WorldUncertaintyHead` still
has **no call site in `agent.py`**; `conditional_predictive_variance` is never passed. Everything
above was produced by a driver constructing, training and reading the head itself, exactly as the
module docstring's usage example prescribes. Wiring it into the agent loop remains a small unbuilt
substrate change -- **and per this verdict it should NOT be built on current evidence.**

### 6. The near-degenerate action distribution is itself a finding

`[0.08, 0.00, 0.92, 0.00, 0.00]` over 250 CEM ticks is a monostrategy/lock-in signature in the
untrained selection path, independent of anything about the commit gate. It is recorded here
because it is (a) the proximate cause of the deployment-condition failure above, and (b)
consistent with the standing monostrategy-ceiling thread. It is a by-product of this probe, not
something the probe was designed to measure, and is not adjudicated here.

## What this does and does not establish

**Establishes.** Under the CURRENT untrained-agent driver family, *neither* gated quantity can
grade the commit gate: rv at 1.02-1.07x (stage 1), `predictive_variance` at 1.2473x in the
deployment condition (stage 2). Two structurally different quantities -- one a state-blind
temporal EMA, one a trained per-input conditional quantile head -- fail the same bar by different
routes. Swapping the gated quantity is therefore **not** the fix, which retires the stage-1
routing's preferred hypothesis.

**Does NOT establish -- and the stage-1 caution is REINFORCED, not discharged.** This is *not*
evidence that z_world cannot express the needed dispersion, and must not be cited as an
established substrate ceiling. Every measurement here is on an **untrained agent**
(`agent.eval()`, no optimizer, no backward), so z_world is a frozen random projection and the
policy is near-degenerate. The measured 0.2% z_world variance share is exactly what a frozen
random encoder driven by a monostrategy policy would be expected to yield. The counterfactual --
a trained z_world and a non-degenerate policy -- is **untested and untestable in this driver**.

What stage 2 adds to stage-1 Finding 6 is corroboration by an **independent route**: stage 1
inferred the frozen-encoder hypothesis from rv's near-stationarity; stage 2 shows that a
fully-trained head *designed* to carry per-point state signal recovers essentially none of it
(0.2%) on the states this agent visits. That moves the frozen-encoder reading from "flagged" to
"strongly corroborated" -- while leaving it, correctly, still a hypothesis about the *training
condition* rather than about z_world's expressive capacity.

## Routing

**Do NOT wire SD-063 into `agent.py`.** The stage-1 spike's recommended substrate entry ("wire and
train `E2WorldUncertaintyHead` and supply `conditional_predictive_variance` to `E3.select`") is
**superseded by this measurement**: the wiring would land a gate whose gated quantity disperses
1.2473x against a 1.455x manipulation, i.e. the same ceiling effect in a new mechanism. The build
is small and correct-looking, and would not help.

**Do NOT queue the stage-2a experiment.** Per MECH-465's registered `what_would_answer`, any
stage-2a run carries the mandatory precondition "median gate margin < 2x AND commit rate away from
both 0 and 1"; Finding 3 shows three of six urgency levels pin at exactly 0. A run queued now
would reproduce the 785a ceiling effect and be scored `precondition_unmet`. This is the stage-2b
outcome the claim text anticipates.

**The binding constraint is upstream: the untrained agent.** The productive lever is
**`sd_zworld_warmup_optimizer_group`** (`substrate_queue.json`, `implemented_pending_validation`,
priority 1, design doc `docs/architecture/sd_070_zworld_p0_anticollapse_recipe.md`), which
addresses exactly this defect -- its own failure record is "0 of 61 latent_stack tensors changed
after P0 warmup", across the same `_train_all_on_agent` driver family. It already has two
independent strikes (V3-EXQ-737, V3-EXQ-728) and blocks MECH-457 / INV-088 / Q-002. **MECH-465
should be re-probed by re-running this stage-2 instrument once a trained z_world is available**,
at which point BOTH gate paths (rv and conditional) become re-testable with the same offline
sweep, cheaply.

Note the ordering claim: this does not assert that a trained z_world WILL clear 1.455x. It asserts
that the question is not answerable until it is trained, and that the conditional-gate build
cannot substitute for that.

## Tension with the 2026-07-20 autopsies -- re-surfaced, and it still holds

The stage-1 spike recorded that both 2026-07-20 autopsies set
`recommended_substrate_queue_entry.action: none`, sound for the **variance-geometry** framing they
addressed but not for the **commit-gate** framing. That remains correct and is **not** discharged
by this stage-2 null. What changes is *which* substrate gap is named: stage 1 identified "lever 5
(SD-063) is unwired"; stage 2 measures that closing that gap would not help, and relocates the gap
to the z_world training path. So the commit-gate framing still carries live substrate work that
those autopsies did not adjudicate -- it is now a different, already-filed piece of work
(`sd_zworld_warmup_optimizer_group`) rather than a new one.

## Limitations

- **Untrained agent / frozen random z_world / near-degenerate policy** -- the dominant limitation,
  and the subject of the routing above rather than a caveat to be worked around.
- The CEM stream is **250 ticks, one seed**, and was evaluated with a head trained on
  uniform-action data. That train/test shift is in the *conservative* direction for the verdict:
  CEM-visited states are less well-fit, which widens and noisies pvar, so the true
  deployment dispersion is if anything **lower** than the 1.2473x measured. The verdict is FAILS,
  so a conservative bias cannot have manufactured it.
- Single environment (`CausalGridWorldV2`, `hazard_harm=0.5`), one head architecture (the 712
  winner), world_dim=32.
- The offline sweep assumes the gate is a pure comparison of the two recorded scalars. That is
  structurally what `e3_selector.py:2788-2792` does on this path (`use_harm_variance_commit` off),
  but it would not transfer to the harm-variance branch.
- Probe script lives in the session scratchpad, not landed: it is a spike instrument, and
  `/queue-experiment` owns anything belonging in `experiments/`.
