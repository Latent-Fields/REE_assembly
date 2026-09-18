# Baboyan et al. (2021) -- Isolating the white matter circuitry of the dorsal language stream

**Claim tested:** MECH-038 (arcuate-like sequence-to-motor channel nudges language emergence)
**Direction:** mixed | **Confidence:** 0.66

## What the paper did

Seventy-one people with chronic stroke-induced aphasia were analysed with connectome-based lesion-symptom mapping:
rather than asking which *voxels* predict a repetition deficit, the authors estimated lesion damage at the level of
individual structural *connections* and fitted a sparse partial least squares model, training on fifty subjects and
evaluating on twenty-one held out.

Ten short- and long-range parietotemporal connections came out. The strongest single predictor was a short-range
supramarginal gyrus connection approximating area Spt -- the auditory-motor interface region Hickok's group has argued
for over many years -- together with long-range pathways from posterior supramarginal and superior temporal cortex to
ventral and dorsal premotor cortex. Their conclusion is blunt: repetition impairment is a parietotemporal
disconnection syndrome impacting Spt and its frontal circuits, "as opposed to being purely a disconnection of the
arcuate fasciculus."

## How this bears on MECH-038

This is the entry in the directory that argues, and what it argues against is the anatomy, not the function. It is
worth noticing that MECH-038's own architecture doc anticipated it: the doc states that the arcuate fasciculus is
treated as a *functional analog, not an anatomical requirement*, and that language relies on distributed dorsal and
ventral streams rather than a single tract. Baboyan et al. is the strongest current evidence that this hedge was
necessary rather than merely modest.

Read as a claim about function, the paper confirms MECH-038 and sharpens it. There is a dorsal route that carries
sequence form from sensory representation to motor output, its hub is an auditory-motor interface with its own
representational state, and it projects to premotor cortex. That is a considerably more useful specification of what
the REE channel should connect than "Broca to Wernicke" ever was, and it is the same shape MECH-038's build note
already describes when it names the multi-content theta packet as the source and E2 signalling affordances as the
destination.

Read as a claim about anatomy, it is a warning about implementation. A REE build that routes E1 sequence summaries into
E2 affordances over a single dedicated fast wire would be instantiating exactly the picture this paper rejects. The
human system's fast route is a distributed set of connections hubbed on an interface *area*, not a tract. If the REE
analog is built as one wire and the ON/LESION contrast comes out null, the null would be ambiguous between "the nudge
is empty" -- MECH-038's falsifying outcome -- and "the channel was built at the wrong grain," which is not an answer to
anything. Building the routing through an interface stage with its own state forecloses that ambiguity.

## Limitations and where the mapping strains

The target is speech repetition in chronic stroke aphasia: an already-acquired system, a copying task, and a human
articulatory apparatus with nothing corresponding to it in ree_core. So this entry's value is architectural rather than
evidential. It constrains how the ON arm should be built; it does not bear on whether that routing nudges emergence,
which is what MECH-038 actually asserts. I have scored it *mixed* because it splits along the function-versus-anatomy
seam, not because it splits along the claim's confirming-versus-falsifying seam -- anyone reading the direction field
alone should know that.

Methodologically it is the most careful lesion study in this directory, and I still would not lean hard on it. Sparse
PLS selecting ten connections from a whole connectome on fifty training subjects is a thin basis, connection-level
lesion load co-varies strongly between neighbouring parietotemporal connections, and the abstract gives no held-out
prediction accuracy for the twenty-one test subjects -- which is awkward, since generalisation to held-out data is the
main advantage the design claims over conventional voxel-based mapping.

## Confidence reasoning

Source quality 0.75, discounted from higher for the unreported test-set accuracy and the thin training set. Mapping
fidelity 0.60: it constrains the build rather than testing the claim. Transfer risk 0.40. Aggregate 0.66.
