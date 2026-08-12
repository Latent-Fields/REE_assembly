---
nav_exclude: true
---

# Thought Intake: REE efficiency as lifetime cognitive efficiency, not model size

**Raw thought file:** `docs/thoughts/2026-08-10_REE_efficiency.md`
**Session:** jovial-shannon-35d300, 2026-08-12
**Status:** processed, claim registered (Q-093)

---

## Verbatim prompt

See `docs/thoughts/2026-08-10_REE_efficiency.md` for the full text. Core reframing, condensed:
efficiency should not be measured as parameter count or per-step compute in isolation, but as
"cognitive efficiency" = competence achieved / total lifetime computational and experiential
cost (developmental/training compute, environmental experience, inference, memory, offline
replay/consolidation, adaptation, planning), counted for BOTH REE and any comparison system,
and evaluated ONLY at approximately matched behavioural competence -- explicitly not yet, since
"REE-v3 is currently enormously less competent than the large pretrained systems with which
such a comparison might eventually be made." The underlying architectural hypothesis: REE's
control/organising machinery (E1, E2, E3, commitment, replay, residue, goal maintenance) might
scale substantially more slowly than the richness of what its representational spaces can
encode, because REE carries history forward via persistent internal state (latent state,
recurrent state, goals, maps, residue, learned parameters) rather than repeatedly invoking a
very large pretrained model over long contexts. The multi-rate architecture (not every
mechanism runs every step) is flagged as potentially load-bearing for this. Proposes a research
programme: scaling curves (competence vs. lifetime compute, vs. environmental experience, vs.
persistent memory; adult inference cost vs. competence; adaptation achieved per unit additional
experience/compute), and raises a developmental-cost question (is "training" the wrong metaphor
for REE -- is "raising" more accurate, and how does that cost compare with amortised
pretraining cost for a deployed foundation model).

---

## What's New vs. Existing REE Docs (novelty table)

| Existing doc/claim | What it already covers | What this thought adds |
|---|---|---|
| Multi-rate architecture (mechanism-level, scattered across E1/E2/E3/control-plane docs) | Individual mechanisms already run at different rates / are selectively recruited rather than every mechanism firing every step. | **Names a specific hypothesis this property might support**: that control-machinery complexity can scale sublinearly relative to represented-world richness -- not previously stated as its own claim anywhere searched (`grep` for "cognitive efficiency", "compute scaling", "lifetime compute", "matched competence" across `claims.yaml` found zero occurrences). |
| Competence-floor campaign (`MECH-457` and dependents), `docs/CURRENT_FRONT.md` | Extensive, live work establishing that REE-v3's CURRENT competence is far below any plausible comparison baseline. | **Directly supplies the non-degeneracy precondition** this thought's own text names but does not resolve: no matched-competence comparison point currently exists, so the efficiency claim cannot yet be validly tested. This is why the registered claim is `substrate_conditional`, not `standard`. |
| No existing claim or plan document | -- | The **measurement protocol itself** (a family of scaling curves at matched competence) is new methodology, describable now even though the underlying architectural hypothesis cannot yet be tested. |

**Net assessment:** the architectural hypothesis (control-machinery cost vs. representational
richness) is genuinely new and claim-shaped once separated from the surrounding research-
strategy material. The broader "REE efficiency research programme" (scaling curves,
developmental-cost accounting, six sub-questions) is real but is evaluation methodology, not
itself a single falsifiable claim -- carried as notes rather than registered separately.

---

## Key formulations

1. Cognitive efficiency = competence achieved / total lifetime computational + experiential
   cost, evaluated ONLY at matched competence.
2. The size of what the cognifold can represent vs. the complexity of the machinery that
   organises those representations -- these need not scale together.
3. Persistent structured state + selective computation (multi-rate architecture) as the
   candidate mechanism for a sublinear-scaling dividend, contrasted with repeatedly invoking a
   large pretrained model over long contexts.
4. Six research sub-questions (recorded in the registered claim's notes, not separately
   registered): per-cycle cost; cost at matched competence; environmental-experience efficiency;
   adaptation cost once mature; whether persistence avoids in-context reconstruction cost; how
   "raising" cost compares with amortised pretraining cost.
5. "Training" may be the wrong metaphor for REE; "raising" may be more accurate, with the
   caveat that biological calendar time and computational developmental time need not be
   equivalent (replay, counterfactual trajectories, faster-than-real-time experience).

---

## Affected existing claims

`MECH-457` (competence-floor campaign) -- unaffected in status; cited as the reason the
registered claim's precondition is currently unmet, not as something this thought revises.

No existing claim's evidence, status, or confidence is altered by this intake.

---

## Candidate claims

**REGISTERED as Q-093** (2026-08-12). The block below is the exact text landed in
`claims.yaml`, kept here verbatim for provenance.

```yaml
id: Q-093
title: "Does REE's organising/control machinery (E1, E2, E3, commitment, replay, residue,
  goal-maintenance dynamics) scale sublinearly relative to the richness of the representational
  spaces it organises -- measured as competence achieved per unit of total lifetime
  computational and experiential cost -- at approximately MATCHED behavioural competence
  against comparison systems, rather than at unmatched competence or raw parameter/model-size
  counts?"
claim_type: open_question
subject: measurement.cognitive_efficiency.control_machinery_scaling
epistemic_category: substrate_conditional
depends_on: [MECH-457]
registered_utc: "2026-08-12"
```

(Full text, including `what_would_answer`, `notes`, and `evidence_quality_note`, is in
`docs/claims/claims.yaml#Q-093`.)

No other genuinely-new candidate claims were identified in this thought; the rest of its
content is evaluation-methodology scaffolding for Q-093, not a separate claim.

---

## Next steps

1. Q-093 registered; `build_claims_json.py` run after this intake session's other edits land.
2. **Not performed this pass (flagged as follow-on):** drafting the actual scaling-curve
   evaluation-methodology document (the thought's "REE efficiency research programme") as a
   standalone `evidence/planning/*_plan.md`-style artifact once Q-093's non-degeneracy
   precondition (a matched-competence comparison point) is closer to being met.
3. No lit-pull performed -- this is a REE-internal measurement-methodology question, not a
   biological claim requiring citation-backed grounding.
