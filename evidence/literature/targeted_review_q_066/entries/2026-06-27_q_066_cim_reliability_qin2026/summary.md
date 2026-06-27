# When small variations become big failures: reliability in compute-in-memory accelerators (Qin, Zheng, Yan, Wen, Hu & Shi, 2026)

**Claim under test:** Q-066 — can a candidate physical substrate furnish *auditability* and *hard safety gates*? This entry is the closest in the pull to REE's actual concern, on the **auditability / hard-gate** axis.

## Framing

POST-V5 derivation; no physical REE substrate exists. This is an arXiv preprint (submitted 3 March 2026), not yet peer-reviewed, so its source_quality is discounted relative to the three Nature/AIP reviews in this pull — but it is the most on-point source, from an established compute-in-memory reliability group.

## What the paper covers and the key finding

The paper analyses how minor device variation and drift in compute-in-memory (CIM) neural accelerators *amplify through matrix operations into catastrophic accuracy collapse*, specifically in safety-critical inference (autonomous systems, medical). Variation tolerances that look minor in conventional digital circuits "become catastrophic" via error accumulation across the analog multiply-accumulate operations fundamental to neural compute. The authors are explicit that hard correctness guarantees cannot presently be assumed under variation conditions, and that existing write-verify protocols require enhancement to provide deterministic safety guarantees. Their proposed remedy — SWIM, a selective verification mechanism, plus training with right-censored Gaussian noise — is a statistical robustness improvement, *not* a hard guarantee.

## Mapping to REE

This is the paper that maps most directly onto Q-066's framing, because it asks the same shape of question REE asks: can an analog substrate provide a *deterministic safety boundary*? Its answer for current analog/in-memory hardware is no — externally-inspectable hard gating is an open problem, not a solved capability. That weakens Q-066's auditability/hard-gate clause more pointedly than any other source in the pull.

## Caveats and confidence

The mapping_caveat is that "safety-critical inference accuracy collapse in a CIM DNN accelerator" is structurally analogous to, but not identical with, REE's simulated-vs-released action gate. The paper shows the *class* of guarantee REE needs is currently unmet in this substrate class; it does not (and cannot) show that REE's specific gate fails, because no physical REE substrate exists to test. This is why its mapping_fidelity (0.35) is nonetheless the highest of the Q-066 set — the framing aligns unusually well — while transfer_risk stays high at 0.85. Logged **weakens**, source_quality 0.65 (preprint), confidence 0.4.

A literature gap worth recording: none of the four Q-066 device-physics reviews addresses **offline reintegration** (one of the ARC-089 primitives) — it is a system/architecture-level operation with no device-physics analog surfaced in this pull.
