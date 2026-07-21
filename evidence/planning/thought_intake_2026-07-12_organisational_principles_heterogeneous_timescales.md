# Thought Intake — Organisational principles of cognition across heterogeneous timescales

**Date of thought:** 2026-07-12
**Intake written:** 2026-07-21
**Raw thought file:** `docs/thoughts/2026-07-12_organisational_principles_of_cognition_across_heterogeneous_timescales.md`
**Session:** `sad-newton-00451d` (thought-intake ingestion, 2026-07-21)
**Source:** *Shared spatial and temporal principles govern connectome dynamics across timescales*, PNAS, DOI `10.1073/pnas.2535464123`
**Status:** structured intake written; candidate claims NOT yet registered (a concurrent session held the `claims.yaml` claim — registration is the next step).
**Promotes/demotes:** nothing. Claim-generative intake material, not canon.

## Authorship note

The raw thought is the user's, and it is already near-intake quality — it contains its own self-correction, its own literature programme, and its own outcome taxonomy. This intake does not restate it. Its job is the **already-owned vs genuinely-new split**, the cross-reference into `claims.yaml`, and the routing.

The load-bearing move is the user's, and it is a *correction of the obvious reading*: the paper's relevance is **not** "REE should add multiple timescales" (REE already has them, by founding substrate decision), but "does REE's existing heterogeneity exhibit *shared organisation*, or only *configured* rate separation?"

## The central move (verbatim from the raw thought)

> What organisational principles allow heterogeneous and asynchronous cognitive processes to remain parts of one integrated system without collapsing into either lockstep synchrony or unrelated modular activity?

and the framing that follows from it:

> REE is a federation of asynchronous, partially independent cognitive streams coordinated by shared organisational constraints.

with the anti-collapse qualification that keeps it honest:

> Successful integration should preserve functionally necessary differences among streams rather than making their dynamics identical.

## Already owned — cross-reference, do NOT re-assert

The raw thought's own review found REE already implements most of the *mechanism* layer. Confirmed against `claims.yaml`:

| Element in the thought | Existing claim(s) |
|---|---|
| E1/E2/E3 at characteristic rates, not lockstep | **SD-006** (verbatim the thought's quote) |
| Three BG-like loops at characteristic thalamic heartbeat rates | **ARC-023** |
| Salient events phase-reset the E3 heartbeat clock | **MECH-091** |
| Quiescent-cycle replay / offline integration | **MECH-092**, **MECH-018**, **MECH-030**, **MECH-291** (waking vs quiescent CEM profiles) |
| Two-level event-boundary detector + nested segment ids | **MECH-288** (substrate side), **MECH-321** (rollout-side consumer) |
| Event-gated frontal write at goal-instantiation | **MECH-298** |
| Engines are irreducible; none collapses into another | **ARC-025** |
| Control plane keeps orthogonal tonic/phasic axes, no scalar collapse | **MECH-063** |
| Error signals are incommensurable and must not be averaged | **MECH-069** |
| Harm stream separate from `z_world`; s/a split protected | **SD-010**, **SD-011**, **ARC-027**, **ARC-033** |
| Valence vector-valued, no scalar collapse | **MECH-035** |
| Residue persists, cannot be erased, only integrated | **INV-004**, **INV-006**, **ARC-013** |
| Responsibility arises through commitment, not prediction | **INV-012** |

So candidate principles 1, 2 (partly), 3 (partly), 5, 6, 8 and 9 of the raw thought are **descriptions of existing REE commitments**, not new proposals. They should be cited, not registered.

## Genuinely new — four things

### N1. Configured rate-separation is not shared organisation (the sharp empirical gap)

This is the thought's strongest contribution and it is a **diagnostic gap in the existing claim set**. SD-006 asserts that E1/E2/E3 *run* at characteristic rates. Nothing in the registry asserts — or tests — that the heterogeneous streams thereby exhibit **recurrent cross-stream structure**. The raw thought states the discriminator explicitly:

> A positive finding would require more than demonstrating that processes update at different configured rates. It would require recurrent cross-stream structure not trivially guaranteed by those settings.

The outcome taxonomy (A shared organisation / B wired-gates-only / C unrelated / D too-much-sharing-collapses / E event-relative beats clock-relative) is already a usable verdict grid, and B is the null that most experiments of this shape would fail to exclude.

**Why this matters beyond bookkeeping:** if the answer is C, REE has an *integration gap* that its multi-rate substrate decision was assumed to have addressed. That is a live risk to SD-006's stated purpose, and it is currently untested.

### N2. Event-relative coordination may be REE's effective temporal grammar (Outcome E)

A specific, cheap, falsifiable sub-hypothesis: streams are more strongly coordinated when aligned on **event boundaries / commitment onset / interruption / completion / offline transitions** than when aligned on wall-clock timestep. REE already emits all the required landmarks (MECH-288 boundary pulses, the beta commitment gate, mode transitions, sleep-phase markers), so this is testable **retrospectively on existing telemetry** with no substrate change.

This sharpens MECH-288/MECH-321 from "a detector exists and a consumer uses it" to "the boundary stream is the coordination substrate for the whole federation."

### N3. Protected non-equivalence as a joint criterion with integration

Individually, integration (ARC-025 irreducibility) and anti-collapse (MECH-063, MECH-069, SD-011, MECH-035) are both owned. What is **not** owned is the statement that an adequate theory must satisfy **both at once**, with a quantity in between — that there is a *band* of cross-stream similarity that is healthy, below which the system is fragmented and above which it has collapsed. Outcome D ("too much shared organisation causes collapse") makes this measurable rather than rhetorical.

### N4. The federation/heterarchy framing itself

REE as neither monolith nor module-collection but a **federation coordinated by shared constraints**, closer to a heterarchy than a hierarchy. This is an architectural-framing claim. It is arguably implied by ARC-025 + MECH-063 + SD-010/011 taken together, but it is nowhere stated as a claim, and it is the frame that makes N1–N3 one programme rather than three unrelated probes.

## Explicitly NOT new (guard against over-registration)

- Multi-timescale processing as such. The raw thought says so itself, twice. Do not register anything that reads as "REE should have heterogeneous timescales."
- Any oscillatory / cross-frequency-coupling mechanism. The thought is explicit that the aim is abstract coupling principles, not importing oscillations.
- DLIF. The thought deliberately separates itself from the Dynamic Latent Information Field line (already answered-negative in the registry as a unifying mathematical object). Cross-reference as orthogonal; **do not merge**.

## Candidate claims (for registration at digestion — IDs to be assigned then)

1. **Configured multi-rate execution does not entail shared cross-stream organisation.** *Candidate, diagnostic.* SD-006 guarantees characteristic rates; it does not guarantee that E1/E2/E3, harm, goal, salience, hippocampal and control signals occupy recurrent system-level configurations or exhibit homologous transition motifs. *Falsifier shape:* recurrent-state / transition-matrix / cross-stream-lag analysis over existing telemetry, with the discriminating comparison **emergent shared structure vs structure trivially implied by the configured rates and wired gates** (Outcome A vs Outcome B). *Non-degeneracy guard:* the cross-stream statistic must show live variance across arms/seeds and must be computed against a rate-matched shuffle control — a result that merely recovers the configured update periods is Outcome B, not a PASS. *Type:* diagnostic / open question over existing substrate. *Cross-ref:* SD-006, ARC-023, ARC-025, MECH-288, MECH-321, MECH-091.

2. **Event-relative coordination exceeds clock-relative coordination (Outcome E).** *Candidate.* Cross-stream alignment measured around event boundaries, commitment onset, interruption, completion and offline transitions is stronger than alignment by wall-clock timestep. *Falsifier:* an event-triggered-average / alignment statistic computed both event-locked and clock-locked on the same traces; PASS requires event-locked alignment to exceed clock-locked by a margin scaled on the SD of the delta plus an absolute floor. *Non-degeneracy guard:* boundary pulses must be non-degenerate (boundary rate not floor- or ceiling-pinned) — a segmenter emitting boundaries every step or never makes the comparison vacuous. *Type:* MECH-flavoured, retrospective-testable. *Cross-ref:* MECH-288, MECH-321, MECH-091, MECH-298, beta commitment gate.

3. **Integration and protected non-equivalence are jointly necessary; cross-stream similarity has a viable band.** *Candidate.* Too little shared organisation is fragmentation; too much is representational collapse (the failure SD-011, MECH-063, MECH-069 and MECH-035 each guard against on one axis). *Falsifier:* an ablation series (remove event broadcasts / remove mode conditioning / remove commitment landmarks / remove residue feedback / force lockstep / randomise rates / collapse the harm streams) showing a non-monotonic relation between cross-stream similarity and task/anti-collapse function. *Non-degeneracy guard:* at least one ablation must move the similarity statistic measurably, or the series tested nothing. *Type:* ARC/INV-flavoured architectural constraint. *Cross-ref:* ARC-025, MECH-063, MECH-069, SD-010, SD-011, MECH-035.

4. **(Framing, lower priority) REE is a federation/heterarchy of partially independent streams under shared constraints.** *Candidate, framing.* Register only if it earns its keep as the parent node for 1–3; otherwise leave as intake prose. *Cross-ref:* ARC-025, MECH-063, SD-006.

## Routing

- **Cheapest first move, and the one the thought itself recommends: retrospective telemetry audit, not a new experiment.** Before anything is queued, answer open question 6 of the raw thought — *do REE's current logs contain sufficient telemetry to test this?* The instrumentation list (E1 hidden state, E2 PE, E3 candidate scores + commitment state, `z_self`, `z_world`, `z_harm_s`, `z_harm_a`, `z_goal`, `operating_mode`, beta, boundary broadcasts, hippocampal proposals, residue updates, offline phase markers) is the audit checklist. This is `complicated (buildable)` — a scoping spike, not a probe.
- **Literature:** the 10-search programme is a well-formed `/lit-pull` brief. Searches 2 (metastability / coordination dynamics), 3 (event segmentation across nested timescales) and 6 (homologous dynamics across heterogeneous state spaces — conjugacy, manifold alignment, Koopman) are the load-bearing ones for candidate claims 1–3. Search 10 (substrate-independent organisational invariants) should follow, not precede, per the thought.
- **Experiments:** none yet. Candidate claim 2 is the first that could be queued, and only after the telemetry audit confirms the signals exist. Do not put this on the V3 critical path — the raw thought is explicit that it does not justify changing it.
- **DLIF:** cross-reference only, orthogonal line.

## Next steps

1. Register candidate claims 1–3 (and 4 if it earns it) in `claims.yaml` at `status: candidate`, wired via `depends_on` into SD-006 / ARC-025 / MECH-288 / MECH-063. **Deferred from this session** — a concurrent session held the `claims.yaml` claim.
2. Mark the raw thought `Status: processed` with a `Processed in:` block once (1) lands.
3. Telemetry-audit spike (see Routing).
4. `/lit-pull` on searches 2, 3, 6.
