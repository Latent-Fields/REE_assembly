---
nav_exclude: true
---

# Receptor-Subtype + Interaction-Effects Layer (model <-> intervention)

**Created:** 2026-06-12
**Status:** working abstraction layer (not a claim cluster; no claims.yaml entries created here)
**Depends on (reads):** MECH-083..088 (four-plane neuromodulatory model), MECH-006/048/085, ARC-005,
psychiatric_failure_modes.md, psychiatric_failure_axes.md (ARC-086)
**Feeds:** `evidence/planning/pharmacological_predictions.v1.json` (PHARM-015..PHARM-022 + PHARM-001/010 orexin retrofit)

> **HONESTY RAIL (read first).** REE is a research-stage computational specification, not a
> deployed AI, not a validated disease model, and not a clinical decision tool. Everything below
> is a set of **testable hypotheses and shared vocabulary**, not treatment guidance. The
> repurposing candidates named here are *predictions to be adjudicated against clinical
> literature* (RCTs, naturalistic cohorts), exactly like the rest of the PHARM registry. No
> patient should be treated on the basis of this document. Receptor pharmacology is the place
> REE has historically been "philosophy-right / mechanism-wrong" (see
> `memory/feedback_biology_before_definitions`): elegance is not evidence.
>
> **This layer cannot produce treatment evidence — only treatment-research directions.** REE is
> never a link in the evidence chain. What it does is *nominate which existing-drug trial is worth
> running* and state the falsification condition in advance, so the trial is informative either way.
> The evidence — if it ever exists — is the trial's, not REE's. A receptor match plus a coherent
> mechanism story is a reason to *test*, never a reason to *prescribe* or to claim an effect. Every
> "predicted_effect" below is a hypothesis about what such a trial would find, not a finding.

---

## 1. Why this layer exists (the missing rung)

REE already has two mappings that sit on either side of a gap:

```
  REE mechanism claims              [drug-CLASS] PHARM registry
  (MECH-083..088 four planes,       (PHARM-001..014: DORA, SSRI,
   MECH-006/048/085, SD-036/037,     anticholinergic, GABAergic,
   psychiatric_failure_modes.md)     melatonergic, ...)
        |                                         ^
        |                                         |
        +------------- ??? -----------------------+
                  no receptor-resolution rung
```

The existing PHARM entries jump from a **mechanism** ("damp the SD-037 override signal") straight
to a **drug class** ("DORA"). That skips the rung where most modern psychiatric drug innovation —
and most *repurposing* opportunity — actually lives: **which receptor subtype, on which projection,
with which interaction effects.** Two drugs in the same coarse class (e.g. "serotonergic") can act
on opposite REE planes; one receptor (e.g. M4) can modulate a *different* plane than its parent
transmitter's headline role. The class label hides this.

This layer inserts that rung. It does three things the class layer cannot:

1. **Resolves an existing internal conflict by receptor subtype.** The MECH-006 vs MECH-085
   serotonin conflict (does 5-HT set temporal/rollout depth or not?) is flagged in
   `neuromodulatory_control_planes.md` with the receptor-subtype split named as the *pending*
   reconciliation. This document executes that reconciliation (Section 3A).
2. **Names interaction effects** (M1 plasticity-gain x M4 dopamine-selection; mu/kappa opposing
   commitment-entropy) that are invisible at transmitter granularity (Section 3).
3. **Surfaces approved-drug repurposing candidates** whose receptor profile matches a REE plane
   failure but whose *labelled indication* does not yet cover it — the highest-yield, lowest-cost-
   of-evidence interventions, especially for public health systems (Section 5).

---

## 2. The resolution table (subtype -> plane -> failure -> approved drug)

Each row reads: a receptor subtype, the REE plane/mechanism it carries, the failure signature when
it is mis-tuned, an **approved** drug whose receptor action matches, and that drug's current label
status. "Repurposing gap" = the REE-predicted indication is *not* the drug's current label.

| Receptor subtype (projection) | REE plane / mechanism | Failure signature | Approved drug (action) | Current label | Repurposing gap | PHARM |
|---|---|---|---|---|---|---|
| **5-HT2A** (dorsal raphe -> L5 cortical pyramidal) | Narrative-level representational collapse / exclusivity & top-level precision (MECH-006 rho-exclusivity; MECH-085 narrative level) | Aberrant high-level salience, "narrative lock" / delusion-like over-precision (IMPL-005 #3 high alpha_theta; MECH-088 psychosis) | **Pimavanserin** (5-HT2A inverse agonist) | Parkinson's disease psychosis (2016) | Adjunctive MDD, primary psychosis (trialled, not labelled) | PHARM-015 |
| **5-HT1A** (median raphe -> hippocampal CA1/DG; + somatodendritic autoreceptor) | Hippocampal-terrain basin geometry — aversive attractor wall steepness (MECH-085 terrain level) | Deep aversive basins, fear-consistent rollout capture (anxiety; MECH-088 PTSD terrain component) | **Buspirone** (5-HT1A partial agonist) | Generalised anxiety disorder | Augmentation in anhedonic/terrain-locked depression; PTSD terrain component | PHARM-016 |
| **M1** (cortical/hippocampal muscarinic) | ACh meta-plane: plasticity gain on bottom-up encoding (MECH-083) | Low plasticity-gain -> new-context encoding failure / confirmation bias; chronically high -> map instability | **Xanomeline**/trospium (M1/M4 agonist) | Schizophrenia (2024, Cobenfy) | MCI / AD cognition, AD psychosis (trialled, expanding) | PHARM-017 |
| **M4** (striatal muscarinic) | INTERACTION: dampens dopamine trajectory-selection gain (MECH-086) without D2 blockade | Aberrant salience / spurious attractor selection (MECH-088 psychosis selection arm) | **Xanomeline**/trospium (M1/M4 agonist) | Schizophrenia (2024) | First non-D2 antipsychotic — the receptor-resolved alternative to D2 antagonism | PHARM-017 |
| **mu-opioid** (mesolimbic/PAG) | Commitment stabiliser — reduces policy-competition entropy (MECH-048; opioid thought 2026-02-11) | Loss -> failure to consolidate selected commitments; excess -> rigid absorption | **Buprenorphine** (mu partial agonist) | Opioid dependence, pain | — (partial; see kappa row) | PHARM-018 |
| **kappa-opioid** (dynorphin system) | INTERACTION: commitment *destabiliser* — raises policy entropy, dysphoria/aversive state | Pathological elevation -> anhedonia, dysphoria, aversive-state lock, suicidality | **Buprenorphine** (kappa antagonist) | (not labelled for this) | Anti-anhedonic / anti-suicidal adjunct in TRD (trialled, not labelled) | PHARM-018 |
| **NMDA-R** (GluN2B; cortical pyramidal + fast-spiking GABAergic interneurons) | RAPID map-geometry remodelling / aversive-basin flattening — the fast analogue of MECH-077 psychedelic remapping; deforms MECH-076 terrain topology / MECH-085 basin depth on an hours timescale, distinct from the 2-4 week monoaminergic route | Rigid deep aversive basins resistant to slow monoaminergic remapping (treatment-resistant depression; acute suicidality) | **Esketamine** (NMDA antagonist) / ketamine | TRD + MDD with suicidal ideation (esketamine, 2019); racemic ketamine off-label | Racemic ketamine (off-label) for the same rapid-remodelling indication — the major repurposing story | PHARM-019 |
| **GABA-A alpha-2/3** (limbic / spinal interneurons) | Harm-stream cross-stream decay regulator (SD-036) — anxiolysis as restored decay of pinned harm streams, *without* alpha-1 sedation | Slowed harm-stream decay -> anxiety / harm-stream lock (catatonia subtype II, V3-EXQ-471) | **alpha-2/3-selective PAM** (MK-0777/TPA023; darigabat) | None approved (multiple Phase 2 GAD/panic; not converted) | Non-sedating anxiolytic / harm-stream decay — the receptor-resolved subunit that carries anxiolysis | PHARM-020 |
| **GABA-A alpha-1** (thalamocortical) | Sedation / sleep-onset plane — hypnotic drive that bypasses homeostatic sleep pressure and does NOT preserve SWS architecture (INV-048) | alpha-1 sedation substitutes for, rather than restores, SWS-dependent consolidation (dementia-pipeline cost, PHARM-009) | **Zolpidem** (alpha-1-preferring PAM) | Insomnia (approved) | — (dissociation control: alpha-1 = sedation, NOT the anxiolytic-decay plane) | PHARM-021 |
| **D2** (dorsal / associative striatum) | Trajectory-selection GAIN plane (MECH-086 headline) — which rollout wins, how fast | Excess -> premature commitment / aberrant salience; loss -> indecision | D2 antagonists / agonists (antipsychotics; ropinirole) | Schizophrenia / Parkinson's (approved) | — (headline selection arm, already labelled) | PHARM-022 |
| **D3** (ventral striatum / nucleus accumbens, limbic) | INTERACTION: anti-anhedonic incentive-salience arm of the selection plane (MECH-086) — reward-motivation weighting dissociable from D2 motor-selection gain | D3 hypofunction -> anhedonia / amotivation (depression reward arm; MECH-088 DA selection failure) | **Pramipexole** (D3-preferring agonist) | Parkinson's disease, restless legs (approved) | Anti-anhedonic augmentation in depression (trialled, not labelled) | PHARM-022 |
| **OX2R** (lateral-hypothalamic orexin -> TMN / LC / raphe wake drive) | SD-037 hyperarousal override / wake-promoting drive on the substrate (schema-repair-starvation plane) | Tonic over-drive -> hyperarousal insomnia, schema-repair starvation (SD-037) | **DORA** (suvorexant / lemborexant / daridorexant; OX2R-dominant for sleep) | Insomnia (approved) | — (cross-link: PHARM-001/010 now receptor-resolved at the OX1R/OX2R rung) | PHARM-001/010 |

---

## 3. Interaction effects (the part class-granularity hides)

### 3A. Serotonin: receptor subtype resolves the MECH-006 / MECH-085 conflict

`neuromodulatory_control_planes.md` carries an unresolved conflict: MECH-006 says serotonin does
**not** select temporal/rollout depth; MECH-085 says it does. The file names the resolution path —
"different raphe nuclei and receptor subtypes re-use the same motif at different hierarchical
levels" — but defers it pending a literature pull.

**Resolution (receptor-resolved):** the two claims describe the *same serotonergic motif*
(modulating resolution pressure / exclusivity) applied at two levels by two receptor populations:

- **5-HT2A on cortical L5 pyramidal cells (dorsal raphe)** carries MECH-006's account: narrative-/
  cognitive-level representational exclusivity and top-level precision. 5-HT2A *agonism* loosens
  high-level priors (the psychedelic remapping of MECH-077); 5-HT2A *inverse agonism* (pimavanserin)
  tightens aberrant high-level salience. This is the "global tau at the E-stack level" that
  MECH-006 correctly says serotonin does not set — 5-HT2A modulates *exclusivity*, not depth.
- **5-HT1A on hippocampal CA1/DG (median raphe)** carries MECH-085's terrain account: aversive
  attractor basin depth and local rollout geometry. This is "hippocampal-terrain-level depth," a
  different construct from global tau.

So MECH-006's prohibition ("does NOT select temporal depth tau") and MECH-085's rollout-depth claim
are **both correct at their own receptor/level** — the apparent conflict was a granularity artefact.
This is a concrete worked example of why the receptor rung is load-bearing: without it, the two
claims look contradictory; with it, they are complementary.

### 3B. Muscarinic: M1 (plasticity) x M4 (dopamine selection) — one drug, two planes

Xanomeline is an M1/M4 agonist. The REE-relevant point is that its two targets sit on **two
different planes** of MECH-087's hierarchy:

- **M1** acts on the ACh meta-plane (MECH-083) — plasticity gain on encoding.
- **M4** acts *downstream*, dampening dopamine trajectory-selection gain (MECH-086) — this is why
  xanomeline is antipsychotic **without D2 blockade**. It attacks MECH-088's psychosis "selection"
  arm (dopamine stamping salience onto noise) from the muscarinic side rather than the D2 side.

This is the clearest interaction-effect example: a single molecule whose therapeutic action is the
*joint* effect of an upstream-plane action (M1) and a downstream-plane action (M4). The class label
"muscarinic agonist" tells you neither plane.

### 3C. Opioid: mu / kappa as opposing poles on the commitment-entropy axis

The opioid thought (2026-02-11, processed into MECH-048) frames mu-opioid as a **commitment
stabiliser** that reduces internal policy competition — "reduced urge to switch." Its mirror is the
kappa/dynorphin system, which *raises* policy entropy and carries dysphoric/aversive state. REE
reads anhedonic, dysphoric, aversive-state-locked depression as **pathological kappa-driven
commitment destabilisation** (nothing holds; the aversive attractor wins by default).

Buprenorphine is a **mu partial agonist + kappa antagonist**. The kappa antagonism is the
architecturally interesting arm: it should normalise pathologically elevated policy-destabilisation,
predicting an anti-anhedonic / anti-suicidal effect distinct from monoaminergic antidepressants
(which act on the serotonin terrain and dopamine selection planes, not the opioid commitment-entropy
axis). The MDD trial record (Section 5) is consistent with this.

### 3D. NMDA / glutamate: rapid map-geometry remodelling on a different timescale

The serotonin terrain account (MECH-085) and the structural-deformation account (MECH-076) both make
map-geometry change *slow* — the 2-4 week SSRI onset is, in REE terms, the time it takes to re-grade a
basin via reconsolidation cycles. MECH-077 already names psychedelic-assisted therapy as the exception:
"transient attractor flattening enabling large-scale map restructuring." NMDA-receptor antagonism
(ketamine / esketamine) is the **other** fast route to the same construct, and it is the one with a
marketed product.

The REE reading is mechanistic, not a re-label of "antidepressant":

- Ketamine blocks NMDA receptors preferentially on **fast-spiking GABAergic interneurons**, producing a
  net **disinhibition** / glutamate surge (AMPA-throughput, synaptogenesis). In REE terms that is a
  transient drop in the rigidity of the hippocampal-terrain attractor walls — a **fast flattening** of
  the MECH-085 aversive basin and a window in which MECH-076 terrain topology can be re-graded in hours
  rather than weeks. This is why the architecture predicts the effect on the **terrain** axis
  (basin depth, rollout capture), not on the dopamine-selection axis (PHARM-022) and not on the
  5-HT2A narrative-exclusivity axis (PHARM-015).
- The distinctive, falsifiable prediction is therefore **timescale + axis**, not just efficacy: a rapid
  (hours) collapse of aversive-basin capture that a monoaminergic agent cannot produce on that
  timescale, and that — crucially — should be **strongest where the basin is deepest and most rigid**
  (treatment-resistant, high-suicidality presentations), exactly the population where esketamine carries
  its label. If ketamine's benefit were uniform across basin depth, or fully reproduced by accelerating
  a monoaminergic agent, the "fast-remodelling-of-a-rigid-terrain" reading would be wrong.

This is the highest-profile repurposing line in the layer: **esketamine is approved (TRD / MDD with
suicidal ideation) but racemic ketamine — the cheaper, generic, off-label molecule — is the same
mechanism**, and the cost-of-evidence gap between them is the public-systems story (Section 5).

### 3E. GABA-A: alpha-1 (sedation/sleep) vs alpha-2/3 (anxiolysis/harm-decay) are two planes

PHARM-004 and PHARM-009 treat GABAergic agents at the class level: PHARM-004 reads benzodiazepine
relief of catatonia as augmenting the SD-036 cross-stream decay regulator; PHARM-009 reads chronic
hypnotic use as SWS-architecture disruption (INV-048). The subunit rung resolves these into **two
different REE planes carried by two different alpha-subunits of the same receptor**:

- **alpha-2/3-containing GABA-A** (limbic, spinal) carries the **anxiolytic / harm-stream-decay** action
  (SD-036). Restoring decay of pinned harm streams *is* anxiolysis in REE terms — the mode flip from
  'avoid' back to goal-seeking that SD-036 predicts. The architecturally clean prediction is that an
  alpha-2/3-selective positive allosteric modulator should produce **anxiolysis without sedation** and
  without the SWS-architecture cost.
- **alpha-1-containing GABA-A** (thalamocortical) carries the **sedation / sleep-onset** action — and,
  per PHARM-009, the SWS-architecture *disruption*. The hypnotic effect substitutes for homeostatic
  sleep pressure rather than restoring SWS-dependent consolidation.

So the non-selective benzodiazepine's two headline effects — anxiolysis and sedation — sit on **two
different REE planes**, and the subunit split predicts they are **dissociable** (this is the GABAergic
analogue of the M1/M4 two-plane story in 3B). The clinical record is consistent with the *difficulty*
of the dissociation, not yet its success: alpha-2/3-selective anxioselective compounds have been
trialled repeatedly (Merck's MK-0777/TPA023 across five Phase 2 GAD studies; AbbVie's darigabat in
panic disorder) but **none is approved** — the efficacy/tolerability separation has been hard to
realise. REE's contribution here is the *prediction that the dissociation is real and worth the
engineering*, with zolpidem (alpha-1-preferring) as the sedation-side control.

### 3F. Dopamine: D2 (selection gain) vs D3 (anti-anhedonic incentive) resolve MECH-086 by subtype

MECH-086 makes dopamine the **trajectory-selection gain plane** — "which rollout wins and how quickly."
Its failure modes are explicitly *two-sided*: "too little -> indecision, flattened landscape,
**anhedonia**; too much -> premature commitment, aberrant salience." The receptor rung resolves these
onto two receptor subtypes with different anatomy:

- **D2** (dorsal / associative striatum) carries the **selection-gain headline** — the
  premature-commitment / aberrant-salience arm that D2 antagonists (antipsychotics) damp and D2 agonists
  push. This is MECH-086 as written and the MECH-088 psychosis "selection" arm.
- **D3** (ventral striatum / nucleus accumbens, limbic) carries the **anti-anhedonic incentive-salience**
  arm — reward-motivation weighting on the selection landscape, dissociable from D2 motor-selection.
  REE reads anhedonic / amotivational depression (MECH-088's "DA selection failure" component) as a
  **D3-resolved hypofunction of the incentive arm**, distinct from the 5-HT2A narrative axis (PHARM-015),
  the 5-HT1A terrain axis (PHARM-016) and the kappa commitment-entropy axis (PHARM-018).

Pramipexole is a **D3-preferring** agonist (its D3:D2 affinity ratio is the relevant pharmacology). The
architecturally distinctive prediction is that its anti-anhedonic signal should track the **D3 (limbic
incentive)** arm and be dissociable from a pure D2 agonist's motor effect — and that it acts on the
**reward-weighting** arm of MECH-086, not on the serotonin terrain. The trial record is the strongest
of the four extensions for an *anhedonia-specific* endpoint: a dedicated anhedonia-augmentation Phase 2
(NCT04121091) and a ventrostriatal-reward mechanistic Phase 4 (NCT02033369) both target exactly this
arm. Pramipexole is approved for Parkinson's disease and restless legs — the depression indication is
off-label, the repurposing yield.

### 3G. Orexin: OX1R/OX2R is the receptor rung under the existing DORA entries

PHARM-001 and PHARM-010 already map the DORA class (suvorexant / lemborexant / daridorexant) onto the
SD-037 hyperarousal-override substrate and the INV-048 sleep-architecture-preservation axis. They sit at
the *class* level; the receptor rung underneath them is the **OX1R / OX2R** split. The
sleep-promoting action is **OX2R-dominant** (OX2R drives the histaminergic TMN wake system; OX1R is more
noradrenergic/reward-coupled), which is why DORAs and the OX2R-selective seltorexant are sleep agents.
Adding the `receptor_resolution` field to PHARM-001/010 makes that rung machine-visible without
changing the predictions: the override that DORAs damp is carried predominantly through **OX2R** onto
the SD-037 wake-drive plane. This is a cross-link, not a new repurposing candidate — DORAs are already
approved for insomnia — but it brings the two pre-existing orexin entries onto the same receptor-resolved
footing as PHARM-015..022.

---

## 4. Substrate-modelling probe: what V3 can and cannot test

The user's second question — can the *current* V3 substrate model these failure modes? — has a
clean, honest answer with a sharp boundary.

**V3 CAN perturb plane-level failures** (existing ablation knobs, confirmed in `ree-v3/`):

| REE plane failure | V3 knob / ablation that reproduces it | Existing script family |
|---|---|---|
| Dopamine selection flattening -> anhedonia/indecision | E3 selection-gain / commitment threshold | `v3_exq_*_monostrategy_*`, `*_zgoal_monostrategy_falsifier` |
| Harm-stream lock (catatonia II analog) | harm-stream weights / cross-stream decay | `v3_exq_533_mech102_harm_stream_ablation`, `*_508_arc033_e2_harm_s_*` |
| Consolidation / sleep-pipeline degradation (dementia analog) | sleep-phase ablation, consolidation ablation | `v3_exq_242_sd017_sleep_phase_ablation`, `*_pharm_sleep_disruption_equivalence` |
| Commitment-gate paralysis (catatonia I / OCD analog) | closure-operator / commitment gate | `v3_exq_*_closure_*`, SD-034 cluster |
| Drive disruption | `drive_weight` | `v3_exq_238_sd012_drive_weight_ablation` |

The key already-registered testable prediction is **MECH-087's cross-plane non-rescue**: degrade the
serotonin (terrain) axis and the resulting trajectory pathology should NOT be rescued by increasing
dopamine gain; degrade the dopamine axis and it should. That is a *substrate-tractable* experiment
and the natural next probe (see Section 7 — flagged for `/queue-experiment`, not run here).

**V3 CANNOT test receptor-subtype resolution.** The substrate has no 5-HT1A-vs-2A split, no
muscarinic M1/M4 distinction, and no explicit opioid policy-entropy term. The receptor *subtype*
distinctions are therefore `out_of_domain` for V3 (consistent with the existing `out_of_domain`
epistemic category for pharmacology in `REE_assembly/CLAUDE.md`): they are adjudicated against
clinical literature, not V3 runs. **Insight from the probe:** the substrate can validate the
*plane-level dissociation logic* that the receptor layer rests on (MECH-087), but the receptor rung
itself is a clinical-literature object. This is the right division of labour — and it tells us the
single highest-value V3 experiment to license the whole layer is the MECH-087 non-rescue test.

---

## 5. Repurposing candidates and their evidence (MCP-validated, 2026-06-12)

Trial counts and NCT IDs below were pulled live from ClinicalTrials.gov; receptor pharmacology from
ChEMBL. "Approved-but-off-this-indication" is the repurposing-yield flag.

- **Pimavanserin (5-HT2A inverse agonist).** Approved 2016 for Parkinson's disease psychosis
  (ChEMBL CHEMBL2448613; USAN stem `-anserin` = 5-HT2 antagonist). ACADIA's CLARITY programme ran
  Phase 2 (NCT03018340) and Phase 3 adjunctive-MDD (NCT03968159, completed) — **the MDD indication
  was trialled but not approved.** A Mount Sinai trial (NCT06592833, recruiting) uses pimavanserin
  to *block* 5-HT2A and dissect psilocybin's mechanism — a ready-made dissociation probe for the
  Section 3A level-split. **Repurposing gap: adjunctive MDD / primary psychosis.**
- **Buprenorphine (mu partial + kappa antagonist).** 27 depression trials on ClinicalTrials.gov,
  including Stanford anti-suicidal Phase 3 (NCT04116528, completed), a French anti-suicidal Phase 3
  (NCT03646058, recruiting, n=180), late-life TRD (NCT01071538), and the ALKS-5461
  (buprenorphine+samidorphan, kappa-antagonism unmasked) MDD programme (NCT01381107). Approved only
  for opioid dependence / pain. **Repurposing gap: anti-anhedonic / anti-suicidal adjunct in
  treatment-resistant depression** — high public-health salience given the suicidality endpoint.
- **Xanomeline/trospium (M1/M4 agonist, Cobenfy).** 40 trials; approved 2024 for schizophrenia, now
  expanding to Alzheimer's psychosis (ADEPT-3, NCT05980949), AD agitation (NCT07011732), and
  schizophrenia cognition (NCT07084831). The first non-D2 antipsychotic — the live proof that the
  receptor-subtype-resolved mechanism is where the field is moving. **Repurposing gap: MCI/AD
  cognition, AD psychosis (actively closing).**
- **Buspirone (5-HT1A partial agonist).** Approved for GAD. REE-predicted extension: terrain-basin
  flattening as augmentation in anhedonic/terrain-locked depression and the PTSD terrain component
  — distinct from the 5-HT2A (pimavanserin) narrative axis. **Repurposing gap: terrain-component
  augmentation.**
- **Esketamine / ketamine (NMDA antagonist).** Esketamine (Spravato, ChEMBL CHEMBL2364609) is FDA-
  approved (2019, max_phase 4) for treatment-resistant depression and for MDD with acute suicidal
  ideation (the MDSI label rests on Janssen Phase 3 NCT03039192, n=226, completed; the adolescent
  MDSI Phase 3 NCT07227454 is now recruiting). Racemic **ketamine is off-label** with a deep trial
  record — 140 TRD trials on ClinicalTrials.gov including Janssen Phase 2 NCT01627782 and MGH's
  suicidal-ideation infusion work (NCT01582945; long-term maintenance NCT05450432). **Repurposing
  gap: racemic ketamine for the same rapid-remodelling indication** — the same NMDA mechanism at a
  fraction of esketamine's cost, the single highest-yield line for a public payer. *(Mechanism note:
  the ChEMBL salt-level mechanism record is sparse; NMDA-receptor antagonism is the established,
  textbook pharmacology and is cited as such, not as an MCP-derived novelty.)*
- **Pramipexole (D3-preferring agonist, Mirapex; ChEMBL CHEMBL3182733).** Approved 1997 (max_phase 4)
  for Parkinson's disease and restless legs. 24 depression trials, with an **anhedonia-specific**
  signal: a dedicated anhedonia-augmentation Phase 2 (NCT04121091, Region Skane, completed), a
  ventrostriatal-reward-motivation mechanistic Phase 4 (NCT02033369, NYSPI), bipolar-depression
  augmentation (NCT00893841), a pramipexole+ondansetron MDD Phase 2a (NCT03642964, CTC-501, active),
  and inclusion in UCSF's precision-MDD Phase 4 (NCT06580041). **Repurposing gap: anti-anhedonic
  augmentation in depression** — distinct from the D2 motor-selection arm and from monoaminergic
  agents. No black-box warning. *(D3-preference is the established pharmacology; the depression
  indication is off-label.)*
- **alpha-2/3-selective GABA-A PAMs (no approved agent yet).** The subunit-selective anxioselective
  programme is real but **unconverted**: Merck's MK-0777/TPA023 ran five Phase 2 GAD studies
  (NCT00539578 n=270; NCT00543920; NCT00546624 head-to-head vs lorazepam; NCT00703833), and AbbVie's
  darigabat reached Phase 2 in panic disorder (NCT05941442, **terminated** 2025). None reached
  approval — the anxiolysis/sedation separation has been hard to realise in practice. The REE
  contribution is the *prediction that the dissociation is architecturally real* (alpha-2/3 = SD-036
  harm-decay anxiolysis; alpha-1 = sedation/SWS-disruption, zolpidem as the control). **This is a
  development-target prediction, not an approved-drug repurposing candidate** — flagged honestly as
  lower-yield than the ketamine/pramipexole lines because there is no marketed alpha-2/3-selective
  molecule to repurpose.

### Why this matters for public systems
The product here is a *research direction*, not a treatment claim. An already-approved drug carries a
known safety profile, so the trial that would generate the evidence is cheaper and faster to run than
for a new molecule — but REE only points to *which* trial is worth prioritising; the trial, not REE,
produces the evidence. For a public payer (HSE included) the value is purely in better-prioritised
research: a falsifiable, mechanism-motivated hypothesis about an off-label use is a stronger reason to
fund a trial than an untethered hunch. It is not, and cannot become, a basis for prescribing ahead of
that trial. The discipline below (falsification conditions, dissociation logic) is what makes a
hypothesis worth a trial's cost — it does not substitute for the trial.

---

## 6. Functional-link audit — new candidate links worth recording

Gap-mining the existing taxonomy against the receptor rung surfaced links not yet captured, each
gated on a falsification condition (the rule: record only if testable).

1. **5-HT2A inverse agonism <-> alpha_theta over-precision (IMPL-005 #3 "narrative lock").** The
   implementation-failure-mode doc names high alpha_theta as delusion-like narrative lock but gives
   no neuromodulator. Candidate link: 5-HT2A tone sets top-level precision; inverse agonism should
   *reduce* narrative-lock severity. *Falsifier:* pimavanserin does not reduce delusional conviction
   in primary psychosis beyond its established antipsychotic-adjunct effect on hallucinations.
2. **M4 muscarinic <-> dopamine-selection plane (MECH-086) without D2.** Candidate link: aberrant
   salience can be corrected from the muscarinic side. *Falsifier:* xanomeline's antipsychotic effect
   is abolished by selective M4 (not M1) knockdown only if the effect is M1-mediated — i.e. the
   prediction is that M4 is necessary; M1-only would falsify the selection-plane attribution.
3. **kappa-opioid <-> commitment-entropy axis as a depression *subtype* axis (ARC-086).** Candidate
   link: kappa-driven destabilisation is a vulnerability axis distinct from the serotonin-terrain and
   dopamine-selection axes already in ARC-086. *Falsifier:* kappa antagonism (buprenorphine arm)
   produces the *same* response profile as an SSRI on anhedonia-specific endpoints (would collapse
   the axis into the existing serotonin axis).
4. **5-HT1A autoreceptor desensitisation <-> SSRI onset delay reframed at the terrain level.** The
   2-4 week SSRI delay is attributed in MECH-085 to slow map-geometry change; the 5-HT1A
   somatodendritic autoreceptor desensitisation timecourse is a receptor-level mechanism for exactly
   that delay. *Falsifier:* 5-HT1A partial agonist augmentation (buspirone, pindolol) does not shorten
   antidepressant onset (the pindolol-augmentation literature is the existing partial test).

5. **NMDA antagonism <-> rapid terrain remodelling (MECH-076/077/085) on an hours timescale.** The
   terrain account makes map-geometry change slow; MECH-077 already excepts psychedelic flattening.
   Candidate link: NMDA-antagonist disinhibition is the *second* fast-remodelling route, predicted to
   act on basin depth (terrain), not selection gain. *Falsifier:* ketamine's antidepressant effect is
   uniform across baseline aversive-basin depth/rigidity (no greater effect in the most
   treatment-resistant, deepest-basin presentations), OR is fully reproduced by accelerating a
   monoaminergic agent — either would collapse the "fast-remodelling-of-a-rigid-terrain" reading into
   generic efficacy.
6. **D3 (vs D2) <-> the anhedonic/incentive arm of MECH-086 as a reward-weighting subtype.** Candidate
   link: the "too little dopamine -> anhedonia" arm of MECH-086 is D3-resolved (limbic incentive
   salience), dissociable from the D2 motor-selection arm. *Falsifier:* a D3-preferring agonist
   (pramipexole) and a non-selective/D2 agonist produce indistinguishable effects on an
   anhedonia-specific (not motor, not global-mood) endpoint — which would collapse the D2/D3
   subtype split of the selection plane.
7. **GABA-A alpha-2/3 (vs alpha-1) <-> SD-036 harm-decay anxiolysis as a subunit-resolved plane.**
   Candidate link: anxiolysis (alpha-2/3, harm-stream decay) and sedation (alpha-1, sleep-onset/SWS
   cost) are separable REE planes carried by different subunits. *Falsifier:* an alpha-2/3-selective
   PAM that achieves clinically meaningful anxiolysis shows the *same* sedation/SWS-architecture
   liability as a non-selective benzodiazepine — which would mean the planes are not subunit-separable
   as predicted. (The repeated failure of alpha-2/3-selective agents to reach approval is a *weak
   prior against easy separability*, not yet a falsification — efficacy, not the dissociation per se,
   is where they have faltered.)

These are candidate links for `psychiatric_failure_modes.md` / the audit, **not** registered claims.
Promotion to a claim requires the biology-first lit-pull (the standing rule).

---

## 7. Next steps (not executed here)

- **Substrate experiment (V3-tractable):** MECH-087 cross-plane non-rescue test — degrade serotonin-
  terrain axis, confirm dopamine-gain does not rescue; degrade dopamine axis, confirm it does. Route
  via `/queue-experiment` (do not hand-write). This is the one experiment that licenses the plane-
  level dissociation logic the receptor layer rests on.
- **Lit-pulls (biology-first, before any claim registration):**
  - **DONE 2026-06-12 — strands 3A/3B/3C grounded** (the original pilot PHARM-015..018):
    `evidence/literature/targeted_review_receptor_subtype_layer/` (11 entries). **3A** raphe projection
    specificity + the 5-HT2A-cortical / 5-HT1A-limbic distribution (Ren et al. 2019 eLife, DR/MR
    projection segregation; Weber & Andrade 2010, 5-HT2A on cortical L5 pyramidal; Akimova et al. 2009,
    5-HT1A in anxiety; Wu et al. 2021, median-raphe 5-HT tunes hippocampal stability). **3B** M4-striatal
    dopamine-selection damping + the non-D2 antipsychotic route (Foster et al. 2016 Neuron, M4->striatal
    dopamine via CB2; Kaul et al. 2024 EMERGENT-3, xanomeline phase 3; McKinzie & Bymaster 2012,
    reciprocal M4-dopamine). **3C** kappa/dynorphin dysphoria as a commitment-entropy substrate (Land
    et al. 2008, dysphoria encoded by dynorphin/KOR; Bruchas et al. 2009, review; Krystal et al. 2020
    Nat Med, KOR antagonism re-engages reward circuitry; Bari et al. 2025, KOR antagonism restores
    OPTIMAL PERSEVERATION — the closest empirical analogue of commitment stability). lit_conf raised on
    MECH-006/048/085/086/087/088 + ARC-086; exp_conf unchanged (all `out_of_domain` — grounds DESIGN +
    PHARM falsification, promotes nothing on the V3 substrate axis). **The kappa-driven commitment-entropy
    ARC-086 axis is now lit-supported and PROPOSED for registration (proposal-first; NOT yet in
    claims.yaml — awaiting user decision, with the optimality + multi-component refinements from Bari
    et al. folded in).**
  - **PENDING — strands 3D/3E/3F/3G** (the extension PHARM-019..022 + orexin retrofit): NMDA-antagonist
    disinhibition + rapid synaptogenesis as fast terrain remodelling (3D); GABA-A alpha-subunit anatomy
    (alpha-2/3 limbic anxiolysis vs alpha-1 thalamocortical sedation, 3E); D3-vs-D2 ventral/limbic
    incentive dissociation (3F); OX1R/OX2R wake-drive specificity (3G) — not yet pulled.
- **Registry:** PHARM-015..018 (pilot) + PHARM-019..022 (this extension: NMDA/glutamate,
  GABA-A alpha-2/3, GABA-A alpha-1, D2/D3 dopamine) added; PHARM-001/010 (DORA) retro-fitted with
  the `receptor_resolution` field (OX1R/OX2R). All carry `receptor_resolution` so the rung is
  machine-visible; all are `out_of_domain` (clinical-literature-adjudicated). Future entries should
  carry the field by default.

---

## Cross-references
- `docs/architecture/neuromodulatory_control_planes.md` (MECH-083..088; the conflict this resolves)
- `docs/architecture/psychiatric_failure_modes.md` (clinical mappings)
- `docs/architecture/psychiatric_failure_axes.md` (ARC-086 vulnerability axes)
- `docs/thoughts/2026-02-11_opioid_receptors.md` (mu/kappa commitment-entropy)
- `evidence/planning/pharmacological_predictions.v1.json` (PHARM registry; PHARM-015..022 + orexin retrofit)
</content>
</invoke>
