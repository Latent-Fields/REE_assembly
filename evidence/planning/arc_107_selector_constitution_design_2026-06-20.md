# ARC-107 design proposal: basal-ganglia-like E3 selector constitution

**Date:** 2026-06-20
**Status:** FORMAL DESIGN PROPOSAL (promoted from thought intake per s10 of
`thought_intake_2026-06-20_basal_ganglia_selector_constitution.md`).
**Trigger to promote:** V3-EXQ-689a landed **readiness-met / no-lift** on the
pre-registered conflict-graded 2x2 (ARM_A1B1 no-lift; Factor A inert; Factor B
alone converts 2/3 but A1B1 destructively cancels). Per the note's s5.3 / s10
branch, this is the sanctioned point to turn the design-pressure note into a
formal proposal. User-adjudicated 2026-06-20: the near-tie parametric lever
family is exhausted -> **elevate the constitution build**.
**Owns:** ARC-107 (architecture), MECH-448 (lead mechanism), MECH-449 (Go/No-Go
constitution), Q-078 (umbrella question). Grounded under ARC-106 (brain-like
construction; this is its first major worked application).
**Cross-plan home:** `biology_grounding_convergence_v4_plan` BG-2 (selector) +
BG-3 (commit latch); `behavioral_diversity_isolation:GAP-I`; substrate-queue
entry `f_dominance_conversion_ceiling`.

---

## 0. V3-EXQ-689c does NOT gate this build (corrected 2026-06-20)

**Earlier drafts of this note gated the build on V3-EXQ-689c. That was wrong and
is retracted.** Per origin/master commit `feb5184824` (MECH-442 packet Section 7,
user decision 2026-06-20, ARC-106 anti-shortcut steer): **689c is stripped of
decision authority.** It is pure no-authority confirmatory data.

The ARC-107 BG-constitution build (LEAD MECH-448 rank-preserving F->eligibility
demotion; follow-on MECH-449) **proceeds regardless of what 689c shows.** Three
independent reasons, none of which 689c can change:

1. **689c is inside the family already adjudicated as exhausted.** Factor-B-alone
   (gap-scaled commit-T) is a *near-tie parametric* lever. The user adjudicated
   the whole near-tie parametric family closed after 689a (readiness-met/no-lift,
   A1B1 destructive cancel). 689c cannot reopen a path closed by decision.
2. **689c carries no new information.** Factor-B's conversion was already observed
   in 689a's own 2x2 (ARM_A0B1 = 0.850, 2/3). 689c only re-isolates a number we
   have; it cannot return new architectural signal.
3. **A Factor-B "PASS" is anti-evidence, not support.** Factor-B raises committed
   entropy by hotting the commit argmax -- stochasticity, not lawful access. That
   is exactly the noise-as-diversity failure mode this note's own acceptance
   criteria reject (s8 #8; risk s9.3). So even a Factor-B PASS does NOT rescue the
   parametric reading or shelve the constitution; it just logs a parametric fact
   in the divergence ledger.

**Therefore:** grounding, design, the claim re-grain, AND the MECH-448 build are
all unconditional on 689c. The real (short) gate for the re-grain + substrate-queue
amend was the governance-689a cycle releasing `claims.yaml` / `substrate_queue.json`
-- which has since LANDED (`7419453d1d`). If 689c ever lands, it only annotates the
divergence ledger.

---

## 1. The problem, restated as a selection-structure fault

Across mechanistically distinct channels (CRF 654g, OFC 485h, SD-037 625e,
dACC 445h, modulatory 569g) the cluster pattern is identical:

```
upstream signal forms -> is measurable -> reaches E3 authority -> committed action does not change
```

The current selector still behaves too much like `candidates -> scalar (F)
score dominance -> committed argmin`. F (the primary harm/goal score)
monopolises ~88-89% of E3 committed-selection variance (V3-EXQ-571), unmoved by
the full diversity stack. Every diversity channel drowns at the same gate.

The required architecture is constitutional, not parametric: **a signal's
STRENGTH must be necessary but not sufficient -- it also needs LAWFUL ACCESS to
committed action.**

```
candidates -> eligibility set -> Go/No-Go pressures -> conflict-hold
           -> threshold modulation -> recurrent competition
           -> context arbitration -> commitment permission -> post-commit latch
```

---

## 2. Already-built partial instances (REUSE, do not duplicate -- ARC-106 guardrail 2)

`e3_selector.py` already implements pieces; the constitution is an
amend/generalisation, not a greenfield rewrite:

| Component | Already in e3_selector.py | Gap the constitution fills |
|---|---|---|
| Eligibility set | `use_modulatory_shortlist_then_modulate` (margin / top_k shortlist) | shortlist is a HARD cutoff and (top_k) ENV-CONDITIONAL (569i works only on the reef-bipartite structural guarantee, fails under threat-engaged pool -- 625d autopsy). Needs a **graded, env-general** eligibility envelope. |
| Conflict-graded width (hyperdirect) | Factor A: `modulatory_shortlist_conflict_graded`, `k=f(F-gap)` | 689a: **inert**. Drop or demote to decorative unless an ablation rescues it. |
| Commit temperature (near-tie hotting) | Factor B: `_gap_scaled_commit_pick`, `T=f(F-gap)` | 689a: converts 2/3 alone; A1B1 cancels. 689c isolates it. Parametric, not constitutional. |
| Within-set arbitration | `_modulatory_accum` arbitrates winner inside shortlist | still loses to F because F also sets the shortlist AND ranks within it. **MECH-448 removes F from the within-eligible argmin.** |
| No-Go (indirect pathway) | MECH-260 (dACC indirect-pathway suppression) | present but channel-specific; MECH-449 generalises into bounded No-Go set governance. |
| Post-commit latch | SD-034 / MECH-090 / MECH-342 / MECH-445 / MECH-446 | the commit/release-duration FACE of F-dominance (460h); owned by the `f_dominance_conversion_ceiling` commit-entry-decisiveness rung (root C). |

---

## 3. The constitution, component by component (ARC-106 grounded)

Each component below carries: **Function** (what it does), **REE translation**
(how), **Divergence** (where REE departs from biology and why -- the ledger
entry), **Ablation falsifier** (the test that proves it load-bearing not
decorative), and **Psychiatric failure mode** (the ARC-106-mandated clinical
mapping -- what breaks if this component breaks).

> **ARC-106 grounding (L2, landed 2026-06-20).** The lit-pull that anchors each
> component below at ARC-106 level L2, with the per-component divergence-ledger
> entries and psychiatric-failure-mode mappings worked in full, is:
> `evidence/literature/targeted_review_connectome_mech_439/ARC107_GROUNDING_SYNTHESIS.md`
> (extends the existing MECH-439 BG-selector review; 5 new entries -- Kravitz 2010
> D1/D2 opponency, Mink 1996 focused selection, Chevalier & Deniau 1990
> disinhibition, Hikosaka 2000 SNr permission gate, Maia & Frank 2011 Go/No-Go
> disorders -- plus the pre-existing STN/normalisation entries for components 2 and 4).
> This discharges the §6 step-1 unconditional grounding chip. None of the
> components is yet at L3 -- that requires the post-689a/689c falsifier.

### 3.1 MECH-448 -- Rank-preserving F->eligibility demotion (LEAD)

- **Function (pallidal permission over an F-graded eligibility set):** F decides
  who is *eligible* to compete, not who *wins*. Within the eligible set, a
  modulatory/diversity channel arbitrates the committed action; F is removed
  from the final argmin.
- **REE translation:** graded eligibility envelope by rank-preserving
  renormalisation against the competing field (divisive-normalisation analog),
  *then* within-eligible arbitration by `_modulatory_accum` (already built).
  No-op default; bit-identical OFF.
- **Divergence (ARC-106 ledger):** canonical divisive normalisation
  (Carandini & Heeger 2012; value DN, Louie/Khaw/Glimcher 2013) is
  ORDER-PRESERVING + POOLED-SYMMETRIC. REE demotes ONLY F and removes it from
  the commit argmin (rank-ALTERING at commit) -- this EXCEEDS canonical DN and
  needs the QD/MAP-Elites justification (CDQ-003). LOAD-BEARING divergence,
  must be lit-anchored + falsifier-validated.
- **Ablation falsifier (V3-EXQ-689a-successor):** committed-class entropy
  reaches the proposer ceiling on >=2/3 seeds **AND** order is preserved on the
  numerators (F still ranks within-eligible) **AND** no harmful action class is
  globally disinhibited (safety). WEAKENED if entropy lifts only by globally
  flattening F (loses signal / admits harmful classes) or if the Factor-B
  near-tie lever already reaches the ceiling (689c). NON-DEGENERACY: the
  envelope must actually exclude non-eligible candidates (bounded, not all-pass).
- **Psychiatric failure mode:** envelope too wide / F removed without bounded
  No-Go -> disinhibition, impulsivity, action-selection without value gating
  (mania / OCD-spectrum loss of inhibitory braking). Envelope too tight ->
  bradykinesia/avolition analog (the current failure: nothing but F converts).

### 3.2 MECH-449 -- Go/No-Go eligibility constitution (FOLLOW-ON, substrate_conditional)

- **Function:** committed-action diversity is recovered by an explicit
  eligibility CONSTITUTION -- bounded **Go** (promote a channel when
  evidence/value/drive/rule/safety make it eligible) AND bounded **No-Go**
  (suppress unsafe / stale / perseverative / irrelevant / low-viability
  channels) governing which candidates may compete for the
  pallidal-like permission gate. Lawful channel-specific access, not scalar
  dominance, decides.
- **REE translation:** generalise MECH-260 (existing No-Go) into a bounded
  Go/No-Go pressure set over the eligibility envelope; MECH-448 demotion is ONE
  component of the broader governance.
- **Divergence (ARC-106 ledger, L2-anchored 2026-06-20):** direct/indirect
  pathway opponency is causally established (Kravitz 2010: D1/D2 are genuinely
  SEPARATE, oppositely-signed populations; Mink 1996: focal-go + surround-no-go).
  REE's divergence: it folds Go and No-Go into algorithmic eligibility pressures
  over an abstract candidate set -- no separate populations, no vigour axis -- and
  collapses multi-loop cortico-striatal arbitration into a single shared
  commitment interface (s4 "contextual loops"). **Reuse-before-duplicate (G2):**
  MECH-260 already hosts a No-Go-like function; MECH-449 must GENERALISE it, not
  add a parallel module. Full ledger entry: grounding synthesis §2.1.
- **Ablation falsifier:** a built Go/No-Go constitution CONVERTS >=1
  previously-gated downstream channel beyond what MECH-447/448 achieve;
  over-specification if it does not.
- **Psychiatric failure mode:** No-Go over-pressure -> perseveration /
  catatonia analog; Go over-pressure -> tics / compulsions; mis-routed context
  arbitration -> context-inappropriate action (a model handle for several
  disorders -- to be made precise in the lit-pull).
- **Gate (INVERTED 2026-06-21, anti-partial-instantiation):** MECH-449 is a
  roadmap leg of ARC-107, NOT a contingency that fires only if MECH-448 fails.
  The earlier "build only if the demotion lever proves insufficient" gate is
  retracted: it makes a *passing* MECH-448 silently foreclose the rest of the
  constitution -- structurally the same trap as the F-dominance route (a local
  win declared circuit-complete). The discriminating question is "what does
  bounded Go/No-Go SUPPRESSION add that rank-preserving demotion structurally
  cannot" -- and rank-preserving demotion is order-preserving, so it can never
  *exclude* an unsafe/stale/perseverative candidate that is F-eligible; only an
  active No-Go can. **Positive build trigger:** V3-EXQ-689f, the No-Go-necessity
  falsifier (§6 step 4b) -- a selection-face diagnostic that demonstrates the
  demotion-insufficient regime. A PASS motivates the MECH-449 build directly;
  the build no longer waits on downstream behavioural retests stumbling into the
  gap. (`epistemic_category: substrate_conditional` is unchanged -- it suppresses
  promote/demote until the constitution is built + tested; only the *build
  decision* is inverted.) NOT gated on 689c (see section 0).

### 3.3 MECH-447 -- conflict-graded near-tie sufficiency (PARAMETRIC; likely demote)

- 689a verdict: Factor A inert; Factor B converts only via commit-temperature
  hotting (noise-as-diversity); A1B1 destructively cancels. Disposition (settled
  on 689a alone, NOT pending 689c -- see section 0): MECH-447 is WEAKENED toward
  refuted and is the loser of the 447<->448 rival pair; the A/B dissociation is
  the split. The constitutional reading (MECH-448) is supported. The
  /claim-synthesis re-grain finalises this disposition now (it does not wait on
  689c).

---

## 4. Acceptance criteria for any constitution experiment (from note s8)

A selector-constitution experiment does NOT succeed merely because action
entropy increases. It must show:

1. **Non-vacuity** -- channels form and reach the selector.
2. **Selector engagement** -- eligibility / hold / Go-NoGo variables vary as intended.
3. **Specificity** -- the relevant channel changes action only where it should.
4. **Gap/conflict sensitivity** -- if claimed, effect scales with measured conflict / top-F gap.
5. **Gap-blind controls** -- non-specific widening/hotting does NOT explain the lift.
6. **Safety** -- no global disinhibition of harmful/irrelevant classes.
7. **Retest transfer** -- >=1 previously-gated downstream channel converts.
8. **No noise-as-diversity** -- added stochasticity alone does not count.

The discriminant is **lawful, channel-specific, context-appropriate conversion
into committed action**, not entropy.

---

## 5. Risk register (from note s9)

- **Overbuild** -- gate the BROADER MECH-449 build behind MECH-448's outcome;
  build the lead MECH-448 lever no-op-default first. (Not gated on 689c.)
- **Cargo-cult biology** -- each analogue needs function + divergence ledger +
  falsifier before it counts as load-bearing (ARC-106 ablation test).
- **Noise-as-diversity** -- criterion 8 above is the guard.
- **Upstream invalidation** -- do not use a selector repair to paper over local
  signal-quality failures where readiness is not met.
- **Commitment instability** -- eligibility/hold machinery must couple to a
  stable post-commit latch (SD-034 family / the root-C commit-entry rung).

---

## 6. Build sequence (the chips spawned from this note)

1. **Grounding lit-pull (unconditional, now):** basal ganglia / STN-hyperdirect
   conflict-hold / direct-indirect Go-NoGo / pallidal permission gate / value
   divisive normalisation. Produces ARC-106 L2 anchors + divergence-ledger
   entries for 3.1-3.2. Routes to `targeted_review_connectome_mech_439`
   extension. **DONE 2026-06-20:**
   `targeted_review_connectome_mech_439/ARC107_GROUNDING_SYNTHESIS.md` + 5 new
   entries (Kravitz/Mink/Chevalier-Deniau/Hikosaka/Maia-Frank). All five
   components at L2 with divergence ledger + psychiatric column drafted.
2. **Claim re-grain (UNCONDITIONAL; gate was governance-689a, now LANDED):**
   /claim-synthesis over MECH-447/448/449 -- decide genuinely-independent children
   vs design alternatives; set MECH-447 disposition from 689a alone (weakened,
   447<->448 rival pair, A/B split); elevate MECH-448 to active build; hold
   MECH-449 substrate_conditional. Reconcile decision_state + closure node
   (derive-only gotcha). NOT gated on 689c.
3. **MECH-448 build (UNCONDITIONAL on 689c; in flight):** /implement-substrate --
   amend `f_dominance_conversion_ceiling`: add the rank-preserving F->eligibility
   demotion lever to e3_selector.py, no-op-default, contracts + activation smoke.
4. **MECH-448 falsifier (sequenced AFTER build 3):** /queue-experiment --
   689a-successor on the demotion lever, acceptance criteria s8. **DONE:**
   V3-EXQ-689d PASS all 4 criteria (2026-06-21); MECH-448 promoted provisional.
4b. **MECH-449 No-Go-necessity falsifier (NEW, 2026-06-21; positive trigger for
   step 5):** /queue-experiment -- V3-EXQ-689f, a selection-face / commitment-free
   diagnostic showing the demotion-insufficient regime: present a candidate set
   containing unsafe / stale / perseverative / low-viability options that are
   F-eligible, and show the rank-preserving MECH-448 envelope ADMITS them
   (order-preserving -> cannot exclude an eligible-but-undesirable candidate),
   whereas a bounded No-Go would suppress them. A PASS is the positive evidence
   that motivates step 5 -- replacing the old "wait until 448 fails downstream"
   gate. Runnable on the CURRENT substrate (MECH-448 built; MECH-449 not) because
   it measures a *gap* in the built envelope, not MECH-449 itself.
5. **MECH-449 build (positively triggered by step 4b, NOT contingent on 448
   failing):** /implement-substrate -- generalise MECH-260 into bounded Go/No-Go
   pressure over the eligibility envelope. Roadmap leg of ARC-107; build proceeds
   on a 689f PASS.

---

## 6b. Completeness ledger (anti-partial-instantiation closure criterion)

**Why this section exists.** The F-dominance route failed because a partial
mechanism (selection-readout near-tie levers) returned a local win and was
treated as the answer until it was exhausted. MECH-448 just returned a strong
local win (V3-EXQ-689d: committed-class entropy 0.938 vs 0.371, ~2x). That is
*exactly* the moment the same trap springs. This ledger makes "is the
constitution actually instantiated?" a checklist rather than a vibe, so a
component-3 win cannot masquerade as a complete circuit.

### V3 constitution components (the ARC-107 scope)

| # | Component | Owner | Build status (2026-06-21) |
|---|---|---|---|
| 1 | Direct/indirect **Go/No-Go opponency** (striatal channel competition; active SUPPRESSION of unsafe/stale/perseverative/low-viability channels) | MECH-449 | **NOT BUILT** -- substrate_conditional. Positive build trigger = V3-EXQ-689f (No-Go-necessity falsifier). This is the core of BG and the most load-bearing gap. |
| 2 | **STN/hyperdirect conflict-graded hold** (threshold raise / candidate-set widening under conflict) | MECH-447 | **EXHAUSTED** -- 689a: Factor A inert, A1B1 destructive. Parametric family closed by decision. Either drop to decorative or an ablation must rescue it; cannot be silently assumed present. |
| 3 | **Pallidal permission-to-commit gate** (F decides eligibility, not the winner; F removed from the within-eligible argmin) | MECH-448 | **BUILT + VALIDATED + provisional** (689d PASS). Channel-adaptive floor in flight (689e). This is the ONLY fully-landed component. |
| 4 | **Value divisive-normalisation** (rank-altering at commit; CDQ-003 load-bearing divergence) | folded into MECH-448 | **PARTIAL** -- realised only as the demotion envelope's denominator. Counts only as part of component 3, not as independent coverage. |
| 5 | **Post-commit latch / de-commit** (commitment stability; the root-C commit-entry-decisiveness face) | SD-034 / MECH-090 / MECH-342 / MECH-445 / MECH-446 | **OPEN** -- 460j is the 8th iteration, design-rethink flagged (latch-hold yields to SD-034 de-commit). Eligibility/hold machinery is unsafe without a stable latch (s5 risk). |
| 5b | **Psychiatric-failure-mode column** (ARC-106 mandate; documentation, not a mechanism) | grounding synthesis | **DRAFTED** at L2 for all components. Not a runtime component. |

### V4+ axes -- explicitly OUT of V3 ARC-107 scope (must be a STATED bet, not a silent cut)

The full biological basal ganglia also includes the following. Deferring them to
v4 may be the right call, but per ARC-106 (zero *silent* divergence) the deferral
must be a named, falsifiable bet, not an unspoken scope cut:

| Axis | Home | Bet to register |
|---|---|---|
| **Vigor / opportunity-cost** (tonic DA sets action amplitude/latency) | `biology_grounding_convergence_v4_plan` BG-4 | "V3 committed-action behaviour does not require a vigor/opportunity-cost axis." |
| **Action chunking / sequencing** (dorsolateral striatal habit loops; sustained multi-step commitment) | v4 | "V3 commitment is single-decision; multi-step action-commitment chunking is v4." (Note: this is the exact layer the don't-queue-commitment-dependent-behaviour gate already protects.) |
| **Dopaminergic RPE learning signal** (TD learning rule on eligibility) | v4 | "V3 eligibility is hand-shaped, not learned by RPE; the learning signal is v4." |
| **Thalamocortical recurrence / beta-gating** | BG-3 latch face (partial) | "V3 closes the loop with the SD-034 latch family, not explicit thalamocortical oscillation." |
| **Multi-loop cortico-striatal arbitration** (separate motor / cognitive / motivational loops) | v4 | "V3 collapses all loops into one shared commitment interface (s4 contextual-loops divergence)." |

### Closure criterion (the forcing function)

**ARC-107 may NOT be promoted past `candidate`, and the constitution may NOT be
called instantiated, on MECH-448 alone.** Minimum bar for "constitution
complete (V3 scope)":

1. Component **1 (Go/No-Go opponency)** built and shown load-bearing by its own
   ablation falsifier (ARC-106 test) -- not just present.
2. Component **2** either functional or its removal explicitly justified in the
   divergence ledger (decorative-by-decision, not by neglect).
3. Component **3** landed (done) + component **5 (post-commit latch)** coupled so
   commitment is stable.
4. Each component passes the ARC-106 load-bearing-vs-decorative ablation test.
5. Each deferred v4 axis above is registered as a stated bet.

ARC-107's own claim definition already enforces most of this (it names Go/No-Go +
hold + pallidal gate + latch), so the structural guardrail exists; this ledger is
the operational tracker that someone must DRIVE rather than letting ARC-107 sit
`candidate` while behaviour rides on component 3.

### Operational drift signal (the early-warning the F-dominance route lacked)

If **N>=3 consecutive in-flight selector experiments all iterate component 3
(MECH-448 envelope-floor calibration / lettered demotion retests)** with no
component-1 build and no 689f-class No-Go diagnostic queued, that is the
partial-instantiation signature recurring -- flag it in `/governance` and route
to step 4b/5. (As of 2026-06-21 the live queue is 689e + 654i, *both* component-3
iterations -- the signal is already at N=2.)

---

## 7. Cross-references

- Thought intake (pre-689a capture): `thought_intake_2026-06-20_basal_ganglia_selector_constitution.md`
- Autopsy: `evidence/experiments/failure_autopsy_V3-EXQ-689a_2026-06-20.md`
- Conversion-ceiling Phase-0/1 synthesis: `conversion_ceiling_phase0_synthesis_2026-06-18.md`
- Claims: ARC-107, MECH-447, MECH-448, MECH-449, Q-078 (claims.yaml); ARC-106 grounding framework `docs/architecture/arc_106_biology_grounding_framework.md`
- ARC-106 grounding synthesis (SELECTION face -- L2 anchors + divergence ledger + psychiatric column): `evidence/literature/targeted_review_connectome_mech_439/ARC107_GROUNDING_SYNTHESIS.md`
- ARC-106 grounding synthesis (COMMIT/RELEASE-DURATION face -- the s2 last-row post-commit latch / s5 "commitment instability" risk; BG-3 cluster SD-034/MECH-090/MECH-342/MECH-445/MECH-446; load-bearing divergence = tuned beta-gate refractory vs biology's graded BG/pallidal urgency + behaviour-co-extensive maintenance; psychiatric poles perseveration/catatonia vs distractibility/disorganisation): `evidence/literature/targeted_review_commit_release_duration_latch/SYNTHESIS.md` (BG-3 grounding, lit-pull-bg3 session 2026-06-20)
- Substrate queue rung: `f_dominance_conversion_ceiling` (substrate_queue.json)
