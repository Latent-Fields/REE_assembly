# Jin, Tecuapetla & Costa 2014 -- parsing and concatenation are distinct basal ganglia operations

Jin and colleagues trained mice on rapid lever-press sequences and recorded from basal ganglia
circuits while the animals performed them. They found neurons whose activity encoded an entire
sequence as though it were a single action. More usefully for us, they found that two different
things were happening in two different populations: some neurons carried start/stop activity that
delimited the sequence -- signalling where one unit ended and the next began, which the authors
call parsing -- while others showed sustained or inhibited activity spanning the whole sequence,
and that sustained activity covaried with the rate at which individual elements were executed,
which is the signature of concatenation. Direct and indirect pathways were concomitantly active at
sequence initiation but diverged during performance.

The reason this matters for ARC-069 is narrower than "chunking is real in the brain", which we
already assumed. ARC-069 carries a specific note, taken from the original observation, that
decomposition and composition *feel* like inverse operations and are computationally treated as one
machinery under the options framework, but that their triggers are asymmetric -- and that we should
therefore register two slots rather than one. That is an architectural bet, and it is the kind of
bet that is cheap to make and expensive to be wrong about. Jin et al. supply the first direct
neural evidence I have found that the bet is the right way round: parsing and concatenation are not
one operation observed from two sides, they have separable signatures in the same substrate. The
claim's asymmetry note survives contact with the electrophysiology.

What the paper does not do is the thing I would most like it to do. These are over-trained
sequences being executed, and what is being read out is neural activity during execution. ARC-069
is a claim about the grain of proposals emitted into hippocampal rollout and apprehended by the
rule layer (ARC-062) -- the simulation side, not the execution side. It is entirely possible for a
motor system to represent a practised sequence as a unit while the planning system that generated
it never operates on anything but single actions. Nothing here distinguishes those. Nor does the
paper show a formed chunk being broken back down, which is ARC-070's whole direction: this is
evidence about how chunks are held and delimited, not about regranularisation under prediction
failure. The task is also two presses deep, which is the shallowest hierarchy that can still be
called one, so it cannot discriminate "the system has an optional coarser grain" from "the system
rescales grain continuously" -- and only the second is ARC-069.

I have put confidence at 0.72. Source quality is high and I have little doubt about the result
itself; this is a well-replicated lineage and Nature Neuroscience with in-vivo recording in behaving
animals. The discount is almost entirely mapping: 0.70 fidelity because the execution/simulation
distinction is a real gap rather than a pedantic one, and 0.35 transfer risk because the bridge from
rodent operant chunking to an artificial planning agent is long. Read this entry as strong support
for ARC-069's *asymmetry* commitment and only weak support for its *rollout-side* commitment.
