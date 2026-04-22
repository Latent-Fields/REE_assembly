# SYNTHESIS -- Waking-Phase Online V_s Invalidation Literature Pull

> Created: 2026-04-22
> Origin: V3-EXQ-475 result (SD-036 GABA decay + MECH-279 PAG freeze gate fire correctly,
> but freeze re-commits dominate; agent has no online anchor invalidation signal driving the
> hippocampal proposer to remap away from the original avoid-anchor)
> Spec: REE_assembly/docs/session_prompts/waking_v_s_invalidation_litpull.md
> Papers: 12 in this directory + cross-references to targeted_review_connectome_mech_269/
> (Pfeiffer&Foster, Dragoi&Tonegawa, Foster, Olafsdottir, Tang, English) and to
> targeted_review_homeostatic_override/ (Sara&Bouret resonance via orexin)

## Per-paper question mapping

The five architectural questions from the spec:

- Q1: Local vs broadcast invalidation
- Q2: Single failure vs accumulation
- Q3: Proportional vs threshold
- Q4: Coupling to MECH-285 sleep replay priority
- Q5: Failure modes

| Paper | Q1 | Q2 | Q3 | Q4 | Q5 |
|------|----|----|----|----|----|
| Schultz, Dayan & Montague 1997 | broadcast (DA dip) | single | proportional (TD-PE) | -- | depression-blunted |
| Matsumoto & Hikosaka 2007 | broadcast (LHb -> DA) | single | proportional | -- | depression / learned helplessness |
| Bromberg-Martin & Hikosaka 2011 | broadcast (LHb info-PE) | single | proportional | -- | OCD vs depression dissociation |
| Wilson, Takahashi, Schoenbaum & Niv 2014 | local (OFC label) | accumulation (label drift) | threshold (label change) | -- | reversal-learning deficits |
| Stalnaker, Cooch & Schoenbaum 2015 | constraint on Wilson | -- | -- | -- | over-attribution warning |
| Gardner, Schoenbaum & Gershman 2018 | broadcast (DA generalized PE) | single | proportional | -- | mixed DA-disorder phenotypes |
| Yassa & Stark 2011 | local input (DG/CA3) | accumulation (interference) | proportional | -- | aging-related discrimination loss |
| Reagh et al 2018 | local input (alEC -> DG/CA3) | accumulation | -- | -- | aging-specific input failure |
| Gershman, Blei & Niv 2010 | both (Bayesian posterior) | accumulation (evidence integration) | both (graded posterior, threshold readout) | implicit | restricted latent-cause inference |
| Gershman, Monfils, Norman & Niv 2017 | both | accumulation | both | EXPLICIT (waking->sleep bridge) | over/under-segmentation |
| Bouton 2004 | -- (behavioural) | accumulation (extinction trials) | -- | -- | renewal predictions |
| Sara & Bouret 2012 | broadcast (LC reset) | single + sustained | both | offline consolidation hint | LC-dysfunction perseveration |
| Aston-Jones & Cohen 2005 | broadcast (LC) + cortical (ACC/OFC) | both (phasic + tonic) | both | -- | phasic-tonic imbalance |

Q4 is the question the literature speaks to least. Only Gershman2017 directly bridges waking
invalidation to sleep priority; the LC/NE literature mentions offline consolidation in passing
but does not establish the coupling quantitatively. This is the biggest underdetermined
question and a candidate for a follow-up pull.

## Verdict on candidate biological substrates

### Broadcast invalidation *trigger*

Four candidates with different shapes:

1. **Locus coeruleus phasic burst** (Sara&Bouret; Aston-Jones&Cohen). Strongest match
   computationally: surprise-shaped, not value-shaped; broadcast widely; under cortical
   control via ACC/OFC; comes with a built-in accumulator (tonic LC) that integrates
   phasic events into a sustained state. The phasic-tonic dual-mode structure is the
   cleanest existing biological substrate for a trigger-plus-accumulator architecture.

2. **Lateral habenula negative-RPE / information-PE** (Matsumoto; Bromberg-Martin).
   Strongest match for the value-violation component. Direct primate substrate evidence.
   Information-PE subpopulation in Bromberg-Martin is the closest biological signal to a
   model-fit-PE.

3. **Dopamine generalized PE** (Schultz; Gardner-Schoenbaum-Gershman). Carries both reward
   and sensory PEs after the 2018 reformulation; broadcast diffusely; well-characterised.
   The natural broadcast signal but somewhat redundant with LHb (which is upstream) and
   with LC (which carries surprise more cleanly).

4. **OFC representational change** (Wilson). Local rather than broadcast; fits the
   accumulator role rather than the trigger role.

**Verdict: LC phasic burst is the best candidate for the broadcast trigger** for V_s
specifically, because (a) the signal is surprise-shaped (closer to schema-fit-PE than
to reward-PE), (b) the same circuit provides a natural accumulator via tonic mode, and
(c) the cortical-control architecture (ACC/OFC -> LC) gives a principled mechanism for
schema-specific credit assignment. The DA / LHb pathway is best read as the value-violation
component that runs in parallel with the LC surprise pathway, both feeding the same local
accumulator. A two-trigger architecture is more parsimonious than trying to force everything
through one substrate, and is consistent with the observation that DA and LC dysfunctions
produce dissociable cognitive failure modes.

### Local *accumulator*

Three candidates:

1. **OFC representational drift** (Wilson; Stalnaker constraint). The cognitive-map-of-task-space
   framing is essentially V_s under another name. OFC labelling integrates evidence over
   trials and reorganises when the underlying state is judged to have changed. The local
   accumulator role is the function this paper most clearly defends -- and the function
   Stalnaker2015 explicitly endorses while critiquing other OFC attributions.

2. **Hippocampal DG remap rate / alEC-DG/CA3 imbalance** (Yassa & Stark; Reagh).
   Substrate for the *input* to the accumulator -- representational interference detection.
   Does not directly compute V_s but feeds the operation that does. Most likely role is
   as an upstream signal feeding either OFC's labelling step or LC's tonic-mode shift,
   rather than as the accumulator itself.

3. **vmPFC latent-cause posterior** (Gershman computational frame; not directly substrated
   in this pull). The computational requirement is for a circuit that maintains a posterior
   over latent causes and updates it with each observation. vmPFC is a plausible candidate
   based on extinction literature but the substrate evidence is weaker than for OFC.

**Verdict: OFC representational drift is the best candidate for the local accumulator**,
with hippocampal DG/alEC providing the upstream interference-detection signal and LC tonic
mode providing the broadcast-amplification mechanism. The most parsimonious architecture
binds OFC + LC + DG/alEC into a single circuit: alEC/DG detect interference; OFC integrates
into a per-anchor schema-validity label; LC tonic level reflects the integrated state and
gates behavioural disengagement; phasic LC + DA dip provide the broadcast trigger events
that drive integration; ACC/OFC -> LC projections do schema-specific credit assignment.

## Verdict on registering a new MECH for the online invalidation event

**Recommendation: register a new MECH for the online invalidation trigger event.**

Draft proposed claim text:

> **MECH-NNN** (waking phase online schema invalidation trigger): The brain registers
> single-event schema-fit violations via a broadcast invalidation signal carried jointly
> by phasic LC-norepinephrine bursts (surprise-shaped) and midbrain dopamine generalized
> prediction errors (value- and identity-shaped). The broadcast event is the trigger that
> MECH-284 integrates over time into a per-schema staleness signal. The trigger event is
> distinct from the accumulator both functionally (broadcast vs local) and substrate-wise
> (LC/DA vs OFC representational drift). Cortical inputs from ACC/OFC to LC implement
> schema-specific credit assignment converting undifferentiated broadcast bursts into
> targeted accumulator integration.
>
> Status: candidate, v3_pending. Depends on MECH-284 (V_s residual schema staleness
> accumulator) and MECH-269 (anchor selection by regional verisimilitude). Implementation
> phase: v3 -- needs explicit trigger event in the substrate distinct from the accumulator.

Rationale for registering separately rather than expanding MECH-284:

1. Failure modes dissociate. LHb hyperactivity (over-trigger), LC hypoactivity (under-trigger),
   OFC lesion (accumulator broken), alEC hypoactivity (input pathway broken) are biologically
   distinct failures. The architecture should reflect that.
2. The substrate-readiness story is different. A trigger-event MECH can be implemented in
   ree-v3 as a per-step signal in the agent loop (similar to how prediction-error signals
   are already wired). The accumulator MECH-284 needs a longer-timescale state machine.
3. The clinical mapping is sharper. OCD, depression, ASD, and aging produce distinguishable
   profiles depending on which component fails. A single MECH would obscure this.

Alternative: if registration parsimony matters more than dissociation, MECH-284 can be
expanded to include the trigger event implicitly (the accumulator integrates "events"
without specifying their substrate). Architecturally weaker but defensible.

## Underdetermined questions warranting follow-up

1. **Schema-specificity of LC bursts.** Are LC phasic bursts targeted to specific cortical
   regions / schemas, or does the broadcast hit everything and credit assignment happen at
   the receivers? The Aston-Jones-Cohen framework leans toward local credit assignment but
   recent LC anatomy (modular projections) suggests some targeting. A V3 experiment could
   discriminate. Lit-pull candidate: Chandler 2014 / Schwarz 2015 modular LC projections;
   Uematsu 2017 LC-amygdala specificity.

2. **Information-PE in non-reward contexts.** Does LHb information-PE fire to anchor-mismatch
   in a navigation task with no reward outcome? Bromberg-Martin's evidence is reward-tied;
   the V_s mapping requires the extension. Lit-pull candidate: Hu et al on LHb in non-reward
   tasks; Lecca 2020 LHb in defensive responding.

3. **Coupling to sleep replay (Q4).** The Gershman 2017 framework predicts a quantitative
   coupling between waking invalidation load and sleep replay priority. The empirical
   literature on this coupling is thin in this pull. A targeted pull on sleep-replay-priority-as-
   function-of-daytime-mismatch would close MECH-285. Lit-pull candidates: Mednick 2011 sleep
   and learning consolidation; Karlsson 2009 wake-sleep replay correlations; Lewis-Jamieson
   2018 schema-relevance and sleep consolidation.

4. **DG remap-rate read-out.** Is DG remap rate read out by other circuits as a validity
   signal, or only as an internal separation operation? The Yassa-Stark / Reagh evidence
   is consistent with the read-out claim but does not establish it. A V3 experiment could
   probe this.

5. **OFC graded vs threshold dynamics.** Wilson2014 specifies labelling but not the dynamics
   of label change. Whether OFC representations drift continuously or reorganise discretely
   determines whether MECH-269 should be a graded or threshold operation. Single-cell
   continuous recording during reversal would help.

## V3-EXQ-475 connection

The freeze re-commit phenotype maps to a substrate failure that is *not* in the broadcast
trigger circuits. In V3-EXQ-475, single freeze releases occur (5-6 per seed) -- so something
analogous to the trigger event *is* firing. But the agent re-commits ~12 times per release
and stays in freeze for 1000/1000 eval steps -- so the accumulator is not crossing threshold
to drive sustained anchor reset. The substrate failure is in the local accumulator step:
trigger events register but never accumulate to anchor invalidation.

This points specifically to the OFC-analog substrate being absent in current ree-v3. The
hippocampal proposer keeps drawing trajectories from the original avoid-anchor because
nothing is integrating the cumulative evidence that the avoid-anchor is no longer the right
schema for this region. Adding MECH-284 as an explicit accumulator wired to (a) LC-analog
phasic events, (b) OFC-analog schema labels, and (c) hippocampal-anchor V_s read-out should
fix the phenotype. A trigger-event MECH (per the recommendation above) is needed first
because the existing prediction-error signals in ree-v3 are not currently formatted as
schema-fit-PEs that the accumulator can integrate.

The dual-trace property from Bouton 2004 also matters: MECH-269 reset should not erase the
avoid-anchor; it should mark it as no longer operative while preserving its retrievability.
This means MECH-272 (state-gated routing) is part of the architectural fix, not just MECH-269.
The avoid-anchor and a new safety-anchor must coexist, with routing deciding which is
operative -- which is the dual-trace requirement, the latent-cause-mixture requirement, and
the LC-tonic-mode-gates-routing requirement all converging on the same architectural step.

## Cross-references to existing lit-pulls

- `targeted_review_connectome_mech_269/` already pulled Pfeiffer & Foster 2013 (replay starts
  at current location), Dragoi & Tonegawa 2011/2013 (preplay), Foster 2017, Olafsdottir 2018,
  Tang 2017 (awake vs sleep SWR), English 2014 (E/I balance gating). These cover replay
  *content* but not waking-phase invalidation triggers; they are complementary to this pull
  rather than overlapping. Cite for the offline consolidation side of MECH-269.
- `targeted_review_connectome_mech_270/` (Anastassiou 2011, Buzsaki 2015) and
  `targeted_review_connectome_mech_271/` (Girardeau 2017, Jadhav 2016) cover ephaptic
  substrate and replay routing. Tangentially relevant; the waking-invalidation trigger
  could plausibly be ephaptically encoded under MECH-270 but this is not addressed in
  any paper in the current pull.
- `targeted_review_homeostatic_override/` (Sara&Bouret resonance through orexin literature)
  -- the LC/orexin coupling is a likely modulation pathway for the trigger sensitivity.
  Worth cross-referencing in any future pull on neuromodulator interactions.
- `neuro_pe_habenula_da/` -- placeholder synthetic entry; not a real reference.

## Summary

12 papers across 7 systems converge on a clean two-circuit architecture for waking V_s
invalidation: (1) LC (phasic+tonic) and DA (generalized PE, partly via LHb) as the broadcast
trigger / amplification pair; (2) OFC representational drift, fed by alEC/DG interference
detection, as the local accumulator. The Gershman latent-cause framework provides the
computational form. The dual-trace property from Bouton requires that MECH-269 reset not
erase predecessor anchors. The LC tonic-mode mechanism gives MECH-272 its biological
underpinning. The trigger event should be registered as a new MECH distinct from MECH-284
the accumulator. The biggest underdetermined question is the quantitative coupling between
waking invalidation load and MECH-285 sleep-replay priority -- only Gershman 2017 speaks to
this directly and the empirical literature is thin.

The V3-EXQ-475 phenotype is best explained by *accumulator* failure, not trigger failure:
the freeze releases indicate trigger events are firing, but the lack of sustained release
indicates accumulator integration is not crossing threshold. The architectural fix is the
OFC-analog accumulator wired to existing prediction-error signals (reformatted as schema-fit
PEs) plus a routing layer (MECH-272) that maintains both the avoid-anchor and a new
safety-anchor concurrently.
