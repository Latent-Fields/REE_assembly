# Failure autopsy — V3-EXQ-1017 (INV-104, ARC-138): regulatory anchoring vs matched auxiliary

**Generated:** 2026-09-09T09:37:25Z · **Scope:** single
**Status:** confirmed (user gate 2026-09-09, with red-team) · **Red-team verdict:** REFUTED
**Run:** `v3_exq_1017_..._20260909T054654Z_v3` · ree-cloud-2, 4m35s, 3 seeds × 7 arms
**Dry-run gate:** clean.

---

## 1. The finding

The pre-registered sensitivity witness **C0 failed** — no choice of P0a training objective moved the
adapter measure by the required 0.05 on any seed (0.0326 / 0.0078 / 0.0041) — short-circuiting the
verdict grid before either load-bearing criterion could carry a verdict.

**The driver's self-route is upheld in full, including its refusal to choose.** It routes to
`p0a_objective_invisible_to_adapter_dv` on the explicit ground that *"matched control matches
anchoring"* and *"the DV cannot see any objective"* are indistinguishable, and records neither.

**This autopsy first tried to resolve that ambiguity and was wrong.** The attempt was refuted at the
adversarial pass, the refutation independently verified, and recording that is part of the finding.

---

## 2. Why the first draft's inference failed

It rested on `own_target_r2_sense_path` being negative on the trained arms. That statistic cannot
bear the weight.

**Mechanism (confirmed by direct code read).** `_own_target_r2_sense` (driver `:497-510`) takes the
**trained** `resource_proximity_head` and applies it **cold to sense-path z with no refitting**,
while its encoder-path sibling (`:470-481`) evaluates the same head on the path it trained on. The
sense-path variant also **omits `pred_mean` / `pred_std`**, which the encoder-path variant returns —
so the one diagnostic that would expose a collapsed predictor is precisely the one not recorded.

**Scale (from the manifest's own `sense_vs_encoder_path`).** `mean_norm_encoder_path` 4.53–8.18
against `mean_norm_sense_path` 1.36–2.30 — the head is fed vectors at **0.23–0.35 of the norm it
trained on**. Through a sigmoid, that collapses the prediction toward its bias.

**Arithmetic (recomputed here).** For a constant predictor *c*, R² = −(c−μ)²/σ². Solved against each
recorded `target_mean` / `target_std`, that reproduces **all nine** observed negative values
(−0.0088 to −2.7215) with implied constants of **0.530, 0.552, 0.571, 0.596, 0.612, 0.654, 0.668,
0.669, 0.715** — squarely a sigmoid's mid-range. No claim about missing information is needed.

**The companion statistic was also misread.** cos θ between the paths is **0.686–0.855**, so the
0.749–0.835 relative residual is dominated by the **norm ratio**, not directional divergence. The
first draft's gloss — "about 80% of what the adapter reads is not the encoder's output" — was
backwards: 69–86% of the *direction* is the encoder's output, scaled down.

**And the evidence points the other way.** Sense-path norm is cleanly **arm-dependent**
(`sd070_default` 1.847 / 2.210 / 2.301, mean 2.119, against ~1.45 for both other trained arms,
separated on 3 of 3 seeds). If the sense path were blind to the objective its norm could not track
the objective this way. Decisively, the corpus already holds the disconfirming measurement:
**V3-EXQ-978 read sense-path r² 0.710 positive** using a probe *fit on that path*. The 978-vs-1017
gap is a **method** difference, not the magnitude difference the first draft claimed.

---

## 3. What the run does establish

**(a) Verified — the headroom gate certified the wrong contrast class.** `dv_headroom_pairwise_delta`
passed at 0.1745 against a 0.1 requirement, but its `measured_cells` are **all**
`ws250_pca − zworld_untrained` — a width/information-content contrast, not the objective-**choice**
contrast the load-bearing criteria test, every one of which came in under 0.033. A headroom
statistic computed over a different contrast class than its criterion certifies a capability that
criterion never uses.

**(b) New — the sense-path diagnostic is broken**, as in §2. Until that probe is refit on the path
it is evaluated on, **no conclusion about what sense-time z_world carries is supportable from this
driver family in either direction.**

---

## 4. What the run got right

The design is careful and this should not be lost in a FAIL. The matched-arbitrary control is
exacting — same head, same loss, same weight, same cadence, same training examples, differing only
in which scalar is piped through the channel, with a cell-permutation-invariant count functional
chosen so it cannot encode direction. All four GOV-MATCHAUX-1 matching properties were certified on
the training rollout itself (KS 0.1954; |r| 0.1778; oracle-action decodability elevation −0.0044;
own-target R² gap 0.1268).

**C0 earned its cost on the run where it fired.** Without it, a four-arm cluster spanning
0.669–0.679 would have been written up as evidence that organism-relevant anchoring does nothing.

---

## 5. Failure location (GOV-FAILLOC-1)

mechanism `established` · measures **`partial`** · environment `established` · **REE `false`** →
net **MEASURES**.

The manipulation was applied and certified and the environment behaved, but the measurement layer
carries a verified contrast-class defect and a broken diagnostic. **Not a REE FAILED read.** Whether
the P0a objective organises z_world remains fully **open**.

---

## 6. Claim dispositions

Both `non_contributory`. **Neither claim is weakened.** INV-104 stays `standard` / `candidate`;
ARC-138 keeps its existing `substrate_conditional` / `candidate` — an `implementation_phase: v4`
commitment probed only through a v3 proxy measure that could not settle its own question.

---

## 7. Routing

**`queue-experiment`** — a same-question re-run whose only changes are (i) refit the own-target probe
on the path it is evaluated on and record `pred_std`, (ii) compute headroom over the
objective-**choice** contrast class. Not another arm and not more seeds.

**Substrate: AMEND `dv-dynamic-range-precondition-class`** — not a create. The first draft
recommended a create and the adversarial pass correctly rejected it: the existing entry is
`implemented_pending_validation`, `degrading`, and its `substrate_paths` are already the same module
a new entry would have named. Its own `governance_2026_09_04` note records a **prior red-team
withdrawing a create in favour of an amend on this very entry** — and the first draft cited that
same episode for its `substrate_paths`-narrowing lesson while missing the create-vs-amend lesson,
which is the more directly applicable half.

Two additions to that entry: a headroom statistic must be computed over the **same contrast class**
as the criterion it protects; and a probe used as a readiness or diagnostic statistic must be
**fitted on the representation it is evaluated on** and must record its prediction spread.
Companion amendments come from V3-EXQ-999a and V3-EXQ-981a in the cluster artifact — **governance
should apply all three in one pass.**

**Re-derive brake: does not fire** (count 0 for both claims; first autopsy for each). A re-run is
explicitly allowed. **No fan-out** — the two live readings are separated by one unambiguous
measurement change, so GOV-FANOUT-1's own exemption applies.

---

## 8. Hypothesis-space registry (Step 9b)

The manifest carries `hypothesis_qid_status: "pre_registration_owed_at_queue_time"` — the authoring
session was refused the registry file by a then-active autopsy claim, correctly did not hand-edit
around it, and recorded that the adjudicating autopsy would register the question. This is that
autopsy. Registering `regulatory_anchoring_matched_aux` with `initial_frozen_count: 5`, **all legs
alive**: the four driver-declared hids plus `H-RA-dv-reads-sense-path-blind`.

The first draft registered that fifth leg as **confirmed**. The adversarial pass rejected it on
three grounds, all accepted: the state-mapping table routes a non-discriminating `non_contributory`
result with manifest `non_degenerate: false` to **alive**; `confirmed` requires `control_passed`
true and this run's *failed* criterion **is** its negative control; and the sense-path diagnostic has
no control condition at all — which is exactly why its scale artefact went undetected.

C3 passed but is uninterpretable: its non-degeneracy flag is conditioned on C0, and a flat C-vs-B
contrast behind a failed sensitivity witness is not evidence that the matched control matches
anchoring. **A passing criterion here is not a resolution.**

---

## 9. Cross-references not adjudicated

- **V3-EXQ-1016 was reserved but never materialised** — absent from the queue, no git history for
  the entry, no driver; its claim is now stale. The id is unburned and **V3-EXQ-1017 is the only
  completed run on this seam**. Nothing should be read as corroborated by 1016.
- **The z_world interface thread.** Stated carefully in light of the refutation: this run does
  **not** establish that sense-time z_world fails to carry encoder-trained content, and V3-EXQ-978's
  0.710 is evidence that it does. What is owed is the correctly-fitted measurement, not a
  conclusion.

---

## 10. Learning extracted

1. **A probe must be fitted on the representation it is evaluated on.** Applying a head trained on
   one path cold to another at a third of the input norm produces a collapsed constant predictor
   whose R² is arbitrarily negative — indistinguishable, from the manifest alone, from genuine
   absence of information. This cost this autopsy its first central inference.
2. **Record the prediction spread, not only the score.** One float would have made the collapse
   visible immediately — to the driver author and to this autopsy.
3. **A headroom gate certifies headroom for the contrast it is measured on**, not the contrast the
   criterion tests.
4. **A ratio of norms is not a measure of different content.** Decompose a residual into scale and
   angle before glossing it.
5. **When a driver declines to choose between two readings, test the decline before overriding it.**
   This driver's refusal was better calibrated than this autopsy's first attempt to resolve it.
6. A pre-registered sensitivity witness earns its cost precisely on the run where it fires.

---

## 11. Checks run

Step 7b: `fire_count: 0` after the C3 literature correction (C3 fired twice on an earlier draft;
both true positives, both acted on). Step 7c adversarial red-team: **REFUTED**, run on the **session
model (Opus 5)** — the preferred cross-model pass on Fable failed with a monthly spend limit on that
model and was re-spawned once without the override per the skill, so this is a **same-model** pass.
Recording provenance: complete, all always-core fields present.
