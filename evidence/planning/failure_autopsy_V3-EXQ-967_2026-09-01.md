# Failure autopsy -- V3-EXQ-967 (MECH-144 shuffle-inertness confirmer)

- **Generated (UTC):** 2026-09-01T06:44:22Z
- **Scope:** single
- **Status:** confirmed (Step 8 gate held 2026-09-01, user present)
- **Run:** `v3_exq_967_mech144_shuffle_inertness_confirmer_20260901T062344Z_v3`
- **Outcome:** PASS -- `experiment_purpose: diagnostic`, `claim_ids: []`
- **Self-route label:** `behaviour_diverges_contacts_coincide` -- **upheld on its load-bearing negative; its positive attribution is over-specified**
- **Dry-run gate:** checked, `dry_run: false`; 0 dry runs cited or excluded.

## 1. What this run was for

`failure_autopsy_966-436g-951-959-822d-cluster_2026-08-30` (confirmed) found the V3-EXQ-966
C2 manipulation INERT: `block_contacts` bit-identical between `ARM_FIXED_VALUE` and
`ARM_SHUFFLED_VALUE` on 4/4 seeds x 4/4 blocks. Its `four_layer_diagnosis.environment` reads
*"unknown -- the mechanism for the zero contrast is UNRESOLVED; the agent_energy channel is
open and amp-scaled in most of each episode, so the earlier clamp-based explanation is
withdrawn"*, and the note governance applied to MECH-143/144 closes with *"the mechanism is
unresolved and a cheap confirmer runs first."* **V3-EXQ-967 is that cheap confirmer**, and it
resolves the question.

## 2. Facts

Criteria: **C1 PASS (load-bearing), C2 PASS, C3 PASS.** Discriminators
`D1_amplitudes_differ`, `D2_contact_benefit_differs`, `D3_energy_differs`,
`D4_actions_differ` all **true**; `D5_contacts_differ` **false**.

| quantity | value |
|---|---|
| `energy_spends_time_unclamped` (readiness) | **0.99** of logged steps strictly below the 1.0 ceiling |
| `max_energy_diff` between arms | **0.99** |
| `n_energy_diff_steps` | 709 |
| `first_energy_divergence_step` | 2580 |
| `n_action_diff` / `n_matched_steps` | **46 / 2400** (0.0192) |
| `first_action_divergence_step` | 4493 |
| `contact_bump_reaches_agent_energy` (positive control) | 0.30 vs 1e-06 floor |
| `logged_contacts_sufficient` | 22 vs floor 4 |
| `p0_warmup_actually_trained` | 1440 optimiser steps vs floor 1 |
| `block_contacts` A vs B | **identical**: `[{t1:3,t2:2},{t1:2,t2:6},{t1:9,t2:5},{t1:2,t2:6}]` both arms |

Seeds: `[42]` -- a single seed. `z_goal_stream.writer_defect: false` (12480 writer calls,
`active_frac` 0.968) -- this run's goal stream is correctly wired, unlike V3-EXQ-642b's.

The readiness set is unusually well-constructed: each precondition is a genuine positive
control for the criterion it gates, and the `contact_bump_reaches_agent_energy` description
explicitly warns that its VALUE is not a calibrated `contact_benefit` (the reconstruction
subtracts per-step decay but not movement cost) and that only its being above zero is asserted.
That self-limitation is correct and is honoured here.

## 3. What is established: the energy route is open and the 966 floor-clamp claim is refuted

The 966 cluster autopsy's `recommended_evidence_quality_note` explained the inertness by all
three amplitude routes being closed -- residue sign-gated, `agent_health` pinned at 1.0 by
`NUM_HAZARDS=0`, and `agent_energy` *"floor-clamped at 0.0 under a 0.01/step decay that
dominates ~0.8 contacts/episode"*. **The third of those is refuted.**

The refutation rests on the energy **level**, not on the run's `energy_spends_time_unclamped`
precondition. That precondition measures distance from the **1.0 ceiling** and would read ~1.0
even if energy were pinned at zero, so it is uninformative about a **floor** claim. The
load-bearing numbers, recomputed directly from `per_step_log` (2400 rows, steps 2400-4799):

| quantity | value |
|---|---|
| `energy_mean` (ARM_FIXED / ARM_SHUFFLED) | **0.4892 / 0.4845** |
| recomputed mean of `energy_post` | 0.4809 |
| **fraction of steps at the 0.0 floor** | **0.1017** |
| fraction at the 1.0 ceiling | 0.0 |
| `max_energy_diff` between arms | 0.99, across 709 steps |

Energy sits near the middle of its range and touches the floor on only ~10% of steps. Decay
does not dominate it, and the amplitude manipulation moves it by up to 0.99 between arms. The
other two routes (residue sign-gating, `agent_health` pinned by `NUM_HAZARDS=0`) are untouched
by this run and stand.

## 4. What is NOT established: the attribution to the DV

The `outcome_note` asserts *"The bit-identity is then a property of the contact-counting DV
(saturation / coarse quantisation), not of the policy."* **The evidence does not carry that.**
The headline "block_contacts bit-identical on 4/4 blocks" substantially overstates what was
observed, and a block-resolved recomputation shows why.

The logged window covers **only the two arm-differing blocks** (0-indexed 2 and 3; the run's
`logged_contacts_sufficient` = 22 is exactly their combined contact count, 9+5+2+6). Blocks 0
and 1 share an amplitude assignment across arms by design, so their contact identity is
expected and carries no information -- correctly so, but it means 2 of the 4 "matching" blocks
are not evidence. Within the two blocks that *do* differ:

| block (0-idx) | steps | **action divergence** | energy divergence | contacts A vs B |
|---|---|---|---|---|
| 2 | 1200 | **0** | 296 steps | `{t1:9, t2:5}` vs `{t1:9, t2:5}` |
| 3 | 1200 | **46** (3.8%) | 413 steps | `{t1:2, t2:6}` vs `{t1:2, t2:6}` |

Two consequences, and the first is the sharper one:

**(a) In block 2 the arms took literally identical actions** despite energy differing on 296
steps. Identical contacts there is a tautology, not a DV property. It is also, read on its own,
exactly what an *insensitive policy* looks like -- so the hypothesis 967 is credited with
eliminating is attenuated in that block rather than excluded.

**(b) The entire evidential weight for "the DV cannot see it" rests on block 3**, where 46 of
1200 steps (3.8%) diverged, all of them late -- `first_action_divergence_step` is 4493 in a
window ending at 4799, so the arms were action-identical for roughly the first 87% of the
logged window. Small integer counts (2 and 6) surviving 46 late divergent steps is at least as
consistent with **insufficient behavioural exposure** as with DV saturation or coarse
quantisation, and this run cannot separate the two.

So the load-bearing negative stands in weakened form -- the policy is not wholly unresponsive
and the energy route is demonstrably open -- while the positive attribution to the DV is
**not established**. What is solid is narrower and still useful: *the manipulation reaches the
agent and changes behaviour, so the inertness is not a closed route.* Where the remaining
inertness comes from is open between a coarse DV and too little divergence to move it.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim-free confirmer; bears on MECH-143 / MECH-144 via the 966 cluster |
| Biological reference | clear | hippocampal value-sensitive trajectory scoring; no translation error implicated, and this run does not reach a test of it |
| Prerequisites | present | P0 warmup genuinely trained (1440 optimiser steps, not merely rolled) -- the precondition exists precisely so an untrained encoder's indifference cannot be read as an insensitive policy |
| Implementation | complete | the amplitude -> benefit -> energy chain is live and measured end to end; energy mean 0.48, arms differ by up to 0.99 |
| Environment | adequate | energy at the 0.0 floor on only 10.2% of steps; the 966 floor-clamp explanation is refuted |
| Measurement | **under-instrumented** | the DV is a per-block integer count over blocks in which the arms are action-identical (block 2) or diverge on only 3.8% of late steps (block 3); it cannot discriminate, but this run does not establish that a *finer* DV would either |
| Integration | coupled | routes coupled and observable |
| Scale | **likely insufficient** -- the dominant limitation | 1 seed; 0/1200 action divergence in one arm-differing block and 46/1200 in the other, all in the last ~13% of the window; only 2 of 4 blocks carry any information |

**Failure-location (GOV-FAILLOC-1) for the 966 phenomenon: MIXED -- MEASURES + SCALE, not
chargeable to REE.** Implementation and Environment both read adequate on this run's own
evidence, so neither MECHANISM nor ENVIRONMENT is established and REE FAILED is not reachable.
Measurement is under-instrumented and behavioural exposure is insufficient, and this run cannot
apportion between them. A solo MEASURES read would overstate what was shown.

## 6. Learning extracted

1. Eliminating one explanation does not establish the named alternative. 967 shows the route is
   open and the policy is not wholly unresponsive; it does not separate DV quantisation from
   insufficient behavioural exposure, and its `outcome_note` asserts the former.
2. **A count of matching cells is not a count of informative cells.** "Bit-identical on 4/4
   blocks" covered two blocks that share an amplitude assignment by design and one in which the
   arms took identical actions. Only one block carried any discriminative weight. Report the
   informative denominator, not the total.
3. **A precondition must be denominated on the quantity the claim it tests is about.**
   `energy_spends_time_unclamped` measures distance from the 1.0 ceiling and was read against a
   claim about the 0.0 floor; it would read ~1.0 under exactly the condition it was invoked to
   exclude. The floor claim is genuinely refuted -- by `energy_mean` 0.48 and a 10.2% at-floor
   fraction -- but by a different number than the one cited.
4. A bit-identical DV across arms is a DV property to investigate, not a null result to report;
   V3-EXQ-966 reported the identity as a finding about the manipulation, and the manipulation
   was live.
5. A repair direction inherited from a prior autopsy needs re-checking against the confirmer's
   own data. 966's "change the env config" was reasonable on 966's evidence and is wrong on
   967's -- naming a downstream repair is not performing it, and the naming does not survive new
   evidence automatically.

## 7. Routing (confirmed at the Step 8 gate)

**`/queue-experiment` -- a V3-EXQ-966 successor under a new letter, changing the DEPENDENT
VARIABLE *and* the exposure.** Keeping the env config is right: the amplitude reaches an
unclamped channel and energy moves by up to 0.99. Three changes, not one:

1. **Replace the per-block integer contact count** with a readout sensitive to when and where
   divergence occurs -- a per-step contact indicator series, contact timing, or an energy
   integral over the block -- and pre-register the criterion against that statistic.
2. **Secure enough behavioural divergence to be worth measuring.** 0/1200 and 46/1200 in the
   two arm-differing blocks is not an exposure a per-block count could have resolved under any
   quantisation. Log the full run rather than two blocks, and report per-block action-divergence
   alongside the DV so a null is interpretable.
3. **Run more than one seed.**

Report the informative denominator explicitly. The successor should be able to say, for each
block, whether the arms behaved differently at all before any claim is made about whether the
DV could see it.

**No substrate work.** `recommended_substrate_queue_entry.action: none`. Nothing in the
substrate is implicated.

**Correction record.** The first draft of this artifact cited
`energy_spends_time_unclamped = 0.99` as refuting 966's floor-clamp claim and read the DV
attribution as established. Both were corrected before landing, on a recomputation from
`per_step_log`: the floor claim is refuted by the energy *level* (mean 0.4809, 10.2% at floor),
and the block-resolved action divergence (0/1200 and 46/1200) shows the DV attribution is not
established. The corrected reading is what governance should act on.
