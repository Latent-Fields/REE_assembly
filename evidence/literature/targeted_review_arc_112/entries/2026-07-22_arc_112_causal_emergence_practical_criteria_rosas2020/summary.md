# Reconciling emergences (Rosas et al., 2020) -- ARC-112, Q-081, INV-091

## What the paper did

Emergence has two literatures that do not talk to each other: one where a macroscopic variable is
said to have causal power over its own constituents, and one where the macro level is said to run
free of them. Rosas and colleagues show both fall out of a single decomposition. Using Integrated
Information Decomposition -- the extension of Partial Information Decomposition to a system's own
future -- they define a supervenient feature V of a multivariate system X as **causally emergent**
when it carries unique predictive information about the system's future that no individual
component carries; **downward causation** when that unique information is about future *micro*
variables; and **causal decoupling** when the macro variable predicts its own future without that
prediction being mediated by any micro variable. The last they call, memorably, a statistical
ghost.

The part that matters for us is what comes next. The full decomposition is combinatorially
intractable, so they derive three criteria that need nothing but standard pairwise mutual
information and scale linearly in system size:

- Psi(V) = I(V_t; V_t') - sum_j I(X_t^j; V_t')  -- emergence
- Delta(V) = max_j [ I(V_t; X_t'^j) - sum_i I(X_t^i; X_t'^j) ]  -- downward causation
- Gamma(V) = max_j I(V_t; X_t'^j)  -- with near-zero Gamma alongside positive Psi supporting decoupling

Proposition 1 states that Psi > 0 is sufficient for causal emergence and Delta > 0 sufficient for
downward causation. Code is released.

## Why this is the load-bearing entry of search 10

Search 10 was flagged as the one most likely to return philosophy that constrains nothing, and the
instruction was to bias toward literature yielding a computable quantity rather than a vocabulary.
This is the entry that clears that bar, and it clears it against ARC-112 specifically.

ARC-112 is a framing claim registered on an explicit condition -- that it earn its keep as the
parent node for Q-081, MECH-466 and INV-091, and not merely restate them. Its assertion is that
REE is a federation: one system, neither a monolith nor a collection of independent modules.
Stated that way it looks like a claim with no falsifier, which is why the claim's own notes call
it lower priority and warn against queuing an experiment against it directly.

This paper supplies the missing shape. Take the micro variables to be the per-stream signals the
Q-081 telemetry audit already enumerates -- E1 hidden state, E2 prediction error, E3 candidate
scores and commitment state, z_self, z_world, z_harm_s, z_harm_a, z_goal, beta, operating_mode.
Then "REE is one system rather than a collection of modules" becomes: there exists a system-level
descriptor V over those streams with Psi(V) > 0, i.e. carrying predictive information about the
federation's future that no single stream has. That is computable from exactly the per-step
recording the cluster already needs for Q-081, using an estimator that is linear rather than
exponential in the number of streams. Delta maps onto the federation's downward arm -- a positive
Delta for a control-plane V against future per-stream variables is the computable form of "shared
organisational constraints coordinate the streams", which is the second half of ARC-112's
sentence.

There is a bonus for INV-091 that I did not expect. Gamma near zero with Psi positive is causal
decoupling: a macro variable that has floated free of its constituents. If INV-091's band has a
collapse end -- too much shared organisation -- then decoupling is a candidate formal signature of
it, and one arrives at that reading from the estimator rather than from the metaphor. I would not
push this hard; it is a hypothesis about which corner of the (Psi, Gamma) plane corresponds to
which end of the band, and nothing in the paper says so.

## The reason this is scored `mixed` and not `supports`

The criteria are one-sided, and the authors say so without hedging: they are sufficient but not
necessary, and "these criteria are unable to rule out emergence". A REE run that computes Psi over
every candidate macro feature and finds all of them non-positive has established nothing at all
about ARC-112. It cannot be written up as evidence against the federation framing. Given how
tempting a clean negative would be in a cluster with exp_conf 0.0 on all four claims, that
asymmetry needs to be in the record before the run rather than discovered in the write-up.

Worse, the direction of the bias is the wrong one for REE. The authors note the criteria
double-count redundancy, so that "if there is redundancy in the system it will be harder to detect
emergence". REE's streams share environmental input and are directly wired to one another -- E2
consumes E1's output, the beta gate reads across, the control plane conditions several at once.
That is a high-redundancy regime by construction, which is precisely where this estimator loses
sensitivity. False negatives are the *expected* failure mode here, not a remote one.

Two further constraints. The user must supply V; there is a feature-agnostic test of emergence
*capacity* (Theorem 1, Syn(X_t; X_t') > 0) but that is the intractable quantity, not the cheap
one. So the analyst chooses the very object the claim is about, and a badly chosen V produces a
null indistinguishable from a true one. And emergence is defined only with respect to a chosen
microscopic partition, for which the paper offers no principled selection method -- in REE,
whether the partition is per-stream, per-latent-block or per-module is a design decision that can
manufacture the result.

## Confidence reasoning

0.68. The source is strong (PLOS Computational Biology, released code, an estimator family since
used at scale) and the transfer risk is the lowest in this pull, because there is no domain
transfer to make: the theory is stated over arbitrary multivariate stochastic processes, which is
exactly the substrate-independence search 10 was hunting for. GOV-ANALOGY-1 is not engaged on the
substrate axis -- this is not a brain result being read across.

What holds it below 0.8 is that the tool can only do half the job ARC-112 needs. It offers a
positive test and forbids a negative one, in a system whose structure biases it toward negatives.
That is still a large improvement on a framing claim with no falsifier at all, and it is the
concrete reason to think ARC-112 can earn its keep. But the honest statement is that this paper
tells us how ARC-112 could be *established*, not how it could be *tested*.

Note also that lit_conf is what is being reported here. exp_conf for ARC-112, Q-081, MECH-466 and
INV-091 remains 0.0 -- nothing in this cluster has been run.
