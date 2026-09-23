# Claim synthesis -- "the DV could not move under this experiment's own manipulation"

**Date:** 2026-09-23
**Session:** `dvreach-synthesis-20260923` (claim-synthesis worker, fleet Orchestrator
`orchestrate-20260922-subagent-wave`)
**Posture:** PROPOSAL ONLY. Nothing written to `claims.yaml`, `experiment_queue.json` or
`substrate_queue.json` (all three contended). One file written (this one) + one governance flag.
**Motivating observation (from the Orchestrator):** four separate REE experiment designs stopped
on 2026-09-23 for what looked like one structural reason -- nobody checked whether the chosen
dependent variable could move under that experiment's own manipulation, at the operating point,
before the design was committed.

**Headline verdict: the observation is right about three of the four cases and those three are
ALREADY OWNED -- by a rule that landed the day before, and which CAUGHT one of them.
The fourth case is two different defects, neither of which is DV-reachability. One of those two
is the only genuinely unowned finding here, and it is narrower and cheaper than the framing
that produced it.**

---

## 0. Summary of calls

| Question | Call |
|---|---|
| One pattern or several? | **Two patterns and a scope finding.** Cases 1/2/3 are one pattern; Case 4 contains two *different* defects of opposite error polarity, one of which is not a reachability defect at all. |
| Is the pattern unowned? | **No, for cases 1/2/3.** `/queue-experiment` Step 2.5d + `/implement-substrate` Step 3h + the `substrate_queue.json` three-field schema, all landed 2026-09-22 under `dec-20260921T044147-GOV-UNWRITTEN-1` option (b), name this exact shape (`INERT`) and its two sub-shapes. Case 2 was **refused by Step 2.5d itself**. |
| Difference from GOV-PATHVALID-1 | It is **not** a sharpening of GOV-PATHVALID-1. That rule guards the *upstream* half (can the organism reach the manipulated state endogenously?) against a *false-positive* reporting move. This guards the *downstream* half (given the state IS manipulated, can the readout register it?) against a *false-negative*. Detail in sec. 4. |
| New claim proposed? | **One**, narrow: `GOV-CRITBAR-1` (provisional id) -- a threshold criterion must be denominated on THIS run's own control arm. Sec. 6. |
| Rule/skill change proposed? | **One sharpening** of Step 2.5d / Step 3h to cover `claim_ids: []` diagnostics. Chipped, not made -- with the GOV-HELDOUT-1 requirement stated. Sec. 7. |
| Mechanical or judgement? | Measured, sec. 8. A **corpus-wide retrospective detector is not buildable** (0.8% computable). A **per-run design-time assertion is** (100% available by construction). |

---

## 1. Verification of the four cases

Every figure below was re-derived from the cited source. Corrections to the Orchestrator's
summary are marked **[CORRECTION]** and are not cosmetic -- two of them change what the case
is evidence of.

### Case 1 -- INV-069 behavioural leg, GatedPolicy channel. CONFIRMED, with two corrections.

Confirmed: `gated_score_bias = w*head_0(features) + (1-w)*head_1(features)`; `z_self` reaches the
bias only through the scalar discriminator weight `w`; candidate features bit-identical across all
32 candidates (pairwise distance max `0.000000e+00`); structural ceiling 0/73 ticks; rank
invariance is a proof, not a power problem.
Sources: `.scratch/inv069_findings_20260922.md` Part 2, GFLAG-0414 (both read in full).

**[CORRECTION 1] The cited line range is the docstring, not the code.**
`ree-v3/ree_core/policy/gated_policy.py:19-23` is the module docstring's *statement* of the
architecture. The implementation is at `:528-536`, and the composed bias is additionally
**clamped** to `+/-bias_scale`. The docstring is accurate; the proof rests on the code.

**[CORRECTION 2] The proof is two-part, and only one part is architectural.**
(a) `z_self` entering only through a scalar `w` makes the reachable bias family one-dimensional:
`bias(w) = h1 + w*(h0 - h1)`. That alone does **not** give a 0/73 ceiling -- a 1-D family can still
re-rank. (b) Candidate features being bit-identical makes the bias *constant across candidates*,
and a constant additive term is rank-invariant by construction. **(b) is an operating-point fact,
not an architectural one** -- it is the V3-EXQ-614e monostrategy collapse
(`cand_world_pairwise_dist = 0.0000`), reproduced. Applying that autopsy's documented remedy
raises the structural ceiling to **8/73 without the normaliser and 73/73 with
`normalize_score_bias_to_e3_range=True`** -- the Orchestrator's summary cites only the 8/73
figure, which understates how far the ceiling moves. Realised movement stays at 1/73.

This matters for the synthesis: **reachability is a property of the tuple (manipulation, channel,
DV, operating point), not of the code.** A static read of `gated_policy.py` cannot answer it.

**Caveat carried forward, from the source and omitted by the summary:** the pilot trained E1/E2
only, so every `|dw|` figure characterises an **untrained** discriminator (`GatedPolicy` has a
dedicated optimizer, LR 5e-4, V3-EXQ-543b). Finding 1 is training-independent; the realised 1/73 is
not, and is not a verdict.

### Case 2 -- INV-069 coherence leg, arm (b) frozen-self. CONFIRMED exactly.

Confirmed at source: `ree-v3/ree_core/hippocampal/module.py:3813-3817` (line numbers exact) --
`denom = ||z_curr|| + eps`; `err = ||z_curr - z_prev|| / denom`; `score = clip(1 - err, 0, 1)`;
`vs = (1-tau)*vs_prev + tau*score`, `tau = 0.1`. Freezing `z_self` makes `z_curr == z_prev`
exactly, so `err = 0` and `score = 1.0` -- the instrument's maximum. Freeze verified engaged
(frozen `||dz_self||max = 0.00000000` in all 12 cells, seeds 42/43/45 x windows 5/10/20/40);
freeze-minus-live delta **positive in 12/12 cells, +0.0023 to +0.0122**, against unmanipulated
within-run variability ~0.005-0.008. Verdict aliasing confirmed: a small positive delta satisfies
both the CONFIRMING and the FALSIFYING clause of the same falsifier.
Source: GFLAG-0428 (`REE_assembly` `abc53c3873`), read in full.

**[REFINEMENT] "Structurally invariant" is the wrong word; "sign-locked at the ceiling" is right.**
The DV is not invariant -- it moves by +0.002 to +0.012. It is *monotonically pinned toward the
instrument's maximum by construction*, and the movement is inside the DV's own noise band. The
distinction matters because an invariant DV is caught by a zero-variance check and a sign-locked
one is not.

**Second finding in GFLAG-0428 that the summary omits and that strengthens the case:** the LIVE
control also saturates at longer windows (mean 0.9908 at window 20, 0.9925 at window 40; 17.5% of
live ticks already exceed 0.99). So the falsifier's *own* non-degeneracy precondition ("it
saturates at 1.0 when z_self is constant, so a pinned readout detects nothing") bites the control
arm too -- which the 2026-09-22 pilot's episode-averaged 0.958/0.965 concealed. **A non-degeneracy
precondition that is checked on the manipulated arm but not on the control is itself a negative
instrument**; this is a direct instance and it anticipates Case 4/A3.

### Case 3 -- INV-023 DV-1, residue specificity. CONFIRMED, with one material correction.

Confirmed: bandwidth 1.0 vs visited-`z_world`-cloud max pairwise distance **0.1249** (median
0.0648) = 8.0x, so the two most distant reachable points read `exp(-0.1249^2/2) = 0.9922`, 0.8%
apart. At production bandwidth, seed 0 reads **ratio 1.006675** while rank AUC on the same
contexts, same field, same moment is **0.8066** against a label-shuffled control of **0.4587**.
Sources: `.scratch/inv023_readout_form_20260923.txt`, `.scratch/inv023_repro_sep_20260923.txt`,
GFLAG-0415, `substrate_queue.json` entry `residue-field-kernel-resolution` (whose
`implementation_hint` carries the 0.1249 figure, measured 2026-09-17 by igw-242 under GFLAG-0337).

**[CORRECTION 3] "The discrimination was always there" holds on ONE of the two seeds.**
Seed 1 reads AUC **0.5737** at bw=1.0 and never exceeds 0.5940 at any bandwidth down to 0.065 --
there is no discrimination for the readout to have hidden. On seed 1, GFLAG-0415's diagnosis
stands unmodified: the root cause is the observation->`z_world` interface (harm context is not
encoded separably; centroid separation 0.0806 is *smaller* than the within-cluster spread of both
clusters). **So Case 3 is readout-saturation on seed 0 and genuine non-separability on seed 1** --
two causes, seed-dependent, and the case supports the readout-saturation reading as an *existence
proof*, not as the general account of INV-023.

Note also two different distances are in play and both are correct: 0.1249 is the max pairwise
distance of the whole visited cloud (bandwidth 8.0x); 0.1878 / 0.0806 are the harm-vs-safe
*centroid* separations (bandwidth 5-12x). They are not interchangeable.

### Case 4 -- V3-EXQ-1075, arms A1 and A3. CONFIRMED exactly, and it is TWO defects.

Confirmed: A3's bar is `conv_rel_drop >= 0.99`; ARM_OFF reads **0.98466 / 0.98486 / 0.99163**,
clearing on 1 of 3 seeds. A1's bar is a bare `ratio > 1.0`; the three A1-passing ratios at margin
0.50 are **1.0109 / 1.0026 / 1.0015** on heads with `skill_vs_identity` **-431 / -563 / -675**.
Source: `REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-1075_2026-09-23.md`, status
**confirmed by the user 2026-09-23T07:52:00Z** (Step 8 gate), red-teamed on `fable`, five contested
findings all accepted.

**[CORRECTION 4] "PASS was unreachable by construction" is the autopsy's phrasing and is slightly
strong.** ARM_OFF clears 0.99 on 1/3 seeds, so the precise statement is the autopsy's own next
sentence: *a margin preserving reconstruction exactly at OFF quality would still fail A3 on two
seeds*. The defect is that the bar measures **baseline convergence variance**, not the
manipulation.

**[CORRECTION 5, the load-bearing one] A1 is not a reachability defect. It is its mirror image.**
A3 fails because the PASS region is (nearly) empty at this operating point -- a **false-negative**
route. A1 fails because the PASS region *contains a state in which the mechanism is destroyed* --
a **false-positive** route. `ARM_OFF` ratios are 0.83/0.88/0.71, so A1 *can* fail; there is nothing
unreachable about it. Merging A1 into a DV-reachability pattern would put two opposite error
directions under one rule, which is precisely the over-merge the Orchestrator warned against.

---

## 2. Is it one pattern? No -- two, plus a scope finding

### Pattern A -- "the readout cannot register the manipulation at this operating point"

Cases **1, 2, 3**. The unifying statement, and it is a real one:

> Every pre-registered criterion is a map `(manipulation, operating point) -> DV value -> verdict`.
> Pattern A is the family in which the first arrow is degenerate: the DV's attainable range under
> this experiment's own manipulation, at the operating point it will run at, does not contain
> values the criterion can distinguish. It is provable from the arithmetic, not a power question.

Three sub-shapes, all genuinely instances:
- **A-i, channel-constant:** the manipulation reaches the DV only through a term that is constant
  in the DV's own contrast dimension (Case 1: candidate-constant additive bias -> rank-invariant).
- **A-ii, numerator-annihilating / sign-locked:** the manipulation zeroes the very increment the DV
  is built from, pinning it at an instrument extremum with a sign locked by construction (Case 2).
- **A-iii, resolution-below-effect:** the DV varies, but the readout's resolution parameter is
  coarser than the spread it must resolve, compressing the contrast into its own noise (Case 3,
  seed 0).

**Pattern A is ALREADY OWNED.** See sec. 3.

### Pattern B -- "the decision boundary was never calibrated against this run's own control"

Case **4/A3**, and -- as a second instance found during verification -- the LIVE-control saturation
in Case 2's second finding. The statement:

> A threshold criterion partitions DV values into PASS and FAIL. Pattern B is the family in which
> the DV moves perfectly well but the *threshold* sits where the run's own control arm already sits
> (or worse), so the criterion is reporting baseline variance rather than the manipulation's effect.

This is **not** Pattern A: the DV is live, the instrument discriminates, the manipulation is
reachable. Only the bar is misplaced. It is the one genuinely unowned finding in this set (sec. 5).

### Pattern C -- "the PASS region admits a pathological instrument state"

Case **4/A1**. Opposite error polarity to A and B. **Recommendation: do not register this as a new
claim.** It is already covered in practice by the conjunction of two existing rules -- the
effect-size PASS-gate discipline (`margin = max(k*sd(delta), ABS_FLOOR)`, never a bare inequality)
and CLAUDE.md's General Rules requirement for an explicit **cannot-determine CATEGORY** on any
negative instrument. The autopsy's own instrument finding #1 states the fix in exactly those terms
("return `cannot_determine` when `skill_vs_identity` is materially worse than the control's, and
require a ratio *margin* rather than a bare `> 1.0`"), and there is a **live open decision chip**
in front of the user for the specific threshold
(`chip-decision-20260923-1075a-a1-margin-bar`). Registering a general claim over a live decision
would duplicate an owner, not add one.

---

## 3. Pattern A is already owned -- the ownership check, redone by subject

The Orchestrator checked 56 GOV-* ids (there are **55**) and read the three nearest. Redone here by
subject and full text over all 55, plus the skill/pipeline layer the id search does not reach.

**`/queue-experiment` Step 2.5d, "Falsifier-runnability trace", landed 2026-09-22 under user
decision `dec-20260921T044147-GOV-UNWRITTEN-1` option (b).** Quoting the shipped step:

> "**INERT.** The event, DV and instrument all exist and are reachable, but at the operating point
> the experiment will use, the DV **cannot move**, or the instrument **cannot discriminate**. ...
> Ask specifically: at the magnitudes this substrate actually produces today, is the bar attainable
> in both directions?"

That is Pattern A, including both of its failure verbs: "the DV cannot move" is A-i/A-ii, "the
instrument cannot discriminate" is A-iii. The step ships with a GOV-HELDOUT-1 check of **4
non-degenerate cases + 1 negative control**, all INERT-shaped (GFLAG-0346, GFLAG-0376, GFLAG-0348,
GFLAG-0351), and its own recorded scope finding is that INERT is the *common* shape.

**`/implement-substrate` Step 3h** is the same trace on the build side (`REE_Working` `0a4fe3efa`).

**The `substrate_queue.json` schema already carries the trace as three required fields** --
`falsifier_requirement_satisfied`, `event_or_manipulation_produced`, `dv_or_instrument_exposed` --
and the `residue-field-kernel-resolution` entry (Case 3's own substrate row) uses them to state a
**pre-computable release condition**: `max_pairwise(z_world_buffer) / residue.kernel_bandwidth >= ~2`.

**Decisive evidence of ownership, not merely of overlap: Case 2 was caught BY the owner.**
GFLAG-0428's first line reads *"V3-EXQ-1078 REFUSED at /queue-experiment Step 2.5d
(falsifier-runnability, INERT)"*. Cases 1 and 3 were caught by campaign pilots on 2026-09-22, the
same day 2.5d landed and under the same campaign discipline.

**So the correct reading of the Orchestrator's observation is the inverse of its framing.** It is
not that "nobody had checked". Somebody had just built the check; it fired on one of the four and
the campaign's pilot discipline caught two more. What needs explaining is not the three catches --
it is the one miss.

### The pre-flight axes are close but are NOT the owner of Pattern A

Checked directly, as instructed. `metaworker-orchestrate` SKILL.md 1d-iii pre-flight:
- **(a2) "instantiated is not armed"** (landed today, `REE_Working` `fb9f599bc5`) and
  **(a) substrate path** -- both interrogate the **producer's liveness**. Confirmed: neither asks
  whether the DV can register the manipulation. The Orchestrator's reading of (a2)/(a3) is correct.
- **(b) "can the load-bearing criterion actually FAIL"** -- this is the **vacuous-PASS** guard
  (false positive). Pattern A is the opposite polarity. Closest of the four, still not it.
- **(c) "are the DV signals live in the regime used (not None, not floor-pinned) ... where the DV
  has a threshold, cite a recorded value from a landed manifest against it: a populated field is
  not a reachable one"** -- this is the nearest axis to *both* patterns, and **it is the axis Case
  4/A3 walked straight through.** A3's 0.99 bar *was* justified by a recorded value from a landed
  manifest: V3-EXQ-1073 reached 0.998 at the same `P0_STEPS` and LR. The axis as written licenses
  exactly that citation. See sec. 5.

---

## 4. How this differs from GOV-PATHVALID-1 (and why it is not a sharpening of it)

GOV-PATHVALID-1, `governance.epistemics.positive_control_production_path_traversal`:

> "A load-bearing positive control ... must traverse the production path it claims to validate.
> Directly injecting or mocking the state immediately downstream of a suspected causal edge can
> certify that a downstream consumer works GIVEN that state, but cannot certify that the production
> organism can reach that state via its own endogenous pathway."

Three independent differences:

1. **Opposite half of the causal chain.** PATHVALID guards *upstream* of the manipulated state:
   can the organism get there by itself? Patterns A and B guard *downstream*: given that the state
   HAS been set, can the readout register it, and is the bar in the right place? A design can
   satisfy PATHVALID perfectly -- Case 2's freeze hook is a verified, exactly-engaged manipulation
   of a real production variable -- and still be dead on both of the patterns here.
2. **Opposite error direction.** PATHVALID guards a **false positive**: a mocked-precondition PASS
   reported as full-pathway evidence. Patterns A and B guard a **false negative**: a design that
   will emit `weakens` (or an aliased verdict) against a claim it could never have supported.
   PATHVALID's own `what_would_answer` is explicit that it is a *reporting* rule, "VIOLATED BY: a
   manifest, autopsy, or claim note that **reports** a ... PASS as evidence the organism
   'possesses' ... a full pathway". Nothing in Patterns A or B is a reporting move; they are design
   defects that exist before anything is reported.
3. **Different bearer.** PATHVALID binds the *positive control's construction*. Pattern B binds the
   *threshold's denominator*.

**GOV-SHARPEN-1 applied, as instructed.** Its test is `C + B` versus `C + A`: a sharper formulation
is a refinement of the same claim when it follows from the canonical claim plus *already-accepted
background*, and a distinct claim when it needs a **new empirical assumption A** introduced at the
rotation. Fixing `B` non-circularly here: the registry's accepted background is the production
path, the substrate as built, and the `depends_on` commitments (GOV-FAILLOC-1, ARC-130).

- "A control's injected state may not certify the endogenous path" (PATHVALID) does **not** entail
  "a threshold must be denominated on this run's own control arm" under that `B`. The entailment
  requires a new empirical assumption **A: the same quantity, recorded in a different landed run's
  manifest, can differ materially from this run's own control arm at this operating point.**
- **A is not free background -- it is measured, in this corpus, in Case 4.** V3-EXQ-1073 recorded
  `conv_rel_drop` 0.998; V3-EXQ-1075's ARM_OFF, at the same `P0_STEPS` and LR, reads
  0.98466/0.98486/0.99163, with the cause unidentified in the driver's own record. Without A the
  new rule does not follow; with A it does.

**Therefore: a DISTINCT claim under GOV-SHARPEN-1, not a sharpening of GOV-PATHVALID-1.** Its
nearest relatives are GOV-PATHVALID-1 and GOV-UNWRITTEN-1, and it should be wired to both.

The *other* half of this work -- extending Step 2.5d's trace to `claim_ids: []` diagnostics -- goes
the other way under the same test: it applies an existing predicate to a new population and needs
**no** new assumption A. That is a **sharpening**, and it is therefore a skill-step edit, not a
claim (sec. 7).

---

## 5. The one thing that is genuinely unowned, and why Case 4 escaped

Case 4 is the only one of the four that was not caught by a pilot. Two independent reasons, both
verifiable:

**(i) Every gate in the family is CLAIM-KEYED, and V3-EXQ-1075 has `claim_ids: []`.**
Step 2.5d's trace is defined on "the claim's `what_would_answer` / pre-registered falsifier".
V3-EXQ-1075 is a *substrate-validation diagnostic* -- `claim_ids: []` deliberately,
`validates_substrate: SD-PP-B5-z-world-per-step-displacement-range` -- so there is no
`what_would_answer` for the trace to take as its subject, and its criteria (A1..A4) were authored
ad hoc in the driver. The same blindness is recorded independently in the autopsy's own mechanical
pre-routing section: *"C1 / C2 / C3 returned `inapplicable` (claim-keyed; `claim_ids: []`). Per the
skill's warning, inapplicable is not 'no fire' -- those checks were structurally blind."*

This is a **negative-instrument defect in the governance layer itself**, of exactly the class
`negative_instrument_audit_20260922.md` catalogues: a gate that returns "nothing to check" and a
gate that returns "nothing found" are indistinguishable to the session reading the verdict. And it
is concentrated on the *worst* population to be blind to -- claim-free substrate-validation
diagnostics are precisely the runs that set their own criteria with no registry review.

**(ii) The bar-denomination defect is outside every gate's subject matter anyway.**
Even had 1075 carried a claim, Step 2.5d would have traced the DV (`conv_rel_drop` -- live, moves
0.028 to 0.9947 across the ladder, no reachability problem at all) and passed it. The pre-flight's
(c) axis would have been satisfied by citing V3-EXQ-1073's landed 0.998. **No shipped gate asks
whether the bar is above the control's own value.**

**The unowned residue, stated as narrowly as the evidence supports:**

> A threshold criterion's bar must be validated against the **control arm of the run that will be
> scored against it**, not against the same quantity recorded in another run's manifest. A bar the
> control itself fails is measuring baseline variance, not the manipulation.

Two properties make this worth registering rather than noting: the predicate is
**definitionally a defect** (a correct design cannot have its control failing the PASS bar, because
then the bar is not measuring the manipulation), and it was **invisible to four independent gates**
that all fired correctly on their own subjects.

---

## 6. Draft candidate claim (NOT registered -- registration is `/governance`'s act)

House style matched against GOV-PATHVALID-1, GOV-MATCHAUX-1 and GOV-SHARPEN-1 (read in full).

```yaml
id: GOV-CRITBAR-1          # provisional -- allocate next free at registration time
claim_type: governance_rule
subject: governance.epistemics.control_denominated_criterion_threshold
polarity: asserts
status: candidate
epistemic_category: governance_rule
claim_level: governance
binds_at_version: v3
blocks_v3_green_board: false
v3_pending: false
depends_on:
  - GOV-UNWRITTEN-1        # the falsifier-runnability trace this sits beside
  - GOV-PATHVALID-1        # the upstream-half sibling in the routing-standard family
related_claims:
  - GOV-FAILLOC-1
  - GOV-MATCHAUX-1
  - GOV-INTERVENE-1
title: >
  A pre-registered threshold criterion is admissible only if its bar is denominated on the CONTROL
  ARM OF THE RUN THAT WILL BE SCORED AGAINST IT, at that run's own operating point -- not on the
  same quantity recorded in another run's landed manifest, and not on an absolute value taken from
  the design's rationale. A bar the run's own control fails, on a majority of its seeds, is
  measuring baseline variance rather than the manipulation's effect, and a PASS/FAIL returned
  against it is uninterpretable in BOTH directions: a FAIL is unattributable to the manipulation,
  and a PASS is a demonstration that the manipulation exceeded a threshold the control could not
  reach for unrelated reasons. This is a distinct defect from falsifier-runnability (the DV moves
  fine; the partition is misplaced) and applies with full force to runs carrying `claim_ids: []`,
  which set their criteria in the driver with no registry review.
functional_restatement: >
  Warn-and-record member of the routing-standard family (GOV-PATHVALID-1 production-path traversal,
  GOV-FAILLOC-1 failure-location triage, GOV-MATCHAUX-1 auxiliary-control admissibility,
  GOV-UNWRITTEN-1 falsifier-runnability). Those govern whether a manipulation is real, where a
  failure belongs, which control a result needs, and whether a DV can move. This one governs where
  the decision boundary is allowed to sit. TRIGGER = any queue entry, driver or autopsy pre-
  registering a numeric threshold on a quantity that a control/OFF/baseline arm also produces.
  REQUIRED = the control arm's realised value on the SAME statistic, from THIS run (or from a pilot
  at this run's operating point), recorded in the manifest alongside the bar. Changes no claim's
  status or confidence by itself; it is a design/admissibility gate.
what_would_answer: >
  NOT an empirical falsifier -- a DESIGN-VALIDITY rule, checkable by inspecting a run's criteria
  block against its own arm_results, never by any single REE experiment outcome.

  NON-DEGENERACY PRECONDITION: the criterion's statistic must be computable on the control arm. A
  criterion scored only on manipulated arms (a within-arm trajectory property with no control
  analogue) is OUT OF SCOPE, and must be recorded as out of scope rather than forced.

  VIOLATED BY: a scored manifest in which a load-bearing threshold criterion's bar is not cleared
  by the run's own control arm on a majority of seeds, where no `cannot_determine` was emitted and
  the resulting PASS or FAIL was carried into an autopsy, a claim-evidence row, or a substrate
  status flip.

  COMPLIANT: the control arm's value on the same statistic is recorded beside the bar; where the
  control fails its own bar, the criterion returns `cannot_determine` (the negative-instrument
  category, CLAUDE.md General Rules) rather than a verdict.

  CONFIRMING: (i) a prospective case in which recording the control's value against the bar
  CHANGES a design before it runs -- the bar is moved, or the criterion is withdrawn; (ii) a
  retrospective case in which a verdict already carried into governance is shown to be
  unattributable by this test alone.

  FALSIFYING -- and these are real, not ceremonial:
   (i) CORPUS SATURATION: a sample of >= 20 landed multi-arm manifests with threshold criteria
       shows designs already record the control's value against the bar as a matter of course, so
       the rule names an existing practice and adds nothing. (Partially probed already: see the
       0.8% machine-readability measurement in the source document -- that measures whether the
       check is AUTOMATABLE, not whether designers do it, and does not discharge this clause.)
   (ii) SOUND-VERDICT COUNTEREXAMPLES: >= 2 cases in which a design whose control failed its own
       bar nevertheless produced a verdict that later evidence vindicated -- which would show the
       defect is tolerable rather than disqualifying.
   (iii) INERT CEREMONY: across >= 3 prospective designs the rule never moves a bar, a criterion or
       a verdict relative to the existing effect-size-margin and non-degeneracy-precondition
       practice -- in which case demote toward superseded and let those stand.
   (iv) SCOPE COLLAPSE: if a revision of GOV-UNWRITTEN-1's Step 2.5d trace is extended to cover
       threshold denomination as well as DV reachability, this claim is absorbed by it and should
       be superseded rather than maintained in parallel.
  WHAT WOULD ACTUALLY REVISE IT: evidence that the binding constraint is not the bar's denominator
  but the absence of a pilot at the run's own operating point -- in which case the rule should be
  restated as a pilot requirement, which is a different and more expensive ask.
  READER NOTE: governance_rule about how the Assembly admits a criterion, not an empirical claim
  about REE cognition. No EXP-#### is to be minted against it.
evidence_seed:
  - V3-EXQ-1075 A3: bar conv_rel_drop >= 0.99; ARM_OFF 0.98466/0.98486/0.99163 (clears 1/3).
    failure_autopsy_V3-EXQ-1075_2026-09-23.md sec 5c, user-confirmed 2026-09-23T07:52:00Z.
  - GFLAG-0428 second finding: INV-069 arm (b)'s non-degeneracy precondition ("a pinned readout
    detects nothing") bites the LIVE control at windows 20/40 (0.9908/0.9925) -- the same defect
    on a precondition rather than a criterion.
```

**Honest statement of what would disconfirm it, as asked:** falsifying clause (i) is the one the
Orchestrator named -- a corpus sample showing designs routinely do this already. **It has not been
run, and it is not discharged by anything in this document.** The 0.8% figure in sec. 8 measures
machine-readability, which is a different question; a human reading 20 drivers would answer it
properly, and that is a `complicated (buildable)` node, not a `complex (probe-gated)` one. Clause
(ii) is the sharper test and I could not construct a candidate for it from this corpus.

---

## 7. Proposed rule/skill sharpening (CHIPPED, not made)

Not made here -- the hard constraints forbid editing any SKILL.md or CLAUDE.md, and correctly so.

**The change:** `/queue-experiment` Step 2.5d and `/implement-substrate` Step 3h define their trace
on "the claim's `what_would_answer` / pre-registered falsifier". Extend the subject to include a
run's **driver-authored criteria block** when `claim_ids` is empty -- i.e. the trace applies to
`validates_substrate` diagnostics, taking the substrate entry's
`falsifier_requirement_satisfied` / `event_or_manipulation_produced` / `dv_or_instrument_exposed`
triple as the subject in place of a `what_would_answer`. Those three fields already exist and are
already populated on the relevant rows (verified on `residue-field-kernel-resolution`).

Under GOV-SHARPEN-1 this is a **sharpening, not a new claim**: same predicate, new population, no
new empirical assumption A.

**GOV-HELDOUT-1 requirement, stated explicitly in the chip:** needs **>= 3 historical cases where
the OLD and NEW wording give DIFFERENT calls** -- i.e. `claim_ids: []` runs whose criteria a
falsifier-runnability trace would have stopped, and which the claim-keyed wording could not reach.
**Today's four cases are the motivating set and are therefore NOT admissible as held-out evidence.**
Cases 1/2/3 are additionally degenerate for this clause: all three carry claims (INV-069, INV-023),
so old and new wording give the same call on them. **If three non-degenerate cases cannot be found,
that is the finding** -- ship it scoped to the single V3-EXQ-1075 case with that stated, exactly as
the (a2) "instantiated is not armed" clause was shipped today.

---

## 8. Mechanical or judgement? -- measured, per case

**Do not build a general detector.** `negative_instrument_audit_20260922.md` recommends against one
for this class, CLAUDE.md restates it, and the reason applies here with full force: a general "can
this DV move?" scanner would itself be a negative instrument scanning a tree, and would fire on
correct designs constantly. The measurement below is what a general detector's coverage would
actually be.

### Measured: a corpus-wide retrospective detector is NOT buildable

Probe over the 500 most recently modified manifests under
`REE_assembly/evidence/experiments/` (flat JSON + run-pack `manifest.json`):

| structure present | count | % |
|---|---|---|
| DENOMINATOR: manifests sampled | 500 | 100% |
| `criteria` as a list | 129 | 25.8% |
| >= 1 numeric `threshold` in `criteria` | 48 | 9.6% |
| `arm_results` readable **on the same manifest** | 13 | 2.6% |
| control arm name-identifiable on the same manifest | **4** | **0.8%** |

**0.8% is the ceiling for any retrospective mechanical check**, and 99.2% would have to return
`cannot_determine`. A gate at that coverage is the negative instrument it is meant to prevent.
Machine-readable `criteria` blocks and machine-readable `arm_results` blocks are largely
**disjoint populations** in this corpus, which is itself a finding worth a separate look.

> **Self-check, recorded because the discipline demands it.** My FIRST run of this probe returned
> `control arm identifiable: 0 (0.0%)` -- because it tested `arm_results` as a dict when it is a
> list of dicts. That zero was a broken search, not a negative. It was caught by a canary
> (`arm_results` had been counted as present on 356/500 in an earlier pass, which is inconsistent
> with zero identifiable arms). Both numbers are reported. The corrected run also shows the arm
> naming convention is strong -- `ARM_OFF` alone appears 247 times across 278 distinct arm names --
> so name-based control identification is not the binding constraint; **co-occurrence of the two
> structures is.**

### Per case: what a check would have to ASK, and whether it can be mechanical

| Case | The question a check must ask | Mechanical? | Where it can live |
|---|---|---|---|
| **1** GatedPolicy | "Is the manipulation's only channel to the DV constant along the DV's own contrast dimension?" Concretely: `max_pairwise(candidate_features) == 0`, and `argsort(base + bias)` identical at the gating extremes `w=0` and `w=1`. | **Mechanical, but needs a PILOT RUN, not a static read.** Both quantities are operating-point facts; no read of `gated_policy.py` yields them. The endpoint check is a 2-point evaluation -- genuinely cheap once an agent is live. | A pilot protocol in `/queue-experiment` Step 2.5d, not a scanner. |
| **2** frozen-self V_s | "Does the manipulation appear in the DV's own definition in a way that annihilates or sign-locks it?" | **Judgement to NOTICE; mechanical to CONFIRM.** Reading `err = ||z_curr - z_prev||/...` and seeing that freeze sets the numerator to zero is three lines and an act of understanding -- no predicate expresses it. But the confirmation is a cheap protocol: run N cells, assert the manipulated-minus-control delta is **not sign-locked** and **exceeds the DV's own unmanipulated within-run sd**. That is exactly the 12-cell measurement the session ran. | Same place; the protocol is the shippable half, the noticing is not. |
| **3** residue kernel | "Is the readout's resolution parameter finer than the spread of the data it must resolve?" | **Fully mechanical, and already written**: `substrate_queue.json` `residue-field-kernel-resolution` states the release condition `max_pairwise(z_world_buffer) / kernel_bandwidth >= ~2`. Generalises to any kernel/bin/tolerance parameter. | Already owned; the general form is a per-readout release condition, not a detector. |
| **4/A3** bar vs control | "Does the run's own control arm clear this criterion's bar?" | **Fully mechanical, and the cheapest of the four** -- it needs only values the run already produces. **Near-zero false-positive rate by construction**: a correct design cannot have its control failing the PASS bar, because then the bar is not partitioning on the manipulation. This is the one check worth building. | **In the DRIVER at scoring time**, emitted into the manifest beside each criterion -- where both the bar and the control's value are in hand by construction (100% available). NOT a corpus scanner (0.8%). |
| **4/A1** destroyed head | "Does the PASS region contain a known pathological state of the instrument?" | **Judgement in general** -- "pathological" has no closed form, and a detector for it would need a health model per instrument. **Mechanical for the specific instance**: require a ratio margin (never a bare inequality) and a control-relative health condition on `skill_vs_identity`. | Already routed: autopsy instrument finding #1 + the open decision chip. |

**So: one of four (Case 4/A3) a tool could have caught with a genuinely cheap, low-false-positive
check. Two (Cases 1 and 3) are mechanical but require a pilot run rather than a static read, which
is the pilot discipline that already caught them. One (Case 2) is irreducibly judgement at the
noticing step, with a mechanical confirmation protocol behind it.**

The honest generalisation: **the noticing is judgement; the confirmation is mechanical.** That
asymmetry is why 2.5d is written as a question an agent must answer in prose with file:line
evidence, rather than as a predicate -- and why it should stay that way. The one exception is
Case 4/A3, where the *noticing* is mechanical too, because the defect is a comparison between two
numbers the run already computes.

---

## 9. Work-graph debt vocabulary for every unfinished node named here

| Node | Class | Why |
|---|---|---|
| Register `GOV-CRITBAR-1` into `claims.yaml` | `complicated (buildable)` | `/governance`'s act; the draft is complete, the registration is execution. |
| Run `GOV-CRITBAR-1` falsifying clause (i) -- corpus sample of >= 20 multi-arm designs | `complicated (buildable)` | A human reading 20 drivers. Expensive, not uncertain. |
| Find >= 3 non-degenerate held-out cases for the Step 2.5d claim-free-diagnostic sharpening | `complex (probe-gated)` | The probe is the search itself; a null result (none found) is the informative outcome and narrows the rule to single-case scope. |
| Build the A3 control-vs-bar assertion into driver scoring | `complicated (buildable)` | Predicate known, data in hand, ~zero design uncertainty. |
| Why `criteria` blocks and `arm_results` blocks are near-disjoint populations (25.8% vs 2.6% co-occurrence) | `puzzle (known rules)` | A missing fact about the manifest writers; one read of the schema/producers answers it. |
| Case 3 seed-dependence: readout saturation (seed 0) vs `z_world` non-separability (seed 1) | `complex (probe-gated)` | Two live causes; which binds is not determined by the two seeds in hand. |
| Whether a trained `GatedPolicy` discriminator changes Case 1's realised figure | `complex (probe-gated)` | Requires choosing an optimiser/objective/schedule, which is itself the circularity the INV-069 session refused -- probe first, do not build. |
| A general DV-reachability detector | **NOT a node.** Closed on measurement (0.8% coverage; `negative_instrument_audit_20260922.md`). Do not re-propose. |

---

## 10. Where the Orchestrator's framing was wrong (collected)

1. **"Nobody had checked."** Somebody had. The check landed 2026-09-22 (`/queue-experiment` Step
   2.5d, `/implement-substrate` Step 3h) and **refused Case 2 by name**. Three of four cases are
   evidence the rule works.
2. **"One structural reason."** Two, with opposite error polarity, plus a scope finding. Case
   4/A1 is a false-positive defect and does not belong in the set.
3. **Case 3's "the discrimination was always there"** holds on seed 0 only; seed 1 has none to hide.
4. **Case 1's 8/73 figure** omits the 73/73-with-normaliser figure and the untrained-discriminator
   caveat.
5. **Case 1's cited lines** are the docstring; the code is at `:528-536`, and the bias is clamped.
6. **56 GOV-* claims** -- there are 55.
7. **The reachability of Case 1 is not architectural** -- it is an operating-point fact
   (monostrategy candidate-feature collapse) that the documented V3-EXQ-614e remedy substantially
   lifts.
