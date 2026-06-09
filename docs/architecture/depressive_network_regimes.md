# Depressive Network Regimes and Repair

Status: anchor doc for the clinical-depression intake claims (RA-001, MECH-367, Q-061).
Registered: 2026-06-09. Off the V3 / GAP-7 critical path (V4/V5 + out-of-domain).
Source intake: [evidence/planning/thought_intake_2026-06-06_clinical_depression_network_connectivity_reversal.md](../../evidence/planning/thought_intake_2026-06-06_clinical_depression_network_connectivity_reversal.md)
Raw thought: [docs/thoughts/2026-06-06_clinical_depression_network_connectivity_reversal.md](../thoughts/2026-06-06_clinical_depression_network_connectivity_reversal.md)

**Terminology guardrail (load-bearing):** "long-term depression" throughout this doc means
**long-term CLINICAL depressive illness**, NOT synaptic long-term depression (LTD).

This doc holds the three claims reaped from the 2026-06-06 clinical-depression thought intake.
It is an anchor/compass doc, not a substrate design: none of these is a V3 implementation target.

---

## ra-001

**Claim (research_anchor, out_of_domain):** Long-term clinical depression involves a
**chronicity-dependent reversal of large-scale network coupling**. Past a ~24-month chronicity
threshold, the relationship between symptom severity and Central-Executive-Network (CEN) <->
Default-Mode-Network (DMN, precuneus) functional connectivity reverses sign:

- **Non-chronic:** stronger CEN-DMN coupling at low severity, weaker at high severity.
- **Chronic:** connectivity *strengthens* as symptoms worsen, co-occurring with entrenched rumination.

The depressive brain-state is **duration-indexed**, not a single static regime.

**Status of the source.** Verified at the press-summary level (Neuroscience News,
[Long-Term Depression Reverses Brain Network Connectivity](https://neurosciencenews.com/brain-network-connectivity-mdd-30745/)).
The underlying peer-reviewed publication was **not** located at registration; treat the
24-month threshold and precuneus locus as press-reported, not paper-verified.

**Precision on "reverses".** This is a *cross-sectional* reversal of the
connectivity-vs-severity relationship between non-chronic and chronic cohorts. It is **not** a
demonstration of *therapeutic* reversibility (that is the open question Q-061).

**Why out_of_domain.** The test domain is a clinical fMRI cohort; no REE substrate at any level
distinguishes named large-scale networks (CEN/DMN). Registered as a `research_anchor` (the
`RA-` prefix; claim_type sanctioned by [v4_spec.md](v4_spec.md) "Out-of-domain claims ... belong
as research_anchor / literature_synthesis claim types"). It **grounds** the existing REE
depression cluster (MECH-088, INV-034, MECH-124, Q-021, MECH-082/086) and motivates MECH-367 and
Q-061. It contradicts nothing in the registry.

---

## mech-367

**Claim (mechanism_hypothesis, substrate_conditional, V4/V5):** The depressive failure mode is
carried by a **multi-axis network-regime vector**, not a scalar low-mood / low-reward value:

```text
depressive_regime_risk = f(future_trajectory_access,
                           goal_stream_coupling,
                           residue_load / self_weighting,
                           rumination_loop_gain,
                           action_threshold / energy_budget,
                           social_affordance_access,
                           offline_repair_quality)
```

The depressive state is defined by the **joint configuration** of these coupling/access axes and
is self-maintaining; a scalar mood/reward value is an insufficient representation.

**What is new vs what REE already owns.** REE already owns each axis individually:

| Axis | Existing REE owner |
|---|---|
| future_trajectory_access | INV-034; MECH-082 / MECH-086 (locked-in avoidant brain) |
| goal_stream_coupling | INV-034 (depressive attractor = goal-maintenance failure, EXQ-237a) |
| residue_load / self_weighting | MECH-124 (residue-field harm dominance) |
| rumination_loop_gain | MECH-124 (self-amplifying replay loop) |
| action_threshold / energy_budget | Q-021 (pure-avoidance behavioural flatness / anhedonia) |
| social_affordance_access | (scattered; nearest: social-coupling salience) |
| offline_repair_quality | MECH-124 / MECH-123 (consolidation can deepen or repair) |

What is **new** is the **composition** into one weighted vulnerability vector whose joint
configuration *is* the regime. The empirical anchor RA-001 (duration-dependent coupling reversal)
motivates treating the regime as a coupling-structure vector rather than a scalar.

**Why substrate_conditional / V4.** The axes exist piecemeal in V3 but the joint-vector read-out
is not built, and there is no named large-scale-network coupling substrate. Off the V3 / GAP-7
critical path. **Do not build in V3** until routed by experiment.

**Failure-mode precision (do not blur).** Keep the depression failure mode distinct from:

- **Psychosis** = NA collapse of E1/E2 constraint + DA aberrant salience on noisy input
  (MECH-088 psychosis profile; tag-MISassignment MECH-094/MECH-115).
- **Confabulation** = tag-LOSS / simulation-real source-monitoring failure (MECH-094).

"Rumination" here is the depressive recurrent-loop sense (MECH-124), not psychotic
content-intrusion.

---

## q-061

**Question (open_question, answer_state):** Is a maladaptive depressive network-regime
(MECH-367) **reversible** -- reconfigurable by REE's existing repair machinery (offline
integration / MECH-124 replay rebalancing, decommitment from ruminative loops, re-access to
social affordances, goal-stream re-coupling) -- or does **chronicity lock** the regime past a
threshold (RA-001) such that the repair routes that work early fail or reverse-sign late?

The sharp sub-question is **duration-dependence**: do the offline-integration / decommitment /
social-re-access routes that reconfigure an *early* depressive regime still work *late*, or does
the MECH-124 self-amplifying consolidation loop plus the RA-001 coupling reversal make late
repair require a different mechanism?

**Status.** A question, not an assertion. Resolvable in REE only once the MECH-367 vector
substrate exists (V4/V5). Off the V3 critical path -- do not queue a V3 experiment against it.
Hold the anti-overclaim guard: do **not** assert that depression is "merely a reversible software
state."

---

## Not registered here

- **Candidate D** -- the depression-analogue *AI* cognitive-failure mode (persistent low
  action-initiation despite available goals; negative-evaluation loops; future-trajectory
  suppression; excessive failure-generalisation) -- belongs in the cross-repo
  `Latent-Fields/ai-cognitive-failure-taxonomy`, **not** in `claims.yaml`, and is handled with
  explicit anti-anthropomorphic guardrails (the analogue is a network-state failure in trajectory
  generation and action readiness, NOT mood/sadness). The REE `EXT-` series (LLM external failure
  modes) is the in-registry sibling pattern, should that taxonomy ever fold back.
