---
design_note:
  id: unified_dopamine_substrate
  title: "The unified dopamine substrate: one signed-RPE primitive, two co-equal jobs (learned selection-gating + the commit/de-commit control-plane driver)"
  registered: 2026-06-22
  last_updated: 2026-06-22
  generation: v3
  status: design_proposal
  decides: >
    The design of the single dopamine substrate the assembly map (A.4 / A.6) calls for, scoped
    to its TWO co-equal jobs: (JOB 1) the learned-gating teaching signal for selection (the
    MECH-439 attack), and (JOB 2) the dopaminergic DRIVER of the commit/maintain/de-commit
    control plane that REE built the machinery for but not the driver. Decides the minimal V3
    substrate, compose-vs-replace against the arithmetic latch (MECH-090/342/SD-034), whether the
    DA-ramp-maintenance + habenula-de-commit pair is the right fix for the parked rung-6 and
    deviation B6, the coupling to the recurrent-settling step, the two falsifiers, and the
    V4->V3 scope pull-forward.
  scope_claims: [ARC-108, ARC-109, MECH-450, ARC-107, MECH-439, MECH-448, MECH-449, MECH-090, MECH-342, MECH-320, ARC-068, ARC-016, MECH-445, MECH-446, MECH-203]
  references_claims: [ARC-108, ARC-109, MECH-450]   # already registered (assembly-map E.2 intake-reap); this note MINTS NOTHING
  derived_from: >
    basal_ganglia_assembly_map_2026-06-22.md (A.4 the learning gap; A.6 the dopaminergic
    control-layer biology check + its two implications; B5/B6 divergences; C1/C3 the
    recurrent-settling repair; D loop segregation; E next-steps);
    dopamine_into_gating_design_2026-06-22.md (the JOB-1 selection-learning mechanism in full);
    arc_107_selector_constitution_design_2026-06-20.md (s3 constitution, s6b completeness ledger +
    V4-axes); grounded against ree-v3/ree_core/predictors/e3_selector.py + ree_core/agent.py
    (the bistable commit latch + closure de-commit site).
  cross_plan_home: [basal_ganglia_assembly_map, conversion_ceiling_campaign, commitment_closure, biology_grounding_convergence_v4]
  promotes_nothing: true
---

# The unified dopamine substrate: one primitive, two co-equal jobs

**What this is.** The umbrella design note the assembly map A.6 (implication 1)
calls for: the single dopamine substrate whose absence is the root of *two*
otherwise-separate problem areas. Before the 2026-06-22 A.6 biology check the
substrate was framed as one thing -- the learned-gating teaching signal for
*selection* (the MECH-439 attack, designed in full in the companion
[`dopamine_into_gating_design_2026-06-22.md`](dopamine_into_gating_design_2026-06-22.md)).
The A.6 lit check established a **second, co-equal job**: the same dopamine
substrate is the missing *driver* of the commit/maintain/de-commit **control
plane** -- the part REE built the machinery for (the beta-gate latch, the SD-034
closure operator, the refractory) but never gave its neuromodulator. This note is
the design-of-record for **ARC-108** (already registered): it states the one
shared primitive, develops JOB 2 in full (JOB 1 is deferred to the companion
note), and makes the five decisions the assembly map E.3 asks for.

**Relationship to the JOB-1 note (no duplication).** The companion
`dopamine_into_gating_design_2026-06-22.md` is the deep tactical design for JOB 1
(the learned per-channel selection weight `w_chan`, the three-factor update, the
2x2 selection falsifier). This note **subsumes** it at the substrate level: it
shows that JOB 1 and JOB 2 run off the *same* signed-RPE primitive, and it adds
the JOB-2 control-plane design that the companion note does not cover. Where JOB-1
mechanism detail is needed, this note points there rather than restating it.

**The decision (headline).** **Build one dopamine substrate emitting a small set
of shared signals -- a signed phasic RPE delta_t, a tonic baseline V-hat, and a
goal-proximity value ramp rho_t -- and drive BOTH jobs from it. Instantiate the
selection-learning job first (it is where MECH-439 is live and the cleanest test),
then the maintenance-ramp + habenula-de-commit pair of the control plane (the
concrete candidate fix for the just-built, now-dissociable rung-6 substrate).
COMPOSE with the existing latch/closure machinery -- keep it as the safety-bearing
plumbing -- REPLACING only the flat-hold maintenance *driver* and ADDING the
habenula negative-RPE *abort input*. Pull the minimal slice of all this forward to
V3; keep the population split (ARC-109), the routed habenula efferent, the
tonic/phasic gate refinements, and the full loop at V4.** PROMOTES NOTHING; mints
no claim (ARC-108/ARC-109/MECH-450 are already registered).

---

## 1. The one primitive that serves both jobs

The assembly map A.6 finding, restated: in the brain dopamine drives *all four
phases* of action commitment, and the *same* dopaminergic machinery also supplies
the three-factor teaching signal that learns selection. REE has neither -- the
arbitration layer is pure arithmetic (A.4) and the control plane runs off
hand-specified readiness arithmetic (`running_variance`, score margin,
nav-competence, rule-state stability) with no dopaminergic driver (A.6). One
substrate closes both gaps.

**The substrate emits three signals, all formed from quantities REE already has:**

| Signal | Type | Formed from (no new substrate) | Drives |
|---|---|---|---|
| **delta_t** (phasic RPE) | **signed** scalar (better/worse than expected) | `R_t - V-hat_t`; `R_t` = realised outcome valence of the committed action via the *already-trained* valuation heads; `V-hat_t` = slow EMA baseline | JOB 1 learning (`w_chan`, `W_lat`); JOB 2 go-signal (positive burst) + de-commit (negative = habenula) |
| **V-hat_t** (tonic baseline) | unsigned slow average | the same leaky-integrator EMA of `R` (the average-reward-rate / opportunity-cost term, Niv 2007) | JOB 2 commit-threshold (high reward rate -> commit more readily); the reference the ramp departs from |
| **rho_t** (proximity ramp) | unsigned ramp, peaks-then-declines | a goal-proximity x value estimate (reuse the goal/benefit valuation already feeding F) scaled toward the active goal | JOB 2 maintenance (sustains the commit while approaching; self-limits at proximity peak) |

**The load-bearing distinction (divergence B5).** `delta_t` is a **signed** scalar
and is explicitly **NOT** the unsigned prediction-error *variance* ARC-016 already
computes (`e3._running_variance`). An unsigned magnitude cannot tell "raise this
channel / hold this commit" from "lower it / abort this commit" -- it has no sign,
so it can drive neither the D1-up/D2-down learning asymmetry (JOB 1) nor the
go-vs-abort polarity of the control plane (JOB 2). ARC-016 stays as the precision /
commit-threshold-sharpening signal it already is; this substrate adds the directional
RPE next to it. (This is the silent-divergence row B5 the assembly map E.1 enters
into the ARC-106 ledger; it is now load-bearing for *both* jobs.)

---

## 2. JOB 1 -- learned selection-gating (summary; full design in the companion note)

The MECH-439 attack. F monopolises 88-89% of committed-selection variance
(V3-EXQ-571) because the arbitration layer has **no learned parameters** -- every
diversity channel is a fixed-magnitude bias competing against a fixed primary
score (A.4). The fix: `delta_t` drives a learned per-channel selection-weight
vector `w_chan` over the modulatory channels (and, coupled, the lateral-inhibition
weights `W_lat` of the settling step, sec 5), via a three-factor (Hebbian
co-activation x signed RPE) eligibility-trace update with a D1-LTP/D2-LTD-analog
asymmetric gain. It **composes** inside the F-bounded MECH-448/449 eligibility
frame (safety inherited; a learned weight can never re-admit a No-Go-suppressed
candidate).

**Full mechanism, the no-op-default contract, and the 2x2 selection falsifier are
in [`dopamine_into_gating_design_2026-06-22.md`](dopamine_into_gating_design_2026-06-22.md)**
(sec 2-5). This note does not restate them. The only thing to carry forward here is
that JOB 1's `delta_t` *is* the same `delta_t` the control plane uses -- that is the
whole content of "one substrate, two jobs."

---

## 3. JOB 2 -- the dopaminergic control-plane driver (the new content)

REE built the commit/maintain/release *machinery* and ran it off arithmetic
readiness signals. The A.6 table maps each of the four control-plane phases to its
dopaminergic driver and to what REE has. Here is the design that supplies each
driver from the sec 1 substrate:

| Control-plane phase | Biology's driver | REE today | This note's driver |
|---|---|---|---|
| **(a) Commit threshold / readiness** | **tonic DA = average reward rate = opportunity cost of time** (Niv 2007; Zenon 2016) | beta-gate opens on `running_variance < threshold` + the MECH-090 R-c conjunction; MECH-320 vigor is a score-bias; ARC-068 opp-cost unbuilt | **V-hat_t modulates the commit threshold**: high tonic reward rate (high opportunity cost of dithering) lowers the readiness threshold -> commit faster; low rate raises it -> deliberate. Reuses the same EMA baseline `delta_t` already needs. |
| **(b) Commit go / gate-open** | **phasic DA "locks the gate to working memory"** (Gruber 2006; PBWM) | the beta-gate opens on the arithmetic conjunction; no DA go-signal | **a phasic positive delta_t at selection gates the commit** -- the burst that "locks" the chosen program into the maintained state, supplementing (not replacing) the R-c conjunction. |
| **(c) Commitment maintenance** | **DA ramp scaled to goal proximity x value** (Howe 2013; Mohebi 2019) -- peaks-then-declines, so it *cannot* monopolise | a **flat bistable latch + refractory + rung-6 occupancy lever** -- flat, not proximity-scaled; this is **deviation B6 / the 460h ~2400-step monolithic hold** | **rho_t (the proximity ramp) sets the hold strength/duration**: maintenance ramps up while approaching the goal and *declines past the proximity peak*, so the hold self-limits instead of running 2400 steps. |
| **(d) De-commit / abort** | **lateral habenula -> RMTg -> DA inhibition = negative RPE** (Matsumoto 2007; Hong 2011; Sosa 2021) | the entire de-commit side (MECH-342, SD-034 closure, the 460d-j lineage, the parked rung-6) is built with **refractory timers and NO negative-RPE driver** | **a negative delta_t (the habenula analog) is a new abort input to the SD-034 closure operator** -- de-commit fires on "worse than expected," content-driven, dissociable from the commit's own latch state. |

The economy of the design: phases (a)+(b) need only the `V-hat_t` and `delta_t`
the substrate already produces for JOB 1; phase (c) needs the one new ramp `rho_t`;
phase (d) needs only the *sign* of `delta_t` (negative = abort). The control plane
costs almost nothing beyond the selection substrate -- which is exactly the A.6
implication-1 point that one missing piece sits upstream of both problem areas.

---

## 4. Compose vs replace the arithmetic latch machinery (decision 2)

**Decision: COMPOSE the machinery; REPLACE only the maintenance *driver*; ADD the
de-commit *driver*.** This mirrors JOB 1's compose-not-replace logic (safety lives
in the existing structure; dopamine drives *within* it) and is deliberately more
surgical than a wholesale swap.

- **Keep as safety-bearing plumbing (compose):** the MECH-090 bistable beta-gate
  (the gate that holds), the SD-034 closure operator (the operator that executes a
  release), MECH-342, and the refractory. These are the commit/release *mechanism*.
  A dopaminergic driver must never be able to (i) hold a harmful commitment open or
  (ii) release a safety-critical commit improperly -- the gate and operator remain
  the arbiters of *whether* a hold/release is permitted. Dopamine decides *how
  strongly* and *when*, inside that envelope.
- **Replace the maintenance *driver* (the one targeted replacement):** the flat
  bistable hold-duration term is replaced by `rho_t`. The latch still gates the
  commit; the ramp decides how long and how strongly it is held. This is the B6
  fix -- a flat hold has no intrinsic decay (it can monopolise for 2400 steps); a
  proximity-scaled ramp peaks-then-declines and therefore self-limits. The
  rung-6 occupancy lever (the hand-built attempt to stop the monopoly) becomes
  unnecessary once maintenance has its native ramp.
- **Add the de-commit *driver* (new input, not a replacement):** the habenula
  negative-RPE becomes a new abort input to the SD-034 closure operator, alongside
  the existing refractory-timer release. The operator still executes the release;
  the habenula tells it *when* (outcome worse than expected) -- the content-driven
  trigger the refractory clock never had.

Replacing the machinery wholesale was rejected for the same reason as in JOB 1: it
would discard the only landed, safety-bearing commit/release components and re-open
a safety surface the dopaminergic driver cannot itself guarantee. The arithmetic
readiness gates (`running_variance`, R-c) are likewise **kept and modulated**, not
deleted -- `V-hat_t` shifts the threshold; it does not remove the conjunction.

---

## 5. Coupling to the recurrent-settling step (decision 4)

The assembly map (C1, C3, A.5) argues that learned gating and a recurrent-settling
competition are coupled -- in biology the lateral-inhibition weights that run the
settling competition are *themselves* learned. This note adds the symmetric point
for the control plane: **selection-settling and maintenance-ramp are the two faces
of the same move -- "add dopamine-driven temporal dynamics where REE has stateless
arithmetic," both off the one substrate.**

- **Selection side (MECH-450, already registered):** the minimal recurrent settling
  step -- a few rounds of mutual inhibition over the eligible set before commit --
  whose lateral-inhibition weights `W_lat` are learned by the **same** `delta_t` as
  `w_chan` (companion note sec 4). Fixes B1 (one-shot argmin -> settling) + B3-blend
  (additive `_modulatory_accum` -> competitive winner-take-most).
- **Maintenance side (this note, sec 3c):** the proximity ramp `rho_t` is the
  *temporal* recurrence of the **hold** phase -- a stateful, declining drive
  replacing a flat latch, exactly as the settling step is the stateful competition
  replacing a one-shot argmin.

Both replace a stateless, hard, hand-specified operation with a stateful,
dopamine-parametrised one. They share `delta_t` / `V-hat_t`; build the selection
settling first (it is the live MECH-439 face), then the maintenance ramp.

---

## 6. Is the DA-ramp + habenula pair the right fix for rung-6 and B6? (decision 3)

**Verdict: yes -- it is the right fix, and the timing is now exactly right to test
it. Pre-register the falsifier (sec 7.2) rather than assume it.**

The argument (assembly map A.6 implication 2): the 460d-j lineage (~10 iterations),
the parked rung-6, and deviation B6 (the 460h monolithic ~2400-step hold) are the
**same missing piece seen from two ends** -- maintenance-and-release driven by a
fixed latch instead of a dopaminergic ramp+habenula pair.

- **B6 (the hold monopolises) is structurally predicted by a *flat* latch.** A flat
  hold has no intrinsic decay term, so nothing stops it running 2400 steps; every
  other channel drowns. A proximity-scaled ramp peaks-then-declines by
  construction, so it *cannot* monopolise. This is a **structural** fix, not another
  parameter tune -- and the whole campaign's lesson (assembly map C1) is exactly
  that "structural bounding works, parametric tuning does not." Ten iterations of
  refractory/latch-hold engineering are hand-emulating, badly, what one ramp does
  natively.
- **rung-6 (de-commit has no authority / is non-dissociable) is predicted by a
  de-commit built *without its teaching signal*.** A refractory timer fires on a
  clock, not on outcome content; it cannot be dissociated from the commit it is
  releasing because it has no independent trigger. A habenula negative-RPE gives
  de-commit a **content-driven** trigger (fires on outcome valence, not on the
  latch's own state) -- dissociable by construction. That is precisely the property
  the rung-6 retests kept failing to produce by timer engineering.
- **The substrate to test it on was just built.** The rung-6 PARK (2026-06-22) was
  resolved the same day by building the **closure-exclusive de-commit eval mode**
  (`closure_exclusive_decommit_eval`, ree-v3 `e52158d`), which makes natural-commit
  occupancy dissociable from closure-de-commit -- and 460k is the queued validation
  successor. **The habenula negative-RPE is the *driver* that the now-dissociable
  de-commit substrate was built to receive.** The A.6 recommendation and the
  just-completed rung-6 BUILD converge: substrate built, driver is the natural next
  thing to add. This is the strongest reason to pull the maintenance-ramp +
  habenula pair forward to V3 (sec 8) rather than wait for V4.

**Caveat (why it is a falsifier, not a fact).** It remains possible that the flat
latch is *not* the binding constraint -- e.g. the monopoly could be driven upstream
of maintenance, in selection (the F-dominated commit chooses the same program
repeatedly regardless of hold dynamics). The sec 7.2 falsifier is designed to
separate "the ramp releases where the flat latch monopolises" from "the monopoly
persists because selection, not maintenance, is the constraint" -- and the latter
routes back to JOB 1, not to a false weakening of the control-plane claim.

---

## 7. Pre-registered falsifiers (decision 5)

Two falsifiers, one per job. They are independent: JOB 1 can convert while JOB 2
does not, or vice versa.

### 7.1 JOB 1 -- learned gating converts where the arithmetic envelope plateaus

This is the companion note's 2x2 (learned-`w_chan` x learned-`W_lat`) selection
falsifier on the GAP-A divergent pool; see
[`dopamine_into_gating_design_2026-06-22.md`](dopamine_into_gating_design_2026-06-22.md)
sec 5 for the full design. **Summary of the discriminator:** committed-action-class
entropy must rise with learning, strict-above BOTH a matched-noise control AND the
envelope-only arm, **growing over training** (a static lift is not learning), with
the **signed RPE load-bearing** -- an ablation arm swapping signed `delta_t` for the
unsigned ARC-016 variance must fail to convert (falsifies B5-collapse). Preconditions-met
no-lift escalates to the V4 full loop; it does not falsely weaken ARC-107.

### 7.2 JOB 2 -- ramp-maintenance releases where the flat latch monopolises

The new falsifier this note pre-registers. **Substrate:** the just-built
closure-exclusive dissociable regime (`closure_exclusive_decommit_eval=True`,
ree-v3 `e52158d`), the same substrate the 460k rung-6 validation runs on -- so
natural-commit occupancy is dissociable from closure-de-commit and the hold
dynamics are observable in isolation.

**Arms (3 seeds):**

| Arm | maintenance driver | de-commit driver |
|---|---|---|
| L0 (flat-latch control) | flat bistable hold (current) | refractory timer only (current) |
| L1 | **rho_t proximity ramp** | refractory timer only |
| L2 | rho_t proximity ramp | **+ habenula negative-delta_t abort** |

**Primary acceptance (the discriminator):**

- **D1 (the ramp self-limits where the flat latch monopolises):** L0 reproduces the
  monolithic-hold signature (a long single occupancy, low de-commit count -- the
  B6/460h shape); L1's hold-duration distribution **peaks-then-declines with
  proximity** (bounded occupancy, no single hold monopolising), and
  committed-action-class diversity over the run rises strict-above L0 on >=2/3 seeds
  *because* no hold monopolises.
- **D2 (the release is content-driven, not a re-parameterised timer -- the core
  discriminator):** the L1/L2 release must **correlate with goal-proximity / `rho_t`
  decline (L1) or with negative `delta_t` (L2)**, not merely occur sooner. A flat
  hold with a shorter fixed duration would also release sooner -- that is *not* the
  claim. The claim is *proximity-scaled self-limiting* (L1) and *negative-RPE-triggered
  abort* (L2). If the only effect is "releases sooner on a clock," the ramp is a
  re-parameterised timer and the mechanism collapses back to the latch family --
  route back to the refractory lever, do not mint.
- **D3 (habenula de-commit is dissociable):** in L2 the negative-`delta_t` aborts
  must fire on **outcome valence** dissociably from the commit latch state (de-commit
  events whose timing tracks `delta_t < 0`, not the latch's refractory phase) -- the
  exact dissociation the rung-6 lineage could not produce with timers.

**Non-vacuity / self-route (never a false weakening):** `substrate_not_ready_requeue`
(NOT a control-plane weakening) if `rho_t` carries no proximity variance to ramp on,
or `delta_t` carries no negative-outcome variance to abort on, or the dissociable
eval mode does not arm (the 460k `ncl_hold_closure_armed_total ~ 0` guard). A
**preconditions-met no-release** (ramp varies, habenula has negative variance, hold
still monopolises) is the genuine "maintenance is not the binding constraint"
outcome -> route to JOB 1 / selection (the F-dominated commit re-chooses the same
program regardless of hold dynamics, sec 6 caveat), NOT a falsification of the
ramp+habenula design.

---

## 8. The V4 -> V3 scope decision (flagged for ratification)

**The scope question, stated plainly.** ARC-107 sec 6b parks "Dopaminergic RPE
learning signal" and "Vigor / opportunity-cost" as **V4 bets**, and ARC-108 is
registered at `implementation_phase: v4` per that stated bet. The assembly map
(A.5 / C1 / C2) and the companion JOB-1 note **recommend pulling the minimal slice
forward to V3**. This note makes the recommendation explicit and precise about
*what moves* and *what stays*, and flags it as a decision for the user / governance
to ratify -- ARC-108 stays `v4` until then.

**Recommended pull-forward (the V3-minimal slice):**

| Piece | Recommendation | Why now |
|---|---|---|
| signed `delta_t` + tonic `V-hat_t` (the shared primitive) | **V3** | the substrate both jobs need; formed from existing valuation heads, no new encoder |
| JOB 1 selection learning (`w_chan`) | **V3** | MECH-439 is the live root; companion note already designed it; MECH-450 (the coupled settling step) is already registered `v3` |
| JOB 2 maintenance ramp `rho_t` + habenula negative-`delta_t` de-commit (the **pair**) | **V3** | the concrete candidate fix for the parked rung-6 / B6, and the dissociable substrate it tests on was **just built** (`e52158d`); testing it is the natural next step after the 2026-06-22 build, not a V4 deferral (sec 6) |

**Stays V4 (named, falsifiable cuts -- ARC-106 zero-silent-divergence):**

| Deferred piece | Why V4 | Bet to register |
|---|---|---|
| **D1/D2 population split** (ARC-109) | the minimal rule renders the asymmetry as a single asymmetric-gain parameter; two opponent populations are required only to *earn* the Parkinson/dyskinesia/Huntington/ICD axis (ARC-106 EARNS) | "V3 renders D1/D2 asymmetry as a single asymmetric-gain weight; the opponent-population split is V4 and is what earns the disease axis." |
| **Lateral-habenula as a routed efferent drain** (A.3) | the minimal de-commit driver is an *internal* negative-`delta_t` scalar, not a routed GPi->habenula output channel | "V3 forms the habenula signal as an internal negative-RPE scalar; the habenula negative-RPE *output drain* is V4." |
| **tonic->threshold (a) and phasic->go (b) refinements** | the current arithmetic readiness gates (`running_variance`, R-c) *work* -- they are not the live failure; modulating them with `V-hat_t`/`delta_t` is a refinement, lower leverage than the maintenance/de-commit pair | "V3 keeps the arithmetic commit-threshold and go-conjunction; tonic-DA threshold modulation and the phasic-DA go-gate are V4 refinements." |
| **full thalamo-cortical recurrent loop; loop segregation; ACh/TAN plasticity-window** | V3 has no thalamus module / one collapsed arena / a plain eligibility trace | (as in the companion note sec 6 and assembly map D) -- pulled forward only if the sec 7 falsifiers leave MECH-439 unresolved. |

**The bet's escape hatch is the sec 7 falsifiers.** If JOB 1 returns
preconditions-met no-lift, the single collapsed arena (loop segregation, assembly
map D) is pulled forward. If JOB 2 returns preconditions-met no-release, selection
(JOB 1), not maintenance, is the binding constraint. We pre-commit to the
falsifiers that decide whether V4 is needed, not to V4 itself.

---

## 9. Disposition summary

| Question | Decision |
|---|---|
| (1) minimal V3 substrate + which function first | one substrate emitting **signed `delta_t`** (R - EMA baseline, reusing trained valuation heads; distinct from ARC-016 unsigned variance, B5) + tonic **`V-hat_t`** + proximity ramp **`rho_t`**. **Selection learning instantiated first** (live MECH-439 root, cleanest test); then the maintenance-ramp + habenula-de-commit pair. |
| (2) control-plane driver: compose vs replace the latch (MECH-090/342/SD-034) | **COMPOSE the machinery** (keep gate + closure operator + refractory as safety plumbing); **REPLACE only the flat-hold maintenance *driver*** with `rho_t`; **ADD the habenula negative-`delta_t` as a new abort input** to the SD-034 operator. Arithmetic readiness gates kept and modulated, not deleted. |
| (3) is DA-ramp + habenula the right fix for rung-6 + B6? | **Yes** -- B6 monopoly is structurally predicted by a *flat* latch (a ramp peaks-then-declines, cannot monopolise); rung-6 non-dissociability is predicted by a de-commit built without a content-driven trigger (habenula negative-RPE supplies it). The dissociable substrate it tests on (`e52158d`) was **just built**; timing converges. Falsify (sec 7.2), do not assume. |
| (4) coupling to the settling step | **COUPLED** -- selection-settling (`W_lat`, MECH-450) and maintenance-ramp (`rho_t`) are the two faces of "dopamine-driven temporal dynamics replacing stateless arithmetic," off the one substrate; both learned by the same `delta_t`. |
| (5) falsifiers | **two**: (7.1) selection -- learned gating converts-where-arithmetic-plateaus, growing-with-training, signed-RPE load-bearing (companion note 2x2); (7.2) control-plane -- ramp-releases-where-flat-latch-monopolises on the `e52158d` dissociable substrate, with release **content-driven not re-parameterised-timer** as the core discriminator, habenula de-commit dissociable, preconditions-met no-release routes to JOB 1 not a false weakening. |
| scope | **Pull the V3-minimal slice forward** (shared primitive + JOB 1 `w_chan` + the JOB 2 ramp+habenula pair); keep ARC-109 D1/D2 split, the routed habenula efferent, the tonic/phasic gate refinements, and the full loop at **V4** as named cuts. **ARC-108 stays `v4` until the user/governance ratifies the pull-forward** -- flagged here for that decision. |

---

## 10. Next steps (governance)

1. **Ratify the V3 scope pull-forward (sec 8)** -- a user/governance decision.
   ARC-108 is registered `implementation_phase: v4`; the recommendation is to carve
   the V3-minimal slice (shared primitive + JOB 1 selection learning + the JOB 2
   maintenance-ramp + habenula-de-commit pair) and re-scope ARC-108's V3-relevant
   portion accordingly, keeping the population split / routed efferent / full loop
   at v4. No claims.yaml change is made by this note.
2. **Build JOB 1 first** via `/implement-substrate` (companion note sec 8): `w_chan`
   + `delta_t`, no-op-default, then the learned-`W_lat` settling step (MECH-450).
3. **Build the JOB 2 pair** via `/implement-substrate` after JOB 1's `delta_t` lands:
   `rho_t` proximity ramp as the maintenance driver (modulating the MECH-090 latch
   hold) + the habenula negative-`delta_t` abort input to the SD-034 closure
   operator, both no-op-default, on the `closure_exclusive_decommit_eval` substrate.
4. **Falsify** via `/queue-experiment`: the sec 7.1 selection 2x2 and the sec 7.2
   control-plane L0/L1/L2 falsifier (the latter as a 460-lineage successor on the
   dissociable substrate, claim_ids referencing MECH-090/MECH-342/MECH-445/MECH-446
   and the control-plane portion of ARC-108).
5. **Enter the silent divergence rows** B5 (RPE-as-unsigned-variance, now load-bearing
   for both jobs) and B6 (global flat latch, now the explicit B6 maintenance fix)
   into the ARC-106 sec 5 living ledger (assembly map E.1).
6. **Hold** ARC-109 (D1/D2 split), the routed habenula efferent, the tonic/phasic
   gate refinements, the full thalamo-cortical loop, and loop segregation (assembly
   map D) as the sec 8 V4 bets unless the sec 7 falsifiers leave MECH-439 / the
   control-plane monopoly unresolved.

---

*Companion to `basal_ganglia_assembly_map_2026-06-22.md` (A.4 the learning gap;
A.6 the dopaminergic control-layer biology check + its two implications; B5/B6
divergences; C1/C3 the settling repair; D loop segregation; E next-steps),
`dopamine_into_gating_design_2026-06-22.md` (the JOB-1 selection-learning mechanism
in full), and `arc_107_selector_constitution_design_2026-06-20.md` (sec 6b
completeness ledger + V4-axes). Design-of-record for ARC-108 (already registered);
references ARC-109 + MECH-450. Grounded against
`ree-v3/ree_core/predictors/e3_selector.py` + `ree_core/agent.py`. PROMOTES
NOTHING; mints no claim.*
