# Failure autopsy -- V3-EXQ-920a (uncensored single-life survival fishtank)

- **Generated (UTC):** 2026-08-16T18:27:57Z
- **Status:** `awaiting_human_confirmation` (STAGING MODE -- Step 8 interactive gate not run; routing drafted, not finalised)
- **Scope:** single
- **Target run_id:** `v3_exq_920_uncensored_survival_single_life_fishtank_20260814T223432Z_v3`
- **Target queue_id:** `V3-EXQ-920a`
- **Outcome:** PASS | `experiment_purpose: diagnostic` | `claim_ids: []` (untagged)
- **Self-route label:** `single_life_uncensored_survival_distribution_obtained`
- **Indexer adjudication:** `verified` (NOT flagged; see Section 5)

This is a clean, unflagged diagnostic PASS. Per the 2026-08-07 user-instructed
correction recorded in `/failure-autopsy` SKILL.md, a diagnostic PASS still requires
this autopsy regardless of adjudication flag. Nothing here edits `claims.yaml`, any
manifest, `review_tracker.json`, or `substrate_queue.json`.

---

## 1. Identity -- read this before citing anything in this lineage

**The `run_id` does not carry the queue letter.** The manifest's `queue_id` is
`V3-EXQ-920a`; its `run_id` is `v3_exq_920_..._20260814T223432Z_v3`, with no `a`.
An **earlier, different run** -- `v3_exq_920_..._20260811T210906Z_v3`, `queue_id`
`V3-EXQ-920` -- shares the identical run_id **stem** and is already adjudicated as
Target 4 of the confirmed cluster artifact
`failure_autopsy_V3-EXQ-916-916a-917-920-fishtank-cluster_2026-08-12.json`.

The two runs are separable **only by their timestamp segment**. Every consumer that
keys on the stem (a `--family v3_exq_920` sweep, a `failure_autopsy_V3-EXQ-920*`
filename glob, a run-pack directory name) sees one thing where there are two.
Coverage for this autopsy was therefore established by **full-run_id content match
across every `failure_autopsy_*.json`**, not by glob: 0 confirmed artifacts name the
08-14 run_id. Section 7 treats the mismatch as a defect in its own right.

Root cause, stated precisely because it constrains the fix: `EXPERIMENT_TYPE` is a
module-level constant in the driver
(`ree-v3/experiments/v3_exq_920_uncensored_survival_single_life_fishtank.py:271`) and
the driver was **reused byte-unchanged** for the re-queue -- only the `--seeds`
argument differed. The driver has no access to its own `queue_id`, so it cannot
encode the letter. This is not an authoring slip; it is structural to any
"same driver, different arguments" re-queue.

---

## 2. Dry-run gate (Step 2a) and recording provenance

```
scripts/check_dry_run_citations.py v3_exq_920_..._20260814T223432Z_v3
-- 0 dry cited, 0 dry in named families, 0 ambiguous, 1 clean, 0 unknown   (exit 0)
```

The target is a real run (`dry_run` absent/falsy). No cluster members, no population
statistics, so nothing else needed checking. `excluded_dry_run_ids: []`.

Recording standard (`ree-v3/validate_recording.py`): **complete**, 0 always-core
gaps, 0 thin-pack provenance drops, 0 schema warnings. `recording_schema: rec/v1`,
`substrate_hash` `ac1f6486e271...`, `substrate_commit` `bf769fb3a445` (clean, `main`),
`machine` `ree-cloud-2` / `machine_class` `linux-x86_64-py3.10-torch2.12.0+cpu`,
`elapsed_seconds` 22772.7, full `config`, explicit `seeds: [0,1,2,3,4,5,6,7]`.
`substrate_stable_across_run: true`, `lag_seconds: 0`, `drifted_since_resolved: false`.
There is **no recording debt in this run.** The 34.8 MB per-step companion
`_episode_log.json` is committed and holds full unthinned traces for all 8 lives
(every seed died `health_depleted`, and the driver's thinning policy keeps full
records for exactly those).

---

## 3. What ran, and what it measured

Design: TRUE single-continuous-life. `EVAL_EPISODES = 1`, `EVAL_STEPS = 20000`,
with `max_episode_steps` set equal to `EVAL_STEPS` as a post-construction setattr on
the 906b ecology tier, so the environment's own `step_limit` termination coincides
exactly with the driver's loop bound. `_observational_run()` calls `env.reset()` only
at a segment boundary, and there is one segment -- so **no body-respawn occurs
anywhere inside an observed life**. One life per seed, 8 seeds, one survival draw each.

Gating (driver lines 500-506):

| Criterion | load_bearing | Result |
|---|---|---|
| `core_channels_non_degenerate` | **true** | PASS -- all of `CORE_CHANNELS = [z_harm_a, z_harm_un, drive, z_goal]` above `STD_FLOOR = 1e-4` |
| `harm_pathway_trained` | **true** | PASS -- 96883 optimizer steps vs threshold 1 |
| `sufficient_uncensored_deaths` | **true** | PASS -- 8 vs `MIN_UNCENSORED_DEATHS_TOTAL = 4` |
| `freeze_not_locked`, `all_seeds_completed`, 10 x `channel_*` | false | all PASS (informational) |

Preconditions: `harm_pathway_trained` 96883 vs 1.0 (met); `all_seeds_completed`
8.0 vs 8.0 (met). `criteria_non_degenerate{}` holds 13 keys, **all `true`**.
`z_goal_stream`: 166773 ticks, 166765 active, 33879 writer calls, `writer_defect:
false`, `goal_state_present: true`, 8 agents -- the channel is live, no defect.

**Primary DV -- pooled single-life survival, one draw per seed:**

| | |
|---|---|
| lives | 8 |
| uncensored (`health_depleted`) deaths | **8 of 8** |
| right-censored at the 20000 ceiling | **0** |
| `pct_right_censored_pooled` | **0.000** |
| survival times (steps) | 628, 1008, 1432, 1816, 1846, 1944, 2517, 2527 |
| min / median / mean / max | 628 / 1831 / 1714.75 / 2527 |
| sd / CV | 670.2 / 0.391 |
| ceiling utilisation | max life = 2527 = **12.6%** of the 20000 cap; 13718 of 160000 budgeted steps realised |

The eleven informational channel criteria are the deliberate fishtank telemetry
maximalism recorded in standing guidance (record generously, never prune). They are
**by design**, not unfocused gating -- the run gates on three criteria and *reports*
fifteen.

---

## 4. Relationship to the 08-11 run, and to the 2026-08-12 cluster autopsy

### 4a. What differs

| | 08-11 (`V3-EXQ-920`) | 08-14 (`V3-EXQ-920a`, target) |
|---|---|---|
| `run_id` timestamp | `20260811T210906Z` | `20260814T223432Z` |
| outcome | FAIL | PASS |
| seeds | `[0]` (1 life) | `[0..7]` (8 lives) |
| `substrate_commit` | `fc0fb4ce5c7b` | `bf769fb3a445` (**+114 commits**) |
| `substrate_hash` | `1aea107827fd` | `ac1f6486e271` |
| machine | `ree-worker-1` | `ree-cloud-2` (same `machine_class`) |
| `elapsed_seconds` | 930 | 22773 |
| driver file | unchanged between the two runs | unchanged |
| `config` (33 keys) | -- | **byte-identical** |
| `enabled_default_off_flags` (72 keys) | -- | **byte-identical** |
| `supersedes` | `null` | `null` |

So the only *declared* experimental difference is the seed count. The environment
config and every default-off flag are identical. The substrate moved 114 commits,
which is **not** nothing -- see 4c.

### 4b. Is this a re-run, a fix-validation, or a supersession?

**It is a fix-validation of an infrastructure defect, and it functionally supersedes
the 08-11 run -- but nothing in either artifact says so.**

The queue entry that produced it is explicit (ree-v3 `8fc8bd3`):

> `V3-EXQ-920a: multi-seed re-run of 920 (explicit --seeds 0..7; workaround for runner
> seeds-not-in-CLI defect, per 916/920 autopsy Target 4; smoke PASS)`

That is a direct, named consumption of the confirmed 2026-08-12 cluster autopsy's
Target-4 routing (`routing: "queue-experiment"`). The Target-4 diagnosis was that the
08-11 run's FAIL was **not** a scientific finding at all: the queue entry declared
`"seeds": 8`, but `experiment_runner.run_experiment()` builds subprocess CLI args only
from the item's `"args"` field, so the driver's own `--seeds` default `[0]` silently
governed and 1 of 8 pre-registered seeds executed. Net classification there was
"infrastructure/execution defect; not chargeable to REE, mechanism, measurement, or
environment".

Under the EXQ versioning policy, a lettered iteration supersedes its predecessor and
the predecessor's evidence should not continue weighting governance where the bug
invalidated its result. **That condition is squarely met** -- the 08-11 result was
invalidated by an execution defect, and 920a is the corrected iteration of the
identical scientific question on the identical config. Yet:

- neither manifest carries `supersedes`;
- the queue entry for 920a carries no `supersedes` field;
- the 08-11 manifest's `evidence_direction` was never set to `superseded`;
- the driver's own `summary_markdown` -- generated identically for **both** runs --
  says "Supersedes V3-EXQ-912's segment-count-scaling workaround", which is a
  *methodological* statement about a **different** experiment (912) and says nothing
  about the 08-11 sibling. A reader of the 08-14 artifact alone has no way to learn
  that a failed predecessor exists.

**This is a finding, per the standing instruction that an undeclared supersession is
itself reportable.** The practical governance exposure is limited rather than absent:
the 08-11 run was already adjudicated `non_contributory` + `standard` by the confirmed
cluster artifact, so it is not silently weighting anything. What is lost is the
*mechanical* link -- the indexer's supersession path (`evidence_direction:
"superseded"` -> inactive) is not engaged, and the two runs remain distinguishable
only by timestamp (Section 1).

### 4c. Do not pool the two runs

The 08-11 single life (seed 0, 1475 steps, `health_depleted`) falls comfortably inside
the 08-14 distribution (628-2527, median 1831), which is a pleasing independent
consistency check across two machines. It is **not** a ninth data point: the substrate
hash differs across 114 commits, and seed 0 itself realised 1475 steps on the old
substrate versus 1944 on the new -- a 32% shift on a fixed seed, so the two runs are
not bit-comparable and the substrate drift demonstrably changed the trajectory.
**n stays 8.** Any later citation should quote n=8, never n=9.

---

## 5. Is the PASS real, or degenerate?

**Real.** Three independent reasons, in descending strength.

1. **The load-bearing gate has a demonstrated failure mode in this very lineage.**
   `sufficient_uncensored_deaths` (>= 4) is exactly the criterion the 08-11 sibling
   *failed* (1 observed vs floor 4), on the same driver and the same config. A gate
   that has been observed to fire against a real run three days earlier is not a gate
   cleared on nothing.
2. **The core-channel gate cleared with orders of magnitude of headroom, not
   marginally.** `STD_FLOOR = 1e-4`; observed `chan_max_std`: `z_harm_a` 2.638,
   `drive` 0.334, `z_goal` 0.126, `z_harm_un` 0.099 -- i.e. 3 to 4.4 orders of
   magnitude above the floor on every gated channel.
3. **The DV was not close to its own instrument ceiling.** The longest life used 12.6%
   of the 20000-step cap, so the "0% censored" result is not a boundary artefact.

**Why the indexer did not flag `vacuous_pass`, precisely.** The check fires when a PASS
carries any `false` in `criteria_non_degenerate{}` after exclusions. Here **every one
of the 13 keys is `true`**, so the check never engages -- the flag path is not reached
at all. This is worth stating exactly, because the run's shape (3 load-bearing gates,
11 informational channel reports) is the broad-report/narrow-gate pattern that
historically produced spurious `vacuous_pass` on this exact 906/665/664 lineage and
required the 2026-08-09 aggregate-scope exclusion in
`build_experiment_indexes.py`. That exclusion **was** available here --
`core_channels_non_degenerate` is `load_bearing: true`, `passed: true`, and its name
ends in `_non_degenerate`, which is exactly the licence condition -- so the aggregate
criterion correctly licenses the informational excess as belt-and-braces. But it did
not need to do any work on this run. Contrast the 08-11 sibling, whose
`channel_vigor` read `false`; had that run been a PASS, the exclusion would have been
load-bearing.

**Three honest degeneracy caveats, none of which touch the PASS:**

- `freeze_not_locked` is computed as `(total_freeze == 0) or (total_freeze <
  total_steps)`. With `total_freeze_fires = 0` the first disjunct is trivially true,
  so the criterion **cannot fail when the mechanism it monitors never fires**. It is
  `load_bearing: false` and does not license anything, but it is a criterion with no
  failing branch reachable in this run.
- `channel_vigor` passed at `chan_max_std = 0.00233` against a floor of `1e-4`, with
  `chan_mean_vigor = 2.6e-05`. Technically non-degenerate; functionally a floor-level
  channel. Informational, not core, so it is not load-bearing here -- but do not cite
  vigor from this run as an active channel.
- **`chan_max_std` is a MAX across seeds, so every channel criterion is monotonically
  easier to pass as seed count rises.** `channel_vigor` read `false` at n=1 (08-11) and
  `true` at n=8 (08-14) with no substrate change relevant to vigor. The core channels
  clear by 3-4 orders of magnitude either way, so this does not affect the gate -- but
  the informational channel criteria are **not seed-invariant** and a channel flipping
  `false -> true` between a 1-seed and an 8-seed run of the same driver is not evidence
  of a substrate change.

---

## 6. What the n=8 survival distribution can and cannot support

### 6a. Usable -- and the censoring question is settled

**Yes, usable, for the question it was built to answer.** `sufficient_uncensored_deaths`
sets its floor at 4 total uncensored deaths and 8 were observed, so the pre-registered
adequacy bar cleared at 2x. More importantly the censoring fraction is **0.000** -- not
merely low. There is no censored observation to model around, no survival-analysis
machinery required, and no estimator sensitivity to a censoring assumption. The
empirical distribution *is* the distribution of the 8 draws. That is the cleanest
possible version of this readout, and it is a genuine improvement over its
predecessor V3-EXQ-912 (93.3% right-censored, `n_uncensored = 4` out of 60 segments).

### 6b. What 8 draws support

- **A firm qualitative answer:** on this ecology tier, an unbroken single life ends in
  genuine `health_depleted` death, reliably, well inside 3000 steps. 8/8.
- **A crude central tendency:** mean 1715, median 1831, sd 670, se 237, approximate
  95% interval on the mean 1154-2275. Quote the interval, never the point estimate
  alone.
- **A decisive refutation of the run's own imported calibration assumption.** The
  driver's STEP-BUDGET CALIBRATION extrapolated 912's segment-level hazard
  (p ~= 4/60 = 6.7% per 500 steps) as approximately memoryless, predicting mean death
  at ~7500 steps and ~6.2% censoring per seed. Observed mean is **1715 -- 4.4x
  earlier** -- with 0% censoring. The driver was explicit that "this run's own result
  is itself the correct test of memorylessness, not an assumption to import from
  912", and the run duly falsifies it: hazard **rises** with within-life time, which is
  what an accumulating-damage (wear) process looks like and is not what a memoryless
  process looks like. Note this is *consistent* with 912 rather than contradicting it:
  every 912 segment began with a fresh body, so 912's estimate was a fresh-body hazard
  and was structurally incapable of seeing the wear term.
- **A demonstration that 912's death-time distribution was a truncation artefact.**
  912's uncensored deaths spanned 261-487 steps (mean 382). 920a's span 628-2527. The
  two ranges are **disjoint, with no overlap at all** -- every genuine single-life
  death here occurred later than the longest death 912 was structurally able to
  observe. 912's reported "death-time distribution" was a conditional-on-dying-within-
  500-steps distribution. It should not be cited as an organism survival distribution.
- **A striking dose-vs-time result, and the strongest scientific content in the run.**
  Reconstructing each life's harm-event count exactly from
  `lifetime_affective_occupancy` (`frac_harm_event x n_lived_steps_measured` recovers
  integers exactly): 93, 88, 81, 72, 98, 57, 94, 73 -- **mean 82.0, sd 14.0, CV 0.170,
  max/min 1.72**. Against survival *time* at CV 0.391 and max/min 4.02, the
  **cumulative harm dose at death is 2.3x more stereotyped than the time to death**.
  Spearman(harm-event rate, survival steps) = **-0.881**. The natural reading is that
  death occurs at an approximately fixed harm tolerance and survival time is
  essentially that budget divided by the encounter rate -- i.e. **this is a harm-dose
  distribution wearing the clothes of a survival distribution.** Flagged as a
  descriptive characterization at n=8, not a claim.

### 6c. What 8 draws cannot support

- **No distributional shape.** 8 points cannot distinguish lognormal from Weibull from
  gamma, and cannot estimate a hazard function. The wear-vs-memoryless call in 6b is a
  gross-magnitude argument (4.4x), not a fitted comparison.
- **No between-condition inference.** There is one arm. Nothing here compares
  anything to anything.
- **No competence inference, in either direction.** See Section 8 -- the environment
  makes death eventually certain, so survival time is not a competence measure.
- **The harm-dose result above is n=8 and reconstructed from a summary statistic.**
  It is a hypothesis worth one cheap reanalysis, not a finding to build on.
- **No pooling with 08-11 or with 912** (different substrate, different design).
- **The seed-3 anomaly is unexplained and should not be smoothed over.** Seed 3 spent
  **91.9%** of its life in the reef (the zero-harm safe zone) and nonetheless carried
  the second-highest harm-event *rate* (0.0714) and died second-earliest (1008 steps).
  Reef occupancy across the 8 seeds is essentially uncorrelated with survival
  (Spearman +0.095). Sheltering did not buy life. Whether that is a spatial artefact
  (a reef patch adjacent to a hazard corridor), boundary oscillation, or starvation
  inside a foodless safe zone is answerable **from the already-committed episode log**
  and is the single highest-value cheap follow-on this run generates.

---

## 7. Findings that are not about the survival result

### 7a. The `run_id` / `queue_id` mismatch -- measured, and reported without overstatement

Corpus scan over `REE_assembly/evidence/experiments/*.json` (flat manifests):

| Measure | Count |
|---|---|
| manifests carrying both `queue_id` and `run_id` | 733 |
| of those, `queue_id` is lettered (`V3-EXQ-NNN<letter>`) | 376 |
| lettered `queue_id` whose `run_id` omits the letter | **17 (4.5% of lettered)** |
| distinct `run_id` stems shared by 2 or more `queue_id`s | **10** |

The 17 split into two unrelated shapes and only one of them is harmful:

- **8 are the SD-068 family** (`V3-EXQ-778a..h`), whose run_ids are
  `v3_exq_sd068_<descriptive-variant>_diagnostic_...` and never encode the number at
  all. Seven distinct descriptive slugs across eight queue ids, so variants remain
  separable by slug. **Not a de-duplication hazard** (the single exception,
  778b/778c, shares a slug and is).
- **9 are genuine letter-drops** where the run_id carries the number but not the
  letter: `612c`, `612d`, `737a`, `737b`, `742a`, `742b`, `766a`, `914a`, **`920a`**.

The operational harm is measured by the **stem-collision** row, which is what any
family sweep, filename glob, or run-pack directory key actually resolves. Ten stems
collide corpus-wide; six are the letter-drop shape (`612c/612d`, `737/737a/737b`,
`742/742a/742b`, `766/766a`, `914/914a`, **`920/920a`**), one is `778b/778c`, and three
are a different naming shape (`596/602`, `790/791`, `742-m/742m-b`).

**Honest scale: this is rare, not systemic -- but it is recurring and unfixed.**
1.4% of manifests, 2.4% of lettered queue ids, 10 collisions out of roughly 700 stems.
Against that, the six letter-drop collisions span six unrelated experiment families
and stretch from 2026-05 (612) to 2026-08 (920a), so it is not a historical artefact
someone has since closed. The fully-timestamped `run_id` **is** unique corpus-wide, so
no evidence has actually been lost -- the exposure is that stem-keyed de-duplication
and coverage checks silently under-report, which is exactly how the parent session
nearly re-autopsied an already-covered run. Two independent fixes, neither of which
this artifact applies: consumers key on the **full** run_id or on `(queue_id, run_id)`,
never the stem; producers thread the runner-supplied `queue_id` into the manifest's
run-pack key so a same-driver re-queue is separable without a timestamp.

**Corroborating observation, recorded but not investigated (scope discipline):** two
*different* experiment drivers both hold `queue_id` `V3-EXQ-931` --
`v3_exq_931_cem_wanting_weight_selection_authority` (ran 2026-08-14) and
`v3_exq_931_sleep_gap9_need_arm` (authored ree-v3 `c38e083`, no runs recorded). That
is a queue-id collision rather than a run_id collision -- the same identifier-hygiene
family, opposite direction. Reported for governance; not chased here.

### 7b. `all_seeds_completed` is structurally blind to the defect it names

Its description reads "every requested seed produced exactly one completed single-life
observation (no early crash/truncation silently shrinking n)". Its implementation
(driver line 504) is `n_seeds_total == len(seeds)`, where `seeds` is **the list the
process was invoked with**. On the 08-11 run it reported `measured 1.0, threshold 1.0,
met: true` -- a clean pass -- while 7 of the 8 queue-declared seeds never executed.
It is a self-consistency check presented as a coverage check, and the one criterion in
the manifest that a reader would expect to have caught the 08-11 defect is the one
that structurally could not. On the target run it reads 8.0 vs 8.0, which is correct
but tells you nothing you did not already know.

This **sharpens** the 2026-08-12 cluster autopsy's Target-4 learning (which correctly
named the runner-side `args`-vs-`seeds` wiring gap) with the driver-side half: even a
correctly-wired runner leaves this criterion unable to detect a declared-vs-actual
seed shortfall, because it never sees the declared count. A criterion that compares
the run to its own arguments cannot detect that the arguments were wrong.

### 7c. The manifest's SLEEP-CADENCE note is STALE on this run's own substrate

Both the `interpretation.note` and the `summary.md` tell a future reader -- naming
`/failure-autopsy` explicitly -- that `total_sleep_cycles_fired = 0` is "EXPECTED",
because "a single-episode eval has no non-zero segment boundary to trigger
`sleep_loop.notify_episode_end()`", and the module docstring generalises this to "a
TRUE single unbroken life ... can NEVER sleep during that life, no matter how long it
runs."

**That structural claim was true for the 08-11 run and is false for the target run.**
Verified by ancestry: `5f14036` (`sleep_substrate:GAP-9 (v1 ceiling arm): within-life
sleep trigger`) and `c38e083` (`MELConsumer.need_crossed()` + `notify_waking_step`
wiring, registering the flag) are **ancestors of `bf769fb3a445`** (the target's
substrate) and **not** ancestors of `fc0fb4ce5c7b` (the 08-11 substrate). The knob
exists: `use_within_life_sleep_trigger: bool = False`
(`ree-v3/ree_core/utils/config.py:5426`), and it is **absent from this run's
`enabled_default_off_flags`**.

So the correct reading of 0 sleep cycles on the target run is **"the within-life sleep
trigger was default-off"**, not "within-life sleep is structurally impossible". The
outcome value is unchanged; the *reason* recorded in the artifact is wrong, and it is
wrong in the direction that misdirects -- a future reader following the note would
conclude a substrate change is still owed when it has already landed. This is the
standing "claim status is not the same as the flag default -- check the knob first"
pattern, arriving inside a manifest's own interpretive prose.

Consequence worth surfacing at the gate: **920a's design is the only bed in the corpus
that can actually exercise a within-life sleep trigger**, because it is the only run
with a continuous unbroken life and no segment boundaries. The designated validation
`v3_exq_931_sleep_gap9_need_arm` is authored and has recorded no runs.

---

## 8. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **n/a** | `claim_ids: []`. No claim is tested, supported or weakened. Nothing to align. |
| Biological reference | **partial** | No mechanism claim is under test. The *design* (one unbroken life, no respawn, death as terminal event) is a faithful organism-lifespan translation and is the point of the run. The observed dose-stereotypy (Section 6b) resembles a cumulative-injury / wear mortality process rather than a constant-hazard one, which is the biologically expected shape -- but with n=8 and no mechanism manipulation this is a resemblance, not a reference triage. |
| Prerequisites | **present** | `SD-FISHTANK-MAX-EPISODE-STEPS` landed (ree-v3 `9d3d148ff8`) and verified live by the driver's own substrate-readiness read. Harm pathway trained (96883 steps). All 72 default-off flags the 906b tier needs are enabled. |
| Implementation completeness | **partial** | The single-life design executed exactly as specified (8/8 lives, one segment each, no respawn, unambiguous `done_cause` on every life). But the organism under observation is incomplete in ways this design makes structural: **no consolidation of any kind occurs within a life** (0 sleep cycles -- for the flag-state reason in 7c, not the stated structural one), the eval is observational so there is no within-life learning, and `vigor` sits at floor. |
| Environment adequacy | **adequate for the DV; INADEQUATE for any survival-competence read** | It did exactly what it was built to do: elicit 8/8 genuine deaths with zero censoring. But `resource_respawn_on_consume: false` with 5 non-renewing resources on a 12x12 grid, plus scheduled limb damage (interval 50, p 0.5), scheduled external hazards (interval 50, p 0.5), and world-rule shift every 250 steps, makes this a strictly attritional world. Confirmed in substrate: the only `_respawn_resource()` path reachable at these settings is a diagnostic-only branch gated on `dual_cue_replace_on_early_consume`, and env drift moves hazards only, never replenishing resources. The reef is a zero-harm zone with no food. **Death is eventually certain here for any policy whatsoever.** |
| Measurement adequacy | **adequate for the primary DV; under-instrumented for the WHY** | `done_cause` and `realized_steps` are exact, unambiguous, and complete on all 8 lives; recording standard clean. The manifest carries no within-life hazard or health time series, so the memorylessness/wear question cannot be answered from the manifest alone -- but the per-step traces for all 8 lives **are** durably committed in the 34.8 MB episode log. This is therefore **not** a recording gap and routes to reanalysis, never to a re-run. |
| Integration adequacy | **coupled** | Full 906b stack live; `z_goal` stream shows 33879 writer calls, `active_frac` 0.99995, `writer_defect: false`. No isolation or coupling instability observed. |
| Scale / capacity | **adequate, and oversized** | The 20000-step ceiling was over-provisioned by roughly 8x -- the longest life reached 12.6% of it, and 13718 of 160000 budgeted steps were realised. Good for the censoring question (0% censored is unambiguous); expensive at 6.3 h wall clock. A successor can cut `EVAL_STEPS` to ~6000 with ample headroom. |

---

## 9. Failure-location summary (GOV-FAILLOC-1)

`claim_ids: []`, so the Claim-alignment row is `n/a` and the table above is the only
structured diagnosis available. GOV-FAILLOC-1's claim-free branch applies in full, and
this run is the exact case it was written for: an organism-level observation
("**REE died in every one of 8 lives, median 1831 steps**") that prose could easily
render as evidence REE itself failed to survive.

| Bucket | Reads from | Verdict |
|---|---|---|
| MECHANISM FAILED | Implementation completeness | **not_established** -- row reads `partial`. No within-life consolidation, no within-life learning, `vigor` at floor. |
| MEASURES FAILED | Measurement adequacy | **established** -- the primary DV is adequately, exactly measured. (Scope note: adequate for *when* death occurred, not for *why*; the *why* is answerable by reanalysis of committed data.) |
| ENVIRONMENT FAILED | Environment adequacy | **partial** -- adequate for eliciting death, which is what the design needed; inadequate to license any competence read, because non-renewing resources make death certain regardless of policy. |
| REE FAILED | all three | **false** |

**Net classification: MIXED -- and specifically, the 8/8 mortality observation is
chargeable to the ENVIRONMENT BY CONSTRUCTION, not to REE.** In a world whose food
supply does not renew, dying is the only available outcome; the survival time measures
how long the agent stretched a finite budget against a fixed harm-encounter rate. Two
of the three buckets fail their adequacy test outright, so REE FAILED is not reachable
and is not asserted anywhere in this artifact.

The positive framing is the accurate one: **no observation in this run is chargeable
to REE, in either direction.** The run neither demonstrates nor fails to demonstrate a
competence. It is a characterization run and it characterized what it set out to.

---

## 10. Learning extracted

1. TRUE single-continuous-life observation on the 906b ecology tier yields **8/8
   uncensored `health_depleted` deaths, 0.000 right-censored**, at 628-2527 steps
   (median 1831). The censoring problem that dominated V3-EXQ-912 (93.3%) is fully
   solved by the `max_episode_steps` route, at **less than half** 912's eval-step cost
   (13718 vs 29529) for **twice** the uncensored deaths (8 vs 4).
2. **912's death-time distribution (261-487) is a truncation artefact.** It is disjoint
   from and entirely below 920a's (628-2527). Do not cite 912 as an organism survival
   distribution.
3. **The memoryless calibration imported from 912 is refuted by 4.4x** (predicted mean
   ~7500 steps, observed 1715). Hazard rises with within-life time -- a wear process.
   912 could not have seen this: each of its segments began with a fresh body, so its
   estimate was a fresh-body hazard by construction.
4. **Cumulative harm dose at death (mean 82.0, CV 0.170) is 2.3x more stereotyped than
   time to death (CV 0.391)**, and harm-event rate anti-correlates with survival at
   Spearman -0.881. The survival distribution is plausibly a harm-dose distribution
   divided by an encounter rate. n=8, descriptive, one cheap reanalysis from settled.
5. **Reef (safe-zone) occupancy does not buy survival** (Spearman +0.095), and the
   91.9%-reef seed died second-earliest with the second-highest harm rate. Unexplained;
   answerable from the committed episode log.
6. **A lettered queue_id whose run_id omits the letter defeats stem-keyed
   de-duplication and coverage checks.** 17 of 376 lettered queue ids (4.5%); 10 run_id
   stems shared by 2+ queue_ids corpus-wide; 6 of those are the letter-drop shape,
   spanning 6 families and 2026-05 to 2026-08. Rare but recurring and unfixed. Root
   cause is structural: `EXPERIMENT_TYPE` is a module constant and the driver never
   sees its `queue_id`, so any same-driver re-queue reproduces it. No evidence is lost
   (full run_ids are unique); the exposure is silent under-reporting by stem-keyed
   consumers.
7. **`all_seeds_completed` compares realised seeds to the seeds the process was
   invoked with, so it cannot detect a declared-vs-actual seed shortfall** -- it read
   a clean `1.0 vs 1.0, met: true` on the 08-11 run while 7 of 8 declared seeds never
   ran. A criterion that checks a run against its own arguments cannot detect that the
   arguments were wrong. Driver-side complement to the 2026-08-12 Target-4 runner-side
   finding.
8. **A manifest's interpretive note can go stale against its own substrate.** The
   SLEEP-CADENCE note asserts within-life sleep is structurally impossible; the
   within-life sleep trigger landed in the target run's substrate (`5f14036`,
   `c38e083`) and is merely default-off (`use_within_life_sleep_trigger`). The outcome
   is right, the recorded reason is wrong, and the wrong reason points a future reader
   at substrate work that is already done.
9. **`chan_max_std` is a max across seeds, so channel non-degeneracy criteria are not
   seed-invariant** -- they get monotonically easier as seed count rises.
   `channel_vigor` flipped `false` (n=1) to `true` (n=8) with no relevant substrate
   change. Never read such a flip as evidence of substrate change.
10. **An undeclared supersession.** 920a is a fix-validation of an infrastructure
    defect diagnosed in a confirmed autopsy, and functionally supersedes the 08-11
    run under the EXQ versioning policy -- but `supersedes` is `null` on both
    manifests and absent from the queue entry, and the driver-generated summary
    mentions only the *methodological* supersession of a different experiment (912).

---

## 11. Routing (DRAFT -- staging mode; not finalised, not chipped)

**Primary: `none`.** The characterization succeeded on its own pre-registered terms.
There is no substrate gap to fill, no measurement redesign owed, no re-run owed, and
no claim to adjudicate. `recommended_substrate_queue_entry.action: "none"`.

Per the 2026-07-30 rule, a `/failure-autopsy` session does **not** `spawn_task` the
follow-on its own recommendation names. The four items below are **reported** for
`/governance` to ratify and chip at its own Step 2b/4/6a. Each is classified with the
work-graph debt vocabulary.

1. **Reanalyse the committed episode log** -- `complicated (buildable)`. All 8 lives
   have full per-step traces in the 34.8 MB companion. Three questions are answerable
   with zero new compute: the empirical within-life hazard function (does the wear
   reading in 6b hold up); the harm-dose-at-death hypothesis (6b) against per-step
   health rather than a reconstructed summary; and the seed-3 reef anomaly (6c). This
   is the highest value-per-unit-cost item this run generates, and it is **analysis,
   not an experiment** -- explicitly not a `/queue-experiment` route.
2. **Fix `all_seeds_completed` to compare against the DECLARED seed count** --
   `complicated (buildable)`, `/implement-substrate` or a driver fix. Requires the
   runner to pass the declared count through; pairs with the 2026-08-12 Target-4
   runner-side finding. Small, and it closes the driver-side half of a defect that has
   already cost one run.
3. **Correct or annotate the stale SLEEP-CADENCE note, and consider 920a's design as
   the bed for the within-life sleep trigger** -- `complicated (buildable)`. The note
   is in a landed manifest and must not be retro-edited; the correction belongs in the
   driver docstring and in any successor. Before queuing anything here, check
   `v3_exq_931_sleep_gap9_need_arm` -- it is the designated GAP-9 validation, is
   already authored, and has recorded no runs; a new experiment would duplicate it.
4. **Identifier hygiene: stem collisions and the 931 queue-id collision** --
   `complicated (buildable)`, infrastructure. Consumers key on the full run_id or
   `(queue_id, run_id)`; producers thread `queue_id` into the run-pack key. Section 7a
   carries the measured scale; treat as low priority (rare, no evidence lost) but do
   not close it as fixed -- it recurs.

**Explicitly NOT recommended:** a re-run at more seeds. The pre-registered adequacy bar
cleared at 2x and the censoring question is settled at 0.000; a bigger n would buy
distributional shape, which nothing currently needs. If a successor is ever queued for
a different question, cut `EVAL_STEPS` from 20000 to ~6000 (the longest observed life
used 12.6% of the ceiling) -- roughly a 3x wall-clock saving on a 6.3 h run.

---

## 12. Draft `evidence_quality_note` (for governance to write; NOT written here)

> V3-EXQ-920a (`v3_exq_920_..._20260814T223432Z_v3`) is a claim-free diagnostic
> characterization PASS and does not weight governance. It is the corrected iteration
> of V3-EXQ-920 (`..._20260811T210906Z_v3`), whose FAIL was an infrastructure defect
> (1 of 8 declared seeds executed) adjudicated in
> `failure_autopsy_V3-EXQ-916-916a-917-920-fishtank-cluster_2026-08-12`; 920a
> functionally supersedes it, though neither manifest declares `supersedes`. Result:
> 8 of 8 single continuous lives ended in genuine `health_depleted` death,
> `pct_right_censored_pooled = 0.000`, survival 628-2527 steps (median 1831, mean 1715,
> sd 670). The PASS is real, not degenerate -- its load-bearing
> `sufficient_uncensored_deaths` gate demonstrably failed on the 08-11 sibling three
> days earlier, and the gated core channels clear `STD_FLOOR` by 3-4 orders of
> magnitude. Two results are load-bearing for future design: V3-EXQ-912's reported
> death-time range (261-487) is a 500-step-cap truncation artefact, disjoint from and
> entirely below this run's; and the memoryless hazard extrapolated from 912 is
> refuted by 4.4x (predicted mean ~7500 steps, observed 1715), indicating an
> accumulating-damage process. Do NOT read the 8/8 mortality as evidence REE failed
> to survive: `resource_respawn_on_consume` is false with 5 non-renewing resources, so
> death is certain for any policy and the observation is chargeable to the environment
> by construction (GOV-FAILLOC-1 net classification: MIXED, not chargeable to REE;
> Implementation reads `partial` and Environment `partial`). The manifest's
> SLEEP-CADENCE note asserting within-life sleep is structurally impossible is STALE
> against this run's own substrate (`use_within_life_sleep_trigger` landed in
> `5f14036`/`c38e083`, ancestors of `bf769fb3a445`, and is merely default-off).
> No substrate entry, no re-run, and no claim disposition is owed; the outstanding
> value is a zero-compute reanalysis of the committed 34.8 MB episode log.

---

## 13. Standing checks

- **Re-derive brake (MOVE-3):** not applicable. `claim_ids: []` -- there is no claim to
  count `substrate_ceiling` readings against. `fired: false`.
- **Granularity-debt recurrence trigger:** does not fire. No claim is tagged, so
  `granularity_debt_cluster.py` has no target and no `claim_alignment` distribution to
  read. Recorded as `fires: false` for GOV-GRAN-1's standing sweep.
- **GOV-FANOUT-1:** no `fanout_recommendation`. There is no discrimination bottleneck
  -- the run answered its question and the outstanding items are buildable analyses,
  not rival hypotheses needing a portfolio.
- **`per_claim_recommendation`:** **empty by necessity, not by omission.** There is no
  `claim_id` to key on. GOV-APPLY-1 has nothing to check because there is no claim
  disposition to apply. This is stated rather than filled with an invented key.
- **`recommended_epistemic_category`: `standard`.** "No category applies" is spelled
  `standard`, never `n/a`. `standard` is the behaviour-preserving stamp for a
  claim-free diagnostic: it asserts no epistemic suppression, keeps the target outside
  `_EPI_SUPPRESS_PROPOSAL`, and is the same stamp the 2026-08-12 cluster artifact used
  for its two claim-free showcase targets.
- **`recommended_evidence_direction`: `non_contributory`.** Matches the manifest's own
  self-stamp and the precedent set for claim-free showcase runs in the 2026-08-12
  cluster. It means "contributes no claim-weighting evidence", which is exactly true;
  it emphatically does **not** mean the run was uninformative -- Section 10 lists ten
  extracted learnings.

## 14. Staging-mode status

Steps 1-7 and 9 were run in full. **Step 8 (interactive gate) was NOT run** -- there is
no user in this session. `status: "awaiting_human_confirmation"`; routing in Section 11
is a draft. **Step 9b was drafted only**: `hypothesis_space_registry.v1.json` was not
opened or written, and the intended ledger action is recorded under
`hypothesis_space_ledger_pending` in the JSON companion. No `TASK_CLAIMS.json` entry
was opened or closed (the parent session holds `cranky-driscoll-126a36-batch`), nothing
was committed or pushed, no chip was spawned, and no index or `pending_review.md`
regeneration was performed.

**For the human at the confirmation gate,** in priority order:

1. Confirm `non_contributory` + `standard` for a claim-free diagnostic PASS, matching
   the 2026-08-12 precedent -- or say if a claim-free characterization that genuinely
   answered its question deserves a different treatment. This is a live governance
   question beyond this run.
2. Confirm the supersession reading (Section 4b): should the 08-11 manifest's
   `evidence_direction` be set to `superseded`, or is its existing `non_contributory`
   adjudication sufficient? This artifact recommends **no manifest edit** -- the
   record is already correct, only the mechanical link is missing -- but the call is
   governance's.
3. Ratify the four follow-ons in Section 11 for chipping, especially item 1 (zero-compute
   reanalysis) and item 3 (check `v3_exq_931_sleep_gap9_need_arm` before queuing
   anything sleep-related, to avoid duplicating an already-authored validation).
