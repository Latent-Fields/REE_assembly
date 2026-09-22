---
title: "Commitment Control Faces (WHEN / WHETHER / WHICH-SET)"
parent: "Control, Precision & Neuromodulation"
grandparent: Architecture
nav_order: 22
status: candidate
status_asof: "2026-09-22"
status_claim: MECH-580
---

# Commitment Control Faces (WHEN / WHETHER / WHICH-SET)

**Claim Type:** mechanism_hypothesis
**Scope:** How a scalar arousal signal can and cannot alter what gets committed
**Depends On:** MECH-463 (arousal channels are argmax-invariant variance amplifiers), MECH-465 (WHETHER face needs a boundary regime), MECH-448 / ARC-107 (BG eligibility envelope), MECH-093 / MECH-005 (WHEN face), ARC-002 (action-conditioned E2), ARC-016 (precision-to-commitment circuit)

Source thought: `docs/thoughts/2026-09-22_action_conditioned_world_model_and_arousal_gated_commitment.md`.
Intake: `evidence/planning/thought_intake_2026-09-22_action_conditioned_world_model_and_arousal_gated_commitment.md`.

## Three faces, already partly owned

| Face | What arousal moves | Owning claims | Substrate |
|---|---|---|---|
| WHEN | E3 update cadence | MECH-093, MECH-005, MECH-161 | `heartbeat/clock.py` z_beta -> e3_steps (endogenous range 0.91% of mean; see substrate_queue `mech005-endogenous-arousal-dynamic-range`) |
| WHETHER | commit threshold / gate | MECH-465, MECH-106, MECH-104, MECH-090 | `e3_selector.py` variance commit gate, urgency threshold shrinkage; BetaGate commit-readiness conjunction (armed gate measured inert 2026-09-18) |
| WHICH-SET | breadth of the admitted candidate set | **MECH-580** (this doc) | `e3_selector.py::_f_eligibility_envelope` (`f_eligibility_envelope_floor`, `f_eligibility_dn_sigma`) -- floor is a fixed global scalar today |

## MECH-580 {#mech-580}

Arousal alters WHICH candidate is committed only by modulating commit-eligibility BREADTH (the width of
the basal-ganglia eligibility envelope, i.e. the size of the candidate set admitted to the commit gate),
never by reordering candidate scores. High phasic arousal narrows the admitted set toward the incumbent
(exploit); low or tonic arousal widens it (explore). This face is dissociable from WHETHER and WHEN.

**Why this is the only WHICH route open to a scalar.** MECH-463 established that the three global-scalar
affect routes into E3 are argmax-invariant: they cannot change which candidate wins a deterministic
argmin. A scalar can still change the committed candidate by truncating the admitted set, and, under a
sampled commit pick, by changing the support the sample is drawn from. That is the mechanism this claim
names.

**Precondition that makes it observable.** Candidate futures must be action-discriminable under the
world model (ARC-002 strong form; SD-e1 rollout consistency). With near-identical candidate scores a
breadth change admits or excludes nothing that differs, so a null under non-discriminable candidates is
uninterpretable. The WHEN and WHETHER faces carry no such dependency.

**Literature (verified 2026-09-22).** Separability: Thura & Cisek 2017 (Neuron 95:1160); Hanks, Kiani &
Shadlen 2014; Murphy, Boonstra & Nieuwenhuis 2016. Breadth: Eldar, Cohen & Niv 2013; Jepma &
Nieuwenhuis 2011. Counter-evidence to an exclusive reading: de Gee et al. 2017, 2020 (arousal also
shifts the drift criterion). Full list in the intake, section 4.

Full YAML entry, falsifier and status: `docs/claims/claims.yaml` (`MECH-580`).
