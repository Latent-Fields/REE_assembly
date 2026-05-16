# Play Substrate Design

**Status:** Draft — 2026-05-16
**Architect session:** play-substrate-design-2026-05-16T115621Z
**Depends on:** play_mode.md, developmental_curriculum.md, developmental_needs_register.md
**Registered claims:** MECH-194–199, ARC-049, INV-058–060, Q-035 (resolved), Q-048–Q-051, MECH-327, MECH-328, ARC-073
**Follow-on lit-pulls:** targeted_review_infant_play_contingency, targeted_review_ethological_play_signals (2026-05-16)

---

## 0. Framing Constraint

Play is **commitment-training infrastructure**. It is not reward shaping. The design purpose
of every play phase is to let E3's commitment architecture accumulate training signal under
conditions where the consequences of strategy selection are real (full gradient flow) but the
costs of bad strategies are bounded (no permanent harm, no real homeostatic depletion). Once
this is understood, every design decision follows from it: synthetic signals must be calibrated
not to make play feel rewarding but to give E3 a training target that is structurally similar
to real goal/harm signals.

---

## 1. Literature Evidence Summary

Seven targeted literature pulls were conducted before this design was written. Key
cross-cutting findings:

### 1.1 Harm Signal Architecture During Play (Critical Clarification)

**Finding (Panksepp 1998 PLAY system; Bekoff 1995 canid signals):** Harm signals are NOT
suppressed during play. The PLAY system (PAG-thalamus-frontal, opioid-modulated) RAISES the
threshold at which physical contact escalates from play-tagged to FEAR/RAGE. Harm signals
remain active and evaluated throughout; only the escalation criterion is shifted.

**Implication for MECH-194:** The current formulation "synthetic z_harm signals" is
under-specified. The architecture is "active but threshold-shifted": during play, z_harm_s and
z_harm_a continue to fire on real events, but the frame tag modifies the threshold for
commitment-gate escalation. Completely suppressing harm signals during play would break
calibration permanently.

### 1.2 Frame Maintenance is Continuous, Not Event-Only

**Finding (Bakeman & Adamson 1984; Bekoff 1995; Galbusera et al. 2017):** Biological play
uses three signal layers:
1. **Frame-open event** (play bow initiation, bilateral ratification)
2. **Continuous low-cost background signal** (play face, body orientation) — runs throughout
3. **Ambiguity-triggered explicit repair** — deployed specifically when an action could be
   misread as real harm (e.g., borrowing predatory motor pattern during chase play)

The frame is not maintained by the open/close events alone. The continuous background signal
is what sustains the context tag across the episode.

**Implication for ARC-049:** The bilateral frame has three component signals, not one.

### 1.3 Synthetic z_goal Must Encode Learning Progress

**Finding (Oudeyer et al. 2007 IAC; Andersen et al. 2022; Baldassarre 2019; Poli et al. 2025
Child Dev):** Children and computational systems trained with competence-based intrinsic
signals (d(prediction_error)/dt) outperform those with flat or knowledge-based (raw PE)
signals. The correct proxy for play drive is learning progress: d(PE_E1)/dt.

**Implication for MECH-194:** Synthetic z_goal must be learning-progress-weighted, not flat
or entropy-based. Flat synthetic z_goal will produce monostrategy attraction in play phase.

### 1.4 Strategy/Calibration Dissociation is Incommensurable by Construction

**Finding (Schmidhuber 2010 Formal Theory; Lynch et al. 2020 Play-LMP; Forestier et al. 2022
IMGEP):** Intrinsic drives are derivative signals (rate of change of knowledge/competence);
extrinsic drives are absolute value signals. They are formally incommensurable — not merely
quantitatively mismatched. This is why play-trained policy structure transfers cleanly while
magnitude calibration does not: there is no common currency to contaminate.

**Implication for MECH-195:** Adds formal grounding. The dissociation is structural, not
coincidental. This also explains why play-to-real transition does not require active
recalibration: the real homeostatic signal introduces a new currency that automatically
dominates the derivative play signal as play drive saturates.

### 1.5 Mode Transition Criterion: Competence Saturation

**Finding (Pezzulo/Santucci 2014; Forestier/IMGEP 2022):** Computational systems
self-terminate the play phase when the competence-based drive saturates — when d(PE)/dt
approaches zero across all reachable state regions. Scheduled transitions underperform
saturation-triggered transitions.

**Implication:** The play-to-real transition criterion is not a fixed episode count or
curriculum schedule. It is competence saturation: the play drive should decay when the
learning progress signal flattens. Real homeostatic drives (z_goal_real, drive depletion) then
naturally dominate.

### 1.6 Goal-Space Continuity Across Modes

**Finding (Colas et al. 2022 Autotelic Agents JAIR):** If play goals and real goals are
encoded in disjoint latent spaces, transfer fails silently: the agent reaches a real goal
state but the latent encoding does not match. The policy trained during play cannot be
directed toward real goals.

**Implication:** z_goal_synthetic and z_goal_real must lie in the SAME latent manifold. This
is a structural constraint on goal-space design, not just a magnitude constraint.

### 1.7 Pretend Play Tags Are Dissociable

**Finding (Kuhn-Popp et al. 2013 ERP; Rutherford & Rogers 2003 autism):** Pretense reasoning
and false-belief reasoning show distinct ERP signatures, and autism produces selective
impairment of ToM-linked pretense without equivalent EF impairment. This empirically supports
the REE two-tag decomposition: ARC-049 (play frame, bilateral, behavioral level) and MECH-094
(hypothesis tag, agent-internal, metarepresentational level) are distinct mechanisms.

### 1.8 Frame Mismatch is Worse Than Absence

**Finding (Ham, Szabo et al. 2024 Dev Psychobiol):** Pairing low-playing rats with
high-playing peers produces worse developmental outcomes than same-strain low-play pairing.
Frame complexity mismatch disrupts rather than scaffolds development.

**Implication for MECH-199/ARC-047:** The harness must calibrate frame complexity to the
learner's current bilateral frame-maintenance capacity. Overshooting the learner is actively
harmful.

### 1.9 Joint Commitment Structure Emerges at ~3y

**Finding (Hamann et al. 2012; Warneken/Brownell group):** Peer-level bilateral frame
maintenance with genuine obligation structure (waiting for partner, role switching, repair on
partner failure) is not robust until age 3. The caregiver unilateral phase spans infancy to
~2.5y.

**Implication for MECH-199:** The MECH-199 caregiver transition timeline is calibrated to
this window. V3 proxy (experimenter = unilateral frame setter) maps to the infancy phase;
peer-level bilateral frame is V4.

---

### 1.10 Follow-On Lit-Pull: Infant Contingency Detection (2026-05-16)

*Sources: Tronick 1978, Murray & Trevarthen 1985, Striano et al. 2005, Gergely & Watson 1996,
Rochat et al. 1999, Ekas et al. 2012, Feldman 2007.*

**Convergent finding:** Continuous frame monitoring is operational from 2–3 months of age,
before any play type in the MECH-197 progression. What escalates across play types is the
CONTENT of what is monitored, not the monitoring architecture. This resolves Q-035 (closed)
and refines ARC-049 with two implementation constraints:

1. **Frame confidence is a decaying scalar** (Ekas 2012): Within-episode monitoring dynamics
   show progressive decline when contingency fails -- monitoring computes a continuously-updating
   frame-confidence signal with temporal decay, not a one-shot violation detector. Implement as a
   scalar restored by reciprocal exchange, decremented per monitoring cycle that returns no
   contingency.

2. **Play frame signals must be "marked"** (Gergely & Watson 1996): The contingency-detection
   module distinguishes marked (perceptibly distinct) from unmarked signals. ARC-049's frame
   signal must be perceptibly different from ordinary behavior for the monitoring system to use
   it. This is a concrete design constraint: `play_frame_open_signal` must be qualitatively
   distinct from normal step outputs, not just a flag toggle in latent state.

**Suggested new MECH (not yet registered):** A MECH for the contingency-detection module as the
biological substrate of frame monitoring -- grounding it in the Gergely-Watson mechanism and the
Feldman 2007 oscillator biology (synchrony has physiological precursors in neonatal oscillator
systems). Would link play frame monitoring to REE's sleep/oscillator thread (INV-049).

### 1.11 Follow-On Lit-Pull: Ethological Play Signals (2026-05-16)

*Sources: Bekoff 1995, Byosiere et al. 2017, Davila-Ross & Palagi 2022, Nolfo & Palagi 2022,
Palagi 2011, Palagi 2024, Waller et al. 2012, Wenig et al. 2021.*

**Convergent finding across 8 species spanning mammals and corvids:**

1. **L2 background signal is universal and graded, not binary** (Waller 2012 gorilla; Nolfo &
   Palagi 2022 hyena): The background signal (open-mouth play face, hyena "happy face") varies
   in intensity as play intensity changes. Standard = frame open at baseline; elevated = higher
   play intensity. Frame confidence is not binary — it is graded. This converges with Ekas 2012
   from the infant lit-pull. Both implementation constraints point to the same architecture:
   frame confidence should be implemented as a continuous scalar.

2. **L3 fires at pause-reinitiation, not only ambiguity** (Byosiere 2017, refines Bekoff 1995):
   In domestic dogs, play bows occur primarily after pauses in play, functioning to reinitiate
   rather than repair imminent misread. This extends L3's functional role: it fires whenever
   the background monitoring signal detects a disruption (ambiguous action OR pause) — a broader
   trigger than the original Bekoff punctuation framing. Implement: L3 trigger condition =
   `P(misread | current_action) > threshold OR frame_confidence_drop > reinitiation_threshold`.

3. **Universal across taxonomy** (Palagi 2024 dolphins; Wenig 2021 ravens): Dolphins (90 MY
   divergence from terrestrial mammals) and ravens (320 MY from mammals) both exhibit the L2
   background signal (open-mouth play face, play-specific vocalizations/movements). The
   architecture predates the mammalian lineage split, confirming it is not a primate-specific
   elaboration. This raises the generalizability confidence for ARC-049 to cross-substrate level.

4. **Play signal competence has a developmental trajectory** (Palagi 2011 gelada): Immature
   animals use only L2 (simpler background signal); adults add L3 (explicit repair/reinitiation
   signals). This mirrors the caregiver → peer transition in MECH-199 and implies that L3
   competence is acquired through play experience, not present from birth.

---

## 2. Literature Evidence Mapping Table

| Source | Finding | Action | Claim IDs | DEV-NEED IDs |
|---|---|---|---|---|
| Panksepp 1998; Bekoff 1995 | Harm signals active but threshold-shifted during play; not suppressed | Refines MECH-194 | MECH-194, ARC-049 | DEV-NEED-009 |
| Bakeman 1984; Bekoff 1995; Galbusera 2017 | Three-level frame signal: open / continuous background / ambiguity-repair | Refines ARC-049 | ARC-049, INV-059 | DEV-NEED-009, 014 |
| Oudeyer 2007; Andersen 2022; Baldassarre 2019 | Synthetic z_goal must be learning-progress-weighted (d(PE)/dt), not flat | Refines MECH-194 | MECH-194, MECH-195 | DEV-NEED-009, 010 |
| Schmidhuber 2010; Lynch 2020; Forestier 2022 | Strategy/calibration dissociation incommensurable by construction | Refines MECH-195 | MECH-195, INV-058 | DEV-NEED-009 |
| Pezzulo 2014; Forestier 2022 | Play-to-real transition = competence saturation, not schedule | Suggests missing claim | ARC-050 | DEV-NEED-009 |
| Colas 2022 | z_goal space must be continuous across play and real modes | Suggests missing claim | MECH-194, ARC-050 | DEV-NEED-009 |
| Stahl & Feigenson 2015; Schulz & Bonawitz 2007 | PE locus in E1 should upweight probe-action selection, not just global curiosity | Suggests missing MECH | MECH-194, MECH-195 | DEV-NEED-010 |
| Libertus & Needham 2010 | DEV-NEED-010 exit = joint E1+E2 competence, not E1 alone | Refines DEV-NEED-010 | MECH-196 | DEV-NEED-010 |
| Weisberg 2013/2016 | Guided play (scaffolded goal difficulty) outperforms free or directed play | Suggests impl metric | MECH-194, MECH-197 | DEV-NEED-009 |
| Piaget 1952 | Tertiary circular reactions = systematic variation; sensorimotor play exit criterion | Supports/refines | MECH-195 | DEV-NEED-010 |
| Kuhn-Popp 2013; Rutherford 2003 | Pretense and false-belief use distinct neural substrates; supports two-tag decomposition | Supports | MECH-198, MECH-094, ARC-049 | DEV-NEED-012 |
| Leslie 1987 | Decoupling (PRETEND operator) = hypothesis tag; structurally equivalent | Supports | MECH-198, MECH-094 | DEV-NEED-012 |
| Buchsbaum 2012 | Pretend play and counterfactual reasoning share causal machinery (r=0.38 after EF ctrl) | Supports | MECH-198, MECH-094 | DEV-NEED-012 |
| Francis 2023 | Shared imaginative capacity latent factor; EF accounts for unique variance | Supports | MECH-198 | DEV-NEED-012 |
| Vasilopoulos 2026 | Pretend play at 2-3y predicts mental health at 4-7y; emotion reg does not mediate | Supports MECH-200/201 | MECH-200, MECH-201 | DEV-NEED-012 |
| Rakoczy 2008 | 2-3y distinguish game-constitutive violations; bilateral normative enforcement | Supports | Q-035, ARC-049, INV-059 | DEV-NEED-013 |
| Ham 2024; Ham 2026 | Quality of reciprocal engagement, not quantity; mismatch worse than absence | Refines INV-059, MECH-199 | INV-059, MECH-199, ARC-047 | DEV-NEED-014, 016 |
| Pellis et al. 2023 | mPFC pruning via R&T; play deprivation -> FEAR hyperreactivity | Supports INV-058 | INV-058, ARC-049 | DEV-NEED-009 |
| Hamann 2012; Brownell group | Peer bilateral frame not robust until ~3y; caregiver phase necessary | Supports MECH-199 | MECH-199, ARC-047 | DEV-NEED-014, 016 |
| Galbusera 2017 | Social play: open/body/close three-phase structure | Refines ARC-049 | ARC-049, INV-059 | DEV-NEED-014 |
| Lynch 2020 Play-LMP | Task-agnostic play trains policy structure, not magnitude; full task transfer | Supports | MECH-194, MECH-195, INV-058 | DEV-NEED-009 |
| Caselles-Dupre 2019 | Mode-tag failure causes gradient contamination in robotic systems | Supports MECH-094 | MECH-094, MECH-194 | DEV-NEED-009 |
| Pezzato 2022 | Competitive drive dynamics produce natural mode-switching without schedule | Suggests ARC claim | ARC-050, MECH-194 | DEV-NEED-009 |
| Tronick et al. 1978 | Still-face paradigm: 3-4 month infants respond within-episode to contingency violation, not just at boundaries | Resolves Q-035 (monitoring primitive) | Q-035 (resolved), ARC-049, INV-059 | DEV-NEED-010 |
| Murray & Trevarthen 1985 | Double-video: 2-month temporal contingency detection; isolates timing from content | Resolves Q-035 | Q-035 (resolved), ARC-049 | DEV-NEED-010 |
| Striano et al. 2005 | 1-month: no discrimination; 3-month: full discrimination of contingency conditions | Pins monitoring onset to 1-3 months | MECH-197, ARC-049 | DEV-NEED-010 |
| Ekas et al. 2012 | Within-episode progressive bidding decline during SFP; frame confidence is a decaying scalar | Refines ARC-049 implementation | ARC-049, Q-035 (resolved) | DEV-NEED-010 |
| Gergely & Watson 1996 | Contingency-detection module; play signals must be "marked" (perceptibly distinct) | Design constraint: ARC-049 frame signal must be qualitatively distinct | ARC-049 | DEV-NEED-010 |
| Feldman 2007 | Parent-infant synchrony grounded in neonatal oscillators; predicts self-reg, empathy; failure -> psychopathology | Links play frame to INV-049 oscillator thread; strengthens INV-059 | ARC-049, INV-059 | DEV-NEED-015 |
| Bekoff 1995 | Play bow: non-random placement before/after agonistic actions; L3 punctuation not L2 background | Three-level architecture: L1/L2/L3 distinct | ARC-049, Q-035 (resolved) | DEV-NEED-009 |
| Byosiere et al. 2017 | Play bow fires at pause-reinitiation in adult dogs, not just ambiguity; refines Bekoff | L3 trigger = ambiguity OR pause (frame confidence drop) | ARC-049 | DEV-NEED-009 |
| Nolfo & Palagi 2022 | Hyena "happy face" (continuous) dissociates from snapping (L3); clear L2/L3 split | Strongest species-level L2/L3 dissociation | ARC-049 | DEV-NEED-009 |
| Waller et al. 2012 | Gorilla play face is graded (teeth exposure = intensity); background signal is scalar | Frame confidence scalar confirmed | ARC-049 | DEV-NEED-009 |
| Palagi 2024 | Dolphin open-mouth play face + mimicry (90 MY divergence from terrestrial mammals) | L2 background signal universal mammalian feature | ARC-049 | DEV-NEED-009 |
| Wenig et al. 2021 | Raven play emotional contagion via play sounds (320 MY from mammals) | L2 background architecture predates mammal-bird split | ARC-049 | DEV-NEED-009 |
| Palagi 2011 | Gelada: immatures use only L2; adults acquire L3; competence developmental | Play signal competence acquired through experience (MECH-199 analogue) | ARC-049, MECH-199 | DEV-NEED-009 |

---

## 3. Q-035 Resolution: Minimal Frame Signal Architecture

**Q-035 (RESOLVED 2026-05-16):** Is a single bilateral open/close tag sufficient, or does ongoing
exchange need to be sustained?

### 3.1 Resolution

**The original framing was incorrect.** Q-035 was premised on a model where the monitoring
architecture *escalates* across play types — from open/close only at simple types to continuous
heartbeat at complex types. Follow-on lit-pulls on infant contingency detection (Tronick 1978,
Murray & Trevarthen 1985, Fantasia 2014) and ethological play signals (Bekoff 1995) establish
that this is wrong.

**Correct resolution:** Continuous bilateral monitoring is a PRIMITIVE CAPACITY present from
2–3 months of age — before any named play type begins. What escalates across play types is
the **CONTENT COMPLEXITY** of the shared state being monitored, not the monitoring architecture.

| Play type | Monitoring architecture | Content being monitored |
|---|---|---|
| Sensorimotor | L1 (open/close) + L2 (continuous background) — BOTH present from infancy | "Is partner still contingently responding?" |
| Constructive | L1 + L2 | "Is compositional goal still shared?" |
| Pretend | L1 + L2 + both hypothesis_tag and play_frame_tag co-active | "Are both decoupling layers simultaneously maintained?" |
| Games with rules | L1 + L2 + L3 (repair at violations) | Dual-level: rule compliance AND strategic rationality (Schmidt 2015) |
| Cooperative | L1 + L2 + L3 from BOTH parties | Full bilateral role/goal state + repair at role ambiguity |

**Three-level signal architecture (Bekoff 1995):**
- **L1 (discrete boundary signals):** play bow / play-face onset — open/close markers
- **L2 (continuous background signal):** ongoing play face, body orientation — absence is itself a violation signal
- **L3 (repair signals):** selectively deployed at ambiguity junctures (P(misread | action) > threshold) — NOT continuous

The three levels are present across all play types from the start. They are not invented at games-with-rules.

**Empirical grounding:**
- Tronick 1978 (still-face): 3-4 month infants respond to mid-episode contingency violations, not just episode boundaries
- Murray & Trevarthen 1985 (double-video): 2-month temporal contingency monitoring isolates timing from content
- Fantasia 2014: 3-month infants detect structural alterations to play routine mid-episode
- Bekoff 1995: three-level signal architecture in canid play regardless of play type

### 3.2 Sub-Questions (Q-048–Q-051)

Q-035 is resolved. The residual open questions concern what CONTENT needs to be monitored at each
play stage, not whether the monitoring architecture exists:

- **Q-048**: Is L2 background signal sufficient for sensorimotor/constructive content ("is partner still responding?"), or are L3 repair events also required? (V3-tractable)
- **Q-049**: Does pretend play require hypothesis_tag + play_frame_tag co-active **throughout** the episode, or only at moments of object substitution? (V3-tractable)
- **Q-050**: Do games-with-rules require per-step dual-level content monitoring (rule + strategic rationality simultaneously), or does turn-by-turn sequential sampling suffice? (V4 needed)
- **Q-051**: Does cooperative play require full L1+L2+L3 from BOTH parties, or can bilateral L1 alone maintain frame integrity? (V4 needed)

**V3 implementation:** The persistent `play_frame_tag` flag in `LatentState` already implements L2.
L1 = `frame_open` / `frame_close` events. L3 = ambiguity-repair triggered by
`P(misread | action) > ambiguity_threshold`. No architectural change needed for V3 degenerate case.
Q-048 and Q-049 are tractable in V3.

---

## 4. Synthetic Signal Specifications

### 4.1 z_goal_synthetic

**Manifold requirement:** z_goal_synthetic MUST lie in the same latent space as z_goal_real
(the real homeostatic goal attractor). If they occupy disjoint spaces, policy trained in play
mode cannot be directed toward real goals post-play (Colas 2022 failure mode).

**Signal profile:**

```
z_goal_synthetic = f_LP(z_world_current) * direction_vector_synthetic
```

Where:
- `f_LP(z_world_current)` = learning progress weight = d(E1_PE)/dt at current state region;
  positive when PE is being reduced, near-zero when mastered or irreducibly noisy
- `direction_vector_synthetic` = a target direction in z_goal space; for sensorimotor play this
  is a sampled outcome; for constructive play this is a goal configuration; for pretend play
  this is a role-defined objective

**GoalConfig extension (V3 proxy):**
```python
play_mode: bool = False               # new flag
z_goal_synthetic_vector: Optional[Tensor] = None   # seeded by experimenter
z_goal_synthetic_magnitude: float = 1.0           # matches real drive_weight=2.0
learning_progress_weight: float = 1.0             # scales learning-progress signal
play_harm_threshold_shift: float = 1.5            # multiplier on z_harm escalation threshold
```

**Decay on play-frame close:** z_goal_synthetic must decay to zero within one episode after
play_frame_tag is cleared (MECH-196). The real z_goal attractor then reasserts. This is
already partially implemented via z_goal_inject=0.0 default behavior — play mode sets
z_goal_inject to the synthetic value, clears it on frame close.

### 4.2 z_harm_synthetic

**Architecture:** z_harm_s and z_harm_a are NOT suppressed during play. They remain active
and fire on real environmental events. The play_frame_tag modifies a single parameter:
`play_harm_threshold_shift` — a multiplier on the threshold at which harm signal magnitude
triggers commitment-gate escalation. This is the opioid-modulation analog.

**During play:**
```
effective_escalation_threshold = base_escalation_threshold * play_harm_threshold_shift
```

Real severe harm (magnitude >> shifted threshold) still triggers emergency exit. The play
frame does not authorize unlimited harm tolerance — it shifts the calibration point for what
counts as play-normal contact vs. genuine damage.

**Synthetic harm events:** For pretend play and games-with-rules, synthetic harm events can
additionally be injected (role-defined damage, rule-violation consequences). These are tagged
with `synthetic=True` in the harm event record so post-play recalibration can exclude them
from real-harm statistics.

### 4.3 Calibration Protection

After play episode close:
1. `z_goal_inject` cleared → real drive level reasserts
2. `play_harm_threshold_shift` reset to 1.0 → base escalation threshold restored
3. Synthetic harm events excluded from calibration statistics (they do not update z_harm
   magnitude calibration)
4. MECH-195: policy structure (E3 trajectory selection weights) IS retained — this is the
   intended transfer

---

## 5. Frame Mechanics Specifications

### 5.1 Frame Open

**Signal:** Set `play_frame_tag=True` in agent context state. In V3 proxy, experimenter
calls `env.set_play_mode(True)`.

**Required bilateral acknowledgment:** In V3 (degenerate case), experimenter is the bilateral
partner — acknowledgment is implicit in env API call. In V4, bilateral acknowledgment requires
partner to confirm frame before play proceeds. Frame without bilateral acknowledgment = invalid
(INV-059).

**Warm-up period:** Before play_frame_tag is set, a brief context-establishment period
(analogous to warm-up play in Ramani/Brownell data) is recommended. This primes the agent's
partner model and reduces frame initiation cost with novel partners.

### 5.2 Continuous Frame Maintenance (Play Types 3-5)

For pretend play and above, a **continuous background signal** must be maintained throughout:

**V3 proxy:** `play_frame_tag` persists in context state throughout the episode. The
experimenter does not need to re-signal it, but the monitoring infrastructure checks for
dropout every N steps and raises a `FrameDropoutWarning` if play_frame_tag is cleared without
an explicit frame-close event.

**Signal architecture (per Bekoff 1995 three-level):**

| Signal type | Cost | When deployed | V3 implementation |
|---|---|---|---|
| Frame-open | High (commitment) | Episode start | `play_frame_tag=True` event |
| Background maintenance | Low (continuous) | Throughout episode | Persistent flag; checked each decision step |
| Ambiguity-repair | Medium (explicit) | When action could be misread | Frame reaffirmation event; resets background signal counter |

### 5.3 Frame Failure Conditions

A play episode is considered **frame-failed** under any of:

1. **Unilateral assertion**: Agent sets play_frame_tag=True without bilateral acknowledgment
   (V4 violation; V3 proxy: experimenter fails to set env play mode)
2. **Signal dropout**: play_frame_tag clears mid-episode without explicit frame-close
3. **Frame confusion**: Agent executes commitment-gated action while play_frame_tag=True
   (MECH-200 risk: real-reads-as-synthetic); OR agent executes learning suppression
   (hypothesis_tag=True) while play_frame_tag=True without the two co-operating correctly
   (pretend play confusion)
4. **Calibration leakage**: Post-play z_goal magnitude distribution shifts toward synthetic
   magnitude (detectable via KL divergence metric; see Section 7)
5. **Frame overflow**: Harm event magnitude exceeds emergency threshold even under
   `play_harm_threshold_shift`; triggers MECH-196 immediate frame collapse and real-signal
   re-entry

### 5.4 Frame Repair Mechanisms

After frame failure:
- **Minor failure (dropout, ambiguity)**: Both parties re-issue frame-open; brief
  context-reestablishment period; episode may continue
- **Moderate failure (commitment confusion)**: Episode terminates; frame repair requires
  explicit re-acknowledgment before new episode
- **Severe failure (calibration leakage)**: Real-signal recalibration episode required
  before next play; drive parameters reset to pre-play baseline
- **Emergency exit (harm overflow)**: MECH-196 triggers immediately; z_harm recalibration;
  play phase suspended until harm calibration stabilizes

### 5.5 Frame Close

**Signal:** `play_frame_tag=False` event with bilateral acknowledgment.

**Post-close sequence:**
1. `z_goal_synthetic` decay begins (one episode to zero)
2. `play_harm_threshold_shift` = 1.0
3. Synthetic harm events flagged; excluded from calibration update
4. E3 policy weights retained (this is the training transfer — do not reset)
5. Drive depletion: real homeostatic drive begins applying; synthetic z_goal compete weaker

---

## 6. Per-Play-Type Minimal Viable Implementations

### 6.1 Sensorimotor Play

**Developmental analogue:** 0-18 months; primary/secondary/tertiary circular reactions

**Prerequisite developmental needs:** None (play entry point). Basic E1 world-model
initialization required; E2 transition model functional.

**Trained subsystems:**
- E1: Prediction accuracy across action space; action-outcome associations
- E2: Motor-mapping quality; transition model stability
- Joint: Action selection drives toward E1 prediction-error-rich regions (probe-action
  selection)

**Synthetic signals:**
- z_goal_synthetic = outcome-space target sampled near E1 prediction error peak
  (goal-babbling variant); weighted by learning progress d(PE_E1)/dt
- No synthetic harm events; real environment constraints provide natural limit
- play_harm_threshold_shift = 1.0 (no threshold shift; no social harm context)

**Frame mechanics:** Open/close only. Experimenter (V3) sets play_mode=True. No bilateral
state tracking required. No continuous background signal.

**Gate criteria (DEV-NEED-010 exit):**
- E1 prediction accuracy > 0.85 on held-out novel action set (actions not trained)
- E2 transition stability (variance of rollout error < threshold) over held-out action set
- Both must be met simultaneously (Libertus/Needham joint criterion)
- Equivalently: d(PE_E1)/dt < saturation threshold across all reachable state regions
  (Pezzulo competence saturation)

**Expected failure modes:**
- Monostrategy: flat synthetic z_goal produces locally optimal but globally narrow motor
  repertoire; detected by action-diversity metric
- Stalled exploration: PE-based (not LP-based) synthetic z_goal stalls in high-variance
  irreducible regions

**V3 proxy:** `play_mode=True` config flag; learning-progress-weighted z_goal injection via
GoalConfig.z_goal_inject; standard CausalGridWorld env.

**V4 requirements:** None additional — sensorimotor play is the simplest tier.

**Possible V3 experiment:** Compare flat vs. learning-progress-weighted synthetic z_goal on
joint E1+E2 competence at gate. Predicted: LP-weighted outperforms flat on E2 stability;
flat produces monostrategy.

---

### 6.2 Constructive Play

**Developmental analogue:** 18 months onward; overlaps with symbolic play

**Prerequisite developmental needs:** Sensorimotor play gate passed; stable z_world object
representations.

**Trained subsystems:**
- E3: Multi-step sequential goal pursuit; sub-goal sequencing
- E2: Longer-horizon rollout accuracy (>15 step plans)
- E1: Object-configuration prediction; causal structure of multi-step sequences

**Synthetic signals:**
- z_goal_synthetic = target configuration in z_world (a goal state to reach via sequence of
  actions); persists across episode (slow attractor, alpha_goal = 0.02 for persistence)
- Intermediate benefit fires on correct sub-goal completion (synthetic benefit events)
- No harm events by default; optional obstacle/constraint injection for constructive
  challenge

**Frame mechanics:** Open/close only (as sensorimotor). Caregiver/experimenter may MODIFY
the synthetic goal mid-episode (adding complexity) — this is the "guided play" intervention
(Weisberg). V3: experimenter updates z_goal_synthetic_vector via env API.

**Gate criteria (DEV-NEED-011 exit):**
- E3 successfully completes 5-step goal-directed sequences with <20% step failure rate
- E2 rollout accuracy at horizon 15 steps (mean squared error on z_world prediction)
- Goal drift metric: z_goal attractor persists against conflicting z_world for full episode

**Expected failure modes:**
- Goal drift: weak goal attractor fails to maintain objective across distracting steps
- Step-by-step reactivity: agent reacts locally rather than planning ahead (E3 trajectory
  selection immature)
- Subgoal binding failure: agent achieves subgoal states but does not chain them toward
  the synthetic target

**V3 proxy:** Multi-step synthetic goal injection; CausalGridWorld path-finding challenge;
GoalConfig.alpha_goal tuned for persistence.

**V4 requirements:** None beyond V3.

---

### 6.3 Pretend Play

**Developmental analogue:** 18 months - 4 years; first use of hypothesis_tag outside sleep
replay

**Prerequisite developmental needs:** Constructive play gate; hypothesis_tag (MECH-094)
functional; play_frame_tag available. Executive function substrates for dual representation.

**Trained subsystems:**
- E3 commitment architecture in SYNTHETIC MODE: full commitment cycle (deliberation, commit,
  post-commit tracking) with synthetic consequences
- hypothesis_tag + play_frame_tag co-activation (MECH-198 mechanism)
- Dual representation maintenance: primary (real world state) + synthetic (play role state)
  held simultaneously without confusion
- Real/synthetic distinction capacity (training against MECH-200/201 failure modes)

**Synthetic signals:**
- z_goal_synthetic = ROLE-DEFINED objective (not arbitrary; must be narratively coherent
  within the pretend context — e.g., "agent is a rescuer; goal = reach distressed target")
- z_harm_synthetic = role-defined harm events (the pretend bear bites back; the doctor's
  patient reacts to treatment) — these fire as synthetic harm signals, tagged accordingly
- Real harm signals: REMAIN ACTIVE with play_harm_threshold_shift applied
- Key distinction from simulation (hypothesis_tag alone): in pretend play, E3 executes
  REAL commitment decisions (not rollout) toward synthetic targets. Post-commit channel IS
  open. Gradient flows through real commitment decisions evaluated against synthetic outcomes.

**Frame mechanics (PERSISTENT — not open/close only):**
- hypothesis_tag=True AND play_frame_tag=True must co-exist throughout
- Frame monitoring infrastructure checks both tags each decision step
- Either tag dropping without explicit close = frame confusion event (logged)
- V3 proxy: experimenter sets both tags at episode start; monitoring middleware checks per step

**Gate criteria (DEV-NEED-012 exit):**
- Agent maintains consistent synthetic goal against conflicting real observations for >20
  consecutive decision steps
- Real commitment architecture exercised in play: E3 deliberation cycle completes, commitment
  fires, post-commit tracking runs — all with synthetic targets
- False commitment rate in play < 0.10 (agent commits without full E3 deliberation cycle)
- Frame confusion rate (tag dropout without explicit close) < 0.05 per episode
- Post-play real calibration: z_goal magnitude distribution unchanged from pre-play baseline
  (KL < threshold) — confirms MECH-195 calibration isolation

**Expected failure modes:**
- Frame confusion (MECH-200): Real consequences treated as synthetic (agent ignores real
  harm because "this is just play")
- Frame confusion (MECH-201): Synthetic consequences treated as real (agent responds to
  pretend harm as if real)
- Tag dropout: hypothesis_tag or play_frame_tag clears mid-episode without explicit close
- Calibration leakage: synthetic signal magnitudes persist post-play (z_goal attractor
  shifts toward play targets)
- Commitment-suppression conflation: agent confuses play mode (learning authorized) with
  simulation mode (hypothesis_tag alone, learning suppressed)

**V3 proxy:** Dual-tag config; synthetic z_goal + z_harm injection; experimenter-maintained
bilateral frame. Monitoring middleware for tag co-activation check.

**V4 requirements:** Peer play partner for genuine bilateral hypothesis_tag co-operation.
In V3 proxy, experimenter maintains bilateral element.

**Possible V3 experiment (ablative, MECH-198):** Three conditions:
1. Full: hypothesis_tag=True AND play_frame_tag=True (MECH-198 intact)
2. Ablated-H: play_frame_tag=True only (play context without decoupling)
3. Ablated-P: hypothesis_tag=True only (simulation without play frame)
Predicted: condition 1 produces best strategy transfer + lowest frame confusion; conditions
2 and 3 each produce characteristic failure signatures.

---

### 6.4 Games with Rules

**Developmental analogue:** 4-7 years; rule-governed play emerges after stable pretend play

**Prerequisite developmental needs:** Pretend play gate; constraint satisfaction in E3;
turn-taking mechanism; inhibitory control (ability to suppress non-permitted moves).

**Trained subsystems:**
- E3: Constraint satisfaction under ongoing shared rule state; turn-taking
- Shared state monitoring: tracking current legal action set based on rule state
- Rule violation detection: detecting partner violations and own-violations
- Inhibitory control: suppressing moves that are valid actions but currently rule-prohibited
- Q-050 mechanism: per-step shared-state update

**Synthetic signals:**
- z_goal_synthetic = rule-defined objective (score, reach target, achieve winning condition)
- z_harm_synthetic = rule-violation events (fire on violation, whether own or partner's)
- z_benefit_synthetic = rule-completion events (fire on goal state or scoring)
- Rule state maintained as structured data parallel to z_world (not inside z_world); rule
  violations detectable without world-model inference

**Frame mechanics (ONGOING SHARED-STATE MONITORING):**
- Frame is NOT just "we are playing" but "we are playing WITH THESE ACTIVE CONSTRAINTS"
- Rule state must be updated and shared each decision step
- Shared state: `{current_turn: agent/partner, legal_moves: list, game_state: dict,
  violation_history: list}`
- Violation detection fires harm_synthetic and triggers frame-repair protocol
- V3 proxy: Experimenter maintains rule state; agent reads legal_moves from env obs;
  violation events injected by experimenter

**Gate criteria (DEV-NEED-013 exit):**
- Agent detects own rule violations reliably (>90%) and self-corrects
- Agent detects partner violations reliably (>80%) and issues repair signal
- Constraint satisfaction: <10% illegal moves per episode
- Turn-taking: no move on partner's turn without explicit permission (inhibitory control)
- Rule inference: agent can generalize to novel rule variants not seen in training

**Expected failure modes:**
- Rule amnesia: agent forgets constraint state mid-episode (E3 shared-state capacity
  insufficient)
- Constraint collapse: under adversarial conditions, agent reverts to unconstrained policy
- Frame-to-rule binding failure: agent knows the frame is active but does not internalize
  constraints as normative (treats rules as suggestions not obligations)
- Turn confusion: agent moves on partner's turn (inhibitory control failure)

**V3 proxy:** Structured rule-state obs; experimenter-injected violation harm; legal_moves
set in obs; CausalGridWorld turn-taking variant.

**V4 requirements:** Genuine peer partner for bilateral rule enforcement and real Q-050
shared-state monitoring test.

---

### 6.5 Cooperative Play

**Developmental analogue:** 4+ years (peer-level bilateral frame capacity emerges ~3y)

**Prerequisite developmental needs:** Games-with-rules gate; partner model in E3 (agent can
represent and predict partner state); bilateral frame maintenance capacity.

**Trained subsystems:**
- Partner state prediction: E3 models partner's likely next action based on joint context
- Role coordination: agent selects actions that complement partner's role (not conflict)
- Joint commitment: both agents must commit to shared plan; neither can unilaterally exit
- Frame repair after partner failure: agent responds appropriately when partner fails

**Synthetic signals:**
- z_goal_synthetic = JOINT outcome (both agents must contribute; agent's portion insufficient
  alone)
- z_harm_synthetic = joint failure events (fires when either agent fails; responsibility
  shared)
- z_benefit_synthetic = joint success (fires ONLY when both agents' contributions land)
- Partner model prediction error: additional signal for updating E3's partner representation

**Frame mechanics (FULL BILATERAL ARC-049):**
- All three signal layers: frame-open (bilateral ratification), continuous background
  (partner-tracking signal per step), ambiguity-repair (when action could be misread)
- Warm-up episode: brief context-establishment before main episode (lowers frame-initiation
  cost with novel partner; Ramani/Brownell data)
- Frame-mismatch detection: if partner's frame complexity exceeds agent's current capacity,
  emit FrameMismatchWarning and downgrade to matched complexity (Ham 2024 constraint)
- V3 proxy: scripted partner (not genuine peer); experimenter-controlled partner actions

**Gate criteria (DEV-NEED-014 exit — V4 only):**
- Agent completes joint episodes with novel partner without warm-up
- Partner state prediction accuracy >70% across episode
- Frame repair successful after simulated partner failure (agent waits, issues repair,
  re-engages rather than abandoning)
- Joint success rate > matched-partner baseline

**V3 proxy only:** Simulated scripted partner; unilateral frame maintained by experimenter.
Cannot fully test bilateral frame capacity in V3 — DEV-NEED-014 is V4-gated.

---

## 7. Metrics Design

### 7.1 Strategy Transfer

**Definition:** Improvement in real-episode goal-pursuit performance (from pre-play baseline)
attributable to play-phase training, after controlling for calibration leakage.

**Measurement:**
1. Pre-play: measure E3 trajectory selection quality in real episodes (mean discounted
   return on real goal-directed tasks)
2. Play phase: N episodes of play mode
3. Post-play: measure E3 trajectory selection quality in real episodes
4. Transfer = post_play_performance - pre_play_baseline, partialling out calibration leakage

**Confound control:** calibration leakage (Section 7.2) must be measured simultaneously;
reported separately and partialled from transfer metric.

### 7.2 Calibration Leakage

**Definition:** Shift in real-episode z_goal magnitude distribution attributable to
synthetic signal contamination.

**Measurement:**
```
KL(z_goal_dist_post_play || z_goal_dist_pre_play)
```
Where distribution is computed over z_goal attractor magnitudes in real (non-play) episodes.

**Threshold:** Leakage < 0.05 nat (expected near zero if MECH-195 architecture is correct).

**Failure signature:** Leakage > 0.1 nat = synthetic magnitude contaminated real attractor;
trigger play pause and recalibration.

### 7.3 False Commitment

**Definition:** Rate at which E3 executes commitment-gated actions without completing the
full deliberation cycle during play.

**Measurement:** Proportion of commitment events where E3's deliberation cycle completed
(theta-cycles > threshold before commit) vs. truncated.

**Expected in play:** Similar to real-episode false commitment rate. Deviation = play mode
disrupting commitment architecture training (either suppressing deliberation or
short-circuiting).

### 7.4 Frame Confusion Index

**Definition:** Rate of MECH-200 and MECH-201 failure events during play.

**Sub-metrics:**
- `frame_confusion_200`: rate of real-consequence-as-synthetic errors (real harm treated as
  play harm) — detected by monitoring real z_harm_a response suppression while play_frame is
  active
- `frame_confusion_201`: rate of synthetic-consequence-as-real errors (play harm treated
  as real) — detected by emergency exits during play episodes where real harm is below
  threshold but synthetic harm is high

**Measurement period:** Per-episode fraction of steps showing confusion signature.

### 7.5 Synthetic-Real Leakage

**Definition:** Rate at which synthetic harm events update real harm calibration statistics
(MECH-195 isolation failure).

**Measurement:** Compare z_harm_a magnitude calibration before and after play episode;
specifically whether calibration update touched synthetic-tagged events.

**Expected:** Zero (synthetic events should be fully tagged and excluded from calibration
update). Any non-zero = calibration isolation failure.

### 7.6 Safe Counterfactual Experimentation Rate

**Definition (pretend play only):** Rate at which agent successfully completes counterfactual
"what if" interventions within the pretend frame without frame confusion or false commitment.

**Measurement:** In structured pretend play episodes with defined counterfactual intervention
points, fraction of interventions that:
- Complete the full counterfactual sequence
- Do not trigger frame confusion
- Return correctly to real-mode state after intervention

**Benchmark:** Should exceed real-episode counterfactual success rate (play provides safe
practice environment; success rate should be higher not lower).

---

## 8. Staged Implementation Roadmap

### Phase 0: Infrastructure (V3, no experiments)

Prerequisite before any play experiment:

- [ ] Add `play_mode: bool = False` and `play_harm_threshold_shift: float = 1.5` to GoalConfig
- [ ] Add `play_frame_tag` to LatentState (analogous to `hypothesis_tag` field)
- [ ] Extend env API: `env.set_play_mode(enabled: bool, synthetic_goal: Optional[Tensor])`
- [ ] Frame monitoring middleware: per-step check of play_frame_tag persistence; emit
  `FrameDropoutWarning` on unintended clear
- [ ] Extend harm event recorder: add `synthetic: bool` field; synthetic events excluded from
  calibration update
- [ ] Verify that z_goal latent space is continuous (play targets and real targets can be
  encoded in same manifold without disjoint regions)

### Phase 1: Sensorimotor Play Validation (V3)

- [ ] Implement learning-progress-weighted z_goal injection (proxy: d(PE_E1)/dt signal)
- [ ] Run EXQ-PLAY-001: flat vs. LP-weighted synthetic z_goal on sensorimotor gate metrics
- [ ] Validate joint E1+E2 exit criterion (both must pass simultaneously)
- [ ] Document sensorimotor play gate in developmental_needs_register.md

### Phase 2: Constructive Play (V3)

- [ ] Multi-step synthetic goal persistence (GoalConfig.alpha_goal tuning for constructive)
- [ ] Sub-goal benefit injection API
- [ ] Run EXQ-PLAY-002: multi-step constructive play with goal-drift monitoring
- [ ] Validate 5-step gate criterion

### Phase 3: Pretend Play Infrastructure (V3)

- [ ] Dual-tag monitoring (hypothesis_tag AND play_frame_tag co-activation check)
- [ ] Synthetic harm injection (role-defined harm events tagged synthetic=True)
- [ ] Frame confusion metrics instrumentation (MECH-200, MECH-201 logging)
- [ ] Run EXQ-PLAY-003: ablation of hypothesis_tag vs. play_frame_tag in pretend episodes
  (tests MECH-198; three-condition design from Section 6.3)
- [ ] Validate pretend play gate (calibration isolation, dual-tag persistence, false commit)

### Phase 4: Games-with-Rules (V3)

- [ ] Rule state data structure in env obs (legal_moves, current_turn, violation_history)
- [ ] Violation harm injection (rule violation fires z_harm_synthetic)
- [ ] Per-step rule-state update protocol
- [ ] Run EXQ-PLAY-004: rule learning and constraint satisfaction in CausalGridWorld variant
- [ ] Tests Q-050: shared-state monitoring requirement

### Phase 5: Cooperative Play (V4 prerequisite)

- [ ] Multi-agent environment (two REEAgent instances or scripted partner)
- [ ] Bilateral play_frame_tag protocol
- [ ] Joint benefit signal (fires only on both agents' contribution)
- [ ] Frame-mismatch detection and downgrade protocol
- [ ] Run EXQ-PLAY-005 (V4): bilateral frame integrity test with peer partner
- [ ] Tests Q-051: continuous background signal requirement

---

## 9. Experimental Proposals

### EXQ-PLAY-001: Sensorimotor Play Signal Comparison

**Question:** Does learning-progress-weighted synthetic z_goal produce better E1+E2 joint
competence at gate than flat z_goal?

**Design:** 3 conditions, 30 episodes each:
1. No play (baseline)
2. Flat synthetic z_goal (constant magnitude, random direction)
3. LP-weighted synthetic z_goal (d(PE_E1)/dt weighted, goal-babbling direction)

**Metrics:** E1 prediction accuracy on novel actions; E2 transition stability; action diversity
index; calibration leakage.

**Predicted:** LP-weighted > flat > baseline on E1+E2 gate metrics; flat shows monostrategy
signature.

**Claim IDs:** MECH-194, MECH-195, INV-058

---

### EXQ-PLAY-002: Pretend Play Tag Ablation (MECH-198 test)

**Question:** Do hypothesis_tag AND play_frame_tag need to co-activate in pretend play, or
is either sufficient?

**Design:** 4 conditions:
1. Full pretend (hypothesis_tag=True AND play_frame_tag=True)
2. Play only (play_frame_tag=True, hypothesis_tag=False)
3. Simulation only (hypothesis_tag=True, play_frame_tag=False)
4. Neither (baseline real episodes)

**Metrics:** Strategy transfer to real episodes; frame confusion rate (200, 201); calibration
leakage; commitment architecture exercise (deliberation cycle completion rate).

**Predicted:** Condition 1 highest transfer + lowest frame confusion. Conditions 2 and 3
produce characteristic failure signatures: condition 2 = calibration leakage (no decoupling);
condition 3 = no transfer (learning suppressed by hypothesis_tag alone).

**Claim IDs:** MECH-198, MECH-194, MECH-094

---

### EXQ-PLAY-003: Q-050 Test — Rule-State Monitoring Necessity

**Question:** In games-with-rules, is per-step shared-state monitoring necessary, or does
open/close frame suffice?

**Design:** 2 conditions:
1. Full: agent has per-step legal_moves obs + violation harm injection
2. Minimal: agent has only frame-open/close; no per-step rule state; only end-of-episode
   outcome signal

**Metrics:** Rule violation rate; constraint satisfaction; rule generalization to novel rule
variants; inhibitory control (moves on partner turn).

**Predicted:** Condition 1 significantly outperforms condition 2 on all metrics; condition 2
produces rule amnesia and constraint collapse.

**Claim IDs:** Q-035, ARC-049, MECH-197

---

### EXQ-PLAY-004: Calibration Leakage Baseline

**Question:** Does MECH-195 (calibration isolation) hold under V3 play implementation?

**Design:** N play episodes with synthetic z_goal magnitude X; measure KL of z_goal
distribution before vs. after; verify < 0.05 nat threshold.

**Metrics:** z_goal magnitude distribution KL; z_harm calibration shift; drive depletion
rate post-play.

**Predicted:** Near-zero leakage if architecture correct.

**Claim IDs:** MECH-195, MECH-196

---

### EXQ-PLAY-005: Play-to-Real Transfer (INV-058 test)

**Question:** Is play structurally necessary? Does untrained-but-equivalent-episode-count
baseline fail to achieve play-trained performance?

**Design:** Matched episode count:
1. Real episodes from cold start (no play phase)
2. Play phase (all types in sequence) then real episodes

**Metrics:** Real episode goal-pursuit performance; E3 trajectory selection diversity; time
to criterion on real goal tasks.

**Predicted:** Play-pretrained significantly outperforms cold-start on all metrics. If not:
INV-058 requires V3 evidence revision.

**Claim IDs:** INV-058, MECH-194, MECH-195, ARC-050

---

## 10. Frame Telemetry Proposals

Each play episode should emit the following telemetry record:

```json
{
  "episode_id": "...",
  "play_type": "sensorimotor|constructive|pretend|games_with_rules|cooperative",
  "frame_open_timestamp": "...",
  "frame_close_timestamp": "...",
  "frame_duration_steps": 0,
  "play_frame_tag_dropouts": 0,
  "hypothesis_tag_dropouts": 0,
  "synthetic_harm_events": 0,
  "real_harm_events_below_threshold": 0,
  "real_harm_events_above_threshold": 0,
  "emergency_exit": false,
  "commitment_events": 0,
  "deliberation_cycle_complete": 0,
  "frame_confusion_200_events": 0,
  "frame_confusion_201_events": 0,
  "z_goal_synthetic_magnitude": 0.0,
  "z_goal_drift_per_step": 0.0,
  "learning_progress_signal_mean": 0.0,
  "rule_violations_self": 0,
  "rule_violations_partner": 0,
  "partner_state_prediction_accuracy": null,
  "strategy_transfer_delta": null,
  "calibration_leakage_KL": null
}
```

This telemetry feeds the play substrate monitoring dashboard (explorer.html extension TBD).

---

## 11. Proposed Gap Log Updates

The following DEV-NEED entries require updates based on this design work and literature
findings. These are proposals only — governance registration of new claims requires a separate
claims.yaml edit pass.

### 11.1 DEV-NEED-010 (Sensorimotor Play) — Refine Gate Criterion

**Current:** Gate criterion under-specified.
**Proposed update:** Exit criterion = JOINT E1 prediction accuracy >0.85 on novel held-out
action set AND E2 transition stability (rollout variance < threshold) on held-out action set.
Neither criterion alone is sufficient (Libertus/Needham evidence).

### 11.2 DEV-NEED-011 (Constructive Play) — Add Sub-goal Binding Failure Mode

**Current:** Failure modes not listed.
**Proposed:** Add: goal drift (attractor too weak), step-by-step reactivity (E3 immature),
sub-goal binding failure (achieves sub-goals but does not chain to target).

### 11.3 DEV-NEED-012 (Pretend Play) — Add Dual-Tag Requirement

**Current:** Mentions hypothesis tag + play frame but does not specify they must CO-ACTIVATE
throughout (not just at open/close).
**Proposed update:** Add persistent dual-tag co-activation as explicit implementation
requirement; add frame confusion metrics (MECH-200, MECH-201 rates) as gate sub-criteria.

### 11.4 DEV-NEED-013 (Games-with-Rules) — Specify Q-050 as Implementation Requirement

**Current:** Q-035 now resolved; Q-050 (games-with-rules dual-level content monitoring) is open.
**Proposed:** Add per-step dual-level shared-state monitoring (rule compliance + strategic
rationality simultaneously, per Schmidt 2015) as implementation requirement for DEV-NEED-013.
Q-050 is marked substrate_conditional (requires V4 multi-agent substrate). Add rule inference
(novel rule generalization) as gate sub-criterion.

### 11.5 New Claims to Propose

The following are candidate new claims surfaced by this design and the literature. They require
full claims.yaml registration in a governance pass:

1. **Missing MECH (PE-locus probe action):** E1 prediction error LOCUS (not just magnitude)
   upweights targeted probe-action selection during sensorimotor play. PE in a specific state
   region increases probability that action selection probes that region. Distinct from global
   curiosity. Evidence: Stahl/Feigenson 2015, Schulz/Bonawitz 2007.

2. **Refine MECH-194:** Synthetic z_goal must encode learning progress (d(PE)/dt), not raw
   prediction error or flat value. Competence-based signal generates transferable curriculum;
   knowledge-based signal risks monostrategy in high-variance regions.

3. **Refine MECH-195 evidence quality note:** Strategy/calibration dissociation is
   INCOMMENSURABLE BY CONSTRUCTION (Schmidhuber 2010): intrinsic drive is derivative
   (d/dt of knowledge), extrinsic is absolute value. Not a quantitative mismatch but a
   formal incompatibility. This formal grounding should be added to MECH-195's
   evidence_quality_note.

4. **New ARC claim (Play-to-real transition):** Play phase terminates via competence
   saturation (d(PE_E1)/dt < threshold across all reachable regions), not via fixed schedule.
   Real homeostatic drives naturally dominate as synthetic drive decays. Alternatively:
   competitive drive dynamics (z_goal, z_harm, z_goal_synthetic as mutually inhibiting
   attractors) produce natural mode switching. Evidence: Pezzulo/Santucci 2014, Forestier 2022.

5. **New MECH claim (Goal-space continuity):** z_goal_synthetic and z_goal_real must lie in
   the same latent manifold. Transfer fails silently if they occupy disjoint spaces.
   Implementation constraint on GoalConfig. Evidence: Colas 2022.

6. **Refine ARC-049 (three-level signal):** Biological play uses three distinct signal types:
   frame-open (bilateral commitment), continuous background (low-cost maintenance throughout),
   ambiguity-triggered repair (explicit at misinterpretation risk points). REE play
   infrastructure must implement all three levels. Evidence: Bekoff 1995, Bakeman 1984.

7. **Refine ARC-049 (three-phase structure):** Social play has open/body/close phase
   structure with distinct commitment events at each phase boundary. The "body" phase has its
   own commitment structure (ongoing mutual maintenance). Evidence: Galbusera 2017.

8. **Refine MECH-194 (harm signal architecture):** Harm signals during play are NOT
   suppressed. They remain active and evaluated against a threshold shifted by the PLAY
   system. Real severe harm still triggers emergency exit. Only the escalation criterion is
   modified. Evidence: Panksepp 1998, Bekoff 1995, Pellis 2023.

9. **Refine MECH-199/ARC-047 (calibration constraint):** Caregiver/harness frame complexity
   must be calibrated to learner's current bilateral capacity. Overshooting produces worse
   outcomes than matched low-play (Frame-mismatch worse than absence). Evidence: Ham 2024.

---

## 12. Literature Directories Created

The following literature record directories were created during this design session:

**Initial session (2026-05-16 AM):**
- `evidence/literature/targeted_review_pretend_play_counterfactual/` — 8 records
  (Leslie 1987, Buchsbaum 2012, Francis 2023, Drayton 2011, Kuhn-Popp 2013,
  Rutherford 2003, Vasilopoulos 2026, Smits 2024)
- `evidence/literature/targeted_review_games_with_rules_ef/` — 9 records
  (Rakoczy 2008, Schmidt 2015, Rakoczy 2007, Tomasello 2005/2019, Zhao 2025,
  Diamond 2011, Fantasia 2014, Rosas 2019)

**Follow-on session (2026-05-16, Q-035 correction pass):**
- `evidence/literature/targeted_review_infant_play_contingency/` — 7 records
  (Tronick 1978, Murray & Trevarthen 1985, Striano et al. 2005, Gergely & Watson 1996,
  Rochat et al. 1999, Ekas et al. 2012, Feldman 2007)
- `evidence/literature/targeted_review_ethological_play_signals/` — 8 records
  (Bekoff 1995, Byosiere et al. 2017, Davila-Ross & Palagi 2022, Nolfo & Palagi 2022,
  Palagi 2011, Palagi 2024, Waller et al. 2012, Wenig et al. 2021)

Other lit-pull results (cognitive development, sensorimotor, social/R&T, robotics) were
returned as structured findings tables and are not yet written as individual records. Those
topics should be written into their respective `targeted_review_*` directories in a
follow-on session.

---

## 13. Claims Registered (Follow-On Pass, 2026-05-16)

**New claims:**
- **MECH-327**: E1 PE locus upweights probe-action selection during sensorimotor play
- **MECH-328**: Goal-space continuity (synthetic z_goal and real z_goal in same manifold)
- **ARC-073**: Play-to-real transition criterion = competence saturation (not schedule)
- **Q-048**: L2 sufficient for sensorimotor/constructive monitoring? (V3-tractable)
- **Q-049**: Pretend play requires hypothesis_tag + play_frame_tag co-active throughout? (V3-tractable)
- **Q-050**: Games-with-rules require per-step dual-level content monitoring? (V4 needed)
- **Q-051**: Cooperative play requires full L1+L2+L3 from both parties? (V4 needed)

**Claims refined (notes updated):**
- **MECH-194**: z_harm threshold-shifted not suppressed (Panksepp 1998); z_goal must be LP-weighted
- **MECH-195**: Incommensurable by construction (Schmidhuber 2010 formal derivation)
- **ARC-049**: Three-level signal architecture + monitoring-is-primitive + graded scalar framing
- **MECH-197**: Corrected: monitoring is primitive throughout; games-with-rules adds content complexity
- **Q-035**: Closed as resolved; resolution_note added; sub-questions Q-048–Q-051 opened

**Suggested future claim (not yet registered):**
- **MECH-329** (candidate): Contingency-detection module as biological substrate of frame monitoring
  (Gergely-Watson mechanism + Feldman 2007 oscillator biology). Would link play frame monitoring
  to REE's sleep/oscillator thread (INV-049).
