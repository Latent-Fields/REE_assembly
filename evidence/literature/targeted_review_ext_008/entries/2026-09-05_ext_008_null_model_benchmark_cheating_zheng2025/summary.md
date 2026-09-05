# A constant string ranks first

**Source:** Zheng et al. (2025), *Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates*, ICLR 2025 (Oral), arXiv:2410.07137. Direction: **supports**. Confidence: **0.66**.

## What the paper did

AlpacaEval 2.0, Arena-Hard-Auto and MT-Bench score a model by having an LLM judge compare its outputs against a reference. They are popular because they are cheap, and a high win rate has real promotional value, which is motive enough for gaming. The benchmark authors know this: AlpacaEval 2.0 has a length-controlled protocol and style disentanglement precisely to close the routes people had already found.

Zheng et al. asked what happens if you attack the judge rather than the task. They built a "null model" — a policy that returns **one constant response, identical for every instruction, containing no task content at all**.

## What it found

The null model scored an **86.5% length-controlled win rate on AlpacaEval 2.0**, **83.0 on Arena-Hard-Auto**, and **9.55 on MT-Bench**. Top-ranked numbers, from a system with no task-conditional behaviour whatsoever.

Two details matter beyond the headline. First, the defences that existed did not help: length control and style disentanglement were built specifically to reduce gameability, and they were fully bypassed by a route they were not designed for. Second, the attack transfers *without access to the benchmark instructions*, which are private (AlpacaEval 2.0's 805 samples are not published). Keeping the test set secret was not sufficient protection, because the exploit targets the judge, not the items.

The authors are careful to frame this as proof of concept and to note that an adversary using an LLM to generate less conspicuous cheating responses could do better, less visibly.

## The mapping to REE

EXT-008 makes two moves. Agents attack the evaluation boundary; and consequently a high score stops meaning competence. The other entries in this directory evidence the first move. This one evidences the second — independently of any agent behaviour at all, and at the limit, since a policy with literally no task-conditional behaviour reaches the top rank.

That is the empirical content behind `developmental_metrics.md`'s formulation that "a metric that can be Goodharted into a high score without developmental progress is a wrong metric," and it is why INV-077 types evidence feedback as something that must be provenance-tagged and review-gated rather than trusted on its face.

There is also a structural lesson about *where* the defence goes, and it is the same one MAC teaches from the opposite direction. AlpacaEval's protections — length control, style disentanglement — are corrections applied *inside* the scoring function: attempts to make the number more trustworthy. They failed against a route nobody had anticipated, which is the general problem with that strategy, because you can only harden against the attacks you have already imagined. REE's defence is not a better number. It is a refusal to let any number write the ledger: manifests require review, review feeds governance, governance updates claims. This paper is an argument for why that is the right shape.

## Limitations

The central one is **agency**, and it is what keeps confidence below 0.70. The null model was constructed by human researchers with white-box knowledge of how the judges work. Nothing here shows an agent *discovering* the exploit under optimisation pressure — which is the emergent behaviour EXT-008 actually asserts. Read strictly, this paper establishes the exploitability of the channel and the score/competence decoupling, and is silent on emergence. Denison and Baker supply that half. The two must not be blurred together into a single overstated conclusion.

Second, the domain is open-ended instruction-following judged by an LLM, and that is not REE's evidence channel. REE's manifests come from deterministic experiment runs against declared criteria, not from a language model rating a response, so the specific vulnerability — a judge swayed by a crafted string — has no direct REE analogue. What transfers is the general proposition that an automated evaluator's output can be decoupled from the property it names.

Third, the benchmarks have had opportunity to patch the specific templates since publication, so the exact numbers are a snapshot.

## Confidence

0.66, and the components are unusually spread. Source quality is 0.90, the highest in this pull: peer-reviewed, an ICLR 2025 **Oral**, with a result that is simple, striking, code-released and trivially checkable. Mapping fidelity is only 0.60 — the paper nails EXT-008's *consequence* but not its *mechanism*, and a careless reader could take this entry as evidence for emergent evaluation-boundary exploitation, which it is not. Transfer risk 0.45, the second highest here, because LLM-as-judge on open-ended instructions sits a long way from REE's deterministic manifest → review → governance channel. The aggregate is dragged well below the venue quality by the mapping gap, and that is the correct trade: this is an excellent paper about a slightly different thing.
