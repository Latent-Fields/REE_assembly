# Claim Synthesis -- ARC-120 (tagging mode: framing-level cross-tag of existing instance evidence)

- **Claim:** ARC-120 -- "Behavioural/write authority in REE is (and should remain) EARNED through
  demonstrated competence, never granted merely because a computation or mechanism exists: REE's
  existing authority-gating mechanisms are independently-discovered instances of one general
  developmental sequence -- existence -> representation -> competence -> authority -> behavioural
  influence -- rather than unrelated ad hoc gates." (`status: candidate`,
  `claim_type: architectural_commitment`, `epistemic_category: standard`, registered 2026-08-06)
- **Session:** recursing-engelbart-dfdf02 (campaign W4-S4 item 2;
  `[chip_ref: chip-20260903-arc120-framing-evidence-tagging]` under
  `chip-20260907-w4-s4-closure-remaining`)
- **Date:** 2026-09-07T17:24:11Z
- **Trigger:** EVB-1233 / EXP-0286 `release_condition` route **(a)** -- "EVIDENCE TAGGING /
  SYNTHESIS FIRST (route: /claim-synthesis or /governance, NOT /queue-experiment)" -- set by
  IGW-20260903-243 when it DECLINED an ARC-120 experiment on three independent gates. Also
  **GFLAG-0179** (`promotion_review`, open, raised 2026-09-06): "ARC-120 carries `exp_count 0`
  while pre-existing, CONFIRMED evidence at its own rung sits untagged, by an explicit decision
  recorded in a sibling claim." Item 1 of this campaign (ARC-130, REE_assembly `d0f11e8e6a`)
  deliberately left MECH-314/320/341 untagged as this rung's work.
- **Plan of record:** `evidence/planning/science_wave_campaign_plan_20260907.md` section 3, S4 row 2.

## TL;DR

**Zero compute, zero new claims, no experiment queued.** Two evidence sets are cross-tagged to
ARC-120 at FRAMING level: (A) three authority-ABSENT run findings that ARC-120's own
`what_would_answer` already names as its rung (MECH-314 / MECH-320 via the confirmed
`failure_autopsy_604a-624a-630_2026-06-03`, MECH-341 via V3-EXQ-614d), and (B) the four instance
gates the claim generalises over (ARC-107, SD-032b, MECH-261, MECH-094), cited as the
design-space corpus rather than stamped on any manifest.

**The finding that matters, and it is a limitation rather than a discharge.** ARC-120 asserts two
things: a DESCRIPTIVE half ("authority *is* earned ... never granted merely because a computation
exists"; the four gates are instances of one sequence) and a NORMATIVE half ("and should remain").
Set (A) supports only the first clause of the descriptive half -- **existence of a computation did
not confer authority, three times, in three independent mechanisms**. It does **not** show
authority *conditioned on* competence, because in all three cases authority was absent for an
incidental scaling/wiring reason with **no competence predicate anywhere in the path**. The
ordering was EMERGENT, not ENFORCED -- which is precisely the discrimination ARC-120's own
literature entry (`2026-09-02_arc_120_protracted_control_maturation_luna2015`) flags as the real
one: "the sequence is evidence for the principle only where the ordering is ENFORCED rather than
merely EMERGENT."

So the tag is real but **narrow**, and the honest verdict is: **ARC-120's experimental debt is
discharged in the sense that no V3 run can add to it, NOT in the sense that its central assertion
is now evidenced.** The one ENFORCED instance in the record is a code reading, not a run (the
ARC-108 JOB-2 habenula de-commit, section B5). Section "Recommendation" hands governance the
consequence: this ceiling, not `exp_count`, is what should govern any promotion.

**Discrimination gate (Step 3): not a FAIL cluster circling a too-coarse claim.** Zero children
proposed. This is the skill's tagging application; "decompose nothing" is the correct output.

## Step 1-2. The evidence set, assembled by content

ARC-120 was registered 2026-08-06. Every run below predates it, so none names ARC-120 in
`claim_ids` or in any autopsy `targets[]`; membership was established by reading what each run
MEASURED against the sequence's transitions, not by grep. ARC-120 appears in **no file in
`ree-v3`** and in no run manifest -- confirmed by the 2026-09-03 gating session and unchanged.

### Set A -- authority-ABSENT findings (ARC-120's own rung)

| # | Evidence | Kind / status | Transition it exercises | Reading for ARC-120 | Tagged here? |
|---|---|---|---|---|---|
| A1 | `failure_autopsy_604a-624a-630_2026-06-03` (`.md` + `.json`), `scope: cluster`, `status: confirmed`. `cluster_pattern.confirmed_reading: substrate_enrichment_selection_authority`; `load_bearing_pair: [V3-EXQ-604a, V3-EXQ-624a]` | cluster autopsy | **competence -> authority** (transition 3 -> 4): the signal exists, is represented and locally operates, but never changes argmax | **supports, descriptive half only** -- "a modulatory/secondary additive score-bias ... does not reach E3 action selection with enough authority to change argmax against the dominant primary (harm/goal) score term" | cited in `live_status.evidence` |
| A1a | `v3_exq_604a_q044_mech314_subflavour_ablation_sd056_substrate_20260602T202814Z_v3` (V3-EXQ-604a, MECH-314 curiosity bias, `experiment_purpose: evidence`, FAIL, `evidence_direction: non_contributory` for its own claims) | run manifest, flat + pack | as A1 | **supports** at framing level. Its four-layer diagnosis is the sentence: `implementation: "partial -- symbol not function: curiosity_bias_abs_mean = 0.0 at e3.select even in ARM_ALL_ON"`; `integration: "coupled but inert -- bias computed but e3.select does not let it change argmax"` | **YES** -- `evidence_direction_per_claim: {ARC-120: supports}` |
| A1b | `v3_exq_624a_arc068_mech320_niv_salamone_dissociation_20260602T172734Z_v3` (V3-EXQ-624a, MECH-320 vigor no-op penalty, evidence, FAIL, non_contributory for its own claims) | run manifest, flat + pack | as A1 | **supports** at framing level -- the second, independent instance of the same shape | **YES** -- same construction |
| A2 | `v3_exq_614d_mech341_within_class_temperature_committed_class_20260603T120121Z_v3` (V3-EXQ-614d, MECH-341, diagnostic, PASS, `evidence_direction: mixed`) | run manifest, flat + pack | as A1 | **supports** at framing level -- `interpretation_label = PASS_C1_C3_only_within_class_active_no_committed_class_lift`: the mechanism FIRES (within-class active, C3 substrate-readiness True) and leaves committed-class entropy invariant (C2 False) | **YES** -- same construction |
| A3 | V3-EXQ-630 | run in the same autopsy | -- | **NOT ARC-120 evidence.** The autopsy itself routes it separately: same family "but via a distinct proximate cause -- an environment confound, not bias-propagation" | **NO** |

A1a/A1b and A2 are **three independent mechanisms** (an exploration bonus, a vigor cost, a
within-class temperature) reaching the same wall in the same place. Three converging on one
transition strengthen a framing-level reading without duplicating each other.

### Set B -- the four instance gates the claim generalises over

Cross-tagged as ARC-120's **design-space corpus**, cited in the claim's evidence note. **No
manifest is stamped for these** -- see "Why set B is cited and not stamped".

| # | Gate | Registry state (read 2026-09-07) | Competence-like predicate it carries | Runtime state (2026-09-03 live probe) |
|---|---|---|---|---|
| B1 | **ARC-107** BG-like E3 selector constitution | `candidate`, `standard`, `v3_pending: false`. Latest evidence V3-EXQ-926a "supports/PASS -- last untested No-Go axis converts, at a non-default envelope floor (0.10 vs stock 0.30)". Its `evidence_quality_note` records that V3-EXQ-937b's stamped `supports` was **NOT applied** -- all six criteria analytically entailed by the shipped code | per-event eligibility mask; Go/No-Go pressures | `use_go_nogo_constitution`, `use_f_eligibility_demotion`, `use_modulatory_selection_authority` all **False** |
| B2 | **SD-032b** dACC/aMCC adaptive control | `candidate`, **`substrate_ceiling`**, `v3_pending: true`. Four consecutive nulls (445/445a/b/c), then 445h `does_not_support`; consumer pathway V_s-monostrategy-blocked | writes to a **learnable** striatal-analog target (learnability as the competence condition) | `dacc_weight = dacc_bias_max_abs = dacc_suppression_weight = dacc_drive_coupling = 0.0` -- implemented but **inert** |
| B3 | **MECH-261** mode-conditioned write gating | `stable`. Latest run evidence V3-EXQ-460g **non_contributory, NOT weakened** -- all closures hook-driven (`n_automatic_fires=0`), so the mode-conditioning predicate was never exercised. 5 lit entries, lit_conf 0.883; the SD-032a coordinator overlay is REE-specific with no direct rodent validation | operating mode gates which substrates may write | not exercised on the cited run |
| B4 | **MECH-094** real-vs-simulated write distinction | `stable`, promoted candidate -> provisional -> stable on **13 supporting literature entries** (conf 0.868) plus 12 supporting runs; latest per-run evidence non_contributory | `hypothesis_tag` provenance -- simulated content must not accumulate as committed experience | `use_simulation_mode_rule_gate` and `simulation_mode_rule_gate_admit_writes` both **False** |

**This table is the honest state of "already-evidenced", and it is more heterogeneous than the
chip's phrasing implies.** Two gates are `stable` but their most recent runs are
`non_contributory` (B3 explicitly did not exercise its predicate; B4's promotion rests
substantially on literature); one is `candidate` with an in-note refusal to apply its own latest
`supports` (B1); one is `candidate`/`substrate_ceiling` after four consecutive nulls (B2). **Not
one of the four has a run that tests the GENERALISATION**, and that is expected -- none was
designed to.

### B5. The one ENFORCED instance, and it is a code reading rather than a run

ARC-120's `what_would_answer` names the ARC-108 JOB-2 habenula de-commit as its "WORKED CONFIRMING
INSTANCE". Verified in code this session, `ree-v3/ree_core/governance/closure_operator.py`
`habenula_tick` (lines 505-575): the abort returns `fired=False` with
`reason="skipped:hypothesis_tag"` when `hypothesis_tag` is True (MECH-094 -- "a replay/DMN outcome
must not abort a waking commitment") and `reason="skipped:..."` when beta is not elevated
("nothing committed to de-commit").

This is the **only** instance in the corpus where a genuinely new behavioural authority is granted
and its admission predicate is an **explicit, enforced competence-like condition read from code** --
and, as the claim's own text notes, the gate was added for a reason internal to the mechanism
rather than to satisfy ARC-120. Two qualifications, both load-bearing:

1. `habenula_abort_enabled` defaults to **False** (`closure_operator.py:188`: "Default False ->
   habenula_tick is a no-op -> bit-identical"). It is a DESIGN-SPACE fact, which is the right
   currency for ARC-120's descriptive half, but it is not a runtime demonstration.
2. The same routine deliberately does **not** gate on operating mode ("a worse-than-expected
   outcome aborts content-wise regardless of operating mode"), an unrecorded carve-out against
   SD-034's mode-conditioning clause already noted by the 2026-09-04 thought-digestion G5 report.
   ARC-120 survives it -- the abort is still gated on MECH-094 and beta -- but the carve-out shows
   the gate family is not uniform.

### Why set B is cited and not stamped

Stamping an instance gate's own manifests with `ARC-120` would record that run as evidence about
the GENERALISATION. It is not: it is evidence about that gate. This is the peripheral-co-tag
mis-attribution the sibling ARC-130 gating (EVB-0633, 2026-08-26) identified and refused, and
which EVB-1233's `release_condition` names again in its "load-bearing half". An ARC-107 ablation
showing eligibility gates selection re-derives ARC-107; it does not adjudicate whether the four
gates are one sequence or four independent gates. Set B is therefore recorded in the claim's
evidence note as a **design-space corpus with per-gate provenance**, where a reader can see B2's
four nulls and B3's unexercised predicate, and cannot mistake either for a test of ARC-120.

Set A is stamped because those runs bear on ARC-120's own transition (competence -> authority) and
on no other claim's -- the finding is *authority absent*, which by ARC-130's 2026-08-26 boundary
("ARC-130 stops after authority is achieved; this claim's contribution is the POST-authority
granularity") belongs to ARC-120 and to nothing else.

## Step 3. Discrimination gate

Applied per the skill, though this is a support cluster rather than a FAIL cluster:

- **vacuous-criterion / test-design debt: none in set A, but note the shape.** A1's autopsy lists
  `test_design_per_mechanism_tuning` among its `readings` -- and then **rejects** it: the
  `confirmed_reading` is `substrate_enrichment_selection_authority`. Its measurement layer is
  recorded `adequate -- the null effect is real; selected_entropy identical across all 5 arms`,
  and `environment: adequate -- C0 confirms candidates are action-divergent`. A2 carries its own
  in-run positive control (C3 substrate-readiness True, within-class firing confirmed). So the
  nulls are real, not measurement artefacts.
- **substrate-not-ready: yes, and it is disqualifying for a RUN, not for this tag.** All four
  instance gates are default-off or inert; ARC-120's terminal rung ("behavioural influence") is
  behind the conversion / F-dominance ceiling. This is exactly why gates (2) and (3) of the
  2026-09-03 refusal stand and why no experiment is queued here.
- **single-point falsification: none.** No evidence in the corpus weakens ARC-120. Its registered
  falsifier is a design-space event (an accepted, production-reachable mechanism granting
  authority with no competence-like predicate); none has been found.
- **granularity debt: none.** There is no set of >= 2 distinct genuine FAIL signatures circling
  ARC-120 -- it has **zero autopsies** of its own (the 2026-09-03 re-derive brake count is 0). The
  claim is not too coarse for its evidence; it is a framing over evidence gathered for other
  claims.

**STOP for decomposition; PROCEED for tagging.** Zero child claims. No `/lit-pull` commissioned:
`evidence/literature/targeted_review_arc_120/` already carries 5 entries (lit_conf 0.851) and no
new mechanism is being registered that would need grounding.

## Step 4. The common thread (one sentence)

Every finding in set A shows a computation that exists, is represented, and locally operates, yet
acquires no authority over the committed argmax -- so **existence demonstrably does not confer
authority in this substrate**; but in none of them is the absence produced by a competence
predicate, so they evidence the claim's negative clause and leave its positive, conditional clause
("authority is EARNED through demonstrated competence") resting on design-space reading alone.

## Step 6. The claim's fate: RETAINED AS-IS, with a two-half evidence map

Not an umbrella, not narrowed here, not superseded. (A narrowing proposal -- collapse the
five-stage ladder parenthetical to a cross-reference to ARC-130's longer ladder -- was raised as a
`contested_disposition` by the 2026-09-04 thought-digestion and is **propose-only**; it is
governance's, not this pass's, and is untouched.)

| Half of the claim | Content | Evidence status after this pass |
|---|---|---|
| Descriptive, negative clause | "never granted merely because a computation or mechanism exists" | **SUPPORTED** -- set A, three independent mechanisms, confirmed autopsy + two manifests |
| Descriptive, positive clause | "authority *is* EARNED through demonstrated competence" | **DESIGN-SPACE ONLY** -- B5 is the single enforced instance and it is a code reading, default-off; set B gates carry the predicates but none is a test |
| Descriptive, generalisation | the four gates are instances of ONE sequence, not four ad hoc gates | **UNTESTED and un-posable in V3** -- "one sequence" and "four independent gates" predict bit-identical telemetry (total verdict aliasing, gate (1) of the 2026-09-03 refusal) |
| Normative | "and should remain" | **NOT EMPIRICAL** -- discharged only by the standing design-space audit, route (b) |

| Sequence stage | Evidence status for ARC-120 |
|---|---|
| 1 existence | trivially exercised by every cited run -- not independently informative |
| 2 representation | as stage 1 |
| 3 competence | **not measured anywhere in set A** -- no run conditions on a competence predicate |
| 4 authority | **demonstrated ABSENT three times** (A1a, A1b, A2); demonstrated *conditioned* only at B5, in code, default-off |
| 5 behavioural influence | **UNTESTED** -- behind the conversion / F-dominance ceiling; must not be read as supported |

## What this pass changed (the tagging actions)

1. `docs/claims/claims.yaml` **ARC-120**: `live_status.as_of` -> 2026-09-07; `live_status.evidence`
   added, citing the confirmed 604a/624a/630 cluster autopsy and V3-EXQ-614d with the verdict
   "supports the descriptive negative clause at framing level; positive clause design-space only;
   generalisation untested"; a new `evidence_quality_note` field created (the claim had none)
   carrying the framing-level scope, the set-B per-gate provenance, and the enforced-vs-emergent
   limitation. **`status` stays `candidate`**, `epistemic_category` stays `standard` -- both are
   governance's (see Recommendation).
2. Three manifests stamped, flat **and** pack copies:
   `v3_exq_604a_..._20260602T202814Z_v3`, `v3_exq_624a_..._20260602T172734Z_v3`,
   `v3_exq_614d_..._20260603T120121Z_v3` -- `evidence_direction_per_claim["ARC-120"] = "supports"`
   plus an `evidence_direction_note` addendum stating the framing-level scope explicitly.
   **`claim_ids` is NOT touched on any of them.**
   **Scoring effect: none, by construction and verified in code.** `build_experiment_indexes.py`
   takes claim membership from `claim_ids_tested` (falling back to `claim_ids`) at L1892-1895 and
   iterates `for claim_id in run.claim_ids_tested:` at L3648, using
   `evidence_direction_per_claim` only as a per-claim *direction override* lookup at L3652. A claim
   absent from `claim_ids` therefore never enters `claim_evidence.v1.json` from that run. ARC-120
   keeps `exp_count 0`, `genuine_exp_count 0`, `experimental_confidence 0.0` and its
   `plausible_unproven` quadrant. **The stamp is an audit trail, not credit** -- deliberately, since
   granting scored credit would assert exactly the direct-test reading this pass refuses.
3. `evidence/planning/experiment_proposals.v1.json` **EXP-0286 / EVB-1233**: dated update appended
   to `gating_reason` recording that `release_condition` route (a) is DISCHARGED by this artifact
   and the proposal is RETIRED -- never to be queued. **`status` left at `blocked_substrate`** and
   `blocked_by` left intact: `blocked_substrate` is already in the workset's
   `_PROPOSAL_ADJUDICATED_NOT_QUEUEABLE_STATUSES`, so it is not re-offered, and every one of the
   five `blocked_by` tokens is still literally true (the no-runtime-discriminator token is
   *permanently* true -- it is not a blocker awaiting discharge). Changing the status to `gated`
   would be cosmetic, would gain nothing functional, and would take on the hand-set-status
   regen-revert risk for zero benefit.
4. GFLAG raised (`promotion_review`, ARC-120) carrying the Recommendation below, so it reaches
   `/governance` through the flag channel rather than a note. **GFLAG-0179 is left OPEN** -- it is
   a `promotion_review` flag addressed to governance, and item 1's precedent is that the executing
   session lands the tag while a governance cycle resolves the flag.

## Recommendation for the next /governance cycle (NOT applied here)

1. **Sequence the deferred category flip AFTER the promotion decision, not on this landing.**
   ARC-120's notes record: "Category HELD at `standard` deliberately: ... flipping
   `epistemic_category` to `derivational` now would suppress promote/demote and freeze the one
   adjudication route this claim has ... **Flip to `derivational` once that cross-tag lands.**"
   That cross-tag is this pass. But flipping *on landing* would re-freeze the promote/demote route
   in the same cycle it was unfrozen for, before anyone has adjudicated the evidence the flip was
   waiting on -- which is the opposite of what the hold was for. **Correct order: adjudicate the
   promotion question (2) first, then flip to `derivational` in the same cycle or the next.** The
   flip itself is right: the claim's residual falsifier is a standing code audit, which is what
   `derivational` names.
2. **Promotion: `candidate` -> `provisional` is NOT yet warranted, and `exp_count` is not the
   reason.** The tagged evidence supports one clause of one half (table in Step 6). The claim's
   central assertions -- that authority is *conditioned on* competence, and that the four gates
   are one sequence -- have design-space support and total verdict aliasing respectively. Promotion
   should wait on route (b), the standing audit, which is the only instrument that can move them.
   This differs from ARC-130's recommendation on purpose: ARC-130's own distinctive rungs were
   demonstrated by confirmed evidence; ARC-120's are not. Note the reciprocal condition item 1
   raised -- it asked governance to consider holding ARC-130 a cycle so the base could move first.
   **On this evidence the base should NOT move first; ARC-130 need not wait for it.**
3. **Consider `diagnostic_evidence_adjudicated: true` on ARC-120 -- governance's call, deliberately
   not taken here.** Verified mechanically: the flag suppresses `missing_experimental_evidence` and
   `lit_only_above_cap` in `build_experiment_indexes.py` (L7060-7061, L7122-7126). Two consequences
   worth stating plainly. (i) **EVB-1233's `release_condition` predicted the `why_now` signals would
   "clear on their own" once tagging landed. They will not** -- this pass grants no scored credit by
   design, so `exp_count` stays 0 and all five signals stand unless the flag is set. That prediction
   should be treated as corrected. (ii) The exposure is nonetheless *low*: EXP-0286 is already
   non-queueable, and ARC-120 cannot enter the GOV-CONFIRM-1 confirmer lane at all, because that
   lane's first guard is `if cid not in built: continue` and ARC-120 has zero `ree-v3` substrate
   footprint. The flag is therefore hygiene, not a live respawn risk -- which is why it is
   recommended rather than applied.
4. **Route (b) is the claim's real instrument, and it is unowned.** ARC-120's falsifier can only be
   discharged by a standing design-space audit over `claims.yaml` + the `ree_core/` write/authority
   sites, asking of each newly-accepted authority-granting mechanism whether its admission
   predicate carries a competence-like condition -- and, per luna2015, whether the ordering is
   ENFORCED or merely EMERGENT. The claim's own `what_would_answer` already specifies it in
   auditable detail (>= 5 mechanisms accepted since 2026-08-06; classify by **reading the admission
   predicate in code**, not the claim prose; 0-2 mechanisms -> "insufficient corpus", never
   "confirmed"). **Recommendation: a standing `/governance` audit bucket, not an architecture doc.**
   The obligation is recurring ("re-run at each governance cycle that accepts a new
   authority-granting mechanism") and its trigger is a governance event; a doc alongside
   `docs/architecture/causal_reach_and_installability.md` would record one snapshot and go stale,
   which is the failure mode ARC-120's own text is written to avoid. This pass does **not** build
   it (the chip says "Do not build it unasked"); B5 above is a worked first row for whoever does.

## Refusal ledger

- **Not queued:** no experiment. `experiment_queue.json` untouched. The three-gate refusal of
  2026-09-03 stands; this pass names no readout on which "one sequence" and "four independent
  gates" differ, and therefore has no standing to reopen it.
- **Not tagged:** the four instance gates' own manifests (set B) -- peripheral co-tag; V3-EXQ-630
  (distinct proximate cause, environment confound, routed separately by its own autopsy).
- **Not credited:** no `claim_ids` edit on any manifest; ARC-120 keeps `exp_count 0` deliberately.
- **Not promoted, not re-categorised:** `status` and `epistemic_category` untouched; the deferred
  `derivational` flip is sequenced in the Recommendation, not applied.
- **Not narrowed:** the propose-only ladder narrowing (thought-digestion G5, `contested_disposition`)
  is left for governance.
- **Not built:** the route-(b) audit bucket; no `substrate_queue` entry; no `ree-v3` change.
- **Not resolved:** GFLAG-0179 stays open for governance.
- **Not rebuilt:** the experiment index -- three per-claim overrides that change no score do not
  warrant a full regen (CLAUDE.md "Narrow Edits Only"); the next `governance.sh` picks them up.
