---
nav_exclude: true
---

# Thought Intake: Behavioural Adjudication as a Scientific Skill for REE Assembly

**Raw thought file:** `docs/thoughts/2026-08-11_behavioural_adjudication_scientific_skill_working_thought.md`
**Session:** jovial-shannon-35d300, 2026-08-12
**Status:** processed, claim registered (GOV-BEHADJ-1, explicitly provisional)

---

## Verbatim prompt

See the raw thought file for the full text (a long, deliberately provisional working thought).
Core reframing, condensed: "we never needed a ruler, we needed an umpire." Recent Fishtank
visual observations (coherent reef use, post-sleep behaviour looking "smoother") may be
genuine, or may be perceptual artefact/stochastic variation -- the challenge is not finding a
number that confirms what the observer believes they saw, but constructing an umpire that
adjudicates among competing explanations using multiple observations, perturbations, controls,
and predictions. Proposes: a three-level separation (Observation / Interpretation / Mechanism,
each independently falsifiable); behaviour as structured process (motifs, states, transitions)
rather than aggregate totals; parallel hypothesis-directed AND discovery-oriented analysis;
variability treated as potentially adaptive/structured, not default noise; discriminating
perturbations (positive, destructive, orthogonal negative control) preferred over additional
metrics; strict discovery/confirmation separation (exploratory observation -> formalised
hypothesis -> pre-specified predictions -> unseen runs -> adjudication), with blinding of
condition labels where practical; invariance tested at the correct level (surface behaviour vs.
functional organisation vs. mechanism); an explicit anti-Goodharting checklist. A tentative
11-step workflow is sketched (Observe/Preserve/Compete/Predict/Perturb/Blind/Measure/Discover/
Adjudicate/Replicate/Generalise). A long list of literatures to mine is provided (ethology,
movement ecology, behavioural neuroscience, motor control, comparative psychology, RL,
dynamical systems, causal inference, open science/metascience, psychometrics, evolutionary
biology, robotics), with explicit instruction to search for methods that CONTRADICT the
proposed workflow, not just supporting citations.

---

## What's New vs. Existing REE Docs (novelty table)

| Existing doc/claim | What it already covers | What this thought adds |
|---|---|---|
| `Q-092` (registered same week, `docs/thoughts/2026-08-11_behavioural_diversity_umpire.md`) | The SAME "umpire, not ruler" reframing, but scoped narrowly to one concrete measurement instrument: a held-out, permutation-tested classifier over trajectory-segment features, distinguishing SD-054 reef-ON vs. reef-OFF conditions. | **Generalises the reframing from one instrument to a standing methodology** applicable to ANY organism-level behavioural claim, not only the reef case -- the three-level Observation/Interpretation/Mechanism separation, the discovery/confirmation discipline, and the anti-Goodharting checklist are new content Q-092 does not itself carry. |
| `GOV-FAILLOC-1` (registered 2026-08-09, same shape of thought) | A four-bucket failure-location triage discipline for failure autopsy (REE failed / mechanism failed / measures failed / environment failed). | **Structurally the nearest precedent, not a duplicate**: both are working thoughts that found an existing REE-Assembly adjudication process under-discriminating and propose an explicit triage/workflow fix. GOV-FAILLOC-1 is about POST-HOC failure classification; this thought is about experiment DESIGN and interpretation more broadly (applies to organism-level PASS reads too, not only failures). |
| `.claude/skills/failure-autopsy/SKILL.md` | An existing REE-Assembly skill with a comparable shape (structured adjudication workflow, demotion gates, non-degeneracy guards) for experimental FAILURES specifically. | Confirms the precedent for turning a working thought like this into a formal skill exists and has already been exercised once (GOV-FAILLOC-1 -> SKILL.md Step 5/7). No existing skill covers behavioural-experiment DESIGN and INTERPRETATION generally (as opposed to failure classification specifically). |

**Net assessment:** genuinely new as a **methodology proposal**, and explicitly, by the
thought's own framing, NOT ready to be treated as settled. The core reframing phrase ("umpire,
not ruler") is shared with Q-092 by design (this thought is an explicit generalisation of it),
not independent duplication.

---

## Key formulations (preserved for eventual skill drafting)

1. Three-level separation: Observation / Interpretation / Mechanism, each may be wrong
   independently of the others.
2. Behaviour as structured process (motifs, bouts, states, transitions, sequences), not
   aggregate output -- two agents can match on occupancy/reward totals while differing
   substantially in behavioural strategy.
3. Hypothesis-directed AND discovery-oriented analysis in parallel ("what behavioural structure
   is present that we did not think to measure?").
4. Variability is not automatically noise -- ask whether randomness is differently organised,
   not merely reduced.
5. Behavioural observations should generate explicit competing rival explanations before any
   mechanism is favoured.
6. Discriminating perturbations (what should preserve/break/leave-irrelevant the pattern under
   each rival explanation) preferred over additional descriptive metrics.
7. Discovery and confirmation kept structurally distinct: exploratory observation ->
   formalised hypothesis -> pre-specified predictions -> unseen runs -> adjudication. REE's
   computational nature makes blinding condition labels during scoring cheap.
8. Visual/naturalistic observation remains legitimate evidence for generating hypotheses; it
   does not confirm itself.
9. Invariance must be tested at the correct level: surface behaviour vs. functional
   organisation vs. mechanism are not the same, and a changed surface trajectory that preserves
   functional organisation is stronger evidence for strategy than literal route repetition.
10. Tentative workflow: Observe -> Preserve -> Compete -> Predict -> Perturb -> Blind -> Measure
    -> Discover -> Adjudicate -> Replicate -> Generalise.
11. Explicit anti-Goodharting checklist: what does this metric index; what else could move it;
    could it improve while the real phenomenon worsens or vice versa; what perturbation would
    distinguish the intended interpretation from metric gaming.
12. Candidate literatures to mine (see raw thought "Possible scientific domains to mine" for
    the full list) -- instruction to search for CONTRADICTING methods and known failure modes,
    not only supporting citations.

---

## Affected existing claims

`Q-092` -- unaffected in status; this thought is its generalisation, not a revision.
`GOV-FAILLOC-1` -- unaffected in status; cited as the structural precedent for turning a
working thought like this into a formal skill.
`.claude/skills/failure-autopsy/SKILL.md` -- unaffected; cited as the existing pattern
(triage discipline formalised from a working thought) this proposal would follow if hardened.

No existing claim's evidence, status, or confidence is altered by this intake.

---

## Candidate claims

**REGISTERED as GOV-BEHADJ-1** (2026-08-12), status `candidate`, explicitly marked provisional
in its own `notes` field per the source thought's framing. Full text in
`docs/claims/claims.yaml#GOV-BEHADJ-1`.

No other candidate claims were identified; this thought is a single methodology proposal, not
a bundle of independent claims.

---

## Next steps

1. GOV-BEHADJ-1 registered as `candidate`; NOT to be treated as evidence the methodology works
   -- per `GOV-HELDOUT-1`'s own discipline (which this claim's `what_would_answer` explicitly
   invokes), promote only after real use on >=1 organism-level behavioural claim, and record
   whether it changed the adjudication outcome.
2. **Chipped (not performed in this intake pass):** a `/lit-pull` literature-mining pass across
   the domains the raw thought names (ethology/computational ethology, movement ecology,
   behavioural neuroscience, motor control, comparative psychology, RL, dynamical systems,
   causal inference/experimental design, open science/metascience, psychometrics, evolutionary
   biology, robotics), explicitly searching for methods that CONTRADICT parts of the proposed
   workflow and known failure modes in behavioural classification, not merely supporting
   citations -- per the raw thought's own "Literature mining should seek methods, not merely
   citations" section.
3. Skill formalisation into `.claude/skills/` is downstream of the lit-pull and is not started
   in this pass.
