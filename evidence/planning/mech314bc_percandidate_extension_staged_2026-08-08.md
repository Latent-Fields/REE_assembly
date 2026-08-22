**Status: REVIEWED 2026-08-22 -- SPLIT OUTCOME. Section 4's budget-split resolution was NOT ratified; follow-on item 1 WAS authorised. Nothing in this file has been written to claims.yaml (or any other registry) as a status/flag change; the accompanying claims.yaml edits remain `implementation_note`s only. See the Review outcome section at the end.**

# MECH-314b / MECH-314c per-candidate architectural slot (ARC-065 GAP-A Phase-2 extension)

Session: `metaworker-chip-20260808-mech314bc-percandidate-extension` (headless metaworker-dispatch, 2026-08-08).
Chip: `chip-20260808-mech314bc-percandidate-extension`.
Substrate-queue entry: `ARC-065` (`REE_assembly/evidence/planning/substrate_queue.json`).

## 1. What this chip was asked to build

Give MECH-314b (uncertainty) and MECH-314c (learning-progress) a **genuine per-candidate
read** over the e2_world_forward candidate rollouts -- the same Phase-2 treatment MECH-314a
(novelty) already received (landed 2026-06-07, `candidate_summary_source=e2_world_forward`,
validated V3-EXQ-649 PASS) -- so their contribution lands in the **argmin-relevant deviation**
term of `StructuredCuriosity.compute_score_bias` rather than only the argmin-inert uniform
offset. And resolve the **open design decision** the ARC-065 entry flags: how the shared
`+/-curiosity_bias_scale` argmin-relevant budget is split once all three sub-flavours compete
for the same deviation term.

Prerequisite already landed (2026-07-21, session `silly-hellman-f0808b`): `compute_score_bias`
decomposes the accumulated bias into an argmin-inert uniform offset (`total.mean()`) and an
argmin-relevant per-candidate deviation, clamping each separately. Contracts:
`ree-v3/tests/contracts/test_mech_314_curiosity_clamp_ordering.py` (S1-S5).

## 2. The load-bearing finding this session discovered (refines the chip's framing)

**314a's genuine per-candidate source was ALREADY wired into the agent; 314b's is NOT, and
314c's does not exist yet.** This is the asymmetry the chip's "same treatment 314a got"
framing under-stated:

- **314a (novelty)** reads `e2.world_forward(z0, a_i)` -> `[K, world_dim]` per-candidate
  predicted next-state (the proposer/world model, already live in the agent via
  `_curiosity_candidate_summaries`). Genuinely per-candidate today.

- **314b (uncertainty)** -- the honest genuine per-candidate source is the SD-063
  `E2WorldUncertaintyHead.predictive_variance(z_world, action) -> [batch]` head
  (`ree-v3/ree_core/predictors/e2_world_uncertainty.py`), the V3-EXQ-712 winner
  (`precision_error_corr` 0.379, a genuine per-point error signal the global running-variance
  EMA structurally cannot carry). **But that head is defined + config-registered
  (`use_e2_world_uncertainty`, `e2_world_uncertainty_hidden_dim`, `e2_world_uncertainty_lr`)
  and NOT instantiated in `agent.py` -- it is used only from experiment scripts.** It also
  must be TRAINED (phased P0 encoder warmup -> P1 frozen-encoder pinball -> P2 eval) before
  its per-candidate variance is meaningful; an untrained head yields a near-uniform spread
  (the MECH-353 / V3-EXQ-642 vacuous-comparison lesson). This is corroborated by MECH-482's
  own precondition text in `claims.yaml`: *"MECH-314b is currently a global scalar per the
  existing curiosity intake -- not yet built in V3."*

- **314c (learning-progress)** -- there is **no** live per-candidate learning-progress
  source. The Phase-1 signal is a global EMA of `|PE_t - PE_{t-K}|`. A genuine per-candidate
  LP requires per-candidate / per-region tracking of reducible uncertainty over time -- which
  is precisely **MECH-482 (epistemic_deficit accumulator)**, whose own registered
  non-degeneracy precondition is a target-bound (not global-scalar) per-candidate uncertainty
  substrate. Manufacturing a per-candidate 314c shape from data that does not carry genuine
  learning-progress information would recreate the exact 604a / 624a / 614d / 640a
  vacuous-channel failure class this codebase is scarred by.

**Consequence:** the fully-honest deliverable is the per-candidate **architectural slot**
(the literal title of ARC-065: "Behavioral-diversity-generation architectural slot") plus the
resolved budget-split design decision, with the two genuine sources routed as follow-on
builds -- NOT a rushed manufacture of live 314b/314c signals in a headless session.

## 3. What landed (code, this session)

All changes are **bit-identical OFF** (default config reproduces Phase-1 exactly).

### 3a. Module -- `ree-v3/ree_core/policy/structured_curiosity.py`
`compute_score_bias` gains two optional per-candidate inputs:
`per_candidate_uncertainty: Optional[[K]]` (314b) and
`per_candidate_learning_progress: Optional[[K]]` (314c). When a vector is provided, the
sub-flavour contributes `total = total - weight * vector` (exactly as 314a already does with
`novelty`), so its **mean automatically flows to the argmin-inert offset (magnitude preserved:
"more total uncertainty -> more total bonus") and its deviation automatically flows to the
argmin-relevant per-candidate term** -- the existing offset/deviation decomposition needs no
new hand-splitting. When a vector is `None`, the Phase-1 uniform broadcast
(`weight * scalar * ones(K)`, pure offset) is used unchanged. New per-sub-flavour deviation
diagnostics (`_last_novelty_dev_range`, `_last_uncertainty_dev_range`, `_last_lp_dev_range`)
expose which flavour carries the argmin-relevant span, so cross-flavour domination is
observable at readiness rather than discovered in a null result.

### 3b. Config -- `ree-v3/ree_core/utils/config.py`
`curiosity_uncertainty_source: {"broadcast","e2_predictive_variance"}` (default `"broadcast"`)
and `curiosity_learning_progress_source: {"broadcast","epistemic_deficit"}` (default
`"broadcast"`). Both defaults reproduce Phase-1 exactly.

### 3c. Agent -- `ree-v3/ree_core/agent.py`
- Instantiates `self.e2_world_uncertainty` (SD-063 head) when `config.use_e2_world_uncertainty`
  is set (guarded, default off -> `None`).
- At the `compute_score_bias` call site, when
  `curiosity_uncertainty_source == "e2_predictive_variance"` AND the head is present, builds
  `head.predictive_variance(z0_K, actions_K) -> [K]` (same per-candidate `(z0, a_i)` pairs the
  314a e2_world_forward summaries use) and passes it as `per_candidate_uncertainty`. Otherwise
  `None` (broadcast). The `epistemic_deficit` 314c path is guarded to `None` (falls back to
  broadcast) until MECH-482 lands.

### 3d. Contracts -- `ree-v3/tests/contracts/test_mech_314_curiosity_clamp_ordering.py`
Existing S1-S5 unchanged (not weakened). New cases: a genuine per-candidate 314b/314c vector
lands purely in the deviation (mean-preserving), combines additively with 314a ordering, the
shared deviation clamp still bounds total selection-relevant influence at `bias_scale`, the
per-flavour diagnostics report honestly, and `None` inputs are bit-identical to Phase-1.

## 4. The resolved design decision (budget split)

> **CROSS-REFERENCE (added 2026-08-22, ratification status unchanged -- see the Review
> outcome section at the end of this file, which remains the authoritative record).** The
> alternatives analysis this section was routed to is
> [`curiosity_budget_split_eligibility_design_2026-08-22.md`](curiosity_budget_split_eligibility_design_2026-08-22.md)
> (REE_assembly `2f6d2033a6`). It finds rationale points 1 and 2 intact -- point 2 becomes a
> binding constraint on every candidate design -- and rationale point 3 refuted by
> measurement. The resolution below is UNEDITED and is the baseline those alternatives are
> measured against.

**RESOLUTION: keep the single shared deviation clamp; relative allocation among 314a/314b/314c
is governed by the per-flavour WEIGHTS (Q-043/Q-044), with `curiosity_bias_scale` as the
whole-channel authority knob. REJECT per-sub-flavour deviation clamps.**

Rationale:
1. The clamp exists to bound curiosity's TOTAL selection-relevant influence relative to the
   rest of the score-bias chain (dACC / lateral_pfc / ofc / mech295). That budget is a
   property of curiosity-as-a-channel, not of individual sub-flavours.
2. Per-sub-flavour deviation clamps would (a) require an arbitrary per-flavour allocation, and
   (b) fail to bound the total -- three flavours each clamped at the rail sum to 3x the rail,
   re-opening the very domination the clamp exists to prevent.
3. What the shared clamp does NOT do is stop one flavour dominating the others WITHIN the
   budget. That is a WEIGHT-calibration question (Q-043/Q-044), not a clamp question -- the
   weights already control relative contribution, and raising `bias_scale` is available if the
   whole channel needs more authority.
4. The residual hazard the ARC-065 constraint text named -- "it will ship still able to rail
   the ranking, the same defect one layer down" (a huge-range 314b compressing 314a's ordering
   inside the shared clamp) -- is caught by the **readiness gate**, not by a hard per-flavour
   clamp: `last_clamp_saturated_frac` rises toward its `(K-1)/K` ceiling and the new
   per-flavour `*_dev_range` diagnostics show WHICH flavour is dominating. This matches the
   codebase's standing philosophy (observe-and-gate-at-readiness, per the clamp_ordering
   constraint's own requirement) rather than adding arbitrary hard rails.

## 5. Readiness gate (binding, per the ARC-065 clamp_ordering_constraint_2026_07_21)

Before scoring any curiosity-dependent DV with 314b or 314c per-candidate ON, an experiment
MUST assert (from `StructuredCuriosity.get_state()`):
- `last_bias_range > 0` (the channel is not flat), AND
- `last_clamp_saturated_frac` strictly below its `(K-1)/K` ceiling (the ranking is not
  fully compressed), AND
- the relevant per-flavour `last_uncertainty_dev_range` / `last_lp_dev_range` `> 0` (the
  sub-flavour under test actually carries argmin-relevant span -- not a vacuous channel).

This is the guard against the 604a / 624a / 614d / 640a failure class recurring one layer down.

## 6. Follow-on work routed (NOT done this session)

1. **SD-063 head training loop wired into the agent** so 314b's `e2_predictive_variance` source
   is genuinely LIVE (instantiation landed this session; **phased P0->P1->P2 training is not**).
   Until trained, do NOT enable `curiosity_uncertainty_source=e2_predictive_variance` for a
   scored run -- an untrained head's predictive_variance is near-uniform and the readiness gate
   in section 5 will (correctly) refuse it. This is the actual keystone that lights 314b up and
   makes Q-044's discriminative design viable; it is a substantial build (training readiness +
   validation experiment) and belongs in its own chip.
2. **MECH-482 (epistemic_deficit accumulator)** as the genuine per-candidate 314c source. Its
   own precondition (per-candidate uncertainty substrate) is partially met by the 314b slot
   landed here; the accumulator itself is a separate substrate build.
3. **Validation experiment** for the 314b live path (feature ON vs OFF, same seeds; acceptance:
   `last_uncertainty_dev_range > 0` at readiness AND a non-zero per-candidate selection delta),
   queued via `/queue-experiment` once (1) is trained.

## 7. Governance posture (why no flag flips)

This landing makes 314b/314c per-candidate-**capable** but does not make either sub-flavour
LIVE (314b needs the trained head; 314c needs MECH-482). Therefore **no** `status`,
`v3_pending`, `pending_retest_after_substrate`, or confidence field was changed on MECH-314b,
MECH-314c, Q-044, or MECH-482. Only `implementation_note`s recording the slot landing were
added. Flipping the retest flags is governance work for after the source is live + validated.


---

## Review outcome (2026-08-22, session pending-task-009a3a, reached via IGW-20260822-154)

This doc sat `AWAITING USER REVIEW` for 14 days. It was surfaced during a plan reconcile of
`orienting_epistemic_deficit_v3:ORNT-2`, which found this doc's unreviewed status to be one of
the two live gates on MECH-482. The user reviewed it via AskUserQuestion. The outcome is
**split** -- do not read the two halves as one verdict.

### Section 4 (budget split): NOT RATIFIED -- re-opened

The user declined to ratify the shared-clamp + weights resolution, verbatim:

> "this is exactly where the constitutional eligibility and more complex biology similar basal
> ganglia set up might have a better answer than a single test. perhaps more consideration as
> to how this could be robustly done is needed"

The objection targets rationale points **3 and 4**, not point 2: static per-flavour weights plus
an observe-at-readiness gate is a "single test", where the biology uses a structured,
state-dependent **eligibility** layer. Point 2's total-bound argument (three flavours each
clamped at the rail sum to 3x the rail) is untouched by this and any alternative must still
answer it.

**Section 4's text is deliberately left in place, unedited, as the BASELINE** the alternatives
are measured against -- it is not withdrawn, it is unratified. Routed to
`chip-20260822-curiosity-budget-split-eligibility` as a **design pass, not a build**
(DELIVERED 2026-08-22: `evidence/planning/curiosity_budget_split_eligibility_design_2026-08-22.md`,
REE_assembly `2f6d2033a6` -- recommends Design B, per-flavour commensuration under the single
existing clamp, build sequenced behind the SD-063 keystone and gated on a named probe): at least
two candidate designs, each answering rationale points 1-4, each with a named falsifier
distinguishing it from static weights (the 604a / 624a / 614d / 640a vacuous-channel class
applies here too -- a mechanism indistinguishable from the baseline is not an improvement).
Registry anchors for the direction: **ARC-008** (commitment eligibility gated by tau/rho/phi;
status provisional, only a coarse BINARY proxy built, the eligibility matrix M_phi is NOT) and
**MECH-062** (E3 tri-loop gating as the pre-commit eligibility layer; status candidate, its own
notes state this over-states what is built). Both being partly-unbuilt is itself a finding the
design pass must size: "use eligibility" may be gated on first building an eligibility layer.

### Follow-on item 1 (SD-063 head training): AUTHORISED

Chipped as `chip-20260822-sd063-head-training-keystone` (/implement-substrate). This is the
keystone that makes MECH-482's non-degeneracy precondition satisfiable, and it was owned by no
chip and no closure node before today. It is **independent of the section 4 question** --
training the head and measuring `last_uncertainty_dev_range` does not depend on how the budget
is eventually allocated -- so it proceeds while the budget split is reconsidered.

Follow-on items 2 (MECH-482 accumulator) and 3 (the ON-vs-OFF validation experiment) remain
routed as written and were NOT authorised by this review.

### Governance posture unchanged

Section 7 still holds: no `status`, `v3_pending`, `pending_retest_after_substrate` or confidence
field was flipped on MECH-314b, MECH-314c, Q-044 or MECH-482 by this review. Flag flips remain
governance work for after the source is live AND validated.
