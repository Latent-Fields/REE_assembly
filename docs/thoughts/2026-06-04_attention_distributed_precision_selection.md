# Attention as distributed precision-selection control

**Date:** 2026-06-04
**Status:** intake / unification note only. NOT a new active workstream. NOT a claim registration. NOT a change to REE-v3 acceptance criteria.
**Scope:** Reflective Ethical Engine version 3 (REE-v3) attention-equivalent substrate.
**Disposition:** containment-only for V3. A unifying *map* over existing mechanisms, not a new substrate. Do not add a generic attention module unless a concrete experiment exposes a specific missing attentional function.

---

## What this is

The user's verbatim intake note, captured as the canonical paragraph so future sessions touching precision routing / salience switching / boundary selection / cue recall / task-set / "an attention system" start from a substantive framing rather than re-deriving it — and, more importantly, so V4/V5 work does not accidentally build a second, parallel attention substrate next to the one REE already has under other names.

Not a plan. Not a claim. Not a substrate design.

---

## 1. Core observation

REE-v3 may appear to have little explicit "attention-system" work, but this is probably because attention has been apprehended under other names and distributed across existing precision, cueing, selection, and gating machinery.

**Do not add a separate generic attention module unless a specific experiment exposes a missing attentional function.**

Current interpretation:

> REE-v3 attention is **distributed precision-selection control**: what gets weighted, selected, maintained, recalled, routed, and allowed to steer action.

---

## 2. Existing attention-equivalent pieces

Claim anchors (all verified present in `docs/claims/claims.yaml` as of 2026-06-04; titles paraphrased here, see the registry for the exact text):

| Anchor | What it already does (the attention-equivalent function) |
|---|---|
| **ARC-005** | Control plane routes precision and modes — the architectural home of "attention = precision/mode routing". |
| **MECH-251** | `z_goal` projects a precision template vector, additively written to the E1 prior via the `dan_feedback` channel (top-down attentional template feedback). |
| **MECH-254** | At each E3 heartbeat boundary, a top-k selection over active E1/E2 latents decides what enters E3 deliberation; weights combine precision + `z_goal` template gain + noradrenergic bottom-up salience (the attentional bottleneck). |
| **MECH-255** | vmPFC value-content x dlPFC context-gated rule projection compiles the precision-space template (the template compiler behind goal-directed attention). |
| **MECH-259 / SD-032a** | Salience-network switch threshold + coordinator: precision-weighted salience over AIC/dACC/MCC/PCC-analog subdivisions fires a whole-system mode switch (salience-driven switching). |
| **MECH-261** | Mode-conditioned write gating — the operating-mode vector determines which substrates may write to E3 / episodic memory / policy / autonomic coupling (state-dependent attentional access control; generalises MECH-094). |
| **SD-057 / MECH-347** | Object-bound incentive salience + cue-triggered wanting / cue recall — a perceived cue retrieves its incentive token and biases `z_goal` toward that object before consumption (object-specific attentional priority + cue-driven capture). |
| **Goal-pipeline / GAP-7** | Object-bound incentive salience and cue-recall wanting, end-to-end (the L0–L9 pipeline that SD-057/MECH-347 sit inside). |
| **Rule/policy apprehension (ARC-062/063)** | Context-conditioned policy selection / rule-state persistence (task-set / attentional set). |

These should be read as **a distributed attention system**, not unrelated mechanisms.

---

## 3. Working translation table

| REE wording | Attention-system equivalent |
|---|---|
| precision routing | attentional gain / weighting |
| salience coordinator | salience-driven switching |
| boundary gate | attentional selection into deliberation |
| top-k latent selection | attentional bottleneck |
| `z_goal` template gain | goal-directed attention |
| cue recall | cue-driven attentional capture |
| incentive token | object-specific attentional priority |
| mode-conditioned write gate | state-dependent attentional access control |
| rule/policy context | task-set / attentional set |
| `dan_feedback` precision write | top-down attentional template feedback |

---

## 4. Distinction from transformer attention

Modern AI usage often treats "attention" as token-to-token weighting inside a transformer.

REE-v3's attention-equivalent is broader and more biological:

> Which latent content becomes behaviourally available, precision-weighted, selected into deliberation, maintained across time, recalled by cues, and permitted to affect action.

This is closer to attentional control / salience / precision / task-set selection than to a single neural-network attention layer. (Do not collapse the two; do not import a transformer attention block as "the attention system".)

---

## 5. The likely missing piece: a unifying map, not a substrate

The probable gap is **not a new substrate** but a unifying map:

> attention-control map = precision routing + salience switching + boundary selection + goal-template feedback + cue recall + mode-conditioned write gating.

This document is that map. Its job is to prevent accidental duplication later — especially when V4/V5 introduces richer object cognition, social attention, language, and explicit policy/rule apprehension, each of which will be tempted to grow its own attention machinery.

Where future work might otherwise duplicate attention, cite this note (and the anchors in §2) rather than building a parallel mechanism.

---

## 6. Version 3 containment

For REE-v3, attention remains **containment-only** unless a concrete experiment exposes a specific attention bottleneck. Do not expand the green-board closure path by adding a broad attention programme.

Instead:

* Treat attention as already distributed across existing mechanisms.
* Add cross-references where future work might otherwise duplicate attention.
* Only promote a new attention substrate if an experiment shows a **specific** failure such as:
  * relevant cue is perceived but never selected;
  * goal trace exists but cannot bias latent selection;
  * object token exists but cannot gain attentional priority;
  * policy/rule context exists but cannot maintain task-set;
  * salience switch fires but write access remains wrong.

Each of those failure modes maps to a specific anchor in §2 (so a failing experiment would point at *which* existing mechanism to enrich, not at a missing module): cue-not-selected -> MECH-347/SD-057; goal-cannot-bias -> MECH-251/254; token-no-priority -> SD-057; no-task-set -> ARC-062/063; switch-but-wrong-write -> MECH-259/SD-032a/MECH-261.

---

## 7. Current race relevance

This note does **not** alter the current nursery-to-forager bottleneck.

The immediate REE-v3 race remains:

> feeding -> protected consolidation -> token formation -> cue recall -> contact lift -> interoceptive authority if needed -> safe weaning -> autonomous foraging.

(See the cue-ecology intake `evidence/planning/thought_intake_2026-06-04_cue_ecology_weaning_nursery_to_forager.md` for that arc.)

Attention may become relevant **only if** cue recall fires but fails *because the cue/token is not selected into action-relevant control* — i.e. the "relevant cue is perceived but never selected" failure mode in §6, which would point at the MECH-254 boundary-gate / MECH-347 cue-recall path specifically. Until such a failure is observed, attention is a distributed explanatory layer already embedded in the assembly, not a new active workstream.

---

## Tracking

This note is the canonical paragraph for "REE's attention system". Until/unless a concrete experiment forces the issue:

* No claim registered in `claims.yaml`.
* No entry in `substrate_queue.json`.
* No closure-map node touched.
* No /lit-pull commissioned.
* Project-memory pointer at `~/.claude/projects/-Users-dgolden-REE-Working/memory/project_attention_distributed_precision_selection.md` so future sessions touching precision/salience/cue-recall/task-set topics surface this framing automatically.

If a future session is tempted to grow this into an attention substrate cluster, the gate to clear first is: **is there a concrete V3 problem this would unblock, and does the failing experiment fall outside all the §2 anchors' remit (i.e. is it genuinely a missing function rather than an under-tuned existing one)?** If yes, biology-first /lit-pull (attentional control, salience network, biased-competition, FIT/object-based attention) before any substrate-design memo.

Optional, un-started follow-up (user decision): drop a one-line "see this note" cross-reference into the §2 anchors' design docs so the map is reachable from each mechanism, not only top-down. Not done here — it touches governance docs and is not required for the note to do its job.
