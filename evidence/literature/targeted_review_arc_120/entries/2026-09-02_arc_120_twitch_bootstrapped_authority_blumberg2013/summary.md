# Twitching in sensorimotor development from sleeping rats to robots

Blumberg, Marques & Iida (2013), *Current Biology* 23(12):R532-R537. PMID 23787051, PMC3709969. doi:10.1016/j.cub.2013.04.075.

## Why this entry is here

The other four entries in this directory support ARC-120. This one is here to press on it, and it is the entry I would read first.

## What the paper says

Myoclonic twitches -- the jerky limb movements of sleeping fetuses and infants -- were for decades written off as functionless motor noise, the discharge of a dreaming brain. Blumberg and colleagues review the work that overturned this. The neural mechanisms producing twitches have been identified, as have the pathways conveying sensory feedback from the twitching limb back to spinal cord and brain. That reafference, they argue, is not incidental: it is the signal that drives self-organisation of spinal and supraspinal sensorimotor circuits. The developmental-robotics half of the review supplies the constructive evidence -- when twitches are mimicked in robot models of a musculoskeletal system, the basic circuitry self-organises without anyone specifying the map.

## The tension with ARC-120

ARC-120 says behavioural authority is earned through demonstrated competence and "never granted merely because a computation or mechanism exists." Twitching is a mechanism that exists, has no competence of any kind, is granted motor output authority anyway, and acquires competence *because* of the output it was granted. The map is not a precondition for the movement. The movement is a precondition for the map.

Read strictly, that is a counterexample, and the strict reading exposes a real design fault rather than a quibble. If authority is conditioned on demonstrated competence, and competence for a given mechanism can only be demonstrated through the reafferent consequences of that mechanism's own output, then the gate is a deadlock. The mechanism can never earn what it is denied. A competence gate with no bootstrap path is not conservative; it is inert. Any ARC-120 instance in REE ought to be auditable against that question: *how does a mechanism under this gate ever acquire the competence the gate demands?* If the answer is "from some other mechanism's output," fine. If there is no answer, the gate is broken in a way that will not show up as an error.

## The reading that rescues the claim, and why it should be written down rather than assumed

There is an obvious rescue, and I think it is probably right, but it is not what ARC-120 currently says. Twitching happens during *active sleep*. The behavioural consequences are, to a first approximation, quarantined -- the animal is not navigating, foraging or escaping while it twitches. So this is not authority granted to an incompetent mechanism in the world; it is authority granted inside a sandbox, where the mechanism can act, generate reafference, and learn, without its incompetence costing anything. On that reading the twitch is not a violation of ARC-120 but an *instance* of it, in a mode ARC-120 does not currently name: sandboxed authority as the bootstrap phase of the sequence.

Two things follow. First, ARC-120's wording should distinguish consequential authority from sandboxed authority, because as written it does not, and the difference is the difference between a principle and a deadlock. Second -- and this is the part that interests me architecturally -- the quarantine here is *state-dependent, not mechanism-dependent*. The same spinal and supraspinal circuitry has consequential authority when the animal is awake and sandboxed authority when it is in active sleep. Nothing about the mechanism changed; the global mode did. A competence gate implemented per-mechanism cannot express that. It needs a mode variable, which in REE means this lands next to MECH-261 (mode gating) rather than next to the per-event eligibility gates. That is a non-obvious consequence, and it is the sort of thing that makes ARC-120's unification claim more interesting rather than less: the four gates it generalises over may need a fifth term.

## Limits

This is a perspective review, not a decisive experiment. The functional claim -- that twitch reafference *builds* the map -- is well motivated and the robotic self-organisation results give it real constructive weight, but it remains a proposal about necessity rather than a demonstration of it. Rodent and robot; no human data; nothing about memory-write or commitment authority. And the sandbox reading should not be waved through: twitches do move real limbs and do generate real proprioceptive and tactile input, so active sleep quarantines *behavioural* consequence, not sensory consequence. Whether that is the right kind of quarantine for REE's purposes is an open question, not a settled one.

## Confidence

0.66, and it is worth being explicit that this number scores how well the entry establishes the *tension* it was included for, not how strongly it supports the claim. Direction is `mixed` rather than `weakens` because the sandbox reading is genuinely available and probably correct -- but the ambiguity is itself the finding, and resolving it is a wording change to ARC-120, not a matter of interpretation. Source quality 0.72 (authoritative group, high-visibility venue, perspective piece resting on a functional proposal). Mapping fidelity 0.70: the bootstrap problem is abstract and transfers cleanly to any competence-gated architecture. Transfer risk 0.35, low for a rodent/robot source, because the chicken-and-egg structure is substrate-independent.
