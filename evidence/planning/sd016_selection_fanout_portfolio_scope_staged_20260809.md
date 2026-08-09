# SD-016 Selection-Mechanism GOV-FANOUT-1 Discrimination Portfolio — Scope of Record

**Status: AWAITING USER REVIEW before any leg is built or queued.** This is a scoping
artifact produced headlessly by chip `chip-20260809-sd016-fanout-portfolio`. It designs the
portfolio and routes each leg; it does **not** itself write experiment scripts or append queue
entries. Each leg still runs through the full `/queue-experiment` skill (Step 2.5 readiness →
Step 2.5b re-derive brake → Step 2.5c substrate-path gate → smoke test) in its own session.

**Date:** 2026-08-09
**Author session:** metaworker-chip-20260809-sd016-fanout-portfolio (headless)
**Upstream autopsy:** `failure_autopsy_V3-EXQ-898_2026-08-08.{md,json}` (confirmed,
user-ratified routing at the Step 8 gate)
**Target substrate:** SD-016 ContextMemory cue-indexed retrieval — the **selection mechanism**,
not the encoder (the encoder-separation precondition is now satisfied, see §1).
**Node classification (work-graph debt vocabulary):** `complex (probe-gated) / puzzle (known
rules)` — the frame is well-posed and the substrate now supplies a genuinely-varying input; the
missing fact is *which* of ≥2 live fixes breaks the uniform-selection saddle. ≥2 live rivals →
GOV-FANOUT-1 portfolio, not one more sequential re-pose.

---

## 1. Shared diagnosis (why a fan-out, not another letter)

Three independently-designed selection mechanisms have now hit the identical uniform-softmax
saddle (`sel_entropy_mean → ln(16) = 2.7726`) under three training regimes:

| Attempt | Mechanism | Training signal | C1 (entropy<2.5) | C1b (ctx-div>0.1) |
|---|---|---|---|---|
| 418d/e/i (Path 1) | q.k attention + population diversification loss (w 0.5–5.0) | slot-diversity (population-level) | FAIL every weight | not instrumented yet |
| 418m (Path 3) | feedforward tagger, **untrained** encoder | `terrain_loss` only | FAIL 0/3 | FAIL 0/3 |
| **898 (Path 3)** | feedforward tagger, **SD-070-trained** encoder | `terrain_loss` only | FAIL 0/3 | FAIL 0/3 |

V3-EXQ-898's decisive contribution: its readiness gate proves the encoder fix genuinely takes
on this apparatus (`world_encoder_weights_moved` = 5.0 vs ≥1.0; `z_world_spread_lift` 3.53–5.20
vs ≥1.3, i.e. **2.7–4.0× the floor**, all 3 seeds), and a held-out probe shows z_world decodes
hazard/resource presence at balanced-accuracy 0.95–0.99. So the FAIL cleanly attributes to the
**selection mechanism**, not to "nothing to select on." C2 (the OFF control) reproduces
`ln(16)` to 5 decimal places on every seed — uniform selection is a **genuine, stable attractor
of this loss landscape**, not an unconverged transient.

**The single unifying gap the three attempts share:** *no tested mechanism has ever been given a
training signal or architecture that specifically rewards context-**CONDITIONED** divergence*
(the safe-vs-dangerous selection distributions differing **from each other**), as distinct from
population-level slot diversity (differing from uniform in aggregate — which Path 1 achieved and
which did **not** help). The portfolio attacks that gap along three orthogonal design axes.

---

## 2. Shared experimental scaffold (every leg inherits this from V3-EXQ-898)

All legs are variants of the 898 harness
(`ree-v3/experiments/v3_exq_898_sd016_lega_encoder_fix_retest.py`), reusing:

- **Encoder recipe:** SD-070 D128_TRAINED — `world_dim=128`, `P0A_EPISODES=60`
  (`experiments._lib.zworld_p0_warmup.run_zworld_p0`), the validated V3-EXQ-783 operating point.
- **Readiness gate (MANDATORY, load-bearing for validity):** every cell runs the two 898
  preconditions (`world_encoder_weights_moved ≥ 1`, `z_world_spread_lift ≥ 1.3`) **before**
  P1. A cell failing readiness self-routes to `substrate_not_ready_requeue` for that seed; if a
  majority of seeds fail readiness the whole run is `non_contributory` (env/encoder, not
  selection). **This is what makes a portfolio null attributable to the selection mechanism
  rather than the encoder** — do not drop it in any leg.
- **P1 training:** E1-only, on `z_world.detach()`, alternating safe/dangerous env every
  `CONTEXT_SWITCH_EVERY=5` episodes; the encoder optimiser is never stepped in P1.
- **Metrics** (computed on held-out `z_safe`/`z_dang` eval batches; the tagger's
  `_last_cue_slot_weights` cache is the read-out for entropy/divergence):
  - `sel_entropy_mean` — mean slot-selection Shannon entropy; uniform ref `ln(16)=2.7726`.
  - `sel_context_divergence` — L1 distance between mean safe-vs-dangerous selection
    distributions (`|mean_w_safe − mean_w_dang|₁`).
  - corroborating (non-gating): `action_bias_div`, `action_bias_per_channel_std`.
- **Acceptance shape (the load-bearing pair + control):**
  - **C1 (primary):** ON `sel_entropy_mean < 2.5` on a majority of ready seeds.
  - **C1b (anti-degeneracy):** ON `sel_context_divergence > 0.1` on a majority of ready seeds.
    C1 alone is degenerate — a tagger that collapses to one slot **regardless of context**
    passes C1 (low entropy) but fails C1b (no divergence). **C1b is the guard against
    "constant-peaky" masquerading as "context-selective"; every leg keeps it.**
  - **C2 (control):** OFF (legacy q.k) `sel_entropy_mean > 2.65` on a majority of ready seeds —
    confirms the ablation isolates the selection change and the substrate is otherwise on the
    418-family saddle.
- **Seeds:** `[42, 43, 44]` (majority = 2/3), `machine_affinity: any` (cloud), `_v3` run_id,
  `architecture_epoch: ree_hybrid_guardrails_v1`.

**Baseline reuse (nicety, not required):** the 898 A0_OFF arm is the exact ln(16) control every
leg carries. If a leg's OFF arm is factored into `experiments/_lib/baselines/sd016_selection.py`
and fingerprinted with `include_driver_script_in_hash=False`, later legs can cache-reuse it
across drivers (per `/queue-experiment` "Saving a baseline for reuse"). Optional; do not gate a
leg on it.

---

## 3. The three legs

### Leg H1 — DRIVE axis: explicit context-divergence auxiliary objective

**Hypothesis:** the tagger *can* represent context-selective slot distributions but the loss
landscape never rewards them; `terrain_loss` is satisfied equally well by uniform mixing (the
ln(16) attractor). Add an auxiliary objective that directly rewards `sel_context_divergence`
during P1 and the tagger leaves the saddle.

**Substrate requirement — NONE (driver-only probe).** The autopsy sketch says "add an auxiliary
loss maximising sel_context_divergence." The obvious hook, `_last_cue_slot_weights`, is
`.detach()`ed at `e1_deep.py:450`, so it carries no gradient. **But the driver does not need
that cache:** it can call `agent.e1.cue_slot_tagger(z_world)` directly (a public `nn.Sequential`
module) and build differentiable softmax weights itself, then add
`−λ · |mean_w_safe − mean_w_dang|₁` (a batched safe/dangerous pair per P1 step) to the E1 loss.
This keeps H1 a **pure `/queue-experiment` diagnostic with no `/implement-substrate`
dependency** — the correct probe-first sequencing. **If H1 confirms the mechanism helps**, THEN
promote it to a real substrate knob (`sd016_context_divergence_weight` + a differentiable
`E1.compute_context_divergence_loss` method) wired into the live E1 training path — a follow-on
`/implement-substrate`, not part of the probe.

**Arms:**
- `A0_OFF` — legacy q.k attention (C2 control, reproduces ln(16)).
- `A1_tagger` — Path-3 tagger, no divergence loss = **matched-budget baseline** (the 898 ON
  arm, same P1 budget). This is what makes an H1 positive attributable to the *objective*, not
  to any budget change.
- `A2_tagger_ctxdiv` — Path-3 tagger + the auxiliary context-divergence loss (sweep λ over
  e.g. {0.5, 1.0, 2.0} as sub-cells, since Path 1 showed weight matters).

**Null declaration (what a non_contributory / FAIL H1 means):** if A2 still fails C1/C1b with
readiness met, the context-conditioned *objective* is insufficient on the current representation
— it does **not** rule out H2 (wrong retrieval unit) or H3 (soft gate can't hold a sparse
optimum even when rewarded); it *does* rule out "the tagger merely lacked the right gradient."
A **degenerate** A2 (C1 pass, C1b fail — collapses to one slot for both contexts) would mean the
divergence term needs pairing with an entropy floor, and routes to a design tweak, not a new
hypothesis.

---

### Leg H3 — ALGORITHM axis: hard / competitive selection

**Hypothesis:** a soft, end-to-end differentiable softmax gate cannot *hold* a sparse,
context-selective optimum — even correctly rewarded, gradient descent relaxes back toward the
uniform attractor (C2's exact ln(16) reproduction is evidence the soft landscape prefers it).
A structurally competitive selector (Gumbel-softmax with annealed temperature, or
straight-through top-k) forces sparsification independent of what downstream loss demands —
matching the biological reference (dentate-gyrus lateral inhibition / CA3 competitive retrieval;
see the H2 lit-pull, which also grounds H3's mechanism).

**Substrate requirement — MINIMAL knob recommended (not driver-inline).** Unlike H1, H3 changes
the selection **operator inside the shared `extract_cue_context` forward path**
(`e1_deep.py:430–445`). Reimplementing that path in the driver to swap in Gumbel/top-k is
error-prone and is itself a validity risk (driver-path drift from the real path). Recommend a
small `/implement-substrate` first: `sd016_cue_slot_tagger_selection: "soft" | "gumbel" |
"topk"` (default `"soft"` = bit-identical), with `gumbel` using an annealed temperature schedule
and `topk` a straight-through k-of-16, implemented once in `extract_cue_context`. So H3 routes
**`/implement-substrate` → `/queue-experiment`**. (Judgment call for the executing session: if it
prefers a driver-inline probe to avoid the build, it must assert the inline path is
bit-faithful to `extract_cue_context` for the soft control arm — otherwise C2 is not a valid
control. Recommendation stands with the knob.)

**Arms:**
- `A0_OFF` — legacy q.k (C2 control).
- `A1_tagger_soft` — Path-3 soft-softmax tagger = matched-budget baseline (898 ON arm).
- `A2_tagger_gumbel` — Path-3 tagger, Gumbel-softmax annealed selection.
- `A3_tagger_topk` — Path-3 tagger, straight-through top-k selection (k a small sub-sweep, e.g.
  k∈{1,2}).

**Null declaration:** if A2/A3 fail C1/C1b with readiness met, hard selection alone does not
break the saddle — implicating the *drive* (no reward for context-conditioning even with a
sparse selector, → H1) or the *representation* (→ H2), not the softness of the gate. A
C1-pass/C1b-fail top-k (selects a fixed slot for both contexts) is the "constant-peaky"
degeneracy C1b exists to catch and would say hard selection sparsifies but does not
*context-condition* — a genuine, informative discrimination against H3-alone.

---

### Leg H2 — REPRESENTATION axis: structured retrieval units (LONGER HORIZON — gated)

**Hypothesis:** the 16 undifferentiated `ContextMemory` slots are the wrong retrieval unit;
selection needs semantically-structured targets (hippocampal event/state/outcome-node indexing,
418m's original proposal) rather than arbitrary slots.

**NOT queueable now — this leg is a build behind unbuilt claims and an absent lit base.**
Verified this session against `claims.yaml`: the dependency claims are all `status:
provisional`, unbuilt — **ARC-006** (entities are sparse persistent bindable structures),
**ARC-007** (hippocampal replay of paths through residue terrain), **MECH-044** (hippocampal
relational binding/comparison), **MECH-267** (mode-conditioned hippocampal trajectory
proposals). And the autopsy's biological-reference triage found **no existing lit entry grounds
the competitive/local pattern-separation indexing mechanism** (existing `targeted_review_sd_016`
covers downstream *valuation* = leg B; `targeted_review_hippocampal_subfield_architecture`
covers CLS/consolidation, not indexing selection).

**Routing:** `/lit-pull` first (see §4) → a `/implement-substrate` scoping spike for the
structured-node representation informed by that review → only then a `/queue-experiment` leg.
Do **not** queue an H2 experiment in this portfolio round. Its null is deferred until it has a
buildable substrate; recording it here keeps the coverage honest (§5).

---

## 4. Companion routing — `/lit-pull` commission

Per the autopsy (routing part 1, user-ratified): commission a literature pull on **hippocampal
competitive / local retrieval-indexing mechanisms** — dentate-gyrus sparse coding via lateral
inhibition, CA3 pattern separation/completion, winner-take-all dynamics — as the biological
reference for what a fix mechanism should look like. This grounds **both H3** (why hard/competitive
selection is the biologically-faithful operator) **and H2** (what a structured retrieval unit
should be). Target: new entries under `targeted_review_sd_016` or a new
`targeted_review_hippocampal_pattern_separation` (lit-pull's own scoping call). PubMed MCP is
available this session but a lit-pull is its own skill/work-type — chipped, not run inline.

**`substrate_queue.json` amend (routing part 3): ALREADY APPLIED — no action.** The SD-016 entry
already reads `status: parked_pending_selection_mechanism_fix`, carries the updated `blocked_on`
(selection-mechanism language), the 898 `failure_record` entry (`resolved: open`), and the
`status_note_addendum_20260808`. Governance applied this in the 2026-08-08/09 cycle. This chip
deliberately does **not** touch the (multi-session-contended) `substrate_queue.json`.

---

## 5. Adversarial design audit (Step 2.5b.4 — BEFORE queuing)

**(i) Hypothesis-space coverage.** The autopsy names three live hypotheses; the portfolio tests
all three design axes (drive H1 / algorithm H3 near-term; representation H2 deferred-but-scoped).
The one axis the autopsy's four-layer table flags but the three sketches do **not** isolate is
**scale/capacity** (`scale: likely_insufficient_untested_directly` — the tagger got only 40 P1
episodes and an indirect gradient). Rather than add a fourth standalone leg that would be a bare
**power-bump of the braked design** (exactly what the re-derive brake refuses), the coverage gap
is closed **inside** H1 and H3: each carries a **matched-budget baseline arm** (`A1_tagger*`, the
898 ON arm at the *same* P1 budget as its experimental arms). A positive experimental arm over a
matched-budget baseline attributes to the *mechanism*; a shared null across baseline and
experimental arms is the signal to raise P1 budget in a *subsequent* round, not a hidden confound
in this one. This is the disciplined way to cover scale without a braked leg.

**(ii) Verdict aliasing.** Enumerated alias risks and their guards:
- *"selective" vs "constant-peaky"* (low entropy, no context-conditioning): guarded structurally
  by requiring **C1 AND C1b** on every leg — the exact anti-degeneracy pair 898 introduced.
- *"mechanism insufficient" vs "under-powered at this budget"*: guarded by the matched-budget
  baseline arm in each leg (above).
- *"selection genuinely uniform" vs "metric washes out real structure"* (the L1-of-means could
  cancel context structure that lives in higher moments): guarded by **recording the full
  per-context selection histograms** (`mean_w_safe[16]`, `mean_w_dang[16]`, and per-seed
  distributions), not only the scalar `sel_context_divergence`, so a null can be inspected for
  hidden structure rather than assumed absent. Record generously (per `/queue-experiment` §3c).
- *encoder-vs-selection* (the whole reason 418m was ambiguous): guarded by the mandatory
  readiness gate on every cell (§2).

**Genuine diversity check (not three flavours of one idea):** H1 changes the *objective* with the
*same* soft tagger; H3 changes the *operator* with the *same* objective; H2 changes the *unit
being selected over*. A null on all of H1+H3 with readiness met is itself a strong,
non-redundant result — it would elevate H2 (representation) from "longer-horizon option" to
"the remaining live hypothesis," which is exactly the discrimination a fan-out is for.

---

## 6. Execution plan (chips — see §7 for refs)

| # | Work | Skill | Blocking? | Chip |
|---|---|---|---|---|
| 1 | Lit-pull: hippocampal pattern-separation / competitive indexing | `/lit-pull` | grounds H2+H3; not blocking for H1 | `chip-20260809-sd016-litpull-patternsep` |
| 2 | H1 leg (drive) — driver-only, no build | `/queue-experiment` | ready now | `chip-20260809-sd016-h1-ctxdiv` |
| 3 | H3 leg (algorithm) — minimal selection-mode knob then experiment | `/implement-substrate` → `/queue-experiment` | ready now | `chip-20260809-sd016-h3-hardselect` |
| 4 | H2 leg (representation) — deferred behind chip 1 + unbuilt deps | `/lit-pull` result → `/implement-substrate` scope | **gated** on chip 1 | not chipped this round (see §7) |

H1 and H3 run in parallel (`machine_affinity: any`); neither depends on the other or on the
lit-pull. H2 is intentionally *not* chipped now — chipping a build behind four provisional claims
and an absent lit base would be a stale tracker; the lit-pull chip's own close is the trigger to
scope H2. That deferral is a deliberate coverage decision recorded in §5, not an omission.

---

## 7. Open decisions surfaced for the user (none block chips 1–3)

1. **H3 build-vs-inline:** this scope recommends a minimal `sd016_cue_slot_tagger_selection` knob
   over a driver-inline reimplementation, on validity grounds (§3 H3). The executing session may
   override with a bit-faithfulness assertion. *Default taken: knob.*
2. **H1 → knob promotion:** H1 is scoped as a driver-only probe; promotion to a live-path
   `sd016_context_divergence_weight` substrate knob is explicitly deferred until the probe
   confirms the mechanism (§3 H1). *Default taken: probe first.*
3. **H2 timing:** deferred behind the lit-pull rather than chipped now (§6). If the user wants H2
   scoped in parallel regardless of the lit base, that is a one-line instruction and a chip.

None of these are destructive or irreversible; all are ordinary design calls decided in-scope
per the headless contract. They are surfaced so a reviewer can redirect cheaply, not because they
block the near-term legs.
