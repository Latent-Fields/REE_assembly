# Permissions on the Loose: overprivilege in real serverless deployments (Yeboah-Duako & Datta, arXiv 2026)

## Why this entry is here

Every other entry in this directory argues *for* MECH-067. This one is the counterweight, and it
is the entry I would read first if I were deciding whether to fund the matrix build.

MECH-067 says a machine-checkable (phase, store, actor) default-deny permission matrix is
*required* to enforce commit-boundary write rules. AWS IAM is that artefact, deployed at planetary
scale: a declarative, machine-checkable, default-deny policy language over (principal, action,
resource) -- structurally REE's (actor, write, store), missing only the phase dimension. If
having the matrix were enough to get write-locus discipline, IAM deployments would exhibit least
privilege.

They do not.

## What the paper measured

The authors built PrivLess, a static analysis that reads a serverless application's source,
derives which cloud resources each function actually touches, maps those interactions to the
permissions they require, and reconciles that inferred requirement against the policy the
application actually declares. Applied to a curated dataset of **789 AWS Lambda applications
comprising 1,293 functions** (drawn from 3,363 candidates), the results are:

- **47.7%** of applications carry excess permissions, with a mean **privilege-reduction potential
  of 99.65%** -- that is, almost all of what was granted was never needed.
- Applications with **wildcard** permissions show an average overprivilege ratio **274x** higher
  than those without (99.02% reduction potential with wildcards, 61.78% without). One coarse row
  defeats the default-deny property of every careful row beside it.
- **88.6%** use global-only policies -- one policy for the whole application rather than one per
  function -- which collapses the actor dimension of the matrix outright.
- **18.8%** hold unnecessary privilege-escalation capability: the matrix grants authority to
  rewrite the matrix. Twelve applications held defense-evasion permissions they did not need.

*Provenance note.* The arXiv listing abstract and the rendered HTML disagree on the dataset size
(789 vs 689); 789 is the figure used throughout the body of the paper and on the canonical
abstract page, so I have used it. An earlier draft of this record carried a "CSP-managed policies
grant 2.5x more permissions than customer-managed" figure that surfaced in a search summary; it
is **not** in this paper and has been removed rather than attributed to it.

## How this bears on MECH-067

The honest reading is narrow, and I want to state it precisely rather than let it do more work
than it can.

This paper **weakens the sufficiency** of a permission matrix. MECH-067 asserts only necessity.
So as a refutation it attacks a claim that was not made, and nothing here licenses demoting the
claim. What it does instead is three things, all of which change how MECH-067 should be tested
rather than whether it is true:

First, **it names the matrix's own failure mode**. A per-site gate fails by omission -- someone
forgot to check. A matrix fails by permissiveness -- someone wrote a row too wide, and every
subsequent write is correctly mediated and wrongly allowed. These are different bugs with
different detectability profiles, and the matrix does not strictly dominate: it trades an
invisible failure (no gate fired) for a visible-but-unexamined one (a gate fired and said yes).
MECH-067's CONFIRMING clause requires that the matrix "closes the leak and removes the
corruption". This paper says that outcome depends on how the matrix is *authored*, not on whether
it exists.

Second, and most concretely, **it constrains the comparator arm's design**. If the matrix-enforced
arm is built with a hand-tuned, tight policy written by the same session that knows exactly which
writes are legitimate, the comparison measures the design intent, not the artefact. The realistic
first matrix for REE would almost certainly carry a wildcard for the sleep pass (because the set
of parameters `offline_gradient_pass` legitimately touches is not enumerated anywhere) and a broad
row for the closure operator. A PASS obtained against an idealised matrix would not transfer.
The 88.6% global-policy finding is the sharpest version of this: given the option, implementers
collapse the actor dimension, which for REE would mean a single row covering "any ree_core caller"
and no enforcement at all on the dimension MECH-067 cares most about.

Third, **the privilege-escalation finding has no per-site-gate analogue**, and it is worth
flagging as a novel risk rather than a transferred one. 18.8% of applications could rewrite their
own permissions. A REE matrix stored as data that `ree_core` can mutate at runtime would inherit
this; a matrix that is a static, machine-checked contract would not. That is a design constraint
this literature supplies that the claim text does not currently carry.

## Limitations

The transfer is weaker than for the Flume and CRIX entries and I do not want to overstate it.
IAM sprawl is substantially an *organisational* phenomenon: permissions granted broadly because
the person who needs them is in another team, deadlines are real, and no one is rewarded for
tightening a policy that already works. `ree_core` is small and effectively single-authored, so
that pressure is largely absent, and the 47.7% should not be read as a forecast for REE.

PrivLess's ground truth is also inferred, not observed. It derives "needed" permissions from
static analysis of source, which will miss reflection, dynamically constructed resource names and
runtime-assembled ARNs -- all of which would appear as unused permissions and inflate the
overprivilege figure. The bias direction is known and one-sided: 47.7% is an upper bound.

And it is a 2026 preprint with no peer review, on a curated open-source corpus that probably
over-represents demo-quality policies relative to production deployments.

## Confidence

0.6, direction `weakens`. Source quality is the limiting factor (0.6): unrefereed, with an
estimated rather than observed denominator. Mapping fidelity is decent (0.7) because IAM genuinely
is the proposed artefact minus the phase dimension -- though that omission matters, since phase is
where REE's hard cases live (a sleep-phase write into a durable authority store has no IAM
analogue at all). Transfer risk 0.4. I would not let this entry block the audit spike; I would let
it shape what the spike and the comparator are allowed to conclude.
