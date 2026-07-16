# ARC-057 ecological env-enablement -- route decision

- Status: **DECISION RECORDED 2026-07-16** -- do NOT `/implement-substrate` an
  ARC-057 environment now; the ecological env test is deferred to V4. The buildable
  node that reaches past the two mechanism validations is an env-FREE interaction
  spike (see section 6), not an environment build.
- Registered: 2026-07-16T15:12:13Z (session infallible-panini-0ba871)
- Claims touched: ARC-057, SD-024, SD-025 (no status change; this is a routing decision, not a promotion)
- Owner node: `substrate_queue.json` -> `hippocampal_module.curiosity_drive` (SD-025),
  `depends_on_unresolved: [ARC-057, MECH-111, INV-051]`

## 1. The question

Now that both ARC-057 components are implemented in ree-v3 -- SD-024
(`hippocampal_module.da_modulated_rbf_density`, main 402285a) and SD-025
(`hippocampal_module.curiosity_drive`, main c886d7c) -- what environment enablement
is needed to test the FULL (ecological) ARC-057 approach-emergence claim, and is that
enablement a `complicated (buildable)` substrate build or a `complex (probe-gated)`
design question first (per `docs/architecture/work_graph_debt_vocabulary.md`)?

ARC-057: *"Approach behavior toward reward locations emerges from the INTERACTION of
DA-mediated representational expansion (MECH-232 / SD-024) and an information-seeking
(curiosity) drive (SD-025) operating on the hippocampal map. Neither alone sufficient."*

The ARC-057 SUBSTRATE CONSTRAINT (claims.yaml ARC-057 notes; `sd_024_..md` Motivation):
the approach side needs *"an environment where representational expansion at a location
captures genuinely additional information -- not just the same sparse features at higher
fidelity ... The current CausalGridWorld cannot test ARC-057 faithfully. Testing the
approach side requires either a richer environment with location-dependent feature
complexity or a conceptual/mind-map space with variable information density."*

## 2. What is already done (verified 2026-07-16, do NOT rebuild)

Both mechanism validations PASSED, and both are **substrate-abstract diagnostics** --
they do NOT run the agent in CausalGridWorld at all:

- **V3-EXQ-766** (`v3_exq_766_..._20260716T062527Z_v3.json`, outcome **PASS**,
  `experiment_purpose=diagnostic`, `supports`): SD-024 representational expansion. Tests
  in synthetic RBF/z_world space -- a weight-INDEPENDENT density hill-climber approaches a
  reward cluster under DA-ON (L1a expansion ratio 2.40 >= 1.5; L2c approach-without-gradient:
  density-follower persists after ALL benefit weights are zeroed while a value-follower
  falls to chance). This is the MECH-232 discriminator against a valence-tag account.
- **V3-EXQ-767** (`v3_exq_767_..._20260716T073159Z_v3.json`, outcome **PASS**,
  `diagnostic`, `supports`): SD-025 curiosity drive PROPAGATES into CEM selection toward
  higher-density regions + the familiarity anti-perseveration discount.

Both are **single-mechanism** tests. **Neither is the ARC-057 interaction**, and neither
touches the environment. (Both PASSes are `diagnostic` and still route through
`/failure-autopsy` before they can move MECH-232 -- they are not yet governance-locked.)

There is **no** ARC-057 interaction experiment (queued or scripted) and **no** ecological
env-enabled test anywhere in `experiments/` or `experiment_queue.json` (queue is empty).

## 3. Three distinct tests -- the task's framing conflates two of them

| Test | What it exercises | Env needed? | Status |
|---|---|---|---|
| **A. Mechanism** (766, 767) | each drive in isolation, synthetic space | no | DONE (PASS) |
| **B. Interaction spike** (`sd_024_..md` Test Plan Phase 3) | SD-024 x SD-025 jointly; 4-arm ablation; interaction effect | **no** -- the SD-024 workaround supplies density internally | **does not exist; buildable now** |
| **C. Ecological** (the ARC-057 SUBSTRATE CONSTRAINT) | approach emerges when the *environment* carries genuine location-dependent information density that DA-expansion tracks | **yes** -- richer env or mind-map space | **not buildable now; V4** |

The task asks for "the env-enabled ecological interaction test" (Test C) but cites the
pass criterion "per the ARC-057 Test Plan Phase 3" (Test B). These are different tests.
**SD-024 is, by construction, the sanctioned WORKAROUND for the ARC-057 substrate
constraint** (claims.yaml SD-024 note: *"Workaround ... instead of requiring an
informationally rich environment, the hippocampal RBF layer itself creates more internal
structure at DA-modulated locations"*). Phase 3 as written runs on that workaround in a
plain grid world / synthetic space -- it needs NO environment change. The environment is
only required for the strictly stronger ecological claim (Test C).

## 4. Classification (work_graph_debt_vocabulary razor)

**Node = "environment enablement for the ecological ARC-057 test" (Test C).**

Recurse *"and is that buildable on demand?"*: **No.** Before any build there is an
unresolved design question, so the node is NOT `complicated (buildable)` and does NOT
route to `/implement-substrate`. It is **`complex (probe-gated)`**, and specifically a
**`mystery (known data)`**: we hold all the data (both mechanisms built + PASSing; the
constraint stated; the workaround built) and lack a *frame*, not a *fact*. The missing
frame is twofold:

1. **What does "location captures genuinely additional information" operationalize to**
   under the fleet invariant? The CausalGridWorld local_view is a fixed `5x5x7`
   one-hot tensor (`NUM_ENTITY_TYPES=7`, `local_view_dim=175`, fleet-invariant; every
   cloud worker's encoder input depends on it). In that tensor a cell IS a one-hot entity
   type -- "nothing more to discover at higher resolution" is *literally true*, exactly as
   the ARC-057 constraint says. Location-dependent complexity therefore cannot live in the
   local_view. It could live in *additional continuous field-views appended to
   `world_state`* (the established SD-049 `multi_resource_heterogeneity` proxy-field
   precedent adds 5x5 views WITHOUT touching the 175-dim local_view), but designing what
   those views *encode* so that RBF expansion captures genuinely additional environmental
   information -- and is not just the SD-024 internal fake relabelled -- is unresolved.
2. **What makes an ecological test non-redundant with the workaround?** The SD-024 doc's
   own "Why This Works in a Grid World" argues the mechanism *does not care* whether the
   density corresponds to environmental features. So the ecological test's entire value --
   showing approach tracks REAL environmental information structure, over and above the
   internal fake -- needs a frame that makes "real environmental information density" a
   measurable, dissociable quantity. That is a reframe, not a measurement. -> `mystery`.

**The cheaper probe comes first.** The correct spike is NOT the environment; it is Test B
(the interaction on the existing workaround), buildable now in the same substrate-abstract
style as 766. Test B is a `complex (probe-gated) / puzzle (known rules)` node -- the
mechanism is well-posed (keep the rules), we lack one fact (does the interaction fire when
both drives are on?). A green Test B supplies ARC-057 mechanism-level evidence AND
re-poses "is the ecological env worth building?"; a red Test B falsifies the composition
for pennies. This spike converts the whole line.

## 5. V3 vs V4 -- two independent gates make Test C premature for V3

**Gate 1 -- the env frame is unresolved and aligns with V4.** The constraint's own escape
hatch, *"a conceptual/mind-map space with variable information density,"* is not a grid
extension -- it is a different substrate owned by the V4 environment / object-representation
roadmap (`object_representation_v4_plan.md` and the `*_v4_plan.md` set). The grid-native
alternative is frame-blocked per section 4.

**Gate 2 -- the ecological test is agent-behavioural and hits the conversion/F-dominance
ceiling.** Test C requires the *agent* to exhibit multi-step committed APPROACH navigation
(curiosity-following-density -> sustained approach) *in an episode*. That is a
commitment-dependent behavioural test. Per the standing project ceiling (MECH-457
competence floor; F-dominance; the "don't queue commitment-dependent behavioural
experiments while the substrate can't sustain multi-step action-commitment" rule), a FAIL
would be **vacuous** -- confounded by the conversion ceiling, not by ARC-057. This is the
identical reasoning applied to MECH-077 on 2026-07-15 (behavioural content -> needs the
multi-step action-commitment layer = known conversion/F-dominance ceiling -> FAIL vacuous).
The ecological test is thus co-blocked on a V3-completion gate independent of the env.

Note both 766/767 sidestep BOTH gates precisely by being substrate-abstract (synthetic
density-follower, no environment, no agent commitment). Test B can be built the same way,
staying out of reach of the conversion ceiling. The moment the test demands the *agent*
approach in an *enriched environment*, it crosses into both gates -> V4.

## 6. Decision

1. **Do NOT `/implement-substrate` an ARC-057 environment.** The env-enablement node is
   `complex (probe-gated) / mystery (known data)` (frame-blocked, section 4) AND
   co-blocked on the conversion/F-dominance ceiling (Gate 2). **Defer the ecological
   Test C to V4** -- it belongs to the V4 environment / object-representation roadmap and
   is gated on conversion-ceiling closure. Forcing a grid env build now would produce a
   test whose FAIL is vacuous and whose "environmental information" is indistinguishable
   from the SD-024 internal fake.

2. **The buildable node that neither 766 nor 767 could reach is the env-FREE interaction
   spike (Test B / `sd_024_..md` Test Plan Phase 3).** Build it in the same
   substrate-abstract style as 766: a density-follower over the combined SD-024+SD-025
   machinery, 4-arm ablation (both-OFF / SD-024-ON+SD-025-OFF / SD-024-OFF+SD-025-ON /
   both-ON), pass = both-ON approach significantly exceeds either alone (interaction, not
   additive). This does NOT need the environment and its prerequisites (766, 767) are both
   green. Route it through `/queue-experiment` (its design pass must resolve the one open
   confound below); do NOT hand-write it.

   **Open design question for the spike (why it is `puzzle`, not free execution):** in the
   SD-024-ON + SD-025-OFF arm the benefit VALUE is conserved at the reward location (the DA
   cluster splits one encounter's intensity across centers; total mass preserved). A plain
   value/terrain follower could therefore approach *via the value gradient* in that arm,
   contaminating the "either alone" baseline and masking the interaction. The spike must
   isolate curiosity-driven approach from value-driven approach -- e.g. the 766
   weight-zeroing discriminator (remove the value field so only representational density
   can drive approach), or a density-only follower. Resolve in the `/queue-experiment`
   design pass before smoke-testing.

## 7. Follow-ups (governance hygiene, not done here to avoid high-contention edits)

- `substrate_queue.json` SD-025 entry still lacks `status: implemented` / `node_class`
  and its `depends_on_unresolved: [ARC-057, MECH-111, INV-051]` should be annotated as the
  **env/claim gate on the full ecological test (Test C, V4)**, not a gate on the (built)
  substrate -- exactly as the claims.yaml SD-025 note already flags. (Left for a governance
  cycle: substrate_queue.json is high-contention and this checkout is behind origin.)
- When Test B is queued, add a one-line pointer from `sd_024_..md` Test Plan Phase 3 to
  this decision doc so the "Phase 3 = env-free interaction spike, not the ecological test"
  distinction is visible at the design site.

## 8. References

- `docs/claims/claims.yaml`: ARC-057 (line ~21997), SD-024 (~19703), SD-025 (~19757).
- `docs/architecture/sd_024_da_modulated_rbf_density.md` (Motivation; Test Plan Phase 3).
- `docs/architecture/work_graph_debt_vocabulary.md` (the five tokens + razor).
- `ree-v3/ree_core/environment/causal_grid_world.py` (5x5x7 local_view invariant lines
  87/1155/3111-3125; SD-049 proxy-field-view precedent ~3189-3216).
- `evidence/planning/causalgridworldv2_env_extensions_spec.md` (the env-only-kwarg /
  bit-identical-OFF / contract-test extension pattern -- none of its primitives touched
  local_view).
- Mechanism results: `evidence/experiments/v3_exq_766_..._20260716T062527Z_v3.json`,
  `evidence/experiments/v3_exq_767_sd025_curiosity_drive_selection_bias/..._20260716T073159Z_v3.json`.
- Conversion-ceiling precedent: TASK_CLAIMS MECH-077 closure 2026-07-15 (behavioural claim
  -> conversion/F-dominance ceiling -> FAIL vacuous).
