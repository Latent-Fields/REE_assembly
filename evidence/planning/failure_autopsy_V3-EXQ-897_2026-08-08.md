# Failure Autopsy: V3-EXQ-897 (SD-009 event-CE ablation decodability confirmer)

**Date:** 2026-08-08
**Scope:** single
**Status:** confirmed
**Target:** `v3_exq_897_sd009_event_ce_ablation_decodability_20260808T100554Z_v3` (queue V3-EXQ-897)
**Claim tagged:** SD-009 only (deliberately does not tag MECH-100 or SD-070 -- see driver docstring)

---

## 1. Facts

**dry_run check:** confirmed NOT a dry run (`check_dry_run_citations.py`: 0 dry cited, 1 clean).
**Recording provenance:** `validate_recording.py` reports 0 always-core gaps -- `substrate_hash`,
`config`, `seeds`, `machine`, `elapsed_seconds` all present.

**Manifest.** `experiment_purpose: evidence`, `outcome: FAIL`, `evidence_direction: unknown`,
`interpretation.label: sd009_event_ce_effect_inconclusive`.

Preconditions (both met, `readiness_ok: true`):
- `positive_control_hazard_in_view_decodable`: measured 0.3161 vs threshold 0.30 -- met.
- `encoder_actually_trained`: 5 changed world-path tensors vs threshold 1 -- met.

Load-bearing criterion `event_ce_on_clears_floor_and_beats_off_majority_seeds`: **failed**
(0/3 seeds satisfied it).

| seed | ON margin | OFF margin | delta (ON-OFF) | supports? |
|---|---|---|---|---|
| 42 | 0.0657 | 0.0909 | -0.0253 | no |
| 43 | 0.0480 | 0.0581 | -0.0101 | no |
| 45 | 0.0807 | 0.0860 | -0.0053 | no |

`mean_on_margin = 0.0648` -- above `EVENT_DECODABILITY_FLOOR = 0.05`, so the pre-registered
`weakens` branch (mean ON margin at/below floor) does not fire either. Per the driver's own
combination rule, the run lands exactly in `unknown`: readiness OK, majority not reached, ON
mean margin not at/below floor.

**The result is not merely "ambiguous," it is sign-consistent.** All three seeds show the OFF
arm (no dedicated event-type CE head) decoding event-type *at least as well as* the ON arm
(with the head). A null effect would put roughly half the seeds on each side; 3/3 in the same
direction is a small, imprecise, but directionally consistent negative signal for the
*marginal* contribution of the added head, layered on top of SD-070's other grounding heads.

**Script.** `ree-v3/experiments/v3_exq_897_sd009_event_ce_ablation_decodability.py` (commit
`3001981498e885eb94181cad93e64b6617df97ba`). 2 arms x 3 seeds (44 excluded, documented reef
instability). ARM_EVENT_CE_ON = SD-070 P0 recipe + an additional event-type CE head trained the
SD-070 way (buffered minibatches, class-balanced CE) -- explicitly NOT the substrate's own
`use_event_classifier` / `compute_event_contrastive_loss` path, which is online at batch=1 and
is exactly SD-070's documented collapse mechanism ("fault 3"). ARM_EVENT_CE_OFF = identical
SD-070 recipe, no event head. Primary DV: held-out decodability margin (macro-recall minus
class-count-adjusted chance) from a FRESH linear probe on a frozen, `.detach()`ed z_world,
trained on a rollout collected after the encoder is frozen -- deliberately a decodability
statistic, not the `selectivity_margin` cosine-separation statistic EXQ-020/023 used.

**Queue entry.** `experiment_purpose: evidence`, no `supersedes`. `GOV-REUSE-1` check in the
docstring: 0 manifests in the 832-manifest corpus tag SD-009 with either
`event_classification_acc` or `selectivity_margin`; the one candidate (EXQ-020) predates the
2026-07-12 recording standard (no `substrate_hash`) and ran under the pre-SD-070 P0 -- not
reusable.

**Expected vs observed.** Expected (per pre-registration): either a clean majority-seed
ON-beats-OFF pattern (`supports`) or a clean floor-failure (`weakens`). Observed: readiness
clean, ON arm itself decodable above floor in all 3 seeds, but OFF matches or beats it in all 3
-- the specific "ambiguous marginal contribution" case the driver's own docstring named in
advance as a live possibility for this design.

## 2. Claim-layer mapping

**SD-009** (`design_decision`, status `provisional`, `depends_on: [SD-005]`).
`claim_evidence.v1.json`: `genuine_exp_count: 0`, `literature_confidence: 0.724` (2
`lit:computational_model` entries: ADAT/Kim2022, CURL/Laskin2020 -- both RL representation-
learning papers, zero biological entries tracked). EXQ-020/023 do not currently count for
SD-009 (tagged `claim_ids_tested`, pre-2026-07-12 standard, no `substrate_hash`) -- this run is
effectively the FIRST experimental evidence entry SD-009 would receive under the current
indexer.

**Did the test let the claim express itself?** Yes, with one declared scope precision. The run
holds SD-005 and SD-070 constant (both implemented, correctly not re-litigated) and ablates only
the added event-CE head, using a validated positive control and a genuine frozen-encoder probe
-- a fair, well-controlled test. But it tests SD-009 *layered on top of SD-070's grounding
heads*, using a buffered-minibatch reformulation of the CE idea (to avoid reintroducing SD-070's
documented collapse mechanism) -- not the *original* SD-009-prescribed training procedure
(online CE, batch=1) under which EXQ-020's supporting evidence was gathered. This is the
correct design choice (re-running the original procedure would reintroduce the exact collapse
SD-070 fixed), but it means this run answers a narrower question than SD-009's literal
"requires" language: *does an additional event-type CE head help, given SD-070's other
categorical grounding heads are already present* -- not *does categorical event supervision
matter for z_world at all*.

**The bigger reconciliation this surfaces (not this run's own claim tags, but directly
relevant).** SD-070's own `claims.yaml` entry (`docs/architecture/sd_070_zworld_p0_anticollapse_recipe.md`)
documents that the ORIGINAL SD-009-prescribed P0 (online CE at batch=1 -- exactly what EXQ-020
ran) **collapses z_world to participation_ratio ~1.06**. EXQ-020/023's PASS evidence currently
backs **MECH-100** (`stable`, `genuine_exp_count: 4`, all `supports`, `overall_confidence:
0.713`) -- not SD-009 directly (already excluded there per the recording-standard gap above).
A 0.882 `selectivity_margin` measured on a near-rank-1 (collapsed) representation is a
materially weaker claim than "the encoder learned event-discriminative structure," exactly the
concern the 2026-07-18 planning doc already raised (see below).

**This run resolves the open governance question** in
[`sd009_event_contrastive_channel_mismatch_2026-07-18.md`](sd009_event_contrastive_channel_mismatch_2026-07-18.md)
(status: AWAITING GOVERNANCE ADJUDICATION, raised by the SD-070 implementation session). That
doc's central finding -- a probe on raw `world_obs` with no encoder in the path scores at or
below chance for event-type -- was measured either with no encoder at all, or (for the "trained
through the encoder" figure, 0.272-0.311 vs chance 0.333) through the pre-SD-070 *collapsing*
P0. V3-EXQ-897 supplies exactly the decodability re-measurement (as opposed to the earlier
`selectivity_margin` conflation) that doc's option (B) asked for, under the FIXED (SD-070)
substrate: z_world genuinely IS decodable for event-type above floor in both arms once the
collapse is fixed -- refuting the 2026-07-18 doc's strongest ("channel is uninformative")
reading -- but the *additional* event-CE head is not shown to be what supplies that
decodability; SD-070's other grounding heads may already suffice.

## 3. Biological-reference triage

**Closest mammalian reference and its citation status.** MECH-100's `claims.yaml` notes cite a
genuine biological reference: ventral-stream category selectivity requires a categorical
top-down training signal, not pure predictive coding/reconstruction alone (Murray et al. 2004,
TICS 8:56-61) -- offered as the biological grounding for "the event classifier is the minimal
stand-in for such categorical supervision." **This citation was never entered into
`claim_evidence.v1.json` as a tracked `targeted_review_sd_009` literature entry** -- SD-009's
tracked `literature_confidence` (0.724) rests entirely on the two computational-RL papers
(ADAT, CURL), not on Murray et al. This is a real evidence-tracking gap: a formal-training-
technique import (categorical CE auxiliary loss, straight out of RL representation-learning
literature) is doing rhetorical work citing biology, without that biology ever being registered
as evidence.

**Does the biology actually predict this run's outcome?** Ambiguously, on inspection. Murray et
al.'s point is categorical-vs-none: predictive coding alone does not yield category-selective
representations. But SD-070's own grounding heads (hazard-presence, resource-presence
classifiers) ARE themselves categorical top-down supervision -- just not event-type-specific.
So even the OFF arm in this run has *some* categorical supervision, satisfying Murray et al.'s
general point already, independent of the additional event-CE head. The biological principle
is not clearly falsified or confirmed by this specific ablation; it mainly clarifies that the
principle, if true, does not obviously require *this specific* additional head once SD-070's
other categorical heads are present.

**Formal-import status.** Confirmed formal-technique import from RL representation learning
(ADAT/Kim2022, CURL/Laskin2020) with a biological citation (Murray et al.) present only in
architecture-doc prose, not in the tracked evidence store.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact, with declared scope precision | fair test of "extra CE head marginal to SD-070," not the original vacuum condition EXQ-020 tested |
| Biological reference | partial | Murray et al. cited in MECH-100 prose, never tracked as SD-009 lit evidence; SD-070's own heads may already satisfy the cited principle |
| Developmental/dependency prerequisites | present | SD-005, SD-070 both implemented, correctly held constant |
| Implementation completeness | complete | clean thin-subclass ablation (`ZWorldP0TrainerEventCE`), no substrate modification |
| Environment adequacy | adequate, with a caveat | label imbalance (`hazard_approach` ~65-97% of samples) collapses the intended 3-class DV to `n_classes_scored: 2` in every cell -- noted, does not invalidate the paired ON/OFF comparison since it affects both arms symmetrically |
| Measurement adequacy | adequate, improved | correctly repairs the 2026-07-18 doc's `selectivity_margin`/decodability conflation; validated positive control confirms probe pipeline integrity |
| Integration adequacy | isolated | only the loss term differs between arms; fingerprints/hashes confirm arm identity |
| Scale/capacity | adequate | 60 P0 + 40 probe episodes, 3 seeds -- matches lineage convention |

**Recommended epistemic_category: `standard`** (a well-designed, genuinely informative,
honestly self-routed inconclusive result -- not a substrate ceiling, not a measurement gap, not
a precondition failure).

**Recommended evidence_direction: `unknown`** (matches self-route; user-confirmed, not
overturned -- the self-route here is honestly earned, not a hypothesis to correct).

## 5. Recurrence / brake checks

- **Re-derive brake:** first-ever SD-009-tagged confirmed autopsy (`granularity_debt_cluster.py
  SD-009` -> 0 tagging targets). Brake does not apply.
- **Granularity-debt trigger:** does NOT fire (0 tagging targets for SD-009 or MECH-100).
- **Cluster check:** `pending_review.md` regenerated fresh; only one other unclaimed manifest
  (V3-EXQ-887b, SD-014, clean `evidence`-purpose PASS -- out of this skill's scope, clears at
  `/governance`). No shared failure shape. Single-scope autopsy.
- **Hypothesis-space ledger (Step 9b):** no existing question node names SD-009 or MECH-100 in
  `hypothesis_space_registry.v1.json`, and this is not a GOV-FANOUT-1 discrimination portfolio
  (no `fanout_recommendation`). Per the skill's own carve-out ("a lone non-fan-out FAIL that
  discriminates nothing and opens no rival set... skip cleanly"), Step 9b is skipped -- nothing
  registered.

## 6. Learning extracted

1. **Existing dependency strengthened (partially) / claim needs no change on its own.** The
   2026-07-18 open governance question is resolved: z_world genuinely carries decodable event-
   type information once the SD-070 collapse fix is in place (refuting the strongest "channel
   uninformative" reading). This is informative independent of SD-009's own adjudication.
2. **Soft signal against the specific "requires a dedicated event-CE head" formulation.** 3/3
   seeds show OFF matching or beating ON; small, imprecise, but sign-consistent. Not strong
   enough for a formal `weakens` (does not meet the pre-registered bar; only 3 seeds; effect
   within single-seed noise), but real enough to record rather than discard.
3. **Adjacent evidence-quality concern (MECH-100, not this run's own claim tags).** MECH-100's
   `stable` status rests on `genuine_exp_count: 4` supports, all gathered on the P0 that SD-070
   now documents as collapsing z_world. This run's clean re-measurement under the fixed
   substrate is the natural trigger to revisit that evidence's currency, per the 2026-07-18
   doc's own candidate option (B) (mark candidate-stale pending decodability re-measurement).
4. **Evidence-tracking gap.** A biological citation (Murray et al. 2004) doing real rhetorical
   work for SD-009/MECH-100 in `claims.yaml` prose has never been entered into
   `claim_evidence.v1.json` as tracked literature evidence -- SD-009's `literature_confidence`
   is computed as if no biology had ever been reviewed for it.

## 7. Repair pathway / routing (user-confirmed, 2026-08-08)

**User confirmed all three recommended options** (AskUserQuestion, logged to
`RECOMMENDATION_LOG.jsonl`):

1. **SD-009 disposition: standard/unknown, no status change.** Record the result honestly;
   the run is informative but does not meet the bar to demote SD-009's "requires" language on
   its own.
2. **MECH-100 evidence: recommend candidate-stale flag to governance.** Surface that EXQ-
   020/022/176/177's supporting evidence for MECH-100 was gathered under the P0 that SD-070
   documents as collapsing z_world to participation_ratio ~1.06, and that this run's decodability
   re-measurement under the fixed substrate is the natural occasion to revisit it, per the
   2026-07-18 doc's own option (B). MECH-100 is not tagged by this run and its adjudication is
   for governance to make, not this autopsy.
3. **Bio-lit registration gap: flag for governance to register directly.** Recommend governance
   add the Murray et al. 2004 citation as a tracked `targeted_review_sd_009` literature entry in
   `claim_evidence.v1.json` (a registration of an already-identified citation, not a fresh
   `/lit-pull` search).

**Draft `evidence_quality_note` for SD-009** (governance to apply, no status change):

> V3-EXQ-897 FAIL/unknown (2026-08-08): well-controlled ablation (2 arms x 3 seeds) of an
> additional event-type CE head layered on the SD-070 anti-collapse recipe (held constant in
> both arms). Positive control and encoder-trained preconditions both met. Primary DV (held-out
> frozen-probe decodability margin, not selectivity_margin) clears the floor in BOTH arms (mean
> ON 0.065, all seeds' OFF >= ON: deltas -0.025/-0.010/-0.005). Resolves the 2026-07-18
> "channel-mismatch" open question (`evidence/planning/sd009_event_contrastive_channel_mismatch_2026-07-18.md`):
> z_world IS genuinely decodable for event-type once the SD-070 collapse is fixed, refuting the
> strongest "channel uninformative" reading -- but the additional event-CE head's marginal
> contribution over SD-070's other grounding heads is not detected (3/3 seeds sign-consistent
> null-to-negative, within single-seed noise). No status change; this is the first genuine
> experimental-evidence entry SD-009 has received under the current indexer (`genuine_exp_count`
> was 0). Adjacent: MECH-100's existing `supports` evidence (EXQ-020/022/176/177) was gathered
> under the pre-SD-070 collapsing P0 -- recommend governance separately consider a candidate-
> stale flag there per the 2026-07-18 doc's option (B).

**Recommendation to governance re: 2026-07-18 planning doc.** Mark
`sd009_event_contrastive_channel_mismatch_2026-07-18.md` resolved/adjudicated, referencing this
autopsy and V3-EXQ-897 as the decisive re-measurement it was awaiting.

**Recommendation to governance re: literature evidence.** Register Murray et al. 2004 (TICS
8:56-61) as a `targeted_review_sd_009` entry in `claim_evidence.v1.json`'s literature evidence
store -- currently prose-only in MECH-100's `claims.yaml` notes.

**No `/implement-substrate`, `/lit-pull` (full commission), `/queue-experiment`, or
`/diagnose-errors` routing is recommended.** Nothing missing from the substrate; the citation
already exists (registration, not a search); the design is adequate as-is; not a crash.

## 8. Governance follow-on (per CLAUDE.md Session Land Protocol step 6 -- reported here, per the
`/failure-autopsy` exception, not chipped)

- Apply the draft `evidence_quality_note` to SD-009 (no status change).
- Mark the 2026-07-18 planning doc resolved, citing this autopsy.
- Consider a candidate-stale flag on MECH-100's EXQ-020/022/176/177 evidence (separate
  adjudication, MECH-100 not tagged by this run).
- Register Murray et al. 2004 as a tracked `targeted_review_sd_009` literature entry.
- Mark `v3_exq_897_sd009_event_ce_ablation_decodability_20260808T100554Z_v3` reviewed
  (`reviewed_run_ids` in `review_tracker.json`) once the above is applied.
