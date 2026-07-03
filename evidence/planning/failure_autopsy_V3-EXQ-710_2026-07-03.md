# Failure Autopsy -- V3-EXQ-710 (MECH-140 x MECH-450 disinhibitory soft-competitive settling validation)

- **Generated (UTC):** 2026-07-03T13:56:58Z
- **Run:** `v3_exq_710_disinhibitory_soft_competitive_settling_validation_20260703T112039Z_v3`
- **Queue:** V3-EXQ-710 (experiment_purpose=evidence; claim_ids [MECH-140, MECH-450, MECH-439])
- **Scope:** single | **Status:** confirmed (interactive gate accepted 2026-07-03)
- **Substrate under test:** landed 2026-07-02 (ree-v3 main 8cc42bc) -- replaces the one-shot within-eligible committed argmin with a few rounds of parameter-free disinhibitory soft-competitive lateral-inhibition settling (`e3_selector._soft_competitive_settle`) over the F+MECH-448/449 within-eligible field before commit.

---

## 1. Facts (no interpretation)

**Outcome:** FAIL, `non_degenerate=True` -- a DECISIVE result at the DV, not a `substrate_not_ready_requeue`. All five readiness preconditions **met**:

| precondition | measured | threshold | met |
|---|---|---|---|
| enough divergent seeds | 3 | 3 | yes |
| settling field moved (INTACT) | scs_mean_round_delta 5-8 | 0.001 | yes |
| eligible set non-degenerate | frac_excluded 1.0 | 0.05 | yes |
| learning engaged | fcg range/delta > floor | -- | yes |
| candidate pool divergent | GAP-A spread | 0.05 | yes |

**Self-route (manifest):** `soft_competitive_settling_does_not_convert_ceiling_intrinsic_weakens_mech140_mech450`
-> per-claim MECH-140 **weakens** / MECH-450 **weakens** / MECH-439 **supports** (ceiling intrinsic).

**Which criterion failed:** the **discrimination** criterion C1 (A1_INTACT committed-class entropy strict-above A0_OFF + 0.05 margin on a strict-majority >=2/3 of divergent seeds) -- passed on **1/3** divergent seeds.

**Per-divergent-seed breakdown** (divergent-on-all-3-arms seeds = {42, 44, 46}; the only seeds where there was real candidate divergence to convert):

| seed | H_off | H_intact | H_ablated | Delta(intact-off) | C1 |
|---|---|---|---|---|---|
| 42 | 1.342 | 1.413 | 1.342 | **+0.071** | pass |
| 44 | 1.053 | 0.884 | 1.053 | **-0.169** | fail (settling REDUCED diversity) |
| 46 | 0.996 | 0.843 | 0.996 | **-0.153** | fail (settling REDUCED diversity) |
| **mean** | **1.130** | **1.047** | **1.130** | **-0.083** | **1/3** |

Two internal-validity facts that fix the reading:

1. **The headline all-6-seed mean is misleading.** The manifest reports `mean_committed_class_entropy_intact=0.937 > off=0.916` (+0.021), computed over ALL six seeds. That apparent lift comes entirely from the three NON-divergent seeds (43/45/47), where the settling raised entropy off a collapsed proposer -- meaningless, because there was nothing to convert. On the three DIVERGENT seeds that matter, INTACT (1.047) is **below** OFF (1.130).
2. **A2_ABLATED (uniform rank-preserving kernel) reproduces A0_OFF bit-identically** (1.130438 == 1.130438 over divergent seeds; identical per-seed counts). So the settling machinery with a flat kernel is a clean no-op landing exactly on the one-shot argmin baseline -- the **structured class-surround kernel is the sole active ingredient**, and over the F-collapsed field it **sharpened** toward the F-winner rather than diversifying.

Task performance unchanged (mean_reward_p2 over divergent seeds: OFF -0.976, INTACT -0.990).

---

## 2. Claim-layer mapping

| claim | status | phase | flags | depends_on |
|---|---|---|---|---|
| MECH-140 (soft-competitive disinhibition) | candidate | -- | first lit grounding 0.60 (Keller2020/Aquino2026); **0 prior autopsies** | MECH-062, ARC-005, Q-016 |
| MECH-450 (minimal recurrent settling step) | candidate | v3 | `substrate_conditional`, `pending_retest_after_substrate`; note already says "does NOT weaken MECH-450" | ARC-107, MECH-439, MECH-448, ARC-108, MECH-449 |
| MECH-439 (F-dominance conversion ceiling) | candidate | v3 | `substrate_ceiling`, `pending_retest_after_substrate` | ARC-065, MECH-309, ARC-062, MECH-294 |

**Did the experiment let the claims express?** No. Loop segregation OFF + learned settling OFF + learned cross-loop arbitration OFF on all arms (by design), so the settling ran over the **single shared selector's** within-eligible field, which F's raw-magnitude monopoly has already collapsed. The between-loop context-reconfiguration function MECH-140/MECH-450 encode had no differentiated field to act on.

---

## 3. Biological-reference triage (the core move)

- **Closest mechanism:** cortical / cortico-striatal **disinhibition** -- VIP-expressing interneurons inhibit SOM interneurons (inhibition-on-inhibition). In mouse V1 the VIP->SOM circuit is **necessary and sufficient** for contextual modulation (Keller et al., Neuron 2020, optogenetic), firing precisely **when center and surround differ**. In biologically-constrained switching RNNs + causal mouse V1 silencing (Rungratsameetaweemana/Aquino, PLOS Biology 2026), weakening the inhibition-to-inhibition motif **specifically collapses task-switching** while other connection types leave processing intact.
- **Functional role:** the disinhibitory channel is a **top-down context signal that reconfigures competition BETWEEN differentiated modules/loops** -- it requires a differentiated context to switch between, and operates by modulating **recurrent** excitation.
- **Faithful translation or impoverished import?** The V3 mechanism is a **faithful translation of the PRIMITIVE** (graded, learned-capable, recurrent-settling class-surround lateral inhibition) but deployed at an **impoverished LOCUS**: the single F-collapsed within-eligible field, not across segregated loops carrying differentiated value. It has the **symbol** of the mechanism, not its **functional role**.
- **Does the failure match a missing-dependency signature?** Yes, decisively. Graded lateral inhibition over a field one score already monopolizes will mathematically **sharpen that score** -- which is exactly the **-0.169 / -0.153 nat diversity REDUCTION** on divergent seeds 44/46. This is the wrong-locus / missing-dependency signature (segregated loops with differentiated value), **not** a falsification of the disinhibition primitive.
- **Lit status:** present (MECH-140 first grounding pulled 2026-07-02; sibling arc_108/mech_450 entries).

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **not-fairly-tested** | between-loop function could not express on the single F-collapsed selector |
| Biological reference | **clear** | disinhibition well-grounded, faithful primitive, wrong locus |
| Prerequisites | **missing** | segregated loops with differentiated value (ARC-110 / v4_loop_segregation) absent; loop-seg OFF |
| Implementation | **partial (symbol, not role)** | settling built + live (round_delta 5-8); A2 uniform kernel == OFF bit-identically; sharpens F over collapsed field |
| Environment | **wrong pressures** | single F-dominated arena; F ~88-89% of E3 selection variance swamps non-motor signal (700d-708) |
| Measurement | **adequate (win)** | non-vacuity gates + A2 rank-preserving control force the substrate (not falsification) reading |
| Integration | **isolated** | settling runs alone (W_lat / cross-loop / loop-seg OFF) -- clean isolation, but denies it the differentiated field |
| Scale | **n/a** | mechanism engaged fully; not a capacity limit |

**Recommended `epistemic_category`: `substrate_ceiling`** -- the same single-arena F-dominance ceiling, third distinct mechanism.

---

## 5. Convergent-pattern context (why this is a substrate property)

This is the SAME single-arena F-dominance conversion ceiling already diagnosed for the 700-lineage, 707b, and 709 -- now expressed through a **third structurally-different mechanism**:

| lineage | conversion mechanism tried | result |
|---|---|---|
| 700 / 700b / 700c / 700d-708 | exploration injection + learned gating/settling + same-layer null | non_contributory / substrate_ceiling |
| 709 | learned/DA-gated cross-loop arbitration | non_contributory / substrate_ceiling (limbic can't reach motor effective weight) |
| **710** | **parameter-free disinhibitory soft-competitive settling** | **non_contributory / substrate_ceiling (sharpens F over collapsed field)** |

700d-708 structural property (verbatim): *"the V3 single F-dominated E3 arena ... dissolves any pre-commit ... injection at the argmax, because F's raw-magnitude monopoly (88-89% of E3 selection variance, MECH-439) swamps every non-motor signal at the single shared selector."* Convergent failure of three structurally-different conversion mechanisms on one substrate is strong evidence the ceiling is a **substrate property (the single shared F-dominated selector)**, not a per-mechanism weakness. **v4_loop_segregation is the load-bearing build.**

---

## 6. Adjudication (self-route REJECTED; user-confirmed 2026-07-03)

| claim | manifest self-route | **autopsy recommendation** | rationale |
|---|---|---|---|
| MECH-140 | weakens | **non_contributory** (substrate-limited) | wrong-locus; sharpened not diversified on divergent seeds; strong first lit grounding 0.60 -> strong-lit/substrate-blocked, NOT under-supported; 1st autopsy |
| MECH-450 | weakens | **non_contributory** (substrate-limited) | consistent with standing note "does NOT weaken MECH-450 -- the substrate-conditional minimal-settling step"; brake fires (5th) |
| MECH-439 | supports (intrinsic) | **non_contributory + narrow corroboration** (`narrow_supports_flag=true`) | single-arena cannot decide intrinsic-vs-liftable (only segregated loops can); corroborates the already-mapped single-arena ceiling (single-pathway), NOT fresh support for global intrinsicness; brake fires (9th) |

**All three:** stay candidate / `pending_retest_after_substrate` / **PROMOTES NOTHING**.

### Illusory-conflict check (mandatory)
MECH-140 and MECH-450 carry `hold_candidate_resolve_conflict` (conflict resolution before promotion). Because the recommendation is **non_contributory (NOT weakens)**, this FAIL **neither resolves nor deepens** that hold -- conflict resolution still awaits the segregated-loop retest. Governance must **not** read 710 as bearing on the hold. The remaining "supports" for MECH-439's ceiling are narrow / single-pathway (single shared selector), flagged accordingly.

### Lit/exp decoupling
MECH-140 lit_conf 0.60 (first grounding, strong), exp = substrate-blocked non_contributory. Reported separately -- a strong-lit / substrate-blocked datum, not "under-supported".

---

## 7. Re-derive brake (MOVE-3) -- FIRES

Prior `substrate_ceiling` / `non_contributory` autopsies tagging each claim (+ this one):

- **MECH-439:** 8 prior -> **9th. FIRES.** (689, 689a, 700-cluster, 700b, 700c, 700d-708, 709, f-dominance-cluster)
- **MECH-450:** 4 prior -> **5th. FIRES.** (700-cluster, 700b, 700c, 700d-708)
- **MECH-140:** 0 prior -> 1st (does not fire yet; one more single-arena letter would).

**Consequence:** routing MUST be `implement-substrate` on **v4_loop_segregation**. A same-claim single-arena test re-queue is **REFUSED** -- another letter circling the single-selector ceiling is exactly the loop the brake exists to stop. A redesign that tests the settling on segregated loops (different substrate / new EXQ) is allowed.

---

## 8. Repair pathway / routing

**Routing: `implement-substrate` -> AMEND `v4_loop_segregation`.**

- Append the 710 failure_record (settling live in single-arena but sharpens F over the collapsed field -> 7 records total).
- Add **MECH-140** to `unblocks_claims` (it was absent; MECH-140's disinhibition also needs the segregated-loop locus).
- `implementation_hint`: the settling step is BUILT (8cc42bc) and LIVE, but must run over MULTIPLE parallel loops carrying DIFFERENTIATED value (motor / associative / limbic), each with its own eligibility+Go/No-Go+settling arbitrated AFTER within-loop competition, PLUS a valid in-layer settling-field committed-class null -- the two conditions the single arena structurally denies. Retest via the segregated-loop redesign (new EXQ / different substrate), NOT another single-arena letter.

The exact `recommended_evidence_quality_note` text for governance to write is in the JSON artifact (`recommended_evidence_quality_note`). This skill does not write it.

---

## 9. Learning extracted

1. The soft-competitive settling primitive is BUILT and LIVE (round_delta 5-8; A2 uniform-kernel control == A0_OFF bit-identically), so this is a clean isolation -- and the isolation itself proves the mechanism cannot express its BETWEEN-loop function on the single F-collapsed selector: graded lateral inhibition over an F-dominated field SHARPENS F (diversity -0.15 to -0.17 nats on 2/3 divergent seeds), it does not convert.
2. "Field moved" + "eligible-set non-degenerate" are necessary mechanism-LIVENESS gates but NOT sufficient to establish a fair FUNCTIONAL test -- exactly analogous to 709's deeper `limbic_loop_can_win` gate. The deeper unmet precondition is "differentiated value across segregated loops for the disinhibition to reconfigure", which single-arena denies. Do not read a future single-arena settling successor as decisive however non-vacuous the field movement.
3. Headline all-seed means can invert the per-divergent-seed decision statistic; always read the conversion DV on divergent seeds only.
4. Three structurally-different conversion mechanisms (exploration/same-layer-null, learned cross-loop arbitration, disinhibitory settling) now fail on one substrate -> the ceiling is a substrate property, not a per-mechanism weakness. v4_loop_segregation is the load-bearing build.
5. MECH-140's first autopsy: strong first lit grounding (0.60) makes this strong-lit/substrate-blocked (novel-discovery-adjacent), NOT under-supported. One more single-arena letter trips its brake.

---

## 10. Governance hand-off (applied in the /governance re-run, NOT here)

1. Apply `recommended_evidence_quality_note` to MECH-140 / MECH-450 / MECH-439 (all non_contributory; PROMOTES NOTHING; all stay candidate + `pending_retest_after_substrate`). Set/keep `epistemic_category`: MECH-140 `substrate_ceiling`, MECH-450 `substrate_conditional`, MECH-439 `substrate_ceiling`. Set MECH-140 `pending_retest_after_substrate=true`.
2. AMEND `v4_loop_segregation` in `substrate_queue.json`: append the 710 `failure_record` (-> 7); add MECH-140 to `unblocks_claims`.
3. Mark V3-EXQ-710 reviewed in `review_tracker.json`; rebuild indexes; confirm pending_review decrements.
4. Do NOT touch the MECH-140/MECH-450 `hold_candidate_resolve_conflict` state -- this FAIL is non_contributory and does not bear on the conflict hold.
