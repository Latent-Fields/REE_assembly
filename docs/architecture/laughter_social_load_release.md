# Laughter as cognitive-load release and inter-regime social signal

Status: SEED (candidate claims registered 2026-06-09; V4/V5, off the V3 critical path)
Source intake: [evidence/planning/thought_intake_2026-06-06_laughter_cognitive_load_social_reconfiguration.md](../../evidence/planning/thought_intake_2026-06-06_laughter_cognitive_load_social_reconfiguration.md)
Raw thought: [docs/thoughts/2026-06-06_laughter_cognitive_load_social_reconfiguration.md](../thoughts/2026-06-06_laughter_cognitive_load_social_reconfiguration.md)

This doc is the home for the two laughter claims that the 2026-06-06 intake added on top of
the existing respiratory-cluster laughter model. It is a **seed / boundary doc**, not a build
spec — there is no V3 substrate work implied here.

---

## Source-weight caution (read first)

The prompting article — Neuroscience News, "Laughter Rewires Brain Architecture and Lowers
Cognitive Load" — summarises a cross-disciplinary **popular-science synthesis** (Dr. Jacqueline
Harding, *The Brain That Loves to Laugh*, Routledge/Taylor & Francis), **not** a primary empirical
study. "Rewires brain architecture" is editorial framing for neuroplasticity + distributed
prefrontal activation, not a measured large-scale network-regime reconfiguration. The claims below
are **compass-level hypotheses**, registered at `candidate / substrate_conditional / v4` — they are
**not** backed by citable experimental evidence and must not be cited as such.

---

## What REE already owned

- **MECH-110** — Laughter is rapid repeated hypothesis-tag cycling: each forced exhalation is one
  E3 plan-sweep (MECH-107) that activates a threat-hypothesis tag and clears it on safe resolution;
  the pleasure is the affective signature of iterated safe-confirmation. Includes a V5-scoped social
  extension (group/contagious laughter = respiratory phase-reset synchronising E3 plan-sweep clocks
  across agents). Home: `control_plane_heartbeat.md`.
- Respiratory cluster **MECH-107** (exhalation = plan-sweep / trajectory-abandonment), **MECH-108**
  (respiratory rhythm = E3 plan-sweep oscillator).
- Modes cluster **ARC-016** (modes ARE control-plane regimes on the precision-to-commitment circuit),
  **MECH-027** (pathological modes = mis-tuned regimes). Home: `modes_of_cognition.md`.
- Play-mode cluster **ARC-049/050 / INV-058–060 / MECH-194–199 / Q-035** — laughter appears in the
  basic-expression catalog as a bilateral frame-opening signal. **Substrate-blocked in V3**
  (no `play_frame_tag`); do not queue probes against it.

The central idea of the intake (laughter = rapid threat→safe-resolution reframe, incl. social
synchrony) is therefore **already owned**. A new laughter claim restating it would duplicate MECH-110.

---

## What is new (the two registered claims)

### MECH-364 — laughter discharges E3 conflict load and marks an inter-regime boundary

`mechanism_hypothesis · candidate · substrate_conditional · v4 · v4_v5`
depends_on: MECH-110, MECH-107, ARC-016, MECH-027, MECH-076

MECH-110 is the **micro** mechanism (per-cycle tag-clear). MECH-364 is the **macro/regime-level**
consequence: the cumulative effect of iterated safe-confirmation is a drop in E3 active
constraint/conflict pressure — a regime-level **load discharge** — and that discharge is what
marks/enables a *safe transition between control-plane regimes* (ARC-016): from threat-vigilant /
high-commitment to exploratory / play.

Mapping the intake's primitive
`laughter_event = f(conflict_detected, threat_reclassified, social_safety, reframe_success, load_release, shared_alignment)`:
`load_release` + the regime-boundary role → MECH-364; per-cycle `reframe_success`/tag-clear →
MECH-110; `shared_alignment` → MECH-110's V5 social-synchrony extension.

**Failure taxonomy (predictions).** A system that cannot run reframe → load-release → regime-re-open
cannot soften rigid commitments after a benign reframe → attractor lock-in (MECH-076),
pathological-regime persistence (MECH-027), social-threat overclassification, feedback entrapment,
belief fixation, excessive literalism.

**Substrate note / V3 reconsideration fork.** `load_release` needs an E3 conflict/constraint-load
readout. ARC-016 already exposes an E3-derived prediction-variance signal *in V3* — so a V3 substrate
check could reclassify MECH-364 toward `implementation_phase: v3`. Held at v4/substrate_conditional
pending that check. **Do not build or queue a probe in V3** until routed by an explicit version
decision; a probe before the readout exists would be vacuous (cf. the play-mode cluster).

### Q-059 — crying analogue + laughter repair-vs-damage adjudication

`open_question · candidate · substrate_conditional · v4 · v4_v5`
depends_on: MECH-110, MECH-364

REE owns a laughter mechanism (MECH-110, MECH-364) but **no crying / tears / sobbing claim** exists
(only "distress vocalisation" inside the play-mode catalog, INV-058). The raw thought pairs laughter
with crying as the two halves of a social-release axis. Open questions: (a) does the high-arousal /
distress-signal counterpart deserve its own claim? (b) how is the *valence* of social laughter
adjudicated — when does it repair the social field vs damage/exclude? — given that laughter is **not
monotone-affiliative** (it can exclude, dominate, mask distress, or signal threat). Set
`substrate_conditional` explicitly so `narrow_open_question` does not fire — V4/V5-parked, awaiting a
social substrate, not a V3-tractable question.

---

## Deliberately NOT registered

- **A restated laughter mechanism** — already MECH-110.
- **The social-synchrony / contagious-laughter strand** — already MECH-110's V5 extension.
- **The play-mode transition strand** — already the ARC-049/050 cluster (substrate-blocked).
- **The non-affiliative dark side as a standalone assertion** — folded as a caveat on MECH-364 and as
  the motivating tension inside Q-059, rather than its own claim, to avoid over-registration.

## Known cost

`substrate_conditional` is **not** in the workset proposal-suppress set on its own, but
`implementation_phase: v4` + `version_relevance: v4_v5` are now suppressed from the /queue-experiment
proposal lane (IGW `_is_deferred_beyond_v3`, landed 2026-06-09). So MECH-364/Q-059 should not surface
as V3 experiment proposals. If one does, it is a **blocked_substrate STOP** (play-mode-cluster
pattern) — do not queue a probe until a version decision routes this to a build.
