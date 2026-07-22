# A partially nested cortical hierarchy of neural states (Geerligs et al., 2022) -- MECH-466, INV-091

## What the paper did

265 participants watched an eight-minute film in the scanner. The authors applied a greedy
state-boundary search to searchlights across the whole cortex, identifying for each searchlight
the timepoints at which the activity pattern shifted from one temporarily stable configuration to
another, and optimising a metric that maximises within-state similarity against between-state
similarity. They then asked how those boundaries relate across regions.

The timescale hierarchy came out as expected: state durations ran from about 4.5 seconds in
primary sensory cortex to about 27.2 seconds in prefrontal regions, and this regional profile
replicated across independent participant groups at r = 0.85. The interesting result is the
sharing. 85% of all pairs of searchlights showed boundary overlap significantly above chance --
strongly within functional networks (auditory, default-mode subnetworks, motor, attention), and
substantially across them too, particularly among higher-order networks. Neural state boundaries
overlapped with human-annotated event boundaries at every level of the hierarchy, most strongly
in anterior cingulate, dorsomedial prefrontal cortex and anterior insula.

And the hierarchy is only partially nested. The authors are explicit that relative boundary
overlap between regions fell short of its theoretical maximum of 1.0: regions at different
timescales genuinely disagree about where boundaries fall.

## Key findings relevant to MECH-466 and INV-091

MECH-466 proposes that event boundaries and commitment landmarks are REE's effective shared
temporal grammar. That claim has a premise underneath it -- that boundaries *can* function as
common landmarks across processes running at very different characteristic rates -- and this is
the best external test of the premise I found.

What makes it useful is that the answer is the middle one. Total sharing would be uninteresting
(it would mean the hierarchy is one clock). No sharing would refute the premise. What is reported
is substantial-but-imperfect sharing across a roughly sixfold spread of timescales, which is
comparable to REE's 1:10 E1:E3 ratio. That is precisely the combination MECH-466 and INV-091
jointly predict: shared enough to coordinate, differentiated enough not to have collapsed. INV-091
asserts a viable band between fragmentation and collapse; this is what a system sitting inside
such a band looks like when measured.

Two methodological decisions transfer directly to REE's prospective run. Boundary sharing has to
be quantified pairwise against a chance-overlap baseline computed from the boundary *counts* --
fast streams have more boundaries and therefore overlap more by accident, and without that
correction REE's E1 stream would look spuriously well-coordinated with everything. And "do the
streams share boundaries" has to be asked as a graded question. The authors' relative-overlap
metric, scaled against the maximum possible given the counts, is a usable template.

## How this translates to REE

With three specific breaks, and the first is the one that matters most.

The direction of causation is reversed. Here boundaries are *detected* by the analyst from the
neural signal; nothing in the brain broadcasts a boundary flag. In REE the two-scale segmenter
*broadcasts* boundaries to consumers. So shared boundaries in REE could be nothing more than a
consequence of the broadcast wiring -- Q-081's Outcome B, where streams are coordinated only by
explicitly wired gates. This study never faces that hazard and offers no advice about it. For
REE it means the boundary-sharing measurement is not by itself informative, and the ablation
(remove the broadcast, re-measure) is where the content is.

Second, every region here is driven by one shared external stimulus. Above-chance boundary
overlap always has a common-input explanation available. REE's analogue is shared environmental
input, and the surrogate has to control for it or the same ambiguity recurs.

Third -- and this is why the entry is scored where it is -- the study never compares event-locked
against clock-locked alignment. That comparison *is* MECH-466's falsifier. So the paper supports
the claim's premise and leaves the claim itself untested.

## Limitations and caveats

The authors are candid that it is "not yet clear what a distinct neural state might represent" in
transmodal regions. The states are statistically robust and semantically opaque, and the same
will be true of any HMM-like states inferred over REE's latents. Recurrence of states is not by
itself evidence that anything functional is shared -- a caution that applies with equal force to
Q-081's recurrent-state analysis.

One 8-minute film, one stimulus type; generalisation is untested. Naturalistic designs trade
control for ecological validity, and the authors note eye movements and preparatory activity as
possible confounds. The improved GSBS algorithm is their own, which is normal but means the
boundary definition and the finding come from the same lab.

GOV-ANALOGY-1: analogy, not evidence. That human cortex shares state boundaries across its
timescale hierarchy tells us the phenomenon is possible in at least one system. It tells us
nothing about REE.

## Confidence

0.58. Source quality 0.85 -- eLife with published peer reviews, n=265, strong internal
replication, and chance baselines computed rather than assumed. Mapping fidelity 0.60: the
phenomenon maps onto MECH-466's premise, but analyst-detected boundaries versus system-broadcast
boundaries is a real structural difference, not a quibble. Transfer risk 0.50: naturalistic fMRI
to an artificial agent, with a common-stimulus confound that has no clean REE counterpart.

Literature confidence 0.58; experimental confidence for MECH-466 and INV-091 remains 0.0. The
premise has external support. The claim does not.
