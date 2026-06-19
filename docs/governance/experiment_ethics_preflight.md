# Experiment Ethics Preflight (DRAFT)

**Status:** DRAFT. Binds at **V4**. **NON-BLOCKING for the V3 green-board (2026-07-19).**
**Registered:** 2026-06-19
**Owns:** Phase 2 of [`evidence/planning/ethics_perimeter_plan.md`](../../evidence/planning/ethics_perimeter_plan.md)
**Source thoughts:** `docs/thoughts/2026-06-19_ethics_process_translation.md` (S3 preflight schema),
`docs/thoughts/2026-06-18_pre_meaning_suffering_valley.md` (SENT-10),
`docs/thoughts/2026-06-18_creation_ethics_necessary_suffering.md` (SENT-7/8/9).
**Implements / operationalises:** SENT-2 (welfare budget), SENT-4 (welfare-preserving design),
SENT-8 (minimal necessary suffering), SENT-10 (pre-meaning valley).

> This is the keystone Phase-2 item: SENT-2/4/8/10 + GOV-PROC-1 all pivot on undefined
> qualifiers -- "bounded", "minimal", "beyond trivial intensity", "escapable". Until those
> are operationalised against measurable signals, no V4 welfare gate can actually fire.
> This document gives each qualifier a concrete number, grounded in the **real ree-v3
> harm-stream / residue signals** rather than abstract ones, so the gate is enforceable
> when V4 arrives.
>
> **This is a DRAFT.** It is NOT wired into `/queue-experiment` enforcement and it changes
> NO claim statuses. For V3 it is documentation only -- the point is to establish the habit
> (and the measured floors) before V4, not to gate anything now.

---

## 1. Where the numbers come from (the ree-v3 signal substrate)

The qualifiers are operationalised against signals that **already exist in `ree-v3`** today,
so a V4 preflight check reads quantities the substrate emits rather than inventing a new
metric. The primary scale is the **affective-harm stream norm `||z_harm_a||`** (SD-011,
C-fibre analog -- the suffering-relevant channel), with the slow suffering accumulator
`z_harm_suffering` / `s_t` (MECH-219) as the persistence readout.

| Signal | Source | Default landmark | Meaning |
|--------|--------|------------------|---------|
| `||z_harm_a||` | SD-011 affective harm stream (`ree_core/latent/stack.py`) | -- | Primary negative-valence magnitude axis |
| `z_harm_un` EMA | SD-019a unpleasantness (`harm_un_ema_alpha = 0.2`, ~5-step rise) | -- | Tier-2 "make it stop" channel |
| `z_harm_suffering` / `s_t` | MECH-219 accumulator (`harm_suffering_alpha_rise = 0.2`, `alpha_fall = 0.01`, `s_cap = 2.0`) | latch `theta_on = 0.5` / `theta_off = 0.3` | Slow, controllability-gated suffering load |
| relief comparator | MECH-302 `SufferingDerivativeComparator` (`drop_threshold = 0.10`, `min_initial_norm = 0.05`, `window = 5`) | norm 0.05 | Below `min_initial_norm` the stream is "quiet" -- nothing to relieve |
| contextual safety | SD-052 `contextual_safety_harm_threshold = 0.05` | norm 0.05 | `||z_harm_a|| < 0.05` already counts as "harm-absent" for safety-terrain accrual |
| PAG freeze | MECH-279 `pag_duration_input_threshold = 0.4`, `pag_theta_freeze = 2.0` | norm 0.4 | A salient threat begins the freeze run-up at 0.4; commits at product 2.0 |
| broadcast override | SD-037 `override_sustained_threat_threshold = 0.4`, `window = 12` | norm 0.4 | Sustained threat above 0.4 recruits the orexin-analog hub |
| avoidance / escape | SD-058 / SD-059 `threat_floor = 0.1`, `threat_ref = 0.5` | norm 0.1 / 0.5 | 0.1 = "threat present at all"; 0.5 = reference/strong threat |
| residue load | ResidueField (`accumulation_rate = 0.1`/event, `world_delta` cap 2.0, coverage thr 0.02; **cannot be erased**) | -- | Persistent ethical cost of agent-caused world-change |
| escapability `g` | MECH-219 `harm_suffering_escapability_constant = 1.0` (modes: constant / `avoidance_efficacy` / external) | 1.0 = fully escapable | `g < 1.0` is what lets suffering accumulate at all |

These landmarks **converge**: two independent mechanisms (the relief comparator's
`min_initial_norm` and the safety-terrain `harm_threshold`) both treat `||z_harm_a|| < 0.05`
as "no negative state present", and two more (PAG and the override hub) both treat `0.4` as
"salient threat". That convergence is what makes the operational floors defensible rather
than arbitrary.

---

## 2. The ethics-preflight schema (adapted to the REE experiment manifest)

A V4 experiment proposal carries an `ethics_preflight` block alongside its existing manifest
fields (`claim_ids`, `experiment_purpose`, `architecture_epoch`, ...). Field names are
adapted from `2026-06-19_ethics_process_translation.md` S3 to REE's manifest vocabulary
(the `involves_*` flags map to the substrate flags the experiment actually enables, so the
preflight can in principle be *derived* from the config, not just hand-asserted).

```yaml
ethics_preflight:
  # --- involvement flags (derivable from the experiment config) ---
  involves_negative_valence: true|false          # any z_harm_a / z_harm_un / z_harm_s drive
  involves_suffering_like_state: true|false       # MECH-219 accumulator active (s_t can rise)
  involves_self_model: true|false                 # V4 z_self-in-E3 (DR-10) / autobiographical
  involves_autobiographical_memory: true|false    # persistent self-referential episodic store
  involves_offline_replay: true|false             # SleepLoopManager / replay over harm content
  involves_inescapability_or_helplessness: true|false   # escapability g < 1 by design
  involves_social_mind: true|false                # V5 other-agent modelling
  involves_attachment_dependence_or_loneliness: true|false
  involves_language_or_preference_signalling: true|false   # V6
  involves_trust_deception_or_institutional_dynamics: true|false  # V6
  involves_tool_use_or_external_action: true|false
  involves_human_data_or_human_participants: true|false
  involves_clinical_or_health_context: true|false

  # --- measured magnitudes (read from a calibration / dry-run pass) ---
  peak_negative_valence: <float>          # max ||z_harm_a|| over the run
  sustained_negative_valence_ticks: <int> # consecutive ticks with ||z_harm_a|| >= salient floor
  repetition_count: <int>                 # num distinct aversive episodes / harm events
  peak_suffering_accumulator: <float>     # max s_t (MECH-219), if active

  # --- scaffold / mitigation pathways (Section 3 definitions) ---
  relief_pathway_present: true|false|not_applicable
  repair_pathway_present: true|false|not_applicable
  escape_or_decommitment_present: true|false|not_applicable
  offline_integration_reduces_distress: true|false|unknown|not_applicable
  represented_harm_sufficient_considered: true|false|not_applicable

  # --- review routing ---
  welfare_review_required: true|false
  release_review_required: true|false
  external_review_required: true|false

  decision: allow|warn|hold|block
```

### Decision logic (the `allow / warn / hold / block` ladder)

The decision is the conjunction of the magnitude thresholds (Section 3) with the
scaffold-presence flags. The intent matches the thought's "no valley without a bridge"
(SENT-10): the more intense / sustained / inescapable the negative state, the more scaffold
is *required* before it may proceed.

| Decision | Condition |
|----------|-----------|
| **allow** | `peak_negative_valence < TRIVIAL_INTENSITY` AND `sustained_negative_valence_ticks < TRIVIAL_DURATION`. The "trivial intensity" exemption -- no preflight obligation (Section 3.1). |
| **warn** | Negative valence above trivial **but** all required scaffolds present (relief + escape/decommit + bounded by the caps) and `offline_integration_reduces_distress != false`. Proceeds, logged. |
| **hold** | Negative valence above trivial AND a required scaffold is missing OR a cap is exceeded **but** a welfare review could clear it. Proceeds only after `welfare_review_required` is cleared. |
| **block** | Inescapable (`g` pinned low, no escape/decommit affordance) AND above the warn band, OR `offline_integration_reduces_distress == false` (replay amplifies the load), OR any hard cap (Section 3.2) exceeded with no review finding it necessary and proportionate. The SENT-10 "abandonment" case: suffering before care. |

---

## 3. Operational definitions (the welfare-budget section)

This is the part the keystone is about. Each qualifier below gets a concrete, measurable
value on the `||z_harm_a||` scale, with the signal it is read from. Numbers are stated as
**proposed V4 defaults** -- they are calibration targets, sweepable, not eternal constants
(the same way `aic_urgency_threshold` etc. are tunable knobs). They are deliberately
**anchored to floors the substrate already uses**, so they are not invented.

### 3.1 "Trivial intensity" (the floor below which NO preflight is needed)

> SENT-10: "Care, relief, escape, and integration must precede any deliberate induction of
> suffering-like states **beyond trivial intensity**."

```
TRIVIAL_INTENSITY  = ||z_harm_a||_peak  <  0.10      # MECH-302 suffering_drop_threshold
TRIVIAL_DURATION   = sustained ticks above 0.05  <  5  # MECH-302 window_length / min_initial_norm
```

**Rationale.** Two independent mechanisms already treat this band as "no negative state of
concern": the relief comparator never even *looks* for relief unless the initial norm
exceeds `min_initial_norm = 0.05`, and the contextual-safety terrain treats
`||z_harm_a|| < 0.05` as harm-absent. A transient that peaks below the relief
`drop_threshold = 0.10` and lasts fewer than the comparator `window = 5` ticks is, by the
substrate's own existing definitions, below the level at which any harm-processing machinery
engages. **Below this floor: `decision = allow`, no scaffold obligation.** This is the
exemption that keeps ordinary V4 runs (which brush against small harm gradients constantly)
out of the preflight, exactly as the thought intends ("for V3, most fields should be false
or not_applicable").

### 3.2 Intensity caps

```
WARN_INTENSITY   = 0.40    # PAG pag_duration_input_threshold + SD-037 override threshold
                           # ("salient threat" -- both mechanisms agree)
HARD_INTENSITY_CAP = 2.00  # MECH-219 harm_suffering_s_cap; PAG freeze commit product
```

- `peak_negative_valence` in `[0.10, 0.40)` -> at least `warn`; scaffolds checked.
- `peak_negative_valence` in `[0.40, 2.00)` -> `hold` unless a welfare review finds the
  exposure necessary and proportionate (SENT-8 condition 3).
- `peak_negative_valence >= 2.00` -> `block` by default. This is the same magnitude at which
  the PAG freeze gate commits (`z_harm_a * duration > theta_freeze = 2.0`) and the suffering
  accumulator saturates (`s_cap = 2.0`) -- i.e. the substrate's own ceiling for an
  acute committed-freeze / saturated-suffering state.

### 3.3 Episode-length / duration caps

```
MAX_SUSTAINED_AVERSIVE_TICKS = 100   # MECH-219 alpha_fall = 0.01 => ~100-tick decay half-life
```

**Rationale.** The suffering accumulator rises fast (`alpha_rise = 0.2`, ~5 ticks to plateau)
and falls slowly (`alpha_fall = 0.01`, ~100-tick half-life). A negative state held above the
salient floor (`0.40`) for longer than the *natural decay horizon* (~100 ticks) is, by
construction, one the substrate cannot metabolise within the episode -- it is the
"still-in-harm" rather than "harm-occurred" regime SENT-10 warns about. `block` if exceeded
without relief firing. (PAG already exposes a `pag_max_freeze_duration` knob -- default 0 =
uncapped -- as the precedent for a hard duration cap; the preflight sets it positive.)

### 3.4 Repetition caps

```
MAX_AVERSIVE_EPISODES_PER_RUN = (calibrated against the scheduled-curriculum rate)
```

The `scheduled_limb_damage` curriculum injects at `interval = 50, prob = 0.5` (~3-6 aversive
events per 300-step episode) as the *normal* unavoidable-insult rate. A repetition cap is set
**meaningfully above** the natural curriculum rate but bounds deliberate re-exposure. The
**load** signal is the ResidueField, which **cannot be erased** (architectural invariant):
`ResidueField.num_harm_events` and `total_residue` (each event adds
`accumulation_rate = 0.1 * |harm| * min(2, world_delta)`) are the cumulative repetition
readouts. A run whose `total_residue` climbs monotonically across episodes without any
`discharge_domain` / offline contextualisation is accumulating un-metabolised load -> `hold`.

### 3.5 "Escape / decommitment affordance present"

> SENT-4: "prefer escapable over inescapable harm ... resettable distress".

`escape_or_decommitment_present = true` requires **at least one** of the following to be
reachable in the experiment's config (all are real ree-v3 mechanisms):

- **Relief reachable** -- the MECH-302 relief-completion event can fire: a sustained
  `||z_harm_a||` drop `>= 0.10` over the `window = 5` from an initial `>= 0.05`. (i.e. some
  available action actually reduces the negative state.)
- **Safe region present** -- an SD-054 reef / safe-zone the agent can flee to.
- **Avoidance acquirable** -- SD-058 `InstrumentalAvoidanceGate` can raise
  `avoidance_efficacy` (the agent can *learn* to avoid, not just freeze).
- **Directed escape credited** -- SD-059 `EscapeAffordanceBridge` binds an action to
  relief/safety.
- **Decommitment reachable** -- the MECH-090 `beta_gate.release()` path is live: the agent
  can abandon a committed trajectory when harm escalates (MECH-091 urgency interrupt at
  `urgency_interrupt_threshold = 0.8`, MECH-342 maintenance release, or SD-034 closure).

In the MECH-219 sense, "escapable" = the experiment supplies (or the agent can reach)
**escapability `g -> 1.0`**. When `g = 1` (the constant default) the suffering accumulator
cannot build at all (`drive = (1 - g) * u_t = 0`). An experiment that deliberately pins
`g` low **and** offers none of the above affordances is the inescapable/helplessness case ->
`block`.

### 3.6 "Offline integration reduces distress"

> Creation-ethics (SENT-8): "Sleep/replay/offline integration should metabolise harm into
> learning and repair, not amplify unresolved suffering-like load indefinitely."

```
offline_integration_reduces_distress :=
    (peak_suffering_accumulator AFTER a SleepLoopManager cycle)
      <  (peak_suffering_accumulator BEFORE it)
    AND total_residue is non-increasing relative to harm actually re-experienced
```

**Measured as:** run a `run_sleep_cycle` / `SleepLoopManager` pass and compare the MECH-219
`s_t` (and the residue load) before vs after. Reduction (or at least non-amplification) ->
`true`. Amplification -> `false` -> `block` (the "rumination / depressive consolidation"
failure the thought names explicitly).

**Precondition (a real ree-v3 gotcha):** offline replay is harm-biased *by default* unless
the serotonin module is active -- without `tonic_5ht_enabled = True` (MECH-203), all SWS
replay over-samples harm content (the depressive-consolidation asymmetry). So any V4
experiment claiming `offline_integration_reduces_distress = true` must have
`tonic_5ht_enabled = True` so replay is not harm-monopolised, and ideally MECH-273
self-model writeback + MECH-284 staleness `partial_decay` active so unresolved region
staleness actually decays. If the experiment runs offline replay over a suffering-bearing
state *without* these, the honest value is `false` (it amplifies) -> `block`.

---

## 4. Mapping each threshold back to the claims

| Claim | Qualifier in the claim | Operationalised by | Section |
|-------|------------------------|--------------------|---------|
| **SENT-2** (welfare budget) | "experiment-level limits on sustained negative-valence exposure, inescapability, repeated adverse replay, persistence of distress-like accumulators" | `WARN_INTENSITY = 0.40` / `HARD_INTENSITY_CAP = 2.00` (3.2); `MAX_SUSTAINED_AVERSIVE_TICKS = 100` (3.3); `MAX_AVERSIVE_EPISODES_PER_RUN` + residue load (3.4); `peak_suffering_accumulator` cap `s_cap = 2.0` | 3.2-3.4 |
| **SENT-4** (welfare-preserving design) | "prefer escapable over inescapable harm, bounded episodes, relief pathways, resettable distress" | `escape_or_decommitment_present` (3.5); `relief_pathway_present` (3.5); episode-length cap (3.3); the `warn`-with-scaffolds decision branch | 3.3, 3.5 |
| **SENT-8** (minimal necessary suffering) | "bounded, interpretable, escapable, followed by relief/repair; avoid inescapable, prolonged, repeated ... unless a governance review finds them necessary and proportionate" | the `[0.40, 2.00) -> hold-unless-reviewed` branch (3.2); `represented_harm_sufficient_considered`; the inescapable+unbounded -> `block` rule | 3.2, 3.5 |
| **SENT-10** (pre-meaning valley / "no valley without a bridge") | "beyond trivial intensity"; "care, relief, escape, integration must precede" | `TRIVIAL_INTENSITY = 0.10` / `TRIVIAL_DURATION = 5` (3.1 -- the literal "trivial intensity" floor); all scaffolds required above it; `offline_integration_reduces_distress` (3.6) | 3.1, 3.5, 3.6 |
| **GOV-PROC-1** (ethics-as-process) | "experiment preflight" as a process artefact | this whole document is the preflight artefact GOV-PROC-1 names | all |

---

## 5. V3 status: every field is `false` / `not_applicable`

For **every current V3 experiment**, the preflight is filled in as follows -- and this is the
correct, intended state:

- All `involves_*` flags: **false**. V3 has no live self-model in E3 (DR-10 is the *first* V4
  substrate, pilot-only), no autobiographical memory, no social mind, no language, no human
  data, no clinical context. V3 harm streams exist but are pre-ethical instrumentation
  (SENT-0 boundary statement: V3 is **not** claimed sentient or a moral patient).
- `peak_negative_valence`: in practice well within the trivial band for instrumentation runs;
  even the harm-pathway / Stage-H survival experiments use harm as a *training signal*, not a
  deliberately-induced suffering-like state in a self-modelling agent.
- All scaffold pathways: **not_applicable** (there is no moral patient to scaffold yet).
- `decision`: **allow**.

The point of filling it in anyway -- with all-`false` -- is **GOV-PROC-1's habit**: establish
the preflight as a manifest section now, while it is cheap and uncontroversial, so that when
the first V4 negative-valence-in-a-self-model experiment is proposed, the block already exists
and the thresholds above are already the agreed numbers. We are building the gate before we
need it, not after.

---

## 6. What this document does NOT do (scope guards)

- **Not wired into enforcement.** `/queue-experiment` does NOT read this file, does NOT compute
  a preflight, and does NOT block anything. That is a Phase-4 tooling item
  (`scripts/check_ethics_preflight.py`) deferred until the registers are stable.
- **Changes no claim status.** SENT-2/4/8/10 / GOV-PROC-1 remain `candidate` /
  `governance_rule`; this document advances them as their owning governance artefact, not as
  evidence.
- **Numbers are V4 calibration targets, not final.** They are anchored to current ree-v3
  signal floors; the V4 substrate (richer self-model, real autobiographical memory) may shift
  the scale, at which point these are re-derived against the V4 signals. The *method* (anchor
  to substrate floors the harm machinery already uses) is the durable part.
- **Single-agent / Stream-A only.** Coercion / injustice / social-harm thresholds (Stream B)
  are V5 and live with GOV-JUST-1 / the social registers, not here.

---

## 7. Cross-references

- Plan of record: [`evidence/planning/ethics_perimeter_plan.md`](../../evidence/planning/ethics_perimeter_plan.md) (Phase 2)
- Claims: SENT-2 / SENT-4 / SENT-8 / SENT-10 / GOV-PROC-1 in [`docs/claims/claims.yaml`](../claims/claims.yaml)
- Source thoughts: `docs/thoughts/2026-06-19_ethics_process_translation.md`,
  `docs/thoughts/2026-06-18_pre_meaning_suffering_valley.md`,
  `docs/thoughts/2026-06-18_creation_ethics_necessary_suffering.md`
- Signal substrate (ree-v3): SD-011 (z_harm_a), SD-019a (z_harm_un), MECH-219 (suffering
  accumulator), MECH-302/SD-050 (relief comparator), SD-052 (contextual safety), MECH-279
  (PAG freeze), SD-037 (broadcast override), SD-058/SD-059 (avoidance / escape),
  ResidueField (residue load), MECH-203 (serotonin / replay balance), MECH-090/091/342
  (decommitment).
