# Failure Autopsy -- V3-EXQ-700b: ARC-108 sec-7 learned-gating settling C3 (test-design-fixed re-run of 700/700a)

- **Generated (UTC):** 2026-06-24T19:33:36Z
- **Scope:** single (terminal run of the V3-EXQ-700 lineage; cluster context = 700 + 700a, autopsied 2026-06-23)
- **Status:** confirmed (user-adjudicated 2026-06-24)
- **Claims tagged:** MECH-439 (F-dominance conversion ceiling; candidate / substrate_ceiling), ARC-108 (dopamine-gated learned channel-gating; candidate / substrate_conditional), MECH-450 (recurrent settling step; candidate / substrate_conditional)
- **Outcome:** FAIL -- self-route `substrate_not_ready_requeue` -- evidence_direction `non_contributory` (all 3 claims)
- **Machine:** ree-cloud-4
- **Run:** `v3_exq_700b_arc108_sec7_learned_gating_settling_c3_20260624T192217Z_v3`

---

## 1. Facts -- reconstruction (no interpretation)

6 seeds x 5 arms, phased P0/P1/P2, reef-bipartite foraging (size 12, hazard_food_attraction 0.7). The landed arithmetic envelope (use_f_eligibility_demotion + adaptive_floor 689e + go_nogo_constitution 689g + modulatory-authority/top_k k=3 569i; use_differentiable_cem=False SD-055) is a **matched constant on all arms**. Swept variables: `use_learned_settling_step` x `use_learned_channel_gating` x `learned_channel_rpe_mode` (+ `use_noise_floor` on ARM_NOISE only). PRIMARY DV = committed-action-class entropy. 30/30 seeds completed.

The 5 arms: A0_ENVELOPE_ONLY / A2_SETTLING_SIGNED (W_lat, focus) / A3_BOTH_SIGNED (w_chan+W_lat) / C3_SETTLING_UNSIGNED (B5 ablation) / ARM_NOISE (matched-noise temperature control, NOISE_FLOOR_ALPHA re-tuned 1.0 -> 2.0).

### Acceptance criteria (from manifest `result.acceptance_criteria`)

| field | value |
|---|---|
| preconditions_met | **False** |
| n_divergent_seeds | 3 (threshold 3) -> enough_divergent_seeds True |
| **noise_verified_lifting** | **False** |
| **n_noise_lifts_over_a0** | **0** |
| C1_conversion | True |
| C1_a2_settling_signed_converts | True (n_seeds 2 / n_divergent 3) |
| C1_a3_both_signed_converts | True (n_seeds 2 / n_divergent 4) |
| C1_c3_settling_unsigned_converts | True (n_seeds 4 / n_divergent 4) |
| C2 (a2/a3 grow) | True (n_grow_seeds 2 each) |
| mean_committed_class_entropy_a0 | 0.915055 |
| mean_committed_class_entropy_a2_settling_signed | 0.951752 (+0.037) |
| mean_committed_class_entropy_a3_both_signed | 0.965783 (+0.051) |
| mean_committed_class_entropy_c3_settling_unsigned | 1.037873 (+0.123) |
| **mean_committed_class_entropy_noise** | **0.916066 (+0.001 over A0 -- inert)** |

**The single unmet precondition is `noise_verified_lifting` (0/3 lift).** The conversion criteria (C1/C2) nominally PASS on a majority of divergent seeds, but the run correctly self-routes to `substrate_not_ready_requeue` because those passes sit above an **unverified null** -- the "strict-above-noise" bar is meaningless when the noise control itself never rose above A0.

### Failed criterion type

`precondition_unmet` (readiness gate), NOT a discrimination/absolute criterion. This is a flagged self-route, adjudicated under the "self-route is a hypothesis" rule.

### Lineage noise-bar history (the load-bearing pattern)

| run | NOISE_FLOOR_ALPHA | noise lifts / divergent seeds |
|---|---|---|
| V3-EXQ-700 | 1.0 | 1/3 |
| V3-EXQ-700a | 1.0 | 0/3 |
| **V3-EXQ-700b** | **2.0** | **0/3** |

Doubling alpha made the null bar *worse*, not better.

---

## 2. Claim-layer mapping

The experiment did **not** test the claims under conditions where they could express themselves -- the conversion DV was gated behind a non-vacuity precondition (a verified null) that failed. No claim is weakened. `claim_ids` are correct: MECH-439 = the conversion ceiling under attack; ARC-108 (w_chan) + MECH-450 (W_lat) = the learned levers being tested as the lift. All three are `candidate`, `implementation_phase: v3`; MECH-439 `substrate_ceiling`, ARC-108/MECH-450 `substrate_conditional`. **PROMOTES NOTHING, WEAKENS NOTHING.**

---

## 3. Biological-reference triage

Unchanged from the 700-cluster autopsy and reconfirmed:

- **ARC-108** -- faithful translation of basal-ganglia three-factor dopaminergic plasticity (cortico-striatal eligibility x signed RPE, D1-LTP/D2-LTD). Not a formal import. Lit present (`targeted_review_connectome_mech_439`).
- **MECH-450** -- faithful translation of BG/pallidal recurrent winner-take-most settling (Mink surround inhibition). Not a formal import.
- **Missing-dependency signature:** biological BG action selection runs over multiple parallel cortico-BG-thalamic loops (loop segregation). A single foraging arena cannot exercise loop-segregated committed diversity. This run makes that latent constraint **concrete** (see Section 4, measurement layer).

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | conversion could not express -- the null was unverified, so the C1/C2 passes are not trustworthy |
| Biological reference | clear | faithful three-factor DA plasticity + recurrent settling; lit present |
| Prerequisites | present | ARC-108/MECH-450 built + engaged; w_chan + W_lat move; delta_t variance; settling moves the field |
| Implementation | complete-and-engaged | NOT symbol-only; the learning machinery runs and produces a strengthening lift |
| Environment | **binding constraint (single arena)** | reef-bipartite single arena cannot support a valid committed-class null; loop-segregated diversity is unreachable here |
| Measurement | **ROOT (dominant)** | the matched-noise null perturbs POLICY SOFTMAX TEMPERATURE (MECH-313 noise floor), but the DV (committed-class entropy) is fixed DOWNSTREAM by the F-bounded eligibility constitution (MECH-448/449 + top_k shortlist + go/nogo). Temperature and committed-class diversity are **DECOUPLED by the very commitment gate under test** -> the null is structurally inert (0/3 at alpha=2.0), and alpha is the WRONG KNOB. A 700c at alpha=3.0 is near-certain to fail identically. |
| Integration | coupled | learning composes inside the F-bounded eligible set |
| Scale | adequate | 6 seeds x 5 arms x phased; the gap is null DESIGN, not budget |

**Dominant diagnosis:** measurement / test-design ROOT -- the null is mis-layered (policy temperature vs committed-class DV), which on a single arena is structurally un-fixable by tuning. Recommended `epistemic_category`: NO CHANGE (MECH-439 stays substrate_ceiling; ARC-108/MECH-450 stay substrate_conditional). Recommended `evidence_direction`: `non_contributory` (matches the self-route), `pending_retest_after_substrate`.

---

## 5. Lineage pattern (700 / 700a / 700b)

One structural property across all three runs, **not** three bugs: the matched-noise null does not verify-lift on a single foraging arena, because it perturbs a layer (policy temperature) decoupled from the committed-class DV by the commitment gate. The settling SIGNAL, by contrast, **strengthens** across the lineage:

| run | settling lift | divergent-seed coverage |
|---|---|---|
| 700 | seed-42 only (+0.25 over A0, beat noise) | 1 clean seed |
| 700a | unscoreable (pool collapsed on majority) | -- |
| **700b** | a2 +0.037 / a3 +0.051 / c3u +0.123 over A0 | **majority of divergent seeds (C1 passed)** |

A strengthening signal blocked by one broken instrument is the **opposite** of the "circling the same ceiling" pattern -- but the instrument is un-fixable at V3 (the decoupling is a single-arena substrate limit).

---

## 6. Re-derive brake

Mechanically FIRES on all three claims:
- **MECH-439:** 4 prior `non_contributory`/`substrate_ceiling` autopsies (689, 689a, f-dominance-cluster, 700-cluster) -> this is the **5th**.
- **ARC-108:** 2 prior (460l, 700-cluster) -> **3rd**.
- **MECH-450:** 1 prior (700-cluster) -> **2nd**.

Threshold = 2 (default). The prior exemption (2026-06-23) was granted for *fresh substrate (new ARC-108/MECH-450 builds) + new mechanism + a test-design fix*. **That test-design fix is exactly what just failed.** Its renewal conditions are NOT met for a 4th attempt: no fresh substrate, same mechanism (settling). The prior autopsy explicitly pre-registered 700b as the last V3 letter.

**Brake disposition: `fired: true`.** It REFUSES the naive same-lever requeue (the manifest's "re-tune NOISE_FLOOR_ALPHA" self-route -- proven futile by the decoupling). It does **not** refuse the user-adjudicated concurrent disposition below, because the V4 escalation proceeds *regardless*, so the brake's anti-delay intent is fully honoured: the V3 redesign is a cheap parallel bet that can only ADD a validated result, never delay the V4 jump.

---

## 7. Learning extracted + routing (user-adjudicated 2026-06-24: CONCURRENT)

**Learning:**
1. The matched-noise null is mis-layered: policy temperature is decoupled from committed-class entropy by the commitment gate -> the null cannot verify-lift on a single arena at any alpha. Alpha is the wrong knob (3 runs confirm).
2. The learned SETTLING (MECH-450 W_lat) conversion signal is real and **strengthening** (700 seed-42-only -> 700b majority-of-divergent-seeds), blocked from scoring solely by the broken null.
3. A valid null for a committed-class DV must perturb at the **same layer the settling acts on** (the eligibility/settling field), not policy temperature.
4. The single foraging arena is the binding constraint for loop-segregated committed diversity (the V4 escalation argument).

**Routing -- BOTH, run concurrently (no work lost):**

**(A -- primary) `implement-substrate`: V4 loop-segregation substrate (escalate).** Honours the prior pre-registration and the now-tripped brake. The single arena cannot support a valid committed-class null (decoupling) or loop-segregated committed diversity -> validate learned-gating conversion on the V4 full BG-thalamo-cortical loop / loop-segregation substrate. `recommended_substrate_queue_entry.action = create` (substrate_queue.json currently empty; no V4 loop-seg entry exists).

**(B -- concurrent, brake-EXEMPT terminal) `/queue-experiment` 700c: null REDESIGN (NOT alpha).** Replace the policy-temperature null with a **same-layer null** -- magnitude-matched random structure injected into the eligibility/settling field (the layer settling acts on), gated cleanly behind `noise_on`. Pre-register as **terminal**: any further null failure auto-escalates to V4 with no more V3 letters. This is a genuine null-redesign (different mechanism), not another lettered iteration of the same lever, and it runs in parallel with (A).
- **Arm-reuse via substrate fingerprint -- YES, strong fit.** Only 1 of 5 arms (ARM_NOISE) changes between 700b and 700c; A0_ENVELOPE_ONLY + the three settling arms (A2/A3/C3) are byte-identical in config on a frozen ARC-108/MECH-450 OFF-path. Conditions: (1) the new null hook must be gated behind `noise_on` so the other arms' execution path stays byte-identical to 700b (no shared-code drift); (2) mint the unchanged arms (at minimum A0; ideally the settling pack) as a canonical baseline `ree-v3/experiments/_lib/baselines/exq700_arc108_settling_baseline.py` keyed on the substrate fingerprint with `include_driver_script_in_hash=False` (mandatory -- so the driver edits for the new null don't bust the reused arms' hash); (3) identical env (reef-bipartite size 12 hazard 0.7), seeds, P0/P1/P2 budget; (4) confirm no ree_core change to the OFF-path/settling path since 700b. Cloud linux-x86_64-py3.10 class (700b ran ree-cloud-4) -> qualifies. The /queue-experiment skill owns the actual minting + reuse wiring (its "Saving a baseline for reuse" block); this autopsy only recommends it.

**Demotion threshold NOT reached** (the claims were never fairly tested). MECH-439 stays substrate_ceiling; ARC-108/MECH-450 stay substrate_conditional; all `pending_retest_after_substrate`.

---

## 8. Draft `evidence_quality_note` (for governance to write -- do not write here)

> V3-EXQ-700b (terminal test-design-fixed re-run of the ARC-108 sec-7 learned-gating settling falsifier; supersedes V3-EXQ-700, folds 700a C3) FAIL / non_contributory (MECH-439, ARC-108, MECH-450). Self-route `substrate_not_ready_requeue`: the sole unmet precondition is `noise_verified_lifting` (0/3 at NOISE_FLOOR_ALPHA=2.0; 700 was 1/3 at 1.0). Autopsy 2026-06-24: the matched-noise null perturbs policy softmax temperature (MECH-313 noise floor), which is DECOUPLED from the committed-class-entropy DV by the F-bounded eligibility constitution under test -- alpha is the wrong knob and the null is structurally inert on a single arena. The learned-settling (MECH-450 W_lat) conversion signal is real and strengthening across the lineage (700 seed-42-only -> 700b majority-of-divergent-seeds), blocked from scoring solely by the broken null. Re-derive brake FIRES (MECH-439 5th / ARC-108 3rd / MECH-450 2nd non_contributory): naive alpha-bump requeue REFUSED. User-adjudicated routing 2026-06-24: CONCURRENT -- (A) escalate to V4 loop-segregation substrate (implement-substrate; substrate_queue create), and (B) one brake-exempt terminal V3 700c that REDESIGNS the null to a same-layer (eligibility/settling-field) perturbation, with arm-reuse via substrate fingerprint for the 4 unchanged arms. No promotion/demotion; pending_retest_after_substrate.
