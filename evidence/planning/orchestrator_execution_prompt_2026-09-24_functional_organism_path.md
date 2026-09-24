# Orchestrator execution prompt -- functional-organism path (programme brief)

**Produced:** 2026-09-24 by session `thought-organism-path-20260924`, from the thought
`REE_assembly/docs/thoughts/2026-09-24_from_components_to_functional_organism.md`, after ingestion
(`evidence/planning/thought_intake_2026-09-24_from_components_to_functional_organism.md`) and
digestion drafting (`evidence/planning/thought_digestion_staged_2026-09-24_from_components_to_functional_organism.md`).

**How to start the session:**
1. Open `/workset` -> Session starts -> **Copy start prompt** for the Orchestrator row. If `serve.py`
   is down, run `/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/session_start_prompt.py --role orchestrator`.
2. Paste it into a new session with cwd `/Users/dgolden/REE_Working`.
3. **Append everything between the two `=====` rules below** directly under it.

The standing prompt carries the bounds, the live state and the `/metaworker-orchestrate` invocation.
This block adds a programme to follow inside those bounds. It does not replace or relax any of them.

**Earliest useful start:**
- **Gate G0 (hard):** `governance-20260924-workset` has closed its claim.
- **For cloud dispatch:** also after 2026-09-25T18:00Z, the `clear_at` in `scripts/dispatcher_pauses.json`,
  unless the user lifts it sooner.

A session started before G0 clears does only the start-time checks and lands (see G0).

=====================================================================================================

PROGRAMME BRIEF -- functional-organism path (source: REE_assembly/docs/thoughts/2026-09-24_from_components_to_functional_organism.md)

Follow /metaworker-orchestrate as the standing prompt above says. This brief adds a PROGRAMME: a
sequence of decisions to raise and science work to curate. None of it is authority. It authorises
no build, no experiment and no claim change. Everything below enters REE through the normal skills
(/governance, /failure-autopsy, /diagnose-errors, /queue-experiment, /implement-substrate), and every
consent is a real AskUserQuestion in THIS session (Step 3b rules, recommendation logged via
record_recommendation_outcome.py with --session-id set to your orchestrate-* id).

THE TARGET, so you can judge relevance. The goal is not "install the remaining modules". It is ONE
reproducible closed learning loop: the organism detects a consequential distinction, predicts what
its own alternatives would change, selects and executes, experiences the outcome, and improves later
choices without losing earlier competence. Evidence domains are GOV-JURIS-1's D0-D7
(REE_assembly/docs/architecture/organism_level_validation_doctrine.md). Ranking reach is at most D2.
Own-choice behavioural benefit is D3.
"Milestone A" below is a D3-scoped operational test in one declared task. It is NOT a rival to the
ratified 2026-08-29 "viable minimal working intelligence" milestone, and it must never be written up
as a milestone event; doctrine sec 11 / Q-108 gates that.

------------------------------------------------------------------------------------------------------
START-TIME STOP-CHECKS -- re-measure every one before acting (the premises below were measured
2026-09-24 ~07:20Z and WILL have moved). A premise that no longer holds is corrected in your
WORKSPACE_STATE entry and you continue on the corrected state; a premise that holds is stated as
re-measured.
------------------------------------------------------------------------------------------------------
BASE=/Users/dgolden/REE_Working ; A=$BASE/REE_assembly ; V=$BASE/ree-v3

S1. Governance cycle done?
      /opt/local/bin/python3 $BASE/scripts/task_claim.py list | grep -A1 governance-20260924-workset
    Its task: IGW-20260924-001 (7 pending), 1066 diagnose, 1077->SD-PP-B9 records, SD-PP-B9 PE-source
    probe, SD-033 LPFC transfer, workset regen. The thought's step 1 (adjudicate) and step 3 (next
    B9 discrimination) are THAT session's work. You never duplicate them.
S2. Six draft autopsies confirmed? For id in 1077 1078 1012c 1080 1081 1082:
      python3 -c "import json;print(json.load(open('$A/evidence/planning/failure_autopsy_V3-EXQ-<id>_2026-09-24.json'))['status'])"
    Expect 'confirmed'. At 07:20Z all six were 'awaiting_human_confirmation'. Also:
      grep -c . $A/evidence/experiments/pending_review.md ; and whether 1066 went through /diagnose-errors.
S3. Pause state: $BASE/scripts/dispatcher_pauses.json (cloud-4/5 clear_at 2026-09-25T18:00Z) and the
    standing prompt's "Coordination plane" line. PAUSED => launch nothing; Step 1d local is also a launch.
S4. Science lane already live: `science-20260924-sdppb5-alpha09` (launched 04:24Z, Mac, SD-PP-B5 at
    alpha_world 0.9). `dispatch_campaigns.py show --campaign-id science-20260924-sdppb5-alpha09`. It
    overlaps programme step 2 directly. Read its brief and result BEFORE raising D2.
S5. Governance flags this programme leans on: GFLAG-0447 (sd032b effort = harm double-count),
    GFLAG-0437 (SD-PP-B1 "no native route" premise false), GFLAG-0312 (re-pose; CURRENT_FRONT source
    text trails it). grep each flag_id in $A/evidence/planning/governance_flags.v1.json and read its
    status/resolution_note.
S6. Queue: $V/experiment_queue.json. At 07:20Z it held only V3-EXQ-1067, the floor was STARVED, and
    V3-EXQ-1083 (SD-081) was being reserved by claim igw-241-proposal-for-sd-081-exq-1083.
S7. Staged claim: grep -n "uncertainty_not_discount" $A/docs/claims/claims.yaml. If absent, the
    staged MECH-586 is still unregistered. Do NOT register it yourself (that belongs to /thought-ingestion,
    intake sec 6). Report it under NEEDS YOU.
S8. Usage: Step 0a as usual. The account switched to daniel.delaharpe.golden@gmail.com at 07:05Z on
    2026-09-24 after the previous account was weekly-exhausted. Re-probe; do not assume headroom.

G0 (hard gate). If S1 shows governance-20260924-workset still ACTIVE, or S3 shows the coordination
plane PAUSED: do the standing Step 0a / decision-lane work only, raise NO programme decision below,
curate nothing from this brief, write the WORKSPACE_STATE entry naming which gate held, and land.

------------------------------------------------------------------------------------------------------
PROGRAMME -- mapped to the thought's section 7. For each item: who owns it, what you do, what you
must NOT do. Dependencies are not one queue: items with independent preconditions may proceed in
the same cycle.
------------------------------------------------------------------------------------------------------

P1. ADJUDICATE WHAT ALREADY RAN  -- owner: /governance (+ /diagnose-errors for 1066). Not you.
    You: verify S2. If any of the six is unconfirmed, list it under NEEDS YOU as
    "run /governance to confirm". Do not raise it as a chip (governance work is never chipped).
    Also report whether governance has done three things:
      - applied GFLAG-0437 (SD-PP-B1 title);
      - fixed the CURRENT_FRONT source text
        ($A/docs/CURRENT_FRONT.md:15 "V3-EXQ-1010 ... queued and running"; :17 re-pose "until it happens");
      - recorded 1081 at most D2 and tagged 1082 against SD-013 / ARC-002.
    Never hand-edit a generated page.
    Diagnostic self-labels are not verdicts: 1078 is a vacuous PASS and 1081's C3 precondition was
    unmet, so credit neither from its overall PASS label.

P2. ONE MEANINGFUL FORWARD-MODEL BASELINE  -- gate: P1 confirmed for 1082 (and 1079's autopsy
    already confirmed). First read S4's campaign. If it already answers "is the readable 1082 baseline
    useful at the deployed multi-step horizon through the actual consumer", do nothing but report.
    Otherwise:
    (a) Check whether the confirmed 1082 autopsy's routing names that follow-on. If it does, it is
        /governance's to chip. Check TASK_CHIPS.json and the IGW ledger; if a chip exists, curate it
        (science lane, one member, read-only preflight, RED refused).
    (b) If no routing names it, raise decision D2.
    D2 (AskUserQuestion). "Commission a usefulness probe on the V3-EXQ-1082 readable baseline at
      the DEPLOYED horizon and through the ACTUAL E3 consumer, reusing recorded material where valid?"
      - (Recommended) yes, via /queue-experiment. It reports both absolute error and error relative
        to persistence, plus actual-vs-swapped-action contrasts, with latent scale and smoothing
        controlled.
      - defer until the S4 campaign lands.
      - decline.
      On yes: spawn_task a /queue-experiment chip (record it with chip_ledger.py in the same turn),
      then curate it.
    MUST NOT:
      - re-run 1079 or 1082 to re-prove the alpha / live-battery point;
      - carry the separation-margin loss forward as a repair (it LOWERED the action read on all
        tested arms);
      - commission SD-PP-B10 encoder builds (registration-only; 1082 is a reason to reassess their
        premise, not to build);
      - reopen the extra-preservation-training branch or the V3-EXQ-1065 whitening comparison.
        The encoder-to-consumer problem is owned by the sd106_objective_consumer_transfer question
        and MECH-567/568 (GFLAG notes: no chip yet carries MECH-567's target-carrying-head route).
        That is /governance's to route.

P3. NEXT SD-PP-B9 DISCRIMINATION  -- owner: governance-20260924-workset (its "SD-PP-B9 PE-source
    probe"). You: report what it chose. If a chip for it exists and is ratified, curate it like any
    science chip. The thought's design constraints travel with it, so check the chip prompt has them:
      - same recorded opportunities, exposure matched: residual-head error vs ensemble disagreement vs
        innovation statistic;
      - decorrelation from harm LEVEL is not calibrated epistemic information;
      - an independently scored outcome/learning-usefulness check before any functional-value claim;
      - an explicit outside-the-partition leg.
    If the chip prompt lacks them, raise it as a decision rather than editing it.
    MUST NOT: re-run V3-EXQ-1077 (ran; ambiguous, not missing), or queue a 1062b-style same-claim
    dose / schedule / window rescue (refused by the confirmed 1062a autopsy). SD-PP-B11 stays
    registration-only.

P4. ONE USEFUL CHOICE, END TO END  -- this is the new work. It is the thought's section 6 assay.
    Gate: P1 confirmed for 1082 AND 1012c. Then do a read-only preflight BEFORE raising D1, using
    Opus as a read-only Agent. The preflight writes its findings to a file under
    $A/evidence/planning/ and gives verdict GREEN / AMBER / RED. It answers:
      - Which EXISTING ree-v3 environment supports two feasible routes to a resource, one locally
        attractive with a delayed adverse consequence, the other trading a measurable cost against
        it, with the distinction learnable from permitted observation/history and inside the planning
        horizon? If none does, say so. That makes the option an env build via /implement-substrate,
        not an experiment.
      - Which NAMED, frozen configuration would be the "creature". Use the canonical-profile
        mechanism and state whether a populated profile has been admitted.
      - Whether the confirmed 1082 / 1012c autopsies leave the forward and channel-normalisation
        pieces usable as-is.
      - Whether an evaluator-only positive control can detect the trade-off without privileged state
        leaking into the organism.
    D1 (AskUserQuestion). "Commission the functional-organism assay: a paired diagnostic (self-yoked,
      logs candidate identity / predicted consequence / uncertainty source / per-channel score /
      eligibility / first-action class / returned action) PLUS an autonomous closed-loop evaluation
      (each arm executes its own choices; resources, avoidable harm, completion, viability), on the
      delayed-consequence slice only?"
      Options follow the preflight verdict:
      - (Recommended, if GREEN) author via /queue-experiment.
      - (if RED on the environment) commission the env via /implement-substrate first.
      - defer.
      - decline.
      The chip prompt MUST carry the thought's preflight list verbatim (thought sec 6, "Preflight")
      and its acceptance/failure table. It must carry these requirements:
      - preregistered primary endpoint, effect-size threshold, exclusion policy and decision rule;
      - episodes/seeds as replication units;
      - frozen incumbent vs the minimally changed candidate at matched budgets;
      - a mechanism-specific lesion and a mismatched-content control;
      - a simple reactive/myopic control.
      Held-rule transfer and effort slices are NOT part of this first assay.
    On yes: spawn_task and chip_ledger record in the same turn, then curate with the preflight file
    as --preflight-file.

P5. CANDIDATE EFFORT (IGW-222, sd032b-candidate-effort-proxy)  -- user-HELD until the re-raise at
    or after 2026-09-25T18:00Z. When the standing decision lane re-raises it, the question MUST carry
    GFLAG-0447. The substrate entry's implementation_hint makes effort "a harm-forward rollout cost".
    That double-counts harm (MECH-354), pre-empts open Q-080, and depends on a harm-forward head that
    loses to persistence 6/6 (1062a).
    If /governance has dispositioned GFLAG-0447, present that disposition.
    If not, present these options:
      - (Recommended) keep HELD until a short design note names what "effort" means in the test and
        a producer not already charged by E3's harm channels;
      - build with a named non-harm producer now;
      - build as hinted (state the double-count plainly).
    Acceptance for any build is within-tick candidate spread > 0, a correct-sign harm/effort/goal
    trade-off, and an attributable outcome. Argmin non-invariance alone is not enough.
    Default-off compatibility preserved.

P6. LATERAL-PFC HELD-RULE TRANSFER (SD-033)  -- governance-20260924-workset names "SD-033 LPFC
    transfer". Check what it produced. This item may be PREPARED independently but may RUN only once
    its competence, mode-occupancy and candidate-readout prerequisites pass. It reuses the trained-head
    and SD-082 post-action-summary infrastructure. Its arms are rule-enabled, E3-alone and frozen-head.
    It scores NOVEL-STIMULUS transfer, not another distractor-resistance copy. A pass credits the
    lateral rule-transfer function, not the subdivision architecture. If a ratified chip exists, curate
    it with those constraints checked. Otherwise report; do not author it.

P7. RETAIN / TRANSFER / SIMPLIFY  -- NOT in this session. It opens only after P4 banks a scoped D3
    result: then retention after learning/sleep, a frozen ecological change, and the assembled bundle
    with one repair removed at a time (GOV-DELETE-1). Adaptive recovery (Q-108) is v4 /
    substrate_conditional; its nearest V3 slice (AR-1 cue remapping) goes through /governance before
    anything is commissioned.

------------------------------------------------------------------------------------------------------
DO-NOT-REPEAT (reject any chip, bundle or queue-floor top-up that amounts to one of these)
------------------------------------------------------------------------------------------------------
- V3-EXQ-1077 (ran; ambiguous). V3-EXQ-1079 / 1082 (ran; adjudicate and reuse).
- V3-EXQ-1080 (scoping result, "no reruns owed"; adjudicate).
- V3-EXQ-1062b-style same-claim rescues (refused by the confirmed 1062a autopsy).
- MECH-018 / EXP-0755 and MECH-154 / EXP-0361: blocked on named substrate.
- SD-ZWORLD-SENSE-PATH-PARITY: registered no-build (the gap did not reproduce). IGW-220 lists it as ready;
  it is hygiene, not organism work.
- SD-PP-B10, SD-PP-B11: registration-only.
- A generic SD-081 confirmation. V3-EXQ-1083 is being authored by igw-241. V3-EXQ-811a credits
  MECH-477, not SD-081. If 1083 reaches your curation, check that its brief says what 811a already
  answered.
- ARC-149, MECH-580, Q-108: later-version proposals, not immediate V3 build items.
- sd105_frozen_shared_entropy_floor_multiplier (IGW-219). CORRECTION to the thought: it is a READY
  build (pending_implementation), not registration-only, and it is user-HELD to the same re-raise.
  It is not organism-path work; leave it to the standing decision lane.
The queue floor is STARVED. Top it up only with items that pass this list. An empty queue is better
than a rescue run.

------------------------------------------------------------------------------------------------------
WHAT WOULD CHANGE THIS PROGRAMME (stop and raise it as a decision rather than pushing on)
------------------------------------------------------------------------------------------------------
- Readable, accurate candidate consequences reach selection but behaviour stays poor. Then the
  bottleneck is objective / action repertoire / commitment / ecology, not communication.
- A simple direct policy matches the whole preregistered phenotype at matched capacity and budget.
  Then the intermediary has not earned its complexity. Do not move the test afterwards.
- Repairs work separately but not jointly. Then integration or learning interference is next.
- Success needs privileged labels, supplied failure identity or continual retuning. Record it as a
  scaffolded demonstration, not autonomous competence.
- Several causes coexist. Re-pose the hypothesis partition before any further rescue.

------------------------------------------------------------------------------------------------------
LANDING -- in addition to the standing prompt's Bounds item 5
------------------------------------------------------------------------------------------------------
Your WORKSPACE_STATE entry names, for each of P1-P7:
- its state: gated / reported / decision raised (+ the answer) / chip spawned (+ chip_ref) /
  curated (+ campaign_id) / not reached;
- which STOP-CHECK premises you corrected.
Whatever programme item is next when you land, make it the first line, so the next Orchestrator
session started from the /workset row and this brief resumes without re-deriving.

=====================================================================================================

## Provenance and limits (not part of the pasted block)

- Programme steps P1-P7 map one-to-one onto the thought's section 7 ("First" ... "Fifth"), with P5/P6
  split out of "Fourth". Section 6's assay is P4.
- Ownership boundaries follow CLAUDE.md:
  - /governance and /failure-autopsy work is reported, never chipped;
  - an autopsy's own routing is chipped by /governance after ratification, not by the orchestrator;
  - orchestrate chips follow-on only from decisions the user consented to in its own lane
    (`metaworker-orchestrate` SKILL.md "Chip discipline");
  - `kind: decision` chips are never proxied.
- Premise corrections found at ingestion, which this brief already reflects:
  - sd105 is a ready build, not registration-only;
  - V3-EXQ-811a credits MECH-477;
  - `sd106_objective_consumer_transfer` is a hypothesis-space question id, not a substrate entry;
  - the six autopsies are drafted, not confirmed.
- New artefacts from this session that the brief depends on:
  - GFLAG-0447 (REE_assembly `bc7edc2465`);
  - the staged MECH-586 (intake section 6; registration pending on `claims.yaml` contention).
