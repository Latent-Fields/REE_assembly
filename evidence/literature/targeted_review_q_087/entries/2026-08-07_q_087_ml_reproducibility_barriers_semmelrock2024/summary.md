# Reproducibility barriers in ML research (Semmelrock et al., 2024) -- Q-087

**Direction: mixed (confidence 0.50)** -- disconfirming for one candidate, cautionary for the machinery, indirectly supportive of the chosen answer.

## What the paper is

A recent multi-author survey (Semmelrock, Ross-Hellauer, Kopeinik, Theiler, Haberl, Thalmann, Kowald), accepted at AI Magazine and available as arXiv:2406.14325, that takes stock of reproducibility in machine-learning-based research: how reproducible ML work actually is, what the barriers are, and what drivers might improve it. Its verdict is bleak and blunt. Reproducibility experiments "have found worryingly low degrees of similarity with original results," and "lack of transparency, data or code, poor adherence to standards, and the sensitivity of ML training conditions mean that many papers are not even reproducible in principle." The authors add that "the general community continues to take this issue too lightly."

## Why it bears on Q-087, in two opposite directions

Q-087's three candidates for "what event counts as V3 closure" included a **green-board-plus-reproducibility-check** option: close only when the board is green *and* an independent reproduction succeeds. This survey is direct evidence against that candidate. If reproduction of ML results is frequently unattained -- sometimes impossible in principle -- then bolting a reproducibility check onto the closure gate risks reproducing (pun intended) the very failure mode that killed the strict-green-board option: a gate that *may never fire*, leaving GOV-V3FREEZE-1 permanently inert. So it **disconfirms candidate C**, and by elimination lends indirect support to the governance-acceptance answer Q-087 actually chose (the resolution note itself rejected green-board-plus-reproducibility partly because it "inherits that risk").

But the same finding is a **caution against the machinery that governance acceptance is meant to unblock**. GOV-V3FREEZE-1's PASS criterion requires that "an independent reader reproduces the flagship result from the frozen spec alone." Semmelrock et al. are telling us that this is exactly the thing ML research routinely fails to achieve. Choosing governance acceptance makes the *gate* fireable, but it does not make the *closure package* automatically reproducible -- and this paper warns that the reproducibility axis of that package is where such efforts most often break down. That is why I have marked the entry mixed rather than supporting: it helps the resolution and it flags a downstream feasibility risk in the same breath.

## The transfer caveat that cuts in REE's favour

One important limit. The survey is about *third-party* reproduction of *published* ML research -- strangers trying to rerun someone else's paper with partial information. REE's closure package is a team freezing and reproducing *its own* substrate, with full internal access to code, seeds, data, and the evidence index. Self-reproduction of a deliberately-frozen artefact is materially easier than external replication, so the paper almost certainly *overstates* the difficulty for REE's specific case. The "not even reproducible in principle" barriers (missing code, undocumented conditions) are largely the ones a disciplined freeze package is designed to eliminate. This is why transfer_risk is set at 0.55 and mapping_fidelity only 0.45 -- the evidence is real but points at an adjacent, harder problem than the one Q-087 faces.

## Confidence reasoning

Source quality is moderate-to-good (0.65): a recent, well-authored survey at a reputable venue, but a synthesis/opinion piece rather than a primary reproducibility study. Mapping fidelity is moderate-low (0.45) because it addresses a rejected candidate and the freeze package indirectly, not the event-definition question head-on. It is the pull's **required disconfirming/mixed source**, and it earns that role honestly: it undercuts a real candidate, cautions on the real machinery, and its own scope limit is disclosed rather than buried.
