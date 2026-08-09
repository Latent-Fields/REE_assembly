# Neunuebel & Knierim (2014) — CA3 completes while DG separates, measured simultaneously

**Source:** Neuron 81(2):416–27. DOI [10.1016/j.neuron.2013.11.017](https://doi.org/10.1016/j.neuron.2013.11.017). PMID 24462102 / PMC3904133. Retrieved via PubMed.

**Claim:** SD-016 (selection mechanism leg — GOV-FANOUT-1 H2).
**Direction:** supports. **Confidence:** 0.79.

## What the paper did

The theoretical claim that the dentate gyrus separates patterns while CA3 completes them dates to
Marr and had been the organising framework for hippocampal memory models for decades. What it lacked
was a direct measurement — most of the single-unit literature up to that point was CA1 recordings,
and comparisons across regions were made between separately-recorded populations under nominally
matched conditions.

Neunuebel & Knierim recorded DG and CA3 **simultaneously** in behaving rats, then put local and
global spatial reference frames into conflict (the double-rotation paradigm). This gives the clean
comparison: the same perturbation, the same animal, the same session, two regions at different stages
of the same circuit. The dissociation is unambiguous. DG's representation of the conflict changed
*more* than its entorhinal inputs did — that is pattern separation, an amplification of input
differences. CA3's representation changed *less* than either its entorhinal or its DG inputs — that is
pattern completion. And critically, CA3 produced a coherent population response *even though its DG
input was severely disrupted*, meaning CA3's output was closer to the originally stored representation
than the degraded input it was working from.

## Why this matters for SD-016

This is the H2 entry. Espinoza and Kim & Lim between them tell us what a competitive *operator* should
look like; this paper raises the prior question of what the operator should be competing *over*, and
it does so by showing that the biological system does not attempt the job in one stage.

The two stages perform **opposite** transformations. DG amplifies differences between similar inputs.
CA3 suppresses differences in service of retrieving a stable stored pattern. Those objectives are
genuinely antagonistic — push toward separation and you degrade your ability to retrieve a stored
association from a partial cue; push toward completion and distinct contexts collapse together.
Knierim & Neunuebel's 2015 review of the same body of work (also in this pull's search, PMID 26514299)
makes the arbitration explicit: CA3 can perform *either* separation or completion "depending on the
nature of its inputs and the relative strength of the internal attractor dynamics."

SD-016 asks a single feedforward stage to do the whole job — take z_world, select which of 16
ContextMemory slots is relevant. On this evidence that stage is carrying two conflicting objectives
with no structural place to arbitrate between them.

That yields the most useful thing this entry contributes, and I want to flag clearly that it is **my
inference from the result rather than a finding of the paper**: uniform mixing over all 16 slots *is*
maximal pattern completion with zero pattern separation. It is the degenerate corner of the
separation–completion trade-off. And it is precisely where you would expect a stage to settle if it
has a retrieval objective (`terrain_loss` wants usable content out) and no separation pressure
whatsoever. That reframing does not overturn the V3-EXQ-898 autopsy's diagnosis — it sharpens it. The
autopsy said no tested mechanism has ever been given a training signal that specifically rewards
context-conditioned divergence. This says the same thing in the biology's own vocabulary: every
mechanism tried so far has been a completion stage with no separation stage in front of it, and
`ln(16)` is what perfect completion looks like from the outside.

Encouragingly, that reading makes a testable prediction which the H3 leg will incidentally check: if
the saddle is the completion corner rather than an optimisation failure, then adding genuine
separation pressure should move entropy (C1) and context-divergence (C1b) **together**. If H3's
competitive operator drops entropy while divergence stays flat, the completion-corner reading is
wrong and something else is going on — most likely the 418m signature of a static non-uniform
selector.

## Limitations

The mapping is architectural-by-analogy and it **motivates a build rather than validating one**. REE
has no DG/CA3 stage separation for this result to map onto; the paper is an argument for creating a
two-stage structure. That is the honest reason mapping_fidelity sits at 0.70 rather than higher, and
it is also why H2 is correctly scoped in the portfolio as the deferred, larger leg rather than
something to attempt alongside H1 and H3.

Three further caveats worth carrying into any H2 scoping:

- **CA3's completion rests on recurrent attractor dynamics.** A retrieval unit with no recurrent
  component does not merely perform the separation–completion balance badly — it does not *have* that
  balance as a parameter at all; the architecture fixes it implicitly. Adding recurrence to SD-016's
  retrieval path is a substantial build, not a knob, and the H2 leg should be scoped on that basis.
- **"Separation" is not only disjoint selection.** In DG the separation here is expressed largely
  through *firing-rate* changes in place-modulated granule cells; Leutgeb et al. (2007, Science, DOI
  [10.1126/science.1135801](https://doi.org/10.1126/science.1135801)) found the population-recruitment
  mechanism — new non-overlapping cell assemblies — in CA3 rather than DG, and concluded that
  separation is *dual-mechanism*. An REE design that assumes separation means "pick disjoint slots"
  imports only one of the two and may miss rate-coded separation entirely. Since SD-016's C1b
  instrument is a divergence between per-context selection distributions, it should in principle catch
  rate-like separation too — but that is worth confirming rather than assuming.
- **The paradigm is a strong perturbation.** Local–global cue conflict is deliberately extreme. The
  result does not establish that the same division of labour operates under ordinary non-conflicting
  input, which is the regime SD-016 mostly runs in.

Finally, the domain jump is real and I have priced it at transfer_risk 0.35: this is spatial
representation under cue conflict in rats, and SD-016's contexts are safe-versus-dangerous terrain.
The claim that those are the same kind of distinction is an inferential step the paper does not
license. What transfers is the computational division of labour, not the spatial result.
