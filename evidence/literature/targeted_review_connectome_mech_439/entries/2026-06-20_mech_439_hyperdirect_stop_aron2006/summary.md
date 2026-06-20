# Aron & Poldrack (2006) — Cortical and subcortical contributions to Stop-signal response inhibition: role of the STN

**Source:** Aron, A.R., Poldrack, R.A. (2006). *Journal of Neuroscience* 26(9):2424-2433. [DOI 10.1523/JNEUROSCI.4682-05.2006](https://doi.org/10.1523/JNEUROSCI.4682-05.2006) · PMID 16510720. (According to PubMed.)

**Claim under test:** MECH-439 — specifically the hyperdirect "hold" / global-NoGo primitive named in its scope (the Aron & Poldrack seed line).

## What the paper did

This is the foundational human-imaging localisation of the STN to response inhibition. In two fMRI experiments using a Stop-signal task, subjects responded to Go signals and tried to cancel the initiated response on occasional Stop signals. *Going* activated the frontal-striatal-pallidal-motor "direct" pathway; *Stopping* activated the right inferior frontal cortex (IFC) and the STN. Critically, Stop-related activation in both IFC and STN was *greater for fast inhibitors than slow ones* and correlated across subjects, and a high-resolution second experiment confirmed the activation sat within the STN. The authors proposed that the STN suppresses thalamocortical output to block response execution, possibly through a direct IFC→STN projection — for which they coined the term **"hyperdirect" pathway**. This is the paper that put the hyperdirect-hold idea on the map.

## Why it grounds the primitive

MECH-439's scope explicitly invokes the hyperdirect "hold" / global-NoGo as the primitive its fix deploys. Aron & Poldrack is the canonical localisation: the STN can rapidly raise the bar on committing a response, anatomically via the hyperdirect pathway, and the strength of that brake tracks how effectively a response is withheld. In REE terms this grounds the *existence and hardware* of a fast cortico-STN hold over committed selection — the structural ingredient the cluster autopsy found absent from REE's pure-argmax E3 selector. So the proposed lever is invoking a real, well-localised neural primitive rather than a metaphor.

## The load-bearing divergence (treated as load-bearing)

This entry is **mixed**, and the reason is exactly the kind of distinction the biology-first discipline exists to surface. The Aron-Poldrack hyperdirect signal is a **global, non-selective brake** — it cancels *all* pending responses (a reactive stop). That is the *opposite* of what REE needs: MECH-439 wants to *widen* the committed-action distribution, and a naive port of the global-NoGo to E3 would simply *freeze* the committed action — suppress everything — producing less behaviour, not more diverse behaviour. The raw global stop is therefore the **wrong functional mode** for a diversity-generating lever.

What rescues the mapping is that the *same STN / hyperdirect hardware* supports two functionally distinct modes: a fast all-or-none reactive stop (Aron & Poldrack) and a slower, *graded* conflict-dependent threshold (Frank 2006, Cavanagh 2011). MECH-439's `k=f(F-gap)` is the *graded* deployment — k scales with the conflict (the F-gap) — and so aligns with the Frank/Cavanagh lineage, not with Aron's global stop. The honest reading is that Aron & Poldrack establishes the primitive's existence and anatomy but warns that its canonical *form* (global NoGo) would suppress diversity if imported directly; the graded form REE actually uses is a refinement evidenced by the other two entries. There is also a transfer gap: this is *reactive stopping* against an external stop signal, not value/conflict-graded selection among competing GO options, so the functional bridge to E3 committed selection is indirect.

## Confidence

I assign **mixed, confidence 0.58**. Source quality is high — foundational, heavily cited, coined the hyperdirect-stopping hypothesis, with 7T-localised STN. Mapping fidelity is moderate-to-low: it grounds the hold *primitive* and its anatomy, but the function it characterises (a global non-selective brake) is the wrong mode for a graded diversity lever, and the graded use must be borrowed from the Frank/Cavanagh lineage. Transfer risk is elevated: a reactive-stopping paradigm rather than conflict-graded GO-selection makes the functional transfer to E3 indirect. The value of the entry is precisely that it forces the distinction — REE must use the hyperdirect hold in its *graded* (Frank/Cavanagh) mode, and a build that accidentally implemented the *global* (Aron) mode would reduce committed-action diversity rather than increase it.
