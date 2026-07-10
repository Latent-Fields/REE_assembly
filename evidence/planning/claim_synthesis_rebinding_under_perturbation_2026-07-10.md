# Claim-synthesis proposal — rebinding-under-perturbation (V3-EXQ-725a salvage)

- **Generated:** 2026-07-10T07:47:25Z
- **Skill:** `/claim-synthesis` (proposal-first; nothing lands in claims.yaml without per-child user approval)
- **Entry point:** DIRECT NOMINATION — the one salvageable positive routed out of
  `failure_autopsy_V3-EXQ-725a_2026-07-10.{md,json}` §8, **decoupled** from the closed
  coherence-nonreducibility Q.
- **bears_on:** MECH-269 (proposer anchor selection / anchor-reset), MECH-270 (ephaptic
  verisimilitude readout), INV-002 (coherence includes temporal/phase binding), ARC-006
  (entities are bindable/persistent), MECH-045 (object-file persistence).
- **Substrate:** ALREADY BUILT + CONVERGED — `ree-v3/ree_core/latent/cross_stream_binder.py`
  (learned mode), `rebinding_probe()`. No `/implement-substrate` owed.

---

## 0. What is NOT in scope (the closed Q)

The coherence-**specificity** question — does a coherence term `C(τ)` change binding
selection **coherence-specifically** vs a contrast-matched shuffle — is **settled NO-CLAIM**
by 725a (SPEC 1/6, gate 4/6; the divergence is reproduced by a contrast-matched shuffle;
formal-import caution vindicated). Both 2026-04-23 intakes settle no-claim on the candidate Q
`entities/selection.coherence_nonreducibility` via the next `/governance` walk. **This
proposal does not re-open that.** A different-mechanism redesign with a non-saturating
divergence metric is separately sanctioned but is not this task.

This proposal concerns ONLY the decoupled positive: **rebinding-under-perturbation**.

---

## 1. The salvaged observation (facts)

`rebinding_probe(z_self, z_world_candidates, perturbation)` perturbs the **shared anchor**
`z_self` and asks whether the argmax binding-affinity world-config **flips** — i.e. whether a
competing configuration overtakes the currently-bound one. In V3-EXQ-725a (converged learned
binder):

- `n_rebind_total = 1676` across 6 seeds; **`rebinding_exercised` = PASS** (non-degenerate).
- **0 in every predecessor** (641/641a/720 fixed field: `binding_score ≡ 0`, undiscriminating;
  725 learned-but-unconverged: vacuous).
- Load-bearing because the perturbation is on the **anchor**, not the candidates: a bilinear
  `binding_score` shifts every candidate by the same constant under a candidate-uniform
  perturbation (can never flip the argmax); an anchor perturbation gives a **per-candidate**
  shift `⟨W_self·p, φ_world(c)⟩` that varies with `c`, so a competitor CAN overtake.

This is the binding intake's own candidate MECH (`thought_intake_2026-04-23_binding.md` §4):
*"the system must monitor coherence and rebind when a competing configuration overtakes the
current one in `exp(-βE)·C`."*

---

## 2. Discrimination gate (the load-bearing filter)

Two findings decide the disposition.

### 2a. What `n_rebind=1676` licenses is EXERCISABILITY, not FUNCTION

The `rebinding_exercised` criterion confirms the learned bilinear scorer is **non-degenerate
and anchor-sensitive** — a competitor *can* overtake under anchor perturbation. That is a
genuine `0 → exercisable` substrate transition (real, and absent in every predecessor). But
it is **not** a demonstration that rebinding does cognitive/behavioural work, tracks a genuine
environmental competing-configuration overtake, or improves any downstream outcome. "The
argmax flips when you perturb the anchor" is close to **guaranteed** for any trained
non-degenerate bilinear scorer over a pool of similar candidates — it is an exercisability /
non-degeneracy signal.

Under the skill's Step-3 gate, an exercisability signal routes to a **test** (or, if the
substrate were absent, to `/implement-substrate`) — **not** by itself to a new `shown`-track
claim.

### 2b. The registry has ALREADY learned this exact lesson at the sibling locus

**MECH-269(b) anchor-reset IS a registered rebinding mechanism** (mark_inactive + seek_new_anchor
when effective verisimilitude `V_s_anchor = V_s − staleness` falls below `θ_reset` for k steps).
Its own validation runs are directly precedential:

> V3-EXQ-478/480: *"anchor resets fire abundantly (63/31 per seed) and staleness peaks ~0.94/0.83,
> but `freeze_recommit_count` is bit-identical OFF=ON … both runs tagged inconclusive."*
> V3-EXQ-481: *"`vs_commit_release_count=0` in both ON and OFF arms — the release path is dead code."*
> V3-EXQ-476c: *"V_s observables do not convert to behaviour without the MECH-284 consumer."*

So **abundant rebinding events with no behavioural consequence = inconclusive, not weighted**.
Minting a new `shown`-eligible claim whose sole novel support is `n_rebind > 0` would repeat,
at the entity-binding locus, precisely the evidence type the registry has already found does
not lift a claim.

### 2c. Gate verdict

- The **content** the intake MECH asserts ("monitor **coherence** and rebind … in `exp(-βE)·C`")
  bundles the coherence-specific selection factor that **725a refuted**. Registering it verbatim
  would smuggle the settled null back in. Any registerable child must be **stripped** of the
  coherence-specificity content.
- The **residual honest content** — *entity-level self↔world-config binding is anchor-sensitive
  and a competitor can overtake it under perturbation* — is real, exercisable, biologically
  grounded (§3), but currently supported only at the **exercisability** tier, and sits adjacent
  to the already-registered MECH-269(b) at a different locus.

→ **This is NOT `shown`-track granularity debt.** It is a **candidate-tier** hypothesis: a
substrate-conditional claim whose promotion is owed a **functional** test, registerable only if
(a) stripped of coherence-specificity and (b) carrying a `what_would_answer` that the MECH-269
inert-reset precedent could not vacuously pass.

---

## 3. Lit grounding (Step 5 — commissioned this run)

The mechanism *dynamic rebinding under perturbation* has **genuine, non-formal-import
biological warrant**, distinct from the path-integral `C(τ)` import that 725a settled:

- **Object-file updating / reviewing** — object continuity is actively maintained and
  **re-linked** across time and perceptual gaps; correspondence can be reassigned (Kahneman,
  Treisman & Gibbs 1992, *Cog Psych*, 2068 cites; Sasi et al. 2022, *J Vision* — reliable
  object-file-updating paradigm). This is the canonical basis for entity-level rebinding.
- **Serial-dependence / illusory stability** — an active online mechanism biases the current
  percept toward the recent past (hysteresis), the **stability counterweight** rebinding must
  overcome (Manassi & Whitney 2022, *Science Advances*, 72 cites). Directly motivates a
  *hysteresis/threshold* on rebinding rather than chatter.
- **Prediction-error-driven switching** — bistable perception switches when residual
  prediction-error for the suppressed percept accumulates (Weilnhammer et al. 2017, *PLoS Comp
  Biol*, 102 cites); ACC prediction-error causally drives single-trial task/state switching
  (Cole et al. 2024, *Nat Commun*, 30 cites). This is the *"competitor overtakes when the
  current config accrues error"* trigger, mechanistically — **not** a coherence-specific factor.
- Latent-cause inference (Gershman 2010/2017, already cited under MECH-269) supplies the
  formal "switch to a new cause when the current one stops explaining the data" account.

**Verdict:** the biology supports rebinding as a real, distinct, dynamic mechanism — and it
grounds it in **prediction-error-driven switching + object-file updating + hysteresis**, i.e.
**exactly the `E(τ)` / stability machinery, NOT the coherence-`C(τ)` factor that failed.**
This *strengthens* the decoupling: rebinding stands on its own biology and does not inherit the
formal-import caution.

---

## 4. Proposal — ONE candidate child (recommended), + evidence-note hygiene

### 4a. RECOMMENDED — register MECH-456 (id "next free at registration time")

| Field | Value |
|---|---|
| **id** | MECH-456 (verify max at write time; 455 is current max) |
| **claim_type** | `mechanism_hypothesis` |
| **subject** | `entities.rebinding_under_perturbation` |
| **status** | `candidate` |
| **epistemic_category** | `substrate_conditional` (substrate built + converged; functional validation owed) |
| **implementation_phase** | v3 · **v3_pending: true** |
| **claim_level** | mechanistic |
| **polarity** | asserts |
| **depends_on** | ARC-006, INV-002, MECH-045, MECH-269 (sibling anchor-reset at a different locus), MECH-270 |

**One-line claim.** *An established entity binding (self-anchor ↔ world-configuration) is not
fixed but continuously re-evaluated: when a competing configuration overtakes the currently-bound
one under perturbation of the shared anchor, the binder re-binds to the competitor. Rebinding is
the entity-layer analogue of MECH-269(b) anchor-reset, operating over self↔world-config bindings
rather than proposer stream-anchors.*

**Explicitly stripped of** the coherence-specificity factor `C(τ)` (settled NO-CLAIM in 725a).
The rebinding trigger is prediction-error / competitor-overtake driven (§3 biology), not a
coherence-specific selection term.

**`what_would_answer` (FUNCTIONAL — cannot be passed by exercisability alone).**
> A V3 experiment on the converged learned `cross_stream_binder` in which the environment
> presents a genuine competing-configuration overtake (the world-config that best matches the
> agent's realized situation changes mid-episode) must show BOTH: (1) the binder re-binds to the
> newly-correct configuration (rebinding tracks the *true* competitor, not arbitrary anchor
> noise — measured by rebinding-alignment-with-ground-truth above a shuffle control), AND (2) a
> **behavioural / competence consequence** — rebinding-ON produces a downstream outcome
> difference (e.g. faster re-acquisition, fewer stale-binding errors) vs a rebinding-frozen arm,
> using a **graded, non-saturating** metric (per the 725a `frac_state_div` saturation note).
> **Unsupported if** rebinding events fire but are bit-identical OFF=ON on the behavioural DV
> (the MECH-269(b) V3-EXQ-478 inert-reset signature), OR if rebinding does not track the true
> competitor above the shuffle control (i.e. it is arbitrary anchor-sensitivity, not functional
> rebinding).

**Why registerable as a candidate despite §2.** Candidates in this registry are precisely
lit-grounded, testable hypotheses not yet shown (MECH-269, MECH-270 themselves). This child is
(a) genuinely lit-grounded (§3, non-formal-import), (b) has a clean functional falsifier,
(c) decoupled from the settled null, (d) a distinct **locus** from MECH-269(b) (entity binding
vs proposer stream-anchor). Registering as `candidate/substrate_conditional/v3_pending` — with a
functional `what_would_answer` that the inert-reset precedent could not vacuously pass — captures
the salvaged positive **without** inflating the `shown` tail: only a `/queue-experiment`
functional win could ever promote it.

**Architecture-doc home.** `docs/architecture/entities_and_binding.md` (ARC-006 primary), with a
cross-link from `docs/architecture/v_s_invalidation_runtime.md` (the MECH-269 anchor-reset doc)
noting the entity-layer sibling.

### 4b. Evidence-note hygiene (applies under EITHER disposition below)

Regardless of 4a, the substrate demonstration is accurate evidence-note material (descriptive,
NOT a confidence move — 725a is `claim_ids=[]` non_contributory):

- **MECH-270** already carries the 720/725 binder-lineage notes → append a 725a line:
  *"V3-EXQ-725a (diagnostic, non_contributory): converged learned binder; rebinding-under-
  perturbation now positively exercised (`n_rebind_total=1676`, 0 in all predecessors) via
  `rebinding_probe`. Coherence-**specificity** SPEC 1/6 (settled no-claim); rebinding capability
  is the decoupled positive. Not a status change."*
- **MECH-269** (optional) → a one-line note that the entity-layer rebinding sibling is now
  substrate-exercisable (cross-ref MECH-456 if 4a is approved).

---

## 5. The decision (per-child, user-gated)

**Option A (RECOMMENDED) — register MECH-456** as scoped in §4a (candidate /
substrate_conditional / v3_pending, coherence-specificity stripped, functional
`what_would_answer`) **+ the §4b evidence notes.** Then it is `/queue-experiment`-ready for the
functional rebinding test.

**Option B (conservative anti-proliferation) — do NOT register a standalone MECH.** Apply only
the §4b evidence notes (record the exercisability gain on MECH-269/270), and **gate any future
claim behind the functional test first** — i.e. queue the §4a `what_would_answer` experiment,
and register a MECH only if it produces a behavioural win. Rationale: the intake itself judged
"continuous rebinding under perturbation" as *"Implicit → sharpening worth a **test**"* (not a
new claim), and MECH-269(b) already occupies the abstract mechanism at a sibling locus while
stuck on exactly the functional-consequence gap.

**Recommendation:** **Option A.** The biology is strong and non-formal-import (§3), the substrate
is built and the capability observed (more than most candidates carry at registration), and a
`candidate/substrate_conditional` with a functional falsifier is the registry's designed vehicle
for exactly this — auditable, reversible, and unable to reach `shown` without a real test. Option
B is the correct choice if the priority is to hold the `candidate` tail as small as possible and
force the test to precede the claim.

---

## 6. Supersession / narrowing

- No existing claim is superseded or narrowed. MECH-269(b) anchor-reset is untouched (this is a
  **sibling** at a different locus, wired via `depends_on`, not a replacement).
- The candidate Q `entities/selection.coherence_nonreducibility` remains **settled NO-CLAIM**
  (governance-owned, out of scope here).

---

## 7. Provenance

- Autopsy: `evidence/planning/failure_autopsy_V3-EXQ-725a_2026-07-10.{md,json}` §7.5, §8.
- Intakes (settling NO-CLAIM on the Q via next governance): `thought_intake_2026-04-23_binding.md`
  §4, `thought_intake_2026-04-23_path_integral_constraints_search.md`.
- Substrate: `ree-v3/ree_core/latent/cross_stream_binder.py::rebinding_probe`.
- Lit (this run): Kahneman/Treisman/Gibbs 1992; Sasi 2022; Manassi & Whitney 2022;
  Weilnhammer 2017; Cole 2024; Gershman 2010/2017 (already under MECH-269).
