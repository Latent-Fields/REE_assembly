---
nav_exclude: true
---

# Medications, Sleep Architecture, and Dementia Risk

**Related claims:** INV-048, MECH-173, MECH-174, MECH-175, MECH-176, MECH-177, Q-031, Q-032, IMPL-026
**Depends on:** INV-045, INV-046, INV-047, MECH-120, MECH-121, MECH-122, MECH-123, MECH-168-172
**Registered:** 2026-04-05

---

## 1. The Equivalence Principle (INV-048)

The attribution pipeline (INV-045, INV-046) responds to phase fidelity, not to the mechanism that
disrupts it. Any pharmacological agent that disrupts sleep architecture -- by suppressing SWS depth,
fragmenting SWS continuity, or suppressing REM -- produces equivalent pipeline degradation to
behavioral sleep deprivation proportional to:
- which phase(s) are disrupted
- the depth of disruption
- the cumulative duration of exposure

This equivalence principle means that medication review is, computationally, a **pipeline audit**.
For each chronically prescribed medication that affects sleep, the relevant question is: which
pipeline phases does this agent suppress, by how much, and over how long?

### Pipeline Phase Notation (from INV-045)

| Phase | Substrate | Claims | Function |
|-------|-----------|--------|----------|
| Phase 0 | Circadian gating / sleep onset | -- | Blocks new input corruption during install |
| Phase 1 | SWS: slow-oscillation depth | MECH-120 | SHY synaptic homeostasis; flattens dominant attractors |
| Phase 2 | SWS: SWR replay sequences | MECH-121 | Schema installation; hip->cx schema consolidation |
| Phase 3 | NREM: spindle coordination | MECH-122 | Theta-gamma nesting; packages E1 for sleep direction |
| Phase 4 | REM | MECH-123 | Precision recalibration; resets decision thresholds |

---

## 2. Phase-Specific Pharmacological Disruption (MECH-173, MECH-174)

### REM Suppression -- Phase 4 Disruption (MECH-173)

MECH-123 precision recalibration is the most downstream pipeline phase. Because INV-047 shows
that Phase 4 fails first in natural neurodegeneration, pharmacological REM suppression selectively
targets the already-most-vulnerable phase.

**Clinical signature of Phase 4 selective failure:** overconfident contextual attributions
before overt memory loss -- the earliest MCI prodrome. An agent continues acting with high
confidence while the accuracy of contextual attributions degrades silently.

Key REM-suppressing medications:

| Medication class | Mechanism of REM suppression | Potency |
|---|---|---|
| Anticholinergics | Muscarinic blockade suppresses PGO wave generators and nucleus basalis | High |
| MAOIs | Monoamine excess acts on REM-off neurons | Very high (near abolition) |
| SSRIs/SNRIs | 5-HT2A excess suppresses REM (paroxetine most potent) | Moderate-high |
| TCAs | Combined anticholinergic + serotonergic | High |
| Benzodiazepines | Stage 2 enhancement at expense of REM% | Moderate |

### SWS Suppression -- Phase 1/2 Disruption (MECH-174)

GABA-A positive allosteric modulators (benzodiazepines and Z-drugs) produce sleep via global CNS
inhibition. This bypasses homeostatic pressure in two ways:
1. **SWS depth suppression:** slow-oscillation amplitude reduced (impairs MECH-120 attractor
   normalisation)
2. **SWS continuity disruption:** fragmented slow-wave episodes impair MECH-121 SWR-replay
   sequences that require sustained hippocampal-cortical coordination

**Z-drug nuance:** Z-drugs (zolpidem, zopiclone, zaleplon) preferentially bind alpha-1 GABA-A
subunits and enhance Stage 2 spindles (potentially partially preserving MECH-122). However, they
still reduce SWS homeostatic depth because sleep is produced pharmacologically rather than via
accumulated sleep pressure -- the homeostatic gradient is partially bypassed regardless.

**Clinical signature of Phase 1/2 selective failure:** new context learning impaired while
remote episodic retrieval relatively preserved; patient has trouble learning that a new doctor's
office is distinct from an old one, but remembers well-consolidated past events.

---

## 3. Anticholinergic Burden: Dual-Pathway Risk (MECH-175)

Anticholinergic medications are unusual in conferring dementia risk via two independent pathways:

### Pathway 1: Nocturnal REM Suppression

ACh (from nucleus basalis of Meynert projecting to cortex, and brainstem PGO wave generators) is
the primary neurochemical driver of REM. Muscarinic blockade directly suppresses PGO wave
initiation and maintenance, abolishing or fragmenting REM nightly. This degrades MECH-123
precision recalibration cumulatively across years of use.

### Pathway 2: Diurnal Cholinergic Deficit Mimicry

Alzheimer's disease is characterised by progressive basal forebrain cholinergic neuron loss
(nucleus basalis of Meynert). Anticholinergic medications produce an iatrogenic cholinergic
deficit during waking hours -- a pharmacological analog of the AD lesion itself -- independently
impairing attention, encoding, and cortical desynchronisation required for active learning.

### Prediction

Anticholinergic burden scores (ACB scale, Anticholinergic Risk Scale) should predict dementia
conversion better than total medication count because they capture both pathway contributions.
Mediation analysis can test whether anticholinergic burden -> dementia is partially mediated via
REM-suppression-years (nocturnal pathway) vs cumulative daytime dose (diurnal pathway) -- see Q-031.

**High-burden medication classes by indication:**

| Indication | High-burden | Lower-burden alternatives |
|---|---|---|
| Overactive bladder | Oxybutynin, solifenacin, tolterodine | Mirabegron (beta-3 agonist, CNS-neutral) |
| OTC antihistamine | Diphenhydramine, chlorphenamine | Loratadine, cetirizine (non-sedating) |
| Depression | Amitriptyline, clomipramine, paroxetine | Sertraline, escitalopram, mirtazapine |
| Antipsychotic | Chlorpromazine, clozapine, olanzapine | Risperidone, aripiprazole (lower ACh) |
| Insomnia | Diphenhydramine OTC | Melatonin-ER, ramelteon, suvorexant |

---

## 4. Architecture-Preserving vs. Architecture-Disrupting Sleep Aids (MECH-176)

### The Mechanistic Distinction

**GABAergic agents (problem):** Produce sleep via active CNS suppression. This bypasses
homeostatic sleep pressure, compressing the phase-specific machinery that depends on homeostatic
gradients to run correctly.

**Orexin antagonists (preferred):** Produce sleep by removing the wake-promoting orexin/hypocretin
signal from the lateral hypothalamus -- a permissive mechanism. The homeostatic sleep pressure
is now free to express itself without pharmacological competition with the sleep machinery.
NREM homeostasis runs on endogenous gradients; REM emerges from endogenous cholinergic-monoaminergic
cycling unimpeded by muscarinic blockade.

### PSG Evidence (MECH-176)

Head-to-head PSG comparisons show orexin antagonists maintain or increase REM% and do not suppress
SWS% below placebo, unlike zolpidem (SWS suppression) and temazepam (REM + SWS compression).
This makes orexin antagonists the preferred choice when a sleep aid is indicated in an older
adult at MCI risk.

---

## 5. Disease-Modifying Candidates and Predictions (MECH-177)

The MECH-171 vicious cycle (sleep disruption -> consolidation failure -> attribution failure ->
arousal -> further sleep disruption) is the amplification mechanism for dementia progression.
Pharmacological pipeline protection breaks this cycle upstream of irreversible neurodegeneration.

**Critical window:** early MCI (before schema scaffold destabilises) shows disproportionately
large treatment effects. Once context slots no longer exist (middle-stage AD), sleep restoration
cannot rebuild them.

**Relationship to amyloid-targeting drugs:** MECH-169 (glymphatic + pipeline complementarity)
predicts these are additive. Amyloid drugs clear substrate damage; pipeline-protecting sleep
aids preserve functional architecture. Combined intervention is predicted to outperform either
alone.

### Disease-Modifying Candidates

| Medication | Sleep mechanism | Pipeline phases protected | DPM evidence tier |
|---|---|---|---|
| Suvorexant / lemborexant | Orexin antagonism (MECH-176) | 1, 2, 3, 4 (all preserved) | Active MCI trials |
| Ramelteon / melatonin-ER | Circadian restoration | 0 + downstream | EU licensed over-65; MCI trials |
| Trazodone (25-100mg) | 5-HT2A antagonism -> SWS increase | 1, 2 (enhanced) | AD sleep RCTs (Cochrane 2020) |
| Gabapentin (low dose) | VGCC alpha-2-delta -> SWS increase | 1, 2 (enhanced) | Conditional (tolerance, fall risk) |
| Low-dose doxepin (3-6mg) | Selective H1; no ACh at this dose | 2/3 (continuity + spindles) | Architecture-neutral low end |

### MECH-170 Prediction for DPM Trials

Sleep architecture restoration in MCI should produce **dissociated** cognitive improvement
following the pipeline rebuild order:
1. First: improved confidence/precision calibration (subtle, needs sensitive testing)
2. Then: improved new episodic consolidation
3. Later: improved contextual semantic memory (only with sustained intervention before schema collapse)

This dissociation distinguishes pipeline-mediated benefit from:
- Diffuse cognitive enhancers (predict uniform improvement)
- Amyloid drugs (predict improvement proportional to amyloid load reduction)
- Sedative reduction (predict uniform improvement from less daytime sedation)

---

## 6. Open Questions

### Q-031 -- Nocturnal vs Diurnal Anticholinergic Risk

Does the anticholinergic burden-dementia association track cumulative REM suppression duration,
total anticholinergic dose, or both independently? PSG-linked prospective cohorts with mediation
analysis can distinguish. Clinical implication: whether switching to non-anticholinergic
alternatives (e.g., oxybutynin -> mirabegron) fully removes the risk, or whether additional
sleep architecture monitoring is required.

### Q-032 -- SWS/REM Ratio as Pharmacodynamic Biomarker

Does SWS/REM ratio on PSG predict dementia outcomes independent of total sleep time across
medication classes? If yes, this validates phase-specific pipeline damage as the causal
intermediate and provides a mechanism-targeted endpoint for DPM trials (rather than total
sleep time, which conflates pipeline fidelity with sedation).

---

## 7. Clinical Decision Framework

When prescribing sleep-affecting medications in patients aged 60+ or with MCI risk:

1. **Anticholinergics: deprescribe or switch whenever possible.** Dual-pathway risk (MECH-175)
   means every year of anticholinergic use may be contributing independently via both nocturnal
   and diurnal mechanisms. Priority switches: oxybutynin -> mirabegron; amitriptyline for sleep
   -> trazodone/melatonin-ER; diphenhydramine OTC -> melatonin.

2. **Benzodiazepines: taper and replace.** Both chronic use and the difficulty of tapering
   (rebound insomnia) must be managed, but the long-term pipeline benefit of cessation is
   significant. Replace with orexin antagonist or trazodone during taper if needed.

3. **Z-drugs: prefer orexin antagonists.** When a pharmacological sleep aid is necessary,
   orexin antagonists have superior pipeline preservation and should be first-line in older
   adults at cognitive risk (MECH-176).

4. **Antidepressants: prefer low-REM-burden agents.** Sertraline and escitalopram cause
   significantly less REM suppression than paroxetine, venlafaxine, or TCAs. Mirtazapine
   provides the additional benefit of SWS enhancement.

5. **Monitor with PSG when in doubt.** Q-032 predicts SWS% and REM% are the relevant
   biomarkers, not total sleep time. Insomnia that is resolved pharmacologically but with
   compressed SWS/REM may be leaving the pipeline unprotected.

---

## Pharmacological Predictions Registry

The drug-by-drug predictions in this document are mirrored as structured entries in
`evidence/planning/pharmacological_predictions.v1.json` (PHARM-007 through PHARM-014 for
the dementia/medications cluster; see PHARM-001 to PHARM-006 in
[`../psychiatric_failure_modes.md`](../psychiatric_failure_modes.md) for the orexin-axis
cluster). Each PHARM entry tags the claim IDs it depends on, the predicted polarity, the
dissociation pattern, and the falsification condition.

| PHARM ID | Intervention | Claim depends on | Polarity |
|----------|-------------|------------------|----------|
| PHARM-007 | anticholinergic burden | INV-046, INV-047, INV-048, MECH-173, MECH-175 | **negative** |
| PHARM-008 | mirabegron substitution | INV-048, MECH-175 | positive |
| PHARM-009 | BZD/Z-drug at hypnotic dose | INV-048, MECH-174 | **negative** (cf. PHARM-004 positive in catatonia) |
| PHARM-010 | DORA for MCI/dementia | INV-048, MECH-176, MECH-177 | positive (sibling of PHARM-001) |
| PHARM-011 | trazodone 25-100mg | INV-048, MECH-176, MECH-177 | positive |
| PHARM-012 | low-REM-burden antidepressants vs paroxetine/TCA/MAOI | INV-048, MECH-173, MECH-177 | mixed (class-dissociation) |
| PHARM-013 | ramelteon / melatonin-ER | INV-048, MECH-176, MECH-177 | positive |
| PHARM-014 | composite pipeline-rebuild dissociation | INV-047, INV-048, MECH-177 | architectural |

PHARM-001 and PHARM-010 are flagged as siblings (same DORA drug class, two phenotypes --
PTSD/hyperarousal vs MCI/dementia). A head-to-head subgroup analysis showing different
DORA response in the two phenotypes would be a strong falsification of the shared-axis
prediction.

Governance review of PHARM predictions against clinical literature is a separate cycle
from substrate-evidence governance and has not yet been instituted.

---

## See Also

- `offline_phases.md` -- sleep phase architecture, INV-045, SD-017
- `docs/claims/claims.yaml` -- full claim text for INV-048, MECH-173-177, Q-031/032, IMPL-026
- `evidence/planning/pharmacological_predictions.v1.json` -- structured PHARM registry
- `../psychiatric_failure_modes.md` -- PHARM-001 to PHARM-006 (orexin-axis cluster)
- `precision_recalibration.md` -- MECH-123 detail
- `reality_consolidation.md` -- MECH-121 detail
