# Q-096 human-AI surface audit (2026-08-25)

Audit of REE's human-facing surfaces for a structural error-signal channel, in the
style of INV-077's write-path audit but applied to conversational/development-support
surfaces rather than claims.yaml write paths. Per Q-096's `what_would_answer`.

External grounding read for vocabulary (not for an REE-specific answer):
`Latent-Fields/ai-cognitive-failure-taxonomy` (public sibling repo, cloned shallow to
`/tmp/ai-cognitive-failure-taxonomy` for this audit, not part of `REE_Working`) --
`failure_modes/shared_delusional_coupling.md` (AI-AI structural folie-a-deux analogue;
lists "Human-AI pairs in high-trust workflows" as one of five behavioural expressions)
and `docs/psychopathology_interaction.md` (dedicated human-AI coupling doc; "cross-substrate
closed loop" entry: "The chatbot's sycophancy-trained response distribution makes it more
likely to produce outputs consistent with whatever framing the user has introduced... Each
iteration tightens the attractor").

## Method

Traced every REE pipeline step where AI-authored framing (a novelty judgment, a
recommendation, a routing decision) can reach a durable claim/experiment/governance
state change, and checked whether an explicit, independent human-confirmation or
evidence gate sits between the framing and the write -- the same structure INV-077
requires for score -> confidence writes, applied to framing -> belief/state writes.

`AskUserQuestion` call counts per skill (a crude but informative proxy for "does this
pipeline step stop and require a human decision, or does it proceed on the session's
own judgment"):

| Skill | AskUserQuestion count | Writes to claims.yaml? |
|---|---|---|
| `/governance` | 16 | yes (promote/demote/dispose) |
| `/session-land` | 6 | no (chip/report split, claim close) |
| `/thought-digestion` | 3 | yes (falsification/testability updates to existing claims) |
| `/failure-autopsy` | 1 | no directly (feeds governance's Step 4 apply) |
| `/thought-ingestion` | **0** | **yes (registers new `candidate` claims)** |

## Findings

### FINDING 1 (CONFIRMING -- gap is real): `/thought-ingestion` registers new claims
into `claims.yaml` on the strength of a single AI session's own novelty judgment, with
**no interactive confirmation gate anywhere in the skill**.

`/thought-ingestion` (`.claude/skills/thought-ingestion/SKILL.md`) is the skill that
puts a claim in the registry in the first place, from a raw human-written thought.
Its Step 4 ("Cross-reference against claims.yaml before drafting anything") builds a
**novelty table** -- thread / existing coverage / verdict (already-owned, adjacent-but-
distinct, or genuinely new) -- entirely from the session's own `grep` + read of
`claims.yaml`. Step 6 then registers every thread the table calls "genuinely new"
directly into `claims.yaml` (`status: candidate`), and Step 9 says only to **report**
the outcome to the user "what was already owned... what got registered as new..." --
after the commit and push have already landed (Step 8 runs before Step 9). There is no
`AskUserQuestion` call anywhere in the file (grep count: 0), and no step where the
novelty table itself is shown to the user for confirmation before the registration
commit. The skill's own text half-acknowledges the risk without closing it: "A
thought's own confident framing ('REE currently lacks...') is a hypothesis to verify
against `claims.yaml`, not a fact to relay" -- but the verifier named is the *same AI
session*, not an independent check.

This is structurally the gap Q-096 asks about: an AI-authored novelty judgment
(itself downstream of a human's raw, informally-written thought -- exactly the
"AI reconstruction/elaboration" step in the raw thought's own framing) becomes a
durable registry write (a new claim, wired into the dependency graph, visible to every
future `/governance` cycle and every future ingestion's own Step 4 search) without an
intervening human-confirmation or independent-evidence gate. `status: candidate` is
lower-stakes than a promotion (it doesn't drive V3 builds or change confidence), but it
is not inert: a wrongly-scoped or wrongly-"not found" candidate claim shapes what every
subsequent session treats as "already covered" (Step 4's own extraction-beats-invention
logic), so an unverified novelty call propagates forward into later sessions' novelty
tables rather than being caught once.

**Concrete case, found live in this audit's own claim history (not hypothetical):** the
raw thought behind Q-096 itself. Session `responsibility-epistemic-hygiene-d6f9d3`
processed `docs/thoughts/2026-08-12_responsibility_as_epistemic_hygiene.md` via this
exact pipeline on 2026-08-25, registering Q-096 (among others) with a note stating the
raw thought's cited source -- "the Machine Folie a Deux work" -- was searched for in
claims.yaml/*.md and **not found**, and flagged "no REE doc/claim found under that
name" as a next-step. That framing landed in `claims.yaml` (REE_assembly `69f784ae05`)
with no interactive check on the "not found" claim. Fourteen minutes later a second
session (`responsibility-epistemic-hygiene-...` closing at `20:16:42Z`, commit
`b5b7a41da9`) corrected it: the user had recognised the reference as the public sibling
repo `Latent-Fields/ai-cognitive-failure-taxonomy`, outside `REE_Working` entirely, and
supplied the correction. **The correction happened only because the user happened to
already know the source material and volunteered it** -- nothing in the ingestion
pipeline required the "not found" framing to be checked before it was committed, and a
user who did not independently know the reference would have had no structural prompt
to question it. This is the NON-DEGENERACY PRECONDITION's "at least one identifiable
case where a human user's uncorrected acceptance of AI-generated elaboration ...
without an intervening independent check" -- satisfied by REE's own claim history, not
a constructed hypothetical. (In this instance the human *did* catch it, which is the
favorable outcome, not evidence against the gap: the pipeline offers no mechanism that
would have caught it had the human not already known.)

### FINDING 2 (partial mitigation, not a closed gate): `/governance`'s promotion/
demotion path IS interactively gated, but the gate's own instrument shows it does not
fully close the sycophancy risk.

Unlike thought-ingestion, `/governance` Step 2 ("Walk pending experiments") and Step 3
("Surface the promotion/demotion agenda") are both explicitly marked INTERACTIVE and
both use `AskUserQuestion` before any claims.yaml disposition is applied (16 call sites
across the skill; Step 3: "CRITICAL: After presenting, use AskUserQuestion to get the
user's decisions on each recommendation before proceeding"). This is a real, structural
difference from Finding 1 -- INV-077's bar (explicit human confirmation before a
confidence-bearing write) is met at the mechanism level here.

But the confirmation is only as independent as the human's actual engagement with an
AI-authored recommendation, and REE's own tooling already treats this as an open
question rather than a solved one: the umbrella `CLAUDE.md` "Recommendation-Agreement
Ledger" instructs logging, after every `AskUserQuestion` call that marks an option
`(Recommended)`, whether the user's actual selection matched the recommendation
(`scripts/record_recommendation_outcome.py`) -- explicitly "the audit trail behind any
future decision to grant an automation ... authority to act on Claude's judgment
without asking first," and explicitly self-reported rather than hook-enforced. This is
evidence REE has already identified the "does the human meaningfully interrupt the
recommendation, or just ratify it" question as unresolved and is instrumenting it
rather than assuming the `AskUserQuestion` stop itself is sufficient. No finding here
that the gate is broken -- only that its own audit instrument confirms the deeper
question (rubber-stamp rate) is still open, which is consistent with Q-096's framing
that a *soft*, unaudited path can coexist with a formally-interactive one.

### FINDING 3 (existing mitigation, different axis): literature/experimental evidence
decoupling addresses a related but distinct failure mode, not this one.

The standing rule (`feedback_lit_exp_decoupled`, cited in `/thought-ingestion` Step 6:
"a paper resembling REE does not strengthen any existing claim's confidence") keeps two
EVIDENCE signal classes non-collapsible, in the same spirit as INV-077's WORLD/EVIDENCE/
GOVERNANCE typing. It prevents an AI session from treating literature corroboration as
if it were independent experimental confirmation. It does **not** address the
human-AI framing-acceptance loop Q-096 asks about (an AI's own elaboration being
accepted by the human without correction) -- it is a same-taxonomy sibling mitigation,
not a covering one. Listed here because Q-096's prompt named it as a candidate existing
gate; it should not be read as closing Finding 1.

### FINDING 4 (lower-stakes, noted not analyzed in depth): `/session-land`'s "chip
everything else" default is a scope/execution decision, not a confidence-bearing one.

`/session-land`'s Phase 3 chip-vs-report split is governed by a standing CLAUDE.md rule
the session applies to itself (0 `AskUserQuestion` calls gate this specific split,
though the skill has 6 total for other steps). This shapes what work gets queued, not
what a claim's status or evidence direction is -- out of scope for INV-077's "confidence
update" framing and Q-096's "claim/experiment/governance decision" framing. Noted for
completeness; not pursued further here.

## Answer to Q-096's `what_would_answer`

**CONFIRMING -- the generalization holds; a real, identified gap exists.** REE's
evaluation-channel-integrity discipline (INV-077) is well-enforced for the write paths
it was scoped to (automated writers, governance's promotion/demotion path). It does
**not** yet generalize to `/thought-ingestion`'s claim-registration path, which lets a
single AI session's own novelty judgment reach `claims.yaml` with zero interactive
confirmation and only a post-hoc report -- structurally the same "self-generated signal
mistaken for independent confirmation" pattern INV-077 forbids for confidence fields,
here operating on claim *existence and framing* instead. The gap is not hypothetical:
this audit found a concrete instance in REE's own claim history (Q-096's own
registration, corrected only because the human happened to already know the source).

This is **not** a call to gate every ingestion pass behind a blocking confirmation --
`status: candidate` is deliberately low-stakes and the skill's asynchronous, high-volume
design (backlog of raw thoughts) is a reasonable tradeoff. The finding is narrower: the
gap should be named explicitly (as this note does) rather than assumed closed by
`/governance`'s downstream gate, since a wrongly-framed candidate can propagate through
several ingestion passes' own novelty checks before ever reaching a `/governance` cycle
that might catch it -- and `/governance`'s promotion/demotion gate is itself confirmed
interactive but only partially audited for whether that interaction is substantively
independent (Finding 2).

## Suggested follow-on (reported, not chipped -- see CLAUDE.md Session Land Protocol
chip-exception rule; this is a `/governance`-adjacent framing question, appropriate for
governance to decide disposition on, not a unilateral process change from this audit)

- Consider whether `/thought-ingestion` Step 6 should show the novelty table (not just
  the final report) to the user before the claims.yaml commit, at least for threads
  the session itself scored as "genuinely new" (the already-owned / cross-ref-only
  threads are lower risk since they add no new registry surface).
- Consider extending the Recommendation-Agreement Ledger's self-reported rubber-stamp
  tracking to cover thought-ingestion's novelty verdicts, not only `AskUserQuestion`
  `(Recommended)` options -- the two are structurally the same "AI framing accepted or
  corrected" measurement, applied to a currently-uninstrumented path.
