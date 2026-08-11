# MECH-490 E3 Commitment-Gate Persistence -- Synthesis

> Created: 2026-08-11
> Scope: 4 entries addressing MECH-490's two open questions -- (1) is "execution
> fluency/persistence of an already-planned sequence" a real, formation-distinct
> sleep-sensitive phenomenon, and (2) is that phenomenon REM-linked or SWS-linked,
> which bears directly on whether MECH-204 (a REM-phase precision-recalibration
> mechanism) is the right substrate to eventually re-enable.
> Sibling pull that this synthesis deliberately does NOT duplicate:
> `targeted_review_connectome_mech_323/` and `targeted_review_connectome_mech_324/`
> (policy-chunking/chunk-FORMATION grounding for ARC-071, already cited directly
> in `ree_core/policy/policy_chunking.py`'s module docstring -- Albouy 2013, Yin &
> Knowlton 2006, Smith & Graybiel 2013, Graybiel 1998/2008, Sakai 2003, Sutton et
> al. 1999). `targeted_review_connectome_mech_204/` (1 entry, van der Helm 2011,
> REM-aminergic-withdrawal-as-recalibration architecture for a DIFFERENT variable
> -- affective reactivity, not motor persistence) is read alongside this pull for
> the MECH-204 cross-reference but is not re-pulled here.

## Verdicts

### 1. Formation vs. fluency: DISSOCIABLE, and fluency is real

Bottary et al. (2016) and Blischke & Malangré (2016) independently, in two
structurally different motor tasks (discrete pegboard keypresses vs. continuous
arm movement), show that "chunks form" and "chunks concatenate fluently into one
continuous run" are separable processes with separable time-courses. Both report
that sleep -- not equivalent waking retention -- specifically improves the speed
of the *slowest, between-chunk* transitions in an already-learned sequence,
i.e. execution becomes more continuous and less internally interrupted, without
new chunks being formed. Walker et al. (2002) is the older, coarser-grained
foundational precedent that first established the sleep-vs-wake asymmetry for
this general class of motor-sequence gain, though it cannot itself separate
formation from fluency.

**Implication for MECH-490:** the claim's central distinction -- E3's
commit-gate persistence (fewer per-tick re-decisions once a plan is committed)
as a mechanism DISTINCT from policy-chunking's macro-primitive FORMATION -- has
a real behavioural precedent in human motor learning. This does not confirm the
E3-specific mechanism (see caveats below), but it establishes that the target
phenomenon category ("post-sleep gain in already-planned-sequence fluency,
formation-independent") is not a false dichotomy invented for this claim; it is
an established, separately-measured category in the source literature.

### 2. REM vs. SWS: converges on NREM2/spindles, NOT REM

This is the most load-bearing finding for MECH-490's open question. Bottary et
al. (2016) directly ties concatenation gains to nREM2 sigma-band (spindle)
power in young adults, and the ABSENCE of concatenation gains in older adults
correlates with reduced nREM2 spindle activity with age -- a within-study
dissociation, not just an absence-of-REM-mention. Walker et al. (2002) is
independent, twenty-years-earlier, larger-effect corroboration at the coarser
whole-sequence level: overnight gain correlated significantly with stage-2 NREM
amount (r=0.72, p=0.008), with no significant relationship to REM amount. No
paper surfaced in this pull, or in the broader REM-specific search run
alongside it, reports a REM-specific driver for this class of effect.

**Implication for MECH-490's `depends_on` (MECH-204):** if a real
coherence-persistence effect exists in the Fishtank data, this literature says
the biologically closer substrate is an NREM2/spindle-linked consolidation
process, not the REM-phase precision-recalibration mechanism MECH-204
implements (and which is confirmed disabled in the Fishtank driver family
regardless). This does not mean MECH-204 is wrong for its OWN claim (affective
recalibration, a different target variable per the MECH-204 lit-pull already on
file) -- it means MECH-204 specifically is not the literature-predicted route
FOR THIS effect, and a currently-unmodeled SWS/spindle-linked mechanism would be
the closer biological analogue if one were built.

### 3. The commit-gate architecture itself is independently grounded (non-sleep)

Dendauw et al. (2024)'s gated cascade diffusion model establishes that a
variance/threshold-gated commitment architecture -- accumulate evidence, smooth
it, hold it gated until a threshold is crossed, then commit and execute without
further re-accumulation -- is an empirically supported feature of human
decision-to-action pipelines generally, validated against joint RT-EMG dynamics
across four independent decision domains. This is structurally close to
E3Selector's `commit_variance < effective_threshold` gate followed by
open-loop execution via `_committed_step_idx`.

**Implication for MECH-490:** this grounds the PLAUSIBILITY of the gate concept
itself as a real neurocomputational primitive, independent of whether sleep
modulates it. It is evidence for a precondition of the claim, not for the claim
(sleep changes gate persistence) directly -- marked `evidence_direction:
unknown` in its record rather than `supports` for exactly that reason. Do not
read it as sleep evidence.

## What this pull does NOT establish

- **No paper here directly measures a per-tick re-decision rate or a
  variance/precision gate variable** -- the closest available proxy (transition
  SPEED at chunk boundaries) is a behavioural correlate REE is inferring maps
  onto reduced re-scoring frequency, not a variable any cited paper measures
  directly. This is the single largest mapping-fidelity gap across all four
  entries.
- **No paper uses an online-replanned, environment-conditioned action sequence**
  -- all four use fixed, externally-specified, once-learned sequences (finger
  taps, pegboard order, single discrete choices), structurally simpler than a
  Fishtank agent continuously regenerating and periodically re-committing to a
  plan under changing hazard/resource layout.
- **No paper establishes what mediates the NREM2/spindle -> fluency link
  mechanistically** -- sigma-power correlation is documented; the causal
  chain from spindle activity to a specific synaptic or systems-level change
  that would correspond to "lower commit-variance" in REE's terms is not
  characterised in any of these sources and remains, per this pull, an open
  question rather than a settled biological mechanism to port in.

## lit_conf: 0.60 (hypothesis-generating support, not confirmatory)

Aggregate read across the four entries: MODERATE. Two independent lines of
human behavioural evidence (Bottary 2016, Blischke & Malangré 2016) converge on
a real, formation-distinct, sleep-sensitive fluency phenomenon; one foundational
paper (Walker 2002) and the Bottary entry converge independently on NREM2/spindle
rather than REM as the relevant stage; one computational paper (Dendauw 2024)
grounds the gate architecture's general plausibility without touching the
sleep question. No paper directly measures the specific commit-gate/re-scoring
variable MECH-490 proposes, and the online-replanning transfer risk from fixed
lab sequences to Fishtank's continuously regenerated plans applies to every
entry. This literature makes the REFINED hypothesis (13c) more plausible and
gives a concrete, testable stage-specificity prediction (NREM2/spindle, not REM)
that the forward plan's instrumentation step (13d item 2: log
`E3Selector._running_variance`/commit-gate engagement per matched window) could
be extended to test directly against sleep-stage composition if that data
becomes available -- but it does not confirm the mechanism, and should not be
read as doing so.

## Papers pulled in this review

| # | First author | Year | Venue | Verdict contribution |
|---|--------------|------|-------|----------------------|
| 1 | Bottary | 2016 | Learning & Memory | Formation/fluency dissociation + NREM2/spindle attribution (strongest, most direct) |
| 2 | Blischke & Malangré | 2016 | J Human Kinetics | Independent formation/fluency corroboration, different motor task |
| 3 | Walker et al. | 2002 | Neuron | Foundational NREM2-not-REM anchor (coarser grain) |
| 4 | Dendauw et al. | 2024 | Psychological Review | Commit-gate architecture plausibility (non-sleep) |

## Papers considered and not pulled

- Rickard et al. 2008 (partial non-replication of sleep benefit for
  probabilistic sequence learning) -- surfaced only as a caveat inside the
  Walker 2002 entry's `failure_signatures`, not pulled as its own entry; it
  qualifies generalisation rather than bearing directly on the
  formation/fluency or stage-specificity questions this pull targets.
- The Albouy/Yin & Knowlton/Smith & Graybiel/Graybiel/Sakai/Sutton chunk-
  FORMATION corpus already cited for ARC-071/MECH-323/324 -- deliberately not
  re-cited here per the task instruction; that corpus grounds formation, this
  pull grounds fluency, and the two should stay distinguishable in the evidence
  record rather than conflated.
