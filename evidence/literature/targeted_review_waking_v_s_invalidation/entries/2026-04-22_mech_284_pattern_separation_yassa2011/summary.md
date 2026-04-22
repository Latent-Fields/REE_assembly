# Yassa & Stark 2011 -- Pattern Separation in the Hippocampus

According to PubMed ([DOI](https://doi.org/10.1016/j.tins.2011.06.006)).

## What the paper does

Yassa and Stark synthesise the convergent evidence -- electrophysiological remapping, lesion studies, immediate-early gene imaging, transgenic mouse models, and human fMRI -- that the hippocampal dentate gyrus and CA3 produce *orthogonal* neural representations for similar inputs. The DG/CA3 transfer function is highly sensitive to small input changes: a slight shift in spatial context or stimulus identity is amplified into a markedly different population code. CA1, by contrast, supports a more graded transfer function. The review also covers age-related and neurogenesis-related modulation of this capacity, which becomes the anchor for clinical relevance.

## Why it matters for V_s invalidation

The architectural mapping I want to make is that DG remap rate is a candidate substrate for *interference detection* -- the upstream signal that the currently anchored schema is being challenged by alternative representations of the same regional inputs. If V_s is the verisimilitude of the anchored schema, then a region in which the same anchor keeps being mapped to subtly different DG patterns is a region in which the anchor is no longer doing the work it should. A DG-remap-rate signal could feed MECH-284's accumulator as one of its inputs.

The mapping is honest about its indirection. Pattern separation in the canonical Yassa-Stark sense is about *producing* distinct representations, not about flagging that a previous representation has become invalid. The translation from "high DG remap rate" to "the anchor is becoming stale" requires an extra step: that the brain reads remap rate as a validity signal, not just as a separation operation. I have no direct evidence for that read-out. It is structurally plausible because remap rate would be one of the easier signals to integrate over a window, and because the same anatomical pathway (DG -> CA3 -> CA1 -> EC) that produces the remapping also has the latency to feed downstream accumulators.

## What the paper does not do

It does not measure V_s. It does not address whether DG remap rate is read out by other circuits as a validity signal. It does not directly test the interference-detection role I am proposing -- though the Reagh 2018 paper later in this pull, which I include partly to anchor the DG/CA3 literature to behavioural mnemonic discrimination deficits, gets one step closer to that.

## Clinical resonance

The clinical hook is age-related decline. If DG remap rate is a substrate for interference detection, then DG dysfunction in aging and early Alzheimer's should produce schema-rigidity through a failure to register interference. Reagh 2018 (next paper) shows exactly that pattern: alEC hypoactivity combined with DG/CA3 hyperactivity correlates with mnemonic discrimination deficits. The interpretation maps cleanly to a V_s-invalidation failure: the broadcast trigger may still fire, but the local interference signal that should bias the accumulator is gone.

## Confidence reasoning

Source quality high. Mapping fidelity moderate (0.55) -- the structural inference is plausible but the read-out step is unverified. Transfer low (0.25). Aggregate 0.66.
