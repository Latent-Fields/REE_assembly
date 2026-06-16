# V3 Closure -- Critical-Path Synthesis (snapshot 2026-06-15)

**Status: point-in-time synthesis, NOT a living plan-of-record.** This doc consolidates the
findings of the five critical-path drill-down sessions run 2026-06-14. The authoritative,
self-updating source is the closure map (`/closure` -> `/api/closure`, snapshot
`closure_status.md`) and the owning `*_plan.md` closure-plan frontmatter. This file is a
reference synthesis; it carries **no `closure_plan` frontmatter** so the closure snapshot does
not auto-discover it as a plan. When the underlying nodes move, trust the closure map over this.

Overall V3 at snapshot time: **75.7% weighted, 23 nodes remaining** (52 done, 14 deferred).

---

## UPDATE -- overnight results 2026-06-15/16 (read this first)

The four live experiments all landed. Net: **goal_pipeline GAP-2 + GAP-7 closed**; the three
blocked clusters (GAP-A, GAP-B, GAP-C) each bottomed out at *substrate/readiness-not-ready ->
/failure-autopsy (all three confirmed)*, not at a falsifier verdict -- and the autopsies revealed
that **GAP-A now gates GAP-B as well**, so GAP-A is the single unblock for ~9 downstream nodes.

- **goal_pipeline GAP-2 / GAP-7 -- CLOSED.** V3-EXQ-514o PASS/supports (object-bound wanting!=liking
  dissociation, non_degenerate). MECH-229 -> provisional; 514p/514q queued toward the stable gate.
- **GAP-A (684, conversion readiness) -- FAIL/non_contributory `substrate_not_ready_requeue`, autopsy confirmed.**
  Route-range REACHES the E3 authority (0.187>0.01) and e2 divergence is present (0.060>0.03) -- both PASS.
  The amend *partially works*: **ARM_STD_G2 (gain=2, std-basis) DID convert** (committed entropy
  0.775 -> 0.989). The lone FAIL was the **matched-noise verify-control not lifting over the proposer
  (0/3 seeds)** -- a readiness-GATE defect, not proof the amend fails. ARM_SHORTLIST
  (shortlist-then-modulate, margin 0.25) converted 0/3. Route: fix the verify-control + lock the
  converting gain=2 std-basis lever -> re-queue a 684 successor -> only then 569h. 569h stays blocked.
- **GAP-B (654c, MECH-309/ARC-062 falsifier) -- FAIL/non_contributory, `substrate_ceiling`, autopsy confirmed.**
  The 666c maintenance amend WORKED (retire-churn fixed, pool holds >=2 differentiated rules,
  crf_max_pairwise_rule_dist 0.0->1.711) but **rule ACTIVATION collapsed to exactly 0.0** -- an inverted
  signature. 666c's PASS measured `frac_MAINTAINED`, not `frac_ACTIVE` (maintained != active). Two coupled
  faults: (1) **the GAP-A monostrategy collapse reached the CRF context key** (consumed-summary spread
  0.0089 < 0.05) -> all differentiated rules co-match one collapsed context; (2) the gate theta
  = 0.15 + 0.25*(n_matched-1) climbs above the 0.45 maintenance floor once >=3 rules co-match -> every
  matched rule is gated out. Route: /implement-substrate amend `crf-availability-maintenance` for BOTH
  faults + flip its `ready True->False` + add a `frac_ACTIVE` readiness gate; **654d re-queue is gated on
  the GAP-A context de-collapse.** No claim demotion (claims never tested).
- **GAP-C (603p, base-harm-landscape diagnostic) -- FAIL/non_contributory `substrate_not_ready_requeue`, autopsy confirmed.**
  Positive control (easiest regime 0.10) cleared `harm_eval_range>=0.02` on only 1/3 seeds -> the
  harm-pathway training / readiness metric is underpowered, **NOT a regime-difficulty verdict**. The
  readout itself was non-vacuous (cross-arm spread 0.057). Route: /implement-substrate **amend
  `scaffolded_sd054_onboarding` (harm-pathway leg)**; **603q is blocked on that fix landing**, not on a
  parameter.

**Revised choke picture:** GAP-A (conversion / context de-collapse) now gates sd_037_axis_b (P1b->P4),
self_attribution (GAP-1/2/3), AND GAP-B (654d) -- ~9 downstream nodes. Its amend is *converging*
(gain=2 std-basis converts), so the near-term work is (a) lock the converting lever + repair the
verify-control (GAP-A), and independently (b) the GAP-C harm-pathway amend (isolated subsystem). The
GAP-B amend is partly doable now (theta-coupling, frac_ACTIVE gate, ready->False) but its load-bearing
fault #1 (context de-collapse) IS the GAP-A fix, so it is sequenced behind GAP-A.

---

## The one-paragraph picture

Two findings dominate. **(1) One choke point gates two whole paths.** Behavioural-diversity
`GAP-A` (the channel->committed-action selection-authority conversion) is upstream of the entire
SD-037 axis-b chain (4 nodes) **and** the entire self-attribution chain (3 nodes). Closing GAP-A
unblocks 7 nodes; nothing in those two chains is independently workable until it lands.
**(2) The frontier is instrument-bound, not evidence-bound.** Every one of the five paths' most
recent experiment FAILed for a *measurement/instrumentation* reason (read-timing bug, post-gap
read, manifest misread, marginal contact guard), **not** a substantive falsification. Three of
the four currently-queued items are therefore claim-free **diagnostics** (`682`, `603p`, `666c`)
that fix the instrument before the evidence experiment re-runs. Net: the genuine "distance to
close" on the three blocked clusters is **two experiments deep** (diagnostic -> then evidence),
and each diagnostic can still route back to a substrate-ceiling.

Current run order (queue priority): **680c (315) > 514o (310) > 672b (300) > 682 (290) >
603p (285) > 666c (250)**. Of these, `514o / 682 / 603p / 666c` are the critical-path outputs;
`680c` (MECH-423 super-additivity) and `672b` (MECH-057b) are adjacent, not on these five paths.

---

## Path 1 -- arc_062_rule_apprehension:GAP-B (rule-apprehension; the master unblocker)

**Gates:** arc_062 GAP-I, GAP-J, GAP-K, and sleep_substrate:GAP-2.

**Finding.** The node's gate was **stale** ("GATED ON V3-EXQ-666 PASS, then queue 654c"). 666 had
already run **three times**, all FAIL/non_contributory, none substantive:
- `666` -- mature-dynamics insufficient (differentiation too low).
- `666a` -- clean monotone `frac_maintained` separation (mechanism confirmed functional) but did
  not clear the fraction gate AND its non-vacuity precondition in the same run.
- `666b` -- self-routed `substrate_not_ready_requeue`: the e2ctx full-pool differentiation
  non-vacuity precondition was read **post-gap**, after the 2000-tick context-absent silence had
  eroded ARM_1's pool to empty *by design* -> min-over-arms = 0.0 starved the gate even though
  both load-bearing criteria PASSED.

The 2026-06-14 session reconciled the drift and built the fix.

**Next (queued): `V3-EXQ-666c`** (prio 250, claim-free diagnostic). Clean re-run of 666b that
(a) measures `crf_max_pairwise_rule_dist` **pre-gap** at end-of-training, and (b) enlarges the
maturation window `N_EPISODES 100 -> 200`. Load-bearing discrimination unchanged: post-gap, ARM_2
(maintenance) `crf_frac_maintained >= 0.625` where ARM_1 (mature+e2ctx, no maintenance) `< 0.5`.
Dry-run smoke PASS 2026-06-14.

**Probable path.** `666c` PASS -> sets `substrate_queue crf-availability-maintenance ready=true`
-> **then queue `V3-EXQ-654c`** (the GAP-B behavioural falsifier, MECH-309/ARC-062, committed-class
entropy as primary DV -- *not yet queued; gated on 666c*) -> 654c contributory PASS closes GAP-B
-> unblocks GAP-I / GAP-J / GAP-K / sleep_substrate:GAP-2.

**Risks / hazards.**
- `666c` self-routes `substrate_not_ready` again (non-vacuity unmet) -> re-queue at larger P0.
- `maintenance_insufficient` / `differentiation_alone_clears_ceiling` -> /failure-autopsy.
- This is now a **4-experiment lineage with no substantive signal yet.** The deeper risk is that
  CRF maintenance is a substrate-ceiling, in which case MECH-309/ARC-062/ARC-063 stay
  candidate/substrate_ceiling/v3_pending and 654c never gets a clean substrate to run on.

---

## Path 2 -- behavioural-diversity GAP-A / GAP-B / GAP-C (the cluster everything waits on)

### GAP-A -- CEM/E3 channel->committed-action conversion (the master choke)

**Finding (important correction).** The first `569g` autopsy was a **manifest misread** -- it read
ARM_0's three seeds (~0 by design) as "all three falsifier arms applied
`modulatory_channel_route_range = 0.0`" and concluded instrumentation-defect/action=none. This was
corrected the same day: ARM_1 actually applied route_range 0.219/0.186/0.134 (mean 0.180) =
exactly the readiness probe, at the live select tick. **Route-range *reach* is DONE.** The real
defect is subtler: the readiness gate certifies the *channel-representation spread*, but the
applied *per-candidate routed bias* is gap-relative ADDITIVE at gain 0.5 and subdominant to the
F-dominated primary score (88-89%, per V3-EXQ-571), so committed-selection entropy does not move
strict-above the proposer/matched-noise control (1/3 seeds). This is a genuine shared **conversion
ceiling** (same signature as 569f / 661 / 654a), not a wiring null. SD-056-NaN was disconfirmed as
the cause (e2_world_forward valid+divergent; V3-EXQ-617 already fixed the multistep NaN).

**Next (queued): `V3-EXQ-682`** (prio 290, claim-free diagnostic). Belt-and-suspenders in-arm
confirmation: measures live in-arm `cand_world_summaries` spread + `project_channel_range` output +
applied route_range at the actual select tick across ARM_0/1/2, attributing any residual collapse
to cause_i (live summary re-collapse) / cause_ii (project_channel_range) / cause_iii (routing
wiring).

**Probable path.** `682` -> /implement-substrate the **gain/contrast amend** (the corrected,
682-gated route recorded durably on the GAP-A node): (a) contrast/normalization or gain bump so the
routed range MOVES the committed argmax against the F-dominated primary, with (b) a
shortlist-then-modulate architectural fallback the gain sweep discriminates -> readiness validation
(committed entropy moves with channel range AND beats a *verified-lifting* matched-noise control)
-> `V3-EXQ-569h` falsifier with an **in-arm route-range gate** -> closes GAP-A.

**Risk.** GAP-A is on its **4th substrate amend** (readiness-validated amends 06-03 / 06-06 / 06-10
all left 0 behavioural conversion). Persistent select-tick non-conversion despite reach being
solved suggests the per-candidate routed bias may need a real architectural change
(shortlist-then-modulate), not another gain tweak. This is the single highest-leverage and
highest-risk node on the whole frontier.

### GAP-B -- E3 within-class diversity (MECH-341)

**Finding.** `V3-EXQ-660` LANDED PASS/supports (binary within-class-representative preserver). On
2026-06-14 **MECH-341 was ratified candidate -> provisional** (exp_conf 0.871; v3_pending cleared);
the closure node + decision_state were reconciled the same day. The explicit caveat on the
ratification: preservation is **scoring-layer only -- it does NOT reach committed action** (that is
the GAP-A conversion ceiling, tracked there). ARC-062 is the sole open strand on this node.

**Status.** No experiment queued in this batch. The thin/temperature-insensitive lift concern is
documented but subordinate to GAP-A (the conversion ceiling is where the behavioural payoff lives).

### GAP-C -- tonic noise floor / escape-affordance bridge (MECH-313 / SD-059 / MECH-358)

**Finding.** `V3-EXQ-603o` (ran 2026-06-11; the 603l-autopsy redesign with headroom + continuous
metric) showed a **strong continuous bridge lift** (both arms ~50.3 vs base ~18.65). It self-routed
`substrate_not_ready_requeue` on **one** gate only: `harm_landscape_discriminative_on_base`
(`harm_eval_range >= 0.02` on 1/3 seeds at `proximity_harm=0.15`).

**Next (queued): `V3-EXQ-603p`** (prio 285, claim-free diagnostic). BASE-arm-only, 4 cells x 3 seeds,
Stage-H only; sweeps `proximity_harm` {0.10 positive-control, 0.12, 0.15} at `harm_lr=1e-3` plus a
{0.15, `harm_lr=3e-3`} training-strength rescue cell, keyed on the same `harm_eval_range >= 0.02`
statistic. Locates whether the base-harm-landscape failure is **regime-difficulty** (find the
hardest trainable proximity_harm) or **harm-training-strength** (3x-LR rescue). Positive-control
gate: 0.10 failing on >=2/3 self-routes substrate_not_ready (pathway/metric broken), never a regime
verdict.

**Probable path.** `603p` output = the located parameter -> corrected SD-059/MECH-358 evidence
re-queue **`V3-EXQ-603q`** -> then the Q-045 / MECH-313 / MECH-260 behavioural retest.

**Risk.** If even the 0.10 positive control fails, the harm pathway/metric is broken (not a regime
issue) -> deeper substrate work on Stage-H harm valuation.

---

## Path 3 -- goal_pipeline:GAP-2 / GAP-7

**Finding.** `514n`'s failure (`n_scored_wl_steps=0`) was a **read-timing bug**, not a substrate
gap: the liking target read `_contacted_resource_type(obs_dict)`, which at eval-read time sees the
*post-consumption-cleared* cell and returns None. `V3-EXQ-681` PASS confirmed the authoritative
consumption signal lives in `info['sd049_consumed_type_tag_this_tick']`. (The contact-guard
1/3-vs-2/3 question turned out to be substrate-marginal, NOT a missing lever -- 514n already ports
the full 603n lever stack byte-equivalently.)

**Next (queued): `V3-EXQ-514o`** (prio 310, claim_ids=[MECH-229]). L9 wanting!=liking dissociation
successor to 514n (NOT a supersede), sourcing the liking tag + L2-bind resource_type from `info[]`.
Smoke scored 9 WL steps (514n got 0). Pre-registered gates, each self-routing
`substrate_not_ready_requeue` (never a false weakens): (a) contact non-vacuity guard >=2/3;
(b) WL readiness (constructed-bank separation 1.0 AND >=2 distinct drive-differentiated tokens,
`n_scored_wl_steps >= 5` on >=2/3 guard-passing seeds); (c) L9 acceptance: drive-coupled
wanting!=liking fraction `C_WL >= 0.6`.

**Probable path.** A `514o` PASS closes **GAP-2 AND GAP-7** in one shot (GAP-7 is gated only on this
L9 retest).

**Risks (pre-registered off-ramps).**
- **Substrate-ceiling caveat:** the contact guard is substrate-marginal (603n cleared G3 only 2/3;
  env layout uses OS-entropy `default_rng(None)`). A `contact_guard_unmet` self-route is a
  **foraging-competence substrate-ceiling** finding -> /implement-substrate (do not iterate),
  NOT a MECH-229 weakens.
- **Falsifier off-ramp:** a genuine weakens triggers the off/control arm (bank disabled -> WL~0) +
  overshoot arm (n_resource_types=5); JOINT failure routes MECH-229 -> `substrate_conditional` with
  a V4-1 multi-agent-ecology dependency (clean V3 exit).
- **infant_substrate:GAP-14 coupling:** GAP-14 stays blocked on non-trivial z_goal seeding (prereq
  b cleared 2026-06-10 via 603n, but prereq c re-opened into c-1 exploration-strength collapse
  [blocked on the same modulatory-bias-selection-authority as GAP-A; 667a retest] + c-2
  single-episode-gate over-permissiveness [`V3-EXQ-591d` diagnostic queued]). Sparse superordinate
  z_goal seeding is flagged as REE's single most live empirically-confirmed blocker.

---

## Path 4 -- sd_037_axis_b: P1b -> P2 -> P3 -> P4

**Finding.** No independent work exists, and the node was **mislabelled**. `P1b`'s
`blocked_pending_substrate` status (set 2026-06-05) predated the substrate landings
(scaffolded_sd054_onboarding ready 2026-06-11 via 603n; modulatory-bias-selection-authority ready
2026-06-07 via 643a), so it was stale. Reconciled to **`upstream_blocked`** on 2026-06-14, with a
**bidirectional cross-plan link** added to/from behavioural-diversity GAP-A/GAP-B.

**Adjudication.** The substrate-BUILD half of the resume condition is now MET; the
**committed-action-diversity half is NOT** (the within-class preserver is scoring-layer only and
does not reach committed action -- the GAP-A ceiling). `V3-EXQ-625d` (joint-composite-on) is
**designable but not newly queueable** -- it would re-derive 625c's monostrategy lock until
committed-action diversity is demonstrated by the GAP-A 569-lineage / ARC-062 falsifier.

**Probable path.** Entirely downstream of GAP-A. Once GAP-A lands a non-monostrategy committed
policy: queue `V3-EXQ-625d` (P1b) -> P2 (deterministic p70 recalibration) -> P3 (verification
diagnostic) -> P4 (`V3-EXQ-483f`, 4-arm 2x2, terminal validation **shared with axis-a**).

**Risk.** Hostage to GAP-A. If GAP-A doesn't deliver oscillating non-monostrategy `z_harm_a`, P1b
can't produce a non-degenerate signal. P4 (483f) failing would force rework on BOTH axes.

---

## Path 5 -- self_attribution: GAP-1 / GAP-2 / GAP-3

**Finding.** Confirmed **genuinely downstream**, no near-term independent work. The drill-down
advanced *framing only* (disconfirmed the SD-056-NaN suspicion shared with the diversity FAILs).
- `GAP-2` (SD-029 / MECH-256 retest): resume gated on diversity GAP-A/GAP-B landing a
  behaviourally-validated non-monostrategy policy in the **main agent path**. (A monostrategy
  policy can't generate balanced agent-vs-env event distributions for the C2/C3 measurement.)
- `GAP-1` (ARC-033 vs ARC-058 arbitration; owner 445h forensic read): additionally needs
  sleep_substrate Phase 1 PASS + MECH-269 V_s landing + MECH-307 conjunction.
- `GAP-3` (MECH-257 dual-function 3-arm ablation): depends on GAP-1 + GAP-2.

**Probable path.** diversity GAP-A/B -> GAP-2; (sleep P1 + MECH-269 + MECH-307) -> GAP-1; then
GAP-1 + GAP-2 -> GAP-3.

**Risk.** Deepest dependency stack of the five. Not reachable within V3 unless the diversity cluster
AND the MECH-269/MECH-307/sleep gates all land. GAP-5 (z_self/z_world materialisation) is explicitly
V4-bound and could drag GAP-1 with it (substrate-ceiling / scope risk).

---

## Consolidated dependency view + the four live experiments

| Queued | Path | Type | Closes on PASS | Then unblocks |
|--------|------|------|----------------|---------------|
| `514o` (310) | goal GAP-2 | evidence (MECH-229) | **GAP-2 + GAP-7** | (infant GAP-14 still needs z_goal seeding) |
| `682` (290) | bdiv GAP-A | diagnostic | -> /implement-substrate -> 569h | **self_attr GAP-1/2/3 + sd_037 P1b->P4** |
| `603p` (285) | bdiv GAP-C | diagnostic | -> 603q evidence re-queue | GAP-C / Q-045 |
| `666c` (250) | arc_062 GAP-B | diagnostic | -> 654c behavioural falsifier | **arc_062 GAP-I/J/K + sleep GAP-2** |

**Leverage ranking.** `682` (bdiv GAP-A) is the highest-leverage and highest-risk node: it sits
under 7 downstream nodes across two chains and is on its 4th amend. `666c` (arc_062 GAP-B) is the
second choke (4 downstream nodes) but its mechanism is confirmed-functional, so the risk is
narrower (instrument + maturation window). `514o` is the only direct claim-closer in flight and the
cleanest win (one read-timing fix away from closing two nodes).

**Recurring theme to design against.** Read-timing bugs, post-gap reads, manifest misreads, and
marginal/degenerate metrics -- not substantive falsification -- are the dominant time-sink on the
closure frontier. The "diagnose-first" discipline (claim-free diagnostic before the evidence
re-run) is the current correct response and should stay the default while the substrate is marginal.
