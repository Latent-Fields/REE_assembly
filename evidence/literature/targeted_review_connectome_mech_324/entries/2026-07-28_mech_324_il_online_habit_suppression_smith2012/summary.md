# Reversible online control of habitual behavior by optogenetic perturbation of medial prefrontal cortex (Smith, Virkud, Deisseroth & Graybiel, PNAS 2012)

## What the paper did

Rats were trained to run a T-maze until the behaviour was habitual, and the habit status was not assumed -- it was confirmed by reward-devaluation testing. Then, during the roughly three-second maze run itself, the experimenters optogenetically disrupted population activity in infralimbic cortex, a small region of medial prefrontal cortex. The design is within-animal and, crucially, the perturbation was later re-imposed after weeks of further training during which the rats acquired a *different* behavioural pattern. Generalised performance ability and motivation to consume reward were measured as controls and were unaffected.

## Findings relevant to MECH-324

Two, and both land squarely on the claim.

The first is that disrupting infralimbic cortex blocked the habit *online*: within an average of three trials, about nine seconds of inhibition, and as early as the very first trial, under three seconds. A habit that took weeks to build was suspended in seconds. Habit maintenance is therefore not a one-shot consolidation event with a persisting product; it is a continuously-supplied gate, and removing the gate removes the behaviour immediately.

The second is the one I think matters more for us. When the same perturbation was imposed again -- after weeks in which a new behavioural pattern had been trained and had become dominant -- the rats "regained the suppressed maze-running that typified the original habit", and the newer habit was simultaneously blocked. The original habit had not been overwritten by the new one, and had not decayed. It had been sitting there, unexpressed, for weeks, fully intact and immediately available the moment the gate moved.

## How this translates to REE

MECH-324's registered ARM_1 versus ARM_2 dissociation is, in substrate terms, the first finding. With `use_chunk_maintenance` off, chunks still form but never crystallise and never become selectable -- which the implementation note already describes as "the substrate analog of Smith & Graybiel 2013 IL disruption". This paper is the sharper version of that citation: it is the acute, causal, reversible manipulation, and it says that what is lost under IL disruption is *expression*, not the underlying unit.

The second finding is the biological warrant for the correction landed on 2026-07-27 (ree-v3 `6c3e67e`), and it is worth being blunt about how directly it bears. As first built, DISSOLVED was an absorbing tombstone: the chunk was kept in the library for the audit trail, `note_outcome()` skipped any sequence already present, and `note_real_execution()` had no DISSOLVED branch -- so the retained record permanently blocked its own sequence from ever re-forming, at any number of repetitions and any outcome consistency. Measured on the contract fixture, two hundred further trials of a perfectly consistent above-baseline regime left the chunk dead. Smith et al. 2012 says biology does the opposite, and does it emphatically: after weeks of a competing behaviour being trained over it, the suppressed unit came straight back. The correction to suppression-with-retention, with re-formation at a reduced bar `R_reacq = R_min * f_reacq`, is what this result requires. The correction was made before this paper was on file; the paper retrospectively vindicates it.

## Limitations and caveats

The intervention is acute and exogenous. Nothing is dissolving here because outcomes became inconsistent -- an experimenter switched off a cortical region. So this paper speaks to *retention* and to *maintenance being continuously required*, and it says nothing at all about MECH-324's sub-mechanism (B), the asymmetric hysteresis gate where `variance_low < variance_high` is enforced by config validation. That band, and `f_reacq`, remain uncalibrated engineering defaults on the same footing as `F_high`, and this entry does not change that.

There is also an unmodelled degree of freedom that I want on the record rather than buried. The perturbation toggled *both* ways in a single intervention -- restoring the old habit while blocking the new one. That looks like competitive selection among retained units, not like independent per-unit gates. MECH-324 implements per-chunk lifecycle states with no cross-chunk competition. If a validation experiment finds REE's chunks dissolving independently where the biology predicts a trade-off, this is the first place I would look, and it would be a design gap rather than a bug.

And a caveat that cannot be resolved from this design: the paper cannot distinguish "the habit was retained and merely suppressed" from "the habit was re-learned extremely fast on re-exposure". Behaviourally those look the same on the timescale tested. MECH-324 commits to retention; the alternative reading -- savings rather than storage -- would be compatible with the same data, and is closer to what the `f_reacq` reduced-bar mechanism actually implements. Arguably REE has hedged this correctly by accident, since a reduced re-formation bar is a savings mechanism dressed as a retention mechanism.

## Confidence reasoning

0.82. This is a causal manipulation with devaluation confirmation of habit status, within-animal reversibility, and explicit performance and motivation controls -- about as strong as this literature gets, and MECH-324's "causally required for chunk crystallisation" framing needs exactly a causal result rather than a correlational one. Mapping fidelity is high but not exceptional, held down by the acute-versus-gradual mismatch and the cross-chunk competition the claim does not model. Transfer risk is comparatively low because what is being carried across is architectural -- a gate that suppresses without erasing -- rather than any parameter value.
