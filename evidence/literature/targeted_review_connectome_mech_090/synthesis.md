# Synthesis: the BG commit-entry predicate — precision alone, or precision AND motor-program readiness?

**Plan-of-record:** [commitment_closure_plan.md](../../planning/commitment_closure_plan.md) GAP-4
**Precipitating empirical finding:** V3-EXQ-592 seed 42 — `running_variance` collapsed to 2.7e-5 while `nav_competence` stayed at 0.0. The agent satisfied the current rv-only commit-entry predicate by becoming trivially predictable (degenerate near-fixed-point policy), not by becoming competent. The current substrate licenses this; the question is whether the substrate is wrong.
**Predecessor work item:** IGW-20260528-013
**Author:** lit-pull session 2026-05-28
**Scope:** First-pass synthesis of 28 existing entries across four directories. Pass 2 (Cisek/Hanes/Roesch/Watanabe/Sakagami) added in this same session and cross-referenced below.

---

## 1. The question, made precise

The current REE-V3 BetaGate elevates into committed mode when:

    running_variance < commitment_threshold (default 0.40)

`running_variance` is an EMA over the E2 world-forward prediction-error trace (precision-of-prediction proxy). Nothing else gates entry.

V3-EXQ-592 seed 42 showed this is satisfiable in two architecturally distinct ways:

- **Honest path:** E2 learns the environment dynamics; predictions tighten; rv falls; commitment is earned.
- **Degenerate path:** the policy collapses to a near-fixed-point trajectory; the dynamics it samples are trivially self-consistent; rv falls to 2.7e-5; commitment is "earned" with `nav_competence = 0.0`.

The substrate cannot distinguish the two. The candidate substrate change is to require a *conjunction*:

    (running_variance < threshold) AND (motor-program readiness above floor)

with "readiness" candidates including `nav_competence`, an accumulator-to-threshold signal on a chosen affordance, a phasic dopaminergic burst on the leading candidate, or some other downstream marker that the commitment is *to something the agent can do*, not just *to a regime it can predict*.

This synthesis asks the existing 28-entry literature corpus: does the biology endorse precision-alone or a conjunction?

---

## 2. What the existing 28 entries say

The corpus splits roughly into three buckets, none of which is a clean adjudication.

### 2a. Precision-alone-compatible voices

The MECH-090 beta-oscillation core (Engel & Fries 2010; Kühn 2004 on STN beta desynchronisation; Pfurtscheller & Lopes Da Silva 1999) characterises beta as a status-quo / motor-release signal whose suppression times movement initiation. In that frame the gate is *one-dimensional*: when the precision-confidence signal crosses, beta drops, motor output proceeds. None of these papers asks "what if the model is confident about a useless plan."

The dissonance / belief-lock cluster (Izuma 2010; Voigt 2018; Colosio 2017; Gudjonsson 2016 on false confession internalisation) shows that the *act of committing alone* is sufficient to shift downstream value and belief representations — no separate readiness verification step is exhibited or implied. The strongest reading: commitment is performative; the lock follows from the commit.

These voices are compatible with a precision-only architecture but do not test the degenerate case V3-EXQ-592 exposed.

### 2b. Conjunction-leaning voices

Tandetnik 2021 is the pivot finding in the existing corpus: dysexecutive frontal-lesion patients failed to show choice-induced preference shifts despite remembering having made the choice. The commit *happened*; the downstream representational lock did *not*. This is direct evidence that the predicate "commitment caused this representational change" requires more than the precision/choice event — it requires intact executive machinery. It does not directly model `competence` as we mean it (motor-program readiness), but it establishes the principle that the commit gate is layered.

Tan 2016 reports that post-movement beta synchronisation (PMBS) tracks *internal model confidence*, not just movement parameters — beta's downstream effects depend on the agent's read of its own state. Hosaka 2016 finds that elevated beta protects the *internal motor-plan representation*, not only the output channel — i.e. beta gates something richer than a pure output valve.

Mayr & Keele 2000's backward-inhibition effect is graded (RT cost), implying that task-set release is modulated rather than binary, consistent with a graded readiness signal in addition to a precision threshold.

Dolan & Dayan 2013's habit/goal arbitration framework treats commitment as a *weighting* across multiple systems' signals; this is incompatible with a binary precision-only gate as the sole predicate.

These voices do not collectively *propose* the specific (precision + motor-readiness) conjunction we are weighing, but they do collectively undermine the sufficiency of precision alone.

### 2c. Out-of-scope / neutral

The play / personality / corticostriatal-window cluster (Miller 2024; McCrae 2000; Ham 2026; Bijlsma 2023; Pellis 2023; Zohar 2018) addresses the *calibration of commitment systems across development* rather than the per-event commit-entry predicate. It is informative for separate work on the personality-window question (INV-075) but does not bear directly on GAP-4.

The OFC / striatal task-bracketing cluster (Schuck 2016; Barnes 2011; Smith & Graybiel 2013; Rich 2009) describes *downstream* correlates of committed sequences — task-state encoding and sequence endpoint markers — rather than commit-*entry* predicates.

OpAL (Collins & Frank 2014) is the closest to the conjunction logic in this cluster: D1/D2 opposition implies that motor-readiness is itself a graded, dopamine-modulated signal rather than a binary release, but does not test conjunction with a precision channel.

---

## 3. The corpus's collective verdict

**No paper in the existing 28 explicitly proposes or tests:**

    BetaGate should condition on (rv_low AND nav_competence_high or
    motor-readiness-above-floor)

**The corpus does, however, supply two converging reasons not to trust the rv-only predicate:**

1. **Belief-lock requires executive machinery, not just choice (Tandetnik 2021).** The commit predicate is at least layered — a precision-driven entry can fire without the downstream consequences setting if executive readiness is absent. This argues for at least *staged* conditioning even if not strict conjunction at entry.

2. **Beta's gating function is richer than pure output release (Tan 2016, Hosaka 2016).** What beta gates (internal plan protection, model-confidence-modulated propagation) is itself state-dependent. A predicate that ignores that state will mis-fire.

The degenerate V3-EXQ-592 trajectory (rv → 0, competence → 0) is *exactly* the failure mode these conjunction-leaning voices would predict if you ask the literature "what happens when you gate purely on prediction-error?" — you commit to a regime that is self-consistent rather than capable.

But the literature corpus is not strong enough on its own to *prescribe* the specific conjunction the V3 substrate change would implement. The 28 entries triangulate the question; they do not answer it.

---

## 4. What is missing from the corpus

Five named bodies of work that would directly bear on the rv-only-vs-conjunction question are absent from the existing 28:

- **Cisek & Kalaska — affordance-competition framework.** Models action selection as parallel specification of multiple motor plans whose competition resolves over time. Commitment in this frame is fundamentally *about an affordance the system has prepared*; "commitment to a regime without a prepared affordance" is not coherent within the model.
- **Hanes & Schall — accumulator-to-threshold (FEF saccadic countermanding).** The canonical accumulator-to-threshold model: commitment is the threshold-crossing of a competence/preparation signal, not of an inverse-precision signal. The threshold is on readiness, not on PE.
- **Roesch — premature commit / impulsivity neural correlates.** Maps the failure mode "committed before the motor plan was specified" directly onto a measurable pathology.
- **Watanabe — prefrontal reward-expectancy.** Bears on whether the commit predicate should include an expected-value-of-the-plan term, which is downstream of competence.
- **Sakagami — prefrontal categorisation / commitment.** Bears on whether the commit gate should reference a categorisation of *what is being committed to*, not just *that prediction is tight*.

The first three are the most directly load-bearing. The Pass 2 entries added in this same session (see §5) bring them into the corpus.

---

## 5. Pass 2 additions (2026-05-28, same session)

Three Pass-2 entries added in the same lit-pull session:

| New entry | Authors / year | Bearing |
|---|---|---|
| `2026-05-28_mech090_affordance_competition_cisek2010` | Cisek & Kalaska 2010 (review) | STRONG_CONJUNCTION — commitment is selection-among-prepared-affordances; the rv-only gate is incoherent in this frame |
| `2026-05-28_mech090_accumulator_to_threshold_hanes_schall1996` | Hanes & Schall 1996 (Science, FEF countermanding) | STRONG_CONJUNCTION — gating is on a readiness accumulator crossing threshold, not on a precision signal |
| `2026-05-28_mech090_premature_commit_pathology_roesch2007` | Roesch, Calu & Schoenbaum 2007 (Nat Neurosci) | STRONG_CONJUNCTION — operationalises "committed before the program was ready" as a measurable pathology with a dopaminergic signature |

These three entries do not exhaust the gap (Watanabe and Sakagami remain unaddressed and are noted as residual gaps for a future pass), but they convert the V3-EXQ-592 finding from "the substrate is satisfiable in a way we don't like" to "the substrate is mis-architected against three load-bearing literatures."

---

## 6. Recommendation to GAP-4 governance

Three readings remain live; the literature now disposes them as follows.

| Reading | Pre-pass support | Post-pass support |
|---|---|---|
| **R-a: rv-only is correct; V3-EXQ-592 seed 42 is a curriculum problem (the agent should not have been allowed to reach degenerate fixed-points)** | weak | weakened further by Cisek/Hanes/Roesch — the issue is gate architecture, not training schedule |
| **R-b: rv-only is correct for *entry*; a separate downstream gate (executive / motor) controls *propagation*** | moderate (Tandetnik) | retained — Cisek/Hanes do not rule this out; in fact OpAL + Tandetnik + Roesch's dopaminergic readiness signal are consistent with a two-stage architecture |
| **R-c: commit entry should require a conjunction (rv_low AND readiness_above_floor) in a single gate** | weak | strengthened — Hanes/Schall's accumulator-to-threshold and Cisek's affordance-readiness are direct precedent for *readiness-as-the-primary-predicate*, with precision as one input rather than the sole input |

R-c is the strongest reading from the post-pass corpus. R-b is the conservative reading that minimises substrate change but accepts that the V3-EXQ-592 trajectory will recur until a downstream gate is added. R-a is not defensible against the post-pass corpus.

**Pass-on:** this synthesis does not stamp the governance question. It supplies the corpus reading; the GAP-4 substrate-design decision (which is implement-substrate territory, not lit-pull territory) consumes this synthesis and the V3-EXQ-592 manifest together. The relevant claim_ids are MECH-090 and SD-034; the substrate change, if landed, would also touch MECH-260 and MECH-266.
