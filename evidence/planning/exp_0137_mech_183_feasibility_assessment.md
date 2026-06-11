# EXP-0137 (MECH-183) Feasibility Assessment

**Assessment Date:** 2026-06-11
**Assessor:** IGW-200 auto-spawned session
**Proposal ID:** EXP-0137
**Claim:** MECH-183 (z_beta leakage: attributed other-model affective state activates self z_beta directly)

---

## Summary

**Recommendation: DEFER to V5.**

EXP-0137 cannot be meaningfully implemented in V3 because MECH-183 requires social/other-agent substrate that does not exist in V3 and is explicitly scoped to V5 (forward roadmap).

---

## Claim Requirements vs V3 Substrate

### MECH-183 Dependencies

From `claims.yaml`:
```
depends_on:
  - INV-005  (harm via mirror modelling, not symbolic rules)
  - MECH-031 (derived social tags, OTHER_SELFLIKE empathy coupling)
  - MECH-032 (other-model infrastructure)
```

### What MECH-183 Needs

1. **Other-agent model**: A computational representation of another agent's internal state
2. **Attribution stream**: Mechanism to attribute observed behavior/signals to the other-agent model
3. **OTHER_SELFLIKE tagging**: Control-plane mechanism to couple self and other processing
4. **Multi-agent environment**: Testable scenarios with observable other-agent distress cues
5. **z_beta direct activation pathway**: Route from other-model state → self z_beta (bypassing inference)

### What V3 Has

- z_beta (affective arousal) ✓
- Attribution comparator (MECH-095 TPJ analog for self/world) - partially relevant
- Observation processing ✓
- Prediction error machinery ✓

### What V3 Does NOT Have

- Other-agent models ✗
- Multi-agent environments ✗
- OTHER_SELFLIKE tagging ✗
- Social attribution pathways ✗

---

## V5 Roadmap Context

From `fast_empathy_v5_plan.md`:

- **Generation:** v5 (forward roadmap; SOCIAL mind tier; excluded from V3 closure %)
- **Scope claims:** ARC-010, MECH-031, MECH-112, SD-011, **MECH-183**, MECH-191, MECH-359, MECH-360
- **Status:** roadmap (no experiments yet; nodes carry no owner_exq)

Key passage (lines 68-75):
> "EMP-3: Stream-binding mechanism: route own motivational-affective streams across the other-model"
> blocking_on: "Requires a stable other-model (ARC-010 mirror modelling materialised as a per-agent object-file slot, object_representation_v4:OBJ-5 / ARC-083), which is gated on MECH-163 multi-step hippocampal planning (V4 social-entry gate) AND DEV-NEED-021 prerequisites (object-permanence + a stable self, both V4)."

**Critical blocker**: MECH-183 is line 73's seed:
> "V3/V4 SEEDS this builds on: MECH-031 (derived social tags / empathy coupling), **MECH-183 (z_beta leakage = attributed other-state activates self z_beta directly)**, SD-011 (the suffering stream that becomes other-bound)..."

MECH-183 is listed as a **seed** that EMP-3 builds on, meaning it's a conceptual/theoretical anchor for V5 design, not a V3-implementable experiment.

---

## Why V3 Proxy Experiments Are Not Viable

### Option A: Simulated Other-Distress Cues

**Proposal**: Test if z_beta activates in response to environmental patterns that *would* signal other-distress (e.g., specific observation sequences) without requiring predictive inference.

**Problem**:
- Without an actual other-agent, this tests "pattern → z_beta activation," not "attributed other-state → self z_beta activation"
- Fails to test the core mechanism: the **attribution** gate and **other-model coupling**
- Would produce misleading evidence: a PASS would not validate MECH-183, and a FAIL would not invalidate it

### Option B: Cross-Modal z_beta Activation

**Proposal**: Test if z_beta can be activated by cues in one modality (e.g., acoustic) that correlate with self-distress in another modality (e.g., proprioceptive harm).

**Problem**:
- Tests sensory association learning, not social attribution
- MECH-183's novelty claim is specifically about **other-agent** affective state leakage via attribution stream
- This would be a test of MECH-182 (acoustic harm signaling) at best, which already has literature support

---

## Existing Evidence for MECH-183

From `claim_evidence.v1.json` (55 mentions):

**Literature support:**
- Lamm, Decety & Singer (2011): bilateral anterior insula / dACC activation for both self-pain and empathy-for-pain (neural substrate of "z_beta leakage")
- Preston & de Waal (2002), Lamm (2011): Perception-Action Model (PAM) functional description
- Yu et al. (2024): multimodal emotional contagion in rodents, emphasizes "automatic and unconscious" channels

**Current evidence status:**
- exp_conf: 0.0 (no experimental evidence in REE)
- lit_conf: moderate to high (PAM well-established; attribution-gated leakage is novel claim)

**Gap**: The **attribution-gated** and **OTHER_SELFLIKE-coupled** aspects are novel and need experimental validation, but that validation requires V5 social substrate.

---

## Recommendations

### 1. Update EXP-0137 Status

Mark EXP-0137 as **deferred** in `experiment_proposals.v1.json`:
```json
{
  "proposal_id": "EXP-0137",
  "status": "deferred_substrate_not_ready",
  "blocking_on": "V5 social substrate: other-agent model (ARC-010, MECH-031, MECH-032), multi-agent environment, attribution stream infrastructure",
  "earliest_feasible_generation": "v5",
  "deferral_date": "2026-06-11",
  "deferral_reason": "MECH-183 z_beta leakage mechanism requires other-agent model and attribution stream not present in V3. No V3-compatible proxy experiment can meaningfully test the core claim without risking misleading evidence."
}
```

### 2. Queue for V5 Roadmap

Add to the V5 social-substrate planning:
- After EMP-3 (stream-binding mechanism) lands, MECH-183 becomes experimentally testable
- Suggested experiment type: multi-agent scenario with observable distress cues; measure z_beta activation in observer agent; dissociate direct activation (via attribution stream) from inference (via prediction)
- Candidate design: 2x2 factorial (OTHER_SELFLIKE tag ON/OFF × distress cue present/absent)

### 3. Interim Action: None Required

No placeholder experiment should be queued. MECH-183's literature support is adequate for governance purposes until V5 substrate exists.

---

## Conclusion

EXP-0137 is a valid and important proposal, but it is **generation-mismatched**: it targets a V5 mechanism using V3 substrate. Queueing a V3 proxy would waste runner capacity and produce non-diagnostic evidence.

**Action:** Mark proposal as `deferred_substrate_not_ready` and revisit when V5 social infrastructure (other-model, attribution stream, multi-agent environment) is available.

---

**Session ID:** igw-200-exp-0137-mech-183
**Assessment Logged:** 2026-06-11T08:25:00Z
