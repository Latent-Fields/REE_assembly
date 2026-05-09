# Walker & Stickgold 2006 — Sleep, memory, and plasticity

**Source:** Walker MP, Stickgold R. *Annual Review of Psychology* 57:139-166 (2006). [DOI](https://doi.org/10.1146/annurev.psych.56.091103.070307). PMID 16318592. According to PubMed.

## What the paper did

Walker and Stickgold's Annual Review synthesises the sleep-dependent memory and plasticity literature through 2006, covering memory encoding, consolidation, brain plasticity, and reconsolidation. The central architectural finding for REE's purposes is that sleep effects on memory accumulate across multiple sleep cycles in a sustained dose-response manner: single-cycle interventions produce partial effects; multi-cycle full-night sleep produces the full benefit; selective deprivation (e.g. REM-only deprivation) impairs the cumulative consolidation proportional to the deprivation magnitude.

For procedural / motor skill consolidation in particular, the data converge on a pattern where the across-night gain in performance is roughly proportional to the amount of late-night REM sleep, and where REM deprivation specifically (not total sleep deprivation) blocks the gain.

## Why it matters for MECH-204

The just-landed F1 substrate in REE (`SerotoninModule._persistent_zero_point`, EMA-tracked across REM captures with `alpha=0.1` default) implements a cumulative-across-cycles dose-response architecture: each cycle contributes ~10% to the running reference, and meaningful change requires multiple cycles. This is exactly the architectural shape Walker and Stickgold document for sleep-dependent memory consolidation more broadly.

The opposing snapshot-only architecture (use the most-recent capture as the consumer target, no cross-cycle accumulation) would predict that single-cycle interventions should produce the full effect — sleep needs only ONE REM episode to recalibrate, not many. The Walker-Stickgold data weigh against that prediction for memory consolidation; by architectural analogy, they weigh against it for precision recalibration too.

This paper does NOT directly address the F1 vs F3 question (passive parameter consumption vs broadcast read at action selection). It addresses a different but adjacent question: cumulative-across-cycles vs single-cycle. Its support for the cumulative reading reinforces F1 against snapshot-only architectures (which V3-EXQ-541 effectively was: the consumer read the most-recent capture each cycle); it does not arbitrate between F1 (passive cumulative reference, just landed) and F3 (live broadcast read of the cumulative reference at action selection).

## Mapping to REE

REE's `_persistent_zero_point <- (1 - alpha) * persistent + alpha * capture` with `alpha = 0.1` is a roughly 10-cycle effective integration window — biologically plausible per the Walker-Stickgold dose-response data showing that overnight sleep effects require multi-cycle accumulation. Each REM episode's contribution is a fraction of the total. This matches the cumulative pattern documented for memory consolidation.

V3-EXQ-541b's step-size sweep is testing whether ALPHA + STEP combinations land at meaningful behavioural effect. By the Walker-Stickgold reading, the sweep should find the regime where multi-cycle accumulation produces measurable rv movement (which V3-EXQ-541a already showed mechanically — mean_abs_delta = 3.6e-3 at step=0.1) AND meaningful cross-arm divergence (which V3-EXQ-541a failed; the sweep tests whether step tuning can clear it).

If V3-EXQ-541b finds that NO step-size in the defensible band {0.05, 0.10, 0.25} clears the cross-arm divergence threshold, the Walker-Stickgold reading suggests the issue is NOT the F1 architecture itself (which they support by analogy) but the experimental cycle count (4 cycles per run may be insufficient to surface the cumulative effect) or the env's drift profile (waking re-randomisation may wash out the accumulation faster than biology does). Both are tractable without F2 / F3 architectural changes.

## Caveats

(1) The paper is about memory consolidation broadly, NOT specifically precision recalibration. The architectural transfer to MECH-204 is by analogy: both share the cumulative-across-cycles dose-response pattern, but the analogy is not directly empirically tested. (2) The paper is older (2006); recent work has refined the picture (e.g. selective spindle / SO contributions during NREM, REM-specific contributions to emotional memory). The cumulative-across-cycles claim has held up but the cycle-by-cycle attribution has gotten more nuanced. (3) The paper does not address the F1 vs F3 question REE is asking; it addresses the broader cumulative-vs-snapshot dichotomy. The F1 support is by elimination of the snapshot alternative, not by direct contrast with F3. (4) The dose-response signature is documented for memory traces (synaptic-level changes); whether precision parameters (single-scalar EMA targets in REE) follow the same dose-response is an architectural assumption.

## Confidence reasoning

0.74 supports for the F1 (cumulative-across-cycles) reading of MECH-204. Source quality 0.85 (Annual Review of Psychology; canonical comprehensive review; senior authors). Mapping fidelity 0.70 (the cumulative pattern transfers cleanly to F1 by architectural analogy; the transfer is not directly empirically tested). Transfer risk 0.25 (the pattern is broad enough — sleep cycles cumulatively refine model parameters — that it applies to both memory traces and precision parameters under the same architectural shape).

The Phase 7 implication: this paper supports F1 over snapshot-only architectures (which V3-EXQ-541 effectively was, and which the F1 fix supersedes). It does not directly arbitrate F1 vs F3, but combined with Hobson-Hong-Friston 2014 it tilts the architectural reading toward F1-sufficient over F3-needed.
