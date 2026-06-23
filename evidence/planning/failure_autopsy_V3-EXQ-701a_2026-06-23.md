# Failure Autopsy — V3-EXQ-701a (INV-050 MEL-measurability, converged-P0 re-run)

- **run_id:** `v3_exq_701a_inv050_mel_measurability_converged_p0_20260623T072156Z_v3`
- **queue_id:** V3-EXQ-701a (supersedes V3-EXQ-701)
- **claim:** INV-050 (MEL = the third / model-error-load sleep drive; this run tests ONLY the directly-testable IV precondition: is accumulated waking prediction-error a measurable, graded, manipulable quantity?)
- **experiment_purpose:** diagnostic (excluded from governance confidence/conflict scoring)
- **outcome:** FAIL — self-route `substrate_not_ready_requeue`, `evidence_direction: non_contributory`
- **scope:** single (lineage: 677 MECH-180 sleep-side -> 701 INV-050 IV-precondition -> 701a converged-P0 re-run)
- **generated_utc:** 2026-06-23T22:51:52Z
- **status:** confirmed (user interactive gate, 2026-06-23: "Re-queue 701b w/ frozen-probe metric")
- **routing:** queue-experiment (re-queue 701b with a FROZEN held-out probe-state convergence metric; re-derive brake does NOT fire). No substrate_queue entry.

**This is a diagnostic, NOT a verdict on INV-050.** Evidence stays `non_contributory`; INV-050 is not weakened. INV-050 attracts duplicate IGW spawns — do not re-derive the sleep DV.

---

## 1. Facts (no interpretation)

The 701 autopsy prescribed the converged-P0 fix: add world-forward reconstruction MSE as the **primary** P0 objective (`L_E2 = L_recon + w_contrast * L_contrast`, sd056_weight 0.05), raise `CONV_EPISODES` 20 -> 60, and add a **per-seed** R2 readiness gate (interpret R1/C1 only on seeds where `conv_rel_drop >= MIN_REL_CONV_DROP=0.10`). 701a implemented all of it. The gate still failed:

- **R2 `world_model_converged_p0_seed_fraction` = 0.333** (threshold 0.667): only **1/3 seeds converged**. Per-seed `conv_rel_drop`:
  - seed42 = **−2.29** (conv_pe_init 0.00074 -> conv_pe_final 0.00243; PE ROSE ~3.3x)
  - seed123 = **−0.47** (0.00144 -> 0.00211; PE rose ~1.5x)
  - seed456 = **+0.80** (0.00640 -> 0.00128; PE FELL ~5x; CONVERGED)
- **R1 `pe_response_range_to_novelty_shock` = −0.55** (threshold 0.25), evaluated on the ready seed (456): on the frozen converged model, PE under a max-novelty shock is *below* PE on the stable env (pe_shock 0.00098 < pe_stable 0.00218) — the WRONG direction.
- **C1 `mel_measurable_monotonic` (load-bearing) = FAIL**, scored on seed 456 only: mel_none 0.00160 / mel_high 0.00175 — flat; `rel_spread_ok=false`.
- **C2 `non_degenerate` = false** by the per-arm degeneracy check (each arm has only 1 ready seed contributing, so within-arm spread is zero) — i.e. with 1/3 seeds passing R2, the C1/C2 arm-level statistics are computed over a single seed and cannot be non-degenerate.

**Which criterion failed:** the two readiness preconditions (R2 dominant, then R1). No claim-bearing criterion was validly reached. Clean readiness self-route, not a claim test.

## 2. Claim-layer mapping

INV-050 is the architectural/invariant claim that sleep is regulated by a THIRD (MEL) drive proportional to accumulated waking prediction error. 701a tests ONLY the IV precondition (is MEL measurable + graded?), commitment-free, NO sleep machinery touched. The DV never spoke to INV-050 because the readiness gates failed. Correctly `non_contributory`; **INV-050 is not weakened.** Promotion held by INV-050's existing v3_pending / substrate-blocked status regardless.

## 3. Biological-reference triage

- Closest reference: sleep as homeostatic model-consolidation pressure scaling with the day's learning load (synaptic-homeostasis / SHY; Tononi-Cirelli). The IV (accumulated prediction error as a proxy for model-error load) is a faithful functional translation, not a formal-definition import. `lit_status: present`.
- The failure does NOT implicate the biological mechanism. It is upstream of any MEL claim: the diagnostic's own convergence READOUT is confounded, so there is no valid certification that the frozen base is a converged world model across seeds.

## 4. The central move — the seed-dependent "divergence" is substantially a CONVERGENCE-METRIC artifact

This is the decisive new finding, distinct from 701's "P0 trained the contrastive alone" root.

`conv_rel_drop = (pe_init - pe_final) / pe_init` is computed from **episode-rollout PE** — `per_ep_mean`, the mean per-step e3 prediction_error over the FREE-RUNNING agent's episode rollout (`_run_window` returns `per_ep_mean`; `run_cell` takes `pe_init` = mean of the first ~3 episode means, `pe_final` = mean of the last ~3; v3_exq_701a script lines 485-495, 486-489). It is **NOT a fixed held-out probe-state battery** — each episode the agent acts and PE is measured over whatever states it happens to visit.

The per-seed numbers expose the confound:

| seed | conv_pe_init | conv_pe_final | conv_rel_drop | n_meas_pe (ARM_0) |
|---|---|---|---|---|
| 42  | 0.00074 | 0.00243 | **−2.29** | 816 |
| 123 | 0.00144 | 0.00211 | **−0.47** | 327 |
| 456 | **0.00640** | 0.00128 | **+0.80** | 660 |

- The **final** PEs cluster tightly: 0.00243 / 0.00211 / 0.00128 — all within ~2x of each other. The model ends in roughly the same place on every seed.
- The **init** PEs vary **8.7x**: 0.00074 / 0.00144 / 0.00640. The "diverged" seeds (42, 123) are exactly the **low-init** ones.
- `conv_rel_drop` is dominated by its volatile init denominator. A fresh agent's episode-1 rollout visits few states (a tiny world model fits them -> tiny measured PE); by episode 60 it roams more (more diverse states -> higher measured PE), so the relative drop reads NEGATIVE even when the absolute final PE is small and clustered. The differing `n_meas_pe` per seed (816/327/660) corroborates differing per-seed exploration/coverage.

So R2 is **not cleanly unmet** — the readiness instrument conflates model convergence with exploration/coverage drift. This is the **V3-EXQ-642 canonical pattern** in a new guise: a `non_contributory` run whose substrate precondition was not *validly* tested, so the correct response is **re-queue with the precondition repaired**, NOT a substrate-ceiling reclassification.

**Crucially, the recon-anchor fix genuinely worked where measurable.** Seed 456 converged cleanly (conv_rel_drop +0.80), which 701 never achieved (701 had a run-level mean conv −2.60). The substrate is not hopeless; there is one partial valid read. On that valid converged base, R1 = −0.55 (novelty does not raise PE; it lowers it) and C1 is flat — the first genuine glimpse of the MEL-measurability ceiling on a valid frozen base — but n=1 ready seed is far too thin to certify a ceiling, especially when the gate that filtered the other two seeds is itself confounded.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | INV-050 IV precondition never validly reached; correctly non_contributory, never a weakens. |
| Biological reference | clear | Sleep-as-model-consolidation (SHY). Not the failing layer. |
| Prerequisites | measurement-confounded | The convergence GATE (episode-rollout `conv_rel_drop`) conflates model quality with exploration/coverage drift; it cannot reliably certify a converged base on a roaming agent. |
| Implementation | partial | The recon-anchor fix is correct (seed456 converged cleanly; 701 never did). The gaps are (a) the convergence-gate instrument and (b) 2/3-seed P0 stability. |
| Environment | adequate | CausalGridWorldV2 graded-drift novelty arms are well-formed; matched-activity NONE control present. |
| Measurement | under-instrumented for convergence | The MEL readout (raw per-step e3 prediction_error, frozen-window accumulation) is sound; the CONVERGENCE readout is the broken instrument. |
| Integration | n/a | Single-module diagnostic. |
| Scale / capacity | partial | recon + 60 ep moved 1/3 seeds; the prescribed fix did not fully stabilize the SD-056 world-forward P0 on the majority of seeds (this could be genuine instability OR the confounded metric mislabelling a fine model — 701b separates them). |

Recommended epistemic_category: **n/a (diagnostic, no claim status change).** evidence_direction `non_contributory`.

## 6. Lineage / re-derive brake

- INV-050: **1** prior `substrate_ceiling`/`non_contributory` autopsy under this tag (the 701 autopsy, 2026-06-23, non_contributory). This 701a is the **2nd** non_contributory autopsy under INV-050 -> the mechanical count reaches the default `RE_DERIVE_BRAKE_THRESHOLD` (2).
- **Brake does NOT fire (user-confirmed).** The brake exists to stop re-deriving the *same clean ceiling* letter-after-letter against an unchanged substrate. 701a is **NOT a clean ceiling read**: (1) the R2 readiness precondition is unmet, AND (2) the convergence GATE that filtered 2/3 seeds is demonstrably confounded (episode-rollout PE; 8.7x init-PE variance; tightly-clustered final PE). Firing the brake here — routing to substrate enrichment and refusing a re-queue — would reclassify a metric-confounded run as a MEL-measurability ceiling: exactly the "illusory conflict resolution" the autopsy rules warn against, and exactly the V3-EXQ-642 untrained/invalid-precondition lesson. The 701b re-queue is narrowly scoped to **repair the broken readiness instrument**, not to circle the same ceiling at the same granularity.
- **Brake-lock condition recorded for 701b:** if 701b's FROZEN-probe convergence metric (which removes the exploration-drift confound) STILL shows genuine multi-seed divergence on the stable env (i.e. the SD-056 world-forward P0 is *really* unstable, not a metric artifact), THEN that is the clean ceiling reading — the brake LOCKS, a same-claim test re-queue is refused, and routing moves to `/implement-substrate` on the SD-056 world-forward / world-model stabilisation substrate. The first clean R2-passing multi-seed read is still the decisive MEL-measurability test; 701b is the run that can finally produce it.

## 7. Learning extracted

1. The seed-dependent "divergence" (seeds 42/123 conv_rel_drop −2.29/−0.47) is substantially an artifact of the convergence GATE: `conv_rel_drop` is built from episode-rollout PE on a free-running agent, so episode-to-episode exploration/coverage drift inflates the late-episode denominator-relative PE. Init PE varies 8.7x while final PE clusters within ~2x — the model ends in the same place on every seed; the metric just can't see it.
2. The recon-anchor fix (the 701 prescription) is genuinely working where measurable: seed 456 converged cleanly (conv_rel_drop +0.80), which 701 never achieved at run level. So the substrate is not hopeless and the fix direction was right; the residual is the convergence-certification instrument + 2/3-seed stability.
3. On the one valid converged seed, R1 = −0.55 (novelty LOWERS PE) and C1 is flat — a first glimpse of a possible MEL ceiling — but n=1 ready seed (filtered by a confounded gate) is far too thin to certify it. A frozen-probe-metric 701b that certifies convergence honestly across seeds is the decisive test; only an R2-passing multi-seed flat-MEL result (or a genuine frozen-metric multi-seed divergence) resolves INV-050 MEL-measurability either way.

## 8. Routing decision (user-confirmed)

- `evidence_direction: non_contributory` CONFIRMED for INV-050 (NOT weakened; diagnostic, scoring-excluded). Self-route `substrate_not_ready_requeue` is correct per the pre-registered grid (the recon-primary P0 did not converge on enough seeds), with the autopsy refinement that the convergence-gate metric is itself confounded.
- **Routing: queue-experiment** — re-queue the MEL-measurability diagnostic (NEW letter, V3-EXQ-701b) with:
  - a **FROZEN held-out probe-state convergence metric**: certify P0 convergence by measuring per-step PE on a FIXED battery of probe states (the same states every episode, e.g. a pre-sampled fixed state set evaluated on the frozen-at-checkpoint model), removing the exploration/coverage-drift confound that makes the episode-rollout `conv_rel_drop` unreliable;
  - optionally also: lower `e2_lr` and/or drop / down-weight the SD-056 contrastive auxiliary term to test whether it is the 2/3-seed destabiliser (a clean diagnostic sub-arm: recon-only vs recon+contrastive P0 on the same frozen-probe metric);
  - keep the raw per-step e3 prediction_error + frozen-window MEL instrument unchanged (it fixed 677's batch-loss wash-out and is sound); keep commitment-free / no-sleep; keep the per-seed R2 gate but compute it on the frozen-probe metric.
- `recommended_substrate_queue_entry.action = none` — no missing mechanism is yet established; the immediate fix is the diagnostic's convergence-certification instrument (test-bed construction), not substrate enrichment. The enrichment path is **pre-staged but conditional**: if 701b's frozen-probe metric confirms genuine multi-seed divergence, THAT result routes to `/implement-substrate` on the SD-056 world-forward stabilisation substrate and fires the re-derive brake on that clean reading.
- Re-derive brake NOT fired (the 701a reading is confounded, not a clean ceiling); brake-lock condition recorded for the 701b frozen-probe result.

### Draft `evidence_quality_note` (for governance to write — diagnostic, no claim status change)

> V3-EXQ-701a (2026-06-23, failure-autopsy): INV-050 MEL-measurability converged-P0 re-run (supersedes 701), non_contributory CONFIRMED (NOT a verdict on INV-050; diagnostic, scoring-excluded). The recon-primary + 60ep + per-seed-R2 fix converged only 1/3 seeds (conv_frac 0.333 < 0.667; per-seed conv_rel_drop seed42 −2.29 / seed123 −0.47 / seed456 +0.80). DECISIVE autopsy finding: the convergence GATE (`conv_rel_drop` from episode-rollout PE) is exploration-confounded — init PE varies 8.7x (0.00074..0.0064) while final PE clusters within ~2x (0.0013..0.0024), so the low-init "diverged" seeds are a metric artifact, not a fine vs broken world model. This is the V3-EXQ-642 invalid-precondition pattern, not a substrate ceiling. The recon-anchor fix WORKED where measurable (seed456 converged cleanly; 701 never did). Route: re-queue (V3-EXQ-701b) with a FROZEN held-out probe-state convergence metric (+ optional e2_lr / contrastive-aux ablation); no substrate_queue entry; re-derive brake NOT fired. Brake-lock condition: if 701b's frozen-probe metric still shows genuine multi-seed divergence, that is the clean ceiling -> route to /implement-substrate on the SD-056 world-forward stabilisation substrate + fire the brake then. On the one valid converged seed, novelty did not raise PE (R1 −0.55, C1 flat) — a first glimpse of a possible MEL ceiling, but n=1 ready seed under a confounded gate is too thin to certify.
