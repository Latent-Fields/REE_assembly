# SYNTHESIS — ARC-067 Idle Aversion / Boredom (Sustained-Low-Engagement Aversive Valence Accumulator)

**Pull 2 of 3** in the non_deficit_action_drives family (companion to ARC-066 tonic vigor and ARC-068 opportunity cost).
**Date:** 2026-05-10. **Entries:** 8 papers (definitional review, attentional theory, emotion-differentiation empirical, functional review, behavioural-aversive Science paper, fMRI neural-correlates, HPA chronic-stress substrate, transdiagnostic apathy-anhedonia).
**Source attribution:** the per-paper records cite PubMed where indexed and include DOI links; this synthesis aggregates and adjudicates rather than re-citing each paper exhaustively.

---

## Why this pull was commissioned

The non_deficit_action_drives family was registered 2026-05-10 from a phenomenology observation: REE's behavioural-source slots are all deficit-keyed (threats, depletion, novelty-as-information-gap), so a well-fed safe agent in familiar territory has no gradient to act and only MECH-313 noise floor prevents inertia. Biology has a different equilibrium — restlessness when bored, drive to act when fresh, the felt cost of doing nothing. Three architectural slots were registered to close this gap: ARC-066 (positive-side capacity-deploy bias), ARC-067 (negative-side engagement-failure aversive), and ARC-068 (opportunity-cost penalty on passivity).

ARC-067 is the aversive-side accumulator. The pre-registration evidence_quality_note declared a lit-pull required before child MECH/SD design, per the project rule that any architectural slot which instantiates a formal concept (here: engagement-failure as aversive valence) needs biology-before-formal-definitions. The boredom literature is broader and less convergent than the vigor literature, so the synthesis effort had to focus on arbitrating between accounts rather than gathering convergent support.

---

## R1 — Functional account arbitration

### Verdict: PRIMARY = engagement-rate aversive accumulator (Eastwood / van Tilburg / Bench-Lench functional-emotion lineage). MAC meaning-component as secondary parallel channel. ARC-068 opportunity-cost is on a different architectural layer. Confidence 0.80.

The three competing accounts the user pre-registered have specific strengths that decompose cleanly when read against the cohort:

- **(a) Eastwood / van Tilburg / Bench-Lench functional-emotion lineage.** Boredom is the aversive experience of wanting-to-engage-but-unable; it is a functional emotion that motivates the pursuit of new (meaningful) goals. This lineage is the dominant theoretical and empirical anchor across the cohort. Eastwood's "wanting-but-unable" definition maps directly onto ARC-067's engagement-rate aversive accumulator. van Tilburg's meaning-seeking action tendency constrains the discharge condition. Bench-Lench's goal-shift function specifies what the accumulator is *for* architecturally (trajectory shift, not just generic action elevation).

- **(b) Westgate & Wilson MAC attentional component.** Boredom arises from attentional misfit — cognitive demands vs available resources. The attentional channel in MAC is roughly equivalent to the engagement-rate aversive accumulator the user pre-registered, but MAC further decomposes the upstream into both under- and over-stimulation routes. The MAC attentional component is therefore not a competing account but a refinement of the primary account.

- **(c) Opportunity-cost-felt overlap with ARC-068.** Westgate & Wilson's MAC-meaning component (mismatch between activity and valued goals, including absence of valued goals) is conceptually adjacent to ARC-068's opportunity-cost framing but mechanistically distinct: meaning-misfit is teleological (about goal-task fit), opportunity cost is value-driven (about expected reward foregone). Wilson 2014's self-shock finding shows that boredom-aversive recruits costly action *exchangeable* with physical pain — that exchangeability is on the z_harm_a / valence axis, not on the E3 score axis where opportunity cost lives.

The arbitrated reading: ARC-067's primary mechanism is the engagement-rate aversive accumulator (lineage a). Westgate & Wilson's MAC meaning-component (the part of lineage b not collapsible into the engagement-rate account) should be implemented as a *parallel secondary channel* that converges on the ARC-067 valence accumulator from the existing z_goal substrate (SD-012 / MECH-308). This is architecturally cheap because the meaning channel reuses existing substrate rather than building a new estimator. ARC-068 stays on a different layer entirely and composes at the E3 score level.

For child-MECH design this means a two-input convergence at the boredom valence accumulator: a primary engagement-rate input from executive proxies and a secondary meaning-misfit input from the z_goal substrate. The relative weighting is a child-MECH calibration question.

---

## R2 — Timescale split: acute restlessness vs chronic anhedonic flatness

### Verdict: BIOLOGY SUPPORTS THE SPLIT. FLAG to governance for slot decision; DO NOT EXECUTE. Confidence 0.72.

The user's pre-registration suggested two timescales — acute restlessness (~minutes / tens of episodes) and chronic anhedonic flatness (~episodes / sessions) — that may need separate child claims. The literature settles this question only partially.

**Acute timescale evidence is strong.** Wilson 2014's 6-15 minute experimental window is the cleanest direct evidence for an acute boredom-aversive that fires within minutes and reaches the threshold to recruit costly action. Danckert 2018's video-induced-boredom paradigm operates at the minutes-scale and produces detectable AIC-deactivation. The acute mechanism is not in dispute.

**Chronic timescale evidence is biology-context only.** Ulrich-Lai & Herman 2009 establishes that chronic stress regimes (including under-stimulation and loss-of-control) produce sustained substrate signatures distinct from acute stress — flattened diurnal cortisol rhythms, blunted reactivity, downstream affective consequences. This is a *separable substrate* in real biology, not just a slow extension of the acute mechanism. The Husain-Roiser 2018 review's discussion of apathy as a chronic motivational syndrome with frontostriatal substrate signatures is independently consistent: chronic apathy looks substrate-level different from acute boredom-aversive (different lesion patterns, different effort-cost-benefit profiles).

The verdict: the timescale split is **biologically supported in principle**. Acute restlessness and chronic anhedonic flatness are not just two ends of one rate-constant curve; they involve at least partly distinct substrates in real biology. Whether REE should split the slot into two child claims (MECH-Xa acute / MECH-Xb chronic) is a *governance call* — splitting requires (1) committing to two separate substrates and (2) deciding the cross-talk architecture between them. The lit-pull cannot make that call; it confirms the split is justifiable.

**Recommended flag to governance:** when child-MECH design proceeds, the design proposal should default to a two-child split (acute / chronic) with explicit cross-talk specification, but should also offer a single-child unified-substrate option for cost-comparison. The split is the literature-justified default; the unified option is the cost-controlled fallback.

---

## R3 — Routing channel: z_harm_a vs separate engagement-rate scalar

### Verdict: ROUTE THROUGH z_harm_a (SD-011 affective harm stream / AIC analog). Confidence 0.82.

The user pre-registered two options: (A) route the boredom aversive through z_harm_a / affective stream, with engagement-failure feeding into the same channel as actual harm; or (B) maintain a separate engagement-rate scalar that converges on a downstream consumer of z_harm_a but does not directly write to z_harm_a. The literature settles this in favour of A.

**Anatomical anchor: Danckert 2018.** Boredom produces AIC deactivation (anticorrelated with DMN activation), distinguishable from rest. The AIC is the anatomical home of the affective-salience integrator (Critchley lineage), which is the biological correlate of REE's z_harm_a / SD-011 affective stream. Boredom is therefore in the AIC functional territory — by deactivation, indicating that the agent is not assigning affective salience to the current task, which is precisely the engagement-failure signature ARC-067 names. This is more parsimoniously implemented as routing-through-z_harm_a (with the engagement-rate signal modulating activity on that channel) than as a separate scalar that converges only at action-selection.

**Behavioural-exchangeability anchor: Wilson 2014.** The self-shock finding is the cleanest available evidence that boredom-aversive and physical pain-aversive are *exchangeable*: humans treat them as substitutable enough to trade one for the other. Exchangeability requires a shared axis. If the substrates were architecturally separate (Option B), the agent would need a costly cross-substrate comparison computation to make this trade. If they share an axis (Option A, both on z_harm_a / affective stream), the trade is automatic via the standard valence comparison.

**Functional-emotion convergence: van Tilburg 2017.** The empirical signature (low-arousal but action-recruiting) is unusual but exactly what z_harm_a / affective stream supports. Routing through z_harm_a allows low-arousal aversive content without recruiting the high-arousal SD-037 broadcast-override / orexin substrate. A separate engagement-rate scalar would need an explicit non-arousal-coupling mechanism to reproduce this signature; routing through z_harm_a gets it for free because z_harm_a already supports varying arousal levels independently of valence magnitude.

For child-MECH design this means: the engagement-rate estimator computes a positive-engagement scalar; when the integrated engagement falls below threshold, a slow accumulator writes negative valence to z_harm_a (specifically, to the boredom sub-channel of the affective stream). The accumulator's output is added to the z_harm_a aggregate that drives E3 score-bias on the same axis as physical harm. This is architecturally clean and matches all three anchor-evidence sources.

---

## R4 — Engagement-rate estimator inputs

### Verdict: KEEP commit transitions per episode, E3 deliberation depth, residue-write rate. DROP novel-observation count as primary input. Confidence 0.74.

The user pre-registered four candidates: commit transitions per episode (rare commits → low engagement), novel-observation count (familiar surroundings → low engagement), E3 deliberation depth (shallow selection → low engagement), and residue-write rate (no learning happening → low engagement). The literature narrows the biologically-grounded subset.

**Commit transitions per episode: KEEP.** Bench & Lench's goal-pursuit-shift framing makes commit-transition-rate a direct functional analog: rare commits correspond to the agent staying on a single trajectory without progress, which is exactly the goal-pursuit-failure boredom is supposed to remedy. Westgate & Wilson's attentional component is also consistent — low commit-transition rate is a signature of executive-control disengagement.

**E3 deliberation depth: KEEP.** Danckert 2018's AIC-deactivation under boredom is interpreted as failure to engage *executive control networks* during a monotonous task. E3 deliberation depth is the cleanest REE analog of executive-control engagement: shallow selection means the agent is not deliberating, which is the executive-engagement-failure signature.

**Residue-write rate: KEEP.** Bench & Lench's goal-shift function presupposes that the agent is updating its world model — boredom should fire when learning is not happening, which is exactly what residue-write-rate measures. Husain-Roiser's effort-allocation framework is also consistent: the cost-benefit computation in apathy/boredom is sensitive to whether the agent is *getting something* out of the current activity, which residue-write-rate operationalises.

**Novel-observation count: DROP as primary input.** This is the load-bearing R4 sub-verdict. van Tilburg & Igou 2017's empirical differentiation showed that boredom is meaning-seeking, not stimulation-seeking; novel territory without engagement opportunity does not discharge boredom. Westgate & Wilson 2018 makes the same distinction: the attentional component is about cognitive-demand-vs-resources misfit, not about novelty rate. Treating novel-observation count as a primary engagement-rate input would conflate ARC-067 with MECH-314a striatal novelty bonus — and as the registration disambiguation already specifies, novelty is not engagement.

Novel-observation count *may* contribute as a *secondary positive engagement signal* (i.e., the engagement-rate estimator may treat genuine novelty as one source of engagement among several), but it should NOT be a primary input to the boredom side of the comparator. The boredom signature must remain dominated by attentional / executive / effort-allocation proxies, with novelty playing at most a downstream supportive role.

For child-MECH design this means a three-input executive engagement-rate estimator (commit transitions, deliberation depth, residue-write rate) feeding the negative side of the boredom comparator, with novelty as an optional secondary input on the positive side only.

---

## R5 — Anhedonia / abulia / catatonic flatness anchor

### Verdict: ARC-067 ablation maps onto APATHY (Husain-Roiser frontostriatal effort-allocation failure), specifically NOT anhedonia (reward-experience failure / MECH-295 liking-channel). ANCHOR ONLY; do not register pathology mapping. Confidence 0.78.

The pre-registration framed the clinical inverse of healthy ARC-067 as "anhedonia / abulia / catatonic flatness." Husain & Roiser 2018 forces a precision the pre-registration anticipated but did not yet make:

- **Anhedonia** is reward-experience failure. In REE this maps onto MECH-295 (liking channel) and the dopaminergic reward-prediction-error pathway. **NOT what ARC-067-OFF produces.**
- **Apathy** is effort-allocation failure: the agent has preserved hedonic experience and preserved capacity but does not mobilise that capacity into action. **What ARC-067-OFF should produce.**
- **Abulia** sits in the middle of the diminished-motivation spectrum and can have either substrate as primary, depending on lesion location.

ARC-067 is structurally the apathy substrate, not the anhedonia substrate. This precision matters because the future psychiatric_failure_modes.md cross-reference must avoid muddying the substrate-to-pathology mapping. Ablation phenotype prediction: capacity preserved (E1/E2/E3 healthy), reward-processing preserved (MECH-295 working), but no aversive-pressure to mobilise capacity (no engagement-rate-driven z_harm_a write). The clinical analog is apathy; the substrate-correlate is the frontostriatal circuit (VTA → ventral striatum / NAcc / ventral pallidum → mPFC / dACC).

The Ulrich-Lai & Herman HPA-axis substrate context complements this: chronic apathetic states (clinical depression, burnout, learned helplessness) involve HPA-axis dysregulation in addition to the frontostriatal effort-allocation pattern, mapping onto the chronic-pole of the R2 timescale split.

**This is anchor only.** The actual psychiatric_failure_modes.md cross-reference is a future governance pass; the synthesis here documents the substrate logic so that pass can proceed without re-doing the lit-pull. The cross-reference, when built, should:

1. Cite Husain & Roiser 2018 for the apathy-anhedonia distinction.
2. Map ARC-067-OFF onto the apathy *architectural archetype*, NOT onto a single specific clinical diagnosis.
3. Distinguish the acute pole (acute boredom intolerance, found in some impulsivity / sensation-seeking presentations) from the chronic pole (depressive / abulia / burnout cluster) per the R2 split.
4. Cite Ulrich-Lai & Herman 2009 as substrate context for the chronic-pole HPA-axis involvement.
5. Maintain mechanistic distinction from anhedonia substrates (MECH-295 liking-channel collapse), which would be a separate governance entry under psychiatric_failure_modes.md.

---

## What this pull does NOT settle

Items deferred to subsequent work:

1. **The acute / chronic split execution.** R2 supports the split biologically but the slot decision is governance, not lit-pull. Child-MECH design proposal should default to two-child split with cross-talk specification, but the actual MECH numbers and substrate parameterisation are not assigned in this pull.

2. **Quantitative engagement-rate estimator calibration.** R4 narrows the inputs to three executive-engagement proxies but does not specify weighting, integration time-constant, or threshold-for-aversive-onset. These are empirical-calibration questions; first child-MECH validation experiment should sweep parametrically.

3. **The MAC meaning-component channel.** R1 supports a parallel meaning-misfit secondary channel, but how it integrates with the engagement-rate primary channel (additive sum / max / multiplicative gate / etc.) is not literature-resolvable. Child-MECH design should propose a default and discriminate experimentally.

4. **The boredom-impulsivity / risk-taking failure-mode literature.** Bench & Lench cite this extensively but the cohort here did not pull dedicated entries. If pathological-ARC-067-overfiring becomes a governance topic (e.g., as a calibration anchor for healthy-substrate parameterisation), a follow-up pull on Zuckerman sensation-seeking, boredom-proneness scales, and ADHD-impulsivity overlap would be appropriate.

5. **Cross-reference to ARC-068 opportunity-cost.** R1 confirmed mechanistic distinctness (different layers) but a future joint family-level review may wish to specify the composition more precisely. Defer to ARC-068's own lit-pull (Pull 3 of 3).

6. **Alternative single-component models.** Post-2018 boredom literature (notably Eastwood-lab reformulations and FEP-flavoured learning-progress accounts) propose collapsing both MAC components into a single information-gain failure signal. The cohort here did not pull dedicated entries on these alternatives — the synthesis defaults to MAC as the dominant decomposition, but the alternative remains plausible. Worth flagging if subsequent child-MECH validation experiments produce signatures that resist the two-component reading.

---

## Recommended next actions

1. **Extend ARC-067 evidence_quality_note** with the lit_conf summary and the R1-R5 verdicts, citing this synthesis (handled in this commit).

2. **Flag R2 to governance** — slot-split decision (one child claim vs two) for the acute / chronic timescale separation. Recommendation: schedule the slot-split call after Pull 3 (ARC-068) lands, so the family-level architecture is fully specified before child-MECH design begins.

3. **Commission Pull 3 (ARC-068 opportunity cost)** — the third of three lit-pulls in the non_deficit_action_drives family. Pull 3's outcome interacts with R1's secondary-meaning-channel decision and with the family-level composition specification.

4. **Hold off on child-MECH registration** until the R2 governance call lands. The child-MECH count (one or two) determines the rest of the design pipeline; registering child MECHs before that decision risks rework.

5. **Reserve a future psychiatric_failure_modes.md governance pass** — the R5 anchor is in place but the actual cross-reference document is a separate governance call that should cover the apathy / anhedonia / abulia substrate map systematically, not piecemeal per ARC.

---

## Per-paper summary index

| Entry | DOI | Verdict it informs | Direction | Confidence |
|---|---|---|---|---|
| Eastwood 2012 | [10.1177/1745691612456044](https://doi.org/10.1177/1745691612456044) | R1 (definitional) | supports | 0.78 |
| Westgate & Wilson 2018 | [10.1037/rev0000097](https://doi.org/10.1037/rev0000097) | R1, R2 | supports | 0.82 |
| van Tilburg & Igou 2017 | [10.1037/emo0000233](https://doi.org/10.1037/emo0000233) | R1, R5 | supports | 0.74 |
| Bench & Lench 2013 | [10.3390/bs3030459](https://doi.org/10.3390/bs3030459) | R1, R4 | supports | 0.66 |
| Wilson et al. 2014 | [10.1126/science.1250830](https://doi.org/10.1126/science.1250830) | R3, R2 acute | supports | 0.78 |
| Danckert & Merrifield 2018 | [10.1007/s00221-016-4617-5](https://doi.org/10.1007/s00221-016-4617-5) | R3, R4 | supports | 0.72 |
| Ulrich-Lai & Herman 2009 | [10.1038/nrn2647](https://doi.org/10.1038/nrn2647) | R2 chronic, R5 substrate | mixed | 0.55 |
| Husain & Roiser 2018 | [10.1038/s41583-018-0029-9](https://doi.org/10.1038/s41583-018-0029-9) | R5 | supports | 0.78 |

**Aggregate ARC-067 lit_conf** (post-indexer): expected to land in the **0.72-0.76** range. Supports-direction, 8-entry cohort with one intentionally-low-confidence substrate-context entry (Ulrich-Lai). Cohort spans definitional theory, attentional theory, emotion-differentiation empirical, behavioural-aversive empirical (Science), fMRI neural-correlates, chronic-stress substrate context, and transdiagnostic apathy substrate.

According to PubMed and the venue records cited above, all entries in this synthesis are sourced from peer-reviewed literature with DOIs as cited.
