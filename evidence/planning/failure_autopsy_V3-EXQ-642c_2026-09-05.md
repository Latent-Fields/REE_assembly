# Failure autopsy (diagnostic adjudication) -- V3-EXQ-642c

**Run:** `v3_exq_642c_blocked_agency_headroom_dv_validation_20260904T214459Z_v3`
**Queue:** V3-EXQ-642c (supersedes V3-EXQ-642b)
**Purpose:** diagnostic | **Outcome:** PASS | **evidence_direction:** non_contributory
**claim_ids:** `[]` (claim-free post-build substrate validation)
**bears_on:** MECH-353, SD-029, MECH-112, MECH-320, MECH-342, ARC-016, SD-011, SD-019b, SD-070, SD-056
**Indexer adjudication flag:** `vacuous_pass` (`criteria_non_degenerate.C2 = false`)
**Generated:** 2026-09-05T02:38:25Z | **Status:** `confirmed`
**Confirmed:** 2026-09-05T09:34:46Z by `governance-20260905 (user gate, inline route A)`
**Step 7c red-team:** RUN (fable-5.1, cross-model) -- **CONTESTED**, F1-F5 + H1-H8 folded; see section 11.
**Step 8 gate:** HELD. User decision, binding: **hold `v3_pending`; route 642d with withdraw representable.**

---

## 0. Verdict in one paragraph

The PASS is **real, and real for a real reason -- but for a narrower reason than its own label
claims**. What V3-EXQ-642c validates is the *substrate lever*: the baseline-relative
`outcome_mismatch` floor built in ree-v3 `d49db86f3e64670` gives the `z_block` integrator genuine
dynamic range, and C1 -- the one load-bearing criterion that both varies and discriminates --
passes 3/3 seeds against an a-priori bar that provably rejects the un-calibrated predecessor
regime. What it does **not** validate is MECH-353 -- and after the Step 7c red-team the reason is
not the one this draft originally gave.

**The decisive defect is that `withdraw` has never been REPRESENTABLE in this family (F3).** The
driver runs at `action_dim=4` while `blocked_agency_noop_class` defaults to `0`, which
`CausalGridWorldV2` maps to MOVE-UP; the stay action is index `4` and a 4-dim policy can never emit
it. So C3's `action_rate` has always scored *"fraction of steps not choosing move-up"*, the
consumer's ASSERT score-bias treats move-up as the passive option (`blocked_agency.py:426`), and
the assert-vs-withdraw dissociation MECH-353 names **has never been measurable at all**, across
642 / 642a / 642b / 642c. This is an experiment-**configuration** defect, not a substrate bug.
Separately, `num_hazards = 0` pins `z_harm_a` at `0.0`, making C2 entirely inert (which the driver
flagged) and C3's `no_suffering` conjunct inert too (which it did not). **Three of the four
load-bearing criteria therefore carry an inert or mis-specified leg.**

**On `v3_pending`, this artifact records a governance JUDGMENT, not a forced reading (F1).** The
claim's own words say *"harm + goal held constant"* and name *"V3-EXQ-642b"* as the release run,
which 642c supersedes and passes -- so a fair reader could call this the release, and the draft's
earlier "not a matter of interpretation" framing was wrong. Both readings were put to the user at
the Step 8 gate; **the user held `v3_pending`**, on the ground that the claim's named release run
has not yet been *validly* run. So the self-route label `validated_clear_v3_pending` is **overturned
in part**: `validated` yes, `clear_v3_pending` no. The `vacuous_pass` flag is **UPHELD and
broadened**.

---

## 1. Facts -- reconstruction, no interpretation

### 1a. Dry-run and recording gates (Step 2a)

`check_dry_run_citations.py` over every run_id this artifact cites -- 642, 642a, 642b, 642c:
**0 dry cited, 0 dry in named families, 0 ambiguous, 4 clean, exit 0.** The target manifest carries
`dry_run: false`. `excluded_dry_run_ids: []`.

`ree-v3/validate_recording.py` on the target manifest: **complete, 0 always-core gaps, 0 thin-pack
provenance drops.** `recording_schema: rec/v1`, `substrate_hash 52ceaa7c...`,
`substrate_commit 8149d3648` (dirty on one unrelated path,
`experiments/_lib/baselines/arc019_curriculum_gating.py`), `substrate_stable_across_run: true`,
`machine ree-cloud-4`, `machine_class linux-x86_64-py3.10-torch2.12.0+cpu`,
`elapsed_seconds 1283.0`, `seeds [42, 43, 44]`. **There is no recording debt in this run.**

### 1b. Design

Same protocol, environment, seeds, arms, budgets, P0a/P0b warmups, readiness gate, C0 and C3 as
642a/642b, inheriting the `CALIBRATION_CONFIG` under validation verbatim. The **sole causal change
is the readout**: 642b's C1/C2 read `z_block_peak`, a max against a hard clamp
(`z_block_cap = 1.5`), which both arms touched on all 3 seeds, making the peak separation exactly
`0.000` and C1/C2 false *by arithmetic*. C1/C2 now read `z_block_mean`.

Environment: `CausalGridWorldV2`, size 8, toroidal, **`num_hazards = 0`**, `num_resources = 0`,
`block_interval = 2` at prob 1.0. `z_goal` pinned at 0.5 via `base._pin_goal()` (a deliberate
control, correctly stamped `goal_pinned: true` this time so `writer_defect` reads `null`).

### 1c. Criteria and what each actually measured

| Criterion | Formula | Seeds passing | Non-degenerate? |
|---|---|---|---|
| C0 detector readiness | BLOCK-arm `blocked_step_mismatch_mean - free_step_mismatch_mean >= 0.10` | 3/3 (0.601 / 0.547 / 0.498) | **yes**, but see 1d |
| C1 z_block rises | `z_block_mean(BLOCK) - z_block_mean(CONTROL) >= 0.30` AND `z_block_mean(BLOCK) >= 0.30` | 3/3 | **yes** |
| C2 dissociation from z_harm_a | `(z_block_sep - z_harm_a_sep) >= 0.30` | 3/3 | **NO** (flagged) |
| C3 assert-not-withdraw | `no_withdraw AND assert_sig AND no_suffering` | 3/3 | **NO -- inert AND mis-specified** (unflagged; see 2b) |

`overall_pass = C0 AND C1 AND C2 AND C3` on `>= 2/3` readiness-cleared seeds. `n_ready_seeds 3`,
`seeds_needed 2`, `n_seeds_skipped_not_ready 0`, `seed_base_sufficient true`.

**This autopsy adjudicates `criteria_non_degenerate` as `{C0: true, C1: true, C2: false, C3: false}`.**
The manifest records only `C2: false`; C3 is added here on red-team F3 (section 2b). Governance may
record a `c3_degeneracy_note` sibling at its discretion -- the overall PASS stands and this autopsy
does not ask for the manifest to be rewritten.

**Headroom DV, per seed** (`headroom_dv_diagnostics`):

| Seed | BLOCK mean | CONTROL mean | separation | BLOCK peak | CONTROL peak | peak sep | BLOCK sat. | CONTROL sat. |
|---|---|---|---|---|---|---|---|---|
| 42 | 0.8119 | 0.1313 | **0.6805** | 1.500 | 1.500 | 0.000 | 0.276 | 0.0058 |
| 43 | 0.7671 | 0.1768 | **0.5904** | 1.500 | 1.500 | 0.000 | 0.346 | 0.0513 |
| 44 | 0.8345 | 0.0636 | **0.7709** | 1.500 | 1.500 | 0.000 | 0.398 | 0.0200 |

Both `dv_headroom` preconditions met: `c1_mean_elevation_headroom_prior` 1.3232 and
`c1_mean_elevation_headroom_measured` 1.3232, each against a 0.60 requirement (margin 2.0). All
six `readiness` preconditions met (`c0_probe_margin` 0.6241/0.5322/0.5077 vs floor 0.10;
`zworld_world_encoder_trained` moved 4/4 world-encoder tensors on every seed).

### 1d. Expected vs observed

**Expected:** if the calibration works, the BLOCK arm's `z_block` integrator sits materially above
the CONTROL arm's on a statistic with room to move. **Observed:** exactly that -- separations
0.59-0.77 against a 0.30 bar, with CONTROL means 0.064-0.177 of a 1.5 cap (down from 1.26-1.35
under 642a's legacy absolute floor). No criterion failed.

**The bar is not fitted, and this matters.** The rule (`every margin = 20% of Z_BLOCK_CAP`) is a
range-fraction stated *before* the predecessor separations were consulted; it is *stricter* than
the 0.20 it replaces (13.3% of the same cap). And its discriminating power was verified by
**replay** over the two predecessor manifests' recorded per-seed arm dicts:

| Regime | mean separations | `_evaluate_seed` verdict |
|---|---|---|
| 642a, legacy absolute floor | 0.1650 / 0.1214 / 0.0831 | C0 T, **C1 F**, C2 F, C3 T -> FAIL 3/3 |
| 642b, calibrated floor | 0.6805 / 0.5904 / 0.7709 | C0 T, **C1 T**, C2 T, C3 T -> PASS 3/3 |

So the criterion rejects the regime the calibration was built to fix and accepts the fixed one.
Neither row is evidence *for* the calibration (642b's data cannot validate 642b), but together
they establish C1 as neither vacuous nor unmeetable. **This is the strongest methodological work in
the family and it is directly answering `failure_autopsy_V3-EXQ-642b` learning 2.**

**But note the ordering point about C0.** C0 also passed 3/3 under the *un-calibrated* 642a regime.
It is a genuine, non-degenerate readiness gate -- it is not evidence for the build under test.
**The PASS's discriminating content rests on C1, alone.**

---

## 2. The adjudication flag -- UPHELD, and broadened

### 2a. C2 is vacuous, exactly as the driver says

`ENV_KWARGS` pins `num_hazards = 0`, so `z_harm_a_mean` is `0.0` in **both arms on all three
seeds** and `z_harm_a_separation` is exactly `0.000`. C2's subtraction is inert:
`(z_block_sep - 0) >= 0.30` **is** C1's first conjunct. C1 therefore *implies* C2 (pre-run red-team F3 --
not to be confused with the Step 7c F3 in 2b-i below),
the grid's `z_block_tracks_z_harm_a_not_dissociated` branch is unreachable, and C2 contributes
**zero** independent confirmation. The driver records this honestly in
`interpretation.c2_degeneracy_reason`, citing V3-EXQ-981 learning 5. Nothing to correct.

### 2b. C3 carries the SAME degeneracy, and it was not flagged

`C3 = no_withdraw AND assert_sig AND no_suffering`, with

```
no_suffering = block["z_harm_a_mean_policy"] <= control["z_harm_a_mean_policy"] + C3_EPS
```

Measured on every seed: `0.0 <= 0.0 + 0.02`. **Trivially true, by the same `num_hazards=0`
construction that made C2 inert.** It is not flagged anywhere in the manifest.

And the surviving conjunct is thin. `assert_sig` is a **zero-margin strict inequality**
(inherited from 642a and deliberately left alone per the 642b gate's "keep C0 and C3 as they
stand"):

| Seed | BLOCK action_rate | CONTROL action_rate | BLOCK alt_switch | CONTROL alt_switch | passes via | margin |
|---|---|---|---|---|---|---|
| 42 | 0.96208 | 0.96042 | 0.00750 | 0.00583 | action_rate | **4 steps / 2400** |
| 43 | 0.99667 | 0.99042 | 0.01625 | 0.02000 | action_rate | **15 steps / 2400** |
| 44 | 1.00000 | 1.00000 | 0.03792 | 0.02792 | alt_switch | **24 steps / 2400** |

Note also (red-team H4) that **seed 43 passes C3 only via `action_rate`, while its `alt_switch`
goes the WRONG way** -- 0.01625 block vs 0.02000 control, i.e. `-9/2400`. The alt-switch signature
that the fan-out's drive probe expects to be *elevated* is, on one of three seeds, depressed.

The pre-run red-team F7 additionally records that C3's rates are **arm-order confounded**: both arms
of a seed run sequentially on one agent, ARM_BLOCK first, and while `agent.reset()` nulls
`blocked_agency._baseline_mismatch_ema` per episode (so C1 is clean), residue and hippocampal
state are *not* reset, so ARM_CONTROL's policy runs on an agent carrying ARM_BLOCK's history.

#### 2b-i. The decisive defect: `withdraw` is unrepresentable (Step 7c red-team F3)

The margins and the order confound above are real, and they are **not the problem**. C3's surviving
conjuncts are not thin -- they are **measuring the wrong quantity**:

- `experiments/v3_exq_642a_blocked_agency_zblock_discriminative.py:252` sets **`action_dim=4`**.
- `ree_core/utils/config.py:5608` (and `:7676`) default **`blocked_agency_noop_class: int = 0`**,
  and the driver's `CFG_KWARGS` never overrides it.
- `ree_core/environment/causal_grid_world.py:113-115` -- `ACTIONS = {0:(-1,0), 1:(1,0), 2:(0,-1),
  3:(0,1), 4:(0,0)}`. **Index 0 is a MOVE (up). The stay action is index 4**, which a 4-dim policy
  can never emit.

So `action_rate = n_action / n_total` where `n_action` counts `cls != noop_class` is literally
*"fraction of steps whose argmax is not move-up"*. **A withdraw (passivity) signature has no
representation in the action space at all**, and `no_withdraw` / `assert_sig` compare move-up
frequency between arms. The consumer inherits the identical miswire: `blocked_agency.py:426`
--- `if cls_i == c.noop_class: vals.append(passive_term)` --- gives the ASSERT score-bias's
*passive* term to move-up, penalising it and favouring the other three moves.

**C3 is therefore UNINFORMATIVE about the assert-vs-withdraw contrast, not weakly informative** --
and this is an experiment-**configuration** defect (the knob exists and is settable), inherited
unchanged across V3-EXQ-642 / 642a / 642b / 642c, through a pre-run red-team and three prior
autopsies. It is also *prior* to the capacity argument in section 3: withdraw could not have been
instantiated in this bed even if capacity-belief HAD been challenged.

**So: three of four load-bearing criteria carry an inert or mis-specified leg, and the fourth is a
readiness gate that passes in both regimes.** The PASS does not rest *wholly* on a degenerate
criterion -- C1 is live and discriminating -- but it rests on **fewer independent legs than the
criteria list implies**, and the degeneracy is a property of the *environment* and the *action
space*, not of C2.

### 2c. A new, unscored finding: the mismatch floor's free-step false-positive rate

This is the strongest result in the manifest that nobody computed. The run records, per arm per
seed, **both** the detector's own classification count (`n_external_block_ticks`, incremented on
`external_block_this_tick`) and the environment's ground truth (`n_blocked_steps`, from
`inf["action_blocked_this_step"]`). Nothing compares them. *Read the arithmetic first and the
attribution second* -- the numbers below are right, and the draft's reading of **which computation**
produced them was not (see the correction beneath the table).

| Seed | CONTROL blocked steps | CONTROL detector fires | **false-positive rate** | BLOCK blocked steps | BLOCK detector fires | fires / blocked steps |
|---|---|---|---|---|---|---|
| 42 | **0** / 2400 | 357 | **14.9%** | 1179 / 2400 | 867 | 73.5% |
| 43 | **0** / 2400 | 362 | **15.1%** | 1183 / 2400 | 933 | 78.9% |
| 44 | **0** / 2400 | 147 | **6.1%** | 1180 / 2400 | 1068 | 90.5% |

The right-hand column is an **upper bound** on recall, because some block-arm fires certainly land
on that arm's ~1220 free steps. If the control-arm false-positive rate transfers to those free
steps -- an *assumption*, not a measurement -- true-positive recall is nearer **58-84%**. That
assumption is load-bearing and cannot be discharged from this run: only **counts** were recorded,
never per-tick series, so the block arm's 867 fires against 1179 blocked and 1221 free steps cannot
be split into TP/FP at any cost (see 7d).

**The draft attributed this to the external-attribution gate. That is wrong (red-team F2), and the
correction matters because it changes what the substrate_queue entry should say.** The predicate is

```
external_block = (not baseline_seeded_this_tick and goal_ok
                  and mism >= effective_floor
                  and motor >= c.attribution_motor_floor)     # blocked_agency.py:318-323
```

and the module docstring names the **ATTRIBUTION** gate as the `motor >= floor` clause specifically.
That clause **never discriminated in this run**: `motor_gate_shut_frac` is `0.0` in *both* arms on
3/3 seeds and `motor_agency_min` is 0.736-0.742 against a floor of 0.5, so it was **TRUE on all
14400 measured ticks** -- it removed nothing, admitted nothing, and is **inert**. With the goal
pinned active and baseline seeding excluded, the only clause that can be False on a control-arm tick
is `mism >= effective_floor`.

So every one of the 357 / 362 / 147 ARM_CONTROL fires is a **free step whose `outcome_mismatch`
crossed the 1.5x-EMA floor**: `free_step_mismatch_mean` 0.384 / 0.462 / 0.493 against
`effective_mismatch_floor_mean` 0.701 / 0.775 / 0.893 -- the tail of the free-step mismatch
distribution crosses the floor 6-15% of the time. The correct name for this finding is the
**baseline-relative mismatch-floor free-step false-positive rate**, which is *this substrate_queue
entry's own subject*.

**And it is not a new defect -- it is the tick-level form of one already on the record.** Runs of
consecutive free-step crossings are exactly what drives the CONTROL arm's `z_block` transiently to
the 1.5 cap, which is the residual the entry's `severity_note` already carries ("CONTROL
`z_block_peak` still reaches 1.500 on 3/3 seeds") and the driver already describes
(`headroom_dv_diagnostics.note`: "this run does NOT close that entry"). Same defect, newly visible
one level down.

**This does not undermine C1** -- the aggregate contrast (36-45% of block-arm ticks vs 6-15% of
control-arm ticks) survives comfortably. What it *does* mean is that any future experiment or claim
reading `z_block` or `external_block_this_tick` as evidence that a block *occurred* inherits an
unsignalled 6-15% base-rate contamination. **It is NOT evidence for H2**: the FP rate says something
about the *floor*, not about the attribution clause's permissiveness, which was never exercised at
all. The draft's H2-support sentence is withdrawn, and H1-vs-H2 is **untouched** by this run.

Also recorded, as a hygiene note: `n_external_block_ticks` (a driver-side run total) and
`n_external_blocks_counter` (from `blocked_agency.get_state()`) sit **side by side in the same
per-arm dict** and are not commensurable. Seed 44 ARM_BLOCK reads `1068` and `0`. Precisely
(red-team H3): `reset()` zeroes `_n_external_blocks` (`blocked_agency.py:456`) and the loop calls
`agent.reset()` on env-done, so the counter reports **ticks since the last env-done** -- not
necessarily an episode boundary; the observed 34 / 56 / 0 are not "final episode" totals of ~60.

---

## 3. Claim layer -- may governance clear MECH-353's `v3_pending`?

**Held -- by user decision at the Step 8 gate, 2026-09-05, and recorded as a governance JUDGMENT
rather than a forced reading of the claim text.** The draft asserted that "the claim's release
condition is not a matter of interpretation". Red-team F1 shows that was wrong, and the correction
is kept here rather than smoothed away. MECH-353's own `evidence_quality_note` reads, verbatim:

> `v3_pending=true` until the smallest-V3 blocked-action discriminative experiment lands (env
> repeatedly blocks an intended predicted-to-succeed action, harm + goal held constant; measure
> **assert-vs-withdraw dissociation from `z_harm_a` under matched controllability**).

and its `functional_restatement` falsifier repeats it: the substrate should produce an assert /
persist response "**behaviourally distinct from the suffering withdraw signature**", and `z_block`
should "**dissociate from `z_harm_a` under a matched controllability manipulation**".

and its `implementation_note` names the release **run**:

> `v3_pending` remains TRUE **until the post-build blocked-action discriminative validation,
> V3-EXQ-642b, passes**; its wrapper is claimless and forces `evidence_direction=non_contributory`.

**The reading that says "clear it".** *"Harm + goal held constant"* is the claim's own instruction,
so a hazard-free bed is not per se disqualifying -- and the draft's original "leg A requires
`z_harm_a` to be free to vary (`num_hazards > 0`)" **inverted the clause it quoted**. The phrases
"free to vary" and "`num_hazards`" appear nowhere in the claim. 642c `supersedes` V3-EXQ-642b and
PASSes. A fair reader could call this run the release. The driver itself hedged in that direction
(`manifest.notes`: "PASS ... permits governance to consider clearing MECH-353 `v3_pending`; this run
does not clear it itself").

**The reading the user took, and why.** The clause's *operative content* is an assert-vs-withdraw
dissociation -- and **that has never been measurable anywhere in this family**, because withdraw is
unrepresentable (section 2b-i: `action_dim=4`, `blocked_agency_noop_class=0` -> MOVE-UP, stay is the
unreachable index 4). C3's `action_rate` has always scored *"fraction of steps not choosing
move-up"*. So the claim's own named release run **has not yet been validly run at all**, whatever
its verdict. On that ground the user held `v3_pending` and routed **V3-EXQ-642d with withdraw
representable**.

Two supporting facts, stated with their correct cells this time:

- **`z_harm_a` is pinned.** With `num_hazards = 0` it is 0.0 in both arms, so C2's subtraction is
  algebraically inert and C3's `no_suffering` conjunct is trivially true. A dissociation in which
  only one signal *can* move does not distinguish "`z_block` is a distinct stream" from "`z_harm_a`
  is disabled".
- **Capacity-belief was never challenged -- but cite the right gate (red-team H1).**
  `capacity_belief = 1 - capacity_collapse_weight * ||z_harm_a||` (`agent.py:4209-4214`, named at
  `agent.py:4022-4023`), so it is pinned at 1.0 by `z_harm_a = 0`. The draft cited
  `motor_gate_shut_frac` / `motor_agency` for this, which feed the **ATTRIBUTION** gate -- a
  different gate, and the same conflation that produced the mis-located finding in 2c.

And the falsifier's second half -- "if blocked-action behaviour is **fully explained by existing
harm + suffering + decommit machinery**, the claim is falsified" -- cannot be evaluated in an
environment with no harm and no suffering machinery in play.

**So: the hold is defensible and is recorded as a judgment.** What is *not* a matter of judgment is
that C3 could never have measured the contrast the clause names.

### 3a. What this run *is* worth to MECH-353

Substantial, and it should be written down rather than lost in a "does not clear" verdict. The run
establishes the **detector-readiness half**: `z_block` rises under external blocking, on a trained
encoder (SD-070) and a trained action-conditional world-forward (SD-056), at a bar that provably
rejects the un-calibrated regime. That is a real precondition for both legs above, discharged. It
is why the recommended `evidence_quality_note` (section 9) leads with the validation and *then*
states what remains.

### 3b. The other nine `bears_on` claims -- read across, not adjudicated

- **SD-029** is the single-pass comparator on the **z_harm_s reafferent** stream. MECH-353's
  detector is that comparator *form* applied to the action-outcome / `z_world` channel, which is
  **SD-031**. With `num_hazards = 0` there is no z_harm_s traffic at all, so SD-029's own stream
  was never exercised -- a peripheral co-tag. Its stored `epistemic_category: substrate_ceiling`
  is neither supported nor disturbed here.
- **SD-070, SD-056** were exercised and are clean, **as readiness preconditions, not as scoring
  evidence**. Deliberately not written as per-claim `supports`: the run is claimless and forces
  `non_contributory` precisely so a wrapper cannot move claim confidence through inherited
  metadata.
- **MECH-112** -- `z_goal` was *pinned* as a deliberate control. A pinned goal cannot test a claim
  about a structured goal representation.
- **MECH-320, MECH-342, ARC-016** are MECH-353's **consumers** (vigor, decommit release,
  commitment threshold). This run measured the detector; no consumer DV appears in the criteria.
- **SD-011, SD-019b** are the claims the dissociation is *from*. That they could not be exercised
  is the finding -- recorded against MECH-353's release condition, not against them.

---

## 4. Biological-reference triage

Closest mechanism: **frustrative non-reward / Panksepp RAGE assert-pole** -- a comparator on
expected-minus-obtained action outcome, firing *without* noxious input, driving assertion and
effort escalation rather than withdrawal.

`lit_status: **present**` and adequate:
`evidence/literature/targeted_review_blocked_agency_anger_stream/VERDICT.md`, 5 entries, all
supports (Papini et al. 2024 *J Neurosci*; Davis & Montag 2019 *Front Neurosci*; Bertsch et al.
2020 *Curr Psychiatry Rep*; Carruthers 2012 *Conscious Cogn* as the comparator anchor). **No
`/lit-pull` is owed.**

`is_formal_import: false`. The detector is a **single-pass** comparator, which is the
biologically-evidenced form (Carruthers) -- this family does **not** repeat the SD-003 two-pass
counterfactual error.

The divergence that *is* live is one of **scope, not mechanism**, and it is what makes the
environment gap load-bearing rather than a caveat: the biology defines FNR precisely by the
**absence** of noxious input. That makes a hazard-free grid a faithful instantiation of the
*antecedent* -- and an inadequate test of the *dissociation-from-nociception predicate* the claim
registers as its falsifier. The environment is right for the substrate question and wrong for the
claim question, and it is the same config line that makes it both.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **n/a** | claim-free (`claim_ids: []`), `non_contributory` forced. Read-across: MECH-353's detector half strengthened; its dissociation half untested -- neither supported nor weakened. |
| Biological reference | **clear** | FNR / RAGE assert pole; lit present (5 entries, all supports); single-pass comparator, no formal-import divergence. |
| Prerequisites | **present** | SD-070 P0a moved 4/4 world-encoder tensors 3/3 seeds; SD-056 contrastive trained (0.317/0.308/0.196); P0 readiness 3/3 at margins 0.62/0.53/0.51 vs floor 0.10. |
| Implementation completeness | **complete** | Baseline-relative floor (`d49db86f3e64670`) built, landed, effective: CONTROL mean 1.26-1.35 -> 0.064-0.177; separation 0.083-0.165 -> 0.590-0.771. |
| Environment adequacy | **too sparse** (for the claim) | `num_hazards=0` removes the dissociation partner and pins `capacity_belief` (`= 1 - w*||z_harm_a||`, `agent.py:4209`) at 1.0. Prior to that: the withdraw pole is **unrepresentable** (`action_dim=4`, `noop_class=0`), so no capacity manipulation in this bed could have instantiated it. Adequate for the *substrate* question. |
| Measurement adequacy | **partial / under-instrumented** | *Three* of four criteria carry an inert or mis-specified leg; the floor's free-step FP rate recorded but never scored; two incommensurable counters share a dict; only COUNTS were recorded, never per-tick series (`metrics.json` is 53 bytes), so no confusion matrix is derivable at any cost. |
| Integration adequacy | **coupled but partially unverified** | Arms sequential on one agent, ARM_BLOCK first; `blocked_agency` state reset per episode (clean for C1), residue/hippocampal state not (confound for C3). |
| Scale / capacity | **adequate** | 3 seeds x 2 arms x 2400 measured steps; 6/6 runs completed; `seed_base_sufficient true` (the pre-run red-team's F6 realized-n trap did not bite). |

### 5a. Failure-location summary (GOV-FAILLOC-1)

Required even for a PASS. Reading the table above:

| Bucket | Verdict |
|---|---|
| MECHANISM | **established** -- Implementation completeness reads `complete` |
| MEASURES | **not established** -- Measurement adequacy reads `partial` |
| ENVIRONMENT | **not established** -- Environment adequacy reads `too sparse` |
| REE | **false** -- not reachable, and not asserted |

**Net classification -- a chargeability read, not a failure read.** The result **is chargeable to
the SUBSTRATE** on the calibration question: implementation reads complete, C1 is non-degenerate,
and the a-priori 0.30 bar demonstrably discriminates 642a's regime from 642b's, so the PASS is
attributable to the built lever rather than to an implementation or measurement artefact. It is
**not chargeable as a MECH-353 claim validation**: Measurement and Environment each independently
read inadequate for the claim's own falsifier -- and the Measurement inadequacy is now known to be
structural (the action space cannot express the contrast C3 names), not a matter of thin margins. Nothing failed, so `REE FAILED` would be both
unreachable and the wrong frame.

---

## 6. Cluster

**Single-target scope.** V3-EXQ-642 / 642a / 642b are *predecessors*, each already
autopsied and confirmed, not co-members of a convergent-shape cluster. They are read here as the
lineage this run supersedes.

Worth stating as lineage, though: **each letter has been consumed by a different measurement
defect, none by a substrate failure** -- 642 by an untrained encoder (prerequisite), 642a by an
absolute mismatch floor below the free-step baseline (calibration), 642b by a peak statistic
against a hard clamp (statistic choice), and 642c by an environment that pins the criterion's
comparison variable (environment). That is a four-deep chain of instrument problems around a
mechanism that, on this evidence, works. The lesson is not that the family is cursed; it is that
**the measurement design has never been checked against the claim's own release condition before
the run** -- which is learning 2 in section 8, and whose action-space sibling (learning 7) is the
defect that had survived all four letters undetected.

---

## 7. Repair pathway, work-graph class and routing

**Work-graph node class: `complex (probe-gated)` / `puzzle (known rules)`.**

The frame is well posed -- everyone agrees what a dissociation test looks like, and
`CausalGridWorldV2` already supports hazards -- and what is missing is a **fact**: does `z_block`
dissociate from `z_harm_a` when `z_harm_a` can vary, and is the elevation attributable to the
external-attribution gate rather than to generic outcome mismatch? A puzzle routes to a **spike**,
i.e. `/queue-experiment` a diagnostic.

It is **not** `complicated (buildable)`: the substrate is built and a build is the wrong
instrument. It is **not** `mystery (known data)`: the settling data does not exist -- this run's
environment could not produce it.

### 7a. Routing: `/queue-experiment`, **one item now** (the second is deferred)

**V3-EXQ-642d -- same-question successor, alphabetic suffix.** The scientific question is unchanged;
what is repaired is an experiment **configuration** defect. **All six spec items are required**, and
(1) is prior to the rest -- without it C3 stays vacuous a fifth time no matter what margin it is
given:

1. **`action_dim=5` with `blocked_agency_noop_class=4`** (or an explicit no-op arm), so **withdraw
   is expressible at all**. This is the repair for the defect inherited across 642/642a/642b/642c
   (section 2b-i), in which `action_rate` scored "fraction of steps not choosing move-up" and
   `blocked_agency.py:426` handed the ASSERT bias's *passive* term to move-up.
2. **An arm with `num_hazards > 0`**, so `z_harm_a` is free to vary -- making C2's subtraction and
   C3's `no_suffering` conjunct live for the first time in the family. This is the H3 probe.
3. **A per-tick `external_block` / `action_blocked` flag SERIES recorded to the run pack.** 642c
   emits only scalar counts (its `metrics.json` is 53 bytes), so the confusion matrix and the
   floor's free-step FP rate are measurable rather than assumed -- and the provisional `<= 2%` bar
   can finally be *derived* instead of invented.
4. **A third arm with SELF-attributable move cancellation** (motor noise / execution failure). This
   is the H1-vs-H2 discriminator, and the only arm that pushes `motor_agency` below the 0.5
   attribution floor -- i.e. the only design in which the attribution clause is exercised at all.
5. **C3 with a pre-registered non-zero margin and counterbalanced arm order.** 642c's C3 passed on
   4-24 steps out of 2400 with a zero-margin strict inequality, ARM_BLOCK always first, and on seed
   43 its `alt_switch` went the wrong way.
6. **Re-key `criteria_non_degenerate` on EVERY criterion leg that reads a structurally pinned
   variable**, not only C2.

*Nothing here is free.* The draft claimed half of (3) was zero-compute reanalysis; it is not --
642c recorded **counts, not series** (section 7d).

**DEFERRED -- a NEW EXQ number (not a 642 letter) for the assert-vs-withdraw capacity-collapse
contrast.** A capacity-collapse manipulation (SD-019b / Q-036 escapability) under a matched block
schedule, so both poles are instantiated in one design, closing leg B of the release condition.
**Do not queue it yet.** Running a capacity-collapse design onto an action space in which passivity
has no representation would repeat the family's configuration defect at greater cost and produce a
fifth vacuous C3. Revisit once 642d's item (1) is verified in a real run.

### 7b. Explicitly NOT routed

- **NOT `/implement-substrate`.** The substrate is built and this run validates it. The re-derive
  brake does not fire.
- **NOT `/lit-pull`.** The anchor is present and adequate; the mechanism is not a formal import.
- **NOT `/claim-synthesis`.** See 7d.
- **NOT governance-demotion.** Nothing weakens MECH-353. The verdict is that its falsifier has not
  yet been run -- which is the opposite of a demotion case.

### 7c. Re-derive brake and granularity trigger

**Brake: does NOT fire.** R1-R3 counting convention run over every confirmed
`failure_autopsy_*.json` at 2026-09-05T02:38:25Z: **MECH-353 ceiling hits = 0**. All four targets
in this family carry `claim_ids: []`, so none counts against any claim. This reading is not
`substrate_ceiling` and adds no hit. The successor recommended above is a **different test**, not
another letter circling a ceiling, so the refusal clause does not apply.

**Granularity-debt trigger: does NOT fire.**
`granularity_debt_cluster.py MECH-353` -> **0 tagging targets across 0 files**. No target in this
family reads `claim_alignment: weakened`; the recurrence is measurement and environment debt, not
granularity debt.

**But that zero is itself a finding for governance.** Four autopsies have now adjudicated
MECH-353's validation path and **not one is visible to GOV-GRAN-1 or GOV-CEIL-1**, because all four
are claim-free and 642a and 642b both left `per_claim_recommendation` as `{}`. This artifact is the
first in the family to fill it -- which is also the only channel by which GOV-APPLY-1 can ever see
this disposition, since a re-adjudicated run is absent from `pending_review.md`.

### 7d. GOV-FANOUT-1 -- fan out, do not re-pose

Three live hypotheses, on three distinct design axes, each with a declared null:

| id | hypothesis | axis | probe | declared null |
|---|---|---|---|---|
| **H1** | The separation is the **external-attribution gate** correctly selecting externally-cancelled steps -- MECH-353's claimed computation. | process | **The self-attributable-cancellation arm inside 642d** (item 4). The confusion matrix is a supporting readout, not the discriminator. | The self-attributable arm's `z_block_mean` is indistinguishable from ARM_BLOCK's. |
| **H2** | The separation is **generic outcome mismatch**; the attribution gate is not load-bearing and `z_block` is a relabelled surprise signal. | process | (same arm -- H1 and H2 are the two verdicts of it) | (mirror of H1's) |
| **H3** | With `z_harm_a` free to vary, `z_block` **co-varies** with it rather than dissociating -- the distinctness predicate fails. | world | **The hazards arm inside 642d** (item 2), goal value and block schedule fixed. | `z_block` and `z_harm_a` separations are proportional across seeds. |

H2 is not a strawman: the pre-run red-team F2 concedes the design "cannot separate external block
from move cancelled by any means".

**But the fan-out has to be collapsed honestly (Step 7c red-team F5), and two claims the draft made
here are withdrawn.** (a) Section 2c's 6-15% control-arm firing rate is **not** evidence that the
attribution gate is permissive -- the attribution clause was true on all 14400 ticks and never
discriminated, so the FP rate is about the *floor* (section 2c). **H1-vs-H2 is untouched by this
run.** (b) The confusion matrix is **not** free reanalysis: 642c stored `n_external_block_ticks` as
a scalar and `n_blocked_steps` as a length, with no per-tick list kept or emitted (`metrics.json` is
53 bytes). The ARM_CONTROL rate is derivable *only* because its ground truth is exactly zero; in
ARM_BLOCK, 867 fires against 1179 blocked and 1221 free steps cannot be split into TP/FP at any
cost. And even a complete matrix would not separate H1 from H2 in a design with no self-attributable
cancellations -- both predict firing on externally cancelled moves.

**So the portfolio is: one build now (642d, carrying the hazards arm, the self-attributable arm, and
the action-space repair), plus one deferred build (the capacity-collapse contrast).** Still
explicitly not a power-bump -- 642c's own criteria are already met, and more seeds of the same
environment would answer none of H1-H3.

### 7e. Mechanical pre-routing checks (Step 7b)

`autopsy_pre_routing_checks.py --artifact ... --json` -> **`fire_count: 0`**.

`inapplicable`: **C1, C2, C3** (claim-keyed; the target carries `claim_ids: []`), **C5**, **C7**.

**`inapplicable` is not "no fire".** Three of the five checks are structurally blind on a
claim-free target, and per the skill that means **Step 7c carries the whole load there**. In the
staged draft Step 7c had not been run, and that was flagged as the artifact's single largest
residual risk. **It has since been run** (2026-09-05, `fable-5.1`, cross-model, CONTESTED) and the
risk was real: F3 alone -- an unrepresentable withdraw pole inherited across four letters -- was
missed by every mechanical check, by three prior autopsies, and by the run's own pre-run design
review. Full record in section 11.

---

## 8. Learning extracted

1. **A criterion degeneracy caused by a pinned ENVIRONMENT VARIABLE is a property of the
   environment, not of the criterion -- so sweep every criterion leg that reads that variable, not
   just the one that made it obvious.** 642c correctly flagged C2 because `num_hazards=0` zeroes
   the `z_harm_a` separation, and missed that the same pin makes C3's `no_suffering` conjunct
   (`0.0 <= 0.0 + 0.02`) trivially true. The discipline exists in the very same file: pre-run red-team F8
   re-keyed C1/C2/C3 non-degeneracy off the clamp-pinned *peak* onto `z_block_mean`. It was applied
   to the pinned **statistic** and not to the pinned **variable**.

2. **Check a claim's `v3_pending` release condition clause by clause against the validating run's
   environment CONFIG -- before the run, not against its outcome afterwards.** MECH-353's condition
   names a dissociation from `z_harm_a` under matched controllability; the validating environment
   pins the dissociation partner to zero and never challenges capacity. A PASS on such a run can
   validate the substrate lever and still be *structurally unable* to release the claim -- and this
   run's own self-route label said `clear_v3_pending`.

3. **Recording two series is not the same as scoring the relation between them.** 642c recorded
   both the detector's classification count and the environment's ground-truth blocked-step count,
   per arm per seed, and nothing compared them -- yielding the strongest unscored result in the
   manifest. This is the *mirror image* of a recording gap: the readout was recorded and the
   analysis was never specified.

4. **Two same-named counters in one manifest dict can be measured over different windows.**
   `n_external_block_ticks` is a run total; `n_external_blocks_counter` comes from `get_state()`,
   and `reset()` zeroes `_n_external_blocks` (`blocked_agency.py:456`) while the loop calls
   `agent.reset()` on env-done -- so it reports **ticks since the last env-done**, which is not
   necessarily an episode boundary (the observed 34 / 56 / 0 are not "final episode" totals of ~60).
   Seed 44 ARM_BLOCK reads `1068` and `0` side by side. Name the window in the key, or emit one.

5. **POSITIVE -- the template worth reusing.** When a statistic change forces a threshold to be
   re-derived, the anti-fabrication-safe pattern is: (a) state an a-priori derivation rule *in the
   DV's own units* before looking at any observed separation; (b) verify it lands somewhere useful
   by **replaying** the criterion over the recorded per-seed cells of two predecessor manifests
   spanning the regimes you want discriminated; (c) gate feasibility with a `dv_headroom`
   precondition so a starved criterion self-routes `substrate_not_ready_requeue` instead of
   recording a falsification. This produced a bar *stricter* than the one it replaced and
   *demonstrably discriminating*, with zero threshold fitting. It is the direct answer to
   `failure_autopsy_V3-EXQ-642b` learning 2 and should be cited as precedent.

6. **A well-derived aggregate criterion can pass cleanly while the per-tick mechanism underneath it
   is noisy.** C1's separation is comfortable and real; the floor producing it fires on 6-15% of
   free steps in an arm with zero blocks. Neither number contradicts the other, and only the first
   was scored. **When a claim's distinctive content is an ATTRIBUTION, the load-bearing readout is a
   confusion matrix, not a group-mean separation** -- and see learning 8 for why "we recorded both
   numbers" did not make that matrix available.

7. **An experiment can be structurally unable to measure its own headline contrast, and no
   criterion-level repair will surface it -- check the ACTION SPACE against the behaviour the
   criterion names, at authoring time.** 642 / 642a / 642b / 642c all scored C3 "assert not
   withdraw" at `action_dim=4` while `blocked_agency_noop_class` defaulted to `0`, which
   `CausalGridWorldV2` maps to MOVE-UP; the stay action is index 4 and a 4-dim policy can never emit
   it. So `action_rate` measured "fraction of steps not choosing move-up" and **withdraw had no
   representation at all** -- through four letters, a pre-run red-team, and three prior autopsies,
   none of which caught it. The consumer carried the same miswire (`blocked_agency.py:426` gives the
   ASSERT bias's *passive* term to move-up). This is the **action-space sibling of learning 2's
   environment-config check**: a criterion that names a behaviour must be checked against the space
   that behaviour would have to be expressed in, before the run.

8. **Counts are not series, and "we already recorded both numbers" is not "the relation is
   derivable".** Learning 3 says recording two series is not the same as scoring their relation. The
   sharper form: 642c recorded two **counts**, never two **series**, so the block-arm confusion
   matrix is not derivable at *any* compute cost -- only the control-arm FP rate is, and only
   because its ground-truth count is exactly zero. A "reanalysis is free" claim inside a routing
   recommendation must be checked against what is actually on disk (here: a 53-byte `metrics.json`),
   not against what the driver appears to have measured.

---

## 9. What governance should write

### 9a. Manifest disposition

| Field | Recommendation |
|---|---|
| `evidence_direction` | **`non_contributory` STANDS**, unchanged -- claim-free by design; the driver forces it on every outcome. |
| `evidence_direction_note` | **Stands as written.** |
| `epistemic_category` | **`standard`** -- see 9b. |
| `vacuous_pass` flag | **UPHELD and BROADENED.** Preserve the manifest's honest record of it. This autopsy adjudicates `criteria_non_degenerate` as `{C0:true, C1:true, C2:false, C3:false}`. Optional addition at governance's discretion: a `c3_degeneracy_note` sibling recording that C3's `no_suffering` conjunct is inert by the `num_hazards=0` construction **and** that its `no_withdraw`/`assert_sig` legs are mis-specified because withdraw is unrepresentable at `action_dim=4`/`noop_class=0`. The **overall PASS stands**. |
| `interpretation.label` | Record a relabel in the review note from `validated_clear_v3_pending` to **`validated_substrate_calibration_v3_pending_stands`**. The manifest is landed evidence; this autopsy does not ask for it to be rewritten. |
| Withdraw-representable re-validation | **OWED** before `v3_pending` can clear -- not because the PASS is unsound, but because the criterion that tests the claim's registered falsifier could never *express* the contrast it names (`action_dim=4`, `noop_class=0`). A hazard-present arm is owed alongside it, for the `z_harm_a` leg. V3-EXQ-642d carries both. |

### 9b. `epistemic_category` -- `standard`, and why not the alternatives

`standard`. Nothing here asserts MECH-353's answer is gated on **substrate** work: the substrate is
built and this run shows it works. What is owed is an experiment in a richer environment -- the
case the skill says maps to `standard` with the diagnosis in the note fields. Stamping
`substrate_ceiling` or `substrate_conditional` would additionally make MECH-353 **not v3-testable**
(`_claim_v3_testable`) and starve it of experiment lanes at exactly the moment the correct route is
a new experiment lane. MECH-353 currently carries **no `epistemic_category` field at all**, so this
is a real, storable, not-yet-true change.

### 9c. `per_claim_recommendation` -- MECH-353

- `recommended_evidence_direction`: `non_contributory`
- `recommended_epistemic_category`: `standard`
- `recommended_diagnostic_evidence_adjudicated`: **`true`**
- **`pending_retest_after_substrate`: NOT recommended, and dropped from the block (red-team H2).**
  MECH-353 carries *none* of `epistemic_category`, `pending_retest_after_substrate` or
  `diagnostic_evidence_adjudicated` today, so the two recommendations above are **adds**, not sets;
  and there is nothing waiting on a build for a `false` to be *about*, so setting it would be a
  no-op with an unstated premise.
- `status_change`: none -- stays `candidate`
- **`v3_pending`: STAYS TRUE** -- user gate decision 2026-09-05, recorded as a governance judgment
  (section 3), not as a forced reading of the claim text.
- `change` tail ends on `-> epistemic_category: standard` (storable and not yet true)
- **Note text governance writes on the claim:** *"PASS validates the mismatch-floor calibration on
  the headroom DV (C1 0.59-0.77 vs 0.30); `v3_pending` held by user decision 2026-09-05 because
  withdraw was unrepresentable (`action_dim=4`/`noop_class=0`) and `z_harm_a` pinned at 0, so the
  named release run has not validly run; 642d owed."*

### 9d. Draft `evidence_quality_note` -- exact text

> Replacing the trailing `v3_pending` sentence of the existing note; leave the literature paragraph
> above it intact.

```
v3_pending=true STANDS as of 2026-09-05. The blocked-agency SUBSTRATE is now validated:
V3-EXQ-642c (run v3_exq_642c_blocked_agency_headroom_dv_validation_20260904T214459Z_v3, PASS,
claimless, non_contributory) showed the baseline-relative outcome_mismatch floor built in ree-v3
d49db86f3e64670 gives the z_block integrator real dynamic range on a headroom statistic --
BLOCK-minus-CONTROL z_block_mean 0.6805/0.5904/0.7709 on 3/3 seeds against an a-priori 0.30 bar
(20 pct of Z_BLOCK_CAP, derived before the predecessor separations were consulted), where the same
criterion rejects the un-calibrated V3-EXQ-642a regime (0.1650/0.1214/0.0831) on 3/3 seeds. The
detector-readiness precondition passed 3/3 (blocked-minus-free mismatch margins 0.601/0.547/0.498
vs floor 0.10) on a trained encoder (SD-070) and a trained action-conditional world_forward
(SD-056).

That is the detector half, and it does NOT release v3_pending. The claim's own release text reads
"harm + goal held constant" and names "the post-build blocked-action discriminative validation,
V3-EXQ-642b" as the release run, which 642c supersedes and passes -- so a fair reader could call
this the release, and the hold below is a governance JUDGMENT rather than a forced reading. The
judgment rests on this: the assert-vs-withdraw dissociation the clause names has never been
MEASURABLE anywhere in this family. The driver runs at action_dim=4 while blocked_agency_noop_class
defaults to 0, which CausalGridWorldV2 maps to MOVE-UP (the stay action is index 4 and a 4-dim
policy cannot emit it), so C3's action_rate scores "fraction of steps not choosing move-up", the
consumer's ASSERT score-bias treats move-up as the passive option (blocked_agency.py:426), and
WITHDRAW has no representation at all. Separately, num_hazards=0 pins the measured z_harm_a
separation at exactly 0.000 on every seed, so C2's dissociation criterion reduces algebraically to
C1 (recorded as criteria_non_degenerate.C2=false) and C3's no_suffering conjunct (0.0 <= 0.0 + 0.02)
is trivially true, and capacity_belief (= 1 - w*||z_harm_a||) is pinned at 1.0. Three of the four
load-bearing criteria therefore carry an inert or mis-specified leg. The claim's named release run
has not yet been validly run.

One further finding from the run's own recorded cells, correctly located: the BASELINE-RELATIVE
MISMATCH FLOOR has a free-step false-positive rate of 6.1-15.1 pct (357/2400, 362/2400, 147/2400
fires in an arm where zero blocks were applied). This is a FLOOR calibration residual, not an
attribution-gate failure -- the attribution (motor) clause was true on all 14400 ticks and never
discriminated -- and it is the tick-level form of the already-recorded CONTROL-transient residual.
It says nothing about whether the external-attribution computation is load-bearing; that question is
untouched by this run.

Clear v3_pending on a run in which WITHDRAW IS EXPRESSIBLE (action_dim=5 with
blocked_agency_noop_class=4, or an explicit no-op arm) and the assert-vs-withdraw contrast is scored
with a pre-registered non-zero margin and counterbalanced arm order; with a hazards-present arm so
z_harm_a is free to vary and z_block demonstrably separates from it under the same block
manipulation; with a self-attributable-cancellation arm so the external attribution gate is actually
exercised; and with a per-tick series recorded so the detector's confusion matrix against
action_blocked_this_step is measurable rather than assumed. V3-EXQ-642d is specified to carry all
four. Adjudicated in evidence/planning/failure_autopsy_V3-EXQ-642c_2026-09-05.{md,json}.
```

### 9e. `substrate_queue.json` -- `amend`

Target: **`sd_blocked_agency_mismatch_floor_calibration`**.

1. **`resolves_prior_failure_record`: the 642b item -> `resolved`, WITH the caveat verbatim.** The
   resolution note must read **"resolved (per-run demonstration; no generic requirement
   installed)"**. Its target is a **disjunction** -- "*either* give the integrator headroom against
   brief excursions, *or* require every blocked-agency criterion to route on a headroom DV and
   record a per-arm saturation fraction" -- and the *shape* reading is correct. But only the second
   disjunct's **demonstration** half is satisfied, and 642c satisfies it **per-run**, not by an
   installed requirement (red-team F4). What ree-v3 `8e133d26ed` (2026-09-04) landed is an **offer,
   not a requirement**: the `dv_headroom` precondition is **opt-in** (`experiments/_metrics.py:605`,
   "OPT-IN, and byte-identical when not opted into") and the `criterion_exceeds_achievable_range`
   lint is **WARN-only in both modes** (`validate_experiments.py:7906`; the commit states it "never
   hardens the exit code in any mode"). Nothing binds a future blocked-agency driver to a headroom
   DV, and nothing requires a per-arm saturation fraction at all. The draft's "the requirement is
   installed generically, not per-run" is **withdrawn** -- that was the half that would have stopped
   re-litigation, and it is the half that is not true. 642c's own design does the demonstration
   (C1/C2 on `z_block_mean`, two `dv_headroom` preconditions at margin 2.0, saturation fraction
   recorded per arm per seed). The first disjunct -- a substrate change giving headroom against
   transients -- was **offered, never required**, and remains unbuilt; CONTROL still touches 1.500
   on 3/3 seeds. Marking it resolved stops a satisfied disjunction being re-litigated every cycle;
   the caveat is recorded so the resolution is never later read as a generic guarantee.

2. **New `failure_record` item -- RETITLED: the baseline-relative mismatch-floor free-step
   false-positive rate** (section 2c), *not* an attribution-gate specificity defect. Metric: on a
   free step with the goal pinned active, `outcome_mismatch` crosses `effective_mismatch_floor`
   (1.5x EMA) and `external_block_this_tick` fires -- 357/2400, 362/2400, 147/2400 in ARM_CONTROL
   where `n_blocked_steps` is 0; the attribution clause is inert (`motor_gate_shut_frac` 0.0 on
   14400/14400 ticks). **Target: provisional -- control-arm free-step FP rate `<= 2%`, to be derived
   from a per-tick series in 642d.** The 2% bar is not derived from anything in this record
   (red-team H7) and this family's own learning 5 is that thresholds must be derived, not invented;
   642c cannot supply the derivation because no per-tick series exists (`metrics.json` is 53 bytes).

3. **`status` / `status_phase`: NO ADVANCE -- the entry stays as it is.** The draft's advance to
   `validated` is **withdrawn** (red-team F2b): a floor calibration with a measured 6-15% free-step
   FP rate, producing transient cap-hits in a no-block arm, is "validated on the headroom statistic"
   and "still defective on the tick statistic" *at the same time*, and advancing `status_phase` to
   validated while a floor-calibration defect is open on the same entry is internally inconsistent.
   **Recommended instead: add a `validation_record_642c` note** recording what did validate --
   BLOCK-minus-CONTROL `z_block_mean` 0.6805/0.5904/0.7709 against the a-priori 0.30 bar, the same
   criterion rejecting 642a 3/3, two `dv_headroom` preconditions at margin 2.0, saturation fraction
   per arm per seed -- with the scope stated: **what is demonstrated is the FLOOR CALIBRATION on a
   headroom DV, not MECH-353, and not the tick-level specificity.**

4. **`severity`: stays `corrupting`, on its ORIGINAL rationale -- keep both the value AND the
   reason.** The re-basing drafted earlier is **withdrawn** (red-team F4). The entry's exit
   condition reads *"Re-assess to degrading once a headroom-DV **requirement** is in place for this
   substrate"*, and no such requirement exists -- `8e133d26ed` is opt-in plus WARN-only (see item 1),
   so a new author can still write a peak criterion and receive only a WARN. **The exit condition has
   NOT fired**, and the original justification stands unretired.

   What this autopsy adds is not a second corrupting condition but the **mechanism of the recorded
   one, at tick level**: the residual the entry already carries (CONTROL `z_block_peak` reaches
   1.500 on 3/3 seeds) is produced by runs of consecutive free-step crossings of the 1.5x-EMA floor,
   measured here at 6.1-15.1% of control-arm ticks. Same defect, one level down.
   `substrate_paths` unchanged (`ree_core/affect/blocked_agency.py`).

### 9f. Apply checklist

1. **MECH-353** -- apply 9d; **add** `epistemic_category: standard`; **add**
   `diagnostic_evidence_adjudicated: true` (the claim carries neither field today); do **not** set
   `pending_retest_after_substrate` (see 9c); refresh `live_status.evidence.from` to
   `failure_autopsy_V3-EXQ-642c_2026-09-05` (it currently cites
   `failure_autopsy_V3-EXQ-642_2026-06-06`, **three runs stale**). **Leave `v3_pending` TRUE** --
   user gate decision 2026-09-05, recorded as a governance judgment.
2. **`substrate_queue.json`** -- apply 9e (four sub-items). Note that two of them are *withdrawals*
   of what the draft recommended: no status advance, and severity stays corrupting on its
   **original** rationale.
3. **Queue** V3-EXQ-642d with all six spec items (7a). **Do NOT queue the capacity-collapse
   new-number experiment -- it is DEFERRED** until 642d shows withdraw is expressible. *Governance
   chips 642d; this autopsy does not `spawn_task` it.*
4. **`hypothesis_space_registry.v1.json`** -- apply the `hypothesis_space_ledger_pending` block
   (section 10b), then `build_hypothesis_space.py` + `check_hypothesis_space_integrity.py`. It is
   still marked **draft-for-governance**; this confirming session performed no registry write.
5. **`review_tracker.json`** -- mark the run reviewed at the governance walk, not here.

---

## 10. Staging-mode residuals

### 10a. What this draft did NOT do

- **Step 7c adversarial red-team pass -- RUN and DISCHARGED** (2026-09-05, `fable-5.1`,
  cross-model). Verdict **CONTESTED**; F1-F5 and H1-H8 are folded throughout this artifact. All
  four conclusions the draft flagged as most needing attack **moved**: the C3 finding was broadened
  from "second inert leg" to "mis-specified, withdraw unrepresentable" (F3, section 2b-i); the
  specificity finding was **re-located** from the attribution gate to the mismatch floor (F2,
  section 2c); the disjunction-satisfied argument was narrowed to a per-run demonstration (F4,
  9e.1); and the stays-corrupting call was kept but on the **original** rationale, with the
  re-basing withdrawn (F4, 9e.4). Full record in section 11.
- **Step 8 interactive gate -- HELD** (2026-09-05). Both readings of MECH-353's release text were
  put to the user with the claim quoted verbatim. **Decision, binding: hold `v3_pending`; route
  642d with withdraw representable.** Recorded as a governance judgment (section 3).
- **Step 9b registry write -- STILL NOT PERFORMED.** Drafted only, below; governance applies it.
- **No claims.yaml / manifest / `review_tracker` / `substrate_queue` / registry / WORKSPACE_STATE
  edits; no commit; no `spawn_task`; no claims opened by the confirming session either.**

### 10b. `hypothesis_space_ledger_pending` (Step 9b, drafted)

**Still `draft` -- governance applies this block; the confirming session performed no registry
write.** No existing question covers this. The registry holds 50 questions at 2026-09-05T02:38:25Z;
none names MECH-353, `z_block`, blocked-agency, or any V3-EXQ-642 run in its `qid`, `title`,
`claims` or hypotheses. Nearest neighbours are `q086-zharma-calibration-vs-ecological` (Q-086) and
`sd031_causal_signature_shortcut_vs_model` (SD-031, the comparator-on-`z_world` claim MECH-353's
detector instantiates); neither adjudicates these legs and neither should absorb them.

**Growth-restriction check: NOT APPLICABLE.** The gate applies only when a leg attaches to an
already-registered question. This draft opens a **new** `questions[]` entry, which by construction
cannot carry a restriction, so no `fanout_growth_events` / `discovery_growth_events` entry is owed.

**A new question IS warranted**, per Mode A/B: two of the three hypotheses are live rivals this run
could not separate, and the third is the claim's own falsifier the environment could not
instantiate. Freezing the denominator now is what stops a later PASS on one leg being read as
having narrowed a space nobody wrote down.

Draft: `qid: mech353_zblock_attribution_and_dissociation`, `claims: [MECH-353, SD-011, SD-019b]`,
`initial_frozen_count: 4` (= `initial_frozen_count_at_registration`), four hypotheses --

| hid | state | axis | note |
|---|---|---|---|
| `H0-calibration-range` | **`confirmed`** | instrumentation | Resolved by 642c. `control_passed: true`, `non_degenerate: true`, `met_elimination_bar: false` (necessary instrument established, question not closed). `self_route_label` recorded as **`validated_substrate_calibration_v3_pending_stands`** (red-team H8 -- not the un-relabelled `validated_clear_v3_pending` the draft carried). `pre_registered_utc = resolved_utc = 2026-09-04T21:44:59Z` (Mode B same-cycle resolve on a new question). |
| `H1-attributional` | `alive` | process | Adjudicating run: **the SELF-ATTRIBUTABLE-cancellation arm inside V3-EXQ-642d** -- not 642d's main hazards contrast, and not the confusion matrix alone. Untouched by 642c. |
| `H2-generic-mismatch` | `alive` | process | Adjudicating run: **the same self-attributable arm.** The draft's "partially supported by 642c's control-arm FP rate" is withdrawn (red-team F2c). |
| `H3-harm-confounded` | `alive` | world | Adjudicating run: **the HAZARDS arm inside V3-EXQ-642d**. Wholly untested -- no observation in the space bears on it. |

**A fourth candidate leg was considered and deliberately NOT registered as a hypothesis.** The
withdraw-unrepresentable fact ("the family's C3 never measured the assert-vs-withdraw contrast") is
recorded in the question's `decision.observation_bottleneck` instead. It is not a rival hypothesis
and it was not discovered by the run's data -- the Step 7c red-team found it by reading the driver
source -- so it is a **configuration fact about the observation bed**, and registering it as a leg
would inflate `initial_frozen_count` with a non-hypothesis. `initial_frozen_count` therefore stays
`4`.

The full JSON block, including the `decision` block and per-leg `basis` strings, is in the sibling
`.json` under `targets[0].hypothesis_space_ledger_pending.draft_registry_block`.

**At apply time:** confirm `instrumentation`, `process` and `world` each exist in the registry's
human-owned `axis_families.map`, or the question's `convergence_class` is forced to
`indeterminate`; add any missing mapping row in the same edit.

---

## 11. Step 7c red-team record

| Field | Value |
|---|---|
| Model | `fable-5.1` (cross-model -- the draft was produced by `claude-opus-5`) |
| Verdict | **CONTESTED** |
| Findings file | `/private/tmp/claude-501/-Users-dgolden-REE-Working/2b29825c-bcaa-4275-97dc-f77b3fd5a682/scratchpad/redteam_642c.md` (session-local scratchpad; the substance is folded in full below and throughout, and the path is recorded in the sibling `.json` `red_team` block) |
| Findings applied | F1, F2, F3, F4, F5, H1, H2, H3, H4, H6, H7, H8 |
| User gate decision | **hold `v3_pending`; route 642d with withdraw representable** |

The review was read-only, ordered draft JSON -> raw evidence (manifest cells, run pack, driver,
substrate, `claims.yaml`, prior autopsies, `substrate_queue`, env) -> draft `.md` last, and it
**recomputed every number in the draft** -- control-arm fire rates, block-arm recall bounds, the
transfer-assumption recall band, C0/C1 margins, C3 step margins, the `z_harm_a` and
`motor_gate_shut_frac` cells. All matched. What it contested was the **routing and the
recommendations built on top of the arithmetic**:

| # | Finding | Disposition |
|---|---|---|
| **F1** | The "conjunction / `z_harm_a` must be free to vary" reading of MECH-353's release condition is not forced, and **inverts** the "harm held constant" clause it quotes; the claim names the 642b lineage as the release run. | **Accepted.** Section 3 rewritten: both readings recorded, claim quoted verbatim, hold recorded as a **governance judgment** taken at the Step 8 gate. |
| **F2** | The specificity finding **mis-locates** the defect. The attribution (motor) clause was TRUE on all 14400 ticks and never discriminated; the false positives are **mismatch-floor** crossings on free steps, and they are the tick-level form of the entry's already-recorded CONTROL-transient residual. | **Accepted.** Section 2c retitled and rewritten; the `failure_record` item retitled; the H2-support sentence dropped from the fan-out basis. |
| **F3** | **C3 cannot express "withdraw" at all** -- `action_dim=4`, `noop_class` default 0 = MOVE-UP, stay is the unreachable index 4; the consumer's ASSERT bias (`blocked_agency.py:426`) treats move-up as passive. An experiment-configuration defect inherited across 642/642a/642b/642c. | **Accepted, and promoted to the DECISIVE defect.** Section 2b-i added; `criteria_non_degenerate` C3 adjudicated **false**; "three of four load-bearing criteria" throughout; 642d's spec item (1). |
| **F4** | `dv_headroom` is **opt-in** and the lint **WARN-only** (ree-v3 `8e133d26ed`), so the 642b item's second disjunct is satisfied **per-run**, not by an installed requirement -- which also means the severity exit condition has **not** fired. | **Accepted.** 9e.1 resolved *with the caveat verbatim*; 9e.3 status advance **withdrawn**; 9e.4 severity stays `corrupting` on its **original** rationale. |
| **F5** | **No per-tick series exists** (`metrics.json` 53 bytes; counts only), so the block-arm confusion matrix is not derivable at any cost -- and even a full matrix would not separate H1 from H2 without a self-attributable arm, which appeared in no recommended experiment. | **Accepted.** "Half free at zero compute" deleted; the self-attributable arm moved **into** 642d's spec (item 4); a per-tick series added (item 3); the fan-out collapsed honestly in 7d. |
| **H1** | Capacity-belief was cited via the wrong gate (`motor_agency` feeds ATTRIBUTION; `capacity_belief = 1 - w*||z_harm_a||`, `agent.py:4022`/`:4209`). True conclusion, wrong evidence. | Fixed in section 3 and the section 5 environment row. |
| **H2** | MECH-353 carries **none** of `epistemic_category`, `pending_retest_after_substrate`, `diagnostic_evidence_adjudicated` today -- the checklist should say "add", and `pending_retest_after_substrate: false` has nothing to be false *about*. | Fixed in 9c/9f; the field dropped from `per_claim_recommendation`. |
| **H3** | `n_external_blocks_counter` reports **ticks since the last env-done**, not "the final episode". | Fixed in section 2c and learning 4. |
| **H4** | Seed 43 passes C3 **only** via `action_rate`; its `alt_switch` goes the wrong way (`-9/2400`). | Recorded in 2b and in `degenerate_criterion_legs`. |
| **H6** | ".md says two of four" must move to **three of four** in both files. | Fixed in both. |
| **H7** | The `<= 2%` bar is **not derived** from anything in the record. | Marked **provisional**, with the derivation deferred to 642d's per-tick series. |
| **H8** | The draft registry's H0 `self_route_label` still read `validated_clear_v3_pending`. | Relabelled to `validated_substrate_calibration_v3_pending_stands`. |

**What the red-team confirmed rather than contested** (worth recording, since it is what the PASS
rests on): the PASS is real on C0/C1; the a-priori 0.30 bar and the 642a/642b replay are sound and
worth citing as precedent (learning 5); C2 is algebraically C1 under `num_hazards=0` and C3's
`no_suffering` is a second inert leg; `non_contributory` stands; `epistemic_category: standard` is
the right call; and NOT `/implement-substrate`, NOT `/lit-pull`, NOT demotion are all correct.

---

*Produced by `/failure-autopsy` in staging mode for `governance-20260905`, then confirmed inline by
that session on 2026-09-05 after the Step 7c red-team and the Step 8 human gate. Generation
timestamp 2026-09-05T02:38:25Z and confirmation timestamp 2026-09-05T09:34:46Z both taken from
`date -u`. This skill never edits claims.yaml, manifests, `review_tracker.json`,
`substrate_queue.json` or the hypothesis-space registry -- it produces the diagnosis; governance
applies it.*
