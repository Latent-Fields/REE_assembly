# GOV-DIAG-1 re-operationalization: `fishtank_906_lineage_ecology_showcase`

**Generated:** 2026-08-14T01:18:49Z
**Session:** `metaworker-chip-20260812-govdiag1-repose-fishtank906` (headless dispatch)
**Chip:** `chip-20260812-govdiag1-repose-fishtank906`
**Routing source:** `/governance` 2026-08-12 (session `sd-016-h3-algorithm-3370cd`), GOV-DIAG-1
standing audit (governance SKILL.md step 6a-v-ter)

**PROMOTES NOTHING. DEMOTES NOTHING.** No `claims.yaml` edit. No experiment queued. No manifest
`evidence_direction` changed. This artifact plus one `diagnostic_recurrence_metabolized` marker
on `arc_062_rule_apprehension:GAP-B` are the whole of this session's writes.

---

## The signal

`bears_on` token `fishtank_906_lineage_ecology_showcase` reached the N=3 threshold of
pure-diagnostic (`claim_ids: []`) no-verdict hits:

| # | run_id | queue_id | outcome | evidence_direction |
|---|---|---|---|---|
| 1 | `v3_exq_906b_full_stack_observational_fishtank_20260809T163034Z_v3` | V3-EXQ-906b | PASS | `non_contributory` |
| 2 | `v3_exq_906c_full_stack_observational_fishtank_20260810T014711Z_v3` | V3-EXQ-906c | PASS | `non_contributory` |
| 3 | `v3_exq_911_ecology_enrichment_fishtank_20260809T201208Z_v3` | V3-EXQ-911 | PASS | `non_contributory` |

All three adjudicated in confirmed `failure_autopsy_906b-906c-911-cluster_2026-08-10`.

---

## Verdict

**(iii) genuine framing problem — dominant, and it is the only one of the three candidates that
can account for the outcome at all.**

Neither (i) the lineage-wide recording gap nor (ii) a seed shortfall could have produced these
no-verdicts, because **the no-verdict outcome in all three runs is definitional, not empirical**:
each driver declares `CLAIM_IDS = []` and `EXPERIMENT_PURPOSE = "diagnostic"` at authoring time,
which makes `evidence_direction: non_contributory` a property of the *declaration*, fixed before
a single step ran. No measurement, on any instrumentation, at any seed count, could have moved it.

This is confirmed by each driver's own module docstring, which states the point plainly:

> WHAT THIS RUN IS NOT: a claim test, a statistically powered multi-seed study, or a
> substrate-readiness diagnostic for any single mechanism.

The runs are not defective. Each did the job it was authored to do (906b fixed a real
grid-wide proximity-harm early-death defect; 911 fixed a real grid-wide benefit-field confound,
moving mean distance-to-resource on benefit steps from 6.02 to 1.29 and consummatory events from
11 to 20; 906c added coupling instrumentation that found two genuine plumbing defects). **What is
mis-posed is the `bears_on` TOKEN, not the runs** — `fishtank_906_lineage_ecology_showcase` names a
work-stream to which no verdict-bearing question was ever attached, so runs accumulate against it
indefinitely without any of them being able to resolve it.

The chip's own framing anticipated this exactly: *"a driver built to DEMONSTRATE rather than to
DISCRIMINATE will reliably return non_contributory, because nothing was set up to be able to come
out either way."* That is what the code shows.

---

## Per-run attribution

All three share one step loop: 906c and 911 both `from experiments.v3_exq_906b_... import
_observational_run, CORE_CHANNELS, STD_FLOOR`. There is one criteria set across the cluster, not
three — consistent with the autopsy's own "one structural property, not three independent
showcases".

| run | (i) recording gap | (ii) seed shortfall | (iii) framing | attribution |
|---|---|---|---|---|
| 906b | present, non-causal | **absent** | **decisive** | (iii) |
| 906c | present, non-causal | **absent** | **decisive** | (iii) |
| 911 | present, non-causal | **absent** | **decisive** | (iii) |

### (ii) Seed shortfall — REFUTED cleanly, for all three

Declared seed count equals actual seed count in every case. The queue entries carry `"seeds": 1`
(first snapshots containing them: `ree-v3` `994e445c` / `b09d1e22` / `929c59d0`), the manifests
report `n_seeds = 1.0` and `seeds: [0]`, and each driver's `run(seeds=None)` defaults to `[0]`
*by design*, stated in its docstring. There is no declared-vs-actual divergence.

This is a **different** situation from V3-EXQ-912 and V3-EXQ-920, which the seed-enforcement
defect did hit (declared 2 and 8, one seed ran; `chip-20260812-queue-seed-enforcement`, now
`done`). Those had a gap between intent and execution. These three had no such gap: single-seed
was the intent, correctly executed, and correct *for a showcase*. It is only wrong for the
successor design proposed below, which is why that design declares its seed count explicitly.

### (i) Recording gap — PRESENT and REAL, but demonstrably not the cause

The lineage-wide gap confirmed by `failure_autopsy_V3-EXQ-916-916a-917-920-fishtank-cluster_2026-08-12`
does apply here, and the wrong-dict read is verified live in this cluster's shared step loop:

```
v3_exq_906b_full_stack_observational_fishtank.py:572
    benefit_exposure = max(0.0, float(obs_dict.get("benefit_exposure", 0.0)))
    agent.update_z_goal(benefit_exposure=benefit_exposure, drive_level=drive_level)
```

`benefit_exposure` is emitted into **`info`** (`causal_grid_world.py:3411`), never into the
observation dict, so `obs_dict.get(...)` returned the `0.0` default on every one of ~3,800 steps
per run. `update_z_goal` was therefore driven by `drive_level` alone.

Three reasons this did not cause the no-verdicts:

1. **The one gap-affected channel that is load-bearing did not fail.** `CORE_CHANNELS = ["z_harm_a",
   "z_harm_un", "drive", "z_goal"]`, and `z_goal` was non-degenerate in all three runs
   (`chan_max_std_z_goal` = 0.0722 / 0.0750 / 0.0737; `z_goal_stream.writer_defect: false`,
   ~4,800 writer calls each). It varied through the `drive_level` input path. For scale, the
   sibling driver 916 read `chan_max_std_z_goal = 0.0` (genuinely FLAT) and its 916a fix moved it
   to 0.078 — the same order as what these three already had *un*fixed.
2. **The channels the gap did zero are not load-bearing.** 906c's `residue_wanting_mean = 0.0`,
   `residue_wanting_std = 0.0` over `n = 3793` is the orphaned-writer signature exactly, but
   `residue_wanting` sits in `EXTRA_CHANNELS`, reported for description only.
3. **Fixing it changes nothing about the outcome.** V3-EXQ-916a's fix was verified to be *purely
   instrumentation* — seed-level simulation outputs bit-identical to 916. Applying the same fix
   here would move a descriptive readout and leave `claim_ids: []` untouched, so the run would
   still be `non_contributory` by declaration.

**Interpretive caveat this does create (worth carrying forward):** 906c's
`coupling_zgoal_t_to_benefit_t1t3_r = -0.048` (n=3785) is not evidence that goal state fails to
anticipate benefit. `z_goal` structurally *could not* encode benefit exposure in this run, so the
near-zero correlation is uninformative rather than negative. It should not be cited as part of the
affect-behaviour decoupling reading. (The `benefit` series in those coupling metrics is raw
`harm_signal`, not `benefit_exposure`, so the benefit side of the correlation is sound — the
contamination is entirely on the `z_goal` side.)

**Correction to the 916 autopsy, recorded so nobody reasons from the error.** That artifact states
`benefit_exposure` "is additionally gated on `use_proxy_fields=True`, which every 664-derived
driver (664, 906, 909, 911, 912, 913, and this run, 916) leaves at its default `False`." For at
least 906b/906c/911 the second half is wrong: the scaffold builds `CausalGridWorldV2`, whose
factory does `kwargs.setdefault("use_proxy_fields", True)`
(`causal_grid_world.py:5187+`), so proxy fields were **ON** and the env was computing a live,
non-zero `benefit_exposure` throughout. Corroborated by the `benefit_approach` transition type,
which only exists under `use_proxy_fields=True` and fired 1,384 times in 906b and 68 in 911; and
by the proximity-approach damage path 906b root-caused, which is itself `use_proxy_fields`-gated.
The operative defect in this sub-lineage is therefore the **wrong-dict read alone**. The net
effect on the reading is unchanged (`benefit_exposure` never reached `update_z_goal` either way),
so no conclusion in that autopsy moves — but the mechanism as written would send a future reader
looking for a config flag that was never the problem here.

### (iii) Framing — the decisive factor

Every load-bearing criterion in this cluster is a **precondition for measurement, not a test**:

| criterion | load-bearing | what it asserts |
|---|---|---|
| `core_channels_non_degenerate` | yes | the affect channels produce varying numbers |
| `harm_pathway_trained` | yes | co-training ran ≥1 optimizer step (measured 3751 / 3898 / 3735 vs threshold 1) |
| `ecology_survivable` | yes | segments outlast 906's early-death signature (488 / 474 / 500 vs threshold 59.6) |
| `benefit_approach_confound_reduced` (911 only) | yes | the narrowed benefit field fires nearer resources, with a sample floor |
| `freeze_not_locked`, `channel_*` | no | descriptive |

The diagnostic test: **what would the FAIL branch have meant?** For every one of these, it means
"the instrument is broken, re-run it" — never "hypothesis H is false". A criterion whose negation
routes to a bug fix rather than to a scientific update cannot produce a verdict in either
direction. Three of these criteria clear their thresholds by factors of 8x, 3,700x and 8x
respectively, which is what a liveness gate is supposed to look like and is also why none of them
was ever at risk.

So the lineage has, entirely correctly, been doing **instrument-and-ecology readiness work**, while
its `bears_on` token names a **scientific work-stream**. GOV-DIAG-1 fired on the mismatch. That is
the counter firing correctly and usefully: the fix is not to exempt showcases from it.

---

## The re-operationalization

### What this lineage is actually trying to establish

Stripped of the showcase framing, the recurring question underneath 906b/906c/911 is:

> **Does the agent's shelter/forage behaviour show *contingent* control — switching driven by
> sensed opportunity and sensed threat — or is it a fixed monomodal policy that merely happens to
> land on the protective pole?**

This is squarely MECH-309 territory, on the SD-054 reef/shelter substrate, and the
906b/906c/911 autopsy already reached it as Finding 1: shelter use is real and protective
(2.4x / 1.6x lower harm-rate while sheltering, replicated) and excursion frequency comfortably
clears V3-EXQ-522's pre-registered C1/C2/C3 bars — **but no contingent control was demonstrated**,
because opportunity-triggered exit is structurally untestable under the current geometry (reef-to-
nearest-resource gap 4–5 cells vs sensory radius 2) and threat-triggered return is distance-
confounded.

That is a discrimination between two live hypotheses, and it is the thing the showcases kept
circling without ever being able to touch.

### Why it never reaches a verdict as currently posed

Three compounding reasons, in order of severity:

1. **`claim_ids: []`.** A run that tags no claim weights nothing, by construction. This is the
   single change that matters most.
2. **The load-bearing criteria are all liveness gates** (above). Nothing was set up to be able to
   come out either way.
3. **The conditioning event never occurs.** Even with the right DV, `P(exit | opportunity sensed)`
   is undefined when opportunity is never sensed — the geometry forecloses it.

### The DV that would let a run reach a verdict

Successor spec, to be authored via `/queue-experiment` (**not queued here**; the EXQ id is assigned
at authoring time to avoid a collision). Working name: **`reef_contingency_discrimination`**.

**Claim tagging.** `claim_ids: [MECH-309]` — non-negotiable, and the point of the whole re-pose.
Consider ARC-062 as a second tag only if the driver actually instruments the rule-apprehension
layer; do not tag it for a purely behavioural contrast.

**C1 — opportunity-triggered exit (primary, load-bearing).**

    Δ_exit = P(exit reef within k steps | ≥1 resource within sensory radius r at t)
           − P(exit reef within k steps | no resource within r at t)

pooled over in-reef steps, k ≈ 5, r = the agent's actual sensory radius (2 under the current
config — read it from the env, do not hardcode). **Pre-register both branches:**

- `Δ_exit > δ` with consistency across seeds → **contingent control**; MECH-309's
  monomodal-collapse reading is contradicted for this contrast (`refutes` / `weakens`).
- `Δ_exit ≈ 0` within CI → exit hazard is state-independent; this is a **positive measurement
  supporting** MECH-309's collapse reading, not another non-verdict.

Both branches update a claim. That is the whole difference from the current design.

**C2 — threat-triggered return (secondary, load-bearing), distance-stratified.**

    Δ_return | d = P(move toward reef within k | hazard within r) − P(move toward reef | no hazard)

computed **within strata** of Manhattan distance-to-nearest-reef-cell (e.g. 1–2, 3–4, ≥5), and
reported per stratum plus a stratum-weighted pooled estimate. The stratification is the direct fix
to the autopsy's "threat-triggered-return test is weak, distance-dependent, inconsistent across
seeds" — under the current pooled design, absolute distance and threat state are confounded.

**Preconditions (must be met, else the run is VOID — not PASS).** This is where the current
liveness gates belong: as preconditions, never as the load-bearing set.

- `n_opportunity_conditioning_events ≥ 100` pooled — i.e. the "resource sensible while in reef"
  state actually occurred often enough for C1 to be estimable. **This is the gate that the
  geometry currently fails.**
- `n_threat_conditioning_events ≥ 100` pooled, and ≥ 20 in each distance stratum used.
- The existing `harm_pathway_trained` / `ecology_survivable` gates, unchanged.

**Environment change required to make the C1 precondition satisfiable.** Follow
`developmental_ecology_curiosity_foraging_correction_2026-08-10.md`, not the reef review's
Section 8 item 1 that it corrects: the right lever is a **probabilistic habitat cue** that shifts
the resource-spawn prior toward reef-adjacent cells *without* guaranteeing sensory reachability —
not "resources must be reef-perceptible". REE's SD-025 curiosity/exploration machinery is active
in this ecology, so discovery-through-exploration is a valid and more developmentally interesting
pipeline than direct sensing. Conditioning C1 on *sensed* opportunity keeps the DV well-defined
while the cue makes the sensed state occur at a non-trivial rate. This work is already covered by
`chip-20260810-fishtank-developmental-ecology` (amended twice) — **do not spawn a second chip for
it**; the successor consumes it.

**Power.** `seeds: 8` minimum, declared in the queue entry. C1/C2 are *rate contrasts*; a single
continuous trajectory cannot separate a rate difference from within-trajectory autocorrelation, so
the single-seed convention that is correct for a showcase is wrong here. The seed-enforcement fix
(`chip-20260812-queue-seed-enforcement`, `done`) is what now makes that declaration binding rather
than decorative.

**Instrumentation.** Port V3-EXQ-916a's fix into the shared `_observational_run`: read
`info.get("benefit_exposure")` rather than `obs_dict.get(...)`, and wire
`agent.update_benefit_salience()` / `update_schema_wanting()` into the step loop. Not load-bearing
for C1/C2 (which are behavioural), but required before any affect-coupling secondary readout —
and it retires the interpretive caveat above.

### What is REFUSED

**A same-question letter re-queue — 906d, 911a, or any further showcase iteration on this criteria
set — is refused**, in the re-derive brake's spirit and per GOV-DIAG-1's own prescription. Adding
a fourth run whose load-bearing criteria are liveness gates would add a fourth hit to the same
token and resolve nothing. This refusal does **not** extend to the successor above, which asks a
different question with a different DV and a claim tag.

---

## Observations for `/governance` (not acted on here)

1. **GOV-FANOUT-1 candidacy.** The re-posed question is a *discrimination* (contingent control vs
   monomodal collapse) on a lineage surfaced by 6a-v-ter, and no diverse portfolio has been run for
   it — the MECH-309 line's history is a long sequential chain. Per 6a-v-quater that makes it a
   fanout candidate, and the diverse-axis split is fairly natural: **measurement** (the C1/C2
   contingency DVs above), **environment** (the habitat-cue geometry), **mechanism** (whether a
   rule-apprehension layer changes the contrast at all — `arc_062_rule_apprehension:GAP-B`'s own
   ARM_0/ARM_1 shape). This is surfaced for the user to route via AskUserQuestion, not decided
   here.
2. **Token hygiene, and a caution against the wrong fix.** The general lesson is *not* "exempt
   showcases from GOV-DIAG-1" — the counter did its job. It is that an instrument-readiness run
   should not carry a scientific work-stream `bears_on` token. `/failure-autopsy` tagging a
   showcase with the work-stream it *supports* rather than the one it *tests* is what let three
   liveness runs accumulate on a question none of them could reach. Worth a narrow tagging
   convention; deliberately not written as a rule here, since one incident is not three
   (CLAUDE.md's held-out check).

---

## Metabolization

The chip's bar: *"An attribution to instrumentation counts as metabolizing IF you name and route
the successor; a bare 'it was the recording gap' with no routing does not."* This is an attribution
to **framing**, and GOV-DIAG-1's prescribed response for that — re-pose the operationalization, fix
the measurement/reference frame, refuse the same-question re-queue — is carried out in full above:
the DV is re-posed with both branches pre-registered onto MECH-309, the distance confound and the
geometry foreclosure are given concrete fixes, and the letter re-queue is refused.

Marker written to `arc_062_rule_apprehension:GAP-B` with
`covers_tokens: [fishtank_906_lineage_ecology_showcase]`. That node is the correct home: same claim
(MECH-309), same substrate (SD-054 reef/shelter), same phenomenon (monomodal collapse vs
discriminative regime switching). No plan node owned the showcase token itself, and per
GOV-DIAG-1's design `covers_tokens` exists precisely to home a free-form token on the node that
metabolized it rather than manufacturing a node for it.

The exclusion is **hit-scoped**: only these three run_ids are subtracted. A new chain later
circling the same work-stream re-accumulates to N and re-fires, as designed.
