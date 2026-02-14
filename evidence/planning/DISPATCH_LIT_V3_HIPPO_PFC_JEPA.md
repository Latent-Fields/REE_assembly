# Dispatch: v3-Critical Literature Program (Hippocampal + PFC + JEPA Mapping)

Generated: `2026-02-14`
Purpose: gather targeted literature evidence to constrain v3 control-completion design.

## Program Targets

1. Hippocampal function:
- replay as planning compute,
- map update after action outcome,
- model-based rollout and trajectory evaluation.

2. Prefrontal/control function:
- arbitration and conflict resolution,
- commitment gating and switching,
- rule/context control under uncertainty.

3. JEPA mapping constraints:
- what latent representations can support directly,
- what must remain external control-plane logic.

---

## Copy/Paste Prompt (REE_assembly)

```md
You are Codex in `REE_assembly`.

Goal: execute a focused literature review program to constrain v3 architecture around hippocampal functions, prefrontal control, and JEPA-to-REE mapping limits.

Create these literature lanes:
- `evidence/literature/targeted_review_v3_hippocampal_rollout/`
- `evidence/literature/targeted_review_v3_prefrontal_control/`
- `evidence/literature/targeted_review_v3_jepa_mapping_limits/`

Minimum output:
- At least 2 entries per lane (6 total).
- Each entry must include:
  - `record.json`
  - `summary.md`
- Required record fields:
  - `claim_ids_tested`
  - `evidence_class`
  - `evidence_direction`
  - `confidence`
  - `confidence_rationale`

Claim linkage guidance:
- hippocampal lane should link primarily to:
  - `ARC-007`, `ARC-018`, `MECH-033`, `MECH-056`, `MECH-060`
- prefrontal/control lane should link primarily to:
  - `ARC-005`, `ARC-003`, `MECH-046`, `MECH-053`, `MECH-060`
- JEPA mapping-limits lane should link primarily to:
  - `IMPL-022`, `MECH-057`, `MECH-058`, `MECH-059`, `Q-013`, `Q-014`

Source quality requirements:
- Prefer primary sources (peer-reviewed or canonical preprints/code docs where applicable).
- Explicitly state mapping caveats and uncertainty in `summary.md`.
- Avoid over-claiming direct equivalence to REE modules.

After adding entries:
1) Run:
   - `python3 evidence/experiments/scripts/build_experiment_indexes.py`
2) Summarize:
   - confidence/direction updates for linked claims,
   - whether any open questions can be narrowed,
   - proposed follow-up experiment dispatches to `ree-v1-minimal` vs `ree-experiments-lab`.

Constraints:
- Keep changes scoped to literature evidence + generated indexes.
- Do not refactor unrelated architecture docs in this pass.
```

---

## Expected Decision Impact

- Reduces ambiguity around hippocampal vs control-plane ownership in v3.
- Tightens what JEPA substrate can reasonably provide versus what v3 must add explicitly.
- Converts broad design debate into claim-linked evidence with explicit confidence.
