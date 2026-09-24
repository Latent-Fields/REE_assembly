# Collins & Frank 2014, "Opponent Actor Learning (OpAL)" -- MECH-464

## What the paper did

Collins & Frank extend the classical actor-critic architecture into a dual "opponent actor"
model of the striatum: a D1-dominated Go population (G) and a D2-dominated NoGo population (N)
that separately accumulate positive and negative evidence for each action via a nonlinear,
three-factor Hebbian update. Choice is a function of the difference between the two
populations' outputs, and both populations are gained multiplicatively by a dopamine-linked
parameter (beta_G, beta_N; later beta_G = beta(1+rho), beta_N = beta(1-rho) in the OpAL* extension).
The model is validated against a wide empirical net: optogenetic D1/D2 stimulation in mice
(Kravitz et al. 2012; Tai et al. 2012), pharmacological D2/A2A manipulation of effort costs, and
human Parkinson's medication behavioral data.

## Findings relevant to MECH-464

The paper's central computational claim is exactly the shape of MECH-464's: dopamine's effect on
the G/N split is not a uniform scalar on action value. Because G and N are gained
asymmetrically and have themselves specialized differently across the value range during
learning, the net preference between two options is not simply confidence-scaled by dopamine --
it can be reversed. Two passages state this outright. In the effort/T-maze simulations:
"Dopamine depletion reverses this preference, but only for the 4 versus 2 pellet case, without
impacting choice in the 4 versus 0 pellet case" -- i.e. the reversal is conditional on the
specific relative magnitudes involved, exactly the kind of pair-dependent effect MECH-464
predicts for accumulators that straddle a critical boundary. And directly, in the learning/choice
interaction simulations: "it is also possible to reverse the asymmetry in choice: when options are
learned with a bias toward N weights, a sufficiently large asymmetry in choice incentive toward G
weights can still result in relatively better [performance for the disfavored option]."

## How this translates to REE

MECH-464 asserts that REE's `_d1_d2_split` (ree-v3/ree_core/predictors/e3_selector.py) -- which
splits a signed loop accumulator into go = relu(-accum) and nogo = relu(+accum) and gains them
asymmetrically by d1_gain/d2_gain as functions of da -- is capable of reordering which candidate
wins, precisely because the two populations are gained differently about zero. OpAL is the
closest available prior-art analog: it is built on the same architectural idea (opponent
D1/D2 populations, asymmetric dopaminergic gain, non-uniform effect on relative preference) and
it explicitly demonstrates, in simulation and against real optogenetic/pharmacological data, that
this asymmetry reorders choice rather than merely rescaling confidence.

## Limitations and caveats -- why this is "supports" but not "prior statement of the claim"

The mechanisms are not the same at the level of implementation. OpAL's reversals emerge from
LEARNED G/N weight asymmetry (accumulated over a Hebbian update across trials) combined with
a performance-time multiplicative beta; REE's mechanism is a SINGLE-TICK piecewise transform
applied directly to whatever sign the accumulator happens to carry at that instant, with no
learning history in the split itself. OpAL's own framing of why asymmetric gain changes
behaviour is in terms of which reward regime is best discriminated (see the companion 2023 eLife
paper, "On the normative advantages of dopamine and striatal opponency for learning and choice"),
not in terms of a "straddle-zero" event for a specific candidate pair within one decision -- that
framing, and the associated non-vacuity gate (require a non-trivial straddle fraction before
scoring the effect as real rather than an artifact of an all-same-sign field), is MECH-464's own
sharpening and does not appear in OpAL in those terms.

## Confidence reasoning

`source_quality` 0.85 (canonical, heavily cross-validated computational model in a top venue).
`mapping_fidelity` 0.45 (the qualitative mechanism class is a clean match; the specific
formalization is not). `transfer_risk` 0.45 (rodent/human data to an artificial multi-agent
substrate, and a learned-weight mechanism generalized to a stateless-split mechanism). Aggregate
confidence 0.55, weighted toward mapping fidelity because this is an architectural/mechanism claim.

## Bearing on the novel_discovery question (searches run)

Queries run: "Collins Frank opponent actor learning OpAL D1 D2 asymmetric gain reorder action
selection"; "Moeller Bogacz striatal D1 D2 opponent gain modulation decision reordering
computational model"; direct WebFetch of the OpAL PDF and PubMed abstract; WebFetch of the eLife
2023 "normative advantages" OpAL* paper. Verdict: MECH-464 does NOT survive as a clean
novel-discovery candidate at the level of the general phenomenon -- "asymmetric opponent D1/D2
gain can reorder relative preference rather than merely rescale it" has been an explicit, tested
computational claim since Collins & Frank 2014 (and elaborated in the 2023 eLife OpAL*
discrimination-sharpening paper). What MECH-464 adds beyond that prior art is a sharper, more
specific and directly falsifiable formalization for REE's particular substrate (a straddle-zero
pair-reordering event with an explicit non-vacuity gate on the straddle fraction), which
V3-EXQ-1019 then tested and found supported. That specific formalization and its non-vacuity
discipline were not found stated anywhere in the searched literature -- this particular
sharpening, not the underlying mechanism class, is what is genuinely new here.
