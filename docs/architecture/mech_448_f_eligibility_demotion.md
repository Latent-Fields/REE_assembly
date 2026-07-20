---
title: "MECH-448: Rank-preserving F->eligibility demotion (ARC-107 LEAD lever)"
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 13
status: candidate
status_asof: 2026-07-20
status_claim: MECH-448
---

# MECH-448: Rank-preserving F->eligibility demotion (ARC-107 LEAD lever)

**Claim ID:** MECH-448
**Architecture:** ARC-107 (basal-ganglia-like E3-selector constitution)
**Subject:** `ethics_engine_3.rank_preserving_f_to_eligibility_demotion`
**Substrate:** built 2026-06-20 — this PROMOTES NOTHING; the 689a-successor
falsifier is the next, separate step and gates any promotion. Governance status
is carried by the `status:` frontmatter / claims.yaml.
**Grounded under:** ARC-106 (brain-like construction); first major worked
application of the grounding ladder + divergence ledger + ablation falsifier.

---

## Problem (restated as a selection-structure fault)

Across mechanistically distinct channels (CRF 654g, OFC 485h, SD-037 625e,
dACC 445h, modulatory 569g) the cluster pattern is identical:

```
upstream signal forms -> is measurable -> reaches E3 authority -> committed action does not change
```

The selector still behaves too much like `candidates -> scalar (F) score
dominance -> committed argmin`. F (the primary harm/goal score) monopolises
~88-89%% of E3 committed-selection variance (V3-EXQ-571), unmoved by the full
diversity stack. The conflict-grade near-tie parametric family is exhausted
(MECH-447 / V3-EXQ-689a: Factor A inert, A1B1 destructively cancels). The
required architecture is **constitutional, not parametric**: a signal's
STRENGTH must be necessary but not sufficient -- it also needs LAWFUL ACCESS to
committed action.

MECH-448 is the LEAD lever: **F decides who is ELIGIBLE to compete, not who
wins.**

## Routing / precondition

Routed here by the user-adjudicated `failure_autopsy_V3-EXQ-689a_2026-06-20`
Step-8 decision ("elevate the constitutional build"). The build is gated on the
689c (Factor-B-alone isolation retest) outcome only for SCOPE: at build time
V3-EXQ-689c was **PENDING (not landed)** in the coordinator queue (status
`pending`, pinned ree-cloud-3, no results row), so no gap-CONCENTRATED parametric
win existed that would shrink scope. Per the design note risk register (s5)
"build the lead lever no-op-default first" -- a no-op-default lever commits
nothing about scope, and the falsifier (the scope-sensitive part) is the
separate next step that will incorporate 689c when it lands.

## Solution

### Reuse, not duplicate (ARC-106 guardrail 2)

`e3_selector.py` already implements the within-eligible arbitration MECH-448
needs (the `use_modulatory_shortlist_then_modulate` block: F filters an eligible
set, `_modulatory_accum` arbitrates the committed action WITHIN it). MECH-448
adds only the genuinely new piece -- a **graded, env-general eligibility
envelope** -- in place of the hard `top_k` count / `margin` cutoff (which is a
HARD, env-conditional shortlist: V3-EXQ-684 showed the margin mode admits a
near-whole, state-stable set; 569i top_k works only on the reef-bipartite
structural guarantee).

### Graded eligibility envelope (divisive-normalisation analog)

`E3TrajectorySelector._f_eligibility_envelope(raw_scores)` (lower-is-better F):

```
merit[i] = clamp(raw_scores.max() - raw_scores[i], min=0)   # best (lowest cost) = highest merit
pooled   = f_eligibility_dn_sigma + merit.sum()
elig[i]  = merit[i] / pooled                                 # SHARE of the competing field
eligible = { i : elig[i] >= f_eligibility_envelope_floor }   # ABSOLUTE share floor
```

The **absolute share floor** is load-bearing: a fraction-of-max threshold would
cancel the pooled term and degenerate to the margin shortlist. With an absolute
floor a candidate must command at least `floor` of the TOTAL competing merit to
be eligible, so the envelope WIDTH adapts to the conflict structure:

| F structure | envelope |
|---|---|
| decisive (one clear F-winner) | NARROW (others fall below the share floor) |
| near-tie (competitive field) | WIDE (share spreads, more clear the floor) |
| exact N-way tie / flat F | WIDE fallback = all (low conflict -> no F restriction) |

This is the basal-ganglia hyperdirect conflict-grade emerging from the field
structure, not a hard count. `elig` is monotone in `merit` -> monotone in `-F`,
so the eligible set is an **F-rank prefix** (rank-preserving). Within the
eligible set the existing `_modulatory_accum` arbitration picks the committed
action (`argmin` committed / softmax-sampled uncommitted) -- **F removed from the
final argmin.**

### Config (all no-op default; bit-identical OFF)

| Param | Default | Purpose |
|---|---|---|
| `use_f_eligibility_demotion` | `False` | master switch (E3Config + from_dims) |
| `f_eligibility_envelope_floor` | `0.30` | absolute DN-share floor for eligibility |
| `f_eligibility_dn_sigma` | `0.0` | DN semi-saturation (global tightness; >0 narrows) |

Requires a modulatory channel (`_modulatory_accum is not None`, i.e. a
`score_bias` / MECH-341 bonus / route bias). With no modulation there is nothing
to demote F to, so the block is skipped (legacy F argmin, bit-identical) -- this
is the non-vacuity precondition the falsifier must satisfy.

### Diagnostics (`last_score_diagnostics`)

- `f_eligibility_demotion_active`
- `f_eligibility_envelope_size` (eligible count)
- `f_eligibility_excluded_count` (K - eligible; **non-degeneracy** signal -- > 0
  means the envelope actually excluded, not all-admit)
- `f_eligibility_winner_neq_f_argmin` (F demoted at commit)
- `f_eligibility_rank_preserving` (eligible set is an F-rank prefix; every
  eligible cost <= every excluded cost, tie-robust)

## ARC-106 divergence ledger (LOAD-BEARING)

Canonical divisive normalisation (Carandini & Heeger 2012; value DN,
Louie/Khaw/Glimcher 2013) is **ORDER-PRESERVING + POOLED-SYMMETRIC**. REE
demotes ONLY F and removes it from the commit argmin -- **rank-ALTERING at
COMMIT** (the within-eligible winner is the modulatory argmin, not the F argmin).
This EXCEEDS canonical DN and is the QD/MAP-Elites justification (CDQ-003): a
strong-but-not-sufficient score grants lawful access, it does not decide.
Load-bearing -- must be lit-anchored (the concurrent `targeted_review_connectome_mech_439`
grounding extension) and falsifier-validated.

## Safety

A clearly-harmful candidate has near-zero merit -> near-zero share -> below the
floor -> excluded. So no global disinhibition: the envelope is itself the
F-bound (parallel to the existing top_k safety guarantee). Verified by contract
(`test_safety_harmful_outlier_never_selected`: an overwhelming modulatory pull
toward an excluded harmful candidate never selects it).

## Psychiatric failure mode (ARC-106 mandate)

- Envelope too wide / F removed without a bounded No-Go -> disinhibition,
  impulsivity, action-selection without value gating (mania / OCD-spectrum loss
  of inhibitory braking).
- Envelope too tight -> bradykinesia / avolition analog (the current failure:
  nothing but F converts).

## Ablation falsifier (V3-EXQ-689a-successor; NOT queued here)

Committed-class entropy reaches the proposer ceiling on >= 2/3 seeds **AND**
order is preserved on the numerators (F still ranks within-eligible) **AND** no
harmful action class is globally disinhibited (safety). WEAKENED if entropy lifts
only by globally flattening F (loses signal / admits harmful classes) or if the
Factor-B near-tie lever already reaches the ceiling (689c). NON-DEGENERACY: the
envelope must actually exclude non-eligible candidates on a divergent pool
(`f_eligibility_excluded_count > 0`); an all-admit envelope is a vacuous
self-route. Acceptance criteria: ARC-107 design note section 4. The falsifier
must run on a DIVERGENT F pool (the GAP-A-ready foraging substrate:
SD-056-trained `e2.world_forward` + ARC-065 GAP-A `candidate_summary_source=e2_world_forward`).

## What this enables

Once a contributory falsifier PASS lands, MECH-448 moves toward `supports` and
ARC-107 gains its first validated lever; MECH-449 (Go/No-Go eligibility
constitution) is built only if the demotion lever alone is insufficient (note
s5.3 double-gate).

## Modules

- `ree-v3/ree_core/predictors/e3_selector.py` -- `_f_eligibility_envelope` +
  the `"f_demotion"` eligibility branch in the shortlist-then-modulate block +
  5 diagnostics.
- `ree-v3/ree_core/utils/config.py` -- E3Config fields + `from_dims`.
- `ree-v3/tests/contracts/test_mech_448_f_eligibility_demotion.py` -- 10
  contracts (config no-op / OFF legacy argmin / graded width / non-degeneracy
  exclusion / safety / F-removed-from-argmin / rank-preserving / requires-
  modulatory / exact-tie wide fallback / from_dims wiring).

## Related claims

ARC-107 (architecture), MECH-447 (conflict-graded near-tie sufficiency; weakened,
exhausted), MECH-449 (Go/No-Go constitution; follow-on, double-gated), MECH-439
(F-dominance root), Q-078 (constitutional-vs-parametric umbrella), ARC-106
(grounding framework). Substrate-queue rung: `f_dominance_conversion_ceiling`.

## Channel-adaptive (mean-relative) envelope amend (2026-06-21)

The absolute share floor `f_eligibility_envelope_floor` (default 0.30) was tuned to
PASS on the GAP-A foraging bank (V3-EXQ-689d). Each downstream channel has a
**different F-merit distribution**, so the same fixed floor mis-fires:

- **V3-EXQ-654h** (arc_062 rule-apprehension): every per-candidate share fell
  below 0.30 -> the floor admitted ALL candidates -> `f_eligibility_excluded_count==0`,
  an all-admit no-op (the lever never engaged; "485i twin").
- **V3-EXQ-485i -> 485j** (OFC): needed a bespoke per-seed envelope-floor
  recalibration to engage. 485j then confirmed OFC discrimination **converts** under
  demotion -- the lever generalises off GAP-A; the residual was a separate
  devaluation test-design gap (re-queued as 485k), NOT the envelope.

So the *direction* is confirmed (MECH-448 generalises), but every downstream channel
otherwise needs its own manual floor sweep.

**Fix.** A new no-op-default flag `use_f_eligibility_adaptive_floor` (E3Config +
`from_dims`, default False -> bit-identical) replaces the fixed absolute floor with a
**mean-relative** one inside `_f_eligibility_envelope`:

```
floor = f_eligibility_adaptive_mean_factor * elig.mean()    # adaptive
vs.    f_eligibility_envelope_floor (0.30)                  # legacy fixed
```

A candidate is eligible iff its share of the competing merit exceeds
`f_eligibility_adaptive_mean_factor` (default 1.0) times the field's **own mean
share**, rather than an absolute constant. Properties:

- **Scale-invariant** -- auto-calibrates to each channel's F-merit distribution; the
  654h all-admit no-op cannot recur and the 485i/485j bespoke recalibration is no
  longer needed. Collapses ~5 per-channel hand-floor dances (654h/485i/485j + the
  pending 625/445/687 successors) into **one global knob**.
- **Conflict-grade preserved** -- a decisive F-winner pulls the mean up so the others
  fall below (narrow envelope); a near-tie sits near the mean (wide). A fixed
  quantile would throw this away; mean-relative keeps it.
- **Excludes by construction** -- for `mean_factor >= 1.0` on any NON-uniform field at
  least one candidate is below the mean share, so `excluded_count > 0`.
- **Rank-preserving** -- still a threshold on `elig` (monotone in merit), so the
  eligible set stays an F-rank prefix.

The exact-tie / flat-F early returns, the empty-eligible all-admit fallback, the
modulatory-channel requirement, and all five diagnostics
(`f_eligibility_excluded_count` / `_winner_neq_f_argmin` / `_envelope_size` /
`_rank_preserving` / `_demotion_active`) are unchanged. Default OFF reads the fixed
floor and `use_f_eligibility_demotion` itself stays OFF for existing runs (double
guard). 16/16 MECH-448 contracts (8 new adaptive) + 8/8 preflight + 48/48 E3-cluster
PASS. PROMOTES NOTHING -- MECH-448 stays candidate; claims.yaml untouched.

**Validation:** V3-EXQ-689e channel-adaptive envelope readiness diagnostic
(claim_ids=[]) -- `excluded_count > 0` lands in a productive range on >= 2 real channel
substrates (the arc_062 bank that no-opped in 654h + the OFC/foraging bank) with the
SAME global adaptive config (no per-channel hand-tuning); bit-identical OFF as the
negative control; `substrate_not_ready_requeue` if the adaptive floor still no-ops on
any channel.
