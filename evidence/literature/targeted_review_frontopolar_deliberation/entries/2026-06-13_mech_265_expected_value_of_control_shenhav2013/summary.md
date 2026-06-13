# Shenhav, Botvinick & Cohen 2013 -- The expected value of control as the arbitrator decision rule

**Claims:** MECH-265, SD-046, SD-032b (cross-link)
**Direction:** supports (arbitrator decision-function grounding)
**Confidence:** 0.66

## What the paper did

Shenhav, Botvinick & Cohen propose that the bewildering diversity of dorsal ACC findings -- reward processing, performance monitoring, conflict, action selection -- collapses into a single normative function: computing the **expected value of control (EVC)**. EVC integrates three terms: the expected payoff of engaging a controlled process, the amount of control that must be invested to achieve it, and the cost of that control in cognitive effort. The dACC uses EVC to decide *whether*, *where*, and *how much* control to allocate. It is a computational theory, not a single experiment -- the contribution is the integrating normative frame.

## Findings relevant to the claims

SD-046's roadmap calls for a "dACC-style arbitrator [that] selects which slot's best trajectory commits this tick," and MECH-265 specifies a parallel relative-importance read that a switching policy consumes. Neither claim said *by what rule* the arbitrator decides. EVC is the missing rule:

- **SD-046 (cross-slot arbitrator).** Each active goal slot proposes a trajectory with an expected payoff and a control demand; an effort cost penalises thrash. The arbitrator commits the slot with the highest EVC. This gives the arbitrator a principled objective rather than an ad-hoc max-over-slots.
- **MECH-265 (relative-importance monitoring).** MECH-265's parallel importance signal is the *input* to the EVC computation -- the per-slot payoff term. EVC explains why a relative-importance read is not enough on its own: importance must be discounted by control demand and effort cost before it drives a switch, which is what stops a high-importance-but-unreachable goal from capturing commitment.
- **SD-032b (dACC-analog).** EVC is explicitly a theory of dACC, REE's SD-032b subject -- so this entry grounds the V3 dACC hook's control-allocation role, the same way Kolling grounds its foraging-value role.

EVC and Kolling's foraging value are complementary readings of the same structure: Kolling gives the *empirical* dACC search-value signal, Shenhav gives the *normative* control-allocation function that signal serves. Together they are the dACC side of the dACC<->FPC deliberation loop.

## Limitations and caveats

Two real caveats. First, EVC is a normative theory, not a measured mechanism, and it deliberately leaves the **effort-cost function unspecified** -- which means a V4 arbitrator implementing EVC inherits that open question. Mis-specify the cost too low and the arbitrator thrashes between slots; too high and it freezes on the first commitment (the OCD-style over-binding SD-046 was partly meant to express). Second, EVC is about control allocation *in general*, not multi-goal arbitration specifically; the multi-goal reading is REE's extension. And it localises to dACC, so it grounds SD-032b and the arbitrator's decision rule, not MECH-265's *frontopolar* relative-importance representation directly (that is Mansouri 2017, already in prong_d).

## Confidence reasoning

A foundational, heavily cited integrative theory (source_quality 0.85, lowered from primary-data levels because it is review/theory). Held to 0.66 overall because mapping_fidelity is moderate (grounds the decision rule and effort-cost term, but is dACC-general not FPC-specific) and the unspecified cost function is a genuine transfer risk. Raises MECH-265 and SD-046 literature confidence; promotes nothing.
