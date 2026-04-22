# V_s Foundation -- Targeted Literature Pull Synthesis

Date: 2026-04-22
Scope: Validate the foundation plan for MECH-269 (anchor selection), MECH-284 (V_s residual staleness accumulator), MECH-287 (broadcast invalidation trigger), MECH-272 (anchor/probe routing), and MECH-094 (hypothesis tag) substrate work.

Entries: 12 papers across 6 neurobiological systems (place-cell remapping, attractor dynamics, splitter/trajectory cells, schema cells/event boundaries, multi-trace/pattern-separation, comparator/HC-VTA loop, subicular routing).

---

## 1. Recommended schema-region granularity

**Recommendation: default to schema/event-segment scale; support multi-scale; do NOT treat place-cell-field as the canonical unit for V_s gating.**

Eichenbaum 2017 establishes that hippocampal coding is multi-dimensional mixed-selectivity at the cell level, with the relevant organisation scale emerging from task structure rather than being fixed. Tse 2007 schemas operate at the level of integrated event/context structures, not individual place fields. Sols/DuBrow/Davachi 2017 shows event boundaries (not place transitions) are the functional units that drive reinstatement and consolidation priority.

For V_s computation to be both (a) tractable and (b) biology-faithful, the substrate should treat the event-segment / action-object / schema-region as the primary granularity unit, with place-cell-field-scale resolution available where the task demands it. A fixed-place-field substrate would be biologically too fine and would lose the schema-level abstraction that drives consolidation in Tse 2007 and event reinstatement in Sols 2017.

Caveat: Eichenbaum's "granularity emerges from task" position implies a fully principled substrate would not architecturally fix granularity at all. The substrate plan's commitment to environmentally-grounded chunks (event segments / action objects) is a pragmatic simplification consistent with the 2017 multi-dimensional code framing.

## 2. Multi-map coexistence as substrate for MECH-269 dual-trace

**Recommendation: dual-trace at the anchor level has direct biological support; substrate should support BOTH hard-switching (global remapping) AND soft re-weighting (rate remapping), not commit to one.**

Wills 2005 (attractor morphing) provides the strongest single result: the hippocampal ensemble shows bistable switching between two distinct attractor states under graded morphing of the input -- a winner-take-all anchor-selection signature at the population level. Leutgeb 2007 (DG/CA3 pattern separation) confirms distinct CA3 ensembles can coexist for highly similar inputs, with DG providing the orthogonalising gate. Together these establish the substrate-level mechanism for dual-trace anchor preservation: distinct ensembles can encode alternative interpretations of the same input.

Colgin 2008 complicates this: rate remapping is also real, and many natural transitions show graded re-weighting rather than hard switching. Frank 2000 and Wood 2000 (splitter/trajectory cells) show context-dependent firing that operates partly through rate modulation of the same place fields rather than always through full remapping.

Substrate implication: MECH-269 dual-trace should support both modes -- a hard anchor switch (Wills 2005 attractor flip) AND soft mixture re-weighting (Colgin rate remapping). MECH-272 routing decisions could then treat the choice between them as a function of V_s magnitude and input ambiguity, not commit to one regime architecturally.

## 3. Per-stream V_s -- biology faithful or computational convenience?

**Recommendation: per-stream V_s is a projection-readout of a mixed-selectivity integrated code, NOT a biology-deviating per-stream computation. Frame this explicitly in the substrate plan to avoid mis-claiming per-stream as the biological computation.**

Eichenbaum 2017 is the strongest constraint here: hippocampal CA1 carries multiplexed independent representations of multiple dimensions with mixed selectivity at the single-cell level. Biology computes a single integrated mixed code; per-stream readout is a downstream extraction.

Vinogradova 2001 supports the principle that biology computes mismatch between functionally distinct streams (brainstem-reticular vs cortical) rather than a single integrated mismatch -- but the original framework has two streams, not five. The substrate plan's five-stream V_s (z_world, z_self, z_harm_s, z_harm_a, z_goal) is a more granular extension; the principle (per-stream rather than integrated mismatch) is biologically grounded but the specific number of streams is an engineering choice.

Yonelinas 2019 contextual-binding theory supports that high-resolution contextual binding fails at high load, implying the integrated code can degrade into something more like per-stream computation under capacity constraints -- giving the substrate plan an additional grounding for per-stream readout as a recoverable fallback when the mixed code cannot be cleanly re-extracted.

Substrate implication: register per-stream V_s as a projection-readout of an integrated mixed-selectivity substrate, not as the biological computation itself. The architecture is faithful via the projection; the per-stream extraction is a computational convenience that surfaces existing information.

## 4. Splitter-cell support for (place, stream-mixture) anchor encoding

**Recommendation: splitter-cell literature strongly supports anchor encoding that conditions on both location and a stream-mixture (trajectory / context) signal; substrate should support both pure-place and mixed (place + stream-mixture) anchor types.**

Wood 2000 provided the foundational splitter-cell result: in continuous-alternation tasks, ~one third of CA1 place cells show context-dependent firing (e.g. fire on stem only on left-trial vs right-trial laps), with ~one third pure-place. Frank 2000 confirmed in W-maze tasks that prospective and retrospective trajectory information is encoded in CA1/CA3 firing during the shared stem.

Two substrate implications. (1) Anchor representations conditional on a stream-mixture signal (trajectory, context, intent) are biologically standard, not exotic. MECH-269 should support such conditioning. (2) Pure-place anchors also exist (~one third in Wood 2000) -- the substrate should not force every anchor to be stream-conditional. A mix of pure-place and stream-conditioned anchors is the biological pattern.

Caveat: splitter-cell literature is task-specific (continuous alternation, W-maze). The exact one-third / one-third / one-third split observed in Wood 2000 is task-dependent and should not be hard-coded into the substrate. The architectural commitment is to support both types, not to fix the ratio.

## 5. MECH-287 anchor-side comparator component (alongside broadcast LC/DA trigger)

**Recommendation: MECH-287 should register a dual-component architecture -- an anchor-side CA1/CA3-comparator-derived component AND the LC/global-DA broadcast component. These are coupled stages, not alternatives.**

Lisman & Grace 2005 articulates the hippocampal-VTA loop: hippocampus detects novel information via a comparator function and conveys it via subiculum-NAc-VP to VTA, which then back-projects dopamine to enhance hippocampal LTP. This makes the broadcast trigger a TWO-component signal: (a) hippocampal mismatch (the comparator-derived upstream source), and (b) VTA dopamine release (the broadcast). They are coupled stages of the same trigger event.

Vinogradova 2001 provides the comparator-side mechanism: CA3 computes match/mismatch between two functionally distinct input streams and the resulting signal gates both intra-hippocampal output AND subcortical arousal modulation. This is the upstream anchor-side comparator component that flows into the Lisman & Grace loop.

O'Mara 2009 confirms the anatomical pathway: subiculum is the routing hub through which hippocampal mismatch reaches NAc-VP-VTA. The broadcast trigger does not bypass this pathway -- it flows through it.

Sols/DuBrow/Davachi 2017 supports the same architecture from the event-boundary side: event boundaries (which behave like local mismatch signals) drive reinstatement and consolidation priority -- matching the Lisman/Vinogradova prediction that local mismatch is the upstream source of broadcast events.

Substrate implication: MECH-287 should register both components and document their coupling. The current waking-V_s lit-pull captures the LC/DA broadcast component (Schultz, Sara-Bouret, Aston-Jones-Cohen). This pull adds the anchor-side comparator component (CA1/CA3 mismatch flowing through subicular routing to broadcast generators). Treating these as alternatives rather than coupled stages would miss the loop architecture biology actually uses.

---

## Cross-cutting failure modes flagged

- Treating MECH-269 dual-trace as either hard-switching XOR soft re-weighting; biology supports both regimes.
- Committing to place-cell-field as the V_s granularity unit; biology operates at event-segment / schema scale for the relevant computations.
- Framing per-stream V_s as the biological computation rather than as a projection-readout of an integrated mixed-selectivity code.
- Treating the broadcast trigger and the anchor-side comparator as alternative trigger sources; they are coupled stages of the same event.
- Treating MECH-272 routing as internal to anchor representations rather than at a dedicated downstream routing layer (subicular fan-out pattern).
- Committing to the 2009 description of subicular code as canonical (substantial subsequent refinement).
- Hard-coding the splitter-cell ratio (one-third pure-place in Wood 2000) into the substrate; ratio is task-dependent.

## Confidence summary by claim

| Claim | Coverage | Direction | Notes |
|---|---|---|---|
| MECH-269 (anchor selection) | 9/12 entries | supports | dual-trace at anchor level well-supported; both hard switch and soft re-weighting biologically present |
| MECH-272 (anchor/probe routing) | 7/12 entries | supports | routing layer downstream of anchor representation; subicular fan-out pattern |
| MECH-287 (broadcast trigger) | 4/12 entries | supports | dual-component architecture (anchor-side comparator + LC/DA broadcast) |
| MECH-094 (hypothesis tag) | 2/12 entries | supports (weak) | event-boundary reinstatement and schema integration consistent with categorical write-gate semantics |
| MECH-284 (V_s residual staleness) | 1/12 entries | supports (weak) | contextual-binding load-degradation provides one mechanism; pull does not deeply test this claim |

Confidence values per entry are recorded in each record.json with confidence_components decomposition.
