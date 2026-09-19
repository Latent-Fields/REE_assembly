# Flume: information flow control for standard OS abstractions (Krohn et al., SOSP 2007)

## What the paper did

Flume is a decentralized information flow control (DIFC) system that attaches secrecy and
integrity *labels* to operating-system processes and to standard OS objects -- pipes, sockets,
file descriptors -- and enforces the resulting flow policy at a single user-level reference
monitor. A confined process cannot make most system calls directly; an interposition layer
converts them into IPC to the monitor, which decides whether the flow is permitted and, if so,
performs the operation on the process's behalf. The policy is default-deny in the sense that
matters: a process carrying a secrecy tag cannot export data unless some trusted party holds
and exercises the corresponding declassification capability. The evaluation ports MoinMoin, a
91,000-line Python wiki, to this model.

The number worth reading twice is not the performance figure. It is the census of the thing
Flume replaced. Moin's access-control policy was implemented as call sites: read ACLs checked
in **41 places across 22 different modules**, write ACLs in **19 places across 12 different
modules**. The authors' own comment is the whole argument in a sentence -- "the danger is that
an ACL check could have easily been omitted" -- and the public vulnerability database plus
Moin's own bug tracker record at least five ACL-bypass vulnerabilities that are exactly that.
Plug-ins compounded it: extension code loaded into the host process inherited the host's
authority and could violate the host's own ACL policy, because the policy lived in host code
rather than in the store. The Flume port required ~1,000 lines of new trusted C++ (`wikilaunch`)
and modification of ~1,000 of Moin's 91,000 Python lines, at 30-40% throughput cost, and
shrank the code you must audit to understand the security policy from 349 modules to one small
program.

## How this bears on MECH-067

MECH-067 asserts that a machine-checkable (phase, store, actor) default-deny matrix is
*required* -- not merely tidy -- to enforce REE's commit-boundary write rules. The interesting
question is what could possibly count as evidence for a "required", given that the local gates
currently in `ree_core` each look correct when read on their own. Flume answers that question
in a different substrate but with the same shape of argument: it exhibits a system whose
per-site gates were each individually correct, counts them, and shows that the *collection*
leaked five times anyway.

The structural correspondence is close enough to be uncomfortable. REE's present position is
Moin's: `ResidueField.accumulate` refuses hypothesis-tagged content (MECH-094), the sleep pass
contracts to write only its named module, the closure operator attenuates within bounds. Each
is a call site. None of them is a statement about the *store*. Add a new write path that
reaches residue without going through `accumulate`, and nothing in the architecture notices --
which is precisely the class of violation MECH-067's audit spike is designed to look for.
Flume's move is to relocate authority from "did the caller remember to check?" to "does this
actor's label permit a flow into this store?", which is what turning MECH-060's update-locus
table from documentation into a machine-checkable matrix would mean.

## Limitations and where the mapping strains

Three, and I do not think any of them is fatal, but the third is the one that should temper the
confidence.

First, **Flume assumes an adversary**. Malicious plug-ins, remote exploits, an attacker who
*wants* the leak. REE's leak is accidental -- a rollout that reaches residue because nobody
thought about that path. Complete mediation is easy to justify when someone is attacking you;
its cost-benefit is genuinely different when the only threat is your own inattention. This is a
real weakening of the transfer, not a formality.

Second, **Flume has a chokepoint and REE may not**. The system call is a narrow waist through
which essentially all OS-object access must pass, which is why interposition is even possible.
`ree_core`'s stores are tensors and Python attributes with no comparable waist; the matrix might
have to be enforced by convention plus an audit rather than by mediation, which is a weaker
guarantee. Flume's own residual hole makes the point from the inside: once it authorises a file
open it does *not* interpose on the subsequent reads and writes, so the policy is only as tight
as the granularity at which the monitor sits. A REE matrix enforced at the granularity of
"module" rather than "write" would inherit the same gap.

Third, and most honestly: **this paper does not test MECH-067's falsifier**. It shows that
centralising mediation helped one application. It does not show what an audit of Moin's 60 call
sites would have found had anyone run one -- which is exactly the question REE's audit spike
asks, and exactly the question that decides whether the matrix is *required* or merely *nicer*.
Flume is strong evidence that the failure mode MECH-067 names is real and recurrent in systems
of this shape. It is not evidence that REE's particular local gates are currently leaking. Only
the instrumented audit can say that, and this paper is a reason to run it, not a substitute for
running it.

## Confidence

0.78. High source quality (SOSP, working artefact, counted rather than asserted) and high
mapping fidelity -- the "scattered enforcement sites in a modular codebase" structure is not an
analogy I had to work for, it is the same structure. Held below 0.8 by the adversary assumption
and the missing chokepoint, and by the fact that for a claim whose operative word is *required*,
a successful centralisation is only half the demonstration; the other half is the negative
result that local gates were insufficient, which this paper gestures at through five CVEs rather
than establishes systematically.
