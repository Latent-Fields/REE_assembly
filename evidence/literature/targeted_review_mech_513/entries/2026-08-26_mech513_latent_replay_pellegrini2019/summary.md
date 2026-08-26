# Pellegrini, Graffieti, Lomonaco & Maltoni (2019/2020) -- Latent Replay for Real-Time Continual Learning

**Claim tested:** MECH-513 (representation-version reindexing for episodic memory)
**Evidence direction:** supports | **Confidence:** 0.55

## What the paper did

This is a continual-learning paper about a very practical constraint: on a resource-limited
device (they eventually deploy it on a smartphone), you cannot afford to store raw input data for
rehearsal against catastrophic forgetting. Their fix, "latent replay," stores activation volumes
at an intermediate network layer instead of raw pixels. That is cheaper -- but it creates a new
problem the paper spends most of its effort solving: if the layers below that intermediate point
keep training, the network that originally produced those stored activations no longer matches
the network that will later consume them. The stored activations drift out of correspondence with
the current representation. Their solution is to slow learning in the layers below the replay
point to a near-freeze, while letting the layers above train at full speed, and they show this
holds up across nearly 400 highly non-uniform, real-time training batches on two video benchmarks
(CORe50 NICv2, OpenLORIS).

## Key findings relevant to the claim

The paper is, in effect, an empirical case study of exactly the failure MECH-513 exists to name:
a representational scheme changing out from under previously stored, indexed content. The raw
thought behind MECH-513 puts it directly -- "an episode organised under an earlier representational
system may no longer be correctly located or interpreted by the current one" -- and that is a
precise description of what happens to Pellegrini et al.'s stored latent activations if nothing
constrains the layers beneath them. This is not a hypothetical concern in their setting; it is the
central engineering problem the whole paper is built to solve, and they show the performance cost
of not solving it is real (across highly non-uniform incremental batches, a naive latent-replay
setup would otherwise degrade badly).

## How this maps to REE

MECH-513 generalises this from a CNN's replay buffer to REE's episodic memory: a bucket split or
merge, or ContextMemory's effective dimensionality crystallising differently as MECH-496
describes, is REE's version of "the layers below the replay point keep changing." Where MECH-513
diverges from this paper is the remedy. Pellegrini et al. solve drift by constraining it --
freezing the lower layers so the representation barely moves. MECH-513 explicitly does not take
that option: REE's design permits MECH-496's dimensionality change to actually happen, so freezing
is not on the table. Instead MECH-513 proposes an additive, versioned reindexing layer, so a
previously stored episode remains interpretable under both its original indexing and the new one,
with explicit provenance back to the change that produced the new version. This paper does not
test that alternative; what it does is make the underlying problem statement credible and show,
empirically, how costly it is to leave unmanaged -- which is exactly the motivating case MECH-513
needs literature for.

## Limitations and caveats

Two gaps are worth stating plainly. First, this paper validates the *problem* (representation
drift breaks previously stored content) and one particular *solution* (rate-limiting the
representation), but says nothing directly about MECH-513's chosen solution (additive versioned
reindexing with dual old/new interpretability) -- that remains a REE-specific engineering
hypothesis motivated by, not tested by, this work. Second, the substrate is different in kind:
Pellegrini et al.'s representation is a supervised CNN's intermediate feature layer under
image/video classification, continuously drifting via ordinary SGD; MECH-513's target is episodic
memory indexed by structures like ContextMemory slots or the E1 associative manifold (MECH-154),
and its change drivers (bucket split/merge, dimensionality crystallisation) are discrete
structural events rather than continuous gradient drift. The qualitative mechanism -- a
downstream consumer's indexing assumptions invalidated by upstream representational change --
transfers reasonably well; the specifics of how and when it happens do not.

## Confidence reasoning

Source quality is solid: a peer-reviewed, empirically validated continual-learning paper with a
real deployed system, not a purely theoretical proposal. Mapping fidelity is moderate rather than
high, reflecting that the paper strongly evidences MECH-513's problem statement but not its
specific proposed remedy. Transfer risk is moderate, given the domain gap between a CNN feature
buffer and REE's episodic-memory indexing substrate. Net confidence of 0.55 sits at the boundary
of "moderate support with caveats" -- enough to treat MECH-513's motivating problem as
well-grounded in existing continual-learning literature, not enough to treat the specific
reindexing mechanism as independently validated.
