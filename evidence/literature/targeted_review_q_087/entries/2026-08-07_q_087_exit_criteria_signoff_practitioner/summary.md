# Exit criteria and QA sign-off (practitioner consensus) -- Q-087

**Direction: mixed (confidence 0.45)** -- this is the entry's disconfirming/mixed contribution.

## What this source is

Not a single paper but the settled practitioner consensus on *when to stop testing and declare a build release-ready*, drawn from several well-known software-QA references (PractiTest, Enov8, BrowserStack, testRigor). I have grouped them because they say the same two things, and it is the tension *between* those two things that makes this evidence worth recording for Q-087.

## The two poles, which are Q-087's two candidates

The first pole is the **objective, measurable exit gate**. The consensus is emphatic that exit criteria "provide a clear, measurable finish line for testing, removing subjectivity and deadline pressure from the decision," and act as "a quality assurance gate." This is, almost word for word, Q-087's **strict-green-board** candidate: closure happens when a defined, objective board is satisfied, and the whole point is to take human judgement out of it.

The second pole is the **stakeholder risk-based sign-off**. The same sources acknowledge that in reality "release decisions are often made in collaboration with developers, product owners, business stakeholders, and release managers," and that "the decision behind each sign-off is typically based on risk assessment, considering the impact of unresolved issues against the project timeline, business needs, and customer expectations." This is Q-087's **governance-acceptance** candidate: a recorded decision by responsible parties, weighing residual risk, on a controllable date.

## Why mixed, not supporting

It would be easy to file this as support for governance acceptance -- the literature plainly treats stakeholder sign-off as normal and legitimate. But intellectual honesty requires flagging the other half: the *prescriptive ideal* in this same literature is the objective gate, recommended **specifically to remove the subjectivity** that Q-087's resolution admits is governance-acceptance's known failure mode (a judgement-call boundary can drift). So the practitioner consensus simultaneously (a) legitimises the chosen option as ordinary practice and (b) keeps alive the strongest argument for the option Q-087 declined. That is a genuine split, and marking it mixed is the accurate call.

## The condition this literature does not model

There is one respect in which the source's default preference does not even apply to Q-087's situation, and it is the decisive one. Exit-criteria guidance assumes the objective board *can* in principle be turned green -- you keep testing until the thresholds are met. Q-087's operative reason for rejecting the objective gate was that nine closure nodes are blocked and a target date had already slipped, so the green board *may never fire* and would leave GOV-V3FREEZE-1 permanently inert. Standard QA practice never confronts a board that is structurally unsatisfiable, so its "just meet the objective criteria" advice is not available here. This both explains why REE reached a different answer than the practitioner default and bounds how much weight this source can carry.

## Confidence reasoning

Source quality is low (0.35) -- these are commercial guides, not peer-reviewed studies -- which caps the aggregate at 0.45 despite unusually high mapping fidelity (0.80): the sources name Q-087's exact dichotomy in near-identical language. Transfer risk is moderate (product-QA sign-off to governance-substrate-closure). The entry earns its place not by settling the question but by showing that Q-087's tension is a real, named tension in release practice, and by supplying the honest counter-argument (the objective-gate ideal) alongside the supporting one.
