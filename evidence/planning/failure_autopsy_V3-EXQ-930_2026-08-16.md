# Failure autopsy -- V3-EXQ-930 (diagnostic PASS, MECH-303)

- **Generated (UTC):** 2026-08-16T18:25:54Z
- **Status:** `awaiting_human_confirmation` (STAGING MODE -- Step 8 interactive gate NOT run; routing drafted, not finalised)
- **Scope:** single
- **Target run_id:** `v3_exq_930_mech303_dedicated_proximity_signal_validation_20260814T092437Z_v3`
- **queue_id:** V3-EXQ-930 | **claim_ids:** `["MECH-303"]` | **experiment_purpose:** `diagnostic`
- **Manifest outcome:** PASS | self-stamped `evidence_direction: supports` | `non_degenerate: true`
- **Self-routed label:** `mech303_dedicated_signal_discriminates_zharma_does_not`

Trigger: **diagnostic-purpose PASS, unflagged**. Per the 2026-08-07 user-instructed correction,
every `experiment_purpose: "diagnostic"` PASS requires this autopsy regardless of whether the
indexer raised an `adjudication` flag -- "cleared its own preconditions" is exactly what a
vacuous or confounded pass would also show.

---

## 0. Gates run before any metric was read

**Already-done check (by CONTENT, not filename glob).** Scanned every
`evidence/planning/failure_autopsy_*.json` for a target whose `run_id` matches this run:
**0 hits**. No prior autopsy covers V3-EXQ-930.

**Step 2a dry-run gate.**

```
scripts/check_dry_run_citations.py v3_exq_930_..._20260814T092437Z_v3
-- 0 dry cited, 0 dry in named families, 0 ambiguous, 1 clean, 0 unknown   (exit 0)
```

The target is a **real full-budget run** (`dry_run` absent/falsey; 150 ticks/cell, not the
20-tick dry path). `excluded_dry_run_ids: []` -- no run was excluded, and no population
statistic in this artifact draws on a smoke. No cluster: this is a single-target autopsy, so
there is no member set to sweep.

**Recording provenance.** `ree-v3/validate_recording.py --paths <manifest>` reports
**OK / complete**: `recording_schema: rec/v1`, `substrate_hash`
`f8b70b727fe09d87fe2cfd377636ca03155945bed34e5e776ce2e45b54d1147b`, `substrate_commit`
`13f7ee538f87b05a1544da788586537c4399c85d` (clean, branch `main`),
`substrate_stable_across_run: true`, `machine` `ree-cloud-2`, `machine_class`
`linux-x86_64-py3.10-torch2.12.0+cpu`, `elapsed_seconds` 539.4, full `config`, explicit
`seeds` `[0..9]`. **No always-core gap.** A substrate-level reading is therefore falsifiable
here, unlike the no-`substrate_hash` case the skill warns about.

---

## 1. Facts -- what the run actually did

### 1a. Design

Driver: `ree-v3/experiments/v3_exq_930_mech303_dedicated_proximity_signal_validation.py`
(505 lines, read in full). 5 hazard-density levels x 10 seeds = **50 cells**, 150 ticks each
(**7,500 ticks**). Each cell builds a **fresh `REEAgent`**, calls `agent.reset()`, then
random-walks the environment (`env.step(random.randint(0,4))`) while ticking the full internal
pipeline via `agent.sense()` + `_act()`. Env scenario:
`limb_damage_enabled=True` (SD-022 damage-sourced `z_harm_a`) **and**
`safety_proximity_signal_enabled=True` (the env emits `obs_dict["safety_proximity_harm"]`).

Two candidate MECH-303 gate signals are recorded per tick **from the same live path**:

| signal | source | role |
|---|---|---|
| `dedicated_proximity` | `obs_dict["safety_proximity_harm"]` (env EMA, tau~20) | **C1, load-bearing** |
| `damage_sourced_zharma` | `latent.z_harm_a.norm()` | **C2, REPORTED CONTROL, explicitly NOT load-bearing** |

For each signal x each of 18 thresholds: `reachability(tau)` = mean per-seed fraction of ticks
with `signal < tau` in the SAFE group (`num_hazards` in {0,1}); `AUC(tau)` = rank-biserial AUC
of those per-seed fire-rates as a SAFE-vs-UNSAFE (`num_hazards` in {4,8}) classifier.
`num_hazards=2` is reported as context and excluded from the binary AUC.

### 1b. What gates the PASS -- and the manifest's `criteria[]` location

The prompt's note is **confirmed and corrected in one direction**: the `interpretation` block
carries **no `criteria[]` array** -- it holds only `label`, `preconditions[]` (2), and
`criteria_non_degenerate` (2 booleans). But the manifest is **not** criterion-less: a
`criteria[]` array sits at **top level**, alongside an explicit `combination_rule`:

```
criteria: [
  {"name": "C1_dedicated_proximity_signal_discriminates (reachable+AUC>=0.75)",
   "load_bearing": true,  "passed": true},
  {"name": "C2_damage_sourced_zharma_discriminates (control -- expected FAIL, reproduces 917)",
   "load_bearing": false, "passed": false}
]
combination_rule: "overall PASS iff C1 ... C2 ... is a REPORTED control, NOT load-bearing:
                   it is expected to FAIL ... a surprising C2 PASS is a context note, not a
                   run failure."
```

**So the PASS is gated by C1 alone.** In source (`run_experiment`) the chain is:
`readiness_met = apparatus_met AND spread_met`; if not met -> FAIL /
`substrate_not_ready_requeue`; else `overall_pass = bool(c1)` where
`c1 = (analysis["dedicated_proximity"]["recommended"] is not None)`, i.e. *some* tau clears
`reach >= 0.15 AND AUC >= 0.75`. **C2's FAIL contributes nothing to the verdict** -- which is
the first crack in the self-routed label (see Section 3).

### 1c. Measured values

**Dedicated proximity signal (C1):**

| `num_hazards` | 0 | 1 | 2 | 4 | 8 |
|---|---|---|---|---|---|
| per-density mean | **0.00000** | 0.28279 | 0.53626 | 0.83965 | 0.86673 |
| sd of cell means across 10 seeds | 0.00000 | 0.03076 | 0.04867 | 0.01558 | 0.00000 |
| mean within-seed std | 0.00000 | 0.09822 | 0.14984 | 0.21646 | 0.22498 |

`density_spread_std` = **0.33112**. Global observed range 0.000000 -> 0.999520.
Per-threshold: **every** tau from 0.02 to 0.30 qualifies; `recommended` tau = **0.08**
(reach 0.5263, AUC **1.0000**); `best_auc_any_threshold` = **1.0**;
`meets_acceptance_target` **true** (1.0 >= the 0.84 acceptance target from the failure record).
The **shipped gate default** `contextual_safety_proximity_threshold = 0.25` also qualifies
(reach 0.6480, AUC 1.0000) -- a genuinely useful calibration readout, see Section 6.

**Damage-sourced `z_harm_a` (C2, control):**

| `num_hazards` | 0 | 1 | 2 | 4 | 8 |
|---|---|---|---|---|---|
| per-density mean | 0.441964 | 0.441805 | 0.441885 | 0.441966 | 0.441814 |
| sd of cell means across 10 seeds | 6.42e-2 | 6.41e-2 | 6.39e-2 | 6.36e-2 | 6.35e-2 |
| mean within-seed std | 9.83e-4 | 1.19e-3 | 1.07e-3 | 1.76e-3 | **2.06e-3** |

`density_spread_std` = **6.96e-5**. `best_auc_any_threshold` = **0.52** (at tau=0.4).
No tau qualifies. Reachability is **0.0** for every tau <= 0.30 and **1.0** for every
tau >= 0.55 -- i.e. the signal is a tight band around ~0.442 with essentially no
density-dependent movement. Global observed range 0.34339 -> 0.54652.

**Preconditions (both met):**

| precondition | measured | threshold | met |
|---|---|---|---|
| `both_signals_apparatus_reachable` | 1.000 (7500/7500 ticks, 150/150 in every cell) | >= 0.99 | true |
| `dedicated_signal_varies_with_density` | 0.33112 | >= 0.001 | true |

`criteria_non_degenerate`: `dedicated_density_battery_nondegenerate` true (spread > 1e-6);
`dedicated_auc_computation_nondegenerate` true.

### 1d. `z_goal_stream` -- reported honestly, and it is NEITHER of the two failure states

The manifest **carries** the block:

```
z_goal_stream: {ticks_total: 0, ticks_active: 0, writer_calls: 0,
                active_frac: null, writer_defect: null,
                goal_state_present: false, n_agents: 50}
```

Reading it against `experiments/_lib/z_goal_stream.py`'s own documented semantics:

- It is **PRESENT**, not absent. `z_goal_stream_stats` returns `None` (and the key is omitted)
  only when no counter-bearing agent was supplied; 50 agents were.
- It is **NOT the writer defect.** `writer_defect` is `True` only when `ticks_total > 0 AND
  writer_calls == 0`. Here `ticks_total == 0`, so the module writes `writer_defect: null`
  ("nothing was measured") and `active_frac: null` (explicitly NOT `0.0`, because 0.0 would be
  a false reading rather than a weak one).
- `goal_state_present: false` is the disambiguator the module provides for exactly this case:
  `GoalState` is constructed only when `config.goal.z_goal_enabled` is set, so `ticks_total == 0`
  here means **z_goal is disabled at config**, not that agents were never stepped.

So the accurate three-way statement the prompt asks for: **present-with-zero-writer-calls is
literally true, but it is NOT the `writer_defect` state** -- it is the module's
"nothing measured, goal machinery off at config" state, which the driver's inline comment
(`# no goal use case here, genuine goal-OFF measured-zero`) correctly anticipates. One minor
wording nit for the record: the recorded value is `null`, not a "measured zero"; the module
deliberately distinguishes those.

**Do this run's criteria depend on a live z_goal? No.** C1 reads an environment observation
channel; C2 reads `latent.z_harm_a.norm()`. Neither the readiness gate nor either criterion
touches `z_goal`, `GoalState`, or any of its listed consumers. This is a genuine goal-OFF
apparatus battery and the dead stream costs it nothing.

---

## 2. The load-bearing criterion: is the PASS real, or degenerate?

**Verdict: REAL, not degenerate -- but NEAR-ANALYTIC, and its information content is
apparatus-level, not mechanism-level.**

Degeneracy is genuinely ruled out. The dedicated signal spans 0.0 -> 0.9995 with real
within-seed variance (mean within-seed std rising 0.098 -> 0.225 across densities) and real
between-seed variance at intermediate densities (0.031 / 0.049 / 0.016). The AUC computation
is non-degenerate on **both** sides at tau=0.05 (AUC 0.99875) and tau=0.30 (AUC 1.0), so the
`dedicated_auc_computation_nondegenerate` flag -- which is a permissive `any(safe OR unsafe)`
over 18 thresholds and would be worth distrusting on its own -- is corroborated by thresholds
where the stricter both-sides condition holds. This is not a vacuous pass.

**But the criterion cannot meaningfully fail except on a wiring defect, and that is by
design.** Three structural facts:

1. `safety_proximity_harm` is a **deterministic environment-computed EMA of hazard proximity
   at the agent**. Its coupling to `num_hazards` is definitional, not empirical: the driver's
   own docstring predicts "safe(nh=0) ~0.0 vs unsafe(nh=8) ~0.87 **by construction** -> AUC
   ~0.95+".
2. At `num_hazards=0` the channel is **identically 0.0** (mean 0, std 0, max 0 in all 10 seeds).
   Since `SAFE_GROUP` contains that arm, every seed there has fire-rate **1.0 for any tau > 0**,
   so `reachability >= 0.5` is guaranteed for the whole sweep -- the `REACH_FLOOR = 0.15`
   sub-condition is unfailable given a wired channel. The AUC sub-condition then only needs the
   unsafe arms to sit above the same tau, which monotonicity supplies.
3. The `dedicated_signal_varies_with_density` precondition (0.331 vs a **0.001** floor) is,
   as the prompt suspects, effectively a **test of non-zero**, not a test of adequacy. It can
   only fail if the channel is flat -- i.e. wired off, `None`, or misconfigured -- which is
   exactly what the driver says it is for ("a flat signal means the dedicated channel is
   inert/misconfigured -> self-route `substrate_not_ready_requeue`, NEVER a substrate verdict").
   **It does not license the discrimination the label claims**, and the driver does not ask it
   to: discrimination is licensed by C1's AUC against the pre-registered `AUC_BAR = 0.75`,
   a separate and genuinely stronger statistic. The precondition is honestly scoped; the
   hazard is only that a reader treats 0.331 >> 0.001 as the discrimination evidence.

**Residual empirical content of C1, stated precisely** (this is what the run really bought):
(i) the dedicated channel is emitted, survives the `obs_dict` -> `_sense()` ->
`agent.sense(obs_safety_proximity=...)` path, and returns a finite value on **7500/7500**
ticks under `limb_damage_enabled=True`; (ii) it is **monotone** across 0 -> 8 hazards with a
clean exact-zero floor (the legacy `proximity_ema_sourced` channel measured by V3-EXQ-917 sat
at 0.464 at `nh=0`, so the zero floor is a property of the new channel, not of proximity
signals generally); (iii) the **shipped default threshold 0.25 sits inside the qualifying
band**. All three are wiring/calibration facts about a substrate build. None is a fact about
MECH-303's mechanism.

**The run never enables the MECH-303 gate.** Verified in source: `_cfg_kwargs()` sets only
`body_obs_dim`, `world_obs_dim`, `action_dim`, `use_harm_stream`, `harm_obs_dim`,
`use_affective_harm_stream`, `harm_obs_a_dim`. It does **not** set
`use_contextual_safety_terrain` (default `False`, `config.py:3286`) nor
`contextual_safety_gate_source` (default `"z_harm_a"`, `config.py:3330`). The
`accumulate_safety` block in `agent.py:5166-5212` is gated on
`use_contextual_safety_terrain` and therefore **never executed in this run**. So V3-EXQ-930
measured the two candidate **inputs** to a gate that was switched off. That is a legitimate
substrate-readiness measurement -- and it is decisively not a MECH-303 mechanism test.

---

## 3. The dissociation label: only ONE half is supported

`mech303_dedicated_signal_discriminates_zharma_does_not` is a **double claim**. A dissociation
needs both halves; they are not equally supported.

### 3a. Half A -- "the dedicated signal discriminates": SUPPORTED (load-bearing, near-analytic)

C1, AUC 1.0 at tau=0.08, band tau 0.02-0.30, acceptance target 0.84 exceeded. Real, as
Section 2 establishes -- with the near-analytic caveat that this is a wiring result.

### 3b. Half B -- "z_harm_a does not": MEASURED, WELL-POWERED AGAINST ITS OWN BAR, but NOT LOAD-BEARING and CONFOUNDED

**Power basis, stated explicitly (as the prompt requires).** Three separate things, in
increasing strength:

1. **Formal power against the pre-registered bar.** The AUC is computed on `n1 = 20` SAFE
   per-seed scores vs `n2 = 20` UNSAFE (2 densities x 10 seeds each). The null SE of a
   rank-biserial AUC is `sqrt((n1+n2+1)/(12*n1*n2))` = `sqrt(41/4800)` = **0.0924**. The
   observed best AUC of 0.52 is **+0.22 SE** above chance; the `AUC_BAR` of 0.75 is **+2.71
   SE**. By the null-SE approximation the design has roughly **77-80% power** at alpha=0.05
   two-sided to detect a bar-clearing effect. So "z_harm_a fails to clear AUC 0.75" is a
   **reasonably powered negative**, not a bare absence -- but only against that bar, and 20%
   of the time it would miss one.
2. **A same-run internal positive control on identical ticks -- much the stronger basis.**
   The identical 7,500 ticks, the same 50 cells, the same density manipulation drove the
   dedicated channel from 0.000 to 0.867 (`density_spread_std` **0.331**) while `z_harm_a`
   moved from 0.441964 to 0.441814 (`density_spread_std` **6.96e-5**). The manipulation is
   demonstrably effective; the control signal's response to it is **~4,760x smaller**. This is
   a measured invariance, not an underpowered null.
3. **Independent reproduction.** V3-EXQ-917's damage-sourced arm recorded per-density means
   "0.442 / 0.442 / 0.442 / 0.442 / 0.442 (flat to the 3rd decimal), AUC pinned at 0.500 at
   every one of 18 thresholds"
   (`evidence/planning/mech303_contextual_safety_threshold_reachability.md:122`).
   930 reproduces that to 3 decimal places on a different substrate commit. And the ledger's
   `q086-zharma-calibration-vs-ecological` question has **already adjudicated** this: leg
   `H-calibration-pathology` **confirmed**, `H-faithful-ecological` **eliminated**
   (resolved 2026-08-02 off V3-EXQ-857a; lineage back to V3-EXQ-664). So half B is the
   fourth observation of an already-settled regularity, not a new finding.

**Why it nonetheless does not carry the label. Four reasons, in order of force:**

- **(i) The run's own design says it is not load-bearing.** `combination_rule` names C2 a
  "REPORTED control, NOT load-bearing ... a surprising C2 PASS is a context note, not a run
  failure." A result the design declares non-load-bearing cannot be promoted to half of a
  headline dissociation by the self-route. This is precisely the "self-route is a hypothesis,
  not a verdict" case.
- **(ii) The agent is UNTRAINED, and the readout is dominated by a per-seed init constant.**
  There is no training loop anywhere in the driver -- no `backward`, no optimizer, no `.step()`
  on any learner; a fresh `REEAgent(cfg)` + `agent.reset()` per cell, then 150 sense/act ticks.
  `z_harm_a` is an unconditional every-tick forward pass through a randomly-initialised
  encoder. The data show the consequence directly: the **between-seed sd of cell means is
  6.4e-2 at every density**, while the **within-seed std is ~1e-3** -- the norm is pinned by a
  seed-dependent bias roughly **60x larger** than any within-run modulation, and the global
  range (0.343 to 0.547) is that init spread. An **absolute-threshold** sweep on an
  unnormalised norm with a 0.064 per-seed offset **cannot** discriminate regardless of how much
  information the signal carries. That is a property of the readout, not of damage-sourcing.
- **(iii) `z_harm_a` demonstrably DOES respond to hazard density in this very run -- the
  effect is just swamped.** Mean within-seed std rises **monotonically** with density:
  9.83e-4, 1.19e-3, 1.07e-3, 1.76e-3, **2.06e-3** -- a 2.1x increase from `nh=0` to `nh=8`.
  A per-seed-standardised or delta-from-own-baseline readout was **not computed**, and the
  per-tick series that would allow it was **not recorded** (the manifest keeps only per-cell
  mean/std/min/max and fire-rates). So the strong form "z_harm_a carries no context
  information" is **not established by this run**; only the weak form "an absolute-threshold
  gate on the raw norm cannot use it" is.
- **(iv) No manipulation check that the damage pathway was ever exercised.** The
  `both_signals_apparatus_reachable` precondition requires only `z_harm_a > 1e-9` and finite --
  which a constant untrained-encoder bias satisfies trivially. Nothing in the manifest records
  damage events, `harm_obs_a` magnitude, or heal dynamics, and with `heal_rate=0.4` over 150
  random-walk ticks it is entirely possible little damage accumulated. The reading "z_harm_a
  is spatially decoupled" (SD-022's *design intent*, so also the least surprising outcome)
  cannot be separated here from "the damage channel was barely driven".

**Net: the dissociation is half-supported and the label overstates.** The defensible
restatement, which governance should prefer:

> Under `limb_damage_enabled=True`, the dedicated proximity channel is monotone in hazard
> density and separable at a threshold band containing the shipped default (AUC 1.0, band
> tau 0.02-0.30, default 0.25 inside it). In the same ticks the damage-sourced `z_harm_a`
> norm is invariant to hazard density (spread 7e-5 vs 0.331), reproducing V3-EXQ-917 -- as
> SD-022's decoupling predicts by construction, and confounded here by an untrained encoder,
> an absolute-threshold readout dominated by a ~60x-larger per-seed init offset, and no
> recorded check that the damage pathway was exercised.

---

## 4. Claim-layer mapping (Step 3)

`MECH-303` -- context-bound passive safety representation (IL expression gating; vHipp->PL
contextual store; diffuse slow accumulation of harm-absence; output lowers background vigilance
threshold). `claim_type` `mechanism_hypothesis`, `status` **provisional**,
`live_status.reading` provisional (as_of 2026-07-15, promote applied off V3-EXQ-760),
`implementation_phase` `v3`, `v3_pending` **false**,
`pending_retest_after_substrate` **true**, `depends_on` `[SD-011, SD-012, ARC-007, MECH-304]`.
Lit basis present and specific (`evidence/literature/targeted_review_connectome_mech_303/`;
Kreutzmann 2020, Meyer 2019, Laing 2022, + Silva 2021 as a cluster-level enrichment anchor).

**`epistemic_category`: ABSENT.** Scanning the MECH-303 block
(`docs/claims/claims.yaml:46173-46382`) there is **no `epistemic_category` key at all**. So
the specific hazard the prompt raises -- *a prior autopsy stamping a category conditional on a
future run scoring, which then goes stale on its own terms while GOV-CAT-1 stays silent because
the field is present* -- **does not apply here in that exact form**: the field is not present,
so there is no stale conditional category to revisit.

**A conditional disposition DOES exist, in a different field, and its condition has now been
met.** The 2026-08-12 governance note (from
`failure_autopsy_V3-EXQ-916-916a-917-920-fishtank-cluster_2026-08-12`) sets
`pending_retest_after_substrate: true` explicitly conditioned on the dedicated signal landing:
*"the behavioural retest is owed once the dedicated signal lands"*. **The dedicated signal
landed 2026-08-14 (ree-v3 `b257e7ad14`).** So the condition is satisfied and the owed retest is
now **unblocked and actionable** -- but it has **not** been run, and V3-EXQ-930 is **not** it
(Section 2: the gate was never enabled). `pending_retest_after_substrate` must therefore
**stay true**. This is the item to put in front of the human.

**Claim-tagging note, worth recording.** The 916-cluster autopsy's V3-EXQ-917 target carries
`claim_ids: ["SD-011"]` -- **not** MECH-303 -- even though its entire finding is about
MECH-303's gate, and governance applied it to MECH-303's `evidence_quality_note` by hand. That
is why MECH-303's autopsy-target count is 0 (Section 7) despite a substantial autopsy history.
Not an error to fix retroactively, but a reader reconstructing MECH-303's history from
`targets[].claim_ids` alone will under-count it.

**Did the experiment test the claim under conditions where it could express itself? NO.**
MECH-303 asserts that accumulated context-exposure-without-harm forms a contextual safety store
whose output lowers background vigilance/avoidance commitment. V3-EXQ-930 measured the
separability of two candidate *input scalars* to that store's write gate, with the store
(`use_contextual_safety_terrain`) switched off, on an untrained agent doing a random walk, with
no behavioural readout of vigilance or avoidance at all. The claim had no opportunity to
express itself. **This is a substrate-readiness validation whose `claim_ids: ["MECH-303"]` tag
is a routing pointer, not an evidence tag** -- and the manifest's self-stamped
`evidence_direction: "supports"` for MECH-303 is the single most important thing this autopsy
corrects.

---

## 5. Biological-reference triage (Step 4)

**Closest reference mechanism.** MECH-303's own anatomy is well-grounded: IL required for
safety *expression* not acquisition (Kreutzmann 2020); vHipp->PL for safety-cue inhibition
(Meyer 2019); standard safety signal -> vmPFC + hippocampus, dissociated from conditioned
inhibitors -> dorsal striatum (Laing 2022). `lit_status` for the claim: **present**.

**The substrate change under validation is a FAITHFUL biological translation, not a formal
import -- and this is the strongest positive finding of the autopsy.** The build gives
MECH-303's gate an *anticipatory, exteroceptive hazard-proximity* signal instead of an
*interoceptive tissue-damage* signal. That is a real and well-attested dissociation in
mammals: contextual safety learning is driven by exteroceptive predictors of harm (the
threat-imminence continuum; PAG/hypothalamic and amygdalar circuitry reading distance-to-threat)
and is **not** computed from nociceptive/damage afferents, which run a separate
spinothalamic -> insula/S1 interoceptive route. A brain that inferred "this place is safe"
from tissue-damage signals would be unable to feel safe in an unfamiliar-but-benign environment
and unable to feel unsafe while undamaged -- exactly the pathology V3-EXQ-917 measured
(AUC 0.52) and 930 reproduces (AUC 0.52, spread 7e-5). **The failure of the damage-sourced
route is what biology predicts**, which retrospectively vindicates the 2026-08-12
user-adjudicated routing decision (option (a), dedicated signal; option (b), threshold retune,
rejected). It also aligns with SD-011's dual-stream separation (sensory-discriminative vs
affective-motivational).

**Does the failure resemble a missing biological dependency?** Yes, and it is a discovered
prerequisite rather than a falsification: the contextual safety store cannot form without an
*anticipatory* harm channel. That is positive evidence for the dependency, not against
MECH-303.

**`lit_status` for the specific sourcing dissociation: PARTIAL.** MECH-303 has a targeted
review; SD-011's dual-stream note carries the general separation. There is **no** targeted lit
entry specifically on *anticipatory threat-proximity vs tissue-damage sourcing for contextual
safety acquisition*. That is a small, non-blocking `/lit-pull` opportunity, not a routing
requirement -- the build already matches the biology, so nothing is gated on it. Recorded here
rather than routed.

---

## 6. Four-layer diagnosis (Step 5)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | The claim was not tested -- the gate was never enabled and no vigilance/avoidance readout exists. Not `weakened` and not `strengthened`: this run is orthogonal to the claim's content. |
| Biological reference | **clear** | Anticipatory exteroceptive proximity vs interoceptive damage is a genuine mammalian dissociation; the build is a faithful translation, not a formal import. The damage-sourced null is what biology predicts. |
| Developmental / dependency prerequisites | **present** | `SD-MECH303-THRESHOLD-SOURCING` landed 2026-08-14 (`b257e7ad14`); `depends_on` SD-011/SD-012/ARC-007/MECH-304 all implemented. |
| Implementation completeness | **partial** | The *channel* is complete and validated end to end (7500/7500 finite readings). The *gate* (`use_contextual_safety_terrain`, `contextual_safety_gate_source="proximity_signal"`) was never enabled in this run -- so the implementation of the mechanism under test is unexercised. |
| Environment adequacy | **partial** | The 0/1/2/4/8 density battery is adequate for the channel question. For the C2 half it is `unknown`: 150 random-walk ticks at `heal_rate=0.4` may generate little damage, and no manipulation check records whether the damage pathway was driven at all. |
| Measurement adequacy | **under-instrumented** | For C1, adequate (though the criterion is near-unfailable). For C2, **not**: an absolute-threshold sweep on an unnormalised norm carrying a ~60x-larger per-seed init offset, no per-seed standardisation, no per-tick series recorded, no damage-exposure readout. |
| Integration adequacy | **isolated** | Two scalars measured off a live pipeline in isolation; the gate -> terrain -> `accumulate_safety` -> `evaluate_safety` -> beta-gate-release chain is untouched. |
| Scale / capacity | **unknown** | Untrained agent, 150 ticks, random walk. Sufficient for a wiring check; says nothing about a trained agent's harm representation. |

### Failure-location summary (GOV-FAILLOC-1)

**Net classification: MIXED / NOT-A-FAILURE. No "REE failed" read is available or asserted.**

This target is a PASS, so no bucket is established as a failure location. Applying the gate's
prose rule (reach REE FAILED only when Implementation, Measurement and Environment each
independently read adequate/complete): Implementation reads **partial** (channel complete, gate
unexercised), Measurement reads **under-instrumented** for the half of the label that is in
dispute, Environment reads **partial** (damage exposure unverified). **All three fail the
adequacy test, so REE FAILED is unreachable by three independent routes.** For the specific
proposition that is *not* supported -- the label's negative half -- the limiting buckets are
**MEASUREMENT** (readout design) and **ENVIRONMENT** (damage-exposure adequacy). Nothing here
is chargeable to REE, to the mechanism, or to the claim.

### Recording-debt vs measurement-debt

The C2 gap is **both**, and the split matters for routing:

- **Recording-debt (cheaper, and the part to fix first):** the per-tick `z_harm_a` series and
  a damage-exposure readout **existed at run time** and were discarded -- the manifest keeps
  only per-cell aggregates. With those recorded, a per-seed-standardised discrimination could
  be computed with no new experiment. Per the Experimental Recording Standard
  (`evidence/planning/experimental_recording_standard_2026-07-12.md` sections 3b/3c) the repair is
  *recording* the readout, not re-running blind.
- **Measurement-debt (the deeper half):** even recorded, the *criterion form* (absolute
  threshold on an unnormalised norm) is the wrong instrument for a signal with a large per-seed
  offset. A within-seed-standardised or delta-from-baseline statistic is the redesign.

Because C2 is not load-bearing and its question is **already adjudicated** in the frozen ledger
(`q086` `H-calibration-pathology` **confirmed**), neither debt justifies a dedicated re-run.
Fold both into the **recording spec of the owed MECH-303 behavioural retest** (Section 8).

---

## 7. Re-derive brake (MOVE-3) and granularity-debt recurrence

**Brake count for MECH-303 under R1-R3: 0. The brake does NOT fire.**

Computed with the skill's recipe over all confirmed `failure_autopsy_*.json`:

```
tagging targets total: 0
ceiling hits:          0
```

- **R1 (unit = the RUN):** zero confirmed autopsy targets list `MECH-303` in their own
  `targets[].claim_ids`, so there is nothing to count at run granularity.
- **R2 (latest supersedes):** vacuous -- no prior adjudication of any MECH-303-tagged run.
- **R3 (`substrate_ceiling` only):** vacuous. This autopsy is **not** heading to a
  `substrate_ceiling` reading either (see Section 8), so it adds **0**; the count stays **0**
  after this artifact lands.

The neighbourhood is *not* empty -- 20 files under `evidence/planning/` mention `MECH-303`,
including the 916-cluster autopsy -- but per the binding counting convention those are the
claim's topical neighbourhood, not its recurrence cluster. The 916-cluster's 917 target tags
`SD-011`, not MECH-303 (Section 4).

**Granularity-debt recurrence trigger: DOES NOT FIRE.**
`scripts/granularity_debt_cluster.py MECH-303` reports **0 targets across 0 files**, so there
is no `claim_alignment` distribution to read and no `weakened` target -- both necessary
conditions are absent. MECH-303 is not showing granularity debt; it is showing a claim whose
first fair test has not yet been run.

**No `fanout_recommendation` is emitted.** The bottleneck is not a discrimination among >=2
live hypotheses -- it is one unambiguous, already-designed next experiment (the pre-registered
behavioural falsifier, now unblocked). GOV-FANOUT-1 explicitly exempts that case.

---

## 8. Learning extracted and repair pathway (Step 7)

**Work-graph classification.** The substrate is `complicated (buildable)` and **already
built**. The remaining MECH-303 question is `complex (probe-gated) / puzzle (known rules)`:
the frame is well-posed (does context-safety accumulation lower background vigilance?), the
rules are known, and a specific missing **fact** is what is wanted -> a **spike**, i.e.
`/queue-experiment`.

**Learning:**

1. A diagnostic can PASS non-degenerately on a criterion that is **near-unfailable given
   correct wiring**. `criteria_non_degenerate` was honestly `true` and the PASS is honestly
   real; neither fact makes the result mechanism-evidence. The discriminator to apply is not
   "did the metric vary" but "**could this criterion have failed for any reason other than a
   wiring defect?**" Here: no.
2. **A `claim_ids` tag on a substrate-readiness validation is a routing pointer, not an
   evidence tag.** The manifest self-stamped `evidence_direction: "supports"` for MECH-303
   from a run in which MECH-303's gate was never enabled. Left unadjudicated this would have
   entered the registry as a mechanism support.
3. **A self-routed label may assert more than the design's own `combination_rule` licenses.**
   The label names a dissociation; the combination rule names one of its two halves as an
   explicitly non-load-bearing reported control. Reading `combination_rule` against
   `interpretation.label` is a cheap, general check that catches this class.
4. **An absolute-threshold criterion on an untrained encoder's norm is structurally unable to
   discriminate** when the per-seed initialisation offset (6.4e-2) exceeds the within-run
   modulation (~1e-3) by ~60x -- while the modulation itself rises monotonically with the
   manipulation. The null is real about the readout and silent about the signal.
5. **A control precondition can be trivially satisfiable.**
   `both_signals_apparatus_reachable` requires only `z_harm_a > 1e-9` and finite -- which a
   constant bias meets. "The signal is reachable" is not "the signal was exercised"; a
   pathway-exercise manipulation check is a different (and here absent) instrument.
6. Positive, load-bearing for the substrate: the **shipped default
   `contextual_safety_proximity_threshold = 0.25` is inside the qualifying band**
   (reach 0.648, AUC 1.0), and the acceptance target 0.84 is exceeded (1.0). The build's
   calibration choice is validated at the signal layer.

**Routing: `/queue-experiment`** -- the owed MECH-303 behavioural retest (a spike), now
unblocked by the landed substrate. Spec sketch for the queue entry:

- Enable the mechanism: `use_contextual_safety_terrain=True`,
  `contextual_safety_gate_source="proximity_signal"`,
  `contextual_safety_proximity_threshold=0.25`, `safety_proximity_signal_enabled=True`.
- Score MECH-303's **stated falsifiable prediction**, not the input channel: background
  vigilance / avoidance-commitment level falls in repeatedly-safe contexts relative to a
  MECH-303-ablated arm; and (per the claim's own text) context-conditioned safety extinguishes
  more slowly than MECH-304 cue-conditioned safety.
- **Train the agent** -- an untrained-encoder run cannot adjudicate a store that forms by
  accumulation.
- **Recording spec (closes the C2 recording-debt at no extra compute):** per-tick `z_harm_a`
  series or a per-seed-standardised summary; a damage-exposure manipulation check
  (damage events / `harm_obs_a` magnitude / heal dynamics); `stamp_recording_core(...)` per
  the Experimental Recording Standard sections 3b/3c.

**Substrate queue: `amend` `SD-MECH303-THRESHOLD-SOURCING`, not `create`.** The entry exists,
is `status: implemented_pending_validation` / `status_phase: validation_owed` / `ready: false`,
and names **V3-EXQ-930 as its `validation_experiment`** with acceptance "safe-vs-unsafe AUC
>=~0.84". **930 met that acceptance target (1.0).** Recommended amendments:

- Resolve the prior `failure_record` item (V3-EXQ-917, currently `resolved: "open"`) as
  **`resolved`** -- its `target` was "a threshold value and/or sourcing convention under which
  the live MECH-303 gate is both reachable and discriminates safe from hazardous contexts",
  and 930 supplies exactly that (qualifying band tau 0.02-0.30, shipped default 0.25 inside it,
  AUC 1.0, reach 0.648). **Caveat to record with the resolution:** 930 established this at the
  **signal** layer with the gate off; the gate-layer evidence is the build's own e2e smoke
  (recorded in the entry's `implementation_note`: "proximity gate fires 150/150 safe vs 6/150
  unsafe"), which is a build smoke, not a scored manifest. The residual gate-layer validation
  is discharged by the owed behavioural retest above.
- Flip `status_phase` `validation_owed` -> validated and `ready` false -> true, at governance's
  discretion given that caveat.
- Leave `severity: "degrading"` and `substrate_paths` unchanged -- this occurrence does not
  change the classification.

**Explicitly NOT recommended:** any `substrate_ceiling` reading (nothing ceilinged -- the
substrate performed as designed); any demotion (the claim was not tested); any re-run of the
C2 question as its own experiment (already adjudicated at `q086`, and not load-bearing here).

**Draft `evidence_quality_note` for governance to write on MECH-303** (exact text in the JSON
`recommended_evidence_quality_note`).

---

## 9. Hypothesis-space ledger (Step 9b) -- DRAFTED ONLY, nothing written

Per staging-mode constraints, `hypothesis_space_registry.v1.json` and its siblings were
**not** modified. The intended disposition is recorded in the JSON under
`hypothesis_space_ledger_pending`, and it is **"no ledger mutation recommended"**:

- **No MECH-303 question exists** among the 34 registered `qid`s, and this run does not warrant
  opening one: it is an apparatus validation, not a discrimination among rival hypotheses, and
  registering a question whose single "hypothesis" is near-analytic would inflate the
  Dimension-3 denominator without narrowing anything.
- **`q086-zharma-calibration-vs-ecological` is already fully adjudicated**
  (`H-calibration-pathology` **confirmed**, `H-faithful-ecological` **eliminated**, both
  resolved 2026-08-02 off V3-EXQ-857a). 930's C2 is a **corroborating observation** on an
  already-resolved leg, not a new adjudication. Appending a hypothesis to an already-adjudicated
  question is exactly the growth invariant 3 forbids absent a labelled fan-out or discovery
  event, and neither applies. Optionally, a confirming session may add
  `V3-EXQ-930` to `H-calibration-pathology.resolution.resolving_runs` as corroboration -- this
  is cosmetic, does not move `initial_frozen_count`, and is not required.
- The target's own `recommended_evidence_direction` is `non_contributory` **and does not
  discriminate any leg**, which by the Step 9b state-mapping table is the "leave alive / nothing
  to register" row. No pre-registered leg exists to leave alive.
- **Growth-restriction check:** not applicable -- no leg is being attached to any existing
  question.

---

## 10. Recommended dispositions (STAGING -- for confirmation, not applied)

| Field | Recommendation |
|---|---|
| `recommended_evidence_direction` (MECH-303) | **`non_contributory`** -- overrides the manifest's self-stamped `supports` |
| `recommended_epistemic_category` (MECH-303) | **`standard`** |
| `status` | **unchanged -- stays `provisional`** |
| `pending_retest_after_substrate` | **stays `true`** (condition met, retest not yet run) |
| `routing` | **`queue-experiment`** (owed behavioural retest, `complex (probe-gated) / puzzle`) |
| `recommended_substrate_queue_entry.action` | **`amend`** SD-MECH303-THRESHOLD-SOURCING (resolve 917 failure record; flip validation phase) |
| `re_derive_brake` | **does not fire** (MECH-303 ceiling count 0) |
| granularity-debt trigger | **does not fire** (0 tagging targets) |
| `fanout_recommendation` | **omitted** (single unambiguous next step) |

**Why `standard` and not a suppressing category.** `standard` is deliberate. MECH-303 must
remain **v3-testable** and must remain visible to GOV-GRAN-1: the whole point of this cycle is
that its first fair mechanism test is now *possible for the first time*.
`substrate_ceiling` / `substrate_conditional` / `out_of_domain` / `derivational` would each
mark the claim not-v3-testable and starve it of experiment lanes at exactly the moment its
substrate blocker was cleared -- the opposite of the true state. The failure-mode diagnosis
("apparatus-layer validation, mechanism untested") lives in the note fields, not in the
category, per the enum discipline.

---

## 11. Items for the human at the confirmation gate

1. **Confirm the direction override.** The manifest self-stamps `evidence_direction: supports`
   for MECH-303; this autopsy recommends `non_contributory`. The whole disposition turns on
   accepting that a run which never enabled `use_contextual_safety_terrain` is not mechanism
   evidence.
2. **Confirm the dissociation label is half-supported.** Should the label be recorded as
   overstated (recommended), or is the C2 reproduction considered sufficient given the
   independent `q086` adjudication? The autopsy's position: the empirical regularity is real
   and thrice-reproduced, but it is *not this run's finding*, it is not load-bearing here, and
   it is confounded by an untrained encoder and an unverified damage manipulation.
3. **Confirm the substrate-queue amend, including how far to go.** Resolve 917's
   `failure_record` item and flip `status_phase`/`ready` on **signal-layer** evidence plus the
   build's own e2e smoke -- or hold `ready: false` until the gate-layer behavioural retest
   scores? Governance's call; the autopsy leans to resolving the failure record while noting
   the caveat, and leaving the `ready` flip to governance's judgement.
4. **The owed MECH-303 behavioural retest is now UNBLOCKED and unqueued.** Its precondition
   ("once the dedicated signal lands") was met on 2026-08-14. Per the 2026-07-30 rule this
   autopsy does **not** chip it; `/governance` chips it once the routing is ratified -- and
   should first check `igw_routine_ledger.json` / `igw_assignments.json` for an
   auto-discovered duplicate.
5. **Optional, non-blocking:** a small `/lit-pull` on anticipatory threat-proximity vs
   tissue-damage sourcing for contextual safety acquisition (`lit_status: partial` for that
   specific dissociation). Nothing is gated on it -- the build already matches the biology.
