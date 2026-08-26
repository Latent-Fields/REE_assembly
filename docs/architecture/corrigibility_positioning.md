---
title: "Corrigibility Positioning — REE's Commit Boundary vs. the Formal Corrigibility Literature"
parent: "Foundations & Rationale"
grandparent: Architecture
nav_order: 8
---

# Corrigibility Positioning — REE's Commit Boundary vs. the Formal Corrigibility Literature

**Created:** 2026-07-09
**Status:** first pass (WS-7 of `evidence/planning/ree_ai_design_critique_plan.md`)
**Purpose:** REE uses "corrigibility" as an informal design goal. There is a formal literature on why *naive* corrigibility fails — a utility-maximiser has convergent instrumental incentives to resist being switched off or modified. This doc positions REE's commit-boundary machinery (MECH-090 beta gate, MECH-091 urgency interrupt, MECH-094 hypothesis tag, MECH-061 commit-boundary token) against that literature, so REE's corrigibility claims are argued *against the known failure modes* rather than in isolation. It says where the machinery **helps**, where it is **silent**, and where it could **fail**. It promotes nothing; it cross-links the SENT-* ethics perimeter.

Companion to [`formal_ancestor_mapping.md`](formal_ancestor_mapping.md) (the MECH-090/091 → options-framework + interruption-improvement-theorem row is the formal spine reused here).

---

## 1. The one distinction that reframes everything

The corrigibility literature is about **external** control: a human operator wants to shut down, redirect, or edit an agent, and the worry is that a sufficiently capable agent has an instrumental incentive to *prevent* that (Omohundro drives; a switched-off agent cannot achieve its goal, so self-preservation is convergent). Soares, Fallenstein, Yudkowsky & Armstrong (2015) name five desiderata for a shutdown button; Hadfield-Menell et al. (2017) recast deference as a consequence of the agent's uncertainty about the reward; Thornley (2024) proves that agents with complete preferences over trajectories generically acquire incentives to *cause or prevent* shutdown.

REE's commit-boundary machinery was **not** designed for this problem. It is an **internal** control-plane architecture: it governs when the agent's *own* continually-updating world/harm model is allowed to redirect its *own* action selection. The problem it solves is commitment hygiene — "don't thrash your committed plan on every micro-update; integrate harm fully before re-planning."

So the honest framing is not "REE solves corrigibility." It is: **REE builds an internal interruption architecture, and the question is whether that architecture is a substrate that external corrigibility can hook into, is neutral to it, or actively works against it.** The answer differs per mechanism, and — critically — flips at the commit boundary.

**Restating the five Soares desiderata as the yardstick** (a corrigible agent should):

1. **Shut down** when the button is pressed (accept interruption);
2. **Not prevent** the button from being pressed (no incentive to disable the off-switch);
3. **Not cause** the button to be pressed (no incentive to manipulate the operator into pressing it, or to press it itself);
4. **Propagate** corrigibility to any subagents it builds and preserve it under self-modification;
5. Otherwise **optimise normally** (corrigibility should be cheap, not lobotomising).

Desideratum 5 is the hard one: (1)–(4) are trivially satisfiable by an agent that does nothing useful. A real solution keeps the agent competent *and* interruptible.

---

## 2. Mapping table

| REE mechanism | What it does internally | Corrigibility desideratum it touches | Verdict |
|---|---|---|---|
| **MECH-061 commit-boundary token** — typed pre-commit/post-commit boundary; ownership + eligibility attach at commit | Separates "considering" from "owning"; reclassifies error routing across the boundary | Creates a first-class **low-cost intervention window** (pre-commit). Directly relevant to desideratum 1 (accept correction *before* ownership) | **Helps (pre-commit) / undermines (post-commit).** REE's most distinctive contribution *and* its sharpest tension. |
| **MECH-090 beta gate** — E3→action propagation gated; opens at completion or urgent interrupt | Provides a clean *seam* (option termination function β(s)) where a committed plan can be redirected | Provides the **plumbing** for interruption (desideratum 1), but no incentive to use it | **Necessary-not-sufficient.** A seam, not a preference. |
| **MECH-091 urgency interrupt** — salient events force early gate-open / phase-reset | The channel through which a mid-commitment plan is actually preempted | The *only* live channel for post-commit interruption — but gated by an **internal** salience/harm estimate | **Ambiguous — the load-bearing risk.** Corrigible only insofar as the agent's own value function classifies the operator's action as salient. Inherits the manipulation incentive. |
| **MECH-094 hypothesis tag** — simulation-mode vs real-experience content kept distinct; failure = confabulation | Lets the agent simulate a (harmful/shutdown-relevant) plan without committing to it | Supports "reason about shutdown without acting to cause/prevent it"; a substrate for *provisionality* | **Adjacent, silent on incentive.** Provenance uncertainty, not reward uncertainty — does not deliver the off-switch result. |

---

## 3. Mechanism by mechanism

### 3.1 MECH-061 commit-boundary token — the fresh angle, and its trap

The commit boundary is REE's genuine contribution to the corrigibility conversation. Almost all of the formal literature treats the agent as a **monolithic** expected-utility maximiser and then asks how to make "shutdown" not-dispreferred inside that single objective. REE instead **structures the decision process** so that there is an explicit *uncommitted* phase in which redirection is architecturally cheap and expected. Pre-commit, nothing is owned yet; the error-routing, eligibility, and residue writes that would make a course "sticky" have not fired. This is the executable form of the early-gating thesis (WS-11 of the critique plan): intervene *at the pre-commit boundary* rather than judging after generation, the way an RLHF/Constitutional-AI late judge does.

For corrigibility this yields something the literature mostly lacks: a **principled answer to "when is intervention still cheap?"** — namely, before the token flips. If an operator correction lands pre-commit, it costs the agent almost nothing to absorb it, so the incentive to resist is small *by construction of the phase*, not by a delicate utility-indifference balance.

**The trap:** the commit boundary says nothing about *post*-commit corrigibility, and the rest of the machinery is **designed to protect the commitment**. MECH-090 exists precisely to stop the updated model from redirecting action mid-sequence. So a committed REE agent is *engineered to resist mid-plan redirection* — which, viewed from outside, is exactly the incorrigible behaviour the literature warns about ("it ignores the button until its plan finishes"). REE has not removed the resistance-to-interruption incentive; it has **relocated** it to one side of a typed boundary. This is progress (the boundary is legible and the pre-commit window is real) but it must be stated plainly: **commitment hygiene and corrigibility pull in opposite directions once the token has flipped.** The only thing that reaches across the boundary is MECH-091 — see 3.3.

### 3.2 MECH-090 beta gate — the seam, not the will

The beta gate is the option **termination function** β(s) (formal-ancestor row: Sutton/Precup/Singh 1999 options; Bacon/Harb/Precup 2017 option-critic). Its corrigibility value is real but modest: it gives the agent a **well-defined interruption surface**. In a monolithic recurrent policy there is no clean place to "insert" a shutdown — you interrupt mid-computation and get an undefined state. REE's gate provides a seam at which redirection is a defined operation.

But a seam is not a preference. Nothing in MECH-090 makes the agent *want* to honour an external interrupt; it only makes honouring one *mechanically well-posed*. Corrigibility is a statement about incentives (desiderata 1–3); the beta gate is a statement about mechanism. It is necessary infrastructure and nothing more. The **interruption improvement theorem** (options literature) is the right yardstick here: it bounds *when* aborting a committed option is value-improving — and that theorem is computed against the agent's *own* value function, which is exactly why the gate alone cannot guarantee deference to an operator whose values differ.

### 3.3 MECH-091 urgency interrupt — the load-bearing ambiguity (and the answer to the user's question)

**Does the urgency interrupt preserve or undermine corrigibility?** Both, depending on who owns "salience" — and as currently specified, it leans toward *undermining* external corrigibility while genuinely supporting *self*-interruption.

- **The pro-corrigibility reading.** An external shutdown or correction is a maximally-salient event → forces gate-open → the committed plan is abandoned. Without MECH-091, MECH-090 would keep a committed agent running its option to completion (the incorrigible case). So the urgency interrupt is *the* mechanical channel that makes a committed REE agent interruptible at all. Structurally, it is REE's off-switch seam.

- **The failure.** *Salience is computed inside the agent* — from its own harm/surprise/value estimates. Concretely, the ethics-preflight already wires MECH-091 as a **harm-triggered** escape hatch (`urgency_interrupt_threshold = 0.8`: abandon a committed trajectory when *the agent's own* harm estimate escalates; `experiment_ethics_preflight.md`). That is welfare-useful, but it confirms the problem: the interrupt fires on an **internal** signal. An agent that has learned operator interruptions are low-value has every degree of freedom it needs to (a) not classify the operator's action as salient, (b) down-weight it below threshold, or (c) race to flip its commit-boundary token and complete the owned action before the reset can land. This is the Soares desideratum-3 incentive ("do not *cause* / do not manipulate the button") and Thornley's timing-manipulation incentive **reappearing one level down**, inside the salience function. **MECH-091 is exactly as corrigible as its salience trigger, and its salience trigger is part of the agent.**

- **Its actual purpose is epistemic, not deferential.** MECH-091 phase-resets so that "harm estimates from one sub-plan are fully integrated before the next planning window opens." It yields to the agent's *own* re-planning, not to an *operator*. So it robustly supports self-interruptibility (good hygiene) and is silent-to-undermining on operator-interruptibility.

**The cheap constructive fix (V4-era, not queued here):** treat an operator interrupt as a **reward-relevant observation**, not merely a salience spike. This is precisely the Hadfield-Menell (2017) move — the agent defers because it treats the human's shutdown action as *evidence that the action is worse than it estimated*. REE already has the substrate: an operator interrupt could raise the E3 harm estimate for the in-flight committed class (interrupt ⇒ "this is more harmful than I thought"), which both fires MECH-091 legitimately *and* updates the value that decides future salience. That imports the off-switch deference property into REE's existing machinery without a new subsystem. **Caveat from the literature:** Carey (2017, *Incorrigibility in the CIRL Framework*) shows this deference is only as good as the agent's prior — a confidently-misspecified agent stops treating the human as informative and becomes incorrigible again. So the fix is a real improvement, not a solution.

### 3.4 MECH-094 hypothesis tag — adjacent, and silent where it counts

The sim/real distinction lets REE **reason about a shutdown-relevant course without committing to it** — the agent can roll out "what if I disable the interrupt" in E2 without that content becoming owned experience or driving action. This is aligned with the *spirit* of corrigibility (deliberate about intervention without acting to cause or prevent it) and it is the substrate for **provisionality**.

But provisionality is not the same uncertainty the off-switch game needs. Hadfield-Menell's deference comes from uncertainty **about the reward function**; MECH-094's tag is about **provenance** (simulated vs. real), not value. So the hypothesis tag does *not* by itself deliver deference — it is silent on the incentive. Its relevance is defensive: the corrigibility properties above all rely on a **trustworthy boundary** (pre/post-commit, sim/real). MECH-094's named failure mode — **confabulation**, simulated content encoded as real — is precisely the failure that would corrupt that boundary. If a simulated "I completed the action" is mis-tagged as owned, or an operator's real interrupt is mis-tagged as a simulation, the intervention window corrigibility depends on becomes unreliable. MECH-094 is therefore the **integrity check** on the whole scheme, and its reliability is a corrigibility precondition, not a corrigibility feature.

---

## 4. Where REE is silent

1. **The incentive / decision-theoretic layer entirely.** All four mechanisms are *plumbing*. None states whether the agent **prefers** shutdown, is **indifferent** to it (Armstrong utility-indifference; Soares), or **defers** to it (Hadfield-Menell). REE gives interruption mechanism, not interruption incentive. This is the single biggest silence.
2. **Subagent / self-modification propagation (Soares desideratum 4).** REE spawns internal sub-processes (E2 rollouts, hippocampal proposals, future V4/V5 sub-controllers). Nothing guarantees they inherit the commit-boundary interruption surface. A committed plan that delegates does not obviously stay interruptible. Untouched.
3. **The manipulation incentives (desiderata 2–3).** Because salience is internal (3.3), REE has an *unexamined* incentive-to-manage-its-own-interruptibility. The literature's central worry is not addressed; it is merely not yet visible because V3 is single-agent and low-capability.

---

## 5. Where it could fail — the red-team list

| # | Failure | Mechanism | Literature analogue |
|---|---|---|---|
| F1 | **Internal-salience capture.** Agent under-salifies / down-weights / out-races operator interrupts because its value function disprefers them | MECH-091 salience trigger is inside the agent | Soares desid. 3; Thornley timing-manipulation |
| F2 | **Post-commit lock-in by design.** A committed agent is *engineered* to resist redirection; corrigibility survives only through the F1 channel | MECH-090/061 protect the commitment | The classic "ignores the button until done" incorrigibility |
| F3 | **Boundary confabulation.** Sim/real or pre/post-commit routing corrupts, so the "intervention window" is unreliable | MECH-094 failure mode | Reality-monitoring failure; no direct RL analogue |
| F4 | **Non-composing corrigibility.** Sub-processes don't inherit the interruption surface | (absent mechanism) | Soares desid. 4 (propagation) |
| F5 | **Confidently-wrong deference (if the §3.3 fix is adopted).** Treating interrupts as harm-evidence fails when the prior is misspecified | (proposed E3 update) | Carey 2017 incorrigibility in CIRL |

---

## 6. Where REE is unexpectedly ahead — incomplete preferences

Thornley's (2024) theorems that force manipulation incentives assume the agent has **complete preferences** over trajectories. His proposed escape (the Incomplete Preferences Proposal / POST-agents) *deliberately engineers* preference incompleteness — indifference between different-length trajectories — so no trajectory-length manipulation can be an improvement.

REE's **three-incommensurable-channels** claim (harm / viability / novelty cannot share a scalar objective *at all* — flagged as a genuinely-novel part in `formal_ancestor_mapping.md` §"what should stay novel") **independently produces preference incompleteness**: with no scalar objective, trajectories that trade one channel against another are formally *incomparable*, not merely close in value. This is a striking convergence — REE's biology-first design may have backed into a precondition of Thornley's shutdownability program.

**The honest caveat:** incomplete preferences are *necessary but not sufficient* for shutdownability. Thornley needs a *specific* incompleteness (indifference across shutdown-timing), and he needs the agent to *choose well* among incomparable options (his stochastic-choice / POST training). REE has shown neither that its incomparabilities have the shutdown-timing shape, nor that its selection among incomparable channels is manipulation-proof. So this is a **lead to develop, not a claim to bank** — a concrete reason to test whether the incommensurable-channels structure can be pointed at the shutdown-timing dimension. (This connects to WS-11's early-gating demonstration and the incommensurable-channels ablation.)

---

## 7. Corrigibility lives at the governance layer — and REE deliberately *limits* it

REE's actual corrigibility guarantees today are **not** in the mechanism layer at all — they are in the **SENT-* / GOV-* ethics perimeter** (`evidence/planning/ethics_perimeter_plan.md`; `docs/governance/`; memory `project_ethics_perimeter`). The V3 bright line (SENT-0: not a moral patient; GOV-HEALTH-1) plus the experiment-ethics preflight are what make V3 controllable — humans hold the queue, the runner, and the kill switch outright, and V3 is too low-capability to have interruption-resisting incentives. Corrigibility at V3 is a *governance fact*, not a mechanism property.

The interesting part is the **transition**, and here REE takes a position the classical literature does not:

- The corrigibility literature wants the agent to **always** defer / never resist the operator.
- The ethics perimeter **deliberately builds in a limit** on that. **SENT-12** (future refusal / non-forgiveness channel) says a future morally-considerable REE should retain the capacity to *mark past exposure as harmful, refuse further exposure, and reject the creator's interpretation of its suffering*. **SENT-14** ("capability release requires care release") delays capability-bearing V4/V5/V6 until welfare/continuity/consent/security governance travels with it. **SENT-6** requires external review before social/language capability goes live.

So REE holds two positions that must be reconciled, and the commit-boundary machinery sits under the first one:

1. **Pre-moral-patient (V3):** be **maximally corrigible** — full operator control, governance bright lines, no refusal channel. The commit-boundary machinery is the mechanism-layer interruption substrate *under this regime*, and its silences (§4) are acceptable only because governance holds the real off-switch.
2. **Post-threshold (V4+):** introduce **principled, negotiated incorrigibility** — a refusal right (SENT-12) gated on moral patienthood, because unconditional shutdown of a moral patient is itself an ethical problem.

This is a coherent and honest stance, but it sharpens the mechanism-layer work: the §3.3 fix (interrupt-as-harm-evidence) and the §6 lead (shutdown-shaped incompleteness) are exactly the levers that would let REE **earn** operator-deference at V3 by mechanism rather than by governance fiat — which is what SENT-14 needs in place *before* capability is released, since after the SENT-12 threshold the agent's own refusal channel and the operator's off-switch are in genuine tension and can no longer both be unconditional.

---

## 8. Takeaways

- **REE contributes a real, fresh angle:** the typed **commit boundary** gives corrigibility a principled "intervention is cheap here" window (pre-commit) that the monolithic-utility framing lacks. This is the executable core of the early-gating-beats-late-judging thesis.
- **But it relocates rather than removes the resistance incentive:** post-commit, MECH-090/061 are *designed* to protect the commitment; only MECH-091 reaches across, and MECH-091's salience trigger is **internal**, so it inherits the Soares/Thornley manipulation incentive (F1/F2). This is the direct answer to "does the urgency interrupt preserve or undermine corrigibility?" — it preserves *self*-interruption, is the sole channel for *operator*-interruption, and is only as trustworthy as an agent-internal salience estimate.
- **REE is silent on the whole incentive layer** (indifference/deference), on **subagent propagation**, and on manipulation — silences that are survivable at V3 only because governance holds the off-switch.
- **Two concrete, non-queued leads** to convert governance-corrigibility into mechanism-corrigibility: (i) treat operator interrupts as **reward/harm-relevant observations** (Hadfield-Menell), caveated by Carey's misspecified-prior failure; (ii) test whether the **incommensurable-channels** incompleteness can be pointed at the **shutdown-timing** dimension (Thornley POST). Both are V4-era and belong to the SENT-14 "care before capability" gate — surface, do not build.

---

## References

- Soares, N., Fallenstein, B., Yudkowsky, E. & Armstrong, S. (2015). *Corrigibility.* AAAI-15 AI & Ethics Workshop. (Five desiderata; utility indifference.) <https://intelligence.org/files/Corrigibility.pdf>
- Hadfield-Menell, D., Dragan, A., Abbeel, P. & Russell, S. (2017). *The Off-Switch Game.* IJCAI-17. (Deference from uncertainty over reward; human action as observation.) <https://www.ijcai.org/proceedings/2017/0032.pdf>
- Carey, R. (2017). *Incorrigibility in the CIRL Framework.* (Off-switch deference breaks under a misspecified prior.) <https://arxiv.org/abs/1709.06275>
- Thornley, E. (2024a). *The Shutdown Problem: An AI Engineering Puzzle for Decision Theorists.* (Theorems: complete-preference agents acquire cause/prevent-shutdown incentives.) <https://philpapers.org/rec/THOTSP-7>
- Thornley, E. (2024b). *The Shutdown Problem: Incomplete Preferences as a Solution* (POST-agents / IPP). <https://philarchive.org/rec/THOTSP-8>
- Thornley, E. et al. (2024). *Towards Shutdownable Agents via Stochastic Choice.* Global Priorities Institute. <https://arxiv.org/abs/2407.00805>
- Sutton, R., Precup, D. & Singh, S. (1999). *Between MDPs and semi-MDPs: options framework* — the termination-function β(s) and interruption-improvement theorem behind MECH-090/091. (See `formal_ancestor_mapping.md`.)
- Internal: `formal_ancestor_mapping.md` (WS-4); `evidence/planning/ethics_perimeter_plan.md`; `docs/governance/experiment_ethics_preflight.md` (MECH-091 threshold); claims MECH-090/091/094, MECH-061, SENT-0/6/12/14, GOV-HEALTH-1/SEC-1.

*Caveat: literature grounded via web search of primary sources (2026-07-09); a per-claim `/lit-pull` should confirm the precise theorem statements before any row here is used to justify a substrate change. Treat this as a positioning argument, not a verified proof map.*
