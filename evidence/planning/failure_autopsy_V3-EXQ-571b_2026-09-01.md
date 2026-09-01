# Failure autopsy -- V3-EXQ-571b (MECH-439 clamped E3 variance-monopoly presence audit)

- **Generated (UTC):** 2026-09-01T06:44:22Z
- **Scope:** single
- **Status:** confirmed (Step 8 gate held 2026-09-01, user present)
- **Run:** `v3_exq_571b_e3_variance_monopoly_presence_clamped_20260901T061141Z_v3`
- **Outcome:** PASS -- `experiment_purpose: diagnostic`, `claim_ids: ["MECH-439"]`
- **Self-route label:** `f_monopoly_present_clamped_occupant_shifted` -- **upheld, with a scope restriction the label does not carry**
- **Dry-run gate:** checked, `dry_run: false`; 0 dry runs cited or excluded.

This is a diagnostic PASS with no `adjudication` flag. It is autopsied because ALL
`experiment_purpose: diagnostic` results require a confirmed adjudication before governance
acts on them -- "cleared its own preconditions" is exactly what a vacuous pass also shows.

## 1. Facts

Four arms x four seeds. `A1_baseline_clamp_on` is the verdict-bearing arm. Criteria:
**C1 PASS (load-bearing), C2 PASS, C3 PASS.**

| arm / seed | committed total var | top channel | top share | f_weighted | harm_weighted | residue |
|---|---|---|---|---|---|---|
| A0 clamp_off / 42 | 11.55 | f_weighted | 0.9993 | 0.9993 | 0.0007 | ~0 |
| A0 clamp_off / 123 | 7.53 | f_weighted | 0.9926 | 0.9926 | 0.0074 | ~0 |
| A0 clamp_off / 456 | 128.59 | f_weighted | 1.0000 | 1.0000 | ~0 | ~0 |
| A0 clamp_off / 43 | 61.16 | f_weighted | 1.0000 | 1.0000 | ~0 | ~0 |
| **A1 clamp_on / 42** | 3.63e-04 | harm_weighted | 0.9953 | 0.0011 | 0.9953 | 0.0037 |
| **A1 clamp_on / 123** | 1.55e-05 | harm_weighted | 0.9368 | 0.0556 | 0.9368 | 0.0076 |
| **A1 clamp_on / 456** | 1.76e-05 | harm_weighted | 0.9879 | 0.0107 | 0.9879 | 0.0013 |
| **A1 clamp_on / 43** | 3.45e-05 | harm_weighted | 0.9683 | 0.0083 | 0.9683 | 0.0235 |

`F_COMPONENTS = ("f_weighted", "harm_weighted")` (driver:208), so both occupants are F
channels and the occupant shift is **within F**, as the run states. The shift is near-total
and unanimous: `f_weighted` 0.9926-1.0000 -> 0.0011-0.0556, `harm_weighted` ~0 -> 0.9368-0.9953,
4/4 seeds.

Recording provenance: always-core complete (`rec/v1`, `substrate_hash fb695aef...`, seeds,
config, `elapsed_seconds 2750.6`). No recording gap.

## 2. Two attacks raised against this run and WITHDRAWN

Recorded rather than deleted, because each was tested and did not hold.

**(a) "9 of 16 cells report a variance share > 1.0, so the decomposition is not a valid
partition."** WITHDRAWN. `pool_share_exceeds_unity` flags the **legacy V3-EXQ-571 pool
method**, a covariance-retained statistic that can legitimately exceed 1.0 and is recorded
only to make the historical 0.886 comparable. The **routed** statistic is the committed
partition (sum-of-per-component-variances denominator, bounded [0,1]) -- driver:705-713 and the
`share_method_note`. The driver states this explicitly and declines to move the 0.85 bar onto
the new statistic, which is the correct anti-fabrication instinct.

**(b) "A1's committed total variance is 1.5e-05, six orders below A0's -- the monopoly share is
computed on numerical noise, and the 1e-09 non-degeneracy floor is set four orders too low to
catch it."** WITHDRAWN on recomputation. The variance collapse tracks a **score-scale**
collapse, and the share is scale-invariant:

| arm | score_range_mean | sqrt(total var) | **std / range** |
|---|---|---|---|
| A0 clamp_off | 1.95 - 16.36 | 2.75 - 11.34 | **0.44 - 1.40** |
| A1 clamp_on | 0.0030 - 0.0067 | 0.0039 - 0.0191 | **0.56 - 3.18** |

The dispersion-to-range ratio is comparable across the two regimes; the clamp shrinks the
scores (`score_range` 4.67 -> 0.006, `zw_max_norm` 135-402 -> 0.78-0.98) and the variance falls
with roughly the square of that. Observed A1 standard deviations are ~0.004-0.019 against a
float64 relative precision of ~1e-16 at these magnitudes -- roughly **fifteen orders above the
numerical floor**. This is a scale change, not a degeneracy. The 1e-09 floor is generous but
is not certifying noise.

## 3. The live finding: the monopoly premise is REGIME-dependent

`failure_autopsy_V3-EXQ-936a_2026-08-30` (confirmed) closed the 936 family with an explicit
gate: *"Further 936-family falsifiers are REFUSED until a monopoly-present regime is
established by a clamped 571b-shape presence audit."* V3-EXQ-571b is that audit and it returns
monopoly-present. But the two runs disagree by five orders of magnitude on the same question,
under the same clamp (`e2_rollout_output_norm_clamp_enabled=True`, ratio 2.0 -- verified in the
936a driver's own docstring, not inferred):

| | V3-EXQ-936a | V3-EXQ-571b (A1) |
|---|---|---|
| clamp ratio | 2.0 | 2.0 |
| env | 12x12, 4 hazards, 5 resources, reef bipartite, env drift | 8x8, 1 hazard, no reef, no drift |
| schedule | P0 60 ep, 200 steps/ep | 20 ep, 100 steps/ep |
| `update_residue` feeding | **every env step** (driver:760) | **never called** (0 calls in the executed driver) |
| **F variance share (clamped baseline)** | **6.33e-06** -- monopoly ABSENT | **0.976 - 0.996** -- monopoly PRESENT |
| monopolist | `residue_weighted` (0.999988 - 0.999998) | `harm_weighted` (0.937 - 0.995) |

The discrepancy is **not** a statistic artifact. It survives both share methods (571b's
clamped legacy-pool F share is 0.886-1.73 against 936a's 6.328e-06 pool / 6.268e-06 committed),
both runs use the same F family (`{f | f_weighted, harm_weighted}`, residue excluded from F on
both sides), and the executed 571b driver is hash-confirmed against the manifest
(`driver_script_hash 15a694e1100f...`).

**But the cause is NOT established as the environment, and this artifact does not claim it is.**
An earlier draft asserted the gap was "attributable to environment, not instrument"; the
cross-model red-team pass contested that and the contest holds. The entire five-order gap is
carried by one channel -- `residue_weighted`, which holds 0.999988-0.999998 of 936a's committed
variance -- and the two runs differ in **three** ways at once, any of which could feed that
channel differently:

1. **Environment** (12x12/4-hazard/reef/drift vs 8x8/1-hazard/static).
2. **Residue-feeding protocol.** 936a calls `agent.update_residue(harm_signal=..., owned=True)`
   on every env step (`v3_exq_936a_...py:760`); the 571b driver that actually executed contains
   **zero** `update_residue` calls.
3. **Schedule** (P0 60 ep x 200 steps vs 20 ep x 100 steps).

The measurement that would separate these -- `residue_rbf_active_centers` -- was added to the
571b driver in a **post-run** commit and is absent from this run's manifest. So the honest
statement is that the monopoly premise is **regime-dependent**, where "regime" means the
environment and/or the residue-feeding protocol and/or the schedule, and this run cannot
apportion between them. Residue's committed fraction in 571b A1 is nonzero (0.0013-0.0235), so
it was a live candidate occupant in the 571 regime and lost -- which rules out "structurally
absent" on the 571b side but says nothing about why it dominates on the 936a side.

**Consequence for the gate -- unchanged by the above.** 571b did exactly what 936a asked for: a
571-shape audit on 571's own seeds, for comparability with the 0.886 reference. But the
*purpose* of the gate was to license 936-family falsifiers, and those run in the 936 regime,
where 936a has already **measured the premise absent directly**. That measurement stands
whatever its cause. Clearing the gate on this run would resume a falsifier family in a regime
where its premise does not hold. The run's own `outcome_note` says a re-posed falsifier "must
name WHICH F channel it targets", which is correct but understates this: it must also establish
monopoly-presence **in the regime it will run in**, matched on residue protocol and schedule as
well as environment.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | MECH-439's premise is confirmed for the 571-shape env only; the claim's channel-level reading does not transfer across the instrument change |
| Biological reference | partial | E3 score-component authority; no biology divergence implicated by this run |
| Prerequisites | present | all three readiness preconditions met; `clamp_config_landed_every_cell` = 1.0 is a genuine config-landing identity, which matters because `REEConfig.from_dims` swallows unknown kwargs silently |
| Implementation | complete | the SD-056 rollout clamp is built and demonstrably binding (`at_ceiling_frac` 0.92-0.97; `max||z_w||/ceiling` 1.0000 clamped vs 293.86 unclamped) |
| Environment | adequate **for its own question** | 8x8 / 1 hazard is a faithful 571-shape reproduction; it is NOT the 936-family env and must not be read as licensing conclusions there |
| Measurement | adequate | the routed statistic is a genuine bounded partition; scale-invariance verified by recomputation (section 2b) |
| Integration | adequate | env seeding derived from the run seed only, so all four arms at a given seed share a layout and the clamp contrast is genuinely within-layout |
| Scale | adequate | 187-285 fresh selections per cell against a 60 floor |

**Failure-location (GOV-FAILLOC-1):** not applicable as a failure -- this is a PASS. Recorded
for completeness: Implementation complete, Measurement adequate, Environment adequate for the
question posed. No bucket established; REE FAILED not reachable and not asserted.

## 5. A side-effect of the SD-056 clamp worth recording

Surfaced by the Step 7b C2 check, which correctly pointed out that SD-056 already unblocks
MECH-439 and was unmentioned in the first draft of this artifact. SD-056 is the rollout
stability clamp that **is** this run's manipulation, so the observation belongs on it.

With the clamp armed, E3's committed score range collapses from 1.95-16.36 to 0.0030-0.0067
(~800x) and 92-97% of rollouts sit pinned at the ceiling. The clamp does its job -- it removes
the divergence SD-056 exists to fix (936 recorded var(F) reaching 4.07e72 unarmed; here
unclamped `max||z_w||/ceiling` reaches 293.86) -- but the previously unrecorded cost is that
E3's candidate scores become nearly indistinguishable in the clamped regime. Whether selection
is meaningfully *driven* under that regime is a separate question this run does not answer, and
one that bears on any experiment reading E3 selection behaviour with the clamp armed.

## 6. Learning extracted

1. A gate phrased as "establish premise P by an experiment of shape S" is satisfied by shape S
   and licenses only shape S's regime. 936a asked for a 571-shape audit to unblock 936-shape
   falsifiers; the audit passed in its own regime while 936a's own data says the premise is
   absent in the target regime. Phrase premise-gates on **every dimension the gated work
   differs on** -- environment, driver protocol and schedule -- not just the one that is easiest
   to name. The first draft of this artifact promoted the environment dimension into the gate
   and silently dropped the residue-feeding protocol, committing the very error this item
   states.
1b. When two runs differ on several dimensions at once, a single-cause attribution needs a
   measurement that isolates it, not a plausible mechanism. The five-order F-share gap here is
   wholly carried by `residue_weighted`, and environment, residue-feeding protocol and schedule
   all differ; the isolating measurement (`residue_rbf_active_centers`) was added post-run and
   is absent from the manifest. "Regime-dependent" is what the evidence supports.
2. A variance SHARE is scale-invariant, so a large drop in absolute variance is not by itself
   evidence of degeneracy. Test it by comparing dispersion to the score range in both regimes
   before reading a collapse as noise -- and set non-degeneracy floors relative to the regime's
   own scale rather than at a fixed absolute the fixed regime cannot approach.
3. A fix can be correct and still change the regime enough to invalidate downstream readings.
   The SD-056 clamp removes a genuine numerical pathology and collapses E3's score range ~800x
   in doing so; both facts need recording on the substrate entry, not just the first.

## 7. Routing (confirmed at the Step 8 gate)

**`/queue-experiment` -- a monopoly-presence audit in the 936-family REGIME.** The user
ratified at the gate that **936a's gate stays SHUT for the 936 regime.** 571b clears the
premise for the 571 regime only. Before any 936-family falsifier resumes, run a presence audit
that is matched to the falsifiers it gates on **all three** dimensions the two runs differ on,
not just the environment:

1. **Environment** -- 12x12, 4 hazards, 5 resources, reef bipartite, env drift.
2. **Residue-feeding protocol** -- per-step `agent.update_residue(...)`, as the 936 family's own
   driver does. This is the dimension the first draft of this artifact left out, and leaving it
   out would reproduce exactly the failure the run's `learning_extracted[1]` names: a gate
   phrased on one dimension licensing work that differs on another. An audit that found
   monopoly-present in the 936 *env* while starving residue the way 571b does could wrongly
   clear the gate for falsifiers that feed residue per step.
3. **Schedule** -- P0 60 episodes x 200 steps/ep.

It must report which channel holds the monopoly and whether the 0.85 bar clears. It should also
record `residue_rbf_active_centers` (added to the 571b driver post-run and absent from this
run's manifest), which is the measurement that would let a future comparison apportion the gap
between environment, residue protocol and schedule rather than asserting one of them.

If that audit does not clear, the 936-family falsifier design needs re-posing against the actual
monopolist, not against F.

**`recommended_diagnostic_evidence_adjudicated: true`** for MECH-439 -- this is a diagnostic
target and is `scoring_excluded` by design, so without the flag the claim keeps reading as an
untouched evidence gap to the auto-proposal generator despite an extensively adjudicated
diagnostic narrative.

**`substrate_queue` action: amend SD-056** with the score-range-collapse observation in
section 5. No new substrate entry; the clamp is built and working.

No `fanout_recommendation` is emitted. This run narrows scope rather than opening a
discrimination portfolio, and the env-dependence question it raises belongs to the 936 family's
own re-pose, not to a new portfolio on `e3_fdominance_causal_discrimination`.

**Correction record.** The cross-model red-team pass (Fable, skill Step 7c) returned
**CONTESTED** on this artifact. Its commensurability attack -- that 936a's 6.33e-06 and 571b's
0.976-0.996 might not be the same statistic -- **failed**: F family, share method, weighting
basis and clamp/arm role were all verified equivalent, so the five-order gap is real. The
contest that held is narrower and is applied above: the first draft asserted the gap was
"attributable to environment, not instrument", and that single-cause attribution is not
established. The gap is wholly carried by `residue_weighted`, and the two runs differ on
environment, residue-feeding protocol and schedule at once, with the isolating measurement
absent from the manifest. The attribution is now stated as **regime**-dependent, and
residue-protocol and schedule parity have been added to the routed audit spec -- the omission
of which would have reproduced the exact failure this artifact's own `learning_extracted[1]`
names. Every confirmer was independently re-verified before the change was applied. The
gate-stays-shut decision, the PASS adjudication, the occupant-shift finding, the SD-056 amend
and the `non_contributory` direction are unchanged.
