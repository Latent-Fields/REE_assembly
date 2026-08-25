# ARC-131 vs MECH-459 Duplication Audit

**Date:** 2026-08-25
**Session:** metaworker-chip-20260825-arc131-mech459-dup-audit
**Trigger:** ARC-131's own registration notes flag this as an open obligation -- "the raw
thought itself flags this distinction needs 'a duplication and literature audit' -- taken
seriously, not glossed over ... NEXT STEP (not done in this pass)." The Stage 2 intake doc
(`thought_intake_2026-08-24_causal_reach_installability_and_when_a_mechanism_becomes_part_of_the_organism.md`,
Section 6 item 4) repeats the same open item. This audit discharges it.

**Verdict: GENUINELY DISTINCT. ARC-131 stands as registered.** No fold, no withdrawal, no
narrowing recommended. Reasoning below; disposition left to a future `/governance` cycle
per the chip's own instructions (this session does not change ARC-131's status or
depends_on structure).

---

## 1. What each claim actually asserts

**ARC-131** (`architecture.installability_as_composition_competence`, claim_level:
architectural, status: candidate): a mechanism that passes component-level validation in
isolation can still fail to appear AT ALL once composed into the whole organism, because the
rest of the organism changes its operating conditions (input distribution, competing-signal
scale, timing, upstream representation availability, downstream commitment dynamics,
resource/mode occupancy, ecology). This is a claim about SIMULTANEOUS composition -- whether
the competence is ever expressed once the full stack is switched on -- independent of any
subsequent learning event.

**MECH-459** (`f_dominance_conversion_ceiling.return_pathway_stabilisation`, claim_level:
mechanistic, status: candidate/v3_pending): a SPECIFIC hypothesis that REE's actor-critic
stacks two two-sided normalisers (Welford running reward std + per-episode advantage
standardisation) into a scale-invariance operator that swamps small-magnitude bootstrap
gradients with re-amplified novelty noise. Read in full (claims.yaml lines 75804-76050+),
this is a narrow, heavily-adjudicated mechanistic claim about one normalisation pathway in
one training loop, NOT a general statement about retention-as-a-competence.

**The retention connection is via a 2026-08-01 fold-in, not MECH-459's own original
content.** MECH-459's `evidence_quality_note` records: "[2026-08-01 governance, MECH-476
WITHDRAWN, folded in here]: MECH-476's three pre-registered falsifier arms ... found
retention invariant to dose, interval, and novelty-pairing alike -- consistent with a
constant regulariser (this claim's return-scale-invariance / one-sided normalisation
mechanism ...), not a dedicated consolidation process." MECH-459 "is UNCHANGED by the
fold-in ... the withdrawal adds no new obligation here, only removes a claim that would have
duplicated it."

**MECH-476** (`f_dominance_conversion_ceiling.acquisition_retention_dissociation`,
claim_level: mechanistic, **status: retired**, live_status.reading: retired) was the actual
general-purpose retention claim: "ACQUIRING competence and RETAINING it are dissociable
capabilities with separate substrate requirements." Its own pre-registered falsifier
(A->B->A retrograde-interference design varying install dose and offline interval, Krakauer
2005) was run to completion (V3-EXQ-836a/d/e) and returned INVARIANT to dose, interval, and
novelty-pairing -- the claim's own stated withdrawal condition. It was withdrawn "back into
MECH-459/460 rather than kept as an umbrella" specifically BECAUSE there turned out to be no
dedicated consolidation PROCESS, only the pre-existing regulariser MECH-459 already
characterises.

**Consequence for this audit:** there is currently no LIVE general "retention is a
dissociable architectural competence" claim in the registry at ARC-131's own level of
abstraction. The one that existed (MECH-476) was retired precisely because its general form
did not survive its own falsifier. What remains under the "MECH-459" label is a narrow,
mechanism-specific finding. ARC-131's depends_on comment ("MECH-459 # competence retention
(post-2026-08-01 MECH-476 fold-in) -- explicitly DISTINGUISHED-FROM") is accurate in effect
but slightly overstates MECH-459's genericity; MECH-459 is the closest LIVE claim that
TOUCHES retention, not a general retention claim in its own right. This is a wording nuance,
not a duplication finding -- it does not change the verdict below, and is recorded here so a
future reader is not misled into treating MECH-459 as ARC-131's architectural-level peer.

---

## 2. Is the distinction real, or does it collapse under scrutiny?

**Within REE's own evidence trail, the two axes are already empirically separable, not just
conceptually asserted.** MECH-476's falsifier tested exactly the retention axis (does a
once-acquired competence survive subsequent interference, as a function of dose and offline
interval) and found invariance -- i.e., in REE's current substrate, "retention" reduces to a
constant regularisation effect rather than a dose/time-sensitive consolidation process. That
finding is about competences that HAVE ALREADY been acquired (via BC installation) and are
then subjected to further RL refinement -- it presupposes the competence was expressed in the
first place. ARC-131's installability axis is about a DIFFERENT failure point: a mechanism
that is built, and individually validated, but never becomes visible in the composed agent's
behaviour stream to begin with (coalition control's inert-until-called controller; a selector
silently equivalent to its own OFF arm under a permissive fallback). Neither of REE's own
concrete installability examples cited in the raw thought is a retention failure -- both are
"never expressed under composition" failures with no prior expression to have retained.
This is a structural, not merely rhetorical, separation: a mechanism can fail installability
(never appears) with the retention question not yet even applicable, or pass installability
and only later fail retention (works when first composed, decays under interference). These
are logically independent failure points, and REE's own registry already contains
instances of the SECOND without evidence of collapse into the first.

**In the cognitive-science literature, the closest analog to "installability" is the
classical learning-performance dissociation (Tolman & Honzik 1930; "latent learning"), not
consolidation/retention.** Tolman's rats acquired a cognitive map of a maze under
no-reward conditions -- the competence existed -- but did not EXPRESS it in behaviour
(taking the direct route) until a motivational condition (food reward) was introduced;
once introduced, performance matched the always-rewarded group within one to two trials.
This is precisely REE's installability shape: a competence exists but is drowned,
gated, or contextually unavailable, and its APPEARANCE depends on the composed system's
current state (drive, competing signals, ecology), not on any additional learning having
occurred. Consolidation research (Krakauer 2005, already MECH-476/459's own citation)
studies a different question -- whether an ALREADY-EXPRESSED competence survives subsequent
interference -- and is a separate, long-established sub-literature within memory research.
The two questions are not treated as the same construct in that literature: the
competence/performance distinction is about availability-at-composition-time; consolidation
is about durability-after-expression-over-time.

**In the machine-learning literature, the same split holds between modular/compositional
"component engagement" research and continual-learning "catastrophic forgetting"
research.** MECH-459's own literature basis (`evidence/literature/targeted_review_mech_459/`:
Wang et al. 2025 on harmful advantage normalisation, Hafner et al. 2023 DreamerV3 percentile
return normalisation, Sullivan et al. 2023 on transferring Dreamer tricks to PPO) is entirely
about RETURN-PATHWAY normalisation mechanics -- none of it is about whether a trained
component gets recruited/expressed when composed into a larger system. The nearest REE-side
analog to an installability-shaped ML phenomenon is not in MECH-459's citation set at all,
but adjacent to MECH-309 (`policy.monomodal_collapse_as_equilibrium_without_rule_apprehender`,
line 48062), whose notes reference "router/expert collapse" in mixture-of-experts systems --
a documented ML phenomenon where an individually-competent expert/component is never engaged
by the routing/gating mechanism once composed into the full system, addressed by a distinct
research thread (load-balancing losses, e.g. Shazeer et al. 2017) from catastrophic-forgetting
mitigation (EWC, Kirkpatrick et al. 2017, already cited in MECH-476's literature grounding).
These remain two separately-studied problems in the ML literature -- component
non-engagement/routing collapse in composed multi-module systems, vs. forgetting under
sequential training -- generally addressed by different techniques (load-balancing /
auxiliary routing losses vs. regularisation or replay), and combined only in a handful of
recent "modular continual learning" papers as an explicit ADDITIVE combination of two
distinct failure modes, not as evidence that they are the same failure mode.

**Conclusion on this question: the distinction does not collapse.** It is supported both by
REE's own within-registry evidence (MECH-476's retention falsifier and the raw thought's own
installability examples target non-overlapping failure shapes) and by two independent
external literatures (cognitive-science learning-performance dissociation vs. consolidation;
ML component-engagement/routing vs. catastrophic forgetting) that treat them as distinct,
separately-diagnosed phenomena.

---

## 3. Search for any other existing REE claim covering this distinction

Searched `claims.yaml` for "installab" (all 20 hits are ARC-131 itself, its own
cross-references, or the informal MECH-457/V3-EXQ-819 "competence FLOOR / installability
explanandum" phrase already wired as ARC-131's depends_on instance -- no independent prior
claim). Searched for "simultaneous composition" and "component-level" -- no hits outside
ARC-131. Searched for "expert collapse", "routing collapse", "module ... collapse", "latent
learning", "Tolman" -- one relevant hit (MECH-309's "router/expert collapse" note, discussed
above; not a duplicate, different subject: single-policy-mode collapse from an absent
rule-apprehension layer, not whole-organism composition failure of an already-built
mechanism). No other claim in the registry states or approximates ARC-131's general,
cross-mechanism property.

---

## 4. Verdict and recommendation

**GENUINELY DISTINCT -- ARC-131 stands as registered.** Do not fold or withdraw. The
installability/retention distinction survives both an internal (REE's own evidence) and an
external (cognitive-science + ML literature) check.

**Non-blocking suggestions for a future pass (not executed here, per the chip's scope --
flagging only):**
- ARC-131's `notes` could eventually cite the Tolman & Honzik (1930) learning-performance
  dissociation as external literature grounding for the installability axis specifically
  (currently ARC-131 has no literature citations at all -- `evidence: []` and no lit-pull
  has been run against it). A dedicated `/lit-pull` targeting ARC-131, as already recommended
  generally in the Stage 2 intake's Section 6.2, would be the right vehicle.
- ARC-131's `depends_on` comment for MECH-459 could be sharpened to note that MECH-459 is
  the closest LIVE claim touching retention, not a general retention claim in its own right
  (MECH-476, which was the general claim, is retired) -- a precision improvement, not a
  duplication fix.
- MECH-309 could optionally be added as a second cross-referenced REE instance of
  composition-time non-engagement (parallel to how MECH-457 is already wired as the
  installability explanandum's actor-critic instance), since its own notes already invoke
  the router/expert-collapse framing that is the nearest ML analog identified here.

These are left for `/governance` or a future thought-digestion/claim-synthesis pass, per
the chip's instruction not to change ARC-131's status, depends_on structure, or notes beyond
recording this audit's completion.
