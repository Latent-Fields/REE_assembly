# Kulkarni, Narasimhan, Saeedi & Tenenbaum (2016) — Hierarchical Deep RL: Integrating Temporal Abstraction and Intrinsic Motivation

**NeurIPS 29 · [arXiv:1604.06057](https://arxiv.org/abs/1604.06057)**
**Claim tested: MECH-428 · direction: supports · confidence: 0.66**

## What the paper did

h-DQN is a two-level hierarchy. A meta-controller learns a policy over *intrinsic goals*; a controller learns a policy over atomic actions to satisfy whichever goal is currently set; an internal critic decides whether the goal has been reached and issues the controller its reward. The two levels operate at different temporal scales.

They test it on two problems chosen for very sparse, delayed feedback: a synthetic stochastic decision process, and Montezuma's Revenge. The comparison that matters is the second one, because flat DQN scores **zero** there. Not "worse" — zero. The hierarchical agent learns.

## Why this speaks to MECH-428

MECH-428 is written for a specific and, in REE, dominant failure: the superordinate goal cannot be seeded directly because the terminal benefit that would instantiate it is rarely or never reached. The claim's own notes record what that looks like in practice — `z_goal_norm < 0.1` "in every iteration", EXQ-085f/g, EXQ-233 and EXQ-536a/b all failing *at* the seeding step, GAP-2 in the goal pipeline blocked because the agent never reaches self-sustaining benefit contact.

Montezuma's Revenge is the cleanest published instance of the same antecedent, and flat DQN's zero is its computational counterpart. So the paper is testing MECH-428's mechanism in MECH-428's regime, which is more than most candidate anchors manage.

The correspondences are close enough to be worth stating one at a time. The internal critic rewarding subgoal attainment is the functional analogue of the proxy/progress feedback MECH-428 depends on. The meta-controller learning a policy *over* goals is the analogue of a structured z_goal attractor (MECH-112/MECH-230) becoming trainable. And the headline result — the subgoal layer converts an unlearnable problem into a learnable one under exactly this sparsity — is the outcome MECH-428 predicts.

## The limitation that decides this entry

The meta-controller **exists from initialisation**. It is an architectural component present before any learning happens; subgoal attainment makes it *trainable*, but it does not bring it into being.

MECH-428 claims something stronger. It says cross-level credit from repeated subgoal attainment can **create** the parent goal where direct seeding failed to produce one — that this is the formation-direction complement to MECH-427's maintenance direction. h-DQN gives you "subgoals rescue an otherwise-unlearnable superordinate goal". It is silent on "subgoals constitute the superordinate goal". Those are different claims and only the second is MECH-428's distinctive content.

I want to be careful about how much that concession costs, because I do not think it costs everything. If the objection to MECH-428 is that a parent goal *cannot* be given useful structure by subordinate success in a regime where it never gets direct contact, this paper answers it. If the objection is that the parent has to *pre-exist* for any of it to work, this paper does not answer it and mildly corroborates the objection. That distinction is exactly what the planned EXP-0390 would have to resolve, and it is worth designing the arm so the parent structure is *absent* at initialisation rather than merely untrained — otherwise the experiment reproduces h-DQN's result and inherits its ambiguity.

Two further caveats. The subgoals are hand-specified via a bespoke object detector, so the result presupposes that someone already knows the useful decomposition — for REE that is closer to `scaffolded_sd054_onboarding`'s external scaffold than to MECH-428's internal complement. And the absolute Montezuma scores are modest; subsequent literature found hierarchical-RL results of this vintage fragile and hard to generalise past the tuned domain, which is why source quality here sits at 0.75 rather than at the venue's face value.

## Confidence reasoning

Source quality 0.75 — NeurIPS, very widely cited, discounted for the fragility of the headline result in follow-up work. Mapping fidelity 0.65 — the regime match is excellent and the architectural correspondence is real, but the pre-provided parent is a genuine gap against the claim's distinctive content. Transfer risk 0.35 — same machine class as REE, so low, with the residual reflecting Atari's discrete, object-rich structure versus REE's environments. Aggregate 0.66.
