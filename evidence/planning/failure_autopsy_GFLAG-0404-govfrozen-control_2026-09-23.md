# Failure autopsy: GOV-FROZEN-1 check (c), legs resolved by ratified disposition (GFLAG-0404)

Generated: 2026-09-23T19:29:26Z. Confirmed at the Step 8 gate: 2026-09-23T19:41:30Z.
Chip: chip-20260923-govfrozen-control-waived. Session: eloquent-lichterman-824f74.
Scope: governance-schema adjudication by the single producer of
`hypothesis_space_registry.v1.json`. This is not a run FAIL. It adjudicates three
check-(c) flags that GFLAG-0404 routed here. It changes no claim.

## 1. The question

`check_hypothesis_space_integrity.py` check (c) flags any `confirmed` or `superseded` leg
without `control_passed == true`. Three legs were flagged:

| Leg | State | resolving_runs | Status coming in |
|---|---|---|---|
| `mech467_legc_event_denominator_cause/H-commitment` | superseded | [] | RULED by GFLAG-0303 item 3 (2026-09-23): the standing advisory is accepted and control_passed stays false. Not re-litigated here. |
| `mech467_legc_event_denominator_cause/H-cadence` | superseded | [] | Same ruling. |
| `sd_e1_var_bar_readout_crush/H-readout-saturation` | confirmed | [V3-EXQ-1006] | OPEN. This is the target. |

GFLAG-0404 asked whether GOV-FROZEN-1 needs a recognised route, such as
`control_waived_with_basis`, for legs resolved by a ratified human disposition with no
adjudicating run. It also asked why the same-start denominator was substituted for
Leg B only.

## 2. Facts (sub-case 2)

Dry-run gate: `check_dry_run_citations.py` over the V3-EXQ-1006 run_id returned 1 clean
and 0 dry.

- **The denominator rule is in the driver before the run.** ree-v3 `790e95a`
  (2026-09-06T19:12:18Z) is the only commit that touches
  `experiments/v3_exq_1006_sd_e1_var_bar_portfolio_fidelity_anchor.py`. The run started
  at about 19:16:12Z (timestamp_utc 19:51:35Z minus elapsed_seconds 2122.8). The Leg B
  docstring ("WHY SAME-START (red-team #3, 2026-09-06)") and criterion C3 both define
  Leg B's declared null on the SAME-START (Phase 4d) real endpoint set. The from-reset
  (Phase 4b) set is recorded alongside it. Note: `substrate_commit` 3939db768c was read
  when the manifest was written, so its ancestry is not the timing proof. The proof is
  that the file has only one commit.
- **Leg B's control passed.** The readiness precondition
  `branched_same_start_nondegenerate_h1` (control: "env deepcopy + latent-state restore
  per candidate sequence") was met on all 4 arms. The run is `non_degenerate: true`,
  `criteria_non_degenerate.C3: true`, and all four arms are green. Legs A and C carry
  `control_passed: true` from the same gate.
- **The run's own pre-registered criterion adjudicates Leg B.** C3 on the same-start
  set: 2 of 6 seeds reach 0.002 (0.001736, 0.002262, 0.023916, 0.000033, 0.000200,
  0.001071). That makes 4 of 6 below, so `leg_verdicts.B = supported`
  (`realvar_below_bar`). On the from-reset set all 6 of 6 reach it. The red-team
  recomputed both counts from the raw 40-sample arrays, and they hold under either ddof.
- **Where `false` came from.** The 2026-09-07 cluster autopsy read the registered leg
  text as naming Phase 4b. It left the leg alive and recorded both denominators. The
  2026-09-08 user decision (`decision_log.v1.jsonl#2026-09-08T19:50:33Z`) chose
  same-start, which is the denominator the driver had already pre-registered.
  `control_passed: false` was being used to mean "not adjudicated", not "control failed".

## 3. Why the Leg-B-only substitution (asymmetry explained)

1. **It was set before the run, not driven by results.** The rule is git-witnessed
   before the run (see above).
2. **It is specific to Leg B.** Leg B's DV is the ABSOLUTE variance of the real
   endpoints, compared with an absolute bar that is computed over 40 rollouts from ONE
   start. At h=1 those rollouts reach at most n_actions distinct endpoints. Legs A and C
   use the real set only as a normaliser for a ratio. Their MAJORITY verdicts do not
   change with the denominator on this run: Leg A's centroid is in band 6 of 6 on both
   sets for both anchor arms, and Leg C reads `rsd_goal_orthogonal` either way (6 below
   on Phase 4b; 5 below and 1 above on Phase 4d). Per-seed values do change: Leg C
   seed2024's r is 0.036 on Phase 4b and 5.24 on Phase 4d.
3. **The note is stale.** `interpretation.branched_same_start_note` says "the registered
   legs read Phase 4b so this run stays comparable with 1000". The same driver's C3
   statement, its Leg B docstring and its dv_headroom block all contradict that
   sentence. It describes the design before red-team #3 changed it. This is a defect in
   a manifest note, not a design asymmetry. The landed driver and the completed run are
   not retro-edited.

## 4. Four-layer read (governance-schema form)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | No claim moves. INV-088 and MECH-135 are unchanged. |
| Measurement adequacy | adequate | Both denominators are recorded and the control passed on the set that decides the verdict. |
| Recording adequacy | defect | Registry `control_passed: false` misrecorded. There is no `probe_amendments` entry for a denominator amendment made before the run. The manifest note is stale. |
| Integration | n/a | |

Failure-location: MEASURES. A recording defect in the ledger, not in REE.

## 5. Decisions (user, Step 8 gate)

- **Sub-case 2: correct it as a recording error** (rec-20260923-62ed4231). In the
  registry, set `resolution.control_passed` to true. Add a `control_passed_correction`
  block that keeps `prior_value: false`. Add a `probe_amendments[]` entry following the
  schema of the only precedent (`consolidation_readout_validity/H-rem-clamp-artifact`,
  2026-07-18): amended before the adjudicating run, hypothesis unchanged, witness ree-v3
  `790e95a`. Append the asymmetry explanation to `resolution.basis`. `state`,
  `evidence_direction`, `resolved_utc`, `pre_registered_utc` and `hid` are unchanged.
- **General question: no route and no checker change** (rec-20260923-fff2f69b).
  `check_hypothesis_space_integrity.py` is not modified. The reasons:
  - Once sub-case 2 is corrected it leaves the class. The only remaining instances are
    the two MECH-467 superseded legs. They come from one event (2026-09-16) and are
    already ruled.
  - The GOV-HELDOUT-1 lens was used here to make the decision, not to ship a change.
    Among the registry's confirmed and superseded legs, no 3 non-degenerate cases exist
    where a waiver route and the current rule give different answers. A waiver route
    would therefore be scoped to its motivating incident.
  - `superseded` was placed in `CONTROL_REQUIRED_STATES` deliberately (REE_assembly
    a74f644753, 2026-08-19).
  - A permissive waiver would let a `confirmed` leg, which is load-bearing, be ratified
    past its control. That is the Goodhart direction GOV-FROZEN-1 polices.
  - Revisit only if a further non-degenerate case arrives.

## 6. Red-team (Step 7c)

Model: fable (cross-model; the drafter is on Opus 5.5). Verdict: CONTESTED (narrow).
The conclusion survived.

- F1: use the existing `probe_amendments[]` record, not only an ad hoc correction note.
  ACCEPTED.
- F2: invariance holds for majority verdicts, not per-seed values. ACCEPTED and
  reworded.
- Hygiene: `substrate_commit` ancestry is not the timing proof. ACCEPTED.

Step 7b pre-routing checks: 0 fires. C1, C2 and C3 were inapplicable because no target
carries claim_ids. C5 was inapplicable because the checks ran on the JSON draft before
this `.md` existed.

## 7. Learning extracted

- **Recording gap.** `control_passed` was used to encode "not adjudicated". The registry
  has no field for "adjudicating rule amended before the run", other than the
  `probe_amendments[]` precedent. When a driver changes a leg's measurement before the
  run, the producer should write `probe_amendments[]` at queue time. That lets the
  resolution self-clear on provenance instead of needing a later human decision.
- A human decision that picks the rule the driver had already pre-registered is a
  ratification, not a waiver. Tell the two apart by git-witness timing, not by who
  signed.

## 8. For governance

- Resolve GFLAG-0404 citing this artifact.
- Optional hygiene: the V3-EXQ-1006 `evidence_direction_note` still says "Leg B LEFT
  ALIVE", which has been stale since 2026-09-08. Append a dated note. The direction
  does not change.
- No `claims.yaml`, `substrate_queue.json` or `review_tracker.json` write is owed.
