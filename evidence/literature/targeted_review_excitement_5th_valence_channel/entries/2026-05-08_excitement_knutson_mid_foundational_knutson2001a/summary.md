# Anticipation of increasing monetary reward selectively recruits nucleus accumbens (Knutson 2001a)

## What the paper did

Knutson, Adams, Fong & Hommer (2001) ran event-related fMRI on eight healthy adult volunteers during a monetary incentive delay (MID) task. Cues signalled a forthcoming reward (varied parametrically: $0.20, $1.00, $5.00) or punishment of equivalent magnitude, followed by a target the subject had to respond to within a brief window. The contrast of interest was anticipation (cue presented, response not yet made) versus baseline. The behavioural readout was self-reported happiness elicited by the cue.

## Key findings relevant to the SD-014 question

Two findings load-bear on whether VALENCE_EXCITEMENT belongs as a fifth channel. First, NAcc activation during reward anticipation scaled parametrically with reward magnitude and correlated with self-reported happiness — at the highest reward level ($5.00), the NAcc BOLD response was significantly correlated with individual differences in self-reported happiness elicited by the reward cue. The construct measured here is *anticipatory positive affect at the cue*, not directional wanting amplitude or consummatory hedonic response. Second, punishment anticipation did *not* recruit the NAcc — instead it activated medial caudate. So the NAcc anticipatory signature is not a general arousal-orientation response; it is selectively positive-valence-coded.

## How this maps to REE

REE currently has VALENCE_WANTING (the persistent z_goal attractor — directional motivation), VALENCE_LIKING (consummatory hedonic at goal receipt), and z_beta-modulated heartbeat rate (MECH-093 — sympathetic-arousal-analog). Knutson 2001a says these three together do not capture anticipatory positive affect. The NAcc signature is high-arousal-positive at the cue, with self-reported happiness as the construct anchor — that is a fourth thing, distinct from any of REE's existing affect channels.

The closest existing claim is MECH-216 (E1 predictive wanting / schema readout) which writes anticipatory wanting at predicted-reward locations. But MECH-216 is a wanting projection — the question is whether the *high-arousal positive affect* component (what humans report as excitement) needs its own channel. The 2001a evidence says: yes, this signature is neurally distinct from wanting and from arousal-in-general.

## Limitations and caveats

The original n=8 is small; replication has been extensive but the construct of "happiness at reward cues" is humans-only and depends on self-report. The translation to REE assumes the *function* of the NAcc anticipatory signal is what the residue field would carry as VALENCE_EXCITEMENT — that is plausible but not strictly proven. The MID task is a cleaner anticipatory paradigm than naturalistic foraging; whether the excitement signature in foraging-class REE environments is similarly distinct from wanting amplitude is testable, not established.

## Confidence reasoning

I rate this 0.85. The paper is foundational and has replicated extensively. The mapping fidelity is moderate-high: the construct (anticipatory positive affect coded selectively in NAcc) is exactly what VALENCE_EXCITEMENT would carry in REE. The transfer risk is moderate: humans-fMRI to RL-agent-residue is a real gap, but the architectural decision is whether to *represent* the construct, which the paper directly motivates rather than measures in REE's substrate.

Source: PubMed via PMID 11459880. [DOI](https://doi.org/10.1523/JNEUROSCI.21-16-j0002.2001).
