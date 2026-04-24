# MECH-285 Sleep-Replay Seed-Distribution Lit-Pull: Narrow vs Broad Staleness-Priority Coverage

> Created: 2026-04-24
> Origin: MECH-284 Phase 3 (online arm) landed in ree-v3 on 2026-04-24
> (`ree_core/hippocampal/staleness_accumulator.py`). MECH-285 (offline arm --
> sleep replay prioritisation weighted by accumulated staleness) is the
> remaining half of the V_s bidirectional cluster. Before implementing it
> one architectural decision needs biology validation: whether the sleep-
> replay start-state distribution should be biased only by *active* anchor
> staleness (narrow) or should also include recently-invalidated / Bouton-
> inactive dual-trace anchors (broad). The MECH-284 region map and the
> anchor-set dual-trace preservation are both already present; what needs
> settling is whether sleep replay reaches the inactive traces at all, and
> if so with what timing and priority.
> Prior V_s pulls -- `targeted_review_waking_v_s_invalidation/`,
> `targeted_review_v_s_foundation/`, `targeted_review_connectome_mech_269/`,
> `targeted_review_connectome_mech_270/`, `targeted_review_connectome_mech_271/` --
> covered waking invalidation, schema-region granularity, multi-map
> coexistence, and routing. Gap: nothing yet directly covers the start-state
> distribution of sleep-phase replay after remap / extinction, which is the
> MECH-285 implementation pivot.

## Prompt

/lit-pull Hippocampal sleep-phase replay start-state distribution after
anchor invalidation / context change. Three converging architectural
questions for MECH-285 (V_s residual-staleness sleep-priority readout):
(1) **seed coverage** -- during sleep replay, does the start-state
distribution draw only from currently-active (winning) place-cell
ensembles, or does it also draw from recently-extinguished / remapped
/ dual-trace-inactive contexts? (2) **staleness-proportional vs
threshold-gated priority** -- does replay priority scale quantitatively
with accumulated epistemic staleness across regions, or is there a
threshold above which a region enters the replay pool with roughly
uniform priority thereafter? (3) **timing of inactive-trace replay** --
if inactive traces are replayed at all, does this happen on the first
sleep bout after invalidation, or with a delay (e.g., first-night
consolidation of the winning trace; subsequent-night integration of
the loser)?

The architectural commitment to test: MECH-285 biases sleep-replay
start-state sampling by accumulated MECH-284 staleness over active
anchors only (narrow reading), with staleness-proportional priority
and no delay. The alternative is that inactive anchors retain replay
eligibility for some window post-invalidation (broad reading), in
which case MECH-285 must maintain a persistent region->seed map that
survives `AnchorSet.mark_inactive`, and MECH-284 staleness must
continue accumulating on inactive regions (or be re-routed to a
separate inactive-trace staleness channel) so the sleep consumer
can rank them.

## Specific neurobiological systems to cover

1. **Sleep-phase replay start-state distribution -- direct evidence**
   - Pfeiffer & Foster 2013 (Science) -- sequence replay start-state
     in goal-directed navigation; the canonical substrate Foster
     identified for biased sampling. (Already cited in
     `targeted_review_connectome_mech_269/`; re-use, do NOT re-pull.)
   - Olafsdottir, Barry, Saleem, Hassabis & Spiers 2015 (eLife) --
     replay of non-local and never-visited trajectories; establishes
     that the sleep-replay distribution is NOT limited to most-recent
     waking experience.
   - Olafsdottir, Bush & Barry 2018 (Current Biology) review of
     replay content.
   - Gupta, van der Meer, Touretzky & Redish 2010 (Neuron) -- replay
     of untaken paths; priority signal extends to counterfactual
     trajectories.
   - Wu & Foster 2014 (J Neurosci) -- reverse-replay magnitude
     scales with reward; establishes a non-trivial priority-by-
     relevance pattern in the canonical sleep-replay substrate.

2. **Replay of remapped / recently-extinguished contexts**
   - Liu, Gillespie, Swanson, Berkowitz & Frank 2021 (Nature) --
     hippocampal replay following aversive experience and context
     remapping; direct test of whether recently-invalidated place
     representations still appear in subsequent replay.
   - Karlsson & Frank 2009 (Nature Neurosci) -- awake replay of
     remote experiences; establishes the time-window over which
     past contexts remain replay-eligible.
   - Pfeiffer 2020 (Hippocampus) review on content of replay.
   - Genzel, Dragoi, Frank, Ganguli, Redish, Tononi (2020) -- review
     of replay-content literature including extinction contexts.

3. **Timing of trace integration during sleep**
   - Tambini & Davachi 2013, 2019 -- cross-state replay persistence
     and forward propagation (already cited in SD-032a; cite where
     relevant, do NOT re-pull).
   - Schlichting & Preston 2015, 2017 -- integration of previously-
     distinct contexts during sleep; whether newly-invalidated traces
     are integrated on the first post-invalidation sleep or only on
     subsequent bouts.
   - Lewis & Durrant 2011 (Trends Cogn Sci) -- overlapping replay
     hypothesis; schema-integration timecourse across multiple
     sleep bouts.
   - Diba & Buzsaki 2007 (Nature Neurosci) -- forward and reverse
     replay in sleep; whether the two modes sample start-states
     differently.

4. **Priority signals in sleep replay -- quantitative vs threshold**
   - Michon, Sun, Kim, Ciliberti & Kloosterman 2019 (Curr Biol) --
     post-learning replay prioritisation by behavioural relevance.
   - Joo & Frank 2018 review (Nat Rev Neurosci) -- hippocampal SWR
     content and priority signals.
   - Mattar & Daw 2018 (Nat Neurosci) -- normative model of replay
     prioritisation (EVB); predicts staleness-proportional priority
     under a well-specified utility function.
   - Whether empirical evidence matches the quantitative prediction
     or supports a threshold-gated scheme.

5. **Dual-trace extinction at the neural level**
   - Radulovic, Jovasevic & Meyer 2017 -- hippocampal context
     reinstatement after extinction; whether the extinguished trace
     remains accessible to replay.
   - Quirk & Mueller 2008 -- extinction is new learning, not erasure;
     biological grounding for dual-trace preservation.
   - Bouton 2004 (already cited in MECH-269/284/285 registration;
     re-use, do NOT re-pull).
   - Whether the Bouton dual-trace at the behavioural level is
     reflected in sleep-replay patterns -- does the inactive trace
     get replay bandwidth, and does that bandwidth track accumulated
     staleness?

6. **Neuromodulatory gating of replay priority**
   - Wang & Morris 2010; McNamara, Tejero-Cantero, Trouche, Campo-
     Urriza & Dupret 2014 -- dopaminergic tagging of replay-eligible
     experiences; whether staleness competes with or composes with
     dopamine-tag priority.
   - Swift, Gross, Frazer, Bauer, Clark, Vazey, Aston-Jones, Li,
     Pickering, Sara & Totah 2018 (Current Biology) -- LC-NE in
     sleep / post-learning consolidation.
   - Whether MECH-285 (epistemic-staleness priority) is dissociable
     from the salience-priority arm or is a composite.

## Architectural questions the lit-pull should help answer

1. **Seed-coverage (narrow vs broad).** Is the sleep-replay start-
   state distribution confined to currently-active ensembles
   (narrow), or does it span recently-invalidated traces for some
   window (broad)? Narrow -> MECH-285 implementation is the active-
   anchor-staleness biased sampler we already have infrastructure
   for. Broad -> MECH-285 must persist a region->seed map across
   `AnchorSet.mark_inactive`, and the staleness accumulator must
   continue writing to inactive regions (or be mirrored on a
   separate inactive channel).

2. **Priority shape.** Is empirical priority staleness-proportional
   (quantitative) or threshold-gated (qualitative)? Both are
   implementable; the biology should fix the default. Quantitative
   implies a softmax / power-weighted sampler; threshold implies a
   categorical "stale-enough-to-replay" flag.

3. **Timing.** Does replay of recently-invalidated traces appear on
   the first post-invalidation sleep bout, or with a delay? First-bout
   -> MECH-285 can be stateless (just reads the current staleness
   snapshot). Delay -> MECH-285 needs a temporal-window parameter
   (minutes-to-hours biological; tick-count in-silico) governing
   when inactive traces become replay-eligible.

4. **Interaction with salience.** Dopamine-tag priority (salience)
   and MECH-285 epistemic-staleness priority are ostensibly
   dissociable (MECH-285 spec explicitly says so). Does the
   literature support two distinct priority signals, or do they
   compose into a single weighted score? If compositional, the
   MECH-285 sampler must take both as inputs and arbitrate; if
   dissociable, they are independent write paths on the same
   replay-selection stage.

5. **Dual-trace at the replay-content level.** MECH-269's dual-trace
   preservation (Bouton) was validated at the anchor-set level by
   the V_s foundation pull. Does it also hold at the sleep-replay
   level -- does an inactive trace still generate SWR content? If
   no, the architectural commitment that "inactive anchors are
   retrievable" is narrower than assumed and MECH-285 narrow-mode
   is the only consistent implementation. If yes, broad-mode is
   the faithful reading.

## Output structure

Standard `targeted_review_*/` format. Suggested directory:
`evidence/literature/targeted_review_mech285_sleep_replay_seed/`

Per-paper records as usual (record.json + summary.md). After the pull,
write a short SYNTHESIS.md flagging:
- Seed-coverage verdict: narrow (active-only) vs broad (active +
  recently-inactive), with timing window for the broad case.
- Priority-shape verdict: staleness-proportional vs threshold-gated,
  with default parameter ranges for the in-silico sampler.
- Timing verdict: first-bout vs delayed, with the delay distribution
  if applicable.
- Salience-interaction verdict: dissociable independent signals vs
  composed weighted score.
- Dual-trace-at-replay verdict: does SWR content include inactive
  traces?
- Implementation recommendation: narrow / broad-window-N / broad-
  unbounded, with one-line rationale tying the recommendation to
  the specific verdicts above.

Estimated scope: ~10 papers, single session.

## Notes for the agent doing the pull

- The user is a consultant psychiatrist; clinical mappings welcome
  (e.g., PTSD intrusive-replay pattern as broad-coverage inactive-
  trace replay with MECH-094 tag loss; depressive rumination as
  narrow-coverage high-salience loop; novelty-blindness in
  schizophrenia as comparator-hypoactivity upstream of MECH-284).
- Re-use papers already pulled in prior V_s / connectome / routing /
  homeostatic-override pulls; cite where relevant, do NOT re-pull.
- The exemplar that motivates this pull is the MECH-285 implementation
  decision (narrow vs broad seed coverage) documented in
  `docs/architecture/v_s_invalidation_runtime.md` Status log entry
  2026-04-24 (Phase 3 online arm IMPLEMENTED) and Open design
  questions section Q4 (MECH-285 coupling magnitude).
- Connect to existing claim cluster: MECH-285 (sleep-priority readout
  target), MECH-284 (upstream staleness substrate, Phase 3 online
  arm landed), MECH-269 (dual-trace anchor-set preservation),
  MECH-273 (sleep self-model aggregation, downstream consumer of
  biased replay), MECH-275 (general sleep Bayesian aggregation,
  downstream consumer), MECH-094 (hypothesis-tag gating of
  replay-write paths; co-failure with MECH-285 produces PTSD
  architecture per claim 20249-20245).
- Be alert to evidence that the architecture should be revised. If
  empirical timing shows delayed integration (second-night or later
  for inactive traces), MECH-285 needs a temporal-gating parameter
  not currently in the substrate plan. If priority is threshold-
  gated rather than proportional, the sampler topology changes
  (categorical flag vs weighted distribution). If narrow-coverage
  is supported, the V_s invalidation runtime design doc open-
  question Q4 can be closed with minimal further architecture work;
  broad-coverage substantially expands MECH-285's state footprint.
