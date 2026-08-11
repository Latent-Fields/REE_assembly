# Failure Autopsy: V3-EXQ-912 + V3-EXQ-913 (Fishtank ecology diagnostics, cluster scope)

**Generated:** 2026-08-11T06:01:31Z
**Status:** confirmed
**Scope:** cluster (same substrate family -- 906b-lineage Fishtank driver -- two structurally
different diagnostic questions, presented together for efficiency; not a shared-failure-shape
cluster in the Step 6 sense)
**Session:** diagnose-errors-8cdcaf

Both targets are `experiment_purpose: "diagnostic"`, `claim_ids: []` ("diagnostic showcase;
does not weight governance" -- their own docstrings). Per this skill's blanket rule, every
diagnostic PASS or FAIL needs a confirmed autopsy before governance can act on it, regardless
of whether the indexer's `adjudication` flag caught anything. Neither run was flagged by the
indexer; both needed this autopsy anyway.

---

## Target 1: V3-EXQ-912 -- Uncensored Survival-to-Death Fishtank Successor

- **run_id:** `v3_exq_912_uncensored_survival_fishtank_20260810T190239Z_v3`
- **queue_id:** V3-EXQ-912
- **Outcome:** FAIL (self-route: `uncensored_survival_still_censoring_dominated`)
- **claim_ids:** [] (diagnostic characterization, not scored against any claim)
- **Dry-run check:** clean (`check_dry_run_citations.py` -- 0 dry cited, 3 clean)

### Facts

Purpose: replace the 906-lineage's single-run, mostly-censored n=8 death-rate point estimates
(906a 0%, 906b 75%, 906c 87.5%, 911 100% right-censored) with a proper survival-analysis
characterization at n=60 segments/seed x 2 seeds. Pre-registered PASS threshold:
`MIN_UNCENSORED_DEATHS_TOTAL=10` genuine (uncensored) `health_depleted` events across both
seeds combined.

**Observed:** the manifest's `seeds` field is `[0]` -- **only 1 of the queued 2 seeds ran.**
`n_segments_total=60` (not the designed 120), `n_uncensored_deaths_total=4` (6.7% death rate),
`pct_right_censored_pooled=0.933`. FAIL on the load-bearing `sufficient_uncensored_deaths`
criterion (4 < 10).

**Root cause of the seed-count mismatch (verified against source, not inferred):**

1. `ree-v3/experiment_queue.json`'s V3-EXQ-912 entry declares `"seeds": 2` and carries no
   `"args"` field.
2. `ree-v3/experiment_runner.py:3779` builds the subprocess command as
   `[sys.executable, "-u", script] + item.get("args", [])` -- the queue's `"seeds"` integer is
   **never translated into a `--seeds` CLI argument.** It is consumed ONLY by `_run_axis_count`
   (`experiment_runner.py:3639,3668,3802`) for progress-bar/ETA denominators
   (`total_runs = seed_count * condition_count`), never to construct `args`.
3. `ree-v3/validate_queue.py:922` validates only the *shape* of the `"seeds"` field (int or
   list); it never cross-checks it against an `"args"` `--seeds` list, nor against the target
   script's own argparse default.
4. `v3_exq_912_uncensored_survival_fishtank.py:621`:
   `parser.add_argument("--seeds", type=int, nargs="+", default=[0])` -- a single-seed default,
   inherited from convention (906b's own queue entry was genuinely `"seeds": 1`, so its
   matching `default=[0]` was correct) but **never updated** to match this run's own docstring
   ("EVAL_EPISODES=60 ... seeds=[0,1]") or its queue entry's `"seeds": 2`.
5. **Sibling driver V3-EXQ-913 does NOT have this defect**: its author correctly set
   `SEEDS_DEFAULT = [0, 1]` (`v3_exq_913_developmental_ecology_fishtank.py:283`) matching that
   run's own `"seeds": 2` queue declaration, and its manifest confirms `seeds: [0, 1]` actually
   ran. This is an authoring inconsistency between two sibling drivers, not a fundamental
   runner limitation that always bites -- but nothing in the pipeline enforces the consistency,
   so it is luck, not design, whether a given driver's default happens to match its own queue
   entry.

**Is the underlying data still informative despite running at half power?** Yes, per the
driver's own docstring ("Even on a FAIL/still-censoring-dominated outcome, the pooled
pct_right_censored and n_uncensored_deaths_total are the load-bearing scientific readouts --
this is a characterization run, not a hypothesis test"). At n=60 (one seed), the empirical
death rate (6.7%) is a substantially better-powered point estimate than 906b's own 25% (2/8)
or 906c's 12.5% (1/8) -- those priors carry huge sampling uncertainty at n=8. The lower rate
observed here may reflect that 906b's 25% was itself a noisy small-n estimate, not that the
906b ecology's death rate has "drifted."

**Death-timing pattern (n=4, underpowered but worth naming precisely):** deaths occurred at
segment indices 17, 19, 53, 56 (of 60) -- a cluster in the first third of the life, a
33-segment death-free stretch, then a cluster near the end. This is *consistent with* (not
confirmed by, at n=4) a bathtub-shaped mortality hazard (elevated early- and late-life risk,
low mid-life risk) -- a well-precedented pattern across many species in real survival
biology, and a concrete, falsifiable framing for the corrected re-run rather than "noise."

### Claim-layer mapping

N/A -- `claim_ids: []`, diagnostic showcase.

### Biological reference

Survival analysis with explicit right-censoring accounting (Kaplan-Meier-style partitioning
of uncensored vs. censored observations) is a standard, well-grounded technique borrowed
directly from real-world mortality/epidemiological characterization -- this is methodology
correctly applied to an already-implemented ecology, not a formal-definition import risking a
wrong mechanism (the SD-003 failure mode this skill warns about does not apply here: nothing
about REE's *mechanism* is being asserted, only a measurement technique). The suggestive
early/late death clustering maps onto the bathtub hazard curve documented across mammalian and
non-mammalian species alike (elevated juvenile mortality + senescence-driven late mortality,
low hazard in between) -- a concrete existence proof for the specific pattern observed, worth
naming even though n=4 cannot confirm it.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | no claims tagged |
| Biological reference | clear | survival-analysis methodology correctly applied; bathtub-hazard framing available for the death-timing pattern |
| Prerequisites | present | harm-pathway trained (3968 steps), z_goal activated |
| Implementation completeness | complete for survival-stat computation; **execution incomplete** | `_survival_stats`/`_lifetime_affective_occupancy`/thinning logic all correctly computed from full unthinned data (verified by code read); but the run executed at 1 of 2 intended seeds |
| Environment adequacy | adequate | deliberate, well-justified reuse of 906b's ecology tuning (not 911's, which produced zero deaths) |
| Measurement adequacy | adequate | censoring accounting, occupancy stats, cumulative-step markers all correctly implemented |
| Integration adequacy | adequate | n/a beyond the above |
| Scale/capacity | **inadequate relative to the run's own design** | n=60 segments realized vs. 120 designed; MIN_UNCENSORED_DEATHS_TOTAL=10 threshold was calibrated against the full 120-segment design |

**Failure-location (GOV-FAILLOC-1):** claim-free diagnostic; no organism-level "REE failed"
reading is warranted or made here. The FAIL is an **execution/apparatus** defect (seed-count
under-run), not a mechanism, measurement, or environment inadequacy in REE's own substrate --
none of the four GOV-FAILLOC-1 buckets apply cleanly since the criterion that failed
(`sufficient_uncensored_deaths`) is a sample-size gate, not a claim about REE's behaviour.

### Repair pathway

`complicated (buildable)` -- the fix is a named build with no open question: (a) update
`v3_exq_912_uncensored_survival_fishtank.py`'s `--seeds` default to `[0, 1]` (matching 913's
correct convention), or pass explicit `"args": ["--seeds", "0", "1"]` in the queue entry; (b)
add a general validate_queue.py / runner check that a queue entry's `"seeds": N` (N > 1) with
no explicit `--seeds` args and a target script whose own argparse default has fewer entries
than N is flagged -- this defect class is not specific to V3-EXQ-912 and nothing currently
catches it corpus-wide.

**Routing: `/implement-substrate` (amend, severity=degrading) + `/queue-experiment` corrected
re-run.** User-confirmed at the Step 8 gate.

### Draft `evidence_quality_note` (not written -- for governance)

> V3-EXQ-912 (`v3_exq_912_uncensored_survival_fishtank_20260810T190239Z_v3`, FAIL,
> claim_ids=[]) ran at 1 of the queued 2 seeds -- the driver's own `--seeds` argparse default
> ([0]) was never updated to match its own docstring's 2-seed design, and neither the queue
> entry nor the runner enforced the declared seed count. At n=60 (not the designed n=120),
> 4/60 segments (6.7%) ended `health_depleted` -- below the pre-registered
> `MIN_UNCENSORED_DEATHS_TOTAL=10` threshold, hence FAIL, but a real and better-powered point
> estimate than 906b's own n=8-based 25%. Non-contributory to governance (claim_ids=[]);
> characterization data retained, not treated as a claim-layer weakens. Corrected re-run routed
> as V3-EXQ-912a.

---

## Target 2: V3-EXQ-913 -- Developmental-Ecology Fishtank Successor

- **run_id:** `v3_exq_913_developmental_ecology_fishtank_20260810T213204Z_v3`
- **queue_id:** V3-EXQ-913
- **Outcome:** PASS (self-route: `developmental_ecology_mechanisms_engaged`)
- **claim_ids:** [] (diagnostic showcase, does not weight governance)
- **Dry-run check:** clean

### Facts

Combines three findings from the Fishtank organism-lifespan/ecology reviews as one successor:
layout continuity (`env.reset_to()` instead of `env.reset()` across segment boundaries),
probabilistic microhabitat-zone habitat cues (region-weighted resource/hazard placement, NOT
a deterministic landmark), and a genuine sleep-vs-no-sleep two-arm ablation (K=10 multi-fire
vs. `use_sleep_loop=False`). 2 arms x 2 seeds x 24 segments. All 5 preconditions met
(`harm_pathway_trained`, `layout_continuity_confirmed`, `zone_map_active`,
`sleep_ablation_engaged`, plus core-channel non-degeneracy); all 5 load-bearing criteria pass.

**Is the PASS vacuous (engagement-only) or does it carry a substantive finding?** Substantive,
verified by reading past the boolean preconditions into the raw comparison data:

1. **Sleep-vs-no-sleep matched-boundary trajectory organization**: at every sleep firing with
   a *valid* matched no-sleep comparison (4 of 5 obtained; see caveat below), sleep firing is
   followed by markedly *lower* turning-angle entropy and tortuosity than the matched no-sleep
   control at the same segment index (seed0: entropy delta -0.378/-0.430/-0.442, tortuosity
   delta -0.881/-8.0/-4.025, all three consistent; seed1 seg9: entropy delta +0.469, in the
   opposite direction). **Caveat**: of the 5 "matched comparisons obtained" the manifest
   reports, 1 (seed1 seg19) is fully degenerate -- the matched no-sleep segment has
   `path_length=0`, `net_displacement=0`, all derived stats null -- so only 4 comparisons are
   actually interpretable, and 1 of those 4 (seed1 seg9) itself rests on a near-static
   (`turning_angle_entropy_bits~0`, `path_length=3`) matched control. The "sleep organizes
   trajectories" reading is directionally supported (3/4 usable comparisons agree, robustly,
   for seed0) but thinner than the headline "5 matched comparisons" count suggests.
2. **Zone-conditioned field statistics**: `mean_resource_field_by_zone` varies substantially
   across the 4 microhabitat zones in every (seed, arm) cell (e.g. seed0_with_sleep: zone 2
   mean=0.76 vs zone 0 mean=0.17) -- the zone-weighted placement manipulation left a real,
   perceptible trace in what REE actually senses via the existing resource_field/hazard_field
   channels, not merely a boolean "zone map object exists" check.
3. **Within-life development** (the run's flagship "is there real learning, now unconfounded
   by per-segment layout re-randomization" readout): `r(segment, benefit_rate)` is negative in
   3 of 4 (seed, arm) cells (-0.135 to -0.649) -- read naively as "foraging success declines
   over the life." **This reading is confounded.** `total_resource_exhausted_segments=55` of
   96 segment-runs (24 segments x 2 seeds x 2 arms) -- a majority of cells experienced full
   resource depletion, and `resource_respawn_on_consume=False` combined with layout continuity
   means each life's resource supply is fixed at `DEV_NUM_RESOURCES=24` for its whole
   24-segment life. The ONE cell with **zero** exhausted segments (seed1_no_sleep) is also the
   only cell with an approximately flat trend (r=+0.016) -- exactly what a genuinely
   confound-free measurement should look like if the "decline" in the other three cells is
   patch depletion rather than a competence change. This is a new synthesis this autopsy
   contributes (the driver's own "for a future reader" note flags high
   `total_resource_exhausted_segments` as a signal to raise `DEV_NUM_RESOURCES` in a successor,
   but does not connect it to the within-life-development readout as a likely confound on
   THIS run's own flagship finding).

### Claim-layer mapping

N/A -- `claim_ids: []`, diagnostic showcase.

### Biological reference

The declining-benefit-rate-under-resource-depletion pattern parallels **patch depletion** in
optimal foraging theory (Charnov's marginal value theorem: foraging returns from a persistent,
non-renewing patch decline as the patch is depleted, independent of any change in the
forager's own competence). This is the biologically correct default reading of the
within-life-development statistic here, and it directly cautions against the naive
"declining competence" misreading -- a real organism foraging a fixed food supply would show
exactly this shape. Sleep-dependent motor-sequence reorganization (reduced post-sleep movement
entropy/tortuosity) has a real biological reference too: sleep-dependent consolidation
reducing exploratory noise in subsequent behaviour is documented in mammalian motor-sequence
learning, consistent in direction with what this run's matched comparisons show.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | no claims tagged |
| Biological reference | clear | patch-depletion / optimal-foraging-theory framing for the confounded readout; sleep-consolidation framing for the trajectory-organization finding |
| Prerequisites | present | harm-pathway trained (25045 steps), MECH-357 (SD-058 instrumental-avoidance) confirmed active and inherited unchanged |
| Implementation completeness | complete | `reset_to()` layout continuity, microhabitat zone weighting, sleep-loop ablation all confirmed via direct source reads at design time (module docstring) and via engagement checks at run time |
| Environment adequacy | **partially confounded for one sub-finding** | `DEV_NUM_RESOURCES=24`, no respawn, was insufficient headroom for a fully-foraging 24-segment life in 3 of 4 cells -- adequate for layout-continuity/zone-cue purposes, inadequate for a clean within-life-development readout |
| Measurement adequacy | adequate, with one thinness caveat | sleep-ablation matched-comparison count (5) includes 1 fully degenerate and 1 near-degenerate pairing; usable n is closer to 2-3 robust comparisons |
| Integration adequacy | adequate | all three manipulations (layout, zone, sleep) combined without interaction defects visible in the data |
| Scale/capacity | adequate | 2 seeds x 2 arms x 24 segments is proportionate to the design's own stated goals |

**Failure-location (GOV-FAILLOC-1):** n/a in the literal sense (this is a PASS, not a FAIL) --
but the skill's caution against organism-level misreadings applies to the PASS's own headline
finding. The within-life "decline" must NOT be read as "REE's foraging competence declined
over its life" -- Implementation/Environment/Measurement are each adequate for the layout- and
zone-continuity findings, but Environment is the identified confound specifically for the
within-life-development sub-finding (resource-patch depletion, not a REE-side effect).

### Repair pathway

The PASS stands -- mechanism engagement is genuine and non-vacuous. The within-life-development
confound is `complicated (buildable)`: raise `DEV_NUM_RESOURCES` well above 24 (still
`resource_respawn_on_consume=False`, per the module's own zone-dilution reasoning) in a
successor if a clean within-life-development readout is wanted. Not urgent; no re-run required
by this autopsy.

**Routing: PASS stands; confound flagged in the evidence note; no re-run queued.**
User-confirmed at the Step 8 gate.

### Draft `evidence_quality_note` (not written -- for governance)

> V3-EXQ-913 (`v3_exq_913_developmental_ecology_fishtank_20260810T213204Z_v3`, PASS,
> claim_ids=[]) -- genuine, non-vacuous engagement of all three combined manipulations (layout
> continuity, microhabitat zone-weighted cues, sleep-vs-no-sleep ablation), with substantive
> zone-conditioned field-statistic and sleep-organizes-trajectories findings (the latter on a
> thinner-than-headline n; 1 of 5 "matched comparisons" is fully degenerate). The flagship
> within-life-development readout (declining benefit_rate) is confounded by resource-patch
> depletion (55/96 segments exhausted; the sole zero-exhaustion cell shows a flat trend, r=+0.016
> vs -0.13 to -0.65 in the exhausted cells) and should NOT be cited as evidence of declining
> competence. Non-contributory to governance (claim_ids=[]); descriptive characterization only.

---

## Learning extracted (both targets)

- New dependency discovered: the queue's `"seeds": N` field is documentation/estimation-only
  and is never enforced into actual `--seeds` execution -- a driver's own argparse default is
  the sole source of truth for how many seeds actually run, and nothing in the pipeline
  (runner, `validate_queue.py`) cross-checks the two. This is a genuine, previously-uncaught
  execution gap affecting any multi-seed queue entry whose driver's default doesn't happen to
  match.
- Measurement gap (913): the sleep-ablation "matched comparisons obtained" count does not
  distinguish valid from degenerate/null pairings -- a future driver in this family should
  report a `matched_comparisons_valid` count alongside the raw total.
- Biology divergence, load-bearing: patch depletion (real ecological phenomenon) is a more
  parsimonious explanation for 913's within-life "decline" than a REE-side competence change --
  caught by checking the resource-exhaustion cross-tabulation the run itself recorded but did
  not connect to its own flagship readout.
- Genuine positive-negative result (912): the corrected point estimate at n=60 (6.7% death
  rate) is itself informative, more reliable than the small-n 906b/906c priors it is compared
  against, independent of the seed-count defect.

## Re-derive brake / granularity-debt checks

N/A for both targets -- `claim_ids: []`, no claim to brake-check (per each driver's own
Step 2.5b note).

## Hypothesis-space ledger (Step 9b)

N/A -- both targets are claim-free diagnostics (`claim_ids: []`); the frozen pre-registration
ledger is scoped to claims (`questions[].claims`), so there is no question to pre-register or
resolve against for either target.
