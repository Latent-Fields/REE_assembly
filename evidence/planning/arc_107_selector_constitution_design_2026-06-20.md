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

## 0. Live dependency: V3-EXQ-689c (do not pretend it isn't running)

A concurrent session has **V3-EXQ-689c** in flight: Factor-B-alone (gap-scaled
commit-T) isolation retest -- the converter 689a's 2x2 pointed at. Its outcome
conditions HOW MUCH of this constitution we build:

| 689c outcome | reading | consequence for ARC-107 build |
|---|---|---|
| Factor-B-alone PASS, gap-CONCENTRATED | parametric win on one factor (s5.1) | refine/keep Factor B; ARC-107 stays as the V4 grounding roadmap; **do NOT broaden** the selector now. MECH-447 partially rescued. |
| Factor-B-alone PASS, gap-BLIND / uniform | non-specific hotting (s5.2) | Factor B is not validated as conflict-grading; **escalate to MECH-448 demotion**. |
| Factor-B-alone FAIL / no-lift | near-tie family fully exhausted (s5.3) | **MECH-448 + MECH-449 are the path.** Constitution build is the clear next step. |

**Therefore:** the *grounding* (lit-pull) and *design* (this note) are
unconditional -- ARC-107 is already registered and needs its ARC-106 grounding
regardless. The *claim re-grain* and the *demotion-lever build/experiment* must
incorporate 689c when it lands. Sequencing is encoded in the chips below.

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
- **Gate:** build ONLY if 689c + MECH-448 show the near-tie + demotion levers
  are insufficient (note s5.3 branch A). Captured now; build is a later step.

### 3.3 MECH-447 -- conflict-graded near-tie sufficiency (PARAMETRIC; likely demote)

- 689a verdict: Factor A inert, A1B1 cancels. Standing reading: the parametric
  near-tie family is exhausted. 689c (Factor-B-alone) is the last hedge. If
  689c also fails to convert robustly, MECH-447 is WEAKENED toward refuted and
  the constitutional reading (MECH-448) is supported. The /claim-synthesis
  re-grain (chip) makes this disposition formal.

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

- **Overbuild** -- gate the broad build behind 689c + MECH-448; build the lead
  lever no-op-default first.
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
2. **Claim re-grain (gated on 689c):** /claim-synthesis over MECH-447/448/449 --
   decide genuinely-independent children vs design alternatives; set MECH-447
   disposition from 689a+689c; elevate MECH-448 to active build; hold MECH-449
   substrate_conditional. Reconcile decision_state + closure node (derive-only
   gotcha).
3. **MECH-448 build (gated on 689c outcome):** /implement-substrate -- amend
   `f_dominance_conversion_ceiling`: add the rank-preserving F->eligibility
   demotion lever to e3_selector.py, no-op-default, contracts + activation smoke.
4. **MECH-448 falsifier (sequenced AFTER build 3):** /queue-experiment --
   689a-successor on the demotion lever, acceptance criteria s8. NOT chipped yet
   (blocked on build 3).
5. **MECH-449 build (sequenced AFTER MECH-448 outcome):** only if demotion alone
   insufficient. NOT chipped yet (double-gated).

---

## 7. Cross-references

- Thought intake (pre-689a capture): `thought_intake_2026-06-20_basal_ganglia_selector_constitution.md`
- Autopsy: `evidence/experiments/failure_autopsy_V3-EXQ-689a_2026-06-20.md`
- Conversion-ceiling Phase-0/1 synthesis: `conversion_ceiling_phase0_synthesis_2026-06-18.md`
- Claims: ARC-107, MECH-447, MECH-448, MECH-449, Q-078 (claims.yaml); ARC-106 grounding framework `docs/architecture/arc_106_biology_grounding_framework.md`
- ARC-106 grounding synthesis (L2 anchors + divergence ledger + psychiatric column): `evidence/literature/targeted_review_connectome_mech_439/ARC107_GROUNDING_SYNTHESIS.md`
- Substrate queue rung: `f_dominance_conversion_ceiling` (substrate_queue.json)
