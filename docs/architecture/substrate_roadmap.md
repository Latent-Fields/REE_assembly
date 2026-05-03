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
| Multi-source env dynamics (SD-047) | MECH-095 substrate_ceiling unblock; MECH-098, MECH-099 evaluable | 2026-05-03 |

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

#### 2. Multi-resource heterogeneity (qualitatively distinct resource types) -- **SD-049 (candidate, registered 2026-05-03)**

**Status (2026-05-03):** registered as **SD-049**
(`environment.multi_resource_heterogeneity`, candidate, v3_pending).
Design doc: `docs/architecture/sd_049_multi_resource_heterogeneity.md`.
Pre-implementation lit-pull complete (5 PubMed entries; lit_conf=0.898;
quadrant=plausible_unproven). Substrate code change blocked on
SD-047 (overlapping file -- both touch `causal_grid_world.py`); SD-049
implementation will layer on top once SD-047 changes are committed and
the file is stable. Substrate queue priority=1 alongside SD-047/048.

**Missing:** all current resources are interchangeable. The
goal/wanting/liking cluster (the largest non-conclusive cluster from the
2026-05-02 failure-landscape survey) needs scenarios where the agent
chooses *between* qualitatively distinct goals, not just whether to
approach a single resource type.

**Note (2026-04-13 atomic split):** MECH-112 was split into MECH-229
(behavioral wanting/liking dissociation, active) and MECH-230 (drive
coupling, gated on SD-012, provisional). The "MECH-112 22 entries"
historical citation refers to evidence accumulated under the pre-split
ID; current cohort is MECH-229 + MECH-230 + the listed downstream
claims.

**Claims unblocked:**
- `MECH-229` (active) wanting/liking behavioral dissociation -- enables
  the discriminative experiment (agent wants novelty cell while liking
  food cell). PASS evidence to date (EXQ-074f) was obtained on z_world
  fallback seeding, not via genuine identity-distinct wanting.
- `MECH-230` (provisional) goal-state latent structure -- z_goal latent
  becomes non-trivially multi-modal under multiple resource identities.
- `MECH-117` (stable) wanting/liking trajectory dissociation -- supports
  current stable rating with non-degenerate evidence.
- `MECH-216` (provisional) E1 schema-wanting -- schema generalisation
  across identity-distinct cues becomes testable.
- `ARC-030` (candidate) approach-avoidance symmetry across goal types.
- `ARC-032` (candidate) theta-routing across goal identities.
- `Q-030` (open) -- the 6-cell `z_resource × z_world` routing sweep
  needs multiple resource identities to make the routing question
  well-posed.
- `SD-015` (candidate) z_resource encoder -- the upstream substrate
  this enables; encoder currently has nothing to encode beyond
  presence (goal_resource_r=0.066 across EXQ-085x cluster).

**Substrate scaffold for downstream developmental schedules:** SD-049's
`resource_introduction_schedule: dict[str, int]` hook is the substrate
prerequisite for any curriculum design that introduces resource types
in stages. Defaults are inert (all types available from step 0); the
hook itself is not the developmental schedule, but downstream
curriculum design cannot be expressed without it.

**Implementation surface:** extend `CausalGridWorldV3` with
`resource_types: list[ResourceTypeConfig]` (3 types default:
food + water + non-homeostatic novelty) + per-axis homeostatic drive
system replacing SD-012's single scalar + curriculum-introduction hook.
Triggers `pending_substrate_reconfirmation` on SD-012-emergent
invariants per invariant-types governance rule. Validation: 4-arm
substrate gradient sweep (ARM_0 OFF / ARM_1 2-type homeostatic /
ARM_2 3-type default / ARM_3 5-type overshoot) with Woo/Spelke-style
falsifier branch (flat-failure on `wanting != liking` trajectory metric
routes MECH-229 to `substrate_conditional` with V4-1 multi-agent
ecology dependency, parallel to SD-047's Woo/Spelke branch). Lit-pull
provenance: `evidence/literature/targeted_review_sd_049/`.

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

#### 4. Multi-source environmental dynamics — **SD-047 IMPLEMENTED 2026-05-03**

**SD claim:** `SD-047` (`environment.multi_source_dynamics`, provisional).
Design doc: `docs/architecture/sd_047_multi_source_dynamics.md`.
**Implementation:** LANDED 2026-05-03 in `ree_core/environment/causal_grid_world.py`.
Calibration ratio 1.95:1 env:agent (within 1:1–2:1 target band). Bit-identical OFF
verified (7/7 preflight + 184/184 contracts PASS with master OFF).

**Previously missing:** "other-caused" change in V3 = hazard drift + resource
respawn + scheduled hazard injection. Too thin a causal background for
agency-detection-comparator claims. Now resolved.

**Claims unblocked (validation pending):**
- `MECH-095` (`substrate_ceiling`) TPJ agency-detection comparator —
  V3-EXQ-506 confirmed the substrate-ceiling signature (C4-only-PASS).
  SD-047 substrate is now in place. Validation: V3-EXQ-509 (substrate
  readiness diagnostic) → V3-EXQ-510 (4-arm noise-level sweep, Asai 2016
  inverted-U; Woo/Spelke falsifier routes to `substrate_conditional` if
  flat-failure).
- `MECH-098` (reafference cancellation) under stochastic afference
- `MECH-099` agency attribution downstream

**Validation still required** before MECH-095 `substrate_ceiling` flag can be
lifted. See SD-047 design doc interpretation grid for the 5-row outcome mapping.

#### 5. Interoceptive noise dynamics — **SD-048 REGISTERED 2026-05-03**

**SD claim:** `SD-048` (`body.interoceptive_noise_dynamics`, candidate, v3_pending).
Design doc: `docs/architecture/sd_048_interoceptive_noise_dynamics.md`.
Implementation dependencies: SD-011 (IMPLEMENTED), SD-022 (IMPLEMENTED) — ready to implement.

**Missing:** after SD-022, all `z_harm_a` variance is agent-caused (limb
damage from hazard contact) or deterministic (heal_rate). There is no
independent body-state background for the interoceptive comparator to
calibrate against. ARC-058's HarmForwardTrunk and ARC-033 E2_harm_a
cannot be honestly tested — a trivial forward model passes by memorising
action-damage coupling, not by learning to separate self-caused from
body-noise-caused change.

**Claims unblocked:**
- `ARC-058` (candidate) — HarmForwardTrunk Level 2 interoceptive
  comparator. V3-tractable but currently no substrate. SD-048 is the
  registered fix. Same 4-arm noise-level sweep validation as SD-047.
- `ARC-033` (provisional, competing) — independent-per-stream baseline
  benefits from same enrichment; arbitration runs on SD-048 substrate.
- `ARC-061` (candidate) — Level 2 contribution to reafference comparator
  family. ARC-061 cannot promote until Level 2 has experimental support.

**Implementation surface:** three stochastic body-state sources in
CausalGridWorldV3 body-state update: (1) autonomic background Gaussian
noise on harm_obs_a, (2) Poisson sensitisation spikes (multiplicative
transient amplification), (3) AR(1) fatigue drift. Bit-identical OFF
flag. Same calibration target as SD-047: 1:1–2:1 body-noise:agent-caused
harm-state-change events per episode.
See SD-048 design doc for full specification.

#### 6. Differentiated coping channels (single-agent multi-modal action repertoire)

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
| Multi-resource heterogeneity | H | MECH-229, MECH-230, MECH-117, MECH-216, ARC-030, ARC-032, Q-030, SD-015 | `SD-049` (registered 2026-05-03, candidate; substrate code blocked on SD-047 file release) |
| Long-horizon regime | H | INV-049, SD-037 dynamics, MECH-260 | (calibration / no SD) |
| Multi-source environmental dynamics | M | MECH-095, MECH-098, MECH-099 | `SD-047` (IMPLEMENTED 2026-05-03; validation V3-EXQ-509/510 pending) |
| Interoceptive noise dynamics | M | ARC-058, ARC-033, ARC-061 Level 2 | `SD-048` (registered 2026-05-03, ready) |
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
