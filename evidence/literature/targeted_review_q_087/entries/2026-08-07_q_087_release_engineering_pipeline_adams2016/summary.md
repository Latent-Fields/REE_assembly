# Modern release engineering (Adams & McIntosh, 2016) -- Q-087

**Direction: supports (with a genuine counter-current) -- confidence 0.50**

## What the paper is

An invited "Future of Software Engineering" overview at SANER 2016 that lays out what modern release engineering actually is: the pipeline from code-change integration and continuous integration, through build-system specification and infrastructure-as-code, to deployment and release. Its headline observation is that continuous-delivery practice now ships content to users "in days or hours rather than months or years," and that this compression has made the release pipeline a first-class engineering concern that researchers have under-studied.

## Why it bears on Q-087

Q-087 needed to decide what *event* constitutes V3 closure. One way to read the whole modern-release-engineering picture is that it dissolves the romantic idea of "release = the software is finished." In a continuous-delivery world a release is simply a **milestone the team decides to trigger** within a defined, instrumented process -- the artefact is never "complete," it is cut at a chosen point. That is the same anti-completeness intuition behind Q-087's resolution: V3 closure is "when a governance decision records it," not "when every closure node is green." The paper supports the general shape of the resolution -- closure/release is a decided milestone, not an emergent state.

## The honest counter-current

I have marked this *supports* but held confidence at 0.50 because the paper actually pulls in two directions on Q-087's specific axis. Q-087's live tension was between an **objective/automatic** gate (the strict green board) and a **human governance** gate (governance acceptance, chosen). Modern release engineering's whole thrust is toward *automated, tool-enforced* gates -- CI passing, build reproducible, deploy scripted -- i.e. it is the intellectual home of the objective-gate candidate that Q-087 *rejected*. So while the paper supports "closure is a decided milestone," it leans toward the rejected mechanism for deciding it. It is included precisely so this pull is on the record rather than hidden.

There is also a structural mismatch: the paper is about *recurring* product releases on a cadence, whereas V3 closure is a *singular* boundary that also has to double as a frozen causal reference (GOV-V3FREEZE-1's second rationale). The analogy from "we cut a release today" to "we declare a research substrate closed and frozen" is loose.

## Confidence reasoning

Source quality is good (peer-reviewed, well-known authors) but the paper is a broad overview, not a study of the release-decision event itself, so it can only frame the question. Mapping fidelity is moderate (0.5) and transfer risk moderate (0.5): deployed-product release cadence is an adjacent but distinct thing from a one-time governance freeze. The value of the entry is that it locates Q-087's choice inside a real practice literature -- and honestly flags that that literature's default preference is for the objective gate Q-087 declined.
