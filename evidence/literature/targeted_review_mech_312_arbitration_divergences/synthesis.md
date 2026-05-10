# SYNTHESIS -- MECH-312 Arbitration Divergences (Focused Supplement)

**Pull 3 of 4** in the ARC-062 rule-apprehension cluster scoping series, FOCUSED SUPPLEMENT version. Original Pull 3 scope (full MECH-312 dual-channel arbitration review covering Daw 2005 / Doll 2012 / Lee 2014 / Smith-Graybiel / habit-vs-goal-directed dual-systems) is substantially covered by Pulls 2 and 4. This pull addresses only the four genuine REE divergences identified in Pull 4 R3 that no existing arbitration literature covers cleanly.
**Date:** 2026-05-10. **Entries:** 8 papers across the four divergence themes.

---

## Why this pull is a focused supplement

Pull 4's vocabulary-mapping verdict was that ~80% of REE's rule-apprehension cluster vocabulary maps cleanly to existing options/HRL/schema/meta-RL/MaxEnt-RL literature, and that the genuine REE contribution is concentrated in four specific divergences: (D1) MECH-094 simulation-mode write-gating, (D2) dual-stream affective-vs-discriminative arbitration (SD-010/011 -> MECH-312), (D3) per-region V_s-staleness modulating arbitration trust, and (D4) multi-variable arbitration combination rule beyond binary uncertainty. The original Pull 3 commission targeted ~12-15 papers across all of MECH-312 dual-channel arbitration; after Pull 4's narrowing, the appropriate scope is 5-8 papers focused on the four R3 divergences only.

Two papers per divergence: D1 = Joo & Frank 2018 (SWR review) + Foster & Wilson 2006 (reverse replay); D2 = Murray & Rudebeck 2018 (OFC value specializations) + Pessoa & Adolphs 2010 (amygdala "many roads"); D3 = Behrens et al. 2007 (ACC volatility) + Bouton 2004 (contextual renewal); D4 = Kool, Gershman & Cushman 2017 (cost-benefit arbitration) + Gershman, Guitart-Masip & Cavanagh 2021 (Pavlovian-instrumental arbitration with controllability).

---

## R1 -- MECH-094 simulation-mode write gating: any biological analog?

**Verdict: GENUINE-NOVELTY-CONFIRMED.** Confidence 0.72.

The biological substrate that REE's MECH-094 (and candidate MECH-319) would need is well-documented: hippocampal sharp-wave-ripples (SWRs) transmit compressed sequences of place-cell activity to cortical and subcortical targets, and these sequences carry structurally-discriminable signatures (temporal compression, often-reversed direction relative to waking experience) that downstream regions could in principle read off. Joo & Frank 2018 (the canonical NRN review) confirms the substrate's existence and its dual-purpose framing (immediate use + consolidation); Foster & Wilson 2006 demonstrates one specific structural marker (reverse temporal order during awake-quiescent replay) that is in-principle available as a discriminable signal.

What the literature does NOT contain is the specific REE function REE assigns to this substrate: a categorical write-gate that suppresses arbitration-weight updates which would otherwise fire if the same rule were applied during waking action. Joo & Frank treat downstream effects of SWR-driven cortical activity as continuous strength modulation (synaptic potentiation, association formation accumulating to consolidation), not as a categorical-tag-driven suppression of specific write rules. Foster & Wilson document the discriminable signal but say nothing about whether downstream regions exploit it as a write-gate. The substrate is right; the mechanism REE proposes is plausible-but-unverified at the cellular/synaptic level.

This is the cleanest "GENUINE-NOVELTY" verdict in this pull. The literature provides only the substrate (here is the SWR machinery, here is the discriminable replay signature); the REE-specific function (categorical write-gate keyed to a simulation tag) is a real REE contribution that future experimental work would need to validate biologically. Architectural recommendation in R5 below: KEEP-AS-IS, register MECH-319 as a candidate REE-novel substrate claim with explicit cross-reference to the MECH-094 hypothesis-tag motivation.

---

## R2 -- Dual-stream affective-vs-discriminative arbitration: any biological analog?

**Verdict: SUBSTANTIAL-OVERLAP for the structural premise, GENUINE-NOVELTY for the functional consequence.** Confidence 0.78.

The structural premise of REE's SD-010 (sensory-discriminative harm stream, z_harm_s) and SD-011 (affective harm stream, z_harm_a) is well-supported by primate ventral prefrontal cortex literature. Murray & Rudebeck 2018 documents that the macaque OFC + amygdala system has exactly two parallel streams carrying structurally-distinct content into downstream choice machinery: an amygdala-mediated affective/hedonic-value stream and a lateral-OFC + IT-cortex sensory-identity stream, with medial OFC integrating both into value-comparison. Pessoa & Adolphs 2010 reinforces the broader principle that affective evaluation is structurally separate from sensory-discriminative classification, with the caveat that the amygdala is best characterised as a coordinator of distributed evaluation rather than as a single affective output channel.

The supporting half: REE's two-stream architecture for harm-related content is biologically well-anchored. SD-010/011 are NOT REE-novel architectural commitments; they map cleanly to documented anatomy, with the only transfer caveat being that the literature is overwhelmingly reward-side and primate-focused while REE wants to apply the same structural premise to harm.

The novel half is downstream of where the literature stops. REE's MECH-312 proposes that these two streams are weighted distinctly into rule-arbitration: affective-stream load modulates which rule wins arbitration in a way that is dissociable from discriminative-stream content. The literature documents that the two streams exist and that they carry different content, but does NOT specify how they jointly modulate arbitration weights on competing rule channels. The Pessoa-Adolphs framework complicates the picture further by distributing affective evaluation across a network rather than localising it to a single source. So the REE-specific contribution is the functional claim that affective-stream load modulates rule-arbitration weights as a SEPARATE input from discriminative-stream content, with the modulation following a biologically-untested combination rule (additive logit, multiplicative gate, or other).

Architectural recommendation in R5: register the dual-stream architectural premise (SD-010/011) as literature-anchored (with explicit Murray-Rudebeck + Pessoa-Adolphs citations in evidence_quality_note), and register the affective-stream-modulation claim (MECH-312-c in the candidate sub-MECH split below) as a REE-specific functional extension to be tested experimentally.

---

## R3 -- Per-region V_s-staleness modulating arbitration trust: any biological analog?

**Verdict: PARTIAL-OVERLAP for the substrate, GENUINE-NOVELTY for the per-region scope and rule-trust function.** Confidence 0.65.

The closest existing-literature analog to REE's V_s machinery (MECH-269 verisimilitude scalar, MECH-284 broadcast invalidation, MECH-287 staleness propagation) is Behrens et al. 2007's demonstration that humans optimally track environmental volatility and that ACC encodes the volatility estimate. The structural premise — "the brain runs a metalearning signal about how trustworthy current beliefs are, and routes that signal into weight modulation" — is established. The substrate (ACC) and the function-class (modulation of downstream weights as a function of inferred trustworthiness) are biologically real.

The genuine REE divergence is on two axes: scope and function. On scope, Behrens 2007 estimates a single GLOBAL volatility level for the task as a whole; REE's V_s is per-region (each region of the world model carries its own freshness scalar). The closest behavioural cousin to per-region trust modulation is Bouton 2004's contextual-renewal framework, which demonstrates that biological agents do effectively maintain per-context "which of these competing associations is currently active" decisions — but Bouton treats context categorically (renewal/no-renewal), not as a continuous freshness scalar. The continuous-scalar per-region form REE proposes has not been directly demonstrated; it is most-closely-cousined by Gershman/Niv-style Bayesian latent-state context models, which still lack the per-region broadcast-invalidation feature REE has. On function, Behrens modulates LEARNING RATE on a single value estimate, whereas REE's V_s modulates RULE TRUST in arbitration. These are related but functionally distinct.

Architectural recommendation in R5: register V_s-modulated arbitration (MECH-312-d in the candidate sub-MECH split) as a REE-specific extension of a literature-supported substrate. Cross-reference Behrens 2007 + Bouton 2004 in evidence_quality_note as the closest cousins; mark the per-region-continuous-scalar and arbitration-trust-routing as REE-novel.

This is a weaker form of "genuine novelty" than R1: the literature provides BOTH the substrate AND a recognisable functional cousin, and the REE-specific contribution is in the precise scope and routing rather than in the existence of the mechanism class. R3's strength of novelty < R1's strength of novelty.

---

## R4 -- Multi-variable arbitration combination rule

**Verdict: MULTIPLICATIVE-GATE recommended as default for MECH-312, with empirical comparison to additive-logit baseline in V3-EXQ-543b/c.** Confidence 0.74.

The two papers in this divergence both directly address how multi-variable arbitration combines into channel weights. Kool, Gershman & Cushman 2017 demonstrate that human arbitration between model-based and model-free systems is governed by a cost-benefit calculation: subjects increase model-based control specifically when the additional accuracy it provides matters AND when the cognitive cost is justified by the accuracy gain. The combination is non-trivially-non-additive — uncertainty alone does not predict arbitration; the interaction with stakes does. Gershman, Guitart-Masip & Cavanagh 2021 extend this: arbitration between Pavlovian and instrumental control is dynamically updated within-session and is governed by an inferred controllability variable that is computationally separate from per-channel reliability. The two papers converge on the structural conclusion that multi-variable arbitration with dynamic within-session updating is the biological norm, NOT uncertainty-only quasi-static weighting.

For MECH-312's combination rule, this recommends a multiplicative-gate form with the following structure:

```
arbitration_weight[channel_k] = softmax_k( reliability[k] * cost_factor[k] * agency[k] * V_s[current_region] * practice_maturity[k] * ... )
```

Each channel's pre-softmax score is a product of (a) per-channel reliability (Daw 2005, Lee 2014 lineage from Pull 2), (b) per-channel cost or efficiency factor (Kool 2017), (c) per-channel agency/controllability (Gershman 2021), (d) global modulators including V_s freshness for the current region (R3 above) and practice maturity (Pull 2 R4). The product form ensures any one factor going to zero can effectively suppress a channel; the softmax ensures arbitration is well-defined across arbitrary numbers of channels.

The PRIMARY/SECONDARY hierarchy from Pull 2 R4 (uncertainty PRIMARY, practice-maturity SECONDARY) is preserved within this framework: uncertainty/reliability remains the largest-weight modulator empirically, but the combination rule is multiplicative across all modulators rather than additive with uncertainty alone. The Pull 1 R4 expansion to 3 channels (instrumental + diversity-pressure + others) and Pull 4 R4's multi-factor expansion are accommodated by the per-channel-product form.

Two transfer-risk caveats. First, Kool/Gershman/Cushman 2017 is two-controller; REE's MECH-312 is 3+ channels, and the multiplicative-gate combination rule may need to extend in non-trivial ways for larger competitor sets. Second, the modulating-variable mapping is approximate — REE's V_s, practice maturity, and diversity pressure do not all map cleanly to the literature's cost / controllability / reliability variables. The combination rule should be treated as a recommended default to be falsified against an additive-logit baseline in V3-EXQ-543b/c.

---

## R5 -- Recommended MECH-312 architecture: single claim or sub-MECH split?

**Verdict: SUB-MECH SPLIT with MECH-312 as parent.** Confidence 0.78.

The aggregate finding from R1-R4 is that MECH-312 has at least four functionally-distinct modulator categories with different biological provenance and different REE-vs-literature divergence profiles:

| Sub-MECH (proposed) | Modulator | Biological provenance | REE-vs-literature divergence |
|---|---|---|---|
| **MECH-312a** uncertainty/reliability weighting | per-channel reliability | Daw 2005 + Lee 2014 (Pull 2) | LOW -- direct literature mapping |
| **MECH-312b** practice/maturity weighting | training-history depth | Smith-Graybiel 2016 + Stachenfeld 2017 (Pull 2) | LOW-MEDIUM -- partial mapping |
| **MECH-312c** affective-stream modulation | z_harm_a load (SD-011) | Murray-Rudebeck 2018 + Pessoa-Adolphs 2010 (R2) | MEDIUM-HIGH -- functional consequence is REE-novel |
| **MECH-312d** V_s freshness modulation | per-region freshness scalar | Behrens 2007 + Bouton 2004 (R3) | HIGH -- per-region scope and rule-trust function are REE-novel |

A fifth sub-MECH may be warranted depending on the V3-EXQ-543b/c results:

| **MECH-312e** (candidate) controllability/agency modulation | per-channel agency confidence | Gershman 2021 (R4) | MEDIUM-HIGH -- requires REE-side operationalisation |

Reasons to prefer a sub-MECH split over a single monolithic MECH-312:

1. **Heterogeneous provenance** -- MECH-312a is direct literature-mapping while MECH-312d is high-novelty; bundling them under one claim conflates "this is well-established arbitration weighting" with "this is REE-specific extension". The 2D quadrant placement (high/low exp_conf x high/low lit_conf) would land each sub-claim in a different cell, which the unified MECH-312 cannot represent.

2. **Independent testability** -- each modulator can be falsified separately by ablating it from the arbitration formula and comparing behaviour. V3-EXQ-543b/c will need to test individual modulators; the sub-MECH structure makes the test/claim mapping cleaner.

3. **Independent governance** -- the affective-stream-modulation claim (312c) and V_s-modulation claim (312d) have different evidence-direction trajectories from uncertainty-weighting (312a), and the explorer surface should be able to show their evidence accumulation separately rather than averaging them under a single MECH-312.

4. **Pull 4 R5 already foreshadowed this** -- Pull 4 explicitly recommended that the dual-stream affective-rule-weighting interaction (SD-010/011 -> MECH-312) "should be registered as a MECH-312 sub-claim (e.g. MECH-312d affective-stream-modulation-of-arbitration) rather than absorbed silently". This pull's R2 reaffirms that recommendation.

The parent MECH-312 then carries the load of asserting "rule-arbitration in BG-cortical loops is multi-variable multi-channel and dynamically updated within-session" -- a high-level architectural claim well-supported by Pull 2 + Pull 4 + this pull's R4 entries. Sub-MECHs carry the load of specifying which modulators are involved.

---

## Recommended MECH-094 / MECH-319 final shape

For MECH-094 (existing claim): KEEP-AS-IS. Pull 4 R3 already recommended this; this pull's R1 reaffirms with substrate-availability evidence (Joo-Frank, Foster-Wilson) and explicit acknowledgement that the specific functional consequence is REE-novel.

For candidate MECH-319 (simulation-mode-rule-write-gating): REGISTER AS REE-NOVEL CANDIDATE. The R1 verdict is GENUINE-NOVELTY-CONFIRMED, with the substrate provided by SWR machinery + reverse-replay discriminable signature. The REE-specific functional claim — that downstream rule-write machinery uses the discriminable replay signature to suppress arbitration-weight updates — is biologically plausible but unverified. Register MECH-319 with substrate cross-references (Joo-Frank 2018, Foster-Wilson 2006) and a clear evidence_quality_note flagging that the substrate-availability premise is well-supported but the functional consequence is REE-specific and pending V3+V4 substrate experiments.

---

## What this pull does NOT settle

1. **The Smith-Graybiel cluster as separate divergence.** Pull 4 marked Smith-Graybiel 2013/2016 as covering the practice/maturity modulator; this pull did not directly retest. If V3-EXQ-543b/c surfaces evidence that practice maturity arbitrates differently from uncertainty in REE's substrate, a re-pull on Smith-Graybiel may be warranted.

2. **The Lee/Shimojo/O'Doherty 2014 extension question.** The original Pull 3 commission included "verify and extend" Lee 2014. Lee 2014 is already in Pull 2 (entry: 2026-05-10_arc_064_arbitration_neural_substrate_lee_2014). This pull does not duplicate that entry; the R4 verdict relies on Pull 2's existing Lee 2014 entry plus this pull's two new R4 entries.

3. **The MECH-309 logical-necessity reformulation.** Pull 4 R3 (d) tagged MECH-309 as a fourth genuine REE divergence; this pull does not address it directly because it is not arbitration-stage substrate. MECH-309 reformulation is post-cluster-registration substrate-design work.

4. **Gershman/Niv Bayesian latent-state context models.** R3 noted these as the closest cousin to V_s; this pull did not formally entry them. A future supplementary pull could formalise the Gershman-Niv anchor for V_s if the V3-EXQ V_s experiments justify it.

5. **The exact form of the multiplicative-gate combination rule.** R4 recommends multiplicative-gate as default but does not specify the precise functional form (which factors enter as products vs sums, what saturating non-linearities apply, etc.). This is a substrate-design call to be made when MECH-312 sub-MECHs are operationalised in V3 substrate.

6. **Whether MECH-312e (controllability/agency) is genuinely needed.** Listed as "candidate" sub-MECH only; depends on whether V3 has any substrate that would carry agency-confidence per channel. If not, fold into MECH-312a until V4.

---

## Aggregate Pull 3 headline

The four R3 genuine REE divergences from Pull 4 hold up under the focused lit pull. R1 (MECH-094 simulation-mode write-gating) is the strongest novelty -- the literature provides only the substrate. R2 (dual-stream affective-vs-discriminative) splits into well-anchored structural premise + REE-novel functional consequence. R3 (per-region V_s) is partial-overlap with literature cousins on substrate and function-class but REE-novel on per-region scope and rule-trust routing. R4 (multi-variable combination rule) recommends multiplicative-gate as default with empirical comparison to additive-logit baseline.

R5 recommends a SUB-MECH SPLIT for MECH-312 with at least four sub-claims (a uncertainty, b practice, c affective-stream, d V_s freshness) and a candidate fifth (e controllability/agency). MECH-094 stays as-is; MECH-319 (simulation-mode-rule-write-gating) registers as REE-novel candidate with substrate cross-references.

Cluster registration in claims.yaml + V3-EXQ-543b/c script revisions are deferred to subsequent sessions per skill rules.

---

## Per-paper summary index

| Entry | DOI | Divergence | Direction | Confidence |
|---|---|---|---|---|
| Joo & Frank 2018 | [10.1038/s41583-018-0077-1](https://doi.org/10.1038/s41583-018-0077-1) | D1 SWR substrate | mixed | 0.62 |
| Foster & Wilson 2006 | [10.1038/nature04587](https://doi.org/10.1038/nature04587) | D1 reverse replay marker | supports | 0.74 |
| Murray & Rudebeck 2018 | [10.1038/s41583-018-0013-4](https://doi.org/10.1038/s41583-018-0013-4) | D2 dual-stream OFC | supports | 0.78 |
| Pessoa & Adolphs 2010 | [10.1038/nrn2920](https://doi.org/10.1038/nrn2920) | D2 amygdala distributed | supports | 0.68 |
| Behrens et al. 2007 | [10.1038/nn1954](https://doi.org/10.1038/nn1954) | D3 ACC volatility | mixed | 0.60 |
| Bouton 2004 | [10.1101/lm.78804](https://doi.org/10.1101/lm.78804) | D3 contextual renewal | supports | 0.65 |
| Kool, Gershman & Cushman 2017 | [10.1177/0956797617708288](https://doi.org/10.1177/0956797617708288) | D4 cost-benefit arbitration | supports | 0.74 |
| Gershman, Guitart-Masip & Cavanagh 2021 | [10.1371/journal.pcbi.1008553](https://doi.org/10.1371/journal.pcbi.1008553) | D4 multi-variable Pavlovian-instrumental | supports | 0.70 |

**Aggregate Pull 3 lit_conf** for MECH-312 (post-indexer): expected to land in the 0.66-0.72 range. Two mixed-direction entries (Joo-Frank, Behrens) provide the calibration that the literature does not fully cover the REE-specific claims; six supports-direction entries cover the substrate-availability premises.
