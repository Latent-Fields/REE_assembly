# Navigation machinery is domain-general -- the premise ARC-031 stands on

**Constantinescu, O'Reilly & Behrens (2016), _Science_ 352(6292):1464-1468.**
Claim assessed: **ARC-031** -- HippocampalModule navigates z_self trajectory space in addition to
z_world action-object space O.

## What the paper did

Subjects learned a two-dimensional conceptual space -- bird silhouettes varying continuously in neck
length and leg length -- and then "moved" through it while being scanned. The analysis looked for the
hexagonally symmetric modulation that is the established fMRI population signature of grid-cell
coding, and found it, in a network markedly overlapping the one active during physical spatial
navigation. The signal held up across sessions acquired more than a week apart.

There is no physical space anywhere in this task. The code appeared anyway.

## Why it matters for ARC-031

ARC-031 makes an architectural move rather than a mechanistic one: it proposes pointing REE's
*existing* hippocampal navigator at a second domain, rather than building a separate deliberation
planner. That move is only coherent if navigation algorithms are genuinely domain-general -- if the
hippocampal-entorhinal system implements "how to get around a continuous space" rather than "how to
get around *the world*."

This is the primary empirical result establishing that they are. The claim's own registration notes
cite Behrens et al. 2018 for the same point; this is the evidence that review is built on, which is
why I have flagged in `failure_signatures` that governance should not count the two as independent
support. It is one line, now recorded at its source.

## What it does not establish, which is most of ARC-031

Two gaps, and I do not think either can be argued away.

**The domain is wrong in an interesting way.** A bird morphospace is exteroceptive: presented,
trainable, with feedback, and smooth by construction. z_self as ARC-031 defines it -- D_eff,
hypothesis-tag integrity, self-coherence cost -- is internal, and there is no guarantee it has the
metric structure a grid code requires. This is not a quibble I am importing; ARC-031's own notes
make MECH-113's D_eff monitoring a *prerequisite* for exactly this reason, observing that a
dispersed self-model means no reliable position in z_self space and navigation degenerating. The
claim already knows its space might not be navigable. This paper studies a space engineered to be.

**The object is wrong.** This is position coding. ARC-031 is about *trajectories* -- planned
sequences of self-state transitions constituting deliberation, evaluated by self-coherence and
self-maintenance cost. Showing that a space is metrically organised is a precondition for planning
routes through it, not evidence that routes are planned. The Schuck & Niv entry in this same pull
addresses the sequence half; neither paper addresses both at once for the same space.

## Confidence

0.55, the highest in this pull, and I think justified: the premise ARC-031 needs really is
established, by a good paper, robustly. But the standing caveat applies to every entry here --
ARC-031 is phase-locked to v4 with zero distinguishing substrate in ree-v3, and HippocampalModule
today takes z_self only as a conditioning input alongside z_world, not as a navigated space. No
literature can move that. What this evidence does is make the eventual build a reasonable thing to
attempt rather than a speculative one.
