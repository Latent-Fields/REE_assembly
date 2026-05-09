# Targeted review: VALENCE_EXCITEMENT as a 5th channel in SD-014's hippocampal valence vector

**Pulled:** 2026-05-08 (9 entries, SD-014 5th-channel question).
**Extended:** 2026-05-09 (5 additional entries tagged MECH-307, weekend lit-pull). Total: 14 entries.

**Target claim:** SD-014 (status `provisional` per current registry; SD-014 currently specifies a 4-component valence vector V = [VALENCE_WANTING, VALENCE_LIKING, VALENCE_HARM_DISCRIMINATIVE, VALENCE_SURPRISE] in RBFLayer + ResidueField).

**Architectural question:** is excitement a primitive affect channel architecturally distinct from VALENCE_WANTING + z_beta arousal modulation, or a derived state already covered by the existing substrate?

**Verdict (revised 2026-05-08, post-code-inspection): FIX EXISTING WIRING (MECH-307 conjunction architecture, registered candidate / v3_pending in claims.yaml).** Excitement and dread should emerge as derived states from a four-gap fix to existing channels (signed `VALENCE_SURPRISE` + MECH-216 `z_beta` coupling + anticipatory `VALENCE_LIKING` write + write-at-predicted-location), NOT as new VALENCE channels. The SD-014 6-channel amendment (`VALENCE_EXCITEMENT` + `VALENCE_DREAD` as discrete channels) is registered as the **FALLBACK** architecture if the conjunction-fix proves unreliable. Confidence aggregate **0.77** across 9 entries (8 supports / 1 mixed / 0 weakens).

> **Why the verdict was revised.** The original verdict ("REGISTER VALENCE_EXCITEMENT as 5th channel") was the right inference from the lit-pull but the wrong architectural conclusion. Code inspection of [`agent.py:3075-3077`](../../../ree-v3/ree_core/agent.py#L3075) and [`agent.py:3753-3757`](../../../ree-v3/ree_core/agent.py#L3753) showed that the V3 substrate has all the upstream pieces required to produce excitement as a derived conjunction (E1 PE, MECH-216 schema readout, z_beta arousal, MECH-216 → VALENCE_WANTING write) but lacks the wiring between them. Biology does not have a "VALENCE_EXCITEMENT neuron type" either — the NAcc-anticipation signal measured in Knutson 2001a is the anatomical convergence of DA RPE + hippocampal preplay + ANS arousal at one structure. Fixing the four wiring gaps (~40 lines, all backward-compatible behind config flags) is more biologically faithful and more parsimonious than adding new channels. The 9 entries below still anchor the verdict; they argue for representational adequacy of anticipatory positive/negative arousal, which the conjunction architecture provides without growing the residue field's valence buffer from `[K, 4]` to `[K, 6]`. Cross-references: [`anticipatory_affect_conjunction_vs_dual_channel.md`](../../docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md), `claims.yaml` MECH-307 entry.

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

8 supports, 1 mixed, 0 weakens. Mean confidence: 0.77 (original 2026-05-08 SD-014-tagged pull).

## 2026-05-09 extension: MECH-307-tagged entries

The 9 entries above all tag SD-014 (the 5th-channel question). After MECH-307 was registered as the FIRST-LINE conjunction-architecture proposal, the indexer surfaced MECH-307 as having literature_confidence=0.0 -- the existing entries argue for representational adequacy of anticipatory affect (which MECH-307 also provides) but were not tagged to the new claim. The 2026-05-09 weekend lit-pull added five entries tagged directly to MECH-307, each targeting a distinctive architectural prediction:

| Entry | Paper | Year | Direction | Confidence | Gap addressed |
|---|---|---|---|---|---|
| `mech307_lateral_habenula_negative_pe_matsumoto2007` | Matsumoto & Hikosaka, Nature | 2007 | supports | 0.88 | Gap 1 (signed VALENCE_SURPRISE) -- LHb is the anatomical substrate of negative PE; biology splits signed PE into two mirror-image populations rather than collapsing to magnitude |
| `mech307_hippocampal_preplay_goal_pfeiffer2013` | Pfeiffer & Foster, Nature | 2013 | supports | 0.86 | Gap 4 (write-at-predicted-location) -- hippocampal place-cell sequences depict future paths to remembered goals at memory-recall onset |
| `mech307_decision_point_forward_sweep_johnson2007` | Johnson & Redish, J Neurosci | 2007 | supports | 0.78 | Gap 4 / consumer-side -- CA3 ensembles sweep forward down each candidate path at decision points; biological precedent for the per-candidate conjunction-read in MECH295LikingBridge.compute_conjunction_score_bias() |
| `mech307_hippocampal_vta_loop_lisman2005` | Lisman & Grace, Neuron | 2005 | supports | 0.82 | Architectural framework -- biology implements memory-relevant function as a multi-stage loop with no dedicated channel; canonical precedent for the conjunction-as-loop reading |
| `mech307_pupil_arousal_disrupts_memory_lloyd2025` | Lloyd, Miletic & Nieuwenhuis, Cognition | 2025 | mixed | 0.62 | Gap 3 caveat -- high pupil-linked arousal during encoding can DISRUPT subsequent memory via decision-urgency; Gap-3 z_beta coupling cannot be implemented as monotonic raise, needs inverted-U or context gate |

MECH-307 lit-pull aggregate (2026-05-09 entries only): 4 supports + 1 mixed, mean confidence 0.79. The mixed entry (Lloyd et al. 2025) is included deliberately as a critical-direction balancing entry; without it the lit base would over-represent the supporting case for the conjunction architecture.

The combined synthesis (SD-014 9 + MECH-307 5 = 14 entries) supports both the FIRST-LINE conjunction architecture (MECH-307) and the FALLBACK 6-channel amendment (SD-014). The architectural choice between them remains empirical, to be adjudicated by V3-EXQ-540 (3-arm gap decomposition currently queued) and any successor that compares ARM_2_full_conjunction against ARM_3_alternative_5channel directly. The new MECH-307 entries also surface a substantive design constraint not visible in the 2026-05-08 pull: Gap 3 z_beta coupling must respect the Lloyd et al. inverted-U finding, either by clamping z_beta_increment at a moderate ceiling or by adding a context gate that distinguishes encoding-relevant from urgency-relevant arousal.

## Five-step argument for the verdict

**1. Excitement is neurally dissociable from wanting.** The Knutson 2001a foundational MID paper is the load-bearing single piece of evidence: NAcc activation during reward anticipation correlates with self-reported HAPPINESS at the cue, not with directional motivation amplitude. Punishment anticipation does not recruit NAcc (medial caudate does instead) — so the NAcc signature is positive-valence-selective, not arousal-general. This rules out the simplest collapse (excitement = z_beta_arousal × sign(VALENCE_WANTING)).

**2. Excitement is neurally dissociable from liking.** Knutson 2001b and 2003 show anticipation (ventral striatum / NAcc) and outcome (vmPFC) activate distinct regions in the same subjects on the same task. Excitement-anticipation is not the same as liking-receipt at the brain level. REE's existing VALENCE_LIKING write site (consummatory at goal contact) does not capture the anticipatory-positive-arousal write that VALENCE_EXCITEMENT would carry.

**3. Excitement has a distinct functional consequence: memory formation.** Adcock 2006 shows that anticipatory mesolimbic activation at encoding *predicts subsequent memory* 24 hours later. This is the most architecturally consequential entry in the pull because it ties VALENCE_EXCITEMENT to a concrete REE pipeline: input to MECH-205 surprise-gated replay write path → priority-weighting in MECH-285 SleepReplaySampler. Locations recorded with high anticipatory excitement get prioritised for sleep consolidation. This is exactly the pipeline EXQ-538 is designed to test.

**4. The 2D circumplex is the right representational geometry.** Posner 2009 establishes that valence and arousal are dissociable at the neural-network level. SD-014's current 4-component vector is one-dimensional in the valence-axis sense (positive: wanting, liking; negative: harm; reactive: surprise). The circumplex argues for at least a 2D representation. VALENCE_EXCITEMENT (high-arousal-positive) and VALENCE_DREAD (high-arousal-negative) bring SD-014 into alignment with the empirically supported 2D affect space.

**5. Symmetric architecture: dread is the negative analog.** Berns 2006 establishes dread as its own construct, dissociable from fear/anxiety and from harm-at-receipt. If REE registers VALENCE_EXCITEMENT, the symmetric architectural choice is to also register VALENCE_DREAD. The clinical literature (depression: Knutson 2008; bipolar: Johnson 2019) further supports the channel-separability principle by showing how each channel can be selectively altered in pathology.

## Counter-reading and why it partially survives

The Bromberg-Martin 2010 review offered the original counter-reading: excitement is the salience-coding signal, captured by z_beta arousal modulation alone (MECH-093 already exists for heartbeat-rate gating). The original SYNTHESIS rejected this on two grounds:

- **Empirical**: Knutson 2001a's NAcc-anticipation is positive-valence-selective, not pure salience. Punishment anticipation activates a different region. So the human-fMRI excitement signature is value-coded, not salience-coded — the salience-only route is the wrong route for what humans report as excitement.
- **Architectural**: z_beta in REE modulates timing (heartbeat rate), not representation. Capturing excitement via z_beta alone would still require consumer-side joint reads with VALENCE_WANTING.

Both critiques are still valid. But the **revised verdict (MECH-307 conjunction)** preserves the spirit of the counter-reading — excitement composes from existing pieces — while fixing the empirical problem (the conjunction is *signed-positive PE × MECH-216 schema × z_beta × predicted-location* — value-selective, not pure salience) and the architectural problem (consumers can read a single conjunction predicate, hidden behind a small helper, rather than every consumer hand-rolling joint reads). The four wiring gaps (G1 signed `VALENCE_SURPRISE`, G2 MECH-216 multi-channel write, G3 z_beta path, G4 write-at-predicted-location) are the *missing scaffolding* the original counter-reading needed to be true. They are now registered as MECH-307.

## SD-014 amendment text (FALLBACK -- moved to architecture doc 2026-05-08)

The full SD-014 6-channel amendment proposal text is retained as the FALLBACK
architecture and now lives in
[`docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md`](../../docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md)
under "SD-014 amendment proposal text (FALLBACK)". It is referenced from SD-014's
`evidence_quality_note` in `claims.yaml` and is not yet applied to the registry; the
empirical 4-arm experiment (described below in "Falsification design") adjudicates
between MECH-307 (first-line) and the SD-014 amendment (fallback). Original text
preserved below for the SYNTHESIS audit trail:

## Original (now FALLBACK) SD-014 amendment text

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

## Recommended next step (revised 2026-05-08)

1. **MECH-307 `anticipatory_affect_conjunction` -- REGISTERED 2026-05-08** (claims.yaml,
   `candidate / v3_pending`). Asserts excitement and dread emerge as derived states from
   the four-gap wiring fix. Lit anchors from this directory; cross-tags MECH-111 because
   the same wiring gaps likely substrate-confounded EXQ-141. ~40 lines of code, all
   backward-compatible.

2. **SD-014 amendment to 6-component valence vector -- PROPOSED, NOT APPLIED.** Full
   amendment text recorded in [`docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md`](../../docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md)
   and cross-referenced in SD-014's `evidence_quality_note`. Will be applied to the
   registry only if the MECH-307 conjunction-fix experiment fails C3 (the parsimony
   head-to-head against ARM_3_5channel).

3. **Sequencing** (unchanged): hold the discriminative experiment until **EXQ-537** (SD-029
   single-pass comparator) and **EXQ-141b** (MECH-111 curiosity drive retest on corrected
   commit-chain substrate) clear. The MECH-307 4-arm + SD-014-amendment alternative
   experiment is queued behind both. User confirmation required before queue insertion.

## Confidence verdict

Aggregate literature confidence: 0.77 across 9 entries. Above the 0.6 design-proceed floor.
Below the ~0.95 ceiling for lit-only promotion. The right zone for a pre-registered V3
substrate amendment (now via MECH-307 conjunction architecture) with a paired falsification
experiment.

The verdict revision (REGISTER-CHANNEL → FIX-WIRING) does not change the lit confidence — the
9 entries support either architecture as long as the construct (anticipatory positive arousal
distinct from wanting + liking + arousal alone) is represented somewhere in the substrate. The
revision is an *architectural* preference for parsimony, biological fidelity, and avoiding
papering-over-of-wiring-gaps with new representational primitives — informed by code
inspection and the prior architectural pattern (MECH-111 + ghost-projection / MECH-188 vs
MECH-295 dual-path) where fixing existing machinery has consistently been more correct than
adding new layers.
