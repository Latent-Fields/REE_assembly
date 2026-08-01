# Fanselow, Hoffman & Zhuravka 2019 -- Timing and the transition between modes in the defensive behavior system

**Source**: Fanselow MS, Hoffman AN, Zhuravka I (2019). *Behavioural Processes* 166:103890. [DOI 10.1016/j.beproc.2019.103890](https://doi.org/10.1016/j.beproc.2019.103890). PMID 31254627, PMC7108871.

## What the paper did

Of everything in this pull, this paper asks the transition-trigger question most directly: what makes the defensive behavior system move from one PIC mode to another? The authors borrowed a logic from appetitive behavior-systems theory (Timberlake's feeding system), where shorter CS-US intervals push behavior toward more terminal, consummatory modes. If defense mirrors that structure, a short CS should provoke circa-strike-like activity-burst responses and a long CS should provoke post-encounter-like freezing. They tested this directly in rats with 10-second versus 3-minute CS durations, and separately tested what happens when a shock is delivered while an animal is already freezing.

## Key findings relevant to the claim

The central prediction failed: both CS durations produced freezing, not the predicted split, and freezing was if anything GREATER for the short CS -- the opposite direction from the appetitive-system analogy. The authors' explanation is an asymmetry argument: appetitive systems are selected to move toward the terminal (consummatory) mode as urgency increases, because more resource sooner is better; the defensive system, by contrast, is selected to stay AWAY from its terminal mode (circa-strike, which implies the predator has essentially made contact) unless forced there, because entering it prematurely is far more costly than a missed meal. Separately, and more usefully for REE's purposes, they found that a SUDDEN CHANGE in stimulation state -- shock delivered mid-freezing -- reliably and immediately triggers a transition to circa-strike/activity-burst behavior, regardless of the ongoing CS timing.

## How this translates to REE

Two results are directly load-bearing for the SD-hazard-aware-policy-decomposition design question. First, the disconfirmed hypothesis is itself a useful caution: a naive assumption that "more harm signal always pushes selection toward the most drastic response" is not simply how the biological system works — the defensive system has its own asymmetric logic that resists moving toward its most extreme mode. A REE selection rule should not treat "more z_harm_a -> ever more aggressive re-tiling" as an unconditional monotonic rule. Second, and more actionable: what most reliably triggers an immediate categorical transition in this data is a CHANGE in threat state on top of an ongoing one, not the absolute level alone. This maps strikingly onto REE's own architecture — MECH-321's own trigger, MECH-288, is already a predictive-surprise/change-point detector (fast-scale PE z-score, slow-scale BOCPD) over z_world/z_self/z_goal, but per the source autopsy it has zero contact with z_harm_a. This paper is a concrete argument that the eventual harm-valence gate should likewise be sensitive to a CHANGE or surprise in z_harm_a, not only its instantaneous absolute value — i.e. the same kind of surprise-detection logic MECH-288 already applies elsewhere in the pipeline, applied to the harm channel.

## Limitations and caveats

This is a classical Pavlovian fear-conditioning paradigm manipulating CS-US timing, not a direct spatial or temporal predator-imminence manipulation — the mapping to REE's harm-valence-weighted tile selection is structural (what triggers a categorical transition), not a quantitative timing calibration REE could import directly. The paper's headline hypothesis was disconfirmed, which makes it more honest evidence but also less simply "supportive" of any single clean functional form; it is coded `mixed` for that reason.

## Confidence reasoning

Well-controlled primary study from the lab that originated PIC, addressing the transition-trigger question more directly than any other entry in this pull. Confidence held to 0.68: source quality is good, but the central prediction failing and the one-step-removed paradigm (conditioning timing rather than direct imminence) both add real transfer risk to reading this as clean support for a specific REE functional form.
