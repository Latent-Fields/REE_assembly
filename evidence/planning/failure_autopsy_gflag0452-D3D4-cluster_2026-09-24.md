# Failure Autopsy (STAGING): GFLAG-0452 D3/D4 cluster -- V3-EXQ-158 / 763 / 917 / 149b / 743

**Status: `awaiting_human_confirmation`** (staging mode). Written by the subagent
`governance-20260924-autopsy-d34` for the `/governance` session `governance-20260924`. The parent
session holds the Step 8 gate. Nothing here has been applied: claims.yaml, the manifests,
review_tracker, substrate_queue, governance flags and the hypothesis registry are all untouched.

- **CONFIRMED 2026-09-24T10:18:00Z** by the user at the /governance gate (session governance-20260924); decisions G1 A rec-20260924-aa33086a, G2 A rec-20260924-a796e485, G3 B rec-20260924-d7d2fb40, G4 A rec-20260924-823fac58, G5 A rec-20260924-17c7e199 (as they apply here). G4 A: Q-004 -> substrate_conditional + registration-only R(x,t) substrate_queue entry. G5 A: 763/743 supports (narrow) kept; 917 -> non_contributory; Q-018 routed to the registered instrument; 746a re-tagged INV-090.

- Generated: 2026-09-24T09:16:44Z (draft); red-team pass completed 2026-09-24T09:28Z.
- Trigger: GFLAG-0452, user decision rec-20260924-34e4e088. Five PASS manifests that the governance
  driver skim (`evidence/planning/gflag0250_pass_driver_skim_20260924.{md,json}`) marked as defects
  of class D3 (a leg passes by construction) or D4 (the direction was misread).
- Machine-readable twin: `failure_autopsy_gflag0452-D3D4-cluster_2026-09-24.json`. Its
  `per_claim_recommendation` blocks are what governance applies.

## 0. Summary for the gate

| Run | Claim (status) | Skim said | This autopsy | Recommended direction | Claim status |
|---|---|---|---|---|---|
| V3-EXQ-158 | Q-018 (active) | D3: harm 0.0 everywhere; gate never reaches action | **Confirmed and extended.** harm_rate is a phantom-key 0.0: the driver reads a dict key the environment never emits | supports -> **non_contributory** | stays active |
| V3-EXQ-763 | MECH-304 (active) | D3: two of three legs pass by construction; cue leg genuine | **Confirmed, with one precision fix.** A completion-release path was live in arm B but could not fire | **supports, narrow** (`narrow_supports_flag`) | stays active (alternative: provisional) |
| V3-EXQ-917 | SD-011 (stable), diagnostic | D4: an OR over a failed production path mapped to supports | **Confirmed in conclusion; overturns the confirmed 2026-08-12 SD-011 disposition.** The encoder was untrained, and the run never compares z_harm_s with z_harm_a | supports -> **non_contributory** (zero index weight either way) | stays stable |
| V3-EXQ-149b | Q-004 (active) | D4: the winning SLOW arm's residue channel is inert | **Confirmed and extended (construct mismatch).** tau_R is the time constant of the astrocytic field R(x,t), which does not exist in ree_core. The run varied a residue deposit gain, which has no time constant | supports -> **non_contributory**; category **substrate_conditional** | stays active |
| V3-EXQ-743 | INV-089 (provisional) | D4: the claim's own DV was made non-gating and ran the wrong way | **Partly overturned.** The C1 floor was inherited from 740a, not tuned after the spot-check. The gate change was a disclosed user decision. The demoted DV now belongs to INV-090. The premise-only reading stands but was already adjudicated twice | **supports, narrow** (no direction change) | stays provisional (alternative: candidate, but only if MECH-304 goes too) |

**Skim findings overturned:**
- **743, C1 floor.** The skim said the floor was "set just under the spot-check". In fact
  `HARM_DECODABLE_FLOOR = 0.05` is inherited verbatim from V3-EXQ-740a (740a driver :208, 743
  driver :203).
- **743, the demoted DV.** The skim framed it as the claim's own DV. Since the 2026-07-16 split it
  belongs to INV-090, not INV-089.
- **743, flip risk.** The skim rated it high. Once the red-team pass was done, this autopsy
  recommends no direction flip.

**Skim findings extended:**
- **158.** The phantom `harm_signal` key.
- **149b.** The construct mismatch with the R(x,t) time constant.
- **917.** The encoder was untrained, and the run never compares z_harm_s with z_harm_a.

## 1. Scope, dry-run gate, prior coverage

- `check_dry_run_citations.py` over all five run_ids: 0 dry, 5 clean. `dry_run_checked: true`, `excluded_dry_run_ids: []`.
- `check_autopsy_coverage.py`: 158, 763, 149b and 743 had no prior autopsy. 917 is covered by the
  confirmed `failure_autopsy_V3-EXQ-916-916a-917-920-fishtank-cluster_2026-08-12`, so it is treated
  here as a **re-adjudication**. The prior artifact's 917 section, cluster read, learning and Step 9b
  record were read in full. Only its SD-011 disposition is superseded. Its `SD-MECH303-THRESHOLD-SOURCING`
  create, now `implemented_validated`, stands.
- Every finding below was re-measured from the driver, the manifest and the run-time substrate.
  None was taken from the skim alone.
- Claim: only this artifact pair was claimed (`governance-20260924-autopsy-d34`). The parent session
  holds the coordination-plane pause and the governance collision set.

## 2. Per target

### 2.1 V3-EXQ-158 -- Q-018 ("What RC-conflict threshold calibration blocks authority spoofing without chronic over-suppression?")

**Facts.**
- Three conditions (LOW 0.05, HIGH 0.40, ADAPTIVE EMA+2 sigma), 2 seeds, 400 episodes, spoofing
  injected on 10% of measurement steps. The spoofing is a Gaussian vector that replaces `world_state`.
- The manifest is PASS/supports with C1-C5 all true.
- `harm_rate` is **0.0 in all 6 cells**.
- Discrimination gaps: LOW 0.84/0.84, HIGH 0.66/0.73, ADAPTIVE 0.48/0.53.
- Clean suppression: LOW 0.087, HIGH 0.038-0.047, ADAPTIVE 0.009-0.013.
- `rc_conflict_mean` is identical across the three conditions within each seed.
- The manifest lacks the recording core: no substrate_hash, recording_schema, machine,
  elapsed_seconds or experiment_purpose.

**Verification.**
- **Gate with no consumer.** `gate_fired` (:427) only increments counters. The action is
  `torch.multinomial(policy probs)` (:444). So one trajectory runs per seed, and the three
  thresholds are applied to it afterwards.
- **Phantom key (new).** The driver reads `obs_dict_next.get("harm_signal", 0.0)` (:452). At the
  run-time environment commit (ree-v3 `8acc947`), `CausalGridWorldV2.step` returns `harm_signal`
  as tuple element 2, and `_get_observation_dict` never emits that key. The red-team checked the
  history: the key never existed at any commit. So harm_rate is 0.0 by construction, and the harm
  evaluator trained on a constant-0 target. C3 ("ADAPTIVE harm <= HIGH + 0.02") therefore reads
  0 <= 0.02 whatever the agent did. Even with the key fixed, `harm_signal` is signed (harm is
  negative, benefit positive, and waypoint rewards are added in), so a mean of it would compare
  the wrong sign.
- **The ADAPTIVE result.** ADAPTIVE is a stricter operating point, not a better calibration. It
  sits below HIGH on both spoof suppression and clean suppression. C2 follows from it being more
  conservative. Its EMA also absorbs the spoof spikes it is meant to detect, because it updates on
  every step (:405-409).
- **No substrate.** MECH-065 has no ree_core substrate (grep for rc_conflict or reality_coherence:
  0 hits). The RC signal here is a residual from a predictor defined inside the driver.

**Claim layer.** Q-018 is an open question that depends on MECH-065, MECH-062 and ARC-005. The run
lets neither half of it express itself. "Blocks spoofing" is a counted flag that blocks nothing.
"Without chronic over-suppression" has no cost channel, and its harm DV is pinned at 0. The current
evidence_quality_note says the run "confirmed ... suppression applies without chronic
over-suppression". The run does not show that.

**Biological reference.** The closest mechanism is source/reality monitoring: prefrontal source
monitoring, with conflict signalling in the dACC raising response thresholds. In biology the
discrimination is by provenance at matched content, not by the size of the surprise. The driver
treats "spoof" as "large prediction error on noise". Literature status: partial.

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | untested | neither half instantiated behaviourally |
| Biological reference | partial | provenance-at-matched-content vs pure surprise |
| Prerequisites | missing | no MECH-065 substrate; the needed instrument is registered as `q018-provenance-authority-marking-instrument` (registration only) |
| Implementation | partial | **inert by DEFECT**, missing link **no consumer**: the call site that should read `gate_fired` is the action/commit step (:444) |
| Environment | wrong pressures | synthetic noise spoofing; suppression has no behavioural cost |
| Measurement | misleading | harm_rate is a phantom 0.0; discrimination figures are post-hoc counts on one shared trajectory |
| Integration | coupled but inert | no consumer |
| Scale | adequate for the classifier statistics, not for a behavioural claim | 2 seeds |

**Failure location:** MIXED (MEASURES + MECHANISM-integration + ENVIRONMENT). Not chargeable to REE.

**Recommendation.**
- Direction: **non_contributory**. Category: **standard** (a measurement/test-design defect).
  pending_retest_after_substrate: **true**.
- Routing: amend the registration-only `q018-provenance-authority-marking-instrument` entry with a
  failure record. That amendment also corrects the entry's premise that 158 "already ran" a valid
  driver-local calibration.
- **No same-design 158a re-queue.** A corrected driver-local run still cannot generalise past
  synthetic noise, and it would also need a new harm DV.
- Re-derive brake: 1 counted hit for Q-018 (this one), below the threshold of 2. Not fired.

Draft `evidence_quality_note`: see JSON `targets[0].recommended_evidence_quality_note`. It also asks
governance to:
- retract the what_would_answer phrase that 158 "answers the threshold-calibration leg";
- re-derive `live_status.evidence`.

### 2.2 V3-EXQ-763 -- MECH-304 (cue-specific conditioned safety prediction; promoted provisional->active on this run)

**Facts.**
- Release rates: A (store on, cue) 0.833; B (store off) 0.0; C (store on, no cue) 0.161;
  D (MECH-303 contextual) 1.0.
- Per seed A-C: 1, 1, 0, 1, 0.033, 1.
  - Seed 2 formed no prototype.
  - In seed 4, C released 0.967 because its no-cue signal (0.655) cleared STORE_THRESHOLD 0.6.
- Under threat, the cue-present safety signal exceeded the cue-absent one in 5/5 formed-prototype
  seeds.
- Arm D's contextual prediction is 12.770-12.772 in every seed, against a release threshold of 0.5.
- The positive control (cue, no threat) released 1, 0, 0, 1, 1, 1 across seeds.

**Verification.**
- **DV2 (rel_D) is fixed by construction.** `CONTEXTUAL_HARM_THRESHOLD 0.55` (:131) was placed
  deliberately above the damage-sourced z_harm_a range (0.34-0.55): the driver comment reads
  "-> safe ticks accumulate". So every teaching tick accumulates, and DV2 cannot fail. This
  coincides with the V3-EXQ-917 C1 fact.
- **The store-necessity gap.** rel_B is 0.0 in 6/6 seeds. The harness turns the urgency interrupt
  off, resets the MECH-302 comparator, sets no goal, and B has the terrain off.
  - *Red-team precision:* the bistable beta gate keeps a hippocampal completion-release path
    nominally live (agent.py `ee0b0ba`:4702-4704). With no goal it cannot reach 0.75, and it fired
    0/180 times.
  - The gap therefore reduces to the absolute rel_A. That value is itself informative: 5/5
    formed-prototype seeds released 1.0 under concurrent threat.
- **Cue-specificity is the genuine, variable leg.** It varies across seeds and failed in one of
  them.
  - STORE_THRESHOLD 0.6 was chosen from observed cue and no-cue signal ranges. Two seeds sit within
    0.06 of it, so the behavioural margin is partly tuned.
- **The signal is also threat-modulated.** Seed 1: 0.704 under threat vs 0.471 without. The
  centered prototype carries some damage/threat context from the relief window. Cue-specificity
  still holds because arms A and C share that context.

**Biological reference.** Conditioned inhibition of fear. The expression pathway is IL -> CeA; the
conditioned inhibitor is encoded in the dorsal striatum and dlPFC (Laing 2022; Ng & Sangha 2023).
The reference is clear, and the cue leg has no load-bearing divergence from it.

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact, narrowly supported | core cue-specific release expressed; MECH-303 dissociation untested |
| Biological reference | clear | |
| Prerequisites | present | SD-065, SD-066, MECH-302 |
| Implementation | complete | store -> beta_gate release live |
| Environment | adequate | harness-induced commitment is **inert by design** (the GAP-I competence wall is bypassed on purpose) |
| Measurement | partial | DV2 and the store-necessity gap cannot vary; cue leg adequate but its threshold was tuned |
| Integration | coupled (MECH-304); arm D coupled but inert | neutralising guard: accumulation threshold above the input range |
| Scale | thin | 6 seeds, 5 valid, one leg |

**Failure location:** MIXED (MEASURES partial). One genuine leg supports the claim; two legs are
vacuous. This is a PASS, so there is no REE failure.

**Recommendation.**
- Direction **supports**, with **narrow_supports_flag: true**. Category **standard**. The claim
  currently has no category.
- **Status: stays active** (recommended). The surviving leg is the claim's core mechanism, and
  V3-EXQ-759 supplies representation-level support.
- **Alternative for the user: active -> provisional.** The pre-registered promote gate was
  "DV1 AND DV2", and DV2 was vacuous. Whichever rule is chosen must also be applied to 743 (§2.5).
- Routing: **queue-experiment**, a new EXQ number (not a 763 letter). The design:
  - a MECH-303 arm on the built `SD-MECH303-THRESHOLD-SOURCING` proximity signal, with its
    threshold inside the discriminating band;
  - a store-OFF arm that keeps an alternative release path **reachable**, so that necessity becomes
    a comparison rather than a structural zero;
  - STORE_THRESHOLD fixed on held-out seeds.
- No substrate is owed.

### 2.3 V3-EXQ-917 -- SD-011 (re-adjudication of the 2026-08-12 confirmed disposition)

**Facts.**
- `experiment_purpose: diagnostic`: a MECH-303 threshold-calibration battery.
- **This run carries zero weight in the SD-011 index.** `claim_evidence.v1.json` marks it
  `scoring_excluded: diagnostic_probe`. This correction moves no confidence number.
- **C1 (damage-sourced, the production default) FAILED.**
  - Density means are 0.44196 / 0.44181 / 0.44188 / 0.44197 / 0.44181 for 0/1/2/4/8 hazards, with
    a spread std of 7e-5.
  - Seed 0 reads 0.546 -> 0.543 across all densities, so the value is set by the seed.
- **C2 (legacy proximity-EMA) PASSED.** Means rise 0.46 -> 0.78, and at tau 0.6 the AUC is 0.969
  with reachability 0.848.
- The combination rule is "PASS iff C1 OR C2 -> supports".

**Verification.**
- **The rule was pre-registered.** The OR rule was pre-registered and argued in the driver, so the
  misread is in the inference, not hidden in the code.
- **The encoder was untrained.** The driver has no optimizer and no backward pass. It builds a fresh
  `REEAgent` per cell and random-walks it. So the AffectiveHarmEncoder is an **untrained random
  projection** in both modes.
  - This fact was surfaced by the Step 7b C2 fire on `sd_zharm_a_warmup_optimizer_group`.
  - The red-team notes it is already recorded in MECH-303's 2026-08-16 V3-EXQ-930 note. It had not
    been applied to the SD-011 disposition.
- **What C2 actually shows.** Damage input is 7-dim limb damage with heal_rate 0.4, near zero on
  most ticks. Proximity input is a 50-dim field EMA that varies with density. So C2 shows that a
  random projection of an input that varies with density also varies with density.
- **The raw-norm mean is seed-determined.** The 930 note records within-seed std rising with
  density, so an absolute threshold on the raw norm cannot discriminate, while a per-seed
  standardised read is untested.
- **No stream comparison.** Both modes feed the same z_harm_a stream (the encoder class instantiated
  at 7-dim and 50-dim). The run compares **two inputs to one stream**. It never reads z_harm_s
  against z_harm_a, and that separation is what SD-011 asserts.
- **Why the 2026-08-12 reasoning does not hold.** That autopsy argued that damage-sourced z_harm_a
  "tracks accumulated homeostatic deviation (its SD-011 job)". A seed-determined, untrained output
  is not shown to track anything.
- **Precedent.** `failure_autopsy_V3-EXQ-472_2026-09-02` recorded an unscored SD-011 calibration
  pilot as non_contributory.
- **Consistency with 743 and 759.** Those runs are positive controls for a *claim-specific* premise
  and are read as narrow supports. 917's C2 establishes a generic property of a random projection,
  which is no premise of the split.

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a for SD-011 | the split is neither manipulated nor measured |
| Biological reference | clear (MECH-303 sourcing); not engaged for SD-011 | the prior reactive-vs-anticipatory reading stays with MECH-303 |
| Prerequisites | present | |
| Implementation | complete (battery) | production MECH-303 consumer since fixed (SD-MECH303-THRESHOLD-SOURCING) |
| Environment | adequate | |
| Measurement | adequate for MECH-303 calibration; misleading as SD-011 evidence | test_design: the SD-011 bearing is non-discriminating in both branches |
| Integration | damage-sourced z_harm_a coupled but inert in this regime | untrained encoder, near-constant input |
| Scale | adequate | 100 arms |

**Failure location:** MEASURES (the mapping to the claim). Not an REE failure.

**Recommendation.**
- Direction **non_contributory** for SD-011. Category standard (unchanged).
  `diagnostic_evidence_adjudicated: true`.
- Status: stays stable.
- Replace the SD-011 claims.yaml paragraph dated 2026-08-12 ("...SUPPORTS SD-011...").
- Routing: governance-reclassify. This is a record correction only.

*Withdrawn argument:* "C1 FAIL should weaken SD-011". An inert-in-regime observation about the
SD-022 input is not a test of stream separation.

*Bears on:*
- Moves: the SD-011 note paragraph and the 917 manifest direction.
- Does NOT move: SD-MECH303-THRESHOLD-SOURCING, MECH-303's note, or the 916/916a/920 targets.

### 2.4 V3-EXQ-149b -- Q-004 ("How to calibrate tau_R relative to E1/E2?")

**Facts.**
- mean_harm: FAST 1.62/31.01, DEFAULT 0.82/21.24, SLOW 0.78/18.49.
- residue_contrast: FAST 0.22/2.57, DEFAULT 0.0/0.24, SLOW 0.0/0.0095.
- total residue: FAST 412/1671, SLOW 14.7/62.7.
- All 32 ring centres are active in every cell.
- Criteria: C2 (slow wins), C3, C4 and C5 true; C1 false.
- Substrate commit `2edeb8ce`.

**Verification.**
- **The skim's points hold.** The PASS comes through C2. C4 checks only FAST's contrast (:660). The
  SLOW field is effectively empty.
- **Construct mismatch (new).**
  - *What tau_R is.* tau_R is the decay constant of the astrocytic regulatory field R(x,t), defined
    by dR/dt = -R/tau_R + f_mono + f_local + f_meta + diffusion. Sources:
    `docs/processed/legacy_tree/.../regulatory_stack_model.md:90-95` (the source linked from
    `astrocyte_regulatory_stack.md#q-004`) and `implementation_hooks.md` `RegulatoryField(tau_R=10.0)`.
    Q-004 depends on MECH-001.
  - *It does not exist in ree_core.* MECH-001's own what_would_answer records no RegulatoryField in
    ree_core (grep for astrocyte: 0 hits).
  - *The stand-in was declared, not inherited silently.* EXQ-149 declared the residue field a
    stand-in for R(x,t) (149 driver :11-13). 149b kept that mapping unchanged. The 2026-09-21
    falsifier audit then adopted it into Q-004's what_would_answer.
  - *The stand-in has no time constant.* `ResidueConfig.accumulation_rate` is a per-deposit gain
    (`magnitude = |harm| * accumulation_rate`). ResidueField has no per-tick decay: the only decay
    is SD-034 `discharge_domain`, which is not on this path. So none of the three arms has a time
    constant at all.
- **The field is near-flat in every arm (new).** FAST's residue at harm vs elsewhere differs by
  0.05-0.16% of the field level. This is the residue-field-geometry ceiling: a 32-slot ring and an
  over-wide kernel. Eval harm tracks the overall field magnitude (FAST > DEFAULT > SLOW), so "less
  residue -> less harm" was read as a timescale preference.
- **The seed dominates the condition.** Harm spreads 19-26x between the two seeds.

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | untested | manipulated object is residue gain x bandwidth, not tau_R |
| Biological reference | partial | astrocytic Ca2+/gliotransmitter integration of monoaminergic tone vs a non-erasable harm residue |
| Prerequisites | missing | no R(x,t) (MECH-001 candidate, substrate_conditional) |
| Implementation | absent for tau_R | the residue channel is near-uniform in all arms and empty in the winning arm |
| Environment | adequate | |
| Measurement | misleading | DV tracks field magnitude; C4 validates only the losing arm |
| Integration | coupled but inert | residue-field-geometry ceiling |
| Scale | inadequate | 2 seeds, 19-26x seed spread |

**Failure location:** MIXED (MECHANISM absent for the claim's object + MEASURES). Not chargeable to REE.

**Recommendation.**
- Direction **non_contributory**. Category **substrate_conditional**. This is a deliberate assertion:
  Q-004's object does not exist in the substrate. pending_retest_after_substrate: **true**.
- Correct the what_would_answer CONFIRMING/DISPOSITION text that records 149b as a realised PASS.
- Routing: governance-reclassify, plus a **registration-only** `create`
  (`mech001-astrocytic-regulatory-field-registration`, priority 3). Building an R(x,t) module is a
  MECH-001 design decision, not authorised by this entry.
- **No 149c re-queue.** Another residue-parameter sweep cannot instantiate tau_R.
- Re-derive brake: 1 counted hit (this one). Not fired.
- **Cost of the recommendation.** substrate_conditional takes Q-004 out of every v3-testable lane,
  and it reverses the 2026-09-21/22 audit's R0 disposition.
  **Alternative for the user:** register a separate question (residue gain/bandwidth vs E1/E2
  horizon) if a v3 lane is wanted. 149b does not answer that question either.

*Withdrawn argument:* "route Q-004 to the residue-geometry entries (ring capacity / kernel
resolution)". Those entries explain why the field is flat, but a geometrically sound residue field
still has no tau_R.

### 2.5 V3-EXQ-743 -- INV-089 (harm-evaluator quality bounded by z_harm differentiation; provisional)

**Facts.**
- PASS = C1 (mature decode r2 >= 0.05) AND C2 (mean IV delta > 0 AND mean decode rho > 0; no noise
  floor, :625).
- Per seed:
  - mature decode: 0.083 / 0.169 / 0.121;
  - IV delta: +0.018 / -0.014 / +0.027;
  - decode rho: 0.6 / -0.1 / 0.8;
  - bound-DV Spearman: -0.5 / 0.0 / -0.1 (mean -0.20).
- All three SEC gates are false.

**Verification.**
- **Confirmed:**
  - C2 has no floor, and one of its 3 seeds is reversed.
  - The bound DV was non-gating and came out negative.
- **Overturned (skim detail):**
  - The C1 floor of 0.05 is inherited verbatim from V3-EXQ-740a.
  - The move to a gate on the positive control alone was a disclosed, user-selected decision at the
    queue gate. The docstring labels it "DELIVERABLE = THE POSITIVE CONTROL".
- **Overturned (skim framing):** since 2026-07-16 the bound/monotone DV belongs to INV-090.
- **Red-team addition:** decodability already clears 0.05 at onset 0 (0.065 / 0.183 / 0.093). So C1
  is a decodability-existence control, not a maturation result.
- **What remains:** the run tests INV-089's **premise**. That is a component of the confirming test
  in its 2026-09-21 what_would_answer, not an instance of the invariant. Governance already weighed
  exactly this reading on 2026-07-13 and 2026-07-16 and kept provisional with a narrow flag.

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | invariant untested; premise supported | |
| Biological reference | partial | |
| Prerequisites | present | SD-010 HarmEncoder, harm_eval_z_harm |
| Implementation | complete | |
| Environment | adequate for decodability | realized post-random-action harm under-determined for the evaluator DV |
| Measurement | adequate (C1); under-powered (C2) | invariant DV non-gating by design |
| Integration | isolated by design | frozen-representation probe |
| Scale | thin | 3 seeds |

**Failure location:** MEASURES. The run measured the premise, not the invariant. It is a PASS, so
there is no REE failure.

**Recommendation (revised after the red-team; see §9).**
- Direction stays **supports**, with **narrow_supports_flag: true**. Category **standard**.
  **Status: stays provisional.** pending_retest_after_substrate stays **true**.
- **Governance precondition.** Re-tag the V3-EXQ-746a manifest from INV-089 to INV-090. The
  2026-07-16 re-assignment never reached the index, which still scores a weakens against INV-089.
  INV-090 has no index entry at all.
- **Alternative for the user: provisional -> candidate.** If chosen, apply the same rule to
  MECH-304 (active -> provisional).

*Withdrawn argument:* the first draft proposed "non_contributory + provisional -> candidate". It was
withdrawn for three reasons:
- it re-litigated a twice-settled reading without any new fact;
- the new facts actually remove grounds for a stronger reading;
- the corpus (MECH-304 promoted on 759) treats claim-specific necessary-not-sufficient controls as
  narrow supports.

*Bears on (read across, not adjudicated):*
- 743's non-gating bound DV is a weak read against INV-090, and an admittedly unfair one; it is not
  scored here.
- Hypothesis registry `ceiling_vs_driver / H-ceiling`: a record-only edit, state unchanged.

## 3. Cluster read (Step 6)

| Experiment | Claim | Absolute / control leg | Leg that carried the PASS | Read |
|---|---|---|---|---|
| 158 | Q-018 | C4/C5 sanity (real) | C3 harm (phantom 0.0), C1/C2 (counts nothing consumes) | constant by construction |
| 763 | MECH-304 | readiness (real, 0.67) | DV2 (pinned 1.0), store gap (pinned 0), cue gap (genuine) | 2 of 3 constant; 1 genuine |
| 917 | SD-011 | apparatus readiness (real) | C2 (projection of a varying input) | proxy; substrate-inert C1 |
| 149b | Q-004 | C4 on the losing arm only | C2 slow-wins on an empty field | construct mismatch + inert channel |
| 743 | INV-089 | PC_events (real) | C1/C2 premise | proxy (premise, not invariant) |

**Not five independent bugs.** One structural property runs through them: *in each run the PASS
went through a quantity that could not vary with the manipulation the claim is about, or through a
proxy of the claim's object.*

- The quantity is pinned in three ways:
  - by the harness (158, and 763's arm B);
  - by a threshold outside the input's range (763's arm D);
  - by a substrate output that does not move in the tested regime (917's C1, 149b's field).
- A proxy stands in for the claim's object in three runs: 149b, 917, 743.
- One substrate fact links two runs: untrained, damage-sourced z_harm_a has a seed-determined
  raw-norm mean. That covers 917's C1 and coincides with 763's arm D. SD-MECH303-THRESHOLD-SOURCING
  has already addressed it for MECH-303.
- Readings:
  - test-design ceiling: 158, 763-B, 743;
  - substrate inertness: 917-C1, 763-D, 149b;
  - construct mismatch: 149b.
- Planning consequence:
  - Three direction corrections. 158 and 149b change the index weight. 917 changes none.
  - Two narrowings (763 and 743), with the narrow flag.
  - No single build unblocks the cluster.

**Granularity-debt recurrence trigger: does NOT fire.**
- Tagging targets (`granularity_debt_cluster.py`): Q-018 0, Q-004 0, MECH-304 0.
- INV-089: 4 targets, alignment intact=3 / weakened=1. The weakened one is 746a, already
  re-scoped to INV-090. The claim was already split on 2026-07-16.
- SD-011: 15 targets. This re-adjudication changes one of them (917) from strengthened to n/a.

## 4. Learning extracted

- **Phantom-key reads.** `obs_dict.get(key, default)` on a value the environment returns as a tuple
  element pins the DV to the default. A "not worse than" criterion then passes trivially. This is
  worth a lint candidate. It is noted here, not chipped.
- **Inert gates.** A gate that is counted but never consumed yields discrimination statistics that
  look like a mechanism test.
- **Ablations with every other path removed.** In such an ablation arm the necessity gap equals the
  intact arm's absolute rate. Report the absolute.
- **Thresholds outside the input's range.** A threshold above the input's full range turns an
  accumulation gate into a constant.
- **Declared proxies.** A declared proxy mapping (the residue field standing in for R(x,t)) must be
  checked against the claim's own source document, not only against the predecessor driver.
- **Positive controls checked on one arm.** A control applied only to the losing arm cannot certify
  the winning arm.
- **Claim tags on diagnostics.** A diagnostic tagged so that PASS means "the encoder can carry some
  input" is a transmission control, not evidence for the claim.
- **Directional criteria at small n.** A directional criterion with no noise floor at n=3 passes on
  a sign. Pair "mean > 0" with an SD floor or a seed-count floor.
- **Recording gap.** The 158 manifest (2026-03) lacks the always-record core. No re-run is owed for
  it, because the adjudication does not depend on the missing fields.

## 5. Routing summary (proposals; `/governance` ratifies)

| Run | Routing | Substrate entry |
|---|---|---|
| 158 | implement-substrate via the registered instrument; no 158a | amend `q018-provenance-authority-marking-instrument` (failure record) |
| 763 | queue-experiment: non-constructed MECH-303/304 dissociation retest (new EXQ number) | none (SD-MECH303-THRESHOLD-SOURCING built) |
| 917 | governance-reclassify (record correction) | none (prior create stands) |
| 149b | governance-reclassify; no 149c | create `mech001-astrocytic-regulatory-field-registration` (registration only, priority 3) |
| 743 | governance-reclassify (narrow flag + category); 746a -> INV-090 re-tag | none |

Per the staging rule and the 2026-07-30 rule, no follow-on was spawned. Governance chips whatever
it ratifies.

## 6. Change-string tails (GOV-APPLY-1)

The red-team checked all five against current claims.yaml values. Each is storable and not yet true.

| Claim | Tail |
|---|---|
| Q-018 | `-> epistemic_category: standard` (key absent) |
| MECH-304 | `-> epistemic_category: standard` (key absent); also set `narrow_supports_flag` |
| SD-011 | `-> non_contributory` (917 manifest; clears by provenance stamp) |
| Q-004 | `-> epistemic_category: substrate_conditional` (key absent) |
| INV-089 | `-> epistemic_category: standard` (key absent); also set `narrow_supports_flag` |

**Live-status pointers to re-derive.** These still cite the runs being re-adjudicated:
- Q-018 and Q-004 `live_status.evidence` (supports/PASS);
- MECH-304's promotion decision.

## 7. Step 9b -- hypothesis ledger (PENDING; not written)

This is staging mode, so `hypothesis_space_registry.v1.json` was not edited. The intended edits are
in the JSON `hypothesis_space_ledger_pending`.
- **Record only:** `ceiling_vs_driver / H-ceiling`. Append V3-EXQ-743 to resolving_runs as a
  non-discriminating run; state stays alive; no bar met.
- **Nothing to register** for 158, 149b or 917 (details in the JSON).
- **Optional, and not recommended yet:** a same-cycle question `mech304_cue_specific_release`. Hold
  it until the dissociation retest runs.
- No `growth_restriction` applies. No existing question is grown.

## 8. Step 7b pre-routing checks

Three fires; each was disposed of:
- **C1 on 917** (v3_exq_241 and v3_exq_472 drivers). **Dismissed.** 917's routing is
  governance-reclassify, and this artifact recommends no SD-011 experiment. 472 is the cited
  precedent. Noted for governance: an SD-011 dual-stream POC driver (241) exists and has never
  scored. A run like that, not 917, is what would bear on the split.
- **C2 on 763** (SD-051, mech303-safety-terrain-decay). **Dismissed.** SD-051 is the store under
  test. The decay knob would not remove the above-range threshold.
- **C2 on 917.** **Acted on** for `sd_zharm_a_warmup_optimizer_group`: it surfaced the untrained
  encoder. **Dismissed** for `sd_blocked_agency_mismatch_floor_calibration`, which is unrelated.

C5 was inapplicable: it ran on the JSON draft before this .md existed.

## 9. Step 7c red-team

The pass ran on **fable**, a different model from this session's Opus 5.5. It was given the draft
JSON and the raw evidence, and the author's reasoning was withheld. Verdicts:

- **158: CONFIRMED.** It found a second reason against a 158a re-queue: `harm_signal` is signed.
- **763: CONFIRMED.** Precision fix, now applied: a goal-dependent completion-release path was live
  in arm B but unreachable.
- **917: CONFIRMED.** Hygiene fixes, now applied: the untrained-encoder fact is not new to the
  corpus (it is in the V3-EXQ-930 note), and "does not move at all" was softened to "raw-norm mean
  seed-determined".
- **149b: CONFIRMED on facts.** Fixes, now applied:
  - the seed spread is 19-26x;
  - the equation's source is `regulatory_stack_model.md`;
  - the mapping was DECLARED in EXQ-149, not inherited silently;
  - the category cost is now stated as an explicit user option.
- **743: CONTESTED on status_change.**
  - *Counter-argument:* the draft's "provisional -> candidate" re-litigated a reading governance
    had settled twice (2026-07-13 and 2026-07-16) without any new fact. It was also inconsistent
    with keeping MECH-304 active on the same necessary-not-sufficient shape.
  - *Cheap confirmer:* `grep -n "STAYS provisional on 743's single-pathway positive control" REE_assembly/docs/claims/claims.yaml`.
  - *Outcome:* the red-team's repair was **adopted**:
    - supports + narrow flag;
    - stays provisional;
    - 746a re-tag as a precondition;
    - pending_retest kept true.

    The contested draft is recorded as a withdrawn argument.

## 10. Questions for the Step 8 gate (parent session)

1. **149b / Q-004.** Accept `substrate_conditional` plus a registration-only MECH-001 R(x,t) entry,
   which reverses the 2026-09-21 R0 disposition? Or register a separate residue-calibration question
   and keep a v3 lane?
2. **763 and 743 share one rule.** Keep both at their current status with narrow flags
   (recommended)? Or treat an unmet pre-registered promote gate as withdrawing the promotion, which
   means MECH-304 -> provisional and INV-089 -> candidate together?
3. **917.** Confirm overturning the 2026-08-12 SD-011 "supports". It carries zero index weight either
   way.
4. **158.** Confirm routing to the registered Q-018 instrument rather than a corrected 158a.
