# Within-Life Functional-Trend Retrospective (V3-EXQ-920 Single-Continuous-Life Lineage)

**Generated:** 2026-08-14T16:16:08Z
**Chip:** `chip-20260812-exq920-multiseed-degradation-retrospective`
**Status:** COMPLETE (2026-08-18). Sections 3-5 are the original `n=1` template; Section 6's
pipeline has now been RUN verbatim over V3-EXQ-920a's 8 seeds and appended as **Section 7**.
**Section 8** answers the three follow-on questions
`failure_autopsy_V3-EXQ-920a_2026-08-16.md` Section 11 item 1 named as a zero-compute reanalysis
(empirical hazard function / wear reading, harm-dose-at-death hypothesis, seed-3 reef anomaly).
**Nothing here is scoring evidence.** Sections 3-5 are `n=1`; Sections 7-8 are `N=8`, and N=8 is
explicitly NOT a reliability claim -- no p-value is computed anywhere in this document. All readings
are hypothesis-generating, per the organism-review framing (Fishtank visual/single-run observations
are explicitly not treated as governance evidence). No claim is tagged, no `claims.yaml` edit is
made or implied.

The addendum did **not** rewrite Sections 1-5. Where the multi-seed pass *corrects* an n=1 reading
(Sections 3a/3c/4 in particular), Section 7 says so explicitly and the original text is left standing
so the revision is auditable. The one exception is **Section 5**, whose two recommendation bullets
exist to be consumed by `chip-20260814-queue-causal-sleep-matched-arm`; a superseding block was
appended there in place, with the n=1 bullets left above it.

---

## 0. What this is, and the two things it does

The 906/Fishtank organism-review lineage asked whether an REE organism's *functioning* changes over
one very long uninterrupted "day" (a single continuous life, no episode-boundary sleep opportunity
by construction -- GAP-9 in `sleep_substrate_plan.md`). V3-EXQ-920 was the first TRUE
single-continuous-life run (`EVAL_EPISODES=1`, `max_episode_steps=20000`, no body-respawn anywhere
in the observed window). It FAILed for an **execution/wiring reason only** -- only 1 of its
pre-registered 8 seeds actually ran, because the runner never translates a queue entry's declarative
`"seeds": N` into a `--seeds` CLI argument (full trace: `failure_autopsy_V3-EXQ-916-916a-917-920-
fishtank-cluster_2026-08-12.md` Target 4). The one seed that ran is scientifically clean: a genuine
`health_depleted` death at 1475 steps (not step-limit-censored), with the full per-step
`episode_log.json` preserved.

This document does two things:

1. **Re-queues the run correctly** (V3-EXQ-920a) with the seed-count workaround, so `>=2` independent
   within-life trajectories become available. **Done** -- see Section 1.
2. **Runs the descriptive early/mid/late trend analysis now, on the one existing trajectory**, as a
   worked, honest, confound-forward template -- and pre-registers the identical pipeline for the
   multi-seed follow-on. See Sections 3-6.

**Deferral, stated plainly:** V3-EXQ-920a is a long cloud run (est. 270 min worst-case, 8 seeds). The
authoring session is headless and cannot wait on it across turns. The multi-seed analysis (Section 6
pipeline over the 920a `episode_log`s) is therefore deferred to a follow-on chip
(`chip-20260814-analyse-920a-multiseed-within-life-trends`, spawned at close). Everything in
Sections 3-5 is the n=1 template that follow-on will apply.

---

## 1. The V3-EXQ-920a re-queue (record)

- **Queued:** `V3-EXQ-920a`, byte-identical driver
  (`ree-v3/experiments/v3_exq_920_uncensored_survival_single_life_fishtank.py`), with the ONLY change
  being an explicit `"args": ["--seeds","0","1","2","3","4","5","6","7"]`. `supersedes: V3-EXQ-920`.
  Diagnostic, `claim_ids=[]`, `machine_affinity: any`, priority 5 (low).
- **Committed:** ree-v3 `8fc8bd304f` (queue file only; `items: +1`, verified no sweep), pushed to
  `origin/main`. Coordinator DB add confirmed live via `POST /queue/add`
  (`applied:true, existed:false`) + `/queue/active` poll (`present`).
- **Workaround confirmed** by dry-run smoke (`--dry-run --seeds 0 1` -> two `Seed N Condition`
  boundaries + two `verdict: PASS`, rc=0). The runner passes `args` verbatim, so all 8 seeds will
  execute -- this was the exact defect V3-EXQ-920 hit.
- **Not re-proposed:** the general infrastructure fix (enforce queue-declared seed count into
  `--seeds`, or fix the driver default) is governance's / a separate infra chip's to apply, per the
  autopsy. This chip only worked around it directly.

---

## 2. The one trajectory, and why most of it is confounded

Seed 0, 1475 steps, genuine `health_depleted` death. The life is **not** one homogeneous regime --
it has three, and only the first is a clean substrate for a "within-life functioning" trend:

| Regime | steps | boundary marker | state |
|---|---|---|---|
| **A -- resourced/foraging** | t=0..~555 | resources drop 5->0, sustained-0 from t~=555 | health 1.0, energy 0.998->0.455; resources present then consumed (respawn=false) |
| **B -- post-resource-exhaustion, pre-energy-collapse** | t~=555..859 | energy reaches 0 at t=859 | health still ~1.0, no resources to replenish, energy draining |
| **C -- terminal health decline** | t~=859..1475 | health <0.5 at t=953, <0.1 at t=1371, death 1475 | starvation-driven deterministic decline to death |

**~62% of the trajectory (920 of 1475 steps) is post-resource-exhaustion (B+C).** Any telemetry
trend in that span is dominated by starvation/dying dynamics, which is a **confound distinct from any
prolonged-wakefulness effect** -- exactly the confound the chip brief flags. The clean pre-morbid
window is Regime A (~555 steps).

**Driven perturbations (not emergent), which further confound raw channel trends:**
- `world_rule_shift_occurred` fires on a fixed 250-step schedule (t = 249, 499, 749, 999, 1249) -- 5
  experimenter-injected rule shifts.
- `limb_damage_injected` fires 14x (t=150..1300) and `external_hazard_injected` 9x (t=50..1250) -- **scheduled
  injections**, not organism-caused injury. Any "injury-like" reading is a **driven input**, not
  emergent degradation (see Section 4).

---

## 3. n=1 descriptive windowed trends (Regime-A thirds + post-exhaustion flagged)

Windows over the pre-exhaustion span (t<555), split into thirds, plus a separately-flagged
post-exhaustion window. **All values n=1, hypothesis-generating.** Proxy caveat: `surprise`,
`z_beta_val`, `world_change_norm` are the driver-recorded prediction-error / world-change /
beta-valuation readouts -- they are the *nearest available* proxies but are **NOT** the E1/E2/E3
predictor uncertainties (E1/E2/E3 are separate `ree_core/predictors/*` modules; the recorded fields
were not verified to equal their internal uncertainty states). Do not label them E1/E2/E3.

**Structurally dead channels in this lineage (exclude as DVs -- not "measured zero"):**
- `residue_wanting` = 0.0 at every step. This is the **known 916a recording gap**
  (`use_proxy_fields=False` + wrong-dict `benefit_exposure` read; `benefit_exposure` structurally 0
  across the whole 664/906/909/911/912/913 lineage). `residue_wanting` is **unmeasurable** here.
- `vigor` = 0.0 throughout; `orienting_active` = 0.0 throughout. Flat, uninformative (same flatness
  the 916 autopsy noted for `vigor`).

### 3a. Candidate within-life trends (present in Regime A, before exhaustion)

| DV | early (t0-185) | mid (185-370) | late-preExh (370-555) | direction | honest read |
|---|---|---|---|---|---|
| `z_goal` | 0.327 | 0.129 | 0.051 | **monotone down** | steepest, cleanest trend; declines *within* the resourced window (0.303@t100 -> 0.041@t500) -- see confound below |
| `drive` | 0.138 | 0.277 | 0.462 | **monotone up** | mirror of z_goal; homeostatic need rising as energy drains |
| `override` | 0.568 | 0.647 | 0.677 | monotone up | modest, monotone |
| `liking` | 2.58 | 6.08 | 12.56 | **monotone up** | residue-liking accumulation |
| `surprise` (proxy) | 0.597 | 0.893 | 1.510 | **monotone up** | rising prediction-error proxy; tracks intensifying situation |
| `excite` | 0.562 | 0.841 | 1.449 | monotone up | co-moves with `surprise` |
| `dread` | 0.036 | 0.053 | 0.060 | up | small |

### 3b. Non-trend / transient / noisy channels

| DV | pattern | note |
|---|---|---|
| `z_block` | 0.09 -> **0.54** -> 0.00 | blocked-agency spike concentrated in the **mid** window, then gone -- acute/transient (Section 4) |
| `z_beta_val` (proxy) | -0.017 / -0.022 / -0.020 | no clean monotone trend pre-exhaustion; drifts toward 0 post-exhaustion |
| `world_change_norm` (proxy) | 0.093 / 0.039 / 0.046 | flat/noisy, no trend |
| `z_harm_a` | 3.77 / 0.63 / 2.48 | bounces with the injection + rule-shift schedule; not a smooth trend |
| `z_harm_norm`/`_s`/`_un` | slight decline | ~0.20 -> ~0.16; mild |
| `z_self_norm` | ~0.50 -> ~0.49 | essentially flat |
| `n_cands` | 32 constant | candidate set fixed |

### 3c. Hippocampal familiarity growth (corrected metric)

`footprint_at_cell` is the visitation count **of the currently-occupied cell**, so it is *not*
globally monotone (it jumps with position) -- the raw per-step "increment" is a misleading
familiarity measure. The correct read is **cumulative distinct cells visited** and **revisit rate**:

| by t= | cumulative distinct cells | max footprint reached | revisit_rate (window) |
|---|---|---|---|
| 185 | 19 | 23 | 0.897 |
| 370 | 34 | 46 | 0.859 |
| 555 | 45 | 47 | 0.897 |
| 1475 | 69 | 71 | 0.934 (post-exh) |

Familiarity accumulates monotonically (distinct-cell count 19->34->45->69; revisit rate ~0.9 and
rising). This is the one trend robust to the exhaustion confound -- it is spatial coverage, not an
affective/homeostatic readout.

### 3d. Action-run coherence (from `mode` / `is_committed`)

`is_committed` is **False at every step** -- commitment never engaged in this single-episode design
(consistent with the E3 commitment cadence over one unbroken episode). So "coherence" is read from
`mode`-run structure only:

| window | mean mode-run | mode-switch rate | dominant modes |
|---|---|---|---|
| early | 4.20 | 0.234 | fragmented |
| mid | **92.50** | 0.005 | locked (co-occurs with the `z_block`=0.54 spike) |
| late-preExh | 10.28 | 0.092 | re-fragmented |
| POST-exh | 5.82 | 0.171 | fragmented |

Overall mode distribution: `neutral` 740, `shelter` 322, `assert` 201, `explore` 126, `approach` 57,
`avoid` 29. The mid-window mode-locking is **not** a monotone coherence trend -- it is a transient
lock-in co-occurring with blocked agency, framed as acute/reversible in Section 4.

---

## 4. The three-way separation the brief demands (do NOT conflate)

The brief requires separating **acute reversible impairment** vs **accumulated functional
degradation** vs any **injury-like signal**. On the n=1 evidence:

- **Acute / reversible:** the **mid-window `z_block` spike (0.54) + mode-lock (mean-run 92.5)**, which
  fully resolves (`z_block` -> 0, mode re-fragments) by the late-preExh window. This is a transient
  blocked-agency episode, not a persistent change.
- **Accumulated (candidate, but CONFOUNDED):** the `z_goal` down / `drive` up / `liking` up / `surprise`
  up trends run across the whole life *including* Regime A. **But they are not separable from
  homeostatic depletion.** The mechanism is mechanical: resources deplete because consumed
  (respawn=false), so `benefit_exposure` falls, so `z_goal` (goal salience is benefit-gated) decays,
  while `drive` (homeostatic need) rises as energy drains. That is a *hungrier organism*, not
  demonstrated *degraded machinery*. At n=1 these cannot be told apart.
- **Injury-like:** **none emergent.** `limb_damage_injected` / `external_hazard_injected` are
  scheduled experimenter injections; the harm channels bounce in response to them and to the
  250-step rule-shift schedule. There is **no accumulating, self-sustaining injury signal separable
  from the scripted perturbations and the death mechanism.**

**Explicit non-transfer (brief item 3):** nothing here is evidence for anything resembling
"neurodegeneration." A single synthetic organism's activation trace, dominated by starvation and
driven perturbations, does not support that framing, and the framing does not transfer to this
substrate. The word is used here only to name what the analysis is **not** claiming.

**Health-based trends are partly tautological with death:** any health-derived "degradation" reading
is partly a direct readout of the `health_depleted` death mechanism, not independent evidence. Health
is excluded as a functioning DV (it is the outcome, not a functional index).

---

## 5. Causal limit (brief item 4 -- stated plainly)

**This design has no matched sleeping-arm control.** By construction (GAP-9), zero sleep cycles fire
within the single continuous eval episode (`total_sleep_cycles_fired=0`). So **any within-life trend,
if it survives to the multi-seed data, is prolonged-wake-ASSOCIATED, not proven caused by the absence
of sleep.** Moreover, in the one trajectory the dominant driver of the late-life trends is
**starvation** (resource exhaustion at t~=555, energy collapse at t=859), which is a confound even
against a clean "wakefulness" interpretation.

The causal test -- same life, same everything, one arm gets an experimenter-triggered sleep cycle
(via `force_cycle()`), the other does not -- is a **separate, already-designed** piece of work:
`chip-20260812-causal-sleep-deprivation-matched-arm-design` (status: **done** -- design staged), with
`chip-20260814-queue-causal-sleep-matched-arm` (status: open) waiting to queue it once this
retrospective supplies **(a) the DV set** and **(b) the sleep cadence T**. This document does **not**
duplicate that design. Its contribution to that chip:

- **Recommended DV set for the matched-arm follow-up** (drop the dead channels; keep what showed
  structure and is not purely homeostatic): `surprise` (proxy), `excite`, `z_block` (acute-impairment
  marker), cumulative-distinct-cells + revisit-rate (familiarity, exhaustion-robust), mode-run
  coherence, and `z_goal`/`drive` **only with `benefit_exposure`/resource-count recorded alongside as
  covariates** so the homeostatic confound is regressible. **Exclude** `residue_wanting`, `vigor`,
  `orienting_active` (structurally dead in this lineage). If the matched-arm run needs
  `residue_wanting`, it must first adopt the 916a fix (`use_proxy_fields=True` + `info`-dict read) --
  a substrate/driver change, not a free readout.
- **Recommended sleep-cadence placement T:** insert the experimenter-triggered sleep **inside Regime A,
  before resource exhaustion** (a candidate: T ~= 350-450 in this seed's clock, i.e. the late-preExh
  window while resources are still being consumed and `z_goal` has partly decayed but the organism is
  not yet starving). Placing it in B or C would confound the sleep effect with dying. The multi-seed
  920a data should set T per-seed relative to each seed's own exhaustion point, not an absolute step.

**UPDATED 2026-08-18 with the V3-EXQ-920a multi-seed evidence (Section 7).** The two bullets above
were written from n=1 and are superseded by the following; they are left in place so the revision is
auditable. The changes are driven by Section 7.3 (most n=1 "trends" are one deterministic energy
clock in different units) and Section 7.4 (`z_block` is not universally acute).

- **DV set for the matched-arm follow-up (revised).**
  - **Primary:** `surprise` (proxy) -- 8/8 monotone up in Regime A *and* seed-varying by an order of
    magnitude, the only channel that is both consistent and informative. **Drop `excite`**:
    `r(surprise, excite) = 0.985 .. 1.0000`, it is the same signal.
  - **Primary:** `z_block` -- **promoted** from "acute-impairment marker" to a primary DV. It is the
    only channel in the corpus showing a plausibly **irreversible** within-life change (persistent to
    death in 2/8 seeds, acute-and-resolving in 3/8), which is precisely the acute-vs-accumulated
    contrast the matched-arm design exists to adjudicate. Record it **with** `action_blocked`, since
    3/8 seeds had blocked actions with `z_block` never crossing 0.05.
  - **Primary:** mode-run length / mode-switch rate **and** dominant-mode identity -- seed 1's
    persistent `z_block` co-occurs with an `assert` mode-lock (longest run 745 steps), so the lock is
    the behavioural readout of the impairment and must be recorded alongside it.
  - **Secondary:** `liking` (8/8 up, wide cross-seed spread, but `r(liking, energy) = -0.76 .. -0.96`).
  - **Secondary:** cumulative-distinct-cells + revisit rate -- **downgraded** from the n=1 claim that
    this was "robust to the exhaustion confound". At N=8 new-cell acquisition stops mid-life in 5/8
    seeds and whole-life coverage spans 6.9%..48.6% of the grid. Report it, do not lean on it.
  - **DROP `drive` outright.** `max |drive - (1 - energy)| = 0.0015` (one step of drain) in 8/8 seeds,
    and this is **definitional** -- `ree-v3/ree_core/agent.py:10951` (SD-012): `drive_level = 1.0 -
    energy`. It is perfectly collinear with the energy covariate by construction and adds a spurious
    "8/8 consistent" line to any table it appears in. Nothing to file against the substrate; this is
    an analysis-side constraint only.
  - **`z_goal` only as a manipulation check, not as an outcome.** `r(z_goal, energy) = 0.9235` to four
    decimal places in 7/8 seeds. Its decline is a readout of the homeostatic clock; treating it as a
    functioning DV would guarantee a "significant" within-life trend that means nothing.
  - **Covariates to record (mandatory):** `energy`, resource count, **and `health`**. Health is the
    addition -- it is the one state variable that genuinely diverges across seeds (0.04 .. 0.85 at
    t=600) while energy does not, so it is what makes seeds distinguishable at all. Health remains
    **excluded as a functioning DV** (Section 4: it is the outcome, tautological with death).
  - **Still excluded:** `residue_wanting` (0.0 in 8/8 seeds -- the 916a recording gap, unmeasurable
    without the `use_proxy_fields=True` + `info`-dict fix), `orienting_active` (0 fires in 8/8),
    `vigor` (0.0 in 7/8, max 0.026 in seed 5). `is_committed` is False at all 13718 steps across all
    seeds, so commitment cannot be a DV in a single-episode design at all.
- **Sleep-cadence placement T (revised, and now SIMPLER than the n=1 recommendation).** The n=1 pass
  recommended setting T per-seed relative to each seed's own exhaustion point. **That is unnecessary
  and should not be implemented:** in 920a the pre-registered resource-exhaustion boundary fires in
  **0/8** seeds, and the energy ramp is bit-identical across seeds (0.0015/step, reaching 0 at
  t=666), so "each seed's own boundary" is the same absolute step in every seed. **Use an absolute
  T ~= 400**, and state the reasoning rather than the number: at t=400 median energy is 0.398 (well
  clear of collapse), median `z_goal` has already fallen from 0.366 to 0.063 (so the homeostatic
  decay to be perturbed is underway), and **all 8/8 seeds are still alive** -- the shortest life was
  628 steps, so T=400 is inside every seed's life with ~228 steps of margin. T=450-500 would still
  clear the shortest seed but with much less margin; T<250 lands before `z_goal` has moved. Verify
  liveness against the run's own minimum survival before fixing T, and if the matched-arm run's
  substrate changes the energy drain rate, re-derive t=666 rather than copying it.

---

## 6. Pre-registered multi-seed analysis pipeline (turnkey for the 920a follow-on)

When V3-EXQ-920a lands, run this **verbatim** per seed and append as Section 7. It is deliberately
descriptive/non-parametric -- **n=2-8 is NOT adequate for a reliability claim**; report trends as
hypothesis-generating only.

1. **Per-seed regime boundaries.** For each seed, find (a) resource-exhaustion t (first sustained
   resources==0), (b) energy-collapse t (first energy<=0), (c) health milestones (<0.5, <0.1). Define
   Regime A = t<exhaustion. **Restrict the primary trend analysis to Regime A**; report B+C
   separately, flagged as starvation-confounded.
2. **Windowed descriptives** (Regime-A thirds + post-exhaustion) for the DV set in Section 5, using
   median + IQR (not mean+/-sd) given small n and non-normal channels.
3. **Familiarity:** cumulative-distinct-cells and revisit-rate per window (NOT raw `footprint_at_cell`
   per-step).
4. **Coherence:** mode-run length + mode-switch rate per window; report `is_committed` fraction (expect
   ~0).
5. **Homeostatic-confound covariates:** record `benefit_exposure`-proxy (or resource count) and energy
   alongside `z_goal`/`drive` so a reader can see the coupling.
6. **Cross-seed consistency (descriptive only):** for each candidate trend, report in how many of the
   N seeds the Regime-A direction is monotone (e.g. "z_goal declined in Regime A in k/N seeds"). Do
   **not** compute a p-value or claim reliability at N<=8.
7. **Separation restated per seed:** acute (transient `z_block`/mode-lock) vs accumulated
   (Regime-A monotone, confound-flagged) vs injury (confirm still driven-only: cross-check every
   harm-channel excursion against the injection/rule-shift schedule).

Reference implementation: the n=1 pass's script was left in a session scratchpad and did NOT survive,
exactly as warned here. The 920a follow-on therefore re-derived it and landed it as a TRACKED file --
`evidence/planning/within_life_functional_trend_920a_pipeline.py` (REE_assembly `9878275d30`). Any
further re-run should start from that file, not from a scratchpad.

---

## 7. Multi-seed addendum (V3-EXQ-920a, N=8) -- FILLED 2026-08-18

**Appended by** `chip-20260814-analyse-920a-multiseed-within-life-trends` (session
`metaworker-chip-20260814-analyse-920a-multiseed-within-life-trends`), running Section 6's
pre-registered pipeline **verbatim** over the 8 per-seed `episode_log`s of
`v3_exq_920_uncensored_survival_single_life_fishtank_20260814T223432Z_v3`.
**Reference implementation, now TRACKED** (the n=1 pass's script was left in a scratchpad and did
not survive, as Section 6 warned): `evidence/planning/within_life_functional_trend_920a_pipeline.py`,
REE_assembly `9878275d30`. Re-running it reproduces every number below.

**Nothing here is scoring evidence.** N=8 is not a reliability claim; no p-value is computed
anywhere. Sections 1-5 are not rewritten -- where this addendum *corrects* an n=1 reading, it says so
explicitly rather than editing the earlier text.

### 7.0 Provenance, and one comparability caveat that must be read first

- 8/8 seeds ran (the `--seeds` workaround of Section 1 worked); **8/8 died uncensored**
  (`done_cause=health_depleted`, `pct_right_censored_pooled=0`). Survival: min 628, median 1831,
  mean 1714.75, max 2527 steps.
- **`total_sleep_cycles_fired = 0.0`** -- the GAP-9 premise of Section 5 holds for 920a exactly as it
  did for 920. No sleep opportunity fired inside any life.
- `env_config` is **byte-identical** between 920 and 920a.
- **CAVEAT: 920a is not a pure seed-count re-run of 920.** The substrate moved **114 commits**
  between them (`fc0fb4ce5c` -> `bf769fb3a4`), including `sleep_substrate:GAP-9 (v1 ceiling arm):
  within-life sleep trigger`, a `MECH-303` proximity-anticipatory harm-signal change and a
  `MECH-267` CEM-selection change. Concretely, **seed 0 does not reproduce**: 920 seed 0 died at
  1475 steps having consumed its resources to 0 by t~=600; 920a seed 0 died at 1944 steps and never
  dropped below 1 resource. So Section 3's n=1 numbers are **not** a within-lineage baseline for the
  numbers here -- treat Section 3 as a methods template that was applied, not as seed 0 of this N=8.

### 7.1 Step 1 -- per-seed regime boundaries (and a pre-registration failure worth stating)

**The pre-registered PRIMARY boundary did not fire in any seed.** Section 6 step 1(a) defines Regime
A by "first sustained `resources==0`". In 920a resources are **never** sustained-0 in **0/8** seeds
(per-seed min resource count 1,1,2,5,1,1,1,4). The pipeline therefore fell through to boundary (b),
first `energy<=0`, and for seed 5 (which died first) to whole-life.

| seed | life (steps) | (a) resource-exh | (b) energy<=0 | health<0.5 | health<0.1 | res start/min/end | Regime-A end |
|---|---|---|---|---|---|---|---|
| 0 | 1944 | never | 666 | 676 | 1887 | 5/1/1 | 666 |
| 1 | 1432 | never | 666 | 639 | 1295 | 5/1/1 | 666 |
| 2 | 1846 | never | 666 | 1066 | 1807 | 5/2/2 | 666 |
| 3 | 1008 | never | 666 | 558 | 709 | 5/5/5 | 666 |
| 4 | 2527 | never | 666 | 1069 | 2503 | 5/1/1 | 666 |
| 5 | 628 | never | never (died first) | 403 | 546 | 5/1/1 | 628 (whole life) |
| 6 | 2517 | never | 666 | 2235 | 2513 | 5/1/1 | 666 |
| 7 | 1816 | never | 666 | 1436 | 1765 | 5/4/4 | 666 |

**`t=666` is a clock, not an event.** Energy drains at a fixed 0.0015/step from 0.9985, so it reaches
0 at t=666 **by arithmetic**, in every seed, independent of anything the organism does. Verified
directly: the energy trace over t<666 is **bit-identical to seed 0's in 7 of 8 seeds** (seed 5 is the
only exception, and only because it died at 628). Health, by contrast, genuinely diverges across
seeds (at t=600: 0.04 .. 0.85). So Regime A here is a fixed 666-step interval shared by all seeds --
which is convenient for the matched-arm design (Section 7.6) and **fatal to the naive reading of the
consistency table** (Section 7.3).

### 7.2 Steps 2-5 -- Regime-A windowed descriptives (median [Q1,Q3])

Full per-seed tables are reproduced by the tracked script. Compressed here as the **range of the 8
per-seed window medians**, which is the quantity that matters for judging cross-seed consistency:

| DV | early | mid | late-preExh | POST-exh |
|---|---|---|---|---|
| `z_goal` | 0.237 .. 0.295 | 0.078 .. 0.098 | 0.026 .. 0.034 | 0.000 .. 0.008 |
| `drive` | 0.156 .. 0.166 | 0.470 .. 0.499 | 0.784 .. 0.832 | 0.775 .. 1.000 |
| `energy` (covariate) | 0.833 .. 0.842 | 0.500 .. 0.529 | 0.167 .. 0.215 | 0.000 .. 0.225 |
| `n_resources` (benefit covariate) | 2.0 .. 5.0 | 1.0 .. 5.0 | 1.0 .. 5.0 | 1.0 .. 5.0 |
| `surprise` (proxy) | 0.000 .. 0.605 | 0.057 .. 1.782 | 0.144 .. 2.708 | 0.597 .. 3.982 |
| `excite` | 0.000 .. 0.459 | 0.057 .. 1.705 | 0.132 .. 2.505 | 0.579 .. 3.831 |
| `liking` | 0.000 .. 4.062 | 0.625 .. 19.049 | 12.798 .. 32.777 | 9.716 .. 31.240 |
| `override` | 0.579 .. 0.652 | 0.667 .. 0.725 | 0.726 .. 0.786 | 0.746 .. 0.818 |
| `dread` | 0.000 .. 0.127 | 0.000 .. 0.164 | 0.001 .. 0.256 | 0.017 .. 0.297 |
| `z_harm_a` | 1.319 .. 5.711 | 1.080 .. 6.025 | 0.439 .. 6.620 | 0.507 .. 9.177 |

**Read the spread, not just the direction.** `z_goal`/`drive`/`energy`/`override` have cross-seed
spreads far narrower than their within-life change; `surprise`/`excite`/`liking` vary by an order of
magnitude across seeds while still moving the same way. That distinction is the whole content of
Section 7.3.

**Familiarity (step 3)** -- cumulative distinct cells, NEW cells per window, revisit rate:

| seed | new cells early/mid/late/POST | distinct cells by end of Regime A | over whole life | grid coverage | revisit rate early/mid/late |
|---|---|---|---|---|---|
| 0 | 23/0/10/37 | 33 | 70 | 48.6% | 0.896/1.000/0.955 |
| 1 | 7/20/11/20 | 38 | 58 | 40.3% | 0.968/0.910/0.950 |
| 2 | 8/0/4/55 | 12 | 67 | 46.5% | 0.964/1.000/0.982 |
| 3 | 7/3/0/0 | 10 | 10 | 6.9% | 0.968/0.986/1.000 |
| 4 | 5/9/0/51 | 14 | 65 | 45.1% | 0.977/0.959/1.000 |
| 5 | 26/9/0/-- | 35 | 35 | 24.3% | 0.876/0.957/1.000 |
| 6 | 14/2/0/42 | 16 | 58 | 40.3% | 0.937/0.991/1.000 |
| 7 | 5/5/0/31 | 10 | 41 | 28.5% | 0.977/0.977/1.000 |

New-cell acquisition falls to **zero in the late-preExh window in 5/8 seeds**, and revisit rate
reaches 1.000 in 5/8 -- i.e. spatial coverage **saturates before the energy clock runs out**. But
displacement rate (fraction of steps where position changed) has **no consistent direction** across
seeds (seed 1 rises 0.027 -> 0.365 -> 0.243; seed 3 collapses 0.706 -> 0.063 -> 0.000), so this is
coverage saturation, not a demonstrated loss of locomotion, and it is not separable from the energy
clock. **This corrects the n=1 reading in Section 3c**, which called monotone familiarity growth "the
one trend robust to the exhaustion confound": at N=8, growth *stops* mid-life in most seeds, and the
whole-life spread is enormous (10 to 70 distinct cells, 6.9% to 48.6% of the 12x12 grid).

**Coherence (step 4)** -- `is_committed` is **False at every step of every seed** (0/13718 steps),
confirming Section 3d's n=1 observation as a structural property of the single-episode design, not a
seed accident. Mode-run length has no consistent direction (up-monotone in 3/8, non-monotone in 5/8);
dominant mode differs wildly by seed (`neutral` in 0/2/4, `assert` in 1, `shelter` in 3/7, `avoid` in
5/6), so "mode-lock" is a per-seed phenomenon, not a life-stage one.

### 7.3 The degeneracy finding -- 8/8 monotone is NOT 8 independent replications

This is the most important result of the multi-seed pass, and it **downgrades** the n=1 candidate
trends rather than confirming them.

- **`drive` is an algebraic restatement of `energy` -- BY DESIGN, not by accident.**
  `max |drive - (1 - energy)| = 0.0015` -- exactly one step of drain -- in **all 8 seeds** across all
  of Regime A, and the substrate confirms this is definitional: `ree-v3/ree_core/agent.py:10951`
  (SD-012) states `drive_level = 1.0 - energy (obs_body[3])`. So this is not a substrate defect to
  file; it is an **analysis** constraint. `drive` carries **zero** information beyond `energy` and
  must never be counted as a second confirming DV -- doing so adds a free "8/8 consistent" row to any
  table it appears in, which is exactly what Section 3a did at n=1.
- **`energy` is the same deterministic ramp in every seed** (7/8 bit-identical, Section 7.1). Its
  "8/8 monotone decline" is one curve counted eight times.
- **`z_goal` is a near-deterministic function of that same ramp.** `r(z_goal, energy)` over Regime A
  is **0.9235 in 7 of 8 seeds -- identical to four decimal places** (seed 5: 0.9306, and only because
  its window is shorter). A correlation that agrees to 4 dp across independent RNG streams is not
  eight independent measurements of a relationship; it is one relationship re-instantiated.
- **`surprise` and `excite` are near-duplicate channels**: `r(surprise, excite) = 0.985 .. 1.0000`
  across seeds. Reporting both as separate DVs double-counts one signal.

So of Section 3a's seven "candidate within-life trends", the cross-seed data supports **at most
two independent ones**:

| DV | k/N monotone in Regime A | independent? | verdict |
|---|---|---|---|
| `z_goal` | 8/8 down | **no** -- r with energy fixed at 0.9235 | homeostatic clock readout |
| `drive` | 8/8 up | **no** -- identically `1 - energy` | drop as a DV |
| `energy` | 8/8 down | **no** -- deterministic ramp | covariate, never a DV |
| `override` | 8/8 up | doubtful -- narrow spread, r(override,energy) = -0.78 .. -0.87 | clock-coupled |
| `surprise` (proxy) | 8/8 up | **partly** -- magnitudes span 0.000 .. 2.708, r with energy varies -0.82 .. -0.98 | candidate |
| `excite` | 8/8 up | **no** -- duplicate of `surprise` | fold into `surprise` |
| `liking` | 8/8 up | **partly** -- wide spread, but r(liking,energy) = -0.76 .. -0.96 | weak candidate |
| `dread` | 5/8 up, 3/8 non-monotone | -- | not consistent |
| `z_block` | 0/8 monotone (8/8 non-monotone) | -- | not a trend (see 7.4) |
| `z_harm_a` | 4/8 down, 2/8 up, 2/8 non-monotone | -- | not consistent |
| `n_resources` | 0/8 monotone | -- | not consistent |
| revisit rate | 3/8 up, 5/8 non-monotone | -- | not consistent |
| mode-run length | 3/8 up, 5/8 non-monotone | -- | not consistent |

**The honest summary: the only channels that both move consistently and carry seed-specific
information are `surprise` (with `excite` folded in) and, more weakly, `liking` -- and both remain
strongly energy-coupled, so neither is separable from the homeostatic ramp on this design.** N=8 does
not rescue the Section 3a candidates; it shows most of them were the energy clock in different units.

### 7.4 Step 7 -- the three-way separation, restated per seed

**Injury: still driven-only, now confirmed across all 8 seeds.** Every one of the 136 limb-damage and
122 external-hazard injections lands exactly on a multiple of 50, every one of the 557 blocked-action
steps on a multiple of 10, and every world-rule shift on the fixed 250-step cadence (sole inter-shift
gap = 250 in all seeds) -- **0 off-grid events in 8/8 seeds**, matching the declared
`scheduled_*_interval` config exactly. The emergent `harm_event` channel (656 events, ~99% off-grid,
i.e. proximity-driven rather than injected) shows **no consistent within-life direction**: its rate
rises late in seeds 1 and 3, falls in seeds 0 and 2, peaks mid-life in seed 5. **There is no
accumulating, self-sustaining injury signal in any seed.** Section 4's finding survives N=8 intact,
and it is the one part of the n=1 read that strengthens.

**Acute vs accumulated: the n=1 read was WRONG about acuteness, and this is a genuine correction.**
Section 4 called the `z_block` spike "acute / reversible ... a transient blocked-agency episode".
At N=8 that generalisation fails. Fraction of steps with `z_block > 0.05`, per window:

| seed | early | mid | late-preExh | POST-exh | pattern |
|---|---|---|---|---|---|
| 0 | 0.10 | 0.00 | 0.00 | 0.00 | acute, resolves (matches the n=1 read) |
| 4 | 0.00 | 0.22 | 0.00 | 0.00 | acute, resolves |
| 2 | 0.00 | 0.14 | 0.10 | 0.00 | mild, resolves |
| 3, 5, 6 | 0.00 | 0.00 | 0.00 | 0.00 | `z_block` never exceeds 0.05 (though `action_blocked` did fire 47/28/97 times) |
| **1** | 0.00 | **0.41** | **0.95** | **0.99** | **onsets mid-life and NEVER resolves -- to death** |
| **7** | 0.00 | 0.00 | **0.52** | 0.31 | **onsets late and persists past the clock** |

So blocked-agency is **acute and reversible in 3/8, never registered above threshold in 3/8, and persistent-to-death in 2/8**.
In seed 1 it co-occurs with a mode-lock into `assert` (1052/1432 steps; POST-exh mean mode-run 127.7,
longest run 745) -- an organism stuck in one mode with agency blocked for the last two-thirds of its
life. **This is the closest thing in the dataset to a non-reversible within-life functional change,
and it is exactly the kind of thing the n=1 pass could not see.** It is reported as
hypothesis-generating: with 2/8 it is equally consistent with a rare bistable trap as with a
prolonged-wake effect, and the design cannot distinguish those (Section 7.5).

**Dead channels, re-checked at N=8:** `residue_wanting` is 0.0 at every step of every seed (the 916a
recording gap, unchanged -- still **unmeasurable**, not "measured zero"); `orienting_active` fires 0
times in 8/8 seeds; `vigor` is 0.0 in 7/8 seeds and reaches a negligible 0.026 in seed 5, so
Section 3's "flat throughout" is very slightly overstated but the DV-exclusion stands.

### 7.5 What did NOT change: the causal limit

Everything in Section 5 about causality holds unchanged, and N=8 does not weaken it:

- Still **no matched sleeping-arm control**; `total_sleep_cycles_fired = 0` in 8/8 seeds. Any trend
  above is prolonged-wake-**associated** at best.
- The dominant driver of the Regime-A trends is now demonstrably **the deterministic energy ramp**,
  which is a *stronger* confound statement than the n=1 pass could make: it is not merely that
  starvation co-varies with time, it is that `drive` and `z_goal` are near-algebraic functions of a
  clock every seed shares.
- N=8 with 8/8 agreement on a clock-driven channel is **not** evidence of reliability. Reporting it
  as such would be the exact degeneracy Section 9 forbids.

### 7.6 Updated inputs for the matched-arm causal follow-up

Section 5 is updated in place with the multi-seed evidence; the substantive changes are: `drive` and
`excite` dropped as redundant, `z_block` promoted (it is the only channel showing a plausibly
irreversible per-seed change), health added as a divergence covariate, and cadence T re-specified as
an absolute step because the energy clock is seed-invariant. See Section 5 for the recommendation
that `chip-20260814-queue-causal-sleep-matched-arm` should consume.

---

## 8. Zero-compute reanalysis: the three follow-on questions (2026-08-18)

**Appended by** `chip-20260816-920a-episode-log-reanalysis`, answering the three questions
`failure_autopsy_V3-EXQ-920a_2026-08-16.md` Section 11 item 1 names as "answerable with zero new
compute" from the already-committed 34.8 MB per-step episode log (8 seeds, all `health_depleted`).
Reference implementation, tracked:
`evidence/planning/within_life_functional_trend_920a_reanalysis_pipeline.py`. Re-running it
reproduces every number below.

**Nothing here is scoring evidence.** N=8, descriptive, no p-values -- same discipline as Sections 0
and 7. This section answers the autopsy's three named questions only; it does not otherwise revise
the DV/methodology recommendations of Sections 5/7.6.

### 8.1 Q1 -- does the "wear" (accumulating-damage) reading hold up?

**Yes, on three independent readings of the same 8 survival times (628, 1008, 1432, 1816, 1846, 1944,
2517, 2527), none of which require fitting a distribution** (autopsy Section 6c is right that n=8
cannot do that -- these are model-free checks, not a fitted comparison).

1. **Coefficient of variation is a distribution-free memorylessness test.** Any constant-hazard
   (homogeneous-Poisson) death process forces i.i.d. Exponential survival times, whose CV is exactly
   1 regardless of the rate. Observed: mean 1714.75, sd 670.17, **CV = 0.391** -- well below 1, which
   is inconsistent with constant hazard and consistent with an increasing (wear-out / IFR) hazard.
2. **Discrete-time hazard rises with age.** Pooling all 8 lives into 500-step bins (912's own segment
   scale) and computing deaths-in-bin / at-risk-at-bin-start:

   | bin | at risk | deaths | hazard |
   |---|---|---|---|
   | 0-500 | 8 | 0 | 0.000 |
   | 500-1000 | 8 | 1 | 0.125 |
   | 1000-1500 | 7 | 2 | 0.286 |
   | 1500-2000 | 5 | 3 | **0.600** |
   | 2000-2500 | 2 | 0 | 0.000 |
   | 2500-3000 | 2 | 2 | 1.000 |

   Hazard climbs monotonically 0 -> 0.125 -> 0.286 -> 0.600 through the informative range (0-2000,
   where at-risk is still >=5). The last two bins are a small-n edge artifact, not a genuine
   dip-then-spike: only 2 seeds remain, and both die at 2517/2527 -- just past the 2500 boundary --
   so the 2000-2500 zero is an artifact of where that boundary happens to fall, not evidence hazard
   fell. Read the table as "rises through 2000, then n=2 is too small to resolve further."
3. **A self-referential memoryless null (fit to this run's own mean, no import from 912) shows the
   classic IFR crossing pattern.** Rate `lambda = 1/1714.75 = 0.000583/step`:

   | t | predicted P(survive) | observed fraction alive |
   |---|---|---|
   | 666 (energy clock zero) | 0.678 | **0.875** (7/8) |
   | 1000 | 0.558 | **0.875** (7/8) |
   | 1500 | 0.417 | **0.625** (5/8) |
   | 2000 | 0.312 | **0.250** (2/8) |
   | 2500 | 0.233 | 0.250 (2/8) |

   Observed survival is ABOVE the memoryless prediction early (more alive than a constant hazard at
   this average rate would predict) and falls BELOW it late (t=2000) -- the curves cross once, from
   above to below. That crossing is the textbook signature of an increasing hazard: fewer early
   deaths than memorylessness predicts, then a late-life cluster it does not predict.

**Cross-check against the imported 912 calibration** (autopsy Section 6b, reproduced here from the
run's own numbers): 912's per-500-step hazard `p=4/60=0.0667` implies a memoryless mean of `500/0.0667
= 7500` steps. Observed mean 1714.75 is **4.37x** earlier -- matches the autopsy's "4.4x" (rounding).

**Verdict: the wear reading holds up under all three checks, and two of the three (CV, the crossing
pattern) do not depend on 912 at all.** As the autopsy already states, 912 could not have seen this:
every 912 segment began with a fresh body, so 912 measured a fresh-body (low, roughly flat) hazard by
construction, and a fresh-body hazard is exactly what the 500-1500 range of the bin table above still
looks like -- the wear term only becomes visible past ~1500 steps, which no 912 segment (261-487 max)
ever reached.

### 8.2 Q2 -- the harm-dose-at-death hypothesis, verified against per-step `harm_event`/`health`

**Confirmed exactly, by direct recount from the raw per-step boolean, with no discrepancy from the
autopsy's summary-stat reconstruction.**

| seed | survival | harm_total (direct count) | harm_rate |
|---|---|---|---|
| 0 | 1944 | 93 | 0.0478 |
| 1 | 1432 | 88 | 0.0615 |
| 2 | 1846 | 81 | 0.0439 |
| 3 | 1008 | 72 | 0.0714 |
| 4 | 2527 | 98 | 0.0388 |
| 5 | 628 | 57 | 0.0908 |
| 6 | 2517 | 94 | 0.0373 |
| 7 | 1816 | 73 | 0.0402 |

Counting `harm_event == True` directly over each seed's per-step trace reproduces `[57, 72, 73, 81,
88, 93, 94, 98]` -- **byte-identical to the autopsy's reconstruction** from
`lifetime_affective_occupancy` (`frac_harm_event x n_lived_steps_measured`). The reconstruction was
lossless; this section is not a correction of Section 6b, it is an independent confirmation of it.

- **Stereotypy:** harm-dose mean 82.00, sd 13.96, **CV 0.170**; survival mean 1714.75, sd 670.17, CV
  0.391. Ratio **2.30x** -- matches the autopsy's "2.3x more stereotyped" exactly.
- **Rate anti-correlates with survival:** Spearman(harm_rate, survival) = **-0.881** -- exact match.
- **Raw total count is NOT anti-correlated with survival** (Spearman(harm_total, survival) = **+0.929**)
  -- stated explicitly because it could otherwise look like a contradiction. It is not: a longer life
  gives more opportunities to encounter harm even at a lower per-step rate, so total count rises with
  duration almost mechanically (seed 4: 2527 steps, rate 0.0388, total 98; seed 5: 628 steps, rate
  0.0908, total 57). The informative quantity is the RATE, and the fact that the total stays within a
  narrow 57-98 band (max/min 1.72) despite a 4.02x range in survival time.
- **New finding: health is not monotonic, and the anomaly is resource-gated.** Net lifetime health
  change is exactly `-1.0` in 7 of 8 seeds (seed 3: `-0.9901`, matching its own non-unit starting
  health), but every seed except seed 3 shows 1-4 discrete UPWARD health jumps over its life (total
  "healing" 0.15-0.60, e.g. seed 1 and seed 4 both show exactly 4 jumps). Seed 3 shows **zero**. The
  jump count tracks resources consumed per seed closely (seed 3: 0 consumed / 0 jumps, the single
  cleanest case; seed 1 and seed 4: 4 consumed / 4 jumps, exact matches elsewhere), consistent with
  health regeneration being gated on successful resource consumption. This is a genuinely new
  observation (not named in the autopsy) and feeds directly into 8.3.
- **A secondary, hedged figure -- do not lean on it.** "Mean health-drop per harm event"
  (total negative health delta / harm_total) is 0.0166 +/- 0.0026 across seeds (CV 0.158), close to
  but not identical to the naive `1/mean(harm_total) = 0.0122` implied by a flat 1.0-unit budget spread
  evenly over ~82 hits. This is **not a clean per-event attribution**: ~2.5% of health-decrementing
  steps in a sampled seed carry no `harm_event` flag at all (likely continuous `harm_signal` exposure
  or injection-driven decrements not gated by the discrete marker), and the regen jumps above partly
  offset losses in the same sum. Report as compatible with, not independent confirmation of, the dose
  story.

**Verdict: the harm-dose-at-death hypothesis survives this direct per-step check unchanged.** The
mechanism reading in the autopsy -- death occurs at an approximately fixed harm-tolerance budget, and
survival time is that budget divided by encounter rate -- is coherent with 8.1's wear-out finding:
the "damage" driving the rising hazard is, to first approximation, integrated harm exposure, and
seeds that happen to encounter harm less often survive longer to reach the same roughly-fixed dose
ceiling. Still n=8, still descriptive, still not distinguishing this from other dose-accumulation
mechanisms that would produce the same aggregate signature.

### 8.3 Q3 -- the seed-3 reef anomaly, explained

**A concrete, well-evidenced mechanism, built from several independent facts in the committed log --
not merely "unexplained" as the autopsy left it.**

| seed | survival | frac_reef | harm_tot | harm_rate | rate_in_reef | rate_out_reef | transitions | trans_rate | resources s/min/end | hazards_in_reef | health<0.5 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1944 | 0.268 | 93 | 0.0478 | 0.0864 | 0.0337 | 27 | 0.0139 | 5/1/1 | 3/4 | 676 |
| 1 | 1432 | 0.224 | 88 | 0.0615 | 0.0654 | 0.0603 | 22 | 0.0154 | 5/1/1 | 0/4 | 639 |
| 2 | 1846 | 0.236 | 81 | 0.0439 | 0.0321 | 0.0475 | 20 | 0.0108 | 5/2/2 | 1/4 | 1066 |
| **3** | **1008** | **0.919** | 72 | 0.0714 | **0.0551** | **0.2561** | **39** | **0.0387** | **5/5/5** | **3/4** | **558** |
| 4 | 2527 | 0.302 | 98 | 0.0388 | 0.0537 | 0.0323 | 44 | 0.0174 | 5/1/1 | 1/4 | 1069 |
| 5 | 628 | 0.072 | 57 | 0.0908 | 0.1111 | 0.0892 | 20 | 0.0318 | 5/1/1 | 0/4 | 403 |
| 6 | 2517 | 0.158 | 94 | 0.0373 | 0.1357 | 0.0189 | 14 | 0.0056 | 5/1/1 | 1/4 | 2235 |
| 7 | 1816 | 0.478 | 73 | 0.0402 | 0.0484 | 0.0327 | 9 | 0.0050 | 5/4/4 | 3/4 | 1436 |

Spearman(frac_in_reef, survival) = **+0.095** -- exact match to the autopsy. Confirmed: reef time
alone predicts nothing across the cohort (seed 6 has low reef time and long survival; seed 7 has high
reef time and long survival; reef occupancy is not the load-bearing variable). Seed 3 is explained by
a specific combination, not by "reef time" as a scalar:

1. **The reef is structurally foodless, corpus-wide.** 0 of 16 resources spawned across all 8 seeds
   ever land inside a reef cell -- 0 in every individual seed, not just seed 3. This is a geometric
   property of the reef/resource placement, not a seed accident.
2. **Seed 3 uniquely never ate.** `resources s/min/end = 5/5/5` -- the only seed of 8 whose resource
   count never moved. Given fact 1, this is the direct, mechanical consequence of spending 91.9% of a
   1008-step life inside a zone that cannot contain food: seed 3 rarely left long enough to forage.
3. **The reef is not harm-free.** `harm_event` fires while `in_reef` in all 8 seeds (14-54 events per
   seed), and in 3 of 8 (seeds 0, 5, 6) the in-reef rate exceeds the out-of-reef rate -- "shelter" is
   not generically protective in this corpus. For seed 3 specifically the reef WAS partially
   protective per-step (0.0551 in-reef vs 0.2561 out-of-reef, a 4.6x reduction), but that in-reef rate
   is still nonzero, and combined with 91.9% occupancy it still produced 51 of seed 3's 72 total harm
   events (71%) from inside the "safe" zone.
4. **Seed 3 drew an unusually hazardous reef layout and then stayed in it.** 3 of seed 3's 4 initial
   hazards spawn inside its own reef cells -- tied for the corpus maximum (also 3/4 for seeds 0 and 7)
   -- but seeds 0 and 7 occupied their reefs only 26.8% and 47.8% of the time, versus seed 3's 91.9%,
   so seed 3 is exposed to its hazard-dense draw far more than the other two seeds that drew the same
   count.
5. **Seed 3's excursions out of the reef were unusually costly and unusually frequent.** Its
   boundary-transition rate (39 crossings / 1008 steps = 0.0387/step) is the highest of all 8 seeds,
   and its out-of-reef harm rate (0.2561/step) exceeds every OTHER seed's overall (whole-life) harm
   rate -- the next-highest overall rate anywhere in the corpus is seed 5's 0.0908. So the margin it
   crossed into repeatedly was worse than any seed's typical environment.
6. **The fatal decline is harm-driven, not the post-exhaustion starvation pattern.** Health drops
   below 0.5 at t=558, before the shared energy-clock boundary at t=666 (Section 7.1) -- i.e. before
   the point the n=1 template (Section 2/4) associates with starvation-driven terminal decline. Seed
   3's death is not a starvation cascade in that sense.
7. **Seed 3 is the only seed that received zero within-life healing** (8.2's new finding): every
   other seed shows 1-4 discrete health-regen jumps, gated (imperfectly but consistently) on resource
   consumption; seed 3, having eaten nothing, got none.

**Verdict: the anomaly is a specific, identifiable combination of a foodless-by-construction reef, a
personally hazard-dense reef draw, an unusually costly and unusually frequent set of excursions, and
a consequent total loss of within-life healing -- not a generic property of "spending time in the
reef."** The other 7 seeds' reef occupancy (7.2%-47.8%) shows no consistent harm or benefit, which is
exactly the null cohort-level correlation (+0.095) predicts. This is a single well-evidenced case
study built from one seed's specific hazard-layout draw, not independently replicated (no other seed
combines high occupancy with a hazard-dense draw), so it explains what happened to seed 3 without
generalizing to a claim about reefs, shelter, or safe zones more broadly.

---

## 9. Non-degeneracy / what this document is careful NOT to do

- Does not tag any claim, edit `claims.yaml`, or mint/AMEND a `substrate_queue` entry. Pure
  hypothesis-generating retrospective.
- Does not treat n=1 (or, later, n<=8) as reliability evidence.
- Does not re-propose the runner seed-count infra fix (governance's to apply).
- Does not duplicate the matched-arm causal design (`chip-20260812-causal-...`, done) -- it supplies
  that design's two missing inputs (DV set, cadence T) and stops there.
- Does not read a wakefulness/sleep-deprivation causal story into a trajectory whose dominant late-life
  driver is starvation.
- Flags residue_wanting/vigor/orienting_active as structurally dead (recording gap / flat), not as
  measured nulls.
