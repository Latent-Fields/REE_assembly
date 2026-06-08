# Failure Autopsy -- V3-EXQ-610f (INV-074 crystallization necessity)

- **Generated (UTC):** 2026-06-08T07:20:06Z
- **Scope:** single
- **Status:** confirmed (user adjudicated 2026-06-08)
- **Run:** v3_exq_610f_inv074_crystallization_necessity_20260608T051516Z_v3
- **Queue:** V3-EXQ-610f (supersedes V3-EXQ-610e); backlog EVB-0270
- **Outcome:** FAIL; manifest evidence_direction=unknown (all 5 claims)
- **Claims tagged:** INV-074, MECH-333, MECH-334, MECH-341, MECH-313
- **Purpose:** evidence
- **Lineage:** 543h/i/k/l + 610a-d (harness no-op, RESOLVED) -> 610e (first behaviourally-live; FAIL d2_control_shows_collapse=FALSE, ARM_0 confounded by always-on diversity stack) -> 610f (ARM_0 stripped to a TRUE NEGATIVE)

## Thesis

The 6th iteration of the INV-074 crystallization-necessity test. 610f did exactly what the
610e autopsy prescribed -- stripped EVERY always-on diversity floor (MECH-313 noise floor,
MECH-341 E3 score-diversity, phase-3 entropy bonus, MECH-260 dACC anti-recency, structured
curiosity) so crystallization (ARM_1 EWC) would be the SOLE phase-3 diversity-preserving
mechanism -- and the true-negative control **still did not collapse**. The pre-registered
necessity premise (collapse-WITHOUT-crystallization) was never instantiated, so the
discrimination criterion (D1, crystallization-preserves) cannot be read. This is a clean
interpretation-grid **branch (ii)** self-route: D2 FAIL while D3 holds.

The self-route is **trustworthy** here (not a V3-EXQ-642-style vacuous/precondition mislabel):
the wiring fixes are independently verified by the manifest `fix_verification` block
(policy genuinely trained, expansion stepped, EWC penalty 283-803 in loss), and D3 sanity
PASSes (the policy reached phase-3 entry with genuine action diversity). The unmet
precondition (D2 control collapse) is a real SCIENTIFIC precondition -- the phenomenon under
test -- correctly identified, not an untrained-substrate artifact.

## Facts (no interpretation)

`fix_verification`: fix1_policy_trained=true (init_entropy 0.410 -> trained 0.491, out of the
untrained 1.04+ band), fix2_expansion_stepped=true (1249 expansion params), fix3_ewc_penalty_in_loss=true
(penalty 0.268, residue grad 1.07). So this is NOT the harness-no-op lineage.

Acceptance:

| Criterion | Rule | Result | Read |
|---|---|---|---|
| **D2** true-negative control collapses | ARM_0.end_p2 - end_p3 >= +0.10 | **FAIL** delta **-0.012** | control entropy slightly ROSE p2->p3; never collapsed |
| **D1** crystallization preserves diversity | ARM_1.end_p3 - ARM_0.end_p3 >= +0.10 | FAIL delta -0.002 | nothing to preserve -> unreadable |
| **D3** both diverse at phase-2 peak | ARM_0.end_p2 > 0.4 AND ARM_1.end_p2 > 0.4 | **PASS** | non-vacuous; policy diverse at phase-3 entry |
| **D4** MECH-341/313 floor preserves diversity | ARM_4.end_p3 - ARM_0.end_p3 >= +0.10 | FAIL delta 0.0 | only interpretable when D2 PASS |

Threshold map (control collapse delta, end_p2 - end_p3): ARM_0 (eb=0.0) -0.0124; ARM_2
(eb=0.005) -0.0116; ARM_3 (eb=0.02) -0.0105. **No entropy floor was load-bearing** -- the
stripped REINFORCE control does not collapse regardless of the phase-3 entropy weight.

Per-seed phase-2 entropy varies (seed42 1.34 / seed43 0.62 / seed44 1.13) but within each
seed phase-2 ~= phase-3 across ALL five arms (ARM_0/1/2/3/4). EWC anchored (ewc_penalty_last
283-803 on ARM_1) but produced no measurable entropy difference vs ARM_0 because there was
no collapse to resist.

## Claim-layer mapping

| Claim | Type | Status | epistemic_category | Read |
|---|---|---|---|---|
| INV-074 | invariant (universal) | candidate | **substrate_ceiling** | plasticity crystallization necessity; biology-faithful (OD critical period, lit_conf 0.82). NOT weakened. |
| MECH-333 | mechanism | candidate (v3, v3_pending) | (inferred) | plasticity-injection open-phase channel. unknown. |
| MECH-334 | mechanism | candidate (v3, v3_pending) | **substrate_ceiling** | EWC residue write-protect. unknown. |
| MECH-341 | mechanism | candidate (v3, v3_pending) | (inferred) | E3 score-diversity floor (D4). unknown. |
| MECH-313 | mechanism | candidate_substrate_landed (v3_pending) | **substrate_ceiling** | LC-NE noise floor (D4). unknown. |

INV-074, MECH-334 and MECH-313 **already carry `epistemic_category: substrate_ceiling`** --
governance has already recognised these as V3-tractable-in-principle but substrate-too-coarse.
A FAIL here does NOT and must NOT weaken a universal invariant grounded in a working
biological existence proof. Per grid (ii): {INV-074, MECH-334, MECH-333} = unknown; per
grid (v): D4 FAIL with D2 FAIL leaves {MECH-341, MECH-313} = unknown. All five non_contributory.

## Biological-reference triage

Closest mechanism: ocular-dominance critical-period crystallization (Hensch 2005) +
plasticity injection (Nikishin 2023 NeurIPS, MECH-333) + EWC write-protect (Kirkpatrick 2017,
MECH-334). Biology CLEARLY supports the mechanism class -- crystallization of plasticity is a
real, necessary property of developing cortex. This is NOT a formal-definition import; lit
entry exists (lit_conf 0.82). The failure resembles "the destabilising pressure was never
strong enough to force the catastrophic-forgetting collapse the necessity premise requires"
-- a missing environmental-pressure DEPENDENCY, not a wrong mechanism. By the autopsy core
principle, demotion is off the table: tested-fairly is NOT satisfied (the test could not let
the claim express).

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | test could not let the claim express (D2 precondition unmet) |
| Biological reference | clear | OD critical period; plasticity injection; EWC; lit_conf 0.82 |
| Prerequisites | missing | a phase-3 regime that actually induces collapse-without-crystallization |
| Implementation | complete | fix_verification: policy trained, expansion stepped, EWC in loss |
| Environment | **wrong pressure** | IGW-023 noise (SD-047 multi-source + SD-048 interoceptive + accelerated drift) does NOT instantiate the necessity premise; threshold map shows no floor load-bearing |
| Measurement | adequate | selected_action_entropy non-degenerate; D3 sanity PASS |
| Integration | fine | arms isolate cleanly |
| Scale / capacity | likely insufficient at test-design level | stripped REINFORCE-on-grid does not collapse under added noise |

Dominant locus: **environment / test-design**. Recommended experiment-level
`recommended_epistemic_category: substrate_ceiling` (consistent with the claims' existing
tags): the V3 substrate as currently exercised cannot deliver the collapse distinction.

## The load-bearing signal

This is the **6th iteration**, and the threshold map establishes the convergent finding:
**no entropy floor is load-bearing and the stripped REINFORCE control never collapses under
added noise.** Two readings:

(a) *escalate-pressure / test-design*: a STRONGER phase-3 destabilising regime -- specifically
a genuine task-distribution SHIFT whose new optimum CONFLICTS with the phase-0-2 policy (not
just added noise) -- would force the overwriting that crystallization is meant to resist, and
D1 would then become readable.

(b) *substrate-incapacity / substrate-ceiling*: the V3 REINFORCE-on-grid substrate cannot
exhibit catastrophic plasticity collapse at all; INV-074's V3-applicability is genuinely
blocked and the claim should rest on its biological grounding + existing substrate_ceiling
status, with the 610 necessity-test cascade stopped.

**User adjudication 2026-06-08: route (a) -- ONE redesign with a TRUE task-shift.** The
distinction the threshold map implies (noise != catastrophic-forgetting pressure) is exactly
what a task-shift tests. The redesign is decisive either way: if a genuine conflicting-task
phase-3 ALSO fails to collapse the stripped control, that confirms reading (b) and the cascade
stops with evidence rather than assumption.

## Learning extracted

1. Adding observation/interoceptive NOISE (IGW-023: SD-047 + SD-048 + drift) is not the same
   destabilising pressure as a task-distribution SHIFT. INV-074's necessity premise requires
   the latter: a phase-3 whose optimal policy CONFLICTS with phases 0-2, forcing overwriting.
2. Six iterations have converged on "no entropy floor is load-bearing / control never
   collapses under noise" -- a structural property of the test design, not tuning noise.
3. The 610f wiring is verified-live (fix_verification) -- the FAIL is genuinely informative
   about the test design, distinct from the 543h/610a-d harness-no-op lineage.
4. INV-074 as a universal invariant with a working biological existence proof cannot be
   weakened by a test that could not instantiate its premise; non_contributory is the correct
   disposition, pending the task-shift retest.

## Routing decision (user-confirmed)

**/queue-experiment** -- ONE redesign successor (new EXQ; a different scientific approach to
instantiating collapse, not an alphabetic noise-escalation). Redesign spec:

- Replace the IGW-023 noise-only phase-3 with a genuine **task-distribution shift**: a phase-3
  environment whose reward/optimal-policy structure CONFLICTS with phases 0-2 (e.g. a
  resource/hazard layout or contingency reversal whose optimal first-action distribution is
  incompatible with the phase-0-2 policy), so the un-crystallized control suffers genuine
  catastrophic forgetting (entropy collapse onto the new single regime) while the EWC-anchored
  arm resists.
- Keep the 610f arm structure (ARM_0 stripped true-negative / ARM_1 stripped+crystallize /
  ARM_4 floor-on-control) and the verified wiring (policy trained, expansion stepped, EWC in
  loss); keep D3 as the non-vacuity sanity gate.
- Pre-register that D2 now reads collapse on the SHIFTED task. Acceptance unchanged
  (D1 AND D2 AND D3). If D2 STILL fails on a genuine task-shift, that is the decisive
  substrate-incapacity finding -> accept INV-074 substrate_ceiling and STOP the cascade.
- supersedes V3-EXQ-610f. claim_ids re-evaluated from scratch per the redesign (the
  necessity test still tags INV-074/MECH-333/MECH-334; D4 floor-contrast still tags
  MECH-341/MECH-313).

## Draft evidence_quality_note (governance applies; do not write here)

- **INV-074 / MECH-333 / MECH-334 (610f):** "V3-EXQ-610f (6th necessity-test iteration; ARM_0
  stripped to a true negative) re-FAILed D2: the stripped REINFORCE control did NOT collapse
  its action entropy under the IGW-023 phase-3 noise regime (delta -0.012; threshold map
  ARM_0/2/3 all -0.010 to -0.012, no entropy floor load-bearing), so the necessity premise
  (collapse-without-crystallization) was never instantiated and D1 is unreadable. Wiring
  verified-live (policy trained, expansion stepped, EWC penalty 283-803 in loss) and D3 sanity
  PASS, so this is a genuine test-design finding, not a harness no-op. INV-074 NOT weakened
  (universal invariant; OD critical-period existence proof; lit_conf 0.82). non_contributory;
  pending_retest_after_redesign (V3-EXQ task-shift successor replacing noise-only phase-3 with
  a conflicting task-distribution shift). User adjudication 2026-06-08: noise != catastrophic-
  forgetting pressure; route one task-shift redesign, decisive for the substrate-incapacity
  reading either way."
- **MECH-341 / MECH-313 (610f, D4 floor-contrast):** "V3-EXQ-610f D4 (floor preserves
  diversity) is uninterpretable because D2 (control collapse) FAILed -- D4 is only readable
  when ARM_0 actually collapses. non_contributory; not weakened; carried to the task-shift
  redesign successor."

## Notes

Shape-similarity to the 2026-06-07 603g/624c/651a cluster (negative-control/precondition fails
-> discrimination unreadable) is the generic substrate-ceiling fingerprint, but the SUBSTRATE
is unrelated (that cluster is goal-pipeline foraging-competence; this is plasticity-collapse
environment pressure). Treated as SINGLE scope; the 610 lineage is the relevant history.
