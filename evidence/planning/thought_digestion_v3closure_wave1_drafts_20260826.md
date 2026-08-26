# `/thought-digestion v3-closure` -- PILOT WAVE 1, drafts for review

**Date:** 2026-08-26 · **Session:** `thoughtdig-grouping-7fd98a-wave1`
**Status:** STAGED ONLY -- **no `claims.yaml` write has been made and none will be made by
this session.** `claims.yaml` is held by the concurrent live session
`insights-7fd98a-digestion`; this pilot is deliberately draft-only and read-only on the
registry. Dispositions are the user's call.

**Mode under test:** grouped (wave-of-groups), `cap=5 floor=3.0`, edge-first agglomerative,
scope = closure-core + 1 hop. One agent per GROUP, three groups in parallel.
**Design + measurements:** `thought_digestion_wave_grouping_design_20260826.md`.

**Wave 1 = 3 groups / 12 claims** (of the 31-claim scope; wave 2 = the remaining 19 in 9
groups, worklist already built). All 12 verified undigested (`what_would_answer` absent,
no `digestion_note`) and disjoint from the concurrent live session's own wave 1/2 claims.

| group | claims | closure-core | why grouped |
|---|---|---|---|
| G1 | MECH-312b, MECH-312c, MECH-316, MECH-317, MECH-318 | 5/5 | `subject: policy.arbitration*` + shared registration batch + `depends_on` |
| G2 | MECH-263, SD-033b, ARC-113, MECH-298 | 2/4 | MECH-263's title NAMES SD-033b; `pfc.*`; ARC-113/MECH-298 one `depends_on` hop |
| G3 | MECH-254, SD-027, SD-064 | 2/3 | SD-064 is the organising concept both instantiate; pulled in by the hop |

---

## PILOT FINDINGS -- mechanism defects found while ASSEMBLING the wave

These are findings about the grouped mode itself, independent of what the agents return.

### P1. `cap=5` splits lettered claim families -- CONFIRMED, and the fix is free
`MECH-312a` <-> `MECH-312b` = **6.00** and `MECH-312a` <-> `MECH-312c` = **6.00**, yet
312a was stranded as a **solo in a different wave**. Mechanism: edge-first agglomeration
consumes the strongest edges first (`316`<->`318` = 8.00, `317`<->`318` = 8.00,
`312b`<->`317` = 7.00), filling the group to cap=5 as {316,317,318,312b,312c}; 312a then
cannot join a full group.

Measured across the full backlog: **4 lettered families have >=2 undigested members, and 2
of the 4 (50%) are split** (`MECH-312a/b/c/d` across two groups; `SD-033b`/`SD-033c` across
two). **No family exceeds cap=5 on its own**, so the fix costs nothing:

> **Proposed refinement (not yet applied to SKILL.md):** pre-merge lettered families
> (same numeric stem, e.g. `MECH-312a..d`) into an ATOMIC unit before clustering, and let
> the cap flex to accommodate a family. Never split a family across groups or waves.

Confidence: the fix is free and clearly right in direction, but n=4 families is a small
base. Flagged rather than shipped.

### P2. The scope filter itself splits a family
`MECH-312d` is `MECH-312a`'s joint-top partner (**6.00**) and is **outside** the
closure-core+1hop scope, so the scoped run sees only 312a/b/c of a 4-member family. The
`depends_on` hop does not close over lettered families.

> **Proposed refinement:** when any member of a lettered family is in scope, pull the whole
> family into scope (a "family closure" rule alongside the `depends_on` hop), OR admit the
> absent members as read-only CONTEXT MEMBERS (design doc 7b.4) so the agent at least sees
> them.

### P3. Deviation from the skill text, deliberate, for evaluation
Step 4/G3 says embed each claim's full YAML block **verbatim in the agent prompt**. Here
the blocks were pre-extracted to a file the agent reads instead (G1 425 lines, G2 547, G3
239 -- 1211 lines total). Rationale: identical information, no 86,000-line registry search,
and prompts stay readable. **Whether this weakens the "extract before inventing"
instruction is an open question this pilot should answer** -- if agents drift toward
inventing, embed verbatim next time.

---

## Wave timing

- dispatched 2026-08-26T20:14:45Z

---

## GROUP RESULTS

*(agents in flight -- results appended on completion)*

---

## GROUP G2 -- MECH-263, SD-033b, ARC-113, MECH-298  (returned 20:22Z, ~7.8 min)

### Dispositions
| claim | disposition |
|---|---|
| MECH-263 | **(c) substrate-blocked -- `substrate_ceiling`, NOT `substrate_conditional`** (see FLAG 1), with an (a)-testable representation-plane carve-out |
| SD-033b | **(a) testable now** -- mint a REPRESENTATION-PLANE SD-033b-vs-SD-033c distinguishability proposal |
| ARC-113 | **(f) defer with a durable marker** -- but a CORRECTED gate + the stage-implementation audit the claim owes |
| MECH-298 | **(a) testable now** -- the only claim in the group neither competence-floor-blocked nor substrate-blocked |

### What the GROUPED view produced that per-claim dispatch could not

1. **`depends_on` CYCLE between MECH-263 and SD-033b** -- each declares the other its ground.
   Neither can be topologically ordered; a governance move on either has no defined
   propagation direction. Only visible reading both blocks together.
2. **Their `functional_restatement` blocks are ~90% identical prose and their `falsifiable`
   clauses are THE SAME falsifier** ("collapses back into SD-033c"). **This explains a
   16-run, zero-evidence trail**: 16 manifests (485 x4, 485a-485m, 696 x2), every one
   adjudicated `non_contributory`, `genuine_exp_count: 0`,
   `experimental_confidence: 0.0` on BOTH claims. The two claims have been tested sixteen
   times and have zero evidence in either direction, because they were being asked the
   same question.
3. **The fix is DIFFERENTIATION, not merge** -- and the agent explicitly declined (g),
   correctly: a `design_decision` and a `mechanism_hypothesis` can each survive the other
   being wrong. SD-033b now takes the *substrate-distinguishability* falsifier; MECH-263
   takes the *functional-signature* falsifier. Different experiments, different
   preconditions, and **only one is competence-floor-blocked.**
4. **MECH-263 fuses ARC-113's `representation` and `prediction` stages** and says so
   explicitly. This hands ARC-113 a **pre-registered prediction it did not have**: the
   representation/prediction seam is the most likely non-dissociable pair, so ARC-113's
   ablation must either find a locus where they separate (`OFCConfig.use_outcome_oracle`,
   verified live) or report the pair as fused and accept a partial refutation at that seam.
5. **MECH-298 is a ready-made ON/OFF lesion for ARC-113's apprehension->representation
   seam** -- already designed, representational readout, so ARC-113 should reuse it rather
   than design a stage-lesion from scratch.
6. **ONE shared falsification condition** (the competence-floor non-degeneracy
   precondition) that MECH-263, SD-033b and ARC-113 should all POINT AT rather than
   re-derive -- 16+ manifests have independently rediscovered it -- **and MECH-298 is
   identified as the one claim that ESCAPES it** (representational DV, not committed
   behaviour).
7. **Cross-cutting finding:** the group is uniformly **mis-planed** -- every registered
   falsifier is on the BEHAVIOURAL plane while every claim's actual evidence, substrate
   maturity and tractability sit on the REPRESENTATION plane. 16 runs of confirming that
   the readout plane is wrong is enough signal to change the plane rather than the gain.

### Governance flags raised (5)
- **FLAG 1** -- `epistemic_category` on MECH-263 + SD-033b appears silently DOWNGRADED
  `substrate_ceiling` -> `substrate_conditional`, contradicting their own notes which say
  `substrate_ceiling` six times incl. *"11th substrate_ceiling reading"* (2026-06-22).
  Flipped between 2026-06-22 and 2026-07-11. **Agent deliberately did NOT decide** --
  both readings defensible, no artifact records the decision. Governance call.
- **FLAG 2** -- V3-EXQ-696 (2 runs, reviewed, adjudicated, `weakens` OVERTURNED to
  `non_contributory`, cleared SD-033b's `hold_candidate_resolve_conflict` agenda item) is
  recorded in **neither** claim's `evidence_quality_note`.
- **FLAG 3** -- SD-033b note cites `ree_core/pfc_analogs/ofc_analog.py`; **that directory
  does not exist** (correct path `ree_core/pfc/ofc_analog.py`). Isolated stale path.
- **FLAG 4** -- both notes terminate on *"next test is the co-armed full-stack arm"*, which
  RAN as V3-EXQ-714 (2026-07-07), terminal FAIL, readiness abort, C2 never scored, brake
  FIRED, re-queue REFUSED. **Following the note's instruction today attempts an
  already-REFUSED re-queue.**
- **FLAG 5** -- ARC-113's gate cites a release condition **already discharged**
  (V3-EXQ-654g, 2026-06-19, a month BEFORE ARC-113 was registered 2026-07-22); the real
  surviving blocker is the conversion ceiling, which binds only its behavioural route.
- **Registry defect** -- the MECH-263 <-> SD-033b `depends_on` cycle (item 1 above).

### Currency verified live in `ree-v3` (2026-08-26)
`ofc_analog.py` state_bias_head / devaluation_bias_head / `use_outcome_oracle` all LIVE
as described; `GoalState.is_active()` exists; MECH-288 `EventSegmenter` slow scale IS a
BOCPD-Gaussian on `z_goal` (= MECH-298's stated trigger); gate-modulated EMA confirmed on
both MECH-298 write targets; **no MECH-298 implementation exists anywhere** (note correct).
ARC-113 and MECH-298 are **absent from `claim_evidence.v1.json` entirely**.

### Agent's own stated uncertainty (kept, not smoothed)
- FLAG 1 left undecided on purpose.
- The MECH-263 outcome-oracle identity-decoding route is a **design sketch**: it was NOT
  verified that `E2HarmSForward` emits anything from which outcome IDENTITY (vs scalar
  harm magnitude) is decodable. **The single assumption most worth checking before minting.**
- ARC-113's representation-plane route is plausible but unproven -- depends on the
  unbuilt stage audit; this is why (f) not (a).

---

## GROUP G3 -- MECH-254, SD-027, SD-064  (returned 20:24Z, ~9.3 min)

### Dispositions
All three: **(c) substrate-blocked -> `substrate_conditional`** (never built, never exercised,
zero evidence either way -- NOT `substrate_ceiling`). Each carries a repair that is prior to
and far cheaper than any build.

### THE FINDING: the closure plan's GATE-B build spec is WRONG, and building it would waste the build

`MECH-254`'s operator `top_k(w_i, k)` ranges over an index `i` -- it presupposes an
**addressable population of content items**. What actually crosses the E1/E2 -> E3 boundary
in V3 is a **single dense vector**: `ree_core/agent.py:5634`, `_e3_tick()` ->
`z_world_for_e3 = self.theta_buffer.summary()` (theta-averaged z_world, MECH-089).
**There is no set to select from.** The boundary channel is a fixed-width COMPRESSION, not
a SELECTION.

Consequence: `global_workspace_jlens_plan.md` GATE-B is specified as *"top-k over active
`z_world`/`z_self` COMPONENTS per heartbeat"*. Top-k over the **coordinates** of a
distributed embedding is a magnitude mask, not selection over content -- in a distributed
code, coordinates are not items. **Built as specified, GATE-B would produce a gate that
passes a capacity check while testing NEITHER SD-027 NOR MECH-254.**

Two genuine addressable populations do exist adjacent to this boundary and the build should
range over one: **MECH-294 packet streams** (`multi_content_theta_packet.py`, 4 named
V_s-vintaged streams) or **SD-016 cue slots** (`e1_deep.py`).

**And the population choice is not free, because REE already ran the experiment:**
V3-EXQ-907/908 (both CONFIRMED 2026-08-10) tested hard selection over the SD-016 slot
population and **ELIMINATED straight-through top-k** at k=1 and k=2
(`constant_peaky_degenerate`, context-discrimination C1b **0/3 seeds each**), retaining
annealed Gumbel (3/3) as the validated production selector; pinned at
`ree_core/utils/config.py:597`. MECH-254's explicit agnosticism (*"Does not commit to
soft-attention vs hard top-k"*) was free when written and **is not free now**. The agent
correctly bounded the transfer: 907/908's selector was a *learned* end-to-end tagger where
MECH-254's weights are separately supervised, so the pathology need not carry -- the point
is it must be **excluded by measurement**, not that it is established.

### Other cross-claim output per-claim dispatch could not produce

1. **SD-027 asserts selection is "not inside E3"; V3 SHIPS a capacity-limited top-k
   selector INSIDE E3** (`e3_selector.py:3622-3676`, k default 3; MECH-439 conflict-graded
   k_max 6), recorded in-code as behaviourally load-bearing (committed-action entropy
   0.549 vs 0.337). Either the negative clause is contradicted by built substrate, or the
   two selectors range over different populations (action candidates vs active latents) and
   SD-027 must SAY so. **This also converts SD-027's test from unrunnable to two-sided:
   the alternative-site control it needs ALREADY SHIPS.**
2. **MECH-254 has no falsifier of its own.** Its `Falsifiable:` clause names **SD-027** in
   both directions and cannot discriminate MECH-254's weight formula from any other
   capacity-enforcing gate at the same site. The four-cell factorial two paragraphs later
   IS its falsifier, framed as a dissection tool. **Repair is text-only and orders of
   magnitude cheaper than the build.**
3. **Two of MECH-254's three weight terms have NO V3 substrate** -- SD-026's template
   channel (not built; queue entry `ready:false`, gated on SD-014 which is *not in the
   queue at all*) and MECH-081's NA salience (LC-NE exists but modulates policy/noise, not
   a boundary weight). With alpha_goal and alpha_na forced to zero the factorial's
   `template only` and `both on` cells are **structurally unreachable**.
4. **ONE shared falsifier written once at SD-064 with three claim-specific arms**, run as a
   single factorial on ONE substrate build -- boundary-gate-ablated-with-intra-E3-active
   scores SD-027 (location), gate-only vs template-only vs both-on scores MECH-254
   (weighting), capacity sweep x {integrative, reactive} DV scores SD-064 (cliff vs
   graceful). Currently each claim re-derives an ablation falsifier separately and **none
   names the intra-E3 control.**
5. **Shared non-degeneracy precondition**, converged on independently by two places in the
   corpus that do not cross-reference each other (V3-EXQ-908's C1b gate; the e3_selector
   top-k comment's "membership rotates with state"): the selected set must be a proper
   subset on a majority of ticks AND its membership must rotate with state above a shuffle
   null. Excludes `constant_peaky_degenerate` -- the degeneracy that makes a capacity-limited
   channel look like it works while doing nothing, **already realised once in this substrate.**

### Governance flags raised (5 more; none of the 8 existing `governance_flags.v1.json` entries touch this cluster)
- **G3-1** MECH-254 `implementation_phase: v4` while SD-027 (which it implements, and
  `depends_on`) is `v3`. Straggler from `chip-20260810-phase-consistency-reconciliation`,
  which reconciled SD-027 and did not carry MECH-254 one hop down. Mechanical fix.
- **G3-2** SD-027's `notes` **asserts and retracts the same GWT hedge in one field** --
  para 4 states it, para 5 (`[2026-07-08 SD-064 reframe]`) retires it, both live, retracted
  version first. A reader greps the first screen and gets the retired text.
- **G3-3** SD-027 "not inside E3" vs shipped substrate (item 1). **Needs adjudication, not
  a silent fix.**
- **G3-4** All three claims `live_status.as_of: 2026-07-11`; plan `last_updated 2026-07-10`
  (46 days). **Three post-dating runs bear on the cluster and NONE is cited by it**:
  V3-EXQ-840b (2026-08-01, the corpus's only well-powered boundary-bandwidth manipulation,
  reads **graceful not cliff**), 907/908 (top-k eliminated), 948 (2026-08-25, names the
  competence blocker node A calls unresolved). **Node A's blocker has moved from
  `complex (probe-gated)` to `complicated (buildable)`.**
- **G3-5** SD-027's `substrate_queue` entry: `ready:false`, 4-month-stale
  `last_seen_session`, **no `node_class`**, unwalked dep chain SD-027 -> SD-026 -> SD-014
  (SD-014 absent from the queue).

### Agent's own stated uncertainty (kept)
It did **not** re-verify at runtime whether MECH-294 `alternation` mode *stales* the three
non-live streams (vintaging) or *drops* them. **If it drops them, V3-EXQ-840b satisfies
SD-064's precondition (3) after all and its null becomes DIRECT and serious pressure on
SD-064 rather than adjacent pressure.** Single-file check, materially changes SD-064's
evidential position -- worth doing before any of this is applied.

---

## GROUP G1 -- MECH-312b, MECH-312c, MECH-316, MECH-317, MECH-318  (returned 20:25Z, ~11.0 min)

### Dispositions
| claim | disposition |
|---|---|
| MECH-312b | **(c) `substrate_conditional`, blocker REPLACED** -- ARC-063 landed; the true residual is a graded practice->weight term (one term, one place) |
| MECH-312c | **(c) `substrate_conditional`, gap located exactly** -- affect reaches CRF as CREDIT, not as CONTEXT KEY |
| MECH-316 | **(a) testable NOW** -- disposition CHANGED by a discovered substrate (see below) |
| MECH-317 | **(b) derivational** -- absorption check vs ARC-071, settled by audit not experiment |
| MECH-318 | **(c) `substrate_conditional`** -- and explicitly AGAINST the `substrate_ceiling` label the 606 autopsy floated |

### FLAG A -- an 11-week promote/demote suppression standing on a FALSE premise
MECH-312b and MECH-312c both carry, verbatim: *"epistemic_category: depends on ARC-063
rule-creator substrate (planned, design-only 2026-06-04, **not yet built**); suppress
promote/demote until it lands. Set 2026-06-07 IGW-046."*

**ARC-063 landed 2026-06-04** (`ree-v3` `175a24f`, `candidate_rule_field.py`, 862 lines).
The note was set **2026-06-07 -- three days AFTER the substrate it declares unbuilt** -- then
migrated verbatim on 2026-07-18 without re-checking. The note's own text carries the correct
date ("design-only 2026-06-04") next to the wrong verdict, which is presumably how it
survived review. **Do not simply delete it**: these claims are still not promotable, but for
a different reason (behavioural coverage), and the recorded reason should be the true one.

### The group's blocker SILENTLY CHANGED CLASS and no claim records it
All five substrates now exist: ARC-063 (2026-06-04), MECH-457 SF critic (2026-07-12),
ARC-071 PolicyChunking (2026-07-22), SD-081 arbitration weight (2026-07-22), SD-054
`reef_bipartite_layout` (exercised 2026-05-21). The real blocker moved from **absence of
mechanism** to **degenerate behavioural coverage on mechanisms that exist**.

**Operational cost:** this mis-routes the cluster to `/implement-substrate` when the actual
lever is upstream of it -- consistent with `substrate_queue.json`'s own 2026-08-21 audit
finding **zero** ready implement-substrate entries while MECH-316/317 sit in
`candidate_v3_pending`.

### NDP-SD054-COVERAGE -- one shared, MEASURED precondition to register once
> A seed contributes evidence to any SD-054 falsifier in this cluster only if the **eval**
> policy actually inhabits the goal-rich states the DV is read from: `reef_frac_eval > 0` in
> **every** regime contrasted, per seed, measured arm-agnostically **before** any arm
> comparison. A failing seed is `degenerate`, **never a null**. A run below `MIN_PASS_SEEDS`
> non-degenerate seeds is `non_contributory` **regardless of what the contrast shows** --
> including when it looks favourable.

Not stipulated -- **measured**: V3-EXQ-606 seeds 7 and 17 gave `reef_frac_eval = 0` in BOTH
axes while the wiring criterion C3 passed 3/3. Seed 42 alone cleared C1 at 0.186. **Reading
that 1-of-3 as weak support is the exact error this prevents.** Register on MECH-318;
cross-reference from the other four instead of restating it four times.

### Deepest cross-cutting finding
**Nothing in V3 learns a predictive representation that is both TRAINED and VALUE-AGNOSTIC
-- which is exactly what MECH-316/317 assert.** The built candidates split into two families,
neither of which is what the claims describe: the structural/counting family is untrained by
design (`candidate_rule_field.py:41` -- *"pure-arithmetic ... the differentiation is
structural, not learned"*; ARC-071 chunks stay **value-flat** by explicit design to preserve
ARC-007 strict), while the trained family is reward-coupled (the SF critic's `w` is grounded
in the MECH-229 VALENCE_WANTING channel). **This is the honest content of
`substrate_conditional` for this cluster -- far sharper than the stale "no module exists".**

### Other cross-claim output
- **Mutual confound neither sibling declares:** MECH-312b's test is valid only with affective
  load pinned; MECH-312c's only with practice count balanced. **Each is the other's confound
  and a null on either is uninterpretable unless the other is pinned.** Now an explicit
  precondition on both drafts.
- **MECH-317 is a duplicate registration of a built mechanism** (ARC-071/MECH-323/MECH-324,
  same Smith & Graybiel + Sutton anchors, 2114 lines, 25+ contracts, 3 readiness runs).
  Neither claim references the other. Expect verdict-B partial absorption -- ARC-071
  explicitly *rejects* the option-critic gradient-discovery route MECH-317 names, so a
  residual survives and must be carried forward, not orphaned. **MECH-312b `depends_on`
  MECH-317 and must be repointed in the same pass.**
- **A merge pressure that points OUT of the group**, which `(g)` as scoped cannot express
  (MECH-317 -> ARC-071; MECH-316 -> the MECH-457 SF critic). See PILOT FINDING P4 below.
- **MECH-312c's gap located to one line:** affect enters CRF as `_crf_outcome =
  -||z_harm_a||` (credit) while the context key is `z_world` -- so **no rule in the field
  carries an affective context signature** and affect-congruent retrieval is *structurally
  impossible* on current wiring. A test run today returns a null for a reason unrelated to
  the hypothesis. Build = concatenate `z_harm_a` into `_crf_ctx` behind a default-OFF knob.

### Agent's own honesty, worth preserving
- It reported its **own first grep was a FALSE NEGATIVE** (`successor_rep|sr_matrix` found
  nothing; a case-insensitive search found the SF critic) -- **and MECH-316's disposition
  turned on that correction**, from substrate-blocked to testable-now.
- It declined to claim the three ARC-071 readiness runs as evidence FOR MECH-317, having
  checked that none carries a `claim_ids` field tagging it.
- It recommended **against** `substrate_ceiling` on MECH-318 *on evidence* (the runs were
  degenerate, not non-degenerate -- failing that label's stated bar), rather than adopting
  the autopsy's floated label.
