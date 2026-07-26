# Failure Autopsy (CLUSTER) — V3-EXQ-816 + V3-EXQ-820

**Policy decomposition (ARC-070 / MECH-321): the vacuous R1-vs-R5-vs-OFF dissociation**

- **generated_utc:** 2026-07-26T05:38:01Z
- **scope:** cluster (two runs, one structural property)
- **status:** confirmed
- **claims:** ARC-070 (architectural_commitment), MECH-321 (mechanism_hypothesis) — both `candidate`, `v3_pending: true`, `implementation_phase: v3`
- **recommended category:** `standard` (env / precondition-not-ready — **NOT** `substrate_ceiling`)
- **evidence_direction:** `non_contributory` per claim (both ARC-070 and MECH-321); pure diagnostic legs → `bears_on`, no weight for or against either claim
- **routing:** `queue-experiment` — a GOV-FANOUT-1 **discrimination portfolio** (user-confirmed at the Step 8 gate)
- **surfaced by:** 2026-07-25 `/governance` cycle (session `angry-ardinghelli-d99740-gov`, REE_assembly `19956b0a2f`), both left pending route B.

---

## 1. Scope

| Run | Design | Outcome | Self-route |
|---|---|---|---|
| V3-EXQ-816 | ARM_0 (OFF) vs ARM_1 (R1 = V_s-drop trigger). Behavioural discriminative: does R1 decomposition reduce **low-V_s** execution-time forward-PE vs OFF? | FAIL | `substrate_not_ready_requeue` |
| V3-EXQ-820 | + ARM_2 (R5 = bottleneck-state trigger). Completes the R1-vs-R5-vs-OFF three-arm dissociation. | FAIL | `substrate_not_ready_requeue` |

Both are diagnostic legs of a single discrimination portfolio for the same claim pair. They share **one** root cause, so this is a cluster autopsy (Step 6).

The runs **ran to completion** (816: 12251 s on `ree-worker-1`; 820: 4724 s on `ree-worker-3`; 5 seeds each: 11/23/47/71/97). This is an autopsy target, not a `/diagnose-errors` case — there is no crash.

---

## 2. Facts reconstruction

Both manifests self-route `substrate_not_ready_requeue`, carry `evidence_direction: unknown` (per-claim unknown for ARC-070 and MECH-321), and `non_degenerate: false`.

**The identical load-bearing precondition failure.** In BOTH runs the precondition `vs_heterogeneity_low_vs_steps_present` FAILED:

- measured `0.0` low-V_s steps vs threshold `5.0` (worst ARM_1 cell)
- `low_vs_step_frac = 0.0` across **all** arms, **all** 5 seeds, in **both** runs
- `fwd_pe_lowvs_n = 0` everywhere; `decomp_n_vs_trigger = 0` everywhere
- 816 `degeneracy_reason`: *"V_s never dropped below decomposition_vs_threshold in a majority-sufficient way (worst ARM_1 cell had 0 low-V_s steps < 5); the R1 trigger's V_s half could not be exercised."*
- 820 `degeneracy_reason`: *"V_s never dropped below threshold sufficiently (worst ARM_1 cell had 0 low-V_s steps < 5); the high/low-V_s partition is not exercisable."*

**Everything else worked.** Every positive/negative control passed:

- OFF positive control: committed-trajectory forward-PE **varies** (`off_pe_var_worst ≈ 2.16e-8 > 1e-12`) and is **bounded** (`off_pe_mean_worst ≈ 0.009 < 1e3`). The world_forward model learned something.
- The **decomposition machinery fires abundantly**, but only at high-V_s / structural loci:
  - 816: `decomp_fired_frac_arm1 = 1.0`; `decomp_n_decomposed_precommit = [225,186,180,218,224]`.
  - 820: ARM_1 `arm1_decomp_fired_frac = 1.0`; ARM_2 `arm2_bottleneck_fired_frac = 1.0`, `arm2_bottleneck_fires_total = 1524`, `arm2_events_total = 484`, `arm1_events_total = 334` (`p3_enough_events` = min 334 ≥ 5).
- Arms **behaviourally diverge**: `any_action_divergence = true` (816), `arm2_action_divergence = true` (820) — the manipulation is live, not inert.

**The consequence.** The R5 bottleneck trigger (820 ARM_2) fires everywhere and produces action divergence; the R1 V_s-drop trigger fired **zero** times in either arm of either run (`arm1_vs_trigger_total = 0`, `arm2_vs_trigger_total = 0`). So `dissociation_high_vs_frac = 0.0`, `dissociation_ok = false`, `readiness_met = false`, and the load-bearing criteria (`C_MAIN_lowvs_forward_pe_reduced` in 816; `C_MAIN_arm2_decomposes_at_high_vs` in 820) could not be evaluated (`n_paired_seeds = 0`, `delta_mean_lowvs_fwd_pe = 0.0`). **The R1-vs-R5-vs-OFF dissociation is vacuous:** the two trigger regimes were never separated, because the environment never entered the low-V_s (high-prediction-uncertainty) regime that separates them.

**Which criterion failed:** the **discrimination** criterion (load-bearing `C_MAIN_...`). The **absolute / positive-control** criteria all passed. Note this is *not* the classic substrate-ceiling fingerprint ("negative control passes, discrimination fails *because the substrate is too coarse*") — here the discrimination criterion never ran at all because its **precondition** (env producing low-V_s states) was unmet.

**Recording provenance.** The always-record core is **present and clean** in both: `recording_schema: rec/v1`, top-level `substrate_hash` (816: `521c92…`; 820: `2e2f0d…`), `machine` / `machine_class` (`linux-x86_64-py3.10-torch2.12.0+cpu`), `elapsed_seconds`, full `config`, explicit `seeds`. This is **not** a core recording gap. One family-specific readout **is** missing, however (see §5): the manifest records the *derived* `low_vs_steps` (0) but **not the region-V_s distribution itself** (min/mean/max/histogram per cell). That is the readout that would let a future run decide *how far* V_s was from crossing the threshold — a family-specific recording gap the re-queue must close.

---

## 3. Claim-layer mapping

Both ARC-070 and MECH-321 are `candidate`, `v3_pending: true`. These two runs were the intended v3 evidence to clear the pending gate.

- **ARC-070** (`architectural_commitment`, depends_on ARC-069): names the decomposition direction — when a chunked primitive's predicted outcome is unreliable, re-segment into finer primitives. Its `functional_restatement` lists the trigger candidates explicitly, R1 first: *"MECH-269 V_s drop on the chunk's region: low region V_s means the agent cannot reliably predict outcomes in this region … the cleanest existing-substrate trigger"* — **and** *"E2 forward-model disagreement"* as an alternative.
- **MECH-321** (`mechanism_hypothesis`, depends_on ARC-070, MECH-288, MECH-269, MECH-094): the policy-side consumer of MECH-288 rollout boundary pulses. Per-rollout-step: `if v_s < v_s_decompose_threshold OR boundary.fired: decompose(p)`.

**Did the test let the claim express itself?** No. The claim asserts an effect *conditional on* a region being unpredictable (low V_s / boundary-fired). The V_s half of that condition was **never satisfied** in the measurement window. The boundary/bottleneck half fired and drove behaviour, but that alone cannot test the *V_s-drop* trigger the claim leads with, nor the R1-vs-R5 dissociation. **Claim alignment: intact (untested).** A precondition-unmet run must not demote a v3_pending architectural/mechanism claim — the FAIL touches the environment/instrument layer, not the claim.

---

## 4. Biological-reference triage

- **Closest mechanism:** PE-driven event segmentation (Zacks 2007) applied to a candidate's imagined continuation, with chunk-size bounds from Sakai 2003 — the mechanism has a solid biological existence proof for the *class*.
- **Formal-import check:** the mechanism itself is biologically grounded (a lit-pull `targeted_review_arc_070_decomposition` already exists; MECH-321 folded R1–R5 verdicts into its functional_restatement). It is **not** an un-grounded formal import.
- **The one operationalization risk** is *not* the mechanism but the **trigger's readout**: the implemented region V_s is `HippocampalModule._region_vs()` = mean `per_stream_vs` = a **"1 − relative-tick-to-tick-latent-change" stability proxy**, whereas the claim's own gloss reads V_s as *"cannot reliably predict outcomes"* (i.e. forward-model PE). The 816 docstring flags this honestly: *"region V_s is a stability proxy NOT forward-model PE … 'a low-V_s region is one where a committed chunk's forward prediction fails' is exactly the hypothesis under test, not an identity."* Whether latent-stability-V_s and forward-PE co-occur is unresolved — and the run produced **neither** (no low-V_s regions AND near-zero forward-PE everywhere), so it did not discriminate them.
- **Missing-dependency signature?** Yes, but env-side, not substrate-side: the failure resembles a working mechanism whose *triggering condition never arose*, because the world was fully learned by measure time. That is an impoverished-environment / developmental-window signature, not a falsification.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (untested) | precondition unmet; the FAIL does not reach the claim |
| Biological reference | clear | Zacks 2007 PE-segmentation; lit entry present. Trigger *readout* (V_s-stability vs forward-PE) is the one open operationalization question |
| Prerequisites | present | depends_on (ARC-069/MECH-288/MECH-269/MECH-094) implemented; `use_per_stream_vs=True` constant across arms — the degenerate constant-1.0 V_s fallback is **ruled out**, V_s tracking is live |
| Implementation completeness | complete | trigger machinery fires abundantly (816 decomp 1.0; 820 bottleneck 1524×). ARM_2 R5 mode built (ree-v3 `2422632`, `decomposition_trigger_mode`) |
| **Environment adequacy** | **too easy / wrong window** | 8×8 grid, 3 hazards, `env_drift_interval` default (5), **40 warmup episodes** → by the 20-episode measure window the forward model has near-zero PE (`fwd_pe_all_mean ≈ 0.005`, `var ≈ 1e-7`). No persistent prediction uncertainty → no low-V_s regions |
| Measurement adequacy | under-instrumented (partial recording gap) | manifest records derived `low_vs_steps` (0) but **not the region-V_s distribution** — cannot tell whether V_s saturated near 1.0 (deep) or hovered just above 0.5 (shallow). Re-queue must record it |
| Integration adequacy | coupled | modules interoperate; the R5 path drives behaviour end-to-end |
| Scale / capacity | adequate | not a capacity limit |

**Dominant diagnosis:** environment / precondition-not-ready (with a second, instrumentation-side reading, below). **Recommended `epistemic_category`: `standard`.** This is explicitly *not* `substrate_ceiling`: the substrate carries and fires the mechanism; the environment failed to exercise the discriminating regime.

**Recording-debt vs measurement-debt.** Partly recording-debt (the region-V_s distribution existed at run time but was not written — close it per the Experimental Recording Standard, §3c family-keyed payload), but **not purely** — even a re-run that records V_s would still show V_s ≥ 0.5 unless the *environment* is changed to produce the low-V_s regime. So the fix is a redesigned env **plus** recording, routed to `/queue-experiment`, not a blind same-env re-run.

---

## 6. Cluster pattern

| Experiment | Claim | Absolute / positive-control criterion | Discrimination criterion | Read |
|---|---|---|---|---|
| V3-EXQ-816 | ARC-070, MECH-321 | PASS (OFF forward-PE varies + bounded; decomp fires frac 1.0) | FAIL — `C_MAIN_lowvs_forward_pe_reduced` never evaluable (`n_paired_seeds = 0`) | R1 V_s-drop trigger never fired (0 low-V_s steps) |
| V3-EXQ-820 | ARC-070, MECH-321 | PASS (ARM_1 + ARM_2 fire; 334/484 events) | FAIL — `C_MAIN_arm2_decomposes_at_high_vs` dissociation vacuous (`dissociation_high_vs_frac = 0.0`) | R5 fires abundantly, but R1 never fires anywhere → no contrast |

**These are NOT two independent bugs. They are ONE structural property:** *the environment, as configured and after 40 warmup episodes, never produced low-V_s (high-prediction-uncertainty) states in the measurement window, so the R1 V_s-drop trigger's condition was never satisfied.* 820 merely adds the R5 arm on top of 816's design; the R5 arm works, but its dissociation from R1 is vacuous for the identical reason 816 failed (`lowvs_worst_arm1 = 0` in both). The convergent shape across the two-arm and three-arm designs is the load-bearing signal: the bottleneck is the env's prediction-uncertainty distribution, not any per-run tuning noise.

---

## 7. Learning extracted & repair pathway

**Learning:**
1. On this env (8×8, 3 hazards, `env_drift_interval` default, 40-episode warmup), the trained forward model reaches near-zero PE by the measure window, so region-V_s (a latent-stability proxy) never drops below 0.5 — the R1 V_s-drop trigger is structurally un-exercisable there. The threshold was already raised 0.4→0.5 in anticipation and still got 0 low-V_s steps.
2. The R5 bottleneck trigger keys on visitation/graph structure (funnel states), which exists independent of V_s — so R5 fires and drives behaviour even when R1 cannot. This confirms the R5 build works, but makes R5 an unsuitable *stand-in* for testing R1.
3. **Open operationalization question (claim-relevant):** region-V_s-stability and forward-model-PE may be **decoupled** in a trained encoder. MECH-321's functional_restatement itself lists "E2 forward-model disagreement" as an alternative trigger — so this is not merely a measurement nit, it bears on which trigger the claim should commit to.
4. Recording gap: log the region-V_s distribution (not just the derived low-V_s count) so the next run can tell saturation-near-1.0 from just-above-threshold.

**Debt-vocabulary classification:** `complex (probe-gated)`. The observation bottleneck is real; *which* fix applies (env-side vs instrumentation-side) is a missing fact obtained by a spike. Because there are ≥2 live hypotheses on **different design axes**, GOV-FANOUT-1 applies → fan out a **portfolio**, not one sequential env-harshen letter.

**Routing (user-confirmed): `queue-experiment` fan-out portfolio.** `recommended_substrate_queue_entry.action = "none"` — no single named substrate BUILD is warranted yet: the env fix is a **driver-config** lever (the knobs already exist; V3-EXQ-677 used `env_drift_interval 999→3` to force a high-vs-low PE contrast), and the proxy reading is a **measurement/trigger reframe**. The spike decides which.

### Fan-out portfolio (GOV-FANOUT-1)

Two live hypotheses about the observation bottleneck, each probed on a different axis, each with a declared null:

- **H-env-underdrives-uncertainty** (axis: `environment`). The default env under-drives persistent prediction uncertainty by measure time; a harsher / non-stationary env (`env_drift_interval → 3`, `background_drift_enabled`, or a shorter warmup / larger grid) produces both forward-PE heterogeneity **and** low-V_s regions.
  - **Probe P-A:** re-run the 816 design with a harshened env and **record the region-V_s distribution + per-cell forward-PE**. *Null:* even at faster drift, worst-cell low-V_s steps remain `< MIN_LOW_VS_STEPS` (V_s does not drop) → H-env refuted, H-vs-proxy-saturation favoured. *Fix if confirmed:* driver-config re-queue under a new letter (816b / 820b).
- **H-vs-proxy-saturation** (axis: `measurement`). Region-V_s (latent-stability) structurally saturates near 1.0 in a trained encoder and is **decoupled** from forward-model PE, so no env manipulation lowers it and the R1 V_s-drop trigger cannot fire in a competent agent.
  - **Probe P-B:** add a forward-PE / per-region-PE **comparator** trigger alongside the V_s trigger and record where each fires (a harshened env from P-A can host it). *Null:* forward-PE heterogeneity is present (PE-trigger fires) while V_s heterogeneity is absent (V_s-trigger silent) → the two are decoupled → H-vs-proxy-saturation confirmed, and MECH-321's R1 trigger operationalization must be reframed toward the claim's own forward-model-disagreement alternative (candidate `/claim-synthesis` on trigger operationalization).

A single well-instrumented harshened-env leg (record V_s distribution **and** forward-PE per cell) can discriminate both at once; P-B adds the parallel comparator to make the decoupling directly observable. Design-audit for coverage + verdict-aliasing before queuing.

### Re-derive brake

**Does NOT fire.** Prior `substrate_ceiling` autopsies (R1–R3 convention, confirmed-only) for **ARC-070: 0**, **MECH-321: 0** — this is the first autopsy of the lineage; no prior autopsy tags either claim. This reading is `standard`, not `substrate_ceiling`, so it does not itself add a ceiling hit. Every target below carries `recommended_epistemic_category = "standard"` stamped explicitly (so GOV-CAT-1 / GOV-CEIL-1 counts stay correct).

### Granularity-debt recurrence trigger

**Does NOT fire.** This is the first autopsy circling ARC-070 / MECH-321 (0 prior tagging targets); the trigger needs ≥2 with a `weakened` alignment, and this one is `intact (untested)`. The H-vs-proxy-saturation reading is flagged as a *candidate* future `/claim-synthesis` on MECH-321's trigger operationalization **only if** P-B confirms the decoupling — it is not a granularity-debt firing today.

---

## Draft `evidence_quality_note` (for `/governance` to write — do not write here)

> **ARC-070 / MECH-321 (non_contributory, standard):** V3-EXQ-816 (ARM_0/ARM_1) and V3-EXQ-820 (+ARM_2) both FAILed on an unmet precondition — `vs_heterogeneity_low_vs_steps_present` measured 0 low-V_s steps (threshold 5) in every arm/seed of both runs. The decomposition machinery fired abundantly (816 decomp frac 1.0; 820 bottleneck 1524×) and arms diverged behaviourally, but the R1 V_s-drop trigger never fired (0 vs-triggers) because the trained forward model reached near-zero PE (≈0.005) by the measure window, so region-V_s never dropped below 0.5. The R1-vs-R5-vs-OFF dissociation is therefore vacuous. This weights **neither** claim; both stay `candidate` / `v3_pending`. Retest gated on a fan-out spike (`/queue-experiment`) that first produces low-V_s states — H-env (harsher env: `env_drift_interval→3` / `background_drift`; cf. V3-EXQ-677) vs H-vs-proxy-saturation (region-V_s-stability decoupled from forward-PE) — recording the region-V_s distribution. See `failure_autopsy_816-820-policy-decomposition-cluster_2026-07-26`.

---

## Routing decision (confirmed at Step 8 gate, 2026-07-26)

- Category: **standard** (env / precondition-not-ready). Not substrate_ceiling; not a claim demotion.
- Evidence direction: **non_contributory** for both ARC-070 and MECH-321; diagnostic legs → `bears_on`.
- Route: **`queue-experiment`** — GOV-FANOUT-1 discrimination portfolio (P-A env axis, P-B measurement axis), both pre-registered in the frozen ledger (§9b).
- No substrate build queued (`recommended_substrate_queue_entry.action = "none"`).
- Both claims stay `candidate` / `v3_pending`; `pending_retest_after_substrate = false` (retest is gated on the env/measurement spike, not a substrate build).
