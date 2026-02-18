THOUGHT: Commitment as Layered Eligibility Filters

Date: 2026-02-18
Status: Candidate mechanism thought (implementation-facing)
Scope: Tri-loop gating refinement; RC grounding; veto hierarchy

⸻

1. Motivation

The current “tri-loop” commitment framing (cognitive-set / motivational / motor gates) risks collapsing into scalar arbitration (e.g., max precision wins), which would undermine:
	•	explicit commitment boundaries (INV-012)
	•	authority stratification (INV-014; MECH-064)
	•	reality-coherence protection (MECH-065; Q-018)
	•	hard veto integrity (safety baseline + volatility drivers)

A biologically plausible alternative is to treat commitment as passing a stack of eligibility filters rather than a vote among competing loops.

⸻

2. Core Proposal

Commitment is permitted only within an eligibility region defined by multiple filters.
These filters operate in parallel but have ordered dominance (hard veto > structural validity > embodiment feasibility > motivational sufficiency > motor readiness).

This reframes “arbitration” as constraint satisfaction under hierarchical veto, not weighted averaging.

⸻

3. Candidate Filter Stack

F1 — Contextual/Experiential Anchoring Filter (Papez-like)

Function: Reject rollouts that are not anchored in coherent experience / temporal binding / known context.
	•	Inputs: hippocampal rollout traces; temporal binding; residue geometry; memory provenance tags
	•	Output: context_valid ∈ {pass, fail} or score_context ∈ [0,1]
	•	Effect: if fail → block commitment eligibility; increase verification pressure; reduce rollout lock-in

Interpretation: “Is this trajectory real enough / coherent with lived structure to be eligible for commitment?”

⸻

F2 — Embodiment/Interoceptive Feasibility Filter (Insula–Hypothalamus–Brainstem-like)

Function: Ensure proposed actions are consistent with current body/homeostatic state and feasible under physiological constraints.
	•	Inputs: HOMEOSTASIS stream; fatigue/energy proxies; arousal baseline; nociceptive state; predicted bodily consequences
	•	Output: body_feasible ∈ {pass, fail} and/or threshold modulation ΔT_body
	•	Effect: if fail → block motor eligibility; force replan or downshift mode

Interpretation: “Can the organism enact this now without violating viability constraints?”

⸻

F3 — Motivational Sufficiency / Aversion Gate (Ventral Striatum / Habenula-like)

Function: Require sufficient drive/salience and sufficiently low aversive prediction for commitment to be justified.
	•	Inputs: VALENCE vectors; signed harm/benefit prediction errors; drive persistence; cost of delay
	•	Output: motivation_ok ∈ {pass, fail} or score_drive, score_aversion
	•	Effect: if fail → keep in rehearsal/exploration; widen rollout; avoid premature commitment

Interpretation: “Is there enough reason to spend irreversible commitment here, and is aversion not prohibitive?”

⸻

F4 — Fast Threat Interrupt / Hard Veto (Amygdala-like)

Function: Rapidly stop or delay commitment when threat signals exceed a critical threshold.
	•	Inputs: HARM stream; volatility; novelty/threat detectors; learned “danger priors”
	•	Output: veto ∈ {none, soft, hard}
	•	Effect:
	•	hard veto → immediate inhibition of motor gate; raise global thresholds; increase verification; shift mode to emergency posture
	•	soft veto → raise threshold / require extra confirmation

Interpretation: “Stop now—do not lock in.”

⸻

F5 — Motor Readiness / Execution Release (Dorsal BG output gate)

Function: Final disinhibition for action/tool execution.
	•	Inputs: motor feasibility; availability of required capabilities; action plan stability
	•	Output: action release (commitment boundary crossing)
	•	Effect: stamps commit token; transitions to post-commit responsibility flow

Interpretation: “Release action now.”

⸻

4. Relationship to RC (Reality Coherence) and Typed Authority

RC_conflict is treated as an eligibility constraint rather than “just another signal.”
	•	RC_conflict gates privileged actions and policy-relevant commitments via verifier checks (MECH-064/065).
	•	RC_conflict also modulates filters (especially F1 and F4): high conflict increases threshold, reduces lock-in, increases verification pressure.

This suggests RC is composite:
	•	Context coherence (F1)
	•	Authority coherence / provenance integrity (verifier + typed boundary)
	•	Identity continuity (trusted anchors)

⸻

5. Commitment Protocol (Minimal Implementation Sketch)

Compute all filter outputs in parallel, then apply ordered dominance:
	1.	If veto == hard → inhibit motor gate; emergency posture.
	2.	If RC_conflict > T_high → inhibit privileged commitment; require verifier pass / additional evidence.
	3.	If context_valid == fail → block eligibility; widen exploration; reduce lock-in.
	4.	If body_feasible == fail → block motor eligibility; replan under homeostatic constraints.
	5.	If motivation_ok == fail → remain in rehearsal/exploration; do not stamp commit.
	6.	If all pass → allow motor release and stamp commit token.

Commit token must capture:
	•	commit_id
	•	trajectory reference / rollout provenance
	•	authority state (verifier status)
	•	RC_conflict state (at commit)
	•	uncertainty/precision state (at commit)

Post-commit:
	•	durable updates require commit traceability (MECH-060/061; INV-004/006; INV-012).

⸻

6. Why This Helps

This layered eligibility model:
	•	Prevents scalar collapse of arbitration (protects precision routing and authority stratification).
	•	Preserves hard veto integrity (threat cannot be outvoted by motivation).
	•	Preserves embodiment constraints (fantasy can’t override HOMEOSTASIS).
	•	Treats RC as structural validity, not salience.
	•	Provides a natural place to implement RC hysteresis (T_high / T_low bands) without oscillatory gating.

⸻

7. Failure Modes to Probe
	•	Motivational urgency overriding RC eligibility (should be impossible).
	•	Chronic false-positive veto (RC hysteresis too tight).
	•	Context filter too permissive (delusional rollout anchoring failure).
	•	Body feasibility ignored (interoceptive lane not binding).
	•	Soft veto ignored by motor gate (priority ordering broken).
	•	Commit token stamped without recording authority/RC state (responsibility geometry weakens).

⸻

8. Open Questions
	•	Should F1 (context anchoring) be purely binary or graded with hysteresis?
	•	What are minimal sufficient observables for F2 in non-embodied agents?
	•	How does F3 interact with delay tolerance (5HT-like) and volatility sensitivity (NE-like)?
	•	Where exactly does STN-like global threshold raising sit (RC conflict vs general conflict)?

⸻

9. Summary

Commitment is not a vote among loops.
It is entry into an eligibility region defined by layered filters with ordered dominance, culminating in a motor/tool release gate that stamps an explicit commit token enabling post-commit responsibility flow.

This provides a biologically plausible and REE-consistent mechanism for tri-loop coordination while preserving typed authority boundaries and RC-based protection.

⸻
