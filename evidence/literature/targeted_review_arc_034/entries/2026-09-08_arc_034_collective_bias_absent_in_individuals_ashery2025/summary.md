# Emergent social conventions and collective bias in LLM populations (Ashery, Aiello & Baronchelli, 2025)

## What the paper did

Ashery, Aiello and Baronchelli took the classical naming game -- a minimal coordination
protocol from the study of human convention formation -- and ran it over populations of LLM
agents. On each round, two randomly paired agents independently choose a name from a shared
pool; they receive +100 points if the choices match and -50 if they do not, and each agent
carries only a short private memory of its own recent interactions (window H=5). There is no
central coordinator, no global view, and no agent that can see the population. Four models were
tested (Llama-2-70b-Chat, Llama-3-70B-Instruct, Llama-3.1-70B-Instruct, Claude-3.5-Sonnet), at
N=24 with a pool of W=10 names, scaled up to N=200 with the full 26-letter alphabet, over 40
independent runs for the main experiments.

Crucially -- and this is the part that makes the paper useful rather than merely interesting --
they ran the control. Before any interaction history exists, with memory empty, do individual
agents have a preference among the names? They tested this directly and found no statistical
bias: p=0.410 for Llama-2-70b-Chat, p=0.100 for Claude-3.5-Sonnet.

## Key findings relevant to ARC-034

Three results matter here. First, global conventions emerged: populations interacting only in
local pairwise exchanges converged on a single universally adopted name, with no mechanism
that could have coordinated them. Second, and this is the load-bearing finding, *strong
collective biases emerged even though the agents exhibited no bias individually*. Populations
did not converge uniformly across the name pool; they converged asymmetrically, with reported
selection probabilities reaching 0.848 against 0.451 for alternative labellings, and the
asymmetry was already visible by the third interaction. Third, committed minorities of
adversarial agents could overturn an established convention, but the critical mass required
was sharply model-dependent -- 5 agents for Claude-3.5-Sonnet, 6 and 10 for the two Llama-3
variants, 16 for Llama-2-70b-Chat, i.e. 12.5% to 66.7% of an N=24 population.

## How this translates to REE

ARC-034 asserts that a REE system can be locally well-behaved at every pairwise (n=1)
interaction and still produce a problematic emergent collective state at n=k, and therefore
that ethics testing must sample nth-order multiagent trajectory distributions rather than
pairwise probes. The structural premise underneath that claim -- that a population-level
property can exist which is *provably absent* from every constituent measured in isolation --
is exactly what this paper demonstrates, and demonstrates with the control that such
demonstrations usually lack. The isolated-agent null (p=0.410, p=0.100) is what converts "the
population became biased" into "the population became biased and no per-agent audit could have
detected it in advance."

The critical-mass result speaks to a different part of ARC-034's formalism. The claim asks for
characterisation of convergence to emergent state q given local rules theta, threshold
parameters, and feedback topology G. That the same local rules under different models yield
tipping points spanning a fivefold range is a concrete instance of q depending on parameters
that are not visible at the level of the individual agent.

## Limitations and caveats

The honest boundary is this: the emergent collective property here is a lexical convention and
its associated bias. ARC-034 is a claim about *ethical* properties. Moving from "collective
bias emerges without individual bias" to "collective ethical failure emerges without individual
ethical failure" is structural analogy, and analogy is not evidence -- nothing in this paper
rules out ethics being precisely the class of property that does compose from pairwise probes,
even though conventions do not. One would want to be careful here, because the analogy is
seductive enough to feel like a result.

Two further constraints. The setting is a coordination game with an explicit scalar payoff,
which is a very long way from the open-ended trajectory distributions ARC-034 wants sampled;
convergence is being driven by an incentive that has no counterpart in the ethical case. And
the agents are LLMs with a text memory window, so the coupling mechanism (accumulated
conversational history) is architecturally specific and does not obviously transfer to REE
agents.

## Confidence reasoning

Confidence 0.72, sitting slightly above the MAEBE entry for this claim despite lower mapping
fidelity, because the two entries fail in different places and this one fails in the better
place. Source quality is high (0.90): peer-reviewed in Science Advances, four models, 40
independent runs, scaling check to N=200, and -- decisively -- the isolated-agent control that
the argument actually requires. Mapping fidelity is capped at 0.70 and transfer risk set at
0.40 for the reason above: the demonstrated emergent property is not ethical. Taken together
with Erisken et al., ARC-034's negative half now has two independent lines of external support
in artificial multi-agent systems -- one on moral-benchmark reasoning with weak methodology,
one on convention formation with strong methodology. Neither touches ARC-034's positive test
programme (counterfactual probes, cascade mapping), and neither tests the favourable direction
that motivated the claim via MECH-127.
