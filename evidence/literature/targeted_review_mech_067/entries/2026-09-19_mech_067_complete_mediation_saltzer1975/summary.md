# Complete mediation and fail-safe defaults (Saltzer & Schroeder, Proc. IEEE 1975)

## What this entry is for

Provenance, mostly -- and a caution.

MECH-067 is registered as a `mechanism_hypothesis`: "a machine-checkable phase/store/actor
permission matrix is required to enforce commit-boundary write rules." Read the claim's two
operative properties -- *machine-checkable* and *default-deny* -- and they are, almost word for
word, two of the eight design principles Saltzer and Schroeder set out fifty years ago:

**Complete mediation.** Every access to every object must be checked for authority, and the
design must supply no mechanism for bypassing the check. This is the principle MECH-067 invokes
when it says the current per-site gates are insufficient. A check that a caller may or may not
route through is not complete mediation by definition, because the *design* supplies the bypass.
`ResidueField.accumulate` refusing hypothesis-tagged content protects residue against callers who
go through `accumulate`. It says nothing at all about a caller who does not.

**Fail-safe defaults.** Base access decisions on permission rather than exclusion: the default
should be lack of access, and the protection scheme should identify conditions under which access
is *permitted*. This is exactly the "default-deny" in MECH-067's matrix, and the argument for it
is asymmetry of error. An allow-list that is incomplete refuses something it should have allowed
-- annoying, and immediately visible, because someone complains. A deny-list that is incomplete
permits something it should have refused -- invisible, because nothing complains. MECH-060's
update-locus table is currently documentation, which means it behaves as neither; there is no list
at all, only the convention that authors will consult it.

So the first thing this entry records is that **MECH-067 is a re-derivation, not a discovery**.
That is not a criticism -- arriving independently at complete mediation while reasoning about an
agent's internal write loci is a point in the reasoning's favour -- but the claims registry should
say so, and a governance cycle deciding what confidence to assign should know that the mechanism
being proposed has a fifty-year literature and is uncontroversial as *design guidance*.

## The caution, which is the more important half

A normative principle is not evidence, and there is a specific way this citation could do damage.

MECH-067's own SUBSTRATE note is disciplined about this: "the audit is the spike that decides
whether the build is owed. Do not invent a matrix DV in the meantime." The temptation Saltzer and
Schroeder create is to skip that. Cite the canon, observe that complete mediation is obviously
correct, and treat the matrix as obligatory without anyone having measured whether REE's local
gates actually leak. That would be confirmation by authority, and it would convert a
`complex (probe-gated)` node into a `complicated (buildable)` one by assertion rather than by
finding anything out.

The empirical content of MECH-067 is not "is default-deny a sound principle" -- it is "does
`ree_core`, as it stands, contain at least one write that violates the MECH-060 update-locus
table, and does that violation measurably corrupt attribution." This paper cannot answer that. No
1975 paper can. The V1 EXQ-005 result (2026-02-27) is likewise evidence for the write-locus
*distinction* being real, not for the matrix being *required*.

It is worth adding that the same paper supplies two principles pointing the other way, and
intellectual honesty requires putting them next to the two above. **Economy of mechanism**: keep
the design as small and simple as possible, because only a small mechanism can be verified.
**Psychological acceptability**: a mechanism that imposes friction on routine work gets bypassed
or disabled, so a correct-but-costly gate is not durably a gate. A default-deny (phase, store,
actor) table with six typed store classes, maintained by hand alongside a substrate under active
experimental development, is neither small nor frictionless. If the audit comes back empty, those
two principles are the argument for MECH-067's own FALSIFYING disposition -- demote to
implementation guidance and let INV-024 carry the invariant. Saltzer and Schroeder are not
unambiguously on the claim's side; they are on the side of whichever answer the audit returns.

## Limitations

No measurements, no system, no evaluation. The principles were derived for adversarial,
multi-user, Multics-era OS protection, where the threat model is a person trying to read your
file. REE's threat model is inattention -- a rollout that writes to residue because the path was
never considered. Complete mediation's cost is easy to justify against an adversary and much
harder to justify against oneself, and that difference is not rhetorical: it is why most
single-process research code does not have a reference monitor, and is mostly fine.

## Confidence

0.5, direction `supports`. The component scores are high (source_quality 0.85, mapping_fidelity
0.8) and the aggregate deliberately sits well below their mean, because for a claim whose operative
word is *required* -- an empirical assertion about this substrate -- a normative source can supply
framing and vocabulary and nothing else. I would cite this in the claim's `location` doc as the
intellectual provenance of the matrix design. I would not let it move the claim's status by a
single step in the absence of the audit.
