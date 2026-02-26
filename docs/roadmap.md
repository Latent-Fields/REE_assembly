# Roadmap

**Claim Type:** implementation_note  
**Scope:** Program phases, repository roles, and phase-gate criteria  
**Depends On:** IMPL-020, IMPL-021, IMPL-022, MECH-057, MECH-058, MECH-059, MECH-060  
**Status:** candidate  
**Claim ID:** IMPL-008
<a id="impl-008"></a>

---

## Status Snapshot (2026-02-23)

- `REE_assembly` is now the canonical governance + specification repo.
- `ree-v1-minimal` is serving as a qualification harness (controlled mechanism comparisons).
- `ree-experiments-lab` is serving as a stress/falsification harness (adversarial and non-stationary checks).
- JEPA integration guidance is now convergence-first: source-method details live in `REE_convergence`, while
  `REE_assembly` keeps REE-first canonical contracts and adjudication outputs.
- JEPA remains an external reference project; REE uses JEPA-like representational patterns for comparison/inspiration only.

---

## Phase Definitions

## REE-v1 (completed purpose: qualification baseline)

Primary role:
- validate whether proposed mechanisms produce expected directional effects under controlled conditions.

Outcome:
- useful for signal discovery and contract hardening,
- not sufficient as final architecture target due to stress-lane conflicts and limited environment breadth.

## REE-v2 (current focus: REE-first representation-interface contract with JEPA-like mappings)

Primary role:
- lock a stable representation-interface contract for sensing adapters + E1/E2 latent prediction.

In-scope:
- sensor adapters mapped to JEPA-like context/target latent interfaces,
- E1/E2 representation-reference integration contract implementation (`IMPL-022`),
- stable output streams for latent prediction error and uncertainty,
- run-pack/adapter-signal compliance and calibration metrics.

Out-of-scope:
- full control-plane completion,
- final hippocampal/E3 commitment architecture,
- full ethical arbitration dynamics.

Exit criteria to start v3 implementation focus:
- representation-interface contract stable across both qualification and stress lanes,
- uncertainty/error streams are calibrated and non-gamed across shifts,
- no unresolved adapter contract drift.

## REE-v3 (next focus: control completion)

Primary role:
- add and iterate control-plane, hippocampal functions, and E3 commitment/accountability on top of the v2 representation interface foundation.

In-scope:
- control-plane arbitration and precision routing,
- hippocampal rollout generation + post-commit map/model updates,
- pre-commit vs post-commit error-channel separation and accountability hooks,
- commitment gating and conflict-resolution policies.

Exit criteria to start v4:
- robust separation of exploratory simulation vs committed learning,
- stable behavior under adversarial trajectory pressure,
- governance confidence above provisional thresholds for core control claims.

## REE-v4 (later: social + institutional complexity)

Primary role:
- scale to richer multi-agent coupling, language-mediated coordination, and institutional constraints.

---

## Repository Roles

- `REE_assembly`:
  - canonical claims, architecture docs, evidence matrix, governance outputs.
- `ree-v2`:
  - primary qualification lane for v2 representation-interface profiles and acceptance gates.
- `ree-experiments-lab`:
  - stress/adversarial/replication experiments and falsification pressure.
- `ree-v1-minimal`:
  - legacy baseline/reference harness and parity backstop during v2 migration.

Current recommendation:
- keep `v2` spec and contract refinement in `REE_assembly`,
- keep source-specific JEPA integration playbooks in `REE_convergence` and promote only adjudicated deltas,
- bootstrap `ree-v2` now and use it as the qualification lane,
- keep `ree-v1-minimal` for transitional parity checks until `ree-v2` coverage is complete.

---

## Immediate Work Queue (This Cycle)

1. Enforce REE-first canonical wording in `REE_assembly` while preserving JEPA-like interface translations.
2. Keep JEPA source-method integration details in `REE_convergence/sources/jepa/*` and promote only packet-backed deltas.
3. Produce first-pass v2 implementation spec (subsystem boundaries + required metrics + failure gates).
4. Run targeted literature program for v3-critical systems:
   - hippocampal replay/planning/map-update mechanisms,
   - prefrontal control/arbitration/commitment mechanisms,
   - JEPA-like latent-to-hippocampal mapping constraints.
5. Route resulting evidence into backlog/proposals and governance decisions.

---

## Open Questions

- Should v2 be incubated in-place (`REE_assembly` + external experimental repos) or split into a dedicated implementation repo now?
- What minimum evidence threshold should trigger promotion of `MECH-058/059/060` from candidate to provisional?

## Related Claims (IDs)

- IMPL-008
- IMPL-020
- IMPL-021
- IMPL-022
- MECH-057
- MECH-058
- MECH-059
- MECH-060

## References / Source Fragments

- `docs/architecture/jepa_ree_hybrid_diagram_spec.md`
- `docs/architecture/jepa_e1e2_integration_contract.md`
- `evidence/experiments/claim_evidence.v1.json`
- `evidence/experiments/promotion_demotion_recommendations.md`
