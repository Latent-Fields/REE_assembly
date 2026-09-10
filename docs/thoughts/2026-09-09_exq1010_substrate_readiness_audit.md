---
nav_exclude: true
---

# EXQ-1010 and hippocampal A/B substrate-readiness audit

**Audit date:** 2026-09-10  
**Scope:** read-only adjudication of the live 978 -> 1002 -> 1008 -> 1010 lineage, related claims/proposals, and current `ree-v3` substrate.  
**Decision:** **do not start the hippocampal assay A or B as a scientific experiment on the present substrate.** The exact-task raw-field and PCA-32 representations are adequate experiment-side positive controls, but the reusable frozen-endpoint, pairing, drift, and native-consumer instruments required to make A/B discriminating do not yet exist. The trained 978-OFF `z_world` is not an adequate positive-control sender for this decision task.

This document makes no claim-registry, proposal, queue, runner, or substrate mutation. It applies the dossier's required distinction:

`encoded != decodable != natively accessible != bridgeable != pairing-specific != causally used != behaviourally useful`

The source is the campaign dossier at `docs/thoughts/2026-09-09_hippocampal_campaign_adjudication.md:28-32,226-262`, especially its instruction at lines 246-246 to use a known information-preserving source or adequate raw/PCA control if 1010 finds the current sender inadequate.

## 1. Evidence and provenance inspected

| Run | Current flat evidence | First evidence commit | Current flat SHA-256 | Direct result used here |
|---|---|---|---|---|
| 978 | `evidence/experiments/v3_exq_978_sd018_directional_field_fishtank_20260903T111718Z_v3.json` | `8a103991fc91c5e012844f82b8af28d5f4f7b1ab` | `ae368a1acb626d8efe4da8119cae294b8d3e5498e4c6f527d58b629a3f9c3e5f` | OFF/ON field decode R2 0.70991/0.70928; native PPO foraging 0.2667/0.2833 resources/episode. |
| 1002 | `evidence/experiments/v3_exq_1002_zworld_actor_adequacy_oracle_adapter_20260905T005017Z_v3.json` | `fae61ff53d27a71c50aa76649f6aee7201e3fd34` | `737daeee2a8c4997b511718fa9d24750250e62c125cf0e6b99b20d55cb3e53e2` | Raw-field worst seed 0.97303; trained `z_world` mean 0.66359; untrained mean 0.68799; trained-latent cloned competence 16.883 resources/episode. |
| 1008 | `evidence/experiments/v3_exq_1008_zworld_adequacy_portfolio_ws250_rebasis_20260907T233826Z_v3.json` | `db8ca96e2768243473e16fa048b5c638c4e93f69` | `1a4b1565448dc44d1c2f302293898d7c962dca6bf685fa18ed19b80e59a2fdc1` | Full 250-D input mean 0.93866; PCA-32 mean 0.86839, 3/3 above 0.80; random projection mean 0.77245; trained `z_world` mean 0.66860; registered linear rebases did not rescue it. |
| 1010 | `evidence/experiments/v3_exq_1010_zworld_overcapacity_decoder_sweep_20260909T195348Z_v3.json`; pack under `evidence/experiments/v3_exq_1010_zworld_overcapacity_decoder_sweep/runs/v3_exq_1010_zworld_overcapacity_decoder_sweep_20260909T195348Z_v3/` | `0241ac2a1965ac12542dfbed8cfad2fb857a6389` | `e49acbd5a6995b28480747a8c9a87f2db503b982b0d5bcb7205ded92c5155246` | Finite ladder did not clear 0.80 from reproduced OFF `z_world`; raw/PCA controls clear; all decoder fits are finite by the run's criterion; sample-size witness is still rising. |

The 1010 driver is `ree-v3/experiments/v3_exq_1010_zworld_overcapacity_decoder_sweep.py`, first landed at ree-v3 commit `203ad0bd2475bbec24c054f93cff218c5bc60ced`. The run records a different ree-v3 substrate commit, `63aa9f2cf02d0aa5664b3b8baa0f388cd08f93d0`, as expected for execution after later repository movement.

The dossier's line 53 correctly said 1010 was unfinished at its snapshot. That statement is now superseded by the completed evidence above; no other dossier conclusion is automatically superseded.

### Coordination snapshot

Startup checks found no competing claim on this audit path. Related live work was left untouched:

- `hippocampal-replay-interface-20260909` owns `docs/thoughts/2026-09-09_hippocampal_replay_interface_maintenance_supplement.md` and a broad evidence scope. Its in-progress supplement independently refines assay B's biological alternatives; this audit does not duplicate or land that work.
- `igw-233-inv104-reanalysis` owns `evidence/reanalysis` and `evidence/planning/experiment_proposals.v1.json`; `igw-233-inv104-exq-1016` and `igw-237-mech005-exq-1018` own separate queue/script resources.
- `gov-flagbacklog-20260909` owns `claims.yaml`, the hypothesis registry, governance flags, and substrate queue; this is an additional reason this document records the stale H-F registry state but does not repair it.

The fetched/default-branch `evidence/experiments/pending_review.md` reports zero pending at its 2026-09-09T14:47:27Z generation. The shared diverged checkout also contains an older locally modified report listing four items. Review state was neither inferred from that dirty file nor changed here; `review_tracker.json` remains the source of truth.

## 2. Bounded adjudication of EXQ-1010

### 2.1 What the measurements establish

On the **re-created 978-OFF regime used by this run**, none of the five fitted feed-forward action-decoder rungs reached the predeclared 0.80 agreement plus 0.20 elevation criterion on any seed. The best held-out OFF values were:

| Seed | OFF best held-out | Best rung | OFF best train | Consumer-width OFF | PCA-32 best | PCA-32 consumer width | Untrained best | OFF - untrained best |
|---:|---:|---|---:|---:|---:|---:|---:|---:|
| 42 | 0.683892 | `mlp2048` | 0.999603 | 0.667598 | 0.883613 | 0.883613 | 0.715549 | -0.031657 |
| 43 | 0.684619 | `mlp2048` | 0.999800 | 0.674915 | 0.872877 | 0.857836 | 0.689471 | -0.004852 |
| 44 | 0.665649 | `mlp512` | 0.999774 | 0.662595 | 0.876336 | 0.870229 | 0.708397 | -0.042748 |

Exact fields are in the 1010 flat manifest `per_seed_verdict` (pretty working copy lines 4286-4543) and pack `metrics.json`. This is strong evidence for a **large finite-reader generalisation deficit** in this particular 32-D encoding. It also reproduces the practically important finding that the trained latent is no better than its untrained 32-D control on this task.

The raw 25-D field is a sound positive control: held-out agreement is 0.983240/0.973799/0.973537; turn-state agreement is 0.980687/0.968786/0.964328; random-state agreement is 0.988158/0.991094/0.981405. PCA-32 is a sound capacity/protocol anchor at consumer width (0.883613/0.857836/0.870229). Those results rule out a generally incapable decoder protocol and a trivial action-marginal explanation.

The finite conclusion is therefore:

> Under 1010's re-created OFF representation, 28 training episodes per seed, train-only preprocessing, 60-pass Adam fit, and the tested linear-to-12.67M-parameter feed-forward ladder, no fitted decoder recovered a held-out oracle policy at the registered adequacy bar. The result is consistent with severe encode-time loss, but does not identify information destruction.

### 2.2 Fitted versus diverged rungs

All 45 track/rung decoder fits and all three raw controls report `decoder_training.diverged: false`; `guards.diverged_rungs` is empty. OFF `mlp2048` reaches 0.999603-0.999800 train agreement on all seeds, and `deep2048x4` reaches 0.981234-0.995435. `guards.memorising_rungs` is therefore `deep2048x4` and `mlp2048`, and the worst-seed max-over-rungs train value is 0.999603. The PCA top-rung minus consumer-rung worst delta is only -0.019553, inside the -0.10 tolerance.

That supports the narrow claim that the ladder **fit** and can interpolate the training labels. It does not support a claim that the learning curve is saturated or that every expressive reader class was tested.

Two implementation details bound this guard:

- `_train_decoder` defines “diverged” only as final CE greater than or equal to `ln(5)` (`...1010...py:786-836`). It is a useful no-fit flag, not a general numerical-convergence test.
- `_best_over_rungs` does not exclude rows carrying `diverged=true` (`...1010...py:1178-1193`). That is a latent logic hazard, but it does not alter this run because no row was flagged and all reported CE values are finite.

### 2.3 Calibration controls and the nonlinear witness

The calibration design is mostly strong:

- raw field verifies exact-task learnability;
- PCA-32 verifies the same 32-D width and fit protocol can clear the bar;
- the untrained latent prevents attributing generic random-compression performance to the trained encoder;
- same seed/rung decoder initialization is reset before each paired fit (`...1010...py:985-1016`);
- the PCA mean, basis, and post-projection z-score are fitted from training rows only (`...1008...py:666-725` and `...1010...py:1122-1131`).

The “reader-free” witness must be named more narrowly. It has no **fitted action head**, but it does have a separately fitted same-capacity latent-to-field decoder (`...1010...py:839-864,1018-1024`) followed by the fixed oracle rule (`...1010...py:902-940`). It is thus an action-head-free field-reconstruction witness, not a reader-free or model-free witness. Its OFF agreement peaks around 0.648-0.662 at `mlp512` and never clears the action bar. The deepest witness collapses on seed 44 (`decision-coordinate R2 = -0.6167`), while the PCA deepest witness has negative decision-coordinate R2 on seed 43 even though its action decoder remains at 0.8593. That divergence between two fitted witnesses is another reason not to promote the witness to an information-theoretic test.

### 2.4 Memorisation and sample saturation

The memorisation guard does its stated job: it rules out an under-capacity fit on the observed training labels. It does **not** rule out an under-sampled input-to-label relation. The script itself acknowledges this at `...1010...py:298-325`.

The sample witness does not show saturation:

| Seed | 50% row-subset held-out | Full-row held-out | Full - half |
|---:|---:|---:|---:|
| 42 | 0.655493 | 0.675512 | +0.020019 |
| 43 | 0.656477 | 0.670063 | +0.013586 |
| 44 | 0.630025 | 0.665649 | +0.035623 |

All three deltas are positive; two exceed the approximately 0.013 seed spread used in the driver's own warning text. A two-point half/full comparison cannot establish an asymptote. Moreover, the half set is sampled by **rows** (`torch.randperm(n_full)`) rather than by whole episodes (`...1010...py:1034-1060`), so it destroys the episode grouping that protects the primary split and gives no environment-level saturation evidence. This witness is properly recorded rather than gated in the manifest, but its observed direction materially weakens the “H-F-confirmed” gloss.

### 2.5 Split leakage

The main train/test split has no neighboring-timestep leakage. `x1002._split_episodes` takes whole episodes (`...1002...py:1211-1217`), and episode environments are instantiated with different `seed*1000+ep` seeds (`...1002...py:1150-1194`). For 40 oracle episodes the split is 28 train / 12 test, yielding 5,038/4,997/4,423 train steps and 2,148/2,061/1,965 held-out steps. Raw, world-state, and `z_world` features preserve this episode/step ordering (`...1002...py:1197-1249`), and standardisation/PCA are fitted on train only.

Remaining qualifications:

- the split is a deterministic prefix/suffix episode split, not a randomized or explicitly stratified held-out environment family;
- decoder model selection takes the maximum over the final test-set agreements across five rungs. There is no separate validation split for rung selection. The 0.80 conclusion survives because **every** rung is below it, but the reported “best” agreement is test-selected and should not be used as an unbiased performance estimate;
- as noted above, the sample-saturation sub-split is row-level and cannot inherit the primary split's protection.

### 2.6 Substrate identity and “same banked latent” warning

1010 did not load the exact frozen 1002/1008 endpoint or a banked observation tensor. The driver states that 978/1002 persisted neither observations nor encoder weights and that it re-collects observations and re-runs 60 P0a + 200 P0 + 90 P1 episodes (`...1010...py:60-73,1094-1169,1366-1388`). “Banked” therefore means banked deterministic **recipe**, not banked data or weights.

The reproduction is close enough to certify the intended operating regime: the consumer-width OFF values fall in the declared 0.60-0.75 band and the latent participation ratios closely match 1008. It is not bit-identical evidence across the lineage:

- 1008 ran as `linux-x86_64-py3.10-torch2.12.0+cpu`, substrate hash `875d3044...`; 1010 ran as `darwin-arm64-py3.13-torch2.12.0`, substrate hash `1fdd6171...`;
- example weight deltas differ slightly (seed 42 `0.2929618` in 1008 versus `0.2930078` in 1010), although the regime-level readouts reproduce;
- 1010 records `substrate_stable_across_run: false`, two process-snapshot drifts, and a 92,134-second identity-resolution lag; per-cell hashes agree, so this is a process/global identity warning rather than within-run cell disagreement;
- the driver script is explicitly excluded from the substrate hash (`include_driver_script_in_hash=False`, `...1010...py:1107-1110`), though its separate driver hash is recorded;
- the five OFF capacity cells share one frozen agent and are correctly marked reuse-ineligible/non-independent.

These facts do not invalidate the paired within-run capacity comparison. They do block the stronger statement that 1010 decoded the exact persisted 1002/1008 latent endpoint.

### 2.7 Manifest label versus warranted inference

The pack manifest says `label: H-F-confirmed` and “DESTROYED AT ENCODE TIME” (`.../manifest.json:43-44`). That is the output of the driver's **pre-registered finite decision grid** (`...1010...py:1203-1245,1680-1697`), not a measured information-destruction variable. The driver's own limitations say the result is only over this ladder/protocol/sample and cannot separate absence from a form outside the tested feed-forward family (`...1010...py:298-331`).

The current governance registry still records H-F as `alive`, with no evidence runs, and says 1010 is not yet queued (`evidence/planning/hypothesis_space.v1.json:5047-5064`). That registry is now stale relative to the landed 1010 manifest. This audit does not mutate it; governance must decide how to apply a **bounded** reading.

**Adjudication:** retain the experiment-local `H-F-confirmed` string as provenance, but do not repeat its “destroyed” paraphrase as established science. The defensible label is:

> **finite-ladder non-recovery on a reproduced OFF regime; strong evidence of a decision-relevant accessibility/retention deficit, with sample-size, reader-family, exact-endpoint, and process-identity alternatives still open**.

Failed finite decoding is not proof of zero mutual information or irreversible information destruction.

## 3. Assay A/B readiness

### 3.1 Representation adequacy, separated from native use

| Representation | Exact-task external adequacy | Behavioural/native-use evidence | A status | B status | Confound |
|---|---|---|---|---|---|
| Raw 25-D `resource_field_view` | **Adequate.** 1010 held-out 0.974-0.983; 1002/1008 agree. | The experiment-only `LocalViewGreedyPolicy` natively reads it and clears 45.75 resources/episode worst seed. A cloned experiment-only reader reaches 51.5 mean in 1008. The live REE actor is not wired to consume this raw field directly. | **Usable as a positive-control source/task oracle, not as a native REE sender-consumer interface.** | **Usable as an information-preserving control source** under a constructed known drift; no live drift/replay interface exists. | Task-informed 25-D slice; using it as the scientific sender would trivialize the very compression/interface question. |
| Full 250-D `world_state` | **Adequate.** 1008 mean agreement 0.9387. | Experiment-only `WorldStateAdapterPolicy`; cloned competence 50.73. No corresponding native bridge consumer. | Strong upper-bound source. | Strong upper-bound source for controlled drift. | High-dimensional direct observation, not a native subsystem representation. |
| Train-split PCA-32 of `world_state` | **Adequate.** 1008 mean 0.8684 and 1010 consumer-width 0.858-0.884, all seeds above 0.80. | Experiment-only transformed adapter; cloned competence 43.83 in 1008. No persisted/runtime PCA component in `ree_core`. | **Best existing dimension-matched positive-control sender** after its projection is frozen and persisted by the assay. | **Best existing compact controlled-drift substrate** for a known orthogonal transform/inverse, after instrument qualification. | Offline fitted transform; no native consumer, no frozen projection artifact, no endpoint/pair identity yet. |
| Trained 978-OFF `z_world` | Field content is decodable in bulk (978 R2 about 0.710), but exact-task action adequacy is **not demonstrated**: 1010 best 0.666-0.685, below bar and below untrained control. | External cloned competence is nonzero (16.23-16.88 mean across 1002/1008), but native PPO competence in 978 is only 0.267 resources/episode OFF. | **Not an adequate positive-control sender for A's decision task.** It may be a challenged/negative arm only. | **Not an adequate task-relevant drift positive control.** A null would alias source inadequacy with maintenance failure. | Bulk field R2 is not decision adequacy; 1010 is finite and under-saturation. |
| Untrained `z_world` | **Not adequate**; 1010 best 0.689-0.716, still below bar. | No native-use qualification. | Negative/compression floor only. | Negative/compression floor only. | It sometimes beats the trained latent, so it cannot validate learned content. |
| E1 `ContextMemory` / cue retrieval | Native read/write and z-world cue-to-action/terrain projections exist (`ree_core/predictors/e1_deep.py:36-265,1006-1078`). | It is wired into current E1 consumers, but the work programme still requires a write/store/retrieve/use ladder (ML-40). Current code comments document historical addressing/content collapse modes, and defaults remain configuration-dependent. | **Mechanically present, not demonstrably adequate for A.** No episode-index lookup plus native reinstatement comparator has been qualified at frozen endpoints. | Potential local-memory/rehearsal comparator, not an intersystem mapping-maintenance mechanism. | Retrieval strength, content identity, and downstream causal use are not separated. |
| Hippocampal `AnchorSet` / trajectory replay | Stores scale/segment/stream-tagged `z_world` anchors (`ree_core/hippocampal/anchor_set.py:192-290`); hippocampal forward proposes trajectories and replay starts from a recent/valence-selected `z_world` (`ree_core/hippocampal/module.py:1929-1985,2855-2916,3954-3970`). | Native planning/replay machinery exists. It does not implement A's frozen episode-index reinstatement or B's paired sender-receiver mapping update. | **Not yet an A index/native-reinstatement comparator.** | **Replay actuator present but assay semantics absent.** | Replay can rehearse local content; no pair identity, wrong-pair control, or cross-interface update target. |

### 3.2 Concrete component readiness

| Required component | A: frozen endpoint | B: controlled drift/replay | Live status |
|---|---|---|---|
| Adequate source positive control | Raw/full/PCA available. | Raw/full/PCA available in experiment code. | **Usable externally; not native.** |
| Frozen source and consumer snapshots | Needed with exact artifact IDs. | Needed before/after each evaluation. | **Missing as a reusable assay primitive.** 1010 re-creates endpoints rather than loading them. |
| Aligned interface telemetry | Sender, actual consumer input/preactivation, target, provenance, gates. | Same plus wake/sleep phase and pre/post identity. | **Missing.** Work programme ML-10 explicitly lists it (`...mutual_legibility_work_program...md:61-84`). |
| Episode/environment dataset builder | Validation/test split reusable across bridge rungs. | Same split reused across drift/maintenance arms. | **Partial/ad hoc.** 1002/1010 split by episode, but no reusable environment-held-out/provenance builder; ML-11 remains proposed (`...md:86-90`). |
| Communication-subspace estimator | Needed to separate full-source from actual consumer surface. | Needed to verify relevant versus unused-coordinate drift. | **Missing.** No RRR/principal-angle library; ML-12 remains proposed (`...md:92-104`). |
| Bridge ladder | Identity/native, Procrustes, affine, low-rank, nonlinear, `T(A,B)`. | Known inverse and complexity tracking. | **Missing from `ree_core` and experiment libraries.** ML-13 remains proposed (`...md:106-138`). |
| Pairing/content controls | Sender-only, receiver-only, correct/wrong episode, receiver permutation, zero, matched random. | Correct-pair replay, shuffled pairs with matched marginals, local-only, no maintenance. | **Missing as a common library.** ML-14 remains proposed (`...md:140-150`). 1010 has none because it asks a different question. |
| Native consumer causal replacement | Message ablation and matched replacement at the actual consumer. | Cross-system transfer plus stable local competence. | **Missing.** Existing adapters are experiment-only readers. |
| Controlled task-relevant/unused drift | Not central, except frame/query holdouts. | Known invertible relevant drift and unused-dimension drift. | **Missing.** Environment drift is not a controlled latent-coordinate intervention. |
| Replay/sleep trigger | Not required. | Boundary firing is available via `REEAgent.force_sleep_cycle_at_eval_boundary()` (`ree_core/agent.py:12666-12718`). | **Mechanically usable, but scientifically incomplete.** It does not provide paired intersystem replay or restrict which mapping updates. |
| Dynamic/recurrent stability | Report repeated interface use where applicable. | Required to distinguish compatible dynamics and cumulative bridge drift. | **Missing.** ML-15/15b remain proposed (`...md:152-190`). |
| Two-interface stable/change comparator | Optional generality check. | Required by assay B. | **Not qualified.** No two live interfaces have the full controls and adequate native consumers. |

**A readiness verdict:** representation controls are ready; the experiment is not. Raw/full/PCA can anchor the instrument, but no current component instantiates the dossier's matched frozen comparison among index lookup/native reinstatement, fixed route, frame bridge, and receiver-conditioned bridge with separate receiver-only and pairing controls. The trained `z_world` cannot be the positive-control sender for this task.

**B readiness verdict:** neither representation-to-interface nor maintenance semantics are ready. A known orthogonal transform of a frozen PCA-32 source would provide a clean information-preserving drift control, and the sleep boundary actuator exists, but the current replay path produces local E2 trajectories from recent/selected `z_world`; it does not replay correctly paired cross-system examples to a designated interface. Running B now would confound local rehearsal, retrieval strength, source inadequacy, and interface repair.

The related claims already cover the space; no duplicate is justified: ARC-139 and MECH-537-540 at `docs/claims/claims.yaml:98012-98237`, INV-105 at `:98095-98133`, and MECH-547/548 at `:99098-99240`. ARC-139's own note says do not build a V3 latent bridge or queue directly (`:98046-98050`). The staged work programme likewise says instrument validation precedes live diagnosis or sleep (`evidence/planning/mutual_legibility_work_program_20260907.md:13-21,61-192`).

## 4. Smallest justified next diagnostic

No additional 1010 diagnostic is required to begin **instrument qualification** on the already existing PCA/raw positive controls. The smallest gate before any hippocampal scientific A/B run is the already-specified synthetic qualification of ML-10 through ML-14: frozen exact artifacts, episode/environment split provenance, planted communication subspace, known rotation/inverse, and correct/mismatch/zero/matched-random replacement. That is instrument work, not a hippocampal mechanism experiment.

If governance wants to use 1010 to choose an **encoder-objective** repair, one smaller diagnostic is required first:

> Refit only the OFF `mlp512` rung on nested **whole-episode** training subsets (7/14/21/28 episodes, fixed 12-episode final test set), with at least three deterministic subset orderings per seed; fit no new capacity ladder. Report the held-out learning curve and its uncertainty. Keep the existing full-data PCA-32 anchor and raw gate as fixed references.

Why this is the smallest useful test: it directly resolves the observed positive half-to-full deltas without adding a new mechanism, decoder family, claim, or endpoint. A plateau well below 0.80 would strengthen the finite-family non-recovery result; continued growth would show that the current `H-F-confirmed` label is sample-limited. Only after a plateau would the driver's named layer-wise observation-to-`z_world` localization be the next question. This audit does not build, queue, or run that diagnostic.

## 5. Go/no-go ledger

| Item | Verdict |
|---|---|
| EXQ-1010 execution validity | **Valid finite decoder stress test**, with green raw/PCA calibration and fitted memorising rungs. |
| “H-F-confirmed” as manifest decision-grid output | **Accurately records the driver's branch.** |
| “Decision content destroyed at encode time” as scientific conclusion | **Not established.** Finite reader, rising sample witness, re-created rather than persisted endpoint, and substrate-identity warnings remain. |
| Raw/full/PCA representational controls | **Adequate externally** for the exact task; PCA-32 is the clean dimension-matched source control. |
| Native REE consumer adequacy | **Not demonstrated** for PCA/full input; native `z_world` path is below floor/bar. Experiment-only adapters must not be relabeled native consumers. |
| Assay A | **NO-GO as a scientific experiment; instrument qualification/build first.** |
| Assay B | **NO-GO as a scientific experiment; pairing-specific drift/maintenance and recurrence instruments absent.** |
| New claims / proposal / queue / runner | **None touched.** |
