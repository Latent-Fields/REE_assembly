Raw thought file: [docs/thoughts/2026-06-06_clinical_depression_network_connectivity_reversal.md](../../docs/thoughts/2026-06-06_clinical_depression_network_connectivity_reversal.md)
Intake date: 2026-06-09
Status: structured intake (Stage 2)
Classification: psychiatric failure-axis architecture compass -- NOT a REE-v3 implementation target
Registration: REGISTERED 2026-06-09 (per user decision to reap, overriding the intake default). Section 5 candidates A/B/C registered into claims.yaml at status:candidate: RA-001 (research_anchor/out_of_domain), MECH-367 (mechanism_hypothesis/substrate_conditional/v4), Q-061 (open_question/answer_state). Anchor doc docs/architecture/depressive_network_regimes.md. Candidate D stays cross-repo (ai-cognitive-failure-taxonomy), NOT in claims.yaml. No promotion/demotion of any existing claim.
Terminology guardrail: "long-term depression" here = long-term CLINICAL depressive illness, NOT synaptic long-term depression (LTD). This distinction is load-bearing -- see Section 9.

---

# THOUGHT INTAKE (Stage 2): Long-term clinical depression and reversible brain-network connectivity patterns

## 0. Source verification (resolves the raw note's "source-check pending" status)

The raw thought recorded the primary source as **unverified** (the `share.google` link was not
openable and exact-title / site-specific searches did not locate the article during capture).
This intake **locates and verifies the article** via web search:

- **Source (VERIFIED):** "Long-Term Depression Reverses Brain Network Connectivity" --
  Neuroscience News, https://neurosciencenews.com/brain-network-connectivity-mdd-30745/
- The Neuroscience News item is a press write-up of a major-depressive-disorder (MDD)
  resting-state functional-connectivity study.

**Findings as reported in the Neuroscience News coverage (verified at the press-summary level):**

- MDD undergoes a structural/functional evolution after a **~24-month chronicity threshold**,
  at which the functional-connectivity dynamics between the **Central Executive Network (CEN)**
  and the **Default Mode Network (DMN)** **reverse**.
- **Non-chronic (short-term) patients:** *stronger* CEN-DMN (precuneus) connectivity at low
  symptom severity, *weaker* at high severity.
- **Chronic (long-term) patients:** the **reverse** relationship -- connectivity *strengthens*
  as symptoms worsen, described as trapping patients in a state of negative cognitive
  **rumination**.
- Framed by the coverage as giving drug developers / psychiatrists a roadmap for therapies
  **tailored to illness duration** (duration-dependent, personalised treatment).

**Important precision about the word "reverses" (do NOT overclaim):**

- In this source, "reverses" denotes that the **sign of the connectivity-vs-severity relationship
  flips** between non-chronic and chronic cohorts past the chronicity threshold. It is a
  **cross-sectional, duration-dependent reversal of a coupling relationship**, observed in fMRI.
- It is **NOT** a demonstration of *therapeutic reversibility* (i.e. that intervention returns a
  chronic patient's network to the non-chronic regime). The raw thought's "possibly reversible"
  framing must be read as a *hypothesis the finding makes plausible*, not as something the source
  demonstrates. Keep this separation when any later architecture note cites this.

**Primary peer-reviewed paper -- TRACED + VERIFIED 2026-06-09** (resolves the intake's original
"not located" gap): Zanao T., Salvan P., Razza L. B., et al., "Chronicity moderates the impact of
severity on central executive-default mode network functional interactions in depression,"
*Scientific Reports* (2026), DOI **10.1038/s41598-026-40364-2**
(https://www.nature.com/articles/s41598-026-40364-2 ; preprint medRxiv 10.64898/2026.01.28.26345027).
- **Sample:** 46 patients (31 female, mean age 40.5); whole-brain network modelling + VBM.
- **Severity:** Hamilton Depression Rating Scale. **Chronicity:** current episode > 24 months.
- **Result:** chronicity *moderates* the severity->connectivity relationship. Non-chronic patients:
  CEN-precuneus(DMN) connectivity DECREASES with severity (stronger at low severity, weaker at high).
  Chronic patients: the reverse (connectivity INCREASES with severity).
- The 24-month threshold and precuneus locus are therefore **paper-verified**, not merely press-reported.
  (The Neuroscience News headline's "reverses" = this chronicity-moderated sign change between cohorts.)

---

## 1. Verbatim thought (preserved)

> A saved REE email pointed to a Neuroscience News item titled "Long-Term Depression Reverses Brain
> Network Connectivity". The direct `share.google` link was not accessible during intake, and
> exact-title plus site-specific searches did not locate the article. Therefore this note preserves
> the possible REE-relevant architectural idea as source-check pending, not as verified evidence.
>
> Important terminology correction: in this saved item, **long-term depression refers to clinical
> depressive illness**, not synaptic long-term depression.
>
> The useful REE idea is:
>
> > prolonged depressive states may correspond to altered, possibly reversible, large-scale network
> > connectivity regimes rather than only low mood, negative belief content, or reward deficit.
>
> For REE, this suggests that depressive failure modes should be modelled as field-level state
> changes involving connectivity, gain, salience, goal access, residue, fatigue, social access, and
> offline integration -- not merely as isolated negative thoughts or low reward values.
>
> [Full raw note, including the seven candidate axes, the REE-analogue mapping table, the AI
> cognitive-failure-taxonomy link, and the cautions/guardrails, is preserved in the raw thought
> file linked at the top of this intake. Reproduced in condensed form in Sections 3-5 below.]

The note's central computational primitive (verbatim):

```text
depressive_regime_risk = f(future_access, goal_coupling, residue_load,
                           rumination_loop_gain, action_threshold,
                           social_affordance, offline_repair_quality)
```

---

## 2. What's New vs Existing REE Docs (novelty table)

REE **already has a substantial clinical-depression cluster**. The grep below (verified against
`docs/claims/claims.yaml`, 2026-06-09) is the relevant prior art. The novelty of this thought is
**narrow and specific**: it is not "model depression as a state" (REE does that), it is the
**chronicity-dependent reversal of large-scale network coupling** plus the **multi-axis network-regime
vector** framing.

| Idea in this thought | Already in REE? | Where | Genuinely new? |
|---|---|---|---|
| Depression is a *state/attractor*, not a scalar low-mood/low-reward | **YES** | INV-034 (goal-maintenance failure = depressive attractor, EXQ-237a "computational definition of the depressive attractor state"); MECH-082/086 ("depression = locked-in avoidant brain insensitive to sensory evidence"); MECH-088 ("Depression = 5-HT distal attractor inaccessibility + DA selection failure") | NO -- core framing already owned |
| Rumination = self-amplifying recurrent loop with impaired decommitment | **YES** | MECH-124 (harm-trace replay -> consolidation -> option-space contraction; "treatment-resistant depression learned"); MECH-094 notes (rumination as repeated simulated-harm trajectories) | NO |
| Anhedonia / reduced motivation = reduced goal/reward affordance access | **YES** | Q-021 (pure harm-avoidance -> behavioral flatness/quiescence; "clinical face = depression"); INV-053 (anhedonia prediction); INV-034 (wanting vs liking, schizophrenia negative-symptom profile) | NO |
| Offline integration can *deepen* rather than *repair* a depressive regime | **YES** | MECH-124 (consolidation amplifies whatever dominates replay; self-amplifying loop); MECH-123 (REM recalibration) | NO |
| Depression as one profile in a *multi-failure-mode* psychiatric taxonomy | **YES** | MECH-088 (four-plane neuromodulatory failures); IMPL-005 (failure-mode taxonomy); MECH-126 (state-abstraction failure modes) | NO |
| **Chronicity-dependent REVERSAL of large-scale network coupling (CEN-DMN sign flip past a ~24-month threshold)** | **NO** | -- | **YES** -- REE has *no* claim that the *sign* of inter-system coupling flips as a function of illness *duration*; REE's depressive attractor is modelled as static-ish inaccessibility, not a duration-indexed bifurcation |
| **A unified network-regime VECTOR** (the 7 axes: future_access, goal_coupling, residue_load, rumination_loop_gain, action_threshold, social_affordance, offline_repair_quality) as the *carrier* of the depressive state | **PARTIAL** | The individual axes exist scattered across INV-034 (goal_coupling), MECH-124 (residue/rumination/offline), Q-021 (action threshold/anhedonia), MECH-082/086 (future access). **No single claim composes them into one weighted vulnerability vector.** | **PARTIAL-NEW** -- the *composition into one vector* is new; the pieces are not |
| Duration-dependent / personalised treatment roadmap (therapy tailored to chronicity) | **NO** (out of REE domain) | -- | Out-of-domain (clinical), not a REE substrate target |
| Depression-analogue **AI cognitive-failure mode** (low action-initiation despite goals; negative-eval loops; future-trajectory suppression; NOT "sadness") | **NO** in REE; lives in sibling repo | `Latent-Fields/ai-cognitive-failure-taxonomy` (external) | NEW for that taxonomy; off REE critical path |

**Net novelty verdict:** Two genuinely-new ideas (chronicity-dependent coupling *reversal*; the
unified network-regime *vector*) and one cross-repo taxonomy seed. Everything else is a re-statement
of the existing REE depression cluster. **None of it is V3-tractable** -- REE-v3 has no large-scale
"named network" coupling substrate (no explicit CEN/DMN analogues whose inter-coupling sign could be
measured), and no duration-indexed regime machinery. This is a **compass for the failure-axis
architecture**, not an implementation target.

---

## 3. Key formulations

1. **Depression as a network-regime, not a scalar.** The depressive state is a *pattern of coupling
   and access* across self/goal/salience/action/memory fields that becomes self-maintaining --
   consistent with REE's existing attractor framing (INV-034) but adding the explicit claim that the
   regime is carried by *inter-field coupling structure*, not by a single low scalar.

2. **Chronicity as a regime-bifurcation parameter (NEW).** Past a duration threshold (~24 months in
   the source), the relationship between symptom severity and large-scale coupling *reverses sign*.
   The REE-relevant abstraction: **illness duration is itself a state variable that can flip the
   sign of a control coupling** -- a depressive regime is not one attractor but (at least) two,
   selected by how long the system has been in the basin. REE currently has no duration-indexed
   coupling-sign-flip primitive.

3. **The seven-axis depressive-regime vector (PARTIAL-NEW as a composition).**
   `depressive_regime_risk = f(future_access, goal_coupling, residue_load, rumination_loop_gain,
   action_threshold, social_affordance, offline_repair_quality)`. Each axis maps to existing REE
   machinery (see Section 4); the new content is treating them as **one weighted vulnerability
   vector** whose *joint configuration* defines the regime, rather than as independent symptoms.

4. **Reversibility is a hypothesis, not a finding.** The maladaptive regime *may* be reconfigurable
   ("network-regime repair"), but the source demonstrates only a cross-sectional reversal of a
   coupling relationship, not therapeutic reversibility. REE should hold reversibility as an open
   question, not an asserted property.

---

## 4. Affected existing claims (REAL ids, verified against claims.yaml 2026-06-09)

This thought **corroborates and extends** the existing depression cluster; it does **not contradict**
any current claim. No claim status should change on the basis of this intake.

| Claim | Title (abbrev.) | Relation to this thought |
|---|---|---|
| **MECH-088** | Psychiatric conditions as four-plane neuromodulatory control failures | Owns the depression *profile* ("Depression = 5-HT distal attractor inaccessibility + DA selection failure") AND the **psychosis/depression distinction** ("Psychosis = NA collapse of E1/E2 constraint + DA aberrant salience"). The network-regime framing is a **complementary level of description** (large-scale coupling) to MECH-088's neuromodulatory-plane level. Candidate cross-ref, not a change. |
| **INV-034** | Goal maintenance necessary for ethical agency; depressive attractor | Owns "depressive attractor state = goal-maintenance failure" (EXQ-237a). The seven-axis vector's `goal_coupling` + `future_access` axes are this claim. Corroborated. |
| **MECH-124** | Harm-trace replay -> consolidation -> option-space contraction | Owns the `residue_load` + `rumination_loop_gain` + `offline_repair_quality` axes (offline integration *deepening* the regime). Directly corroborated by the source's "trapped in negative cognitive rumination." |
| **Q-021** | Harm-avoidance-only -> behavioral flatness | Owns the `action_threshold` / anhedonia axis ("clinical face = depression"). Corroborated. |
| **MECH-082 / MECH-086** | Hippocampal map distortion; DA trajectory-selection gain ("depression = locked-in avoidant brain") | Owns `future_access` (distal-trajectory inaccessibility). Corroborated; the coupling-reversal idea is a new wrinkle these don't yet capture. |
| **MECH-065** | Reality-coherence conflict lane; clinical analogue over_suppression -> anhedonia | Adjacent; `action_threshold` axis. |
| **MECH-094** | Simulation/real distinction; confabulation; rumination distinct from psychosis | **Distinction anchor** -- preserves the precise separation this intake must not blur (rumination/depression vs confabulation vs psychosis/hallucination). |
| **IMPL-005** | Failure-mode taxonomy | Parent taxonomy node; already sources the prior depression thought `2026-02-12_DEPRESSIVE-PATH-PRUNING-HIPPOCAMPAL-ROLLBACK.md`. A network-regime axis would extend this taxonomy, not replace it. |
| **MECH-126** | State-abstraction failure modes (overmerge/oversplit/...) | Adjacent failure-mode registry; network-regime depression is a different axis. |

**Prior depression thought already in the tree:** `docs/thoughts/2026-02-12_DEPRESSIVE-PATH-PRUNING-HIPPOCAMPAL-ROLLBACK.md` (sourced by IMPL-005). That note framed depression via *path pruning / hippocampal rollback*; this note adds the *large-scale coupling reversal* + *unified vector* angle. The two are complementary depression compasses, neither subsumes the other.

---

## 5. Candidate claims -- REGISTERED 2026-06-09 (A/B/C); D stays cross-repo

Per the user's decision to reap (overriding the intake default), candidates A, B, and C were
registered into `claims.yaml` at `status: candidate`, with `epistemic_category` chosen so none can
promote without the substrate/evidence it lacks. Anchor doc:
[docs/architecture/depressive_network_regimes.md](../../docs/architecture/depressive_network_regimes.md).
**No existing claim was promoted or demoted.**

1. **CANDIDATE-A -> RA-001** (REGISTERED). `claim_type: research_anchor`,
   `epistemic_category: out_of_domain`. *"Long-term clinical depression involves a
   chronicity-dependent reversal of large-scale network coupling (CEN-DMN sign flip past a ~24-month
   threshold); the depressive brain-state is duration-indexed, not unitary."* First of the new `RA-`
   (research-anchor) prefix -- `research_anchor` is the claim_type `v4_spec.md` names for
   out-of-domain anchors. Primary paper TRACED + verified (Zanao et al., *Scientific Reports* 2026,
   DOI 10.1038/s41598-026-40364-2); recorded in the claim notes + source.

2. **CANDIDATE-B -> MECH-367** (REGISTERED). `claim_type: mechanism_hypothesis`,
   `epistemic_category: substrate_conditional`, `implementation_phase: v4`. *"The depressive failure
   mode is carried by a multi-axis network-regime vector (future_trajectory_access,
   goal_stream_coupling, residue_load, rumination_loop_gain, action_threshold, social_affordance,
   offline_repair_quality), not a scalar mood/reward value; the regime is the joint configuration."*
   The genuinely-new REE-architectural composition; `depends_on` INV-034 / MECH-124 / Q-021 /
   MECH-088 / MECH-082 / RA-001. Registered as a NEW MECH (not an INV-034 amendment) per the user's
   selection. V4/V5, off the V3 / GAP-7 critical path; do not build in V3.

3. **CANDIDATE-C -> Q-061** (REGISTERED). `claim_type: open_question`,
   `epistemic_category: answer_state`. *"Is a maladaptive depressive network-regime (MECH-367)
   reversible by REE's repair machinery, or does chronicity lock the regime past a threshold
   (RA-001)?"* `depends_on` MECH-367 / MECH-124 / INV-034 / RA-001. Resolvable in REE only once the
   MECH-367 vector substrate exists; do not queue a V3 experiment against it.

4. **CANDIDATE-D -- NOT registered in claims.yaml (cross-repo).** The depression-analogue AI
   cognitive-failure mode (persistent low action-initiation despite available goals;
   negative-evaluation loops; future-trajectory suppression; excessive failure-generalisation)
   belongs in `Latent-Fields/ai-cognitive-failure-taxonomy`, handled with explicit
   anti-anthropomorphic guardrails (the analogue is *network-state failure in trajectory generation
   and action readiness*, NOT mood/sadness). The REE `EXT-` series (LLM external failure modes) is
   the in-registry sibling pattern, should that taxonomy ever fold back. Per the user's selection,
   D stays out of `claims.yaml`.

**Source status:** RA-001's primary peer-reviewed paper was TRACED + verified 2026-06-09 (Zanao et
al., *Scientific Reports* 2026, DOI 10.1038/s41598-026-40364-2; see Section 0) -- the 24-month
threshold and precuneus locus are now paper-verified. The original "source-check pending" gap is
closed.

---

## 6. Psychosis / depression failure-mode distinction (precision guardrail)

This intake must keep three distinct REE failure modes separate (the request is explicit, and the
existing cluster already encodes the distinction):

- **Depression** = goal-maintenance failure / distal-attractor inaccessibility / DA selection
  failure / self-maintaining rumination regime (INV-034, MECH-088 depression profile, MECH-124,
  Q-021). This thought is about **this** mode.
- **Psychosis** = NA collapse of E1/E2 constraint + DA aberrant salience on noisy input (MECH-088
  psychosis profile); tag-MISassignment (MECH-094/MECH-115). A *prior-dominated precision failure*.
- **Confabulation** = tag-LOSS / simulation-real source-monitoring failure (MECH-094) -- simulated
  events encoded as real. Distinct from both above.

The network-regime / coupling-reversal idea is a **depression-specific** compass. It must **not** be
generalised into psychosis or confabulation, and "rumination" here is the depressive recurrent-loop
sense (MECH-124), not psychotic content-intrusion. (Per memory `feedback_psychosis_confabulation_distinction`.)

---

## 7. Important cautions (carried from raw note)

- Do **not** cite this as experimental evidence -- it is a press-summarised clinical finding plus an
  architectural prompt. The peer-reviewed paper behind it was not located at intake.
- Do **not** confuse this item with synaptic long-term depression (LTD).
- Do **not** reduce clinical depression to connectivity alone, nor imply it is "merely a reversible
  software state."
- Do **not** over-map human depressive illness onto artificial systems (anti-anthropomorphic guard).
- Do **not** make this a REE-v3 implementation target -- there is no V3 substrate for named
  large-scale network coupling, and the claim is `out_of_domain` for V3 experiments.

---

## 8. Next steps (none on the V3 critical path)

1. **(Optional, low priority)** Trace the primary peer-reviewed publication behind the Neuroscience
   News press item to obtain paper-verified quantitative anchors (authors, journal, DOI, the
   24-month threshold statistics, precuneus locus). Only needed if CANDIDATE-A/B are ever pursued.
2. **(Deferred)** If/when the failure-axis architecture is formalised, fold the two genuinely-new
   ideas (duration-indexed coupling reversal; unified network-regime vector) in as amendments to
   MECH-088 / INV-034 rather than as standalone INVs -- and as `out_of_domain` /
   `substrate_conditional`, never V3-promotable.
3. **(Cross-repo)** Seed CANDIDATE-D into `Latent-Fields/ai-cognitive-failure-taxonomy` if/when that
   taxonomy is next worked, with anti-anthropomorphic guardrails.
4. **No experiment, no substrate, no claims.yaml edit** flows from this intake.

If the source is ever fully verified and a specific REE gap is identified, the candidate architecture
note is `docs/architecture/depressive_network_regimes_and_repair.md` (as the raw note proposed) --
but only with user go-ahead.

---

## 9. Guardrail for future agents

If a future agent tries to convert this into **synaptic long-term depression (LTD)**, stop and
reframe: this is **long-term clinical depressive illness**.

The correct near-term extraction is:

> preserve long-term clinical depression as a candidate example of a *duration-dependent*,
> possibly-reversible *large-scale network-coupling regime* -- carried by a multi-axis vulnerability
> vector, not a scalar mood/reward value.

The incorrect extractions are:

> treat this as synaptic LTD; OR reduce clinical depression to simple low reward / sadness / negative
> belief content; OR assert therapeutic reversibility (the source shows a coupling-sign reversal
> across cohorts, not demonstrated reversal-by-treatment); OR generalise the depressive regime into
> psychosis or confabulation.
