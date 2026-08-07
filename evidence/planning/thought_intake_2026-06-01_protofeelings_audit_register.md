# Thought intake: proto-feelings as control signals -- a staged proto-affective audit register

**Date:** 2026-06-01 (raw); intake written 2026-06-05
**Status:** intake / planning scaffold (NOT yet registered). Proposes a deliverable (audit
register), not a claim cluster.
**Raw thought file:** `docs/thoughts/2026-06-01_ProtoFeelings_implementation_timing.md`
**Origin:** user audit -- REE already contains several proto-feelings as drive-weighted control
signals; the next task is not an emotion module but a staged audit of which signals exist, which
are missing, which are needed for minimum-viable control vs mammalian completeness, and when each
should be implemented.
**Anchors:** `docs/architecture/affect_primitives.md` (the EXISTING three-primitive register --
this thought extends it), MECH-112 (wanting/liking), SD-011 (threat/harm), residue (MECH-056),
ARC-065 + MECH-313/314 (curiosity), MECH-320 (tonic vigor), MECH-061/MECH-090 (commitment), and
the V4 ethics cluster `thought_intake_2026-05-31_musings_on_v4.md` (guilt/shame/repair).

---

## 1. Core idea

A **proto-feeling** = a drive-weighted control signal that changes perception, salience, action
selection, persistence, commitment, or learning (need not be conscious or human-named). The thought
audits **17 candidate signals** against two thresholds -- **A: minimum-viable control** (absence
breaks action arbitration) and **B: mammalian/human affective completeness** -- and assigns each an
implementation timing (Now/V3, late-V3 conditional, V4-social, theory). Recommended deliverable: a
**proto-affective audit register**, one row per signal (function, current substrate, threshold A/B,
pathology-if-absent, pathology-if-overactive, V3/V4 timing, smallest testable proxy, lit anchors,
claim IDs, open questions). "Implementation should follow failure signatures, not emotion names."

## 2. What is new vs what REE already has

| Element | Already in REE? | Verdict |
|---|---|---|
| An affect-primitive register | **Yes** -- `affect_primitives.md` (three-primitive split) | The register concept EXISTS; this thought is the **completeness audit against it** |
| Wanting / liking / threat / residue / commitment as control signals | **Yes** -- MECH-112, SD-011, MECH-056, MECH-061/090 | Confirms (signals 1-5 = "already V3-core") |
| Curiosity / fatigue-stop-recover / safety-soothing / boundary-violation as **P0 V3-relevant gaps** | **Partial** -- curiosity ARC-065/MECH-313/314, vigor MECH-320; fatigue noted as a missing constraint in claims.yaml; safety/anger weak | **Extension** -- names the V3-actionable subset |
| **Threshold A vs B framing** (min-viable-control vs mammalian-completeness) as the prioritisation axis | **No** | **NOVEL framing** -- a clean triage primitive |
| **Implementation-timing-follows-failure-signature** discipline (don't build by emotion name) | **Partial** -- consistent with the calibration-debt + containment-only ethos | Sharpening |
| Guilt/shame/grief/care/attachment as V4 social signals with explicit early-implementation RISK (shame-before-repair -> pathological self-punishment) | **Overlaps** the V4 ethics cluster (musings_on_V4: no-global-self-condemnation, guilt-repair) | **Cross-link** -- ProtoFeelings is the affect-side register; musings_on_V4 is the attribution/repair-side cluster |

**Verdict: a planning scaffold, not a claim cluster.** Its value is the audit register deliverable
+ the threshold-A/B triage + the P0 V3-relevant gap list (curiosity, fatigue/stop-recover, safety/
soothing, boundary-violation). It deliberately overlaps several existing clusters (curiosity =
ARC-065; guilt/shame = musings_on_V4; safety/fatigue = homeostasis/sleep) -- it is the *unifying
audit* over them, the affective analogue of the attention-as-distributed-precision unification note.

## 3. The actionable deliverable

Build a **proto-affective audit register** (one row/signal) that cross-references existing claim IDs
so the 17 signals map onto what REE already has. The thought's P0 set is the V3-relevant subset to
audit first:
- **Curiosity / novelty** (ties to monostrategy bottleneck; ARC-065 cluster) -- audit first.
- **Fatigue / overload / stop-recover** (over-persistence prevention + sleep timing).
- **Safety / soothing** as a *positive* "safe-enough" state (low-harm != safety).
- **Boundary-violation / blocked-agency** (anti-coercion; at least as an audit category).

P1 conditional: disgust/contamination (OCD-contamination link to SD-033/034), boredom, guilt-if-
residue-doesn't-repair, anger. P2 V4-social: care/attachment, grief, shame, full play, co-regulation.
P3 out-of-scope: lust.

## 4. Candidate claims / artifacts

**RESOLVED 2026-08-07 -- REGISTERED, in section 7 below rather than here.** This section correctly
proposed no new MECH/ARC of its own; the claims the thought's routing produced are
**MECH-353** (blocked_agency / `z_block`, V3), **MECH-354** (effort/fatigue stop-recover, SD-012
side, V3-minimal) and **MECH-355** (soothing/comfort autonomic state-gain modulator, V4-social) --
all three minted 2026-06-05 after their gating `/lit-pull`s landed, plus the pre-existing
**MECH-302** (relief) / **MECH-303** + **MECH-304** (safety) which the register cross-references
rather than duplicates. The section-3 deliverable also EXISTS: the rows live in
`docs/architecture/affect_primitives.md` "Extension Register: Beyond Harm", each carrying its
neighbour-differentiation. The one item still genuinely open is the Q below -- deliberately
un-minted, because the register answers it row-by-row rather than as a single claim.

- **Artifact (proto-affective audit register)** -- a planning doc / register, NOT a claim. Likely
  `evidence/planning/proto_affective_register.*` or a section in `affect_primitives.md`.
- **Q (threshold-A-minimal-affect-set)** -- which proto-feelings are truly necessary for minimal
  REE control? *[open; the register answers it row-by-row]*
- No new MECH/ARC from this thought directly -- it routes work into existing clusters (curiosity,
  fatigue/homeostasis, safety, boundary, and the V4 ethics cluster) rather than asserting mechanisms.

## 5. Affected existing claims / docs

- `docs/architecture/affect_primitives.md` (extend the register or cross-reference it).
- MECH-112, SD-011, MECH-056, MECH-061/090, ARC-065 + MECH-313/314, MECH-320; homeostasis/sleep
  (SD-017) for fatigue; SD-033/034 for contamination/disgust.
- V4 ethics cluster `thought_intake_2026-05-31_musings_on_v4.md` (guilt/shame/repair side) and
  the calibration-debt programme (`evidence/calibration/calibration_debt_index.md`) -- ProtoFeelings
  is a sibling unification audit, not a competing plan.

## 6. Next steps (gated)

1. **Build the audit register** as the concrete deliverable (one row/signal, cross-referenced to
   claim IDs). This is the highest-value, lowest-risk action -- it is bookkeeping over existing
   substrate, not new architecture.
2. Route each P0 gap into its existing home (curiosity -> ARC-065; fatigue -> homeostasis/sleep;
   safety/boundary -> new audit categories) rather than building a parallel "emotion module."
3. Keep V4 social signals (care/grief/shame) cross-linked to the musings_on_V4 ethics cluster; heed
   that thought's risk note + memory `feedback_psychosis_confabulation_distinction` (guilt != shame
   != self-condemnation).

## 7. Lit-check verdict + spawned /lit-pulls (2026-06-05)

A user-prompted question -- "are the P0 gaps best placed in the Developmental Needs Register, or
are they really commitment-boundary phenomena or their own streams (like goal/harm stream)?" --
led to a placement correction and a PubMed scouting check. **Two findings, both confirming the
gaps are DISTINCT streams, not duplicates of existing rows (collapsing them would repeat the
SD-010->SD-011 "philosophy-right/mechanism-wrong" error; see memory
`feedback_biology_before_formal_definitions`):**

1. **Placement correction.** These are standing control signals (streams), NOT developmental-stage
   gates. The architecturally-correct home is the **`affect_primitives.md` "Extension Register:
   Beyond Harm"** (which already carries V4-deferred rows like Relief), with consumer cross-notes
   to commitment-closure (MECH-342 decommit) and control_plane -- NOT new DEV-NEED rows, NOT GAP
   nodes in the active V3 closure map. Curiosity is excluded (already ARC-065 + DEV-NEED-029).

2. **"safety/soothing" is THREE distinct systems, none identical to the existing Relief row:**
   - RELIEF = appetitive signal at the OFFSET of an aversive event; NAc dopamine-D1 + NMDA
     (Bergado Acosta et al. 2016, Neuropharmacology, DOI 10.1016/j.neuropharm.2016.11.022). REE's
     existing Relief row.
   - SAFETY = a LEARNED PREDICTOR of threat-absence (active inhibition, prospective); nucleus
     reuniens->BLA (Silva et al. 2021, Nat Neurosci, DOI 10.1038/s41593-021-00856-y) + PL/IL mPFC
     ensembles (Corches et al. 2018, Behav Brain Res, DOI 10.1016/j.bbr.2018.11.042). NEW stream.
   - SOOTHING/COMFORT = down-regulation of an ONGOING stress response (social buffering;
     parasympathetic/oxytocin). NEW stream, V4-social.

3. **"fatigue/stop-recover" != suffering-withdrawal:** learned helplessness is uncontrollable-
   AVERSIVE-stress -> dorsal-raphe 5-HT + CRF (Maier & Watkins 2005, Neurosci Biobehav Rev, DOI
   10.1016/j.neubiorev.2005.03.021; Hashimoto et al. 2021, Brain Commun, DOI
   10.1093/braincomms/fcab285) = SD-011 / z_harm_a territory. Central/mental fatigue is a
   metabolic/effort-depletion construct (MFI-20 multidimensional). They CONVERGE on "stop/disengage"
   but from opposite antecedents. **Fatigue therefore belongs on the SD-012 homeostasis side, NOT
   the SD-011 suffering pathway** -- which REE's own DEV-NEED-002 ("Harm, hunger, fatigue ... blur
   together" = failure) and the SD-011/SD-012 split already predict. The stop/disengage CONSUMER may
   be shared with MECH-342 (maintenance-time decommit) but the SIGNAL is distinct.

**Registration is GATED on three spawned /lit-pull chips (do not write rows into
`affect_primitives.md` before these land, per biology-before-formal-definitions):**
- `task_3ab79018` -- safety vs relief vs soothing differentiation.
- `task_93a719b6` -- fatigue/stop-recover vs suffering-withdrawal (SD-012 vs SD-011).
- `task_64c2e558` -- boundary-violation / blocked-agency / anger(RAGE) stream (frustrative
  non-reward, sense-of-agency, reactance/coercion; V4-social with possible V3 blocked-action proxy).

When the pulls land: register confirmed-distinct streams as new `affect_primitives.md` Extension
Register rows, each explicitly differentiated from its neighbour (safety!=relief!=soothing;
fatigue!=suffering), with consumer cross-notes. Attribution: *Based on articles retrieved from
PubMed.*

**Status update 2026-06-05:** chip `task_64c2e558` (boundary-violation / blocked-agency / anger)
LANDED -- `evidence/literature/targeted_review_blocked_agency_anger_stream/` (5 entries + VERDICT).
Verdict: distinct stream warranted, splits into **Stream A blocked-agency/control-failure (V3)**
and **Stream B coercion/domination/injustice (V4-social)**. **Stream A is now registered** as the
`blocked_agency` (`z_block`) V3-candidate row in `affect_primitives.md` Extension Register
(detector = SD-029 comparator; antecedent = frustrative-non-reward expected-minus-realised,
no noxious input; consumers assert + decommit/MECH-342 gated by ARC-016; capacity-axis opposite
pole to Q-036/z_harm_a withdraw). **Stream B deferred to V4** (stub row added; needs other-agent
model; cross-link `musings_on_v4`). GATED next steps (NOT done): a `claims.yaml` SD/MECH backing
`z_block` + the smallest-V3 blocked-action experiment (per VERDICT).

**Status update 2026-06-05 (register consolidation):** ALL THREE pulls' confirmed-distinct streams
are now written into the `affect_primitives.md` Extension Register (previously only blocked-agency
was). Added/sharpened rows: **Relief**->MECH-302 (V3), **Safety**->MECH-303+MECH-304 (V3, doc-sync
of existing claims + Silva-2021 thalamic-relay enrichment flag), **Soothing/comfort** (NEW row,
V4-social + optional V3-min autonomic-recovery hook on MECH-219/SD-012/SD-032e, explicitly
NOT-302/303/304/112), **Effort/fatigue stop-recover** (SD-012 side + SD-048 host, two-bound Meyniel
accumulator, shares MECH-342 release actuator, own recover integrator, V3-minimal-gated, NOT SD-011),
plus the existing **blocked_agency** (`z_block`, V3-candidate) and **coercion/injustice** (V4 stub).
Each row carries its neighbour-differentiation.

**Status update 2026-06-05 (claims minted):** the three previously-unbacked streams now have
`claims.yaml` claims (all `candidate`, lit-grounded, mirroring the MECH-302 lit-pull precedent):
**MECH-353** blocked_agency / control-failure (`z_block`; V3, `v3_pending`, dep SD-029 + MECH-112 +
MECH-342 + ARC-016 + MECH-320, diff-from SD-011/SD-019b); **MECH-354** effort/fatigue stop-recover
(V3-minimal, `v3_pending`, SD-012 side, dep SD-012 + SD-048 + MECH-342 + ARC-078 + SD-017, NOT SD-011);
**MECH-355** soothing/comfort autonomic state-gain modulator (V4-social, `epistemic_category:
substrate_conditional`, dep MECH-219 + SD-012 + SD-032e, NOT 302/303/304/112). Relief + Safety keep
their existing claims (MECH-302 / MECH-303 / MECH-304). Coercion/domination/injustice (blocked-agency
Stream B) remains an un-minted V4 stub (no claim) -- it needs the V4 other-agent substrate first.
REMAINING (NOT done, gated): the V3 discriminative experiments for MECH-353 (blocked-action assert-vs-
withdraw) and MECH-354 (time-on-task disengage with rest-recovery), and the V4 design pass for the
MECH-355 update rule. claims.json rebuilt; validator clean.

## 8. Cross-references

- Raw: `docs/thoughts/2026-06-01_ProtoFeelings_implementation_timing.md`.
- Claims/docs: `affect_primitives.md`, MECH-112, SD-011, MECH-056, MECH-061, MECH-090, ARC-065,
  MECH-313/314, MECH-320, SD-017, SD-033/034.
- Clusters: `thought_intake_2026-05-31_musings_on_v4.md`, `evidence/calibration/calibration_debt_index.md`,
  `docs/thoughts/2026-06-04_attention_distributed_precision_selection.md` (the analogous unification note).
- Memory: `project_calibration_debt`, `feedback_psychosis_confabulation_distinction`.
