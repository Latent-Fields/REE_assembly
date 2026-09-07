# Claim Synthesis -- ARC-130 (tagging mode: closure on existing convergent evidence)

- **Claim:** ARC-130 -- "Organism-level mechanism status is stage-qualified beyond ARC-120's
  competence-before-authority sequence ... 'competence should precede authority, but authority
  must also demonstrate throughput.'" (`status: candidate`, `claim_type: architectural_commitment`,
  `epistemic_category: standard`, `diagnostic_evidence_adjudicated: true` since 2026-08-26)
- **Session:** serene-leavitt-f8ccf5 (campaign W4-S4 item 1; `[chip_ref: chip-20260905-arc130-claim-synthesis-tagging]`
  under `chip-20260907-campaign-w4-s4-zero-compute-closure`)
- **Date:** 2026-09-07T08:50:04Z
- **Trigger:** GFLAG-0134 (`contested_disposition`, raised 2026-09-04 by the campaign C3
  unowned-blocked-proposal audit) was resolved by the 2026-09-05 governance cycle with the
  **user decision (b)**: ARC-130 CLOSES on the existing convergent evidence via `/claim-synthesis`
  evidence tagging; **NO reach-stage instrumentation build is authorised** (the
  "MechanismReachTrace" schema stays recorded in the claim's own notes as an UNBUILT, unauthorised
  proposal). EXP-1344 (backlog EVB-0633) was left `gated` with the blocker
  `ARC-130-reach-stage-instrumentation-unauthorised` until this pass landed.
- **Plan of record:** `evidence/planning/science_wave_campaign_plan_20260907.md` section 3, S4 row 1.

## TL;DR

**Zero compute, zero new claims.** ARC-130's distinctive assertion -- that competitive authority at
an internal selection boundary and committed behavioural throughput are *independently
demonstrable, independently failable* stages -- is already demonstrated by pre-existing, CONFIRMED
evidence from two independent mechanisms. The 2026-08-26 cross-tag pass
(chip-20260826-arc130-authority-throughput-evidence-tagging) adjudicated that evidence into the
claim's `evidence_quality_note` and set `diagnostic_evidence_adjudicated: true`; what it did not
do, and what this pass does, is (1) record the closure as the claim's `live_status.evidence`
citation, (2) stamp the one manifest that genuinely exercised the claim with a per-claim
direction so the cross-tag is auditable at the manifest, not only in registry prose, (3) resolve
EXP-1344's instrumentation blocker against this artifact, and (4) hand a promotion recommendation
to the next `/governance` cycle. **The "three prior convergent instances" named in EXP-1344's
`blocked_note` are identified by content below and deliberately NOT tagged to ARC-130**: they
instantiate ARC-120's rung, ARC-120's own falsifier text now claims them, and their cross-tag is
S4 item 2 / GFLAG-0179, not this item.

**Discrimination gate (Step 3): this is not a FAIL cluster circling a too-coarse claim, so there
is nothing to decompose.** It is convergent SUPPORT for a claim registered *after* the evidence
existed. Zero children proposed. This is the skill's tagging application, not its decomposition
application, and "decompose nothing" is the correct output.

## Step 1-2. The evidence set, assembled by content

ARC-130 was registered 2026-08-25. Every run below predates it, so none names ARC-130 in
`claim_ids` or in any autopsy `targets[]`. Membership was established by reading what each run
MEASURED against the ladder's rungs, not by grep.

| # | Evidence | Kind / status | Rung it exercises | Reading for ARC-130 | Tagged here? |
|---|---|---|---|---|---|
| E1 | `failure_autopsy_931-932-wanting-authority-cluster_2026-08-16` (`.md` + `.json`), `scope: cluster`, `status: confirmed`, human-gated 2026-08-16T18:41:10Z | cluster autopsy over V3-EXQ-931 (FAIL) + V3-EXQ-932 (PASS) | **competitive authority -> committed throughput** (rungs 5 -> 6) | **supports** -- the cleanest single demonstration in the record that the two rungs dissociate | cited in `live_status.evidence` |
| E1a | `v3_exq_931_cem_wanting_weight_selection_authority_20260814T123949Z_v3` (V3-EXQ-931, `experiment_purpose: diagnostic`, `claim_ids: []`, `dry_run: false`, 5 seeds 42/43/45/46/47, `linux-x86_64`, ree-v3 `a57e6dd`) | run manifest, flat + pack | as E1 | **supports** (per-claim override; the run FAILed its own load-bearing C_AUTH criterion, which is precisely the authority-absent half of the dissociation) | **YES** -- `evidence_direction_per_claim: {ARC-130: supports}` on flat and pack copies |
| E1b | `v3_exq_932_zgoal_wanting_coupling_reinstrument_20260814T155424Z_v3` (V3-EXQ-932, diagnostic, PASS) | run manifest | none of the ladder's rungs -- it measures an observational coupling (residue_wanting -> locomotion at t+1) that the autopsy uses to *interpret* 931, not a stage of causal reach | n/a | **NO** -- tagging it would credit a coupling measurement to a reach-ladder claim |
| E2 | `diagnostic_arc071_commit_latch_h1h2_probe_2026-07-31.md` (H1 CONFIRMED ree_core wiring defect, H2 REFUTED) | unqueued scratch probe (no manifest) | **committed throughput** (rung 6, persistence sub-clause "survives any later selector, latch, commitment boundary, or stale-selection path") | **supports** -- an otherwise-valid commitment is overwritten by E3 re-deliberation every E3 tick; `_committed_step_idx` never advances past 1 | cited in `live_status.evidence` (no manifest to stamp) |
| E3 | `diagnostic_arc071_e3_reselection_probe_2026-08-01.md` (REAL, non-aleatoric defect at practically-used chunk sizes) | unqueued scratch probe (no manifest) | as E2 | **supports** -- 36.8 pct premature re-selection at `chunk_max_size=5`, 41-55 pct at 8/15 | cited in `live_status.evidence` (no manifest to stamp) |
| C1 | MECH-314 curiosity bias, MECH-320 vigor penalty: `failure_autopsy_604a-624a-630_2026-06-03` finding that the score-bias terms are "dominated by the primary harm/goal score term, so they never change argmax" | confirmed autopsy | **local operation -> competitive authority** (rungs 4 -> 5): the signal exists and operates but never competes at any forcing | authority ABSENT outright -- ARC-120's rung by ARC-130's own notes | **NO** (see "Why C1-C2 stay untagged") |
| C2 | MECH-341 within-class temperature: `v3_exq_614d_mech341_within_class_temperature_committed_class_20260603T120121Z_v3` (PASS, mixed) -- "fires but leaves committed-class entropy invariant" | run manifest, `claim_ids: [MECH-341]` | as C1 | as C1 | **NO** |

E1 + E1a and E2 + E3 are two independent mechanisms failing the SAME rung in two different ways
(a downstream re-scoring step ignoring an elite pick, vs. repeated re-deliberation overwriting an
otherwise-valid commitment). Two mechanisms converging on one rung strengthen the ladder-level
claim without duplicating each other.

### What E1/E1a actually show, restated in the ladder's own terms

At the documented operating weight (0.5) the hippocampal-CEM wanting term has no competitive
authority at the CEM's own elite-selection boundary: `wanting_authority_ratio ~= 0.0037`,
`selection_flip_rate = 0.0` in 5/5 seeds (`c_auth_seed_fraction 0.0`, in-run positive control
flips 5/5 so the null is not vacuous). Forced to full authority (w=5000), the CEM elite argmin
flips on 80.3 pct of genuine refits -- competitive authority ACHIEVED -- while
`mean_resource_proximity` is bit-identical to the ablation arm (`c_behav_proximity_gap_vs_ablated`
0.0 at W05/W50/W5000, 3.3e-4 at W500), because `REEAgent.select_action` re-scores the candidate
pool with `e3.last_scores` independently of the CEM's elite pick. That is authority at one
internal selection boundary with committed throughput exactly zero, at ~2700x the measured
operating-weight authority. It is the claim's sentence, measured.

Substrate-historical caveat, carried verbatim from the 2026-08-26 note: the SPECIFIC throughput gap
931 measured was partially closed by ree-v3 `1a4b6be` (2026-08-20: CEM elite-stage authority plus
a bounded, advisory-only-by-default throughput channel into E3's committed selection). The run's
numeric null is therefore historical for that call site; the LADDER POINT -- authority does not
imply throughput, each must be separately demonstrated and each can independently fail -- is what
ARC-130 asserts and is unaffected by the fix. The E2/E3 rung failure (E3 unexpired-commitment
short-circuit) is NOT built as of this pass: that rung is an active substrate gap.

### Why C1-C2 stay untagged (the peripheral-co-tag refusal, restated so it is not re-litigated)

ARC-130's own registered notes draw the boundary: "ARC-120 stops at 'behavioural influence'; this
claim's contribution is specifically the POST-authority granularity." C1-C2 measure a signal that
never achieves competitive authority at any forcing. They do not measure authority achieved and
throughput failing; they measure authority absent. That is the transition ARC-120 owns, and since
2026-09-06 ARC-120's own `what_would_answer` names exactly these three findings as "the
authority-ABSENT findings ARC-130's 2026-08-26 note explicitly assigns to it", with GFLAG-0179
(`promotion_review`, open) owning the cross-tag. Tagging them to ARC-130 as well would (i) be the
peripheral-co-tag mis-attribution the ladder exists to prevent, (ii) double-count one finding under
two claims at adjacent rungs, and (iii) pre-empt S4 item 2. EXP-1344's `blocked_note` phrase
"three prior convergent instances" is ree-v3 `1a4b6be`'s commit-message framing of a
*substrate-queue bottleneck* ("scoring-layer signals do not reach the committed argmax") and is
correct AS a bottleneck count; it does not make the four instances co-equal evidence for ARC-130's
post-authority rung. Only the fourth instance (931) reaches that rung.

The one respect in which C1-C2 touch ARC-130's text at all is the parenthetical at rung 5,
"non-zero influence is not necessarily competitive influence against the dominant arbitration
term". That parenthetical is a *definition of the rung boundary*, not a separate empirical
assertion; the shared `authority_spread_ratio()` / `authority_ratio_is_competitive()` readiness
gate ree-v3 `1a4b6be` added (floor 0.1, reported never enforced) is its operational form. Its
evidence is ARC-120-rung evidence and is credited there.

## Step 3. Discrimination gate

Applied per the skill, though the cluster is a support cluster rather than a FAIL cluster:

- vacuous-criterion / test-design debt: **none**. 931's null has an in-run positive control
  (5/5 flips at w=5000) and `criteria_non_degenerate` is recorded; E2/E3 are direct wiring
  probes with confirmed, named defects.
- substrate-not-ready: **partially, and it is the point, not a disqualifier**. The rung ARC-130
  uniquely contributes (committed throughput) is behind four default-OFF knobs and is known-broken
  at the E3 re-selection site. For a claim that asserts "these rungs can independently fail", a
  substrate in which they demonstrably do is evidence, not a readiness exclusion. It IS a readiness
  exclusion for any future run reaching for rungs 7-8 (recorded under EXP-1344).
- single-point falsification: **none** -- no evidence in the corpus weakens ARC-130.
- granularity debt: **none** -- there is no set of >= 2 distinct genuine FAIL signatures circling
  ARC-130; the claim is not too coarse for its evidence, it is *finer* than the flat
  implemented/not-implemented judgment its evidence was originally recorded under.

**STOP for decomposition; PROCEED for tagging.** Zero child claims. No `/lit-pull` commissioned:
the claim already carries `evidence/literature/targeted_review_arc_130/` (Bacon/Harb/Precup 2017;
Harb et al. 2018; Nijjer 2026 candidate, preprint-confidence) and no new mechanism is being
registered that would need grounding.

## Step 4. The common thread (one sentence)

Every piece of tagged evidence shows a signal that is present, represented, endogenously
recruited and locally operating -- and in 931 competitively authoritative at its own boundary --
whose effect nonetheless never survives the next selection or commitment surface downstream: the
ladder's rungs are separable in the running organism, which is the whole of what ARC-130 adds to
ARC-120.

## Step 6. The claim's fate: RETAINED AS-IS, with a stage-qualified evidence map

Not an umbrella, not narrowed, not superseded. The ladder is already the finest useful unit
here; what was missing was the per-rung evidence map, which is the claim's own recommended
recording doctrine applied to itself:

| Rung | Stage | Evidence status for ARC-130 as an audit projection |
|---|---|---|
| 1 | existence | trivially exercised by every cited run (the mechanisms exist) -- not independently informative |
| 2 | representation | as rung 1 |
| 3 | endogenous recruitment | 931: wanting field live on 100 pct of steps (P1 gate passed) -- exercised, not the claim's contribution |
| 4 | local operation | 931: CEM scores the term (P3 instrument-capable passed); C1-C2 (ARC-120 rung) |
| 5 | competitive authority | 931: absent at operating weight, achieved at w=5000 -- **demonstrated as an independently failable stage** |
| 6 | committed throughput | 931: zero even with authority forced (cross-boundary re-scoring); E2/E3: overwritten by E3 re-deliberation (persistence) -- **demonstrated as an independently failable stage, by two mechanisms** |
| 7 | ecological consequence | **UNTESTED** -- behind the conversion / F-dominance ceiling; must not be read as supported |
| 8 | retention / generalisation | **UNTESTED** -- must not be read as supported |

Version-routing: unchanged. The registered flag asking a governance session to confirm v3
scoping (vs. a v4/v4_v5 park like ARC-128) is still open and is listed for the next cycle below.
No reach-stage instrumentation is authorised, built, or drafted; the claim's notes are not edited.

## What this pass changed (the tagging actions)

1. `docs/claims/claims.yaml` ARC-130: `live_status.as_of` -> 2026-09-07; `live_status.evidence`
   added, citing the confirmed 931/932 cluster autopsy and the two ARC-071 probes with the verdict
   "supports at rungs 5-6, rungs 7-8 untested"; dated addendum appended to
   `evidence_quality_note` pointing here. `status` stays `candidate` (promotion is governance's,
   below). `docs/assets/data/claims.json` rebuilt (`build_claims_json.py`): no diff, it does not
   project `live_status.evidence` or `evidence_quality_note`.
2. `evidence/experiments/v3_exq_931_cem_wanting_weight_selection_authority_20260814T123949Z_v3`
   (flat manifest, `.json` at `evidence/experiments/`) and `.../v3_exq_931_cem_wanting_weight_selection_authority/runs/<run_id>/manifest.json`
   (pack): `evidence_direction_per_claim: {"ARC-130": "supports"}` with an
   `evidence_direction_note` addendum. `claim_ids` stays `[]` -- the driver's own "WHY NO CLAIM
   TAG" design decision is not overridden. **Scoring effect: none, by construction and verified.**
   The indexer takes claim membership from `claim_ids` and uses `evidence_direction_per_claim`
   only as a per-claim direction override (`build_experiment_indexes.py` ~L1852-1867); the
   precedent `v3_exq_445` (claim-free diagnostic carrying five per-claim overrides) does not
   appear in `claim_evidence.v1.json` under any of them. ARC-130 therefore keeps
   `exp_count 0` and its `plausible_unproven` quadrant, with `diagnostic_evidence_adjudicated:
   true` continuing to suppress the spurious `missing_experimental_evidence` /
   `lit_only_above_cap` signals. The stamp is an audit trail, not credit.
   `check_dry_run_citations.py` run on this artifact before commit: exit 0, 0 dry run_ids cited,
   0 ambiguous (V3-EXQ-931 has no dry sibling on disk).
3. `evidence/planning/experiment_proposals.v1.json` EXP-1344: `blocked_by` token
   `ARC-130-reach-stage-instrumentation-unauthorised` replaced by this artifact's path; ARC-071
   and ARC-120 kept as the standing prerequisites for any future rung-7/8 run; `status` stays
   `gated` (the IGW workset's `_PROPOSAL_ADJUDICATED_NOT_QUEUEABLE_STATUSES` includes `gated`, so
   it is not re-offered; `executed` would be false -- nothing ran). Dated update appended to
   `gating_reason`. The proposal is RETIRED per its own `release_condition` (a) and GFLAG-0134 (b).
   It lives only in the generated file (not `manual_proposals.v1.json`), so the regen carry-forward
   of `gated` is the surviving state.
4. GFLAG raised (`promotion_review`, ARC-130) pointing here, so the recommendation below reaches
   `/governance` through the flag channel rather than a note.

## Recommendation for the next /governance cycle (NOT applied here)

1. **Promotion: `candidate` -> `provisional` is warranted on the tagged evidence, with two
   conditions governance should settle in the same cycle.** The claim's distinctive rungs (5-6) are
   demonstrated by confirmed evidence from two independent mechanisms; nothing weakens it;
   `lit_conf 0.736` over three computational-model entries. The `exp_conf` gate cannot be the
   criterion here -- `exp_count` is 0 by the design decision already recorded (fix shape 1), which
   is exactly the situation `diagnostic_evidence_adjudicated` exists to name. Conditions:
   (a) confirm the open VERSION-ROUTING flag (v3 scoping vs v4/v4_v5 park) -- a provisional claim
   should not carry an unresolved routing flag; (b) decide base-before-refinement: ARC-120 is
   `candidate` with `exp_count 0` and its own rung cross-tag is pending (GFLAG-0179 / S4 item 2).
   If governance prefers the base to move first, HOLD one cycle and promote both together; the
   evidence for ARC-130's rungs does not depend on ARC-120's tag landing, so promoting ARC-130
   first is defensible but out of order.
2. **Do not read rungs 7-8 as supported.** Any future promotion beyond `provisional` needs
   ecological-consequence and retention evidence, which are behaviourally blocked (conversion /
   F-dominance ceiling) and instrumentation-blocked (unauthorised schema). That is the correct
   ceiling for this claim's status until a separate build decision, not an evidence defect.
3. **GOV-FAILLOC-1 amendment** (the claim's own folded-in "record the furthest stage demonstrated"
   doctrine) remains flagged-not-done in the claim's notes; this artifact's rung table is a worked
   instance of that doctrine and can serve as its template if governance takes it up.

## Refusal ledger

- Not tagged: V3-EXQ-932 (coupling measurement, not a reach rung); MECH-314 / MECH-320 / MECH-341
  findings (ARC-120's rung; owned by GFLAG-0179 and S4 item 2).
- Not built, not drafted: reach-stage instrumentation / `MechanismReachTrace`; no substrate_queue
  entry.
- Not promoted: ARC-130 status untouched; recommendation routed via GFLAG.
- Not run: no experiment queued; `experiment_queue.json` untouched.
- Not rebuilt: the experiment index (`build_experiment_indexes.py`) -- a single per-claim override
  on one manifest does not warrant a full regen (CLAUDE.md "Narrow Edits Only"); the next
  `governance.sh` picks it up and, per the scoring analysis above, it changes no score.
