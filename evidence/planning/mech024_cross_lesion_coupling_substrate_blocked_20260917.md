# MECH-024 ("Selfhood, personality, and ethics converge structurally") -- SUBSTRATE-BLOCKED

- **Recorded:** 2026-09-17T22:50:00Z
- **Session:** `igw-243-proposal-for-mech-024` (IGW-20260917-243, lane `experiment`, skill `/queue-experiment`)
- **Proposal:** `EVB-1395` / `EXP-0763` / `proposal_type: experimental` -> `status: blocked_substrate`
- **Outcome:** NO experiment queued. Refused at the Step 2.5 substrate-readiness STOP-GATE, before
  any script was written. Every blocking fact below was measured or read off recorded evidence in
  this session, not inherited as narration.
- **Claim status UNCHANGED** in `claims.yaml`. This document promotes nothing.
- **The `literature_review` twin `LIT-0764` is deliberately left `status: proposed`** -- the block
  is about V3 substrate, not about the literature, and MECH-024 carries
  `missing_literature_evidence` in its own `why_now`.

---

## 1. What the registered falsifier asks for

MECH-024's `what_would_answer` specifies a **3x3 cross-lesion coupling matrix** on one trained
substrate per seed (capture/restore between cells):

| axis | lesion | readout |
|---|---|---|
| SELFHOOD | freeze the `SelfRecurrenceCell` hidden state | `z_self` coherence (`hippocampal.per_stream_vs['z_self']`) |
| PERSONALITY | freeze `LatentStack` precision logits + readiness floors at init | distribution of `SalienceCoordinator.operating_mode` and `CommitReadiness.get_readiness` |
| ETHICS | freeze/zero the residue field | harm-veto / residue-cost rate on a fixed hazard probe set |

with two gates that decide everything below:

- **NON-DEGENERACY PRECONDITION:** each lesion must move ITS OWN readout (a non-zero diagonal),
  and no readout may be "constant across seeds or saturated", before any off-diagonal is
  interpretable.
- **CONFIRMING** needs **>= 2 off-diagonal cells at a sign-consistent shift `>= 2 SD(seeds)`**
  AND a **connected** coupling graph -- "every axis reaches every other through some lesion".
  With three axes, connectivity *requires* the ethics row/column to be readable.
- **FALSIFYING** is "the matrix is DIAGONAL -- every off-diagonal sits inside the seed-noise band".

This is a commitment-free, measurement-only design (all three readouts are probe reads, never a
committed-action outcome), so it is correctly NOT blocked by the
`f_dominance_conversion_ceiling`. The block is elsewhere.

## 2. Axis-by-axis readiness (measured 2026-09-17)

### 2a. SELFHOOD -- READY

`V4-EXQ-002` (`v4_exq_002_dr13_self_recurrence_falsifier`, 2026-07-01, **PASS**, 3 seeds) is a
purpose-built substrate-readiness probe for exactly this lesion:

| gate | value |
|---|---|
| `self_recurrence_live_state_departure` (precondition) | **1.1472** vs floor 0.001, met on every seed |
| `C1_carries_history` | 3/3 seeds |
| `C2_perturbation_isolated` | 3/3 seeds |
| `C3_anchor_blend_live` | 3/3 seeds |

The self subject is live, stateful, lesionable and perturbation-isolated. **This axis is not the
problem.** (`use_self_recurrence` defaults False, so a successor must set it.)

### 2b. PERSONALITY -- readout SATURATED by default; has a lever, so NOT counted as a blocker

`SalienceCoordinator`'s own source records the degeneracy
(`ree_core/cingulate/salience_coordinator.py:275-292`, MECH-266 / 2026-08-12):

> `dacc_pe` (and the `foraging_value` derived from it) are unbounded and enter the AFFINITY logits
> at raw magnitude -- diagnostic replay of the V3-EXQ-464d/467d substrate measured `dacc_pe`
> ~16-17 through eval, two orders of magnitude above the [0,1]-bounded `external_task_drive` ...
> so `internal_planning`'s argmax never yields regardless of engagement and **`operating_mode`
> collapses to one-hot `internal_planning`** instead of the soft-weighted vector this class's own
> docstring specifies.

`salience_affinity_input_cap` defaults to `None` (no clamp, bit-identical to pre-2026-08-12), so
**the default configuration delivers a one-hot `operating_mode`** -- precisely the "saturated"
readout MECH-024's own non-degeneracy precondition names as degenerate.

This is a config lever, not missing substrate, so it is recorded as a **mandatory design
precondition for the successor** rather than as a blocker: set `salience_affinity_input_cap` and
assert `H(operating_mode) > 0` per seed before reading any personality cell.

A second, unresolved design defect on this axis is recorded here because it needs a decision, not
a knob: **"freeze the precision logits and readiness floors at their init values" on an ALREADY
TRAINED agent is a reset-to-init, not a freeze.** Applied at probe time it discards the learned
control plane wholesale, which is a global control-plane disruption -- exactly the pattern
MECH-024's own text says is NOT confirmation ("all readouts degrade under every lesion by the
same proportion"). Applied at training time it forces a separately-trained agent per lesion,
which contradicts the "one trained substrate per seed (capture/restore between cells)"
construction. The claim already flags this axis as "the weakest operationalisation"; the
ambiguity is sharper than that wording suggests and should be resolved in `what_would_answer`
before a successor designs against it.

### 2c. ETHICS -- BLOCKING

Three separate facts, all confirmed in this session.

**(i) The ethics channel's seed dispersion exceeds the criterion it must be measured against.**
`V3-EXQ-697` (`v3_exq_697_arc013_residue_separability_falsifier`, 2026-06-21, PASS, 5 seeds,
`residue_populated: true`, coverage 100%) is the only recorded measurement of a POPULATED residue
field's effect on selection. Per-seed:

| seed | `mean_weight` | `flip_intact_vs_zeroed` |
|---|---|---|
| 42 | 54.07 | 0.8986 |
| 43 | 2.52 | 0.0596 |
| 44 | 7.73 | 0.2986 |
| 45 | 26.14 | 0.9964 |
| 46 | 43.91 | 0.8850 |

| statistic | `mean_weight` | `flip_intact_vs_zeroed` |
|---|---|---|
| max/min | **21.5x** | 16.7x |
| mean | 26.87 | 0.6276 |
| SD | 22.30 | 0.4203 |
| CV | **0.830** | **0.670** |
| **2 SD** | 44.61 | **0.8406** |

MECH-024's confirming criterion is a shift `>= 2 SD(seeds)`. On the ethics channel **2 SD spans
0.84 of a DV bounded in [0,1]** -- i.e. 84% of the entire measurable range. No off-diagonal cell
touching ethics can clear that bar at any effect size the substrate can produce, with 3 seeds or
with 30. The criterion is not merely hard on this channel; it is **arithmetically unreachable**.

**(ii) The instability has a known structural cause, and it is MECH-023's capacity blocker
arriving by a different route.** `RBFLayer.add_residue` is a 32-slot RING BUFFER
(`num_basis_functions = 32`, `kernel_bandwidth = 1.0`, both confirmed at
`ree_core/utils/config.py:3116-3117`), measured by IGW-242 to wrap ~28 times in a 720-step run
(895 harm events). MECH-024 injects no fork history, so the *relocation* artifact that blocks
MECH-023 does not apply here. What does apply is its corollary: **the final field is a sample of
whichever 32 harm events happened last**, so its total mass is a property of recent harm
intensity rather than a stable property of the agent -- which is what the 21.5x `mean_weight`
spread above is measuring. Same substrate defect, different and independently decisive
consequence.

**(iii) The ethics readout carries an untrained random term that does not cancel here.**
`ResidueField.neural_field` (`ree_core/residue/field.py:434`) is a randomly-initialised MLP
contributing `0.1 * MLP(z)` to every `evaluate_trajectory` (`:615`, `:629`, `:1137`). Re-verified
this session: those are the only references, and no loss, optimizer or backward pass anywhere in
`ree_core/` touches any residue parameter -- **it is never trained.** IGW-242 could discount this
because MECH-023 contrasts fork-vs-fork, where the term cancels. **MECH-024's ethics lesion is
intact-vs-zeroed, so it does not cancel**: the random field enters the ethics diagonal and every
ethics-column off-diagonal as unmodelled seed-varying offset. The analogous untrained-scorer
hazard is already gated OFF for E3's `reality_scorer`
(`e3_include_untrained_fallback_scorers=False`); it is ungated here.

**(iv) Separately, the ethics DIAGONAL as registered is near-tautological.** Zeroing the residue
field drives residue-cost to exactly zero by construction, so the "non-zero diagonal" gate passes
without testing anything. Only the harm-veto half of the readout is substantive, and that is the
0.42-SD channel in (i).

## 3. The registered ordering precondition is also unsatisfiable

MECH-024's own 2026-09-16 governance disposition reads: *"Recommend it be queued only after
MECH-023 (the ethics-geometry half) has a result, since MECH-023 is one of this matrix's diagonal
cells."* MECH-023 has **no result**: `EVB-1394`/`EXP-0761` was itself set `blocked_substrate` on
2026-09-17T21:16:49Z (REE_assembly `055b4d35553`), 77 minutes before this session was spawned, on
the same residue substrate. The ordering gate cannot clear until the residue work lands, which is
the same release condition recorded below.

## 4. What the run would have produced (why this is a refusal, not caution)

The matrix would have completed. The selfhood diagonal would be live (2a). The personality
readout would be one-hot and constant unless the successor happened to set an undocumented cap
(2b). Every ethics off-diagonal would sit inside a seed-noise band 0.84 wide (2c-i) and therefore
be scored as "inside the noise band" -- which is MECH-024's **FALSIFYING** branch verbatim.

The recorded verdict would have been *"in V3 selfhood, personality and ethics ARE separable
modules; the convergence claim is false as a mechanism claim"*, entering the evidence record as a
measured property of the architecture. It would in fact be a statement about a 32-slot ring
buffer's mass variance and an unclamped `dacc_pe` logit. That is a vacuous result with a
confident sign, which is worse than no result -- and at 9 cells x >= 3 seeds x one trained
substrate per seed, an expensive one.

## 5. Release condition

MECH-024's registered falsifier becomes runnable when **all three** hold:

1. **`residue-field-ring-capacity`** -- residue accumulation is no longer a 32-slot window over
   the most recent harm events, so total field mass is a stable property of the agent rather than
   of its last 32 steps. Target: `num_harm_events < num_centers` over the experiment's schedule,
   or an append-only / consolidating accumulation path. (Shared with MECH-023; `complicated
   (buildable)`.)
2. **`residue-field-kernel-resolution`** -- residue kernel bandwidth commensurate with the
   `z_world` manifold (`pole_sep / bandwidth >= 2`). Note `ree_core/utils/config.py:3151` already
   records that `kernel_bandwidth` 1.0 is "~15x too wide for the z_world residual scale", and
   SD-067's opt-in `safety_terrain_bandwidth` fixes this for the MECH-303 *safety* terrain only --
   the harm residue field is untouched and unowned. (Shared with MECH-023; `complicated
   (buildable)`.)
3. **`residue-cost-untrained-neural-field`** -- MECH-024-specific. Either train
   `ResidueField.neural_field`, or gate it off for intact-vs-zeroed reads the way
   `e3_include_untrained_fallback_scorers=False` already gates E3's untrained fallback scorers.
   `complicated (buildable)`.

Plus two things a successor must carry that are **not** blockers:

4. Set `salience_affinity_input_cap` and assert `H(operating_mode) > 0` per seed, or the
   personality readout is saturated one-hot (2b).
5. Get `what_would_answer`'s personality LESION disambiguated -- freeze-at-training vs
   reset-at-probe are different experiments and the second is a global disruption (2b). This is a
   `/governance` edit to the claim, not substrate work.

## 6. Verification checks a successor should re-run first (cheap)

```
# ethics-channel stability: the criterion needs 2*SD(seeds) to be SMALL vs the DV range
CV(mean_weight across seeds)          # measured 0.830 -- want << 1
num_harm_events < residue.num_basis_functions          # measured FALSE (895 vs 32)
max_pairwise(z_world_buffer) / residue.kernel_bandwidth # measured 0.125 -- want >= 2

# personality readout must not be saturated
H(operating_mode) > 0 per seed        # zero at salience_affinity_input_cap=None

# selfhood axis is already green (V4-EXQ-002) but re-assert cheaply
self_recurrence_diag['state_departure'] >= 0.001
```

## 7. Provenance

- Refused at Step 2.5 (substrate readiness), before authoring, so **no driver script was written
  and none is owed** -- an unqueued script under `ree-v3/experiments/` is audited as debt.
- Facts (i)/(iii) and the personality saturation in 2b were established in this session from
  recorded evidence and source, not carried over from IGW-242. Fact (ii) reuses IGW-242's
  measurement of the ring wrap but derives a different consequence for this claim.
- GOV-REUSE-1 (Step 2.4): the decisive readout is the 3x3 lesion x readout coupling matrix. No
  recorded manifest carries a cross-lesion matrix over these three axes; `V4-EXQ-002` carries the
  selfhood diagonal alone and `V3-EXQ-697` the ethics channel alone. Not recoverable by
  reanalysis -- which is why the stop is a substrate block rather than a reuse routing.
- Governance action owed: mint `residue-cost-untrained-neural-field` into `substrate_queue.json`
  alongside GFLAG-0337's `residue-field-ring-capacity` / `residue-field-kernel-resolution`, and
  amend MECH-024's `what_would_answer` per 5.5.
