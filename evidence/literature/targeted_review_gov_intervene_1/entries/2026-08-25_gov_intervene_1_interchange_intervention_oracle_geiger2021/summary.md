# Causal Abstractions of Neural Networks (Geiger, Lu, Icard & Potts, NeurIPS 2021)

Where the companion entry in this directory (Vig et al., 2020) is a clean instance of
GOV-INTERVENE-1's non-oracle, silky quadrant, this paper is close to a textbook instance of
the opposite corner: the ORACLE intervention. The authors hand-specify an interpretable causal
model of a task (a tree-structured natural-logic parse of a natural-language-inference corpus)
and align hypothesised variables in that causal model with specific neural representations
inside a trained network. They then run "interchange interventions": take the value a
representation would hold on a *different* input the causal model says should produce a
particular counterfactual, and force the network's representation to that value, checking
whether the resulting output matches what the causal model predicts. That is privileged,
target-correct information being imported into the system under test -- the intervention does
not perturb the network's own dynamics to see what happens, it injects the answer the causal
model says should be there and checks whether the network's downstream behaviour tracks it.
GOV-INTERVENE-1 describes exactly this role for an oracle intervention: establishing an
achievable ceiling and downstream usability, as a positive control, rather than establishing
that the network ordinarily produces that structure on its own.

What makes this paper unusually strong support, rather than a loose analogy, is that the
authors state the oracle/endogenous distinction themselves, in almost GOV-INTERVENE-1's own
terms: a successful interchange intervention verifies that a representation *can be made to
behave like* a causal variable under intervention, which is a claim about alignment under
forced conditions, not a claim that the network exercises that causal structure unprompted
during ordinary forward passes. Their own empirical result reinforces why this distinction is
not academic -- a simpler baseline model fails the interchange-intervention test outright,
while a stronger BERT-based model succeeds on parts of the causal structure, showing that
oracle verification is a real, falsifiable test rather than a rubber stamp that any sufficiently
large network passes automatically. That is direct precedent for GOV-INTERVENE-1's warning
that an oracle result must never be silently treated as endogenous competence: here, the
authors demonstrate the oracle test can and does fail, which is what makes a pass informative
rather than vacuous.

The mapping has a specific limit worth stating rather than glossing over: the causal model
this paper intervenes from is hand-specified in advance from known, formal task structure (a
synthetic corpus built directly from a natural-logic grammar), which is a considerably
stronger and more literal oracle condition than most REE diagnostic interventions would have
available -- REE mechanisms rarely have an equally crisp, independently verifiable ground-truth
causal model to draw the "correct" counterfactual value from. The analysis is also
static-inference-time on a frozen, trained network, so it says nothing about how an oracle
intervention interacts with an online, continually-learning, recurrent agent's commitment
boundaries the way REE's own diagnostics must. Confidence is set at 0.7, the higher of the four
entries in this pull, because the oracle/ceiling-versus-endogenous distinction is stated
almost verbatim in the paper's own methodology rather than requiring interpretive stretching to
map onto GOV-INTERVENE-1.
