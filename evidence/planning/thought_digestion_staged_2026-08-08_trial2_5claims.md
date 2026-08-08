# STAGED (not applied): `/thought-digestion` drafts (trial 2) for INV-004, SD-033e, MECH-264, INV-073, MECH-138

**Status: AWAITING USER REVIEW. Nothing in this file has been written to `claims.yaml`.**

- Drafted: 2026-08-08T06:30:19Z (wave completed; drafts below are the agents' verbatim output, lightly reformatted)
- Session: `metaworker-chip-20260808-thoughtdigestion-trial2-5` (headless dispatch chip,
  `[chip_ref: chip-20260808-thoughtdigestion-trial2-5]`)
- Base: `REE_assembly` `2a256cef32`
- Mode: **unattended / draft-only**, per `.claude/skills/thought-digestion/SKILL.md`
  "Unattended / overnight mode". Wave size = 5, one wave, no self-pacing. Write policy:
  **draft-only-stage-for-review** -- nothing minted to `claims.yaml` or
  `evidence/planning/manual_proposals.v1.json`.

**Deviation from the skill, stated plainly:** the skill's overnight-mode step 2 says to stage
drafts to an *untracked* scratchpad file. That is correct for an interactive overnight `/loop`
where the same live user returns to the same session. It is WRONG for a headless `claude -p`
worker in a throwaway git worktree: an untracked file there is orphaned the instant the process
exits, and the worktree is GC-eligible the moment this chip resolves with a clean tree
(`scripts/hygiene_routine_tick.py`'s `_metaworker_worktree_gc_findings` flags it; a dispatcher
then removes it). That is exactly what destroyed TRIAL 1's review artifact
(`chip-20260807-thoughtdigestion-trial-5`) -- an untracked file at the worktree root, reaped
before the user could read it, with only the governance flags and the structured resolution note
surviving. So this trial stages to a TRACKED `evidence/planning/` path, committed
pathspec-limited under this session's active TASK_CLAIMS entry (which also stops the
runner-heartbeat autostash from reverting it before commit). It touches nothing else. This
mirrors the proven pattern in `thought_digestion_staged_2026-08-07_mech485_q090.md`.

**To apply:** read each draft below, edit as you see fit, then for each claim re-read its FULL
current block in `claims.yaml` immediately before editing (concurrency -- other sessions write
here; note a MASSIVE governance regen was in flight at draft time, see the note at the very
bottom), insert the `what_would_answer` (and `epistemic_category` where the draft adds one), then
from `REE_assembly/` run `python scripts/build_claims_json.py`. **Expected effect on the
missing-`what_would_answer` warning count: it will drop by EXACTLY the number of the five that are
`asked`-bucket claims.** Of these five, ONLY the two `asked`-bucket claims are counted by that
warning (the validator warns on `asked`/`open_question` claims only). INV-004, SD-033e, MECH-264,
INV-073, MECH-138 -- verify each one's `epistemic_stance` in `claims.json` before predicting the
delta: at draft time the two counted asked-bucket claims in the whole registry were Q-020 and
Q-090 (trial 1's, never applied), and **none of these five is currently in the asked bucket** (all
five are `believed`), so applying all five drafts should drop the missing-WWA *warning* count by
**0** while removing five genuine gaps that the warning does not track. Do NOT be alarmed by a
0-delta warning count -- confirm instead that each of the five `claims.yaml` blocks now carries a
`what_would_answer` (`grep -A1 "^  id: INV-004" ...` etc.). Delete this file once the drafts are
applied or explicitly rejected.

---

## GOVERNANCE FLAGS (read first, separate from the per-claim drafts)

### GFLAG-0011 (RAISED structurally this session) -- `stale_note`, claims SD-033e + MECH-264

**V3-EXQ-724 has already run; both claims' gating language reads as if it were pending.**
SD-033e's `implementation_note` (and MECH-264, which inherits it by cross-reference) states the
V3-narrow frontopolar de-commit lever's all-ON validation is "gated on V3-EXQ-724", reading as
pending-execution. But `v3_exq_724_competence_localization_diagnostic_20260709T211405Z_v3`
**ran 2026-07-09** with `outcome=FAIL`, `evidence_direction=non_contributory`, `claim_ids=[]` --
a competence-**localization** diagnostic (verdict `competence_deficit_diffuse`), NOT a frontopolar
validation. The all-ON de-commit contrast is therefore currently **degenerate** (the binding
constraint is the upstream MECH-457 competence floor, still open per 687a/819a/748a of
2026-07-30/31), not pending 724. **Nothing is mis-scored** (`non_contributory`, `claim_ids=[]`), so
this is a wording-currency correction, not a status/confidence change -- but the gating language in
both claims should be refreshed to: *"all-ON validation blocked -- V3-EXQ-724 (2026-07-09) returned
`competence_deficit_diffuse`, so the binding constraint is the MECH-457 competence floor (open per
687a/819a/748a), not the commit latch; a dedicated de-commit validation experiment is still owed
once the floor clears."* Raised as GFLAG-0011 (`governance_flags.v1.json`). Two accidental
duplicate raises (GFLAG-0012, GFLAG-0013) from a retry-on-push-rejection loop were **superseded**
in the same session; GFLAG-0011 is canonical.

### Recommended documentation-currency corrections (NOT raised as structural flags -- apply with the drafts)

These are `stale_note`-flavoured but low-value and best fixed when the drafts are applied, not
tracked as standalone governance flags:

- **INV-073 `notes` present-tense staleness.** The notes say "The cue_action_proj gradient path is
  severed (EXP-0155)" as a present-tense fact. It is now *toggleable*: SD-055's opt-in
  `use_differentiable_cem` (default False, bit-identical off) restores the gradient, and EXQ-568
  confirmed gradient-readiness (PASS, `non_contributory`). Suggested amendment: *"...is severed by
  default (EXP-0155); SD-055's opt-in `use_differentiable_cem` restores it, gradient-readiness
  confirmed EXQ-568, but the behavioural consequence is untested."*
- **MECH-138 `notes` substrate-gap pointer.** Append: *"Substrate status 2026-08-08:
  `cancel_window`/`veto_window`/`cancel_open` have zero hits in ree-v3/ree_core/; the only commit
  machinery is the beta latch (post-elevation) and the rung-6 hold-DURATION lever
  (`natural_commit_urgency.py`), both downstream of lock-in -- the pre-lock-in veto window is
  unbuilt."* Makes the `substrate_conditional` disposition self-documenting.
- **`depends_on` gaps** proposed per-claim below (INV-004 -> INV-027/INV-012/INV-019; MECH-264 ->
  MECH-163/MECH-257; INV-073 -> SD-055; SD-033e -> consider MECH-457 as blocked_on). All are
  "also proposed", the user's call, and none is applied here.

### Systemic finding (for the user to decide whether to spin off a chip -- NOT chipped by this session)

**Five of the highest-fan-in claims in the registry lacked a `what_would_answer` and had to be
digested from scratch this pass; the ripest-first scan surfaced that the *believed* bucket (585
claims missing WWA) is where nearly all the un-digested fan-in now sits, not the *asked* bucket
(2).** This is expected metabolic backlog, not a defect -- but it means the missing-WWA *warning
count* (which only tracks the 2 asked-bucket claims) badly understates the real digestion debt.
If the user wants the digestion campaign to keep chipping through the believed-bucket tail, that
is a durable multi-session effort worth its own tracked chip; this session deliberately did not
spawn one (headless, and the "chip a systemic finding" decision is the user's per the skill).

---

## Per-claim drafts

Each section: recommended disposition + one-line justification, a compressed currency check, the
full drafted `what_would_answer` (paste-ready YAML block-scalar, ASCII-only), and any also-proposed
non-falsifier suggestions. All five were drafted by read-only research agents; nothing was written,
committed, or minted to `claims.yaml`/`manual_proposals.v1.json`.

---

### DRAFT 1 -- `INV-004` (Post-commit consequence traces are persistent, not resettable)

**Disposition: (b) derivational** -- `epistemic_category: derivational`. A decision-theoretic
universal settled by argument from axiom INV-027 (the world is real and independent), not by
experiment; its own reference doc (`docs/invariants.md#inv-004`) and notes are accurate and were
verified. It is strictly a **fused** claim -- there is a genuine conformance leg ("does REE's
substrate actually realize non-resettable traces"), which is *already built* and testable-now as a
residue-field contract (`ree_core/residue/field.py` enforces accumulate-never-subtract +
`MIN_FLOOR = 1e-6`, refusing true zero) -- but that leg tests REE's *adherence*, not the
universal's *truth*, so it does not pull the claim off (b). No `EXP-####` minted.

**Currency check:** `invariants.md#inv-004` mechanism-agnosticism note present verbatim; INV-027
identified as the explicit derivational ground (`invariants.md:389`); residue-field conformance
enforced by construction (`field.py:1013-1016,1037-1040`); INV-006 (erasability) confirmed a
distinct sibling. `depends_on` is `[]` despite the doc naming parents -- a gap (see also-proposed).
No stale note, no category conflict.

```yaml
  epistemic_category: derivational
  what_would_answer: |
    DERIVATIONAL. This is a decision-theoretic universal, settled by argument
    from axiom, not by experiment. It does not get a runnable falsifier; it
    gets a proof obligation and a counterexample schema. (A SEPARATE,
    already-built conformance leg is named at the end -- it tests whether REE's
    substrate honours this invariant, NOT whether the invariant is true, and it
    is not this claim's falsifier.)

    PROOF OBLIGATION (what would establish the universal):
    Establish that for any agent embedded in a real, independent world
    (INV-027), the consequence trace of a COMMITTED action is not resettable.
    The argument:
    (1) INV-027 -- the world is real and has causal power independent of the
    agent's model. What actually happens in the world is a fact about the
    world's history, not a model-internal variable.
    (2) A "commit" (INV-012 commitment gate) is the RELEASE of an action whose
    effects register in the world and test the trajectory against it -- as
    opposed to rehearsal/simulation, which is model-internal and costless
    (INV-019 selection-compression boundary: rehearsal traversal and
    irreversible durable update must stay separated).
    (3) A "consequence trace" is a record faithful to what actually happened.
    To RESET such a trace is to return the agent-world system to a state as if
    the committed action had never occurred -- i.e. to unwrite a fact about the
    world's actual causal history.
    (4) By (1) the agent cannot unilaterally rewrite the world's history, and a
    record faithful to that history inherits its irreversibility. No purely
    model-internal operation (rollback, replay, checkpoint-restore, reset) can
    un-happen a world event. Therefore the trace is persistent, not resettable.
    QED-shape. The precise decision-theoretic content is: PERSISTENCE IS THE
    DEFINITIONAL FLIPSIDE OF COMMITMENT. An action is committed exactly insofar
    as its effects are not undoable; an action whose effects are resettable was
    never committed -- it was rehearsal.

    COUNTEREXAMPLE THAT WOULD FALSIFY (the universal fails if this setting is
    exhibited): a decision structure or world in which an action is GENUINELY
    committed -- released into a real, independent world, not rehearsed -- and
    yet its consequence trace is subsequently FULLY resettable: there exists an
    operation returning the agent-world system to a pre-commit state that is
    bit-identical, leaving NO trace in world, model, residue, or path-memory.
    Concrete shape: a perfect-undo / save-state-load-state world where committed
    effects can be un-happened with zero accumulated record. Note this is NOT a
    counterexample if the "world" is itself a simulation the agent controls
    (then the reset is a model operation and INV-027 does not hold for it), and
    NOT a counterexample if any residue/model-update/path-trace survives the
    reset (then the trace was persistent after all). A genuine counterexample
    requires BOTH real-world commitment AND complete, traceless reversibility --
    and the claim's content is precisely that no INV-027-embedded agent inhabits
    such a setting. If one is exhibited, INV-004 and INV-019's boundary fail
    together, because "commit" and "rehearse" would collapse.

    NON-DEGENERACY PRECONDITION (the claim must not be vacuously true):
    The universal is VACUOUS if "persistent"/"trace" is defined as "whatever
    survives" and "commit" as "an action that leaves a durable trace" -- then it
    reduces to "the part that persists, persists." Non-vacuity requires TWO
    independent criteria fixed in advance:
    (i) an independent criterion for COMMIT -- what counts as a released,
    world-registering action (INV-012's viability-gate release), distinct from
    rehearsal (INV-019); and
    (ii) an independent criterion for TRACE -- the faithful record of what
    happened (residue increment / durable model update / path memory), NOT
    defined as "the persistent bit."
    With both fixed independently, the assertion "for all committed actions the
    trace is not resettable" is CONTENTFUL and could in principle be false --
    save-state game-worlds and pure-simulation agents are conceivable settings
    where it WOULD be false. The claim's force is exactly that a genuinely
    INV-027-embedded agent is not one of those. That conceivability is what
    makes it non-vacuous.

    RELATIONSHIP TO INV-006 (do not conflate; they are separately falsifiable):
    INV-004 denies RESETTABILITY (no undo of the trace to a prior/null state);
    INV-006 denies ERASABILITY (no deletion of the trace) and positively asserts
    it can only be INTEGRATED/CONTEXTUALISED. A substrate that attenuates and
    re-weights a trace but never removes it satisfies BOTH; a substrate that
    could snap a trace back to its pre-commit value would violate INV-004 while
    a substrate that could delete it outright would violate INV-006. Keep the
    two obligations distinct.

    FUSED CONFORMANCE LEG (separate obligation, NOT this claim's falsifier;
    epistemic status of THIS leg is testable-now, not derivational): "REE's
    chosen realization actually satisfies the invariant." This IS checkable now
    as a substrate contract over ree-v3 ree_core/residue/field.py, which already
    enforces it by construction (verified 2026-08-08): accumulation is monotone
    (harm adds, never subtracts); multiplicative decay/discharge is floor-clamped
    at MIN_FLOOR = 1e-6 and refuses true zero (discharge_domain, field.py
    1013-1016, 1037-1040); SD-034 closure attenuates within a bounded domain
    (INV-006 contextualisation) without global erasure. A conformance FALSIFIER
    is: any code path that sets a live residue weight to exactly zero / below the
    floor, or a rollback path that restores a residue tensor to a pre-commit
    snapshot, would show REE VIOLATING the invariant it binds itself to. Because
    INV-004 is mechanism-agnostic (persistence may be realized via residue,
    hippocampal/path memory, or model updates), this conformance failure would
    indict REE's implementation, NOT the universal. Track it as a residue-field
    contract/lint, not as an INV-004 experiment.
```

**Also proposed (your call):**
1. Populate `depends_on` (currently `[]`): `INV-027  # world is real/independent -- the axiom this
   universal derives from`, `INV-012  # commitment gate -- the independent 'commit' criterion the
   non-degeneracy precondition needs`, `INV-019  # selection-compression boundary -- co-falsified;
   if commit/rehearse collapse, both fail`. Do NOT add INV-006 (sibling axiom, neither derives from
   the other -- cross-referenced in text instead).
2. Add `epistemic_category: derivational` (absent today) alongside the `what_would_answer`.

---

### DRAFT 2 -- `SD-033e` (Frontopolar-analog parallel-goal deliberation substrate)

**Disposition: (c) substrate-blocked** -- `epistemic_category: substrate_conditional`, with the
V3-narrow slice noted as **built-but-validation-gated**. The full learned MECH-264/MECH-265
substrate is never-exercised (MECH-163 multi-step planning and a K>=2-goal env both genuinely
absent); the already-landed V3-narrow geometric de-commit lever cannot be validated all-ON because
V3-EXQ-724 (ran 2026-07-09) returned a *diffuse competence deficit*, proving the binding constraint
is the upstream MECH-457 competence floor, not the commit latch the lever releases -- so the all-ON
contrast is currently degenerate, not merely un-run. No proposal minted (unrunnable).

**Currency check (verified against ree-v3 HEAD):** V3-narrow lever CONFIRMED present
(`ree_core/utils/config.py:3855,3860` `use_frontopolar_decommit`/`frontopolar_gain`;
`frontopolar_analog.py:323` geometric `compute_counterfactual_value`; release pressure
`agent.py:2984`->`:5658`). Learned head `use_frontopolar_analog` untouched (raises
`NotImplementedError`). **V3-EXQ-724 RAN 2026-07-09** (`competence_deficit_diffuse`,
`non_contributory`, `claim_ids=[]`; all-ON agent forages below the 1.0 floor 0/3 seeds while a
greedy oracle clears it at 6.05 -- env achievable, agent is the deficit). **No frontopolar all-ON
validation manifest exists anywhere in evidence** (the only `*decommit` runs are SD-034/MECH-342, a
different lever). MECH-457 floor still open (687a/819a/748a). K>=2-goal env absent. -> **See
GFLAG-0011.**

```yaml
  what_would_answer: |
    TWO FACES, and the split IS the falsifier. Face 1 is the already-landed
    V3-narrow geometric de-commit lever (testable in principle, currently
    blocked by measured evidence). Face 2 is the full learned V4 substrate
    (untestable by construction today). They fail independently and carry
    different remedies.

    ============================================================
    FACE 1 -- V3-NARROW GEOMETRIC DE-COMMIT LEVER (MECH-439 DURATION face)
    ============================================================
    Answered by an ALL-ON A/B contrast of frontopolar_gain>0 (ON) vs
    frontopolar_gain=0 (null, bit-identical to use_frontopolar_decommit=False):
    does injecting release pressure = frontopolar_gain * max(0, cfv_now -
    cfv_at_entry) -- where cfv is the MECH-264 goal-proximity ADVANTAGE
    ||z_chosen - z_goal|| - ||z_alt - z_goal|| (NON-F channel) -- into
    ree_core/policy/natural_commit_urgency.py measurably SHORTEN commit-latch
    occupancy / RAISE switch propensity on the F-dominance conversion-ceiling
    DURATION face, WITHOUT degrading task performance (resources/episode,
    viability), in a way the gain=0 arm does not?

    NON-DEGENERACY PRECONDITION (three parts). This is not boilerplate: as of
    2026-08-08 part (c) is MEASURED-VIOLATED, which is why this face is blocked
    rather than merely un-run.
    (a) cfv_now must be a LIVE, VARYING quantity -- it is a transient scalar
        recomputed each maintenance tick (agent.py compute_counterfactual_value
        at :2984, released as pressure at :5658) and reset per commit; the
        off-entry-value cells (cfv_at_entry) must be populated, or the
        derivative max(0, cfv_now - cfv_at_entry) is identically 0 and the
        lever is a no-op indistinguishable from OFF for reasons unrelated to
        the hypothesis.
    (b) COMMITS MUST BE OVER-LONG in the test env. The lever RELEASES a latch;
        if the natural-commit latch is not holding too long in the chosen env,
        there is nothing to release and ON==OFF trivially.
    (c) THE COMMIT LATCH MUST BE THE BINDING CONSTRAINT. --- CURRENCY-CRITICAL,
        currently FALSE. --- V3-EXQ-724 (the experiment this claim names as the
        all-ON gate) RAN 2026-07-09 as a competence-localization diagnostic and
        returned competence_deficit_diffuse: the integrated all-ON agent forages
        0.065/0.0/0.455 resources/episode (BELOW the 1.0 competence floor, 0/3
        seeds), with NO localizing arm, while a greedy nearest-resource oracle
        clears the floor (6.05/ep) proving the env is achievable. So the binding
        constraint is the UPSTREAM MECH-457 competence floor, not commit-latch
        duration. Releasing a latch on an agent that cannot forage above floor
        yields an UNREADABLE contrast -- any ON/OFF difference is dominated by
        below-floor noise. The all-ON validation is therefore gated on the
        MECH-457 competence-floor wall CLEARING, which remains open as of the
        latest non-resolving evidence (V3-EXQ-687a / 819a / 748a, 2026-07-30/31).
        V3-EXQ-724 has run and did NOT lift this gate; it CONFIRMED it.

    CONFIRMING signature (Face 1), readable ONLY once (a)-(c) hold:
    (i) DURATION MOVES -- ON reduces mean/median committed-latch length vs the
        gain=0 null by a margin exceeding seed spread, monotone in
        frontopolar_gain over a small sweep.
    (ii) SWITCH PROPENSITY RISES on high-cfv ticks specifically (releases are
        concentrated where cfv_now - cfv_at_entry is large), not a uniform
        shortening -- distinguishing "geometric de-commit" from "generic
        shorter refractory".
    (iii) NO TASK-PERFORMANCE COST -- resources/episode and viability at the
        best-shortening gain are within noise of, or above, the OFF arm.

    FALSIFYING (Face 1), two distinct outcomes, two distinct remedies:
    -- LEVER INERT on a valid (post-competence-floor) 724-successor: with the
       floor cleared and commits demonstrably over-long, ON still equals the
       gain=0 null on duration and switch propensity. Then the
       de-commit-RELEASE hypothesis for the MECH-445-cluster arming residual is
       WRONG -- the arming residual is not a held-latch that a counterfactual
       derivative can release. Remedy: retire the frontopolar de-commit route
       for the DURATION face and fold the residual back to the ARC-107 BG
       eligibility route (MECH-448/MECH-449 Go/No-Go), which is already the
       primary MECH-439 resolution path.
    -- LEVER HELPS but a later ablation shows the LEARNED head is unnecessary:
       the parameter-free geometric cfv (no trained MECH-264 head) captures the
       full effect and a learned counterfactual-value head adds nothing. Then
       the frontopolar SUBDIVISION does not earn separate substrate status --
       fold it into the vmPFC-analog (SD-033c) chosen-value machinery as a
       geometric switch term, and demote SD-033e's learned-substrate scope.

    ============================================================
    FACE 2 -- FULL LEARNED V4 SUBSTRATE (parallel counterfactual-value +
    external/internal gateway + relative-importance monitoring)
    ============================================================
    UNTESTABLE BY CONSTRUCTION today -- this face is never-exercised, and the
    preconditions are structural, not merely unfavored:
    -- MECH-264 counterfactual-value TRACKING (the learned head): see MECH-264's
       own what_would_answer for the parallel-value + switch-margin test; DO NOT
       re-derive it here.
    -- MECH-163 hippocampal MULTI-STEP planning is unbuilt: with 1-step
       counterfactuals MECH-264 collapses to MECH-257 and there is no
       "alternative rollout" for a parallel value to be tracked OVER.
    -- MECH-265 relative-importance monitoring requires a K>=2 active-goal env;
       the substrate is single-resource (no CausalGridWorldV2 dual-active-goal
       extension exists), so the K-way comparison is structurally inaccessible.
    -- the external/internal attentional gateway (Burgess 2007) has no discrete
       substrate; operating_mode reserves the parallel_goal_deliberation NAME
       only (forward-compat hook, done -- bit-identical OFF).
    The learned-head flag use_frontopolar_analog is untouched and raises
    NotImplementedError when set. No experiment can exercise this face until
    MECH-163 and a K>=2-goal env exist; minting a proposal now would describe a
    run nothing can execute.

    ============================================================
    WHOLE-CLAIM DISPOSITION READ
    ============================================================
    The claim is substrate_conditional. Face 2 is never-exercised. Face 1 is
    built but its all-ON validation is itself substrate-blocked on the MECH-457
    competence floor -- and that block is EVIDENCED (V3-EXQ-724, diffuse
    deficit), not assumed. A verdict on the frontopolar lever cannot be read
    while the all-ON agent is below the competence floor; any run attempted in
    that regime must be reported VACUOUS (precondition (c) violated), not scored
    as evidence for or against the lever.
```

**Also proposed (your call):** register a `what_would_answer` on MECH-264 (this falsifier
cross-references it -- see Draft 3, drafted in this same wave); consider adding `MECH-457` as an
explicit `depends_on`/`blocked_on` (the evidenced gate on the all-ON validation); no proposal
minted. **Also refresh the `implementation_note` gating clause per GFLAG-0011.**

---

### DRAFT 3 -- `MECH-264` (Frontopolar counterfactual-value tracking)

**Disposition: (c) substrate-blocked** -- `epistemic_category: substrate_conditional`. The
MECH-264-specific content (chosen-vs-counterfactual value *dissociation* over multi-step
counterfactuals) is untestable by construction as of 2026-08-08 because MECH-163 multi-step
planning is a genuine, roadmapped-but-unbuilt V4 prerequisite; only the single-tick geometric
de-commit slice is exercisable today, and that slice cannot by itself confirm the
parallel-maintained-value claim. This draft **extracts** the claim's own explicit "Falsifiable
(primary)" clause into the house structure rather than inventing a test. No proposal minted.

**Currency check:** geometric slice CONFIRMED (`frontopolar_analog.py:287,331-333`
`compute_counterfactual_value`, `d_chosen - d_alt`; STUB docstring, single-tick); full parallel
channel unbuilt (V4 path raises `NotImplementedError`); MECH-163-relevant multi-step counterfactual
maintenance confirmed absent; **V3-EXQ-724 HAS RUN** (see GFLAG-0011); SD-033e's `what_would_answer`
does not yet exist (forward cross-reference, drafted same wave).

```yaml
  what_would_answer: |
    Answered by a DISSOCIATION test, once MECH-163 multi-step planning exists:
    does the FPC-analog track the value of the best UNCHOSEN alternative
    (counterfactual value) rather than the value of the CHOSEN option? This is
    the MECH-264-specific question; the shared substrate preconditions below
    belong to SD-033e and are cross-referenced, not re-derived.

    NON-DEGENERACY PRECONDITION (all currently unmet as of 2026-08-08 -- this
    claim is untestable BY CONSTRUCTION, not merely unfavored):
    (1) MULTI-STEP COUNTERFACTUALS MUST EXIST. The claim is about a value
    estimate maintained IN PARALLEL over multi-step rollouts of the foregone
    alternative. MECH-163 multi-step planning is the prerequisite and is
    unbuilt for this purpose (verified 2026-08-08: compute_counterfactual_value
    in ree_core/pfc/frontopolar_analog.py is a single-tick geometric STUB over
    single endpoints; the V4 learned path raises NotImplementedError). A
    1-step counterfactual collapses to MECH-257 and there is nothing
    frontopolar-SPECIFIC left to test.
    (2) SHARED SUBSTRATE PRECONDITIONS -- the V3-narrow parameter-free de-commit
    lever (use_frontopolar_decommit), its V3-EXQ-724 all-ON validation gate, and
    the V4 learned-substrate scope are SD-033e's. See SD-033e's what_would_answer
    (drafted in the same digestion wave); do NOT re-derive them here.
    (3) CHOSEN AND COUNTERFACTUAL VALUE MUST BE MEASURABLY DISSOCIABLE in the
    test distribution -- the one precondition that is MECH-264's own. Require a
    >=3-alternative decision task in which the value of the best UNCHOSEN
    alternative varies INDEPENDENTLY of the chosen option's value. If the two
    co-vary in the environment used, SD-033e and SD-033c are indistinguishable
    by construction and any "tracks chosen value" or "tracks counterfactual
    value" verdict is an artifact of the probe set, not a finding. Require the
    reported joint distribution over (chosen value, best-alt value) to populate
    the off-diagonal cells -- specifically high-alt-value/low-chosen-value,
    the cell where a switch SHOULD be signalled -- by count, before any verdict
    is read. A run whose off-diagonal cells are empty is VACUOUS and must be
    reported as such rather than scored.

    CONFIRMING signature (all three, not any one):
    (i) SUBSTRATE TRACKS COUNTERFACTUAL, NOT CHOSEN -- FPC-analog activity in a
    V4 implementation covaries with the value of the best unchosen alternative,
    and does NOT reduce to chosen-option value, across the dissociable
    distribution of (3).
    (ii) SWITCH-PROPENSITY LINK (Boorman 2009 signature) -- individual variation
    in the magnitude of the counterfactual signal predicts propensity to switch
    to the alternative; a larger counterfactual-minus-chosen margin precedes
    more switches.
    (iii) DISSOCIATION FROM MECH-151/SD-033c -- the counterfactual signal and the
    chosen-option value signal (SD-033c, MECH-151 vmPFC) are separable channels:
    an intervention that moves chosen-option value leaves the counterfactual
    estimate's tracking intact, and vice versa. Same computation, different
    substrate, different input stream -- as the claim asserts.

    FALSIFYING (the claim's own primary clause, extracted):
    -- TRACKS-CHOSEN: if FPC-analog activity in a V4 implementation tracks
    CHOSEN-option value rather than counterfactual-option value during the
    >=3-alternative task, MECH-264 fails AT SOURCE. SD-033e then collapses
    functionally into SD-033c, the OFC/vmPFC/FPC value architecture is
    over-specified at REE's level of description, and the remedy is to FOLD the
    frontopolar subdivision into the vmPFC-analog (MECH-151) rather than
    maintain a separate counterfactual channel.

    PARTIAL-FALSIFICATION GUARD (do NOT conflate two different claims):
    the V3-narrow single-tick geometric slice can succeed AS A DE-COMMIT LEVER
    -- reducing over-commitment / improving switch timing on the F-dominance
    duration face -- while the FULL parallel-maintained multi-step
    counterfactual-value claim STILL FAILS the dissociation test above. The
    former is SD-033e's V3 question (validated isolated-GAP-A; all-ON gated on
    V3-EXQ-724); the latter is THIS claim. A working de-commit lever is NOT
    evidence that FPC-analog maintains a parallel counterfactual value, and a
    failed dissociation test does NOT retire the geometric lever. Record any
    result against the specific claim it bears on.

    ORDER OF ATTACK, if ever built: precondition (1) is the gate -- there is no
    MECH-264-specific test until multi-step counterfactual maintenance exists
    (MECH-163). Do not attempt the dissociation test on the single-tick slice;
    it can only ever return the MECH-257 collapse.
```

**Also proposed (your call):** consider adding `MECH-163` and `MECH-257` to `depends_on` (the
`implementation_note` names both as load-bearing; verify no cycle first); no proposal minted.

---

### DRAFT 4 -- `INV-073` (Developmental bootstrapping necessity)

**Disposition: (c) substrate-blocked overall** -- `epistemic_category: substrate_conditional`.
This is a **fusion** claim: Leg A (the biological universal over "any model-building agent") is
**(c2) out-of-domain** -- resolves by cross-species/developmental literature, and per the schema
belongs as a `research_anchor`/`literature_synthesis`; Leg B (the REE prediction) is substrate-
blocked with **one partially-runnable arm** -- the feedback-loop-severance half is now toggleable
(SD-055 `use_differentiable_cem`, EXQ-568 confirmed gradient flow), but the exploration-epoch
*permanence* half is blocked on unbuilt substrate (ARC-072 R1/R2, MECH-325/326). No `EXP-####`
minted (the full double contrast is unrunnable), but the SD-055 ON/OFF arm is a chippable
`/queue-experiment` follow-on (see also-proposed).

**Currency check:** exploration-epoch/persistent-trajectory-store CONFIRMED ABSENT (grep 0 hits);
`cue_action_proj` gradient severance NOW REMEDIABLE (`use_differentiable_cem` default-off at
`hippocampal/module.py:1916`, EXQ-568 PASS confirmed `uc4_grad_max` gradient flow) -- so the notes'
present-tense "gradient path is severed" is **stale**; MECH-325/326 (V4 library+routing) zero code;
MECH-269 monostrategy still open (`action_class_entropy=0` in EXQ-478/480/550); EXQ-561 PASS but
`non_contributory`; ARC-072 registered (`depends_on` INV-073). No landed result scores INV-073.

```yaml
  what_would_answer: |
    INV-073 is a FUSION claim. Its two legs resolve by different evidence and
    must not be collapsed into one verdict.

    ============================================================
    LEG A -- OUT-OF-DOMAIN BIOLOGICAL UNIVERSAL (resolves by literature)
    ============================================================
    The universal ("ANY model-building agent requiring flexible multi-option
    selection must undergo a motor-sensory exploration epoch before RL narrows
    the repertoire; insufficient exploration PERMANENTLY restricts the option
    library") is grounded in cross-species developmental biology, not a REE run.
    STRENGTHENED by: further LMAN/subsong-silencing evidence that the
    variability epoch is causally necessary rather than incidental noise
    (Doupe & Kuhl 1999); developmental-window evidence that motor exploration
    is upstream of, not concurrent with, perceptual-template formation
    (Leitao & Gahr 2024); severed-feedback -> single-attractor demonstrations
    independent of exploration DURATION (Warlaumont & Finnegan 2016);
    isolation-rearing showing PERMANENT reversal-learning (update) deficits
    with intact acquisition (Li et al. 2007).
    FALSIFIED / WEAKENED FROM "UNIVERSAL" if: a model-building agent class is
    exhibited that attains a full flexible option library WITHOUT a dedicated
    exploration epoch (e.g. one-shot library synthesis from a world model), or
    if late exploration in a biological system is shown to fully recover the
    repertoire -- either removes the "necessity" and the "permanence".
    SCHEMA NOTE: this leg is a literature/cross-species proposition. It belongs
    as a research_anchor / literature_synthesis on INV-073, NOT as a REE
    experiment, and its confidence should track lit_conf, not exp_conf.

    ============================================================
    LEG B -- TESTABLE REE PREDICTION (the primary disposition)
    ============================================================
    The REE-internal prediction is a DOUBLE CONTRAST on option-library
    diversity / escape from monostrategy (the MECH-269 / EXQ-561 effect):
      (i)  WITH a bootstrapping exploration epoch AND an intact intrinsic
           feedback loop (cue -> trajectory generation gradient live), the
           agent populates a diverse, retrievable option library and escapes
           monostrategy;
      (ii) WITHOUT it -- epoch suppressed, OR the cue_action_proj feedback loop
           severed -- the agent is PERMANENTLY restricted: the restriction does
           NOT recover under unlimited later task-reward RL. "Permanent" is the
           load-bearing word; slower acquisition alone does NOT confirm it.

    NON-DEGENERACY PRECONDITIONS (as of 2026-08-08 -- read before any verdict):
    (1) MULTI-OPTION MUST BE REWARDED. The env must genuinely reward more than
        one strategy (contingency reversals, or multiple goal cues mapping to
        different optimal trajectories). If a single strategy is globally
        optimal, no option library is needed and the test is VACUOUS -- report
        as such, do not score.
    (2) MONOSTRATEGY MUST BE MEASURABLE. Report action-class / trajectory
        diversity directly (e.g. action_class_entropy, cross-cue trajectory
        divergence). MECH-269's diagnostics already show action_class_entropy=0
        collapse (EXQ-478/480/550), so the readout exists; use it as the DV.
    (3) THE "PERMANENCE" ARM NEEDS AN EPOCH THAT CAN CLOSE. Non-recovery can
        only be shown if there is a distinct early phase that ends and a later
        RL phase that cannot repair the deficit. As of 2026-08-08 REE has NO
        such mechanism: grep of ree_core/ for exploration_epoch / babbling /
        persistent trajectory store / intrinsic diversity reward returns ZERO
        hits; MECH-325 (trajectory library) and MECH-326 (retrieval routing),
        ARC-072's R1/R3/R4, have zero code presence. So the WITH-epoch arm (i)
        and the permanence half of arm (ii) are NOT RUNNABLE -- this leg is
        substrate-blocked, not merely unfavored.
    (4) THE FEEDBACK-LOOP HALF IS PARTIALLY RUNNABLE NOW. The severed
        cue_action_proj gradient (EXP-0155, ARC-072 gap 2) is now TOGGLEABLE:
        SD-055's use_differentiable_cem (default False, bit-identical off)
        restores a softmax-weighted CEM so gradient flows from task reward back
        to cue_action_proj; EXQ-568 confirmed the gradient flows
        (substrate-readiness PASS). This lets ONE arm of contrast (ii) be run:
        severed-loop (flag off) vs restored-loop (flag on), measuring whether
        the restored loop produces measurably cue-conditioned, more-diverse
        trajectories on a goal-rich env. EXQ-568's own note flags this is the
        missing test ("requires a trained-policy cue-conditioned divergence
        experiment on a goal-rich env"). This arm does NOT test permanence.

    CONFIRMING signature (REE leg), requires BOTH:
      (a) FEEDBACK-LOOP IS LOAD-BEARING -- with use_differentiable_cem ON, a
          trained policy produces measurably distinct trajectory distributions
          across distinct goal cues AND higher action-class diversity than the
          severed (flag-off) baseline on the same goal-rich env; AND
      (b) NON-RECOVERY (only testable once an exploration-epoch mechanism
          exists) -- an agent whose early epoch is suppressed, then given
          unlimited later RL, does NOT reach the diversity of an agent that had
          the epoch. Until (b)'s substrate exists, only (a) is decidable and
          the full "necessity/permanence" claim stays open.

    FALSIFYING (REE leg), three distinct routes with distinct remedies:
    -- LOOP NOT LOAD-BEARING: with use_differentiable_cem ON, trained
       trajectories are NO more cue-differentiated / diverse than the severed
       baseline. Then the Warlaumont "severed feedback -> single attractor"
       topology does not hold in REE, and INV-073's mechanism (3) is wrong for
       this substrate. Remedy: weaken the REE leg to "monostrategy has a cause
       OTHER than feedback-loop severance"; keep MECH-269 open.
    -- RECOVERS WITH ENOUGH RL: once an epoch mechanism exists, a
       late-exploration / epoch-suppressed agent RECOVERS the full option
       library given sufficient later RL. Then "permanent restriction" (the
       load-bearing word) is FALSE and INV-073 collapses to a SAMPLE-EFFICIENCY
       claim, not a necessity invariant. Remedy: demote from invariant/
       universal to a mechanism claim about bootstrapping SPEEDING, not
       ENABLING, library formation.
    -- DIVERSITY WITHOUT EITHER: the agent reaches a full flexible library with
       no dedicated epoch and no restored gradient (e.g. ARC-065 runtime
       noise-floor diversity alone suffices). Then neither precondition is
       necessary in REE. Remedy: reassign the monostrategy cause to the runtime
       diversity stack (ARC-065) and retire INV-073's REE leg; note ARC-072
       explicitly claims ARC-065 CANNOT fix this, so this outcome also weakens
       ARC-072.

    ORDER OF ATTACK: precondition (4) is the one runnable, independently useful
    step -- an SD-055 ON/OFF cue-conditioned-divergence experiment on a
    goal-rich env (the test EXQ-568 named and did not run) resolves the
    feedback-loop half regardless of INV-073's ultimate fate, and its result
    directly informs ARC-072 gap 2 and SD-055 promotion. Do NOT treat INV-073
    as one indivisible build: the permanence/epoch arm is V4-gated (MECH-325/326),
    the loop arm is testable now.
```

**Also proposed (your call):** the SD-055 `use_differentiable_cem` ON/OFF cue-conditioned
trajectory-divergence experiment on a goal-rich env (the test EXQ-568's note says is missing) is a
chippable `/queue-experiment` follow-on -- advances SD-055 + ARC-072 gap 2 independent of INV-073's
fate; add `SD-055` to `depends_on` (ARC-072 already depends on INV-073, so add only the forward
SD-055 edge to avoid a cycle); refresh the "is severed" notes per the documentation-currency block
above.

---

### DRAFT 5 -- `MECH-138` (Commit-token cancel-window-open flag)

**Disposition: (c) substrate-blocked** -- `epistemic_category: substrate_conditional`. The
cancel-window-open flag and its dFMC/pre-SMA -> premotor suppressive veto pathway have **zero
presence** in `ree_core/`; the mechanism has never been built and therefore never exercised
(`substrate_conditional`, not `substrate_ceiling`), so the ablation test is untestable by
construction and no `EXP-####` is minted. `depends_on` left as-is (no existing substrate id owns a
cancel-window mechanism; the nearest neighbour `natural_commit_urgency.py` is a *hold-duration*
lever, the wrong side of lock-in).

**Currency check (re-confirms the 2026-08-07 pass):** fresh grep over `ree_core/` --
`cancel_window|veto_window|cancel_open` = **0 hits**; `commit_token|boundary_token|execution_lock` =
0; `dfmc`/`pre_sma` = 0. What exists is orthogonal: a bistable beta latch that elevates on commit
and holds, plus `natural_commit_urgency.py` (rung-6 hold-DURATION release) -- every commit mechanism
acts *after* lock-in. Confirmed UNBUILT.

```yaml
  what_would_answer: |
    Answered by ABLATING THE CANCEL WINDOW, once the substrate exists: does a
    commit token that carries a live cancel_window_open flag -- a genuinely
    distinct temporal zone between simulation-complete (E3 selection made) and
    execution-lock-in (beta latch elevated / action emitted), during which a
    top-down suppressive pathway (the dFMC/pre-SMA -> premotor veto analog) can
    abort the transition -- produce measurably better behaviour than an ATOMIC-
    COMMIT control in which selection and lock-in are simultaneous, the flag
    never opens, and only post-commit error routing is available after the fact?

    The predicted benefit is specific: a veto-worthy signal (a harm or error
    signal) that arrives AFTER selection but BEFORE lock-in is caught by the
    open window and the bad transition is aborted, whereas atomic commitment
    would already have executed it and could only route the error post-hoc.

    NON-DEGENERACY PRECONDITION (four parts; ALL currently unmet as of
    2026-08-08 -- this claim is untestable by construction, not merely
    unfavoured. Verified at ree-v3 substrate: cancel_window / veto_window /
    cancel_open = ZERO hits in ree_core/; the only commit machinery present
    is the bistable beta latch and the rung-6 hold-DURATION lever
    natural_commit_urgency.py, both of which act AFTER lock-in and neither of
    which is this window):
    (1) WINDOW EXISTS AND IS ENTERED. The cancel window must be a genuinely
    distinct temporal zone actually entered on a NON-TRIVIAL fraction of
    commits. If lock-in follows selection instantly (window width -> 0), there
    is nothing to veto and the ablation is vacuous. REQUIRE reported window
    OCCUPANCY -- the fraction of commits that spend >0 steps with
    cancel_window_open true, and the distribution of window widths. A window
    that is structurally present but empirically never occupied fails this
    precondition exactly as an absent one does.
    (2) IN-WINDOW VETO-WORTHY SIGNALS EXIST. The test distribution must contain
    veto-worthy signals (late-arriving harm/error) that arrive INSIDE the
    window -- after selection, before lock-in. If every veto-worthy fact is
    available at or before selection, the window is redundant with pre-commit
    simulation and, by the claim's OWN neural-distinctness assertion, the two
    must be distinguished. REQUIRE the count of in-window-arriving veto signals
    reported by cell; a run with none is redundant-with-pre-commit by
    construction and must be reported as such, not scored.
    (3) THE SUPPRESSIVE PATHWAY HAS A REAL EFFECT. The dFMC/pre-SMA -> premotor
    veto analog must actually suppress transitions when asserted, not be a flag
    that is set but never acted on. REQUIRE a demonstrated abort: at least some
    commits with cancel_window_open true and an in-window veto signal are
    measurably prevented from locking in, relative to a run where the pathway
    is disconnected.
    (4) THE THREE PHASES ARE NEURALLY DISTINCT IN THE SUBSTRATE. Per the
    claim, the cancel window is distinct from BOTH the planning/simulation
    phase and the post-commit execution phase. The window's veto must operate
    on state that is NOT identical to the pre-commit simulation input (else it
    is phase 1 relabelled) and NOT merely post-hoc error routing (else it is
    phase 3 relabelled).

    CONFIRMING signature (all three, not any one):
    (i) THE WINDOW CATCHES LATE VETOES -- with the window live and populated
    with in-window veto signals (preconditions 1-2 met), the agent aborts bad
    transitions it would otherwise lock in, improving a harm/error outcome
    metric relative to the atomic-commit control.
    (ii) THE BENEFIT IS NOT REPRODUCIBLE BY EARLIER DELIBERATION -- the same
    improvement CANNOT be obtained by simply lowering the E3 pre-commit
    selection threshold (or widening pre-commit simulation) in the atomic
    control. If a lower selection threshold on the atomic control recovers the
    full benefit, the window is redundant with pre-commit deliberation, not a
    distinct zone. This is the load-bearing discriminator and it must be run
    as an explicit third arm, not assumed.
    (iii) THE BENEFIT IS DRIVEN BY IN-WINDOW SIGNALS SPECIFICALLY -- restricting
    veto signals to arrive only pre-selection collapses the benefit toward the
    atomic control, and restricting them to arrive only in-window preserves it.
    A benefit that survives removing all in-window signals is coming from
    somewhere other than the cancel window.

    FALSIFYING, in three distinct ways with three distinct remedies:
    -- (i) DECORATIVE WINDOW: the atomic-commit control matches the windowed
    commit on all metrics. The cancel window buys nothing; commitment should
    stay atomic. Remedy: drop the cancel_window_open flag, keep atomic commit
    with post-commit error routing only.
    -- (ii) REDUNDANT WITH PRE-COMMIT SIMULATION: any benefit is fully
    reproduced by lowering the pre-commit selection threshold or widening
    pre-commit simulation (confirming signature (ii) fails). Then the "window"
    is just more pre-commit deliberation and is NOT the neurally-distinct zone
    the claim asserts -- this contradicts MECH-138's own central assertion.
    Remedy: merge the mechanism into pre-commit simulation and demote the
    distinct-zone claim.
    -- (iii) OVER-CONSTRAINED WINDOW: keeping the window open long enough to
    catch in-window vetoes costs reaction-time / throughput (delayed lock-in)
    by more than the aborted-bad-action benefit is worth -- every window width
    wide enough to be non-vacuous is wide enough to degrade the RT/throughput
    metric past the harm-avoidance gain. Remedy: the window is real but
    mistuned; treat lock-in latency as a first-class cost and either shrink the
    window (accepting some missed late vetoes) or gate window-opening on a
    cheap in-window-veto-likelihood predictor rather than opening it on every
    commit.

    ORDER OF ATTACK, if this is ever built: precondition (1) is the cheapest
    and gates everything -- instrument window occupancy on a commit path that
    already exists (the beta-latch elevation is the natural lock-in event) and
    confirm a non-zero window can be entered at all BEFORE building the veto
    pathway. A window that is never occupied makes the whole mechanism moot
    regardless of how good the veto logic is.
```

**Also proposed (your call):** append the substrate-gap pointer to `notes` (see the
documentation-currency block above); do NOT add a `depends_on` edge to the
`natural_commit_urgency` duration-lever cluster (would falsely imply the cancel window is a
duration lever -- the text cross-ref is the correct link).

---

## What was NOT done, and why

- **Nothing was written to `claims.yaml` or `manual_proposals.v1.json`.** Headless chip, draft-only
  write policy, no live user to approve. This is the skill's own standing rule.
- **No `EXP-####` proposal minted.** All five dispositions are (b) derivational or (c)
  substrate-blocked; none is (a)/(d) testable-now, so none mints. The one genuinely runnable arm
  (INV-073's SD-055 feedback-loop test) is surfaced as a `/queue-experiment` follow-on for the user
  to chip, not minted here.
- **`build_claims_json.py` was NOT run to completion as a commit.** It was run once at session start
  (Step 1) to read the stance tally; with no `claims.yaml` edit applied there is nothing to
  regenerate, and a MASSIVE concurrent governance regen (see below) had the `evidence/experiments/**`
  tree dirty, so committing any derived artifact would have swept another process's work. Run it
  after applying the drafts.
- **The documentation-currency corrections (INV-073/MECH-138 notes, all `depends_on` gaps) were NOT
  applied.** They are `claims.yaml` edits, and this session is draft-only. Apply them with the drafts.
- **The systemic "believed-bucket digestion debt" finding was NOT chipped.** Surfaced above for the
  user to decide; chipping a systemic finding is the user's call per the skill.

## Concurrency note (for whoever applies this)

At draft time (2026-08-08 ~06:20-06:30Z) a large governance/index regen was in flight on the shared
`REE_assembly` checkout -- **1226 `evidence/experiments/**` files modified + many new
`v3_exq_89x_*` experiment dirs untracked**. This session touched NONE of them; it committed only
`evidence/planning/thought_digestion_staged_2026-08-08_trial2_5claims.md` (this file),
`evidence/planning/governance_flags.v1.json` (GFLAG-0011 + the two superseded dups), and
`TASK_CLAIMS.json`. Also note: this session's `task_claim.py open` commit preserved (remedy (a), did
not revert) one foreign uncommitted TASK_CLAIMS entry -- `metaworker-chip-litpull-lit0570`'s
`completion_note`/`completion_note_history` edit. And a stale (>6h) IGW auto-claim
(`igw-auto-igw-208-...20260807T201602Z`) also names `claims.yaml`; it is an awaiting-launch
placeholder, not an active editor, and this draft-only session did not conflict with it.
