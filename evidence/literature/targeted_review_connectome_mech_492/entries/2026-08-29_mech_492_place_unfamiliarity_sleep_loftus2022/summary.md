# Loftus et al. (2022) — place is a real, non-redundant input to sleep, and it overrides homeostasis

**Claim tested:** MECH-492 (MECH-286's sleep-permission threat conjunct is an uncalibrated, undeclared-source consumer of the shared `z_harm_a.norm()` expression)
**Direction:** supports (the function, not the defect)

## What the paper did

Most of what we know about sleep regulation comes from animals in boxes, where the ecology has been deliberately removed. Loftus and colleagues went the other way: tri-axial accelerometry collars with simultaneous GPS on a whole troop of wild olive baboons at Mpala, across many nights, including nights at familiar roosting sites and nights at unfamiliar ones.

The headline result is a negative one for the standard model. Homeostatic sleep pressure did not have the last word. Animals slept less when at unfamiliar sleep locations — and, tellingly, did not make it up afterwards. There was no compensatory recovery sleep. Ecological context did not merely *bias* the homeostatic drive; on these nights it beat it, and the debt went unpaid.

## What this says about MECH-492

MECH-286's sleep-onset gate is a three-way AND, and one of its conjuncts, `threat_ok`, exists to withhold sleep permission when the agent's location is unsafe. MECH-492's charge is that this conjunct reads an expression which, measured, carries no place-safety information: V3-EXQ-950 put it at AUC 0.5016 under `damage_sourced` and 0.4966 under `proximity_ema_sourced`, chance under both.

The obvious rejoinder to a defect claim like that is: so what — maybe the term was never doing much anyway, and the other two conjuncts carry the gate. Loftus et al. are the reason that rejoinder does not land. In a real sleeper in a real environment, place is not a decorative input. It is strong enough to suppress sleep against accumulated homeostatic pressure and strong enough that the resulting loss is simply absorbed rather than recovered. If the biological analogue of `threat_ok` were a weak modulator, we would expect rebound; we do not see it. That is a hard constraint, and a hard constraint implemented by a chance-level signal is precisely the "silently degrades to always-permit" failure MECH-492 predicts.

There is something else worth noticing, which is that these baboons were not injured. Nothing had bitten them. The entire effect this study measures occurs in a regime where a damage-sourced threat signal reads zero — which is the cleanest statement I can give of why sourcing is the whole question here, rather than a wiring detail.

## Limitations, stated plainly

The paper measures *unfamiliarity*, not *hazard*, and I do not want to blur those. An unfamiliar site may well be safer than the familiar one; the baboons' caution is a prior, not a measurement. MECH-492's own falsifier is defined against ground-truth hazard, so this is an adjacent operationalisation rather than the same one.

More limiting still: this is behavioural work. It establishes that place modulates sleep. It says nothing about which neural signal *carries* place safety, so it cannot arbitrate between `damage_sourced` and `proximity_ema_sourced` — and the sourcing question is MECH-492's actual subject. Nor can it say anything about the 0.4 threshold or about the arithmetic of conjunctive degradation. The study is also observational; the place-to-sleep link is correlational, however well-instrumented.

And the transfer is long. Wild primate behaviour to an artificial sleep-onset gate asks a lot. The paper's *social* pressures — troop dynamics, neighbour proximity — have no REE analogue whatsoever, so only half the finding maps at all.

## Why confidence 0.68

Source quality 0.82: eLife, well-instrumented, ecologically valid, but observational. Mapping fidelity 0.66: the functional role maps cleanly, the unfamiliarity-versus-hazard operationalisation does not quite, and the mechanism is absent. Transfer risk 0.42. The aggregate is deliberately modest. This entry earns its place by closing off the "the term probably didn't matter" escape route — it establishes that a place-safety conjunct is doing real work in any sleeper worth the name. It does not, and should not be read to, establish anything about REE's wiring.
