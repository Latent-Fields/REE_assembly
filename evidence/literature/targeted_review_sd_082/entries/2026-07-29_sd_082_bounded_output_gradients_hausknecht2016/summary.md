# Hausknecht & Stone 2016 — someone already ran this ablation, and the tanh arm lost

**Claim:** SD-082 (`pfc.lateral_pfc.common_mode_invariant_trained_rule_to_action_readout`)
**Direction:** mixed · **Confidence:** 0.74
**Source:** ICLR 2016; preprint [arXiv:1511.04143](https://arxiv.org/abs/1511.04143)

## What the paper did

Hausknecht and Stone were training a DDPG-family actor-critic on RoboCup Half Field Offense, where
each discrete action carries continuous parameters (dash power, kick direction). They hit a problem
that will sound familiar: "after a few hundred updates, we observed continuous parameters routinely
exceeding the bounds." The critic simply kept asking for more power, forever.

So they compared three ways of enforcing a bound, and reported what each did:

1. **Zeroing gradients** — "examine the critic's gradients for each parameter and zero the gradients
   that suggest increasing/decreasing the value of a parameter that is already at the upper/lower
   limit."
2. **Squashing gradients** — "A squashing function such as the hyperbolic tangent (tanh) is used to
   bound the activation of each parameter. Subsequently, the parameters are re-scaled into their
   intended ranges."
3. **Inverting gradients** — "Gradients are downscaled as the parameter approaches the boundaries of
   its range and are inverted if the parameter exceeds the value range."

Only the third worked. The best agents went on to outscore the 2012 RoboCup champion.

## Why this entry matters more than the others

Because those are not three approaches *related to* SD-082's decision. They **are** SD-082's
decision, tested head to head, ten years ago, under their own names.

Condition 1 is the landing path: `bias_raw.clamp(-bias_scale, +bias_scale)`, whose flat region
zeroes `d bias / d head_params`. It failed. "Unstable learning was observed in one of the two
zeroing gradient agents", and the remaining stable agent "showed clear results of not learning."
That is an independent replication of the V3-EXQ-822 null — 70 episodes of REINFORCE moving nothing
— arriving from a different algorithm, a different task and a different codebase. SD-082's
root-cause analysis is in good shape.

Condition 2 is SD-082(ii). And it also failed:

> "parameters stayed within their bounds, but squashing functions quickly became saturated"
>
> "The resulting agents take the same discrete action with the same maximum/minimum parameters each
> timestep."
>
> "Given the observed proclivity of the critic's gradients to push parameters towards ever
> larger/small values, it is no surprise that squashing function quickly become saturated and never
> recover."

Read that middle quote against SD-082's problem statement. Every output pinned at the same rail, no
differentiation between alternatives, identical behaviour every tick — that is the *exact pathology
SD-082 was built to remove*, reappearing under SD-082's own remedy. And "never recover" is the
operative phrase. Tanh's gradient is non-zero everywhere, which is the whole argument for preferring
it to a clamp, but it decays exponentially: under sustained one-directional pressure you reach a
soft-saturated state that is practically as dead as a hard clamp and, unlike a hard clamp, offers no
obvious signal that it has happened. A clamp at least tells you it is clamping.

## The caveat that may rescue SD-082 — and why it is an argument, not a reassurance

There is a real disanalogy, and it cuts in SD-082's favour, so it deserves stating carefully rather
than gratefully.

Saturation here was driven by a critic pushing monotonically outward — "ever larger/small values."
Against monotone outward pressure, *any* squashing bound saturates eventually; the tanh arm never
had a chance. In SD-082, the systematic outward push had an identified source: the SD-008 common
mode, which is precisely why every candidate's raw output overshot `bias_scale` **in the same
direction** and landed on one rail. Component (i) removes that source.

So SD-082(i) and (ii) are not two independent improvements bundled together — (i) plausibly
*protects* (ii) by removing the pressure that would otherwise saturate it. The honest reading is
that this counter-evidence applies with full force to a tanh bound *alone* and with reduced force to
tanh-plus-centering.

But "reduced" is not "removed", and the argument has a gap: REINFORCE on a bias head could develop
sustained one-directional pressure for reasons that have nothing to do with the common mode. If a
particular bias direction is reliably rewarded, the head will keep pushing that way, and nothing in
SD-082 stops it from pushing into saturation. `readout_init_scale = 0.25` sets the *initial*
operating point into tanh's responsive band; it says nothing about where the head ends up after a
training window.

## The consequence for V3-EXQ-822a, stated plainly

The acceptance criterion — `on_prop_delta_mean >= 0.001` with an ON>OFF contrast — is a **window
mean**, and it is blind to this failure mode.

A run that starts in the responsive band (as `readout_init_scale` intends) and saturates partway
through P1 will show a healthy early `prop_delta` and a dead late one. It can clear the 0.001 floor
on the mean while *ending in exactly the state SD-082 exists to prevent*, and it would be reported
as a pass. That is the specific way this validation could mislead us, and it is cheap to close:

- log the **saturation fraction** (share of candidates with `|bias_raw| > bias_scale`) and the head
  **grad-norm** as *time series* over P1, not window means;
- read the **trend**, not the average. A falling `prop_delta` with a rising saturation fraction is
  the Hausknecht failure recurring, whatever the mean says.

And if it does recur, the fallback is not a fresh design cycle: **inverting gradients** is the option
that actually worked in this comparison, and SD-082 never evaluated it. Recording that here so a
822a failure routes to a known alternative rather than to another round of substrate invention.

One further warning worth carrying, from their condition 1. Zeroing failed not only by
non-learning but by **overflow** — "parameters still overflow their bounds", hypothesised to come
from "gradients applied to other parameters pi ≠ p which inadvertently allow parameter p to
overflow" (they observed a dash power of 120 against a maximum of 100). The lesson is about coupled
heads: bounding each output element does not keep the others controlled when the parameters are
shared. The SD-033a bias head emits a per-candidate vector from shared weights, so per-candidate
bounding does not give per-candidate control of where each candidate sits relative to the bound.

## Confidence reasoning

Source quality 0.78 — ICLR 2016, foundational for parameterized action spaces, but the bounding
comparison is a methods ablation with roughly two agents per condition in one domain. Enough to
establish that the failure mode exists and is not exotic; not enough to establish its rate.

Mapping fidelity 0.85 — the highest in this pull, above even the Kaufman entry, for the simple
reason that this paper does not merely inform SD-082's mechanism, it *tests SD-082's two candidate
mechanisms against each other*.

Transfer risk 0.45 — the highest here, and load-bearing rather than cosmetic, because the pressure
regime differs in the specific way that (i) may neutralise.

Aggregate 0.74, direction **mixed**. Mixed rather than weakens because the halves genuinely oppose:
the paper strongly corroborates SD-082's root-cause analysis while supplying the clearest available
reason to doubt its remedy. It should be read as raising one specific, instrumentable risk for
822a — saturation drift within P1, invisible to a window-mean test — and as pre-identifying the
fallback if that risk lands.
