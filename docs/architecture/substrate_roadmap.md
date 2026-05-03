# Substrate Roadmap (V3 enrichment planning)

> Planning artifact, not a spec. Captures the V3 substrate enrichments
> required to unblock claims currently sitting at `epistemic_category:
> substrate_ceiling` or `substrate_conditional`. Updated when new
> ceiling-bound claims surface or substrate features land.

## Why this document exists

Phase 3 wave 2 of the Option E lit/exp decoupling exposed that ~141
claims sit at lit-only / zero-exp / quadrant=plausible_unproven. Many of
these are V3-tractable in principle but blocked on substrate features
that have not yet landed. The reactive cycle (claim fails → diagnose
substrate gap → add substrate → re-test) works but is slow because the
diagnosis happens AFTER an experiment burns through trying. This
roadmap converts the reactive cycle into a deliberate plan: enumerate
the substrate gaps, map them to the claims they'd unblock, and
prioritise.

The companion document for the V4-bound cohort is
`docs/architecture/v4_spec.md` -- claims that need multi-agent ecology,
richer action repertoire, or longer time horizons than V3 can supply.
This roadmap is the V3-tractable counterpart.

## Methodology

For each substrate gap:
1. Name the missing feature (one substrate-level capability)
2. List claims that would clear if it lands (with their current
   `epistemic_category` if non-default)
3. Note the implementation surface (which `ree_core/` modules + which
   `SD-*` claim would register the substrate change)
4. Priority: H / M / L based on cohort size + downstream dependency
   density

## In-flight enrichments (already partial / landing)

These are substrate features added between 2026-04-01 and 2026-05-02
that unblocked specific claim cohorts. Listed for context -- the
roadmap below is everything still outstanding.

| feature | claims unblocked | landed via |
|---|---|---|
| Limb damage body-state (SD-022) | SD-011 dual-stream sub-claims | 2026-04-09 |
| Gradient texture / landmarks (SD-023) | MECH-216, ARC-051 | 2026-04-09 |
| Scheduled external hazards (SD-029 substrate) | C2/C3 SD-029 measurement | 2026-04-21 |
| Amygdala analog (SD-035) | MECH-074 family + V3-EXQ-501 PASS | 2026-04-21 |
| GABAergic decay (SD-036) | PAG freeze gate + SD-037 chain | 2026-04-22 |
| Orexin override (SD-037) | EXQ-483 catatonic-lock follow-ups | 2026-04-25 |
| V_s invalidation runtime (MECH-269 family + MECH-269b) | MECH-287, MECH-288, MECH-284, MECH-285 cluster | 2026-04-22..04-29 |
| Sleep aggregator (MECH-272/273/275/285) | INV-049 sleep cluster + V3-EXQ-503 PASS | 2026-04-25 |
| Ghost-goal substrate (SD-039 + MECH-292/293) | MECH-292/293/SD-039 trio | 2026-04-26..04-27 |
| MECH-295 liking-bridge | EXQ-490 successors for Q-040 | 2026-04-26 |

## Outstanding V3 enrichments

### H-priority

#### 1. Foreclosure primitives (terminal grid states + resource extinction + agent-state lock-in)

**Missing:** CausalGridWorldV2 has hazard drift (recoverable) and
resource respawn (recoverable). It has no genuine *foreclosure* of
state-space reachability -- no terminal grid cells, no
permanently-extinct resources, no agent-state values that lock in.

**Claims unblocked:**
- `Q-027` (`derivational` + partial substrate) -- substrate-validation of
  the irreversibility-under-uncertainty definition needs foreclosure
  primitives.
- `MECH-097` (peripersonal space commit locus) -- commit boundary
  semantics need a real "no going back" condition.
- `INV-025` (irreversible-class harm) sub-claims that depend on
  foreclosure being real.

**Implementation surface:** new `CausalGridWorldV2` flags --
`terminal_cells: list[(x,y)]`, `resource_extinction_on_consume: bool`,
`damage_lock_threshold: float`. Probably one new SD claim
(`environment.foreclosure_primitives`) registering the addition.

#### 2. Multi-resource heterogeneity (qualitatively distinct resource types)

**Missing:** all current resources are interchangeable. The
goal/wanting/liking cluster (the largest non-conclusive cluster from the
2026-05-02 failure-landscape survey: MECH-112 22 entries, SD-012 16,
SD-015 13, ARC-030 10, MECH-216, MECH-117, ARC-032) needs scenarios
where the agent chooses *between* qualitatively distinct goals, not
just whether to approach a single resource type.

**Claims unblocked:**
- `MECH-112` wanting/liking dissociation
- `MECH-117` schema readout when targets differ in identity
- `MECH-216` predictive wanting on identity-distinct cues
- `ARC-030` go/nogo symmetry across goal-types
- `Q-030` (`standard`) -- the 6-cell z_resource × z_world routing sweep
  needs multiple resource identities to make the routing question well-
  posed.

**Implementation surface:** extend `CausalGridWorldV2` with
`resource_types: list[str]` + per-type `benefit_profile`. SD claim:
`environment.multi_resource_heterogeneity`.

#### 3. Long-horizon dynamics (thousands-of-steps regimes)

**Missing:** episode lengths are typically 100-300 steps; chronic /
sensitisation phenomena need 10k+ step regimes. Sleep aggregation
work (MECH-272/273/275/285) partly addresses this for the offline
side; the waking side still saturates well before sensitisation
signatures appear.

**Claims unblocked:**
- `INV-049` waking-vs-offline necessity -- chronic-pain sensitisation
  signature requires sustained exposure.
- `SD-037` orexin override -- recruitment dynamics over hours.
- The pACC drive_bias accumulation (already implemented per SD-032e)
  is timescale-bound; long-horizon regime is the test condition.
- `MECH-260` dACC bias suppression -- the recency-bias-suppression
  signature is hard to disambiguate from bias decay at short horizons.

**Implementation surface:** `experiment_runner.py` long-run mode
(checkpointed sleep cycles + waking phases); env-side `episode_length`
unification. Probably no new SD; just calibration + tooling.

### M-priority

#### 4. Multi-source environmental dynamics — **SD-047 REGISTERED 2026-05-03**

**SD claim:** `SD-047` (`environment.multi_source_dynamics`, candidate, v3_pending).
Design doc: `docs/architecture/sd_047_multi_source_dynamics.md`.
Implementation dependencies: SD-022 (IMPLEMENTED), SD-029 (IMPLEMENTED) — ready to implement.

**Missing:** "other-caused" change in V3 = hazard drift + resource
respawn + scheduled hazard injection. That's a thin causal background.
Agency detection and similar comparator-driven claims need a richer
multi-source environment.

**Claims unblocked:**
- `MECH-095` (`substrate_ceiling`) TPJ agency-detection comparator —
  V3-EXQ-506 confirmed the substrate-ceiling signature (C4-only-PASS).
  SD-047 is the registered fix. Validation uses a 4-arm noise-level sweep
  (Asai 2016 non-monotonicity grounds the inverted-U prediction; Woo/Spelke
  falsifier branch routes to V4-bound `substrate_conditional` if flat-failure).
- `MECH-098` (reafference cancellation) under stochastic afference
- `MECH-099` agency attribution downstream

**Implementation surface:** three concurrent stochastic sources added to
CausalGridWorldV3: (1) AR(1) spatial perturbation field, (2) Poisson
transient events, (3) background drift sources. Bit-identical OFF flag.
Calibration target: 1:1–2:1 env:agent change events per episode.
See SD-047 design doc for full specification.

#### 5. Differentiated coping channels (single-agent multi-modal action repertoire)

**Missing:** V3 agent has 5 actions (4 cardinal moves + noop). MECH-102
"violence as terminal error-correction triggered only when all other
channels fail" requires *channels* to fail through. Five actions don't
constitute meaningful distinct pathways.

This sits at the V3/V4 boundary. The pure version (multi-agent social
coping) is V4-bound (see v4_spec.md). A V3-tractable lite version
exists: extend the action repertoire so that the agent has structurally
distinct intervention modes (e.g. communication-analog action,
manipulation-analog action, withdrawal-analog action) without requiring
multiple agents.

**Claims partly unblocked:**
- `MECH-102` (`substrate_ceiling`) -- a V3-lite test could probe the
  structural signature even without full multi-agent ecology.

**Implementation surface:** action-space extension; significant. SD
claim: `environment.differentiated_coping_channels` (V3-lite) +
acknowledge that full validation moves to V4.

### L-priority (nice-to-have, not blocking)

#### 6. Multi-frequency oscillatory probes

For control-plane-heartbeat work (ARC-023, MECH-089/090/091). Already
mostly serviced by the existing heartbeat substrate; deeper probes
would help.

#### 7. Persistent agent identity across episodes

For some of the maturational sequence claims (INV-064, MECH-214,
MECH-215). Currently each episode is fresh; persistent body state /
self-model across resets would unlock "what does the agent have
learned about itself?" probes.

## Substrate-feature → claim mapping summary

| feature | priority | claim cohort | SD candidate |
|---|---|---|---|
| Foreclosure primitives | H | Q-027, MECH-097, INV-025 sub-claims | `environment.foreclosure_primitives` |
| Multi-resource heterogeneity | H | MECH-112, MECH-117, MECH-216, ARC-030, ARC-032, Q-030 | `environment.multi_resource_heterogeneity` |
| Long-horizon regime | H | INV-049, SD-037 dynamics, MECH-260 | (calibration / no SD) |
| Multi-source environmental dynamics | M | MECH-095, MECH-098, MECH-099 | `SD-047` (registered 2026-05-03, ready) |
| Differentiated coping channels (V3-lite) | M | MECH-102 (lite); full -> V4 | `environment.differentiated_coping_channels` |
| Multi-frequency oscillatory probes | L | ARC-023, MECH-089/090/091 deeper | (probe expansion / no SD) |
| Persistent agent identity | L | INV-064, MECH-214, MECH-215 | `agent.persistent_identity_across_episodes` |

## How this roadmap is used

1. When a `substrate_ceiling` claim is annotated, the
   `evidence_quality_note` should reference the substrate feature(s)
   that would unblock it (point at this roadmap entry by name).
2. When a substrate feature lands (new SD claim), this roadmap moves
   the entry into the "in-flight enrichments" table above and the
   relevant `epistemic_category: substrate_ceiling` claims may be
   re-evaluated -- some will move to `standard`, others may move to
   V4-bound.
3. The H-priority items inform what SD work to queue when there's
   substrate-design bandwidth.

## V3/V4 boundary

This roadmap covers V3-tractable work. Claims that require multi-agent
ecology, social systems, or fundamentally different substrate primitives
move to `docs/architecture/v4_spec.md`. The boundary is not always
obvious from the claim text -- the discriminator is whether the
substrate feature can be added incrementally to CausalGridWorldV2 (V3)
or whether it requires a new substrate generation entirely (V4).
