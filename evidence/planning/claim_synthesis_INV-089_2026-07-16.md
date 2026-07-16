# Claim-Synthesis Proposal — INV-089 (ceiling vs growth-coupling/driver split)

- **Generated (UTC):** 2026-07-16T05:31:57Z
- **Skill:** `/claim-synthesis` (proposal-first; **nothing lands in `claims.yaml` without per-child user approval**)
- **Trigger:** `failure_autopsy_746c-756_2026-07-16.{md,json}` (Target A), `granularity_debt_trigger.fires = true`, user-confirmed route at the autopsy gate.
- **Cluster:** INV-089 `harm_evaluator_bounded_by_z_harm_differentiation` (emergent invariant, **provisional**), the 746 lineage (743 / 746 / 746a / 746b / 746c).
- **Status:** PROPOSAL — awaiting per-child approval. Registration DEFERRED until the active `governance-2026-07-16` claim on `claims.yaml` closes (concurrency note §7).

---

## 1. The cluster (direct nomination)

Every run bearing on INV-089, with its adjudicated weight:

| Run | Preconditions | Outcome | Adjudication | Weight on INV-089 |
|---|---|---|---|---|
| **743** | met | PASS (positive control) | supports | **active — the sole undisturbed support** (single-pathway z_harm-decodability rises with maturation) |
| 746 | unmet | FAIL, superseded | DV starved (undecodable single-cell target, un-clipped head blow-up) | scoring-excluded (superseded) |
| 746a | met | FAIL, **weakens** | DV measurement artifact (unregularised head, held-out R² −26…−166) → **measurement-suspect** per 746b autopsy | still active/weighted, flagged measurement-suspect |
| 746b | unmet | FAIL, non_contributory | IV starved (`PC_iv_moved=False`); DV-estimator fix validated at maturity (dv_mature 0.45) | no weight |
| **746c** | **met (all 4)** | FAIL, self-routed `weakens` | **ADJUDICATED non_contributory** — first VALID bound test, ran in a **non-binding regime** | **no weight** |

Autopsy docs naming the cluster: `failure_autopsy_morning-digest-742-744a-745-746-746a_2026-07-13`, `failure_autopsy_V3-EXQ-746b_2026-07-15`, `failure_autopsy_746c-756_2026-07-16`.

---

## 2. Discrimination gate (Step 3 — the load-bearing filter)

Classifying each FAIL by the four Step-3 classes:

- **746 / 746a / 746b — measurement / test-design debt (EXCLUDE from the granularity signal).** 746 = DV target/clipping starve; 746a = unregularised-head DV artifact (now measurement-suspect); 746b = IV starved because the DV-power fix (`collect 14→60`) washed out the IV onset gradient (anti-coupled data budgets). These three are *measurement-instrument iterations of one bound test* — which is exactly why the 746b autopsy set `granularity_debt_trigger.fires = false`.
- **746c — the residue that changes the verdict.** 746c is the **first VALID test**: all four preconditions met, `non_degenerate=True`, DV-estimator fix retained (dv_mature 0.89). It fails C1/C2/C3 — but its four-layer diagnosis reads `claim_alignment: intact (untested)`, `measurement: inadequate (regime)`. The failure is **not another measurement bug and not a claim falsification**: the test operationalizes the bound as a **monotone driver** (`couple_rho ≥ 0.80`), while it ran in a regime where prox z_harm differentiation is **already ~0.82 at onset 0**, rising only to ~0.87 — non-binding at every tested onset. In a non-binding regime a *ceiling* predicts flat-high, decoupled harm_eval — exactly observed (dv_mature 0.89; couple_rho 0.675, 6/8 seeds strongly positive).

**Why this clears the granularity-debt bar rather than the test-design-debt STOP.** By the letter of Step 3, a cluster whose dominant `measurement` is "regime-inadequate" could look like the MECH-341 over-specified-falsifier EXCLUDE. It is the **mirror image**, and the discriminator is decisive:

- MECH-341 (STOP): the *test* interrogated a finer axis than the claim asserts → **retire one test**, no new claim.
- INV-089 (PROCEED): the **claim text itself** asserts *two separable mechanisms under one id** — read the description verbatim: *"strictly bounded by z_harm representational differentiation"* (a **ceiling**: `harm_eval ≤ f(differentiation)`) **and** *"Productive harm-evaluator training cannot precede sufficient z_harm differentiation"* (a **growth-coupling/driver**: quality *rises with* differentiation as it matures). These need **different instruments** (an envelope/upper-bound test vs a monotone-coupling test) and **different regimes** (the ceiling is expressible at any differentiation level; the driver is only falsifiable while differentiation is *binding*). The 746 lineage kept building the driver instrument, and — across 746a/b/c — **no available harm target has a binding maturation gradient in this substrate** (`dens` = small-sample artifact, realized-harm `Y` = flat, `prox` = already-high). The driver reading is therefore *structurally unfalsifiable* in every regime the current curriculum can reach, while the ceiling reading has never been given its own instrument.

**Verdict: PROCEED (granularity debt).** ≥2 distinct, genuine, substrate-ready signatures are circling one claim, and the residue is not a measurement bug — it is one id carrying two separately-testable assertions. This is the same shape that split INV-064 → {INV-088 world/goal leg, INV-089 harm leg} on 2026-07-12; INV-089 now pays a second, finer round of the same debt.

---

## 3. The common thread (Step 4)

> **Every run in the cluster tests whether harm_eval quality *rises with* z_harm differentiation (a monotone driver); INV-089's title and lit warrant actually assert only that harm_eval quality *cannot exceed* z_harm differentiation (a ceiling). The claim never names which of the two is the invariant — and the two require different instruments and different regimes. The ceiling is testable now (as a per-onset envelope, in any regime); the driver needs a binding-then-released differentiation gradient that no current harm target provides.**

---

## 4. Lit grounding (Step 5) — the existing `targeted_review_inv_089` is sufficient and *differential*

No new lit-pull is commissioned: the existing review (lit_conf 0.793, pulled 2026-07-14) already speaks to both readings, and it **leans toward the ceiling** while gently pressuring the driver. This differential is itself a finding that shapes the split.

- **Beggs 2015 (supports 0.60) — grounds the CEILING.** "Nociceptive circuitry is functioning at birth… however, there is still considerable organization and refinement… before full discrimination… is possible." A *present-but-undifferentiated-then-refines* / **precondition-gating** shape: differentiation *gates* discriminative capacity. This is the ceiling ("cannot exceed"), not a claim that experience drives the co-rise.
- **Verriotis, Chang, Fitzgerald & Fabrizi 2016 (supports 0.74 — highest) — grounds the CEILING and *pressures* the DRIVER.** "Unlike other sensory systems, the pain system… cannot rely upon prolonged activity-dependent shaping through repeated noxious stimulation." Nociceptive representational maturation is **largely non-activity-dependent**, on a distinct timeline. The entry explicitly flags that this "gently warns that the REE picture — train the harm-evaluator once z_harm has differentiated — may over-assume that experience-driven refinement is even the operative mechanism for harm." → The differentiation trajectory is a **maturational gate** (ceiling) more than an **experience-driven co-riser** (driver).
- **Bastuji 2016 (supports 0.72) — grounds the distinct-encoder premise** (parallel spino-thalamic/spino-parabrachial routing to operculo-insular/mid-cingulate, separate from the exteroceptive stream). Warrants the *separate z_harm stream* that both children inherit; adult data, silent on developmental time-course, so neutral between ceiling and driver.

**Consequence for the split:** the **ceiling child inherits the bulk of the 0.793 warrant**; the **driver child's biological warrant is thinner and partly counter-indicated** (Verriotis). The driver is not a pure formal import (a developmental-refinement story exists), so it is proposed — but as a weaker, substrate-conditional candidate, explicitly flagged.

---

## 5. Proposed decomposition

**Fate of INV-089: NARROW-AND-RETAIN as the ceiling + mint ONE new driver child (INV-090).**

Rationale for narrow-and-retain (vs pure umbrella + two children): INV-089's *title* — `harm_evaluator_bounded_by_z_harm_differentiation` ("bounded by" = upper bound) — and its lit warrant already **are** the ceiling. The driver ("rises with") is the reading the *tests* drifted into but the title never asserts. So the faithful, minimal move is to tighten INV-089's own text to the ceiling and isolate the driver as a separate claim, rather than inflate the registry with two new ids and an empty umbrella. This also **cleanly resolves the 746a re-read** (§6): 746a/b/c are *all driver tests*, so once INV-089 = ceiling, none of them weigh on it — they attach to the new driver child.

### Child A — INV-089 (NARROWED, retained) · the CEILING

| Field | Value |
|---|---|
| id | **INV-089** (unchanged — narrowed in place) |
| claim_type / invariant_type | invariant / emergent (unchanged: `emergent_from: [ARC-003, ARC-019, ARC-027]`) |
| status | **provisional** (unchanged; must NOT advance to stable until a valid **ceiling-form** test exists — narrow-supports rail) |
| subject | development.maturational_sequence (unchanged) |
| one-line claim | E3's nociceptive harm-evaluation quality (`harm_eval_z_harm`) **cannot exceed** an upper bound set by z_harm representational differentiation: for a fixed evaluator-training budget on frozen z_harm, held-out harm-eval quality at any maturation point is ≤ what a same-budget decoder can extract from z_harm at that point. A *ceiling*, not a co-riser: it constrains the maximum, and is silent on whether quality tracks differentiation upward during maturation. |
| draft `what_would_answer` | An **envelope / upper-bound** contrast (works in any regime, incl. non-binding): at each HarmEncoder onset, compare held-out `harm_eval_z_harm` quality against the same-budget z_harm→harm-target *decodability ceiling* on frozen z_harm. **Supported** if harm-eval quality stays at-or-below the differentiation-implied ceiling across onsets (never exceeds it), with the z_harm trajectory reported separately from z_world. **Falsified** if `harm_eval_z_harm` quality *exceeds* the z_harm-differentiation ceiling at any onset (evaluation richer than the representation can support → the bound is not real). Explicitly NOT a monotone-coupling test and NOT a z_world decode. |
| epistemic_category | (none — **not** `substrate_ceiling`; substrate is built, SD-010 HarmEncoder + `harm_eval_z_harm` exist) |
| depends_on | `[INV-064, SD-010, ARC-003, ARC-019, ARC-027]` (unchanged) |
| lit grounding | Beggs 2015 (gating shape), Verriotis 2016 (non-activity-dependent maturation-as-precondition), Bastuji 2016 (separate stream). **Inherits the bulk of lit_conf 0.793.** |
| cluster evidence it explains | 743 (positive control — decodability exists and rises: the *precondition* the ceiling needs); 746c's flat-high decoupled harm_eval in a non-binding regime is **consistent** with (not against) a ceiling. |
| relationship | umbrella parent of INV-090 (the driver child); sibling of INV-088 (the z_world-leg analogue). |

### Child B — INV-090 (NEW) · the GROWTH-COUPLING / DRIVER

| Field | Value |
|---|---|
| id | **INV-090** (next free — max INV id is 089 at time of writing; re-check at registration) |
| claim_type / invariant_type | invariant / emergent (`emergent_from: [ARC-003, ARC-019, ARC-027]`) |
| status | **candidate**, `epistemic_category: substrate_conditional`, `pending_substrate_reconfirmation: true` — **substrate-blocked**: not validly testable until a curriculum drives harm-target z_harm differentiation through a *binding* (genuinely low → released) regime. |
| subject | development.maturational_sequence |
| one-line claim | During maturation, `harm_eval_z_harm` held-out quality **rises monotonically with** z_harm representational differentiation **while differentiation is the binding constraint** (the low-differentiation regime). Distinct from the ceiling (INV-089): asserts the *upward co-movement*, not merely the cap. |
| draft `what_would_answer` | A monotone-coupling contrast **in a binding regime**: with a harm target whose z_harm differentiation starts genuinely LOW (onset-0 differentiation well below the harm-eval-saturating level) and rises with maturation, show `harm_eval_z_harm` held-out quality rises monotonically with, and rank-couples to (`couple_rho ≥ 0.80`), that differentiation across onset. **Precondition gate must verify a binding regime** (a minimum onset-0-to-mature differentiation gap AND onset-0 below saturation) — the missing gate the 746 lineage's `PC_iv_moved` never enforced. **Falsified** if quality is flat/non-monotone across a validly-moving, binding differentiation gradient. |
| epistemic_category | `substrate_conditional` |
| depends_on | `[INV-089, INV-064, SD-010, ARC-003, ARC-019, ARC-027]` (child of the INV-089 ceiling) |
| lit grounding | Beggs 2015 (postnatal refinement) — but **thinner / partly counter-indicated**: Verriotis 2016 says nociceptive maturation is *non-activity-dependent*, which pressures an experience-driven co-rise. Registered with an explicit `notes` caveat that its warrant is weaker than the ceiling's and the driver mechanism may not be biologically operative for harm. |
| cluster evidence it explains | The entire 746 lineage (746a/b/c) — all monotone-driver tests. 746c is the first *valid* one and fails only because it ran non-binding; 746a/746b never validly ran (measurement-suspect / IV-starved). |
| substrate fallback (NOT created here) | If INV-090 is approved, the test needs a **new `substrate_queue` entry**: a maturation curriculum that starts harm-target z_harm differentiation genuinely LOW (binding-then-released). Created only *after* the split lands, per the re-derive brake — **not** a naive same-regime 746-letter. |

---

## 6. 746a re-read (fold-in from the autopsy — governance decides)

The autopsy asked governance to re-weigh the still-active 746a weakens. This split resolves it structurally:

- **746a is a DRIVER test** (monotone C1 rho / C2 couple). Under the split, the driver reading is **INV-090**, not INV-089. So 746a's weakens should **move off INV-089 (the ceiling) and attach to INV-090 (the driver)** — and there it is doubly discounted: already flagged *measurement-suspect* (746b validated the DV-estimator fix that 746a lacked), and 746c now shows the driver test **cannot validly run in the available (non-binding) regime** at all, so 746a's onset gradient is itself likely the collect=14 small-sample artifact.
- **Net effect on INV-089's live_status:** the current `live_status.evidence` (746a weakens) and the `evidence_quality_note` phrase *"the 'strictly bounded by z_harm differentiation' reading is now actively pressured"* **over-state a driver-test result against the ceiling**. On the narrowed ceiling INV-089, the correct reading is: **no active weakens; sole support 743; stays provisional pending a valid ceiling-form test.** Recommend governance update `live_status` accordingly when the split lands.
- **This is analysis-only.** `/claim-synthesis` does not re-score; governance applies the re-weight. Flagged here so the two operations stay consistent.

---

## 7. Registration plan + concurrency note (Step 7 — on approval only)

**Do not register yet.** On per-child approval:

1. **Concurrency gate:** the `governance-2026-07-16` session holds an **active** claim on `claims.yaml` / `claims.json` / `assets/data/claims.json` / `evidence/planning/` (claimed 2026-07-16T01:31Z). Registration must wait until that claim closes (or is explicitly deconflicted with the user), then **re-read the INV-089 insertion region immediately before editing** — governance may itself rewrite INV-089's `evidence_quality_note`/`live_status` from the 746c adjudication.
2. Expand this session's `TASK_CLAIMS` entry to cover `docs/claims/claims.yaml`, `docs/assets/data/claims.json`, and this planning file.
3. Narrow INV-089 in place (tighten description/`what_would_answer`/`live_status` to the ceiling; add the INV-090 child pointer + `origin` note referencing this proposal). Register INV-090 (allocate id by re-checking max at write time + recent `git log`; wire `depends_on: [INV-089, …]`; add an architecture-doc stub). Neither promotes nor demotes anything.
4. `python scripts/build_claims_json.py` (re-runs validator + regenerates `claims.json`; confirm INV-090 appears and the stance tally moved by +1 candidate).
5. Pathspec commit (`-- docs/claims/claims.yaml docs/assets/data/claims.json evidence/planning/claim_synthesis_INV-089_2026-07-16.md`), `git show --stat HEAD`, push `HEAD:master`.
6. **Hand-off:** INV-089 (ceiling) → `/queue-experiment` for a **ceiling-form envelope test** (testable now, no substrate build owed). INV-090 (driver) → `/implement-substrate` for the binding-regime maturation curriculum (a *new* substrate_queue entry), THEN `/queue-experiment`. Re-derive brake stays armed: a naive same-regime 746-letter of the driver test is REFUSED.

**Constraint honoured:** INV-089 is **not weakened** — this is granularity refinement, not falsification. 743 remains its undisturbed support; it stays provisional.

---

## 8. Open decision for the user (per-child)

1. **Narrow INV-089 to the ceiling** (Child A) — approve / edit / reject.
2. **Register INV-090 as the driver child** (Child B), substrate_conditional / candidate — approve / edit / reject. (Rejecting B = INV-089 narrows to the ceiling and the driver reading is dropped, not registered; the 746 lineage's driver framing is retired.)
3. Structure preference: **narrow-and-retain + one child** (recommended, above) vs **pure umbrella + two new children** (INV-089 → empty umbrella, mint INV-090 ceiling + INV-091 driver).
