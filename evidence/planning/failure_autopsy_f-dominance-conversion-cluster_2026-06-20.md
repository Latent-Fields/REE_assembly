# Failure Autopsy -- CLUSTER: F-dominance committed-action conversion ceiling (MECH-439)

- **Generated (UTC):** 2026-06-20T08:44:00Z
- **Scope:** cluster (four mechanistically-independent behavioural channels; one shared failure shape)
- **Status:** confirmed (interactive, user-ratified 2026-06-20 at the Step-8 gate, with two modifications -- see Section 7)
- **Root claim:** `MECH-439` (F-dominance bounds committed-action diversity; candidate, `mechanism_hypothesis`, `epistemic_category: standard`, V3-tractable)
- **Owner node:** `behavioral_diversity_isolation:GAP-I` (owner experiment V3-EXQ-689a); substrate entry `f_dominance_conversion_ceiling`
- **Routed by:** interactive `/failure-autopsy` request "all the recent failures which are to do with f-dominance conversion"

This is a **consolidating cluster autopsy**. The four member channels were each individually
adjudicated and confirmed `non_contributory` in prior sessions; this doc does **not** re-adjudicate
them or touch their manifests. Its load-bearing output is the **convergent pattern** -- the four
together as one structural property -- plus the consolidated governance handoff.

---

## 1. Members and scope

**In scope** (committed-action conversion ceiling = root B, F-dominance):

| Channel (biology) | Run | Claim(s) | Prior autopsy | Verdict |
|---|---|---|---|---|
| CRF rule_state (PFC rule-creation) | V3-EXQ-654g | MECH-309, ARC-062 | `failure_autopsy_V3-EXQ-654g_2026-06-19` | non_contributory |
| OFC valuation (outcome value) | V3-EXQ-485h | SD-033b, MECH-263 | `failure_autopsy_V3-EXQ-485h_2026-06-19` | non_contributory |
| SD-037 threat / foraging | V3-EXQ-625e | (no claim tag) | `failure_autopsy_V3-EXQ-625e_2026-06-20` | non_contributory |
| dACC conflict (conflict monitoring) | V3-EXQ-445h | SD-032b, MECH-258, MECH-260 | `failure_autopsy_V3-EXQ-445h_2026-06-19` | non_contributory |

**Rescued reference channel** (existence proof, not a FAIL member): modulatory bias / GAP-A
(V3-EXQ-569g/682 FAILed -> V3-EXQ-569i PASSed via the top-k shortlist; ARC-065 promoted stable).

**Explicitly out of scope** (different roots, per `conversion_ceiling_phase0_synthesis_2026-06-18`):
de-commit-authority FAILs V3-EXQ-460g/460h/468f (**root C**, commitment-dynamics, orthogonal);
V3-EXQ-514t (MECH-436/SD-049 drive-coupling, a separate substrate-ceiling lineage).

---

## 2. The convergent fingerprint (facts)

Every member exhibits the **same shape**: the channel's bias signal is real, matured, and reaches
the E3 accumulator with genuine authority (all non-vacuity / readiness controls PASS), yet committed
action-class entropy is floor-locked between arms (every discrimination criterion FAILS).

| Member | Non-vacuity / readiness control (PASS) | Discrimination criterion (FAIL) | Purest signature |
|---|---|---|---|
| 654g | C1 5/5 met (crf_frac_active 0.581 / 0.942 / 0.783; propagation paired-diff 0.047 / 0.013 / 0.017; within-arm counterfactual 2/3) | C2 paired lifts {-0.013, +0.047, 0.000}; 0/3 >= +0.05 margin | **seed-44 ARM_ON committed_class_counts {0:16,2:237,4:384} byte-identical to ARM_OFF** despite CRF active 78% of ticks |
| 485h | readiness 3/3 (head delta 5.63; high-threat bias range 0.50); C3 frozen-head control PASS 3/3 | C1 1/3 (0.017/0.080/0.012); C2 0/3 (between-context TV 0.004/0.006/0.011) | **seed1 authority_range 0.501 -> committed shift 0.0** (`f_dominance_positive_adjacent`) |
| 625e | R1 curriculum 3/3; R2 z_harm_a nonzero 3/3; 603q harm_eval_range 0.194/0.151/0.390 (3/3) | R3 conversion 1/3; R4 selected_action_class_entropy **0.0 on all 3 seeds** | **selected_class_counts {0:4000} monostrategy** with shortlist active (size 3.0, authority 4000 ticks) |
| 445h | dACC mean_score_bias_abs 2.0 ON vs 0.0 OFF; harm_a_forward_r2 ~0.94 | committed-action-entropy shift floor-locked: action_class_entropy **0.0 in every arm incl. OFF control** | identical entropy across the whole arm grid (monostrategy cause shared with 455a / SD-032 contamination cluster) |

**Failed criterion class (uniform):** discrimination. **Negative/non-vacuity controls (uniform):**
PASS. This is the canonical "negative-control passes, every discrimination criterion fails"
substrate-ceiling fingerprint -- replicated across four channels that share **no claim, no substrate,
no upstream mechanism**. The only shared locus is the **E3 committed argmax**.

The committed DV is **non-degenerate** in every case (committed-class entropy ranges 0.0-1.21 across
seeds -- it can and does move; it simply does not move *between arms within a seed*). The floor-lock
is a property of the selector, not the metric (the 485h seed2 C2 sep-ratio degeneracy was caught
separately by `criteria_non_degenerate`).

---

## 3. One structural property, NOT four independent bugs

Three independent arguments converge:

1. **Coincidence is ruled out by independence.** The four channels are mechanistically unrelated
   (rule-creation / outcome-value / threat-curriculum / conflict-monitoring) and each was *separately*
   matured and verified non-vacuous before testing. Four independent bugs do not produce the
   *identical* "bias reaches authority, committed entropy floor-locked" fingerprint.

2. **The locus is structurally measured.** V3-EXQ-571: F (the primary harm/goal score) accounts for
   **88-89% of E3 committed-selection temporal variance in BOTH the baseline and the
   full-diversity-stack arms** -- the stack does not dent F's share. So every modulatory channel acts
   only at near-ties and drowns at the same selector. This is the quantitative content of MECH-439.

3. **The 569i top-k partial-rescue is the existence proof.** The top-k shortlist *lifted the
   modulatory/GAP-A channel* (569i PASS 2/3; ARC-065 promoted stable) -- proving the ceiling is (a)
   real and channel-specifically liftable (a global measurement artifact could not be lifted for any
   channel) and (b) **non-transferring**: 654g and 625e armed the *same* validated top-k (shortlist
   size 3.0, authority active) and still floor-locked. The fix is channel-specific; the remaining
   channels need either a *generalized* conflict-graded version (689a) or direct F-variance
   rebalancing.

**Verdict: one structural property** -- the F-monopoly at the committed argmax -- not N bugs.

---

## 4. Biological reference triage -- missing-dependency, not falsification

**Closest reference mechanism:** the basal-ganglia action-selection bottleneck. In mammals, multiple
cortical bias streams (OFC value, ACC conflict, PFC rule, amygdala/PAG threat) converge on the
striatum for a winner-take-all committed selection. Critically, real BG selection is **not** a pure
argmax over a single dominant score: the **hyperdirect (cortico-STN) pathway implements a
conflict-graded HOLD** that transiently raises the decision threshold and widens the effective
consideration set when options are close in value -- preventing premature commitment to the single
highest-value option. This is precisely the mechanism MECH-439's falsifier translates
(conflict-graded top-k, `k = f(top-F gap)`, the BG hyperdirect-hold analog).

**Reading:** REE's current E3 committed selection is a *faithful* translation of the BG bottleneck's
winner-take-all aspect but an **incomplete** one -- it lacks the hyperdirect conflict-graded hold
that, in real brains, is what lets a non-dominant stream (a salient ACC conflict signal, an OFC
devaluation) actually change the committed action at near-ties. Without it, a single dominant score
(F) monopolises selection variance and every modulatory stream is decorative.

**This is the good inverse of the SD-003 failure mode.** The four channels are *not* formal-definition
imports that got the mechanism wrong -- they are faithful biological translations of real cortical
bias streams. They fail for a **missing-dependency** reason: the dependency (BG hyperdirect
conflict-grading) of the reference selection mechanism is absent. By the autopsy core principle, that
makes the four FAILs **positive-adjacent evidence for the dependency claim (MECH-439)**, not
falsification of the four channels' own claims.

**Lit status:** the *maintain-diversity-against-a-dominant-gradient* side is grounded (Quality-Diversity
/ MAP-Elites, CDQ-003). The **BG hyperdirect / STN conflict-graded selection** side -- the actual
mechanism of the proposed fix -- is **not yet grounded by a targeted lit entry**. Per the core
principle (a formal/quantitative mechanism with no biology lit entry should commission a lit-pull),
and per the user's Step-8 election, this cluster commissions one (Section 7, routing 2).

---

## 5. Four-layer diagnosis (cluster-level)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** (four channel claims) / **strengthened** (MECH-439) | None of MECH-309/ARC-062/SD-033b/MECH-263/SD-032b/MECH-258/MECH-260/SD-037 was adjudicated -- each is gated behind a downstream ceiling it does not own. MECH-439 is strengthened by the convergence (positive-adjacent, not a counted "supports"). |
| Biological reference | **clear** | BG action-selection bottleneck + missing hyperdirect conflict-graded hold; four faithful cortical-bias-stream translations failing for a missing dependency, not a wrong mechanism. |
| Prerequisites / dependency | **missing (one shared)** | The conflict-graded committed-selection mechanism (`k=f(F-gap)` hyperdirect analog) is the single missing dependency. BUILT in `ree-v3/ree_core/.../e3_selector.py` (`_gap_scaled_commit_pick` + conflict-graded top-k block) but NOT yet validated (689 FAILed; 689a pending). |
| Implementation | **complete (per channel) / partial (root)** | Each channel's bias is fully wired and reaches authority; the root fix is built but unvalidated. |
| Environment | **adequate -> wrong-pressures (conditional)** | 569i shows the reef-bipartite env CAN exhibit committed diversity (structural guarantee of opposite first-action argmaxes); the foraging substrate's natural monostrategy does not (625e). Env adequacy is channel/env-conditional -- a real confound the cluster surfaces. |
| Measurement | **adequate** | committed_action_class_entropy is non-degenerate; the non-vacuity gates caught the right thing. One gate gap noted (625e): no "z_harm_a oscillation-capable band" precondition -- channel-specific, already recorded in the 625e autopsy. |
| Integration | **coupled, ceiling at the argmax** | Every channel couples to the accumulator; all fail at the SAME argmax. The integration IS the bottleneck (seed-44 byte-identical is the purest demonstration). |
| Scale | n/a | -- |

**Recommended `epistemic_category`:** the four **downstream** channel claims stay `substrate_ceiling`
(already set per-channel). **MECH-439 itself is `standard`** -- V3-tractable *now* (the fix exists and
is testable); it is NOT substrate_ceiling and must not be re-tagged as such.

---

## 6. The two live readings (which planning decision they force)

The cluster does **not** force a choice between these now -- it identifies that **689a is the single
experiment that discriminates them**, and that all four channels plus the held downstream retests are
blocked on it.

- **Reading 1 -- substrate-enrichment (B-rebalance is the answer).** The conflict-graded shortlist
  (689a) lifts committed-action-class entropy strict-above both gap-blind controls; the ceiling lifts;
  the four channels' retests release and convert.
- **Reading 2 -- test-design ceiling.** A shortlist-then-modulate lever can only act at near-ties and
  may cap achievable committed entropy *below the proposer's own ceiling* regardless of lever (phase-0
  synthesis, the MECH-439 title's own caveat). If 689a's lift does NOT correlate with per-tick F-gap
  (the pre-registered falsifier), the real target is direct F-variance rebalancing (rank-preserving
  F->eligibility demotion), and the committed-entropy criterion itself may need redesign relative to
  what a near-ties lever can physically deliver.

**689a's pre-registered falsifier (lift must correlate with per-tick F-gap) IS the Reading-1-vs-2
test.** This elevates 689a from "one queued experiment" to the **cluster keystone**.

---

## 7. Routing (user-ratified 2026-06-20, with two modifications)

The user confirmed the one-structural-property cluster read but elected two additions at the Step-8
gate: (a) escalate the granularity-debt hook to a **/claim-synthesis** recommendation anyway (reads
MECH-439 as still too coarse), and (b) **also commission a /lit-pull**.

**Routing 1 -- implement-substrate (keystone validation) + substrate_queue amend.**
689a is the *validation* of an already-built lever, not a build. Substrate action = **amend** the
existing `f_dominance_conversion_ceiling` entry with the four-channel convergence consolidated as
failure-records and point the four downstream retests' `blocked_by` at it (IGW linkage). All four
channel-claim sets stay `substrate_ceiling` / `pending_retest_after_substrate` behind the **same**
689a gate. MECH-439 stays `candidate` (strengthened, NOT promotable until 689a yields a direct
manifest). **None of the four channels re-queued on the current selector.**
**Operational:** 689a (prio 400) is claimed by the Mac (DLAPTOP-4.local) -- dispreferred. Recommend
re-routing it to a cloud worker when one frees (cloud-first rule); it blocks four channels + the
downstream registry.

**Routing 2 -- /lit-pull (commissioned).** Targeted review of **BG hyperdirect (cortico-STN)
conflict-graded action selection**: the STN's role in raising the decision threshold under
choice-conflict, the hyperdirect-pathway "hold" / global-NoGo, and conflict-modulated dynamic
thresholds (Frank's BG/STN models; Bogacz/Cohen threshold-adaptation; Aron & Poldrack STN stopping;
Wei/Rubchinsky STN-conflict). Goal: ground the `k=f(F-gap)` conflict-graded-shortlist mechanism in
biology *before* 689a is adjudicated, so a 689a PASS is read as a confirmed biological translation and
a 689a FAIL is triaged against the reference rather than as a bare null. Register the divergence (if
any) as load-bearing, not a caveat. `targeted_review_MECH-439` (none currently exists).

**Routing 3 -- /claim-synthesis (flagged, proposal-first).** Per the user's read that MECH-439 is
still too coarse. The candidate decomposition the cluster surfaces (proposal-only -- /claim-synthesis
applies its discrimination gate and writes the proposal; no registration here):
- **Child 1 -- existence/bound:** "F-share > ~0.85 at the committed argmax bounds achievable
  committed-action diversity" (the *measured* fact; V3-EXQ-571). Testable, arguably already shown.
- **Child 2 -- lever-sufficiency:** "a conflict-graded near-ties shortlist (`k=f(F-gap)`, BG
  hyperdirect analog) lifts committed entropy strict-above gap-blind controls WITHOUT reducing F's
  variance share" (the optimistic Reading-1 mechanism; 689a is its falsifier).
- **Child 3 -- residual-ceiling:** "near-ties levers cap committed entropy below the proposer ceiling
  regardless; only direct rank-preserving F->eligibility demotion lifts it" (the pessimistic Reading-2
  mechanism).
The discriminating evidence between Children 2 and 3 is *exactly* 689a's F-gap-correlation falsifier,
so the synthesis is **best sequenced to consume the 689a result** -- it is the cleanest two-reading
fork the cluster produces. (Caveat recorded for /claim-synthesis: this is convergent-recurrence, not
the classic divergent-signature granularity debt; the discrimination gate should confirm the children
are independently testable before registering -- Child 1 may already be `shown`.)

**Draft consolidated note** (governance may append to the `f_dominance_conversion_ceiling` substrate
entry / GAP-I node `governance_*` line -- no per-claim status change):

> "Cluster autopsy 2026-06-20 (`failure_autopsy_f-dominance-conversion-cluster_2026-06-20`):
> consolidated four mechanistically-independent committed-action conversion FAILs -- 654g (CRF
> rule_state), 485h (OFC valuation), 625e (SD-037 threat/foraging), 445h (dACC conflict) -- all
> individually confirmed non_contributory. Shared fingerprint: bias reaches E3 accumulator authority,
> committed-action-class entropy floor-locked between arms (purest: 654g seed-44 ARM_ON==ARM_OFF
> byte-identical at 78% CRF active; 485h seed1 authority 0.50 -> committed shift 0.0). ONE structural
> property (F = 88-89% E3 variance, V3-EXQ-571), not four bugs; 569i top-k rescued the modulatory
> channel only (channel-specific, non-transferring). Biology: missing BG hyperdirect conflict-graded
> hold -> the FAILs are positive-adjacent evidence for MECH-439, not falsification of the four channel
> claims (all intact, gated behind a ceiling they do not own). Keystone = V3-EXQ-689a (conflict-graded
> shortlist, built, prio 400, on Mac -- re-route to cloud); its F-gap-correlation falsifier
> discriminates substrate-enrichment vs test-design-ceiling. Routing: implement-substrate (689a
> validation) + substrate_queue amend; /lit-pull targeted_review_MECH-439 (BG hyperdirect/STN);
> /claim-synthesis proposal (MECH-439 -> existence / lever-sufficiency / residual-ceiling children,
> sequenced to consume 689a). All four channels stay substrate_ceiling/pending_retest behind the same
> gate; none re-queued on the current selector. MECH-439 stays candidate (strengthened, not promotable
> until 689a yields a direct manifest)."

---

## 8. Learning extracted

1. **Four mechanistically-independent cortical-bias channels converge on one selector bottleneck**
   with an identical fingerprint -- the load-bearing cross-claim signal that no per-FAIL autopsy could
   establish. This is the empirical body of MECH-439.
2. **The 569i top-k rescue is channel-specific and non-transferring** -- a validated fix for one
   channel (modulatory/GAP-A) does NOT generalize to CRF, OFC, threat, or dACC. Generalization
   requires the conflict-graded version (689a) or direct F-rebalancing.
3. **Biology localizes the missing dependency precisely:** the BG hyperdirect (STN) conflict-graded
   hold. The four FAILs are positive-adjacent evidence for that dependency, not falsification of the
   channels.
4. **689a is a keystone, not just the highest-priority queued experiment** -- it gates four channels
   plus the downstream retest registry, and its F-gap-correlation falsifier discriminates the two live
   readings. It should be on a cloud worker, not the Mac.
5. **The recurrence is convergent, not divergent** -- but the user elects to treat MECH-439's coarse
   single-claim framing as granularity debt anyway, with the cleanest decomposition (existence /
   lever-sufficiency / residual-ceiling) sequenced to consume the 689a result.

---

## 9. Granularity-debt recurrence note

4+ autopsies (445h, 485h, 654g, 625e) plus the lineage autopsies (569g/682/689) circle MECH-439. The
*default* autopsy reading is NOT debt: the recurrence is **convergent** (identical signature, shared
root the claims do not own), and the four-roots decomposition (phase-0, 2026-06-18) already
discharged the classic divergent-signature debt. **However, per the user's Step-8 judgment**, MECH-439
itself bundles an existence claim, a lever-sufficiency claim, and a residual-ceiling claim that the
two live readings pull apart -- so a proposal-first /claim-synthesis is flagged (Section 7, routing 3),
to be sequenced behind / to consume the 689a result rather than to block it.
