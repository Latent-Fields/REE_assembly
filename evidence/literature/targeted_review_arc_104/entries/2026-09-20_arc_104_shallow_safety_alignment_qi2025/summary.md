# Safety Alignment Should Be Made More Than Just a Few Tokens Deep (Qi et al., ICLR 2025)

## What the paper did

Qi and colleagues offer a consolidating diagnosis: current LLM safety alignment is **shallow**. By
that they mean something specific and measurable -- the alignment adapts the model's generative
distribution primarily over only its very first few output tokens. The guard is, in effect, a thin
prefix behaviour. They present case studies showing why this shortcut arises and evidence that
current aligned models are subject to it, then demonstrate that this single issue explains four
separately-discovered vulnerability classes: adversarial suffix attacks, prefilling attacks,
decoding-parameter attacks, and fine-tuning attacks. Finally they show the remedy direction --
deepening alignment past the first few tokens improves robustness -- and design a regularized
fine-tuning objective that constrains updates on initial tokens, making alignment more persistent
against fine-tuning attacks. It was an Oral and an Outstanding Paper at ICLR 2025.

## Why this bears on ARC-104

ARC-104 is not a general claim about safety. It is specifically about the **language-mediated update
path** -- the point at which linguistic input revises the system's state. This paper is the best
available characterisation of what goes wrong at exactly that point, which makes it a closer fit to
the claim's scope than its subject matter first suggests.

The detail I keep returning to is that **benign fine-tuning is sufficient to jailbreak an aligned
model**. Not an attack. Ordinary updating. If the guard does not survive innocent revision, then
ARC-104 cannot be discharged by any amount of hostile-input filtering, because there is no hostile
input to filter -- the harm constraint simply fails to persist across the update. That is an
argument that the veto has to be *structural*: a property of how updates are permitted to move the
system, not a disposition carried inside the thing being updated.

There is a further, slightly rueful observation. The authors' own remedy -- a regularized objective
that constrains which parts of the model an update may move -- is a weak architectural analogue of
the veto ARC-104 specifies. They have arrived, from the empirical side and under a different
description, at "some part of this system must be protected from language-mediated revision." That
convergence is worth something, even though the mechanism is not the same.

## Limitations

The frame is **depth**, not **authority**, and these come apart. A guard could be made arbitrarily
deep -- covering every token of the output -- and still live entirely in the language-writable
substrate, and so still be defeasible by a sufficiently well-chosen update. Conversely ARC-104's
veto is not a claim about token depth at all. So this is corroboration that the update path is the
vulnerable surface; it is not evidence about the veto mechanism ARC-104 prescribes, and it should
not be cited as though it were. The generic caveat for this stream also applies: there is no
non-linguistic harm substrate anywhere in these systems.

## Confidence

0.73. Source quality 0.85 -- top venue, award-winning, and the consolidating explanation is
genuinely load-bearing rather than a restatement, since it subsumes four independently-reported
vulnerabilities under one mechanism. Mapping fidelity 0.72: good, but one step removed, for the
depth-versus-separation reason above. The benign-fine-tuning finding is what lifts mapping fidelity
above what a purely adversarial paper would earn, because ARC-104 guards ordinary language-mediated
updates and not only attacks. Transfer risk 0.35.
