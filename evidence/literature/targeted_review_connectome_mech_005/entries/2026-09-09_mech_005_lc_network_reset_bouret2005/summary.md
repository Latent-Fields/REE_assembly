# Network reset as the biological precedent for nu-gated interruptibility

Bouret and Sara set out to simplify a literature that had become baroque. By 2005 noradrenaline
had been assigned roles ranging from bare vigilance through prediction error to unexpected
uncertainty, and the authors' response was to look sideways -- at crustacea, where neuromodulators
do something conceptually blunt and mechanically clear: they interrupt an ongoing pattern of
network activity and let the elements reassemble into a different functional configuration. The
proposal for mammals follows the same shape. Phasic activation of locus coeruleus noradrenergic
neurons, occurring in time with cognitive shifts, interrupts target networks and permits their
rapid reorganisation. The supporting material is not a new experiment but a detailed reading of
extensive single-unit recordings from LC in behaving rats and monkeys, in tasks -- reversal,
extinction, set shift -- where the animal must abandon one way of proceeding and adopt another.

For MECH-005 the relevance is to the second pillar. The claim holds that nu determines whether a
gamma or beta-scale mismatch stays a local update or escalates into theta-scale path reevaluation:
high nu and small mismatches can force reorientation, low nu and local errors are absorbed while
the system stays the course. Bouret and Sara describe a neuromodulatory system that does
approximately this job in biology, and they describe it at the right level of abstraction -- not
as a signal that carries content, but as a signal that changes what the rest of the machinery is
permitted to do next. Two of MECH-005's architectural prohibitions get incidental support from the
same source. The paper is explicitly a rival to prediction-error and unexpected-uncertainty
accounts of NE, which is REE's position that nu does not encode prediction error; and it is
explicit that reset is not itself learning, which is REE's "this is not learning; it is allocation
of attention and urgency."

The caveats are real and I want them on the record rather than buried. First, network reset is a
claim about what happens downstream, in the target networks, after an LC pulse arrives. MECH-005's
nu is a weighting term inside the agent's own commitment machinery -- Authority(P_i) proportional
to A(P_i) times g(nu, context). Those are compatible pictures but they are not the same picture,
and nothing in the reviewed data establishes that the biological reset is graded in the way REE's
formalism needs. Much of the electrophysiology is as consistent with a fairly binary interrupt as
with a continuous authority dial. If the reset really is nonspecific, as the authors half-suggest
when they push the explanatory work onto the target networks, then nu is a trigger and not an
authority function, and REE's first pillar would need a different substrate.

Second, this is temporal-coincidence evidence, not causal manipulation. LC fires around the time
of behavioural shifts. That is compatible with LC enabling the shift, and equally compatible with
LC responding to a shift decided elsewhere. The reviewed corpus does not settle it, and the
distinction matters more for REE than it does for neuroscience, because a nu that merely reports
reorientation cannot be the control variable the architecture is built around.

I have set confidence at 0.75. Source quality is high -- this is a canonical review, still standard
reading two decades on, grounded in primary recordings rather than speculation. Mapping fidelity is
good on interruptibility and on the prohibitions, weaker on the graded-authority formalism.
Transfer risk is moderate and slightly unusual in shape: the rodent-and-monkey-to-REE step is the
familiar one, but there is a second transfer stacked underneath it, from the invertebrate model
that generated the theory in the first place. That is a longer inferential chain than the citation
count would suggest.
