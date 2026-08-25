# Thought Intake: Persistence Must Earn Continuation

**Date:** 2026-08-25
**Raw thought file:** `docs/thoughts/2026-08-12_persistence_must_earn_continuation.md`
**Session:** dazzling-jackson-efb9e9 (worktree), 2026-08-25

## Verbatim prompt (core proposal)

> For every persistent process that REE can initiate, what makes it continue, and what makes it
> stop? ... Persistence itself must continually earn continuation.

The thought arose from considering redundant checking in basal-ganglia decision systems and the
apparent failure of closure in OCD, then generalised into an architecture-wide question: REE has
extensive machinery for *starting* persistent processes (hunger, curiosity, information-seeking,
exploration, prediction, planning, checking, goal formation, threat monitoring, memory retrieval,
error correction, social inference) but comparatively little explicit, general machinery for
*stopping* them. It proposes (a) certainty cannot be the stopping condition since certainty is
never available in principle, so the real question is "when is REE sure enough to act, given that
it can never be sure"; (b) a preliminary termination taxonomy (completion / satiety / closure /
disengagement / suspension / switching / interruption / reopening) that preserves *why*
termination occurred; (c) a Marginal-Value-Theorem-style continuation rule (continue while
marginal return exceeds available alternatives); (d) a progress-monitoring stopping heuristic
("am I actually getting anywhere?"); (e) the hierarchical-RL observation that `option = initiation
+ policy + termination`, i.e. every skill needs an explicit stop condition, not just a policy; and
(f) OCD read as evidence for a more dangerous failure mode -- a persistent process can degrade the
very variable used to judge whether it should persist (repeated checking eroding subjective
confidence while leaving objective accuracy intact), producing positive-feedback failure to stop.

## What's new vs. existing REE docs/claims (novelty table)

| Thread in the raw thought | Existing REE coverage | Verdict |
|---|---|---|
| "Turn evaluation off on completion" (a closure token that releases commitment latch + installs No-Go + discharges residue) | **SD-034** (IMPLEMENTED 2026-04-20), the governance `ClosureOperator`. Per its own doc: "The 2026-04-20 GAP MEMO and the OCD thought set identify this as the load-bearing missing piece" -- the *same* root the raw thought reaches independently, four months later, via a different route. | Already owned. Cross-ref only, not re-asserted. |
| "When is REE sure enough to act" / certainty is never available / dynamic threshold | **MECH-434** (epistemic commitment timing): inference-layer WHEN-to-stop-gathering-evidence control parameter, inverted-U between epistemic-freezing and anti-epistemic-panic. | Already owned for the inference-layer instance. Cross-ref only. |
| Widen search under stalled-but-salient goal progress | **MECH-343 / SD-061** (difficulty-gated proposal-entropy regulator): widen candidate generation under goal-progress stall while goal salience is preserved. | Already owned -- but only the *widen* direction. The thought's disengagement direction (what if widening also fails) is NOT covered. |
| OCD as a psychiatric individual-differences failure mode | **MECH-080** (rollout-truncation set-points): OCD = abnormally deep BG/ACh attractor lock-in. | Already owned, but via a *different mechanism* than the checking-erodes-confidence account in thought section 13 -- see below. |
| Marginal-Value-Theorem / optimal-foraging continuation rule, as an environment to test against | **Q-080** (effort-dissociation env, landed 2026-07-09; Charnov MVT). | Already owned as substrate; not re-asserted. Cited as the natural test env for MECH-498 below. |
| General termination taxonomy (satiety / disengagement / suspension / switching / interruption / reopening) applied across ALL persistent-process families, preserving why termination occurred | No existing claim generalises SD-034 beyond rule_state closure. | **Genuinely new -> registered as ARC-128.** |
| Self-referential stopping failure: checking degrades the confidence variable that gates its own termination, independent of BG/ACh attractor dynamics | No existing claim; MECH-080 covers a different (gate-dynamics) mechanism for the same clinical phenomenon. | **Genuinely new -> registered as MECH-497.** |
| Progress-gated disengagement: continue only while marginal return AND observed rate of progress both justify it; the complement to MECH-343's widening response when widening also fails | MECH-343/SD-061 cover only the widen-under-stall direction. | **Genuinely new -> registered as MECH-498.** |
| Information-seeking as an action competing with other actions (expected-value-of-information framing) | Partially covered by MECH-314b (uncertainty-driven curiosity / epistemic-value bonus) and MECH-434, but neither explicitly frames information-seeking as competing on the SAME action-selection ledger as eating/resting/fleeing/helping. | Adjacent, not a clean duplicate, but thin enough (and close enough to MECH-314b/MECH-434 in spirit) that it is folded into ARC-128's framing rather than given its own claim. |
| Multi-agent strategic cost of delay (another mind can make waiting costly independent of information value) | No hits for "strategic cost of delay" / adversarial-delay framing found by targeted search of claims.yaml. | Plausibly new, but not verified against REE's existing (large) multi-agent/adversarial-evidence claim cluster carefully enough in this pass to register responsibly. **Left as a next-step lit/claims check, not registered.** |
| Sleep may alter termination behaviour specifically (not just representations/policies) | Speculative, single anecdotal Fishtank observation per the thought's own section 17. | Correctly left unclaimed by the raw thought itself; not claim-worthy material. |

## Key formulations (verbatim, load-bearing)

> Persistence itself must continually earn continuation.

> REE is sure enough when further uncertainty reduction is no longer expected to improve the
> trajectory sufficiently to justify delaying commitment.

> A persistent cognitive process may modify the variables used to determine whether that same
> process should persist.

> Continue process X while its marginal expected return remains preferable to available
> alternatives.

> Termination should therefore preserve **why** termination occurred.

## Affected existing claims

- **SD-034** -- generalised (not superseded, not amended) by ARC-128. SD-034 remains the correct,
  sole owner of the rule_state-specific implemented mechanism.
- **MECH-343 / SD-061** -- named as the complementary widen-direction response; MECH-498 is its
  disengagement-direction counterpart, not a revision of either.
- **MECH-080** -- explicitly distinguished from MECH-497 (gate-dynamics attractor lock-in vs.
  self-referential confidence erosion); both may be true simultaneously in a real OCD-like
  failure.
- **MECH-434** -- adjacent (both concern "when is evidence/deliberation enough"), cross-referenced
  by `depends_on` from ARC-128 and MECH-498, not modified.
- **Q-080** -- cited as the existing test substrate for a future MECH-498 experiment; not
  re-asserted or amended.

No existing claim's status, confidence, or evidence record was touched.

## Candidate claims -- REGISTERED this pass (not "for future registration")

Per standing practice (thought-intake registers genuinely-new ideas into `claims.yaml` in the
same pass, version-scoped, rather than leaving them as prose), the following were registered
directly:

- **ARC-128** -- `control_plane.termination_taxonomy_generality`. `status: candidate`,
  `epistemic_category: substrate_conditional` (set explicitly), `implementation_phase: v4`,
  `version_relevance: v4_v5`. `depends_on`: SD-034, MECH-343, SD-061, MECH-434.
- **MECH-497** -- `control_plane.self_referential_stopping_failure`. Same status/category/phase
  pattern. `depends_on`: MECH-080, SD-034, ARC-128.
- **MECH-498** -- `control_plane.progress_gated_disengagement`. Same status/category/phase
  pattern. `depends_on`: MECH-343, SD-061, Q-080, MECH-434, ARC-128.

All three: `status: candidate`, `polarity: asserts`, `registered_utc: 2026-08-25`. Compass /
architectural framing only -- promote/demote and `narrow_open_question` are suppressed by the
explicit `epistemic_category: substrate_conditional`; none of the three should be read as a V3
build authorization. Full comparison against existing machinery, and the explicit "out of scope"
list, is in the new architecture doc
`docs/architecture/persistent_process_termination_taxonomy.md`.

## Next steps

1. **Literature pull, before hardening any of the three claims further**: repeated-checking /
   subjective-confidence-erosion literature (van den Hout & Kindt family is the closest known
   anchor named in this intake but not yet verified against a specific citation -- needed before
   MECH-497 can be called literature-grounded rather than provisional); Marginal Value Theorem /
   optimal foraging (Charnov, already partially covered via Q-080's design doc); hierarchical-RL
   options/termination (Sutton et al. 1999, already used elsewhere in the registry for MECH-317 --
   check whether that citation covers the termination-function half or only option-formation).
2. **Multi-agent strategic-cost-of-delay thread**: check REE's existing multi-agent /
   adversarial-evidence claim cluster carefully (not yet done in this pass) before deciding
   whether it is genuinely new or already implicit somewhere. If new, register as its own claim
   rather than folding into ARC-128.
3. **Version-routing decision**: all three registered claims are parked `v4`/`substrate_conditional`
   by default, per standing practice for thought-intake registrations. A future `/governance`
   cycle can route any of them onto V3 explicitly if a cheap, non-degenerate test becomes
   available (MECH-498 against the already-built Q-080 env is the most plausible near-term
   candidate).
4. **Behavioural experiment design** (thought section 16) is rich (diminishing-information-value,
   information-plateau, declining-resource-patch, goal-impossibility, temporary-obstruction,
   costly-deliberation, hazard-urgency, competition, adversarial-information, pathological-
   checking, self-expanding-uncertainty manipulations) but is explicitly premature before any of
   ARC-128/MECH-497/MECH-498 is routed to V3 -- do not queue an experiment from this list without
   that routing decision first.
5. Raw thought file `docs/thoughts/2026-08-12_persistence_must_earn_continuation.md` marked
   `Status: processed` with this intake linked, per the Stage 1/2 linking convention.
