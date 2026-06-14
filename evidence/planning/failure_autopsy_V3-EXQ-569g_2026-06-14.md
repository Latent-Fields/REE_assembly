# Failure Autopsy -- V3-EXQ-569g (ARC-065 GAP-A route-range matched-entropy falsifier)

**Generated:** 2026-06-14T20:48:33Z
**Scope:** single (lineage member; see recurrence note)
**Status:** confirmed (user adjudicated via AskUserQuestion 2026-06-14 -- "Correct, but keep 682 running")
**Target:** `v3_exq_569g_gapa_routerange_matched_entropy_falsifier_20260611T224954Z_v3`
**Queue id:** V3-EXQ-569g - **claim_ids:** [ARC-065] - **evidence_direction:** non_contributory
**Routing:** implement-substrate (amend `modulatory-bias-selection-authority`) -- with V3-EXQ-682 in-arm diagnostic kept running as a belt-and-suspenders confirmation BEFORE the amend acts
**Supersedes (this file):** the 2026-06-14T20:14Z version of this autopsy (commit `a8fd6ae7d2`), which mis-read the manifest -- see Section 0.

---

## 0. Correction of the prior (20:14Z) autopsy -- the load-bearing fix

The first 569g autopsy (landed `a8fd6ae7d2`) concluded **"instrumentation defect, not a
ceiling -> diagnose-first, `action=none`, no substrate amend"** on the strength of one
"smoking gun":

> *"`arm_results[0/1/2].modulatory_channel_route_range_mean = 0.0` for ALL THREE
> falsifier arms (ARM_0 proposer, ARM_1 e2_world_forward, ARM_2 matched-noise)."*

**That claim is false.** `arm_results[0/1/2]` are the **three seeds (42/43/44) of
ARM_0_PROPOSER**, the collapsed-channel baseline that carries routed range ~0 **by
design** (proposer source -> no e2_world_forward divergence -> no spread). The actual
treatment arm **ARM_1_E2WF** is `arm_results[3/4/5]`:

| arm_results idx | arm | seed | `modulatory_channel_route_range_mean` |
|---|---|---|---|
| 3 | ARM_1_E2WF | 42 | **0.219136** |
| 4 | ARM_1_E2WF | 43 | **0.186431** |
| 5 | ARM_1_E2WF | 44 | **0.133989** |

Mean = **0.179852**, identical to `summary.route_range_per_arm_mean.ARM_1_E2WF` and to the
readiness probe (`arm1_route_range_mean = 0.179852`). The per-arm value is the **live
in-arm route_range** accumulated at the actual select tick
(`v3_exq_569g_..._falsifier.py:530` reads `metrics["modulatory_channel_route_range"]` each
tick into `route_ranges`; `:611` means it). There is **no probe-vs-applied divergence**:
the readiness gate and the scored ARM_1 agree at 0.18. ARM_0 and ARM_2 read 0.0 because
they are the **intended no-routing controls**, not because routing failed.

So the 20:14Z autopsy's V3-EXQ-642 "precondition-unmet / inert mechanism" framing does not
hold: **the routing/authority mechanism WAS active in the arm where the DV was scored.**
The correct reading -- and the one in the task brief -- is below.

---

## 1. The adjudicated question (corrected)

569g self-routed `r1a_entropy_only_artefact`. Is that the right reading?

**Verdict: the self-route is essentially right, but it is best read as a CONVERSION
ceiling, not an entropy-only artefact.** The routed per-candidate range **genuinely
reached the E3 selection authority** (ARM_1 applied 0.18) yet the **committed action did
not gain reliable diversity** over a temperature-matched control. This is the **same
shared structural ceiling** as `failure_autopsy_569f-661-654a` (range present, no
behavioural conversion), advanced one link: the route-range amend fixed the **reach**, and
569g now isolates the **conversion** as the residual gap.

---

## 2. Facts (no interpretation)

From the 569g manifest:

- `acceptance_criteria`: `readiness_route_range_ready=TRUE`,
  `readiness_consumed_spread_ready=TRUE`, `readiness_substrate_ready=TRUE`,
  `C1_arm1_e2_world_forward_divergent=TRUE`,
  **`C_R1B_selected_entropy_strict_above_matched_noise=FALSE`** -> `overall_pass=FALSE`.
- **In-arm applied route_range (the mechanism under test):**
  `route_range_per_arm_mean = {ARM_0_PROPOSER: 0.0, ARM_1_E2WF: 0.179852,
  ARM_2_MATCHED_NOISE: 0.0}`. ARM_1 cleared the floor on **3/3 seeds**. (ARM_0/ARM_2 are
  the no-routing controls -- 0.0 is by design.)
- `consumed_spread_per_arm_mean = {..., ARM_1_E2WF: 0.057448, ...}` (> floor 0.05) and
  `cand_world_pairwise_dist` divergent (C1 PASS): the upstream channel carries real spread.
- **Committed-action readout (the DV):** `selected_action_entropy_per_arm_mean =
  {ARM_0_PROPOSER: 0.704085, ARM_1_E2WF: 0.614972, ARM_2_MATCHED_NOISE: 0.704085}`.
  ARM_1 is **below** both controls on the mean; per-seed strict-above-both =
  **1/3** (seed 42 only: 1.0997 > 0.9722; seeds 43/44 below). `min_seeds_for_pass=2` -> FAIL.

**Smoking gun (corrected):** the routed range **reaches the authority in ARM_1 (0.18,
3/3 seeds)** but the committed-action entropy does **not** rise above the proposer / matched-
noise controls (1/3 seeds). The mechanism is active where the verdict is computed and the
verdict is still negative.

**Failed criterion:** discrimination (`C_R1B`), scored on an arm whose enabling mechanism
**is** active (route_range 0.18).

**Note on the matched-noise control:** ARM_2 (proposer @ temperature 2.5) returned
committed entropy **bit-identical to ARM_0** (proposer @ 1.0) -- 0.704085 each. The
temperature lever did not raise selected-action entropy, so the "matched-entropy" control
is weaker than intended this run. The load-bearing comparison still fails, because ARM_1 is
not reliably above the **proposer** baseline either; but a successor falsifier should verify
the noise control actually lifts entropy (else it cannot discriminate structured from
random diversity).

## 3. Why this is a conversion ceiling, not a wiring null

`project_channel_range` (e3_selector.py:61) is range-preserving, and the manifest confirms
the routed range survives into the arm (0.18). The authority block (e3_selector.py:923-944)
then does a **gap-relative additive** rescale:

```
target_range = modulatory_authority_gain * raw_score_range        # gain = 0.5
scale_factor = target_range / modulatory_range
scores       = scores_raw + scale_factor * modulatory_total
```

So the modulatory contribution is renormalized to **half** the primary score range and
**added**. Against an F-dominated primary (V3-EXQ-571: the forward-model term F is
**88-89%** of E3 score variance), a perturbation capped at `0.5 * raw_score_range` can flip
**near-ties** but not decisive winners. That is exactly the observed pattern: committed
action **moves** (V3-EXQ-662 readiness showed routing-ON vs OFF committed-class TV > floor
3/3) but does **not reliably gain diversity** over a temperature control (569g). The
conversion is **sub-threshold / non-specific**, not absent.

This also explains why the **magnitude sweeps already failed**: V3-EXQ-667 (noise_floor x
curiosity, 1x..8x) and V3-EXQ-640a (cue_recall_gain x kappa) swept **upstream** magnitudes
and were byte-identical / flat -- because the authority **range-renormalizes its input**, so
upstream magnitude is washed out. Only the **authority gain** and the **structure** of the
modulatory contribution can change the committed argmax.

## 4. Claim-layer map

`claim_ids=[ARC-065]` (architectural_commitment, **provisional**, v3_pending cleared
2026-05-31, `depends_on: []`). 569g does **not** falsify ARC-065: its diversity pathway
(SP-CEM) demonstrably produces real upstream range (consumed spread 0.057, route_range 0.18,
cand_world divergent) -- positive evidence the **source exists**. The FAIL is on
reach-to-behaviour conversion, not source existence. Result correctly **non_contributory**;
ARC-065 **unmoved**. claim_ids accurate (single claim, not inherited).

## 5. Biological-reference triage

Mechanism class: a BG-like / cortico-striatal committed-action selection gate that applies
DA-modulated **gain/contrast** to convert small representational differences into discrete
choice, competing against a forward-model-dominated primary value. **Not a formal-definition
import; no lit gap** -- the failure is gain/architecture of the selection coupling, a known
dependency of the reference mechanism, not biology divergence. No `/lit-pull` warranted.

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | ARC-065 source exists (route_range 0.18 reached authority); FAIL is on conversion, not falsification -> non_contributory |
| Biological reference | clear | BG gain/contrast selection gate; failure = under-gained / additive-subdominant conversion vs F-dominated primary; no formal import; no lit gap |
| Prerequisites | present | route-range substrate (662/663 PASS) + authority (643a PASS) landed AND active in the scored arm (ARM_1 route_range 0.18) |
| Implementation completeness | **partial -- conversion under-powered** | authority is gap-relative ADDITIVE at gain 0.5 (modrange = 0.5*raw_score_range), structurally subdominant to F (88-89% of variance, V3-EXQ-571) |
| Environment | adequate | matched-noise / proposer controls present (noise control under-lifted this run -- successor fix) |
| Measurement | adequate (load-bearing) | C_R1B scored on an arm where the mechanism IS active (route_range 0.18); the negative is real, not an artefact |
| Integration | **isolated -> partially coupled** | range reaches authority + perturbs argmax (662 TV>0) but conversion does not reliably raise committed-action diversity above a temperature control |
| Scale | adequate | not a budget/warmup issue (1/3-seed conversion + upstream-magnitude-flat 667 rule it out) |

**Recommended `epistemic_category`:** the result stays **`non_contributory`**. The shape is
a **substrate conversion ceiling** (same class as the 569f-661-654a cluster), **not**
`substrate_ceiling`-as-coarse-claim and **not** the V3-EXQ-642 precondition-unmet pattern
(that was the prior autopsy's mis-label).

## 7. Recurrence -- substrate iteration, not claim-granularity debt

This is the **6th autopsy** circling the GAP-A channel->committed-action conversion:
569c -> 569e -> 614e -> 643 -> 569f-661-654a -> 569g. The recurrence is **substrate
iteration** -- each amend fixed the next isolated link (643 dead-gate; 06-06 float32
cancellation; 06-10 route-range reach) and the falsifier re-exposed the next link -- **not**
granularity debt on a coarse claim. ARC-065 is **one** architectural commitment, not several
mechanisms. So the route is **diagnose+amend the conversion**, explicitly **not**
`/claim-synthesis`. (This overrides the manifest `evidence_direction_note`'s
`/claim-synthesis`-as-granularity-debt routing, written by failure_autopsy_batch9_2026-06-12;
the prior cluster autopsy already adjudicated this as substrate iteration.)

## 8. Learning extracted

1. **Route-range REACH is solved; CONVERSION is the residual.** The 06-10 route-range amend
   works: ARM_1 applied route_range 0.18 (3/3 seeds) at the live select tick, matching the
   readiness probe. The gap moved one link downstream -- from "range reaches the accumulator"
   to "range moves the committed argmax."
2. **The authority is additive and gain-bounded (gain 0.5), hence subdominant to the
   F-dominated primary (88-89%, V3-EXQ-571).** A `0.5 * raw_score_range`-capped additive
   perturbation flips near-ties (662 TV>0) but not decisive winners (569g entropy flat).
3. **Upstream-magnitude sweeps cannot fix this** (667/640a byte-identical) because the
   authority range-renormalizes its input. The live levers are **authority gain** and the
   **arbitration architecture**, not upstream bias magnitude.
4. **Necessary-but-not-sufficient, refined one more link:** the channel range must not only
   **reach the authority accumulator** (achieved) but **move the committed argmax against the
   F-dominated primary**, AND do so with **structure a temperature control cannot replicate**
   (the matched-noise gate). Reach without reliable, structured conversion = still a
   decorative channel at the commit layer.
5. SD-056-NaN remains disconfirmed for this lineage (C1 e2_world_forward divergent TRUE;
   V3-EXQ-617 fixed the multistep NaN). The blocker is the conversion, not the predictor.

## 9. Routing (user-confirmed: correct, but keep 682 running)

- **implement-substrate** (`action: amend` the existing `modulatory-bias-selection-authority`
  entry -- NOT create, NOT none): append the 569g failure record and refine the
  necessary-but-not-sufficient note. The amend should pursue **(a) before (b)**:
  - **(a) gain/contrast tuning (cheapest live hypothesis, try first):** sweep
    `modulatory_authority_gain` (0.5 -> 1.0 / 2.0 / 4.0) and/or replace the additive
    rescale with a contrast/normalization that lets the structured channel win near-decisive
    (not just near-tie) candidates. **Must be scored against the matched-noise control** --
    higher gain that only adds noise-like entropy (not above matched-noise) **falsifies (a)
    and promotes (b)**.
  - **(b) architectural change (pre-registered fallback the gain sweep discriminates):** a
    **shortlist-then-modulate** arbitration -- F filters to a near-tie candidate set, then the
    modulatory channel arbitrates *within* it -- so the structured channel is load-bearing
    without having to out-magnitude F.
- **Keep V3-EXQ-682 running** (the claim-free in-arm route-range collapse diagnostic already
  queued): it confirms the in-arm applied route_range and rules out any residual per-cell
  re-collapse **before** `/implement-substrate` acts. Belt-and-suspenders -- it is no longer
  load-bearing for the routing (the manifest already shows ARM_1 applies 0.18), but it
  cheaply de-risks the amend.
- **Then** a real GAP-A falsifier (V3-EXQ-569h-successor) with: an **in-arm** applied-route-
  range non-vacuity gate (assert applied route_range > floor *in the scored arm*), a
  **verified-lifting** matched-noise control, and the committed-diversity DV measured under
  the new gain/contrast or shortlist arbitration.
- **No claim demotions.** ARC-065 stays provisional / non_contributory /
  `pending_retest_after_substrate`. Cross-reference **MECH-341** (within-class temperature
  lever shares this exact conversion bottleneck), **ARC-062 / MECH-309** (rule-field channel),
  **MECH-294** (coherence channel) -- one shared conversion fix.

## Draft `evidence_quality_note` (for /governance -- do NOT write here)

> [2026-06-14 autopsy V3-EXQ-569g, CORRECTED]: 569g FAIL/non_contributory. The routed
> per-candidate range GENUINELY reached the E3 selection authority -- ARM_1_E2WF applied
> modulatory_channel_route_range = 0.18 at the live select tick on 3/3 seeds
> (route_range_per_arm_mean.ARM_1_E2WF = 0.179852, = the readiness probe; ARM_0/ARM_2 = 0.0
> are the no-routing controls by design). [Corrects the 20:14Z autopsy, which misread
> arm_results[0/1/2] -- the three SEEDS of ARM_0_PROPOSER -- as "all three arms = 0.0".]
> Yet ARM_1 committed-action entropy 0.615 is NOT strict-above proposer/matched-noise 0.704
> (1/3 seeds). So the range reaches the authority and perturbs the argmax (V3-EXQ-662 TV>0)
> but does not reliably gain committed-action diversity over a temperature control -- the
> SAME conversion ceiling as failure_autopsy_569f-661-654a, advanced one link. Cause: the
> authority is gap-relative ADDITIVE at gain 0.5 (modrange = 0.5*raw_score_range),
> subdominant to the F-dominated primary (88-89% of E3 score variance, V3-EXQ-571); upstream
> magnitude sweeps (667/640a) are washed out by the authority's range-renormalization, so
> only authority GAIN + arbitration STRUCTURE are live levers. ARC-065 unmoved
> (non_contributory; source exists, conversion is the gap). Routed to /implement-substrate
> (amend modulatory-bias-selection-authority): try (a) gain/contrast tuning first, scored
> against a verified-lifting matched-noise control; (b) shortlist-then-modulate arbitration
> as the pre-registered fallback the gain sweep discriminates. V3-EXQ-682 kept running as
> in-arm confirmation before the amend acts. xref MECH-341/ARC-062/MECH-294 (one shared
> conversion fix). NOT /claim-synthesis (substrate iteration, ARC-065 is one commitment).
