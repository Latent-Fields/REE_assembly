# Failure autopsy (cluster) -- V3-EXQ-960 + V3-EXQ-961

- **Status:** `awaiting_human_confirmation` (staging mode -- non-interactive session; routing NOT finalised)
- **Generated:** 2026-08-30T06:34:18Z
- **Scope:** cluster, 2 targets
- **Dry-run gate:** both clean (`dry_run: false`)

| Run | Claim | Purpose | `non_degenerate` | emitted `evidence_direction` |
|---|---|---|---|---|
| `v3_exq_960_mech143_dca1_value_free_map_probe_...` | MECH-143 | evidence | **false** | `does_not_support` |
| `v3_exq_961_mech144_ventral_valence_spatial_gradient_probe_...` | MECH-144 | evidence | **false** | `does_not_support` |

## 1. Why these are one cluster

They share a surface shape -- *a run flagged degenerate that nevertheless weighs against its claim* -- and, underneath, **one structural property**. But their causes point in **opposite directions**, and that is the interesting part: they are the two failure modes of a single missing coupling.

**Structural property: the non-degeneracy scoring net is computed and recorded, but not wired to `evidence_direction`** -- and nothing checks that the flag was computed on a well-formed input. Two independently authored drivers, landing the same day, exhibit the two opposite consequences: one *degenerate* run credited as evidence against a claim, one *sound* run stamped degenerate.

This is **not** N independent bugs, and it is **not** a substrate ceiling.

## 2. V3-EXQ-960 -- the degeneracy flag is TRUE and CORRECT

The driver pre-registers `MIN_DISPERSION = 0.02` on cross-position `z_world` dispersion and states its meaning outright (docstring lines 86-91): below it, *"the 8 probe positions are not even distinguishable from one another and any low map_drift reading would be a representation-collapse artifact, not evidence of value-invariance."*

| Seed | `pre_dispersion` | vs floor 0.02 | `value_drift` | `location_drift` | pairwise delta |
|---|---|---|---|---|---|
| 42 | 0.009649 | 2.1x below | 0.0689 | 0.1386 | +0.0696 |
| 7 | 0.007550 | 2.6x below | 0.0574 | 0.2159 | +0.1585 |
| 13 | **0.000256** | **78x below** | 0.2269 | 0.1464 | **-0.0805** |

Every cell breaches the floor. Consequently:

- **C1 (value-stability) passes vacuously** -- a collapsed latent cannot drift under *any* manipulation, so a low value-drift is forced, not observed.
- **C2 (location-sensitivity) fails for the same reason**, not for want of a value-free map.
- The two criteria are **not independent**: one collapse produces the C1 pass and the C2 fail simultaneously. Reading the C1 pass as partial support would invert the finding.
- **Seed 13, the most collapsed cell, produced the run's only negative pairwise delta and its only C1-failing value drift** -- noise on a degenerate representation.

`cell_ok = pre_dispersion >= MIN_DISPERSION` is computed at driver line 384, but is **neither recorded in the manifest nor used to gate the emitted direction**.

**=> `does_not_support` should be corrected to `non_contributory`. MECH-143 is untouched by this run.**

## 3. V3-EXQ-961 -- the degeneracy flag is a FALSE POSITIVE

The flag fired on `c3_geom_distance_spread`, reason *"every group pinned -- zero spread"*. The cause is a driver bug at line 596:

```
geom_dist_groups = [[r["distance_std"]] for r in all_results if r["condition"] == "ARM_GEOM"]
```

Each group is a **singleton list**. `metric_is_degenerate` computes `spread = max - min`, which is `0` for any singleton, and `0 <= eps (1e-9)`, so **every singleton group is "pinned" by definition**. `metric_groups_are_degenerate` -- the *within-group* variant, designed for multi-value groups such as `[arm_on, arm_off]` per seed -- therefore returns degenerate **unconditionally**, and would fire identically on a perfect run.

The readiness it purports to test is in fact sound:

| Seed | active centers (floor 4) | `distance_std` (floor 0.5, degeneracy floor 1e-6) |
|---|---|---|
| 101 | 32 | 1.2100 |
| 202 | 32 | 1.0938 |
| 303 | 32 | 1.0408 |

On the substance, **C1** (Pearson r of harm-discriminative valence vs hazard proximity) measured **-0.1937 / 0.1523 / 0.2150** against a pre-registered 0.35 -- **0/3 seeds**, one negative.

**C2 carries no discriminative weight, and the driver says so.** Argument raised and withdrawn: the ablated arm's r of exactly `0.0` on all three seeds looked like a concealed vacuity, but the docstring (lines 125-134) declares it openly -- `ARM_ABLATED`'s `evaluate_valence` "returns identically zero by construction", r is *defined* as 0.0 by the guarded helper, and C2 is "recorded as a sanity check on the harness rather than a novel discriminative claim". Honestly scoped. The adjudication consequence is retained: **C1 alone is load-bearing** (C3 is readiness).

**=> `does_not_support` STANDS and the run SHOULD be scored. The `non_degenerate: false` stamp must not be used to discount it.** At 3 seeds with r spanning -0.19 to +0.21 this is a *weak* negative -- a miss at this scale and design, not a refutation.

## 4. Four-layer summary

| Layer | 960 | 961 |
|---|---|---|
| Claim alignment | unclear (not reached) | **weakened** (genuine, low-powered) |
| Prerequisites | **missing** (latent collapsed) | present (32 centers, spread ok) |
| Implementation | partial (guard not wired) | complete for what was tested |
| Environment | unknown | adequate |
| Measurement | **misleading** (C1 vacuous) | adequate for C1; flag is a false positive |
| Scale | unknown | **likely insufficient** (3 seeds) |

**Failure-location (GOV-FAILLOC-1).** 960: `MEASURES` (+ implementation) -- not chargeable to REE. 961: `MECHANISM` is the only bucket not excluded, but at 3 seeds Measurement adequacy is only marginally established, so the net classification is **MIXED**, and **REE FAILED is not asserted** for either.

## 5. Routing (proposed -- awaiting confirmation)

Both route to **`queue-experiment`**, plus one shared substrate entry covering the structural property:

`sd_nondegeneracy_net_gates_evidence_direction` -- two `failure_record` items:

1. **(from 960)** A run whose own pre-registered readiness floor is breached on every cell must emit `non_contributory`, not a claim-weakening direction.
2. **(from 961)** `metric_groups_are_degenerate` must refuse or warn on a singleton group rather than reporting it as pinned.

Per-run follow-up:
- **960** -- re-run only once `z_world` clears `MIN_DISPERSION`; record `cell_ok` per cell in the manifest. Re-running blind reproduces the same collapse.
- **961** -- fix the singleton-group call; if MECH-144 is to be pursued, raise seed count before treating r ~ 0.2 as a settled negative.

**Re-derive brake:** does not fire on either. MECH-143 and MECH-144 each have **0** prior `substrate_ceiling` hits under R1-R3, and neither reading is `substrate_ceiling`.

**No fan-out recommendation:** both routes are single named fixes, not discriminations among rival hypotheses.

## 6. Recommended per-claim dispositions

| Claim | Direction | `epistemic_category` | Status |
|---|---|---|---|
| **MECH-143** | `does_not_support` -> **`non_contributory`** | no category field today -- set one -> `standard` | stays `candidate` |
| **MECH-144** | `does_not_support` (**stands**, and should be scored) | no category field today -- set one -> `standard` | stays `candidate` |

## 7. Mechanical pre-routing checks (Step 7b)

**1 fire, acted on (not dismissed).**

**C1** -- `queue-experiment` was recommended for MECH-143 while `v3_exq_165_mech143_hippocampal_value_sensitivity` is already on disk and has **never scored a run**.

Checked. V3-EXQ-165 covers **both** MECH-143 and MECH-144, but its own docstring declares it a standalone analog: *"Inline 8x8 grid world (no ree_core agent imports). All terrain navigation is implemented as a lightweight hippocampal analog operating on a residue field."* It therefore does **not** probe the live `ree_core` `z_world` / residue field that 960 and 961 measure, and running it would not answer either run's question -- in particular it cannot address 960's `z_world` dispersion collapse, which is a property of the real substrate.

It is nonetheless a genuine unqueued asset (on disk since 2026-07-12, absent from `experiment_queue.json`, never scored) covering both cluster claims. **Surfaced for an explicit queue-or-retire decision** rather than left dormant.

## Adversarial red-team pass (Step 7c) -- NOT RUN

**No independent verifier ran, and no CONFIRMED verdict is claimed.** Step 7c calls for spawning a separate agent (preferably on a different model) to attack the conclusion. This session operates under a standing instruction not to invoke the Agent tool unless the user requests it, and the user did not.

The adversarial discipline was applied in-context instead, and it did change conclusions rather than rubber-stamping them -- six arguments were raised and withdrawn on direct code or docstring reads, each recorded under `arguments_withdrawn`. That is explicitly **weaker** than an independent pass: it shares the drafter's priors by construction, which is the exact property the pass exists to break.

**For governance:** treat every routing recommendation here as unverified by a second reader. The two highest-value targets for an independent check are V3-EXQ-963's claim that sampling starvation is refuted by the 779a comparison, and V3-EXQ-964's claim that C2 was mathematically unsatisfiable at `n_targets == 1`.
