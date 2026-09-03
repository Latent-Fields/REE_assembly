# Thought Intake: Claim Rotation and Dual-View Claim Matrices

- **Date processed:** 2026-09-03
- **Raw thought:** `docs/thoughts/2026-09-03_claim_rotation_dual_view_claim_matrix.md`
- **Session:** thought-routing-20260903 (claim draft by a Sonnet subagent; reviewed and landed by the session)
- **Stage:** 2 (structured intake). **REGISTERED:** GOV-ROTATE-1.

## Verbatim core proposal

> REE may benefit from maintaining multiple explicit representations of the same canonical scientific claims. The canonical claim retains a single evidence and promotion state, while alternative architectural, transformation, behavioural, developmental or biological views expose different observables and interventions. When a claim stalls, rotating its representation may reveal a simpler next experiment without multiplying claims or evidence.

> Same claim, multiple views, one truth state. If a new view introduces new empirical content, that content becomes a new claim rather than inheriting the old claim's evidence.

A governance/epistemic-tooling thought, not a scientific claim, triggered by the two companion 2026-09-03 thoughts and by V3-EXQ-978, where the architectural framing (does `z_world` discard direction) suggested SD-018 and the transformation framing (where does the direction distinction stop propagating toward action) suggests a different family of experiments.

## What's new vs. existing REE docs/claims (novelty table)

| Thread | Existing coverage | Verdict |
|---|---|---|
| Fan a stalled question out into rival hypotheses across diverse axes | GOV-FANOUT-1 (portfolio of independently falsifiable rivals when a bottleneck fires) | Adjacent but distinct: fan-out multiplies hypotheses; rotation holds ONE claim fixed and changes its coordinates. A rotated view may feed one fan-out leg. |
| Evidence must not be counted twice / denominators must not be padded | GOV-FROZEN-1 (frozen hypothesis-set integrity), governance derive-only pipeline | Already-owned constraint that rotation must respect; wired as depends_on. |
| A standing-rule change must be checked on held-out cases before adoption | GOV-HELDOUT-1 | Already-owned discipline; this claim is itself subject to it (adopting rotation is not evidence it works). |
| Alternative representations of a claim as a named epistemic layer with one truth state, a smuggled-content rule, and a stall-triggered heuristic | Nothing registers this. Views exist informally (claims carry `functional_restatement`, `title`, `notes`; the triple-view diagram bundle in `docs/architecture/diagram_views.md` is architectural only) but no rule says how a re-description relates to evidence state. | Genuinely new -> registered narrowly as GOV-ROTATE-1, with an explicit no-build gate. |
| A representations schema (`canonical_claim_id` / `representations[]`) | The thought itself says "illustrative only... should not be implemented merely because the thought exists" | Not registered; explicitly gated in GOV-ROTATE-1 notes (i). |

## Key formulations (verbatim, load-bearing)

> When a claim stalls, rotate it.

> Alternative representations may restate a claim, but they may not smuggle additional empirical content into the same truth state.

> Does rotating a stalled claim produce a clearer, smaller or more discriminating next experiment? If not, the machinery is unnecessary.

## Affected existing claims

Cross-referenced via `depends_on` only: GOV-FANOUT-1, GOV-HELDOUT-1, GOV-FROZEN-1. No status, evidence, or wording change on any existing claim.

## Candidate claims -- REGISTERED this pass

- **GOV-ROTATE-1** (`governance.epistemics.claim_rotation`, governance_rule, candidate, implementation_phase v3). Multiple views, one truth state; new empirical content exposed by a view becomes a new claim and never inherits the parent's evidence. Notes carry: (i) a binding no-schema/no-tooling/no-second-ledger gate until one rotation is shown on a real adjudication to have produced a smaller or more discriminating next experiment; (ii) the V3-EXQ-978 autopsy as the first held-out trial (INV-088 rotated from architectural into transformation coordinates), whose outcome on that question is the only admissible evidence and is to be recorded on the claim once the autopsy lands; (iii) what it is not (a second ledger, GOV-FANOUT-1, a paraphrase licence); (iv) the thought's section 11 success criterion verbatim.

## Next steps

1. When `evidence/planning/failure_autopsy_V3-EXQ-978_2026-09-03.md` lands (owned by session autopsy-outstanding-20260903 at the time of this intake), record on GOV-ROTATE-1, as a dated note, whether the rotation produced a smaller or more discriminating next experiment than the architectural framing alone; a rotation that restates the same next step counts as a null.
2. No experiment is ever minted against GOV-ROTATE-1 (governance_rule). It advances by recorded trials only.
3. Literature: none owed.
