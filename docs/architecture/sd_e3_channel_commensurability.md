# SD-E3-CHANNEL-COMMENSURABILITY: e3_selector.channel_commensurability

**Substrate entry:** `f_dominance_conversion_ceiling` (rung 3, "E3 channel-scale normalisation")
**Primary claim:** MECH-439
**Status:** IMPLEMENTED 2026-09-07 -- but **UNVALIDATABLE AS SPECIFIED** as of 2026-09-10 (see "Amendment 2026-09-10"): the rung's pre-registered acceptance condition is an arithmetic identity of this operator, so the rung cannot be validated against it. This is materially different from 'validation owed'.
**Depends on:** MECH-448 (BUILT/VALIDATED), MECH-449 (BUILT/VALIDATED), V3-EXQ-571c instrument
**Blocks:** MECH-439, ARC-062, MECH-309, MECH-341

> This is a **rung of an existing substrate_queue entry**, not a new SD. Governance
> chose AMEND over CREATE on 2026-09-02 (`amend_note_2026_09_02`) because the entry's
> `implementation_hint` already carried the divisive-normalisation rung. This doc is the
> implementation record for that rung; the entry remains the plan of record.

## Problem

`E3TrajectorySelector.score_trajectory` sums its channels in their **native units**:

```
J = f_weight*F + lambda_eff*M + rho_residue*Phi - benefit_weight*B - goal_weight*G
```

Nothing puts those terms on a common scale, so which channel decides the committed
action is settled by units rather than by content.

`failure_autopsy_V3-EXQ-571c_2026-09-02` (confirmed; ratified by /governance 2026-09-02,
REE_assembly `0ade914d46`) measured this directly with a bounded, sum-to-one within-tick
**cross-candidate** partition over the additive channels, latch-gated to genuine fresh
selections. In the 936 regime a single channel held **0.98-0.99999** of the cross-candidate
variance in 15 of 16 cells:

| cells | occupant | share | F's share |
|---|---|---|---|
| all 8 residue-**fed** | `residue_weighted` | 0.98-0.99999 | 4e-06 to 1.1e-05 |
| 7 of 8 residue-**starved** | `f`/`harm_weighted` | 0.994-0.9998 | — |
| B2/seed46 (sole exception) | — | 0.7379, 3 live channels | — |

The load-bearing observation, and the one that determines the fix:

> **Every competing channel cleared the 1e-12 ABSOLUTE variance floor and failed only the
> 1e-3 RELATIVE share floor.** The monopoly is a *scale* phenomenon, not dead channels.

`n_live_channels = 1` therefore red-gated all four arms of 571c before criteria evaluation,
voiding an otherwise arithmetically-passed C1. Every MECH-439 / ARC-062 channel-authority
experiment silently assumes a precondition the substrate does not meet.

**Why not bound F.** 571c measured two *different* occupants under the lineage's own
`F_COMPONENTS` definition. A bound on F alone would simply hand the monopoly to residue.
The operator is therefore specified against the **joint** channel scale.

## Solution

Per-channel divisive normalisation against a **running** scale estimate. Each declared
channel's per-candidate term is divided by an EMA of that channel's own cross-candidate
standard deviation before entering the additive sum.

```
score_trajectory (per candidate)
  raw terms {f_weighted, harm_weighted, residue_weighted, benefit_weighted, goal_weighted}
    -> recorded RAW into _last_commensurability_raw     [operator ON; ungated by the decomp flag]
    -> each divided by max(scale_ema[c], floor)          [operator ON and warm]
    -> additive sum -> score
select()  (once, after the candidate loop)
  per-channel cross-candidate std over this tick's RAW terms
    -> EMA update of _chan_scale_ema[c];  _chan_scale_n += 1
    -> published to last_channel_scale_estimates
```

### Why *running*, not within-tick

`score_trajectory` scores **one candidate at a time** (the loop in `select()`), so the
tick's cross-candidate spread does not exist yet at scoring time. The estimate is folded in
*after* every candidate has been scored, so a tick is always scored against the estimate
accumulated from **prior** ticks — causal, and never self-referential.

### Why per-channel, not a pooled denominator

The `implementation_hint` permits either. A single pooled scalar denominator shared by all
channels is a uniform positive rescale of the score, hence **argmin-invariant** — it cannot
move the shares at all. This is the same lesson already recorded on the deleted MECH-111
broadcast branch ("uniform scalar shift is argmin-invariant", V3-EXQ-571). A per-candidate
pooled (Carandini-Heeger) form does vary across candidates, but still leaves a channel six
orders of magnitude larger dominant. Only per-channel standardisation reaches the target.

### Rank preservation

Within a tick each channel is divided by a **positive constant**, so each channel's own
ordering over candidates is preserved — the `implementation_hint`'s "rank-preserving
renormalisation vs the competing field". What changes is the relative authority *between*
channels, which is the intent.

## Config

`E3Config` only. Follows the `f_weight` / `e3_include_untrained_fallback_scorers` precedent
of **not** being wired through `REEConfig.from_dims()`; set per-arm as `cfg.e3.<field> = X`.

| Param | Default | Purpose |
|---|---|---|
| `use_e3_channel_commensurability` | `False` | master switch; False is bit-identical |
| `e3_commensurability_ema_alpha` | `0.05` | EMA decay (matches `precision_ema_alpha`) |
| `e3_commensurability_warmup_ticks` | `20` | estimate-only ticks before engagement |
| `e3_commensurability_floor` | `1e-12` | absolute scale floor; below it a channel keeps unit scale |

The floor is deliberately 571c's own `MIN_LIVE_CHANNEL_VARIANCE`, so the operator's floor
and the instrument's liveness floor agree.

## Scope

Normalised: `f_weighted`, `harm_weighted`, `residue_weighted`, `benefit_weighted`,
`goal_weighted` — exactly 571c's declared `SCORE_COMPONENTS` minus the structural zero.

Deliberately excluded, with reasons:

- `novelty_weighted` — hardcoded `0.0`; the MECH-111 broadcast branch was deleted
  2026-05-25 as argmin-invariant. There is no term to scale.
- `pe_confidence` / `self_viability` penalties — `generation:v4`, default-off, and outside
  571c's declared partition. Normalising them would redefine the partition a successor
  measures against.

**`residue/field.py` is not touched.** The substrate entry names `add_residue` and
`RBFLayer.forward` because residue is the monopolising *occupant*, not because the operator
lives there. Divisive normalisation is scale-invariant to the accumulator's magnitude by
construction — that is its virtue: it fixes the monopoly whatever the native scale is,
without picking a magic bound. Bounding `add_residue`'s unbounded `+=` is a separate lever
that would change residue semantics for every experiment on that path. (The autopsy is
separately emphatic that `field.py::update_valence` is **not** this path:
`SD-RESIDUE-VALENCE-BOUND` clamps `valence_vecs`, a different accumulator.)
Scope confirmed by the user at the design gate, 2026-09-07.

## Three design properties that are easy to get wrong

1. **The term capture is ungated by `e3_score_decomp_enabled`.** `_last_traj_components` is
   written only when that *diagnostic* flag is on. Reusing it would make the operator
   silently inert whenever the diagnostic is off — a live selection-path behaviour must not
   depend on a diagnostic switch. The operator captures its own terms.
2. **The EMA is fed from RAW terms, never normalised ones.** Estimating from
   post-normalisation values is a self-referential feedback loop that drives every scale to
   1.0 and makes the exposure a lie.
3. **A dead channel keeps unit scale.** A structurally-zero channel divided by its own
   near-zero spread would explode; the absolute floor with unit-scale passthrough prevents it.

Each is pinned by a named contract test with its own negative control.

## Verification exposure (spec-mandated)

`E3TrajectorySelector.last_channel_scale_estimates` carries `scales` (per channel),
`n_updates`, `engaged`, `warmup_ticks`, `floor`, `ema_alpha`, `channels`. The autopsy
requires that a successor be able to **verify** commensurability was achieved rather than
assume it.

## Readiness target

> **AMENDED 2026-09-10 -- the condition quoted immediately below is the ORIGINAL
> pre-registered target, preserved verbatim. It is NO LONGER the acceptance condition:
> it is an arithmetic identity of the operator. See "Amendment 2026-09-10" below.**

ORIGINAL (pre-registered by `failure_autopsy_V3-EXQ-571c_2026-09-02`, confirmed; SUPERSEDED
2026-09-10):

> **>= 2 E3 score channels simultaneously above a 1e-3 relative cross-candidate share in the
> 936 regime**, so that "which channel holds authority" is a contest rather than a
> restatement of units.

Measured at build time on a bare selector driven 40 ticks over 6 candidates, using the
substrate's *native* f/harm scale disparity (not an injected one):

| | n_live (>= 1e-3) | top share |
|---|---|---|
| operator OFF | 1 | 0.999518 |
| operator ON | **2** | 0.500000 |

The suppressed channel (`harm_weighted`) moves 4.82e-04 -> 5.00e-01. This is a bare-selector
measurement, not the 936 regime; the **regime-level** validation experiment is owed and is
tracked separately (it was pacing-gated at build time — see the implementation log on the
substrate entry).

## Amendment 2026-09-10 (rung status: IMPLEMENTED but UNVALIDATABLE AS SPECIFIED)

**AMENDED 2026-09-10 (/governance GFLAG-0234, option A, user-approved).** Ratified by the user on 2026-09-10 as option A of GFLAG-0234; the ORIGINAL target above is an ARITHMETIC IDENTITY of the operator it is meant to validate. The operator divides each channel's per-candidate term by an EMA of THAT CHANNEL'S OWN cross-candidate SD, and the DV is the cross-candidate variance partition over those same post-division terms (e3_selector.py's own comment: 'EFFECTIVE (post-commensurability) terms -- what actually entered the score'). Var(term/s) = Var(term)/s^2 ~= 1 per channel, so shares tend to 1/k and every channel above the 1e-12 ABSOLUTE floor clears the 1e-3 RELATIVE floor by three orders of magnitude. NO EXPERIMENT ADOPTING THE ORIGINAL TARGET CAN FAIL; the build-time ON row (n_live 2, top_share 0.500000 = exactly 1/2) is the identity's fingerprint, not an effect. AMENDED TARGET: a SELECTION-level DV -- commit-flip rate under shadow OFF/ON scoring on the same tick and the same candidate set -- which is what the spec's own argmin-invariance argument is actually about. STATUS OF THE RUNG: IMPLEMENTED but UNVALIDATABLE AS SPECIFIED, which differs materially from 'validation owed'. MECH-439's direction does NOT move: nothing here says the operator does or does not work, only that the registered target cannot tell. The owed validation V3-EXQ-1012 is authored and smoke-green but sits UNQUEUED as a .blocked scratch file and must NOT be queued against the original target. Also refuted, separately: the natural control gate 'the monopoly means n_live==1' is a misreading of a worst-cell verdict -- 571c's env_starved_warmup arm measures n_live 1/2/1/3 across seeds 42/43/45/46 and n_live==1 holds in 8 of its 16 cells (the flag says 7; either figure refutes it). Derivation, citations and successor recipe: evidence/planning/exq1012_blocked_readiness_target_tautological_20260908.md. Amending a CONFIRMED autopsy's pre-registered acceptance condition was done under explicit governance authority; the original text is preserved verbatim everywhere it appears and all four carriers were amended together: docs/architecture/sd_e3_channel_commensurability.md, evidence/planning/failure_autopsy_V3-EXQ-571c_2026-09-02.md, evidence/planning/failure_autopsy_V3-EXQ-571c_2026-09-02.json and evidence/planning/substrate_queue.json.

Read the table above accordingly: the ON row is what the identity predicts (1/k with k=2 live
channels), so it is not evidence that the operator achieved commensurability. The honest
statement of this rung's status is IMPLEMENTED but UNVALIDATABLE AS SPECIFIED -- NOT
'validation owed', which would wrongly imply that running the registered target could settle
anything.

## Backward compatibility

Bit-identical when off, verified at full `float64` precision against pristine `origin/main`
across 25 `select()` ticks — scores, selected indices, and every per-channel decomp value
(1250 recorded values, zero differences). With the operator off there is no term capture,
no EMA update and no division; `score_trajectory` takes exactly its pre-operator path.

## Biological grounding

Divisive normalisation is a canonical cortical computation (Carandini & Heeger 2012). The
running-scale form implemented here is its **adaptation** face: adaptation to each channel's
own recent statistics, as in contrast-gain adaptation (Fairhall et al. 2001). Consistent
with the `targeted_review_connectome_mech_439` grounding already cited on the substrate
entry's `implementation_hint`.

## Not applicable

- **MECH-094** — no simulation or replay content is written to memory.
- **Phased training** — no encoder head and no learned parameters. A BatchNorm-style
  learned affine was deliberately **not** adopted: it would add untrained parameters to the
  live selection path, which is exactly the `SD-E3-SCORER-COMPLETION` defect
  (`failure_autopsy_V3-EXQ-190a_2026-08-09`) this file already carries a fix for.

## Contracts

`ree-v3/tests/contracts/test_e3_channel_commensurability.py` — 13 tests. The file opens with
`test_monopoly_is_reproduced_with_the_operator_off`, a negative control for the whole file:
if the substrate ever stops exhibiting the 571c monopoly, that test fails and the rest are
known to be vacuous rather than silently passing.

## Related

MECH-439 (primary), ARC-062, MECH-309, MECH-341, MECH-448/449 (the eligibility-face levers
this rung sits beside), SD-085 (`f_weight`), SD-E3-SCORER-COMPLETION,
`failure_autopsy_V3-EXQ-571c_2026-09-02`, `substrate_queue.json::f_dominance_conversion_ceiling`.
