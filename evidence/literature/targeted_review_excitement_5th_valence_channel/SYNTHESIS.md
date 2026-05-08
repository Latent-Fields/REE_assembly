# Targeted review: VALENCE_EXCITEMENT as a 5th channel in SD-014's hippocampal valence vector

**Pulled:** 2026-05-08. 9 entries.

**Target claim:** SD-014 (status `provisional` per current registry; SD-014 currently specifies a 4-component valence vector V = [VALENCE_WANTING, VALENCE_LIKING, VALENCE_HARM_DISCRIMINATIVE, VALENCE_SURPRISE] in RBFLayer + ResidueField).

**Architectural question:** is excitement a primitive affect channel architecturally distinct from VALENCE_WANTING + z_beta arousal modulation, or a derived state already covered by the existing substrate?

**Verdict: REGISTER** VALENCE_EXCITEMENT as a 5th channel in SD-014, **with VALENCE_DREAD as a 6th channel** for symmetric anticipatory affect representation. Confidence aggregate **0.78** across 9 entries (8 supports / 1 mixed / 0 weakens).

## Entries

| Entry | Paper | Year | Direction | Confidence | Key contribution |
|---|---|---|---|---|---|
| `knutson_mid_foundational_knutson2001a` | Knutson, Adams, Fong & Hommer, J Neurosci | 2001 | supports | 0.85 | NAcc anticipation correlates with self-reported HAPPINESS at reward cues; selectively positive-valence-coded (no NAcc response to punishment anticipation -- medial caudate instead). The construct anchor for excitement-as-distinct-from-wanting. |
| `anticipation_outcome_dissociation_knutson2001b` | Knutson, Fong, Adams, Varner & Hommer, NeuroReport | 2001 | supports | 0.78 | Anticipation (ventral striatum / NAcc) and outcome (vmPFC) recruit anatomically distinct regions. Direct dissociation of excitement-anticipation from liking-receipt. |
| `da_value_vs_salience_brombergmartin2010` | Bromberg-Martin, Matsumoto & Hikosaka, Neuron | 2010 | mixed | 0.74 | DA neurons split into VALUE-coding (reward-preferring) vs SALIENCE-coding (orienting). Mixed direction: supports multi-channel anticipatory affect, but offers an architectural alternative (excitement as salience modulation rather than its own value channel). |
| `tonic_phasic_anticipation_brombergmartin2010b` | Bromberg-Martin, Matsumoto & Hikosaka, Neuron | 2010 | supports | 0.80 | Macaque single-unit: tonic anticipatory signal (reward-preferring) vs phasic anticipatory signal (reward+punishment) coexist within same neurons. Direct neurophysiological evidence for multi-channel anticipatory affect. |
| `anticipation_memory_adcock2006` | Adcock, Thangavel, Whitfield-Gabrieli, Knutson & Gabrieli, Neuron | 2006 | supports | 0.82 | NAcc-VTA-hippocampus anticipatory activation predicts memory formation 24h later. Functional consequence of anticipatory positive arousal: schema/memory etching. Cross-tags SD-017 (sleep consolidation pipeline). |
| `dread_neural_substrates_berns2006` | Berns, Chappelow, Cekic, Zink, Pagnoni & Martin-Skurski, Science | 2006 | supports | 0.78 | Dread is dissociable from fear/anxiety; mediated by attention to expected physical response in posterior cortical pain matrix. Symmetric negative analog of excitement; supports adding VALENCE_DREAD as 6th channel. |
| `circumplex_valence_arousal_posner2009` | Posner, Russell, Gerber et al., Hum Brain Mapp | 2009 | supports | 0.72 | Two distinct neural networks subserve valence (insula, lateral PFC) and arousal (parahippocampus, dACC). The two-dimensional circumplex is reflected at the neural level; representational adequacy for affect requires both dimensions. |
| `depression_anticipation_dissociation_knutson2008` | Knutson, Bhanji, Cooney, Atlas & Gotlib, Biol Psychiatry | 2008 | supports | 0.72 | Unmedicated MDD: NAcc anticipation INTACT, outcome discrimination reduced, ACC-anticipation altered. Clinical dissociation: excitement (NAcc-anticipation) is selectively preservable while related affect channels are disrupted. |
| `bipolar_blunted_anticipation_johnson2019` | Johnson, Mehta, Ketter, Gotlib & Knutson, NeuroImage Clin | 2019 | supports | 0.74 | Remitted bipolar I: NAcc anticipation BLUNTED, mediated by Positive Urgency. Bipolar mania is the clearest phenomenological case of pathological excitement; the construct maps onto a measurable neural signature. |

## Aggregate direction

8 supports, 1 mixed, 0 weakens. Mean confidence: 0.77.

## Five-step argument for the verdict

**1. Excitement is neurally dissociable from wanting.** The Knutson 2001a foundational MID paper is the load-bearing single piece of evidence: NAcc activation during reward anticipation correlates with self-reported HAPPINESS at the cue, not with directional motivation amplitude. Punishment anticipation does not recruit NAcc (medial caudate does instead) — so the NAcc signature is positive-valence-selective, not arousal-general. This rules out the simplest collapse (excitement = z_beta_arousal × sign(VALENCE_WANTING)).

**2. Excitement is neurally dissociable from liking.** Knutson 2001b and 2003 show anticipation (ventral striatum / NAcc) and outcome (vmPFC) activate distinct regions in the same subjects on the same task. Excitement-anticipation is not the same as liking-receipt at the brain level. REE's existing VALENCE_LIKING write site (consummatory at goal contact) does not capture the anticipatory-positive-arousal write that VALENCE_EXCITEMENT would carry.

**3. Excitement has a distinct functional consequence: memory formation.** Adcock 2006 shows that anticipatory mesolimbic activation at encoding *predicts subsequent memory* 24 hours later. This is the most architecturally consequential entry in the pull because it ties VALENCE_EXCITEMENT to a concrete REE pipeline: input to MECH-205 surprise-gated replay write path → priority-weighting in MECH-285 SleepReplaySampler. Locations recorded with high anticipatory excitement get prioritised for sleep consolidation. This is exactly the pipeline EXQ-538 is designed to test.

**4. The 2D circumplex is the right representational geometry.** Posner 2009 establishes that valence and arousal are dissociable at the neural-network level. SD-014's current 4-component vector is one-dimensional in the valence-axis sense (positive: wanting, liking; negative: harm; reactive: surprise). The circumplex argues for at least a 2D representation. VALENCE_EXCITEMENT (high-arousal-positive) and VALENCE_DREAD (high-arousal-negative) bring SD-014 into alignment with the empirically supported 2D affect space.

**5. Symmetric architecture: dread is the negative analog.** Berns 2006 establishes dread as its own construct, dissociable from fear/anxiety and from harm-at-receipt. If REE registers VALENCE_EXCITEMENT, the symmetric architectural choice is to also register VALENCE_DREAD. The clinical literature (depression: Knutson 2008; bipolar: Johnson 2019) further supports the channel-separability principle by showing how each channel can be selectively altered in pathology.

## Counter-reading and why it loses

The Bromberg-Martin 2010 review offers the architectural alternative: excitement is the salience-coding signal, captured by z_beta arousal modulation (MECH-093 already exists for heartbeat-rate gating). This reading would let REE avoid adding new channels. Two reasons it loses:

- **Empirical**: Knutson 2001a's NAcc-anticipation is positive-valence-selective, not pure salience. Punishment anticipation activates a different region. So the human-fMRI excitement signature is value-coded, not salience-coded — the Bromberg-Martin salience route is the wrong route for what humans report as excitement.
- **Architectural**: z_beta in REE modulates timing (heartbeat rate), not representation. To capture excitement via z_beta + VALENCE_WANTING joint reads at consumer sites, every consumer (MECH-205 replay write, MECH-292 ghost-priority, etc.) would need to know to do the joint read. That is dispersed and error-prone. A dedicated channel writes once and consumers read directly.

## Recommended SD-014 amendment text

```
SD-014 — Hippocampal Valence Vector Node Recording (amendment 2026-05-XX)

Status: provisional -> provisional (amendment, no quadrant change pending evidence)
Implementation phase: v3
v3_pending: true (substrate amendment + behavioural validation needed)

Amendment: V is extended from 4-component to 6-component:
  V = [VALENCE_WANTING, VALENCE_LIKING, VALENCE_HARM_DISCRIMINATIVE,
       VALENCE_SURPRISE, VALENCE_EXCITEMENT, VALENCE_DREAD]

VALENCE_EXCITEMENT (index 4): high-arousal-positive anticipatory affect.
Write site: cue-stage anticipatory write, gated by predicted-imminent-positive-
event. Write magnitude proportional to (drive_level x predicted_goal_proximity x
prediction_certainty), gated by z_beta arousal level (excitement is high-arousal,
not low-arousal).

VALENCE_DREAD (index 5): high-arousal-negative anticipatory affect.
Symmetric to VALENCE_EXCITEMENT; written at cue-stage when MECH-216 schema readout
predicts imminent harm with low controllability/safety prediction.

Functional consumers:
  - MECH-205 surprise-gated replay write: priority-weighted by VALENCE_EXCITEMENT
    + VALENCE_DREAD (anticipatory affect drives consolidation).
  - MECH-292 ghost-priority: ghost_priority += w_e * anticipated_excitement(r)
    - w_d * anticipated_dread(r) (modulates ghost-goal selection).
  - MECH-279 PAG freeze gate: VALENCE_DREAD as input (already partially captured
    by z_harm_a but the anticipatory cue-stage signal is currently absent).

Lit anchors: Knutson 2001a [DOI](https://doi.org/10.1523/JNEUROSCI.21-16-j0002.2001),
Knutson 2001b [DOI](https://doi.org/10.1097/00001756-200112040-00016),
Adcock 2006 [DOI](https://doi.org/10.1016/j.neuron.2006.03.036),
Bromberg-Martin 2010 [DOI](https://doi.org/10.1016/j.neuron.2010.06.016),
Berns 2006 [DOI](https://doi.org/10.1126/science.1123721),
Posner 2009 [DOI](https://doi.org/10.1002/hbm.20553).
```

## Implementation cost estimate

Cheap. The change is a single-axis expansion of the residue field's valence buffer from K x 4 to K x 6, plus two new write sites in REEAgent (one in sense() / update_z_goal() for VALENCE_EXCITEMENT, one in the harm-prediction pathway for VALENCE_DREAD), plus updates to MECH-205 and MECH-292 to consume the new channels. ~50-100 lines of code; backward compatible with valence_enabled=False default.

## Falsification design

If registered, the falsifying experiment would be a 4-arm ablation over (excitement_channel ON/OFF) x (dread_channel ON/OFF), measuring (a) memory-formation pickup at high-excitement-coded locations during sleep replay (Adcock prediction), (b) ghost-goal selection bias toward excitement-coded over staleness-coded locations (MECH-292 prediction), (c) avoidance behaviour amplitude at dread-coded locations (Berns prediction). Pre-register Adcock's effect size as the C1 acceptance criterion: high-excitement locations should show >= 1.5x replay frequency in MECH-285 SleepReplaySampler vs uniform-priority baseline. ~3-4h runtime on Mac.

## Open lit gaps

The cleanest direct test of the value-vs-salience question for excitement (lesion or pharmacological isolation of NAcc-anticipation while measuring tonic-phasic dissociation) does not exist as a single paper in our pull. The Bromberg-Martin 2010b tonic/phasic dissociation is the closest, but it does not include a behavioural anchor for human-style "excitement" (which is necessarily self-reported). This is the load-bearing literature gap. Tag as **LIT-PULL-PENDING-EXCITEMENT-CAUSAL-INTERVENTION** for a future, more focused pull.

A second gap: the Russell circumplex 2D framework is well-established but the *specific neural mapping of high-arousal-positive vs low-arousal-positive* is less consolidated than the 2D principle itself. Whether VALENCE_EXCITEMENT and a hypothetical VALENCE_CONTENTMENT (low-arousal-positive) would also need separation depends on whether REE wants the full 4-quadrant circumplex or just the high-arousal axis added to its existing valence-axis representation.

## Recommended next step

1. **Register MECH-XX (proposed: MECH-307 anticipatory_affect_dual_channel)** as a candidate mechanism_hypothesis with implementation_phase=v3, v3_pending=true. Its content: SD-014 should be extended to a 6-component valence vector to represent high-arousal anticipatory affect (positive: VALENCE_EXCITEMENT; negative: VALENCE_DREAD) as separable from VALENCE_WANTING (directional motivation) and VALENCE_LIKING (consummatory hedonic).

2. **Hold SD-014 amendment** pending the EXQ-141b retest (MECH-111 curiosity drive on corrected commit-chain substrate) so we don't add channels to a substrate that is currently buggy in known ways. The EXQ-141b plus an EXQ-XXX excitement-channel falsification could be designed as a paired experiment.

3. **Engage Daniel** before claim registration. The architectural decision -- 6 channels vs 4 channels in SD-014 -- is significant enough that user signoff before registry edit is the right governance move.

## Confidence verdict

Aggregate literature confidence: 0.77 across 9 entries. Above the 0.6 design-proceed floor. Below the ~0.95 ceiling for lit-only promotion. The right zone for a pre-registered V3 substrate amendment with a paired falsification experiment.
