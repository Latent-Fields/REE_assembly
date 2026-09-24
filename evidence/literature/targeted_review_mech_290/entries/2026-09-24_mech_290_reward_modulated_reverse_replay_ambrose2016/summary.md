# Ambrose, Pfeiffer & Foster 2016, "Reverse Replay ... Uniquely Modulated by Changing Reward" -- MECH-290

## What the paper did

Ambrose, Pfeiffer & Foster (Foster's own lab, the same group behind the foundational Foster &
Wilson 2006 reverse-replay finding already tagged to ARC-028) recorded hippocampal place-cell
ensembles in rats running a W-track spatial alternation task while experimenters manipulated
reward magnitude at the reward wells. They isolated forward- and reverse-ordered sharp-wave-ripple
replay events and asked whether either class's rate tracked the change in reward.

## Findings relevant to MECH-290

Only reverse replay tracked reward: its rate increased when reward was increased and decreased
when reward was decreased, at the reward location, while forward replay was unaffected by either
manipulation. The authors explicitly frame this as evidence that reverse replay carries a
reward-linked function distinct from forward replay's role (canonically tied to planning/lookahead),
concluding "a unique relationship between reverse replay and reward processing."

## How this translates to REE

MECH-290's own claims.yaml text already cites Foster & Wilson 2006 as its "primary evidence,"
filed under targeted_review_connectome_arc_028 (confidence 0.72) -- but that entry supports only
that reverse replay EXISTS at reward endpoints, not that it functions as a reward/credit signal
specifically. This paper closes exactly that gap: it is the direct empirical demonstration that
reverse replay's RATE is reward-sensitive, which is the load-bearing premise MECH-290 needs before
it can claim reverse replay is the biological analog of a backward TD credit sweep (rather than,
say, a generic post-hoc memory consolidation mechanism that happens to run in reverse order).

## Limitations and caveats

The paper's dependent variable is event RATE / FREQUENCY as a function of a between-condition
change in reward magnitude -- not a within-event, discount-weighted UPDATE applied to each
preceding state's value estimate, which is what MECH-290's discount^(T-t) formula specifically
proposes. Showing reverse replay is reward-modulated is necessary support for treating it as a
credit-carrying signal, but it does not itself demonstrate the graded, per-step propagation
MECH-290's backward_credit_sweep() implements. No paper found in this search directly measures a
discounted, step-indexed value update during individual reverse-replay events (that would require
simultaneous value-cell recordings during the replay itself, which is a harder experiment than
rate-counting).

## Confidence reasoning

`source_quality` 0.85 (Neuron, direct single-unit electrophysiology, same lab lineage as the
existing ARC-028 evidence). `mapping_fidelity` 0.5 (strengthens the reward-linkage premise; does
not test the specific discounted per-step propagation). `transfer_risk` 0.45 (rodent spatial
navigation to an artificial multi-step trajectory-planning substrate). Aggregate confidence 0.55.

## Bearing on the novel_discovery question (searches run, and an important premise correction)

Queries run: "Ambrose Pfeiffer Foster 2016 reward modulated reverse replay hippocampus science";
this followed a read of MECH-290's own claims.yaml entry, which already names Foster & Wilson
2006 as grounding. **Correction to the chip's premise**: MECH-290 does NOT have "zero literature
ever pulled" in spirit -- the claim's own functional_restatement was written FROM biological
literature (Foster & Wilson 2006, filed under ARC-028) and cites a "well-replicated phenomenon
(Carr et al. 2011 review cites multiple replications)." What is true is that no entry's
`claim_ids_tested` has ever included "MECH-290" specifically -- the chip's zero-literature signal
is a claim_ids_tested artifact, not evidence the mechanism was invented independently of the
literature. Given that, MECH-290 does NOT survive as a novel-discovery candidate at all: it was
explicitly designed as an REE-side implementation of a named, cited biological finding, and this
entry (plus the pre-existing ARC-028 entry) is squarely confirmatory grounding, not a case of REE
experiments running ahead of a literature search. The open scientific question is narrower and
different in kind: whether the SPECIFIC discount-weighted per-step propagation mechanism is the
right computational reading of reverse replay, which remains untested in the literature searched
here and is a genuine implementation choice, not a discovery claim.
