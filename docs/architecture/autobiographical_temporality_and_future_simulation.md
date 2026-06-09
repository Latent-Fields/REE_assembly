# Autobiographical Temporality and Future Simulation (ARC-085 / MECH-365 / MECH-366 / Q-060)

Status: candidate cluster, V4/V5, off the V3 critical path. Registered 2026-06-09.

Source intake: [evidence/planning/thought_intake_2026-06-06_hyperthymesia_autobiographical_temporality.md](../../evidence/planning/thought_intake_2026-06-06_hyperthymesia_autobiographical_temporality.md)
Raw thought: [docs/thoughts/2026-06-06_hyperthymesia_autobiographical_temporality.md](../thoughts/2026-06-06_hyperthymesia_autobiographical_temporality.md)

Empirical anchor (verified): Valentina La Corte, Pascale Piolino, Laurent Cohen, "Autobiographical hypermnesia as a particular form of mental time travel," *Neurocase* 31(4):188-192 (2025), DOI [10.1080/13554794.2025.2537950](https://www.tandfonline.com/doi/abs/10.1080/13554794.2025.2537950) (Paris Brain Institute / ICM). Single case TL (~17yo female), TEMPau + TEEAM. Computational analogue for later read: Lampinen et al., "Towards mental time travel: a hierarchical memory for RL agents," [arXiv:2105.14039].

## The idea

A human case of highly superior autobiographical memory (hyperthymesia) reports two things together: exceptionally detailed, emotion-saturated recall of personal past events, and unusually vivid, detailed projection of personal future events — recalled and imagined from switchable first-person/observer perspectives, organised as an identity-indexed "memory palace." The REE-relevant extraction is **not** precognition or perfect memory. It is that **autobiographical past reconstruction and future simulation may draw on one self-tagged temporal event substrate**, which argues for treating memory as an organised identity field with strong provenance labels rather than neutral storage.

This cluster captures that as version-scoped candidate claims. It does **not** re-assert REE's existing imagination-safety stack (INV-011, MECH-094, MECH-037, ARC-014, SD-026) — that content is already owned; here it is depended-on, not duplicated.

## <a id="arc-085"></a>ARC-085 — Unified autobiographical temporal event substrate

Retrospective replay (ARC-007) and prospective simulation (ARC-018) draw on **one** self-tagged event-token store, not two parallel machineries. Replay is backward reinstatement of event tokens; future trajectory generation is forward re-composition of the same tokens. Memory is an identity-indexed event field (events bound to perspective, emotion, residue, self-state), not neutral storage.

- **V3 reality:** REE owns the two halves *separately* — ARC-007 (store/replay paths through residue-field terrain) and ARC-018 (explicit rollouts + post-commitment viability map). What is new is the assertion they are one substrate.
- **Falsifier:** corrupting the shared store degrades past-recall and future-simulation fidelity *together*, vs independent degradation under a two-store model.
- `epistemic_category: substrate_conditional` set explicitly (overriding `architectural_commitment -> substrate_coherence`): this is a candidate commitment gated on a V4 event-token store that does not exist in V3.

## <a id="mech-365"></a>MECH-365 — Provenance-bearing event token

Every event token carries `{time, place, self_state, other_agents, perspective, affect, residue, source_status, committed_vs_imagined}`, and a **one-way gate** ensures imagined/simulated future tokens are usable for planning without ever acquiring committed-history status. The scarce resource is provenance, not capacity; any path that lets a simulated event accrue committed weight is a confabulation bug.

This is the **data structure** that carries a safety property REE already enforces in pieces (MECH-094 sim-vs-real / confabulation; MECH-037 Papez provenance gating; INV-011 imagination without belief update). It does not re-assert the property — it makes `committed_vs_imagined` a first-class field on the ARC-085 substrate. SD-026 (prospective write channel) is the nearest write-side mechanism.

## <a id="mech-366"></a>MECH-366 — Switchable episodic perspective tag

Event tokens carry a viewpoint label (participant/first-person vs observer/third-person) and can be re-experienced or re-simulated from either viewpoint at retrieval, independent of encoding viewpoint. Perspective is a represented, switchable property of the episode.

- SD-005 (z_self/z_world split) is the nearest substrate but represents self-vs-world *content*, not a switchable viewpoint *on an episode* — that construct is absent from claims.yaml.
- Anchor: TL fluidly switches participant/observer perspective on both recalled and imagined events.

## <a id="q-060"></a>Q-060 — Distinct autobiographical memory type?

Should REE represent autobiographical event memory as a distinct first-class type, separate from semantic (facts/relations) and task/procedural (policies/schemas) memory — or is the existing episodic->semantic consolidation pathway (MECH-121) sufficient? The case motivates the distinction (TL separates emotion-tagged "life memory" from neutral encyclopedic "black memory"), but REE has no memory-type taxonomy claim. Sub-questions: does a distinct layer earn its keep vs a tag on episodic content; how does residue attach without contaminating imagined futures (ties MECH-365); where is the replay / counterfactual-simulation / future-planning boundary. `epistemic_category: substrate_conditional` explicit so `narrow_open_question` does not fire — V4-parked, not V3-tractable.

## Cautions (carry forward verbatim from the intake)

Do not treat hyperthymesia as desirable, vivid memory as accurate, or future simulation as prediction/precognition. Do not generalise strongly from a single case. Do not promote any of this to an invariant or a V3 target. Correct extraction: preserve autobiographical temporality as a bridge between memory, identity, and future trajectory generation; provenance and commitment-status labels are the load-bearing safety requirement.

## Dependency wiring

- ARC-085 depends_on ARC-007, ARC-018.
- MECH-365 depends_on ARC-085, MECH-094, MECH-037, INV-011.
- MECH-366 depends_on ARC-085, SD-005.
- Q-060 depends_on ARC-085, MECH-121.

All `status: candidate`, `epistemic_category: substrate_conditional`, `implementation_phase: v4`, `version_relevance: v4_v5`. Promote/demote suppressed; the right response is to wait for the upstream V4 substrate, not to run experiments on the current V3 machinery. DO NOT build in V3 until routed by an explicit version decision.
