# MECH-189 literature synthesis — biology-before-formal-definitions pass

**Claim:** MECH-189 — *"During the child phase, high-salience benefit contacts under high contextual complexity are written to persistent ContextMemory as super-ordinal goal anchors that bias adult z_goal seeding across novel episodes."*
**Subject:** development.super_ordinal_goal_formation
**Status at pull:** candidate / v3_pending / confidence 0.0 (experimental); substrate IMPLEMENTED 2026-06-09 (`SuperOrdinalGoalMemory`), validation EXQ pending (infant_substrate:GAP-11).
**Pull date:** 2026-06-09. **Entries:** 5. **Scope:** the four pillars the substrate rests on, treated as a *mechanism class*, not as the V3 implementation.
**Companion review:** [`targeted_review_connectome_mech_189`](../targeted_review_connectome_mech_189/SYNTHESIS.md) (DEV-NEED-024 write-gate threshold angle). **Combined governance view:** [`mech_189_evidence_overview.md`](../mech_189_evidence_overview.md).

This pull exists because the MECH-189 substrate was implemented (separate session) without the biology-before-formal-definitions evidence pass that the project's own methodology rule requires for any mechanism instantiating a formal construct. There was no `evidence/literature/` directory for it; the substrate leaned on two in-claim anchors (Rovee-Collier; Berridge & Robinson). This pass grounds — or stresses — each pillar against the canonical literature.

## Pillar-by-pillar verdict

| Pillar (MECH-189 component) | Entry | Direction | Verdict |
|---|---|---|---|
| (a) WRITE gate keys on **incentive salience**, not calibrated liking | Berridge & Robinson 1998 | supports (0.72) | **Grounded.** Wanting/liking are dissociable; a drive-modulated salience signal is the biologically correct write trigger. |
| (2) **Infant operant/contingency learning forms durable cue-indexed goal biases** | Rovee-Collier 1999 | mixed (0.60) | **Grounded for formation; STRESSED for persistence.** Best human-developmental analogue of the write event AND the cue-index structure — but infant traces decay in ~1-2 weeks without reactivation and are sharply context-specific. |
| (3) **Cue-indexed / schema-based consolidation** of value memories (hippocampal–vmPFC anchor) | Tse et al. 2007 | supports (0.62) | **Grounded.** Schema-accelerated hippocampal→mPFC consolidation is the mechanism that converts a labile infant trace into a stable cortical anchor — it closes the durability gap Rovee-Collier opens. |
| (4) **Why childhood** maximises super-ordinal formation (INV-041 / INV-056) | Gopnik 2020 | supports (0.58) | **Grounded.** Childhood is the evolved explore phase (high novelty/plasticity); adulthood the exploit phase (routine/stability) — the exact asymmetry the novelty-gated, child-phase-only write window implements. |
| (1b) MECH-329 **wanting-before-liking** developmental ordering | Smith, Berridge & Aldridge 2011 | supports premise (0.55) | **Premise grounded; ORDERING under-evidenced.** Neural separability of wanting/liking/learning is confirmed; the *developmental* ordering itself is not, and the cited MECH-329 anchor could not be verified. |

## Verdict on the mechanism CLASS

**Biology supports the MECH-189 mechanism class.** Each of the four structural pillars maps onto a real, well-characterised biological process, and — importantly — the pillars chain: an accidental high-*salience* benefit contact (Berridge & Robinson) creates a labile, *cue-indexed* infant trace (Rovee-Collier), which *schema-assisted consolidation* migrates into a stable hippocampal–vmPFC anchor (Tse et al.), during the *childhood explore window* that is evolutionarily specialised to produce exactly such high-novelty contacts (Gopnik). That chain is the MECH-189 mechanism, and the literature traces it end to end. This clears the biology-before-mechanism gate: MECH-189 is *philosophy-right and mechanism-plausible*, not a formal construct floating free of biology.

**Two reservations bound the verdict — neither blocks the gate, both shape the validation EXQ:**

1. **Durability is conditional, not automatic.** Rovee-Collier's own data is the strongest internal tension: infant operant memories decay within ~1-2 weeks unless *reactivated*, and retrieval is sharply context-specific. MECH-189 asserts persistence across *novel* adult episodes. The class survives this only under the consolidation reading (Tse): the persistent anchor is the *consolidated end-state* of a reactivation-maintained childhood trace — not the labile trace itself. **Implication for validation:** the EXQ should build in repeated child-phase re-encounters (so anchors are reinforced, matching the reactivation biology), and the substrate's lack of any decay/reactivation dynamics is a fidelity gap worth noting (not fixing in this pass — substrate code is out of scope and under another session's claim).

2. **The MECH-329 developmental-ordering half is the thinnest link.** Separability of wanting and liking is solidly grounded (Smith et al.); the *temporal* claim that wanting seeds anchors *before* liking is calibrated is grounded only indirectly, and its registered anchor "Keren-Portnoy & Tomasello 2021" could not be independently verified (Keren-Portnoy's published work is in speech/phonological development; the verifiable infant-intentionality literature is Behne/Carpenter/Call/Tomasello). **Recommended follow-up:** a targeted developmental-ontogeny lit-pull for MECH-329 specifically, and correction/replacement of the unverified anchor in claims.yaml MECH-329 (deferred — claims.yaml is held by the substrate session; flagged to the user).

## Governance notes

- Lit signal only. Per the lit/exp-decoupling rule, this pass updates `literature_confidence` (via the rebuilt index into `claim_evidence.v1.json`) as a **parallel** signal. It does **not** touch MECH-189's `experimental_confidence` (stays 0.0) or `status` (stays candidate / v3_pending). Promotion past v3_pending still requires the validation EXQ — the biology gate is necessary, not sufficient.
- Expected quadrant after index rebuild: **plausible_unproven** (lit support now present, experimental confidence still 0.0) — the appropriate state for a substrate awaiting its validation run.
- No edit to MECH-189's claims.yaml block was needed or made (no inline lit field; the substrate session holds claims.yaml). The two unverified-anchor / decay-fidelity items above are surfaced to the user rather than actioned.
