# Infants' metaphysics: the case of numerical identity (Xu & Carey 1996)

## What the paper did

Across five visual-habituation and manual-search experiments with 158 infants, Xu and Carey
asked how infants decide *numerical identity* — whether the object in front of them now is the
same one they saw a moment ago — and *individuation* — how many distinct objects there are. The
canonical design: an object emerges from behind a screen and returns; then a different-looking
object (say a duck where a ball had been) emerges and returns, but the two are never seen
together. An adult infers two objects, because one thing cannot be both a duck and a ball. The
screen is then lifted to reveal either one object or two, and looking time is read against the
infant's expectation.

The result: 10-month-olds did **not** use the property/kind difference (duck vs ball) to infer
two objects — they looked equivalently at the one-object and two-object outcomes. But they
**did** individuate when given **spatiotemporal** evidence — for example, an object disappearing
behind one screen while another simultaneously emerged from a second screen, which can only mean
two objects. Kind-based individuation appeared later, around 12 months. Xu and Carey framed this
as the *Object-first Hypothesis*: for the most general sortal, "bounded physical object,"
spatiotemporal properties — not features or category — provide the criteria of identity and
individuation, and they do so first in development.

## Why this is the load-bearing entry for the pull

The object-representation memo's section 2.2 names the central representational gap precisely:
"true object permanence needs token-instance tracking ('where is THAT particular object now'),
which is the central representational gap the memo flags (REE's live object identity is
TYPE-level via SD-049 tags)." Xu & Carey is the empirical backbone of that sentence. They show,
with the cleanest available developmental dissociation, that:

- **Token identity is carried by spatiotemporal continuity.** What makes the thing behind the
  screen *the same* thing is that it traces one connected path — Spelke's continuity principle,
  now operationalised as numerical identity.
- **Type/kind identity is a separate, later capacity.** Using "this is a duck and that is a
  ball, so there are two" does not come online until ~12 months. It is not the route by which
  young infants track objects through occlusion.

This matters for REE because REE has built the *later* route and lacks the *earlier* one. The
entire live identity lineage — SD-015 `z_resource`, SD-049's per-type tag and identity
classifier, SD-057's `IncentiveTokenBank` keyed by resource *type* — is property/kind-based.
That is exactly the individuation-by-property route Xu & Carey show is *not* what carries an
object through occlusion. REE's developmental order is inverted relative to the infant's: it has
a type identity but no spatiotemporal token tracker, and permanence rests on the token tracker.

That gives the spine a concrete design verdict. A permanence pillar built as a fourth per-object
store keyed on the existing *type* tag would reproduce REE's gap, not close it. The unit for
permanence has to be a spatiotemporally-tracked token — a "this particular object, here is its
trajectory, here is where it went when it disappeared" representation — which none of REE's three
current stores (anchor-keyed ghost bank, type-keyed incentive bank, dormant object-file) actually
provides. The first design fork the memo identifies (type vs token vs anchor as the unit) is
answered here by biology: token, established spatiotemporally.

## Limitations and caveats

The mapping is at the level of the representational *distinction*, not the algorithm — an infant
looking-time numerical-identity task is not a machine object-tracker, and I have not pretended
otherwise. Xu & Carey also do not claim property information is useless; only that it is not yet
recruited for individuation at 10 months. So REE's type identity is not *wrong* — it is a real,
useful, developmentally later layer. It simply does not substitute for token tracking, and that
is the point. I have marked the entry `mixed` precisely because it cuts both ways: it strongly
*supports* the token-permanence pillar as the right thing to build, and it *weakens* any
assumption that the existing type-level identity already delivers permanence.

## Confidence reasoning

Confidence 0.74. Source quality is high (0.82) — a heavily cited, multi-experiment, large-N
foundational paper that has structured the individuation literature for thirty years. Mapping
fidelity is high (0.80): this is the most direct possible grounding of the token-vs-type
distinction the pillar turns on. Transfer risk is moderate (0.35) — the developmental dissociation
is robust, but the bridge from infant looking-time to a machine token-tracker is conceptual. I
hold the aggregate at 0.74, weighting the unusually strong mapping against that bridge.
