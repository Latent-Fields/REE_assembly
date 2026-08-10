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

**Failure-location (GOV-FAILLOC-1):** MEASURES — sharpened after reading
`sleep_transition_investigation_906_lineage_2026-08-10.md` Section 4 (read after this artifact's
initial draft): not merely a shallow OR-gated bar or a missing readout, but **a different DV
entirely** — 909's pre-registered rule targets sleep-mechanism internal diversity
(`sws_slot_diversity`, `replay_diversity_index`), which has zero conceptual overlap with
behavioural trajectory reorganisation. Net: **MEASURES — the measure was never aimed at the
behavioural-reorganisation question at all, not a REE finding.**

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

## Repair pathway — ALREADY CHIPPED, sharpened by a document read after the initial draft of
this artifact

`complicated (buildable)` — recording gap, not a measurement redesign. Originally drafted as an
independent "909a" recording-only re-run recommendation; checked against
`sleep_transition_investigation_906_lineage_2026-08-10.md` before finalizing, which (a) sharpens
this autopsy's own "recording gap" framing to something more precise — Section 4 establishes
909 did not merely fail to record the right readout, it measured **sleep-mechanism internal
diversity, a different DV entirely**, with zero overlap with the behavioural-reorganisation
question — and (b) confirms a fuller fix is already chipped:
`chip-20260810-fishtank-developmental-ecology` item 3 has been amended (a third time, by that
same document, Section 9) to specify an explicit sleep-vs-matched-no-sleep ABLATION arm — the
minimum design that actually separates a sleep effect from ordinary elapsed-time/experience
effects, which a bare "add pre/post instrumentation" re-run (my original 909a framing) would not
by itself provide. **No independent 909a recommendation is issued here** — this autopsy's
finding is superseded by, and should be read through, that chip's design.

## `recommended_substrate_queue_entry`

`action: none` — this is an experiment-instrumentation gap, already routed via the existing
chip (see Repair pathway above), not a substrate/mechanism gap and not a fresh queue-experiment
proposal.

## Recommended `evidence_quality_note`

None — `claim_ids: []`, nothing to weight. `evidence_direction` stays `non_contributory`
(unchanged from the manifest).

## Growth-restriction / Step 9b

Not applicable — no fan-out, no pre-registered hypothesis adjudicated. Skip cleanly.

## Re-derive brake / granularity-debt

`claim_ids: []` — neither applies.

## Routing (revised after reading the sleep-transition investigation document)

**Already chipped, no new routing issued.** `chip-20260810-fishtank-developmental-ecology`
item 3 (amended a third time) already specifies the sleep-vs-no-sleep ablation design this
finding calls for, and does so more precisely (as an ablation, not a bare instrumentation
add-on) than this autopsy's original 909a framing. Governance should not spawn a duplicate chip
for this finding.
