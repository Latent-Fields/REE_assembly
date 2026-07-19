<!-- Produced by /failure-autopsy. Session clever-elion-56ba52. -->

# Failure autopsy — V3-EXQ-787 (MECH-463 hazard geometry, exogenous proximity)

**Target:** `v3_exq_787_mech463_hazard_geometry_exogenous_proximity_20260719T223352Z_v3`
**Queue id:** V3-EXQ-787 · **Claim:** MECH-463 · **Machine:** ree-cloud-2 (`linux-x86_64-py3.10-torch2.11.0+cpu`)
**Substrate hash:** `f64a92fcfae87ffecb0fcb1ed17238dd3fbf98bda5a420f1cc91225c418e578c`
**Outcome:** FAIL · `evidence_direction: does_not_support` · `non_degenerate: true`
**Self-route:** `hazard_geometry_inert_on_selection_variance` (cell `flat_with_expressive_channel`)
**Elapsed:** 7140.7 s · **Seeds:** 24 (hazard arms), 8 (A3) · **Autopsy written:** 2026-07-19T22:44Z

This is not a defect autopsy. The run executed exactly as designed and returned a clean,
well-powered null with a passing positive control. The autopsy exists because the null
**resolves the last live leg** of a frozen pre-registration question, and that resolution is
what needs adjudicating.

---

## 1. What was being decided

`hypothesis_space_registry.v1.json` question `arousal-variance-amplifier` (claims MECH-463) was
registered 2026-07-19T10:53Z with three frozen hypotheses. V3-EXQ-785a eliminated two of them.
The survivor was:

> **`H-endogenous-hazard-geometry`** — "The profile is hazard geometry, not arousal." High-urgency
> ticks are near-hazard ticks whose candidate geometry differs for reasons unrelated to the arousal
> scalar; both the variance rise and the share redistribution in V3-EXQ-785 are artifacts of
> conditioning on an endogenous variable.

The 785a adjudication deliberately left it `alive` and named what would settle it: *"Confirming it
needs a run that MANIPULATES hazard proximity, or a within-seed design with enough seeds to separate
the two."* V3-EXQ-787 is that run — it does both.

---

## 2. Reading order and what each check returned

The driver self-routes, but the routing is a hypothesis. Checks were verified in the order the
design pre-declares, gating on the arbiter first.

### [1] A3 expressivity positive control — **GREEN**

`interpretation.null_vs_inexpressive_discriminator.a3_expressive = true`. This is the pre-declared
arbiter separating a genuine null from an inert measurement channel; had it been false the label
would be `measurement_channel_inexpressive`, nothing could be concluded about hazard, and the leg
would stay `alive` with no bit claimed.

It did not merely pass — it passed with room to spare, on the *same* statistic C1 routes on:

| A3 quantity | Value |
|---|---|
| mean per-seed `log10 var_total` span | **1.347 decades** |
| min per-seed span | 1.051 |
| per-seed monotone fraction | **1.0** (ρ = 1.0 on all 8 seeds) |
| pooled span (secondary) | 1.361 |
| 785 reference effect being sought (`log10_var_fold`) | **1.149** |

The channel can be driven further than the effect under investigation. That is the strongest form
this control can take: the substrate could have shown the 785 profile and did not.

### [2] Load-bearing within-seed statistic — **flat, both halves**

`arm_analyses[].within_seed_slopes_LOAD_BEARING`, primary arm `hazard_exog_urgency_clamped`,
mean of per-seed OLS slopes with a one-sample t across 24 seeds.

| Criterion | Mean slope | sd | t (df 23, crit 2.069) | Floor | % of 785 reference | Verdict |
|---|---|---|---|---|---|---|
| C1 amplification (`log10 var_total`) | −0.000944 | 0.005087 | −0.909 n.s. | 0.0287 not cleared | **0.33%** | `flat` |
| C2 redistribution (incumbent share) | +0.000131 | 0.002446 | +0.262 n.s. | 0.0035 not cleared | **0.38%** | `flat` |

C2's sign is *positive* where the hypothesis predicts negative. Sign tests agree with the null
(C1 11+/13−; C2 15+/9−, neither near a majority that would survive the floor).

### [3] D3 covariance decomposition — Simpson signature **does not reproduce**

`between_fraction` near 1.0 would reproduce the 785a artifact. It does not:

| Arm | share `between_fraction` | log10 var `between_fraction` |
|---|---|---|
| clamped | 0.490 | 0.711 |
| free | 0.168 | 0.779 |

More decisively, D1 shows there is no longer a pooled signal left to decompose: pooled tick-level
r = **+0.004** (share) and **−0.012** (log10 var) on 5592 rows, against 785a's −0.187 / +0.171.
The pooled correlation that made hazard look confirmed in 785a collapses to zero once S=24
averages the between-seed heterogeneity away. *(D1 is a recorded decoy and routes nothing; it is
cited here only to show the decoy itself vanished.)*

### [4] D4 seed-0 anomaly — **does not replicate** (`replicates: false`)

785a's seed 0 carried the between-seed signal nearly alone at mean share 0.833, suspiciously close
to 785's endpoint 0.831. At S=24:

- `seeds_near_785a_seed0_share = [0]` at tolerance 0.02 — only seed 0 itself, which is the **same
  RNG seed** and therefore the same trajectory. That is reproduction of a seed, not of a mechanism.
- Across 24 seeds mean share = 0.954, sd = 0.055; seed 0 at 0.8268 sits at **z = −2.33**, the low
  tail of a smooth distribution (2 of 24 seeds ≤ 0.87).

So 785a's seed-0 leverage was Simpson's paradox on n=5, exactly as that adjudication suspected. The
open question the prior ledger entry flagged is now answered: **one-seed artifact, not a signal.**

### [5] Participation ratio — objection materially weakened

`zworld_participation_ratio_mean` = **4.3135 / 4.2962 / 4.3805** across the three arms, against the
**~1.06** the 785a caveat assumed. Close to the dry run's ~5.0. The "substrate cannot *express* it"
objection is correspondingly weaker, and combined with the A3 control it is not available as a
defence of the leg here.

### Internal validity — "no effect", not "no treatment"

The check that makes the null adjudicable rather than empty:

| Fidelity quantity | Value |
|---|---|
| corr(assigned level, realized `hazard_prox_center`) | **0.988** |
| realized vs expected centers by level | 0.222/0.286/0.400/0.500/0.667 vs 0.222/0.286/0.400/0.500/0.667 (6 dp) |
| proximity range spanned | 3× |
| `pin_miss_frac` mean / max | 0.006 / 0.067 |

All three arms gate GREEN, `criteria_non_degenerate` true on all three criteria, incumbent
`harm_weighted` at margin 0.906 with **2** non-trivial components — clearing the ≥2-component gate
that V3-EXQ-785 structurally failed.

### The premise fails independently, at the first stage

`metrics.mediation_premise`, computed on the **urgency-free** arm (correctly — urgency is clamped by
construction in the primary arm, where the correlation is 0.0 by design):

```
corr_assigned_proximity_vs_realized_urgency = 0.163868
premise_holds = false            (threshold 0.2)
```

The hypothesis's own premise — *high-urgency ticks are near-hazard ticks* — is false in this
substrate. This is logically upstream of the geometry result and independent of it: even had the
geometry moved, proximity is not what endogenous urgency was tracking in 785. Two independent
refutations, at different stages of the posited causal chain.

---

## 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | MECH-463 is untouched by this run; the leg was a *rival* explanation of 785's profile, not the claim itself. No demotion follows. |
| Biological reference | n/a for this leg | The leg is an `instrumentation`-axis artifact hypothesis (conditioning on an endogenous variable), not a mechanism import. |
| Dependency prerequisites | present | All arms gated green; incumbent identity and ≥2-component structure as pre-registered. |
| Implementation completeness | complete | Exogenous re-pinning delivered at fidelity 0.988. |
| Environment adequacy | adequate | 3× proximity range realised exactly; `pin_miss_frac` 0.6%. |
| Measurement adequacy | **adequate and positively demonstrated** | A3 moves the identical statistic 1.347 decades, exceeding the 1.149 effect sought. This is the layer that would normally be `unknown` for a null; here it is proven. |
| Integration adequacy | coupled | Urgency-free arm shows the input path is live but weakly coupled (r = 0.164) — which is itself the premise finding. |
| Scale / capacity | adequate | S=24 with within-seed slopes; z_world PR 4.3 vs the 1.06 the prior caveat assumed. |

**Recommended `epistemic_category`: `standard`.** Not `substrate_ceiling` — the positive control
forecloses that reading, which is precisely what it was built to do.

---

## 4. Ledger resolution applied (Step 9b, Mode B)

`H-endogenous-hazard-geometry` → **`eliminated`**.

| Field | Value |
|---|---|
| `resolving_runs` | `["V3-EXQ-787"]` |
| `evidence_direction` | `weakens` (leg vocabulary) |
| `manifest_evidence_direction` | `does_not_support` (claim-level, preserved alongside — 785a precedent) |
| `epistemic_category` | `standard` |
| `self_route_label` | `hazard_geometry_inert_on_selection_variance` |
| `control_passed` | `true` (C3 positive control) |
| `non_degenerate` | `true` |
| `met_elimination_bar` | `true` |
| `resolved_utc` | `2026-07-19T22:33:52Z` (manifest `timestamp_utc`) |

**Question `arousal-variance-amplifier` is now 3 of 3 eliminated** — `alive: 0`, `resolved_out: 3`,
`reduction_ratio: 1.0`, `bits_removed: 1.58`, momentum class `ruled_out`. No denominator change; no
`fanout_growth_events` entry was needed or made. Integrity audit: **a=0 b=0 c=0 d=0**.

Frozen-set invariants checked before commit: (1) `initial_frozen_count == len(hypotheses) == 3`,
unchanged; (2) `pre_registered_utc` 2026-07-19T10:53:44Z ≤ `resolved_utc` 2026-07-19T22:33:52Z;
(4) full bar present on all three eliminated legs.

---

## 5. What this leaves open — read this before treating the question as closed

The rival set is **exhausted without a positive account.** All three registered explanations of the
V3-EXQ-785 profile are eliminated, and nothing pre-registered replaces them. That is an honest
unknown, and the reduction ratio of 1.0 should not be read as "the mechanism is understood":

- **Arousal** is inert (785a).
- **Hazard geometry** is inert, and its premise is false (787).
- **What endogenous urgency was actually tracking in 785** has no surviving candidate.

In the work-graph vocabulary this is `complex (probe-gated)` — a **mystery (known data)** rather
than a `puzzle (known rules)`. V3-EXQ-785's per-tick sink is now embedded in-manifest (785a's fix),
so the data to reframe against exists; what is missing is a reframing, not a further measurement.
Opening a fresh portfolio of rivals on the unchanged framing is exactly the move the GOV-FROZEN-1
recurrence clause warns against.

**Scope bounds that still hold and must travel with any citation of this result:**

1. **One incumbent identity** — `harm_weighted` only. **Channel-agnosticism is NOT covered here.**
   That half is V3-EXQ-785b (`v3_exq_785b_mech463_channel_agnosticism_decomp`, landed
   2026-07-19T21:24Z, FAIL / `does_not_support`), a separate concurrent workstream awaiting its own
   adjudication. Do not read 787 as covering a second incumbent identity.
2. **SD-011 commit-threshold route only** — `use_harm_variance_commit` is OFF, so the gated quantity
   is the z_world running variance (world-model stability), not candidate separation.
3. **MECH-463 stays `candidate`.** This run adjudicates a rival hypothesis about 785's profile; it
   is not itself evidence for or against MECH-463's registered prediction beyond what 785a already
   recorded.

**Recording gap (minor, worth fixing in the next driver of this family):** every entry in
`per_arm_gate.green[].preconditions[]` carries `met: true` with `observed: null` — the gate
evaluated correctly against its thresholds, but the observed values were not serialised into that
block. They are recoverable from `arm_analyses[].fidelity` here, so nothing is lost for *this* run,
but a future reader checking preconditions alone cannot see the numbers. This is recording-debt, not
measurement-debt, per `experimental_recording_standard_2026-07-12.md`.

**Registry-wide, pre-existing, not caused by this edit:** `convergence.convergence_class` for this
question is `indeterminate` because the axis labels `instrumentation` and `process` are absent from
the human-owned `axis_families.map`. Both are canonical family names in the Step 9b taxonomy, so
these look like missing identity rows rather than a taxonomy dispute. Left for a human — the map is
human-owned by design, and with zero fan-out growth on this question the class is moot here.
