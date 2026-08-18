**Status: AWAITING USER REVIEW** -- scoping spike, not an experiment, not a substrate build.

# Navigation immobility scoping spike -- CausalGridWorldV2, P0-trained agent

Generated: 2026-08-18T23:49:30Z
Session: `metaworker-chip-20260816-substrate-navigation-immobility-probe` (headless, chip
`chip-20260816-substrate-navigation-immobility-probe`)
Scope: cross-cutting scoping spike, triggered by a pre-authoring probe during the MECH-467
distractor-battery redesign (V3-EXQ-874b, `ree-v3` `73e5fa2ffa`).

## 0. What triggered this

While authoring V3-EXQ-874b, a pre-authoring probe measured a P0-trained REEAgent
(`run_p0_warmup`, 60 episodes x 80 steps) on `CausalGridWorldV2` (size 10, `num_resources=5`,
`num_hazards=0`), stepped 300 ticks with `operating_mode` pinned:

```
internal_planning: moved on 14 of 300 ticks, 9 unique cells, 0 consumption events
internal_replay  : moved on 14 of 300 ticks, 11 unique cells, 0 consumption events
```

Action histogram dominated by one value (untrained: action 3 on 150/150 ticks; after P0
warmup, roughly `{3: 227, 0: 70, 1: 2, 2: 1}` of 300). Shrinking to size 6 / `num_resources=6`
raised this to 3 consumption events per arm per 300 ticks. Toroidal wrap restores movement to
100% of ticks and then kills the agent (`agent_health` -> 0.0 by tick ~22-27, even at
`num_hazards=0`).

This chip's job: determine whether this is a new finding or an already-owned consequence, find
where the near-constant action comes from (by measurement/code, not reasoning), estimate how
many landed behavioural experiments could be silently affected, and characterise the
`agent_health` depletion under toroidal wrap. No new experiment or substrate change is in scope.

## 1. Is this already known/owned? -- Yes. Two already-tracked mechanisms, one active today.

**This is not a new finding.** It is the raw-navigation, CausalGridWorldV2 instance of two
separately-tracked, extensively-autopsied substrate phenomena that compound:

### 1a. E3 heartbeat hold-and-repeat (the amplifier)

`ree_core/heartbeat/clock.py:52` / `ree_core/utils/config.py:2577`:
`e3_steps_per_tick: int = 10  # E3 updates every 10 env steps (deliberation rate)`
(MECH-093-modulated to 5-20 steps depending on `z_beta` arousal -- not fixed at 10 in practice,
per `failure_autopsy_V3-EXQ-790_2026-07-22.md` and `diagnostic_arc071_e3_reselection_probe_2026-08-01.md`).
`clock.py` fires a genuine `e3_tick` only ~1-in-10 (or ~1-in-8-to-20) env ticks. On every other
tick, `ree_core/agent.py:6513-6548` (file header, `agent.py:30`: *"E3 selection is repeated
(MECH-057a: action-loop gate)"*) either steps a committed CEM trajectory or simply repeats
`_last_action` verbatim. So most of the 300-tick window is not re-selection at all -- it is one
E3 decision held for up to ~9-19 subsequent ticks.

This cadence/latching behaviour, and the sample-size-integrity hazard it creates for anyone
counting "ticks" as if each were an independent decision, is independently documented across
at least five prior autopsies and one dedicated diagnostic:
`failure_autopsy_V3-EXQ-708_2026-07-19.md`, `failure_autopsy_V3-EXQ-790_2026-07-22.md`,
`failure_autopsy_V3-EXQ-790-run2_2026-07-24.md`, `failure_autopsy_V3-EXQ-603e_hold_weighted_entropy_dv_2026-07-29.md`,
`failure_autopsy_V3-EXQ-924_2026-08-12.md`, `diagnostic_arc071_e3_reselection_probe_2026-08-01.md`.
None of these is about CausalGridWorldV2 raw movement specifically -- this probe is a new
*instance*, not a new *mechanism*.

### 1b. F-dominance in the E3 comparator (the source of the collapse itself) -- MECH-439

`ree_core/predictors/e3_selector.py`'s `select()` (~line 2421) scores candidates from several
channels (primary harm/goal score "F", `score_bias`, `score_diversity`, `channel_route_bias`,
...) before committing. **MECH-439** in `claims.yaml:70583` ("F-dominance bounds
committed-action diversity") is exactly this: *"the primary harm/goal score (F) monopolises
~88-89% of E3 committed-selection variance ... so modulatory, within-class, and rule-bias
diversity channels cannot convert to committed-action diversity while F dominates."*
`status: candidate`, `epistemic_category: standard`, `ceiling_decision: exhausted`,
`awaiting: ARC-107`. 9 confirmed `substrate_ceiling` failure-autopsy hits
(`689a/700/700a-d/709/711/713`; a 10th, 710, was withdrawn 2026-07-20 on re-adjudication) report
`action_class_entropy=0.0` in every arm with no positive discrimination on any richer substrate
tried so far.

**This is the same signature the MECH-467 autopsy already flagged** (`failure_autopsy_V3-EXQ-874_2026-08-03.md`):
zero target-consumption events across 900 real ticks under `internal_planning`/`internal_replay`.
It is also the identical signature **ARC-062's GAP-B falsifier lineage** carries across **21
autopsies** (`654g/654j/485h/485m/714/719a` and others, `claims.yaml:48024`): the minted
rule-apprehension bias demonstrably *reaches* the E3 accumulator with genuine modulatory
authority, but committed-class entropy never lifts, because the downstream conversion ceiling
(MECH-439) sits below it. `claims.yaml` explicitly cross-references ARC-062 GAP-B, dACC C2, and
SD-034 de-commit as independently hitting the *same* F-dominance root (`claims.yaml:1009-1013`).

**This is under active, sophisticated investigation right now -- as recently as today.** A
dedicated hypothesis-space-registry entry (`hypothesis_space_registry.v1.json`, qid
`e3_fdominance_causal_discrimination`, claims `[MECH-439, ARC-062]`, registered 2026-08-12 from
`failure_autopsy_V3-EXQ-925_2026-08-12`) tracks H1-H4 (literal-F vs primary-field vs upstream
insufficiency vs conditional specialisation) plus two hypotheses discovered *during* the
investigation itself: `H0-selector-regime-confound` (2026-08-12, from V3-EXQ-925's own replay
harness) and `H5-score-scale-uncontrolled` (**2026-08-18**, i.e. today, from
`failure_autopsy_V3-EXQ-936_2026-08-18.md`). V3-EXQ-925's frozen-replay causal harness itself
found something that complicates the naive "F wins the argmax" story: normalised selection
entropy 0.998 (near-uniform) and `committed_fraction=0.000` on this substrate -- i.e. selection
is closer to near-random softmax sampling over a candidate pool than a clean deterministic
capture, a nuance the *existing* investigation is still actively resolving (V3-EXQ-936, dated
today, adjudicated a `weakens` claim as vacuous due to unbounded score-magnitude growth --
unrelated bug, separately tracked). **This scoping spike does not attempt to add to that
resolution -- it is squarely owned by that in-flight line and re-deriving it here would
duplicate work already several sessions deep.**

**Distinguish from a sibling cluster, for accuracy**: `claims.yaml` also uses "monostrategy"
language for **MECH-269** ("V_s monostrategy" -- hippocampal-proposer representational
discriminability, a *precondition* for a context discriminator to route between policy heads,
`claims.yaml:40067`, cited in `ARC-062.depends_on` as the representational precondition,
distinct from the selection-variance mechanism). MECH-269 is about whether *regions* are
discriminably represented; MECH-439 is about whether the *selector* converts available signal
into committed-action diversity once representation exists. The raw single-agent, single-context
navigation probe here is a selection-layer phenomenon (matches MECH-439), not a
representational-discriminability one (MECH-269) -- both belong to the same broader
"conversion ceiling" family but are formally distinct claims and should not be conflated.

**Verdict: `puzzle (known rules)`.** The rules that explain this are already known and
extensively documented; nothing here is a `mystery (known data)` requiring reframing, and it is
not `aleatoric (irreducible)`. The deeper causal question underneath MECH-439 (which of
H0-H5 is correct) remains genuinely `complex (probe-gated)` -- but that probe is already running,
under an active session lineage, as of today.

## 2. Where the near-constant action comes from (measured, not reasoned)

Two mechanisms, additive, not competing:

1. **Structural amplifier -- E3 heartbeat hold** (`ree_core/heartbeat/clock.py`,
   `ree_core/agent.py:6513-6548`): ~85-90% of environment ticks are not re-selection at all;
   they repeat (or step through) whatever the last genuine E3 firing chose. This alone predicts
   that most of a 300-tick window will show one action value in long runs, regardless of what
   the selector itself does.
2. **Source of the value itself -- F-dominance / MECH-439**: when E3 *does* fire, the primary
   score (F) has historically monopolised the majority of committed-selection variance, and
   independent evidence from 21+9 confirmed autopsies shows this converts to
   `action_class_entropy ~ 0.0` under a wide range of conditions. V3-EXQ-925's own finding (near-
   uniform selection entropy, `committed_fraction=0.000`) means the live picture is more subtle
   than "F wins a clean argmax" -- selection may be closer to flat sampling over a candidate
   pool whose first-action composition was not itself characterised by this probe or by
   V3-EXQ-925/936. That open sub-question belongs to the existing causal-discrimination line,
   not to this scoping spike.

**Ruled out / not found**: a distinct "degenerate proposer" bug. `generate_candidates_random()`
(`ree_core/predictors/e2_fast.py:767`) shows no structural degeneracy in how candidates are
generated; the collapse is attributable to the comparator/selection stage, not candidate
proposal, as far as this spike's (and the E3-925 harness's) code reading goes.

**Additive but distinct -- wall-blocking**: `ree_core/environment/causal_grid_world.py:2333`
(`elif self.toroidal or self.grid[new_x, new_y] != self.ENTITY_TYPES["wall"]:`) silently absorbs
a movement action into a wall as a no-op (no position change). This is a genuine
"selected-but-blocked" contributor to low cell-visitation and is additive to (1)/(2), but by
itself cannot explain the skewed *action-value* histogram, since it doesn't change which action
was chosen -- only whether it moved the agent.

## 3. Scale of potentially-affected experiments (grep-scale estimate only, not re-autopsied)

Rough and almost certainly noisy in both directions:

- `ree-v3/experiments/*.py`: ~1266 of 1371 scripts (~92%) reference consumption/foraging/
  waypoint/resource-type terms somewhere -- a large over-count, since most of that is incidental
  (imports, unrelated telemetry, comments) rather than a scored DV that depends on reach
  actually completing.
- `REE_assembly/evidence/experiments/` manifests: only 7 carry an explicit top-level
  consumption/foraging/waypoint DV key (`v3_exq_634c_scaffolded_nursery_seeding_calibration_readiness`,
  `v3_exq_793_sd049_arm2_competence_calibration`, `v3_exq_793a_sd049_arm2_competence_repower`,
  `v3_exq_874b_mech467_distractor_three_leg_battery`, plus `arm_fingerprint_index.json`) --
  almost certainly an under-count, since most manifests carry these metrics nested inside
  `aggregate`/`interpretation` blocks rather than as literal top-level fields, which a plain grep
  misses.
- **What is NOT a rough estimate**: this exact failure mode (a reach-dependent DV silently
  starved to a 0/0 denominator by near-immobility) has already been directly confirmed once,
  autopsied, and repaired by redesign -- MECH-467 / V3-EXQ-874 -> 874b (shrink arena, raise
  resource density, extend window; see `failure_autopsy_V3-EXQ-874_2026-08-03.md` and the
  874b script header). And the *general pattern* (rule-biased/modulatory signal reaches E3 but
  committed-action diversity never lifts) is the confirmed signature across 21 ARC-062 GAP-B
  autopsies plus 9 direct MECH-439 hits -- i.e. at least 31 confirmed prior autopsy hits already
  document some variant of "this substrate does not diversify committed action under current
  defaults," independent of this scoping spike's own count.

**Recommendation, not performed here**: a small, mechanical corpus audit (grep every manifest
for its actual consumption/foraging/waypoint event-count field, wherever it is nested, and flag
near-zero counts against non-zero eval-tick budgets) would tighten this estimate from "grep-scale"
to "known." This is `complicated (buildable)` -- it needs no new experiment or substrate
change, only execution against data that already exists -- and is left for governance/the next
cycle to chip if it judges the corpus-QA gap worth closing now, rather than spawned unilaterally
by this scoping spike (out of this chip's stated scope, and better judged after this doc is
reviewed).

## 4. `agent_health` depletion under toroidal wrap: by-design footgun, not a bug -- but an
   effective defect for a "hazard-free" probe that doesn't know to opt out

`ree_core/environment/causal_grid_world.py:60-79` (module docstring, existing, not written by
this session) states this explicitly:

> "contamination_spread defaults to 0.5 and applies to EVERY cell the agent enters, regardless
> of num_hazards. A 'hazard-free' probe (num_hazards=0) therefore still kills its own agent:
> revisited cells cross contamination_threshold, become ENTITY_TYPES['contaminated'], and drain
> agent_health via contaminated_harm until the episode terminates far short of its configured
> step budget. V3-EXQ-884 died at 32/19/90 of 400 steps this way."

Mechanics, verified directly: `contamination_grid[x,y] += contamination_spread` (0.5/visit,
line ~2665) on every cell entry; once accumulated contamination crosses `contamination_threshold`
(default 2.0 -- two visits from lethal), the cell becomes `ENTITY_TYPES["contaminated"]`
(~line 2336-2337), and re-entry drains `agent_health -= contaminated_harm` (~line 2415),
independent of `num_hazards`. Toroidal wrap removes the walls that would otherwise channel
exploration into fresh territory, forcing revisitation of a small cell set -- so contamination
accumulates and crosses the lethal threshold within the ~22-27 ticks this probe observed. This
is the same class of self-inflicted-contamination death as the documented `V3-EXQ-884` precedent,
not a new mechanism.

**Verdict: by design**, with an existing opt-out (`contamination_spread=0.0`, the `V3-EXQ-513`
precedent, or `hazard_free_contamination_gate=True` for `num_hazards=0` configs) -- both off by
default for backward compatibility, per the same docstring ("Both flags are off by default so
every existing script is bit-identical"). In practice this behaves as a footgun for any new
`num_hazards=0` script that doesn't already know to pass one of those flags, but it is not an
undiscovered defect -- this probe rediscovered an already-documented behaviour, it did not find
a new one.

## 5. Routing summary

| Question | Debt classification | Action |
|---|---|---|
| Is the near-immobility a new finding? | `puzzle (known rules)` | No new work -- already MECH-439 (+ E3-cadence amplification), cross-linked above |
| Root cause of F-dominance itself (H0-H5) | `complex (probe-gated)` | Already an active, dedicated investigation line (hypothesis-space qid `e3_fdominance_causal_discrimination`); not this chip's job |
| Corpus-wide scale of affected experiments | `complicated (buildable)` | Recommended but not performed; leave for governance/next cycle to chip if warranted |
| `agent_health` toroidal depletion | resolved (by design) | No action; already documented, opt-out exists |

**No `/implement-substrate` or `/queue-experiment` routing from this chip.** No missing
mechanism is implicated (MECH-448/449/ARC-107 already exist as the in-progress repair route,
gated on further calibration -- `use_f_eligibility_demotion` defaults `False`, and even when
enabled needs a non-default `f_eligibility_envelope_floor` (0.10 vs stock 0.30) to engage the
No-Go axis per ARC-107's own 2026-08-16 evidence note), and no new experiment is warranted here
-- the live causal-discrimination line (V3-EXQ-924/925/936-and-successors) already owns that
question and is actively running.

## 6. Learning extracted

1. The near-immobility observed on raw CausalGridWorldV2 navigation is not a new substrate
   defect -- it is the plain-navigation instance of MECH-439 (F-dominance conversion ceiling,
   `ceiling_decision: exhausted`, awaiting ARC-107) amplified by the E3 heartbeat hold-and-repeat
   cadence (`e3_steps_per_tick`, MECH-093-modulated).
2. Any behavioural battery whose DV depends on the agent *completing* an approach/consumption/
   waypoint event under default E3 selection settings inherits this risk of a silently
   zero/near-zero denominator -- already confirmed once directly (MECH-467/V3-EXQ-874) and
   consistent with the pattern behind 21+9 confirmed prior autopsy hits on the same underlying
   mechanism family.
3. `agent_health` depletion under toroidal wrap is a known, documented, opt-outable footgun
   (`contamination_spread`/`hazard_free_contamination_gate`), not a new bug.
4. No degenerate-proposer defect was found; the collapse is attributable to the
   comparator/selection stage, consistent with the existing MECH-439 framing.
5. The deepest open question (why F/the selection regime behaves this way, H0-H5) is already
   being actively resolved by a dedicated causal investigation line, with a discovery event
   recorded as recently as today (2026-08-18, `failure_autopsy_V3-EXQ-936_2026-08-18.md`,
   `H5-score-scale-uncontrolled`). This scoping spike deliberately does not attempt to extend
   that resolution.
