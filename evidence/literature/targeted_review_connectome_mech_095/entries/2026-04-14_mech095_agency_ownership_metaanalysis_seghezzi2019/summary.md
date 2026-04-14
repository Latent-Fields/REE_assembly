# Seghezzi et al. (2019) -- Meta-analysis dissociating sense-of-agency from body-ownership: agency network is premotor, not TPJ

## What the paper did

Seghezzi and colleagues conducted a quantitative neuroimaging meta-analysis using activation likelihood estimation (ALE) to compare the neural correlates of two dissociable components of self-consciousness: body-ownership (as probed by rubber hand illusion and multisensory integration paradigms) and sense of agency (as probed by action-outcome contingency tasks, intentional binding, and motor control paradigms). The central question was whether these two constructs share neural substrates or rely on distinct networks -- and if distinct, what architecture each requires.

## Key findings relevant to MECH-095

The meta-analysis identified three separate clusters. A body-ownership-specific network included the left inferior parietal lobule (IPL) and left extra-striate body area. A sense-of-agency-specific network included the left supplementary motor area (SMA), left posterior insula, right postcentral gyrus, and right superior temporal lobe. A shared network was found in the left middle insula.

For MECH-095, the critical finding is that the sense-of-agency-specific network does NOT include the inferior parietal lobule / TPJ. The IPL is body-ownership-specific. The agency network is centered on premotor and sensorimotor cortex. The authors interpret the agency network as "specifically associated with premotor and sensory-motor areas, typically involved in generating motor predictions and in action monitoring" -- which is architecturally earlier than the TPJ.

## Translation to REE and the EXQ-121 failure

MECH-095 specifies the TPJ as the agency-detection comparator. This meta-analysis introduces a localization challenge. If the neural mechanism for detecting self-generated action is primarily in SMA and posterior insula rather than in the TPJ, then the REE AgencyComparator module may be positioned at the wrong architectural stage. A two-stage model emerges from combining this finding with Farrer and Frith (2002) and Farrer et al. (2003): an automatic comparator at SMA/posterior insula (motor prediction error, fast, premotor) and a deliberative attribution circuit at the TPJ (causal belief updating, slower, social-cognitive framing).

This could explain EXQ-121. If the AgencyComparator is implemented as a TPJ-equivalent operation -- comparing latent states after sensory integration -- it may be operating at the wrong stage. The actual comparison may need to happen at the motor command level (SMA-equivalent), before the state observation is fully integrated. An architecture where the comparator fires against the E2 forward model prediction before the observation is processed might succeed where the current post-hoc comparison fails.

That said, this interpretation requires caution. The Farrer et al. (2003) graded discrepancy study clearly involves inferior parietal cortex, not SMA, in proportion to the motor-visual mismatch. The apparent contradiction may be that SMA is the primary agency monitor for normal, fluent action, while the inferior parietal / TPJ is recruited specifically when agency is disrupted -- the mismatch-detection step that fires only when the forward model fails. If so, MECH-095 may be correct in scope but the comparator should be dormant under normal conditions and active only when a mismatch threshold is crossed.

## Limitations and caveats

Meta-analyses aggregate heterogeneous paradigms. The studies pooled under "sense of agency" range from intentional binding (temporal perception tasks) to motor control tasks to explicit agency judgments -- these may not all probe the same mechanism. The absence of IPL in the agency-specific cluster could reflect paradigm heterogeneity, particularly if most agency studies used relatively naturalistic motor tasks where mismatch was rare. Studies specifically designed to probe prediction-error-driven agency (like Farrer et al. 2003) might show different patterns when analysed separately.

The body-ownership / sense-of-agency distinction also does not map cleanly onto z_self / z_world in REE. Body-ownership is closer to the self-model (what is my body?), while sense of agency is the comparator question (did I cause this?). Both are relevant to MECH-095 but they probe different functional components.

## Confidence reasoning

Confidence is set at 0.72 as mixed evidence. The meta-analysis provides genuine constraints on where the agency comparator is implemented neurally, and the finding that agency-specific activation is premotor rather than parietal is a real challenge to the current MECH-095 localization. But the heterogeneity of the source studies and the clean dissociation from Farrer et al. (2003) suggest the picture is more nuanced -- both SMA (normal monitoring) and inferior parietal / TPJ (mismatch-detection) may contribute to the full comparator architecture MECH-095 requires. This entry is valuable precisely because it creates productive tension with the Farrer studies and opens the two-stage interpretation.
