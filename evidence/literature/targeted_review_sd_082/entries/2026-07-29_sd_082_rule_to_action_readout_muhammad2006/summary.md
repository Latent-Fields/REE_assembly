# Muhammad, Wallis & Miller 2006 — rules do reach action, but not in the order we assumed

**Claim:** SD-082 (`pfc.lateral_pfc.common_mode_invariant_trained_rule_to_action_readout`)
**Direction:** mixed · **Confidence:** 0.58
**DOI:** [10.1162/jocn.2006.18.6.974](https://doi.org/10.1162/jocn.2006.18.6.974) (retrieved via PubMed, PMID 16839304)

## What the paper did

Monkeys were trained on two abstract rules — "same" and "different" — and had to hold or release a
lever depending on whether two successively presented pictures matched, and on which rule was
currently in force. The interest is that the same perceptual input demands opposite responses under
opposite rules, so rule information and response information can be dissociated. Muhammad, Wallis
and Miller recorded single units across four interconnected areas: lateral prefrontal cortex,
premotor cortex, inferior temporal cortex and dorsal striatum.

Rule and response information turned up in PFC, premotor cortex and dorsal striatum, and barely at
all in inferior temporal cortex — which instead carried the perceptual identity of the pictures,
strongest and earliest there, then PFC, with weak or absent effects in premotor cortex and striatum.
A clean double dissociation: perceptual content flows one way through the network, rule-and-response
content another.

## Why it is in this pull

SD-082's architecture doc grounds itself on a specific biological assertion —
"corticostriatal rule-to-action mapping: a selected rule/context representation must gate a motor
bias for the selection to have behavioural consequence; selection without a trained read-out to
action is inert." This paper is the primate evidence for that assertion. Rule signals are not
sequestered inside a rule-representing prefrontal module; they are co-represented with response
signals in premotor cortex and in the striatum, in the structures that actually commit to actions.

That does a particular job for SD-082, and it is worth being precise about which job. It does not
tell us how to build the read-out. What it does is establish that V3-EXQ-822's result — a
differentiated rule pool (`on_rule_state_diff_mean` 0.644, `max_live` 16) whose propagation to the
action bias was exactly `0.0` — is a **genuine architectural defect** rather than a tolerable design
choice one could shrug at. A rule field whose content never reaches action selection is not
implementing the biology it is modelled on. This is the entry that justifies SD-082 *existing*.

## The finding that complicates SD-082, and why the direction is mixed

Rules and behavioural responses "were reflected most strongly and, on average, tended to be earlier
in the PMC followed by the PFC and then the STR."

Premotor cortex *led* prefrontal cortex. That is the reverse of the architecture SD-082 encodes,
which is strictly serial and prefrontal-first: `CandidateRuleField → rule_state →
LateralPFCAnalog.compute_bias → E3 per-candidate score_bias`. If the biology is closer to concurrent
rule/action coding, or premotor-led coding, then SD-082 may be right that a read-out is required and
wrong about where it sits.

The uncomfortable part is that this is not a defect V3-EXQ-822a can detect. 822a asks whether
propagation is non-vacuous (`on_prop_delta_mean >= 0.001` with an ON>OFF contrast). A read-out placed
at the wrong stage of a wrongly-serialised pipeline would pass that test perfectly well, because it
*is* propagating — just not in the arrangement the biology uses. So this is a question that survives
a 822a PASS, and it should be recorded as an open one rather than quietly closed by a green result.

I do want to hold this caveat at arm's length in one respect: cross-area latency orderings are
notoriously sensitive to analysis choices — spike-count windows, ROC thresholds, which cells enter
the population — and a 2006 single-lab study reporting that premotor leads prefrontal for *rule*
information is the kind of result that later work has argued about. The authors themselves hedge it
("on average, tended to be earlier"). I would not restructure SD-082 on the strength of it. I would
also not pretend it is not there.

## What this paper cannot tell us

Almost everything SD-082 actually changes. The measurements are area-wise information content and
relative latency; there is no population geometry and no model of how a downstream area reads an
upstream code. Raw versus centered input, hard clamp versus scaled tanh — all four are equally
consistent with these data. Citing this paper as support for SD-082's *mechanism*, as opposed to its
*necessity*, would be an overreach, and I want that written down because the temptation is real: it
is the paper whose subject matter looks closest to SD-082's subject line.

The paradigm is also at the wrong end of the relevant scale. Two rules, one binary hold-or-release
response — a candidate set of cardinality two, the smallest in which "subtract the across-candidate
mean" is even defined. SD-082's benefit is expected to grow with candidate-set size, and V3-EXQ-822
had 16 live rules. The many-similar-alternatives regime where the common-mode pathology actually
bites is nowhere in this experiment.

One last observation that cuts a different way. Rule coding was *negligible* in inferior temporal
cortex — the rule pathway is selective, not a broadcast. SD-082 adds a consumer of `rule_state`
without any stated gating on which downstream structures may read it. If REE has consumers that
should not see the rule signal, this paper is a reason to check that.

## Confidence reasoning

Source quality 0.82 — a well-executed four-area comparison from the Miller lab, established
paradigm, ROC-quantified. Discounted for the usual small-n primate structure and, specifically,
because a latency ordering is doing real work in the caveat above and latency orderings are fragile.

Mapping fidelity 0.45 — the paper grounds SD-082's necessity, not its content, and SD-082 is a claim
about content. Its two components are a centering operation and an output bound, and this paradigm
could not see either.

Transfer risk 0.50 — macaque physiology to a V3 lateral-PFC *analog* (a correspondence that is
architectural convention, not measured homology), and a two-rule binary-response task to a 16-rule
pool with per-candidate biases.

Aggregate 0.58, mixed. It substantiates that a behaviourally silent rule pool is a defect worth
fixing — the load SD-082's architecture doc asks it to carry — while leaving a standing question
about whether the serial prefrontal-first placement is right, which 822a is not designed to answer.
