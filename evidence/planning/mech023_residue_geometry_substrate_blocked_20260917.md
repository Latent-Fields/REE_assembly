# MECH-023 ("Responsibility is geometric and path-dependent") -- SUBSTRATE-BLOCKED

- **Recorded:** 2026-09-17T21:16:49Z
- **Session:** `igw-242-proposal-for-mech-023` (IGW-20260917-242, lane `experiment`, skill `/queue-experiment`)
- **Proposal:** `EVB-1394` / `proposal_type: experimental` -> `status: blocked_substrate`
- **Outcome:** NO experiment queued. The design was built, reviewed, smoke-tested, and then
  refused at the Step 4.5 adversarial design review with a **BLOCKING** verdict. Both blocking
  findings were independently re-measured against the substrate before acting.
- **Claim status UNCHANGED** in `claims.yaml`. This document promotes nothing; it records why a
  falsifier that reads "testable now" is not in fact runnable, and what would make it runnable.

---

## 1. What was attempted

MECH-023's registered `what_would_answer` is unusually complete: fork a trained agent, drive
fork A through a harm-accruing path in region R and fork B through a harm-free path, bring both
to the same `z_world` with **bit-identical non-residue surfaces**, and read the **pre-sampling
E3 candidate ranking**. Add fork B' (equal harm mass in a distant region R') as the load-bearing
control, and a hypothesis-tagged fork H as the MECH-094 gate.

This is a commitment-free, measurement-only read, so it is the right shape for the current
substrate: it sits upstream of the known `f_dominance_conversion_ceiling`, which is a
COMMITTED-action conversion defect.

The driver was written to make the matched state exact rather than approximate: at each decision
point the candidate set is generated ONCE and the residue-free primary recovered as
`base_i = raw_score_i - residue_weighted_i` (the V3-EXQ-697 idiom), with every fork scored as
`base_i + rho * Phi_X(candidate_i)`. `base_i` is literally the same float for every fork, so F,
M, benefit, goal, bias and all network weights are shared by construction.

## 2. Step 2.5c gate: resolved in favour of running (recorded, because it reverses a shape argument)

`f_dominance_conversion_ceiling` (severity `corrupting`) names this driver's exact load-bearing
functions -- `e3_selector.py::score_trajectory`, `residue/field.py::add_residue`,
`residue/field.py::RBFLayer.forward`. A shape match would have stopped the work here.

The content audit says otherwise, and it is worth recording because the obvious reading is wrong:

- **V3-EXQ-936** reports a residue cross-candidate variance share of `1.5e-14 .. 1.2e-40`
  (`arm_results[].component_variance_fractions.residue_weighted`, ARM_OFF, seeds 42/43/45/46).
  That looks like total F dominance over the residue channel. It is **not**: 936's residue field
  was effectively EMPTY (`p1_mean_abs_harm` 0.003-0.098, no deliberate residue load). The number
  measures an absent field, not a swamped one.
- **V3-EXQ-697**, with a POPULATED field (`residue_populated: true`, coverage 100%, `mean_weight`
  2.5-54), measured `flip_intact_vs_zeroed` = **0.0596, 0.2986, 0.885, 0.8986, 0.9964**
  (mean 0.628, 5 seeds, 160k rows). Residue changes the pre-sampling argmin on most decisions.

So residue does reach selection, and the ceiling does not by itself block this DV.
**The block is elsewhere, and it is structural.**

## 3. The two blocking substrate facts (measured 2026-09-17)

### 3a. CAPACITY -- the residue field is a 32-slot ring buffer, so it cannot hold a "path"

`RBFLayer.add_residue` (`ree_core/residue/field.py:165-180`):

```
idx = self.next_center_idx.item()
self.centers.data[idx] = location                              # OVERWRITE
self.weights.data[idx] = self.weights.data[idx] + intensity    # add onto whatever was there
self.next_center_idx  = (self.next_center_idx + 1) % self.num_centers
```

`num_basis_functions = 32` under `REEConfig.from_dims` (the constructor every driver in this
lineage uses; only `.large`/`.xlarge` override it). Harm fires on a large majority of steps in
the reef config, so the ring wraps continuously.

Measured on the driver's own config (seed 42, 720 steps, `harm_gradient_scale=0.30`):

| quantity | value |
|---|---|
| harm steps | 450 / 720 (62.5%) |
| `num_harm_events` | 895 |
| `num_centers` | 32 |
| **ring wraps** | **28.0** |

Two consequences, both fatal to the registered design:

1. **There is no "add a divergent harm history" operation on a trained agent.** Injecting N fork
   events does not extend the history; it **relocates the N most recently written centres** to
   the fork's region while keeping their accumulated weight. Fork A therefore differs from fork B
   by *both* "harm added at R" *and* "a chunk of the shared field deleted from where it was".
   A positive result is unattributable between a geometric effect and a near-field deletion.
2. **More fundamentally, the field is a sliding window over the last 32 harm locations, not a
   path.** MECH-023 asserts that responsibility depends on *how the agent got here*. The
   substrate structurally forgets all but the most recent 32 harm events, so "how it got here"
   is representable only over that window.

### 3b. RESOLUTION -- the kernel is ~8x wider than the entire reachable state space

`RBFLayer.forward` reads region identity only through `exp(-||z-c||^2 / 2*bw^2)`, with
`kernel_bandwidth = 1.0` (`from_dims` default; `world_dim = 32`).

Measured on the same run:

| quantity | value |
|---|---|
| `z_world` median pairwise distance | 0.0648 |
| `z_world` max pairwise distance (the two poles = R, R') | 0.1249 |
| `kernel_bandwidth` | 1.0 |
| pole separation / bandwidth | 0.125 |
| **RBF contrast between the two most distant points reachable** | **exp(-0.1249^2/2) = 0.9922** |

The two most widely separated points in the whole visited manifold differ by **0.8%** in how any
residue centre reads them. The residue field is therefore spatially near-UNIFORM across the
entire reachable state space: it behaves as an almost-constant offset rather than a terrain.

This matters precisely because of the DV-symmetry rule: a spatially uniform additive term is a
broadcast constant, and **a broadcast constant is argmin-invariant**. Whatever residue does to
selection on this substrate (and per 697 it does a lot), it is not currently doing it as
*geometry* -- there is almost no spatial contrast available to be geometric with.

A related gap is already recognised elsewhere in the registry: `SD-067` asks for "a dedicated
safety-terrain RBF bandwidth: an opt-in, TIGHTER bandwidth" for the MECH-303 contextual-safety
terrain. The same objection applies to the residue field's harm geometry, and is unowned there.

### 3c. A gate that certified its own subject (why this was nearly missed)

The driver's own region-distinctness precondition was written as
`pole_separation / median_pairwise_distance >= 1.5` -- scale-free, and deliberately so. On the
measured cloud that reads **1.928, i.e. it PASSES**, while the kernel contrast it is supposed to
certify is 0.992. The gate is denominated in the cloud's units; the DV reads in the kernel's
units. It would have green-lit exactly the configuration its own docstring cites as fatal.
Recorded because the failure mode is general: **a readiness gate must be denominated in the units
of the statistic the criterion actually reads.**

## 4. What the run would have produced

Most likely: both readiness preconditions green; C1 passes off the 3a relocation artifact; C2
fails because 3b leaves it arithmetically dead; run records MECH-023 `evidence_direction:
"weakens"` under the label "path dependence present but mass not location specific". That
sentence would have entered the evidence record as a measured property of responsibility
geometry, when it is a statement about a 1.0-wide kernel reading a 0.125-wide manifold and a
32-slot ring recycling its own centres.

## 5. Release condition

MECH-023's registered falsifier becomes runnable when **both** hold:

1. **Residue capacity exceeds the harm-event count of a trained run**, so a fork's injected
   history is additive rather than a relocation -- i.e. `num_harm_events < num_centers` over the
   experiment's schedule (or an explicit non-recycling / append-only accumulation path, or a
   consolidation mechanism that makes the 32 slots a summary of a longer history rather than a
   window over the last 32 events). The last option is the interesting one scientifically.
2. **Residue kernel bandwidth is commensurate with the `z_world` manifold** -- spatial contrast
   between distinct visited regions must be resolvable (e.g. `pole_sep / bandwidth >= 2`, giving
   `exp(-2) ~ 0.14` rather than `0.99`). Either tighten `residue.kernel_bandwidth` toward the
   measured cloud scale, or normalise distances by the cloud's own scale inside `RBFLayer`.
   Note this is a substrate change with wide blast radius -- every residue consumer moves -- so
   it is a governance/`/implement-substrate` decision, NOT an experiment knob.

Both are `complicated (buildable)`. Neither is probe-gated: the measurements above already say
what is wrong and roughly what the target values are.

## 6. Verification checks a successor should re-run first (cheap)

```
# capacity: must be FALSE before forking a trained agent
num_harm_events  <  residue.num_basis_functions

# resolution: want >= ~2, measured 0.125
max_pairwise(z_world_buffer) / residue.kernel_bandwidth
```

## 7. Provenance

- Adversarial design review (Step 4.5), verdict **BLOCKING**; findings F1 (resolution gate) and
  F2 (ring recycling) independently re-measured by this session before acting, both CONFIRMED.
  Two further confirmed findings not restated above: `substrate_ready = len(ready) > 0` admits a
  "weakens" verdict when PASS is arithmetically impossible (`n_pass >= 3` unreachable with <3
  ready seeds); and `ResidueField.neural_field` is a randomly-initialised, never-trained MLP
  (`grep -rn neural_field ree_core/` -> definition + reads only, no loss or optimizer anywhere)
  contributing `0.1 * MLP(z)` to every `evaluate_trajectory`, which cancels across forks but
  inflates any intact-vs-zeroed headroom gate. The untrained-scorer hazard is already gated OFF
  for E3's `reality_scorer` (`e3_include_untrained_fallback_scorers=False`); it is ungated here.
- The driver written for this proposal was NOT committed: an unqueued script under
  `ree-v3/experiments/` is audited as debt, and it would need rewriting against whatever
  capacity/bandwidth substrate lands. Its one reusable idea is recorded in section 1 (the
  `base_i = raw_i - residue_weighted_i` shared-base construction, which makes "bit-identical
  non-residue surfaces" true by construction rather than by hashing).
