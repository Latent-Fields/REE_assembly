# Failure Autopsy -- V3-EXQ-786 (MECH-163 dual-system recruitment)

- **Generated:** 2026-07-20T15:30:07Z
- **Session:** `malloc-stack-logging-explorer-a0e312`
- **Scope:** single run -- **flagged diagnostic** (`precondition_unmet`)
- **Status:** confirmed (user-gated 2026-07-20)
- **Machine-readable companion:** `failure_autopsy_V3-EXQ-786_2026-07-20.json`

---

## Headline

**The self-route `substrate_not_ready_requeue` mislabels the cause.** FamiliarityTracker is
present and working; it produced a novel-vs-familiar separation of **0.04937 against a 0.05
floor** -- short by 1.3%. That is a **manipulation-strength and power defect in the test design**,
not an immature substrate. This is the canonical V3-EXQ-642 pattern: a self-route that names
"substrate" for what is actually an experiment that could not deliver its own treatment.

Both halves of the defect were foreseeable at design time.

---

## 1. Facts

**Manifest:** `outcome: FAIL`, `evidence_direction: non_contributory`,
`interpretation.label: substrate_not_ready_requeue`, indexer flag **`precondition_unmet`**.

**Preconditions:**

| Precondition | Measured | Threshold | Met |
|---|---|---|---|
| `familiarity_separation` | **0.049365** | 0.05 | **false** |
| `candidate_score_range_non_degenerate` | 27.489 | 1e-06 | true |

**Load-bearing criterion:** `C1_recruitment_higher_on_novel`, `passed: false`, and
`criteria_non_degenerate: {C1: false}` -- so the null is uninterpretable as evidence about
MECH-163 regardless of its value.

**Robustness bar:** `mean - k*SEM > margin` with n=5, mean 0.013322, SEM 0.011687, k=1.0,
margin 0.05 -> lower bound 0.001635. Fails. The manifest itself stamps
`sample_size_improvable: true`.

**Per-seed recruitment deltas:** `[-0.01312, +0.02942, +0.02880, -0.02244, +0.04395]` -- three
positive, two negative, straddling zero.

**Recording provenance: COMPLETE.** `recording_schema`, `substrate_hash`
(`67c01b2d...`), `machine`, `machine_class` (`linux-x86_64-py3.10`), `elapsed_seconds` (5343.08),
full `config`, explicit `seeds`. No recording gap.

---

## 2. Why the self-route is wrong

`substrate_not_ready_requeue` asserts that the substrate cannot yet support the test. But the
substrate *did* what it was asked: FamiliarityTracker discriminated practiced from held-out
layouts and returned a separation **within 1.3% of the pre-registered floor**. A substrate that
misses its gate by 0.0006 is not absent, missing, or stubbed -- it is being asked to resolve a
contrast the experiment did not make large enough.

Two design-time causes, both visible in the committed `config`:

**(a) The novelty contrast is actively eroded during the practice phase.**
`env_drift_interval: 5` with `env_drift_prob: 0.1` runs throughout the 20
`practice_episodes_per_layout`. Drift is precisely the mechanism that decays familiarity, so the
design spends its practice budget building a familiarity signal against a process dismantling it.

**(b) "Novel" and "familiar" layouts are not structurally distinct enough.** The held-out seeds
(`novel_env_seeds: [2000, 2001, 2002]`) come from the same generator as the familiar ones
(`[1000, 1001, 1002]`) on a 10x10 grid with the same `num_hazards: 3` / `num_resources: 5`.
Different seeds from the same generator on a small grid yield structurally similar layouts, which
caps the achievable separation near the floor by construction.

**(c) The design is underpowered against its own pre-registered margin.** To clear
`mean - SEM > 0.05` at the observed SEM of 0.0117 requires a mean above **0.062** -- roughly
**4.7x** the observed 0.0133. At n=5 with per-seed deltas straddling zero, the margin was not
reachable by any plausible effect this design could produce. The margin appears to have been set
without a power calculation against a measured or estimated effect size.

---

## 3. Claim-layer mapping

`MECH-163` (`mechanism_hypothesis`, status `candidate`, `implementation_phase: v3`,
depends_on ARC-007 / ARC-021 / MECH-112 / SD-012 / INV-029 / ARC-071). Prior evidence: 9 lit
supports, **0 genuine experimental entries** -- this was to be the first V3 experimental evidence
on the dual-system distinction.

**The claim is not touched by this FAIL.** The manipulation check failed, so novel and familiar
were not established as real conditions, so C1's null carries no information about dual-system
recruitment. Recording this against MECH-163's confidence would demote the claim for an
experiment that never delivered its treatment.

Worth carrying forward alongside: the manifest's own `scope_note` states this tests **leg (1)
only** -- leg (2) long-horizon benefit accumulation is blocked by ARC-007 STRICT value-flat
proposals, leg (3) prosocial planning has no V3 substrate, and ARC-071 (planned->habit transfer)
is unbuilt. **Even a clean PASS here would not confirm MECH-163.** The claim's `v3_pending` hold
stands on its own terms irrespective of this run.

---

## 4. Biological-reference triage

- **Closest reference mechanism:** dual-process control -- goal-directed/model-based recruitment
  under novelty versus habitual/model-free control under familiarity; dorsomedial-to-dorsolateral
  striatal transfer with training.
- **Lit status: PRESENT** (`evidence/literature/targeted_review_connectome_mech_163`); the
  2026-05-10 targeted review already established ARC-071 as the missing transition mechanism
  MECH-163 presupposes. **No `/lit-pull` owed.**
- **Missing-dependency signature?** Not demonstrated here. The biology predicts the recruitment
  contrast scales with how genuinely novel the novel condition is -- which is exactly the quantity
  the manipulation check says was insufficient. The result is consistent with a working mechanism
  under too weak a contrast, and equally consistent with no mechanism. It does not discriminate.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | the claim was not tested under conditions where it could express itself |
| Biological reference | clear | lit present; dual-process control is well evidenced |
| Prerequisites | **partial** | ARC-071 unbuilt, ARC-007 STRICT blocks leg (2) -- but neither caused this FAIL |
| Implementation | **complete** | FamiliarityTracker present and discriminating, just below the gate |
| Environment | **too sparse** | same-generator seeds on a 10x10 grid cap layout novelty; drift erodes familiarity during practice |
| Measurement | **under-instrumented** | margin 0.05 set ~4.7x above the achievable effect; n=5 with SEM 0.0117 |
| Integration | isolated | leg (1) only by design |
| Scale | **likely insufficient** | `sample_size_improvable: true` at n=5 |

**Recommended `epistemic_category`: `measurement_test_design_defect`.
Recommended `evidence_direction`: `non_contributory`.**

The interpretable signal that keeps this from being merely non-contributory: **the achievable
familiarity separation under this env configuration is ~0.049**, which is a reusable design
constraint. Any successor must either raise that number or lower its floor with justification.

---

## 6. Learning extracted

1. **A manipulation check that fails by ~1% is a design finding, not a substrate finding.** The
   gap between "the substrate cannot do this" and "we did not ask hard enough" is the difference
   between an `/implement-substrate` route and a re-queue, and the self-route took the expensive
   branch.
2. **Environmental drift applied during a familiarisation phase works against the phase's
   purpose.** `env_drift_interval: 5` / `drift_prob: 0.1` over 20 practice episodes decays the
   very signal the design is accumulating. Check whether any always-on env process opposes a
   phase's objective before setting that phase's budget.
3. **Sampling "novel" layouts from the same generator as "familiar" ones caps the contrast by
   construction.** On a small grid with fixed object counts, a different seed is not a different
   layout in any sense the familiarity metric can register.
4. **Pre-register the margin against a power calculation, not an intuition.** A margin of 0.05
   with an achievable effect near 0.013 and SEM 0.0117 could not have been cleared at any outcome.
   One arithmetic step at design time (required mean = margin + SEM) would have caught it, exactly
   as the V3-EXQ-785 autopsy found for its own gate.
5. **Report the achievable value, not just the pass/fail.** `familiarity_separation = 0.049365`
   is the number a successor design needs; a bare "precondition unmet" would have discarded it.

---

## 7. Routing

**`/queue-experiment` -- V3-EXQ-786a, same scientific question, alphabetic suffix**
(user-confirmed 2026-07-20).

The question is unchanged, so this is a lettered iteration, not a new number. Required changes:

1. **Strengthen the manipulation.** Suppress or greatly lengthen `env_drift_interval` during the
   practice phase so familiarity can accumulate; and/or raise `practice_episodes_per_layout` above
   20.
2. **Make "novel" structurally novel.** Vary layout-generating parameters (grid size, hazard and
   resource counts, landmark configuration) between familiar and held-out layouts rather than
   varying the seed alone.
3. **Power the margin.** Either raise n above 5, or re-derive `divergence_margin` from a measured
   effect size. Record the power calculation in the queue entry so the gate is auditable before
   the run rather than after.
4. **Keep the manipulation check as a gating precondition** -- it worked exactly as intended here,
   catching an uninterpretable run before it could weigh against a claim.

**Explicitly NOT routed:**

- **No `/implement-substrate`.** FamiliarityTracker is present and discriminating. There is no
  substrate gap in this run's causal path. (ARC-071 and ARC-007 do block legs 2 and 3 of MECH-163,
  but they are unrelated to this FAIL and already tracked.)
- **No `/lit-pull`.** `targeted_review_connectome_mech_163` is on file.
- **No claim weighting.** `non_contributory`; MECH-163's `v3_pending` hold stands unchanged.

**Re-derive brake:** does not fire. This is the first autopsy on MECH-163 (0 prior targets,
0 `substrate_ceiling` hits).

### Draft `evidence_quality_note` for governance (do NOT apply from this skill)

> 2026-07-20 (failure autopsy, V3-EXQ-786): NON-CONTRIBUTORY -- the run's manipulation check
> failed, so novel and familiar were never established as distinct conditions and the load-bearing
> C1 is stamped `criteria_non_degenerate: false`. The manifest self-routed
> `substrate_not_ready_requeue`; the autopsy rejects that label. FamiliarityTracker is present and
> discriminating, returning a separation of 0.049365 against a 0.05 floor (short by 1.3%) -- a
> test-design defect, not substrate immaturity. Two design-time causes, both in the committed
> config: `env_drift_interval: 5` / `drift_prob: 0.1` erodes familiarity throughout the 20
> practice episodes, and "novel" layouts differ from "familiar" only by generator seed on a 10x10
> grid. The design was also underpowered against its own margin -- clearing `mean - SEM > 0.05` at
> the observed SEM of 0.0117 needs a mean of 0.062, ~4.7x the observed 0.0133, with
> `sample_size_improvable: true` at n=5. Routed to /queue-experiment as V3-EXQ-786a (same
> question) with a strengthened manipulation and a powered margin. This run must NOT weigh against
> MECH-163. Separately: per the run's own scope_note, this tests leg (1) only -- legs (2) and (3)
> remain blocked by ARC-007 STRICT and by the unbuilt ARC-071, so even a PASS would not confirm
> the full dual-system claim.

---

## 8. Ledger delta (Step 9b)

**None owed.** V3-EXQ-786 adjudicates no pre-registered hypothesis: MECH-163 has no question in
`hypothesis_space_registry.v1.json`, and the run discriminates nothing (the manipulation check
failed). Registering a leg now and immediately marking it unresolved would add a denominator entry
with no adjudicating evidence. Skipped cleanly per Step 9b.

---

*Adjudicated by session `malloc-stack-logging-explorer-a0e312`. Inputs: the V3-EXQ-786 manifest
(preconditions, robustness_bar, pre_registered, config, scope_note); `claims.yaml` MECH-163;
`evidence/literature/targeted_review_connectome_mech_163`; `pending_review.md` diagnostic
adjudication flag; `proposal_diagnostic_adjudication_gate_2026-06-06.md`.*
