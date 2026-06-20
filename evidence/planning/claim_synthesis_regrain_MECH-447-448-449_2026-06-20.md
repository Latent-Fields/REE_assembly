# Claim Synthesis RE-GRAIN -- MECH-447 / MECH-448 / MECH-449 (BG E3 selector-constitution family) post-689a

- **Generated (UTC):** 2026-06-20T18:39:11Z
- **Skill:** `/claim-synthesis` (proposal-first; nothing registered without per-child user approval)
- **Nominated by:** the `failure_autopsy_V3-EXQ-689a_2026-06-20` Step-8 routing ("/claim-synthesis
  re-grain", SECONDARY route) + `arc_107_selector_constitution_design_2026-06-20.md` s6 item 2 +
  the Q-078 / MECH-449 notes that defer the independent-vs-alternatives decision to a post-689a
  `/claim-synthesis` pass.
- **Family under re-grain:** MECH-447 (conflict-graded near-tie lever sufficiency, PARAMETRIC),
  MECH-448 (residual ceiling / rank-preserving F->eligibility demotion, LEAD), MECH-449 (Go/No-Go
  eligibility constitution, substrate_conditional), under the ARC-107 umbrella + Q-078.
- **This is the SECOND `/claim-synthesis` on this lineage.** The first
  (`claim_synthesis_MECH-439_2026-06-20.md`) decomposed the over-coarse MECH-439 into the existence
  fact (Child 1 = MECH-439, narrowed) + two rival forward mechanisms (Children 2/3), deferred to the
  689a manifest. Those children were registered (MECH-447/448) plus MECH-449 (Go/No-Go) + ARC-107 +
  Q-078 on 2026-06-20 ahead of 689a per the user capture-all-with-gates directive. **This pass
  re-grains the registered family in light of 689a's actual result.**

---

## 0. TWO GATES ON THIS RUN (read before acting on anything below)

### 0.1 V3-EXQ-689c has NOT landed -- MECH-447's final disposition is DEFERRED

Checked the coordinator DB on the hub (`coordinator.db`, 2026-06-20T18:39Z, authoritative per the
Phase-3 / effect-size memory; git evidence lags):

| queue_id | `experiments.status` | `results` row |
|---|---|---|
| V3-EXQ-689a | `completed` | **FAIL** (manifest landed 2026-06-20T17:58:11Z) |
| **V3-EXQ-689c** | **`pending`** (unclaimed) | **NONE** |

689c is the **Factor-B-alone (gap-scaled commit-T) gap-scaled isolation retest** -- the converter
689a's 2x2 pointed at. Per the design note s0 table, its outcome conditions HOW MUCH of MECH-447
survives and whether MECH-448's "ONLY demotion lifts" strong form weakens further. **Therefore this
run does NOT force MECH-447's final disposition.** It performs the *unconditional* structural
re-grain (the independent-vs-alternatives adjudication + the discrimination gate, both fully
determined by 689a) and leaves MECH-447's verdict + any split pending 689c. The 689c-outcome ->
disposition map is Section 6.

### 0.2 A LIVE concurrent session holds `docs/claims/claims.yaml`

Two active TASK_CLAIMS entries (both minutes old, NOT stale) overlap this family:

| session | claimed_at | holds | relation to this re-grain |
|---|---|---|---|
| `governance-689a-apply-...` | 18:27Z | `docs/claims/claims.yaml`, `claims.json`, `substrate_queue.json`, `review_tracker.json`, `pending_review.md`, `promotion_demotion_recommendations.md` | the autopsy's **PRIMARY** route (MECH-439 -> non_contributory, `f_dominance_conversion_ceiling` amend, mark 689a reviewed). Complementary, not competing -- but shares the `claims.yaml` FILE. |
| `lit-pull-arc107-bg-const` | 18:35Z | `targeted_review_connectome_mech_439/`, `arc_107_selector_constitution_design_2026-06-20.md`, `claim_evidence.v1.json` | ARC-106 grounding for ARC-107 (Go/No-Go opponency, pallidal disinhibition, psychiatric-failure-mode mappings for MECH-448/449). Feeds the lit warrant this re-grain relies on. |

Per the umbrella CLAUDE.md concurrency rule (never silently overwrite a live claim on a shared
resource), **this run makes NO `docs/claims/claims.yaml` edit.** It lands only this NEW planning doc.
The claims.yaml edits this re-grain implies are themselves 689c-gated (Section 6) and must wait for
the governance-689a session to release `claims.yaml` regardless -- so deferral costs nothing.

---

## 1. The cluster's failure record (Steps 1-2) -- the 689a 2x2

689a is the keystone conflict-graded falsifier (superseded 689; gap-blind-control redesign). Readiness
ALL met, `non_degenerate: true`:

- `a1b1_modulatory_channel_route_range` = 0.624 (floor 0.01) -- bias reaches the selector.
- `a1b1_e2_world_forward_prediction_spread` = 0.187 (floor 0.03) -- candidate pool genuinely divergent.
- `grading_levers_engaged` = 3/3 seeds (k varies AND t_eff varies) -- both conflict-grade levers acted.

The load-bearing **2x2 dissociation** (`two_by_two_dissociation`):

| arm | lever config | committed entropy | seeds strict-above collapsed | seeds strict-above gap-blind |
|---|---|---|---|---|
| ARM_A0B0 | both off (baseline) | 0.371 | 1/3 | 0/3 |
| ARM_A1B0 | **Factor A only** (graded shortlist width / STN-hold) | 0.440 | 0/3 | 0/3 |
| **ARM_A0B1** | **Factor B only** (gap-scaled commit-T / pallidal-gain) | **0.850** | **2/3** | **2/3** |
| ARM_A1B1 | **both** (the pre-registered gated hypothesis) | 0.387 | 0/3 | 0/3 |
| ARM_FIXED_KMAX | gap-blind A (flat k=6) | 0.546 | 1/3 | 0/3 |
| ARM_FIXED_HOT_T | gap-blind B (flat T=2.5) | 0.591 | 1/3 | 0/3 |

Three genuine, non-degenerate, substrate-ready failure/effect signatures:

1. **Factor A (graded shortlist width / STN-hold) alone is INERT** (0.440, 0/3 above controls).
2. **Factor B (gap-scaled commit-T / pallidal-gain) alone CONVERTS** (0.850, 2/3 above BOTH control
   sets) -- but seed-fragile (0.569 not collapse on the seed-43 monostrategy seed).
3. **A x B is DESTRUCTIVE** -- A1B1 (0.387) collapses to the A0B0 baseline, far below A0B1. The
   pre-registered both-levers gate landed on the cancelling cell.

`C_FGAP` (quantile slope vs F-gap; secondary, non-gating) PASS, slope -0.716 (gap-concentrated).

---

## 2. Discrimination gate (Step 3) -- applied to the THREE registered children

The re-grain is not "is MECH-439 too coarse" (the first synthesis settled that). It is: **now that 689a
has landed, are the three children correctly grained, or is one of them itself too coarse?** Apply the
gate per claim:

| Claim | Gate class | Verdict |
|---|---|---|
| **MECH-447** (conflict-graded near-tie lever sufficiency; text bundles `k=f(gap)` AND `T=f(gap)` as one "lever") | **GRANULARITY DEBT (proceed)** | 689a's 2x2 proves the single "lever" is **>=2 dissociable sub-levers with a destructive interaction** (A inert / B converts / AxB cancels). Three distinct, genuine, non-degenerate, substrate-ready signatures circling one claim = the granularity-debt bar, cleared. |
| **MECH-448** (residual ceiling / F->eligibility demotion) | NOT debt -- correctly grained | A single, well-posed mechanism hypothesis (remove F from the final argmin) with its own falsifier. The A0B1 lift mildly counter-evidences its "ONLY demotion lifts" strong form, but that is an evidence-direction caveat (governance), not a granularity problem. No split. |
| **MECH-449** (Go/No-Go eligibility constitution) | NOT debt -- correctly grained, broader rung | A strictly-broader mechanism (full eligibility-set governance), already `substrate_conditional`, double-gated. Not a finer split of anything; the next rung up. No split. |

**Gate result:** PROCEED for MECH-447 (internal granularity debt: STN-hold leg vs pallidal-gain leg);
STOP for MECH-448 and MECH-449 (correctly grained). The proceed-output (split MECH-447) is itself
**689c-gated** -- see Section 5.

---

## 3. The re-grain question, ANSWERED (Step 4): independent children or design alternatives?

This is the anti-proliferation adjudication the autopsy / Q-078 / MECH-449 notes deferred to this pass.
The answer has three distinct parts -- the family is NOT homogeneous on this axis:

### 3.1 MECH-447 <-> MECH-448 are **RIVAL READINGS ON ONE AXIS**, not independent mechanisms

They are not two separable mechanisms you would build additively. They are the two poles of a single
axis -- **parametric-sufficiency <-> constitutional-residual** -- and they make **opposite,
mutually-exclusive** predictions on the *same* discriminating experiment (689a's F-gap-correlation leg,
now 689c):

- MECH-447: the F-bound is *locally circumventable* at near-ties by a conflict-graded selection lever
  (F keeps monopolising variance; conversion recovered by widening/hotting only at near-ties).
- MECH-448: the near-tie lever *caps* committed entropy below the proposer ceiling; only *removing F
  from the final argmin* lifts through the bound.

At most ONE is the operative truth for the V3 tract. This is the textbook legitimate-decomposition
shape (**rival mechanism claims + a shared discriminator**) -- so they are NOT redundant proliferation,
but they are also NOT "independent" in the additive sense. **Anti-proliferation verdict: keep them as a
rival PAIR with a single discriminator; do not treat them as two mechanisms to both build.** The build
follows whichever the discriminator (689c) supports.

### 3.2 MECH-449 IS genuinely independent of the 447<->448 axis (a broader rung, double-gated)

MECH-449 is not a design alternative *along* the parametric<->constitutional axis. It is the **next rung
up**: the full Go/No-Go eligibility-set governance, of which MECH-448's isolated F->eligibility demotion
is ONE component. It is correctly `substrate_conditional` and **double-gated**: build only if BOTH (a)
689a/689c show the near-tie levers (MECH-447) insufficient AND (b) MECH-448's isolated demotion proves
insufficient alone. So it is a genuinely-independent child *of the architecture (ARC-107)*, gated behind
447 and 448, not a sibling alternative to either. **No re-grain; the registered double-gate is correct.**

### 3.3 MECH-447 itself is INTERNALLY too coarse -- the genuine new granularity debt

This is the one finding the first synthesis could not have made (it predates the 2x2). MECH-447's text
bundles Factor A (`k=f(top-F gap)`, STN-hyperdirect-hold analog) and Factor B (`T=f(top-F gap)`,
pallidal-disinhibition-gain analog) as **one** "conflict-graded near-tie lever." 689a proves they are
**two dissociable levers that interact destructively**, and the autopsy's biological reading (s3) gives
the mechanism: **raising the STN hold threshold (A) suppresses the very near-ties the pallidal commit-gain
(B) would diversify** -- so the two are *not independent*, and the biologically-faithful translation is
**one permission-to-commit constitution, not two stacked near-tie patches**. Concretely the conjuncts of
MECH-447 dissociate:

| sub-lever | biological analog | 689a verdict | bearing on MECH-447 as registered |
|---|---|---|---|
| Factor A: `k=f(F-gap)` graded shortlist width | cortico-STN hyperdirect conflict-hold | INERT (0/3) | the shortlist-width leg does NOT convert -> this conjunct is **weakened toward refuted** |
| Factor B: `T=f(F-gap)` gap-scaled commit-T | pallidal disinhibition gain | CONVERTS ALONE (2/3, seed-fragile) | the commit-T leg is the only converting parametric lever -> this conjunct is the **parametric partial-rescue** candidate |
| A x B (the both-levers form MECH-447 literally asserts) | stacked STN-hold + pallidal-gain | DESTRUCTIVE (A1B1 = baseline) | the *as-written* "shortlist+commit-T lever is SUFFICIENT" claim is **refuted in its combined form** |

So MECH-447 should re-grain into **the STN-hold/shortlist-width leg (refuted)** and **the
pallidal-gain/commit-T leg (partial-rescue, robustness-pending)**, with the destructive interaction
recorded as the constitutional/integration signal that motivates MECH-448/ARC-107. **But whether the
commit-T leg is a registrable, robust partial-rescue child is EXACTLY what 689c isolates** -- so the
split is deferred (Section 5), not executed now. Registering a "Factor-B-alone commit-T sufficiency"
child today would manufacture a claim whose evidence is one unread experiment away -- the same
anti-proliferation error the first synthesis avoided by deferring Children 2/3 to 689a.

---

## 4. Common thread (Step 4, one sentence)

Every effect in the 689a 2x2 shares this: **a conflict-graded near-tie lever can only act *at* a near-tie,
and the two ways to make near-ties exploitable (raise the hold threshold to create them = Factor A; hot the
commit to sample across them = Factor B) work against each other** -- so the family's missing structure is
not a *louder* near-tie lever but a *single coherent permission-to-commit gate* (eligibility demotion +
Go/No-Go governance) that the broad "near-tie sufficiency" framing of MECH-447 does not name. That is
precisely what MECH-448 (lead) + MECH-449 (broader) + ARC-107 (architecture) already capture; the family's
granularity below ARC-107 is correct EXCEPT for MECH-447's internal A/B conflation.

---

## 5. Lit grounding (Step 5) -- present; no new pull needed from this skill

Per "biology before formal definitions," the re-grain mechanism content is already grounded, and a
dedicated consolidating pull is in flight (the live `lit-pull-arc107-bg-const` session, s0.2):

- **STN hyperdirect conflict-hold (Factor A / MECH-447 A-leg):** SD-034 / Cavanagh & Frank 2011 (STN
  conflict-graded threshold, causal via DBS); Q-019 Aron 2007 / O'Reilly & Frank 2006 / Brittain & Brown
  2013. `lit_status: present`.
- **Divisive normalization (MECH-448 demotion lever):** `targeted_review_connectome_mech_439`
  Carandini & Heeger 2012 + Louie/Khaw/Glimcher 2013 -- with the LOAD-BEARING DIVERGENCE already filed
  (canonical DN is order-preserving + pooled-symmetric; REE proposes rank-ALTERING demotion of F only,
  needing the QD/MAP-Elites CDQ-003 justification). The s9 code-inspection finding in the first synthesis
  doc (deterministic-argmin default => divisive-norm-with-F-retained is inert without a stochastic commit)
  sharpens the MECH-448 build spec and is unaffected by 689c.
- **Go/No-Go opponency + pallidal disinhibition + psychiatric-failure-mode mappings (MECH-449):** being
  pulled now by `lit-pull-arc107-bg-const`. Confirm filed before any MECH-449 build.

No new `/lit-pull` is commissioned by this re-grain.

---

## 6. Per-claim dispositions + the 689c-gated registration trigger map (Steps 6-7, DEFERRED)

**No `claims.yaml` edit this session** (689c absent + live concurrent holder). When 689c lands and is
adjudicated, and the governance-689a session has released `claims.yaml`, a follow-on pass applies:

### 6.1 MECH-447 -- DEFERRED to 689c (the gated decision)

| 689c outcome | MECH-447 disposition | Action |
|---|---|---|
| Factor-B-alone PASS, gap-CONCENTRATED | parametric win on the commit-T leg (one factor) | **partially rescued (parametric reading).** SHRINK the constitution scope: re-grain MECH-447 to the commit-T leg only (register/retain the pallidal-gain partial-rescue as the surviving conjunct); the STN-hold/shortlist-width leg is WEAKENED. ARC-107 stays the V4 grounding roadmap; do NOT broaden the selector now. |
| Factor-B-alone PASS, gap-BLIND / uniform | non-specific hotting (just a hotter softmax, not conflict-grading) | escalate to **MECH-448 demotion**; MECH-447 (incl. the B-leg) WEAKENED -- the lift is not conflict-graded so the parametric reading fails. |
| Factor-B-alone FAIL / no-lift | near-tie parametric family fully exhausted (A inert AND B non-robust) | **WEAKEN MECH-447 toward refuted** (no split needed -- do not manufacture a child for a non-converting leg); MECH-448 + MECH-449 are the path. |

In all three the **STN-hold/shortlist-width leg (Factor A) is already weakened by 689a unconditionally**
(inert, 0/3) -- only the commit-T leg's fate is 689c-gated. The pre-registered `non_degenerate` /
`substrate_not_ready_requeue` non-vacuity floor applies to 689c as usual (a vacuous Factor-B isolation
self-routes, not a verdict).

### 6.2 MECH-448 -- ELEVATE to active build (UNCONDITIONAL from 689a; build sequencing 689c-gated)

689a's pre-registered both-levers gate (A1B1) returned **readiness-met / no-lift** (0/3 above both
control sets), which supports the residual-ceiling reading for the both-levers form. User-adjudicated
2026-06-20: the near-tie *parametric* family is exhausted -> MECH-448 (rank-preserving F->eligibility
demotion) is the **lead constitutional build lever**. This is a **build-path elevation** (substrate_queue
`f_dominance_conversion_ceiling` amend + the already-spawned implement-substrate chip), **NOT a claim
status promotion** -- MECH-448 stays `candidate` (a hypothesis, not yet shown; only `/governance` on
exp_conf makes it `shown`). Its registered text already carries the **A0B1-lifts-without-demotion caveat**
(the "ONLY demotion lifts" strong form is mildly counter-evidenced). 689c sharpens, not gates, the caveat:
a robust Factor-B conversion weakens "ONLY demotion lifts" further; a Factor-B failure strengthens the
residual-ceiling reading. **No claims.yaml status change owed** (the build elevation is the
substrate_queue/chip action the governance-689a + kickoff sessions already own).

### 6.3 MECH-449 -- HOLD substrate_conditional, double-gated (UNCONDITIONAL; already correct)

MECH-449 stays `candidate` / `epistemic_category: substrate_conditional`, built ONLY if BOTH the near-tie
levers (689a/689c) AND MECH-448's isolated demotion prove insufficient. Its registered double-gate
(`depends_on` MECH-448 + the s5.3-branch note) is already correct. **No change owed.**

### 6.4 ARC-107 / Q-078 -- unchanged this pass

ARC-107 stays `candidate`, instantiation gated on the 689 series (Q-078 what_would_answer already maps the
outcomes). Q-078 stays `answer_state`. The only post-689c update they may want is a one-line note that 689c
is the parametric-partial-rescue discriminator -- folded into the deferred follow-on, not done now.

---

## 7. Hand-off + close (Step 8)

- **This session wrote this analysis doc only.** No `claims.yaml` / manifest / decision_state / closure-node
  edit. No experiment, no promotion, no new child registered.
- **689c was NOT incorporated** (it has not landed; coordinator DB `pending`, no result row). The
  *unconditional* structural re-grain (Sections 2-4: discrimination gate, independent-vs-alternatives
  verdict, MECH-447 internal A/B granularity-debt finding) is complete; MECH-447's final disposition + any
  split is deferred to the Section-6.1 689c map.
- **Anti-proliferation rails held:** no child manufactured from a 689c-pending leg; MECH-448/449 correctly
  judged NOT granularity debt; the only debt found (MECH-447 A/B conflation) is recorded but its split is
  evidence-gated, not registered speculatively.
- **Concurrency resolved by sequencing, not arbitration:** the governance-689a session (PRIMARY route) and
  this re-grain (SECONDARY route) are complementary; deferring the claims.yaml edits avoids the shared-file
  conflict at zero cost since they were 689c-gated anyway.
- **Follow-on (chip):** when 689c lands AND `claims.yaml` is free, run the deferred re-grain registration
  per Section 6.1 (set MECH-447 disposition; if partial-rescue, shrink to the commit-T leg with the STN-hold
  leg weakened), then apply the derive-only reconcile (closure node `behavioral_diversity_isolation:GAP-I`
  + `biology_grounding_convergence_v4:BG-2` prose + `decision_state` via `record_decision.py`),
  `build_claims_json.py` + `governance.sh`, land on master.

### Cross-references

- First synthesis (MECH-439 decomposition): `claim_synthesis_MECH-439_2026-06-20.md`
- Autopsy: `evidence/planning/failure_autopsy_V3-EXQ-689a_2026-06-20.md`
- ARC-107 design proposal: `evidence/planning/arc_107_selector_constitution_design_2026-06-20.md`
- Claims: MECH-447, MECH-448, MECH-449, ARC-107, Q-078, MECH-439 (claims.yaml)
- Closure homes: `behavioral_diversity_isolation:GAP-I`; `biology_grounding_convergence_v4:BG-2`/BG-3
- Substrate rung: `f_dominance_conversion_ceiling` (substrate_queue.json)

---

## 8. DEFERRED REGISTRATION EXECUTED -- 2026-06-20 (weaken-now; 689c NOT awaited)

The Section-6.1 deferred decision was executed on 2026-06-20T18:55Z
(session `claimsynth-regrain-447-execute-20260620T1855Z`). **The 689c-gated trigger map (Section 6.1)
did NOT drive it** -- two things changed after this doc was written (18:39Z):

1. **689c never landed** as a gate. At execution time the coordinator DB still showed `V3-EXQ-689c`
   `pending` / unclaimed / no result row.
2. **The MECH-442 Section-7 biological-fidelity / anti-shortcut steer** (commit `feb5184824`, 2026-06-20,
   *after* this doc) **stripped 689c of all decision authority** -- it is no-authority confirmatory /
   divergence-ledger data only; "a 689c PASS does NOT lower the bar" for skipping the faithful build.
   This **kills the Section-6.1 gap-concentrated-PASS -> register-a-Factor-B-partial-rescue-child branch**:
   registering a parametric near-tie lever child is exactly the rejected shortcut.

Under **every surviving branch**, MECH-447 weakens with **no child**. The user adjudicated **weaken-now,
do not wait for 689c** (the outcome is invariant to it). Executed:

- **MECH-447 -> `status: superseded`** (`superseded_by: [MECH-448, MECH-449]`, `superseded_utc:
  2026-06-20`) with a `supersession_note` recording: (a) its pre-registered falsifier V3-EXQ-689a refuted
  the as-written both-levers sufficiency form (ARM_A1B1 0.387 = baseline, 0/3 strict-above both control
  sets, readiness met, non_degenerate); (b) the 2x2 dissociation (A inert / B converts seed-fragile /
  AxB destructive); (c) the Factor-B-alone effect is no-authority data earning no rescue child per the
  s7 steer, and 689c does not gate the disposition. This supersession_note ALSO discharges the
  "unconditional 689a evidence_quality_note" the follow-on owed (it had been added to MECH-448 only, not
  MECH-447).
- **MECH-448 / MECH-449 -- no status change** (correct as registered; build-path elevation owned by the
  substrate_queue + `implement-substrate-mech-448` session, which proceeds regardless of 689c).
- **Closure reconcile:** `behavioral_diversity_isolation:GAP-J` got an additive `governance_2026_06_20c`
  note (the disposition prose lived in GAP-J, not GAP-I/BG-2 as Section-7 hand-off guessed) marking the
  re-grain DONE + the partial-rescue branch dead + 689c no-authority. `decision_log.v1.jsonl` appended.
  `docs/assets/data/claims.json` rebuilt via `build_claims_json.py`.
- **Indexer / `governance.sh` NOT run** (concurrency): two live lit-pull sessions held
  `claim_evidence.v1.json` -- running the indexer would clobber their in-flight edits.
  `promotion_demotion_recommendations.md` + `decision_state.v1.json` regen defers to the next
  `/governance` cycle (recommendations.md self-reconciles from claims.yaml; a `superseded` claim drops out).
