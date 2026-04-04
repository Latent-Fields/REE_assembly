# Relative reward preference in primate orbitofrontal cortex

**Tremblay & Schultz (1999), Nature, DOI: 10.1038/19525**

## What the paper did

Tremblay and Schultz recorded from single neurons in the orbitofrontal cortex (OFC) of macaque monkeys performing a spatial delayed response task in which different food and liquid rewards were available. The key manipulation was to assess not whether neurons discriminated reward magnitudes in an absolute sense, but whether they tracked the animal's current relative preference -- as expressed by its free-choice behaviour -- rather than the physical properties of the stimuli themselves. Neural activity was measured across three phases: the response to reward-predicting stimuli, the expectation interval (delay), and receipt of reward.

## Key findings relevant to the claim

The key finding is that OFC neurons fire during the expectation period -- the delay between cue and reward -- not just at reward delivery. Neurons discriminate between available rewards, but the discrimination reflects the animal's relative preference ranking rather than caloric content or volume. When the monkey's preference shifted (after sating on one food), the neural discrimination shifted accordingly. This means OFC is not a lookup table of fixed reward magnitudes; it encodes a continuously updated motivational valuation that represents what the animal is currently working toward.

## Translation to REE (the mapping)

MECH-112 asserts that E3 requires a structured latent goal representation -- a positive attractor in z_world or z_goal sub-space -- that is distinct from harm avoidance and from a terminal hedonic signal. Tremblay and Schultz provide exactly the neural substrate for this requirement: a cortical region that maintains a forward-looking, preference-relative representation of what the agent is approaching, sustaining that signal across the expectation period rather than computing it only at reward contact. In REE terms, this corresponds to z_goal encoding the motivational pull toward a valued future state (wanting) rather than registering benefit_exposure at consummation (liking). The preference-relativity result is also architecturally important: z_goal in REE needs to be context-sensitive and continuously updated, not fixed. OFC's preference tracking across satiety states is the biological analog of z_goal updating as environmental and internal conditions change.

## Limitations and caveats

OFC sits within the limbic-affective prefrontal-ventral striatal loop that Rusu & Pennartz 2019 propose as the highest-level loop in the three-loop BG hierarchy -- not directly E3 or the hippocampal module. The translation to REE requires mapping OFC's goal-context function onto REE's z_goal latent, which involves an intermediate conceptual step. The task is a well-trained single-step delayed response with no subgoal sequencing, so the paper does not speak to MECH-112's requirement for subgoal representations at multiple trajectory steps. Transfer from macaque OFC to REE's goal representation is also limited by species and task context differences.

## Confidence reasoning

Source quality is very high (Nature, landmark Schultz lab study, rigorous primate single-unit methodology with preference tracking controls). Mapping fidelity is strong for the core claim -- the existence of a prospective, preference-relative neural representation -- but moderate for any claims about subgoal sequencing or multi-step trajectories. Transfer risk is low for the architectural principle and moderate for mechanistic specifics. Overall confidence: 0.82.
