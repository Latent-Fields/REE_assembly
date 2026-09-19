# Schneier & Kelsey (1999) -- Secure audit logs to support computer forensics

**Claim tested:** ARC-098 (safety.autonomy_suspension_without_shame) | **Direction:** supports | **Confidence:** 0.68

## Why this entry exists

The Winfield & Jirotka entry in this directory gives ARC-098's preservation conjunct its
architectural shape -- a one-way dataflow into a recorder the agent cannot reach -- and then
discharges the hard half in a single sentence: "The EBB will of course also need to be secure and
tamper-proof." This entry is what that sentence resolves to when someone actually does the work.

## What the paper did

Schneier and Kelsey address a problem in computer forensics with an awkward circularity. Audit logs
are how you find out what an attacker did. But the log lives on the machine the attacker has taken,
and the first thing a competent attacker does is edit the log. If the machine holds the keys that
authenticate its own entries, the attacker holds them too, and can rewrite history at leisure.

Their construction breaks the circle with key evolution. A logging machine opening a new log
establishes a shared secret with a trusted remote server. After each entry is written, the current
key is evolved into the next through a one-way function and the old key is erased. Entries are
linked in a hash chain -- each entry's hash covers the entry data and the previous link -- and each
carries a MAC computed under whatever key was current when it was written.

The consequence is the one that matters. An attacker who takes complete control of the machine at
time *b*, including every secret it currently holds, gets the key for time *b* and everything after.
The keys for times before *b* are gone -- destroyed by the machine itself, in the ordinary course of
logging, before the attacker arrived. So every entry written before the break-in is unforgeable,
unmodifiable, and undeletable without detection, by an adversary who has otherwise won completely.
This is *forward security*: the past is sealed against a future compromise.

The paper has been the foundation for most subsequent secure-logging work, and its limits are
correspondingly well characterised. I have taken the two that matter here from Ma and Tsudik's
analysis (IACR ePrint 2008/185), which is careful about attributing them.

## How this bears on ARC-098

ARC-098's preservation conjunct has an adversary problem that the claim's wording does not make
obvious. *Preserve evidence* -- against whom?

The answer is the uncomfortable one. Against the system itself, in the state the evidence is about.
Every other conjunct of ARC-098 can be read as a constraint on a cooperative agent; this one cannot,
because its whole point is to hold when cooperation is what has failed. A preservation design that
depends on the agent's continued willingness to preserve has assumed away the case it exists for.

Schneier and Kelsey are evidence that the uncooperative case is tractable. Their threat model is
literally "the custodian of the log and the thing under investigation are the same machine, and it
has turned", and they show that the record leading up to the turn survives it. Transposed: the trail
of a V5 self-model's approach to a dangerous self-state can be made unrewritable by the self-model
that arrives in that state -- not by its restraint, but by the fact that the keys which would let it
rewrite were destroyed while it was still well. That is a meaningfully stronger form of "preserve
evidence" than a record the agent merely declines to alter, and it is the strongest form actually
available.

It also draws a line ARC-098 should adopt explicitly, because the line is sharp and the claim
currently blurs it. Forward security protects the past and abandons the present. From the moment of
compromise, the adversary holds the current key and everything it writes verifies correctly. So the
record of the *approach* to a dangerous self-state is defensible; the record produced by a system
already in one is not, and must not be treated as equally trustworthy. That is a real design
constraint, and a useful one: it tells you which part of the log an investigator should weight.

## Where the guarantee falls short of the claim

Two documented weaknesses, and both land on ARC-098 rather than passing it by.

The scheme does not defend against truncation -- deleting a contiguous run of tail-end entries. Ma
and Tsudik's account is precise about why: entries still on the logging machine have no single
authentication tag covering the file as a whole, so a hash-chain element only protects what preceded
it, and truncating everything after some point goes undetected unless the trusted server happens to
know how far the chain should have run. The bitter part for this claim is *which* entries are
exposed. The tail is the recent past. The recent past is the episode under investigation. The scheme
protects most strongly exactly the evidence an investigator needs least.

Verification is server-assisted. The verifier cannot check the log alone; it must send the final
hash and MAC to a trusted server that knows the initial key. This yields delayed detection --
tampering goes unnoticed until the log is uploaded -- and a single point of failure. ARC-098 does
not escape this; it inherits it. The conjunct presupposes an external party with standing to hold
the other end of the key chain, and the claim as written names no such party. This is the second
time in this directory that an unnamed external corrector has surfaced from a different direction:
Winfield & Jirotka reach it through the argument that it is the investigation, not the recorder,
that concludes anything. Two independent literatures pointing at the same missing entity is worth
governance attention.

## Limitations

The transfer is structural analogy and the source domain is not agents. This is a paper about hosts,
keys and attackers, making no claim about cognition, self-states, or anything a system might be said
to want. The analogy holds only if "agent entering a dangerous self-state" can stand in for
"attacker compromising the logging host", and that substitution is doing work the paper cannot
license. A compromised host has an adversary's goals. ARC-098's premise -- read with its third
conjunct and with the Tangney entry -- is that a well-designed agent should have no such goal.

So the honest reading is narrower than it first looks: this paper establishes what preservation can
guarantee under the *worst* case, not what the expected case looks like. It is an upper bound on the
adversary and a lower bound on the machinery, which is genuinely useful for an architectural
commitment and is not the same thing as evidence that REE's agent would ever behave this way.

There is also a completeness gap that no amount of cryptography closes. Integrity guarantees that
the record is faithful to what was emitted. It says nothing about whether what was emitted is
faithful to what happened. An agent that never writes the entry, or writes a technically-true and
uninformative one, defeats the whole construction without touching a key. ARC-098's preservation
conjunct therefore needs a completeness argument as well as an integrity one, and this literature
supplies only the integrity half.

## Confidence reasoning

Source quality 0.88, the highest in this directory: ACM TISSEC, foundational, heavily built upon,
and -- the part that actually justifies the number -- with limits that the subsequent literature has
characterised precisely rather than left implicit. Mapping fidelity 0.60 is the binding constraint,
for the reason above: the subject is a logging host under attack, not an agent. Transfer risk 0.45,
close to the Tangney entry's 0.48 but for a different reason -- not species transfer but domain
transfer from security engineering to cognitive architecture.

Aggregate 0.68, below Winfield's 0.72 despite far stronger source quality, because ARC-098 is an
`architectural_commitment` and the weighting follows mapping fidelity. A better paper can be weaker
evidence for a particular claim, and saying so is the point of keeping the components separate.
