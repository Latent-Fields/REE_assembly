# CRIX: detecting missing-check bugs at scale (Lu, Pakki & Wu, USENIX Security 2019)

## What the paper did

CRIX is a static analyser that looks for *absent* security checks in OS kernels. The hard part
of that problem is epistemic rather than technical: to know that a check is missing you must
first know the variable needed one, and criticalness is a semantic property that no type system
records. CRIX's answer is cross-checking against peers. For a given variable it collects the
slices of code that use analogous values in analogous contexts, models the conditional
statements those peers impose, and infers from the majority behaviour what constraint this site
ought to have carried. Run over the whole Linux kernel in 64 minutes at a relative-frequency
threshold of 0.15, it extracted 308K security checks from 1,028K conditional statements and
reported 804 candidate sites. Manual adjudication -- three researchers, 36 man-hours -- confirmed
**278 new missing-check bugs**. The authors patched all of them; Linux maintainers **accepted
151**, confirming 99 within a week.

Three numbers from the evaluation matter more to REE than the headline. The mean latent period
between the patch that introduced a missing check and its detection was **1,675 days**, about
four years seven months, with 27 bugs latent over ten years and six over thirteen. Missing-check
bugs were the root cause of **59.5%** of the recent vulnerabilities the authors sampled -- the
dominant cause, not a tail. And in a codebase where the local idiom is not merely conventional
but explicitly mandated (Linux insists every alloc-like return be tested for NULL), CRIX still
found 39 call sites across `kzalloc`, `kmalloc`, `kcalloc` and `kmemdup` where the check was
simply not there.

## How this bears on MECH-067

MECH-067's own SUBSTRATE note is unusually clear about what would settle it: the audit is the
spike, and the matrix build is owed only if the audit finds violations. This paper is that spike
run in a different substrate, and its result is the one that makes the spike worth running.

The methodological transfer is closer than the domain gap suggests. CRIX infers what *should* be
checked by comparing sites that check against sites that do not. The REE analogue is already
sketched in the claim: a driver-side instrument wrapping `ResidueField.accumulate`,
`discharge_domain`, `BetaGate.elevate`/`release` and `AnchorSet` writes, plus hash-before/after
on `SleepLoopManager._run_cycle` parameter deltas, recording a (phase, store, actor) tuple per
write, with phase read from `SleepPhase` and actor from the call site. The peer-comparison step
is even simpler for REE than for Linux, because REE already *has* the majority behaviour written
down: MECH-060's update-locus table. Any observed tuple with no row in that table is the
candidate. CRIX's result says an instrument of this kind, pointed at a codebase with mandated
local gates, returns non-empty.

The latency figure is the part I find most directly applicable. Four years seven months is how
long a missing check survived in code that thousands of people read. The reason is structural,
not sociological: **an absent gate emits nothing**. It produces no exception, no log line, no
failing test -- only a write that lands somewhere it should not have, indistinguishable at the
call site from a write that was authorised. That is exactly why MECH-067 cannot be settled by
inspection, and exactly why REE's own gates each reading correctly is not evidence that the set
of them is complete.

## Limitations and where the mapping strains

The first strain is one I should not paper over: **this paper supports machine-checkable
auditing, not a machine-checkable matrix**. CRIX is a detector bolted on after the fact. Nowhere
do the authors propose replacing Linux's per-site check idiom with a central (subsystem, object,
caller) policy object -- that would be a far larger claim, and they do not make it. MECH-067
asserts the matrix. Reading this paper as support for the matrix specifically is an extrapolation
from "the leak exists and an audit finds it" to "a default-deny table is the right remedy," and
that second step is carried by Krohn et al. (the Flume entry in this directory), not by this one.

The second is scale. Linux is roughly twenty million lines with thousands of contributors;
`ree_core` is small and effectively single-authored. A leak rate measured on the former is a poor
prior for the latter. It is entirely consistent with this paper that an REE audit returns zero
violations -- which is MECH-067's own FALSIFYING condition, and would demote the claim to
implementation guidance. This paper raises the prior that the audit is worth running; it does not
predict its outcome.

The third is the audit instrument's own honesty about itself: a **65% false-positive rate**. 804
candidates yielded 278 confirmations, at 36 man-hours of adjudication. An REE write audit should
be budgeted the same way -- as a screen that produces a candidate list requiring judgement, not
as a verdict. A design that assumes the instrument's output can be read as violations would
misrepresent the evidence it generates.

## Confidence

0.72. Source quality is high and, unusually, externally validated: 151 accepted maintainer
patches is an adjudication by parties with no stake in the paper's thesis. Mapping fidelity is
moderate rather than high because of the audit-versus-matrix gap above -- the paper lands
squarely on the spike MECH-067 proposes and only obliquely on the artefact MECH-067 asserts.
Transfer risk is moderate: the scale mismatch means the measured rate does not carry across, only
the demonstration that the failure mode survives conscientious, mandated, heavily-reviewed local
gating. For a claim whose whole content is "local gates are not enough", that demonstration is
the relevant thing, but it is a prior, not a finding about REE.
