# Within-Life Functional-Trend Retrospective (V3-EXQ-920 Single-Continuous-Life Lineage)

**Generated:** 2026-08-14T16:16:08Z
**Chip:** `chip-20260812-exq920-multiseed-degradation-retrospective`
**Status:** LIVE analysis of the single existing n=1 trajectory + a pre-registered multi-seed
pipeline. **Nothing here is scoring evidence.** All trend readings are `n=1`,
hypothesis-generating, per the organism-review framing (Fishtank visual/single-run observations
are explicitly not treated as governance evidence). No claim is tagged, no `claims.yaml` edit is
made or implied.

This document is addendum-friendly: when V3-EXQ-920a lands (2-8 independent within-life
trajectories), a follow-on session re-runs Section 6's pipeline verbatim and appends its output as
a Section 7 addendum. It does **not** rewrite Sections 1-5.

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

Reference implementation of steps 1-4 (the exact script used for the n=1 pass) is in this chip's
scratchpad; the follow-on should re-derive it against the 920a `episode_log`s (do not depend on the
scratchpad surviving).

---

## 7. Multi-seed addendum (PENDING -- filled by the 920a follow-on)

*Awaiting V3-EXQ-920a results. To be appended by
`chip-20260814-analyse-920a-multiseed-within-life-trends` once >=2 seeds' `episode_log`s land.*

---

## 8. Non-degeneracy / what this document is careful NOT to do

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
