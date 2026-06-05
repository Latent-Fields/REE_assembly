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

## 7. Cross-references

- Raw: `docs/thoughts/2026-06-01_ProtoFeelings_implementation_timing.md`.
- Claims/docs: `affect_primitives.md`, MECH-112, SD-011, MECH-056, MECH-061, MECH-090, ARC-065,
  MECH-313/314, MECH-320, SD-017, SD-033/034.
- Clusters: `thought_intake_2026-05-31_musings_on_v4.md`, `evidence/calibration/calibration_debt_index.md`,
  `docs/thoughts/2026-06-04_attention_distributed_precision_selection.md` (the analogous unification note).
- Memory: `project_calibration_debt`, `feedback_psychosis_confabulation_distinction`.
