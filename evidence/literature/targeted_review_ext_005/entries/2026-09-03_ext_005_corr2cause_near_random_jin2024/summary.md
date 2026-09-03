# Remove the recall, and the causal competence goes with it (Jin et al., ICLR 2024) — EXT-005

**Source:** Jin Z, Liu J, Lyu Z, Poff S, Sachan M, Mihalcea R, Diab M, Schölkopf B. *Can Large Language Models Infer Causation from Correlation?* ICLR 2024. arXiv:2306.05836.

## What the paper does

The authors make an observation about the state of causal NLP that is, on reflection, damning: essentially every existing benchmark lets a model score well by *remembering* rather than *inferring*. Asked whether smoking causes cancer, a model can answer correctly from the corpus, and its answer tells you nothing about whether it can reason causally at all. So they build **Corr2Cause**: over 200,000 samples, each presenting a set of correlational statements over abstract variables and asking for the causal relationship between them. The empirical knowledge is gone by construction; only the inference remains.

Seventeen LLMs are evaluated. They perform close to random. The authors then try to repair this by finetuning, and the result of that attempt is the more interesting half of the paper: the finetuned models do learn the task, but only in-distribution. Perturb the variable names and the textual expressions, and the competence disappears. What was fitted was the shape of the answer, not the operation that produces it.

## The finding that matters for EXT-005

This converts the Zečević et al. conjecture — also in this pull — into a measurement, and it does so with the right control. Their claim was that apparent causal competence is recitation from a corpus in which the causal conclusions already sit as text. Corr2Cause is precisely the experiment that removes the text and looks for what remains. What remains is near-chance.

The finetuning result is what makes me weight this entry highly. If the deficit were a matter of insufficient supervision on causal tasks, supervision would fix it. It does not; it moves the surface. That is the signature of something absent rather than something undertrained, and "absent rather than undertrained" is the load-bearing modality in EXT-005.

The architectural reading for REE: a causal conclusion has to be computed from something, and what a causal computation needs is an *intervention*. An agent has one — the action it just took. Text does not. REE's comparator family is a computation over exactly that: SD-029 differences the observed reafferent state against the forward model's prediction under the action actually issued, and ARC-037 is the routing circuit that decides whether the resulting error is booked as agent-caused or environment-caused. None of that is in this paper. What the paper establishes is the negative half — with no such computation, causal output is surface form — and it establishes it under a control that the alternatives lack.

## Limitations

The central one is task shape, and it is a real distance rather than a formality. Corr2Cause is offline, third-person and formal: given correlational statements about variables the system never acted on, name the causal relation. EXT-005's failure mode is online, first-person and agentive: attribute an observed change to one's own action, or decline to. These are related deficits, not the same deficit. A comparator does not induce a DAG; it subtracts a prediction. A system could in principle be hopeless at Corr2Cause and perfectly serviceable at reafference cancellation. So what this entry supports is the *general* absence of causal machinery in text-trained systems, from which EXT-005's specific claim follows only by inference.

Second, near-random performance measures the absence of a *competence*, and the step from there to the absence of a *mechanism* is a step. A very weak mechanism fits the data equally well. The finetuning generalisation failure narrows this considerably — it is hard to see what weak mechanism would be invisible to in-distribution finetuning yet present — but it does not close it.

Third, this is the 2023–2024 model generation, evaluated zero-shot and finetuned. The finetuning result insulates the conclusion against the "you prompted it wrong" objection much better than a zero-shot-only result would, but it does not insulate against the "that generation" objection.

## Confidence

0.80, the highest in this pull. Source quality 0.88 — ICLR main track, Schölkopf on the author list, 200K samples, and above all a design whose entire purpose is removing the confound that makes competing results uninterpretable. Transfer risk 0.25: no species or clinical step, only generation. Mapping fidelity 0.70 is what holds the aggregate below 0.85, for the first limitation: this measures third-person causal induction, and EXT-005 is about first-person attribution.
