# Claim-Synthesis Proposal — Q-080 (effort_as_harm_energy_conservation)

**Date:** 2026-07-09
**Skill:** `/claim-synthesis` (proposal-first, lit-grounded decomposition)
**Entry point:** direct nomination (Q-080), user decision 2026-07-09 "narrow now"
**User registration disposition (inherited from the 2026-06-24 intake):** *"pose the
question first, do NOT mint a mechanism on a hunch."*

---

## 0. What this pass is (and is not)

Q-080 is an `open_question`, **not** a FAIL-cluster. The skill's discrimination gate
(Steps 2–3, which filters vacuous / substrate-not-ready / cleanly-falsified FAIL
signatures) has **no failure record to act on** and is therefore N/A here. The binding
disciplines that DO carry over:

- **Lit grounding is mandatory before registration** (Step 5) — done below (§2).
- **Every sub-question must be independently testable** (a `what_would_answer`) or it is
  not proposed (§3).
- **Proposal-first, per-child user approval** — nothing lands in `claims.yaml` without
  explicit approval (§5).
- **Register questions, not mechanisms** — the output is testable sub-*questions*, not
  minted `mechanism_hypothesis` claims. (Contrast MECH-454, minted in the same 2026-06-24
  pass with a different disposition.)

**Precedent for the FORM:** Q-040 was narrowed the same way (claims.yaml:18279,
`narrow_open_question applied`): the sub-questions Q-040.a/b/c were registered as
**embedded testable scaffolding inside the existing open_question entry** (a note block +
the `what_would_answer` field), the question stayed `open`, no new claim IDs were minted,
no status changed. This proposal recommends the identical form for Q-080 (§4).

---

## 1. The broad question and why it decomposes

Q-080 asks a single conflated question:

> Is wasted/excessive effort a **'harm'** in REE (routed into the residue/allostatic/
> irreversibility-aware stream, with energy-conservation as an evolutionarily-primary
> least-effort prior) — or only a **foregone value** (already handled by dACC EVC
> effort-cost + MECH-320/ARC-068 opportunity-cost + pACC allostatic load)?

Three *separable* propositions are bundled inside it, each independently
true-or-false and each with a distinct discriminating test:

1. **HARM-COUPLING** — does over-exertion → depletion need harm's *irreversibility-aware
   special status*, or does the existing allostatic + EVC handling suffice?
2. **EVOLUTIONARY-PRIMACY** — should energy-conservation be a default **least-effort
   prior** (a prior over policies), or is it adequately a value-subtraction *term*?
3. **MECH-454 GROUNDING** — is MECH-454's option-value cost better grounded as a
   **re-acquisition-ENERGY** cost than as abstract real-options / empowerment value?

These are genuinely orthogonal: (1) could resolve "no harm-coupling needed" while (2)
resolves "yes, a least-effort prior is warranted" (a prior is not a harm), and (3) is an
architectural-grounding question about a *different* claim (MECH-454) that Q-080 only
touches. Bundling them makes Q-080 un-answerable by any single experiment.

---

## 2. Lit grounding (Step 5 — mandatory)

Targeted searches run 2026-07-09 (consensus). This is proposal-grade grounding; a full
`/lit-pull` with evidence files is deferred to *if/when a sub-question resolves toward a
mechanism* (per the Q-080 note and skill Step 8). **Key finding: the lit warrants posing
each sub-question but does NOT pre-decide any of them — the ideal state for a
"pose-the-question-first" narrowing.**

### 2a. Harm-coupling (Q-080.a)
- **Hogan et al. 2020, *Nat Commun*** (55 cites) — physical fatigue *increases the
  subjective COST of effort*, computed in insula from premotor/motor-cortical state. →
  Fatigue feeds back into **effort-cost valuation** (REE's SD-032b dACC/insula EVC), not
  obviously into a nociceptive/harm stream.
- **McMorris et al. 2018, *Neurosci Biobehav Rev*** (104 cites) — central fatigue as
  **interoception**: AIC compares interoceptive feedback to predictions; ACC/LPFC decide
  continue-vs-stop when "reward not worth the cost." → An **interoceptive-allostatic**
  loop (REE's SD-032c AIC + SD-032e pACC), again cost-framed.
- **Pizzolla et al. 2026, *Front Psychol*** — allostatic framework: fatigue emerges from
  the **anticipatory energy-regulation (allostatic) system**; imprecise energy
  predictions produce the fatigue percept.
- **Net warrant:** over-exertion → depletion → an aversive interoceptive state is real,
  but the biology routes it into the two loci REE *already has* (SD-032b EVC cost +
  SD-032e/SD-032c allostatic prediction). The lit does **not** show effort-depletion
  recruiting the *irreversibility-aware, residue/No-Go* special status of harm. This
  **sharpens** Q-080.a from "is effort a harm?" to "does effort-depletion need harm's
  *irreversibility-aware handling* on top of the allostatic+EVC handling REE already has?"

### 2b. Evolutionary-primacy / least-effort prior (Q-080.b)
- **Selinger et al. 2015, *Curr Biol*** (348 cites) — humans **continuously optimize
  energetic cost in real time**; "energetic cost is not just an outcome of movement, but
  also plays a central role in continuously shaping it," re-converging within seconds on
  <5% savings. → Energy minimization behaves like a **standing prior on action**, not a
  post-hoc value subtraction.
- **McAllister et al. 2025, *J Exp Biol*** (18 cites) — "behavioural energetics" review:
  energy optimization across diverse dynamic tasks, adapted over short timescales.
- **Charnov MVT / optimal foraging** (Guo et al. 2025 *PNAS Nexus*; Norberg 2021;
  Orjollet-Lacomme 2025) — **net energy gain is the fitness optimization criterion**;
  MVT holds even for minimal feeding-rate-only organisms. → Energy budget as an
  evolutionarily-primary currency.
- **Net warrant:** strongly supports that energy-conservation *can* be an evolutionarily-
  primary least-effort prior. It does **not** settle whether REE's *existing* value-
  subtraction term already reproduces least-effort-default behaviour — that is the
  empirical crux Q-080.b poses.

### 2c. MECH-454 energy-grounding (Q-080.c)
- **Catenacci Volpi et al. 2020, *IEEE TCDS*** (17 cites) — goal-directed empowerment =
  *number of future options*; explicitly handles **delayed goal commitment** and
  uncertain/changing goals (the MECH-454 uncertainty-gated foreclosure regime).
- **Hayashi et al. 2025, ArXiv** — empowerment = maintain/expand controllability; agents
  seek/sustain **high-optionality states**.
- **Net warrant:** grounds "option-value = future-option maximization," but frames
  optionality **information-theoretically**, *not* as an energy re-acquisition cost. So
  Q-080.c's specific move (energy-economy is a *stronger* anchor for MECH-454 than the
  abstract real-options/empowerment lit) is **left open** by the lit — correctly.

### Lit clusters still owed IF a sub-question resolves toward a mechanism (not pulled)
Full `/lit-pull` on: effort-discounting / cost-of-cognition (Kool & Botvinick 2010;
Westbrook & Braver); least-action priors; Selinger-lineage sensing mechanisms for energy
expenditure; empowerment↔metabolic-budget bridge for Q-080.c.

---

## 3. Proposed decomposition — three testable sub-questions

All three stay `open_question`; none mints a mechanism. Each carries a discriminating
test, a version scope, and its lit anchor.

### Q-080.a — HARM-COUPLING
**Question:** Does over-exertion → depletion require harm's **irreversibility-aware
special status** (residue that cannot be erased / No-Go-adjacent caution), or does REE's
existing allostatic (SD-032e pACC + SD-032c AIC) + EVC (SD-032b dACC) handling suffice
without coupling effort into the z_harm_a stream?

**Discriminating test:** On an effort-dissociating env (a LOW-effort and a HIGH-effort
path to the SAME benefit, per-action energy cost measurable, plus a chronic-exertion
regime that can deplete), factorial `{effort→z_harm_a coupling OFF/ON}` with the existing
value-subtraction + allostatic machinery ON in **both** arms.
- **ANSWERED "harm-coupling needed"** iff the ON arm produces *irreversibility-aware*
  behaviour the OFF (value-subtraction+allostatic) baseline does not — specifically
  protective disengagement BEFORE depletion and caution scaled to the non-reversibility
  of the depletion, on a strict majority of seeds.
- **ANSWERED "suffices, no coupling"** iff OFF already reproduces protective
  disengagement + irreversibility-aware caution and ON adds nothing measurable → effort
  is a foregone value, **do NOT mint a harm-coupling mechanism.**
- **NON-DEGENERACY:** the two paths must differ measurably in energy cost AND depletion
  must actually accrue in the chronic regime (else neither pole is distinguishable →
  `substrate_not_ready_requeue`, not a verdict).

**Version:** v3 (needs the effort-dissociating env; substrate-conditional on that env +
an SD-032e effort-input variant). **Lit anchor:** Hogan 2020, McMorris 2018, Pizzolla
2026 (§2a). **Bears on:** SD-032b, SD-032e, SD-032c, MECH-219, MECH-454, SD-012.

### Q-080.b — EVOLUTIONARY-PRIMACY (least-effort prior)
**Question:** Should energy-conservation be a default **least-effort prior** (an
evolutionarily-primary prior over policies favouring low effort when benefit is
indifferent), or is it adequately captured by the existing value-subtraction term
(SD-032b EVC + MECH-320/ARC-068 opportunity-cost)?

**Discriminating test:** Same effort-dissociating env, `{least-effort prior OFF/ON}` with
the value-subtraction term ON in both arms.
- **ANSWERED "prior warranted"** iff the ON arm defaults to the low-effort path when
  benefit is indifferent / uninformative in a way the value-subtraction-only arm does not
  (e.g. before any benefit signal accrues, or under benefit ties the value term leaves
  unbroken), majority of seeds.
- **ANSWERED "term suffices"** iff the value-subtraction arm already produces the
  least-effort default and the prior is redundant.
- **NON-DEGENERACY:** benefit must be genuinely indifferent/tied across the two paths in
  the probe condition (else the value term trivially decides and the prior has nothing to
  add).

**Version:** v3. **Lit anchor:** Selinger 2015, McAllister 2025, Charnov-MVT cluster
(§2b). **Bears on:** SD-032b, MECH-320, ARC-068, SD-012.

### Q-080.c — MECH-454 ENERGY-GROUNDING
**Question:** Is MECH-454's uncertainty-gated option-value cost better grounded as a
**re-acquisition-ENERGY** cost (foreclosing an option = paying energy to rebuild it) than
as the abstract real-options / empowerment value it currently cites — i.e. does the
energy-economy framing *predict* MECH-454's behaviour better?

**Discriminating test (gated on MECH-454's substrate landing):** parameterize the
MECH-454 option-value cost two ways on the reachable-option-dissociating env MECH-454
already requires — (i) abstract reachable-distinct-state count, (ii) **energy-to-reacquire
the foreclosed option** — and test which better predicts the option-preserving /
protective behaviour under manipulated forecast uncertainty.
- **ANSWERED "energy-grounding stronger"** iff the energy-to-reacquire parameterization
  predicts committed behaviour better than (or subsumes) the abstract-count one.
- **ANSWERED "abstract suffices"** iff the two are behaviourally indistinguishable →
  keep the real-options/empowerment framing.

**Version:** v3, **substrate_conditional** — inherits MECH-454's two missing substrates
(reachable-option-dissociating env + E3 option-value term). A V4 meta-leg (reasoning about
energy over REE's OWN future option-space) is already folded into the self_model_v4 plan.
**Lit anchor:** Catenacci Volpi 2020, Hayashi 2025 (§2c); energy-grounding is the OPEN
move. **Bears on:** MECH-454, INV-026, SD-012, MECH-320.

---

## 4. Recommended registration form

**RECOMMENDED (matches the Q-040 precedent):** register Q-080.a/b/c as **embedded
testable scaffolding inside the Q-080 entry** — a `status_note` block
(`narrow_open_question applied`) enumerating the three sub-questions with their tests,
version scopes, and lit anchors, plus fold the (a)/(b)/(c) structure into `what_would_answer`.
Q-080 stays `status: open`; **no new claim IDs minted**; no status change. Add
`version_relevance: v3` to Q-080 and note the per-sub-question scopes inline.

- **Pro:** exact precedent (Q-040), zero registry-ID inflation, keeps them as scaffolding
  under the parent (not standalone `believed`/`asked` claims), maximally faithful to
  "pose the question first."
- **Con:** the sub-questions don't get their own top-level `version_relevance` field or
  independent `depends_on` graph edges.

**ALTERNATIVE (if you want standalone entries):** register Q-080.a/b/c as three separate
`open_question` entries, each `polarity: open`, `status: open`, `version_relevance: v3`
(Q-080.c substrate_conditional), `depends_on: [Q-080, …substrate deps]`, with the tests
above as their `what_would_answer`.

- **Pro:** each sub-question is independently trackable, version-scoped as its own field,
  and directly queue-able via `/queue-experiment`.
- **Con:** three new IDs into the open-question registry for a question the parent already
  holds; heavier than the Q-040 precedent.

---

## 5. Approval gate (Step 7)

Per-sub-question approve / edit / reject, plus the registration-form choice, requested
from the user before any `claims.yaml` edit. **Concurrency note:** an active TASK_CLAIMS
entry from another session ("cross_stream_binding repair") currently lists
`REE_assembly/docs/claims/claims.yaml`; registration must coordinate with / wait for that
claim to clear, re-reading the Q-080 insertion region immediately before editing.
