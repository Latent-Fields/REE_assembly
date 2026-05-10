# SYNTHESIS -- ARC-071 policy.composition_via_repeated_grounding (chunk formation / habit composition)

**Pull commissioned:** 2026-05-10 from the policy_primitive_granularity architectural family registration session.
**Companion pull (deferred):** ARC-070 decomposition-on-prediction-failure.
**Date:** 2026-05-10. **Entries:** 9 papers (Graybiel 1998 + 2008, Yin & Knowlton 2006, Smith & Graybiel 2013, Wymbs 2012, Sakai 2003, Botvinick / Niv / Barto 2009, Sutton / Precup / Singh 1999, Albouy 2013).
**Source attribution:** the per-paper records cite PubMed entries with DOIs and PMIDs as listed; this synthesis aggregates and adjudicates rather than re-citing each paper exhaustively.

---

## Why this pull was commissioned

ARC-071 was registered 2026-05-10 alongside ARC-069 (parent dynamic-regranularisation commitment) and ARC-070 (decomposition-on-prediction-failure). The architectural commitment: sequences of policy primitives that have been repeatedly executed together with consistent outcomes are accumulated into a single primitive that the rule-apprehension layer (ARC-062) and the diversity-generation layer (ARC-065) can treat atomically.

The slot was registered with a specific load-bearing observation: ARC-071 explicitly NAMES THE TRANSITION MECHANISM that MECH-163 dual_goal_directed_systems presupposes but does not specify. MECH-163 names the PRESENCE of two systems (planned + habitual); ARC-071 is the machinery that pumps content from planned-into-habitual. Without ARC-071 the dual systems in MECH-163 are static configurations; with ARC-071 the division of labour shifts continuously with experience.

Six falsifiable verdicts were pre-specified in the briefing. R3 (transition mechanism for MECH-163) and R6 (real-vs-imagined gating in the chunking write path) were flagged as the most architecturally consequential -- R3 because if confirmed it triggers a governance update to MECH-163's depends_on; R6 because if biology fails to gate, REE has a new and serious safety gap to register, not just a parameter to set. The synthesis settles each at a stated confidence; both load-bearing verdicts come back with substantive findings the slot pre-registration did not anticipate.

---

## R1 -- Trigger primary: repetition+consistency, reward-rate, V_s-positive, or FEP?

### Verdict: REPETITION + OUTCOME CONSISTENCY is the primary trigger (the canonical Graybiel pattern). Reward-rate and V_s-positive are secondary modulators / gates. Free-energy-minimisation is not directly supported in the chunking literature. Confidence 0.78.

The evidence cluster:

- **Graybiel 1998 (PMID 9753592)** -- foundational. S-R learning recodes within striatum to chunk action sequences. The trigger is repetition; the recoding is gradual; the canonical pattern is repetition + consistent outcome over many trials.
- **Graybiel 2008 (PMID 18558860)** -- decade-on review. Chunking is downstream of evaluative-circuit gating: circuits mediating evaluation gradually lead to selection of particular behaviors that, through chunking, become habits. This adds the EVALUATIVE-GATE upstream of pure repetition -- chunks form preferentially over evaluated-as-good sequences.
- **Sakai et al. 2003 (PMID 12879170)** -- behavioural human evidence. Subjects spontaneously chunk during sequence learning without instruction; chunks become clearer and more consistent as learning progresses.

The repetition + outcome consistency framing is converged across rodent (Graybiel), primate (Hikosaka lab), and human (Sakai, Wymbs) data. The reward-rate-conditioned chunking the briefing pre-registered (Sakai 2003 frame) is supported but as a SECONDARY MODULATOR -- the evaluative-gate from Graybiel 2008 sits between the trigger and the write, gating chunking toward evaluated-as-good sequences. The V_s-positive trigger (the symmetric inverse of ARC-070's V_s-negative trigger) is biologically plausible (high V_s = stable predictions = good chunking candidate) but is not directly tested in the available chunking literature; it is REE's own framing extension and should be treated as a child-MECH design hypothesis to validate, not as a direct biological mapping. The free-energy-minimisation framing (Friston) is theoretically compatible but not directly tested in the chunking literature; it could be reformulated post-hoc but is not a primary trigger candidate the biology nominates.

Recommendation for child-MECH design: implement repetition + outcome-consistency as the primary trigger, with an evaluative-gate upstream (REE analog: SD-014 valence integration) and V_s-positive as a secondary precondition (chunk preferentially over high-V_s regions). Reward-rate and FEP are not implementation primitives but can be derived from these.

---

## R2 -- Substrate locus: DLS only, or phase-dependent multi-substrate?

### Verdict: PHASE-DEPENDENT MULTI-SUBSTRATE. ARC-071 substrate is striatum (DLS-analog) for the chunk-association formation, with infralimbic cortex (vmPFC-analog in REE) required for chunk maintenance, and frontoparietal cortex involvement during early-phase parsing. NOT a single substrate. Confidence 0.81.

The evidence cluster:

- **Yin & Knowlton 2006 (PMID 16715055)** -- DLS as the habit substrate, DMS as the goal-directed substrate. The substrate-distinct dual-systems framing.
- **Smith & Graybiel 2013 (PMID 23810540)** -- causal manipulation evidence. Selective optogenetic disruption of infralimbic cortex (IL) during overtraining PREVENTS habit formation. Substrate is NOT just striatum -- a cortical (IL-analog) component is required.
- **Wymbs et al. 2012 (PMID 22681696)** -- human fMRI. Putamen supports concatenation (chunking IN, ARC-071 direction); frontoparietal cortex supports segmentation (chunking OUT, ARC-070 direction). Substrate-distinct attribution at human-imaging level.

The R2 verdict has a sharp implication for the slot's pre-registration. The slot's notes mention "dorsolateral striatum (Yin & Knowlton 2006 DLS) is the prime substrate" -- this is correct but incomplete. The full picture, integrating Smith & Graybiel 2013 + Wymbs 2012:

- **Putamen / DLS-analog**: motor-motor association formation (the chunking IN process). REE substrate analog: striatal-equivalent in habit_substrate (MECH-163 habit system substrate). This is the load-bearing substrate for chunk-formation.
- **Infralimbic cortex / vmPFC-analog**: chunk MAINTENANCE -- the late-overtraining acquired pattern that gates whether chunks crystallise. REE substrate analog: vmPFC.md INV-037 / INV-038 (stored / active distinction; EVR pattern). Without the vmPFC-analog component, chunks will not crystallise even if the striatal-analog accumulator fires.
- **Frontoparietal cortex**: early-phase parsing / segmentation. This is more relevant to ARC-070 than ARC-071 but the two share substrate during the early-learning phase.

The recommendation for child-MECH design: ARC-071 substrate is at minimum a TWO-COMPONENT machinery (striatal-analog + vmPFC-analog), not a single accumulator. The slot's pre-registration underspecifies; the synthesis recommends explicit substrate registration covering both components in the ARC-071 family doc and an architecture note cross-linking to vmPFC.md / INV-037 / INV-038 / MECH-163 habit system substrate.

---

## R3 -- LOAD-BEARING: does ARC-071 IS the missing transition mechanism in MECH-163?

### Verdict: CONFIRMED. ARC-071 IS the missing transition mechanism in MECH-163 dual_goal_directed_systems. Recommend MECH-163 governance update to add ARC-071 to its depends_on. Confidence 0.85.

This is the load-bearing verdict the briefing flagged for extra synthesis effort. The verdict comes back CONFIRMED at the causal level, with two independent strands of evidence:

**Strand 1: substrate-level support from Yin & Knowlton 2006.** The DMS-to-DLS transfer over training is the system-level signature of the planned->habitual transition that MECH-163 names. The transfer happens gradually, through repetition. The DMS and DLS coexist during transition (parallel, interdependent), which directly supports ARC-071's design choice that the original primitive sequence remains available alongside the chunked unit (chunks are additive, not replacing). The system-level evidence anchors the framing.

**Strand 2: chunk-level causal evidence from Smith & Graybiel 2013.** Selective optogenetic disruption of infralimbic cortex during overtraining PREVENTS habit formation. This is causal manipulation, not just correlational evidence -- removing one component of the chunking machinery breaks the planned->habitual transition. ARC-071's chunk-level mechanism is therefore not just present but CAUSALLY NECESSARY for the transition MECH-163 describes.

The two strands together close the inferential gap. The system-level evidence (Yin & Knowlton 2006) supplies the framework within which the chunk-level mechanism (Smith & Graybiel 2013) becomes architecturally meaningful. ARC-071 is the chunk-level machinery by which content moves from planned (DMS-analog) to habitual (DLS-analog); without ARC-071, the dual systems in MECH-163 are static configurations; with ARC-071, the division of labour shifts continuously with experience -- which is exactly the rodent-overtraining picture.

**Governance recommendation:** MECH-163's claims.yaml entry should be updated post-pull to add ARC-071 to its depends_on list. The entry currently does not list ARC-071 (because ARC-071 was registered after MECH-163). The depends_on update is a one-line edit but it is architecturally consequential -- it formally records that MECH-163's dual-systems framing is incomplete without ARC-071 supplying the transition machinery. The synthesis flags this for a follow-on governance pass.

**What the verdict does NOT say:** ARC-071 is the transition machinery; it is not the transition itself. MECH-163's dual systems are still substrate-distinct (DMS / DLS in biology; planned / habitual in REE). ARC-071 is the operation that crosses the boundary between them, not a third system that subsumes them. The relation is: MECH-163 names the substrates; ARC-071 names the operation that pumps content across them.

A second-order observation: the absence-of-transition-mechanism in MECH-163 has been a known-but-unnamed gap since MECH-163 was registered. Several REE design discussions across the past months have implicitly assumed something like ARC-071 was happening (e.g. SD-039 anchor payload extending to "recipes" the agent has formed; MECH-292/293 ghost-goal bank acting on accumulated structure). ARC-071 explicitly fills the slot. The synthesis recommends the family doc and ARC-071 entry in claims.yaml record this -- ARC-071 closes a gap that has been hiding in plain sight.

---

## R4 -- Chunks-of-chunks recursion: how deep, and what tradeoffs?

### Verdict: PERMIT RECURSION TO 2-3 LEVELS. Botvinick / Niv / Barto 2009 supports deep hierarchy formally; biology rarely deeper than 2-3 in healthy operation; deeper hierarchies become brittle in hierarchical RL formalisms. Architectural requirement: chunks must carry initiation-set + termination-condition fields beyond the sequence itself. Confidence 0.72.

The evidence cluster:

- **Botvinick / Niv / Barto 2009 (PMID 18926527)** -- formal hierarchy with prefrontal-substrate mapping. Behaviour is divisible into discrete tasks containing subtask sequences containing simple actions. Each level of the hierarchy maps onto progressively more rostral / orbital prefrontal substrate.
- **Sutton / Precup / Singh 1999 (Artificial Intelligence 112:181-211)** -- formal options framework. Options can be composed of options (recursive); a set of options over an MDP forms a semi-MDP that supports further option-composition.

The R4 verdict has two parts.

**Part 1: depth limit.** ARC-071 should permit recursion (chunks-of-chunks) but cap it at 2-3 levels by default. Behavioural hierarchies in biology are rarely deeper than that in healthy operation -- "make coffee" decomposes into "boil water" + "grind beans" + "brew" + "pour" (1 level), and "boil water" might decompose further into "fill kettle" + "switch on" (2 levels), but rarely deeper. Hierarchical RL formalisms become brittle at depth (exploration over the option space explodes), and the prefrontal-substrate evidence has limited rostro-caudal extent (Botvinick 2008 TiCS estimates 4-5 levels at the architectural maximum). REE should default to 2-3 levels and treat deeper recursion as an exception requiring justification.

**Part 2: chunked-primitive structure.** The options-framework structure imposes an architectural requirement the slot's pre-registration did not capture. An option requires three fields: a policy (the sequence itself), an initiation set (context conditions under which the option fires), and a termination condition (when the option completes). ARC-071's chunked primitive cannot be just a sequence; it must carry context-keyed initiation and a completion signal. Without these, chunks will mis-fire in the wrong contexts or fail to terminate cleanly. The synthesis recommends adding initiation-set and termination-condition fields to ARC-071's chunk representation specification at child-MECH design time.

The caveats are non-trivial. Botvinick / Niv / Barto draw heavily on the hierarchical RL formalism; biology may not match this formalism exactly; the prefrontal-substrate evidence is correlational. Sutton 1999's value-side machinery (Q-learning over options) does NOT translate to ARC-071 because ARC-007 strict preserves value-flat hippocampal proposals. The synthesis treats the formalism as the cleanest computational framing while flagging that REE adopts the SHAPE (options as policy + initiation + termination) without the value-side machinery (Q-learning over options). Cross-link to ARC-007 strict preservation.

---

## R5 -- Outcome-consistency threshold for chunk formation and dissolution

### Verdict: GRADUAL VARIANCE THRESHOLD with chunk-size budget of 2-5 elements per level. Chunks dissolve under sustained outcome inconsistency on slower timescale than formation. Recommend implementation as sliding-window outcome-variance measure with form/dissolve thresholds asymmetric (form below F_low, dissolve above F_high, F_low < F_high). Confidence 0.71.

The evidence cluster:

- **Sakai et al. 2003 (PMID 12879170)** -- chunks typically 2-4 items, occasionally 5; chunks become clearer and more consistent as learning progresses (gradual not step-function).
- **Smith & Graybiel 2013 (PMID 23810540)** -- chunks form, dissolve, and reform across overtraining timescales; dissolution timescale is slower than formation timescale.
- **Graybiel 2008 (PMID 18558860)** -- chunking review with parametric range across rodent / primate / human (hundreds to thousands of repetitions in rodents; task-dependent in humans).

The R5 verdict has three parameterisation primitives.

**Primitive 1: chunk-size budget.** ARC-071 should default to chunks of 2-5 primitive elements per level. Larger chunks are biologically unusual at one level; if the agent needs to chunk a longer sequence, the right shape is hierarchical (chunk-of-chunks per R4) rather than a flat very-long-chunk. The chunk-size budget needs calibration at REE-primitive grain (Sakai's elements are finger-presses over milliseconds; REE's primitives are coarser action units over seconds), but the principle that chunks are SMALL at any one level is biologically robust.

**Primitive 2: variance threshold for chunk formation.** Chunks form when outcome variance over a sliding window drops below a threshold. The threshold is gradual not step-function -- chunks crystallise progressively as variance drops. ARC-071 implementation should track outcome variance over a sliding window (window-size to be determined experimentally; biology suggests 50-200 trials in rodents, scaled by task complexity) and form chunks when variance drops below a low threshold F_low.

**Primitive 3: variance threshold for chunk dissolution.** Chunks dissolve when sustained outcome variance rises above a higher threshold F_high. The dissolution threshold is HIGHER than the formation threshold (F_low < F_high) -- this is hysteresis, not symmetric thresholding. The dissolution timescale is also SLOWER than the formation timescale per Smith & Graybiel 2013 -- once formed, chunks persist longer than their formation window.

The implementation recommendation: ARC-071 should track per-chunk outcome-variance EWMA, form chunks when variance < F_low, dissolve chunks when variance > F_high (with F_low ~ 0.1-0.2, F_high ~ 0.4-0.5 as starting heuristics on a 0-1 normalised variance scale; child-MECH design pass should refine via parametric sweep). The cross-link to ARC-070 matters: chunk DISSOLUTION (chunk removed from proposal pool entirely) is distinct from chunk DECOMPOSITION (chunk re-segmented into sub-elements during simulation; original chunk persists). ARC-070 handles decomposition; ARC-071 handles formation AND dissolution. The synthesis recommends explicit registration of this distinction in the family doc.

The lower confidence (0.71) reflects that the parametric values are not precisely fixed by biology -- the literature gives a parametric RANGE rather than precise thresholds. The recommendation is to land starting heuristics in the first child-MECH and run a parametric sweep on a discriminative-pair experiment to refine.

---

## R6 -- SAFETY-CRITICAL: does biology distinguish real-executed from imagined/replayed in chunking write path?

### Verdict: NO. Biology does NOT cleanly gate the chunking write path against replay/imagined sequences. Sleep replay is part of the chunking machinery in biology, not gated out of it. ARC-071's pre-registered MECH-094 hypothesis_tag=False gating is therefore MORE CONSERVATIVE than biology, with substantive safety-vs-realism tradeoff implications. ESCALATE TO GOVERNANCE DECISION as a NEW REE GAP. Confidence 0.74.

This is the second load-bearing verdict the briefing flagged for extra synthesis effort. The verdict comes back with a substantive finding the pre-registration did not anticipate -- and one that requires explicit governance decision rather than a parameter choice the child-MECH design pass can settle privately.

The pre-registration assumed, on plausibility grounds, that biology gates the chunking write path against replay/imagined sequences -- "striatal LTP requires actual motor execution + dopaminergic confirmation, not imagined replay" was the briefing's expected finding. The literature evidence runs in the opposite direction:

- **Albouy et al. 2013 (PMID 23929594)** -- joint hippocampal-striatal reactivations during sleep, with hippocampal activity LEADING ventral striatal replays, drive sleep-dependent motor sequence consolidation INCLUDING chunk crystallisation. The competitive interaction between hippocampus and striatum during initial learning transforms into a cooperative interplay overnight, paralleling overnight performance enhancement.

The supporting context from the broader literature (Lansink 2009 hippocampal-VTA-ventral striatal replay coupling; van der Meer 2016 striatal replay; sleep-dependent motor consolidation more generally): sleep-replay-driven plasticity in the chunking circuit is well-documented. The hippocampus-striatum coupling is reward-prediction-biased -- the brain selectively consolidates replays of high-reward sequences -- but the consolidation does happen, and it does shape the chunking circuit.

The implication for ARC-071 design is substantive. REE has two architectural options:

**Option A: keep MECH-094 strict gating.** ARC-071 fires ONLY from real executed sequences with hypothesis_tag=False. This is MORE CONSERVATIVE than biology. It sacrifices the sleep-replay-driven chunk consolidation that biological systems get for free, but it eliminates the hallucinated-chunk risk that biology accepts. This is the current pre-registered design; it trades realism for safety.

**Option B: relax MECH-094 for ARC-071 with a sleep-mode value-conditioned exception.** Permit replay-driven chunking during sleep / DMN periods, but require value/reward-prediction conditioning (matching the Albouy 2013 reward-prediction bias). This is more biology-faithful but introduces residue-write through the simulation channel that MECH-094 was specifically built to prevent. The risk model: a hallucinated chunk that the value system mis-evaluates as high-reward would be promoted into the chunking pool with all the structural consequences ARC-071 implies (selectable atomically by hippocampal proposals, potentially chained recursively, etc.).

**Recommendation:** ESCALATE to governance decision. The decision touches MECH-094 (the hypothesis_tag substrate itself), ARC-071 (the chunking-write-path), MECH-292/293 (ghost-goal bank during waking probes -- analogous channel), the sleep-substrate cluster (sleep_substrate_plan.md is the relevant plan-of-record), and SD-039 anchor payload. The synthesis recommends a session dedicated to this decision rather than rolling it into the ARC-071 child-MECH design pass.

The right response may be: (a) keep MECH-094 strict and accept the realism gap; (b) carve out a sleep-specific exception in MECH-094 that ARC-071 alone can use under value-prediction-conditioning, with explicit replay-tagged chunk-formation-only-during-sleep gating; (c) treat the gap as a reason to develop a more sophisticated MECH-094-equivalent that distinguishes "value-confirmed-replay chunk consolidation" from "free-association DMN chunk hallucination" as separate write-modes. Option (c) is the most architecturally interesting but also the most work.

The synthesis is NOT recommending one option over the others -- the decision is architecturally consequential enough that it should be debated explicitly in a governance session, not absorbed into a child-MECH design pass. The synthesis's job is to surface that the decision exists and that the pre-registered Option A is not the cost-free default it appeared to be.

A second-order observation: this is the kind of finding that justifies the project's biology-before-formal-definitions rule (memory file feedback_biology_before_formal_definitions.md). The pre-registration assumed a biological gate that does not exist; the lit-pull surfaced the assumption. Without the lit-pull, ARC-071 would have been implemented with strict MECH-094 gating on the assumption that this matched biology -- a substantive realism gap would have entered the substrate without anyone noticing. The lit-pull caught it before the child-MECH design pass.

---

## What this pull does NOT settle

Items deferred to subsequent pulls or future sessions:

1. **The R6 governance decision itself.** The synthesis surfaces the safety-vs-realism tradeoff but does not pick a resolution. A dedicated session is required.
2. **ARC-070 lit-pull.** The companion slot needs its own targeted_review (decomposition-on-prediction-failure: hippocampal-prefrontal hierarchical control during planning, event segmentation theory imagination side, bottleneck-state subgoal discovery, mid-execution prediction-error machinery). The two slots are decoupled within the family per ARC-069, similar to how ARC-066 / ARC-067 / ARC-068 are decoupled within the non-deficit-action-drives family.
3. **Child MECH design for ARC-071 substrate.** The R2 verdict says ARC-071 substrate is at minimum two-component (striatal-analog + vmPFC-analog); the child MECH design pass needs to specify how the components compose, what the data flow is, and how the substrate maps onto REE's existing infrastructure (habit_substrate / vmPFC.md / MECH-163 habit system).
4. **Parameter calibration for R5 thresholds.** The variance thresholds (F_low, F_high) and window size for outcome-variance EWMA need calibration via parametric sweep on a discriminative-pair experiment. The first child-MECH validation experiment should design this sweep.
5. **Cognitive chunking dimension.** Graybiel 1998 / 2008 frame chunking as cognitive AND motor; the slot's pre-registration is silent on the cognitive extension. Whether ARC-071 covers cognitive-chunk formation (chunked rules, chunked schema) as well as motor-chunk formation is open.
6. **Pathology cross-references** (OCD, autism, motor-learning impairments). The slot's notes register these speculatively; Graybiel 2008 supplies more grounded framings (OCD as evaluative-gate failure rather than pure ARC-071-weakened) but the pathology mappings remain pre-registration. A future psychiatric_failure_modes.md update should integrate the lit-pull findings.
7. **Behavioural-latency signature for chunks.** Sakai 2003 supplies the inter-element-timing signature; the family doc's prediction is rollout deliberation cost drops; the synthesis suggests a sharper behavioural-latency prediction (faster within-chunk transitions than between-chunk transitions). The validation experiment design should use this signature.

---

## Recommended next actions

1. **Update the ARC-071 evidence_quality_note in claims.yaml** to reference this synthesis with the lit_conf computed below. Flag R3 confirmation (transition mechanism for MECH-163) and R6 escalation (safety-vs-realism tradeoff requiring governance decision).
2. **Update MECH-163's depends_on in claims.yaml** to add ARC-071 (R3 governance follow-on). MECH-163's claims.yaml entry currently does not list ARC-071 because ARC-071 was registered after MECH-163; the lit-pull confirms the depends_on update is warranted.
3. **Update the family doc** (`docs/architecture/policy_primitive_granularity.md`) to record: (a) R2 multi-substrate substrate registration (striatum + vmPFC-analog + frontoparietal involvement); (b) R3 confirmed transition mechanism with depends_on update; (c) R5 outcome-consistency threshold parameterisation with hysteresis (F_low < F_high) and chunk-size budget 2-5 per level; (d) R6 safety-vs-realism gap escalated to governance decision.
4. **Commission the ARC-070 lit-pull** (decomposition-on-prediction-failure). The two slots are decoupled within the family but the ARC-070 verdicts inform the chunk-dissolution / chunk-decomposition distinction for ARC-071 (R5).
5. **Schedule a governance session for the R6 decision.** Touches MECH-094, ARC-071, MECH-292/293, sleep_substrate cluster, SD-039. Should not be absorbed into the ARC-071 child-MECH design pass -- decide first, then design.
6. **Defer ARC-071 child-MECH design** until R6 governance decision lands. The child MECH cannot be specified without knowing whether replay-driven chunking is permitted.
7. **Queue the first ARC-071 validation experiment** once child MECH design completes. Discriminative pair: (ARM_0) ARC-071 OFF baseline, (ARM_1) ARC-071 ON in environment with structurally repeating sub-sequence (e.g. SD-054 reef + repeating forage-loop), measuring chunk-formation signature via behavioural latency drop on within-chunk transitions vs between-chunk transitions, and rollout deliberation cost reduction.

---

## Per-paper summary index

| Entry | DOI | Verdict it informs | Direction | Confidence |
|---|---|---|---|---|
| Graybiel 1998 | [10.1006/nlme.1998.3843](https://doi.org/10.1006/nlme.1998.3843) | R1 trigger, R2 substrate | supports | 0.84 |
| Graybiel 2008 | [10.1146/annurev.neuro.29.051605.112851](https://doi.org/10.1146/annurev.neuro.29.051605.112851) | R1 evaluative gating, R5 dynamics | supports | 0.78 |
| Yin & Knowlton 2006 | [10.1038/nrn1919](https://doi.org/10.1038/nrn1919) | R3 LOAD-BEARING substrate | supports | 0.83 |
| Smith & Graybiel 2013 | [10.1016/j.neuron.2013.05.038](https://doi.org/10.1016/j.neuron.2013.05.038) | R3 causal evidence, R5 dynamics | supports | 0.86 |
| Wymbs et al. 2012 | [10.1016/j.neuron.2012.03.038](https://doi.org/10.1016/j.neuron.2012.03.038) | R2 multi-substrate phase-dependent | supports | 0.79 |
| Sakai et al. 2003 | [10.1007/s00221-003-1548-8](https://doi.org/10.1007/s00221-003-1548-8) | R5 chunk size, threshold | supports | 0.74 |
| Botvinick / Niv / Barto 2009 | [10.1016/j.cognition.2008.08.011](https://doi.org/10.1016/j.cognition.2008.08.011) | R4 recursion + substrate | supports | 0.72 |
| Sutton / Precup / Singh 1999 | [10.1016/S0004-3702(99)00052-1](https://doi.org/10.1016/S0004-3702(99)00052-1) | R4 formal options structure | supports | 0.72 |
| Albouy et al. 2013 | [10.1002/hipo.22183](https://doi.org/10.1002/hipo.22183) | R6 SAFETY-CRITICAL gap | weakens | 0.78 |

**Aggregate ARC-071 lit_conf:** expected to land in the **0.74-0.78 range**, supports-direction net (8 supports + 1 weakens; load-bearing supports cluster averaging 0.79; the weakens-entry on Albouy 2013 (0.78 conf) applies specifically to the MECH-094 sub-assumption that biology gates replay-driven chunking -- it does NOT weaken the architectural commitment ARC-071 makes about chunk formation; it weakens the cleanness of the safety story). Weighted aggregate (mean weighted by confidence): (0.84+0.78+0.83+0.86+0.79+0.74+0.72+0.72+0.78)/9 = 6.06/9 = **0.78** (taking weakens as still contributing to confidence-in-the-claim's-evidential-grounding). The R3 verdict (transition mechanism for MECH-163 confirmed) is the strongest support; the R6 verdict (safety gap) is the most architecturally consequential finding.

The aggregate framing is "supports the architectural commitment with strong substrate attribution to phase-dependent multi-substrate machinery (DLS + IL/vmPFC + frontoparietal); confirms ARC-071 is the missing transition mechanism in MECH-163 (depends_on update warranted); weakens the pre-registered MECH-094 strict-gating assumption (R6 escalation required)".

According to PubMed and the cited journals, all entries in this synthesis are sourced from peer-reviewed literature with DOIs and PMIDs as cited above.
