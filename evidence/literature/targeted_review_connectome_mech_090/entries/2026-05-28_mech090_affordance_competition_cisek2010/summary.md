# Cisek & Kalaska 2010 — affordance competition, recast for the BetaGate commit-entry question

**Citation.** Cisek, P., & Kalaska, J. F. (2010). Neural mechanisms for interacting with a world full of action choices. *Annual Review of Neuroscience*, 33, 269–298. https://doi.org/10.1146/annurev.neuro.051508.135409

## What the paper does

This is a canonical Annu Rev Neurosci synthesis, not a single empirical study. The authors review two decades of premotor and parietal cortex single-unit work in behaving macaques (their own and others'), together with a body of computational modelling, and argue that the serial perceive-then-decide-then-act pipeline that frames most action-selection research is architecturally wrong. They propose, instead, that the brain specifies multiple potential motor plans in parallel — directly encoded in premotor and parietal populations — and that biasing signals (target value, salience, urgency, recent history, prior probability) modulate those plans' relative activation in continuous time until one of them crosses a commit threshold. The framework is offered as a generalisation across reach, saccade, locomotor, and perceptual-decision domains. It is supported by the now-canonical PMd and PRR findings of co-encoding of competing reach targets, the dorsal stream's parallel-plan signatures during instructed-delay tasks, and the BG/SC accumulator literatures.

## What it says about REE's commit predicate

The current MECH-090 BetaGate elevates into committed mode when `running_variance < commitment_threshold`. That is a one-dimensional precision predicate over the E2 world-forward prediction-error trace. The Cisek-Kalaska framework does not endorse this architecture. In their model, the predicate that fires the commit is a readiness signal over a specified motor plan — a candidate action whose representation has been built up by parallel-affordance specification and biased toward selection by value/urgency inputs. Precision of internal model prediction is one of several biasing inputs to that competition; it is not, on its own, the predicate.

The V3-EXQ-592 seed 42 trajectory is exactly the failure mode this framework would predict. The agent collapsed its policy to a near-fixed-point, the dynamics it sampled became trivially self-consistent, `running_variance` fell to 2.7e-5, and the commit predicate fired — while `nav_competence` was 0.0. In Cisek-Kalaska terms: the agent never specified an affordance to commit to, so there should have been nothing for the gate to fire on. The substrate, as currently architected, has no representation of "the motor plan I am about to commit to," so it cannot ask "is that plan ready?". The rv-only predicate fills the void with a signal that the model has stopped surprising itself, regardless of whether any plan exists.

## How this translates to a substrate-design recommendation

The framework does not prescribe a specific implementation but it strongly implies the shape of one: BetaGate entry should depend on the readiness of a leading candidate action / motor program, not on a precision threshold alone. The readiness signal can be implemented in several ways — accumulator-to-threshold over E3 candidate scores (the Hanes-Schall path in this same pass-2 cohort), an explicit dopaminergic readiness burst (the Roesch path), or a margin-based readout over the E3 candidate scoring stage. Precision (current rv) becomes a biasing input to that readiness signal rather than the gate itself.

A conservative reading would keep rv as one gate and add a readiness gate in conjunction — the "rv_low AND readiness_above_floor" pattern. A more architecturally honest reading would invert the predicate: gate primarily on readiness, with rv as one of several inputs to the readiness computation. The framework leans toward the latter but does not exclude the former.

## Limitations and caveats

The framework is theoretical synthesis. It does not test the specific BG beta-elevation pattern that MECH-090 instantiates; the focal data are cortical (PMd, PRR, LIP) rather than subcortical. The transfer to BG-level commit-entry gating is by architectural posture, not by direct mechanism replication. The macaque reach task domain is also further from REE's CausalGridWorldV2 than from, say, a rodent navigation task — but the framework explicitly aims for cross-domain generality, and the architectural commitments are at a level of abstraction where the transfer is defensible.

A second caveat: Cisek-Kalaska is one of several frameworks in this conceptual neighbourhood. The drift-diffusion / accumulator literature (Gold & Shadlen, Hanes & Schall) makes overlapping but distinct claims about what gates commitment. Pass-2 includes the Hanes-Schall entry as a complementary anchor; the Cisek-Kalaska piece supplies the affordance-competition architecture that the accumulator literature operationalises.

## Confidence reasoning

Source quality is very high — Annu Rev Neurosci canonical synthesis by the framework's originators, cited 2000+ times. Mapping fidelity is moderate-to-high: the framework's architectural commitments transfer cleanly to the commit-predicate question even where focal recordings are cortical. Transfer risk is low: the framework is explicitly cross-domain and is widely adopted in BG/cortico-striatal modelling. The `weakens` direction reflects the framework's incompatibility with the current rv-only implementation, not a contradiction of any specific MECH-090 sub-claim about beta as a status-quo signal — those remain intact; the framework relocates them within a richer predicate.
