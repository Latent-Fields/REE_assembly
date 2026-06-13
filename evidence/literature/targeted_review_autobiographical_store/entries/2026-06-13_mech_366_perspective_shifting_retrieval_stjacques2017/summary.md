# Shifting visual perspective during retrieval shapes autobiographical memories (St. Jacques, Szpunar & Schacter, 2017)

**Claim grounded:** MECH-366 (switchable episodic perspective tag) — specifically the *switchability* half that the Nigro & Neisser (1983) entry in this same review established was missing.

## What the paper did

St. Jacques and colleagues took the field/observer distinction out of the questionnaire and into a controlled encode-then-retrieve fMRI paradigm. Participants encoded autobiographical-style events and were later cued to recall each one from either the perspective it was naturally experienced in (typically first-person, own-eyes) or from the *alternative* perspective. The decisive move is that perspective is treated as an experimentally manipulable variable at **retrieval**, not as a fixed property read off the encoded trace. They then asked what happens to the memory when you make that switch, and which brain regions track it.

## Key findings relevant to the claim

Two results carry the weight. First, people *can* re-adopt a novel visual perspective on a specific, already-encoded event — the switch is available on demand. That alone is the part MECH-366 most needed and that the Nigro entry flagged as untested: viewpoint is not locked to the encoding camera. Second, exercising the switch is not phenomenologically inert. Shifting perspective changed the emotional intensity and vividness of the memory, and the magnitude of that change was predicted by recruitment of the precuneus — a region already tied to visuospatial perspective-taking and self-referential memory. So the viewpoint label is both re-settable and consequential: re-reading the episode from the other vantage reshapes it.

## How it translates to REE

This is the biological warrant for the load-bearing clause in MECH-366 — that the participant/observer viewpoint label is *switchable at retrieval, independent of the viewpoint at encoding*. Nigro & Neisser gave REE the construct (the tag exists, and it is the field/observer construct we name); St. Jacques et al. give REE the dynamics (the tag can be re-set on a given event token). Together they cover both halves of the claim, which is why this entry moves the strand off the lone MIXED 0.55 it sat at.

There is an honest architectural wrinkle worth carrying forward, captured in the entry's failure signature. In the brain, switching perspective *writes back* — it modifies the trace rather than just re-rendering it. MECH-366's tidy picture (one immutable event token, a viewpoint label read at retrieval) is therefore an idealisation. A faithful V4 implementation has to decide whether a viewpoint-switch is a pure read over the ARC-085 token or an operation that legitimately updates the episode (and if it updates, MECH-365's provenance gate has to police that the update is tagged as a re-construction, not a fresh perceptual fact). That is a design question this paper raises rather than settles.

## Confidence reasoning

I put this at 0.78, the strongest entry on the strand. Source quality is high (NeuroImage; combined behavioural and fMRI with a converging neural correlate), and mapping fidelity is high because the study tests precisely the switchability the claim asserts rather than an adjacent construct. I held it below ~0.85 for two reasons: the switch is demonstrated under instruction in a lab paradigm (so "voluntary on demand" is shown, but spontaneous switching is inferred), and the reshaping side-effect means the cleanest version of MECH-366 — switchable *and* inert — is not quite what biology delivers. The transfer risk is the usual one: a human cognitive-neuroscience result is being mapped onto a represented tag in an artificial architecture. exp_conf is unchanged at 0 — this raises literature confidence only and promotes nothing.
