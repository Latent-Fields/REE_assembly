# ARC-070 / MECH-321 decomposition-trigger re-operationalization -- design spike

**Status: AWAITING GOVERNANCE REVIEW.** This is a PROPOSAL only. It queues no experiment,
edits no `claims.yaml` entry, and edits no `*_plan.md` frontmatter or status field. It is
written for `/governance` to ratify, revise, or reject.

- **Generated (UTC):** 2026-08-28T20:00:49Z
- **Session:** metaworker-chip-20260827-arc070-repose-reoperationalization
- **Chip:** `chip-20260827-arc070-repose-reoperationalization`
- **Scope:** `policy_decomposition_trigger:REPOSE` (ARC-070 / MECH-321), per
  `evidence/planning/policy_decomposition_trigger_plan.md`
- **Trigger for this spike:** V3-EXQ-938 (confirmed `failure_autopsy_V3-EXQ-938_2026-08-20`,
  applied by `/governance` 2026-08-21) returned `non_contributory` on both claims -- a clean
  null at its own grain, not a detected negative -- and governance explicitly REFUSED a
  lettered 938 successor and a fourth environment-axis escalation: *"reopen only on a
  different operationalization, not another env-axis letter."* The 2026-08-27
  debt-classification sweep classes this node `mystery (known data)`: the substrate and
  corpus needed to answer are already in hand; a frame is owed, not more data collection.

---

## 1. Where the chain actually stands (read, not re-derived)

Six prior runs (816, 820, 816b, 816c, 816d, 830, 839 -- 830 and 839 contribute the fifth and
sixth hits) died circling one readout: an absolute floor on region-`V_s`, confirmed
`H-vs-proxy-saturation` -- region-`V_s` saturates at 0.9338 and is decoupled from forward-PE
(spearman 0.083 against a 0.2 coupled floor). V3-EXQ-938 re-posed the trigger onto a
within-run rank on forward-PE (top-20%, expanding-window quantile) with a rate-matched
`ARM_YOKED` control and an unconditional whole-episode harm DV -- the shape V3-EXQ-919 proved
decisive on this substrate. It executed cleanly (rate gap 1.85%, 0 seeds outside tolerance,
A-A control exact, all 15 readiness preconditions met, `non_degenerate: true`) and returned a
genuine null: harm delta -0.001338 against SE 0.002764 (t = -0.484), 19/17 seed split, and an
observed effect that is 17.3% of the run's own 80%-power MDE.

The confirmed autopsy drew two conclusions worth restating because they set the boundary
this spike must respect:

1. **938's DV class is explicitly excluded by ARC-070's own registered falsifier.** ARC-070's
   `what_would_answer` states in terms that a failure of downstream task-level benefit
   (decomposition fires but does not reduce harm) does NOT by itself falsify ARC-070 -- that
   is MECH-321's separate claim. 938 measured exactly that excluded class. Its null is real
   evidence about *selectivity of placement*, but it is not evidence against ARC-070's
   narrow architectural claim (the mechanism engaging when it should), and the governance
   disposition (`non_contributory` on both claims, not `weakens`) already reflects this.
2. **`H-representation-axis` is alive and unexcluded**, and 938's own proximal readout
   (`secondary_fwd_pe_delta_yoked_minus_pe = -2.6e-05`) is exactly that hypothesis's
   signature: a within-run rank normalisation does not fix a readout that is too coarse to
   locate the loci where decomposition would help. Governance's own words: *"needs a readout
   spike, not another outcome comparison."*

**What this rules in and out for a re-pose.** Both a fourth region-`V_s` escalation and a
fifth PE-placement-vs-outcome outcome comparison would repeat the same measurement gap the
autopsy just diagnosed. A genuinely different operationalization has to move on at least one
of: (a) what counts as "prediction failure" is measured on, (b) what behavioural surface is
read out, or (c) the grain at which the DV is computed -- and ideally sidestep the
occupancy-gate failure mode by construction rather than by hoping for a favourable dose.

**Also read and not re-litigated here:** MECH-321's separate task-outcome axis (whether
decomposition, once triggered, IMPROVES harm) is independently and heavily explored --
V3-EXQ-844 (FAIL), 867/867a/867b (pool-exhausted, refused a further letter), and 919 (the
harm-aware-selection substrate, built 2026-08-01, tested unconditional whole-episode and
**eliminated** `H-harm-aware-reduces-task-harm`). That axis is not "mystery (known data)" in
the same sense as the trigger-readout question; it looks closer to exhausted-at-this-grain.
This spike does not propose reopening it, and candidate C below explains why it is
deliberately not recommended.

---

## 2. Candidate A -- readout-validity diagnostic (attacks `H-representation-axis` directly)

**What it measures.** Not an outcome comparison at all. A single-arm (or `ARM_OFF`-only)
dense-instrumentation diagnostic run, in the `816c` mould (measurement `experiment_purpose`,
not `evidence`), that records a PER-STEP forward-PE trace alongside a per-step, per-locus
**oracle "would decomposing here have helped" label**, computed offline by a bounded
counterfactual: at a sampled set of candidate loci (e.g. every commit boundary in a fixed,
seeded batch of episodes), replay the SAME trajectory prefix through the deterministic env
twice -- once continuing on the committed chunk, once forcibly decomposing at that locus --
and record whether the forced-decompose branch's subsequent forward-PE / harm signal is
lower. This produces a ground-truth "beneficial-to-decompose" label per locus, independent
of forward-PE. Then measure forward-PE's own precision/recall (or rank-correlation) against
that oracle label set -- i.e., does the readout that 938's trigger already uses actually
locate the loci where decomposition would have helped, at any threshold, not just the
top-20% cut 938 happened to use.

**Why a 938-class null cannot recur by construction.** 938's null was a SE-bounded,
whole-episode-diluted outcome comparison -- a real effect between 1 and 2.8 SE would have
been neither detected nor excluded by its own admission (autopsy learning #3). This design
has no such equivalence-band ambiguity: it is a correlation / precision-recall calibration
against a directly-computed oracle, not a mean-difference test starved by episode-level
averaging. A null here (low correlation, poor precision/recall at every threshold) is
directly interpretable as "the readout cannot locate the loci" with no dilution artifact to
explain away. It also does not depend on natural occupancy of any rare state (the
occupancy-gate failure mode that killed 816/820/816b/816d) because loci are sampled from
already-occurring commit boundaries in a bounded batch, not from a rare threshold-crossing
event.

**What a positive result means.** Forward-PE (even at its current granularity) DOES locate
genuinely-beneficial-to-decompose loci above chance. This substantially narrows the
governance-surfaced conflict from 938: the measurement leg would read closer to adequate,
which reopens the possibility that 938's null is closer to a genuine selectivity null after
all (though still scoped to ARC-070's own excluded-DV-class caveat) -- and licenses a future,
better-targeted outcome re-pose (e.g. using an oracle-informed threshold rather than a fixed
top-20% cut) with a real prior that the readout is not the bottleneck.

**What a null means.** Forward-PE genuinely cannot locate the loci -- `H-representation-axis`
moves from alive-and-unexcluded to actively supported. This is itself the actionable
finding: it tells `/governance` and any future `/implement-substrate` pass that the next
re-pose needs a DIFFERENT readout entirely (candidates: an ensemble-disagreement /
epistemic-uncertainty signal computed from the same forward model rather than its point
prediction error, or a learned locus-classifier trained on exactly the oracle labels this
diagnostic would produce), not a better statistic derived from the same forward-PE scalar.

**Rough cost.** Low. This is architecturally a `816c`-class diagnostic (single measurement
pass, dense per-step recording, no rate-matching machinery, no 40-seed power requirement --
correlation/precision-recall estimates are informative from a much smaller sample than a
mean-difference test needs). The counterfactual replay doubles the compute of a normal
diagnostic pass but stays well under 938's 13.7-hour outcome run. No substrate build is
required -- the deterministic env, the forward-PE readout, and the decomposition operator
are all already landed and default-off/bit-identical.

**Relation to the "mystery (known data)" classification.** This is the candidate that
matches the classification most literally: the substrate that generates the needed data
(deterministic env, forward model, decomposition operator) is already built; what has never
existed is the OFFLINE COUNTERFACTUAL FRAME needed to score the readout against ground truth
rather than against another downstream outcome statistic. No existing manifest in the corpus
has this per-locus oracle label already computed (938 and 816c both record aggregate /
histogram statistics, not per-locus counterfactual outcomes), so this is a new (cheap)
diagnostic run, not a pure re-analysis of an existing manifest -- but it needs no new
substrate and no new outcome-comparison machinery.

---

## 3. Candidate B -- ARC-070's own registered falsifier, tested literally for the first time

**What it measures.** ARC-070's `what_would_answer` FALSIFYING clause, verbatim: *"the
WITH-ARC-070 agent nonetheless commits blind and executes the ungrounded remainder... even
though its own trigger condition... is genuinely met -- the mechanism does not engage when
it architecturally should."* No run in the corpus has tested this literally. V3-EXQ-904
tests trigger-selectivity under artificially-forced pre-commit conditions (fires when
region_vs < threshold, silent above) but never compares a WITH-ARC-070 agent against a
WITHOUT-ARC-070 agent on an engagement-RATE outcome. V3-EXQ-839 compares `ARM_HANDLE_ON` vs
`ARM_HANDLE_OFF` (both WITH decomposition) to test mid-execution reachability, not
decomposition on vs off. V3-EXQ-938 compares `ARM_PE` vs `ARM_YOKED` (both WITH
decomposition) on downstream harm. **`ARM_OFF` (`use_policy_decomposition: false`) exists in
938's own config as a structural-zero manipulation check, but has never been the load-bearing
comparison arm for anything.**

The proposed design: use an artificially-INDUCED (not merely configured) mid-sequence
uncertainty spike -- reusing 938's own `hazard_tuned_env_overlay` / `scheduled_external_hazard`
mechanism, which is already validated to produce forward-PE heterogeneity, but scheduling one
KNOWN, GUARANTEED-TO-OCCUR spike per episode rather than relying on rank-selection over
whatever heterogeneity happens to occur. Compare `ARM_ON` (`use_policy_decomposition: true`,
mid-execution forward-PE trigger, per SD-084's persistent commit handle) against `ARM_OFF`
(`use_policy_decomposition: false`) on the RATE at which the agent, following the induced
spike, continues executing its pre-committed program unchanged (the FALSIFYING outcome) versus
re-decomposing / aborting (the CONFIRMING outcome per the claim's own (a)/(b) either-direction
language). The DV is a proportion, not a harm magnitude.

**Note on the readout:** ARC-070's falsifier text was written keyed to "MECH-269 V_s drop,"
but `H-vs-proxy-saturation` (confirmed) has since established that region-`V_s` cannot be
driven low by environment manipulation at all. Using forward-PE as the trigger signal here
(as 938 already does) is consistent with the standing refusals in
`govdiag1_repose_mech321_chain_2026-08-12.md` section 6 -- that document explicitly refuses
region-`V_s`-keyed re-queues but explicitly does NOT refuse `H-representation-axis` variation,
and using forward-PE for the trigger (not the DV) here is a design substitution the same
document already sanctions in section 5b, not a new probe of a refused axis.

**Why a 938-class null cannot recur by construction.** This changes BOTH the comparison
(mechanism-on vs mechanism-off, not placement-A vs placement-B within an always-on
mechanism) and the behavioural surface (an engagement/commit-blind RATE, not a downstream
harm magnitude that ARC-070's own falsifier explicitly excludes). It also sidesteps the
six-run occupancy-gate death by construction: the spike is scheduled and guaranteed, not
awaited. A rate DV over a guaranteed-occurring event class needs materially fewer seeds to
power than a mean-difference outcome test (no rate-matching machinery is needed at all, since
the two arms differ in mechanism, not in decomposition volume) -- the design does not inherit
938's own thin-SE-band exposure.

**What a positive result means.** WITH-ARC-070 re-plans/aborts at a rate statistically
distinguishable from WITHOUT-ARC-070 (near-zero blind-commit rate under a genuine,
guaranteed spike) -- this closes the one gap V3-EXQ-904's own scope_note left explicitly
open (904 confirms selective firing under artificially-forced PRE-COMMIT conditions, not
under a genuinely-induced MID-EXECUTION spike) and gives ARC-070's narrow claim its first
mid-execution-grain positive evidence.

**What a null result means.** WITH-ARC-070 commits blind at a rate statistically
indistinguishable from WITHOUT-ARC-070, even though the induced trigger condition is
genuinely met. Per the claim's own registered text this is NOT an excluded DV class -- this
IS the falsifying condition, verbatim. Unlike 938, a null here would be a real,
claim-level-actionable finding in either direction, not a scoped non-contributory reading.

**Rough cost.** Moderate. Reuses 938's hazard-overlay machinery and SD-084's persistent
commit handle wholesale; the new work is (i) the guaranteed-spike scheduling logic (simpler
than 938's expanding-window rank quantile), (ii) the commit-blind-rate instrumentation
(arguably simpler than a harm-magnitude DV -- no rate-matching, no A-A control needed since
arms differ mechanically), and (iii) a binomial/proportion power calculation in place of
938's paired-mean-difference one, which is likely to need fewer than 938's 40 seeds for
comparable power given a guaranteed rather than probabilistic occasion. Below 938's own
build+run cost; a `/queue-experiment` pass, not a substrate build.

---

## 4. Candidate C -- local, boundary-conditioned outcome grain (explicitly NOT recommended now)

Stated for completeness and honesty, not as a recommendation. A local-window harm DV
(harm delta in a fixed window immediately following each decomposition event, matched
against a yoked control's local window, rather than 938's whole-episode mean) would have a
materially larger expected effect size than a whole-episode-diluted DV -- the autopsy's own
learning #3 notes 938's whole-episode mean is diluted by exactly this. In principle this is
a genuine grain change from 938.

**Why it is not recommended as a next move.** It is still an outcome comparison on the SAME
axis 938 tested (does decomposition, once placed, reduce harm), and governance's routing on
938 was explicit: *"Do NOT queue a lettered successor to 938 on the strength of this
null... needs a readout spike, not another outcome comparison."* Worse, the closely-related
task-outcome axis is not merely tested once but heavily explored and mostly closed: V3-EXQ-844
(FAIL, wrong direction), 867/867a/867b (pool-exhausted, 867c explicitly refused), and 919
(harm-aware-selection substrate, built 2026-08-01, **eliminated**
`H-harm-aware-reduces-task-harm` on an unconditional whole-episode design -- the same shape
this candidate would reuse). A local-window re-cut of an already-eliminated hypothesis is not
a new operationalization in the sense this spike is charged with finding; it is a
statistical-power variant of a question the corpus has already answered in the negative
several ways. **Recommendation: park this candidate.** It becomes worth reconsidering only if
Candidate A returns a clearly positive readout-validity result (i.e., there turns out to be a
locatable signal worth re-testing at finer grain) or if a materially new selection mechanism
is built that 919 did not test.

---

## 5. Recommendation

1. **Run Candidate A first.** It is cheap, needs no substrate build, and is the direct
   instrument the confirmed 938 autopsy asked for ("a readout spike, not another outcome
   comparison"). Its outcome is informative regardless of direction and directly resolves
   whether `H-representation-axis` should move from alive to confirmed or be meaningfully
   weakened, which the corpus currently has no data to decide.
2. **Queue Candidate B only after Candidate A lands, informed by its result.** Candidate B
   does not depend on Candidate A's outcome to be well-posed (it tests a different claim
   text, ARC-070's own falsifier, at claim-scope, not MECH-321's task-benefit scope), but
   running A first is cheap insurance against building B's trigger on a readout A might show
   to be unreliable -- and A's diagnostic instrumentation may usefully inform B's threshold
   choice for "genuinely met" trigger condition.
3. **Do not queue Candidate C.** Recorded as parked, with the specific condition under which
   it should be reconsidered (A positive, or a new selection mechanism).
4. **This is not a case for parking the claim pair pending a substrate change.** Both A and B
   are buildable now on landed substrate (SD-084 persistent commit handle, 938's hazard
   overlay, the existing decomposition operator) -- this is a `complex (probe-gated)` /
   `mystery (known data)` node in the work-graph-debt vocabulary sense, not a
   `complicated (buildable)`-blocked-on-a-missing-build one. Nothing here is gated on an
   `/implement-substrate` pass.

## 6. What this spike deliberately does not do

- Does not re-queue a lettered V3-EXQ-938 successor.
- Does not re-queue on a region-`V_s` absolute-floor readout (still refused, per govdiag1
  section 6 item 2 -- unaffected by 938).
- Does not touch MECH-321's task-outcome / harm-aware-selection axis (844/867-family/919),
  which reads closer to exhausted-at-this-grain than "mystery."
- Does not edit `claims.yaml`, `hypothesis_space_registry.v1.json`, or
  `policy_decomposition_trigger_plan.md`'s frontmatter/status. Those are `/governance`'s and
  `/failure-autopsy`'s writes, contingent on this proposal being ratified.
- Does not queue either candidate experiment. Both are described at design-intent grain
  (comparison, DV, why-it-differs, cost) sufficient for a `/governance` ratification
  decision; full driver authoring is `/queue-experiment` work, to follow ratification.
