# The context channel is real and graded — but fragile (Isarida et al. 2020)

**Claim under test:** MECH-339 — the composite ghost-bank cue and its outshining gate. This entry addresses a different facet from its companion (the 2018 outshining paper): not the *gate*, but the *channel the gate operates on*. Is there a real, recoverable contextual retrieval signal worth composing into the cue at all, and how does its strength behave?

## What the paper did

The same Shizuoka group asked why environmental context-dependent *recognition* is so often null when context-dependent *recall* is robust. Their move here is to enrich the context: instead of studying and testing items against a static photograph of an environment, participants encounter the items embedded in a **dynamic video** context. The finding is that video contexts produce reliable context-dependent recognition effects where static photographic contexts typically do not. The richer, more distinctive, temporally extended context furnishes a stronger contextual retrieval cue, and a measurable recognition advantage follows when that context is reinstated at test.

## Why it bears on MECH-339

MECH-339 makes two bets. The first — the one the 2018 paper supports — is that the context contribution is *gated* by direct-cue strength (outshining). The second, which this paper speaks to, is the prior assumption that **there is a contextual channel worth carrying**: that the preserved-but-match-unused SD-039 payload (`arousal_tag`, `last_vs`, `cause`) holds genuine retrieval-relevant signal, and that its contribution should *scale with how much information it carries*. The implemented salience term, `context_salience = 1 − exp(−arousal_tag / arousal_scale)`, is exactly a "richer context → stronger channel" monotone. Isarida et al. 2020 is behavioural confirmation that contextual retrieval signal is real and that its potency scales with informational richness — thin contexts (static photos) give little, rich contexts (video) give a reliable effect.

It also draws the *boundary* MECH-339 needs to respect. Context-dependent recognition is fragile: a context can be present at encoding and still contribute nothing at retrieval if it is informationally thin. That argues against a flat context term that credits any stored payload equally. The salience weight must be sensitive to content — which is the design already chosen, and this paper is the reason to keep it that way rather than collapsing to a constant.

## Why it is logged "mixed," not "supports"

The honest limitation: this study manipulates *context richness*, not *item-cue strength*. The outshining gate is defined by the inverse dependence of the context effect on the **direct** cue's strength, and that is not what is varied here. So the paper motivates and bounds the context channel (supports its existence and gradedness) without testing the gate's conditional shape (which the 2018 companion does). Logging it `mixed` keeps the evidence record honest about what it actually demonstrates: a real, content-scaled context channel, plus a fragility boundary, rather than a second independent confirmation of the gate. As always this is parallel literature signal — `exp_conf` for MECH-339 stays 0 (candidate / v3_pending).

## Confidence

`mixed`, confidence **0.50**. Source quality high (JML, careful design). Mapping fidelity moderate — it validates the premise behind the context channel and its salience weight, not the gating rule. Transfer risk moderate, the same human-recognition-to-agent-goal-bank analogy that caveats the companion entry. Taken together, the two 2018/2020 entries cover MECH-339's two bets: the gate (strength-conditional, 2018) and the channel it gates (real and graded, 2020).
