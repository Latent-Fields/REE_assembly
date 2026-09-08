# Deeply Felt Affect: the emergence of valence in deep active inference (Hesp et al., 2021)

## What the paper did

Hesp, Smith, Parr, Allen, Friston and Ramstead set out to do for valence what active inference
has done for perception and action: derive it rather than posit it. Their proposal is that an
agent infers its own valence state from the *expected precision of its action model* -- an
internal estimate of how well its policy-generating model is currently working, which they call
subjective fitness. The updating term for that estimate, which they name affective charge,
tracks changes in fitness and supplies a sign to divergences between prediction and outcome
that would otherwise be unsigned. Good news is not simply surprise reduced; it is surprise
reduced in a way that raises confidence in one's own model.

Structurally, this places valence high in the hierarchy: perception and world model at the
bottom, policy selection above that, implicit metacognition tracking confidence in the action
model above that, and explicit valence states accumulating affective charge above that again.
They simulated an affective agent in a T-maze requiring context learning followed by context
reversal, and compared it against a lesioned agent with the valence representations removed. The
affective agent switched adaptively between exploratory (negative valence) and exploitative
(positive valence) modes and recovered better after reversal.

## Key findings relevant to ARC-043

Two, pulling in opposite directions -- which is why I have scored this entry mixed rather than
supporting, and it took some deciding.

The supporting half: ARC-043 asserts that Layers 0-4 function as *axioms* from which Layer 5
ethics is derived. For that architecture to be more than a list, the lower layers need to be
the sort of thing that can ground derivation. Hesp et al. show that valence -- which is
routinely treated as a primitive, a raw given of the system -- is formally derivable from an
inference architecture resting on epistemic foundations. That is a real point in favour of the
stack's derivational logic. Valence does not have to be bolted on; it can fall out.

The weakening half: the derivation requires nothing social. There is no representation of
another agent anywhere in the model. A complete, behaviourally efficacious valence emerges from
purely self-directed inference about one's own model fitness. ARC-043 places shared valence at
Layer 4, sitting *above* other minds (Layer 2) and shared world (Layer 3). If valence is
obtainable without either, that placement is a substantive extra commitment which this
formalism does not underwrite.

There is a third wrinkle worth flagging. Hesp's valence is second-order -- a belief about the
precision of one's own action model -- which puts it structurally *above* policy selection.
ARC-043 has Layer 4 valence as an axiom feeding Layer 6, the decision system. The orderings
are, on their face, inverted.

## How this translates to REE

The fair reading is that this paper endorses ARC-043's method while querying its arrangement.
It says: yes, you can build an ethical stack by derivation rather than stipulation, and valence
is one of the things that derives. It also says: your particular sequencing of the lower layers
is not forced by the mathematics, and at least one well-worked formalism gets valence without
the two layers you put beneath it.

## Limitations and caveats

The most important caveat cuts in ARC-043's favour, and I should state it plainly rather than
bury it. ARC-043's Layer 4 is "love/shared valence" -- the *shared* is doing work. Hesp et al.
model valence simpliciter. It is entirely coherent that individual valence needs no social
substrate while *shared* valence does, in which case the ordering survives untouched and this
paper is simply about a different quantity. I have not scored the entry as a clean weakening
for exactly this reason. But that rescue is available rather than established: nothing here
demonstrates that shared valence requires other-minds and shared-world beneath it, so the
ordering is currently a commitment rather than a result, and this paper is what makes that
visible.

Beyond that: the work is simulation-only, on a rodent T-maze, with no ethical content at any
point. The authors are explicit that they have demonstrated face validity and that the model
awaits fitting to behavioural and neuronal data. So it constrains what an architecture *can*
look like, not what any real system does.

## Confidence reasoning

Confidence 0.55, which is deliberately modest. Source quality 0.80 -- Neural Computation,
formally rigorous, but simulation-only and self-declared as a first step. Mapping fidelity 0.60,
capped by the shared-versus-individual valence ambiguity, which is this entry's main
interpretive risk: the paper is unambiguously about valence, and may nonetheless not be about
ARC-043's valence. Transfer risk 0.40. The value of the entry is less that it settles anything
than that it locates the load-bearing under-specification in ARC-043 -- the claim needs to say
whether Layer 4 is shared valence *because* sharing requires the layers beneath it, or whether
the ordering there is inherited from the axiom list's narrative order rather than from a
dependency. That is a question governance can act on.
