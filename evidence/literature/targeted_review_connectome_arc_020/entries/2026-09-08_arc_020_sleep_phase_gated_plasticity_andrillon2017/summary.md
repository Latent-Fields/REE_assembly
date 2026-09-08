# Sleep-phase-gated plasticity as an existence proof for a gated offline write path

**Andrillon, Pressnitzer, Leger & Kouider (2017), _Nature Communications_ 8:179.**
Claim assessed: **ARC-020** -- "Offline consolidation is protected by typed authority/write boundaries."

## What the paper did

Sleeping human listeners were played samples of novel acoustic noise, and tested behaviourally on
waking for whether a trace of that specific noise had formed. The design's strength is that the
*same* stimulus was delivered across different sleep stages, so the manipulation is the brain's
ongoing regime rather than the material. The result is sharper than the usual "sleep helps memory"
finding: exposure during REM or light NREM produced improvement, and exposure during deep NREM
produced performance *worse* than baseline. EEG markers extracted during sleep tracked the
dissociation, and the authors traced facilitation to spindles and suppression to slow waves.

So the sleeping brain is not simply less available for learning. It is running something that
admits some plasticity and actively refuses -- indeed reverses -- other plasticity, moment to
moment, on identical input.

## Why this bears on ARC-020, and how far

ARC-020 commits to a specific architectural shape: offline consolidation may update
representational, residue and precision material freely, but a write that would affect a
privileged authority store (policy, identity, capabilities) must be intercepted and re-routed
through a typed commit boundary rather than landing directly. The claim's own
`what_would_answer` is candid that this is currently untestable in V3 -- an exhaustive grep for
`write_locus`, `permission_matrix`, `commit_token` and authority-store analogues returns nothing,
so there is no reachable code path for offline consolidation to violate *or* respect.

That means literature here cannot confirm the claim. What it can do is tell us whether the
architectural commitment is biologically idle or biologically motivated. On that narrower
question this paper is genuinely informative: it establishes that a live, dynamic gate on the
offline write path is a real feature of a real consolidating system, not an engineering
conceit imported from database transaction semantics.

## Where the mapping breaks, and it does break

The honest problem is the axis. Andrillon et al. demonstrate gating by sleep **phase**, applied to
a single content type. ARC-020 asserts gating by write **type**, within a phase. Those are
different claims, and the paper's finding is entirely compatible with ARC-020's own falsifier
(b): a boundary that exists but does not discriminate by type -- any offline-originated write
reaching the store regardless of whether it is representational or authority-affecting. Nothing
authority-like was ever presented to these sleepers; only novel noise, which on REE's own
taxonomy sits squarely in the "MAY update" list that ought to pass unimpeded.

There is a second, subtler mismatch worth recording. Deep-NREM exposure did not merely fail to
write -- it degraded performance below baseline. A boundary that damages the material it declines
is not the same object as one that re-routes it through a verifier. If anything, that detail
argues the biological mechanism here is closer to global synaptic downscaling than to a
permission check.

## Confidence

0.4, with mapping fidelity (0.35) doing most of the work in holding it there rather than source
quality (0.82), which is high. This is the calibration the lit-pull guidance asks for on
architectural claims: a methodologically excellent paper about an adjacent question should not be
allowed to launder into support for the question actually asked. Read this entry as: *a gated
offline write path is a real thing that real brains have*, and no further. Whether that gate is
typed in ARC-020's sense is untouched by this evidence, and cannot be settled by literature at
all until the V3 non-degeneracy precondition is met.
