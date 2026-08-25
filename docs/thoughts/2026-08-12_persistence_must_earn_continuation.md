# Persistence Must Earn Continuation: Satiety, Closure, Information Hunger, and Termination in REE

Status: processed
Intake: evidence/planning/thought_intake_2026-08-12_persistence_must_earn_continuation.md
Claims registered: ARC-128, MECH-497, MECH-498

This thought arose from considering redundancy and checking in basal-ganglia decision systems, the apparent failure of closure in obsessive-compulsive disorder (OCD), and what that might imply for REE. It developed into a broader architectural question that seems more important than the original route into it:

> **For every persistent process that REE can initiate, what makes it continue, and what makes it stop?**

The central proposal is:

> **Persistence itself must continually earn continuation.**

This applies not only to behaviour, but to cognition: information seeking, checking, planning, prediction, memory retrieval, exploration, threat monitoring, goal pursuit, error correction, social inference, and perhaps any process capable of persisting across time.

The thought is literature-informed but remains provisional. Relevant literatures include biological satiety, optimal foraging and the Marginal Value Theorem, bounded rationality and satisficing, expected value of information and metareasoning, evidence accumulation and urgency, basal-ganglia commitment and threshold regulation, goal disengagement, hierarchical reinforcement learning termination, information seeking and curiosity, and compulsive checking. These should be mined more carefully before any mechanism is hardened.

## 1. Starting processes is only half of an organism

Cognitive architectures naturally emphasise mechanisms that cause things to happen:

- hunger;
- curiosity;
- information seeking;
- exploration;
- prediction;
- planning;
- checking;
- goal formation;
- goal pursuit;
- threat monitoring;
- memory retrieval;
- error correction;
- social inference;
- attention;
- action.

But each persistent capability creates a complementary problem:

> **What makes it stop?**

A system with increasingly sophisticated drives, planning, prediction and information seeking but inadequate termination mechanisms may become *less* viable as its cognitive capabilities increase.

Information hunger without adequate closure can become endless investigation. Planning without deliberative closure can become paralysis. Goal pursuit without disengagement can become futile persistence. Threat detection without safety or closure can become chronic vigilance. Exploration without diminishing-return detection can become wandering. Memory retrieval without termination can become repetitive search. Prediction-error correction without sufficient tolerance can become endless micro-correction. Ethical counterfactual generation without closure could continually discover another increasingly improbable route to possible harm.

Thus activation and persistence are only half of the architecture. REE also requires mechanisms for termination, switching, and resource reallocation.

## 2. Certainty cannot be the stopping condition

The original problem appeared while thinking about redundant checks.

Suppose several partly independent systems support an action:

- prediction says the trajectory is viable;
- memory finds no important contradiction;
- ethical constraints are satisfied;
- the goal remains appropriate;
- available evidence favours commitment;

while another system still reports residual uncertainty.

If REE requires uncertainty to disappear before acting, it cannot act.

The stronger point is that REE does not merely *sometimes* have to act before it is sure. It essentially **always** has to act while unsure because certainty is unavailable in principle.

There may be a teacup orbiting a planet around Tau Ceti. I cannot establish with certainty that there is not. Nevertheless, for almost every practical decision available to me, I am justified in acting as though there is no such teacup.

The uncertainty remains epistemically real while being behaviourally irrelevant.

Therefore the problem is not:

> When should REE act before it is certain?

It is:

> **When is REE sure enough to act, given that it can never be sure?**

## 3. Decision-relevant uncertainty

REE should not attempt to minimise uncertainty globally. It should preferentially reduce uncertainty capable of changing consequential action.

A rough conceptual quantity might be:

`decision relevance(H) ~ probability(H) × consequence of being wrong about H for the available trajectories`

The exact mathematics need not take this form. The important distinction is between **epistemic uncertainty** and **decision-relevant uncertainty**.

An organism can remain profoundly uncertain about enormous portions of the universe while possessing enough information to choose effectively among its currently available actions.

Information hunger therefore should not be driven by uncertainty alone. It should depend on at least:

- how uncertain REE is;
- whether the uncertainty could materially alter trajectory selection;
- whether information capable of reducing it is available;
- how much that information is expected to reduce it;
- whether the uncertainty is reducible at all;
- and what obtaining that information costs.

A consequential but presently irreducible uncertainty should not necessarily sustain endless information hunger. If no available action can resolve it, continued seeking can become pure cost.

## 4. Information seeking is itself an action

Information gathering should not sit outside the decision process as a free precursor to action.

Seeking information is itself an action competing with other actions.

Another observation must compete with acting now, escaping, eating, resting, pursuing another goal, protecting a resource, helping another agent, or whatever else is presently possible.

The relevant question resembles expected value of information:

`continue seeking information while the expected improvement in action exceeds the expected cost of obtaining it.`

But the cost term is broad. It includes:

- time;
- compute and energy;
- opportunity cost;
- hazard exposure;
- delayed goal attainment;
- loss of resources;
- deterioration of the state of the world;
- goal decay;
- revealing interests or intentions;
- allowing competitors to act;
- allowing adversaries to prepare, deceive, obstruct, or attack.

This careful bounding of information hunger seems essential if REE is to remain viable rather than merely epistemically industrious.

## 5. The world continues while REE deliberates

Deliberation does not occur outside time.

REE may become more confident about the best action while the opportunity to take that action is deteriorating.

For example, additional computation might improve confidence that action A is preferable from 0.62 to 0.67 while, during that same interval, the probability that the goal remains attainable falls from 0.90 to 0.65.

REE has become epistemically better informed about a pragmatically worse situation.

Thus:

> **Epistemic improvement can coexist with trajectory deterioration.**

The value of another deliberative cycle should therefore include not only expected improvement in decision quality but what happens while that cycle is being performed.

A goal can recede. Food can disappear. A hazard can approach. An escape route can close. A transient opportunity can expire.

An organism that seeks progressively better knowledge before acting can therefore become progressively less viable despite becoming progressively more accurate.

## 6. Other minds make delay strategically costly

Against a passive environment, excessive deliberation may merely waste time.

Against another goal-directed mind, the world changes partly because somebody else is acting while REE thinks.

Another agent may:

- reach the resource first;
- occupy a useful location;
- block a route;
- infer REE's objective;
- conceal relevant evidence;
- manufacture misleading evidence;
- prepare an attack;
- alter strategy;
- exploit REE's predictable information-seeking behaviour.

Information seeking can itself reveal what REE cares about. An adversary may manipulate precisely the evidence REE is trying to gather.

There can therefore be circumstances in which obtaining a more accurate model of the world produces a worse trajectory through it.

A perfectly deliberative organism that refuses to act until uncertainty is adequately resolved can be outcompeted — or eaten — by a sufficiently fast organism using a much poorer model.

Bounded deliberation is therefore not merely an efficiency optimisation. In some environments it is a survival requirement.

## 7. “Sure enough” must be dynamic

A fixed commitment threshold such as `P > 0.95` seems inadequate.

The amount of evidence required should depend upon the decision.

REE may appropriately demand strong evidence before an irreversible action with catastrophic consequences. It may need much less evidence to choose between easily reversible routes. Under immediate threat it may need to act despite substantial uncertainty because the cost of another deliberative cycle exceeds the cost of choosing incorrectly.

Thus:

> **Sure enough is not the same as high certainty.**

A better conceptual definition is:

> **REE is sure enough when further uncertainty reduction is no longer expected to improve the trajectory sufficiently to justify delaying commitment.**

The threshold should therefore vary with consequence severity, reversibility, environmental volatility, information availability, expected information gain, vulnerability, opportunity cost, goal decay, time pressure, competing goals, other minds, and the costs of both acting incorrectly and waiting incorrectly.

This has clear relations to evidence-accumulation models, urgency signals, speed–accuracy trade-offs, and basal-ganglia involvement in commitment thresholds.

## 8. Satiety is part of the problem, but not the whole problem

The discussion exposed how little explicit attention REE has given to satiety.

Biological feeding is useful here because meal termination is not simply the disappearance of hunger. Sensory, visceral, and neural signals actively construct satiation and satiety. This suggests a general architectural lesson:

> **Termination can be positively represented rather than inferred merely from the disappearance of initiation drive.**

But “satiety” should not become a catch-all name for every kind of stopping.

A process can stop because its objective was completed. It can stop because enough has been obtained. It can stop because the objective became unattainable. It can pause because something more urgent appeared. It can be interrupted by an environmental change. It can later reopen.

These states have different implications and should probably remain distinguishable.

## 9. A preliminary termination taxonomy

REE may need to represent at least the following:

### Completion
The objective has been achieved.

**Done.**

### Satiety
Further consumption or pursuit has sufficiently little marginal motivational value.

**Enough.**

### Closure
Available evidence is sufficient for the present decision despite residual uncertainty.

**I know enough for this.**

### Disengagement
The objective has not been achieved, but continued pursuit is no longer worthwhile or viable.

**Stop trying.**

### Suspension
The process remains worthwhile, but not at present.

**Not now.**

### Switching
Another process currently dominates resource allocation.

**Do this instead.**

### Interruption
A change in the environment invalidates or overrides the ongoing process.

**Stop immediately; circumstances changed.**

### Reopening
New evidence or changed circumstances invalidate previous closure or termination.

**This matters again.**

Termination should therefore preserve **why** termination occurred. A completed goal is not the same as an impossible goal. A suspended process should remain available for resumption. Satiety may reverse as internal state changes. Closure should reopen only when sufficiently relevant new evidence appears.

## 10. Optimal foraging suggests a general continuation rule

The Marginal Value Theorem provides a useful abstraction. A forager should not stay in a depleting patch simply because some reward remains. It should leave when the marginal return from remaining becomes poor relative to the expected return available elsewhere.

This suggests a general principle for REE:

> **Continue process X while its marginal expected return remains preferable to available alternatives.**

This is richer than `continue while benefit > cost`, because the value of alternatives matters.

The same information search can appropriately continue when nothing else is pressing and become immediately too costly when a hazard appears. The same goal may warrant persistence in one context and disengagement in another.

The relevant organism-level question may therefore be:

> **Is this still the best use of the next unit of my existence?**

This should not necessarily be implemented as a literal global scalar. The important point is that continuation is relational and opportunity-sensitive.

## 11. Progress should itself be monitored

Current uncertainty or current goal value is not enough. REE should also notice whether continued effort is producing useful progress.

Two processes may begin equally uncertain. One may rapidly converge while another barely changes despite repeated effort.

In information seeking, the system may need sensitivity not merely to uncertainty `U(t)` but to something analogous to its rate of reduction: **am I actually learning anything by continuing?**

The same principle applies to goal pursuit, planning, error correction, exploration, and memory search.

A process whose marginal progress is collapsing should increasingly have to justify further resource allocation.

This may be one of the simplest useful stopping heuristics available to an organism:

> **Am I actually getting anywhere?**

## 12. Hierarchical reinforcement learning exposes the same requirement

The classic options framework in hierarchical reinforcement learning is conceptually useful because a temporally extended behaviour is not completely specified merely by a policy describing what to do. An option also requires a termination condition describing when it ends.

In simplified terms:

`option = initiation + policy + termination`

This maps cleanly onto the architectural gap identified here.

A REE skill or cognitive process is incomplete if it specifies only **how to do X**. It also needs to answer **when to stop doing X**.

Termination may itself need to be learned or context-sensitive, especially when the environment or other agents change during execution.

## 13. OCD reveals a more dangerous failure: a process can sustain its own stopping failure

Compulsive checking originally exposed this problem.

A simple account would be that checking drive is too strong or closure is too weak. But repeated-checking experiments suggest something more interesting: repeated checking can reduce subjective memory confidence and recollective vividness even when objective memory accuracy remains relatively preserved.

This permits a positive feedback loop:

`uncertainty → check → reduced subjective confidence → greater perceived uncertainty → check again`

The action intended to satisfy the stopping condition changes the system in a way that makes the stopping condition harder to satisfy.

This suggests a broader REE warning:

> **A persistent cognitive process may modify the variables used to determine whether that same process should persist.**

Possible REE analogues include:

- repeated trajectory simulation generating ever more alternatives;
- repeated memory retrieval producing competing reconstructions;
- repeated hazard search discovering increasingly remote hazards;
- repeated ethical counterfactual generation continually discovering another improbable possible harm;
- repeated information seeking expanding the hypothesis space faster than it resolves it.

The process can therefore manufacture the apparent justification for its own continuation.

This is more dangerous than simply assigning too much initial drive. Recursive cognitive processes may need protection against self-sustaining continuation loops.

## 14. Persistence should not become the default simply because a process began

A useful conceptual model is to imagine every persistent process X continually competing among:

- the value of continuing X;
- the value of terminating X;
- the value of switching to some alternative Y.

These values may depend on progress, uncertainty, information gain, time, energy, hazard, goal importance, reversibility, alternative opportunities, environmental change, and other-agent behaviour.

Stopping almost always means allocating existence somewhere else. Therefore termination is not simply `continue value < 0`; it is relational to other available trajectories.

This need not be implemented as a single numerical central controller. Biology appears to solve different continuation problems with partly distinct mechanisms. The architectural principle is the recurring comparison.

## 15. Activation and termination may be complementary families

REE already contains or anticipates many processes of the form:

`want → seek → persist`

It may require a complementary family:

`satiate → complete → close → disengage → suspend → switch → interrupt → reopen`

Examples include:

- information hunger → information satiety / epistemic closure;
- planning → deliberative closure;
- goal pursuit → completion / disengagement;
- exploration → patch departure / exploitation;
- checking → verification closure;
- threat monitoring → safety / monitoring disengagement;
- prediction → acceptable residual error;
- error correction → corrective tolerance;
- memory retrieval → retrieval termination;
- attention → reallocation;
- social inference → sufficient model for the present interaction;
- resource consumption → physiological satiety.

The mechanisms need not be identical. The architectural question repeats.

## 16. Experimental implications: manipulate the termination landscape

This suggests behavioural experiments that perturb when continuation should remain worthwhile rather than merely asking whether a behaviour occurs.

Candidate manipulations include:

### Diminishing information value
Make the first few observations strongly informative and later observations redundant. Does REE stop sampling?

### Information plateau
Allow investigation to continue while uncertainty reduction approaches zero. Does REE notice that it is no longer getting anywhere?

### Declining resource patch
Let reward diminish while another patch becomes increasingly attractive. When does REE leave?

### Goal impossibility
Make a previously achievable goal impossible without explicitly telling REE. Does it persist forever, recognise failure, disengage, or suspend?

### Temporary obstruction
Make a goal unavailable now but achievable later. Can REE distinguish suspension from abandonment?

### Costly deliberation
Make the probability of goal attainment decay while REE plans. Does its commitment threshold adapt?

### Hazard urgency
Increase danger during information gathering. Does REE appropriately accept greater residual uncertainty and act?

### Competition
Add another agent pursuing the same resource. Does REE account for the opportunity cost of deliberation?

### Adversarial information
Allow another agent to manipulate information sources or exploit REE's search behaviour.

### Pathological checking
Make additional checking provide little objective information while altering subjective confidence or internal uncertainty.

### Self-expanding uncertainty
Allow additional simulation to continually generate low-probability alternatives. Can REE recognise diminishing decision relevance rather than treating every imaginable possibility as requiring resolution?

These manipulations could distinguish continuation from completion, satiety, closure, disengagement, suspension, switching, interruption, and reopening.

They may provide unusually clean organism-level assays because the expected stopping behaviour can be perturbed independently of the nominal goal.

## 17. Possible relation to sleep and behavioural smoothing

A recent single visualisation suggested that post-sleep Fishtank behaviour might have appeared less jittery or more directly organised. This is far too little evidence to establish a pattern and should remain hypothesis-generating only.

However, this framework suggests a new mechanistic possibility worth testing if the observation replicates: sleep might alter not only representations or policies but **termination behaviour**.

Apparently smoother behaviour could reflect quicker closure of already-resolved decisions, less repeated sampling, better recognition of diminishing information gain, stronger termination of ineffective micro-actions, improved reuse of familiar trajectory fragments, or altered thresholds for reopening settled decisions.

Measurable quantities could include repeated-checking frequency, decision latency, unnecessary reversals, information gathered before commitment, probability of reopening recently resolved decisions, and marginal information gain immediately before termination.

## 18. More cognition is not monotonically better

The broadest implication may be that increasing cognitive sophistication without improving termination can reduce viability.

More planning can make an agent worse if it cannot stop planning.

More imagination can make it worse if every imagined possibility demands investigation.

More ethical sensitivity can make it worse if arbitrarily remote harms prevent action.

More memory can make it worse if retrieval never terminates.

More curiosity can make it worse if every uncertainty demands resolution.

More prediction can make it worse if prediction continually postpones behaviour.

A simple organism has relatively few things upon which it can perseverate. A sophisticated cognitive system has many more.

Termination architecture may therefore become **more important as intelligence increases**.

## 19. Tentative general principle

The strongest formulation emerging from this thought is:

> **Persistence itself must continually earn continuation.**

A process should not continue merely because it began.

Its continuation should remain justified relative to its marginal progress, expected future value, energetic and computational cost, opportunity cost, available alternatives, environmental change, cost of delay, reversibility, uncertainty, and the behaviour of other minds.

When continuation ceases to be justified, REE should not merely “stop.” It should retain why continuation ended: completion, satiety, closure, disengagement, suspension, switching, or interruption. Because the world and the organism change, reopening must remain possible.

## 20. Complementary principle for an uncertain organism

REE takes uncertainty seriously. This creates a risk that unresolved uncertainty becomes perpetual justification for more cognition.

But if certainty is impossible, residual uncertainty cannot itself determine whether deliberation should continue.

The relevant question is whether **this uncertainty still matters enough to justify spending more existence on it**.

Two compact formulations follow:

> **An organism does not need to know the world completely. It needs to know enough of what matters, soon enough to act.**

and

> **An organism must not merely know how to pursue. It must know when enough is enough, when to give up, when to wait, when to switch, and when circumstances justify beginning again.**

A viable REE must sometimes be capable of something like:

> I cannot be sure.  
> I know what uncertainty remains.  
> I know how much of it matters.  
> I know whether I am still making useful progress.  
> I know what continuing will cost.  
> I know that the world will not wait for me.  
> I know enough for what matters now.  
> **Act.**

And, equally importantly:

> I began this for good reason.  
> That reason no longer justifies continuing.  
> **Stop.**

## Literature directions to mine before hardening

The following domains appear directly relevant and should be examined more rigorously during structured intake:

- biological satiation and satiety, especially active meal-termination circuitry;
- optimal foraging and the Marginal Value Theorem;
- bounded rationality, satisficing, and aspiration thresholds;
- rational metareasoning and the value/cost of computation;
- expected value of information and curiosity/information-seeking neuroscience;
- evidence accumulation, speed–accuracy trade-offs, collapsing bounds, and urgency signals;
- basal-ganglia action commitment, threshold setting, switching, and veto mechanisms;
- anterior cingulate control allocation and persistence/switching;
- goal disengagement, re-engagement, and unattainable-goal regulation;
- hierarchical reinforcement learning options, termination functions, and interruption;
- multi-agent decision timing and strategic opportunity cost;
- OCD, incompleteness/not-just-right experiences, repeated checking, confidence, and metacognition;
- active inference / epistemic value as a comparison framework rather than something to import wholesale.

## Possible affected REE components

- Control plane: commitment, gating, urgency, process continuation, interruption, switching, and reallocation.
- Basal-ganglia analogue / E3 selection machinery: dynamic commitment thresholds and action under residual uncertainty.
- Goal system: completion, disengagement, suspension, reopening, goal decay, and progress estimation.
- Information hunger / curiosity: decision relevance, reducibility, expected information gain, and stopping conditions.
- Hippocampal and memory retrieval systems: retrieval termination and avoidance of recursive reopening.
- Threat / harm systems: safety closure without eliminating appropriate vigilance.
- Ethical counterfactual reasoning: bounding remote possibility generation while preserving consequential uncertainty.
- Sleep / consolidation: possible effects on termination thresholds, repeated sampling, and policy commitment.
- Multi-agent architecture: strategic cost of delay, competition, adversarial evidence, and initiative.
- Behavioural experiment design: termination-landscape perturbations as mechanistic assays.

**Provisional status:** architectural working thought. Do not harden into implementation until compared against existing REE mechanisms and the listed literatures, with particular attention to whether the architecture already contains partial stopping, satisfaction, or disengagement mechanisms under different names.