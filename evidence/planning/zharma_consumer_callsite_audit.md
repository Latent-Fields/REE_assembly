# `z_harm_a.norm()` consumer audit -- which call sites are place-safety consumers

**Slug for STOP-CHECK greps:** `zharma_consumer_callsite`

**Status:** audit complete, AUDIT-ONLY. No substrate code, no threshold, no flag default, no
`claims.yaml` status was changed by this work. This document is an INPUT to the MECH-303
dedicated-proximity-signal build (`chip-20260814-mech303-proximity-signal-focused`), which
owns every re-pointing decision it recommends.
**Date:** 2026-08-14
**Chip:** `chip-20260814-zharma-consumer-callsite-audit`
**Claims:** MECH-492 (the owed audit), MECH-303 (the routing decision that owed it),
MECH-286 (the second consumer MECH-492 identified), SD-011 / SD-022 (the sourcing).
**Substrate audited:** `ree-v3` `ree_core/`, working tree at 2026-08-14.

---

## Why this audit exists

MECH-303's 2026-08-12 user-adjudicated routing decision took option (a) -- build a DEDICATED
proximity-anticipatory safety signal, decoupled from SD-022's damage-sourcing -- rather than
re-source the shared `z_harm_a`, on the reasoning that re-sourcing one gate would break other
consumers. That decision explicitly owed "auditing which other production drivers should
consume which signal", but scoped the audit to drivers enabling
`use_contextual_safety_terrain` (764 / 520 / 916 / 916a). MECH-286's sleep-permission gate is
not one of those drivers, which is exactly how a second consumer of the identical expression
went unnoticed. MECH-492 (registered 2026-08-14, `REE_assembly` `484da1d6a3` / `9824927cb7`)
records that consumer and states the per-call-site adjudication as an OWED AUDIT it
deliberately does not assert. This document is that audit.

---

## 0. Two corrections to MECH-492's own premises

Both were found by re-running the enumeration rather than trusting the cited figure, and
neither changes MECH-492's argument -- each strengthens it.

**(a) There are 16 executable call sites, not 10.** MECH-492 says "There are 10
`z_harm_a.norm()` call sites in `ree_core`". A literal `z_harm_a.norm()` grep does return
about that many, but it misses two shapes that are real reads of the same quantity:

* the `**.norm(dim=-1).mean()`** form -- `agent.py:3866`, `hippocampal/module.py:1033`,
  `e3_selector.py:1213`, `e3_selector.py:3159` (4 sites). Mathematically this is a
  batch-mean of per-row norms rather than a whole-tensor norm; for the batch=1 agent path it
  is the same scalar.
* **the site where the tensor is bound to a local named something else** --
  `sleep/sleep_onset_gate.py:69` reads `z.norm().item()` inside `_z_harm_a_tonic_norm()`.
  This is MECH-492's OWN subject, and a `z_harm_a.norm()` grep does not find it.

The corrected sweep is `grep -rnE 'z_harm_a[a-z_]*\)?\.(detach\(\)\.)?norm\('` plus a manual
read of `sleep_onset_gate.py`. Full enumeration in §2.

**(b) Four of the "call sites" are documentation, not reads.** `residue/field.py:792`,
`comparator/suffering_derivative_comparator.py:16`, `utils/config.py:807` and
`utils/config.py:819` mention `z_harm_a.norm()` in a docstring or comment and execute
nothing. They still matter -- `field.py:792` is MECH-303's own docstring and will be stale
the moment the gate is re-pointed -- so they are listed in §3 rather than dropped.

---

## 1. The discriminator used, and the sourcing fact that governs everything below

**The question asked of each site:** does this consumer need to know *how hazardous the place
the organism currently occupies is* (place-safety proxy -> should be re-pointed at the
dedicated signal), or *how much damage / unpleasantness / arousal the organism itself is
carrying* (body-state -> correctly damage-sourced, leave alone)?

The sharpest single test is **whether the consumer keys its output on a location.** MECH-303
writes its increment into a terrain indexed by `z_world`; that makes its need for place
information structural rather than interpretive. Sites that write into whole-organism state
(drive level, tonic 5-HT, a suffering accumulator, a commit threshold) have no location in
their output and therefore no structural claim on place information.

**The sourcing fact, verified in `causal_grid_world.py` and not inferred:** `z_harm_a` is
`AffectiveHarmEncoder(harm_obs_a)`, and `harm_obs_a` has two mutually exclusive forms
selected by one boolean:

| `limb_damage_enabled` | `harm_obs_a` | proximity content |
|---|---|---|
| `False` (**default**) | 50-dim: EMA (`alpha=0.05`) of the hazard / resource scalar **at the agent's current cell**, replicated across dims (`causal_grid_world.py:2785-2790`) | YES -- it *is* a lagged place-hazard signal |
| `True` (SD-022) | 7-dim: the four directional limb-damage accumulators + max / mean / residual pain (`causal_grid_world.py:3825-3838`) | NONE -- pure body state |

Two consequences that shape how the table below should be read:

1. **"Is this a place-safety consumer?" and "is the current sourcing adequate for it?" are
   different questions,** and the second is sourcing-mode-dependent for *every* row. Under
   the default proximity-EMA mode a place-safety consumer is reading something roughly
   right-shaped (lagged, unnormalised, and per V3-EXQ-764 barely discriminating -- but not
   categorically wrong). Under SD-022 damage-sourcing it is reading a signal with *zero*
   proximity content. The adjudications below are about which signal each site SHOULD read;
   the severity of reading the wrong one is set by the driver's `limb_damage_enabled`.
2. **The mirror-image hazard is real and is why "just re-source `z_harm_a`" was correctly
   rejected.** Under the default proximity-EMA mode, the body-state consumers in §2 are the
   ones reading something wrong-shaped -- a hazard-proximity EMA standing in for body damage.
   Nothing in this audit proposes fixing that; it is noted so the dedicated-signal build does
   not mistake "leave alone" for "this site is well-sourced today".

---

## 2. The enumeration -- 16 executable call sites

`P` = place-safety proxy (re-point at the dedicated signal). `B` = body-damage / arousal / PE
(correctly damage-sourced, leave alone). `?` = cannot adjudicate from the code alone.
`F` = learned feature, not a gate (see the row).

| # | file:line | consumer | claim | gate on the flag | verdict |
|---|---|---|---|---|---|
| 1 | `agent.py:5145` | contextual safety terrain accumulation | MECH-303 | `use_contextual_safety_terrain` (default `False`) | **P** |
| 2 | `sleep/sleep_onset_gate.py:69` | sleep-onset permission, `threat_ok` conjunct | MECH-286 / MECH-492 | none -- runs whenever the gate is evaluated | **P** |
| 3 | `agent.py:8974` | PAG freeze-gate drive | MECH-279 | `pag_freeze_gate is not None`; **preempted** by `use_lpb_interoceptive_routing` | **?** |
| 4 | `agent.py:4547` | suffering accumulator, `body_damage_norm=` arg | MECH-219 / SD-019b | `harm_suffering_accumulator is not None` | **B** |
| 5 | `agent.py:4619` | AIC interoceptive salience urgency | SD-032c | `aic is not None`; superseded by `z_harm_un` when `latent.use_harm_un` | **B** |
| 6 | `agent.py:5117` | suffering-derivative comparator input | MECH-302 | `suffering_comparator is not None` | **B** |
| 7 | `agent.py:6570` | pACC drive sensitisation | SD-032e | `pacc is not None` | **B** |
| 8 | `agent.py:10728` | tonic 5-HT step | MECH-203 | `serotonin.enabled` (default `False`) | **B** |
| 9 | `agent.py:3866` | blocked-agency `capacity_belief` | MECH-353 | `blocked_agency is not None` | **B** |
| 10 | `agent.py:5875` | MECH-091 urgency interrupt | MECH-091 / SD-011 | `beta_gate.is_elevated`; `e3.urgency_interrupt_threshold` (0.8) | **B** |
| 11 | `cingulate/dacc.py:214` | dACC control PE, `\|\|z_harm_a - z_harm_a_pred\|\|` | MECH-258 / SD-032b | dACC bundle active | **B** |
| 12 | `cingulate/dacc.py:212` | same, no-prediction fallback (raw norm as PE) | MECH-258 / SD-032b | as above, `z_harm_a_pred is None` | **B** |
| 13 | `e3_selector.py:1213` | ethical-cost amplification `lambda_eff` | SD-011 | `e3.affective_harm_scale > 0` (default `0.0`) | **B** |
| 14 | `e3_selector.py:3159` | commit-threshold urgency lowering | SD-011 | `e3.urgency_weight > 0` (default `0.0`) | **B** |
| 15 | `hippocampal/module.py:1033` | harm-aware chunk-decomposition selection | (chunk decomposition) | `decomposition_use_harm_aware_selection` (default `False`) | **B** |
| 16 | `pfc/e2_escape_affordance_linker.py:323` **and** `pfc/trainable_escape_affordance_learner.py:215` | one scalar in a learned state-feature vector | SD-059 / MECH-358 successor substrate | OFF by default; **fallback only** -- used when the caller passes `z_harm_a_norm=None` | **F** |

### Evidence, per verdict

**#1 `agent.py:5145` -- MECH-303 contextual safety terrain. P, definitive.**
The block gates `residue_field.accumulate_safety(new_latent.z_world, ...)` on
`harm_norm < contextual_safety_harm_threshold`. It writes a safety increment **into a terrain
indexed by `z_world`** -- the output is location-keyed, so the gating quantity must be a
property of the location. This is the structural test in §1 passing at its strongest. The
claim text is explicit that the mechanism is passive contextual association of a *place* with
the absence of harm. Already the acknowledged re-point target of the 2026-08-12 routing
decision; listed here for completeness, not as a new finding.

**#2 `sleep_onset_gate.py:69` -- MECH-286 sleep-onset permission. P, recommended, with a
second defect underneath it.**
`evaluate_sleep_onset_permit` computes `threat_ok = harm_a_norm < threat_tonic_threshold`
(default `0.4`) and ANDs it with `override_ok` and `staleness_ok`. The question the term is
asking is *is it safe to become behaviourally unresponsive here and now* -- an anticipatory
property of the current context, and the same question MECH-303 asks. Body damage is not just
uninformative for it but arguably **anti**-informative: a damaged organism in a safe refuge is
a strong sleep candidate, and under SD-022 sourcing this gate would suppress sleep exactly
then. Under the default proximity-EMA sourcing it reads a lagged place-hazard signal, which is
the right shape.

Two things the re-point does NOT fix, which the build should know:

* **There is no tonic/phasic decomposition anywhere in this path.** The function is named
  `_z_harm_a_tonic_norm` and MECH-286's text says "tonic component low", but it returns the
  full instantaneous norm -- verified by reading the function body. Re-pointing it at a
  dedicated proximity signal yields an *instantaneous proximity* norm, not a tonic one. If
  MECH-286 means tonic, that is a separate build.
* **The `0.4` default is uncalibrated.** V3-EXQ-917 located the reachable-and-discriminating
  band for this signal at ~0.55-0.6; `0.4` sits below it and predates any measurement. The
  two gates use the comparison in opposite directions for different purposes so the band does
  not transfer, but a re-point changes what the number is measuring and therefore obliges a
  fresh calibration rather than carrying `0.4` across. Do not port the constant.

**#3 `agent.py:8974` -- MECH-279 PAG freeze gate. `?` -- FLAGGED, cannot adjudicate from the
code.**
This is the one row that resists the discriminator, and it is flagged rather than guessed.
Arguments both ways:

* Toward **P**: freeze is a defensive response to *threat imminence*, classically a
  predator-proximity phenomenon. The entry condition is
  `z_harm_a_norm * duration_above_threshold > theta_freeze`, i.e. a sustained-external-threat
  reading. Body damage is a poor freeze trigger.
* Toward **B/no action**: the site **already has a preferred non-`z_harm_a` source**. When
  `use_lpb_interoceptive_routing` is on, `pag_z_norm` comes from
  `self._lpb_last_output.external_magnitude` and `z_harm_a` is never read; and MECH-219 can
  redirect it again to `z_harm_suffering`. So `z_harm_a` here is the *legacy fallback of a
  path that has already been given a better source twice*, and the principled fix may be to
  make the LPB external-magnitude channel non-optional rather than to add a third redirect.

**Recommendation: do not re-point #3 as part of the MECH-303 build.** Decide it as its own
question against MECH-279 and the LPB routing claim, with someone who owns the
external-magnitude channel. Re-pointing a fallback that a live config already bypasses adds a
fourth source to a three-source site for no measured gain.

**#4 `agent.py:4547` -- MECH-219 suffering accumulator. B, definitive.**
The strongest B in the table: the value is passed as the keyword argument
`body_damage_norm=body_norm`. The API *names* the semantics, and they are body damage. The
drive term of the same call is `unpleasantness_norm=||z_harm_un||`, taken separately. No
ambiguity.

**#5 `agent.py:4619` -- SD-032c AIC. B.**
The insula analog; the module's whole purpose is interoceptive salience. The code comment
states that when `use_harm_un` is active the correct AIC input is `z_harm_un` (the
unpleasantness dimension per Loffler 2018) and `z_harm_a` is the fallback. A consumer that has
already been argued into a *more* interoceptive source is not a place-safety consumer.

**#6 `agent.py:5117` -- MECH-302 suffering-derivative comparator. B, with the interesting
nuance.**
The comparator detects a sustained *descent* of the norm over a rolling window and fires
`relief_completion_event`. Relief is a property of the organism's own unpleasantness falling,
so the damage-sourced reading is correct. Worth stating explicitly because the naive reading
goes the other way: the downstream consumer (SD-051 / MECH-304 conditioned safety store,
`agent.py:5128`) *is* place-coupled -- it updates an EMA prototype **of `z_world`** when this
event fires. But the location coupling is done by the store reading `z_world` at fire time;
the detector supplies only the *when*. Splitting it that way is correct and should not be
disturbed: re-pointing #6 at a proximity signal would turn "the organism's suffering fell"
into "the agent moved somewhere less hazardous", which is a different (and much weaker)
teaching event.

**#7 `agent.py:6570` / #8 `agent.py:10728` / #9 `agent.py:3866` -- B.**
All three write into whole-organism state with no location in the output: pACC drive-bias EMA
(sensitisation of drive level by accumulated harm load); tonic 5-HT -> `z_goal_seeding_gain`
and `valence_wanting_floor`; and blocked-agency `capacity_belief`, whose own comment reads
"capacity-belief proxy: collapses with affective suffering load". Accumulated organismic load
is what each of them means.

**#10 `agent.py:5875` -- MECH-091 urgency interrupt. B.**
Aborts a committed motor program when the harm signal is extreme. Like #5, it has already been
argued toward a *more* interoceptive source: SD-019a redirects it to `z_harm_un` because that
gives "faster-rising urgency proportional to current unpleasantness", and MECH-219 can redirect
it again to `z_harm_suffering`. `z_harm_a` is the legacy default. Not place-safety.

**#11 / #12 `dacc.py:214` / `dacc.py:212` -- B, and source-agnostic.**
`pe = ||z_harm_a - z_harm_a_pred||`. This is a prediction error against `E2_harm_a`'s own
prediction of the same quantity, so it is well-defined whatever `z_harm_a` denotes: re-sourcing
the signal re-sources both sides of the subtraction. Nothing to do here under any option.
`dacc.py:212` is the degenerate branch taken when no prediction exists (`pe = ||z_harm_a||`),
same conclusion.

**#13 / #14 `e3_selector.py:1213` / `:3159` -- B, `:3159` with a caveat.**
`:1213` amplifies `lambda_ethical` by accumulated threat -- organismic load weighting a cost
term, clearly B. `:3159` lowers the E3 commit threshold ("commit faster under threat", D2
avoidance escape). That one is arguably arousal-from-external-threat rather than body damage,
so it leans the same way as #3 -- but unlike #3 the config comment frames it as accumulated
affective load, both readings support "commit faster", and it is inert at its `0.0` default.
Left as B; noted so a later reader does not mistake the omission for an oversight.

**#15 `hippocampal/module.py:1033` -- B.**
Harm-aware chunk-decomposition selection: a whole-organism arousal gate narrowing which chunk
candidates survive. No location in the output. Off by default.

**#16 the two escape-affordance modules -- F, no re-point needed, and structurally immune.**
Both append the scalar as one element of a learned, detached state-feature vector consumed by
trained heads; there is no threshold and no gate. Two reasons this needs no action: a learned
head can adapt to whatever the feature denotes, and -- decisively -- **both take
`z_harm_a_norm` as an injectable parameter and compute the norm themselves only when the
caller passes `None`**. If the dedicated signal exists, the caller passes it and neither
module changes. Noting this because "escape affordance" reads as proximity-flavoured
("where out is") and could otherwise look like a missed **P**: the proximity content these
modules need already arrives separately as `refuge_features`.

---

## 3. Documentation-only references (no executable read)

| file:line | what it says | action |
|---|---|---|
| `residue/field.py:792` | `accumulate_safety` docstring: "Called per step when `z_harm_a.norm()` is below the quiescent threshold" | **Update with the re-point of #1** -- this is MECH-303's own docstring and goes stale the moment the gate changes source |
| `comparator/suffering_derivative_comparator.py:16` | class docstring: "Reads `z_harm_a.norm()` scalar each tick" | Accurate, leave (#6 is B) |
| `utils/config.py:807` | `urgency_weight` comment (#14) | Accurate, leave |
| `utils/config.py:819` | `urgency_interrupt_threshold` comment (#10) | Accurate, leave |

---

## 4. What this means for the dedicated-signal build

Scoped to what the audit establishes; the build owns the decisions.

1. **Two consumers to re-point, not one:** #1 (MECH-303, already known) and #2 (MECH-286,
   the MECH-492 finding). Everything else in §2 is either correctly damage-sourced, a
   learned feature that needs no change, or the flagged #3.
2. **#2 is the higher-severity one** and MECH-492's reasoning holds up against the code:
   MECH-303's gate failing means safety terrain silently does not accumulate, while
   MECH-286's is one conjunct of an AND that decides whether the agent sleeps at all --
   a false `threat_ok` blocks sleep entirely, and the diagnostics
   (`mech286_threat_ok`, `mech286_sleep_permitted`) report the gate's *decision*, not that
   its input was the wrong quantity.
3. **Do not carry `0.4` across to the re-pointed MECH-286 gate**, and do not carry `0.05`
   across to the re-pointed MECH-303 gate. Both were set against a signal the new one
   replaces; V3-EXQ-917's ~0.55-0.6 band is a property of the *old* signal's scale.
4. **#3 (PAG) is deferred, deliberately.** Flagged as `?`, with the argument on both sides in
   §2 so a later session does not have to re-derive it.
5. **The `limb_damage_enabled` coupling documented in the MECH-303 planning doc's 2026-08-12
   addendum applies to #2 as well.** Any driver that enables SD-022 body-damage sourcing
   strips the proximity content out of the sleep gate's input at the same time, and nothing
   in the sleep-gate path signals that it happened.

---

## Cross-references

* `evidence/planning/mech303_contextual_safety_threshold_reachability.md` -- the reachability
  finding, the V3-EXQ-917 probe, and the 2026-08-12 sourcing-mode addendum this audit builds on.
* `docs/claims/claims.yaml` -- MECH-492 (owes this audit), MECH-303, MECH-286, SD-011, SD-022.
* `chip-20260814-mech303-proximity-signal-focused` -- the build this feeds.

**Method note.** Every line reference and every flag default above was read from the `ree-v3`
working tree on 2026-08-14, not inferred from claim text. Where the code and a claim's prose
disagree (MECH-286's "tonic component", MECH-492's call-site count) this document follows the
code and says so.
