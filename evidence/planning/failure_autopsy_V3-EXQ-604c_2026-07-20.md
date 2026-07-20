# Failure autopsy — V3-EXQ-604c (intra-run substrate divergence, defect class D3)

**Generated** 2026-07-20T06:44:11Z · **Session** `interesting-wu-b46711` · **Status** confirmed
**Target** `v3_exq_604c_q044_mech314_subflavour_ablation_gapa_ready_20260607T193029Z_v3`
(`V3-EXQ-604c`, PASS, `evidence_direction: supports`, `ree-cloud-2`, 2026-06-07)
**Claims** MECH-314, MECH-314a, MECH-314b, MECH-314c, Q-044
**Commissioned by** [`intra_run_substrate_divergence_sweep_2026-07-20.md`](intra_run_substrate_divergence_sweep_2026-07-20.md) sec 5b
(REE_assembly `3427fe852a`); defect class D3 first confirmed on
[`failure_autopsy_V3-EXQ-689d_2026-07-20`](failure_autopsy_V3-EXQ-689d_2026-07-20.md) sec 4.

> **AMENDED 2026-07-20T07:25Z (sec 2c) — verdict unchanged, warrant strengthened.** All 15 cells
> **executed one substrate** (`f80bc236`): the driver imports `ree_core` at module scope in a single
> process, so the mid-run edit could not reach execution and `0bedd600` never ran. 604c is therefore a
> **recording artefact** of the same `executed_substrate_identity` class as V3-EXQ-778a, not an
> execution confound. Read sec 2c before citing sec 2a/2b.

> **One line.** The D3 divergence is **real but demonstrably DV-inert** — five cross-boundary matched
> cell-pairs are bit-identical on every trajectory quantity, and C1's strongest seed is fully
> substrate-matched — so it is **withdrawn** and MECH-314 / MECH-314a keep `supports`. But the
> autopsy surfaces a **larger, independent defect the sweep only half-saw**: MECH-314b and MECH-314c
> are Phase-1 **broadcast scalars**, which cannot move an argmax, while C2's DV is a pure function of
> the argmax. Their `0.0` deltas are an **arithmetic identity, not a measurement**. C2 is
> structurally vacuous for two of its three legs; 314b/314c and Q-044 go **`non_contributory`**, the
> re-derive brake **fires** (3rd), and a further ablation is **refused**.

---

## 1. Facts — what ran, what was measured

Five arms x three seeds (42/43/44), `curiosity_candidate_source=e2_world_forward`, on the
GAP-A-repaired substrate. This is the retest **sanctioned by** the predecessor autopsy
[`failure_autopsy_gapA-cluster-604b-648a-649_2026-06-07`](failure_autopsy_gapA-cluster-604b-648a-649_2026-06-07.md),
which routed 604b `non_contributory` / `substrate_ceiling` and specified exactly this repair: gate on
the cross-candidate **range** rather than bias **magnitude** (the same-statistic confound), on the
now-validated ARC-065 GAP-A channel. All three readiness preconditions cleared:

| readiness gate | measured | floor | met |
|---|---|---|---|
| `consumed_candidate_spread_supra_floor` | 0.276286 | 0.05 | yes |
| `curiosity_bias_range_supra_floor` (the 604c fix) | 0.01529031 | 0.0001 | yes |
| `primary_scores_bounded_fraction_supra_floor` | 1.0 | 0.9 | yes |

Criteria: `C0` pass (3/3 seeds every arm), **`C1` (load-bearing)** `c1_parent_delta_on_vs_off =
0.402505` vs `DISTINCT_MARGIN = 0.03`, `c1_non_degenerate: true`; `C2` pass on one arm
(`ARM_NOVELTY_OFF` 0.402505; `ARM_UNCERTAINTY_OFF` **0.0**; `ARM_LP_OFF` **0.0**).

**Recording provenance.** Top-level `substrate_hash`, `machine_class`, `elapsed_seconds` and `seeds`
are all **absent** (`seeds` is present inside `config`). Per-cell `arm_fingerprint` is present on all
15 cells, which is what made this adjudication possible at all — and is precisely the field the
Experimental Recording Standard's per-run always-core would have **hidden** (sweep sec 1: the
`_hoist_multi_arm_substrate_hash()` trap). Recording debt is noted but is **not** what blocks
anything here.

## 2. The D3 divergence — and why it is withdrawn

Two substrates, `substrate_n_files` 90 -> 91 (a file **added** mid-run):

| substrate | cells |
|---|---|
| `f80bc236` (90 files) | `ARM_OFF` 42/43/44, `ARM_ALL_ON` **42** |
| `0bedd600` (91 files) | `ARM_ALL_ON` **43/44**, `ARM_NOVELTY_OFF` x3, `ARM_UNCERTAINTY_OFF` x3, `ARM_LP_OFF` x3 |

This is 689d's signature exactly: whole control arm on one build, treatment arm split 1/2. Benign
channels were ruled out corpus-wide (sweep sec 2) and re-confirmed here: `globs`, `scoped`,
`machine_class`, `driver_script_in_substrate_hash` all constant within the run.

### 2a. The internal control — five cross-boundary matched pairs

604c happens to contain its own falsifier, because arms on **opposite sides** of the boundary
produced identical trajectories. Comparing all 29 recorded per-cell fields:

| pair | seed | substrates | identical | differing fields |
|---|---|---|---|---|
| `ARM_OFF` / `ARM_NOVELTY_OFF` | 42 | `f80bc236` / `0bedd600` | **26/29** | `curiosity_bias_max_abs_{mean,peak}`, `curiosity_subflavours_fired_mean` |
| `ARM_OFF` / `ARM_NOVELTY_OFF` | 43 | `f80bc236` / `0bedd600` | **26/29** | (same three) |
| `ARM_OFF` / `ARM_NOVELTY_OFF` | 44 | `f80bc236` / `0bedd600` | **26/29** | (same three) |
| `ARM_ALL_ON` / `ARM_UNCERTAINTY_OFF` | 42 | `f80bc236` / `0bedd600` | 24/29 | + `curiosity_bias_range_peak`, `modulatory_authority_scale_factor_mean` |
| `ARM_ALL_ON` / `ARM_LP_OFF` | 42 | `f80bc236` / `0bedd600` | **26/29** | + `modulatory_authority_scale_factor_mean` |

Every field that differs is **curiosity-bias bookkeeping the arm's own treatment is defined to
change**. Every *trajectory-determined* quantity is bit-identical across the boundary —
`selected_class_counts` and `candidate_first_action_counts` (discrete histograms),
`selected_action_class_entropy`, `cand_world_pairwise_dist_{mean,min,max}`, `raw_score_range_{mean,max}`,
`contrastive_loss_mean`, `n_p1_ticks`, `n_buffer_appends`, `n_contrastive_steps`,
`selected_classes_n_unique`.

**Load-bearing C1 additionally has a fully substrate-matched seed.** `ARM_OFF` 42 and `ARM_ALL_ON` 42
are *both* on `f80bc236`; their entropy delta is **0.732** — the largest of the three seeds, against a
0.03 margin. All three seeds move the same direction (42: -0.732, 43: -0.062, 44: -0.414). This is
**689d inverted**: there the only substrate-matched seed was the one that *failed* the primary
criterion; here it is the strongest pass. C1 stands on a substrate-homogeneous subset alone — the
sec-5e "finding survives on matched seeds" disposition.

### 2b. The mechanistic story — corroborating, NOT load-bearing

The only commit in the window adding exactly one file to the hashed globs is `ree-v3 6bba8cf`
(2026-06-07T16:23:23Z, before the run's 19:30:29Z stamp), which adds
`ree_core/pfc/infralimbic_avoidance_gate.py` (SD-058/MECH-357) and modifies `agent.py` + `config.py`.
Every hunk of the `agent.py` diff sits behind `if getattr(config, "use_instrumental_avoidance",
False)` / `if self.instrumental_avoidance is not None`, the config default is
`use_instrumental_avoidance: bool = False`, and 604c's config never sets it.

**This could not be confirmed by hash and must not be reported as if it were.** The executing tree was
**dirty**: recomputing `compute_substrate_hash` over git blobs at every candidate commit in the window
yields 89 and 90 files where the manifest records 90 and 91 — a constant +1, i.e. one untracked `.py`
under the globs — and no recomputed hash matches `f80bc236` or `0bedd600`. So the commit archaeology
is **corroboration**; the empirical cross-boundary identity in 2a is the warrant. That ordering
matters: the empirical argument is indifferent to *what* changed.

**The residual objection, and why it does not survive.** One could posit that the substrate change had
effect E and the ablation had effect -E, cancelling. That would have to hold simultaneously for three
different ablations, across up to three seeds, on 20+ independent continuous *and discrete-count*
quantities, to full recorded precision. It is not a credible confound, and the independent
mechanistic check rules it out separately.

### 2c. AMENDMENT 2026-07-20T07:25Z — the executed substrate was UNIFORM; `0bedd600` never ran

*Added after the original adjudication landed (`75726ecb4c`), applying the module-import-binding rung
established independently by [`failure_autopsy_V3-EXQ-778a_2026-07-20`](failure_autopsy_V3-EXQ-778a_2026-07-20.md).
**The verdict is unchanged — exonerated — but the reasoning below is stronger and more general than
2a/2b, and supersedes them as the primary warrant.***

604c is a **single process** whose substrate modules were bound in `sys.modules` **before any cell
ran**. Verified on the driver:

| check | evidence |
|---|---|
| all substrate imports at module scope | `experiments/v3_exq_604c_...py:145-152` — `experiments._lib.arm_fingerprint`, `ree_core.agent`, `ree_core.environment.causal_grid_world`, `ree_core.utils.config`, all before the loop |
| one process, one loop | `:959-960` `for arm in ARMS: for seed in seeds:` — arm-major, seed-minor |
| no dynamic reimport | no `importlib` / `reload(` / `__import__` / `subprocess` / `multiprocessing` in the driver, `ree_core/agent.py`, `structured_curiosity.py`, `e3_selector.py`, `arm_fingerprint.py`, `_harness.py` |
| fingerprint re-reads DISK per cell | `:965` `compute_arm_fingerprint(...)` is called **inside** the cell loop; `compute_substrate_hash` globs and `read_bytes()` the working tree at call time |

The observed hash sequence is **exactly one monotone transition in loop order**, each of the 15 cells
present exactly once (`ARM_OFF` 42/43/44, `ARM_ALL_ON` 42 | `ARM_ALL_ON` 43/44, then the three OFF arms).
That is the single-process signature: a restart would have re-run earlier cells on the new substrate.

**Therefore the mid-run edit could not reach execution for ANY cell.** `ree_core.agent` — and with it
the newly added `ree_core/pfc/infralimbic_avoidance_gate.py` and the amended `REEConfig` — was bound at
process start, i.e. at the `f80bc236` state. All 15 cells executed `f80bc236`. **`0bedd600` is a
disk-state reading that never executed**, produced because the fingerprint re-reads the working tree
per cell while execution uses the process-start binding.

Three consequences:

1. **The flag-gating argument in 2b is now redundant, not load-bearing.** It does not matter that
   `use_instrumental_avoidance` defaults False — the gate's code was never loaded, and the config field
   did not exist on the process's `REEConfig` class. The dirty-tree obstacle that blocked hash
   attribution is likewise moot: *whatever* changed on disk at ~16:23Z could not execute.
2. **The bit-identity in 2a is a confirmed PREDICTION of this argument, not an independent
   coincidence.** If all cells ran one build, cross-boundary matched pairs *must* be identical on
   trajectory quantities. 2a therefore stands as strong corroboration — and remains the right
   *first* triage step when the driver's import structure is unknown or a restart is suspected —
   but it is no longer the primary warrant.
3. **604c belongs to the same defect class as 778a: `executed_substrate_identity` — a RECORDING
   artefact, not an execution confound.** It is a second corpus instance for the
   `arm_fingerprint` / `manifest_core` / `arm_reuse` fix in flight under session
   `relaxed-pike-81943c`, and it differs from 778a in one useful way: 778a's `substrate_n_files` was
   **constant** (129) whereas 604c's **moves 90 -> 91**, so a file addition on disk is *not* evidence
   that the addition executed. A triage ladder keyed on `n_files` movement would mis-rank 604c as the
   more severe of the two; both are the same artefact.

**Verdict: D3 detected, exonerated — `sufficient_alone_to_withdraw: false`, now over-determined.**
Primary warrant: the change could not reach execution (2c). Corroborating: cross-boundary bit-identity
(2a). Redundant: flag-gating (2b). Contrast 689d, where the same signature *was* judged sufficient —
that adjudication is under re-examination by session `musing-einstein-c80816`, and the import-binding
rung should be applied to it before its D3 is treated as settled.

## 3. The defect that does matter — C2 is structurally vacuous for 314b/314c

`ree_core/policy/structured_curiosity.py:40-41,101` states it plainly: in Phase 1 the uncertainty
(MECH-314b) and learning-progress (MECH-314c) sub-flavours are **global scalars broadcast across the
K candidates**. Only novelty (MECH-314a, Phase-2 `e2_world_forward`) is per-candidate.

A constant added uniformly to all K candidate scores **cannot change an argmax** (nor a softmax
sample — a uniform additive shift cancels in the normalisation). C2's DV,
`selected_action_class_entropy`, is a pure function of the selected-action sequence. Therefore:

> For `ARM_UNCERTAINTY_OFF` and `ARM_LP_OFF`, `delta == 0.0` is an **arithmetic identity**, fixed
> before the experiment ran, and **independent of whether MECH-314b or MECH-314c is true**.

**The manifest confirms the architecture unaided**, which is what raises this from inference to
demonstration:

| readout | ALL_ON | UNCERTAINTY_OFF | LP_OFF | reads as |
|---|---|---|---|---|
| `curiosity_bias_range_mean` | 0.01529031 | **0.01529031** | **0.01529031** | a broadcast constant **cancels** in a max-minus-min range |
| `curiosity_bias_max_abs_mean` | 0.240986 | 0.235738 | 0.240916 | ...but **does not** cancel in a magnitude |
| `curiosity_subflavours_fired_mean` (s42) | 2.866 | 1.866 | 2.000 | the ablations **are** correctly plumbed and do fire |

So the channels compute, fire, and contribute bias magnitude — they simply have **no selection-level
authority by construction**. Two consequences:

1. **The 604c readiness gate r2 was, unknowingly, a novelty-only gate.** `curiosity_bias_range` is the
   exact statistic in which the broadcast terms vanish. The 604b autopsy's repair (magnitude -> range)
   was correct for its purpose and remains correct — but the repaired gate certifies readiness for
   MECH-314a alone, never for 314b/314c.
2. **`ARM_NOVELTY_OFF` collapses exactly onto `ARM_OFF`** on every trajectory quantity, because
   novelty is the only per-candidate term. That is *why* C1 and the C2-novelty leg are the same number
   (0.402505) — the sweep's non-independence observation is correct, and this is its mechanism. The
   run yields **one** finding, not two; governance must not count C1 and C2 as independent
   corroboration.

**This is not a script defect and not dishonesty.** The script's pre-registered block states the
caveat up front ("314b/314c are broadcast scalars by design") and routes non-discriminating arms to
`mixed`. What the autopsy adds is that `mixed` is the **wrong category**: `mixed` connotes a measured
weak-or-equivocal effect, whereas nothing was measured. The correct category is `non_contributory`
under `substrate_ceiling`.

**Secondary check, cleared.** `n_p1_ticks` varies widely (129-4000), and plug-in entropy is biased low
at small N — so small-sample bias could in principle drive C1. It does not: at seed 42 `ARM_ALL_ON`
has *ten times more* ticks than `ARM_OFF` (2394 vs 240) yet *lower* entropy, the opposite of the bias
direction; at seed 43 both arms have exactly 4000 ticks. Only seed 44 is directionally confounded
(129 vs 179), 1 of 3. C1 is not a sampling artefact.

## 4. Claim-layer map

| claim | status | prior direction | recommended | why |
|---|---|---|---|---|
| MECH-314 (parent) | `candidate_substrate_landed` | `supports` | **`supports` STANDS** | C1 valid; substrate-matched on seed 42 with the largest margin; D3 withdrawn |
| MECH-314a (novelty) | `provisional` | `supports` | **`supports` STANDS** | per-candidate term; its ablation is a real manipulation and carries the whole parent effect |
| MECH-314b (uncertainty) | `candidate_substrate_landed` | `mixed` | **`non_contributory`** | broadcast scalar; delta 0.0 is an arithmetic identity, not a measurement |
| MECH-314c (LP) | `candidate_substrate_landed` | `mixed` | **`non_contributory`** | same |
| Q-044 (which sub-flavours load-bearing) | `open` | `supports` | **`non_contributory`** | 2 of 3 legs structurally incapable of discriminating; the surviving leg is numerically C1 |

`claim_ids` tagging is **accurate** — not inherited-without-re-evaluation. Note MECH-314's
`epistemic_category` in `claims.yaml` still reads `substrate_ceiling`, which 604c's cleared readiness
gates supersede for the *parent*; that is governance's to update, not this skill's.

## 5. Four-layer diagnosis

Two distinct diagnoses, because the parent and the 314b/314c legs fail at different layers.

### 5a. MECH-314 / MECH-314a — no defect

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | the claim expressed itself; C1 large, consistent in sign across 3/3 seeds |
| Biological reference | partial | frontopolar/rostrolateral PFC exploration bonus; striatal novelty (Wittmann 2008). Not a formal import |
| Prerequisites | present | ARC-065 GAP-A validated (V3-EXQ-649) *before* this run — the exact gap that voided 604b |
| Implementation | complete | per-candidate novelty on `e2_world_forward`; authority gate active (`frac 1.0`) |
| Environment | adequate | CausalGridWorldV2 reef/bipartite; candidate spread 0.276 well clear of floor |
| Measurement | adequate | range-based readiness gate is the correct statistic for a per-candidate bias |
| Integration | coupled | GAP-A channel + authority gate both operative |
| Scale | adequate | 3 seeds, 60 P0 + 20 P1 episodes |

### 5b. MECH-314b / MECH-314c — measurement blind by construction

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | the claim could not express itself under **any** outcome — not evidence either way |
| Biological reference | partial | Daw 2006 frontopolar uncertainty; Schmidhuber 1991 / Oudeyer compression-progress for 314c (Pull 1 already flagged 314c as least anchored) |
| Prerequisites | present | not the blocker |
| Implementation | **stub (symbol-of-mechanism, not functional role)** | broadcast scalar has the *shape* of a curiosity bonus with **zero** selection authority |
| Environment | adequate | not the blocker |
| Measurement | **misleading** | argmax-derived DV against an argmax-invariant manipulation; reports a structural zero as an empirical null |
| Integration | isolated | channels fire but reach no consumer that can act on them |
| Scale | adequate | more seeds cannot help — the zero is exact |

**Recommended `epistemic_category`: `substrate_ceiling`** for 314b/314c/Q-044 (the ceiling is the
Phase-1 broadcast implementation). `standard` for MECH-314/314a — no ceiling, the run succeeded.

## 6. Learning extracted

1. **D3 triage has two rungs, and the cheaper one is also the stronger — take it FIRST.**
   *(Re-ranked in the 2026-07-20T07:25Z amendment; the original text had these the other way round.)*
   **Rung 1 — executed-substrate identity (static, no data needed):** if the driver imports its
   substrate at module scope and runs one process with no dynamic reimport, `sys.modules` binds the
   code at process start and **no mid-run edit can reach execution** — the divergence is a *recording*
   artefact of `compute_substrate_hash` re-reading the working tree per cell. Establishes the
   executed identity outright. Rung independently established by the 778a autopsy; applies to 604c.
   **Rung 2 — matched cross-boundary cells (empirical):** find two cells on opposite sides whose
   *intended* difference is separable from the substrate difference and compare all recorded fields;
   bit-identity on trajectory quantities exonerates the boundary regardless of what changed. Use it
   when the import structure is unknown, a restart is suspected, or rung 1 is inconclusive — and as
   corroboration when rung 1 clears, since rung 1 *predicts* the identity rung 2 measures.
   Either way, the sweep's severity ranking is a *prior*, not a verdict.
1b. **`substrate_n_files` movement does NOT rank severity.** 778a (constant 129) and 604c (90 -> 91)
   are the same artefact class despite opposite `n_files` behaviour: a file appearing on disk is not
   evidence it executed. Any triage ladder keyed on `n_files` will mis-rank them.
2. **A dirty tree defeats hash-based attribution but not empirical exoneration.** Recomputing
   `compute_substrate_hash` at candidate commits is worth doing, but when `substrate_n_files` disagrees
   with the clean tree by a constant, attribution must be reported as corroborating only.
3. **A broadcast scalar cannot be tested with an argmax-derived DV.** This is a *general* vacuity
   pattern, distinct from both known E3 pseudo-replication forms and from the `vacuous_pass` flag: the
   criterion is not degenerate, the arms are correctly plumbed, and the run legitimately PASSes — yet
   two of its legs were arithmetic identities. **Detectable statically**: a manipulation that is
   invariant under the DV's own symmetry (here, additive-constant invariance of an argmax) tested
   against that DV. Candidate for a lint in the `/queue-experiment` design-audit step.
4. **The manifest's own readouts diagnosed the architecture.** `curiosity_bias_range` equal to full
   precision while `curiosity_bias_max_abs` differs *is* the broadcast-scalar signature. Recording both
   a range and a magnitude of the same quantity turned out to be decisive; the pair should be kept.
5. **A repaired readiness gate certifies only the channel it measures.** The 604b -> 604c
   magnitude-to-range repair was correct and is not withdrawn, but it silently narrowed the gate's
   scope to the per-candidate channel. When a gate is re-pointed at a new statistic, re-check which
   arms it still certifies.

## 7. Routing

### 7a. MECH-314 / MECH-314a — none owed

`supports` stands. D3 withdrawn. No re-queue, no substrate work.

### 7b. MECH-314b / MECH-314c / Q-044 — `implement-substrate`; re-derive brake FIRES

Ceiling-hit counts under the binding R1-R3 convention, **including this autopsy**: MECH-314b **3**,
MECH-314c **3**, Q-044 **3** (priors: `failure_autopsy_604a-624a-630_2026-06-03`,
`failure_autopsy_gapA-cluster-604b-648a-649_2026-06-07`). Threshold 2 -> **fired**.

**A further same-claim ablation is REFUSED.** Another lettered iteration would return `0.0`
deterministically — not probably, but as an arithmetic consequence of adding a constant to every
candidate. This is the strongest possible instance of the loop the brake exists to stop: the re-test's
result is knowable in advance without running it.

**Build first:** make uncertainty and LP **per-candidate**, the Phase-2 treatment MECH-314a already
received (`novelty_source` / `e2_world_forward`). `recommended_substrate_queue_entry.action = amend`
on **ARC-065**, per the user's Step-8 decision, keeping 604b's failure record and this one on the same
entry that already tracks the GAP-A channel.

A redesign testing a *different* mechanism (new EXQ number, different `claim_ids`) remains permitted.
A DV swap alone is **not** a viable escape: a uniform additive bonus is inert under argmax *and*
softmax, so no selection-level readout can rescue the Phase-1 implementation.

### 7c. Granularity-debt recurrence — trigger fires, but does NOT indicate granularity debt

This is the 4th autopsy circling MECH-314 (`V3-EXQ-603a-b-c-604-605_2026-05-29`,
`604a-624a-630_2026-06-03`, `gapA-cluster-604b-648a-649_2026-06-07`, this). The signatures differ each
time, which is the documented recurrence tell — but they are a **converging instrument-repair chain on
one question**, and the chain **terminated in a PASS**: candidate-uniform `z_world` -> GAP-A shared
channel -> magnitude-vs-range same-statistic confound -> C1 clean. `/claim-synthesis` is **not**
recommended. MECH-314's decomposition into 314a/b/c is working *as designed*: it returned a sharp,
actionable answer (one child load-bearing, two structurally untestable). Recorded here so the standing
GOV-GRAN-1 scan sees a deliberate non-route rather than a dropped handoff.

## 8. Draft `evidence_quality_note` text for governance

**MECH-314, MECH-314a** (append):

> [2026-07-20 autopsy V3-EXQ-604c, D3 intra-run substrate divergence]: divergence DETECTED and
> WITHDRAWN. 604c's cells span two substrates (`f80bc236` 90 files / `0bedd600` 91 files, a file added
> mid-run at ~16:23Z), reproducing the V3-EXQ-689d signature (whole control arm one build, treatment
> arm split 1/2). It is NOT a confound here: five cross-boundary matched cell-pairs
> (`ARM_OFF`/`ARM_NOVELTY_OFF` x3 seeds; `ARM_ALL_ON`/`ARM_UNCERTAINTY_OFF` and `ARM_ALL_ON`/`ARM_LP_OFF`
> at seed 42) are bit-identical on 24-26 of 29 recorded fields, differing ONLY in curiosity-bias
> bookkeeping the arms' own treatments define. Every trajectory-determined quantity — discrete
> `selected_class_counts` / `candidate_first_action_counts`, entropy, pairwise dist, raw-score range,
> contrastive loss, tick counts — is identical across the boundary. Load-bearing C1 additionally has a
> FULLY SUBSTRATE-MATCHED seed (`ARM_OFF` 42 and `ARM_ALL_ON` 42 both on `f80bc236`, delta 0.732, the
> largest of the three, vs margin 0.03), so C1 stands on a substrate-homogeneous subset alone.
> Corroborating (not load-bearing): the only +1-file commit in the window (ree-v3 `6bba8cf`) adds
> `ree_core/pfc/infralimbic_avoidance_gate.py` fully behind `use_instrumental_avoidance=False`, which
> 604c never sets; hash attribution was NOT reproducible because the executing tree was dirty (+1
> untracked `.py`). `supports` STANDS. Note C1 and the C2-novelty leg are the SAME comparison
> (`ARM_NOVELTY_OFF` collapses exactly onto `ARM_OFF`, novelty being the only per-candidate
> sub-flavour), so they are one finding, not two independent supports.

**MECH-314b, MECH-314c** (append; direction `mixed` -> `non_contributory`,
`epistemic_category: substrate_ceiling`, `pending_retest_after_substrate: true`):

> [2026-07-20 autopsy V3-EXQ-604c]: direction corrected `mixed` -> NON_CONTRIBUTORY. 604c's C2
> sub-flavour-discriminability test is STRUCTURALLY VACUOUS for 314b/314c. Both are Phase-1 BROADCAST
> SCALARS (`ree_core/policy/structured_curiosity.py:40-41,101`) — one constant added uniformly across
> all K candidates — while C2's DV (`selected_action_class_entropy`) is a pure function of the argmax
> sequence. A uniform additive constant cannot change an argmax (nor a softmax sample), so the observed
> `c2_sub_flavour_deltas` of EXACTLY 0.0 for `ARM_UNCERTAINTY_OFF` and `ARM_LP_OFF` are an ARITHMETIC
> IDENTITY fixed before the run, independent of whether 314b/314c are true. The manifest confirms the
> architecture unaided: `curiosity_bias_range_mean` is identical to full precision across
> ALL_ON/UNCERTAINTY_OFF/LP_OFF (0.01529031 — a broadcast constant cancels in a max-minus-min range)
> while `curiosity_bias_max_abs_mean` differs (0.240986/0.235738/0.240916 — it does not cancel), and
> `curiosity_subflavours_fired_mean` changes correctly, proving the ablations ARE plumbed and the
> channels DO fire. They simply have no selection-level authority by construction. `mixed` overstates
> this: nothing was measured. The 604c readiness gate r2 (`curiosity_bias_range`) is, unknowingly, a
> NOVELTY-ONLY gate — the exact statistic in which the broadcast terms vanish — so it certifies
> readiness for MECH-314a alone. Not a script defect: the pre-registered block flagged the
> broadcast-scalar caveat up front. `pending_retest_after_substrate` — 314b/314c must be made
> PER-CANDIDATE (the Phase-2 treatment 314a received) before any direction is weighed. RE-DERIVE BRAKE
> FIRED (3rd substrate_ceiling adjudication): a further same-claim ablation is REFUSED — its result
> (0.0) is knowable in advance without running it. Note this run does NOT weaken 314b/314c.

**Q-044** (append; direction `supports` -> `non_contributory`):

> [2026-07-20 autopsy V3-EXQ-604c]: direction corrected `supports` -> NON_CONTRIBUTORY. Q-044 asks
> which curiosity sub-flavours are behaviourally load-bearing at the selection level. 604c's C2 cleared
> its pre-registered bar (">=1 sub-flavour discriminates") on `ARM_NOVELTY_OFF` alone, but (a) that
> leg's delta (0.402505) is NUMERICALLY IDENTICAL to load-bearing C1's, because `ARM_NOVELTY_OFF`
> collapses exactly onto `ARM_OFF` — so C2 carries no information independent of C1 — and (b) the other
> two legs were STRUCTURALLY INCAPABLE of discriminating (broadcast scalars vs an argmax-derived DV;
> see the MECH-314b/314c note). The answer "novelty only" is therefore PRE-DETERMINED BY THE PHASE-1
> IMPLEMENTATION, not measured. Q-044 stays `open` and gains nothing from this run. Re-adjudicable once
> uncertainty/LP are per-candidate.

## 9. Hypothesis-space ledger (Step 9b)

No `fanout_recommendation` is emitted — the bottleneck routes to a single unambiguous build
(per-candidate uncertainty/LP), which GOV-FANOUT-1 explicitly exempts.

No existing registry question covers MECH-314/Q-044, so a new question
**`curiosity_subflavour_authority`** is registered and partly resolved in the same edit
(`pre_registered_utc == resolved_utc == 2026-06-07T19:30:29Z`, the run's own completion stamp, so
`pre_registered_utc <= resolved_utc` holds):

| hid | axis | state | basis |
|---|---|---|---|
| `H-novelty-per-candidate` | `selection` | **confirmed** | C1/C2-novelty; control (`ARM_OFF`) passed; non-degenerate. Carries the entire parent effect |
| `H-uncertainty-broadcast` | `selection` | **alive** | resolving run recorded, but the run could not discriminate — structural vacuity is an observation bottleneck, not a narrowing |
| `H-lp-broadcast` | `selection` | **alive** | same |

`initial_frozen_count = 3 = len(hypotheses)`. No `fanout_growth_events` (new question, not growth).
`decision.decidable: false`, `observation_bottleneck` names the broadcast-scalar implementation. Axis
`selection` is already mapped to family `process`, so no `axis_families` edit is needed.

## 10. Scope

Analysis and hand-off only. **No manifest was edited** — completed runs are re-adjudicated via
autopsy, never rewritten. `claims.yaml`, `review_tracker.json` and `substrate_queue.json` are
untouched; `/governance` applies the recommendations above. The one dashboard-plane write is the
frozen pre-registration ledger (sec 9), which is derive-only input and never mutates claim status.
