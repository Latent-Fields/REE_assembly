# Failure autopsy -- V3-EXQ-1057b (MECH-017 additive-budget final-pass dose ladder)

Status: **confirmed** (Step 8 gate held 2026-09-22, user present; Step 7c red-team `fable` cross-model **CONTESTED**, revisions applied)
Target: `v3_exq_1057b_mech017_additive_budget_dose_ladder_20260920T154955Z_v3` -- diagnostic, **PASS**, self-route `final_pass_dose_response_opposite_sign_across_orders_last_writer_signature`. ree-worker-3, 39m27s, 13 arms x 5 seeds. Supersedes V3-EXQ-1057a.

Adjudicated under **trigger 2** (`experiment_purpose: diagnostic`), not because of a failure. A clean diagnostic PASS still requires this skill before governance can act on it.

## 1. What this run is

It is **fan-out probe 1 of the GOV-FANOUT-1 portfolio** registered by `failure_autopsy_V3-EXQ-1057-1057a-cluster_2026-09-20`, whose sketch reads: *"dose ladder on the final pass -- after a fixed whole-buffer pass run k in {0, 3, 6, 12, 24} recent-window steps (and the mirror) ... **Null: both curves flat in k.**"*

That null is rejected. C1 (the sole load-bearing criterion, driver `:2349`) measured 4.0 of 4 legs non-flat against a threshold of 1.0, at `FLAT_BAND = 0.10` on 5 of 5 sign-consistent seeds.

Dry-run gate clean (0 dry, 2 clean); `validate_recording` OK; unreachable-criterion lint silent on this driver. `FLAT_BAND = 0.10` and `SIGN_CONSISTENCY_REQUIRED = 4` were verified identical in all four drivers of the lineage (1048 `:346-347`, 1057 `:445-446`, 1057a `:577-578`, 1057b `:787-788`) -- the manifest's provenance claim holds.

## 2. The four legs

| leg | order | dosed window | stratum | mean rel delta (k0 -> k24) | sign-consistent seeds | Spearman rho | k_half |
|---|---|---|---|---|---|---|---|
| D1_early | whole_then_recent | recent | early | **+1.3769588611814731** | 5/5 | +0.960 | 12 |
| D1_late | whole_then_recent | recent | late | **-0.3141292596217214** | 5/5 | -0.840 | 3 |
| D2_early | recent_then_whole | whole | early | **-0.4933430012971710** | 5/5 | -0.960 | 6 |
| D2_late | recent_then_whole | whole | late | **+0.4470232551959693** | 5/5 | +0.820 | 12 |

The DV is held-out E1 MSE, so **lower is better**. The sign matrix is perfectly antisymmetric:

```
             early   late
D1 (W->R)      +      -      dosing RECENT last: helps late, hurts early
D2 (R->W)      -      +      dosing WHOLE  last: helps early, hurts late
```

A clean zero-sum trade in which the last-dosed window wins its stratum at the other's expense. A pure total-budget mechanism cannot produce it: `k` adds steps in *both* orders, so a budget effect moves both curves the same way.

`hypothesis_verdict`: H-schedule `favoured_strongest_form`; H-reallocation and H-intrinsic `not_separated`.

## 3. Three qualifications the manifest does not make

**(a) C1's two halves differ in strength -- corrected after red-team.** At `k = 0` the dosed pass is not run (driver `:1266-1279`), so each order's reference rung sits in **its mirror's last-writer state**. For the **early** legs that makes non-flatness close to forced: the final pass carries ~102%/77% of the between-order early gap. For the **late** legs it does not -- under an equal-four-point null they would read -0.069 and +0.102, both *inside* the 0.10 band, and they came in at -0.3141 and +0.4470. So C1 was a genuine test on its late half. **Withdrawn:** the first draft said the driver "nowhere states the converse". It does, in advance -- `:550-563` predicts that "under the last-writer reading the two curves MUST move in OPPOSITE directions" and records the reviewer's reconstruction of all four legs as non-flat from 1057a's per-seed rows. The design is self-aware about its own easy half.

**(b) The within-order inversion is measured and never computed.** `_classify(stratum)` (driver `:2375-2387`) takes `legs[f"D1_{stratum}"]` and `legs[f"D2_{stratum}"]` -- it compares D1 against D2 *within* a stratum only. The row contrast (each order inverting between its own early and late) is the zero-sum structure a reallocation account predicts, and nothing in the driver reads it. `pattern_by_stratum` reports `{early: opposite, late: opposite}`, which is the column reading alone.

**(c) D2_late is the marginal leg.** Sign-consistent on 4 of 5 seeds at the endpoint (seed 456 at +0.0799, inside the band) and non-flat only at rungs 12 and 24.

## 4. A declared substrate limit that is factually wrong

The manifest declares: *"`E2.world_forward` has no trainer in ree_core, so a world_forward DV is identically 0.0 in every arm"*, citing substrate_queue entry `e2-world-forward-sleep-trainer` at status `pending_implementation`.

Verified against the code, that is **false**:

- `Agent.compute_e2_world_loss` exists at `ree_core/agent.py:12515`, and its docstring is headed *"THE GAP THIS CLOSES"* -- it was written for exactly this.
- It is wired into the sleep path at `ree_core/sleep/phase_manager.py:766-778`, behind the default-off lever `use_sleep_world_forward_consolidation`.
- The substrate_queue entry read `implemented_pending_validation` **already at 2026-09-20T12:19:24Z** -- about 3.5 hours before the run and before the driver was written -- not the `pending_implementation` the driver quotes.
- This is dated, not inferred: the trainer/wiring commit `4610133` (2026-09-17T20:53:57Z) is a verified **ancestor** of the run's own `substrate_commit` `995ba252` (2026-09-20T15:11:58Z), and `compute_e2_world_loss` is present in that exact tree. It trains `world_transition` and `world_action_encoder` -- the world-domain heads that constitute `world_forward`.

**The run's decision to leave it off was right**; only its stated reason is wrong. `phase_manager.py:759-765` records that enabling the lever changes `cross_module_replay_share` for existing arms and consumes global-RNG draws between the e1 and e2 draws -- so switching it on would have broken the bit-identical reproduction of the 1048/1057/1057a A/B/C cells this design reads as its prior. Implementation therefore stays **complete**, and integration is `coupled but inert -- INERT BY DESIGN`.

What changes is the routing: MECH-017 names held-out one-step E2 `world_forward` error as a **co-primary** readout, and that readout is `complicated (buildable)` behind an existing lever, not structurally unavailable. **User decision at the gate: record it as buildable and bind the successor to it; do not raise a separate governance flag.**

Two smaller corrections: the "12.5x" noise-band ratio is 12.3457x against the stated 0.81%; and the `185-201` citation for the interleaved branch should be `185-195` (`196-201` is the blocked branch).

## 5. Why `non_contributory` is right -- for two reasons, not one

The manifest gives one: a dose-curve **shape** criterion neither raises nor lowers "replay counters forgetting at no cost to recency", so scoring it into MECH-017's confidence would corrupt it. That is correct and deliberate.

There is a second the manifest does not state. MECH-017's non-degeneracy precondition **(iii), as it stood at run time** (`claims.yaml` `44a0665b4fc`, 2026-09-20T14:18:50Z) requires that *"the consolidation pass must actually UPDATE the world model (`CrossModuleConsolidator` metrics `updates_<module> > 0` for the E1 and E2-world losses, not only `e2_harm_s`)"*. The E1 half is met. **The E2-world half is not**, because `use_sleep_world_forward_consolidation` was left off, and OFF is structural absence -- no module key, no closure, no updates counter (`phase_manager.py:759-765`).

> **Withdrawn (red-team F3).** A first draft cited instead the clause requiring consolidation to run through `SleepLoopManager.force_cycle`. That clause was **not in the claim at run time** -- it entered `claims.yaml` at `02caebd047f`, 2026-09-22T04:16:21Z, about 36 hours *after* the run. A run cannot deviate from a precondition that did not yet exist. The substance relocates to (iii), which is contemporaneous and which the run genuinely does fail on its E2-world half.

The driver's own reason for building no `SleepLoopManager` remains sound and is not a defect (`:425-434`): routing through `force_cycle` would expose the buffer narrowing to every other reader in `_run_cycle` -- `offline_integration()`'s `e1.integrate_experience`, the SWS schema pass, REM attribution, the replay sampler -- destroying attribution. V3-EXQ-1026 (PASS, 2026-09-14) owns the wiring; this run isolates the content. Note for successors: the `force_cycle` requirement is now live, so a run intended to discharge the CONFIRMING clause must satisfy it.

## 6. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | unclear (protected, correctly) | cannot discharge the confirming clause, for the two independent reasons in section 5 |
| Biological reference | clear | sleep-dependent systems consolidation, recency/remote trade-off; `targeted_review_mech_017` present |
| Prerequisites | present | `probe_set_identical_across_arms` hashes probe tensors and asserts bit-identical latents across arms of a seed |
| Implementation | complete | with the correction in section 4 |
| Environment | adequate | for a dose-response on a consolidation schedule |
| Measurement | adequate | C1's EARLY half near-forced by the k=0 last-writer swap; its LATE half a genuine test (section 3a) |
| Integration | **coupled but inert -- INERT BY DESIGN** | the world_forward lever, deliberately off; named run that supplies it: the D3 successor |
| Scale | adequate | 13 arms x 5 seeds, 4-of-5 sign consistency |

**Failure location (GOV-FAILLOC-1):** not a failure -- the run PASSED and delivered the discrimination it was fanned out to deliver. MEASURES recorded `partial` only because C1's early half was near-forced by construction; the late half was a real test and passed. Nothing chargeable to REE or to MECH-017.

## 7. Frozen-ledger effect (Step 9b, Mode B)

Question `mech017_recency_cost_locus`, registered 2026-09-20T11:43:49Z by the 1057/1057a cluster autopsy, `growth_restriction` empty, `initial_frozen_count` 3 == `len(hypotheses)` 3. All three legs were pre-registered naming **V3-EXQ-1057b itself** as `adjudicating_runs`, and the run executed at 15:49:55Z -- so invariant 2 holds on real pre-registration, not a same-cycle backfill. **No hypotheses are added; the denominator does not move.**

| leg | axis | before | after |
|---|---|---|---|
| H-schedule | instrumentation | alive | **confirmed**, `met_elimination_bar: false` |
| H-reallocation | process | alive | alive (resolving_runs + basis recorded) |
| H-intrinsic | process | alive | alive (resolving_runs + basis recorded) |

`met_elimination_bar` is **false** deliberately: the run confirms a schedule/last-writer effect *exists* and eliminates neither sibling. The two survivors stay alive because the run was their pre-registered adjudicator and did not separate them -- order is perfectly confounded with which window is dosed (`:1257-1262`, verified: no arm decouples them). That is an observation bottleneck, not a power problem, and an uninformative run narrows nothing.

**Mode D (H-other): does not fire.** One leg confirmed and two alive does not reach the `>= 2 confirmed` candidate signal, and the full antisymmetric 2x2 is producible by a single last-writer mechanism -- no second leg is simultaneously required. Nothing recorded.

## 8. Routing -- `queue-experiment` (reversed after red-team)

**No substrate work is owed.** A first draft routed `implement-substrate` with a new entry for a per-step data-window argument to `consolidate()`, on the premise that driver-side alternation would cold-start Adam every step. **That premise is false**, and the reversal is the red-team's F1:

- `consolidate()` builds its per-module optimisers **once per call** (`cross_module_consolidation.py:158-162`).
- It then calls the driver's own loss closure **fresh on each step** (`:164-183`, driven by the interleaved loop at `:185-195`).
- So a **stateful closure** that alternates its window per invocation interleaves whole-buffer and recent-window steps *inside one `consolidate()` call*, with Adam momentum intact.

Confirmed by execution during this autopsy: 6 alternating steps, **1** Adam optimiser constructed, `updates_e1 = 6`. The fresh-Adam-per-**call** fact is real but irrelevant here, because the interleaving never crosses a call boundary.

> **How the error happened, recorded because it is the instructive part.** The mechanism was quoted from this run's own manifest, which repeats it. But `failure_autopsy_V3-EXQ-1057-1057a-cluster_2026-09-20` had **already withdrawn exactly that account** -- *"WITHDRAWN (first draft): 'fresh Adam per consolidate() call makes passes overwrite'. The same call accumulates 18 times per cell in wake training"* -- and had listed the driver-built route. Reading the prior artifact's `learning_extracted` was not enough; the withdrawn mechanism was still propagated because the manifest restated it.

**Successor requirements** (fan-out probe 2, the interleaved arm D3 -- the only probe that separates H-reallocation from H-intrinsic):

1. Build D3 **driver-side** with a stateful per-step window closure. No substrate change.
2. **Enable `use_sleep_world_forward_consolidation`** and report held-out one-step E2 `world_forward` error. Not a build: the trainer and its wiring were both in the substrate this run executed against (commit `4610133`, 2026-09-17T20:53:57Z, is an ancestor of the run's `995ba252`, 2026-09-20T15:11:58Z). Enabling it is also what satisfies run-time precondition (iii)'s E2-world half.
3. Compute the **within-order** early/late contrast as well as the across-order one (section 3b).
4. If the run is meant to discharge MECH-017's CONFIRMING clause rather than probe content, route through `SleepLoopManager.force_cycle` -- now a live precondition -- and say which it is.

## 8b. Step 7c red-team

- **Model:** `fable` -- cross-model (this session drafted on Opus 5).
- **Verdict: CONTESTED.** Survived: direction `non_contributory`, category `standard`, the 2x2 finding (b), the D2_late marginality (c), and the `world_forward` mis-declaration (d) -- strengthened with dated ancestry.
- **Changed:** F1 reverses the routing (above); F2 corrects (a) in both directions and **strengthens** the H-schedule verdict; F3 withdraws the anachronistic `force_cycle` reason.
- **Cheap confirmers run:** the executed interleave confirmer; `git merge-base --is-ancestor 4610133 995ba252` -> YES; `claims.yaml` at run time (no `force_cycle`); substrate_queue status flip at 2026-09-20T12:19:24Z, before the run; all four per-leg deltas recomputed at full precision.

## 9. Brake, granularity, debt class

- **Re-derive brake: does NOT fire.** MECH-017 ceiling count 0 under R1-R3 (5 targets tag the claim, none reads `substrate_ceiling`). This run is not a re-letter of the blocked construction -- it is the pre-registered fan-out probe the cluster routed to, and it delivered.
- **Granularity trigger: does NOT fire.** `granularity_debt_cluster.py MECH-017`: 5 targets, `unclear=4` / `other=1`, none `weakened`. The `other` target (V3-EXQ-1048) reads MIXED-and-faithfully-so, not weakened.
- **Debt class:** `complicated (buildable)` -- the separating probe is a named build with no open question, and after red-team F1 it is a **driver-side** build, not a substrate one.
