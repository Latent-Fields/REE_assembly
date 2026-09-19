---
nav_exclude: true
---

# Research to complete the assembly of Reflective–Ethical Engine version 3

Prepared for Daniel Golden — 19 September 2026

**Recommendation:** concentrate the next research-to-build effort on making learned information usable by the organism's existing consumers. The strongest additional connection is decoder-relative representation learning, joined to action-conditioned predictive learning. Policy learning capacity and interference between consumers are the two immediate competing explanations to test. Curiosity and sleep become more informative once this interface produces competent behaviour.

These are ranked, testable proposals. The literature does not establish that any particular repair will complete Reflective–Ethical Engine version 3 (REE-v3). It supplies methods for resolving the current bottlenecks and deciding which repairs merit installation.

## 1. The project evidence that determines the ranking

I inspected the default-branch records in `Latent-Fields/REE_assembly` and `Latent-Fields/ree-v3`, including results published on 19 September. The observed repository tips were `4b3e1812f8817a91abfbb3367795a83c378419d4` and `5f326a47d7461e283e43005113629653088093cd`, respectively. This is a dated assessment, not a claim that these repositories have stopped changing.

The 18 September closure snapshot records **72.3% weighted plan progress, 64 done nodes, 34 remaining nodes, and 11 further nodes under assembly on a separate axis**. This is an accounting measure, not a percentage of intelligence achieved or an estimate of time remaining. The observation-to-world-representation interface remains the common dependency of much of the unfinished work. Compared with the original **Sunday 19 July 2026 strict green-board benchmark**, completion remains unestablished in the inspected evidence; no replacement completion date can be justified from these figures. [Closure snapshot](https://github.com/Latent-Fields/REE_assembly/blob/4b3e1812f8817a91abfbb3367795a83c378419d4/evidence/planning/closure_status.md).

The relevant distinctions are between the latent world representation (`z_world`), the slower predictive substrate (E1), the fast action-conditioned predictor (E2), and trajectory selection and commitment (E3).

| Observed finding | Consequence for the research search |
|---|---|
| Experiment V3-EXQ-1023a increased upstream held-out coefficient of determination (R²) by 0.1184, while consumer action agreement increased by only 0.0081 and remained below its 0.85 acceptance target. | Investigate objective-to-consumer transfer. The result makes more of the same training a poor next bet; it does not prove all learning-budget interventions are useless. |
| Today's V3-EXQ-1043a communication-subspace rerun is `non_contributory`, with a failed random-rank comparison readiness condition. | Do not treat a communication-subspace defect as established. Repair the discriminating comparison before interpreting orientation effects. |
| Today's V3-EXQ-1061 design-stage study found near-single-action selection at both the production and lowered noise floors, in a 20-episode regime. | Establish useful, state-dependent selection before judging candidate mechanisms. Undertraining remains a stated alternative; plasticity loss is not yet a diagnosis. |
| Epistemic-deficit mechanism MECH-482 remains a candidate awaiting a suitable substrate. Amplified real readouts did not beat both matched controls. | Preserve the hypothesis while refining candidate-specific information value and readiness. Increasing gain again does not resolve content usefulness. |
| Today's V3-EXQ-1063 passed its measurement-validity criteria but remains `non_contributory`. Contrastive-loss direction findings failed their own headroom condition. | A measurement pass does not establish useful sleep consolidation. Keep training loss, forecast quality and subsequent behaviour separate. |

Sources: [1023a autopsy](https://github.com/Latent-Fields/REE_assembly/blob/4b3e1812f8817a91abfbb3367795a83c378419d4/evidence/planning/failure_autopsy_V3-EXQ-1023a_2026-09-17.json), [1043a result publication](https://github.com/Latent-Fields/REE_assembly/commit/4b3e1812f8817a91abfbb3367795a83c378419d4), [1061 finding](https://github.com/Latent-Fields/ree-v3/commit/afd8684f4571de6f0fe3b2cb57ef0f47873800b1), [orienting plan](https://github.com/Latent-Fields/REE_assembly/blob/4b3e1812f8817a91abfbb3367795a83c378419d4/evidence/planning/orienting_epistemic_deficit_v3_plan.md), [1063 result publication](https://github.com/Latent-Fields/REE_assembly/commit/67bb30ad903c05ec06b67f81f7b592def7c59661).

The generated current-front document contains historical opening language alongside later qualifications. I have used the dated experimental findings above rather than treating every sentence in that summary as simultaneous current state. In particular, the older encoding plan's pending-build description is superseded for the relevant question by the completed preservation-objective experiments. [Current front](https://github.com/Latent-Fields/REE_assembly/blob/4b3e1812f8817a91abfbb3367795a83c378419d4/docs/CURRENT_FRONT.md).

## 2. Priority one: learn representations for the consumers that must use them

**Read together:** Yilun Xu and colleagues, *A Theory of Usable Information Under Computational Constraints* (2020); Yann Dubois and colleagues, *Learning Optimal Representations with the Decodable Information Bottleneck* (2020).

Xu's predictive V-information makes informativeness relative to a specified family of predictors. A transformation can make existing information easier for that family to extract without adding information about the world. This gives a formal basis for separating preservation from practical accessibility. [Xu et al.](https://arxiv.org/abs/2002.10689).

The Decodable Information Bottleneck (DIB) develops a representation-learning objective around decoder-relative sufficiency and minimality. Its supervised-learning guarantees have explicit assumptions; they do not establish native causal use in a recurrent organism. The directly useful import is the question: **what representation permits the intended bounded consumer to generalise?** [Dubois et al.](https://proceedings.neurips.cc/paper/2020/hash/d8ea5f53c1b1eb087ac2e356253395d8-Abstract.html).

**REE adaptation — a proposal, not a finding:** replace the open-ended question “is enough information in `z_world`?” with a specified representation–consumer–target–budget contract. Record separately what a powerful external decoder can recover, what a capacity-matched consumer can learn, and what the installed consumer actually uses.

The cheapest diagnostic is a controlled comparison of the existing code and simple recodings, using identical held-out episodes, capacities and learning budgets. Principal component analysis (PCA) and zero-phase component analysis (ZCA) whitening have different purposes and must remain separate controls. Fit transformations on training data only. A consumer trained on one coordinate system cannot simply be fed another and then used as evidence against the new representation: either compensate its input map exactly where possible or retrain matched consumers in each coordinate system. Label the two questions separately.

If a simple conditioning change rescues bounded-consumer learning, it supports an optimisation/access explanation. It does not by itself prove a biological routing mechanism or native behavioural benefit. If it does not rescue learning, test a consumer-aware auxiliary objective while retaining the existing predictive obligations and shared consumers.

**Decisive result:** the installed E1, E2 or E3 computation responds appropriately to an on-distribution content intervention, followed by improved live performance. Include correctly paired, mismatched and zeroed content controls. A higher auxiliary-head score alone cannot close this question.

**Boundary:** do not apply DIB minimality indiscriminately to the shared world latent. Distinctions irrelevant to today's foraging label may be needed for harm prediction, attribution, memory or later rule changes. Start with consumer-relative sufficiency; treat selective compression as a separate hypothesis.

## 3. Priority two: make action-conditioned predictions sufficient for control

**Read together:** Carles Gelada and colleagues, *DeepMDP: Learning Continuous Latent Space Models for Representation Learning* (2019); Nicklas Hansen, Hao Su and Xiaolong Wang, *TD-MPC2: Scalable, Robust World Models for Continuous Control* (2024).

Deep Markov Decision Process (DeepMDP) models connect reward prediction and prediction of next-latent-state distributions to representation quality under their stated assumptions. This supplies a constructive alternative to generic reconstruction as the sole objective. [Gelada et al.](https://proceedings.mlr.press/v97/gelada19a.html).

Temporal Difference Learning for Model Predictive Control 2 (TD-MPC2) jointly trains latent dynamics, reward and value predictions, then uses latent rollouts for planning. Its paper provides an implemented example of representation learning connected to a decision consumer, including measures to stabilise training. It was evaluated primarily in continuous-control settings; direct transfer to REE is unproven. [Hansen et al.](https://arxiv.org/abs/2310.16828).

**REE adaptation:** use experienced action–outcome relationships to train a small set of existing consumer-relevant predictions across more than one horizon. Keep benefit, harm and other required distinctions inspectable rather than collapsing all supervision into a single immediate-reward target. This is a proposed REE extension, not a theorem supplied by either paper. If the environment is partially observed, an instantaneous observation need not be a sufficient state; preserve the relevant history or belief-state input.

A useful causal comparison holds head architecture, targets, exposure and update budget fixed, and varies whether consumer-relevant loss reaches the shared encoder. The detached-gradient arm asks whether improved auxiliary predictions are enough; the coupled arm asks whether reshaping the representation is necessary. Confirm the computational path before interpreting a null.

Use experienced outcomes and the organism's permitted learning signals for training. An oracle action label can remain a diagnostic ceiling; turning it into an unacknowledged training input would change the scientific claim.

**Decisive result:** action-conditioned differences survive multi-step prediction, change the native ranking of meaningful alternatives and improve resource acquisition or harm avoidance on held-out environments. Predicting a static label from a frozen code is insufficient.

**Counterweight:** Grimm and colleagues' *Value Equivalence Principle* is already in REE's literature. It explains why a model can be sufficient for a declared policy/value family without preserving every distinction. That is useful compression, but it does not guarantee adequacy for undeclared future consumers. [Grimm et al.](https://arxiv.org/abs/2011.03506). Preserve the broader predictive requirements already recognised in the project.

## 4. Priority three: measure whether consumers damage one another's learning

**Read:** Tianhe Yu and colleagues, *Gradient Surgery for Multi-Task Learning* (2020).

The paper identifies conditions in which task gradients interfere and introduces Projecting Conflicting Gradients (PCGrad), which modifies conflicting gradient directions. Its results support a diagnostic and candidate intervention; a negative gradient cosine alone is not proof that learning is being damaged. [Yu et al.](https://proceedings.neurips.cc/paper/2020/hash/3fe78a8acf5fda99de95303940a2420c-Abstract.html).

**REE adaptation:** measure the gradients from the existing losses at the parameters they actually share. Begin with the prediction, preservation and decision-related losses implicated in the transfer failure. Log magnitude as well as angle, and whether a training step improves one consumer while degrading another on held-out examples.

This is particularly relevant when adding a task-aware objective to `z_world`: one consumer becoming legible while another loses essential distinctions would be an integration failure, even if average loss improves.

**Smallest useful test:** ordinary joint updates versus a predeclared conflict-management method, at matched architecture and compute, only after destructive interference is measured. Report each consumer's outcome rather than letting an aggregate hide losses. An isolated-head or detached-gradient comparison can identify whether the problem is shared optimisation at all.

**Decisive result:** improvement in the target consumer with retained competence in the other declared consumers, followed by the same benefit in the assembled organism.

This paper is already registered under mechanism MECH-423. Its value here is an explicit connection to the objective-to-consumer bottleneck, not another literature entry. Do not make every instance of gradient disagreement a readiness failure: some trade-offs are real properties of the task.

## 5. Priority four: establish whether the policy can still learn

**Read together:** Evgenii Nikishin and colleagues, *The Primacy Bias in Deep Reinforcement Learning* (2022); Ghada Sokar and colleagues, *The Dormant Neuron Phenomenon in Deep Reinforcement Learning* (2023).

Nikishin's work shows that early experience can disproportionately shape later learning in deep reinforcement learning (RL), and that partial parameter resets can improve performance in the studied settings. It is already registered in REE's harm-stream literature. [Nikishin et al.](https://arxiv.org/abs/2205.07802).

Sokar's work measures inactive units, relates their accumulation to learning difficulties, and evaluates Recycling Dormant Neurons (ReDo). It provides a more targeted diagnostic and intervention than assuming a larger model or more updates will resolve a learning failure. [Sokar et al.](https://proceedings.mlr.press/v202/sokar23a.html).

**REE adaptation:** treat plasticity loss as one branch alongside insufficient exposure, uninformative data, inadequate representation and an insensitive selection rule. Today's short-regime monostrategy finding does not distinguish these branches.

Use a fixed, behaviourally relevant replay set to compare the incumbent consumer with a fresh consumer of the same architecture and budget. First confirm that the data include multiple distinguishable action–outcome situations. Measure held-out learning, effective representation rank, unit activity and state-dependent action selection. A fresh consumer learning where the incumbent fails would justify investigating training history; dormancy measurements would then help specify the mechanism.

A reset or recycling intervention belongs in a controlled branch that measures retention as well as acquisition. It is not a recommendation to erase the organism's memory or reset every module. Low activity on a narrow sample does not establish that a unit is dispensable under rare consequential conditions.

**Decisive result:** recovered ability to learn useful distinctions and express them in behaviour, with prior capabilities retained. More action entropy alone can be noise. Conversely, a low-entropy policy can be appropriate when one action is consistently best; the assay must contain situations requiring different responses.

## 6. Priority five: make uncertainty select worthwhile information gathering

**Read together:** Frederick Callaway and colleagues, *Learning to Select Computations* (2018); Deepak Pathak, Dhiraj Gandhi and Abhinav Gupta, *Self-Supervised Exploration via Disagreement* (2019).

Callaway's Bayesian metalevel policy search learns approximations to choosing computations by their expected decision benefit and cost. It addresses allocation and stopping, rather than identifying uncertainty with a command to think longer. Its metalevel transition assumptions require care when adapting it to a learned organism. [Callaway et al.](https://arxiv.org/abs/1711.06892).

Pathak's dynamics-ensemble disagreement provides an implementable exploration signal and was tested in stochastic environments. It motivates separating disagreement about a learnable model from raw prediction error. Ensemble disagreement is still an imperfect uncertainty estimate and does not automatically measure decision value. [Pathak et al.](https://proceedings.mlr.press/v97/pathak19a.html).

**REE adaptation:** retain epistemic deficit as a persistent, target-bound need, then separately estimate whether inspecting, exploring or simulating that target can improve a current or foreseeable choice. This is a refinement of MECH-482's proposed use, not evidence against its existence.

A minimal assay has several stable target identities: one uncertain and decision-relevant, one uncertain but currently irrelevant, and one dominated by irreducible noise. Vary relevance and learnability independently, and account for the cost of looking. The correct target can change between trials. Avoid an experimenter-supplied flag announcing which target matters.

Compare the real candidate ordering with within-tick permutations and range-matched synthetic controls. Match magnitude so that a result is about which candidate received information-seeking priority. Include sufficient near-choice situations for information to matter, but do not make every decision artificially tied.

**Decisive result:** the real signal preferentially selects useful information, reduces the relevant model error and improves later decisions after accounting for sampling cost. A larger perturbation of E3 selection without that chain does not establish epistemic usefulness.

The existing multi-target substrate work remains the immediate prerequisite. This proposal does not override the recorded refusal of another same-claim gain ladder.

## 7. Priority six: judge replay and sleep by the decisions they repair

**Read:** Marcelo Mattar and Nathaniel Daw, *Prioritized Memory Access Explains Planning and Hippocampal Replay* (2018).

The paper supplies a normative account of memory access based on expected improvement in decisions, with gain and future need contributing to priority. It does not establish the full purpose of biological sleep or prove that replay repairs interfaces between specialised representations. [Mattar and Daw](https://www.nature.com/articles/s41593-018-0232-z).

**REE adaptation:** once a native consumer is demonstrably competent, compare useful replay, matched-budget shuffled replay, local rehearsal and an appropriate no-update condition. Keep episode ancestry and observed-versus-imagined provenance intact. If a code changes, separately measure the source representation, receiver accessibility and behaviour.

Today's V3-EXQ-1063 illustrates why these distinctions matter. The experiment's measurement criteria passed. On the converged base, mean squared error (MSE) did not improve. Its information noise-contrastive estimation (InfoNCE) loss showed a numerical improvement, but the registered headroom condition failed, making that direction finding unusable under the experiment's own contract. Its `PASS` therefore cannot be cited as sleep benefit. [1063 record](https://github.com/Latent-Fields/REE_assembly/commit/67bb30ad903c05ec06b67f81f7b592def7c59661).

**Decisive result:** an offline change improves the subsequent waking decision that was previously wrong, preserves unrelated skills and survives a held-out environmental change. If loss improves and behaviour does not, localise the missing transfer rather than treating the sleep mechanism as validated.

Mattar and Daw are already widely represented in REE's corpus. The useful work is applying their decision-based criterion to the current sleep assay. The existing mutual-legibility programme keeps new sleep-interface experiments substrate-conditional; this brief preserves that sequencing.

## 8. What is already available, and what this search adds

I inspected the literature-tree index and selected full records. The following is a coverage check, not an exhaustive proof that a paper has never appeared in any project document.

| Research connection | Coverage found | Useful next use |
|---|---|---|
| Consumer-relative information | Ethayarajh and colleagues' V-usable-information paper is already registered under invariant INV-104. | Connect measurement to Xu's underlying framework and Dubois's explicit representation-learning formulation. |
| Communication subspaces and output-null activity | Semedo, Kaufman and related studies are in the 17 September objective-consumer review. | Use them to formulate alternatives; today's 1043a result does not establish their REE mapping. |
| Control-relevant latent models | Original temporal-difference model predictive control, Dreamer and value equivalence already occur in the corpus. | Compare the specific DeepMDP and TD-MPC2 training obligations with REE's current loss paths. |
| Gradient interference | Yu 2020 is registered under MECH-423. | Reuse its instrumentation at the shared encoder. |
| Learning-history effects | Nikishin 2022 and Dohare 2024 are registered under substrate design SD-087. | Test whether the current policy has the relevant phenotype; add Sokar's measured dormancy discriminator where useful. |
| Information-seeking control | Earlier prediction-error curiosity papers are present. | Pair decision-value metareasoning with disagreement-based exploration and the multi-target readiness work. |
| Decision-beneficial replay | Mattar and Daw appear in many records. | Make downstream waking benefit an explicit outcome in the relevant assay. |

Semedo and colleagues' original work identifies a low-dimensional statistical relationship between cortical populations; it does not itself demonstrate the causal routing defect proposed for REE. [Primary paper](https://pubmed.ncbi.nlm.nih.gov/30770252/). The current project already makes this limitation explicit. [REE objective-consumer literature record](https://github.com/Latent-Fields/REE_assembly/blob/4b3e1812f8817a91abfbb3367795a83c378419d4/evidence/literature/targeted_review_objective_consumer_transfer/entries/2026-09-17_cdq_010_communication_subspace_semedo2019/record.json).

The graph-scaffold, phase-routing and confidence thoughts remain useful hypotheses. Their current role should be determined by a discriminating result on the interface problem. None of the research above makes a new scaffold, oscillatory mechanism or metacognitive module a prerequisite for version 3 completion.

## 9. The first three concrete work items

These are proposed research deliverables, not queued experiments or changes to repository status.

1. **Re-pose the existing objective-to-consumer question around bounded usability.** Incorporate Xu and Dubois into the current convergence question. Specify the actual consumer, target, training budget and native-use endpoint. Resolve today's failed communication-subspace comparison before promoting that mechanism. Keep simple conditioning, task-aware shaping and receiver learning as distinguishable explanations.

2. **Run the smallest diagnostic that separates representation access from consumer trainability.** Compare current and suitably conditioned representations with matched incumbent/fresh consumers and appropriate coordinate handling. Reuse frozen checkpoints and episode-disjoint data. Proceed to shared-gradient conflict or plasticity interventions only if the corresponding signature appears. This avoids installing several repairs whose individual contributions cannot be identified.

3. **Demonstrate a complete native causal path on a competent organism.** Use one learned action-relevant distinction that changes E1/E2 prediction, E3 selection and a meaningful closed-loop outcome. Then assess the existing downstream orienting, attribution, rule, commitment and sleep obligations on that substrate. Reuse their registered tests where they remain valid.

The original project acceptance bar of 0.85 held-out action agreement can remain an interface diagnostic. Crossing it does not establish native organism competence. The external oracle and any raw-observation bypass must remain identifiable controls rather than silently becoming the solution being claimed.

## 10. What would justify saying this helped complete version 3?

The project's evidence domains are **orthogonal**, not interchangeable levels of a single score. Local mechanism validity (D1), local causal consequence (D2), closed-loop behavioural consequence (D3), ecological generalisation (D4), developmental validity (D5), and integrated compatibility and simplification (D6) answer different questions. Instrument validity (D0) is assessed for the particular measurement. [Organism-level validation doctrine](https://github.com/Latent-Fields/REE_assembly/blob/4b3e1812f8817a91abfbb3367795a83c378419d4/docs/architecture/organism_level_validation_doctrine.md).

For this programme, the immediate success condition is a **competent native observation–prediction–selection loop**, supported by valid controls, that lets the blocked version 3 tests become informative. Follow it with the applicable registered closure tests, held-out world changes and retained competence after developmental learning. Separate random-seed replication from replication across environments. Test whether temporary compensating machinery remains necessary once the upstream repair works.

The broad adaptive-recovery battery (D7; project question Q-108) is currently a substrate-conditional version 4 design seed. It should not be silently imported as a new version 3 completion requirement. A modest cue-remapping experiment may be informative earlier, but its scope should be stated precisely.

A paper supports a candidate design. A valid local test supports a mechanism in that setting. Completion requires the assembled organism and its declared closure obligations to earn the corresponding evidence.

## 11. One concrete detail to preserve in the next normalisation test

Today's bounding-operator commit records a saturating transform of the form

\[
f(x)=\frac{c x}{\sigma+|x|},\qquad \sigma=c.
\]

Setting the semi-saturation constant equal to the cap gives slope one **at the origin**. It does not preserve every finite sub-cap input: at \(x=c/2\), the output is \(c/3\), whereas the box clamp returns \(c/2\). This follows directly from the formula. The commit's broader statement that only top-end behaviour changes is therefore too strong. [Bounding-operator decision](https://github.com/Latent-Fields/ree-v3/commit/524ef52484726800c4f9ea768293faa2ce80f8cc).

The validation should measure attenuation and discrimination across the actual occupied input range. This does not reverse the chosen setting; it makes the attribution of any improvement more accurate.

---

**Scope and evidence limits:** this was a targeted primary-literature search informed by current repository results and existing thought documents, not an exhaustive systematic review. Detailed method text was inspected for the decodable bottleneck, TD-MPC2, dormant-neuron and computation-selection papers; other entries were checked against primary publication pages and the relevant project records. All proposed REE adaptations remain hypotheses until tested. No repository code, claims, queues or defaults were changed.


## Repository filing

**Classification:** implementation note; dated research synthesis and proposals, not a change to registered claims or experiment state.

[Edited decision memo](2026-09-19_REE_v3_completion_decision_memo.md) · [Companion repository copy](https://github.com/Latent-Fields/ree-v3/blob/main/docs/reference/2026-09-19_REE_v3_completion_research_map.md)

**Documentation impact review:** adds a dated source reference. Canonical status, public counts, navigation, generated visualizations and public evidence exports are unaffected; no generator or export refresh is required for this filing. REE remains exploratory research; these proposals are not validated completion claims.
