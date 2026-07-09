# Parr, Pezzulo & Friston (2022) — *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*

**Claims touched:** ARC-016 (precision-to-commitment), ARC-021 / MECH-069 (three incommensurable error channels).
**Direction:** mixed — strong *supports* for the ARC-016 precision vocabulary, *weakens-leaning* for the strong form of the incommensurability claim.

## What the book is

This is the canonical, book-length synthesis of active inference by the framework's three principals. It is the natural target for WS-5 of the AI-design critique roadmap because REE's control-plane machinery — precision-weighted prediction error, action under uncertainty, exploration as information-seeking — is the free-energy program re-derived from biology, and REE's docs pointedly do not cite it. The book does two things REE needs: it (a) supplies a mature calculus REE currently only gestures at, and (b) states cleanly the single-functional position REE says it rejects, so that the rejection can be made precise instead of rhetorical.

## The math REE can inherit

Three pieces map onto REE's existing mechanisms with little friction:

1. **Precision as inverse variance.** Active inference weights every prediction error by a precision (inverse variance) term; raising precision makes sensory evidence dominate priors, lowering it makes priors dominate. This is exactly the lever ARC-016 built as "E3-derived prediction variance sets the commitment threshold" (EXQ-018b: `commit_threshold = 2 × training_baseline_variance`). REE has the mechanism; active inference has the closed-form and, crucially, the *units* (surprise in nats).

2. **Precision over policies (γ) as the commit-confidence control.** The book proposes that the precision of beliefs *about policies* — a scalar gain γ on the softmax over expected free energy — corresponds to dopaminergic discharge. This is the formal analogue of REE's beta-gate: the variable that decides how decisively a prediction converts to committed action. REE can adopt γ's update equations as the null model for its commitment gate.

3. **Expected free energy decomposes into epistemic + pragmatic value.** Action minimises `G(π)`, which splits into pragmatic/extrinsic value (expected log preference — reward/utility) and epistemic/intrinsic value (expected information gain — *salience* about hidden states, *novelty* about parameters). This is the principled exploration metric REE's control plane lacks: instead of a hand-tuned curiosity bonus, information gain is derived, and the explore/exploit trade-off is dissolved into one objective. WS-1's competence work and any future intrinsic-motivation mechanism (WS-9) should be scored against this decomposition rather than a bespoke novelty term.

## Where REE genuinely departs — stated precisely

Here is the point the roadmap flags as "partly a strawman." REE's standing objection to active inference is that it collapses everything into *one scalar*. That is only half right, and getting the other half right is the whole value of this entry:

- **What is *not* a real departure:** the mere existence of a single objective. Active inference already *factorizes* — the generative model factorizes over hidden-state factors, the approximate posterior is mean-field (a product of per-factor marginals), and `G(π)` is a *sum* of separable terms. So "active inference can only optimise one undifferentiated scalar" is false; it optimises a factorized functional. If REE's objection stops at "one scalar," it attacks a position no serious active-inference practitioner holds.

- **What *is* the real departure:** *commensurability*. In active inference, pragmatic value and epistemic value are both measured in nats and are therefore *summable by construction* — risk plus ambiguity is a well-defined single number. ARC-021/MECH-069 make the stronger claim that REE's three error channels (sensory-prediction, motor-sensory, harm/goal) have **no common currency at all** — that forcing them through a shared scalar mis-attributes credit *even after factorization*, because the errors are not merely separate terms but *incommensurable* quantities. The V3-EXQ-009 result (wider E2 capacity caused overfitting, not better harm attribution) is exactly this: the motor-sensory channel cannot learn harm attribution *regardless of capacity*, which a single-currency functional with enough parameters should eventually manage. That is the falsifiable edge: incommensurability predicts a forced-shared-loss ablation *fails to converge to correct credit assignment no matter the capacity*, where a factorized-but-commensurable EFE predicts it eventually succeeds.

So the honest framing is: REE is not rejecting a scalar *objective* (active inference factorizes freely); it is rejecting a shared *currency* across error types. Stated that way the departure is precise and testable, and it does not require pretending active inference is cruder than it is.

## Similarly for ARC-016's multi-axis precision

Active inference's precision is (typically) a scalar or low-dimensional gain on a common surprise currency. ARC-016 asserts *heterogeneous, multi-axis* precision — different precision on different functional channels. This is not supplied by the standard formalism, so it is a second documented departure: REE must show that single-currency precision cannot reproduce its mode transitions (focus / flow / panic / apathy), rather than assuming multi-axis precision is necessary. Until that is shown, ARC-016's multi-axis claim is a *hypothesised* enrichment of the active-inference precision lever, not an established one.

## Confidence

0.63, mixed. Source quality is high (the definitive synthesis). Mapping fidelity is strong for the precision import and weaker for the incommensurability departure, because on that axis the book supplies the *null hypothesis*, not support. The value of the entry is not that it confirms REE — it is that it lets REE state its two real departures (incommensurable currency; multi-axis precision) against the exact formal object they depart from, and inherit the precision/epistemic-value calculus for the many parts where REE is simply re-deriving. Cross-references: existing entries `targeted_review_connectome_arc_016/2026-03-28_arc_016_precision_weighting_action_friston2012` (Friston et al. 2012, dopamine/precision) and `targeted_review_q_044/2026-05-11_q_044_active_inference_epistemic_value_friston2015` (Friston et al. 2015, epistemic value) cover the primary-source precision and epistemic-value papers; this textbook is the synthesis that ties them together for the bridge doc.
