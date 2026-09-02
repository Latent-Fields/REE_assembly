# Failure autopsy -- V3-EXQ-571c (MECH-439)

- **Run:** `v3_exq_571c_e3_variance_monopoly_presence_936_regime_20260902T152856Z_v3`
- **Generated:** 2026-09-02T16:13:52Z -- **status: confirmed** (Step 8 gate held, user present)
- **Outcome:** FAIL - `experiment_purpose: diagnostic` - self-route `substrate_not_ready_requeue` - indexer flag `precondition_unmet`
- **Claims:** MECH-439 - **Routing:** `implement-substrate` (amend `f_dominance_conversion_ceiling`)
- **Red-team (Step 7c):** cross-model, Fable -- **CONTESTED**, three defects upheld and applied
- **Pre-routing checks (Step 7b):** 0 fires on the corrected draft

## 1. Facts

Dry-run gate: run is real (`check_dry_run_citations.py` clean; no `dry_run` key). `validate_recording.py` reports no always-core gaps.

The load-bearing precondition `n_live_channels` (measured **1.0**, threshold 2.0) is UNMET in **all four arms**, and it is the *only* unmet precondition. Every other readiness check passed in every arm:

| precondition | measured (B1) | threshold | met |
|---|---|---|---|
| `decomp_samples_sufficient` | 202 (range 130-219) | 60 | yes |
| `xcand_total_variance_nondegenerate` | 8.55 | 1e-12 | yes |
| `temporal_committed_total_variance_nondegenerate` | 463.9 | 1e-09 | yes |
| `clamp_config_landed` | 1.0 | 1.0 | yes |
| `residue_protocol_landed` | 1.0 | 1.0 | yes |
| **`n_live_channels`** | **1.0** | **2.0** | **NO** |

C1 (load-bearing) is arithmetically **PASSED** -- modal channel share 0.999992 vs a 0.85 bar, 4/4 B1 seeds unanimous -- but the gate precedes criterion evaluation, so `criteria_non_degenerate` is false for all six criteria and the run scores nothing.

### The occupant is regime-dependent, and F is one of the occupants

Under the lineage's own definition (`driver:345`, `F_COMPONENTS = ("f_weighted", "harm_weighted")`):

| arm | occupant | top share | F share | `occupant_is_f` |
|---|---|---|---|---|
| B1 fed + warmup | `residue_weighted` | 0.999989-0.999996 | 4e-06 - 1.1e-05 | no (4/4) |
| B2 starved + warmup | `harm_weighted` | 0.7379-0.9996 | 0.796-0.9998 | yes (3/4) |
| B3 fed + no warmup | `residue_weighted` | 0.9872-0.9992 | 0.0008-0.0126 | no (4/4) |
| B4 starved + no warmup | `harm_weighted` | 0.9927-0.9997 | 0.9941-0.9998 | yes (4/4) |

`monopoly_occupant_is_f` is **true in 7 of 16 cells**, all of them starved. So MECH-439's F-monopoly premise **holds when residue is starved and fails when residue is fed**, with the environment held fixed at the 936 regime throughout.

### No channel is dead; the partition is one-dimensional in RELATIVE terms only

Every non-structurally-zero component in every one of the 16 cells clears the **absolute** liveness floor (1e-12). **Every** liveness failure in the run is a failure of the **relative** share floor (1e-3) -- a floor the precondition's own `description` does not mention (it names only `MIN_LIVE_CHANNEL_VARIANCE`; the code at `driver:1044-1046` requires both).

The single genuinely contested cell is **B2/seed46**: three live channels, top share 0.737871, `monopoly_present: false` -- the only direct observation in this lineage of what the partition looks like when more than one channel is live. It is also one of two cells short of the driver's own 200-selection target (145).

8 of 16 cells individually carry >=2 live channels; the arm gate takes the worst cell across an arm's seeds, so one red cell reds the arm.

## 2. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | Vacuous by its own gate; the reason cuts both ways for MECH-439 (see above). `ceiling_decision: exhausted` already stands. |
| Biological reference | partial | Multi-attribute value integration; the analogue presupposes a common currency. No new divergence. |
| Prerequisites | present | All landing checks 1.0. Load-bearing because `REEConfig.from_dims` swallows unknown kwargs silently. |
| Implementation | **partial** | SD-056 rollout clamp armed and binding. **No bound exists on the residue quantity E3 reads.** |
| Environment | adequate | Faithful 936 regime from the lineage's canonical baseline module. |
| Measurement | adequate | DV correctly moved to the within-tick cross-candidate partition. The gate did its job. |
| Integration | adequate | `make_env(seed)` arm-independent, so contrasts are within-layout. |
| Scale | adequate vs floor | 130-219 vs 60. Two cells short of the driver's richer 200 target. |

**Failure-location (GOV-FAILLOC-1): MIXED** -- mechanism `partial`, measures `established`, environment `established`. **NOT chargeable to REE**; `REE FAILED` is neither reached nor asserted.

## 3. What the red-team pass changed

The cross-model pass (Fable) returned CONTESTED with three defects, all upheld on independent re-verification and all in this artifact's *reading* rather than in the run's science:

1. **Misattributed substrate.** The first draft said the residue-side bound was "built but unarmed". Wrong: `SD-RESIDUE-VALENCE-BOUND` clamps `RBFLayer.valence_vecs` (`field.py:294-332`), but E3's residue term reaches `RBFLayer.forward`, which sums `self.weights` (`field.py:122-149`), written only by the unbounded `+=` in `add_residue` (`field.py:171`). Arming `residue.valence_bounding_enabled` cannot move this DV. The refusal survives for a *stronger* reason: no bound on that channel exists at all.
2. **"F holds the monopoly in no arm" was false** -- `harm_weighted` IS F under `F_COMPONENTS`.
3. **The "every cell" absolutes were false** -- B2/seed46 breaks them; the quoted 0.9379 was 571b's figure, wrongly imported.

The pass also caught that the recommended `create` duplicated a live rung, changing the routing to `amend`. It **confirmed as drafted**: the gate/criterion band arithmetic; that absence from `enabled_default_off_flags` is genuine proof (the helper recurses `REEConfig.residue`, and there is no truncation marker); and that the substrate drift is a labelling caveat only.

## 4. Learning extracted

See the JSON `learning_extracted` for the full list. The load-bearing items:

- A readiness gate that fires is not automatically a measurement failure -- here the gate **is** the finding.
- **Read the self-route's remedy clause, not only its label.** "Re-queue at an adequate n" names a remedy the run's own data refutes; a wrong remedy sends the next session to build the wrong thing.
- **Bounding one channel relocates the monopoly** is a mechanism story this run does **not** demonstrate. No run has bounded two channels at once. Stated as a prediction to be tested.
- **Check which field a fix actually writes** before treating it as the counterpart to another fix. That error cost this artifact a wrong substrate path and a wrong remedy.
- The gate and the criterion it guards are jointly satisfiable only for a top share in roughly [0.85, 0.999]; a *stronger* monopoly always self-routes to "not ready". The instrument cannot confirm the strongest form of its own hypothesis.
- C6: the routed partition decides the final commit on only 0.056 of B1 selections -- a monopoly here is over **eligibility**, not commitment as MECH-439 frames it.

## 5. Routing (ratified at the Step 8 gate)

**AMEND `f_dominance_conversion_ceiling`.** Its `implementation_hint` already carries the divisive-normalisation rung; 571c removes that rung's standing tractability blocker by supplying the per-channel decomposition at the select site, and redirects its target from F specifically to the **joint channel scale**. Add `field.py::add_residue` and `RBFLayer.forward` to `substrate_paths`, with an explicit note that `update_valence` is NOT this path. Append four `metric_trajectory` observations (936, 936a, 571b, 571c).

**The re-derive brake FIRES** (14 counted hits under R1-R3, reproduced independently and matching the driver's own Step 2.5b figure; MECH-439 additionally already carries `ceiling_decision: exhausted`, so this corroborates a recorded state rather than escalating). **A same-claim re-queue is REFUSED** -- no 571d re-measuring monopoly presence with one more channel bounded.

**Explicitly permitted and preferred:** a run whose DV is the commensurability **operator** itself.

`epistemic_category` stays **`standard`** by user decision -- `substrate_conditional`'s suppression is largely redundant given the existing ceiling demotion, while its lane-starvation cost is not.

**Draft `evidence_quality_note` and the per-claim recommendation are in the JSON. This skill recommends; `/governance` applies.**
