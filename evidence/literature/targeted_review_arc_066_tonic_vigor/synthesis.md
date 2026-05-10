# SYNTHESIS -- ARC-066 Tonic Vigor Coupling (capacity-keyed action drive)

**Pull commissioned:** 2026-05-10 from the non_deficit_action_drives architectural family registration session.
**Companion pulls (deferred):** ARC-067 idle-aversion / boredom; ARC-068 opportunity-cost no-op penalty.
**Date:** 2026-05-10. **Entries:** 7 papers (mesolimbic-DA-vigor formalism, human-pharmacological causal test, mesolimbic-DA substrate review, LC-NE adaptive-gain theory + the empirical test that disambiguates it, ACC effort-cost lesion, BAS personality / abstract-level commitment).
**Source attribution:** the per-paper records cite PubMed entries with DOIs and PMIDs as listed; this synthesis aggregates and adjudicates rather than re-citing each paper exhaustively.

---

## Why this pull was commissioned

ARC-066 was registered 2026-05-10 from a phenomenological observation by the user (consultant psychiatrist + REE author): "I observe a drive in me to do something while I have energy rather than nothing / imagination and other non-behavioural work. In REE it seems that the agent is happy doing nothing." The architectural insight: every existing REE behavioural-source slot is keyed to a deficit (z_harm threats, z_goal seeded from depletion, novelty / curiosity from unfamiliarity). A well-fed-safe-familiar agent has no positive gradient to act. Biology has a positive gradient.

ARC-066 is the first of three slots in the non_deficit_action_drives family. It names the architectural slot for a target-free, capacity-keyed positive bias toward action over no-op. The companion slots (ARC-067 idle-aversion, ARC-068 opportunity-cost-on-passive) cover the aversive-of-rest and cost-of-passivity halves of the same architectural commitment. This pull is the first of three required before child MECH/SD design (per the project's biology-before-formal-definitions rule).

Four falsifiable verdicts were pre-specified in the briefing. The synthesis settles each at a stated confidence; one of them carries a substantive substrate-attribution reframe relative to the slot's pre-registered anchor cluster.

---

## R1 -- Substrate attribution: DA-vigor vs LC-NE-direction vs BAS-abstract

### Verdict: MESOLIMBIC DA-VIGOR is load-bearing. LC-NE-direction is rejected. BAS is the abstract-level commitment, not a separate substrate. Confidence 0.78.

The evidence cluster:

- **Niv et al. 2007 (Psychopharmacology, PMID 17031711)** -- theoretical-formal anchor. The long-run average rate of reward functions as an opportunity cost on time and is reported by tonic dopamine in the nucleus accumbens. Higher tonic DA produces faster, more vigorous responding regardless of any specific phasic prediction. The mathematical structure is target-free. Confidence 0.83.
- **Salamone & Correa 2012 (Neuron, PMID 23141060)** -- substrate identity. Mesolimbic DA encodes the activational dimension of motivation (behavioural activation, exertion of effort, sustained task engagement), dissociable from hedonic / consummatory functions. Quote: "DA antagonism and accumbens DA depletions have a greater effect on appetitive, instrumental, preparatory or seeking behavior, as well as behavioral activation and 'wanting', while having less effect on consummatory behavior, directional aspects of motivation, and 'liking'." Confidence 0.80.
- **Beierholm et al. 2013 (Neuropsychopharmacology, PMID 23419875)** -- human pharmacological causal test. Double-blind three-arm design (placebo, L-DOPA, citalopram) in 90 healthy subjects. The relationship between average reward rate and response vigor was significantly stronger under L-DOPA than under placebo; citalopram did not produce the same effect. Confidence 0.79.
- **Depue & Collins 1999 (Behav Brain Sci, PMID 11301519)** -- abstract-level commitment. The BAS (behavioural approach / activation system) tonic baseline is a target-free dopamine-keyed activational scalar that varies both within-individual within-time and between-individuals as a personality dimension. Confidence 0.66.

The DA-vigor cluster (Niv 2007 + Salamone & Correa 2012 + Beierholm 2013) gives a complete substrate package: formalism + substrate identity + human causal test. The BAS cluster (Depue & Collins) is the abstract-level commitment that the function is real and target-free at the personality level. Together they nominate mesolimbic DA-vigor as the load-bearing substrate for ARC-066.

The LC-NE-direction substrate (pre-registered as a primary anchor via Aston-Jones & Cohen 2005) is rejected -- see R2 below for the disambiguation. The R1 substrate attribution should not include LC-NE.

The R2 verdict has direct substrate-attribution consequences: the family doc currently lists Aston-Jones & Cohen 2005 in the ARC-066 anchor cluster with the gloss "directional bias TOWARD action, not noise on choice". This attribution is wrong under current evidence and the synthesis recommends governance update remove Aston-Jones from ARC-066's primary anchors and reposition it as a "what ARC-066 is NOT" anchor (LC-NE tonic mode is noise-mediated, covered by MECH-313, not a separate ARC-066 function).

---

## R2 -- Noise vs direction: is LC-NE tonic mode ONE mechanism or TWO?

### Verdict: ONE mechanism. LC-NE tonic mode is noise (= MECH-313). Direction is not present in the LC-NE substrate; ARC-066 must be attributed to mesolimbic DA-vigor. NO slot split required. Confidence 0.78.

The disambiguation paper is the load-bearing item:

- **Kane et al. 2017 (Cogn Affect Behav Neurosci, PMID 28900892)** -- DREADD-mediated chemogenetic stimulation of LC tonic activity in Long-Evans rats on a patch-foraging task, with formal model comparison between (a) increased decision noise and (b) systematic shift of leave threshold. Result quote: "This effect is best explained by an increase in decision noise rather than a systematic bias to leave earlier (i.e., at higher values)." Confidence 0.82.

The authorship matters: Aston-Jones (originator of the LC-NE adaptive gain theory) and Cohen (theory co-author) are co-authors on Kane 2017. These are the people most motivated to find a directional-bias component if one existed. They ran the cleanest available causal manipulation (DREADD), fit a formal model comparison, and reported noise-best-explanation. The follow-up to their own 2005 theory disambiguates the noise-vs-direction question in favour of noise.

The 2005 paper itself (Aston-Jones & Cohen 2005, PMID 16022602) is consistent with both readings at the conceptual level (the dual-mode framework can be interpreted as either noise-driven exploration or direction-driven exploration); the empirical resolution Kane 2017 supplied was not in the 2005 framework. The same paper is therefore an entry against ARC-065 (LC-NE tonic noise reading, mapping to MECH-313, confidence 0.84) and a separate entry against ARC-066 (LC-NE tonic direction reading, mapping to ARC-066, confidence 0.62 mixed-direction). The downgrade from 0.84 to 0.62 reflects the empirical disambiguation.

The implication for ARC-066 is substantive but does NOT trigger a slot split. The architectural function ARC-066 names (capacity-keyed positive bias toward action over no-op, target-free) is real and well-supported by the DA-vigor cluster; the substrate attribution to LC-NE is wrong and must be corrected. The slot stays; its biology anchor cluster gets reframed.

The R2 verdict therefore explicitly answers the briefing's pre-specified question "if R2 verdict is two distinct mechanisms recommend slot split": NO, R2 verdict is ONE LC-NE mechanism (noise), and the second function the briefing speculated about (LC-NE direction) does not exist as a separate substrate. ARC-066 is its own slot with its own substrate (DA-vigor), distinct from MECH-313 (LC-NE noise) for orthogonal reasons.

---

## R3 -- Implementation shape: additive bias vs multiplicative gain vs policy target-state

### Verdict: ADDITIVE E3 score bias on action vs no-op trajectories (primary recommendation). Multiplicative gain is the falsifiable secondary alternative. Policy-target-state and other alternatives are not supported by current literature. Confidence 0.72.

The primary recommendation is grounded in Niv 2007's opportunity-cost derivation: the long-run average reward rate enters the cost-benefit equation as an additive cost on time-spent-passive, equivalently an additive bonus on time-spent-acting. The form is naturally additive in the formalism. Beierholm 2013's empirical RT data is consistent with this (and would also be consistent with multiplicative gain), so the empirical evidence does not selectively support additive over multiplicative.

The primary recommendation is therefore:

```
E3 score(action_trajectory) += vigor_scalar * action_proxy(trajectory)
E3 score(no_op_trajectory)  -= vigor_scalar * passive_proxy(trajectory)
```

with `vigor_scalar` = a slow EWMA over the realised E3-score-receipt stream (per R4 below) and `action_proxy` / `passive_proxy` distinguishing trajectories that involve commit-to-action from trajectories that hold position. The two terms are mathematically equivalent (signed scalar) but compose ARC-066 (positive on action) and ARC-068 (negative on passive) cleanly, leaving the open question of whether the slots collapse to one signed scalar or stay as two separate parameters during child-MECH design.

Falsifiable secondary alternative: MULTIPLICATIVE GAIN, where `vigor_scalar` multiplies E3 score-magnitude rather than adding. A parametric sweep on a child-MECH validation experiment can distinguish: under additive, the action-vs-no-op gap scales linearly with the scalar regardless of pre-existing action preference; under multiplicative, the gap scales differentially when the pre-existing preference is already strong. Both can be implemented; Niv 2007's formalism prefers additive but the empirical evidence does not exclude multiplicative.

Tertiary alternative (not recommended): policy target-state biasing, where ARC-066 enters via the action distribution's reference rather than its score. This conflates ARC-066 with goal-target machinery (MECH-216 / E2_goal) and would be hard to compose cleanly with z_goal-driven wanting. Reject.

The R3 verdict's confidence is moderate (0.72) because the additive-vs-multiplicative empirical disambiguation is open. The recommendation is to land additive as primary in the child MECH and queue a parametric-sweep validation experiment on a child-MECH ablation cell to test the multiplicative alternative. This is exactly the work the queue-experiment skill should produce as the first ARC-066 validation experiment.

---

## R4 -- Capacity scalar composition: what enters the vigor scalar?

### Verdict: SLOW EWMA over realised E3-score-receipt is the primary scalar. Internal-capacity proxies (energy reserve, drive integrator) enter as secondary modulators. Autonomic / cardiac substrate enters only weakly via downstream MECH-313, NOT directly into ARC-066. The pre-registered functional restatement ("high energy AND low recent prediction error AND low drive") is partially correct but mis-attributed. Confidence 0.65.

The user-registered ARC-066 slot text says the capacity scalar is "high energy AND low recent prediction error AND low drive" -- a composition over internal-state variables. The literature attribution is to "long-run average reward rate" -- a slow integrator over the realised reward / score stream, which is an environmental signal.

The two are correlated in normal conditions (a healthy agent in a good environment will have high reward rate), but they are mathematically distinct. The literature evidence (Niv 2007 formalism, Beierholm 2013 empirical test) is that the SCALAR is the reward history average, not the internal state composition.

The R4 verdict therefore is: the primary scalar should be the SLOW EWMA OVER REALISED E3-SCORE-RECEIPT (across-episode, multi-window), not the internal-state composite. Internal-state variables enter as SECONDARY MODULATORS:

- **Energy reserve:** when energy is below a threshold, the vigor scalar is gated DOWN (the agent should not act vigorously when energy-depleted; this is the homeostatic-priority side already covered by SD-012).
- **Drive integrator:** when drive is high, the vigor scalar may be gated DOWN (the agent should commit to z_goal pursuit, not engage in target-free action). This is consistent with the SD-012 / SD-037 deficit-corner attribution.
- **Recent prediction error:** when PE is high, the vigor scalar may be gated DOWN (the agent should attend / consolidate / sleep, not act vigorously). This connects to MECH-104 (volatility surprise) and the sleep-cluster MECH-272/273/274.

The autonomic / cardiac substrate (ARC-058 affective-PE) does NOT enter the ARC-066 scalar directly. The autonomic substrate's downstream into LC-NE is the noise channel (MECH-313), per R2. ARC-066's substrate is mesolimbic DA, not autonomic-routed LC-NE.

The R4 verdict confidence is the lowest of the four (0.65) because the literature does not directly settle the SECONDARY-MODULATOR composition; it settles only the primary scalar. The recommendation is to land the primary scalar in the first child MECH and design the secondary modulators in a follow-on iteration after the primary scalar's behaviour is observed in baseline experiments.

The functional_restatement of ARC-066 in claims.yaml therefore needs a small update: the capacity scalar should be described as "long-window EWMA over realised E3-score-receipt (primary); modulated by energy reserve, drive integrator, and recent PE (secondary)". This is a refinement of the slot's pre-registered description, not a slot-revision (the architectural function is unchanged; the scalar attribution is corrected).

---

## What this pull does NOT settle

Items deferred to subsequent pulls or future sessions:

1. **ARC-067 idle-aversion / boredom and ARC-068 opportunity-cost no-op penalty pulls.** Both are companion slots in the non_deficit_action_drives family. ARC-067 likely lands a separable substrate (engagement-failure / clinical anhedonia / chronic-stress HPA); ARC-068 may collapse partially with ARC-066 as opposite ends of the same signed scalar (per the family doc's note). Pull commissioning: ARC-067 next, ARC-068 third (since ARC-068's substrate-distinctness depends on ARC-066's child mechanism shape).
2. **Whether ARC-066 and ARC-068 collapse to one signed scalar at the child-MECH level.** R3 verdict states this is open; the family doc already noted the collapse possibility. Resolution requires the ARC-068 lit-pull and a queue-experiment skill design pass.
3. **Tonic-vs-phasic DA isolation in human pharmacology.** Beierholm 2013 cannot cleanly isolate tonic from phasic DA effects. A future pull on selective tonic-DA pharmacology (e.g. low-dose D2 autoreceptor literature) might tighten the substrate attribution.
4. **Multi-modular LC literature.** Recent work (Schwarz 2015, Totah 2018, Chandler 2019, Poe 2020) has refined the dual-mode framework with spatial / temporal heterogeneity. This affects MECH-313's substrate attribution more than ARC-066's, but a future MECH-313-revision pull should examine whether modular LC organisation introduces a directional component the Kane 2017 DREADD design missed.
5. **Vigor-of-execution timing axis.** Niv 2007 also covers response latency / execution speed. ARC-066 explicitly excludes vigor-of-execution from current scope. A future MECH/Q-claim may extend the slot to the timing axis (likely as a child-MECH on the same scalar).
6. **Validation experiment design for ARC-066's primary child MECH.** The queue-experiment skill should produce a discriminative-pair experiment with arms: (ARM_0) ARC-066 OFF baseline, (ARM_1) ARC-066 ADDITIVE primary, (ARM_2) ARC-066 MULTIPLICATIVE secondary, in a well-fed-safe-familiar environment with no z_goal active. Predicted result: ARM_0 = inert (action density at MECH-313 noise floor); ARM_1 and ARM_2 = action density rises monotonically with the vigor scalar; ARM_1 vs ARM_2 differ on the action-preference scaling pattern (parametric sweep on a pre-existing action preference).

---

## Recommended next actions

1. **Update the ARC-066 evidence_quality_note in claims.yaml** to reference this synthesis with the lit_conf computed below, and to flag the R2 substrate-attribution reframe (LC-NE-direction rejected; mesolimbic DA-vigor load-bearing). The functional_restatement update is a smaller follow-up; stash for the child-MECH design session.
2. **Update the family doc** (`docs/architecture/non_deficit_action_drives.md`) ARC-066 anchor cluster: remove Aston-Jones & Cohen 2005 from the primary anchor list; add a "what ARC-066 is NOT" section explicitly referencing Kane 2017 as the disambiguation that the LC-NE substrate is noise-only (= MECH-313). Keep Niv 2007, Salamone & Correa 2012, Beierholm 2013, Walton 2003, Depue & Collins 1999 as the primary anchor cluster, with the substrate attribution corrected to mesolimbic DA-vigor + BAS abstract.
3. **Commission the ARC-067 lit-pull** (idle-aversion / boredom). The substrate is likely separable (clinical anhedonia / abulia / engagement-failure literature) and the slot's resolution is independent of ARC-066's.
4. **Defer the ARC-068 lit-pull** until ARC-067 is settled. ARC-068's substrate-distinctness depends on whether the ARC-066 child mechanism collapses with ARC-068 at design time.
5. **Queue the first ARC-066 validation experiment** (additive vs multiplicative discriminative pair) once R3 is confirmed via child-MECH design pass. The queue-experiment skill should produce the script + queue entry.

---

## Per-paper summary index

| Entry | DOI | Verdict it informs | Direction | Confidence |
|---|---|---|---|---|
| Niv et al. 2007 | [10.1007/s00213-006-0502-4](https://doi.org/10.1007/s00213-006-0502-4) | R1 substrate, R3 form, R4 scalar | supports | 0.83 |
| Kane et al. 2017 | [10.3758/s13415-017-0531-y](https://doi.org/10.3758/s13415-017-0531-y) | R2 (load-bearing) | weakens | 0.82 |
| Salamone & Correa 2012 | [10.1016/j.neuron.2012.10.021](https://doi.org/10.1016/j.neuron.2012.10.021) | R1 substrate identity | supports | 0.80 |
| Aston-Jones & Cohen 2005 | [10.1146/annurev.neuro.28.061604.135709](https://doi.org/10.1146/annurev.neuro.28.061604.135709) | R2 (theoretical anchor, downgraded) | mixed | 0.62 |
| Beierholm et al. 2013 | [10.1038/npp.2013.48](https://doi.org/10.1038/npp.2013.48) | R1 causal test, R3, R4 | supports | 0.79 |
| Walton et al. 2003 | [10.1523/JNEUROSCI.23-16-06475.2003](https://doi.org/10.1523/JNEUROSCI.23-16-06475.2003) | R2 boundary anchor | mixed | 0.65 |
| Depue & Collins 1999 | [10.1017/S0140525X99002046](https://doi.org/10.1017/S0140525X99002046) | R1 abstract-level commitment | supports | 0.66 |

**Aggregate ARC-066 lit_conf:** expected to land in the 0.72-0.76 range, supports-direction net (5 supports + 2 mixed; load-bearing supports cluster Niv / Salamone / Beierholm averaging 0.81, balanced against the mixed downgrade on Aston-Jones / Walton). The R2 weakens-entry on Kane 2017 (the LC-NE attribution) is conf 0.82 weakens but applies specifically to the rejected LC-NE-substrate sub-hypothesis, not to the architectural commitment ARC-066 names. The aggregate framing is "supports the architectural function with strong substrate attribution to mesolimbic DA-vigor; rejects the pre-registered LC-NE-direction substrate".

According to PubMed, all entries in this synthesis are sourced from PubMed-indexed literature with DOIs and PMIDs as cited above.
