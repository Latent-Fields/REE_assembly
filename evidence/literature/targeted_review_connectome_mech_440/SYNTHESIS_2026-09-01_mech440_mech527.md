# Targeted literature review: MECH-440 narrowing, widened to MECH-527

- **Date:** 2026-09-01
- **Session:** c1-lit-pull-mech440-20260901 (campaign item C1.7)
- **Chip:** chip-20260830-mech440-targeted-lit-pull
- **Commissioned by:** the user, at the Step 8 gate of confirmed autopsy `failure_autopsy_966-436g-951-959-822d-cluster_2026-08-30` (2026-08-30T15:41:56Z, user present)
- **Scope widened per:** `evidence/planning/thought_intake_2026-08-30_false_bottom_exploration_noise.md`, which asked that one pull serve both claims
- **Entries written:** 6 under `targeted_review_connectome_mech_440/entries/`, 3 under `targeted_review_connectome_mech_527/entries/`
- **Status:** RECOMMENDATIONS ONLY. No claim status or text was edited. `/governance` applies or rejects.

---

## 1. The question this review was asked

V3-EXQ-959 is described in its own autopsy as the best-instrumented run in that cycle. Its `weakens` on MECH-440 stands. Of the claim's three legs, (i) propagation is SUPPORTED by V3-EXQ-955; (ii) state-conditioning missed at 2/6 seeds against a pre-registered 4/6 bar; (iii) self-annealing missed at 1/6. The commissioned question was whether the literature supports MECH-440 as registered, or supports a narrower form -- and specifically whether state-conditioning and self-annealing are attested as ONE mechanism or are DISSOCIABLE, such that the claim was over-scoped when it was registered.

The answer is that they are dissociable, and the evidence for this is stronger and more varied than I expected going in.

## 2. What the literature says: three methods, one architecture

Three independent lines converge on the same picture -- the *injection* of variability and the *control of its magnitude* are separate, and the control signal arrives from outside the injecting mechanism.

- **Behavioural decomposition (rat).** Dhawale, Miyamoto, Smith & Olveczky (2019, *Current Biology*, PMID 31630947) fit millions of trials and conclude that "motor variability is regulated by two distinct processes". A fast process modulates variability as a function of recent trial outcomes, raising it when performance is poor. A slower process tunes the *gain* of the fast process, keyed to uncertainty in the reward landscape. Different timescales, different driving signals, and hierarchical rather than parallel: the slow one does not inject variability, it sets the gain of the thing that does.
- **Pharmacological dissociation (human).** Dubois, Habicht, Michely, Moran, Dolan & Hauser (2021, *eLife*, PMID 33393461) find value-free random exploration attenuated by propranolol but not amisulpride. The noradrenergic grounding MECH-440 rests on survives; what it grounds is a separable *component*, not a bundle.
- **Lesion dissociation (songbird).** Kao, Doupe & Brainard (2005, *Nature*, PMID 15703748): lesioning the anterior forebrain pathway's output nucleus abolishes the natural modulation of song variability while song survives. Variability magnitude is delivered by a lesionable channel, gated in real time -- the same channel that withdraws slowly across development, but via a different control signal acting on it.

Wilson, Geana, White, Ludvig & Cohen (2014, *JEP:General*, PMID 25347535) corroborate from human choice behaviour: random and directed exploration are separately estimable, and what scales random exploration is the horizon -- a control variable computed elsewhere and handed in.

## 3. The finding that decides it: MECH-440's own source does not support two of its three legs

This is the part I did not anticipate and consider the most consequential result of the review.

MECH-440 names NoisyNet (Fortunato et al., ICLR 2018, arXiv:1706.10295) as its external analog and inherits self-annealing and state-conditioning from it. The existing entry in this directory (`2026-06-29_mech_440_noisynet_fortunato2018`, filed `supports` at 0.85) records that the floor "self-anneals via a gradient-trained sigma" and is "state-conditioned by construction". Going back to the paper's own analysis section:

> "We observe that Sigma-bar of the last layer of the network decreases as the learning proceeds in all cases, whereas in the case of the penultimate layer this only happens for 2 games out of 5 (Pong and Beam rider) and in the remaining 3 games Sigma-bar in fact increases. This shows that in the case of NoisyNet-DQN the agent does not necessarily evolve towards a deterministic solution as one might have expected."

The authors add that sigma's evolution "significantly differs from one game to another and in some cases from one seed to another seed", and describe the result as a *problem-specific* exploration strategy. There is no per-state analysis of sigma anywhere in the paper.

So: leg (iii) was measured by the source and reported unreliable. Leg (ii) was not measured by the source at all -- "problem-specific" is not "state-specific". Corroborating this, Aravindan & Lee (2021, arXiv:2102.03719) propose SANE explicitly to improve on NoisyNets "by allowing a non-uniform perturbation, where the amount of parameter perturbation is conditioned on the state of the agent", via a separate auxiliary module. State-conditioned perturbation *magnitude* is a thing one adds to NoisyNet, not a thing NoisyNet has.

This changes the evidential status of V3-EXQ-959's negative. It is not an isolated experimental miss against a well-supported claim. It is an experiment failing to find two properties that the claim's own cited source never established.

## 4. RECOMMENDATION 1 -- MECH-440: NARROW to leg (i), and re-register the rest

**MECH-440 should be narrowed to the injection-site / propagation claim (leg i) and nothing more.** That leg is genuinely what NoisyNet demonstrates, is what the V3-EXQ-687 non-propagation failure required, and is what V3-EXQ-955 confirmed on the single load-bearing criterion C1. Everything the claim asserts beyond it -- that the same learned per-parameter sigma is thereby state-conditioned and self-annealing -- was inherited from a source that does not support it and has now failed a well-instrumented six-seed test.

**The state-conditioning function should not simply be deleted; it should be re-registered in the form the literature actually attests** -- an externally gated noise magnitude arriving at the selection head from a separable control pathway, rather than an emergent property of the noise parameters. Three methods (behavioural decomposition, pharmacology, lesion) agree on that architecture, and REE's own substrate already has the right injection locus; what it lacks is a control channel distinct from the injector. Whether that becomes a successor MECH claim or an amendment is `/governance`'s call, not mine. I would note only that deleting legs (ii)/(iii) without re-registering the function would discard a well-supported architectural finding along with a badly-scoped claim.

Two evidential-hygiene items follow from this section:

- The existing `2026-06-29_mech_440_noisynet_fortunato2018` entry's leg-(ii)/(iii) reading is **not sustained** by the source. I have not edited it; I wrote `2026-09-01_mech_440_noisynet_sigma_nonannealing_fortunato2018` alongside it so the correction is visible and the audit trail intact. Governance may wish to adjust the older entry's `evidence_direction` or confidence.
- Per the V3-EXQ-959 autopsy, there is **no manipulation-engagement gate on the ON arm**. Given that the source algorithm's sigma direction varies by seed, any future annealing test needs one. The sole C_ANNEAL-passing seed (43) was the least-annealed seed at 3.9% engagement.

## 5. RECOMMENDATION 2 -- MECH-527: formulation STANDS on its distinctive commitments; RENAME; and fix the nominated trigger substrate

**MECH-527's core formulation stands, and its central distinction from MECH-440 is vindicated rather than merely stipulated.** Two of its structural commitments have direct support. Above-action-level perturbation: Karlsson, Tervo & Karpova (2012, *Science*, PMID 23042898) report coordinated destabilisation across the majority of sampled mPFC neurons when "prior belief was abandoned in favor of exploration of alternative strategies" -- a population-level representation, not an action. Post-resolution decay: the same instability "diminishes over the period of exploration as new stable representations are formed". And the failure-not-uncertainty trigger has independent behavioural support from Dhawale's fast process (variability up when performance is poor) and from Neuringer, Kornell & Olufs (2001, PMID 11199517), where variability rises under continued non-reinforcement with no near-tie and no uncertainty manipulation.

**But three revisions are owed, and the third is the one I would not let through unamended.**

1. **RENAME / re-position.** Escalate-on-stagnation, collapse-on-improvement is Variable Neighborhood Search (Mladenovic & Hansen, 1997, DOI 10.1016/S0305-0548(97)00031-2), where it is the algorithm's definitional control rule. The claim should position itself as the hypothesis that a VNS-shaped control structure operates above the action level in a cognitive architecture, with network resets as its biological signature -- not as a new coinage. This makes the genuinely novel content explicit: the control structure is borrowed; the assertion that a brain-like architecture implements one is the claim.
2. **Soften "attractor escape" to "variability injection under stuckness", pending evidence.** Neuringer et al. found variability rising under persistent failure *while the rank ordering of responses was preserved* -- the dominant sequence stayed dominant and rare variants appeared beneath it. That is added variation around a preserved attractor, not escape from it. This is a caution rather than a refutation (extinction is cruder than a false bottom, and the response space was small), but the claim should not assume that raising variation relocates the policy. It is also exactly why the claim's own demand for a genuine false-bottom ecology is right.
3. **The nominated trigger substrate does not fit the trigger as stated.** MECH-527 nominates MECH-482's `epistemic_deficit` accumulator. Per MECH-482's implementation note, the landed SD-102 substrate (`ree-v3/ree_core/policy/epistemic_deficit.py`) is fed by three inputs: candidate-specific predictive **uncertainty**, **persistent realized prediction error**, and predictive-system **disagreement**. Only the middle one matches MECH-527's trigger. A settled, confident, persistently-failing attractor -- the claim's paradigm case -- has *low* predictive uncertainty and *low* inter-predictor disagreement, so two of the three inputs are suppressed exactly when the trigger should fire. Either MECH-527 must specify that it consumes the persistent-PE channel *only*, or MECH-482's uncertainty term must be shown to mean model-inadequacy-about-the-target rather than policy uncertainty. Note also that MECH-314c (learning-progress, substrate landed) is arguably a better-fitting stuckness detector -- near-zero learning progress despite continued high stakes is close to "confidence without resolution" -- and MECH-527 does not currently consider it. Resolving this is cheap and should happen before any falsifier is designed.

**Escalating breadth remains unsupported biologically.** Karlsson gives the decay; nothing in this pull gives graded escalation under continued failure. The only precedent is algorithmic, and under the biology-before-formal-definitions invariant that is not grounding. This should be recorded as a known gap in the claim rather than carried as an asserted property.

## 6. Incidental finding: GFLAG-0082 confirmed stale, and staler than the flag states

The chip asked me to check this while in the claim. **Confirmed stale.** MECH-440's `ceiling_routing_note` still instructs that a thrash-not-carve outcome should "route to ARC-110, NOT a deeper noise build". ARC-110's own validation resolved in the negative -- V3-EXQ-707b returned `weakens (NARROW)`, 707c likewise on a repaired instrument -- and later work found even learned cross-loop arbitration hits a loop-effective-weight ceiling. There is no ARC-110 clearance to wait for and no ARC-110 destination to route to.

**Beyond what GFLAG-0082 records:** the flag proposes the ARMED-CONVERSION precondition as the correct replacement hold. That is now *also* superseded -- V3-EXQ-955 and V3-EXQ-959 both ran met-and-measured, and `pending_retest_after_substrate` is already false. So the rewrite owed on MECH-440 is larger than the flag describes: the note needs the ARC-110 routing removed *and* the replacement hold stated as satisfied rather than pending. Flagged only; `claims.yaml` is `/governance`'s to edit.

## 7. Honest limits of this review

- Every identifier here was resolved against NCBI E-utilities, arXiv, or Crossref during this session. Author lists for PubMed sources are recorded in the exact form the record gives (initials, not expanded first names) after one first-name expansion in a draft record was caught and corrected.
- The strongest entries are animal and human studies whose measured quantities -- kinematic variance, fitted decision-noise parameters, population activity volatility -- are not REE's observables. Every mapping in this pull is functional/architectural, and each record's `mapping_caveat` states its own gap.
- One unresolved tension in the human developmental literature is worth recording rather than smoothing: Meder et al. (2021, PMID 33539647) report random exploration decreasing markedly with age, while Schulz et al. (2019, PMID 31652093) report no reliable developmental difference in random sampling. Both still support dissociability of directed from random exploration; they disagree on random exploration's own trajectory. Neither was written up as an entry.
- The VNS entry is a formal precedent, not evidence about any organism, and should not be read as raising confidence that the mechanism is real.
