# Claim Synthesis PROPOSAL -- MECH-439 (F-dominance committed-action conversion ceiling)

- **Generated (UTC):** 2026-06-20T08:52:34Z
- **Skill:** `/claim-synthesis` (proposal-first; nothing registered without per-child user approval)
- **Nominated by:** user, at the Step-8 gate of `failure_autopsy_f-dominance-conversion-cluster_2026-06-20`
  (Section 7 routing 3 + Section 9) -- the user reads MECH-439's single-claim framing as still too coarse.
- **Root claim:** `MECH-439` (candidate, `mechanism_hypothesis`, `subject: selection.primary_score_variance_monopoly`, `epistemic_category: standard`, V3-tractable)
- **Sequencing:** **DEFERRED-REGISTRATION.** The discriminating evidence between Children 2 and 3 is
  *exactly* V3-EXQ-689a's pre-registered F-gap-correlation falsifier. This proposal is **sequenced to
  consume the 689a result**; it does **not** block 689a. See Section 6 (689a state) and Section 7
  (registration trigger).

---

## 0. Status of V3-EXQ-689a (the keystone this synthesis consumes)

Checked the coordinator DB on the hub (`coordinator.db`, 2026-06-20T08:52Z):

| Field | Value |
|---|---|
| `experiments.status` | **`claimed`** (DLAPTOP-4.local, claimed 2026-06-19T20:25:17Z; row updated 2026-06-20T08:45:29Z) |
| `results` row | **NONE** -- 689a has not yet produced a manifest |
| Predecessor 689 | `results` outcome = `FAIL`, but the FAIL self-routed `substrate_not_ready_requeue` on the grading-non-vacuity gap-spread leg (a measurement gap, not a verdict) -> superseded by 689a's gap-blind-control redesign |

**Consequence:** the 689a manifest that discriminates Children 2 and 3 is **not yet in**. Per the
nomination's explicit instruction, this proposal is written now (the decomposition logic is fully
determined by the cluster autopsy + phase-0 synthesis) but **per-child registration into `claims.yaml`
is deferred** until the 689a manifest lands and is adjudicated. Registration trigger and the
689a-outcome -> child-disposition map are in Section 7.

> Operational note (not part of this skill's scope, carried from the cluster autopsy Routing 1):
> 689a is on the Mac (dispreferred). Re-routing it to a cloud worker is recommended but is the
> implement-substrate / runner-ops track, not claim-synthesis.

---

## 1. The cluster's failure record (Step 2)

Source: `failure_autopsy_f-dominance-conversion-cluster_2026-06-20` (the consolidating cluster
autopsy; `scope: cluster`), which itself consolidates four already-confirmed per-channel autopsies.
This skill does **not** re-read or re-adjudicate the four channel manifests -- it reads the cluster
verdict.

| Member | Run | Non-vacuity / readiness (PASS) | Discrimination criterion (FAIL) | Purest signature |
|---|---|---|---|---|
| CRF rule_state | V3-EXQ-654g | C1 5/5 met (crf active 58-94%) | C2 paired lifts {-0.013,+0.047,0.000}; 0/3 >= +0.05 | seed-44 ARM_ON committed counts byte-identical to ARM_OFF |
| OFC valuation | V3-EXQ-485h | readiness 3/3 (head delta 5.63) | C1 1/3; C2 0/3 (between-context TV ~0.007) | seed1 authority_range 0.501 -> committed shift 0.0 |
| SD-037 threat/foraging | V3-EXQ-625e | R1 3/3; R2 3/3; harm_eval_range 3/3 | R3 1/3; R4 selected entropy 0.0 all 3 seeds | selected_class_counts {0:4000} monostrategy, shortlist active |
| dACC conflict | V3-EXQ-445h | dACC bias 2.0 ON vs 0.0 OFF; r2 ~0.94 | committed entropy floor-locked, 0.0 every arm incl. OFF | identical entropy across the whole arm grid |
| MECH-439's own first falsifier | V3-EXQ-689 | GAP-A readiness PASS; both levers engaged | grading-non-vacuity gap-spread 0/3 (regression uncomputable) | F-gap pinned in the near-tie bin -> `substrate_not_ready_requeue` |

**Uniform failed-criterion class:** discrimination. **Uniform non-vacuity controls:** PASS. The
committed DV is **non-degenerate** in every case (committed-class entropy ranges 0.0-1.21 across
seeds -- it can and does move; it simply does not move *between arms within a seed*). The one genuine
degeneracy (485h seed2 C2 sep-ratio) was caught separately by `criteria_non_degenerate` and is
already excluded.

---

## 2. Discrimination gate (Step 3) -- the load-bearing filter

**This is a convergent-recurrence cluster, NOT classic divergent-signature granularity debt.** The
skill's auto-detector keys granularity debt on *distinct* failure-signature count across a cluster.
Here the four channels share an **identical** fingerprint (bias reaches E3 authority; committed entropy
floor-locked between arms). So the classic detector would **not** flag this -- and the cluster autopsy
Section 9 records exactly that: the default autopsy reading is "NOT debt; convergent signature, shared
root the claims do not own; the four-roots phase-0 decomposition already discharged the divergent
debt."

So why does this clear the gate at all? Because the decomposition is **not** motivated by circling
distinct failures. It is motivated by the **claim's own conjunctive structure**: MECH-439's text
bundles three logically-separable assertions that the two live readings (cluster autopsy Section 6)
pull apart. This is **compositional debt within a single claim**, and the gate it must clear is
**independent-testability of the conjuncts**, exactly as the nomination instructs.

Run the four exclude-classes against the cluster:

| Exclude class | Verdict | Why |
|---|---|---|
| vacuous-criterion / test-design debt | **NOT** this | Committed DV non-degenerate in every member; the one degenerate sub-criterion already excluded. The signature is genuine. |
| substrate-not-ready | **NOT** this *at the MECH-439 level* | MECH-439 is explicitly `standard` / V3-tractable now -- the lever exists and is testable (`e3_selector.py` `_gap_scaled_commit_pick` + conflict-graded top-k, both built). The four *downstream* channels are `substrate_ceiling`, but that is because they are gated behind a ceiling **they do not own** -- which is the decomposition's whole point, not a reason to exclude. |
| genuine single-point falsification | **NOT** this | MECH-439 is candidate and *strengthened* by the convergence (positive-adjacent), not falsified. Decomposing a wrong claim would be illegitimate; this claim is not wrong. |
| **compositional / independent-testability debt** | **THIS** (proceed) | The three conjuncts make *different, separately-falsifiable* predictions; one (existence) is already measured, the other two make **opposite** predictions on the same keystone experiment. See Section 3. |

**Gate result: PROCEED -- on independent-testability grounds, not on divergent-failure grounds.**
The honesty rail the nomination demanded: had this been auto-surfaced rather than user-nominated, the
convergent signature means it would (correctly) NOT have ranked as debt. The legitimate trigger here is
the conjunctive claim text + the two-reading fork, which the user identified directly.

---

## 3. Independent-testability proof (the gate's actual content)

Each conjunct is independently testable, and Children 2 and 3 are mutually-exclusive rivals sharing one
discriminating experiment -- the textbook shape of a legitimate decomposition (rival mechanism claims +
a discriminator), distinct from manufacturing untested claims from a measurement bug.

| Conjunct | Independently testable? | Test / falsifier | Independent of the others? |
|---|---|---|---|
| **Existence/bound** (Child 1) | Yes -- already measured | V3-EXQ-571 variance decomposition: F = 88-89% of E3 committed-selection temporal variance, baseline AND full-diversity-stack arms | Measures the *current* selector only; asserts nothing about whether any lever fixes it |
| **Lever-sufficiency** (Child 2) | Yes | V3-EXQ-689a: ARM_A1B1 (gap-scaled k + commit-T) committed-class entropy **strict-above BOTH gap-blind controls** on >=2/3 seeds, lift **gap-concentrated** (correlates with per-tick top-F gap), WITHOUT reducing F's variance share | Predicts the bound is *locally circumventable*; opposite of Child 3 |
| **Residual-ceiling** (Child 3) | Yes | 689a read the other way (uniform / no lift => near-ties levers cannot exceed the proposer ceiling) **plus** a positive test of the rung-2 lever: rank-preserving F->eligibility demotion lifts committed entropy where the near-ties lever did not | Predicts the bound is *not* circumventable by a near-ties lever; opposite of Child 2 |

The phase-0 synthesis's pre-registered 689a-outcome routing table (`conversion_ceiling_phase0_synthesis_2026-06-18`,
"689a result -> routing") already maps the three outcomes onto exactly this Child-2-vs-Child-3 fork:

- *ARM_A1B1 strict-above both gap-blind controls, gap-concentrated* -> conflict-grading load-bearing
  -> **Child 2 supported** (MECH-439 lever-sufficiency confirmed; ceiling lifts; downstream retests release).
- *Lift uniform (gap-blind controls match)* -> "just a bigger shortlist" -> escalate rung 2
  -> **Child 3 favoured** (near-ties insufficient; F-eligibility demotion is the real lever).
- *No lift (ARM_A1B1 ~ collapsed controls)* -> structural bound caps below proposer ceiling -> rung 3+
  -> **Child 3 supported in its strong form** (no near-ties lever suffices).
- *Non-vacuity floor miss* -> `substrate_not_ready_requeue` -> not a verdict; re-queue (neither child moves).

This is why the synthesis must **consume** 689a rather than precede it: the same manifest that
adjudicates 689a is the manifest that decides which of Children 2/3 is `supports` and which is
`weakens`. Registering them before 689a would be registering two claims whose evidence is one
unread experiment away.

---

## 4. The common thread (Step 4)

One sentence: **every member fails because a single primary score (F) monopolises ~88-89% of the
committed-argmax selection variance, so each independently-matured bias stream has genuine authority
*at the accumulator* but no authority *at the committed selection* except in the rare near-tie -- the
broad claim names the bound but does not separate (a) that the bound exists from (b) whether a
near-ties lever can convert through it from (c) whether the bound is hard below the proposer ceiling.**

That (a)/(b)/(c) separation is the missing structure. It is not a missing *mechanism* (the biology is
one mechanism -- the BG action-selection bottleneck); it is a missing *epistemic decomposition* of one
claim into a shown fact + two rival forward mechanisms.

---

## 5. Lit grounding (Step 5)

Per "biology before formal definitions," the missing-mechanism content must be lit-grounded before
registration. **Substantial grounding already exists in the registry**, and the cluster autopsy
Routing 2 commissions a dedicated consolidating pull:

| Child | Mechanism to ground | Existing grounding (already filed) | Gap to fill before registration |
|---|---|---|---|
| **Child 1** (existence/bound) | none -- it is a *measured fact* (V3-EXQ-571), not an imported mechanism | n/a (the measurement is the warrant) | none |
| **Child 2** (conflict-graded shortlist `k=f(F-gap)`, BG hyperdirect/STN analog) | STN conflict-graded decision-threshold "hold" via the cortico-STN hyperdirect pathway | **SD-034 / Cavanagh & Frank 2011** (Nat Neurosci; STN conflict-graded threshold, causal via DBS reversal -- `targeted_review_sd_034/.../cavanagh_frank2011`, supports 0.72); **Q-019** Aron 2007 / O'Reilly & Frank 2006 / Brittain & Brown 2013 (STN hyperdirect stopping & global-NoGo) | the dedicated **`targeted_review_MECH-439`** consolidating pull (cluster autopsy Routing 2; TASK_CLAIMS `lit-pull-mech-439-bg-hyperdirect`) -- consolidate the above onto MECH-439 + add Frank BG/STN models, Bogacz/Cohen threshold-adaptation, Wei/Rubchinsky STN-conflict |
| **Child 3** (residual-ceiling; rank-preserving F->eligibility demotion / divisive normalization / QD) | maintain diversity against a dominant fitness gradient; divisive normalization of the dominant score | **MAP-Elites / Mouret & Clune 2015** (`targeted_review_rl_diversity_monostrategy_curriculum`, CDQ-003) for the QD/maintain-diversity side | a divisive-normalization anchor (Carandini & Heeger canonical-normalization) is **not yet filed specifically** -- file before Child 3 registration |

**Reading:** Child 2's mechanism is the *good inverse* of the SD-003 failure mode -- a faithful
biological translation (BG hyperdirect conflict-grade) with a missing dependency, not a formal import
with a wrong mechanism (cluster autopsy Section 4). The lit warrant for Child 2 is already strong;
the Routing-2 pull consolidates it under a MECH-439-specific review. Child 3's QD side is grounded;
its divisive-normalization side needs one targeted entry. **Neither blocks this proposal** (registration
is deferred to post-689a regardless); both should be confirmed filed at the registration step.

---

## 6. The decomposition PROPOSAL (Step 6)

### 6.1 MECH-439's fate: **NARROW-AND-RETAIN as the umbrella + existence claim; spawn two candidate children**

Recommended disposition (one of two presented; see 6.5 for the alternative):

- **MECH-439 narrows to its existence/bound content (Child 1)** and is **retained as the umbrella**
  anchoring the two children. Its load-bearing evidence (V3-EXQ-571) *is* the existence fact, so the
  narrowed MECH-439 is **`shown`-eligible** (exp_conf from 571) rather than a perpetual candidate
  bundling two unanswered questions. This keeps MECH-439's id, history, and the downstream `blocked_by`
  / substrate-entry linkage intact (no four-channel re-pointing surgery), matching the ARC-080
  umbrella precedent the skill cites.
- **Two NEW candidate children** carry the genuinely-open forward mechanisms. This avoids
  manufacturing a redundant separate Child-1 claim (anti-proliferation rail: the existence fact is
  already MECH-439's shown core).

### 6.2 Child 1 -- existence/bound (== MECH-439, narrowed)

| Field | Value |
|---|---|
| id | **MECH-439** (retained; narrowed) |
| claim_type | `mechanism_hypothesis` (unchanged) |
| subject | `selection.primary_score_variance_monopoly` (unchanged) |
| one-line claim | "The primary harm/goal score F monopolises ~88-89% of E3 committed-selection temporal variance (V3-EXQ-571: 0.886 baseline, 0.894 with the full diversity stack -- the stack does not dent F's share), so any modulatory / within-class / rule-bias channel has authority at the accumulator but acts on the committed argmax only at near-ties; F's variance share **bounds** achievable committed-action diversity. (This claim asserts the *bound*; whether a near-ties lever converts through it = MECH-447; whether the bound is hard below the proposer ceiling = MECH-448.)" |
| epistemic_category | `standard` (unchanged) |
| epistemic_stance | derives to **`shown`** once exp_conf from 571 attaches (currently candidate -> on narrowing + indexer, promotable to provisional on the 571 evidence) |
| what_would_answer | already answered (571 variance decomposition); falsifier = an E3 variance decomposition showing F < ~0.85 of committed-selection variance, or the diversity stack materially denting F's share |
| depends_on | ARC-065, MECH-309, ARC-062, MECH-294 (unchanged) |
| children | MECH-447, MECH-448 (new umbrella links) |
| lit grounding | n/a (measured fact) |
| cluster evidence | the *shared root* every member is gated behind; V3-EXQ-571 is the direct measurement |

### 6.3 Child 2 -- lever-sufficiency (NEW)

| Field | Value |
|---|---|
| id | **MECH-447** (placeholder -- "next free at registration time"; current max is MECH-446) |
| claim_type | `mechanism_hypothesis` |
| subject | `selection.conflict_graded_shortlist_conversion` |
| one-line claim | "A conflict-graded near-ties shortlist (`k = f(top-F gap)`, the BG hyperdirect-hold analog) plus a gap-scaled commit-T lifts committed-action-class entropy strict-above gap-blind controls -- the lift being **gap-concentrated** (correlated with per-tick top-F gap) -- WITHOUT reducing F's E3 variance share; i.e. the F-bound is locally circumventable at near-ties by a conflict-graded selection lever." |
| epistemic_category | `standard` (V3-tractable; the lever is built and 689a tests it) |
| epistemic_stance | `believed` (candidate; becomes `shown`/`weakens` on the 689a manifest) |
| what_would_answer | **V3-EXQ-689a:** ARM_A1B1 (gap-scaled k + commit-T) committed-class entropy strict-above BOTH gap-blind controls (ARM_FIXED_KMAX + ARM_FIXED_HOT_T) on >=2/3 seeds AND the lift gap-concentrated (per-gap-bin entropy slope negative, more negative than fixed-k ARM_A0B0). Refuted if the lift is uniform (gap-blind controls match) or absent. |
| depends_on | MECH-439 (umbrella/parent), MECH-294 (selection-authority substrate), ARC-062 (rule-apprehension selector half), MECH-260 (the conflict-signal leg) |
| lit grounding | SD-034 Cavanagh & Frank 2011 (STN conflict-graded threshold) + Q-019 Aron/O'Reilly-Frank/Brittain-Brown; consolidated by `targeted_review_MECH-439` (Routing 2) |
| cluster evidence | the 569i top-k partial-rescue (channel-specific liftability existence proof; PASS 2/3, thin margin) is the *optimistic* prior for this claim; the four floor-locked channels are what it must convert |

### 6.4 Child 3 -- residual-ceiling (NEW)

| Field | Value |
|---|---|
| id | **MECH-448** (placeholder -- "next free at registration time") |
| claim_type | `mechanism_hypothesis` |
| subject | `selection.near_ties_lever_residual_ceiling` |
| one-line claim | "A near-ties selection lever (conflict-graded shortlist / gap-scaled commit-T) caps committed-action-class entropy **below the proposer's own ceiling** regardless of tuning, because it can only act in the rare near-tie while F monopolises the rest; only a **direct rank-preserving F->eligibility demotion** (F removed from the final argmin, used as a graded eligibility envelope only) lifts committed entropy through the bound." |
| epistemic_category | `standard` now, with a likely `substrate_ceiling` re-tag IF 689a shows the strong no-lift form pushes the fix to the V4-leaning rungs (divisive-norm / output-null / QD-archive) -- decide at registration on the 689a outcome |
| epistemic_stance | `believed` (candidate; the pessimistic Reading-2 rival) |
| what_would_answer | Two-part: (i) **V3-EXQ-689a** uniform/no lift (gap-blind controls match ARM_A1B1, or ARM_A1B1 ~ collapsed controls) supports the cap; (ii) a **rung-2 experiment** (rank-preserving F->eligibility demotion, "build owed only if reached" per phase-0 action ladder) lifting committed entropy strict-above the near-ties-lever arms confirms the demotion is the operative lever. Refuted if the near-ties lever already achieves the proposer ceiling (Child 2 wins) OR if F-eligibility demotion fails to lift where the near-ties lever failed. |
| depends_on | MECH-439 (umbrella/parent), MECH-294, ARC-065 (the diversity-generation pathway the bound caps) |
| lit grounding | MAP-Elites Mouret & Clune 2015 (QD / maintain-diversity-against-dominant-gradient, CDQ-003); divisive-normalization anchor (Carandini & Heeger) to be filed before registration |
| cluster evidence | the *non-transferring* 569i rescue (channel-specific, did NOT generalize to CRF/OFC/threat/dACC) is the prior that a near-ties lever may be intrinsically local; the phase-0 "thin margin" caveat (569i 0.711 vs proposer 0.650, ~0.06 nats) is the quantitative seed |

### 6.5 Alternative disposition (for the user to weigh)

**Pure umbrella + three separate children.** MECH-439 becomes a bare umbrella; Child 1 is registered
as its *own* new claim (e.g. MECH-447 existence) alongside Child 2 (MECH-448) and Child 3 (MECH-449).
- *Pro:* symmetric; each conjunct is a first-class claim.
- *Con:* manufactures a separate Child-1 claim that duplicates MECH-439's already-shown existence core
  (mild proliferation); requires re-pointing the four downstream `blocked_by` links + the
  `f_dominance_conversion_ceiling` substrate entry from MECH-439 to the new umbrella. The recommended
  6.1 disposition avoids both.

### 6.6 Supersession / narrowing summary

- **No supersession.** MECH-439 is narrowed (its title/notes rewritten to the existence/bound +
  child-pointers), not superseded. Its history stays informative.
- **MECH-447, MECH-448** are *new* candidate children (the open forward mechanisms), wired
  `depends_on: MECH-439`.
- The four downstream channel claims (MECH-309/ARC-062, SD-033b/MECH-263, SD-032b/MECH-258/MECH-260,
  SD-037) are **untouched** -- they stay `substrate_ceiling` / `pending_retest`, gated behind the same
  689a keystone, none re-queued on the current selector.

---

## 7. Registration trigger + 689a-outcome -> child-disposition map (Step 7, deferred)

**No `claims.yaml` edit in this session.** Registration fires only after BOTH: (a) the 689a manifest
lands and is adjudicated, and (b) per-child user approval (AskUserQuestion). At that point the 689a
outcome sets the children's initial evidence direction:

| 689a outcome | Child 1 (MECH-439) | Child 2 (MECH-447) | Child 3 (MECH-448) |
|---|---|---|---|
| ARM_A1B1 strict-above both gap-blind controls, gap-concentrated | `shown` (571) | register + **supports** (lever-sufficiency confirmed) | register `believed` (rival not needed; park or low-priority) |
| Lift uniform (gap-blind controls match) | `shown` (571) | register + **weakens** ("just a bigger shortlist") | register + **favoured** -> rung-2 (F->eligibility demotion) becomes the live test |
| No lift (ARM_A1B1 ~ collapsed controls) | `shown` (571) | register + **weakens** | register + **supports (strong form)**; likely `substrate_ceiling` re-tag -> rung 3+ (V4-leaning) |
| Non-vacuity floor miss (`substrate_not_ready_requeue`) | `shown` (571) | hold (re-queue 689b); register deferred again | hold; register deferred again |

Registration steps when triggered (per skill Step 7): TASK_CLAIMS claim covering
`docs/claims/claims.yaml` + `docs/assets/data/claims.json` + this planning doc; allocate ids by max +
recent `git log` at write time; wire the umbrella; confirm the Section-5 lit entries are filed
(`targeted_review_MECH-439` + the Carandini-Heeger divisive-norm anchor for Child 3);
`python scripts/build_claims_json.py`; pathspec-limited commit; `git show --stat HEAD`; push `HEAD:master`.

Also apply the **derive-only reconcile** in the same pass (REE_assembly CLAUDE.md): a MECH-439
narrowing that flips its stance to `shown` needs the owning closure node
(`behavioral_diversity_isolation:GAP-I`) prose + `decision_state` reconciled by hand / `record_decision.py`.

---

## 8. Hand-off + close (Step 8)

- **This session:** wrote this proposal only. No claims.yaml edit, no experiment, no promotion.
- **Blocked-on:** V3-EXQ-689a manifest (status `claimed`, no result row as of 2026-06-20T08:52Z).
- **Next actions (carried as chips / existing claims):**
  1. 689a completes -> adjudicate -> return here, present Children per the Section-7 map, get per-child
     approval, register.
  2. `targeted_review_MECH-439` lit-pull (already an active TASK_CLAIMS claim) consolidates Child 2's
     grounding; add a Carandini-Heeger divisive-norm entry for Child 3 before its registration.
- **Discipline note:** the discrimination gate PROCEEDED on *independent-testability* grounds for a
  *convergent* (not divergent) cluster, justified by the conjunctive claim text + the two-reading fork,
  and user-nominated rather than auto-surfaced. The anti-proliferation rails held: every proposed child
  carries a `what_would_answer`; Child 1 reuses MECH-439's id rather than manufacturing a redundant
  claim; Children 2/3 are mutually-exclusive rivals with a single pre-registered discriminator (689a),
  not speculative spawn.
