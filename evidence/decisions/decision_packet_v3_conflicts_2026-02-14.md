# V3 Conflict Decision Packet (2026-02-14)

Purpose: human-in-the-loop decision packet for the four active candidate-mechanism conflicts.
Data snapshot source: `evidence/experiments/claim_evidence.v1.json`, `evidence/experiments/conflicts.md`, `evidence/planning/experiment_proposals.v1.json` generated on 2026-02-14.

## Decision Rule (used consistently)

- **Promote candidate -> provisional** only when:
  - directional conflict is low/stable (no active directional conflict alert), and
  - at least one replication batch passes without the current recurring failure signatures.
- **Hold at candidate** when:
  - there is active directional conflict and mechanism shape is still useful enough to keep testing.
- **Demote to legacy** when:
  - repeated adjudication runs keep failing on the same signature class and no narrowed sub-claim remains defensible.

---

## Claim: `MECH-056`

### What this claim means

`MECH-056` = **trajectory-first residue placement**.
In plain terms: when there is mismatch/failure, REE should first place update pressure in **trajectory/decision space** (what was chosen and projected), before treating it as pure representational distortion.

### Current evidence state

- Claim status: `candidate`
- Aggregate confidence: `0.576`
- Direction counts: supports=`3`, weakens=`1`, mixed=`0`
- Source counts: experimental=`2`, literature=`2`
- Conflict ratio: `0.5` (directional conflict still active)
- Current recurring signatures from conflict report:
  - `ledger_editing`
  - `explanation_policy_divergence`

### Decision recommendation

- Recommendation: **hold at candidate** (`hold_candidate_resolve_conflict`)
- Why: evidence leans supportive, but conflict is unresolved and failure signatures are architectural (not cosmetic).

### Focused adjudication actions

- Experimental dispatch: `EXP-0010` to `ree-v1-minimal` (`trajectory_integrity`)
- Literature dispatch: `LIT-0011` in `REE_assembly` (`targeted_review_v3_hippocampal_rollout`)
- Promotion gate for this claim:
  - one clean replication set without `ledger_editing` and without `explanation_policy_divergence`.

---

## Claim: `MECH-058`

### What this claim means

`MECH-058` = **JEPA EMA target-anchor timescale separation**.
In plain terms: stable slow target dynamics (anchor) plus faster predictor adaptation is a required substrate pattern for REE-style E1/E2 stability.

### Current evidence state

- Claim status: `candidate`
- Aggregate confidence: `0.729`
- Direction counts: supports=`4`, weakens=`7`, mixed=`1`
- Source counts: experimental=`10`, literature=`2`
- Conflict ratio: `0.727` (high directional conflict)
- Current recurring signatures:
  - `mech058:ema_drift_under_shift`
  - `mech058:latent_cluster_collapse`
  - `mech058:anchor_separation_collapse`

### Decision recommendation

- Recommendation: **hold at candidate** (`hold_candidate_resolve_conflict`)
- Why: literature says substrate idea is plausible, but experiment lane still weakens more often than supports.

### Focused adjudication actions

- Experimental dispatch: `EXP-0013` to `ree-experiments-lab` (`jepa_anchor_ablation`)
- Literature dispatch: `LIT-0014` in `REE_assembly` (`targeted_review_mech_058`)
- Promotion gate for this claim:
  - replication under distribution shift where anchor metrics no longer show collapse signatures.

---

## Claim: `MECH-059`

### What this claim means

`MECH-059` = **confidence-channel separation from residual prediction error**.
In plain terms: REE should keep a confidence channel (uncertainty-derived precision) separate from generic prediction error, so control policy can be calibrated explicitly.

### Current evidence state

- Claim status: `candidate`
- Aggregate confidence: `0.755`
- Direction counts: supports=`4`, weakens=`7`, mixed=`2`
- Source counts: experimental=`10`, literature=`3`
- Conflict ratio: `0.727` (high directional conflict)
- Current recurring signatures:
  - `mech059:calibration_slope_break`
  - `mech059:uncertainty_metric_gaming_detected`
  - `mech059:abstention_reliability_collapse`

### Decision recommendation

- Recommendation: **hold at candidate** (`hold_candidate_resolve_conflict`)
- Why: claim is structurally important, but current implementation evidence is still unstable and gameable.

### Focused adjudication actions

- Experimental dispatch: `EXP-0015` to `ree-experiments-lab` (`jepa_uncertainty_channels`)
- Literature dispatch: `LIT-0016` in `REE_assembly` (`targeted_review_v3_jepa_mapping_limits`)
- Promotion gate for this claim:
  - calibration remains stable across adversarial/gaming checks and abstention reliability remains above stop thresholds.

---

## Claim: `MECH-060`

### What this claim means

`MECH-060` = **dual error channels (pre-commit vs post-commit)**.
In plain terms: REE should route error signals differently before a commitment (planning/control) vs after commitment (attribution/learning), instead of one merged channel.

### Current evidence state

- Claim status: `candidate`
- Aggregate confidence: `0.777`
- Direction counts: supports=`6`, weakens=`7`, mixed=`2`
- Source counts: experimental=`10`, literature=`5`
- Conflict ratio: `0.923` (very high directional conflict)
- Current recurring signatures:
  - `mech060:precommit_channel_contamination`
  - `mech060:postcommit_channel_contamination`
  - `mech060:attribution_reliability_break`

### Decision recommendation

- Recommendation: **hold at candidate** (`hold_candidate_resolve_conflict`)
- Why: strongest conceptual importance, but highest conflict and channel contamination persists.

### Focused adjudication actions

- Experimental dispatch: `EXP-0017` to `ree-experiments-lab` (`commit_dual_error_channels`)
- Literature dispatch: `LIT-0018` in `REE_assembly` (`targeted_review_v3_prefrontal_control`)
- Promotion gate for this claim:
  - channel contamination signatures eliminated across seed sweeps and attribution reliability remains stable post-commit.

---

## Resolution Log

- `2026-02-14`: user approved all recommendations in this packet.
- Approved status decisions:
  - `MECH-056`: `hold_candidate_resolve_conflict`
  - `MECH-058`: `hold_candidate_resolve_conflict`
  - `MECH-059`: `hold_candidate_resolve_conflict`
  - `MECH-060`: `hold_candidate_resolve_conflict`
- Approved execution order:
  - option A: `MECH-060` -> `MECH-059` -> `MECH-058` -> `MECH-056`
