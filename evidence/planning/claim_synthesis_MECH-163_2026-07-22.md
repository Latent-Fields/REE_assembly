# Claim synthesis — MECH-163 (dual goal-directed systems)

**Generated:** 2026-07-22T04:47:15Z · session `mystifying-merkle-f826e9`
**Status:** PROPOSAL. Nothing registered. `claims.yaml` untouched.
**Promotes nothing, demotes nothing.**

Commissioned as a three-target run (`MECH-440`, `MECH-204`, `MECH-163`) after the
granularity-debt recurrence trigger fired for all three in the 2026-07-22
failure-autopsy session. **Two of the three are REFUSED at the Step-3 discrimination
gate** (§1). Only MECH-163 clears, and the decomposition proposal for it is §2–§6.

---

## 0. Headline

| Target | Genuine, non-degenerate, substrate-ready FAIL signatures | Step-3 verdict |
|---|---|---|
| **MECH-440** | **0** | **STOP — measurement debt.** One readout (708b) settles it. |
| **MECH-204** | **0** | **STOP — instrument + implementation debt.** Never once validly tested. |
| **MECH-163** | **1** (786a), plus an explicit, lit-confirmed tri-partite claim structure with three distinct blockers | **PROCEED** |

The re-derive brake does not fire on any of the three (0 confirmed `substrate_ceiling`
hits each under R1–R3), which is correct and is *not* the question here. None of these
is a ceiling-exhaustion case. But "not a demotion case" does not automatically make
something a decomposition case, and for two of the three it does not.

---

## 1. Step-3 discrimination gate — the two refusals

The gate admits exactly one class: **≥ 2 distinct, genuine, non-degenerate,
substrate-ready FAIL signatures circling the same claim.** Vacuous-criterion /
test-design debt, substrate-not-ready, and clean single falsification are all excluded.
Refusing is the skill's primary function; forcing a decomposition here would mint
untested claims out of measurement bugs.

### 1a. The recurrence trigger's inputs were over-counted (report this)

Before classifying, the cluster memberships were checked against each autopsy's own
`targets[].claim_ids` rather than against topical proximity. **The trigger counted
autopsy FILES in the neighbourhood, not autopsy TARGETS tagging the claim**, and it
over-counted in both directions:

| Cited as bearing on | Actually tags | Verdict |
|---|---|---|
| MECH-440 — `failure_autopsy_V3-EXQ-709_2026-07-03` | `[MECH-439, ARC-108, ARC-110]` | **not MECH-440** |
| MECH-440 — `failure_autopsy_V3-EXQ-710_2026-07-03` | `[MECH-140, MECH-450, MECH-439]` | **not MECH-440** |
| MECH-440 — `failure_autopsy_V3-EXQ-707b_2026-07-20` | `[ARC-110]` | **not MECH-440** |
| MECH-440 — `failure_autopsy_V3-EXQ-699_2026-07-20` | `[MECH-448, MECH-449]` | **not MECH-440** |
| MECH-204 — `failure_autopsy_V3-EXQ-606_2026-05-29` | `[MECH-318]` | **not MECH-204** |
| MECH-204 — `failure_autopsy_V3-EXQ-774_2026-07-17` | `[MECH-173]` | **not MECH-204** |

MECH-440's real cluster is **3 targets across 3 files** (700d-708 cluster, 708, 708a),
not 7. MECH-204's is **5 targets across 3 files** (541/541a/541b cluster, 596-602
cluster, 794), not 5-across-4 including 606/774.

This is a live detector defect. A recurrence trigger keyed on neighbourhood file count
will systematically over-fire `/claim-synthesis` — which is precisely the
believed-tail-inflation hazard the skill's rails exist to prevent. Worth fixing at the
source; noted for chipping.

### 1b. MECH-440 — STOP (measurement debt)

Every one of the three real targets is excluded, and each autopsy says so in its own
`four_layer_diagnosis`:

| Target | `claim_alignment` | `measurement` | Class |
|---|---|---|---|
| 700d-708 cluster (708 arm) | *"intact — non_contributory; injection washed at the F-dominated argmax, claim could not express"*; cluster `readings: [substrate_enrichment]` | adequate | **substrate-not-ready** |
| `V3-EXQ-708` 2026-07-19 | *"unclear — MECH-440 was never validly tested"* | **"misleading — DOMINANT LAYER"** (pseudo-replicated DV) | **test-design debt** |
| `V3-EXQ-708a` 2026-07-22 | *"untested — no injected pre-commit variance means no propagation to observe"* | **"under-instrumented — DOMINANT LAYER"**; category `measurement_gap` | **test-design debt** |

**Genuine non-degenerate substrate-ready FAIL signatures: 0.** MECH-440 has *never once
expressed itself*. This is the canonical Step-3 STOP shape — the same shape as the
skill's own worked counter-example (the MECH-341 `660 → 660a → 660b` lineage): dominant
measurement layer, `claim_alignment` never `weakened`, verdict *fix the test*.

**On the candidate seam** ("the claim conflates PROPAGATION of selection noise with the
PRESENCE of pre-commit variance to propagate"): the seam is real and well-spotted — it
is visible in 708a, whose falsifier presupposes pre-commit variance exists and asks
whether it propagates, while the run found it does not exist. **But its truth value is
one readout away.** 708a names two rival readings that are not separable from its
manifest — (i) the pre-commit distribution is saturated/argmax-like, or (ii) the levers
are applied downstream of where it is formed — and names the readout that separates
them (per-select `max_prob`, effective support, per-candidate mass, per arm per seed).
Under (i) the seam is real and a child claim is warranted; under (ii) it is a wiring
bug and no claim should exist. Registering the child now would be a coin-flip on a
question 708b answers. The autopsy's own routing agrees:
`recommended_substrate_queue_entry.action = "none"`, *"Do not route to
`/implement-substrate`"*, route to **708b**.

**Verdict: refuse now, pre-register the decomposition as contingent.** If 708b returns
reading (i) — `max_prob` near 1 in **every** arm including `A0_OFF` — the seam is
confirmed and MECH-440 should be decomposed then, into a presence claim
(*the E3 pre-commit distribution carries non-trivial support over ≥ 2 candidates*) and
the existing propagation claim conditioned on it. That is the correct trigger for a
re-run of this skill on MECH-440, and it costs one experiment rather than one guess.

`/lit-pull` `targeted_review_mech_440_selection_variability` (stochastic resonance /
channel-specific variability in striatal selection) remains owed regardless, per the
708a autopsy — the global-softmax-temperature translation is an engineering import and
its biological warrant is unestablished.

### 1c. MECH-204 — STOP (instrument + implementation debt)

Same treatment; same result.

| Target | `claim_alignment` | `measurement` | Class |
|---|---|---|---|
| `EXQ-541` | *"unclear — experiment did not implement the mechanism correctly"* | **"broken — no-op means nothing to measure"** | **test-design debt** |
| `EXQ-541a` | **"intact"** — *"mechanism fires correctly; C3 failure = timescale mismatch"* | *"under-instrumented — rv divergence is noisy proxy"* | **scale/measurement debt** |
| `EXQ-541b` | **"intact"** — *"monotone dose-response confirmed; C4 failure = timescale mismatch"* | *"under-instrumented"* | **scale/measurement debt** |
| `V3-EXQ-596/602` | **"strengthened"** | **"misleading"** | **not a MECH-204 failure at all** |
| `V3-EXQ-794` | *"untested (both) — MECH-204's correction had no drift to correct"* | *"adequate — and it WORKED"*; category `competence_implementation_gap` | **implementation debt** |

**Genuine non-degenerate substrate-ready FAIL signatures: 0.** Not one target carries a
`weakened` claim alignment. Two carry **`intact`** and one carries **`strengthened`**.
The 541 timescale problem was *resolved* — `V3-EXQ-541c` PASSED at 16 cycles with a
monotone step-size dose-response, and that PASS is on file in the claim's own
`evidence_quality_note`. 794's clamp is a named, cheap, buildable fix
(`sd_waking_confidence_inflation_headroom`) on **SD-076**, a *separately registered*
claim — the drift source is already decomposed out of MECH-204.

**On the candidate seam** ("the claim bundles a DRIFT SOURCE, a CORRECTION mechanism,
and a TIMESCALE"): the observation is right, and one third of it is already actioned —
SD-076 *is* the drift-source claim, registered separately, with its own autopsy and its
own build. But the diagnosis this points to is **not granularity debt**. Splitting
MECH-204 further would not have prevented a single one of these five failures: 541 was a
no-op, 541a/b were under-powered on cycles, 596/602 failed on a MECH-285 criterion that
was never a MECH-204 prediction, and 794 clamped a variable in SD-076's implementation.

The real defect is a **specification** gap, not a granularity gap: MECH-204 states a
mechanism but **does not state its own falsification conditions** — not the DV, not the
required drift source, not the timescale at which the correction must act. So every
test has had to invent all three, and each invention has been wrong in a different way.
That is why the signatures look diverse. The remedy is to write MECH-204 a proper
`what_would_answer` naming (a) the drift source (now SD-076), (b) the precision DV and
why it is not tautological — the 774 lineage's symmetric-EMA lesson, and (c) the
minimum cycle count, which 541c has already measured at 16. **That is a
`/thought-digestion` or governance specification task, not a decomposition.** It is
cheap, it is buildable, and it converts the recurring failure mode into a fixed one
without adding a single claim to the believed tail.

One genuinely open sub-object is worth flagging but **not** worth registering yet: the
*timescale* is the only one of the three bundled objects with no owning claim. If, after
`sd_waking_confidence_inflation_headroom` lands and 794a runs, the correction again
fails on cycle count, a `Q-085 recalibration_timescale` child becomes warranted. Until
then it would be an untested claim minted from a resolved problem (541c).

---

## 2. MECH-163 — the case that clears

### 2a. Why it clears on one signature

Under a literal signature count MECH-163 has **one** genuine target, not two:

| Target | `claim_alignment` | `measurement` | Class |
|---|---|---|---|
| `V3-EXQ-786` 2026-07-20 | *"unclear"* | *"under-instrumented"* (non-scale-free manipulation bar) | **test-design debt — EXCLUDED** |
| `V3-EXQ-786a` 2026-07-22 | **"weakened, NARROWLY"** | **"adequate"** — AUC readout, scale-free, principled null at 0.5 | **GENUINE** |

This is stated plainly rather than counted to two, because the case does not rest on the
count. **MECH-163 satisfies the underlying coarse-claim condition by a stronger and more
direct route than signature-circling**, on three independent grounds:

1. **The tri-partite structure is explicit and pre-existing**, in the claim's own title
   and notes: *"required for (1) novel contexts…, (2) long-horizon benefit
   accumulation…, (3) prosocial planning."* The 786a manifest's own `scope_note` repeats
   it. Nothing is being invented here.
2. **The three legs have three different, independently documented blockers** — leg 1
   now nulled without an arbitrator; leg 2 blocked by ARC-007 STRICT value-flat
   proposals; leg 3 with no V3 substrate at all. A claim whose parts are blocked by
   unrelated things is not one claim.
3. **There is a live governance hazard that only decomposition fixes.** 786a's `weakens`
   is scoped to leg 1, and the autopsy mandates a scope qualifier *in prose*. Prose
   qualifiers do not survive the indexer: `claim_evidence.v1.json` attaches the
   `weakens` to **the whole claim**, so legs 2 and 3 — never tested, one of them with no
   substrate in existence — will silently inherit a refutation they did not earn. That
   is a structural defect with a structural fix and no other remedy.

Critically, **this decomposition does not inflate the believed tail.** Legs 2 and 3
already exist as assertions inside MECH-163's text, carrying the parent's confidence
invisibly. Splitting them out *disaggregates* existing belief rather than adding any:
after decomposition each says, in its own right, that it is untested and why — which is
strictly more honest than the status quo.

### 2b. Step 4 — the common thread

> **MECH-163 asserts the PRESENCE of two systems and names no mechanism that ALLOCATES
> control between them — yet both experiments measured allocation.**

786 could not establish the conditions under which allocation would be observable; 786a
established them cleanly (AUC 0.848, n=8, non-degenerate) and found allocation **flat**:
delta mean 0.00435, Cohen's d **0.047**, seven of eight seeds within ±0.15. A *flat*
response, not a noisy or bimodal one. That is the signature of two pathways and **no
arbitrator** — and it is exactly what MECH-163 predicts for a system it does not
realise it is describing.

The claim conflates **architecture** (two pathways exist) with **dynamics** (control
shifts between them with novelty, uncertainty and practice). Both of the mechanisms
that produce the dynamics are named in the registry and neither is in MECH-163: the
**arbitrator** (uncertainty/reliability-weighted control allocation) and the
**transfer** mechanism (ARC-071, planned → habitual chunking — confirmed as MECH-163's
missing transition mechanism by `targeted_review_arc_071_composition` R3, lit_conf
0.848, and **unbuilt**).

### 2c. Step 5 — lit grounding is already on file, and it is the finding

**No new `/lit-pull` is owed for the primary child.** The arbitration mechanism is
already reviewed *inside MECH-163's own targeted review*:

- `targeted_review_connectome_mech_163/2026-04-05_mech163_uncertainty_competition_daw2005`
  — Daw, Niv & Dayan 2005, *Nature Neuroscience* 8(12):1704-1711 (conf **0.79**). Its
  own summary states the point directly: *"given that both systems exist, how does the
  brain decide which one to trust at any given moment?"* — a Bayesian arbitration that
  weights the two systems by relative uncertainty, presented as **a distinct
  computational element**, not a property of having two pathways.
- Supporting, same folder: `balleine_odoherty_2010` (0.83), `dolan_dayan_2013` (0.85),
  `niv_2009` (0.78), `fraser2023` VTA/SNc dissociation (0.88), `miller2017` (0.87),
  `vikbladh2019` (0.86). Nine lit supports total; `is_formal_import: false`.

**This is itself the granularity-debt evidence, and it is the strongest single fact in
this document.** MECH-163's lit review contained the arbitrator as a separate mechanism
**since 2026-04-05**, and the claim text has never named it. The debt has been documented
for three and a half months; 786a is simply the first experiment to make it cost
something.

**One small top-up is owed** (not a blocker, not gating registration): the 786a autopsy
cites *reliability-based* arbitration in vlPFC/FPC (Lee, Shimojo & O'Doherty 2014) as
the empirical complement to Daw's normative account, and that entry is **not on file**.
Commission `targeted_review_connectome_mech_163` extension: `lee2014` +
`daw2011` (fMRI test of the 2005 proposal). Both refine the arbitrator child's
parameterisation; neither is required to justify registering it.

---

## 3. Proposed decomposition

**MECH-163's fate: NARROWED-AND-RETAINED** (not umbrella, not superseded). It keeps the
proposition that was actually tested, and keeps its refutation. The two untested legs
leave, and the missing mechanism is registered as a new sibling.

> Ids below are placeholders. Max at drafting: **MECH-474**, **Q-084**. Allocate at
> registration time from the then-current max plus `git log`, per the concurrency rule.

### Child 1 — MECH-163 (NARROWED, retained id)

| Field | Value |
|---|---|
| Disposition | **narrow in place**; retains its own id and its `weakens` |
| Narrowed claim | Two dissociable goal-directed pathways exist — a model-free habit pathway (SNc/dorsal-striatum analog) sufficient for approach in practised contexts, and a hippocampally-planned model-based pathway (VTA/ventral-striatum + PFC analog) — **and the planned pathway is preferentially recruited in novel contexts.** |
| Why this scope | This is exactly the proposition `V3-EXQ-786a` tested, fairly, at n=8 with a repaired instrument. The tested proposition keeps its refutation — no laundering. |
| `status` | `candidate` (unchanged) |
| Evidence | `V3-EXQ-786a` `weakens` **STANDS**, now correctly whole-claim-scoped because the claim is now only leg 1. `lit_conf` and `exp_conf` reported separately (9 lit supports; 1 experimental weakens — they do not blend). |
| `depends_on` | `[ARC-007, ARC-021, MECH-112, SD-012, INV-029, ARC-071]` unchanged; **add** the arbitration child |
| What changes | Legs 2 and 3 are **removed from the title and notes** and re-registered below. This is the whole point: they stop inheriting a refutation they did not earn. |

### Child 2 — `MECH-47x` `dual_system_uncertainty_arbitration` ← **the load-bearing child**

| Field | Value |
|---|---|
| `claim_type` | `mechanism_hypothesis` |
| `subject` | `goal_directed.uncertainty_based_control_arbitration` |
| Claim | Differential recruitment between the habit and planned pathways is produced by an explicit **arbitration element** that reads the two pathways' relative uncertainty/reliability and reallocates control accordingly. Two pathways **without** an arbitrator produce a **flat** recruitment response regardless of context novelty. |
| `status` | `candidate` |
| `epistemic_category` | `standard` (the substrate is buildable and specified; no ceiling reading) |
| `depends_on` | `[MECH-163, ARC-071, ARC-007]` |
| Lit grounding | `targeted_review_connectome_mech_163/2026-04-05_mech163_uncertainty_competition_daw2005` (conf 0.79) — normative Bayesian arbitration by relative uncertainty. Top-up owed: Lee/Shimojo/O'Doherty 2014, Daw 2011. |
| **`what_would_answer`** | Build an uncertainty/reliability-weighted arbitrator over the two pathways (`sd_dualsystem_uncertainty_arbitration`, default OFF / bit-identical). Re-run the `V3-EXQ-786a` design as a two-arm contrast, arbitrator OFF vs ON, same familiarity manipulation and the same AUC manipulation-check bar (≥ 0.7). **Supports** if the novel-minus-familiar recruitment delta is strictly greater with the arbitrator ON than OFF on ≥ 2/3 of divergent seeds, with the ON-arm delta clearing `mean − SEM > margin`. **Refuted** if the ON arm reproduces the OFF arm's flat response (delta mean within noise of 0, d < 0.1) with the arbitrator demonstrably live (manipulation check: arbitration weight varies with measured uncertainty). |
| Evidence from 786a | **`non_contributory`.** 786a did not test this claim — no arbitrator existed in the substrate. The flat-response shape is the child's **motivation**, not evidence for it. Recorded that way deliberately: reframing a null as a support for the mechanism whose absence explains it would be evidence-laundering. |
| Routes to | `/implement-substrate` — `sd_dualsystem_uncertainty_arbitration`, `priority_suggested: 2`, `unblocks_claims: [MECH-163, MECH-47x]`. This is the 786a autopsy's own recommendation. |

### Child 3 — `MECH-47y` `long_horizon_benefit_requires_model_based_rollout` (leg 2)

| Field | Value |
|---|---|
| `claim_type` | `mechanism_hypothesis` |
| `subject` | `goal_directed.long_horizon_benefit_accumulation` |
| Claim | Sustained benefit accumulation is a **trajectory** property, not a single-contact event, and is therefore reachable only by goal-seeded multi-step rollout; a 1-step greedy or value-flat-proposal policy cannot navigate toward it. |
| `status` | `candidate`; `epistemic_category` `substrate_conditional` |
| `depends_on` | `[MECH-163, ARC-007, SD-012, INV-029]` |
| **Blocker, stated in its own right** | **ARC-007 STRICT value-flat proposals.** The hippocampal proposer is value-flat by architectural commitment, so no goal-seeded rollout can be generated. This is the claim's blocker — **not** MECH-163's, and not something that should be inferred from a parent. |
| Lit grounding | `miller2017` (0.87), `vikbladh2019` (0.86) — hippocampal contribution to model-based planning, both already on file in `targeted_review_connectome_mech_163`. |
| **`what_would_answer`** | Requires an ARC-007 relaxation (goal-seeded proposal generation; the `MECH-292` / `MECH-293` ghost-goal path is the registered candidate route). Then: an environment where the cumulative-benefit optimum diverges from the greedy-contact optimum. **Supports** if the goal-seeded arm accumulates strictly higher integrated benefit than the value-flat arm on ≥ 2/3 seeds while matched on contact count. **Refuted** if integrated benefit is equal or lower with rollout live and the divergence between the two optima demonstrably present (manipulation check on the environment, not the agent). |
| Evidence | **none.** Never tested. Explicitly does **not** inherit 786a. |

### Child 4 — `MECH-47z` `prosocial_planning_requires_planned_system` (leg 3)

| Field | Value |
|---|---|
| `claim_type` | `mechanism_hypothesis` |
| `subject` | `goal_directed.prosocial_trajectory_planning` |
| Claim | Planning trajectories that affect **another agent's** `z_harm_a` accumulation and `benefit_exposure` over time is structurally inaccessible to a 1-step greedy policy and requires the planned pathway. |
| `status` | `candidate`; `epistemic_category` `substrate_conditional`; **`implementation_phase: v4`** |
| `depends_on` | `[MECH-163, INV-029, ARC-007]`, plus Child 3 (long-horizon rollout is a prerequisite for prosocial rollout) |
| **Blocker, stated in its own right** | **No V3 substrate exists.** There is no second agent, hence no other-agent `z_harm_a` to plan over. This is a V4 social-extension claim mis-filed inside a V3 claim — arguably the single clearest piece of granularity debt in MECH-163, since it has been carrying a V3 `implementation_phase` it cannot satisfy. |
| Lit grounding | `INV-029` benefit gradient (registry-internal); external lit **owed** before this child is tested — flag a `/lit-pull` on prosocial/vicarious planning at child-test design time, not now. |
| **`what_would_answer`** | Requires the V4 multi-agent substrate. **Supports** if a planned-arm agent reduces a second agent's integrated `z_harm_a` relative to a greedy-arm agent, on ≥ 2/3 seeds, with its own resource acquisition matched (so the effect is not confounded by the planned agent simply being better at everything). **Refuted** if planned and greedy arms are indistinguishable on the other agent's integrated harm with both demonstrably able to perceive the other agent. |
| Evidence | **none.** Never tested; no substrate. Explicitly does **not** inherit 786a. |

### Not proposed (deliberately)

- **A transfer/chunking child.** ARC-071 already *is* that claim, registered 2026-05-10,
  `candidate` / `v3_pending`, already in MECH-163's `depends_on`, with its own lit-pull
  (aggregate lit_conf ~0.78) and its own six settled review verdicts. It needs
  **building**, not registering. Do not mint a duplicate.
- **An "architecture vs dynamics" meta-claim.** That is this document's framing device,
  not a testable proposition. No `what_would_answer` ⇒ not a child.

---

## 4. What this changes in the evidence record

| Before | After |
|---|---|
| MECH-163 carries a whole-claim `weakens` from a one-leg test; the scope qualifier lives in prose that the indexer cannot read | MECH-163 is *only* that leg, so the `weakens` is correctly scoped **structurally** |
| Legs 2 and 3 silently inherit a refutation; leg 3 carries `implementation_phase: v3` for a mechanism with no V3 substrate | Each is a claim with `evidence: []`, its own named blocker, and its own falsifier |
| The arbitrator exists only inside a 2026-04-05 lit summary and a 2026-07-22 autopsy paragraph | The arbitrator is a registered, testable claim with a build route |
| Believed-tail size | **unchanged in substance** — belief is disaggregated, not added |

---

## 5. Follow-on routing (none of it done here)

| Route | Target |
|---|---|
| `/implement-substrate` | `sd_dualsystem_uncertainty_arbitration` (Child 2), `priority_suggested: 2` |
| `/implement-substrate` | **ARC-071** — unbuilt, `depends_on` of MECH-163, named transition mechanism |
| `/queue-experiment` | **708b** — MECH-440 pre-commit distribution *shape* readout (§1b); this is the gate on whether MECH-440 is ever decomposed |
| `/implement-substrate` | `sd_waking_confidence_inflation_headroom` (SD-076 clamp), then **794a** — MECH-204's actual repair path (§1c) |
| governance / `/thought-digestion` | Write MECH-204 an explicit `what_would_answer` naming drift source, DV and timescale (§1c) — the real fix for its recurring failures |
| `/lit-pull` | `targeted_review_connectome_mech_163` top-up: Lee/Shimojo/O'Doherty 2014, Daw 2011 |
| `/lit-pull` | `targeted_review_mech_440_selection_variability` (owed per the 708a autopsy regardless of §1b) |
| infrastructure | Fix the granularity-debt recurrence trigger to count autopsy **targets tagging the claim**, not neighbourhood **files** (§1a) |

---

## 6. Registration gate

**Nothing in §3 is registered.** Per the skill, each child requires explicit per-child
user approval before it touches `claims.yaml`.

**Concurrency note for the registration step:** two sessions hold active
`TASK_CLAIMS` entries on `docs/claims/claims.yaml` as of 2026-07-22T04:47Z —
`cool-sutherland-623d3f` (registering 24 candidate claims from six 2026-07-21 thought
intakes) and `elegant-curran-fe12ba` (`/claim-synthesis` on MECH-457). Ids must be
allocated from the then-current max **plus** `git log`, and the insertion region
re-read immediately before editing.
