# The deformation has an address

The weakest point in any "history shapes the geometry" claim is not whether history leaves a trace —
that is easy to show — but whether the trace is *shaped*. A global increase in caution after a bad
experience would satisfy a naive reading of MECH-023 while being nothing like what the claim actually
asserts. This is why MECH-023's CONFIRMING criterion (ii) is written as it is: the divergence must be
concentrated on candidates whose rollouts enter the harm region R, and an equal-mass harm inflicted in
a distant region R′ must produce divergence localised to R′ instead. Without that control, "path-dependent
geometry" reduces to "global cost shift", which is the claim's own stated falsifier.

Mamad and colleagues supply the biological half of that requirement. Recording CA1 place cells in rats
exposed to the innately aversive fox odour TMT in specific maze arms, they found that cells whose fields
lay *outside* the TMT arms nonetheless fired in those arms during the aversive episode — extrafield
spiking — and subsequently shifted their place field centre of mass toward the threat locations.
Optogenetic activation of the basolateral amygdala both triggered the extrafield spiking and predicted
how much the field would move. Their conclusion is the sentence that matters here: aversive remapping
depends on the perceived location of the threat rather than occurring randomly. The deformation has an
address, and an identified pathway delivers it.

There is a sign inversion worth flagging rather than glossing. The fields move *toward* the threat: the
map allocates more representational resolution to the dangerous region, not less. REE's residue field,
as it currently sits in `compute_residue_cost`, raises the cost of candidates entering R and thereby
suppresses them — a policy-level avoidance implemented on a representation that, in the rat, is getting
*sharper* over exactly that region. These are not straightforwardly contradictory; representing a hazard
more finely and choosing to route around it are compatible, and arguably the former is what makes the
latter possible. But if the V3 run finds residue producing avoidance with no accompanying increase in
resolution over R, that is a genuine dissociation from the biology and should be recorded as such
rather than folded into a confirmation.

The paper's real limit for our purposes is that it does not run the B′ control. Locality is established
against the non-threatened arms of a single maze, which tells us the effect is not uniform, but it does
not distinguish a region-shaped geometry from a global cost that simply decays with distance from the
event. That discrimination is precisely what MECH-023's design carries as its own load-bearing control,
and this literature cannot lift it for us — it can only establish that the phenomenon is not
a priori implausible.

And the deeper caveat: TMT is an innate threat, sniffed rather than caused. There is no action, no
self-attribution, no commitment. Whatever this paper evidences, it is *harm history*, not
*responsibility*. The clause in MECH-023 that does the ethical work — that the agent's own committed
action is what shapes the terrain — requires the ARC-015/MECH-095 self-versus-world routing sitting
upstream of accumulation, and nothing in this preparation touches it.

Confidence 0.7. eNeuro, modest sample, a single-cell centre-of-mass statistic, and an optogenetic arm
that identifies a driver rather than a consequence. Included because the locality result is scarce in
this literature and speaks to the criterion REE is least able to import from anywhere else.
