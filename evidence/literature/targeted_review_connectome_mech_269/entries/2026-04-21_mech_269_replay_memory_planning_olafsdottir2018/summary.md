# Ólafsdóttir, Bush & Barry (2018) — "The Role of Hippocampal Replay in Memory and Planning"

**Current Biology** 28:R37–R50. [DOI](https://doi.org/10.1016/j.cub.2017.10.073). PMID 29316421.

*(According to PubMed.)*

## What the paper does

The authors review the case that hippocampal replay is not a single process but a family of processes recruited differently across tasks. They catalogue the range of functions replay has been proposed to subserve — systems consolidation, recall, spatial working memory, navigational planning, reinforcement learning — and argue that the observed inconsistencies in the field are partly explained by the function of replay changing dynamically with task demands and arousal level. Their central move is to deny that any one functional story owns replay, and to argue instead that what replay is doing depends on when you look.

## Findings relevant to MECH-269

This review's architectural shape is closer to MECH-269 than any other paper I pulled. MECH-269 predicts that the hippocampal proposer's mixture of anchored and probe output is modulated by context — heartbeat / dACC / salience gating produces a different anchor/probe ratio under high-harm versus low-threat conditions. Ólafsdóttir et al. propose, without using this language, that replay mode is similarly context-conditioned.

They do not identify the gating variable. Their discussion is organised around task demand and arousal, which are composite quantities — salience, precision, reward expectancy, and prediction error all ride on them. MECH-269 commits to one specific component of that composite: per-stream verisimilitude. The review is consistent with MECH-269 being the right decomposition of the composite, but does not directly test it.

## How it translates to REE

For REE, the most useful move in the review is their pressure toward taking the task-dependence seriously. A V3 experiment testing MECH-269 should therefore not just look at baseline replay statistics — it should manipulate context (harm-load, novel vs familiar, task phase) and check whether the anchor/probe ratio follows per-stream V_s specifically or whether it follows a simpler arousal/salience composite. If it only follows arousal, MECH-269 is redundant with existing precision-weighting claims and should be collapsed.

The review also implicitly supports MECH-271's routing reframe: if replay function changes with task, then its downstream consequences should too, and "different routing to different consumers in different modes" is a natural implementation of what the authors are describing.

## Limitations and caveats

The review is advocacy for context-dependent function without committing to the gating variable. It is compatible with MECH-269 but does not isolate the specific claim from competitors (global precision, arousal, salience). Counting it as strong MECH-269 evidence would overweight its directness.

Rodent-only. Translation to REE's latent-stack decomposition requires granting that per-stream prediction-alignment is what rodent studies see as "task demand" — a plausible but not established identification.

## Confidence reasoning

Source quality is high (Current Biology review; established Barry lab). Mapping fidelity is the strongest piece: the review's architectural shape (context-dependent, task-modulated, functionally switching replay) is structurally isomorphic to MECH-269's anchor/probe mixture. Transfer risk is present but bounded — the paper speaks directly to the kind of functional differentiation MECH-269 needs, even if it does not commit to the specific gating variable. Net confidence 0.70.
