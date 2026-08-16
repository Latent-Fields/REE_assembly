# Failure Autopsy — V3-EXQ-927 + V3-EXQ-928 (MECH-267 CEM selection fix validation)

- **Generated:** 2026-08-16T17:20:29Z
- **Scope:** cluster (2 manifests, but ONE measurement — see "Cluster shape")
- **Status:** confirmed (interactive gate answered 2026-08-16)
- **Trigger:** two `experiment_purpose: "diagnostic"` PASSes, both flagged `vacuous_pass` by the indexer
- **Claim:** MECH-267 (context tag only — diagnostic, excluded from governance confidence/conflict scoring)

---

## 0. Dry-run gate (Step 2a) — clean

`scripts/check_dry_run_citations.py` over both run_ids and both queue_ids:
`0 dry cited, 0 dry in named families, 0 ambiguous, 2 clean, 0 unknown` (exit 0).
Both manifests carry top-level `dry_run: false` / absent-falsy.

`validate_experiments.py --checks dry_run_unreachable_criterion` is **silent** on this
lineage (it fires on the `v3_exq_543` b–l family only). Per the standing caution, a silent
lint is a net and not an all-clear, so the driver's dry-run reduction block was read
directly: the `--dry-run` path reduces seeds and does not gate any reported detector on an
absolute mid-training episode index. No unsettable criterion.

- **Run ids checked:** `v3_exq_927_mech267_cem_selection_fix_validation_20260814T012404Z_v3`
  (dry_run false), `v3_exq_928_mech267_cem_selection_fix_validation_20260814T013434Z_v3`
  (dry_run false).
- **Excluded dry run_ids:** none.
- **Real-run denominator for every statistic below: 30 seeds x 4 arms x 4 modes = 480 cells.**

## 0b. Recording provenance — complete

`ree-v3/validate_recording.py --paths <both>` -> `2 complete, 0 always-core gaps,
0 thin-pack provenance drops, 0 schema warnings`. Both carry `recording_schema`,
`substrate_hash`, `substrate_commit`, `machine` / `machine_class`, `elapsed_seconds`,
full `config`, and the explicit 30-seed `seeds` list. **There is no recording gap here** —
the readout that decides this adjudication is present in the manifest (see §3). That
matters for routing: the repair is NOT a re-run.

---

## 1. Facts

### 1a. Cluster shape — these are NOT two replicates

`git log --follow experiments/v3_exq_928_mech267_cem_selection_fix_validation.py`:

```
73f07e4 V3-EXQ-928: rename MECH-267 CEM-fix validation from burned id 927
44fd045 SD-MECH267-CEM-SELECTION-FIX: H2 mode-value term + H3 persistent mode breadth
        (both no-op default); queue V3-EXQ-927 validation
```

Only **one** driver file exists in `ree-v3/experiments/`. V3-EXQ-927 is a **burned queue
id**; 928 is the same driver re-run ~10 minutes later under the new id.

Every numeric field is **bit-identical** between the two manifests —
`per_arm_mean_broad_minus_tight_gap`, `per_arm_n_seeds_positive_gap`,
`per_arm_mode_mean_raw_std`, `per_arm_adjacent_mean_gaps`, `per_arm_seed_broad_minus_tight_gaps`.

The two runs report **different** `substrate_hash` (`efd6a65b6cdd7d5a` vs
`5060ccf7f8974211`) and `substrate_commit` (`8aa975e9cc` vs `fed315c702`). That looks
alarming and is not: the diff between those commits is

```
CLAUDE.md                                                  |  2 +-
experiment_queue.json                                      |  6 +++---
... => v3_exq_928_mech267_cem_selection_fix_validation.py} | 14 +++++++-------
```

— **no `ree_core/` change whatsoever**; the 14 driver lines are the id strings changed by
the rename. The substrate under test is byte-identical across the two runs, the driver is
fully seeded (`torch.manual_seed(seed)` immediately before module construction, per-cell
sampling seeds), and the probe is deterministic. Bit-identical results are therefore the
**correct** outcome, and the pair is an inadvertent **exact-reproducibility positive
control** for this harness.

**Recording defect:** neither manifest declares `supersedes`. The indexer consequently
treats them as two independent diagnostic runs against MECH-267 — one measurement
double-counted in `pending_review.md` and in any MECH-267 population statistic. This is the
[memory] `feedback_burned_queue_id_is_not_untested_question` signature seen from the
manifest side.

### 1b. What the experiment measured

A **static proposer probe**, not an agent episode run (hence 31.9s / 20.2s for 480 cells —
legitimate, not truncation). For each (seed, arm): construct `HippocampalModule`, draw one
`(z_world, z_self)` pair shared across all 4 modes and identical across arms, pin each
operating mode to probability 1.0, call propose, read
`action_object_decoder_raw_output_stats.std_by_action_dim` from
`hip.get_last_propose_diagnostics()` — the exact key V3-EXQ-869/923 use.

- **Primary DV:** `broad_minus_tight_gap = raw_std[internal_planning] - raw_std[offline_consolidation]`
  (broadest predicted mode, `mode_noise_scale` 1.3, minus tightest, 0.3).
- **Acceptance per arm:** across-seed mean of that gap `>= FLOOR_PRODUCTION = 0.01`, at
  production `num_cem_iterations = 3`.
- **Arms** (differ ONLY by the two new no-op-default facets):
  OFF (control, the 869/869a/923 wash-out regime) / H2 `mode_value_weight` /
  H3 `mode_partitioned_cem` / BOTH.
- Both evidence directions pre-registered. Manipulation check: 480/480 cells engaged
  exactly as configured; `raw_std` populated on every cell.

### 1c. Expected vs observed, and which criterion failed

| criterion | load_bearing | passed | mean gap | floor |
|---|---|---|---|---|
| `C_manipulation_engagement_check` | true | **true** | 480/480 | — |
| `C_OFF_broad_minus_tight_gap_clears_floor` | false | false *(expected)* | −0.00309 | 0.01 |
| `C_H2_broad_minus_tight_gap_clears_floor` | **true** | **false** | −0.00162 | 0.01 |
| `C_H3_broad_minus_tight_gap_clears_floor` | true | true | +0.01363 | 0.01 |
| `C_BOTH_broad_minus_tight_gap_clears_floor` | true | true | +0.01112 | 0.01 |
| `C_at_least_one_fix_arm_clears_floor_with_off_washed_out` | true | **true** | fix_clearing = [H3, BOTH], off_clears = false | — |

**Failed criterion class: discrimination** (a per-arm localisation criterion), not an
absolute or negative-control criterion. The negative control behaved exactly as predicted
(OFF stayed washed out).

Both preconditions met (`manipulation_all_cells_engaged_as_configured` 1.0/1.0;
`raw_std_readout_populated_all_cells` 1.0/1.0), and every key of
`criteria_non_degenerate` is `true`.

---

## 2. The `vacuous_pass` flag — ADJUDICATED CLEARED (tagging artifact)

The flag fires via `build_experiment_indexes.py` rule **(3b)**: an overall PASS while a
criterion explicitly tagged `load_bearing: true` has `passed: false`. Here that is
`C_H2_broad_minus_tight_gap_clears_floor`.

The indexer is behaving exactly per its own documented rule. The rule's own comment says it
is "gated on the explicit `load_bearing` tag so it never over-fires on a legitimate M-of-N
pass" — and that gating is defeated here by the **driver's tagging**, not by the indexer.
The declared `combination_rule` is an explicit **disjunction**:

> PASS iff **>=1** fix arm's across-seed mean broad-minus-tight raw_std gap clears
> FLOOR_PRODUCTION while the OFF control stays washed out.

The author nonetheless tagged **all three** per-arm criteria `load_bearing: true`, which
encodes a *conjunction*. Under the actual rule, H2's sub-floor result is not a gate that
cleared on nothing — it is **the informative half of the localisation**: it is what
separates "the elite-selection value function was the missing locus" from "the refit
breadth was". The gate that genuinely carries the PASS,
`C_at_least_one_fix_arm_clears_floor_with_off_washed_out`, passed non-degenerately with the
manipulation confirmed on all 480 cells.

**Verdict: the flag is a criteria-tagging artifact and is cleared.** The fix direction is
the **driver/artifact**, not a widened indexer rule: an M-of-N or disjunctive gate should
tag the *aggregate* criterion `load_bearing: true` and the per-arm members
`load_bearing: false` (as this driver already, correctly, does for the OFF control arm).

This does **not** mean the run is sound as gated — see §3, which is a separate and more
consequential finding.

---

## 3. The label is right for the wrong reason — the gate is under-powered

The acceptance gate is a **single-arm mean against an absolute floor**, with no dispersion
scaling. Recomputed from `per_arm_seed_broad_minus_tight_gaps` (n = 30 per arm):

| arm | mean gap | sd | t vs floor 0.01 | paired vs OFF | t (paired) | seeds positive |
|---|---|---|---|---|---|---|
| OFF | −0.00309 | 0.01130 | −6.34 | — | — | 17/30 |
| H2 | −0.00162 | 0.01488 | −4.28 | +0.00147 | **+0.48** | 14/30 (diff 14/30) |
| H3 | +0.01363 | 0.01825 | **+1.09** | +0.01672 | **+4.34** | 21/30 (diff 24/30) |
| BOTH | +0.01112 | 0.01677 | **+0.36** | +0.01420 | **+4.02** | 21/30 (diff 23/30) |

Two things follow.

1. **The per-seed SD (0.011–0.018) is LARGER than the floor being cleared (0.010).** So
   "the across-seed mean cleared 0.01" is a near-chance event on its own: H3 sits t = +1.09
   above the floor and BOTH t = +0.36. Taken alone, neither arm's floor-clearing would
   survive any dispersion-aware test.
2. **The statistic that actually settles the question was computed and recorded but never
   gated on.** The paired, same-seed contrast against the OFF control gives
   H3 − OFF = +0.0167 (t = +4.34, 24/30 seeds positive) and BOTH − OFF = +0.0142
   (t = +4.02, 23/30), while H2 − OFF = +0.0015 (t = +0.48, 14/30) is a clean null.

So the self-routed label `fix_effective::H3+BOTH` is **substantively correct and
well-powered** — but the gate it cleared is not what makes it correct. The paired-versus-
control contrast is.

**Root cause of the gate defect.** The parent-session smoke that calibrated
`FLOOR_PRODUCTION = 0.01` measured OFF ~ 2.1e-6 and H3-ON ~ 0.0172 — an apparently clean
separation from a single-seed point estimate. The 30-seed reality is OFF mean −0.0031 with
sd 0.0113. The smoke badly understated seed-level dispersion, and the floor inherited that.
This is precisely [memory] `feedback_effect_size_pass_gate_margin` ("scale on SD of delta
+ absolute floor") going unmet: the design used the absolute floor and omitted the SD-of-
delta term, on a quantity whose noise exceeds the floor.

**Consequence for routing:** none of this requires a re-run. The decisive statistic is
already in the manifest — this is a `mystery (known data)` for the gate question (reframe
/ re-operationalise, do not gather), not a `puzzle (known rules)`.

---

## 4. Genuine narrowing — H3 restores the endpoint contrast, NOT the ordered gradient

`per_arm_all_adjacent_gaps_clear_floor` is **false in all four arms**, including H3 and
BOTH. The three adjacent predicted-order gaps (reported, non-gating):

| arm | planning − task | task − replay | replay − consolidation |
|---|---|---|---|
| OFF | −0.00194 | −0.00016 | −0.00098 |
| H2 | −0.00194 | +0.00308 | −0.00275 |
| H3 | **+0.00729** | **+0.00750** | **−0.00116** |
| BOTH | +0.0073 (approx) | +0.0075 (approx) | −0.0012 (approx) |

H3 does move the gradient where OFF does not: the first two adjacent steps go from
~zero/negative to clearly positive. But **each step remains below the 0.01 floor, and the
final step (internal_replay -> offline_consolidation) inverts.**

So the demonstrated result is: **H3 restores the extreme-pair (broad − tight) breadth
separation; it does not restore the predicted monotone four-mode gradient.** Describing
this run as "mode-content persistence rescued" would overclaim. The locus is settled; the
restoration is partial.

---

## 5. Production-inertness — the validated fix is a no-op by default

- `ree_core/utils/config.py:2177` — `mode_partitioned_cem: bool = False`
- `ree_core/utils/config.py:2163` — `mode_value_weight: Dict[str, List[float]] = field(default_factory=dict)`

Both facets default OFF. This is correct and deliberate for the *build* (no-op default
means every pre-existing call site is bit-identical), and it is exactly what made this
clean four-arm localisation possible. But it means that **as of this autopsy, MECH-267's
mode-conditioned proposal content is still washed out in production**, and every other
experiment touching `HippocampalModule.propose_trajectories` continues to run the
washed-out regime.

This is [memory] `reference_claim_status_vs_default_off_flag` — "claim status != flag
default; check the knob first." The substrate exists and is validated; the knob is off.

---

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | diagnostic run discriminating between causal loci for an already-established FAIL; does not test MECH-267's core prediction directly, and does not bear on it either way |
| Biological reference | **partial** | closest mechanism: mode/state-dependent hippocampal replay content + prioritized memory access (Pfeiffer & Foster 2013; Mattar & Daw 2018; Wikenheiser & Redish 2015). Targeted lit-pull complete (`targeted_review_connectome_mech_267`, 5 entries). Not a formal-definition import; the CEM elite-refit is an engineering substrate whose mode-blindness has no biological counterpart to defend |
| Prerequisites | **present** | both facets built (SD-MECH267-CEM-SELECTION-FIX, landed 2026-08-14) and runtime-confirmed engaged on 480/480 cells |
| Implementation | **partial** | fix works but is default-OFF (§5); and it restores only the endpoint contrast, not the ordered gradient (§4) |
| Environment | **adequate** | a static proposer probe is the correct bed for a question about CEM refit breadth; no episode dynamics required |
| Measurement | **under-instrumented** | absolute floor smaller than the per-seed SD of the gated quantity; the decisive paired-vs-control statistic was recorded but not gated (§3) |
| Integration | **isolated** | by design — single-module probe |
| Scale | **adequate** | 30 seeds x 4 arms x 4 modes; paired design across arms |

### Failure-location summary (GOV-FAILLOC-1)

- **MECHANISM FAILED** — *partial*. Implementation reads `partial`, not `complete`: the
  facet is default-off and the restoration is endpoint-only.
- **MEASURES FAILED** — *established*. Measurement adequacy reads `under-instrumented`: the
  gate cannot distinguish its own effect from seed noise.
- **ENVIRONMENT FAILED** — *not established*. Environment adequacy reads `adequate`.
- **REE FAILED** — **false**. Requires all three of Implementation / Measurement /
  Environment to read adequate-or-complete independently; two do not.

**Net classification: MIXED (MEASURES + MECHANISM) — not chargeable to REE.**

### Recommended epistemic category

`standard` for MECH-267. The finding is a measurement/test-design + implementation-gap
result, which is the behaviour-preserving mapping: it asserts no epistemic suppression, and
keeps the claim inside GOV-GRAN-1 surfacing and v3-testability. It is explicitly **not**
`substrate_ceiling` or `substrate_conditional` — the substrate for this locus now *exists
and works*; the outstanding item is a default flag, which is buildable, not a ceiling.

Note for the corpus: the two prior MECH-267 autopsies (869, 869a) carry
`competence_implementation_gap`, which is **out of the eight-value enum** in
`validate_claims.py:VALID_EPISTEMIC_CATEGORIES`. That failure mode is recorded here rather
than propagated — the diagnosis goes in the note fields, the category stays in the enum.

---

## 7. Re-derive brake and granularity-debt trigger

**Re-derive brake (MOVE-3): DOES NOT FIRE.** Counted under the binding R1–R3 convention
(R1 unit = run; R2 latest adjudication supersedes; R3 only `substrate_ceiling` counts):

| run | latest category | counts? |
|---|---|---|
| `v3_exq_869_...` | `competence_implementation_gap` | no (R3) |
| `v3_exq_869a_...` | `competence_implementation_gap` | no (R3) |
| `v3_exq_923_...` | `standard` | no (R3) |

**Ceiling hits for MECH-267 = 0**, against `RE_DERIVE_BRAKE_THRESHOLD = 2`. No refusal is
owed. (The driver's own header asserted a count of 2 and declared the brake "released" on
substrate-now-built grounds; under R1–R3 the count is 0, so the release was correct, though
for a different reason than stated. Recorded so the number does not diverge again.)

**Granularity-debt recurrence trigger: DOES NOT FIRE.**
`granularity_debt_cluster.py MECH-267` reports **3 targets across 3 files**, alignment
distribution **intact=1, other=1, unclear=1** — **no target reads `weakened`**. Per the
standing rule, a cluster with no `weakened` target is measurement or implementation debt,
not granularity debt, however many autopsies exist. The one `other` was read directly
(869: "claim not tested under conditions where it could fully express itself — only 1 of
>=2 claimed mechanisms was implemented") and is implementation debt, confirming the read.
The tagging targets are:

- `failure_autopsy_V3-EXQ-869_2026-08-02` — `v3_exq_869_...` — non_contributory / other
- `failure_autopsy_V3-EXQ-869a_2026-08-03` — `v3_exq_869a_...` — non_contributory / unclear
- `failure_autopsy_V3-EXQ-923_2026-08-12` — `v3_exq_923_...` — non_contributory / intact

No `/claim-synthesis` routing is owed.

---

## 8. Learning extracted

1. **A disjunctive (M-of-N) acceptance rule must not tag its per-member criteria
   `load_bearing: true`.** Doing so makes the indexer's aggregation-vacuity rule (3b) fire
   on the very member whose failure is the informative result. Tag the *aggregate*
   criterion load-bearing and the members not — as this driver already does correctly for
   its control arm. Fix direction is the driver, never the indexer rule.
2. **A PASS gate on an absolute floor is invalid when the per-seed SD exceeds the floor.**
   Here sd 0.011–0.018 against floor 0.010, giving t = +1.09 / +0.36 for the two "clearing"
   arms. Gates must carry an SD-of-delta term alongside the absolute floor.
3. **A single-seed smoke must not calibrate a floor.** The smoke read OFF ~ 2.1e-6; the
   30-seed distribution is mean −0.0031, sd 0.0113. Floor calibration needs a dispersion
   estimate, not a point estimate.
4. **Prefer the paired same-seed contrast against the control arm as the gated quantity**
   when the design already shares seeds across arms. This run's design was strong enough to
   support t = +4.34; only the choice of gated statistic wasted it.
5. **A burned queue id that is re-run under a new id should stamp `supersedes` on the new
   manifest.** Absent it, the indexer double-counts one measurement (here 927 + 928 as two
   diagnostic runs against MECH-267).
6. **A no-op-default facet is not a delivered fix.** Validating H3 does not change
   production behaviour while `mode_partitioned_cem` defaults False.
7. **Incidental positive control:** a deterministic seeded probe re-executed 10 minutes
   later, across a `substrate_hash` change carrying no `ree_core/` delta, reproduced every
   metric to the last decimal. Useful reproducibility evidence for this harness.
8. **`substrate_hash` moved on a `CLAUDE.md` + queue-snapshot + driver-rename change with
   no `ree_core/` delta.** Not investigated here (out of scope), but noted: if the hash is
   that sensitive, arm-reuse fingerprint matching may be missing legitimately reusable
   cells. Flagged for whoever owns GOV-REUSE-1, not routed from this autopsy.

---

## 9. Routing (confirmed at the interactive gate, 2026-08-16)

**Primary: `implement-substrate` — amend `SD-MECH267-CEM-SELECTION-FIX`.**

The entry is currently `status: implemented_pending_validation`, `priority: 1`,
`severity: degrading`, `substrate_paths: ['ree_core/hippocampal/module.py']`, titled
*"...(locus TBD: mode-aware value-function term or partitioned candidate pools)"*.

This run **resolves that "locus TBD"**: it is the partitioned/refit-breadth locus (H3),
not the value-function locus (H2). Governance should:

1. Record the locus resolution in the entry title/hint (H3 `mode_partitioned_cem`; H2
   `mode_value_weight` is a confirmed null and can be left default-off or retired).
2. Mark the existing V3-EXQ-923 `failure_record` item **`resolved`** — the wash-out it
   named is closed at production `num_cem_iterations = 3` by the H3 facet, on a paired
   vs-control contrast of t = +4.34.
3. Append a **new** `failure_record` item for the residual: the ordered four-mode gradient
   is not restored in any arm (all adjacent gaps sub-floor; final step inverted).
4. Route the **`mode_partitioned_cem` default flip** as the buildable next step —
   `complicated (buildable)`, no open question. Downstream behavioural validation after the
   flip is `complex (probe-gated)` and is a separate, later item.

**Explicitly NOT routed:** a `/queue-experiment` re-run with a corrected gate. The decisive
statistic is already recorded in the manifest; re-running would gather nothing new. The
gate defect is captured as learning (§8.2–8.4) for future drivers.

**Not routed:** `/claim-synthesis` (trigger does not fire, §7); `/lit-pull` (targeted review
complete, 5 entries); `/diagnose-errors` (no crash); governance demotion (failure-location
is MIXED, §6 — demotion threshold not reached).

**Per CLAUDE.md Session Land Protocol step 6, this session does NOT `spawn_task` the above.**
The routing is a proposal; `/governance` Step 2b re-confirms it before Step 4/6a applies it,
and chips it once ratified.

---

## 10. Draft `evidence_quality_note` for governance (do not apply from here)

> V3-EXQ-928 (superseding burned-id V3-EXQ-927; identical measurement) localised the
> MECH-267 mode-content wash-out at production num_cem_iterations=3 to the CEM refit
> breadth, not the elite-selection value function. Four arms x 30 shared seeds: H3
> (mode_partitioned_cem) − OFF = +0.0167 paired, t=+4.34, 24/30 seeds positive; BOTH − OFF
> = +0.0142, t=+4.02; H2 (mode_value_weight) − OFF = +0.0015, t=+0.48, a clean null.
> Manipulation confirmed on 480/480 cells. The run's own acceptance gate (across-seed mean
> vs absolute FLOOR_PRODUCTION=0.01) is under-powered — per-seed SD 0.011–0.018 exceeds the
> floor, giving t=+1.09 (H3) and t=+0.36 (BOTH) against it — so the self-routed label
> `fix_effective::H3+BOTH` is correct on the paired vs-control contrast rather than on the
> gate it cleared. The indexer's `vacuous_pass` flag is adjudicated CLEARED as a
> criteria-tagging artifact: the declared combination rule is a disjunction (">=1 fix arm
> clears") while all three per-arm criteria were tagged load_bearing:true; H2's sub-floor
> result is the informative half of the localisation, not a gate cleared on nothing.
> NARROWING: H3 restores the extreme-pair (broad−tight) breadth separation only — the
> predicted monotone four-mode gradient is NOT restored in any arm (all adjacent gaps
> sub-floor; internal_replay→offline_consolidation inverts). Both facets default OFF
> (mode_partitioned_cem=False, mode_value_weight={}), so MECH-267 mode-conditioning remains
> washed out in production until the default flips. Diagnostic — excluded from confidence
> and conflict scoring; pending_retest_after_substrate remains true, now gated on the
> default flip rather than on a build.

---

## 11. Hypothesis-space ledger delta (Step 9b)

Question `mech267_content_persistence_cem_refit` (claims: MECH-267;
`initial_frozen_count` 5, `initial_frozen_count_at_registration` 5;
`growth_restriction: None` — **no growth-restriction gate applies**, and no growth is
performed: this is a pure **Mode B resolve** of two already-pre-registered legs).

| hid | axis | before | after | basis |
|---|---|---|---|---|
| `H-mech267-mode-aware-scoring` | representation | alive | **eliminated** | H2 facet engaged on all 480 cells and produced nothing: arm mean −0.0016 (sub-floor) and H2−OFF paired +0.0015, t=+0.48, 14/30. Discriminating non_contributory — sub-floor against a *passing* reference band (H3/BOTH) in the same run, with the negative control washed out as predicted. Bar met. |
| `H-mech267-partitioned-pools` | algorithm | alive | **confirmed** | H3 facet rescues the broad−tight breadth gap at production iters=3: H3−OFF paired +0.0167, t=+4.34, 24/30 seeds positive, OFF control washed out, manipulation confirmed. `met_elimination_bar: false` — the LOCUS is settled, but restoration is partial (ordered four-mode gradient not restored; all adjacent gaps sub-floor, final step inverted). |

Surviving after this append: **0 of 5** alive. The question's decisive locus is answered —
the wash-out is structural to the shared elite-refit breadth. `decision.decidable` is set
true; `decision_log_ref` is left null (human-owned).

No `fanout_growth_events` or `discovery_growth_events` entry is written: no hypothesis is
added, `initial_frozen_count` is unchanged at 5, and
`initial_frozen_count_at_registration` is preserved at 5.
