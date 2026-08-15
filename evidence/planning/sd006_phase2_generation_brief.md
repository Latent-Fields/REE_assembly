# SD-006 Phase 2 — Generation Decision Brief

**Status:** DECISION BRIEF — assembles facts, does not decide.
**Prepared:** 2026-08-15T07:34:17Z
**Session:** `modest-gauss-a38f51` (chip `chip-20260815-sd006-phase2-generation-brief`)
**Base:** REE_assembly `4089301534`
**Owning flag:** `GFLAG-0037` (`contested_disposition`, open) in `evidence/planning/governance_flags.v1.json`
**Route:** `/governance`
**Authority:** This document PROPOSES. No claim status, closure-node status, substrate_queue entry, or experiment was changed by the session that wrote it.

---

## 0. Why this brief exists

The 2026-08-15 D-002 orphan-V3-claim adjudication (REE_assembly `7478ffe8ad`, session
`orphan-v3-claims-adjudicate-6f88bd`) resolved three of four findings to a status change.
MECH-091 was deliberately left UNDETERMINED, because the fact that would decide it —
**the generation of SD-006 phase 2** — does not exist anywhere in the repo. In the
work-graph debt vocabulary that made it a `puzzle (known rules)`, not a
`complicated (buildable)`.

This brief gathers the missing facts. **Its headline finding is that the puzzle, as
posed, rests on a false premise**, and the decision governance actually faces is a
different and cheaper one than "V3 or V4".

---

## 1. HEADLINE — the premise is contradicted by the substrate

> **MECH-091's mechanism is not absent. It is implemented, wired, firing, and was measured
> on 2026-08-01 as the DOMINANT driver of E3 tick cadence in a real 53,063-step rollout.**

The hold on MECH-091 rests on this sentence, repeated in `claims.yaml` twice and in both
EXQ-133 reclassifications:

> "Without SD-006 phase 2 async execution there is no oscillatory clock phase to reset —
> the mechanism under test is absent, not failing."

Four independent artefacts contradict it. Re-verify each; none is a matter of interpretation.

### 1a. `phase_reset()` is built

[`ree-v3/ree_core/heartbeat/clock.py:182-199`](../../../ree-v3/ree_core/heartbeat/clock.py) —
`MultiRateClock.phase_reset()`, docstring "Phase reset on salient event (MECH-091)". The
module header at line 16 lists MECH-091 under **"Claims implemented"**. The reset is not
decorative: `advance()` at lines 149-155 branches on `_pending_phase_reset`, fires E3
immediately, and zeroes `_e3_phase_step`. There is a real phase counter, and it is really reset.

### 1b. It is wired into the agent

[`ree-v3/ree_core/agent.py:9903`](../../../ree-v3/ree_core/agent.py) — `self.clock.phase_reset()`,
comment `# MECH-091: harm is salient -> phase reset`. Clock constructed at `agent.py:402`.

### 1c. It was MEASURED, and it dominates

[`evidence/planning/diagnostic_arc071_e3_reselection_probe_2026-08-01.md`](./diagnostic_arc071_e3_reselection_probe_2026-08-01.md)
drove a real 53,063-step hazard-exposed rollout and found (lines 36-45, 215-232):

> "**The dominant trigger is instead MECH-091's unconditional `clock.phase_reset()` on every
> `harm_signal < 0` step** … this forces an E3 tick independent of the periodic counter."

Measured consequence: `premature_reselection` of 36.8% / 41.4% / 55.1% at `chunk_max_size`
5 / 8 / 15. The effect is large enough that a *separate* substrate flag
(`use_e3_reselection_shortcircuit`, [`ree_core/utils/config.py:4481-4516`](../../../ree-v3/ree_core/utils/config.py))
was designed around it, whose comment states MECH-091 "must NEVER be swallowed."

A mechanism that sets the effective cadence of the loop it targets is not absent.

### 1d. The claim's own text says the ANN form does not need async

`claims.yaml` MECH-091 `functional_restatement`:

> "In an ANN substrate, implemented as an **explicit cycle-boundary marker triggered by
> salient events — not as oscillatory phase reset**. The biological mechanism (thalamic-driven
> phase reset …) is one implementation; **it is not required in the ANN substrate**."

And the architecture doc that owns the hold,
[`docs/architecture/control_plane_heartbeat.md:211`](../../docs/architecture/control_plane_heartbeat.md),
explicitly sanctions exactly this:

> "experiments can target the *functional analog* … the functional requirement (rate
> separation, temporal batching, commitment gating, **cycle resync**, offline replay) is
> implementable in the current synchronous ANN substrate as a simplified proxy. These
> functional-analog experiments are **a valid V3 pre-test** before full SD-006 async execution."

"Cycle resync" is MECH-091. The doc's *own* rule permits the V3 test that the hold forbids.
The rule the doc actually states is narrower than how it has been applied: null-by-construction
applies to experiments targeting the **biological mechanism**, and MECH-091's ANN form is
declared, by the claim itself, not to be that.

**Confidence: high on 1a-1c (direct code and measurement). Moderate on 1d** — it is a reading
of two documents, and governance may weigh them differently. See §6 for the counter-argument.

---

## 2. What SD-006 phase 2 actually requires — and why "phase 2" is not one thing

### 2a. The spec offers three options; the recommended one is largely built

[`docs/architecture/control_plane_heartbeat.md:201-209`](../../docs/architecture/control_plane_heartbeat.md)
(content unchanged since 2026-03-21 — later commits to that file were nav/sidebar only):

| # | Option | Spec's own verdict | Built? |
|---|---|---|---|
| 1 | Separate threads + message-passing queues | "Cons: thread-safety complexity, **GIL limitations in Python**" | No |
| 2 | Time-multiplexed, explicit rate params | "Simpler than threading; **less faithful**" | **YES — this is phase 1** |
| 3 | **Hierarchical temporal abstraction (HTA)** — E3 receives temporally-abstracted inputs (theta-cycle summaries, MECH-089) rather than raw E1/E2 output | **"Recommendation for V3: HTA (option 3)"** | **substantially YES** |

Option 3 is the recommended design, and its defining mechanism exists:
[`ree-v3/ree_core/latent/theta_buffer.py:1-14`](../../../ree-v3/ree_core/latent/theta_buffer.py)
— *"ThetaBuffer — Cross-Rate Integration for SD-006 (MECH-089). E3 does NOT receive raw
E1/E2 output. It receives temporally-abstracted theta-cycle summaries of z_world."* That is
option 3's text, implemented. It has since been extended (SD-100 phase-aware summary,
`use_theta_phase_weighted_summary`, [`sd_100_theta_buffer_phase_aware_summary.md`](../../docs/architecture/sd_100_theta_buffer_phase_aware_summary.md)).

### 2b. The conflation

[`clock.py:32`](../../../ree-v3/ree_core/heartbeat/clock.py) defines the deferral as:

> "Note: phase 2 (**full HTA with separate goroutines/threads**) is deferred per spec §3/SD-006."

This single phrase **fuses the recommended option 3 with the rejected option 1**. The HTA half
is built; the threading half is what remains, and the spec never recommended it. Every
downstream "blocked on SD-006 phase 2" inherits this fused definition without distinguishing
the halves.

**So "is SD-006 phase 2 V3 or V4?" is under-specified.** The answerable questions are:

- **(i)** True concurrent execution (threads / event loop) — genuinely unbuilt, genuinely undesigned, and the one thing option 1's GIL caveat warns about. This is what ARC-023 needs.
- **(ii)** HTA temporal-grain abstraction — substantially built (ThetaBuffer + SD-100).
- **(iii)** The specific unwired bits of MECH-091 — see §2c. Small, concrete, and *not* async at all.

### 2c. The real, concrete MECH-091 gap: two of three triggers are unwired

MECH-091 names three salient events (`claims.yaml` `notes`, and `clock.py:186`):
**task completion, unexpected harm, commitment-boundary crossing.**

`grep` for `phase_reset` across `ree_core/` returns exactly **one** call site
(`agent.py:9903`), gated on `harm_signal < 0`. **Completion and commitment-boundary
crossing are not wired.** The ARC-071 diagnostic independently corroborates this at line 18
("`harm_signal < 0` is the sole trigger for MECH-091's `clock.phase_reset()`").

This is the concrete substrate deficit for MECH-091 — and it is
`complicated (buildable)`, not blocked on anything. Both missing triggers already exist as
events elsewhere in the substrate (hippocampal completion drives BetaGate release;
commitment entry/exit is the MECH-090 beta-gate boundary).

**A no-reset control is constructible today.** MECH-091's `what_would_answer` asks for a
comparison "compared to a no-reset control where partial integration measurably occurs."
Under phase 1 that control is simply `phase_reset()` disabled — and the ARC-071 data shows
the two conditions differ substantially in E3 cadence. The experiment is constructible on
the current substrate; it was not constructible in the form EXQ-133 attempted, which
measured latent divergence as a *proxy* rather than the cycle-boundary DV the claim names.

---

## 3. Blast radius

Swept all 1,012 claims in `claims.yaml`, all `evidence/planning/*_plan.md` frontmatter, and
all 157 `substrate_queue.json` entries.

### 3a. Hard-blocked — the decision changes their fate (6)

| Claim | Type | Status | phase | How it is blocked |
|---|---|---|---|---|
| **MECH-091** | mechanism_hypothesis | candidate | v3 | Originating claim. EXQ-133 ×2 non_contributory. **Per §1, may not be blocked at all.** |
| **ARC-023** | **architectural_commitment** | candidate | v3 | `what_would_answer` NON-DEGENERACY PRECONDITION on phase 2; EXQ-131 reclassified INCONCLUSIVE ("E3 output freeze artifact"). **Genuinely needs (i) true async.** |
| **MECH-092** | mechanism_hypothesis | provisional | v3 | Triggering half CONFIRMED (V3-EXQ-761 PASS); **consolidation-benefit half** gated. EXQ-136 non_contributory. Promote-to-active gated. |
| **MECH-097** | mechanism_hypothesis | candidate | — | "Requeue after SD-006 phase 2." Blocked *via* MECH-091 → **unblocks with MECH-091**. |
| **MECH-291** | mechanism_hypothesis | candidate | v3 | "Blocked on SD-006 for the quiescent path"; carries a ready-made falsifiable factorial design "after SD-006 implementation". Waking-mode half independent. |
| **MECH-057a** | mechanism_hypothesis | provisional | — | "Full test requires ARC-023 + MECH-090 + SD-006." |

### 3b. Downstream — blocked transitively via MECH-092's consolidation half (3)

- **MECH-165** (substrate_conditional) — states that while MECH-092 is gated on "unbuilt SD-006 phase-2 async execution", **"no real-SWS-phase (non-proxy) test of MECH-165 is possible at all."**
- **MECH-209** — needs MECH-092's consolidation-benefit half.
- **MECH-122** (provisional) — `depends_on: [MECH-030, MECH-089, SD-006]`; ThetaBuffer bidirectional, already marked "V4 design needed" in the V3/V4 boundary doc.

### 3c. Explicit NON-dependents — negative controls (4)

These matter: they show the repo has already reasoned case-by-case about what needs phase 2,
and repeatedly concluded "not this one."

- **MECH-107** — *"does NOT require SD-006 phase 2 async execution, unlike its formal dependencies MECH-091 and ARC-023 — **do not gate this test on SD-006 phase 2 landing**."*
- **MECH-290** — "does not require SD-006 (async execution) … runs at the same synchronous completion event."
- **SD-038** — "Implementation does not require SD-006 (runs synchronously in waking CEM)."
- **ARC-032**, **ARC-112** — corollary mentions only, no dependency.

### 3d. Related — a live claim about whether SD-006 achieves its purpose

**Q-081** (open_question, candidate, v3): *"Does REE's configured multi-rate execution produce
SHARED cross-stream organisation, or only configured rate separation?"* — its notes call this
*"a live risk to SD-006's stated purpose and is currently untested."* Two design docs exist
(`q081_landmark_removal_arm_design.md`, `q081_surrogate_null_design.md`). Governance should
know a phase-2 decision interacts with an open question about whether phase 1 delivers what
it claims.

### 3e. Live inconsistency worth resolving in the same pass

Two artefacts treat SD-006 as **complete**, with no phase-2 caveat at all:

- [`docs/architecture/v3_v4_transition_boundary.md:57`](../../docs/architecture/v3_v4_transition_boundary.md) — V3-Prerequisites-for-V4 table: `Multi-rate execution | SD-006 | EXQ-052b (PASS) | **PASS**`.
- `claims.yaml` **MECH-030** — "multi-rate execution (SD-006, **already PASSED** per EXQ-052b)".

Against `claims.yaml` MECH-091/ARC-023/MECH-092, which treat SD-006 as half-built. Whatever
governance decides, one of these two readings should be corrected.

**Totals: 6 hard-blocked + 3 downstream = 9 claims, of which one (ARC-023) is an
architectural_commitment.** This is a nine-claim decision, not a one-claim decision.

**Evidence state of the two headline claims** (`claim_evidence.v1.json`): both are
`plausible_unproven` — MECH-091 `lit_conf 0.826 / exp_conf 0.125` (1 experimental entry),
ARC-023 `lit_conf 0.806 / exp_conf 0.0` (**zero** experimental entries). Literature-strong,
experimentally empty. The block is what keeps them there.

---

## 4. Has anyone ever stated its generation?

**No unconditional statement exists. Three artefacts give three different readings** — which
is itself the finding.

| Artefact | What it says | Reading |
|---|---|---|
| [`docs/roadmap.md:4386-4389`](../../docs/roadmap.md), under **"Open Questions"** | *"**SD-006 phase 2**: time-multiplexed multi-rate is phase 1; true asynchronous execution (thread-based or event-loop) is still open. HTA … is the recommended direction **but not yet designed**."* | **No generation assigned.** Classified as an open question and, notably, as *undesigned*. |
| [`commitment_closure_plan.md`](./commitment_closure_plan.md) — line 409 table, line 647 prose (under heading *"V4 deferrals (genuinely out of V3 scope)"*), line 666 status table | *"low (V4 deferred)"* … *"deferred to V4 **unless SD-006 phase 2 lands earlier**"* … *"deferred until SD-006 phase 2 lands **or** V4 substrate redesign occurs"* … status `deferred V4` | **GAP-7 is V4-deferred — but explicitly CONDITIONALLY**, leaving open that phase 2 could land in V3. It assigns a generation to the *gap*, not to *phase 2*. |
| [`v3_v4_transition_boundary.md:57`](../../docs/architecture/v3_v4_transition_boundary.md) | `Multi-rate execution \| SD-006 \| EXQ-052b (PASS) \| PASS` | **SD-006 is a SATISFIED V3 prerequisite.** No phase-2 caveat anywhere in the doc. |

**So the adjudication's finding stands, with one refinement.** It said "no artefact says V3
and none says V4." More precisely: the closure plan *does* say V4, but conditionally and about
the *gap*; the roadmap says *undecided and undesigned*; the boundary doc says *done*. This is
not a lost pointer — it is three artefacts that were never reconciled.

**One of them is now stale.** roadmap.md's "HTA … not yet designed" is contradicted by
§2a — HTA's defining mechanism (ThetaBuffer) is built and has since been extended by SD-100.

---

## 5. Both branches, prepared

Governance need only pick. **Neither branch is extra work later.**

### Branch V3 — "phase 2 is V3 scope"

**(a) Add to `evidence/planning/substrate_queue.json` `queue`:**

```json
{
  "sd_id": "SD-006-phase2",
  "title": "SD-006 phase 2: asynchronous multi-rate loop execution (E1/E2/E3 true concurrency)",
  "status": "queued",
  "ready": false,
  "ready_blocked_by": "Design not written. control_plane_heartbeat.md:201-209 offers three options and recommends HTA (option 3), whose defining mechanism (MECH-089 ThetaBuffer, theta_buffer.py) is ALREADY BUILT; what remains unbuilt is option 1 (threads/event loop), which the spec itself flags for GIL limitations. A design pass must first decide whether phase 2 means (i) true concurrency, (ii) further HTA depth, or both -- clock.py:32 currently fuses them as 'full HTA with separate goroutines/threads'. See evidence/planning/sd006_phase2_generation_brief.md section 2.",
  "unblocks_claims": ["ARC-023", "MECH-092", "MECH-291", "MECH-057a", "MECH-122", "MECH-165", "MECH-209"],
  "priority": 2,
  "added_session": "<governance session id>",
  "design_doc": "docs/architecture/control_plane_heartbeat.md",
  "depends_on_unresolved": [],
  "implementation_hint": "SCOPE FIRST, BUILD SECOND. Step 1: split 'phase 2' into (i) true concurrent execution and (ii) HTA temporal-grain depth, and record which claims need which -- ARC-023's non-degeneracy precondition is specifically about rate separation surviving REAL asynchronous load, so it needs (i); MECH-092's consolidation-benefit half may be satisfiable by (ii). Step 2: if (i) is in scope, evaluate an event loop / asyncio against threads -- the spec's option 1 GIL caveat still applies and torch releases the GIL only inside kernels. Step 3: preserve bit-identical default-off behaviour (the substrate convention -- see use_theta_phase_weighted_summary, breath_period=0). NOTE: MECH-091 is NOT in unblocks_claims -- per brief section 1 it appears testable on phase 1 today; if governance accepts that, it routes separately (see the MECH-091 entry below)."
}
```

**(b) Closure-node change:** `commitment_closure:GAP-7` `status: deferred` -> `blocked`;
`last_updated: 2026-08-15`; clear `needs_review`.

**(c) MEASURED closure effect — GAP-7 ONLY.** A/B regeneration of
`scripts/generate_closure_snapshot.py` on one base (REE_assembly `4089301534`), in an
isolated detached worktree, single-node flip, worktree removed afterwards and the main
checkout verified free of leakage. **Not** differenced against `docs/closure_dashboard.md`.

| Metric | A (as-is) | B (GAP-7 `blocked`) | Δ |
|---|---|---|---|
| Weighted V3 progress | **71.9%** | **71.3%** | **−0.6 pp** |
| Non-deferred denominator | 94 | 95 | +1 |
| Remaining | 32 | 33 | +1 |
| Deferred | 13 | 12 | −1 |
| `blocked` tally | 11 | 12 | +1 |
| Done | 62 | 62 | unchanged |

The A arm reproduces the adjudication's baseline exactly (71.9% / 94), which validates the
measurement. This isolates the per-node attribution the earlier 3-node batch measurement
(71.9%/94 → 70.0%/97) left unseparated.

### Branch V4 — "phase 2 is V4 scope"

**(a) Owning plan.** No V4 plan currently owns SD-006. The correct owner is
[`docs/architecture/v3_v4_transition_boundary.md`](../../docs/architecture/v3_v4_transition_boundary.md),
whose "V3 Prerequisites for V4" table already carries MECH-122 as "ThetaBuffer bidirectional
— V4 design needed" — the nearest existing row. **Add a cross_plan_link** from
`commitment_closure:GAP-7` to that doc, and **correct line 57**, which currently reads SD-006
as an unqualified `PASS` and would otherwise contradict a V4 deferral outright (§3e).

**(b) `claims.yaml` correction — PROPOSAL ONLY, not applied:**

```yaml
# MECH-091 (~line 11117)
- implementation_phase: v3
+ implementation_phase: v4
```

Same correction applies to **ARC-023** (`implementation_phase: v3`) and, for the
consolidation-benefit half only, **MECH-092** — otherwise the V4 branch leaves the identical
orphan pattern on two more claims, including an architectural_commitment, and D-002 will
resurface them.

**(c) Closure effect:** none. GAP-7 stays `deferred`, progress stays 71.9%/94. `needs_review`
is cleared with a resolution note recording the decision.

---

## 6. Recommendation (RECOMMENDATION, NOT A DECISION)

> **Recommended: neither branch as posed. SPLIT the question — route MECH-091 to V3 as a small
> buildable, and send SD-006 phase 2 (true concurrency) to V4.**

### Reasoning

**1. The V3-vs-V4 framing inherits the false premise.** Both branches assume MECH-091 is
blocked on phase 2. §1 shows the mechanism is built, wired, firing, and measured as the
dominant E3-cadence driver. Choosing either branch as posed leaves MECH-091 gated on
something it appears not to need — the V4 branch permanently.

**2. MECH-091's real gap is small and buildable.** Two of three salient-event triggers unwired
(§2c). That is `complicated (buildable)`, not `complex (probe-gated)`. Both events already
exist in the substrate.

**3. The spec never recommended the unbuilt half.** Its V3 recommendation was HTA (option 3),
which is substantially built. What remains is option 1 (threads), flagged by the spec itself
for GIL limitations — a poor fit for a torch-based substrate and a reasonable V4 item.

**4. It splits the blast radius favourably.** MECH-091 + MECH-097 (2 claims) unblock in V3 at
small cost. ARC-023, MECH-092-consolidation, MECH-291-quiescent, MECH-057a, and the three
downstream claims stay honestly phase-2-gated — ARC-023's precondition is specifically that
rate separation survive *real* asynchronous load, which no phase-1 test can supply.

**5. It is the cheapest way to buy information.** MECH-091 is `lit_conf 0.826 / exp_conf 0.125`
— literature-strong, experimentally empty, and has been so since March. A small wiring fix
converts a permanently-parked claim into a testable one.

### Concretely

| Item | Route | Closure effect |
|---|---|---|
| **MECH-091** — wire completion + commitment-crossing triggers into `phase_reset()`; then a V3 experiment using the ON/OFF no-reset control the claim already specifies | `/implement-substrate`, then `/queue-experiment`. `commitment_closure:GAP-7` -> `blocked` on the *wiring*, `blocking_external` corrected from "SD-006 phase 2 async heartbeat" | **−0.6 pp, +1 denominator** (§5c) |
| **SD-006 phase 2 (true concurrency)** | V4; queue entry per §5 Branch V3(a) with `priority` lowered, OR the V4 cross_plan_link per Branch V4(a) | none |
| **ARC-023, MECH-092-consolidation, MECH-291-quiescent, MECH-057a** | Stay phase-2-gated. Correct `implementation_phase` v3 -> v4 on ARC-023 (proposal) | none |
| **§3e inconsistency** | Correct either `v3_v4_transition_boundary.md:57` or the MECH-091/ARC-023/MECH-092 gating text — they cannot both be right | none |

### The honest counter-argument, stated so governance can weigh it

ARC-023's EXQ-131 diagnosis says time-multiplexed polling produces an **"E3 output freeze
artifact"** — stale E3 state driving `var_harm_eval_on` to 1.05e-7, "uninformative by
construction." If that staleness also swallows MECH-091's phase reset, the recommendation is
wrong and the hold was right.

Two reasons to think it does not, and one reason to check:

- The two claims measure different things. EXQ-131's artefact is about **rate-separation
  discriminability** — whether E3's *output* distinguishes conditions. MECH-091 is about
  **cycle-boundary timing** — *when* E3 fires. The ARC-071 probe measured the timing channel
  directly and found the reset dominant, so the timing channel is demonstrably not frozen.
- MECH-091's own `functional_restatement` and `control_plane_heartbeat.md:211` both say the
  ANN functional analog is the target and is testable now (§1d).
- **Worth one cheap check before building**: confirm that the DV MECH-091's
  `what_would_answer` names — "no partial-integration artefacts straddling a salient event"
  — is observable on phase 1, i.e. that E3's *integration* of post-event harm estimates is
  measurable and not itself absorbed by staleness. That is a `puzzle (known rules)`: one
  reading of the E3 integration path, not an experiment. If it fails, the V4 branch of §5
  is the fallback and nothing in this brief is wasted.

**A note on this brief's own status.** §1a-1c are direct code reads and a logged measurement,
and should be treated as established. §1d, §2a-2b and the recommendation are *inference from
documents*, offered for governance to weigh, not established fact.

---

## 7. What this brief did NOT do (authority boundary)

- Did **not** edit `claims.yaml` — MECH-091 / ARC-023 `implementation_phase` corrections are proposals.
- Did **not** change any closure node's status, add an `owner_exq`, or clear `needs_review`.
- Did **not** add the `substrate_queue.json` entry — adding it *is* the V3 decision.
- Did **not** queue any experiment.
- Did **not** resolve `GFLAG-0037` — resolving it is the governance decision. A pointer to
  this brief was added to the flag as a note; the flag is now decision-ready.
- Did **not** re-adjudicate MECH-316 / MECH-317 / MECH-314a (settled and landed).
