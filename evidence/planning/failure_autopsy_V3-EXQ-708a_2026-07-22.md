# Failure autopsy — V3-EXQ-708a (MECH-440 noisy-selection-head propagation falsifier)

**Scope:** single. **Status:** confirmed (user-adjudicated 2026-07-22).
**Generated:** 2026-07-22T03:48:30Z. **Promotes and demotes nothing.**

Run: `v3_exq_708a_mech440_noisy_selection_head_propagation_falsifier_20260720T211903Z_v3` ·
claims `[MECH-440]` · purpose `diagnostic` · `supersedes V3-EXQ-708` ·
outcome **FAIL** · direction `non_contributory` · self-route
`substrate_not_ready_requeue`, indexer flag **`precondition_unmet`**.

---

## 1. Facts

Recording complete (`rec/v1`, `substrate_hash`, `machine_class`, `config`,
`seeds [42..47]`, `elapsed_seconds 57353`). **No recording debt.**

**The instrument repair worked.** 708 was withdrawn (autopsy 2026-07-19) because its
pre-commit class-entropy DV read `e3.last_precommit_probs` once per env step with no
clear, replicating each probability vector by its hold duration — arm-dependently, so
the between-arm delta was distorted rather than merely imprecise. 708a clears both
attributes before every `select_action` and records a row only if repopulated. The
repair is verified in this run's own numbers:

| Precondition | measured | threshold | met |
|---|---|---|---|
| `fresh_selects_sufficient` | **862** | 30 | ✅ |
| `enough_divergent_seeds` | 4 | 3 | ✅ |
| `noise_bias_range_supra_floor_vs_raw` | 0.221 | 1e-4 | ✅ |
| `dacc_suppression_live` | 1.0 | 0.0 | ✅ |
| `learning_engaged_finer_channels_dissociable` | 0.00127 | 1e-4 | ✅ |
| **`temperature_control_raises_precommit_entropy`** | **0.0** | 2.0 | ✗ |
| **`weight_noise_raises_precommit_entropy`** | **1.0** | 2.0 | ✗ |

So: 862 genuine E3 `select()` calls, 4 divergent seeds, a supra-floor and
non-trivial-vs-raw noise bias range, live dACC suppression, dissociable finer
channels — **and neither designed lever moves the DV.** ARM_TEMP (the 687 temperature
control) raises pre-commit sampling-class entropy above A0_OFF on **0 of 4** divergent
seeds. ARM_NOISE_SINGLE does so on **1 of 4**.

The failed criteria are `readiness`-kind, hence `precondition_unmet`.

---

## 2. Adjudicating the self-route

**The self-route `substrate_not_ready_requeue` is technically correct but materially
under-reads its own run, and that matters.**

The canonical `precondition_unmet` failure mode (V3-EXQ-642) is *the instrument or the
setup was not ready, so nothing was measured*. That is **not** what happened here. The
instrument was ready — demonstrably, at 862 fresh selects against a floor of 30, after
a targeted repair whose whole purpose was to make this measurable. What failed is a
**manipulation check**: the levers that were supposed to inject pre-commit variance did
not inject it.

A manipulation check that fails on a *working* instrument is a **finding about the
system**, not a readiness problem. Two readings are available and both are substantive:

- **(i) The pre-commit sampling distribution is saturated.** If pre-commit is already
  near-deterministic (argmax-like), neither a temperature perturbation nor
  supra-floor weight noise will lift its entropy — the distribution has no headroom.
  This is the F-dominance / single-arena-argmax signature the 700d/708 lineage has
  circled before, now observed at the *pre-commit* stage rather than post-commit.
- **(ii) The levers do not reach the pre-commit stage.** Temperature and weight noise
  may be applied downstream of where the pre-commit distribution is formed, in which
  case this is a wiring gap and not a substrate property.

**These are not distinguishable from this manifest**, because nothing records the
*shape* of the pre-commit distribution — only its entropy delta between arms. A single
number (`precommit_class_entropy`) cannot tell "already at ceiling" from "lever never
arrived". That is the measurement gap.

The `non_contributory` direction is therefore **correct for MECH-440** — the claim was
not tested — but the run is **not uninformative**, and its learning must be recorded
rather than discarded with a bare requeue.

---

## 3. Claim-layer mapping

MECH-440 (`candidate`, `v3_pending`, `implementation_phase v3`,
`depends_on [MECH-313, MECH-260, Q-045, ARC-065]`). Its existing
`evidence_quality_note` already records the 708 withdrawal and states MECH-440 "was
never validly tested". That remains true after 708a: the propagation question is still
unasked, now for a different reason.

**MECH-440 could not express itself.** The claim is about whether selection-head noise
*propagates*; with no injected pre-commit variance there is nothing to propagate. The
absolute/negative-control criteria all passed; the discrimination criteria could not
be reached. This is the substrate-ceiling fingerprint in *form*, but the fingerprint
is not diagnostic here because the manipulation check failed upstream of it.

---

## 4. Biological-reference triage

**Closest mechanism:** stochastic resonance / neural variability in action selection —
striatal and cortical selection circuits use intrinsic variability (dopaminergic
modulation of exploration, cortical noise correlations) to keep multiple candidate
actions live up to commitment. Dependencies: a genuinely *distributed* pre-commitment
representation (several candidates carrying non-trivial probability mass) and a
commitment threshold that variability can push around.

**Formal-definition import?** Yes, mildly — "temperature" is a Boltzmann/softmax import,
and NoisyNet weight noise is an RL-engineering import (Fortunato et al.), not a
biological one. Real neural variability is not a global softmax temperature; it is
channel-specific and modulated by arousal and uncertainty. **This divergence is
load-bearing and is a plausible cause of reading (ii)**: a global temperature knob
applied at the wrong stage will not reproduce channel-specific pre-commit variability.

**Does the failure resemble a missing dependency?** **Yes — strongly.** The biological
prediction is that variability can only matter where several candidates carry mass. If
the pre-commit distribution is already collapsed onto one candidate, the biology
predicts exactly the null observed. That makes this FAIL **positive evidence for the
pre-commit-collapse hypothesis** rather than evidence against MECH-440.

**Lit status:** absent — no `targeted_review` on pre-commitment variability / stochastic
resonance in selection on file.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **untested** | No injected pre-commit variance ⇒ no propagation to observe. |
| Biological reference | **partial, divergence load-bearing** | Global softmax temperature + NoisyNet weight noise are engineering imports; biological selection variability is channel-specific and arousal-modulated. |
| Prerequisites | **missing** | The manipulation's own precondition (a non-collapsed pre-commit distribution, or levers that reach it) is absent. |
| Implementation completeness | **unclear — the open question** | Cannot distinguish "lever applied downstream of pre-commit" from "pre-commit saturated". |
| Environment adequacy | adequate | GAP-A reef-bipartite substrate, same as 708. |
| Measurement adequacy | **under-instrumented — DOMINANT LAYER** | Only the entropy *delta* is recorded. The pre-commit distribution's own shape (max prob, effective support, per-candidate mass) is not, so the two readings cannot be separated. |
| Integration adequacy | isolated | — |
| Scale / capacity | adequate | 862 fresh selects, 6 seeds, 4 divergent. |

**Recommended `epistemic_category`: `measurement_gap`.** The metric was blind to the
discriminator, and the discriminator was never computed. Explicitly **NOT**
`substrate_ceiling` — recorded so the MECH-440 brake count (currently **0** under
R1–R3) is not inflated by a reading this autopsy does not make.

---

## 6. Learning extracted

1. **SUBSTANTIVE FINDING (the point of this autopsy):** with a repaired,
   demonstrably-adequate instrument (862 fresh selects vs a floor of 30), **neither a
   temperature perturbation nor supra-floor weight noise raises pre-commit
   sampling-class entropy on a strict majority of divergent seeds.** 0/4 and 1/4
   against a bar of 2. This is a property of the system, not a readiness failure, and
   it must be recorded as such rather than filed as "requeue".
2. **A failed *manipulation check* on a working instrument is not the same as an
   unready substrate**, and the `precondition_unmet` flag cannot tell them apart —
   both are `kind: readiness`. Worth a schema distinction: `kind: readiness` (was the
   setup adequate) vs `kind: manipulation_check` (did the lever move anything). Only
   the first should self-route `substrate_not_ready_requeue`; the second is a result.
3. **The 708 instrument repair is validated and should be reused.** The
   clear-before-`select_action` + record-only-if-repopulated pattern (from
   `v3_exq_785a`, now lifted into `_lib` at ree-v3 `08e9955`) delivered 862 fresh
   selects where 708 had pure pseudo-replication. That fix is not in question.
4. **Measurement gap, not recording gap.** The pre-commit *distribution shape* was
   never computed, so this is not repairable by recording more of what already
   existed — it needs a new readout. Do not route it as recording-debt.

---

## 7. Repair pathway

**Node classification:** `complex (probe-gated) / puzzle (known rules)` — two named
rival readings, and one readout separates them.

**Re-derive brake:** MECH-440 = **0** confirmed `substrate_ceiling` hits under R1–R3
(1 confirmed autopsy target). **Does not fire.**

**Granularity-debt recurrence trigger: DOES NOT FIRE.** *(Corrected 2026-07-22 — the
original block read "FIRES ... six files" and listed 709, 710, 707b and 699 among them.
None of those four tag MECH-440: their targets read `['MECH-439','ARC-108','ARC-110']`,
`['MECH-140','MECH-450','MECH-439']`, `['ARC-110']` and `['MECH-448','MECH-449']`
respectively. They were counted from the claim's topical neighbourhood rather than from
`targets[].claim_ids` — the trigger defect fixed the same day; see
`scripts/granularity_debt_cluster.py`.)*

Verified with `python3 scripts/granularity_debt_cluster.py MECH-440`: **3 targets across
3 files** — `failure_autopsy_700d-708-single-arena-ceiling_2026-06-29`,
`failure_autopsy_V3-EXQ-708_2026-07-19`, and this one. And decisively, **no target reads
`weakened`**: the distribution is `intact=1, unclear=1, untested=1`. Three
non-contributory readings on a claim that was never validly tested is measurement debt,
not granularity debt — the readout has to change before the claim's granularity is even
in question. No `/claim-synthesis` recommendation is surfaced.

**Routing: `/queue-experiment` — same-question re-run, alphabetic suffix (708b).**
The scientific question is unchanged; the readout is what must change. Required
additions:

- **Record the pre-commit distribution's shape, not just its entropy**: per-select
  `max_prob`, effective support (participation ratio or n_candidates above a mass
  floor), and the per-candidate mass vector summary, per arm per seed. This separates
  reading (i) *saturated* from reading (ii) *lever never arrived*: under (i) `max_prob`
  is near 1 in **every** arm including A0_OFF; under (ii) `max_prob` differs by arm
  while entropy does not.
- **Instrument the lever's own arrival**: assert at the E3 call site that the
  temperature and the weight-noise perturbation are applied *upstream* of the
  pre-commit softmax, and record the applied value.
- **Reclassify the two failed entries** as `kind: manipulation_check` so a null there
  reports as a result rather than as an unready substrate.

`recommended_substrate_queue_entry.action = "none"` — no substrate build is warranted
until (i) vs (ii) is settled. **Do not route to `/implement-substrate`.**

Secondary: `/lit-pull` commission `targeted_review_mech_440_selection_variability` on
stochastic resonance / channel-specific variability in striatal selection, to ground
whether a global temperature knob is the right translation at all.

### Draft `evidence_quality_note` (governance to write — do not apply here)

> 2026-07-22 (V3-EXQ-708a, diagnostic, claim_ids=[MECH-440], `non_contributory` —
> weights nothing; failure_autopsy_V3-EXQ-708a_2026-07-22). The V3-EXQ-708 instrument
> repair WORKED: 862 genuinely-fresh E3 `select()` calls against a floor of 30, 4
> divergent seeds, supra-floor and non-trivial-vs-raw noise bias range, live dACC
> suppression, dissociable finer channels. MECH-440 was nonetheless not tested, for a
> new and substantive reason: **neither designed lever moves the dependent variable.**
> ARM_TEMP raises pre-commit sampling-class entropy above A0_OFF on 0 of 4 divergent
> seeds and ARM_NOISE_SINGLE on 1 of 4, against a bar of 2. With no injected pre-commit
> variance there is nothing for the propagation question to observe. This is a failed
> MANIPULATION CHECK on a demonstrably working instrument, not an unready substrate —
> the `precondition_unmet` flag cannot presently distinguish the two. Two readings are
> live and are not separable from this manifest, which records only the between-arm
> entropy delta: (i) the pre-commit distribution is already saturated/argmax-like and
> has no headroom (the F-dominance signature, now observed pre-commit), or (ii) the
> levers are applied downstream of where the pre-commit distribution is formed. Route
> to 708b recording pre-commit distribution SHAPE (max_prob, effective support,
> per-candidate mass) per arm per seed, which discriminates them. `measurement_gap`,
> explicitly NOT substrate_ceiling. MECH-440 stays `candidate` / `v3_pending`;
> `pending_retest_after_substrate` NOT set (no substrate build is owed yet).

---

## 8. Confirmed routing (user-adjudicated 2026-07-22)

User confirmed **"708a: record as a substantive finding"** — the learning is that
neither lever moves the pre-commit distribution, not merely that the run was not ready.
