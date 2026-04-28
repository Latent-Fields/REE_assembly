# Castro, Terry, Berridge (2016) -- Orexin in NAc shell amplifies wanting and liking

## What the paper does

The Berridge group ran a careful microinjection experiment in adult rats targeting
sub-regions of the nucleus accumbens (NAc) medial shell -- the rostral hedonic hotspot
versus the caudal shell -- with orexin-A and with scopolamine (a muscarinic acetylcholine
antagonist). They used the established taste-reactivity protocol (orofacial reactions to
sucrose are read as 'liking', orofacial aversive reactions to quinine as 'disgust', and
intake of palatable chocolates as 'wanting'). The headline finding is a dissociation:
orexin-A in the rostral hotspot amplifies 'liking' (hedonic orofacial reactions to
sucrose), while orexin-A at *all* NAc shell sites amplifies 'wanting' (palatable intake).
Scopolamine in the caudal shell did the opposite -- it shifted sucrose 'liking' toward
'disgust' and 'fear', including a characteristic defensive treading toward chamber walls.

## Findings relevant to SD-037

SD-037's central architectural commitment includes a drive->goal seeding bridge: when
the override_signal is above threshold, drive_level is permitted to seed z_goal directly,
and below threshold this bridge is closed. The biology underlying this bridge needs to be
something more concrete than "orexin matters for motivation" -- it needs to be a causal
demonstration that orexin tone at a downstream consumer node is sufficient to amplify
motivated approach. Castro et al. provide that demonstration. Microinjection of orexin-A
into NAc shell -- which is one of the strongest downstream targets of LH orexin
projections -- causally increases 'wanting' for palatable food at every site they tested,
and additionally enhances hedonic 'liking' at the rostral hotspot. This is the cleanest
direct test I am aware of in the literature that orexin tone is permissive for the
drive-driven goal-seeking pathway, which is exactly what SD-037 commits the override_signal
to gate.

## REE translation and mapping caveats

There are two important caveats that hold the confidence below 0.85.

First, the paper does not test the harm-reweighting axis of SD-037. The override_signal
in SD-037 has two consumer sites: the SD-012 drive->z_goal bridge (which Castro et al.
license) AND the reweighting of z_harm at downstream commit gates. The experiment uses
appetitive sucrose with no concurrent threat manipulation, so we cannot read the harm
reweighting from this data. The PAG/freeze-gate experiments (MECH-279/MECH-280) and
LH->PAG projection literature handle the harm-reweighting axis separately.

Second, microinjection is supraphysiological tone delivery, not endogenous override
recruitment under sustained drive+threat as in the SD-037 falsifiable. The experiment
tells us *what would happen if endogenous orexin tone at NAc shell were elevated*, not
*whether the LH orexin system actually does this in response to integrated drive+threat
context*. The latter is a stronger causal chain that would need optogenetic activation of
LH orexin neurons under specific drive+threat conditions, not microinjection.

A third, smaller observation: the rostral/caudal dissociation in Castro's data implies
that the override effect on downstream consumers is not spatially uniform. SD-037
currently treats override_signal as a unitary scalar; biology supports something more
like a low-dimensional vector with hotspot/coldspot specificity. This is the same
caveat that arises from OX1R/OX2R receptor biology in Jacobson 2022.

## Confidence reasoning

I am setting confidence to 0.78. The source quality is high (Neuropsychopharmacology,
Berridge lab, established methodology). Mapping fidelity is moderate-to-high: the paper
directly tests a causal chain from orexin tone at a downstream consumer to enhanced
motivated approach, which is one of the two axes SD-037 commits to. It does not test the
other axis (harm reweighting at commit gates). Transfer risk is moderate -- rat NAc shell
generalises reasonably to the REE drive-seeding architecture, but the supraphysiological
microinjection design weakens the inference about endogenous integrator-output coupling.

The honest reading: Castro et al. license the drive-gating half of SD-037. The harm-
reweighting half still rests on the Johnson 2012 panic/PAG literature and the V3-EXQ-483
substrate-side wiring confirmation. The combined picture from the lit-pull is that SD-037
has solid biological cover on its two functional axes, but the cover is split across
papers rather than concentrated in any single experiment.
