# MECH-219 Affective-Harm Hysteretic Integrator — Design Memo (SD-019b unblock)

**Status:** IMPLEMENTED 2026-06-10 (substrate; SD-019b stays `v3_pending` until the
validation EXQ PASSes). Built by the `/implement-substrate` session
`mech219-implement-hysteretic-integrator-20260610T0720Z`. As-built record +
architecture doc: `docs/architecture/mech_219_hysteretic_integrator.md`. This memo
remains the authoritative design-rationale plan-of-record. (Was: DESIGN-FIRST,
pre-implementation.)
**Authored:** 2026-06-10 (session `mech219-hysteretic-integrator-design-memo-20260610T0713Z`).
**Scope:** design only — no `claims.yaml` edits, no `ree-v3` code in this pass.

---

## 0. One-paragraph summary

`SD-019b (harm_stream.suffering_accumulator)` is `ready: false` because the mechanism it
names — `MECH-219 affective_harm_hysteretic_integration` — has never been built, and the
`escapability_estimate` input MECH-219 needs was only ever a no-op placeholder
([cea.py:40](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/amygdala/cea.py)). Since MECH-219 was registered
(2026-04-24) a control-efficacy subsystem has landed (SD-058 `avoidance_efficacy`, MECH-353
`capacity_belief`, SD-059 escape-affordance credit) that now supplies that signal. This memo
(a) adjudicates the open `Q-036` variable set, (b) selects the escapability source, (c)
specifies the hysteretic-integrator dynamics, and (d) gives the `z_harm_a` re-source migration
plan — the load-bearing refactor that touches every `z_harm_a` consumer.

---

## 1. Where this sits

Three-tier harm-affect hierarchy. SD-019a built tier 2; this memo designs the tier-2→tier-3 step.

```
z_harm_s   (SD-010/011)            fast, instantaneous nociception            BUILT
   │  EMA α=0.2  (SD-019a, harm_un_ema)
z_harm_un  (SD-019a)               medium "make it stop" unpleasantness       BUILT + V3-EXQ-518 PASS
   │  MECH-219 controllability-gated hysteretic integration                   THIS MEMO
z_harm_a   (suffering)             slow, persistent, controllability-gated    UNBUILT (currently mis-sourced — see §6)
```

### Claim state (verbatim from `claims.yaml` / `substrate_queue.json`)
- **SD-019b** `harm_suffering_accumulator` — `candidate`, `v3_pending`,
  `depends_on: [SD-019a, SD-019, MECH-219, Q-036]`,
  `substrate_queue.depends_on_unresolved: [MECH-219, Q-036]`, `ready: false`.
  Functional restatement: `z_harm_a(t) = MECH219_integrate(z_harm_un, escapability_estimate, t)`.
- **MECH-219** `affective_harm_hysteretic_integration` — `candidate`, `mechanism_hypothesis`,
  `depends_on: [SD-019, SD-019a, SD-019b, SD-011, ARC-016]`. **No substrate_queue build entry.**
- **Q-036** (open_question): *"What additional variables, beyond temporal integration, are
  required for affective harm to become a genuinely distinct load state: persistence, recovery
  failure, uncontrollability, inescapability, or prediction error?"*

### Biology grounding already on file (biology-before-formal rule SATISFIED)
SD-019 targeted reviews: Price 2000 (dual pain pathway), Rainville 1997 (ACC/S1 double
dissociation), Woolf & Salter 2000 (central sensitisation), Craig 2003 (interoception),
Berthier 1988. Q-036 review: Salomons 2004 (controllability gates the ACC/insula suffering
circuit), De Ridder 2021, Loffler 2018 (three-way intensity/unpleasantness/suffering
dissociation; controllability selectively reduces suffering). Chronic-pain drift anchor:
Baliki 2012 (corticostriatal sensitisation). **A formal control-theory primitive (hysteretic
integrator) is being introduced, but it is anchored in this literature, not invented — the
SD-003/SD-010 "philosophy-right / mechanism-wrong" failure mode is guarded.**

---

## 2. Q-036 variable adjudication

Q-036 enumerates five candidate variables that might define affective harm as a *distinct*
load state. Adjudicated against the literature and against **what REE already owns**, to avoid
re-registering primitives that exist:

| Variable | Verdict | Rationale / where REE owns it |
|---|---|---|
| **Temporal integration** | **necessary, not sufficient** | already the bare EMA in SD-019a/z_harm_a. Loffler 2018 + the SD-019b title say integration alone makes z_harm_a "merely a temporally lagged copy" — the thing we must move past. |
| **Uncontrollability / inescapability** | **LOAD-BEARING — the defining gate** | Salomons 2004 + Maier & Seligman learned-helplessness tradition: the SAME nociception produces suffering when uncontrollable and not when controllable. This is the `escapability_estimate` modulator in SD-019b's restatement. Treat **uncontrollability and inescapability as one axis** at V3 grain (escapability ∈ [0,1]); a future split is V4. |
| **Recovery failure / persistence** | **emergent from the hysteresis, do NOT add as a separate input** | this is precisely what a *hysteretic* (asymmetric, sticky) integrator produces — slow to build, slow to release. Registering it as a separate variable would double-count the mechanism. |
| **Prediction error** | **secondary modulator, optional flag, default off** | SD-020 already aligns z_harm_a's *training target* with unsigned aversive PE (Chen 2023). Re-introducing PE as a per-tick accumulation driver risks re-litigating SD-020. Expose as an off-by-default gain so the validation can test it, but it is not part of the core commitment. |

**Recommended Q-036 resolution (governance follow-up, not this pass):** convert Q-036 from
`open` toward `resolved-by-design` once MECH-219 validates, with the answer: *suffering = a
controllability-gated **hysteretic** integral of unpleasantness; uncontrollability is the
defining modulator, recovery-failure/persistence is the emergent hysteresis signature, and
prediction-error is a secondary (optional) driver.* Keep Q-036 `open` until the validation
EXQ (§7) confirms the controllability dissociation.

---

## 3. Escapability-source options

MECH-219's accumulation rate is modulated by `escapability ∈ [0,1]` (1 = fully controllable →
minimal suffering accrual; 0 = inescapable → maximal accrual). The original `cea.py`
`escapability_hint` was a no-op placeholder. The following control-efficacy signals now exist
and can supply it:

| Source | Accessor | Semantics | Fit |
|---|---|---|---|
| **A. SD-058 / MECH-357 `InstrumentalAvoidanceGate`** | `agent.instrumental_avoidance.effective_efficacy()` → `[0,1]` ([infralimbic_avoidance_gate.py:182](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/pfc/infralimbic_avoidance_gate.py)) | learned avoidance-efficacy (eligibility trace), cross-episode-persistent, scaffold-floored | **RECOMMENDED.** Directly *is* "how well can I act to make this stop" — the literal escapability construct (Maier/Moscarello). Already cross-episode (matches suffering's slow timescale). |
| **B. MECH-353 `BlockedAgency` `capacity_belief`** | `capacity_belief` arg into `BlockedAgency.update` / `BlockedAgencyOutput.capacity_belief` ([blocked_agency.py:133](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/affect/blocked_agency.py)) | belief that capacity to act is retained; splits assert-vs-withdraw on the **same controllability axis** (its docstring names SD-019b explicitly) | strong conceptual sibling (assert pole vs suffering withdraw pole). But `capacity_belief` is itself derived from `1 - w·‖z_harm_a‖` → **circular** if z_harm_a is the MECH-219 output. Use as a *cross-check*, not the primary source. |
| **C. SD-059 / MECH-358 escape-affordance credit** | `agent.escape_affordance_bridge.get_state()` per-action relief/safety credit | per-action-class directed-escape credit | too fine-grained (per-action); escapability for suffering is a scalar regime signal. Could *aggregate* (max over classes) as a fallback. |
| **D. legacy `cea.py` `escapability_hint`** | placeholder | no-op | retire; replaced by (A). |

**Recommendation:** source escapability from **(A) `effective_efficacy()`**, with **(B)
`capacity_belief` retained only as a validation cross-check** (never as the driver, to avoid
the z_harm_a→capacity_belief→z_harm_a loop). Make the source **pluggable**
(`harm_suffering_escapability_mode ∈ {avoidance_efficacy, external, constant}`) exactly as
SD-058/MECH-353 made their analogous signals pluggable — so the validation EXQ can drive it
externally and a future session can swap sources without a module refactor. **Default
`constant=1.0` (fully escapable) so the integrator is inert/maximally-relieving under the
no-op default → bit-identical OFF.**

> **Dependency note:** sourcing escapability from SD-058 means MECH-219 (and therefore SD-019b)
> acquires a soft dependency on the SD-058 substrate. SD-058 is itself `v3_pending` pending
> V3-EXQ-603h-lineage validation. This is acceptable because the **default `constant` mode has
> no such dependency** — only the `avoidance_efficacy` mode does, and that mode is what the
> behavioural validation exercises once SD-058 clears. Record this in the SD-019b
> `depends_on` as a new soft edge to SD-058 during governance registration.

---

## 4. The hysteretic integrator — dynamics

A *hysteretic* integrator (vs the plain EMA already in z_harm_un) is the mechanism that turns
"lagged copy" into "distinct sticky load state". Proposed pure-arithmetic regulator
(`ree_core/affect/harm_suffering_accumulator.py`, sibling to `blocked_agency.py`), no trained
parameters, no gradient flow — matching the SD-019a EMA-buffer precedent and the MECH-313 /
MECH-320 / MECH-342 regulator pattern.

Per waking tick (gated `simulation_mode=False`, MECH-094):

```
u_t      = ‖z_harm_un‖                      # drive: medium-timescale unpleasantness (SD-019a)
g_t      = 1 - escapability_t               # uncontrollability gate ∈ [0,1]  (§3)
drive_t  = g_t * u_t                         # uncontrollable unpleasantness only accrues suffering

# Asymmetric (hysteretic) accumulation: fast-up under uncontrollable harm, slow-down on relief
if drive_t > s_{t-1}:                         # building
    s_t = s_{t-1} + alpha_rise * (drive_t - s_{t-1})
else:                                         # releasing (recovery)
    s_t = s_{t-1} + alpha_fall * (drive_t - s_{t-1})
#   with alpha_rise >> alpha_fall  -> hysteresis: suffering is sticky, recovery is slow

# Optional Schmitt-style bistable latch (the "distinct load STATE" reading, default off):
if s_t > theta_on:   suffering_latched = True
if s_t < theta_off:  suffering_latched = False     # theta_off < theta_on  -> hysteresis band

# Optional SD-020 PE driver (default off, gain 0):
drive_t += pe_gain * unsigned_PE_t
```

Output: a `z_harm_suffering` scalar/vector (same dim as z_harm_un) = `s_t` (× the latch if
enabled). This is what SD-019b means by "the output of MECH-219 operating on
harm_unpleasantness with controllability gating".

**Key design properties:**
- **`alpha_rise >> alpha_fall`** is the hysteresis (recovery-failure/persistence emerges here —
  §2 — not from a separate input). Lit anchor: Baliki 2012 corticostriatal drift; the slow
  release is the chronic-pain / allostatic-load signature.
- **`g_t = 1 - escapability`** is the Salomons 2004 / Loffler 2018 controllability gate: under
  full control (`escapability=1`) `drive_t=0` → suffering does not accrue even when
  unpleasantness `u_t` is high. **This is the falsifiable dissociation** (§7).
- **Controllability parity, the SD-019a mirror:** SD-021 descending modulation attenuates
  `z_harm_s` (and hence indirectly `z_harm_un`) but the escapability gate is computed from
  control-efficacy, *not* from the descending-modulation factor — so the
  intensity/unpleasantness/suffering three-way dissociation (Loffler 2018) is preserved end to
  end. (SD-019a already guarantees z_harm_un is not touched by SD-021; MECH-219 must guarantee
  the same for `escapability`.)
- **All knobs default to the inert regime** (`escapability_mode=constant=1.0` → `g_t=0` →
  `s_t→0`; latch off; pe_gain 0) → bit-identical OFF.

**Defaults (lit-anchored, calibratable by the validation EXQ — do NOT pin as governance):**
`alpha_rise≈0.2` (~5-step build, matches z_harm_un timescale), `alpha_fall≈0.01`
(~100-step release, allostatic), `theta_on≈0.5`, `theta_off≈0.3` (hysteresis band),
`pe_gain=0`, `use_bistable_latch=False`.

---

## 5. Distinct-from contracts (anti-duplication)

MECH-219 must be falsifiably distinct from adjacent substrates, or it is over-specification:

- **vs SD-019a z_harm_un (EMA):** z_harm_un is *symmetric* EMA, controllability-*independent*.
  MECH-219 is *asymmetric/hysteretic* and controllability-*gated*. The escapability gate is the
  discriminator (turn it to constant=1 → MECH-219 collapses toward a slow EMA).
- **vs SD-022 body-damage z_harm_a (current):** body-damage is an env-sourced slow EMA over
  limb state; it is NOT controllability-gated. MECH-219 re-sources z_harm_a from z_harm_un
  under a control gate (§6). The migration must show the controllability dissociation that the
  body-damage stream cannot produce.
- **vs MECH-353 blocked-agency:** MECH-353 is the *capacity-RETAINED ASSERT* pole (high
  capacity_belief → act); MECH-219 is the *capacity-COLLAPSED WITHDRAW* pole (low escapability
  → suffer). Same controllability axis, opposite pole — already noted in
  [blocked_agency.py:17](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/affect/blocked_agency.py). They must
  anti-correlate in the validation.
- **vs SD-032e pACC (`drive_bias`):** pACC accumulates a slow autonomic drift from z_harm_a.
  MECH-219 sits UPSTREAM (it *produces* the z_harm_a that pACC then drifts on). Wiring order
  matters (§6): MECH-219 must run before pACC reads z_harm_a.

---

## 6. The `z_harm_a` re-source migration — the load-bearing refactor

This is why SD-019b is not a clean standalone build. SD-019b redefines what `z_harm_a` *is*:
from the SD-022 body-damage encoder output to the MECH-219 hysteretic-integrator output.
`z_harm_a` is read by **CeA, BLA (SD-035), AIC (SD-032c), dACC (SD-032b), pACC (SD-032e), PAG
(MECH-279), MECH-090/091 urgency interrupt, MECH-353 capacity_belief, SD-058/059 threat
scaling**. A naive swap would silently change every one of those.

**Migration strategy — the SD-019a redirect precedent (do NOT hard-swap):**

1. **Add `z_harm_suffering` as a NEW LatentState field** (parallel to how SD-019a added
   `z_harm_un`). Populate it from MECH-219 in `sense()` after z_harm_un is computed and after
   escapability is read.
2. **Do NOT overwrite the existing z_harm_a path.** Instead add a master flag
   `use_harm_suffering_accumulator` (default False, bit-identical). When **ON**, redirect the
   z_harm_a *consumers* to read `z_harm_suffering` — exactly as SD-019a redirected AIC + E3
   urgency to read z_harm_un. Per-consumer redirect, not a global alias, so the migration can be
   staged and individually ablated.
3. **Staged consumer migration (each independently flagged for the validation ablation):**
   AIC urgency → PAG freeze drive → MECH-091 interrupt → dACC/pACC. dACC and pACC are the
   riskiest (they have their own E2_harm_a forward models keyed on the current z_harm_a
   semantics); migrate them last and verify their forward-model R² survives the source change.
4. **Wiring order:** MECH-219 runs in `sense()` *before* SD-032 consumers and pACC drift, so
   they read the suffering output on the same tick (the SD-019a/SD-036 in-sense ordering
   precedent).
5. **Bit-identical OFF guarantee:** with `use_harm_suffering_accumulator=False`,
   `z_harm_suffering=None`, every consumer reads the legacy z_harm_a → byte-identical action
   stream. Verify with the standard default-vs-explicit-False contract.

**Open design fork (flag in the memo for the build session):** is the SD-022 body-damage
signal (a) *replaced* by MECH-219, or (b) *folded into* MECH-219's drive (body damage is
itself a source of uncontrollable unpleasantness)? **Recommendation (b):** route the
body-damage contribution through z_harm_un / the MECH-219 drive rather than discarding it, so
SD-022's causal-independence evidence (EXQ-319/323a) is preserved rather than orphaned. This
keeps SD-019/SD-022's non-redundancy result intact and avoids invalidating landed evidence.

---

## 7. Validation experiment (sketch — for a later `/queue-experiment` session, NOT now)

**Substrate-readiness diagnostic, `claim_ids=[]`** first; the behavioural MECH-219/SD-019b
evidence successor is separate.

**Core falsifier — the controllability dissociation (Loffler 2018 / Salomons 2004):**
matched nociception (same z_harm_un trajectory) under **escapable** vs **inescapable**
conditions (drive escapability from SD-058 `effective_efficacy()` or an external scripted
schedule). Pre-registered prediction:

- **C1 (controllability gate):** `z_harm_suffering` accrues under inescapable but stays low
  under escapable, at matched z_harm_un. (The dissociation the body-damage z_harm_a cannot
  produce.)
- **C2 (hysteresis):** after a harm bout ends, `z_harm_suffering` releases on the slow
  `alpha_fall` timescale (recovery-failure signature); z_harm_un releases fast. Asymmetric
  build-vs-release confirmed.
- **C3 (non-vacuity / distinct-from):** `z_harm_suffering` ≠ a re-scaled z_harm_un (escapable
  arm with high z_harm_un but near-zero suffering is the discriminator); and anti-correlates
  with MECH-353 `z_block_assert` under the same controllability sweep (assert vs withdraw).
- **C4 (parity):** SD-021 descending modulation attenuates z_harm_s but not the escapability
  gate (the SD-019a UC3 mirror).

Self-route `substrate_not_ready_requeue` if the encoder is untrained (the escapability signal
or z_harm_un are degenerate) — same discipline as the SD-058/MECH-353 validations.

---

## 8. Governance follow-ups (NOT done in this design pass)

1. **`substrate_queue.json`:** add a build entry for **MECH-219** itself (it currently has
   none) and an `amend_history` note on SD-019b pointing at this memo; keep both `ready: false`
   until the build + validation land.
2. **`claims.yaml`:** add the soft `depends_on: SD-058` edge to MECH-219/SD-019b (escapability
   source); add an `implementation_note` on MECH-219 referencing this memo; **no flag or
   confidence change** (design only).
3. **Q-036:** keep `open`; record the §2 adjudication as the *proposed* resolution, to be
   confirmed by the validation C1/C2.
4. **`design_doc` field:** set SD-019b / MECH-219 `design_doc` →
   `docs/architecture/mech_219_*.md` once the build session promotes this planning memo to an
   architecture doc (the SD-056 / MECH-342 precedent: plan-of-record in `evidence/planning/`,
   architecture doc in `docs/architecture/` at implement time).

---

## 9. Risks / open questions

- **R1 — circularity:** if escapability is sourced from MECH-353 `capacity_belief` (which is
  `1 - w·‖z_harm_a‖`) and z_harm_a becomes the MECH-219 output, the loop closes on itself. §3
  mitigation: source from SD-058 `effective_efficacy()` (no z_harm_a term); use capacity_belief
  only as a cross-check.
- **R2 — SD-058 dependency timing:** the `avoidance_efficacy` escapability mode depends on
  SD-058 clearing its own validation. Default `constant` mode is dependency-free; the
  behavioural validation that needs `avoidance_efficacy` waits on SD-058. Sequence accordingly.
- **R3 — dACC/pACC forward-model breakage:** SD-032b/e own E2_harm_a forward models keyed on
  the current z_harm_a semantics. Migrating them to z_harm_suffering may degrade their R².
  Migrate last, measure, and keep the option to leave dACC/pACC on the legacy z_harm_a if the
  forward models do not transfer (i.e. z_harm_suffering redirects only the urgency/PAG/interrupt
  consumers in v1).
- **R4 — orphaned SD-022 evidence:** mitigated by §6 fork (b) — fold body-damage into the
  MECH-219 drive rather than discarding it.
- **R5 — bistable latch scope:** the Schmitt latch (`use_bistable_latch`) is the strongest
  "distinct load STATE" reading but adds a discrete state variable. Default off; let the
  validation decide whether the graded `s_t` alone suffices or the latch is needed.

---

## 10. Build-session checklist (hand to `/implement-substrate`)

- [ ] New module `ree_core/affect/harm_suffering_accumulator.py` (pure-arithmetic regulator, §4).
- [ ] `LatentState.z_harm_suffering` field + `detach()` handling.
- [ ] `escapability_mode` pluggable source (default `constant=1.0`), wired to
      `effective_efficacy()` in the `avoidance_efficacy` mode (§3).
- [ ] `use_harm_suffering_accumulator` master flag + per-consumer redirect flags (§6), all
      default OFF → bit-identical.
- [ ] `sense()` wiring before SD-032/pACC consumers; MECH-094 `simulation_mode` no-op.
- [ ] Body-damage fold-in per §6 fork (b).
- [ ] Contracts: bit-identical OFF; controllability gate; hysteresis asymmetry; distinct-from
      z_harm_un; MECH-094 sim no-op; SD-021 parity.
- [ ] Substrate-readiness EXQ (§7) via `/queue-experiment` (NOT in the build session).
- [ ] Governance follow-ups (§8) via `/governance` after validation.

---

*See also:* `sd_019_harm_nonredundancy.md` (SD-019), ree-v3/CLAUDE.md "SD-019a:
harm_unpleasantness_channel" (the tier-2 precedent this mirrors), `sd_058_*` /
`sd_059_*` / `mech_353_*` (the escapability sources), `substrate_queue.json` (SD-019b /
SD-019a / MECH-302 entries).
