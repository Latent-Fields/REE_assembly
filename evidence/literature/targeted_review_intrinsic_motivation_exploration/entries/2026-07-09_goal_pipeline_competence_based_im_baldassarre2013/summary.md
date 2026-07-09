# Mirolli & Baldassarre (2013) — Functions and Mechanisms of Intrinsic Motivations

**Claims tested:** MECH-314c, MECH-307 (goal-representation host), ARC-065
**Direction:** mixed · **Confidence:** 0.74
*(Chapter 3 of Baldassarre & Mirolli (eds), *Intrinsically Motivated Learning in Natural and Artificial Systems*, Springer 2013.)*

## What the chapter did

Mirolli & Baldassarre take the sprawling intrinsic-motivation literature and impose a
single, functionally-grounded cut. Intrinsic motivations, they argue, come in **two kinds
that do different jobs**. *Knowledge-based* IM — novelty, surprise, prediction error,
learning progress — rewards the agent for improving its **model of the world**; it drives
exploration and attention. *Competence-based* IM — the reward is **progress in the agent's
ability to achieve a self-generated goal** — drives the autonomous acquisition of reusable
**skills**. The distinction is not cosmetic: the two require different machinery. Knowledge-
based IM needs only a predictor and its error signal. Competence-based IM needs an explicit
**repertoire of goals** and, for each, an estimator of how well the agent is getting at
*reaching* that goal. The chapter's thesis is that autonomous cumulative learning — building
a hierarchy of skills with no external task reward — requires competence-based IM, and that
substituting a knowledge-based signal for it produces agents that explore richly but never
consolidate competence.

## The finding that matters for REE — and why it is the WS-1 hinge

Read against REE's registry, the diagnosis is uncomfortably precise. **Every** intrinsic-
motivation claim REE has registered — MECH-314 (info-gain), MECH-314a (novelty), MECH-314c
(learning progress) — is *knowledge-based*. All three reward improving prediction; not one
rewards improving goal-achievement. REE has, in other words, built the entire knowledge-based
half of the IM taxonomy and **none of the competence-based half**.

Now put that beside WS-1's terminal finding: the fully-integrated all-ON agent forages
0.065 / 0.0 / 0.455 resources per episode — it *cannot competently act* — even though its
curiosity substrate is wired and its goal pipeline (MECH-307 conjunction, SD-012 drive,
MECH-229 wanting/liking) passes every isolation test. Mirolli & Baldassarre predict exactly
this symptom: an agent driven to earn skills by a knowledge-based drive alone will explore
but not become competent. The competence floor is not (only) a training-regime bug; it is
the signature of a **missing drive type**. The goal pipeline supplies the goal
representations competence-based IM needs, but it currently sources *wanting* from
homeostatic/hedonic value (SD-012, MECH-229), never from *competence progress on a goal*.

## The translation to substrate

Competence-based IM in REE would be a wanting signal indexed to **goal-achievement progress**:
for each active goal in the pipeline, an EMA of the improvement in the agent's success rate /
proximity-at-termination, injected as an intrinsic bonus that biases the agent toward goals it
is *currently getting better at reaching*. This is structurally the learning-progress idea of
MECH-314c (companion Oudeyer & Schmidhuber entries) but computed over **behavioural competence**
rather than **predictive error** — the same derivative, a different operand. It attaches to the
goal pipeline / drive plane, not the E1/E2 world-model, and it is the concrete mechanism WS-1
is reaching for when it asks how the substrate could *earn* the capability floor at which
commitment gating becomes measurable.

## Limitations and honest caveats

This is a conceptual/taxonomic chapter, not a decisive experiment, so it evidences the
*distinction and its functional necessity*, not a quantitative REE result — hence the mixed
direction. Crucially, competence-based IM is **not currently a registered REE claim**; this
entry documents an *absence*, tagging the claims the distinction bears on (MECH-314c as the
knowledge-based endpoint, MECH-307 as the goal host, ARC-065 as the diversity umbrella) rather
than testing an existing claim. The proper downstream move is a candidate-claim registration
("competence-based intrinsic motivation / goal-achievement-progress wanting"), which WS-9's
synthesis flags for the goal_pipeline_plan and WS-1, not something to assert from a single
review chapter. The risk in adopting it is the mirror of knowledge-based IM's noisy-TV trap:
if goal-competence is mis-estimated the agent chases goals it only *appears* to be improving
at — so any implementation needs the same derivative-not-level discipline Oudeyer & Kaplan
insist on.
