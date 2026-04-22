# V_s Foundation Lit-Pull: Schema-Region Granularity, Multi-Map Coexistence, Per-Stream Verisimilitude

> Created: 2026-04-22
> Origin: Foundation work for MECH-269 base anchor selection + MECH-284 staleness +
> MECH-287 trigger. Three architectural choices in the implementation plan need biology
> validation before substrate edits. Earlier pulls covered: replay content/start-state
> (`targeted_review_connectome_mech_269/`), ephaptic substrate (`mech_270/`), routing
> (`mech_271/`), and waking V_s invalidation signal-types (`waking_v_s_invalidation/`).
> Gap: nothing yet validates (a) the *unit* over which V_s/staleness is indexed, (b)
> whether dual-trace maps onto coexisting ensembles for the same place, (c) per-stream
> vs per-ensemble verisimilitude computation.

## Prompt

/lit-pull Hippocampal foundation for MECH-269/284/287 substrate. Three converging
architectural questions: (1) **schema-region granularity** -- what is the biologically
natural unit over which a hippocampal verisimilitude signal indexes (place-cell field,
event/chunk boundary, action-object, learned schema)? (2) **multi-map coexistence at
the ensemble level** -- does the literature support multiple distinct place-cell
representations for the same physical location coexisting (rate remapping, global
remapping, splitter cells, multi-trace), as the substrate for MECH-269's dual-trace
anchor preservation? (3) **per-stream vs per-ensemble V_s** -- does hippocampal
verisimilitude/match-mismatch computation operate per modality/stream (allothetic vs
idiothetic, exteroceptive vs interoceptive) or per integrated ensemble, or both? The
architectural commitment to test: regions are environmentally-grounded chunks (grid
cell or action-object), V_s is per-stream (z_world, z_self, z_harm_s, z_harm_a,
z_goal), staleness is per-region indexed by the active anchor's location, dual-trace
is preserved by keeping inactive anchors in the anchor set with MECH-272 routing
deciding which is operative.

## Specific neurobiological systems to cover

1. **Place-cell remapping types and multi-map coexistence**
   - Colgin, Leutgeb & Moser 2010 (review of rate vs global remapping)
   - Leutgeb et al 2007 (rate remapping = same ensemble, different rates; global =
     different ensemble entirely; CA1 vs CA3 differ)
   - Wills et al 2005 (gradual transformation between maps under cue morphing)
   - Whether multiple maps for the same place can coexist as the substrate for a
     dual-trace inactive-but-retrievable anchor

2. **Splitter cells and context-dependent firing**
   - Wood et al 2000 (CA1 splitter cells: same place, different firing depending on
     past or future trajectory context)
   - Frank, Brown & Wilson 2000 (prospective coding)
   - Whether splitter cells are evidence that anchor-state is composed of (place,
     stream-mixture) rather than place alone

3. **Schema cells and event boundaries**
   - Tse, Langston, Kakeyama, Bethus, Spooner, Wood, Witter & Morris 2007 (hippocampal
     schemas; rapid one-trial encoding into existing schema)
   - DuBrow & Davachi 2014 (event boundaries segment continuous experience)
   - Brunec & Momennejad 2022 (hippocampal events as schema chunks)
   - Whether the natural granularity of hippocampal "chunks" matches grid-cell-level
     or action-object-level discretization, or operates at a higher event-segment
     scale

4. **Multi-trace theory at the population level**
   - Nadel & Moscovitch 1997 (multiple-trace theory; each retrieval creates a new
     trace, old traces persist)
   - Yonelinas, Ranganath, Ekstrom & Wiltgen 2019 (CMS / multi-trace synthesis)
   - Whether dual-trace at the *anchor* level (active + inactive coexist, routed by
     state) matches the population-level evidence on multi-trace persistence

5. **Per-modality vs integrated hippocampal coding**
   - Eichenbaum 2017 (memory space: time cells, place cells, event cells)
   - O'Mara, Sanchez-Vives, Brotons-Mas & O'Hare 2009 (subiculum integration of
     allothetic and idiothetic streams)
   - Whether match/mismatch detection in hippocampus is per-stream (allothetic vs
     idiothetic, exteroceptive vs interoceptive) or per integrated representation

6. **Comparator function in hippocampus**
   - Vinogradova 2001 (hippocampus as comparator; CA1 as match/mismatch detector
     between CA3 retrieval and EC input)
   - Lisman & Grace 2005 (novelty detection via VTA loop; CA1 mismatch upstream)
   - Whether the comparator is per-stream or per-population, and whether it directly
     drives the broadcast trigger (substrate candidate for MECH-287 anchor-side)

## Architectural questions the lit-pull should help answer

1. **Region granularity.** Are hippocampal "schema regions" naturally place-cell-field
   sized (grid cell), action-object sized (sequence chunk), or event-segment sized
   (multiple actions bound by a context boundary)? The architectural commitment is
   tractable at any of these scales but the biology should constrain the default.

2. **Multi-map coexistence as dual-trace substrate.** Does the literature on rate vs
   global remapping support multiple distinct ensembles for the same place coexisting
   in a way that could route by state? If yes, MECH-269's dual-trace preservation has
   direct biological backing. If only rate remapping (same ensemble, different rates),
   the implementation should reflect that — anchors aren't fully separable, just
   differentially weighted.

3. **Per-stream vs integrated V_s.** The substrate plan computes V_s per stream
   (z_world, z_self, etc.). Is this consistent with hippocampal comparator biology,
   which appears to operate at the CA1 ensemble level on integrated CA3 retrieval vs
   EC input? If V_s is fundamentally integrated, per-stream V_s is an in-silico
   computational convenience that needs to be flagged as architecture-deviates-from-
   biology rather than architecture-grounded-in-biology.

4. **Splitter-cell evidence for (place, context) coding.** If splitter cells are
   robust, anchors should be (place, stream-mixture) rather than just place — and the
   stream-mixture is the context that disambiguates which anchor is active under
   MECH-272 routing. If splitter cells are a small minority phenomenon, the
   architectural lift is harder to justify.

5. **Trigger substrate from comparator function.** Vinogradova / Lisman & Grace
   suggest CA1 mismatch detection feeds VTA novelty signals. Is this a candidate
   anchor-side substrate for MECH-287 distinct from the broadcast LC/DA trigger
   (which is amygdala/cortex-side)? If yes, MECH-287 may need to register both an
   anchor-side comparator-fed component AND a broadcast LC/DA component, with
   crosstalk.

## Output structure

Standard `targeted_review_*/` format. Suggested directory:
`evidence/literature/targeted_review_v_s_foundation/`

Per-paper records as usual (record.json + summary.md). After the pull, write a short
SYNTHESIS.md flagging:
- Recommended region granularity (place-cell-field / action-object / event-segment)
  for the in-silico foundation, with one-line justification per option considered.
- Whether dual-trace at the anchor level has direct biological support or is an
  in-silico extension requiring an architectural-deviation note.
- Whether per-stream V_s is biologically supported or an in-silico convenience.
- Whether the splitter-cell literature supports (place, stream-mixture) anchor
  encoding.
- Whether MECH-287 needs an additional CA1-comparator anchor-side component
  alongside the broadcast LC/DA trigger.

Estimated scope: ~10 papers, single session.

## Notes for the agent doing the pull

- The user is a consultant psychiatrist; clinical mappings welcome (e.g., remapping
  failure as substrate for context-binding deficits in PTSD; comparator hypoactivity
  as substrate for novelty-blindness in schizophrenia).
- Pfeiffer & Foster 2013, Dragoi & Tonegawa 2011/2013, Tang 2017, Foster 2017,
  Olafsdottir 2018, Anastassiou 2011, Buzsaki 2015, Girardeau 2017, Jadhav 2016
  are already pulled in `targeted_review_connectome_mech_{269,270,271}/` -- do NOT
  re-pull; cite where relevant.
- Schultz 1997, Matsumoto 2007, Bromberg-Martin 2011, Wilson 2014, Stalnaker 2015,
  Gardner 2018, Yassa-Stark 2011, Reagh 2018, Gershman 2010/2017, Bouton 2004,
  Sara-Bouret 2012, Aston-Jones-Cohen 2005 already in
  `targeted_review_waking_v_s_invalidation/` -- cite where relevant.
- The exemplar that motivates this pull is the substrate foundation work for
  MECH-269/284/287 implementation; design doc at
  `docs/architecture/v_s_invalidation_runtime.md`.
- Connect to existing claim cluster: MECH-269 (anchor selection + reset), MECH-272
  (state-gated routing -- load-bearing for dual-trace mixture), MECH-094 (hypothesis
  tag interaction with anchor-reset events), MECH-284/285/287 (V_s bidirectional
  cluster + trigger).
- Be alert to evidence that the architecture should be revised. If multi-map
  coexistence is NOT supported (e.g., if remapping is exclusively winner-take-all),
  the dual-trace mechanism may need to be implemented as soft re-weighting rather
  than hard active/inactive flags. If V_s is exclusively integrated (no per-stream
  computation in biology), the in-silico per-stream V_s is a deviation that needs a
  rationale in the architecture doc.
