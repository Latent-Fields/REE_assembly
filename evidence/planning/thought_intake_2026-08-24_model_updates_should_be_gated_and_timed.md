# Thought Intake: Model Updates Should Be Gated and Timed

**Date:** 2026-08-25
**Raw thought file:** `docs/thoughts/2026-08-24_model_updates_should_be_gated_and_timed.md`
**Session:** loop-ti-model-gated-3c01c6 (worktree), 2026-08-25

## Verbatim prompt (core proposal)

> REE may need an explicit distinction between receiving information and permitting that
> information to modify a model. A useful minimal decomposition is: **signal -> update
> eligibility -> permitted update -> durable commit**, rather than treating signal arrival as
> equivalent to immediate plasticity... The important architectural requirement is that different
> kinds of change may occur on different schedules. Some provisional state changes should be
> immediate; some learning should accumulate eligibility before being applied; some persistent
> changes may require repeated or independently corroborating evidence; and some deeper
> representational changes may be preferentially permitted during sleep/offline processing. Thus
> REE may require not merely multiple processing timescales, but **multiple plasticity/commit
> timescales**.

The thought is explicitly framed by its own author as **primarily integrative, not a new-mechanism
proposal**: "This may already be partly represented across existing REE mechanisms and claims...
The purpose of this thought is therefore primarily integrative: when the relevant claims are next
processed, ask whether together they provide coherent governance over *when* models are allowed to
change." Its own "Mining instruction" says: inspect the existing claims matrix for ACh/plasticity
gating, neuromodulation, eligibility traces, consolidation/reconsolidation, sleep, precision and
model-update cadence, and "prefer connecting or refining existing claims where they already
instantiate the requirement" before proposing new substrate.

## Answering the thought's own mining question

**Yes -- taken together, existing REE claims already provide a coherent (if not fully unified)
answer to "when are models allowed to change", staged almost exactly as the thought's own
signal -> eligibility -> permitted-update -> durable-commit decomposition.** The clearest single
artifact is `docs/architecture/plasticity_write_authority_gating.md`, whose own table (below) lays
out three sequential, timescale-differentiated layers that are explicitly documented as
"complements, not substitutes":

| Layer (existing doc's own framing) | Grain | Claim(s) |
|---|---|---|
| Window-level plasticity gain (ACh/PV/BDNF learning-rate gain) | global/state, slow | `docs/thoughts/2026-06-01_plasticity_window_neuromodulators.md` (adjacent note, not yet claim-registered itself) + MECH-083 (ACh meta-level plasticity gain) |
| Event-level admission ("does *this* event earn durable write?") | per-event, fast | **MECH-368** (event-level write-authority gate), **MECH-431** (two-factor tag-and-capture eligibility, with an explicit TIME WINDOW) |
| Window closure / crystallization ("when does plasticity lock?") | developmental, slowest | **INV-074**, **MECH-333** (critical-period open phase), **MECH-334** (critical-period closure) |

This is essentially the thought's own pipeline, already built out in more mechanistic detail than
the raw thought proposes, and already stamped with the same "different stages, different
timescales, sequential complements not substitutes" framing the thought is asking REE to check
for.

## What's new vs. existing REE docs/claims (novelty table)

| Thread in the raw thought | Existing REE coverage | Verdict |
|---|---|---|
| "Receiving information" vs "permitting that information to modify a model" as a distinct architectural cut | **MECH-368**: "an event may be salient, real-provenance, and in a write-permitted mode yet still fail the [write-authority] gate." This is the identical cut, already load-bearing (its own doc calls out the "undifferentiated-global-update / catastrophic-interference failure mode" that treating signal arrival as equivalent to plasticity would produce). | Already owned. Cross-ref only. |
| "signal -> update eligibility" stage | **MECH-207** (ACh permissive write-gate on the surprise buffer: "PE alone is necessary but not sufficient... the agent must be in an ACh-permissive state"); **MECH-083** (ACh as meta-level plasticity gain); **MECH-368**'s `f(prediction_error, salience, pathway_state, residue_status, goal_relevance, plasticity_eligibility)`. | Already owned, at both the neuromodulatory-gain layer and the event-admission layer. |
| "some learning should accumulate eligibility before being applied" | **MECH-431**: two-factor tag-and-capture eligibility -- "a local event sets a transient, input-specific eligibility TAG, and a durable... write is consummated only if that tag CAPTURES a separately-gated... signal within a TIME WINDOW." This is a near-verbatim match, already anchored to the synaptic tagging-and-capture literature (Frey & Morris 1997, Redondo & Morris 2011). | Already owned. Cross-ref only. |
| "permitted update" stage (which channels/substrates are even open to write) | **MECH-261** (mode-conditioned write gating: which substrates can write to E3, episodic memory, policy updates, autonomic coupling, keyed on operating mode) and **MECH-094** (provenance/simulation-vs-real write-profile gate). Also **INV-019** (rehearsal traversal and irreversible durable write must remain separated). | Already owned. Cross-ref only. |
| "durable commit" stage, generally | **INV-074 / MECH-333 / MECH-334** (developmental plasticity crystallization: a time-bounded open window, then closure that locks the crystallized state) -- this is the closure/protection half that `plasticity_write_authority_gating.md` explicitly names as the doc's own missing-admission-side complement. | Already owned. Cross-ref only. |
| "durable commit" stage, specifically for privileged/authority-affecting writes | **ARC-020** (offline consolidation protected by typed authority/write boundaries -- a stricter commit gate than an ordinary representational write, though its own non-degeneracy precondition currently fails: no `commit_boundary`/permission-matrix machinery exists in ree-v3 yet). **SD-034** (closure operator: a five-part "done" token that releases the commitment latch, installs No-Go bias, and discharges residue on completion -- a discharge/commit-boundary mechanism in the governance/action domain, distinct from ARC-020's authority-store domain). | Already owned, in two distinct domains (authority-store writes vs. action/residue discharge). Cross-ref only. |
| "some persistent changes may require repeated or independently corroborating evidence" before a deep/durable change | **MECH-511** (registered TODAY, 2026-08-25, by a same-date sibling thought-intake pass on `2026-08-24_compression-decompression-prospective-attractors-barrett-miller-convergence.md`): "Durable ('deep') revision of E1 or a deep attractor should be gated by a LEARNING ELIGIBILITY function of (error, error precision, predicted future/control relevance, organism-or-other consequence, evidence provenance, current mode)... accumulated or structurally important contradiction -> counterfactual reprocessing and possible offline revision." This is close to a verbatim match for this specific clause of the raw thought, arrived at independently the same week via a different source thought. | Already owned (as of today). Cross-ref only -- flagged as the single most load-bearing coincidental convergence found in this pass. |
| "some deeper representational changes may be preferentially permitted during sleep/offline processing" | **MECH-285** (sleep-consolidation priority from V_s residuals: replay order/weight during sleep is biased by accumulated verisimilitude-residual "staleness", not just salience); **MECH-121-124** (NREM SWR replay / spindle packaging / REM precision recalibration, the four sub-phases of offline consolidation, MECH-030 parent); **MECH-249** (ACh/NA balance sets mode-specific hippocampal write profiles across waking/SWS/REM). | Already owned, at the sleep-substrate layer specifically. Cross-ref only. |
| Eligibility with its own bounded time window, in the action-selection (not world-model) domain | **MECH-452** (loop-local eligibility traces under a globally-broadcast dopamine signal) + **ARC-108** (unified dopamine substrate, learned gating) -- a third, independent instance of the same "signal x local eligibility x bounded window" pattern, this time for BG/E3 selection rather than E1/E2 world-model updates or episodic consolidation. | Already owned. Cross-ref only -- cited as evidence the pattern recurs across at least three substrates (world-model MECH-368/431, selection MECH-452/ARC-108, episodic MECH-285) without needing a fourth unifying mechanism. |
| Is an explicit event-level eligibility gate needed at all, or does channel-gating + provenance + consolidation-priority already suffice? | **Q-062** is the pre-registered falsifier for exactly this question, already scoped against MECH-261 + MECH-094 + MECH-285. | Already owned. Cross-ref only. |
| "REE may require not merely multiple processing timescales, but multiple plasticity/commit timescales" (general multi-timescale framing) | **INV-013** (cognition is predictive, iterative, and multi-timescale) and **SD-006** (E1/E2/E3 run at characteristic rates, async multi-rate) already assert multiple *processing* timescales at the architecture-commitment level; the plasticity-specific instances above (window-gain / event-admission / crystallization-closure, plus the three-substrate eligibility-with-window pattern) already give REE multiple *plasticity/commit* timescales in practice. | Already owned in substance; no claim currently states the general "processing timescales != plasticity timescales, and REE needs both" distinction as its own line, but every specific instance the raw thought would motivate is already covered piecemeal (see novelty-table rows above) -- registering a purely restating umbrella claim over an already-dense, already-cited cluster would not survive Step 4's own bar. **Not registered; see "Genuinely new?" below.** |
| "the recently questioned E1/E2/E3 dynamical-timescale separation" | This is `failure_autopsy_V3-EXQ-942_2026-08-21.md` (confirmed 2026-08-21T01:56:34Z): the DESIGNED tick ratio (SD-006, ARC-023) does not match a REALISED persistence-timescale separation at the continuous-representation level -- recomputed half-lives show tau(E1) 4.33 > tau(E2) 3.00 > tau(E3) 2.67, the OPPOSITE of the designed E1<E2<E3 ordering, on two fully-powered seeds independently. Routed `governance-note-only`; INV-013 itself STANDS (it is an existence audit, not a realised-separation measurement, and its own `what_would_answer` explicitly delegates that sharper question to ARC-001/ARC-002/ARC-004). Read-across (not adjudicated) to **ARC-004**, **ARC-023**, **SD-006**; new qid `e-ladder-realised-timescale-separation` was born from the autopsy's own C1 recompute. | Already owned and current (4 days old at ingestion time). This is directly relevant to the raw thought's own closing caveat ("without implying that each requires a new mechanism") -- the finding is a caution about assuming SD-006's CLOCK-level rate separation automatically yields REPRESENTATION-level plasticity-timescale separation; it does not, on this evidence, and that gap is exactly the kind of thing a future coherence check on this cluster should account for. Cross-ref only; this artifact does not itself dispose ARC-004/ARC-023/SD-006. |

## Genuinely new?

**No new claim registered.** Every load-bearing piece of the raw thought's proposed
signal -> eligibility -> permitted-update -> durable-commit decomposition, including the "different
kinds of change on different schedules" requirement, already exists in the registry -- most
concentrated in the dedicated `docs/architecture/plasticity_write_authority_gating.md` home doc
(MECH-368, MECH-431, Q-062, cross-referencing MECH-261, MECH-094, MECH-285, INV-074, MECH-333,
MECH-334), reinforced by a same-day, independently-arrived-at sibling registration (MECH-511) that
supplies almost exactly the "repeated or independently corroborating evidence" clause for the
specific case of deep E1-attractor revision, and by a distinct third instance of the same
eligibility-with-bounded-window pattern in the action-selection domain (MECH-452/ARC-108). This is
a case where the raw thought's own stated purpose -- "ask whether together they provide coherent
governance" -- is best served by pointing at the existing cluster precisely rather than minting an
umbrella claim that would only restate what MECH-368's own doc already says in its "sequential
complements, not substitutes" table. Per the skill's own guidance, this is a complete and
successful ingestion pass, not an incomplete one.

## Key formulations (verbatim, load-bearing)

> REE may need an explicit distinction between receiving information and permitting that
> information to modify a model.

> signal -> update eligibility -> permitted update -> durable commit

> REE may require not merely multiple processing timescales, but multiple plasticity/commit
> timescales.

> This distinction could matter for several existing problems -- competence retention, attractor
> rigidity, threat attribution, sleep-dependent reorganisation and the recently questioned
> E1/E2/E3 dynamical-timescale separation -- without implying that each requires a new mechanism.

## Affected existing claims

No claim's `status`, `confidence`, `epistemic_category`, or evidence record was touched by this
pass. The following are cross-referenced (read-only) as the existing coverage this thought
rediscovers or touches, grouped by pipeline stage:

- **Signal admission / neuromodulatory gain:** MECH-083, MECH-207, MECH-084, MECH-087, MECH-249
- **Update eligibility (event-level, world-model/policy path):** MECH-368, MECH-431, Q-062
- **Update eligibility (selection/action path):** MECH-452, ARC-108
- **Permitted update (channel/mode gating):** MECH-261, MECH-094, INV-019
- **Durable commit (authority-store domain):** ARC-020
- **Durable commit (action/residue discharge domain):** SD-034
- **Durable commit (sleep/offline domain):** MECH-285, MECH-121, MECH-122, MECH-123, MECH-030
- **Deep/durable revision with corroboration requirement (E1-specific):** MECH-511, MECH-512, INV-103 (registered 2026-08-25 by sibling pass, commit `eda8c4a81a`)
- **Multiple processing timescales (architecture-level):** INV-013, SD-006, ARC-004, ARC-023
- **Currently open, adjacent to this cluster:** the 2026-08-21 finding that SD-006's designed clock-rate separation does not (yet, on this evidence) produce a realised representation-level persistence-timescale separation -- read-across only, `evidence/planning/failure_autopsy_V3-EXQ-942_2026-08-21.md`.

Neither `docs/claims/claims.yaml` entries nor the `plasticity_write_authority_gating.md` doc were
edited by this pass; all of the above were read, not modified.

## Next steps

- **No literature pull needed for this pass** -- this is a pure claims-coverage/integration check,
  not new empirical territory; the relevant literature anchors (Frey & Morris 1997, Redondo &
  Morris 2011, Ballarini et al. 2009 for MECH-431; Tononi & Cirelli 2006, Diekelmann & Born 2010,
  Hobson & Friston 2012 for the sleep cluster) are already cited on the existing claims.
- **Left for a future session, not performed here:** `plasticity_write_authority_gating.md`'s own
  table cites `docs/thoughts/2026-06-01_plasticity_window_neuromodulators.md` as the window-level
  layer but that note does not appear to have its own dedicated MECH claim (only MECH-083 stands in
  for the ACh gain piece) -- a future `/thought-ingestion` or `/thought-digestion` pass on that
  2026-06-01 note specifically may be warranted to check whether it needs its own registration or
  is fully subsumed by MECH-083/MECH-368/MECH-431.
- **Left for a future session, not performed here:** whether MECH-368/431's own `notes` should
  gain a cross-reference to this thought (`2026-08-24_model_updates_should_be_gated_and_timed.md`)
  as independent convergent motivation, the way SD-034's design doc already names "the OCD thought
  set" as a prior convergent route. Not done in this pass to avoid amending another claim's record
  without an explicit user steer, per the skill's Step 5 discipline.
- **Version-routing:** not applicable -- no new claim was registered, so there is no V3-vs-V4
  routing decision to make in this pass.
- No threads were left deliberately unregistered pending a closer check; the "attractor rigidity"
  and "threat attribution" items the raw thought lists as candidate beneficiaries of this
  distinction are themselves already covered by MECH-088 (psychiatric four-plane failures, incl.
  OCD as DA-attractor-lock + ACh-gating failure) and MECH-208 (valence-asymmetric replay / threat
  bias) respectively, but neither of those claims was modified here since the raw thought does not
  assert anything new about them beyond "this distinction could matter."
