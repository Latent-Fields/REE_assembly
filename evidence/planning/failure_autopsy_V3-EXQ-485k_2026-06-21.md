# Failure Autopsy — V3-EXQ-485k (SD-033b re-ranking-devalued behavioural; demotion-enabled selector)

- **generated_utc:** 2026-06-21T19:40:23Z
- **status:** confirmed (user-adjudicated 2026-06-21)
- **scope:** single (with an explicit autopsy-stream recurrence note, §6)
- **run_id:** v3_exq_485k_sd033b_demotion_devalued_rerank_behavioural_20260621T192541Z_v3
- **queue_id:** V3-EXQ-485k  (machine ree-cloud-2; supersedes V3-EXQ-485j)
- **claim_ids (manifest):** SD-033b, MECH-263
- **manifest self-route:** FAIL / evidence_direction=`non_contributory` / `non_degenerate:false` / interpretation.label=`substrate_not_ready_requeue`. Self-route **CONFIRMED** (readiness genuinely unmet) but its *stated cause* and its *display* are corrected here (§2, §7); left PENDING by governance-cycle-20260621T1919Z, no evidence stamp owed.

---

## 1. One-line verdict

The C1-devaluation conversion does not fail because the re-ranking driver "didn't engage" — it fails because **demotion-alone (eligibility access) cannot express an active No-Go *withdrawal* of the previously-preferred action**, which is what behavioural outcome-devaluation *is*. The OFC head's re-ranking is real (the bias vector inverts: cosine −0.71/−0.57 on 2/3 seeds) but it can only act by *out-magnituding* F within the F-eligible set, so it saturates the ±0.5 bias clamp uniformly → readable range collapses to **exactly 0.0** on 2/3 seeds → readiness unmet. This is the ARC-107 constitution's **"demotion alone insufficient"** trigger (design note line 171/243), now cleared by the six-autopsy 485e→k lineage. The corrected residual is **substrate-incompleteness (MECH-449 Go/No-Go not built) + an un-adopted channel-adaptive envelope**, NOT a standalone driver-tuning sweep.

The autopsy question — "tune the driver" vs "MECH-448 doesn't generalise" — is again the wrong binary. The answer is **(c): the demotion lever generalised the *discrimination* signature (sig-b, converted in 485j), but the *devaluation* signature (sig-a) is an active withdrawal that needs the No-Go pathway demotion-alone does not provide.**

---

## 2. Facts — reconstruction (no interpretation)

### Acceptance (BOTH load-bearing DVs vacuous)

| Criterion | load-bearing | per-seed | n_seeds | non_degenerate | verdict |
|---|---|---|---|---|---|
| C1_devaluation_behavioural_shift | yes | 0 / 0 / 1.0* | 1/3 | **false** | FAIL |
| C2_discrimination_behavioural_separation | yes | 0 / 0 / 0 | 0/3 | **false** | FAIL |
| C3_silence_control | yes | held | 3/3 | true | PASS |

`criteria_non_degenerate = {C1:false, C2:false, C3:true}`. *seed-2's C1 shift=1.0 is spurious (devalued range=0.0, winner==F-argmin) — an incidental argmax flip, not a re-ranking, and C1 needs ≥2/3.

### The aggregate-precondition / per-seed-readiness mismatch (the "all met=True yet readiness unmet" puzzle)

`interpretation.preconditions[*].met` all read **True** because each `measured` is an **aggregate max over the 3 ARM_2 seeds** (`max_test_*`). `readiness_met` is a **per-seed 2-of-3 conjunction** (`ready_seeds ≥ MIN_PASS_SEEDS=2`). The maxes come from *different seeds*:

| precondition | reported (aggregate max) | from seed | floor | per-seed pass |
|---|---|---|---|---|
| high-threat bias range | 0.4228 | s1 | 0.05 | s0 ✓ s1 ✓ s2 ✓ (3/3) |
| **devalued bias range (FIX-2, the C1 statistic)** | **0.1071** | **s0** | 0.05 | **s0 ✓ s1 ✗ s2 ✗ (1/3)** |
| head weight-delta | 5.635 | — | 0.001 | 3/3 |
| MECH-448 excluded_count | 5.0 | — | >0 | 3/3 |

Only **seed 0** clears the devalued floor + head + eval-built → `ready_seeds=1` → `readiness_met=False`. **The `met=True` panel masks the per-seed collapse** — the meta-version of the V3-EXQ-642 same-statistic lesson: the displayed statistic (aggregate max) is not the one the gate routes on (per-seed 2-of-3). The self-route to `substrate_not_ready_requeue` is therefore *correct*, but the manifest's `degeneracy_reason` text ("head untrained, OR envelope all-admit, OR below floor") mis-names the cause.

### ARM_2 per-seed (code-confirmed extraction)

| ARM_2 seed | range_hi | range_dev | `devaluation_bias_l2_shift` | `devaluation_bias_cosine` | excl_count | winner≠F | deval_shift | between_tv | ctxA / ctxB range |
|---|---|---|---|---|---|---|---|---|---|
| s0 | 0.226 | **0.107** ✓ | 0.118 | **+0.986** (small re-rank) | 5 | True | 0.0 | 0.0 | 0.160 / 0.075 |
| s1 | **0.423** | **0.000** ✗ | 1.876 | **−0.706** (vector inverts) | 5 | True | 0.0 | 0.0 | 0.151 / 0.000 |
| s2 | 0.147 | **0.000** ✗ | 1.516 | **−0.566** (vector inverts) | 4 | False | 1.0* | 0.0 | 0.000 / 0.000 |

The MECH-448 demotion envelope **fired correctly** (excluded 4–5 of 8; winner≠F-argmin on 2/3) — not the failure locus.

### The clamp-saturation mechanism (script-confirmed)

- C1 reads `TV(onehot(idx_high), onehot(idx_low))`: committed selection after settling to high-threat vs devalued state_code (`_demotion_committed_eval`).
- FIX-1 replaced the 485h/485j anti-range variance penalty with an **inverted re-ranking REINFORCE term** (`adv_dev = DEVALUED_RERANK_GAIN(4.0) * (harm - harm.mean())`, weight 0.5; script lines 638-653). The secondary readouts prove it *works*: on s1/s2 the bias vector shifts massively (l2 1.88/1.52) and the cosine goes **negative** — the high→devalued re-ranking signature.
- `compute_bias` clamps to ±`ofc_bias_scale` (0.5). The overstrong term drives **all** candidates to the *same* rail at the devalued state → cross-candidate range = **exactly 0.0** despite the large vector shift (uniform saturation). This is the GAP-8 clamp-saturation mode CLAUDE.md explicitly warns about. Where the re-rank stayed in-band (s0, cosine +0.99) the range survived (0.107) but was too gentle to move the committed argmin (shift=0).

**Which criterion failed, and why:** discrimination (C1's `devaluation_selection_shift` and C2's `between_context_tv`) — but the C1 failure is a *clamp-saturation non-vacuity breach on the devalued range*, and the C2 failure is a *driver-coupling regression* (next).

---

## 3. Claim-layer mapping (did the test let each claim express itself?)

| claim | status / category | tested fairly? |
|---|---|---|
| **MECH-448** (rank-preserving F→eligibility demotion) | provisional / standard | **Not tagged; not weakened.** The envelope fired (excl 4–5, winner≠F on 2/3). 485k re-confirms the demotion lever engages on the OFC bank. |
| **MECH-263 sig-b** (task-role discrimination) | candidate / substrate_ceiling / v3_pending / pending_retest | **Converted on demotion-alone in 485j** (between_tv 1.0 on 2/3). In 485k it **REGRESSED to 0/3** — a *driver-coupling* cost of FIX-1, NOT evidence against the claim (see §5). |
| **MECH-263 sig-a** (devaluation sensitivity) | (same claim; sig-a enumerated separately) | **Not testable on demotion-alone.** Devaluation is an active *withdrawal* of the preferred action — it needs a No-Go pathway. Demotion (eligibility access) forces the OFC re-rank to out-magnitude F → clamp saturation. → **substrate_conditional / blocked on MECH-449**, not a fair weakens. |
| **SD-033b** (OFC substrate) | candidate / substrate_ceiling / v3_pending=False / pending_retest | Same split: discrimination half is demotion-tractable; devaluation half is blocked on the Go/No-Go constitution. |

The manifest's blanket self-route does NOT weaken (non_degenerate:false → scoring_excluded). No overturn needed; this autopsy confirms non_contributory and reclassifies the *devaluation* residual to substrate_conditional.

---

## 4. Biological-reference triage

OFC outcome-devaluation (Rudebeck & Murray 2014; Dickinson & Balleine) is a faithful biological target — no `/lit-pull` needed (`lit_status: present`). The mammalian devaluation signature is an **active behavioural withdrawal**: devalue an outcome and the agent *stops emitting* the action that leads to it. In the basal ganglia this is the **indirect / No-Go pathway** suppressing the previously-Go action while the OFC re-values (Mink 1996 focal-go + surround-no-go; Hikosaka 2000 SNr permission gate; Maia & Frank 2011 Go/No-Go). REE's demotion envelope (MECH-448) implements **eligibility access only** — it removes F's *dominance* over the final argmin but provides **no oppositely-signed No-Go pressure** to actively suppress the devalued candidate. So a devalued OFC valuation has only one route to a committed shift: out-magnitude F within the eligible set — which the ±0.5 clamp converts into uniform saturation. **This is a discovered prerequisite (the Go/No-Go constitution must be in concert), not a falsification of MECH-263 sig-a.** The discrimination signature (sig-b) needs no withdrawal — it is a passive re-ranking of *which* eligible candidate wins — which is exactly why it converted on demotion-alone in 485j.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **strengthened (sig-b, 485j) / blocked (sig-a)** | MECH-448 demotion + sig-b discrimination corroborated; sig-a not expressible without No-Go |
| **Biological reference** | **clear (load-bearing)** | devaluation = active No-Go withdrawal; demotion = eligibility access only → the missing-machinery diagnosis |
| Prerequisites / dependency | **missing (MECH-449)** | trained head + demotion envelope present, but the Go/No-Go pathway the devaluation-withdrawal needs is NOT built (substrate_conditional) |
| Implementation completeness | **partial** | FIX-1 re-rank overshoots the ±0.5 clamp → uniform saturation; the single shared OFC head couples devaluation-training to discrimination |
| Environment adequacy | adequate | OFC-isolated SD-054 bipartite reef/forage bank |
| **Measurement adequacy** | **misleading (load-bearing)** | (a) `interpretation.preconditions` report aggregate maxes that mask the per-seed 2-of-3 readiness collapse; (b) the committed-argmax-TV C1 DV is blind to clamp-saturated re-ranking (the l2/cosine secondary readout catches it but is not a gate) |
| Integration adequacy | **coupled but unstable** | one OFC head must do BOTH re-ranking devaluation AND task-role discrimination; tuning the devalued driver (FIX-1) destabilised C2 |
| Scale / capacity | clamp-bound | the ±0.5 bias clamp is the binding ceiling on readable range |

**Dominant diagnosis → substrate_conditional (sig-a devaluation blocked on the MECH-449 Go/No-Go constitution)**, compounded by a measurement-display gap (aggregate-max precondition panel) and a driver-coupling regression (C2). The C2 regression is a *real, fixable* driver-coupling cost (485j proved sig-b converts when the devalued term does not swamp the high-threat spread).

---

## 6. The recurrence (autopsy-stream signal) — `/claim-synthesis` discharged

This is the **6th** autopsy artifact circling the SD-033b/MECH-263 OFC behavioural conversion:

| run | signature | route |
|---|---|---|
| 485e | range-starved bank | instrumentation |
| 485g | first non-vacuous; discrimination FAIL | queue-experiment |
| 485h | threat-invariant REFUTED (paired driver closed the gap) | implement-substrate |
| 485i | MECH-448 envelope all-admit no-op (excluded_count==0) | implement-substrate (calibrate floor) |
| 485j | demotion engaged (excl=5); **C2 converted**, C1 devalued-range collapse (flat anti-range) | queue-experiment |
| **485k** | demotion engaged (excl 4–5); **C1 clamp-saturation overshoot + C2 regression**; readiness 1/3 | **this autopsy → MECH-449 build** |

**This is NOT granularity debt requiring `/claim-synthesis`.** MECH-263 is already decomposed into sig-a (devaluation) + sig-b (discrimination), and the conversion-ceiling family is already owned by the ARC-107 constitution (MECH-447/448/449, claim_synthesis discharged in the f-dominance-conversion-cluster autopsy). The lineage is a **convergent sequence** that has now produced the decisive structural finding: **demotion-alone converts sig-b but not sig-a — the design note's "demotion alone insufficient" gate (line 171/243) is cleared.** Recorded for audit; `/claim-synthesis` hook discharged.

Separately, the lineage exposes a **per-channel-config circle** (485i/485j bespoke `_calibrate_envelope_floor`; 654h all-admit no-op; pending 625/445/687) that the just-landed `use_f_eligibility_adaptive_floor` (mean-relative, scale-invariant) was built to collapse into one knob — and **689e already validates it on the OFC channel**. Adopting the adaptive envelope is the standing fix for that axis.

---

## 7. Learning + routing (user-confirmed 2026-06-21)

**Learning extracted:**
1. **Demotion-alone converts the discrimination signature (sig-b) but not the devaluation signature (sig-a).** Discrimination is a passive re-ranking of which eligible candidate wins; devaluation is an active No-Go *withdrawal*. The MECH-448 eligibility envelope provides access, not suppression — so devaluation can only act by out-magnituding F, which clamp-saturates. **The 485e→k lineage clears the ARC-107 "demotion alone insufficient" gate that triggers the MECH-449 Go/No-Go build.**
2. **`interpretation.preconditions` that report aggregate maxes can mask a per-seed 2-of-3 readiness collapse** (the meta-version of the V3-EXQ-642 same-statistic miss). The panel should report the binding per-seed pass-count, not max-over-seeds.
3. **FIX-1's re-ranking devalued driver regressed C2** (1.0/0.0/1.0 → 0/0/0): a strong devalued term co-opts the single shared OFC head and destabilises the high-threat spread that drives discrimination. The two fixes are not independent.
4. **The per-channel envelope-floor circle is real and already has a fix** (`use_f_eligibility_adaptive_floor`, 689e validates on OFC). Re-queuing a standalone OFC behavioural arm with another bespoke floor/driver sweep is chasing that circle.

**Routing: `implement-substrate` — MECH-449 Go/No-Go eligibility constitution (build gate cleared).** The ARC-107 design note gates the MECH-449 build on "MECH-448 proves insufficient"; the six-autopsy demotion-alone non-conversion of the OFC *withdrawal* signature is that demonstration. Governance should clear the MECH-449 build gate (chip the Go/No-Go constitution build, per arc_107_selector_constitution_design §3.2). **NOT** another standalone `/queue-experiment` 485l on demotion-alone (chasing the circle). **NOT** envelope-floor recalibration (the envelope fired correctly).

**Gated follow-on (carried, NOT queued now):** the corrected OFC devaluation behavioural arm = **tune the re-rank gain so the devalued bias stays in-band on ≥2/3 seeds** (or soften/raise the ±0.5 clamp + pre-clamp magnitude regulariser per GAP-8) **+ protect C2** (reduce/phase the devalued term so the high-threat spread survives) **+ promote the bias-VECTOR re-ranking (l2_shift/cosine) to a guarded scored DV** (with a non-saturation readiness check) **+ adopt `use_f_eligibility_adaptive_floor`** (pending 689e). Queue this as **V3-EXQ-485l ONLY AFTER MECH-449 is built and 689e validates the adaptive envelope on OFC** — so the behavioural arm runs on the complete Go/No-Go constitution, not demotion-alone.

**Governance impact (PROMOTES NOTHING):**
- **MECH-448:** not tagged, not weakened (envelope fired correctly).
- **MECH-263 sig-b / SD-033b discrimination:** narrow-supports stands from 485j; the 485k regression is a driver-coupling artifact, not new evidence — do not let it weight conflict ratio (already non_degenerate:false).
- **MECH-263 sig-a / SD-033b devaluation:** **non_contributory / substrate_conditional**, blocked on MECH-449, `pending_retest_after_substrate`. Reclassify the devaluation residual from "needs more driver tuning" to "needs the Go/No-Go constitution."
- **MECH-449:** the build gate is **cleared** (demotion-alone insufficient demonstrated). Surface to governance to chip the build.
- **commitment_closure:GAP-8** (SD-033b candidate→provisional behavioural evidence): unchanged — promotion still needs the full behavioural PASS, now gated on MECH-449 + the corrected 485l.
- **behavioral_diversity_isolation:GAP-I:** the discrimination conversion (485j) stands as the first downstream MECH-448 generalisation; the devaluation conversion is deferred to post-MECH-449.

**Draft `evidence_quality_note` for governance to write on the 485k manifest / SD-033b+MECH-263 (do NOT write here):**
> V3-EXQ-485k (2026-06-21, ree-cloud-2): supersedes 485j; FAIL/non_contributory/non_degenerate:false (no governance weight), self-route `substrate_not_ready_requeue` CONFIRMED + reclassified by failure_autopsy_V3-EXQ-485k_2026-06-21. Both DVs vacuous: readiness 1/3 (the aggregate `interpretation.preconditions met=True` panel reports max-over-seeds and masks a per-seed 2-of-3 collapse — only seed 0 cleared the devalued floor). FIX-1's re-ranking devalued driver works (bias vector inverts, cosine −0.71/−0.57 on 2/3) but overshoots the ±0.5 OFC bias clamp → uniform saturation → readable devalued range = exactly 0.0 on 2/3 seeds; and it REGRESSED the 485j C2 discrimination conversion (1.0/0.0/1.0 → 0/0/0) by swamping the shared OFC head. Diagnosis: demotion-alone (MECH-448 eligibility access) cannot express the active No-Go *withdrawal* that behavioural outcome-devaluation requires; the discrimination signature (sig-b) is demotion-tractable (converted 485j) but the devaluation signature (sig-a) is blocked on the MECH-449 Go/No-Go constitution (NOT built; substrate_conditional). The 485e→k lineage clears the ARC-107 "demotion-alone-insufficient" build gate (arc_107_selector_constitution_design §3.2 line 171/243). MECH-448 NOT weakened (envelope fired, excl 4–5, winner≠F on 2/3). MECH-263 sig-a / SD-033b devaluation: non_contributory / substrate_conditional / pending_retest_after_substrate (blocked on MECH-449). Corrected OFC devaluation arm (V3-EXQ-485l: in-band re-rank gain + C2 protection + bias-vector scored DV + `use_f_eligibility_adaptive_floor`) GATED behind the MECH-449 build + 689e. PROMOTES NOTHING.

---

## 8. Recommended substrate_queue write (governance applies)

**action: amend** `f_dominance_conversion_ceiling` — emit the 485k failure record and **flag the MECH-449 Go/No-Go build gate as CLEARED** (demotion-alone insufficient for the OFC active-withdrawal devaluation signature, demonstrated across the 485e→k lineage). The MECH-449 build is the `depends_on_unresolved[1]` (substrate_conditional) of this entry; this autopsy converts it from "double-gated, not chipped" to "gate cleared, ready to chip." Adopt `use_f_eligibility_adaptive_floor` on the OFC channel (pending 689e) as the standing fix for the per-channel envelope-floor circle. The corrected V3-EXQ-485l is the gated downstream behavioural validation, queued post-MECH-449.
