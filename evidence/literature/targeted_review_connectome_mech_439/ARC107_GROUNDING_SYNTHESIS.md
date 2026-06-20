# ARC-107 basal-ganglia selector constitution — ARC-106 grounding synthesis

**Date:** 2026-06-20
**Owns grounding for:** ARC-107 (architecture), MECH-448 (lead mechanism), MECH-449 (Go/No-Go constitution), Q-078 (umbrella question), under ARC-106 (brain-like construction).
**Method:** ARC-106 grounding ladder (L0→L3), load-bearing-vs-decorative ablation test, living divergence ledger, required psychiatric-failure-mode column (`docs/architecture/arc_106_biology_grounding_framework.md`).
**Companion design note:** `evidence/planning/arc_107_selector_constitution_design_2026-06-20.md` §3.
**Scope of this artifact:** it brings each ARC-107 BG analogue to **L2 (literature-anchored)**, drafts its divergence-ledger entry, and maps its psychiatric-failure-mode. It does **not** move any component to L3 — that requires the REE falsifier (the post-689a successor experiments), which is downstream of this prep work.

This review extends `targeted_review_connectome_mech_439` (the BG-selector connectome review). The 7 pre-existing entries (Frank 2006, Cavanagh 2011, Bogacz 2007, Aron 2006 — STN/hyperdirect; Carandini 2012, Louie 2013, Reynolds 2009 — divisive normalisation) already anchor components 2 and 4; this pass adds 5 entries (Kravitz 2010, Mink 1996, Chevalier & Deniau 1990, Hikosaka 2000, Maia & Frank 2011) for the uncovered components 1, 3, and 5. Together the 12 entries anchor the full constitution.

*According to PubMed* for the five newly-added biomedical sources; DOIs are linked per entry below.

---

## 1. Component → lit-anchor → grounding-level map

| # | ARC-107 component | Lit anchors (entry) | Level | Owns |
|---|---|---|---|---|
| 1 | **Direct/indirect Go/No-Go opponency** (striatal channel competition) | Kravitz et al. 2010 (causal D1/D2 opponency); Mink 1996 (focused selection + surround inhibition) | **L2** | MECH-449, MECH-448 |
| 2 | **STN/hyperdirect conflict-graded hold** (decision-threshold modulation) | *existing:* Frank 2006, Cavanagh 2011, Aron 2006, Bogacz 2007 | **L2** (689a verdict in) | MECH-447 (parametric), ARC-107 hold leg |
| 3 | **Pallidal output gate as permission-to-commit** (disinhibition, not argmax) | Chevalier & Deniau 1990 (disinhibition); Hikosaka 2000 (SNr→SC gate + context); Mink 1996 (focal release) | **L2** | MECH-448 |
| 4 | **Value divisive normalisation** — and the MECH-448 rank-ALTERING divergence | *existing:* Carandini 2012, Louie 2013 (order-preserving, pooled-symmetric DN); *this pass:* Kravitz 2010 (opponent populations = the biological basis for rank alteration) | **L2** | MECH-448 |
| 5 | **Go/No-Go imbalance disorders** (the psychiatric-failure-mode column) | Maia & Frank 2011 (RL/Go-No-Go → Parkinson's, OCD, Tourette's, ADHD, addiction) | **L2** | MECH-449 column; MECH-448 column |

---

## 2. Divergence ledger (ARC-106 §5 schema, drafted to L2)

Schema: **component | REE construction | neural analog (function) | level | key divergence | load-bearing? | psychiatric failure mode | status**

### 2.1 Go/No-Go opponency (component 1) — MECH-449 / MECH-448

- **REE construction:** today, none — F is a single additive scalar and the "No-Go" is only MECH-260's channel-specific dACC suppression. MECH-449 adds a bounded Go (eligibility-promotion) + bounded No-Go (eligibility-suppression) pressure set.
- **Neural analog (function):** D1 direct (Go / facilitate) and D2 indirect (No-Go / suppress) striatal pathways as **genuinely separate, oppositely-signed** populations whose balance sets behaviour (Kravitz 2010, causal optogenetic; Mink 1996, focused selection + surround inhibition).
- **Key divergence (LOAD-BEARING):** biology realises opponency with two distinct populations operating on movement vigour; REE folds Go and No-Go into algorithmic eligibility pressures over an abstract candidate set, with no separate populations and no vigour axis. **Reuse-before-duplicate (ARC-106 G2):** MECH-260 already hosts a No-Go-like function — MECH-449 must *generalise* it, not add a parallel module.
- **Ablation falsifier (L2→L3):** a built Go/No-Go constitution converts ≥1 previously-gated downstream channel beyond what MECH-447/448 achieve; decorative if not (design note §3.2).
- **Psychiatric failure mode (Maia & Frank 2011):** No-Go over-pressure → perseveration / catatonic action-collapse; Go over-pressure → tics / compulsions / impulsivity; mis-routed context arbitration → context-inappropriate action.
- **Status:** L2 anchored. MECH-449 substrate_conditional (build double-gated behind 689c + MECH-448).

### 2.2 STN/hyperdirect conflict-graded hold (component 2) — MECH-447

- **REE construction:** Factor A `modulatory_shortlist_conflict_graded`, `k=f(F-gap)`; Factor B `_gap_scaled_commit_pick`, `T=f(F-gap)`.
- **Neural analog (function):** cortico-STN hyperdirect pathway raises the decision threshold under response conflict — "hold your horses" (Frank 2006; Cavanagh 2011 mediofrontal theta; Aron 2006; Bogacz 2007 MSPRT). *Already anchored by the existing entries.*
- **Key divergence (LOAD-BEARING, already in the existing Frank-2006 entry):** the STN raises a **continuous temporal** threshold on a within-trial accumulator (buys time for more evidence); REE widens a **discrete set** (top-k) at a single commit step with no temporal accumulation. The hold is inert wherever F also dominates the within-shortlist scoring.
- **689a verdict (in):** the combined conflict-grade form (A1B1) does **not** convert; Factor A alone is inert; only Factor B (gap-scaled commit-T) converts alone, and A poisons B. The parametric near-tie family is exhausted → elevate the constitution (this is why ARC-107 is being built).
- **Psychiatric failure mode:** STN-DBS loss of the hold → impulsive choice under conflict (Cavanagh 2011); over-hold → freezing/indecision.
- **Status:** L2, falsifier returned. MECH-447 weakened toward refuted; 689c isolates Factor B as the last parametric hedge.

### 2.3 Pallidal permission-to-commit gate (component 3) — MECH-448

- **REE construction:** today, unconditional `argmin J(ζ)`. MECH-448 reframes commitment as **permission over an F-graded eligibility set** (no-op default, bit-identical OFF).
- **Neural analog (function):** BG output (SNr/GPi) **tonically inhibits** motor targets; selection is the **focal release** (disinhibition) of the chosen target, default-deny (Chevalier & Deniau 1990; Hikosaka 2000 SNr→SC, with electrophysiology + context modulation; Mink 1996 focal release + surround).
- **Key divergence (LOAD-BEARING):** biology's gate is literal tonic GABAergic inhibition phasically paused; REE implements permission as an algorithmic commit-entry predicate, not a released brake. The biological default state is "everything inhibited" → the **default failure of a mis-set gate is global akinesia** (nothing converts), which in the aggregate metric looks identical to a genuine upstream ceiling — the falsifier's non-degeneracy + safety checks must separate them.
- **Double-edged grounding (Hikosaka):** the same circuit that grounds multi-channel context arbitration also shows reward expectation *facilitating the rewarded saccade* — i.e. the substrate **can still collapse onto one dominant value channel** at the gate. So component 3 grounds the structure *and* documents the F-monopoly failure mode; it does **not** show that adding a gate is sufficient (the gate buys flexibility only if its eligibility input is multi-channel, not F alone).
- **Ablation falsifier (L2→L3):** the eligibility envelope must actually exclude non-eligible candidates (bounded, not all-pass) AND order is preserved on the numerators (design note §3.1 non-degeneracy).
- **Psychiatric failure mode:** envelope too tight / gate over-closed → bradykinesia / avolition (the current REE failure); envelope too wide / gate over-open → disinhibition / impulsivity.
- **Status:** L2 anchored. MECH-448 = lead build (gated on 689c outcome).

### 2.4 Value divisive normalisation and the MECH-448 rank-altering divergence (component 4) — MECH-448

- **REE construction:** MECH-448 demotes **only F** to a graded eligibility envelope and **removes it from the committed argmin**, letting a modulatory channel arbitrate within the eligible set.
- **Neural analog (function):** canonical divisive normalisation — every value divided by a shared pooled field (Carandini & Heeger 2012; value-DN: Louie/Khaw/Glimcher 2013). *Already anchored by the existing entries.*
- **Key divergence (THE load-bearing one, design note §3.1 / ARC-106 §4.4 model case):** canonical DN is **order-preserving** and **pooled-symmetric** — alone it keeps F the argmax. MECH-448 is **rank-ALTERING** and **single-target** (F demoted, removed from argmin) — it *exceeds* canonical DN and therefore needs its own justification (QD/MAP-Elites, **CDQ-003**). The biological basis for *rank alteration* (which symmetric DN cannot do) is **opponent population competition** (Kravitz 2010): the brain overrides a would-be winner via a separately-controllable suppression channel, not via symmetric renormalisation. So MECH-448's stronger-than-DN operation is grounded in the Go/No-Go opponency, not in DN itself.
- **Ablation falsifier (L2→L3, = V3-EXQ-689a-successor):** committed-class entropy reaches the proposer ceiling on ≥2/3 seeds **AND** order preserved on the numerators **AND** no harmful class globally disinhibited. Weakened if entropy lifts only by globally flattening F.
- **Psychiatric failure mode:** flattening F globally (faithful-but-wrong DN import) → loss of value signal, admits harmful classes (disinhibition); over-tight demotion → avolition.
- **Status:** L2 anchored; divergence is the registered CDQ-003 justification target.

### 2.5 Psychiatric-failure-mode column (component 5) — cross-cuts MECH-448 / MECH-449

- **Source:** Maia & Frank 2011 — the canonical RL/Go-No-Go → disorder map (Parkinson's, Tourette's, OCD, ADHD, addiction, schizophrenia).
- **What it grounds:** the ARC-106-mandated requirement that each component's breakage map to a recognisable disorder. The bidirectional dopamine-graded dyad (under-Go/over-No-Go → Parkinsonian bradykinesia + perseveration + anhedonic collapse; over-Go/under-No-Go → impulsivity + the manic pole; OCD-spectrum → braking loss) supplies the column for §2.1, §2.3, §2.4 above.
- **Discipline (ARC-106 §7):** model-of-a-model. A REE selector failure earns a disorder label only by reproducing the **specific signature** (e.g. perseveration *with intact value learning*), not by sharing the word; the falsifier must localise which failure each lever produces; a row may honestly carry "no clean analog." Catatonic action-collapse is the *extreme* of the No-Go-over-pressure pole — flagged as the strongest reading of the current "nothing but F converts" failure, but its label is earned only if a built No-Go over-pressure reproduces global commit suppression *with* preserved upstream candidate formation (the non-degeneracy precondition).

---

## 3. What this changes for the build

- **The constitution is L2-grounded, not L3.** Every component now has a literature anchor and a drafted divergence + psychiatric mapping. None is validated — that is the post-689a/689c falsifier's job. This artifact discharges the design note §6 step-1 "grounding lit-pull (unconditional, now)" chip and is the precondition for the §6 step-3 MECH-448 build.
- **The most load-bearing divergence (component 4) is anchored on both sides:** canonical DN's order-preservation (existing Louie/Carandini entries) *and* the biological basis for exceeding it via opponent competition (Kravitz). CDQ-003 remains the registered QD/MAP-Elites justification for the rank-altering step.
- **Two grounding entries are deliberately double-edged** (Hikosaka §2.3, Maia & Frank §2.5): they ground the structure *and* document the failure mode the structure can still fall into. This is honest L2 grounding, not cheerleading — the gate/constitution buys nothing unless its eligibility input is genuinely multi-channel and its No-Go is bounded.
- **ARC-106 guardrails actively bind:** G2 (reuse-before-duplicate) forces MECH-449 to generalise MECH-260 rather than add a parallel No-Go module; G1 (function-not-homology) forces every "tonic inhibition / disinhibition" import to land as an algorithmic predicate, not a GABAergic mechanism; the load-bearing-vs-decorative test (§4.2) is the falsifier each component carries.

---

## 4. Entries in this pass

| Entry | Source | Components | Direction · confidence |
|---|---|---|---|
| `2026-06-20_arc_107_d1d2_gonogo_opponency_kravitz2010` | Kravitz et al. 2010, *Nature* | 1, 4 | supports · 0.72 |
| `2026-06-20_arc_107_focused_selection_surround_inhibition_mink1996` | Mink 1996, *Prog Neurobiol* | 1, 3 | supports · 0.70 |
| `2026-06-20_arc_107_pallidal_disinhibition_chevalier1990` | Chevalier & Deniau 1990, *TINS* | 3 | supports · 0.71 |
| `2026-06-20_arc_107_snr_permission_gate_hikosaka2000` | Hikosaka et al. 2000, *Physiol Rev* | 3 | supports · 0.74 |
| `2026-06-20_arc_107_gonogo_imbalance_disorders_maia2011` | Maia & Frank 2011, *Nat Neurosci* | 5 | supports · 0.70 |

Pre-existing entries reused for components 2 and 4: Frank 2006, Cavanagh 2011, Aron 2006, Bogacz 2007, Carandini 2012, Louie 2013, Reynolds 2009.
