# Failure Autopsy -- V3-EXQ-816c + V3-EXQ-822 (batch, 2 independent targets)

Generated: `2026-07-26T12:22:13Z` -- scope `batch`, status `confirmed`

**Scoping note.** The committed `pending_review.md` (generated `2026-07-26T00:09Z`) still lists 3 FAILs
(816, 817, 820) as pending -- all three are **already adjudicated** in
`failure_autopsy_816-820-policy-decomposition-cluster_2026-07-26` and
`failure_autopsy_batch-793a-817-819_2026-07-26`. The two genuinely un-adjudicated ran-to-completion
targets, which landed after the 00:09Z snapshot, are below. Scope was regenerated **read-only**: the
shared `REE_assembly` working tree carried an **active concurrent `/governance` regeneration** (1123
dirty derived files, `INDEX.md` mtime 11:31Z) that was **not disturbed** -- this artifact was written
and landed via a throwaway worktree off `origin/master`.

---

## Target 1 -- V3-EXQ-816c (passed diagnostic, `non_contributory`)

`v3_exq_816c_mech321_vs_pe_decoupling_comparator_20260726T105608Z_v3` -- bears on MECH-321 / ARC-070
(untagged diagnostic). Full recording core present (`substrate_hash`, seeds, config; machine ree-cloud-2).

### Facts
- **Outcome PASS, answerable.** All positive controls held: `vs_tracking_live=true` (worst-cell 3
  streams tracked, not the degenerate constant-1.0 fallback), `pe_control_ok=true`,
  `forward_pe_varies=true` (pe_var_best 8.6e-7 > 1e-9), `forward_pe_bounded=true` (0.0086 << 1000),
  `enough_paired_steps=1654 > 30`.
- **Answer-label** `vs_pe_decoupled_proxy_saturation`: `decoupled=true`, `not_saturated=false`,
  `vs_heterogeneous=false`. region-V_s is flat (`region_vs_min_over_cells 0.934`, `var_best 0.00027`,
  `total_low_vs_steps 0`) and statistically decoupled from forward-PE
  (`spearman_unc_vs_pe_mean_over_cells 0.083`), while `pe_heterogeneous=true`.

### Diagnosis (four-layer)
The dominant layer is **measurement**: region-V_s (a latent-stability proxy) **saturates** near 1.0 in
the trained encoder and is **decoupled** from forward-model prediction error. So the R1 "V_s-drop"
decomposition trigger **cannot fire via this proxy in a competent agent**. Positive controls confirm
this is a real reading, not the degenerate fallback. Biological reference: uncertainty signals that
gate option boundaries retain dynamic range once a policy is learned; the REE proxy does not -- a
**proxy-design divergence**, not a claim divergence.

### Role in the fanout
816c is the **measurement-axis leg** of the pre-registered fanout question
`policy_decomposition_discrimination` (frozen 4), opened by the 816-820 cluster autopsy. It bears on
hypothesis **`H-vs-proxy-saturation`**. The **environment-axis sibling 816b is claimed/running** and
tests whether a harsher env can drive region-V_s into a low band.

### Adjudication (user, 2026-07-26): **leave the leg alive pending 816b**
Record 816c as a resolving run with basis, but **do not flip** `H-vs-proxy-saturation` to eliminated/
confirmed. Rationale: if 816b shows env can create low-V_s regions, the proxy could still be usable, so
816c *narrows* but does not meet the elimination bar. The registry update (Mode B narrow, state
unchanged) is deferred to the next `/governance` walk via `hypothesis_space_ledger_pending` (registry
write held back to avoid contending with the active governance regen).

**Routing: governance (derive-only).** No re-queue of 816c. The campaign's next move is decided by
816b, not 816c.

---

## Target 2 -- V3-EXQ-822 (SD-078 evidence, self-route `substrate_not_ready_requeue`)

`v3_exq_822_sd078_rule_selection_consumer_20260726T112152Z_v3` -- claim SD-078. ~3.6h on the hub
(ree-worker-1). Full recording core.

### Facts
- **3 of 4 readiness gates PASS**: cone present (`zworld_common_mode_cone` 0.963 > 0.9), ON pool
  differentiated (3.0 > 2.0), rule active P2 (0.882 > 0.1).
- **Gate (d) `propagation_non_vacuity` FAILS**: `on_prop_delta_mean` = `off_prop_delta_mean` =
  **exactly 0.0** (`readiness_prop_nonvac=false`).
- The rule-attributable **state** signal is present and clean: `on_rule_state_diff_mean 0.644` vs
  `off 0.0`, `frac_c1_rule_state_diff 1.0`, `c1_pass=true`; the ON pool activates (`on_max_live 16` vs
  `off 1`).

### Diagnosis (four-layer)
Dominant layers are **prerequisites / implementation / integration**: the SD-078 rule-selection cue
geometry is landed and validated (V3-EXQ-806 PASS) and the rule pool **differentiates and activates**,
but the **downstream consumer** -- the trained bias-head mapping `rule_state -> action bias` -- is
**not wired/trained**, so propagation is a structural zero on both arms. The **measurement is
adequate**: 0.0 is a real measured zero (not the best-effort `None`-on-failure fallback), and the same
instrument returns nonzero for `rule_state` (0.644) -- so this is a **substrate gap, not a
measurement/recording artefact** (user-confirmed 2026-07-26). Biological reference is a match:
corticostriatal rule-to-action mapping is inert without a trained read-out; a differentiated rule
representation with no consumer is behaviourally silent. The FAIL is a **discovered prerequisite**,
consistent with the mechanism -- **non-contributory for SD-078, does not weaken it**.

### Adjudication (user, 2026-07-26): **substrate gap -> implement-substrate**
The self-route `substrate_not_ready_requeue` is **correct** -- precondition genuinely unmet.

- **Routing: `/implement-substrate`.** Create a `substrate_queue.json` entry (`action: create`):
  *"Trained bias-head consumer coupling differentiated rule_state to an action bias (SD-078
  propagation consumer)"*, `unblocks_claims: [SD-078]`, `priority 2`,
  `depends_on: [SD-008, SD-066, SD-077, ARC-063]`.
- **`pending_retest_after_substrate: true`** -- once the consumer is trained, re-queue V3-EXQ-822 under
  an alphabetic suffix (same question). **Do not re-queue blind** before the consumer exists.
- **Re-derive brake: does not fire** -- first substrate-not-ready autopsy for SD-078, and category
  `precondition_unmet` (not `substrate_ceiling`) does not count under R3.

---

## Draft `evidence_quality_note`s for governance (do not apply here)

See the `recommended_evidence_quality_note` fields in the companion JSON -- exact text for governance to
write for 816c (measurement-saturation, non_contributory, ledger leg alive) and SD-078 (precondition
unmet, non_contributory, pending retest, substrate_queue create).

## Learning extracted
- **region-V_s saturates in a trained encoder and is decoupled from forward-PE** (spearman 0.083) --
  the R1 V_s-drop discrimination cannot be instrumented off this proxy; a non-saturating readout, or a
  low-V_s env (816b), is required.
- **A differentiated selection substrate is behaviourally silent without a paired trained consumer**
  read-out (rule_state -> action bias). SD-078 selection is landed; its consumer is the next build.
- Positive-control design and the 0.0-vs-None distinction both worked as intended -- the two self-routes
  are trustworthy, not artefacts.
