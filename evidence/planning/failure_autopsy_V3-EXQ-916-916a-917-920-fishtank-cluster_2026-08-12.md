# Failure Autopsy: V3-EXQ-916 / 916a / 917 / 920 -- Fishtank/harm diagnostic cluster

**Generated:** 2026-08-12T04:16:58Z
**Scope:** cluster (4 targets, `experiment_purpose: "diagnostic"`, mandatory adjudication per
`pending_review.md`'s "Diagnostic -- autopsy required" section, independent of `adjudication`
flag)
**Status:** confirmed (interactive gate run via AskUserQuestion, 2026-08-12)
**Dry-run check:** ran `check_dry_run_citations.py` over all 4 run_ids + all other pending
candidates this session considered -- 13 clean, 0 dry hits. None of these 4 targets are smokes.

---

## Why these four are bundled, and why this is NOT one structural cluster

All four are `experiment_purpose: "diagnostic"` results from the 2026-08-10/11 Fishtank/harm
testing lineage, selected together (user choice, presented against 8 candidate un-autopsied
targets from a freshly-regenerated `pending_review.md`) for session efficiency. **They are three
independent findings, not a convergent structural failure** -- see Cluster Read below. 916/916a
share a lineage (same driver family, a lettered fix); 917 is a standalone discriminating probe
answering an already-open question; 920 is mechanistically unrelated to the other three (no
MECH-302/303/304 involvement at all).

---

## Target 1 -- V3-EXQ-916 (Relief/Safety Fishtank Showcase)

**Facts.** `run_id=v3_exq_916_relief_safety_fishtank_showcase_20260811T064913Z_v3`,
`experiment_purpose=diagnostic`, `outcome=PASS`, `claim_ids=[]`, `evidence_direction=non_contributory`
(does not weight governance by design). Self-route label `relief_safety_showcase_channels_live`.
Follow-on to V3-EXQ-664, first driver to enable `use_suffering_derivative_comparator` (MECH-302),
`use_conditioned_safety_store` (MECH-304), `use_contextual_safety_terrain` (MECH-303) --
real, previously-validated substrate no prior Fishtank showcase driver had exercised.

PASS criteria (all load-bearing, all passed): core affect channels (z_harm_a/z_harm_un/drive)
non-degenerate across 3 seeds, blocked-agency pole engaged, PAG freeze not permanently locked.
Non-load-bearing channels `z_goal` and `vigor` read FLAT (`chan_max_std_z_goal=0.0`,
`chan_nondegen_z_goal=0.0`).

**Claim-layer map.** claim_ids=[] -- no claim weighted; n/a.

**Biological reference.** Closest mechanisms: MECH-302 (suffering-derivative comparator ->
relief, dependencies MECH-057a/MECH-091/MECH-094/MECH-303/SD-011/SD-012), MECH-303 (contextual
safety terrain, dependencies SD-011/SD-012/ARC-007/MECH-304), MECH-304 (conditioned safety
store, dependencies MECH-302/MECH-094/SD-011/SD-012/MECH-303). All three carry substantial,
already-registered lit-pull anchors in `claims.yaml` (Andreatta 2012, Navratilova 2012 PNAS,
Ramirez 2015, Tanimoto 2004 for MECH-302; Kreutzmann 2020, Meyer 2019 PNAS, Laing 2022, Silva
2021 Nat Neurosci for MECH-303/304). Not a formal-definition import; this run is a telemetry
showcase confirming already-validated substrate is observable, not a fresh claim test.

**Four-layer diagnosis.**

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim_ids=[] |
| Biological reference | clear | MECH-302/303/304, well-anchored in claims.yaml |
| Prerequisites | present | MECH-057a/MECH-091/MECH-094/SD-011/SD-012/ARC-007 all IMPLEMENTED |
| Implementation completeness | partial | z_goal/residue_wanting channels structurally flat -- see recording gap below |
| Environment adequacy | adequate | reef ecology tier, 3 seeds |
| Measurement adequacy | partial | benefit_exposure never reached update_z_goal (recording gap) |
| Integration adequacy | partially coupled | MECH-302/303/304 fire correctly; z_goal coupling broken |
| Scale / capacity | adequate | 3 seeds sufficient for a showcase PASS |

**Failure-location summary (GOV-FAILLOC-1).** Not a FAIL -- PASS on all load-bearing criteria.
The z_goal/residue_wanting flatness is a **recording gap** (readout existed at run time but was
never wired to the writer), not a measurement or environment inadequacy. n/a for
MECHANISM/MEASURES/ENVIRONMENT/REE-FAILED buckets (no failure to classify).

**Recording gap, traced and already resolved.** V3-EXQ-916a (below) found the root cause:
`REEAgent.update_benefit_salience()` / `update_schema_wanting()` are never called from this
driver family's step loop (orphaned writer, traced to
`failure_autopsy_906b-906c-911-cluster_2026-08-10.md` Finding 2), AND a second, independent
defect -- `benefit_exposure` is read from the wrong dict (`obs_dict` instead of `info`) and is
additionally gated on `use_proxy_fields=True`, which every 664-derived driver (664, 906, 909,
911, 912, 913, **and this run, 916**) leaves at its default `False`. So `benefit_exposure` has
been **structurally 0.0 across the entire lineage**, not just in this run.

**This is already fully resolved and documented** in `substrate_queue.json`'s
`SD-RESIDUE-VALENCE-BOUND` entry (`implementation_note` + `failure_record[1].resolved_note`,
both dated 2026-08-11, citing `ree-v3 26260a519634` = V3-EXQ-916a) -- a prior session's chip
(`chip-20260811-sd-residue-valence-bound-wanting-resolved`) already closed this. **No further
routing from this autopsy** -- confirming the existing resolution is accurate and complete.

**Recommended `epistemic_category`:** `standard`. **Recommended `evidence_direction`:**
`non_contributory` (unchanged). **Routing:** none (already resolved elsewhere; this autopsy
confirms).

---

## Target 2 -- V3-EXQ-916a (Relief/Safety Fishtank Showcase, residue_wanting writer fix)

**Facts.** `run_id=v3_exq_916a_relief_safety_fishtank_showcase_20260811T194142Z_v3`,
`experiment_purpose=diagnostic`, `outcome=PASS`, `claim_ids=[]`, `evidence_direction=non_contributory`.
Same self-route label as 916. Lettered iteration (same scientific question, broken
instrumentation, per CLAUDE.md EXQ versioning policy) applying two fixes: (1)
`tonic_5ht_enabled=True` (activates `update_benefit_salience`'s no-op guard, a genuine
mechanism-activation change, hence a new letter not a silent patch), (2)
`agent.update_benefit_salience(...)` wired into the step loop, (3) `use_proxy_fields=True` +
reading `info.get("benefit_exposure")` instead of `obs_dict.get(...)`.

**Result.** Seed-level simulation outputs (rewards, harms, freeze/relief fire counts) are
**bit-identical to 916** -- confirming the fix is purely instrumentation, not a behavioural
change. `chan_max_std_z_goal` moves from `0.0` (FLAT) to `0.07800` (varies, non-degenerate);
`residue_wanting` newly reported (`chan_max_std_residue_wanting=0.568`, non-degenerate). All
three core PASS gates (core-channel non-degeneracy, blocked-agency, freeze-not-locked) --
untouched by the fix -- remain independently satisfied. 916 is explicitly **not superseded**
(its own gates don't read the fixed channels).

**Four-layer diagnosis.**

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim_ids=[] |
| Biological reference | clear | same as 916 |
| Prerequisites | present | same as 916 |
| Implementation completeness | complete | fix applied and verified (bit-identical sim, new channels live) |
| Environment adequacy | adequate | same as 916 |
| Measurement adequacy | adequate | recording gap closed for THIS driver |
| Integration adequacy | coupled | z_goal/residue_wanting now correctly coupled |
| Scale / capacity | adequate | same 3 seeds |

**Lineage-wide caveat (explicitly flagged by the driver author, not retrofitted).** The fix
applies **only to this script**; 664/906/909/911/912/913/916 themselves are NOT retroactively
corrected (already-landed/already-scored predecessors, per CLAUDE.md's no-retroactive-edit
rule). Any prior claim evidence from those runs that depended on `z_goal` non-degeneracy should
be read with this in mind -- already captured in the SD-RESIDUE-VALENCE-BOUND entry's
`resolved_note`, which explicitly names the affected predecessors.

**Recommended `epistemic_category`:** `standard`. **Recommended `evidence_direction`:**
`non_contributory` (unchanged). **Routing:** none (fix landed and fully recorded).

---

## Target 3 -- V3-EXQ-917 (MECH-303 harm-threshold calibration battery)

**Facts.** `run_id=v3_exq_917_mech303_harm_threshold_calibration_battery_20260811T205119Z_v3`,
`experiment_purpose=diagnostic`, `outcome=PASS`, `claim_ids=[SD-011]`, `evidence_direction=supports`,
`non_degenerate=true`. Self-route label `mech303_tension_sourcing_mode_dependent`. Follow-on to
`evidence/planning/mech303_contextual_safety_threshold_reachability.md` (2026-08-11), which found
`REEConfig.contextual_safety_harm_threshold` (default 0.05) unreachable in every prior experiment
exercising MECH-303's live gate (V3-EXQ-520 had to override to 999; V3-EXQ-764 measured real
z_harm_a norms ~11x the default, safe vs unsafe barely distinguishable) and flagged the question
as `complex (probe-gated)`: is the reachability/discrimination tension an intrinsic SD-011
encoder limitation, or specific to a particular sourcing choice?

**Design.** 2 sourcing modes (`damage_sourced` = production default via SD-022 body-damage
re-sourcing, set by every prior driver that exercises this gate -- 764/520/916; vs
`proximity_ema_sourced` = pre-SD-022 legacy direct-proximity EMA) x 5 hazard-density levels x 10
seeds = 100 arms, 150 ticks each, random-walk policy (decouples internal computation from
walk direction). Per arm: reachability(tau) and safe(0,1)-vs-unsafe(4,8) AUC across 18 swept
thresholds. C1 (damage_sourced, production's own question) and C2 (proximity_ema_sourced,
mechanistic-reframe question) are independent load-bearing criteria; combination rule is
**PASS iff C1 OR C2**.

**Result -- a clean dissociation, not a uniform PASS.**
- **C1 (damage_sourced, production default): FAILED.** Across all 18 thresholds (0.02-0.8), AUC
  never exceeds **0.52** (chance = 0.50). No threshold both reaches the reachability floor and
  discriminates.
- **C2 (proximity_ema_sourced, legacy): PASSED.** AUC climbs to **0.84-0.97** across thresholds
  0.4-0.8, with reachability 0.23-0.98 across the same band -- both reachable and
  strongly discriminating.
- Overall PASS is driven entirely by C2; **the production default cannot calibrate a working
  threshold at all**, at any of the 18 values tested.

**Claim-layer map.** SD-011 (affective-harm encoder dual-stream architecture, `status=stable`,
`depends_on=[SD-010, ARC-027]`). This experiment's own `claim_ids` scoping (driver author's
choice, correct) tags SD-011 only -- MECH-303 itself is explicitly NOT tagged, since its own
representation-level validation (V3-EXQ-760, PASS) and claim are unaffected; this is a
downstream default-config usability question for MECH-303's live-path consumers, not a defect
in MECH-303's own mechanism.

**Biological reference -- the core move for this target.** SD-011's own `evidence_quality_note`
already carries the load-bearing biological grounding for exactly this kind of dissociation:
Melzack & Casey (1968) three-component pain model, Craig (2002/2003/2009) interoception, and
**Rainville et al. (1997, Science)** -- the gold-standard dissociation showing hypnotic
modulation of *unpleasantness* (affective-motivational) does not modulate S1 (sensory-
discriminative), i.e. the two pain components are functionally independent. Mapped onto this
finding: `damage_sourced` (accumulated body-damage, triggered only after tissue harm has
already occurred) is architecturally a **reactive, sensory-discriminative-style** signal --
closer to a nociceptive reflex than to context-driven threat appraisal. `proximity_ema_sourced`
(a slow EMA of spatial hazard/resource proximity, updating continuously and anticipating
contact before it happens) is architecturally an **anticipatory, affective-motivational-style**
signal -- exactly what MECH-303's own cited lit anchors (Kreutzmann 2020 IL/PL safety
expression, Meyer 2019 vHipp->PL safety-cue inhibition, Laing 2022 vmPFC+hippocampus safety
signal) describe as the substrate for *contextual* safety learning. Biologically, mammalian
threat avoidance is predominantly **anticipatory** (proximity/context-based amygdala-BNST
threat circuits), not reactive (having already been hurt) -- gating MECH-303's anticipatory
safety-terrain accumulation on a reactive damage signal is a mechanistic mismatch, and the
empirical result (chance-level discrimination under damage-sourcing, strong discrimination
under proximity-sourcing) is exactly what that mismatch predicts. This is a **load-bearing
biology divergence**, not a caveat to refine: SD-022's damage-sourcing choice was made for a
different consumer's purposes (body-damage tracking) and happens to be the wrong substrate for
MECH-303's specific anticipatory-safety purpose.

**Four-layer diagnosis.**

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | strengthened (with caveat) | resolves the open `complex (probe-gated)` reachability question; encoder CAN discriminate given correct sourcing |
| Biological reference | clear | Melzack/Craig/Rainville dual-pathway dissociation predicts exactly this result |
| Prerequisites | present | `z_harm_a_apparatus_reachable` = 1.0 across whole battery |
| Implementation completeness | complete (battery) / partial (production consumer) | the diagnostic itself is fully built; no production driver currently has a working threshold under damage-sourcing |
| Environment adequacy | adequate | 5-density x 2-mode x 10-seed battery, well-powered |
| Measurement adequacy | adequate | AUC/reachability construction is sound, non-degenerate by construction |
| Integration adequacy | partially coupled | encoder integrates correctly when sourced correctly; MECH-303's live gate is coupled to the wrong sourcing convention in production |
| Scale / capacity | adequate | 100 arms, 10 seeds each |

**Failure-location summary (GOV-FAILLOC-1).** Not a FAIL overall (PASS via C2), so this is a
mixed/nuanced read rather than a clean bucket: MECHANISM adequate (SD-011 encoder itself
discriminates fine under the right input), the defect is in which SIGNAL feeds it in
production -- an implementation/config-wiring issue at the MECH-303-consumer layer, not a
representation or measurement failure.

**Granularity-debt recurrence check.** Ran `granularity_debt_cluster.py` for SD-011 (6 prior
tagging targets, mostly grandfathered 2026-03/04 z_world-forward-model findings -- a
structurally different question, `alignment distribution: unclear=6, weakened=5`) and MECH-303
(0 tagging targets -- this run doesn't tag MECH-303 at all). Neither fires the recurrence
trigger for this finding: SD-011's history is dominated by an unrelated sub-question
(z_world-perp-z_harm bridge infeasibility), and this run's own finding (sourcing-mode
dependence) is a first occurrence, not a recurring pattern circling the same claim.
**Re-derive brake:** not applicable (`evidence_direction=supports`, not `substrate_ceiling`).

**Recommended `epistemic_category`:** `standard`. **Recommended `evidence_direction`:**
`supports` (matches manifest, correct under the run's own OR-gate rule) -- **with a mandatory
caveat note** (see below) so a future reader does not over-read "supports" as validating the
production configuration.

**Recommended `evidence_quality_note` (verbatim, for governance to apply):**

> V3-EXQ-917 resolves the `complex (probe-gated)` open question from
> `mech303_contextual_safety_threshold_reachability.md` (2026-08-11): the SD-011 affective-harm
> encoder's threshold reachability/discrimination tension is NOT intrinsic -- it dissociates
> cleanly by sourcing mode. Under the production default (damage_sourced, SD-022 body-damage),
> the safe-vs-unsafe AUC never exceeds 0.52 (chance) across 18 thresholds tested (C1 FAIL).
> Under the legacy pre-SD-022 sourcing (proximity_ema_sourced, a slow EMA of hazard/resource
> spatial proximity), AUC reaches 0.84-0.97 across a wide threshold band 0.4-0.8 (C2 PASS).
> Overall evidence_direction=supports is correct under the run's own OR-gate combination rule
> (found a workable configuration), but this should NOT be read as validating the PRODUCTION
> default -- every driver that has exercised MECH-303's live threshold gate (764, 520, 916) uses
> damage_sourced, and none of them can calibrate a working threshold under it. Biological
> grounding: this matches the classical dissociation between reactive/interoceptive nociception
> (damage-triggered, Melzack & Casey 1968 sensory-discriminative component) and anticipatory
> contextual threat perception (proximity/context-driven, the affective-motivational component
> SD-011's own dual-stream design is grounded in) -- MECH-303 models the latter (contextual
> safety learning), so gating it on the former (accumulated body damage) is a mechanistically
> mismatched sourcing choice, not evidence the encoder itself cannot discriminate.

**Recommended `recommended_substrate_queue_entry`** (action=`create` -- no existing
substrate_queue entry covers this; confirmed via grep, `--implement-substrate` recommended and
confirmed by user at Step 8):

- `sd_id_suggested`: `SD-MECH303-THRESHOLD-SOURCING`
- `title`: Recalibrate MECH-303 `contextual_safety_harm_threshold` to use a proximity-anticipatory
  signal instead of SD-022 damage-sourced `z_harm_a`
- `implementation_hint`: V3-EXQ-917 found the production default (damage_sourced) never clears
  chance-level (AUC<=0.52) discrimination at any of 18 tested thresholds, while proximity_ema_sourced
  reaches AUC 0.84-0.97 with reachability 0.23-0.98 across thresholds 0.4-0.8. Either (a) source
  MECH-303's specific gate from a dedicated proximity-EMA-style anticipatory signal decoupled
  from SD-022's damage-sourcing default (so other consumers needing body-damage tracking are
  unaffected), or (b) make harm_obs_a sourcing driver/consumer-configurable and set
  `contextual_safety_harm_threshold` to a value in the reachable+discriminating band (e.g. 0.55:
  reachability 0.77/AUC 0.9625, or 0.6: reachability 0.85/AUC 0.969). Needs a design decision on
  whether other production drivers (764, 520, 916/916a, and any future `use_contextual_safety_terrain`
  driver) should switch sourcing, since damage_sourced is also relied on for SD-022's own
  body-damage-tracking purpose -- may need a SECOND harm signal rather than re-sourcing the
  existing one.
- `unblocks_claims`: [MECH-303]
- `priority_suggested`: 2 (medium -- MECH-303 is `provisional`, not currently blocked on this;
  promote-to-active is already gated on a different, unrelated behavioural falsifier per
  claims.yaml; this is a downstream default-config usability fix)
- `severity`: `degrading` (MECH-303's own claim/validation via V3-EXQ-760 is unaffected --
  driver's own `claim_ids` scoping deliberately excludes MECH-303; this affects driver-level
  usability of the live threshold gate that other drivers may silently misuse)
- `substrate_paths`: `ree_core/utils/config.py` (contextual_safety_harm_threshold default),
  `ree_core/environment/causal_grid_world.py` (SD-022 damage-sourcing of harm_obs_a, ~3816-3838),
  `ree_core/agent.py` (sense() live gate, ~5128-5145)
- `failure_record_entry`: run_id=V3-EXQ-917's run_id, metric="damage_sourced AUC capped at 0.52
  across all 18 swept thresholds", target="a threshold/sourcing convention where the live gate
  is both reachable and discriminating (AUC notably >0.5) under PRODUCTION sourcing", resolved=open

**Routing:** `implement-substrate` (confirmed by user).

---

## Target 4 -- V3-EXQ-920 (Uncensored survival-to-death, TRUE single-life design)

**Facts.** `run_id=v3_exq_920_uncensored_survival_single_life_fishtank_20260811T210906Z_v3`,
`experiment_purpose=diagnostic`, `outcome=FAIL`, `claim_ids=[]`, `evidence_direction=non_contributory`.
Self-route label `single_life_uncensored_survival_still_censoring_dominated`. Successor to
V3-EXQ-912's segment-count-scaling workaround, now implementing true single-continuous-life
design literally (`EVAL_EPISODES=1`, `max_episode_steps=20000`, no body-respawn anywhere in the
observed window) since `CausalGridWorldV2` gained a driver-configurable `max_episode_steps`
kwarg (`SD-FISHTANK-MAX-EPISODE-STEPS`, ree-v3 9d3d148ff8).

**Pre-registered design (driver docstring, "STEP-BUDGET CALIBRATION"):** SEEDS=8,
`MIN_UNCENSORED_DEATHS_TOTAL=4`, calibrated from V3-EXQ-912's naive per-500-step hazard rate
(~6.7%) to expect ~94% chance of an uncensored death per seed over 20000 steps, i.e. ~7.5
expected deaths across 8 seeds -- comfortably clearing the pre-registered floor of 4. The queue
entry (`ree-v3` git history, commit `fc0fb4ce5c`) correctly carried `"seeds": 8`.

**What actually ran.** The manifest's `seeds` field is `[0]` -- **only 1 of the 8 pre-registered
seeds executed.** `n_uncensored_deaths_total=1` (< floor of 4) -> load-bearing criterion
`sufficient_uncensored_deaths` FAILS -> overall FAIL. But `pct_right_censored_pooled=0.0` --
**literally zero censoring occurred.** The self-route label's "still_censoring_dominated" is a
hardcoded else-branch string in the driver
(`v3_exq_920_uncensored_survival_single_life_fishtank.py:557-558`,
`"...distribution_obtained" if sufficient_uncensored_deaths else "...still_censoring_dominated"`)
-- it fires whenever the death-count floor isn't met, **regardless of whether censoring is
actually the cause.** Here it manifestly is not: the one seed that ran produced a genuine,
uncensored `health_depleted` death at 1475 steps (well within the 261-487+ range V3-EXQ-912
observed, consistent with the pre-registered calibration), and the run simply never reached the
7 additional seeds needed to clear the floor.

**Root cause, traced to `experiment_runner.py`.** `run_experiment()` builds the subprocess
command line as `args = [sys.executable, "-u", str(script)] + list(raw_args)` where
`raw_args = item.get("args", [])` -- **only** the queue item's explicit `"args"` field ever
reaches the driver's CLI. The queue item's `"seeds": 8` field is consumed **only** by
`seed_count = _run_axis_count(item.get("seeds", 1), "seeds")`, which feeds `total_runs` for the
**progress-bar denominator** -- it is never translated into `--seeds` arguments. This queue
entry carried no `"args"` field. The driver's own argparse default,
`parser.add_argument("--seeds", type=int, nargs="+", default=[0])`, therefore silently governed
the actual run -- a single seed, not the pre-registered eight. (Contrast V3-EXQ-917's driver,
which happens to work correctly because its own default, `type=int, default=N_SEEDS` with
`N_SEEDS=10` matching its intended count, coincidentally matches the queue's declared `"seeds":
10` -- the two mechanisms are entirely independent and only appear consistent by luck.)

**Claim-layer map.** claim_ids=[] -- no claim weighted; n/a.

**Biological reference.** n/a -- this is an execution/infrastructure defect, not a finding
about REE's cognitive substrate. The pre-registered survival-time question itself (single-life
mortality/hazard-rate characterization) has an obvious biological analog (ecological survival
curves), but that question was never actually tested at adequate power by this run.

**Four-layer diagnosis.**

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim_ids=[] |
| Biological reference | n/a | infrastructure defect, not a mechanism question |
| Prerequisites | present | harm_pathway_trained (4038 optimizer steps), all_seeds_completed (1 of 1 requested) |
| Implementation completeness | broken (execution wiring) | driver `--seeds` default doesn't match pre-registered design; queue `"seeds"` field never reaches CLI args |
| Environment adequacy | adequate | max_episode_steps design correctly implements true single-life (design itself is sound) |
| Measurement adequacy | adequate | pct_right_censored_pooled/n_uncensored_deaths_total are exactly correct for the 1 seed that ran |
| Integration adequacy | n/a | |
| Scale / capacity | insufficient | 1 of 8 pre-registered seeds executed |

**Failure-location summary (GOV-FAILLOC-1).** None of MECHANISM FAILED / MEASURES FAILED /
ENVIRONMENT FAILED / REE FAILED apply -- this is an **infrastructure/execution defect**
(queue-to-CLI args wiring gap), entirely outside REE's cognitive substrate. Net classification:
not chargeable to REE, mechanism, measurement, or environment.

**Self-route-is-a-hypothesis pattern (recurring).** This is another instance of the canonical
V3-EXQ-642 trap: the manifest's own `interpretation.label` is a hardcoded string keyed on
whether ONE criterion passed, not a genuine diagnosis of *why* it didn't. Left unadjudicated,
"still_censoring_dominated" would read as a real scientific finding about within-life mortality
dynamics -- it is not.

**Recommended `epistemic_category`:** `standard`. **Recommended `evidence_direction`:**
`non_contributory` (unchanged -- correct in the "tells us nothing about the science" sense, for
the corrected reason).

**Recommended `evidence_quality_note` (verbatim, for governance to apply):**

> Self-route label `single_life_uncensored_survival_still_censoring_dominated` is INCORRECT and
> should not be read as a measurement finding -- `pct_right_censored_pooled=0.0` (literally zero
> censoring; the max_episode_steps-enabled design worked exactly as intended). The true cause of
> the FAIL is that only 1 of the pre-registered 8 seeds actually executed: the queue entry
> correctly declared `"seeds": 8`, but `experiment_runner.py`'s `run_experiment()` builds
> subprocess CLI args ONLY from the queue item's `"args"` field
> (`raw_args = item.get("args", [])`) -- the declarative `"seeds"` count is used solely for the
> progress-bar denominator (`_run_axis_count`), never translated into `--seeds` CLI arguments.
> This queue entry carried no `"args"` field, so the driver's own `--seeds` default (`[0]`, a
> single seed) silently governed the actual run. The seed that DID run (seed 0) behaved exactly
> as the pre-registered STEP-BUDGET CALIBRATION predicted (1 uncensored death at 1475 steps,
> well within the expected 261-487+ range extrapolated from V3-EXQ-912's naive hazard-rate
> calibration) -- this is an execution/wiring gap, not a scientific result about within-life
> survival or censoring.

**Recommended `recommended_substrate_queue_entry`:** `action: none` -- this is a driver/queue
wiring bug, not a substrate gap.

**Routing:** `queue-experiment` (confirmed by user) -- a same-question re-queue (new letter,
V3-EXQ-920a) whose only change is to correctly launch with the pre-registered 8 seeds, e.g. by
adding an explicit `"args": ["--seeds", "0", "1", "2", "3", "4", "5", "6", "7"]` to the queue
entry (or fixing the driver's own default to `default=list(range(8))`, matching the
already-correct pattern in V3-EXQ-917's driver). User declined a broader systemic audit of
other drivers for the same `--seeds` default-vs-queue-count mismatch pattern at this time --
noted here as a candidate follow-on if it resurfaces.

---

## Cluster read

**Not one structural failure.** Three independent findings:

1. **916/916a (recording debt, resolved).** A lineage-wide telemetry wiring gap
   (`use_proxy_fields=False` + wrong-dict read silently zeroing `benefit_exposure`) was found
   and fixed in 916a; already fully documented in `substrate_queue.json`. No action needed.
2. **917 (sourcing-mode dependent threshold, genuine scientific finding).** Resolves an
   open `complex (probe-gated)` question: SD-011's threshold reachability/discrimination
   tension is not intrinsic to the encoder -- it is specific to SD-022's damage-sourcing
   convention, which every production driver currently uses for MECH-303's live gate.
   Biologically well-grounded (Melzack/Craig/Rainville dual-pathway dissociation, already
   in SD-011's own evidence trail). Routes to `/implement-substrate`.
3. **920 (execution/wiring gap, self-route mislabeled).** A driver/runner CLI-args wiring
   defect silently ran 1 of 8 pre-registered seeds, producing an underpowered FAIL that the
   driver's own hardcoded label misattributes to persistent censoring. Routes to
   `/queue-experiment` for a corrected re-run.

None of these three share a claim_id, a common substrate defect, or a common failure signature
with each other -- they are reported together only because they were adjudicated in the same
session.

## Learning extracted

- Recording gap discovered lineage-wide (`use_proxy_fields=False` + `obs_dict`-vs-`info` read
  bug) silently zeroed `benefit_exposure` across 664/906/909/911/912/913/916; MECH-302/303/304
  telemetry channels are real and correctly wired once the relevant flags are enabled.
- SD-011's affective-harm-encoder discrimination tension is sourcing-mode dependent, not
  intrinsic -- production's damage-sourcing convention (SD-022) is mechanistically mismatched
  for MECH-303's anticipatory contextual-safety purpose; this dissociation is independently
  predicted by SD-011's own cited biology (Melzack/Craig/Rainville).
- `experiment_queue.json`'s `"seeds": N` field is progress-tracking metadata ONLY -- it is
  never translated into CLI `--seeds` arguments by `experiment_runner.py`. A driver's own
  argparse default must independently match its documented seed count, or the queue entry must
  explicitly carry an `"args"` field with the seed list -- otherwise a pre-registered N-seed
  design can silently execute as a 1-seed run with no error, warning, or visible discrepancy
  anywhere except a mismatch between the queue's declarative metadata and the manifest's actual
  `seeds` field.
- The self-routed `interpretation.label` can be actively misleading when a driver's
  PASS/FAIL branch hardcodes a specific failure-mode string regardless of the true cause
  (recurring pattern, canonical V3-EXQ-642) -- confirmed again here (920) independent of
  V3-EXQ-642's own domain.

## Step 9b (hypothesis-space registry)

Not run -- user declined at the Step 8 gate (916/916a question, option "Just confirm and
close"). V3-EXQ-917's C1-vs-C2 dissociation would have been a clean Mode B same-cycle
registration (two hypotheses, one resolved-eliminated, one resolved-confirmed, both on the
run's own completion date), but was not registered per the user's choice.
