# Thought Intake -- 2026-09-22 -- action-conditioned world model, dynamic precision, arousal control of commitment

**Date:** 2026-09-22
**Raw thought file:** `docs/thoughts/2026-09-22_action_conditioned_world_model_and_arousal_gated_commitment.md`
**Session:** `thought-ingest-acwm-arousal-commit-20260922` (umbrella main checkout, Mac)
**Digestion drafts:** `evidence/planning/thought_digestion_staged_2026-09-22_action_conditioned_world_model_and_arousal_gated_commitment.md` (draft-only; not applied)

## 1. Verbatim prompt

> it seems to me that an action conditioned world model is an owed capability of REE and a genuinely
> dynamic precision control and arousal control that can alter selection for commitment. Should this
> be planned and incorporated into REE?

The raw file's expansion (three faces of arousal on commitment: WHEN / WHETHER / WHICH-SET; the
dependency ordering WHICH-SET -> action-conditioned world model) was drafted by the session at the
user's instruction, not captured from the user, and is treated below as a proposal.

## 2. What is new vs. existing REE docs/claims

| Thread in the thought | Existing REE coverage | Verdict |
|---|---|---|
| T1. Action-conditioned world model is owed | **ARC-002** (active): E2 is the fast forward predictor of affordances; its 2026-09-03 note already separates the strong form (action-conditioned predictions discriminate viable from non-viable actions) from the weak form (predicted-outcome divergence across actions). **MECH-135** (candidate): E1 must co-evolve z_world during rollout via an action-conditioned transition; its falsifier includes an action-conditioning-OFF arm. Substrate: `ree-v3/ree_core/predictors/e2_world.py` `E2WorldForward(z_world, action)` with SD-013 interventional contrastive loss; `use_e2_world_forward` and `use_interventional` both default OFF. substrate_queue `SD-e1-rollout-consistency-training`: items 1-2 landed, item 3 landed with validation owed. `evidence/planning/cross_plan_root_cause_synthesis_20260902.md`: the observation -> z_world -> E1/E2 rollout interface is the binding constraint on v3 closure (39/43 nodes). | **Already owned.** Cross-reference only. The thought's "owed" is the registry's own diagnosis; what is owed is the SD-e1 item 3 validation run and a routing decision on the E2 world-forward default. |
| T2. Genuinely dynamic precision control that alters selection/commitment | **ARC-016** (stable): the precision-to-commitment circuit; E3 precision is the running variance of its own prediction error, commit fires when variance < threshold. **MECH-104** (LC-NE volatility interrupt raises running_variance), **MECH-106** (valence-asymmetric threshold), **MECH-043** (DA precision weighting), **INV-022** (precision allocation must be heterogeneous, not one scalar; candidate, unbuilt). Substrate: `e3_selector.py` dynamic precision (ARC-016), plus `use_precision_scaled_commit_temperature`, `use_gap_scaled_commit_temperature`, `use_variance_tracking_commit_threshold` (ARC-029, landed 2026-09-18) -- all default OFF. Liveness: precision collapse is the ONE control-plane pathology that moves behaviour (83/150 divergences, 2026-09-18). | **Already owned.** The "genuinely" qualifier is met for the E3 commit gate; the open piece is INV-022 (heterogeneity), unchanged by this thought. |
| T3a. Arousal alters WHEN (E3 cadence) | **MECH-093**, **MECH-005**, **MECH-161**, **ARC-044**. Substrate: `heartbeat/clock.py` z_beta -> e3_steps. substrate_queue `mech005-endogenous-arousal-dynamic-range` (registered 2026-09-22 15:26Z): endogenous ||z_beta|| spans 0.91% of its mean, so the endogenous WHEN face is unsatisfiable as an identity; user ruled "fix the instrument before spending a run". | **Already owned**, including the defect. |
| T3b. Arousal alters WHETHER (commit fires) | **MECH-465** (substrate_ceiling): arousal's effect on WHETHER commitment fires is expressible only near the gate boundary; **MECH-463**: scalar arousal routes cannot reorder candidates but DO change whether commitment fires; **MECH-106**, **MECH-104**, **MECH-090** (BetaGate commit-readiness conjunction). substrate_queue `MECH465-COMMIT-GATE-HEADROOM`: boundary regime reached on seeds 0 and 3 (V3-EXQ-1015); `ready:false` now stale per its own 2026-09-22 audit note. | **Already owned.** One defect is recorded but UNOWNED as a repair: the armed commit-readiness gate is behaviourally inert (2026-09-18 probe; MECH-042 audit: "EXISTING NODE, MISSING EDGE"). Routed to /governance by flag (section 7). |
| T3c. Arousal alters WHICH candidate is committed -- via eligibility BREADTH | **MECH-463** says a scalar cannot reorder (argmax-invariant). **MECH-448 / ARC-107** build the BG eligibility envelope with a FIXED global floor (`f_eligibility_envelope_floor` 0.30) tuned on GAP-A; memory records the per-channel calibration limitation. **MECH-313** (LC-NE tonic noise floor) is state-independent selection noise, not breadth. **MECH-359** (scalar too weak to steer). No claim couples arousal to envelope width / admitted-set size; grep of `claims.yaml` for arousal x eligibility/envelope/shortlist finds none. | **Genuinely new, narrow.** Registered as **MECH-580**: the WHICH-SET face -- arousal modulates the breadth of the admitted candidate set, the one WHICH route a scalar has that does not contradict MECH-463. |
| T4. Dependency ordering: WHICH-SET presupposes T1; WHEN/WHETHER do not | The binding-constraint synthesis (2026-09-02) and the per-claim non-degeneracy-precondition discipline (`dv-dynamic-range-precondition-class`) already carry this as a gate on individual falsifiers; GFLAG-0114 asked for the gate to be declared on the ceiling nodes. The 2026-09-18 liveness memo states the control-plane inertness is NOT the conversion ceiling -- consistent with the ordering. | **Owned as a precondition pattern, not as a claim.** Not registered separately; written into MECH-580's precondition P1 and its `notes`, and into the architecture stub, so the next session finds it by grep. |

## 3. Key formulations (verbatim from the raw file)

- "an action-blind or single-step model ... can be accurate at 'what happens next' while carrying no
  information about 'what changes because of THIS candidate action'"
- "a precision that is computed but consumed only as telemetry is not control"
- "the only way a scalar arousal signal can change WHICH candidate is committed is by changing how
  many candidates are eligible"
- "the observed inertness of the commit-readiness gate and of the endogenous arousal signal ... is
  NOT explained by the world-model gap; those are separate instrument defects with their own repairs"

## 4. Literature check

Run this pass by a read-only research agent (37 lookups); every anchor located, none unverified.
Full citations with DOIs are in the agent report summarised here. Verdicts are against the thread
they anchor, and a paper resembling REE strengthens no claim's confidence (`feedback_lit_exp_decoupled`).

**T1 (action-conditioned world model) -- SUPPORTED, with two refinements.**
- Ha & Schmidhuber 2018 (arXiv 1803.10122; NeurIPS title "Recurrent World Models Facilitate Policy
  Evolution"); Hafner et al. PlaNet, ICML 2019 (RSSM + latent overshooting = the multi-step
  consistency clause, closest match to SD-e1); Hafner et al. Dreamer, ICLR 2020; Oh et al. NIPS 2015
  (representation supported, selection benefit weak); Wolpert & Kawato 1998 Neural Networks 11:1317
  (efference-copy forward models; the biological instance).
- Refinement 1: Lambert, Amos, Yadan & Calandra 2020 (L4DC, PMLR 120:761) -- one-step likelihood is
  UNCORRELATED with control performance, so predictive accuracy is the wrong capability test even for
  an action-conditioned model. Lambert, Pister & Calandra 2022 (arXiv 2203.09637) is the correct anchor
  for "single-step is not enough" (compounding error over composed horizons). Two papers, not one.
- Refinement 2: Pearl 2019 CACM 62(3):54 -- rung 1 (seeing) vs rung 2 (doing) is T1's distinction, BUT
  a P(s'|s,a) model fit on on-policy data is not automatically interventional if the behaviour policy
  is confounded with state. Do not over-claim action-conditioning = do-calculus. (SD-013's
  interventional contrastive loss is the substrate's answer to exactly this.)

**T2 (dynamic precision altering selection/commitment) -- SUPPORTED, directly.**
- Feldman & Friston 2010 Front. Hum. Neurosci. 4:215 -- precision INFERRED from the system's own
  error statistics (the "derived online, not a fixed gain" clause). Friston et al. 2012 PLoS Comput.
  Biol. 8:e1002327 -- policy precision IS the softmax inverse temperature (REE's
  `use_precision_scaled_commit_temperature` is that term, not an analogy). Parr & Friston 2017
  J. R. Soc. Interface 14:20170376; Parr & Friston 2019 Curr. Opin. Psychol. 29:1 (attention vs
  salience). Friston 2010 Nat. Rev. Neurosci. 11:127 (framework only).
- Yu & Dayan 2005 Neuron 46:681 -- NE = UNEXPECTED uncertainty. This assigns the arousal analogue an
  uncertainty/precision role, which cuts against a clean arousal-vs-precision split (see T3).

**T3 (arousal alters commitment) -- SEPARABILITY supported; EXCLUSIVITY contradicted.**
- WHETHER/WHEN face, strong: Thura & Cisek 2017 Neuron 95:1160 "The Basal Ganglia Do Not Select
  Reach Targets but Control the Urgency of Commitment" (the single strongest anchor for a
  WHETHER-vs-WHICH decomposition); Thura & Cisek 2014 Neuron 81:1401; Hanks, Kiani & Shadlen 2014
  eLife 3:e02260 (evidence-independent additive urgency); Cisek, Puskas & El-Murr 2009 J. Neurosci.
  29:11560 (multiplicative urgency gating); Murphy, Boonstra & Nieuwenhuis 2016 Nat. Commun. 7:13526
  (pupil-indexed global gain generates urgency -- the tightest arousal -> urgency link); Bouret & Sara
  2005 TINS 28:574; Dayan & Yu 2006 Network 17:335; Standage, Blohm & Dorris 2014 Front. Neurosci.
  8:236; Aston-Jones & Cohen 2005 Annu. Rev. Neurosci. 28:403 (MIXED: gain on the decision function
  itself, so not WHETHER-only).
- Refinement: Steinemann, O'Connell & Kelly 2018 Nat. Commun. 9:3627 -- urgency applied at
  motor-preparation levels only, BUT the same speed pressure also enhanced sensory-evidence encoding.
  The faces are separable in locus yet CO-RECRUITED by one control demand; a REE test must not assume
  the arousal knob leaves the evidence path untouched.
- CONTRADICTION of the exclusive reading ("arousal is WHICH-neutral"), reported honestly: de Gee,
  Knapen & Donner 2014 PNAS 111:E618 (pupil tracks upcoming choice and individual bias); de Gee et
  al. 2017 eLife 6:e23232 and de Gee et al. 2020 eLife 9:e54014 (phasic arousal shifts the DRIFT
  CRITERION, suppressing choice bias across species and domains -- a WHICH effect that is neither
  threshold nor starting point); Eldar, Cohen & Niv 2013 Nat. Neurosci. 16:1146 (global gain sets
  attentional BREADTH and which dimension is learned about); Jepma & Nieuwenhuis 2011 J. Cogn.
  Neurosci. 23:1587 (pupil predicts explore-vs-exploit choice).
- Instrument caveat: Megemont et al. 2022 eLife 11:e70510 -- pupil is not an accurate real-time LC
  readout; Murphy et al. 2014 Hum. Brain Mapp. 35:4140 validates only the coupling.

**What the literature did to the thought.**
1. The raw file's "the only way a scalar arousal signal can change WHICH" is over-strong as a
   statement about brains: arousal has at least two WHICH routes there, attentional BREADTH (Eldar
   2013; Jepma & Nieuwenhuis 2011 -- these SUPPORT MECH-580's mechanism) and drift-criterion BIAS
   SUPPRESSION (de Gee 2017/2020 -- a per-candidate accumulation effect, not a breadth effect).
   MECH-580 is therefore scoped to REE's GLOBAL-SCALAR routes, where MECH-463's argmax-invariance
   makes breadth the only surviving WHICH route; a de Gee-type bias effect would have to enter REE
   through the per-candidate `score_bias` route, which MECH-463 already treats separately. The claim
   title says so.
2. Locus tension recorded, not resolved: Thura & Cisek 2017 put BG authority on urgency (WHETHER),
   not on target choice; MECH-580 places its breadth face in the ARC-107 BG eligibility envelope. A
   literature-faithful reading would put breadth modulation upstream (cortical attentional breadth)
   and the BG on WHETHER. Which locus REE uses is a substrate choice; MECH-580's falsifier reads the
   admitted-set size and is locus-agnostic, and the notes carry the tension for whoever builds it.
3. T4's ordering (WHICH-SET presupposes an action-conditioned world model) gets NO support and NO
   contradiction from the decision-neuroscience anchors -- they are all pre-specified two-option
   perceptual paradigms. That bridge rests on the MBRL literature (Ha & Schmidhuber; Hafner; Lambert
   2022) alone, and the intake says so rather than letting the LC citations appear to cover it.

## 5. Affected existing claims

- **Cross-referenced (`depends_on` from MECH-580):** MECH-463, MECH-465, MECH-448, ARC-107, MECH-313,
  MECH-093, MECH-005, MECH-106, MECH-090, ARC-002, ARC-016, ARC-044.
- **Distinguished from:** MECH-463 (argmax-invariance -- MECH-580 accepts it and names the one WHICH
  route that survives it); MECH-313 (state-independent noise floor vs state-dependent breadth);
  MECH-465 (WHETHER face vs WHICH-SET face); MECH-093/MECH-005 (WHEN face).
- **Amended:** none. No existing claim's status, confidence, evidence record, or `what_would_answer`
  was touched.

## 6. Candidate claims -- REGISTERED this pass

- **MECH-580** -- Arousal alters WHICH candidate is committed only by modulating commit-eligibility
  BREADTH (the width of the BG eligibility envelope / size of the admitted candidate set), never by
  reordering scores; high phasic arousal narrows toward the incumbent, low/tonic widens; dissociable
  from the WHETHER (MECH-465) and WHEN (MECH-093) faces; observable only under action-discriminable
  candidate futures (ARC-002 strong form). `candidate`, `substrate_conditional`,
  `implementation_phase: v4` by the ingestion default WITH an explicit V3-testability note for
  /governance to route (every substrate piece except the arousal -> envelope coupling exists in V3
  today). Location: `docs/architecture/commitment_control_faces.md#mech-580`.

No other claim registered: T1, T2, T3a, T3b are owned (table above), T4 is a precondition pattern.

## 7. Next steps

1. **Routing decision (/governance):** whether to commission the arousal -> envelope-floor coupling
   build (three-site `REEConfig` knob) that MECH-580's falsifier needs, and whether MECH-580 is V3 or
   V4. DO NOT queue an experiment on MECH-580 before that decision.
2. **Governance flag raised this pass:** `MECH-090` -- the armed commit-readiness gate is behaviourally
   inert (2026-09-18 probe, 0/150 divergences with `use_commit_readiness_gate=True` and readiness pinned
   below floor); MECH-042's audit calls it a missing edge but no substrate_queue row owns the repair.
3. **Already-owned work this thought points at, not re-chipped here:** SD-e1 item 3 validation run
   (`/queue-experiment`, owned by the SD-e1 row); `mech005-endogenous-arousal-dynamic-range`
   (registered today, /governance adjudicates); `MECH465-COMMIT-GATE-HEADROOM` stale `ready` (its own
   audit note).
4. **Digestion:** MECH-580's `what_would_answer` is DRAFTED in the staging file named in the header,
   not applied. The user approves or edits; then an applying session copies it in and sets the
   category.
5. **Version routing:** MECH-580 registered v4 by default; see item 1.
6. **Do not harden.** The raw thought's own instruction stands: nothing here is promoted, and a
   literature resemblance strengthens no claim's confidence.
