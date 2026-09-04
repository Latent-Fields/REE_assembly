# Seehagen, Konrad, Herbert & Schneider (2015) -- "Timely sleep facilitates declarative memory consolidation in infants"

## What the paper did

This study is the first experimental (causal, not merely correlational) demonstration that offline consolidation is time-sensitive in human infants. The authors tested infants aged 6 and 12 months on a deferred imitation task: infants watched an experimenter model a novel action sequence on unfamiliar objects, and their retention of that sequence was tested after a delay. The key manipulation was whether infants napped within 4 hours of the learning episode, or remained awake through that window before napping (or not napping) later.

## Key findings relevant to MECH-533 / DEV-NEED-007

Infants who napped within the 4-hour window retained the modeled action sequence at both 4-hour and 24-hour delays. Infants who did not nap within that window failed to retain it, even though they eventually slept. A single nap of at least 30 minutes was sufficient to produce the retention benefit -- but only if it occurred within the timely window. This establishes that offline consolidation in infancy is not simply a function of total sleep obtained, but of WHEN that sleep occurs relative to the learning episode, and that this timing dependency can be demonstrated causally rather than merely inferred from correlational sleep-diary data.

## Translation to REE

MECH-533 proposes that offline processing frequency and offline processing COMPETENCE co-mature during development -- DEV-NEED-007 already names the frequency half of this claim ("frequent offline integration during early development"). Seehagen et al. strengthen the empirical basis for that frequency/timing claim specifically, by showing a genuine causal dependency: infant retention requires a TIMELY offline window, not merely an eventual one. This is directly relevant to any REE implementation of a developmental offline-window scheduler -- it constrains not just how OFTEN offline processing should occur during early development, but how quickly it must follow experience to be effective.

## Limitations and caveats

This paper evidences the frequency/timing half of MECH-533's joint claim; it does not itself measure or manipulate offline-processing COMPETENCE as an independent variable, so on its own it cannot establish the CROSSED relationship (frequency benefit conditional on competence level) that is MECH-533's distinguishing claim over a simple frequency-matters account. It should be read together with the competence-maturation evidence in the companion Pochinok (2024) and Noguchi (2023) entries in this same directory, which establish that the underlying replay-generating hardware and sequence-fidelity machinery are themselves still maturing over this same developmental window. The task itself -- deferred imitation of a modeled action sequence -- is also a simpler memory demand than REE's cross-episode, replay-dependent reorganisation architecture, so the transfer is not one-to-one.

## Confidence reasoning

High source quality: a landmark, causally-demonstrated finding in a top general-science venue (PNAS), described by the authors themselves as the first experimental causal demonstration of offline consolidation time-sensitivity in year-one infants. Mapping fidelity is moderate -- it strongly grounds the frequency/timing half of MECH-533's joint claim without directly testing the competence half or the crossed relationship between them.
