# Thought Intake — z_harm_a saturates high and decouples from current safety

**Date of thought:** 2026-06-10
**Intake written:** 2026-07-21
**Raw thought file:** `docs/thoughts/2026-06-10_z_harm_a_saturation_decoupling.md`
**Session:** `confident-pare-9273f1` (orphaned-thought intake pass, 2026-07-21)
**Source:** the V3-EXQ-664 affective fishtank showcase episode log — an **internal experimental observation**, not literature. The embodied visualisation surfaced it before the scalar metrics did (`feedback_whimsy_visualization`).
**Status:** structured intake written; candidate claims **NOT yet registered** — two concurrent sessions (`stoic-blackwell-756d3a`, `scientific-dashboard-status-7d2d08`, `malloc-stack-logging-explorer-a0e312`) held active TASK_CLAIMS on `docs/claims/claims.yaml` at intake time, so registration is deferred to a session that holds that claim.
**Promotes/demotes:** nothing.

## Authorship note

The observation, the quantification, and the two-stacked-effects reading (faithful chronic-stress component *plus* calibration pathology) are the user's, from watching the fishtank replay and then quantifying what the viz exposed. The scope caveat about the non-curriculum agent is also the user's and is load-bearing. This intake supplies the substrate verification (what the code actually does), the registry cross-reference, and the routing.

## Substrate verification performed for this intake

Two things were checked in `ree-v3` rather than assumed, because both change what is new here:

1. **`harm_surprise_pe_enabled: bool = False`** — `ree_core/utils/config.py:2306`. SD-020's prediction-error training target for `z_harm_a` is behind a **default-off flag**. With it off, `compute_harm_accum_loss` (`ree_core/agent.py:8598`, PE branch at `:8636-8642`) trains the `harm_accum_head` against the EMA **accumulated-harm** target — i.e. exactly the absolute-state integrator SD-020 says `z_harm_a` should *not* be.
2. **The latent norm is the live functional readout, not just the viz readout** — `z_harm_a.norm(dim=-1).mean()` appears at `ree_core/predictors/e3_selector.py:1038` (lambda_ethical amplification, SD-011) and `:2766` (urgency modulation of the commit threshold). SD-050's suffering-derivative comparator also reads `z_harm_a.norm()` per its own registered title.

Both facts are load-bearing below.

## Already owned — cross-reference, do NOT re-assert

The harm-stream area is densely claimed. Most of the raw thought's "candidate directions" already have owners:

| Element in the thought | Existing claim(s) |
|---|---|
| Two-stream separation, `z_harm_a` as the affective/accumulator stream | **SD-011** (stable), **SD-010**, **ARC-027** (active) |
| `z_harm_a` must not be a lagged/smoothed copy of `z_harm_s` | **SD-019** (provisional; PASS on V3-EXQ-323a) |
| Middle tier `z_harm_un` (unpleasantness) | **SD-019a** |
| `z_harm_a` as a controllability-gated hysteretic integrator, load state | **SD-019b** (candidate, v3_pending), **MECH-219** |
| Decay / recovery asymmetry (onset vs recovery parameters) | **MECH-219** (leaky integrator, asymmetric onset/recovery) |
| Cross-stream exponential decay, missing-decay as a regulatory failure | **SD-036** (GABAergic regulatory layer over `z_harm_s`, `z_harm_a`, `z_beta`) |
| "What beyond temporal integration makes affective harm a distinct load state?" | **Q-036** (open) — the raw thought's decay/uncontrollability/persistence list is this question verbatim |
| `z_harm_a` should encode affective **surprise** (precision-weighted PE), not raw accumulated state | **SD-020** (stable; PASS on V3-EXQ-324b) |
| `z_harm_a` as precision-weighted PE entering action selection | **MECH-258** |
| Relief on suffering descent; the comparator that should pull it down | **MECH-302**, **SD-050** |
| Safety prediction as the candidate coupling | **MECH-303**, **MECH-304**, **SD-051**, **SD-052** |
| Descending modulation gates `z_harm_s` only, `z_harm_a` persists | **SD-021** |
| `z_harm_a` as slow interoceptive accumulation sharing a motif with `drive_level` | **MECH-167** |
| Fast salience classification off `z_harm_a` into the mode prior | **MECH-046**, **MECH-074c** (CeA `fast_prime` on low-frequency `z_harm_a`) |
| `z_harm_a` -> autonomic/valence coupling | **SD-032e** (stable), **SD-032b** (dACC reads `z_harm_a` PE) |
| Harm evaluation bounded by / growing with `z_harm` differentiation | **INV-089** (provisional), **INV-090** (candidate, substrate_conditional) |
| Magnitude-without-dynamic-range affect pathology, cross-candidate form | V3-EXQ-643 / `project_candidate_differentiated_affective_gradients` |
| `z_harm_a` as motivational urgency into commit gating | **ARC-016**, **SD-011** |

So: **the accumulator, its decay, its PE target, its relief comparator, and its safety-coupling candidates are all already claimed.** Do not register any of them again. In particular, do **not** re-raise "should `z_harm_a` decay faster / relax during shelter" as a new claim — that is Q-036 plus MECH-219 plus SD-036.

## Genuinely new — three things

### N1. A `stable` claim whose mechanism is default-off, and the observed pathology is its predicted consequence

SD-020 reads `stable` on a `supports/PASS` verdict (V3-EXQ-324b, 2026-04-19). But `harm_surprise_pe_enabled` defaults to `False`, so **the default-trained substrate trains `z_harm_a` on the absolute accumulated-harm target that SD-020 argues against.** The V3-EXQ-664 agent is default-configured. Saturation near a ceiling, a large near-constant offset, and near-zero within-episode range are what an absolute-state integrator in a relentlessly punishing environment is *supposed* to produce.

This is not a new mechanism hypothesis. It is a **claim-status-vs-default drift** finding: SD-020's stable reading is scoped to the flag-on configuration and does not describe the agents actually being run. That distinction is not recorded anywhere on the claim. (Compare the general hazard in `reference_reeconfig_from_dims_silent_kwargs` — a knob that exists but is not reached.)

It also reframes the thought's own two-stacked-effects reading: effect (2), the "calibration / representation pathology", may be substantially **effect (1) measured through the pre-SD-020 training target**, not a separate encoder pathology.

### N2. The norm is the functional readout, so saturation degrades E3 behaviour, not only the display

The raw thought treats "readout != raw norm" as a candidate direction for a *faithful suffering scalar*. The substrate check makes it stronger than that: the norm is what **E3 actually consumes** at two live sites — `lambda_eff` ethical-cost amplification and commit-threshold urgency. A norm with a large constant component and near-zero cross-state range therefore enters both consumers as an approximately **constant gain**, not a signal. Whatever behavioural work `z_harm_a` is supposed to do through ARC-016 commit gating, it is currently doing as an offset.

The same fact resolves the thought's own puzzle — *"the relief comparator exists but `z_harm_a` clearly is not being pulled down by it here."* SD-050 detects a **sustained descent** in `z_harm_a.norm()`. Within a single 664 episode that quantity spans ~7.18-7.42. There is no descent to detect. SD-050 inherits the degenerate readout; it is not failing on its own terms.

No claim in the registry asserts a **readout form** for `z_harm_a`. SD-011/SD-019/SD-019b/MECH-219 all constrain what the latent must *encode*; none constrains how it is *read*. That is the gap.

### N3. Non-redundancy is satisfiable by a degenerate constant — the sign inversion shows it

SD-019 (PASS) requires `z_harm_a` not be a lagged/smoothed/monotone-transformed copy of `z_harm_s`. The 664 data satisfies that requirement **and is useless**: mode means run `shelter` 7.25 > `avoid` 6.26 > `freeze` 5.79, and harm-steps (5.97) sit *below* non-harm steps (6.76). Suffering is highest when safest.

A near-constant signal is maximally non-redundant with a tracking signal. So SD-019's criterion is **necessary but not sufficient**, and the registry has no companion criterion asserting that `z_harm_a` must retain *functional cross-state range* and a *non-inverted* relation to instantaneous safety. Note the required care here: the correct claim is **not** "`z_harm_a` should track current safety" — that would collapse it toward `z_harm_s` and violate SD-019/SD-011. The claim is about **range and sign**, not tracking.

### Also new, methodologically

The finding is an instance of the embodied-visualisation value-add: the fishtank made a representational pathology legible at a glance that pooled scalar metrics had not surfaced. Worth keeping as a note on the viz's justification rather than as a claim.

## Explicitly NOT proposed

- **Not** proposing `z_harm_a` should track instantaneous safety (collapses it into `z_harm_s`; violates SD-019, SD-011).
- **Not** proposing to remove or fast-decay the accumulator — the chronic-load reading is the *point* of SD-019b/MECH-219, and INV-053's depressive attractor depends on exactly this integration.
- **Not** re-registering decay/recovery/uncontrollability drivers (Q-036, MECH-219, SD-036 own them).
- **Not** treating the 664 numbers as a substrate property of the developmentally-trained agent. The raw thought's scope caveat stands: this agent had no `scaffolded_sd054_onboarding` and no `scaffold_train_harm_pathway`. That caveat is now *more* important, not less, because N1 shows the training target itself was the pre-SD-020 one.
- **Not** a claim about `z_goal` flatness in 664 — that is the known missing-curriculum consequence, already understood.

## Candidate claims (for registration at digestion)

1. **`z_harm_a`'s functional readout must be a calibrated scalar valuation, not the latent norm.** *Candidate, design_decision / architectural.* The latent norm conflates a large near-constant encoder offset with a small functional component; E3 consumes it as an approximately constant gain at `e3_selector.py:1038` and `:2766`. Replace with a trained scalar head off `z_harm_a` (parallel to how harm/benefit are read via trained eval heads, not latent norms). *Falsifier / PASS-FAIL shape:* a two-arm comparison, norm-readout vs trained-head-readout, on matched seeds. PASS requires **both** (a) cross-state dynamic range of the readout increases by a margin scaled on the SD of the delta plus an absolute floor, and (b) at least one downstream consumer changes measurably (commit-threshold distribution or `lambda_eff` distribution moves beyond the seed-noise band). FAIL if range rises but nothing downstream moves — that would show the readout is not load-bearing. *Non-degeneracy precondition:* the `z_harm_a` **latent** must itself carry decodable cross-state information — a linear decode of behavioural mode or harm-event status from `z_harm_a` must clear a floor, with non-zero cross-seed variance. If the latent is uninformative, the readout form is not the defect and the run self-routes `substrate_not_ready`. *Cross-ref:* SD-011, SD-019, SD-020, MECH-258, ARC-016, SD-050, INV-089/INV-090.

2. **SD-020's `stable` reading is scoped to the flag-on configuration and does not describe default-trained agents.** *Candidate, governance / evidence-scoping — or a `live_status` scope annotation on SD-020 rather than a new claim; adjudicate at digestion.* *Falsifier / PASS-FAIL shape:* re-run the 664 affective fingerprint as a two-arm experiment, `harm_surprise_pe_enabled` OFF vs ON, everything else matched. PASS (claim upheld) = the saturation-and-inversion signature is present in OFF and materially reduced in ON — specifically, OFF shows within-episode CoV below a pre-registered floor **and** inverted mode-ordering (`shelter` > `avoid` > `freeze`), while ON shows neither. FAIL = the signature survives the flag flip, which would relocate the defect to the encoder or the environment and hand the question to candidate 3. *Non-degeneracy precondition:* the OFF arm must **reproduce** the original 664 signature before the ON arm means anything, and the two arms must differ on the training loss they actually optimise (assert the PE branch is entered) — an ON arm that silently falls through to the EMA target tests nothing and self-routes `substrate_not_ready`. *Cross-ref:* SD-020, SD-019b, MECH-219, Q-036, and the V3-EXQ-324b evidence record.

3. **Environment-confound control: is the saturation ecological or representational?** *Candidate, diagnostic.* The raw thought's own control. Re-measure the affective fingerprint on a gentler environment (lower `num_hazards`, lower `hazard_food_attraction`). *Falsifier / PASS-FAIL shape:* PASS for "calibration, not ecology" = `z_harm_a` still pegs high with sub-floor CoV in the benign environment. PASS for "faithful chronic suffering" = the level and range track hazard density. *Non-degeneracy precondition:* the manipulation must demonstrably take — the **sensory** tier `z_harm_s` must differ across arms (its mean or CoV moving beyond the seed-noise band). If `z_harm_s` is unmoved, the environment was not actually made gentler and the arm self-routes `substrate_not_ready`. *Cross-ref:* SD-011, SD-019, INV-053, MECH-219.

4. **SD-050 cannot fire on a range-degenerate `z_harm_a` — a readout precondition on MECH-302, not a new mechanism.** *Candidate, precondition annotation.* A sustained peak-to-trough descent detector requires the signal to have a trough. Register as a **precondition on SD-050/MECH-302** (their falsifiers are uninterpretable while candidate 1's non-degeneracy guard fails) rather than as an independent claim. *Non-degeneracy precondition:* this claim *is* a non-degeneracy precondition; its own test is candidate 1's decode floor. *Cross-ref:* SD-050, MECH-302, MECH-057a, MECH-091, MECH-094.

5. **Curriculum-scope re-check.** *Not a claim — a required scope condition on all of the above.* Every number here is from a ~50-episode raw warmup with `scaffold_train_harm_pathway` off. Candidates 1-3 should be run on the curriculum-trained configuration, or their conclusions explicitly scoped to raw-warmup agents. Registering any of 1-3 without this scope tag would over-claim. *Cross-ref:* the 603i/603k harm-pathway co-training, `project_stageh_harm_pathway_training`.

## Routing

- **Cheapest first move is re-analysis, not an experiment** (GOV-REUSE-1 applies). Candidate 1's non-degeneracy guard — can behavioural mode / harm-event status be decoded from the stored `z_harm_a` latents in the existing 664 episode logs? — is answerable from data already on disk. If the decode is at floor, candidates 1 and 4 are answered negatively for free and the whole line collapses to candidates 2/3. `complicated (buildable)`.
- **Then candidate 2**, which is a **one-flag two-arm run** and is the single highest-information action here: it separates "SD-020 was right and simply isn't on" from "the pathology survives the fix". `complicated (buildable)`.
- **Candidate 3** is the confound control and should run alongside or after 2. `complicated (buildable)`.
- **Candidate 1's readout swap is a substrate change** and should not be built until 2 and 3 have reported — if the PE target alone restores range, no new head is needed. `complex (probe-gated)`, with candidate 2 as the probe.
- **Q-036 remains the standing home** for "what beyond temporal integration". This thought does not answer it and should not be allowed to look like it does; it contributes one datum (the default-off finding) to that question. Currently `mystery (known data)` — the driver list exists, what is missing is a frame for choosing among persistence / recovery-failure / uncontrollability / PE, not more data.
- **Do NOT queue any experiment through anything but `/queue-experiment`.** Candidates 2 and 3 are close relatives of V3-EXQ-664 and are exactly the copy-and-modify case the skill exists for.

## Next steps

1. Register candidates 1-4 (5 as a scope tag on each). **Deferred from this session** — `claims.yaml` was held by three concurrent sessions at intake time.
2. Mark the raw thought `Status: processed` only once (1) lands. It currently remains `unprocessed`, correctly.
3. Retrospective decode spike against the stored 664 episode logs (Routing, first bullet).
4. Consider whether SD-020 needs a standing `default_off` annotation in `claims.yaml` — and whether other claims carry the same drift. That generalises beyond this thought and is worth its own audit.
