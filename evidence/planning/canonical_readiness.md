# Canonical Readiness (canonical_readiness/v1)

Generated: 2026-09-01T04:57:20Z

## Verdict: NO_WARRANT

There is not yet sufficient evidence to justify a canonical-profile admission pass. This is the normal developmental state before the relevant conditions have converged -- it is not a failure of the project.

Reasons this pass:
- Gate A: NO_IDENTIFIABLE_ORGANISM; no (substrate_commit, enabled_default_off_flags) combination recurs across >=2 distinct experiment_type values at size >=3; substrate_hash recurrence exists (see fingerprint_recurring_best_group) but is code-identity only -- it does not by itself establish that the SAME configuration was tested, only that the SAME code checkout was; per Gate A tier 2 this is informational, not sufficient to satisfy the gate on its own in this detector
- Gate B: unmeasured (No instrumentation exists in this detector pass for Gate B (canonical-profile candidate substrate -- admission-doctrine criteria per evidence/planning/architecture_epoch_investigation.md section 9 (corpus enablement, cited-evidence-run check, non-degeneracy, known-interaction check)). This is reported as UNMEASURED, not FALSE: absence of evidence is not evidence of absence, and this detector's conservative posture requires that distinction stay visible rather than collapsing to a green or red reading.)
- Gate D: unmeasured (No instrumentation exists in this detector pass for Gate D (whole-organism non-degeneracy -- moves, observation variance, action collapse, candidate generation, no NaN dominance; couples to the GOV-CAPCONTRACT-1 capability/plasticity contract). This is reported as UNMEASURED, not FALSE: absence of evidence is not evidence of absence, and this detector's conservative posture requires that distinction stay visible rather than collapsing to a green or red reading.)
- Gate E: unmeasured (No instrumentation exists in this detector pass for Gate E (behavioural evidence -- Behavioural Evidence Ladder rung attributable to a single identifiable organism). This is reported as UNMEASURED, not FALSE: absence of evidence is not evidence of absence, and this detector's conservative posture requires that distinction stay visible rather than collapsing to a green or red reading.)
- Gate F: unmeasured (No instrumentation exists in this detector pass for Gate F (reproducibility -- same frozen configuration (or same developmental recipe/constitution) across multiple seeds/runs/machines). This is reported as UNMEASURED, not FALSE: absence of evidence is not evidence of absence, and this detector's conservative posture requires that distinction stay visible rather than collapsing to a green or red reading.)

## Transition since the previous derived artifact

No prior artifact found -- this is the first run. Every predicate reads INITIAL.

## Gate A -- identifiable organism

Satisfied: False (tier: None)
- Scorable manifests: 2697 (with substrate_commit: 208, with substrate_hash: 375, with enabled_default_off_flags: 33)
- No exact-recurring-configuration group clears the threshold.
- Best substrate_hash (code-identity only) recurrence: 11 manifests across 11 distinct experiment types
- Equivalent-for-purpose tier: unmeasured

## Gate C -- coexistence (mechanisms exercised together)

- Manifests carrying any enabled_default_off_flags: 33 (33 with >=2 flags)
- Distinct flags observed: 99; pairs observed at least once: 2929 of 4851 possible (1922 never combined)

Top coexisting pairs:
- e3.goal_weight + heartbeat.breath_period: 33
- e3.goal_weight + goal.z_goal_enabled: 23
- goal.z_goal_enabled + heartbeat.breath_period: 23
- e3.goal_weight + latent.use_affective_harm_stream: 22
- e3.goal_weight + latent.use_harm_stream: 22
- heartbeat.breath_period + latent.use_affective_harm_stream: 22
- heartbeat.breath_period + latent.use_harm_stream: 22
- latent.use_affective_harm_stream + latent.use_harm_stream: 22
- e2.e2_action_contrastive_enabled + e2.e2_rollout_output_norm_clamp_enabled: 21
- e2.e2_action_contrastive_enabled + e3.goal_weight: 21

Caveat: The flag-bearing subset of the corpus is thin (a small fraction of the scorable manifests carry enabled_default_off_flags at all) and clustered -- a high pairwise coexistence rate among the flags that DO appear reflects a small number of 'many-flags-at-once' runs, not a broad, repeated demonstration that the listed mechanisms jointly produce non-degenerate behaviour across many independent trials. Read counts, not ratios.

## Gate B -- canonical-profile candidate substrate

Status: UNMEASURED
No instrumentation exists in this detector pass for Gate B (canonical-profile candidate substrate -- admission-doctrine criteria per evidence/planning/architecture_epoch_investigation.md section 9 (corpus enablement, cited-evidence-run check, non-degeneracy, known-interaction check)). This is reported as UNMEASURED, not FALSE: absence of evidence is not evidence of absence, and this detector's conservative posture requires that distinction stay visible rather than collapsing to a green or red reading.

## Gate D -- whole-organism non-degeneracy

Status: UNMEASURED
No instrumentation exists in this detector pass for Gate D (whole-organism non-degeneracy -- moves, observation variance, action collapse, candidate generation, no NaN dominance; couples to the GOV-CAPCONTRACT-1 capability/plasticity contract). This is reported as UNMEASURED, not FALSE: absence of evidence is not evidence of absence, and this detector's conservative posture requires that distinction stay visible rather than collapsing to a green or red reading.

## Gate E -- behavioural evidence

Status: UNMEASURED
No instrumentation exists in this detector pass for Gate E (behavioural evidence -- Behavioural Evidence Ladder rung attributable to a single identifiable organism). This is reported as UNMEASURED, not FALSE: absence of evidence is not evidence of absence, and this detector's conservative posture requires that distinction stay visible rather than collapsing to a green or red reading.

## Gate F -- reproducibility

Status: UNMEASURED
No instrumentation exists in this detector pass for Gate F (reproducibility -- same frozen configuration (or same developmental recipe/constitution) across multiple seeds/runs/machines). This is reported as UNMEASURED, not FALSE: absence of evidence is not evidence of absence, and this detector's conservative posture requires that distinction stay visible rather than collapsing to a green or red reading.

---
This artifact is produced by REE_assembly/scripts/generate_canonical_readiness.py, a read-only detector. It has no authority to admit a canonical profile member or declare a canonical version. See docs/claims/claims.yaml GOV-UMPIRE-1.
