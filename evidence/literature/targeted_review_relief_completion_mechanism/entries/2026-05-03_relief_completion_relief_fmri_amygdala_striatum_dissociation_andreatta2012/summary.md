# Andreatta, Fendt, Muhlberger et al. 2012 — Onset and offset of aversive events establish distinct memories requiring fear and reward networks

## What the paper did

This is a two-species design — human fMRI plus rat pharmacological inactivation — testing whether relief and fear memories share a substrate or use distinct circuits. Humans underwent Pavlovian conditioning where one cue preceded an electric shock (fear conditioning) and another cue followed shock cessation (relief conditioning). fMRI tracked which structures encoded each kind of cue. In parallel, rats received muscimol injections into either the basolateral amygdala or the ventral striatum before retrieval of conditioned fear or conditioned relief, asking which structure each memory required.

## Key finding

The dissociation was clean in both directions and in both species. Fear-conditioned cues drove activation in the amygdala (and not the striatum) in humans, and amygdala inactivation in rats blocked conditioned fear without affecting conditioned relief. Relief-conditioned cues drove activation in the ventral striatum (and not the amygdala) in humans, and ventral-striatum inactivation in rats blocked conditioned relief without affecting conditioned fear. The two memory systems are anatomically separable, and the relief system maps onto the reward network — the same ventral striatum that encodes appetitive reinforcers — not onto a parallel aversive-only structure.

## How it translates to REE

This is the load-bearing entry for the architectural decision the user posed. It directly tests whether relief uses goal-achievement / reward machinery (Model 1) or a parallel aversive-channel mechanism (Model 2). The answer at the level of structure is unambiguous: relief is computed in the reward circuit. A REE relief-completion mechanism that fires MECH-057a (commitment release / beta gate drop), MECH-091 (salient-event phase reset), and MECH-094 (hypothesis tag write) is biologically licensed — those are the post-event consolidation pipeline that goal-achievement uses, and the empirical evidence here says relief sits on top of the same substrate.

The paper does not, however, tell us the *full* story. It shows that the ventral-striatal relief signal is required for conditioned relief expression, but it does not test whether predictive encoding of safety cues — knowing that *this thing predicts* relief, as opposed to relief just having happened — uses a parallel circuit. Other papers in this slate (Kreutzmann 2020, Meyer 2019) suggest safety-signal encoding has its own infralimbic / ventral-hippocampal substrate. So the cleanest architectural reading is: the *completion event* uses goal-achievement machinery (Model 1), and *long-horizon safety prediction* may have a parallel encoder.

## Limitations and caveats

The fMRI activation is correlational and the rat lesion is gross structural — neither resolves whether relief uses the same neurons or same dopamine receptors as reward, only that the same structure is required. The paper also does not probe the infralimbic cortex or ventral hippocampus, both of which other work implicates in safety processing. So the dissociation it draws is between fear and relief, not between relief and safety, and that distinction matters for the eventual REE spec.

The conditioning paradigms are short-horizon Pavlovian. Whether the same dissociation holds for the kind of long-arc suffering-reduction the REE substrate would have to model is a transfer assumption rather than a tested one — but the convergence with the broader pain-relief / DA literature (Navratilova et al.) makes that transfer reasonable.

## Confidence

Source quality is high (peer-reviewed cross-species design, well-cited). Mapping fidelity is high because the paper directly tests the architectural question. Transfer risk is reduced by the cross-species replication. Net confidence 0.86, supports — and this is the entry that most strongly settles the M1 vs M2 branch toward Model 1 for the completion event itself.
