# Roesch, Calu & Schoenbaum 2007 — DA readiness over the leading option; premature-commit as pathology

**Citation.** Roesch, M. R., Calu, D. J., & Schoenbaum, G. (2007). Dopamine neurons encode the better option in rats deciding between differently delayed or sized rewards. *Nature Neuroscience*, 10(12), 1615–1624. https://doi.org/10.1038/nn2013

## What the paper does

Roesch and colleagues recorded from 81 putative dopamine neurons in the VTA of adult male Long-Evans rats trained on an odour-cued binary choice task. The rats chose between two reward wells whose outcomes differed in either delay (short vs long) or magnitude (small vs large). Identity of recorded units was supported by waveform, response properties, and apomorphine sensitivity in a subset. Standard prediction-error signatures were present on reward delivery — as expected.

The headline finding for this lit-pull is upstream of the prediction error. Cue-evoked DA firing came to reflect the *value of the better option* — the option with higher subjective value given the delay/magnitude tradeoff. Critically, this preferential encoding of the better option was present even on trials when the rat *subsequently chose the worse option*. So DA carries a readiness/value signal over the leading candidate that is dissociable, on any given trial, from the action ultimately selected.

In subsequent Roesch / Schoenbaum work (which this single paper anchors but does not exhaust), dysregulation of this signal is mapped onto impulsive-choice and addiction phenotypes — the broad class of failure I will call "premature-commit pathology" following the user's framing.

## What it says about the REE commit predicate

The current MECH-090 BetaGate elevates into committed mode on `running_variance < commitment_threshold`. This predicate has no representation of *which candidate the system is committing to*, and no readiness signal over that candidate. The Roesch finding establishes that biological action systems do carry such a signal — DA over the leading option — and that the signal is dissociable from the eventual action.

The V3-EXQ-592 seed 42 trajectory makes the gap explicit. The agent's policy collapsed to a near-fixed-point, `running_variance` fell to 2.7e-5, and BetaGate elevated — while `nav_competence` was 0.0 and no specific motor program was prepared. There is, in REE's substrate, no analogue of the Roesch DA readiness signal. The gate fired because the world stopped surprising the agent, not because the agent had prepared a plan it was ready to enact.

This is not a behavioural failure that the rv-only predicate happens to permit; it is the architectural baseline the predicate produces. If you map the failure onto the Roesch / Schoenbaum pathology axis, you get an interesting reading: the V3-EXQ-592 trajectory is a clean case of *premature commit*, the failure mode that this body of work tracks across impulsivity, addiction, and OCD-style early closure phenotypes. REE-V3 implements as baseline what those literatures characterise as pathological.

## How this translates to a substrate-design recommendation

The Roesch finding does not by itself prescribe a single implementation, but it does add a constraint that Cisek-Kalaska's affordance-competition and Hanes-Schall's accumulator-to-threshold frameworks share: the commit gate should reference a readiness signal over a specified candidate. The Roesch contribution is to specify *what kind of signal* — a value-weighted DA-style readiness over the leading option — and to anchor a pathology mapping: substrates that gate without this signal are pre-pathological by design.

For REE, a concrete operationalisation would be: compute a margin or accumulator over E3 candidate scores for the leading action class (or, more biologically motivated, over a leading goal/option at a higher level of abstraction), and condition BetaGate entry on that signal crossing a criterion. The current rv signal can be retained either as a biasing input (precision-modulated rise rate, à la urgency in modern accumulator models) or as a parallel conjunction (the GAP-4 reading the synthesis weighs explicitly).

## Limitations and caveats

The paper is about binary choice between two known cued options, not about commitment-versus-exploration in a novel environment. The translation "DA encodes readiness over the leading candidate, so a commit gate should reference that readiness" is the architectural transfer; the paper does not directly test commit-entry gating. The "premature-commit pathology" framing draws on the broader Roesch / Schoenbaum corpus (impulsivity, addiction, OCD-related early closure) more than on this one paper — a future pass should add either a Roesch impulsivity paper directly, or the Sakagami / Watanabe parallel cohorts that the synthesis flagged as residual gaps.

A second caveat: the architectural transfer relies on the proposition that REE's "committed mode" is the appropriate analogue of biological action commitment. There is a defensible reading on which it is *not* — REE's committed mode is a state-of-protected-internal-computation more than an action-onset event, and the Hanes-Schall / Roesch frameworks are specifically about action initiation. The synthesis weighs this; this entry contributes to the readiness-gate reading but does not settle the analogy question.

## Confidence reasoning

Source quality is high: Nat Neurosci, single-unit DA recording with pharmacological identity confirmation, well-controlled choice task, well-replicated in subsequent work. Mapping fidelity is moderate: the architectural claim transfers (DA carries readiness/value over the leading candidate, distinct from precision) but the specific behavioural test is binary choice rather than commit-vs-explore. Transfer risk is moderate-to-high: rat → generalised-vertebrate is well-trodden for VTA-DA function, but the "premature-commit pathology" framing genuinely draws on a corpus broader than this single paper. The `weakens` direction is on the rv-only predicate specifically: a substrate that licenses commit without a readiness signal implements as baseline what these literatures characterise as pathology.
