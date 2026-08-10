# Failure Autopsy: V3-EXQ-909 (sleep-refinement DV, multi-firing/multi-seed)

**Generated:** 2026-08-10T14:21:33Z
**Scope:** single
**Status:** confirmed
**Target:** V3-EXQ-909 (PASS, `experiment_purpose: diagnostic`, `claim_ids: []`)

Written as part of `/governance`'s Step 1.5 inline autopsy pass. Primary source:
`organism_lifespan_development_review_906_lineage_2026-08-10.md` Section 4, verified directly
against the manifest.

**Dry-run gate:** clean (`check_dry_run_citations.py`, 0 hits).
**Recording provenance:** `recording_schema: rec/v1`, `substrate_hash`, `machine`/`machine_class`,
`elapsed_seconds` (22254.8s — the longest of the batch), `seeds: [0,1,2]` all present.

## Facts

Pre-registered discrimination rule: "a firing is 'non-null' if `sws_slot_diversity > 0.01` OR
`replay_diversity_index > 0.01`... label='sleep_dv_nonnull_detected' iff frac_nonnull >= 0.1."
All 6 load-bearing preconditions met (waking diversity present, SWS/REM write mechanisms
engaged, replay-draw structurally reachable — confirmed this run's config fix actually took
effect vs 906b's own permanently-zero-draws baseline, sufficient firing sample n=45 across 3
seeds). PASS is real on its own narrow terms.

**But the magnitudes are near-degenerate, not diverse:**
- `sws_slot_diversity`: mean 2.3e-04 (cosine similarity between memory slots ~0.9998-0.99999) —
  clears the `>0.01` bar only via its OR-partner.
- `replay_diversity_index`: **exactly 0.02 on every single one of 45 firings, all 3 seeds, zero
  variance.** One unique region replayed out of 50 draws, every time.
- No pre/post-sleep behavioural comparison exists anywhere in the collected data. The only
  before/after pair is `post_sleep_z_goal_before`/`_after` — an internal numeric-retention check
  (bit-identical in sampled records), not a behavioural measure. Route efficiency, hazard
  exposure, resource acquisition, action entropy of the post-sleep segment are not logged before
  OR after in any comparable form.

## Claim-layer map

`claim_ids: []` — no claims.yaml entry.

## Biological reference

Sleep-dependent memory consolidation (SWS/REM replay) is a well-grounded biological reference
class. The finding here is instrumentation, not translation fidelity — the mechanism computes
the right things (SWS writes, REM rollouts, replay draws) but the manifest never records the
one comparison (pre vs post waking behaviour) that would let a human or a future analysis judge
whether consolidation produced any behavioural effect.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim-free |
| Biological reference | clear | SWS/REM consolidation is a real, well-grounded target |
| Prerequisites | present | replay-draw structural fix confirmed to have taken effect this run |
| Implementation | partial | mechanism runs and writes structurally, but replay diversity is exactly 0.02 with zero variance across 45 firings -- possibly near-collapsed in which region it draws, not diagnosed to code level here |
| Environment | adequate | n/a to this finding |
| Measurement | under_instrumented | no pre/post-sleep behavioural window recorded anywhere -- a genuine RECORDING gap, not merely a blind metric |
| Integration | isolated | the pass bar (OR of two channels at a shallow 0.01 floor) does not establish "diverse", just "not-permanently-zero" |
| Scale | unknown | n=45 firings/3 seeds is a real sample for the structural non-degeneracy check, but says nothing about behavioural effect since that comparison was never recorded |

**Failure-location (GOV-FAILLOC-1):** MEASURES (shallow OR-gated bar overstates what "non-null"
established) + a genuine RECORDING gap (the readout needed existed conceptually but was never
written to the manifest, distinct from a measurement gap where the metric itself is blind).
Net: **MIXED, leaning MEASURES/recording-debt — not a REE finding.**

## Learning extracted

1. "Non-null" per this pre-registered rule is a structural non-degeneracy check (replay diversity
   channels are not stuck at the -1.0 zero-draws sentinel), not a behavioural diversity finding —
   the plain-English label overclaims relative to its narrow, technically-correct definition.
2. `replay_diversity_index` exactly 0.02 with zero variance across 45 firings is itself a
   strongly degenerate result worth a future mechanism-level look (not diagnosed here — would
   need reading the replay-draw sampling code, a separate task).
3. The load-bearing gap for the user's original sleep question ("does behaviour improve after
   sleep") cannot be answered even from already-collected data — this is recording-debt, not
   measurement-debt: the fix is recording a matched post-firing window in a re-run, not
   redesigning the metric.

## Repair pathway

`complicated (buildable)` — recording gap, not a measurement redesign. Per the
Experimental Recording Standard (`experimental_recording_standard_2026-07-12.md` §3c
family-keyed payload): a 909a re-run whose only change is to log a matched post-firing waking
window (route efficiency, hazard exposure, resource acquisition, action entropy) keyed to the
same `(seed, boundary_index)` as the existing `sleep_firing_records`, calling
`stamp_recording_core(...)` plus the new readout. A blind re-run would reproduce the same blind
spot at the same compute cost — the fix is specifically to RECORD, not to re-measure differently.

## `recommended_substrate_queue_entry`

`action: none` — this is an experiment-instrumentation gap (routes to `/queue-experiment`), not
a substrate/mechanism gap.

## Recommended `evidence_quality_note`

None — `claim_ids: []`, nothing to weight. `evidence_direction` stays `non_contributory`
(unchanged from the manifest).

## Growth-restriction / Step 9b

Not applicable — no fan-out, no pre-registered hypothesis adjudicated. Skip cleanly.

## Re-derive brake / granularity-debt

`claim_ids: []` — neither applies.

## Routing (confirmed at interactive gate)

**queue-experiment** — recording-gap re-run (909a), same question, instrumentation-only change
citing the Experimental Recording Standard. Not spawned from this artifact (per the skill's
Step 8 rule against self-chipping a routing this session's own gate just confirmed) — governance
records the recommendation; a future `/queue-experiment` session or governance chip executes it.
