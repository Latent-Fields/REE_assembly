# Failure autopsy (cluster) -- V3-EXQ-960 + V3-EXQ-961

- **Status:** `awaiting_human_confirmation` (staging mode -- non-interactive session; routing NOT finalised)
- **Generated:** 2026-08-30T06:34:18Z
- **Scope:** cluster, 2 targets
- **Dry-run gate:** both clean (`dry_run: false`)

| Run | Claim | Purpose | `non_degenerate` | emitted `evidence_direction` |
|---|---|---|---|---|
| `v3_exq_960_mech143_dca1_value_free_map_probe_...` | MECH-143 | evidence | **false** | `does_not_support` |
| `v3_exq_961_mech144_ventral_valence_spatial_gradient_probe_...` | MECH-144 | evidence | **false** | `does_not_support` |

## 1. Why these are grouped -- CORRECTED after red-team

> **This section was substantially wrong in the first revision and has been rewritten.** The red-team verdict was **CONTESTED**; the science held, the routing did not. Details in the red-team section at the end.

They share a surface shape -- *a run flagged degenerate that nevertheless emits a claim-weakening direction*.

**What the first revision claimed, and why it was false.** It asserted that "the non-degeneracy net is computed and recorded but **not wired** to `evidence_direction`", and that nothing downstream prevents a degenerate run from weighing against a claim. That is **not true**. `build_experiment_indexes.py:3431-3436` implements the documented 2026-06-11 non-degeneracy gate (`scoring_excluded = "degenerate"`), and it has **already fired on both runs**:

```
MECH-143   scoring_excluded=degenerate   reason=zworld_probe_dispersion: floor-pinned (max=0.00964888<=floor=0.02)
MECH-144   scoring_excluded=degenerate   reason=c3_geom_distance_spread: every group pinned -- ...
```

(live `claim_evidence.v1.json`). The gate exists; it sits one layer downstream -- at the indexer -- of where the first revision looked, which was the drivers.

**What they actually share.** Because the gate is purely mechanical and trusts `non_degenerate` unconditionally, **the flag's correctness is load-bearing** -- and neither driver validates the input it computes that flag from. 960 sets it correctly and is correctly excluded. 961 sets it wrongly and is wrongly excluded. That is a common *consequence* of a working gate fed by an unvalidated flag, not one missing coupling.

**So calling this "ONE structural property" overstates it**, and the first revision's own `readings` list already named two distinct defects. These are two genuinely independent bugs -- a real representation collapse, and a bad argument passed to a helper -- that meet only at a shared downstream consumer. They are reported together because that consumer is what makes both consequential, not because they have one cause.

## 2. V3-EXQ-960 -- the degeneracy flag is TRUE and CORRECT

The driver pre-registers `MIN_DISPERSION = 0.02` on cross-position `z_world` dispersion and states its meaning outright (docstring lines 86-91): below it, *"the 8 probe positions are not even distinguishable from one another and any low map_drift reading would be a representation-collapse artifact, not evidence of value-invariance."*

| Seed | `pre_dispersion` | vs floor 0.02 | `value_drift` | `location_drift` | pairwise delta |
|---|---|---|---|---|---|
| 42 | 0.009649 | 2.1x below | 0.0689 | 0.1386 | +0.0696 |
| 7 | 0.007550 | 2.6x below | 0.0574 | 0.2159 | +0.1585 |
| 13 | **0.000256** | **78x below** | 0.2269 | 0.1464 | **-0.0805** |

Every cell breaches the floor. Consequently:

- **Neither criterion is interpretable.** With the 8 probe positions mutually indistinguishable, no map-drift statistic computed over them carries the meaning the design assigns it -- in *either* direction. C1's 2/3 pass and C2's 0/3 fail are both computed over a representation that cannot express the distinction required.
- **CORRECTED after red-team:** the first revision argued C1 passed *vacuously* because "a collapsed latent cannot drift under any manipulation". **That mechanism is wrong, and this run's own cells refute it** -- seed 13, the *most* collapsed cell (78x below floor), produced the *largest* value drift (0.2269) and the only C1 failure. Cross-position dispersion and PRE->POST `map_drift` are independent quantities: a collapsed vector can still rotate freely. C1 also passed only 2/3 seeds, so nothing was "forced" at all. The right word is **uninterpretable**, not vacuous, and the surviving argument is the pre-registered one, not a mechanical one.
- Reading the C1 pass as partial support would still invert the finding.
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

**=> `does_not_support` STANDS -- but the run is NOT scored today, and saying "it should be scored" does not make it so.** CORRECTED after red-team: `build_experiment_indexes.py:3431` currently excludes it, and `claim_evidence.v1.json` shows MECH-144 `scoring_excluded="degenerate"`. **Fixing the driver bug only fixes future runs.** Making *this* run count requires three steps, in order:

1. **Amend this run's manifest `non_degenerate` flag** false -> true (preserving the original finding and the reason for amendment, for audit).
2. **Re-run `build_experiment_indexes.py`** so `claim_evidence.v1.json` drops `scoring_excluded` for MECH-144.
3. **Separately** fix the driver's singleton-group call (line 596) and add an arity guard to `metric_groups_are_degenerate`.

Applied as first written -- without steps 1 and 2 -- this autopsy would have left MECH-144 with **zero** evidence from this run, the exact opposite of its own assertion.

At 3 seeds with r spanning -0.19 to +0.21 this remains a *weak* negative -- a miss at this scale and design, not a refutation.

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

## Adversarial red-team pass (Step 7c) -- VERDICT: CONTESTED

An independent verifier (different model, reasoning withheld until it had recomputed from the raw cells) attacked this cluster. **The science held; the routing did not** -- the documented failure family for this corpus.

**Independently reproduced:** the singleton claim is TRUE -- `metric_is_degenerate` returns on `spread <= eps` *before* the floor check, so `floor=1e-6` cannot rescue a singleton; a live replay of driver lines 596-598's exact input reproduces the manifest's `degeneracy_reason` byte-for-byte, and a perfect-run singleton fires identically. Fed correctly (flat, or per-seed `[geom, ablated]` pairs) the same data returns non-degenerate. 960's flag is likewise correct -- replay reproduces `floor-pinned (max=0.00964888<=floor=0.02)`, ratios 2.1x / 2.6x / 78.0x verified, and every driver line citation checked verbatim. The seed-13 triple was verified exhaustively. 961's `does_not_support` at 3 seeds is defensible against the pre-registered bar.

**The verdict-moving defect.** The first revision's central structural premise -- *"the non-degeneracy net is computed and recorded but not wired to `evidence_direction`"* -- is **false**. The gate exists at `build_experiment_indexes.py:3431-3436` and **has already fired on both runs**. Three consequences, all applied above:

1. **961's headline recommendation was inert as written.** "Should be scored" named no mechanism, while the false-positive flag is excluding it *today*. The operative steps (amend the manifest flag, rebuild the index) are now stated. Applied verbatim, the first revision would have left MECH-144 with **zero** evidence -- the opposite of its own assertion.
2. **960's asserted harm never materialised.** The run weighs nothing already; the direction correction is hygiene, not a rescue.
3. **The proposed remedy would have made 961 worse.** Wiring flag -> direction, on a false-positive flag, deepens the exclusion. The first revision never resolved that tension because it did not know the gate existed.

**Also corrected:** the absolute *"a collapsed latent cannot drift under any manipulation"* is contradicted by this cluster's own seed-13 cell -- the most collapsed cell produced the **largest** drift. The `non_contributory` recommendation for 960 survives, but on the **pre-registration** argument, not a mechanical one. And the "ONE structural property" framing is overstated: these are two independent defects meeting at a shared consumer.

**Also flagged:** `_metrics.py` already ships `p0_readiness_gate` / `P0NotReady` -- the designed producer-side remedy for 960's exact shape -- and the 960 driver never calls it. Now named in that target's routing.

**Not checked by either party:** raw per-step data (absent from the manifests), `claims.yaml` alignment for MECH-143/144, and the V3-EXQ-165 disposition beyond confirming the file exists.
