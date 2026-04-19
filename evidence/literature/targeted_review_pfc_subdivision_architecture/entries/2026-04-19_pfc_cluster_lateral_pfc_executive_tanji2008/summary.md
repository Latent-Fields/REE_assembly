# Tanji & Hoshi 2008 — Role of the Lateral PFC in Executive Behavioral Control

## What the paper does

This Physiological Reviews synthesis from the Tanji lab covers the integrated function of lateral PFC, pre-SMA, SMA, and dorsal premotor cortex in executive sequence control. The Tanji lab is best known for systematic single-unit recording across these regions during sequence tasks, and the review argues for a functionally graded system: lateral PFC holds rules and goals; pre-SMA plans sequences and handles set-switching; SMA and dorsal premotor cortex execute sequences and implement stimulus-action bindings. The functional distinctions are supported by lesion dissociations, single-unit response profiles across task phases, and microstimulation-evoked behavioural effects.

## Key findings relevant to the PFC cluster

The load-bearing contribution for REE is the substrate boundary between the lateral-PFC-analogue and what sits downstream of it. In REE's current architecture, the E3 sequence-selection machinery already performs a lot of what the pre-SMA / SMA / dorsal premotor literature attributes to those regions: holding candidate sequences, selecting among them, binding actions to states. This means the existing E3 implementation is already the REE premotor/SMA-analogue. What is missing is the upstream substrate — the lateral-PFC-analogue that holds the rule context E3 operates inside.

That reshapes the design question. Rather than adding a whole new suite of modules, REE needs to add one clear upstream module (lateral-PFC-analogue for rule/goal maintenance) and recognise that premotor/SMA-analogue function is already implemented inside E3. The Tanji & Hoshi framing supports that this minimal addition is biologically plausible and not an oversimplification.

## How this translates into REE

Concrete architectural implication:

- The lateral-PFC-analogue (new in V3/V4) holds the currently active rule and the currently held goal.
- E3 (premotor/SMA-analogue, already implemented) proposes and selects sequences in service of that rule/goal.
- Write gating under MECH-261:
  - Rule/goal writes into the lateral-PFC-analogue are licensed during external_task and internal_planning; consolidated slowly during offline_consolidation; suppressed during internal_replay (so imagined sequences don't rewrite the held rule).
  - Sequence-level updates into E3 / premotor/SMA-analogue are already governed by MECH-094 (hypothesis tag) and its MECH-261 generalisation.

## Limitations and caveats

The 2008 review predates the more recent pre-SMA / SMA parcellation work and the premotor subdivision work that has since refined the anatomical picture. Some of its specific anatomical claims have been revised. The review is also primate-heavy, and rodent premotor organisation does not cleanly align. REE should adopt the functional-gradient framing (rules → planning → execution, with separable substrates at each level) without over-committing to the 2008 anatomical specifics.

## Confidence reasoning

Source quality high (Physiological Reviews, Tanji lab). Mapping fidelity moderate-strong: the rule/sequence-execution distinction matches what REE needs. Transfer risk moderate, mostly from anatomical-refinement drift since 2008. Net confidence: 0.78.
