---
nav_exclude: true
---

# Receptor-Subtype + Interaction-Effects Layer (model <-> intervention)

**Created:** 2026-06-12
**Status:** working abstraction layer (not a claim cluster; no claims.yaml entries created here)
**Depends on (reads):** MECH-083..088 (four-plane neuromodulatory model), MECH-006/048/085, ARC-005,
psychiatric_failure_modes.md, psychiatric_failure_axes.md (ARC-086)
**Feeds:** `evidence/planning/pharmacological_predictions.v1.json` (PHARM-015..PHARM-018)

> **HONESTY RAIL (read first).** REE is a research-stage computational specification, not a
> deployed AI, not a validated disease model, and not a clinical decision tool. Everything below
> is a set of **testable hypotheses and shared vocabulary**, not treatment guidance. The
> repurposing candidates named here are *predictions to be adjudicated against clinical
> literature* (RCTs, naturalistic cohorts), exactly like the rest of the PHARM registry. No
> patient should be treated on the basis of this document. Receptor pharmacology is the place
> REE has historically been "philosophy-right / mechanism-wrong" (see
> `memory/feedback_biology_before_definitions`): elegance is not evidence.

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

### Why this matters for public systems
An already-approved drug carries a known safety profile and an off-label / low-cost-of-evidence
path to a new indication. For a public payer (HSE included) that is structurally the cheapest way to
add a treatment option — *provided* the prediction has survived a refutation attempt, not merely
been registered. The discipline below (falsification conditions, dissociation logic) is what
converts "interesting receptor match" into a payer-relevant asset.

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

These are candidate links for `psychiatric_failure_modes.md` / the audit, **not** registered claims.
Promotion to a claim requires the biology-first lit-pull (the standing rule).

---

## 7. Next steps (not executed here)

- **Substrate experiment (V3-tractable):** MECH-087 cross-plane non-rescue test — degrade serotonin-
  terrain axis, confirm dopamine-gain does not rescue; degrade dopamine axis, confirm it does. Route
  via `/queue-experiment` (do not hand-write). This is the one experiment that licenses the plane-
  level dissociation logic the receptor layer rests on.
- **Lit-pulls (biology-first, before any claim registration):** raphe projection specificity +
  5-HT1A/2A distribution (reconciliation 3A); M4-striatal modulation of dopamine selection (3B);
  kappa/dynorphin dysphoria circuitry as a commitment-entropy substrate (3C).
- **Registry:** PHARM-015..018 added (Section 5). Future entries should carry the
  `receptor_resolution` field so the rung is machine-visible.

---

## Cross-references
- `docs/architecture/neuromodulatory_control_planes.md` (MECH-083..088; the conflict this resolves)
- `docs/architecture/psychiatric_failure_modes.md` (clinical mappings)
- `docs/architecture/psychiatric_failure_axes.md` (ARC-086 vulnerability axes)
- `docs/thoughts/2026-02-11_opioid_receptors.md` (mu/kappa commitment-entropy)
- `evidence/planning/pharmacological_predictions.v1.json` (PHARM registry; PHARM-015..018)
</content>
</invoke>
