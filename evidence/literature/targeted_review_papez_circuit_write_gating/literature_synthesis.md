# Literature Synthesis: Papez Circuit Write Gating

**Date:** 2026-04-16 (original); extended 2026-04-18.
**Purpose:** Targeted literature pull to ground the anatomical substrate for action-mode-specific
write profiles to the hippocampal system. The Papez circuit (hippocampus -> fornix -> mammillary
bodies -> anterior thalamus -> cingulate -> entorhinal cortex -> hippocampus, plus multiple
reciprocal connections) is proposed as the circuit through which the hypothesis_tag signal is
delivered to hippocampal phi(z) write operations (MECH-094), and through which trajectory
proposals navigating residue-field terrain are enabled (ARC-007).

**Claims under investigation:** MECH-094, ARC-007.

---

## Entries

### 2026-04-16 pass (original three entries)

- **Bubb et al. 2017** — hippocampal-diencephalic-cingulate network anatomy (supports ARC-007).
- **Aggleton et al. 2010** — anterior-thalamic disconnection impairs spatial memory (supports ARC-007).
- **Schnider 2003** — confabulation as orbitofrontal reality-filter failure (supports MECH-094).

### 2026-04-18 extension (four new entries)

- **Kamali et al. 2023** — tractography update of Papez circuit adding prefrontal/orbitofrontal,
  septum, amygdala, anterior temporal lobes (supports ARC-007, MECH-094).
- **Dillingham et al. 2015** — two-stream mammillary architecture: medial (memory, VTN-Gudden)
  vs lateral (head direction, DTN-Gudden) streams converging on anterior thalamus
  (supports ARC-007, MECH-094).
- **Arts et al. 2017** — Korsakoff clinical review: Papez-relay lesion pattern produces the
  predicted amnesia+confabulation phenotype (supports MECH-094).
- **Lavallé et al. 2020** — meta-analysis of source-monitoring deficits in schizophrenia;
  establishes clinical dissociation between confabulation (tag loss) and hallucination
  (tag misassignment) (supports MECH-094).

---

## Summary of Evidence

### ARC-007: Hippocampal Map Navigation

**Bubb et al. 2017** (DOI: 10.1177/2398212817723443) establishes the full anatomy of the
hippocampal-diencephalic-cingulate network as a multiply-connected reciprocal system, not a
simple serial loop. The anterior thalamic nuclei are a convergence node receiving both direct
hippocampal input and mammillary body input, and projecting back to hippocampus via cingulate
and retrosplenial cortex. This architecture supports the claim that hippocampal terrain navigation
requires the full circuit, not hippocampus alone.

**Aggleton et al. 2010** (PMID: 20550571) provides disconnection evidence: severing
hippocampal-anterior thalamic connectivity impairs spatial memory even with intact hippocampus
and intact anterior thalamus. This establishes that the anterior thalamic relay is necessary
(not merely associated) for the kind of memory that terrain navigation requires.

**Kamali et al. 2023** (PMID: 37148369) updates this topology from modern human diffusion
tractography: the limbic network is not the classical Papez loop but a cortico-limbo-thalamo-
cortical system incorporating prefrontal / orbitofrontal cortex, septum, amygdala, and anterior
temporal lobes as core components. Multiple reciprocal fibre bundles, not a serial loop.

**Dillingham et al. 2015** (PMID: 25107491) establishes that the mammillary-anterior-thalamic
relay itself is dual-channel: a medial stream (VTN-Gudden input, AM-thalamus output, memory)
and a lateral stream (DTN-Gudden input, AD-thalamus output, head direction) run in parallel.
This is the structural prerequisite for channel-specific write gating: different action modes
can route through different Papez sub-pathways. Without this two-stream architecture, mode-
specific write profiles would have to share a single bottleneck, which contradicts MECH-094's
requirement that the tag gate specific content categories.

### MECH-094: Hypothesis Tag as Write Gate

**Schnider 2003** (PMID: 12894241) provides the most direct neurobiological account of
reality-monitoring failure: confabulation follows orbitofrontal damage and produces write of
contextually inappropriate memory traces to the agent's behavioral state. The OFC reality
filter normally flags whether activated content pertains to ongoing reality -- exactly the
function assigned to the hypothesis_tag in MECH-094.

**Arts et al. 2017** (PMID: 29225466) provides the complementary clinical footprint. Korsakoff's
syndrome damages the Papez-circuit relay (mammillary, anterior / mediodorsal thalamus, fornix)
and produces exactly the phenotype MECH-094 predicts for a broken tag-delivery pathway:
severe anterograde amnesia with confabulation, executive dysfunction, preserved procedural
and remote memory. The tag is missing, but the storage substrate is intact.

**Lavallé et al. 2020** (PMID: 32406366) provides the clinical dissociation that refines
MECH-094 into sub-claims. Source-monitoring meta-analysis in schizophrenia shows a distinct
pattern from Korsakoff: the tag is delivered but with systematically inverted source, so
internally-generated content is externally attributed (the hallucination pattern). This is
different from tag loss; it is tag misassignment. Two separable failure modes of the same
general write-gate architecture, with distinct clinical and probably distinct circuit
signatures.

The connectome + tractography evidence (Bubb 2017, Kamali 2023) supplies the structural
substrate. The rodent anatomy (Dillingham 2015) supplies the parallel-stream architecture.
The clinical evidence (Schnider 2003, Arts 2017, Lavallé 2020) supplies the phenotypes that
characterise specific failure modes of the tag system.

---

## Candidate claim extractions (2026-04-18)

The extended pull suggests three specific refinements to the existing claim registry. Each
is a *candidate* — the user makes the final registration decision.

### Candidate refinement 1 — MECH-094 sub-claim split

MECH-094 currently treats hypothesis_tag failure as a single mechanism producing confabulation
and psychosis together. The Lavallé 2020 / Arts 2017 dissociation argues against this. Two
sub-claims are warranted:

- **MECH-094a — tag_loss_syndrome:** hypothesis_tag delivery pathway damaged; write occurs
  without tag; content is reconstructed but unmarked. Clinical footprint: Korsakoff-pattern
  confabulation. Circuit substrate: Papez relay (mammillary, anterior/mediodorsal thalamus,
  fornix).
- **MECH-094b — tag_misassignment_syndrome:** hypothesis_tag delivered with inverted source
  attribution; internally-generated content marked external. Clinical footprint:
  schizophrenia-pattern hallucination and delusion. Circuit substrate: not fully localised;
  candidates include prefrontal-temporal dysconnectivity.

This preserves the parent MECH-094 as the general architectural claim (tag-gated write) and
specialises it into clinically-dissociable mechanisms. The memory note
`feedback_psychosis_confabulation_distinction.md` explicitly called for this refinement.

### Candidate refinement 2 — MECH new claim, parallel-stream write gating

Registered candidate: **MECH-XXX — papez_dual_channel_write_gating.**
Statement: *the Papez relay is dual-channel (medial mammillary / AM-thalamus = memory
stream; lateral mammillary / AD-thalamus = head-direction stream; Dillingham 2015), and
different action modes (habitual / planned / simulated / sleep) route through different
combinations of these channels.* Depends on: ARC-007, MECH-094. Status: candidate,
implementation_phase: v4 (requires dual-stream hippocampal substrate not yet in REE).

This is the structural claim the 2026-04-16 synthesis's "gap" section explicitly flagged.
It now has anatomical support from Dillingham 2015. It does not yet have direct functional
evidence for action-mode routing; that remains the open empirical question.

### Candidate refinement 3 — ARC-007 connectome update

The existing ARC-007 evidence_quality_note cites Bubb 2017. It should be extended to cite
Kamali 2023 (tractography confirms reciprocal multi-pathway architecture in humans) and
Dillingham 2015 (mammillary relay is itself dual-channel). No change to claim status —
this is evidence strengthening on a claim already in `v3_pending` state pending SD-004
HippocampalModule.

---

## Gaps (revised)

- **Circuit substrate for MECH-094b (hallucination-pattern tag misassignment) is unsettled.**
  Source-monitoring deficits in schizophrenia correlate with prefrontal-temporal dysconnectivity
  but the specific write-gate substrate is not localised by the papers pulled. A further
  targeted pull on source-monitoring circuit imaging would close this gap.
- **Action-mode specificity (habitual vs deliberate vs simulated vs sleep) is still indirect.**
  Dillingham 2015's two-stream architecture makes mode-specific routing anatomically possible
  but does not prove any stream carries a mode-specific write-gating signal.
- **Mammillary two-stream architecture in humans is less well-characterised.** The Gudden
  tegmental nuclei have well-established rodent anatomy; human homology is credible but
  imaging evidence is sparser.
- **The REM sleep write-profile (hypothesis_tag active but may fail) is addressed separately
  in targeted_review_connectome_mech_094 (Hobson & Pace-Schott 2002 entry).** Not extended in
  this pull.
