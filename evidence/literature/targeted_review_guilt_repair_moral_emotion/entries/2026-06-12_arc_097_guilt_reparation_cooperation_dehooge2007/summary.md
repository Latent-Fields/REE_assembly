# de Hooge, Zeelenberg & Breugelmans (2007) — Moral Sentiments and Cooperation: Differential Influences of Shame and Guilt

**Claims grounded:** ARC-097 (guilt-as-repair routing), MECH-411 (E3 repair-trajectory generation)
**Direction:** supports · **Confidence:** 0.74

## What the paper did

Where Tangney et al. review the *distinction* between guilt and shame, de Hooge and colleagues test its *behavioural consequences* experimentally. Across a series of laboratory experiments with healthy adults, they induced guilt or shame (or a neutral state) and then measured social behaviour in cooperative and allocation tasks — economic-game-style choices about whether to give resources to, or cooperate with, another party. The design is what makes it valuable for grounding an architectural routing claim: it does not merely ask people how guilt feels; it observes what guilt makes them *do*.

## Key findings relevant to the claim

The central result is that guilt and shame have *differential* effects on behaviour, and that guilt specifically motivates reparative, prosocial action directed at the harmed party. A guilt induction increased cooperation and the willingness to compensate or restore the relationship with the victim, in a way a shame induction did not. A particularly diagnostic finding from this line of work is that guilt's reparative push is *regulated by whether the damage has already been repaired*: when another party repairs the harm, the transgressor's reparative intentions and prosocial behaviour fall away. In other words, the guilt signal is not a static badness flag — it is tied to the *accomplishment* of repair, and it discharges when repair is done. This is precisely the shape REE wants: a self-attributed-harm signal that generates and selects a reparative action, and whose pressure depends on whether repair has been achieved.

## How it translates to REE

ARC-097 asserts that self-attributed harm "must open repair and policy-update pathways," and MECH-411 makes that concrete: after self-attributed harm, E3 should *generate* repair trajectories and *compare* them against avoidance, concealment, and ordinary goal-continuation, selecting the repair branch. de Hooge et al. supply the behavioural evidence that, in humans, guilt does exactly this selection — it preferentially produces reparative action over the alternatives — and that the selection is targeted at the harmed other. The regulation-by-repair finding additionally foreshadows MECH-412 (repair completion releases residue): if human guilt subsides once repair is accomplished, the REE residue-release mechanism is modelling a real regularity, not inventing a convenience.

## Limitations and caveats

The dependent measures here are human cooperative choices following emotion inductions; MECH-411 is an E3 trajectory-generation-and-comparison computation over a represented other's value trajectory (D_{V,j}). The paper establishes that guilt selects reparation over alternatives in people — it does not show that an argmin over E3-generated trajectories is the mechanism that does so, nor that REE yet represents the repair *target* (another agent) at all; that representation is exactly what the ETH-1 / ARC-083 readiness gates say is missing in V3. There is also an important failure signature: later work in this programme shows guilt-driven compensation can be displaced onto uninvolved third parties when that is the cheaper way to discharge the guilt. So the human signal is reparative-*intending* but not guaranteed globally prosocial — a caution that REE's repair-routing must target the actually-harmed other, not merely seek the cheapest residue discharge.

## Confidence reasoning

I set confidence at 0.74. The experimental, behavioural design lifts it above a purely correlational or review-level entry, and the mapping to the repair-routing prescription is direct. I hold it in the mid-band because it is a single (multi-experiment) lab paper on healthy adults using induced emotion and economic-game behaviour, the transfer to a synthetic E3 mechanism is non-trivial, and the conditional/displaceable nature of human guilt-repair means the simple REE routing captures only the core of a more textured phenomenon.
