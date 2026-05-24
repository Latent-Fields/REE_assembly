# Failure Autopsy: V3-EXQ-603 (Q-045 / MECH-313 / MECH-260)

**Generated**: 2026-05-24T05:57:54Z  
**Scope**: single  
**Status**: confirmed  
**Autopsy session**: failure-autopsy-603-20260523T222253Z

---

## 1. Target

| Field | Value |
|---|---|
| run_id | v3_exq_603_q045_mech313_mech260_four_arm_ablation_20260521T204222Z_v3 |
| queue_id | V3-EXQ-603 |
| claim_ids | Q-045, MECH-313, MECH-260 |
| outcome | FAIL x2 (two independent runs, bit-identical) |
| experiment_purpose | evidence |
| manifest evidence_direction | mixed (per-claim: MECH-313 supports, MECH-260 weakens, Q-045 mixed) |

---

## 2. Facts Reconstruction

### Arm results (mean entropy across 3 seeds)

| ARM | Config | entropy | delta vs ARM_0 |
|-----|--------|---------|---------------|
| ARM_0 | both-OFF | 0.244051 | baseline |
| ARM_1 | MECH-313 only | 0.292153 | +0.048 |
| ARM_2 | MECH-260 only | 0.244051 | 0.000 (identical to ARM_0) |
| ARM_3 | both-ON | 0.292153 | +0.048 (identical to ARM_1) |

ARM_2 == ARM_0 and ARM_3 == ARM_1 to 6 decimal places, including per-seed step counts
and unique_actions counts. Two independent runs (same session and 6h later) confirm this
is deterministic and structural.

### Criteria

| Criterion | Result | Detail |
|---|---|---|
| C1: both-ON beats both-OFF | False | margin 0.048 < ENTROPY_MARGIN 0.05 |
| C2: mutually load-bearing | False | ARM_3 = ARM_1; MECH-260 adds zero |
| C3: each-alone beats off | False | ARM_2 = ARM_0 exactly |
| overall_pass | False | |

### Manifest evidence_direction (as written by script)

- MECH-313: "supports" (ARM_1 > ARM_0, but below margin)
- MECH-260: "weakens" (ARM_2 entropy < ARM_1 entropy, but this is MECH-260-alone vs
  MECH-313-alone, not vs baseline -- script logic compares wrong arms)
- Q-045: "mixed" (derives from sub-claims being split)

**All three directions are artifacts of the broken call path or misleading comparison logic.**

---

## 3. Root Cause

The experiment uses `agent.act_with_split_obs(obs_body, obs_world)` under `torch.no_grad()`
(pure inference, no training). MECH-260 anti-recency suppression requires
`dacc.record_action(argmax(action[0]))` to be called each step to populate the FIFO
suppression history. That call lives in `select_action()` -- NOT in `act_with_split_obs()`.

Result: in every ARM_2 and ARM_3 step, the FIFO is permanently empty, suppression is
always 0.0, and the dACC module produces zero behavioral effect. ARM_2 is structurally
identical to ARM_0, and ARM_3 is structurally identical to ARM_1.

MECH-313 (temperature noise floor) modifies `effective_T = max(baseline_T + noise_floor_alpha,
min_temperature)` directly at the `e3.select()` call site with no history dependency --
so it IS operative in inference-only mode and produces the real +0.048 entropy lift.

### Pre-run warning that was not acted on

The Q-045 evidence_quality_note (from the 2026-05-11 lit-pull) contained:

> "current 4-arm design insufficient; needs extension to 8-cell OR addition of LC->ACC
> coupling ablation... SD-054 substrate-readiness for multi-trial outcome dependencies
> must be verified BEFORE 4-arm authorisation... a single-tick outcome substrate cannot
> dissociate MECH-260 from MECH-313 in the Kennerley sense."

The experiment ran despite this pre-authorization flag. This is a design-gate failure in
addition to a call-path failure.

---

## 4. Claim-Layer Map

| Claim | Type | Status | Prior evidence | Did this test let it express? |
|---|---|---|---|---|
| MECH-260 | mechanism_hypothesis | candidate, v3_pending | EXQ-445h supports (C3 3/3 seeds) | NO -- record_action() never called |
| MECH-313 | mechanism_hypothesis | candidate_substrate_landed, v3_pending | None prior | Partial -- operative but sub-threshold |
| Q-045 | open_question | open | lit_conf=0.9 (COUPLED-NOT-COLLAPSED) | NO -- MECH-260 non-operative |

Notes:
- MECH-313 depends_on MECH-260 in claims.yaml. The ablation was designed assuming both
  would be operative; only one was. This creates an asymmetric test.
- MECH-260's EXQ-445h evidence record is from a training run using select_action() and
  is unaffected by this failure.
- The "weakens" direction for MECH-260 must not be allowed to weight governance.

---

## 5. Biological-Reference Triage

### MECH-260 (dACC anti-recency)
**Closest mechanism**: dACC action-outcome history integration across trials  
**Literature**: Scholl & Kolling 2015, Kennerley 2006 (DOI 10.1038/nn1724)  
**Biological faithfulness**: high -- FIFO suppression is a biologically grounded
implementation of the action-repetition penalty observed in dACC multi-trial recordings.  
**Key property**: inherently multi-step, history-dependent. Testing in single-step inference
with an empty FIFO tests a completely uninstantiated mechanism -- equivalent to testing
hippocampal sequence memory in an animal with no prior experience.  
**Divergence from biology**: the call-path failure is an implementation detail, not a
biological divergence. The biological mechanism is intact.

### MECH-313 (LC-NE tonic noise floor)
**Closest mechanism**: locus coeruleus tonic norepinephrine release as stochastic
background for state-dependent neuromodulation  
**Literature**: Aston-Jones & Cohen 2005, Haarnoja 2018 (SAC entropy regularization
as computational analog), Faisal 2008  
**Biological faithfulness**: moderate -- temperature floor is a reasonable simplified
proxy for LC tonic NE. State-independent design is biologically appropriate for tonic
(as opposed to phasic) LC activity.  
**Result here**: operative, real +0.048 effect, directionally correct. Sub-threshold.

### Q-045 (LC-NE / dACC substrate independence)
**Literature (lit-pull R1)**: Tervo et al. 2014 (Cell, DOI 10.1016/j.cell.2014.08.037)  
**Biological verdict**: COUPLED-NOT-COLLAPSED. LC-NE input drives dACC stochastic-mode
switching; the substrates are coupled at the circuit level. The biology predicts they are
distinct but interacting -- not fully independent and not fully collapsed. This prediction
is untestable when one mechanism is non-operative.

---

## 6. Four-Layer Diagnosis Table

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | measurement gap | MECH-260 blocked from expressing; MECH-313 operative but sub-threshold |
| Biological reference | clear | Both mechanisms well-grounded; failure matches missing-prerequisite signature |
| Prerequisites | missing | MECH-260 requires per-step call through select_action(); act_with_split_obs() bypasses it |
| Implementation completeness | partial | MECH-313 complete and operative; MECH-260 module exists but call path broken for inference-only |
| Environment adequacy | likely insufficient | SD-054 temporal-horizon requirement for Kennerley-style history not verified |
| Measurement adequacy | misleading | Entropy metric correct in principle; script's conditional logic assigns evidence_direction via wrong-arm comparison |
| Integration adequacy | broken for MECH-260 | act_with_split_obs() / select_action() call-path split creates inference-vs-training gap |
| Scale / capacity | unknown | Zero training steps; MECH-260 temporal horizon may require 10s-100s of accumulated steps |

**Dominant diagnosis**: measurement_gap (inference-path bypass of history-accumulating mechanism)

**Recommended epistemic_category**: measurement_gap

---

## 7. Learning Extracted

1. **Call-path audit rule for inference-only experiments**: any experiment using
   `act_with_split_obs()` must explicitly verify that all mechanisms under test have their
   wiring on that path. The select_action() / act_with_split_obs() split is a latent
   footgun for history-dependent mechanisms (dACC, hippocampal replay, anything with
   accumulated state).

2. **Design-gate violation**: the Q-045 lit-pull (2026-05-11) pre-authorized a warning
   ("verify SD-054 substrate readiness BEFORE 4-arm authorization; Kennerley criterion
   requires sufficient temporal horizon"). The experiment ran without satisfying that
   gate. A mechanism for enforcing lit-pull authorization conditions on queue entries is
   needed.

3. **MECH-313 produces a real sub-threshold signal (+0.048)** directionally consistent
   with the noise-floor hypothesis. NC for governance (below margin) but non-zero.
   This is a narrow directional signal, not zero evidence.

4. **MECH-260's valid evidence record is unaffected**: EXQ-445h (C3 3/3 seeds, training
   run via select_action()) remains the valid support for MECH-260.

5. **The "weakens" direction in the manifest must not enter governance weighting**.
   It is an artifact of comparing ARM_2 vs ARM_1 (not vs baseline) and of MECH-260 being
   non-operative. Any future governance session touching MECH-260 confidence must exclude
   V3-EXQ-603 entirely.

---

## 8. Repair Pathway

**Routing**: /queue-experiment for V3-EXQ-603a

### Required fixes for 603a

**Fix 1 (mandatory)**: Ensure `dacc.record_action(action)` is called for MECH-260 arms.
Options in order of biological fidelity:
  a. (Preferred) Run training episodes using select_action() (where record_action is
     already wired), then measure behavioral diversity post-training
  b. (Acceptable) Add dacc.record_action(action) call inside act_with_split_obs() for
     experiment-only instrumentation -- clearly comment as experiment scaffolding

**Fix 2 (required)**: Verify SD-054 temporal horizon. The FIFO must accumulate enough
steps to differentiate arms. Kennerley criterion suggests many trials; minimum:
>= 2 x dacc_suppression_memory (default=8) = 16 steps, but likely 50-100+ for robust
action-history statistics.

**Fix 3 (recommended)**: Fix the evidence_direction assignment logic. Compare each arm
vs ARM_0 (baseline), not arm vs arm. This is a script-design bug that will propagate
to any future runs using the same template.

**Future extension (603b, not a prerequisite for 603a)**: 8-cell design (4 arms x 2 LC
amplitudes) per lit-pull R4 recommendation, to expose the Tervo LC->dACC asymmetry.

---

## 9. Recommended Governance Writes

These are RECOMMENDATIONS ONLY. /governance applies them interactively.

### MECH-260 evidence_quality_note addition
```
[2026-05-23 autopsy V3-EXQ-603]: MEASUREMENT GAP -- act_with_split_obs() bypasses
select_action() where dacc.record_action() is called; FIFO permanently empty,
suppression zero throughout. ARM_2==ARM_0 to 6 d.p. across all seeds+step counts
(2 independent runs confirm structural). 'weakens' direction in manifest is a
script logic artifact (wrong-arm comparison). EXQ-445h (C3 3/3 seeds) remains
valid evidence. Pending retest: 603a with call path repaired.
```

### MECH-313 evidence_quality_note addition
```
[2026-05-23 autopsy V3-EXQ-603]: MEASUREMENT GAP -- +0.048 entropy lift above control
(below 0.05 threshold), directionally consistent with noise-floor hypothesis but
sub-threshold and confounded by MECH-260 non-operativeness. 'supports' in manifest
overstates. Non-contributory pending 603a retest under valid MECH-260 conditions.
```

### Q-045 evidence_quality_note addition
```
[2026-05-23 autopsy V3-EXQ-603]: NON-CONTRIBUTORY -- MECH-260 non-operative
(inference call-path bypass); substrate-independence question untestable.
Lit-pull R5 flag (Kennerley temporal-horizon, design-gate) also unresolved.
Pending retest: 603a with call path repaired and temporal horizon verified.
```

### Recommended manifest overrides (for /governance to apply)
- V3-EXQ-603 both manifests: evidence_direction -> non_contributory
- evidence_direction_per_claim: all three -> non_contributory
- epistemic_category: measurement_gap

---

## 10. Confirmed Routing

**User judgment (2026-05-24)**: Confirmed -- write artifacts and queue 603a.

**Routing**: /queue-experiment for V3-EXQ-603a (call-path fix + temporal horizon verification)
