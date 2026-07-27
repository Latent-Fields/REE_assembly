# Claim synthesis — MECH-163, hierarchical-vs-flat framing (Dezfouli & Balleine 2013)

**Generated:** 2026-07-27T06:01:26Z · session `dazzling-taussig-f58f4c`
**Status:** PROPOSAL. Nothing registered. `claims.yaml` untouched. No lit entry written.
**Promotes nothing, demotes nothing.**

Nominated on a **non-standard entry point**: not a FAIL cluster, but a framing tension
recorded as `failure_signatures[0]` of the 2026-07-26 lit entry
`targeted_review_connectome_mech_323/entries/2026-07-26_mech_323_hierarchical_action_sequences_dezfouli2013`
(Dezfouli & Balleine 2013, *PLoS Comput Biol* 9(12):e1003364; landed `d8db515e86`).
That entry was deliberately tagged `claim_ids_tested: ["MECH-323"]` only, because its
direction differs by claim, and routed the MECH-163 half here.

---

## 0. Headline

| Question | Verdict |
|---|---|
| Step-3 gate on MECH-163's FAIL record | **STOP — decompose nothing.** One genuine signature (786b), and it is a clean single falsification of leg (1), not a cluster. MECH-163 was already decomposed 2026-07-22; the debt is metabolized. |
| Q1 — restate / leave / split? | **RESTATE, narrowly.** Not a split. MECH-163 calls its habit pathway `model-free`; **the V3 substrate contains no model-free machinery at all**, and what *was* built is Dezfouli's hierarchical architecture. This is a description that was never true of the build. |
| Q2 — separate MECH-163-tagged lit entry? | **YES, one entry**, `evidence_direction: weakens` scoped to the `model-free` conjunct. `failure_signatures` prose and a `tags:` string are invisible to the indexer's claim attribution. |
| Q3 — discriminating falsifier | **Designed below, and NOT runnable today.** The paper's own signature (sequence coupling) does not port — it is true by construction in REE. The REE discriminator is a **dose-response of outcome-insensitivity on committed-macro grain**. Blocked by V3-EXQ-810. |
| Q4 — chunk-size budget as controllability parameter | **YES — one Q-claim**, whose `what_would_answer` is the dose-response arm of Q3, so it costs zero extra compute. |

**Three runs landed 2026-07-23/24 that neither the lit entry nor `claims.yaml` reflects**, and
they change the adjudication materially. They are in `review_tracker.json` as reviewed, but
reviewed != absorbed (see §5).

---

## 1. Step-3 discrimination gate — MECH-163's FAIL record as of now

| Run | Date | Recorded direction | Class |
|---|---|---|---|
| `V3-EXQ-786` | 07-20 | `non_contributory` / measurement_test_design_defect | test-design debt — **EXCLUDE** |
| `V3-EXQ-786a` | 07-22 → 07-24 | `weakens` **WITHDRAWN** → `non_contributory` (DV degeneracy) | test-design debt — **EXCLUDE** |
| **`V3-EXQ-786b`** | **07-24** | **`weakens`**, `non_degenerate: true`, AUC 0.848 vs 0.7 bar | **GENUINE** |
| `V3-EXQ-811a` | 07-24 | **`supports`** (MECH-477 + MECH-163), `outcome: PASS` | not a failure |

**Genuine, non-degenerate, substrate-ready FAIL signatures: 1.**

Per Step 3 that is a **clean single falsification**, which routes to `/governance` demotion
consideration — **not** to decomposition. Decomposing on one signature would manufacture
claims from a result that is already interpretable. The re-derive brake also fires
independently: MECH-163 was decomposed five days ago (`claim_synthesis_MECH-163_2026-07-22.md`,
user-approved per-child), yielding MECH-477 / MECH-478 / MECH-479 plus a narrow-in-place, and
carries registered children — the metabolized-cluster exclude.

**So the granularity-debt route returns nothing, and that is the correct output.** What
follows is a different kind of finding, and it is worth saying plainly that it is different:
the Dezfouli tension is **not granularity debt**. It is a **descriptive-accuracy defect** —
the claim text describes a substrate that was never built.

### 1a. What 786b + 811a jointly establish (and it vindicates the 07-22 split)

- `V3-EXQ-786b` (repaired instrument, `non_degenerate: true`, AUC 0.848): with **two pathways
  and no arbitrator**, `C1_recruitment_higher_on_novel` **fails**. Leg (1) weakened.
- `V3-EXQ-811a` (PASS, `supports`): with **the arbitrator ON**, differential recruitment
  **appears** — C1 passes, 6 of 7 divergent seeds (85.7%); C2 novel-minus-familiar mean
  `w_planned` = 0.194 against a 0.01 threshold.

That is a clean dissociation, and it is exactly the prediction the 2026-07-22 synthesis
registered MECH-477 on. **The arbitrator is the thing that produces differential recruitment;
the mere presence of two pathways does not.**

---

## 2. Q1 — the substrate finding, and why it settles the framing question

Everything in this section was read from the code, not inferred.

### 2a. There is no model-free machinery in REE. At all.

```
grep -rn "model_free\|model-free\|q_value\|q_table\|td_error\|sarsa" ree-v3/ree_core/   ->  0 hits
```

MECH-163's title characterises its habit pathway as *"(SNc/dorsal-striatum, **model-free**)"*.
Nothing answering that description has ever been built.

### 2b. What WAS built for the habit pathway is a depth-truncation of the same model

SD-081 (`ree_core/predictors/e3_selector.py:1330`):

```python
self._score_depth_limit = max(2, int(getattr(cfg, "dualsystem_habit_depth", 2)))
```

The "habit" read calls **`self.score_trajectory`** — the same scorer, on the same forward
model — with the `z_world` sequence truncated to the first 2 steps
(`e3_selector.py:887-902`). Both of MECH-163's "two systems" are **one model read at two
grains**, arbitrated by relative uncertainty. That is neither Daw's flat model-free/model-based
pair nor Dezfouli's chunk-only hierarchy — it is a third thing, **grain arbitration**.

Consequence for 811a: it is evidence that *depth*-arbitration produces the recruitment
signature. It is **not** evidence for a model-free second controller, and is therefore fully
compatible with Dezfouli's negative result.

### 2c. What was built for chunking IS Dezfouli's hierarchical architecture

- ARC-071 chunks are spliced into the ARC-007 proposal pool as **atomic value-flat
  Trajectories** (`ree_core/hippocampal/module.py:1796`, under `use_chunk_proposal_injection`).
- The E3 selector has **zero chunk-awareness** (`grep -n chunk ree_core/predictors/e3_selector.py`
  -> no hits). A chunk is scored by the single goal-directed scorer exactly like a primitive.
- A selected chunk is then **committed atomically**: `e3._committed_trajectory` with
  `metadata["source"] == "arc071_chunk"`, stepped by `_committed_step_idx`
  (`ree_core/agent.py:5332-5341`).

That is, precisely: *a single goal-directed process selecting between individual actions and
habitual sequences, where the sequence once selected executes as a unit.*

> **REE already implements the hierarchical account and has never implemented the flat one.**
> The paper does not put the substrate under pressure. It puts MECH-163's prose under pressure.

### 2d. Outcome-insensitivity is already structural, and there is no controller producing it

A committed trajectory can be released mid-execution by exactly five mechanisms
(`ree_core/agent.py`, `select_action`):

| Release | Reads | Value-driven? |
|---|---|---|
| MECH-091 urgency interrupt | `z_harm_a` / `z_harm_un` / `z_harm_suffering` norm | no — acute threat |
| MECH-342 maintenance release | score-margin decisiveness + `nav_competence` | no — execution readiness |
| rung-6 `natural_commit_urgency` | committed-run length, sequence completion | no — duration |
| └ SD-033e frontopolar pressure | `cfv_now - cfv_at_entry` (goal-proximity of best **foregone alternative**) | *nearest analogue* — but it reads alternatives, not devaluation of the committed outcome |
| MECH-321 / ARC-070 mid-chunk decomposition | region `V_s`, MECH-288 rollout boundary | no — prediction failure |
| SD-034 closure de-commit | closure state | no |

**None of them reads whether the committed outcome is still valuable.** So a committed chunk
in REE runs to completion regardless of devaluation — *outcome-insensitivity, produced by
grain, in a substrate with no model-free controller anywhere*. That is the strongest possible
instantiation of the lit entry's second-order point, and it is verifiable in code rather than
hypothesised.

### 2e. Verdict on Q1: RESTATE — three narrow edits, no new claims, no split

MECH-163's fate stays **narrowed-and-retained** (unchanged from 2026-07-22). Proposed edits:

| # | Edit | Why |
|---|---|---|
| **E1** | Strike **`model-free`** from the habit-pathway characterisation; replace with *"a myopic, depth-limited read of the same forward model (SD-081 `dualsystem_habit_depth`)"*. | False of the build (§2a/§2b) and independently disfavoured by the paper's model comparison. |
| **E2** | Record **`V3-EXQ-786b`** — currently absent from `claims.yaml` (grep count 0). Leg (1) is **no longer "experimentally untested"**; it has a genuine `weakens` on a repaired instrument. | The claim's own title still asserts the pre-786b state. |
| **E3** | Add a `notes` paragraph: REE instantiates the **hierarchical** account (§2c) and the *habit* half of MECH-163 is realised jointly by MECH-323's chunk inventory **and** the commit-latch grain — not by either alone. | Answers the lit entry's framing question in the registry rather than in a summary. |

**On "does MECH-323 become close to the whole of what habit names?"** — in REE, **jointly with
the commit layer, yes; alone, no.** MECH-323 supplies the *inventory*; the beta-gate /
`_committed_step_idx` / release set supplies the *grain*. Because the thing MECH-163's habit
leg reduces to is **MECH-323 ⊕ the commitment machinery**, and the commitment machinery is not
in MECH-323, folding MECH-163 into MECH-323 would lose the half that actually produces the
phenomenon. **Do not merge them.** This is also why no new "habit = chunk inventory" child is
proposed: it would be a rename of two existing claims.

---

## 3. Q2 — a MECH-163-tagged lit entry: YES, and why it is structural

The tension is currently recorded as `failure_signatures[0]` prose plus a `tags: ["mech-163"]`
string. **Neither is read for claim attribution.** `claim_evidence.v1.json` attaches on
`claim_ids_tested`, so as things stand the tension is invisible to the indexer, to
`lit_conf`, and to the governance walk — the same "prose does not survive the indexer" hazard
that forced the structural split on 2026-07-22.

Proposed entry, in `targeted_review_connectome_mech_163/` (**not** `_mech_323`, which is held
by another live session — see §5):

| Field | Value |
|---|---|
| `claim_ids_tested` | `["MECH-163"]` |
| `evidence_direction` | **`weakens`** |
| Scope | The **`model-free` conjunct only**. The paper does not refute that two selectable grains exist, and says nothing about novel-context recruitment (which is 786b's business). |
| `confidence` | ~0.72 — below the MECH-323 entry's 0.78: the architectural relation transfers well, but the negative claim ("model-free RL is unnecessary") is the part the authors themselves hedge as not ruling out all model-free accounts. |
| `mapping_caveat` | Must state that REE's habit pathway is a depth-truncated read of the *same* model, so the paper's target (a cached-value second controller) is **not what REE built** — the weakening lands on the claim's wording, not on its substrate. |

**Direction rationale, stated because it is the judgement call in this document.** `weakens`
is chosen over `supports` deliberately: the honest reading is what the source does to the
claim **as it stands on 2026-07-27**, and as it stands MECH-163 asserts a model-free habit
system. Writing it `supports` against the *restated* claim would launder the fact that the
wording was pushed back on. The entry is what **motivates** E1; E1's note then records that
the `weakens` is against pre-restatement wording. That is the same structural discipline the
07-22 split used when it retained 786a's `weakens` and re-scoped it by structure.

*If the user prefers, the alternative is to land E1 first and write the entry `does_not_support`
against the restated claim. Recommendation is the above.*

---

## 4. Q3 — the falsifier

### 4a. The paper's own signature does not port

Dezfouli & Balleine's discriminator is **sequence coupling**: selecting the habitual action at
stage one is followed by the habitual action at stage two, versus stage independence. They
needed it because they could not observe the inventory.

**In REE, coupling is true by construction.** Once a chunk is committed, `_committed_step_idx`
walks its actions; the successor is the chunk's own next element by definition. So coupling is
a **readiness check** here, not a discriminator. This is worth stating explicitly because it is
the natural thing to port and it would produce a guaranteed PASS that means nothing.

### 4b. The REE discriminator: a dose-response of outcome-insensitivity on grain

**DV:** post-devaluation policy persistence — after a mid-episode devaluation of the committed
goal's outcome, the fraction of subsequent steps continuing the pre-devaluation policy.
Devaluation substrate exists: SD-033b OFC-analog (`ree_core/pfc/ofc_analog.py`), with an
existing driver lineage to reuse (`v3_exq_485g/485i/485k/485m`).

**Arms** — every knob already built and default-OFF:

| Arm | `use_dualsystem_arbitration` | `use_policy_chunking` + `use_chunk_proposal_injection` |
|---|---|---|
| `A_off` — baseline; **mint reusable** (`include_driver_script_in_hash=False`) | False | False |
| `A_flat` | **True** | False |
| `A_hier` | False | **True** |

**Dose axis**, crossed on `A_hier` (and on a `A_flat`+chunking cell, so the axis is not
confounded with the arm): `chunk_max_size ∈ {2, 3, 5}`, optionally `chunk_max_depth ∈ {1, 3}`.

**The discriminating statistic is the *partial* contribution of realised mean committed-chunk
length versus arbitration weight to post-devaluation persistence:**

- **Hierarchical reading SUPPORTED** if persistence is **monotone increasing in realised mean
  committed-chunk length**, and `A_hier` shows persistence **with no arbitrator instantiated
  anywhere**. Grain is the cause.
- **Flat reading SUPPORTED** if persistence tracks `last_arbitration.w_planned` (lower w ->
  more habit-weighted -> more persistent) and is **invariant to chunk length once w is
  controlled for**.
- Both effects present and separable -> both mechanisms are real and additive, which is a
  third, informative outcome and should be pre-registered as such rather than forced into a
  binary.

### 4c. Mandatory readiness gates

This lineage has burned two runs on degenerate DVs (786a's constant first-step vector; 811's
`0.0`-for-empty-list aggregation). Pre-register all of:

1. **Chunks are formed AND injected AND selected** — per seed, count committed trajectories
   with `metadata["source"] == "arc071_chunk"` > 0. Zero -> readiness failure, scores nothing.
   *This is the gate V3-EXQ-810 failed.*
2. **Realised mean committed-chunk length differs across dose conditions.** Configuring
   `chunk_max_size` is not the manipulation; the realised length is. An inert dose axis is a
   readiness failure.
3. **Devaluation manipulation check** measured on a probe that does not involve the agent's
   policy — otherwise a null is a devaluation failure, not an insensitivity finding.
4. **`A_flat`:** `last_arbitration.w_planned` varies with measured uncertainty (MECH-477's
   existing mandatory check, already implemented and consumed by 811a).
5. **Gate every input to the DV's own statistic, not the prominent one** (the 786a lesson; the
   811 precedent for distinguishing "no data" from "zero range").
6. **Log per-release counts for all five mid-commitment releases** (§2d). This is a real
   confounder with the power to *invert* the dose effect: a longer chunk is exposed to more
   release opportunities, so it can read as *less* insensitive purely because it was
   interrupted more often. Persistence must be reported both raw and conditioned on
   uninterrupted macros.

### 4d. BLOCKER — not runnable today, and the probe has already run

`V3-EXQ-810` (2026-07-23, `v3_exq_810_arc071_chunk_accumulator_readiness_20260723T222726Z_v3`,
diagnostic, `claim_ids: [ARC-071, MECH-323, MECH-324]`) is the ARC-071 readiness probe. It
**FAILED `C1_accumulator_fires`** — gate 1 above.

Per-seed detail, which matters more than the verdict:

| Arm / seed | `n_formed` | `n_tracked_sequences` | `n_crystallised` |
|---|---|---|---|
| ARM_FORM / 101 | **7** | **22** | 0 (maintenance off — correct) |
| ARM_FULL / 101 | **7** | **22** | **6** |
| ARM_FORM+FULL / 202 | 0 | 6 | 0 |
| ARM_FORM+FULL / 303 | 0 | 6 | 0 |

`c1_form_seed_frac = c1_full_seed_frac = 0.333` against a `seed_pass_fraction` of 0.667, over
**n = 3 seeds**.

**The interpretation label `chunk_accumulator_silent` overstates the finding.** The accumulator
ran on every arm and seed (`n_steps` 360, `n_outcomes` 120 throughout), the OFF arm was
correctly inert (C3), the formation/maintenance dissociation was correct (C5), no replay-origin
chunks leaked (C4), and on seed 101 it formed **and** crystallised end-to-end. The precondition
that would have excused a null — flat outcome stream — was **met** (spread 0.256 vs 0.05 floor).
What failed is that on 2 of 3 seeds the agent's behaviour offered only 6 distinct tracked
sub-sequences, and none of them cleared the joint AND-gate. With n=3 and a 2/3 bar, one seed's
behaviour decided the verdict.

**Work-graph classification.** The falsifier is `complex (probe-gated)` — and **the probe has
already run**. What remains is `complicated (buildable)`: determine which of the three AND-gates
(repetition >= `R_min` / variance < `F_low` / mean > baseline + margin) blocks seeds 202 and 303.
The accumulator's own per-sequence tally already holds the answer, so this is one diagnostic
read, not a research question. Adjudicating 810 is **`/failure-autopsy` work** (§5) — it has no
autopsy on file.

**A note on sequencing that is easy to get backwards:** building a value-driven mid-commitment
release (§2d) would *destroy the phenomenon under test*. It must come **after** this falsifier,
not before.

**Secondary gate:** the DV needs sustained multi-step commitment, which is the BG/commitment
layer still under construction (F-dominance conversion ceiling). Gate 1 conditions the DV on
realised committed chunk executions, so a shortfall surfaces as a readiness failure rather than
a confounded null — but the run should not be queued until 810's successor clears.

---

## 5. Q4 — one Q-claim proposed

### Candidate — `Q-08x` `committed_macro_grain_is_a_controllability_parameter`

| Field | Value |
|---|---|
| `claim_type` | `open_question` (Q-claim) |
| `subject` | `policy.composition.grain_as_controllability` |
| Claim | The duration over which the goal-directed controller **cannot** intervene is set by committed-macro grain (`chunk_max_size` x `chunk_max_depth`), so MECH-323's chunk-size budget is a **controllability** parameter and not only a formation parameter. A budget set too high presents as outcome-insensitivity and **reports nothing at the accumulator**. |
| `status` | `candidate`; `epistemic_category` `standard` |
| `depends_on` | `[MECH-323, ARC-071, MECH-321, MECH-163]` |
| Lit grounding | The Dezfouli entry itself (`failure_signatures[2]`, conf 0.78). **Note:** session `optimistic-ellis-4357c6` opened a `/lit-pull` at 2026-07-27T05:45Z specifically on MECH-321/MECH-323's ungrounded numeric parameters **including the 2-5 chunk-size budget** — that pull is the natural primary grounding for this Q-claim and lands imminently. Sequence this after it. |
| **`what_would_answer`** | **The dose-response arm of §4b** — persistence monotone in realised mean committed-chunk length across `chunk_max_size ∈ {2,3,5}`, with the §4c gates. **Zero additional compute: it IS the discriminator.** RESOLVED-YES if persistence rises monotonically with realised length under gate 2. RESOLVED-NO if persistence is flat in length while chunks demonstrably form, are selected, and are committed at differing realised lengths. |
| Why not folded into MECH-323 | MECH-323 is the *formation* operator and its parameters are stated as formation parameters. The controllability semantics belong to the **consumer** side (commit latch + release set), which MECH-323 does not own. Registering it against MECH-323 would hide the coupling this document exists to surface. |

**Bounding note worth carrying into the claim:** the registered defaults are
`chunk_max_size = 5`, `chunk_max_depth = 3`. Because a depth-3 chunk's `sequence` may itself
contain depth-2 chunks, the defaults admit a top-level macro **longer than a typical episode**
(810 ran at 24 steps/episode). The insensitivity window is, at default settings, effectively
bounded by episode length rather than by the budget.

### Not proposed (deliberately)

- **A "habit = chunk inventory" child.** It would be a rename of MECH-323 ⊕ the commit layer
  (§2e). No new proposition, therefore no `what_would_answer` that is not already MECH-323's.
- **A "grain arbitration" architecture claim** unifying SD-081's depth read with ARC-071's
  chunk grain (§2b). It is a genuine and attractive observation, but it is this document's
  framing device, not a testable proposition distinct from the §4b falsifier. If §4b returns
  "both effects present and separable", *that* is the moment to register it — with the result
  in hand rather than as a guess.
- **A value-driven mid-commitment release claim.** §2d is a **substrate gap**, not a claim —
  `complicated (buildable)`, routes to `/implement-substrate`, and must be sequenced after §4b.

---

## 6. Governance debt surfaced (report inline; `/governance` and `/failure-autopsy` work)

1. **`V3-EXQ-786b` is absent from `claims.yaml`** (grep count 0). It is MECH-163's first
   genuine, non-degenerate `weakens` on a repaired instrument, and the claim's own title still
   asserts leg (1) is "EXPERIMENTALLY UNTESTED pending a non-degenerate re-run". That re-run
   happened on 2026-07-24. — `/governance`.
2. **`V3-EXQ-810` has no autopsy on file** and its `chunk_accumulator_silent` label overstates
   a 1-of-3-seed behavioural shortfall (§4d). It is the gate on every downstream ARC-071 /
   MECH-323 experiment, including §4b. — `/failure-autopsy`.
3. **MECH-477's `live_status.evidence` still cites `failure_autopsy_V3-EXQ-811_2026-07-24`**
   (`supports/measurement_test_design_defect`) though `811a` landed a clean PASS/`supports` on
   2026-07-24 and is absorbed elsewhere in the file. — `/governance`.

## 7. Concurrency notes

- `optimistic-ellis-4357c6` (opened 2026-07-27T05:45:58Z) holds
  `evidence/literature/targeted_review_connectome_mech_323` — the Dezfouli entry's own folder.
  **The §3 entry must go in `targeted_review_connectome_mech_163`**, and the §5 Q-claim should
  be sequenced after that pull lands.
- `cool-sutherland-623d3f` and `elegant-curran-fe12ba` hold `docs/claims/claims.yaml` with
  `claimed_at` of 2026-07-22 — **5 days stale** against the 6-hour bar, and their work
  (MECH-477/478/479) is registered. Confirm with the user before clearing; do not clear
  silently.

## 8. Registration gate

**Nothing in §2e, §3 or §5 is applied.** Per the skill, each item requires explicit per-item
user approval before it touches `claims.yaml` or the literature tree. Ids allocated from the
then-current max plus `git log` at write time; insertion region re-read immediately before
editing.
