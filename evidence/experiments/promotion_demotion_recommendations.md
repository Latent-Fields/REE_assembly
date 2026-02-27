# Promotion / Demotion Recommendations

Generated: `2026-02-27T15:08:08.175494Z`
Decision scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

This file proposes decisions only. No claim status changes are applied automatically.
Use this as the human-in-the-loop review queue.

## Decision Queue

| claim_id | current_status | decision_needed | recommendation | decision_status |
|---|---|---|---|---|
| `ARC-003` | `active` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `ARC-005` | `active` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `ARC-007` | `active` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `ARC-018` | `provisional` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `IMPL-022` | `stable` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `MECH-033` | `provisional` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `MECH-040` | `provisional` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `MECH-046` | `provisional` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `MECH-053` | `provisional` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `MECH-054` | `provisional` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `MECH-057` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-058` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-062` | `stable` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `MECH-063` | `provisional` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `Q-001` | `active` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `Q-002` | `active` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `Q-003` | `active` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `Q-004` | `active` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `Q-005` | `active` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `Q-006` | `active` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `Q-007` | `active` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `Q-012` | `candidate` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `Q-013` | `active` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `Q-014` | `active` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `Q-015` | `active` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `Q-016` | `active` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |
| `Q-017` | `active` | Genuine evidence required before any status change | `collect_genuine_evidence` | `pending_user` |

## Decision Details

### ARC-003
- Current status: `active`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for ARC-003 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 7. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=4, weakens=4, mixed=0, unknown=0, conflict_ratio=1
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-25T16:56:17.901452Z`
- Last selected option: retain_ree
- Last rationale: Refreshed after corrected thought-date intake; retain REE E3 trajectory-commitment architecture with current task-loop extraction clarifications.

### ARC-005
- Current status: `active`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for ARC-005 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 2. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=3, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`

### ARC-007
- Current status: `active`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for ARC-007 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 12. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=8, weakens=4, mixed=0, unknown=0, conflict_ratio=0.667
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-15T18:46:42.773429Z`
- Last selected option: hybridize
- Last rationale: Applied anti-lock-in dispatch recommendation: hybridize; basis=high_conflict; conflict_ratio=0.857; overall_confidence=0.58.

### ARC-018
- Current status: `provisional`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for ARC-018 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 9. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=6, weakens=4, mixed=0, unknown=0, conflict_ratio=0.8
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-15T18:46:42.773429Z`
- Last selected option: retain_ree
- Last rationale: Applied anti-lock-in dispatch recommendation: retain_ree; basis=conflict_below_hybrid_threshold; conflict_ratio=0.6; overall_confidence=0.639.

### IMPL-022
- Current status: `stable`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for IMPL-022 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 2. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=0, weakens=2, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`

### MECH-033
- Current status: `provisional`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for MECH-033 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 10. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=7, weakens=4, mixed=0, unknown=0, conflict_ratio=0.727
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-15T18:46:42.773429Z`
- Last selected option: retain_ree
- Last rationale: Applied anti-lock-in dispatch recommendation: retain_ree; basis=conflict_below_hybrid_threshold; conflict_ratio=0.6; overall_confidence=0.637.

### MECH-040
- Current status: `provisional`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for MECH-040 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 9. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=5, weakens=4, mixed=0, unknown=0, conflict_ratio=0.889
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-15T18:46:42.773429Z`
- Last selected option: retain_ree
- Last rationale: Applied anti-lock-in dispatch recommendation: retain_ree; basis=conflict_below_hybrid_threshold; conflict_ratio=0.667; overall_confidence=0.607.

### MECH-046
- Current status: `provisional`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for MECH-046 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 9. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=5, weakens=4, mixed=0, unknown=0, conflict_ratio=0.889
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-15T18:46:42.773429Z`
- Last selected option: retain_ree
- Last rationale: Applied anti-lock-in dispatch recommendation: retain_ree; basis=conflict_below_hybrid_threshold; conflict_ratio=0.667; overall_confidence=0.597.

### MECH-053
- Current status: `provisional`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for MECH-053 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 2. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=2, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-15T20:51:27.090007Z`
- Last selected option: promote_to_provisional
- Last rationale: Applied approved promotion decision from governance queue.

### MECH-054
- Current status: `provisional`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for MECH-054 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 2. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=3, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-15T20:51:27.090007Z`
- Last selected option: promote_to_provisional
- Last rationale: Applied approved promotion decision from governance queue.

### MECH-057
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.521, conflict_ratio=1, exp_entries=12, lit_entries=0; directions supports=6, weakens=6, mixed=0, unknown=0, conflict_ratio=1
- Recommendation: `hold_candidate_resolve_conflict`
- Options (pros/cons):
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-02-25T16:39:07.535473Z`
- Last selected option: hold_candidate_resolve_conflict
- Last rationale: Applied conflict-lane hold after architecture adjudication (hybridize); keep candidate while reducing uncertainty with targeted probes.

### MECH-058
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.724, conflict_ratio=0.816, exp_entries=94, lit_entries=5; directions supports=58, weakens=40, mixed=1, unknown=0, conflict_ratio=0.816
- Recommendation: `hold_candidate_resolve_conflict`
- Options (pros/cons):
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-02-25T16:39:07.573674Z`
- Last selected option: hold_candidate_resolve_conflict
- Last rationale: Applied conflict-lane hold after architecture adjudication (hybridize); maintain candidate status while anchor-separation conflict signatures are worked down.

### MECH-062
- Current status: `stable`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for MECH-062 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 44. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=32, weakens=0, mixed=12, unknown=0, conflict_ratio=0
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-25T14:07:04.606327Z`
- Last selected option: promote_to_stable
- Last rationale: Applied previously approved promotion decision; claims registry status updated to stable.

### MECH-063
- Current status: `provisional`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for MECH-063 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 2. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=2, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-15T20:51:27.090007Z`
- Last selected option: promote_to_provisional
- Last rationale: Applied approved promotion decision from governance queue.

### Q-001
- Current status: `active`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for Q-001 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 11. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=7, weakens=4, mixed=0, unknown=1, conflict_ratio=0.727
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`

### Q-002
- Current status: `active`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for Q-002 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 11. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=7, weakens=4, mixed=0, unknown=1, conflict_ratio=0.727
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`

### Q-003
- Current status: `active`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for Q-003 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 11. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=7, weakens=4, mixed=0, unknown=1, conflict_ratio=0.727
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`

### Q-004
- Current status: `active`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for Q-004 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 11. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=7, weakens=4, mixed=0, unknown=1, conflict_ratio=0.727
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`

### Q-005
- Current status: `active`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for Q-005 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 11. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=7, weakens=4, mixed=0, unknown=1, conflict_ratio=0.727
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`

### Q-006
- Current status: `active`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for Q-006 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 11. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=7, weakens=4, mixed=0, unknown=1, conflict_ratio=0.727
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-25T16:51:50.794689Z`
- Last selected option: retain_open_question_with_prototype_first
- Last rationale: Keep Q-006 open while prioritizing prototype assembly; ethics-development adjudication is deferred until richer integrated behavior is observable.

### Q-007
- Current status: `active`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for Q-007 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 12. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=8, weakens=4, mixed=0, unknown=1, conflict_ratio=0.667
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`

### Q-012
- Current status: `candidate`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for Q-012 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 8. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=4, weakens=4, mixed=0, unknown=0, conflict_ratio=1
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-15T18:46:42.773429Z`
- Last selected option: retain_ree
- Last rationale: Applied anti-lock-in dispatch recommendation: retain_ree; basis=conflict_below_hybrid_threshold; conflict_ratio=0.667; overall_confidence=0.634.

### Q-013
- Current status: `active`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for Q-013 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 13. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=9, weakens=4, mixed=0, unknown=0, conflict_ratio=0.615
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-25T16:51:50.720541Z`
- Last selected option: hybridize
- Last rationale: Adjudicated Q-013 to hybridize: keep deterministic JEPA baseline with derived dispersion as default, while preserving a guarded stochastic-head branch as an interface candidate pending discriminative calibration evidence.

### Q-014
- Current status: `active`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for Q-014 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 13. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=9, weakens=4, mixed=0, unknown=0, conflict_ratio=0.615
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-25T16:51:50.758372Z`
- Last selected option: hybridize
- Last rationale: Adjudicated Q-014 to hybridize: preserve invariance for robustness but require explicit ethical-relevance probes and fallback pathways when invariance suppresses responsibility-relevant distinctions.

### Q-015
- Current status: `active`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for Q-015 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 9. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=5, weakens=4, mixed=0, unknown=0, conflict_ratio=0.889
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-15T18:46:42.773429Z`
- Last selected option: retain_ree
- Last rationale: Applied anti-lock-in dispatch recommendation: retain_ree; basis=conflict_below_hybrid_threshold; conflict_ratio=0.667; overall_confidence=0.586.

### Q-016
- Current status: `active`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for Q-016 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 77. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=53, weakens=0, mixed=24, unknown=0, conflict_ratio=0
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-25T16:51:50.829631Z`
- Last selected option: retain_open_question_with_policy_probe_plan
- Last rationale: Keep Q-016 open with explicit probe-plan requirement; tri-loop conflict arbitration policy remains an unresolved design-space question pending targeted mechanism tests.

### Q-017
- Current status: `active`
- Decision needed: Genuine evidence required before any status change
- Why this decision is needed: All experimental evidence for Q-017 is from synthetic substrates (ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: 0. Total synthetic exp entries: 95. Confidence scores and conflict ratios are unreliable. Collect ≥1 genuine experimental run on ree-v1-minimal before treating this claim as a promotion or demotion candidate.; directions supports=59, weakens=40, mixed=1, unknown=0, conflict_ratio=0.808
- Recommendation: `collect_genuine_evidence`
- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates (ree-v2 / ree-experiments-lab). Confidence scores unreliable. Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate.
- Options (pros/cons):
  - Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).
  - Demote to legacy and re-open when genuine evidence is available.
  - Keep current status and suppress recommendations until genuine run completes.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-25T16:51:50.648196Z`
- Last selected option: hybridize
- Last rationale: Reaffirmed Q-017 as hybridized: retain REE orthogonal control-axis framing while using external priors only through interface-level guardrails; resolve via scoped axis-ablation follow-ups.
