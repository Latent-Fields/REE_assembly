# A timescale hierarchy exists — but it is not orthogonal to abstraction (Murray et al. 2014)

## What the paper did

Murray and colleagues pooled single-unit recordings from seven macaque cortical areas, collected across several laboratories, and asked a deliberately simple question: how fast does spiking activity in each area forget its own recent history? They estimated the decay constant of spike-count autocorrelation during pre-stimulus baseline periods and found a systematic ordering. Sensory areas (MT, V4) have short intrinsic timescales, of the order of tens of milliseconds; association and prefrontal areas (LIP, OFC, ACC, LPFC) have long ones, running to hundreds of milliseconds and beyond. The conclusion they draw is modest and well-hedged: intrinsic timescales reflect areal specialisation for task-relevant computations over multiple temporal ranges.

## Why this speaks to ARC-008

ARC-008 defines REE tokens over three coordinates, one of which is temporal depth — the effective horizon over which predictions are integrated and expected to remain coherent — and posits four canonical tau bands. The first thing this paper does is confirm that the underlying commitment is not arbitrary. Cortex really does organise itself by integration timescale, the ordering is systematic rather than noisy, and it is a property of areas rather than of tasks. That matters, because ARC-008's architectural invariant — that predictions, errors and confidence must not be mixed across tau bands without an explicit projection or aggregation operator — is only a meaningful constraint if distinct temporal strata exist to be mixed. Murray et al. supply exactly that precondition.

The second thing the paper does is less comfortable, and I think it is the more valuable finding for governance. ARC-008 opens by describing tau-depth and rho-depth as *orthogonal* coordinates. Murray et al. find the timescale gradient running along the anatomical hierarchy — which is also, by any reasonable reading, the abstraction hierarchy that REE calls rho-depth. Short timescales sit in the concrete, modality-bound, detail-rich areas; long timescales sit in the schema-like, invariant, value-adjacent ones. In cortex, tau and rho are not independent axes; they are close to two readings of the same gradient.

I do not think this falsifies ARC-008, and I have recorded the direction as mixed rather than weakens for that reason. A design may legitimately factor apart what biology happens to confound — separating them buys REE the ability to represent a deep abstraction at a short horizon, which cortex may simply never need. But the claim cannot have it both ways: it cannot appeal to the neuroscience of temporal hierarchy as support for the tau axis while ignoring that the same literature entangles that axis with the one next to it. If orthogonality is a design decision rather than a biological finding, the claim should say so explicitly, and should say what the decision buys.

## Limitations

Three caveats bound how much weight this entry should carry. First, an autocorrelation decay constant is an *integration window*, not a *prediction horizon*. ARC-008 defines tau as the horizon over which predictions remain coherent; Murray et al. measure how long activity remembers. These are related but not the same quantity, and the slippage between them is exactly the kind of thing that makes architectural claims feel better-evidenced than they are. Second, the reported hierarchy is a graded continuum across areas. ARC-008's four-band gamma/beta/theta/delta taxonomy imposes a discretisation the data do not supply — the bands may be a useful engineering fiction, but they are not read off this result. Third, this is macaque electrophysiology during cognitive tasks, mapped onto a control-plane primitive in an artificial agent; the structural argument transfers, the numbers do not.

A note for whoever picks this claim up next. ARC-008 currently carries a digestion note recording that the three-axis system it describes does not exist anywhere in ree-v3 — no tau bands, no rho strata, no eligibility matrix, with only a coarse binary proxy for phi. That is a substrate fact and this pull does not change it. What this entry adds is that if the tau/rho portion is ever built, the orthogonality assumption is the part most worth interrogating first, because it is the part the external literature least supports.

## Provenance

Retrieved via PubMed (PMID 25383900; open access at PMC4241138). DOI: https://doi.org/10.1038/nn.3862
