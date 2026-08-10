# Failure Autopsy: V3-EXQ-906b / 906c / 911 cluster (fishtank ecology/measurement showcase)

**Generated:** 2026-08-10T14:21:33Z
**Scope:** cluster (shared shape: fishtank ecology observational showcase, all `claim_ids: []`)
**Status:** confirmed
**Targets:** V3-EXQ-906b (PASS), V3-EXQ-906c (PASS, flagged `precondition_unmet`), V3-EXQ-911 (PASS)

Written as part of `/governance`'s Step 1.5 inline autopsy pass (session
`queue-depth-low-ops-aac785`), clearing the un-adjudicated diagnostic set found by the
pre-flight. Primary source material: `organism_lifespan_development_review_906_lineage_2026-08-10.md`
and `reef_ecology_strategy_affective_occupancy_review_2026-08-10.md` (both read in full this
session) — this autopsy adjudicates and structures their findings, and adds source-code-level
verification the reviews did not perform.

**Dry-run gate:** `check_dry_run_citations.py` run against all three run_ids — 0 dry hits, all
clean. `dry_run_checked: true`.

**Recording provenance:** all three carry `recording_schema: rec/v1`, `substrate_hash`,
`machine`/`machine_class`, `elapsed_seconds`, `seeds` — no recording gap on the always-core.

---

## Facts

All three are diagnostic-purpose showcases on the 906-lineage full-stack observational fishtank
(`claim_ids: []`, do not weight governance). PASS gates in all three: harm-pathway training ran
(≥3735 steps), core affect channels non-degenerate, eval ecology survivable (well past 906's
early-death signature). 911 additionally gates on `benefit_approach_confound_reduced` (a
narrowed benefit field vs 906b's grid-wide one, sample floor 20, measured 68). 906c additionally
carries a third precondition, `excite_channel_contaminated` (`met: false`) — the driver's own
authors explicitly documented, at authoring time, that SD-RESIDUE-VALENCE-BOUND had not yet
landed, and that `coupling_excite_benefit_contemporaneous_r` must not be read as a trustworthy
appetitive-anticipation readout as a result.

## Claim-layer map

`claim_ids: []` on all three — no claims.yaml entry to map to directly. The cluster's findings
bear on **MECH-309** (candidate, `substrate_ceiling`, gated on SD-054/SD-029/MECH-256/MECH-269/
ARC-062/ARC-063/ARC-077) by corroboration, not by direct tagging — see "Claim-layer
corroboration" below.

## Biological-reference triage

The reef/shelter mechanic (SD-054) is explicitly pre-registered on a coral-reef-refugia
prey-fish analogy (`sd_054_reef_enrichment_substrate.md`, 2026-05-04), and its own design
record already downgraded its target from "balanced switching" to "expect monomodal collapse"
as of 2026-07-10 — well before this cluster ran. So the biological reference for the *shelter*
half of the finding is well-established and pre-dates this observation; the finding here is
which pole a real, protective collapse favours, not whether collapse itself is anticipated.

## Four-layer diagnosis (per finding, not per target — findings span the cluster)

### Finding 1 — Reef-strategy convergence is MIXED, corroborates MECH-309, is NOT a fresh claim

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim-free diagnostic; bears on MECH-309 by corroboration |
| Biological reference | clear | SD-054's own coral-reef-refugia analogy; already-tracked collapse-to-a-pole prediction (MECH-309) |
| Developmental / dependency prerequisites | present | MECH-309 depends_on chain (SD-054, SD-029, ARC-062 etc.) already implemented enough to observe the phenotype |
| Implementation completeness | complete | reef/shelter mechanic, benefit-field, harm-field all implemented and functioning as designed |
| Environment adequacy | too sparse (novel) | reef-to-nearest-resource gap (4-5 cells) exceeds sensory radius (2) in every episode of both runs — an opportunity-triggered-exit mechanism cannot be exercised by this geometry at all |
| Measurement adequacy | adequate for the excursion-frequency claim; the threat-return test is confounded by absolute distance | excursion frequency clears V3-EXQ-522's own pre-registered numeric bars comfortably; threat-triggered-return test is weak, distance-dependent, inconsistent across seeds |
| Integration adequacy | coupled but unstable | shelter/forage coupling is real (2.4x/1.6x harm-rate ratio, replicated) but not demonstrably contingent on sensed opportunity/threat |
| Scale / capacity | likely insufficient for a rule-apprehension layer | matches MECH-309's own diagnosis: a parametric-policy learner without a rule-apprehender collapses to the smoothest single regime |

**Failure-location (GOV-FAILLOC-1):** MECHANISM (already-tracked, MECH-309: no rule-apprehender
proposing discriminative "near-hazard→reef; else→forage" regimes) + ENVIRONMENT (novel: reef-
resource geometry structurally forecloses opportunity-triggered testing). Net: **MIXED, not
chargeable to REE alone** — and the mechanism half is not new; cross-reference MECH-309 rather
than treating this as a fresh finding, per the reef review's own Section 1c verdict, confirmed
correct on read of MECH-309's `evidence_quality_note` (19+ substrate-ceiling readings on the
same monomodal-collapse mechanism, most recently V3-EXQ-654g/714/719a).

### Finding 2 — Two new measurement/plumbing defects (906c): `residue_wanting` orphaned writer, `liking`/`dread` extend the excite accumulator defect

Verified directly against `ree_core/agent.py` and `ree_core/residue/field.py`:

- **`residue_wanting` orphaned writer.** `evaluate_valence(z_world)[0,0]` (VALENCE_WANTING, index
  0) is read correctly, but its two writer methods (`update_benefit_salience()`,
  `update_schema_wanting()`) are never called from inside the agent's own step loop — their only
  callers anywhere in the repo are unrelated experiment scripts. This is a **different** channel
  from `z_goal` (already characterized as sparse-but-real). Classification: MECHANISM/plumbing —
  the write path exists and works elsewhere, it is simply never invoked in this driver family.
- **`liking`/`dread` share `excite`'s unclamped-accumulator defect.** All six residue valence
  components go through the identical `RBFLayer.update_valence()` `+=` write path
  (`ree_core/residue/field.py`), already flagged for `excite` by the 906a autopsy under
  **SD-RESIDUE-VALENCE-BOUND**. `liking` (906c: mean=19.88, ~50x a smoke-observed per-step
  ceiling of 0.39) and `dread` (reef review Section 3b: ~40-55x rise across 8 episodes in both
  906b/906c, alongside excite's 20-110x rise) both show the same signature — confirmed the
  identical write path is the shared cause, not three independent bugs.

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim-free |
| Biological reference | n/a | plumbing/instrumentation defect, not a translation question |
| Implementation completeness | partial | writer methods exist but are disconnected from the step loop (wanting); accumulator has no clamp/decay across ALL six valence indices (excite/liking/dread confirmed, harm_discriminative/surprise/wanting not yet checked) |
| Measurement adequacy | under-instrumented / misleading | `liking`/`dread`/`excite` readouts are not currently trustworthy quantitative signals; the manifest's own contamination caveat is written only against `excite` and needs to extend |

**Failure-location:** MECHANISM (unclamped accumulator write path; orphaned wanting writer) +
MEASURES (contaminated readouts not flagged as such in the manifest for liking/dread). Net:
**MECHANISM+MEASURES**, not REE.

### Finding 3 — 906b/906c coupling nulls replicate cross-seed (corroboration, not new)

5 of 6 coupling metrics replicate within noise across 906b→906c (dread→harm, z_goal→approach,
z_goal→benefit, surprise-spike→mode-change, surprise-spike→moved); one
(dread↔z_harm_a contemporaneous) sign-flips (+0.032→-0.175), unexplained, single-seed each side.
This strengthens (does not merely repeat) the organism review's own Section-4 finding that affect
channels vary but largely do not predict subsequent behaviour/events at the moment-to-moment
level. **Failure-location:** candidate REE (weak internal-state→behaviour coupling), but this is
already an established, tracked reading (`is_committed`=0/N), not new here.

### Finding 4 — 906c's `precondition_unmet` flag is a correct, self-documented caveat, not a mislabel

Adjudicated: the flagged precondition (`excite_channel_contaminated`) is not a runtime
measurement — it is a governance-state check ("was SD-RESIDUE-VALENCE-BOUND applied to
claims.yaml as of authoring time") that the driver's own authors wrote in explicitly to prevent
`coupling_excite_benefit_contemporaneous_r` from being read as trustworthy until the fix lands.
The self-route label `coupling_instrumentation_live` is **not** invalidated by this — it asserts
only that the new coupling instrumentation is producing data, which is true. The flag correctly
narrows what can be trusted (one specific coupling metric); it does not mislabel the overall
result. No re-queue is owed for this reason alone — a future re-run after SD-RESIDUE-VALENCE-BOUND
lands should simply re-check this one metric, which the fix's own recommended_evidence_direction
will make possible without a dedicated re-queue.

---

## Cluster pattern

| Experiment | Shared shape | Reading |
|---|---|---|
| 906b | full-stack showcase, harm/ecology gates PASS | affect-behaviour decoupling baseline |
| 906c | + coupling instrumentation, 1 self-documented contaminated metric | decoupling replicates; 2 plumbing defects found |
| 911 | + narrowed benefit field (confound reduction) | excursion frequency clears V3-EXQ-522's own bars |

**This is one structural property, not three independent showcases**: all three exercise the
identical harm-pathway-trained, reef-enabled substrate, and every genuinely new finding
(residue channel contamination, reef-geometry foreclosure) is a property of that shared
substrate, not of any one run's specific config. The three showcases corroborate and extend each
other rather than testing independent things.

---

## Learning extracted

1. `residue_wanting` writer methods exist but are never called in the 906-family step loop — a
   novel, previously-unflagged plumbing bug.
2. `SD-RESIDUE-VALENCE-BOUND`'s scope must widen from `excite` alone to **all six** valence
   indices — `liking` and now `dread` are independently confirmed to share the identical
   unclamped-accumulator write path.
3. The reef-to-nearest-resource spatial gap (4-5 cells, sensory radius 2) makes an
   opportunity-triggered-exit mechanism untestable by construction in the current ecology — a
   concrete, fixable geometry requirement for any developmental-ecology redesign.
4. Reef-strategy convergence corroborates the already-tracked MECH-309 mechanism gap
   (monomodal collapse without a rule-apprehension layer) in a new context (which pole a real,
   protective collapse favours) — it does not license a new claim.
5. Excursion frequency in this diagnostic-showcase config comfortably clears V3-EXQ-522's own
   pre-registered numeric bars (C1/C2/C3) — a genuinely positive observation for a future
   *properly scored* trained-policy retest to test formally (not asserted as a pass here, since
   these are diagnostic showcases, not the scored arm V3-EXQ-522 targets).

## Repair pathway

- **Finding 2 (residue defects)** → `complicated (buildable)` → `/implement-substrate`. Wire
  `update_benefit_salience()`/`update_schema_wanting()` into the step loop; extend the
  clamp/decay fix (already scoped for `excite`) to `liking` and `dread` explicitly.
- **Finding 1 environment gap (reef geometry)** → `complicated (buildable)` design constraint for
  a future ecology redesign → `/queue-experiment` (new EXQ; not queued here per the
  mandatory-skill-path rule). Two concrete requirements to carry forward: (a) resource
  reachability from at least the edge of the shelter zone's sensory range; (b) decouple sleep
  firing from segment-boundary reset (this second requirement is 909's territory — see that
  autopsy).
- **Finding 1 MECH-309 corroboration** → governance note only (see below); no claims.yaml status
  change.

## Recommended `evidence_quality_note` additions

**For MECH-309** (append, do not replace — this is a corroboration, not a new reading):

> 2026-08-10 (failure_autopsy_906b-906c-911-cluster_2026-08-10, confirmed): V3-EXQ-906b/906c/911
> (diagnostic showcases, claim_ids=[]) corroborate the monomodal-collapse-without-rule-apprehender
> reading in a NEW context: real, replicated protective shelter use (2.4x/1.6x lower harm-rate
> while sheltering) with excursion frequency comfortably clearing V3-EXQ-522's own pre-registered
> numeric bars (C1/C2/C3), but no demonstrated contingent control (opportunity-triggered exit is
> structurally untestable by the current ecology's geometry; threat-triggered return is weak,
> distance-dependent, inconsistent across seeds). This is the collapse landing on the safety pole
> of a real two-attractor context, exactly as MECH-309 predicts happens absent a discriminative
> rule-apprehension layer -- not a fresh finding; no status/confidence change.

No `evidence_direction` change on any of the three target manifests — `claim_ids: []`, they
correctly weight nothing.

## `recommended_substrate_queue_entry`

**Action: amend.** `target_sd_id: SD-RESIDUE-VALENCE-BOUND`. The 906a/894b autopsy
(`failure_autopsy_V3-EXQ-906a_894b_2026-08-09`) already recommended `action: create` for this
exact `sd_id_suggested`, but governance has not yet applied it to `substrate_queue.json` this
cycle (Step 6a-iv runs later in this same cycle) — per the skill's collision rule for parallel
autopsies recommending the same gap, this is an amend against that pending create, not a
duplicate. `severity: degrading` (known limitation, weakens confidence in specific coupling
metrics, does not invalidate the showcase's own PASS gates) on `ree_core/residue/field.py`
(`RBFLayer.update_valence`) and `ree_core/agent.py` (`update_benefit_salience`,
`update_schema_wanting` — orphaned writer, a related but distinct plumbing gap on the same file).

```json
"failure_record_entry": {
  "run_id": "v3_exq_906c_full_stack_observational_fishtank_20260810T014711Z_v3",
  "experiment_type": "v3_exq_906c_full_stack_observational_fishtank",
  "metric": "liking mean=19.88 (~50x a smoke-observed 0.39 per-step ceiling); dread rises 40-110x across 8 episodes in both 906b/906c (excite already flagged); residue_wanting exact 0.0/3793 steps (orphaned writer, not floor)",
  "target": "liking/dread/excite bounded to a per-tick-plausible hedonic-impact range after clamp+decay; residue_wanting writer methods invoked from the agent step loop",
  "resolved": "open"
}
```

## Growth-restriction / Step 9b (hypothesis-space registry)

Not applicable — no `fanout_recommendation` (this is not a discrimination between live rival
hypotheses; the reef-strategy finding is a corroboration of an already-adjudicated mechanism,
and the residue defects are a plumbing bug, not an open scientific question), and no target
adjudicates a pre-registered hypothesis. Checked: no existing `qid` in
`hypothesis_space_registry.v1.json` references MECH-309/906-lineage/MECH-489. Skip cleanly.

## Re-derive brake / granularity-debt check

`claim_ids: []` on all three targets — no claim-keyed brake or granularity-debt cluster applies.

## Routing (confirmed at interactive gate)

- **implement-substrate** — SD-RESIDUE-VALENCE-BOUND amend (residue channel fixes, `residue_wanting` orphaned writer)
- **queue-experiment** (future session, not spawned here) — developmental-ecology redesign carrying forward the reef-resource reachability requirement
- **governance note only** — MECH-309 corroboration, no claims.yaml status/confidence change
