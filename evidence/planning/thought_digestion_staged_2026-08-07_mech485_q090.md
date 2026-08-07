# STAGED (not applied): `/thought-digestion` drafts for MECH-485 + Q-090

**Status: AWAITING USER REVIEW. Nothing in this file has been written to `claims.yaml`.**

- Drafted: 2026-08-07T18:38:40Z
- Session: `metaworker-chip-20260807-thoughtdigest-mech485-q090` (headless dispatch chip,
  `[chip_ref: chip-20260807-thoughtdigest-mech485-q090]`)
- Base: `REE_assembly` `8b00b6244e`
- Mode: **unattended / draft-only**, per `.claude/skills/thought-digestion/SKILL.md`
  "Unattended / overnight mode" step 3 and the skill's standing rule that the falsification
  condition and disposition are always the user's call. There is no live user in a headless
  chip, so the drafts are staged rather than applied.

**Deviation from the skill, stated plainly:** the skill says to stage to an *untracked*
scratchpad. That is correct for an interactive overnight loop where the user returns to the
same session. It is wrong for a headless worker -- an untracked file in a throwaway worktree
is orphaned the moment the process exits. So this is staged to a tracked `evidence/planning/`
path and committed pathspec-limited, which is covered by this session's active TASK_CLAIMS
entry (so the runner heartbeat autostash cannot revert it). It touches nothing else.

**To apply:** read the two blocks below, edit as you see fit, paste into `claims.yaml`
(re-reading each claim's full block immediately before editing), then
`python scripts/build_claims_json.py` from `REE_assembly/` and confirm the
missing-`what_would_answer` warning count drops by **exactly 2**. Delete this file when done.

---

## GOVERNANCE / SUBSTRATE CALLOUT (read first, separate from the drafts)

Surfaced by this pass's currency verification, **not acted on**, and not part of either
falsifier. It bears on `SD-059`/`MECH-358` (the escape-affordance linker's own claims), not
on MECH-485.

**`predicted_harm_delta` is computed and never read.**
`ree-v3/ree_core/pfc/e2_escape_affordance_linker.py` declares it (line 111) and assigns it
(line 665, `out.predicted_harm_delta = self.predict_head("harm_delta", a, state_vec)`). A
repo-wide grep over `ree-v3/**/*.py` at `8b00b6244e` finds **exactly those two lines and no
others** -- no consumer in `ree_core/`, no experiment driver, no test, no diagnostic.

Two readings, and this pass did not adjudicate between them:
- **Benign** -- the module's own docstring describes the viability readouts as *exposed* for
  optional downstream consumption ("the relief/safety affect heads ... can optionally
  consume"), so an unconsumed readout may be exactly as designed.
- **Worth checking** -- zero consumers *including zero tests* means the head has never been
  validated against anything, so it is a trained output nothing has ever checked for
  correctness. If MECH-485 is ever built, this is the most likely place its
  `predicted_harm_magnitude` would come from, and it would be inherited unverified.

Recommended: a small `/failure-autopsy`-adjacent or substrate check, **not** a digestion
action. Flagged here so it is not lost; deliberately not chipped, since it is a judgment call
about an existing claim's substrate rather than an actionable build.

---

## Currency verification performed this pass

Everything below was re-checked against live state rather than trusted from the claims' own
notes (Step 4's standing "verify, not assume" instruction). Results:

| Thing checked | Source note said | Verified 2026-08-07 | Δ |
|---|---|---|---|
| `MECH-439` conversion ceiling | `ceiling_decision: exhausted` | still `exhausted`, `status: candidate`, `epistemic_category: standard` | unchanged |
| `INV-012` Leg 3 | "added later same day (`c7530416d7`)" | **landed**, full house-style Leg 3 present in `INV-012.what_would_answer`, `depends_on` includes MECH-485 | confirmed |
| MECH-138 cross-ref into MECH-090/141 | "not attempted this pass" | **landed since** -- `REE_assembly` `39e445e49e` (sibling chip `chip-20260807-mech138-crossref`, resolved `done`) | resolved |
| Leg-3 retention mechanism registration | "deliberately NOT registered, gated on lit-pull" | still unregistered; sibling chip `chip-20260807-litpull-uncommitted-retention` is **still `open`** | unchanged |
| `MECH-482`/`MECH-483` build status | "genuinely not built" | `epistemic_deficit` has **zero hits** anywhere in `ree-v3/ree_core/`; both still `candidate/v3_pending/substrate_conditional` | confirmed unbuilt |
| `MECH-138` cancel-window in substrate | (not previously checked) | `cancel_window` / `veto_window` / `cancel_open`: **zero hits** in `ree_core/` | newly confirmed unbuilt |
| `SD-033e`/`MECH-264` `cfv_now` | "transient scalar, overwritten every tick" | confirmed -- `agent.py:1227` `_fp_last_cfv_now: float = 0.0`, recomputed per maintenance tick (`agent.py:5665`), reset at `3174`; consumed once as `max(0, cfv_now - cfv_at_entry)` release pressure | confirmed |
| `SD-039` retrieval level | "measured-open, V3-EXQ-889 non-degeneracy finding" | still `candidate/v3_pending`, `substrate_conditional` | unchanged |
| E3 discards non-winning candidates | "`select()` discards every non-winning candidate" | confirmed -- no retention/persistence of losing candidates in `e3_selector.py`; the one `retain` is `MECH-463` per-candidate channel-bias tensors held *within* the tick | confirmed |
| Predicted-harm magnitude in substrate | (not previously checked) | partial -- `predicted_harm_delta` exists but is **never consumed** (see callout above); `harm_magnitude` in `agent.py:9303` is *actual* post-hoc harm, not predicted | newly found |

**Net:** every substrate precondition either half-exists as a dead readout or does not exist at
all. Both claims are correctly `substrate_conditional`; neither is anywhere near testable.
No category change is proposed for either, and no `EXP-####` proposal is minted (the test is
not runnable -- minting one would be a proposal nothing can act on).

---

## DRAFT 1 -- `MECH-485`

**Disposition recommended: (c) substrate-blocked.** Keep `epistemic_category:
substrate_conditional` (already set -- no change). No proposal minted. Add
`what_would_answer` only.

```yaml
  what_would_answer: |
    Answered by ABLATING THE FAN-OUT, once the substrate exists: does routing
    one magnitude+confidence signal to three regime-specific consumers do
    anything a single graded response would not?

    Two separable assertions, which can fail independently:
    (A) SHARED SOURCE -- the three legs are driven by the SAME predicted
    magnitude + confidence pair, not by three independently-computed triggers
    that merely co-vary. This is Addendum 5's synthesis; Addendum 2's own
    earlier reading (three "functionally distinct consumers" of shared
    representational substrate) is the competing hypothesis, not a strawman.
    (B) DIFFERENTIATED RESPONSE -- the fan-out is genuinely regime-gated, not
    one uniform response whose intensity happens to scale with magnitude.

    NON-DEGENERACY PRECONDITION (five parts, ALL currently unmet as of
    2026-08-07 -- this claim is untestable by construction, not merely
    unfavored):
    (1) Leg 0 cleared -- E3 must select among genuinely graded, differentiated
    candidates, or there is nothing for a magnitude to be computed OVER. See
    INV-012's own what_would_answer LEG 0 for the full statement and the
    MECH-439 `ceiling_decision: exhausted` evidence; do NOT re-derive it here.
    (2) The magnitude half must exist AND be consumed. Verified 2026-08-07 at
    ree-v3 substrate: `predicted_harm_delta`
    (ree_core/pfc/e2_escape_affordance_linker.py) is the nearest existing
    forward-rollout predicted-harm quantity, but a repo-wide grep finds one
    write site and ZERO read sites -- it is produced and discarded. A
    magnitude nothing consumes cannot gate anything.
    (3) The confidence half must exist. `epistemic_deficit` has zero hits
    anywhere in ree_core/ (verified 2026-08-07); MECH-482/MECH-483 are both
    candidate/v3_pending/substrate_conditional.
    (4) The leg-1 target pathways must accept a predicted-harm input.
    BetaGate (ree_core/heartbeat/beta_gate.py) exists but takes no harm or
    predicted-harm term in any method signature; MECH-138's cancel-window has
    no substrate presence at all (`cancel_window`/`veto_window`: zero hits).
    So leg 1 is currently a claim about a wire that does not exist, between
    an endpoint that exists and one that does not.
    (5) Leg 3's retention mechanism must exist. It does not, in any form --
    see INV-012's LEG 3 for the full statement of what is missing and why it
    is deliberately unregistered pending a dedicated lit-pull; do NOT
    re-derive it here.

    PLUS one non-degeneracy guard specific to THIS claim rather than
    inherited: (6) MAGNITUDE AND CONFIDENCE MUST BE MEASURABLY DISSOCIABLE in
    the test distribution. The claim asserts a two-dimensional gate
    (magnitude x confidence) fanning into three regimes. If confidence is in
    practice a monotone function of magnitude -- confidently-predicted harms
    are also large ones -- the gate collapses to one dimension, only two
    regimes are ever occupied, and leg 2 (orient/survey) is never entered.
    A run under those conditions would report "no three-way structure" for a
    reason that has nothing to do with whether the claim is true. Require a
    reported joint distribution over (magnitude, confidence) with populated
    off-diagonal cells -- specifically high-magnitude/low-confidence, which
    is the ONLY cell that distinguishes leg 2 from leg 1 -- before any
    verdict is read.

    CONFIRMING signature (all three, not any one):
    (i) FAN-OUT IS LOAD-BEARING -- collapsing the three consumers into a
    single graded response (interrupt probability scaled by magnitude, no
    orient/survey regime, no retention) degrades performance on at least two
    of the three legs' own outcome metrics relative to the intact pipeline.
    (ii) DOUBLE DISSOCIATION OF CUT-POINTS -- sweeping the interrupt
    threshold moves the leg-1/leg-3 boundary WITHOUT moving the leg-2
    boundary, and sweeping the epistemic_deficit threshold moves the leg-2
    boundary WITHOUT moving the leg-1/leg-3 boundary. This is what separates
    "one signal, independently-placed cut-points" from "three signals": three
    independent triggers would not show each sweep confined to its own
    boundary.
    (iii) SHARED SOURCE IS SUFFICIENT -- substituting a leg-specific,
    independently-computed trigger for the shared signal in any single leg
    yields no improvement over the shared signal on that leg's own metric.

    FALSIFYING, in three distinct ways with three distinct remedies:
    -- THREE-SIGNAL reading: the shared signal underperforms a leg-specific
    trigger in at least one leg by a margin that survives the other legs
    being held intact. Then the legs need different COMPUTATIONS, not
    different thresholds on one, and Addendum 2's pre-synthesis reading was
    right. Remedy: demote MECH-485 from a unity claim to "three mechanisms
    sharing E2/E3 forward-prediction substrate" and keep each leg. NOTE this
    is a partial falsification -- MECH-485 can fail AS A UNITY CLAIM while
    every individual leg survives, and that outcome must not be recorded as
    refuting the legs.
    -- DECORATIVE FAN-OUT: a single graded response reproduces the intact
    pipeline's benefit on all three legs' metrics. Then threshold-gating is
    a description of the response curve, not a mechanism, and (B) is false
    even if (A) holds. Remedy: retire the three-consumer structure, keep the
    shared-signal claim.
    -- OVER-CONSTRAINED SCALE: no placement of the two cut-points leaves all
    three legs simultaneously non-degenerate -- every setting at which leg 1
    fires usefully starves leg 3 of retainable candidates, or vice versa.
    This is Q-090's independent-criterion reading generalized to the whole
    pipeline, and it falsifies the "one scale partitioned at two cut-points"
    architecture specifically. Remedy: give the legs independent admission
    criteria, which is exactly what Q-090 asks about for leg 3.

    ORDER OF ATTACK, if this is ever built: precondition (2) is the cheapest
    and is independently useful -- wiring an existing-but-unconsumed
    `predicted_harm_delta` to any consumer at all is a smaller step than
    MECH-482/483, and its result is informative regardless of MECH-485's
    fate. Do not treat the whole pipeline as one indivisible build.
```

### Also proposed for `MECH-485` (separate from the falsifier -- your call)

1. **Add `MECH-094` and `MECH-322` to `depends_on`.** `INV-012` Leg 3 names both as
   load-bearing for the confabulation guard on the retention leg; `MECH-485`'s own `notes`
   discuss the confabulation risk in prose but its `depends_on` does not carry either.
   Suggested comments: `MECH-094  # imagination/reality write gate -- leg 3's retained
   content must stay provenance-distinguishable` and `MECH-322  # the one bounded, audited
   exception through MECH-094 -- template shape any leg-3 retention must follow`.
2. **Not proposed: a reverse `depends_on` to `INV-012`.** `INV-012` already depends on
   `MECH-485`; adding the reverse would make the graph cyclic. The falsifier cross-references
   it in text instead, which is the skill's stated preference.

---

## DRAFT 2 -- `Q-090`

**Disposition recommended: (c) substrate-blocked.** Keep `epistemic_category:
substrate_conditional` (already set -- no change). No proposal minted. Add
`what_would_answer` only.

**Extraction note:** this is drafted by extracting the dissociable-prediction sketch already
present in `Q-090`'s own `notes:` and in the raw thought's Addendum 5, and converting it into
the house structure -- per the skill's "extract before inventing". The 2x2 factorial shape,
the decorrelation precondition, and the third "both, at different levels" answer are the only
additions; the two competing readings and their signature predictions are the user's own.

```yaml
  what_would_answer: |
    Answered by a 2x2 FACTORIAL over (predicted-harm magnitude) x (goal-match),
    measuring which alternatives actually get retained. This is a question, not
    an assertion, so BOTH readings have confirming signatures -- the failure
    mode here is a vacuous test, not a wrong answer.

    THE TWO READINGS, and why they are dissociable (extracted from this claim's
    own notes and the raw thought's Addendum 5, not re-derived):
    -- SAME-SCALE: leg 3's admission is a second, lower cut-point on the same
    predicted-harm magnitude scale the interrupt threshold sits on. Predicts
    retained alternatives cluster just below the interrupt cut-point;
    retention probability is monotone in magnitude; goal-match adds no
    independent variance once magnitude is in the model.
    -- INDEPENDENT-CRITERION: retention tracks goal-relevance instead, via the
    MECH-292/293 cue system -- specifically SD-039's `goal_match`, the
    cue-to-trace match score between a live z_goal/context cue and a stored
    goal-snapshot payload. Predicts dissociation cases the same-scale reading
    cannot produce: low-magnitude/high-goal-match alternatives RETAINED, and
    high-magnitude/goal-irrelevant alternatives NOT retained.

    NON-DEGENERACY PRECONDITION, in two parts. The first is inherited; the
    second is the one that actually decides whether this question is askable.
    (1) INHERITED -- everything MECH-485's own what_would_answer requires
    (Leg 0 cleared, magnitude consumed, confidence term exists, leg-1 pathways
    wired, retention mechanism exists). Do NOT re-derive it here; see
    MECH-485. As of 2026-08-07 all five are unmet, so this question is not
    askable at all yet. Additionally SD-039's own retrieval/query level is
    still measured-open (z_goal cue collapse across goal-epochs, V3-EXQ-889,
    2026-08-03) -- if `goal_match` is not a live, discriminating quantity,
    the independent-criterion arm has no measurable predictor and the test
    silently degenerates into "magnitude explains everything", which LOOKS
    like a clean same-scale answer and is not one.
    (2) SPECIFIC AND DECISIVE -- MAGNITUDE AND GOAL-MATCH MUST BE
    MEASURABLY DECORRELATED IN THE TEST DISTRIBUTION. If harmful alternatives
    happen to also be goal-irrelevant in the environment used, the two
    readings make IDENTICAL predictions and no outcome distinguishes them,
    however clean the statistics look. The test therefore requires a probe
    set deliberately populated in the OFF-DIAGONAL cells --
    (low-magnitude, high-goal-match) and (high-magnitude, low-goal-match) --
    with those two cells reported by count, not merely assumed present. A run
    whose off-diagonal cells are empty or near-empty is VACUOUS and must be
    reported as such rather than scored. This is the single most likely way
    for this question to be answered wrongly-but-convincingly.

    ANSWERED IN FAVOUR OF SAME-SCALE if: retention is well predicted by
    magnitude alone; adding `goal_match` explains no significant additional
    variance; the off-diagonal cells behave as magnitude alone predicts
    (low-magnitude/high-goal-match NOT retained, high-magnitude/goal-
    irrelevant RETAINED); and the fitted retention cut-point sits below the
    interrupt cut-point on the same scale, the two moving together when that
    scale is rescaled.

    ANSWERED IN FAVOUR OF INDEPENDENT-CRITERION if: `goal_match` explains
    retention variance over and above magnitude; the off-diagonal cells
    dissociate in the direction the reading predicts (low-magnitude/high-goal-
    match RETAINED, high-magnitude/goal-irrelevant NOT); and moving the
    interrupt threshold shifts the interrupt boundary while leaving the
    retention boundary where it was.

    ANSWERED "BOTH, AT DIFFERENT LEVELS" if magnitude predicts ADMISSION
    (whether an alternative is retained at all) while `goal_match` predicts
    PERSISTENCE (how long it survives, or whether it is consolidated rather
    than decayed). This is a real third outcome the binary framing hides, and
    it is named here so the test is not forced into a false dichotomy. It
    would mean leg 3 has a two-stage criterion and Q-090's own framing needs
    revising rather than answering.

    THE QUESTION IS MALFORMED (report as such, do not force an answer) if:
    neither predictor explains retention above chance once the substrate
    exists -- retention is driven by something neither reading names, e.g.
    recency or capacity pressure, which is an informative finding about leg 3
    and a reframe of this question, not a null result. OR if the off-diagonal
    cells cannot be populated in ANY available REE environment, making
    precondition (2) structurally unachievable -- in which case the
    admission criterion genuinely is a design stipulation after all, contrary
    to the user's framing of it as empirically resolvable, and that reframe
    should be recorded here explicitly rather than treated as a failure to
    answer.
```

### Also proposed for `Q-090` (separate from the falsifier -- your call)

1. **Add `SD-039` to `depends_on`.** `goal_match` is SD-039's own quantity (the cue-to-trace
   match score over its dual-trace anchor goal-snapshot payload), and SD-039's measured-open
   retrieval level is a hard precondition on the independent-criterion arm -- but `Q-090`
   currently lists only `MECH-485`, `MECH-292`, `MECH-293`. Suggested comment:
   `SD-039  # dual-trace anchor payload -- supplies goal_match, the independent-criterion
   arm's predictor; its own retrieval level is measured-open (V3-EXQ-889)`.
2. **Not proposed: adding `MECH-439`.** Its precondition reaches Q-090 through MECH-485
   already; a direct edge would duplicate rather than add.

---

## What was NOT done, and why

- **Nothing was written to `claims.yaml`.** Headless chip, no user to approve. This is the
  skill's own rule, not caution on this session's part.
- **No `EXP-####` proposal minted in `manual_proposals.v1.json`.** Correct disposition for
  both claims is (c) substrate-blocked, and (c) explicitly does not mint. Every one of
  MECH-485's five substrate preconditions is unmet, so a proposal would describe a run
  nothing can execute.
- **`build_claims_json.py` was not run.** It regenerates `docs/assets/data/claims.json`, and
  with no `claims.yaml` edit applied there is nothing to regenerate; running it would dirty a
  tracked artifact for no gain. Run it after applying the drafts, and expect the
  missing-`what_would_answer` count to drop by exactly 2.
- **The `predicted_harm_delta` dead-readout finding was not acted on** -- see the callout at
  the top. It is a live judgment call about `SD-059`/`MECH-358`'s substrate, which the skill's
  "fix things as we go" boundary explicitly reserves for the user.
