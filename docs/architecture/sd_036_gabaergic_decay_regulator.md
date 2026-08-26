---
title: "SD-036: GABAergic Cross-Stream Decay Regulator"
parent: "Control, Precision & Neuromodulation"
grandparent: Architecture
nav_order: 15
status: candidate/v3_pending
status_asof: 2026-07-10
status_claim: SD-036
---

# SD-036: GABAergic Cross-Stream Decay Regulator

**Claim ID:** SD-036 (parent), MECH-279 (PAG freeze-gate child)
**Subject:** `gabaergic.cross_stream_decay_regulator`
**Registered:** 2026-04-22
**Origin exemplar:** V3-EXQ-471 seed 0 ep 0 — sustained 200-step `avoid`-mode lock with
`z_harm_norm` pinned at ~0.7 absent input. See
[psychiatric_failure_modes.md](psychiatric_failure_modes.md) "Catatonia, Subtype II".
**Depends on:** SD-010, SD-011, SD-012, MECH-090, MECH-269

---

## Problem

The current V3 substrate has no mechanism by which the *absence* of input over time
returns a latent stream toward baseline. Streams integrate input (e.g. SD-010/SD-011 for
harm; MECH-090 for beta) but contain no decay regulator. A single salient event therefore
produces a permanently elevated stream value.

V3-EXQ-471 made this concrete: a single hazard contact at t=0 elevated `z_harm_norm` to
~0.82, which then stayed at ~0.7 for the remaining 199 steps despite zero harm input.
Because `z_harm` was pinned, mode arbitration stayed locked in `avoid`, the agent froze
in place, and energy ran to zero without any homeostatic rescue. The behavioural lock is
the surface symptom; the missing decay regulator is the architectural cause.

The architectural commitment SD-036 makes is that **decay is not a property of each
stream's update rule** (which would distribute the same logic across many modules and
produce inconsistent rates) **but a property of a regulatory layer that touches multiple
streams**. The biological analogue is the GABAergic system: a broadly-projecting
inhibitory neuromodulatory layer that applies tonic regulation across cortical and
subcortical sites simultaneously.

---

## Mechanism

### 1. Decay as a regulator-layer operation

For each registered stream `s ∈ S_decay`, the regulator applies in the absence of
above-threshold input:

```
z_s(t+1) = z_s(t) * exp(-tau_s * gaba_tone(t))
```

where `tau_s` is a per-stream baseline decay rate and `gaba_tone(t)` is a global
multiplier representing tonic GABAergic level. When stream input exceeds threshold, decay
is suspended for that step (the input drives the update). Otherwise, decay proceeds.

The choice of which streams are decay-eligible is an architectural commitment, not a
per-stream concern. Initial coverage:

| Stream | Decay rationale | tau (initial) |
|--------|----------------|---------------|
| `z_harm_s` (sensory harm, SD-010) | Single pain event should not drive permanent elevation | 0.05 (~20-step half-life) |
| `z_harm_a` (affective harm, SD-011) | Slower than sensory; emotional residue persists longer | 0.02 (~50-step half-life) |
| `z_beta` (precision weight, MECH-090) | Bistable gate must be able to relax | 0.03 (~30-step half-life) |
| Drive accumulator (SD-012, conditional) | Open question — see Open design questions | n/a (pending) |

> **Implementation note (2026-07-31): how the recurrence is actually realised,
> and why the mechanism above is not implemented literally.**
>
> The formula is autoregressive, so the stream must be STATEFUL. From the
> original 2026-04-22 implementation until 2026-07-31 it was not, for the two
> harm streams: `LatentStack.encode()` produced `z_harm` and `z_harm_a` as pure
> feedforward encodes of the current observation, so the regulator's per-tick
> rescale was overwritten on the next tick and `z_s(t+1)` was not a function of
> `z_s(t)` at all. `z_beta` was unaffected — it already blends with `prev_state`.
> Consequence: the regulator degenerated to a **one-step constant rescale**, and
> every scale-free DV — including `harm_norm_sustain_ratio` (= mean/peak), the
> DV of the registered dose-response falsifier in "Predicted observables" #2 —
> was **exactly invariant** to `gaba_tone`. Measured spread over the whole
> {0.3, 0.5, 1.0, 1.5, 2.0} sweep: **8.6e-08**. Observables 1–3 were all
> unbuildable; see the status log entry for the full measurement.
>
> The fix gives the streams state via a `prev_state` blend in `encode()` —
> `z_s(t) = alpha_s * encode(obs_t) + (1 - alpha_s) * z_s_decayed(t-1)` —
> which composes with the regulator's end-of-tick rescale into a leaky
> integrator with pole `(1 - alpha_s) * exp(-tau_s * gaba_tone)`. The decay
> arithmetic **stays in the regulator**; `encode()` supplies only the
> recurrence, so the architectural commitment below ("multi-target regulation
> lives at the regulator, not in each target") is preserved.
>
> **The literal "suspend decay when input exceeds threshold, else decay" switch
> was NOT implemented, because it presumes an event-like input that this
> substrate does not have.** `harm_obs` is a dense, continuously-present field
> view (hazard field + resource field + exposure). Measured over 60 steps in
> the 471-lineage environment, `||harm_obs||` ranged **2.32 to 5.21 and was
> never zero** — there is no "absence of input" tick to switch on. A hard
> switch would either never fire (low threshold) or permanently starve the
> stream of input (high threshold). The regulator's `input_threshold_*` gate
> remains as the soft form of the same idea, defaulting to off.
>
> **A caveat on the origin exemplar, which this work did not resolve.**
> `harm_encoder(zeros)` has norm **0.462** and `affective_harm_encoder(zeros,
> zeros)` **0.332**. So the "`z_harm_norm` pinned at ~0.7 despite zero harm
> input" of the V3-EXQ-471 exemplar is substantially an **encoder floor
> response to the ambient hazard field**, not purely the missing decay this
> document attributes it to. Decay toward zero fights that floor to an
> equilibrium rather than returning the stream to baseline, so observable #1
> as worded ("mode flip by ~t=50 when `z_harm_norm` decays below threshold")
> may still not be achievable at default `tau`/`alpha`. Raised for governance;
> deliberately **not** acted on in the implementing session.

### 2. GABAergic tone as global multiplier

`gaba_tone(t)` is a slow-varying scalar in `[0, 2]` representing tonic inhibitory level.
At baseline `gaba_tone = 1.0` (decay proceeds at the per-stream `tau_s`). Pharmacological
or pathological perturbation maps cleanly:

- **Benzodiazepines / GABA-A agonists:** `gaba_tone > 1` → faster decay → unlocks frozen
  streams. This is the architectural prediction matching the clinical observation that
  benzodiazepines are first-line for catatonia of the SD-036/MECH-279 subtype.
- **GABA-A receptor antibodies / benzodiazepine withdrawal:** `gaba_tone < 1` → slower
  decay across all registered streams simultaneously. Predicts the clinical cluster
  (catatonia + autonomic dysregulation + perceptual disturbance + sleep disruption) as a
  coherent architectural failure rather than four separate disorders.
- **Chronic stress / glucocorticoid-mediated GABA suppression:** sustained `gaba_tone <
  1` produces the substrate-level vulnerability for harm-stream lock-in. Matches the
  clinical observation that stress-vulnerable individuals show prolonged threat
  responses.

### 3. PAG freeze-gating (MECH-279)

The freeze response is a *committed* behavioural state — sustained motor immobility plus
elevated autonomic arousal. It is not just "no movement"; it is an active commitment to
not-move that itself has a duration and an exit criterion. Biologically this is gated by
the periaqueductal gray (PAG), where descending inputs from amygdala, hypothalamus, and
medial PFC converge on a population whose activity determines freeze vs flight vs fight
selection. PAG freeze-promoting cells are themselves GABAergic, and freeze termination
requires GABAergic inhibitory control to wane.

MECH-279 commits to this architecture:

```
freeze_commit(t) = (z_harm_a(t) * duration_above_threshold(t)) > theta_freeze
freeze_active(t) = freeze_commit OR (freeze_active(t-1) AND z_harm_a(t) > exit_threshold)
exit_threshold = theta_freeze * gaba_tone(t)
```

When freeze is active, the action selector is constrained to no-op / minimal-movement
actions. Exit requires `z_harm_a` to fall below `exit_threshold`, which depends on both
SD-036 decay (z_harm_a returns toward baseline) and `gaba_tone` (GABA agonists raise the
exit_threshold, making exit easier). This means **the same neurotransmitter system gates
both the entry and the exit** — entry via PAG freeze-cell commitment, exit via SD-036
decay returning z_harm_a below the exit threshold. The clinical observation that GABA
agonists treat freeze catatonia is an architectural prediction, not an empirical add-on.

---

## Why a regulator layer rather than per-stream decay

Two reasons:

1. **Coordination across streams.** Pathological GABAergic states (withdrawal, antibody
   syndromes) produce *clusters* of failures, not single-stream failures. Putting decay
   on a regulator layer means a single perturbation (`gaba_tone < 1`) explains the cluster.
   Per-stream decay would require coordinated multi-stream perturbation to produce the
   same clinical picture, which is architecturally less parsimonious and clinically
   harder to motivate.

2. **Pharmacological tractability.** Benzodiazepines, GABA-A antagonists, alcohol, and
   barbiturates all act at the GABA-A receptor. A regulator-layer model means these
   compounds have a single point of action with broad downstream effects, matching their
   pharmacology. A per-stream decay model would predict that benzodiazepines should have
   selective effects on specific streams — which is not what is observed.

The same logic applied to give the cingulate substrate (SD-032) a network-level
coordinator (SD-032a) rather than per-subdivision coordination. The principle:
**multi-target regulation lives at the regulator, not in each target.**

---

## Relationship to existing claims

| Existing claim | Relationship |
|----------------|--------------|
| **SD-010** (z_harm_s sensory harm stream) | Provides the substrate stream; SD-036 provides decay back to baseline. SD-010 was registered without decay; this is a substrate completion, not a contradiction. |
| **SD-011** (z_harm_a affective harm stream) | Same as SD-010. |
| **SD-012** (drive-modulated goal seeding) | Drive accumulator is *candidate* for SD-036 coverage. Open question whether drive should decay (vs. the homeostatic-override mechanism providing its own dynamics — see homeostatic_override_litpull). |
| **MECH-090** (bistable beta gate) | Bistability is preserved; SD-036 provides the decay channel that allows the gate to relax out of a stuck high-beta state. EXQ-471 showed `z_beta_val` flat at 0.0019 across 200 steps — consistent with no decay channel. |
| **MECH-269** (hippocampal anchor selection / regional verisimilitude) | Anchor reset in MECH-269 should be informed by SD-036 decay state — when the harm stream has decayed, the anchor based on the original harm event becomes invalid. See [hippocampal_anchor_selection.md](hippocampal_anchor_selection.md) post-EXQ-471 update. |
| **MECH-186/187/188** (serotonergic V4 mechanisms) | Different neurotransmitter system, different timescale. 5-HT modulates terrain/transduction/maintenance for the goal pipeline; GABA modulates decay across streams. They are co-operating regulatory layers, not alternatives. |

---

## Predicted observables (V3 scope)

A V3 experiment validating SD-036 + MECH-279 would measure:

1. **EXQ-471 lock pattern resolution.** Re-running V3-EXQ-471 with SD-036 enabled
   (default `tau_harm_s = 0.05`, `gaba_tone = 1.0`) should produce mode flip from
   `avoid` back to a goal-seeking mode by ~t=50 (when `z_harm_norm` decays below the
   mode-arbitration threshold). The seed-0 ep-0 trace would shift from "200 steps stuck"
   to "~50 steps avoid, then resumed exploration."

2. **GABA tone manipulation.** Setting `gaba_tone = 1.5` (benzo-analog) should accelerate
   recovery to ~30 steps; `gaba_tone = 0.5` (withdrawal-analog) should extend lock to
   ~100 steps or beyond. The dose-response curve is the falsifiable prediction.

3. **Multi-stream cluster.** Setting `gaba_tone = 0.3` should produce simultaneous
   failures across `z_harm_s`, `z_harm_a`, and `z_beta` — concretely, the agent should
   show prolonged harm responses, persistent over-precision, and freeze-prone behaviour
   *together*, not in isolation. This is the architectural signature distinguishing
   SD-036 from per-stream decay alternatives.

4. **MECH-279 freeze commit/exit.** Inducing sustained `z_harm_a` above `theta_freeze`
   for >5 steps should produce committed freeze (action repertoire constrained); exit
   should require `z_harm_a < exit_threshold` AND should be accelerated by `gaba_tone >
   1`. Catatonia-equivalent (gaba_tone = 0.7, sustained harm) should produce sustained
   freeze with elevated z_harm_a, matching the EXQ-471 phenotype.

Candidate experiment names (not yet queued):
- `v3_exq_NNN_sd036_decay_unlocks_exq471.py` (single-condition: SD-036 on/off, replicate
  EXQ-471 conditions)
- `v3_exq_NNN_sd036_gaba_tone_dose_response.py` (multi-condition: gaba_tone ∈ {0.3, 0.5,
  1.0, 1.5, 2.0})
- `v3_exq_NNN_mech279_pag_freeze_gate.py` (sustained-threat protocol; measure freeze
  commit, exit, and gaba_tone modulation)

Substrate hooks required:
- `ree_core/regulators/gabaergic_decay.py` — new module with `GABAergicDecayRegulator`
  registering streams and applying per-step decay.
- `ree_core/pag/freeze_gate.py` — new module hosting MECH-279 freeze commit/exit logic;
  consumes `z_harm_a` and `gaba_tone`; emits `freeze_active` boolean to action selector.
- Wiring in `ree_core/agent.py` to tick the regulator after stream updates and before
  mode arbitration.

---

## Open design questions

1. **Drive accumulator decay.** SD-012's drive accumulator (energy / hunger) is
   candidate for SD-036 coverage but ambiguously so: drive *should* keep accumulating
   under sustained deprivation (that is its point), so a simple decay would defeat its
   function. The likely resolution is that drive is *not* covered by SD-036 — instead,
   the homeostatic-override mechanism (separate, V4-or-late-V3) provides the dynamics
   that allow drive to outweigh threat under survival demand. SD-036 then covers
   regulatory streams (harm, beta, possibly precision) but not homeostatic
   accumulators. Defer to homeostatic_override_litpull synthesis.

2. **gaba_tone source.** In V3 baseline, `gaba_tone = 1.0` constant is the simplest
   first pass. A more complete model would have `gaba_tone` driven by sleep state
   (elevated during NREM, reduced during REM), by stress accumulation (chronic stress
   suppresses tone), or by external pharmacological state (for medication modeling).
   Defer specification to a V4-style 5-HT/GABA cross-state architecture (parallel to
   MECH-203/204 for serotonin).

3. **Per-stream tau learning.** First pass uses fixed per-stream `tau_s`. Long-run, the
   decay rate could itself be plastic — e.g. an agent with chronic harm exposure might
   slow `tau_harm_s` (architectural model of stress-induced sensitization). Open question
   whether this belongs in SD-036 or in a downstream plasticity claim.

4. **Interaction with the bistable beta gate (MECH-090).** MECH-090 was designed as
   bistable but EXQ-471 showed it flat — either the bistability never engaged or the
   stuck-state has no exit. Adding SD-036 decay to `z_beta` may resolve this by
   providing the exit channel. Worth confirming experimentally that SD-036 + MECH-090
   together produce *bistable-with-relaxation* behaviour, not just slow-monotonic
   behaviour.

5. **Failure mode to surface as diagnostic.** If `gaba_tone` is set too high, harm
   response is suppressed too rapidly and the agent fails to learn from harm events
   (no time for residue field update). Architecturally this matches the clinical
   observation that benzodiazepine-treated patients show impaired fear-learning. Worth
   surfacing as a diagnostic counter rather than relying on the dose-response sweep to
   catch it.

---

## Status log

- **2026-04-22** — Design doc written. SD-036 and MECH-279 reserved. Discussion origin:
  V3-EXQ-471 fishtank visualization (user observation 2026-04-22) showed 200-step
  catatonic lock with pinned `z_harm_norm` despite zero harm input; user proposed
  GABAergic decay as the missing regulator; agreement that catatonia subtype II is
  architecturally distinct from MECH-202B commit-gate paralysis.
- Registration in `claims.yaml` follows in same session.
- **2026-07-31** — Harm-stream decay **recurrence** implemented (ree-v3
  `LatentStack.encode()` + `LatentStackConfig`). Until this landed the decay
  regulator had **no temporal authority over `z_harm` (SD-010) or `z_harm_a`
  (SD-011)**, which made the entire pre-registered observable set unbuildable.
  Method: one identical recorded observation tape (60 steps, seed 0,
  471-lineage env) replayed into agents differing only in `gaba_tone`.
  Peak-normalised trajectory max-deviation vs `tone=1.0`:

  | stream | pre-fix | post-fix | raw ratio at tone=0.0 (pre-fix) | expected if pure rescale |
  |---|---|---|---|---|
  | `z_harm` | <= 2.0e-07 (bit-identical) | 1.3e-02 .. 1.8e-02 | 1.05127107 | `exp(0.05)` = 1.0512711 |
  | `z_harm_a` | <= 1.4e-07 (bit-identical) | 5.0e-02 .. 7.1e-02 | 1.02020133 | `exp(0.02)` = 1.0202013 |
  | `z_beta` | 2.0e-02 .. 2.9e-02 | unchanged | 1.09578768 | 1.03045 — does NOT match, already compounded |

  The harm-stream match to a single-tick `exp(-tau * delta_tone)` was exact to
  8 significant figures; `z_beta` was the contrast that localised the defect.
  `harm_norm_sustain_ratio` spread across the registered `gaba_tone` sweep went
  from **8.6e-08** (structurally vacuous) to **1.4e-03** (`z_harm`) and
  **1.0e-01** (`z_harm_a`, monotone decreasing in tone).
  Backward compatibility verified **differentially**: with
  `use_gabaergic_decay=False` the full latent trajectory is bit-identical to
  the pre-change substrate (max|diff| = 0.000e+00). Note `gaba_tone=0.0` with
  the master switch ON is **no longer** equivalent to the switch being off —
  decay is suspended but the recurrence is not, so use
  `use_gabaergic_decay=False` for the legacy arm and
  `gaba_recurrence_z_harm_s/_a=False` to isolate decay from recurrence.
  Contracts: `ree-v3/tests/contracts/test_sd_036_gabaergic_decay.py` C11–C16,
  which step a real `REEAgent` through `sense()` — the thing no SD-036 test did
  before, and the reason the defect survived three months. Verified to fail
  against the pre-change substrate.
  Implementation detail and the two caveats it raises (the literal
  suspend-on-input switch; the encoder-floor reading of the origin exemplar)
  are in the "Implementation note" under **Mechanism 1** above.
  No validation experiment was queued by that session — the experiment design
  is recorded in the CATATONIA-II `completion_note` in
  `evidence/planning/psychiatric_failure_modes_plan.md` and is owned by a
  separate `/queue-experiment` task.
