---
status: PENDING
status_asof: 2026-07-31
status_claim: SD-085
---

# SD-085: e3.reality_cost_weight

**Claim ID:** SD-085
**Subject:** `e3.reality_cost_weight` (config field: `E3Config.f_weight`)
**Status:** PENDING
**Registered:** 2026-07-31
**Depends on:** none (pure additive config lever on already-live `score_trajectory`)
**Blocks:** ARC-062 GOV-FANOUT-1 Leg P-B (`REE_assembly/evidence/planning/arc_062_conversion_fanout_2026-07-29.md`
Section 2 Leg P-B) -- an H2 (F-dominance) discriminator that needs to sweep F's
weight in the committed argmin directly, independent of eligibility.

## Problem

`E3TrajectorySelector.score_trajectory` (`ree_core/predictors/e3_selector.py:1118-1261`)
computes the committed-selection score as

```
score = f + lambda_eff * m + rho_residue * phi  [+ optional benefit/goal/pe_confidence/self_viability terms]
```

`f = self.compute_reality_cost(trajectory)` is the primary harm/goal-adjacent
cost -- V3-EXQ-571 measured it monopolising **~88-89% of E3 committed-selection
variance**. Every other additive term in the sum has a dedicated `*_weight`
config field that can be dialed down (`lambda_ethical`, `rho_residue`,
`benefit_weight`, `goal_weight`, `pe_confidence_weight`, `self_viability_weight`).
`f` alone enters at an **implicit, unconfigurable coefficient of 1.0** -- there
is no `f_weight`, `reality_cost_weight`, or any other field anywhere in
`e3_selector.py` / `config.py` that scales F's contribution to the score itself.

This gap blocks a specific, already-designed discrimination. ARC-062's fanout
(GOV-FANOUT-1) needs Leg P-B to test **H2**: is committed-class conversion
recoverable *only* when F's grip on the committed argmin is loosened directly,
independent of which upstream bias channel is pushing? The two attenuation-shaped
levers that already exist near F are both the wrong shape for this question:

- **MECH-448/449** (`_f_eligibility_envelope` / `_go_nogo_eligibility_gate`,
  `e3_selector.py:1449-1686`) act on **eligibility** -- which candidates survive
  to compete -- not on F's weight in the score itself. 654i/654j already armed
  both as matched constants and still failed C2 (`failure_autopsy_f-dominance-conversion-cluster_2026-06-20`),
  which is exactly why Leg P-B is designed to test a different axis rather than
  re-run the eligibility lever a third time.
- **MECH-090** (`docs/architecture/mech_090_commit_entry_predicate.md`,
  `HeartbeatConfig.use_commit_readiness_gate` in `beta_gate.py`) is a post-hoc
  commit-*elevation* gate: it conditions whether BetaGate elevates into
  committed mode based on the score margin, **after** the committed argmin has
  already been decided. It cannot attenuate F's role in *choosing* the argmin.
- `use_natural_commit_urgency_release` (`config.py:3630-3662`) is the
  **duration face** (how long a commit is held once made) -- explicitly
  documented as "PARALLEL to the selection-face MECH-448", not a selection lever.

Full resolution trail, including the code citations above verified at build
time: `REE_assembly/evidence/planning/arc_062_conversion_fanout_2026-07-29.md`,
"P-B buildability resolution (2026-07-31)".

## Solution

Add a single scalar coefficient, `E3Config.f_weight: float = 1.0`, placed
beside `lambda_ethical` / `rho_residue` in the "Scoring weights" block
(`config.py` ~line 549-551) -- its closest structural siblings: always-present
multiplicative coefficients on an always-computed score term, not gated
additive terms behind a `use_*` master switch (`benefit_weight` / `goal_weight`
/ `pe_confidence_weight` / `self_viability_weight` all gate an *optional*
term that is skipped entirely when disabled; `f` is never skipped, so a
master switch has no meaning here -- the coefficient itself is the control,
exactly as for `lambda_ethical` and `rho_residue`).

`score_trajectory` changes from:
```python
score = f + lambda_eff * m + self.config.rho_residue * phi
```
to:
```python
score = self.config.f_weight * f + lambda_eff * m + self.config.rho_residue * phi
```

**No `REEConfig.from_dims()` wiring.** `lambda_ethical` and `rho_residue` --
the two structurally identical siblings -- are *not* threaded through
`from_dims()` either; every experiment that sweeps them sets the attribute
directly post-construction (e.g. `v3_exq_735_drive_reward_balance_sweep.py`:
`cfg.e3.lambda_ethical = float(arm["lambda_ethical"])`,
`cfg.e3.rho_residue = float(arm["rho_residue"])`). Leg P-B's F-attenuation
ladder will follow the identical pattern: `cfg.e3.f_weight = <rung>` per arm.
Adding `from_dims` plumbing here would be inconsistent with the two fields
this one is modeled on, and unnecessary for the one consumer it exists to
serve.

**Diagnostics.** `_last_traj_components` (populated when
`e3_score_decomp_enabled`) gains a new key `f_weighted` holding
`float((self.config.f_weight * f).detach().mean().item())`, so Leg P-B (and
any future consumer) can read F's actual weighted score contribution. The
existing `f` key is left reporting the **raw, unweighted** `compute_reality_cost`
output, unchanged -- this SD does not redefine what any existing consumer of
`_last_traj_components["f"]` receives.

**Backward compatibility.** `f_weight` defaults to `1.0`. Multiplying a finite
float by `1.0` is an IEEE-754 identity operation (bit-exact, not merely
numerically close), so `self.config.f_weight * f == f` for every existing call
site under default config -- `score_trajectory`'s output, and therefore every
downstream committed-selection decision, is unchanged. The new dataclass field
is purely additive; no existing `E3Config(...)` or `REEConfig.from_dims(...)`
call site is affected (unset fields simply take the new default).

## Architecture Context

Sibling to `lambda_ethical` (weight on the ethical/harm term `M`) and
`rho_residue` (weight on the residue term `Phi_R`) in the same scoring
equation `J(zeta) = F(zeta) + lambda*M(zeta) + rho*Phi_R(zeta) - beta*B(zeta)`
(see `e3_selector.py` module docstring / ARCHITECTURE NOTE). Those two terms
already had dedicated weight fields; `F` was the one term without one. This SD
closes that asymmetry rather than introducing a new architectural primitive --
it is `complicated (buildable)`, not `complex (probe-gated)`, per the parent
fanout doc's own buildability caveat.

Distinct from MECH-448/449 (eligibility face) and `natural_commit_urgency_release`
(duration face): this is the **selection-score face** -- which candidate wins
the argmin, evaluated by directly rescaling one of the three named terms in
the score equation, not by changing which candidates compete or how long a
winner is held.

No independent biological claim is made by this SD itself. It is an
engineering/diagnostic lever that makes an existing, already-grounded
construct (context-dependent down-weighting of a "reality/movement-cost" term
relative to threat- or goal-relevant evaluation, broadly analogous to
effort-cost arbitration in cortico-basal-ganglia action selection) directly
testable, rather than proposing new biology of its own. The biological
question lives in Leg P-B's hypothesis (H2), not in this coefficient.

**No ML/AI engineering concerns identified.** This is a plain scalar
multiplicative coefficient on one term of an existing bounded weighted sum,
structurally identical in shape to `lambda_ethical`. No new numerical
stability, initialisation, or gradient-flow consideration is introduced --
`f_weight` has no learned parameters and is never differentiated through (E3
trajectory scoring is not a training loss).

**Phased training:** not applicable. `f_weight` is a scalar coefficient set by
the caller, not a learned parameter or encoder head; no P0/P1/P2 phasing
applies (mirrors `lambda_ethical` / `rho_residue`).

**MECH-094:** not applicable. This SD touches no simulation, replay, or
memory-write content.

## What This SD Enables

- ARC-062 GOV-FANOUT-1 Leg P-B (H2 F-dominance discriminator) becomes buildable
  via `/queue-experiment`.
- A minimal diagnostic validation experiment (this session, see below) confirming
  the knob actually moves `score_trajectory`'s output and is numerically stable.

## Related Claims

ARC-062, MECH-090, MECH-448, MECH-449, MECH-309 (co-tagged on ARC-062's fanout
Leg P-A). V3-EXQ-571 (the F-dominance measurement motivating this lever).
