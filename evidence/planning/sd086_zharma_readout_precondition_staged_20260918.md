# SD-086 `z_harm_a` readout -- decode-precondition probe: REFUSED at design, with measurements

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or any other registry).**

- Session: `metaworker-science-20260918-sd086-zharma-readout` (headless, campaign `science-20260918-sd086-zharma-readout`)
- Chip: `chip-proposal-exp-1222-paced` | Claim: **SD-086** | Proposal: **EXP-1194** (`EVB-1666`, experimental)
- Recorded: 2026-09-18T18:52:06Z
- Outcome: **no experiment queued.** The pre-registered precondition cannot discriminate as written. Decision chip raised.

---

## 1. What was asked

The chip's pre-flight (AMBER, `cranky-wiles-c85265`, 2026-09-17) named one change that would turn
AMBER into GREEN: run SD-086's own `non_degeneracy_precondition` as a cheap decode probe first.
Verbatim:

> The z_harm_a LATENT must itself carry decodable cross-state information -- a linear decode of
> behavioural mode or harm-event status from z_harm_a must clear a floor with non-zero cross-seed
> variance. If the latent is uninformative the readout form is not the defect and the run
> self-routes substrate_not_ready.

The pre-flight's reasoning rested on this premise, verbatim: *"A norm that is flat while the vector
is informative is precisely SD-086's thesis."*

**That premise is measurably false in this claim's own scope.** Details below.

## 2. Chip preconditions -- all verified, all clear

| Check | Result |
|---|---|
| `implementation_phase` still v3 (not moved to v4/v5) | v3 |
| SD-086 has no completed run | absent from `claim_evidence.v1.json` |
| Gate claims SD-087 / Q-086 have reported (claim `notes`) | both carry autopsy evidence |
| Open *corrupting* `substrate_queue` entry blocking the path | none; SD-086's own entry is `pending_implementation`, `ready:false` (the trained-head build, correctly routed to `/implement-substrate`, not here) |
| GOV-REUSE-1 (Step 2.4) | **not recoverable -> run.** No manifest anywhere records a 16-d `z_harm_a` decode |

GOV-REUSE-1 detail, since it is independently informative: across 1045 scanned manifests, 71 carry
a `z_harm_a` readout and **every one of them is norm-derived** (`z_harm_a_norm` x1004,
`max_z_harm_a_norm`, `z_harm_a_mean_norm`, ...). The two vector-sounding keys are not vectors:
`cov_z_harm_a` is a scalar float, and `z_harm_a_trajectory` is `list[300]` (per-tick norm, not
300x16). The entire recorded evidence base reads this latent through its norm -- which is itself a
corroboration of SD-086's framing, and the reason the decisive readout had to be run rather than
reused.

## 3. The AMBER caveat: RESOLVED, and the V3-EXQ-642d root cause named

The pre-flight flagged V3-EXQ-642d (W5-S2a, 2026-09-08): `z_harm_a` was `None` on **400/400 ticks**
with `use_affective_harm_stream` set, and that session "could not name what else the producer needs".

**Named.** `z_harm_a` is non-`None` iff BOTH the flag is set AND the driver actually forwards
`obs_harm_a` into `encode()`. `ree_core/latent/stack.py:1612`:

```python
if harm_obs_a is not None and self.affective_harm_encoder is not None:
```

`act_with_split_obs()` does **not** forward `obs_harm_a`; `agent.sense(..., obs_harm_a=...)` does.
This is already recorded in-tree as the fix in
`experiments/v3_exq_603a_...py:16,214` ("Fix1: select_action() path with obs_harm_a").

Measured this session: **30/30 ticks non-`None`**, shape `(16,)`, per-dim std across ticks
0.0032 / 0.0542 / 0.1220 (min/mean/max). The producer is healthy; 642d was a driver-path defect.

## 4. The three measurements that refuse the design

All from the standard raw-warmup configuration SD-086's `scope_note` scopes itself to
(`CausalGridWorldV2(use_proxy_fields=True)`, `scaffold_train_harm_pathway` off).

### 4a. `harm_obs_a` has EXACT rank 2 -- structural, training-invariant

`ree_core/environment/causal_grid_world.py:3037-3038` writes one scalar into 25 dims and a second
into the other 25:

```python
self.harm_obs_a_ema[:25] = (1-a)*self.harm_obs_a_ema[:25] + a*hazard_at_agent
self.harm_obs_a_ema[25:] = (1-a)*self.harm_obs_a_ema[25:] + a*resource_at_agent
```

Measured over 500 ticks: singular values `[22.597, 6.698, 0, 0, 0, 0]`; **numerical rank 2**;
exactly **2 distinct column patterns**; `col0==col24`, `col25==col49`. The 16-d `z_harm_a` is a
function of a rank-2 input and can never carry more than 2 independent d.o.f. about the world.
Correspondingly `z_harm_a` puts **97.1%** of its variance in PC1 and **99.8%** in PC2.

### 4b. The affective encoder is NEVER TRAINED on the standard path

`experiments/_lib/allon_training.py:541-548` builds optimizers over `agent.e2`, the lPFC bias head
and the OFC devaluation head only. Measured by parameter-identity intersection:

```
latent_stack param tensors            : 53
affective_harm_encoder param tensors  : 4
latent_stack params COVERED           : 0
affective encoder params COVERED      : 0
AFFECTIVE ENCODER REACHABLE BY TRAINER: False
```

The aux loss that *could* train it (`agent.compute_harm_accum_loss`) returns `zero_loss` unless
`harm_accum_pred` exists, which requires `harm_history_len > 0` (default 0; the env emits no
`harm_history` by default) -- and it is called by exactly one non-standard driver
(`_lib/baselines/exq610_inv074_crystallization_baseline.py:538`), not by the standard trainer.

This is the **same defect the repo already records for the sibling `z_world` stream** at
`allon_training.py:475-476`: *"cover NO latent_stack parameter ... z_world stays a frozen random
projection -- measured 0 of 61 latent_stack"*.

So in SD-086's own scope, `z_harm_a` is a **frozen random projection of a rank-2 signal**.

### 4c. The norm is NOT flat -- it tracks the signal at r = 0.9885

Measured over 500 ticks at that frozen projection:

```
corr(||z_harm_a||, hazard_EMA) = 0.9885
||z_harm_a||: mean 1.06707  std 0.12501  (cv 0.117)
```

## 5. Why the pre-registered precondition cannot discriminate

The precondition asks whether a linear decode from the 16-d vector clears a floor. Given 4a-4c it
**will clear, trivially and vacuously**: a random projection of an informative scalar is linearly
decodable. But the **norm decodes the same signal at r=0.9885**, so clearing says nothing about
SD-086's actual thesis -- that the norm *conflates a large near-constant offset with a small
functional component*. In this regime the norm retains the component.

A CLEAR verdict would therefore license the expensive two-arm trained-head build on evidence that
does not support it. In the skill's own vocabulary this is a `vacuous_pass`; in the Step 4.5
red-team table it is *"the criterion cannot discriminate by construction"*. It is exactly the
"confident-but-wrong verdict -> building the wrong substrate" failure the campaign brief warns of.

**Scope discipline, stated rather than overclaimed:** none of this shows SD-086 is false. A trained
scalar head could still be better *calibrated* than the norm. What is shown is that the
**precondition as written cannot distinguish that**, in the configuration the claim scopes itself to.

## 6. The decision required (raised as a decision chip)

Fixing this means changing the load-bearing criterion, which determines the route -- the user's call
under the consent rule, not this session's. Options, with what each would measure:

- **A. Hazard-context median split (literal-ish reading).** Balanced 48/52 by construction, but a
  monotone function of the encoder's own dominant input channel -- near-tautological. Would CLEAR
  vacuously and route to the expensive build.
- **B. "Harm-event status" at a balance-chosen threshold.** The harm scalar is *signed*: prevalence
  is 2.75% at `h>0` and 83-88% at `h<-0.01`. No balanced threshold exists without inventing one,
  and the threshold sets the decode's difficulty and hence the verdict.
- **C. RECOMMENDED -- re-specify as a vector-vs-norm contrast.** Load-bearing criterion becomes
  *"does a linear decode from the 16-d `z_harm_a` beat a decode from `||z_harm_a||` alone, beyond
  the cross-seed noise band?"* This is SD-086's thesis operationalised directly; it **cannot clear
  vacuously** (both readouts see the same latent); it is cheap (no trained head needed); and it
  self-routes correctly -- vector ~ norm weakens the premise and correctly avoids the build, vector
  >> norm justifies it.
- **D. Route to SD-011 / re-specification first.** Treat 4a+4b as the answer: a frozen random
  projection of a rank-2 input is not a substrate on which a *readout-form* question is meaningful.

## 7. Second-order finding (a FINDING, not a decision)

The rank-2 bottleneck (4a) bounds **any** readout of `z_harm_a` -- norm or trained head -- at 2
d.o.f. That bears on SD-086's proposed *remedy*, not only its precondition, and on **SD-011**
(whether the affective stream encodes what it is claimed to). Recorded here and in the governance
flag; not acted on.

## 8. Reproduction

Probes under this session's worktree `scratch/` (throwaway, not committed):
`probe_zharma_liveness.py` (3), `probe_rank.py` (4a, 4c), `probe_optcover.py` (4b),
`probe_labels.py` / `probe_labels2.py` (5/B label balance). All read-only; no run, no queue entry.
