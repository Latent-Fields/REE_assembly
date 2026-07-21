# Histaminergic gating of moment-to-moment memory accessibility (2026-06-12)

Status: processed
Processed in:
- `docs/claims/claims.yaml` (thought-intake REAP: Q-076, MECH-425 (histaminergic retrieval-accessibility gating). This file is cited in those claims' `sources`.)


**Status: INTAKE DONE 2026-06-12.** Literature explored; `/thought-digestion` registration
complete. Registered: **MECH-425** (two-layer retrieval-time accessibility gating -- Line A
gain + Line B suppression), **Q-076** (the gain x suppression interaction), and a cross-ref
reap note on **MECH-261** (its read-side sibling). All candidate / `substrate_conditional` /
`implementation_phase: v4`, OFF the V3 critical path -- promotes nothing. See "Intake outcome"
at the foot of this doc.

Source thought (Daniel, 2026-06-12), preserved verbatim:

> [news-medical article: "Brain histamine neurons control moment-to-moment memory
> accessibility"] this article is very interesting and relevant for ree. I would imagine
> that access to all memories could produce problematic interference and active management
> of what cues are retrievable would be needed to manage this. This histaminergic effect
> and the links of histamine to arousal and gating link it all together I think. once these
> ideas are explored in literature then a thought intake could be created to ensure the
> ideas are all captured.

## Trigger paper

**Morishita et al., "Infraslow histaminergic dynamics govern priming states to gate
moment-to-moment memory accessibility," *Neuron* (2026), DOI: 10.1016/j.neuron.2026.05.019**
(Nomura lab, Nagoya City University). Slow (infraslow) spontaneous fluctuations in
tuberomammillary-nucleus (TMN) histamine neuron activity set a *priming state*: when
histamine activity is high just before a cue, a learned reward memory is ~40% more likely
to be expressed, and basolateral amygdala (BLA) ensemble patterns are reinstated more
reliably. Framing: recall is not just read-out of a stored trace -- an internal
(arousal-coupled) brain state *gates whether the trace becomes accessible at that moment*.
Failure to recall != memory loss; it can be a transient low-gating state.

## Literature exploration

The two intuitions in the source thought turn out to map onto **two mechanistically
distinct lines** in the literature. Keeping them separate is the main analytic payload.

### Line A -- global, arousal-coupled retrieval *gain/priming* (the histamine axis)

- **Morishita 2026** (above): infraslow TMN-histamine priming state as a global retrieval-
  readiness knob over BLA reinstatement.
- **Nomura et al. 2019, *Biol Psychiatry* (DOI 10.1016/j.biopsych.2018.11.009)** -- same
  group precursor: central histamine boosts perirhinal-cortex activity and *restores
  forgotten* object memories; H3 inverse agonists (thioperamide, betahistine) disinhibit
  histamine release, depolarise PRh neurons, raise spontaneous activity, and facilitate
  reactivation of behaviourally-tagged ensembles. Explicitly framed as **stochastic
  resonance** (raising a noisy gain so sub-threshold traces cross into accessibility).
  Includes a human betahistine RCT -- effect strongest for hard-to-remember items / poor
  performers.
- **Chemogenetic activation of histamine neurons promotes retrieval of apparently lost
  memories**, *Molecular Brain* 2024 (DOI 10.1186/s13041-024-01111-8) -- direct causal
  TMN-histamine -> retrieval-of-lost-memory link.
- **H3 as arousal/sleep-wake + heteroreceptor hub:** Esbenshade et al. 2008 *Br J Pharmacol*
  (DOI 10.1038/bjp.2008.147); Alhusaini et al. 2022 *Front Pharmacol*
  (DOI 10.3389/fphar.2022.861094). H3 autoreceptor/heteroreceptor gates release of HA, ACh,
  DA, NE; histamine is a wake-promoting arousal system (off in sleep). This is what ties
  "retrieval gating" to "arousal" in the source thought -- they are the *same* slow state
  variable.
- **Bidirectional, history-dependent retrieval control:** Fabbri et al. 2016 *PNAS*
  (DOI 10.1073/pnas.1604841113) + Passani et al. 2017 review *Neurobiol Learn Mem*
  (DOI 10.1016/j.nlm.2017.08.007) -- hippocampal H1 *facilitates* retrieval while H2 can
  *inhibit* it, and which one fires depends on the recent reinforcement history of the cue.
  So the histamine gate is not a pure on-switch; it has a context-dependent suppress arm.
- **Histamine x ACh cross-talk:** Zheng et al. 2023 *Cell Rep* (DOI 10.1016/j.celrep.2023.113073)
  -- postsynaptic H3 on ventral-basal-forebrain cholinergic neurons modulates contextual
  fear retrieval. Connects this thread to the plasticity-window ACh memory (do NOT conflate:
  here ACh/HA gate *retrieval*, not learning-rate).

### Line B -- content-selective competitive *inhibition* (the interference axis)

This is Daniel's "access to all memories produces interference; active management of which
cues are retrievable is needed." That is the **retrieval-induced-forgetting (RIF) /
inhibitory-control** literature, and it is a *different* mechanism from the histamine gate:

- Penolazzi et al. 2014 *J Neurosci* (DOI 10.1523/JNEUROSCI.0349-14.2014) and Khan et al.
  2024 *J Neurosci* (DOI 10.1523/JNEUROSCI.0189-24.2024) -- causal (tDCS) evidence that
  (dl/m)PFC inhibitory control *actively suppresses competing memories* to resolve
  retrieval competition; suppressing the controller reduces RIF and raises competitor
  accessibility.
- Storm & White 2010 *Memory* (DOI 10.1080/09658210903547884) -- ADHD shows a deficit in
  this inhibitory control of memory (failure mode of the management system).
- Giebl et al. 2016 *QJEP* (DOI 10.1080/17470218.2015.1085586) -- RIF shapes affect/
  future-imagining (positivity bias), i.e. the management policy has downstream valence
  consequences.

## Candidate synthesis (the part worth registering)

The single most useful abstraction: **memory retrieval is governed by two composable
control layers, and REE currently models neither as an explicit retrieval-time policy.**

1. **A global, slowly-fluctuating, arousal-coupled retrieval-readiness gain** (histamine /
   Line A). Sets the *threshold/gain* on whether ANY stored trace can be reinstated this
   moment. Content-blind. Infraslow. Coupled to the wake/arousal state. Stochastic-resonance
   flavour (raising gain rescues sub-threshold traces, at the cost of specificity).
2. **A content-selective competitive inhibition** (RIF / Line B). Given whatever the global
   gate lets through, *suppress specific competitors* to keep retrieval clean and prevent
   interference. This is the "active management of which cues are retrievable" piece.

The interesting REE claim is the *interaction*: a high global gate without selective
inhibition should produce exactly the "problematic interference" Daniel predicts (too many
traces accessible at once); a low global gate looks like apparent forgetting / poor recall.
The competent regime is high gain + sharp competitive suppression.

## Where this lands against the existing REE registry (for the intake to resolve)

- **Attention = distributed precision-selection** (project memory): Line A is a *retrieval-
  side instance of precision/gain control* -- a biological example of the global precision
  gate that memory says REE already distributes across ARC-005 / MECH-251/254/255/259/261/347.
  Question for intake: is histaminergic retrieval-readiness already covered by that
  distributed precision story, or is "a global slow arousal-coupled gain specifically over
  *memory reinstatement*" a genuinely uncovered variable?
- **Contextual Memory Allocation Gate** (project memory): that note found REE owns the
  *gates* (MECH-094/261, ARC-035, SD-016) but not the *gating POLICY*. Line A is a policy
  variable (when is the system in a high-retrieval-readiness state) and Line B is another
  (which competitor to suppress). Likely amends MECH-261 rather than spawning a new INV.
- **MECH-094 / MECH-271** (tag loss -> confabulation; routing signature): relevant to Line B
  -- failed competitive suppression / wrong-trace reinstatement is a confabulation pathway.
- **Sleep cluster:** histamine is a wake-arousal system, so retrieval-readiness is
  state-gated by the sleep/wake axis -- consistent with offline-phase claims; retrieval gain
  should be low offline.
- **Plasticity-window neuromodulators (ACh/PV/BDNF)** (project memory): adjacent via H3-ACh
  cross-talk (Zheng 2023) but a DIFFERENT axis -- that memory is about gating *learning*;
  this is about gating *retrieval*. Keep them distinct in the intake.

## V-phase

Off the V3 critical path (V4/V5-leaning, like the other neuromodulator/memory-gate intakes).
Candidate claims most likely land as `substrate_conditional` / version-scoped and as an
amendment to MECH-261 (gating policy) plus possibly a new Q-claim on the gain-x-suppression
interaction. The intake (`/thought-digestion`) is the step that decides registration vs
cross-reference-only and writes the `what_would_answer` test designs.

## Intake outcome (registered 2026-06-12)

The three registry questions, resolved:

1. **Line A is genuinely uncovered.** It is an *instance* of `ARC-005` precision-routing at
   the abstract level, but the existing precision cluster (`MECH-251/254/255/259/347`) acts on
   *current* perception, candidate-selection, and goal-templates -- `MECH-254` selects among
   *currently-active* latents entering E3; `MECH-347` is fast, content-specific cue->incentive
   recall. None is a *global, infraslow, arousal-coupled gain over stored-trace reinstatement*.
   Registered, with `ARC-005` as an abstract-parent cross-ref (not a duplicate).
2. **`MECH-261` is the WRITE-side family; this is its READ-side sibling.** Folding an untested
   V4 retrieval extension into a `stable`, 33-support write-gate claim would muddy it, so the
   read-side gating is a **new MECH** (`MECH-425`) with `MECH-261` cross-referenced both ways
   (its `depends_on` + a dated reap note on MECH-261). "Amendment, not a new INV" -- satisfied
   at the MECH/Q level; no invariant minted.
3. **Distinct from plasticity-window ACh/BDNF.** That memory gates *learning-rate*; this gates
   *retrieval*. Adjacent only via H3-ACh cross-talk (Zheng 2023) -- noted in the claim text,
   no `depends_on`.

Registered claims (all `candidate` / `substrate_conditional` / `implementation_phase: v4` /
`v3_pending: true`; `exp_conf` stays 0 -- promotes nothing):

- **MECH-425** -- retrieval-time accessibility gating, the two composable read-side policy
  layers (Line A global arousal-coupled reinstatement gain + Line B content-selective
  competitive suppression). `depends_on` MECH-261 / MECH-094 / MECH-271 / ARC-005 / ARC-035 /
  SD-016 / MECH-347. `what_would_answer` = the Line-A vs Line-B double-dissociation
  (uniform-forgetting vs selective-intrusion) with a co-encoded-competitors non-degeneracy gate.
- **Q-076** -- the gain x suppression INTERACTION governs the interference-vs-forgetting
  tradeoff (the headline). `depends_on` MECH-425. `what_would_answer` = a 2x2
  {gain high/low} x {suppression on/off} interaction-term test.
- **MECH-261** -- dated cross-ref reap note added pointing to MECH-425/Q-076 as the read-side
  sibling; no status change.

Owned-by-design / cross-reference-only (NOT registered): the distributed precision story
(`ARC-005` cluster) for Line A's abstract parent; `MECH-094`/`MECH-271` for the Line-B failure
mode (confabulation / wrong-trace reinstatement); the sleep/wake axis for the state-gating of
retrieval gain.
