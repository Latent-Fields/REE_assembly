# Bonsai trees in your head (Huys et al., 2012)

## What the paper did

Huys and colleagues gave healthy adults a sequential decision task -- a tree of states in
which each move carried a gain or a loss, and the best total return sometimes required
passing *through* a large loss to reach a larger downstream gain. They then fit a family of
lookahead models to the choices, differing in how deep into the tree the subject evaluated
and under what conditions evaluation stopped. The winning model was not "evaluate to depth
N". It was: evaluate forward until you hit a large loss, then stop and discard that branch.
The authors call this Pavlovian pruning, because the truncation is triggered reflexively by
an aversive outcome rather than chosen deliberatively, and because subjects kept doing it
in exactly the trials where doing it cost them money.

## What is relevant to MECH-080

MECH-080 asserts that rollout truncation set-points are the substrate of psychiatric
individual differences. That assertion has two separable parts, and this paper speaks
clearly to the first one only. The first part is that forward-search depth is a real,
separable, individually-varying parameter rather than an architectural constant -- and that
variation in it is psychiatrically meaningful. Huys et al. establish precisely that: the
pruning parameter was identifiable per subject, it varied substantially across subjects, and
its strength correlated with sub-clinical mood disturbance. If search depth were a fixed
property of the planner, MECH-080 would have nothing to be about. This paper is the reason
it does have something to be about.

The second part -- that the specific parameter is a *horizon* and that its settings map onto
ADHD, anxiety and OCD respectively -- gets no support here, and I want to be careful not to
let the first part launder the second.

## How it translates, and where the translation breaks

The break is sharper than it first looks. REE's `config.e2.rollout_horizon` is an
unconditional cap: every rollout runs to depth h and stops, regardless of what it encounters.
Huys' pruning is conditional: the rollout runs until it meets a large loss and stops *there*.
These produce different signatures under the same manipulation. Shortening an unconditional
horizon degrades planning uniformly; strengthening conditional pruning degrades planning
*asymmetrically*, only on paths that cross aversive states, and leaves appetitive planning
intact. A REE experiment that shortens `rollout_horizon` is therefore not running the
manipulation this paper models, and a result from one does not transfer to the other. That
matters for MECH-080's design, because the claim's own manipulation spec names the horizon
knob, not a loss-triggered pruning knob -- and REE has no loss-triggered pruning knob.

The second caveat is the sample. Sub-clinical mood disturbance in healthy adults is not
ADHD, is not anxiety, and is not OCD. The paper is suggestive that affective state sets
search depth; it is silent on whether three *different* disorders correspond to three
*different* settings of one parameter, which is the actual content of MECH-080.

## Confidence

I have put this at 0.68 and classed it `supports`, which may look generous for a paper that
does not measure any of the three disorders. The reasoning is that it supports the claim's
*enabling premise* strongly and its *specific content* not at all, and that the enabling
premise was genuinely open -- one could coherently have held that planning depth is set by
compute budget and is not an individual-difference dimension at all. That possibility is now
closed. Source quality is high. Mapping fidelity at 0.60 is doing the real work of the
discount, and it is the number a future governance pass should look at rather than the
headline direction.
