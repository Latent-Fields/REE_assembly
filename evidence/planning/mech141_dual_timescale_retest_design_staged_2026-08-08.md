**Status: AWAITING USER / GOVERNANCE REVIEW -- do not treat as ratified.**

# MECH-141 dual-timescale arbitration -- retest disposition + redesign brief

- **Proposal:** EXP-0489 (`backlog_id` EVB-0603), claim **MECH-141**, `dispatch_mode: targeted_probe`,
  `why_now: [insufficient_experimental_replication, low_exp_conf]`.
- **Author:** headless metaworker chip `chip-proposal-exp-0489`
  (session `metaworker-chip-proposal-exp-0489`), 2026-08-08T17:0xZ.
- **Bottom line:** do **NOT** naively re-run V3-EXQ-163 (it is structurally vacuous), and do
  **NOT** autonomously build the major redesign in a headless session. Disposition =
  **`blocked_substrate`** pending (a) governance ratification of the redesign vehicle and
  (b) MECH-457's own validation. The one-line proposal-status flip is **deferred** -- see
  "Handoff" below (a `failure-autopsy` session holds the `evidence/planning/` scope claim).

---

## 1. The claim

**MECH-141** (`mechanism_hypothesis`, status `candidate`, `evidence: []`):

> Tri-loop arbitration requires BOTH a slow proactive inhibition pathway (prefrontal-caudate,
> seconds-scale) AND a fast reactive hyperdirect pathway (STN, ms-scale); these operate at
> segregated timescales and cannot be collapsed into a single arbitration signal without losing
> the fast-interrupt capability.

Biological anchor: Zhang & Iwaki (Front Behav Neurosci 2019, fMRI DCM). The proactive pathway maps
to E3 pre-commit eligibility (MECH-062); the reactive pathway maps to the cancel-window (MECH-138)
at a shorter timescale. Depends on MECH-062, MECH-138, MECH-140, ARC-005, Q-016.

## 2. Why the only existing run is non-contributory (not merely under-replicated)

The single existing run, `v3_exq_163_mech141_dual_timescale_arbitration_20260329T203824_v3`
(2026-03-29), is `outcome: FAIL`, `evidence_direction: inconclusive`. Its stated failure is C4
(`n_conflict_steps > 50`) with **0 conflict steps**, `harm_rate = 0.0` and `inter_loop_spread = 0.0`
across all three arms (DUAL_TIMESCALE / SLOW_ONLY / FAST_ONLY). The proposal frames this as
"insufficient replication," but adding seeds cannot fix it -- **two** seeds (42, 123) already ran and
both returned 0 conflict steps. The vacuity is structural, and has **four** compounding causes
(the first is the one the pipeline already recorded; the other three are additional design defects
found by reading the driver):

1. **No condition-sensitive action policy (the recorded cause).** All three arms execute one
   shared seeded random walk -- `action_idx = random.randint(0, ACTION_DIM - 1)` at
   `experiments/v3_exq_163_...py:346`. With identical actions across arms, harm outcomes are
   bit-identical and the arbitration variants cannot behaviourally diverge. This is exactly the
   `failure_autopsy_20260329-legacy-cluster_2026-08-08` finding: the driver population for
   behaviour-dependent discriminative designs was queued **before** its prerequisite
   action-learning substrate (MECH-457, `ree_core/action_learning/actor_critic.py`) existed --
   MECH-457 landed 2026-07-12, ~3.5 months after this run.
2. **`harm_rate == 0` -- nothing to avoid.** Under a random policy the agent never encounters
   hazards, so `harm_eval_loss` carries no differentiating gradient and there is no task pressure
   for the loops to disagree. Even a real policy needs an env regime that actually produces harm
   events for a harm-avoidance DV to move.
3. **The gate-entropy regulariser suppresses the very signal being measured.** `gate_ent_reg`
   maximises the entropy of `g_motor`/`g_cog`, driving both sigmoids toward 0.5, which drives
   `fast_conflict = |g_motor - g_cog|` toward 0 -- structurally below `CONFLICT_THRESH = 0.2`.
   The regulariser and the conflict criterion are in direct opposition.
4. **`g_commit` gradients are severed.** `g_w = g_commit.detach()` and `g_commit` is rebuilt from
   `torch.sigmoid(torch.tensor(scalar))` (a fresh non-leaf constant), so no gradient reaches the
   gates through the commit path; the gates learn only via the entropy term (toward 0.5). There is
   no mechanism by which the loops could ever learn to conflict.

The autopsy's per-claim disposition: MECH-141 = `competence_implementation_gap`,
`recommended_evidence_direction_per_claim.MECH-141 = non_contributory`,
`recommended_substrate_queue_entry.action = none`, `pending_retest_after_substrate: true`,
`routing: queue-experiment`. Its quality note: *"MECH-141 is genuinely untouched ... Now unblocked
by MECH-457 -- candidate for /queue-experiment re-run, **not chipped by this autopsy pending
governance ratification**."* (MECH-140, co-tagged on 163, is separately `substrate_ceiling` /
`superseded` by `failure_autopsy_V3-EXQ-710_2026-07-03` -- do not re-tag MECH-140 on any retest.)

## 3. Substrate readiness -- ready in principle, but with two real caveats

- **MECH-457 is IMPLEMENTED** (`ree_core/action_learning/actor_critic.py`, 2026-07-12;
  `ree-v3/CLAUDE.md:10326`). This removes the *recorded* blocker (cause 1).
- **Caveat A -- MECH-457 is itself `candidate / v3_pending` and "PROMOTES NOTHING until the ON/OFF
  validation runs + is reviewed."** Building MECH-141 evidence on top of an unvalidated
  action-learning substrate confounds a MECH-141 result with whether MECH-457 works at all. Its own
  4-arm validation (frozen-vs-cotrain x plain-vs-SF, denominator = V3-EXQ-738 local-view ceiling
  48.05) should land and be reviewed first.
- **Caveat B -- the dual-timescale arbitration mechanism is NOT `ree_core` substrate.** The
  slow/fast `g_commit` gate is constructed in the driver, not in E3. A faithful test of MECH-141's
  actual claim ("cannot be collapsed ... in the tri-loop arbitration policy") would exercise the
  *real* E3 pre-commit eligibility (MECH-062) and cancel-window (MECH-138) machinery, not a toy
  re-implementation of them. The synthetic vehicle risks confirming a mechanism the author builds.

## 4. What a correct retest requires (major redesign -- new EXQ *number*, not a `163x` letter)

A non-vacuous test must fix **all four** causes at once, which is a ground-up redesign:

1. **Real policy so arms diverge:** replace `random.randint` with a MECH-457
   `ActorCriticPolicy` + `ActorCriticStep`, trained with PPO/GAE (+ SF-TD if using the SF critic),
   phased P0 world-model warmup -> P1 actor-critic. The three arms (DUAL / SLOW / FAST) must gate or
   bias that policy's commitment so different arbitration -> different behaviour -> different harm.
2. **Env regime that produces harm** (`harm_rate > 0` under the trained policy) so the harm-avoidance
   DV can move -- verify in the smoke test, not after a multi-hour run.
3. **Remove/redesign the entropy regulariser** so it cannot annihilate the conflict signal; make the
   conflict signal a genuine, non-degenerate loop-tension measurement.
4. **Wire `g_commit` into the differentiable graph** (or drop the "learned gate" framing and drive
   the arbitration from measured E3 loop terms).
5. **Smoke assertions (mandatory, per skill Step 4):** `n_conflict_steps > 0` AND the harm DV differs
   across at least two arms, BEFORE committing to the seed x arm grid. A structural zero here is the
   642/785/604c family of "vacuous verdict" failures.

Open design branch points that genuinely need judgment (this is `complex (probe-gated)`, and per
**GOV-FANOUT-1** a single re-posed sequential probe risks inheriting the prior confound):

- **Vehicle:** refined synthetic toy (fast, but partly self-confirming) vs. integration with the
  real E3 eligibility + cancel-window substrate (faithful, but large and depends on MECH-062/138
  maturity). These are >=2 live hypotheses about *how* to test the claim.
- **Whether to gate the retest on MECH-457's own validation landing first** (Caveat A).
- **How the dual-timescale readout maps onto the real commitment machinery** (E3 cadence
  `heartbeat.e3_steps_per_tick` default 10; beta-gate hold; cancel-window) -- the ms-vs-seconds
  timescale separation in the claim needs an operational analog in the substrate's tick structure.

## 5. Recommended disposition

- **EXP-0489 -> `blocked_substrate`**, `blocked_by: ["MECH-457"]`,
  `blocked_note`: *"Only run (V3-EXQ-163) is non_contributory (competence_implementation_gap):
  random-policy shared walk + harm_rate 0 + self-defeating gate-entropy reg -> 0 conflict steps;
  naive replication stays vacuous. Retest requires a major redesign integrating MECH-457
  actor-critic (itself v3_pending, promotes nothing until validated) + real E3 eligibility/
  cancel-window; per failure_autopsy_20260329-legacy-cluster_2026-08-08 it is pending governance
  ratification (routing: queue-experiment, not yet chipped). Not a 163-letter re-run."*
- **Governance action (why the decision chip exists):** ratify the redesign **vehicle** (synthetic
  vs real-substrate integration) and decide whether to gate on MECH-457 validation, THEN chip a
  fresh-numbered `/queue-experiment` build. Do not naively re-queue 163.

## 6. Handoff (headless, contended)

- The proposal-status flip could **not** be applied here: `failure-autopsy-9e8737-r2-pause`
  (claimed 2026-08-08T16:55:31Z) holds the `evidence/planning/` scope claim covering
  `experiment_proposals.v1.json`. The not-owner arbitration verdict is binding -- I did not edit it.
- **Action for the owning failure-autopsy session or the next governance cycle:** set EXP-0489
  (`backlog_id` EVB-0603) to `blocked_substrate` with the `blocked_by` / `blocked_note` in section 5,
  then re-run `build_experiment_indexes.py` to propagate. (Index status persistence keys off
  `backlog_id` in `experiment_proposals.v1.json`.)
- A `kind: decision` chip has been recorded to surface the redesign-vehicle ratification.
