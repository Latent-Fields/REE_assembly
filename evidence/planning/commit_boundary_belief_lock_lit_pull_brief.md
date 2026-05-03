# Commit-Boundary Belief Lock — Pre-Registration Lit-Pull Brief

**Drafted:** 2026-05-03
**Status:** lit-pull spec; no claims registered
**Scope:** decide whether post-commit attribution rigidity warrants registration as a distinct mechanism for delusion, complementing the existing MECH-244 / MECH-246 / MECH-247 psychosis cluster. The brief is the gate: actual lit-pull is queued only after this brief is signed off.

---

## One-line framing

> A belief that has crossed the commit boundary is not just a belief held — it is part of the durable, attribution-bearing record of what the agent has done. Revising it costs more than revising an unenacted belief, because revision must propagate back through the agent's own action history. Pathological setting of this cost = delusion-resistant-to-argument signature.

## Source observation

User (consultant psychiatrist, HSE Ireland) noted that the clinical heuristic for distinguishing delusion from belief / fear / idea leans heavily on whether the belief has influenced action. Mapping that heuristic onto INV-021 ("responsibility-bearing durable updates occur only at typed commit boundaries") and its `emergent_from` chain (ARC-003 typed commit, SD-026 prospective precision template write channel) yields a candidate mechanism that does not currently appear in the registry.

## Hypothesis under investigation

**Pre-commit:** belief is one candidate among many; revisable under counter-evidence at standard cost.

**At the typed commit boundary (ARC-003):** action enacted under the belief; INV-012 / INV-021 make the action's residue + its lineage durable.

**Post-commit:** revising the belief now requires a corresponding revision of what the agent takes to be their own authored history. The architecture protects the belief not because of precision strength (MECH-244) or simulation-leakage (MECH-094), but because the belief is structurally load-bearing for downstream attribution stability.

**Pathology:** an attribution-rigidity setpoint tuned too high → counter-evidence cannot dislodge the belief, because dislodging it would destabilise the agent's record of self-as-author. This is the delusion-resistant-to-argument signature, and predicts a specific clinical course (insight develops slowly, behavioural enactment under the delusional frame entrenches rather than dislodges it, early intervention disproportionately effective).

## Why this is plausibly distinct from existing mechanisms

| Mechanism | Failure mode | Locus |
|---|---|---|
| MECH-244 prior-dominated precision failure | top-down priors override sensory input | precision allocation |
| MECH-246 signal-degradation pathway | input quality breakdown | sensory chain |
| MECH-247 trauma-shaped prior pathway | prior shaped by past trauma | prior content |
| MECH-094 simulation/real distinction | simulated experience encoded as real | source-monitoring |
| **proposed mechanism** | **acted-upon belief protected by attribution stability** | **post-commit attribution chain** |

The proposed mechanism operates orthogonally — it does not require dysregulated precision, degraded input, traumatic prior content, or source-monitoring failure. It predicts that even under intact precision and intact source-monitoring, beliefs that have driven typed commits will be measurably harder to revise than matched non-enacted beliefs.

This is the falsifiable part: a precision-only account predicts symmetry between enacted and non-enacted false beliefs; the commit-boundary lock predicts asymmetry.

## Architectural prediction (provisional, not registered)

If support is strong, two registrations are warranted:

- **MECH-X commit_boundary_belief_lock** — durable belief representations that motivated typed commit-boundary crossings carry attribution-load that resists revision; pathological setting produces delusion-resistant-to-argument signature.
- **MECH-Y attribution_rigidity_setpoint** — tunable parameter setting how strongly downstream belief revision must respect upstream commit history. Too low → confabulation territory (already covered by MECH-094). Too high → delusion territory (this proposal). Defines the dose-response curve.

Co-mechanism framing is preferred over single-mechanism because it captures the dose–response question explicitly and ties the new claim into the existing MECH-094 territory cleanly (one mechanism, two pathological tails of the same parameter).

## Literature streams

Target ~7 entries total, distributed roughly 2 / 1 / 1 / 1 / 2 across the streams below. Adjust if early hits dictate.

### Stream 1 — Cognitive dissonance + post-decisional belief consolidation

**Why:** This is the closest existing empirical phenomenon. Festinger-tradition work has documented post-action belief alignment for ~70 years. If the literature does not converge on action → belief consolidation as a robust effect with measurable asymmetry, the architectural claim is unfounded.

**Searches:**
- "cognitive dissonance" + "post-decisional" + "belief revision"
- "choice-supportive bias" + memory consolidation
- "effort justification" + "belief change"
- Festinger 1957 + key successors (Cooper 2007, Aronson, Stone)
- Recent neuroimaging: dACC / vmPFC engagement during dissonance reduction (Izuma; Kitayama; Harmon-Jones)

**Key question:** Is there a measurable asymmetry between pre-commit and post-commit belief revision rates under matched evidence? Has the asymmetry survived recent replication efforts (post-2015 replication crisis)?

### Stream 2 — Insight in psychosis (clinical literature)

**Why:** If the mechanism is real, insight should track exposure to commit boundaries crossed under the belief — not just severity or chronicity. Late-presenting first-episode psychosis (more enacted commits accumulated) should have worse insight than early-presenting matched for severity; insight gain should require re-authoring of past actions.

**Searches:**
- David, A.S. — Schedule for Assessment of Insight (SAI / SAI-E) and successors
- Amador, X. — anosognosia in schizophrenia
- "insight" + "schizophrenia" + "longitudinal" + "behavioural enactment"
- "first-episode psychosis" + insight + duration of untreated psychosis
- Lysaker et al. — metacognition in psychosis

**Key question:** Does pre-treatment behavioural enactment of the delusion predict insight trajectory independent of duration of untreated psychosis?

### Stream 3 — Forensic / confession psychology

**Why:** Naturalistic test of the mechanism. Internalised false-confession cases (the confessor comes to believe the confession) are the clearest real-world demonstration of acting-on-a-belief consolidating the belief. Forensic literature has documented this for decades.

**Searches:**
- Kassin, S. — internalised false confession + interrogation
- Gudjonsson — memory distrust syndrome
- "false confession" + "internalisation" + post-hoc belief
- "post-decisional regret" + rationalisation

**Key question:** Does the strength of post-confession belief consolidation track the irreversibility / formality of the confession act (a typed-commit-boundary signature)?

### Stream 4 — Predictive-coding accounts of delusion (orthogonality cross-check)

**Why:** Make sure the proposed mechanism is genuinely orthogonal to existing prior-strength accounts (Corlett, Fletcher & Frith, Adams & Friston) rather than a re-description in different vocabulary. If the predictive-coding accounts already predict the action-history asymmetry, this is the same claim wearing different clothes.

**Searches:**
- Corlett, P.R. — predictive-coding accounts of delusion formation
- Adams, R.A. + Friston — active inference and psychiatry
- Fletcher & Frith — perceiving is believing
- Sterzer et al. — predictive coding account of psychotic symptoms

**Key question:** Do these accounts predict an asymmetry between enacted and non-enacted false beliefs, or only a precision/prior asymmetry? If the latter, the proposed mechanism adds a distinct prediction worth registering.

### Stream 5 — Neural substrate (connectome side)

**Why:** If real, there should be identifiable circuitry binding action-history to belief representation. Candidates: vmPFC + hippocampus (autobiographical action memory), dACC (conflict monitoring during attempted revision), default-mode network (autobiographical self-narrative integration).

**Searches:**
- "vmPFC" + "value updating" + self-relevance
- "autobiographical memory" + "belief revision"
- "default mode network" + "self-narrative consistency"
- "dACC" + "cognitive dissonance" + neuroimaging

**Key question:** Is there evidence that revising a belief that motivated past action recruits more conflict-resolution / re-encoding machinery than revising a non-acted-upon belief of matched strength?

## Decision criteria (to apply at verdict time)

After the entries land, classify into one of three outcomes:

**Strong support — register MECH-X + MECH-Y as candidate, v3_pending=true:**
- Festinger tradition converges on post-action belief consolidation with measurable asymmetry (Stream 1)
- Insight literature shows enactment-track relationship independent of severity proxies (Stream 2)
- At least one neuroimaging study shows distinct circuitry for revising acted-upon vs non-acted-upon beliefs (Stream 5)
- Existing predictive-coding accounts (Stream 4) do not already predict the action-history asymmetry as part of prior strength

**Mixed — register as candidate with explicit `evidence_quality_note` flagging the gaps:**
- Festinger work supports the effect but clinical psychiatric literature does not differentiate enacted vs non-enacted delusions
- Insight literature treats enactment as covarying with severity but does not separate the two
- Recommend a follow-up clinical-design lit-pull before promotion gates

**Weakens — do not register, or register differently:**
- Existing predictive-coding accounts already predict action-history asymmetry as part of prior strength (then this is not a new claim — fold it into a clarification of MECH-244)
- No clinical signal differentiating enacted vs non-enacted delusion trajectory
- The Festinger effect does not survive recent replication (then the architectural framing has no empirical foundation regardless of how clean it looks)

## Failure mode being guarded against

This pull is the explicit application of the **biology-before-formal-definitions** rule (canonical failures: SD-003 28 FAILs, SD-010/SD-011 harm-stream split). The mechanism is architecturally clean and clinically motivated, but those are exactly the conditions under which past philosophy-right / mechanism-wrong claims have generated 20+ FAILs before being retracted. The lit-pull is the gate to prevent another instance.

## Output expected

`evidence/literature/targeted_review_commit_boundary_belief_lock/`
- `entries/` — ~7 record.json + summary.md pairs (per /lit-pull skill spec)
- `verdict.md` — explicit per-stream classification (supports / mixed / weakens) + overall recommendation (register / register-with-modification / do not register / fold-into-existing)

If verdict is "register": this brief becomes the basis for a follow-up `commit_boundary_belief_lock_governance_plan.md` mirroring the SD-033 structure, with claim registrations + EXQ proposals.

## When to revisit

- After verdict.md lands: come back here, mark this brief as `Status: closed (verdict X)`.
- If "register" verdict: linked from the new claim's `evidence_quality_note` and from the governance plan that follows.
- If "weakens" verdict: archive in place; the brief itself becomes useful provenance for why the claim was not registered.

## Related claims (existing registry, do not duplicate)

- INV-012 (load-bearing for INV-021) — responsibility / commitment substrate
- INV-021 — responsibility-bearing durable updates only at typed commit boundaries
- ARC-003 — E3 typed commit action
- SD-026 — prospective precision template write channel
- MECH-061 — commitment boundary mechanism
- MECH-094 — simulation/real distinction (the confabulation tail of the same parameter)
- MECH-244 — prior-dominated precision failure (psychosis)
- MECH-246 — signal-degradation pathway (psychosis)
- MECH-247 — trauma-shaped prior pathway (psychosis)
