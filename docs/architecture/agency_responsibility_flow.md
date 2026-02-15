# Agency and Responsibility Flow

**Claim Type:** architectural_commitment  
**Scope:** Agency, self-impact attribution, and responsibility flow  
**Depends On:** INV-018 (agency required), INV-012 (commitment gates responsibility), ARC-003 (E3), ARC-005 (control plane), ARC-004 (L-space), ARC-013 (residue geometry), ARC-007 (hippocampal systems)  
**Status:** provisional  
**Claim ID:** ARC-015
<a id="arc-015"></a>

---

Source: `docs/thoughts/2026-02-08_control_plane_modes_responsibility_flow.md`

## Agency and self-impact attribution

REE must support self-impact attribution: the ability to model which parts of incoming data were caused by the agent’s own outputs (efference copy / reafference), and to route that attribution into control-plane learning.

**Subsystem abstract (core claims):** ARC‑015 anchors agency/responsibility flow, while MECH‑023 and MECH‑024 frame
responsibility as path‑dependent geometry and the convergence of selfhood/personality/ethics. MECH‑057 adds the
agentic-extension claim: latent predictive world models require explicit self-attribution and control-plane completion
to remain stable under intervention. MECH‑060/061/062 extend this with explicit pre/post-commit error separation,
commit-boundary tokenization, and tri-loop commitment gating for attributable routing. Supporting context includes
INV‑018 (agency required), INV‑012 (commitment gates responsibility), ARC‑003 (E3), ARC‑005 (control plane), ARC‑004
(L‑space), ARC‑013 (residue geometry), ARC‑007 (hippocampal systems), and Q‑006/Q‑012 (developmental and convergence
falsifiability questions).

Without it:
- the system can still predict,
- it can even act,
- but responsibility cannot arise internally.

Learning would be about correlation, not ownership.

Responsibility requires the system to know, in a meaningful sense: *this change was because of me*.

## Why motor / policy systems are ethically central

Motor systems are not important because they move bodies. They are important because they instantiate **intervention capacity**.

The moment a system can:
- issue an output,
- predict its sensory consequences (via a fast loop),
- compare predicted versus observed reafference,
- and adjust future control policies,

it acquires:
- ownership of consequences (“this change was mine”),
- counterfactual sensitivity (“if I did otherwise, the world would differ”),
- morally shaped learning (“some interventions are constrained”).

This creates an internal responsibility flow. Responsibility attaches where action meets prediction error.

---

<a id="mech-023"></a>
## Responsibility as geometry, not choice (MECH-023)

Responsibility should not be located at a moment of discrete choice. It lives in the evolving geometry of possible futures.

Control-plane tuning and learning progressively:
- preserve some ethical degrees of freedom,
- collapse others,
- and shape what becomes thinkable, doable, or tolerable.

Two agents in the same state may differ morally because of how they arrived there. Responsibility is therefore path-dependent, history-bound, and non-Markovian.

---

<a id="mech-024"></a>
## Convergence of selfhood, personality, and ethics (MECH-024)

Selfhood, personality, relational identity, and ethics may not be separable modules.

- Selfhood corresponds to stable patterns of control sensitivity.
- Personality reflects long-run biases in tuning and learning.
- Relational identity reflects which others are included in error ownership.
- Ethics reflects which constraints are treated as inviolable.

Responsibility is a global property of this evolved control geometry, not a local rule.

---

<a id="mech-057"></a>
## Agentic extension requires control completion (MECH-057)

Latent predictive representation learning (for example, JEPA-like world-model framing) is likely necessary but
insufficient for stable agency.

Once an architecture moves from representation to intervention, it must support:

- action emission and consequence prediction,
- predicted-vs-observed reafference comparison,
- self-attribution of intervention effects,
- trajectory gating that preserves long-horizon coherence under uncertainty.

Without these loops, intervention can destabilize the model that is trying to predict intervention outcomes.
In REE terms, this means E1/E2 representational geometry must be completed by E3 commitment gating and control-plane
constraint routing, rather than replaced by them.

---

<a id="mech-058"></a>
## EMA target anchoring preserves E1/E2 substrate separation (MECH-058)

When JEPA-like substrate training is used for REE E1/E2, a slow target-anchor pathway (for example, EMA-updated target
encoder) should be treated as a stability requirement rather than an optimization trick.

Proposed role in REE terms:

- fast predictor updates support E2-like short-horizon adaptation,
- slow anchor updates preserve E1-like representational continuity,
- their separation reduces collapse/drift that would otherwise corrupt commitment-level attribution.

This mechanism is currently a candidate and needs direct ablation evidence in REE-shaped tasks.

---

<a id="mech-059"></a>
## Confidence channel must remain distinct from residual error (MECH-059)

Latent prediction residual and the confidence channel (uncertainty-derived precision) should remain distinct streams.

- residual answers: *how wrong was the prediction*,
- confidence channel answers: *how strongly should this error be trusted for control and learning*.
- uncertainty/dispersion remains an explicit input to confidence-channel computation.

Precision routing should consume both; confidence signals must not be collapsed into a single scalar error term.
Signed control semantics (harm/benefit channeling) remain a downstream REE control-plane function.

---

<a id="mech-060"></a>
## Dual error channels map to pre-commit and post-commit learning (MECH-060)

REE should maintain two explicit error channels around E3 commitment:

- pre-commit simulation error: from uncommitted rollouts/counterfactuals, used for gating/search,
- post-commit realized error: from executed committed trajectories, used for responsibility attribution and durable
  model update.

In JEPA-integrated systems this implies at least one exploratory/simulation-side error stream and one
execution-outcome stream; both are required and should not be merged.

MECH‑061 and MECH‑062 provide a concrete realization path for this split:

- MECH‑061: explicit commit-boundary token as error reclassification boundary,
- MECH‑062: tri-loop gate family whose arbitration determines which commitment becomes attributable.

### Commit-boundary enforcement contract

To preserve responsibility semantics, REE must enforce a strict boundary between pre-commit rehearsal and post-commit
attribution:

- Pre-commit channel (`sim_error`): may shape search/gating only.
- Post-commit channel (`realized_error`): may update durable policy/ledger/residue state.

Required implementation checks:
- No durable update paths are reachable from `sim_error` without a commit token.
- Every post-commit update is traceable to a commit token and action trace.
- Any mixed or contaminated channel event is tagged as a failure signature.

### Update-locus separation contract (learning boundary map)

To prevent cross-channel leakage and ledger corruption, learning/update permissions must be explicit by phase:

- `pre_commit` phase:
  - allowed writes: temporary rollout cache, gate-threshold scratch stats, proposal ranking buffers.
  - forbidden writes: policy weights, residue ledger, durable memory traces, attribution ledger.
- `commit_boundary` phase:
  - allowed writes: commit token, provenance tags, commit-scoped routing metadata.
  - forbidden writes: reward/residue attribution updates before realized outcome is observed.
- `post_commit` phase:
  - allowed writes: attribution ledger, residue/viability updates, durable policy updates, replay-priority updates.
  - required joins: `commit_id`, action trace, realized outcome trace.

Tri-loop note:
- Each gate family (motor, cognitive-set, motivational) may read the same commit token but should write only its own
  lane metrics pre-commit; cross-lane durable writes are post-commit only.

Primary hooks:
- `mech060:precommit_channel_contamination`
- `mech060:postcommit_channel_contamination`
- `mech060:attribution_reliability_break`
- `mech060:commitment_reversal_spike`

Design intent:
- Rehearsal is allowed to be broad and exploratory.
- Responsibility-bearing learning is narrow and commit-gated.

---

## Open Questions

<a id="q-006"></a>
### Q-006: Is ethics developmental rather than additive?

If REE can be refined using human-style cognition — with fast and slow predictors, hippocampal hypothesis injection, and a control plane that governs committed learning — and if systems “brought up well” under these constraints reliably tend toward ethical behaviour, then this would suggest that ethics is developmental rather than additive.

<a id="q-012"></a>
### Q-012: Can latent predictive world models remain agentically stable without REE-like control constraints?

Convergence weakens if large latent predictive agents remain stable without explicit self-attribution loops, trajectory
coherence pressure, or commitment-level gating.

It strengthens if scaling to embodied and multi-agent settings repeatedly requires:

- explicit efference/reafference ownership loops,
- control-plane arbitration across timescales,
- trajectory constraints that prevent destabilizing branches.

<a id="q-013"></a>
### Q-013: Can deterministic JEPA plus derived dispersion match explicit stochastic uncertainty heads for REE precision routing?

If deterministic predictors with derived dispersion estimates are sufficient, REE can keep substrate complexity lower.
If explicit stochastic/latent-variable heads produce materially better calibration under intervention, they may be
required for stable precision routing.

<a id="q-014"></a>
### Q-014: Do JEPA invariances hide ethically relevant distinctions in REE contexts?

Invariant representations can improve robustness, but may also suppress distinctions that matter for harm attribution,
responsibility boundaries, or social modelability. This remains an open empirical risk question.

## Related Claims (IDs)

- ARC-015
- MECH-023
- MECH-024
- MECH-057
- MECH-058
- MECH-059
- MECH-060
- MECH-061
- MECH-062
- INV-018
- INV-012
- ARC-003
- ARC-005
- ARC-013
- ARC-007
- Q-006
- Q-012
- Q-013
- Q-014
- Q-015
- Q-016

## References / Source Fragments

- `docs/thoughts/2026-02-08_control_plane_modes_responsibility_flow.md`
